import datetime
import time
from selenium import webdriver
from selenium.webdriver.chrome.options import Options


def champion_details(url):
    CHROME_PATH = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    CHROMEDRIVER_PATH = "C:\\Users\\Fourth\\.PyCharm2019.3\\chromedriver.exe"
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    driver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                              options=chrome_options
                              )
    driver.get(url)
    file1 = open("tft_info.txt", "a+")

    #
    a = driver.find_elements_by_class_name("guide-champion-detail__name")
    url_string = a[0].text
    file1.write("----------------------------------------------------------------\n")
    file1.write(str(url_string) + "\n")
    file1.write("\n")

    #
    a = driver.find_elements_by_class_name("align-middle")
    for i in range(len(a)):
        if len(a[i].text) > 3:
            file1.write(str(a[i].text) + "\n")
    file1.write("\n")

    a = driver.find_elements_by_class_name("guide-champion-detail__base-stat__value")
    for i in range(7):
        if i == 3:
            b = driver.find_element_by_xpath("//div[@class='guide-champion-detail__base-stat__value']//img")
            st = attack_range_converter(str(b.get_attribute("src")))
            file1.write(str(stat_name(i)) + "\t" + st + "\n")
        else:
            file1.write(str(stat_name(i)) + "\t" + str(a[i].text) + "\n")
    file1.write("\n")

    #
    a = driver.find_elements_by_class_name("guide-champion-detail__skill")
    url_string = a[0].text
    file1.write(str(url_string) + "\n")
    file1.write("\n")

    file1.close()
    driver.quit()


def stat_name(i):
    switcher = {
        0: 'HP :',
        1: 'AD :',
        2: 'DPS:',
        3: 'AtR:',
        4: 'AS :',
        5: 'ARM:',
        6: 'MR :'
    }
    return switcher.get(i, "Invalid")


def attack_range_converter(s):
    switcher = {
        "https://cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance301.png": '180',
        "https://cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance302.png": '420',
        "https://cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance303.png": '660',
        "https://cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance304.png": '890',
        "https://cdn.lolchess.gg/images/tft/attack-distance/set3/ico_attack_distance305.png": '?'
    }
    return switcher.get(s, "Invalid")


def list_maker(u):
    CHROME_PATH = "C:\Program Files (x86)\Google\Chrome\Application\chrome.exe"
    CHROMEDRIVER_PATH = "C:\\Users\\Fourth\\.PyCharm2019.3\\chromedriver.exe"
    WINDOW_SIZE = "1920,1080"
    chrome_options = Options()
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--window-size=%s" % WINDOW_SIZE)
    chrome_options.binary_location = CHROME_PATH
    adriver = webdriver.Chrome(executable_path=CHROMEDRIVER_PATH,
                              options=chrome_options
                              )
    adriver.get(u)
    # champ_list = []
    a = adriver.find_elements_by_class_name("guide-champion-list__item")
    # print(str(len(a)))
    for i in range(len(a)):
        # temp = champ_list.append(str(a[i].get_attribute("href")))
        champion_details(a[i].get_attribute("href"))


url = "https://lolchess.gg/champions/set4/aatrox"
list_maker(url)
# champion_details(url)
