from tkinter import *

ws = Tk()
ws.geometry('400x300')
ws.title('PythonGuides')
ws['bg']='#ffbf00'

f = ("Times bold", 14)
 
def sendMail():
    ws.destroy()
    import texteditor

def subscribe():
    ws.destroy()
    import subscribe

def unsubscribe():
    ws.destroy()
    import unsubscribe

Label(
    ws,
    text="SEND ME",
    padx=20,
    pady=10,
    # bg='#ffbf00',
    font=f
).pack(expand=True, fill=BOTH)
Button(
    ws, 
    text="Send Mail", 
    font=f,
    padx=20,
    pady=20,
    command=sendMail
    ).pack(expand=True, fill=BOTH)
Button(
    ws, 
    text="Subscribe", 
    font=f,
    padx=20,
    pady=20,
    command=subscribe
    ).pack(expand=True, fill=BOTH)
Button(
    ws, 
    text="Un-subscribe", 
    padx=20,
    pady=40,

    justify= CENTER,
    font=f,
    command=unsubscribe
    ).pack(expand=True, fill=BOTH)

ws.mainloop()

