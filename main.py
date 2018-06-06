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








#USER = 'cisco'
#PASSWORD = os.getenv('ciscopass')
#device_details = {'device_type': 'cisco_asa',
#                  'username': USER,
#                  'password': PASSWORD,
#                  'verbose': False}
#
## File details
#
#source_file = 'test.txt'
#dest_file = 'codefile.bin'
#file_system = 'disk0:'
#direction = 'put'
#
#device_ips = ['192.168.1.76', '192.168.1.79']

if __name__ == "__main__":
    code_upgrade()