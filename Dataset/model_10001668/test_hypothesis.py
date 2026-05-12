import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    Inventory,
    Product,
    Payment,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_inventory_is_not_abstract():
    assert not inspect.isabstract(Inventory)


def test_inventory_constructor_exists():
    assert callable(Inventory.__init__)


def test_inventory_constructor_args():
    sig = inspect.signature(Inventory.__init__)
    params = list(sig.parameters.keys())
    assert "list" in params, "Missing parameter 'list'"
    assert "SuperMarket" in params, "Missing parameter 'SuperMarket'"

def test_inventory_has_list():
    assert hasattr(Inventory, "list")
    descriptor = None
    for klass in Inventory.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)

def test_inventory_has_SuperMarket():
    assert hasattr(Inventory, "SuperMarket")
    descriptor = None
    for klass in Inventory.__mro__:
        if "SuperMarket" in klass.__dict__:
            descriptor = klass.__dict__["SuperMarket"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "qty" in params, "Missing parameter 'qty'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "amount" in params, "Missing parameter 'amount'"
    assert "blgl" in params, "Missing parameter 'blgl'"
    assert "price" in params, "Missing parameter 'price'"
    assert "type" in params, "Missing parameter 'type'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_product_has_qty():
    assert hasattr(Product, "qty")
    descriptor = None
    for klass in Product.__mro__:
        if "qty" in klass.__dict__:
            descriptor = klass.__dict__["qty"]
            break
    assert isinstance(descriptor, property)

def test_product_has_ID():
    assert hasattr(Product, "ID")
    descriptor = None
    for klass in Product.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_product_has_amount():
    assert hasattr(Product, "amount")
    descriptor = None
    for klass in Product.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_product_has_blgl():
    assert hasattr(Product, "blgl")
    descriptor = None
    for klass in Product.__mro__:
        if "blgl" in klass.__dict__:
            descriptor = klass.__dict__["blgl"]
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

def test_product_has_type():
    assert hasattr(Product, "type")
    descriptor = None
    for klass in Product.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_product_has_attribute():
    assert hasattr(Product, "attribute")
    descriptor = None
    for klass in Product.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_product_has_Name():
    assert hasattr(Product, "Name")
    descriptor = None
    for klass in Product.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "discountamount" in params, "Missing parameter 'discountamount'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Imtiaz" in params, "Missing parameter 'Imtiaz'"
    assert "finalamount" in params, "Missing parameter 'finalamount'"
    assert "amount__" in params, "Missing parameter 'amount__'"
    assert "totalamount" in params, "Missing parameter 'totalamount'"
    assert "list" in params, "Missing parameter 'list'"

def test_payment_has_discountamount():
    assert hasattr(Payment, "discountamount")
    descriptor = None
    for klass in Payment.__mro__:
        if "discountamount" in klass.__dict__:
            descriptor = klass.__dict__["discountamount"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_quantity():
    assert hasattr(Payment, "quantity")
    descriptor = None
    for klass in Payment.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_ID():
    assert hasattr(Payment, "ID")
    descriptor = None
    for klass in Payment.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Imtiaz():
    assert hasattr(Payment, "Imtiaz")
    descriptor = None
    for klass in Payment.__mro__:
        if "Imtiaz" in klass.__dict__:
            descriptor = klass.__dict__["Imtiaz"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_finalamount():
    assert hasattr(Payment, "finalamount")
    descriptor = None
    for klass in Payment.__mro__:
        if "finalamount" in klass.__dict__:
            descriptor = klass.__dict__["finalamount"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_amount__():
    assert hasattr(Payment, "amount__")
    descriptor = None
    for klass in Payment.__mro__:
        if "amount__" in klass.__dict__:
            descriptor = klass.__dict__["amount__"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_totalamount():
    assert hasattr(Payment, "totalamount")
    descriptor = None
    for klass in Payment.__mro__:
        if "totalamount" in klass.__dict__:
            descriptor = klass.__dict__["totalamount"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_list():
    assert hasattr(Payment, "list")
    descriptor = None
    for klass in Payment.__mro__:
        if "list" in klass.__dict__:
            descriptor = klass.__dict__["list"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "royalty" in params, "Missing parameter 'royalty'"

def test_customer_has_type():
    assert hasattr(Customer, "type")
    descriptor = None
    for klass in Customer.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_royalty():
    assert hasattr(Customer, "royalty")
    descriptor = None
    for klass in Customer.__mro__:
        if "royalty" in klass.__dict__:
            descriptor = klass.__dict__["royalty"]
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
Inventory_strategy = st.builds(
    Inventory,
    list=
        safe_text,
    SuperMarket=
        safe_text
)
Product_strategy = st.builds(
    Product,
    qty=
        st.integers(),
    ID=
        st.integers(),
    amount=
        safe_text,
    blgl=
        st.booleans(),
    price=
        safe_text,
    type=
        safe_text,
    attribute=
        safe_text,
    Name=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    discountamount=
        safe_text,
    quantity=
        st.integers(),
    ID=
        st.integers(),
    Imtiaz=
        safe_text,
    finalamount=
        safe_text,
    amount__=
        safe_text,
    totalamount=
        safe_text,
    list=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    type=
        safe_text,
    royalty=
        st.booleans()
)

@given(instance=Inventory_strategy)
@settings(max_examples=50)
def test_inventory_instantiation(instance):
    assert isinstance(instance, Inventory)

@given(instance=Inventory_strategy)
def test_inventory_list_type(instance):
    assert isinstance(instance.list, str)


@given(instance=Inventory_strategy)
def test_inventory_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=Inventory_strategy)
def test_inventory_SuperMarket_type(instance):
    assert isinstance(instance.SuperMarket, str)


@given(instance=Inventory_strategy)
def test_inventory_SuperMarket_setter(instance):
    original = instance.SuperMarket
    instance.SuperMarket = original
    assert instance.SuperMarket == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)

@given(instance=Product_strategy)
def test_product_qty_type(instance):
    assert isinstance(instance.qty, int)


@given(instance=Product_strategy)
def test_product_qty_setter(instance):
    original = instance.qty
    instance.qty = original
    assert instance.qty == original

@given(instance=Product_strategy)
def test_product_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=Product_strategy)
def test_product_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Product_strategy)
def test_product_amount_type(instance):
    assert isinstance(instance.amount, str)


@given(instance=Product_strategy)
def test_product_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Product_strategy)
def test_product_blgl_type(instance):
    assert isinstance(instance.blgl, bool)


@given(instance=Product_strategy)
def test_product_blgl_setter(instance):
    original = instance.blgl
    instance.blgl = original
    assert instance.blgl == original

@given(instance=Product_strategy)
def test_product_price_type(instance):
    assert isinstance(instance.price, str)


@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Product_strategy)
def test_product_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Product_strategy)
def test_product_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Product_strategy)
def test_product_attribute_type(instance):
    assert isinstance(instance.attribute, str)


