import tkinter as tk
window = tk.Tk()
window.title("Quadratic Equation")
window.geometry("400x600")
window.configure(bg="#2E3440")

def qe():
    try:
        a=float(a_entry.get())
        b=float(b_entry.get())
        c=float(c_entry.get())
        delta=b**2-4*a*c
        if delta<0:delta_label.config(text="Phương trình vô nghiệm")
        elif delta==0:
            x=-b/(2*a)
            delta_label.config(text=f"Phương trình có nghiệm kép x={x}")
        else:
            x1=(-b+delta**0.5)/(2*a)
            x2=(-b-delta**0.5)/(2*a)
            delta_label.config(text=f"Phương trình có 2 nghiệm x1={x1} và x2={x2}")
    except ValueError:
        delta_label.config(text="Vui lòng nhập vào các giá trị hợp lệ cho a, b và c")
tk.Label(window, text="Nhập a: ").grid(row=0,column=0,padx=7,pady=5)
a_entry = tk.Entry(window)
a_entry.grid(row=0,column=1,padx=7,pady=5)

tk.Label(window, text="Nhập b: ").grid(row=1,column=0,padx=7,pady=5)
b_entry = tk.Entry(window)
b_entry.grid(row=1,column=1,padx=7,pady=5)

tk.Label(window, text="Nhập c: ").grid(row=2,column=0,padx=7,pady=5)
c_entry = tk.Entry(window)
c_entry.grid(row=2,column=1,padx=7,pady=5)

button = tk.Button(window, text="Run", command=qe)
button.grid(row=3, column=0, columnspan=2, padx=5, pady=5)

delta_label = tk.Label(window, text="")
delta_label.grid(row=4, column=0, columnspan=2, padx=5, pady=5)

window.mainloop()