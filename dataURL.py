import os

class DataURL:

  dataFile = "dataURL.txt"

  def __init__(self):
    fileTest = open(self.dataFile, 'a')
    fileTest.close()

  def dataWrite(self):
    dataOpen = open(self.dataFile, 'a')
    siteURL = input("Site adresini ön eki ile birlikte giriniz: ")

    kontrolHTTP = siteURL[:7]
    kontrolHTTPS = siteURL[:8]
    if kontrolHTTP == 'http://' or kontrolHTTPS == 'https://':
      print('Adres girişi kaydedildi!')
    else:
      print('Ön giriş hatalı,lütfen tekrar deneyiniz!')

    dataOpen.write(siteURL + "\n")
    dataOpen.close()

  def dataRead(self):
    dataOpen = open(self.dataFile, 'r')
    if os.stat(self.dataFile).st_size == 0:
      print('Kaydedilmiş adres yok!')
    else:
      print('Kaydedilmiş adresler mevcut!')
    for dataShow in dataOpen:
      print(dataShow)
    dataOpen.close()