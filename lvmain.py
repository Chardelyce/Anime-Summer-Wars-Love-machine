import pygame
import string
import sys
import getpass

# Initialize Pygame
pygame.init()

# Constants
WINDOW_WIDTH = 800
WINDOW_HEIGHT = 600
WHITE = (255, 255, 255)
GRAY = (200, 200, 200)
FONT = pygame.font.Font(None, 36)
SMALL_FONT = pygame.font.Font(None, 25)
INPUT_FONT = pygame.font.Font(None, 48)
NUMBERS_FONT = pygame.font.Font(None, 28)
GRAY_RECT_HEIGHT = 420
GRAY_RECT_WIDTH = 760

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

def render_paragraph(surface, font, text, x, y, width, line_height):
    lines = []
    current_line = []
    current_line_width = 0
    words = text.split(" ")
    
    for word in words:
        word_width, _ = font.size(word)
        if current_line_width + word_width <= width:
            current_line.append(word)
            current_line_width += word_width + font.size(" ")[0]
        else:
            lines.append(" ".join(current_line))
            current_line = [word]
            current_line_width = word_width + font.size(" ")[0]

    if current_line:
        lines.append(" ".join(current_line))
    
    for line in lines:
        text_surface = font.render(line, True, (0, 0, 0))
        surface.blit(text_surface, (x, y))
        y += line_height

def main():
    # Get the computer's username
    username = getpass.getuser()

    message = "The magic words are squeamish ossifrage to know is to know that you know nothing That is the true meaning of knowledge"
    encrypted_message = encrypt_message(message)

    # Initialize Pygame window
    screen = pygame.display.set_mode((WINDOW_WIDTH, WINDOW_HEIGHT))
    pygame.display.set_caption("Love Machine Puzzle")

    input_text = ""
    solved = False
    show_reply_screen = False
    reply_input_text = ""  # Initialize the reply input text

    while not solved:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_RETURN:
                    if input_text == encrypted_message:
                        solved = True
                    else:
                        input_text = ""
                elif event.key == pygame.K_BACKSPACE:
                    input_text = input_text[:-1]
                else:
                    input_text += event.unicode

        screen.fill(WHITE)

        # Gmail message design
        pygame.draw.rect(screen, (255, 255, 255), (20, 20, 760, 80))
        pygame.draw.rect(screen, (240, 240, 240), (20, 100, 760, GRAY_RECT_HEIGHT))
        pygame.draw.line(screen, (200, 200, 200), (20, 100), (780, 100), 2)

        # Light gray lines under "To," "From," and "Subject" lines with reduced space
        pygame.draw.line(screen, GRAY, (30, 65), (300, 65), 2)  # Under "To" line
        pygame.draw.line(screen, GRAY, (30, 95), (300, 95), 2)  # Under "From" line
        pygame.draw.line(screen, GRAY, (20, 40), (300, 40), 2)  # Under "Subject" line

        # Email-like interface
        to_line = SMALL_FONT.render(f"To: {username}", True, GRAY)
        screen.blit(to_line, (30, 20))
        from_line = SMALL_FONT.render("From: Wonderful World of OZ", True, GRAY)
        screen.blit(from_line, (30, 50))
        subject_line = SMALL_FONT.render("Subject: Solve me", True, GRAY)
        screen.blit(subject_line, (30, 80))

        # Display numbers in a neat paragraph within the gray rectangle
        render_paragraph(screen, NUMBERS_FONT, encrypted_message, 30, 140, GRAY_RECT_WIDTH, NUMBERS_FONT.size(" ")[1])

        input_surface = INPUT_FONT.render(input_text, True, (0, 0, 0))
        screen.blit(input_surface, (30, 520))

        # Add a "Reply" button
        reply_button = SMALL_FONT.render("Reply", True, (0, 0, 0))
        reply_button_rect = reply_button.get_rect()
        reply_button_rect.center = (WINDOW_WIDTH // 2, 570)
        screen.blit(reply_button, reply_button_rect)

        # Check if the "Reply" button is clicked
        mouse_x, mouse_y = pygame.mouse.get_pos()
        if reply_button_rect.collidepoint(mouse_x, mouse_y):
            pygame.draw.rect(screen, (200, 200, 200), reply_button_rect, 1)
            if pygame.mouse.get_pressed()[0]:  # Left mouse button clicked
                show_reply_screen = True

        pygame.display.flip()

        # Show the reply screen if the flag is set
        if show_reply_screen:
            reply_input_text = ""  # Clear the reply input text when entering the reply screen
            reply_screen_active = True

            while reply_screen_active:
                for event in pygame.event.get():
                    if event.type == pygame.QUIT:
                        pygame.quit()
                        sys.exit()
                    elif event.type == pygame.KEYDOWN:
                        if event.key == pygame.K_RETURN:
                            # Check if the user's reply on the reply screen matches the expected message
                            if reply_input_text.lower() == message.lower():
                                solved = True
                            else:
                                reply_input_text = ""
                        elif event.key == pygame.K_BACKSPACE:
                            reply_input_text = reply_input_text[:-1]
                        elif event.unicode.isalpha():  # Check if input is a letter
                            reply_input_text += event.unicode

                screen.fill(WHITE)

                # Gmail-like reply screen design
                pygame.draw.rect(screen, (240, 240, 240), (20, 100, 760, GRAY_RECT_HEIGHT))

                # To: Wonderful World of OZ
                to_line_reply = SMALL_FONT.render("To: Wonderful World of OZ", True, GRAY)
                screen.blit(to_line_reply, (30, 20))
                # From: User's Name
                from_line_reply = SMALL_FONT.render(f"From: {username}", True, GRAY)
                screen.blit(from_line_reply, (30, 50))
                # Subject: Re solve me
                subject_line_reply = SMALL_FONT.render("Subject: Re: Solve me", True, GRAY)
                screen.blit(subject_line_reply, (30, 80))

                # Create an input field for the user's reply
                reply_input_rect = pygame.Rect(30, 150, GRAY_RECT_WIDTH - 60, 40)
                pygame.draw.rect(screen, (255, 255, 255), reply_input_rect)

                # Display the user's reply in the input field
                reply_input_surface = INPUT_FONT.render(reply_input_text, True, (0, 0, 0))
                screen.blit(reply_input_surface, (reply_input_rect.x + 10, reply_input_rect.y + 10))

                pygame.display.flip()

            show_reply_screen = False  # Reset the flag when leaving the reply screen

    # Puzzle solved
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
