import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    expressionDSL::UnaryMinus,
    expressionDSL::Exponent,
    expressionDSL::IntConstant,
    expressionDSL::QualifiedRef,
    expressionDSL::BinaryMinus,
    expressionDSL::UnaryPlus,
    expressionDSL::Or,
    expressionDSL::BooleanConstant,
    expressionDSL::And,
    expressionDSL::Not,
    expressionDSL::MulOrDiv,
    expressionDSL::StringConstant,
    expressionDSL::VariableArrayOrFunctionRef,
    expressionDSL::Named,
    expressionDSL::FunctionCall,
    expressionDSL::Expression,
    expressionDSL::BinaryPlus,
    expressionDSL::Comparison,
    SubField,
    expressionDSL::Dim,
    Named,
    Statement,
    expressionDSL::VariableAssignment,
    expressionDSL::FunctionCallStatement,
    expressionDSL::ConstDef,
    expressionDSL::StructDef,
    expressionDSL::VariableDef,
    expressionDSL::Statement,
    expressionDSL::Model,
    expressionDSL::FunctionDef,
    expressionDSL::SubFieldDef,
    expressionDSL::SubField,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::unaryminus_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::UnaryMinus)


def test_expressiondsl::unaryminus_constructor_exists():
    assert callable(expressionDSL::UnaryMinus.__init__)


def test_expressiondsl::unaryminus_constructor_args():
    sig = inspect.signature(expressionDSL::UnaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::exponent_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Exponent)


def test_expressiondsl::exponent_constructor_exists():
    assert callable(expressionDSL::Exponent.__init__)


def test_expressiondsl::exponent_constructor_args():
    sig = inspect.signature(expressionDSL::Exponent.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::intconstant_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::IntConstant)


def test_expressiondsl::intconstant_constructor_exists():
    assert callable(expressionDSL::IntConstant.__init__)


def test_expressiondsl::intconstant_constructor_args():
    sig = inspect.signature(expressionDSL::IntConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressiondsl::intconstant_has_value():
    assert hasattr(expressionDSL::IntConstant, "value")
    descriptor = None
    for klass in expressionDSL::IntConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::qualifiedref_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::QualifiedRef)


def test_expressiondsl::qualifiedref_constructor_exists():
    assert callable(expressionDSL::QualifiedRef.__init__)


def test_expressiondsl::qualifiedref_constructor_args():
    sig = inspect.signature(expressionDSL::QualifiedRef.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::binaryminus_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::BinaryMinus)


def test_expressiondsl::binaryminus_constructor_exists():
    assert callable(expressionDSL::BinaryMinus.__init__)


def test_expressiondsl::binaryminus_constructor_args():
    sig = inspect.signature(expressionDSL::BinaryMinus.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::unaryplus_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::UnaryPlus)


def test_expressiondsl::unaryplus_constructor_exists():
    assert callable(expressionDSL::UnaryPlus.__init__)


def test_expressiondsl::unaryplus_constructor_args():
    sig = inspect.signature(expressionDSL::UnaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::or_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Or)


def test_expressiondsl::or_constructor_exists():
    assert callable(expressionDSL::Or.__init__)


def test_expressiondsl::or_constructor_args():
    sig = inspect.signature(expressionDSL::Or.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::booleanconstant_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::BooleanConstant)


def test_expressiondsl::booleanconstant_constructor_exists():
    assert callable(expressionDSL::BooleanConstant.__init__)


def test_expressiondsl::booleanconstant_constructor_args():
    sig = inspect.signature(expressionDSL::BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressiondsl::booleanconstant_has_value():
    assert hasattr(expressionDSL::BooleanConstant, "value")
    descriptor = None
    for klass in expressionDSL::BooleanConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::and_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::And)


def test_expressiondsl::and_constructor_exists():
    assert callable(expressionDSL::And.__init__)


def test_expressiondsl::and_constructor_args():
    sig = inspect.signature(expressionDSL::And.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::not_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Not)


def test_expressiondsl::not_constructor_exists():
    assert callable(expressionDSL::Not.__init__)


