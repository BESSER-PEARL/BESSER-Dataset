import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    _Product,
    _ProductRating,
    _User,
    _UserType,
    _PaymentInfo,
    _OrderDetail,
    _ProductType,
    _LoginCredential,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test__product_is_not_abstract():
    assert not inspect.isabstract(_Product)


def test__product_constructor_exists():
    assert callable(_Product.__init__)


def test__product_constructor_args():
    sig = inspect.signature(_Product.__init__)
    params = list(sig.parameters.keys())
    assert "_stock" in params, "Missing parameter '_stock'"
    assert "_modelno" in params, "Missing parameter '_modelno'"
    assert "_description" in params, "Missing parameter '_description'"
    assert "_name" in params, "Missing parameter '_name'"
    assert "_producttypeid" in params, "Missing parameter '_producttypeid'"
    assert "_price" in params, "Missing parameter '_price'"

def test__product_has__stock():
    assert hasattr(_Product, "_stock")
    descriptor = None
    for klass in _Product.__mro__:
        if "_stock" in klass.__dict__:
            descriptor = klass.__dict__["_stock"]
            break
    assert isinstance(descriptor, property)

def test__product_has__modelno():
    assert hasattr(_Product, "_modelno")
    descriptor = None
    for klass in _Product.__mro__:
        if "_modelno" in klass.__dict__:
            descriptor = klass.__dict__["_modelno"]
            break
    assert isinstance(descriptor, property)

def test__product_has__description():
    assert hasattr(_Product, "_description")
    descriptor = None
    for klass in _Product.__mro__:
        if "_description" in klass.__dict__:
            descriptor = klass.__dict__["_description"]
            break
    assert isinstance(descriptor, property)

def test__product_has__name():
    assert hasattr(_Product, "_name")
    descriptor = None
    for klass in _Product.__mro__:
        if "_name" in klass.__dict__:
            descriptor = klass.__dict__["_name"]
            break
    assert isinstance(descriptor, property)

def test__product_has__producttypeid():
    assert hasattr(_Product, "_producttypeid")
    descriptor = None
    for klass in _Product.__mro__:
        if "_producttypeid" in klass.__dict__:
            descriptor = klass.__dict__["_producttypeid"]
            break
    assert isinstance(descriptor, property)

def test__product_has__price():
    assert hasattr(_Product, "_price")
    descriptor = None
    for klass in _Product.__mro__:
        if "_price" in klass.__dict__:
            descriptor = klass.__dict__["_price"]
            break
    assert isinstance(descriptor, property)



def test__productrating_is_not_abstract():
    assert not inspect.isabstract(_ProductRating)


def test__productrating_constructor_exists():
    assert callable(_ProductRating.__init__)


def test__productrating_constructor_args():
    sig = inspect.signature(_ProductRating.__init__)
    params = list(sig.parameters.keys())
    assert "_userid" in params, "Missing parameter '_userid'"
    assert "_productid" in params, "Missing parameter '_productid'"
    assert "_rating" in params, "Missing parameter '_rating'"

def test__productrating_has__userid():
    assert hasattr(_ProductRating, "_userid")
    descriptor = None
    for klass in _ProductRating.__mro__:
        if "_userid" in klass.__dict__:
            descriptor = klass.__dict__["_userid"]
            break
    assert isinstance(descriptor, property)

def test__productrating_has__productid():
    assert hasattr(_ProductRating, "_productid")
    descriptor = None
    for klass in _ProductRating.__mro__:
        if "_productid" in klass.__dict__:
            descriptor = klass.__dict__["_productid"]
            break
    assert isinstance(descriptor, property)

def test__productrating_has__rating():
    assert hasattr(_ProductRating, "_rating")
    descriptor = None
    for klass in _ProductRating.__mro__:
        if "_rating" in klass.__dict__:
            descriptor = klass.__dict__["_rating"]
            break
    assert isinstance(descriptor, property)



def test__user_is_not_abstract():
    assert not inspect.isabstract(_User)


def test__user_constructor_exists():
    assert callable(_User.__init__)


