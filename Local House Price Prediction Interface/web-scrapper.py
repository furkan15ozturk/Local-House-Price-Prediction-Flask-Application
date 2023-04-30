from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import re
import os
import time


house_list = []
def update_houses():
    edge_options = Options()
    link = "https://www.emlakjet.com/satilik-konut/istanbul-arnavutkoy/"
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    edge_options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Edge(f"{os.getcwd()}/msedgedriver.exe")
    next_page = True
    while next_page:
        browser.get(link)  # opens the web browser
        time.sleep(3)
        houses = browser.find_elements(by=By.CSS_SELECTOR, value="._3qUI9q")
        for c in houses:
            if c.get_attribute("data-index") is None:
                continue
            else:
                elements = c.find_elements(by=By.CSS_SELECTOR, value="._2UELHn")
                price = c.find_elements(by=By.CSS_SELECTOR, value="._2C5UCT")
                location = c.find_elements(by=By.CSS_SELECTOR, value="._2wVG12")
                try:
                    for element in elements:
                        find_m2 = element.find_element(by=By.XPATH, value=".//span[contains(text(),'m2')]")
                        m2_text = find_m2.text
                        m2_value = re.search(r'\d+\s*m2', m2_text)
                        m2 = m2_value.group()
                        house_list.append({'price': int(price[0].text.replace('\n', '').replace('.', '').replace('TL', '')),
                                           'location': location[0].text.replace('\n', ''),
                                           'm2': m2.replace(' m2', '')})

                except:
                    pass
        try:
            next_link = browser.find_element(by=By.XPATH, value="/html/body/div/div/div[3]/div[1]/div/div[7]/div["
                                                                "1]/div[35]/div[1]/ul/li[3]/div")
            a = next_link.find_element(by=By.CSS_SELECTOR, value="a")
            link = a.get_attribute("href")
            print(link)
            next_page = True
        except:
            next_page = False
            break

    browser.close()


if __name__ == "__main__":
    update_houses()
    print(house_list)
