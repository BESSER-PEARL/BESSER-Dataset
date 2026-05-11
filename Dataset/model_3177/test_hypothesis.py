import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    iotdsl::IfBlock,
    Expression,
    iotdsl::IntConstant,
    iotdsl::VariableRef,
    iotdsl::BoolConstant,
    iotdsl::Or,
    iotdsl::And,
    iotdsl::StringConstant,
    iotdsl::Not,
    iotdsl::MulOrDiv,
    iotdsl::Minus,
    iotdsl::Plus,
    iotdsl::Comparison,
    iotdsl::Equality,
    iotdsl::Device,
    iotdsl::Iot,
    iotdsl::IfStatement,
    Action,
    iotdsl::Expression,
    iotdsl::Variable,
    iotdsl::Action,
    iotdsl::Transition,
    iotdsl::Event,
    iotdsl::State,
    iotdsl::Attribute,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_iotdsl::ifblock_is_not_abstract():
    assert not inspect.isabstract(iotdsl::IfBlock)


def test_iotdsl::ifblock_constructor_exists():
    assert callable(iotdsl::IfBlock.__init__)


def test_iotdsl::ifblock_constructor_args():
    sig = inspect.signature(iotdsl::IfBlock.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::intconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl::IntConstant)


def test_iotdsl::intconstant_constructor_exists():
    assert callable(iotdsl::IntConstant.__init__)


