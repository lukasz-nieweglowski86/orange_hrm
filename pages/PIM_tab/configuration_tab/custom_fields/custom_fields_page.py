import repo.orange_hrm.data.PIM_tab.add_custom_field_page as add_custom_field_data


page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/listCustomFields'
buttons = {
    'add': '//button[text()=" Add "]',
    'removal_confirmation': '//button[text()=" Yes, Delete "]',
    'removal_cancellation': '//button[text()=" No, Cancel "]'
}
icons = {
    'edit': '//div[text()="{}"]/following::button[2]'.format(add_custom_field_data.inputs['field_name']),
    'delete': '//div[text()="{}"]/following::button[1]'.format(add_custom_field_data.inputs['field_name'])
}
