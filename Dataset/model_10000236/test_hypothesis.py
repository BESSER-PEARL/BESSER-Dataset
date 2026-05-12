import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BookedTables,
    Bookings,
    OrderItem,
    ViewOrder,
    Membership_Card,
    Order,
    Table,
    Users,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bookedtables_is_not_abstract():
    assert not inspect.isabstract(BookedTables)


def test_bookedtables_constructor_exists():
    assert callable(BookedTables.__init__)


def test_bookedtables_constructor_args():
    sig = inspect.signature(BookedTables.__init__)
    params = list(sig.parameters.keys())
    assert "TableNo" in params, "Missing parameter 'TableNo'"
    assert "BookingID" in params, "Missing parameter 'BookingID'"

def test_bookedtables_has_TableNo():
    assert hasattr(BookedTables, "TableNo")
    descriptor = None
    for klass in BookedTables.__mro__:
        if "TableNo" in klass.__dict__:
            descriptor = klass.__dict__["TableNo"]
            break
    assert isinstance(descriptor, property)

def test_bookedtables_has_BookingID():
    assert hasattr(BookedTables, "BookingID")
    descriptor = None
    for klass in BookedTables.__mro__:
        if "BookingID" in klass.__dict__:
            descriptor = klass.__dict__["BookingID"]
            break
    assert isinstance(descriptor, property)



def test_bookings_is_not_abstract():
    assert not inspect.isabstract(Bookings)


def test_bookings_constructor_exists():
    assert callable(Bookings.__init__)


def test_bookings_constructor_args():
    sig = inspect.signature(Bookings.__init__)
    params = list(sig.parameters.keys())
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "BookingID" in params, "Missing parameter 'BookingID'"
    assert "People" in params, "Missing parameter 'People'"
    assert "Time" in params, "Missing parameter 'Time'"
    assert "TableNo" in params, "Missing parameter 'TableNo'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"

def test_bookings_has_Phone():
    assert hasattr(Bookings, "Phone")
    descriptor = None
    for klass in Bookings.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_bookings_has_BookingID():
    assert hasattr(Bookings, "BookingID")
    descriptor = None
    for klass in Bookings.__mro__:
        if "BookingID" in klass.__dict__:
            descriptor = klass.__dict__["BookingID"]
            break
    assert isinstance(descriptor, property)

def test_bookings_has_People():
    assert hasattr(Bookings, "People")
    descriptor = None
    for klass in Bookings.__mro__:
        if "People" in klass.__dict__:
            descriptor = klass.__dict__["People"]
            break
    assert isinstance(descriptor, property)

def test_bookings_has_Time():
    assert hasattr(Bookings, "Time")
    descriptor = None
    for klass in Bookings.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_bookings_has_TableNo():
    assert hasattr(Bookings, "TableNo")
    descriptor = None
    for klass in Bookings.__mro__:
        if "TableNo" in klass.__dict__:
            descriptor = klass.__dict__["TableNo"]
            break
    assert isinstance(descriptor, property)

def test_bookings_has_Date():
    assert hasattr(Bookings, "Date")
    descriptor = None
    for klass in Bookings.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_bookings_has_CustomerName():
    assert hasattr(Bookings, "CustomerName")
    descriptor = None
    for klass in Bookings.__mro__:
        if "CustomerName" in klass.__dict__:
            descriptor = klass.__dict__["CustomerName"]
            break
    assert isinstance(descriptor, property)



def test_orderitem_is_not_abstract():
    assert not inspect.isabstract(OrderItem)


def test_orderitem_constructor_exists():
    assert callable(OrderItem.__init__)


def test_orderitem_constructor_args():
    sig = inspect.signature(OrderItem.__init__)
    params = list(sig.parameters.keys())
    assert "RemaningTime" in params, "Missing parameter 'RemaningTime'"
    assert "ItemName" in params, "Missing parameter 'ItemName'"
    assert "Completed" in params, "Missing parameter 'Completed'"

def test_orderitem_has_RemaningTime():
    assert hasattr(OrderItem, "RemaningTime")
    descriptor = None
    for klass in OrderItem.__mro__:
        if "RemaningTime" in klass.__dict__:
            descriptor = klass.__dict__["RemaningTime"]
            break
    assert isinstance(descriptor, property)

