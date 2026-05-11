import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Reference,
    titan::SingleReference,
    titan::MultiReference,
    Feature,
    titan::DataType,
    titan::Reference,
    DataType,
    titan::SingleDataType,
    titan::MultiDataType,
    titan::Feature,
    titan::Entity,
    titan::Package,
    titan::Module,
    DataTypes,
    InternalDSLType,
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



def test_titan::singlereference_is_not_abstract():
    assert not inspect.isabstract(titan::SingleReference)


def test_titan::singlereference_constructor_exists():
    assert callable(titan::SingleReference.__init__)


def test_titan::singlereference_constructor_args():
    sig = inspect.signature(titan::SingleReference.__init__)
    params = list(sig.parameters.keys())



def test_titan::multireference_is_not_abstract():
    assert not inspect.isabstract(titan::MultiReference)


def test_titan::multireference_constructor_exists():
    assert callable(titan::MultiReference.__init__)


def test_titan::multireference_constructor_args():
    sig = inspect.signature(titan::MultiReference.__init__)
    params = list(sig.parameters.keys())



def test_feature_is_not_abstract():
    assert not inspect.isabstract(Feature)


def test_feature_constructor_exists():
    assert callable(Feature.__init__)


def test_feature_constructor_args():
    sig = inspect.signature(Feature.__init__)
    params = list(sig.parameters.keys())



def test_titan::datatype_is_not_abstract():
    assert not inspect.isabstract(titan::DataType)


def test_titan::datatype_constructor_exists():
    assert callable(titan::DataType.__init__)