def test_expressiondsl::not_constructor_args():
    sig = inspect.signature(expressionDSL::Not.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::mulordiv_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::MulOrDiv)


def test_expressiondsl::mulordiv_constructor_exists():
    assert callable(expressionDSL::MulOrDiv.__init__)


def test_expressiondsl::mulordiv_constructor_args():
    sig = inspect.signature(expressionDSL::MulOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expressiondsl::mulordiv_has_op():
    assert hasattr(expressionDSL::MulOrDiv, "op")
    descriptor = None
    for klass in expressionDSL::MulOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::stringconstant_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::StringConstant)


def test_expressiondsl::stringconstant_constructor_exists():
    assert callable(expressionDSL::StringConstant.__init__)


def test_expressiondsl::stringconstant_constructor_args():
    sig = inspect.signature(expressionDSL::StringConstant.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_expressiondsl::stringconstant_has_value():
    assert hasattr(expressionDSL::StringConstant, "value")
    descriptor = None
    for klass in expressionDSL::StringConstant.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::variablearrayorfunctionref_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::VariableArrayOrFunctionRef)


def test_expressiondsl::variablearrayorfunctionref_constructor_exists():
    assert callable(expressionDSL::VariableArrayOrFunctionRef.__init__)


def test_expressiondsl::variablearrayorfunctionref_constructor_args():
    sig = inspect.signature(expressionDSL::VariableArrayOrFunctionRef.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::named_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Named)


def test_expressiondsl::named_constructor_exists():
    assert callable(expressionDSL::Named.__init__)


def test_expressiondsl::named_constructor_args():
    sig = inspect.signature(expressionDSL::Named.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_expressiondsl::named_has_name():
    assert hasattr(expressionDSL::Named, "name")
    descriptor = None
    for klass in expressionDSL::Named.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::functioncall_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::FunctionCall)


def test_expressiondsl::functioncall_constructor_exists():
    assert callable(expressionDSL::FunctionCall.__init__)


def test_expressiondsl::functioncall_constructor_args():
    sig = inspect.signature(expressionDSL::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::expression_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Expression)


def test_expressiondsl::expression_constructor_exists():
    assert callable(expressionDSL::Expression.__init__)


def test_expressiondsl::expression_constructor_args():
    sig = inspect.signature(expressionDSL::Expression.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::binaryplus_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::BinaryPlus)


def test_expressiondsl::binaryplus_constructor_exists():
    assert callable(expressionDSL::BinaryPlus.__init__)


def test_expressiondsl::binaryplus_constructor_args():
    sig = inspect.signature(expressionDSL::BinaryPlus.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::comparison_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Comparison)


def test_expressiondsl::comparison_constructor_exists():
    assert callable(expressionDSL::Comparison.__init__)


