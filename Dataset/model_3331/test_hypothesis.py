import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Object,
    psample::Type,
    Member,
    psample::Variable,
    psample::Function,
    Type,
    psample::PrimitiveTypeVariable,
    psample::Member,
    TypedElement,
    psample::Interface,
    psample::Class,
    psample::Object,
    psample::TypedElement,
    psample::Package,
    PrimitiveTypes,
    Visibility,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_object_is_not_abstract():
    assert not inspect.isabstract(Object)


def test_object_constructor_exists():
    assert callable(Object.__init__)


def test_object_constructor_args():
    sig = inspect.signature(Object.__init__)
    params = list(sig.parameters.keys())



def test_psample::type_is_not_abstract():
    assert not inspect.isabstract(psample::Type)


def test_psample::type_constructor_exists():
    assert callable(psample::Type.__init__)


def test_psample::type_constructor_args():
    sig = inspect.signature(psample::Type.__init__)
    params = list(sig.parameters.keys())



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_psample::variable_is_not_abstract():
    assert not inspect.isabstract(psample::Variable)


def test_psample::variable_constructor_exists():
    assert callable(psample::Variable.__init__)


def test_psample::variable_constructor_args():
    sig = inspect.signature(psample::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "isParameter" in params, "Missing parameter 'isParameter'"

def test_psample::variable_has_isParameter():
    assert hasattr(psample::Variable, "isParameter")
    descriptor = None
    for klass in psample::Variable.__mro__:
        if "isParameter" in klass.__dict__:
            descriptor = klass.__dict__["isParameter"]
            break
    assert isinstance(descriptor, property)



def test_psample::function_is_not_abstract():
    assert not inspect.isabstract(psample::Function)


def test_psample::function_constructor_exists():
    assert callable(psample::Function.__init__)


def test_psample::function_constructor_args():
    sig = inspect.signature(psample::Function.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_psample::primitivetypevariable_is_not_abstract():
    assert not inspect.isabstract(psample::PrimitiveTypeVariable)


def test_psample::primitivetypevariable_constructor_exists():
    assert callable(psample::PrimitiveTypeVariable.__init__)


def test_psample::primitivetypevariable_constructor_args():
    sig = inspect.signature(psample::PrimitiveTypeVariable.__init__)
    params = list(sig.parameters.keys())
    assert "isParameter" in params, "Missing parameter 'isParameter'"

def test_psample::primitivetypevariable_has_isParameter():
    assert hasattr(psample::PrimitiveTypeVariable, "isParameter")
    descriptor = None
    for klass in psample::PrimitiveTypeVariable.__mro__:
        if "isParameter" in klass.__dict__:
            descriptor = klass.__dict__["isParameter"]
            break
    assert isinstance(descriptor, property)



def test_psample::member_is_not_abstract():
    assert not inspect.isabstract(psample::Member)


def test_psample::member_constructor_exists():
    assert callable(psample::Member.__init__)


def test_psample::member_constructor_args():
    sig = inspect.signature(psample::Member.__init__)
    params = list(sig.parameters.keys())



def test_typedelement_is_not_abstract():
    assert not inspect.isabstract(TypedElement)


def test_typedelement_constructor_exists():
    assert callable(TypedElement.__init__)


def test_typedelement_constructor_args():
    sig = inspect.signature(TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_psample::interface_is_not_abstract():
    assert not inspect.isabstract(psample::Interface)


def test_psample::interface_constructor_exists():
    assert callable(psample::Interface.__init__)


def test_psample::interface_constructor_args():
    sig = inspect.signature(psample::Interface.__init__)
    params = list(sig.parameters.keys())



def test_psample::class_is_not_abstract():
    assert not inspect.isabstract(psample::Class)


def test_psample::class_constructor_exists():
    assert callable(psample::Class.__init__)


def test_psample::class_constructor_args():
    sig = inspect.signature(psample::Class.__init__)
    params = list(sig.parameters.keys())



def test_psample::object_is_not_abstract():
    assert not inspect.isabstract(psample::Object)


def test_psample::object_constructor_exists():
    assert callable(psample::Object.__init__)


def test_psample::object_constructor_args():
    sig = inspect.signature(psample::Object.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_psample::object_has_Name():
    assert hasattr(psample::Object, "Name")
    descriptor = None
    for klass in psample::Object.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_psample::typedelement_is_not_abstract():
    assert not inspect.isabstract(psample::TypedElement)


def test_psample::typedelement_constructor_exists():
    assert callable(psample::TypedElement.__init__)


def test_psample::typedelement_constructor_args():
    sig = inspect.signature(psample::TypedElement.__init__)
    params = list(sig.parameters.keys())



def test_psample::package_is_not_abstract():
    assert not inspect.isabstract(psample::Package)


def test_psample::package_constructor_exists():
    assert callable(psample::Package.__init__)


def test_psample::package_constructor_args():
    sig = inspect.signature(psample::Package.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_psample::package_has_Name():
    assert hasattr(psample::Package, "Name")
    descriptor = None
    for klass in psample::Package.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_primitivetypes_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypes is not None

def test_primitivetypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypes]
    expected_literals = [
        "double",
        "int",
        "string",
        "bool",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypes"

def test_visibility_exists():
    # Check that the Enumeration exists
    assert Visibility is not None

def test_visibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Visibility]
    expected_literals = [
        "private",
        "public",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Visibility"


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
Object_strategy = st.builds(
    Object,
)
psample::Type_strategy = st.builds(
    psample::Type,
)
Member_strategy = st.builds(
    Member,
)
psample::Variable_strategy = st.builds(
    psample::Variable,
    isParameter=
        st.booleans()
)
psample::Function_strategy = st.builds(
    psample::Function,
)
Type_strategy = st.builds(
    Type,
)
psample::PrimitiveTypeVariable_strategy = st.builds(
    psample::PrimitiveTypeVariable,
    isParameter=
        st.booleans()
)
psample::Member_strategy = st.builds(
    psample::Member,
)
TypedElement_strategy = st.builds(
    TypedElement,
)
psample::Interface_strategy = st.builds(
    psample::Interface,
)
psample::Class_strategy = st.builds(
    psample::Class,
)
psample::Object_strategy = st.builds(
    psample::Object,
    Name=
        safe_text
)
psample::TypedElement_strategy = st.builds(
    psample::TypedElement,
)
psample::Package_strategy = st.builds(
    psample::Package,
    Name=
        safe_text
)

@given(instance=Object_strategy)
@settings(max_examples=50)
def test_object_instantiation(instance):
    assert isinstance(instance, Object)

@given(instance=psample::Type_strategy)
@settings(max_examples=50)
def test_psample::type_instantiation(instance):
    assert isinstance(instance, psample::Type)

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=psample::Variable_strategy)
@settings(max_examples=50)
def test_psample::variable_instantiation(instance):
    assert isinstance(instance, psample::Variable)

@given(instance=psample::Variable_strategy)
def test_psample::variable_isParameter_type(instance):
    assert isinstance(instance.isParameter, bool)


@given(instance=psample::Variable_strategy)
def test_psample::variable_isParameter_setter(instance):
    original = instance.isParameter
    instance.isParameter = original
    assert instance.isParameter == original

@given(instance=psample::Function_strategy)
@settings(max_examples=50)
def test_psample::function_instantiation(instance):
    assert isinstance(instance, psample::Function)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=psample::PrimitiveTypeVariable_strategy)
@settings(max_examples=50)
def test_psample::primitivetypevariable_instantiation(instance):
    assert isinstance(instance, psample::PrimitiveTypeVariable)

@given(instance=psample::PrimitiveTypeVariable_strategy)
def test_psample::primitivetypevariable_isParameter_type(instance):
    assert isinstance(instance.isParameter, bool)


@given(instance=psample::PrimitiveTypeVariable_strategy)
def test_psample::primitivetypevariable_isParameter_setter(instance):
    original = instance.isParameter
    instance.isParameter = original
    assert instance.isParameter == original

@given(instance=psample::Member_strategy)
@settings(max_examples=50)
def test_psample::member_instantiation(instance):
    assert isinstance(instance, psample::Member)

@given(instance=TypedElement_strategy)
@settings(max_examples=50)
def test_typedelement_instantiation(instance):
    assert isinstance(instance, TypedElement)

@given(instance=psample::Interface_strategy)
@settings(max_examples=50)
def test_psample::interface_instantiation(instance):
    assert isinstance(instance, psample::Interface)

@given(instance=psample::Class_strategy)
@settings(max_examples=50)
def test_psample::class_instantiation(instance):
    assert isinstance(instance, psample::Class)

@given(instance=psample::Object_strategy)
@settings(max_examples=50)
def test_psample::object_instantiation(instance):
    assert isinstance(instance, psample::Object)

@given(instance=psample::Object_strategy)
def test_psample::object_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=psample::Object_strategy)
def test_psample::object_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=psample::TypedElement_strategy)
@settings(max_examples=50)
def test_psample::typedelement_instantiation(instance):
    assert isinstance(instance, psample::TypedElement)

@given(instance=psample::Package_strategy)
@settings(max_examples=50)
def test_psample::package_instantiation(instance):
    assert isinstance(instance, psample::Package)

@given(instance=psample::Package_strategy)
def test_psample::package_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=psample::Package_strategy)
def test_psample::package_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original
