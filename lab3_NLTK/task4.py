import re


email_data = """
john.doe@example.com - John Doe
jane.smith@gmail.com - Jane Smith
bob.jones@yahoo.com - Bob Jones
alice.wonderland@hotmail.com - Alice Wonderland
"""

# Отримання списку доменів електронних адрес за допомогою регулярного виразу
email_domains_list = re.findall(r'@([a-zA-Z0-9.-]+)', email_data)
print(f"List of email address domains: {email_domains_list}")
