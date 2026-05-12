import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Shopping_Interface,
    Address,
    Electronic,
    Clothes,
    payment,
    ShippingCart,
    Items,
    Order,
    CustomerInfo,
    RetailStore,
    OnlineShopping,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shopping_interface_is_not_abstract():
    assert not inspect.isabstract(Shopping_Interface)


def test_shopping_interface_constructor_exists():
    assert callable(Shopping_Interface.__init__)


def test_shopping_interface_constructor_args():
    sig = inspect.signature(Shopping_Interface.__init__)
    params = list(sig.parameters.keys())



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "country" in params, "Missing parameter 'country'"
    assert "postalcode" in params, "Missing parameter 'postalcode'"
    assert "street" in params, "Missing parameter 'street'"
    assert "city" in params, "Missing parameter 'city'"

def test_address_has_state():
    assert hasattr(Address, "state")
    descriptor = None
    for klass in Address.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_address_has_country():
    assert hasattr(Address, "country")
    descriptor = None
    for klass in Address.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_address_has_postalcode():
    assert hasattr(Address, "postalcode")
    descriptor = None
    for klass in Address.__mro__:
        if "postalcode" in klass.__dict__:
            descriptor = klass.__dict__["postalcode"]
            break
    assert isinstance(descriptor, property)

def test_address_has_street():
    assert hasattr(Address, "street")
    descriptor = None
    for klass in Address.__mro__:
        if "street" in klass.__dict__:
            descriptor = klass.__dict__["street"]
            break
    assert isinstance(descriptor, property)

def test_address_has_city():
    assert hasattr(Address, "city")
    descriptor = None
    for klass in Address.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_electronic_is_not_abstract():
    assert not inspect.isabstract(Electronic)


def test_electronic_constructor_exists():
    assert callable(Electronic.__init__)


def test_electronic_constructor_args():
    sig = inspect.signature(Electronic.__init__)
    params = list(sig.parameters.keys())
    assert "brand" in params, "Missing parameter 'brand'"

def test_electronic_has_brand():
    assert hasattr(Electronic, "brand")
    descriptor = None
    for klass in Electronic.__mro__:
        if "brand" in klass.__dict__:
            descriptor = klass.__dict__["brand"]
            break
    assert isinstance(descriptor, property)



def test_clothes_is_not_abstract():
    assert not inspect.isabstract(Clothes)


def test_clothes_constructor_exists():
    assert callable(Clothes.__init__)


def test_clothes_constructor_args():
    sig = inspect.signature(Clothes.__init__)
    params = list(sig.parameters.keys())
    assert "typeofclothe" in params, "Missing parameter 'typeofclothe'"
    assert "color" in params, "Missing parameter 'color'"

def test_clothes_has_typeofclothe():
    assert hasattr(Clothes, "typeofclothe")
    descriptor = None
    for klass in Clothes.__mro__:
        if "typeofclothe" in klass.__dict__:
            descriptor = klass.__dict__["typeofclothe"]
            break
    assert isinstance(descriptor, property)

def test_clothes_has_color():
    assert hasattr(Clothes, "color")
    descriptor = None
    for klass in Clothes.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(payment)


