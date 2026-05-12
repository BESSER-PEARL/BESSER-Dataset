import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Product,
    Menu,
    Store,
    Manager,
    Drink,
    Order,
    Food,
    customerDatabase,
    Payment,
    SUID,
    Card,
    CardReader,
    Register,
    Sale,
    Sales_Line_Item,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "itemID" in params, "Missing parameter 'itemID'"
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"

def test_product_has_itemID():
    assert hasattr(Product, "itemID")
    descriptor = None
    for klass in Product.__mro__:
        if "itemID" in klass.__dict__:
            descriptor = klass.__dict__["itemID"]
            break
    assert isinstance(descriptor, property)

def test_product_has_description():
    assert hasattr(Product, "description")
    descriptor = None
    for klass in Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_product_has_name():
    assert hasattr(Product, "name")
    descriptor = None
    for klass in Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_product_has_price():
    assert hasattr(Product, "price")
    descriptor = None
    for klass in Product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_menu_is_not_abstract():
    assert not inspect.isabstract(Menu)


def test_menu_constructor_exists():
    assert callable(Menu.__init__)


def test_menu_constructor_args():
    sig = inspect.signature(Menu.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"

def test_menu_has__attr():
    assert hasattr(Menu, "_attr")
    descriptor = None
    for klass in Menu.__mro__:
        if "_attr" in klass.__dict__:
            descriptor = klass.__dict__["_attr"]
            break
    assert isinstance(descriptor, property)



def test_store_is_not_abstract():
    assert not inspect.isabstract(Store)


def test_store_constructor_exists():
    assert callable(Store.__init__)


def test_store_constructor_args():
    sig = inspect.signature(Store.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_store_has_Name():
    assert hasattr(Store, "Name")
    descriptor = None
    for klass in Store.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_store_has_Address():
    assert hasattr(Store, "Address")
    descriptor = None
    for klass in Store.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "password" in params, "Missing parameter 'password'"

def test_manager_has_name():
    assert hasattr(Manager, "name")
    descriptor = None
    for klass in Manager.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_password():
    assert hasattr(Manager, "password")
    descriptor = None
    for klass in Manager.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_drink_is_not_abstract():
    assert not inspect.isabstract(Drink)


def test_drink_constructor_exists():
    assert callable(Drink.__init__)


def test_drink_constructor_args():
    sig = inspect.signature(Drink.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "name" in params, "Missing parameter 'name'"

def test_drink_has_price():
    assert hasattr(Drink, "price")
    descriptor = None
    for klass in Drink.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_drink_has_quantity():
    assert hasattr(Drink, "quantity")
    descriptor = None
    for klass in Drink.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_drink_has_name():
    assert hasattr(Drink, "name")
    descriptor = None
    for klass in Drink.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "drinkPrice" in params, "Missing parameter 'drinkPrice'"
    assert "foodName" in params, "Missing parameter 'foodName'"
    assert "foodPrice" in params, "Missing parameter 'foodPrice'"
    assert "customer" in params, "Missing parameter 'customer'"
    assert "drinkName" in params, "Missing parameter 'drinkName'"

def test_order_has_drinkPrice():
    assert hasattr(Order, "drinkPrice")
    descriptor = None
    for klass in Order.__mro__:
        if "drinkPrice" in klass.__dict__:
            descriptor = klass.__dict__["drinkPrice"]
            break
    assert isinstance(descriptor, property)

def test_order_has_foodName():
    assert hasattr(Order, "foodName")
    descriptor = None
    for klass in Order.__mro__:
        if "foodName" in klass.__dict__:
            descriptor = klass.__dict__["foodName"]
            break
    assert isinstance(descriptor, property)

def test_order_has_foodPrice():
    assert hasattr(Order, "foodPrice")
    descriptor = None
    for klass in Order.__mro__:
        if "foodPrice" in klass.__dict__:
            descriptor = klass.__dict__["foodPrice"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customer():
    assert hasattr(Order, "customer")
    descriptor = None
    for klass in Order.__mro__:
        if "customer" in klass.__dict__:
            descriptor = klass.__dict__["customer"]
            break
    assert isinstance(descriptor, property)

def test_order_has_drinkName():
    assert hasattr(Order, "drinkName")
    descriptor = None
    for klass in Order.__mro__:
        if "drinkName" in klass.__dict__:
            descriptor = klass.__dict__["drinkName"]
            break
    assert isinstance(descriptor, property)



def test_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_food_constructor_exists():
    assert callable(Food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_food_has_name():
    assert hasattr(Food, "name")
    descriptor = None
    for klass in Food.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_food_has_price():
    assert hasattr(Food, "price")
    descriptor = None
    for klass in Food.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_food_has_attribute():
    assert hasattr(Food, "attribute")
    descriptor = None
    for klass in Food.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_food_has_quantity():
    assert hasattr(Food, "quantity")
    descriptor = None
    for klass in Food.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_customerdatabase_is_not_abstract():
    assert not inspect.isabstract(customerDatabase)


def test_customerdatabase_constructor_exists():
    assert callable(customerDatabase.__init__)


def test_customerdatabase_constructor_args():
    sig = inspect.signature(customerDatabase.__init__)
    params = list(sig.parameters.keys())
    assert "creditCardNum" in params, "Missing parameter 'creditCardNum'"
    assert "paymentHistory" in params, "Missing parameter 'paymentHistory'"
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "SUID" in params, "Missing parameter 'SUID'"

def test_customerdatabase_has_creditCardNum():
    assert hasattr(customerDatabase, "creditCardNum")
    descriptor = None
    for klass in customerDatabase.__mro__:
        if "creditCardNum" in klass.__dict__:
            descriptor = klass.__dict__["creditCardNum"]
            break
    assert isinstance(descriptor, property)

def test_customerdatabase_has_paymentHistory():
    assert hasattr(customerDatabase, "paymentHistory")
    descriptor = None
    for klass in customerDatabase.__mro__:
        if "paymentHistory" in klass.__dict__:
            descriptor = klass.__dict__["paymentHistory"]
            break
    assert isinstance(descriptor, property)

def test_customerdatabase_has_customerName():
    assert hasattr(customerDatabase, "customerName")
    descriptor = None
    for klass in customerDatabase.__mro__:
        if "customerName" in klass.__dict__:
            descriptor = klass.__dict__["customerName"]
            break
    assert isinstance(descriptor, property)

def test_customerdatabase_has_SUID():
    assert hasattr(customerDatabase, "SUID")
    descriptor = None
    for klass in customerDatabase.__mro__:
        if "SUID" in klass.__dict__:
            descriptor = klass.__dict__["SUID"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_payment_has_amount():
    assert hasattr(Payment, "amount")
    descriptor = None
    for klass in Payment.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_suid_is_not_abstract():
    assert not inspect.isabstract(SUID)


def test_suid_constructor_exists():
    assert callable(SUID.__init__)


def test_suid_constructor_args():
    sig = inspect.signature(SUID.__init__)
    params = list(sig.parameters.keys())
    assert "suFOODBal" in params, "Missing parameter 'suFOODBal'"
    assert "studentName" in params, "Missing parameter 'studentName'"
    assert "ID" in params, "Missing parameter 'ID'"

def test_suid_has_suFOODBal():
    assert hasattr(SUID, "suFOODBal")
    descriptor = None
    for klass in SUID.__mro__:
        if "suFOODBal" in klass.__dict__:
            descriptor = klass.__dict__["suFOODBal"]
            break
    assert isinstance(descriptor, property)

def test_suid_has_studentName():
    assert hasattr(SUID, "studentName")
    descriptor = None
    for klass in SUID.__mro__:
        if "studentName" in klass.__dict__:
            descriptor = klass.__dict__["studentName"]
            break
    assert isinstance(descriptor, property)

def test_suid_has_ID():
    assert hasattr(SUID, "ID")
    descriptor = None
    for klass in SUID.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)



def test_card_is_not_abstract():
    assert not inspect.isabstract(Card)


def test_card_constructor_exists():
    assert callable(Card.__init__)


def test_card_constructor_args():
    sig = inspect.signature(Card.__init__)
    params = list(sig.parameters.keys())
    assert "cardholderName" in params, "Missing parameter 'cardholderName'"
    assert "isDebit" in params, "Missing parameter 'isDebit'"
    assert "cardSN" in params, "Missing parameter 'cardSN'"
    assert "isCredit" in params, "Missing parameter 'isCredit'"
    assert "cardNumber" in params, "Missing parameter 'cardNumber'"

def test_card_has_cardholderName():
    assert hasattr(Card, "cardholderName")
    descriptor = None
    for klass in Card.__mro__:
        if "cardholderName" in klass.__dict__:
            descriptor = klass.__dict__["cardholderName"]
            break
    assert isinstance(descriptor, property)

def test_card_has_isDebit():
    assert hasattr(Card, "isDebit")
    descriptor = None
    for klass in Card.__mro__:
        if "isDebit" in klass.__dict__:
            descriptor = klass.__dict__["isDebit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardSN():
    assert hasattr(Card, "cardSN")
    descriptor = None
    for klass in Card.__mro__:
        if "cardSN" in klass.__dict__:
            descriptor = klass.__dict__["cardSN"]
            break
    assert isinstance(descriptor, property)

def test_card_has_isCredit():
    assert hasattr(Card, "isCredit")
    descriptor = None
    for klass in Card.__mro__:
        if "isCredit" in klass.__dict__:
            descriptor = klass.__dict__["isCredit"]
            break
    assert isinstance(descriptor, property)

def test_card_has_cardNumber():
    assert hasattr(Card, "cardNumber")
    descriptor = None
    for klass in Card.__mro__:
        if "cardNumber" in klass.__dict__:
            descriptor = klass.__dict__["cardNumber"]
            break
    assert isinstance(descriptor, property)



def test_cardreader_is_not_abstract():
    assert not inspect.isabstract(CardReader)


def test_cardreader_constructor_exists():
    assert callable(CardReader.__init__)


def test_cardreader_constructor_args():
    sig = inspect.signature(CardReader.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_cardreader_has_attribute():
    assert hasattr(CardReader, "attribute")
    descriptor = None
    for klass in CardReader.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_register_is_not_abstract():
    assert not inspect.isabstract(Register)


def test_register_constructor_exists():
    assert callable(Register.__init__)


def test_register_constructor_args():
    sig = inspect.signature(Register.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_register_has_attribute():
    assert hasattr(Register, "attribute")
    descriptor = None
    for klass in Register.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_sale_is_not_abstract():
    assert not inspect.isabstract(Sale)


def test_sale_constructor_exists():
    assert callable(Sale.__init__)


def test_sale_constructor_args():
    sig = inspect.signature(Sale.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "isComplete" in params, "Missing parameter 'isComplete'"

def test_sale_has_Date():
    assert hasattr(Sale, "Date")
    descriptor = None
    for klass in Sale.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_sale_has_Time():
    assert hasattr(Sale, "Time")
    descriptor = None
    for klass in Sale.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_sale_has_isComplete():
    assert hasattr(Sale, "isComplete")
    descriptor = None
    for klass in Sale.__mro__:
        if "isComplete" in klass.__dict__:
            descriptor = klass.__dict__["isComplete"]
            break
    assert isinstance(descriptor, property)



def test_sales_line_item_is_not_abstract():
    assert not inspect.isabstract(Sales_Line_Item)


def test_sales_line_item_constructor_exists():
    assert callable(Sales_Line_Item.__init__)


def test_sales_line_item_constructor_args():
    sig = inspect.signature(Sales_Line_Item.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"

def test_sales_line_item_has_Quantity():
    assert hasattr(Sales_Line_Item, "Quantity")
    descriptor = None
    for klass in Sales_Line_Item.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)


# =============================================================================
# HYPOTHESIS STRATEGIES
# =============================================================================

safe_text = st.text(
    alphabet=st.characters(
        whitelist_categories=("Ll", "Lu", "Nd"),
        whitelist_characters="_",
    ),
    min_size=1,
).filter(lambda s: s[0].isalpha())
Product_strategy = st.builds(
    Product,
    itemID=
        st.integers(),
    description=
        safe_text,
    name=
        safe_text,
    price=
        safe_text
)
Menu_strategy = st.builds(
    Menu,
    _attr=
        safe_text
)
Store_strategy = st.builds(
    Store,
    Name=
        safe_text,
    Address=
        safe_text
)
Manager_strategy = st.builds(
    Manager,
    name=
        safe_text,
    password=
        safe_text
)
Drink_strategy = st.builds(
    Drink,
    price=
        safe_text,
    quantity=
        st.integers(),
    name=
        safe_text
)
Order_strategy = st.builds(
    Order,
    drinkPrice=
        st.integers(),
    foodName=
        safe_text,
    foodPrice=
        st.integers(),
    customer=
        safe_text,
    drinkName=
        safe_text
)
Food_strategy = st.builds(
    Food,
    name=
        safe_text,
    price=
        safe_text,
    attribute=
        safe_text,
    quantity=
        st.integers()
)
customerDatabase_strategy = st.builds(
    customerDatabase,
    creditCardNum=
        st.integers(),
    paymentHistory=
        safe_text,
    customerName=
        safe_text,
    SUID=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    amount=
        safe_text
)
SUID_strategy = st.builds(
    SUID,
    suFOODBal=
        safe_text,
    studentName=
        safe_text,
    ID=
        st.integers()
)
Card_strategy = st.builds(
    Card,
    cardholderName=
        safe_text,
    isDebit=
        st.booleans(),
    cardSN=
        st.integers(),
    isCredit=
        st.booleans(),
    cardNumber=
        st.integers()
)
CardReader_strategy = st.builds(
    CardReader,
    attribute=
        safe_text
)
Register_strategy = st.builds(
    Register,
    attribute=
        safe_text
)
Sale_strategy = st.builds(
    Sale,
    Date=
        safe_text,
    Time=
        safe_text,
    isComplete=
        st.booleans()
)
Sales_Line_Item_strategy = st.builds(
    Sales_Line_Item,
    Quantity=
        st.integers()
)

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)

@given(instance=Product_strategy)
def test_product_itemID_type(instance):
    assert isinstance(instance.itemID, int)


@given(instance=Product_strategy)
def test_product_itemID_setter(instance):
    original = instance.itemID
    instance.itemID = original
    assert instance.itemID == original

@given(instance=Product_strategy)
def test_product_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=Product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=Product_strategy)
def test_product_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Product_strategy)
def test_product_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Menu_strategy)
@settings(max_examples=50)
def test_menu_instantiation(instance):
    assert isinstance(instance, Menu)

@given(instance=Menu_strategy)
def test_menu__attr_type(instance):
    assert isinstance(instance._attr, str)


@given(instance=Menu_strategy)
def test_menu__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original

@given(instance=Store_strategy)
@settings(max_examples=50)
def test_store_instantiation(instance):
    assert isinstance(instance, Store)

@given(instance=Store_strategy)
def test_store_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Store_strategy)
def test_store_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Store_strategy)
def test_store_Address_type(instance):
    assert isinstance(instance.Address, str)


@given(instance=Store_strategy)
def test_store_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)

@given(instance=Manager_strategy)
def test_manager_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Manager_strategy)
def test_manager_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Manager_strategy)
def test_manager_password_type(instance):
    assert isinstance(instance.password, str)