def test__user_constructor_args():
    sig = inspect.signature(_User.__init__)
    params = list(sig.parameters.keys())
    assert "_username" in params, "Missing parameter '_username'"
    assert "_usertypeid" in params, "Missing parameter '_usertypeid'"
    assert "_phone" in params, "Missing parameter '_phone'"
    assert "_logincredentialsid" in params, "Missing parameter '_logincredentialsid'"
    assert "_address" in params, "Missing parameter '_address'"
    assert "_email" in params, "Missing parameter '_email'"

def test__user_has__username():
    assert hasattr(_User, "_username")
    descriptor = None
    for klass in _User.__mro__:
        if "_username" in klass.__dict__:
            descriptor = klass.__dict__["_username"]
            break
    assert isinstance(descriptor, property)

def test__user_has__usertypeid():
    assert hasattr(_User, "_usertypeid")
    descriptor = None
    for klass in _User.__mro__:
        if "_usertypeid" in klass.__dict__:
            descriptor = klass.__dict__["_usertypeid"]
            break
    assert isinstance(descriptor, property)

def test__user_has__phone():
    assert hasattr(_User, "_phone")
    descriptor = None
    for klass in _User.__mro__:
        if "_phone" in klass.__dict__:
            descriptor = klass.__dict__["_phone"]
            break
    assert isinstance(descriptor, property)

def test__user_has__logincredentialsid():
    assert hasattr(_User, "_logincredentialsid")
    descriptor = None
    for klass in _User.__mro__:
        if "_logincredentialsid" in klass.__dict__:
            descriptor = klass.__dict__["_logincredentialsid"]
            break
    assert isinstance(descriptor, property)

def test__user_has__address():
    assert hasattr(_User, "_address")
    descriptor = None
    for klass in _User.__mro__:
        if "_address" in klass.__dict__:
            descriptor = klass.__dict__["_address"]
            break
    assert isinstance(descriptor, property)

def test__user_has__email():
    assert hasattr(_User, "_email")
    descriptor = None
    for klass in _User.__mro__:
        if "_email" in klass.__dict__:
            descriptor = klass.__dict__["_email"]
            break
    assert isinstance(descriptor, property)



def test__usertype_is_not_abstract():
    assert not inspect.isabstract(_UserType)


def test__usertype_constructor_exists():
    assert callable(_UserType.__init__)


def test__usertype_constructor_args():
    sig = inspect.signature(_UserType.__init__)
    params = list(sig.parameters.keys())
    assert "_userrole" in params, "Missing parameter '_userrole'"

def test__usertype_has__userrole():
    assert hasattr(_UserType, "_userrole")
    descriptor = None
    for klass in _UserType.__mro__:
        if "_userrole" in klass.__dict__:
            descriptor = klass.__dict__["_userrole"]
            break
    assert isinstance(descriptor, property)



def test__paymentinfo_is_not_abstract():
    assert not inspect.isabstract(_PaymentInfo)


def test__paymentinfo_constructor_exists():
    assert callable(_PaymentInfo.__init__)


def test__paymentinfo_constructor_args():
    sig = inspect.signature(_PaymentInfo.__init__)
    params = list(sig.parameters.keys())
    assert "_cvv" in params, "Missing parameter '_cvv'"
    assert "_expirydate" in params, "Missing parameter '_expirydate'"
    assert "_cardno" in params, "Missing parameter '_cardno'"
    assert "_cardname" in params, "Missing parameter '_cardname'"
    assert "_userid" in params, "Missing parameter '_userid'"

def test__paymentinfo_has__cvv():
    assert hasattr(_PaymentInfo, "_cvv")
    descriptor = None
    for klass in _PaymentInfo.__mro__:
        if "_cvv" in klass.__dict__:
            descriptor = klass.__dict__["_cvv"]
            break
    assert isinstance(descriptor, property)

def test__paymentinfo_has__expirydate():
    assert hasattr(_PaymentInfo, "_expirydate")
    descriptor = None
    for klass in _PaymentInfo.__mro__:
        if "_expirydate" in klass.__dict__:
            descriptor = klass.__dict__["_expirydate"]
            break
    assert isinstance(descriptor, property)

