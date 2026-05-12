import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Credit_Card,
    Debit_Card,
    Hotel,
    Payment,
    Room,
    Admin,
    Customer,
    Booking,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_credit_card_is_not_abstract():
    assert not inspect.isabstract(Credit_Card)


def test_credit_card_constructor_exists():
    assert callable(Credit_Card.__init__)


def test_credit_card_constructor_args():
    sig = inspect.signature(Credit_Card.__init__)
    params = list(sig.parameters.keys())
    assert "Card_No_" in params, "Missing parameter 'Card_No_'"
    assert "Pin_No_" in params, "Missing parameter 'Pin_No_'"

def test_credit_card_has_Card_No_():
    assert hasattr(Credit_Card, "Card_No_")
    descriptor = None
    for klass in Credit_Card.__mro__:
        if "Card_No_" in klass.__dict__:
            descriptor = klass.__dict__["Card_No_"]
            break
    assert isinstance(descriptor, property)

def test_credit_card_has_Pin_No_():
    assert hasattr(Credit_Card, "Pin_No_")
    descriptor = None
    for klass in Credit_Card.__mro__:
        if "Pin_No_" in klass.__dict__:
            descriptor = klass.__dict__["Pin_No_"]
            break
    assert isinstance(descriptor, property)



def test_debit_card_is_not_abstract():
    assert not inspect.isabstract(Debit_Card)


def test_debit_card_constructor_exists():
    assert callable(Debit_Card.__init__)


def test_debit_card_constructor_args():
    sig = inspect.signature(Debit_Card.__init__)
    params = list(sig.parameters.keys())
    assert "Card_No_" in params, "Missing parameter 'Card_No_'"
    assert "Pin_No_" in params, "Missing parameter 'Pin_No_'"

def test_debit_card_has_Card_No_():
    assert hasattr(Debit_Card, "Card_No_")
    descriptor = None
    for klass in Debit_Card.__mro__:
        if "Card_No_" in klass.__dict__:
            descriptor = klass.__dict__["Card_No_"]
            break
    assert isinstance(descriptor, property)

def test_debit_card_has_Pin_No_():
    assert hasattr(Debit_Card, "Pin_No_")
    descriptor = None
    for klass in Debit_Card.__mro__:
        if "Pin_No_" in klass.__dict__:
            descriptor = klass.__dict__["Pin_No_"]
            break
    assert isinstance(descriptor, property)



def test_hotel_is_not_abstract():
    assert not inspect.isabstract(Hotel)


def test_hotel_constructor_exists():
    assert callable(Hotel.__init__)


def test_hotel_constructor_args():
    sig = inspect.signature(Hotel.__init__)
    params = list(sig.parameters.keys())
    assert "Hotel_Address" in params, "Missing parameter 'Hotel_Address'"
    assert "Hotel_Type" in params, "Missing parameter 'Hotel_Type'"
    assert "Hotel_Rent" in params, "Missing parameter 'Hotel_Rent'"
    assert "Hotel_Name" in params, "Missing parameter 'Hotel_Name'"
    assert "Hotel_ID" in params, "Missing parameter 'Hotel_ID'"

