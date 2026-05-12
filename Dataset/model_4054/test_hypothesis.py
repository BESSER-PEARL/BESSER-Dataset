import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Type,
    smalluml_RealType,
    smalluml_IntegerType,
    smalluml_BooleanType,
    smalluml_Enumeration,
    smalluml_Attribute,
    Entity,
    smalluml_Class,
    smalluml_Association,
    smalluml_Cardinalities,
    smalluml_Parameter,
    smalluml_Type,
    smalluml_Entity,
    smalluml_ClassDiagram,
    smalluml_Operation,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_realtype_is_not_abstract():
    assert not inspect.isabstract(smalluml_RealType)


def test_smalluml_realtype_constructor_exists():
    assert callable(smalluml_RealType.__init__)


def test_smalluml_realtype_constructor_args():
    sig = inspect.signature(smalluml_RealType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_integertype_is_not_abstract():
    assert not inspect.isabstract(smalluml_IntegerType)


def test_smalluml_integertype_constructor_exists():
    assert callable(smalluml_IntegerType.__init__)


def test_smalluml_integertype_constructor_args():
    sig = inspect.signature(smalluml_IntegerType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_booleantype_is_not_abstract():
    assert not inspect.isabstract(smalluml_BooleanType)


def test_smalluml_booleantype_constructor_exists():
    assert callable(smalluml_BooleanType.__init__)


def test_smalluml_booleantype_constructor_args():
    sig = inspect.signature(smalluml_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_enumeration_is_not_abstract():
    assert not inspect.isabstract(smalluml_Enumeration)


def test_smalluml_enumeration_constructor_exists():
    assert callable(smalluml_Enumeration.__init__)


def test_smalluml_enumeration_constructor_args():
    sig = inspect.signature(smalluml_Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "variable" in params, "Missing parameter 'variable'"
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_enumeration_has_variable():
    assert hasattr(smalluml_Enumeration, "variable")
    descriptor = None
    for klass in smalluml_Enumeration.__mro__:
        if "variable" in klass.__dict__:
            descriptor = klass.__dict__["variable"]
            break
    assert isinstance(descriptor, property)

def test_smalluml_enumeration_has_name():
    assert hasattr(smalluml_Enumeration, "name")
    descriptor = None
    for klass in smalluml_Enumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_attribute_is_not_abstract():
    assert not inspect.isabstract(smalluml_Attribute)


def test_smalluml_attribute_constructor_exists():
    assert callable(smalluml_Attribute.__init__)


def test_smalluml_attribute_constructor_args():
    sig = inspect.signature(smalluml_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_attribute_has_name():
    assert hasattr(smalluml_Attribute, "name")
    descriptor = None
    for klass in smalluml_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entity_is_not_abstract():
    assert not inspect.isabstract(Entity)


def test_entity_constructor_exists():
    assert callable(Entity.__init__)


def test_entity_constructor_args():
    sig = inspect.signature(Entity.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_class_is_not_abstract():
    assert not inspect.isabstract(smalluml_Class)


def test_smalluml_class_constructor_exists():
    assert callable(smalluml_Class.__init__)


def test_smalluml_class_constructor_args():
    sig = inspect.signature(smalluml_Class.__init__)
    params = list(sig.parameters.keys())
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_smalluml_class_has_abstract():
    assert hasattr(smalluml_Class, "abstract")
    descriptor = None
    for klass in smalluml_Class.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_association_is_not_abstract():
    assert not inspect.isabstract(smalluml_Association)


def test_smalluml_association_constructor_exists():
    assert callable(smalluml_Association.__init__)


def test_smalluml_association_constructor_args():
    sig = inspect.signature(smalluml_Association.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_cardinalities_is_not_abstract():
    assert not inspect.isabstract(smalluml_Cardinalities)


def test_smalluml_cardinalities_constructor_exists():
    assert callable(smalluml_Cardinalities.__init__)


def test_smalluml_cardinalities_constructor_args():
    sig = inspect.signature(smalluml_Cardinalities.__init__)
    params = list(sig.parameters.keys())
    assert "upperbound" in params, "Missing parameter 'upperbound'"
    assert "lowerbound" in params, "Missing parameter 'lowerbound'"

def test_smalluml_cardinalities_has_upperbound():
    assert hasattr(smalluml_Cardinalities, "upperbound")
    descriptor = None
    for klass in smalluml_Cardinalities.__mro__:
        if "upperbound" in klass.__dict__:
            descriptor = klass.__dict__["upperbound"]
            break
    assert isinstance(descriptor, property)

def test_smalluml_cardinalities_has_lowerbound():
    assert hasattr(smalluml_Cardinalities, "lowerbound")
    descriptor = None
    for klass in smalluml_Cardinalities.__mro__:
        if "lowerbound" in klass.__dict__:
            descriptor = klass.__dict__["lowerbound"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_parameter_is_not_abstract():
    assert not inspect.isabstract(smalluml_Parameter)


def test_smalluml_parameter_constructor_exists():
    assert callable(smalluml_Parameter.__init__)


def test_smalluml_parameter_constructor_args():
    sig = inspect.signature(smalluml_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_parameter_has_name():
    assert hasattr(smalluml_Parameter, "name")
    descriptor = None
    for klass in smalluml_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_type_is_not_abstract():
    assert not inspect.isabstract(smalluml_Type)


def test_smalluml_type_constructor_exists():
    assert callable(smalluml_Type.__init__)


def test_smalluml_type_constructor_args():
    sig = inspect.signature(smalluml_Type.__init__)
    params = list(sig.parameters.keys())



def test_smalluml_entity_is_not_abstract():
    assert not inspect.isabstract(smalluml_Entity)


def test_smalluml_entity_constructor_exists():
    assert callable(smalluml_Entity.__init__)


def test_smalluml_entity_constructor_args():
    sig = inspect.signature(smalluml_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_entity_has_name():
    assert hasattr(smalluml_Entity, "name")
    descriptor = None
    for klass in smalluml_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_classdiagram_is_not_abstract():
    assert not inspect.isabstract(smalluml_ClassDiagram)


def test_smalluml_classdiagram_constructor_exists():
    assert callable(smalluml_ClassDiagram.__init__)


def test_smalluml_classdiagram_constructor_args():
    sig = inspect.signature(smalluml_ClassDiagram.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_classdiagram_has_name():
    assert hasattr(smalluml_ClassDiagram, "name")
    descriptor = None
    for klass in smalluml_ClassDiagram.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_smalluml_operation_is_not_abstract():
    assert not inspect.isabstract(smalluml_Operation)


def test_smalluml_operation_constructor_exists():
    assert callable(smalluml_Operation.__init__)


def test_smalluml_operation_constructor_args():
    sig = inspect.signature(smalluml_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_smalluml_operation_has_name():
    assert hasattr(smalluml_Operation, "name")
    descriptor = None
    for klass in smalluml_Operation.__mro__:
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
Type_strategy = st.builds(
    Type,
)
smalluml_RealType_strategy = st.builds(
    smalluml_RealType,
)
smalluml_IntegerType_strategy = st.builds(
    smalluml_IntegerType,
)
smalluml_BooleanType_strategy = st.builds(
    smalluml_BooleanType,
)
smalluml_Enumeration_strategy = st.builds(
    smalluml_Enumeration,
    variable=
        safe_text,
    name=
        safe_text
)
smalluml_Attribute_strategy = st.builds(
    smalluml_Attribute,
    name=
        safe_text
)
Entity_strategy = st.builds(
    Entity,
)
smalluml_Class_strategy = st.builds(
    smalluml_Class,
    abstract=
        st.booleans()
)
smalluml_Association_strategy = st.builds(
    smalluml_Association,
)
smalluml_Cardinalities_strategy = st.builds(
    smalluml_Cardinalities,
    upperbound=
        st.integers(),
    lowerbound=
        st.integers()
)
smalluml_Parameter_strategy = st.builds(
    smalluml_Parameter,
    name=
        safe_text
)
smalluml_Type_strategy = st.builds(
    smalluml_Type,
)
smalluml_Entity_strategy = st.builds(
    smalluml_Entity,
    name=
        safe_text
)
smalluml_ClassDiagram_strategy = st.builds(
    smalluml_ClassDiagram,
    name=
        safe_text
)
smalluml_Operation_strategy = st.builds(
    smalluml_Operation,
    name=
        safe_text
)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=smalluml_RealType_strategy)
@settings(max_examples=50)
def test_smalluml_realtype_instantiation(instance):
    assert isinstance(instance, smalluml_RealType)

@given(instance=smalluml_IntegerType_strategy)
@settings(max_examples=50)
def test_smalluml_integertype_instantiation(instance):
    assert isinstance(instance, smalluml_IntegerType)

@given(instance=smalluml_BooleanType_strategy)
@settings(max_examples=50)
def test_smalluml_booleantype_instantiation(instance):
    assert isinstance(instance, smalluml_BooleanType)

@given(instance=smalluml_Enumeration_strategy)
@settings(max_examples=50)
def test_smalluml_enumeration_instantiation(instance):
    assert isinstance(instance, smalluml_Enumeration)



@given(instance=smalluml_Enumeration_strategy)
def test_smalluml_enumeration_variable_setter(instance):
    original = instance.variable
    instance.variable = original
    assert instance.variable == original



@given(instance=smalluml_Enumeration_strategy)
def test_smalluml_enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml_Attribute_strategy)
@settings(max_examples=50)
def test_smalluml_attribute_instantiation(instance):
    assert isinstance(instance, smalluml_Attribute)



@given(instance=smalluml_Attribute_strategy)
def test_smalluml_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Entity_strategy)
@settings(max_examples=50)
def test_entity_instantiation(instance):
    assert isinstance(instance, Entity)

@given(instance=smalluml_Class_strategy)
@settings(max_examples=50)
def test_smalluml_class_instantiation(instance):
    assert isinstance(instance, smalluml_Class)



@given(instance=smalluml_Class_strategy)
def test_smalluml_class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=smalluml_Association_strategy)
@settings(max_examples=50)
def test_smalluml_association_instantiation(instance):
    assert isinstance(instance, smalluml_Association)

@given(instance=smalluml_Cardinalities_strategy)
@settings(max_examples=50)
def test_smalluml_cardinalities_instantiation(instance):
    assert isinstance(instance, smalluml_Cardinalities)



@given(instance=smalluml_Cardinalities_strategy)
def test_smalluml_cardinalities_upperbound_setter(instance):
    original = instance.upperbound
    instance.upperbound = original
    assert instance.upperbound == original



@given(instance=smalluml_Cardinalities_strategy)
def test_smalluml_cardinalities_lowerbound_setter(instance):
    original = instance.lowerbound
    instance.lowerbound = original
    assert instance.lowerbound == original

@given(instance=smalluml_Parameter_strategy)
@settings(max_examples=50)
def test_smalluml_parameter_instantiation(instance):
    assert isinstance(instance, smalluml_Parameter)



@given(instance=smalluml_Parameter_strategy)
def test_smalluml_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml_Type_strategy)
@settings(max_examples=50)
def test_smalluml_type_instantiation(instance):
    assert isinstance(instance, smalluml_Type)

@given(instance=smalluml_Entity_strategy)
@settings(max_examples=50)
def test_smalluml_entity_instantiation(instance):
    assert isinstance(instance, smalluml_Entity)



@given(instance=smalluml_Entity_strategy)
def test_smalluml_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml_ClassDiagram_strategy)
@settings(max_examples=50)
def test_smalluml_classdiagram_instantiation(instance):
    assert isinstance(instance, smalluml_ClassDiagram)



@given(instance=smalluml_ClassDiagram_strategy)
def test_smalluml_classdiagram_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=smalluml_Operation_strategy)
@settings(max_examples=50)
def test_smalluml_operation_instantiation(instance):
    assert isinstance(instance, smalluml_Operation)



@given(instance=smalluml_Operation_strategy)
def test_smalluml_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
