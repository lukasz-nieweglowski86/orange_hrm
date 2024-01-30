from selenium.webdriver.common.keys import Keys
from repo.orange_hrm.methods.session import SessionHelper


class Application(SessionHelper):

    def clear_employee_id_input(self):
        employee_id_len = len(self.wd.find_element(self.types['xpath'],
                                                   self.add_employee_page.inputs['employee_id']).get_attribute('value'))
        for i in range(employee_id_len):
            self.wd.find_element(self.types['xpath'],
                                 self.add_employee_page.inputs['employee_id']).send_keys(Keys.BACKSPACE)

    def clear_custom_field_inputs(self, input_name):
        self.wait_for_element_to_be_visible('xpath', self.add_custom_field_page.inputs[input_name])
        custom_field_input_len = len(self.wd.find_element(self.types['xpath'],
                                                          self.add_custom_field_page.inputs[
                                                              input_name]).get_attribute('value'))
        for i in range(custom_field_input_len):
            self.wd.find_element(self.types['xpath'],
                                 self.add_custom_field_page.inputs[input_name]).send_keys(Keys.BACKSPACE)

    def add_employee(self, details, first_name='', middle_name='', last_name='', employee_id='',
                     username='', password='', confirm_password=''):
        self.navigate_to_page(self.add_employee_page.page_url)
        self.fill_input('xpath', self.add_employee_page.inputs['first_name'], first_name)
        self.fill_input('xpath', self.add_employee_page.inputs['middle_name'], middle_name)
        self.fill_input('xpath', self.add_employee_page.inputs['last_name'], last_name)
        self.clear_employee_id_input()
        self.fill_input('xpath', self.add_employee_page.inputs['employee_id'], employee_id)
        if details == 'yes':
            self.click_button('xpath', self.add_employee_page.buttons['create_login_details'])
            self.fill_input('xpath', self.add_employee_page.inputs['username'], username)
            self.fill_input('xpath', self.add_employee_page.inputs['password'], password)
            self.fill_input('xpath', self.add_employee_page.inputs['confirm_password'], confirm_password)
        self.click_button('xpath', self.add_employee_page.buttons['save'])

    def add_custom_field(self, field_name='', screen='', field_type='', dropdown_options=''):
        self.navigate_to_page(self.custom_fields_page.page_url)
        self.click_button('xpath', self.custom_fields_page.buttons['add'])
        self.fill_input('xpath', self.add_custom_field_page.inputs['field_name'], field_name)
        self.select_option_from_dropdown('xpath', self.add_custom_field_page.dropdowns['screen'], screen)
        self.select_option_from_dropdown('xpath', self.add_custom_field_page.dropdowns['type'],
                                         self.add_custom_field_page.types[field_type])
        if field_type == 'dropdown':
            self.fill_input('xpath', self.add_custom_field_page.inputs['select_options'], dropdown_options)
        self.click_button('xpath', self.add_custom_field_page.buttons['save'])
