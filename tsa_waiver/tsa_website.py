import requests
import json
from bs4 import BeautifulSoup


from tsa_waiver.const import *

def login_tsa_website():
    session = requests.Session()


    login_page = session.get(URL_TSA_LOGIN)


    soup = BeautifulSoup(login_page.text, features="lxml")
    csrf = soup.find(type="hidden")
    print(csrf.__dict__['attrs']['value'])
    TSA_CREDIENTIAL['i_token'] = csrf.__dict__['attrs']['value']

    session.post(URL_TSA_LOGIN, data=TSA_CREDIENTIAL)


    print(session.get("https://waivers.faa.gov/aap/te_pages.p_main"))

    return session


def create_list_input(session):
    responce = session.get(URL_TSA_INT)
    print(responce)

    soup = BeautifulSoup(responce.text, features="lxml")
    id_list = list()
    for input in soup.find_all("input"):
        try:
            print(input.__dict__['attrs']['id'])
            id_list.append(input.__dict__['attrs']['id'])
        except:
            pass

    print(len(id_list))
        #id_list.append(input.__dict__["id"])

def create_new_waiver(session):

    responce = session.get(URL_TSA_INT)
    print(responce)

    soup = BeautifulSoup(responce.text, features="lxml")
    print(soup.find("i_confirmation"))

def read_tsa_waiver_text():

    text = open("tsa_waiver", 'r')
    tsa_waiver_dict = {}
    for line in text:

        try:
            tsa_waiver_dict[line.split(': ')[0][ :-1]] = line.split(': ')[1][ :-1]
        except IndexError:
            pass
            #tsa_waiver_dict[line.split(': ')[0][ :-1]] = None
    print(tsa_waiver_dict)
    return tsa_waiver_dict

def save_draft(session):
    session.get("https://waivers.faa.gov/aap/l_aap.p_waiver_form?i_confirmation=131903")
    payload = read_tsa_waiver_text()
    req = session.post(URL_TSA_SAVE_DRAFT, data= payload)
    # "https://waivers.faa.gov/aap/l_aap.p_waiver_form?i_confirmation=131903"
    print(req)