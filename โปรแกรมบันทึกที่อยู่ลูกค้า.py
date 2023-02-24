from tkinter import *
from tkinter import ttk
from tkinter import messagebox

###############CSV################

import csv

def writecsv(datalist):
    with open('data.csv','a',encoding='utf-8',newline='') as file:
        fw = csv.writer(file)   #fw = file writer
        fw.writerow(datalist)   #datalist = ['pen','pencil','eraser']

def readcsv():
    with open('data.csv',encoding='utf-8',newline='')as file:
        fr = csv.reader(file)  #fr = file reader
        data = list(fr)
    return data




GUI = Tk()
GUI.title ('โปรแกรมบันทึกข้อมูลที่อยู่ลูกค้า')
GUI.geometry('600x600')


L1 = Label(GUI,text='ข้อมูลที่อยู่ลูกค้า',font=('angsana New',32),fg='blue')
L1.place(x=190,y=30)


L2 = Label(GUI,text='คำนำหน้า',font=('angsana New',20),fg='blue')
L2.place(x=60,y=100)
combo1 = ttk.Combobox(value=["บริษัท","โรงเรียน","โรงสี"])
combo1.place(x=170,y=105)


L2 = Label(GUI,text='ชื่อ',font=('angsana New',20),fg='blue')
L2.place(x=60,y=150)

v_data2 = StringVar()  #ตัวแปรพิเศษใช้กันฃ้อความใน GUI
E2 = ttk.Entry(textvariable=v_data2,font=('Angsana New',18)) 
E2.place(x=170,y=150)



L3 = Label(GUI,text='ที่อยู่',font=('angsana New',20),fg='blue')
L3.place(x=60,y=200)
v_data3 = StringVar()  #ตัวแปรพิเศษใช้กันฃ้อความใน GUI
E3 = ttk.Entry(textvariable=v_data3,font=('Angsana New',18)) 
E3.place(x=170,y=200)


L4 = Label(GUI,text='เลขประจำตัวผู้เสียภาษี',font=('angsana New',20),fg='blue')
L4.place(x=60,y=250)
v_data4 = StringVar()  #ตัวแปรพิเศษใช้กันฃ้อความใน GUI
E4 = ttk.Entry(textvariable=v_data4,font=('Angsana New',18)) 
E4.place(x=250,y=250)

#######ปุ่มบันทึก#########

def Savedata():
    data = v_data.get  #ดึงข้อมูลจากตัวแปร v_data มาใช้งาน
    text = [data]
    writecsv(text)  #บันทึกลง csv
    v_data.set('')  #เคลียร์ข้อมูลที่อยู่ในช่องกรอก

def Button() :
    text = 'บันทึกสำเร็จ'
    messagebox.showinfo('บันทึก',text)

B1 = ttk.Button(text='บันทึก', command=Button)
B1.place(x=250,y=320)

GUI.mainloop()
