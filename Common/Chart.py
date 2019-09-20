import logging

import Common.Music as Ms


class Chart:
    def __init__(self):
        self.__list = []

    # Getter ------------------------------
    @property
    def list(self) -> list:
        return self.__list

    # Setter ------------------------------
    @list.setter
    def list(self, list: list):
        self.__list = list

    # Method ------------------------------
    def appendList(self, music: Ms.Music):
        self.list.append(music)

    def removeList(self, data):
        if type(data) == 'int':
            del self.list[data]
        elif type(data) == 'str':
            for music in self.list:
                if music.isrc == data:
                    self.list.remove(music)
                    break
        else:
            logging.debug('Type Error')

