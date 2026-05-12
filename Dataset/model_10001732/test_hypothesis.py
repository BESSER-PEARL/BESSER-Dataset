import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Category,
    Food_Items,
    Cash_on_delievery,
    Bank,
    Payment,
    System_order,
    Customer,
    Admin,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_category_is_not_abstract():
    assert not inspect.isabstract(Category)


def test_category_constructor_exists():
    assert callable(Category.__init__)


def test_category_constructor_args():
    sig = inspect.signature(Category.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_category_has_ID():
    assert hasattr(Category, "ID")
    descriptor = None
    for klass in Category.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_category_has_Type():
    assert hasattr(Category, "Type")
    descriptor = None
    for klass in Category.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_food_items_is_not_abstract():
    assert not inspect.isabstract(Food_Items)


def test_food_items_constructor_exists():
    assert callable(Food_Items.__init__)


def test_food_items_constructor_args():
    sig = inspect.signature(Food_Items.__init__)
    params = list(sig.parameters.keys())
    assert "Items_Manage" in params, "Missing parameter 'Items_Manage'"
    assert "item_photo" in params, "Missing parameter 'item_photo'"
    assert "Items_Detail" in params, "Missing parameter 'Items_Detail'"
    assert "Items_Price" in params, "Missing parameter 'Items_Price'"
    assert "Item_Name" in params, "Missing parameter 'Item_Name'"
    assert "Items_ID" in params, "Missing parameter 'Items_ID'"

def test_food_items_has_Items_Manage():
    assert hasattr(Food_Items, "Items_Manage")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "Items_Manage" in klass.__dict__:
            descriptor = klass.__dict__["Items_Manage"]
            break
    assert isinstance(descriptor, property)

def test_food_items_has_item_photo():
    assert hasattr(Food_Items, "item_photo")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "item_photo" in klass.__dict__:
            descriptor = klass.__dict__["item_photo"]
            break
    assert isinstance(descriptor, property)

def test_food_items_has_Items_Detail():
    assert hasattr(Food_Items, "Items_Detail")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "Items_Detail" in klass.__dict__:
            descriptor = klass.__dict__["Items_Detail"]
            break
    assert isinstance(descriptor, property)

def test_food_items_has_Items_Price():
    assert hasattr(Food_Items, "Items_Price")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "Items_Price" in klass.__dict__:
            descriptor = klass.__dict__["Items_Price"]
            break
    assert isinstance(descriptor, property)

def test_food_items_has_Item_Name():
    assert hasattr(Food_Items, "Item_Name")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "Item_Name" in klass.__dict__:
            descriptor = klass.__dict__["Item_Name"]
            break
    assert isinstance(descriptor, property)

def test_food_items_has_Items_ID():
    assert hasattr(Food_Items, "Items_ID")
    descriptor = None
    for klass in Food_Items.__mro__:
        if "Items_ID" in klass.__dict__:
            descriptor = klass.__dict__["Items_ID"]
            break
    assert isinstance(descriptor, property)



def test_cash_on_delievery_is_not_abstract():
    assert not inspect.isabstract(Cash_on_delievery)


def test_cash_on_delievery_constructor_exists():
    assert callable(Cash_on_delievery.__init__)


def test_cash_on_delievery_constructor_args():
    sig = inspect.signature(Cash_on_delievery.__init__)
    params = list(sig.parameters.keys())
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "Phone_number" in params, "Missing parameter 'Phone_number'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Customer_Name" in params, "Missing parameter 'Customer_Name'"

def test_cash_on_delievery_has_Amount():
    assert hasattr(Cash_on_delievery, "Amount")
    descriptor = None
    for klass in Cash_on_delievery.__mro__:
        if "Amount" in klass.__dict__:
            descriptor = klass.__dict__["Amount"]
            break
    assert isinstance(descriptor, property)

def test_cash_on_delievery_has_Phone_number():
    assert hasattr(Cash_on_delievery, "Phone_number")
    descriptor = None
    for klass in Cash_on_delievery.__mro__:
        if "Phone_number" in klass.__dict__:
            descriptor = klass.__dict__["Phone_number"]
            break
    assert isinstance(descriptor, property)

def test_cash_on_delievery_has_Address():
    assert hasattr(Cash_on_delievery, "Address")
    descriptor = None
    for klass in Cash_on_delievery.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_cash_on_delievery_has_Customer_Name():
    assert hasattr(Cash_on_delievery, "Customer_Name")
    descriptor = None
    for klass in Cash_on_delievery.__mro__:
        if "Customer_Name" in klass.__dict__:
            descriptor = klass.__dict__["Customer_Name"]
            break
    assert isinstance(descriptor, property)



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "Account_type" in params, "Missing parameter 'Account_type'"
    assert "Account_no" in params, "Missing parameter 'Account_no'"
    assert "Online_payment_ID_and_password" in params, "Missing parameter 'Online_payment_ID_and_password'"

def test_bank_has_Account_type():
    assert hasattr(Bank, "Account_type")
    descriptor = None
    for klass in Bank.__mro__:
        if "Account_type" in klass.__dict__:
            descriptor = klass.__dict__["Account_type"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_Account_no():
    assert hasattr(Bank, "Account_no")
    descriptor = None
    for klass in Bank.__mro__:
        if "Account_no" in klass.__dict__:
            descriptor = klass.__dict__["Account_no"]
            break
    assert isinstance(descriptor, property)

def test_bank_has_Online_payment_ID_and_password():
    assert hasattr(Bank, "Online_payment_ID_and_password")
    descriptor = None
    for klass in Bank.__mro__:
        if "Online_payment_ID_and_password" in klass.__dict__:
            descriptor = klass.__dict__["Online_payment_ID_and_password"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Payment_Option" in params, "Missing parameter 'Payment_Option'"
    assert "Amount" in params, "Missing parameter 'Amount'"

def test_payment_has_Payment_Option():
    assert hasattr(Payment, "Payment_Option")
    descriptor = None
    for klass in Payment.__mro__:
        if "Payment_Option" in klass.__dict__:
            descriptor = klass.__dict__["Payment_Option"]
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



def test_system_order_is_not_abstract():
    assert not inspect.isabstract(System_order)


def test_system_order_constructor_exists():
    assert callable(System_order.__init__)


def test_system_order_constructor_args():
    sig = inspect.signature(System_order.__init__)
    params = list(sig.parameters.keys())
    assert "Time" in params, "Missing parameter 'Time'"
    assert "Delivery_Charges" in params, "Missing parameter 'Delivery_Charges'"
    assert "Customer_Name" in params, "Missing parameter 'Customer_Name'"
    assert "Order_ID" in params, "Missing parameter 'Order_ID'"
    assert "Customer_ID" in params, "Missing parameter 'Customer_ID'"
    assert "Total" in params, "Missing parameter 'Total'"
    assert "Payment_Option" in params, "Missing parameter 'Payment_Option'"
    assert "Date" in params, "Missing parameter 'Date'"

def test_system_order_has_Time():
    assert hasattr(System_order, "Time")
    descriptor = None
    for klass in System_order.__mro__:
        if "Time" in klass.__dict__:
            descriptor = klass.__dict__["Time"]
            break
    assert isinstance(descriptor, property)

def test_system_order_has_Delivery_Charges():
    assert hasattr(System_order, "Delivery_Charges")
    descriptor = None
    for klass in System_order.__mro__:
        if "Delivery_Charges" in klass.__dict__:
            descriptor = klass.__dict__["Delivery_Charges"]
            break
    assert isinstance(descriptor, property)

def test_system_order_has_Customer_Name():
    assert hasattr(System_order, "Customer_Name")
    descriptor = None
    for klass in System_order.__mro__:
        if "Customer_Name" in klass.__dict__:
            descriptor = klass.__dict__["Customer_Name"]
            break
    assert isinstance(descriptor, property)

def test_system_order_has_Order_ID():
    assert hasattr(System_order, "Order_ID")
    descriptor = None
    for klass in System_order.__mro__:
        if "Order_ID" in klass.__dict__:
            descriptor = klass.__dict__["Order_ID"]
            break
    assert isinstance(descriptor, property)

def test_system_order_has_Customer_ID():
    assert hasattr(System_order, "Customer_ID")
    descriptor = None
    for klass in System_order.__mro__:
        if "Customer_ID" in klass.__dict__:
            descriptor = klass.__dict__["Customer_ID"]
            break
    assert isinstance(descriptor, property)

def test_system_order_has_Total():
    assert hasattr(System_order, "Total")
    descriptor = None
    for klass in System_order.__mro__:
        if "Total" in klass.__dict__:
            descriptor = klass.__dict__["Total"]
            break
    assert isinstance(descriptor, property)

def test_system_order_has_Payment_Option():
    assert hasattr(System_order, "Payment_Option")
    descriptor = None
    for klass in System_order.__mro__:
        if "Payment_Option" in klass.__dict__:
            descriptor = klass.__dict__["Payment_Option"]
            break
    assert isinstance(descriptor, property)

def test_system_order_has_Date():
    assert hasattr(System_order, "Date")
    descriptor = None
    for klass in System_order.__mro__:
        if "Date" in klass.__dict__:
            descriptor = klass.__dict__["Date"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "User_Password" in params, "Missing parameter 'User_Password'"
    assert "User_Name" in params, "Missing parameter 'User_Name'"
    assert "User_Type" in params, "Missing parameter 'User_Type'"
    assert "User_ID" in params, "Missing parameter 'User_ID'"

def test_user_has_User_Password():
    assert hasattr(User, "User_Password")
    descriptor = None
    for klass in User.__mro__:
        if "User_Password" in klass.__dict__:
            descriptor = klass.__dict__["User_Password"]
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

def test_user_has_User_Type():
    assert hasattr(User, "User_Type")
    descriptor = None
    for klass in User.__mro__:
        if "User_Type" in klass.__dict__:
            descriptor = klass.__dict__["User_Type"]
            break
    assert isinstance(descriptor, property)

def test_user_has_User_ID():
    assert hasattr(User, "User_ID")
    descriptor = None
    for klass in User.__mro__:
        if "User_ID" in klass.__dict__:
            descriptor = klass.__dict__["User_ID"]
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
Category_strategy = st.builds(
    Category,
    ID=
        st.integers(),
    Type=
        safe_text
)
Food_Items_strategy = st.builds(
    Food_Items,
    Items_Manage=
        st.none(),
    item_photo=
        safe_text,
    Items_Detail=
        safe_text,
    Items_Price=
        st.integers(),
    Item_Name=
        safe_text,
    Items_ID=
        st.integers()
)
Cash_on_delievery_strategy = st.builds(
    Cash_on_delievery,
    Amount=
        safe_text,
    Phone_number=
        st.integers(),
    Address=
        safe_text,
    Customer_Name=
        safe_text
)
Bank_strategy = st.builds(
    Bank,
    Account_type=
        safe_text,
    Account_no=
        st.integers(),
    Online_payment_ID_and_password=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    Payment_Option=
        safe_text,
    Amount=
        st.integers()
)
System_order_strategy = st.builds(
    System_order,
    Time=
        st.integers(),
    Delivery_Charges=
        st.integers(),
    Customer_Name=
        safe_text,
    Order_ID=
        st.integers(),
    Customer_ID=
        st.integers(),
    Total=
        st.integers(),
    Payment_Option=
        safe_text,
    Date=
        st.integers()
)
Customer_strategy = st.builds(
    Customer,
)
Admin_strategy = st.builds(
    Admin,
)
User_strategy = st.builds(
    User,
    User_Password=
        safe_text,
    User_Name=
        safe_text,
    User_Type=
        safe_text,
    User_ID=
        st.integers()
)

@given(instance=Category_strategy)
@settings(max_examples=50)
def test_category_instantiation(instance):
    assert isinstance(instance, Category)



@given(instance=Category_strategy)
def test_category_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Category_strategy)
def test_category_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=Food_Items_strategy)
@settings(max_examples=50)
def test_food_items_instantiation(instance):
    assert isinstance(instance, Food_Items)



@given(instance=Food_Items_strategy)
def test_food_items_Items_Manage_setter(instance):
    original = instance.Items_Manage
    instance.Items_Manage = original
    assert instance.Items_Manage == original



@given(instance=Food_Items_strategy)
def test_food_items_item_photo_setter(instance):
    original = instance.item_photo
    instance.item_photo = original
    assert instance.item_photo == original



@given(instance=Food_Items_strategy)
def test_food_items_Items_Detail_setter(instance):
    original = instance.Items_Detail
    instance.Items_Detail = original
    assert instance.Items_Detail == original



@given(instance=Food_Items_strategy)
def test_food_items_Items_Price_setter(instance):
    original = instance.Items_Price
    instance.Items_Price = original
    assert instance.Items_Price == original



@given(instance=Food_Items_strategy)
def test_food_items_Item_Name_setter(instance):
    original = instance.Item_Name
    instance.Item_Name = original
    assert instance.Item_Name == original



@given(instance=Food_Items_strategy)
def test_food_items_Items_ID_setter(instance):
    original = instance.Items_ID
    instance.Items_ID = original
    assert instance.Items_ID == original

@given(instance=Cash_on_delievery_strategy)
@settings(max_examples=50)
def test_cash_on_delievery_instantiation(instance):
    assert isinstance(instance, Cash_on_delievery)



@given(instance=Cash_on_delievery_strategy)
def test_cash_on_delievery_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=Cash_on_delievery_strategy)
def test_cash_on_delievery_Phone_number_setter(instance):
    original = instance.Phone_number
    instance.Phone_number = original
    assert instance.Phone_number == original



@given(instance=Cash_on_delievery_strategy)
def test_cash_on_delievery_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Cash_on_delievery_strategy)
def test_cash_on_delievery_Customer_Name_setter(instance):
    original = instance.Customer_Name
    instance.Customer_Name = original
    assert instance.Customer_Name == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_Account_type_setter(instance):
    original = instance.Account_type
    instance.Account_type = original
    assert instance.Account_type == original



