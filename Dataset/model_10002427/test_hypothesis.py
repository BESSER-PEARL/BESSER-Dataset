import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Memory_Interface,
    Web_User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_memory_interface_is_not_abstract():
    assert not inspect.isabstract(Memory_Interface)


def test_memory_interface_constructor_exists():
    assert callable(Memory_Interface.__init__)


def test_memory_interface_constructor_args():
    sig = inspect.signature(Memory_Interface.__init__)
    params = list(sig.parameters.keys())



def test_web_user_is_not_abstract():
    assert not inspect.isabstract(Web_User)


def test_web_user_constructor_exists():
    assert callable(Web_User.__init__)


def test_web_user_constructor_args():
    sig = inspect.signature(Web_User.__init__)
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
Memory_Interface_strategy = st.builds(
    Memory_Interface,
)
Web_User_strategy = st.builds(
    Web_User,
)

@given(instance=Memory_Interface_strategy)
@settings(max_examples=50)
def test_memory_interface_instantiation(instance):
    assert isinstance(instance, Memory_Interface)

@given(instance=Web_User_strategy)
@settings(max_examples=50)
def test_web_user_instantiation(instance):
    assert isinstance(instance, Web_User)
