import unittest
from selenium import webdriver


class ConvertingTests(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.get('https://www.metric-conversions.org/')

    def tearDown(self):
        self.driver.quit()

    def test_temp_conversion(self):
        temp_conversion_button = self.driver.find_element_by_class_name('temperature')
        temp_conversion_button.click()

        celsius_to_fahrenheit_button = self.driver.find_element_by_xpath('//*[@id="popLinks"]/ol/li[1]/a')
        celsius_to_fahrenheit_button.click()

        form = self.driver.find_element_by_id('argumentConv')
        form.send_keys('36.6')
        form.submit()

        answer = self.driver.find_element_by_xpath('//*[@id="answer"]')
        result = answer.text
        result_expected = '36.6°C= 97.88000°F'
        self.assertEqual(result, result_expected)

    def test_length_conversion(self):
        length_conversion_button = self.driver.find_element_by_class_name('length')
        length_conversion_button.click()

        meters_to_feet_button = self.driver.find_element_by_xpath('//*[@id="popLinks"]/ol/li[1]/a')
        meters_to_feet_button.click()

        form = self.driver.find_element_by_id('argumentConv')
        form.send_keys('25')
        form.submit()

        answer = self.driver.find_element_by_xpath('//*[@id="answer"]')
        result = answer.text
        result_expected = '25m= 82ft 0.2519700in'
        self.assertEqual(result, result_expected)

    def test_weight_conversion(self):
        weight_conversion_button = self.driver.find_element_by_class_name('weight')
        weight_conversion_button.click()

        ounces_to_grams_button = self.driver.find_element_by_xpath('//*[@id="popLinks"]/ol/li[5]/a')
        ounces_to_grams_button.click()

        form = self.driver.find_element_by_id('argumentConv')
        form.send_keys('1')
        form.submit()

        answer = self.driver.find_element_by_xpath('//*[@id="answer"]')
        result = answer.text
        result_expected = '1oz= 28.34952g'
        self.assertEqual(result, result_expected)


if __name__ == '__main__':
    unittest.main()
