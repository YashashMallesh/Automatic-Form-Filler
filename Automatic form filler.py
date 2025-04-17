#! python3
# Automatic form filler

import pyautogui
import time

# Give yourself time to switch to the form window
print("You have 5 seconds to switch to the form window...")
time.sleep(5)

form_data = [
    {'name': 'Yashash Gowda', 'fear': 'Spiders', 'source': 'wand', 'robocop': 4, 'comments': 'No comment.'},
    {'name': 'Alice Smith', 'fear': 'Heights', 'source': 'amulet', 'robocop': 3, 'comments': 'Please be nice.'},
    {'name': 'Bob Johnson', 'fear': 'Clowns', 'source': 'crystal ball', 'robocop': 5, 'comments': 'No clowns please!'},
]

for person in form_data:
    print(f"Filling form for: {person['name']}")
    
    # Name field
    pyautogui.write(person['name'], interval=0.1)
    pyautogui.press('tab')

    # Fear field
    pyautogui.write(person['fear'], interval=0.1)
    pyautogui.press('tab')

    # Source dropdown (use arrow keys to select option)
    if person['source'] == 'wand':
        pyautogui.press(['down'])
    elif person['source'] == 'amulet':
        pyautogui.press(['down', 'down'])
    elif person['source'] == 'crystal ball':
        pyautogui.press(['down', 'down', 'down'])
    pyautogui.press('tab')

    # Robocop rating (1–5): tab over and use right arrows
    for i in range(1, person['robocop']):
        pyautogui.press('right')
    pyautogui.press('tab')

    # Comments
    pyautogui.write(person['comments'], interval=0.1)
    pyautogui.press('tab')

    # Submit
    pyautogui.press('enter')

    # Wait for the form to reload
    time.sleep(2)

    # Go to the next form
    pyautogui.press('tab')
    pyautogui.press('enter')
    time.sleep(2)

print("Done filling all forms!")