def test_expressiondsl::comparison_constructor_args():
    sig = inspect.signature(expressionDSL::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expressiondsl::comparison_has_op():
    assert hasattr(expressionDSL::Comparison, "op")
    descriptor = None
    for klass in expressionDSL::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_subfield_is_not_abstract():
    assert not inspect.isabstract(SubField)


def test_subfield_constructor_exists():
    assert callable(SubField.__init__)


def test_subfield_constructor_args():
    sig = inspect.signature(SubField.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::dim_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Dim)


def test_expressiondsl::dim_constructor_exists():
    assert callable(expressionDSL::Dim.__init__)


def test_expressiondsl::dim_constructor_args():
    sig = inspect.signature(expressionDSL::Dim.__init__)
    params = list(sig.parameters.keys())
    assert "arrayDimensions" in params, "Missing parameter 'arrayDimensions'"

def test_expressiondsl::dim_has_arrayDimensions():
    assert hasattr(expressionDSL::Dim, "arrayDimensions")
    descriptor = None
    for klass in expressionDSL::Dim.__mro__:
        if "arrayDimensions" in klass.__dict__:
            descriptor = klass.__dict__["arrayDimensions"]
            break
    assert isinstance(descriptor, property)



def test_named_is_not_abstract():
    assert not inspect.isabstract(Named)


def test_named_constructor_exists():
    assert callable(Named.__init__)


def test_named_constructor_args():
    sig = inspect.signature(Named.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::variableassignment_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::VariableAssignment)


def test_expressiondsl::variableassignment_constructor_exists():
    assert callable(expressionDSL::VariableAssignment.__init__)


def test_expressiondsl::variableassignment_constructor_args():
    sig = inspect.signature(expressionDSL::VariableAssignment.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_expressiondsl::variableassignment_has_op():
    assert hasattr(expressionDSL::VariableAssignment, "op")
    descriptor = None
    for klass in expressionDSL::VariableAssignment.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::FunctionCallStatement)


def test_expressiondsl::functioncallstatement_constructor_exists():
    assert callable(expressionDSL::FunctionCallStatement.__init__)


def test_expressiondsl::functioncallstatement_constructor_args():
    sig = inspect.signature(expressionDSL::FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::constdef_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::ConstDef)


def test_expressiondsl::constdef_constructor_exists():
    assert callable(expressionDSL::ConstDef.__init__)


def test_expressiondsl::constdef_constructor_args():
    sig = inspect.signature(expressionDSL::ConstDef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_expressiondsl::constdef_has_type():
    assert hasattr(expressionDSL::ConstDef, "type")
    descriptor = None
    for klass in expressionDSL::ConstDef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::structdef_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::StructDef)


def test_expressiondsl::structdef_constructor_exists():
    assert callable(expressionDSL::StructDef.__init__)


def test_expressiondsl::structdef_constructor_args():
    sig = inspect.signature(expressionDSL::StructDef.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::variabledef_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::VariableDef)


def test_expressiondsl::variabledef_constructor_exists():
    assert callable(expressionDSL::VariableDef.__init__)


def test_expressiondsl::variabledef_constructor_args():
    sig = inspect.signature(expressionDSL::VariableDef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_expressiondsl::variabledef_has_type():
    assert hasattr(expressionDSL::VariableDef, "type")
    descriptor = None
    for klass in expressionDSL::VariableDef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::statement_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Statement)


def test_expressiondsl::statement_constructor_exists():
    assert callable(expressionDSL::Statement.__init__)


def test_expressiondsl::statement_constructor_args():
    sig = inspect.signature(expressionDSL::Statement.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::model_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::Model)


def test_expressiondsl::model_constructor_exists():
    assert callable(expressionDSL::Model.__init__)


def test_expressiondsl::model_constructor_args():
    sig = inspect.signature(expressionDSL::Model.__init__)
    params = list(sig.parameters.keys())



def test_expressiondsl::functiondef_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::FunctionDef)


def test_expressiondsl::functiondef_constructor_exists():
    assert callable(expressionDSL::FunctionDef.__init__)


def test_expressiondsl::functiondef_constructor_args():
    sig = inspect.signature(expressionDSL::FunctionDef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_expressiondsl::functiondef_has_type():
    assert hasattr(expressionDSL::FunctionDef, "type")
    descriptor = None
    for klass in expressionDSL::FunctionDef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::subfielddef_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::SubFieldDef)


def test_expressiondsl::subfielddef_constructor_exists():
    assert callable(expressionDSL::SubFieldDef.__init__)


