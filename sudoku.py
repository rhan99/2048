from tkinter import *
from helper import *

class Square:
  '''
  Create the 2048 squares
  '''
  def __init__(self, canvas, center, size, color):
    (x,y) = center
    x1 = x - size / 2
    x2 = x + size / 2
    y1 = y - size / 2
    y2 = y + size / 2
    self.handle = canvas.create_rectangle(x1, y1, x2, y2, fill = color, \
                                          outline = color)
    self.canvas = canvas
    self.center = center
    self.size = size
    self.color = color

  def setColor(self, color):
    self.canvas.itemconfig(self.handle, fill = color, outline = color)

class Number:
  '''
  Fill each square with a number
  '''
  def __init__(self, canvas, center, num, color):
    (x, y) = center
    self.handle = canvas.create_text(x, y, text = num, \
                                     font = ('Helvetica', '50'), fill = color)
    self.canvas = canvas
    self.num = num

  def setNum(self, num):
    if num == 0:
      num = ''
    else:
      num = str(num)
    self.canvas.itemconfig(self.handle, text = num)

  def getNum(self):
    return self.num

def updateBoard(board):
  for (r, c) in numbers:
    numbers[(r, c)].setNum(0)
    squares[(r, c)].setColor('snow')

  for (r, c) in board:
    numbers[(r, c)].setNum(board[(r, c)])
    num = board[(r, c)]
    if num == 2:
      squares[(r, c)].setColor('#B0E2FF')
    elif num == 4:
      squares[(r, c)].setColor('#63B8FF')
    elif num == 8:
      squares[(r, c)].setColor('#66CCCC')
    elif num == 16:
      squares[(r, c)].setColor('#00E5EE')
    elif num == 32:
      squares[(r, c)].setColor('#1C86EE')
    elif num == 64:
      squares[(r, c)].setColor('#436EEE')
    elif num == 128:
      squares[(r, c)].setColor('#5959AB')
    elif num == 256:
      squares[(r, c)].setColor('#838EDE')
    elif num == 512:
      squares[(r, c)].setColor('#9F79EE')
    elif num == 1024:
      squares[(r, c)].setColor('#ABA2FF')
    elif num == 2048:
      squares[(r, c)].setColor('#FFB6C1')

def key_handler(event):
  key = event.keysym
  key = str(key)
  if key in ['w', 'd', 'a', 's']:
    update(board, key)
    updateBoard(board)

def quit_game():
  root.destroy()

if __name__ == '__main__':
  root = Tk()
  root.title('Midterm Honor Roll')
  root.geometry('900x900')

  canvas = Canvas(root, background = '#f6fbfc', width = 900, height = 1000)
  canvas.pack()

  title = canvas.create_text((230, 85), text = '2048', font = ('Helvetica', 60))

  quitBtn = Button(root, text = "Quit", font = ('Helvetica', 25), \
                      command = quit_game)
  quitBtn.configure(width = 6, background = '#7da7ca', foreground = 'white',\
                       activebackground = '#7da7ca')
  quitBtn = canvas.create_window(650, 85, window = quitBtn)

  squares = {}
  sColor = 'snow'
  for r in range(4):
    for c in range(4):
      squares[(r, c)] = Square(canvas, (175 + (c * 170), 250 + (r * 170) ), 145, sColor)

  numbers = {}
  nColor = 'black'
  for r in range(4):
    for c in range(4):
      numbers[(r, c)] = Number(canvas, (175 + (c * 170), 250 + (r * 170) ), '', nColor)

  lcolor = 'black'
  for l in range(5):
    i = 170 * l
    canvas.create_line(77.5, 165 + i, 782.5, 165 + i, fill = lcolor, width = 25)
    canvas.create_line(90 + i, 155, 90 + i, 855, fill = lcolor, width = 25)

  board = make_board()
  updateBoard(board)

  root.bind('<Key>', key_handler)
  root.mainloop()


