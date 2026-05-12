import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Relation,
    smalluml_Reference,
    smalluml_Composition,
    Type,
    smalluml_Real,
    smalluml_Integer,
    smalluml_UnlimitedNatural,
    smalluml_Bool,
    smalluml_String,
    smalluml_Type,
    NamedElement,
    smalluml_Role,
    smalluml_Package,
    smalluml_Relation,
    smalluml_Attribute,
    smalluml_Method,
    smalluml_Parameter,
    smalluml_Enumeration,
    smalluml_Class,
    smalluml_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_relation_is_not_abstract():
    assert not inspect.isabstract(Relation)


def test_relation_constructor_exists():
    assert callable(Relation.__init__)


def test_relation_constructor_args():
    sig = inspect.signature(Relation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_reference_is_not_abstract():
    assert not inspect.isabstract(smalluml_Reference)


def test_smalluml_reference_constructor_exists():
    assert callable(smalluml_Reference.__init__)


def test_smalluml_reference_constructor_args():
    sig = inspect.signature(smalluml_Reference.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_composition_is_not_abstract():
    assert not inspect.isabstract(smalluml_Composition)


def test_smalluml_composition_constructor_exists():
    assert callable(smalluml_Composition.__init__)


def test_smalluml_composition_constructor_args():
    sig = inspect.signature(smalluml_Composition.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_real_is_not_abstract():
    assert not inspect.isabstract(smalluml_Real)


def test_smalluml_real_constructor_exists():
    assert callable(smalluml_Real.__init__)


def test_smalluml_real_constructor_args():
    sig = inspect.signature(smalluml_Real.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_integer_is_not_abstract():
    assert not inspect.isabstract(smalluml_Integer)


def test_smalluml_integer_constructor_exists():
    assert callable(smalluml_Integer.__init__)


def test_smalluml_integer_constructor_args():
    sig = inspect.signature(smalluml_Integer.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_unlimitednatural_is_not_abstract():
    assert not inspect.isabstract(smalluml_UnlimitedNatural)


def test_smalluml_unlimitednatural_constructor_exists():
    assert callable(smalluml_UnlimitedNatural.__init__)


def test_smalluml_unlimitednatural_constructor_args():
    sig = inspect.signature(smalluml_UnlimitedNatural.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_bool_is_not_abstract():
    assert not inspect.isabstract(smalluml_Bool)


def test_smalluml_bool_constructor_exists():
    assert callable(smalluml_Bool.__init__)


def test_smalluml_bool_constructor_args():
    sig = inspect.signature(smalluml_Bool.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_string_is_not_abstract():
    assert not inspect.isabstract(smalluml_String)


def test_smalluml_string_constructor_exists():
    assert callable(smalluml_String.__init__)


def test_smalluml_string_constructor_args():
    sig = inspect.signature(smalluml_String.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_type_is_not_abstract():
    assert not inspect.isabstract(smalluml_Type)


def test_smalluml_type_constructor_exists():
    assert callable(smalluml_Type.__init__)


def test_smalluml_type_constructor_args():
    sig = inspect.signature(smalluml_Type.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_role_is_not_abstract():
    assert not inspect.isabstract(smalluml_Role)


def test_smalluml_role_constructor_exists():
    assert callable(smalluml_Role.__init__)


def test_smalluml_role_constructor_args():
    sig = inspect.signature(smalluml_Role.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_smalluml_role_has_lowerBound():
    assert hasattr(smalluml_Role, "lowerBound")
    descriptor = None
    for klass in smalluml_Role.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_smalluml_role_has_upperBound():
    assert hasattr(smalluml_Role, "upperBound")
    descriptor = None
    for klass in smalluml_Role.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_package_is_not_abstract():
    assert not inspect.isabstract(smalluml_Package)


def test_smalluml_package_constructor_exists():
    assert callable(smalluml_Package.__init__)


def test_smalluml_package_constructor_args():
    sig = inspect.signature(smalluml_Package.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_relation_is_not_abstract():
    assert not inspect.isabstract(smalluml_Relation)


def test_smalluml_relation_constructor_exists():
    assert callable(smalluml_Relation.__init__)


def test_smalluml_relation_constructor_args():
    sig = inspect.signature(smalluml_Relation.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml_Attribute)


def test_smalluml_attribute_constructor_exists():
    assert callable(smalluml_Attribute.__init__)


def test_smalluml_attribute_constructor_args():
    sig = inspect.signature(smalluml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_method_is_not_abstract():
    assert not inspect.isabstract(smalluml_Method)


def test_smalluml_method_constructor_exists():
    assert callable(smalluml_Method.__init__)


def test_smalluml_method_constructor_args():
    sig = inspect.signature(smalluml_Method.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_parameter_is_not_abstract():
    assert not inspect.isabstract(smalluml_Parameter)


def test_smalluml_parameter_constructor_exists():
    assert callable(smalluml_Parameter.__init__)


def test_smalluml_parameter_constructor_args():
    sig = inspect.signature(smalluml_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml_Enumeration)


def test_smalluml_enumeration_constructor_exists():
    assert callable(smalluml_Enumeration.__init__)


def test_smalluml_enumeration_constructor_args():
    sig = inspect.signature(smalluml_Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "values" in params, "Missing parameter 'values'"

def test_smalluml_enumeration_has_values():
    assert hasattr(smalluml_Enumeration, "values")
    descriptor = None
    for klass in smalluml_Enumeration.__mro__:
        if "values" in klass.__dict__:
            descriptor = klass.__dict__["values"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_class_is_not_abstract():
    assert not inspect.isabstract(smalluml_Class)


def test_smalluml_class_constructor_exists():
    assert callable(smalluml_Class.__init__)


def test_smalluml_class_constructor_args():
    sig = inspect.signature(smalluml_Class.__init__)
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
Relation_strategy = st.builds(
    Relation,
)
smalluml_Reference_strategy = st.builds(
    smalluml_Reference,
)
smalluml_Composition_strategy = st.builds(
    smalluml_Composition,
)
Type_strategy = st.builds(
    Type,
)
smalluml_Real_strategy = st.builds(
    smalluml_Real,
)
smalluml_Integer_strategy = st.builds(
    smalluml_Integer,
)
smalluml_UnlimitedNatural_strategy = st.builds(
    smalluml_UnlimitedNatural,
)
smalluml_Bool_strategy = st.builds(
    smalluml_Bool,
)
smalluml_String_strategy = st.builds(
    smalluml_String,
)
smalluml_Type_strategy = st.builds(
    smalluml_Type,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml_Role_strategy = st.builds(
    smalluml_Role,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)
smalluml_Package_strategy = st.builds(
    smalluml_Package,
)
smalluml_Relation_strategy = st.builds(
    smalluml_Relation,
)
smalluml_Attribute_strategy = st.builds(
    smalluml_Attribute,
)
smalluml_Method_strategy = st.builds(
    smalluml_Method,
)
smalluml_Parameter_strategy = st.builds(
    smalluml_Parameter,
)
smalluml_Enumeration_strategy = st.builds(
    smalluml_Enumeration,
    values=
        safe_text
)
smalluml_Class_strategy = st.builds(
    smalluml_Class,
)
smalluml_NamedElement_strategy = st.builds(
    smalluml_NamedElement,
    name=
        safe_text
)

@given(instance=Relation_strategy)
@settings(max_examples=50)
def test_relation_instantiation(instance):
    assert isinstance(instance, Relation)

@given(instance=smalluml_Reference_strategy)
@settings(max_examples=50)
def test_smalluml_reference_instantiation(instance):
    assert isinstance(instance, smalluml_Reference)

@given(instance=smalluml_Composition_strategy)
@settings(max_examples=50)
def test_smalluml_composition_instantiation(instance):
    assert isinstance(instance, smalluml_Composition)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml_Real_strategy)
@settings(max_examples=50)
def test_smalluml_real_instantiation(instance):
    assert isinstance(instance, smalluml_Real)

@given(instance=smalluml_Integer_strategy)
@settings(max_examples=50)
def test_smalluml_integer_instantiation(instance):
    assert isinstance(instance, smalluml_Integer)

@given(instance=smalluml_UnlimitedNatural_strategy)
@settings(max_examples=50)
def test_smalluml_unlimitednatural_instantiation(instance):
    assert isinstance(instance, smalluml_UnlimitedNatural)

@given(instance=smalluml_Bool_strategy)
@settings(max_examples=50)
def test_smalluml_bool_instantiation(instance):
    assert isinstance(instance, smalluml_Bool)

@given(instance=smalluml_String_strategy)
@settings(max_examples=50)
def test_smalluml_string_instantiation(instance):
    assert isinstance(instance, smalluml_String)

@given(instance=smalluml_Type_strategy)
@settings(max_examples=50)
def test_smalluml_type_instantiation(instance):
    assert isinstance(instance, smalluml_Type)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=smalluml_Role_strategy)
@settings(max_examples=50)
def test_smalluml_role_instantiation(instance):
    assert isinstance(instance, smalluml_Role)



@given(instance=smalluml_Role_strategy)
def test_smalluml_role_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=smalluml_Role_strategy)
def test_smalluml_role_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=smalluml_Package_strategy)
@settings(max_examples=50)
def test_smalluml_package_instantiation(instance):
    assert isinstance(instance, smalluml_Package)

@given(instance=smalluml_Relation_strategy)
@settings(max_examples=50)
def test_smalluml_relation_instantiation(instance):
    assert isinstance(instance, smalluml_Relation)

@given(instance=smalluml_Attribute_strategy)
@settings(max_examples=50)
def test_smalluml_attribute_instantiation(instance):
    assert isinstance(instance, smalluml_Attribute)

@given(instance=smalluml_Method_strategy)
@settings(max_examples=50)
def test_smalluml_method_instantiation(instance):
    assert isinstance(instance, smalluml_Method)

@given(instance=smalluml_Parameter_strategy)
@settings(max_examples=50)
def test_smalluml_parameter_instantiation(instance):
    assert isinstance(instance, smalluml_Parameter)

@given(instance=smalluml_Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml_enumeration_instantiation(instance):
    assert isinstance(instance, smalluml_Enumeration)



@given(instance=smalluml_Enumeration_strategy)
def test_smalluml_enumeration_values_setter(instance):
    original = instance.values
    instance.values = original
    assert instance.values == original

@given(instance=smalluml_Class_strategy)
@settings(max_examples=50)
def test_smalluml_class_instantiation(instance):
    assert isinstance(instance, smalluml_Class)

@given(instance=smalluml_NamedElement_strategy)
@settings(max_examples=50)
def test_smalluml_namedelement_instantiation(instance):
    assert isinstance(instance, smalluml_NamedElement)



@given(instance=smalluml_NamedElement_strategy)
def test_smalluml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
