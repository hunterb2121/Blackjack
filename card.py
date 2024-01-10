class Card:
    def __init__(self, suit, face, value, hidden):
        self._suit = suit
        self._face = face
        self._value = value
        self._hidden = hidden

    @property
    def suit(self):
        return self._suit

    @property
    def face(self):
        return self._face

    @property
    def value(self):
        return self._value

    @property
    def hidden(self):
        return self._hidden

    @suit.setter
    def suit(self, new):
        self._suit = new

    @face.setter
    def face(self, new):
        self._face = new

    @value.setter
    def value(self, new):
        self._value = new

    @hidden.setter
    def hidden(self, new):
        self._hidden = new

    def __str__(self):
        return f'{self._face} of {self._suit}'