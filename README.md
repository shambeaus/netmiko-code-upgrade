# netmiko-code-upgrade

This is a test Interactive script to upload code and set boot variables on network devies using netmiko. Scripted is tested on ASAs in GNS3 and only meant for lab environments

## Setup

- python3
- clone repo to local machine
- Setup virtual environment and install packages with pipenv

```
pipenv install
pipenv shell
```

## Features

- imports device information from CSV file
- threaded process for uploading and sending commands to devices

## Usage

- create CSV file with device information in /CSV folder (example 'devices.csv')
- add network device code images to /images folder
- launch run.py interactive prompt to execute copy
- script will scp files to network devices, add boot variable and wr mem

## Network Device requirements

- Device management IP accessible
- SSH acccess configured
- scp must be enabled on device

### ASAv config example

```
interface GigabitEthernet0/0
 nameif outside
 security-level 0
 ip address <outside IP> <MASK>

aaa authentication ssh console LOCAL
aaa authorization command LOCAL
aaa authorization exec LOCAL
ssh scopy enable
ssh <sourceIP> <MASK> outside
ssh timeout 5
ssh version 2
```

## TODO:

- Clean results ouput
- add option to send reboot command to devices to boot into new code
- Test and add required commands for devices other than ASA
- ...

