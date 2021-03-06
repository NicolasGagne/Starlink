import datetime

def aim_date_correction():
    check_date = datetime.datetime(year=2018,month=10,day=11,hour=9,minute=1)
    now = datetime.datetime.utcnow()
    # 168 day winter edition
    # 196 day summer edition
    y = 168 + 196

    while(True):
        if now < check_date + datetime.timedelta(days=168):
            year = check_date.year
            version = 2
            break

        elif now < check_date + datetime.timedelta(days=y):
            year = check_date.year + 1
            version = 1
            break
        else:
            check_date = check_date + datetime.timedelta(days=y)
    return str(year) + '-' + str(version)

ARINC_LOGIN_URL = "https://direct.arinc.net/ADC/Login/Login"
ARINC_CREDIENTIAL = {'username': 'ngagne', 'password': 'BAS922794'}
AIM_CREDIENTIAL = {'username': 'Starlink', 'password': 'Starlink1'}
ARINC_DOC_URL = "https://direct.arinc.net/ADC/ADCContext/DocumentManagement"

NAV_CANADA_LOGIN_URL = "https://checkout.na3.netsuite.com/c.1063417/checkout-2-05-0/index.ssp?is=login&origin=defaultbehavior&whence=#login-register"
NAV_CANADA_DOWNLOAD_PAGE = "https://checkout.na3.netsuite.com/app/site/hosting/scriptlet.nl?script=12&deploy=1&compid=1063417&custpage_sel_lang=en_CA&whence="
NAV_CANADA_CREDIENTIAL = {'email': 'yquellais@hotmail.com',
                          'password': 'star9025',
                          }



AIP_URL = {
    'AIP_GEN_ENG': "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_1_gen/1gen_eng.pdf",
    'AIP_ENR_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_2_enr/2enr_eng.pdf",
    'AIP_AD_ENG': "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_3_ad/3ad_eng.pdf",
    'AIP_SUP_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_4_aip_sup/4aip_sup_eng.pdf",
    'AIP_AIC_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Current/part_5_aic/5aic_eng.pdf",
    'NEXT_AIP_GEN_ENG': "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Next/part_1_gen/1gen_eng.pdf",
    'NEXT_AIP_ENR_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Next/part_2_enr/2enr_eng.pdf",
    'NEXT_AIP_AD_ENG': "http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Next/part_3_ad/3ad_eng.pdf",
    'NEXT_AIP_SUP_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Next/part_4_aip_sup/4aip_sup_eng.pdf",
    'NEXT_AIP_AIC_ENG':"http://www.navcanada.ca/EN/products-and-services/Documents/AIP/Next/part_5_aic/5aic_eng.pdf",
    }

AIM_URL = "http://www.tc.gc.ca/media/documents/ca-publications/AIM_" + aim_date_correction() + "_EN-ACCESS.pdf"

AA_URL = "http://laws-lois.justice.gc.ca/PDF/A-2.pdf"

URL_CHROMEDRIVER = "https://chromedriver.storage.googleapis.com/2.42/chromedriver_win32.zip"
