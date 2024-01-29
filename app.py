from selenium import webdriver
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.support import expected_conditions as EC
from datetime import date
import random
import time
import os
import urllib.request
import config


# Initializing Bot
print('Bot started, if it fails, make sure you have not reached your upload limit Or adjust the sleep time and retry.')
x = random.randint(10, 30)

options = Options()
options.add_argument("start-maximized")
options.add_argument("disable-infobars")
options.add_argument("--disable-blink-features")
options.add_argument("--disable-blink-features=AutomationControlled")
options.add_argument("--ignore-certificate-error")
options.add_argument("--ignore-ssl-errors")
options.add_argument("log-level=2")

options.add_experimental_option("detach", True)
options.add_experimental_option("excludeSwitches", ["enable-automation"])
options.add_experimental_option('useAutomationExtension', False)

options.binary_location = config.binaryPath
s = Service(executable_path=config.chromeDriverPath)
# driver_path = config.chromeDriverPath
drvr = webdriver.Chrome(options=options, service=s)
drvr.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
    "source":
        "const newProto = navigator.__proto__;"
        "delete newProto.webdriver;"
        "navigator.__proto__ = newProto;"
})

drvr.get('https://www.redbubble.com/portfolio/images/new')


# CloudFlare Blocker
time.sleep(10)
CFelement = WebDriverWait(drvr, 20).until(EC.visibility_of_element_located((By.CSS_SELECTOR, "label.ctp-checkbox-label")))
CFelement.click()
time.sleep(10)

# Login Process
emailField = drvr.find_element(
    "xpath", '/html/body/div[1]/div[5]/div[2]/div[2]/div/form/div[1]/div/div/input')
emailField.send_keys(config.email)
time.sleep(x)
passField = drvr.find_element(
    "xpath", '/html/body/div[1]/div[5]/div[2]/div[2]/div/form/div[2]/div/div/input')
passField.send_keys(config.password)
time.sleep(x)
button = drvr.find_element(
    "xpath", '/html/body/div[1]/div[5]/div[2]/div[2]/div/form/span/button')
time.sleep(x)
button.click()


# Captcha Beater
print('Checking for captcha...')
for i in range(1, 11):
    print('.')
try:
    time.sleep(x)
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
    input = drvr.find_element("xpath", '/html/body/div/div/div[6]/input')
    time.sleep(x)
    input.send_keys(trans)
    sub = drvr.find_element(
        "xpath", '/html/body/div/div/div[8]/div[2]/div[1]/div[2]/button')
    sub.click()
    print('we beat that captcha like it was a mean prostitute')
    time.sleep(x)
except:
    print("We probably didn't have one")
finally:
    print("Ladies and gentleman, we're in")


# Loop for uploading
x = 0
for filename in os.scandir(config.directory):
    fileName, fileExtension = os.path.splitext(filename)
    print('meme file type is ' + fileExtension)
    print('meme file name is ' + fileName)

   # Upload Image Process
    if fileExtension.endswith("png") | fileExtension.endswith("jpg") | fileExtension.endswith("jpeg") | fileExtension.endswith("PNG"):
        time.sleep(x)
        print('Uploading meme: ' + filename.path)
        uploadButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/div/div[1]/div[1]/input')
        uploadButton.send_keys(filename.path)
        time.sleep(10)
        memeName = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[1]/input')
        today = date.today()
        d2 = today.strftime("%B %d, %Y")
        memeName.send_keys("Meme number " + str(x) + " on " + d2)
        x = x + 1
        print('Meme number: ' + str(x))
        time.sleep(x)
        memeTags = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[2]/textarea')
        memeTags.send_keys(
            "#stickerbomb, #stickergame, #stickersale, #stickerlove, #stickerdesign, #sticker, #stickerbombing, #stickeraddict, #stickerlife, #stickerartist")
        memeDescription = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/div/div[3]/div/div/div[1]/div/div[3]/textarea')
        memeDescription.send_keys("I beat off to this regularly")
        stickerButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/section[1]/div/div[14]/div[2]/div[4]/div[2]/div[3]')
        designButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[1]/div[1]/div/div/label[2]/input[2]')
        drawingButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[1]/div[1]/div/div/label[4]/input[2]')
        memesButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[1]/div[2]/div[2]/section/ul/li/label/input')
        matureButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[2]/div[2]/div/label[2]/input')
        rightsButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[3]/input')
        saveWorkButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div[5]/div[2]/form/section[2]/div[4]/div/input')
        time.sleep(5)
        stickerButton.click()
        designButton.click()
        drawingButton.click()
        memesButton.click()
        matureButton.click()
        rightsButton.click()
        time.sleep(5)
        saveWorkButton.click()
        time.sleep(5)
        os.remove(filename.path)
        restartButton = drvr.find_element(
            "xpath", '/html/body/div[1]/div/div[1]/div[2]/div/div/div/div[1]/div/div/div[2]/div/a/span')
        restartButton.click()
    else:
        print('no memes left or limit reached')
