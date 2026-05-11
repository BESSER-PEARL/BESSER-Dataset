import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    behaviour::Variable,
    behaviour::ReadLine,
    behaviour::BinaryExpression,
    behaviour::FunctionCall,
    behaviour::Literal,
    ComparisonOperator,
    behaviour::Equals,
    ArithmeticOperation,
    behaviour::Plus,
    BinaryExpression,
    behaviour::ComparisonOperator,
    behaviour::ArithmeticOperation,
    behaviour::Expression,
    Statement,
    behaviour::LoopStatement,
    behaviour::AssignmentStatement,
    behaviour::CondionalStatement,
    behaviour::ExceptionStatement,
    behaviour::TryCatchStatement,
    behaviour::CallFunctionStatement,
    behaviour::ReturnStatement,
    behaviour::DeclarationStatement,
    behaviour::Statement,
    behaviour::Function,
    behaviour::Behaviour,
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



def test_behaviour::variable_is_not_abstract():
    assert not inspect.isabstract(behaviour::Variable)


def test_behaviour::variable_constructor_exists():
    assert callable(behaviour::Variable.__init__)


def test_behaviour::variable_constructor_args():
    sig = inspect.signature(behaviour::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_behaviour::variable_has_varName():
    assert hasattr(behaviour::Variable, "varName")
    descriptor = None
    for klass in behaviour::Variable.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::readline_is_not_abstract():
    assert not inspect.isabstract(behaviour::ReadLine)


def test_behaviour::readline_constructor_exists():
    assert callable(behaviour::ReadLine.__init__)


def test_behaviour::readline_constructor_args():
    sig = inspect.signature(behaviour::ReadLine.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour::BinaryExpression)


def test_behaviour::binaryexpression_constructor_exists():
    assert callable(behaviour::BinaryExpression.__init__)


def test_behaviour::binaryexpression_constructor_args():
    sig = inspect.signature(behaviour::BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::functioncall_is_not_abstract():
    assert not inspect.isabstract(behaviour::FunctionCall)


def test_behaviour::functioncall_constructor_exists():
    assert callable(behaviour::FunctionCall.__init__)


def test_behaviour::functioncall_constructor_args():
    sig = inspect.signature(behaviour::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "funcName" in params, "Missing parameter 'funcName'"

def test_behaviour::functioncall_has_funcName():
    assert hasattr(behaviour::FunctionCall, "funcName")
    descriptor = None
    for klass in behaviour::FunctionCall.__mro__:
        if "funcName" in klass.__dict__:
            descriptor = klass.__dict__["funcName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::literal_is_not_abstract():
    assert not inspect.isabstract(behaviour::Literal)


def test_behaviour::literal_constructor_exists():
    assert callable(behaviour::Literal.__init__)


def test_behaviour::literal_constructor_args():
    sig = inspect.signature(behaviour::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "vlaue" in params, "Missing parameter 'vlaue'"

def test_behaviour::literal_has_vlaue():
    assert hasattr(behaviour::Literal, "vlaue")
    descriptor = None
    for klass in behaviour::Literal.__mro__:
        if "vlaue" in klass.__dict__:
            descriptor = klass.__dict__["vlaue"]
            break
    assert isinstance(descriptor, property)



def test_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(ComparisonOperator)


def test_comparisonoperator_constructor_exists():
    assert callable(ComparisonOperator.__init__)


def test_comparisonoperator_constructor_args():
    sig = inspect.signature(ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::equals_is_not_abstract():
    assert not inspect.isabstract(behaviour::Equals)


def test_behaviour::equals_constructor_exists():
    assert callable(behaviour::Equals.__init__)


def test_behaviour::equals_constructor_args():
    sig = inspect.signature(behaviour::Equals.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperation_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperation)


def test_arithmeticoperation_constructor_exists():
    assert callable(ArithmeticOperation.__init__)


def test_arithmeticoperation_constructor_args():
    sig = inspect.signature(ArithmeticOperation.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::plus_is_not_abstract():
    assert not inspect.isabstract(behaviour::Plus)


def test_behaviour::plus_constructor_exists():
    assert callable(behaviour::Plus.__init__)


def test_behaviour::plus_constructor_args():
    sig = inspect.signature(behaviour::Plus.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(behaviour::ComparisonOperator)


def test_behaviour::comparisonoperator_constructor_exists():
    assert callable(behaviour::ComparisonOperator.__init__)


def test_behaviour::comparisonoperator_constructor_args():
    sig = inspect.signature(behaviour::ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::arithmeticoperation_is_not_abstract():
    assert not inspect.isabstract(behaviour::ArithmeticOperation)


def test_behaviour::arithmeticoperation_constructor_exists():
    assert callable(behaviour::ArithmeticOperation.__init__)


def test_behaviour::arithmeticoperation_constructor_args():
    sig = inspect.signature(behaviour::ArithmeticOperation.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::expression_is_not_abstract():
    assert not inspect.isabstract(behaviour::Expression)


def test_behaviour::expression_constructor_exists():
    assert callable(behaviour::Expression.__init__)


def test_behaviour::expression_constructor_args():
    sig = inspect.signature(behaviour::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::loopstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour::LoopStatement)


def test_behaviour::loopstatement_constructor_exists():
    assert callable(behaviour::LoopStatement.__init__)


def test_behaviour::loopstatement_constructor_args():
    sig = inspect.signature(behaviour::LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour::AssignmentStatement)


def test_behaviour::assignmentstatement_constructor_exists():
    assert callable(behaviour::AssignmentStatement.__init__)


def test_behaviour::assignmentstatement_constructor_args():
    sig = inspect.signature(behaviour::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_behaviour::assignmentstatement_has_varName():
    assert hasattr(behaviour::AssignmentStatement, "varName")
    descriptor = None
    for klass in behaviour::AssignmentStatement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::condionalstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour::CondionalStatement)


def test_behaviour::condionalstatement_constructor_exists():
    assert callable(behaviour::CondionalStatement.__init__)


def test_behaviour::condionalstatement_constructor_args():
    sig = inspect.signature(behaviour::CondionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::exceptionstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour::ExceptionStatement)


def test_behaviour::exceptionstatement_constructor_exists():
    assert callable(behaviour::ExceptionStatement.__init__)


def test_behaviour::exceptionstatement_constructor_args():
    sig = inspect.signature(behaviour::ExceptionStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::trycatchstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour::TryCatchStatement)


def test_behaviour::trycatchstatement_constructor_exists():
    assert callable(behaviour::TryCatchStatement.__init__)


def test_behaviour::trycatchstatement_constructor_args():
    sig = inspect.signature(behaviour::TryCatchStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::callfunctionstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour::CallFunctionStatement)


def test_behaviour::callfunctionstatement_constructor_exists():
    assert callable(behaviour::CallFunctionStatement.__init__)


def test_behaviour::callfunctionstatement_constructor_args():
    sig = inspect.signature(behaviour::CallFunctionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "nameFunc" in params, "Missing parameter 'nameFunc'"

def test_behaviour::callfunctionstatement_has_nameFunc():
    assert hasattr(behaviour::CallFunctionStatement, "nameFunc")
    descriptor = None
    for klass in behaviour::CallFunctionStatement.__mro__:
        if "nameFunc" in klass.__dict__:
            descriptor = klass.__dict__["nameFunc"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::returnstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour::ReturnStatement)


def test_behaviour::returnstatement_constructor_exists():
    assert callable(behaviour::ReturnStatement.__init__)


def test_behaviour::returnstatement_constructor_args():
    sig = inspect.signature(behaviour::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::declarationstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour::DeclarationStatement)


def test_behaviour::declarationstatement_constructor_exists():
    assert callable(behaviour::DeclarationStatement.__init__)


def test_behaviour::declarationstatement_constructor_args():
    sig = inspect.signature(behaviour::DeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "varType" in params, "Missing parameter 'varType'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_behaviour::declarationstatement_has_varType():
    assert hasattr(behaviour::DeclarationStatement, "varType")
    descriptor = None
    for klass in behaviour::DeclarationStatement.__mro__:
        if "varType" in klass.__dict__:
            descriptor = klass.__dict__["varType"]
            break
    assert isinstance(descriptor, property)

def test_behaviour::declarationstatement_has_varName():
    assert hasattr(behaviour::DeclarationStatement, "varName")
    descriptor = None
    for klass in behaviour::DeclarationStatement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::statement_is_not_abstract():
    assert not inspect.isabstract(behaviour::Statement)


def test_behaviour::statement_constructor_exists():
    assert callable(behaviour::Statement.__init__)


def test_behaviour::statement_constructor_args():
    sig = inspect.signature(behaviour::Statement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour::function_is_not_abstract():
    assert not inspect.isabstract(behaviour::Function)


def test_behaviour::function_constructor_exists():
    assert callable(behaviour::Function.__init__)


def test_behaviour::function_constructor_args():
    sig = inspect.signature(behaviour::Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behaviour::function_has_name():
    assert hasattr(behaviour::Function, "name")
    descriptor = None
    for klass in behaviour::Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_behaviour::behaviour_is_not_abstract():
    assert not inspect.isabstract(behaviour::Behaviour)


def test_behaviour::behaviour_constructor_exists():
    assert callable(behaviour::Behaviour.__init__)


def test_behaviour::behaviour_constructor_args():
    sig = inspect.signature(behaviour::Behaviour.__init__)
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
behaviour::Variable_strategy = st.builds(
    behaviour::Variable,
    varName=
        safe_text
)
behaviour::ReadLine_strategy = st.builds(
    behaviour::ReadLine,
)
behaviour::BinaryExpression_strategy = st.builds(
    behaviour::BinaryExpression,
)
behaviour::FunctionCall_strategy = st.builds(
    behaviour::FunctionCall,
    funcName=
        safe_text
)
behaviour::Literal_strategy = st.builds(
    behaviour::Literal,
    vlaue=
        safe_text
)
ComparisonOperator_strategy = st.builds(
    ComparisonOperator,
)
behaviour::Equals_strategy = st.builds(
    behaviour::Equals,
)
ArithmeticOperation_strategy = st.builds(
    ArithmeticOperation,
)
behaviour::Plus_strategy = st.builds(
    behaviour::Plus,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
behaviour::ComparisonOperator_strategy = st.builds(
    behaviour::ComparisonOperator,
)
behaviour::ArithmeticOperation_strategy = st.builds(
    behaviour::ArithmeticOperation,
)
behaviour::Expression_strategy = st.builds(
    behaviour::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
behaviour::LoopStatement_strategy = st.builds(
    behaviour::LoopStatement,
)
behaviour::AssignmentStatement_strategy = st.builds(
    behaviour::AssignmentStatement,
    varName=
        safe_text
)
behaviour::CondionalStatement_strategy = st.builds(
    behaviour::CondionalStatement,
)
behaviour::ExceptionStatement_strategy = st.builds(
    behaviour::ExceptionStatement,
)
behaviour::TryCatchStatement_strategy = st.builds(
    behaviour::TryCatchStatement,
)
behaviour::CallFunctionStatement_strategy = st.builds(
    behaviour::CallFunctionStatement,
    nameFunc=
        safe_text
)
behaviour::ReturnStatement_strategy = st.builds(
    behaviour::ReturnStatement,
)
behaviour::DeclarationStatement_strategy = st.builds(
    behaviour::DeclarationStatement,
    varType=
        safe_text,
    varName=
        safe_text
)
behaviour::Statement_strategy = st.builds(
    behaviour::Statement,
)
behaviour::Function_strategy = st.builds(
    behaviour::Function,
    name=
        safe_text
)
behaviour::Behaviour_strategy = st.builds(
    behaviour::Behaviour,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=behaviour::Variable_strategy)
@settings(max_examples=50)
def test_behaviour::variable_instantiation(instance):
    assert isinstance(instance, behaviour::Variable)

@given(instance=behaviour::Variable_strategy)
def test_behaviour::variable_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=behaviour::Variable_strategy)
def test_behaviour::variable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=behaviour::ReadLine_strategy)
@settings(max_examples=50)
def test_behaviour::readline_instantiation(instance):
    assert isinstance(instance, behaviour::ReadLine)

@given(instance=behaviour::BinaryExpression_strategy)
@settings(max_examples=50)
def test_behaviour::binaryexpression_instantiation(instance):
    assert isinstance(instance, behaviour::BinaryExpression)

@given(instance=behaviour::FunctionCall_strategy)
@settings(max_examples=50)
def test_behaviour::functioncall_instantiation(instance):
    assert isinstance(instance, behaviour::FunctionCall)

@given(instance=behaviour::FunctionCall_strategy)
def test_behaviour::functioncall_funcName_type(instance):
    assert isinstance(instance.funcName, str)


@given(instance=behaviour::FunctionCall_strategy)
def test_behaviour::functioncall_funcName_setter(instance):
    original = instance.funcName
    instance.funcName = original
    assert instance.funcName == original

@given(instance=behaviour::Literal_strategy)
@settings(max_examples=50)
def test_behaviour::literal_instantiation(instance):
    assert isinstance(instance, behaviour::Literal)

@given(instance=behaviour::Literal_strategy)
def test_behaviour::literal_vlaue_type(instance):
    assert isinstance(instance.vlaue, str)


@given(instance=behaviour::Literal_strategy)
def test_behaviour::literal_vlaue_setter(instance):
    original = instance.vlaue
    instance.vlaue = original
    assert instance.vlaue == original

@given(instance=ComparisonOperator_strategy)
@settings(max_examples=50)
def test_comparisonoperator_instantiation(instance):
    assert isinstance(instance, ComparisonOperator)

@given(instance=behaviour::Equals_strategy)
@settings(max_examples=50)
def test_behaviour::equals_instantiation(instance):
    assert isinstance(instance, behaviour::Equals)

@given(instance=ArithmeticOperation_strategy)
@settings(max_examples=50)
def test_arithmeticoperation_instantiation(instance):
    assert isinstance(instance, ArithmeticOperation)

@given(instance=behaviour::Plus_strategy)
@settings(max_examples=50)
def test_behaviour::plus_instantiation(instance):
    assert isinstance(instance, behaviour::Plus)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=behaviour::ComparisonOperator_strategy)
@settings(max_examples=50)
def test_behaviour::comparisonoperator_instantiation(instance):
    assert isinstance(instance, behaviour::ComparisonOperator)

@given(instance=behaviour::ArithmeticOperation_strategy)
@settings(max_examples=50)
def test_behaviour::arithmeticoperation_instantiation(instance):
    assert isinstance(instance, behaviour::ArithmeticOperation)

@given(instance=behaviour::Expression_strategy)
@settings(max_examples=50)
def test_behaviour::expression_instantiation(instance):
    assert isinstance(instance, behaviour::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=behaviour::LoopStatement_strategy)
@settings(max_examples=50)
def test_behaviour::loopstatement_instantiation(instance):
    assert isinstance(instance, behaviour::LoopStatement)

@given(instance=behaviour::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_behaviour::assignmentstatement_instantiation(instance):
    assert isinstance(instance, behaviour::AssignmentStatement)

@given(instance=behaviour::AssignmentStatement_strategy)
def test_behaviour::assignmentstatement_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=behaviour::AssignmentStatement_strategy)
def test_behaviour::assignmentstatement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=behaviour::CondionalStatement_strategy)
@settings(max_examples=50)
def test_behaviour::condionalstatement_instantiation(instance):
    assert isinstance(instance, behaviour::CondionalStatement)

@given(instance=behaviour::ExceptionStatement_strategy)
@settings(max_examples=50)
def test_behaviour::exceptionstatement_instantiation(instance):
    assert isinstance(instance, behaviour::ExceptionStatement)

@given(instance=behaviour::TryCatchStatement_strategy)
@settings(max_examples=50)
def test_behaviour::trycatchstatement_instantiation(instance):
    assert isinstance(instance, behaviour::TryCatchStatement)

@given(instance=behaviour::CallFunctionStatement_strategy)
@settings(max_examples=50)
def test_behaviour::callfunctionstatement_instantiation(instance):
    assert isinstance(instance, behaviour::CallFunctionStatement)

@given(instance=behaviour::CallFunctionStatement_strategy)
def test_behaviour::callfunctionstatement_nameFunc_type(instance):
    assert isinstance(instance.nameFunc, str)


@given(instance=behaviour::CallFunctionStatement_strategy)
def test_behaviour::callfunctionstatement_nameFunc_setter(instance):
    original = instance.nameFunc
    instance.nameFunc = original
    assert instance.nameFunc == original

@given(instance=behaviour::ReturnStatement_strategy)
@settings(max_examples=50)
def test_behaviour::returnstatement_instantiation(instance):
    assert isinstance(instance, behaviour::ReturnStatement)

@given(instance=behaviour::DeclarationStatement_strategy)
@settings(max_examples=50)
def test_behaviour::declarationstatement_instantiation(instance):
    assert isinstance(instance, behaviour::DeclarationStatement)

@given(instance=behaviour::DeclarationStatement_strategy)
def test_behaviour::declarationstatement_varType_type(instance):
    assert isinstance(instance.varType, str)


@given(instance=behaviour::DeclarationStatement_strategy)
def test_behaviour::declarationstatement_varType_setter(instance):
    original = instance.varType
    instance.varType = original
    assert instance.varType == original

@given(instance=behaviour::DeclarationStatement_strategy)
def test_behaviour::declarationstatement_varName_type(instance):
    assert isinstance(instance.varName, str)


@given(instance=behaviour::DeclarationStatement_strategy)
def test_behaviour::declarationstatement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=behaviour::Statement_strategy)
@settings(max_examples=50)
def test_behaviour::statement_instantiation(instance):
    assert isinstance(instance, behaviour::Statement)

@given(instance=behaviour::Function_strategy)
@settings(max_examples=50)
def test_behaviour::function_instantiation(instance):
    assert isinstance(instance, behaviour::Function)

@given(instance=behaviour::Function_strategy)
def test_behaviour::function_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=behaviour::Function_strategy)
def test_behaviour::function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=behaviour::Behaviour_strategy)
@settings(max_examples=50)
def test_behaviour::behaviour_instantiation(instance):
    assert isinstance(instance, behaviour::Behaviour)