def test_orderitem_has_ItemName():
    assert hasattr(OrderItem, "ItemName")
    descriptor = None
    for klass in OrderItem.__mro__:
        if "ItemName" in klass.__dict__:
            descriptor = klass.__dict__["ItemName"]
            break
    assert isinstance(descriptor, property)

def test_orderitem_has_Completed():
    assert hasattr(OrderItem, "Completed")
    descriptor = None
    for klass in OrderItem.__mro__:
        if "Completed" in klass.__dict__:
            descriptor = klass.__dict__["Completed"]
            break
    assert isinstance(descriptor, property)



def test_vieworder_is_not_abstract():
    assert not inspect.isabstract(ViewOrder)


def test_vieworder_constructor_exists():
    assert callable(ViewOrder.__init__)


def test_vieworder_constructor_args():
    sig = inspect.signature(ViewOrder.__init__)
    params = list(sig.parameters.keys())
    assert "getUser" in params, "Missing parameter 'getUser'"

def test_vieworder_has_getUser():
    assert hasattr(ViewOrder, "getUser")
    descriptor = None
    for klass in ViewOrder.__mro__:
        if "getUser" in klass.__dict__:
            descriptor = klass.__dict__["getUser"]
            break
    assert isinstance(descriptor, property)



def test_membership_card_is_not_abstract():
    assert not inspect.isabstract(Membership_Card)


def test_membership_card_constructor_exists():
    assert callable(Membership_Card.__init__)


def test_membership_card_constructor_args():
    sig = inspect.signature(Membership_Card.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "DiscountLVL" in params, "Missing parameter 'DiscountLVL'"

def test_membership_card_has_ID():
    assert hasattr(Membership_Card, "ID")
    descriptor = None
    for klass in Membership_Card.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_membership_card_has_DiscountLVL():
    assert hasattr(Membership_Card, "DiscountLVL")
    descriptor = None
    for klass in Membership_Card.__mro__:
        if "DiscountLVL" in klass.__dict__:
            descriptor = klass.__dict__["DiscountLVL"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "DicountLvl" in params, "Missing parameter 'DicountLvl'"
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_order_has_DicountLvl():
    assert hasattr(Order, "DicountLvl")
    descriptor = None
    for klass in Order.__mro__:
        if "DicountLvl" in klass.__dict__:
            descriptor = klass.__dict__["DicountLvl"]
            break
    assert isinstance(descriptor, property)

def test_order_has_UserID():
    assert hasattr(Order, "UserID")
    descriptor = None
    for klass in Order.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Total():
    assert hasattr(Order, "Total")
    descriptor = None
    for klass in Order.__mro__:
        if "Total" in klass.__dict__:
            descriptor = klass.__dict__["Total"]
            break
    assert isinstance(descriptor, property)

def test_order_has_OrderID():
    assert hasattr(Order, "OrderID")
    descriptor = None
    for klass in Order.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_Date():
    assert hasattr(Order, "Date")
    descriptor = None
    for klass in Order.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
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



def test_users_is_not_abstract():
    assert not inspect.isabstract(Users)


def test_users_constructor_exists():
    assert callable(Users.__init__)


def test_users_constructor_args():
    sig = inspect.signature(Users.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "UserLevel" in params, "Missing parameter 'UserLevel'"

def test_users_has_UserID():
    assert hasattr(Users, "UserID")
    descriptor = None
    for klass in Users.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_users_has_UserName():
    assert hasattr(Users, "UserName")
    descriptor = None
    for klass in Users.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_users_has_UserLevel():
    assert hasattr(Users, "UserLevel")
    descriptor = None
    for klass in Users.__mro__:
        if "UserLevel" in klass.__dict__:
            descriptor = klass.__dict__["UserLevel"]
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
BookedTables_strategy = st.builds(
    BookedTables,
    TableNo=
        st.integers(),
    BookingID=
        st.integers()
)
Bookings_strategy = st.builds(
    Bookings,
    Phone=
        safe_text,
    BookingID=
        st.integers(),
    People=
        st.integers(),
    Time=
        st.dates(),
    TableNo=
        st.integers(),
    Date=
        st.dates(),
    CustomerName=
        safe_text
)
OrderItem_strategy = st.builds(
    OrderItem,
    RemaningTime=
        st.dates(),
    ItemName=
        safe_text,
    Completed=
        st.integers()
)
ViewOrder_strategy = st.builds(
    ViewOrder,
    getUser=
        st.integers()
)
Membership_Card_strategy = st.builds(
    Membership_Card,
    ID=
        st.integers(),
    DiscountLVL=
        st.integers()
)
Order_strategy = st.builds(
    Order,
    DicountLvl=
        st.integers(),
    UserID=
        st.integers(),
    Total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    OrderID=
        st.integers(),
    Date=
        st.dates()
)
Table_strategy = st.builds(
    Table,
    Occupied=
        st.integers(),
    TableNo=
        st.integers()
)
Users_strategy = st.builds(
    Users,
    UserID=
        st.integers(),
    UserName=
        safe_text,
    UserLevel=
        st.integers()
)

@given(instance=BookedTables_strategy)
@settings(max_examples=50)
def test_bookedtables_instantiation(instance):
    assert isinstance(instance, BookedTables)



@given(instance=BookedTables_strategy)
def test_bookedtables_TableNo_setter(instance):
    original = instance.TableNo
    instance.TableNo = original
    assert instance.TableNo == original



@given(instance=BookedTables_strategy)
def test_bookedtables_BookingID_setter(instance):
    original = instance.BookingID
    instance.BookingID = original
    assert instance.BookingID == original

@given(instance=Bookings_strategy)
@settings(max_examples=50)
def test_bookings_instantiation(instance):
    assert isinstance(instance, Bookings)



@given(instance=Bookings_strategy)
def test_bookings_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Bookings_strategy)
def test_bookings_BookingID_setter(instance):
    original = instance.BookingID
    instance.BookingID = original
    assert instance.BookingID == original



@given(instance=Bookings_strategy)
def test_bookings_People_setter(instance):
    original = instance.People
    instance.People = original
    assert instance.People == original



@given(instance=Bookings_strategy)
def test_bookings_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=Bookings_strategy)
def test_bookings_TableNo_setter(instance):
    original = instance.TableNo
    instance.TableNo = original
    assert instance.TableNo == original



@given(instance=Bookings_strategy)
def test_bookings_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Bookings_strategy)
def test_bookings_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original

