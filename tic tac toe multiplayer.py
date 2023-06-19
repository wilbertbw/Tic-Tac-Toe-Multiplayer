import pygame
pygame.font.init()

WIN_WIDTH, WIN_HEIGHT = 510, 510

WINNER_FONT = pygame.font.SysFont('timesnew', 100)
TEXT_FONT = pygame.font.SysFont('timesnew', 40)
SCORE_FONT = pygame.font.SysFont('timesnew', 30)

VERT_ONE = pygame.Rect(100,100,10,300)
VERT_TWO = pygame.Rect(200,100,10,300)
VERT_THREE = pygame.Rect(300,100,10,300)
VERT_FOUR = pygame.Rect(400,100,10,300)
HORI_ONE = pygame.Rect(100,100,310,10)
HORI_TWO = pygame.Rect(100,200,310,10)
HORI_THREE = pygame.Rect(100,300,310,10)
HORI_FOUR = pygame.Rect(100,400,310,10)

FPS = 60

WHITE = (255, 255, 255)
RAND_COLOUR = (128, 128, 128)
BLACK = (0, 0, 0)
BLUE = (0, 0, 255)
RED = (255,0,0)


class Sprite(pygame.sprite.Sprite):
    def __init__(self, color, width, height):
        super().__init__()

        self.image = pygame.Surface([width, height], pygame.SRCALPHA)
        pygame.draw.rect(self.image, color, pygame.Rect(0, 0, width, height))
        
        self.click_image = pygame.Surface([width, height], pygame.SRCALPHA)

        self.rect = self.image.get_rect()

        self.start_time = pygame.time.get_ticks()

pygame.init()

WIN = pygame.display.set_mode((WIN_WIDTH, WIN_HEIGHT))
pygame.display.set_caption("TIC TAC DOE")

group = pygame.sprite.Group()


def mark_down(click_pos, turn): # fix the part when pattern is clicked in the same spot
    (x, y) = click_pos
    if (turn % 2 == 0):
        colour = BLUE
    else:
        colour = RED
    
    if (x > 110 and x < 200 and y > 110 and y < 200):
        top_left = Sprite(colour, 90, 90)
        top_left.rect.x = 110
        top_left.rect.y = 110
        if top_left not in group:
            group.add(top_left)
    
    elif (x > 210 and x < 300 and y > 110 and y < 200):
        top_middle = Sprite(colour, 90, 90)
        top_middle.rect.x = 210
        top_middle.rect.y = 110
        if top_middle not in group:
            group.add(top_middle)
    
    elif (x > 310 and x < 400 and y > 110 and y < 200):
        top_right = Sprite(colour, 90, 90)
        top_right.rect.x = 310
        top_right.rect.y = 110
        if top_right not in group:
            group.add(top_right)
    
    elif (x > 110 and x < 200 and y > 210 and y < 300):
        middle_left = Sprite(colour, 90, 90)
        middle_left.rect.x = 110
        middle_left.rect.y = 210
        if middle_left not in group:
            group.add(middle_left)
    
    elif (x > 210 and x < 300 and y > 210 and y < 300):
        middle_middle = Sprite(colour, 90, 90)
        middle_middle.rect.x = 210
        middle_middle.rect.y = 210
        if middle_middle not in group:
            group.add(middle_middle)
    
    elif (x > 310 and x < 400 and y > 210 and y < 300):
        middle_right = Sprite(colour, 90, 90)
        middle_right.rect.x = 310
        middle_right.rect.y = 210
        if middle_right not in group:
            group.add(middle_right)
    
    elif (x > 110 and x < 200 and y > 310 and y < 400):
        bottom_left = Sprite(colour, 90, 90)
        bottom_left.rect.x = 110
        bottom_left.rect.y = 310
        if bottom_left not in group:
            group.add(bottom_left)
    
    elif (x > 210 and x < 300 and y > 310 and y < 400):
        bottom_middle = Sprite(colour, 90, 90)
        bottom_middle.rect.x = 210
        bottom_middle.rect.y = 310
        if bottom_middle not in group:
            group.add(bottom_middle)
    
    elif (x > 310 and x < 400 and y > 310 and y < 400):
        bottom_right = Sprite(colour, 90, 90)
        bottom_right.rect.x = 310
        bottom_right.rect.y = 310
        if bottom_right not in group:
            group.add(bottom_right)