def test_expressiondsl::subfielddef_constructor_args():
    sig = inspect.signature(expressionDSL::SubFieldDef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_expressiondsl::subfielddef_has_type():
    assert hasattr(expressionDSL::SubFieldDef, "type")
    descriptor = None
    for klass in expressionDSL::SubFieldDef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_expressiondsl::subfield_is_not_abstract():
    assert not inspect.isabstract(expressionDSL::SubField)


def test_expressiondsl::subfield_constructor_exists():
    assert callable(expressionDSL::SubField.__init__)


def test_expressiondsl::subfield_constructor_args():
    sig = inspect.signature(expressionDSL::SubField.__init__)
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
Expression_strategy = st.builds(
    Expression,
)
expressionDSL::UnaryMinus_strategy = st.builds(
    expressionDSL::UnaryMinus,
)
expressionDSL::Exponent_strategy = st.builds(
    expressionDSL::Exponent,
)
expressionDSL::IntConstant_strategy = st.builds(
    expressionDSL::IntConstant,
    value=
        st.integers()
)
expressionDSL::QualifiedRef_strategy = st.builds(
    expressionDSL::QualifiedRef,
)
expressionDSL::BinaryMinus_strategy = st.builds(
    expressionDSL::BinaryMinus,
)
expressionDSL::UnaryPlus_strategy = st.builds(
    expressionDSL::UnaryPlus,
)
expressionDSL::Or_strategy = st.builds(
    expressionDSL::Or,
)
expressionDSL::BooleanConstant_strategy = st.builds(
    expressionDSL::BooleanConstant,
    value=
        safe_text
)
expressionDSL::And_strategy = st.builds(
    expressionDSL::And,
)
expressionDSL::Not_strategy = st.builds(
    expressionDSL::Not,
)
expressionDSL::MulOrDiv_strategy = st.builds(
    expressionDSL::MulOrDiv,
    op=
        safe_text
)
expressionDSL::StringConstant_strategy = st.builds(
    expressionDSL::StringConstant,
    value=
        safe_text
)
expressionDSL::VariableArrayOrFunctionRef_strategy = st.builds(
    expressionDSL::VariableArrayOrFunctionRef,
)
expressionDSL::Named_strategy = st.builds(
    expressionDSL::Named,
    name=
        safe_text
)
expressionDSL::FunctionCall_strategy = st.builds(
    expressionDSL::FunctionCall,
)
expressionDSL::Expression_strategy = st.builds(
    expressionDSL::Expression,
)
expressionDSL::BinaryPlus_strategy = st.builds(
    expressionDSL::BinaryPlus,
)
expressionDSL::Comparison_strategy = st.builds(
    expressionDSL::Comparison,
    op=
        safe_text
)
SubField_strategy = st.builds(
    SubField,
)
expressionDSL::Dim_strategy = st.builds(
    expressionDSL::Dim,
    arrayDimensions=
        st.integers()
)
Named_strategy = st.builds(
    Named,
)
Statement_strategy = st.builds(
    Statement,
)
expressionDSL::VariableAssignment_strategy = st.builds(
    expressionDSL::VariableAssignment,
    op=
        safe_text
)
expressionDSL::FunctionCallStatement_strategy = st.builds(
    expressionDSL::FunctionCallStatement,
)
expressionDSL::ConstDef_strategy = st.builds(
    expressionDSL::ConstDef,
    type=
        safe_text
)
expressionDSL::StructDef_strategy = st.builds(
    expressionDSL::StructDef,
)
expressionDSL::VariableDef_strategy = st.builds(
    expressionDSL::VariableDef,
    type=
        safe_text
)
expressionDSL::Statement_strategy = st.builds(
    expressionDSL::Statement,
)
expressionDSL::Model_strategy = st.builds(
    expressionDSL::Model,
)
expressionDSL::FunctionDef_strategy = st.builds(
    expressionDSL::FunctionDef,
    type=
        safe_text
)
expressionDSL::SubFieldDef_strategy = st.builds(
    expressionDSL::SubFieldDef,
    type=
        safe_text
)
expressionDSL::SubField_strategy = st.builds(
    expressionDSL::SubField,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=expressionDSL::UnaryMinus_strategy)
@settings(max_examples=50)
def test_expressiondsl::unaryminus_instantiation(instance):
    assert isinstance(instance, expressionDSL::UnaryMinus)

@given(instance=expressionDSL::Exponent_strategy)
@settings(max_examples=50)
def test_expressiondsl::exponent_instantiation(instance):
    assert isinstance(instance, expressionDSL::Exponent)

@given(instance=expressionDSL::IntConstant_strategy)
@settings(max_examples=50)
def test_expressiondsl::intconstant_instantiation(instance):
    assert isinstance(instance, expressionDSL::IntConstant)

@given(instance=expressionDSL::IntConstant_strategy)
def test_expressiondsl::intconstant_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=expressionDSL::IntConstant_strategy)
def test_expressiondsl::intconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressionDSL::QualifiedRef_strategy)
@settings(max_examples=50)
def test_expressiondsl::qualifiedref_instantiation(instance):
    assert isinstance(instance, expressionDSL::QualifiedRef)