def test__paymentinfo_has__cardno():
    assert hasattr(_PaymentInfo, "_cardno")
    descriptor = None
    for klass in _PaymentInfo.__mro__:
        if "_cardno" in klass.__dict__:
            descriptor = klass.__dict__["_cardno"]
            break
    assert isinstance(descriptor, property)

def test__paymentinfo_has__cardname():
    assert hasattr(_PaymentInfo, "_cardname")
    descriptor = None
    for klass in _PaymentInfo.__mro__:
        if "_cardname" in klass.__dict__:
            descriptor = klass.__dict__["_cardname"]
            break
    assert isinstance(descriptor, property)

def test__paymentinfo_has__userid():
    assert hasattr(_PaymentInfo, "_userid")
    descriptor = None
    for klass in _PaymentInfo.__mro__:
        if "_userid" in klass.__dict__:
            descriptor = klass.__dict__["_userid"]
            break
    assert isinstance(descriptor, property)



def test__orderdetail_is_not_abstract():
    assert not inspect.isabstract(_OrderDetail)


def test__orderdetail_constructor_exists():
    assert callable(_OrderDetail.__init__)


def test__orderdetail_constructor_args():
    sig = inspect.signature(_OrderDetail.__init__)
    params = list(sig.parameters.keys())
    assert "_productid" in params, "Missing parameter '_productid'"
    assert "_orderdate" in params, "Missing parameter '_orderdate'"
    assert "_totalamount" in params, "Missing parameter '_totalamount'"
    assert "_userid" in params, "Missing parameter '_userid'"
    assert "_quantity" in params, "Missing parameter '_quantity'"

def test__orderdetail_has__productid():
    assert hasattr(_OrderDetail, "_productid")
    descriptor = None
    for klass in _OrderDetail.__mro__:
        if "_productid" in klass.__dict__:
            descriptor = klass.__dict__["_productid"]
            break
    assert isinstance(descriptor, property)

def test__orderdetail_has__orderdate():
    assert hasattr(_OrderDetail, "_orderdate")
    descriptor = None
    for klass in _OrderDetail.__mro__:
        if "_orderdate" in klass.__dict__:
            descriptor = klass.__dict__["_orderdate"]
            break
    assert isinstance(descriptor, property)

def test__orderdetail_has__totalamount():
    assert hasattr(_OrderDetail, "_totalamount")
    descriptor = None
    for klass in _OrderDetail.__mro__:
        if "_totalamount" in klass.__dict__:
            descriptor = klass.__dict__["_totalamount"]
            break
    assert isinstance(descriptor, property)

def test__orderdetail_has__userid():
    assert hasattr(_OrderDetail, "_userid")
    descriptor = None
    for klass in _OrderDetail.__mro__:
        if "_userid" in klass.__dict__:
            descriptor = klass.__dict__["_userid"]
            break
    assert isinstance(descriptor, property)

def test__orderdetail_has__quantity():
    assert hasattr(_OrderDetail, "_quantity")
    descriptor = None
    for klass in _OrderDetail.__mro__:
        if "_quantity" in klass.__dict__:
            descriptor = klass.__dict__["_quantity"]
            break
    assert isinstance(descriptor, property)



def test__producttype_is_not_abstract():
    assert not inspect.isabstract(_ProductType)


def test__producttype_constructor_exists():
    assert callable(_ProductType.__init__)


def test__producttype_constructor_args():
    sig = inspect.signature(_ProductType.__init__)
    params = list(sig.parameters.keys())
    assert "_type" in params, "Missing parameter '_type'"

def test__producttype_has__type():
    assert hasattr(_ProductType, "_type")
    descriptor = None
    for klass in _ProductType.__mro__:
        if "_type" in klass.__dict__:
            descriptor = klass.__dict__["_type"]
            break
    assert isinstance(descriptor, property)



def test__logincredential_is_not_abstract():
    assert not inspect.isabstract(_LoginCredential)


def test__logincredential_constructor_exists():
    assert callable(_LoginCredential.__init__)


def test__logincredential_constructor_args():
    sig = inspect.signature(_LoginCredential.__init__)
    params = list(sig.parameters.keys())
    assert "_loginid" in params, "Missing parameter '_loginid'"
    assert "_password" in params, "Missing parameter '_password'"

