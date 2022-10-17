#!/usr/bin/python
# -*- coding: utf-8 -*-

from tkinter import PhotoImage, Tk, Canvas, ARC


if __name__ == '__main__':
    root = Tk()
    root.title('Рисунок')
    root.geometry('900x500')

    c = Canvas(root, width=900, height=500, bg='white')
    c.pack()

    # Создаем основу дома и солнце
    c.create_oval(383, 18, 450, 84, fill="#FFFF00")
    c.create_rectangle(129, 143, 340, 360, fill='orange')
    c.create_polygon(232, 30, 90, 144, 375, 143, fill='#804040')

    # Создаем кота
    img = PhotoImage(file='1.png')
    #c.create_image(640, 270, image=img)

    c.create_polygon(526, 180, 528, 165, 530, 155, 528, 145, 525, 139, 535, 130, 550, 121, 565,
    112, 575, 104, 570, 94, 551, 91, 536, 93, 521, 97, 506, 101, 486, 105, 471, 108, 456, 111,
    446, 114, 436, 119, 426, 124, 416, 133, 406, 142, 406, 167, 420, 172, 440, 172, 458, 174,
    470, 177, 484, 207, 490, 257, 492, 277, 497, 287, 504, 297, 520, 307, 535, 317, 543, 320,
    547, 335, 557, 346, 567, 357, 588, 370, 584, 420, 580, 420, 540, 430, 520, 445, 622, 445,
    631, 360, 647, 370, 644, 420, 640, 420, 600, 430, 580, 445, 680, 445, 694, 354, 689, 345,
    685, 330, 689, 315, 700, 300, 718, 273, 830, 230, 850, 223, 880, 190, 815, 210, 750, 217,
    530, 204, 530, 200, fill="#fba94f")
    c.create_oval(450, 135, 460, 145, fill="black")
    c.create_arc(580, 465, 650, 425, start=180, extent=-110, style=ARC, width=1, outline='black')


    # Добавляем детали к дому
    c.create_rectangle(200, 160, 265, 227, fill='white')
    c.create_line(232, 160, 232, 227)
    c.create_line(200, 195, 265, 195)
    c.create_rectangle(260, 250, 315, 355, fill='#753313')
    c.create_oval(298, 305, 308, 315, fill="black")
    
    x = 0
    while x < 900:
        c.create_arc(x, 555, x+90, 450, start=180, extent=-80, style=ARC, width=3, outline='green')
        x += 15

    root.mainloop()
