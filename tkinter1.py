import tkinter as tk
import random
from tkinter.filedialog import askopenfilename, asksaveasfilename


def frame_test():
    window = tk.Tk()

    frame_a = tk.Frame()
    frame_b = tk.Frame()

    label_a = tk.Label(master=frame_a, text="I'm in Frame A")
    label_a.pack()

    label_b = tk.Label(master=frame_b, text="I'm in Frame B")
    label_b.pack()

    frame_a.pack()
    frame_b.pack()

    window.mainloop()


def frame_test2():
    border_effects = {
        "flat": tk.FLAT,
        "sunken": tk.SUNKEN,
        "raised": tk.RAISED,
        "groove": tk.GROOVE,
        "ridge": tk.RIDGE,
    }

    window = tk.Tk()

    for relief_name, relief in border_effects.items():
        frame = tk.Frame(master=window, relief=relief, borderwidth=5)
        frame.pack(side=tk.LEFT)
        label = tk.Label(master=frame, text=relief_name)
        label.pack()

    window.mainloop()


def window_test():
    window = tk.Tk()
    label = tk.Label(text="Name", fg="#F07616", bg="#185532", width=30, height=2)
    button = tk.Button(text="Start!", width=10, height=2, fg="#F07616", bg="#185532")
    entry = tk.Entry(fg="#F07616", bg="#185532", width=50)
    name = entry.get()
    label2 = tk.Label(text=name, fg="#F07616", bg="#185532", width=30, height=2)
    text_box = tk.Text()
    label.pack()
    entry.pack()
    button.pack()
    label2.pack()
    text_box.pack()
    window.mainloop()


def entry_test1():
    # Create a new window with the title "Address Entry Form"
    window = tk.Tk()
    window.title("Address Entry Form")

    # Create a new frame `frm_form` to contain the Label
    # and Entry widgets for entering address information.
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    # Pack the frame into the window
    frm_form.pack()

    # Create the Label and Entry widgets for "First Name"
    lbl_first_name = tk.Label(master=frm_form, text="First Name:")
    ent_first_name = tk.Entry(master=frm_form, width=50)
    # Use the grid geometry manager to place the Label and
    # Entry widgets in the first and second columns of the
    # first row of the grid
    lbl_first_name.grid(row=0, column=0, sticky="e")
    ent_first_name.grid(row=0, column=1)

    # Create the Label and Entry widgets for "Last Name"
    lbl_last_name = tk.Label(master=frm_form, text="Last Name:")
    ent_last_name = tk.Entry(master=frm_form, width=50)
    # Place the widgets in the second row of the grid
    lbl_last_name.grid(row=1, column=0, sticky="e")
    ent_last_name.grid(row=1, column=1)

    # Create the Label and Entry widgets for "Address Line 1"
    lbl_address1 = tk.Label(master=frm_form, text="Address Line 1:")
    ent_address1 = tk.Entry(master=frm_form, width=50)
    # Place the widgets in the third row of the grid
    lbl_address1.grid(row=2, column=0, sticky="e")
    ent_address1.grid(row=2, column=1)

    # Create the Label and Entry widgets for "Address Line 2"
    lbl_address2 = tk.Label(master=frm_form, text="Address Line 2:")
    ent_address2 = tk.Entry(master=frm_form, width=5)
    # Place the widgets in the fourth row of the grid
    lbl_address2.grid(row=3, column=0, sticky=tk.E)
    ent_address2.grid(row=3, column=1)

    # Create the Label and Entry widgets for "City"
    lbl_city = tk.Label(master=frm_form, text="City:")
    ent_city = tk.Entry(master=frm_form, width=50)
    # Place the widgets in the fifth row of the grid
    lbl_city.grid(row=4, column=0, sticky=tk.E)
    ent_city.grid(row=4, column=1)

    # Create the Label and Entry widgets for "State/Province"
    lbl_state = tk.Label(master=frm_form, text="State/Province:")
    ent_state = tk.Entry(master=frm_form, width=50)
    # Place the widgets in the sixth row of the grid
    lbl_state.grid(row=5, column=0, sticky=tk.E)
    ent_state.grid(row=5, column=1)

    # Create the Label and Entry widgets for "Postal Code"
    lbl_postal_code = tk.Label(master=frm_form, text="Postal Code:")
    ent_postal_code = tk.Entry(master=frm_form, width=50)
    # Place the widgets in the seventh row of the grid
    lbl_postal_code.grid(row=6, column=0, sticky=tk.E)
    ent_postal_code.grid(row=6, column=1)

    # Create the Label and Entry widgets for "Country"
    lbl_country = tk.Label(master=frm_form, text="Country:")
    ent_country = tk.Entry(master=frm_form, width=50)
    # Place the widgets in the eight row of the grid
    lbl_country.grid(row=7, column=0, sticky=tk.E)
    ent_country.grid(row=7, column=1)

    # Create a new frame `frm_buttons` to contain the
    # Submit and Clear buttons. This frame fills the
    # whole window in the horizontal direction and has
    # 5 pixels of horizontal and vertical padding.
    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # Create the "Submit" button and pack it to the
    # right side of `frm_buttons`
    btn_submit = tk.Button(master=frm_buttons, text="Submit")
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    # Create the "Clear" button and pack it to the
    # right side of `frm_buttons`
    btn_clear = tk.Button(master=frm_buttons, text="Clear")
    btn_clear.pack(side=tk.RIGHT, ipadx=10)

    # Start the application
    window.mainloop()


