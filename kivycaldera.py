import kivy
kivy.require('1.8.0')

from kivy.app import App
from kivy.core.window import Window
from kivy.uix.anchorlayout import AnchorLayout
from kivy.uix.widget import Widget
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput

from kivy.graphics import Color, Rectangle

from caldera import board, fill_board

fill_board()


class CalderaBlockWidget(Widget):
    color = '_'
    col = 0
    row = 0
    box_size = 0
    pos = (0, 0)
    def __init__(self, col, row, color, **kwargs):
        super(CalderaBlockWidget, self).__init__(**kwargs)
        self.col = col;
        self.row = row;
        self.color = color
        self.size = Window.size
        self.box_size = min(self.size[0], self.size[1])/5
        self.set_pos()
        self.draw_me()

    def draw_me(self):
      with self.canvas:
        self.my_color()
        Rectangle(pos = self.pos, size=(self.box_size,self.box_size))

    def my_color(self):
      if self.color == 'B':
        Color(0,0,1)
      elif self.color == 'G':
        Color(0,1,0)
      elif self.color == 'R':
        Color(1,0,0)
      elif self.color == 'Y':
        Color(1,1,0)
      else:
        Color(0,0,0)

    def set_pos(self):
      offseth = self.height/2 - 2.5 * self.box_size;
      offsetw = self.width/2 - 2.5 * self.box_size;
      self.pos = (offsetw+ self.col * self.box_size,
                  offseth + self.row * self.box_size)


class CalderaWidget(Widget):
    boardwidgets = []
    def __init__(self, **kwargs):
        super(CalderaWidget, self).__init__(**kwargs)
        for row in range(5):
          for col in range(5):
            self.add_widget(CalderaBlockWidget(col, row, board(col, row)))

class MyApp(App):
    def build(self):
        l = AnchorLayout(anchor_x='center', anchor_y='center')
        l.size = Window.size
        w = CalderaWidget()
        l.add_widget(w)
        #import pdb; pdb.set_trace();
        return l

if __name__ == '__main__':
  MyApp().run()
