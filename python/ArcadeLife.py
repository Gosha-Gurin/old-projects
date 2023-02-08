#Аркадная жизнь
import arcade
import random


WIDTH = 800
HEIGHT = 800


class MyGameWindow(arcade.Window):

    def __init__(self, width, height, title):
        super().__init__(width, height, title)
        self.set_location(0, 0)
        self.Bot_list = {}
        self.Food_list = {}
        self.Poison_list = {}
        self.Bot_gen = {}
        self.Bot_life = {}

        arcade.set_background_color(arcade.color.BLACK)
        self.A = [0] * (width // 10) * (height // 10)
        #Это яд
        for x in range(50):
            Pois_rand = random.randint(0, 6399)
            self.A[Pois_rand] = 'R'
            self.Poison_list[x] = Pois_rand
        #Это еда
        for x in range(70):
            Food_rand = random.randint(0, 6399)
            self.A[Food_rand] = 'G'
            self.Food_list[x] = Food_rand
        #Это боты
        for x in range(25):
            Bot_Rand = random.randint(0, 6399)
            self.A[Bot_Rand] = 'B'
            self.Bot_list[x] = Bot_Rand
            self.Bot_gen[x] = [1] * 48
            self.Bot_life[x] = 25
        #Это создани файла с исх. данными
        o = open('Bot_list.txt', 'w')
        o.write(str(self.Bot_list) + '\n' + str(self.Bot_gen))
        self.Number_B = 0

    def on_draw(self):
        arcade.start_render()

        for x in range(6400):
            if self.A[x] == 'R':
                arcade.draw_point((x % 80) * 10 + 5, (x // 80) * 10 + 5, (255, 0, 0), 10)
            if self.A[x] == 'G':
                arcade.draw_point((x % 80) * 10 + 5, (x // 80) * 10 + 5, (0, 255, 0), 10)
            if self.A[x] == 'B':
                Bot_x = (x % 80) * 10 + 5
                Bot_y = (x // 80) * 10 + 5
                arcade.draw_point(Bot_x, Bot_y, (0, 0, 255), 10)
                arcade.draw_text(str(self.Bot_life[self.Number_B]), Bot_x - 5, Bot_y - 5, (255, 255, 255), 8)
                if self.Number_B < 24:
                    self.Number_B += 1

    def on_update(self, delta_time):
        for x in range(self.Number_B):
            for y in range(46):
                if self.Bot_gen[x][y] == 0:
                    self.A[self.Bot_list[x] % 6400] = 0
                    self.A[(self.Bot_list[x] + 79) % 6400] = 'B'
                    self.Bot_list[x] = (self.Bot_list[x] + 79) % 6400
                if self.Bot_gen[x][y] == 1:
                    self.A[self.Bot_list[x] % 6400] = 0
                    self.A[(self.Bot_list[x] + 80) % 6400] = 'B'
                    self.Bot_list[x] = (self.Bot_list[x] + 80) % 6400
                if self.Bot_gen[x][y] == 2:
                    self.A[self.Bot_list[x] % 6400] = 0
                    self.A[(self.Bot_list[x] + 81) % 6400] = 'B'
                    self.Bot_list[x] = (self.Bot_list[x] + 81) % 6400
                if self.Bot_gen[x][y] == 3:
                    self.A[self.Bot_list[x] % 6400] = 0
                    self.A[(self.Bot_list[x] + 1) % 6400] = 'B'
                    self.Bot_list[x] = (self.Bot_list[x] + 1) % 6400
                if self.Bot_gen[x][y] == 4:
                    self.A[self.Bot_list[x] % 6400] = 0
                    self.A[(self.Bot_list[x] - 79) % 6400] = 'B'
                    self.Bot_list[x] = (self.Bot_list[x] - 79) % 6400
                if self.Bot_gen[x][y] == 5:
                    self.A[self.Bot_list[x] % 6400] = 0
                    self.A[(self.Bot_list[x] - 80) % 6400] = 'B'
                    self.Bot_list[x] = (self.Bot_list[x] - 80) % 6400
                if self.Bot_gen[x][y] == 6:
                    self.A[self.Bot_list[x] % 6400] = 0
                    self.A[(self.Bot_list[x] - 81) % 6400] = 'B'
                    self.Bot_list[x] = (self.Bot_list[x] - 81) % 6400
                if self.Bot_gen[x][y] == 7:
                    self.A[self.Bot_list[x] % 6400] = 0
                    self.A[(self.Bot_list[x] - 1) % 6400] = 'B'
                    self.Bot_list[x] = (self.Bot_list[x] - 1) % 6400

            self.Bot_gen[x][random.randint(0, 45)] = random.randint(0, 46)


MyGameWindow(WIDTH, HEIGHT, "ArcadeLife")
arcade.run()