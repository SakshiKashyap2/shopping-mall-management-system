from os import close, stat
from tkinter import *
from tkinter import messagebox
# from PIL import ImageTk, Image
import sqlite3

root = Tk()
root.title("Verification")
root.geometry("260x130")
root.configure(bg='#569D04')

uname_password = {
    "sakshi": "kumari",
    "harsh":"sharma",
}

logged_in_user = "None"


def add(table_name, values):
    # Inserting values into Contains table:
    if table_name.lower() == "contains":
        # Create a database or connect to one
        conn = sqlite3.connect('Shopping_mall_management.db')
        # Create cursor
        cur = conn.cursor()

        cur.execute("select i_id from items")
        i_ids_tupple = cur.fetchall()
        cur.execute("select o_id from orders")
        o_ids_tupple = cur.fetchall()

        i_ids = []
        for id in i_ids_tupple:
            i_ids.append(*id)

        o_ids = []
        for id in o_ids_tupple:
            o_ids.append(*id)

        if int(values[0].get()) in i_ids and int(values[0].get()) in o_ids:
            cur.execute("insert into contains values(:i_id,:o_id)",
                        {
                            'i_id': int(values[0].get()),
                            'o_id': int(values[1].get())
                        })
        else:
            messagebox.showwarning(
                "Warninig", "Foreign key Constraint Fails!!")
            values[0].delete(0, END)
            values[1].delete(0, END)

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()

    # Inserting values into Customers table:
    if table_name.lower() == "customers":
        # Create a database or connect to one
        conn = sqlite3.connect('Shopping_mall_management.db')
        # Create cursor
        cur = conn.cursor()

        cur.execute("select T_id from tenants")
        T_ids_tupple = cur.fetchall()
        # print(T_ids)
        T_ids = []
        for id in T_ids_tupple:
            T_ids.append(*id)

        cur.execute("select c_id from customers")
        C_ids_tupple = cur.fetchall()
        C_ids = []
        for id in C_ids_tupple:
            C_ids.append(*id)

        if int(values[5].get()) in T_ids:
            if int(values[0].get()) not in C_ids:
                cur.execute("insert into customers values(:c_id,:c_name,:address,:contact_no,:email_id,:T_id)",
                            {
                                'c_id': int(values[0].get()),
                                'c_name': values[1].get(),
                                'address': values[2].get(),
                                'contact_no': int(values[3].get()),
                                'email_id': values[4].get(),
                                'T_id': int(values[5].get())
                            })
                values[0].delete(0, END)
                values[1].delete(0, END)
                values[2].delete(0, END)
                values[3].delete(0, END)
                values[4].delete(0, END)
                values[5].delete(0, END)

            else:
                messagebox.showwarning(
                    "Warninig", "Duplicate records not allowed for primary key!!")
                values[0].delete(0, END)

        else:
            messagebox.showwarning(
                "Warninig", "Foreign key Constraint Fails!!")
            values[5].delete(0, END)

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()

    # Inserting values into items table:
    if table_name.lower() == "items":
        # Create a database or connect to one
        conn = sqlite3.connect('Shopping_mall_management.db')
        # Create cursor
        cur = conn.cursor()

        cur.execute("select i_id from itmes")
        i_ids_tupple = cur.fetchall()
        i_ids = []
        for id in i_ids_tupple:
            i_ids.append(*id)

        if int(values[0].get()) not in i_ids:
            cur.execute("insert into items values(:i_id,:name,:quantity,:rate)",
                        {
                            'i_id': int(values[0].get()),
                            'name': values[1].get(),
                            'quantity': int(values[2].get()),
                            'rate': float(values[3].get())
                        })
        else:
            messagebox.showwarning(
                "Warning", "Duplicate records not allowed for primary key!!")
            values[0].delete(0, END)

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()

    # Inserting values into mall table
    if table_name.lower() == "mall":
        # Create a database or connect to one
        conn = sqlite3.connect('Shopping_mall_management.db')
        # Create cursor
        cur = conn.cursor()

        cur.execute("select m_id from mall")
        m_ids_tupple = cur.fetchall()
        m_ids = []
        for id in m_ids_tupple:
            m_ids.append(*id)

        print(m_ids)
        if int(values[0].get()) not in m_ids:
            cur.execute("insert into mall values(:m_id,:m_name,:m_location)",
                        {
                            'm_id': int(values[0].get()),
                            'm_name': values[1].get(),
                            'm_location': values[2].get()
                        })
        else:
            messagebox.showwarning(
                "Warning", "Duplicate records not allowed for primary key!!")
            values[0].delete(0, END)

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()

    # Inserting values into orders table
    if table_name.lower() == "orders":
        # Create a database or connect to one
        conn = sqlite3.connect('Shopping_mall_management.db')
        # Create cursor
        cur = conn.cursor()

        cur.execute("select o_id from orders")
        o_ids_tupple = cur.fetchall()
        o_ids = []
        for id in o_ids_tupple:
            o_ids.append(*id)

        cur.execute("select c_id from customers")
        c_ids_tupple = cur.fetchall()
        c_ids = []
        for id in c_ids_tupple:
            c_ids.append(*id)

        if int(values[5].get()) in c_ids:
            if int(values[0].get()) not in o_ids:
                cur.execute("insert into orders values(:o_id,:price,:status,:date,:date,:time,:c_id)",
                            {
                                'o_id': int(values[0].get()),
                                'price': float(values[1].get()),
                                'status': values[2].get(),
                                'date': values[3].get(),
                                'time': values[4].get(),
                                'c_id': int(values[5].get())
                            })
            else:
                messagebox.showwarning(
                    "Warning", "Duplicate records not allowed for primary key!!")
                values[0].delete(0, END)
        else:
            messagebox.showwarning("Warning", "Foreign key constraint fails!!")
            values[5].delete(0, END)

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()

    # Inserting values into payment table
    if table_name.lower() == "payment":
        # Create a database or connect to one
        conn = sqlite3.connect('Shopping_mall_management.db')
        # Create cursor
        cur = conn.cursor()

        cur.execute("select p_id from payment")
        p_ids_tupple = cur.fetchall()
        p_ids = []
        for id in p_ids_tupple:
            p_ids.append(*id)

        cur.execute("select c_id from customers")
        c_ids_tupple = cur.fetchall()
        c_ids = []
        for id in c_ids_tupple:
            c_ids.append(*id)

        cur.execute("select o_id from orders")
        o_ids_tupple = cur.fetchall()
        o_ids = []
        for id in o_ids_tupple:
            o_ids.append(*id)

        if int(values[4].get()) in c_ids and int(values[3].get()) in o_ids:
            if int(values[0].get()) not in p_ids:
                cur.execute("insert into payment values(:p_id,:payment_type,:amount,:o_id,:c_id)",
                            {
                                'p_id': int(values[0].get()),
                                'payment_type': values[1].get(),
                                'amount': float(values[2].get()),
                                'o_id': int(values[3].get()),
                                'c_id': int(values[4].get())
                            })
            else:
                messagebox.showwarning(
                    "Warning", "Duplicate records not allowed for primary key!!")
                values[0].delete(0, END)
        else:
            messagebox.showwarning("Warning", "Foreign key constraint fails!!")
            values[3].delete(0, END)
            values[4].delete(0, END)

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()

    # Inserting values into tenants table
    if table_name.lower() == "tenants":
        # Create a database or connect to one
        conn = sqlite3.connect('Shopping_mall_management.db')
        # Create cursor
        cur = conn.cursor()

        cur.execute("select t_id from tenants")
        t_ids_tupple = cur.fetchall()
        t_ids = []
        for id in t_ids_tupple:
            t_ids.append(*id)

        cur.execute("select m_id from mall")
        m_ids_tupple = cur.fetchall()
        m_ids = []
        for id in m_ids_tupple:
            m_ids.append(*id)

        if int(values[3].get()) in m_ids:
            if int(values[0].get()) not in t_ids:
                cur.execute("insert into tenants values(:t_id,:shop_no,:shop_name,:m_id)",
                            {
                                't_id': int(values[0].get()),
                                'shop_no': values[1].get(),
                                'shop_name': values[2].get(),
                                'm_id': int(values[3].get())
                            })
            else:
                messagebox.showwarning(
                    "Warning", "Duplicate records not allowed for primary key!!")
                values[0].delete(0, END)
        else:
            messagebox.showwarning("Warning", "Foreign key constraint fails!!")
            values[3].delete(0, END)

        # Commit Changes
        conn.commit()
        # Close connection
        conn.close()


