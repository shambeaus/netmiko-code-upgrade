import lib.upload as upload
import os
import sys
import pprint


image_directory = './images/'
csv_directory = './csv/'

def code_upgrade():
    images = os.listdir(image_directory)
    CSVS = os.listdir(csv_directory)

    for files in CSVS:
        print(files)

    print('current CSV files in directory')
    print('---------------------------------')

    for files in CSVS:
        print(files)

    print('---------------------------------')

    csv_file = csv_directory + input('local CSV name :')

    if os.path.isfile(csv_file):
        pass
    else:
        print('CSV file does not exist in directory')
        sys.exit(1)


    print('current files in images directory')
    print('---------------------------------')
    for image in images:
        print(image)

    print('---------------------------------')

    image_file = image_directory + input('Source image name :')

    if os.path.isfile(image_file):
        pass
    else:
        print('image file does not exist in directory')
        sys.exit(1)

    print('Image {} will be uploaded to all devices defined in {}'.format(image_file, csv_file))
    print('press enter to confirm and proceed with upload')

    run_input = input('Proceed?')

    upload_result = upload.start_upload(csv_file, image_file)

    print('initiating file transfer to devices')


    print('file upload results')

    pprint.pprint(upload_result)


if __name__ == "__main__":
    code_upgrade()
