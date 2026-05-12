import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Payment,
    shippinginfo,
    order,
    orderDetail,
    product,
    cartitem,
    ShoppingCart,
    User,
    Login,
    login_status,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Payment_type" in params, "Missing parameter 'Payment_type'"
    assert "Payment_method" in params, "Missing parameter 'Payment_method'"
    assert "Payment_id" in params, "Missing parameter 'Payment_id'"

def test_payment_has_Payment_type():
    assert hasattr(Payment, "Payment_type")
    descriptor = None
    for klass in Payment.__mro__:
        if "Payment_type" in klass.__dict__:
            descriptor = klass.__dict__["Payment_type"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Payment_method():
    assert hasattr(Payment, "Payment_method")
    descriptor = None
    for klass in Payment.__mro__:
        if "Payment_method" in klass.__dict__:
            descriptor = klass.__dict__["Payment_method"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Payment_id():
    assert hasattr(Payment, "Payment_id")
    descriptor = None
    for klass in Payment.__mro__:
        if "Payment_id" in klass.__dict__:
            descriptor = klass.__dict__["Payment_id"]
            break
    assert isinstance(descriptor, property)



def test_shippinginfo_is_not_abstract():
    assert not inspect.isabstract(shippinginfo)


def test_shippinginfo_constructor_exists():
    assert callable(shippinginfo.__init__)


def test_shippinginfo_constructor_args():
    sig = inspect.signature(shippinginfo.__init__)
    params = list(sig.parameters.keys())
    assert "shipping_type" in params, "Missing parameter 'shipping_type'"
    assert "shipping_date" in params, "Missing parameter 'shipping_date'"
    assert "shipping_cost" in params, "Missing parameter 'shipping_cost'"
    assert "shipping_id" in params, "Missing parameter 'shipping_id'"
    assert "shipping_Address" in params, "Missing parameter 'shipping_Address'"

def test_shippinginfo_has_shipping_type():
    assert hasattr(shippinginfo, "shipping_type")
    descriptor = None
    for klass in shippinginfo.__mro__:
        if "shipping_type" in klass.__dict__:
            descriptor = klass.__dict__["shipping_type"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shipping_date():
    assert hasattr(shippinginfo, "shipping_date")
    descriptor = None
    for klass in shippinginfo.__mro__:
        if "shipping_date" in klass.__dict__:
            descriptor = klass.__dict__["shipping_date"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shipping_cost():
    assert hasattr(shippinginfo, "shipping_cost")
    descriptor = None
    for klass in shippinginfo.__mro__:
        if "shipping_cost" in klass.__dict__:
            descriptor = klass.__dict__["shipping_cost"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shipping_id():
    assert hasattr(shippinginfo, "shipping_id")
    descriptor = None
    for klass in shippinginfo.__mro__:
        if "shipping_id" in klass.__dict__:
            descriptor = klass.__dict__["shipping_id"]
            break
    assert isinstance(descriptor, property)

def test_shippinginfo_has_shipping_Address():
    assert hasattr(shippinginfo, "shipping_Address")
    descriptor = None
    for klass in shippinginfo.__mro__:
        if "shipping_Address" in klass.__dict__:
            descriptor = klass.__dict__["shipping_Address"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(order)


def test_order_constructor_exists():
    assert callable(order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(order.__init__)
    params = list(sig.parameters.keys())
    assert "shippingid" in params, "Missing parameter 'shippingid'"
    assert "status" in params, "Missing parameter 'status'"
    assert "date_created" in params, "Missing parameter 'date_created'"
    assert "order_ID" in params, "Missing parameter 'order_ID'"
    assert "shipping_date" in params, "Missing parameter 'shipping_date'"
    assert "c_name" in params, "Missing parameter 'c_name'"

def test_order_has_shippingid():
    assert hasattr(order, "shippingid")
    descriptor = None
    for klass in order.__mro__:
        if "shippingid" in klass.__dict__:
            descriptor = klass.__dict__["shippingid"]
            break
    assert isinstance(descriptor, property)

def test_order_has_status():
    assert hasattr(order, "status")
    descriptor = None
    for klass in order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_order_has_date_created():
    assert hasattr(order, "date_created")
    descriptor = None
    for klass in order.__mro__:
        if "date_created" in klass.__dict__:
            descriptor = klass.__dict__["date_created"]
            break
    assert isinstance(descriptor, property)

def test_order_has_order_ID():
    assert hasattr(order, "order_ID")
    descriptor = None
    for klass in order.__mro__:
        if "order_ID" in klass.__dict__:
            descriptor = klass.__dict__["order_ID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shipping_date():
    assert hasattr(order, "shipping_date")
    descriptor = None
    for klass in order.__mro__:
        if "shipping_date" in klass.__dict__:
            descriptor = klass.__dict__["shipping_date"]
            break
    assert isinstance(descriptor, property)

def test_order_has_c_name():
    assert hasattr(order, "c_name")
    descriptor = None
    for klass in order.__mro__:
        if "c_name" in klass.__dict__:
            descriptor = klass.__dict__["c_name"]
            break
    assert isinstance(descriptor, property)



def test_orderdetail_is_not_abstract():
    assert not inspect.isabstract(orderDetail)


def test_orderdetail_constructor_exists():
    assert callable(orderDetail.__init__)


def test_orderdetail_constructor_args():
    sig = inspect.signature(orderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "productid" in params, "Missing parameter 'productid'"
    assert "productname" in params, "Missing parameter 'productname'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "subtotall" in params, "Missing parameter 'subtotall'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "orderId" in params, "Missing parameter 'orderId'"

def test_orderdetail_has_productid():
    assert hasattr(orderDetail, "productid")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
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

def test_orderdetail_has_quantity():
    assert hasattr(orderDetail, "quantity")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_orderdetail_has_orderId():
    assert hasattr(orderDetail, "orderId")
    descriptor = None
    for klass in orderDetail.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(product)


def test_product_constructor_exists():
    assert callable(product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(product.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "productid" in params, "Missing parameter 'productid'"
    assert "productname" in params, "Missing parameter 'productname'"
    assert "imagefilename" in params, "Missing parameter 'imagefilename'"

def test_product_has_price():
    assert hasattr(product, "price")
    descriptor = None
    for klass in product.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_product_has_productid():
    assert hasattr(product, "productid")
    descriptor = None
    for klass in product.__mro__:
        if "productid" in klass.__dict__:
            descriptor = klass.__dict__["productid"]
            break
    assert isinstance(descriptor, property)

def test_product_has_productname():
    assert hasattr(product, "productname")
    descriptor = None
    for klass in product.__mro__:
        if "productname" in klass.__dict__:
            descriptor = klass.__dict__["productname"]
            break
    assert isinstance(descriptor, property)

def test_product_has_imagefilename():
    assert hasattr(product, "imagefilename")
    descriptor = None
    for klass in product.__mro__:
        if "imagefilename" in klass.__dict__:
            descriptor = klass.__dict__["imagefilename"]
            break
    assert isinstance(descriptor, property)



def test_cartitem_is_not_abstract():
    assert not inspect.isabstract(cartitem)


def test_cartitem_constructor_exists():
    assert callable(cartitem.__init__)


def test_cartitem_constructor_args():
    sig = inspect.signature(cartitem.__init__)
    params = list(sig.parameters.keys())
    assert "subtotal" in params, "Missing parameter 'subtotal'"
    assert "unitcost" in params, "Missing parameter 'unitcost'"
    assert "product" in params, "Missing parameter 'product'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "name" in params, "Missing parameter 'name'"

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

def test_cartitem_has_product():
    assert hasattr(cartitem, "product")
    descriptor = None
    for klass in cartitem.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)

def test_cartitem_has_quantity():
    assert hasattr(cartitem, "quantity")
    descriptor = None
    for klass in cartitem.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_cartitem_has_name():
    assert hasattr(cartitem, "name")
    descriptor = None
    for klass in cartitem.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "productId" in params, "Missing parameter 'productId'"
    assert "cartId" in params, "Missing parameter 'cartId'"
    assert "dateAdded" in params, "Missing parameter 'dateAdded'"

def test_shoppingcart_has_quantity():
    assert hasattr(ShoppingCart, "quantity")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
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

def test_shoppingcart_has_cartId():
    assert hasattr(ShoppingCart, "cartId")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "cartId" in klass.__dict__:
            descriptor = klass.__dict__["cartId"]
            break
    assert isinstance(descriptor, property)

def test_shoppingcart_has_dateAdded():
    assert hasattr(ShoppingCart, "dateAdded")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "dateAdded" in klass.__dict__:
            descriptor = klass.__dict__["dateAdded"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"
    assert "User_name" in params, "Missing parameter 'User_name'"
    assert "phone_no" in params, "Missing parameter 'phone_no'"
    assert "Card_info" in params, "Missing parameter 'Card_info'"
    assert "shipping_info" in params, "Missing parameter 'shipping_info'"

def test_user_has_email():
    assert hasattr(User, "email")
    descriptor = None
    for klass in User.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_user_has_address():
    assert hasattr(User, "address")
    descriptor = None
    for klass in User.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_user_has_User_name():
    assert hasattr(User, "User_name")
    descriptor = None
    for klass in User.__mro__:
        if "User_name" in klass.__dict__:
            descriptor = klass.__dict__["User_name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_phone_no():
    assert hasattr(User, "phone_no")
    descriptor = None
    for klass in User.__mro__:
        if "phone_no" in klass.__dict__:
            descriptor = klass.__dict__["phone_no"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Card_info():
    assert hasattr(User, "Card_info")
    descriptor = None
    for klass in User.__mro__:
        if "Card_info" in klass.__dict__:
            descriptor = klass.__dict__["Card_info"]
            break
    assert isinstance(descriptor, property)

def test_user_has_shipping_info():
    assert hasattr(User, "shipping_info")
    descriptor = None
    for klass in User.__mro__:
        if "shipping_info" in klass.__dict__:
            descriptor = klass.__dict__["shipping_info"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "UserId" in params, "Missing parameter 'UserId'"
    assert "password" in params, "Missing parameter 'password'"
    assert "login_status" in params, "Missing parameter 'login_status'"

def test_login_has_UserId():
    assert hasattr(Login, "UserId")
    descriptor = None
    for klass in Login.__mro__:
        if "UserId" in klass.__dict__:
            descriptor = klass.__dict__["UserId"]
            break
    assert isinstance(descriptor, property)

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_login_status():
    assert hasattr(Login, "login_status")
    descriptor = None
    for klass in Login.__mro__:
        if "login_status" in klass.__dict__:
            descriptor = klass.__dict__["login_status"]
            break
    assert isinstance(descriptor, property)

def test_login_status_exists():
    # Check that the Enumeration exists
    assert login_status is not None

def test_login_status_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in login_status]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in login_status"


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
Payment_strategy = st.builds(
    Payment,
    Payment_type=
        safe_text,
    Payment_method=
        st.integers(),
    Payment_id=
        safe_text
)
shippinginfo_strategy = st.builds(
    shippinginfo,
    shipping_type=
        safe_text,
    shipping_date=
        st.dates(),
    shipping_cost=
        st.integers(),
    shipping_id=
        safe_text,
    shipping_Address=
        safe_text
)
order_strategy = st.builds(
    order,
    shippingid=
        safe_text,
    status=
        safe_text,
    date_created=
        st.dates(),
    order_ID=
        st.integers(),
    shipping_date=
        st.dates(),
    c_name=
        safe_text
)
orderDetail_strategy = st.builds(
    orderDetail,
    productid=
        st.integers(),
    productname=
        safe_text,
    unitcost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    subtotall=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    quantity=
        st.integers(),
    orderId=
        st.integers()
)
product_strategy = st.builds(
    product,
    price=
        st.integers(),
    productid=
        st.integers(),
    productname=
        safe_text,
    imagefilename=
        safe_text
)
cartitem_strategy = st.builds(
    cartitem,
    subtotal=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    unitcost=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    product=
        st.integers(),
    quantity=
        st.integers(),
    name=
        safe_text
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    quantity=
        st.integers(),
    productId=
        st.integers(),
    cartId=
        st.integers(),
    dateAdded=
        st.integers()
)
User_strategy = st.builds(
    User,
    email=
        safe_text,
    address=
        safe_text,
    User_name=
        safe_text,
    phone_no=
        st.integers(),
    Card_info=
        safe_text,
    shipping_info=
        safe_text
)
Login_strategy = st.builds(
    Login,
    UserId=
        safe_text,
    password=
        safe_text,
    login_status=
        safe_text
)

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Payment_type_setter(instance):
    original = instance.Payment_type
    instance.Payment_type = original
    assert instance.Payment_type == original



@given(instance=Payment_strategy)
def test_payment_Payment_method_setter(instance):
    original = instance.Payment_method
    instance.Payment_method = original
    assert instance.Payment_method == original



@given(instance=Payment_strategy)
def test_payment_Payment_id_setter(instance):
    original = instance.Payment_id
    instance.Payment_id = original
    assert instance.Payment_id == original

@given(instance=shippinginfo_strategy)
@settings(max_examples=50)
def test_shippinginfo_instantiation(instance):
    assert isinstance(instance, shippinginfo)



@given(instance=shippinginfo_strategy)
def test_shippinginfo_shipping_type_setter(instance):
    original = instance.shipping_type
    instance.shipping_type = original
    assert instance.shipping_type == original



@given(instance=shippinginfo_strategy)
def test_shippinginfo_shipping_date_setter(instance):
    original = instance.shipping_date
    instance.shipping_date = original
    assert instance.shipping_date == original



@given(instance=shippinginfo_strategy)
def test_shippinginfo_shipping_cost_setter(instance):
    original = instance.shipping_cost
    instance.shipping_cost = original
    assert instance.shipping_cost == original



@given(instance=shippinginfo_strategy)
def test_shippinginfo_shipping_id_setter(instance):
    original = instance.shipping_id
    instance.shipping_id = original
    assert instance.shipping_id == original



@given(instance=shippinginfo_strategy)
def test_shippinginfo_shipping_Address_setter(instance):
    original = instance.shipping_Address
    instance.shipping_Address = original
    assert instance.shipping_Address == original

@given(instance=order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, order)



@given(instance=order_strategy)
def test_order_shippingid_setter(instance):
    original = instance.shippingid
    instance.shippingid = original
    assert instance.shippingid == original



@given(instance=order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=order_strategy)
def test_order_date_created_setter(instance):
    original = instance.date_created
    instance.date_created = original
    assert instance.date_created == original



@given(instance=order_strategy)
def test_order_order_ID_setter(instance):
    original = instance.order_ID
    instance.order_ID = original
    assert instance.order_ID == original



@given(instance=order_strategy)
def test_order_shipping_date_setter(instance):
    original = instance.shipping_date
    instance.shipping_date = original
    assert instance.shipping_date == original



@given(instance=order_strategy)
def test_order_c_name_setter(instance):
    original = instance.c_name
    instance.c_name = original
    assert instance.c_name == original

@given(instance=orderDetail_strategy)
@settings(max_examples=50)
def test_orderdetail_instantiation(instance):
    assert isinstance(instance, orderDetail)



@given(instance=orderDetail_strategy)
def test_orderdetail_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=orderDetail_strategy)
def test_orderdetail_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original



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



@given(instance=orderDetail_strategy)
def test_orderdetail_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=orderDetail_strategy)
def test_orderdetail_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original

@given(instance=product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, product)



@given(instance=product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=product_strategy)
def test_product_productid_setter(instance):
    original = instance.productid
    instance.productid = original
    assert instance.productid == original



@given(instance=product_strategy)
def test_product_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original



@given(instance=product_strategy)
def test_product_imagefilename_setter(instance):
    original = instance.imagefilename
    instance.imagefilename = original
    assert instance.imagefilename == original

@given(instance=cartitem_strategy)
@settings(max_examples=50)
def test_cartitem_instantiation(instance):
    assert isinstance(instance, cartitem)



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
def test_cartitem_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original



@given(instance=cartitem_strategy)
def test_cartitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=cartitem_strategy)
def test_cartitem_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_productId_setter(instance):
    original = instance.productId
    instance.productId = original
    assert instance.productId == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_cartId_setter(instance):
    original = instance.cartId
    instance.cartId = original
    assert instance.cartId == original



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_dateAdded_setter(instance):
    original = instance.dateAdded
    instance.dateAdded = original
    assert instance.dateAdded == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=User_strategy)
def test_user_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=User_strategy)
def test_user_User_name_setter(instance):
    original = instance.User_name
    instance.User_name = original
    assert instance.User_name == original



@given(instance=User_strategy)
def test_user_phone_no_setter(instance):
    original = instance.phone_no
    instance.phone_no = original
    assert instance.phone_no == original



@given(instance=User_strategy)
def test_user_Card_info_setter(instance):
    original = instance.Card_info
    instance.Card_info = original
    assert instance.Card_info == original



@given(instance=User_strategy)
def test_user_shipping_info_setter(instance):
    original = instance.shipping_info
    instance.shipping_info = original
    assert instance.shipping_info == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_UserId_setter(instance):
    original = instance.UserId
    instance.UserId = original
    assert instance.UserId == original



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_login_status_setter(instance):
    original = instance.login_status
    instance.login_status = original
    assert instance.login_status == original
