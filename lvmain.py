import getpass
import os
import time

# Custom ASCII art for the lock
lock_art = """
@@@@@@#GP55YYY55PG#@@@@@@
@@@&G5YYY5PPPP55YYY5G&@@@
@@GYYYPGBGPPPPGGBGPYYYG@@
@PYY5BB5YYYYYYYYYPBB5YYP@
GYY5&GYYYYYYYYYYYYYG&5YYG
5YYB#YYYYYYYYYYYYYYY&GYY5
5YY#BYYYYYYYYYYYYYYY#BYY5
GYYP&PYYYYYYYYY5B&PYYP@
@PYYP&G5YYYYYYYYY5B&PYYP@
@@B5Y5G#BGPPPPPGB#GYY5B@@
@@@&G5YY5PGGGGGP5YY5G&@@@
@@@@@#YYYYYYYYYYYYY#@@@@@
@@@@@GYYPBBBBBGBB5YG@@@@@
@@@@@5YY555555G&GYY5@@@@@
@@@@#YYYYYYYYB#5YYYY#@@@@
@@@@GYYYYYYP#GYYYYYYG@@@@
@@@@5YYYYYB#5YYYYYYY5@@@@
@@@#YYYY5#GYYYYYYYYYY#@@@
@@@GYYYB&G5PPPPPPPP5YG@@@
@@@5YY5GGGGGGGGGGGG5Y5@@@
@@&YYYYYYYYYYYYYYYYYYY&@@
"""

# Define the encrypt_message function here
def encrypt_message(message):
    encrypted_message = []
    cubed_sequence = []

    for char in message:
        if char.isalpha():
            char_value = ord(char.lower()) - ord('a') + 1
            cubed_result = char_value ** 3
            encrypted_message.append(str(cubed_result))
            cubed_sequence.append(str(cubed_result))
        else:
            encrypted_message.append(char)  # Preserve spaces and other characters

    return " ".join(encrypted_message), cubed_sequence

# Define the render_paragraph function here
def render_paragraph(text):
    lines = text.split('\n')
    for line in lines:
        print(line)

def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')

def main():
    # Get the computer's username
    username = getpass.getuser()

    message = "The magic words are squeamish ossifrage to know is to know that you know nothing That is the true meaning of knowledge"
    encrypted_message, cubed_sequence = encrypt_message(message)

    # Calculate the number of spaces to center the text
    terminal_width = os.get_terminal_size().columns
    padding = (terminal_width - len("Welcome to the World of Oz")) // 2

    # Display the welcome message centered
    print(" " * padding  * padding + lock_art)

    # Display the cubed sequence under the welcome message
    render_paragraph(" ".join(cubed_sequence))

    input_text = ""
    solved = False

    while not solved:
        print(f"To: {username}")
        print(f"From: Wonderful World of OZ")
        print("Subject: Solve me")

        user_input = input("Your reply: ")

        # Remove spaces and convert to lowercase for comparison
        user_input_cleaned = user_input.replace(" ", "").lower()
        original_message_cleaned = "".join(message.split()).replace(" ", "").lower()

        if user_input_cleaned == original_message_cleaned:
            solved = True
            break  # Exit the loop when the correct solution is entered

    # Display the lock ASCII art under the welcome message
    print(lock_art)

    # Display a loading bar
    for _ in range(terminal_width):
        print("-", end='', flush=True)
        time.sleep(0.05)  # Add a small delay to create the loading effect

    # Clear the screen
    clear_screen()

if __name__ == "__main__":
    main()
