import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Triangles_AbstractClass,
    AbstractClass,
    Triangles_C_Class,
    Triangles_B_Class,
    Triangles_E_Class,
    Triangles_D_Class,
    Triangles_A_Class,
    Triangles_Container,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_triangles_abstractclass_is_not_abstract():
    assert not inspect.isabstract(Triangles_AbstractClass)


def test_triangles_abstractclass_constructor_exists():
    assert callable(Triangles_AbstractClass.__init__)


def test_triangles_abstractclass_constructor_args():
    sig = inspect.signature(Triangles_AbstractClass.__init__)
    params = list(sig.parameters.keys())
    assert "flag" in params, "Missing parameter 'flag'"
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_triangles_abstractclass_has_flag():
    assert hasattr(Triangles_AbstractClass, "flag")
    descriptor = None
    for klass in Triangles_AbstractClass.__mro__:
        if "flag" in klass.__dict__:
            descriptor = klass.__dict__["flag"]
            break
    assert isinstance(descriptor, property)

def test_triangles_abstractclass_has_name():
    assert hasattr(Triangles_AbstractClass, "name")
    descriptor = None
    for klass in Triangles_AbstractClass.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_triangles_abstractclass_has_id():
    assert hasattr(Triangles_AbstractClass, "id")
    descriptor = None
    for klass in Triangles_AbstractClass.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_abstractclass_is_not_abstract():
    assert not inspect.isabstract(AbstractClass)


def test_abstractclass_constructor_exists():
    assert callable(AbstractClass.__init__)


def test_abstractclass_constructor_args():
    sig = inspect.signature(AbstractClass.__init__)
    params = list(sig.parameters.keys())



def test_triangles_c_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_C_Class)


def test_triangles_c_class_constructor_exists():
    assert callable(Triangles_C_Class.__init__)


def test_triangles_c_class_constructor_args():
    sig = inspect.signature(Triangles_C_Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles_b_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_B_Class)


def test_triangles_b_class_constructor_exists():
    assert callable(Triangles_B_Class.__init__)


def test_triangles_b_class_constructor_args():
    sig = inspect.signature(Triangles_B_Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles_e_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_E_Class)


def test_triangles_e_class_constructor_exists():
    assert callable(Triangles_E_Class.__init__)


def test_triangles_e_class_constructor_args():
    sig = inspect.signature(Triangles_E_Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles_d_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_D_Class)


def test_triangles_d_class_constructor_exists():
    assert callable(Triangles_D_Class.__init__)


def test_triangles_d_class_constructor_args():
    sig = inspect.signature(Triangles_D_Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles_a_class_is_not_abstract():
    assert not inspect.isabstract(Triangles_A_Class)


def test_triangles_a_class_constructor_exists():
    assert callable(Triangles_A_Class.__init__)


def test_triangles_a_class_constructor_args():
    sig = inspect.signature(Triangles_A_Class.__init__)
    params = list(sig.parameters.keys())



def test_triangles_container_is_not_abstract():
    assert not inspect.isabstract(Triangles_Container)


def test_triangles_container_constructor_exists():
    assert callable(Triangles_Container.__init__)


def test_triangles_container_constructor_args():
    sig = inspect.signature(Triangles_Container.__init__)
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
Triangles_AbstractClass_strategy = st.builds(
    Triangles_AbstractClass,
    flag=
        st.booleans(),
    name=
        safe_text,
    id=
        st.integers()
)
AbstractClass_strategy = st.builds(
    AbstractClass,
)
Triangles_C_Class_strategy = st.builds(
    Triangles_C_Class,
)
Triangles_B_Class_strategy = st.builds(
    Triangles_B_Class,
)
Triangles_E_Class_strategy = st.builds(
    Triangles_E_Class,
)
Triangles_D_Class_strategy = st.builds(
    Triangles_D_Class,
)
Triangles_A_Class_strategy = st.builds(
    Triangles_A_Class,
)
Triangles_Container_strategy = st.builds(
    Triangles_Container,
)

@given(instance=Triangles_AbstractClass_strategy)
@settings(max_examples=50)
def test_triangles_abstractclass_instantiation(instance):
    assert isinstance(instance, Triangles_AbstractClass)



@given(instance=Triangles_AbstractClass_strategy)
def test_triangles_abstractclass_flag_setter(instance):
    original = instance.flag
    instance.flag = original
    assert instance.flag == original



@given(instance=Triangles_AbstractClass_strategy)
def test_triangles_abstractclass_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Triangles_AbstractClass_strategy)
def test_triangles_abstractclass_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=AbstractClass_strategy)
@settings(max_examples=50)
def test_abstractclass_instantiation(instance):
    assert isinstance(instance, AbstractClass)

@given(instance=Triangles_C_Class_strategy)
@settings(max_examples=50)
def test_triangles_c_class_instantiation(instance):
    assert isinstance(instance, Triangles_C_Class)

@given(instance=Triangles_B_Class_strategy)
@settings(max_examples=50)
def test_triangles_b_class_instantiation(instance):
    assert isinstance(instance, Triangles_B_Class)

@given(instance=Triangles_E_Class_strategy)
@settings(max_examples=50)
def test_triangles_e_class_instantiation(instance):
    assert isinstance(instance, Triangles_E_Class)

@given(instance=Triangles_D_Class_strategy)
@settings(max_examples=50)
def test_triangles_d_class_instantiation(instance):
    assert isinstance(instance, Triangles_D_Class)

@given(instance=Triangles_A_Class_strategy)
@settings(max_examples=50)
def test_triangles_a_class_instantiation(instance):
    assert isinstance(instance, Triangles_A_Class)

@given(instance=Triangles_Container_strategy)
@settings(max_examples=50)
def test_triangles_container_instantiation(instance):
    assert isinstance(instance, Triangles_Container)
