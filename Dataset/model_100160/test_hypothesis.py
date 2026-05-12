import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    DataStructureType,
    nosql::CollectionType,
    nosql::MapType,
    Type,
    nosql::DataStructureType,
    nosql::PrimitiveType,
    nosql::Type,
    nosql::Column,
    nosql::ColumnFamily,
    ColumnFamily,
    nosql::StaticColumnFamily,
    nosql::DynamicColumnFamily,
    nosql::KeySpace,
    PrimitiveTypeType,
    ReplicaPlacementStrategies,
    CollectionTypeType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_datastructuretype_is_not_abstract():
    assert not inspect.isabstract(DataStructureType)


def test_datastructuretype_constructor_exists():
    assert callable(DataStructureType.__init__)


def test_datastructuretype_constructor_args():
    sig = inspect.signature(DataStructureType.__init__)
    params = list(sig.parameters.keys())



def test_nosql::collectiontype_is_not_abstract():
    assert not inspect.isabstract(nosql::CollectionType)


def test_nosql::collectiontype_constructor_exists():
    assert callable(nosql::CollectionType.__init__)


def test_nosql::collectiontype_constructor_args():
    sig = inspect.signature(nosql::CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"
    assert "keyType" in params, "Missing parameter 'keyType'"

def test_nosql::collectiontype_has_kind():
    assert hasattr(nosql::CollectionType, "kind")
    descriptor = None
    for klass in nosql::CollectionType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_nosql::collectiontype_has_keyType():
    assert hasattr(nosql::CollectionType, "keyType")
    descriptor = None
    for klass in nosql::CollectionType.__mro__:
        if "keyType" in klass.__dict__:
            descriptor = klass.__dict__["keyType"]
            break
    assert isinstance(descriptor, property)



def test_nosql::maptype_is_not_abstract():
    assert not inspect.isabstract(nosql::MapType)


def test_nosql::maptype_constructor_exists():
    assert callable(nosql::MapType.__init__)


def test_nosql::maptype_constructor_args():
    sig = inspect.signature(nosql::MapType.__init__)
    params = list(sig.parameters.keys())
    assert "baseType" in params, "Missing parameter 'baseType'"
    assert "keyType" in params, "Missing parameter 'keyType'"

def test_nosql::maptype_has_baseType():
    assert hasattr(nosql::MapType, "baseType")
    descriptor = None
    for klass in nosql::MapType.__mro__:
        if "baseType" in klass.__dict__:
            descriptor = klass.__dict__["baseType"]
            break
    assert isinstance(descriptor, property)

def test_nosql::maptype_has_keyType():
    assert hasattr(nosql::MapType, "keyType")
    descriptor = None
    for klass in nosql::MapType.__mro__:
        if "keyType" in klass.__dict__:
            descriptor = klass.__dict__["keyType"]
            break
    assert isinstance(descriptor, property)



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_nosql::datastructuretype_is_not_abstract():
    assert not inspect.isabstract(nosql::DataStructureType)


def test_nosql::datastructuretype_constructor_exists():
    assert callable(nosql::DataStructureType.__init__)


def test_nosql::datastructuretype_constructor_args():
    sig = inspect.signature(nosql::DataStructureType.__init__)
    params = list(sig.parameters.keys())



def test_nosql::primitivetype_is_not_abstract():
    assert not inspect.isabstract(nosql::PrimitiveType)


def test_nosql::primitivetype_constructor_exists():
    assert callable(nosql::PrimitiveType.__init__)


def test_nosql::primitivetype_constructor_args():
    sig = inspect.signature(nosql::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "kind" in params, "Missing parameter 'kind'"

def test_nosql::primitivetype_has_kind():
    assert hasattr(nosql::PrimitiveType, "kind")
    descriptor = None
    for klass in nosql::PrimitiveType.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_nosql::type_is_not_abstract():
    assert not inspect.isabstract(nosql::Type)


def test_nosql::type_constructor_exists():
    assert callable(nosql::Type.__init__)


def test_nosql::type_constructor_args():
    sig = inspect.signature(nosql::Type.__init__)
    params = list(sig.parameters.keys())



def test_nosql::column_is_not_abstract():
    assert not inspect.isabstract(nosql::Column)


def test_nosql::column_constructor_exists():
    assert callable(nosql::Column.__init__)


def test_nosql::column_constructor_args():
    sig = inspect.signature(nosql::Column.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nosql::column_has_name():
    assert hasattr(nosql::Column, "name")
    descriptor = None
    for klass in nosql::Column.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_nosql::columnfamily_is_not_abstract():
    assert not inspect.isabstract(nosql::ColumnFamily)


def test_nosql::columnfamily_constructor_exists():
    assert callable(nosql::ColumnFamily.__init__)


def test_nosql::columnfamily_constructor_args():
    sig = inspect.signature(nosql::ColumnFamily.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_nosql::columnfamily_has_name():
    assert hasattr(nosql::ColumnFamily, "name")
    descriptor = None
    for klass in nosql::ColumnFamily.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_columnfamily_is_not_abstract():
    assert not inspect.isabstract(ColumnFamily)


def test_columnfamily_constructor_exists():
    assert callable(ColumnFamily.__init__)


def test_columnfamily_constructor_args():
    sig = inspect.signature(ColumnFamily.__init__)
    params = list(sig.parameters.keys())



def test_nosql::staticcolumnfamily_is_not_abstract():
    assert not inspect.isabstract(nosql::StaticColumnFamily)


def test_nosql::staticcolumnfamily_constructor_exists():
    assert callable(nosql::StaticColumnFamily.__init__)


def test_nosql::staticcolumnfamily_constructor_args():
    sig = inspect.signature(nosql::StaticColumnFamily.__init__)
    params = list(sig.parameters.keys())



def test_nosql::dynamiccolumnfamily_is_not_abstract():
    assert not inspect.isabstract(nosql::DynamicColumnFamily)


def test_nosql::dynamiccolumnfamily_constructor_exists():
    assert callable(nosql::DynamicColumnFamily.__init__)


def test_nosql::dynamiccolumnfamily_constructor_args():
    sig = inspect.signature(nosql::DynamicColumnFamily.__init__)
    params = list(sig.parameters.keys())



def test_nosql::keyspace_is_not_abstract():
    assert not inspect.isabstract(nosql::KeySpace)


def test_nosql::keyspace_constructor_exists():
    assert callable(nosql::KeySpace.__init__)


def test_nosql::keyspace_constructor_args():
    sig = inspect.signature(nosql::KeySpace.__init__)
    params = list(sig.parameters.keys())
    assert "replicationFactor" in params, "Missing parameter 'replicationFactor'"
    assert "replicaPlacementStrategy" in params, "Missing parameter 'replicaPlacementStrategy'"
    assert "name" in params, "Missing parameter 'name'"

def test_nosql::keyspace_has_replicationFactor():
    assert hasattr(nosql::KeySpace, "replicationFactor")
    descriptor = None
    for klass in nosql::KeySpace.__mro__:
        if "replicationFactor" in klass.__dict__:
            descriptor = klass.__dict__["replicationFactor"]
            break
    assert isinstance(descriptor, property)

def test_nosql::keyspace_has_replicaPlacementStrategy():
    assert hasattr(nosql::KeySpace, "replicaPlacementStrategy")
    descriptor = None
    for klass in nosql::KeySpace.__mro__:
        if "replicaPlacementStrategy" in klass.__dict__:
            descriptor = klass.__dict__["replicaPlacementStrategy"]
            break
    assert isinstance(descriptor, property)

def test_nosql::keyspace_has_name():
    assert hasattr(nosql::KeySpace, "name")
    descriptor = None
    for klass in nosql::KeySpace.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_primitivetypetype_exists():
    # Check that the Enumeration exists
    assert PrimitiveTypeType is not None

def test_primitivetypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in PrimitiveTypeType]
    expected_literals = [
        "float",
        "int",
        "ascii",
        "varint",
        "varchar",
        "boolean",
        "decimal",
        "bigint",
        "uuid",
        "timestamp",
        "text",
        "counter",
        "timeuuid",
        "double",
        "blob",
        "inet",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in PrimitiveTypeType"

def test_replicaplacementstrategies_exists():
    # Check that the Enumeration exists
    assert ReplicaPlacementStrategies is not None

def test_replicaplacementstrategies_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ReplicaPlacementStrategies]
    expected_literals = [
        "OldNetworkTopologyStrategy",
        "SimpleStrategy",
        "NetworkTopologyStrategy",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ReplicaPlacementStrategies"

def test_collectiontypetype_exists():
    # Check that the Enumeration exists
    assert CollectionTypeType is not None

def test_collectiontypetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionTypeType]
    expected_literals = [
        "list",
        "set",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionTypeType"


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
DataStructureType_strategy = st.builds(
    DataStructureType,
)
nosql::CollectionType_strategy = st.builds(
    nosql::CollectionType,
    kind=
        safe_text,
    keyType=
        safe_text
)
nosql::MapType_strategy = st.builds(
    nosql::MapType,
    baseType=
        safe_text,
    keyType=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
nosql::DataStructureType_strategy = st.builds(
    nosql::DataStructureType,
)
nosql::PrimitiveType_strategy = st.builds(
    nosql::PrimitiveType,
    kind=
        safe_text
)
nosql::Type_strategy = st.builds(
    nosql::Type,
)
nosql::Column_strategy = st.builds(
    nosql::Column,
    name=
        safe_text
)
nosql::ColumnFamily_strategy = st.builds(
    nosql::ColumnFamily,
    name=
        safe_text
)
ColumnFamily_strategy = st.builds(
    ColumnFamily,
)
nosql::StaticColumnFamily_strategy = st.builds(
    nosql::StaticColumnFamily,
)
nosql::DynamicColumnFamily_strategy = st.builds(
    nosql::DynamicColumnFamily,
)
nosql::KeySpace_strategy = st.builds(
    nosql::KeySpace,
    replicationFactor=
        safe_text,
    replicaPlacementStrategy=
        safe_text,
    name=
        safe_text
)

@given(instance=DataStructureType_strategy)
@settings(max_examples=50)
def test_datastructuretype_instantiation(instance):
    assert isinstance(instance, DataStructureType)

@given(instance=nosql::CollectionType_strategy)
@settings(max_examples=50)
def test_nosql::collectiontype_instantiation(instance):
    assert isinstance(instance, nosql::CollectionType)

@given(instance=nosql::CollectionType_strategy)
def test_nosql::collectiontype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=nosql::CollectionType_strategy)
def test_nosql::collectiontype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=nosql::CollectionType_strategy)
def test_nosql::collectiontype_keyType_type(instance):
    assert isinstance(instance.keyType, str)


@given(instance=nosql::CollectionType_strategy)
def test_nosql::collectiontype_keyType_setter(instance):
    original = instance.keyType
    instance.keyType = original
    assert instance.keyType == original

@given(instance=nosql::MapType_strategy)
@settings(max_examples=50)
def test_nosql::maptype_instantiation(instance):
    assert isinstance(instance, nosql::MapType)

@given(instance=nosql::MapType_strategy)
def test_nosql::maptype_baseType_type(instance):
    assert isinstance(instance.baseType, str)


@given(instance=nosql::MapType_strategy)
def test_nosql::maptype_baseType_setter(instance):
    original = instance.baseType
    instance.baseType = original
    assert instance.baseType == original

@given(instance=nosql::MapType_strategy)
def test_nosql::maptype_keyType_type(instance):
    assert isinstance(instance.keyType, str)


@given(instance=nosql::MapType_strategy)
def test_nosql::maptype_keyType_setter(instance):
    original = instance.keyType
    instance.keyType = original
    assert instance.keyType == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=nosql::DataStructureType_strategy)
@settings(max_examples=50)
def test_nosql::datastructuretype_instantiation(instance):
    assert isinstance(instance, nosql::DataStructureType)

@given(instance=nosql::PrimitiveType_strategy)
@settings(max_examples=50)
def test_nosql::primitivetype_instantiation(instance):
    assert isinstance(instance, nosql::PrimitiveType)

@given(instance=nosql::PrimitiveType_strategy)
def test_nosql::primitivetype_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=nosql::PrimitiveType_strategy)
def test_nosql::primitivetype_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=nosql::Type_strategy)
@settings(max_examples=50)
def test_nosql::type_instantiation(instance):
    assert isinstance(instance, nosql::Type)

