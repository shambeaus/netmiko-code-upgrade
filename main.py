import shared
import os
import pprint


def code_upgrade():
    csv_file = input('local CSV name :')
    image_file = input('Source image name :')

    print('proceed with copying code to devices [Y/n}')
    resp = input()

    print('initiating file transfer to devices')
    upload_result = shared.start_upload(csv_file, image_file)

    print('file upload results')

    pprint.pprint(upload_result)


if __name__ == "__main__":
    code_upgrade()
