# Wtyczka programu QGIS

## Spis treści 
* [Ogólne informacje](#ogólne-informacje)
* [Wymagania sprzętowe](#wymagania-sprzętowe)
* [Funkcje](#funkcje)
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
**1. Przewyższenie** <br/>
Aby obliczyć przewyższenie między punktami, należy wybrać dwa różne punkty na tej samej warstwie. Dzięki wtyczce, program obliczy różnice wysokości między tymi punktami na podstawie ich współrzędnych.
> [!TIP]
>  Aby znaleźć przewyższenie punktów B-A, użyj przewyższenia punktów A-B z przeciwnym znakiem. <br>

**2. Pole powierzchni** <br/>
Aby obliczyć pole powierzchni między punktami, należy wybrać co najmniej trzy różne punkty na tej samej warstwie. Dzięki wtyczce, program obliczy pole powierzchni zawarte między tymi punktami na podstawie ich współrzędnych.

## Uruchomienie programu
1. Aby uruchomić program, Pobierz Python oraz QGIS w odpowiedniej wersji. Możesz w tym celu skorzystać z odnośników zamieszczonych w zakładce [Wymagania sprzętowe](#wymagania-sprzętowe).
2. Pobraną wtyczkę zamieść w folderze z wtyczkami QGIS, np.:
```
C:\Users\**TWOJA_NAZWA_UŻYTKOWNIKA**\AppData\Roaming\QGIS\QGIS3\profiles\default\python\plugins
```
> [!TIP]
>  Aby znaleźć lokalizację folderu z wtyczkami należy wybrać w QGIS-ie Ustawienia > Profile użytkownika > Otwórz katalog aktywnego profilu. <br>
3. Następnie, w programie QGIS, udaj się do zakładki 'Wtyczki' i wybierz 'Zarzdządzanie wtyczkami'. W panelu 'Ustawienia', zaznacz opcję 'Pokazuj również wtyczki eksperymentalne'. Do odświeżenia repozytorium, użyj przycisku 'Wczytaj ponownie zawartość repozytorium'. Teraz wtyczka powinna być widoczna w panelu 'Wszystkie'. Musisz ją pobrać, klikając 'Zainstaluj wtyczkę eksperymentalną' znajdujące się w prawym dolnym rogu okna. Teraz wtyczka pojawia się w liście rozwijalnej zakładki 'Wtyczki'.
> [!TIP]
> Jeśli po wykonaniu powyższych kroków wtyczka nie pojawia się na liście dostępnych wtyczek, powinna pomóc opcja 'Instaluj z pliku ZIP' dostępna w oknie Zarządzania wtyczkami. 
4. Po wczytaniu interesujących Cię warstw, możesz zacząć pracować z wtyczką.

## Przykłady użycia
Zależnie od funkcji, której chcesz użyć, zaznacz dwa lub więcej punktów. Z rozwijalnej listy warstw wybierz tę, na której znajdują się twoje punkty. Klikajać przycisk 'Zlicz', otrzymasz informację o liczbie zaznaczonych obiektów znajdujących się na tej warstwie. Możesz również wczytać wspólrzędne punktów z pliku tekstowego, używając środkowego panelu. Aby obliczyć przewyższenie, kliknij przycisk 'Oblicz dh'. Jeżeli interesuje Cię pole obszaru, znajdującego się pomiędzy zaznaczonymi punktami, użyj 'Oblicz pole'. Z rozwijalnej listy po prawej, możesz wybrać jednostki powierzchni Twojego wyniku. Na koniec, przyciskiem 'Wyczyść' możesz zrestartować wpisane dane.

## Znane błędy
Podczas tworzenia kodu nie napotkaliśmy na żadne błędy programu.
