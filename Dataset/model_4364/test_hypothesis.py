import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ArithmeticExpression,
    workflow_Subtraction,
    workflow_Multiplication,
    workflow_Division,
    workflow_Addition,
    EqualityExpression,
    workflow_NotEqual,
    workflow_LessThanOrEqual,
    workflow_GreaterThan,
    workflow_LessThan,
    workflow_GreaterThanOrEqual,
    workflow_Equal,
    LogicExpression,
    workflow_Or,
    workflow_And,
    BinaryExpression,
    workflow_EqualityExpression,
    workflow_ArithmeticExpression,
    workflow_LogicExpression,
    UnaryExpression,
    workflow_UMinus,
    workflow_Not,
    Expression,
    workflow_UnaryExpression,
    workflow_BinaryExpression,
    workflow_ProcedureCall,
    workflow_Constant,
    Declaration,
    workflow_ParameterDeclaration,
    workflow_VariableDeclaration,
    workflow_Variable,
    Statement,
    workflow_Expression,
    workflow_While,
    workflow_VariableAssignment,
    workflow_If,
    workflow_Write,
    workflow_ProcedureReturn,
    workflow_Declaration,
    workflow_Read,
    workflow_Block,
    workflow_Statement,
    workflow_ProcedureDeclaration,
    workflow_CompilationUnit,
    Languages,
    AccessModifiers,
    Type,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(ArithmeticExpression)


def test_arithmeticexpression_constructor_exists():
    assert callable(ArithmeticExpression.__init__)


