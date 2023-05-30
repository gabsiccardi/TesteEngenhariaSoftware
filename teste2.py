from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Set up Selenium WebDriver (make sure to install the appropriate webdriver for your browser)
driver = webdriver.Chrome()  # Assuming you're using Chrome. Adjust if using a different browser.
driver.get("file:///path/to/your/html/file.html")  # Replace with the actual path to your HTML file

# Input the first set of values
name_input = driver.find_element_by_id("name")
surname_input = driver.find_element_by_id("surname")
email_input = driver.find_element_by_id("email")

name_input.send_keys("John")
surname_input.send_keys("Smith")
email_input.send_keys("johnsmith@example.com")

# Submit the form
email_input.send_keys(Keys.RETURN)

# Wait for a moment to observe the result
driver.implicitly_wait(5)

# Clear the form fields
name_input.clear()
surname_input.clear()
email_input.clear()

# Input the second set of values
name_input.send_keys("Emily")
surname_input.send_keys("Johnson")
email_input.send_keys("emilyjohnson@example.com")

# Submit the form
email_input.send_keys(Keys.RETURN)

# Wait for a moment to observe the result
driver.implicitly_wait(5)

# Clear the form fields
name_input.clear()
surname_input.clear()
email_input.clear()

# Input the third set of values
name_input.send_keys("Michael")
surname_input.send_keys("Davis")
email_input.send_keys("michael.davis@example.com")

# Submit the form
email_input.send_keys(Keys.RETURN)

# Wait for a moment to observe the result
driver.implicitly_wait(5)

# Close the browser
driver.quit()