@given(instance=Manager_strategy)
def test_manager_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Drink_strategy)
@settings(max_examples=50)
def test_drink_instantiation(instance):
    assert isinstance(instance, Drink)

@given(instance=Drink_strategy)
def test_drink_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=Drink_strategy)
def test_drink_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Drink_strategy)
def test_drink_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=Drink_strategy)
def test_drink_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Drink_strategy)
def test_drink_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Drink_strategy)
def test_drink_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)

@given(instance=Order_strategy)
def test_order_drinkPrice_type(instance):
    assert isinstance(instance.drinkPrice, int)


@given(instance=Order_strategy)
def test_order_drinkPrice_setter(instance):
    original = instance.drinkPrice
    instance.drinkPrice = original
    assert instance.drinkPrice == original

@given(instance=Order_strategy)
def test_order_foodName_type(instance):
    assert isinstance(instance.foodName, str)


@given(instance=Order_strategy)
def test_order_foodName_setter(instance):
    original = instance.foodName
    instance.foodName = original
    assert instance.foodName == original

@given(instance=Order_strategy)
def test_order_foodPrice_type(instance):
    assert isinstance(instance.foodPrice, int)


@given(instance=Order_strategy)
def test_order_foodPrice_setter(instance):
    original = instance.foodPrice
    instance.foodPrice = original
    assert instance.foodPrice == original

