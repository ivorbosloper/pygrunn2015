This soil data is part of an open data set distributed by rvo (rvo.nl).
It describes the regulatory soil type.

The AHN data is part of ahn.nl

See atom feed for links: http://geodata.nationaalgeoregister.nl/ahn1/atom/ahn1_5m.xml
Downloaded file: http://geodata.nationaalgeoregister.nl/ahn1/extract/ahn1_5m/07gn1.tif.zip

> gdalwarp -overwrite -s_srs EPSG:28992 -t_srs EPSG:3857 07gn1.tif 07gn1_3875.tif 
> gdal_translate -of GTIFF -a_nodata 0 07gn1_3875.tif ../static/07gn1_3875.png
> gdaldem color-relief 07gn1_3875.tif -of PNG color_ramp.txt ../static/07gn1_3875_rgb.png
