import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    rell_Conditions,
    Expression,
    rell_And,
    rell_Equality,
    rell_Comparison,
    rell_Plus,
    rell_Not,
    rell_VariableRef,
    rell_Minus,
    rell_BoolConstant,
    rell_StringConstant,
    rell_IntConstant,
    rell_MulOrDiv,
    rell_Or,
    rell_ClassType,
    rell_PrimitiveType,
    rell_TypeReference,
    rell_ConditionElement,
    Relational,
    rell_Delete,
    rell_Create,
    rell_Update,
    rell_Expression,
    rell_VariableDeclaration,
    Statement,
    rell_VariableInit,
    rell_Relational,
    rell_Variable,
    rell_Statement,
    rell_RelAttrubutesList,
    rell_Attribute,
    rell_Operation,
    rell_ClassDefinition,
    rell_Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_rell_conditions_is_not_abstract():
    assert not inspect.isabstract(rell_Conditions)


def test_rell_conditions_constructor_exists():
    assert callable(rell_Conditions.__init__)


def test_rell_conditions_constructor_args():
    sig = inspect.signature(rell_Conditions.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_rell_and_is_not_abstract():
    assert not inspect.isabstract(rell_And)


def test_rell_and_constructor_exists():
    assert callable(rell_And.__init__)


def test_rell_and_constructor_args():
    sig = inspect.signature(rell_And.__init__)
    params = list(sig.parameters.keys())



def test_rell_equality_is_not_abstract():
    assert not inspect.isabstract(rell_Equality)


def test_rell_equality_constructor_exists():
    assert callable(rell_Equality.__init__)


def test_rell_equality_constructor_args():
    sig = inspect.signature(rell_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rell_equality_has_op():
    assert hasattr(rell_Equality, "op")
    descriptor = None
    for klass in rell_Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rell_comparison_is_not_abstract():
    assert not inspect.isabstract(rell_Comparison)


def test_rell_comparison_constructor_exists():
    assert callable(rell_Comparison.__init__)


def test_rell_comparison_constructor_args():
    sig = inspect.signature(rell_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rell_comparison_has_op():
    assert hasattr(rell_Comparison, "op")
    descriptor = None
    for klass in rell_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rell_plus_is_not_abstract():
    assert not inspect.isabstract(rell_Plus)


def test_rell_plus_constructor_exists():
    assert callable(rell_Plus.__init__)


def test_rell_plus_constructor_args():
    sig = inspect.signature(rell_Plus.__init__)
    params = list(sig.parameters.keys())



def test_rell_not_is_not_abstract():
    assert not inspect.isabstract(rell_Not)


def test_rell_not_constructor_exists():
    assert callable(rell_Not.__init__)


def test_rell_not_constructor_args():
    sig = inspect.signature(rell_Not.__init__)
    params = list(sig.parameters.keys())



def test_rell_variableref_is_not_abstract():
    assert not inspect.isabstract(rell_VariableRef)


def test_rell_variableref_constructor_exists():
    assert callable(rell_VariableRef.__init__)


def test_rell_variableref_constructor_args():
    sig = inspect.signature(rell_VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_rell_minus_is_not_abstract():
    assert not inspect.isabstract(rell_Minus)


def test_rell_minus_constructor_exists():
    assert callable(rell_Minus.__init__)


def test_rell_minus_constructor_args():
    sig = inspect.signature(rell_Minus.__init__)
    params = list(sig.parameters.keys())



def test_rell_boolconstant_is_not_abstract():
    assert not inspect.isabstract(rell_BoolConstant)


def test_rell_boolconstant_constructor_exists():
    assert callable(rell_BoolConstant.__init__)


def test_rell_boolconstant_constructor_args():
    sig = inspect.signature(rell_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rell_boolconstant_has_value():
    assert hasattr(rell_BoolConstant, "value")
    descriptor = None
    for klass in rell_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rell_stringconstant_is_not_abstract():
    assert not inspect.isabstract(rell_StringConstant)


def test_rell_stringconstant_constructor_exists():
    assert callable(rell_StringConstant.__init__)


def test_rell_stringconstant_constructor_args():
    sig = inspect.signature(rell_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rell_stringconstant_has_value():
    assert hasattr(rell_StringConstant, "value")
    descriptor = None
    for klass in rell_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rell_intconstant_is_not_abstract():
    assert not inspect.isabstract(rell_IntConstant)


def test_rell_intconstant_constructor_exists():
    assert callable(rell_IntConstant.__init__)


def test_rell_intconstant_constructor_args():
    sig = inspect.signature(rell_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_rell_intconstant_has_value():
    assert hasattr(rell_IntConstant, "value")
    descriptor = None
    for klass in rell_IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_rell_mulordiv_is_not_abstract():
    assert not inspect.isabstract(rell_MulOrDiv)


def test_rell_mulordiv_constructor_exists():
    assert callable(rell_MulOrDiv.__init__)


def test_rell_mulordiv_constructor_args():
    sig = inspect.signature(rell_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_rell_mulordiv_has_op():
    assert hasattr(rell_MulOrDiv, "op")
    descriptor = None
    for klass in rell_MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_rell_or_is_not_abstract():
    assert not inspect.isabstract(rell_Or)


def test_rell_or_constructor_exists():
    assert callable(rell_Or.__init__)


def test_rell_or_constructor_args():
    sig = inspect.signature(rell_Or.__init__)
    params = list(sig.parameters.keys())



def test_rell_classtype_is_not_abstract():
    assert not inspect.isabstract(rell_ClassType)


def test_rell_classtype_constructor_exists():
    assert callable(rell_ClassType.__init__)


def test_rell_classtype_constructor_args():
    sig = inspect.signature(rell_ClassType.__init__)
    params = list(sig.parameters.keys())



def test_rell_primitivetype_is_not_abstract():
    assert not inspect.isabstract(rell_PrimitiveType)


def test_rell_primitivetype_constructor_exists():
    assert callable(rell_PrimitiveType.__init__)


def test_rell_primitivetype_constructor_args():
    sig = inspect.signature(rell_PrimitiveType.__init__)
    params = list(sig.parameters.keys())
    assert "primitiveType" in params, "Missing parameter 'primitiveType'"

def test_rell_primitivetype_has_primitiveType():
    assert hasattr(rell_PrimitiveType, "primitiveType")
    descriptor = None
    for klass in rell_PrimitiveType.__mro__:
        if "primitiveType" in klass.__dict__:
            descriptor = klass.__dict__["primitiveType"]
            break
    assert isinstance(descriptor, property)



def test_rell_typereference_is_not_abstract():
    assert not inspect.isabstract(rell_TypeReference)


def test_rell_typereference_constructor_exists():
    assert callable(rell_TypeReference.__init__)


def test_rell_typereference_constructor_args():
    sig = inspect.signature(rell_TypeReference.__init__)
    params = list(sig.parameters.keys())



def test_rell_conditionelement_is_not_abstract():
    assert not inspect.isabstract(rell_ConditionElement)


def test_rell_conditionelement_constructor_exists():
    assert callable(rell_ConditionElement.__init__)


def test_rell_conditionelement_constructor_args():
    sig = inspect.signature(rell_ConditionElement.__init__)
    params = list(sig.parameters.keys())
    assert "compareName" in params, "Missing parameter 'compareName'"

def test_rell_conditionelement_has_compareName():
    assert hasattr(rell_ConditionElement, "compareName")
    descriptor = None
    for klass in rell_ConditionElement.__mro__:
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



def test_rell_delete_is_not_abstract():
    assert not inspect.isabstract(rell_Delete)


def test_rell_delete_constructor_exists():
    assert callable(rell_Delete.__init__)


def test_rell_delete_constructor_args():
    sig = inspect.signature(rell_Delete.__init__)
    params = list(sig.parameters.keys())



def test_rell_create_is_not_abstract():
    assert not inspect.isabstract(rell_Create)


def test_rell_create_constructor_exists():
    assert callable(rell_Create.__init__)


def test_rell_create_constructor_args():
    sig = inspect.signature(rell_Create.__init__)
    params = list(sig.parameters.keys())



def test_rell_update_is_not_abstract():
    assert not inspect.isabstract(rell_Update)


def test_rell_update_constructor_exists():
    assert callable(rell_Update.__init__)


def test_rell_update_constructor_args():
    sig = inspect.signature(rell_Update.__init__)
    params = list(sig.parameters.keys())



def test_rell_expression_is_not_abstract():
    assert not inspect.isabstract(rell_Expression)


def test_rell_expression_constructor_exists():
    assert callable(rell_Expression.__init__)


def test_rell_expression_constructor_args():
    sig = inspect.signature(rell_Expression.__init__)
    params = list(sig.parameters.keys())



def test_rell_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(rell_VariableDeclaration)


def test_rell_variabledeclaration_constructor_exists():
    assert callable(rell_VariableDeclaration.__init__)


def test_rell_variabledeclaration_constructor_args():
    sig = inspect.signature(rell_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rell_variabledeclaration_has_name():
    assert hasattr(rell_VariableDeclaration, "name")
    descriptor = None
    for klass in rell_VariableDeclaration.__mro__:
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



def test_rell_variableinit_is_not_abstract():
    assert not inspect.isabstract(rell_VariableInit)


def test_rell_variableinit_constructor_exists():
    assert callable(rell_VariableInit.__init__)


def test_rell_variableinit_constructor_args():
    sig = inspect.signature(rell_VariableInit.__init__)
    params = list(sig.parameters.keys())



def test_rell_relational_is_not_abstract():
    assert not inspect.isabstract(rell_Relational)


def test_rell_relational_constructor_exists():
    assert callable(rell_Relational.__init__)


def test_rell_relational_constructor_args():
    sig = inspect.signature(rell_Relational.__init__)
    params = list(sig.parameters.keys())
    assert "entity" in params, "Missing parameter 'entity'"

def test_rell_relational_has_entity():
    assert hasattr(rell_Relational, "entity")
    descriptor = None
    for klass in rell_Relational.__mro__:
        if "entity" in klass.__dict__:
            descriptor = klass.__dict__["entity"]
            break
    assert isinstance(descriptor, property)



def test_rell_variable_is_not_abstract():
    assert not inspect.isabstract(rell_Variable)


def test_rell_variable_constructor_exists():
    assert callable(rell_Variable.__init__)


def test_rell_variable_constructor_args():
    sig = inspect.signature(rell_Variable.__init__)
    params = list(sig.parameters.keys())



def test_rell_statement_is_not_abstract():
    assert not inspect.isabstract(rell_Statement)


def test_rell_statement_constructor_exists():
    assert callable(rell_Statement.__init__)


def test_rell_statement_constructor_args():
    sig = inspect.signature(rell_Statement.__init__)
    params = list(sig.parameters.keys())



def test_rell_relattrubuteslist_is_not_abstract():
    assert not inspect.isabstract(rell_RelAttrubutesList)


def test_rell_relattrubuteslist_constructor_exists():
    assert callable(rell_RelAttrubutesList.__init__)


def test_rell_relattrubuteslist_constructor_args():
    sig = inspect.signature(rell_RelAttrubutesList.__init__)
    params = list(sig.parameters.keys())



def test_rell_attribute_is_not_abstract():
    assert not inspect.isabstract(rell_Attribute)


def test_rell_attribute_constructor_exists():
    assert callable(rell_Attribute.__init__)


def test_rell_attribute_constructor_args():
    sig = inspect.signature(rell_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "modificator" in params, "Missing parameter 'modificator'"

def test_rell_attribute_has_modificator():
    assert hasattr(rell_Attribute, "modificator")
    descriptor = None
    for klass in rell_Attribute.__mro__:
        if "modificator" in klass.__dict__:
            descriptor = klass.__dict__["modificator"]
            break
    assert isinstance(descriptor, property)



def test_rell_operation_is_not_abstract():
    assert not inspect.isabstract(rell_Operation)


def test_rell_operation_constructor_exists():
    assert callable(rell_Operation.__init__)


def test_rell_operation_constructor_args():
    sig = inspect.signature(rell_Operation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rell_operation_has_name():
    assert hasattr(rell_Operation, "name")
    descriptor = None
    for klass in rell_Operation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rell_classdefinition_is_not_abstract():
    assert not inspect.isabstract(rell_ClassDefinition)


def test_rell_classdefinition_constructor_exists():
    assert callable(rell_ClassDefinition.__init__)


def test_rell_classdefinition_constructor_args():
    sig = inspect.signature(rell_ClassDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_rell_classdefinition_has_name():
    assert hasattr(rell_ClassDefinition, "name")
    descriptor = None
    for klass in rell_ClassDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_rell_model_is_not_abstract():
    assert not inspect.isabstract(rell_Model)


def test_rell_model_constructor_exists():
    assert callable(rell_Model.__init__)


def test_rell_model_constructor_args():
    sig = inspect.signature(rell_Model.__init__)
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
rell_Conditions_strategy = st.builds(
    rell_Conditions,
)
Expression_strategy = st.builds(
    Expression,
)
rell_And_strategy = st.builds(
    rell_And,
)
rell_Equality_strategy = st.builds(
    rell_Equality,
    op=
        safe_text
)
rell_Comparison_strategy = st.builds(
    rell_Comparison,
    op=
        safe_text
)
rell_Plus_strategy = st.builds(
    rell_Plus,
)
rell_Not_strategy = st.builds(
    rell_Not,
)
rell_VariableRef_strategy = st.builds(
    rell_VariableRef,
)
rell_Minus_strategy = st.builds(
    rell_Minus,
)
rell_BoolConstant_strategy = st.builds(
    rell_BoolConstant,
    value=
        safe_text
)
rell_StringConstant_strategy = st.builds(
    rell_StringConstant,
    value=
        safe_text
)
rell_IntConstant_strategy = st.builds(
    rell_IntConstant,
    value=
        st.integers()
)
rell_MulOrDiv_strategy = st.builds(
    rell_MulOrDiv,
    op=
        safe_text
)
rell_Or_strategy = st.builds(
    rell_Or,
)
rell_ClassType_strategy = st.builds(
    rell_ClassType,
)
rell_PrimitiveType_strategy = st.builds(
    rell_PrimitiveType,
    primitiveType=
        safe_text
)
rell_TypeReference_strategy = st.builds(
    rell_TypeReference,
)
rell_ConditionElement_strategy = st.builds(
    rell_ConditionElement,
    compareName=
        safe_text
)
Relational_strategy = st.builds(
    Relational,
)
rell_Delete_strategy = st.builds(
    rell_Delete,
)
rell_Create_strategy = st.builds(
    rell_Create,
)
rell_Update_strategy = st.builds(
    rell_Update,
)
rell_Expression_strategy = st.builds(
    rell_Expression,
)
rell_VariableDeclaration_strategy = st.builds(
    rell_VariableDeclaration,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
rell_VariableInit_strategy = st.builds(
    rell_VariableInit,
)
rell_Relational_strategy = st.builds(
    rell_Relational,
    entity=
        safe_text
)
rell_Variable_strategy = st.builds(
    rell_Variable,
)
rell_Statement_strategy = st.builds(
    rell_Statement,
)
rell_RelAttrubutesList_strategy = st.builds(
    rell_RelAttrubutesList,
)
rell_Attribute_strategy = st.builds(
    rell_Attribute,
    modificator=
        safe_text
)
rell_Operation_strategy = st.builds(
    rell_Operation,
    name=
        safe_text
)
rell_ClassDefinition_strategy = st.builds(
    rell_ClassDefinition,
    name=
        safe_text
)
rell_Model_strategy = st.builds(
    rell_Model,
)

@given(instance=rell_Conditions_strategy)
@settings(max_examples=50)
def test_rell_conditions_instantiation(instance):
    assert isinstance(instance, rell_Conditions)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=rell_And_strategy)
@settings(max_examples=50)
def test_rell_and_instantiation(instance):
    assert isinstance(instance, rell_And)

@given(instance=rell_Equality_strategy)
@settings(max_examples=50)
def test_rell_equality_instantiation(instance):
    assert isinstance(instance, rell_Equality)



@given(instance=rell_Equality_strategy)
def test_rell_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=rell_Comparison_strategy)
@settings(max_examples=50)
def test_rell_comparison_instantiation(instance):
    assert isinstance(instance, rell_Comparison)



@given(instance=rell_Comparison_strategy)
def test_rell_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=rell_Plus_strategy)
@settings(max_examples=50)
def test_rell_plus_instantiation(instance):
    assert isinstance(instance, rell_Plus)

@given(instance=rell_Not_strategy)
@settings(max_examples=50)
def test_rell_not_instantiation(instance):
    assert isinstance(instance, rell_Not)

@given(instance=rell_VariableRef_strategy)
@settings(max_examples=50)
def test_rell_variableref_instantiation(instance):
    assert isinstance(instance, rell_VariableRef)

@given(instance=rell_Minus_strategy)
@settings(max_examples=50)
def test_rell_minus_instantiation(instance):
    assert isinstance(instance, rell_Minus)

@given(instance=rell_BoolConstant_strategy)
@settings(max_examples=50)
def test_rell_boolconstant_instantiation(instance):
    assert isinstance(instance, rell_BoolConstant)



@given(instance=rell_BoolConstant_strategy)
def test_rell_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rell_StringConstant_strategy)
@settings(max_examples=50)
def test_rell_stringconstant_instantiation(instance):
    assert isinstance(instance, rell_StringConstant)



@given(instance=rell_StringConstant_strategy)
def test_rell_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rell_IntConstant_strategy)
@settings(max_examples=50)
def test_rell_intconstant_instantiation(instance):
    assert isinstance(instance, rell_IntConstant)



@given(instance=rell_IntConstant_strategy)
def test_rell_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=rell_MulOrDiv_strategy)
@settings(max_examples=50)
def test_rell_mulordiv_instantiation(instance):
    assert isinstance(instance, rell_MulOrDiv)



@given(instance=rell_MulOrDiv_strategy)
def test_rell_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=rell_Or_strategy)
@settings(max_examples=50)
def test_rell_or_instantiation(instance):
    assert isinstance(instance, rell_Or)

@given(instance=rell_ClassType_strategy)
@settings(max_examples=50)
def test_rell_classtype_instantiation(instance):
    assert isinstance(instance, rell_ClassType)

@given(instance=rell_PrimitiveType_strategy)
@settings(max_examples=50)
def test_rell_primitivetype_instantiation(instance):
    assert isinstance(instance, rell_PrimitiveType)



@given(instance=rell_PrimitiveType_strategy)
def test_rell_primitivetype_primitiveType_setter(instance):
    original = instance.primitiveType
    instance.primitiveType = original
    assert instance.primitiveType == original

@given(instance=rell_TypeReference_strategy)
@settings(max_examples=50)
def test_rell_typereference_instantiation(instance):
    assert isinstance(instance, rell_TypeReference)

@given(instance=rell_ConditionElement_strategy)
@settings(max_examples=50)
def test_rell_conditionelement_instantiation(instance):
    assert isinstance(instance, rell_ConditionElement)



@given(instance=rell_ConditionElement_strategy)
def test_rell_conditionelement_compareName_setter(instance):
    original = instance.compareName
    instance.compareName = original
    assert instance.compareName == original

@given(instance=Relational_strategy)
@settings(max_examples=50)
def test_relational_instantiation(instance):
    assert isinstance(instance, Relational)

@given(instance=rell_Delete_strategy)
@settings(max_examples=50)
def test_rell_delete_instantiation(instance):
    assert isinstance(instance, rell_Delete)

@given(instance=rell_Create_strategy)
@settings(max_examples=50)
def test_rell_create_instantiation(instance):
    assert isinstance(instance, rell_Create)

@given(instance=rell_Update_strategy)
@settings(max_examples=50)
def test_rell_update_instantiation(instance):
    assert isinstance(instance, rell_Update)

@given(instance=rell_Expression_strategy)
@settings(max_examples=50)
def test_rell_expression_instantiation(instance):
    assert isinstance(instance, rell_Expression)

@given(instance=rell_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_rell_variabledeclaration_instantiation(instance):
    assert isinstance(instance, rell_VariableDeclaration)



@given(instance=rell_VariableDeclaration_strategy)
def test_rell_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=rell_VariableInit_strategy)
@settings(max_examples=50)
def test_rell_variableinit_instantiation(instance):
    assert isinstance(instance, rell_VariableInit)

@given(instance=rell_Relational_strategy)
@settings(max_examples=50)
def test_rell_relational_instantiation(instance):
    assert isinstance(instance, rell_Relational)



@given(instance=rell_Relational_strategy)
def test_rell_relational_entity_setter(instance):
    original = instance.entity
    instance.entity = original
    assert instance.entity == original

@given(instance=rell_Variable_strategy)
@settings(max_examples=50)
def test_rell_variable_instantiation(instance):
    assert isinstance(instance, rell_Variable)

@given(instance=rell_Statement_strategy)
@settings(max_examples=50)
def test_rell_statement_instantiation(instance):
    assert isinstance(instance, rell_Statement)

@given(instance=rell_RelAttrubutesList_strategy)
@settings(max_examples=50)
def test_rell_relattrubuteslist_instantiation(instance):
    assert isinstance(instance, rell_RelAttrubutesList)

@given(instance=rell_Attribute_strategy)
@settings(max_examples=50)
def test_rell_attribute_instantiation(instance):
    assert isinstance(instance, rell_Attribute)



@given(instance=rell_Attribute_strategy)
def test_rell_attribute_modificator_setter(instance):
    original = instance.modificator
    instance.modificator = original
    assert instance.modificator == original

@given(instance=rell_Operation_strategy)
@settings(max_examples=50)
def test_rell_operation_instantiation(instance):
    assert isinstance(instance, rell_Operation)



@given(instance=rell_Operation_strategy)
def test_rell_operation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rell_ClassDefinition_strategy)
@settings(max_examples=50)
def test_rell_classdefinition_instantiation(instance):
    assert isinstance(instance, rell_ClassDefinition)



@given(instance=rell_ClassDefinition_strategy)
def test_rell_classdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=rell_Model_strategy)
@settings(max_examples=50)
def test_rell_model_instantiation(instance):
    assert isinstance(instance, rell_Model)
