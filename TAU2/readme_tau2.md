Scenariusz Testu dla Strony Amazon
Testowanie funkcji wyszukiwania na stronie e-commerce Amazon, konkretnie wyszukiwanie produktu "Echo Dot".

Kroki:
1. Otwarcie Strony Amazon: Otwórz stronę główną Amazon (www.amazon.com) za pomocą przeglądarki Chrome.
2. Znalezienie i Użycie Paska Wyszukiwania: Zlokalizuj pasek wyszukiwania na stronie Amazon, który jest identyfikowany przez jego ID, "twotabsearchtextbox".
3. Wprowadzenie Zapytania Wyszukiwania: Wyczyść pole wyszukiwania, wpisz frazę "Echo Dot" i wyślij zapytanie, naciskając klawisz Enter.
4. Oczekiwanie na Wyniki: Poczekaj krótko (2 sekundy), aby strona załadowała wyniki wyszukiwania.
5. Weryfikacja Wyników Wyszukiwania: Sprawdź, czy na stronie wyników wyszukiwania zawarto frazę "Echo Dot", co wskazywałoby na znalezienie szukanego produktu.

Zakończenie Testu:
1. Jeśli fraza "Echo Dot" jest obecna na stronie wyników, test kończy się sukcesem, wskazując, że produkt został znaleziony.
2. Jeśli fraza nie jest obecna, test kończy się niepowodzeniem, sugerując, że wyniki wyszukiwania nie zawierają szukanego produktu.
3. Zamknięcie Przeglądarki: Niezależnie od wyniku, test kończy się zamknięciem przeglądarki.

Scenariusz Testu dla Strony "Trojmiasto.pl"
Testowanie funkcji wyszukiwania na lokalnej stronie informacyjnej "Trojmiasto.pl", konkretnie wyszukiwanie informacji o "kulturze".

Kroki:
1. Otwarcie Strony "Trojmiasto.pl": Uruchom przeglądarkę Edge i otwórz stronę "Trojmiasto.pl".
2. Znalezienie Pola Wyszukiwania: Użyj WebDriverWait z Selenium, aby poczekać maksymalnie 10 sekund na pojawienie się pola wyszukiwania, które jest identyfikowane przez atrybut name o wartości "string".
3. Wprowadzenie Zapytania Wyszukiwania: Wyczyść pole wyszukiwania, wpisz frazę "kultura" i przygotuj się do wysłania zapytania.
4. Wyszukiwanie Przycisku Wyszukiwania i Kliknięcie: Znajdź przycisk wyszukiwania na stronie, używając selektora klasy By.CLASS_NAME o wartości "button--secondary", a następnie kliknij ten przycisk, aby wysłać zapytanie.

Zakończenie Testu:
1. W przypadku powodzenia, skrypt wydrukuje informację o wykonaniu wyszukiwania.
2. W przypadku napotkania wyjątku, skrypt wydrukuje komunikat błędu.
3. Zamknięcie Przeglądarki: Niezależnie od wyniku, test kończy się zamknięciem przeglądarki.  
