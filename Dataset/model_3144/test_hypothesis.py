import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    USE::Role,
    USE::Literal,
    USE::Type,
    USE::Association,
    USE::Enumeration,
    USE::Model,
    USE::OCLExpression,
    USE::Operation,
    USE::Attribute,
    Type,
    USE::CollectionType,
    USE::SimpleType,
    USE::ReferenceType,
    USE::EnumerationType,
    USE::Class,
    USE::Parameter,
    SimpleTypes,
    AssocKind,
    CollectionTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_use::role_is_not_abstract():
    assert not inspect.isabstract(USE::Role)


def test_use::role_constructor_exists():
    assert callable(USE::Role.__init__)


def test_use::role_constructor_args():
    sig = inspect.signature(USE::Role.__init__)
    params = list(sig.parameters.keys())
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"
    assert "name" in params, "Missing parameter 'name'"

def test_use::role_has_ordered():
    assert hasattr(USE::Role, "ordered")
    descriptor = None
    for klass in USE::Role.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_use::role_has_lowerBound():
    assert hasattr(USE::Role, "lowerBound")
    descriptor = None
    for klass in USE::Role.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_use::role_has_upperBound():
    assert hasattr(USE::Role, "upperBound")
    descriptor = None
    for klass in USE::Role.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)

def test_use::role_has_name():
    assert hasattr(USE::Role, "name")
    descriptor = None
    for klass in USE::Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use::literal_is_not_abstract():
    assert not inspect.isabstract(USE::Literal)


def test_use::literal_constructor_exists():
    assert callable(USE::Literal.__init__)