@given(instance=Order_strategy)
def test_order_customer_type(instance):
    assert isinstance(instance.customer, str)


@given(instance=Order_strategy)
def test_order_customer_setter(instance):
    original = instance.customer
    instance.customer = original
    assert instance.customer == original

@given(instance=Order_strategy)
def test_order_drinkName_type(instance):
    assert isinstance(instance.drinkName, str)


@given(instance=Order_strategy)
def test_order_drinkName_setter(instance):
    original = instance.drinkName
    instance.drinkName = original
    assert instance.drinkName == original

@given(instance=Food_strategy)
@settings(max_examples=50)
def test_food_instantiation(instance):
    assert isinstance(instance, Food)

@given(instance=Food_strategy)
def test_food_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=Food_strategy)
def test_food_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Food_strategy)
def test_food_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=Food_strategy)
def test_food_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Food_strategy)
def test_food_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=Food_strategy)
def test_food_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Food_strategy)
def test_food_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=Food_strategy)
def test_food_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=customerDatabase_strategy)
@settings(max_examples=50)
def test_customerdatabase_instantiation(instance):
    assert isinstance(instance, customerDatabase)

@given(instance=customerDatabase_strategy)
def test_customerdatabase_creditCardNum_type(instance):
    assert isinstance(instance.creditCardNum, int)


