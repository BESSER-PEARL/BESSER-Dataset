import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Customer_Support,
    Shop_Owner,
    Administrator,
    AjoutProduit_UseCase,
    Webuser_Actor,
    Admin_Actor,
    MyActor_Actor,
    Product,
    LineItem,
    Order,
    Visitor,
    Account,
    ShoppingCart,
    Payment,
    Customer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_customer_support_is_not_abstract():
    assert not inspect.isabstract(Customer_Support)


def test_customer_support_constructor_exists():
    assert callable(Customer_Support.__init__)


def test_customer_support_constructor_args():
    sig = inspect.signature(Customer_Support.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_customer_support_has_ID():
    assert hasattr(Customer_Support, "ID")
    descriptor = None
    for klass in Customer_Support.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_customer_support_has_Email():
    assert hasattr(Customer_Support, "Email")
    descriptor = None
    for klass in Customer_Support.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_customer_support_has_Password():
    assert hasattr(Customer_Support, "Password")
    descriptor = None
    for klass in Customer_Support.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_shop_owner_is_not_abstract():
    assert not inspect.isabstract(Shop_Owner)


def test_shop_owner_constructor_exists():
    assert callable(Shop_Owner.__init__)


def test_shop_owner_constructor_args():
    sig = inspect.signature(Shop_Owner.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Last_name" in params, "Missing parameter 'Last_name'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "IDSowner" in params, "Missing parameter 'IDSowner'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_shop_owner_has_Name():
    assert hasattr(Shop_Owner, "Name")
    descriptor = None
    for klass in Shop_Owner.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_shop_owner_has_Last_name():
    assert hasattr(Shop_Owner, "Last_name")
    descriptor = None
    for klass in Shop_Owner.__mro__:
        if "Last_name" in klass.__dict__:
            descriptor = klass.__dict__["Last_name"]
            break
    assert isinstance(descriptor, property)

def test_shop_owner_has_Email():
    assert hasattr(Shop_Owner, "Email")
    descriptor = None
    for klass in Shop_Owner.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_shop_owner_has_IDSowner():
    assert hasattr(Shop_Owner, "IDSowner")
    descriptor = None
    for klass in Shop_Owner.__mro__:
        if "IDSowner" in klass.__dict__:
            descriptor = klass.__dict__["IDSowner"]
            break
    assert isinstance(descriptor, property)

def test_shop_owner_has_Password():
    assert hasattr(Shop_Owner, "Password")
    descriptor = None
    for klass in Shop_Owner.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_administrator_is_not_abstract():
    assert not inspect.isabstract(Administrator)


def test_administrator_constructor_exists():
    assert callable(Administrator.__init__)


def test_administrator_constructor_args():
    sig = inspect.signature(Administrator.__init__)
    params = list(sig.parameters.keys())
    assert "Last_name" in params, "Missing parameter 'Last_name'"
    assert "IDAdm" in params, "Missing parameter 'IDAdm'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_administrator_has_Last_name():
    assert hasattr(Administrator, "Last_name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Last_name" in klass.__dict__:
            descriptor = klass.__dict__["Last_name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_IDAdm():
    assert hasattr(Administrator, "IDAdm")
    descriptor = None
    for klass in Administrator.__mro__:
        if "IDAdm" in klass.__dict__:
            descriptor = klass.__dict__["IDAdm"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Name():
    assert hasattr(Administrator, "Name")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Email():
    assert hasattr(Administrator, "Email")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_administrator_has_Password():
    assert hasattr(Administrator, "Password")
    descriptor = None
    for klass in Administrator.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_ajoutproduit_usecase_is_not_abstract():
    assert not inspect.isabstract(AjoutProduit_UseCase)


def test_ajoutproduit_usecase_constructor_exists():
    assert callable(AjoutProduit_UseCase.__init__)


def test_ajoutproduit_usecase_constructor_args():
    sig = inspect.signature(AjoutProduit_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_webuser_actor_is_not_abstract():
    assert not inspect.isabstract(Webuser_Actor)


def test_webuser_actor_constructor_exists():
    assert callable(Webuser_Actor.__init__)


def test_webuser_actor_constructor_args():
    sig = inspect.signature(Webuser_Actor.__init__)
    params = list(sig.parameters.keys())



def test_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_myactor_actor_is_not_abstract():
    assert not inspect.isabstract(MyActor_Actor)


def test_myactor_actor_constructor_exists():
    assert callable(MyActor_Actor.__init__)


def test_myactor_actor_constructor_args():
    sig = inspect.signature(MyActor_Actor.__init__)
    params = list(sig.parameters.keys())



def test_product_is_not_abstract():
    assert not inspect.isabstract(Product)


def test_product_constructor_exists():
    assert callable(Product.__init__)


def test_product_constructor_args():
    sig = inspect.signature(Product.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_product_has_name():
    assert hasattr(Product, "name")
    descriptor = None
    for klass in Product.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_product_has_description():
    assert hasattr(Product, "description")
    descriptor = None
    for klass in Product.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_lineitem_is_not_abstract():
    assert not inspect.isabstract(LineItem)


def test_lineitem_constructor_exists():
    assert callable(LineItem.__init__)


def test_lineitem_constructor_args():
    sig = inspect.signature(LineItem.__init__)
    params = list(sig.parameters.keys())
    assert "quantity" in params, "Missing parameter 'quantity'"
    assert "price" in params, "Missing parameter 'price'"

def test_lineitem_has_quantity():
    assert hasattr(LineItem, "quantity")
    descriptor = None
    for klass in LineItem.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)

def test_lineitem_has_price():
    assert hasattr(LineItem, "price")
    descriptor = None
    for klass in LineItem.__mro__:
        if "price" in klass.__dict__:
            descriptor = klass.__dict__["price"]
            break
    assert isinstance(descriptor, property)



def test_order_is_not_abstract():
    assert not inspect.isabstract(Order)


def test_order_constructor_exists():
    assert callable(Order.__init__)


def test_order_constructor_args():
    sig = inspect.signature(Order.__init__)
    params = list(sig.parameters.keys())
    assert "total" in params, "Missing parameter 'total'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "shipTo" in params, "Missing parameter 'shipTo'"
    assert "shipped" in params, "Missing parameter 'shipped'"
    assert "number" in params, "Missing parameter 'number'"
    assert "status" in params, "Missing parameter 'status'"

def test_order_has_total():
    assert hasattr(Order, "total")
    descriptor = None
    for klass in Order.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_order_has_ordered():
    assert hasattr(Order, "ordered")
    descriptor = None
    for klass in Order.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shipTo():
    assert hasattr(Order, "shipTo")
    descriptor = None
    for klass in Order.__mro__:
        if "shipTo" in klass.__dict__:
            descriptor = klass.__dict__["shipTo"]
            break
    assert isinstance(descriptor, property)

def test_order_has_shipped():
    assert hasattr(Order, "shipped")
    descriptor = None
    for klass in Order.__mro__:
        if "shipped" in klass.__dict__:
            descriptor = klass.__dict__["shipped"]
            break
    assert isinstance(descriptor, property)

def test_order_has_number():
    assert hasattr(Order, "number")
    descriptor = None
    for klass in Order.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_order_has_status():
    assert hasattr(Order, "status")
    descriptor = None
    for klass in Order.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_visitor_is_not_abstract():
    assert not inspect.isabstract(Visitor)


def test_visitor_constructor_exists():
    assert callable(Visitor.__init__)


def test_visitor_constructor_args():
    sig = inspect.signature(Visitor.__init__)
    params = list(sig.parameters.keys())



def test_account_is_not_abstract():
    assert not inspect.isabstract(Account)


def test_account_constructor_exists():
    assert callable(Account.__init__)


def test_account_constructor_args():
    sig = inspect.signature(Account.__init__)
    params = list(sig.parameters.keys())
    assert "open" in params, "Missing parameter 'open'"
    assert "closed" in params, "Missing parameter 'closed'"
    assert "billingAddress" in params, "Missing parameter 'billingAddress'"
    assert "isClosed" in params, "Missing parameter 'isClosed'"

def test_account_has_open():
    assert hasattr(Account, "open")
    descriptor = None
    for klass in Account.__mro__:
        if "open" in klass.__dict__:
            descriptor = klass.__dict__["open"]
            break
    assert isinstance(descriptor, property)

def test_account_has_closed():
    assert hasattr(Account, "closed")
    descriptor = None
    for klass in Account.__mro__:
        if "closed" in klass.__dict__:
            descriptor = klass.__dict__["closed"]
            break
    assert isinstance(descriptor, property)

def test_account_has_billingAddress():
    assert hasattr(Account, "billingAddress")
    descriptor = None
    for klass in Account.__mro__:
        if "billingAddress" in klass.__dict__:
            descriptor = klass.__dict__["billingAddress"]
            break
    assert isinstance(descriptor, property)

def test_account_has_isClosed():
    assert hasattr(Account, "isClosed")
    descriptor = None
    for klass in Account.__mro__:
        if "isClosed" in klass.__dict__:
            descriptor = klass.__dict__["isClosed"]
            break
    assert isinstance(descriptor, property)



def test_shoppingcart_is_not_abstract():
    assert not inspect.isabstract(ShoppingCart)


def test_shoppingcart_constructor_exists():
    assert callable(ShoppingCart.__init__)


def test_shoppingcart_constructor_args():
    sig = inspect.signature(ShoppingCart.__init__)
    params = list(sig.parameters.keys())
    assert "creationDate" in params, "Missing parameter 'creationDate'"

def test_shoppingcart_has_creationDate():
    assert hasattr(ShoppingCart, "creationDate")
    descriptor = None
    for klass in ShoppingCart.__mro__:
        if "creationDate" in klass.__dict__:
            descriptor = klass.__dict__["creationDate"]
            break
    assert isinstance(descriptor, property)



def test_payment_is_not_abstract():
    assert not inspect.isabstract(Payment)


def test_payment_constructor_exists():
    assert callable(Payment.__init__)


def test_payment_constructor_args():
    sig = inspect.signature(Payment.__init__)
    params = list(sig.parameters.keys())
    assert "total" in params, "Missing parameter 'total'"
    assert "paidDate" in params, "Missing parameter 'paidDate'"
    assert "details" in params, "Missing parameter 'details'"

def test_payment_has_total():
    assert hasattr(Payment, "total")
    descriptor = None
    for klass in Payment.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_paidDate():
    assert hasattr(Payment, "paidDate")
    descriptor = None
    for klass in Payment.__mro__:
        if "paidDate" in klass.__dict__:
            descriptor = klass.__dict__["paidDate"]
            break
    assert isinstance(descriptor, property)

def test_payment_has_details():
    assert hasattr(Payment, "details")
    descriptor = None
    for klass in Payment.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "IDCust" in params, "Missing parameter 'IDCust'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Last_name" in params, "Missing parameter 'Last_name'"

def test_customer_has_IDCust():
    assert hasattr(Customer, "IDCust")
    descriptor = None
    for klass in Customer.__mro__:
        if "IDCust" in klass.__dict__:
            descriptor = klass.__dict__["IDCust"]
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

def test_customer_has_Name():
    assert hasattr(Customer, "Name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Password():
    assert hasattr(Customer, "Password")
    descriptor = None
    for klass in Customer.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_customer_has_Last_name():
    assert hasattr(Customer, "Last_name")
    descriptor = None
    for klass in Customer.__mro__:
        if "Last_name" in klass.__dict__:
            descriptor = klass.__dict__["Last_name"]
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
Customer_Support_strategy = st.builds(
    Customer_Support,
    ID=
        st.integers(),
    Email=
        safe_text,
    Password=
        safe_text
)
Shop_Owner_strategy = st.builds(
    Shop_Owner,
    Name=
        safe_text,
    Last_name=
        safe_text,
    Email=
        safe_text,
    IDSowner=
        st.integers(),
    Password=
        safe_text
)
Administrator_strategy = st.builds(
    Administrator,
    Last_name=
        safe_text,
    IDAdm=
        st.integers(),
    Name=
        safe_text,
    Email=
        safe_text,
    Password=
        safe_text
)
AjoutProduit_UseCase_strategy = st.builds(
    AjoutProduit_UseCase,
)
Webuser_Actor_strategy = st.builds(
    Webuser_Actor,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)
MyActor_Actor_strategy = st.builds(
    MyActor_Actor,
)
Product_strategy = st.builds(
    Product,
    name=
        safe_text,
    description=
        safe_text
)
LineItem_strategy = st.builds(
    LineItem,
    quantity=
        st.integers(),
    price=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Order_strategy = st.builds(
    Order,
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    ordered=
        st.dates(),
    shipTo=
        safe_text,
    shipped=
        st.booleans(),
    number=
        st.integers(),
    status=
        safe_text
)
Visitor_strategy = st.builds(
    Visitor,
)
Account_strategy = st.builds(
    Account,
    open=
        st.dates(),
    closed=
        st.dates(),
    billingAddress=
        safe_text,
    isClosed=
        st.booleans()
)
ShoppingCart_strategy = st.builds(
    ShoppingCart,
    creationDate=
        st.dates()
)
Payment_strategy = st.builds(
    Payment,
    total=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    paidDate=
        st.dates(),
    details=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    IDCust=
        st.integers(),
    Email=
        safe_text,
    Name=
        safe_text,
    Password=
        safe_text,
    Last_name=
        safe_text
)

@given(instance=Customer_Support_strategy)
@settings(max_examples=50)
def test_customer_support_instantiation(instance):
    assert isinstance(instance, Customer_Support)



@given(instance=Customer_Support_strategy)
def test_customer_support_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original



@given(instance=Customer_Support_strategy)
def test_customer_support_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Customer_Support_strategy)
def test_customer_support_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Shop_Owner_strategy)
@settings(max_examples=50)
def test_shop_owner_instantiation(instance):
    assert isinstance(instance, Shop_Owner)



@given(instance=Shop_Owner_strategy)
def test_shop_owner_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Shop_Owner_strategy)
def test_shop_owner_Last_name_setter(instance):
    original = instance.Last_name
    instance.Last_name = original
    assert instance.Last_name == original



@given(instance=Shop_Owner_strategy)
def test_shop_owner_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Shop_Owner_strategy)
def test_shop_owner_IDSowner_setter(instance):
    original = instance.IDSowner
    instance.IDSowner = original
    assert instance.IDSowner == original



@given(instance=Shop_Owner_strategy)
def test_shop_owner_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Administrator_strategy)
@settings(max_examples=50)
def test_administrator_instantiation(instance):
    assert isinstance(instance, Administrator)



@given(instance=Administrator_strategy)
def test_administrator_Last_name_setter(instance):
    original = instance.Last_name
    instance.Last_name = original
    assert instance.Last_name == original



@given(instance=Administrator_strategy)
def test_administrator_IDAdm_setter(instance):
    original = instance.IDAdm
    instance.IDAdm = original
    assert instance.IDAdm == original



@given(instance=Administrator_strategy)
def test_administrator_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Administrator_strategy)
def test_administrator_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Administrator_strategy)
def test_administrator_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=AjoutProduit_UseCase_strategy)
@settings(max_examples=50)
def test_ajoutproduit_usecase_instantiation(instance):
    assert isinstance(instance, AjoutProduit_UseCase)

