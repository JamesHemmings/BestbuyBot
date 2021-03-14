from selenium import webdriver
from selenium.webdriver.chrome.options import Options                                                                                                       #import selenium and all other necessary modules
from selenium.common.exceptions import NoSuchElementException
import os
import time
from sms import sms
import sms_reply
from sms_reply import sms_reply


item_url="https://www.bestbuy.com/site/evga-nvidia-geforce-rtx-3060-xc-gaming-12gb-gddr6-pci-express-4-0-graphics-card/6454328.p?skuId=6454328"             #page of item you are trying to purchase

def check_exists_by_xpath(xpath):                                                                                                                           #function to check if an element exists by its xpath this will tell us if the item is sold out
    try:
        driver.find_element_by_xpath(xpath)
    except NoSuchElementException:
        return False
    return True

user_agent = "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.182 Safari/537.36"                           #help hide automation

options = webdriver.ChromeOptions()                                                                                                                         #selenium setup for CHROME version 84.xxxx
options.add_argument('--disable-blink-features=AutomationControlled')
#options.headless=True
options.add_argument('--ignore-certificate-errors')
options.add_argument('--ignore-ssl-errors')
options.add_experimental_option("excludeSwitches", ["enable-logging"])
options.add_argument(f'user-agent={user_agent}')
options.add_argument("--window-size=1920,1080")
options.add_argument('--ignore-certificate-errors')                                                                                                         #remove error messages from command prompt
options.add_argument('--allow-running-insecure-content')                                                                                                    
options.add_argument("--disable-extensions")
options.add_argument("--proxy-server='direct://'")
options.add_argument("--proxy-bypass-list=*")
options.add_argument("--start-maximized")
options.add_argument('--disable-gpu')
options.add_argument('--disable-dev-shm-usage')
options.add_argument('--no-sandbox')
prefs = {"profile.managed_default_content_settings.images": 2}
options.add_experimental_option("prefs", prefs)                                                                                                             #dont load images

driver = webdriver.Chrome(executable_path=r'C:\Users\james\source\repos\botpractice\botpractice\chromedriver.exe',options=options)                          #change this to location where webdriver is installed
driver.execute_script("Object.defineProperty(navigator, 'webdriver', {get: () => undefined})")                                                              #supposed to hide that browser is automated
driver.get("https://www.bestbuy.com")                                                                                                                       #navigate to bestbuy.com




print('READ CAREFULLY OR BOT MAY NOT WORK AS INTENDED.hit enter once you have completed each step')
time.sleep(3)
security_code=input('Enter 3 digit security code on back of debit card(this is the only personal information this bot asks for):')                          #get card csv to autofill later
input("Login to your bestbuy account and fill out shipping and payment method.")
input('Add an in stock item to your cart and go all the way through checkout process until you get to the confirm order button.')
input('Now return to your cart and make sure you REMOVE the item from your cart or you will be charged for this item also.')
driver.get('https://www.bestbuy.com/cart')
print("checking cart is empty")
time.sleep(4)

cart_not_empty = check_exists_by_xpath('/html/body/div[1]/main/div/div[2]/div[1]/div/div[1]/div[1]/section[2]/div/div/div[4]/div/div[1]/button')
time.sleep(2)

if cart_not_empty == True:
    input('WARNING CART IS NOT EMPTY.hit enter if you wish to proceed')
else:
    print ('Cart is empty')

print('Setup is now complete')
driver.get(item_url)
time.sleep(1.5)
title=driver.find_element_by_xpath('/html/body/div[3]/main/div[2]/div[3]/div[1]/div[1]/div/div/div[1]/h1')
print ("Selected item is "+title.text)
input('Hit enter when ready to start bot')
sms("bot for " +title.text+" has started")
def bot():
    
       
    timer=time.time()
    sold_out=True 
    
    print('Bot is starting')                                                                                                                                                                         
    print('Loading item page')
    still_running_check=0        
    while sold_out==True:                                                                                                                                       #while item is sold out reload the page and print sold out to the console
       driver.get(item_url)                      
       #time.sleep(1)
       sold_out=check_exists_by_xpath("/html/body/div[3]/main/div[2]/div[3]/div[2]/div/div/div[6]/div[1]/div/div/div/button")                                   
       still_running_check+=1
       sms_reply()
       #if still_running_check%100==0:
           #sms('Bot is still running and is on attempt '+str(still_running_check)+'\n '+str(round((time.time()-timer)/60,2))+' minute(s) have passed')
       if sold_out==False:
           break
       else:
           print ("Sold out")
    
    cart_button = driver.find_element_by_class_name("fulfillment-add-to-cart-button")                                                                   #once sold out is no longer true add to cart button is clicked
    cart_button.click()
    time.sleep(1)
    driver.get("https://www.bestbuy.com/checkout/r/fast-track")                                                                                             #navigates to checkout page
    time.sleep(1)
    code= driver.find_element_by_xpath('//*[@id="credit-card-cvv"]')                                                                                        #csv input location
    code.send_keys(security_code)                                                                                                                           #inputs previously given csv code
    time.sleep(2)
    #confirm_button= driver.find_element_by_class_name("button--place-order-fast-track")
    #confirm_button.click()
    
    print('Order submission screenshot saved as "OrderSubmission.png" in repository location')                                                              #order completion code
    driver.get_screenshot_as_file('OrderSubmission.png')
    sms('Bot Program executed succesfully for '+title.text)
    end=input(title.text+' program executed succesfuly hit enter to exit browser or type retry to start bot again:')                                                    #if program ran all the way through will print program ran succesfully
    if end=='retry':
                bot()
bot()  
#while True:
#    try:
#        bot()
#    except:
#        pass
#    else:
#        break
