class Position(object):
    x = 0

    def up(self, distance):
        self.x = self.x + distance

    def down(self, distance):
        self.x = self.x - distance

    y = 0

    z = 0

    def toString(self):
        """
        Prints the current values of this position object.
        """
        return "[x:" + str(self.x) + ", y:" + str(self.y) + ", z:" + str(self.z) + "]"