def test_payment_constructor_exists():
    assert callable(payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(payment.__init__)
    params = list(sig.parameters.keys())
    assert "cardID" in params, "Missing parameter 'cardID'"
    assert "amount" in params, "Missing parameter 'amount'"

def test_payment_has_cardID():
    assert hasattr(payment, "cardID")
    descriptor = None
    for klass in payment.__mro__:
        if "cardID" in klass.__dict__:
            descriptor = klass.__dict__["cardID"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_amount():
    assert hasattr(payment, "amount")
    descriptor = None
    for klass in payment.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_shippingcart_is_not_abstract():
    assert not inspect.isabstract(ShippingCart)


def test_shippingcart_constructor_exists():
    assert callable(ShippingCart.__init__)


def test_shippingcart_constructor_args():
    sig = inspect.signature(ShippingCart.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"
    assert "productID" in params, "Missing parameter 'productID'"
    assert "cartID" in params, "Missing parameter 'cartID'"

def test_shippingcart_has_quantity():
    assert hasattr(ShippingCart, "quantity")
    descriptor = None
    for klass in ShippingCart.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_shippingcart_has_dateAdded():
    assert hasattr(ShippingCart, "dateAdded")
    descriptor = None
    for klass in ShippingCart.__mro__:
        if "dateAdded" in klass.__dict__:
            descriptor = klass.__dict__["dateAdded"]
            break
    assert isinstance(descriptor, property)

def test_shippingcart_has_productID():
    assert hasattr(ShippingCart, "productID")
    descriptor = None
    for klass in ShippingCart.__mro__:
        if "productID" in klass.__dict__:
            descriptor = klass.__dict__["productID"]
            break
    assert isinstance(descriptor, property)

def test_shippingcart_has_cartID():
    assert hasattr(ShippingCart, "cartID")
    descriptor = None
    for klass in ShippingCart.__mro__:
        if "cartID" in klass.__dict__:
            descriptor = klass.__dict__["cartID"]
            break
    assert isinstance(descriptor, property)



def test_items_is_not_abstract():
    assert not inspect.isabstract(Items)


def test_items_constructor_exists():
    assert callable(Items.__init__)


def test_items_constructor_args():
    sig = inspect.signature(Items.__init__)
    params = list(sig.parameters.keys())
    assert "itemid" in params, "Missing parameter 'itemid'"

def test_items_has_itemid():
    assert hasattr(Items, "itemid")
    descriptor = None
    for klass in Items.__mro__:
        if "itemid" in klass.__dict__:
            descriptor = klass.__dict__["itemid"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "Orderid" in params, "Missing parameter 'Orderid'"
    assert "shippingid" in params, "Missing parameter 'shippingid'"
    assert "shippinddate" in params, "Missing parameter 'shippinddate'"
    assert "statues" in params, "Missing parameter 'statues'"
    assert "customername" in params, "Missing parameter 'customername'"
    assert "customerid" in params, "Missing parameter 'customerid'"
    assert "datecreated" in params, "Missing parameter 'datecreated'"

def test_order_has_Orderid():
    assert hasattr(Order, "Orderid")
    descriptor = None
    for klass in Order.__mro__:
        if "Orderid" in klass.__dict__:
            descriptor = klass.__dict__["Orderid"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shippingid():
    assert hasattr(Order, "shippingid")
    descriptor = None
    for klass in Order.__mro__:
        if "shippingid" in klass.__dict__:
            descriptor = klass.__dict__["shippingid"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shippinddate():
    assert hasattr(Order, "shippinddate")
    descriptor = None
    for klass in Order.__mro__:
        if "shippinddate" in klass.__dict__:
            descriptor = klass.__dict__["shippinddate"]
            break
    assert isinstance(descriptor, property)

def test_order_has_statues():
    assert hasattr(Order, "statues")
    descriptor = None
    for klass in Order.__mro__:
        if "statues" in klass.__dict__:
            descriptor = klass.__dict__["statues"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customername():
    assert hasattr(Order, "customername")
    descriptor = None
    for klass in Order.__mro__:
        if "customername" in klass.__dict__:
            descriptor = klass.__dict__["customername"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customerid():
    assert hasattr(Order, "customerid")
    descriptor = None
    for klass in Order.__mro__:
        if "customerid" in klass.__dict__:
            descriptor = klass.__dict__["customerid"]
            break
    assert isinstance(descriptor, property)

def test_order_has_datecreated():
    assert hasattr(Order, "datecreated")
    descriptor = None
    for klass in Order.__mro__:
        if "datecreated" in klass.__dict__:
            descriptor = klass.__dict__["datecreated"]
            break
    assert isinstance(descriptor, property)



def test_customerinfo_is_not_abstract():
    assert not inspect.isabstract(CustomerInfo)


def test_customerinfo_constructor_exists():
    assert callable(CustomerInfo.__init__)


def test_customerinfo_constructor_args():
    sig = inspect.signature(CustomerInfo.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "shippingaddress" in params, "Missing parameter 'shippingaddress'"
    assert "Cname" in params, "Missing parameter 'Cname'"
    assert "billingaddress" in params, "Missing parameter 'billingaddress'"
    assert "Cid" in params, "Missing parameter 'Cid'"

def test_customerinfo_has_password():
    assert hasattr(CustomerInfo, "password")
    descriptor = None
    for klass in CustomerInfo.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_customerinfo_has_shippingaddress():
    assert hasattr(CustomerInfo, "shippingaddress")
    descriptor = None
    for klass in CustomerInfo.__mro__:
        if "shippingaddress" in klass.__dict__:
            descriptor = klass.__dict__["shippingaddress"]
            break
    assert isinstance(descriptor, property)

def test_customerinfo_has_Cname():
    assert hasattr(CustomerInfo, "Cname")
    descriptor = None
    for klass in CustomerInfo.__mro__:
        if "Cname" in klass.__dict__:
            descriptor = klass.__dict__["Cname"]
            break
    assert isinstance(descriptor, property)

def test_customerinfo_has_billingaddress():
    assert hasattr(CustomerInfo, "billingaddress")
    descriptor = None
    for klass in CustomerInfo.__mro__:
        if "billingaddress" in klass.__dict__:
            descriptor = klass.__dict__["billingaddress"]
            break
    assert isinstance(descriptor, property)

def test_customerinfo_has_Cid():
    assert hasattr(CustomerInfo, "Cid")
    descriptor = None
    for klass in CustomerInfo.__mro__:
        if "Cid" in klass.__dict__:
            descriptor = klass.__dict__["Cid"]
            break
    assert isinstance(descriptor, property)



def test_retailstore_is_not_abstract():
    assert not inspect.isabstract(RetailStore)


def test_retailstore_constructor_exists():
    assert callable(RetailStore.__init__)


def test_retailstore_constructor_args():
    sig = inspect.signature(RetailStore.__init__)
    params = list(sig.parameters.keys())



def test_onlineshopping_is_not_abstract():
    assert not inspect.isabstract(OnlineShopping)


def test_onlineshopping_constructor_exists():
    assert callable(OnlineShopping.__init__)


def test_onlineshopping_constructor_args():
    sig = inspect.signature(OnlineShopping.__init__)
    params = list(sig.parameters.keys())


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
Shopping_Interface_strategy = st.builds(
    Shopping_Interface,
)
Address_strategy = st.builds(
    Address,
    state=
        safe_text,
    country=
        safe_text,
    postalcode=
        safe_text,
    street=
        safe_text,
    city=
        safe_text
)
Electronic_strategy = st.builds(
    Electronic,
    brand=
        safe_text
)
Clothes_strategy = st.builds(
    Clothes,
    typeofclothe=
        safe_text,
    color=
        safe_text
)
payment_strategy = st.builds(
    payment,
    cardID=
        st.integers(),
    amount=
        st.integers()
)
ShippingCart_strategy = st.builds(
    ShippingCart,
    quantity=
        st.integers(),
    dateAdded=
        st.integers(),
    productID=
        st.integers(),
    cartID=
        st.integers()
)
Items_strategy = st.builds(
    Items,
    itemid=
        st.integers()
)
Order_strategy = st.builds(
    Order,
    Orderid=
        st.integers(),
    shippingid=
        st.integers(),
    shippinddate=
        st.integers(),
    statues=
        safe_text,
    customername=
        safe_text,
    customerid=
        st.integers(),
    datecreated=
        st.integers()
)
CustomerInfo_strategy = st.builds(
    CustomerInfo,
    password=
        safe_text,
    shippingaddress=
        safe_text,
    Cname=
        safe_text,
    billingaddress=
        safe_text,
    Cid=
        st.integers()
)
RetailStore_strategy = st.builds(
    RetailStore,
)
OnlineShopping_strategy = st.builds(
    OnlineShopping,
)

@given(instance=Shopping_Interface_strategy)
@settings(max_examples=50)
def test_shopping_interface_instantiation(instance):
    assert isinstance(instance, Shopping_Interface)

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)



@given(instance=Address_strategy)
def test_address_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Address_strategy)
def test_address_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=Address_strategy)
def test_address_postalcode_setter(instance):
    original = instance.postalcode
    instance.postalcode = original
    assert instance.postalcode == original



@given(instance=Address_strategy)
def test_address_street_setter(instance):
    original = instance.street
    instance.street = original
    assert instance.street == original



@given(instance=Address_strategy)
def test_address_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=Electronic_strategy)
@settings(max_examples=50)
def test_electronic_instantiation(instance):
    assert isinstance(instance, Electronic)



@given(instance=Electronic_strategy)
def test_electronic_brand_setter(instance):
    original = instance.brand
    instance.brand = original
    assert instance.brand == original

@given(instance=Clothes_strategy)
@settings(max_examples=50)
def test_clothes_instantiation(instance):
    assert isinstance(instance, Clothes)



@given(instance=Clothes_strategy)
def test_clothes_typeofclothe_setter(instance):
    original = instance.typeofclothe
    instance.typeofclothe = original
    assert instance.typeofclothe == original



@given(instance=Clothes_strategy)
def test_clothes_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, payment)



@given(instance=payment_strategy)
def test_payment_cardID_setter(instance):
    original = instance.cardID
    instance.cardID = original
    assert instance.cardID == original



@given(instance=payment_strategy)
def test_payment_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=ShippingCart_strategy)
@settings(max_examples=50)
def test_shippingcart_instantiation(instance):
    assert isinstance(instance, ShippingCart)



@given(instance=ShippingCart_strategy)
def test_shippingcart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=ShippingCart_strategy)
def test_shippingcart_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original



@given(instance=ShippingCart_strategy)
def test_shippingcart_productID_setter(instance):
    original = instance.productID
    instance.productID = original
    assert instance.productID == original



@given(instance=ShippingCart_strategy)
def test_shippingcart_cartID_setter(instance):
    original = instance.cartID
    instance.cartID = original
    assert instance.cartID == original

@given(instance=Items_strategy)
@settings(max_examples=50)
def test_items_instantiation(instance):
    assert isinstance(instance, Items)



@given(instance=Items_strategy)
def test_items_itemid_setter(instance):
    original = instance.itemid
    instance.itemid = original
    assert instance.itemid == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_Orderid_setter(instance):
    original = instance.Orderid
    instance.Orderid = original
    assert instance.Orderid == original



@given(instance=Order_strategy)
def test_order_shippingid_setter(instance):
    original = instance.shippingid
    instance.shippingid = original
    assert instance.shippingid == original



@given(instance=Order_strategy)
def test_order_shippinddate_setter(instance):
    original = instance.shippinddate
    instance.shippinddate = original
    assert instance.shippinddate == original



@given(instance=Order_strategy)
def test_order_statues_setter(instance):
    original = instance.statues
    instance.statues = original
    assert instance.statues == original



@given(instance=Order_strategy)
def test_order_customername_setter(instance):
    original = instance.customername
    instance.customername = original
    assert instance.customername == original



@given(instance=Order_strategy)
def test_order_customerid_setter(instance):
    original = instance.customerid
    instance.customerid = original
    assert instance.customerid == original



@given(instance=Order_strategy)
def test_order_datecreated_setter(instance):
    original = instance.datecreated
    instance.datecreated = original
    assert instance.datecreated == original

@given(instance=CustomerInfo_strategy)
@settings(max_examples=50)
def test_customerinfo_instantiation(instance):
    assert isinstance(instance, CustomerInfo)



@given(instance=CustomerInfo_strategy)
def test_customerinfo_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=CustomerInfo_strategy)
def test_customerinfo_shippingaddress_setter(instance):
    original = instance.shippingaddress
    instance.shippingaddress = original
    assert instance.shippingaddress == original



@given(instance=CustomerInfo_strategy)
def test_customerinfo_Cname_setter(instance):
    original = instance.Cname
    instance.Cname = original
    assert instance.Cname == original



@given(instance=CustomerInfo_strategy)
def test_customerinfo_billingaddress_setter(instance):
    original = instance.billingaddress
    instance.billingaddress = original
    assert instance.billingaddress == original



@given(instance=CustomerInfo_strategy)
def test_customerinfo_Cid_setter(instance):
    original = instance.Cid
    instance.Cid = original
    assert instance.Cid == original

@given(instance=RetailStore_strategy)
@settings(max_examples=50)
def test_retailstore_instantiation(instance):
    assert isinstance(instance, RetailStore)

@given(instance=OnlineShopping_strategy)
@settings(max_examples=50)
def test_onlineshopping_instantiation(instance):
    assert isinstance(instance, OnlineShopping)
