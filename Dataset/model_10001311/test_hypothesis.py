import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Student,
    Savings,
    Main,
    Instructor,
    Checking,
    BankAccount,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_student_is_not_abstract():
    assert not inspect.isabstract(Student)


def test_student_constructor_exists():
    assert callable(Student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(Student.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_student_has_name():
    assert hasattr(Student, "name")
    descriptor = None
    for klass in Student.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_savings_is_not_abstract():
    assert not inspect.isabstract(Savings)


def test_savings_constructor_exists():
    assert callable(Savings.__init__)


def test_savings_constructor_args():
    sig = inspect.signature(Savings.__init__)
    params = list(sig.parameters.keys())



def test_main_is_not_abstract():
    assert not inspect.isabstract(Main)


def test_main_constructor_exists():
    assert callable(Main.__init__)


def test_main_constructor_args():
    sig = inspect.signature(Main.__init__)
    params = list(sig.parameters.keys())



def test_instructor_is_not_abstract():
    assert not inspect.isabstract(Instructor)


def test_instructor_constructor_exists():
    assert callable(Instructor.__init__)


def test_instructor_constructor_args():
    sig = inspect.signature(Instructor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_instructor_has_name():
    assert hasattr(Instructor, "name")
    descriptor = None
    for klass in Instructor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_checking_is_not_abstract():
    assert not inspect.isabstract(Checking)


def test_checking_constructor_exists():
    assert callable(Checking.__init__)


def test_checking_constructor_args():
    sig = inspect.signature(Checking.__init__)
    params = list(sig.parameters.keys())
    assert "OVERDRAFT_FEE" in params, "Missing parameter 'OVERDRAFT_FEE'"
    assert "OVERDRAFT_LIMIT" in params, "Missing parameter 'OVERDRAFT_LIMIT'"
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_checking_has_OVERDRAFT_FEE():
    assert hasattr(Checking, "OVERDRAFT_FEE")
    descriptor = None
    for klass in Checking.__mro__:
        if "OVERDRAFT_FEE" in klass.__dict__:
            descriptor = klass.__dict__["OVERDRAFT_FEE"]
            break
    assert isinstance(descriptor, property)

def test_checking_has_OVERDRAFT_LIMIT():
    assert hasattr(Checking, "OVERDRAFT_LIMIT")
    descriptor = None
    for klass in Checking.__mro__:
        if "OVERDRAFT_LIMIT" in klass.__dict__:
            descriptor = klass.__dict__["OVERDRAFT_LIMIT"]
            break
    assert isinstance(descriptor, property)

def test_checking_has_isActive():
    assert hasattr(Checking, "isActive")
    descriptor = None
    for klass in Checking.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "TRANSACTION_FEE" in params, "Missing parameter 'TRANSACTION_FEE'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "balance" in params, "Missing parameter 'balance'"
    assert "numOfTransactions" in params, "Missing parameter 'numOfTransactions'"
    assert "minimumBalance" in params, "Missing parameter 'minimumBalance'"
    assert "FREE_TRANSACTIONS" in params, "Missing parameter 'FREE_TRANSACTIONS'"

def test_bankaccount_has_TRANSACTION_FEE():
    assert hasattr(BankAccount, "TRANSACTION_FEE")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "TRANSACTION_FEE" in klass.__dict__:
            descriptor = klass.__dict__["TRANSACTION_FEE"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_isActive():
    assert hasattr(BankAccount, "isActive")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_balance():
    assert hasattr(BankAccount, "balance")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "balance" in klass.__dict__:
            descriptor = klass.__dict__["balance"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_numOfTransactions():
    assert hasattr(BankAccount, "numOfTransactions")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "numOfTransactions" in klass.__dict__:
            descriptor = klass.__dict__["numOfTransactions"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_minimumBalance():
    assert hasattr(BankAccount, "minimumBalance")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "minimumBalance" in klass.__dict__:
            descriptor = klass.__dict__["minimumBalance"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_FREE_TRANSACTIONS():
    assert hasattr(BankAccount, "FREE_TRANSACTIONS")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "FREE_TRANSACTIONS" in klass.__dict__:
            descriptor = klass.__dict__["FREE_TRANSACTIONS"]
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
Student_strategy = st.builds(
    Student,
    name=
        safe_text
)
Savings_strategy = st.builds(
    Savings,
)
Main_strategy = st.builds(
    Main,
)
Instructor_strategy = st.builds(
    Instructor,
    name=
        safe_text
)
Checking_strategy = st.builds(
    Checking,
    OVERDRAFT_FEE=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    OVERDRAFT_LIMIT=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    isActive=
        st.booleans()
)
BankAccount_strategy = st.builds(
    BankAccount,
    TRANSACTION_FEE=
        st.integers(),
    isActive=
        st.booleans(),
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    numOfTransactions=
        st.integers(),
    minimumBalance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    FREE_TRANSACTIONS=
        st.integers()
)

@given(instance=Student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, Student)



@given(instance=Student_strategy)
def test_student_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Savings_strategy)
@settings(max_examples=50)
def test_savings_instantiation(instance):
    assert isinstance(instance, Savings)

@given(instance=Main_strategy)
@settings(max_examples=50)
def test_main_instantiation(instance):
    assert isinstance(instance, Main)

@given(instance=Instructor_strategy)
@settings(max_examples=50)
def test_instructor_instantiation(instance):
    assert isinstance(instance, Instructor)



@given(instance=Instructor_strategy)
def test_instructor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Checking_strategy)
@settings(max_examples=50)
def test_checking_instantiation(instance):
    assert isinstance(instance, Checking)



@given(instance=Checking_strategy)
def test_checking_OVERDRAFT_FEE_setter(instance):
    original = instance.OVERDRAFT_FEE
    instance.OVERDRAFT_FEE = original
    assert instance.OVERDRAFT_FEE == original



@given(instance=Checking_strategy)
def test_checking_OVERDRAFT_LIMIT_setter(instance):
    original = instance.OVERDRAFT_LIMIT
    instance.OVERDRAFT_LIMIT = original
    assert instance.OVERDRAFT_LIMIT == original



@given(instance=Checking_strategy)
def test_checking_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=BankAccount_strategy)
@settings(max_examples=50)
def test_bankaccount_instantiation(instance):
    assert isinstance(instance, BankAccount)



@given(instance=BankAccount_strategy)
def test_bankaccount_TRANSACTION_FEE_setter(instance):
    original = instance.TRANSACTION_FEE
    instance.TRANSACTION_FEE = original
    assert instance.TRANSACTION_FEE == original



@given(instance=BankAccount_strategy)
def test_bankaccount_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=BankAccount_strategy)
def test_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original



@given(instance=BankAccount_strategy)
def test_bankaccount_numOfTransactions_setter(instance):
    original = instance.numOfTransactions
    instance.numOfTransactions = original
    assert instance.numOfTransactions == original



@given(instance=BankAccount_strategy)
def test_bankaccount_minimumBalance_setter(instance):
    original = instance.minimumBalance
    instance.minimumBalance = original
    assert instance.minimumBalance == original



@given(instance=BankAccount_strategy)
def test_bankaccount_FREE_TRANSACTIONS_setter(instance):
    original = instance.FREE_TRANSACTIONS
    instance.FREE_TRANSACTIONS = original
    assert instance.FREE_TRANSACTIONS == original
