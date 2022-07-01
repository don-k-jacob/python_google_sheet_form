import gspread
from tkinter import *



# print('rows: ',wks.row_count)
# print('rows: ',wks.col_count)

# print(wks.acell("B2").value)

# 

# 



from tkinter import *
class MyWindow:
   
    def __init__(self, win):
       
        self.lbl2=Label(win, text='phone')
        self.lbl3=Label(win, text='status')
        self.name=Entry(bd=3)
        self.phone=Entry()
        self.t3=Entry()
        self.btn1 = Button(win, text='Unsubscribe')
        self.lbl2.place(x=100, y=100)
        self.phone.place(x=200, y=100)
        self.b1=Button(win, text='Unsubscribe', command=self.remove)
        
        self.b1.place(x=200, y=150)
        self.lbl3.place(x=100, y=200)
        self.t3.place(x=200, y=200)
    
    def remove(self):

        sa = gspread.service_account()

        sh = sa.open("PythonNewsLetter")

        wks= sh.worksheet("data")
        cell = wks.find(self.phone.get())
        wks.delete_rows(cell.row)
        self.t3.insert(END, 'removed')
    

window=Tk()
mywin=MyWindow(window)
window.title('Unsubscribe')
window.geometry("400x300+10+10")
window.mainloop()