@given(instance=nosql::Column_strategy)
@settings(max_examples=50)
def test_nosql::column_instantiation(instance):
    assert isinstance(instance, nosql::Column)

@given(instance=nosql::Column_strategy)
def test_nosql::column_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nosql::Column_strategy)
def test_nosql::column_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=nosql::ColumnFamily_strategy)
@settings(max_examples=50)
def test_nosql::columnfamily_instantiation(instance):
    assert isinstance(instance, nosql::ColumnFamily)

@given(instance=nosql::ColumnFamily_strategy)
def test_nosql::columnfamily_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nosql::ColumnFamily_strategy)
def test_nosql::columnfamily_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ColumnFamily_strategy)
@settings(max_examples=50)
def test_columnfamily_instantiation(instance):
    assert isinstance(instance, ColumnFamily)

@given(instance=nosql::StaticColumnFamily_strategy)
@settings(max_examples=50)
def test_nosql::staticcolumnfamily_instantiation(instance):
    assert isinstance(instance, nosql::StaticColumnFamily)

@given(instance=nosql::DynamicColumnFamily_strategy)
@settings(max_examples=50)
def test_nosql::dynamiccolumnfamily_instantiation(instance):
    assert isinstance(instance, nosql::DynamicColumnFamily)

@given(instance=nosql::KeySpace_strategy)
@settings(max_examples=50)
def test_nosql::keyspace_instantiation(instance):
    assert isinstance(instance, nosql::KeySpace)

@given(instance=nosql::KeySpace_strategy)
def test_nosql::keyspace_replicationFactor_type(instance):
    assert isinstance(instance.replicationFactor, str)


@given(instance=nosql::KeySpace_strategy)
def test_nosql::keyspace_replicationFactor_setter(instance):
    original = instance.replicationFactor
    instance.replicationFactor = original
    assert instance.replicationFactor == original

@given(instance=nosql::KeySpace_strategy)
def test_nosql::keyspace_replicaPlacementStrategy_type(instance):
    assert isinstance(instance.replicaPlacementStrategy, str)


@given(instance=nosql::KeySpace_strategy)
def test_nosql::keyspace_replicaPlacementStrategy_setter(instance):
    original = instance.replicaPlacementStrategy
    instance.replicaPlacementStrategy = original
    assert instance.replicaPlacementStrategy == original

@given(instance=nosql::KeySpace_strategy)
def test_nosql::keyspace_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=nosql::KeySpace_strategy)
def test_nosql::keyspace_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