def show_selected(attributes, table_name):
    # return
    # Create a database or connect to one
    conn = sqlite3.connect('Shopping_mall_management.db')
    # Create cursor
    cur = conn.cursor()
    query = "select "
    for i in range(len(attributes)):
        query += attributes[i]+","

    query = query[:-1] + f" from {table_name};"
    # print(query)

    cur.execute(query)
    data = cur.fetchall()
    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()

    # Displaying the record in tabular form
    data_frame = Tk()
    data_frame.title("Selected Records of table - "+table_name)
    data_frame.configure(bg='#50C878')

    for i in range(len(attributes)):
        attribute_Entry = Entry(data_frame, fg="blue", font=(
            'Arial', 10, 'bold'), width=25, justify='center')
        attribute_Entry.grid(row=0, column=i, columnspan=1)
        attribute_Entry.insert(0, attributes[i])
        attribute_Entry.configure(bg='#B0FF55')

    for i in range(len(data)):
        info = (data[i])
        for j in range(len(info)):
            data_Entry = Entry(data_frame, font=(
                'Arial', 10, 'bold'), width=25, justify='center')
            data_Entry.grid(row=i+1, column=j, columnspan=1)
            data_Entry.insert(0, info[j])

    close_btn = Button(data_frame, text="Close",
                       command=lambda: data_frame.destroy())
    close_btn.grid(row=1+len(data), column=0, padx=10,
                   pady=10, columnspan=len(data[0]))


