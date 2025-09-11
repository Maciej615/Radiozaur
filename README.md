"""
=====================================================
🎵 Radiozaur – odtwarzacz internetowych stacji radiowych
=====================================================

Autor: Maciej
Licencja: CC BY-NC 4.0
(https://creativecommons.org/licenses/by-nc/4.0/)

Opis:
------
Radiozaur to prosty odtwarzacz internetowych stacji radiowych napisany w Pythonie.
Projekt stworzony w celu nauki, zabawy oraz jako pokaz umiejętności programistycznych.
Plik do pobrania:
https://github.com/Maciej615/Radiozaur/releases/download/1.0/radiozaur.exe
⚠ Wymagania:
-------------
- Python 3.10+ 
- Plik mpv.exe dostępny w PATH lub wskazany ręcznie w konfiguracji
- Biblioteki Python: python-mpv, ttkbootstrap
- Plik ikony (opcjonalnie): radiozaur.ico

Funkcje:
--------
- Odtwarzanie stacji radiowych przy użyciu mpv.exe
- Kilkanaście wbudowanych stacji startowych
- Wyszukiwanie i dodawanie nowych stacji
- Lekki interfejs Tkinter z motywem ttkbootstrap
- Obsługa listy ulubionych stacji
- Zapis konfiguracji ścieżki do mpv.exe

Instalacja:
-----------
1. Zainstaluj wymagane biblioteki:
   pip install -r requirements.txt
   lub ręcznie:
   pip install python-mpv ttkbootstrap

2. Uruchom aplikację:
   python radiozaur.py
   (przy pierwszym uruchomieniu wskaż ścieżkę do mpv.exe, jeśli nie jest w PATH)

Kompilacja do EXE (Windows, Nuitka):
-------------------------------------
nuitka --onefile --enable-plugin=tk-inter --windows-icon-from-ico=radiozaur.ico --windows-console-mode=disable radiozaur.py

Po kompilacji powstanie radiozaur.exe, gotowy do uruchomienia.
"""
