import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Invoice,
    SalariedEmployee,
    Payable_Interface,
    Employee,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_invoice_is_not_abstract():
    assert not inspect.isabstract(Invoice)


def test_invoice_constructor_exists():
    assert callable(Invoice.__init__)


def test_invoice_constructor_args():
    sig = inspect.signature(Invoice.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"
    assert "product" in params, "Missing parameter 'product'"
    assert "num" in params, "Missing parameter 'num'"
    assert "quantity" in params, "Missing parameter 'quantity'"

def test_invoice_has_amount():
    assert hasattr(Invoice, "amount")
    descriptor = None
    for klass in Invoice.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)

def test_invoice_has_product():
    assert hasattr(Invoice, "product")
    descriptor = None
    for klass in Invoice.__mro__:
        if "product" in klass.__dict__:
            descriptor = klass.__dict__["product"]
            break
    assert isinstance(descriptor, property)

def test_invoice_has_num():
    assert hasattr(Invoice, "num")
    descriptor = None
    for klass in Invoice.__mro__:
        if "num" in klass.__dict__:
            descriptor = klass.__dict__["num"]
            break
    assert isinstance(descriptor, property)

def test_invoice_has_quantity():
    assert hasattr(Invoice, "quantity")
    descriptor = None
    for klass in Invoice.__mro__:
        if "quantity" in klass.__dict__:
            descriptor = klass.__dict__["quantity"]
            break
    assert isinstance(descriptor, property)



def test_salariedemployee_is_not_abstract():
    assert not inspect.isabstract(SalariedEmployee)


def test_salariedemployee_constructor_exists():
    assert callable(SalariedEmployee.__init__)


def test_salariedemployee_constructor_args():
    sig = inspect.signature(SalariedEmployee.__init__)
    params = list(sig.parameters.keys())
    assert "salary" in params, "Missing parameter 'salary'"

def test_salariedemployee_has_salary():
    assert hasattr(SalariedEmployee, "salary")
    descriptor = None
    for klass in SalariedEmployee.__mro__:
        if "salary" in klass.__dict__:
            descriptor = klass.__dict__["salary"]
            break
    assert isinstance(descriptor, property)



def test_payable_interface_is_not_abstract():
    assert not inspect.isabstract(Payable_Interface)


def test_payable_interface_constructor_exists():
    assert callable(Payable_Interface.__init__)


def test_payable_interface_constructor_args():
    sig = inspect.signature(Payable_Interface.__init__)
    params = list(sig.parameters.keys())



def test_employee_is_not_abstract():
    assert not inspect.isabstract(Employee)


def test_employee_constructor_exists():
    assert callable(Employee.__init__)


def test_employee_constructor_args():
    sig = inspect.signature(Employee.__init__)
    params = list(sig.parameters.keys())
    assert "lastname" in params, "Missing parameter 'lastname'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "ssn" in params, "Missing parameter 'ssn'"

def test_employee_has_lastname():
    assert hasattr(Employee, "lastname")
    descriptor = None
    for klass in Employee.__mro__:
        if "lastname" in klass.__dict__:
            descriptor = klass.__dict__["lastname"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_firstname():
    assert hasattr(Employee, "firstname")
    descriptor = None
    for klass in Employee.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_employee_has_ssn():
    assert hasattr(Employee, "ssn")
    descriptor = None
    for klass in Employee.__mro__:
        if "ssn" in klass.__dict__:
            descriptor = klass.__dict__["ssn"]
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
Invoice_strategy = st.builds(
    Invoice,
    amount=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    product=
        safe_text,
    num=
        safe_text,
    quantity=
        st.integers()
)
SalariedEmployee_strategy = st.builds(
    SalariedEmployee,
    salary=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Payable_Interface_strategy = st.builds(
    Payable_Interface,
)
Employee_strategy = st.builds(
    Employee,
    lastname=
        safe_text,
    firstname=
        safe_text,
    ssn=
        safe_text
)

@given(instance=Invoice_strategy)
@settings(max_examples=50)
def test_invoice_instantiation(instance):
    assert isinstance(instance, Invoice)



@given(instance=Invoice_strategy)
def test_invoice_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original



@given(instance=Invoice_strategy)
def test_invoice_product_setter(instance):
    original = instance.product
    instance.product = original
    assert instance.product == original



@given(instance=Invoice_strategy)
def test_invoice_num_setter(instance):
    original = instance.num
    instance.num = original
    assert instance.num == original



@given(instance=Invoice_strategy)
def test_invoice_quantity_setter(instance):
    original = instance.quantity
    instance.quantity = original
    assert instance.quantity == original

@given(instance=SalariedEmployee_strategy)
@settings(max_examples=50)
def test_salariedemployee_instantiation(instance):
    assert isinstance(instance, SalariedEmployee)



@given(instance=SalariedEmployee_strategy)
def test_salariedemployee_salary_setter(instance):
    original = instance.salary
    instance.salary = original
    assert instance.salary == original

@given(instance=Payable_Interface_strategy)
@settings(max_examples=50)
def test_payable_interface_instantiation(instance):
    assert isinstance(instance, Payable_Interface)

@given(instance=Employee_strategy)
@settings(max_examples=50)
def test_employee_instantiation(instance):
    assert isinstance(instance, Employee)



@given(instance=Employee_strategy)
def test_employee_lastname_setter(instance):
    original = instance.lastname
    instance.lastname = original
    assert instance.lastname == original



@given(instance=Employee_strategy)
def test_employee_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Employee_strategy)
def test_employee_ssn_setter(instance):
    original = instance.ssn
    instance.ssn = original
    assert instance.ssn == original