@given(instance=OrderItem_strategy)
@settings(max_examples=50)
def test_orderitem_instantiation(instance):
    assert isinstance(instance, OrderItem)



@given(instance=OrderItem_strategy)
def test_orderitem_RemaningTime_setter(instance):
    original = instance.RemaningTime
    instance.RemaningTime = original
    assert instance.RemaningTime == original



@given(instance=OrderItem_strategy)
def test_orderitem_ItemName_setter(instance):
    original = instance.ItemName
    instance.ItemName = original
    assert instance.ItemName == original



@given(instance=OrderItem_strategy)
def test_orderitem_Completed_setter(instance):
    original = instance.Completed
    instance.Completed = original
    assert instance.Completed == original

@given(instance=ViewOrder_strategy)
@settings(max_examples=50)
def test_vieworder_instantiation(instance):
    assert isinstance(instance, ViewOrder)



@given(instance=ViewOrder_strategy)
def test_vieworder_getUser_setter(instance):
    original = instance.getUser
    instance.getUser = original
    assert instance.getUser == original

@given(instance=Membership_Card_strategy)
@settings(max_examples=50)
def test_membership_card_instantiation(instance):
    assert isinstance(instance, Membership_Card)



@given(instance=Membership_Card_strategy)
def test_membership_card_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Membership_Card_strategy)
def test_membership_card_DiscountLVL_setter(instance):
    original = instance.DiscountLVL
    instance.DiscountLVL = original
    assert instance.DiscountLVL == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_DicountLvl_setter(instance):
    original = instance.DicountLvl
    instance.DicountLvl = original
    assert instance.DicountLvl == original



@given(instance=Order_strategy)
def test_order_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=Order_strategy)
def test_order_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original



@given(instance=Order_strategy)
def test_order_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Order_strategy)
def test_order_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

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

@given(instance=Users_strategy)
@settings(max_examples=50)
def test_users_instantiation(instance):
    assert isinstance(instance, Users)



@given(instance=Users_strategy)
def test_users_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=Users_strategy)
def test_users_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Users_strategy)
def test_users_UserLevel_setter(instance):
    original = instance.UserLevel
    instance.UserLevel = original
    assert instance.UserLevel == original
