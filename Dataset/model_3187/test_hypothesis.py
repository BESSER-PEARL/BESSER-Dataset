import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BasicType,
    myDsl_BoolType,
    myDsl_StringType,
    myDsl_IntType,
    myDsl_Expression,
    myDsl_Condition,
    myDsl_Rule,
    myDsl_ArrayElement,
    ElementType,
    myDsl_BasicType,
    myDsl_ArrayType,
    Expression,
    myDsl_And,
    myDsl_Not,
    myDsl_StringConstant,
    myDsl_BoolConstant,
    myDsl_MulOrDiv,
    myDsl_Minus,
    myDsl_IntConstant,
    myDsl_Comparison,
    myDsl_Plus,
    myDsl_VariableConstant,
    myDsl_Equality,
    myDsl_Or,
    myDsl_Model,
    myDsl_EntityType,
    myDsl_ElementType,
    myDsl_ValueType,
    myDsl_Attribute,
    myDsl_IsServer,
    Member,
    myDsl_Verb,
    myDsl_Entity,
    myDsl_Member,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_basictype_is_not_abstract():
    assert not inspect.isabstract(BasicType)


def test_basictype_constructor_exists():
    assert callable(BasicType.__init__)


def test_basictype_constructor_args():
    sig = inspect.signature(BasicType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_booltype_is_not_abstract():
    assert not inspect.isabstract(myDsl_BoolType)


def test_mydsl_booltype_constructor_exists():
    assert callable(myDsl_BoolType.__init__)


def test_mydsl_booltype_constructor_args():
    sig = inspect.signature(myDsl_BoolType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_booltype_has_value():
    assert hasattr(myDsl_BoolType, "value")
    descriptor = None
    for klass in myDsl_BoolType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_stringtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_StringType)


def test_mydsl_stringtype_constructor_exists():
    assert callable(myDsl_StringType.__init__)


def test_mydsl_stringtype_constructor_args():
    sig = inspect.signature(myDsl_StringType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_stringtype_has_value():
    assert hasattr(myDsl_StringType, "value")
    descriptor = None
    for klass in myDsl_StringType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_inttype_is_not_abstract():
    assert not inspect.isabstract(myDsl_IntType)


def test_mydsl_inttype_constructor_exists():
    assert callable(myDsl_IntType.__init__)


def test_mydsl_inttype_constructor_args():
    sig = inspect.signature(myDsl_IntType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_inttype_has_value():
    assert hasattr(myDsl_IntType, "value")
    descriptor = None
    for klass in myDsl_IntType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_expression_is_not_abstract():
    assert not inspect.isabstract(myDsl_Expression)


def test_mydsl_expression_constructor_exists():
    assert callable(myDsl_Expression.__init__)


def test_mydsl_expression_constructor_args():
    sig = inspect.signature(myDsl_Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_condition_is_not_abstract():
    assert not inspect.isabstract(myDsl_Condition)


def test_mydsl_condition_constructor_exists():
    assert callable(myDsl_Condition.__init__)


def test_mydsl_condition_constructor_args():
    sig = inspect.signature(myDsl_Condition.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_rule_is_not_abstract():
    assert not inspect.isabstract(myDsl_Rule)


def test_mydsl_rule_constructor_exists():
    assert callable(myDsl_Rule.__init__)


def test_mydsl_rule_constructor_args():
    sig = inspect.signature(myDsl_Rule.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arrayelement_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArrayElement)


def test_mydsl_arrayelement_constructor_exists():
    assert callable(myDsl_ArrayElement.__init__)


def test_mydsl_arrayelement_constructor_args():
    sig = inspect.signature(myDsl_ArrayElement.__init__)
    params = list(sig.parameters.keys())



def test_elementtype_is_not_abstract():
    assert not inspect.isabstract(ElementType)


def test_elementtype_constructor_exists():
    assert callable(ElementType.__init__)


def test_elementtype_constructor_args():
    sig = inspect.signature(ElementType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_basictype_is_not_abstract():
    assert not inspect.isabstract(myDsl_BasicType)


def test_mydsl_basictype_constructor_exists():
    assert callable(myDsl_BasicType.__init__)


def test_mydsl_basictype_constructor_args():
    sig = inspect.signature(myDsl_BasicType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_arraytype_is_not_abstract():
    assert not inspect.isabstract(myDsl_ArrayType)


def test_mydsl_arraytype_constructor_exists():
    assert callable(myDsl_ArrayType.__init__)


def test_mydsl_arraytype_constructor_args():
    sig = inspect.signature(myDsl_ArrayType.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_and_is_not_abstract():
    assert not inspect.isabstract(myDsl_And)


def test_mydsl_and_constructor_exists():
    assert callable(myDsl_And.__init__)


def test_mydsl_and_constructor_args():
    sig = inspect.signature(myDsl_And.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_not_is_not_abstract():
    assert not inspect.isabstract(myDsl_Not)


def test_mydsl_not_constructor_exists():
    assert callable(myDsl_Not.__init__)


def test_mydsl_not_constructor_args():
    sig = inspect.signature(myDsl_Not.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_stringconstant_is_not_abstract():
    assert not inspect.isabstract(myDsl_StringConstant)


def test_mydsl_stringconstant_constructor_exists():
    assert callable(myDsl_StringConstant.__init__)


def test_mydsl_stringconstant_constructor_args():
    sig = inspect.signature(myDsl_StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_stringconstant_has_value():
    assert hasattr(myDsl_StringConstant, "value")
    descriptor = None
    for klass in myDsl_StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_boolconstant_is_not_abstract():
    assert not inspect.isabstract(myDsl_BoolConstant)


def test_mydsl_boolconstant_constructor_exists():
    assert callable(myDsl_BoolConstant.__init__)


def test_mydsl_boolconstant_constructor_args():
    sig = inspect.signature(myDsl_BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_boolconstant_has_value():
    assert hasattr(myDsl_BoolConstant, "value")
    descriptor = None
    for klass in myDsl_BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_mulordiv_is_not_abstract():
    assert not inspect.isabstract(myDsl_MulOrDiv)


def test_mydsl_mulordiv_constructor_exists():
    assert callable(myDsl_MulOrDiv.__init__)


def test_mydsl_mulordiv_constructor_args():
    sig = inspect.signature(myDsl_MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_mulordiv_has_op():
    assert hasattr(myDsl_MulOrDiv, "op")
    descriptor = None
    for klass in myDsl_MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_minus_is_not_abstract():
    assert not inspect.isabstract(myDsl_Minus)


def test_mydsl_minus_constructor_exists():
    assert callable(myDsl_Minus.__init__)


def test_mydsl_minus_constructor_args():
    sig = inspect.signature(myDsl_Minus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_intconstant_is_not_abstract():
    assert not inspect.isabstract(myDsl_IntConstant)


def test_mydsl_intconstant_constructor_exists():
    assert callable(myDsl_IntConstant.__init__)


def test_mydsl_intconstant_constructor_args():
    sig = inspect.signature(myDsl_IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_intconstant_has_value():
    assert hasattr(myDsl_IntConstant, "value")
    descriptor = None
    for klass in myDsl_IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_comparison_is_not_abstract():
    assert not inspect.isabstract(myDsl_Comparison)


def test_mydsl_comparison_constructor_exists():
    assert callable(myDsl_Comparison.__init__)


def test_mydsl_comparison_constructor_args():
    sig = inspect.signature(myDsl_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_comparison_has_op():
    assert hasattr(myDsl_Comparison, "op")
    descriptor = None
    for klass in myDsl_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_plus_is_not_abstract():
    assert not inspect.isabstract(myDsl_Plus)


def test_mydsl_plus_constructor_exists():
    assert callable(myDsl_Plus.__init__)


def test_mydsl_plus_constructor_args():
    sig = inspect.signature(myDsl_Plus.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_variableconstant_is_not_abstract():
    assert not inspect.isabstract(myDsl_VariableConstant)


def test_mydsl_variableconstant_constructor_exists():
    assert callable(myDsl_VariableConstant.__init__)


def test_mydsl_variableconstant_constructor_args():
    sig = inspect.signature(myDsl_VariableConstant.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_equality_is_not_abstract():
    assert not inspect.isabstract(myDsl_Equality)


def test_mydsl_equality_constructor_exists():
    assert callable(myDsl_Equality.__init__)


def test_mydsl_equality_constructor_args():
    sig = inspect.signature(myDsl_Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_mydsl_equality_has_op():
    assert hasattr(myDsl_Equality, "op")
    descriptor = None
    for klass in myDsl_Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_or_is_not_abstract():
    assert not inspect.isabstract(myDsl_Or)


def test_mydsl_or_constructor_exists():
    assert callable(myDsl_Or.__init__)


def test_mydsl_or_constructor_args():
    sig = inspect.signature(myDsl_Or.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_model_is_not_abstract():
    assert not inspect.isabstract(myDsl_Model)


def test_mydsl_model_constructor_exists():
    assert callable(myDsl_Model.__init__)


def test_mydsl_model_constructor_args():
    sig = inspect.signature(myDsl_Model.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_entitytype_is_not_abstract():
    assert not inspect.isabstract(myDsl_EntityType)


def test_mydsl_entitytype_constructor_exists():
    assert callable(myDsl_EntityType.__init__)


def test_mydsl_entitytype_constructor_args():
    sig = inspect.signature(myDsl_EntityType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_elementtype_is_not_abstract():
    assert not inspect.isabstract(myDsl_ElementType)


def test_mydsl_elementtype_constructor_exists():
    assert callable(myDsl_ElementType.__init__)


def test_mydsl_elementtype_constructor_args():
    sig = inspect.signature(myDsl_ElementType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_valuetype_is_not_abstract():
    assert not inspect.isabstract(myDsl_ValueType)


def test_mydsl_valuetype_constructor_exists():
    assert callable(myDsl_ValueType.__init__)


def test_mydsl_valuetype_constructor_args():
    sig = inspect.signature(myDsl_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_attribute_is_not_abstract():
    assert not inspect.isabstract(myDsl_Attribute)


def test_mydsl_attribute_constructor_exists():
    assert callable(myDsl_Attribute.__init__)


def test_mydsl_attribute_constructor_args():
    sig = inspect.signature(myDsl_Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_attribute_has_name():
    assert hasattr(myDsl_Attribute, "name")
    descriptor = None
    for klass in myDsl_Attribute.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_isserver_is_not_abstract():
    assert not inspect.isabstract(myDsl_IsServer)


def test_mydsl_isserver_constructor_exists():
    assert callable(myDsl_IsServer.__init__)


def test_mydsl_isserver_constructor_args():
    sig = inspect.signature(myDsl_IsServer.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_mydsl_isserver_has_value():
    assert hasattr(myDsl_IsServer, "value")
    descriptor = None
    for klass in myDsl_IsServer.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_verb_is_not_abstract():
    assert not inspect.isabstract(myDsl_Verb)


def test_mydsl_verb_constructor_exists():
    assert callable(myDsl_Verb.__init__)


def test_mydsl_verb_constructor_args():
    sig = inspect.signature(myDsl_Verb.__init__)
    params = list(sig.parameters.keys())
    assert "verb" in params, "Missing parameter 'verb'"
    assert "qa" in params, "Missing parameter 'qa'"

def test_mydsl_verb_has_verb():
    assert hasattr(myDsl_Verb, "verb")
    descriptor = None
    for klass in myDsl_Verb.__mro__:
        if "verb" in klass.__dict__:
            descriptor = klass.__dict__["verb"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_verb_has_qa():
    assert hasattr(myDsl_Verb, "qa")
    descriptor = None
    for klass in myDsl_Verb.__mro__:
        if "qa" in klass.__dict__:
            descriptor = klass.__dict__["qa"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_entity_is_not_abstract():
    assert not inspect.isabstract(myDsl_Entity)


def test_mydsl_entity_constructor_exists():
    assert callable(myDsl_Entity.__init__)


def test_mydsl_entity_constructor_args():
    sig = inspect.signature(myDsl_Entity.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mydsl_entity_has_name():
    assert hasattr(myDsl_Entity, "name")
    descriptor = None
    for klass in myDsl_Entity.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_member_is_not_abstract():
    assert not inspect.isabstract(myDsl_Member)


def test_mydsl_member_constructor_exists():
    assert callable(myDsl_Member.__init__)


def test_mydsl_member_constructor_args():
    sig = inspect.signature(myDsl_Member.__init__)
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
BasicType_strategy = st.builds(
    BasicType,
)
myDsl_BoolType_strategy = st.builds(
    myDsl_BoolType,
    value=
        safe_text
)
myDsl_StringType_strategy = st.builds(
    myDsl_StringType,
    value=
        safe_text
)
myDsl_IntType_strategy = st.builds(
    myDsl_IntType,
    value=
        st.integers()
)
myDsl_Expression_strategy = st.builds(
    myDsl_Expression,
)
myDsl_Condition_strategy = st.builds(
    myDsl_Condition,
)
myDsl_Rule_strategy = st.builds(
    myDsl_Rule,
)
myDsl_ArrayElement_strategy = st.builds(
    myDsl_ArrayElement,
)
ElementType_strategy = st.builds(
    ElementType,
)
myDsl_BasicType_strategy = st.builds(
    myDsl_BasicType,
)
myDsl_ArrayType_strategy = st.builds(
    myDsl_ArrayType,
)
Expression_strategy = st.builds(
    Expression,
)
myDsl_And_strategy = st.builds(
    myDsl_And,
)
myDsl_Not_strategy = st.builds(
    myDsl_Not,
)
myDsl_StringConstant_strategy = st.builds(
    myDsl_StringConstant,
    value=
        safe_text
)
myDsl_BoolConstant_strategy = st.builds(
    myDsl_BoolConstant,
    value=
        safe_text
)
myDsl_MulOrDiv_strategy = st.builds(
    myDsl_MulOrDiv,
    op=
        safe_text
)
myDsl_Minus_strategy = st.builds(
    myDsl_Minus,
)
myDsl_IntConstant_strategy = st.builds(
    myDsl_IntConstant,
    value=
        st.integers()
)
myDsl_Comparison_strategy = st.builds(
    myDsl_Comparison,
    op=
        safe_text
)
myDsl_Plus_strategy = st.builds(
    myDsl_Plus,
)
myDsl_VariableConstant_strategy = st.builds(
    myDsl_VariableConstant,
)
myDsl_Equality_strategy = st.builds(
    myDsl_Equality,
    op=
        safe_text
)
myDsl_Or_strategy = st.builds(
    myDsl_Or,
)
myDsl_Model_strategy = st.builds(
    myDsl_Model,
)
myDsl_EntityType_strategy = st.builds(
    myDsl_EntityType,
)
myDsl_ElementType_strategy = st.builds(
    myDsl_ElementType,
)
myDsl_ValueType_strategy = st.builds(
    myDsl_ValueType,
)
myDsl_Attribute_strategy = st.builds(
    myDsl_Attribute,
    name=
        safe_text
)
myDsl_IsServer_strategy = st.builds(
    myDsl_IsServer,
    value=
        safe_text
)
Member_strategy = st.builds(
    Member,
)
myDsl_Verb_strategy = st.builds(
    myDsl_Verb,
    verb=
        safe_text,
    qa=
        safe_text
)
myDsl_Entity_strategy = st.builds(
    myDsl_Entity,
    name=
        safe_text
)
myDsl_Member_strategy = st.builds(
    myDsl_Member,
)

@given(instance=BasicType_strategy)
@settings(max_examples=50)
def test_basictype_instantiation(instance):
    assert isinstance(instance, BasicType)

@given(instance=myDsl_BoolType_strategy)
@settings(max_examples=50)
def test_mydsl_booltype_instantiation(instance):
    assert isinstance(instance, myDsl_BoolType)



@given(instance=myDsl_BoolType_strategy)
def test_mydsl_booltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_StringType_strategy)
@settings(max_examples=50)
def test_mydsl_stringtype_instantiation(instance):
    assert isinstance(instance, myDsl_StringType)



@given(instance=myDsl_StringType_strategy)
def test_mydsl_stringtype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_IntType_strategy)
@settings(max_examples=50)
def test_mydsl_inttype_instantiation(instance):
    assert isinstance(instance, myDsl_IntType)



@given(instance=myDsl_IntType_strategy)
def test_mydsl_inttype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_Expression_strategy)
@settings(max_examples=50)
def test_mydsl_expression_instantiation(instance):
    assert isinstance(instance, myDsl_Expression)

@given(instance=myDsl_Condition_strategy)
@settings(max_examples=50)
def test_mydsl_condition_instantiation(instance):
    assert isinstance(instance, myDsl_Condition)

@given(instance=myDsl_Rule_strategy)
@settings(max_examples=50)
def test_mydsl_rule_instantiation(instance):
    assert isinstance(instance, myDsl_Rule)

@given(instance=myDsl_ArrayElement_strategy)
@settings(max_examples=50)
def test_mydsl_arrayelement_instantiation(instance):
    assert isinstance(instance, myDsl_ArrayElement)

@given(instance=ElementType_strategy)
@settings(max_examples=50)
def test_elementtype_instantiation(instance):
    assert isinstance(instance, ElementType)

@given(instance=myDsl_BasicType_strategy)
@settings(max_examples=50)
def test_mydsl_basictype_instantiation(instance):
    assert isinstance(instance, myDsl_BasicType)

@given(instance=myDsl_ArrayType_strategy)
@settings(max_examples=50)
def test_mydsl_arraytype_instantiation(instance):
    assert isinstance(instance, myDsl_ArrayType)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=myDsl_And_strategy)
@settings(max_examples=50)
def test_mydsl_and_instantiation(instance):
    assert isinstance(instance, myDsl_And)

@given(instance=myDsl_Not_strategy)
@settings(max_examples=50)
def test_mydsl_not_instantiation(instance):
    assert isinstance(instance, myDsl_Not)

@given(instance=myDsl_StringConstant_strategy)
@settings(max_examples=50)
def test_mydsl_stringconstant_instantiation(instance):
    assert isinstance(instance, myDsl_StringConstant)



@given(instance=myDsl_StringConstant_strategy)
def test_mydsl_stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_BoolConstant_strategy)
@settings(max_examples=50)
def test_mydsl_boolconstant_instantiation(instance):
    assert isinstance(instance, myDsl_BoolConstant)



@given(instance=myDsl_BoolConstant_strategy)
def test_mydsl_boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_MulOrDiv_strategy)
@settings(max_examples=50)
def test_mydsl_mulordiv_instantiation(instance):
    assert isinstance(instance, myDsl_MulOrDiv)



@given(instance=myDsl_MulOrDiv_strategy)
def test_mydsl_mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_Minus_strategy)
@settings(max_examples=50)
def test_mydsl_minus_instantiation(instance):
    assert isinstance(instance, myDsl_Minus)

@given(instance=myDsl_IntConstant_strategy)
@settings(max_examples=50)
def test_mydsl_intconstant_instantiation(instance):
    assert isinstance(instance, myDsl_IntConstant)



@given(instance=myDsl_IntConstant_strategy)
def test_mydsl_intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=myDsl_Comparison_strategy)
@settings(max_examples=50)
def test_mydsl_comparison_instantiation(instance):
    assert isinstance(instance, myDsl_Comparison)



@given(instance=myDsl_Comparison_strategy)
def test_mydsl_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_Plus_strategy)
@settings(max_examples=50)
def test_mydsl_plus_instantiation(instance):
    assert isinstance(instance, myDsl_Plus)

@given(instance=myDsl_VariableConstant_strategy)
@settings(max_examples=50)
def test_mydsl_variableconstant_instantiation(instance):
    assert isinstance(instance, myDsl_VariableConstant)

@given(instance=myDsl_Equality_strategy)
@settings(max_examples=50)
def test_mydsl_equality_instantiation(instance):
    assert isinstance(instance, myDsl_Equality)



@given(instance=myDsl_Equality_strategy)
def test_mydsl_equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=myDsl_Or_strategy)
@settings(max_examples=50)
def test_mydsl_or_instantiation(instance):
    assert isinstance(instance, myDsl_Or)

@given(instance=myDsl_Model_strategy)
@settings(max_examples=50)
def test_mydsl_model_instantiation(instance):
    assert isinstance(instance, myDsl_Model)

@given(instance=myDsl_EntityType_strategy)
@settings(max_examples=50)
def test_mydsl_entitytype_instantiation(instance):
    assert isinstance(instance, myDsl_EntityType)

@given(instance=myDsl_ElementType_strategy)
@settings(max_examples=50)
def test_mydsl_elementtype_instantiation(instance):
    assert isinstance(instance, myDsl_ElementType)

@given(instance=myDsl_ValueType_strategy)
@settings(max_examples=50)
def test_mydsl_valuetype_instantiation(instance):
    assert isinstance(instance, myDsl_ValueType)

@given(instance=myDsl_Attribute_strategy)
@settings(max_examples=50)
def test_mydsl_attribute_instantiation(instance):
    assert isinstance(instance, myDsl_Attribute)



@given(instance=myDsl_Attribute_strategy)
def test_mydsl_attribute_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_IsServer_strategy)
@settings(max_examples=50)
def test_mydsl_isserver_instantiation(instance):
    assert isinstance(instance, myDsl_IsServer)



@given(instance=myDsl_IsServer_strategy)
def test_mydsl_isserver_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)

@given(instance=myDsl_Verb_strategy)
@settings(max_examples=50)
def test_mydsl_verb_instantiation(instance):
    assert isinstance(instance, myDsl_Verb)



@given(instance=myDsl_Verb_strategy)
def test_mydsl_verb_verb_setter(instance):
    original = instance.verb
    instance.verb = original
    assert instance.verb == original



@given(instance=myDsl_Verb_strategy)
def test_mydsl_verb_qa_setter(instance):
    original = instance.qa
    instance.qa = original
    assert instance.qa == original

@given(instance=myDsl_Entity_strategy)
@settings(max_examples=50)
def test_mydsl_entity_instantiation(instance):
    assert isinstance(instance, myDsl_Entity)



@given(instance=myDsl_Entity_strategy)
def test_mydsl_entity_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=myDsl_Member_strategy)
@settings(max_examples=50)
def test_mydsl_member_instantiation(instance):
    assert isinstance(instance, myDsl_Member)
