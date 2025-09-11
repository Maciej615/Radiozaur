"""
=====================================================
🎵 Radiozaur – odtwarzacz internetowych stacji radiowych
=====================================================

Autor: Maciek
Licencja: CC BY-NC 4.0
(https://creativecommons.org/licenses/by-nc/4.0/)

Opis:
------
Radiozaur to prosty odtwarzacz internetowych stacji radiowych napisany w Pythonie.
Projekt stworzony w celu nauki, zabawy oraz jako pokaz umiejętności programistycznych.

Funkcje:
--------
- Odtwarzanie stacji radiowych przy użyciu mpv
- Kilkanaście wbudowanych stacji startowych
- Wyszukiwanie i dodawanie nowych stacji
- Lekki interfejs Tkinter z motywem ttkbootstrap
- Obsługa listy ulubionych stacji
- Zapis konfiguracji ścieżki do mpv

Instalacja:
-----------
1. Zainstaluj wymagane biblioteki:
   pip install -r requirements.txt
   lub ręcznie:
   pip install python-mpv ttkbootstrap

2. Uruchom aplikację:
   python radiozaur.py

Kompilacja do EXE (Windows, Nuitka):
-------------------------------------
nuitka --onefile --enable-plugin=tk-inter --windows-icon-from-ico=radiozaur.ico --windows-console-mode=disable radiozaur.py
"""
