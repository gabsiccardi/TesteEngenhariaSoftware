from selenium import webdriver
from selenium.webdriver.common.keys import Keys

# Instantiate a WebDriver (in this case, using Chrome)
driver = webdriver.Chrome()

# Open Google
driver.get("https://www.google.com")

# Find the search input element and enter a query
search_input = driver.find_element("name", "q")
search_input.send_keys("OpenAI")

# Submit the search query
search_input.send_keys(Keys.RETURN)

# Wait for the search results to load
driver.implicitly_wait(10)

# Verify that the search results page is displayed
assert "Pesquisa Google" in driver.title

# Find the search results and print the titles
search_results = driver.find_elements("css selector", "h3")
for result in search_results:
    print(result.text)

# Close the browser
driver.quit()