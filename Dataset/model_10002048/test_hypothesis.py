import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Doctor,
    Shopping_Cart,
    Payment,
    Manager,
    Employee,
    Pets,
    Order,
    Administrator,
    User,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_doctor_is_not_abstract():
    assert not inspect.isabstract(Doctor)


def test_doctor_constructor_exists():
    assert callable(Doctor.__init__)


def test_doctor_constructor_args():
    sig = inspect.signature(Doctor.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "ContactNo" in params, "Missing parameter 'ContactNo'"
    assert "DoctorID" in params, "Missing parameter 'DoctorID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_doctor_has_Email():
    assert hasattr(Doctor, "Email")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_ContactNo():
    assert hasattr(Doctor, "ContactNo")
    descriptor = None
    for klass in Doctor.__mro__:
        if "ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["ContactNo"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_DoctorID():
    assert hasattr(Doctor, "DoctorID")
    descriptor = None
    for klass in Doctor.__mro__:
        if "DoctorID" in klass.__dict__:
            descriptor = klass.__dict__["DoctorID"]
            break
    assert isinstance(descriptor, property)

def test_doctor_has_Name():
    assert hasattr(Doctor, "Name")
    descriptor = None
    for klass in Doctor.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_shopping_cart_is_not_abstract():
    assert not inspect.isabstract(Shopping_Cart)


def test_shopping_cart_constructor_exists():
    assert callable(Shopping_Cart.__init__)


def test_shopping_cart_constructor_args():
    sig = inspect.signature(Shopping_Cart.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "CartID" in params, "Missing parameter 'CartID'"
    assert "OrderID" in params, "Missing parameter 'OrderID'"

def test_shopping_cart_has_Quantity():
    assert hasattr(Shopping_Cart, "Quantity")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_CartID():
    assert hasattr(Shopping_Cart, "CartID")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "CartID" in klass.__dict__:
            descriptor = klass.__dict__["CartID"]
            break
    assert isinstance(descriptor, property)

def test_shopping_cart_has_OrderID():
    assert hasattr(Shopping_Cart, "OrderID")
    descriptor = None
    for klass in Shopping_Cart.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "Method" in params, "Missing parameter 'Method'"
    assert "PaymentID" in params, "Missing parameter 'PaymentID'"

def test_payment_has_OrderID():
    assert hasattr(Payment, "OrderID")
    descriptor = None
    for klass in Payment.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Method():
    assert hasattr(Payment, "Method")
    descriptor = None
    for klass in Payment.__mro__:
        if "Method" in klass.__dict__:
            descriptor = klass.__dict__["Method"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_PaymentID():
    assert hasattr(Payment, "PaymentID")
    descriptor = None
    for klass in Payment.__mro__:
        if "PaymentID" in klass.__dict__:
            descriptor = klass.__dict__["PaymentID"]
            break
    assert isinstance(descriptor, property)



def test_manager_is_not_abstract():
    assert not inspect.isabstract(Manager)


def test_manager_constructor_exists():
    assert callable(Manager.__init__)


def test_manager_constructor_args():
    sig = inspect.signature(Manager.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ManagerID" in params, "Missing parameter 'ManagerID'"
    assert "ContatctNo" in params, "Missing parameter 'ContatctNo'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_manager_has_Name():
    assert hasattr(Manager, "Name")
    descriptor = None
    for klass in Manager.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_ManagerID():
    assert hasattr(Manager, "ManagerID")
    descriptor = None
    for klass in Manager.__mro__:
        if "ManagerID" in klass.__dict__:
            descriptor = klass.__dict__["ManagerID"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_ContatctNo():
    assert hasattr(Manager, "ContatctNo")
    descriptor = None
    for klass in Manager.__mro__:
        if "ContatctNo" in klass.__dict__:
            descriptor = klass.__dict__["ContatctNo"]
            break
    assert isinstance(descriptor, property)

def test_manager_has_Email():
    assert hasattr(Manager, "Email")
    descriptor = None
    for klass in Manager.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "Department" in params, "Missing parameter 'Department'"
    assert "ContactNo" in params, "Missing parameter 'ContactNo'"
    assert "EmpID" in params, "Missing parameter 'EmpID'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_employee_has_Department():
    assert hasattr(Employee, "Department")
    descriptor = None
    for klass in Employee.__mro__:
        if "Department" in klass.__dict__:
            descriptor = klass.__dict__["Department"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_ContactNo():
    assert hasattr(Employee, "ContactNo")
    descriptor = None
    for klass in Employee.__mro__:
        if "ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["ContactNo"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmpID():
    assert hasattr(Employee, "EmpID")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmpID" in klass.__dict__:
            descriptor = klass.__dict__["EmpID"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_Name():
    assert hasattr(Employee, "Name")
    descriptor = None
    for klass in Employee.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_pets_is_not_abstract():
    assert not inspect.isabstract(Pets)


def test_pets_constructor_exists():
    assert callable(Pets.__init__)


def test_pets_constructor_args():
    sig = inspect.signature(Pets.__init__)
    params = list(sig.parameters.keys())
    assert "PetName" in params, "Missing parameter 'PetName'"
    assert "PetID" in params, "Missing parameter 'PetID'"
    assert "PetType" in params, "Missing parameter 'PetType'"
    assert "Age" in params, "Missing parameter 'Age'"

def test_pets_has_PetName():
    assert hasattr(Pets, "PetName")
    descriptor = None
    for klass in Pets.__mro__:
        if "PetName" in klass.__dict__:
            descriptor = klass.__dict__["PetName"]
            break
    assert isinstance(descriptor, property)

def test_pets_has_PetID():
    assert hasattr(Pets, "PetID")
    descriptor = None
    for klass in Pets.__mro__:
        if "PetID" in klass.__dict__:
            descriptor = klass.__dict__["PetID"]
            break
    assert isinstance(descriptor, property)

def test_pets_has_PetType():
    assert hasattr(Pets, "PetType")
    descriptor = None
    for klass in Pets.__mro__:
        if "PetType" in klass.__dict__:
            descriptor = klass.__dict__["PetType"]
            break
    assert isinstance(descriptor, property)

def test_pets_has_Age():
    assert hasattr(Pets, "Age")
    descriptor = None
    for klass in Pets.__mro__:
        if "Age" in klass.__dict__:
            descriptor = klass.__dict__["Age"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "CusID" in params, "Missing parameter 'CusID'"
    assert "DateCreated" in params, "Missing parameter 'DateCreated'"

def test_order_has_OrderID():
    assert hasattr(Order, "OrderID")
    descriptor = None
    for klass in Order.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_CusID():
    assert hasattr(Order, "CusID")
    descriptor = None
    for klass in Order.__mro__:
        if "CusID" in klass.__dict__:
            descriptor = klass.__dict__["CusID"]
            break
    assert isinstance(descriptor, property)

def test_order_has_DateCreated():
    assert hasattr(Order, "DateCreated")
    descriptor = None
    for klass in Order.__mro__:
        if "DateCreated" in klass.__dict__:
            descriptor = klass.__dict__["DateCreated"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "adminID" in params, "Missing parameter 'adminID'"

def test_administrator_has_Name():
    assert hasattr(Administrator, "Name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_adminID():
    assert hasattr(Administrator, "adminID")
    descriptor = None
    for klass in Administrator.__mro__:
        if "adminID" in klass.__dict__:
            descriptor = klass.__dict__["adminID"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "UserID" in params, "Missing parameter 'UserID'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_user_has_UserID():
    assert hasattr(User, "UserID")
    descriptor = None
    for klass in User.__mro__:
        if "UserID" in klass.__dict__:
            descriptor = klass.__dict__["UserID"]
            break
    assert isinstance(descriptor, property)

def test_user_has_Password():
    assert hasattr(User, "Password")
    descriptor = None
    for klass in User.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "ContactNo" in params, "Missing parameter 'ContactNo'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "CusID" in params, "Missing parameter 'CusID'"

def test_customer_has_ContactNo():
    assert hasattr(Customer, "ContactNo")
    descriptor = None
    for klass in Customer.__mro__:
        if "ContactNo" in klass.__dict__:
            descriptor = klass.__dict__["ContactNo"]
            break
    assert isinstance(descriptor, property)

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

def test_customer_has_Email():
    assert hasattr(Customer, "Email")
    descriptor = None
    for klass in Customer.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_CusID():
    assert hasattr(Customer, "CusID")
    descriptor = None
    for klass in Customer.__mro__:
        if "CusID" in klass.__dict__:
            descriptor = klass.__dict__["CusID"]
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
Doctor_strategy = st.builds(
    Doctor,
    Email=
        safe_text,
    ContactNo=
        safe_text,
    DoctorID=
        st.integers(),
    Name=
        safe_text
)
Shopping_Cart_strategy = st.builds(
    Shopping_Cart,
    Quantity=
        st.integers(),
    CartID=
        st.integers(),
    OrderID=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    OrderID=
        st.integers(),
    Method=
        safe_text,
    PaymentID=
        st.integers()
)
Manager_strategy = st.builds(
    Manager,
    Name=
        safe_text,
    ManagerID=
        st.integers(),
    ContatctNo=
        safe_text,
    Email=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    Department=
        safe_text,
    ContactNo=
        safe_text,
    EmpID=
        st.integers(),
    Name=
        safe_text
)
Pets_strategy = st.builds(
    Pets,
    PetName=
        safe_text,
    PetID=
        st.integers(),
    PetType=
        safe_text,
    Age=
        st.integers()
)
Order_strategy = st.builds(
    Order,
    OrderID=
        st.integers(),
    CusID=
        st.integers(),
    DateCreated=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    Name=
        safe_text,
    adminID=
        safe_text
)
User_strategy = st.builds(
    User,
    UserID=
        safe_text,
    Password=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    ContactNo=
        safe_text,
    Address=
        safe_text,
    Name=
        safe_text,
    Email=
        safe_text,
    CusID=
        st.integers()
)

@given(instance=Doctor_strategy)
@settings(max_examples=50)
def test_doctor_instantiation(instance):
    assert isinstance(instance, Doctor)



@given(instance=Doctor_strategy)
def test_doctor_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Doctor_strategy)
def test_doctor_ContactNo_setter(instance):
    original = instance.ContactNo
    instance.ContactNo = original
    assert instance.ContactNo == original



@given(instance=Doctor_strategy)
def test_doctor_DoctorID_setter(instance):
    original = instance.DoctorID
    instance.DoctorID = original
    assert instance.DoctorID == original



@given(instance=Doctor_strategy)
def test_doctor_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Shopping_Cart_strategy)
@settings(max_examples=50)
def test_shopping_cart_instantiation(instance):
    assert isinstance(instance, Shopping_Cart)



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_CartID_setter(instance):
    original = instance.CartID
    instance.CartID = original
    assert instance.CartID == original



@given(instance=Shopping_Cart_strategy)
def test_shopping_cart_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Payment_strategy)
def test_payment_Method_setter(instance):
    original = instance.Method
    instance.Method = original
    assert instance.Method == original



@given(instance=Payment_strategy)
def test_payment_PaymentID_setter(instance):
    original = instance.PaymentID
    instance.PaymentID = original
    assert instance.PaymentID == original

@given(instance=Manager_strategy)
@settings(max_examples=50)
def test_manager_instantiation(instance):
    assert isinstance(instance, Manager)



@given(instance=Manager_strategy)
def test_manager_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Manager_strategy)
def test_manager_ManagerID_setter(instance):
    original = instance.ManagerID
    instance.ManagerID = original
    assert instance.ManagerID == original



@given(instance=Manager_strategy)
def test_manager_ContatctNo_setter(instance):
    original = instance.ContatctNo
    instance.ContatctNo = original
    assert instance.ContatctNo == original



@given(instance=Manager_strategy)
def test_manager_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_Department_setter(instance):
    original = instance.Department
    instance.Department = original
    assert instance.Department == original



@given(instance=Employee_strategy)
def test_employee_ContactNo_setter(instance):
    original = instance.ContactNo
    instance.ContactNo = original
    assert instance.ContactNo == original



@given(instance=Employee_strategy)
def test_employee_EmpID_setter(instance):
    original = instance.EmpID
    instance.EmpID = original
    assert instance.EmpID == original



@given(instance=Employee_strategy)
def test_employee_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Pets_strategy)
@settings(max_examples=50)
def test_pets_instantiation(instance):
    assert isinstance(instance, Pets)



@given(instance=Pets_strategy)
def test_pets_PetName_setter(instance):
    original = instance.PetName
    instance.PetName = original
    assert instance.PetName == original



@given(instance=Pets_strategy)
def test_pets_PetID_setter(instance):
    original = instance.PetID
    instance.PetID = original
    assert instance.PetID == original



@given(instance=Pets_strategy)
def test_pets_PetType_setter(instance):
    original = instance.PetType
    instance.PetType = original
    assert instance.PetType == original



@given(instance=Pets_strategy)
def test_pets_Age_setter(instance):
    original = instance.Age
    instance.Age = original
    assert instance.Age == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Order_strategy)
def test_order_CusID_setter(instance):
    original = instance.CusID
    instance.CusID = original
    assert instance.CusID == original



@given(instance=Order_strategy)
def test_order_DateCreated_setter(instance):
    original = instance.DateCreated
    instance.DateCreated = original
    assert instance.DateCreated == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Administrator_strategy)
def test_administrator_adminID_setter(instance):
    original = instance.adminID
    instance.adminID = original
    assert instance.adminID == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_UserID_setter(instance):
    original = instance.UserID
    instance.UserID = original
    assert instance.UserID == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_ContactNo_setter(instance):
    original = instance.ContactNo
    instance.ContactNo = original
    assert instance.ContactNo == original



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
def test_customer_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Customer_strategy)
def test_customer_CusID_setter(instance):
    original = instance.CusID
    instance.CusID = original
    assert instance.CusID == original