@given(instance=customerDatabase_strategy)
def test_customerdatabase_creditCardNum_setter(instance):
    original = instance.creditCardNum
    instance.creditCardNum = original
    assert instance.creditCardNum == original

@given(instance=customerDatabase_strategy)
def test_customerdatabase_paymentHistory_type(instance):
    assert isinstance(instance.paymentHistory, str)


@given(instance=customerDatabase_strategy)
def test_customerdatabase_paymentHistory_setter(instance):
    original = instance.paymentHistory
    instance.paymentHistory = original
    assert instance.paymentHistory == original

@given(instance=customerDatabase_strategy)
def test_customerdatabase_customerName_type(instance):
    assert isinstance(instance.customerName, str)


@given(instance=customerDatabase_strategy)
def test_customerdatabase_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original

@given(instance=customerDatabase_strategy)
def test_customerdatabase_SUID_type(instance):
    assert isinstance(instance.SUID, int)


@given(instance=customerDatabase_strategy)
def test_customerdatabase_SUID_setter(instance):
    original = instance.SUID
    instance.SUID = original
    assert instance.SUID == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)

@given(instance=Payment_strategy)
def test_payment_amount_type(instance):
    assert isinstance(instance.amount, str)


@given(instance=Payment_strategy)
def test_payment_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=SUID_strategy)
@settings(max_examples=50)
def test_suid_instantiation(instance):
    assert isinstance(instance, SUID)

