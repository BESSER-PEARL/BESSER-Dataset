import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expr,
    miniJava::Point,
    miniJava::SquareBrackets,
    miniJava::Addition,
    miniJava::Multiplication,
    miniJava::Expression,
    miniJava::MethodCall,
    miniJava::NumberValue,
    miniJava::Expr,
    miniJava::Variable,
    miniJava::Type,
    miniJava::Statement,
    miniJava::Method,
    miniJava::VarDeclaration,
    miniJava::MainMethod,
    miniJava::ClassDecl,
    miniJava::Program,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expr_is_not_abstract():
    assert not inspect.isabstract(Expr)


def test_expr_constructor_exists():
    assert callable(Expr.__init__)


def test_expr_constructor_args():
    sig = inspect.signature(Expr.__init__)
    params = list(sig.parameters.keys())



def test_minijava::point_is_not_abstract():
    assert not inspect.isabstract(miniJava::Point)


def test_minijava::point_constructor_exists():
    assert callable(miniJava::Point.__init__)


def test_minijava::point_constructor_args():
    sig = inspect.signature(miniJava::Point.__init__)
    params = list(sig.parameters.keys())



def test_minijava::squarebrackets_is_not_abstract():
    assert not inspect.isabstract(miniJava::SquareBrackets)


def test_minijava::squarebrackets_constructor_exists():
    assert callable(miniJava::SquareBrackets.__init__)


def test_minijava::squarebrackets_constructor_args():
    sig = inspect.signature(miniJava::SquareBrackets.__init__)
    params = list(sig.parameters.keys())



def test_minijava::addition_is_not_abstract():
    assert not inspect.isabstract(miniJava::Addition)


def test_minijava::addition_constructor_exists():
    assert callable(miniJava::Addition.__init__)


def test_minijava::addition_constructor_args():
    sig = inspect.signature(miniJava::Addition.__init__)
    params = list(sig.parameters.keys())



def test_minijava::multiplication_is_not_abstract():
    assert not inspect.isabstract(miniJava::Multiplication)


def test_minijava::multiplication_constructor_exists():
    assert callable(miniJava::Multiplication.__init__)


