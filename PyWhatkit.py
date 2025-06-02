# PyWhatkit is a versatile Python library designed for automating WhatsApp messaging and other tasks.
import pywhatkit

#1. WhatsApp Automation:

# Send a WhatsApp Message to a Contact at 1:30 PM
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30)

# Same as above but Closes the Tab in 2 Seconds after Sending the Message
pywhatkit.sendwhatmsg("+910123456789", "Hi", 13, 30, 15, True, 2)

# Send a WhatsApp Message to a Group at 12:00 AM
pywhatkit.sendwhatmsg_to_group("AB123CDEFGHijklmn", "Hey All!", 0, 0)

# Send a WhatsApp Message to a Group instantly
pywhatkit.sendwhatmsg_to_group_instantly("AB123CDEFGHijklmn", "Hey All!")
    
# Send an Image to a Group with the Caption as Hello
pywhatkit.sendwhats_image("AB123CDEFGHijklmn", "Images/Hello.png", "Hello")

# Send an Image to a Contact with the no Caption
pywhatkit.sendwhats_image("+910123456789", "Images/Hello.png")
    
#2. YouTube Interaction:
   
# Play a YouTube Video on a Specific Topic
pywhatkit.playonyt("Python tutorials")

#3. text to Handwriting Conversion:

# Convert the given text to a handwriting-style image and save it as 'handwriting.png'
pywhatkit.text_to_handwriting("Hello, this is a handwriting style example!", save_to="handwriting.png",rgb=(0, 0, 255))  # Blue color text

#4. ASCII Art

# Convert a text string to ASCII art and save it as 'ascii_art.txt'
pywhatkit.text_to_ascii_art("Python", "ascii_art.txt")

#5. google Search:

# Perform a Google search for the term "Python programming"
pywhatkit.search("Python programming")

# Get a short summary about a topic (returns a string)
summary = pywhatkit.info("Python programming", lines=2, return_value=True)
print(summary)

# Show the history of all searches and actions performed by pywhatkit
pywhatkit.show_history()

# Take a screenshot after a delay and save it as 'my_screenshot.png'
pywhatkit.take_screenshot(file_name="my_screenshot.png", delay=3)

# Open the default web browser and return True if successful
success = pywhatkit.open_web()
print("Web browser opened:", success)

#6. email Automation:

# Example: Send a plain text email (requires valid credentials and may need app password for Gmail)
# pywhatkit.send_mail(
#     "your_email@gmail.com",           # Sender's email
#     "your_password",                  # Sender's email password or app password
#     "Greetings",                      # Subject
#     "Hello, this is a test email!",   # Message
#     "receiver_email@gmail.com"        # Receiver's email
# )

# Example: Send an HTML email
# pywhatkit.send_hmail(
#     "your_email@gmail.com",           # Sender's email
#     "your_password",                  # Sender's email password or app password
#     "HTML Greetings",                 # Subject
#     "<h1>Hello!</h1><p>This is an <b>HTML</b> email.</p>",  # HTML code
#     "receiver_email@gmail.com"        # Receiver's email
# )
