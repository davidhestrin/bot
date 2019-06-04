from selenium import webdriver
##### ARGUMENTS #####
url = 'https://cnn.com/'
username = 'username'
password = 'password'
driver = webdriver.Firefox(executable_path = "/Users/davidshlomohestrin/work/geckodriver")
driver.get(url)
# dir(driver)
driver.save_screenshot('cnn.png')
driver.quit()
