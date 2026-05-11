import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression,
    parameterizedExpressionsTestLanguage::RelationalExpression,
    parameterizedExpressionsTestLanguage::YieldExpression,
    parameterizedExpressionsTestLanguage::ShiftExpression,
    parameterizedExpressionsTestLanguage::IndexedAccessExpression,
    parameterizedExpressionsTestLanguage::AssignmentExpression,
    parameterizedExpressionsTestLanguage::IdentifierRef,
    parameterizedExpressionsTestLanguage::Expression,
    parameterizedExpressionsTestLanguage::CommaExpression,
    Statement,
    parameterizedExpressionsTestLanguage::Block,
    parameterizedExpressionsTestLanguage::ExpressionStatement,
    parameterizedExpressionsTestLanguage::LabelledStatement,
    parameterizedExpressionsTestLanguage::FunctionDeclaration,
    parameterizedExpressionsTestLanguage::Statement,
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



def test_parameterizedexpressionstestlanguage::parameterizedpropertyaccessexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression)


def test_parameterizedexpressionstestlanguage::parameterizedpropertyaccessexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression.__init__)


def test_parameterizedexpressionstestlanguage::parameterizedpropertyaccessexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression.__init__)
    params = list(sig.parameters.keys())
    assert "_property" in params, "Missing parameter '_property'"

def test_parameterizedexpressionstestlanguage::parameterizedpropertyaccessexpression_has__property():
    assert hasattr(parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression, "_property")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression.__mro__:
        if "_property" in klass.__dict__:
            descriptor = klass.__dict__["_property"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedexpressionstestlanguage::relationalexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::RelationalExpression)


def test_parameterizedexpressionstestlanguage::relationalexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::RelationalExpression.__init__)


def test_parameterizedexpressionstestlanguage::relationalexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::RelationalExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_parameterizedexpressionstestlanguage::relationalexpression_has_op():
    assert hasattr(parameterizedExpressionsTestLanguage::RelationalExpression, "op")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::RelationalExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedexpressionstestlanguage::yieldexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::YieldExpression)


def test_parameterizedexpressionstestlanguage::yieldexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::YieldExpression.__init__)


def test_parameterizedexpressionstestlanguage::yieldexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::YieldExpression.__init__)
    params = list(sig.parameters.keys())
    assert "many" in params, "Missing parameter 'many'"

def test_parameterizedexpressionstestlanguage::yieldexpression_has_many():
    assert hasattr(parameterizedExpressionsTestLanguage::YieldExpression, "many")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::YieldExpression.__mro__:
        if "many" in klass.__dict__:
            descriptor = klass.__dict__["many"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedexpressionstestlanguage::shiftexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::ShiftExpression)


def test_parameterizedexpressionstestlanguage::shiftexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::ShiftExpression.__init__)


def test_parameterizedexpressionstestlanguage::shiftexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::ShiftExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_parameterizedexpressionstestlanguage::shiftexpression_has_op():
    assert hasattr(parameterizedExpressionsTestLanguage::ShiftExpression, "op")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::ShiftExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedexpressionstestlanguage::indexedaccessexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::IndexedAccessExpression)


def test_parameterizedexpressionstestlanguage::indexedaccessexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::IndexedAccessExpression.__init__)


def test_parameterizedexpressionstestlanguage::indexedaccessexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::IndexedAccessExpression.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpressionstestlanguage::assignmentexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::AssignmentExpression)


def test_parameterizedexpressionstestlanguage::assignmentexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::AssignmentExpression.__init__)


def test_parameterizedexpressionstestlanguage::assignmentexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::AssignmentExpression.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_parameterizedexpressionstestlanguage::assignmentexpression_has_op():
    assert hasattr(parameterizedExpressionsTestLanguage::AssignmentExpression, "op")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::AssignmentExpression.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedexpressionstestlanguage::identifierref_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::IdentifierRef)


def test_parameterizedexpressionstestlanguage::identifierref_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::IdentifierRef.__init__)


def test_parameterizedexpressionstestlanguage::identifierref_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::IdentifierRef.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_parameterizedexpressionstestlanguage::identifierref_has_id():
    assert hasattr(parameterizedExpressionsTestLanguage::IdentifierRef, "id")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::IdentifierRef.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedexpressionstestlanguage::expression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::Expression)


def test_parameterizedexpressionstestlanguage::expression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::Expression.__init__)


def test_parameterizedexpressionstestlanguage::expression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::Expression.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpressionstestlanguage::commaexpression_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::CommaExpression)


def test_parameterizedexpressionstestlanguage::commaexpression_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::CommaExpression.__init__)


