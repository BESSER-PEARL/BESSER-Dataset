import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expr,
    miniJava_Multiplication,
    miniJava_Point,
    miniJava_SquareBrackets,
    miniJava_Addition,
    miniJava_Expression,
    miniJava_MethodCall,
    miniJava_NumberValue,
    miniJava_Expr,
    miniJava_Variable,
    miniJava_Type,
    miniJava_Statement,
    miniJava_Method,
    miniJava_VarDeclaration,
    miniJava_MainMethod,
    miniJava_ClassDecl,
    miniJava_Program,
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



def test_minijava_multiplication_is_not_abstract():
    assert not inspect.isabstract(miniJava_Multiplication)


def test_minijava_multiplication_constructor_exists():
    assert callable(miniJava_Multiplication.__init__)


def test_minijava_multiplication_constructor_args():
    sig = inspect.signature(miniJava_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_minijava_point_is_not_abstract():
    assert not inspect.isabstract(miniJava_Point)


def test_minijava_point_constructor_exists():
    assert callable(miniJava_Point.__init__)


def test_minijava_point_constructor_args():
    sig = inspect.signature(miniJava_Point.__init__)
    params = list(sig.parameters.keys())



def test_minijava_squarebrackets_is_not_abstract():
    assert not inspect.isabstract(miniJava_SquareBrackets)


def test_minijava_squarebrackets_constructor_exists():
    assert callable(miniJava_SquareBrackets.__init__)


def test_minijava_squarebrackets_constructor_args():
    sig = inspect.signature(miniJava_SquareBrackets.__init__)
    params = list(sig.parameters.keys())



def test_minijava_addition_is_not_abstract():
    assert not inspect.isabstract(miniJava_Addition)


def test_minijava_addition_constructor_exists():
    assert callable(miniJava_Addition.__init__)


def test_minijava_addition_constructor_args():
    sig = inspect.signature(miniJava_Addition.__init__)
    params = list(sig.parameters.keys())



def test_minijava_expression_is_not_abstract():
    assert not inspect.isabstract(miniJava_Expression)


def test_minijava_expression_constructor_exists():
    assert callable(miniJava_Expression.__init__)


def test_minijava_expression_constructor_args():
    sig = inspect.signature(miniJava_Expression.__init__)
    params = list(sig.parameters.keys())



def test_minijava_methodcall_is_not_abstract():
    assert not inspect.isabstract(miniJava_MethodCall)


def test_minijava_methodcall_constructor_exists():
    assert callable(miniJava_MethodCall.__init__)


def test_minijava_methodcall_constructor_args():
    sig = inspect.signature(miniJava_MethodCall.__init__)
    params = list(sig.parameters.keys())



def test_minijava_numbervalue_is_not_abstract():
    assert not inspect.isabstract(miniJava_NumberValue)


def test_minijava_numbervalue_constructor_exists():
    assert callable(miniJava_NumberValue.__init__)


def test_minijava_numbervalue_constructor_args():
    sig = inspect.signature(miniJava_NumberValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_minijava_numbervalue_has_value():
    assert hasattr(miniJava_NumberValue, "value")
    descriptor = None
    for klass in miniJava_NumberValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_minijava_expr_is_not_abstract():
    assert not inspect.isabstract(miniJava_Expr)


def test_minijava_expr_constructor_exists():
    assert callable(miniJava_Expr.__init__)


def test_minijava_expr_constructor_args():
    sig = inspect.signature(miniJava_Expr.__init__)
    params = list(sig.parameters.keys())
    assert "expressionType" in params, "Missing parameter 'expressionType'"

def test_minijava_expr_has_expressionType():
    assert hasattr(miniJava_Expr, "expressionType")
    descriptor = None
    for klass in miniJava_Expr.__mro__:
        if "expressionType" in klass.__dict__:
            descriptor = klass.__dict__["expressionType"]
            break
    assert isinstance(descriptor, property)



def test_minijava_variable_is_not_abstract():
    assert not inspect.isabstract(miniJava_Variable)


def test_minijava_variable_constructor_exists():
    assert callable(miniJava_Variable.__init__)


def test_minijava_variable_constructor_args():
    sig = inspect.signature(miniJava_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava_variable_has_name():
    assert hasattr(miniJava_Variable, "name")
    descriptor = None
    for klass in miniJava_Variable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minijava_type_is_not_abstract():
    assert not inspect.isabstract(miniJava_Type)


def test_minijava_type_constructor_exists():
    assert callable(miniJava_Type.__init__)


def test_minijava_type_constructor_args():
    sig = inspect.signature(miniJava_Type.__init__)
    params = list(sig.parameters.keys())
    assert "typeName" in params, "Missing parameter 'typeName'"

def test_minijava_type_has_typeName():
    assert hasattr(miniJava_Type, "typeName")
    descriptor = None
    for klass in miniJava_Type.__mro__:
        if "typeName" in klass.__dict__:
            descriptor = klass.__dict__["typeName"]
            break
    assert isinstance(descriptor, property)



def test_minijava_statement_is_not_abstract():
    assert not inspect.isabstract(miniJava_Statement)


def test_minijava_statement_constructor_exists():
    assert callable(miniJava_Statement.__init__)


def test_minijava_statement_constructor_args():
    sig = inspect.signature(miniJava_Statement.__init__)
    params = list(sig.parameters.keys())
    assert "isArrayElementAssignment" in params, "Missing parameter 'isArrayElementAssignment'"
    assert "statementType" in params, "Missing parameter 'statementType'"

def test_minijava_statement_has_isArrayElementAssignment():
    assert hasattr(miniJava_Statement, "isArrayElementAssignment")
    descriptor = None
    for klass in miniJava_Statement.__mro__:
        if "isArrayElementAssignment" in klass.__dict__:
            descriptor = klass.__dict__["isArrayElementAssignment"]
            break
    assert isinstance(descriptor, property)

def test_minijava_statement_has_statementType():
    assert hasattr(miniJava_Statement, "statementType")
    descriptor = None
    for klass in miniJava_Statement.__mro__:
        if "statementType" in klass.__dict__:
            descriptor = klass.__dict__["statementType"]
            break
    assert isinstance(descriptor, property)



def test_minijava_method_is_not_abstract():
    assert not inspect.isabstract(miniJava_Method)


def test_minijava_method_constructor_exists():
    assert callable(miniJava_Method.__init__)


def test_minijava_method_constructor_args():
    sig = inspect.signature(miniJava_Method.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava_method_has_name():
    assert hasattr(miniJava_Method, "name")
    descriptor = None
    for klass in miniJava_Method.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minijava_vardeclaration_is_not_abstract():
    assert not inspect.isabstract(miniJava_VarDeclaration)


def test_minijava_vardeclaration_constructor_exists():
    assert callable(miniJava_VarDeclaration.__init__)


def test_minijava_vardeclaration_constructor_args():
    sig = inspect.signature(miniJava_VarDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_minijava_mainmethod_is_not_abstract():
    assert not inspect.isabstract(miniJava_MainMethod)


def test_minijava_mainmethod_constructor_exists():
    assert callable(miniJava_MainMethod.__init__)


def test_minijava_mainmethod_constructor_args():
    sig = inspect.signature(miniJava_MainMethod.__init__)
    params = list(sig.parameters.keys())



def test_minijava_classdecl_is_not_abstract():
    assert not inspect.isabstract(miniJava_ClassDecl)


def test_minijava_classdecl_constructor_exists():
    assert callable(miniJava_ClassDecl.__init__)


def test_minijava_classdecl_constructor_args():
    sig = inspect.signature(miniJava_ClassDecl.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_minijava_classdecl_has_name():
    assert hasattr(miniJava_ClassDecl, "name")
    descriptor = None
    for klass in miniJava_ClassDecl.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_minijava_program_is_not_abstract():
    assert not inspect.isabstract(miniJava_Program)


def test_minijava_program_constructor_exists():
    assert callable(miniJava_Program.__init__)


def test_minijava_program_constructor_args():
    sig = inspect.signature(miniJava_Program.__init__)
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
miniJava_Multiplication_strategy = st.builds(
    miniJava_Multiplication,
)
miniJava_Point_strategy = st.builds(
    miniJava_Point,
)
miniJava_SquareBrackets_strategy = st.builds(
    miniJava_SquareBrackets,
)
miniJava_Addition_strategy = st.builds(
    miniJava_Addition,
)
miniJava_Expression_strategy = st.builds(
    miniJava_Expression,
)
miniJava_MethodCall_strategy = st.builds(
    miniJava_MethodCall,
)
miniJava_NumberValue_strategy = st.builds(
    miniJava_NumberValue,
    value=
        st.integers()
)
miniJava_Expr_strategy = st.builds(
    miniJava_Expr,
    expressionType=
        safe_text
)
miniJava_Variable_strategy = st.builds(
    miniJava_Variable,
    name=
        safe_text
)
miniJava_Type_strategy = st.builds(
    miniJava_Type,
    typeName=
        safe_text
)
miniJava_Statement_strategy = st.builds(
    miniJava_Statement,
    isArrayElementAssignment=
        st.booleans(),
    statementType=
        safe_text
)
miniJava_Method_strategy = st.builds(
    miniJava_Method,
    name=
        safe_text
)
miniJava_VarDeclaration_strategy = st.builds(
    miniJava_VarDeclaration,
)
miniJava_MainMethod_strategy = st.builds(
    miniJava_MainMethod,
)
miniJava_ClassDecl_strategy = st.builds(
    miniJava_ClassDecl,
    name=
        safe_text
)
miniJava_Program_strategy = st.builds(
    miniJava_Program,
)

@given(instance=Expr_strategy)
@settings(max_examples=50)
def test_expr_instantiation(instance):
    assert isinstance(instance, Expr)

@given(instance=miniJava_Multiplication_strategy)
@settings(max_examples=50)
def test_minijava_multiplication_instantiation(instance):
    assert isinstance(instance, miniJava_Multiplication)

@given(instance=miniJava_Point_strategy)
@settings(max_examples=50)
def test_minijava_point_instantiation(instance):
    assert isinstance(instance, miniJava_Point)

@given(instance=miniJava_SquareBrackets_strategy)
@settings(max_examples=50)
def test_minijava_squarebrackets_instantiation(instance):
    assert isinstance(instance, miniJava_SquareBrackets)

@given(instance=miniJava_Addition_strategy)
@settings(max_examples=50)
def test_minijava_addition_instantiation(instance):
    assert isinstance(instance, miniJava_Addition)

@given(instance=miniJava_Expression_strategy)
@settings(max_examples=50)
def test_minijava_expression_instantiation(instance):
    assert isinstance(instance, miniJava_Expression)

@given(instance=miniJava_MethodCall_strategy)
@settings(max_examples=50)
def test_minijava_methodcall_instantiation(instance):
    assert isinstance(instance, miniJava_MethodCall)

@given(instance=miniJava_NumberValue_strategy)
@settings(max_examples=50)
def test_minijava_numbervalue_instantiation(instance):
    assert isinstance(instance, miniJava_NumberValue)



@given(instance=miniJava_NumberValue_strategy)
def test_minijava_numbervalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=miniJava_Expr_strategy)
@settings(max_examples=50)
def test_minijava_expr_instantiation(instance):
    assert isinstance(instance, miniJava_Expr)



@given(instance=miniJava_Expr_strategy)
def test_minijava_expr_expressionType_setter(instance):
    original = instance.expressionType
    instance.expressionType = original
    assert instance.expressionType == original

@given(instance=miniJava_Variable_strategy)
@settings(max_examples=50)
def test_minijava_variable_instantiation(instance):
    assert isinstance(instance, miniJava_Variable)



@given(instance=miniJava_Variable_strategy)
def test_minijava_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniJava_Type_strategy)
@settings(max_examples=50)
def test_minijava_type_instantiation(instance):
    assert isinstance(instance, miniJava_Type)



@given(instance=miniJava_Type_strategy)
def test_minijava_type_typeName_setter(instance):
    original = instance.typeName
    instance.typeName = original
    assert instance.typeName == original

@given(instance=miniJava_Statement_strategy)
@settings(max_examples=50)
def test_minijava_statement_instantiation(instance):
    assert isinstance(instance, miniJava_Statement)



@given(instance=miniJava_Statement_strategy)
def test_minijava_statement_isArrayElementAssignment_setter(instance):
    original = instance.isArrayElementAssignment
    instance.isArrayElementAssignment = original
    assert instance.isArrayElementAssignment == original



@given(instance=miniJava_Statement_strategy)
def test_minijava_statement_statementType_setter(instance):
    original = instance.statementType
    instance.statementType = original
    assert instance.statementType == original

@given(instance=miniJava_Method_strategy)
@settings(max_examples=50)
def test_minijava_method_instantiation(instance):
    assert isinstance(instance, miniJava_Method)



@given(instance=miniJava_Method_strategy)
def test_minijava_method_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniJava_VarDeclaration_strategy)
@settings(max_examples=50)
def test_minijava_vardeclaration_instantiation(instance):
    assert isinstance(instance, miniJava_VarDeclaration)

@given(instance=miniJava_MainMethod_strategy)
@settings(max_examples=50)
def test_minijava_mainmethod_instantiation(instance):
    assert isinstance(instance, miniJava_MainMethod)

@given(instance=miniJava_ClassDecl_strategy)
@settings(max_examples=50)
def test_minijava_classdecl_instantiation(instance):
    assert isinstance(instance, miniJava_ClassDecl)



@given(instance=miniJava_ClassDecl_strategy)
def test_minijava_classdecl_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=miniJava_Program_strategy)
@settings(max_examples=50)
def test_minijava_program_instantiation(instance):
    assert isinstance(instance, miniJava_Program)
