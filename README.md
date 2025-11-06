# Auto-typing-script-using-pyautogui-on-Python

This script simulates realistic human typing on your computer.  
It can type from a text file directly into any active window (browser, doc, chat, etc.) with configurable typing speed, delay randomness, and typing mistakes.

## Features
1)Types text automatically like a human.
2)Works on any application that accepts keyboard input.
3)Uses random delays per character to look natural.
4)Can make random typing mistakes like a real person.
5)Can auto-correct those mistakes using backspace.
6)Allows users to change typing speed.
7)Allows users to change mistake chance.
8)Includes a countdown so you have time to switch windows before typing starts.
9)Reads content directly from a text file (content.txt).\

## Installation
1)Install dependencies:
pip install pyautogui

2)Create and put the text file 'content.txt' in the same folder where this python script has been saved.

## Usage
1) Put your text inside `content.txt`
2) Run the script
3) Enter these when asked:
- Countdown time (seconds)
- Minimum typing delay per character
- Maximum typing delay per character
- Mistake chance (0.00 to 0.20)
After the countdown → switch to the window where you want it to type  
(example: Notes, Chrome, WhatsApp Web, Word, etc.)
The script will automatically type everything from `content.txt` as if a human is typing.

## Notes
- accurateness of “human typing” depends on your delay range
- lower min/max delay → faster typing
- higher mistake chance → more realistic errors

## Disclaimer
Use this responsibly.

Do not use this script for cheating, exam writing, spamming, or any unethical purpose.  
This is for automation learning, demos, scripting productivity, etc.