def test_minijava::multiplication_constructor_args():
    sig = inspect.signature(miniJava::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_minijava::expression_is_not_abstract():
    assert not inspect.isabstract(miniJava::Expression)


def test_minijava::expression_constructor_exists():
    assert callable(miniJava::Expression.__init__)


def test_minijava::expression_constructor_args():
    sig = inspect.signature(miniJava::Expression.__init__)
    params = list(sig.parameters.keys())



def test_minijava::methodcall_is_not_abstract():
    assert not inspect.isabstract(miniJava::MethodCall)


def test_minijava::methodcall_constructor_exists():
    assert callable(miniJava::MethodCall.__init__)


def test_minijava::methodcall_constructor_args():
    sig = inspect.signature(miniJava::MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_minijava::numbervalue_is_not_abstract():
    assert not inspect.isabstract(miniJava::NumberValue)


def test_minijava::numbervalue_constructor_exists():
    assert callable(miniJava::NumberValue.__init__)


def test_minijava::numbervalue_constructor_args():
    sig = inspect.signature(miniJava::NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava::numbervalue_has_value():
    assert hasattr(miniJava::NumberValue, "value")
    descriptor = None
    for klass in miniJava::NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava::expr_is_not_abstract():
    assert not inspect.isabstract(miniJava::Expr)


def test_minijava::expr_constructor_exists():
    assert callable(miniJava::Expr.__init__)


def test_minijava::expr_constructor_args():
    sig = inspect.signature(miniJava::Expr.__init__)
    params = list(sig.parameters.keys())
    assert "expressionType" in params, "Missing parameter 'expressionType'"

def test_minijava::expr_has_expressionType():
    assert hasattr(miniJava::Expr, "expressionType")
    descriptor = None
    for klass in miniJava::Expr.__mro__:
        if "expressionType" in klass.__dict__:
            descriptor = klass.__dict__["expressionType"]
            break
    assert isinstance(descriptor, property)



def test_minijava::variable_is_not_abstract():
    assert not inspect.isabstract(miniJava::Variable)


def test_minijava::variable_constructor_exists():
    assert callable(miniJava::Variable.__init__)


def test_minijava::variable_constructor_args():
    sig = inspect.signature(miniJava::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava::variable_has_name():
    assert hasattr(miniJava::Variable, "name")
    descriptor = None
    for klass in miniJava::Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minijava::type_is_not_abstract():
    assert not inspect.isabstract(miniJava::Type)


def test_minijava::type_constructor_exists():
    assert callable(miniJava::Type.__init__)


def test_minijava::type_constructor_args():
    sig = inspect.signature(miniJava::Type.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_minijava::type_has_typeName():
    assert hasattr(miniJava::Type, "typeName")
    descriptor = None
    for klass in miniJava::Type.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_minijava::statement_is_not_abstract():
    assert not inspect.isabstract(miniJava::Statement)


def test_minijava::statement_constructor_exists():
    assert callable(miniJava::Statement.__init__)


def test_minijava::statement_constructor_args():
    sig = inspect.signature(miniJava::Statement.__init__)
    params = list(sig.parameters.keys())
    assert "isArrayElementAssignment" in params, "Missing parameter 'isArrayElementAssignment'"
    assert "statementType" in params, "Missing parameter 'statementType'"

def test_minijava::statement_has_isArrayElementAssignment():
    assert hasattr(miniJava::Statement, "isArrayElementAssignment")
    descriptor = None
    for klass in miniJava::Statement.__mro__:
        if "isArrayElementAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isArrayElementAssignment"]
            break
    assert isinstance(descriptor, property)

def test_minijava::statement_has_statementType():
    assert hasattr(miniJava::Statement, "statementType")
    descriptor = None
    for klass in miniJava::Statement.__mro__:
        if "statementType" in klass.__dict__:
            descriptor = klass.__dict__["statementType"]
            break
    assert isinstance(descriptor, property)



def test_minijava::method_is_not_abstract():
    assert not inspect.isabstract(miniJava::Method)


def test_minijava::method_constructor_exists():
    assert callable(miniJava::Method.__init__)


def test_minijava::method_constructor_args():
    sig = inspect.signature(miniJava::Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava::method_has_name():
    assert hasattr(miniJava::Method, "name")
    descriptor = None
    for klass in miniJava::Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minijava::vardeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava::VarDeclaration)


def test_minijava::vardeclaration_constructor_exists():
    assert callable(miniJava::VarDeclaration.__init__)


def test_minijava::vardeclaration_constructor_args():
    sig = inspect.signature(miniJava::VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava::mainmethod_is_not_abstract():
    assert not inspect.isabstract(miniJava::MainMethod)


def test_minijava::mainmethod_constructor_exists():
    assert callable(miniJava::MainMethod.__init__)


def test_minijava::mainmethod_constructor_args():
    sig = inspect.signature(miniJava::MainMethod.__init__)
    params = list(sig.parameters.keys())



def test_minijava::classdecl_is_not_abstract():
    assert not inspect.isabstract(miniJava::ClassDecl)


def test_minijava::classdecl_constructor_exists():
    assert callable(miniJava::ClassDecl.__init__)


def test_minijava::classdecl_constructor_args():
    sig = inspect.signature(miniJava::ClassDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava::classdecl_has_name():
    assert hasattr(miniJava::ClassDecl, "name")
    descriptor = None
    for klass in miniJava::ClassDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minijava::program_is_not_abstract():
    assert not inspect.isabstract(miniJava::Program)


def test_minijava::program_constructor_exists():
    assert callable(miniJava::Program.__init__)


def test_minijava::program_constructor_args():
    sig = inspect.signature(miniJava::Program.__init__)
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
Expr_strategy = st.builds(
    Expr,
)
miniJava::Point_strategy = st.builds(
    miniJava::Point,
)
miniJava::SquareBrackets_strategy = st.builds(
    miniJava::SquareBrackets,
)
miniJava::Addition_strategy = st.builds(
    miniJava::Addition,
)
miniJava::Multiplication_strategy = st.builds(
    miniJava::Multiplication,
)
miniJava::Expression_strategy = st.builds(
    miniJava::Expression,
)
miniJava::MethodCall_strategy = st.builds(
    miniJava::MethodCall,
)
miniJava::NumberValue_strategy = st.builds(
    miniJava::NumberValue,
    value=
        st.integers()
)
miniJava::Expr_strategy = st.builds(
    miniJava::Expr,
    expressionType=
        safe_text
)
miniJava::Variable_strategy = st.builds(
    miniJava::Variable,
    name=
        safe_text
)
miniJava::Type_strategy = st.builds(
    miniJava::Type,
    typeName=
        safe_text
)
miniJava::Statement_strategy = st.builds(
    miniJava::Statement,
    isArrayElementAssignment=
        st.booleans(),
    statementType=
        safe_text
)
miniJava::Method_strategy = st.builds(
    miniJava::Method,
    name=
        safe_text
)
miniJava::VarDeclaration_strategy = st.builds(
    miniJava::VarDeclaration,
)
miniJava::MainMethod_strategy = st.builds(
    miniJava::MainMethod,
)
miniJava::ClassDecl_strategy = st.builds(
    miniJava::ClassDecl,
    name=
        safe_text
)
miniJava::Program_strategy = st.builds(
    miniJava::Program,
)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=miniJava::Point_strategy)
@settings(max_examples=50)
def test_minijava::point_instantiation(instance):
    assert isinstance(instance, miniJava::Point)

@given(instance=miniJava::SquareBrackets_strategy)
@settings(max_examples=50)
def test_minijava::squarebrackets_instantiation(instance):
    assert isinstance(instance, miniJava::SquareBrackets)

@given(instance=miniJava::Addition_strategy)
@settings(max_examples=50)
def test_minijava::addition_instantiation(instance):
    assert isinstance(instance, miniJava::Addition)

@given(instance=miniJava::Multiplication_strategy)
@settings(max_examples=50)
def test_minijava::multiplication_instantiation(instance):
    assert isinstance(instance, miniJava::Multiplication)

@given(instance=miniJava::Expression_strategy)
@settings(max_examples=50)
def test_minijava::expression_instantiation(instance):
    assert isinstance(instance, miniJava::Expression)

@given(instance=miniJava::MethodCall_strategy)
@settings(max_examples=50)
def test_minijava::methodcall_instantiation(instance):
    assert isinstance(instance, miniJava::MethodCall)

@given(instance=miniJava::NumberValue_strategy)
@settings(max_examples=50)
def test_minijava::numbervalue_instantiation(instance):
    assert isinstance(instance, miniJava::NumberValue)

@given(instance=miniJava::NumberValue_strategy)
def test_minijava::numbervalue_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=miniJava::NumberValue_strategy)
def test_minijava::numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava::Expr_strategy)
@settings(max_examples=50)
def test_minijava::expr_instantiation(instance):
    assert isinstance(instance, miniJava::Expr)

@given(instance=miniJava::Expr_strategy)
def test_minijava::expr_expressionType_type(instance):
    assert isinstance(instance.expressionType, str)


@given(instance=miniJava::Expr_strategy)
def test_minijava::expr_expressionType_setter(instance):
    original = instance.expressionType
    instance.expressionType = original
    assert instance.expressionType == original

@given(instance=miniJava::Variable_strategy)
@settings(max_examples=50)
def test_minijava::variable_instantiation(instance):
    assert isinstance(instance, miniJava::Variable)

@given(instance=miniJava::Variable_strategy)
def test_minijava::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniJava::Variable_strategy)
def test_minijava::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniJava::Type_strategy)
@settings(max_examples=50)
def test_minijava::type_instantiation(instance):
    assert isinstance(instance, miniJava::Type)

@given(instance=miniJava::Type_strategy)
def test_minijava::type_typeName_type(instance):
    assert isinstance(instance.typeName, str)


@given(instance=miniJava::Type_strategy)
def test_minijava::type_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=miniJava::Statement_strategy)
@settings(max_examples=50)
def test_minijava::statement_instantiation(instance):
    assert isinstance(instance, miniJava::Statement)