def test__logincredential_has__loginid():
    assert hasattr(_LoginCredential, "_loginid")
    descriptor = None
    for klass in _LoginCredential.__mro__:
        if "_loginid" in klass.__dict__:
            descriptor = klass.__dict__["_loginid"]
            break
    assert isinstance(descriptor, property)

def test__logincredential_has__password():
    assert hasattr(_LoginCredential, "_password")
    descriptor = None
    for klass in _LoginCredential.__mro__:
        if "_password" in klass.__dict__:
            descriptor = klass.__dict__["_password"]
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
_Product_strategy = st.builds(
    _Product,
    _stock=
        st.integers(),
    _modelno=
        safe_text,
    _description=
        safe_text,
    _name=
        safe_text,
    _producttypeid=
        st.integers(),
    _price=
        st.integers()
)
_ProductRating_strategy = st.builds(
    _ProductRating,
    _userid=
        st.integers(),
    _productid=
        st.integers(),
    _rating=
        st.integers()
)
_User_strategy = st.builds(
    _User,
    _username=
        safe_text,
    _usertypeid=
        st.integers(),
    _phone=
        st.integers(),
    _logincredentialsid=
        st.integers(),
    _address=
        safe_text,
    _email=
        safe_text
)
_UserType_strategy = st.builds(
    _UserType,
    _userrole=
        safe_text
)
_PaymentInfo_strategy = st.builds(
    _PaymentInfo,
    _cvv=
        st.integers(),
    _expirydate=
        st.dates(),
    _cardno=
        st.integers(),
    _cardname=
        safe_text,
    _userid=
        st.integers()
)
_OrderDetail_strategy = st.builds(
    _OrderDetail,
    _productid=
        st.integers(),
    _orderdate=
        st.dates(),
    _totalamount=
        st.integers(),
    _userid=
        st.integers(),
    _quantity=
        st.integers()
)
_ProductType_strategy = st.builds(
    _ProductType,
    _type=
        safe_text
)
_LoginCredential_strategy = st.builds(
    _LoginCredential,
    _loginid=
        safe_text,
    _password=
        safe_text
)

@given(instance=_Product_strategy)
@settings(max_examples=50)
def test__product_instantiation(instance):
    assert isinstance(instance, _Product)



@given(instance=_Product_strategy)
def test__product__stock_setter(instance):
    original = instance._stock
    instance._stock = original
    assert instance._stock == original



@given(instance=_Product_strategy)
def test__product__modelno_setter(instance):
    original = instance._modelno
    instance._modelno = original
    assert instance._modelno == original



@given(instance=_Product_strategy)
def test__product__description_setter(instance):
    original = instance._description
    instance._description = original
    assert instance._description == original



@given(instance=_Product_strategy)
def test__product__name_setter(instance):
    original = instance._name
    instance._name = original
    assert instance._name == original



@given(instance=_Product_strategy)
def test__product__producttypeid_setter(instance):
    original = instance._producttypeid
    instance._producttypeid = original
    assert instance._producttypeid == original



@given(instance=_Product_strategy)
def test__product__price_setter(instance):
    original = instance._price
    instance._price = original
    assert instance._price == original

@given(instance=_ProductRating_strategy)
@settings(max_examples=50)
def test__productrating_instantiation(instance):
    assert isinstance(instance, _ProductRating)



@given(instance=_ProductRating_strategy)
def test__productrating__userid_setter(instance):
    original = instance._userid
    instance._userid = original
    assert instance._userid == original



@given(instance=_ProductRating_strategy)
def test__productrating__productid_setter(instance):
    original = instance._productid
    instance._productid = original
    assert instance._productid == original



@given(instance=_ProductRating_strategy)
def test__productrating__rating_setter(instance):
    original = instance._rating
    instance._rating = original
    assert instance._rating == original

@given(instance=_User_strategy)
@settings(max_examples=50)
def test__user_instantiation(instance):
    assert isinstance(instance, _User)



@given(instance=_User_strategy)
def test__user__username_setter(instance):
    original = instance._username
    instance._username = original
    assert instance._username == original



