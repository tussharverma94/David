from selenium import webdriver
import time


# driver = webdriver.Edge("D:\\python\\edgedriver_win64\\msedgedriver.exe")
# driver.get("https://web.whatsapp.com/")
# driver.maximize_window()


class auto_send:
    def __init__(self, name, mssg, site, count=1):
        self.name = name
        self.mssg = mssg
        self.site = site
        self.count = count
        self.driver = webdriver.Edge("D:\\python\\edgedriver_win64\\msedgedriver.exe")


    def send_mssg(self):
        try:
            self.driver.get(self.site)
            time.sleep(15)
            self.driver.maximize_window()

            # path to the user to send
            user = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[3]/div/div[2]/div[1]/div/div/div[14]/div/div/div[2]/div[1]/div[1]/span/span")
            user.click()

            # path of the message box where one type the message
            msg_box = self.driver.find_element_by_xpath(
                "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[2]/div/div[2]")

            for index in range(self.count):
                msg_box.send_keys(self.mssg)
                # path of the clickable object for sending message
                self.driver.find_element_by_xpath(
                    "/html/body/div[1]/div/div/div[4]/div/footer/div[1]/div[3]/button/span")

            return "successful"
        except Exception as e:
            str(e)
            return "failed"

# k = auto_send("Dad Voda", "Test", "https://web.whatsapp.com", 10)
# # k.send_mssg()
