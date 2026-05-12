import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FixedAccount,
    SavingsAccount,
    BankAccount,
    Bank,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fixedaccount_is_not_abstract():
    assert not inspect.isabstract(FixedAccount)


def test_fixedaccount_constructor_exists():
    assert callable(FixedAccount.__init__)


def test_fixedaccount_constructor_args():
    sig = inspect.signature(FixedAccount.__init__)
    params = list(sig.parameters.keys())
    assert "chequeBookNo" in params, "Missing parameter 'chequeBookNo'"

def test_fixedaccount_has_chequeBookNo():
    assert hasattr(FixedAccount, "chequeBookNo")
    descriptor = None
    for klass in FixedAccount.__mro__:
        if "chequeBookNo" in klass.__dict__:
            descriptor = klass.__dict__["chequeBookNo"]
            break
    assert isinstance(descriptor, property)



def test_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(SavingsAccount)


def test_savingsaccount_constructor_exists():
    assert callable(SavingsAccount.__init__)


def test_savingsaccount_constructor_args():
    sig = inspect.signature(SavingsAccount.__init__)
    params = list(sig.parameters.keys())
    assert "noticeGiven" in params, "Missing parameter 'noticeGiven'"
    assert "interestRate" in params, "Missing parameter 'interestRate'"

def test_savingsaccount_has_noticeGiven():
    assert hasattr(SavingsAccount, "noticeGiven")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "noticeGiven" in klass.__dict__:
            descriptor = klass.__dict__["noticeGiven"]
            break
    assert isinstance(descriptor, property)

def test_savingsaccount_has_interestRate():
    assert hasattr(SavingsAccount, "interestRate")
    descriptor = None
    for klass in SavingsAccount.__mro__:
        if "interestRate" in klass.__dict__:
            descriptor = klass.__dict__["interestRate"]
            break
    assert isinstance(descriptor, property)



def test_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "accountHolder" in params, "Missing parameter 'accountHolder'"
    assert "accountNumber" in params, "Missing parameter 'accountNumber'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_bankaccount_has_accountHolder():
    assert hasattr(BankAccount, "accountHolder")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "accountHolder" in klass.__dict__:
            descriptor = klass.__dict__["accountHolder"]
            break
    assert isinstance(descriptor, property)

def test_bankaccount_has_accountNumber():
    assert hasattr(BankAccount, "accountNumber")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "accountNumber" in klass.__dict__:
            descriptor = klass.__dict__["accountNumber"]
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



def test_bank_is_not_abstract():
    assert not inspect.isabstract(Bank)


def test_bank_constructor_exists():
    assert callable(Bank.__init__)


def test_bank_constructor_args():
    sig = inspect.signature(Bank.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_bank_has_name():
    assert hasattr(Bank, "name")
    descriptor = None
    for klass in Bank.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
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
FixedAccount_strategy = st.builds(
    FixedAccount,
    chequeBookNo=
        safe_text
)
SavingsAccount_strategy = st.builds(
    SavingsAccount,
    noticeGiven=
        st.booleans(),
    interestRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
BankAccount_strategy = st.builds(
    BankAccount,
    accountHolder=
        safe_text,
    accountNumber=
        st.integers(),
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Bank_strategy = st.builds(
    Bank,
    name=
        safe_text
)

@given(instance=FixedAccount_strategy)
@settings(max_examples=50)
def test_fixedaccount_instantiation(instance):
    assert isinstance(instance, FixedAccount)



@given(instance=FixedAccount_strategy)
def test_fixedaccount_chequeBookNo_setter(instance):
    original = instance.chequeBookNo
    instance.chequeBookNo = original
    assert instance.chequeBookNo == original

@given(instance=SavingsAccount_strategy)
@settings(max_examples=50)
def test_savingsaccount_instantiation(instance):
    assert isinstance(instance, SavingsAccount)



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_noticeGiven_setter(instance):
    original = instance.noticeGiven
    instance.noticeGiven = original
    assert instance.noticeGiven == original



@given(instance=SavingsAccount_strategy)
def test_savingsaccount_interestRate_setter(instance):
    original = instance.interestRate
    instance.interestRate = original
    assert instance.interestRate == original

@given(instance=BankAccount_strategy)
@settings(max_examples=50)
def test_bankaccount_instantiation(instance):
    assert isinstance(instance, BankAccount)



@given(instance=BankAccount_strategy)
def test_bankaccount_accountHolder_setter(instance):
    original = instance.accountHolder
    instance.accountHolder = original
    assert instance.accountHolder == original



@given(instance=BankAccount_strategy)
def test_bankaccount_accountNumber_setter(instance):
    original = instance.accountNumber
    instance.accountNumber = original
    assert instance.accountNumber == original



@given(instance=BankAccount_strategy)
def test_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original

@given(instance=Bank_strategy)
@settings(max_examples=50)
def test_bank_instantiation(instance):
    assert isinstance(instance, Bank)



@given(instance=Bank_strategy)
def test_bank_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
