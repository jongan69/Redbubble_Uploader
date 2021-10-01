from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
import time
import os
import urllib.request
import config



# Initializing Bot
print('Bot started, if it fails, make sure you havent reached your upload limit')
options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)
options.binary_location = '/Applications/Brave Browser.app/Contents/MacOS/Brave Browser'
driver_path = config.chromeDriverPath
drvr = webdriver.Chrome(options = options, executable_path = driver_path)
drvr.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source":
        "const newProto = navigator.__proto__;"
        "delete newProto.webdriver;"
        "navigator.__proto__ = newProto;"
    })
drvr.get('https://www.redbubble.com/portfolio/images/new')



# Login Process
emailField = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/div[1]/div/div/input')
emailField.send_keys(config.email)
time.sleep(2)
passField = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/div[2]/div/div/input')
passField.send_keys(config.password)
time.sleep(2)
button = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/div[2]/div/form/span/button')
time.sleep(2)
button.click()



# Capatcha Beater
print('Checking for capatcha...')
for i in range(1, 11):
        print('.')
try:
    seq = drvr.find_elements_by_tag_name('iframe')
    wait = WebDriverWait(drvr, 10).until(expected_conditions.element_to_be_clickable(
       (By.CSS_SELECTOR, "iframe[title='recaptcha challenge']"))).click()
    drvr.switch_to.default_content()
    WebDriverWait(drvr, 5).until(
    expected_conditions.frame_to_be_available_and_switch_to_it((By.CSS_SELECTOR, "iframe[title='recaptcha challenge']")))
    WebDriverWait(drvr, 5).until(
    expected_conditions.element_to_be_clickable((By.CSS_SELECTOR, "button#recaptcha-audio-button"))).click()
    WebDriverWait(drvr, 10).until(
    expected_conditions.presence_of_element_located((By.CSS_SELECTOR, ".rc-audiochallenge-play-button button")))
    # get the mp3 audio file
    src = drvr.find_element_by_id("audio-source").get_attribute("src")
    print(src)
    urllib.request.urlretrieve(src, "src.mp3")
    # transcribe the mp3 file
    from transcribe import trans
    input = drvr.find_element_by_xpath('/html/body/div/div/div[6]/input')
    input.send_keys(trans)
    sub = drvr.find_element_by_xpath('/html/body/div/div/div[8]/div[2]/div[1]/div[2]/button')
    sub.click()
    print('we beat that captcha like it was a mean prostitue')
    time.sleep(1)
except:
    print("We probably didn't have one")
finally: 
    print("Ladies and gentleman, we're in")



# Loop for uploading
x = 0
for filename in os.scandir(config.directory):
    fileName,fileExtension = os.path.splitext(filename)
    print ('meme file type is ' + fileExtension) 
    print ('meme file name is ' + fileName) 

   # Upload Image Proccess
    if fileExtension.endswith("png") | fileExtension.endswith("jpg") | fileExtension.endswith("jpeg"):
        time.sleep(1.5)
        print('Uplaoding meme: ' + filename.path)
        uploadButton = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/div/div[1]/div[1]/input')
        uploadButton.send_keys(filename.path)
        time.sleep(1)
        memeName = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[1]/input')
        memeName.send_keys("Meme number: " + str(x))
        x = x + 1
        print('Meme number: '+ str(x))
        memeTags = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[2]/textarea')
        memeTags.send_keys("stickers, swag, merch, meme, memes, funny, dankmemes, memesdaily, funnymemes, lol, follow, humor, dank, like, love, memepage, instagram, comedy, dankmeme, tiktok, lmao, anime, fun, dailymemes, edgymemes, ol, offensivememes, memestagram, bhfyp, instagood, funnymeme, memer, bhfyp")
        memeDescription = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[3]/textarea')
        memeDescription.send_keys("I beat off to this regularly")
        stickerButton = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[14]/div[2]/div[4]/div[2]/div[2]')
        designButton = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[1]/div[1]/div/div/label[2]/input[2]')
        drawingButton = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[1]/div[1]/div/div/label[4]/input[2]')
        memesButton = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[1]/div[2]/div[2]/section/ul/li/label/input')
        matureButton = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[2]/div[2]/div/label[2]/input')
        rightsButton = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[3]/input')
        saveWorkButton = drvr.find_element_by_xpath('/html/body/div[1]/div[5]/div[2]/form/section[2]/div[4]/div/input')
        time.sleep(2.5)
        stickerButton.click()
        designButton.click()
        drawingButton.click()
        memesButton.click()
        matureButton.click()
        rightsButton.click()
        time.sleep(2.5)
        saveWorkButton.click()
        time.sleep(11)
        os.remove(filename.path)
        restartButton = drvr.find_element_by_xpath('/html/body/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div[2]/div/a/span')
        restartButton.click()
    else:
        print('no memes left or limit reached')