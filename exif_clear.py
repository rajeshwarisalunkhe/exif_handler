import gi
gi.require_version('GExiv2', '0.10')
from gi.repository import GExiv2


def clear_file_data():
    exif = GExiv2.Metadata('img1.jpg')
    exif.clear_exif()
    # exif.clear_xmp()

    exif.save_file()
