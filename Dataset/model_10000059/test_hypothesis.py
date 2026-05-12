import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Login,
    processQuery,
    AdminController,
    Membership_Card,
    OrderController,
    Table,
    BookingController,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "LoyaltyID" in params, "Missing parameter 'LoyaltyID'"
    assert "Discount" in params, "Missing parameter 'Discount'"

def test_login_has_LoyaltyID():
    assert hasattr(Login, "LoyaltyID")
    descriptor = None
    for klass in Login.__mro__:
        if "LoyaltyID" in klass.__dict__:
            descriptor = klass.__dict__["LoyaltyID"]
            break
    assert isinstance(descriptor, property)

def test_login_has_Discount():
    assert hasattr(Login, "Discount")
    descriptor = None
    for klass in Login.__mro__:
        if "Discount" in klass.__dict__:
            descriptor = klass.__dict__["Discount"]
            break
    assert isinstance(descriptor, property)



def test_processquery_is_not_abstract():
    assert not inspect.isabstract(processQuery)


def test_processquery_constructor_exists():
    assert callable(processQuery.__init__)


def test_processquery_constructor_args():
    sig = inspect.signature(processQuery.__init__)
    params = list(sig.parameters.keys())



def test_admincontroller_is_not_abstract():
    assert not inspect.isabstract(AdminController)


def test_admincontroller_constructor_exists():
    assert callable(AdminController.__init__)


def test_admincontroller_constructor_args():
    sig = inspect.signature(AdminController.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "UserLevel" in params, "Missing parameter 'UserLevel'"
    assert "UserName" in params, "Missing parameter 'UserName'"

def test_admincontroller_has_UserID():
    assert hasattr(AdminController, "UserID")
    descriptor = None
    for klass in AdminController.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_admincontroller_has_UserLevel():
    assert hasattr(AdminController, "UserLevel")
    descriptor = None
    for klass in AdminController.__mro__:
        if "UserLevel" in klass.__dict__:
            descriptor = klass.__dict__["UserLevel"]
            break
    assert isinstance(descriptor, property)

def test_admincontroller_has_UserName():
    assert hasattr(AdminController, "UserName")
    descriptor = None
    for klass in AdminController.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)



def test_membership_card_is_not_abstract():
    assert not inspect.isabstract(Membership_Card)


def test_membership_card_constructor_exists():
    assert callable(Membership_Card.__init__)


def test_membership_card_constructor_args():
    sig = inspect.signature(Membership_Card.__init__)
    params = list(sig.parameters.keys())
    assert "LoyaltyID" in params, "Missing parameter 'LoyaltyID'"
    assert "Discount" in params, "Missing parameter 'Discount'"

def test_membership_card_has_LoyaltyID():
    assert hasattr(Membership_Card, "LoyaltyID")
    descriptor = None
    for klass in Membership_Card.__mro__:
        if "LoyaltyID" in klass.__dict__:
            descriptor = klass.__dict__["LoyaltyID"]
            break
    assert isinstance(descriptor, property)

def test_membership_card_has_Discount():
    assert hasattr(Membership_Card, "Discount")
    descriptor = None
    for klass in Membership_Card.__mro__:
        if "Discount" in klass.__dict__:
            descriptor = klass.__dict__["Discount"]
            break
    assert isinstance(descriptor, property)



def test_ordercontroller_is_not_abstract():
    assert not inspect.isabstract(OrderController)


def test_ordercontroller_constructor_exists():
    assert callable(OrderController.__init__)


