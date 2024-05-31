import pygame
import sys

# Initialize Pygame
pygame.init()

# Set up display
WIDTH, HEIGHT = 800, 600
win = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Itneg to Tagalog/English Translation")

# Load background image
background_image = pygame.image.load('background.jpg')  # Ensure this is the path to your image

# Colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (76, 175, 80)
BLUE = (0, 140, 186)
RED = (244, 67, 54)
TAN = (210, 180, 140)
GRAY = (200, 200, 200)
# Fonts
font = pygame.font.Font(None, 40)
label_font = pygame.font.Font(None, 30)



# Admin Credentials
user_name = 'admin'
pass_word = 'admin'


# Text input class
class TextInput:
    def __init__(self, x, y, w, h, font, label, text='', obscure = False):
        self.rect = pygame.Rect(x, y, w, h)
        self.color = WHITE
        self.text = text
        self.label = label_font.render(label, True, WHITE)
        self.txt_surface = font.render(text, True, self.color)
        self.active = False
        self.obscure = obscure

    def handle_event(self, event):
        if event.type == pygame.MOUSEBUTTONDOWN:
            # If the user clicked on the input box rect
            if self.rect.collidepoint(event.pos):
                self.active = not self.active
            else:
                self.active = False
            self.color = GREEN if self.active else WHITE
        if event.type == pygame.KEYDOWN:
            if self.active:
                if event.key == pygame.K_RETURN:
                    self.text = ''
                elif event.key == pygame.K_BACKSPACE:
                    self.text = self.text[:-1]
                else:
                    self.text += event.unicode
                self.txt_surface = font.render(self.text if not self.obscure else '*' * len(self.text), True, WHITE)

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
        # print(pos)
        return self.rect.collidepoint(pos)

# Padding and positions
PADDING = 50
ELEMENT_WIDTH = 300
ELEMENT_HEIGHT = 50

def get_centered_positions(n_elements):
    total_height = n_elements * ELEMENT_HEIGHT + (n_elements - 1) * PADDING
    start_y = (HEIGHT - total_height) // 2
    positions = [(WIDTH // 2 - ELEMENT_WIDTH // 2, start_y + i * (ELEMENT_HEIGHT + PADDING)) for i in range(n_elements)]
    return positions




def millis_delay(start_time, delay):
    current_time = pygame.time.get_ticks()
    return current_time - start_time >= delay


# Create UI elements with centered positions
positions_menu = get_centered_positions(2)
user_button = Button(positions_menu[0][0], positions_menu[0][1], 200, 50, 'User', GREEN, font)
admin_button = Button(positions_menu[1][0], positions_menu[1][1], 200, 50, 'Admin', BLUE, font)

positions_user = get_centered_positions(1)
search_entry = TextInput(positions_user[0][0], positions_user[0][0], ELEMENT_WIDTH, ELEMENT_HEIGHT, font, 'Enter Itneg word:')

positions_admin = get_centered_positions(5)
search_entry_admin = TextInput(positions_admin[0][0], positions_admin[0][0], ELEMENT_WIDTH, ELEMENT_HEIGHT, font, 'Enter Itneg word:')
itneg_entry = TextInput(positions_admin[1][0], positions_admin[1][1], ELEMENT_WIDTH, ELEMENT_HEIGHT, font, 'Itneg word:')
english_entry = TextInput(positions_admin[2][0], positions_admin[2][1], ELEMENT_WIDTH, ELEMENT_HEIGHT, font, 'English translation:')
tagalog_entry = TextInput(positions_admin[3][0], positions_admin[3][1], ELEMENT_WIDTH, ELEMENT_HEIGHT, font, 'Tagalog translation:')

add_button = Button(WIDTH // 2 - 150, positions_admin[4][1], 100, 50, 'Add', GREEN, font)
delete_button = Button(WIDTH // 2 - 50, positions_admin[4][1], 100, 50, 'Delete', RED, font)
update_button = Button(WIDTH // 2 + 50, positions_admin[4][1], 100, 50, 'Update', BLUE, font)


back_button = Button(10, 10, 100, 50, '<- Back', GREEN, label_font)



# for logging in UI

username_entry_admin = TextInput(positions_admin[1][0], positions_admin[1][1], ELEMENT_WIDTH, ELEMENT_HEIGHT, font, 'Username')
password_entry_admin = TextInput(positions_admin[2][0], positions_admin[2][1], ELEMENT_WIDTH, ELEMENT_HEIGHT, font, 'Password',obscure=True)
login_button = Button(WIDTH // 2 - 150, positions_admin[3][1], 100, 50, 'Login', GREEN, font)
def main():
    clock = pygame.time.Clock()
    mode = 'menu'


# delay parameters for adding
    add_delay_active = False
    add_delay_start_time = 0
    add_delay_duration = 500

# delay parameters for deleting
    delete_delay_active = False
    delete_delay_start_time = 0
    delete_delay_duration = 500

# delay parameters for update
    update_delay_active = False
    update_delay_start_time = 0
    update_delay_duration = 500



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
                        mode = 'login'

            if mode == 'user':
                search_entry.handle_event(event)
            if mode == 'login':
                username_entry_admin.handle_event(event)
                password_entry_admin.handle_event(event)

            if mode == 'admin':
                itneg_entry.handle_event(event)
                english_entry.handle_event(event)
                tagalog_entry.handle_event(event)
            if event.type == pygame.MOUSEBUTTONDOWN:
                if back_button.is_clicked(event.pos):
                    mode = 'menu'
                if login_button.is_clicked(event.pos):
                    if username_entry_admin.text == user_name and password_entry_admin.text == pass_word:
                        mode = 'admin'
                

        win.blit(background_image, (0, 0))

        if mode == 'menu':
            user_button.draw(win)
            admin_button.draw(win)
        elif mode == 'user':
            back_button.draw(win)
            search_entry.draw(win)

        elif mode == 'login':
            username_entry_admin.draw(win)
            password_entry_admin.draw(win)
            login_button.draw(win)


        elif mode == 'admin':
            back_button.draw(win)
            itneg_entry.draw(win)
            english_entry.draw(win)
            tagalog_entry.draw(win)
            add_button.draw(win)
            delete_button.draw(win)
            update_button.draw(win)
            if event.type == pygame.MOUSEBUTTONDOWN:
               
                if add_button.is_clicked(event.pos) and not add_delay_active:
                     # Put your logic here for addin in the database
                    print('add')
                    add_delay_active = True
                    add_delay_start_time = pygame.time.get_ticks()


                elif delete_button.is_clicked(event.pos) and not delete_delay_active:
                    # Put your logic here for deleting to the database
                    print('delete')
                    delete_delay_active = True
                    delete_delay_start_time = pygame.time.get_ticks()

                elif update_button.is_clicked(event.pos) and not update_delay_active:
                    # Put your logic here for updating to the database
                    print('update')
                    update_delay_active = True
                    update_delay_start_time = pygame.time.get_ticks()

        if add_delay_active:
            if millis_delay(add_delay_start_time, add_delay_duration):
                add_delay_active = False

        if delete_delay_active:
            if millis_delay(delete_delay_start_time, delete_delay_duration):
                delete_delay_active = False

        if update_delay_active:
            if millis_delay(update_delay_start_time, update_delay_duration):
                update_delay_active = False

        pygame.display.flip()
        clock.tick(30)

if __name__ == '__main__':
    main()
