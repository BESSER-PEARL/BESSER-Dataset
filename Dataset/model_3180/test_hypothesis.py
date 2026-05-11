import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    rell::Conditions,
    Expression,
    rell::Plus,
    rell::IntConstant,
    rell::Equality,
    rell::And,
    rell::MulOrDiv,
    rell::Comparison,
    rell::StringConstant,
    rell::VariableRef,
    rell::Not,
    rell::BoolConstant,
    rell::Minus,
    rell::Or,
    rell::ClassType,
    rell::PrimitiveType,
    rell::TypeReference,
    rell::ConditionElement,
    Relational,
    rell::Create,
    rell::Delete,
    rell::Update,
    rell::Expression,
    rell::VariableDeclaration,
    Statement,
    rell::Relational,
    rell::VariableInit,
    rell::Variable,
    rell::Statement,
    rell::RelAttrubutesList,
    rell::Attribute,
    rell::Operation,
    rell::ClassDefinition,
    rell::Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rell::conditions_is_not_abstract():
    assert not inspect.isabstract(rell::Conditions)


def test_rell::conditions_constructor_exists():
    assert callable(rell::Conditions.__init__)


def test_rell::conditions_constructor_args():
    sig = inspect.signature(rell::Conditions.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_rell::plus_is_not_abstract():
    assert not inspect.isabstract(rell::Plus)


def test_rell::plus_constructor_exists():
    assert callable(rell::Plus.__init__)


def test_rell::plus_constructor_args():
    sig = inspect.signature(rell::Plus.__init__)
    params = list(sig.parameters.keys())



def test_rell::intconstant_is_not_abstract():
    assert not inspect.isabstract(rell::IntConstant)


def test_rell::intconstant_constructor_exists():
    assert callable(rell::IntConstant.__init__)


def test_rell::intconstant_constructor_args():
    sig = inspect.signature(rell::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rell::intconstant_has_value():
    assert hasattr(rell::IntConstant, "value")
    descriptor = None
    for klass in rell::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rell::equality_is_not_abstract():
    assert not inspect.isabstract(rell::Equality)


def test_rell::equality_constructor_exists():
    assert callable(rell::Equality.__init__)


def test_rell::equality_constructor_args():
    sig = inspect.signature(rell::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rell::equality_has_op():
    assert hasattr(rell::Equality, "op")
    descriptor = None
    for klass in rell::Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rell::and_is_not_abstract():
    assert not inspect.isabstract(rell::And)


def test_rell::and_constructor_exists():
    assert callable(rell::And.__init__)


def test_rell::and_constructor_args():
    sig = inspect.signature(rell::And.__init__)
    params = list(sig.parameters.keys())



def test_rell::mulordiv_is_not_abstract():
    assert not inspect.isabstract(rell::MulOrDiv)


def test_rell::mulordiv_constructor_exists():
    assert callable(rell::MulOrDiv.__init__)


def test_rell::mulordiv_constructor_args():
    sig = inspect.signature(rell::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rell::mulordiv_has_op():
    assert hasattr(rell::MulOrDiv, "op")
    descriptor = None
    for klass in rell::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rell::comparison_is_not_abstract():
    assert not inspect.isabstract(rell::Comparison)


def test_rell::comparison_constructor_exists():
    assert callable(rell::Comparison.__init__)


def test_rell::comparison_constructor_args():
    sig = inspect.signature(rell::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rell::comparison_has_op():
    assert hasattr(rell::Comparison, "op")
    descriptor = None
    for klass in rell::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rell::stringconstant_is_not_abstract():
    assert not inspect.isabstract(rell::StringConstant)


def test_rell::stringconstant_constructor_exists():
    assert callable(rell::StringConstant.__init__)


def test_rell::stringconstant_constructor_args():
    sig = inspect.signature(rell::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rell::stringconstant_has_value():
    assert hasattr(rell::StringConstant, "value")
    descriptor = None
    for klass in rell::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rell::variableref_is_not_abstract():
    assert not inspect.isabstract(rell::VariableRef)


def test_rell::variableref_constructor_exists():
    assert callable(rell::VariableRef.__init__)


def test_rell::variableref_constructor_args():
    sig = inspect.signature(rell::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_rell::not_is_not_abstract():
    assert not inspect.isabstract(rell::Not)


def test_rell::not_constructor_exists():
    assert callable(rell::Not.__init__)


def test_rell::not_constructor_args():
    sig = inspect.signature(rell::Not.__init__)
    params = list(sig.parameters.keys())



def test_rell::boolconstant_is_not_abstract():
    assert not inspect.isabstract(rell::BoolConstant)


def test_rell::boolconstant_constructor_exists():
    assert callable(rell::BoolConstant.__init__)


def test_rell::boolconstant_constructor_args():
    sig = inspect.signature(rell::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rell::boolconstant_has_value():
    assert hasattr(rell::BoolConstant, "value")
    descriptor = None
    for klass in rell::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rell::minus_is_not_abstract():
    assert not inspect.isabstract(rell::Minus)


def test_rell::minus_constructor_exists():
    assert callable(rell::Minus.__init__)


def test_rell::minus_constructor_args():
    sig = inspect.signature(rell::Minus.__init__)
    params = list(sig.parameters.keys())



def test_rell::or_is_not_abstract():
    assert not inspect.isabstract(rell::Or)


def test_rell::or_constructor_exists():
    assert callable(rell::Or.__init__)


def test_rell::or_constructor_args():
    sig = inspect.signature(rell::Or.__init__)
    params = list(sig.parameters.keys())



def test_rell::classtype_is_not_abstract():
    assert not inspect.isabstract(rell::ClassType)


def test_rell::classtype_constructor_exists():
    assert callable(rell::ClassType.__init__)


def test_rell::classtype_constructor_args():
    sig = inspect.signature(rell::ClassType.__init__)
    params = list(sig.parameters.keys())



def test_rell::primitivetype_is_not_abstract():
    assert not inspect.isabstract(rell::PrimitiveType)


def test_rell::primitivetype_constructor_exists():
    assert callable(rell::PrimitiveType.__init__)


def test_rell::primitivetype_constructor_args():
    sig = inspect.signature(rell::PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_rell::primitivetype_has_primitiveType():
    assert hasattr(rell::PrimitiveType, "primitiveType")
    descriptor = None
    for klass in rell::PrimitiveType.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_rell::typereference_is_not_abstract():
    assert not inspect.isabstract(rell::TypeReference)


def test_rell::typereference_constructor_exists():
    assert callable(rell::TypeReference.__init__)


def test_rell::typereference_constructor_args():
    sig = inspect.signature(rell::TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_rell::conditionelement_is_not_abstract():
    assert not inspect.isabstract(rell::ConditionElement)


def test_rell::conditionelement_constructor_exists():
    assert callable(rell::ConditionElement.__init__)


def test_rell::conditionelement_constructor_args():
    sig = inspect.signature(rell::ConditionElement.__init__)
    params = list(sig.parameters.keys())
    assert "compareName" in params, "Missing parameter 'compareName'"

def test_rell::conditionelement_has_compareName():
    assert hasattr(rell::ConditionElement, "compareName")
    descriptor = None
    for klass in rell::ConditionElement.__mro__:
        if "compareName" in klass.__dict__:
            descriptor = klass.__dict__["compareName"]
            break
    assert isinstance(descriptor, property)



def test_relational_is_not_abstract():
    assert not inspect.isabstract(Relational)


def test_relational_constructor_exists():
    assert callable(Relational.__init__)


def test_relational_constructor_args():
    sig = inspect.signature(Relational.__init__)
    params = list(sig.parameters.keys())



def test_rell::create_is_not_abstract():
    assert not inspect.isabstract(rell::Create)


def test_rell::create_constructor_exists():
    assert callable(rell::Create.__init__)


def test_rell::create_constructor_args():
    sig = inspect.signature(rell::Create.__init__)
    params = list(sig.parameters.keys())



def test_rell::delete_is_not_abstract():
    assert not inspect.isabstract(rell::Delete)


def test_rell::delete_constructor_exists():
    assert callable(rell::Delete.__init__)


def test_rell::delete_constructor_args():
    sig = inspect.signature(rell::Delete.__init__)
    params = list(sig.parameters.keys())



def test_rell::update_is_not_abstract():
    assert not inspect.isabstract(rell::Update)


def test_rell::update_constructor_exists():
    assert callable(rell::Update.__init__)


def test_rell::update_constructor_args():
    sig = inspect.signature(rell::Update.__init__)
    params = list(sig.parameters.keys())



def test_rell::expression_is_not_abstract():
    assert not inspect.isabstract(rell::Expression)


def test_rell::expression_constructor_exists():
    assert callable(rell::Expression.__init__)


def test_rell::expression_constructor_args():
    sig = inspect.signature(rell::Expression.__init__)
    params = list(sig.parameters.keys())



def test_rell::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(rell::VariableDeclaration)


def test_rell::variabledeclaration_constructor_exists():
    assert callable(rell::VariableDeclaration.__init__)


def test_rell::variabledeclaration_constructor_args():
    sig = inspect.signature(rell::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rell::variabledeclaration_has_name():
    assert hasattr(rell::VariableDeclaration, "name")
    descriptor = None
    for klass in rell::VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_rell::relational_is_not_abstract():
    assert not inspect.isabstract(rell::Relational)


def test_rell::relational_constructor_exists():
    assert callable(rell::Relational.__init__)


def test_rell::relational_constructor_args():
    sig = inspect.signature(rell::Relational.__init__)
    params = list(sig.parameters.keys())
    assert "entity" in params, "Missing parameter 'entity'"

def test_rell::relational_has_entity():
    assert hasattr(rell::Relational, "entity")
    descriptor = None
    for klass in rell::Relational.__mro__:
        if "entity" in klass.__dict__:
            descriptor = klass.__dict__["entity"]
            break
    assert isinstance(descriptor, property)



def test_rell::variableinit_is_not_abstract():
    assert not inspect.isabstract(rell::VariableInit)


def test_rell::variableinit_constructor_exists():
    assert callable(rell::VariableInit.__init__)


def test_rell::variableinit_constructor_args():
    sig = inspect.signature(rell::VariableInit.__init__)
    params = list(sig.parameters.keys())



def test_rell::variable_is_not_abstract():
    assert not inspect.isabstract(rell::Variable)


def test_rell::variable_constructor_exists():
    assert callable(rell::Variable.__init__)


def test_rell::variable_constructor_args():
    sig = inspect.signature(rell::Variable.__init__)
    params = list(sig.parameters.keys())



def test_rell::statement_is_not_abstract():
    assert not inspect.isabstract(rell::Statement)


def test_rell::statement_constructor_exists():
    assert callable(rell::Statement.__init__)


def test_rell::statement_constructor_args():
    sig = inspect.signature(rell::Statement.__init__)
    params = list(sig.parameters.keys())



def test_rell::relattrubuteslist_is_not_abstract():
    assert not inspect.isabstract(rell::RelAttrubutesList)


def test_rell::relattrubuteslist_constructor_exists():
    assert callable(rell::RelAttrubutesList.__init__)


def test_rell::relattrubuteslist_constructor_args():
    sig = inspect.signature(rell::RelAttrubutesList.__init__)
    params = list(sig.parameters.keys())



def test_rell::attribute_is_not_abstract():
    assert not inspect.isabstract(rell::Attribute)


def test_rell::attribute_constructor_exists():
    assert callable(rell::Attribute.__init__)


def test_rell::attribute_constructor_args():
    sig = inspect.signature(rell::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "modificator" in params, "Missing parameter 'modificator'"

def test_rell::attribute_has_modificator():
    assert hasattr(rell::Attribute, "modificator")
    descriptor = None
    for klass in rell::Attribute.__mro__:
        if "modificator" in klass.__dict__:
            descriptor = klass.__dict__["modificator"]
            break
    assert isinstance(descriptor, property)



def test_rell::operation_is_not_abstract():
    assert not inspect.isabstract(rell::Operation)


def test_rell::operation_constructor_exists():
    assert callable(rell::Operation.__init__)


def test_rell::operation_constructor_args():
    sig = inspect.signature(rell::Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rell::operation_has_name():
    assert hasattr(rell::Operation, "name")
    descriptor = None
    for klass in rell::Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rell::classdefinition_is_not_abstract():
    assert not inspect.isabstract(rell::ClassDefinition)


def test_rell::classdefinition_constructor_exists():
    assert callable(rell::ClassDefinition.__init__)


def test_rell::classdefinition_constructor_args():
    sig = inspect.signature(rell::ClassDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rell::classdefinition_has_name():
    assert hasattr(rell::ClassDefinition, "name")
    descriptor = None
    for klass in rell::ClassDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rell::model_is_not_abstract():
    assert not inspect.isabstract(rell::Model)


def test_rell::model_constructor_exists():
    assert callable(rell::Model.__init__)


def test_rell::model_constructor_args():
    sig = inspect.signature(rell::Model.__init__)
    params = list(sig.parameters.keys())


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
rell::Conditions_strategy = st.builds(
    rell::Conditions,
)
Expression_strategy = st.builds(
    Expression,
)
rell::Plus_strategy = st.builds(
    rell::Plus,
)
rell::IntConstant_strategy = st.builds(
    rell::IntConstant,
    value=
        st.integers()
)
rell::Equality_strategy = st.builds(
    rell::Equality,
    op=
        safe_text
)
rell::And_strategy = st.builds(
    rell::And,
)
rell::MulOrDiv_strategy = st.builds(
    rell::MulOrDiv,
    op=
        safe_text
)
rell::Comparison_strategy = st.builds(
    rell::Comparison,
    op=
        safe_text
)
rell::StringConstant_strategy = st.builds(
    rell::StringConstant,
    value=
        safe_text
)
rell::VariableRef_strategy = st.builds(
    rell::VariableRef,
)
rell::Not_strategy = st.builds(
    rell::Not,
)
rell::BoolConstant_strategy = st.builds(
    rell::BoolConstant,
    value=
        safe_text
)
rell::Minus_strategy = st.builds(
    rell::Minus,
)
rell::Or_strategy = st.builds(
    rell::Or,
)
rell::ClassType_strategy = st.builds(
    rell::ClassType,
)
rell::PrimitiveType_strategy = st.builds(
    rell::PrimitiveType,
    primitiveType=
        safe_text
)
rell::TypeReference_strategy = st.builds(
    rell::TypeReference,
)
rell::ConditionElement_strategy = st.builds(
    rell::ConditionElement,
    compareName=
        safe_text
)
Relational_strategy = st.builds(
    Relational,
)
rell::Create_strategy = st.builds(
    rell::Create,
)
rell::Delete_strategy = st.builds(
    rell::Delete,
)
rell::Update_strategy = st.builds(
    rell::Update,
)
rell::Expression_strategy = st.builds(
    rell::Expression,
)
rell::VariableDeclaration_strategy = st.builds(
    rell::VariableDeclaration,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
rell::Relational_strategy = st.builds(
    rell::Relational,
    entity=
        safe_text
)
rell::VariableInit_strategy = st.builds(
    rell::VariableInit,
)
rell::Variable_strategy = st.builds(
    rell::Variable,
)
rell::Statement_strategy = st.builds(
    rell::Statement,
)
rell::RelAttrubutesList_strategy = st.builds(
    rell::RelAttrubutesList,
)
rell::Attribute_strategy = st.builds(
    rell::Attribute,
    modificator=
        safe_text
)
rell::Operation_strategy = st.builds(
    rell::Operation,
    name=
        safe_text
)
rell::ClassDefinition_strategy = st.builds(
    rell::ClassDefinition,
    name=
        safe_text
)
rell::Model_strategy = st.builds(
    rell::Model,
)

@given(instance=rell::Conditions_strategy)
@settings(max_examples=50)
def test_rell::conditions_instantiation(instance):
    assert isinstance(instance, rell::Conditions)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=rell::Plus_strategy)
@settings(max_examples=50)
def test_rell::plus_instantiation(instance):
    assert isinstance(instance, rell::Plus)

@given(instance=rell::IntConstant_strategy)
@settings(max_examples=50)
def test_rell::intconstant_instantiation(instance):
    assert isinstance(instance, rell::IntConstant)

@given(instance=rell::IntConstant_strategy)
def test_rell::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=rell::IntConstant_strategy)
def test_rell::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rell::Equality_strategy)
@settings(max_examples=50)
def test_rell::equality_instantiation(instance):
    assert isinstance(instance, rell::Equality)

@given(instance=rell::Equality_strategy)
def test_rell::equality_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=rell::Equality_strategy)
def test_rell::equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=rell::And_strategy)
@settings(max_examples=50)
def test_rell::and_instantiation(instance):
    assert isinstance(instance, rell::And)

@given(instance=rell::MulOrDiv_strategy)
@settings(max_examples=50)
def test_rell::mulordiv_instantiation(instance):
    assert isinstance(instance, rell::MulOrDiv)

@given(instance=rell::MulOrDiv_strategy)
def test_rell::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=rell::MulOrDiv_strategy)
def test_rell::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=rell::Comparison_strategy)
@settings(max_examples=50)
def test_rell::comparison_instantiation(instance):
    assert isinstance(instance, rell::Comparison)

@given(instance=rell::Comparison_strategy)
def test_rell::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=rell::Comparison_strategy)
def test_rell::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=rell::StringConstant_strategy)
@settings(max_examples=50)
def test_rell::stringconstant_instantiation(instance):
    assert isinstance(instance, rell::StringConstant)

@given(instance=rell::StringConstant_strategy)
def test_rell::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=rell::StringConstant_strategy)
def test_rell::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rell::VariableRef_strategy)
@settings(max_examples=50)
def test_rell::variableref_instantiation(instance):
    assert isinstance(instance, rell::VariableRef)

@given(instance=rell::Not_strategy)
@settings(max_examples=50)
def test_rell::not_instantiation(instance):
    assert isinstance(instance, rell::Not)

@given(instance=rell::BoolConstant_strategy)
@settings(max_examples=50)
def test_rell::boolconstant_instantiation(instance):
    assert isinstance(instance, rell::BoolConstant)

@given(instance=rell::BoolConstant_strategy)
def test_rell::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=rell::BoolConstant_strategy)
def test_rell::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rell::Minus_strategy)
@settings(max_examples=50)
def test_rell::minus_instantiation(instance):
    assert isinstance(instance, rell::Minus)

@given(instance=rell::Or_strategy)
@settings(max_examples=50)
def test_rell::or_instantiation(instance):
    assert isinstance(instance, rell::Or)

@given(instance=rell::ClassType_strategy)
@settings(max_examples=50)
def test_rell::classtype_instantiation(instance):
    assert isinstance(instance, rell::ClassType)

@given(instance=rell::PrimitiveType_strategy)
@settings(max_examples=50)
def test_rell::primitivetype_instantiation(instance):
    assert isinstance(instance, rell::PrimitiveType)

@given(instance=rell::PrimitiveType_strategy)
def test_rell::primitivetype_primitiveType_type(instance):
    assert isinstance(instance.primitiveType, str)


@given(instance=rell::PrimitiveType_strategy)
def test_rell::primitivetype_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=rell::TypeReference_strategy)
@settings(max_examples=50)
def test_rell::typereference_instantiation(instance):
    assert isinstance(instance, rell::TypeReference)

@given(instance=rell::ConditionElement_strategy)
@settings(max_examples=50)
def test_rell::conditionelement_instantiation(instance):
    assert isinstance(instance, rell::ConditionElement)

@given(instance=rell::ConditionElement_strategy)
def test_rell::conditionelement_compareName_type(instance):
    assert isinstance(instance.compareName, str)


@given(instance=rell::ConditionElement_strategy)
def test_rell::conditionelement_compareName_setter(instance):
    original = instance.compareName
    instance.compareName = original
    assert instance.compareName == original

@given(instance=Relational_strategy)
@settings(max_examples=50)
def test_relational_instantiation(instance):
    assert isinstance(instance, Relational)

@given(instance=rell::Create_strategy)
@settings(max_examples=50)
def test_rell::create_instantiation(instance):
    assert isinstance(instance, rell::Create)

@given(instance=rell::Delete_strategy)
@settings(max_examples=50)
def test_rell::delete_instantiation(instance):
    assert isinstance(instance, rell::Delete)

@given(instance=rell::Update_strategy)
@settings(max_examples=50)
def test_rell::update_instantiation(instance):
    assert isinstance(instance, rell::Update)

@given(instance=rell::Expression_strategy)
@settings(max_examples=50)
def test_rell::expression_instantiation(instance):
    assert isinstance(instance, rell::Expression)

@given(instance=rell::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_rell::variabledeclaration_instantiation(instance):
    assert isinstance(instance, rell::VariableDeclaration)

@given(instance=rell::VariableDeclaration_strategy)
def test_rell::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rell::VariableDeclaration_strategy)
def test_rell::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=rell::Relational_strategy)
@settings(max_examples=50)
def test_rell::relational_instantiation(instance):
    assert isinstance(instance, rell::Relational)

