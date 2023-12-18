from tkinter import *

def clear_all():
    principle_field.delete(0,END)
    rate_field.delete(0,END)
    time_field.delete(0,END)
    compound_field.delete(0,END)
    Totalamount_field.delete(0,END)
    principle_field.focus_set()

def calculate_ci():
    principle=int(principle_field.get())
    rate=int(rate_field.get())
    time=int(time_field.get())

    Amount=principle*(pow((1+rate/100),time))
    CI=Amount-principle
    compound_field.insert(10,CI)
    Totalamount_field.insert(5,Amount)

if __name__=="__main__":
    root=Tk()
    root.configure(background="grey27")
    root.geometry("400x380")
    root.title("Compound Interest Calculator")
    label1=Label(root,text="Principal Amount (Rs):",fg='black',bg='light green',font=('bold'))
    label2=Label(root,text="Rate (%):",fg='Black',bg='light green',font=('bold'))
    label3=Label(root,text="Time (Years):",fg='Black',bg='light green',font=('bold'))
    label4=Label(root,text="Compound Interest:",fg='Black',bg='light green',font=('bold'))
    label5=Label(root,text="Total Amount:",fg='Black',bg='light green',font=('bold'))

    label1.grid(row=1,column=0,padx=10,pady=10)
    label2.grid(row=2,column=0,padx=10,pady=10)
    label3.grid(row=3,column=0,padx=10,pady=10)
    label4.grid(row=5,column=0,padx=10,pady=10)
    label5.grid(row=6,column=0,padx=10,pady=10)

    principle_field=Entry(root)
    rate_field=Entry(root)
    time_field=Entry(root)
    compound_field=Entry(root)
    Totalamount_field=Entry(root)

    principle_field.grid(row=1,column=1,padx=10,pady=10)
    rate_field.grid(row=2,column=1,padx=10,pady=10)
    time_field.grid(row=3,column=1,padx=10,pady=10)
    compound_field.grid(row=5,column=1,padx=10,pady=10)
    Totalamount_field.grid(row=6,column=1,padx=10,pady=10)

    button1=Button(root,text="Calculate",fg='black',bg='darkolivegreen',font=('bold'),command=calculate_ci)
    button2=Button(root,text="Clear All",fg='black',bg='darkolivegreen',font=('bold'),command=clear_all)

    button1.grid(row=4,column=1,pady=10)
    button2.grid(row=7,column=1,pady=10)
    root.mainloop()