from io import BytesIO

from django.test import TestCase, Client
from django.urls import reverse

# Create your tests here.
class FileProcessingTestCase(TestCase):

    def setUp(self):
        self.client = Client()
        self.upload_url = reverse('')

    def test_upload_txt_file(self):

        file_content = b'This is a test document. \nIt has multiple lines. \nMultiple lines'
        file = BytesIO(file_content)
        file.name = 'test.txt'

        response = self.client.post(self.upload_url, {
            'file': file
        }, format="multipart")

        self.assertEquals(response.status_code, 200)