import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Reference,
    titan_SingleReference,
    titan_MultiReference,
    Feature,
    titan_DataType,
    titan_Reference,
    DataType,
    titan_SingleDataType,
    titan_MultiDataType,
    titan_Feature,
    titan_Entity,
    titan_Package,
    titan_Module,
    InternalDSLType,
    DataTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_reference_is_not_abstract():
    assert not inspect.isabstract(Reference)


def test_reference_constructor_exists():
    assert callable(Reference.__init__)


def test_reference_constructor_args():
    sig = inspect.signature(Reference.__init__)
    params = list(sig.parameters.keys())



def test_titan_singlereference_is_not_abstract():
    assert not inspect.isabstract(titan_SingleReference)


def test_titan_singlereference_constructor_exists():
    assert callable(titan_SingleReference.__init__)


def test_titan_singlereference_constructor_args():
    sig = inspect.signature(titan_SingleReference.__init__)
    params = list(sig.parameters.keys())



def test_titan_multireference_is_not_abstract():
    assert not inspect.isabstract(titan_MultiReference)


def test_titan_multireference_constructor_exists():
    assert callable(titan_MultiReference.__init__)


def test_titan_multireference_constructor_args():
    sig = inspect.signature(titan_MultiReference.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_titan_datatype_is_not_abstract():
    assert not inspect.isabstract(titan_DataType)


def test_titan_datatype_constructor_exists():
    assert callable(titan_DataType.__init__)


def test_titan_datatype_constructor_args():
    sig = inspect.signature(titan_DataType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_titan_datatype_has_type():
    assert hasattr(titan_DataType, "type")
    descriptor = None
    for klass in titan_DataType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_titan_reference_is_not_abstract():
    assert not inspect.isabstract(titan_Reference)


def test_titan_reference_constructor_exists():
    assert callable(titan_Reference.__init__)


def test_titan_reference_constructor_args():
    sig = inspect.signature(titan_Reference.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_titan_reference_has_unique():
    assert hasattr(titan_Reference, "unique")
    descriptor = None
    for klass in titan_Reference.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_datatype_is_not_abstract():
    assert not inspect.isabstract(DataType)


def test_datatype_constructor_exists():
    assert callable(DataType.__init__)


def test_datatype_constructor_args():
    sig = inspect.signature(DataType.__init__)
    params = list(sig.parameters.keys())



def test_titan_singledatatype_is_not_abstract():
    assert not inspect.isabstract(titan_SingleDataType)


def test_titan_singledatatype_constructor_exists():
    assert callable(titan_SingleDataType.__init__)


def test_titan_singledatatype_constructor_args():
    sig = inspect.signature(titan_SingleDataType.__init__)
    params = list(sig.parameters.keys())



def test_titan_multidatatype_is_not_abstract():
    assert not inspect.isabstract(titan_MultiDataType)


def test_titan_multidatatype_constructor_exists():
    assert callable(titan_MultiDataType.__init__)


def test_titan_multidatatype_constructor_args():
    sig = inspect.signature(titan_MultiDataType.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_titan_multidatatype_has_unique():
    assert hasattr(titan_MultiDataType, "unique")
    descriptor = None
    for klass in titan_MultiDataType.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_titan_feature_is_not_abstract():
    assert not inspect.isabstract(titan_Feature)


def test_titan_feature_constructor_exists():
    assert callable(titan_Feature.__init__)


def test_titan_feature_constructor_args():
    sig = inspect.signature(titan_Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_titan_feature_has_name():
    assert hasattr(titan_Feature, "name")
    descriptor = None
    for klass in titan_Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_titan_entity_is_not_abstract():
    assert not inspect.isabstract(titan_Entity)


def test_titan_entity_constructor_exists():
    assert callable(titan_Entity.__init__)


def test_titan_entity_constructor_args():
    sig = inspect.signature(titan_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_titan_entity_has_name():
    assert hasattr(titan_Entity, "name")
    descriptor = None
    for klass in titan_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_titan_package_is_not_abstract():
    assert not inspect.isabstract(titan_Package)


def test_titan_package_constructor_exists():
    assert callable(titan_Package.__init__)


def test_titan_package_constructor_args():
    sig = inspect.signature(titan_Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_titan_package_has_name():
    assert hasattr(titan_Package, "name")
    descriptor = None
    for klass in titan_Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_titan_module_is_not_abstract():
    assert not inspect.isabstract(titan_Module)


def test_titan_module_constructor_exists():
    assert callable(titan_Module.__init__)


def test_titan_module_constructor_args():
    sig = inspect.signature(titan_Module.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_titan_module_has_name():
    assert hasattr(titan_Module, "name")
    descriptor = None
    for klass in titan_Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_titan_module_has_type():
    assert hasattr(titan_Module, "type")
    descriptor = None
    for klass in titan_Module.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_internaldsltype_exists():
    # Check that the Enumeration exists
    assert InternalDSLType is not None

def test_internaldsltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InternalDSLType]
    expected_literals = [
        "NestedFunctions",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InternalDSLType"

def test_datatypes_exists():
    # Check that the Enumeration exists
    assert DataTypes is not None

def test_datatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypes]
    expected_literals = [
        "Double",
        "Long",
        "Integer",
        "String",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypes"


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
Reference_strategy = st.builds(
    Reference,
)
titan_SingleReference_strategy = st.builds(
    titan_SingleReference,
)
titan_MultiReference_strategy = st.builds(
    titan_MultiReference,
)
Feature_strategy = st.builds(
    Feature,
)
titan_DataType_strategy = st.builds(
    titan_DataType,
    type=
        safe_text
)
titan_Reference_strategy = st.builds(
    titan_Reference,
    unique=
        st.booleans()
)
DataType_strategy = st.builds(
    DataType,
)
titan_SingleDataType_strategy = st.builds(
    titan_SingleDataType,
)
titan_MultiDataType_strategy = st.builds(
    titan_MultiDataType,
    unique=
        st.booleans()
)
titan_Feature_strategy = st.builds(
    titan_Feature,
    name=
        safe_text
)
titan_Entity_strategy = st.builds(
    titan_Entity,
    name=
        safe_text
)
titan_Package_strategy = st.builds(
    titan_Package,
    name=
        safe_text
)
titan_Module_strategy = st.builds(
    titan_Module,
    name=
        safe_text,
    type=
        safe_text
)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=titan_SingleReference_strategy)
@settings(max_examples=50)
def test_titan_singlereference_instantiation(instance):
    assert isinstance(instance, titan_SingleReference)

@given(instance=titan_MultiReference_strategy)
@settings(max_examples=50)
def test_titan_multireference_instantiation(instance):
    assert isinstance(instance, titan_MultiReference)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=titan_DataType_strategy)
@settings(max_examples=50)
def test_titan_datatype_instantiation(instance):
    assert isinstance(instance, titan_DataType)



@given(instance=titan_DataType_strategy)
def test_titan_datatype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=titan_Reference_strategy)
@settings(max_examples=50)
def test_titan_reference_instantiation(instance):
    assert isinstance(instance, titan_Reference)



@given(instance=titan_Reference_strategy)
def test_titan_reference_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=titan_SingleDataType_strategy)
@settings(max_examples=50)
def test_titan_singledatatype_instantiation(instance):
    assert isinstance(instance, titan_SingleDataType)

@given(instance=titan_MultiDataType_strategy)
@settings(max_examples=50)
def test_titan_multidatatype_instantiation(instance):
    assert isinstance(instance, titan_MultiDataType)



@given(instance=titan_MultiDataType_strategy)
def test_titan_multidatatype_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=titan_Feature_strategy)
@settings(max_examples=50)
def test_titan_feature_instantiation(instance):
    assert isinstance(instance, titan_Feature)



@given(instance=titan_Feature_strategy)
def test_titan_feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=titan_Entity_strategy)
@settings(max_examples=50)
def test_titan_entity_instantiation(instance):
    assert isinstance(instance, titan_Entity)



@given(instance=titan_Entity_strategy)
def test_titan_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=titan_Package_strategy)
@settings(max_examples=50)
def test_titan_package_instantiation(instance):
    assert isinstance(instance, titan_Package)



@given(instance=titan_Package_strategy)
def test_titan_package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=titan_Module_strategy)
@settings(max_examples=50)
def test_titan_module_instantiation(instance):
    assert isinstance(instance, titan_Module)



@given(instance=titan_Module_strategy)
def test_titan_module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=titan_Module_strategy)
def test_titan_module_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original
