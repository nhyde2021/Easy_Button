import tkinter as tk
from random import randint



def generate_values():
    global chance
    global value

    chance = randint(1, 20)
    value = randint(1, 20)

    print(chance)
    print(value)

def add_point():
    global points
    global value
    global chance
    global bank
    global attempts

    points += 1
    press.config(text="\u2620  " + str(points) + "  \u2620")

    if chance == value:
        press.config(text="  Game Over | Total Score: "+ str(bank) + "  ", bg="red", disabledforeground="black", state="disabled")
        bank_points.config(text="XXXXXXX", bg="red", disabledforeground="black", state="disabled")
        attempts = 1

def high_score():
    global highScore

    if bank >= highScore:
        highScore = bank
        label.config(text="High Score: " + str(highScore))
        with open("EB_high_score.txt", "w") as file:
            file.write(str(highScore))

def start_over():
    global points
    global value
    global bank

    points = 0
    attempts = 1
    bank = 0
    press.config(text="Wango!!", bg="light gray", state="normal")
    bank_points.config(text="Bank Points", bg="light gray", state="normal")
    label2.config(text="Attempt # 1")
    label3.config(text="Bank: 0")

def attempts_count():
    global attempts

    attempts += 1
    label2.config(text="Attempt # " + str(attempts))
    if attempts > 3:
        press.config(text="Total Score: "+ str(bank), bg="green", disabledforeground="black", state="disabled")
        bank_points.config(text="XXXXXXX", bg="red", disabledforeground="black", state="disabled")
        label2.config(text="Attempt # \u2620")
        attempts = 1

def bank_value():
    global bank
    global points

    bank += points
    label3.config(text="Bank: " + str(bank))
    points = 0
    press.config(text="\u2620  " + str(points) + "  \u2620")
    attempts_count()

def open_new_window():
    new_window = tk.Toplevel(root)
    new_window.title("New Window")

    # Add widgets to the new window here
    label = tk.Label(new_window, text="This is a new window!")
    label.pack(pady=20)



root = tk.Tk()
root.title("Easy Button")
    
with open('EB_high_score.txt', 'r') as file:
    content = file.read()

points = 0
value = None
chance = None
highScore = int(content)
attempts = 1
bank = 0

press = tk.Button(root, text="Wango!!", width=22, bg="light gray", command=lambda:[generate_values(), add_point()])
press.pack()
press.place(x=120, y=100)

reset = tk.Button(root, text="Reset", width=10, bg="light gray", command=lambda:[start_over()])
reset.pack()
reset.place(x=300, y=20)

bank_points = tk.Button(root, text="Bank Points", width=10, bg="light gray", command=lambda:[bank_value(), high_score()])
bank_points.pack()
bank_points.place(x=300, y=60)

leaderboard = tk.Button(root, text="Open New Window", command=open_new_window)
leaderboard.pack(pady=20)

label = tk.Label(root, text="High Score: " + content)
label.pack()
label.place(x=10, y=20)

label2 = tk.Label(root, text="Attempt # 1")
label2.pack()
label2.place(x=10, y=40)

label3 = tk.Label(root, text="Bank: " + str(bank))
label3.pack()
label3.place(x=10, y=60)

root.geometry("400x200")
root.mainloop()


