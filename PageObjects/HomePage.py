from selenium.webdriver.common.by import By

from PageObjects.BasePage import BasePage
# from Utilities.ExcelUtils import ExcelUtils


class Home_Page(BasePage):

    def __init__(self, driver):
        super().__init__(driver)


    username_id = 'user-name'
    password_id ='password'
    login_button_id = 'login-button'
    error_message_xpath = "//h3[@data-test='error']"


    def enter_username(self, text):
        self.type_in_the_element('username_id',self.username_id, text)
    def enter_password(self, text):
        self.type_in_the_element('password_id',self.password_id, text)
    def click_on_login_button(self):
        self.click_element('login_button_id',self.login_button_id)
    def verify_error_message(self):
        error_element=self.get_element('error_message_xpath',self.error_message_xpath)
        return error_element.text

    # def enter_text_in_the_search_box(self, file_path, sheet_name, row, column):
    #     search_text = ExcelUtils(file_path).get_cell_data(sheet_name, row, column)
    #     self.type_in_the_element('search_field_xpath',self.search_field_xpath, search_text)
    # def displayed_results(self):
    #     return self.get_elements('results_xpath',self.results_xpath)