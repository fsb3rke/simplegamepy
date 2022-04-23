class Vector2:
    def __init__(self, x: float, y: float):
        self.__x = x
        self.__y = y

    @property
    def x(self):
        return self.__x

    @property
    def y(self):
        return self.__y

    @property
    def xy(self):
        tuple_xy = (self.__x, self.__y)
        return tuple_xy

    def set_vector(self, new_vector: tuple):
        self.__x = new_vector[0]
        self.__y = new_vector[1]