@given(instance=Bank_strategy)
def test_bank_Account_no_setter(instance):
    original = instance.Account_no
    instance.Account_no = original
    assert instance.Account_no == original



@given(instance=Bank_strategy)
def test_bank_Online_payment_ID_and_password_setter(instance):
    original = instance.Online_payment_ID_and_password
    instance.Online_payment_ID_and_password = original
    assert instance.Online_payment_ID_and_password == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Payment_Option_setter(instance):
    original = instance.Payment_Option
    instance.Payment_Option = original
    assert instance.Payment_Option == original



@given(instance=Payment_strategy)
def test_payment_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original

@given(instance=System_order_strategy)
@settings(max_examples=50)
def test_system_order_instantiation(instance):
    assert isinstance(instance, System_order)



@given(instance=System_order_strategy)
def test_system_order_Time_setter(instance):
    original = instance.Time
    instance.Time = original
    assert instance.Time == original



@given(instance=System_order_strategy)
def test_system_order_Delivery_Charges_setter(instance):
    original = instance.Delivery_Charges
    instance.Delivery_Charges = original
    assert instance.Delivery_Charges == original



@given(instance=System_order_strategy)
def test_system_order_Customer_Name_setter(instance):
    original = instance.Customer_Name
    instance.Customer_Name = original
    assert instance.Customer_Name == original



