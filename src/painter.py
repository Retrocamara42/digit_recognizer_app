# Class for making drawings on a virtual whiteboard
# Based on https://gist.github.com/nikhilkumarsingh/85501ee2c3d8c0cfa9d1a27be5781f06

from tkinter import *
from PIL import Image, ImageDraw
import classifier

class Paint(object):

    def __init__(self):
        self.root = Tk()

        self.width = 200
        self.height = 200
        self.background = (255,255,255)

        self.guess_button = Button(self.root, text='Guess', command=self.guess)
        self.guess_button.grid(row=0, column=0)

        self.clear_button = Button(self.root, text='Clear', command=self.clear_board)
        self.clear_button.grid(row=0, column=1)

        self.canvas = Canvas(self.root, bg="white", width=self.width, height=self.height)
        self.canvas.grid(row=1, columnspan=5)

        self.image = Image.new("RGB", (self.width, self.height), self.background)
        self.draw = ImageDraw.Draw(self.image)

        self.clf = classifier.DigitRecognizer()
        self.clf.load_model()

        self.setup()
        self.root.mainloop()

    def setup(self):
        self.old_x = None
        self.old_y = None
        self.color = '#000000'
        self.canvas.bind('<B1-Motion>', self.paint)
        self.canvas.bind('<ButtonRelease-1>', self.reset)

    def paint(self, event):
        if self.old_x and self.old_y:
            self.canvas.create_line(self.old_x, self.old_y, event.x, event.y, width=3, fill=self.color, capstyle=ROUND, smooth=TRUE, splinesteps=48)
            self.draw.line((self.old_x, self.old_y, event.x, event.y), width=3, fill=self.color)

        self.old_x = event.x
        self.old_y = event.y

    def guess(self):
        self.saving_image()
        self.clf.predicting()

    def clear_board(self):
        self.canvas.delete("all")
        self.image = None
        self.image = Image.new("RGB", (self.width, self.height), self.background)
        self.draw = ImageDraw.Draw(self.image)
        self.saving_image()

    def saving_image(self):
        self.image.save('input/number.jpg')
        try:
            im = Image.open('input/number.jpg')
            im.thumbnail((28,28), Image.ANTIALIAS)
            im.save('input/input.jpg', "JPEG")
        except IOError:
            print("Error ocurred while saving, please try again")

    def reset(self, event):
        self.old_x, self.old_y = None, None
