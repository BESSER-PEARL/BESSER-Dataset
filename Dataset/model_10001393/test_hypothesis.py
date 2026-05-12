import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    PaymentMethod,
    ExerciseMachine,
    MediDevices,
    Cart,
    Medicine,
    Customer,
    Admin,
    Order,
    Product,
    Person,
    Registration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_paymentmethod_is_not_abstract():
    assert not inspect.isabstract(PaymentMethod)


def test_paymentmethod_constructor_exists():
    assert callable(PaymentMethod.__init__)


def test_paymentmethod_constructor_args():
    sig = inspect.signature(PaymentMethod.__init__)
    params = list(sig.parameters.keys())
    assert "online" in params, "Missing parameter 'online'"
    assert "paymentType" in params, "Missing parameter 'paymentType'"
    assert "cashOnDelievery" in params, "Missing parameter 'cashOnDelievery'"

def test_paymentmethod_has_online():
    assert hasattr(PaymentMethod, "online")
    descriptor = None
    for klass in PaymentMethod.__mro__:
        if "online" in klass.__dict__:
            descriptor = klass.__dict__["online"]
            break
    assert isinstance(descriptor, property)

def test_paymentmethod_has_paymentType():
    assert hasattr(PaymentMethod, "paymentType")
    descriptor = None
    for klass in PaymentMethod.__mro__:
        if "paymentType" in klass.__dict__:
            descriptor = klass.__dict__["paymentType"]
            break
    assert isinstance(descriptor, property)

def test_paymentmethod_has_cashOnDelievery():
    assert hasattr(PaymentMethod, "cashOnDelievery")
    descriptor = None
    for klass in PaymentMethod.__mro__:
        if "cashOnDelievery" in klass.__dict__:
            descriptor = klass.__dict__["cashOnDelievery"]
            break
    assert isinstance(descriptor, property)



def test_exercisemachine_is_not_abstract():
    assert not inspect.isabstract(ExerciseMachine)


def test_exercisemachine_constructor_exists():
    assert callable(ExerciseMachine.__init__)