def entry_test2():
    # Create a new window with the title "Address Entry Form"
    window = tk.Tk()
    window.title("Address Entry Form")

    # Create a new frame `frm_form` to contain the Label
    # and Entry widgets for entering address information.
    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    # Pack the frame into the window
    frm_form.pack()

    # List of field labels
    labels = [
        "First Name:",
        "Last Name:",
        "Address Line 1:",
        "Address Line 2:",
        "City:",
        "State/Province:",
        "Postal Code:",
        "Country:",
    ]

    # Loop over the list of field labels
    for idx, text in enumerate(labels):
        # Create a Label widget with the text from the labels list
        label = tk.Label(master=frm_form, text=text)
        # Create an Entry widget
        entry = tk.Entry(master=frm_form, width=50)
        # Use the grid geometry manager to place the Label and
        # Entry widgets in the row whose index is idx
        label.grid(row=idx, column=0, sticky="e")
        entry.grid(row=idx, column=1)

    # Create a new frame `frm_buttons` to contain the
    # Submit and Clear buttons. This frame fills the
    # whole window in the horizontal direction and has
    # 5 pixels of horizontal and vertical padding.
    frm_buttons = tk.Frame()
    frm_buttons.pack(fill=tk.X, ipadx=5, ipady=5)

    # Create the "Submit" button and pack it to the
    # right side of `frm_buttons`
    btn_submit = tk.Button(master=frm_buttons, text="Submit")
    btn_submit.pack(side=tk.RIGHT, padx=10, ipadx=10)

    # Create the "Clear" button and pack it to the
    # right side of `frm_buttons`
    btn_clear = tk.Button(master=frm_buttons, text="Clear")
    btn_clear.pack(side=tk.RIGHT, ipadx=10)

    # Start the application
    window.mainloop()


def handler_test1():
    window = tk.Tk()

    def handle_keypress(event):
        """Print the character associated to the key pressed"""
        print(event.char)

    # Bind keypress event to handle_keypress()
    window.bind("<Key>", handle_keypress)

    def handle_click(event):
        print("The button was clicked!")

    button = tk.Button(text="Click me!")

    button.bind("<Button-1>", handle_click)
    button.pack(side=tk.RIGHT, ipadx=10)

    window.mainloop()


def handler_test2():
    def increase():
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value + 1}"

    def decrease():
        value = int(lbl_value["text"])
        lbl_value["text"] = f"{value - 1}"

    window = tk.Tk()

    window.rowconfigure(0, minsize=50, weight=1)
    window.columnconfigure([0, 1, 2], minsize=50, weight=1)

    btn_decrease = tk.Button(master=window, text="-", command=decrease)
    btn_decrease.grid(row=0, column=0, sticky="nsew")

    lbl_value = tk.Label(master=window, text="0")
    lbl_value.grid(row=0, column=1)

    btn_increase = tk.Button(master=window, text="+", command=increase)
    btn_increase.grid(row=0, column=2, sticky="nsew")

    window.mainloop()


def handler_test3():
    def roll():
        lbl_result["text"] = str(random.randint(1, 6))

    window = tk.Tk()
    window.columnconfigure(0, minsize=150)
    window.rowconfigure([0, 1], minsize=50)

    btn_roll = tk.Button(text="Roll", command=roll)
    lbl_result = tk.Label()

    btn_roll.grid(row=0, column=0, sticky="nsew")
    lbl_result.grid(row=1, column=0)

    window.mainloop()


def handler_test4():
    master = tk.Tk()
    master.title('Test')
    master.geometry("100x100+700+350")

    b1 = tk.Button(text='1')
    b1.grid(row=0, column=0)

    b2 = tk.Button(text='2')
    b2.grid(row=0, column=1)

    b3 = tk.Button(text='3')
    b3.grid(row=1, column=0)

    b4 = tk.Button(text='4')
    b4.grid(row=1, column=1)

    b5 = tk.Button(text='5')
    b5.grid(row=2, columnspan=3)

    tk.mainloop()