def check_grid(colours):
    coordinates = [(0,(155,155)), (1,(255,155)), (2,(355,155)), (3,(155,255)), (4,(255,255)), (5,(355,255)), (6,(155,355)), (7,(255,355)), (8,(355,355))]
    for track, coordinate in coordinates:
        val = WIN.get_at(coordinate)[:3]
        x, y, z=  val
        if (x == 255 and y == 0 and z == 0):
            colours[track] = 1
        elif (x == 0 and y == 0 and z == 255):
            colours[track] = 2
    
    if colours[0] == colours[1] and colours[0] == colours[2]:
        return colours[0]
    
    elif colours[3] == colours[4] and colours[3] == colours[5]:
        return colours[3]
    
    elif colours[6] == colours[7] and colours[6] == colours[8]:
        return colours[6]
    
    elif colours[0] == colours[3] and colours[0] == colours[6]:
        return colours[0]
    
    elif colours[1] == colours[4] and colours[1] == colours[7]:
        return colours[1]
    
    elif colours[2] == colours[5] and colours[2] == colours[8]:
        return colours[2]
    
    elif colours[0] == colours[4] and colours[0] == colours[8]:
        return colours[0]
    
    elif colours[2] == colours[4] and colours[2] == colours[6]:
        return colours[2]


def draw_winner(text):
    draw_text = WINNER_FONT.render(text, 1, BLACK)
    WIN.blit(draw_text, (WIN_WIDTH // 2 - draw_text.get_width() // 2, WIN_HEIGHT - draw_text.get_height() / 2 - 45))

    pygame.display.update()
    pygame.time.delay(5000)


def draw_grid():
    draw_text = TEXT_FONT.render("Welome to Tic Tac Doe!", 1, BLACK)
    WIN.blit(draw_text, (20, 20))

    pygame.draw.rect(WIN, BLACK, HORI_ONE)
    pygame.draw.rect(WIN, BLACK, HORI_TWO)
    pygame.draw.rect(WIN, BLACK, HORI_THREE)
    pygame.draw.rect(WIN, BLACK, HORI_FOUR)

    pygame.draw.rect(WIN, BLACK, VERT_ONE)
    pygame.draw.rect(WIN, BLACK, VERT_TWO)
    pygame.draw.rect(WIN, BLACK, VERT_THREE)
    pygame.draw.rect(WIN, BLACK, VERT_FOUR)


def draw_score(red_wins, blue_wins):
    draw_text_red = SCORE_FONT.render("Red Score: " + str(red_wins), 1, RED)
    draw_text_blue = SCORE_FONT.render("Blue Score: " + str(blue_wins), 1, BLUE)

    WIN.blit(draw_text_red, (WIN_WIDTH - draw_text_red.get_width() - 10, 20))
    WIN.blit(draw_text_blue, (WIN_WIDTH - draw_text_blue.get_width() - 10, 25 + draw_text_red.get_height()))


def main():
    clock = pygame.time.Clock()
    run = True

    colours = [10,11,12,13,14,15,16,17,18,19]

    click_pos = (0,0)

    red_wins = 0
    blue_wins = 0

    turn = 1
    
    while run:
        clock.tick(FPS)

        event_list = pygame.event.get()

        for event in event_list:
            if event.type == pygame.QUIT:
                run = False
                pygame.quit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                click_pos = pygame.mouse.get_pos()
                x, y = click_pos
                initial_len = len(group)
                if (x > 120 and x < 190 or x > 220 and x < 290 or x > 320 and x < 390):
                    if (y > 120 and y < 190 or y > 220 and y < 290 or y > 320 and y < 390):
                        mark_down(click_pos, turn)
                        current_len = len(group)
                        if (current_len > initial_len):
                            turn += 1
                        

        winner_text = ""

        if (turn >= 6):
            val = check_grid(colours)
            if val == 1:
                red_wins += 1
                winner_text = "RED WINS!"
                draw_winner(winner_text)
                group.empty()
                turn = 1
                colours = [10,11,12,13,14,15,16,17,18,19]
                click_pos = (0,0)
                pass
            elif val == 2:
                blue_wins += 1
                winner_text = "BLUE WINS!" 
                draw_winner(winner_text)
                group.empty()
                turn = 1
                colours = [10,11,12,13,14,15,16,17,18,19]
                click_pos = (0,0)
                pass

        group.update()

        WIN.fill(WHITE)
        draw_grid()
        draw_score(red_wins, blue_wins)
        group.draw(WIN)
        pygame.display.flip()

        if (turn == 10):
            winner_text = "DRAW!"
            draw_winner(winner_text)
            group.empty()
            turn = 1
            colours = [10,11,12,13,14,15,16,17,18,19]
            click_pos = (0,0)
            pass


if __name__ == "__main__":
    main()