def test_exercisemachine_constructor_args():
    sig = inspect.signature(ExerciseMachine.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_exercisemachine_has_size():
    assert hasattr(ExerciseMachine, "size")
    descriptor = None
    for klass in ExerciseMachine.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_exercisemachine_has_type():
    assert hasattr(ExerciseMachine, "type")
    descriptor = None
    for klass in ExerciseMachine.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_exercisemachine_has_id():
    assert hasattr(ExerciseMachine, "id")
    descriptor = None
    for klass in ExerciseMachine.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_exercisemachine_has_name():
    assert hasattr(ExerciseMachine, "name")
    descriptor = None
    for klass in ExerciseMachine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_medidevices_is_not_abstract():
    assert not inspect.isabstract(MediDevices)


def test_medidevices_constructor_exists():
    assert callable(MediDevices.__init__)


def test_medidevices_constructor_args():
    sig = inspect.signature(MediDevices.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"

def test_medidevices_has_type():
    assert hasattr(MediDevices, "type")
    descriptor = None
    for klass in MediDevices.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_medidevices_has_id():
    assert hasattr(MediDevices, "id")
    descriptor = None
    for klass in MediDevices.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_medidevices_has_name():
    assert hasattr(MediDevices, "name")
    descriptor = None
    for klass in MediDevices.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_cart_is_not_abstract():
    assert not inspect.isabstract(Cart)


def test_cart_constructor_exists():
    assert callable(Cart.__init__)


def test_cart_constructor_args():
    sig = inspect.signature(Cart.__init__)
    params = list(sig.parameters.keys())
    assert "TotalBill" in params, "Missing parameter 'TotalBill'"
    assert "id" in params, "Missing parameter 'id'"

def test_cart_has_TotalBill():
    assert hasattr(Cart, "TotalBill")
    descriptor = None
    for klass in Cart.__mro__:
        if "TotalBill" in klass.__dict__:
            descriptor = klass.__dict__["TotalBill"]
            break
    assert isinstance(descriptor, property)

def test_cart_has_id():
    assert hasattr(Cart, "id")
    descriptor = None
    for klass in Cart.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_medicine_is_not_abstract():
    assert not inspect.isabstract(Medicine)


def test_medicine_constructor_exists():
    assert callable(Medicine.__init__)


def test_medicine_constructor_args():
    sig = inspect.signature(Medicine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "formula" in params, "Missing parameter 'formula'"
    assert "potency" in params, "Missing parameter 'potency'"

def test_medicine_has_name():
    assert hasattr(Medicine, "name")
    descriptor = None
    for klass in Medicine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_id():
    assert hasattr(Medicine, "id")
    descriptor = None
    for klass in Medicine.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_formula():
    assert hasattr(Medicine, "formula")
    descriptor = None
    for klass in Medicine.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)

def test_medicine_has_potency():
    assert hasattr(Medicine, "potency")
    descriptor = None
    for klass in Medicine.__mro__:
        if "potency" in klass.__dict__:
            descriptor = klass.__dict__["potency"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"

def test_customer_has_userName():
    assert hasattr(Customer, "userName")
    descriptor = None
    for klass in Customer.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_id():
    assert hasattr(Customer, "id")
    descriptor = None
    for klass in Customer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_password():
    assert hasattr(Customer, "password")
    descriptor = None
    for klass in Customer.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "id" in params, "Missing parameter 'id'"
    assert "password" in params, "Missing parameter 'password'"

def test_admin_has_userName():
    assert hasattr(Admin, "userName")
    descriptor = None
    for klass in Admin.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_id():
    assert hasattr(Admin, "id")
    descriptor = None
    for klass in Admin.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "orderStatus" in params, "Missing parameter 'orderStatus'"
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "orderDate" in params, "Missing parameter 'orderDate'"

def test_order_has_id():
    assert hasattr(Order, "id")
    descriptor = None
    for klass in Order.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderStatus():
    assert hasattr(Order, "orderStatus")
    descriptor = None
    for klass in Order.__mro__:
        if "orderStatus" in klass.__dict__:
            descriptor = klass.__dict__["orderStatus"]
            break
    assert isinstance(descriptor, property)

def test_order_has_quantity():
    assert hasattr(Order, "quantity")
    descriptor = None
    for klass in Order.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_order_has_orderDate():
    assert hasattr(Order, "orderDate")
    descriptor = None
    for klass in Order.__mro__:
        if "orderDate" in klass.__dict__:
            descriptor = klass.__dict__["orderDate"]
            break
    assert isinstance(descriptor, property)



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "pID" in params, "Missing parameter 'pID'"
    assert "manufecturedDate" in params, "Missing parameter 'manufecturedDate'"
    assert "name" in params, "Missing parameter 'name'"
    assert "manufecturer" in params, "Missing parameter 'manufecturer'"
    assert "price" in params, "Missing parameter 'price'"
    assert "color" in params, "Missing parameter 'color'"
    assert "expiry" in params, "Missing parameter 'expiry'"

def test_product_has_pID():
    assert hasattr(Product, "pID")
    descriptor = None
    for klass in Product.__mro__:
        if "pID" in klass.__dict__:
            descriptor = klass.__dict__["pID"]
            break
    assert isinstance(descriptor, property)

def test_product_has_manufecturedDate():
    assert hasattr(Product, "manufecturedDate")
    descriptor = None
    for klass in Product.__mro__:
        if "manufecturedDate" in klass.__dict__:
            descriptor = klass.__dict__["manufecturedDate"]
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

def test_product_has_manufecturer():
    assert hasattr(Product, "manufecturer")
    descriptor = None
    for klass in Product.__mro__:
        if "manufecturer" in klass.__dict__:
            descriptor = klass.__dict__["manufecturer"]
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

def test_product_has_color():
    assert hasattr(Product, "color")
    descriptor = None
    for klass in Product.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_product_has_expiry():
    assert hasattr(Product, "expiry")
    descriptor = None
    for klass in Product.__mro__:
        if "expiry" in klass.__dict__:
            descriptor = klass.__dict__["expiry"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "Email" in params, "Missing parameter 'Email'"
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "LastName" in params, "Missing parameter 'LastName'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Address" in params, "Missing parameter 'Address'"

def test_person_has_Email():
    assert hasattr(Person, "Email")
    descriptor = None
    for klass in Person.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_person_has_DOB():
    assert hasattr(Person, "DOB")
    descriptor = None
    for klass in Person.__mro__:
        if "DOB" in klass.__dict__:
            descriptor = klass.__dict__["DOB"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Phone():
    assert hasattr(Person, "Phone")
    descriptor = None
    for klass in Person.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
            break
    assert isinstance(descriptor, property)

def test_person_has_LastName():
    assert hasattr(Person, "LastName")
    descriptor = None
    for klass in Person.__mro__:
        if "LastName" in klass.__dict__:
            descriptor = klass.__dict__["LastName"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Name():
    assert hasattr(Person, "Name")
    descriptor = None
    for klass in Person.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_person_has_Address():
    assert hasattr(Person, "Address")
    descriptor = None
    for klass in Person.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)



def test_registration_is_not_abstract():
    assert not inspect.isabstract(Registration)


def test_registration_constructor_exists():
    assert callable(Registration.__init__)


def test_registration_constructor_args():
    sig = inspect.signature(Registration.__init__)
    params = list(sig.parameters.keys())
    assert "Phone" in params, "Missing parameter 'Phone'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "UserName" in params, "Missing parameter 'UserName'"
    assert "DOB" in params, "Missing parameter 'DOB'"
    assert "name" in params, "Missing parameter 'name'"
    assert "Address" in params, "Missing parameter 'Address'"
    assert "LastName" in params, "Missing parameter 'LastName'"

def test_registration_has_Phone():
    assert hasattr(Registration, "Phone")
    descriptor = None
    for klass in Registration.__mro__:
        if "Phone" in klass.__dict__:
            descriptor = klass.__dict__["Phone"]
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

def test_registration_has_Email():
    assert hasattr(Registration, "Email")
    descriptor = None
    for klass in Registration.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
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

def test_registration_has_DOB():
    assert hasattr(Registration, "DOB")
    descriptor = None
    for klass in Registration.__mro__:
        if "DOB" in klass.__dict__:
            descriptor = klass.__dict__["DOB"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_name():
    assert hasattr(Registration, "name")
    descriptor = None
    for klass in Registration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_Address():
    assert hasattr(Registration, "Address")
    descriptor = None
    for klass in Registration.__mro__:
        if "Address" in klass.__dict__:
            descriptor = klass.__dict__["Address"]
            break
    assert isinstance(descriptor, property)

def test_registration_has_LastName():
    assert hasattr(Registration, "LastName")
    descriptor = None
    for klass in Registration.__mro__:
        if "LastName" in klass.__dict__:
            descriptor = klass.__dict__["LastName"]
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
PaymentMethod_strategy = st.builds(
    PaymentMethod,
    online=
        safe_text,
    paymentType=
        safe_text,
    cashOnDelievery=
        safe_text
)
ExerciseMachine_strategy = st.builds(
    ExerciseMachine,
    size=
        st.integers(),
    type=
        safe_text,
    id=
        st.integers(),
    name=
        safe_text
)
MediDevices_strategy = st.builds(
    MediDevices,
    type=
        safe_text,
    id=
        safe_text,
    name=
        safe_text
)
Cart_strategy = st.builds(
    Cart,
    TotalBill=
        st.integers(),
    id=
        st.integers()
)
Medicine_strategy = st.builds(
    Medicine,
    name=
        safe_text,
    id=
        st.integers(),
    formula=
        safe_text,
    potency=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    userName=
        safe_text,
    id=
        st.integers(),
    password=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    userName=
        safe_text,
    id=
        st.integers(),
    password=
        safe_text
)
Order_strategy = st.builds(
    Order,
    id=
        st.integers(),
    orderStatus=
        safe_text,
    quantity=
        st.integers(),
    orderDate=
        safe_text
)
Product_strategy = st.builds(
    Product,
    pID=
        safe_text,
    manufecturedDate=
        safe_text,
    name=
        safe_text,
    manufecturer=
        safe_text,
    price=
        st.integers(),
    color=
        safe_text,
    expiry=
        safe_text
)
Person_strategy = st.builds(
    Person,
    Email=
        safe_text,
    DOB=
        safe_text,
    Phone=
        st.integers(),
    LastName=
        safe_text,
    Name=
        safe_text,
    Address=
        safe_text
)
Registration_strategy = st.builds(
    Registration,
    Phone=
        st.integers(),
    Password=
        safe_text,
    Email=
        safe_text,
    UserName=
        safe_text,
    DOB=
        safe_text,
    name=
        safe_text,
    Address=
        safe_text,
    LastName=
        safe_text
)

@given(instance=PaymentMethod_strategy)
@settings(max_examples=50)
def test_paymentmethod_instantiation(instance):
    assert isinstance(instance, PaymentMethod)



@given(instance=PaymentMethod_strategy)
def test_paymentmethod_online_setter(instance):
    original = instance.online
    instance.online = original
    assert instance.online == original



@given(instance=PaymentMethod_strategy)
def test_paymentmethod_paymentType_setter(instance):
    original = instance.paymentType
    instance.paymentType = original
    assert instance.paymentType == original



@given(instance=PaymentMethod_strategy)
def test_paymentmethod_cashOnDelievery_setter(instance):
    original = instance.cashOnDelievery
    instance.cashOnDelievery = original
    assert instance.cashOnDelievery == original

@given(instance=ExerciseMachine_strategy)
@settings(max_examples=50)
def test_exercisemachine_instantiation(instance):
    assert isinstance(instance, ExerciseMachine)



@given(instance=ExerciseMachine_strategy)
def test_exercisemachine_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=ExerciseMachine_strategy)
def test_exercisemachine_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=ExerciseMachine_strategy)
def test_exercisemachine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=ExerciseMachine_strategy)
def test_exercisemachine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=MediDevices_strategy)
@settings(max_examples=50)
def test_medidevices_instantiation(instance):
    assert isinstance(instance, MediDevices)



@given(instance=MediDevices_strategy)
def test_medidevices_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=MediDevices_strategy)
def test_medidevices_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=MediDevices_strategy)
def test_medidevices_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Cart_strategy)
@settings(max_examples=50)
def test_cart_instantiation(instance):
    assert isinstance(instance, Cart)



