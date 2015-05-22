from app import app
from util import get_db_cursor
from flask import Response

@app.route('/raster/png')
def get_raster_image():
    with get_db_cursor() as cursor:
        #cursor.execute("select ST_AsPNG(ST_Reclass(rast, '-256-5:1-256', '8BUI')) as img from ahn")
        cursor.execute("""select ST_AsPNG(ST_ColorMap(rast,1, '100% 215 25 28
80% 253 174 97
60% 255 255 191
40% 171 221 164
20% 43 131 186
0% 43 131 186
')) as img from ahn""")

        row = cursor.fetchone()
        img = row['img']
        return Response(img, status=200, mimetype='image/png')
