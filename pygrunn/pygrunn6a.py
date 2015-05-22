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
