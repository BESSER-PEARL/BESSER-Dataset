import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    OrderCustomer,
    Address,
    CustomerProduct,
    OrderProduct,
    Order,
    Payment,
    Guest,
    Products,
    Customer1,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ordercustomer_is_not_abstract():
    assert not inspect.isabstract(OrderCustomer)


def test_ordercustomer_constructor_exists():
    assert callable(OrderCustomer.__init__)


def test_ordercustomer_constructor_args():
    sig = inspect.signature(OrderCustomer.__init__)
    params = list(sig.parameters.keys())
    assert "Order" in params, "Missing parameter 'Order'"
    assert "id" in params, "Missing parameter 'id'"
    assert "Customer" in params, "Missing parameter 'Customer'"

def test_ordercustomer_has_Order():
    assert hasattr(OrderCustomer, "Order")
    descriptor = None
    for klass in OrderCustomer.__mro__:
        if "Order" in klass.__dict__:
            descriptor = klass.__dict__["Order"]
            break
    assert isinstance(descriptor, property)

def test_ordercustomer_has_id():
    assert hasattr(OrderCustomer, "id")
    descriptor = None
    for klass in OrderCustomer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_ordercustomer_has_Customer():
    assert hasattr(OrderCustomer, "Customer")
    descriptor = None
    for klass in OrderCustomer.__mro__:
        if "Customer" in klass.__dict__:
            descriptor = klass.__dict__["Customer"]
            break
    assert isinstance(descriptor, property)



def test_address_is_not_abstract():
    assert not inspect.isabstract(Address)


def test_address_constructor_exists():
    assert callable(Address.__init__)


def test_address_constructor_args():
    sig = inspect.signature(Address.__init__)
    params = list(sig.parameters.keys())
    assert "Street" in params, "Missing parameter 'Street'"
    assert "City" in params, "Missing parameter 'City'"
    assert "House" in params, "Missing parameter 'House'"

def test_address_has_Street():
    assert hasattr(Address, "Street")
    descriptor = None
    for klass in Address.__mro__:
        if "Street" in klass.__dict__:
            descriptor = klass.__dict__["Street"]
            break
    assert isinstance(descriptor, property)

def test_address_has_City():
    assert hasattr(Address, "City")
    descriptor = None
    for klass in Address.__mro__:
        if "City" in klass.__dict__:
            descriptor = klass.__dict__["City"]
            break
    assert isinstance(descriptor, property)

def test_address_has_House():
    assert hasattr(Address, "House")
    descriptor = None
    for klass in Address.__mro__:
        if "House" in klass.__dict__:
            descriptor = klass.__dict__["House"]
            break
    assert isinstance(descriptor, property)



def test_customerproduct_is_not_abstract():
    assert not inspect.isabstract(CustomerProduct)


def test_customerproduct_constructor_exists():
    assert callable(CustomerProduct.__init__)


