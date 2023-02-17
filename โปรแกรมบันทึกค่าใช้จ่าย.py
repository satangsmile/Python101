from tkinter import *
from tkinter import ttk
from tkinter import messagebox


GUI = Tk()
GUI.title('โปรแกรมบันทึกค่าใช้จ่าย')
GUI.geometry('500x500')


L1 = Label(GUI,text='โปรแกรมบันทึกค่าใช้จ่ายประจำวัน',font=('angsana New',32),fg='blue')
L1.place(x=25,y=50)

#####################################


L2 = Label(GUI,text='วันที่',font=('angsana New',20),fg='black')
L2.place(x=60,y=130)
E2 = ttk.Entry()
E2.place(x=160,y=10)


L3 = Label(GUI,text='รายการ',font=('angsana New',20),fg='black')
L3.place(x=60,y=180)
E3 = ttk.Entry()
E3.place(x=160,y=180)

L4 = Label(GUI,text='จำนวนเงิน',font=('angsana New',20),fg='black')
L4.place(x=60,y=230)
L6 = Label(GUI,text='บาท',font=('angsana New',20),fg='black')
L6.place(x=360,y=230)
E4 = ttk.Entry()
E4.place(x=160,y=230)


L5 = Label(GUI,text='ประเภท',font=('angsana New',20),fg='black')
L5.place(x=60,y=280)
combo1 = ttk.Combobox(value=["ช้อปปิ้ง","อาหาร","ค่าเดินทาง","ของใช้ในบ้าน","อื่นๆ"])
combo1.place(x=160,y=280)

#####################################
def Button() :
    text = 'บันทึกสำเร็จ'
    messagebox.showinfo('บันทึก',text)
    
B1 = ttk.Button(text='บันทึก', command=Button)
B1.place(x=220,y=350)