@given(instance=System_order_strategy)
def test_system_order_Order_ID_setter(instance):
    original = instance.Order_ID
    instance.Order_ID = original
    assert instance.Order_ID == original



@given(instance=System_order_strategy)
def test_system_order_Customer_ID_setter(instance):
    original = instance.Customer_ID
    instance.Customer_ID = original
    assert instance.Customer_ID == original



@given(instance=System_order_strategy)
def test_system_order_Total_setter(instance):
    original = instance.Total
    instance.Total = original
    assert instance.Total == original



@given(instance=System_order_strategy)
def test_system_order_Payment_Option_setter(instance):
    original = instance.Payment_Option
    instance.Payment_Option = original
    assert instance.Payment_Option == original



@given(instance=System_order_strategy)
def test_system_order_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_User_Password_setter(instance):
    original = instance.User_Password
    instance.User_Password = original
    assert instance.User_Password == original



@given(instance=User_strategy)
def test_user_User_Name_setter(instance):
    original = instance.User_Name
    instance.User_Name = original
    assert instance.User_Name == original



@given(instance=User_strategy)
def test_user_User_Type_setter(instance):
    original = instance.User_Type
    instance.User_Type = original
    assert instance.User_Type == original



@given(instance=User_strategy)
def test_user_User_ID_setter(instance):
    original = instance.User_ID
    instance.User_ID = original
    assert instance.User_ID == original
