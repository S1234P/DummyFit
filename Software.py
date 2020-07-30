from tkinter import *



root = Tk()

root.title("DummyFit")

root.geometry('340x720')
root.resizable(0, 0)


lbl = Label(root, text="DummyFit", font=("Arial Bold", 50))
lbl.grid(column=0, row=0)



head1 =Label(root, text="Input ---", font=("Arial Bold", 10))
head1.grid(column=0, row=1)

txt1 = Entry(root,width=10,)
txt1.grid(column=0, row=2)


head2 =Label(root, text="Input ---", font=("Arial Bold", 10))
head2.grid(column=0, row=4)

txt2 = Entry(root,width=10,)
txt2.grid(column=0, row=5)


head3 =Label(root, text="Input ---", font=("Arial Bold", 10))
head3.grid(column=0, row=6)

txt3 = Entry(root,width=10,)
txt3.grid(column=0, row=7)


head4 =Label(root, text="Input ---", font=("Arial Bold", 10))
head4.grid(column=0, row=8)

txt4 = Entry(root,width=10,)
txt4.grid(column=0, row=9)


def clicked():

    rlt.configure(text="#Output from BMI Calc internal")

btn = Button(root, text="Enter", command=clicked)

btn.grid(column=0, row=11)


rlt = Label(root, text="Results", font=("Arial Bold", 10))
rlt.grid(column=0, row=12)



root.mainloop()