@given(instance=SUID_strategy)
def test_suid_suFOODBal_type(instance):
    assert isinstance(instance.suFOODBal, str)


@given(instance=SUID_strategy)
def test_suid_suFOODBal_setter(instance):
    original = instance.suFOODBal
    instance.suFOODBal = original
    assert instance.suFOODBal == original

@given(instance=SUID_strategy)
def test_suid_studentName_type(instance):
    assert isinstance(instance.studentName, str)


@given(instance=SUID_strategy)
def test_suid_studentName_setter(instance):
    original = instance.studentName
    instance.studentName = original
    assert instance.studentName == original

@given(instance=SUID_strategy)
def test_suid_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=SUID_strategy)
def test_suid_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Card_strategy)
@settings(max_examples=50)
def test_card_instantiation(instance):
    assert isinstance(instance, Card)

@given(instance=Card_strategy)
def test_card_cardholderName_type(instance):
    assert isinstance(instance.cardholderName, str)


@given(instance=Card_strategy)
def test_card_cardholderName_setter(instance):
    original = instance.cardholderName
    instance.cardholderName = original
    assert instance.cardholderName == original

@given(instance=Card_strategy)
def test_card_isDebit_type(instance):
    assert isinstance(instance.isDebit, bool)


@given(instance=Card_strategy)
def test_card_isDebit_setter(instance):
    original = instance.isDebit
    instance.isDebit = original
    assert instance.isDebit == original

