import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    USE_Literal,
    USE_Role,
    USE_Association,
    USE_Enumeration,
    USE_Model,
    USE_OCLExpression,
    USE_Operation,
    USE_Attribute,
    Type,
    USE_ReferenceType,
    USE_CollectionType,
    USE_SimpleType,
    USE_EnumerationType,
    USE_Parameter,
    USE_Type,
    USE_Class,
    AssocKind,
    CollectionTypes,
    SimpleTypes,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_use_literal_is_not_abstract():
    assert not inspect.isabstract(USE_Literal)


def test_use_literal_constructor_exists():
    assert callable(USE_Literal.__init__)


def test_use_literal_constructor_args():
    sig = inspect.signature(USE_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use_literal_has_name():
    assert hasattr(USE_Literal, "name")
    descriptor = None
    for klass in USE_Literal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use_role_is_not_abstract():
    assert not inspect.isabstract(USE_Role)


def test_use_role_constructor_exists():
    assert callable(USE_Role.__init__)


def test_use_role_constructor_args():
    sig = inspect.signature(USE_Role.__init__)
    params = list(sig.parameters.keys())
    assert "lowerBound" in params, "Missing parameter 'lowerBound'"
    assert "ordered" in params, "Missing parameter 'ordered'"
    assert "name" in params, "Missing parameter 'name'"
    assert "upperBound" in params, "Missing parameter 'upperBound'"

def test_use_role_has_lowerBound():
    assert hasattr(USE_Role, "lowerBound")
    descriptor = None
    for klass in USE_Role.__mro__:
        if "lowerBound" in klass.__dict__:
            descriptor = klass.__dict__["lowerBound"]
            break
    assert isinstance(descriptor, property)

def test_use_role_has_ordered():
    assert hasattr(USE_Role, "ordered")
    descriptor = None
    for klass in USE_Role.__mro__:
        if "ordered" in klass.__dict__:
            descriptor = klass.__dict__["ordered"]
            break
    assert isinstance(descriptor, property)

def test_use_role_has_name():
    assert hasattr(USE_Role, "name")
    descriptor = None
    for klass in USE_Role.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_use_role_has_upperBound():
    assert hasattr(USE_Role, "upperBound")
    descriptor = None
    for klass in USE_Role.__mro__:
        if "upperBound" in klass.__dict__:
            descriptor = klass.__dict__["upperBound"]
            break
    assert isinstance(descriptor, property)



def test_use_association_is_not_abstract():
    assert not inspect.isabstract(USE_Association)


def test_use_association_constructor_exists():
    assert callable(USE_Association.__init__)


def test_use_association_constructor_args():
    sig = inspect.signature(USE_Association.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_use_association_has_name():
    assert hasattr(USE_Association, "name")
    descriptor = None
    for klass in USE_Association.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_use_association_has_kind():
    assert hasattr(USE_Association, "kind")
    descriptor = None
    for klass in USE_Association.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_use_enumeration_is_not_abstract():
    assert not inspect.isabstract(USE_Enumeration)


def test_use_enumeration_constructor_exists():
    assert callable(USE_Enumeration.__init__)


def test_use_enumeration_constructor_args():
    sig = inspect.signature(USE_Enumeration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use_enumeration_has_name():
    assert hasattr(USE_Enumeration, "name")
    descriptor = None
    for klass in USE_Enumeration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use_model_is_not_abstract():
    assert not inspect.isabstract(USE_Model)


def test_use_model_constructor_exists():
    assert callable(USE_Model.__init__)


def test_use_model_constructor_args():
    sig = inspect.signature(USE_Model.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use_model_has_name():
    assert hasattr(USE_Model, "name")
    descriptor = None
    for klass in USE_Model.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use_oclexpression_is_not_abstract():
    assert not inspect.isabstract(USE_OCLExpression)


def test_use_oclexpression_constructor_exists():
    assert callable(USE_OCLExpression.__init__)


def test_use_oclexpression_constructor_args():
    sig = inspect.signature(USE_OCLExpression.__init__)
    params = list(sig.parameters.keys())
    assert "expr" in params, "Missing parameter 'expr'"

def test_use_oclexpression_has_expr():
    assert hasattr(USE_OCLExpression, "expr")
    descriptor = None
    for klass in USE_OCLExpression.__mro__:
        if "expr" in klass.__dict__:
            descriptor = klass.__dict__["expr"]
            break
    assert isinstance(descriptor, property)



def test_use_operation_is_not_abstract():
    assert not inspect.isabstract(USE_Operation)


def test_use_operation_constructor_exists():
    assert callable(USE_Operation.__init__)


def test_use_operation_constructor_args():
    sig = inspect.signature(USE_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use_operation_has_name():
    assert hasattr(USE_Operation, "name")
    descriptor = None
    for klass in USE_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use_attribute_is_not_abstract():
    assert not inspect.isabstract(USE_Attribute)


def test_use_attribute_constructor_exists():
    assert callable(USE_Attribute.__init__)


def test_use_attribute_constructor_args():
    sig = inspect.signature(USE_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use_attribute_has_name():
    assert hasattr(USE_Attribute, "name")
    descriptor = None
    for klass in USE_Attribute.__mro__:
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



def test_use_referencetype_is_not_abstract():
    assert not inspect.isabstract(USE_ReferenceType)


def test_use_referencetype_constructor_exists():
    assert callable(USE_ReferenceType.__init__)


def test_use_referencetype_constructor_args():
    sig = inspect.signature(USE_ReferenceType.__init__)
    params = list(sig.parameters.keys())



def test_use_collectiontype_is_not_abstract():
    assert not inspect.isabstract(USE_CollectionType)


def test_use_collectiontype_constructor_exists():
    assert callable(USE_CollectionType.__init__)


def test_use_collectiontype_constructor_args():
    sig = inspect.signature(USE_CollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_use_collectiontype_has_type():
    assert hasattr(USE_CollectionType, "type")
    descriptor = None
    for klass in USE_CollectionType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_use_simpletype_is_not_abstract():
    assert not inspect.isabstract(USE_SimpleType)


def test_use_simpletype_constructor_exists():
    assert callable(USE_SimpleType.__init__)


def test_use_simpletype_constructor_args():
    sig = inspect.signature(USE_SimpleType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_use_simpletype_has_type():
    assert hasattr(USE_SimpleType, "type")
    descriptor = None
    for klass in USE_SimpleType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_use_enumerationtype_is_not_abstract():
    assert not inspect.isabstract(USE_EnumerationType)


def test_use_enumerationtype_constructor_exists():
    assert callable(USE_EnumerationType.__init__)


def test_use_enumerationtype_constructor_args():
    sig = inspect.signature(USE_EnumerationType.__init__)
    params = list(sig.parameters.keys())



def test_use_parameter_is_not_abstract():
    assert not inspect.isabstract(USE_Parameter)


def test_use_parameter_constructor_exists():
    assert callable(USE_Parameter.__init__)


def test_use_parameter_constructor_args():
    sig = inspect.signature(USE_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_use_parameter_has_name():
    assert hasattr(USE_Parameter, "name")
    descriptor = None
    for klass in USE_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_use_type_is_not_abstract():
    assert not inspect.isabstract(USE_Type)


def test_use_type_constructor_exists():
    assert callable(USE_Type.__init__)


def test_use_type_constructor_args():
    sig = inspect.signature(USE_Type.__init__)
    params = list(sig.parameters.keys())



def test_use_class_is_not_abstract():
    assert not inspect.isabstract(USE_Class)


def test_use_class_constructor_exists():
    assert callable(USE_Class.__init__)


def test_use_class_constructor_args():
    sig = inspect.signature(USE_Class.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "abstract" in params, "Missing parameter 'abstract'"

def test_use_class_has_name():
    assert hasattr(USE_Class, "name")
    descriptor = None
    for klass in USE_Class.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_use_class_has_abstract():
    assert hasattr(USE_Class, "abstract")
    descriptor = None
    for klass in USE_Class.__mro__:
        if "abstract" in klass.__dict__:
            descriptor = klass.__dict__["abstract"]
            break
    assert isinstance(descriptor, property)

def test_assockind_exists():
    # Check that the Enumeration exists
    assert AssocKind is not None

def test_assockind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssocKind]
    expected_literals = [
        "Composition",
        "Association",
        "Aggregation",
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
        "Bag",
        "Sequence",
        "Set",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CollectionTypes"

def test_simpletypes_exists():
    # Check that the Enumeration exists
    assert SimpleTypes is not None

def test_simpletypes_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in SimpleTypes]
    expected_literals = [
        "Integer",
        "String",
        "Real",
        "Boolean",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in SimpleTypes"


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
USE_Literal_strategy = st.builds(
    USE_Literal,
    name=
        safe_text
)
USE_Role_strategy = st.builds(
    USE_Role,
    lowerBound=
        st.integers(),
    ordered=
        st.booleans(),
    name=
        safe_text,
    upperBound=
        st.integers()
)
USE_Association_strategy = st.builds(
    USE_Association,
    name=
        safe_text,
    kind=
        safe_text
)
USE_Enumeration_strategy = st.builds(
    USE_Enumeration,
    name=
        safe_text
)
USE_Model_strategy = st.builds(
    USE_Model,
    name=
        safe_text
)
USE_OCLExpression_strategy = st.builds(
    USE_OCLExpression,
    expr=
        safe_text
)
USE_Operation_strategy = st.builds(
    USE_Operation,
    name=
        safe_text
)
USE_Attribute_strategy = st.builds(
    USE_Attribute,
    name=
        safe_text
)
Type_strategy = st.builds(
    Type,
)
USE_ReferenceType_strategy = st.builds(
    USE_ReferenceType,
)
USE_CollectionType_strategy = st.builds(
    USE_CollectionType,
    type=
        safe_text
)
USE_SimpleType_strategy = st.builds(
    USE_SimpleType,
    type=
        safe_text
)
USE_EnumerationType_strategy = st.builds(
    USE_EnumerationType,
)
USE_Parameter_strategy = st.builds(
    USE_Parameter,
    name=
        safe_text
)
USE_Type_strategy = st.builds(
    USE_Type,
)
USE_Class_strategy = st.builds(
    USE_Class,
    name=
        safe_text,
    abstract=
        st.booleans()
)

@given(instance=USE_Literal_strategy)
@settings(max_examples=50)
def test_use_literal_instantiation(instance):
    assert isinstance(instance, USE_Literal)



@given(instance=USE_Literal_strategy)
def test_use_literal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE_Role_strategy)
@settings(max_examples=50)
def test_use_role_instantiation(instance):
    assert isinstance(instance, USE_Role)



@given(instance=USE_Role_strategy)
def test_use_role_lowerBound_setter(instance):
    original = instance.lowerBound
    instance.lowerBound = original
    assert instance.lowerBound == original



@given(instance=USE_Role_strategy)
def test_use_role_ordered_setter(instance):
    original = instance.ordered
    instance.ordered = original
    assert instance.ordered == original



@given(instance=USE_Role_strategy)
def test_use_role_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=USE_Role_strategy)
def test_use_role_upperBound_setter(instance):
    original = instance.upperBound
    instance.upperBound = original
    assert instance.upperBound == original

@given(instance=USE_Association_strategy)
@settings(max_examples=50)
def test_use_association_instantiation(instance):
    assert isinstance(instance, USE_Association)



@given(instance=USE_Association_strategy)
def test_use_association_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=USE_Association_strategy)
def test_use_association_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=USE_Enumeration_strategy)
@settings(max_examples=50)
def test_use_enumeration_instantiation(instance):
    assert isinstance(instance, USE_Enumeration)



@given(instance=USE_Enumeration_strategy)
def test_use_enumeration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE_Model_strategy)
@settings(max_examples=50)
def test_use_model_instantiation(instance):
    assert isinstance(instance, USE_Model)



@given(instance=USE_Model_strategy)
def test_use_model_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE_OCLExpression_strategy)
@settings(max_examples=50)
def test_use_oclexpression_instantiation(instance):
    assert isinstance(instance, USE_OCLExpression)



@given(instance=USE_OCLExpression_strategy)
def test_use_oclexpression_expr_setter(instance):
    original = instance.expr
    instance.expr = original
    assert instance.expr == original

@given(instance=USE_Operation_strategy)
@settings(max_examples=50)
def test_use_operation_instantiation(instance):
    assert isinstance(instance, USE_Operation)



@given(instance=USE_Operation_strategy)
def test_use_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE_Attribute_strategy)
@settings(max_examples=50)
def test_use_attribute_instantiation(instance):
    assert isinstance(instance, USE_Attribute)



@given(instance=USE_Attribute_strategy)
def test_use_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=USE_ReferenceType_strategy)
@settings(max_examples=50)
def test_use_referencetype_instantiation(instance):
    assert isinstance(instance, USE_ReferenceType)

@given(instance=USE_CollectionType_strategy)
@settings(max_examples=50)
def test_use_collectiontype_instantiation(instance):
    assert isinstance(instance, USE_CollectionType)



@given(instance=USE_CollectionType_strategy)
def test_use_collectiontype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=USE_SimpleType_strategy)
@settings(max_examples=50)
def test_use_simpletype_instantiation(instance):
    assert isinstance(instance, USE_SimpleType)



@given(instance=USE_SimpleType_strategy)
def test_use_simpletype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=USE_EnumerationType_strategy)
@settings(max_examples=50)
def test_use_enumerationtype_instantiation(instance):
    assert isinstance(instance, USE_EnumerationType)

@given(instance=USE_Parameter_strategy)
@settings(max_examples=50)
def test_use_parameter_instantiation(instance):
    assert isinstance(instance, USE_Parameter)



@given(instance=USE_Parameter_strategy)
def test_use_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=USE_Type_strategy)
@settings(max_examples=50)
def test_use_type_instantiation(instance):
    assert isinstance(instance, USE_Type)

@given(instance=USE_Class_strategy)
@settings(max_examples=50)
def test_use_class_instantiation(instance):
    assert isinstance(instance, USE_Class)



@given(instance=USE_Class_strategy)
def test_use_class_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=USE_Class_strategy)
def test_use_class_abstract_setter(instance):
    original = instance.abstract
    instance.abstract = original
    assert instance.abstract == original
