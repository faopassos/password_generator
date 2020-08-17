#!/bin/python3

import os
import random
import PySimpleGUI as sg
# from playsound import playsound


class PassGen:
  def __init__(self):
    # Layout
    char_list = list(range(30))

    sg.theme('Black')
    # playsound('music.mp3')
    layout = [
      [sg.Text('Site/Software', size=(11, 1)),
      sg.Input(key='site', size=(20, 1))],
      [sg.Text('email/user', size=(11, 1)),
      sg.Input(key='user', size=(20, 1))],
      [sg.Text('Number of character'), sg.Combo(values=char_list,
        key='total_chars', default_value=8, size=(3, 1))],
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
        self.save_password(new_password, values)

  def generate_pass(self, values):
    char_list = 'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz1234567890!@#$%&*'
    chars = random.choices(char_list, k=(values['total_chars']))
    new_pass = ''.join(chars)
    return new_pass

  def save_password(self, new_password, values):
    with open('passwords.txt', 'a', newline='') as file:
      file.write(
        f"site: {values['site']}, user: {values['user']}, new password: {new_password}\n")

    print('File saved')

gen = PassGen()

if __name__ == '__main__':
  gen.Start()