@given(instance=Card_strategy)
def test_card_cardSN_type(instance):
    assert isinstance(instance.cardSN, int)


@given(instance=Card_strategy)
def test_card_cardSN_setter(instance):
    original = instance.cardSN
    instance.cardSN = original
    assert instance.cardSN == original

@given(instance=Card_strategy)
def test_card_isCredit_type(instance):
    assert isinstance(instance.isCredit, bool)


@given(instance=Card_strategy)
def test_card_isCredit_setter(instance):
    original = instance.isCredit
    instance.isCredit = original
    assert instance.isCredit == original

@given(instance=Card_strategy)
def test_card_cardNumber_type(instance):
    assert isinstance(instance.cardNumber, int)


@given(instance=Card_strategy)
def test_card_cardNumber_setter(instance):
    original = instance.cardNumber
    instance.cardNumber = original
    assert instance.cardNumber == original

@given(instance=CardReader_strategy)
@settings(max_examples=50)
def test_cardreader_instantiation(instance):
    assert isinstance(instance, CardReader)

@given(instance=CardReader_strategy)
def test_cardreader_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=CardReader_strategy)
def test_cardreader_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Register_strategy)
@settings(max_examples=50)
def test_register_instantiation(instance):
    assert isinstance(instance, Register)

@given(instance=Register_strategy)
def test_register_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=Register_strategy)
def test_register_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Sale_strategy)
@settings(max_examples=50)
def test_sale_instantiation(instance):
    assert isinstance(instance, Sale)

@given(instance=Sale_strategy)
def test_sale_Date_type(instance):
    assert isinstance(instance.Date, str)


@given(instance=Sale_strategy)
def test_sale_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Sale_strategy)
def test_sale_Time_type(instance):
    assert isinstance(instance.Time, str)


@given(instance=Sale_strategy)
def test_sale_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original

@given(instance=Sale_strategy)
def test_sale_isComplete_type(instance):
    assert isinstance(instance.isComplete, bool)


@given(instance=Sale_strategy)
def test_sale_isComplete_setter(instance):
    original = instance.isComplete
    instance.isComplete = original
    assert instance.isComplete == original

@given(instance=Sales_Line_Item_strategy)
@settings(max_examples=50)
def test_sales_line_item_instantiation(instance):
    assert isinstance(instance, Sales_Line_Item)

@given(instance=Sales_Line_Item_strategy)
def test_sales_line_item_Quantity_type(instance):
    assert isinstance(instance.Quantity, int)


@given(instance=Sales_Line_Item_strategy)
def test_sales_line_item_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original