def test_iotdsl::intconstant_constructor_args():
    sig = inspect.signature(iotdsl::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl::intconstant_has_value():
    assert hasattr(iotdsl::IntConstant, "value")
    descriptor = None
    for klass in iotdsl::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::variableref_is_not_abstract():
    assert not inspect.isabstract(iotdsl::VariableRef)


def test_iotdsl::variableref_constructor_exists():
    assert callable(iotdsl::VariableRef.__init__)


def test_iotdsl::variableref_constructor_args():
    sig = inspect.signature(iotdsl::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::boolconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl::BoolConstant)


def test_iotdsl::boolconstant_constructor_exists():
    assert callable(iotdsl::BoolConstant.__init__)


def test_iotdsl::boolconstant_constructor_args():
    sig = inspect.signature(iotdsl::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl::boolconstant_has_value():
    assert hasattr(iotdsl::BoolConstant, "value")
    descriptor = None
    for klass in iotdsl::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::or_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Or)


def test_iotdsl::or_constructor_exists():
    assert callable(iotdsl::Or.__init__)


def test_iotdsl::or_constructor_args():
    sig = inspect.signature(iotdsl::Or.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::and_is_not_abstract():
    assert not inspect.isabstract(iotdsl::And)


def test_iotdsl::and_constructor_exists():
    assert callable(iotdsl::And.__init__)


def test_iotdsl::and_constructor_args():
    sig = inspect.signature(iotdsl::And.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::stringconstant_is_not_abstract():
    assert not inspect.isabstract(iotdsl::StringConstant)


def test_iotdsl::stringconstant_constructor_exists():
    assert callable(iotdsl::StringConstant.__init__)


def test_iotdsl::stringconstant_constructor_args():
    sig = inspect.signature(iotdsl::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_iotdsl::stringconstant_has_value():
    assert hasattr(iotdsl::StringConstant, "value")
    descriptor = None
    for klass in iotdsl::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::not_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Not)


def test_iotdsl::not_constructor_exists():
    assert callable(iotdsl::Not.__init__)


def test_iotdsl::not_constructor_args():
    sig = inspect.signature(iotdsl::Not.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::mulordiv_is_not_abstract():
    assert not inspect.isabstract(iotdsl::MulOrDiv)


def test_iotdsl::mulordiv_constructor_exists():
    assert callable(iotdsl::MulOrDiv.__init__)


def test_iotdsl::mulordiv_constructor_args():
    sig = inspect.signature(iotdsl::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_iotdsl::mulordiv_has_op():
    assert hasattr(iotdsl::MulOrDiv, "op")
    descriptor = None
    for klass in iotdsl::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::minus_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Minus)


def test_iotdsl::minus_constructor_exists():
    assert callable(iotdsl::Minus.__init__)


def test_iotdsl::minus_constructor_args():
    sig = inspect.signature(iotdsl::Minus.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::plus_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Plus)


def test_iotdsl::plus_constructor_exists():
    assert callable(iotdsl::Plus.__init__)


def test_iotdsl::plus_constructor_args():
    sig = inspect.signature(iotdsl::Plus.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::comparison_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Comparison)


def test_iotdsl::comparison_constructor_exists():
    assert callable(iotdsl::Comparison.__init__)


def test_iotdsl::comparison_constructor_args():
    sig = inspect.signature(iotdsl::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_iotdsl::comparison_has_op():
    assert hasattr(iotdsl::Comparison, "op")
    descriptor = None
    for klass in iotdsl::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::equality_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Equality)


def test_iotdsl::equality_constructor_exists():
    assert callable(iotdsl::Equality.__init__)


def test_iotdsl::equality_constructor_args():
    sig = inspect.signature(iotdsl::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_iotdsl::equality_has_op():
    assert hasattr(iotdsl::Equality, "op")
    descriptor = None
    for klass in iotdsl::Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::device_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Device)


def test_iotdsl::device_constructor_exists():
    assert callable(iotdsl::Device.__init__)


def test_iotdsl::device_constructor_args():
    sig = inspect.signature(iotdsl::Device.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::device_has_name():
    assert hasattr(iotdsl::Device, "name")
    descriptor = None
    for klass in iotdsl::Device.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::iot_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Iot)


def test_iotdsl::iot_constructor_exists():
    assert callable(iotdsl::Iot.__init__)


def test_iotdsl::iot_constructor_args():
    sig = inspect.signature(iotdsl::Iot.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::ifstatement_is_not_abstract():
    assert not inspect.isabstract(iotdsl::IfStatement)


def test_iotdsl::ifstatement_constructor_exists():
    assert callable(iotdsl::IfStatement.__init__)


def test_iotdsl::ifstatement_constructor_args():
    sig = inspect.signature(iotdsl::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::expression_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Expression)


def test_iotdsl::expression_constructor_exists():
    assert callable(iotdsl::Expression.__init__)


def test_iotdsl::expression_constructor_args():
    sig = inspect.signature(iotdsl::Expression.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::variable_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Variable)


def test_iotdsl::variable_constructor_exists():
    assert callable(iotdsl::Variable.__init__)


def test_iotdsl::variable_constructor_args():
    sig = inspect.signature(iotdsl::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::variable_has_name():
    assert hasattr(iotdsl::Variable, "name")
    descriptor = None
    for klass in iotdsl::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::action_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Action)


def test_iotdsl::action_constructor_exists():
    assert callable(iotdsl::Action.__init__)


def test_iotdsl::action_constructor_args():
    sig = inspect.signature(iotdsl::Action.__init__)
    params = list(sig.parameters.keys())



def test_iotdsl::transition_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Transition)


def test_iotdsl::transition_constructor_exists():
    assert callable(iotdsl::Transition.__init__)


def test_iotdsl::transition_constructor_args():
    sig = inspect.signature(iotdsl::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::transition_has_name():
    assert hasattr(iotdsl::Transition, "name")
    descriptor = None
    for klass in iotdsl::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::event_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Event)


def test_iotdsl::event_constructor_exists():
    assert callable(iotdsl::Event.__init__)


def test_iotdsl::event_constructor_args():
    sig = inspect.signature(iotdsl::Event.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::event_has_name():
    assert hasattr(iotdsl::Event, "name")
    descriptor = None
    for klass in iotdsl::Event.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::state_is_not_abstract():
    assert not inspect.isabstract(iotdsl::State)


def test_iotdsl::state_constructor_exists():
    assert callable(iotdsl::State.__init__)


def test_iotdsl::state_constructor_args():
    sig = inspect.signature(iotdsl::State.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_iotdsl::state_has_name():
    assert hasattr(iotdsl::State, "name")
    descriptor = None
    for klass in iotdsl::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_iotdsl::attribute_is_not_abstract():
    assert not inspect.isabstract(iotdsl::Attribute)


def test_iotdsl::attribute_constructor_exists():
    assert callable(iotdsl::Attribute.__init__)


def test_iotdsl::attribute_constructor_args():
    sig = inspect.signature(iotdsl::Attribute.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "typeName" in params, "Missing parameter 'typeName'"
    assert "tag" in params, "Missing parameter 'tag'"

def test_iotdsl::attribute_has_value():
    assert hasattr(iotdsl::Attribute, "value")
    descriptor = None
    for klass in iotdsl::Attribute.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_iotdsl::attribute_has_typeName():
    assert hasattr(iotdsl::Attribute, "typeName")
    descriptor = None
    for klass in iotdsl::Attribute.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)

def test_iotdsl::attribute_has_tag():
    assert hasattr(iotdsl::Attribute, "tag")
    descriptor = None
    for klass in iotdsl::Attribute.__mro__:
        if "tag" in klass.__dict__:
            descriptor = klass.__dict__["tag"]
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
iotdsl::IfBlock_strategy = st.builds(
    iotdsl::IfBlock,
)
Expression_strategy = st.builds(
    Expression,
)
iotdsl::IntConstant_strategy = st.builds(
    iotdsl::IntConstant,
    value=
        st.integers()
)
iotdsl::VariableRef_strategy = st.builds(
    iotdsl::VariableRef,
)
iotdsl::BoolConstant_strategy = st.builds(
    iotdsl::BoolConstant,
    value=
        safe_text
)
iotdsl::Or_strategy = st.builds(
    iotdsl::Or,
)
iotdsl::And_strategy = st.builds(
    iotdsl::And,
)
iotdsl::StringConstant_strategy = st.builds(
    iotdsl::StringConstant,
    value=
        safe_text
)
iotdsl::Not_strategy = st.builds(
    iotdsl::Not,
)
iotdsl::MulOrDiv_strategy = st.builds(
    iotdsl::MulOrDiv,
    op=
        safe_text
)
iotdsl::Minus_strategy = st.builds(
    iotdsl::Minus,
)
iotdsl::Plus_strategy = st.builds(
    iotdsl::Plus,
)
iotdsl::Comparison_strategy = st.builds(
    iotdsl::Comparison,
    op=
        safe_text
)
iotdsl::Equality_strategy = st.builds(
    iotdsl::Equality,
    op=
        safe_text
)
iotdsl::Device_strategy = st.builds(
    iotdsl::Device,
    name=
        safe_text
)
iotdsl::Iot_strategy = st.builds(
    iotdsl::Iot,
)
iotdsl::IfStatement_strategy = st.builds(
    iotdsl::IfStatement,
)
Action_strategy = st.builds(
    Action,
)
iotdsl::Expression_strategy = st.builds(
    iotdsl::Expression,
)
iotdsl::Variable_strategy = st.builds(
    iotdsl::Variable,
    name=
        safe_text
)
iotdsl::Action_strategy = st.builds(
    iotdsl::Action,
)
iotdsl::Transition_strategy = st.builds(
    iotdsl::Transition,
    name=
        safe_text
)
iotdsl::Event_strategy = st.builds(
    iotdsl::Event,
    name=
        safe_text
)
iotdsl::State_strategy = st.builds(
    iotdsl::State,
    name=
        safe_text
)
iotdsl::Attribute_strategy = st.builds(
    iotdsl::Attribute,
    value=
        safe_text,
    typeName=
        safe_text,
    tag=
        safe_text
)

@given(instance=iotdsl::IfBlock_strategy)
@settings(max_examples=50)
def test_iotdsl::ifblock_instantiation(instance):
    assert isinstance(instance, iotdsl::IfBlock)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=iotdsl::IntConstant_strategy)
@settings(max_examples=50)
def test_iotdsl::intconstant_instantiation(instance):
    assert isinstance(instance, iotdsl::IntConstant)

@given(instance=iotdsl::IntConstant_strategy)
def test_iotdsl::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=iotdsl::IntConstant_strategy)
def test_iotdsl::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl::VariableRef_strategy)
@settings(max_examples=50)
def test_iotdsl::variableref_instantiation(instance):
    assert isinstance(instance, iotdsl::VariableRef)

@given(instance=iotdsl::BoolConstant_strategy)
@settings(max_examples=50)
def test_iotdsl::boolconstant_instantiation(instance):
    assert isinstance(instance, iotdsl::BoolConstant)

@given(instance=iotdsl::BoolConstant_strategy)
def test_iotdsl::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iotdsl::BoolConstant_strategy)
def test_iotdsl::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl::Or_strategy)
@settings(max_examples=50)
def test_iotdsl::or_instantiation(instance):
    assert isinstance(instance, iotdsl::Or)

@given(instance=iotdsl::And_strategy)
@settings(max_examples=50)
def test_iotdsl::and_instantiation(instance):
    assert isinstance(instance, iotdsl::And)

@given(instance=iotdsl::StringConstant_strategy)
@settings(max_examples=50)
def test_iotdsl::stringconstant_instantiation(instance):
    assert isinstance(instance, iotdsl::StringConstant)

@given(instance=iotdsl::StringConstant_strategy)
def test_iotdsl::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iotdsl::StringConstant_strategy)
def test_iotdsl::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl::Not_strategy)
@settings(max_examples=50)
def test_iotdsl::not_instantiation(instance):
    assert isinstance(instance, iotdsl::Not)

