# -*- coding: utf-8 -*-
"""
Created on Fri May 31 04:20:28 2019

@author: Sunmarg Das
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:52:02 2019

@author: Sunmarg Das
"""

# -*- coding: utf-8 -*-
"""
Created on Tue May 28 18:47:38 2019

@author: Sunmarg Das
"""


from selenium.webdriver.common.keys import Keys
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import NoSuchElementException
# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# create new instance of chrome in incognito mode
browser = webdriver.Chrome(executable_path=r'C:/Users/Sunmarg Das/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=option)
chrome_path  = r"C:/Users/Sunmarg Das/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
# go to website of interest
browser.get("https://njdg.ecourts.gov.in/njdgnew/index.php")
timeout = 15
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='report_body']/tr[27]/td[4]")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
browser.maximize_window()

path={}
val={}

tag1=browser.find_element_by_xpath("//*[@id='report_body']/tr[17]/td[1]")
time.sleep(3)
x1=str(tag1.text+"-->")
time.sleep(2)
try:
       WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='report_body']/tr[17]/td[3]")))
except TimeoutException:
        print("Timed out waiting for page to load")
        browser.quit()
browser.find_element_by_xpath("//*[@id='report_body']/tr[17]/td[3]/a").click()
time.sleep(5)
row_count1 = len(browser.find_elements_by_xpath("//*[@id='caseDetails_report_body']/tr"))
time.sleep(3)
elm=browser.find_element_by_tag_name('html')
elm.send_keys(Keys.END)
time.sleep(2)
val1={}  
for j in range(1,row_count1+1):
    titles_element = browser.find_elements_by_xpath("//*[@id='caseDetails_report_body']/tr["+str(j)+"]/td[1]")
    values_element = browser.find_elements_by_xpath("//*[@id='caseDetails_report_body']/tr["+str(j)+"]/td[2]/a")
    values = [x.text for x in values_element]
    titles = []
    j=j+1
    for k in titles_element:
        titles.append(k.text)
    for title, value in zip(titles, values):
        print(title + ' : ' + value)
        val1[x1+title]=value
