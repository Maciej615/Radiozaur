import ttkbootstrap as ttk
from ttkbootstrap.constants import *
import tkinter.messagebox as messagebox
import subprocess
import urllib.request
import urllib.parse
import json
import shutil
from tkinter import filedialog
import os
import logging

logging.basicConfig(filename='error.log', level=logging.ERROR)

# --- Tłumaczenia ---
translations = {
    "pl": {
        "title": "🎵 Radiozaur",
        "search": "🔍 Szukaj stacji",
        "play": "▶️ Odtwórz wybraną stację",
        "stop": "⏹ Stop",
        "resume": "⏯ Wznów",
        "stream_label": "🎧 Adres strumienia: ",
        "no_station": "Nie ma stacji do wznowienia.",
        "no_results": "Nie znaleziono stacji.",
        "mpv_error": "Nie można uruchomić odtwarzacza",
        "select_mpv": "Nie wybrano poprawnej ścieżki do mpv.exe. Aplikacja zostanie zamknięta."
    },
    "en": {
        "title": "🎵 Radiozaur",
        "search": "🔍 Search station",
        "play": "▶️ Play selected station",
        "stop": "⏹ Stop",
        "resume": "⏯ Resume",
        "stream_label": "🎧 Stream URL: ",
        "no_station": "No station to resume.",
        "no_results": "No stations found.",
        "mpv_error": "Cannot run MPV player",
        "select_mpv": "No valid path to mpv.exe selected. App will close."
    }
}

current_lang = "pl"  # domyślny język

