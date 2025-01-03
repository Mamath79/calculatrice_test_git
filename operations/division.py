class Division:
    @staticmethod
    def calculer (a, b):
        if b == 0:
            raise ValueError('division par zero impossible')
        return a / b