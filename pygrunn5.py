from pygrunn import app
from pygrunn3 import get_image
from mercator import GlobalMercator

@app.route('/tile/<int:z>/<int:x>/<int:y>.png')
def tile(z, x, y):
    g = GlobalMercator()
    ymin, xmin, ymax, xmax = g.TileLatLonBounds(x, y, z)
    return get_image(xmin, ymin, xmax, ymax, 256, 256)
