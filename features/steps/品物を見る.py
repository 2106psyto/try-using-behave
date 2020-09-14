import csv
import json
from behave import *
from kennyvendor import KennyVendor

goods = dict()
def product_list():
  with open("product_price_list", "r", newline="") as ppl:
    reader = csv.reader(ppl)
    for row in reader:
      goods[row[0]] = int(row[1])
  return json.dumps(goods, ensure_ascii=False)


@given('ユーザーがお金を投入していないとき')
def step_impl(context):
    context.nv = KennyVendor()
    context.nv.charge(0)

@when('任意の品物を選択すると')
def step_impl(context):
    context.goods = context.nv.select()

@then('商品の一覧が返る')
def step_impl(context):
    assert context.failed is False
    assert context.goods == product_list()