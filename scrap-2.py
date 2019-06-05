from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.webdriver.common.keys import Keys
# example option: add 'incognito' command line arg to options
option = webdriver.ChromeOptions()
option.add_argument("--incognito")

# create new instance of chrome in incognito mode
browser = webdriver.Chrome(executable_path=r'C:/Users/Sunmarg Das/Downloads/chromedriver_win32/chromedriver.exe', chrome_options=option)
chrome_path  = r"C:/Users/Sunmarg Das/Downloads/chromedriver_win32/chromedriver.exe"
driver = webdriver.Chrome(chrome_path)
# go to website of interest
browser.get("https://njdg.ecourts.gov.in/njdgnew/index.php")
browser.execute_script("document.body.style.zoom='100%'")
timeout = 15
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='report_body']/tr[27]/td[4]")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
browser.maximize_window()
browser.execute_script("document.body.style.zoom='100%'")
print("  Pending Cases ")
elm=browser.find_element_by_tag_name('html')
path={}
val={}
for i in range(2,8):
    titles_element = browser.find_elements_by_xpath("//*[@id='report_body']/tr["+str(i)+"]/td[1]")
    values_element = browser.find_elements_by_xpath("//*[@id='report_body']/tr["+str(i)+"]/td[3]/a")
    values = [x.text for x in values_element]
    titles = []
    i=i+1;
    for x in titles_element:
        titles.append(x.text)
    for title, value in zip(titles, values):
        print(title + ' : ' + value)
        val[title]=value

    
tag1=browser.find_element_by_xpath("//*[@id='report_body']/tr[2]/td[1]")
time.sleep(3)
x1=str(tag1.text+"-->")
time.sleep(2)
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='report_body']/tr[2]/td[3]")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
time.sleep(2)
elm.send_keys(Keys.END)
time.sleep(2)  
browser.find_element_by_xpath("//*[@id='report_body']/tr[2]/td[3]/a").click()
time.sleep(3)

