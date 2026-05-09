import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SElement,
    source::Y,
    source::PathElementCS,
    source::EObject,
    source::SElement,
    source::SRoot,
    source::PathNameCS,
    Y,
    source::Y2,
    source::Y1,
    source::Z,
    source::X,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_selement_is_not_abstract():
    assert not inspect.isabstract(SElement)


def test_selement_constructor_exists():
    assert callable(SElement.__init__)


def test_selement_constructor_args():
    sig = inspect.signature(SElement.__init__)
    params = list(sig.parameters.keys())



def test_source::y_is_not_abstract():
    assert not inspect.isabstract(source::Y)


def test_source::y_constructor_exists():
    assert callable(source::Y.__init__)


def test_source::y_constructor_args():
    sig = inspect.signature(source::Y.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source::y_has_name():
    assert hasattr(source::Y, "name")
    descriptor = None
    for klass in source::Y.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source::pathelementcs_is_not_abstract():
    assert not inspect.isabstract(source::PathElementCS)


def test_source::pathelementcs_constructor_exists():
    assert callable(source::PathElementCS.__init__)


def test_source::pathelementcs_constructor_args():
    sig = inspect.signature(source::PathElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source::pathelementcs_has_name():
    assert hasattr(source::PathElementCS, "name")
    descriptor = None
    for klass in source::PathElementCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source::eobject_is_not_abstract():
    assert not inspect.isabstract(source::EObject)


def test_source::eobject_constructor_exists():
    assert callable(source::EObject.__init__)


def test_source::eobject_constructor_args():
    sig = inspect.signature(source::EObject.__init__)
    params = list(sig.parameters.keys())



def test_source::selement_is_not_abstract():
    assert not inspect.isabstract(source::SElement)


def test_source::selement_constructor_exists():
    assert callable(source::SElement.__init__)


def test_source::selement_constructor_args():
    sig = inspect.signature(source::SElement.__init__)
    params = list(sig.parameters.keys())



def test_source::sroot_is_not_abstract():
    assert not inspect.isabstract(source::SRoot)


def test_source::sroot_constructor_exists():
    assert callable(source::SRoot.__init__)


def test_source::sroot_constructor_args():
    sig = inspect.signature(source::SRoot.__init__)
    params = list(sig.parameters.keys())



def test_source::pathnamecs_is_not_abstract():
    assert not inspect.isabstract(source::PathNameCS)


def test_source::pathnamecs_constructor_exists():
    assert callable(source::PathNameCS.__init__)


def test_source::pathnamecs_constructor_args():
    sig = inspect.signature(source::PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())



def test_source::y2_is_not_abstract():
    assert not inspect.isabstract(source::Y2)


def test_source::y2_constructor_exists():
    assert callable(source::Y2.__init__)


def test_source::y2_constructor_args():
    sig = inspect.signature(source::Y2.__init__)
    params = list(sig.parameters.keys())



def test_source::y1_is_not_abstract():
    assert not inspect.isabstract(source::Y1)


def test_source::y1_constructor_exists():
    assert callable(source::Y1.__init__)


def test_source::y1_constructor_args():
    sig = inspect.signature(source::Y1.__init__)
    params = list(sig.parameters.keys())



def test_source::z_is_not_abstract():
    assert not inspect.isabstract(source::Z)


def test_source::z_constructor_exists():
    assert callable(source::Z.__init__)


def test_source::z_constructor_args():
    sig = inspect.signature(source::Z.__init__)
    params = list(sig.parameters.keys())



def test_source::x_is_not_abstract():
    assert not inspect.isabstract(source::X)


def test_source::x_constructor_exists():
    assert callable(source::X.__init__)


def test_source::x_constructor_args():
    sig = inspect.signature(source::X.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isA1" in params, "Missing parameter 'isA1'"
    assert "isA2" in params, "Missing parameter 'isA2'"

def test_source::x_has_name():
    assert hasattr(source::X, "name")
    descriptor = None
    for klass in source::X.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_source::x_has_isA1():
    assert hasattr(source::X, "isA1")
    descriptor = None
    for klass in source::X.__mro__:
        if "isA1" in klass.__dict__:
            descriptor = klass.__dict__["isA1"]
            break
    assert isinstance(descriptor, property)

def test_source::x_has_isA2():
    assert hasattr(source::X, "isA2")
    descriptor = None
    for klass in source::X.__mro__:
        if "isA2" in klass.__dict__:
            descriptor = klass.__dict__["isA2"]
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
SElement_strategy = st.builds(
    SElement,
)
source::Y_strategy = st.builds(
    source::Y,
    name=
        safe_text
)
source::PathElementCS_strategy = st.builds(
    source::PathElementCS,
    name=
        safe_text
)
source::EObject_strategy = st.builds(
    source::EObject,
)
source::SElement_strategy = st.builds(
    source::SElement,
)
source::SRoot_strategy = st.builds(
    source::SRoot,
)
source::PathNameCS_strategy = st.builds(
    source::PathNameCS,
)
Y_strategy = st.builds(
    Y,
)
source::Y2_strategy = st.builds(
    source::Y2,
)
source::Y1_strategy = st.builds(
    source::Y1,
)
source::Z_strategy = st.builds(
    source::Z,
)
source::X_strategy = st.builds(
    source::X,
    name=
        safe_text,
    isA1=
        st.booleans(),
    isA2=
        st.booleans()
)

@given(instance=SElement_strategy)
@settings(max_examples=50)
def test_selement_instantiation(instance):
    assert isinstance(instance, SElement)

@given(instance=source::Y_strategy)
@settings(max_examples=50)
def test_source::y_instantiation(instance):
    assert isinstance(instance, source::Y)

@given(instance=source::Y_strategy)
def test_source::y_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=source::Y_strategy)
def test_source::y_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source::PathElementCS_strategy)
@settings(max_examples=50)
def test_source::pathelementcs_instantiation(instance):
    assert isinstance(instance, source::PathElementCS)

@given(instance=source::PathElementCS_strategy)
def test_source::pathelementcs_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=source::PathElementCS_strategy)
def test_source::pathelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source::EObject_strategy)
@settings(max_examples=50)
def test_source::eobject_instantiation(instance):
    assert isinstance(instance, source::EObject)

