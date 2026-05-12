import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    smalluml_Diagram,
    smalluml_NamedElement,
    Type,
    smalluml_Boolean,
    smalluml_Int,
    smalluml_String,
    smalluml_Float,
    NamedElement,
    smalluml_Association,
    smalluml_Method,
    smalluml_Type,
    smalluml_Class,
    smalluml_Heritage,
    smalluml_Role,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_smalluml_diagram_is_not_abstract():
    assert not inspect.isabstract(smalluml_Diagram)


def test_smalluml_diagram_constructor_exists():
    assert callable(smalluml_Diagram.__init__)


def test_smalluml_diagram_constructor_args():
    sig = inspect.signature(smalluml_Diagram.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_namedelement_is_not_abstract():
    assert not inspect.isabstract(smalluml_NamedElement)


def test_smalluml_namedelement_constructor_exists():
    assert callable(smalluml_NamedElement.__init__)


def test_smalluml_namedelement_constructor_args():
    sig = inspect.signature(smalluml_NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_namedelement_has_name():
    assert hasattr(smalluml_NamedElement, "name")
    descriptor = None
    for klass in smalluml_NamedElement.__mro__:
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



def test_smalluml_boolean_is_not_abstract():
    assert not inspect.isabstract(smalluml_Boolean)


def test_smalluml_boolean_constructor_exists():
    assert callable(smalluml_Boolean.__init__)


def test_smalluml_boolean_constructor_args():
    sig = inspect.signature(smalluml_Boolean.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_int_is_not_abstract():
    assert not inspect.isabstract(smalluml_Int)


def test_smalluml_int_constructor_exists():
    assert callable(smalluml_Int.__init__)


def test_smalluml_int_constructor_args():
    sig = inspect.signature(smalluml_Int.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_string_is_not_abstract():
    assert not inspect.isabstract(smalluml_String)


def test_smalluml_string_constructor_exists():
    assert callable(smalluml_String.__init__)


def test_smalluml_string_constructor_args():
    sig = inspect.signature(smalluml_String.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_float_is_not_abstract():
    assert not inspect.isabstract(smalluml_Float)


def test_smalluml_float_constructor_exists():
    assert callable(smalluml_Float.__init__)


def test_smalluml_float_constructor_args():
    sig = inspect.signature(smalluml_Float.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_association_is_not_abstract():
    assert not inspect.isabstract(smalluml_Association)


def test_smalluml_association_constructor_exists():
    assert callable(smalluml_Association.__init__)


def test_smalluml_association_constructor_args():
    sig = inspect.signature(smalluml_Association.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_method_is_not_abstract():
    assert not inspect.isabstract(smalluml_Method)


def test_smalluml_method_constructor_exists():
    assert callable(smalluml_Method.__init__)


def test_smalluml_method_constructor_args():
    sig = inspect.signature(smalluml_Method.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_type_is_not_abstract():
    assert not inspect.isabstract(smalluml_Type)


def test_smalluml_type_constructor_exists():
    assert callable(smalluml_Type.__init__)


def test_smalluml_type_constructor_args():
    sig = inspect.signature(smalluml_Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_class_is_not_abstract():
    assert not inspect.isabstract(smalluml_Class)


def test_smalluml_class_constructor_exists():
    assert callable(smalluml_Class.__init__)


def test_smalluml_class_constructor_args():
    sig = inspect.signature(smalluml_Class.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_heritage_is_not_abstract():
    assert not inspect.isabstract(smalluml_Heritage)


def test_smalluml_heritage_constructor_exists():
    assert callable(smalluml_Heritage.__init__)


def test_smalluml_heritage_constructor_args():
    sig = inspect.signature(smalluml_Heritage.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_role_is_not_abstract():
    assert not inspect.isabstract(smalluml_Role)


def test_smalluml_role_constructor_exists():
    assert callable(smalluml_Role.__init__)


def test_smalluml_role_constructor_args():
    sig = inspect.signature(smalluml_Role.__init__)
    params = list(sig.parameters.keys())
    assert "upper" in params, "Missing parameter 'upper'"
    assert "lower" in params, "Missing parameter 'lower'"

def test_smalluml_role_has_upper():
    assert hasattr(smalluml_Role, "upper")
    descriptor = None
    for klass in smalluml_Role.__mro__:
        if "upper" in klass.__dict__:
            descriptor = klass.__dict__["upper"]
            break
    assert isinstance(descriptor, property)

def test_smalluml_role_has_lower():
    assert hasattr(smalluml_Role, "lower")
    descriptor = None
    for klass in smalluml_Role.__mro__:
        if "lower" in klass.__dict__:
            descriptor = klass.__dict__["lower"]
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
smalluml_Diagram_strategy = st.builds(
    smalluml_Diagram,
)
smalluml_NamedElement_strategy = st.builds(
    smalluml_NamedElement,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
smalluml_Boolean_strategy = st.builds(
    smalluml_Boolean,
)
smalluml_Int_strategy = st.builds(
    smalluml_Int,
)
smalluml_String_strategy = st.builds(
    smalluml_String,
)
smalluml_Float_strategy = st.builds(
    smalluml_Float,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml_Association_strategy = st.builds(
    smalluml_Association,
)
smalluml_Method_strategy = st.builds(
    smalluml_Method,
)
smalluml_Type_strategy = st.builds(
    smalluml_Type,
)
smalluml_Class_strategy = st.builds(
    smalluml_Class,
)
smalluml_Heritage_strategy = st.builds(
    smalluml_Heritage,
)
smalluml_Role_strategy = st.builds(
    smalluml_Role,
    upper=
        st.integers(),
    lower=
        st.integers()
)

@given(instance=smalluml_Diagram_strategy)
@settings(max_examples=50)
def test_smalluml_diagram_instantiation(instance):
    assert isinstance(instance, smalluml_Diagram)

@given(instance=smalluml_NamedElement_strategy)
@settings(max_examples=50)
def test_smalluml_namedelement_instantiation(instance):
    assert isinstance(instance, smalluml_NamedElement)



@given(instance=smalluml_NamedElement_strategy)
def test_smalluml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml_Boolean_strategy)
@settings(max_examples=50)
def test_smalluml_boolean_instantiation(instance):
    assert isinstance(instance, smalluml_Boolean)

@given(instance=smalluml_Int_strategy)
@settings(max_examples=50)
def test_smalluml_int_instantiation(instance):
    assert isinstance(instance, smalluml_Int)

@given(instance=smalluml_String_strategy)
@settings(max_examples=50)
def test_smalluml_string_instantiation(instance):
    assert isinstance(instance, smalluml_String)

@given(instance=smalluml_Float_strategy)
@settings(max_examples=50)
def test_smalluml_float_instantiation(instance):
    assert isinstance(instance, smalluml_Float)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=smalluml_Association_strategy)
@settings(max_examples=50)
def test_smalluml_association_instantiation(instance):
    assert isinstance(instance, smalluml_Association)

@given(instance=smalluml_Method_strategy)
@settings(max_examples=50)
def test_smalluml_method_instantiation(instance):
    assert isinstance(instance, smalluml_Method)

@given(instance=smalluml_Type_strategy)
@settings(max_examples=50)
def test_smalluml_type_instantiation(instance):
    assert isinstance(instance, smalluml_Type)

@given(instance=smalluml_Class_strategy)
@settings(max_examples=50)
def test_smalluml_class_instantiation(instance):
    assert isinstance(instance, smalluml_Class)

@given(instance=smalluml_Heritage_strategy)
@settings(max_examples=50)
def test_smalluml_heritage_instantiation(instance):
    assert isinstance(instance, smalluml_Heritage)

@given(instance=smalluml_Role_strategy)
@settings(max_examples=50)
def test_smalluml_role_instantiation(instance):
    assert isinstance(instance, smalluml_Role)



@given(instance=smalluml_Role_strategy)
def test_smalluml_role_upper_setter(instance):
    original = instance.upper
    instance.upper = original
    assert instance.upper == original



@given(instance=smalluml_Role_strategy)
def test_smalluml_role_lower_setter(instance):
    original = instance.lower
    instance.lower = original
    assert instance.lower == original
