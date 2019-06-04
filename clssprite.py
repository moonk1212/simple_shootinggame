from tkinter import *
import random
import time
import clscoord
class Sprite:
    def __init__(self, game):
        self.game = game
        self.endgame = False
        self.coordinates = None
    def move(self):
        pass
    def coords(self):
        return self.coordinates
class PlatformSprite(Sprite):
    def __init__(self, game, photo_image, x, y, width, height):
        Sprite.__init__(self, game)
        self.photo_image = photo_image
        self.image = game.canvas.create_image(x, y, image=self.photo_image, anchor='nw')
        self.coordinates = clscoord.Coords(x, y, x + width, y + height)
        
class StickFigureSprite(Sprite):
    def __init__(self, game):
        Sprite.__init__(self, game)
        self.images_left = [
            PhotoImage(file="C.png"),
            PhotoImage(file="C.png"),
            PhotoImage(file="C.png")
        ]
        self.images_right = [
            PhotoImage(file="C.png"),
            PhotoImage(file="C.png"),
            PhotoImage(file="C.png")
        ]
        self.image = game.canvas.create_image(0,0, image=self.images_left[0], anchor='nw')
        self.x = -2
        self.y = 0
        self.current_image = 0
        self.current_image_add = 1
        self.jump_count = 0
        self.last_time = time.time()
        self.coordinates = clscoord.Coords()
        game.canvas.bind_all('<KeyPress-Left>', self.turn_left)
        game.canvas.bind_all('<KeyPress-Right>', self.turn_right)
        game.canvas.bind_all('<space>', self.jump)
        game.canvas.bind_all('<KeyPress-Up>', self.turn_up)
        game.canvas.bind_all('<KeyPress-Down>', self.turn_down)

    def turn_left(self, evt):
        if self.y == 0:
            self.x = -2

    def turn_right(self, evt):
        if self.y == 0:
            self.x = 2

    def jump(self, evt):
        if self.y == 0:
            self.y = -50
            self.jump_count = 0
    def turn_up(self,evt):
        if self.x==0:
            self.y=-2
    def turn_down(self,evt):
        if self.x==0:
            self.y=2
            
    def animate(self):
        if self.x != 0 and self.y == 0:
            if time.time() - self.last_time > 0.1:
                self.last_time = time.time()
                self.current_image += self.current_image_add
                if self.current_image >= 2:
                    self.current_image_add = -1
                if self.current_image <= 0:
                    self.current_image_add = 1
        if self.x < 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_left[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_left[self.current_image])
        elif self.x > 0:
            if self.y != 0:
                self.game.canvas.itemconfig(self.image, image=self.images_right[2])
            else:
                self.game.canvas.itemconfig(self.image, image=self.images_right[self.current_image])

    def coords(self):
        xy = list(self.game.canvas.coords(self.image))
        self.coordinates.x1 = xy[0]
        self.coordinates.y1 = xy[1]
        self.coordinates.x2 = xy[0] + 27
        self.coordinates.y2 = xy[1] + 30
        return self.coordinates
        
    def move(self):
        self.animate()
        if self.y < 0:
            self.jump_count += 1
            if self.jump_count > 20:
                self.y = 4
        if self.y > 0:
            self.jump_count -= 1
           
        co = self.coords()
        left = True
        right = False
        top = True
        bottom = True
        falling = False
        
        if self.y > 0 and co.y2 >= self.game.canvas_height:
            self.y = 0
            bottom = False
        elif self.y < 0 and co.y1 <= 0:
            self.y = 0
            top = False

        if self.x > 0 and co.x2 >= self.game.canvas_width:
            self.x = 0
            right = False
        elif self.x < 0 and co.x1 <= 0:
            self.x = 0
            left = False

        for sprite in self.game.sprites:
            if sprite == self:
                continue
            sprite_co = sprite.coords()
            if top and self.y < 0 and clscoord.collided_top(co, sprite_co):
                self.y = -self.y
                top = False
                
            if bottom and self.y > 0 and clscoord.collided_bottom(self.y, co, sprite_co):
                self.y = sprite_co.y1 - co.y2
                if self.y < 0:
                    self.y = 0
                bottom = False
                top = False

            if bottom and falling and self.y == 0 and co.y2 < self.game.canvas_height and clscoord.collided_bottom(1, co, sprite_co):
                falling = False
                
            if left and self.x < 0 and clscoord.collided_left(co, sprite_co):
                self.x = 0
                left = False

            if right and self.x > 0 and clscoord.collided_right(co, sprite_co):
                self.x = 0
                right = False
            
        if falling and bottom and self.y == 0 and co.y2 < self.game.canvas_height:
            self.y = 4
        
        self.game.canvas.move(self.image, self.x, self.y)

