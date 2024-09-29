""" ALKIŞ VE GÜLEN SURAT EMOJİSİ İÇİN ÖRNEKLER """

from selenium import webdriver
from selenium.webdriver.common.by import By
import time

option = webdriver.ChromeOptions()
driver = webdriver.Chrome(options = option)
driver2 = webdriver.Chrome(options = option)

driver.get('https://www.youtube.com/watch?v=2Y1NCgt7O2M&lc=Ugx-eMoZXztQsFsDwmx4AaABAg')
driver2.get('https://m.youtube.com/watch?v=BHBn7Zm1nR8&pp=ygUOZW4ga29taWsgdmlkZW8%3D')

time.sleep(5)

""" TEPKİKOLİK DOKTORLAR VİDEOSU """
doktorlar = []
doktorlar_comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")
driver.execute_script("window.scrollTo(0,700)")
time.sleep(5)

print(str(len(doktorlar_comments)) + " adet doktorlar yorumu başarıyla çekildi")
for i in doktorlar_comments:
    doktorlar.append(i.text)

counter = 0
final = driver.execute_script("return document.documentElement.scrollHeight")
while True:
    if counter > 3 :
        break
    driver.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    time.sleep(5)
    new = driver.execute_script("return document.documentElement.scrollHeight")
    if final == new :
        break
    final = new
    counter += 1
    doktorlar_comments = driver.find_elements(By.CSS_SELECTOR, "#content-text")
    time.sleep(5)
    print(str(len(doktorlar_comments)) + " adet doktorlar yorumu başarıyla çekildi")
    for i in doktorlar_comments:
        doktorlar.append(i.text)

number = 1
with open("doktorlar.txt", "w", encoding="UTF-8") as file :
    for a in doktorlar :
        file.write(f"{number} - {a}\n")
        number += 1
print("Yorumlar doktorlar.txt dosyasına başarı ile kaydedildi")
driver.quit()

""" MERT GÜLTAŞ GÜLMEME CHALLANGE """
challange = []
challenge_comments = driver2.find_elements(By.CSS_SELECTOR, "#content-text")
driver2.execute_script("window.scrollTo(0,700)")
time.sleep(10)

print(str(len(challenge_comments)) + " adet gülmeme challange yorumu başarıyla çekildi")
for i in challenge_comments:
    challange.append(i.text)

counter2 = 0
final2 = driver2.execute_script("return document.documentElement.scrollHeight")
while True:
    if counter2 > 3 :
        break
    driver2.execute_script("window.scrollTo(0,document.documentElement.scrollHeight)")
    time.sleep(5)
    new2 = driver2.execute_script("return document.documentElement.scrollHeight")
    if final2 == new2 :
        break
    final2 = new2
    counter2 += 1
    challenge_comments = driver2.find_elements(By.CSS_SELECTOR, "#content-text")
    time.sleep(5)
    print(str(len(challenge_comments)) + " adet gülmeme challange yorumu başarıyla çekildi")
    for i in challenge_comments:
        challange.append(i.text)

number2 = 1
with open("challenge.txt", "w", encoding="UTF-8") as file :
    for a in challange :
        file.write(f"{number2} - {a}\n")
        number2 += 1
print("Yorumlar challenge.txt dosyasına başarı ile kaydedildi")
driver2.quit()