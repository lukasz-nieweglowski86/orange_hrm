page_url = 'https://opensource-demo.orangehrmlive.com/web/index.php/pim/saveCustomFields'
inputs = {
    'field_name': '//label[text()="Field Name"]/following::input[1]',
    'select_options': '//label[text()="Select Options"]/following::input[1]'
}
buttons = {
    'save': '//button[text()=" Save "]',
    'cancel': '//button[text()=" Cancel "]'
}
dropdowns = {
    'screen': '//label[text()="Screen"]/following::i[1]',
    'type': '//label[text()="Type"]/following::i[1]'
}
screen_options = {
    'select': '//div[@role="option" and text()="-- Select --"]',
    'personal_details': '//span[text()="Personal Details"]',
    'contact_details': '//span[text()="Contact Details"]',
    'emergency_contacts': '//span[text()="Emergency Contacts"]',
    'dependents': '//span[text()="Dependents"]',
    'immigration': '//span[text()="Immigration"]',
    'job': '//span[text()="Job"]',
    'salary': '//span[text()="Salary"]',
    'tax_exemptions': '//span[text()="Tax Exemptions"]',
    'report_to': '//span[text()="Report-to"]',
    'qualifications': '//span[text()="Qualifications"]',
    'memberships': '//span[text()="Memberships"]'
}
types = {
    'select': '//div[@role="option" and text()="-- Select --"]',
    'text': '//span[text()="Text or Number"]',
    'dropdown': '//span[text()="Drop Down"]'
}
error_messages = {
    'missing_field_name': '//label[text()="Field Name"]/following::span[text()="Required"][1]',
    'missing_screen': '//label[text()="Screen"]/following::span[text()="Required"][1]',
    'missing_type': '//label[text()="Type"]/following::span[text()="Required"][1]',
    'missing_options': '//label[text()="Select Options"]/following::span[text()="Required"][1]'
}
