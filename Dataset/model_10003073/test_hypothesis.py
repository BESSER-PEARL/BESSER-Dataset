import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    User,
    Registration,
    Cart,
    StaffUI,
    Chef,
    Product,
    Order,
    Invoice,
    Table,
    Booking,
    ReservationManagementSystem,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "Passowrd" in params, "Missing parameter 'Passowrd'"
    assert "User_Name" in params, "Missing parameter 'User_Name'"

def test_user_has_Passowrd():
    assert hasattr(User, "Passowrd")
    descriptor = None
    for klass in User.__mro__:
        if "Passowrd" in klass.__dict__:
            descriptor = klass.__dict__["Passowrd"]
            break
    assert isinstance(descriptor, property)

def test_user_has_User_Name():
    assert hasattr(User, "User_Name")
    descriptor = None
    for klass in User.__mro__:
        if "User_Name" in klass.__dict__:
            descriptor = klass.__dict__["User_Name"]
            break
    assert isinstance(descriptor, property)



def test_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "attribute5" in params, "Missing parameter 'attribute5'"
    assert "First_Name" in params, "Missing parameter 'First_Name'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Last_Name" in params, "Missing parameter 'Last_Name'"
    assert "Gender" in params, "Missing parameter 'Gender'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_registration_has_attribute():
    assert hasattr(Registration, "attribute")
    descriptor = None
    for klass in Registration.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_UserName():
    assert hasattr(Registration, "UserName")
    descriptor = None
    for klass in Registration.__mro__:
        if "UserName" in klass.__dict__:
            descriptor = klass.__dict__["UserName"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_attribute5():
    assert hasattr(Registration, "attribute5")
    descriptor = None
    for klass in Registration.__mro__:
        if "attribute5" in klass.__dict__:
            descriptor = klass.__dict__["attribute5"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_First_Name():
    assert hasattr(Registration, "First_Name")
    descriptor = None
    for klass in Registration.__mro__:
        if "First_Name" in klass.__dict__:
            descriptor = klass.__dict__["First_Name"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Password():
    assert hasattr(Registration, "Password")
    descriptor = None
    for klass in Registration.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Last_Name():
    assert hasattr(Registration, "Last_Name")
    descriptor = None
    for klass in Registration.__mro__:
        if "Last_Name" in klass.__dict__:
            descriptor = klass.__dict__["Last_Name"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Gender():
    assert hasattr(Registration, "Gender")
    descriptor = None
    for klass in Registration.__mro__:
        if "Gender" in klass.__dict__:
            descriptor = klass.__dict__["Gender"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Email():
    assert hasattr(Registration, "Email")
    descriptor = None
    for klass in Registration.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())
    assert "Product" in params, "Missing parameter 'Product'"

def test_cart_has_Product():
    assert hasattr(Cart, "Product")
    descriptor = None
    for klass in Cart.__mro__:
        if "Product" in klass.__dict__:
            descriptor = klass.__dict__["Product"]
            break
    assert isinstance(descriptor, property)



def test_staffui_is_not_abstract():
    assert not inspect.isabstract(StaffUI)


def test_staffui_constructor_exists():
    assert callable(StaffUI.__init__)


def test_staffui_constructor_args():
    sig = inspect.signature(StaffUI.__init__)
    params = list(sig.parameters.keys())



def test_chef_is_not_abstract():
    assert not inspect.isabstract(Chef)


def test_chef_constructor_exists():
    assert callable(Chef.__init__)


def test_chef_constructor_args():
    sig = inspect.signature(Chef.__init__)
    params = list(sig.parameters.keys())



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "Note" in params, "Missing parameter 'Note'"
    assert "price" in params, "Missing parameter 'price'"
    assert "food_id" in params, "Missing parameter 'food_id'"
    assert "name" in params, "Missing parameter 'name'"

def test_product_has_Note():
    assert hasattr(Product, "Note")
    descriptor = None
    for klass in Product.__mro__:
        if "Note" in klass.__dict__:
            descriptor = klass.__dict__["Note"]
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

def test_product_has_food_id():
    assert hasattr(Product, "food_id")
    descriptor = None
    for klass in Product.__mro__:
        if "food_id" in klass.__dict__:
            descriptor = klass.__dict__["food_id"]
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



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "order_id" in params, "Missing parameter 'order_id'"
    assert "foodList" in params, "Missing parameter 'foodList'"

def test_order_has_order_id():
    assert hasattr(Order, "order_id")
    descriptor = None
    for klass in Order.__mro__:
        if "order_id" in klass.__dict__:
            descriptor = klass.__dict__["order_id"]
            break
    assert isinstance(descriptor, property)

def test_order_has_foodList():
    assert hasattr(Order, "foodList")
    descriptor = None
    for klass in Order.__mro__:
        if "foodList" in klass.__dict__:
            descriptor = klass.__dict__["foodList"]
            break
    assert isinstance(descriptor, property)



def test_invoice_is_not_abstract():
    assert not inspect.isabstract(Invoice)


def test_invoice_constructor_exists():
    assert callable(Invoice.__init__)


def test_invoice_constructor_args():
    sig = inspect.signature(Invoice.__init__)
    params = list(sig.parameters.keys())
    assert "invoice_id" in params, "Missing parameter 'invoice_id'"
    assert "orders" in params, "Missing parameter 'orders'"

def test_invoice_has_invoice_id():
    assert hasattr(Invoice, "invoice_id")
    descriptor = None
    for klass in Invoice.__mro__:
        if "invoice_id" in klass.__dict__:
            descriptor = klass.__dict__["invoice_id"]
            break
    assert isinstance(descriptor, property)

def test_invoice_has_orders():
    assert hasattr(Invoice, "orders")
    descriptor = None
    for klass in Invoice.__mro__:
        if "orders" in klass.__dict__:
            descriptor = klass.__dict__["orders"]
            break
    assert isinstance(descriptor, property)



def test_table_is_not_abstract():
    assert not inspect.isabstract(Table)


def test_table_constructor_exists():
    assert callable(Table.__init__)


def test_table_constructor_args():
    sig = inspect.signature(Table.__init__)
    params = list(sig.parameters.keys())
    assert "numSeats" in params, "Missing parameter 'numSeats'"
    assert "avaliable" in params, "Missing parameter 'avaliable'"
    assert "table_id" in params, "Missing parameter 'table_id'"

def test_table_has_numSeats():
    assert hasattr(Table, "numSeats")
    descriptor = None
    for klass in Table.__mro__:
        if "numSeats" in klass.__dict__:
            descriptor = klass.__dict__["numSeats"]
            break
    assert isinstance(descriptor, property)

def test_table_has_avaliable():
    assert hasattr(Table, "avaliable")
    descriptor = None
    for klass in Table.__mro__:
        if "avaliable" in klass.__dict__:
            descriptor = klass.__dict__["avaliable"]
            break
    assert isinstance(descriptor, property)

def test_table_has_table_id():
    assert hasattr(Table, "table_id")
    descriptor = None
    for klass in Table.__mro__:
        if "table_id" in klass.__dict__:
            descriptor = klass.__dict__["table_id"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "startTime" in params, "Missing parameter 'startTime'"
    assert "endTime" in params, "Missing parameter 'endTime'"
    assert "reservedTables" in params, "Missing parameter 'reservedTables'"
    assert "booking_id" in params, "Missing parameter 'booking_id'"
    assert "customer_name" in params, "Missing parameter 'customer_name'"
    assert "date" in params, "Missing parameter 'date'"

def test_booking_has_startTime():
    assert hasattr(Booking, "startTime")
    descriptor = None
    for klass in Booking.__mro__:
        if "startTime" in klass.__dict__:
            descriptor = klass.__dict__["startTime"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_endTime():
    assert hasattr(Booking, "endTime")
    descriptor = None
    for klass in Booking.__mro__:
        if "endTime" in klass.__dict__:
            descriptor = klass.__dict__["endTime"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_reservedTables():
    assert hasattr(Booking, "reservedTables")
    descriptor = None
    for klass in Booking.__mro__:
        if "reservedTables" in klass.__dict__:
            descriptor = klass.__dict__["reservedTables"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_booking_id():
    assert hasattr(Booking, "booking_id")
    descriptor = None
    for klass in Booking.__mro__:
        if "booking_id" in klass.__dict__:
            descriptor = klass.__dict__["booking_id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_customer_name():
    assert hasattr(Booking, "customer_name")
    descriptor = None
    for klass in Booking.__mro__:
        if "customer_name" in klass.__dict__:
            descriptor = klass.__dict__["customer_name"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_date():
    assert hasattr(Booking, "date")
    descriptor = None
    for klass in Booking.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_reservationmanagementsystem_is_not_abstract():
    assert not inspect.isabstract(ReservationManagementSystem)


def test_reservationmanagementsystem_constructor_exists():
    assert callable(ReservationManagementSystem.__init__)


def test_reservationmanagementsystem_constructor_args():
    sig = inspect.signature(ReservationManagementSystem.__init__)
    params = list(sig.parameters.keys())
    assert "bookings" in params, "Missing parameter 'bookings'"

def test_reservationmanagementsystem_has_bookings():
    assert hasattr(ReservationManagementSystem, "bookings")
    descriptor = None
    for klass in ReservationManagementSystem.__mro__:
        if "bookings" in klass.__dict__:
            descriptor = klass.__dict__["bookings"]
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
User_strategy = st.builds(
    User,
    Passowrd=
        safe_text,
    User_Name=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    attribute=
        safe_text,
    UserName=
        safe_text,
    attribute5=
        safe_text,
    First_Name=
        safe_text,
    Password=
        safe_text,
    Last_Name=
        safe_text,
    Gender=
        safe_text,
    Email=
        safe_text
)
Cart_strategy = st.builds(
    Cart,
    Product=
        st.none()
)
StaffUI_strategy = st.builds(
    StaffUI,
)
Chef_strategy = st.builds(
    Chef,
)
Product_strategy = st.builds(
    Product,
    Note=
        safe_text,
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    food_id=
        safe_text,
    name=
        safe_text
)
Order_strategy = st.builds(
    Order,
    order_id=
        safe_text,
    foodList=
        safe_text
)
Invoice_strategy = st.builds(
    Invoice,
    invoice_id=
        safe_text,
    orders=
        safe_text
)
Table_strategy = st.builds(
    Table,
    numSeats=
        st.integers(),
    avaliable=
        st.booleans(),
    table_id=
        safe_text
)
Booking_strategy = st.builds(
    Booking,
    startTime=
        safe_text,
    endTime=
        safe_text,
    reservedTables=
        safe_text,
    booking_id=
        st.integers(),
    customer_name=
        safe_text,
    date=
        st.dates()
)
ReservationManagementSystem_strategy = st.builds(
    ReservationManagementSystem,
    bookings=
        safe_text
)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_Passowrd_setter(instance):
    original = instance.Passowrd
    instance.Passowrd = original
    assert instance.Passowrd == original



@given(instance=User_strategy)
def test_user_User_Name_setter(instance):
    original = instance.User_Name
    instance.User_Name = original
    assert instance.User_Name == original

@given(instance=Registration_strategy)
@settings(max_examples=50)
def test_registration_instantiation(instance):
    assert isinstance(instance, Registration)



@given(instance=Registration_strategy)
def test_registration_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Registration_strategy)
def test_registration_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Registration_strategy)
def test_registration_attribute5_setter(instance):
    original = instance.attribute5
    instance.attribute5 = original
    assert instance.attribute5 == original



@given(instance=Registration_strategy)
def test_registration_First_Name_setter(instance):
    original = instance.First_Name
    instance.First_Name = original
    assert instance.First_Name == original



@given(instance=Registration_strategy)
def test_registration_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Registration_strategy)
def test_registration_Last_Name_setter(instance):
    original = instance.Last_Name
    instance.Last_Name = original
    assert instance.Last_Name == original



@given(instance=Registration_strategy)
def test_registration_Gender_setter(instance):
    original = instance.Gender
    instance.Gender = original
    assert instance.Gender == original



@given(instance=Registration_strategy)
def test_registration_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Cart_strategy)
@settings(max_examples=50)
def test_cart_instantiation(instance):
    assert isinstance(instance, Cart)



@given(instance=Cart_strategy)
def test_cart_Product_setter(instance):
    original = instance.Product
    instance.Product = original
    assert instance.Product == original

@given(instance=StaffUI_strategy)
@settings(max_examples=50)
def test_staffui_instantiation(instance):
    assert isinstance(instance, StaffUI)

@given(instance=Chef_strategy)
@settings(max_examples=50)
def test_chef_instantiation(instance):
    assert isinstance(instance, Chef)

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_Note_setter(instance):
    original = instance.Note
    instance.Note = original
    assert instance.Note == original



@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Product_strategy)
def test_product_food_id_setter(instance):
    original = instance.food_id
    instance.food_id = original
    assert instance.food_id == original



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_order_id_setter(instance):
    original = instance.order_id
    instance.order_id = original
    assert instance.order_id == original



@given(instance=Order_strategy)
def test_order_foodList_setter(instance):
    original = instance.foodList
    instance.foodList = original
    assert instance.foodList == original

@given(instance=Invoice_strategy)
@settings(max_examples=50)
def test_invoice_instantiation(instance):
    assert isinstance(instance, Invoice)



@given(instance=Invoice_strategy)
def test_invoice_invoice_id_setter(instance):
    original = instance.invoice_id
    instance.invoice_id = original
    assert instance.invoice_id == original



@given(instance=Invoice_strategy)
def test_invoice_orders_setter(instance):
    original = instance.orders
    instance.orders = original
    assert instance.orders == original

@given(instance=Table_strategy)
@settings(max_examples=50)
def test_table_instantiation(instance):
    assert isinstance(instance, Table)



@given(instance=Table_strategy)
def test_table_numSeats_setter(instance):
    original = instance.numSeats
    instance.numSeats = original
    assert instance.numSeats == original



@given(instance=Table_strategy)
def test_table_avaliable_setter(instance):
    original = instance.avaliable
    instance.avaliable = original
    assert instance.avaliable == original



@given(instance=Table_strategy)
def test_table_table_id_setter(instance):
    original = instance.table_id
    instance.table_id = original
    assert instance.table_id == original

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_startTime_setter(instance):
    original = instance.startTime
    instance.startTime = original
    assert instance.startTime == original



@given(instance=Booking_strategy)
def test_booking_endTime_setter(instance):
    original = instance.endTime
    instance.endTime = original
    assert instance.endTime == original



@given(instance=Booking_strategy)
def test_booking_reservedTables_setter(instance):
    original = instance.reservedTables
    instance.reservedTables = original
    assert instance.reservedTables == original



@given(instance=Booking_strategy)
def test_booking_booking_id_setter(instance):
    original = instance.booking_id
    instance.booking_id = original
    assert instance.booking_id == original



@given(instance=Booking_strategy)
def test_booking_customer_name_setter(instance):
    original = instance.customer_name
    instance.customer_name = original
    assert instance.customer_name == original



@given(instance=Booking_strategy)
def test_booking_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=ReservationManagementSystem_strategy)
@settings(max_examples=50)
def test_reservationmanagementsystem_instantiation(instance):
    assert isinstance(instance, ReservationManagementSystem)



@given(instance=ReservationManagementSystem_strategy)
def test_reservationmanagementsystem_bookings_setter(instance):
    original = instance.bookings
    instance.bookings = original
    assert instance.bookings == original
