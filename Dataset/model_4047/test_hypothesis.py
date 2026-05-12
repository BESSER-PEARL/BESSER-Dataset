import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SuperType,
    smalluml_Enumeration,
    smalluml_Type,
    smalluml_Class,
    NamedElement,
    smalluml_Attribute,
    smalluml_Parameter,
    smalluml_Operation,
    smalluml_Package,
    smalluml_Role,
    smalluml_Association,
    smalluml_SuperType,
    smalluml_NamedElement,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_supertype_is_not_abstract():
    assert not inspect.isabstract(SuperType)


def test_supertype_constructor_exists():
    assert callable(SuperType.__init__)


def test_supertype_constructor_args():
    sig = inspect.signature(SuperType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml_Enumeration)


def test_smalluml_enumeration_constructor_exists():
    assert callable(smalluml_Enumeration.__init__)


def test_smalluml_enumeration_constructor_args():
    sig = inspect.signature(smalluml_Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "enumeration" in params, "Missing parameter 'enumeration'"

def test_smalluml_enumeration_has_enumeration():
    assert hasattr(smalluml_Enumeration, "enumeration")
    descriptor = None
    for klass in smalluml_Enumeration.__mro__:
        if "enumeration" in klass.__dict__:
            descriptor = klass.__dict__["enumeration"]
            break
    assert isinstance(descriptor, property)



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
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_smalluml_class_has_isAbstract():
    assert hasattr(smalluml_Class, "isAbstract")
    descriptor = None
    for klass in smalluml_Class.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml_Attribute)


def test_smalluml_attribute_constructor_exists():
    assert callable(smalluml_Attribute.__init__)


def test_smalluml_attribute_constructor_args():
    sig = inspect.signature(smalluml_Attribute.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_parameter_is_not_abstract():
    assert not inspect.isabstract(smalluml_Parameter)


def test_smalluml_parameter_constructor_exists():
    assert callable(smalluml_Parameter.__init__)


def test_smalluml_parameter_constructor_args():
    sig = inspect.signature(smalluml_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_operation_is_not_abstract():
    assert not inspect.isabstract(smalluml_Operation)


def test_smalluml_operation_constructor_exists():
    assert callable(smalluml_Operation.__init__)


def test_smalluml_operation_constructor_args():
    sig = inspect.signature(smalluml_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "isAbstract" in params, "Missing parameter 'isAbstract'"

def test_smalluml_operation_has_isAbstract():
    assert hasattr(smalluml_Operation, "isAbstract")
    descriptor = None
    for klass in smalluml_Operation.__mro__:
        if "isAbstract" in klass.__dict__:
            descriptor = klass.__dict__["isAbstract"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_package_is_not_abstract():
    assert not inspect.isabstract(smalluml_Package)


def test_smalluml_package_constructor_exists():
    assert callable(smalluml_Package.__init__)


def test_smalluml_package_constructor_args():
    sig = inspect.signature(smalluml_Package.__init__)
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



def test_smalluml_association_is_not_abstract():
    assert not inspect.isabstract(smalluml_Association)


def test_smalluml_association_constructor_exists():
    assert callable(smalluml_Association.__init__)


def test_smalluml_association_constructor_args():
    sig = inspect.signature(smalluml_Association.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_supertype_is_not_abstract():
    assert not inspect.isabstract(smalluml_SuperType)


def test_smalluml_supertype_constructor_exists():
    assert callable(smalluml_SuperType.__init__)


def test_smalluml_supertype_constructor_args():
    sig = inspect.signature(smalluml_SuperType.__init__)
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
SuperType_strategy = st.builds(
    SuperType,
)
smalluml_Enumeration_strategy = st.builds(
    smalluml_Enumeration,
    enumeration=
        safe_text
)
smalluml_Type_strategy = st.builds(
    smalluml_Type,
)
smalluml_Class_strategy = st.builds(
    smalluml_Class,
    isAbstract=
        st.booleans()
)
NamedElement_strategy = st.builds(
    NamedElement,
)
smalluml_Attribute_strategy = st.builds(
    smalluml_Attribute,
)
smalluml_Parameter_strategy = st.builds(
    smalluml_Parameter,
)
smalluml_Operation_strategy = st.builds(
    smalluml_Operation,
    isAbstract=
        st.booleans()
)
smalluml_Package_strategy = st.builds(
    smalluml_Package,
)
smalluml_Role_strategy = st.builds(
    smalluml_Role,
    lowerBound=
        st.integers(),
    upperBound=
        st.integers()
)
smalluml_Association_strategy = st.builds(
    smalluml_Association,
)
smalluml_SuperType_strategy = st.builds(
    smalluml_SuperType,
)
smalluml_NamedElement_strategy = st.builds(
    smalluml_NamedElement,
    name=
        safe_text
)

@given(instance=SuperType_strategy)
@settings(max_examples=50)
def test_supertype_instantiation(instance):
    assert isinstance(instance, SuperType)

@given(instance=smalluml_Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml_enumeration_instantiation(instance):
    assert isinstance(instance, smalluml_Enumeration)



@given(instance=smalluml_Enumeration_strategy)
def test_smalluml_enumeration_enumeration_setter(instance):
    original = instance.enumeration
    instance.enumeration = original
    assert instance.enumeration == original

@given(instance=smalluml_Type_strategy)
@settings(max_examples=50)
def test_smalluml_type_instantiation(instance):
    assert isinstance(instance, smalluml_Type)

@given(instance=smalluml_Class_strategy)
@settings(max_examples=50)
def test_smalluml_class_instantiation(instance):
    assert isinstance(instance, smalluml_Class)



@given(instance=smalluml_Class_strategy)
def test_smalluml_class_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=smalluml_Attribute_strategy)
@settings(max_examples=50)
def test_smalluml_attribute_instantiation(instance):
    assert isinstance(instance, smalluml_Attribute)

@given(instance=smalluml_Parameter_strategy)
@settings(max_examples=50)
def test_smalluml_parameter_instantiation(instance):
    assert isinstance(instance, smalluml_Parameter)

@given(instance=smalluml_Operation_strategy)
@settings(max_examples=50)
def test_smalluml_operation_instantiation(instance):
    assert isinstance(instance, smalluml_Operation)



@given(instance=smalluml_Operation_strategy)
def test_smalluml_operation_isAbstract_setter(instance):
    original = instance.isAbstract
    instance.isAbstract = original
    assert instance.isAbstract == original

@given(instance=smalluml_Package_strategy)
@settings(max_examples=50)
def test_smalluml_package_instantiation(instance):
    assert isinstance(instance, smalluml_Package)

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

@given(instance=smalluml_Association_strategy)
@settings(max_examples=50)
def test_smalluml_association_instantiation(instance):
    assert isinstance(instance, smalluml_Association)

@given(instance=smalluml_SuperType_strategy)
@settings(max_examples=50)
def test_smalluml_supertype_instantiation(instance):
    assert isinstance(instance, smalluml_SuperType)

@given(instance=smalluml_NamedElement_strategy)
@settings(max_examples=50)
def test_smalluml_namedelement_instantiation(instance):
    assert isinstance(instance, smalluml_NamedElement)



@given(instance=smalluml_NamedElement_strategy)
def test_smalluml_namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
