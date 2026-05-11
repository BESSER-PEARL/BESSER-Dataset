import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    tym::Block,
    Expression,
    tym::MulOrDiv,
    tym::Minus,
    tym::Equality,
    tym::Not,
    tym::Comparison,
    tym::And,
    tym::BoolConstant,
    tym::VariableRef,
    tym::IntConstant,
    tym::Plus,
    tym::StringConstant,
    tym::Or,
    tym::Expression,
    AbstractElement,
    tym::LoopStatement,
    tym::Return,
    tym::PrintStatement,
    tym::FunctionCall,
    tym::TestStatement,
    tym::Variable,
    tym::AbstractElement,
    tym::EObject,
    tym::Model,
    tym::FunctionBlock,
    tym::Function,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_tym::block_is_not_abstract():
    assert not inspect.isabstract(tym::Block)


def test_tym::block_constructor_exists():
    assert callable(tym::Block.__init__)


def test_tym::block_constructor_args():
    sig = inspect.signature(tym::Block.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_tym::mulordiv_is_not_abstract():
    assert not inspect.isabstract(tym::MulOrDiv)


def test_tym::mulordiv_constructor_exists():
    assert callable(tym::MulOrDiv.__init__)


def test_tym::mulordiv_constructor_args():
    sig = inspect.signature(tym::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_tym::mulordiv_has_op():
    assert hasattr(tym::MulOrDiv, "op")
    descriptor = None
    for klass in tym::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_tym::minus_is_not_abstract():
    assert not inspect.isabstract(tym::Minus)


def test_tym::minus_constructor_exists():
    assert callable(tym::Minus.__init__)


def test_tym::minus_constructor_args():
    sig = inspect.signature(tym::Minus.__init__)
    params = list(sig.parameters.keys())



def test_tym::equality_is_not_abstract():
    assert not inspect.isabstract(tym::Equality)


def test_tym::equality_constructor_exists():
    assert callable(tym::Equality.__init__)


def test_tym::equality_constructor_args():
    sig = inspect.signature(tym::Equality.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_tym::equality_has_op():
    assert hasattr(tym::Equality, "op")
    descriptor = None
    for klass in tym::Equality.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_tym::not_is_not_abstract():
    assert not inspect.isabstract(tym::Not)


def test_tym::not_constructor_exists():
    assert callable(tym::Not.__init__)


def test_tym::not_constructor_args():
    sig = inspect.signature(tym::Not.__init__)
    params = list(sig.parameters.keys())



def test_tym::comparison_is_not_abstract():
    assert not inspect.isabstract(tym::Comparison)


def test_tym::comparison_constructor_exists():
    assert callable(tym::Comparison.__init__)


def test_tym::comparison_constructor_args():
    sig = inspect.signature(tym::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_tym::comparison_has_op():
    assert hasattr(tym::Comparison, "op")
    descriptor = None
    for klass in tym::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_tym::and_is_not_abstract():
    assert not inspect.isabstract(tym::And)


def test_tym::and_constructor_exists():
    assert callable(tym::And.__init__)


def test_tym::and_constructor_args():
    sig = inspect.signature(tym::And.__init__)
    params = list(sig.parameters.keys())



def test_tym::boolconstant_is_not_abstract():
    assert not inspect.isabstract(tym::BoolConstant)


def test_tym::boolconstant_constructor_exists():
    assert callable(tym::BoolConstant.__init__)


def test_tym::boolconstant_constructor_args():
    sig = inspect.signature(tym::BoolConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tym::boolconstant_has_value():
    assert hasattr(tym::BoolConstant, "value")
    descriptor = None
    for klass in tym::BoolConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tym::variableref_is_not_abstract():
    assert not inspect.isabstract(tym::VariableRef)


def test_tym::variableref_constructor_exists():
    assert callable(tym::VariableRef.__init__)


def test_tym::variableref_constructor_args():
    sig = inspect.signature(tym::VariableRef.__init__)
    params = list(sig.parameters.keys())



def test_tym::intconstant_is_not_abstract():
    assert not inspect.isabstract(tym::IntConstant)


def test_tym::intconstant_constructor_exists():
    assert callable(tym::IntConstant.__init__)


def test_tym::intconstant_constructor_args():
    sig = inspect.signature(tym::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tym::intconstant_has_value():
    assert hasattr(tym::IntConstant, "value")
    descriptor = None
    for klass in tym::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tym::plus_is_not_abstract():
    assert not inspect.isabstract(tym::Plus)


def test_tym::plus_constructor_exists():
    assert callable(tym::Plus.__init__)


def test_tym::plus_constructor_args():
    sig = inspect.signature(tym::Plus.__init__)
    params = list(sig.parameters.keys())



def test_tym::stringconstant_is_not_abstract():
    assert not inspect.isabstract(tym::StringConstant)


def test_tym::stringconstant_constructor_exists():
    assert callable(tym::StringConstant.__init__)


def test_tym::stringconstant_constructor_args():
    sig = inspect.signature(tym::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_tym::stringconstant_has_value():
    assert hasattr(tym::StringConstant, "value")
    descriptor = None
    for klass in tym::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_tym::or_is_not_abstract():
    assert not inspect.isabstract(tym::Or)


def test_tym::or_constructor_exists():
    assert callable(tym::Or.__init__)


def test_tym::or_constructor_args():
    sig = inspect.signature(tym::Or.__init__)
    params = list(sig.parameters.keys())



def test_tym::expression_is_not_abstract():
    assert not inspect.isabstract(tym::Expression)


def test_tym::expression_constructor_exists():
    assert callable(tym::Expression.__init__)


def test_tym::expression_constructor_args():
    sig = inspect.signature(tym::Expression.__init__)
    params = list(sig.parameters.keys())



def test_abstractelement_is_not_abstract():
    assert not inspect.isabstract(AbstractElement)


def test_abstractelement_constructor_exists():
    assert callable(AbstractElement.__init__)


def test_abstractelement_constructor_args():
    sig = inspect.signature(AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_tym::loopstatement_is_not_abstract():
    assert not inspect.isabstract(tym::LoopStatement)


def test_tym::loopstatement_constructor_exists():
    assert callable(tym::LoopStatement.__init__)


def test_tym::loopstatement_constructor_args():
    sig = inspect.signature(tym::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_tym::return_is_not_abstract():
    assert not inspect.isabstract(tym::Return)


def test_tym::return_constructor_exists():
    assert callable(tym::Return.__init__)


def test_tym::return_constructor_args():
    sig = inspect.signature(tym::Return.__init__)
    params = list(sig.parameters.keys())



def test_tym::printstatement_is_not_abstract():
    assert not inspect.isabstract(tym::PrintStatement)


def test_tym::printstatement_constructor_exists():
    assert callable(tym::PrintStatement.__init__)


def test_tym::printstatement_constructor_args():
    sig = inspect.signature(tym::PrintStatement.__init__)
    params = list(sig.parameters.keys())



def test_tym::functioncall_is_not_abstract():
    assert not inspect.isabstract(tym::FunctionCall)


def test_tym::functioncall_constructor_exists():
    assert callable(tym::FunctionCall.__init__)


def test_tym::functioncall_constructor_args():
    sig = inspect.signature(tym::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_tym::teststatement_is_not_abstract():
    assert not inspect.isabstract(tym::TestStatement)


def test_tym::teststatement_constructor_exists():
    assert callable(tym::TestStatement.__init__)


def test_tym::teststatement_constructor_args():
    sig = inspect.signature(tym::TestStatement.__init__)
    params = list(sig.parameters.keys())



def test_tym::variable_is_not_abstract():
    assert not inspect.isabstract(tym::Variable)


def test_tym::variable_constructor_exists():
    assert callable(tym::Variable.__init__)


def test_tym::variable_constructor_args():
    sig = inspect.signature(tym::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "vartype" in params, "Missing parameter 'vartype'"
    assert "name" in params, "Missing parameter 'name'"

def test_tym::variable_has_vartype():
    assert hasattr(tym::Variable, "vartype")
    descriptor = None
    for klass in tym::Variable.__mro__:
        if "vartype" in klass.__dict__:
            descriptor = klass.__dict__["vartype"]
            break
    assert isinstance(descriptor, property)

def test_tym::variable_has_name():
    assert hasattr(tym::Variable, "name")
    descriptor = None
    for klass in tym::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tym::abstractelement_is_not_abstract():
    assert not inspect.isabstract(tym::AbstractElement)


def test_tym::abstractelement_constructor_exists():
    assert callable(tym::AbstractElement.__init__)


def test_tym::abstractelement_constructor_args():
    sig = inspect.signature(tym::AbstractElement.__init__)
    params = list(sig.parameters.keys())



def test_tym::eobject_is_not_abstract():
    assert not inspect.isabstract(tym::EObject)


def test_tym::eobject_constructor_exists():
    assert callable(tym::EObject.__init__)


def test_tym::eobject_constructor_args():
    sig = inspect.signature(tym::EObject.__init__)
    params = list(sig.parameters.keys())



def test_tym::model_is_not_abstract():
    assert not inspect.isabstract(tym::Model)


def test_tym::model_constructor_exists():
    assert callable(tym::Model.__init__)


def test_tym::model_constructor_args():
    sig = inspect.signature(tym::Model.__init__)
    params = list(sig.parameters.keys())



def test_tym::functionblock_is_not_abstract():
    assert not inspect.isabstract(tym::FunctionBlock)


def test_tym::functionblock_constructor_exists():
    assert callable(tym::FunctionBlock.__init__)


def test_tym::functionblock_constructor_args():
    sig = inspect.signature(tym::FunctionBlock.__init__)
    params = list(sig.parameters.keys())



def test_tym::function_is_not_abstract():
    assert not inspect.isabstract(tym::Function)


def test_tym::function_constructor_exists():
    assert callable(tym::Function.__init__)


def test_tym::function_constructor_args():
    sig = inspect.signature(tym::Function.__init__)
    params = list(sig.parameters.keys())
    assert "return_" in params, "Missing parameter 'return_'"
    assert "name" in params, "Missing parameter 'name'"

def test_tym::function_has_return_():
    assert hasattr(tym::Function, "return_")
    descriptor = None
    for klass in tym::Function.__mro__:
        if "return_" in klass.__dict__:
            descriptor = klass.__dict__["return_"]
            break
    assert isinstance(descriptor, property)

def test_tym::function_has_name():
    assert hasattr(tym::Function, "name")
    descriptor = None
    for klass in tym::Function.__mro__:
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
tym::Block_strategy = st.builds(
    tym::Block,
)
Expression_strategy = st.builds(
    Expression,
)
tym::MulOrDiv_strategy = st.builds(
    tym::MulOrDiv,
    op=
        safe_text
)
tym::Minus_strategy = st.builds(
    tym::Minus,
)
tym::Equality_strategy = st.builds(
    tym::Equality,
    op=
        safe_text
)
tym::Not_strategy = st.builds(
    tym::Not,
)
tym::Comparison_strategy = st.builds(
    tym::Comparison,
    op=
        safe_text
)
tym::And_strategy = st.builds(
    tym::And,
)
tym::BoolConstant_strategy = st.builds(
    tym::BoolConstant,
    value=
        safe_text
)
tym::VariableRef_strategy = st.builds(
    tym::VariableRef,
)
tym::IntConstant_strategy = st.builds(
    tym::IntConstant,
    value=
        st.integers()
)
tym::Plus_strategy = st.builds(
    tym::Plus,
)
tym::StringConstant_strategy = st.builds(
    tym::StringConstant,
    value=
        safe_text
)
tym::Or_strategy = st.builds(
    tym::Or,
)
tym::Expression_strategy = st.builds(
    tym::Expression,
)
AbstractElement_strategy = st.builds(
    AbstractElement,
)
tym::LoopStatement_strategy = st.builds(
    tym::LoopStatement,
)
tym::Return_strategy = st.builds(
    tym::Return,
)
tym::PrintStatement_strategy = st.builds(
    tym::PrintStatement,
)
tym::FunctionCall_strategy = st.builds(
    tym::FunctionCall,
)
tym::TestStatement_strategy = st.builds(
    tym::TestStatement,
)
tym::Variable_strategy = st.builds(
    tym::Variable,
    vartype=
        safe_text,
    name=
        safe_text
)
tym::AbstractElement_strategy = st.builds(
    tym::AbstractElement,
)
tym::EObject_strategy = st.builds(
    tym::EObject,
)
tym::Model_strategy = st.builds(
    tym::Model,
)
tym::FunctionBlock_strategy = st.builds(
    tym::FunctionBlock,
)
tym::Function_strategy = st.builds(
    tym::Function,
    return_=
        safe_text,
    name=
        safe_text
)

@given(instance=tym::Block_strategy)
@settings(max_examples=50)
def test_tym::block_instantiation(instance):
    assert isinstance(instance, tym::Block)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=tym::MulOrDiv_strategy)
@settings(max_examples=50)
def test_tym::mulordiv_instantiation(instance):
    assert isinstance(instance, tym::MulOrDiv)

@given(instance=tym::MulOrDiv_strategy)
def test_tym::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=tym::MulOrDiv_strategy)
def test_tym::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tym::Minus_strategy)
@settings(max_examples=50)
def test_tym::minus_instantiation(instance):
    assert isinstance(instance, tym::Minus)

@given(instance=tym::Equality_strategy)
@settings(max_examples=50)
def test_tym::equality_instantiation(instance):
    assert isinstance(instance, tym::Equality)

@given(instance=tym::Equality_strategy)
def test_tym::equality_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=tym::Equality_strategy)
def test_tym::equality_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tym::Not_strategy)
@settings(max_examples=50)
def test_tym::not_instantiation(instance):
    assert isinstance(instance, tym::Not)

@given(instance=tym::Comparison_strategy)
@settings(max_examples=50)
def test_tym::comparison_instantiation(instance):
    assert isinstance(instance, tym::Comparison)

@given(instance=tym::Comparison_strategy)
def test_tym::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=tym::Comparison_strategy)
def test_tym::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=tym::And_strategy)
@settings(max_examples=50)
def test_tym::and_instantiation(instance):
    assert isinstance(instance, tym::And)

@given(instance=tym::BoolConstant_strategy)
@settings(max_examples=50)
def test_tym::boolconstant_instantiation(instance):
    assert isinstance(instance, tym::BoolConstant)

@given(instance=tym::BoolConstant_strategy)
def test_tym::boolconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=tym::BoolConstant_strategy)
def test_tym::boolconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tym::VariableRef_strategy)
@settings(max_examples=50)
def test_tym::variableref_instantiation(instance):
    assert isinstance(instance, tym::VariableRef)

@given(instance=tym::IntConstant_strategy)
@settings(max_examples=50)
def test_tym::intconstant_instantiation(instance):
    assert isinstance(instance, tym::IntConstant)

@given(instance=tym::IntConstant_strategy)
def test_tym::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=tym::IntConstant_strategy)
def test_tym::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tym::Plus_strategy)
@settings(max_examples=50)
def test_tym::plus_instantiation(instance):
    assert isinstance(instance, tym::Plus)

