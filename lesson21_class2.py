# Problem 1 and 2

"""
class Factory:
    def __init__(self):
        pass

    def engine(self):
        return "Двигатель создан"

    def bridge(self):
        return "Ходовая часть создана"


class Tayota(Factory):
    def __init__(self):
        Factory.__init__(self)

    def wheels(self):
        return "Колёса готовы"

    def windows(self):
        return "Стёкла готовы"

ta = Tayota()
results = []
results.append(ta.wheels())
results.append(ta.windows())
print(results)
"""


# Problem 3
"""
class Zoo:

    def __init__(self):
        self.animal_1 = 'Тигр'
        self.animal_2 = 'Бегемот'
        self.animal_3 = 'Жираф'


z = Zoo()
z.animal_1 = 'Лев'
z.animal_4 = [z.animal_2, z.animal_3]
z.animal_3 = "Змея"
print(z.__dict__)
"""


