@echo off
:poczatek
cls
echo -----------------
echo    Menu Glowne
echo -----------------
echo.
echo 1) Zasady dzialanie programu
echo 2) Uruchomienie programow
echo 3) Raporty
echo 4) Usuwanie raportow
echo 5) Koniec
echo.

set /p opcja=Wybierz:
if %opcja%==1 goto opcja1
if %opcja%==2 goto opcja2
if %opcja%==3 goto opcja3
if %opcja%==4 goto opcja4
if %opcja%==5 exit
goto zly_wybor

:opcja1
cls
echo ------------------------------ 
echo
echo Dzialanie programu:
echo "program.py"
echo Otwiera on plik 'IN.txt' i dla podanych liczb wyszukuje wielokrotnosc
echo skladajaca sie wylacznie z zer i jedynek, a nastepnie zapisuje je do pliku 'OUT.txt'.
echo
echo "html.py"
echo Korzystajac z plikow 'IN.txt' oraz 'OUT.txt' program tworzy tabele w HTML z wczytanych liczb i
echo tworzy plik, ktory zapisuje do folderu raporty.
echo
echo ------------------------------
pause
goto poczatek

:opcja2
cls
call program.py
call html.py
goto poczatek

:opcja3
cls
start %windir%\explorer.exe raporty
goto poczatek

:opcja4
cls
del /q raporty\*
goto poczatek

:zly_wybor
echo Opcja nie znana, wybierz ponownie.
pause
goto poczatek