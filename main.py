
import tkinter as tk

def calculate_x():
    a = int(entry_a.get())
    b = int(entry_b.get())
    c = int(entry_c.get())
    x = 43 * a + 65 * b - 2 * c + 4
    label_result.config(text="X = {}".format(x))

# создаем окно
window = tk.Tk()
window.title("Калькулятор X")

# создаем элементы интерфейса
label_a = tk.Label(window, text="a:")
label_a.grid(row=0, column=0)

entry_a = tk.Entry(window)
entry_a.grid(row=0, column=1)

label_b = tk.Label(window, text="b:")
label_b.grid(row=1, column=0)

entry_b = tk.Entry(window)
entry_b.grid(row=1, column=1)

label_c = tk.Label(window, text="c:")
label_c.grid(row=2, column=0)

entry_c = tk.Entry(window)
entry_c.grid(row=2, column=1)

button_calculate = tk.Button(window, text="Вычислить X", command=calculate_x)
button_calculate.grid(row=3, column=0, columnspan=2)

label_result = tk.Label(window, text="")
label_result.grid(row=4, column=0, columnspan=2)

# запускаем цикл обработки событий
window.mainloop()