@given(instance=Cart_strategy)
def test_cart_TotalBill_setter(instance):
    original = instance.TotalBill
    instance.TotalBill = original
    assert instance.TotalBill == original



@given(instance=Cart_strategy)
def test_cart_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Medicine_strategy)
@settings(max_examples=50)
def test_medicine_instantiation(instance):
    assert isinstance(instance, Medicine)



@given(instance=Medicine_strategy)
def test_medicine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Medicine_strategy)
def test_medicine_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Medicine_strategy)
def test_medicine_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original



@given(instance=Medicine_strategy)
def test_medicine_potency_setter(instance):
    original = instance.potency
    instance.potency = original
    assert instance.potency == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Customer_strategy)
def test_customer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Customer_strategy)
def test_customer_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=Admin_strategy)
def test_admin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Order_strategy)
def test_order_orderStatus_setter(instance):
    original = instance.orderStatus
    instance.orderStatus = original
    assert instance.orderStatus == original



@given(instance=Order_strategy)
def test_order_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=Order_strategy)
def test_order_orderDate_setter(instance):
    original = instance.orderDate
    instance.orderDate = original
    assert instance.orderDate == original

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_pID_setter(instance):
    original = instance.pID
    instance.pID = original
    assert instance.pID == original



@given(instance=Product_strategy)
def test_product_manufecturedDate_setter(instance):
    original = instance.manufecturedDate
    instance.manufecturedDate = original
    assert instance.manufecturedDate == original



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Product_strategy)
def test_product_manufecturer_setter(instance):
    original = instance.manufecturer
    instance.manufecturer = original
    assert instance.manufecturer == original



