#!/bin/python3

import random
import PySimpleGUI as sg
from vlc import MediaPlayer


class PassGen:
  def __init__(self):
    # Music
    music = MediaPlayer('music.mp3')
    music.play()
    # Layout
    sg.theme('DarkBrown')
    char_list = list(range(30))
    layout = [
      [sg.Text('Number of character'), sg.Combo(values=char_list,
        key='total_chars', default_value=8, size=(3, 1))],
      [sg.Text('Default: Upper, Lower, Numbers and Symbols')],
      [sg.Checkbox('Exclude symbols', key='no_symbols'),
        sg.Checkbox('Exclude numbers', key='no_numbers')],  
      [sg.Output(size=(32, 5))],
      [sg.Button('Generate')]
    ]
    # declarate window
    self.window = sg.Window('Password Generator', layout)

  def Start(self):
    while True:
      event, values = self.window.read()
      
      if event == sg.WINDOW_CLOSED:
        break
      if event == 'Generate':
        new_password = self.generate_pass(values)
        print(new_password)

  def generate_pass(self, values):
    no_symbols = values['no_symbols']
    no_numbers = values['no_numbers']

    if no_symbols == False and no_numbers == False:
      char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*'
    elif no_symbols == True and no_numbers == False:
      char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890'
    elif no_symbols == False and no_numbers == True:
      char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz!@#$%&*'
    else:
      char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz'

    chars = random.choices(char_list, k=(values['total_chars']))
    new_pass = ''.join(chars)

    return new_pass

gen = PassGen()

if __name__ == '__main__':
  gen.Start()
