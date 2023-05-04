from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
import re
import os
import time


house_list = []
def update_houses():
    edge_options = Options()
    link = "https://www.emlakjet.com/satilik-konut/istanbul-adalar/"
    edge_options.add_experimental_option("excludeSwitches", ["enable-automation"])
    edge_options.add_experimental_option('useAutomationExtension', False)
    browser = webdriver.Edge(f"{os.getcwd()}/msedgedriver.exe")
    # browser2 = webdriver.Edge(f"{os.getcwd()}/msedgedriver.exe")
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
                # print(house_href)
                # house_info = browser2.find_elements(by=By.CSS_SELECTOR, value="._35T4WV")

                # browser.find_element(by=By.TAG_NAME, value="body").send_keys(Keys.CONTROL + "T")
                browser.execute_script('''window.open("http://bings.com","_blank");''')
                browser.switch_to.window(browser.window_handles[-1])

                browser.get(house_href)

                area_xpath = '//div[contains(text(), "Brüt Metrekare")]/following-sibling::div'
                absolute_area_xpath = '//div[contains(text(), "Net Metrekare")]/following-sibling::div'
                room_xpath = '//div[contains(text(), "Oda Sayısı")]/following-sibling::div'
                floor_count_xpath = '//div[contains(text(), "Binanın Kat Sayısı")]/following-sibling::div'
                building_age_xpath = '//div[contains(text(), "Binanın Yaşı")]/following-sibling::div'

                area_elements = browser.find_elements(by=By.XPATH, value=area_xpath)
                absolute_area_elements = browser.find_elements(by=By.XPATH, value=absolute_area_xpath)
                room_elements = browser.find_elements(by=By.XPATH, value=room_xpath)
                floor_count_elements = browser.find_elements(by=By.XPATH, value=floor_count_xpath)
                building_age_elements = browser.find_elements(by=By.XPATH, value=building_age_xpath)
                price_element = browser.find_elements(by=By.CSS_SELECTOR, value=".R-RKDB")
                location_element = browser.find_elements(by=By.CSS_SELECTOR, value="._3VQ1JB")

                price = price_element[0].text.replace('.', '').replace('TL', '') if price_element else None
                price_value = int(re.findall(r'\d+', price)[0])

                location = location_element[0].text if location_element else None
                location_value = location.replace('location_on\n','')

                area = area_elements[0].text if area_elements else None
                area_value = int(area.replace(' M2', '').replace('.', ''))

                absolute_area = absolute_area_elements[0].text if absolute_area_elements else None
                absolute_area_value = int(absolute_area.replace(' M2', ''))

                room = room_elements[0].text if room_elements else None
                room_count = re.findall(r'\d+', room)
                if len(room_count) == 2:
                    room_value = int(room_count[0]) + int(room_count[1])
                else:
                    room_value = int(room_count[0])
                floor_count_value = int(floor_count_elements[0].text) if floor_count_elements else None

                building_age = building_age_elements[0].text.lower() if building_age_elements else None
                if building_age == "0 (yeni)":
                    building_age_value = 0
                elif building_age == "5-10":
                    building_age_value == 7.5
                elif building_age == "11-15":
                    building_age_value == 13.5
                elif building_age == "16-20":
                    building_age_value == 18.5
                elif building_age == "21 ve üzeri":
                    building_age_value == 21
                else:
                    building_age_value = int(building_age)


                house_list.append({'price': price_value,
                                   'area': area_value,
                                   'absolute_area': absolute_area_value,
                                   'room': room_value,
                                   'floor_count': floor_count_value,
                                   'building_age': building_age_value,
                                   'location': location_value})
                time.sleep(0.5)
                browser.close()
                browser.switch_to.window(browser.window_handles[0])

        browser.switch_to.window(browser.window_handles[0])

        next_link = browser.find_elements(by=By.CSS_SELECTOR, value="._3au2n_")
        for i in next_link:
            if "Sonraki" in i.text:
                a = i.find_element(By.CSS_SELECTOR, "a")
                href_value = a.get_attribute("href")
                link = href_value
                print(i.text)
                next_page = True
            else:
                next_page = False
    browser.close()


if __name__ == "__main__":
    update_houses()
    print(house_list)