@given(instance=miniJava::Statement_strategy)
def test_minijava::statement_isArrayElementAssignment_type(instance):
    assert isinstance(instance.isArrayElementAssignment, bool)


@given(instance=miniJava::Statement_strategy)
def test_minijava::statement_isArrayElementAssignment_setter(instance):
    original = instance.isArrayElementAssignment
    instance.isArrayElementAssignment = original
    assert instance.isArrayElementAssignment == original

@given(instance=miniJava::Statement_strategy)
def test_minijava::statement_statementType_type(instance):
    assert isinstance(instance.statementType, str)


@given(instance=miniJava::Statement_strategy)
def test_minijava::statement_statementType_setter(instance):
    original = instance.statementType
    instance.statementType = original
    assert instance.statementType == original

@given(instance=miniJava::Method_strategy)
@settings(max_examples=50)
def test_minijava::method_instantiation(instance):
    assert isinstance(instance, miniJava::Method)

@given(instance=miniJava::Method_strategy)
def test_minijava::method_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniJava::Method_strategy)
def test_minijava::method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniJava::VarDeclaration_strategy)
@settings(max_examples=50)
def test_minijava::vardeclaration_instantiation(instance):
    assert isinstance(instance, miniJava::VarDeclaration)

@given(instance=miniJava::MainMethod_strategy)
@settings(max_examples=50)
def test_minijava::mainmethod_instantiation(instance):
    assert isinstance(instance, miniJava::MainMethod)

@given(instance=miniJava::ClassDecl_strategy)
@settings(max_examples=50)
def test_minijava::classdecl_instantiation(instance):
    assert isinstance(instance, miniJava::ClassDecl)

@given(instance=miniJava::ClassDecl_strategy)
def test_minijava::classdecl_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=miniJava::ClassDecl_strategy)
def test_minijava::classdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniJava::Program_strategy)
@settings(max_examples=50)
def test_minijava::program_instantiation(instance):
    assert isinstance(instance, miniJava::Program)