@given(instance=rell::Relational_strategy)
def test_rell::relational_entity_type(instance):
    assert isinstance(instance.entity, str)


@given(instance=rell::Relational_strategy)
def test_rell::relational_entity_setter(instance):
    original = instance.entity
    instance.entity = original
    assert instance.entity == original

@given(instance=rell::VariableInit_strategy)
@settings(max_examples=50)
def test_rell::variableinit_instantiation(instance):
    assert isinstance(instance, rell::VariableInit)

@given(instance=rell::Variable_strategy)
@settings(max_examples=50)
def test_rell::variable_instantiation(instance):
    assert isinstance(instance, rell::Variable)

@given(instance=rell::Statement_strategy)
@settings(max_examples=50)
def test_rell::statement_instantiation(instance):
    assert isinstance(instance, rell::Statement)

@given(instance=rell::RelAttrubutesList_strategy)
@settings(max_examples=50)
def test_rell::relattrubuteslist_instantiation(instance):
    assert isinstance(instance, rell::RelAttrubutesList)

@given(instance=rell::Attribute_strategy)
@settings(max_examples=50)
def test_rell::attribute_instantiation(instance):
    assert isinstance(instance, rell::Attribute)

@given(instance=rell::Attribute_strategy)
def test_rell::attribute_modificator_type(instance):
    assert isinstance(instance.modificator, str)


@given(instance=rell::Attribute_strategy)
def test_rell::attribute_modificator_setter(instance):
    original = instance.modificator
    instance.modificator = original
    assert instance.modificator == original

@given(instance=rell::Operation_strategy)
@settings(max_examples=50)
def test_rell::operation_instantiation(instance):
    assert isinstance(instance, rell::Operation)

@given(instance=rell::Operation_strategy)
def test_rell::operation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rell::Operation_strategy)
def test_rell::operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rell::ClassDefinition_strategy)
@settings(max_examples=50)
def test_rell::classdefinition_instantiation(instance):
    assert isinstance(instance, rell::ClassDefinition)

@given(instance=rell::ClassDefinition_strategy)
def test_rell::classdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=rell::ClassDefinition_strategy)
def test_rell::classdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rell::Model_strategy)
@settings(max_examples=50)
def test_rell::model_instantiation(instance):
    assert isinstance(instance, rell::Model)
