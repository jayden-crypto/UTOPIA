from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

def automate_event_booking(username, password):
    # Set up the WebDriver (provide the path to chromedriver)
    driver = webdriver.Chrome(executable_path='path_to_chromedriver.exe')

    try:
        # Open the college event booking website
        driver.get('https://college-events-example.com')

        # Login
        username_field = driver.find_element_by_id('username')
        password_field = driver.find_element_by_id('password')
        login_button = driver.find_element_by_id('login-button')

        username_field.send_keys(username)
        password_field.send_keys(password)
        login_button.click()

        # Navigate to the events page
        events_page_link = driver.find_element_by_link_text('Events')
        events_page_link.click()

        # Find all available events
        event_buttons = driver.find_elements_by_xpath('//div[@class="event"]/button')

        # Loop through events and book them
        for event_button in event_buttons:
            event_name = event_button.text
            event_button.click()

            # Fill in additional details (ticket count)
            ticket_count_input = driver.find_element_by_id('ticket-count')
            ticket_count_input.send_keys('2')

            # Proceed to payment/confirmation
            proceed_button = driver.find_element_by_id('proceed-button')
            proceed_button.click()

            # Complete the booking process
            confirm_button = driver.find_element_by_id('confirm-button')
            confirm_button.click()

            # Wait for a moment before going back to events page
            time.sleep(5)

            # Go back to events page
            driver.back()

    finally:
        # Close the browser, regardless of success or failure
        driver.quit()

# Replace these values with your actual credentials
username = 'your_username'
password = 'your_password'

# Call the function to automate event booking
automate_event_booking(username, password)