time.sleep(2)        
val.update(val1)
     
    
for m in range(4,11):
    elm.send_keys(Keys.END)
    time.sleep(2)
    try:
        tag2=browser.find_element_by_xpath("//*[@id='caseDetails_report_body']/tr["+str(m)+"]/td[1]")
        time.sleep(3)
        x2=str(tag2.text+"-->")
        time.sleep(3)
        try:
            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='caseDetails_report_body']/tr["+str(m)+"]/td[2]/a")))
        except TimeoutException:
            print("Timed out waiting for page to load")
            browser.quit()
        elm.send_keys(Keys.END)
        time.sleep(2)
        
        browser.find_element_by_xpath("//*[@id='caseDetails_report_body']/tr["+str(m)+"]/td[2]/a").click()
        time.sleep(4)
        
        for e in range(1,4):
            elm.send_keys(Keys.END)
            time.sleep(2)
            if m==3:
                e=2
            ispresent=len(browser.find_elements_by_xpath("//*[@id='example_stateWise_caseDetails_paginate']/span/a["+str(e)+"]"))
            time.sleep(3)
            if(ispresent==1):
                browser.find_element_by_xpath("//*[@id='example_stateWise_caseDetails_paginate']/span/a["+str(e)+"]").click()        
                time.sleep(3)
                row_count2 = len(browser.find_elements_by_xpath("//*[@id='stateWise_caseDetails_report_body']/tr"))
                time.sleep(3)
                val2={}
                for i in range(1,row_count2+1):
                    titles_element = browser.find_elements_by_xpath("//*[@id='stateWise_caseDetails_report_body']/tr["+str(i)+"]/td[1]")
                    values_element = browser.find_elements_by_xpath("//*[@id='stateWise_caseDetails_report_body']/tr["+str(i)+"]/td[2]/a")
                    values = [x.text for x in values_element]
                    titles = []
                    for x in titles_element:
                        titles.append(x.text)
                    for title, value in zip(titles, values):
                        print(title + ' : ' + value)
                        
                        val2[x1+x2+title]=value
                time.sleep(3)
                    
                val.update(val2)
                time.sleep(3)
                for n in range(1,row_count2+1):
                   
                    elm.send_keys(Keys.END)
                    time.sleep(2)
                    try:
                        tag3=browser.find_element_by_xpath("//*[@id='stateWise_caseDetails_report_body']/tr["+str(n)+"]/td[1]")
                        time.sleep(3)
                        x3=str(tag3.text+"-->")
                        try:
                            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='stateWise_caseDetails_report_body']/tr["+str(n)+"]/td[2]/a")))
                        except TimeoutException:
                            print("Timed out waiting for page to load")
                            browser.quit()
                        
                        time.sleep(3)
                        elm.send_keys(Keys.END)
                        time.sleep(2)
                        browser.find_element_by_xpath("//*[@id='stateWise_caseDetails_report_body']/tr["+str(n)+"]/td[2]/a").click()
                        time.sleep(5)       
                        for f in range(1,8):
                            elm.send_keys(Keys.END)
                            time.sleep(2)
                            ispresent=len(browser.find_elements_by_xpath("//*[@id='example_distWise_caseDetails_paginate']/span/a["+str(f)+"]"))
                            time.sleep(3)
                            if(ispresent==1):
                                elm.send_keys(Keys.END)
                                time.sleep(2)
                                browser.find_element_by_xpath("//*[@id='example_distWise_caseDetails_paginate']/span/a["+str(f)+"]").click()        
                                time.sleep(3)
                                row_count3 = len(browser.find_elements_by_xpath("//*[@id='distWise_caseDetails_report_body']/tr"))
                                time.sleep(2)
                                val3={}
                                
                                for i in range(1,row_count3+1):
                                        titles_element = browser.find_elements_by_xpath("//*[@id='distWise_caseDetails_report_body']/tr["+str(i)+"]/td[1]")
                                        values_element = browser.find_elements_by_xpath("//*[@id='distWise_caseDetails_report_body']/tr["+str(i)+"]/td[2]/a")
                                        values = [x.text for x in values_element]
                                        titles = []
                                        for x in titles_element:
                                            titles.append(x.text)
                                        for title, value in zip(titles, values):
                                            print(title + ' : ' + value)
                                            
                                            val3[x1+x2+x3+title]=value
                               
                                val.update(val3)
                                time.sleep(3)
                                for n1 in range(1,row_count3+1):
                                    
                                    try:
                                        elm.send_keys(Keys.END)
                                        time.sleep(2)
                                        tag4=browser.find_element_by_xpath("//*[@id='distWise_caseDetails_report_body']/tr["+str(n1)+"]/td[1]")
                                        time.sleep(3)
                                        x4=str(tag4.text+"-->") 
                                        try:
                                            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='distWise_caseDetails_report_body']/tr["+str(n1)+"]/td[2]/a")))
                                        except TimeoutException:
                                            print("Timed out waiting for page to load")
                                            browser.quit()
                                        time.sleep(3)
                                        elm.send_keys(Keys.END)
                                        time.sleep(2)
                                        browser.find_element_by_xpath("//*[@id='distWise_caseDetails_report_body']/tr["+str(n1)+"]/td[2]/a").click()
                                        val4={}
                                        time.sleep(4)
                                        for r in range(1,8):
                                            elm.send_keys(Keys.END)
                                            time.sleep(2)
                                            ispresent=len(browser.find_elements_by_xpath("//*[@id='example_estCodeWise_caseDetails_paginate']/span/a["+str(r)+"]"))
                                            time.sleep(3)
                                            if(ispresent==1):
                                                elm.send_keys(Keys.END)
                                                time.sleep(2)
                                                browser.find_element_by_xpath("//*[@id='example_estCodeWise_caseDetails_paginate']/span/a["+str(r)+"]").click()        
                                                time.sleep(3)
                                                row_count4 = len(browser.find_elements_by_xpath("//*[@id='estCodeWise_caseDetails_report_body']/tr"))
                                                time.sleep(3)
                                                val4={}
                                                for i in range(1,row_count4+1):
                                                            titles_element = browser.find_elements_by_xpath("//*[@id='estCodeWise_caseDetails_report_body']/tr["+str(i)+"]/td[1]")
                                                            values_element = browser.find_elements_by_xpath("//*[@id='estCodeWise_caseDetails_report_body']/tr["+str(i)+"]/td[2]/a")
                                                            values = [x.text for x in values_element]
                                                            titles = []
                                                            for x in titles_element:
                                                                titles.append(x.text)
                                                            for title, value in zip(titles, values):
                                                                time.sleep(3)
                                                                print(title + ' : ' + value)
                                                                
                                                                val4[x1+x2+x3+x4+title]=value
                                                
                                                val.update(val4)
                                                time.sleep(3)
                                                for n2 in range(1,row_count4+1):
                                                    time.sleep(3)
                                                    elm.send_keys(Keys.END)
                                                    time.sleep(2)
                                                    try:
                                                        tag5=browser.find_element_by_xpath("//*[@id='estCodeWise_caseDetails_report_body']/tr["+str(n2)+"]/td[1]")
                                                        time.sleep(3)
                                                        x5=str(tag5.text+"-->")
                                                        time.sleep(2)
                                                        try:
                                                            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='estCodeWise_caseDetails_report_body']/tr["+str(n2)+"]/td[2]/a")))
                                                        except TimeoutException:
                                                            print("Timed out waiting for page to load")
                                                            browser.quit()
                                                        time.sleep(3)
                                                        elm.send_keys(Keys.END)
                                                        time.sleep(2)
                                                        browser.find_element_by_xpath("//*[@id='estCodeWise_caseDetails_report_body']/tr["+str(n2)+"]/td[2]/a").click()
                                                        
                                                        time.sleep(4)
                                                        for w in range(1,8):
                                                            elm.send_keys(Keys.END)
                                                            time.sleep(2)
                                                            ispresent=len(browser.find_elements_by_xpath("//*[@id='example_regYearWise_caseDetails_paginate']/span/a["+str(w)+"]"))
                                                            time.sleep(3)
                                                            if(ispresent==1):
                                                                elm.send_keys(Keys.END)
                                                                time.sleep(2)
                                                                browser.find_element_by_xpath("//*[@id='example_regYearWise_caseDetails_paginate']/span/a["+str(w)+"]").click()        
                                                                time.sleep(3)
                                                                row_count5 = len(browser.find_elements_by_xpath("//*[@id='regYearWise_caseDetails_report_body']/tr"))
                                                                time.sleep(4)
                                                                val5={}
                                                                for i in range(1,row_count5+1):
                                                                        titles_element = browser.find_elements_by_xpath("//*[@id='regYearWise_caseDetails_report_body']/tr["+str(i)+"]/td[1]")
                                                                        values_element = browser.find_elements_by_xpath("//*[@id='regYearWise_caseDetails_report_body']/tr["+str(i)+"]/td[2]/a")
                                                                        values = [x.text for x in values_element]
                                                                        titles = []
                                                                        for x in titles_element:
                                                                            titles.append(x.text)
                                                                        for title, value in zip(titles, values):
                                                                            print(title + ' : ' + value)
                                                                            
                                                                            val5[x1+x2+x3+x4+x5+title]=value
                                                                
                                                                val.update(val5)
                                                                time.sleep(3)
                                                                for n3 in range(1,row_count5+1): 
                                                                    time.sleep(1)
                                                                    elm.send_keys(Keys.END)
                                                                    time.sleep(2)
                                                                    try:
                                                                        tag6=browser.find_element_by_xpath("//*[@id='regYearWise_caseDetails_report_body']/tr["+str(n3)+"]/td[1]")
                                                                        time.sleep(4)
                                                                        x6=str(tag6.text)
                                                                        count=browser.find_element_by_xpath("//*[@id='regYearWise_caseDetails_report_body']/tr["+str(n3)+"]/td[2]/a")
                                                                        time.sleep(3)
                                                                        row=str(count.text)
                                                                        row=int(row)
                                                                        if row<10:
                                                                            row=1
                                                                        if row >10:
                                                                            row=row/10
                                                                            if row % 10==0:
                                                                                row=int(row)
                                                                            else:
                                                                                row=int(row+1)
                                                                        try:
                                                                             WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='regYearWise_caseDetails_report_body']/tr["+str(n3)+"]/td[2]/a")))
                                                                        except TimeoutException:
                                                                             print("Timed out waiting for page to load")
                                                                             browser.quit()
                                                                        elm.send_keys(Keys.END)
                                                                        time.sleep(3)
                                                                                       
                                                                        browser.find_element_by_xpath("//*[@id='regYearWise_caseDetails_report_body']/tr["+str(n3)+"]/td[2]/a").click()
                                                                        time.sleep(4)
                                                                        for t in range(1,row+1):
                                                                            elm.send_keys(Keys.END)
                                                                            time.sleep(2)
                                                                            if t>1:
                                                                                    browser.find_element_by_xpath("//*[@id='example_regnoWise_caseDetails_next']").click()
                                                                                    
                                                                                    run=1
                                                                                
                                                                            if t==1:
                                                                                    ispresent=len(browser.find_elements_by_xpath("//*[@id='example_regnoWise_caseDetails_paginate']/span/a["+str(t)+"]"))
                                                                            time.sleep(3)
                                                                            if(ispresent == 1 or run==1):
                                                                                    
                                                                                    row_count6 = len(browser.find_elements_by_xpath("//*[@id='regnoWise_caseDetails_report_body']/tr"))
                                                                                    time.sleep(3)
                                                                                    if row_count6>10:
                                                                                        row_count6=10
                                                                                    
                                                                                    
                                                                                    for i in range(1,row_count6+1):
                                                                                           
                                                                                            
                                                                                            titles_element = browser.find_elements_by_xpath("//*[@id='regnoWise_caseDetails_report_body']/tr["+str(i)+"]/td/a")
                                                                                            values_element = browser.find_elements_by_xpath("//*[@id='regnoWise_caseDetails_report_body']/tr["+str(i)+"]/td/a")
                                                                                            values = [x.text for x in values_element]
                                                                                            titles = []
                                                                                            for x in titles_element:
                                                                                                titles.append(x.text)
                                                                                            for title, value in zip(titles, values):
                                                                                                path[title]=x1+x2+x3+x4+x5+x6   
                                                                                                print (title)
                                                                                                ispresent=0
                                                                                                run=0
                                                                        elm.send_keys(Keys.HOME)
                                                                        time.sleep(2)
                                                                        try:
                                                                             WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='regno_Wise_caseDetails_tab']/a")))
                                                                        except TimeoutException:
                                                                            print("Timed out waiting for page to load")
                                                                            browser.quit()
                                                                        time.sleep(3)
                                
                                                                        browser.find_element_by_xpath("//*[@id='regno_Wise_caseDetails_tab']/a").click()
                                                                    except NoSuchElementException:
                                                                        pass
                                                        elm.send_keys(Keys.HOME)
                                                        time.sleep(2)
                                                        try:
                                                            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='regYearWise_caseDetails_tab']/a")))
                                                        except TimeoutException:
                                                            print("Timed out waiting for page to load")
                                                            browser.quit()
                                                        time.sleep(3)
                                                        
                                                        browser.find_element_by_xpath("//*[@id='regYearWise_caseDetails_tab']/a").click()  
                                                    except NoSuchElementException:
                                                         pass
                                        
                                        elm.send_keys(Keys.HOME)
                                        time.sleep(2)
                                        try:
                                            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='estCodeWise_caseDetails_tab']/a")))
                                            
                                        except TimeoutException:
                                            print("Timed out waiting for page to load")
                                            browser.quit()
                                        time.sleep(4)
                                        browser.find_element_by_xpath("//*[@id='estCodeWise_caseDetails_tab']/a").click()        
                                    except NoSuchElementException:
                                        pass
                        elm.send_keys(Keys.HOME)
                        time.sleep(2)           
                        try:
                            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='distWise_caseDetails_tab']/a")))
                        except TimeoutException:
                            print("Timed out waiting for page to load")
                            browser.quit()
                        time.sleep(4)   
                        browser.find_element_by_xpath("//*[@id='distWise_caseDetails_tab']/a").click()
                    except NoSuchElementException:
                        pass
        elm.send_keys(Keys.HOME)
        time.sleep(2)
        try:
            WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='stateWise_caseDetails_tab']/a")))
        except TimeoutException:
            print("Timed out waiting for page to load")
            browser.quit()
        time.sleep(3)
        browser.find_element_by_xpath("//*[@id='stateWise_caseDetails_tab']/a").click()
    except NoSuchElementException:
        pass

try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='caseDetails_tab']/a")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
browser.find_element_by_xpath("//*[@id='caseDetails_tab']/a").click()
           
