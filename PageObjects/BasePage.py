from selenium.webdriver.common.by import By


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    def get_element(self, locator_name, locator_value):
        element = None
        if locator_name.__contains__("xpath"):
            element = self.driver.find_element(By.XPATH, locator_value)
        elif locator_name.__contains__("css"):
            element = self.driver.find_element(By.CSS_SELECTOR, locator_value)
        elif locator_name.__contains__("_name"):
            element = self.driver.find_element(By.NAME, locator_value)
        elif locator_name.__contains__("_id"):
            element = self.driver.find_element(By.ID, locator_value)
        elif locator_name.__contains__("_class"):
            element = self.driver.find_element(By.CLASS_NAME, locator_value)
        elif locator_name.__contains__("_link_text"):
            element = self.driver.find_element(By.LINK_TEXT, locator_value)
        elif locator_name.__contains__("_tag"):
            element = self.driver.find_element(By.TAG_NAME, locator_value)
        elif locator_name.__contains__("_partial_link_text"):
            element = self.driver.find_element(By.PARTIAL_LINK_TEXT, locator_value)
        return element

    def get_elements(self, locator_name, locator_value):
        elements = None
        if locator_name.__contains__("_xpath"):
            elements = self.driver.find_elements(By.XPATH, locator_value)
        elif locator_name.__contains__("_css"):
            elements = self.driver.find_elements(By.CSS_SELECTOR, locator_value)
        elif locator_name.__contains__("_name"):
            elements = self.driver.find_elements(By.NAME, locator_value)
        elif locator_name.__contains__("_id"):
            elements = self.driver.find_elements(By.ID, locator_value)
        elif locator_name.__contains__("_class"):
            elements = self.driver.find_elements(By.CLASS_NAME, locator_value)
        elif locator_name.__contains__("_link_text"):
            elements = self.driver.find_elements(By.LINK_TEXT, locator_value)
        elif locator_name.__contains__("_tag"):
            elements = self.driver.find_elements(By.TAG_NAME, locator_value)
        elif locator_name.__contains__("_partial_link_text"):
            elements = self.driver.find_elements(By.PARTIAL_LINK_TEXT, locator_value)
        return elements

    def type_in_the_element(self, locator_name,locator_value, text):
        element = self.get_element(locator_name, locator_value)
        element.click()
        element.send_keys(text)

    def click_element(self, locator_name,locator_value):
        element = self.get_element(locator_name,locator_value)
        element.click()