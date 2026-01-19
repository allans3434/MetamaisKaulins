import tkinter as tk
import random

root = tk.Tk()
root.title("Metamais Kauliņš")
root.resizeble(False, False)

chosen_number = tk.IntVar()
success_count = 0

dice_images = [
  tk.PhotoImage(file="dice/dice1.png"),
  tk.PhotoImage(file="dice/dice2.png"),
  tk.PhotoImage(file="dice/dice3.png"),
  tk.PhotoImage(file="dice/dice4.png"),
  tk.PhotoImage(file="dice/dice5.png"),
  tk.PhotoImage(file="dice/dice6.png")
]

def roll_dice():
  global success_count

roll = random.randint(1, 6)
dice_label.config(image=dice_images[roll - 1])

if roll == chosen_number.get():
  success_count += 1
  status_label.config(
    text=f"Veiksmīgi metieni pēc kārtas: {success_count}"
  )
else:
  success_count = 0
  status_label.config(text="Tu uzvarēji!")

tk.Label(root, text="Izvēlies ciparu (1-6):").pack(pady=5)

number_menu = tk.OptionMenu(
  root,
  chosen_number,
  1, 2, 3, 4, 5, 6
)
chosen_number.set(1)
number_menu.pack()

dice_label = tk.Label(root, image=dice_images[0])
dice_label.pack(pady=10)

roll_button = tk.Button(
  root,
  text="Mest Kauliņu",
  command=roll_dice
)
roll_button.pack(pady=5)

status_label = tk.Label(root, text="Spēle sākta")
status_label.pack(pady=10)

root.mainloop()