def show_all(table_name):
    # Create a database or connect to one
    conn = sqlite3.connect('Shopping_mall_management.db')
    # Create cursor
    cur = conn.cursor()

    cur.execute("select * from "+table_name)
    attributes = list(map(lambda x: x[0], cur.description))
    print(attributes)

    cur.execute("select * from "+table_name)
    data = cur.fetchall()
    print(data)

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()

    # Displaying the record in tabular form
    data_frame = Tk()
    data_frame.title("Records of table - "+table_name)
    data_frame.configure(bg='#50C878') 

    for i in range(len(attributes)):
        attribute_Entry = Entry(data_frame, fg="blue", font=(
            'Arial', 10, 'bold'), width=25, justify='center')
        attribute_Entry.grid(row=0, column=i, columnspan=1)
        attribute_Entry.insert(0, attributes[i])
        attribute_Entry.configure(bg='#B0FF55')

    for i in range(len(data)):
        info = (data[i])
        for j in range(len(info)):
            data_Entry = Entry(data_frame, font=(
                'Arial', 10, 'bold'), width=25, justify='center')
            data_Entry.grid(row=i+1, column=j, columnspan=1)
            data_Entry.insert(0, info[j])

    close_btn = Button(data_frame, text="Close",
                       command=lambda: data_frame.destroy())
    close_btn.grid(row=1+len(data), column=0, padx=10,
                   pady=10)


def display(table_name, table_work, row_no):
    show_all_btn = Button(table_work, text="Show all Records",
                          command=lambda: show_all(table_name))
    show_all_btn.grid(row=row_no+3, column=0, padx=10, pady=10)
    show_all_btn.configure(bg='#000000',fg='#FFFFFF')

    # Create a database or connect to one
    conn = sqlite3.connect('Shopping_mall_management.db')
    # Create cursor
    cur = conn.cursor()

    cur.execute("select * from "+table_name)
    attributes = list(map(lambda x: x[0], cur.description))

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()
    print(attributes)

    listbox = Listbox(table_work, selectmode=MULTIPLE, width=15)
    listbox.grid(row=row_no+4, column=0, padx=10, pady=10)
    for i in range(len(attributes)):
        listbox.insert(i+1, attributes[i])

    def selected():
        reslist = list()
        selection = listbox.curselection()

        for i in selection:
            val = listbox.get(i)
            reslist.append(val)

        # print(reslist)
        show_selected(reslist, table_name)

    choices_btn = Button(
        table_work, text="Show selected Attributes", command=selected)
    choices_btn.grid(row=len(attributes)+row_no+5, column=0, padx=10, pady=10)
    choices_btn.configure(bg='#000000',fg='#FFFFFF')


