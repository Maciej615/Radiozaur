
-----

# 🎵 Radiozaur

Prosty i lekki odtwarzacz internetowych stacji radiowych napisany w Pythonie.

<br>

**Radiozaur** powstał jako projekt edukacyjny – stworzony do nauki i zabawy, a jednocześnie będący demonstracją umiejętności programistycznych.

-----

## ✨ Główne Funkcje

  * **🎶 Płynne odtwarzanie** — Wykorzystuje potężny silnik `mpv` do odtwarzania strumieni radiowych.
  * **📻 Wbudowane stacje** — Zawiera listę gotowych stacji, abyś mógł zacząć słuchać od razu po uruchomieniu.
  * **🔎 Wyszukiwarka stacji** — Zintegrowana z bazą [Radio-Browser](https://www.radio-browser.info/), daje dostęp do tysięcy stacji z całego świata.
  * **🎨 Lekki interfejs** — Szybki i prosty interfejs oparty na Tkinter z nowoczesnym motywem `ttkbootstrap`.
  * **💾 Zapisywanie ustawień** — Aplikacja zapamiętuje ścieżkę do odtwarzacza `mpv`.
  * **🌍 Dwa języki interfejsu** — Możliwość przełączania między językiem polskim (PL) a angielskim (EN).

-----

## ⚙️ Instalacja i Uruchomienie

### Wymagania wstępne

  * **Python 3.7+** (dla wersji źródłowej)
  * **Odtwarzacz `mpv`** — Radiozaur używa go do odtwarzania. Pobierz go z [**mpv.io**](https://mpv.io/) i upewnij się, że jest dostępny w systemie.

-----

### **❖ Opcja 1: Wersja .EXE (dla Windows)**

Najprostszy sposób na uruchomienie:

1.  Pobierz plik `Radiozaur.exe` z sekcji [podejrzany link usunięto].
2.  Pobierz `mpv.exe` ze strony [mpv.io](https://mpv.io/).
3.  Umieść pobrany plik `mpv.exe` w tym samym folderze, w którym znajduje się `Radiozaur.exe`.
4.  Uruchom `Radiozaur.exe` i gotowe\!

-----

### **❖ Opcja 2: Uruchomienie ze źródeł (Windows / Linux / macOS)**

Dla użytkowników, którzy chcą uruchomić aplikację bezpośrednio z kodu:

1.  **Sklonuj repozytorium:**

    ```bash
    git clone https://github.com/<twoj_login>/radiozaur.git
    cd radiozaur
    ```

2.  **Zainstaluj zależności:**

    ```bash
    pip install -r requirements.txt
    ```

3.  **Uruchom aplikację:**

    ```bash
    python radiozaur.py
    ```

\<details\>
\<summary\>\<b\>❖ Opcja 3: Samodzielna kompilacja do .EXE (zaawansowane)\</b\>\</summary\>

Możesz samodzielnie zbudować plik wykonywalny przy użyciu Nuitka. Upewnij się, że masz zainstalowane odpowiednie pakiety Pythona, a następnie wykonaj polecenie w terminalu:

```bash
nuitka --onefile --windows-icon-from-ico=radiozaur.ico --windows-console-mode=disable --enable-plugin=tk-inter radiozaur.py
```

\</details\>

-----

## 🚀 Jak Używać?

1.  **Uruchom aplikację.**
2.  Wybierz jedną ze stacji z listy i kliknij **▶️ Odtwórz**.
3.  Aby znaleźć nową stację, wpisz jej nazwę (lub gatunek) w polu wyszukiwania i kliknij **🔍 Szukaj stacji**.
4.  Wybierz interesującą Cię pozycję z wyników i rozpocznij odtwarzanie.

-----

## 💡 FAQ - Często Zadawane Pytania

**1. Odtwarzanie nie działa, nic nie słychać.**

> Najprawdopodobniej brakuje pliku `mpv.exe` (w przypadku wersji dla Windows) lub `mpv` nie jest zainstalowany w systemie (dla wersji źródłowej). Upewnij się, że odtwarzacz jest dostępny i ewentualnie wskaż poprawną ścieżkę w ustawieniach aplikacji.

**2. Czy aplikacja działa na systemach Linux lub macOS?**

> Tak, wersja uruchamiana ze źródeł (przez Pythona) działa na każdym systemie, na którym można zainstalować `mpv` i biblioteki z pliku `requirements.txt`.

**3. Dlaczego plik `.exe` jest taki duży?**

> Plik wykonywalny stworzony przez Nuitka zawiera w sobie nie tylko kod aplikacji, ale również cały interpreter Pythona i wszystkie wymagane biblioteki. Dzięki temu jest w pełni przenośny i nie wymaga instalacji Pythona na docelowym komputerze.

-----

## 📜 Licencja

**Radiozaur – odtwarzacz internetowych stacji radiowych** Autor: **Maciek**

Projekt udostępniany jest na licencji **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**.

👉 Pełna treść licencji: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

### W skrócie:

  * ✅ **Możesz** używać, kopiować i modyfikować ten projekt na własne potrzeby.
  * ✅ **Możesz** udostępniać swoje zmodyfikowane wersje, pod warunkiem podania autora oryginału.
  * ❌ **Nie możesz** używać tego projektu ani jego pochodnych w celach komercyjnych.
