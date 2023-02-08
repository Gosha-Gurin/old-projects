import arcade
import random
import numpy as np
import time
import sys


WIDTH = 800
HEIGHT = 800


def Slider(mass, num = 1):
    for x in range(num):
        mass[82 + 80 * 38 + x * 20] = 1
        for z in range(2):
            mass[3 + z + 80 * 38 + x * 20] = 1
        for z in range(2):
            mass[84 + 80 * z + 80 * 38 + x * 20] = 1

def Random(mass, num = 1000):
    for x in range(num):
        mass[random.randint(0,6399)] = 1


class MyGameWindow(arcade.Window):
    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(0, 0)
        self.Life_list = {}
        self.delt = [[0,1],[0,-1],[-1,1],[-1,0],[-1,-1],[1,1],[1,0],[1,-1]]
        self.Run = False
        self.Cad = 0

        arcade.set_background_color(arcade.color.BLACK)
        self.A = [0] * (width // 10) * (height // 10)
        self.B = [0] * (width // 10) * (height // 10)

        #Slider(self.A)
        Random(self.A)

    def on_key_press(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.Run = True

    def on_key_release(self, symbol, modifiers):
        if symbol == arcade.key.SPACE:
            self.Run = False

    def on_draw(self):
        if self.Run:
            self.Cad += 1
        arcade.start_render()
        for x in range(80 * 80):
            if self.A[x] == 1:
                arcade.draw_point((x % 80) * 10 + 5, (x // 80) * 10 + 5, (255, 255, 255), 10)
        arcade.draw_text('Кадр: ' + str(self.Cad), 2, 780, (122, 122, 122), 15)

    def on_update(self, delta_time):
        if self.Run:
            for z in range(80 * 80):
                Sum = 0
                row = z // 80
                col = z % 80
                for x in range(8):
                    #rowS = (row + self.delt[x][0] + 80) % 80
                    #colS = (col + self.delt[x][1] + 80) % 80
                    indexS = 80 * ((row + self.delt[x][0] + 80) % 80) + (col + self.delt[x][1] + 80) % 80
                    Sum += self.A[indexS]
                if self.A[z] == 0:
                    if Sum == 3:
                        self.B[z] = 1
                    else:
                        self.B[z] = 0
                else:
                    if Sum < 2 or Sum > 3:
                        self.B[z] = 0
                    else:
                        self.B[z] = 1
                #print(z, Sum, self.B[z], self.A[z])
            for z in range(80 * 80):    
                self.A[z] = self.B[z]
            #print("===================================")

MyGameWindow(WIDTH, HEIGHT, "Grid")
arcade.run()