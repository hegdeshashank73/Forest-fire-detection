from gmplot import gmplot
import PIL.ExifTags
import keyword
import PIL.Image
from matplotlib.pyplot import flag
from pyrsistent import v

img = PIL.Image.open("sample.jpg")
img1 = PIL.Image.open("sample1.jpg")
img2 = PIL.Image.open("sample2.jpg")


exif = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img._getexif().items()
    if k in PIL.ExifTags.TAGS



}
exif1 = {
    PIL.ExifTags.TAGS[k]: v
    for k, v in img1._getexif().items()
    if k in PIL.ExifTags.TAGS



}

exif['GPSInfo']
north = exif['GPSInfo'][2]
east = exif['GPSInfo'][4]

lat = ((((north[0]*60) + north[1])*60) + north[2])/60/60

long = ((((east[0]*60) + east[1])*60) + east[2])/60/60

lat, long = float(lat), float(long)


gmap.marker(lat, long, "cornflowerblue")
exif1['GPSInfo']
north1 = exif1['GPSInfo'][2]
east1 = exif1['GPSInfo'][4]

lat1 = ((((north[0]*60) + north[1])*60) + north[2])/60/60

long1 = ((((east[0]*60) + east[1])*60) + east[2])/60/60

lat1, long1 = float(lat), float(long)

gmap = gmplot.GoogleMapPlotter(lat, long, 20)

gmap2 = gmplot.GoogleMapPlotter(lat1, long1, 20)
gmap.marker(lat, long, "red")
gmap.marker(11.749486239153919, 76.50154335598731, "cornflowerblue")
gmap.draw("location.html")
