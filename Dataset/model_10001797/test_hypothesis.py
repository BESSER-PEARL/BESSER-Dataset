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



def test_savingsaccount_is_not_abstract():
    assert not inspect.isabstract(SavingsAccount)


def test_savingsaccount_constructor_exists():
    assert callable(SavingsAccount.__init__)


def test_savingsaccount_constructor_args():
    sig = inspect.signature(SavingsAccount.__init__)
    params = list(sig.parameters.keys())



def test_bankaccount_is_not_abstract():
    assert not inspect.isabstract(BankAccount)


def test_bankaccount_constructor_exists():
    assert callable(BankAccount.__init__)


def test_bankaccount_constructor_args():
    sig = inspect.signature(BankAccount.__init__)
    params = list(sig.parameters.keys())
    assert "accountHolderName" in params, "Missing parameter 'accountHolderName'"
    assert "balance" in params, "Missing parameter 'balance'"

def test_bankaccount_has_accountHolderName():
    assert hasattr(BankAccount, "accountHolderName")
    descriptor = None
    for klass in BankAccount.__mro__:
        if "accountHolderName" in klass.__dict__:
            descriptor = klass.__dict__["accountHolderName"]
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
)
SavingsAccount_strategy = st.builds(
    SavingsAccount,
)
BankAccount_strategy = st.builds(
    BankAccount,
    accountHolderName=
        safe_text,
    balance=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)

@given(instance=FixedAccount_strategy)
@settings(max_examples=50)
def test_fixedaccount_instantiation(instance):
    assert isinstance(instance, FixedAccount)

@given(instance=SavingsAccount_strategy)
@settings(max_examples=50)
def test_savingsaccount_instantiation(instance):
    assert isinstance(instance, SavingsAccount)

@given(instance=BankAccount_strategy)
@settings(max_examples=50)
def test_bankaccount_instantiation(instance):
    assert isinstance(instance, BankAccount)



@given(instance=BankAccount_strategy)
def test_bankaccount_accountHolderName_setter(instance):
    original = instance.accountHolderName
    instance.accountHolderName = original
    assert instance.accountHolderName == original



@given(instance=BankAccount_strategy)
def test_bankaccount_balance_setter(instance):
    original = instance.balance
    instance.balance = original
    assert instance.balance == original
