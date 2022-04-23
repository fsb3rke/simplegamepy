class color:
    def __init__(self, r: int, g: int, b: int):
        self.__color = (r, g, b)

    def get_by_color_name(self, color_name: str):
        pass

    @property
    def r(self):
        return self.__color[0]

    @property
    def g(self):
        return self.__color[1]

    @property
    def b(self):
        return self.__color[2]

    @property
    def rgb(self):
        return self.__color


class color_keys:
    none_color: int = 0
