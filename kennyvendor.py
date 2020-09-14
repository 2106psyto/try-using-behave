import csv
import json


class Stock():
  def __init__(self):
    self.goods = dict()
    with open("product_price_list", "r", newline="") as ppl:
      reader = csv.reader(ppl)
      for row in reader:
        self.goods[row[0]] = int(row[1])

  def price(self, name):
    return self.goods[name]

  def list(self):
    return json.dumps(self.goods, ensure_ascii=False)


class KennyVendor():
  def __init__(self):
    self.goods = Stock()

  def charge(self, amount):
    self.charged = amount

  def price(self, item):
    return self.goods.price(item)
  
  def select(self, item=None):
    if self.charged == 0:
      return self.goods.list()

    if self.charged >= self.price(item):
      self.charged -= self.price(item)
  
    return item, self.charged