def test_use::literal_constructor_args():
    sig = inspect.signature(USE::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use::literal_has_name():
    assert hasattr(USE::Literal, "name")
    descriptor = None
    for klass in USE::Literal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use::type_is_not_abstract():
    assert not inspect.isabstract(USE::Type)


def test_use::type_constructor_exists():
    assert callable(USE::Type.__init__)


def test_use::type_constructor_args():
    sig = inspect.signature(USE::Type.__init__)
    params = list(sig.parameters.keys())



def test_use::association_is_not_abstract():
    assert not inspect.isabstract(USE::Association)


def test_use::association_constructor_exists():
    assert callable(USE::Association.__init__)


def test_use::association_constructor_args():
    sig = inspect.signature(USE::Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_use::association_has_name():
    assert hasattr(USE::Association, "name")
    descriptor = None
    for klass in USE::Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_use::association_has_kind():
    assert hasattr(USE::Association, "kind")
    descriptor = None
    for klass in USE::Association.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_use::enumeration_is_not_abstract():
    assert not inspect.isabstract(USE::Enumeration)


def test_use::enumeration_constructor_exists():
    assert callable(USE::Enumeration.__init__)


def test_use::enumeration_constructor_args():
    sig = inspect.signature(USE::Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use::enumeration_has_name():
    assert hasattr(USE::Enumeration, "name")
    descriptor = None
    for klass in USE::Enumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use::model_is_not_abstract():
    assert not inspect.isabstract(USE::Model)


def test_use::model_constructor_exists():
    assert callable(USE::Model.__init__)


def test_use::model_constructor_args():
    sig = inspect.signature(USE::Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use::model_has_name():
    assert hasattr(USE::Model, "name")
    descriptor = None
    for klass in USE::Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use::oclexpression_is_not_abstract():
    assert not inspect.isabstract(USE::OCLExpression)


def test_use::oclexpression_constructor_exists():
    assert callable(USE::OCLExpression.__init__)


def test_use::oclexpression_constructor_args():
    sig = inspect.signature(USE::OCLExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"

def test_use::oclexpression_has_expr():
    assert hasattr(USE::OCLExpression, "expr")
    descriptor = None
    for klass in USE::OCLExpression.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_use::operation_is_not_abstract():
    assert not inspect.isabstract(USE::Operation)


def test_use::operation_constructor_exists():
    assert callable(USE::Operation.__init__)


def test_use::operation_constructor_args():
    sig = inspect.signature(USE::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use::operation_has_name():
    assert hasattr(USE::Operation, "name")
    descriptor = None
    for klass in USE::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use::attribute_is_not_abstract():
    assert not inspect.isabstract(USE::Attribute)


def test_use::attribute_constructor_exists():
    assert callable(USE::Attribute.__init__)


def test_use::attribute_constructor_args():
    sig = inspect.signature(USE::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use::attribute_has_name():
    assert hasattr(USE::Attribute, "name")
    descriptor = None
    for klass in USE::Attribute.__mro__:
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



def test_use::collectiontype_is_not_abstract():
    assert not inspect.isabstract(USE::CollectionType)


def test_use::collectiontype_constructor_exists():
    assert callable(USE::CollectionType.__init__)


def test_use::collectiontype_constructor_args():
    sig = inspect.signature(USE::CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_use::collectiontype_has_type():
    assert hasattr(USE::CollectionType, "type")
    descriptor = None
    for klass in USE::CollectionType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_use::simpletype_is_not_abstract():
    assert not inspect.isabstract(USE::SimpleType)


def test_use::simpletype_constructor_exists():
    assert callable(USE::SimpleType.__init__)


def test_use::simpletype_constructor_args():
    sig = inspect.signature(USE::SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_use::simpletype_has_type():
    assert hasattr(USE::SimpleType, "type")
    descriptor = None
    for klass in USE::SimpleType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_use::referencetype_is_not_abstract():
    assert not inspect.isabstract(USE::ReferenceType)


def test_use::referencetype_constructor_exists():
    assert callable(USE::ReferenceType.__init__)


def test_use::referencetype_constructor_args():
    sig = inspect.signature(USE::ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_use::enumerationtype_is_not_abstract():
    assert not inspect.isabstract(USE::EnumerationType)


def test_use::enumerationtype_constructor_exists():
    assert callable(USE::EnumerationType.__init__)


def test_use::enumerationtype_constructor_args():
    sig = inspect.signature(USE::EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_use::class_is_not_abstract():
    assert not inspect.isabstract(USE::Class)


def test_use::class_constructor_exists():
    assert callable(USE::Class.__init__)


def test_use::class_constructor_args():
    sig = inspect.signature(USE::Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_use::class_has_name():
    assert hasattr(USE::Class, "name")
    descriptor = None
    for klass in USE::Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_use::class_has_abstract():
    assert hasattr(USE::Class, "abstract")
    descriptor = None
    for klass in USE::Class.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)



def test_use::parameter_is_not_abstract():
    assert not inspect.isabstract(USE::Parameter)


def test_use::parameter_constructor_exists():
    assert callable(USE::Parameter.__init__)


def test_use::parameter_constructor_args():
    sig = inspect.signature(USE::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use::parameter_has_name():
    assert hasattr(USE::Parameter, "name")
    descriptor = None
    for klass in USE::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_simpletypes_exists():
    # Check that the Enumeration exists
    assert SimpleTypes is not None

def test_simpletypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleTypes]
    expected_literals = [
        "Boolean",
        "Integer",
        "String",
        "Real",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleTypes"

def test_assockind_exists():
    # Check that the Enumeration exists
    assert AssocKind is not None

def test_assockind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssocKind]
    expected_literals = [
        "Association",
        "Aggregation",
        "Composition",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssocKind"

def test_collectiontypes_exists():
    # Check that the Enumeration exists
    assert CollectionTypes is not None

def test_collectiontypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CollectionTypes]
    expected_literals = [
        "Sequence",
        "Set",
        "Bag",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionTypes"


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
USE::Role_strategy = st.builds(
    USE::Role,
    ordered=
        st.booleans(),
    lowerBound=
        st.integers(),
    upperBound=
        st.integers(),
    name=
        safe_text
)
USE::Literal_strategy = st.builds(
    USE::Literal,
    name=
        safe_text
)
USE::Type_strategy = st.builds(
    USE::Type,
)
USE::Association_strategy = st.builds(
    USE::Association,
    name=
        safe_text,
    kind=
        safe_text
)
USE::Enumeration_strategy = st.builds(
    USE::Enumeration,
    name=
        safe_text
)
USE::Model_strategy = st.builds(
    USE::Model,
    name=
        safe_text
)
USE::OCLExpression_strategy = st.builds(
    USE::OCLExpression,
    expr=
        safe_text
)
USE::Operation_strategy = st.builds(
    USE::Operation,
    name=
        safe_text
)
USE::Attribute_strategy = st.builds(
    USE::Attribute,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
USE::CollectionType_strategy = st.builds(
    USE::CollectionType,
    type=
        safe_text
)
USE::SimpleType_strategy = st.builds(
    USE::SimpleType,
    type=
        safe_text
)
USE::ReferenceType_strategy = st.builds(
    USE::ReferenceType,
)
USE::EnumerationType_strategy = st.builds(
    USE::EnumerationType,
)
USE::Class_strategy = st.builds(
    USE::Class,
    name=
        safe_text,
    abstract=
        st.booleans()
)
USE::Parameter_strategy = st.builds(
    USE::Parameter,
    name=
        safe_text
)

@given(instance=USE::Role_strategy)
@settings(max_examples=50)
def test_use::role_instantiation(instance):
    assert isinstance(instance, USE::Role)

@given(instance=USE::Role_strategy)
def test_use::role_ordered_type(instance):
    assert isinstance(instance.ordered, bool)


@given(instance=USE::Role_strategy)
def test_use::role_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original

@given(instance=USE::Role_strategy)
def test_use::role_lowerBound_type(instance):
    assert isinstance(instance.lowerBound, int)


@given(instance=USE::Role_strategy)
def test_use::role_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original

@given(instance=USE::Role_strategy)
def test_use::role_upperBound_type(instance):
    assert isinstance(instance.upperBound, int)


@given(instance=USE::Role_strategy)
def test_use::role_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=USE::Role_strategy)
def test_use::role_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Role_strategy)
def test_use::role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE::Literal_strategy)
@settings(max_examples=50)
def test_use::literal_instantiation(instance):
    assert isinstance(instance, USE::Literal)

@given(instance=USE::Literal_strategy)
def test_use::literal_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Literal_strategy)
def test_use::literal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE::Type_strategy)
@settings(max_examples=50)
def test_use::type_instantiation(instance):
    assert isinstance(instance, USE::Type)

@given(instance=USE::Association_strategy)
@settings(max_examples=50)
def test_use::association_instantiation(instance):
    assert isinstance(instance, USE::Association)

@given(instance=USE::Association_strategy)
def test_use::association_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Association_strategy)
def test_use::association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE::Association_strategy)
def test_use::association_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=USE::Association_strategy)
def test_use::association_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=USE::Enumeration_strategy)
@settings(max_examples=50)
def test_use::enumeration_instantiation(instance):
    assert isinstance(instance, USE::Enumeration)

@given(instance=USE::Enumeration_strategy)
def test_use::enumeration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Enumeration_strategy)
def test_use::enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE::Model_strategy)
@settings(max_examples=50)
def test_use::model_instantiation(instance):
    assert isinstance(instance, USE::Model)

@given(instance=USE::Model_strategy)
def test_use::model_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Model_strategy)
def test_use::model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE::OCLExpression_strategy)
@settings(max_examples=50)
def test_use::oclexpression_instantiation(instance):
    assert isinstance(instance, USE::OCLExpression)