@given(instance=expressionDSL::BinaryMinus_strategy)
@settings(max_examples=50)
def test_expressiondsl::binaryminus_instantiation(instance):
    assert isinstance(instance, expressionDSL::BinaryMinus)

@given(instance=expressionDSL::UnaryPlus_strategy)
@settings(max_examples=50)
def test_expressiondsl::unaryplus_instantiation(instance):
    assert isinstance(instance, expressionDSL::UnaryPlus)

@given(instance=expressionDSL::Or_strategy)
@settings(max_examples=50)
def test_expressiondsl::or_instantiation(instance):
    assert isinstance(instance, expressionDSL::Or)

@given(instance=expressionDSL::BooleanConstant_strategy)
@settings(max_examples=50)
def test_expressiondsl::booleanconstant_instantiation(instance):
    assert isinstance(instance, expressionDSL::BooleanConstant)

@given(instance=expressionDSL::BooleanConstant_strategy)
def test_expressiondsl::booleanconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expressionDSL::BooleanConstant_strategy)
def test_expressiondsl::booleanconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressionDSL::And_strategy)
@settings(max_examples=50)
def test_expressiondsl::and_instantiation(instance):
    assert isinstance(instance, expressionDSL::And)

@given(instance=expressionDSL::Not_strategy)
@settings(max_examples=50)
def test_expressiondsl::not_instantiation(instance):
    assert isinstance(instance, expressionDSL::Not)

@given(instance=expressionDSL::MulOrDiv_strategy)
@settings(max_examples=50)
def test_expressiondsl::mulordiv_instantiation(instance):
    assert isinstance(instance, expressionDSL::MulOrDiv)

@given(instance=expressionDSL::MulOrDiv_strategy)
def test_expressiondsl::mulordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expressionDSL::MulOrDiv_strategy)
def test_expressiondsl::mulordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expressionDSL::StringConstant_strategy)
@settings(max_examples=50)
def test_expressiondsl::stringconstant_instantiation(instance):
    assert isinstance(instance, expressionDSL::StringConstant)

@given(instance=expressionDSL::StringConstant_strategy)
def test_expressiondsl::stringconstant_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=expressionDSL::StringConstant_strategy)
def test_expressiondsl::stringconstant_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=expressionDSL::VariableArrayOrFunctionRef_strategy)
@settings(max_examples=50)
def test_expressiondsl::variablearrayorfunctionref_instantiation(instance):
    assert isinstance(instance, expressionDSL::VariableArrayOrFunctionRef)

@given(instance=expressionDSL::Named_strategy)
@settings(max_examples=50)
def test_expressiondsl::named_instantiation(instance):
    assert isinstance(instance, expressionDSL::Named)

@given(instance=expressionDSL::Named_strategy)
def test_expressiondsl::named_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=expressionDSL::Named_strategy)
def test_expressiondsl::named_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=expressionDSL::FunctionCall_strategy)
@settings(max_examples=50)
def test_expressiondsl::functioncall_instantiation(instance):
    assert isinstance(instance, expressionDSL::FunctionCall)

@given(instance=expressionDSL::Expression_strategy)
@settings(max_examples=50)
def test_expressiondsl::expression_instantiation(instance):
    assert isinstance(instance, expressionDSL::Expression)

@given(instance=expressionDSL::BinaryPlus_strategy)
@settings(max_examples=50)
def test_expressiondsl::binaryplus_instantiation(instance):
    assert isinstance(instance, expressionDSL::BinaryPlus)

@given(instance=expressionDSL::Comparison_strategy)
@settings(max_examples=50)
def test_expressiondsl::comparison_instantiation(instance):
    assert isinstance(instance, expressionDSL::Comparison)

