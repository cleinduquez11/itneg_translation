import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Translation Application")

# Load background image
background_image = pygame.image.load('background.jpg')  # Ensure this is the path to your image

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (76, 175, 80)
BLUE = (0, 140, 186)
RED = (244, 67, 54)
TAN = (210, 180, 140)

# Fonts
font = pygame.font.Font(None, 40)
label_font = pygame.font.Font(None, 30)

# Text input class
class TextInput:
    def __init__(self, x, y, w, h, font, label, text=''):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = BLACK
        self.text = text
        self.label = label_font.render(label, True, BLACK)
        self.txt_surface = font.render(text, True, self.color)
        self.active = False

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box rect
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = GREEN if self.active else BLACK
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    print(self.text)
                    # self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text, True, self.color)

    def draw(self, win):
        win.blit(self.label, (self.rect.x, self.rect.y - 30))
        win.blit(self.txt_surface, (self.rect.x + 5, self.rect.y + 5))
        pygame.draw.rect(win, self.color, self.rect, 2)

# Button class
class Button:
    def __init__(self, x, y, w, h, text, color, font, action=None):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = color
        self.text = text
        self.font = font
        self.txt_surface = font.render(text, True, WHITE)
        self.action = action

    def draw(self, win):
        pygame.draw.rect(win, self.color, self.rect)
        win.blit(self.txt_surface, (self.rect.x + (self.rect.width - self.txt_surface.get_width()) // 2, self.rect.y + (self.rect.height - self.txt_surface.get_height()) // 2))

    def is_clicked(self, pos):
        return self.rect.collidepoint(pos)

# Create UI elements
search_entry = TextInput(WIDTH // 2 - 150, HEIGHT // 2 - 100, 300, 50, font, 'Enter Itneg word:')
itneg_entry = TextInput(WIDTH // 2 - 150, HEIGHT // 2 - 30, 300, 50, font, 'Itneg word:')
english_entry = TextInput(WIDTH // 2 - 150, HEIGHT // 2 + 40, 300, 50, font, 'English translation:')
tagalog_entry = TextInput(WIDTH // 2 - 150, HEIGHT // 2 + 110, 300, 50, font, 'Tagalog translation:')

user_button = Button(WIDTH // 2 - 100, HEIGHT // 2 - 50, 200, 50, 'User', GREEN, font)
admin_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 50, 200, 50, 'Admin', BLUE, font)

add_button = Button(WIDTH // 2 - 100, HEIGHT // 2 + 180, 100, 50, 'Add', GREEN, font)
delete_button = Button(WIDTH // 2, HEIGHT // 2 + 180, 100, 50, 'Delete', RED, font)
update_button = Button(WIDTH // 2 + 100, HEIGHT // 2 + 180, 100, 50, 'Update', BLUE, font)

def main():
    clock = pygame.time.Clock()
    mode = 'menu'

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()

            if mode == 'menu':
                if event.type == pygame.MOUSEBUTTONDOWN:
                    if user_button.is_clicked(event.pos):
                        mode = 'user'
                    elif admin_button.is_clicked(event.pos):
                        mode = 'admin'

            # if mode == 'user' or mode == 'admin':
            #     search_entry.handle_event(event)

            if mode == 'user':
                search_entry.handle_event(event)
                
            if mode == 'admin':
                itneg_entry.handle_event(event)
                english_entry.handle_event(event)
                tagalog_entry.handle_event(event)

        win.blit(background_image, (0, 0))

        if mode == 'menu':
            user_button.draw(win)
            admin_button.draw(win)
        elif mode == 'user':
            search_entry.draw(win)
        elif mode == 'admin':
            # search_entry.draw(win)
            itneg_entry.draw(win)
            english_entry.draw(win)
            tagalog_entry.draw(win)
            add_button.draw(win)
            delete_button.draw(win)
            update_button.draw(win)

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