def column_test():
    class Example(tk.Frame):
        def __init__(self, parent):
            tk.Frame.__init__(self, parent)

            self.logo = tk.Label(self, text="Logo", background="orange")
            self.buttons = []
            for i in range(6):
                self.buttons.append(tk.Button(self, text="Button %s" % (i + 1,), background="green"))
            self.other1 = tk.Label(self, background="purple")
            self.other2 = tk.Label(self, background="yellow")
            self.other3 = tk.Label(self, background="pink")
            self.other4 = tk.Label(self, background="gray")
            self.main = tk.Frame(self, background="blue")

            self.logo.grid(row=0, column=0, rowspan=2, sticky="nsew")
            self.other1.grid(row=0, column=1, sticky="nsew")
            self.other2.grid(row=0, column=2, sticky="nsew")
            self.other3.grid(row=1, column=1, sticky="nsew")
            self.other4.grid(row=1, column=2, sticky="nsew")
            self.buttons[0].grid(row=2, column=0, sticky="nsew")
            self.buttons[1].grid(row=3, column=0, sticky="nsew")
            self.buttons[2].grid(row=4, column=0, sticky="nsew")
            self.buttons[3].grid(row=5, column=0, sticky="nsew")
            self.buttons[4].grid(row=6, column=0, sticky="nsew")
            self.buttons[5].grid(row=7, column=0, sticky="nsew")
            self.main.grid(row=2, column=2, columnspan=2, rowspan=6)

            for row in range(8):
                self.grid_rowconfigure(row, weight=1)
            for col in range(3):
                self.grid_columnconfigure(col, weight=1)

    if __name__ == "__main__":
        root = tk.Tk()
        Example(root).pack(fill="both", expand=True)
        root.geometry("800x400")
        root.mainloop()


def calculator():
    def function_equ():
        results["text"] = str(eval(results["text"]))

    def function_zero():
        results["text"] += str(zero["text"])

    def function_point():
        results["text"] += str(point["text"])

    def function_add():
        results["text"] += str(add["text"])

    def function_cle():
        results["text"] = ""

    def test_function(input_key):
        def function_num():
            results["text"] += str(input_key)

        def function_sub():
            results["text"] += str(input_key)

        def function_mul():
            results["text"] += str(input_key)

        def function_div():
            results["text"] += str(input_key)


        function_map = {
            '1': function_num, '2': function_num, '3': function_num, '4': function_num, '5': function_num, '6': function_num, '7': function_num, '8': function_num, '9': function_num, '.': function_num,
            '-': function_sub,
            '*': function_mul,
            '/': function_div,


        }
        return function_map[input_key]()

    window = tk.Tk()
    window.title("Simple calculator")

    frm_form = tk.Frame(relief=tk.SUNKEN, borderwidth=3)
    # Pack the frame into the window
    frm_form.pack(fill="both", expand=True)

    frm_form.rowconfigure([0, 1, 2, 3, 4], minsize=60, weight=0)
    frm_form.columnconfigure([0, 1, 2, 3, 4], minsize=60, weight=0)

    labels = [['7', '8', '9', '/'], ['4', '5', '6', '*'], ['1', '2', '3', '-']]

    for i in range(3):
        for j in range(4):
            btn_text = labels[i][j]
            number = tk.Button(master=frm_form, text=btn_text, command=lambda input_key=btn_text: test_function(input_key))
            number.grid(row=i, column=j, sticky="nsew")

    zero = tk.Button(master=frm_form, text="0", command=function_zero)
    zero.grid(row=3, column=0, columnspan=2, rowspan=1, sticky="nsew")

    point = tk.Button(master=frm_form, text=".", command=function_point)
    point.grid(row=3, column=2, sticky="nsew")

    add = tk.Button(master=frm_form, text="+", command=function_add)
    add.grid(row=3, column=3, sticky="nsew")

    clear = tk.Button(master=frm_form, text="c", command=function_cle)
    clear.grid(row=0, column=4, rowspan=2, sticky="nsew")

    equ = tk.Button(master=frm_form, text="=", command=function_equ)
    equ.grid(row=2, column=4, rowspan=2, sticky="nsew")

    results = tk.Label(master=frm_form, text="")
    results.grid(row=4, column=0, columnspan=5, rowspan=1, sticky="nsew", ipadx=5, ipady=5)

    window.mainloop()


