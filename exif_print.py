import gi
gi.require_version('GExiv2', '0.10')
from gi.repository import GExiv2


def print_file(exif):
    print"Image Information"
    print("\n")
    print"1.Maker:", exif.get('Exif.Image.Make')
    print"2.Flash:", exif.get('Exif.Photo.Flash')
    print"3.Location:", exif.get('Exif.Image.GPSTag')
    print"4.Date and time:", exif.get('Exif.Photo.DateTimeOriginal')
    print"5.Aperture:", exif.get('Exif.Photo.ApertureValue')
    print"6.Focal Length:", exif.get('Exif.Photo.FocalLength')
    print"7.ISO:", exif.get('Exif.Photo.ISOSpeedRatings')
    print"8.Model:", exif.get('Exif.Image.Model')

