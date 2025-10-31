from django.test import TestCase
from datetime import datetime

now = datetime.now().strftime('%Y-%m-%d')
print(now)

job_data = {
    'company_name': 'Mugna Tech',
    'address': 'Davao City, Philippines',
    'hiring_manager_name': 'John Doe',
    'company_description': 'Mugna Tech is a software development company that specializes in building web applications.',
    'job_description': 'We are looking for a backend developer to join our team.',
}
# Create your tests here.
