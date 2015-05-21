from flask import Response
from util import get_db_cursor

from PIL import Image, ImageDraw
from cStringIO import StringIO
from app import app

OPACITY = int(0.4 * 256)
COLORS = {'ZAND': (0xff, 0xff, 0xC7),
          'KLEI': (0x87, 0xB6, 0x80),
          'VEEN': (0xFA, 0xD6, 0x80),
          'XXX':  (0x85, 0x62, 0x4C)}

@app.route('/image_overlay/<bbox>/<int:xsize>/<int:ysize>')
def image_overlay(bbox, xsize, ysize):
    xmin, ymin, xmax, ymax = map(float, bbox.split(','))
    return get_image(xmin, ymin, xmax, ymax, xsize, ysize)

def get_image(xmin, ymin, xmax, ymax, xsize, ysize):
    xscale, yscale = xsize / (xmax - xmin), ysize / (ymax - ymin)
    image = Image.new("RGBA", (xsize, ysize))
    draw = ImageDraw.Draw(image)
    with get_db_cursor() as cursor:
        cursor.execute("""select ST_AsTEXT(geom) as txt, hoofdgrs from soil
                          where geom && ST_MakeEnvelope(%s, %s, %s, %s, 4326)""",
                       (xmin, ymin, xmax, ymax,))

        for row in cursor.fetchall():
            polygons = row['txt'][len('POLYGON(('):-len('))')].split('),(')
            for index, polygon in enumerate(polygons):
                coords = [map(float, p.split(' ')) for p in polygon.split(',')]
                scaled_polygon = [((x - xmin) * xscale, ysize - (y - ymin) * yscale) for (x, y) in coords]
                if index == 0:
                    options = {
                       'fill': COLORS[row['hoofdgrs']] + (OPACITY,),
                       'outline': COLORS[row['hoofdgrs']]}
                else: # subtract inner polygons (holes) from outer polygon
                    options = {'fill': (255, 255, 255, 0)}
                draw.polygon(scaled_polygon, **options)
    buf = StringIO()
    image.save(buf, format='PNG')
    return Response(buf.getvalue(), content_type="image/png")
