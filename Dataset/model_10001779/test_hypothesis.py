import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class4,
    Class3,
    Class2,
    c1,
    c,
    Class,
    Teacher,
    Room,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class4_is_not_abstract():
    assert not inspect.isabstract(Class4)


def test_class4_constructor_exists():
    assert callable(Class4.__init__)


def test_class4_constructor_args():
    sig = inspect.signature(Class4.__init__)
    params = list(sig.parameters.keys())



def test_class3_is_not_abstract():
    assert not inspect.isabstract(Class3)


def test_class3_constructor_exists():
    assert callable(Class3.__init__)


def test_class3_constructor_args():
    sig = inspect.signature(Class3.__init__)
    params = list(sig.parameters.keys())



def test_class2_is_not_abstract():
    assert not inspect.isabstract(Class2)


def test_class2_constructor_exists():
    assert callable(Class2.__init__)


def test_class2_constructor_args():
    sig = inspect.signature(Class2.__init__)
    params = list(sig.parameters.keys())



def test_c1_is_not_abstract():
    assert not inspect.isabstract(c1)


def test_c1_constructor_exists():
    assert callable(c1.__init__)


def test_c1_constructor_args():
    sig = inspect.signature(c1.__init__)
    params = list(sig.parameters.keys())



def test_c_is_not_abstract():
    assert not inspect.isabstract(c)


def test_c_constructor_exists():
    assert callable(c.__init__)


def test_c_constructor_args():
    sig = inspect.signature(c.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_teacher_is_not_abstract():
    assert not inspect.isabstract(Teacher)


def test_teacher_constructor_exists():
    assert callable(Teacher.__init__)


def test_teacher_constructor_args():
    sig = inspect.signature(Teacher.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_teacher_has_Name():
    assert hasattr(Teacher, "Name")
    descriptor = None
    for klass in Teacher.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_room_has_Name():
    assert hasattr(Room, "Name")
    descriptor = None
    for klass in Room.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
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
Class4_strategy = st.builds(
    Class4,
)
Class3_strategy = st.builds(
    Class3,
)
Class2_strategy = st.builds(
    Class2,
)
c1_strategy = st.builds(
    c1,
)
c_strategy = st.builds(
    c,
)
Class_strategy = st.builds(
    Class,
)
Teacher_strategy = st.builds(
    Teacher,
    Name=
        safe_text
)
Room_strategy = st.builds(
    Room,
    Name=
        safe_text
)

@given(instance=Class4_strategy)
@settings(max_examples=50)
def test_class4_instantiation(instance):
    assert isinstance(instance, Class4)

@given(instance=Class3_strategy)
@settings(max_examples=50)
def test_class3_instantiation(instance):
    assert isinstance(instance, Class3)

@given(instance=Class2_strategy)
@settings(max_examples=50)
def test_class2_instantiation(instance):
    assert isinstance(instance, Class2)

@given(instance=c1_strategy)
@settings(max_examples=50)
def test_c1_instantiation(instance):
    assert isinstance(instance, c1)

@given(instance=c_strategy)
@settings(max_examples=50)
def test_c_instantiation(instance):
    assert isinstance(instance, c)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Teacher_strategy)
@settings(max_examples=50)
def test_teacher_instantiation(instance):
    assert isinstance(instance, Teacher)



@given(instance=Teacher_strategy)
def test_teacher_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)



@given(instance=Room_strategy)
def test_room_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
