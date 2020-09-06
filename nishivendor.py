import csv


class NishiVendor():
  def __init__(self):
    self.goods = dict()
    with open("product_price_list", "r", newline="") as ppl:
      reader = csv.reader(ppl)
      for row in reader:
        self.goods[row[0]] = int(row[1])

  def charge(self, amount):
    self.charged = amount

  def price(self, item):
    return self.goods[item]
  
  def select(self, item):
    self.charged -= self.price(item)
  
    return item, self.charged