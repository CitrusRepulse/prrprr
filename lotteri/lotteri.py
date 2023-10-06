import random

class lotteri:

    def __init__(self):
        
        self.list_vinster = [
            "En kruka",
            "fot massage från amin",
            "Strumpa med hål",
            "Trasig balong",
            "Fri entre på soptippen",
            "En ruta marabou choklad",
            "En ofungerande whiteboardtavla",
            "Sten från 1700 talet",
            "Date med Emil",
            "Slaskig gurka"
        ]


    def get_vinst(self):
        slumptal = random.randint(0, len(self.list_vinster)-1 )
        
        return self.list_vinster[slumptal]