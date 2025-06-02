# PyAutoGUI is a Python library for automating mouse and keyboard interactions.

import pyautogui

# 1. General Functions

# Get current mouse position (x, y)
print("Mouse position:", pyautogui.position())

# Get current screen resolution (width, height)
print("Screen size:", pyautogui.size())

# Check if a point is on the screen
print("Is (100, 100) on screen?", pyautogui.onScreen(100, 100))

# 2. Fail-Safes

# Set up a 2.5 second pause after each PyAutoGUI call
pyautogui.PAUSE = 2.5

# Enable fail-safe: move mouse to upper-left to abort
pyautogui.FAILSAFE = True

# 3. Mouse Functions

# Move mouse to (500, 500) over 1 second
pyautogui.moveTo(500, 500, duration=1)

# Move mouse relative to current position
pyautogui.moveRel(100, 0, duration=0.5)

# Drag mouse to (600, 600) over 1 second
pyautogui.dragTo(600, 600, duration=1)

# Drag mouse relative to current position
pyautogui.dragRel(0, 100, duration=0.5)

# Click at current position
pyautogui.click()

# Click at specific position with options
pyautogui.click(x=700, y=300, clicks=2, interval=0.25, button='left')

# Right, middle, double, triple click
pyautogui.rightClick()
pyautogui.middleClick()
pyautogui.doubleClick()
pyautogui.tripleClick()

# Tweening mouse movement
pyautogui.moveTo(100, 100, 2, pyautogui.easeInQuad)
pyautogui.moveTo(200, 200, 2, pyautogui.easeOutQuad)
pyautogui.moveTo(300, 300, 2, pyautogui.easeInOutQuad)
pyautogui.moveTo(400, 400, 2, pyautogui.easeInBounce)
pyautogui.moveTo(500, 500, 2, pyautogui.easeInElastic)

# Scroll vertically and horizontally
pyautogui.scroll(100)    # scroll up
pyautogui.scroll(-100)   # scroll down
pyautogui.hscroll(10)    # scroll right
pyautogui.hscroll(-10)   # scroll left

# Mouse button down and up
pyautogui.mouseDown(button='left')
pyautogui.mouseUp(button='left')

# 4. Keyboard Functions

# Type a string instantly
pyautogui.write('Hello world!')

# Type a string with delay between each character
pyautogui.write('Hello world!', interval=0.25)

# Type a list of keys
pyautogui.typewrite(['a', 'b', 'c', 'left', 'backspace', 'enter', 'f1'], interval=0.1)

# Keyboard hotkeys (e.g., Ctrl+C, Ctrl+V)
pyautogui.hotkey('ctrl', 'c')
pyautogui.hotkey('ctrl', 'v')

# Key down and up
pyautogui.keyDown('shift')
pyautogui.keyUp('shift')

# Press a key
pyautogui.press('left')
pyautogui.press('esc')
pyautogui.press('delete')

# Hold a key using context manager
with pyautogui.hold('shift'):
    pyautogui.press(['left', 'left', 'left'])

# 5. Message Box Functions

# Show an alert box
pyautogui.alert(text='This is an alert box.', title='Alert', button='OK')

# Show a confirm box
pyautogui.confirm(text='Do you want to continue?', title='Confirm', buttons=['OK', 'Cancel'])

# Show a prompt box
pyautogui.prompt(text='Enter your name:', title='Prompt', default='')

# Show a password box
pyautogui.password(text='Enter your password:', title='Password', default='', mask='*')

# 6. Screenshot Functions

# Take a screenshot and get a PIL Image object
screenshot = pyautogui.screenshot()
screenshot.save('screenshot.png')

# Take a screenshot and save directly
pyautogui.screenshot('foo.png')

# Locate an image on the screen
location = pyautogui.locateOnScreen('looksLikeThis.png')
print("Location of image:", location)

# Locate all occurrences of an image on the screen
for loc in pyautogui.locateAllOnScreen('looksLikeThis.png'):
    print("Found at:", loc)

# Get all locations as a list
locations = list(pyautogui.locateAllOnScreen('looksLikeThis.png'))
print("All locations:", locations)

# Get the center of the found image
center = pyautogui.locateCenterOnScreen('looksLikeThis.png')
print("Center of image:", center)