def work(table_name):
    table_work = Tk()
    table_work.title("Table "+table_name)
    table_work.configure(bg='#ADD8E6')

    # Create a database or connect to one
    conn = sqlite3.connect('Shopping_mall_management.db')
    # Create cursor
    cur = conn.cursor()

    cur.execute("select * from "+table_name)
    attributes = list(map(lambda x: x[0], cur.description))
    # print(attributes)

    values = []
    for i in range(len(attributes)):
        label = Label(table_work, text=attributes[i]+" : :",relief='groove')
        label.grid(row=i, column=0, padx=10, pady=10)
        label.configure(bg='#B0FF55')

        entry = Entry(table_work, width=30)
        entry.grid(row=i, column=1, padx=10, pady=10, columnspan=2)
        values.append(entry)

    add_btn = Button(table_work,text="Add record to table",
                     command=lambda: add(table_name, values))
    add_btn.grid(row=len(attributes)+1, column=0,
                 columnspan=1, padx=10, pady=10)
    add_btn.configure(bg='#000000',fg='#FFFFFF')

    

    show_btn = Button(table_work, text="Show records", command=lambda: display(
        table_name, table_work, len(attributes)+1))
    show_btn.grid(row=len(attributes)+1, column=1,
                  columnspan=1, padx=10, pady=10)
    show_btn.configure(bg='#000000',fg='#FFFFFF')

    change_table_btn = Button(
        table_work, text="Change Table", command=lambda: table_work.destroy())
    change_table_btn.grid(row=len(attributes)+1, column=2,
                          columnspan=1, padx=10, pady=10)
    change_table_btn.configure(bg='#000000',fg='#FFFFFF')

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()

    def delete(id):
        if id == "":
            messagebox.showerror("Error", "Invalid Id!!")
        else:
            # Create a database or connect to one
            conn = sqlite3.connect('Shopping_mall_management.db')
            # Create cursor
            cur = conn.cursor()

            cur.execute(f"select {attributes[0]} from {table_name};")
            ids_tupple = cur.fetchall()
            keys = []
            for ids in ids_tupple:
                keys.append(*ids)

            print(id, keys)
            if int(id) in keys:
                cur.execute(
                    f"delete from {table_name} where {attributes[0]} = {id}")
                messagebox.showinfo(
                    "Deleted record", f"Deleted record in {table_name} where {attributes[0]} :: {id}")
            else:
                messagebox.showerror("Error", "Id not present!!")
            # Commit Changes
            conn.commit()
            # Close connection
            conn.close()

    def edit(id, table_name):
        # return
        global editor
        editor = Tk()
        editor.title("Update a record")
        editor.configure(bg='#D4A017')

        if id == "":
            editor.destroy()
            messagebox.showerror("Error", "Invalid primary key value!!")
        else:
            # Create a database or connect to one
            conn = sqlite3.connect('Shopping_mall_management.db')
            # Create cursor
            cur = conn.cursor()

            cur.execute("select * from "+table_name)
            attributes = list(map(lambda x: x[0], cur.description))
            # print(attributes)

            cur.execute(
                f"select * from {table_name} where {attributes[0]} = {id};")
            temp = cur.fetchall()
            # print(temp)

            # Commit Changes
            conn.commit()
            # Close connection
            conn.close()

            def save(values, prim_id, table_name):
                # return
                # Updateing values into Contains table:
                if table_name.lower() == "contains":
                    # Create a database or connect to one
                    conn = sqlite3.connect('Shopping_mall_management.db')
                    # Create cursor
                    cur = conn.cursor()

                    cur.execute("select i_id from items")
                    i_ids_tupple = cur.fetchall()
                    cur.execute("select o_id from orders")
                    o_ids_tupple = cur.fetchall()

                    i_ids = []
                    for id in i_ids_tupple:
                        i_ids.append(*id)

                    o_ids = []
                    for id in o_ids_tupple:
                        o_ids.append(*id)

                    if int(values[0].get()) in i_ids and int(values[0].get()) in o_ids:
                        cur.execute(f"""update {table_name} set
                                    i_id=: i_id,
                                    o_id=: o_id
                                    where i_id={prim_id}""",
                                    {
                                        'i_id': int(values[0].get()),
                                        'o_id': int(values[1].get())
                                    })
                        messagebox.showinfo(
                            "Record Updated", f"Updated records of id : {prim_id} in {table_name} table")
                        editor.destroy()
                    else:
                        messagebox.showwarning(
                            "Warninig", "Foreign key Constraint Fails!!")
                        values[0].delete(0, END)
                        values[1].delete(0, END)

                    # Commit Changes
                    conn.commit()
                    # Close connection
                    conn.close()

                # Updating values into Customers table:
                if table_name.lower() == "customers":
                    # Create a database or connect to one
                    conn = sqlite3.connect('Shopping_mall_management.db')
                    # Create cursor
                    cur = conn.cursor()

                    cur.execute("select T_id from tenants")
                    T_ids_tupple = cur.fetchall()
                    # print(T_ids)
                    T_ids = []
                    for id in T_ids_tupple:
                        T_ids.append(*id)

                    if int(values[5].get()) in T_ids:
                        cur.execute(f"""update {table_name} set 
                                    c_name = "{values[1].get()}",
                                    address = "{values[2].get()}",
                                    contact_no = {int(values[3].get())},
                                    email_id = "{values[4].get()}",
                                    t_id = {int(values[5].get())}
                                    where c_id = {prim_id};""")

                        messagebox.showinfo(
                            "Record Updated", f"Updated records of id : {prim_id} in {table_name} table")
                        editor.destroy()
                    else:
                        messagebox.showwarning(
                            "Warninig", "Foreign key Constraint Fails!!")
                        values[5].delete(0, END)

                    # Commit Changes
                    conn.commit()
                    # Close connection
                    conn.close()

                # Updating values into items table:
                if table_name.lower() == "items":
                    # Create a database or connect to one
                    conn = sqlite3.connect('Shopping_mall_management.db')
                    # Create cursor
                    cur = conn.cursor()

                    cur.execute(f"""update {table_name} set
                                name = :name,
                                quantity = :quantity,
                                rate = :rate
                                where i_id = {prim_id};""",
                                {
                                    'name': values[1].get(),
                                    'quantity': int(values[2].get()),
                                    'rate': float(values[3].get())
                                })
                    messagebox.showinfo(
                        "Record Updated", f"Updated records of id : {prim_id} in {table_name} table")
                    editor.destroy()
                    # Commit Changes
                    conn.commit()
                    # Close connection
                    conn.close()

                # Updating values into mall table
                if table_name.lower() == "mall":
                    # Create a database or connect to one
                    conn = sqlite3.connect('Shopping_mall_management.db')
                    # Create cursor
                    cur = conn.cursor()
                    cur.execute(f"""update {table_name} set 
                                m_name = :m_name,
                                m_location = :m_location
                                where m_id = {prim_id};""",
                                {
                                    'm_name': values[1].get(),
                                    'm_location': values[2].get()
                                })
                    messagebox.showinfo(
                        "Record Updated", f"Updated records of id : {prim_id} in {table_name} table")
                    editor.destroy()
                    # Commit Changes
                    conn.commit()
                    # Close connection
                    conn.close()

                # Updating values into orders table
                if table_name.lower() == "orders":
                    # Create a database or connect to one
                    conn = sqlite3.connect('Shopping_mall_management.db')
                    # Create cursor
                    cur = conn.cursor()

                    cur.execute("select c_id from customers")
                    c_ids_tupple = cur.fetchall()
                    c_ids = []
                    for id in c_ids_tupple:
                        c_ids.append(*id)

                    if int(values[5].get()) in c_ids:
                        cur.execute(f"""update {table_name} set
                                    price = :price,
                                    status = :status,
                                    date = :date,
                                    time = :time,
                                    c_id = :c_id
                                    where o_id = {prim_id};""",
                                    {
                                        'price': float(values[1].get()),
                                        'status': values[2].get(),
                                        'date': values[3].get(),
                                        'time': values[4].get(),
                                        'c_id': int(values[5].get())
                                    })
                        messagebox.showinfo(
                            "Record Updated", f"Updated records of id : {prim_id} in {table_name} table")
                        editor.destroy()
                    else:
                        messagebox.showwarning(
                            "Warning", "Foreign key constraint fails!!")
                        values[5].delete(0, END)

                    # Commit Changes
                    conn.commit()
                    # Close connection
                    conn.close()

                # Updating values into payment table
                if table_name.lower() == "payment":
                    # Create a database or connect to one
                    conn = sqlite3.connect('Shopping_mall_management.db')
                    # Create cursor
                    cur = conn.cursor()

                    cur.execute("select c_id from customers")
                    c_ids_tupple = cur.fetchall()
                    c_ids = []
                    for id in c_ids_tupple:
                        c_ids.append(*id)

                    cur.execute("select o_id from orders")
                    o_ids_tupple = cur.fetchall()
                    o_ids = []
                    for id in o_ids_tupple:
                        o_ids.append(*id)

                    if int(values[4].get()) in c_ids and int(values[3].get()) in o_ids:
                        cur.execute(f"""update {table_name} 
                                    payment_type = :payment_type,
                                    amount = :amount,
                                    o_id = :o_id,
                                    c_id = :c_id)
                                    where p_id = {prim_id};""",
                                    {
                                        'payment_type': values[1].get(),
                                        'amount': float(values[2].get()),
                                        'o_id': int(values[3].get()),
                                        'c_id': int(values[4].get())
                                    })
                        messagebox.showinfo(
                            "Record Updated", f"Updated records of id : {prim_id} in {table_name} table")
                        editor.destroy()
                    else:
                        messagebox.showwarning(
                            "Warning", "Foreign key constraint fails!!")
                        values[3].delete(0, END)
                        values[4].delete(0, END)

                    # Commit Changes
                    conn.commit()
                    # Close connection
                    conn.close()

                # Upadting values into tenants table
                if table_name.lower() == "tenants":
                    # Create a database or connect to one
                    conn = sqlite3.connect('Shopping_mall_management.db')
                    # Create cursor
                    cur = conn.cursor()

                    cur.execute("select m_id from mall")
                    m_ids_tupple = cur.fetchall()
                    m_ids = []
                    for id in m_ids_tupple:
                        m_ids.append(*id)

                    if int(values[3].get()) in m_ids:
                        cur.execute(f"""update {table_name} set
                                    shop_no = :shop_no,
                                    shop_name = :shop_name,
                                    m_id = :m_id
                                    where t_id = {prim_id}""",
                                    {
                                        'shop_no': values[1].get(),
                                        'shop_name': values[2].get(),
                                        'm_id': int(values[3].get())
                                    })
                        messagebox.showinfo(
                            "Record Updated", f"Updated records of id : {prim_id} in {table_name} table")
                        editor.destroy()
                    else:
                        messagebox.showwarning(
                            "Warning", "Foreign key constraint fails!!")
                        values[3].delete(0, END)

                    # Commit Changes
                    conn.commit()
                    # Close connection
                    conn.close()

            values = []
            for i in range(len(attributes)):
                label = Label(editor, text=attributes[i]+" : :")
                label.grid(row=i, column=0, padx=10, pady=10)
                label.configure(bg='#B0FF55') 

                entry = Entry(editor, width=30)
                entry.grid(row=i, column=1, padx=10, pady=10, columnspan=2)
                values.append(entry)

            for i in range(len(attributes)):
                values[i].insert(0, temp[0][i])

            save_btn = Button(editor, text="Save Record",
                              command=lambda: save(values, id, table_name))
            save_btn.grid(row=len(attributes)+1, column=0,
                          columnspan=1, padx=10, pady=10)
            save_btn.configure(bg='#000000',fg='#FFFFFF')

            close_btn = Button(editor, text="Close",
                               command=lambda: editor.destroy())
            close_btn.grid(row=len(attributes)+1, column=1,
                           columnspan=1, padx=10, pady=10)
            close_btn.configure(bg='#000000',fg='#FFFFFF')

    select_label = Label(table_work, text="Enter "+attributes[0],relief='groove')
    select_label.grid(row=len(attributes)+2, column=0,
                      columnspan=1, padx=10, pady=10)
    select_label.configure(bg='#B0FF55')

    prim_select = Entry(table_work, width=15)
    prim_select.grid(row=len(attributes)+2, column=1,
                     columnspan=1, padx=10, pady=10)

    delete_btn = Button(table_work, text="Delete Record",
                        command=lambda: delete(prim_select.get()))
    delete_btn.grid(row=len(attributes)+3, column=0,
                    columnspan=1, padx=10, pady=10)
    delete_btn.configure(bg='#000000',fg='#FFFFFF')

    edit_btn = Button(table_work, text="Edit Record",
                      command=lambda: edit(prim_select.get(), table_name))
    edit_btn.grid(row=len(attributes)+3, column=1,
                  columnspan=1, padx=10, pady=10)
    edit_btn.configure(bg='#000000',fg='#FFFFFF')

    close_btn = Button(table_work, text="Close",
                       command=lambda: table_work.destroy())
    close_btn.grid(row=len(attributes)+3, column=2,
                   columnspan=1, padx=10, pady=10)
    close_btn.configure(bg='#000000',fg='#FFFFFF')