@given(instance=source::SElement_strategy)
@settings(max_examples=50)
def test_source::selement_instantiation(instance):
    assert isinstance(instance, source::SElement)

@given(instance=source::SRoot_strategy)
@settings(max_examples=50)
def test_source::sroot_instantiation(instance):
    assert isinstance(instance, source::SRoot)

@given(instance=source::PathNameCS_strategy)
@settings(max_examples=50)
def test_source::pathnamecs_instantiation(instance):
    assert isinstance(instance, source::PathNameCS)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)

@given(instance=source::Y2_strategy)
@settings(max_examples=50)
def test_source::y2_instantiation(instance):
    assert isinstance(instance, source::Y2)

@given(instance=source::Y1_strategy)
@settings(max_examples=50)
def test_source::y1_instantiation(instance):
    assert isinstance(instance, source::Y1)

@given(instance=source::Z_strategy)
@settings(max_examples=50)
def test_source::z_instantiation(instance):
    assert isinstance(instance, source::Z)

@given(instance=source::X_strategy)
@settings(max_examples=50)
def test_source::x_instantiation(instance):
    assert isinstance(instance, source::X)

@given(instance=source::X_strategy)
def test_source::x_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=source::X_strategy)
def test_source::x_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source::X_strategy)
def test_source::x_isA1_type(instance):
    assert isinstance(instance.isA1, bool)


@given(instance=source::X_strategy)
def test_source::x_isA1_setter(instance):
    original = instance.isA1
    instance.isA1 = original
    assert instance.isA1 == original

@given(instance=source::X_strategy)
def test_source::x_isA2_type(instance):
    assert isinstance(instance.isA2, bool)


@given(instance=source::X_strategy)
def test_source::x_isA2_setter(instance):
    original = instance.isA2
    instance.isA2 = original
    assert instance.isA2 == original
