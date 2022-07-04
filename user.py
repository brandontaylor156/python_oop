class User:
    def __init__(self, first_name, last_name, email, age):
        self.first_name = first_name
        self.last_name = last_name
        self.email = email
        self.age = age
        self.is_rewards_member = False
        self.gold_card_points = 0

    def display_info(self):
        print(f"First Name: {self.first_name}\nLast Name: {self.last_name}\nEmail: {self.email}\nAge: {self.age}\nRewards Member: {self.is_rewards_member}\nGold Card Points: {self.gold_card_points}")
        print("\n")

    def enroll(self):
        if self.is_rewards_member is True:
            print("Already a member")
            return
        self.is_rewards_member = True
        self.gold_card_points = 200

    def spend_points(self, amount):
        if self.gold_card_points - amount < 0:
            print("Not enough points")
            return
        self.gold_card_points -= amount

myUser = User("Brandon", "Taylor", "brandon.david4@outlook.com", 26) 
myUser.enroll()
# myUser.display_info()

newUser1 = User("Kobe", "Bryant", "kobe@gmail.com", 24)
# newUser1.display_info()

newUser2 = User("Lebron", "James", "lebron@gmail.com", 23)
# newUser2.display_info()

myUser.spend_points(50)
# myUser.display_info()

newUser1.enroll()
newUser1.spend_points(80)

myUser.display_info()
newUser1.display_info()
newUser2.display_info()

myUser.enroll()
newUser2.spend_points(40)
