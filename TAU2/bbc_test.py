from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# Konfiguracja przeglądarki Edge
driver = webdriver.Edge()

# Otwarcie strony trojmiasto.pl
driver.get("https://www.trojmiasto.pl")
print("Strona trojmiasto.pl została otwarta.")

try:
    # Wyszukiwanie pola do wprowadzania zapytania
    search_box = WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.NAME, "string"))  # Selektor 'name' dla pola wyszukiwania
    )
    search_box.clear()
    search_box.send_keys("kultura")

    # Wyszukiwanie przycisku wyszukiwania i kliknięcie
    search_button = driver.find_element(By.CLASS_NAME, "button--secondary")
    search_button.click()

    print("Wyszukiwanie informacji zostało wykonane.")

except Exception as e:
    print(f"Wystąpił błąd: {e}")

# Zamknięcie przeglądarki
driver.quit()

