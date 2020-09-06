class NishiVendor():
  def __init__(self):
    self.goods = {
      "ペットボトルの水":100,
      "RedBull":200,
      "おでん":500
    }

  def charge(self, amount):
    self.charged = amount

  def price(self, item):
    return self.goods[item]
  
  def select(self, item):
    self.charged -= self.price(item)
  
    return item, self.charged