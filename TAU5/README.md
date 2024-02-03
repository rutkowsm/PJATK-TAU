
Testowanie Wydajnościowe za pomocą Apache JMeter
1. Obiekt Testowy: Strona primate.diet
   
Opis Testu
Test ma na celu ocenę wydajności strony internetowej primate.diet. W tym teście użyto narzędzia Apache JMeter do symulacji obciążenia.

Ustawienia Testu 1:
- Liczba Użytkowników: 50
- Okres Rozruchu: 5 sekund
- Powtórzenia: 2

Wyniki w tabeli:

![image](https://github.com/rutkowsm/PJATK-TAU/assets/37616390/c36018b7-383f-4f64-bd3a-b27c047b70cf)

Graf:

![image](https://github.com/rutkowsm/PJATK-TAU/assets/37616390/48138d3f-26db-4bb4-a54c-fc2fc03b1dac)

Agregacja:

![image](https://github.com/rutkowsm/PJATK-TAU/assets/37616390/4b21ad7f-8f4b-4448-a87d-3a5e959402e6)


Ustawienia Testu 2:
- Liczba Użytkowników: 1000
- Okres Rozruchu: 5 sekund
- Powtórzenia: 4

Wyniki w tabeli:

![image](https://github.com/rutkowsm/PJATK-TAU/assets/37616390/6aebf505-ac51-4068-bb60-ab9ee4ac9cbc)


Graf:

![image](https://github.com/rutkowsm/PJATK-TAU/assets/37616390/0c3c62f1-8ded-47ed-8991-22eaafc01bbd)


Agregacja:

![image](https://github.com/rutkowsm/PJATK-TAU/assets/37616390/6262d873-24b3-418d-b2f9-da5d0ad460aa)


Analiza wyników dla testu 2 - 100 użytkowników:

- Min: 3968 ms (minimalny czas odpowiedzi) - pokazuje najlepszy czas reakcji serwera na żądanie.
- Max: 159230 ms (maksymalny czas odpowiedzi) - wskazuje na najdłuższy czas odpowiedzi, co może sygnalizować potencjalne wąskie gardła lub problemy z wydajnością pod dużym obciążeniem.
- Średnia: 25770 ms - średni czas odpowiedzi jest stosunkowo wysoki, co może wskazywać na to, że użytkownicy doświadczają zauważalnych opóźnień.
- Odstępstwo standardowe: 21040 - duże odstępstwo standardowe wskazuje na znaczną zmienność czasów odpowiedzi, co może świadczyć o nierównomiernym rozkładzie obciążenia lub niestabilności serwera.
- Percentyl 90%: 63873 ms - 90% żądań zostało obsłużonych w czasie krótszym niż 63.873 sekundy, co nadal jest dość długim czasem oczekiwania.
- ERROR %: 94,96% - Ten wysoki wskaźnik błędów wskazuje na poważne problemy z aplikacją lub infrastrukturą, które uniemożliwiają prawidłowe funkcjonowanie pod obciążeniem generowanym przez 1000 jednoczesnych użytkowników.

Aplikacja prawdopodobnie napotyka krytyczne błędy podczas przetwarzania żądań, co może być spowodowane przeciążeniem serwera, problemami z kodem aplikacji, problemami z bazą danych lub innymi ograniczeniami systemowymi. Na podstawie analizy może być konieczne optymalizowanie kodu aplikacji, zapytań do bazy danych, konfiguracji serwera (np. pule połączeń, timeouty) oraz infrastruktury (np. load balancing, skalowanie).

Analiza jasno pokazuje, że aplikacja Primate.diet jest przystosowana do niskiej liczby użytkowników, zaś przy zwiększonym ruchu jest wrażliwa na przeciążenia.
