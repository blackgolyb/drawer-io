from dataclasses import dataclass
import numpy as np
import keyboard

import pyautogui
import time


@dataclass
class Canvas(object):
    size: list[int, int]
    padding: list[int, int]


colors_coords = np.array([
    [333, 425],
    [378, 425],
    [423, 425],
    
    [333, 475],
    [378, 475],
    [423, 475],
    
    [333, 525],
    [378, 525],
    [423, 525],
    
    [333, 575],
    [378, 575],
    [423, 575],
    
    [333, 625],
    [378, 625],
    [423, 625],
    
    [333, 675],
    [378, 675],
    [423, 675],
])

colors = np.array([
    [0, 0, 0],
    [102, 102, 102],
    [0, 80, 205],
    
    [255, 255, 255],
    [170, 170, 170],
    [38, 201, 255],
    
    [1, 116, 32],
    [153, 0, 0],
    [150, 65, 18],
    
    [17, 176, 60],
    [255, 0, 19],
    [255, 120, 41],
    
    [176, 112, 28],
    [153, 0, 78],
    [203, 90, 87],
    
    [255, 193, 38],
    [255, 0, 143],
    [254, 175, 168],
])

def is_break():
    """Need root in linux"""
    return keyboard.is_pressed('q')

class Drawer(object):
    def __init__(self, canvas):
        self.canvas = canvas
        self.prev_color = []
        
    def select_color(self, target_color):
        if np.array_equal(self.prev_color, target_color):
            return
        
        self.prev_color = target_color
            
        for i in range(len(colors)):
            if not np.array_equal(colors[i], target_color):
                continue
            
            pyautogui.click(colors_coords[i][0], colors_coords[i][1])
            return
        
    def draw_rect(self, rect):
        self.select_color(rect.color)
        pyautogui.moveTo(
            self.canvas.padding[0]+rect.start[0],
            self.canvas.padding[1]+rect.start[1],
        )
        pyautogui.dragTo(
            self.canvas.padding[0]+rect.end[0],
            self.canvas.padding[1]+rect.end[1],
        )
        
    def draw_pixel(self, pixel):
        self.select_color(pixel.color)
        pyautogui.moveTo(
            self.canvas.padding[0]+pixel.x,
            self.canvas.padding[1]+pixel.y,
        )
        pyautogui.dragTo(
            self.canvas.padding[0]+pixel.x+1,
            self.canvas.padding[1]+pixel.y+1,
        )
        
    def draw(self, figures):
        self.prev_color = []
        
        for rect in figures.rects:
            if is_break(): break
            self.draw_rect(rect)
            
        # for pixel in figures.pixels[:10]:
        for pixel in figures.pixels[:10]:
            if is_break(): break
            self.draw_pixel(pixel)