def test_parameterizedexpressionstestlanguage::commaexpression_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::CommaExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpressionstestlanguage::block_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::Block)


def test_parameterizedexpressionstestlanguage::block_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::Block.__init__)


def test_parameterizedexpressionstestlanguage::block_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::Block.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpressionstestlanguage::expressionstatement_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::ExpressionStatement)


def test_parameterizedexpressionstestlanguage::expressionstatement_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::ExpressionStatement.__init__)


def test_parameterizedexpressionstestlanguage::expressionstatement_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::ExpressionStatement.__init__)
    params = list(sig.parameters.keys())



def test_parameterizedexpressionstestlanguage::labelledstatement_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::LabelledStatement)


def test_parameterizedexpressionstestlanguage::labelledstatement_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::LabelledStatement.__init__)


def test_parameterizedexpressionstestlanguage::labelledstatement_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::LabelledStatement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_parameterizedexpressionstestlanguage::labelledstatement_has_name():
    assert hasattr(parameterizedExpressionsTestLanguage::LabelledStatement, "name")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::LabelledStatement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedexpressionstestlanguage::functiondeclaration_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::FunctionDeclaration)


def test_parameterizedexpressionstestlanguage::functiondeclaration_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::FunctionDeclaration.__init__)


def test_parameterizedexpressionstestlanguage::functiondeclaration_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::FunctionDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "generator" in params, "Missing parameter 'generator'"

def test_parameterizedexpressionstestlanguage::functiondeclaration_has_name():
    assert hasattr(parameterizedExpressionsTestLanguage::FunctionDeclaration, "name")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::FunctionDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_parameterizedexpressionstestlanguage::functiondeclaration_has_generator():
    assert hasattr(parameterizedExpressionsTestLanguage::FunctionDeclaration, "generator")
    descriptor = None
    for klass in parameterizedExpressionsTestLanguage::FunctionDeclaration.__mro__:
        if "generator" in klass.__dict__:
            descriptor = klass.__dict__["generator"]
            break
    assert isinstance(descriptor, property)



def test_parameterizedexpressionstestlanguage::statement_is_not_abstract():
    assert not inspect.isabstract(parameterizedExpressionsTestLanguage::Statement)


def test_parameterizedexpressionstestlanguage::statement_constructor_exists():
    assert callable(parameterizedExpressionsTestLanguage::Statement.__init__)


def test_parameterizedexpressionstestlanguage::statement_constructor_args():
    sig = inspect.signature(parameterizedExpressionsTestLanguage::Statement.__init__)
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
parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression,
    _property=
        safe_text
)
parameterizedExpressionsTestLanguage::RelationalExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage::RelationalExpression,
    op=
        safe_text
)
parameterizedExpressionsTestLanguage::YieldExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage::YieldExpression,
    many=
        st.booleans()
)
parameterizedExpressionsTestLanguage::ShiftExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage::ShiftExpression,
    op=
        safe_text
)
parameterizedExpressionsTestLanguage::IndexedAccessExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage::IndexedAccessExpression,
)
parameterizedExpressionsTestLanguage::AssignmentExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage::AssignmentExpression,
    op=
        safe_text
)
parameterizedExpressionsTestLanguage::IdentifierRef_strategy = st.builds(
    parameterizedExpressionsTestLanguage::IdentifierRef,
    id=
        safe_text
)
parameterizedExpressionsTestLanguage::Expression_strategy = st.builds(
    parameterizedExpressionsTestLanguage::Expression,
)
parameterizedExpressionsTestLanguage::CommaExpression_strategy = st.builds(
    parameterizedExpressionsTestLanguage::CommaExpression,
)
Statement_strategy = st.builds(
    Statement,
)
parameterizedExpressionsTestLanguage::Block_strategy = st.builds(
    parameterizedExpressionsTestLanguage::Block,
)
parameterizedExpressionsTestLanguage::ExpressionStatement_strategy = st.builds(
    parameterizedExpressionsTestLanguage::ExpressionStatement,
)
parameterizedExpressionsTestLanguage::LabelledStatement_strategy = st.builds(
    parameterizedExpressionsTestLanguage::LabelledStatement,
    name=
        safe_text
)
parameterizedExpressionsTestLanguage::FunctionDeclaration_strategy = st.builds(
    parameterizedExpressionsTestLanguage::FunctionDeclaration,
    name=
        safe_text,
    generator=
        st.booleans()
)
parameterizedExpressionsTestLanguage::Statement_strategy = st.builds(
    parameterizedExpressionsTestLanguage::Statement,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::parameterizedpropertyaccessexpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression)

@given(instance=parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression_strategy)
def test_parameterizedexpressionstestlanguage::parameterizedpropertyaccessexpression__property_type(instance):
    assert isinstance(instance._property, str)


