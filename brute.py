import pyautogui
import time
import string
import random
import keyboard

errorImage = 'error.png'

letters = string.ascii_uppercase
digits = string.digits

maxLetters = 4
maxNumbers = 2

num_codes = 500

combinations = []

for _ in range(num_codes):
    numberOfLetters = random.randint(0, maxLetters)
    numberOfNumbers = random.randint(0, maxNumbers)
    
    letterComb = ''.join(random.choices(letters, k=numberOfLetters))
    numberComb = ''.join(random.choices(digits, k=numberOfLetters))
    
    code = letterComb + numberComb
    code += ''.join(random.choices(letters, k=4 - len(code))) 
    combinations.append(code[:4])

random.shuffle(combinations)

print("Switch to GeoGussr in the next 5 seconds")
time.sleep(5)

for code in combinations:
    for letter in code:
        pyautogui.typewrite(letter)

    pyautogui.typewrite(code)

    for i in range(4):
        pyautogui.press('backspace')

    if keyboard.is_pressed('shift'):
        print("Script terminated")
        break

    try:
        if pyautogui.locateOnScreen(errorImage, confidence=0.8):
            print("Invalid code")
            pyautogui.hotkey('alt', 'left')
            time.sleep(0.5)
    except pyautogui.ImageNotFoundException:
        print("Code Not Found")

print("Finished script")