def text_editor():
    def open_file():
        """Open a file for editing."""
        filepath = askopenfilename(
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")]
        )
        if not filepath:
            return
        txt_edit.delete("1.0", tk.END)
        with open(filepath, "r") as input_file:
            text = input_file.read()
            txt_edit.insert(tk.END, text)
        window.title(f"Simple Text Editor - {filepath}")

    def save_file():
        """Save the current file as a new file."""
        filepath = asksaveasfilename(
            defaultextension="txt",
            filetypes=[("Text Files", "*.txt"), ("All Files", "*.*")],
        )
        if not filepath:
            return
        with open(filepath, "w") as output_file:
            text = txt_edit.get("1.0", tk.END)
            output_file.write(text)
        window.title(f"Simple Text Editor - {filepath}")

    window = tk.Tk()
    window.title("Simple Text Editor")

    window.rowconfigure(0, minsize=800, weight=1)
    window.columnconfigure(1, minsize=800, weight=1)

    txt_edit = tk.Text(master=window)
    fr_buttons = tk.Frame(master=window)

    btn_open = tk.Button(fr_buttons, text="Open", command=open_file)
    btn_save = tk.Button(fr_buttons, text="Save As...", command=save_file)

    btn_open.grid(row=0, column=0, sticky="ew", padx=5, pady=5)
    btn_save.grid(row=1, column=0, sticky="ew", padx=5)

    fr_buttons.grid(row=0, column=0, sticky="ns")
    txt_edit.grid(row=0, column=1, sticky="nsew")

    window.mainloop()


def exam():

    root = tk.Tk()

    # setting the windows size
    root.geometry("600x400")

    # declaring string variable
    # for storing name and password
    name_var = tk.StringVar()
    passw_var = tk.StringVar()


    # defining a function that will
    # get the name and password and
    # print them on the screen
    def submit():
        name = name_entry.get()
        password = passw_var.get()

        print("The name is : " + name)
        print("The password is : " + password)

        name_var.set("")
        passw_var.set("")


    # creating a label for
    # name using widget Label
    name_label = tk.Label(root, text='Username',
                          font=('calibre',
                                10, 'bold'))

    # creating a entry for input
    # name using widget Entry
    name_entry = tk.Entry(root,
                          textvariable=name_var, font = ('calibre', 10, 'normal'))

    # creating a label for password
    passw_label = tk.Label(root,
                           text='Password',
                           font=('calibre', 10, 'bold'))

    # creating a entry for password
    passw_entry = tk.Entry(root,
                           textvariable=passw_var,
                           font=('calibre', 10, 'normal'),
                           show='*')

    # creating a button using the widget
    # Button that will call the submit function
    sub_btn = tk.Button(root, text='Submit',
                        command=submit)

    # placing the label and entry in
    # the required position using grid
    # method
    name_label.grid(row=0, column=0)
    name_entry.grid(row=0, column=1)
    passw_label.grid(row=1, column=0)
    passw_entry.grid(row=1, column=1)
    sub_btn.grid(row=2, column=1)

    # performing an infinite loop
    # for the window to display
    root.mainloop()


def excel_show():
    try:
        # Python 2
        import Tkinter as tk
        import ttk
        from tkFileDialog import askopenfilename
    except ImportError:
        # Python 3
        import tkinter as tk
        from tkinter import ttk
        from tkinter.filedialog import askopenfilename

    import pandas as pd

    # --- classes ---

    class MyWindow:

        def __init__(self, parent):

            self.parent = parent

            self.filename = None
            self.df = None

            self.text = tk.Text(self.parent)
            self.text.pack()

            self.button = tk.Button(self.parent, text='Load Data', command=self.load)
            self.button.pack()

            self.button = tk.Button(self.parent, text='Display Data', command=self.display)
            self.button.pack()

        def load(self):

            name = askopenfilename(filetypes=[('CSV', '*.csv',), ('Excel', ('*.xls', '*.xlsx'))])

            if name:
                if name.endswith('.csv'):
                    self.df = pd.read_csv(name)
                else:
                    self.df = pd.read_excel(name)

                self.filename = name

                # display directly
                # self.text.insert('end', str(self.df.head()) + '\n')

        def display(self):
            # ask for file if not loaded yet
            if self.df is None:
                self.load()

            # display if loaded
            if self.df is not None:
                self.text.insert('end', self.filename + '\n')
                self.text.insert('end', str(self.df) + '\n')

    root = tk.Tk()
    top = MyWindow(root)
    root.mainloop()

def main():
    # frame_test()
    # window_test()
    # frame_test2()
    # entry_test1()
    # entry_test2()
    # handler_test1()
    # handler_test2()
    # handler_test3()
    #handler_test4()
    calculator()
    text_editor()
    exam()
    excel_show()


if __name__ == '__main__':
    main()

