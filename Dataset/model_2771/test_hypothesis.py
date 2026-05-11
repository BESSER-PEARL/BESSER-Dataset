import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ecoreJavascriptTest::C2,
    ecoreJavascriptTest::C1,
    C2,
    ecoreJavascriptTest::C3,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ecorejavascripttest::c2_is_not_abstract():
    assert not inspect.isabstract(ecoreJavascriptTest::C2)


def test_ecorejavascripttest::c2_constructor_exists():
    assert callable(ecoreJavascriptTest::C2.__init__)


def test_ecorejavascripttest::c2_constructor_args():
    sig = inspect.signature(ecoreJavascriptTest::C2.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "value" in params, "Missing parameter 'value'"

def test_ecorejavascripttest::c2_has_name():
    assert hasattr(ecoreJavascriptTest::C2, "name")
    descriptor = None
    for klass in ecoreJavascriptTest::C2.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_ecorejavascripttest::c2_has_value():
    assert hasattr(ecoreJavascriptTest::C2, "value")
    descriptor = None
    for klass in ecoreJavascriptTest::C2.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_ecorejavascripttest::c1_is_not_abstract():
    assert not inspect.isabstract(ecoreJavascriptTest::C1)


def test_ecorejavascripttest::c1_constructor_exists():
    assert callable(ecoreJavascriptTest::C1.__init__)


def test_ecorejavascripttest::c1_constructor_args():
    sig = inspect.signature(ecoreJavascriptTest::C1.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_ecorejavascripttest::c1_has_name():
    assert hasattr(ecoreJavascriptTest::C1, "name")
    descriptor = None
    for klass in ecoreJavascriptTest::C1.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_c2_is_not_abstract():
    assert not inspect.isabstract(C2)


def test_c2_constructor_exists():
    assert callable(C2.__init__)


def test_c2_constructor_args():
    sig = inspect.signature(C2.__init__)
    params = list(sig.parameters.keys())



def test_ecorejavascripttest::c3_is_not_abstract():
    assert not inspect.isabstract(ecoreJavascriptTest::C3)


def test_ecorejavascripttest::c3_constructor_exists():
    assert callable(ecoreJavascriptTest::C3.__init__)


def test_ecorejavascripttest::c3_constructor_args():
    sig = inspect.signature(ecoreJavascriptTest::C3.__init__)
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
ecoreJavascriptTest::C2_strategy = st.builds(
    ecoreJavascriptTest::C2,
    name=
        safe_text,
    value=
        st.integers()
)
ecoreJavascriptTest::C1_strategy = st.builds(
    ecoreJavascriptTest::C1,
    name=
        safe_text
)
C2_strategy = st.builds(
    C2,
)
ecoreJavascriptTest::C3_strategy = st.builds(
    ecoreJavascriptTest::C3,
)

@given(instance=ecoreJavascriptTest::C2_strategy)
@settings(max_examples=50)
def test_ecorejavascripttest::c2_instantiation(instance):
    assert isinstance(instance, ecoreJavascriptTest::C2)

@given(instance=ecoreJavascriptTest::C2_strategy)
def test_ecorejavascripttest::c2_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecoreJavascriptTest::C2_strategy)
def test_ecorejavascripttest::c2_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ecoreJavascriptTest::C2_strategy)
def test_ecorejavascripttest::c2_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=ecoreJavascriptTest::C2_strategy)
def test_ecorejavascripttest::c2_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=ecoreJavascriptTest::C1_strategy)
@settings(max_examples=50)
def test_ecorejavascripttest::c1_instantiation(instance):
    assert isinstance(instance, ecoreJavascriptTest::C1)

@given(instance=ecoreJavascriptTest::C1_strategy)
def test_ecorejavascripttest::c1_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=ecoreJavascriptTest::C1_strategy)
def test_ecorejavascripttest::c1_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=C2_strategy)
@settings(max_examples=50)
def test_c2_instantiation(instance):
    assert isinstance(instance, C2)

@given(instance=ecoreJavascriptTest::C3_strategy)
@settings(max_examples=50)
def test_ecorejavascripttest::c3_instantiation(instance):
    assert isinstance(instance, ecoreJavascriptTest::C3)
