class CoffeeMachine():
    def __init__(self):
        self.water = 400
        self.milk = 540
        self.beans = 120
        self.cups = 9
        self.money = 550
        self.keep_running = True
        while self.keep_running:
            self.user_action()

    def machine_status(self):
        print("The coffee machine has:")
        print(f"{self.water} ml of water")
        print(f"{self.milk} ml of milk")
        print(f"{self.beans} gm of coffee beans")
        print(f"{self.cups} of disposable cups")
        print(f"${self.money} of money")

    def buy(self, num):
        # global water,milk,beans,cups,money
        if num == "1":
            if self.water < 250:
                print("Sorry, not enough water!")
            elif self.beans < 16:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 250
                self.beans -= 16
                self.cups -= 1
                self.money += 4
        elif num == "2":
            if self.water < 350:
                print("Sorry, not enough water!")
            elif self.milk < 75:
                print("Sorry, not enough milk!")
            elif self.beans < 20:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 350
                self.milk -= 75
                self.beans -= 20
                self.cups -= 1
                self.money += 7
        elif num == "3":
            if self.water < 200:
                print("Sorry, not enough water!")
            elif self.milk < 100:
                print("Sorry, not enough milk!")
            elif self.beans < 12:
                print("Sorry, not enough coffee beans!")
            elif self.cups < 1:
                print("Sorry, not enough cups!")
            else:
                print("I have enough resources, making you a coffee!")
                self.water -= 200
                self.milk -= 100
                self.beans -= 12
                self.cups -= 1
                self.money += 6
        elif num == "back":
            pass

    def fill(self):
        # global water,milk,beans,cups,money
        add_w = int(input("Write how many ml of water do you want to add: "))
        self.water += add_w
        add_m = int(input("Write how many ml of milk do you want to add: "))
        self.milk += add_m
        add_b = int(input("Write how many grams of coffee beans do you want to add: "))
        self.beans += add_b
        add_c = int(input("Write how many disposable cups of coffee do you want to add: "))
        self.cups += add_c

    def take(self):
        # global water,milk,beans,cups,money
        print(f"I gave you ${self.money}")
        self.money -= self.money

    def user_action(self):
        action = input("Write action (buy, fill, take, remaining, exit): ")
        if action == "buy":
            option = input("What do you want to buy? 1 - espresso, 2 - latte, 3 - cappuccino, back - to main menu:")
            CoffeeMachine.buy(self, option)
        elif action == "fill":
            CoffeeMachine.fill(self)
        elif action == "take":
            CoffeeMachine.take(self)
        elif action == "remaining":
            CoffeeMachine.machine_status(self)
        elif action == "exit":
            self.keep_running = False
        else:
            print("Please enter valid input !!")


machine = CoffeeMachine()
