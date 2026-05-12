import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Guest,
    Employee,
    OrderDetails,
    Meals,
    Payment,
    Admin,
    Transport,
    User,
    Orders,
    Cart,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())
    assert "guestID" in params, "Missing parameter 'guestID'"

def test_guest_has_guestID():
    assert hasattr(Guest, "guestID")
    descriptor = None
    for klass in Guest.__mro__:
        if "guestID" in klass.__dict__:
            descriptor = klass.__dict__["guestID"]
            break
    assert isinstance(descriptor, property)



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "EmpPassword" in params, "Missing parameter 'EmpPassword'"
    assert "EmployeeID" in params, "Missing parameter 'EmployeeID'"
    assert "EmpName" in params, "Missing parameter 'EmpName'"

def test_employee_has_EmpPassword():
    assert hasattr(Employee, "EmpPassword")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmpPassword" in klass.__dict__:
            descriptor = klass.__dict__["EmpPassword"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmployeeID():
    assert hasattr(Employee, "EmployeeID")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmployeeID" in klass.__dict__:
            descriptor = klass.__dict__["EmployeeID"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_EmpName():
    assert hasattr(Employee, "EmpName")
    descriptor = None
    for klass in Employee.__mro__:
        if "EmpName" in klass.__dict__:
            descriptor = klass.__dict__["EmpName"]
            break
    assert isinstance(descriptor, property)



def test_orderdetails_is_not_abstract():
    assert not inspect.isabstract(OrderDetails)


def test_orderdetails_constructor_exists():
    assert callable(OrderDetails.__init__)


def test_orderdetails_constructor_args():
    sig = inspect.signature(OrderDetails.__init__)
    params = list(sig.parameters.keys())
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "totPrice" in params, "Missing parameter 'totPrice'"
    assert "orderTime" in params, "Missing parameter 'orderTime'"
    assert "MealID" in params, "Missing parameter 'MealID'"
    assert "status" in params, "Missing parameter 'status'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_orderdetails_has_OrderID():
    assert hasattr(OrderDetails, "OrderID")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_totPrice():
    assert hasattr(OrderDetails, "totPrice")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "totPrice" in klass.__dict__:
            descriptor = klass.__dict__["totPrice"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_orderTime():
    assert hasattr(OrderDetails, "orderTime")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "orderTime" in klass.__dict__:
            descriptor = klass.__dict__["orderTime"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_MealID():
    assert hasattr(OrderDetails, "MealID")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "MealID" in klass.__dict__:
            descriptor = klass.__dict__["MealID"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_status():
    assert hasattr(OrderDetails, "status")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_orderdetails_has_quantity():
    assert hasattr(OrderDetails, "quantity")
    descriptor = None
    for klass in OrderDetails.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_meals_is_not_abstract():
    assert not inspect.isabstract(Meals)


def test_meals_constructor_exists():
    assert callable(Meals.__init__)


def test_meals_constructor_args():
    sig = inspect.signature(Meals.__init__)
    params = list(sig.parameters.keys())
    assert "MealID" in params, "Missing parameter 'MealID'"
    assert "Portion" in params, "Missing parameter 'Portion'"
    assert "supplier" in params, "Missing parameter 'supplier'"
    assert "MealType" in params, "Missing parameter 'MealType'"
    assert "MealName" in params, "Missing parameter 'MealName'"
    assert "unitPrice" in params, "Missing parameter 'unitPrice'"

def test_meals_has_MealID():
    assert hasattr(Meals, "MealID")
    descriptor = None
    for klass in Meals.__mro__:
        if "MealID" in klass.__dict__:
            descriptor = klass.__dict__["MealID"]
            break
    assert isinstance(descriptor, property)

def test_meals_has_Portion():
    assert hasattr(Meals, "Portion")
    descriptor = None
    for klass in Meals.__mro__:
        if "Portion" in klass.__dict__:
            descriptor = klass.__dict__["Portion"]
            break
    assert isinstance(descriptor, property)

def test_meals_has_supplier():
    assert hasattr(Meals, "supplier")
    descriptor = None
    for klass in Meals.__mro__:
        if "supplier" in klass.__dict__:
            descriptor = klass.__dict__["supplier"]
            break
    assert isinstance(descriptor, property)

def test_meals_has_MealType():
    assert hasattr(Meals, "MealType")
    descriptor = None
    for klass in Meals.__mro__:
        if "MealType" in klass.__dict__:
            descriptor = klass.__dict__["MealType"]
            break
    assert isinstance(descriptor, property)

def test_meals_has_MealName():
    assert hasattr(Meals, "MealName")
    descriptor = None
    for klass in Meals.__mro__:
        if "MealName" in klass.__dict__:
            descriptor = klass.__dict__["MealName"]
            break
    assert isinstance(descriptor, property)

def test_meals_has_unitPrice():
    assert hasattr(Meals, "unitPrice")
    descriptor = None
    for klass in Meals.__mro__:
        if "unitPrice" in klass.__dict__:
            descriptor = klass.__dict__["unitPrice"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "PaymentType" in params, "Missing parameter 'PaymentType'"
    assert "paymentID" in params, "Missing parameter 'paymentID'"
    assert "paymentDate" in params, "Missing parameter 'paymentDate'"
    assert "PaymentStatus" in params, "Missing parameter 'PaymentStatus'"
    assert "paymentAmount" in params, "Missing parameter 'paymentAmount'"

def test_payment_has_PaymentType():
    assert hasattr(Payment, "PaymentType")
    descriptor = None
    for klass in Payment.__mro__:
        if "PaymentType" in klass.__dict__:
            descriptor = klass.__dict__["PaymentType"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_paymentID():
    assert hasattr(Payment, "paymentID")
    descriptor = None
    for klass in Payment.__mro__:
        if "paymentID" in klass.__dict__:
            descriptor = klass.__dict__["paymentID"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_paymentDate():
    assert hasattr(Payment, "paymentDate")
    descriptor = None
    for klass in Payment.__mro__:
        if "paymentDate" in klass.__dict__:
            descriptor = klass.__dict__["paymentDate"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_PaymentStatus():
    assert hasattr(Payment, "PaymentStatus")
    descriptor = None
    for klass in Payment.__mro__:
        if "PaymentStatus" in klass.__dict__:
            descriptor = klass.__dict__["PaymentStatus"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_paymentAmount():
    assert hasattr(Payment, "paymentAmount")
    descriptor = None
    for klass in Payment.__mro__:
        if "paymentAmount" in klass.__dict__:
            descriptor = klass.__dict__["paymentAmount"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_transport_is_not_abstract():
    assert not inspect.isabstract(Transport)


def test_transport_constructor_exists():
    assert callable(Transport.__init__)


def test_transport_constructor_args():
    sig = inspect.signature(Transport.__init__)
    params = list(sig.parameters.keys())
    assert "transportCost" in params, "Missing parameter 'transportCost'"
    assert "location" in params, "Missing parameter 'location'"
    assert "TransportID" in params, "Missing parameter 'TransportID'"

def test_transport_has_transportCost():
    assert hasattr(Transport, "transportCost")
    descriptor = None
    for klass in Transport.__mro__:
        if "transportCost" in klass.__dict__:
            descriptor = klass.__dict__["transportCost"]
            break
    assert isinstance(descriptor, property)

def test_transport_has_location():
    assert hasattr(Transport, "location")
    descriptor = None
    for klass in Transport.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_transport_has_TransportID():
    assert hasattr(Transport, "TransportID")
    descriptor = None
    for klass in Transport.__mro__:
        if "TransportID" in klass.__dict__:
            descriptor = klass.__dict__["TransportID"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "userID" in params, "Missing parameter 'userID'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"

def test_user_has_userID():
    assert hasattr(User, "userID")
    descriptor = None
    for klass in User.__mro__:
        if "userID" in klass.__dict__:
            descriptor = klass.__dict__["userID"]
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

def test_user_has_loginStatus():
    assert hasattr(User, "loginStatus")
    descriptor = None
    for klass in User.__mro__:
        if "loginStatus" in klass.__dict__:
            descriptor = klass.__dict__["loginStatus"]
            break
    assert isinstance(descriptor, property)



def test_orders_is_not_abstract():
    assert not inspect.isabstract(Orders)


def test_orders_constructor_exists():
    assert callable(Orders.__init__)


def test_orders_constructor_args():
    sig = inspect.signature(Orders.__init__)
    params = list(sig.parameters.keys())
    assert "OrderID" in params, "Missing parameter 'OrderID'"
    assert "status" in params, "Missing parameter 'status'"
    assert "dateFinished" in params, "Missing parameter 'dateFinished'"
    assert "dateOrdered" in params, "Missing parameter 'dateOrdered'"

def test_orders_has_OrderID():
    assert hasattr(Orders, "OrderID")
    descriptor = None
    for klass in Orders.__mro__:
        if "OrderID" in klass.__dict__:
            descriptor = klass.__dict__["OrderID"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_status():
    assert hasattr(Orders, "status")
    descriptor = None
    for klass in Orders.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_dateFinished():
    assert hasattr(Orders, "dateFinished")
    descriptor = None
    for klass in Orders.__mro__:
        if "dateFinished" in klass.__dict__:
            descriptor = klass.__dict__["dateFinished"]
            break
    assert isinstance(descriptor, property)

def test_orders_has_dateOrdered():
    assert hasattr(Orders, "dateOrdered")
    descriptor = None
    for klass in Orders.__mro__:
        if "dateOrdered" in klass.__dict__:
            descriptor = klass.__dict__["dateOrdered"]
            break
    assert isinstance(descriptor, property)



def test_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())
    assert "Quantity" in params, "Missing parameter 'Quantity'"
    assert "cartID" in params, "Missing parameter 'cartID'"
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "date" in params, "Missing parameter 'date'"

def test_cart_has_Quantity():
    assert hasattr(Cart, "Quantity")
    descriptor = None
    for klass in Cart.__mro__:
        if "Quantity" in klass.__dict__:
            descriptor = klass.__dict__["Quantity"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_cartID():
    assert hasattr(Cart, "cartID")
    descriptor = None
    for klass in Cart.__mro__:
        if "cartID" in klass.__dict__:
            descriptor = klass.__dict__["cartID"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_ProductID():
    assert hasattr(Cart, "ProductID")
    descriptor = None
    for klass in Cart.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_date():
    assert hasattr(Cart, "date")
    descriptor = None
    for klass in Cart.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "CutsomerAddress" in params, "Missing parameter 'CutsomerAddress'"
    assert "PhoneNumber" in params, "Missing parameter 'PhoneNumber'"
    assert "CustomerName" in params, "Missing parameter 'CustomerName'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_customer_has_CutsomerAddress():
    assert hasattr(Customer, "CutsomerAddress")
    descriptor = None
    for klass in Customer.__mro__:
        if "CutsomerAddress" in klass.__dict__:
            descriptor = klass.__dict__["CutsomerAddress"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_PhoneNumber():
    assert hasattr(Customer, "PhoneNumber")
    descriptor = None
    for klass in Customer.__mro__:
        if "PhoneNumber" in klass.__dict__:
            descriptor = klass.__dict__["PhoneNumber"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_CustomerName():
    assert hasattr(Customer, "CustomerName")
    descriptor = None
    for klass in Customer.__mro__:
        if "CustomerName" in klass.__dict__:
            descriptor = klass.__dict__["CustomerName"]
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
Guest_strategy = st.builds(
    Guest,
    guestID=
        safe_text
)
Employee_strategy = st.builds(
    Employee,
    EmpPassword=
        safe_text,
    EmployeeID=
        safe_text,
    EmpName=
        safe_text
)
OrderDetails_strategy = st.builds(
    OrderDetails,
    OrderID=
        st.integers(),
    totPrice=
        safe_text,
    orderTime=
        safe_text,
    MealID=
        safe_text,
    status=
        safe_text,
    quantity=
        st.integers()
)
Meals_strategy = st.builds(
    Meals,
    MealID=
        safe_text,
    Portion=
        safe_text,
    supplier=
        safe_text,
    MealType=
        safe_text,
    MealName=
        safe_text,
    unitPrice=
        safe_text
)
Payment_strategy = st.builds(
    Payment,
    PaymentType=
        safe_text,
    paymentID=
        safe_text,
    paymentDate=
        safe_text,
    PaymentStatus=
        safe_text,
    paymentAmount=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
)
Transport_strategy = st.builds(
    Transport,
    transportCost=
        safe_text,
    location=
        safe_text,
    TransportID=
        st.integers()
)
User_strategy = st.builds(
    User,
    userID=
        safe_text,
    Password=
        safe_text,
    loginStatus=
        safe_text
)
Orders_strategy = st.builds(
    Orders,
    OrderID=
        st.integers(),
    status=
        safe_text,
    dateFinished=
        safe_text,
    dateOrdered=
        safe_text
)
Cart_strategy = st.builds(
    Cart,
    Quantity=
        st.integers(),
    cartID=
        st.integers(),
    ProductID=
        safe_text,
    date=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    CutsomerAddress=
        safe_text,
    PhoneNumber=
        st.integers(),
    CustomerName=
        safe_text,
    Email=
        safe_text
)

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)



@given(instance=Guest_strategy)
def test_guest_guestID_setter(instance):
    original = instance.guestID
    instance.guestID = original
    assert instance.guestID == original

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_EmpPassword_setter(instance):
    original = instance.EmpPassword
    instance.EmpPassword = original
    assert instance.EmpPassword == original



@given(instance=Employee_strategy)
def test_employee_EmployeeID_setter(instance):
    original = instance.EmployeeID
    instance.EmployeeID = original
    assert instance.EmployeeID == original



@given(instance=Employee_strategy)
def test_employee_EmpName_setter(instance):
    original = instance.EmpName
    instance.EmpName = original
    assert instance.EmpName == original

@given(instance=OrderDetails_strategy)
@settings(max_examples=50)
def test_orderdetails_instantiation(instance):
    assert isinstance(instance, OrderDetails)



@given(instance=OrderDetails_strategy)
def test_orderdetails_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_totPrice_setter(instance):
    original = instance.totPrice
    instance.totPrice = original
    assert instance.totPrice == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_orderTime_setter(instance):
    original = instance.orderTime
    instance.orderTime = original
    assert instance.orderTime == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_MealID_setter(instance):
    original = instance.MealID
    instance.MealID = original
    assert instance.MealID == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=OrderDetails_strategy)
def test_orderdetails_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=Meals_strategy)
@settings(max_examples=50)
def test_meals_instantiation(instance):
    assert isinstance(instance, Meals)



@given(instance=Meals_strategy)
def test_meals_MealID_setter(instance):
    original = instance.MealID
    instance.MealID = original
    assert instance.MealID == original



@given(instance=Meals_strategy)
def test_meals_Portion_setter(instance):
    original = instance.Portion
    instance.Portion = original
    assert instance.Portion == original



@given(instance=Meals_strategy)
def test_meals_supplier_setter(instance):
    original = instance.supplier
    instance.supplier = original
    assert instance.supplier == original



@given(instance=Meals_strategy)
def test_meals_MealType_setter(instance):
    original = instance.MealType
    instance.MealType = original
    assert instance.MealType == original



@given(instance=Meals_strategy)
def test_meals_MealName_setter(instance):
    original = instance.MealName
    instance.MealName = original
    assert instance.MealName == original



@given(instance=Meals_strategy)
def test_meals_unitPrice_setter(instance):
    original = instance.unitPrice
    instance.unitPrice = original
    assert instance.unitPrice == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_PaymentType_setter(instance):
    original = instance.PaymentType
    instance.PaymentType = original
    assert instance.PaymentType == original



@given(instance=Payment_strategy)
def test_payment_paymentID_setter(instance):
    original = instance.paymentID
    instance.paymentID = original
    assert instance.paymentID == original



@given(instance=Payment_strategy)
def test_payment_paymentDate_setter(instance):
    original = instance.paymentDate
    instance.paymentDate = original
    assert instance.paymentDate == original



@given(instance=Payment_strategy)
def test_payment_PaymentStatus_setter(instance):
    original = instance.PaymentStatus
    instance.PaymentStatus = original
    assert instance.PaymentStatus == original



@given(instance=Payment_strategy)
def test_payment_paymentAmount_setter(instance):
    original = instance.paymentAmount
    instance.paymentAmount = original
    assert instance.paymentAmount == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=Transport_strategy)
@settings(max_examples=50)
def test_transport_instantiation(instance):
    assert isinstance(instance, Transport)



@given(instance=Transport_strategy)
def test_transport_transportCost_setter(instance):
    original = instance.transportCost
    instance.transportCost = original
    assert instance.transportCost == original



@given(instance=Transport_strategy)
def test_transport_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original



@given(instance=Transport_strategy)
def test_transport_TransportID_setter(instance):
    original = instance.TransportID
    instance.TransportID = original
    assert instance.TransportID == original

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_userID_setter(instance):
    original = instance.userID
    instance.userID = original
    assert instance.userID == original



@given(instance=User_strategy)
def test_user_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=User_strategy)
def test_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original

@given(instance=Orders_strategy)
@settings(max_examples=50)
def test_orders_instantiation(instance):
    assert isinstance(instance, Orders)



@given(instance=Orders_strategy)
def test_orders_OrderID_setter(instance):
    original = instance.OrderID
    instance.OrderID = original
    assert instance.OrderID == original



@given(instance=Orders_strategy)
def test_orders_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Orders_strategy)
def test_orders_dateFinished_setter(instance):
    original = instance.dateFinished
    instance.dateFinished = original
    assert instance.dateFinished == original



@given(instance=Orders_strategy)
def test_orders_dateOrdered_setter(instance):
    original = instance.dateOrdered
    instance.dateOrdered = original
    assert instance.dateOrdered == original

@given(instance=Cart_strategy)
@settings(max_examples=50)
def test_cart_instantiation(instance):
    assert isinstance(instance, Cart)



@given(instance=Cart_strategy)
def test_cart_Quantity_setter(instance):
    original = instance.Quantity
    instance.Quantity = original
    assert instance.Quantity == original



@given(instance=Cart_strategy)
def test_cart_cartID_setter(instance):
    original = instance.cartID
    instance.cartID = original
    assert instance.cartID == original



@given(instance=Cart_strategy)
def test_cart_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Cart_strategy)
def test_cart_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_CutsomerAddress_setter(instance):
    original = instance.CutsomerAddress
    instance.CutsomerAddress = original
    assert instance.CutsomerAddress == original



@given(instance=Customer_strategy)
def test_customer_PhoneNumber_setter(instance):
    original = instance.PhoneNumber
    instance.PhoneNumber = original
    assert instance.PhoneNumber == original



@given(instance=Customer_strategy)
def test_customer_CustomerName_setter(instance):
    original = instance.CustomerName
    instance.CustomerName = original
    assert instance.CustomerName == original



@given(instance=Customer_strategy)
def test_customer_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original
