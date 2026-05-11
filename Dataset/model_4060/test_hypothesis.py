import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NamedElement,
    myumlclassdiagram::Package,
    myumlclassdiagram::Parameter,
    myumlclassdiagram::NamedElement,
    myumlclassdiagram::Method,
    myumlclassdiagram::Attribute,
    myumlclassdiagram::Class,
    EVisibility,
    EReturnType,
    EType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_myumlclassdiagram::package_is_not_abstract():
    assert not inspect.isabstract(myumlclassdiagram::Package)


def test_myumlclassdiagram::package_constructor_exists():
    assert callable(myumlclassdiagram::Package.__init__)


def test_myumlclassdiagram::package_constructor_args():
    sig = inspect.signature(myumlclassdiagram::Package.__init__)
    params = list(sig.parameters.keys())



def test_myumlclassdiagram::parameter_is_not_abstract():
    assert not inspect.isabstract(myumlclassdiagram::Parameter)


def test_myumlclassdiagram::parameter_constructor_exists():
    assert callable(myumlclassdiagram::Parameter.__init__)


def test_myumlclassdiagram::parameter_constructor_args():
    sig = inspect.signature(myumlclassdiagram::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"

def test_myumlclassdiagram::parameter_has_Type():
    assert hasattr(myumlclassdiagram::Parameter, "Type")
    descriptor = None
    for klass in myumlclassdiagram::Parameter.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_myumlclassdiagram::namedelement_is_not_abstract():
    assert not inspect.isabstract(myumlclassdiagram::NamedElement)


def test_myumlclassdiagram::namedelement_constructor_exists():
    assert callable(myumlclassdiagram::NamedElement.__init__)


def test_myumlclassdiagram::namedelement_constructor_args():
    sig = inspect.signature(myumlclassdiagram::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_myumlclassdiagram::namedelement_has_Name():
    assert hasattr(myumlclassdiagram::NamedElement, "Name")
    descriptor = None
    for klass in myumlclassdiagram::NamedElement.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_myumlclassdiagram::method_is_not_abstract():
    assert not inspect.isabstract(myumlclassdiagram::Method)


def test_myumlclassdiagram::method_constructor_exists():
    assert callable(myumlclassdiagram::Method.__init__)


def test_myumlclassdiagram::method_constructor_args():
    sig = inspect.signature(myumlclassdiagram::Method.__init__)
    params = list(sig.parameters.keys())
    assert "Visibility" in params, "Missing parameter 'Visibility'"
    assert "Returns" in params, "Missing parameter 'Returns'"

def test_myumlclassdiagram::method_has_Visibility():
    assert hasattr(myumlclassdiagram::Method, "Visibility")
    descriptor = None
    for klass in myumlclassdiagram::Method.__mro__:
        if "Visibility" in klass.__dict__:
            descriptor = klass.__dict__["Visibility"]
            break
    assert isinstance(descriptor, property)

def test_myumlclassdiagram::method_has_Returns():
    assert hasattr(myumlclassdiagram::Method, "Returns")
    descriptor = None
    for klass in myumlclassdiagram::Method.__mro__:
        if "Returns" in klass.__dict__:
            descriptor = klass.__dict__["Returns"]
            break
    assert isinstance(descriptor, property)



def test_myumlclassdiagram::attribute_is_not_abstract():
    assert not inspect.isabstract(myumlclassdiagram::Attribute)


def test_myumlclassdiagram::attribute_constructor_exists():
    assert callable(myumlclassdiagram::Attribute.__init__)


def test_myumlclassdiagram::attribute_constructor_args():
    sig = inspect.signature(myumlclassdiagram::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Visibility" in params, "Missing parameter 'Visibility'"

def test_myumlclassdiagram::attribute_has_Type():
    assert hasattr(myumlclassdiagram::Attribute, "Type")
    descriptor = None
    for klass in myumlclassdiagram::Attribute.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_myumlclassdiagram::attribute_has_Visibility():
    assert hasattr(myumlclassdiagram::Attribute, "Visibility")
    descriptor = None
    for klass in myumlclassdiagram::Attribute.__mro__:
        if "Visibility" in klass.__dict__:
            descriptor = klass.__dict__["Visibility"]
            break
    assert isinstance(descriptor, property)



def test_myumlclassdiagram::class_is_not_abstract():
    assert not inspect.isabstract(myumlclassdiagram::Class)


def test_myumlclassdiagram::class_constructor_exists():
    assert callable(myumlclassdiagram::Class.__init__)


def test_myumlclassdiagram::class_constructor_args():
    sig = inspect.signature(myumlclassdiagram::Class.__init__)
    params = list(sig.parameters.keys())
    assert "Visibility" in params, "Missing parameter 'Visibility'"

def test_myumlclassdiagram::class_has_Visibility():
    assert hasattr(myumlclassdiagram::Class, "Visibility")
    descriptor = None
    for klass in myumlclassdiagram::Class.__mro__:
        if "Visibility" in klass.__dict__:
            descriptor = klass.__dict__["Visibility"]
            break
    assert isinstance(descriptor, property)

def test_evisibility_exists():
    # Check that the Enumeration exists
    assert EVisibility is not None

def test_evisibility_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EVisibility]
    expected_literals = [
        "protected",
        "private",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EVisibility"

def test_ereturntype_exists():
    # Check that the Enumeration exists
    assert EReturnType is not None

def test_ereturntype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EReturnType]
    expected_literals = [
        "string",
        "void",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EReturnType"

def test_etype_exists():
    # Check that the Enumeration exists
    assert EType is not None

def test_etype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EType]
    expected_literals = [
        "string",
        "integer",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EType"


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
NamedElement_strategy = st.builds(
    NamedElement,
)
myumlclassdiagram::Package_strategy = st.builds(
    myumlclassdiagram::Package,
)
myumlclassdiagram::Parameter_strategy = st.builds(
    myumlclassdiagram::Parameter,
    Type=
        safe_text
)
myumlclassdiagram::NamedElement_strategy = st.builds(
    myumlclassdiagram::NamedElement,
    Name=
        safe_text
)
myumlclassdiagram::Method_strategy = st.builds(
    myumlclassdiagram::Method,
    Visibility=
        safe_text,
    Returns=
        safe_text
)
myumlclassdiagram::Attribute_strategy = st.builds(
    myumlclassdiagram::Attribute,
    Type=
        safe_text,
    Visibility=
        safe_text
)
myumlclassdiagram::Class_strategy = st.builds(
    myumlclassdiagram::Class,
    Visibility=
        safe_text
)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=myumlclassdiagram::Package_strategy)
@settings(max_examples=50)
def test_myumlclassdiagram::package_instantiation(instance):
    assert isinstance(instance, myumlclassdiagram::Package)

@given(instance=myumlclassdiagram::Parameter_strategy)
@settings(max_examples=50)
def test_myumlclassdiagram::parameter_instantiation(instance):
    assert isinstance(instance, myumlclassdiagram::Parameter)

@given(instance=myumlclassdiagram::Parameter_strategy)
def test_myumlclassdiagram::parameter_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=myumlclassdiagram::Parameter_strategy)
def test_myumlclassdiagram::parameter_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=myumlclassdiagram::NamedElement_strategy)
@settings(max_examples=50)
def test_myumlclassdiagram::namedelement_instantiation(instance):
    assert isinstance(instance, myumlclassdiagram::NamedElement)

