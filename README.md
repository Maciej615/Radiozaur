# 🎵 Radiozaur

Radiozaur to prosty odtwarzacz internetowych stacji radiowych napisany w Pythonie.  
Powstał w celach edukacyjnych – jako projekt do nauki i zabawy, a także jako pokaz umiejętności programistycznych.

---

## ✨ Funkcje
- 🎶 Odtwarzanie stacji radiowych przy użyciu `mpv`  
- 📻 Kilka wbudowanych stacji startowych  
- 🔎 Wyszukiwanie i dodawanie nowych stacji z [Radio-Browser](https://www.radio-browser.info/)  
- ⭐ Obsługa listy ulubionych stacji  
- 🎨 Lekki interfejs Tkinter z motywem `ttkbootstrap`  
- 💾 Zapis konfiguracji (ścieżka do `mpv`, ulubione)  

---

## 📥 Pobierz
👉 [Najnowsza wersja Radiozaura (EXE dla Windows)](../../releases/latest)

---

## ⚙️ Instalacja

### 1. Uruchomienie z Pythona (wersja źródłowa)
1. Pobierz repozytorium:
   ```bash
   git clone https://github.com/<twoj_login>/radiozaur.git
   cd radiozaur
````

2. Zainstaluj wymagane biblioteki:

   ```bash
   pip install -r requirements.txt
   ```
3. Uruchom aplikację:

   ```bash
   python radiozaur.py
   ```

---

### 2. Wersja EXE (Windows)

1. Pobierz plik `Radiozaur.exe` z [Releases](../../releases/latest).
2. Upewnij się, że w systemie jest dostępny `mpv.exe` (można pobrać z [mpv.io](https://mpv.io/)).
3. Umieść `mpv.exe` w tym samym katalogu co `Radiozaur.exe`.
4. Uruchom `Radiozaur.exe`.

---

### 3. Kompilacja własna (Nuitka)

Możesz samodzielnie zbudować plik EXE:

```bash
nuitka --onefile --enable-plugin=tk-inter --windows-icon-from-ico=radiozaur.ico --windows-console-mode=disable radiozaur.py
```

---

## ❓ FAQ

### 1. Nie działa odtwarzanie

Sprawdź, czy w katalogu aplikacji znajduje się `mpv.exe`.
Radiozaur korzysta z odtwarzacza MPV jako backendu.

---

### 2. Jak uruchomić nową stację?

W aplikacji wpisz nazwę stacji i kliknij „🔍 Szukaj stacji”,
a następnie wybierz ją z listy i kliknij „▶️ Odtwórz”.

---

### 3. Czy działa na Linux/Mac?

Tak, w wersji źródłowej (Python). Potrzebny jest tylko zainstalowany `mpv`.

---

### 4. Dlaczego exe jest tak duże?

Nuitka pakuje cały interpreter Pythona i biblioteki w jeden plik, dlatego exe ma kilkadziesiąt MB.

---

## 📜 Licencja

Radiozaur – odtwarzacz internetowych stacji radiowych
Autor: **Maciek**

Projekt dostępny na licencji: **Creative Commons Attribution-NonCommercial 4.0 International (CC BY-NC 4.0)**

👉 Szczegóły: [https://creativecommons.org/licenses/by-nc/4.0/](https://creativecommons.org/licenses/by-nc/4.0/)

### Warunki licencji:

* ✅ Możesz używać, kopiować i modyfikować projekt
* ✅ Możesz udostępniać własne modyfikacje (z podaniem autora)
* ❌ Nie wolno używać projektu w celach komercyjnych


```