@given(instance=iotdsl::MulOrDiv_strategy)
@settings(max_examples=50)
def test_iotdsl::mulordiv_instantiation(instance):
    assert isinstance(instance, iotdsl::MulOrDiv)

@given(instance=iotdsl::MulOrDiv_strategy)
def test_iotdsl::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=iotdsl::MulOrDiv_strategy)
def test_iotdsl::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=iotdsl::Minus_strategy)
@settings(max_examples=50)
def test_iotdsl::minus_instantiation(instance):
    assert isinstance(instance, iotdsl::Minus)

@given(instance=iotdsl::Plus_strategy)
@settings(max_examples=50)
def test_iotdsl::plus_instantiation(instance):
    assert isinstance(instance, iotdsl::Plus)

@given(instance=iotdsl::Comparison_strategy)
@settings(max_examples=50)
def test_iotdsl::comparison_instantiation(instance):
    assert isinstance(instance, iotdsl::Comparison)

@given(instance=iotdsl::Comparison_strategy)
def test_iotdsl::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=iotdsl::Comparison_strategy)
def test_iotdsl::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=iotdsl::Equality_strategy)
@settings(max_examples=50)
def test_iotdsl::equality_instantiation(instance):
    assert isinstance(instance, iotdsl::Equality)

@given(instance=iotdsl::Equality_strategy)
def test_iotdsl::equality_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=iotdsl::Equality_strategy)
def test_iotdsl::equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=iotdsl::Device_strategy)
@settings(max_examples=50)
def test_iotdsl::device_instantiation(instance):
    assert isinstance(instance, iotdsl::Device)