@given(instance=myumlclassdiagram::NamedElement_strategy)
def test_myumlclassdiagram::namedelement_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=myumlclassdiagram::NamedElement_strategy)
def test_myumlclassdiagram::namedelement_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=myumlclassdiagram::Method_strategy)
@settings(max_examples=50)
def test_myumlclassdiagram::method_instantiation(instance):
    assert isinstance(instance, myumlclassdiagram::Method)

@given(instance=myumlclassdiagram::Method_strategy)
def test_myumlclassdiagram::method_Visibility_type(instance):
    assert isinstance(instance.Visibility, str)


@given(instance=myumlclassdiagram::Method_strategy)
def test_myumlclassdiagram::method_Visibility_setter(instance):
    original = instance.Visibility
    instance.Visibility = original
    assert instance.Visibility == original

@given(instance=myumlclassdiagram::Method_strategy)
def test_myumlclassdiagram::method_Returns_type(instance):
    assert isinstance(instance.Returns, str)


@given(instance=myumlclassdiagram::Method_strategy)
def test_myumlclassdiagram::method_Returns_setter(instance):
    original = instance.Returns
    instance.Returns = original
    assert instance.Returns == original

@given(instance=myumlclassdiagram::Attribute_strategy)
@settings(max_examples=50)
def test_myumlclassdiagram::attribute_instantiation(instance):
    assert isinstance(instance, myumlclassdiagram::Attribute)

@given(instance=myumlclassdiagram::Attribute_strategy)
def test_myumlclassdiagram::attribute_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=myumlclassdiagram::Attribute_strategy)
def test_myumlclassdiagram::attribute_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=myumlclassdiagram::Attribute_strategy)
def test_myumlclassdiagram::attribute_Visibility_type(instance):
    assert isinstance(instance.Visibility, str)


@given(instance=myumlclassdiagram::Attribute_strategy)
def test_myumlclassdiagram::attribute_Visibility_setter(instance):
    original = instance.Visibility
    instance.Visibility = original
    assert instance.Visibility == original

@given(instance=myumlclassdiagram::Class_strategy)
@settings(max_examples=50)
def test_myumlclassdiagram::class_instantiation(instance):
    assert isinstance(instance, myumlclassdiagram::Class)

@given(instance=myumlclassdiagram::Class_strategy)
def test_myumlclassdiagram::class_Visibility_type(instance):
    assert isinstance(instance.Visibility, str)


@given(instance=myumlclassdiagram::Class_strategy)
def test_myumlclassdiagram::class_Visibility_setter(instance):
    original = instance.Visibility
    instance.Visibility = original
    assert instance.Visibility == original
