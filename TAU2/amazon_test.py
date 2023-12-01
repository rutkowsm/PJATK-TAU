from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
import time

# Konfiguracja przeglądarki
driver = webdriver.Chrome()

# Otwarcie strony Amazon
driver.get("https://www.amazon.com")
print("Strona Amazon została otwarta.")

# Znalezienie paska wyszukiwania i wpisanie szukanego produktu
search_box = driver.find_element(By.ID, "twotabsearchtextbox")
search_box.clear()
search_box.send_keys("Echo Dot")
search_box.send_keys(Keys.RETURN)
print("Wyszukiwanie produktu zostało wykonane.")

# Oczekiwanie na załadowanie wyników wyszukiwania
time.sleep(2)

# Weryfikacja wyników
if "Echo Dot" in driver.page_source:
    print("Test zakończony sukcesem - znaleziono wyniki wyszukiwania.")
else:
    print("Test nieudany - brak wyników wyszukiwania.")

# Zamknięcie przeglądarki
driver.quit()
