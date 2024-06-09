# Wtyczka programu QGIS

## Spis treści 
* [Ogólne informacje](#ogólne-informacje)
* [Wymagania sprzętowe](#wymagania-sprzętowe)
* [Funkcje](#funkcje)
* [Struktura plików wejściowych](#struktura-plików-wejściowych)
* [Uruchomienie programu](#uruchomienie-programu)
* [Przykłady użycia](#przykłady-użycia)
* [Znane błędy](#znane-błędy)

## Ogólne informacje
Celem programu jest stworzenie wtyczki, która na podstawie współrzędnych dwóch punktów liczy przewyższenie między nimi oraz dla każdych trzech punktów liczy pole powierzchni.

## Wymagania sprzętowe
Wymagania, które musi spełnić komputer użytkownika:
1. Posiadanie wersji programu [Python 3.8 lub wyższej](https://www.python.org/downloads/).
2. Posiadanie wersji programu [QGIS 3.34.5 lub wyższej](https://qgis.org/pl/site/forusers/download.html).
3. Zainstalowane biblioteki os, qgis.PyQt, qgis.core, qgis.utils
4. Dane wejściowe muszą być zapisane w pliku tekstowym.
5. Posiadanie systemu operacyjnego Windows, MacOS lub Linux.

## Funkcje
1. Przewyższenie
Aby obliczyć przewyższenie między punktami, należy wybrać dwa różne punkty na tej samej warstwie. Dzięki wtyczce, program obliczy różnice wysokości między tymi punktami na podstawie ich współrzędnych.

2. Pole powierzchni
Aby obliczyć pole powierzchni między punktami, należy wybrać co najmniej trzy różne punkty na tej samej warstwie. Dzięki wtyczce, program obliczy pole powierzchni zawarte między tymi punktami na podstawie ich współrzędnych.

## Struktura plików wejściowych
## Uruchomienie programu
1. Aby uruchomić program, Pobierz Python oraz QGIS w odpowiedniej wersji. Możesz w tym celu skorzystać z odnośników zamieszczonych w zakładce [Wymagania sprzętowe](#wymagania-sprzętowe).
2. Pobraną wtyczkę zamieść w folderze z wtyczkami QGIS, np.:
```
C:\Users\* TWOJA_NAZWA_UŻYTKOWNIKA *\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins
```
> [!TIP]
>  Aby znaleźć lokalizację folderu z wtyczkami należy wybrać w QGIS-ie Ustawienia > Profile użytkownika > Otwórz katalog aktywnego profilu. <br>
3. Następnie, w programie QGIS, udaj się do zakładki 'Wtyczki' i wybierz 'Zarzdządzanie wtyczkami'. W panelu 'Ustawienia', zaznacz opcję 'Pokazuj również wtyczki eksperymentalne'. Do odświeżenia repozytorium, użyj przycisku 'Wczytaj ponownie zawartość repozytorium'. Teraz wtyczka powinna być widoczna w panelu 'Wszystkie'. Musisz ją pobrać, klikając 'Zainstaluj wtyczkę eksperymentalną' znajdujące się w prawym dolnym rogu okna. Teraz wtyczka pojawia się w liście rozwijalnej zakładki 'Wtyczki'.
> [!TIP]
> Jeśli po wykonaniu powyższych kroków wtyczka nie pojawia się na liście dostępnych wtyczek, powinna pomóc opcja 'Instaluj z pliku ZIP' dostępna w oknie Zarządzania wtyczkami. 
4. Po wczytaniu interesujących Cię warstw, możesz zacząć pracować z wtyczką. Zależnie od funkcji, której chcesz użyć, zaznacz dwa lub trzy punkty.

## Przykłady użycia
## Znane błędy