def test_ordercontroller_constructor_args():
    sig = inspect.signature(OrderController.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "OrderTotal" in params, "Missing parameter 'OrderTotal'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"

def test_ordercontroller_has_UserID():
    assert hasattr(OrderController, "UserID")
    descriptor = None
    for klass in OrderController.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_ordercontroller_has_OrderTotal():
    assert hasattr(OrderController, "OrderTotal")
    descriptor = None
    for klass in OrderController.__mro__:
        if "OrderTotal" in klass.__dict__:
            descriptor = klass.__dict__["OrderTotal"]
            break
    assert isinstance(descriptor, property)

def test_ordercontroller_has_Date():
    assert hasattr(OrderController, "Date")
    descriptor = None
    for klass in OrderController.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_ordercontroller_has_OrderID():
    assert hasattr(OrderController, "OrderID")
    descriptor = None
    for klass in OrderController.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "Occupied" in params, "Missing parameter 'Occupied'"
    assert "TableNo" in params, "Missing parameter 'TableNo'"

def test_table_has_Occupied():
    assert hasattr(Table, "Occupied")
    descriptor = None
    for klass in Table.__mro__:
        if "Occupied" in klass.__dict__:
            descriptor = klass.__dict__["Occupied"]
            break
    assert isinstance(descriptor, property)

def test_table_has_TableNo():
    assert hasattr(Table, "TableNo")
    descriptor = None
    for klass in Table.__mro__:
        if "TableNo" in klass.__dict__:
            descriptor = klass.__dict__["TableNo"]
            break
    assert isinstance(descriptor, property)



def test_bookingcontroller_is_not_abstract():
    assert not inspect.isabstract(BookingController)


def test_bookingcontroller_constructor_exists():
    assert callable(BookingController.__init__)


def test_bookingcontroller_constructor_args():
    sig = inspect.signature(BookingController.__init__)
    params = list(sig.parameters.keys())
    assert "BookingID" in params, "Missing parameter 'BookingID'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "TableNo" in params, "Missing parameter 'TableNo'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_bookingcontroller_has_BookingID():
    assert hasattr(BookingController, "BookingID")
    descriptor = None
    for klass in BookingController.__mro__:
        if "BookingID" in klass.__dict__:
            descriptor = klass.__dict__["BookingID"]
            break
    assert isinstance(descriptor, property)

def test_bookingcontroller_has_Time():
    assert hasattr(BookingController, "Time")
    descriptor = None
    for klass in BookingController.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_bookingcontroller_has_Phone():
    assert hasattr(BookingController, "Phone")
    descriptor = None
    for klass in BookingController.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_bookingcontroller_has_CustomerName():
    assert hasattr(BookingController, "CustomerName")
    descriptor = None
    for klass in BookingController.__mro__:
        if "CustomerName" in klass.__dict__:
            descriptor = klass.__dict__["CustomerName"]
            break
    assert isinstance(descriptor, property)

def test_bookingcontroller_has_TableNo():
    assert hasattr(BookingController, "TableNo")
    descriptor = None
    for klass in BookingController.__mro__:
        if "TableNo" in klass.__dict__:
            descriptor = klass.__dict__["TableNo"]
            break
    assert isinstance(descriptor, property)

def test_bookingcontroller_has_Date():
    assert hasattr(BookingController, "Date")
    descriptor = None
    for klass in BookingController.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
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
Login_strategy = st.builds(
    Login,
    LoyaltyID=
        st.integers(),
    Discount=
        st.integers()
)
processQuery_strategy = st.builds(
    processQuery,
)
AdminController_strategy = st.builds(
    AdminController,
    UserID=
        st.integers(),
    UserLevel=
        st.integers(),
    UserName=
        safe_text
)
Membership_Card_strategy = st.builds(
    Membership_Card,
    LoyaltyID=
        st.integers(),
    Discount=
        st.integers()
)
OrderController_strategy = st.builds(
    OrderController,
    UserID=
        st.integers(),
    OrderTotal=
        safe_text,
    Date=
        safe_text,
    OrderID=
        st.integers()
)
Table_strategy = st.builds(
    Table,
    Occupied=
        st.booleans(),
    TableNo=
        safe_text
)
BookingController_strategy = st.builds(
    BookingController,
    BookingID=
        st.integers(),
    Time=
        safe_text,
    Phone=
        safe_text,
    CustomerName=
        safe_text,
    TableNo=
        safe_text,
    Date=
        safe_text
)

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_LoyaltyID_setter(instance):
    original = instance.LoyaltyID
    instance.LoyaltyID = original
    assert instance.LoyaltyID == original



@given(instance=Login_strategy)
def test_login_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original

@given(instance=processQuery_strategy)
@settings(max_examples=50)
def test_processquery_instantiation(instance):
    assert isinstance(instance, processQuery)

@given(instance=AdminController_strategy)
@settings(max_examples=50)
def test_admincontroller_instantiation(instance):
    assert isinstance(instance, AdminController)



@given(instance=AdminController_strategy)
def test_admincontroller_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=AdminController_strategy)
def test_admincontroller_UserLevel_setter(instance):
    original = instance.UserLevel
    instance.UserLevel = original
    assert instance.UserLevel == original



@given(instance=AdminController_strategy)
def test_admincontroller_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original

@given(instance=Membership_Card_strategy)
@settings(max_examples=50)
def test_membership_card_instantiation(instance):
    assert isinstance(instance, Membership_Card)



@given(instance=Membership_Card_strategy)
def test_membership_card_LoyaltyID_setter(instance):
    original = instance.LoyaltyID
    instance.LoyaltyID = original
    assert instance.LoyaltyID == original



@given(instance=Membership_Card_strategy)
def test_membership_card_Discount_setter(instance):
    original = instance.Discount
    instance.Discount = original
    assert instance.Discount == original

@given(instance=OrderController_strategy)
@settings(max_examples=50)
def test_ordercontroller_instantiation(instance):
    assert isinstance(instance, OrderController)



@given(instance=OrderController_strategy)
def test_ordercontroller_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=OrderController_strategy)
def test_ordercontroller_OrderTotal_setter(instance):
    original = instance.OrderTotal
    instance.OrderTotal = original
    assert instance.OrderTotal == original



@given(instance=OrderController_strategy)
def test_ordercontroller_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=OrderController_strategy)
def test_ordercontroller_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_Occupied_setter(instance):
    original = instance.Occupied
    instance.Occupied = original
    assert instance.Occupied == original



@given(instance=Table_strategy)
def test_table_TableNo_setter(instance):
    original = instance.TableNo
    instance.TableNo = original
    assert instance.TableNo == original

@given(instance=BookingController_strategy)
@settings(max_examples=50)
def test_bookingcontroller_instantiation(instance):
    assert isinstance(instance, BookingController)



@given(instance=BookingController_strategy)
def test_bookingcontroller_BookingID_setter(instance):
    original = instance.BookingID
    instance.BookingID = original
    assert instance.BookingID == original



@given(instance=BookingController_strategy)
def test_bookingcontroller_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=BookingController_strategy)
def test_bookingcontroller_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=BookingController_strategy)
def test_bookingcontroller_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=BookingController_strategy)
def test_bookingcontroller_TableNo_setter(instance):
    original = instance.TableNo
    instance.TableNo = original
    assert instance.TableNo == original



@given(instance=BookingController_strategy)
def test_bookingcontroller_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original
