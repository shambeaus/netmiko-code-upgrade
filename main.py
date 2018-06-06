# device details

import csv
import pprint
import shared

saved = {}

def code_upgrade():


    csv_file = input('local CSV name :')
    image_file = input('Source image name :')

    print('proceed with copying code to devices [Y/n}')
    resp = input()

    upload_result = shared.start_upload(csv_file, image_file)

    print(upload_result)


if __name__ == "__main__":
    code_upgrade()