@given(instance=tym::StringConstant_strategy)
@settings(max_examples=50)
def test_tym::stringconstant_instantiation(instance):
    assert isinstance(instance, tym::StringConstant)

@given(instance=tym::StringConstant_strategy)
def test_tym::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=tym::StringConstant_strategy)
def test_tym::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=tym::Or_strategy)
@settings(max_examples=50)
def test_tym::or_instantiation(instance):
    assert isinstance(instance, tym::Or)

@given(instance=tym::Expression_strategy)
@settings(max_examples=50)
def test_tym::expression_instantiation(instance):
    assert isinstance(instance, tym::Expression)

@given(instance=AbstractElement_strategy)
@settings(max_examples=50)
def test_abstractelement_instantiation(instance):
    assert isinstance(instance, AbstractElement)

@given(instance=tym::LoopStatement_strategy)
@settings(max_examples=50)
def test_tym::loopstatement_instantiation(instance):
    assert isinstance(instance, tym::LoopStatement)

@given(instance=tym::Return_strategy)
@settings(max_examples=50)
def test_tym::return_instantiation(instance):
    assert isinstance(instance, tym::Return)

@given(instance=tym::PrintStatement_strategy)
@settings(max_examples=50)
def test_tym::printstatement_instantiation(instance):
    assert isinstance(instance, tym::PrintStatement)

