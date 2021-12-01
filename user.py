class User:
    def __init__(self, name, balance=0):
        self.name = name
        self.balance = balance

    def make_withdrawl(self, amount):
        self.balance -= amount
        return self

    def deposit(self, amount):
        self.balance += amount 
        return self 

    def display_user_balance(self):
        print(self.balance)
        return self

    def transfer_money(user1, user2, amount):
        user1.balance -= amount
        user2.balance += amount
 
        print(f"{user1.name} transferred {amount} to {user2.name}")

Chelsea = User("Chelsea", 150)
Weston = User("Weston", 500)
Colby = User("Colby", 235)

Chelsea.make_withdrawl(50).deposit(50).deposit(500).deposit(10)
Chelsea.deposit(10)
print(Chelsea.name)
print(Chelsea.balance)

Weston.deposit(90).deposit(50000).make_withdrawl(2500).make_withdrawl(300)
print(Weston.name)
print(Weston.balance)

Weston.transfer_money(Chelsea, 345)

print(Chelsea.name)
print(Chelsea.balance)

print(Weston.name)
print(Weston.balance)