def check_table(table_name):
    print(table_name)
    if table_name == "---Select---":
        messagebox.showerror("Error", "Invalid Table Selected!!")
    else:
        work(table_name)

# Actual database


def logged(name):
    # Create a database or connect to one
    conn = sqlite3.connect('Shopping_mall_management.db')

    # Create cursor
    cur = conn.cursor()

        # # Creating the required tables
        # cur.execute("""
        #     create table mall(
        #         M_id integer,
        #         M_name text,
        #         M_location text,
        #         primary key(M_id)
        # )""")

        # cur.execute("""
        #     create table tenants(
        #         T_id integer,
        #         shop_no text,
        #         shop_name text,
        #         M_id integer,
        #         primary key(T_id),
        #         foreign key(M_id) references mall(M_id)
        # )""")

        # cur.execute("""
        #     create table customers(
        #         C_id integer,
        #         C_name text,
        #         address text,
        #         contact_no integer,
        #         email_id text,
        #         T_id integer,
        #         primary key(C_id),
        #         foreign key(T_id) references tenants(T_id)
        # )""")

        # cur.execute("""
        #     create table orders(
        #         O_id integer,
        #         price real,
        #         status text,
        #         date text,
        #         time text,
        #         C_id integer,
        #         primary key(O_id),
        #         foreign key(C_id) references tenants(C_id)
        # )""")

        # cur.execute("""
        #     create table payment(
        #         P_id integer,
        #         payment_type text,
        #         amount real,
        #         o_id integer,
        #         c_id integer,
        #         primary key(P_id),
        #         foreign key(o_id) references orders(O_id),
        #         foreign key(c_id) references customers(c_id)
        #     )
        # """)

        # cur.execute("""
        #     create table items(
        #         I_id integer,
        #         name text,
        #         quantity integer,
        #         rate real,
        #         primary key(I_id)
        #     )
        # """)

        # cur.execute("""
        #     create table contains(
        #         i_id integer,
        #         o_id integer,
        #         foreign key(i_id) references items(I_id),
        #         foreign key(o_id) references orders(O_id)
        #     )
        # """)

    # Commit Changes
    conn.commit()

    # Close connection
    conn.close()

    database_frame = Tk()
    database_frame.title("Database")
    database_frame.configure(bg='#569D04')
    # database_frame.geometry("600x400")

    message = "Current User : :  "+name.upper()+" "
    # user_label = Label(database_frame, text=message)
    # user_label.grid(row=0, column=0, padx=10, pady=10)

    frame = LabelFrame(database_frame, text=message, padx=10, pady=10)
    frame.pack(padx=10, pady=10)
    frame.configure(bg='#569D04')
    main_label = Label(frame, text="Select the table to work with ")
    main_label.grid(row=0, column=0, padx=10, pady=10, columnspan=1)
    main_label.configure(bg='#B0FF55')

    # Create a database or connect to one
    conn = sqlite3.connect('Shopping_mall_management.db')
    # Create cursor
    cur = conn.cursor()
    # Retriving all tables present in database
    cur.execute("""
        SELECT name 
        FROM sqlite_master
        WHERE type='table'
        ORDER BY name;
    """)
    tables = cur.fetchall()
    table_names = []
    for table in tables:
        # print(*table)
        table_names.append(*table)

    print(table_names)

    # Commit Changes
    conn.commit()
    # Close connection
    conn.close()

    def selected(event):
        msg = "Selected Table : : "+table_selected.get()
        tmp_label.config(text=msg)
        tmp_label.configure(bg='#FFF380')

    table_selected = StringVar()
    table_selected.set("---Select---")
    tables_dropdown = OptionMenu(
        frame, table_selected, *table_names, command=selected)
    tables_dropdown.grid(row=0, column=1, padx=10, pady=10)
    tables_dropdown.configure(bg='#50C878')

    tmp_label = Label(frame, text="Selected Table : : "+table_selected.get())
    tmp_label.grid(row=1, column=0, columnspan=2, padx=10, pady=10)
    tmp_label.configure(bg='#FFF380')

    submit = Button(frame, text="continue",
                    command=lambda: check_table(table_selected.get()))
    submit.grid(row=2, column=0, columnspan=1, padx=10, pady=10)
    submit.configure(bg='#000000',fg='#FFFFFF')

    close_btn = Button(frame, text="close",
                       command=lambda: database_frame.destroy())
    close_btn.grid(row=2, column=1, columnspan=1, padx=10, pady=10)
    close_btn.configure(bg='#000000',fg='#FFFFFF')

