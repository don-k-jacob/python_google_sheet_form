import gspread
from tkinter import *



# print('rows: ',wks.row_count)
# print('rows: ',wks.col_count)

# print(wks.acell("B2").value)

# wks.delete_rows(3)

# 



from tkinter import *
class MyWindow:
   
    def __init__(self, win):
        self.mywin=win
        self.lbl1=Label(win, text='name')
        self.lbl2=Label(win, text='phone')
        self.lbl3=Label(win, text='status')
        self.name=Entry(bd=3)
        self.phone=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Subscribe')
        self.lbl1.place(x=100, y=50)
        self.name.place(x=200, y=50)
        self.lbl2.place(x=100, y=100)
        self.phone.place(x=200, y=100)
        self.b1=Button(win, text='Subscribe', command=self.upload)
        self.b2=Button(win, text='Home', command=self.home)
        
        self.b1.place(x=200, y=150)
        self.b2.place(x=200, y=250)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    def home(self):
        self.mywin.destroy()
        import home
    def upload(self):

        sa = gspread.service_account()

        sh = sa.open("PythonNewsLetter")

        wks= sh.worksheet("data")
    
        wks.append_row([
            # str(wks.row_count),
            self.name.get(),
            self.phone.get()
            ])
        self.t3.insert(END, 'uploaded')
    

window=Tk()
mywin=MyWindow(window)
window.title('ADD To Google Sheet')
window.geometry("400x300+10+10")
window.mainloop()