@given(instance=expressionDSL::Comparison_strategy)
def test_expressiondsl::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expressionDSL::Comparison_strategy)
def test_expressiondsl::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=SubField_strategy)
@settings(max_examples=50)
def test_subfield_instantiation(instance):
    assert isinstance(instance, SubField)

@given(instance=expressionDSL::Dim_strategy)
@settings(max_examples=50)
def test_expressiondsl::dim_instantiation(instance):
    assert isinstance(instance, expressionDSL::Dim)

@given(instance=expressionDSL::Dim_strategy)
def test_expressiondsl::dim_arrayDimensions_type(instance):
    assert isinstance(instance.arrayDimensions, int)


@given(instance=expressionDSL::Dim_strategy)
def test_expressiondsl::dim_arrayDimensions_setter(instance):
    original = instance.arrayDimensions
    instance.arrayDimensions = original
    assert instance.arrayDimensions == original

@given(instance=Named_strategy)
@settings(max_examples=50)
def test_named_instantiation(instance):
    assert isinstance(instance, Named)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=expressionDSL::VariableAssignment_strategy)
@settings(max_examples=50)
def test_expressiondsl::variableassignment_instantiation(instance):
    assert isinstance(instance, expressionDSL::VariableAssignment)

@given(instance=expressionDSL::VariableAssignment_strategy)
def test_expressiondsl::variableassignment_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=expressionDSL::VariableAssignment_strategy)
def test_expressiondsl::variableassignment_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=expressionDSL::FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_expressiondsl::functioncallstatement_instantiation(instance):
    assert isinstance(instance, expressionDSL::FunctionCallStatement)

@given(instance=expressionDSL::ConstDef_strategy)
@settings(max_examples=50)
def test_expressiondsl::constdef_instantiation(instance):
    assert isinstance(instance, expressionDSL::ConstDef)

@given(instance=expressionDSL::ConstDef_strategy)
def test_expressiondsl::constdef_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=expressionDSL::ConstDef_strategy)
def test_expressiondsl::constdef_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=expressionDSL::StructDef_strategy)
@settings(max_examples=50)
def test_expressiondsl::structdef_instantiation(instance):
    assert isinstance(instance, expressionDSL::StructDef)

@given(instance=expressionDSL::VariableDef_strategy)
@settings(max_examples=50)
def test_expressiondsl::variabledef_instantiation(instance):
    assert isinstance(instance, expressionDSL::VariableDef)

@given(instance=expressionDSL::VariableDef_strategy)
def test_expressiondsl::variabledef_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=expressionDSL::VariableDef_strategy)
def test_expressiondsl::variabledef_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=expressionDSL::Statement_strategy)
@settings(max_examples=50)
def test_expressiondsl::statement_instantiation(instance):
    assert isinstance(instance, expressionDSL::Statement)

@given(instance=expressionDSL::Model_strategy)
@settings(max_examples=50)
def test_expressiondsl::model_instantiation(instance):
    assert isinstance(instance, expressionDSL::Model)

@given(instance=expressionDSL::FunctionDef_strategy)
@settings(max_examples=50)
def test_expressiondsl::functiondef_instantiation(instance):
    assert isinstance(instance, expressionDSL::FunctionDef)

@given(instance=expressionDSL::FunctionDef_strategy)
def test_expressiondsl::functiondef_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=expressionDSL::FunctionDef_strategy)
def test_expressiondsl::functiondef_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=expressionDSL::SubFieldDef_strategy)
@settings(max_examples=50)
def test_expressiondsl::subfielddef_instantiation(instance):
    assert isinstance(instance, expressionDSL::SubFieldDef)

@given(instance=expressionDSL::SubFieldDef_strategy)
def test_expressiondsl::subfielddef_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=expressionDSL::SubFieldDef_strategy)
def test_expressiondsl::subfielddef_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=expressionDSL::SubField_strategy)
@settings(max_examples=50)
def test_expressiondsl::subfield_instantiation(instance):
    assert isinstance(instance, expressionDSL::SubField)