def test_arithmeticexpression_constructor_args():
    sig = inspect.signature(ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_subtraction_is_not_abstract():
    assert not inspect.isabstract(workflow_Subtraction)


def test_workflow_subtraction_constructor_exists():
    assert callable(workflow_Subtraction.__init__)


def test_workflow_subtraction_constructor_args():
    sig = inspect.signature(workflow_Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_workflow_multiplication_is_not_abstract():
    assert not inspect.isabstract(workflow_Multiplication)


def test_workflow_multiplication_constructor_exists():
    assert callable(workflow_Multiplication.__init__)


def test_workflow_multiplication_constructor_args():
    sig = inspect.signature(workflow_Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_workflow_division_is_not_abstract():
    assert not inspect.isabstract(workflow_Division)


def test_workflow_division_constructor_exists():
    assert callable(workflow_Division.__init__)


def test_workflow_division_constructor_args():
    sig = inspect.signature(workflow_Division.__init__)
    params = list(sig.parameters.keys())



def test_workflow_addition_is_not_abstract():
    assert not inspect.isabstract(workflow_Addition)


def test_workflow_addition_constructor_exists():
    assert callable(workflow_Addition.__init__)


def test_workflow_addition_constructor_args():
    sig = inspect.signature(workflow_Addition.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(EqualityExpression)


def test_equalityexpression_constructor_exists():
    assert callable(EqualityExpression.__init__)


def test_equalityexpression_constructor_args():
    sig = inspect.signature(EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_notequal_is_not_abstract():
    assert not inspect.isabstract(workflow_NotEqual)


def test_workflow_notequal_constructor_exists():
    assert callable(workflow_NotEqual.__init__)


def test_workflow_notequal_constructor_args():
    sig = inspect.signature(workflow_NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_workflow_lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(workflow_LessThanOrEqual)


def test_workflow_lessthanorequal_constructor_exists():
    assert callable(workflow_LessThanOrEqual.__init__)


def test_workflow_lessthanorequal_constructor_args():
    sig = inspect.signature(workflow_LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_workflow_greaterthan_is_not_abstract():
    assert not inspect.isabstract(workflow_GreaterThan)


def test_workflow_greaterthan_constructor_exists():
    assert callable(workflow_GreaterThan.__init__)


def test_workflow_greaterthan_constructor_args():
    sig = inspect.signature(workflow_GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_workflow_lessthan_is_not_abstract():
    assert not inspect.isabstract(workflow_LessThan)


def test_workflow_lessthan_constructor_exists():
    assert callable(workflow_LessThan.__init__)


def test_workflow_lessthan_constructor_args():
    sig = inspect.signature(workflow_LessThan.__init__)
    params = list(sig.parameters.keys())



def test_workflow_greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(workflow_GreaterThanOrEqual)


def test_workflow_greaterthanorequal_constructor_exists():
    assert callable(workflow_GreaterThanOrEqual.__init__)


def test_workflow_greaterthanorequal_constructor_args():
    sig = inspect.signature(workflow_GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_workflow_equal_is_not_abstract():
    assert not inspect.isabstract(workflow_Equal)


def test_workflow_equal_constructor_exists():
    assert callable(workflow_Equal.__init__)


def test_workflow_equal_constructor_args():
    sig = inspect.signature(workflow_Equal.__init__)
    params = list(sig.parameters.keys())



def test_logicexpression_is_not_abstract():
    assert not inspect.isabstract(LogicExpression)


def test_logicexpression_constructor_exists():
    assert callable(LogicExpression.__init__)


def test_logicexpression_constructor_args():
    sig = inspect.signature(LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_or_is_not_abstract():
    assert not inspect.isabstract(workflow_Or)


def test_workflow_or_constructor_exists():
    assert callable(workflow_Or.__init__)


def test_workflow_or_constructor_args():
    sig = inspect.signature(workflow_Or.__init__)
    params = list(sig.parameters.keys())



def test_workflow_and_is_not_abstract():
    assert not inspect.isabstract(workflow_And)


def test_workflow_and_constructor_exists():
    assert callable(workflow_And.__init__)


def test_workflow_and_constructor_args():
    sig = inspect.signature(workflow_And.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(workflow_EqualityExpression)


def test_workflow_equalityexpression_constructor_exists():
    assert callable(workflow_EqualityExpression.__init__)


def test_workflow_equalityexpression_constructor_args():
    sig = inspect.signature(workflow_EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(workflow_ArithmeticExpression)


def test_workflow_arithmeticexpression_constructor_exists():
    assert callable(workflow_ArithmeticExpression.__init__)


def test_workflow_arithmeticexpression_constructor_args():
    sig = inspect.signature(workflow_ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_logicexpression_is_not_abstract():
    assert not inspect.isabstract(workflow_LogicExpression)


def test_workflow_logicexpression_constructor_exists():
    assert callable(workflow_LogicExpression.__init__)


def test_workflow_logicexpression_constructor_args():
    sig = inspect.signature(workflow_LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_uminus_is_not_abstract():
    assert not inspect.isabstract(workflow_UMinus)


def test_workflow_uminus_constructor_exists():
    assert callable(workflow_UMinus.__init__)


def test_workflow_uminus_constructor_args():
    sig = inspect.signature(workflow_UMinus.__init__)
    params = list(sig.parameters.keys())



def test_workflow_not_is_not_abstract():
    assert not inspect.isabstract(workflow_Not)


def test_workflow_not_constructor_exists():
    assert callable(workflow_Not.__init__)


def test_workflow_not_constructor_args():
    sig = inspect.signature(workflow_Not.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(workflow_UnaryExpression)


def test_workflow_unaryexpression_constructor_exists():
    assert callable(workflow_UnaryExpression.__init__)


def test_workflow_unaryexpression_constructor_args():
    sig = inspect.signature(workflow_UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(workflow_BinaryExpression)


def test_workflow_binaryexpression_constructor_exists():
    assert callable(workflow_BinaryExpression.__init__)


def test_workflow_binaryexpression_constructor_args():
    sig = inspect.signature(workflow_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_procedurecall_is_not_abstract():
    assert not inspect.isabstract(workflow_ProcedureCall)


def test_workflow_procedurecall_constructor_exists():
    assert callable(workflow_ProcedureCall.__init__)


def test_workflow_procedurecall_constructor_args():
    sig = inspect.signature(workflow_ProcedureCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_procedurecall_has_name():
    assert hasattr(workflow_ProcedureCall, "name")
    descriptor = None
    for klass in workflow_ProcedureCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_constant_is_not_abstract():
    assert not inspect.isabstract(workflow_Constant)


def test_workflow_constant_constructor_exists():
    assert callable(workflow_Constant.__init__)


def test_workflow_constant_constructor_args():
    sig = inspect.signature(workflow_Constant.__init__)
    params = list(sig.parameters.keys())
    assert "asInteger" in params, "Missing parameter 'asInteger'"
    assert "asBoolean" in params, "Missing parameter 'asBoolean'"
    assert "asReal" in params, "Missing parameter 'asReal'"
    assert "asString" in params, "Missing parameter 'asString'"

def test_workflow_constant_has_asInteger():
    assert hasattr(workflow_Constant, "asInteger")
    descriptor = None
    for klass in workflow_Constant.__mro__:
        if "asInteger" in klass.__dict__:
            descriptor = klass.__dict__["asInteger"]
            break
    assert isinstance(descriptor, property)

def test_workflow_constant_has_asBoolean():
    assert hasattr(workflow_Constant, "asBoolean")
    descriptor = None
    for klass in workflow_Constant.__mro__:
        if "asBoolean" in klass.__dict__:
            descriptor = klass.__dict__["asBoolean"]
            break
    assert isinstance(descriptor, property)

def test_workflow_constant_has_asReal():
    assert hasattr(workflow_Constant, "asReal")
    descriptor = None
    for klass in workflow_Constant.__mro__:
        if "asReal" in klass.__dict__:
            descriptor = klass.__dict__["asReal"]
            break
    assert isinstance(descriptor, property)

def test_workflow_constant_has_asString():
    assert hasattr(workflow_Constant, "asString")
    descriptor = None
    for klass in workflow_Constant.__mro__:
        if "asString" in klass.__dict__:
            descriptor = klass.__dict__["asString"]
            break
    assert isinstance(descriptor, property)



def test_declaration_is_not_abstract():
    assert not inspect.isabstract(Declaration)


def test_declaration_constructor_exists():
    assert callable(Declaration.__init__)


def test_declaration_constructor_args():
    sig = inspect.signature(Declaration.__init__)
    params = list(sig.parameters.keys())



def test_workflow_parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(workflow_ParameterDeclaration)


def test_workflow_parameterdeclaration_constructor_exists():
    assert callable(workflow_ParameterDeclaration.__init__)


def test_workflow_parameterdeclaration_constructor_args():
    sig = inspect.signature(workflow_ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_workflow_parameterdeclaration_has_type():
    assert hasattr(workflow_ParameterDeclaration, "type")
    descriptor = None
    for klass in workflow_ParameterDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_workflow_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(workflow_VariableDeclaration)


def test_workflow_variabledeclaration_constructor_exists():
    assert callable(workflow_VariableDeclaration.__init__)


def test_workflow_variabledeclaration_constructor_args():
    sig = inspect.signature(workflow_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "isConstant" in params, "Missing parameter 'isConstant'"
    assert "type" in params, "Missing parameter 'type'"

def test_workflow_variabledeclaration_has_isConstant():
    assert hasattr(workflow_VariableDeclaration, "isConstant")
    descriptor = None
    for klass in workflow_VariableDeclaration.__mro__:
        if "isConstant" in klass.__dict__:
            descriptor = klass.__dict__["isConstant"]
            break
    assert isinstance(descriptor, property)

def test_workflow_variabledeclaration_has_type():
    assert hasattr(workflow_VariableDeclaration, "type")
    descriptor = None
    for klass in workflow_VariableDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_workflow_variable_is_not_abstract():
    assert not inspect.isabstract(workflow_Variable)


def test_workflow_variable_constructor_exists():
    assert callable(workflow_Variable.__init__)


def test_workflow_variable_constructor_args():
    sig = inspect.signature(workflow_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_variable_has_name():
    assert hasattr(workflow_Variable, "name")
    descriptor = None
    for klass in workflow_Variable.__mro__:
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



def test_workflow_expression_is_not_abstract():
    assert not inspect.isabstract(workflow_Expression)


def test_workflow_expression_constructor_exists():
    assert callable(workflow_Expression.__init__)


def test_workflow_expression_constructor_args():
    sig = inspect.signature(workflow_Expression.__init__)
    params = list(sig.parameters.keys())



def test_workflow_while_is_not_abstract():
    assert not inspect.isabstract(workflow_While)


def test_workflow_while_constructor_exists():
    assert callable(workflow_While.__init__)


def test_workflow_while_constructor_args():
    sig = inspect.signature(workflow_While.__init__)
    params = list(sig.parameters.keys())



def test_workflow_variableassignment_is_not_abstract():
    assert not inspect.isabstract(workflow_VariableAssignment)


def test_workflow_variableassignment_constructor_exists():
    assert callable(workflow_VariableAssignment.__init__)


def test_workflow_variableassignment_constructor_args():
    sig = inspect.signature(workflow_VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_workflow_if_is_not_abstract():
    assert not inspect.isabstract(workflow_If)


def test_workflow_if_constructor_exists():
    assert callable(workflow_If.__init__)


def test_workflow_if_constructor_args():
    sig = inspect.signature(workflow_If.__init__)
    params = list(sig.parameters.keys())



def test_workflow_write_is_not_abstract():
    assert not inspect.isabstract(workflow_Write)


def test_workflow_write_constructor_exists():
    assert callable(workflow_Write.__init__)


def test_workflow_write_constructor_args():
    sig = inspect.signature(workflow_Write.__init__)
    params = list(sig.parameters.keys())



def test_workflow_procedurereturn_is_not_abstract():
    assert not inspect.isabstract(workflow_ProcedureReturn)


def test_workflow_procedurereturn_constructor_exists():
    assert callable(workflow_ProcedureReturn.__init__)


def test_workflow_procedurereturn_constructor_args():
    sig = inspect.signature(workflow_ProcedureReturn.__init__)
    params = list(sig.parameters.keys())



def test_workflow_declaration_is_not_abstract():
    assert not inspect.isabstract(workflow_Declaration)


def test_workflow_declaration_constructor_exists():
    assert callable(workflow_Declaration.__init__)


def test_workflow_declaration_constructor_args():
    sig = inspect.signature(workflow_Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_declaration_has_name():
    assert hasattr(workflow_Declaration, "name")
    descriptor = None
    for klass in workflow_Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow_read_is_not_abstract():
    assert not inspect.isabstract(workflow_Read)


def test_workflow_read_constructor_exists():
    assert callable(workflow_Read.__init__)


def test_workflow_read_constructor_args():
    sig = inspect.signature(workflow_Read.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_workflow_read_has_type():
    assert hasattr(workflow_Read, "type")
    descriptor = None
    for klass in workflow_Read.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_workflow_block_is_not_abstract():
    assert not inspect.isabstract(workflow_Block)


def test_workflow_block_constructor_exists():
    assert callable(workflow_Block.__init__)


def test_workflow_block_constructor_args():
    sig = inspect.signature(workflow_Block.__init__)
    params = list(sig.parameters.keys())



def test_workflow_statement_is_not_abstract():
    assert not inspect.isabstract(workflow_Statement)


def test_workflow_statement_constructor_exists():
    assert callable(workflow_Statement.__init__)


def test_workflow_statement_constructor_args():
    sig = inspect.signature(workflow_Statement.__init__)
    params = list(sig.parameters.keys())



def test_workflow_proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(workflow_ProcedureDeclaration)


def test_workflow_proceduredeclaration_constructor_exists():
    assert callable(workflow_ProcedureDeclaration.__init__)


def test_workflow_proceduredeclaration_constructor_args():
    sig = inspect.signature(workflow_ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"

def test_workflow_proceduredeclaration_has_returnType():
    assert hasattr(workflow_ProcedureDeclaration, "returnType")
    descriptor = None
    for klass in workflow_ProcedureDeclaration.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_workflow_proceduredeclaration_has_accessModifier():
    assert hasattr(workflow_ProcedureDeclaration, "accessModifier")
    descriptor = None
    for klass in workflow_ProcedureDeclaration.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)



def test_workflow_compilationunit_is_not_abstract():
    assert not inspect.isabstract(workflow_CompilationUnit)


def test_workflow_compilationunit_constructor_exists():
    assert callable(workflow_CompilationUnit.__init__)


def test_workflow_compilationunit_constructor_args():
    sig = inspect.signature(workflow_CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "name" in params, "Missing parameter 'name'"

def test_workflow_compilationunit_has_language():
    assert hasattr(workflow_CompilationUnit, "language")
    descriptor = None
    for klass in workflow_CompilationUnit.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_workflow_compilationunit_has_name():
    assert hasattr(workflow_CompilationUnit, "name")
    descriptor = None
    for klass in workflow_CompilationUnit.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_languages_exists():
    # Check that the Enumeration exists
    assert Languages is not None

def test_languages_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Languages]
    expected_literals = [
        "CS",
        "CPP",
        "Python",
        "Java",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Languages"

def test_accessmodifiers_exists():
    # Check that the Enumeration exists
    assert AccessModifiers is not None

def test_accessmodifiers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessModifiers]
    expected_literals = [
        "protected",
        "default",
        "private",
        "public",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessModifiers"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "char",
        "boolean",
        "void",
        "int",
        "double",
        "long",
        "string",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"


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
ArithmeticExpression_strategy = st.builds(
    ArithmeticExpression,
)
workflow_Subtraction_strategy = st.builds(
    workflow_Subtraction,
)
workflow_Multiplication_strategy = st.builds(
    workflow_Multiplication,
)
workflow_Division_strategy = st.builds(
    workflow_Division,
)
workflow_Addition_strategy = st.builds(
    workflow_Addition,
)
EqualityExpression_strategy = st.builds(
    EqualityExpression,
)
workflow_NotEqual_strategy = st.builds(
    workflow_NotEqual,
)
workflow_LessThanOrEqual_strategy = st.builds(
    workflow_LessThanOrEqual,
)
workflow_GreaterThan_strategy = st.builds(
    workflow_GreaterThan,
)
workflow_LessThan_strategy = st.builds(
    workflow_LessThan,
)
workflow_GreaterThanOrEqual_strategy = st.builds(
    workflow_GreaterThanOrEqual,
)
workflow_Equal_strategy = st.builds(
    workflow_Equal,
)
LogicExpression_strategy = st.builds(
    LogicExpression,
)
workflow_Or_strategy = st.builds(
    workflow_Or,
)
workflow_And_strategy = st.builds(
    workflow_And,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
workflow_EqualityExpression_strategy = st.builds(
    workflow_EqualityExpression,
)
workflow_ArithmeticExpression_strategy = st.builds(
    workflow_ArithmeticExpression,
)
workflow_LogicExpression_strategy = st.builds(
    workflow_LogicExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
workflow_UMinus_strategy = st.builds(
    workflow_UMinus,
)
workflow_Not_strategy = st.builds(
    workflow_Not,
)
Expression_strategy = st.builds(
    Expression,
)
workflow_UnaryExpression_strategy = st.builds(
    workflow_UnaryExpression,
)
workflow_BinaryExpression_strategy = st.builds(
    workflow_BinaryExpression,
)
workflow_ProcedureCall_strategy = st.builds(
    workflow_ProcedureCall,
    name=
        safe_text
)
workflow_Constant_strategy = st.builds(
    workflow_Constant,
    asInteger=
        safe_text,
    asBoolean=
        safe_text,
    asReal=
        safe_text,
    asString=
        safe_text
)
Declaration_strategy = st.builds(
    Declaration,
)
workflow_ParameterDeclaration_strategy = st.builds(
    workflow_ParameterDeclaration,
    type=
        safe_text
)
workflow_VariableDeclaration_strategy = st.builds(
    workflow_VariableDeclaration,
    isConstant=
        safe_text,
    type=
        safe_text
)
workflow_Variable_strategy = st.builds(
    workflow_Variable,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
workflow_Expression_strategy = st.builds(
    workflow_Expression,
)
workflow_While_strategy = st.builds(
    workflow_While,
)
workflow_VariableAssignment_strategy = st.builds(
    workflow_VariableAssignment,
)
workflow_If_strategy = st.builds(
    workflow_If,
)
workflow_Write_strategy = st.builds(
    workflow_Write,
)
workflow_ProcedureReturn_strategy = st.builds(
    workflow_ProcedureReturn,
)
workflow_Declaration_strategy = st.builds(
    workflow_Declaration,
    name=
        safe_text
)
workflow_Read_strategy = st.builds(
    workflow_Read,
    type=
        safe_text
)
workflow_Block_strategy = st.builds(
    workflow_Block,
)
workflow_Statement_strategy = st.builds(
    workflow_Statement,
)
workflow_ProcedureDeclaration_strategy = st.builds(
    workflow_ProcedureDeclaration,
    returnType=
        safe_text,
    accessModifier=
        safe_text
)
workflow_CompilationUnit_strategy = st.builds(
    workflow_CompilationUnit,
    language=
        safe_text,
    name=
        safe_text
)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=workflow_Subtraction_strategy)
@settings(max_examples=50)
def test_workflow_subtraction_instantiation(instance):
    assert isinstance(instance, workflow_Subtraction)

@given(instance=workflow_Multiplication_strategy)
@settings(max_examples=50)
def test_workflow_multiplication_instantiation(instance):
    assert isinstance(instance, workflow_Multiplication)

@given(instance=workflow_Division_strategy)
@settings(max_examples=50)
def test_workflow_division_instantiation(instance):
    assert isinstance(instance, workflow_Division)

@given(instance=workflow_Addition_strategy)
@settings(max_examples=50)
def test_workflow_addition_instantiation(instance):
    assert isinstance(instance, workflow_Addition)

@given(instance=EqualityExpression_strategy)
@settings(max_examples=50)
def test_equalityexpression_instantiation(instance):
    assert isinstance(instance, EqualityExpression)

@given(instance=workflow_NotEqual_strategy)
@settings(max_examples=50)
def test_workflow_notequal_instantiation(instance):
    assert isinstance(instance, workflow_NotEqual)

@given(instance=workflow_LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_workflow_lessthanorequal_instantiation(instance):
    assert isinstance(instance, workflow_LessThanOrEqual)

@given(instance=workflow_GreaterThan_strategy)
@settings(max_examples=50)
def test_workflow_greaterthan_instantiation(instance):
    assert isinstance(instance, workflow_GreaterThan)

@given(instance=workflow_LessThan_strategy)
@settings(max_examples=50)
def test_workflow_lessthan_instantiation(instance):
    assert isinstance(instance, workflow_LessThan)

@given(instance=workflow_GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_workflow_greaterthanorequal_instantiation(instance):
    assert isinstance(instance, workflow_GreaterThanOrEqual)

@given(instance=workflow_Equal_strategy)
@settings(max_examples=50)
def test_workflow_equal_instantiation(instance):
    assert isinstance(instance, workflow_Equal)

@given(instance=LogicExpression_strategy)
@settings(max_examples=50)
def test_logicexpression_instantiation(instance):
    assert isinstance(instance, LogicExpression)

@given(instance=workflow_Or_strategy)
@settings(max_examples=50)
def test_workflow_or_instantiation(instance):
    assert isinstance(instance, workflow_Or)

@given(instance=workflow_And_strategy)
@settings(max_examples=50)
def test_workflow_and_instantiation(instance):
    assert isinstance(instance, workflow_And)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=workflow_EqualityExpression_strategy)
@settings(max_examples=50)
def test_workflow_equalityexpression_instantiation(instance):
    assert isinstance(instance, workflow_EqualityExpression)

@given(instance=workflow_ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_workflow_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, workflow_ArithmeticExpression)

@given(instance=workflow_LogicExpression_strategy)
@settings(max_examples=50)
def test_workflow_logicexpression_instantiation(instance):
    assert isinstance(instance, workflow_LogicExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=workflow_UMinus_strategy)
@settings(max_examples=50)
def test_workflow_uminus_instantiation(instance):
    assert isinstance(instance, workflow_UMinus)

@given(instance=workflow_Not_strategy)
@settings(max_examples=50)
def test_workflow_not_instantiation(instance):
    assert isinstance(instance, workflow_Not)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=workflow_UnaryExpression_strategy)
@settings(max_examples=50)
def test_workflow_unaryexpression_instantiation(instance):
    assert isinstance(instance, workflow_UnaryExpression)

@given(instance=workflow_BinaryExpression_strategy)
@settings(max_examples=50)
def test_workflow_binaryexpression_instantiation(instance):
    assert isinstance(instance, workflow_BinaryExpression)

@given(instance=workflow_ProcedureCall_strategy)
@settings(max_examples=50)
def test_workflow_procedurecall_instantiation(instance):
    assert isinstance(instance, workflow_ProcedureCall)



@given(instance=workflow_ProcedureCall_strategy)
def test_workflow_procedurecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_Constant_strategy)
@settings(max_examples=50)
def test_workflow_constant_instantiation(instance):
    assert isinstance(instance, workflow_Constant)



@given(instance=workflow_Constant_strategy)
def test_workflow_constant_asInteger_setter(instance):
    original = instance.asInteger
    instance.asInteger = original
    assert instance.asInteger == original



@given(instance=workflow_Constant_strategy)
def test_workflow_constant_asBoolean_setter(instance):
    original = instance.asBoolean
    instance.asBoolean = original
    assert instance.asBoolean == original



@given(instance=workflow_Constant_strategy)
def test_workflow_constant_asReal_setter(instance):
    original = instance.asReal
    instance.asReal = original
    assert instance.asReal == original



@given(instance=workflow_Constant_strategy)
def test_workflow_constant_asString_setter(instance):
    original = instance.asString
    instance.asString = original
    assert instance.asString == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=workflow_ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_workflow_parameterdeclaration_instantiation(instance):
    assert isinstance(instance, workflow_ParameterDeclaration)



@given(instance=workflow_ParameterDeclaration_strategy)
def test_workflow_parameterdeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=workflow_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_workflow_variabledeclaration_instantiation(instance):
    assert isinstance(instance, workflow_VariableDeclaration)



@given(instance=workflow_VariableDeclaration_strategy)
def test_workflow_variabledeclaration_isConstant_setter(instance):
    original = instance.isConstant
    instance.isConstant = original
    assert instance.isConstant == original



@given(instance=workflow_VariableDeclaration_strategy)
def test_workflow_variabledeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=workflow_Variable_strategy)
@settings(max_examples=50)
def test_workflow_variable_instantiation(instance):
    assert isinstance(instance, workflow_Variable)



@given(instance=workflow_Variable_strategy)
def test_workflow_variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=workflow_Expression_strategy)
@settings(max_examples=50)
def test_workflow_expression_instantiation(instance):
    assert isinstance(instance, workflow_Expression)

@given(instance=workflow_While_strategy)
@settings(max_examples=50)
def test_workflow_while_instantiation(instance):
    assert isinstance(instance, workflow_While)

@given(instance=workflow_VariableAssignment_strategy)
@settings(max_examples=50)
def test_workflow_variableassignment_instantiation(instance):
    assert isinstance(instance, workflow_VariableAssignment)

@given(instance=workflow_If_strategy)
@settings(max_examples=50)
def test_workflow_if_instantiation(instance):
    assert isinstance(instance, workflow_If)

@given(instance=workflow_Write_strategy)
@settings(max_examples=50)
def test_workflow_write_instantiation(instance):
    assert isinstance(instance, workflow_Write)

@given(instance=workflow_ProcedureReturn_strategy)
@settings(max_examples=50)
def test_workflow_procedurereturn_instantiation(instance):
    assert isinstance(instance, workflow_ProcedureReturn)

@given(instance=workflow_Declaration_strategy)
@settings(max_examples=50)
def test_workflow_declaration_instantiation(instance):
    assert isinstance(instance, workflow_Declaration)



@given(instance=workflow_Declaration_strategy)
def test_workflow_declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow_Read_strategy)
@settings(max_examples=50)
def test_workflow_read_instantiation(instance):
    assert isinstance(instance, workflow_Read)



@given(instance=workflow_Read_strategy)
def test_workflow_read_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=workflow_Block_strategy)
@settings(max_examples=50)
def test_workflow_block_instantiation(instance):
    assert isinstance(instance, workflow_Block)

@given(instance=workflow_Statement_strategy)
@settings(max_examples=50)
def test_workflow_statement_instantiation(instance):
    assert isinstance(instance, workflow_Statement)

@given(instance=workflow_ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_workflow_proceduredeclaration_instantiation(instance):
    assert isinstance(instance, workflow_ProcedureDeclaration)



@given(instance=workflow_ProcedureDeclaration_strategy)
def test_workflow_proceduredeclaration_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original



@given(instance=workflow_ProcedureDeclaration_strategy)
def test_workflow_proceduredeclaration_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original

@given(instance=workflow_CompilationUnit_strategy)
@settings(max_examples=50)
def test_workflow_compilationunit_instantiation(instance):
    assert isinstance(instance, workflow_CompilationUnit)



@given(instance=workflow_CompilationUnit_strategy)
def test_workflow_compilationunit_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original



@given(instance=workflow_CompilationUnit_strategy)
def test_workflow_compilationunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
