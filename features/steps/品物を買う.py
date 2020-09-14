from behave import *
from kennyvendor import KennyVendor


@given('ユーザーが {amount:d} 円を投入して')
def step_impl(context, amount):
    context.nv = KennyVendor()
    context.nv.charge(amount)

@when('"{product_name}"を選択すると')
def step_impl(context, product_name):
    context.selected_product = product_name
    context.item, context.change = context.nv.select(product_name)

@then('"{product_name}"が買えて')
def step_impl(context, product_name):
    assert context.failed is False
    assert context.item == product_name

@then('おつりは{change:d}円')
def step_impl(context, change):
    assert context.failed is False
    assert context.change == change