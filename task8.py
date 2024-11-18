from tkinter import *

def calculate_area():

    length = float(entry_length.get())
    width = float(entry_width.get())


    area = length * width

    result_text.delete(1.0, END)  # Очищення текстового поля
    result_text.insert(END, f"Площа прямокутника: {area}")

root = Tk()
root.title("Обчислення площі прямокутника")

label_length = Label(root, text="Довжина:")
entry_length = Entry(root)
label_width = Label(root, text="Ширина:")
entry_width = Entry(root)
button_calculate = Button(root, text="Обчислити", command=calculate_area)
result_text = Text(root, height=2)

label_length.pack()
entry_length.pack()
label_width.pack()
entry_width.pack()
button_calculate.pack()
result_text.pack()

root.mainloop()