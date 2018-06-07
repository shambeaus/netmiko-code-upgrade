import shared
import os
import sys
import pprint


image_directory = './images'

def code_upgrade():

    csv_file = input('local CSV name :')

    if os.path.isfile(csv_file):
        pass
    else:
        print('CSV file does not exist in directory')
        sys.exit(1)

    images = os.listdir(image_directory)

    print('current files in images directory')
    print('---------------------------------')
    for image in images:
        print(image)

    image_file = './images/' + input('Source image name :')

    if os.path.isfile(image_file):
        pass
    else:
        print('CSV file does not exist in directory')
        sys.exit(1)


    print('proceed with copying code to devices [Y/n}')


    print('initiating file transfer to devices')
    upload_result = shared.start_upload(csv_file, image_file)

    print('file upload results')

    pprint.pprint(upload_result)


if __name__ == "__main__":
    code_upgrade()
