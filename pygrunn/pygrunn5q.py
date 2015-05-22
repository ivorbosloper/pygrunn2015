from app import app
from pygrunn.mercator import GlobalMercator

@app.route('/tilep/<int:z>/<int:x>/<int:y>.png')
def tile(z, x, y):
    g = GlobalMercator()
    ymin, xmin, ymax, xmax = g.TileLatLonBounds(x, y, z)

    # not working example yet: draw in PostGIS
    # SELECT ST_AsPNG(ST_AsRaster(
    #     ST_Buffer(ST_Point(1,5),10), 256, 256, '2BUI'));

    return
