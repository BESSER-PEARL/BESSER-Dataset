import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SElement,
    source_Y,
    source_PathElementCS,
    source_EObject,
    source_SElement,
    source_SRoot,
    source_PathNameCS,
    Y,
    source_Y2,
    source_Y1,
    source_Z,
    source_X,
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



def test_source_y_is_not_abstract():
    assert not inspect.isabstract(source_Y)


def test_source_y_constructor_exists():
    assert callable(source_Y.__init__)


def test_source_y_constructor_args():
    sig = inspect.signature(source_Y.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source_y_has_name():
    assert hasattr(source_Y, "name")
    descriptor = None
    for klass in source_Y.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source_pathelementcs_is_not_abstract():
    assert not inspect.isabstract(source_PathElementCS)


def test_source_pathelementcs_constructor_exists():
    assert callable(source_PathElementCS.__init__)


def test_source_pathelementcs_constructor_args():
    sig = inspect.signature(source_PathElementCS.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_source_pathelementcs_has_name():
    assert hasattr(source_PathElementCS, "name")
    descriptor = None
    for klass in source_PathElementCS.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_source_eobject_is_not_abstract():
    assert not inspect.isabstract(source_EObject)


def test_source_eobject_constructor_exists():
    assert callable(source_EObject.__init__)


def test_source_eobject_constructor_args():
    sig = inspect.signature(source_EObject.__init__)
    params = list(sig.parameters.keys())



def test_source_selement_is_not_abstract():
    assert not inspect.isabstract(source_SElement)


def test_source_selement_constructor_exists():
    assert callable(source_SElement.__init__)


def test_source_selement_constructor_args():
    sig = inspect.signature(source_SElement.__init__)
    params = list(sig.parameters.keys())



def test_source_sroot_is_not_abstract():
    assert not inspect.isabstract(source_SRoot)


def test_source_sroot_constructor_exists():
    assert callable(source_SRoot.__init__)


def test_source_sroot_constructor_args():
    sig = inspect.signature(source_SRoot.__init__)
    params = list(sig.parameters.keys())



def test_source_pathnamecs_is_not_abstract():
    assert not inspect.isabstract(source_PathNameCS)


def test_source_pathnamecs_constructor_exists():
    assert callable(source_PathNameCS.__init__)


def test_source_pathnamecs_constructor_args():
    sig = inspect.signature(source_PathNameCS.__init__)
    params = list(sig.parameters.keys())



def test_y_is_not_abstract():
    assert not inspect.isabstract(Y)


def test_y_constructor_exists():
    assert callable(Y.__init__)


def test_y_constructor_args():
    sig = inspect.signature(Y.__init__)
    params = list(sig.parameters.keys())



def test_source_y2_is_not_abstract():
    assert not inspect.isabstract(source_Y2)


def test_source_y2_constructor_exists():
    assert callable(source_Y2.__init__)


def test_source_y2_constructor_args():
    sig = inspect.signature(source_Y2.__init__)
    params = list(sig.parameters.keys())



def test_source_y1_is_not_abstract():
    assert not inspect.isabstract(source_Y1)


def test_source_y1_constructor_exists():
    assert callable(source_Y1.__init__)


def test_source_y1_constructor_args():
    sig = inspect.signature(source_Y1.__init__)
    params = list(sig.parameters.keys())



def test_source_z_is_not_abstract():
    assert not inspect.isabstract(source_Z)


def test_source_z_constructor_exists():
    assert callable(source_Z.__init__)


def test_source_z_constructor_args():
    sig = inspect.signature(source_Z.__init__)
    params = list(sig.parameters.keys())



def test_source_x_is_not_abstract():
    assert not inspect.isabstract(source_X)


def test_source_x_constructor_exists():
    assert callable(source_X.__init__)


def test_source_x_constructor_args():
    sig = inspect.signature(source_X.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isA2" in params, "Missing parameter 'isA2'"
    assert "isA1" in params, "Missing parameter 'isA1'"

def test_source_x_has_name():
    assert hasattr(source_X, "name")
    descriptor = None
    for klass in source_X.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_source_x_has_isA2():
    assert hasattr(source_X, "isA2")
    descriptor = None
    for klass in source_X.__mro__:
        if "isA2" in klass.__dict__:
            descriptor = klass.__dict__["isA2"]
            break
    assert isinstance(descriptor, property)

def test_source_x_has_isA1():
    assert hasattr(source_X, "isA1")
    descriptor = None
    for klass in source_X.__mro__:
        if "isA1" in klass.__dict__:
            descriptor = klass.__dict__["isA1"]
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
source_Y_strategy = st.builds(
    source_Y,
    name=
        safe_text
)
source_PathElementCS_strategy = st.builds(
    source_PathElementCS,
    name=
        safe_text
)
source_EObject_strategy = st.builds(
    source_EObject,
)
source_SElement_strategy = st.builds(
    source_SElement,
)
source_SRoot_strategy = st.builds(
    source_SRoot,
)
source_PathNameCS_strategy = st.builds(
    source_PathNameCS,
)
Y_strategy = st.builds(
    Y,
)
source_Y2_strategy = st.builds(
    source_Y2,
)
source_Y1_strategy = st.builds(
    source_Y1,
)
source_Z_strategy = st.builds(
    source_Z,
)
source_X_strategy = st.builds(
    source_X,
    name=
        safe_text,
    isA2=
        st.booleans(),
    isA1=
        st.booleans()
)

@given(instance=SElement_strategy)
@settings(max_examples=50)
def test_selement_instantiation(instance):
    assert isinstance(instance, SElement)

@given(instance=source_Y_strategy)
@settings(max_examples=50)
def test_source_y_instantiation(instance):
    assert isinstance(instance, source_Y)



@given(instance=source_Y_strategy)
def test_source_y_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source_PathElementCS_strategy)
@settings(max_examples=50)
def test_source_pathelementcs_instantiation(instance):
    assert isinstance(instance, source_PathElementCS)



@given(instance=source_PathElementCS_strategy)
def test_source_pathelementcs_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=source_EObject_strategy)
@settings(max_examples=50)
def test_source_eobject_instantiation(instance):
    assert isinstance(instance, source_EObject)

@given(instance=source_SElement_strategy)
@settings(max_examples=50)
def test_source_selement_instantiation(instance):
    assert isinstance(instance, source_SElement)

@given(instance=source_SRoot_strategy)
@settings(max_examples=50)
def test_source_sroot_instantiation(instance):
    assert isinstance(instance, source_SRoot)

@given(instance=source_PathNameCS_strategy)
@settings(max_examples=50)
def test_source_pathnamecs_instantiation(instance):
    assert isinstance(instance, source_PathNameCS)

@given(instance=Y_strategy)
@settings(max_examples=50)
def test_y_instantiation(instance):
    assert isinstance(instance, Y)

@given(instance=source_Y2_strategy)
@settings(max_examples=50)
def test_source_y2_instantiation(instance):
    assert isinstance(instance, source_Y2)

@given(instance=source_Y1_strategy)
@settings(max_examples=50)
def test_source_y1_instantiation(instance):
    assert isinstance(instance, source_Y1)

@given(instance=source_Z_strategy)
@settings(max_examples=50)
def test_source_z_instantiation(instance):
    assert isinstance(instance, source_Z)

@given(instance=source_X_strategy)
@settings(max_examples=50)
def test_source_x_instantiation(instance):
    assert isinstance(instance, source_X)



@given(instance=source_X_strategy)
def test_source_x_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=source_X_strategy)
def test_source_x_isA2_setter(instance):
    original = instance.isA2
    instance.isA2 = original
    assert instance.isA2 == original



@given(instance=source_X_strategy)
def test_source_x_isA1_setter(instance):
    original = instance.isA1
    instance.isA1 = original
    assert instance.isA1 == original
