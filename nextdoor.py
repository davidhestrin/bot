
import re
from selenium import webdriver
from selenium.webdriver.firefox.options import Options

##### OPTIONS #####
options = Options()
options.headless = True



##### ARGUMENTS #####
list_of_urls = ['https://nbc.com/', 'https://cnn.com']

driver = webdriver.Firefox(executable_path = "/Users/davidshlomohestrin/work/geckodriver", options = options)




for site_url in list_of_urls:
    pattern = re.compile('https?://(www\.)?(\w+)\..*')
    match = pattern.search(site_url)
    name = match.groups(2)[1]

    driver.get(site_url)
    page = driver.find_element_by_tag_name('body')
    file = open(f"{name}.txt", "w")
    desiredData = re.compile('Trump').search(page.text)
    print(desiredData, file = file)
    file.close()



driver.quit()
