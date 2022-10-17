#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Listbox, Button, EXTENDED, END


def add_item():
    product = []
    select = list(lbox_first.curselection())
    select.reverse()
    for item in select:
        op = lbox_first.get(item)
        product.append(op)
    for val in product:
        lbox_second.insert(0, val)
    for k in select:
        lbox_first.delete(k)


def delete_item():
    product = []
    select = list(lbox_second.curselection())
    select.reverse()
    for item in select:
        op = lbox_second.get(item)
        product.append(op)
    for val in product:
        lbox_first.insert(0, val)
    for k in select:
        lbox_second.delete(k)


if __name__ == '__main__':
    root = Tk()
    root.title('Продукты')
    root.geometry('380x240')

    products = ['apple', 'bananas', 'carrot', 'bread', 'butter', 'meat', 'potato', 'Enigma', 'pineapple']

    lbox_first = Listbox(selectmode=EXTENDED)
    lbox_second = Listbox(selectmode=EXTENDED)

    button_up = Button(height=1, width=5, text='>>>', command=add_item)
    button_back = Button(height=1, width=5, text='<<<', command=delete_item)

    lbox_first.grid(row=1, column=1, pady=15, padx=3)
    lbox_second.grid(row=1, column=4, pady=15)

    button_up.grid(row=1, column=2, padx=3)
    button_back.grid(row=1, column=3, padx=5)

    for i in products:
        lbox_first.insert(END, i)

    root.mainloop()
