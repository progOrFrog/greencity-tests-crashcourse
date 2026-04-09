import unittest
import time
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class TestGreenCityEvents(unittest.TestCase):

    def setUp(self):
        options = webdriver.ChromeOptions()
        options.add_argument('--window-size=1920,1080')
        self.driver = webdriver.Chrome(options=options)
        self.wait = WebDriverWait(self.driver, 15)
        
        self.driver.get("https://www.greencity.cx.ua/#/greenCity/events")
        
        self.wait.until(EC.presence_of_element_located((By.XPATH, "//p[@class='main-header' and contains(text(), 'Events')]")))

    def tearDown(self):
        if self.driver:
            self.driver.quit()

    def test_tc_01_switch_display_mode(self):
        """TC-01: Switching event display mode (Grid/List view)"""
        grid_view_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.gallery[aria-label='table view']")))
        list_view_btn = self.wait.until(EC.presence_of_element_located((By.CSS_SELECTOR, "button.list[aria-label='list view']")))

        list_view_btn.click()
        self.wait.until(lambda d: list_view_btn.get_attribute("aria-pressed") == "true")

        self.assertEqual(list_view_btn.get_attribute("aria-pressed"), "true", "List view failed to activate")
        self.assertEqual(grid_view_btn.get_attribute("aria-pressed"), "false", "Grid view is still active when it shouldn't be")

        grid_view_btn.click()
        self.wait.until(lambda d: grid_view_btn.get_attribute("aria-pressed") == "true")

        self.assertEqual(grid_view_btn.get_attribute("aria-pressed"), "true", "Grid view failed to activate")
        self.assertEqual(list_view_btn.get_attribute("aria-pressed"), "false", "List view is still active when it shouldn't be")

    def test_tc_02_view_event_details(self):
        """TC-02: Viewing detailed information about an event"""
        
        more_buttons = self.wait.until(EC.presence_of_all_elements_located(
            (By.CSS_SELECTOR, "app-events-list-item button.secondary-global-button")
        ))
        
        self.assertTrue(len(more_buttons) > 0, "No events found on the page")
        
        self.driver.execute_script("arguments[0].click();", more_buttons[0])
        
        back_button = self.wait.until(EC.presence_of_element_located(
            (By.XPATH, "//*[contains(text(), 'Back')]")
        ))
        
        self.assertTrue(back_button.is_displayed(), "Failed to open event details page")

    def test_tc_04_create_event_unauthorized(self):
        """TC-04 (Negative): Attempting to create an event as an unauthorized user"""
        

        create_event_btn = self.wait.until(EC.element_to_be_clickable(
            (By.CSS_SELECTOR, "div.create button.secondary-global-button")
        ))
        create_event_btn.click()
        
        login_modal = self.wait.until(EC.visibility_of_element_located(
            (By.XPATH, "//h2[contains(text(), 'Sign in')] | //app-auth-modal | //mat-dialog-container")
        ))
        
        self.assertTrue(login_modal.is_displayed(), "Login modal did not appear for an unauthorized user")
        
if __name__ == "__main__":
    unittest.main()