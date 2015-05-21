# Prepare data

> createdb pygrunn
> psql pygrunn -c "CREATE EXTENSION postgis"
> shp2pgsql -S -w -s 28992:4326 data/soil.shp |psql pygrunn

# Run program

python app.py
