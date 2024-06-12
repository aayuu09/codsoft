from tkinter import *
from tkinter import messagebox

def newTask():
    task = my_entry.get()
    if task != "":
        lb.insert(END, task)
        my_entry.delete(0, "end")
    else:
        messagebox.showwarning("warning!!","Invalid..")

def deleteTask():
    lb.delete(ANCHOR)
    
ws = Tk()
ws.geometry('500x450+500+200')
ws.title('To-Do List')
ws.config(bg='#091233')
ws.resizable(0,0)

frame = Frame(ws)
frame.pack(pady=10)

lb = Listbox(
    frame,
    width=25,
    height=8,
    font=('bookman old style', 18),
    bd=0,
    fg='#14161c',
    highlightthickness=0,
    selectbackground='#bec1cc',
    activestyle="none",
    
)
lb.pack(side=LEFT, fill=BOTH)
task_list = ['']
for item in task_list:
    lb.insert(END, item)
sb = Scrollbar(frame)
sb.pack(side=RIGHT, fill=BOTH)
lb.config(yscrollcommand=sb.set)
sb.config(command=lb.yview)
my_entry = Entry(ws, font=('bookman old style', 24))
my_entry.pack(pady=20)
button_frame = Frame(ws)
button_frame.pack(pady=20)

addTask_btn = Button(
    button_frame,
    text='Add Task',
    font=('bookman old style', '14'),
    bg='#c5f776',
    padx=20,
    pady=10,
    command=newTask
)
addTask_btn.pack(fill=BOTH, expand=True, side=LEFT)

delTask_btn = Button(
    button_frame,
    text='Delete Task',
    font=('bookman old style','14'),
    bg='#eb4f28',
    padx=20,
    pady=10,
    command=deleteTask
)
delTask_btn.pack(fill=BOTH, expand=True, side=LEFT)


ws.mainloop()