@given(instance=tym::FunctionCall_strategy)
@settings(max_examples=50)
def test_tym::functioncall_instantiation(instance):
    assert isinstance(instance, tym::FunctionCall)

@given(instance=tym::TestStatement_strategy)
@settings(max_examples=50)
def test_tym::teststatement_instantiation(instance):
    assert isinstance(instance, tym::TestStatement)

@given(instance=tym::Variable_strategy)
@settings(max_examples=50)
def test_tym::variable_instantiation(instance):
    assert isinstance(instance, tym::Variable)

@given(instance=tym::Variable_strategy)
def test_tym::variable_vartype_type(instance):
    assert isinstance(instance.vartype, str)


@given(instance=tym::Variable_strategy)
def test_tym::variable_vartype_setter(instance):
    original = instance.vartype
    instance.vartype = original
    assert instance.vartype == original

@given(instance=tym::Variable_strategy)
def test_tym::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tym::Variable_strategy)
def test_tym::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=tym::AbstractElement_strategy)
@settings(max_examples=50)
def test_tym::abstractelement_instantiation(instance):
    assert isinstance(instance, tym::AbstractElement)

@given(instance=tym::EObject_strategy)
@settings(max_examples=50)
def test_tym::eobject_instantiation(instance):
    assert isinstance(instance, tym::EObject)

@given(instance=tym::Model_strategy)
@settings(max_examples=50)
def test_tym::model_instantiation(instance):
    assert isinstance(instance, tym::Model)

@given(instance=tym::FunctionBlock_strategy)
@settings(max_examples=50)
def test_tym::functionblock_instantiation(instance):
    assert isinstance(instance, tym::FunctionBlock)

@given(instance=tym::Function_strategy)
@settings(max_examples=50)
def test_tym::function_instantiation(instance):
    assert isinstance(instance, tym::Function)

@given(instance=tym::Function_strategy)
def test_tym::function_return__type(instance):
    assert isinstance(instance.return_, str)


@given(instance=tym::Function_strategy)
def test_tym::function_return__setter(instance):
    original = instance.return_
    instance.return_ = original
    assert instance.return_ == original

@given(instance=tym::Function_strategy)
def test_tym::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=tym::Function_strategy)
def test_tym::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
