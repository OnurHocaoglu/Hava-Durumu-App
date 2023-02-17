from selenium import webdriver
from bs4 import BeautifulSoup
import time
import datetime



class Havadurumu:

    def __init__(self):

        self.browserProfile = webdriver.ChromeOptions() # Chrome !! Chrome:	https://chromedriver.chromium.org/downloads
        self.browserProfile.add_experimental_option('prefs', {'intl.accept_languages': 'tr,tr_TR'}) # TR dili
        self.browser = webdriver.Chrome('chromedriver.exe', chrome_options=self.browserProfile)
        self.url = "https://www.mgm.gov.tr/tahmin/il-ve-ilceler.aspx?il="


    def weather(self,il):

        self.browser.get(self.url+il)
        time.sleep(1)
        kaynak = self.browser.page_source # Kaynak kod
        bs_soup = BeautifulSoup(kaynak,"html.parser") # Beautifulsoup ile parse
        convert = bs_soup.find("div",{"class":"anlik-durum"})
        return convert




havadurumu = Havadurumu()
time.sleep(2)

print("""
***********************************************************
*********************ANLIK HAVA DURUMU*********************
***********************************************************
""")

# Kullanıcıdan Bilgi Alma

il = input("İli Yazınız: ").lower()

search = havadurumu.weather(il)

# Etiketler
temperature = search.find("div",{"class":"anlik-sicaklik-deger ng-binding"}).text
weather = search.find("div",{"class":"anlik-sicaklik-havadurumu-ikonismi ng-binding"}).text
damp = search.find("div",{"class":"anlik-nem-deger-kac ng-binding"}).text

# Ekrana Yazdırma
print(f"--------{il.upper()} İlinin Hava Durumu--------\nAnlık Durum: {datetime.datetime.now()}\nAnlık Sıcaklık: {temperature}\nAnlık Hava Durumu: {weather}\nNem Değeri: %{damp}")


# Coded By Onurhocaoglu
# https://www.onurhocaoglu.com





