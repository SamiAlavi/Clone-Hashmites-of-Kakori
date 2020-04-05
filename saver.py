from os import chdir
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import selenium
import os
import re

# Using Chrome to access web
driver = webdriver.Chrome('chromedriver.exe')
# Open the website
driver.get("http://www.nasabnama.com/")

chdir('webpages/')

# Select the id box
id_box = driver.find_element_by_name('txtUserName')
# Send id information
id_box.send_keys('#enter username')
# Find password box
pass_box = driver.find_element_by_name('txtUserPass')
# Send password
pass_box.send_keys('#enter password')

# Find login button
login_button = driver.find_element_by_name('Login')
# Click login
pass_box.send_keys(Keys.RETURN)

links=['http://www.nasabnama.com/default.asp',
    'http://www.nasabnama.com/intro.asp',
    'http://www.nasabnama.com/glance.asp',
    'http://www.nasabnama.com/additions.asp',
    'http://www.nasabnama.com/contributors.asp',
    'http://www.nasabnama.com/thanks.asp',
    'http://www.nasabnama.com/links.asp',
    'http://www.nasabnama.com/feedback.asp',
    'http://www.nasabnama.com/users.asp?mode=editprofile',
    'http://www.nasabnama.com/users.asp?mode=changepassword']

def change_asp(text):
    c=text.count('.asp')
    text=text.replace('.asp','.html',c)
    text=text.replace('users.html?mode=editprofile','editprofile.html')
    text=text.replace('users.html?mode=changepassword','changepassword.html')
    text=text.replace('logout.html','default.html')
    return text

def change_loc(html):
    for j in range(1,html.count('details.asp?key=')+1):
        index=html.find('details.asp?key=')
        
        key=html[index+16:index+23]
        key=re.search(r'\d+', key).group()
        lenkey=len(key)

        html=html[:index]+key+'.html'+html[index+15+lenkey+1:]        
    return html
            
for i in links:
    driver.get(i)
    html=change_loc(driver.page_source)
    html=change_asp(html)
    
    name=i[25:-4]
    if i.endswith('editprofile'):
        name='editprofile'
    elif i.endswith('changepassword'):
        name='changepassword'
        
    with open(name+'.html', 'w') as f:
        f.write(html) 

for i in range(7800,10828):
    driver.get('http://www.nasabnama.com/details.asp?key='+str(i))
    html=driver.page_source
    html=change_loc(html)
    html=change_asp(html)
            
    with open(str(i)+'.html', 'w') as f:
        f.write(html)           

