from simplegamepy import *

screen_size = Vector2(500, 500)
# screen_size.set_vector(Vector2(500, 500).xy)
screen = window(screen_size.xy)

background_color = color(color_keys.none_color, 255, 255)
screen.set_background_color(background_color.rgb)

screen.set_screen_title("Berke simplegamepy deneme")


def start():
    pass


def event(event: pygame.event.Event):
    if event.type == pygame.QUIT:
        screen.running = False


def loop():
    python_logo = pygame.image.load("pyxd.png")
    screen.add(python_logo, Vector2(24, 52).xy)


screen.start(start, event, loop)
