import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    behaviour_FunctionCall,
    behaviour_ReadLine,
    behaviour_BinaryExpression,
    behaviour_Variable,
    behaviour_Literal,
    ComparisonOperator,
    behaviour_Equals,
    ArithmeticOperation,
    behaviour_Plus,
    BinaryExpression,
    behaviour_ComparisonOperator,
    behaviour_ArithmeticOperation,
    behaviour_Expression,
    Statement,
    behaviour_AssignmentStatement,
    behaviour_LoopStatement,
    behaviour_CondionalStatement,
    behaviour_ExceptionStatement,
    behaviour_TryCatchStatement,
    behaviour_CallFunctionStatement,
    behaviour_ReturnStatement,
    behaviour_DeclarationStatement,
    behaviour_Statement,
    behaviour_Function,
    behaviour_Behaviour,
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



def test_behaviour_functioncall_is_not_abstract():
    assert not inspect.isabstract(behaviour_FunctionCall)


def test_behaviour_functioncall_constructor_exists():
    assert callable(behaviour_FunctionCall.__init__)


def test_behaviour_functioncall_constructor_args():
    sig = inspect.signature(behaviour_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "funcName" in params, "Missing parameter 'funcName'"

def test_behaviour_functioncall_has_funcName():
    assert hasattr(behaviour_FunctionCall, "funcName")
    descriptor = None
    for klass in behaviour_FunctionCall.__mro__:
        if "funcName" in klass.__dict__:
            descriptor = klass.__dict__["funcName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_readline_is_not_abstract():
    assert not inspect.isabstract(behaviour_ReadLine)


def test_behaviour_readline_constructor_exists():
    assert callable(behaviour_ReadLine.__init__)


def test_behaviour_readline_constructor_args():
    sig = inspect.signature(behaviour_ReadLine.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(behaviour_BinaryExpression)


def test_behaviour_binaryexpression_constructor_exists():
    assert callable(behaviour_BinaryExpression.__init__)


def test_behaviour_binaryexpression_constructor_args():
    sig = inspect.signature(behaviour_BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_variable_is_not_abstract():
    assert not inspect.isabstract(behaviour_Variable)


def test_behaviour_variable_constructor_exists():
    assert callable(behaviour_Variable.__init__)


def test_behaviour_variable_constructor_args():
    sig = inspect.signature(behaviour_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_behaviour_variable_has_varName():
    assert hasattr(behaviour_Variable, "varName")
    descriptor = None
    for klass in behaviour_Variable.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_literal_is_not_abstract():
    assert not inspect.isabstract(behaviour_Literal)


def test_behaviour_literal_constructor_exists():
    assert callable(behaviour_Literal.__init__)


def test_behaviour_literal_constructor_args():
    sig = inspect.signature(behaviour_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "vlaue" in params, "Missing parameter 'vlaue'"

def test_behaviour_literal_has_vlaue():
    assert hasattr(behaviour_Literal, "vlaue")
    descriptor = None
    for klass in behaviour_Literal.__mro__:
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



def test_behaviour_equals_is_not_abstract():
    assert not inspect.isabstract(behaviour_Equals)


def test_behaviour_equals_constructor_exists():
    assert callable(behaviour_Equals.__init__)


def test_behaviour_equals_constructor_args():
    sig = inspect.signature(behaviour_Equals.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticoperation_is_not_abstract():
    assert not inspect.isabstract(ArithmeticOperation)


def test_arithmeticoperation_constructor_exists():
    assert callable(ArithmeticOperation.__init__)


def test_arithmeticoperation_constructor_args():
    sig = inspect.signature(ArithmeticOperation.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_plus_is_not_abstract():
    assert not inspect.isabstract(behaviour_Plus)


def test_behaviour_plus_constructor_exists():
    assert callable(behaviour_Plus.__init__)


def test_behaviour_plus_constructor_args():
    sig = inspect.signature(behaviour_Plus.__init__)
    params = list(sig.parameters.keys())



def test_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(BinaryExpression)


def test_binaryexpression_constructor_exists():
    assert callable(BinaryExpression.__init__)


def test_binaryexpression_constructor_args():
    sig = inspect.signature(BinaryExpression.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_comparisonoperator_is_not_abstract():
    assert not inspect.isabstract(behaviour_ComparisonOperator)


def test_behaviour_comparisonoperator_constructor_exists():
    assert callable(behaviour_ComparisonOperator.__init__)


def test_behaviour_comparisonoperator_constructor_args():
    sig = inspect.signature(behaviour_ComparisonOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_arithmeticoperation_is_not_abstract():
    assert not inspect.isabstract(behaviour_ArithmeticOperation)


def test_behaviour_arithmeticoperation_constructor_exists():
    assert callable(behaviour_ArithmeticOperation.__init__)


def test_behaviour_arithmeticoperation_constructor_args():
    sig = inspect.signature(behaviour_ArithmeticOperation.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_expression_is_not_abstract():
    assert not inspect.isabstract(behaviour_Expression)


def test_behaviour_expression_constructor_exists():
    assert callable(behaviour_Expression.__init__)


def test_behaviour_expression_constructor_args():
    sig = inspect.signature(behaviour_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour_AssignmentStatement)


def test_behaviour_assignmentstatement_constructor_exists():
    assert callable(behaviour_AssignmentStatement.__init__)


def test_behaviour_assignmentstatement_constructor_args():
    sig = inspect.signature(behaviour_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_behaviour_assignmentstatement_has_varName():
    assert hasattr(behaviour_AssignmentStatement, "varName")
    descriptor = None
    for klass in behaviour_AssignmentStatement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_loopstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour_LoopStatement)


def test_behaviour_loopstatement_constructor_exists():
    assert callable(behaviour_LoopStatement.__init__)


def test_behaviour_loopstatement_constructor_args():
    sig = inspect.signature(behaviour_LoopStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_condionalstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour_CondionalStatement)


def test_behaviour_condionalstatement_constructor_exists():
    assert callable(behaviour_CondionalStatement.__init__)


def test_behaviour_condionalstatement_constructor_args():
    sig = inspect.signature(behaviour_CondionalStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_exceptionstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour_ExceptionStatement)


def test_behaviour_exceptionstatement_constructor_exists():
    assert callable(behaviour_ExceptionStatement.__init__)


def test_behaviour_exceptionstatement_constructor_args():
    sig = inspect.signature(behaviour_ExceptionStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_trycatchstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour_TryCatchStatement)


def test_behaviour_trycatchstatement_constructor_exists():
    assert callable(behaviour_TryCatchStatement.__init__)


def test_behaviour_trycatchstatement_constructor_args():
    sig = inspect.signature(behaviour_TryCatchStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_callfunctionstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour_CallFunctionStatement)


def test_behaviour_callfunctionstatement_constructor_exists():
    assert callable(behaviour_CallFunctionStatement.__init__)


def test_behaviour_callfunctionstatement_constructor_args():
    sig = inspect.signature(behaviour_CallFunctionStatement.__init__)
    params = list(sig.parameters.keys())
    assert "nameFunc" in params, "Missing parameter 'nameFunc'"

def test_behaviour_callfunctionstatement_has_nameFunc():
    assert hasattr(behaviour_CallFunctionStatement, "nameFunc")
    descriptor = None
    for klass in behaviour_CallFunctionStatement.__mro__:
        if "nameFunc" in klass.__dict__:
            descriptor = klass.__dict__["nameFunc"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_returnstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour_ReturnStatement)


def test_behaviour_returnstatement_constructor_exists():
    assert callable(behaviour_ReturnStatement.__init__)


def test_behaviour_returnstatement_constructor_args():
    sig = inspect.signature(behaviour_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_declarationstatement_is_not_abstract():
    assert not inspect.isabstract(behaviour_DeclarationStatement)


def test_behaviour_declarationstatement_constructor_exists():
    assert callable(behaviour_DeclarationStatement.__init__)


def test_behaviour_declarationstatement_constructor_args():
    sig = inspect.signature(behaviour_DeclarationStatement.__init__)
    params = list(sig.parameters.keys())
    assert "varType" in params, "Missing parameter 'varType'"
    assert "varName" in params, "Missing parameter 'varName'"

def test_behaviour_declarationstatement_has_varType():
    assert hasattr(behaviour_DeclarationStatement, "varType")
    descriptor = None
    for klass in behaviour_DeclarationStatement.__mro__:
        if "varType" in klass.__dict__:
            descriptor = klass.__dict__["varType"]
            break
    assert isinstance(descriptor, property)

def test_behaviour_declarationstatement_has_varName():
    assert hasattr(behaviour_DeclarationStatement, "varName")
    descriptor = None
    for klass in behaviour_DeclarationStatement.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_statement_is_not_abstract():
    assert not inspect.isabstract(behaviour_Statement)


def test_behaviour_statement_constructor_exists():
    assert callable(behaviour_Statement.__init__)


def test_behaviour_statement_constructor_args():
    sig = inspect.signature(behaviour_Statement.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_function_is_not_abstract():
    assert not inspect.isabstract(behaviour_Function)


def test_behaviour_function_constructor_exists():
    assert callable(behaviour_Function.__init__)


def test_behaviour_function_constructor_args():
    sig = inspect.signature(behaviour_Function.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_behaviour_function_has_name():
    assert hasattr(behaviour_Function, "name")
    descriptor = None
    for klass in behaviour_Function.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_behaviour_behaviour_is_not_abstract():
    assert not inspect.isabstract(behaviour_Behaviour)


def test_behaviour_behaviour_constructor_exists():
    assert callable(behaviour_Behaviour.__init__)


def test_behaviour_behaviour_constructor_args():
    sig = inspect.signature(behaviour_Behaviour.__init__)
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
behaviour_FunctionCall_strategy = st.builds(
    behaviour_FunctionCall,
    funcName=
        safe_text
)
behaviour_ReadLine_strategy = st.builds(
    behaviour_ReadLine,
)
behaviour_BinaryExpression_strategy = st.builds(
    behaviour_BinaryExpression,
)
behaviour_Variable_strategy = st.builds(
    behaviour_Variable,
    varName=
        safe_text
)
behaviour_Literal_strategy = st.builds(
    behaviour_Literal,
    vlaue=
        safe_text
)
ComparisonOperator_strategy = st.builds(
    ComparisonOperator,
)
behaviour_Equals_strategy = st.builds(
    behaviour_Equals,
)
ArithmeticOperation_strategy = st.builds(
    ArithmeticOperation,
)
behaviour_Plus_strategy = st.builds(
    behaviour_Plus,
)
BinaryExpression_strategy = st.builds(
    BinaryExpression,
)
behaviour_ComparisonOperator_strategy = st.builds(
    behaviour_ComparisonOperator,
)
behaviour_ArithmeticOperation_strategy = st.builds(
    behaviour_ArithmeticOperation,
)
behaviour_Expression_strategy = st.builds(
    behaviour_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
behaviour_AssignmentStatement_strategy = st.builds(
    behaviour_AssignmentStatement,
    varName=
        safe_text
)
behaviour_LoopStatement_strategy = st.builds(
    behaviour_LoopStatement,
)
behaviour_CondionalStatement_strategy = st.builds(
    behaviour_CondionalStatement,
)
behaviour_ExceptionStatement_strategy = st.builds(
    behaviour_ExceptionStatement,
)
behaviour_TryCatchStatement_strategy = st.builds(
    behaviour_TryCatchStatement,
)
behaviour_CallFunctionStatement_strategy = st.builds(
    behaviour_CallFunctionStatement,
    nameFunc=
        safe_text
)
behaviour_ReturnStatement_strategy = st.builds(
    behaviour_ReturnStatement,
)
behaviour_DeclarationStatement_strategy = st.builds(
    behaviour_DeclarationStatement,
    varType=
        safe_text,
    varName=
        safe_text
)
behaviour_Statement_strategy = st.builds(
    behaviour_Statement,
)
behaviour_Function_strategy = st.builds(
    behaviour_Function,
    name=
        safe_text
)
behaviour_Behaviour_strategy = st.builds(
    behaviour_Behaviour,
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=behaviour_FunctionCall_strategy)
@settings(max_examples=50)
def test_behaviour_functioncall_instantiation(instance):
    assert isinstance(instance, behaviour_FunctionCall)



@given(instance=behaviour_FunctionCall_strategy)
def test_behaviour_functioncall_funcName_setter(instance):
    original = instance.funcName
    instance.funcName = original
    assert instance.funcName == original

@given(instance=behaviour_ReadLine_strategy)
@settings(max_examples=50)
def test_behaviour_readline_instantiation(instance):
    assert isinstance(instance, behaviour_ReadLine)

@given(instance=behaviour_BinaryExpression_strategy)
@settings(max_examples=50)
def test_behaviour_binaryexpression_instantiation(instance):
    assert isinstance(instance, behaviour_BinaryExpression)

@given(instance=behaviour_Variable_strategy)
@settings(max_examples=50)
def test_behaviour_variable_instantiation(instance):
    assert isinstance(instance, behaviour_Variable)



@given(instance=behaviour_Variable_strategy)
def test_behaviour_variable_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=behaviour_Literal_strategy)
@settings(max_examples=50)
def test_behaviour_literal_instantiation(instance):
    assert isinstance(instance, behaviour_Literal)



@given(instance=behaviour_Literal_strategy)
def test_behaviour_literal_vlaue_setter(instance):
    original = instance.vlaue
    instance.vlaue = original
    assert instance.vlaue == original

@given(instance=ComparisonOperator_strategy)
@settings(max_examples=50)
def test_comparisonoperator_instantiation(instance):
    assert isinstance(instance, ComparisonOperator)

@given(instance=behaviour_Equals_strategy)
@settings(max_examples=50)
def test_behaviour_equals_instantiation(instance):
    assert isinstance(instance, behaviour_Equals)

@given(instance=ArithmeticOperation_strategy)
@settings(max_examples=50)
def test_arithmeticoperation_instantiation(instance):
    assert isinstance(instance, ArithmeticOperation)

@given(instance=behaviour_Plus_strategy)
@settings(max_examples=50)
def test_behaviour_plus_instantiation(instance):
    assert isinstance(instance, behaviour_Plus)

@given(instance=BinaryExpression_strategy)
@settings(max_examples=50)
def test_binaryexpression_instantiation(instance):
    assert isinstance(instance, BinaryExpression)

@given(instance=behaviour_ComparisonOperator_strategy)
@settings(max_examples=50)
def test_behaviour_comparisonoperator_instantiation(instance):
    assert isinstance(instance, behaviour_ComparisonOperator)

@given(instance=behaviour_ArithmeticOperation_strategy)
@settings(max_examples=50)
def test_behaviour_arithmeticoperation_instantiation(instance):
    assert isinstance(instance, behaviour_ArithmeticOperation)

@given(instance=behaviour_Expression_strategy)
@settings(max_examples=50)
def test_behaviour_expression_instantiation(instance):
    assert isinstance(instance, behaviour_Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=behaviour_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_behaviour_assignmentstatement_instantiation(instance):
    assert isinstance(instance, behaviour_AssignmentStatement)



@given(instance=behaviour_AssignmentStatement_strategy)
def test_behaviour_assignmentstatement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=behaviour_LoopStatement_strategy)
@settings(max_examples=50)
def test_behaviour_loopstatement_instantiation(instance):
    assert isinstance(instance, behaviour_LoopStatement)

@given(instance=behaviour_CondionalStatement_strategy)
@settings(max_examples=50)
def test_behaviour_condionalstatement_instantiation(instance):
    assert isinstance(instance, behaviour_CondionalStatement)

@given(instance=behaviour_ExceptionStatement_strategy)
@settings(max_examples=50)
def test_behaviour_exceptionstatement_instantiation(instance):
    assert isinstance(instance, behaviour_ExceptionStatement)

@given(instance=behaviour_TryCatchStatement_strategy)
@settings(max_examples=50)
def test_behaviour_trycatchstatement_instantiation(instance):
    assert isinstance(instance, behaviour_TryCatchStatement)

@given(instance=behaviour_CallFunctionStatement_strategy)
@settings(max_examples=50)
def test_behaviour_callfunctionstatement_instantiation(instance):
    assert isinstance(instance, behaviour_CallFunctionStatement)



@given(instance=behaviour_CallFunctionStatement_strategy)
def test_behaviour_callfunctionstatement_nameFunc_setter(instance):
    original = instance.nameFunc
    instance.nameFunc = original
    assert instance.nameFunc == original

@given(instance=behaviour_ReturnStatement_strategy)
@settings(max_examples=50)
def test_behaviour_returnstatement_instantiation(instance):
    assert isinstance(instance, behaviour_ReturnStatement)

@given(instance=behaviour_DeclarationStatement_strategy)
@settings(max_examples=50)
def test_behaviour_declarationstatement_instantiation(instance):
    assert isinstance(instance, behaviour_DeclarationStatement)



@given(instance=behaviour_DeclarationStatement_strategy)
def test_behaviour_declarationstatement_varType_setter(instance):
    original = instance.varType
    instance.varType = original
    assert instance.varType == original



@given(instance=behaviour_DeclarationStatement_strategy)
def test_behaviour_declarationstatement_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=behaviour_Statement_strategy)
@settings(max_examples=50)
def test_behaviour_statement_instantiation(instance):
    assert isinstance(instance, behaviour_Statement)

@given(instance=behaviour_Function_strategy)
@settings(max_examples=50)
def test_behaviour_function_instantiation(instance):
    assert isinstance(instance, behaviour_Function)



@given(instance=behaviour_Function_strategy)
def test_behaviour_function_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=behaviour_Behaviour_strategy)
@settings(max_examples=50)
def test_behaviour_behaviour_instantiation(instance):
    assert isinstance(instance, behaviour_Behaviour)
