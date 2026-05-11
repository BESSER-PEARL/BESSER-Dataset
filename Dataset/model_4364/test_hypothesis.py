import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ArithmeticExpression,
    workflow::Division,
    workflow::Multiplication,
    workflow::Subtraction,
    workflow::Addition,
    EqualityExpression,
    workflow::LessThanOrEqual,
    workflow::NotEqual,
    workflow::GreaterThanOrEqual,
    workflow::LessThan,
    workflow::GreaterThan,
    workflow::Equal,
    LogicExpression,
    workflow::Or,
    workflow::And,
    BinaryExpression,
    workflow::ArithmeticExpression,
    workflow::EqualityExpression,
    workflow::LogicExpression,
    UnaryExpression,
    workflow::UMinus,
    workflow::Not,
    Expression,
    workflow::BinaryExpression,
    workflow::UnaryExpression,
    workflow::ProcedureCall,
    workflow::Constant,
    Declaration,
    workflow::ParameterDeclaration,
    workflow::VariableDeclaration,
    workflow::Variable,
    Statement,
    workflow::Write,
    workflow::Read,
    workflow::If,
    workflow::Declaration,
    workflow::Expression,
    workflow::VariableAssignment,
    workflow::While,
    workflow::ProcedureReturn,
    workflow::Block,
    workflow::Statement,
    workflow::ProcedureDeclaration,
    workflow::CompilationUnit,
    Languages,
    Type,
    AccessModifiers,
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



def test_workflow::division_is_not_abstract():
    assert not inspect.isabstract(workflow::Division)


def test_workflow::division_constructor_exists():
    assert callable(workflow::Division.__init__)


def test_workflow::division_constructor_args():
    sig = inspect.signature(workflow::Division.__init__)
    params = list(sig.parameters.keys())



def test_workflow::multiplication_is_not_abstract():
    assert not inspect.isabstract(workflow::Multiplication)


def test_workflow::multiplication_constructor_exists():
    assert callable(workflow::Multiplication.__init__)


def test_workflow::multiplication_constructor_args():
    sig = inspect.signature(workflow::Multiplication.__init__)
    params = list(sig.parameters.keys())



def test_workflow::subtraction_is_not_abstract():
    assert not inspect.isabstract(workflow::Subtraction)


def test_workflow::subtraction_constructor_exists():
    assert callable(workflow::Subtraction.__init__)


def test_workflow::subtraction_constructor_args():
    sig = inspect.signature(workflow::Subtraction.__init__)
    params = list(sig.parameters.keys())



def test_workflow::addition_is_not_abstract():
    assert not inspect.isabstract(workflow::Addition)


def test_workflow::addition_constructor_exists():
    assert callable(workflow::Addition.__init__)


def test_workflow::addition_constructor_args():
    sig = inspect.signature(workflow::Addition.__init__)
    params = list(sig.parameters.keys())



def test_equalityexpression_is_not_abstract():
    assert not inspect.isabstract(EqualityExpression)


def test_equalityexpression_constructor_exists():
    assert callable(EqualityExpression.__init__)


