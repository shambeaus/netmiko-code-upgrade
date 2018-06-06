
import threading
from queue import Queue
import os
from netmiko import ConnectHandler, file_transfer
import csv

def code_upload(devicedict, image_file, output_q):
    output_dict = {}
    hostname = devicedict['host']
    file_system = devicedict.pop('file_system')
    connection = ConnectHandler(**devicedict)
    print('starting file transfer to device: ' + hostname)
    transfer_result = file_transfer(connection,
                                    source_file=image_file,
                                    dest_file=image_file,
                                    file_system=file_system,
                                    direction='put',
                                    overwrite_file=True)
    output_dict[hostname] = transfer_result
    output_q.put(output_dict)


def start_upload(csv_file, image_file):

    upload_result = {}
    output_q = Queue()

    with open(csv_file) as devices:
        devicedict = csv.DictReader(devices)

        for row in devicedict:
            print(row)
            thread = threading.Thread(target=code_upload, args=(row, image_file, output_q))
            thread.start()

    main_thread = threading.currentThread()
    for new_thread in threading.enumerate():
        if new_thread != main_thread:
            new_thread.join()

    while not output_q.empty():
        upload_result.update(output_q.get())

    return upload_result

