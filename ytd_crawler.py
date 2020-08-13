from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.action_chains import ActionChains
from selenium.webdriver.chrome.options import Options
import time
from random import randint


class Downloader():
    def __init__(self, *args):
        self.update_user = self.update

    def dilly_dally(self, num=3, factor=1):
        time.sleep(randint(num, int(factor*num)))

    def download_to_mp3(self, youtube_url):
        converter = "https://youtubetomp3.sc/"
        self.update_user()
        driver = webdriver.Chrome(executable_path="C://Program Files (x86)/chromedriver.exe")
        self.update_user()
        driver.get(converter)
        driver.find_element_by_id("videoURL").send_keys(youtube_url)
        self.dilly_dally(1)
        self.update_user()
        driver.find_element_by_name("submitForm").click()
        self.dilly_dally(1)
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        driver.switch_to.window(driver.window_handles[-1])
        while True:
            try:
                success = driver.find_element_by_xpath("//*[@id='conversionSuccess']/p[4]/a")
                success.click()
                break
            except:
                self.dilly_dally(3)
                continue
        self.dilly_dally(10)
        driver.switch_to.window(driver.window_handles[-1])
        driver.close()
        self.dilly_dally(30,1.2)
        driver.quit()

    def update(self):
        pass


if __name__ == "__main__":
    youtube_url = "https://www.youtube.com/watch?v=a4RRHEeunjg"

    downloader = Downloader()
    downloader.download_to_mp3(youtube_url)