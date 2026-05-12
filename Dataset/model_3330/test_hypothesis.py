import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    TypedElement,
    psample_Class,
    psample_Object,
    Object,
    psample_TypedElement,
    psample_Type,
    Member,
    psample_Variable,
    psample_Function,
    psample_Interface,
    Type,
    psample_PrimitiveTypeVariable,
    psample_Member,
    psample_Package,
    Visibility,
    PrimitiveTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_psample_class_is_not_abstract():
    assert not inspect.isabstract(psample_Class)


def test_psample_class_constructor_exists():
    assert callable(psample_Class.__init__)


def test_psample_class_constructor_args():
    sig = inspect.signature(psample_Class.__init__)
    params = list(sig.parameters.keys())



def test_psample_object_is_not_abstract():
    assert not inspect.isabstract(psample_Object)


def test_psample_object_constructor_exists():
    assert callable(psample_Object.__init__)


def test_psample_object_constructor_args():
    sig = inspect.signature(psample_Object.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_psample_object_has_Name():
    assert hasattr(psample_Object, "Name")
    descriptor = None
    for klass in psample_Object.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_psample_typedelement_is_not_abstract():
    assert not inspect.isabstract(psample_TypedElement)


def test_psample_typedelement_constructor_exists():
    assert callable(psample_TypedElement.__init__)


def test_psample_typedelement_constructor_args():
    sig = inspect.signature(psample_TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_psample_type_is_not_abstract():
    assert not inspect.isabstract(psample_Type)


def test_psample_type_constructor_exists():
    assert callable(psample_Type.__init__)


def test_psample_type_constructor_args():
    sig = inspect.signature(psample_Type.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_psample_variable_is_not_abstract():
    assert not inspect.isabstract(psample_Variable)


def test_psample_variable_constructor_exists():
    assert callable(psample_Variable.__init__)


def test_psample_variable_constructor_args():
    sig = inspect.signature(psample_Variable.__init__)
    params = list(sig.parameters.keys())



def test_psample_function_is_not_abstract():
    assert not inspect.isabstract(psample_Function)


def test_psample_function_constructor_exists():
    assert callable(psample_Function.__init__)


def test_psample_function_constructor_args():
    sig = inspect.signature(psample_Function.__init__)
    params = list(sig.parameters.keys())



def test_psample_interface_is_not_abstract():
    assert not inspect.isabstract(psample_Interface)


def test_psample_interface_constructor_exists():
    assert callable(psample_Interface.__init__)


def test_psample_interface_constructor_args():
    sig = inspect.signature(psample_Interface.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_psample_primitivetypevariable_is_not_abstract():
    assert not inspect.isabstract(psample_PrimitiveTypeVariable)


def test_psample_primitivetypevariable_constructor_exists():
    assert callable(psample_PrimitiveTypeVariable.__init__)


def test_psample_primitivetypevariable_constructor_args():
    sig = inspect.signature(psample_PrimitiveTypeVariable.__init__)
    params = list(sig.parameters.keys())



def test_psample_member_is_not_abstract():
    assert not inspect.isabstract(psample_Member)


def test_psample_member_constructor_exists():
    assert callable(psample_Member.__init__)


def test_psample_member_constructor_args():
    sig = inspect.signature(psample_Member.__init__)
    params = list(sig.parameters.keys())



def test_psample_package_is_not_abstract():
    assert not inspect.isabstract(psample_Package)


def test_psample_package_constructor_exists():
    assert callable(psample_Package.__init__)


def test_psample_package_constructor_args():
    sig = inspect.signature(psample_Package.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_psample_package_has_Name():
    assert hasattr(psample_Package, "Name")
    descriptor = None
    for klass in psample_Package.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "protected",
        "public",
        "private",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"

def test_primitivetypes_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypes is not None

def test_primitivetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypes]
    expected_literals = [
        "string",
        "int",
        "double",
        "bool",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypes"


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
TypedElement_strategy = st.builds(
    TypedElement,
)
psample_Class_strategy = st.builds(
    psample_Class,
)
psample_Object_strategy = st.builds(
    psample_Object,
    Name=
        safe_text
)
Object_strategy = st.builds(
    Object,
)
psample_TypedElement_strategy = st.builds(
    psample_TypedElement,
)
psample_Type_strategy = st.builds(
    psample_Type,
)
Member_strategy = st.builds(
    Member,
)
psample_Variable_strategy = st.builds(
    psample_Variable,
)
psample_Function_strategy = st.builds(
    psample_Function,
)
psample_Interface_strategy = st.builds(
    psample_Interface,
)
Type_strategy = st.builds(
    Type,
)
psample_PrimitiveTypeVariable_strategy = st.builds(
    psample_PrimitiveTypeVariable,
)
psample_Member_strategy = st.builds(
    psample_Member,
)
psample_Package_strategy = st.builds(
    psample_Package,
    Name=
        safe_text
)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=psample_Class_strategy)
@settings(max_examples=50)
def test_psample_class_instantiation(instance):
    assert isinstance(instance, psample_Class)

@given(instance=psample_Object_strategy)
@settings(max_examples=50)
def test_psample_object_instantiation(instance):
    assert isinstance(instance, psample_Object)



@given(instance=psample_Object_strategy)
def test_psample_object_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=psample_TypedElement_strategy)
@settings(max_examples=50)
def test_psample_typedelement_instantiation(instance):
    assert isinstance(instance, psample_TypedElement)

@given(instance=psample_Type_strategy)
@settings(max_examples=50)
def test_psample_type_instantiation(instance):
    assert isinstance(instance, psample_Type)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=psample_Variable_strategy)
@settings(max_examples=50)
def test_psample_variable_instantiation(instance):
    assert isinstance(instance, psample_Variable)

@given(instance=psample_Function_strategy)
@settings(max_examples=50)
def test_psample_function_instantiation(instance):
    assert isinstance(instance, psample_Function)

@given(instance=psample_Interface_strategy)
@settings(max_examples=50)
def test_psample_interface_instantiation(instance):
    assert isinstance(instance, psample_Interface)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=psample_PrimitiveTypeVariable_strategy)
@settings(max_examples=50)
def test_psample_primitivetypevariable_instantiation(instance):
    assert isinstance(instance, psample_PrimitiveTypeVariable)

@given(instance=psample_Member_strategy)
@settings(max_examples=50)
def test_psample_member_instantiation(instance):
    assert isinstance(instance, psample_Member)

@given(instance=psample_Package_strategy)
@settings(max_examples=50)
def test_psample_package_instantiation(instance):
    assert isinstance(instance, psample_Package)



@given(instance=psample_Package_strategy)
def test_psample_package_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