@given(instance=Product_strategy)
def test_product_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Product_strategy)
def test_product_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=Product_strategy)
def test_product_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)

@given(instance=Payment_strategy)
def test_payment_discountamount_type(instance):
    assert isinstance(instance.discountamount, str)


@given(instance=Payment_strategy)
def test_payment_discountamount_setter(instance):
    original = instance.discountamount
    instance.discountamount = original
    assert instance.discountamount == original

@given(instance=Payment_strategy)
def test_payment_quantity_type(instance):
    assert isinstance(instance.quantity, int)


@given(instance=Payment_strategy)
def test_payment_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Payment_strategy)
def test_payment_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=Payment_strategy)
def test_payment_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=Payment_strategy)
def test_payment_Imtiaz_type(instance):
    assert isinstance(instance.Imtiaz, str)


@given(instance=Payment_strategy)
def test_payment_Imtiaz_setter(instance):
    original = instance.Imtiaz
    instance.Imtiaz = original
    assert instance.Imtiaz == original

@given(instance=Payment_strategy)
def test_payment_finalamount_type(instance):
    assert isinstance(instance.finalamount, str)


@given(instance=Payment_strategy)
def test_payment_finalamount_setter(instance):
    original = instance.finalamount
    instance.finalamount = original
    assert instance.finalamount == original

@given(instance=Payment_strategy)
def test_payment_amount___type(instance):
    assert isinstance(instance.amount__, str)


@given(instance=Payment_strategy)
def test_payment_amount___setter(instance):
    original = instance.amount__
    instance.amount__ = original
    assert instance.amount__ == original

@given(instance=Payment_strategy)
def test_payment_totalamount_type(instance):
    assert isinstance(instance.totalamount, str)


@given(instance=Payment_strategy)
def test_payment_totalamount_setter(instance):
    original = instance.totalamount
    instance.totalamount = original
    assert instance.totalamount == original

@given(instance=Payment_strategy)
def test_payment_list_type(instance):
    assert isinstance(instance.list, str)


@given(instance=Payment_strategy)
def test_payment_list_setter(instance):
    original = instance.list
    instance.list = original
    assert instance.list == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=Customer_strategy)
def test_customer_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Customer_strategy)
def test_customer_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Customer_strategy)
def test_customer_royalty_type(instance):
    assert isinstance(instance.royalty, bool)


@given(instance=Customer_strategy)
def test_customer_royalty_setter(instance):
    original = instance.royalty
    instance.royalty = original
    assert instance.royalty == original