@given(instance=parameterizedExpressionsTestLanguage::ParameterizedPropertyAccessExpression_strategy)
def test_parameterizedexpressionstestlanguage::parameterizedpropertyaccessexpression__property_setter(instance):
    original = instance._property
    instance._property = original
    assert instance._property == original

@given(instance=parameterizedExpressionsTestLanguage::RelationalExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::relationalexpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::RelationalExpression)

@given(instance=parameterizedExpressionsTestLanguage::RelationalExpression_strategy)
def test_parameterizedexpressionstestlanguage::relationalexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=parameterizedExpressionsTestLanguage::RelationalExpression_strategy)
def test_parameterizedexpressionstestlanguage::relationalexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=parameterizedExpressionsTestLanguage::YieldExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::yieldexpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::YieldExpression)

@given(instance=parameterizedExpressionsTestLanguage::YieldExpression_strategy)
def test_parameterizedexpressionstestlanguage::yieldexpression_many_type(instance):
    assert isinstance(instance.many, bool)


@given(instance=parameterizedExpressionsTestLanguage::YieldExpression_strategy)
def test_parameterizedexpressionstestlanguage::yieldexpression_many_setter(instance):
    original = instance.many
    instance.many = original
    assert instance.many == original

@given(instance=parameterizedExpressionsTestLanguage::ShiftExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::shiftexpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::ShiftExpression)

@given(instance=parameterizedExpressionsTestLanguage::ShiftExpression_strategy)
def test_parameterizedexpressionstestlanguage::shiftexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=parameterizedExpressionsTestLanguage::ShiftExpression_strategy)
def test_parameterizedexpressionstestlanguage::shiftexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=parameterizedExpressionsTestLanguage::IndexedAccessExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::indexedaccessexpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::IndexedAccessExpression)

@given(instance=parameterizedExpressionsTestLanguage::AssignmentExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::assignmentexpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::AssignmentExpression)

@given(instance=parameterizedExpressionsTestLanguage::AssignmentExpression_strategy)
def test_parameterizedexpressionstestlanguage::assignmentexpression_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=parameterizedExpressionsTestLanguage::AssignmentExpression_strategy)
def test_parameterizedexpressionstestlanguage::assignmentexpression_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=parameterizedExpressionsTestLanguage::IdentifierRef_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::identifierref_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::IdentifierRef)

@given(instance=parameterizedExpressionsTestLanguage::IdentifierRef_strategy)
def test_parameterizedexpressionstestlanguage::identifierref_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=parameterizedExpressionsTestLanguage::IdentifierRef_strategy)
def test_parameterizedexpressionstestlanguage::identifierref_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=parameterizedExpressionsTestLanguage::Expression_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::expression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::Expression)

@given(instance=parameterizedExpressionsTestLanguage::CommaExpression_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::commaexpression_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::CommaExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=parameterizedExpressionsTestLanguage::Block_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::block_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::Block)

@given(instance=parameterizedExpressionsTestLanguage::ExpressionStatement_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::expressionstatement_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::ExpressionStatement)

@given(instance=parameterizedExpressionsTestLanguage::LabelledStatement_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::labelledstatement_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::LabelledStatement)

@given(instance=parameterizedExpressionsTestLanguage::LabelledStatement_strategy)
def test_parameterizedexpressionstestlanguage::labelledstatement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=parameterizedExpressionsTestLanguage::LabelledStatement_strategy)
def test_parameterizedexpressionstestlanguage::labelledstatement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=parameterizedExpressionsTestLanguage::FunctionDeclaration_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::functiondeclaration_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::FunctionDeclaration)

@given(instance=parameterizedExpressionsTestLanguage::FunctionDeclaration_strategy)
def test_parameterizedexpressionstestlanguage::functiondeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=parameterizedExpressionsTestLanguage::FunctionDeclaration_strategy)
def test_parameterizedexpressionstestlanguage::functiondeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=parameterizedExpressionsTestLanguage::FunctionDeclaration_strategy)
def test_parameterizedexpressionstestlanguage::functiondeclaration_generator_type(instance):
    assert isinstance(instance.generator, bool)


@given(instance=parameterizedExpressionsTestLanguage::FunctionDeclaration_strategy)
def test_parameterizedexpressionstestlanguage::functiondeclaration_generator_setter(instance):
    original = instance.generator
    instance.generator = original
    assert instance.generator == original

@given(instance=parameterizedExpressionsTestLanguage::Statement_strategy)
@settings(max_examples=50)
def test_parameterizedexpressionstestlanguage::statement_instantiation(instance):
    assert isinstance(instance, parameterizedExpressionsTestLanguage::Statement)
