#!/usr/bin/env python
# coding: utf-8

# In[1]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
import pandas as pd 
import time

service=Service(ChromeDriverManager().install())
driver=webdriver.Chrome(service=service)
driver.get("https://www.scrapingcourse.com/button-click")
wait=WebDriverWait(driver, 10)

while True:
    try:
        load_more=wait.until(EC.element_to_be_clickable((By.ID,"load-more-bun")))
        driver.execute_script("arguments[0].click();",load_more)
        time.sleep(2)
    except:
        print("No more load button.")
        break

products=driver.find_elements(By.CLASS_NAME,"product-item")
names=[]
prices=[]
for product in products:
    name=product.find_element(By.CLASS_NAME,"product-name").text
    price=product.find_element(By.CLASS_NAME,"product-price").text
    names.append(name)
    prices.append(price)

df=pd.DataFrame({"Product Name":names,"Price":prices})
df.to_csv("load_more_products.csv",index=False)
print("Done")
print("Total products:",len(names))
driver.quit()


# #loop ek he bar click ho raha tha is lya 12 product ka output aya ab code change krte ha take loop proprely wait kre

# In[3]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
driver=webdriver.Chrome()
driver.get("https://www.scrapingcourse.com/button-click")
wait=WebDriverWait(driver, 10)
while True:
    try:
        load_more=wait.until(EC.element_to_be_clickable((By.ID,"load_more_btn")))


        driver.execute_script("arguments[0].scrollIntoView();",load_more)
        time.sleep(1)
        load_more.click()
        time.sleep(2)
    except:
        print("No more load button.")
        break
products=driver.find_elements(By.CLASS_NAME,"product-item")
names=[]
prices=[]

for product in products:
    name=product.find_element(By.CLASS_NAME,"product-name").text
    price=product.find_element(By.CLASS_NAME,"product-price").text
    names.append(name)
    prices.append(price)
df=pd.DataFrame({"Product Name":names,"Price":prices})
df.to_csv("load_button.csv",index=False)
print("Done")
print("Total Products:",len(names))
driver.quit()


# In[5]:


from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pandas as pd
import time
driver=webdriver.Chrome()
driver.get("https://www.scrapingcourse.com/button-click")
wait=WebDriverWait(driver, 10)
while True:
    try:
        load_more=wait.until(EC.presence_of_element_located((By.ID,"load_more_btn")))


        driver.execute_script("arguments[0].click();",load_more)
        time.sleep(2)
    except:
        print("No more load button.")
        break

time.sleep(3)
products=driver.find_elements(By.CLASS_NAME,"product-item")
names=[]
prices=[]

for product in products:
    names.append(product.find_element(By.CLASS_NAME,"product-name").text)
    prices.append(product.find_element(By.CLASS_NAME,"product-price").text)

print("Total products:",len(names))
df=pd.DataFrame({"Product Name":names,"Price":prices})
df.to_csv("load_button.csv",index=False)
driver.quit()




# In[ ]:




