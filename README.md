# Redbubble_Uploader



______________ ___ .___  _________ .___  _________ ____________________ ________   ____  __.___________ _______                                                                          
\__    ___/   |   \|   |/   _____/ |   |/   _____/ \______   \______   \\_____  \ |    |/ _|\_   _____/ \      \                                                                         
  |    | /    ~    \   |\_____  \  |   |\_____  \   |    |  _/|       _/ /   |   \|      <   |    __)_  /   |   \                                                                        
  |    | \    Y    /   |/        \ |   |/        \  |    |   \|    |   \/    |    \    |  \  |        \/    |    \                                                                       
  |____|  \___|_  /|___/_______  / |___/_______  /  |______  /|____|_  /\_______  /____|__ \/_______  /\____|__  /                                                                       
                \/             \/              \/          \/        \/         \/        \/        \/         \/                                                                        
  ____________________________ __________     _____    _____________  __.___ _______    ________     _____  ___________ ___________________    ___________._______  ___ .______________  
 /   _____/\__    ___/\_____  \\______   \   /  _  \  /   _____/    |/ _|   |\      \  /  _____/    /     \ \_   _____/ \__    ___/\_____  \   \_   _____/|   \   \/  / |   \__    ___/  
 \_____  \   |    |    /   |   \|     ___/  /  /_\  \ \_____  \|      < |   |/   |   \/   \  ___   /  \ /  \ |    __)_    |    |    /   |   \   |    __)  |   |\     /  |   | |    |     
 /        \  |    |   /    |    \    |     /    |    \/        \    |  \|   /    |    \    \_\  \ /    Y    \|        \   |    |   /    |    \  |     \   |   |/     \  |   | |    |     
/_______  /  |____|   \_______  /____|     \____|__  /_______  /____|__ \___\____|__  /\______  / \____|__  /_______  /   |____|   \_______  /  \___  /   |___/___/\  \ |___| |____| /\  
        \/                    \/                   \/        \/        \/           \/        \/          \/        \/                     \/       \/              \_/              )/  
 __      __  _________________________   ___ ___   ______________ ___ .___  _________ ____   ____.___________  ___________________                                                       
/  \    /  \/  _  \__    ___/\_   ___ \ /   |   \  \__    ___/   |   \|   |/   _____/ \   \ /   /|   \______ \ \_   _____/\_____  \                                                      
\   \/\/   /  /_\  \|    |   /    \  \//    ~    \   |    | /    ~    \   |\_____  \   \   Y   / |   ||    |  \ |    __)_  /   |   \                                                     
 \        /    |    \    |   \     \___\    Y    /   |    | \    Y    /   |/        \   \     /  |   ||    `   \|        \/    |    \                                                    
  \__/\  /\____|__  /____|    \______  /\___|_  /    |____|  \___|_  /|___/_______  /    \___/   |___/_______  /_______  /\_______  /                                                    
       \/         \/                 \/       \/                   \/             \/                         \/        \/         \/                                                     



https://youtube.com/live/BkVkD8nb2LY?feature=share









A Selenium ChromeDriver Script for automatically uploading art and memes alike to Redbubble stickers as merchandise on Redbubble that also passes captcha

## What is this?

This is a bot that uploads memes to [redbubble.com](https://www.redbubble.com/portfolio/images/new).

## How to use?

1. `pip3 install -r ./requirements.txt` to Install [Selenium](https://selenium-python.readthedocs.io/), [Chrome Driver](https://chromedriver.chromium.org/downloads) and [Python](https://www.python.org/downloads/).

2. Download this bot and add your login credentials and chrome driver path in the config.py file:
   A. Redbubble Email
   B. Redbubble Password
   C. Path to Chrome Webdriver (This was built using Brave Browser or Chromium 93)

3. Place the memes you wish to upload in the specified directory.

4. `python3 app.py` to Run the bot

5. The bot will now automatically upload the memes to redbubble.com.

## What does it do?

This bot will log in to your redbubble account and upload memes from the specified directory. It will automatically fill out the necessary fields such as tags, description and categories. It will also delete the meme from the directory once it is uploaded.

## What does it not do?

This bot does not check for duplicates. It will upload the memes as is without any checks.

The bot will run up to 60 times before failure (Redbubble caps out number of uploads per day at 60)
