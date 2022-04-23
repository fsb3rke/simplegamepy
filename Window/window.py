import pygame


class window:
    def __init__(self, size: tuple):
        self.__game_screen = pygame.display.set_mode(size)
        self.__screen = pygame.display
        self.running = True

    def start(self, start_name: any, event_loop_name: any, loop_name: any):
        self.__screen.flip()
        start_name()
        while self.running:
            for event in pygame.event.get():
                event_loop_name(event)
            loop_name()

    def set_background_color(self, new_background_color: tuple):
        self.__game_screen.fill(new_background_color)

    def set_screen_title(self, new_title_text: str):
        self.__screen.set_caption(new_title_text)

    def set_screen_icon(self, new_icon_path: str):
        self.__screen.set_caption(self.__screen.get_caption()[0], new_icon_path)

    def get_screen_title(self):
        return self.__screen.get_caption()[0]

    def get_screen_icon(self):
        return self.__screen.get_caption()[1]

    def get_screen_caption(self):
        return self.__screen.get_caption()

    def get_screen_x(self):
        return self.__screen.get_window_size()[0]

    def get_screen_y(self):
        return self.__screen.get_window_size()[1]

    def get_screen_size(self):
        return self.__screen.get_window_size()
