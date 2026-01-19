import tkinter as tk
import random
import os

root = tk.Tk()
root.title("Metamais kauliņš")
root.resizable(False, False)

chosen_number = tk.IntVar(value=1)
success_count = 0

BASE_DIR = os.path.dirname(__file__)

dice_images = [
    tk.PhotoImage(file=os.path.join(BASE_DIR, "dice", "dice1.png")),
    tk.PhotoImage(file=os.path.join(BASE_DIR, "dice", "dice2.png")),
    tk.PhotoImage(file=os.path.join(BASE_DIR, "dice", "dice3.png")),
    tk.PhotoImage(file=os.path.join(BASE_DIR, "dice", "dice4.png")),
    tk.PhotoImage(file=os.path.join(BASE_DIR, "dice", "dice5.png")),
    tk.PhotoImage(file=os.path.join(BASE_DIR, "dice", "dice6.png"))
]

def roll_dice():
    global success_count

    roll = random.randint(1, 6)
    dice_label.config(image=dice_images[roll - 1])

    if roll == chosen_number.get():
        success_count += 1
        status_label.config(text=f"Veiksmīgi metieni pēc kārtas: {success_count}")
    else:
        success_count = 0
        status_label.config(text="Nesakrita! Viss no jauna.")

    if success_count == 3:
        status_label.config(text="Tu uzvarēji!")

tk.Label(root, text="Izvēlies ciparu (1–6):").pack(pady=5)

tk.OptionMenu(root, chosen_number, 1, 2, 3, 4, 5, 6).pack()

dice_label = tk.Label(root, image=dice_images[0])
dice_label.pack(pady=10)

tk.Button(root, text="Mest kauliņu", command=roll_dice).pack(pady=5)

status_label = tk.Label(root, text="Spēle sākta")
status_label.pack(pady=10)

root.mainloop()