# --- Radiozaur App ---
class RadiozaurApp:
    def __init__(self, root):
        self.root = root
        self.root.title(translations[current_lang]["title"])
        self.root.geometry("460x520")
        self.root.protocol("WM_DELETE_WINDOW", self.on_close)

        self.stations_list = [
            ("RMF FM", "http://195.150.20.242:8000/rmf_fm", "PL"),
            ("Nowy Świat", "http://stream.rcs.revma.com/ypqt40u0x1zuv", "PL"),
            ("Polskie Radio 24", "http://stream3.polskieradio.pl:8902/", "PL")
        ]

        self.current_process = None
        self.paused_station_url = None
        self.player_path = None

        self.setup_gui()
        self.root.after(500, self.init_player)

    def save_path_to_config(self, file_path):
        with open("config.json", "w") as f:
            json.dump({"mpv_path": file_path}, f, indent=4)

    def load_path_from_config(self):
        if os.path.exists("config.json"):
            try:
                with open("config.json", "r") as f:
                    return json.load(f).get("mpv_path")
            except Exception as e:
                logging.error("Error reading config.json", exc_info=True)
        return None

    def get_mpv_path(self):
        config_path = self.load_path_from_config()
        if config_path and os.path.exists(config_path):
            return config_path

        auto_path = shutil.which("mpv")
        if auto_path:
            self.save_path_to_config(auto_path)
            return auto_path

        manual_path = filedialog.askopenfilename(
            title="Select mpv.exe",
            filetypes=[("Executable files", "*.exe")]
        )
        if manual_path and "mpv" in os.path.basename(manual_path).lower():
            self.save_path_to_config(manual_path)
            return manual_path
        return None

    def init_player(self):
        self.player_path = self.get_mpv_path()
        if not self.player_path:
            messagebox.showerror("Error", translations[current_lang]["select_mpv"])
            self.root.after(100, self.root.destroy)

    def setup_gui(self):
        frame = ttk.Frame(self.root, padding=10)
        frame.pack(fill="both", expand=True)

        # --- język ---
        self.btn_lang = ttk.Button(self.root, text=current_lang.upper(), width=4, command=self.switch_language)
        self.btn_lang.place(relx=1.0, x=-10, y=15, anchor="ne")

        self.entry_search = ttk.Entry(frame, width=30)
        self.entry_search.pack(pady=5)
        self.entry_search.bind("<Return>", lambda e: self.on_search())
        self.entry_search.focus_set()

        btn_search = ttk.Button(frame, text=translations[current_lang]["search"], bootstyle=PRIMARY, command=self.on_search)
        btn_search.pack(pady=5)
        self.btn_search = btn_search

        tree_frame = ttk.Frame(frame)
        tree_frame.pack(pady=5, fill="both", expand=True)

        self.tree = ttk.Treeview(tree_frame, columns=("name", "country"), show="headings", height=10, bootstyle=INFO)
        self.tree.heading("name", text="📻 Station")
        self.tree.heading("country", text="🌍 Country")
        self.tree.column("name", anchor="w", width=280)
        self.tree.column("country", anchor="center", width=80)
        self.tree.pack(side="left", fill="both", expand=True)

        scrollbar = ttk.Scrollbar(tree_frame, orient="vertical", command=self.tree.yview)
        scrollbar.pack(side="right", fill="y")
        self.tree.configure(yscrollcommand=scrollbar.set)

        for name, _, country in self.stations_list:
            self.tree.insert("", "end", values=(name, country))

        self.tree.bind("<Double-Button-1>", self.on_tree_select)

        btn_play = ttk.Button(frame, text=translations[current_lang]["play"], bootstyle=SUCCESS, command=self.on_tree_select)
        btn_play.pack(pady=5)
        self.btn_play = btn_play

        self.btn_toggle = ttk.Button(frame, text=translations[current_lang]["stop"], bootstyle=WARNING, command=self.toggle_playback)
        self.btn_toggle.pack(pady=5)

        self.label_url = ttk.Label(frame, text=translations[current_lang]["stream_label"], bootstyle=INFO, anchor="center", wraplength=420)
        self.label_url.pack(pady=10)

    def switch_language(self):
        global current_lang
        current_lang = "en" if current_lang == "pl" else "pl"
        self.btn_lang.config(text=current_lang.upper())
        self.update_texts()

    def update_texts(self):
        self.root.title(translations[current_lang]["title"])
        self.btn_search.config(text=translations[current_lang]["search"])
        self.btn_play.config(text=translations[current_lang]["play"])
        if self.current_process:
            self.btn_toggle.config(text=translations[current_lang]["stop"])
        else:
            self.btn_toggle.config(text=translations[current_lang]["resume"])
        self.label_url.config(text=translations[current_lang]["stream_label"])

    def play_stream(self, url):
        if self.current_process:
            self.current_process.terminate()
            self.current_process = None

        try:
            self.label_url.config(text=f"{translations[current_lang]['stream_label']} {url}")
            command = [self.player_path, "--no-video", "--quiet", url]

            self.current_process = subprocess.Popen(
                command,
                stdout=subprocess.DEVNULL,
                stderr=subprocess.DEVNULL
            )
            self.paused_station_url = url
            self.btn_toggle.config(text=translations[current_lang]["stop"])

        except Exception as e:
            logging.error("MPV error", exc_info=True)
            messagebox.showerror("Error", f"{translations[current_lang]['mpv_error']}:\n{e}")

    def toggle_playback(self):
        if self.current_process:
            self.current_process.terminate()
            self.current_process = None
            self.label_url.config(text="⏸ Playback stopped")
            self.btn_toggle.config(text=translations[current_lang]["resume"])
        elif self.paused_station_url:
            self.play_stream(self.paused_station_url)
        else:
            messagebox.showinfo("Info", translations[current_lang]["no_station"])

    def search_stations_by_name(self, query, limit=20):
        query_encoded = urllib.parse.quote(query)
        url = f"https://de1.api.radio-browser.info/json/stations/byname/{query_encoded}"
        results = []
        try:
            with urllib.request.urlopen(url) as response:
                data = json.loads(response.read())
                for item in data[:limit]:
                    name = item['name']
                    stream = item.get('url_resolved', item['url'])
                    country = item.get('countrycode', '??')
                    results.append((name, stream, country))
        except Exception as e:
            logging.error("Station search error", exc_info=True)
            messagebox.showerror("Error", f"Station search failed:\n{e}")
        return results

    def on_tree_select(self, event=None):
        selected = self.tree.selection()
        if selected:
            index = self.tree.index(selected[0])
            if index < len(self.stations_list):
                name, url, country = self.stations_list[index]
                self.play_stream(url)

    def on_search(self):
        try:
            query = self.entry_search.get().strip()
            if not query:
                return
            results = self.search_stations_by_name(query)
            if results:
                for item in self.tree.get_children():
                    self.tree.delete(item)
                self.stations_list = results
                for name, _, country in self.stations_list:
                    self.tree.insert("", "end", values=(name, country))
            else:
                messagebox.showinfo("Info", translations[current_lang]["no_results"])
        except Exception as e:
            logging.error("Search error", exc_info=True)
            messagebox.showerror("Error", f"Search failed:\n{e}")

    def on_close(self):
        if self.current_process:
            self.current_process.terminate()
        self.root.destroy()


if __name__ == "__main__":
    root = ttk.Window(themename="darkly")
    app = RadiozaurApp(root)
    root.iconbitmap("radiozaur2.ico")  # plik .ico
    root.mainloop()


“Added bilingual interface and language switch”
