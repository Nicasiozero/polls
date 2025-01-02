from selenium import webdriver

# browser = webdriver.Firefox()
browser = webdriver.Chrome()
browser.get("http://localhost:8000")

assert "Calculator" in browser.title
print("OK", browser.title)

# browser.close()