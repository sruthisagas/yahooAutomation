__doc__ = '''

Test Case Header:
=================
:Author: Sruthi sagar
:TestId: 01
:Release: NA
:TestName: test_yahooLogin
:Objective: "To verify a user can login to yahoo mail by using mobile number and valid login code"
:Requirements: 1. Already created yahoo account to login by mobile number
:TestDescription: " 1. Fill the Mobile in Mobile field then click Next
                    2. To confirm to receive a login code to his number
                    3. Filling the code that will be received over phone"
:PlanPriority:3 - high
:TestPassCriteria: "If the code was entered successfully the user will login" '''

import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec

class Test(unittest.TestCase):

    def test_loginByPhone(self):

        service_obj = Service("C:/Users/anees/Downloads/chromedriver_win32/chromedriver")
        driver = webdriver.Chrome(service=service_obj)
        # Checking for Admin console Launched or not.
        actual_url = "https://login.yahoo.com/"
        driver.get(actual_url)
        current_url = driver.current_url
        assert actual_url == current_url, "Yahoo login page not launch Successfully."
        print("Yahoo login page launched Successfully.")

        # User needs to enter mobile number which  he wants to log in on yahoo
        login_mobile = input("please enter the mobile number which you want login:")
        driver.find_element("xpath", '//input[@id="login-username"]').send_keys(login_mobile)
        driver.find_element("xpath", '//input[@id="login-signin"]').click()

        # delaying for manually complete the captcha
        time.sleep(20)
        actual_text_send_code_page = driver.find_element(By.CLASS_NAME, 'challenge-heading').text
        expected_text_send_code_page = "Do you have this phone?"
        assert actual_text_send_code_page == expected_text_send_code_page, "page not redirected successfully"
        driver.find_element(By.XPATH, '//button[@name="sendCode"]').click()

        # Negative testing with invalid code
        driver.find_element("xpath", '//input[@id="verification-code-field"]').send_keys("ABCDEFGH")
        time.sleep(5)
        driver.find_element(By.XPATH, '//button[@name="verifyCode"]').click()
        error_msg = driver.find_element(By.CLASS_NAME, 'error-msg').text
        if error_msg == "Invalid verification code":
            print("Error message displayed as expected")
        else:
            print("Error message not displayed")

        # Needs to wait 50s for the resend code button to clickable
        time.sleep(55)
        driver.find_element(By.XPATH, '//button[@name="resendCode"]').click()

        # Sending valid code from console
        login_code = input("please enter the login code received in your mobile number:")
        time.sleep(5)
        driver.find_element("xpath", '//input[@id="verification-code-field"]').send_keys(login_code)
        time.sleep(2)
        element = WebDriverWait(driver, 10).until(
            ec.presence_of_element_located(
                (By.XPATH, '//button[@name="verifyCode"]')))
        driver.execute_script("arguments[0].click();", element)
        time.sleep(2)
        # time.sleep(10)
        # driver.find_element(By.XPATH, '//button[@name="verifyCode"]').click()
        text_after_login = driver.find_element(By.XPATH, '//span[@class="_yb_1si0e"]').text
        assert text_after_login == "Home", "Not logged in successfully"
        print("Logged into yahoo mail successfully.")
        driver.close()


if __name__ == "__main__":
    unittest.main()