@given(instance=Webuser_Actor_strategy)
@settings(max_examples=50)
def test_webuser_actor_instantiation(instance):
    assert isinstance(instance, Webuser_Actor)

@given(instance=Admin_Actor_strategy)
@settings(max_examples=50)
def test_admin_actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)

@given(instance=MyActor_Actor_strategy)
@settings(max_examples=50)
def test_myactor_actor_instantiation(instance):
    assert isinstance(instance, MyActor_Actor)

@given(instance=Product_strategy)
@settings(max_examples=50)
def test_product_instantiation(instance):
    assert isinstance(instance, Product)



@given(instance=Product_strategy)
def test_product_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Product_strategy)
def test_product_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=LineItem_strategy)
@settings(max_examples=50)
def test_lineitem_instantiation(instance):
    assert isinstance(instance, LineItem)



@given(instance=LineItem_strategy)
def test_lineitem_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original



@given(instance=LineItem_strategy)
def test_lineitem_price_setter(instance):
    original = instance.price
    instance.price = original
    assert instance.price == original

@given(instance=Order_strategy)
@settings(max_examples=50)
def test_order_instantiation(instance):
    assert isinstance(instance, Order)



@given(instance=Order_strategy)
def test_order_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Order_strategy)
def test_order_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=Order_strategy)
def test_order_shipTo_setter(instance):
    original = instance.shipTo
    instance.shipTo = original
    assert instance.shipTo == original