def test_titan::datatype_constructor_args():
    sig = inspect.signature(titan::DataType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_titan::datatype_has_type():
    assert hasattr(titan::DataType, "type")
    descriptor = None
    for klass in titan::DataType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_titan::reference_is_not_abstract():
    assert not inspect.isabstract(titan::Reference)


def test_titan::reference_constructor_exists():
    assert callable(titan::Reference.__init__)


def test_titan::reference_constructor_args():
    sig = inspect.signature(titan::Reference.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_titan::reference_has_unique():
    assert hasattr(titan::Reference, "unique")
    descriptor = None
    for klass in titan::Reference.__mro__:
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



def test_titan::singledatatype_is_not_abstract():
    assert not inspect.isabstract(titan::SingleDataType)


def test_titan::singledatatype_constructor_exists():
    assert callable(titan::SingleDataType.__init__)


def test_titan::singledatatype_constructor_args():
    sig = inspect.signature(titan::SingleDataType.__init__)
    params = list(sig.parameters.keys())



def test_titan::multidatatype_is_not_abstract():
    assert not inspect.isabstract(titan::MultiDataType)


def test_titan::multidatatype_constructor_exists():
    assert callable(titan::MultiDataType.__init__)


def test_titan::multidatatype_constructor_args():
    sig = inspect.signature(titan::MultiDataType.__init__)
    params = list(sig.parameters.keys())
    assert "unique" in params, "Missing parameter 'unique'"

def test_titan::multidatatype_has_unique():
    assert hasattr(titan::MultiDataType, "unique")
    descriptor = None
    for klass in titan::MultiDataType.__mro__:
        if "unique" in klass.__dict__:
            descriptor = klass.__dict__["unique"]
            break
    assert isinstance(descriptor, property)



def test_titan::feature_is_not_abstract():
    assert not inspect.isabstract(titan::Feature)


def test_titan::feature_constructor_exists():
    assert callable(titan::Feature.__init__)


def test_titan::feature_constructor_args():
    sig = inspect.signature(titan::Feature.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_titan::feature_has_name():
    assert hasattr(titan::Feature, "name")
    descriptor = None
    for klass in titan::Feature.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_titan::entity_is_not_abstract():
    assert not inspect.isabstract(titan::Entity)


def test_titan::entity_constructor_exists():
    assert callable(titan::Entity.__init__)


def test_titan::entity_constructor_args():
    sig = inspect.signature(titan::Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_titan::entity_has_name():
    assert hasattr(titan::Entity, "name")
    descriptor = None
    for klass in titan::Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_titan::package_is_not_abstract():
    assert not inspect.isabstract(titan::Package)


def test_titan::package_constructor_exists():
    assert callable(titan::Package.__init__)


def test_titan::package_constructor_args():
    sig = inspect.signature(titan::Package.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_titan::package_has_name():
    assert hasattr(titan::Package, "name")
    descriptor = None
    for klass in titan::Package.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_titan::module_is_not_abstract():
    assert not inspect.isabstract(titan::Module)


def test_titan::module_constructor_exists():
    assert callable(titan::Module.__init__)


def test_titan::module_constructor_args():
    sig = inspect.signature(titan::Module.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_titan::module_has_type():
    assert hasattr(titan::Module, "type")
    descriptor = None
    for klass in titan::Module.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_titan::module_has_name():
    assert hasattr(titan::Module, "name")
    descriptor = None
    for klass in titan::Module.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_datatypes_exists():
    # Check that the Enumeration exists
    assert DataTypes is not None

def test_datatypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DataTypes]
    expected_literals = [
        "String",
        "Boolean",
        "Long",
        "Integer",
        "Double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DataTypes"

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
titan::SingleReference_strategy = st.builds(
    titan::SingleReference,
)
titan::MultiReference_strategy = st.builds(
    titan::MultiReference,
)
Feature_strategy = st.builds(
    Feature,
)
titan::DataType_strategy = st.builds(
    titan::DataType,
    type=
        safe_text
)
titan::Reference_strategy = st.builds(
    titan::Reference,
    unique=
        st.booleans()
)
DataType_strategy = st.builds(
    DataType,
)
titan::SingleDataType_strategy = st.builds(
    titan::SingleDataType,
)
titan::MultiDataType_strategy = st.builds(
    titan::MultiDataType,
    unique=
        st.booleans()
)
titan::Feature_strategy = st.builds(
    titan::Feature,
    name=
        safe_text
)
titan::Entity_strategy = st.builds(
    titan::Entity,
    name=
        safe_text
)
titan::Package_strategy = st.builds(
    titan::Package,
    name=
        safe_text
)
titan::Module_strategy = st.builds(
    titan::Module,
    type=
        safe_text,
    name=
        safe_text
)

@given(instance=Reference_strategy)
@settings(max_examples=50)
def test_reference_instantiation(instance):
    assert isinstance(instance, Reference)

@given(instance=titan::SingleReference_strategy)
@settings(max_examples=50)
def test_titan::singlereference_instantiation(instance):
    assert isinstance(instance, titan::SingleReference)

@given(instance=titan::MultiReference_strategy)
@settings(max_examples=50)
def test_titan::multireference_instantiation(instance):
    assert isinstance(instance, titan::MultiReference)

@given(instance=Feature_strategy)
@settings(max_examples=50)
def test_feature_instantiation(instance):
    assert isinstance(instance, Feature)

@given(instance=titan::DataType_strategy)
@settings(max_examples=50)
def test_titan::datatype_instantiation(instance):
    assert isinstance(instance, titan::DataType)

@given(instance=titan::DataType_strategy)
def test_titan::datatype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=titan::DataType_strategy)
def test_titan::datatype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=titan::Reference_strategy)
@settings(max_examples=50)
def test_titan::reference_instantiation(instance):
    assert isinstance(instance, titan::Reference)

@given(instance=titan::Reference_strategy)
def test_titan::reference_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=titan::Reference_strategy)
def test_titan::reference_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=DataType_strategy)
@settings(max_examples=50)
def test_datatype_instantiation(instance):
    assert isinstance(instance, DataType)

@given(instance=titan::SingleDataType_strategy)
@settings(max_examples=50)
def test_titan::singledatatype_instantiation(instance):
    assert isinstance(instance, titan::SingleDataType)

@given(instance=titan::MultiDataType_strategy)
@settings(max_examples=50)
def test_titan::multidatatype_instantiation(instance):
    assert isinstance(instance, titan::MultiDataType)

@given(instance=titan::MultiDataType_strategy)
def test_titan::multidatatype_unique_type(instance):
    assert isinstance(instance.unique, bool)


@given(instance=titan::MultiDataType_strategy)
def test_titan::multidatatype_unique_setter(instance):
    original = instance.unique
    instance.unique = original
    assert instance.unique == original

@given(instance=titan::Feature_strategy)
@settings(max_examples=50)
def test_titan::feature_instantiation(instance):
    assert isinstance(instance, titan::Feature)

@given(instance=titan::Feature_strategy)
def test_titan::feature_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=titan::Feature_strategy)
def test_titan::feature_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=titan::Entity_strategy)
@settings(max_examples=50)
def test_titan::entity_instantiation(instance):
    assert isinstance(instance, titan::Entity)

@given(instance=titan::Entity_strategy)
def test_titan::entity_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=titan::Entity_strategy)
def test_titan::entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=titan::Package_strategy)
@settings(max_examples=50)
def test_titan::package_instantiation(instance):
    assert isinstance(instance, titan::Package)

@given(instance=titan::Package_strategy)
def test_titan::package_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=titan::Package_strategy)
def test_titan::package_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=titan::Module_strategy)
@settings(max_examples=50)
def test_titan::module_instantiation(instance):
    assert isinstance(instance, titan::Module)

@given(instance=titan::Module_strategy)
def test_titan::module_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=titan::Module_strategy)
def test_titan::module_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=titan::Module_strategy)
def test_titan::module_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=titan::Module_strategy)
def test_titan::module_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
