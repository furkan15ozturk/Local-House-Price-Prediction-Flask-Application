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
    browser2 = webdriver.Edge(f"{os.getcwd()}/msedgedriver.exe")
    next_page = True
    while next_page:
        browser.get(link)  # opens the web browser
        time.sleep(3)
        houses = browser.find_elements(by=By.CSS_SELECTOR, value="._3qUI9q")
        count = 0
        for c in houses:
            if c.get_attribute("data-index") is None:
                continue
            else:
                house_link = c.find_element(by=By.CSS_SELECTOR, value="a")
                house_href = house_link.get_attribute("href")
                print(house_href)
                browser2.get(house_href)
                house_info = browser2.find_elements(by=By.CSS_SELECTOR, value="._35T4WV")

                # area_xpath = '//div[contains(text(), "Brüt Metrekare")]/following-sibling::div'
                # room_xpath = '//div[contains(text(), "Oda Sayısı")]/following-sibling::div'
                # bathroom_xpath = '//div[contains(text(), "Banyo Sayısı")]/following-sibling::div'
                # floor_count_xpath = '//div[contains(text(), "Binanın Kat Sayısı")]/following-sibling::div'
                # balcony_xpath = '//div[contains(text(), "Balkon Sayısı")]/following-sibling::div'
                area_xpath = '//div[contains(text(), "Brüt Metrekare")]/following-sibling::div'
                room_xpath = '//div[contains(text(), "Oda Sayısı")]/following-sibling::div'
                floor_count_xpath = '//div[contains(text(), "Binanın Kat Sayısı")]/following-sibling::div'
                building_age_xpath = '//div[contains(text(), "Binanın Yaşı")]/following-sibling::div'
                area_elements = browser2.find_elements(by=By.XPATH, value=area_xpath)
                room_elements = browser2.find_elements(by=By.XPATH, value=room_xpath)
                floor_count_elements = browser2.find_elements(by=By.XPATH, value=floor_count_xpath)
                building_age_elements = browser2.find_elements(by=By.XPATH, value=building_age_xpath)

                area_value = area_elements[0].text if area_elements else None
                room_value = room_elements[0].text if room_elements else None
                floor_count_value = floor_count_elements[0].text if floor_count_elements else None
                building_age_value = building_age_elements[0].text if building_age_elements else None

                if count == 0:
                    print("Area: " + area_value)
                    print("Room: " + room_value)
                    print("Floor Count: " + floor_count_value)
                    print("Building age: " + building_age_value)
                count += 1

                # 7 -
                # elements = c.find_elements(by=By.CSS_SELECTOR, value="._2UELHn")
                # price = c.find_elements(by=By.CSS_SELECTOR, value="._2C5UCT")
                # location = c.find_elements(by=By.CSS_SELECTOR, value="._2wVG12")
                # try:
                #     for element in elements:
                #         find_m2 = element.find_element(by=By.XPATH, value=".//span[contains(text(),'m2')]")
                #         m2_text = find_m2.text
                #         m2_value = re.search(r'\d+\s*m2', m2_text)
                #         m2 = m2_value.group()
                #         house_list.append({'price': int(price[0].text.replace('\n', '').replace('.', '').replace('TL', '')),
                #                            'location': location[0].text.replace('\n', ''),
                #                            'm2': m2.replace(' m2', '')})
                # except:
                #     print("Error")
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