@given(instance=Order_strategy)
def test_order_shipped_setter(instance):
    original = instance.shipped
    instance.shipped = original
    assert instance.shipped == original



@given(instance=Order_strategy)
def test_order_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Order_strategy)
def test_order_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Visitor_strategy)
@settings(max_examples=50)
def test_visitor_instantiation(instance):
    assert isinstance(instance, Visitor)

@given(instance=Account_strategy)
@settings(max_examples=50)
def test_account_instantiation(instance):
    assert isinstance(instance, Account)



@given(instance=Account_strategy)
def test_account_open_setter(instance):
    original = instance.open
    instance.open = original
    assert instance.open == original



@given(instance=Account_strategy)
def test_account_closed_setter(instance):
    original = instance.closed
    instance.closed = original
    assert instance.closed == original



@given(instance=Account_strategy)
def test_account_billingAddress_setter(instance):
    original = instance.billingAddress
    instance.billingAddress = original
    assert instance.billingAddress == original



@given(instance=Account_strategy)
def test_account_isClosed_setter(instance):
    original = instance.isClosed
    instance.isClosed = original
    assert instance.isClosed == original

@given(instance=ShoppingCart_strategy)
@settings(max_examples=50)
def test_shoppingcart_instantiation(instance):
    assert isinstance(instance, ShoppingCart)



@given(instance=ShoppingCart_strategy)
def test_shoppingcart_creationDate_setter(instance):
    original = instance.creationDate
    instance.creationDate = original
    assert instance.creationDate == original

@given(instance=Payment_strategy)
@settings(max_examples=50)
def test_payment_instantiation(instance):
    assert isinstance(instance, Payment)



@given(instance=Payment_strategy)
def test_payment_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=Payment_strategy)
def test_payment_paidDate_setter(instance):
    original = instance.paidDate
    instance.paidDate = original
    assert instance.paidDate == original



@given(instance=Payment_strategy)
def test_payment_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_IDCust_setter(instance):
    original = instance.IDCust
    instance.IDCust = original
    assert instance.IDCust == original



@given(instance=Customer_strategy)
def test_customer_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=Customer_strategy)
def test_customer_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=Customer_strategy)
def test_customer_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Customer_strategy)
def test_customer_Last_name_setter(instance):
    original = instance.Last_name
    instance.Last_name = original
    assert instance.Last_name == original
