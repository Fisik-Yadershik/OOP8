#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from tkinter import Tk, Canvas
import math
from time import sleep


class Table:
    def __init__(self) -> None:
        self.height = 400
        self.width = 400
        self.c = Canvas(root, width=self.width, height=self.height, bg="white")
        self.c.pack()


class GameBall:
    def __init__(self, color, width, height):
        self.color = color
        self.vx = 1
        self.vy = 1
        self.t = 0
        self.dt = 1
        self.i = 0
        self.r = 0
        self.dx = 0
        self.dy = 0
        self.p = 0
        self.width=width
        self.height=height
        self.rad = 20
        self.ball = table.c.create_oval(self.width // 2 - self.rad, self.height // 2 - self.rad,
                                       self.width // 2 + self.rad, self.height // 2 + self.rad, fill=self.color)

        table.c.bind('<Button-1>', self.onclick)
        root.after(10, self.onframe)

    def onclick(self, event):
        ball1.p = table.c.coords(ball1.ball)
        ball1.dx = event.x - ball1.p[0]
        ball1.dy = event.y - ball1.p[1]

        ball1.r = math.sqrt(ball1.dx ** 2 + ball1.dy ** 2)

        ball1.vx = ball1.dx / ball1.r
        ball1.vy = ball1.dy / ball1.r

        ball1.t += ball1.dt
        ball1.p[0] += ball1.vx + 10
        ball1.p[1] += ball1.vy + 10

        ball2.p = table.c.coords(ball2.ball)
        ball2.dx = event.x - ball2.p[0]
        ball2.dy = event.y - ball2.p[1]

        ball2.r = math.sqrt(ball2.dx ** 2 + ball2.dy ** 2)

        ball2.vx = ball2.dx / ball2.r
        ball2.vy = ball2.dy / ball2.r

        ball2.t += ball2.dt
        ball2.p[0] += ball2.vx + 10
        ball2.p[1] += ball2.vy + 10

    def onframe(self):
        table.c.move(ball1.ball, ball1.dt * ball1.vx, ball1.dt * ball1.vy)
        table.c.move(ball2.ball, ball2.dt * ball2.vx, ball2.dt * ball2.vy)
        ball1.p = table.c.coords(ball1.ball)
        ball2.p = table.c.coords(ball2.ball)

        l = math.sqrt( (ball1.p[1] - ball2.p[1])**2 + (ball1.p[0] - ball2.p[0])**2 )
        if l <= ball1.rad + ball2.rad:
            ball1.vy = -ball1.vy
            ball2.vy = -ball2.vy
            ball1.vx = -ball1.vx
            ball2.vx = -ball2.vx    

        if ball1.p[1] < 0 or ball1.p[1] > ball2.height - 2 * ball2.rad:
            ball1.vy = -ball1.vy

        if ball1.p[0] < 0 or ball1.p[0] > ball2.width - 2 * ball2.rad:
            ball1.vx = -ball1.vx

        if ball2.p[1] < 0 or ball2.p[1] > ball2.height - 2 * ball2.rad:
            ball2.vy = -ball2.vy

        if ball2.p[0] < 0 or ball2.p[0] > ball2.width - 2 * ball2.rad:
            ball2.vx = -ball2.vx

        root.after(10, self.onframe)


if __name__ == '__main__':
    root = Tk()
    root.resizable(False, False)
    table = Table()
    ball2 = GameBall("red", 400, 400)
    ball1 = GameBall("green", 500, 500)
    table, ball2, ball1
    root.mainloop()
