class CoffeeMachine:
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.type_coffee = {'1': [250, 0, 16, 1, 4], '2': [350, 75, 20, 1, 7], '3': [200, 100, 12, 1, 6]}
        self.choice = 0
        self.finished_products = []

    def remaining(self):  # Узнать содержимое кофемашины
        print('The coffee machine has:', str(self.water) + ' of water', str(self.milk) + ' of milk',
              str(self.beans) + ' of coffee beans', str(self.cups) + ' of disposable cups',
              str(self.money) + ' of money', sep='\n')

    def buy(self):
        self.choice = input('What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:')
        if self.choice == 'back':
            return
        """Проверка недостающих продуктов и добавления их в массив для дальнейшего вывода"""
        self.finished_products += ['water'] if self.water < self.type_coffee[self.choice][0] else []
        self.finished_products += ['milk'] if self.milk < self.type_coffee[self.choice][1] else []
        self.finished_products += ['beans'] if self.beans < self.type_coffee[self.choice][2] else []
        self.finished_products += ['cups'] if self.cups < self.type_coffee[self.choice][3] else []
        if len(self.finished_products) > 0:
            print('Sorry, not enough ' + ', '.join(self.finished_products) + '!')
            self.finished_products.clear()
        else:
            print('I have enough resources, making you a coffee!')
            self.water -= self.type_coffee[self.choice][0]
            self.milk -= self.type_coffee[self.choice][1]
            self.beans -= self.type_coffee[self.choice][2]
            self.cups -= self.type_coffee[self.choice][3]
            self.money += self.type_coffee[self.choice][4]

    def fill(self):  # Загрузка кофемашины продуктами
        self.water += int(input('How many ml of water do you want to add:'))
        self.milk += int(input('How many ml of milk do you want to add:'))
        self.beans += int(input('How many grams of coffee beans do you want to add:'))
        self.cups += int(input('How many disposable cups of coffee do you want to add:'))

    def take(self):  # Забрать с кофемашины накопленные деньги
        print('I gave you $' + str(self.money))
        self.money = 0


Go = CoffeeMachine()
while True:
    Go.action = input('Write action (buy, fill, take, remaining, exit):')
    if Go.action == 'buy':
        Go.buy()
    elif Go.action == 'fill':
        Go.fill()
    elif Go.action == 'take':
        Go.take()
    elif Go.action == 'remaining':
        Go.remaining()
    else:
        break
