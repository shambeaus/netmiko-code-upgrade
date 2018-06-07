upload_response = {'192.168.1.221': {'file_exists': True,
                   'file_transferred': False,
                   'file_verified': True},
 '192.168.1.222': {'file_exists': True,
                   'file_transferred': False,
                   'file_verified': True}}

successful

for k,v in upload_response.items():
    print(k)
    print(v)