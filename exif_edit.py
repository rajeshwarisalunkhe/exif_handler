import gi
gi.require_version('GExiv2', '0.10')
from gi.repository import GExiv2


def edit_file(number):
    exif = GExiv2.Metadata('img1.jpg')
    import pdb; pdb.set_trace()
    if(number == 1):
        maker = raw_input("Enter the updated maker name:")
        exif['Exif.Image.Make'] = maker
    elif(number == 2):
        flash = raw_input("Enter the updated flash value:")
        exif['Exif.Photo.Flash'] = flash
    elif(number == 3):
        location = raw_input("Enter the updated location:")
        exif['Exif.Image.GPSTag'] = location
    elif(number == 4):
        date_time = raw_input("Enter new date and time in yyyy:mm:dd hh:mm:ss format:")
        exif['Exif.Photo.DateTimeOriginal'] = date_time
    elif(number == 6):
        aperture = raw_input("Enter updated aperture value:")
        exif['Exif.Photo.ApertureValue'] = aperture
    elif(number == 7):
        focal_length = raw_input("Enter updated focal length:")
        exif['Exif.Photo.FocalLength'] = focal_length
    elif(number == 8):
        model = raw_input("Enter updated model name:")
        exif['Exif.Image.Model'] = model

    exif.save_file()
