import traceback
import random

pieces = {'Y': 6, 'B': 6, 'G': 6, "R": 6}
board_state = [['_'] * 5, ['_'] * 5, ['_'] * 5, ['_'] * 5, ['_'] * 5]

def reset_board():
  global board_state
  global pieces
  pieces = {'Y': 6, 'B': 6, 'G': 6, "R": 6}
  board_state = [['_'] * 5, ['_'] * 5, ['_'] * 5, ['_'] * 5, ['_'] * 5]
  #print_board()

def iterate_board():
  for row in range(5):
    for col in range(5):
      if col == 2 and row == 2:
        continue

def board(col, row):
  if col >= 0 and col < 5 and row >= 0 and row < 5:
    return board_state[col][row]
  return '_'

def add_piece(col, row, color):
  board_state[col][row] = color

def neighbors(col, row):
  return [c for c in [board(col - 1, row),
                      board(col, row - 1),
                      board(col + 1, row),
                      board(col, row + 1)] if c != '_']

def valid_pieces(col, row):
  n = neighbors(col, row)
  valid_colors = set(pieces.keys()) - set(n)
  return [c for c in valid_colors if pieces[c] != 0]

def random_valid_piece(col, row):
  try:
    return random.choice([
      thing
      for p in valid_pieces(col, row)
      for thing in p * pieces[p]
    ])
  except:
    return None

def fill_board():
  tries = 0
  while tries < 1000:
    tries = tries + 1
    try:
      for row in range(5):
        for col in range(5):
          if col == 2 and row == 2:
            continue
          # set to random piece.
          piece = random_valid_piece(col, row)
          if piece is None:
            raise Exception('')
          pieces[piece] = pieces[piece] - 1
          board_state[col][row] = piece
      break
    except Exception:
      reset_board()
      continue
  print "Tries: %s" % tries

def print_board():
  print pieces
  for row in range(5):
    for col in range(5):
      if col == 2 and row == 2:
        print ' ',
      else:
        print board_state[col][row],
    print ''

if __name__ == '__main__':
  print "Hi"
  fill_board()
  print_board()