def test_hotel_has_Hotel_Address():
    assert hasattr(Hotel, "Hotel_Address")
    descriptor = None
    for klass in Hotel.__mro__:
        if "Hotel_Address" in klass.__dict__:
            descriptor = klass.__dict__["Hotel_Address"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_Hotel_Type():
    assert hasattr(Hotel, "Hotel_Type")
    descriptor = None
    for klass in Hotel.__mro__:
        if "Hotel_Type" in klass.__dict__:
            descriptor = klass.__dict__["Hotel_Type"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_Hotel_Rent():
    assert hasattr(Hotel, "Hotel_Rent")
    descriptor = None
    for klass in Hotel.__mro__:
        if "Hotel_Rent" in klass.__dict__:
            descriptor = klass.__dict__["Hotel_Rent"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_Hotel_Name():
    assert hasattr(Hotel, "Hotel_Name")
    descriptor = None
    for klass in Hotel.__mro__:
        if "Hotel_Name" in klass.__dict__:
            descriptor = klass.__dict__["Hotel_Name"]
            break
    assert isinstance(descriptor, property)

def test_hotel_has_Hotel_ID():
    assert hasattr(Hotel, "Hotel_ID")
    descriptor = None
    for klass in Hotel.__mro__:
        if "Hotel_ID" in klass.__dict__:
            descriptor = klass.__dict__["Hotel_ID"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Customer_s_Id" in params, "Missing parameter 'Customer_s_Id'"
    assert "Payment_Description" in params, "Missing parameter 'Payment_Description'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Payment_Date" in params, "Missing parameter 'Payment_Date'"

def test_payment_has_Customer_s_Id():
    assert hasattr(Payment, "Customer_s_Id")
    descriptor = None
    for klass in Payment.__mro__:
        if "Customer_s_Id" in klass.__dict__:
            descriptor = klass.__dict__["Customer_s_Id"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Payment_Description():
    assert hasattr(Payment, "Payment_Description")
    descriptor = None
    for klass in Payment.__mro__:
        if "Payment_Description" in klass.__dict__:
            descriptor = klass.__dict__["Payment_Description"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Amount():
    assert hasattr(Payment, "Amount")
    descriptor = None
    for klass in Payment.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Payment_Date():
    assert hasattr(Payment, "Payment_Date")
    descriptor = None
    for klass in Payment.__mro__:
        if "Payment_Date" in klass.__dict__:
            descriptor = klass.__dict__["Payment_Date"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "Room_description" in params, "Missing parameter 'Room_description'"
    assert "Room_type" in params, "Missing parameter 'Room_type'"
    assert "Room_number" in params, "Missing parameter 'Room_number'"
    assert "Room_Id" in params, "Missing parameter 'Room_Id'"

def test_room_has_Room_description():
    assert hasattr(Room, "Room_description")
    descriptor = None
    for klass in Room.__mro__:
        if "Room_description" in klass.__dict__:
            descriptor = klass.__dict__["Room_description"]
            break
    assert isinstance(descriptor, property)

def test_room_has_Room_type():
    assert hasattr(Room, "Room_type")
    descriptor = None
    for klass in Room.__mro__:
        if "Room_type" in klass.__dict__:
            descriptor = klass.__dict__["Room_type"]
            break
    assert isinstance(descriptor, property)

def test_room_has_Room_number():
    assert hasattr(Room, "Room_number")
    descriptor = None
    for klass in Room.__mro__:
        if "Room_number" in klass.__dict__:
            descriptor = klass.__dict__["Room_number"]
            break
    assert isinstance(descriptor, property)

def test_room_has_Room_Id():
    assert hasattr(Room, "Room_Id")
    descriptor = None
    for klass in Room.__mro__:
        if "Room_Id" in klass.__dict__:
            descriptor = klass.__dict__["Room_Id"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_admin_has_Password():
    assert hasattr(Admin, "Password")
    descriptor = None
    for klass in Admin.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Id():
    assert hasattr(Admin, "Id")
    descriptor = None
    for klass in Admin.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Name():
    assert hasattr(Admin, "Name")
    descriptor = None
    for klass in Admin.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Mobile_no___Email" in params, "Missing parameter 'Mobile_no___Email'"

def test_customer_has_Address():
    assert hasattr(Customer, "Address")
    descriptor = None
    for klass in Customer.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Name():
    assert hasattr(Customer, "Name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Id():
    assert hasattr(Customer, "Id")
    descriptor = None
    for klass in Customer.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Mobile_no___Email():
    assert hasattr(Customer, "Mobile_no___Email")
    descriptor = None
    for klass in Customer.__mro__:
        if "Mobile_no___Email" in klass.__dict__:
            descriptor = klass.__dict__["Mobile_no___Email"]
            break
    assert isinstance(descriptor, property)



def test_booking_is_not_abstract():
    assert not inspect.isabstract(Booking)


def test_booking_constructor_exists():
    assert callable(Booking.__init__)


def test_booking_constructor_args():
    sig = inspect.signature(Booking.__init__)
    params = list(sig.parameters.keys())
    assert "Date" in params, "Missing parameter 'Date'"
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Id" in params, "Missing parameter 'Id'"
    assert "Description" in params, "Missing parameter 'Description'"

def test_booking_has_Date():
    assert hasattr(Booking, "Date")
    descriptor = None
    for klass in Booking.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Type():
    assert hasattr(Booking, "Type")
    descriptor = None
    for klass in Booking.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Id():
    assert hasattr(Booking, "Id")
    descriptor = None
    for klass in Booking.__mro__:
        if "Id" in klass.__dict__:
            descriptor = klass.__dict__["Id"]
            break
    assert isinstance(descriptor, property)

def test_booking_has_Description():
    assert hasattr(Booking, "Description")
    descriptor = None
    for klass in Booking.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
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
Credit_Card_strategy = st.builds(
    Credit_Card,
    Card_No_=
        safe_text,
    Pin_No_=
        safe_text
)
Debit_Card_strategy = st.builds(
    Debit_Card,
    Card_No_=
        safe_text,
    Pin_No_=
        safe_text
)
Hotel_strategy = st.builds(
    Hotel,
    Hotel_Address=
        safe_text,
    Hotel_Type=
        safe_text,
    Hotel_Rent=
        safe_text,
    Hotel_Name=
        safe_text,
    Hotel_ID=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    Customer_s_Id=
        safe_text,
    Payment_Description=
        safe_text,
    Amount=
        safe_text,
    Payment_Date=
        safe_text
)
Room_strategy = st.builds(
    Room,
    Room_description=
        safe_text,
    Room_type=
        safe_text,
    Room_number=
        safe_text,
    Room_Id=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    Password=
        safe_text,
    Id=
        safe_text,
    Name=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    Address=
        safe_text,
    Name=
        safe_text,
    Id=
        safe_text,
    Mobile_no___Email=
        safe_text
)
Booking_strategy = st.builds(
    Booking,
    Date=
        safe_text,
    Type=
        safe_text,
    Id=
        safe_text,
    Description=
        safe_text
)

@given(instance=Credit_Card_strategy)
@settings(max_examples=50)
def test_credit_card_instantiation(instance):
    assert isinstance(instance, Credit_Card)



@given(instance=Credit_Card_strategy)
def test_credit_card_Card_No__setter(instance):
    original = instance.Card_No_
    instance.Card_No_ = original
    assert instance.Card_No_ == original



@given(instance=Credit_Card_strategy)
def test_credit_card_Pin_No__setter(instance):
    original = instance.Pin_No_
    instance.Pin_No_ = original
    assert instance.Pin_No_ == original

@given(instance=Debit_Card_strategy)
@settings(max_examples=50)
def test_debit_card_instantiation(instance):
    assert isinstance(instance, Debit_Card)



@given(instance=Debit_Card_strategy)
def test_debit_card_Card_No__setter(instance):
    original = instance.Card_No_
    instance.Card_No_ = original
    assert instance.Card_No_ == original



@given(instance=Debit_Card_strategy)
def test_debit_card_Pin_No__setter(instance):
    original = instance.Pin_No_
    instance.Pin_No_ = original
    assert instance.Pin_No_ == original

@given(instance=Hotel_strategy)
@settings(max_examples=50)
def test_hotel_instantiation(instance):
    assert isinstance(instance, Hotel)



@given(instance=Hotel_strategy)
def test_hotel_Hotel_Address_setter(instance):
    original = instance.Hotel_Address
    instance.Hotel_Address = original
    assert instance.Hotel_Address == original



@given(instance=Hotel_strategy)
def test_hotel_Hotel_Type_setter(instance):
    original = instance.Hotel_Type
    instance.Hotel_Type = original
    assert instance.Hotel_Type == original



@given(instance=Hotel_strategy)
def test_hotel_Hotel_Rent_setter(instance):
    original = instance.Hotel_Rent
    instance.Hotel_Rent = original
    assert instance.Hotel_Rent == original



@given(instance=Hotel_strategy)
def test_hotel_Hotel_Name_setter(instance):
    original = instance.Hotel_Name
    instance.Hotel_Name = original
    assert instance.Hotel_Name == original



@given(instance=Hotel_strategy)
def test_hotel_Hotel_ID_setter(instance):
    original = instance.Hotel_ID
    instance.Hotel_ID = original
    assert instance.Hotel_ID == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Customer_s_Id_setter(instance):
    original = instance.Customer_s_Id
    instance.Customer_s_Id = original
    assert instance.Customer_s_Id == original



@given(instance=Payment_strategy)
def test_payment_Payment_Description_setter(instance):
    original = instance.Payment_Description
    instance.Payment_Description = original
    assert instance.Payment_Description == original



@given(instance=Payment_strategy)
def test_payment_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=Payment_strategy)
def test_payment_Payment_Date_setter(instance):
    original = instance.Payment_Date
    instance.Payment_Date = original
    assert instance.Payment_Date == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_Room_description_setter(instance):
    original = instance.Room_description
    instance.Room_description = original
    assert instance.Room_description == original



@given(instance=Room_strategy)
def test_room_Room_type_setter(instance):
    original = instance.Room_type
    instance.Room_type = original
    assert instance.Room_type == original



@given(instance=Room_strategy)
def test_room_Room_number_setter(instance):
    original = instance.Room_number
    instance.Room_number = original
    assert instance.Room_number == original



@given(instance=Room_strategy)
def test_room_Room_Id_setter(instance):
    original = instance.Room_Id
    instance.Room_Id = original
    assert instance.Room_Id == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Admin_strategy)
def test_admin_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Admin_strategy)
def test_admin_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Customer_strategy)
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Customer_strategy)
def test_customer_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Customer_strategy)
def test_customer_Mobile_no___Email_setter(instance):
    original = instance.Mobile_no___Email
    instance.Mobile_no___Email = original
    assert instance.Mobile_no___Email == original

@given(instance=Booking_strategy)
@settings(max_examples=50)
def test_booking_instantiation(instance):
    assert isinstance(instance, Booking)



@given(instance=Booking_strategy)
def test_booking_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Booking_strategy)
def test_booking_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original



@given(instance=Booking_strategy)
def test_booking_Id_setter(instance):
    original = instance.Id
    instance.Id = original
    assert instance.Id == original



@given(instance=Booking_strategy)
def test_booking_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original
