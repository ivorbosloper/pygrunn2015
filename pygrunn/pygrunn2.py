from flask import Response
from util import get_db_cursor
from app import app

@app.route('/geojson/<bbox>')
def geojson(bbox):
    args = map(float, bbox.split(','))
    with get_db_cursor() as cursor:
        cursor.execute("""select ST_AsGeoJSON(geom) as json, hoofdgrs from soil
                          where geom && ST_MakeEnvelope(%s, %s, %s, %s, 4326)""", args)
        # Insert "properties" element inside geojson string
        features = [row['json'][:-1] + ',"properties" : {"soil": "%s"}}' % row['hoofdgrs']
                        for row in cursor.fetchall()]

    return Response('{"type": "FeatureCollection", "features": [%s]}' % ','.join(features),
                    status=200, mimetype='application/json')