# Retry credential function


def retry():
    verify()
    user_name_entry.delete(0, END)
    user_pwd_entry.delete(0, END)

# User validation function


def verify():
    user = user_name_entry.get()
    pwd = user_pwd_entry.get()

    if user in uname_password:
        if pwd == uname_password[user]:
            logged_in_user = user
            # print(logged_in_user)
            user_name_entry.delete(0, END)
            user_pwd_entry.delete(0, END)
            logged(logged_in_user)

        else:
            messagebox.showwarning("Warning", "Incorrect Password")
            retry_btn = Button(root, text="Retry",
                               command=retry)
            retry_btn.grid(row=2, column=1, padx=10, pady=10)
    else:
        messagebox.showwarning("Warning", "Invalid User")
        retry_btn = Button(root, text="Retry",
                           command=retry)
        retry_btn.grid(row=2, column=1, padx=10, pady=10)


# User Login Menu
user_name_label = Label(root, text="User name")
user_name_label.grid(row=0, column=0, padx=10, pady=10)
user_name_label.configure(bg='#B0FF55') 

user_pwd_label = Label(root, text="Password")
user_pwd_label.grid(row=1, column=0, padx=10, pady=10)
user_pwd_label.configure(bg='#B0FF55')

user_name_entry = Entry(root, width=20)
user_name_entry.grid(row=0, column=1, padx=10, pady=10)

user_pwd_entry = Entry(root, width=20)
user_pwd_entry.grid(row=1, column=1, padx=10, pady=10)

login_btn = Button(root, text="Login", command=verify)
login_btn.grid(row=2, column=0, padx=10, pady=10)


root.mainloop()
