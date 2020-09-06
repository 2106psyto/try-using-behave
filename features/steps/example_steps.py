from behave import *
from nishivendor import NishiVendor


@given('we have behave installed')
def step_impl(context):
    pass

@when('we implement {number:d} tests')
def step_impl(context, number):  # -- NOTE: number is converted into integer
    assert number > 1 or number == 0
    context.tests_count = number

@then('behave will test them for us!')
def step_impl(context):
    assert context.failed is False
    assert context.tests_count >= 0


@given('ユーザーが {amount:d} 円を投入して')
def step_impl(context, amount):
    context.nv = NishiVendor()
    context.nv.charge(amount)

@when('"{product_name}"を選択すると')
def step_impl(context, product_name):  # -- NOTE: number is converted into integer
    context.selected_product = product_name
    context.item, context.change = context.nv.select(product_name)

@then('"{product_name}"が買える')
def step_impl(context, product_name):
    assert context.failed is False
    assert context.item == product_name

@then('おつりは {change:d} 円')
def step_impl(context, change):
    assert context.failed is False
    assert context.change == change