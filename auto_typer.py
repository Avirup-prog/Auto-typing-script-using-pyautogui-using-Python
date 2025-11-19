import time
import random
import pyautogui

def human_type(text, min_speed=0.03, max_speed=0.15, mistake_chance=0.05):
    for char in text:
        time.sleep(random.uniform(min_speed, max_speed))
        if random.random() < mistake_chance and char.isalpha():
            wrong_char = random.choice("abcdefghijklmnopqrstuvwxyz")
            pyautogui.typewrite(wrong_char)
            time.sleep(random.uniform(0.05, 0.25))
            pyautogui.press('backspace')
            time.sleep(random.uniform(0.05, 0.2))
        pyautogui.typewrite(char)

def countdown(seconds=3):
    print("Typing will start in:")
    for i in range(seconds, 0, -1):
        print(i)
        time.sleep(1)
    print("Switch to your target window now!\n")
    time.sleep(0.5)

file_path = "content.txt"  #Text file for the contents to be typed

try:
    with open(file_path, "r", encoding="utf-8") as f:
        content = f.read()
except FileNotFoundError:
    print(f"Error: '{file_path}' not found.")
    exit()
#Settings
countdown_time = int(input("Enter countdown time (seconds): "))
min_speed = float(input("Enter min typing delay (e.g. 0.03): "))
max_speed = float(input("Enter max typing delay (e.g. 0.15): "))
mistake_rate = float(input("Enter mistake chance (0.0 to 0.2): "))

countdown(countdown_time)
human_type(content, min_speed, max_speed, mistake_rate)
