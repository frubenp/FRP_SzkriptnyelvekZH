import tkinter as tk
import random
import time
from datetime import datetime
from frp_utils import frp_calc_wpm, FRPStats

texts = [
    "A programozás türelemjáték.",
    "A Python egyszerű és hatékony nyelv.",
    "Gyors gépeléssel időt spórolsz meg.",
    "Megszentségteleníthetetlenségeskedéseitekért.",
    "Ez egy magyar példamondat a teszthez."
]

stats = FRPStats()
start_time = None
original_text = ""
filename = "frp_eredmenyek.txt"

def update_stats_labels():
    last = stats.last()
    avg = round(sum(stats.results) / len(stats.results), 2) if stats.results else 0.0
    lbl_last.config(text=f"Utolsó: {last if last is not None else '-'}")
    lbl_avg.config(text=f"Átlag WPM: {avg}")

def reset_after_finish():
    entry.delete("1.0", tk.END)
    entry.config(state="disabled")
    btn_start.config(state="normal")
    btn_finish.config(state="normal")

def start():
    global original_text, start_time
    original_text = random.choice(texts)
    lbl_text.config(text=original_text)
    entry.config(state="disabled")
    entry.delete("1.0", tk.END)
    start_time = None
    countdown(3)

def real_start():
    global start_time
    entry.config(state="normal")
    entry.focus_set()
    start_time = time.time()

def finish():
    global start_time
    if not start_time:
        return
    entered = entry.get("1.0", tk.END).strip()
    if entered != original_text:
        lbl_result.config(text="HIBA: nem egyezik a szöveg!")
        reset_after_finish()
        return
    end = time.time()
    diff = end - start_time
    wpm = frp_calc_wpm(len(entered), diff)
    stats.add(wpm)
    lbl_result.config(text=f"WPM: {wpm}")
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"{datetime.now().strftime('%Y-%m-%d %H:%M:%S')} ; {wpm}\n")
    update_stats_labels()
    start_time = None
    reset_after_finish()

def countdown(n):
    if n == 0:
        lbl_text.config(text=original_text)
        real_start()
    else:
        lbl_text.config(text=f"Kezdés {n}...")
        root.after(1000, lambda: countdown(n-1))

root = tk.Tk()
root.title("FRP Typing WPM")

lbl_text = tk.Label(root, text="Nyomd meg a START gombot!", font=("Arial", 14))
lbl_text.pack(pady=10)

entry = tk.Text(root, height=5, width=60, state="disabled")
entry.pack(pady=10)

btn_start = tk.Button(root, text="START", command=start, width=20)
btn_start.pack(pady=5)

btn_finish = tk.Button(root, text="FINISH", command=finish, width=20)
btn_finish.pack(pady=5)

lbl_result = tk.Label(root, text="", font=("Arial", 14))
lbl_result.pack(pady=10)

frame_stats = tk.Frame(root)
frame_stats.pack(pady=10, fill="x")
lbl_last = tk.Label(frame_stats, text="Utolsó: -", font=("Arial", 12))
lbl_last.pack(side="left", padx=10)
lbl_avg = tk.Label(frame_stats, text="Átlag WPM: 0.0", font=("Arial", 12))
lbl_avg.pack(side="left", padx=10)

root.bind("<Return>", lambda e: finish())

root.mainloop()
