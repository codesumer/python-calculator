import tkinter as tk

root = tk.Tk()

root.geometry("500x500")
root.title("Calculator")

label=tk.Label(root, text="Calculator", font=('Arial',20))
label.pack(padx= 20, pady=5)

display = tk.Entry(root, font=('Arial', 20))
display.pack(fill="x", padx=10, pady=10, ipady=10)

frame= tk.Frame(root)
frame.columnconfigure(0, weight=1)
frame.columnconfigure(1, weight=1)
frame.columnconfigure(2, weight=1)
frame.columnconfigure(3, weight=1)

frame.rowconfigure(0, weight=1)
frame.rowconfigure(1, weight=1)
frame.rowconfigure(2, weight=1)
frame.rowconfigure(3, weight=1)
frame.rowconfigure(4, weight=1)


def add(val):
    display.insert(tk.END, val)


def clear():
    display.delete(0, tk.END)


def backspace():
    current = display.get()
    if current:
        display.delete(len(current)-1,tk.END)


def calculate():
    try:
        result= eval(display.get())
        clear()
        add(str(result))
    except:
        clear()
        add("ERROR!")
#row 1
btn1=tk.Button(frame, text="+", font=('Arial',18), bg="#FFA500", fg="white", command=lambda: add("+"))
btn1.grid(row=0, column=0, sticky="nsew")

btn2=tk.Button(frame, text="-", font=('Arial',18), bg="#FFA500", fg="white", command=lambda: add("-"))
btn2.grid(row=0, column=1, sticky="nsew")

btn3=tk.Button(frame, text="*", font=('Arial',18), bg="#FFA500", fg="white", command=lambda: add("*"))
btn3.grid(row=0, column=2, sticky="nsew")

btn4=tk.Button(frame, text="/", font=('Arial',18), bg="#FFA500", fg="white",  command=lambda: add("/"))
btn4.grid(row=0, column=3, sticky="nsew")


#row 2

btn5=tk.Button(frame, text="1", font=('Arial',18), command=lambda: add("1"))
btn5.grid(row=1, column=0, sticky="nsew")

btn6=tk.Button(frame, text="2", font=('Arial',18), command=lambda: add("2"))
btn6.grid(row=1, column=1, sticky="nsew")

btn7=tk.Button(frame, text="3", font=('Arial',18), command=lambda: add("3"))
btn7.grid(row=1, column=2, sticky="nsew")

btn8=tk.Button(frame, text="⌫", font=('Arial',18),bg="#FF5555", fg="white", command= backspace)
btn8.grid(row=1, column=3, sticky="nsew")

#row 3

btn9=tk.Button(frame, text="4", font=('Arial',18), command=lambda: add("4"))
btn9.grid(row=2, column=0, sticky="nsew")

btn10=tk.Button(frame, text="5", font=('Arial',18), command=lambda: add("5"))
btn10.grid(row=2, column=1, sticky="nsew")

btn11=tk.Button(frame, text="6", font=('Arial',18), command=lambda: add("6"))
btn11.grid(row=2, column=2, sticky="nsew")

btn12=tk.Button(frame, text="C", font=('Arial',18), command=clear)
btn12.grid(row=2, column=3, sticky="nsew")

#row 4
btn13=tk.Button(frame, text="7", font=('Arial',18), command=lambda: add("7"))
btn13.grid(row=3, column=0, sticky="nsew")

btn14=tk.Button(frame, text="8", font=('Arial',18), command=lambda: add("8"))
btn14.grid(row=3, column=1, sticky="nsew")

btn15=tk.Button(frame, text="9", font=('Arial',18), command=lambda: add("9"))
btn15.grid(row=3, column=2, sticky="nsew")

btn16=tk.Button(frame, text="=", font=('Arial',18), bg="#00B7FF", fg="white", command=calculate)
btn16.grid(row=3, column=3, sticky="nsew")

#row 5
btn17=tk.Button(frame, text=" ", font=('Arial',18), command=lambda: add(" "))
btn17.grid(row=4, column=0, sticky="nsew")

btn18=tk.Button(frame, text="0", font=('Arial',18), command=lambda: add("0"))
btn18.grid(row=4, column=1, sticky="nsew")

btn19=tk.Button(frame, text="00", font=('Arial',18), command=lambda: add("00"))
btn19.grid(row=4, column=2, sticky="nsew")

btn20=tk.Button(frame, text=".", font=('Arial',18), command=lambda: add("."))
btn20.grid(row=4, column=3, sticky="nsew")




frame.pack(fill='both', expand=True)

root.mainloop()
