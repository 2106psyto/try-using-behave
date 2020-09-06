class NishiVendor():
  def charge(self, amount):
    self.charged = amount

  def select(self, item):
    if item == "ペットボトルの水":
      self.charged -= 100
    else:
      self.charged -= 200
  
    return item, self.charged