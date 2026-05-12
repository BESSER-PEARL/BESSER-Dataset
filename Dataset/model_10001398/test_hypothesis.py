import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    shippinginfo,
    order,
    orderDetail,
    product,
    cartitem,
    ShoppingCart,
    coustomer,
    user,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(shippinginfo)


def test_shippinginfo_constructor_exists():
    assert callable(shippinginfo.__init__)


def test_shippinginfo_constructor_args():
    sig = inspect.signature(shippinginfo.__init__)
    params = list(sig.parameters.keys())
    assert "shippingcost" in params, "Missing parameter 'shippingcost'"
    assert "shippingId" in params, "Missing parameter 'shippingId'"

def test_shippinginfo_has_shippingcost():
    assert hasattr(shippinginfo, "shippingcost")
    descriptor = None
    for klass in shippinginfo.__mro__:
        if "shippingcost" in klass.__dict__:
            descriptor = klass.__dict__["shippingcost"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shippingId():
    assert hasattr(shippinginfo, "shippingId")
    descriptor = None
    for klass in shippinginfo.__mro__:
        if "shippingId" in klass.__dict__:
            descriptor = klass.__dict__["shippingId"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(order)


def test_order_constructor_exists():
    assert callable(order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(order.__init__)
    params = list(sig.parameters.keys())
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "name" in params, "Missing parameter 'name'"
    assert "datecreated" in params, "Missing parameter 'datecreated'"
    assert "shippingid" in params, "Missing parameter 'shippingid'"
    assert "customerid" in params, "Missing parameter 'customerid'"

def test_order_has_orderId():
    assert hasattr(order, "orderId")
    descriptor = None
    for klass in order.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_order_has_name():
    assert hasattr(order, "name")
    descriptor = None
    for klass in order.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_order_has_datecreated():
    assert hasattr(order, "datecreated")
    descriptor = None
    for klass in order.__mro__:
        if "datecreated" in klass.__dict__:
            descriptor = klass.__dict__["datecreated"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shippingid():
    assert hasattr(order, "shippingid")
    descriptor = None
    for klass in order.__mro__:
        if "shippingid" in klass.__dict__:
            descriptor = klass.__dict__["shippingid"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customerid():
    assert hasattr(order, "customerid")
    descriptor = None
    for klass in order.__mro__:
        if "customerid" in klass.__dict__:
            descriptor = klass.__dict__["customerid"]
            break
    assert isinstance(descriptor, property)



def test_orderdetail_is_not_abstract():
    assert not inspect.isabstract(orderDetail)


def test_orderdetail_constructor_exists():
    assert callable(orderDetail.__init__)


def test_orderdetail_constructor_args():
    sig = inspect.signature(orderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "productname" in params, "Missing parameter 'productname'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "productid" in params, "Missing parameter 'productid'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "subtotall" in params, "Missing parameter 'subtotall'"

def test_orderdetail_has_orderId():
    assert hasattr(orderDetail, "orderId")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_productname():
    assert hasattr(orderDetail, "productname")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "productname" in klass.__dict__:
            descriptor = klass.__dict__["productname"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_quantity():
    assert hasattr(orderDetail, "quantity")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_productid():
    assert hasattr(orderDetail, "productid")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_unitcost():
    assert hasattr(orderDetail, "unitcost")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "unitcost" in klass.__dict__:
            descriptor = klass.__dict__["unitcost"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_subtotall():
    assert hasattr(orderDetail, "subtotall")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "subtotall" in klass.__dict__:
            descriptor = klass.__dict__["subtotall"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(product)


def test_product_constructor_exists():
    assert callable(product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(product.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "name" in params, "Missing parameter 'name'"
    assert "price" in params, "Missing parameter 'price'"
    assert "image" in params, "Missing parameter 'image'"
    assert "productId" in params, "Missing parameter 'productId'"

def test_product_has_description():
    assert hasattr(product, "description")
    descriptor = None
    for klass in product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_product_has_name():
    assert hasattr(product, "name")
    descriptor = None
    for klass in product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_product_has_price():
    assert hasattr(product, "price")
    descriptor = None
    for klass in product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_product_has_image():
    assert hasattr(product, "image")
    descriptor = None
    for klass in product.__mro__:
        if "image" in klass.__dict__:
            descriptor = klass.__dict__["image"]
            break
    assert isinstance(descriptor, property)

def test_product_has_productId():
    assert hasattr(product, "productId")
    descriptor = None
    for klass in product.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)



def test_cartitem_is_not_abstract():
    assert not inspect.isabstract(cartitem)


def test_cartitem_constructor_exists():
    assert callable(cartitem.__init__)


def test_cartitem_constructor_args():
    sig = inspect.signature(cartitem.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "subtotal" in params, "Missing parameter 'subtotal'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "productId" in params, "Missing parameter 'productId'"

def test_cartitem_has_quantity():
    assert hasattr(cartitem, "quantity")
    descriptor = None
    for klass in cartitem.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_cartitem_has_subtotal():
    assert hasattr(cartitem, "subtotal")
    descriptor = None
    for klass in cartitem.__mro__:
        if "subtotal" in klass.__dict__:
            descriptor = klass.__dict__["subtotal"]
            break
    assert isinstance(descriptor, property)

def test_cartitem_has_unitcost():
    assert hasattr(cartitem, "unitcost")
    descriptor = None
    for klass in cartitem.__mro__:
        if "unitcost" in klass.__dict__:
            descriptor = klass.__dict__["unitcost"]
            break
    assert isinstance(descriptor, property)

def test_cartitem_has_productId():
    assert hasattr(cartitem, "productId")
    descriptor = None
    for klass in cartitem.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"
    assert "cartId" in params, "Missing parameter 'cartId'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_shoppingcart_has_dateAdded():
    assert hasattr(ShoppingCart, "dateAdded")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "dateAdded" in klass.__dict__:
            descriptor = klass.__dict__["dateAdded"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_cartId():
    assert hasattr(ShoppingCart, "cartId")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "cartId" in klass.__dict__:
            descriptor = klass.__dict__["cartId"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_productId():
    assert hasattr(ShoppingCart, "productId")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "productId" in klass.__dict__:
            descriptor = klass.__dict__["productId"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_quantity():
    assert hasattr(ShoppingCart, "quantity")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_coustomer_is_not_abstract():
    assert not inspect.isabstract(coustomer)


def test_coustomer_constructor_exists():
    assert callable(coustomer.__init__)


def test_coustomer_constructor_args():
    sig = inspect.signature(coustomer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "shippinginfo" in params, "Missing parameter 'shippinginfo'"
    assert "customerId" in params, "Missing parameter 'customerId'"
    assert "email" in params, "Missing parameter 'email'"
    assert "phoneno" in params, "Missing parameter 'phoneno'"
    assert "address" in params, "Missing parameter 'address'"

def test_coustomer_has_name():
    assert hasattr(coustomer, "name")
    descriptor = None
    for klass in coustomer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_coustomer_has_shippinginfo():
    assert hasattr(coustomer, "shippinginfo")
    descriptor = None
    for klass in coustomer.__mro__:
        if "shippinginfo" in klass.__dict__:
            descriptor = klass.__dict__["shippinginfo"]
            break
    assert isinstance(descriptor, property)

def test_coustomer_has_customerId():
    assert hasattr(coustomer, "customerId")
    descriptor = None
    for klass in coustomer.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)

def test_coustomer_has_email():
    assert hasattr(coustomer, "email")
    descriptor = None
    for klass in coustomer.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_coustomer_has_phoneno():
    assert hasattr(coustomer, "phoneno")
    descriptor = None
    for klass in coustomer.__mro__:
        if "phoneno" in klass.__dict__:
            descriptor = klass.__dict__["phoneno"]
            break
    assert isinstance(descriptor, property)

def test_coustomer_has_address():
    assert hasattr(coustomer, "address")
    descriptor = None
    for klass in coustomer.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_user_constructor_exists():
    assert callable(user.__init__)


def test_user_constructor_args():
    sig = inspect.signature(user.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "password" in params, "Missing parameter 'password'"
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "loginstatus" in params, "Missing parameter 'loginstatus'"

def test_user_has_email():
    assert hasattr(user, "email")
    descriptor = None
    for klass in user.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(user, "password")
    descriptor = None
    for klass in user.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_UserId():
    assert hasattr(user, "UserId")
    descriptor = None
    for klass in user.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_user_has_loginstatus():
    assert hasattr(user, "loginstatus")
    descriptor = None
    for klass in user.__mro__:
        if "loginstatus" in klass.__dict__:
            descriptor = klass.__dict__["loginstatus"]
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
shippinginfo_strategy = st.builds(
    shippinginfo,
    shippingcost=
        st.integers(),
    shippingId=
        st.integers()
)
order_strategy = st.builds(
    order,
    orderId=
        st.integers(),
    name=
        safe_text,
    datecreated=
        safe_text,
    shippingid=
        safe_text,
    customerid=
        st.integers()
)
orderDetail_strategy = st.builds(
    orderDetail,
    orderId=
        st.integers(),
    productname=
        safe_text,
    quantity=
        st.integers(),
    productid=
        st.integers(),
    unitcost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    subtotall=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
product_strategy = st.builds(
    product,
    description=
        safe_text,
    name=
        safe_text,
    price=
        st.integers(),
    image=
        safe_text,
    productId=
        st.integers()
)
cartitem_strategy = st.builds(
    cartitem,
    quantity=
        st.integers(),
    subtotal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    unitcost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    productId=
        st.integers()
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    dateAdded=
        st.integers(),
    cartId=
        st.integers(),
    productId=
        st.integers(),
    quantity=
        st.integers()
)
coustomer_strategy = st.builds(
    coustomer,
    name=
        safe_text,
    shippinginfo=
        safe_text,
    customerId=
        st.integers(),
    email=
        safe_text,
    phoneno=
        st.integers(),
    address=
        safe_text
)
user_strategy = st.builds(
    user,
    email=
        safe_text,
    password=
        safe_text,
    UserId=
        st.integers(),
    loginstatus=
        safe_text
)

@given(instance=shippinginfo_strategy)
@settings(max_examples=50)
def test_shippinginfo_instantiation(instance):
    assert isinstance(instance, shippinginfo)



@given(instance=shippinginfo_strategy)
def test_shippinginfo_shippingcost_setter(instance):
    original = instance.shippingcost
    instance.shippingcost = original
    assert instance.shippingcost == original



@given(instance=shippinginfo_strategy)
def test_shippinginfo_shippingId_setter(instance):
    original = instance.shippingId
    instance.shippingId = original
    assert instance.shippingId == original

@given(instance=order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, order)



@given(instance=order_strategy)
def test_order_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original



@given(instance=order_strategy)
def test_order_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=order_strategy)
def test_order_datecreated_setter(instance):
    original = instance.datecreated
    instance.datecreated = original
    assert instance.datecreated == original



@given(instance=order_strategy)
def test_order_shippingid_setter(instance):
    original = instance.shippingid
    instance.shippingid = original
    assert instance.shippingid == original



@given(instance=order_strategy)
def test_order_customerid_setter(instance):
    original = instance.customerid
    instance.customerid = original
    assert instance.customerid == original

@given(instance=orderDetail_strategy)
@settings(max_examples=50)
def test_orderdetail_instantiation(instance):
    assert isinstance(instance, orderDetail)



@given(instance=orderDetail_strategy)
def test_orderdetail_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original



@given(instance=orderDetail_strategy)
def test_orderdetail_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original



@given(instance=orderDetail_strategy)
def test_orderdetail_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=orderDetail_strategy)
def test_orderdetail_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=orderDetail_strategy)
def test_orderdetail_unitcost_setter(instance):
    original = instance.unitcost
    instance.unitcost = original
    assert instance.unitcost == original



@given(instance=orderDetail_strategy)
def test_orderdetail_subtotall_setter(instance):
    original = instance.subtotall
    instance.subtotall = original
    assert instance.subtotall == original

@given(instance=product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, product)



@given(instance=product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=product_strategy)
def test_product_image_setter(instance):
    original = instance.image
    instance.image = original
    assert instance.image == original



@given(instance=product_strategy)
def test_product_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original

@given(instance=cartitem_strategy)
@settings(max_examples=50)
def test_cartitem_instantiation(instance):
    assert isinstance(instance, cartitem)



@given(instance=cartitem_strategy)
def test_cartitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=cartitem_strategy)
def test_cartitem_subtotal_setter(instance):
    original = instance.subtotal
    instance.subtotal = original
    assert instance.subtotal == original



@given(instance=cartitem_strategy)
def test_cartitem_unitcost_setter(instance):
    original = instance.unitcost
    instance.unitcost = original
    assert instance.unitcost == original



@given(instance=cartitem_strategy)
def test_cartitem_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=coustomer_strategy)
@settings(max_examples=50)
def test_coustomer_instantiation(instance):
    assert isinstance(instance, coustomer)



@given(instance=coustomer_strategy)
def test_coustomer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=coustomer_strategy)
def test_coustomer_shippinginfo_setter(instance):
    original = instance.shippinginfo
    instance.shippinginfo = original
    assert instance.shippinginfo == original



@given(instance=coustomer_strategy)
def test_coustomer_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original



@given(instance=coustomer_strategy)
def test_coustomer_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=coustomer_strategy)
def test_coustomer_phoneno_setter(instance):
    original = instance.phoneno
    instance.phoneno = original
    assert instance.phoneno == original



@given(instance=coustomer_strategy)
def test_coustomer_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=user_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, user)



@given(instance=user_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=user_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=user_strategy)
def test_user_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=user_strategy)
def test_user_loginstatus_setter(instance):
    original = instance.loginstatus
    instance.loginstatus = original
    assert instance.loginstatus == original
