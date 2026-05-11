import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    smalluml::Diagram,
    smalluml::NamedElement,
    Type,
    smalluml::Int,
    smalluml::Boolean,
    smalluml::String,
    smalluml::Float,
    NamedElement,
    smalluml::Type,
    smalluml::Association,
    smalluml::Method,
    smalluml::Class,
    smalluml::Heritage,
    smalluml::Role,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smalluml::diagram_is_not_abstract():
    assert not inspect.isabstract(smalluml::Diagram)


def test_smalluml::diagram_constructor_exists():
    assert callable(smalluml::Diagram.__init__)


def test_smalluml::diagram_constructor_args():
    sig = inspect.signature(smalluml::Diagram.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::namedelement_is_not_abstract():
    assert not inspect.isabstract(smalluml::NamedElement)


def test_smalluml::namedelement_constructor_exists():
    assert callable(smalluml::NamedElement.__init__)


def test_smalluml::namedelement_constructor_args():
    sig = inspect.signature(smalluml::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml::namedelement_has_name():
    assert hasattr(smalluml::NamedElement, "name")
    descriptor = None
    for klass in smalluml::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::int_is_not_abstract():
    assert not inspect.isabstract(smalluml::Int)


def test_smalluml::int_constructor_exists():
    assert callable(smalluml::Int.__init__)


def test_smalluml::int_constructor_args():
    sig = inspect.signature(smalluml::Int.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::boolean_is_not_abstract():
    assert not inspect.isabstract(smalluml::Boolean)


def test_smalluml::boolean_constructor_exists():
    assert callable(smalluml::Boolean.__init__)


def test_smalluml::boolean_constructor_args():
    sig = inspect.signature(smalluml::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::string_is_not_abstract():
    assert not inspect.isabstract(smalluml::String)


def test_smalluml::string_constructor_exists():
    assert callable(smalluml::String.__init__)


def test_smalluml::string_constructor_args():
    sig = inspect.signature(smalluml::String.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::float_is_not_abstract():
    assert not inspect.isabstract(smalluml::Float)


def test_smalluml::float_constructor_exists():
    assert callable(smalluml::Float.__init__)


def test_smalluml::float_constructor_args():
    sig = inspect.signature(smalluml::Float.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::type_is_not_abstract():
    assert not inspect.isabstract(smalluml::Type)


def test_smalluml::type_constructor_exists():
    assert callable(smalluml::Type.__init__)


def test_smalluml::type_constructor_args():
    sig = inspect.signature(smalluml::Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::association_is_not_abstract():
    assert not inspect.isabstract(smalluml::Association)


def test_smalluml::association_constructor_exists():
    assert callable(smalluml::Association.__init__)


def test_smalluml::association_constructor_args():
    sig = inspect.signature(smalluml::Association.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::method_is_not_abstract():
    assert not inspect.isabstract(smalluml::Method)


def test_smalluml::method_constructor_exists():
    assert callable(smalluml::Method.__init__)


def test_smalluml::method_constructor_args():
    sig = inspect.signature(smalluml::Method.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::class_is_not_abstract():
    assert not inspect.isabstract(smalluml::Class)


def test_smalluml::class_constructor_exists():
    assert callable(smalluml::Class.__init__)


def test_smalluml::class_constructor_args():
    sig = inspect.signature(smalluml::Class.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::heritage_is_not_abstract():
    assert not inspect.isabstract(smalluml::Heritage)


def test_smalluml::heritage_constructor_exists():
    assert callable(smalluml::Heritage.__init__)


def test_smalluml::heritage_constructor_args():
    sig = inspect.signature(smalluml::Heritage.__init__)
    params = list(sig.parameters.keys())



def test_smalluml::role_is_not_abstract():
    assert not inspect.isabstract(smalluml::Role)


def test_smalluml::role_constructor_exists():
    assert callable(smalluml::Role.__init__)


def test_smalluml::role_constructor_args():
    sig = inspect.signature(smalluml::Role.__init__)
    params = list(sig.parameters.keys())
    assert "lower" in params, "Missing parameter 'lower'"
    assert "upper" in params, "Missing parameter 'upper'"

def test_smalluml::role_has_lower():
    assert hasattr(smalluml::Role, "lower")
    descriptor = None
    for klass in smalluml::Role.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
            break
    assert isinstance(descriptor, property)

def test_smalluml::role_has_upper():
    assert hasattr(smalluml::Role, "upper")
    descriptor = None
    for klass in smalluml::Role.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
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
smalluml::Diagram_strategy = st.builds(
    smalluml::Diagram,
)
smalluml::NamedElement_strategy = st.builds(
    smalluml::NamedElement,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
smalluml::Int_strategy = st.builds(
    smalluml::Int,
)
smalluml::Boolean_strategy = st.builds(
    smalluml::Boolean,
)
smalluml::String_strategy = st.builds(
    smalluml::String,
)
smalluml::Float_strategy = st.builds(
    smalluml::Float,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml::Type_strategy = st.builds(
    smalluml::Type,
)
smalluml::Association_strategy = st.builds(
    smalluml::Association,
)
smalluml::Method_strategy = st.builds(
    smalluml::Method,
)
smalluml::Class_strategy = st.builds(
    smalluml::Class,
)
smalluml::Heritage_strategy = st.builds(
    smalluml::Heritage,
)
smalluml::Role_strategy = st.builds(
    smalluml::Role,
    lower=
        st.integers(),
    upper=
        st.integers()
)

@given(instance=smalluml::Diagram_strategy)
@settings(max_examples=50)
def test_smalluml::diagram_instantiation(instance):
    assert isinstance(instance, smalluml::Diagram)

@given(instance=smalluml::NamedElement_strategy)
@settings(max_examples=50)
def test_smalluml::namedelement_instantiation(instance):
    assert isinstance(instance, smalluml::NamedElement)

@given(instance=smalluml::NamedElement_strategy)
def test_smalluml::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=smalluml::NamedElement_strategy)
def test_smalluml::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml::Int_strategy)
@settings(max_examples=50)
def test_smalluml::int_instantiation(instance):
    assert isinstance(instance, smalluml::Int)

@given(instance=smalluml::Boolean_strategy)
@settings(max_examples=50)
def test_smalluml::boolean_instantiation(instance):
    assert isinstance(instance, smalluml::Boolean)

@given(instance=smalluml::String_strategy)
@settings(max_examples=50)
def test_smalluml::string_instantiation(instance):
    assert isinstance(instance, smalluml::String)

@given(instance=smalluml::Float_strategy)
@settings(max_examples=50)
def test_smalluml::float_instantiation(instance):
    assert isinstance(instance, smalluml::Float)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=smalluml::Type_strategy)
@settings(max_examples=50)
def test_smalluml::type_instantiation(instance):
    assert isinstance(instance, smalluml::Type)

@given(instance=smalluml::Association_strategy)
@settings(max_examples=50)
def test_smalluml::association_instantiation(instance):
    assert isinstance(instance, smalluml::Association)

@given(instance=smalluml::Method_strategy)
@settings(max_examples=50)
def test_smalluml::method_instantiation(instance):
    assert isinstance(instance, smalluml::Method)

@given(instance=smalluml::Class_strategy)
@settings(max_examples=50)
def test_smalluml::class_instantiation(instance):
    assert isinstance(instance, smalluml::Class)

@given(instance=smalluml::Heritage_strategy)
@settings(max_examples=50)
def test_smalluml::heritage_instantiation(instance):
    assert isinstance(instance, smalluml::Heritage)

@given(instance=smalluml::Role_strategy)
@settings(max_examples=50)
def test_smalluml::role_instantiation(instance):
    assert isinstance(instance, smalluml::Role)

@given(instance=smalluml::Role_strategy)
def test_smalluml::role_lower_type(instance):
    assert isinstance(instance.lower, int)


@given(instance=smalluml::Role_strategy)
def test_smalluml::role_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original

@given(instance=smalluml::Role_strategy)
def test_smalluml::role_upper_type(instance):
    assert isinstance(instance.upper, int)


@given(instance=smalluml::Role_strategy)
def test_smalluml::role_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original