@given(instance=iotdsl::Device_strategy)
def test_iotdsl::device_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Device_strategy)
def test_iotdsl::device_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::Iot_strategy)
@settings(max_examples=50)
def test_iotdsl::iot_instantiation(instance):
    assert isinstance(instance, iotdsl::Iot)

@given(instance=iotdsl::IfStatement_strategy)
@settings(max_examples=50)
def test_iotdsl::ifstatement_instantiation(instance):
    assert isinstance(instance, iotdsl::IfStatement)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=iotdsl::Expression_strategy)
@settings(max_examples=50)
def test_iotdsl::expression_instantiation(instance):
    assert isinstance(instance, iotdsl::Expression)

@given(instance=iotdsl::Variable_strategy)
@settings(max_examples=50)
def test_iotdsl::variable_instantiation(instance):
    assert isinstance(instance, iotdsl::Variable)

@given(instance=iotdsl::Variable_strategy)
def test_iotdsl::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Variable_strategy)
def test_iotdsl::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::Action_strategy)
@settings(max_examples=50)
def test_iotdsl::action_instantiation(instance):
    assert isinstance(instance, iotdsl::Action)

@given(instance=iotdsl::Transition_strategy)
@settings(max_examples=50)
def test_iotdsl::transition_instantiation(instance):
    assert isinstance(instance, iotdsl::Transition)

@given(instance=iotdsl::Transition_strategy)
def test_iotdsl::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Transition_strategy)
def test_iotdsl::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::Event_strategy)
@settings(max_examples=50)
def test_iotdsl::event_instantiation(instance):
    assert isinstance(instance, iotdsl::Event)

@given(instance=iotdsl::Event_strategy)
def test_iotdsl::event_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::Event_strategy)
def test_iotdsl::event_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::State_strategy)
@settings(max_examples=50)
def test_iotdsl::state_instantiation(instance):
    assert isinstance(instance, iotdsl::State)

@given(instance=iotdsl::State_strategy)
def test_iotdsl::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=iotdsl::State_strategy)
def test_iotdsl::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=iotdsl::Attribute_strategy)
@settings(max_examples=50)
def test_iotdsl::attribute_instantiation(instance):
    assert isinstance(instance, iotdsl::Attribute)

@given(instance=iotdsl::Attribute_strategy)
def test_iotdsl::attribute_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=iotdsl::Attribute_strategy)
def test_iotdsl::attribute_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=iotdsl::Attribute_strategy)
def test_iotdsl::attribute_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=iotdsl::Attribute_strategy)
def test_iotdsl::attribute_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=iotdsl::Attribute_strategy)
def test_iotdsl::attribute_tag_type(instance):
    assert isinstance(instance.tag, str)


@given(instance=iotdsl::Attribute_strategy)
def test_iotdsl::attribute_tag_setter(instance):
    original = instance.tag
    instance.tag = original
    assert instance.tag == original
