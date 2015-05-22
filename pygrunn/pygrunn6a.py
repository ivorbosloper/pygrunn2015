from app import app
from pygrunn3 import get_image
from pygrunn.mercator import GlobalMercator


def get_raster_image(xmin, ymin, xmax, ymax, xsize, ysize):
    cursor.execute("select day, ST_AsPNG(ST_Reclass(geom, '-256-5:1-256', '8BUI')) as img from raster")

@app.route('/raster_tiled/<int:z>/<int:x>/<int:y>.png')
def raster_tiled():
    g = GlobalMercator()
    ymin, xmin, ymax, xmax = g.TileLatLonBounds(x, y, z)
    return get_raster_image(xmin, ymin, xmax, ymax, 256, 256)

    cursor.execute("""select ST_AsPNG(ST_ColorMap(rast,1, '-256 215 25 28
-190 253 174 97
-125 255 255 191
-60 171 221 164
5 43 131 186')) as img from ahn""")