@given(instance=USE::OCLExpression_strategy)
def test_use::oclexpression_expr_type(instance):
    assert isinstance(instance.expr, str)


@given(instance=USE::OCLExpression_strategy)
def test_use::oclexpression_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=USE::Operation_strategy)
@settings(max_examples=50)
def test_use::operation_instantiation(instance):
    assert isinstance(instance, USE::Operation)

@given(instance=USE::Operation_strategy)
def test_use::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Operation_strategy)
def test_use::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE::Attribute_strategy)
@settings(max_examples=50)
def test_use::attribute_instantiation(instance):
    assert isinstance(instance, USE::Attribute)

@given(instance=USE::Attribute_strategy)
def test_use::attribute_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Attribute_strategy)
def test_use::attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=USE::CollectionType_strategy)
@settings(max_examples=50)
def test_use::collectiontype_instantiation(instance):
    assert isinstance(instance, USE::CollectionType)

@given(instance=USE::CollectionType_strategy)
def test_use::collectiontype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=USE::CollectionType_strategy)
def test_use::collectiontype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=USE::SimpleType_strategy)
@settings(max_examples=50)
def test_use::simpletype_instantiation(instance):
    assert isinstance(instance, USE::SimpleType)

@given(instance=USE::SimpleType_strategy)
def test_use::simpletype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=USE::SimpleType_strategy)
def test_use::simpletype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=USE::ReferenceType_strategy)
@settings(max_examples=50)
def test_use::referencetype_instantiation(instance):
    assert isinstance(instance, USE::ReferenceType)

@given(instance=USE::EnumerationType_strategy)
@settings(max_examples=50)
def test_use::enumerationtype_instantiation(instance):
    assert isinstance(instance, USE::EnumerationType)

@given(instance=USE::Class_strategy)
@settings(max_examples=50)
def test_use::class_instantiation(instance):
    assert isinstance(instance, USE::Class)

@given(instance=USE::Class_strategy)
def test_use::class_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Class_strategy)
def test_use::class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE::Class_strategy)
def test_use::class_abstract_type(instance):
    assert isinstance(instance.abstract, bool)


@given(instance=USE::Class_strategy)
def test_use::class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original

@given(instance=USE::Parameter_strategy)
@settings(max_examples=50)
def test_use::parameter_instantiation(instance):
    assert isinstance(instance, USE::Parameter)

@given(instance=USE::Parameter_strategy)
def test_use::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=USE::Parameter_strategy)
def test_use::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
