class Account:
  def __init__(self, _Name, _City, _isChecking):
    self.name = _Name
    self.city = _City
    self.isChecking = _isChecking
    self.currentBalence = 0

  def checkBalence(self):
    return self.currentBalence

  def deposit(self, amountDeposit):
   # amountDeposit = input("How much would you like to deposit?")
    self.currentBalence = self.currentBalence + amountDeposit

  def withdraw(self, amountWithdraw):
    if amountWithdraw > self.currentBalence:
      print("You don't have enough money to withdraw that amount")
    else:
      self.currentBalence = self.currentBalence - amountWithdraw