def test_equalityexpression_constructor_args():
    sig = inspect.signature(EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::lessthanorequal_is_not_abstract():
    assert not inspect.isabstract(workflow::LessThanOrEqual)


def test_workflow::lessthanorequal_constructor_exists():
    assert callable(workflow::LessThanOrEqual.__init__)


def test_workflow::lessthanorequal_constructor_args():
    sig = inspect.signature(workflow::LessThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_workflow::notequal_is_not_abstract():
    assert not inspect.isabstract(workflow::NotEqual)


def test_workflow::notequal_constructor_exists():
    assert callable(workflow::NotEqual.__init__)


def test_workflow::notequal_constructor_args():
    sig = inspect.signature(workflow::NotEqual.__init__)
    params = list(sig.parameters.keys())



def test_workflow::greaterthanorequal_is_not_abstract():
    assert not inspect.isabstract(workflow::GreaterThanOrEqual)


def test_workflow::greaterthanorequal_constructor_exists():
    assert callable(workflow::GreaterThanOrEqual.__init__)


def test_workflow::greaterthanorequal_constructor_args():
    sig = inspect.signature(workflow::GreaterThanOrEqual.__init__)
    params = list(sig.parameters.keys())



def test_workflow::lessthan_is_not_abstract():
    assert not inspect.isabstract(workflow::LessThan)


def test_workflow::lessthan_constructor_exists():
    assert callable(workflow::LessThan.__init__)


def test_workflow::lessthan_constructor_args():
    sig = inspect.signature(workflow::LessThan.__init__)
    params = list(sig.parameters.keys())



def test_workflow::greaterthan_is_not_abstract():
    assert not inspect.isabstract(workflow::GreaterThan)


def test_workflow::greaterthan_constructor_exists():
    assert callable(workflow::GreaterThan.__init__)


def test_workflow::greaterthan_constructor_args():
    sig = inspect.signature(workflow::GreaterThan.__init__)
    params = list(sig.parameters.keys())



def test_workflow::equal_is_not_abstract():
    assert not inspect.isabstract(workflow::Equal)


def test_workflow::equal_constructor_exists():
    assert callable(workflow::Equal.__init__)


def test_workflow::equal_constructor_args():
    sig = inspect.signature(workflow::Equal.__init__)
    params = list(sig.parameters.keys())



def test_logicexpression_is_not_abstract():
    assert not inspect.isabstract(LogicExpression)


def test_logicexpression_constructor_exists():
    assert callable(LogicExpression.__init__)


def test_logicexpression_constructor_args():
    sig = inspect.signature(LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::or_is_not_abstract():
    assert not inspect.isabstract(workflow::Or)


def test_workflow::or_constructor_exists():
    assert callable(workflow::Or.__init__)


def test_workflow::or_constructor_args():
    sig = inspect.signature(workflow::Or.__init__)
    params = list(sig.parameters.keys())



def test_workflow::and_is_not_abstract():
    assert not inspect.isabstract(workflow::And)


def test_workflow::and_constructor_exists():
    assert callable(workflow::And.__init__)


def test_workflow::and_constructor_args():
    sig = inspect.signature(workflow::And.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::arithmeticexpression_is_not_abstract():
    assert not inspect.isabstract(workflow::ArithmeticExpression)


def test_workflow::arithmeticexpression_constructor_exists():
    assert callable(workflow::ArithmeticExpression.__init__)


def test_workflow::arithmeticexpression_constructor_args():
    sig = inspect.signature(workflow::ArithmeticExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::equalityexpression_is_not_abstract():
    assert not inspect.isabstract(workflow::EqualityExpression)


def test_workflow::equalityexpression_constructor_exists():
    assert callable(workflow::EqualityExpression.__init__)


def test_workflow::equalityexpression_constructor_args():
    sig = inspect.signature(workflow::EqualityExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::logicexpression_is_not_abstract():
    assert not inspect.isabstract(workflow::LogicExpression)


def test_workflow::logicexpression_constructor_exists():
    assert callable(workflow::LogicExpression.__init__)


def test_workflow::logicexpression_constructor_args():
    sig = inspect.signature(workflow::LogicExpression.__init__)
    params = list(sig.parameters.keys())



def test_unaryexpression_is_not_abstract():
    assert not inspect.isabstract(UnaryExpression)


def test_unaryexpression_constructor_exists():
    assert callable(UnaryExpression.__init__)


def test_unaryexpression_constructor_args():
    sig = inspect.signature(UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::uminus_is_not_abstract():
    assert not inspect.isabstract(workflow::UMinus)


def test_workflow::uminus_constructor_exists():
    assert callable(workflow::UMinus.__init__)


def test_workflow::uminus_constructor_args():
    sig = inspect.signature(workflow::UMinus.__init__)
    params = list(sig.parameters.keys())



def test_workflow::not_is_not_abstract():
    assert not inspect.isabstract(workflow::Not)


def test_workflow::not_constructor_exists():
    assert callable(workflow::Not.__init__)


def test_workflow::not_constructor_args():
    sig = inspect.signature(workflow::Not.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(workflow::BinaryExpression)


def test_workflow::binaryexpression_constructor_exists():
    assert callable(workflow::BinaryExpression.__init__)


def test_workflow::binaryexpression_constructor_args():
    sig = inspect.signature(workflow::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::unaryexpression_is_not_abstract():
    assert not inspect.isabstract(workflow::UnaryExpression)


def test_workflow::unaryexpression_constructor_exists():
    assert callable(workflow::UnaryExpression.__init__)


def test_workflow::unaryexpression_constructor_args():
    sig = inspect.signature(workflow::UnaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::procedurecall_is_not_abstract():
    assert not inspect.isabstract(workflow::ProcedureCall)


def test_workflow::procedurecall_constructor_exists():
    assert callable(workflow::ProcedureCall.__init__)


def test_workflow::procedurecall_constructor_args():
    sig = inspect.signature(workflow::ProcedureCall.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::procedurecall_has_name():
    assert hasattr(workflow::ProcedureCall, "name")
    descriptor = None
    for klass in workflow::ProcedureCall.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::constant_is_not_abstract():
    assert not inspect.isabstract(workflow::Constant)


def test_workflow::constant_constructor_exists():
    assert callable(workflow::Constant.__init__)


def test_workflow::constant_constructor_args():
    sig = inspect.signature(workflow::Constant.__init__)
    params = list(sig.parameters.keys())
    assert "asInteger" in params, "Missing parameter 'asInteger'"
    assert "asReal" in params, "Missing parameter 'asReal'"
    assert "asBoolean" in params, "Missing parameter 'asBoolean'"
    assert "asString" in params, "Missing parameter 'asString'"

def test_workflow::constant_has_asInteger():
    assert hasattr(workflow::Constant, "asInteger")
    descriptor = None
    for klass in workflow::Constant.__mro__:
        if "asInteger" in klass.__dict__:
            descriptor = klass.__dict__["asInteger"]
            break
    assert isinstance(descriptor, property)

def test_workflow::constant_has_asReal():
    assert hasattr(workflow::Constant, "asReal")
    descriptor = None
    for klass in workflow::Constant.__mro__:
        if "asReal" in klass.__dict__:
            descriptor = klass.__dict__["asReal"]
            break
    assert isinstance(descriptor, property)

def test_workflow::constant_has_asBoolean():
    assert hasattr(workflow::Constant, "asBoolean")
    descriptor = None
    for klass in workflow::Constant.__mro__:
        if "asBoolean" in klass.__dict__:
            descriptor = klass.__dict__["asBoolean"]
            break
    assert isinstance(descriptor, property)

def test_workflow::constant_has_asString():
    assert hasattr(workflow::Constant, "asString")
    descriptor = None
    for klass in workflow::Constant.__mro__:
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



def test_workflow::parameterdeclaration_is_not_abstract():
    assert not inspect.isabstract(workflow::ParameterDeclaration)


def test_workflow::parameterdeclaration_constructor_exists():
    assert callable(workflow::ParameterDeclaration.__init__)


def test_workflow::parameterdeclaration_constructor_args():
    sig = inspect.signature(workflow::ParameterDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_workflow::parameterdeclaration_has_type():
    assert hasattr(workflow::ParameterDeclaration, "type")
    descriptor = None
    for klass in workflow::ParameterDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_workflow::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(workflow::VariableDeclaration)


def test_workflow::variabledeclaration_constructor_exists():
    assert callable(workflow::VariableDeclaration.__init__)


def test_workflow::variabledeclaration_constructor_args():
    sig = inspect.signature(workflow::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "isConstant" in params, "Missing parameter 'isConstant'"

def test_workflow::variabledeclaration_has_type():
    assert hasattr(workflow::VariableDeclaration, "type")
    descriptor = None
    for klass in workflow::VariableDeclaration.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_workflow::variabledeclaration_has_isConstant():
    assert hasattr(workflow::VariableDeclaration, "isConstant")
    descriptor = None
    for klass in workflow::VariableDeclaration.__mro__:
        if "isConstant" in klass.__dict__:
            descriptor = klass.__dict__["isConstant"]
            break
    assert isinstance(descriptor, property)



def test_workflow::variable_is_not_abstract():
    assert not inspect.isabstract(workflow::Variable)


def test_workflow::variable_constructor_exists():
    assert callable(workflow::Variable.__init__)


def test_workflow::variable_constructor_args():
    sig = inspect.signature(workflow::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::variable_has_name():
    assert hasattr(workflow::Variable, "name")
    descriptor = None
    for klass in workflow::Variable.__mro__:
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



def test_workflow::write_is_not_abstract():
    assert not inspect.isabstract(workflow::Write)


def test_workflow::write_constructor_exists():
    assert callable(workflow::Write.__init__)


def test_workflow::write_constructor_args():
    sig = inspect.signature(workflow::Write.__init__)
    params = list(sig.parameters.keys())



def test_workflow::read_is_not_abstract():
    assert not inspect.isabstract(workflow::Read)


def test_workflow::read_constructor_exists():
    assert callable(workflow::Read.__init__)


def test_workflow::read_constructor_args():
    sig = inspect.signature(workflow::Read.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_workflow::read_has_type():
    assert hasattr(workflow::Read, "type")
    descriptor = None
    for klass in workflow::Read.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_workflow::if_is_not_abstract():
    assert not inspect.isabstract(workflow::If)


def test_workflow::if_constructor_exists():
    assert callable(workflow::If.__init__)


def test_workflow::if_constructor_args():
    sig = inspect.signature(workflow::If.__init__)
    params = list(sig.parameters.keys())



def test_workflow::declaration_is_not_abstract():
    assert not inspect.isabstract(workflow::Declaration)


def test_workflow::declaration_constructor_exists():
    assert callable(workflow::Declaration.__init__)


def test_workflow::declaration_constructor_args():
    sig = inspect.signature(workflow::Declaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::declaration_has_name():
    assert hasattr(workflow::Declaration, "name")
    descriptor = None
    for klass in workflow::Declaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_workflow::expression_is_not_abstract():
    assert not inspect.isabstract(workflow::Expression)


def test_workflow::expression_constructor_exists():
    assert callable(workflow::Expression.__init__)


def test_workflow::expression_constructor_args():
    sig = inspect.signature(workflow::Expression.__init__)
    params = list(sig.parameters.keys())



def test_workflow::variableassignment_is_not_abstract():
    assert not inspect.isabstract(workflow::VariableAssignment)


def test_workflow::variableassignment_constructor_exists():
    assert callable(workflow::VariableAssignment.__init__)


def test_workflow::variableassignment_constructor_args():
    sig = inspect.signature(workflow::VariableAssignment.__init__)
    params = list(sig.parameters.keys())



def test_workflow::while_is_not_abstract():
    assert not inspect.isabstract(workflow::While)


def test_workflow::while_constructor_exists():
    assert callable(workflow::While.__init__)


def test_workflow::while_constructor_args():
    sig = inspect.signature(workflow::While.__init__)
    params = list(sig.parameters.keys())



def test_workflow::procedurereturn_is_not_abstract():
    assert not inspect.isabstract(workflow::ProcedureReturn)


def test_workflow::procedurereturn_constructor_exists():
    assert callable(workflow::ProcedureReturn.__init__)


def test_workflow::procedurereturn_constructor_args():
    sig = inspect.signature(workflow::ProcedureReturn.__init__)
    params = list(sig.parameters.keys())



def test_workflow::block_is_not_abstract():
    assert not inspect.isabstract(workflow::Block)


def test_workflow::block_constructor_exists():
    assert callable(workflow::Block.__init__)


def test_workflow::block_constructor_args():
    sig = inspect.signature(workflow::Block.__init__)
    params = list(sig.parameters.keys())



def test_workflow::statement_is_not_abstract():
    assert not inspect.isabstract(workflow::Statement)


def test_workflow::statement_constructor_exists():
    assert callable(workflow::Statement.__init__)


def test_workflow::statement_constructor_args():
    sig = inspect.signature(workflow::Statement.__init__)
    params = list(sig.parameters.keys())



def test_workflow::proceduredeclaration_is_not_abstract():
    assert not inspect.isabstract(workflow::ProcedureDeclaration)


def test_workflow::proceduredeclaration_constructor_exists():
    assert callable(workflow::ProcedureDeclaration.__init__)


def test_workflow::proceduredeclaration_constructor_args():
    sig = inspect.signature(workflow::ProcedureDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "returnType" in params, "Missing parameter 'returnType'"
    assert "accessModifier" in params, "Missing parameter 'accessModifier'"

def test_workflow::proceduredeclaration_has_returnType():
    assert hasattr(workflow::ProcedureDeclaration, "returnType")
    descriptor = None
    for klass in workflow::ProcedureDeclaration.__mro__:
        if "returnType" in klass.__dict__:
            descriptor = klass.__dict__["returnType"]
            break
    assert isinstance(descriptor, property)

def test_workflow::proceduredeclaration_has_accessModifier():
    assert hasattr(workflow::ProcedureDeclaration, "accessModifier")
    descriptor = None
    for klass in workflow::ProcedureDeclaration.__mro__:
        if "accessModifier" in klass.__dict__:
            descriptor = klass.__dict__["accessModifier"]
            break
    assert isinstance(descriptor, property)



def test_workflow::compilationunit_is_not_abstract():
    assert not inspect.isabstract(workflow::CompilationUnit)


def test_workflow::compilationunit_constructor_exists():
    assert callable(workflow::CompilationUnit.__init__)


def test_workflow::compilationunit_constructor_args():
    sig = inspect.signature(workflow::CompilationUnit.__init__)
    params = list(sig.parameters.keys())
    assert "language" in params, "Missing parameter 'language'"
    assert "name" in params, "Missing parameter 'name'"

def test_workflow::compilationunit_has_language():
    assert hasattr(workflow::CompilationUnit, "language")
    descriptor = None
    for klass in workflow::CompilationUnit.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_workflow::compilationunit_has_name():
    assert hasattr(workflow::CompilationUnit, "name")
    descriptor = None
    for klass in workflow::CompilationUnit.__mro__:
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
        "Java",
        "CPP",
        "Python",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Languages"

def test_type_exists():
    # Check that the Enumeration exists
    assert Type is not None

def test_type_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Type]
    expected_literals = [
        "boolean",
        "char",
        "long",
        "void",
        "string",
        "int",
        "double",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Type"

def test_accessmodifiers_exists():
    # Check that the Enumeration exists
    assert AccessModifiers is not None

def test_accessmodifiers_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AccessModifiers]
    expected_literals = [
        "public",
        "default",
        "private",
        "protected",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AccessModifiers"


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
workflow::Division_strategy = st.builds(
    workflow::Division,
)
workflow::Multiplication_strategy = st.builds(
    workflow::Multiplication,
)
workflow::Subtraction_strategy = st.builds(
    workflow::Subtraction,
)
workflow::Addition_strategy = st.builds(
    workflow::Addition,
)
EqualityExpression_strategy = st.builds(
    EqualityExpression,
)
workflow::LessThanOrEqual_strategy = st.builds(
    workflow::LessThanOrEqual,
)
workflow::NotEqual_strategy = st.builds(
    workflow::NotEqual,
)
workflow::GreaterThanOrEqual_strategy = st.builds(
    workflow::GreaterThanOrEqual,
)
workflow::LessThan_strategy = st.builds(
    workflow::LessThan,
)
workflow::GreaterThan_strategy = st.builds(
    workflow::GreaterThan,
)
workflow::Equal_strategy = st.builds(
    workflow::Equal,
)
LogicExpression_strategy = st.builds(
    LogicExpression,
)
workflow::Or_strategy = st.builds(
    workflow::Or,
)
workflow::And_strategy = st.builds(
    workflow::And,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
workflow::ArithmeticExpression_strategy = st.builds(
    workflow::ArithmeticExpression,
)
workflow::EqualityExpression_strategy = st.builds(
    workflow::EqualityExpression,
)
workflow::LogicExpression_strategy = st.builds(
    workflow::LogicExpression,
)
UnaryExpression_strategy = st.builds(
    UnaryExpression,
)
workflow::UMinus_strategy = st.builds(
    workflow::UMinus,
)
workflow::Not_strategy = st.builds(
    workflow::Not,
)
Expression_strategy = st.builds(
    Expression,
)
workflow::BinaryExpression_strategy = st.builds(
    workflow::BinaryExpression,
)
workflow::UnaryExpression_strategy = st.builds(
    workflow::UnaryExpression,
)
workflow::ProcedureCall_strategy = st.builds(
    workflow::ProcedureCall,
    name=
        safe_text
)
workflow::Constant_strategy = st.builds(
    workflow::Constant,
    asInteger=
        safe_text,
    asReal=
        safe_text,
    asBoolean=
        safe_text,
    asString=
        safe_text
)
Declaration_strategy = st.builds(
    Declaration,
)
workflow::ParameterDeclaration_strategy = st.builds(
    workflow::ParameterDeclaration,
    type=
        safe_text
)
workflow::VariableDeclaration_strategy = st.builds(
    workflow::VariableDeclaration,
    type=
        safe_text,
    isConstant=
        safe_text
)
workflow::Variable_strategy = st.builds(
    workflow::Variable,
    name=
        safe_text
)
Statement_strategy = st.builds(
    Statement,
)
workflow::Write_strategy = st.builds(
    workflow::Write,
)
workflow::Read_strategy = st.builds(
    workflow::Read,
    type=
        safe_text
)
workflow::If_strategy = st.builds(
    workflow::If,
)
workflow::Declaration_strategy = st.builds(
    workflow::Declaration,
    name=
        safe_text
)
workflow::Expression_strategy = st.builds(
    workflow::Expression,
)
workflow::VariableAssignment_strategy = st.builds(
    workflow::VariableAssignment,
)
workflow::While_strategy = st.builds(
    workflow::While,
)
workflow::ProcedureReturn_strategy = st.builds(
    workflow::ProcedureReturn,
)
workflow::Block_strategy = st.builds(
    workflow::Block,
)
workflow::Statement_strategy = st.builds(
    workflow::Statement,
)
workflow::ProcedureDeclaration_strategy = st.builds(
    workflow::ProcedureDeclaration,
    returnType=
        safe_text,
    accessModifier=
        safe_text
)
workflow::CompilationUnit_strategy = st.builds(
    workflow::CompilationUnit,
    language=
        safe_text,
    name=
        safe_text
)

@given(instance=ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_arithmeticexpression_instantiation(instance):
    assert isinstance(instance, ArithmeticExpression)

@given(instance=workflow::Division_strategy)
@settings(max_examples=50)
def test_workflow::division_instantiation(instance):
    assert isinstance(instance, workflow::Division)

@given(instance=workflow::Multiplication_strategy)
@settings(max_examples=50)
def test_workflow::multiplication_instantiation(instance):
    assert isinstance(instance, workflow::Multiplication)

@given(instance=workflow::Subtraction_strategy)
@settings(max_examples=50)
def test_workflow::subtraction_instantiation(instance):
    assert isinstance(instance, workflow::Subtraction)

@given(instance=workflow::Addition_strategy)
@settings(max_examples=50)
def test_workflow::addition_instantiation(instance):
    assert isinstance(instance, workflow::Addition)

@given(instance=EqualityExpression_strategy)
@settings(max_examples=50)
def test_equalityexpression_instantiation(instance):
    assert isinstance(instance, EqualityExpression)

@given(instance=workflow::LessThanOrEqual_strategy)
@settings(max_examples=50)
def test_workflow::lessthanorequal_instantiation(instance):
    assert isinstance(instance, workflow::LessThanOrEqual)

@given(instance=workflow::NotEqual_strategy)
@settings(max_examples=50)
def test_workflow::notequal_instantiation(instance):
    assert isinstance(instance, workflow::NotEqual)

@given(instance=workflow::GreaterThanOrEqual_strategy)
@settings(max_examples=50)
def test_workflow::greaterthanorequal_instantiation(instance):
    assert isinstance(instance, workflow::GreaterThanOrEqual)

@given(instance=workflow::LessThan_strategy)
@settings(max_examples=50)
def test_workflow::lessthan_instantiation(instance):
    assert isinstance(instance, workflow::LessThan)

@given(instance=workflow::GreaterThan_strategy)
@settings(max_examples=50)
def test_workflow::greaterthan_instantiation(instance):
    assert isinstance(instance, workflow::GreaterThan)

@given(instance=workflow::Equal_strategy)
@settings(max_examples=50)
def test_workflow::equal_instantiation(instance):
    assert isinstance(instance, workflow::Equal)

@given(instance=LogicExpression_strategy)
@settings(max_examples=50)
def test_logicexpression_instantiation(instance):
    assert isinstance(instance, LogicExpression)

@given(instance=workflow::Or_strategy)
@settings(max_examples=50)
def test_workflow::or_instantiation(instance):
    assert isinstance(instance, workflow::Or)

@given(instance=workflow::And_strategy)
@settings(max_examples=50)
def test_workflow::and_instantiation(instance):
    assert isinstance(instance, workflow::And)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=workflow::ArithmeticExpression_strategy)
@settings(max_examples=50)
def test_workflow::arithmeticexpression_instantiation(instance):
    assert isinstance(instance, workflow::ArithmeticExpression)

@given(instance=workflow::EqualityExpression_strategy)
@settings(max_examples=50)
def test_workflow::equalityexpression_instantiation(instance):
    assert isinstance(instance, workflow::EqualityExpression)

@given(instance=workflow::LogicExpression_strategy)
@settings(max_examples=50)
def test_workflow::logicexpression_instantiation(instance):
    assert isinstance(instance, workflow::LogicExpression)

@given(instance=UnaryExpression_strategy)
@settings(max_examples=50)
def test_unaryexpression_instantiation(instance):
    assert isinstance(instance, UnaryExpression)

@given(instance=workflow::UMinus_strategy)
@settings(max_examples=50)
def test_workflow::uminus_instantiation(instance):
    assert isinstance(instance, workflow::UMinus)

@given(instance=workflow::Not_strategy)
@settings(max_examples=50)
def test_workflow::not_instantiation(instance):
    assert isinstance(instance, workflow::Not)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=workflow::BinaryExpression_strategy)
@settings(max_examples=50)
def test_workflow::binaryexpression_instantiation(instance):
    assert isinstance(instance, workflow::BinaryExpression)

@given(instance=workflow::UnaryExpression_strategy)
@settings(max_examples=50)
def test_workflow::unaryexpression_instantiation(instance):
    assert isinstance(instance, workflow::UnaryExpression)

@given(instance=workflow::ProcedureCall_strategy)
@settings(max_examples=50)
def test_workflow::procedurecall_instantiation(instance):
    assert isinstance(instance, workflow::ProcedureCall)

@given(instance=workflow::ProcedureCall_strategy)
def test_workflow::procedurecall_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::ProcedureCall_strategy)
def test_workflow::procedurecall_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::Constant_strategy)
@settings(max_examples=50)
def test_workflow::constant_instantiation(instance):
    assert isinstance(instance, workflow::Constant)

@given(instance=workflow::Constant_strategy)
def test_workflow::constant_asInteger_type(instance):
    assert isinstance(instance.asInteger, str)


@given(instance=workflow::Constant_strategy)
def test_workflow::constant_asInteger_setter(instance):
    original = instance.asInteger
    instance.asInteger = original
    assert instance.asInteger == original

@given(instance=workflow::Constant_strategy)
def test_workflow::constant_asReal_type(instance):
    assert isinstance(instance.asReal, str)


@given(instance=workflow::Constant_strategy)
def test_workflow::constant_asReal_setter(instance):
    original = instance.asReal
    instance.asReal = original
    assert instance.asReal == original

@given(instance=workflow::Constant_strategy)
def test_workflow::constant_asBoolean_type(instance):
    assert isinstance(instance.asBoolean, str)


@given(instance=workflow::Constant_strategy)
def test_workflow::constant_asBoolean_setter(instance):
    original = instance.asBoolean
    instance.asBoolean = original
    assert instance.asBoolean == original

@given(instance=workflow::Constant_strategy)
def test_workflow::constant_asString_type(instance):
    assert isinstance(instance.asString, str)


@given(instance=workflow::Constant_strategy)
def test_workflow::constant_asString_setter(instance):
    original = instance.asString
    instance.asString = original
    assert instance.asString == original

@given(instance=Declaration_strategy)
@settings(max_examples=50)
def test_declaration_instantiation(instance):
    assert isinstance(instance, Declaration)

@given(instance=workflow::ParameterDeclaration_strategy)
@settings(max_examples=50)
def test_workflow::parameterdeclaration_instantiation(instance):
    assert isinstance(instance, workflow::ParameterDeclaration)

@given(instance=workflow::ParameterDeclaration_strategy)
def test_workflow::parameterdeclaration_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=workflow::ParameterDeclaration_strategy)
def test_workflow::parameterdeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=workflow::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_workflow::variabledeclaration_instantiation(instance):
    assert isinstance(instance, workflow::VariableDeclaration)

@given(instance=workflow::VariableDeclaration_strategy)
def test_workflow::variabledeclaration_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=workflow::VariableDeclaration_strategy)
def test_workflow::variabledeclaration_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=workflow::VariableDeclaration_strategy)
def test_workflow::variabledeclaration_isConstant_type(instance):
    assert isinstance(instance.isConstant, str)


@given(instance=workflow::VariableDeclaration_strategy)
def test_workflow::variabledeclaration_isConstant_setter(instance):
    original = instance.isConstant
    instance.isConstant = original
    assert instance.isConstant == original

@given(instance=workflow::Variable_strategy)
@settings(max_examples=50)
def test_workflow::variable_instantiation(instance):
    assert isinstance(instance, workflow::Variable)

@given(instance=workflow::Variable_strategy)
def test_workflow::variable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Variable_strategy)
def test_workflow::variable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=workflow::Write_strategy)
@settings(max_examples=50)
def test_workflow::write_instantiation(instance):
    assert isinstance(instance, workflow::Write)

@given(instance=workflow::Read_strategy)
@settings(max_examples=50)
def test_workflow::read_instantiation(instance):
    assert isinstance(instance, workflow::Read)

@given(instance=workflow::Read_strategy)
def test_workflow::read_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=workflow::Read_strategy)
def test_workflow::read_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=workflow::If_strategy)
@settings(max_examples=50)
def test_workflow::if_instantiation(instance):
    assert isinstance(instance, workflow::If)

@given(instance=workflow::Declaration_strategy)
@settings(max_examples=50)
def test_workflow::declaration_instantiation(instance):
    assert isinstance(instance, workflow::Declaration)

@given(instance=workflow::Declaration_strategy)
def test_workflow::declaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::Declaration_strategy)
def test_workflow::declaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=workflow::Expression_strategy)
@settings(max_examples=50)
def test_workflow::expression_instantiation(instance):
    assert isinstance(instance, workflow::Expression)

@given(instance=workflow::VariableAssignment_strategy)
@settings(max_examples=50)
def test_workflow::variableassignment_instantiation(instance):
    assert isinstance(instance, workflow::VariableAssignment)

@given(instance=workflow::While_strategy)
@settings(max_examples=50)
def test_workflow::while_instantiation(instance):
    assert isinstance(instance, workflow::While)

@given(instance=workflow::ProcedureReturn_strategy)
@settings(max_examples=50)
def test_workflow::procedurereturn_instantiation(instance):
    assert isinstance(instance, workflow::ProcedureReturn)

@given(instance=workflow::Block_strategy)
@settings(max_examples=50)
def test_workflow::block_instantiation(instance):
    assert isinstance(instance, workflow::Block)

@given(instance=workflow::Statement_strategy)
@settings(max_examples=50)
def test_workflow::statement_instantiation(instance):
    assert isinstance(instance, workflow::Statement)

@given(instance=workflow::ProcedureDeclaration_strategy)
@settings(max_examples=50)
def test_workflow::proceduredeclaration_instantiation(instance):
    assert isinstance(instance, workflow::ProcedureDeclaration)

@given(instance=workflow::ProcedureDeclaration_strategy)
def test_workflow::proceduredeclaration_returnType_type(instance):
    assert isinstance(instance.returnType, str)


@given(instance=workflow::ProcedureDeclaration_strategy)
def test_workflow::proceduredeclaration_returnType_setter(instance):
    original = instance.returnType
    instance.returnType = original
    assert instance.returnType == original

@given(instance=workflow::ProcedureDeclaration_strategy)
def test_workflow::proceduredeclaration_accessModifier_type(instance):
    assert isinstance(instance.accessModifier, str)


@given(instance=workflow::ProcedureDeclaration_strategy)
def test_workflow::proceduredeclaration_accessModifier_setter(instance):
    original = instance.accessModifier
    instance.accessModifier = original
    assert instance.accessModifier == original

@given(instance=workflow::CompilationUnit_strategy)
@settings(max_examples=50)
def test_workflow::compilationunit_instantiation(instance):
    assert isinstance(instance, workflow::CompilationUnit)

@given(instance=workflow::CompilationUnit_strategy)
def test_workflow::compilationunit_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=workflow::CompilationUnit_strategy)
def test_workflow::compilationunit_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=workflow::CompilationUnit_strategy)
def test_workflow::compilationunit_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=workflow::CompilationUnit_strategy)
def test_workflow::compilationunit_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
