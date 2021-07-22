import sys
import mysql.connector
import tkinter
from tkinter import messagebox
from tkinter import IntVar

try:
    import Tkinter as tk
except ImportError:
    import tkinter as tk

try:
    import ttk
    py3=False
except ImportError:
    import tkinter.ttk as ttk
    py3=True

import prostudent_support

def vp_start_gui():
    
    global val, w, root
    root=tk.Tk()
    prostudent_support.set_Tk_var()
    top=studentdata (root)
    prostudent_support.init(root, top)
    root.mainloop()

w=None
def create_studentdata(rt,*args,**kwargs):
    
    global w, w_win, root
    root=rt
    w=tk.Toplevel (root)
    prostudent_support.set_Tk_var()
    top=studentdata (w)
    prostudent_support.init(w, top, *args, **kwargs)
    return (w, top)

def destroy_studentdata():
    global w
    w.destroy()
    w=None

class studentdata:
    def modify_student(self):
        cursor=self.con.cursor()
        name=self.txtname.get('1.0','end-1c')
        regno=self.txtreg.get('1.0','end-1c')
        cgpa=self.txtcgpa.get('1.0','end-1c')
        batch=self.batch
        year=self.txtage.get()
        if(float(cgpa)>10):
        	messagebox.showerror('Error','CGPA cannot be greater than 10')
        	return
        if(int(year)>4):
        	messagebox.showerror('Error','Year cannot be greater than 4')
        	return
        query1="update studentinfo set name=\""+name+"\" where regno=\""+regno+"\";"
        query2="update studentinfo set cgpa=\""+cgpa+"\" where regno=\""+regno+"\";"
        query3="update studentinfo set batch=\""+batch+"\" where regno=\""+regno+"\";"
        query4="update studentinfo set year="+year+" where regno=\""+regno+"\";"
        cursor.execute(query1)
        cursor.execute(query2)
        cursor.execute(query3)
        cursor.execute(query4)
        self.con.commit()
        messagebox.showinfo('updation','record updated successfully')

    def delete_student(self):
        cursor=self.con.cursor()
        roll=self.txtreg.get('1.0','end-1c')
        query="delete from studentinfo where regno=\""+roll+"\";"
        cursor.execute(query)
        self.con.commit()
        messagebox.showinfo('deletion','student record was removed successfully')

    def moselected(self):
        self.batch="MO"

    def mnselected(self):
        self.batch="MN"
        
    def add_student(self):
        try:
            name=self.txtname.get('1.0','end-1c')
            regno=self.txtreg.get('1.0','end-1c')
            cgpa=self.txtcgpa.get('1.0','end-1c')
            batch=self.batch
            year=self.txtage.get()
            cursor=self.con.cursor()
            print(year)
            if(float(cgpa)>10):
                messagebox.showerror('error','CGPA cannot be greater than 10')
                return
            query="insert into studentinfo (name,regno,cgpa,batch,year) values(%s,%s,%s,%s,%s);"
            if(int(year)>4):
            	messagebox.showerror('error','Year cannot be greater than 4')
            	return
            
            val=(name,regno,cgpa,batch,year)
            cursor.execute(query,val)
            self.con.commit()
            messagebox.showinfo('insertion','record inserted successfully')
        except Exception:
            messagebox.showerror('error','Cannot insert data')


    def show_details(self):
        try:
            cursor=self.con.cursor()
            cursor.execute("select * from studentinfo;")
            c=0
            self.liststudent.delete(0,tk.END)
            for i in cursor:
                self.liststudent.insert(c,i)
                c=c+1

                
        except Exception:
            messagebox.showerror('error','do table exist')

  

    def __init__ (self,top=None):
        try:
            self.con=mysql.connector.connect(host="localhost",user="root",password="",database="student")
            self.display()
        except Exception:
            messagebox.showerror('error','cannot connect')
	

        _bgcolor='#d9d9d9'  # X11 color: 'gray85'
        _fgcolor='#000000'  # X11 color: 'black'
        _compcolor='#d9d9d9' # X11 color: 'gray85'
        _ana1color='#d9d9d9' # X11 color: 'gray85'
        _ana2color='#ececec' # Closest X11 color: 'gray92'
        font9="-family {Stencil} -size 18 -weight bold"

        top.geometry("600x646+606+107")
        top.minsize(116, 1)
        top.maxsize(1604, 862)
        top.resizable(1, 1)
        top.title("student database")
        top.configure(borderwidth="3")
        top.configure(background="#d9d9d9")
        top.configure(height="2")
        top.configure(highlightcolor="#000000")
        self.var=IntVar()

        self.Frame1=tk.Frame(top)
        self.Frame1.place(relx=0.083, rely=0.093, relheight=0.395
                , relwidth=0.825)
        self.Frame1.configure(relief='groove')
        self.Frame1.configure(borderwidth="2")
        self.Frame1.configure(relief="groove")
        self.Frame1.configure(background="#d9d9d9")

        self.Label1 = tk.Label(self.Frame1)
        self.Label1.place(relx=0.123, rely=0.118, height=21, width=54)
        self.Label1.configure(background="#d9d9d9")
        self.Label1.configure(disabledforeground="#a3a3a3")
        self.Label1.configure(foreground="#3c17e8")
        self.Label1.configure(highlightcolor="#000000")
        self.Label1.configure(text='''Name''')

        self.Label2 = tk.Label(self.Frame1)
        self.Label2.place(relx=0.123, rely=0.275, height=21, width=54)
        self.Label2.configure(background="#d9d9d9")
        self.Label2.configure(disabledforeground="#a3a3a3")
        self.Label2.configure(foreground="#3c17e8")
        self.Label2.configure(text='''Reg.no''')

        self.Label3=tk.Label(self.Frame1)
        self.Label3.place(relx=0.147, rely=0.431, height=21, width=42)
        self.Label3.configure(background="#d9d9d9")
        self.Label3.configure(disabledforeground="#a3a3a3")
        self.Label3.configure(foreground="#3c17e8")
        self.Label3.configure(text='''CGPA''')

        self.Label4=tk.Label(self.Frame1)
        self.Label4.place(relx=0.147, rely=0.588, height=21, width=42)
        self.Label4.configure(background="#d9d9d9")
        self.Label4.configure(disabledforeground="#a3a3a3")
        self.Label4.configure(foreground="#3c17e8")
        self.Label4.configure(text='''Batch''')

        self.Label5=tk.Label(self.Frame1)
        self.Label5.place(relx=0.147, rely=0.745, height=21, width=42)
        self.Label5.configure(background="#d9d9d9")
        self.Label5.configure(disabledforeground="#a3a3a3")
        self.Label5.configure(foreground="#3c17e8")
        self.Label5.configure(highlightcolor="#000000")
        self.Label5.configure(text='''Year''')

        self.txtname=tk.Text(self.Frame1)
        self.txtname.place(relx=0.345, rely=0.118, relheight=0.094
                , relwidth=0.602)
        self.txtname.configure(background="white")
        self.txtname.configure(font="TkTextFont")
        self.txtname.configure(foreground="black")
        self.txtname.configure(highlightbackground="#d9d9d9")
        self.txtname.configure(highlightcolor="black")
        self.txtname.configure(insertbackground="black")
        self.txtname.configure(selectbackground="#c4c4c4")
        self.txtname.configure(selectforeground="black")
        self.txtname.configure(wrap="word")

        self.txtreg=tk.Text(self.Frame1)
        self.txtreg.place(relx=0.345, rely=0.275, relheight=0.094
                , relwidth=0.602)
        self.txtreg.configure(background="white")
        self.txtreg.configure(font="TkTextFont")
        self.txtreg.configure(foreground="black")
        self.txtreg.configure(highlightbackground="#d9d9d9")
        self.txtreg.configure(highlightcolor="black")
        self.txtreg.configure(insertbackground="black")
        self.txtreg.configure(selectbackground="#c4c4c4")
        self.txtreg.configure(selectforeground="black")
        self.txtreg.configure(wrap="word")

        self.txtcgpa=tk.Text(self.Frame1)
        self.txtcgpa.place(relx=0.345, rely=0.431, relheight=0.094
                , relwidth=0.602)
        self.txtcgpa.configure(background="white")
        self.txtcgpa.configure(font="TkTextFont")
        self.txtcgpa.configure(foreground="black")
        self.txtcgpa.configure(highlightbackground="#d9d9d9")
        self.txtcgpa.configure(highlightcolor="black")
        self.txtcgpa.configure(insertbackground="black")
        self.txtcgpa.configure(selectbackground="#c4c4c4")
        self.txtcgpa.configure(selectforeground="black")
        self.txtcgpa.configure(wrap="word")

        self.rdmo=tk.Radiobutton(self.Frame1)
        self.rdmo.place(relx=0.345, rely=0.588, relheight=0.098, relwidth=0.097)
        self.rdmo.configure(activebackground="#ececec")
        self.rdmo.configure(activeforeground="#000000")
        self.rdmo.configure(background="#d9d9d9")
        self.rdmo.configure(disabledforeground="#a3a3a3")
        self.rdmo.configure(foreground="#000000")
        self.rdmo.configure(highlightbackground="#d9d9d9")
        self.rdmo.configure(highlightcolor="black")
        self.rdmo.configure(justify='left')
        self.rdmo.configure(text='''MO''')
        self.rdmo.configure(variable=prostudent_support.selectedButton)
        self.rdmo.configure(variable=self.var,value=1,command=self.moselected)

        self.rdmn=tk.Radiobutton(self.Frame1)
        self.rdmn.place(relx=0.642, rely=0.588, relheight=0.098, relwidth=0.097)
        self.rdmn.configure(activebackground="#ececec")
        self.rdmn.configure(activeforeground="#000000")
        self.rdmn.configure(background="#d9d9d9")
        self.rdmn.configure(disabledforeground="#a3a3a3")
        self.rdmn.configure(foreground="#000000")
        self.rdmn.configure(highlightbackground="#d9d9d9")
        self.rdmn.configure(highlightcolor="black")
        self.rdmn.configure(justify='left')
        self.rdmn.configure(text='''MN''')
        self.rdmn.configure(variable=prostudent_support.selectedButton)
        self.rdmn.configure(variable=self.var,value=2,command=self.mnselected)


        self.txtage=tk.Spinbox(self.Frame1, from_=1.0, to=100.0)
        self.txtage.place(relx=0.37, rely=0.745, relheight=0.075, relwidth=0.21)
        self.txtage.configure(activebackground="#f9f9f9")
        self.txtage.configure(background="white")
        self.txtage.configure(buttonbackground="#d9d9d9")
        self.txtage.configure(disabledforeground="#a3a3a3")
        self.txtage.configure(font="TkDefaultFont")
        self.txtage.configure(foreground="black")
        self.txtage.configure(highlightbackground="black")
        self.txtage.configure(highlightcolor="black")
        self.txtage.configure(insertbackground="black")
        self.txtage.configure(selectbackground="#c4c4c4")
        self.txtage.configure(selectforeground="black")
        self.txtage.configure(textvariable=prostudent_support.spinbox)

        self.Label6=tk.Label(top)
        self.Label6.place(relx=0.0, rely=0.015, height=40, width=594)
        self.Label6.configure(background="#d9d9d9")
        self.Label6.configure(borderwidth="4")
        self.Label6.configure(disabledforeground="#a3a3a3")
        self.Label6.configure(font=font9)
        self.Label6.configure(foreground="#000000")
        self.Label6.configure(text='''Department of Computer Technology''')

        self.menubar=tk.Menu(top,font="TkMenuFont",bg=_bgcolor,fg=_fgcolor)
        top.configure(menu=self.menubar)

        self.btnshow=tk.Button(top)
        self.btnshow.place(relx=0.1, rely=0.542, height=24, width=39)
        self.btnshow.configure(activebackground="#ececec")
        self.btnshow.configure(activeforeground="#000000")
        self.btnshow.configure(background="#d9d9d9")
        self.btnshow.configure(disabledforeground="#a3a3a3")
        self.btnshow.configure(foreground="#3c17e8")
        self.btnshow.configure(highlightbackground="#d9d9d9")
        self.btnshow.configure(highlightcolor="#000000")
        self.btnshow.configure(pady="0")
        self.btnshow.configure(command=self.show_details,text='''show''')

        self.btnadd=tk.Button(top)
        self.btnadd.place(relx=0.833, rely=0.542, height=24, width=43)
        self.btnadd.configure(activebackground="#ececec")
        self.btnadd.configure(activeforeground="#000000")
        self.btnadd.configure(background="#d9d9d9")
        self.btnadd.configure(disabledforeground="#a3a3a3")
        self.btnadd.configure(foreground="#3c17e8")
        self.btnadd.configure(highlightbackground="#d9d9d9")
        self.btnadd.configure(highlightcolor="black")
        self.btnadd.configure(pady="0")
        self.btnadd.configure(command=self.add_student,text='''Add''')

        self.btnmodify=tk.Button(top)
        self.btnmodify.place(relx=0.833, rely=0.681, height=24, width=49)
        self.btnmodify.configure(activebackground="#ececec")
        self.btnmodify.configure(activeforeground="#000000")
        self.btnmodify.configure(background="#d9d9d9")
        self.btnmodify.configure(disabledforeground="#a3a3a3")
        self.btnmodify.configure(foreground="#3c17e8")
        self.btnmodify.configure(highlightbackground="#d9d9d9")
        self.btnmodify.configure(highlightcolor="black")
        self.btnmodify.configure(pady="0")
        self.btnmodify.configure(command=self.modify_student,text='''Modify''')

        self.btndelete=tk.Button(top)
        self.btndelete.place(relx=0.833, rely=0.851, height=24, width=47)
        self.btndelete.configure(activebackground="#ececec")
        self.btndelete.configure(activeforeground="#000000")
        self.btndelete.configure(background="#d9d9d9")
        self.btndelete.configure(disabledforeground="#a3a3a3")
        self.btndelete.configure(foreground="#3c17e8")
        self.btndelete.configure(highlightbackground="#d9d9d9")
        self.btndelete.configure(highlightcolor="black")
        self.btndelete.configure(pady="0")
        self.btndelete.configure(command=self.delete_student,text='''delete''')

        self.liststudent=tk.Listbox(top)
        self.liststudent.place(relx=0.208, rely=0.534, relheight=0.375
                , relwidth=0.575)
        self.liststudent.configure(background="white")
        self.liststudent.configure(disabledforeground="#a3a3a3")
        self.liststudent.configure(font="TkFixedFont")
        self.liststudent.configure(foreground="#000000")

if __name__ == '__main__':
    vp_start_gui()
