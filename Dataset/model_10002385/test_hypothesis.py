import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer,
    User,
    Payment,
    Bookstore_Shop,
    Order,
    BookSet,
    Search,
    Shopping_Cart,
    Admin,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "customerPhone" in params, "Missing parameter 'customerPhone'"
    assert "customerId" in params, "Missing parameter 'customerId'"
    assert "customerPaymentInfo" in params, "Missing parameter 'customerPaymentInfo'"
    assert "customerName" in params, "Missing parameter 'customerName'"
    assert "customerAddress" in params, "Missing parameter 'customerAddress'"

def test_customer_has_customerPhone():
    assert hasattr(Customer, "customerPhone")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerPhone" in klass.__dict__:
            descriptor = klass.__dict__["customerPhone"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customerId():
    assert hasattr(Customer, "customerId")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customerPaymentInfo():
    assert hasattr(Customer, "customerPaymentInfo")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerPaymentInfo" in klass.__dict__:
            descriptor = klass.__dict__["customerPaymentInfo"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customerName():
    assert hasattr(Customer, "customerName")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerName" in klass.__dict__:
            descriptor = klass.__dict__["customerName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_customerAddress():
    assert hasattr(Customer, "customerAddress")
    descriptor = None
    for klass in Customer.__mro__:
        if "customerAddress" in klass.__dict__:
            descriptor = klass.__dict__["customerAddress"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "userId" in params, "Missing parameter 'userId'"

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_userId():
    assert hasattr(User, "userId")
    descriptor = None
    for klass in User.__mro__:
        if "userId" in klass.__dict__:
            descriptor = klass.__dict__["userId"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "paymentTotal" in params, "Missing parameter 'paymentTotal'"
    assert "paymentId" in params, "Missing parameter 'paymentId'"

def test_payment_has_paymentTotal():
    assert hasattr(Payment, "paymentTotal")
    descriptor = None
    for klass in Payment.__mro__:
        if "paymentTotal" in klass.__dict__:
            descriptor = klass.__dict__["paymentTotal"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_paymentId():
    assert hasattr(Payment, "paymentId")
    descriptor = None
    for klass in Payment.__mro__:
        if "paymentId" in klass.__dict__:
            descriptor = klass.__dict__["paymentId"]
            break
    assert isinstance(descriptor, property)



def test_bookstore_shop_is_not_abstract():
    assert not inspect.isabstract(Bookstore_Shop)


def test_bookstore_shop_constructor_exists():
    assert callable(Bookstore_Shop.__init__)


def test_bookstore_shop_constructor_args():
    sig = inspect.signature(Bookstore_Shop.__init__)
    params = list(sig.parameters.keys())
    assert "Admin" in params, "Missing parameter 'Admin'"
    assert "User" in params, "Missing parameter 'User'"

def test_bookstore_shop_has_Admin():
    assert hasattr(Bookstore_Shop, "Admin")
    descriptor = None
    for klass in Bookstore_Shop.__mro__:
        if "Admin" in klass.__dict__:
            descriptor = klass.__dict__["Admin"]
            break
    assert isinstance(descriptor, property)

def test_bookstore_shop_has_User():
    assert hasattr(Bookstore_Shop, "User")
    descriptor = None
    for klass in Bookstore_Shop.__mro__:
        if "User" in klass.__dict__:
            descriptor = klass.__dict__["User"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "price" in params, "Missing parameter 'price'"
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "NumberOfBooks" in params, "Missing parameter 'NumberOfBooks'"
    assert "customerId" in params, "Missing parameter 'customerId'"

def test_order_has_price():
    assert hasattr(Order, "price")
    descriptor = None
    for klass in Order.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderId():
    assert hasattr(Order, "orderId")
    descriptor = None
    for klass in Order.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_order_has_NumberOfBooks():
    assert hasattr(Order, "NumberOfBooks")
    descriptor = None
    for klass in Order.__mro__:
        if "NumberOfBooks" in klass.__dict__:
            descriptor = klass.__dict__["NumberOfBooks"]
            break
    assert isinstance(descriptor, property)

def test_order_has_customerId():
    assert hasattr(Order, "customerId")
    descriptor = None
    for klass in Order.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)



def test_bookset_is_not_abstract():
    assert not inspect.isabstract(BookSet)


def test_bookset_constructor_exists():
    assert callable(BookSet.__init__)


def test_bookset_constructor_args():
    sig = inspect.signature(BookSet.__init__)
    params = list(sig.parameters.keys())
    assert "bookTitle" in params, "Missing parameter 'bookTitle'"
    assert "bookIsbn" in params, "Missing parameter 'bookIsbn'"

def test_bookset_has_bookTitle():
    assert hasattr(BookSet, "bookTitle")
    descriptor = None
    for klass in BookSet.__mro__:
        if "bookTitle" in klass.__dict__:
            descriptor = klass.__dict__["bookTitle"]
            break
    assert isinstance(descriptor, property)

def test_bookset_has_bookIsbn():
    assert hasattr(BookSet, "bookIsbn")
    descriptor = None
    for klass in BookSet.__mro__:
        if "bookIsbn" in klass.__dict__:
            descriptor = klass.__dict__["bookIsbn"]
            break
    assert isinstance(descriptor, property)



def test_search_is_not_abstract():
    assert not inspect.isabstract(Search)


def test_search_constructor_exists():
    assert callable(Search.__init__)


def test_search_constructor_args():
    sig = inspect.signature(Search.__init__)
    params = list(sig.parameters.keys())
    assert "authorName" in params, "Missing parameter 'authorName'"
    assert "bookTitle" in params, "Missing parameter 'bookTitle'"
    assert "priceLimit" in params, "Missing parameter 'priceLimit'"

def test_search_has_authorName():
    assert hasattr(Search, "authorName")
    descriptor = None
    for klass in Search.__mro__:
        if "authorName" in klass.__dict__:
            descriptor = klass.__dict__["authorName"]
            break
    assert isinstance(descriptor, property)

def test_search_has_bookTitle():
    assert hasattr(Search, "bookTitle")
    descriptor = None
    for klass in Search.__mro__:
        if "bookTitle" in klass.__dict__:
            descriptor = klass.__dict__["bookTitle"]
            break
    assert isinstance(descriptor, property)

def test_search_has_priceLimit():
    assert hasattr(Search, "priceLimit")
    descriptor = None
    for klass in Search.__mro__:
        if "priceLimit" in klass.__dict__:
            descriptor = klass.__dict__["priceLimit"]
            break
    assert isinstance(descriptor, property)



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "customerId" in params, "Missing parameter 'customerId'"
    assert "orderId" in params, "Missing parameter 'orderId'"
    assert "price" in params, "Missing parameter 'price'"

def test_shopping_cart_has_customerId():
    assert hasattr(Shopping_Cart, "customerId")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "customerId" in klass.__dict__:
            descriptor = klass.__dict__["customerId"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_orderId():
    assert hasattr(Shopping_Cart, "orderId")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "orderId" in klass.__dict__:
            descriptor = klass.__dict__["orderId"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_price():
    assert hasattr(Shopping_Cart, "price")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "adminId" in params, "Missing parameter 'adminId'"
    assert "adminName" in params, "Missing parameter 'adminName'"
    assert "adminPassword" in params, "Missing parameter 'adminPassword'"
    assert "adminRmail" in params, "Missing parameter 'adminRmail'"

def test_admin_has_adminId():
    assert hasattr(Admin, "adminId")
    descriptor = None
    for klass in Admin.__mro__:
        if "adminId" in klass.__dict__:
            descriptor = klass.__dict__["adminId"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_adminName():
    assert hasattr(Admin, "adminName")
    descriptor = None
    for klass in Admin.__mro__:
        if "adminName" in klass.__dict__:
            descriptor = klass.__dict__["adminName"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_adminPassword():
    assert hasattr(Admin, "adminPassword")
    descriptor = None
    for klass in Admin.__mro__:
        if "adminPassword" in klass.__dict__:
            descriptor = klass.__dict__["adminPassword"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_adminRmail():
    assert hasattr(Admin, "adminRmail")
    descriptor = None
    for klass in Admin.__mro__:
        if "adminRmail" in klass.__dict__:
            descriptor = klass.__dict__["adminRmail"]
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
Customer_strategy = st.builds(
    Customer,
    customerPhone=
        st.integers(),
    customerId=
        st.integers(),
    customerPaymentInfo=
        safe_text,
    customerName=
        safe_text,
    customerAddress=
        safe_text
)
User_strategy = st.builds(
    User,
    password=
        safe_text,
    userId=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    paymentTotal=
        safe_text,
    paymentId=
        st.integers()
)
Bookstore_Shop_strategy = st.builds(
    Bookstore_Shop,
    Admin=
        st.none(),
    User=
        st.none()
)
Order_strategy = st.builds(
    Order,
    price=
        safe_text,
    orderId=
        st.integers(),
    NumberOfBooks=
        st.integers(),
    customerId=
        st.integers()
)
BookSet_strategy = st.builds(
    BookSet,
    bookTitle=
        safe_text,
    bookIsbn=
        st.integers()
)
Search_strategy = st.builds(
    Search,
    authorName=
        safe_text,
    bookTitle=
        safe_text,
    priceLimit=
        safe_text
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    customerId=
        st.none(),
    orderId=
        st.integers(),
    price=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    adminId=
        st.integers(),
    adminName=
        safe_text,
    adminPassword=
        safe_text,
    adminRmail=
        safe_text
)

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_customerPhone_setter(instance):
    original = instance.customerPhone
    instance.customerPhone = original
    assert instance.customerPhone == original



@given(instance=Customer_strategy)
def test_customer_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original



@given(instance=Customer_strategy)
def test_customer_customerPaymentInfo_setter(instance):
    original = instance.customerPaymentInfo
    instance.customerPaymentInfo = original
    assert instance.customerPaymentInfo == original



@given(instance=Customer_strategy)
def test_customer_customerName_setter(instance):
    original = instance.customerName
    instance.customerName = original
    assert instance.customerName == original



@given(instance=Customer_strategy)
def test_customer_customerAddress_setter(instance):
    original = instance.customerAddress
    instance.customerAddress = original
    assert instance.customerAddress == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=User_strategy)
def test_user_userId_setter(instance):
    original = instance.userId
    instance.userId = original
    assert instance.userId == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_paymentTotal_setter(instance):
    original = instance.paymentTotal
    instance.paymentTotal = original
    assert instance.paymentTotal == original



@given(instance=Payment_strategy)
def test_payment_paymentId_setter(instance):
    original = instance.paymentId
    instance.paymentId = original
    assert instance.paymentId == original

@given(instance=Bookstore_Shop_strategy)
@settings(max_examples=50)
def test_bookstore_shop_instantiation(instance):
    assert isinstance(instance, Bookstore_Shop)



@given(instance=Bookstore_Shop_strategy)
def test_bookstore_shop_Admin_setter(instance):
    original = instance.Admin
    instance.Admin = original
    assert instance.Admin == original



@given(instance=Bookstore_Shop_strategy)
def test_bookstore_shop_User_setter(instance):
    original = instance.User
    instance.User = original
    assert instance.User == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Order_strategy)
def test_order_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original



@given(instance=Order_strategy)
def test_order_NumberOfBooks_setter(instance):
    original = instance.NumberOfBooks
    instance.NumberOfBooks = original
    assert instance.NumberOfBooks == original



@given(instance=Order_strategy)
def test_order_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original

@given(instance=BookSet_strategy)
@settings(max_examples=50)
def test_bookset_instantiation(instance):
    assert isinstance(instance, BookSet)



@given(instance=BookSet_strategy)
def test_bookset_bookTitle_setter(instance):
    original = instance.bookTitle
    instance.bookTitle = original
    assert instance.bookTitle == original



@given(instance=BookSet_strategy)
def test_bookset_bookIsbn_setter(instance):
    original = instance.bookIsbn
    instance.bookIsbn = original
    assert instance.bookIsbn == original

@given(instance=Search_strategy)
@settings(max_examples=50)
def test_search_instantiation(instance):
    assert isinstance(instance, Search)



@given(instance=Search_strategy)
def test_search_authorName_setter(instance):
    original = instance.authorName
    instance.authorName = original
    assert instance.authorName == original



@given(instance=Search_strategy)
def test_search_bookTitle_setter(instance):
    original = instance.bookTitle
    instance.bookTitle = original
    assert instance.bookTitle == original



@given(instance=Search_strategy)
def test_search_priceLimit_setter(instance):
    original = instance.priceLimit
    instance.priceLimit = original
    assert instance.priceLimit == original

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_customerId_setter(instance):
    original = instance.customerId
    instance.customerId = original
    assert instance.customerId == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_orderId_setter(instance):
    original = instance.orderId
    instance.orderId = original
    assert instance.orderId == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_adminId_setter(instance):
    original = instance.adminId
    instance.adminId = original
    assert instance.adminId == original



@given(instance=Admin_strategy)
def test_admin_adminName_setter(instance):
    original = instance.adminName
    instance.adminName = original
    assert instance.adminName == original



@given(instance=Admin_strategy)
def test_admin_adminPassword_setter(instance):
    original = instance.adminPassword
    instance.adminPassword = original
    assert instance.adminPassword == original



@given(instance=Admin_strategy)
def test_admin_adminRmail_setter(instance):
    original = instance.adminRmail
    instance.adminRmail = original
    assert instance.adminRmail == original
