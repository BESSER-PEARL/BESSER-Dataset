import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    UserHomePage,
    ManagerHomePage,
    AdminHomePage,
    AbstractHomePage,
    RegisterPage,
    LoginPage,
    AbstractWebpage,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_userhomepage_is_not_abstract():
    assert not inspect.isabstract(UserHomePage)


def test_userhomepage_constructor_exists():
    assert callable(UserHomePage.__init__)


def test_userhomepage_constructor_args():
    sig = inspect.signature(UserHomePage.__init__)
    params = list(sig.parameters.keys())



def test_managerhomepage_is_not_abstract():
    assert not inspect.isabstract(ManagerHomePage)


def test_managerhomepage_constructor_exists():
    assert callable(ManagerHomePage.__init__)


def test_managerhomepage_constructor_args():
    sig = inspect.signature(ManagerHomePage.__init__)
    params = list(sig.parameters.keys())



def test_adminhomepage_is_not_abstract():
    assert not inspect.isabstract(AdminHomePage)


def test_adminhomepage_constructor_exists():
    assert callable(AdminHomePage.__init__)


def test_adminhomepage_constructor_args():
    sig = inspect.signature(AdminHomePage.__init__)
    params = list(sig.parameters.keys())



def test_abstracthomepage_is_not_abstract():
    assert not inspect.isabstract(AbstractHomePage)


def test_abstracthomepage_constructor_exists():
    assert callable(AbstractHomePage.__init__)


def test_abstracthomepage_constructor_args():
    sig = inspect.signature(AbstractHomePage.__init__)
    params = list(sig.parameters.keys())



def test_registerpage_is_not_abstract():
    assert not inspect.isabstract(RegisterPage)


def test_registerpage_constructor_exists():
    assert callable(RegisterPage.__init__)


def test_registerpage_constructor_args():
    sig = inspect.signature(RegisterPage.__init__)
    params = list(sig.parameters.keys())



def test_loginpage_is_not_abstract():
    assert not inspect.isabstract(LoginPage)


def test_loginpage_constructor_exists():
    assert callable(LoginPage.__init__)


def test_loginpage_constructor_args():
    sig = inspect.signature(LoginPage.__init__)
    params = list(sig.parameters.keys())



def test_abstractwebpage_is_not_abstract():
    assert not inspect.isabstract(AbstractWebpage)


def test_abstractwebpage_constructor_exists():
    assert callable(AbstractWebpage.__init__)


def test_abstractwebpage_constructor_args():
    sig = inspect.signature(AbstractWebpage.__init__)
    params = list(sig.parameters.keys())


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
UserHomePage_strategy = st.builds(
    UserHomePage,
)
ManagerHomePage_strategy = st.builds(
    ManagerHomePage,
)
AdminHomePage_strategy = st.builds(
    AdminHomePage,
)
AbstractHomePage_strategy = st.builds(
    AbstractHomePage,
)
RegisterPage_strategy = st.builds(
    RegisterPage,
)
LoginPage_strategy = st.builds(
    LoginPage,
)
AbstractWebpage_strategy = st.builds(
    AbstractWebpage,
)

@given(instance=UserHomePage_strategy)
@settings(max_examples=50)
def test_userhomepage_instantiation(instance):
    assert isinstance(instance, UserHomePage)

@given(instance=ManagerHomePage_strategy)
@settings(max_examples=50)
def test_managerhomepage_instantiation(instance):
    assert isinstance(instance, ManagerHomePage)

@given(instance=AdminHomePage_strategy)
@settings(max_examples=50)
def test_adminhomepage_instantiation(instance):
    assert isinstance(instance, AdminHomePage)

@given(instance=AbstractHomePage_strategy)
@settings(max_examples=50)
def test_abstracthomepage_instantiation(instance):
    assert isinstance(instance, AbstractHomePage)

@given(instance=RegisterPage_strategy)
@settings(max_examples=50)
def test_registerpage_instantiation(instance):
    assert isinstance(instance, RegisterPage)

@given(instance=LoginPage_strategy)
@settings(max_examples=50)
def test_loginpage_instantiation(instance):
    assert isinstance(instance, LoginPage)

@given(instance=AbstractWebpage_strategy)
@settings(max_examples=50)
def test_abstractwebpage_instantiation(instance):
    assert isinstance(instance, AbstractWebpage)
