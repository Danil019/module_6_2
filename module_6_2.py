class Vehicle:
    __COLOR_VARIANTS = ['red', 'blue', 'white', 'black', 'silver']
    def __init__(self, owner: str, model: str, engine_power: int, color: str):
        self.owner: str = owner
        self.__model: str = model
        self.__engine_power: int = engine_power
        self.__color: str = color

    def get_model(self):
        return print(f"Модель: {self.__model}")

    def get_horsepower(self):
        return print(f"Мощность двигателя: {self.__engine_power}")

    def get_color(self):
        return print(f"Цвет: {self.__color}")

    def print_info(self, ):
        self.get_model()
        self.get_horsepower()
        self.get_color()
        print(f"Владелец: {self.owner}")

    def set_color(self, new_color: str):
        for i in self.__COLOR_VARIANTS:
            if new_color.lower() == i:
                self.__color = new_color
                print(f'Вы изменили цвет на {new_color}!')
                break
        else:
            print(f"Нельзя сменить цвет на {new_color}")


class Sedan(Vehicle):
    pass

vehicle1 = Sedan('Fedos', 'Toyota Mark II', 500, 'blue')
vehicle1.print_info()
vehicle1.set_color('Pink')
vehicle1.set_color('BLACK')
vehicle1.owner = 'Vasyok'
vehicle1.print_info()