for q in range (1,3):
    elm.send_keys(Keys.END)
    time.sleep(2)  
    ispresent=len(browser.find_elements_by_xpath("//*[@id='example_year_paginate']/span/a["+str(q)+"]"))
    time.sleep(3)
    if(ispresent==1):
        elm.send_keys(Keys.END)
        time.sleep(2)  
        browser.find_element_by_xpath("//*[@id='example_year_paginate']/span/a["+str(q)+"]").click()        
        time.sleep(3)
        row_count1 = len(browser.find_elements_by_xpath("//*[@id='state_report_body']/tr"))
        time.sleep(3)
        val1={}
        for j in range(1,row_count1+1):
            titles_element = browser.find_elements_by_xpath("//*[@id='state_report_body']/tr["+str(j)+"]/td[1]")
            values_element = browser.find_elements_by_xpath("//*[@id='state_report_body']/tr["+str(j)+"]/td[2]/a")
            values = [x.text for x in values_element]
            titles = []
            j=j+1
            for k in titles_element:
                titles.append(k.text)
            for title, value in zip(titles, values):
                print(title + ' : ' + value)
                val1[x1+title]=value
        time.sleep(3)        
        val.update(val1)
        for m in range (1,row_count1+1):      
            
            elm.send_keys(Keys.END)
            time.sleep(2)
            try:
                tag2=browser.find_element_by_xpath("//*[@id='state_report_body']/tr["+str(m)+"]/td[1]")
                time.sleep(3)
                x2=str(tag2.text+"-->")
                time.sleep(3)
                try:
                    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='state_report_body']/tr["+str(m)+"]/td[2]/a")))
                except TimeoutException:
                    print("Timed out waiting for page to load")
                    browser.quit()
                
                  
                browser.find_element_by_xpath("//*[@id='state_report_body']/tr["+str(m)+"]/td[2]/a").click()
                time.sleep(5)
                
                for e in range(1,8):
                    elm.send_keys(Keys.END)
                    time.sleep(2)  
                    ispresent=len(browser.find_elements_by_xpath("//*[@id='example_state_paginate']/span/a["+str(e)+"]"))
                    time.sleep(3)
                    if(ispresent==1):
                        browser.find_element_by_xpath("//*[@id='example_state_paginate']/span/a["+str(e)+"]").click()        
                        time.sleep(3)
                        row_count2 = len(browser.find_elements_by_xpath("//*[@id='state_report_body']/tr"))
                        time.sleep(3)
                        if row_count2>10:
                            row_count2=10
                        val2={}
                        for i in range(1,row_count2+1):
                            
                            titles_element = browser.find_elements_by_xpath("//*[@id='state_report_body']/tr["+str(i)+"]/td[1]")
                            
                            values_element = browser.find_elements_by_xpath("//*[@id='state_report_body']/tr["+str(i)+"]/td[2]/a")
                            
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
                            time.sleep(3)
                            elm.send_keys(Keys.END)
                            time.sleep(2)  
                            try:
                                tag3=browser.find_element_by_xpath("//*[@id='state_report_body']/tr["+str(n)+"]/td[1]")
                                time.sleep(3)
                                x3=str(tag3.text+"-->")
                                try:
                                    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='state_report_body']/tr["+str(n)+"]/td[2]/a")))
                                except TimeoutException:
                                    print("Timed out waiting for page to load")
                                    browser.quit()
                                
                                time.sleep(3)
                                elm.send_keys(Keys.END)
                                time.sleep(2)                              
                                browser.find_element_by_xpath("//*[@id='state_report_body']/tr["+str(n)+"]/td[2]/a").click()
                                time.sleep(4)       
                                for f in range(1,8):
                                    elm.send_keys(Keys.END)
                                    time.sleep(2)  
                                    ispresent=len(browser.find_elements_by_xpath("//*[@id='example_dist_paginate']/span/a["+str(f)+"]"))
                                    time.sleep(4)
                                    if(ispresent==1):
                                        browser.find_element_by_xpath("//*[@id='example_dist_paginate']/span/a["+str(f)+"]").click()        
                                        time.sleep(4)
                                        row_count3 = len(browser.find_elements_by_xpath("//*[@id='dist_report_body']/tr"))
                                        time.sleep(3)
                                        if row_count3>10:
                                            row_count3=10
                                        val3={}
                                        
                                        for i in range(1,row_count3+1):
                                                titles_element = browser.find_elements_by_xpath("//*[@id='dist_report_body']/tr["+str(i)+"]/td[1]")
                                                values_element = browser.find_elements_by_xpath("//*[@id='dist_report_body']/tr["+str(i)+"]/td[2]/a")
                                                values = [x.text for x in values_element]
                                                titles = []
                                                for x in titles_element:
                                                    titles.append(x.text)
                                                for title, value in zip(titles, values):
                                                    print(title + ' : ' + value)
                                                    
                                                    val3[x1+x2+x3+title]=value
                                        time.sleep(3)
                                        val.update(val3)
                                        time.sleep(3)
                                        for n1 in range(1,row_count3+1):
                                            
                                            elm.send_keys(Keys.END)
                                            time.sleep(2)  
                                            try:
                                                tag4=browser.find_element_by_xpath("//*[@id='dist_report_body']/tr["+str(n1)+"]/td[1]")
                                                time.sleep(3)
                                                x4=str(tag4.text+"-->") 
                                                try:
                                                    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='dist_report_body']/tr["+str(n1)+"]/td[2]/a")))
                                                except TimeoutException:
                                                    print("Timed out waiting for page to load")
                                                    browser.quit()
                                                
                                                val4={}
                                                elm.send_keys(Keys.END)
                                                time.sleep(2)  
                                                browser.find_element_by_xpath("//*[@id='dist_report_body']/tr["+str(n1)+"]/td[2]/a").click()
                                            
                                                time.sleep(4)
                                                for r in range(1,8):
                                                    elm.send_keys(Keys.END)
                                                    time.sleep(2)  
                                                    ispresent=len(browser.find_elements_by_xpath("//*[@id='example_est_paginate']/span/a["+str(r)+"]"))
                                                    time.sleep(4)
                                                    if(ispresent==1):
                                                        browser.find_element_by_xpath("//*[@id='example_est_paginate']/span/a["+str(r)+"]").click()        
                                                        time.sleep(3)
                                                        row_count4 = len(browser.find_elements_by_xpath("//*[@id='est_report_body']/tr"))
                                                        time.sleep(5)
                                                        if row_count4:
                                                            row_count4=10
                                                        val4={}
                                                        for i in range(1,row_count4+1):
                                                                    titles_element = browser.find_elements_by_xpath("//*[@id='est_report_body']/tr["+str(i)+"]/td[1]")
                                                                    values_element = browser.find_elements_by_xpath("//*[@id='est_report_body']/tr["+str(i)+"]/td[2]/a")
                                                                    values = [x.text for x in values_element]
                                                                    titles = []
                                                                    for x in titles_element:
                                                                        titles.append(x.text)
                                                                    for title, value in zip(titles, values):
                                                                        
                                                                        print(title + ' : ' + value)
                                                                        
                                                                        val4[x1+x2+x3+x4+title]=value
                                                        time.sleep(3)
                                                        val.update(val4)
                                                        time.sleep(3)
                                                        for n2 in range(1,row_count4+1):
                                                            elm.send_keys(Keys.END)
                                                            time.sleep(2)  
                                                            
                                                            try:
                                                                tag5=browser.find_element_by_xpath("//*[@id='est_report_body']/tr["+str(n2)+"]/td[1]")
                                                                time.sleep(3)
                                                                x5=str(tag5.text)
                                                                time.sleep(2)
                                                                count=browser.find_element_by_xpath("//*[@id='est_report_body']/tr["+str(n2)+"]/td[2]/a")
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
                                                                    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='est_report_body']/tr["+str(n2)+"]/td[2]/a")))
                                                                except TimeoutException:
                                                                    print("Timed out waiting for page to load")
                                                                    browser.quit()
                                                                time.sleep(2)
                                                                elm.send_keys(Keys.END)
                                                                time.sleep(2)  
                                                                browser.find_element_by_xpath("//*[@id='est_report_body']/tr["+str(n2)+"]/td[2]/a").click()
                                                        
                                                                time.sleep(4)
                                                                
                                                                for t in range(1,row+1):
                                                                    elm.send_keys(Keys.END)
                                                                    time.sleep(2)  
                                                                    if t>1:
                                                                        browser.find_element_by_xpath("//*[@id='example_cases_next']").click()
                                                                        
                                                                        run=1
                                                                    if t==1:
                                                                        ispresent=len(browser.find_elements_by_xpath("//*[@id='example_cases_paginate']/span/a["+str(t)+"]"))
                                                                    time.sleep(1)
                                                                    if(ispresent == 1 or run==1):
                                                                        
                                                                        row_count5 = len(browser.find_elements_by_xpath("//*[@id='cases_report_body']/tr"))
                                                                        time.sleep(2)
                                                                        if row_count5>10:
                                                                            row_count5=10
                                                                        time.sleep(2)
                                                                        
                                                                        for i in range(1,row_count5+1):
                                                                               
                                                                                
                                                                                titles_element = browser.find_elements_by_xpath("//*[@id='cases_report_body']/tr["+str(i)+"]/td/a")
                                                                                values_element = browser.find_elements_by_xpath("//*[@id='cases_report_body']/tr["+str(i)+"]/td/a")
                                                                                values = [x.text for x in values_element]
                                                                                titles = []
                                                                                for x in titles_element:
                                                                                    titles.append(x.text)
                                                                                for title, value in zip(titles, values):
                                                                                    path[title]=x1+x2+x3+x4+x5   
                                                                                    print (title)
                                                                                    ispresent=0
                                                                                    run=0
                                                            
                                                                time.sleep(2)
                                                                elm.send_keys(Keys.HOME)
                                                                time.sleep(2)  
                                                                try:
                                                                     WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='cases_tab1']/a")))
                                                                except TimeoutException:
                                                                    print("Timed out waiting for page to load")
                                                                    browser.quit()
                                                                time.sleep(5)
                                                                browser.find_element_by_xpath("//*[@id='cases_tab1']/a").click()
                                                                
                                                            except NoSuchElementException:
                                                                        pass
                                                elm.send_keys(Keys.HOME)
                                                time.sleep(2)  
                                                try:
                                                    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='est_tab']/a")))
                                                except TimeoutException:
                                                    print("Timed out waiting for page to load")
                                                    browser.quit()
                                                time.sleep(5)
                                                
                                                browser.find_element_by_xpath("//*[@id='est_tab']/a").click()  
                                                time.sleep(2)
                                                
                                            except NoSuchElementException:
                                                pass
                                
                                elm.send_keys(Keys.END)
                                time.sleep(2)  
                                try:
                                    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='dist_tab']/a")))
                                    
                                except TimeoutException:
                                    print("Timed out waiting for page to load")
                                    browser.quit()
                                time.sleep(5)
                                browser.find_element_by_xpath("//*[@id='dist_tab']/a").click()
                                
                            except NoSuchElementException:
                                pass
                elm.send_keys(Keys.END)
                time.sleep(2)            
                try:
                    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='state_tab']/a")))
                except TimeoutException:
                    print("Timed out waiting for page to load")
                    browser.quit()
                time.sleep(5)   
                browser.find_element_by_xpath("//*[@id='state_tab']/a").click()
                
            except NoSuchElementException:
                pass
elm.send_keys(Keys.END)
time.sleep(2)  
try:
    WebDriverWait(browser, timeout).until(EC.visibility_of_element_located((By.XPATH, "//*[@id='year_tab']/a")))
except TimeoutException:
    print("Timed out waiting for page to load")
    browser.quit()
time.sleep(3)
browser.find_element_by_xpath("//*[@id='year_tab']/a").click()
time.sleep(3)


   