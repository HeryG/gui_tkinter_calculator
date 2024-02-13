import tkinter as tk

symbols = ["0","1","2","3","4","5","6","7","8","9","-","+","*","/","x^2","%","(",")",",","C","\u21BA","\u221A"]

def WindowInit():
    root = tk.Tk()
    root.configure(bg="#c2cbcf")
    root.geometry("405x300")
    root.title("GUI Calculator")
    return root

def ScreenInit(root):
    screen = [tk.Label(root, width=54, bg="#dadec5", anchor="w", borderwidth=2) for i in range(2)]
    for i in range(len(screen)):
        screen[i].grid(row=i, columnspan=6, ipadx=7.5, ipady=15, padx=2, pady=2)
    return screen

def DataInit(root, screen):
    data_entry = tk.Entry(root, borderwidth=4)
    data_entry.grid(row=len(screen)+1, columnspan=6, ipadx=135, ipady=7)

    return data_entry

def buttonClick(datas, symbol):
    def function():
        if symbol == "\u21BA":
            bufor = datas.get()[:-1]
            datas.delete(0, tk.END)
            datas.insert(0, bufor)

        elif symbol == "C":
            datas.delete(0, tk.END)

        else:
            tekst = symbol if symbol != "x^2" else "^2"
            datas.insert(tk.END, tekst)
    return function


def calculate(datas, screen):
    def is_correct(tekst):
        i = 1
        while tekst[i - 1] == ")":
            i += 1
        return tekst[-i].isdigit()
    
    def are_multiple_operators(tekst):

        for i in range(len(tekst)):
            if tekst[i].isdigit() and not tekst[i+1].isdigit():
                return
        return False
    
    def change_the_power_sign(tekst):
        for i in range(len(tekst)):
            if tekst[i] == '^':
                tekst = tekst[:i] + '**' + tekst[i+1:]
        return tekst
    
    def function():
        tekst = datas.get()

        for i in range(1, len(screen)):
            if not is_correct(tekst) or are_multiple_operators(tekst):
                continue
            elif screen[i]["text"]:
                screen[i - 1]["text"] = screen[i]["text"]
        screen[-1]["text"] = tekst + " = " + str(eval(tekst))

        if '^' in tekst:
            term = change_the_power_sign(tekst)
            screen[-1]['text'] = tekst + ' = ' + str(eval(term))
        else:
            screen[-1]['text'] = tekst + ' = ' + str(eval(tekst))
    return function


def ButtonInit(root, screen):
    buttons = [tk.Button(root, text=symbol, bg="#f2f4f7", borderwidth=3) for symbol in symbols]

    j = len(screen) + 2
    for i in range(len(buttons)):
        if i % 6 == 0:
            j += 1
        margin = 21 if len(symbols[i]) == 1 else 10
        buttons[i].grid(row=j, column=i % 6, ipadx=margin, ipady=4.3,columnspan=1)
        buttons[i].configure(command=buttonClick(datas, buttons[i]["text"]))

    equality_button = tk.Button(root,text="=",bg="#19c0fc",borderwidth=3,command=calculate(datas, screen))
    equality_button.grid(row=len(screen) + 6, column=4, columnspan=2, ipady=5, ipadx=53)
    return buttons

if __name__ == "__main__":
    root = WindowInit()
    screen = ScreenInit(root)
    datas = DataInit(root, screen)
    buttons = ButtonInit(root, screen)
    root.mainloop()
