import string
import getpass

def alphabet_mapping(letter):
    letter = letter.lower()
    if letter in string.ascii_lowercase:
        position = ord(letter) - ord('a') + 1
        result = position ** 3
        return result
    else:
        return None

def encrypt_message(message):
    encrypted_message = []
    for char in message:
        if char.isalpha():
            char_value = ord(char.lower()) - ord('a') + 1
            cubed_result = char_value ** 3
            encrypted_message.append(str(cubed_result))
        else:
            encrypted_message.append(char)
    return " ".join(encrypted_message)

def render_paragraph(text):
    lines = text.split('\n')
    for line in lines:
        print(line)

def main():
    # Get the computer's username
    username = getpass.getuser()

    message = "The magic words are squeamish ossifrage to know is to know that you know nothing That is the true meaning of knowledge"
    encrypted_message = encrypt_message(message)

    # Display the welcome message
    print("Welcome to the World of Oz")

    input_text = ""
    solved = False
    show_reply_screen = False
    reply_input_text = ""  # Initialize the reply input text

    while not solved:
        print(f"To: {username}")
        print(f"From: Wonderful World of OZ")
        print("Subject: Solve me")
        render_paragraph(encrypted_message)

        user_input = input("Your reply: ")

        if user_input == encrypted_message:
            solved = True

    print("Puzzle solved!")

if __name__ == "__main__":
    main()
