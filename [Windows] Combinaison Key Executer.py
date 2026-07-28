import keyboard
import time
print('Welcome to Keyboard library!')
time.sleep(1)
code = input('Enter the combinaison of keys that you want to execute!: ')
code = code.lower()
time.sleep(1)
print('Executing...',code)
time.sleep(.5)
keyboard.press_and_release(code,do_press=True,do_release=False)
time.sleep(1)
print('Done!')