def test_customerproduct_constructor_args():
    sig = inspect.signature(CustomerProduct.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Product" in params, "Missing parameter 'Product'"
    assert "Customer" in params, "Missing parameter 'Customer'"

def test_customerproduct_has_ID():
    assert hasattr(CustomerProduct, "ID")
    descriptor = None
    for klass in CustomerProduct.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_customerproduct_has_Product():
    assert hasattr(CustomerProduct, "Product")
    descriptor = None
    for klass in CustomerProduct.__mro__:
        if "Product" in klass.__dict__:
            descriptor = klass.__dict__["Product"]
            break
    assert isinstance(descriptor, property)

def test_customerproduct_has_Customer():
    assert hasattr(CustomerProduct, "Customer")
    descriptor = None
    for klass in CustomerProduct.__mro__:
        if "Customer" in klass.__dict__:
            descriptor = klass.__dict__["Customer"]
            break
    assert isinstance(descriptor, property)



def test_orderproduct_is_not_abstract():
    assert not inspect.isabstract(OrderProduct)


def test_orderproduct_constructor_exists():
    assert callable(OrderProduct.__init__)


def test_orderproduct_constructor_args():
    sig = inspect.signature(OrderProduct.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Oid" in params, "Missing parameter 'Oid'"
    assert "Pid" in params, "Missing parameter 'Pid'"

def test_orderproduct_has_ID():
    assert hasattr(OrderProduct, "ID")
    descriptor = None
    for klass in OrderProduct.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_orderproduct_has_Oid():
    assert hasattr(OrderProduct, "Oid")
    descriptor = None
    for klass in OrderProduct.__mro__:
        if "Oid" in klass.__dict__:
            descriptor = klass.__dict__["Oid"]
            break
    assert isinstance(descriptor, property)

def test_orderproduct_has_Pid():
    assert hasattr(OrderProduct, "Pid")
    descriptor = None
    for klass in OrderProduct.__mro__:
        if "Pid" in klass.__dict__:
            descriptor = klass.__dict__["Pid"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "ProductID" in params, "Missing parameter 'ProductID'"
    assert "Date" in params, "Missing parameter 'Date'"
    assert "id" in params, "Missing parameter 'id'"

def test_order_has_ProductID():
    assert hasattr(Order, "ProductID")
    descriptor = None
    for klass in Order.__mro__:
        if "ProductID" in klass.__dict__:
            descriptor = klass.__dict__["ProductID"]
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

def test_order_has_id():
    assert hasattr(Order, "id")
    descriptor = None
    for klass in Order.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "Customer" in params, "Missing parameter 'Customer'"
    assert "Amount" in params, "Missing parameter 'Amount'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Details" in params, "Missing parameter 'Details'"

def test_payment_has_Customer():
    assert hasattr(Payment, "Customer")
    descriptor = None
    for klass in Payment.__mro__:
        if "Customer" in klass.__dict__:
            descriptor = klass.__dict__["Customer"]
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

def test_payment_has_ID():
    assert hasattr(Payment, "ID")
    descriptor = None
    for klass in Payment.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_Details():
    assert hasattr(Payment, "Details")
    descriptor = None
    for klass in Payment.__mro__:
        if "Details" in klass.__dict__:
            descriptor = klass.__dict__["Details"]
            break
    assert isinstance(descriptor, property)



def test_guest_is_not_abstract():
    assert not inspect.isabstract(Guest)


def test_guest_constructor_exists():
    assert callable(Guest.__init__)


def test_guest_constructor_args():
    sig = inspect.signature(Guest.__init__)
    params = list(sig.parameters.keys())



def test_products_is_not_abstract():
    assert not inspect.isabstract(Products)


def test_products_constructor_exists():
    assert callable(Products.__init__)


def test_products_constructor_args():
    sig = inspect.signature(Products.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Description" in params, "Missing parameter 'Description'"

def test_products_has_Name():
    assert hasattr(Products, "Name")
    descriptor = None
    for klass in Products.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_products_has_ID():
    assert hasattr(Products, "ID")
    descriptor = None
    for klass in Products.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_products_has_Description():
    assert hasattr(Products, "Description")
    descriptor = None
    for klass in Products.__mro__:
        if "Description" in klass.__dict__:
            descriptor = klass.__dict__["Description"]
            break
    assert isinstance(descriptor, property)



def test_customer1_is_not_abstract():
    assert not inspect.isabstract(Customer1)


def test_customer1_constructor_exists():
    assert callable(Customer1.__init__)


def test_customer1_constructor_args():
    sig = inspect.signature(Customer1.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Email" in params, "Missing parameter 'Email'"

def test_customer1_has_Name():
    assert hasattr(Customer1, "Name")
    descriptor = None
    for klass in Customer1.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_customer1_has_attribute():
    assert hasattr(Customer1, "attribute")
    descriptor = None
    for klass in Customer1.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_customer1_has_ID():
    assert hasattr(Customer1, "ID")
    descriptor = None
    for klass in Customer1.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_customer1_has_Password():
    assert hasattr(Customer1, "Password")
    descriptor = None
    for klass in Customer1.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_customer1_has_Email():
    assert hasattr(Customer1, "Email")
    descriptor = None
    for klass in Customer1.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "attribute3" in params, "Missing parameter 'attribute3'"
    assert "attribute2" in params, "Missing parameter 'attribute2'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_customer_has_attribute3():
    assert hasattr(Customer, "attribute3")
    descriptor = None
    for klass in Customer.__mro__:
        if "attribute3" in klass.__dict__:
            descriptor = klass.__dict__["attribute3"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_attribute2():
    assert hasattr(Customer, "attribute2")
    descriptor = None
    for klass in Customer.__mro__:
        if "attribute2" in klass.__dict__:
            descriptor = klass.__dict__["attribute2"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_attribute():
    assert hasattr(Customer, "attribute")
    descriptor = None
    for klass in Customer.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
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
OrderCustomer_strategy = st.builds(
    OrderCustomer,
    Order=
        st.none(),
    id=
        st.integers(),
    Customer=
        st.none()
)
Address_strategy = st.builds(
    Address,
    Street=
        safe_text,
    City=
        safe_text,
    House=
        safe_text
)
CustomerProduct_strategy = st.builds(
    CustomerProduct,
    ID=
        st.integers(),
    Product=
        st.none(),
    Customer=
        st.none()
)
OrderProduct_strategy = st.builds(
    OrderProduct,
    ID=
        st.integers(),
    Oid=
        st.none(),
    Pid=
        st.none()
)
Order_strategy = st.builds(
    Order,
    ProductID=
        st.none(),
    Date=
        safe_text,
    id=
        st.integers()
)
Payment_strategy = st.builds(
    Payment,
    Customer=
        st.none(),
    Amount=
        st.integers(),
    ID=
        st.integers(),
    Details=
        safe_text
)
Guest_strategy = st.builds(
    Guest,
)
Products_strategy = st.builds(
    Products,
    Name=
        safe_text,
    ID=
        st.integers(),
    Description=
        safe_text
)
Customer1_strategy = st.builds(
    Customer1,
    Name=
        safe_text,
    attribute=
        safe_text,
    ID=
        safe_text,
    Password=
        safe_text,
    Email=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    attribute3=
        safe_text,
    attribute2=
        safe_text,
    attribute=
        safe_text
)

@given(instance=OrderCustomer_strategy)
@settings(max_examples=50)
def test_ordercustomer_instantiation(instance):
    assert isinstance(instance, OrderCustomer)



@given(instance=OrderCustomer_strategy)
def test_ordercustomer_Order_setter(instance):
    original = instance.Order
    instance.Order = original
    assert instance.Order == original



@given(instance=OrderCustomer_strategy)
def test_ordercustomer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=OrderCustomer_strategy)
def test_ordercustomer_Customer_setter(instance):
    original = instance.Customer
    instance.Customer = original
    assert instance.Customer == original

@given(instance=Address_strategy)
@settings(max_examples=50)
def test_address_instantiation(instance):
    assert isinstance(instance, Address)



@given(instance=Address_strategy)
def test_address_Street_setter(instance):
    original = instance.Street
    instance.Street = original
    assert instance.Street == original



@given(instance=Address_strategy)
def test_address_City_setter(instance):
    original = instance.City
    instance.City = original
    assert instance.City == original



@given(instance=Address_strategy)
def test_address_House_setter(instance):
    original = instance.House
    instance.House = original
    assert instance.House == original

@given(instance=CustomerProduct_strategy)
@settings(max_examples=50)
def test_customerproduct_instantiation(instance):
    assert isinstance(instance, CustomerProduct)



@given(instance=CustomerProduct_strategy)
def test_customerproduct_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=CustomerProduct_strategy)
def test_customerproduct_Product_setter(instance):
    original = instance.Product
    instance.Product = original
    assert instance.Product == original



@given(instance=CustomerProduct_strategy)
def test_customerproduct_Customer_setter(instance):
    original = instance.Customer
    instance.Customer = original
    assert instance.Customer == original

@given(instance=OrderProduct_strategy)
@settings(max_examples=50)
def test_orderproduct_instantiation(instance):
    assert isinstance(instance, OrderProduct)



@given(instance=OrderProduct_strategy)
def test_orderproduct_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=OrderProduct_strategy)
def test_orderproduct_Oid_setter(instance):
    original = instance.Oid
    instance.Oid = original
    assert instance.Oid == original



@given(instance=OrderProduct_strategy)
def test_orderproduct_Pid_setter(instance):
    original = instance.Pid
    instance.Pid = original
    assert instance.Pid == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_ProductID_setter(instance):
    original = instance.ProductID
    instance.ProductID = original
    assert instance.ProductID == original



@given(instance=Order_strategy)
def test_order_Date_setter(instance):
    original = instance.Date
    instance.Date = original
    assert instance.Date == original



@given(instance=Order_strategy)
def test_order_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_Customer_setter(instance):
    original = instance.Customer
    instance.Customer = original
    assert instance.Customer == original



@given(instance=Payment_strategy)
def test_payment_Amount_setter(instance):
    original = instance.Amount
    instance.Amount = original
    assert instance.Amount == original



@given(instance=Payment_strategy)
def test_payment_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Payment_strategy)
def test_payment_Details_setter(instance):
    original = instance.Details
    instance.Details = original
    assert instance.Details == original

@given(instance=Guest_strategy)
@settings(max_examples=50)
def test_guest_instantiation(instance):
    assert isinstance(instance, Guest)

@given(instance=Products_strategy)
@settings(max_examples=50)
def test_products_instantiation(instance):
    assert isinstance(instance, Products)



@given(instance=Products_strategy)
def test_products_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Products_strategy)
def test_products_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Products_strategy)
def test_products_Description_setter(instance):
    original = instance.Description
    instance.Description = original
    assert instance.Description == original

@given(instance=Customer1_strategy)
@settings(max_examples=50)
def test_customer1_instantiation(instance):
    assert isinstance(instance, Customer1)



@given(instance=Customer1_strategy)
def test_customer1_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Customer1_strategy)
def test_customer1_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Customer1_strategy)
def test_customer1_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Customer1_strategy)
def test_customer1_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Customer1_strategy)
def test_customer1_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_attribute3_setter(instance):
    original = instance.attribute3
    instance.attribute3 = original
    assert instance.attribute3 == original



@given(instance=Customer_strategy)
def test_customer_attribute2_setter(instance):
    original = instance.attribute2
    instance.attribute2 = original
    assert instance.attribute2 == original



@given(instance=Customer_strategy)
def test_customer_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original
