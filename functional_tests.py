from email import header
import imp
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
import unittest



class NewVisitorTest(unittest.TestCase):

    def setUp(self):
        self.browser = webdriver.Firefox()


    def tearDown(self):
        self.browser.quit()   


    def test_can_start_a_list_and_retrieve_it_later(self):
        # open the web app
        self.browser.get('http://localhost:8000')
        # notices the title of the page
        self.assertIn('To-Do',self.browser.title)
        #notices the contents of the page
        header_text = self.browser.find_element_by_tag_name('h1').text
        self.assertIn('To-Do', header_text)

        # seeing a field with placeholder 'Enter a to-do item
        input_box = self.browser.find_element_by_id('id_new_item')
        self.assertEqual(input_box.get_attribute('placeholder'), 'Enter a to-do item')
        
        # enter an item
        input_box.send_keys('Push code to Github Repo')

        # saves the item by tapping 'Enter'
        input_box.send_keys(Keys.ENTER)
        time.sleep(1)

        table = self.browser.find_element_by_id('id_list_table')
        rows = table.find_elements_by_id('tr')
        self.assertTrue(
            any(row.text == '1: Push code to Github Repo' for row in rows)
        )

        self.fail('Finish the test!')


if __name__ == '__main__':
    unittest.main(warnings='ignore')
