from tkinter import *
import tkinter.messagebox
import FBackend
import tempfile
import os


# FBackend = Database('store.FBackend')


def populate_list():
    item_list.delete(0, END)
    for row in FBackend.view():
        item_list.insert(END, row)


def add_item():
    if item_text.get() == '' or Price_text.get() == '' or Quantity_text.get() == '' or tax_text.get() == '':
        tkinter.messagebox.showerror(
            'Required Fields', 'Please include all fields')
        return
    FBackend.Insert(item_text.get(), Quantity_text.get(),
                    tax_text.get(), Price_text.get())
    item_list.delete(0, END)
    item_list.insert(END, (item_text.get(), Price_text.get(),
                           Quantity_text.get(), tax_text.get()))
    clear_text()
    populate_list()


def view():
    for row in FBackend.view():
        item_list.insert(END, row)


def Search():
    s = FBackend.Search(item_entry.get(), Quantity_entry.get(),
                        tax_text.get(), Price_entry.get())
    for i in s:
        item_list.insert(END, i)


def Print():
    Print1 = tkinter.messagebox.askyesno("Shopping Mart",
                                         "About to print your cart items\t\t\nConfirm if you want to print")
    if Print1 > 0:
        q = str(item_list.get(0, END))
        filename = tempfile.mktemp(".txt")
        open(filename, 'w').write(q)
        os.startfile(filename, 'print')
        return


def Iexit():
    iExit = tkinter.messagebox.askyesno(
        "Shopping Mart", "Confirm if you want to exit")
    if iExit > 0:
        app.destroy()
        return


# Create window object
app = Tk()
# Frames
MainFrame = Frame(app)
MainFrame.pack()
Tops = Frame(MainFrame, bd=10, relief=RIDGE)
Tops.pack(side=TOP)
Titframe = LabelFrame(MainFrame)
Titframe.pack(side=TOP)
topframe = LabelFrame(MainFrame, font=('times', 12, 'bold'),
                      bd=5, text="Entries", relief=RIDGE)
topframe.pack(side=TOP, padx=10)
RightLabel = LabelFrame(MainFrame, text="Controls", font=(
    'times', 12, 'bold'), bd=5, relief=RIDGE)
RightLabel.pack(side=TOP)

Display1 = LabelFrame(MainFrame, bd=5, width=100, font=(
    'times', 12, 'bold'), text="Receipt", relief=RIDGE)
Display1.pack(side=TOP)

lbltitle = Label(Titframe, width=30, font=('times', 39, 'bold'),
                 text="Mart V1", justify=CENTER)
lbltitle.grid(padx=140)
# item
item_text = StringVar()
item_label = Label(topframe, text='Item:', font=('Times', 14, 'bold'))
item_label.grid(row=0, column=0, sticky=W, pady=20)
item_entry = Entry(topframe, textvariable=item_text)
item_entry.grid(row=0, column=1)
# Price
Price_text = StringVar()
Price_label = Label(topframe, text='Price:', font=('Times', 14, 'bold'))
Price_label.grid(row=0, column=2, sticky=W, padx=20)
Price_entry = Entry(topframe, textvariable=Price_text)
Price_entry.grid(row=0, column=3)
# Quantity
Quantity_text = IntVar()
Quantity_label = Label(topframe, text='Quantity:', font=('Times', 14, 'bold'))
Quantity_label.grid(row=1, column=0, sticky=W, pady=20)
Quantity_entry = Entry(topframe, textvariable=Quantity_text)
Quantity_entry.grid(row=1, column=1)
# tax
tax_text = StringVar()
tax_label = Label(topframe, text='Tax:', font=('Times', 14, 'bold'))
tax_label.grid(row=1, column=2, sticky=W, padx=20)
tax_entry = Entry(topframe, textvariable=tax_text)
tax_entry.grid(row=1, column=3)
# item List (Listbox)
item_list = Listbox(Display1, height=15, width=80, border=0)
item_list.grid(row=3, column=0, columnspan=3, rowspan=6, pady=20, padx=20)
# Create scrollbar
scrollbar = Scrollbar(Display1)
scrollbar.grid(row=3, column=3)
# Set scroll to listbox
item_list.configure(yscrollcommand=scrollbar.set)
scrollbar.configure(command=item_list.yview)
# Bind select
#item_list.bind('<<ListboxSelect>>', select_item)

# Buttons
add_btn = Button(RightLabel, text='Add', width=12, command=add_item)
add_btn.grid(row=2, column=0, pady=20)

view_btn = Button(RightLabel, text='View', width=12, command=view)
view_btn.grid(row=2, column=1)

search_btn = Button(RightLabel, text='Search', width=12, command=Search)
search_btn.grid(row=2, column=3)

print_btn = Button(RightLabel, text='Print', width=12, command=Print)
print_btn.grid(row=2, column=4)

close_btn = Button(RightLabel, text='CLOSE', width=12, command=Iexit)
close_btn.grid(row=2, column=5)

app.title('item Manager')
app.geometry('700x350')

# Populate data
populate_list()

# Start program
app.mainloop()