@given(instance=_User_strategy)
def test__user__usertypeid_setter(instance):
    original = instance._usertypeid
    instance._usertypeid = original
    assert instance._usertypeid == original



@given(instance=_User_strategy)
def test__user__phone_setter(instance):
    original = instance._phone
    instance._phone = original
    assert instance._phone == original



@given(instance=_User_strategy)
def test__user__logincredentialsid_setter(instance):
    original = instance._logincredentialsid
    instance._logincredentialsid = original
    assert instance._logincredentialsid == original



@given(instance=_User_strategy)
def test__user__address_setter(instance):
    original = instance._address
    instance._address = original
    assert instance._address == original



@given(instance=_User_strategy)
def test__user__email_setter(instance):
    original = instance._email
    instance._email = original
    assert instance._email == original

@given(instance=_UserType_strategy)
@settings(max_examples=50)
def test__usertype_instantiation(instance):
    assert isinstance(instance, _UserType)



@given(instance=_UserType_strategy)
def test__usertype__userrole_setter(instance):
    original = instance._userrole
    instance._userrole = original
    assert instance._userrole == original

@given(instance=_PaymentInfo_strategy)
@settings(max_examples=50)
def test__paymentinfo_instantiation(instance):
    assert isinstance(instance, _PaymentInfo)



@given(instance=_PaymentInfo_strategy)
def test__paymentinfo__cvv_setter(instance):
    original = instance._cvv
    instance._cvv = original
    assert instance._cvv == original



@given(instance=_PaymentInfo_strategy)
def test__paymentinfo__expirydate_setter(instance):
    original = instance._expirydate
    instance._expirydate = original
    assert instance._expirydate == original



@given(instance=_PaymentInfo_strategy)
def test__paymentinfo__cardno_setter(instance):
    original = instance._cardno
    instance._cardno = original
    assert instance._cardno == original



@given(instance=_PaymentInfo_strategy)
def test__paymentinfo__cardname_setter(instance):
    original = instance._cardname
    instance._cardname = original
    assert instance._cardname == original



@given(instance=_PaymentInfo_strategy)
def test__paymentinfo__userid_setter(instance):
    original = instance._userid
    instance._userid = original
    assert instance._userid == original

@given(instance=_OrderDetail_strategy)
@settings(max_examples=50)
def test__orderdetail_instantiation(instance):
    assert isinstance(instance, _OrderDetail)



@given(instance=_OrderDetail_strategy)
def test__orderdetail__productid_setter(instance):
    original = instance._productid
    instance._productid = original
    assert instance._productid == original



@given(instance=_OrderDetail_strategy)
def test__orderdetail__orderdate_setter(instance):
    original = instance._orderdate
    instance._orderdate = original
    assert instance._orderdate == original



@given(instance=_OrderDetail_strategy)
def test__orderdetail__totalamount_setter(instance):
    original = instance._totalamount
    instance._totalamount = original
    assert instance._totalamount == original



@given(instance=_OrderDetail_strategy)
def test__orderdetail__userid_setter(instance):
    original = instance._userid
    instance._userid = original
    assert instance._userid == original



@given(instance=_OrderDetail_strategy)
def test__orderdetail__quantity_setter(instance):
    original = instance._quantity
    instance._quantity = original
    assert instance._quantity == original

@given(instance=_ProductType_strategy)
@settings(max_examples=50)
def test__producttype_instantiation(instance):
    assert isinstance(instance, _ProductType)



@given(instance=_ProductType_strategy)
def test__producttype__type_setter(instance):
    original = instance._type
    instance._type = original
    assert instance._type == original

@given(instance=_LoginCredential_strategy)
@settings(max_examples=50)
def test__logincredential_instantiation(instance):
    assert isinstance(instance, _LoginCredential)



@given(instance=_LoginCredential_strategy)
def test__logincredential__loginid_setter(instance):
    original = instance._loginid
    instance._loginid = original
    assert instance._loginid == original



@given(instance=_LoginCredential_strategy)
def test__logincredential__password_setter(instance):
    original = instance._password
    instance._password = original
    assert instance._password == original
