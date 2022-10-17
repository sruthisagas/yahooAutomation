__doc__ = '''

Test Case Header:
=================
:Author: Sruthi sagar
:TestId: 02
:Release: NA
:TestName: test_searchHelp
:Objective: "To search on yahoo help that how to login by phone"
:TestDescription: " Return Results that match the search word Login by Phone when user search on help page"
:PlanPriority:1 - low
:TestPassCriteria: "Return Results that match the search word" '''


import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By


class Test(unittest.TestCase):

    def test_loginByPhoneHelp(self):

        # service_obj = Service("C:/Users/anees/Downloads/chromedriver_win32/chromedriver")
        # driver = webdriver.Chrome(service=service_obj)
        # Checking for Admin console Launched or not.
        driver = webdriver.Chrome(executable_path="C:\\chromedriver.exe")
        actual_url = "https://login.yahoo.com/"
        driver.get(actual_url)
        current_url = driver.current_url
        assert actual_url == current_url, "Yahoo login page not launch Successfully."
        print("Yahoo login page launched Successfully.")

        driver.find_element(By.LINK_TEXT, 'Help').click()
        # time.sleep(10)
        driver.find_element(By.ID, 'searchInput').send_keys("Login by Phone")
        driver.find_element(By.ID, 'search-submit').click()
        # time.sleep(10)
        links = driver.find_elements(By.XPATH, "//article/a")
        headlines = driver.find_elements(By.XPATH, "//article/a/h1")
        contents = driver.find_elements(By.XPATH, "//article/a/p")
        results_links = []
        result_headlines = []
        result_contents = []
        for link in links:
            href = link.get_attribute("href")
            results_links.append(href)

        for headline in headlines:
            heading = headline.text
            result_headlines.append(heading)

        for content in contents:
            paragraph = content.text
            result_contents.append(paragraph)
        print("\n")
        for head, content, link_url in zip(result_headlines, result_contents, results_links):
            print(head)
            print(content)
            print(link_url)
            print("\n")

        if len(results_links) > 0:
            print("Search result displayed successfully.")
        driver.close()


if __name__ == "__main__":
    unittest.main()
