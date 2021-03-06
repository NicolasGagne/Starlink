

import requests

def download_aip(aip_url, temp_dir):
    print('AIP downloading...')
    for key, value in aip_url.items():
        responce = requests.get(value)
        with open(temp_dir + "/" + key + '.pdf', 'wb') as file:
            file.write(responce.content)
    print('AIP download completed.')

def download_aim(aim_url, temp_dir):
    print('AIM downloading...')
    print("ULL", aim_url)
    responce = requests.get(aim_url)
    with open(temp_dir + "/Aeronautical_Information_Manual_(AIM)" + '.pdf', 'wb') as file:
        file.write(responce.content)
    print('AIM download completed.')



def download_aa(aa_url, temp_dir):
    print('Aeronautic Act downloading...')
    responce = requests.get(aa_url, verify=False)
    with open(temp_dir + "/Aeronautical Act" + '.pdf', 'wb') as file:
        file.write(responce.content)

    print('Aeronautic Act download completed.')