@given(instance=Product_strategy)
def test_product_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original



@given(instance=Product_strategy)
def test_product_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=Product_strategy)
def test_product_expiry_setter(instance):
    original = instance.expiry
    instance.expiry = original
    assert instance.expiry == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Person_strategy)
def test_person_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=Person_strategy)
def test_person_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Person_strategy)
def test_person_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original



@given(instance=Person_strategy)
def test_person_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Person_strategy)
def test_person_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original

@given(instance=Registration_strategy)
@settings(max_examples=50)
def test_registration_instantiation(instance):
    assert isinstance(instance, Registration)



@given(instance=Registration_strategy)
def test_registration_Phone_setter(instance):
    original = instance.Phone
    instance.Phone = original
    assert instance.Phone == original



@given(instance=Registration_strategy)
def test_registration_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Registration_strategy)
def test_registration_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Registration_strategy)
def test_registration_UserName_setter(instance):
    original = instance.UserName
    instance.UserName = original
    assert instance.UserName == original



@given(instance=Registration_strategy)
def test_registration_DOB_setter(instance):
    original = instance.DOB
    instance.DOB = original
    assert instance.DOB == original



@given(instance=Registration_strategy)
def test_registration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Registration_strategy)
def test_registration_Address_setter(instance):
    original = instance.Address
    instance.Address = original
    assert instance.Address == original



@given(instance=Registration_strategy)
def test_registration_LastName_setter(instance):
    original = instance.LastName
    instance.LastName = original
    assert instance.LastName == original
