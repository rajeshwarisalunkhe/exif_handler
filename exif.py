import gi
gi.require_version('GExiv2', '0.10')
from gi.repository import GExiv2
from exif_print import print_file
from exif_edit import edit_file
from exif_clear import clear_file_data


def main():

    exif = GExiv2.Metadata('img1.jpg')

    while(True):
        print("Press 1 to print exif data")
        print("Press 2 to edit exif data")
        print("press 3 to clear all data")
        print("press 4 to Show all data")
        print("Press 5 to exit")
        choice = int(raw_input("Enter your choice:"))
        print("\n")
        if(choice == 1):
            # to print all available tags print exif.get_exif_tags()
            print_file(exif)
        elif(choice == 2):
            number = int(raw_input("Enter the number of the field need to be edited"))
            edit_file(number)
        elif(choice == 3):
            clear_file_data()
        elif(choice == 4):
            _show_all_exif('img1.jpg')
        elif(choice == 5):
            print"Exiting..."
            break
        print("\n")


def _show_all_exif(filepath):
    """
    Displays all exif data of input file
    """
    exif = GExiv2.Metadata(filepath)
    # import pdb
    # pdb.set_trace()
    for data in exif.get_exif_tags():
        print '%s : %s' % (data.split('.')[-1], exif[data])

if __name__ == '__main__':
    main()
