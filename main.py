import os
import smtplib
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By

chrome_driver=r"C:\developer\chromedriver.exe"
driver=webdriver.Chrome(service=Service(chrome_driver))
driver.get('https://www.amazon.in/BassHeads-225-Super-Extra-Headphones/dp/B01M9C51T9/ref=sr_1_4?sr=8-4')

price= int(driver.find_element(By.XPATH, '//*[@id="corePriceDisplay_desktop_feature_div"]/div[1]/span[3]/span[2]/span[2]').text)

driver.quit()
username= os.getenv('username')
password=os.getenv('password')

if price<400:
    with smtplib.SMTP('smtp.gmail.com', 587) as connection:
        connection.starttls()
        connection.login(user=username, password=password)
        connection.sendmail(
            from_addr=username,
            to_addrs=username,
            msg=f'subject:headphone price {price}\n\n headphone price is now lower than the price you expected'
        )



