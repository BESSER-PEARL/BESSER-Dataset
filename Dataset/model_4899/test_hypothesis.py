import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ComparsionOperator,
    behaviouralProgramMM_Equals,
    FunctionCallStatement,
    behaviouralProgramMM_WriteLineStatement,
    behaviouralProgramMM_ReadLineStatement,
    ArithmeticInfixOperator,
    behaviouralProgramMM_Plus,
    BinaryOperator,
    behaviouralProgramMM_ComparsionOperator,
    behaviouralProgramMM_ArithmeticInfixOperator,
    Expression,
    behaviouralProgramMM_Literal,
    behaviouralProgramMM_Variable,
    behaviouralProgramMM_BinaryOperator,
    behaviouralProgramMM_ReadLine,
    behaviouralProgramMM_FunctionCall,
    behaviouralProgramMM_Expression,
    Statement,
    behaviouralProgramMM_Instantiation,
    behaviouralProgramMM_Loop,
    behaviouralProgramMM_RaiseException,
    behaviouralProgramMM_ConditionalBranch,
    behaviouralProgramMM_FunctionCallStatement,
    behaviouralProgramMM_Assignment,
    behaviouralProgramMM_Statement,
    behaviouralProgramMM_TryCatch,
    behaviouralProgramMM_Return,
    behaviouralProgramMM_Function,
    behaviouralProgramMM_Behaviour,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_comparsionoperator_is_not_abstract():
    assert not inspect.isabstract(ComparsionOperator)


def test_comparsionoperator_constructor_exists():
    assert callable(ComparsionOperator.__init__)


def test_comparsionoperator_constructor_args():
    sig = inspect.signature(ComparsionOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_equals_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Equals)


def test_behaviouralprogrammm_equals_constructor_exists():
    assert callable(behaviouralProgramMM_Equals.__init__)


def test_behaviouralprogrammm_equals_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Equals.__init__)
    params = list(sig.parameters.keys())



def test_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(FunctionCallStatement)


def test_functioncallstatement_constructor_exists():
    assert callable(FunctionCallStatement.__init__)


def test_functioncallstatement_constructor_args():
    sig = inspect.signature(FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_writelinestatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_WriteLineStatement)


def test_behaviouralprogrammm_writelinestatement_constructor_exists():
    assert callable(behaviouralProgramMM_WriteLineStatement.__init__)


def test_behaviouralprogrammm_writelinestatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_WriteLineStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_readlinestatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ReadLineStatement)


def test_behaviouralprogrammm_readlinestatement_constructor_exists():
    assert callable(behaviouralProgramMM_ReadLineStatement.__init__)


def test_behaviouralprogrammm_readlinestatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ReadLineStatement.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticinfixoperator_is_not_abstract():
    assert not inspect.isabstract(ArithmeticInfixOperator)


def test_arithmeticinfixoperator_constructor_exists():
    assert callable(ArithmeticInfixOperator.__init__)


def test_arithmeticinfixoperator_constructor_args():
    sig = inspect.signature(ArithmeticInfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_plus_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Plus)


def test_behaviouralprogrammm_plus_constructor_exists():
    assert callable(behaviouralProgramMM_Plus.__init__)


def test_behaviouralprogrammm_plus_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Plus.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_comparsionoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ComparsionOperator)


def test_behaviouralprogrammm_comparsionoperator_constructor_exists():
    assert callable(behaviouralProgramMM_ComparsionOperator.__init__)


def test_behaviouralprogrammm_comparsionoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ComparsionOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_arithmeticinfixoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ArithmeticInfixOperator)


def test_behaviouralprogrammm_arithmeticinfixoperator_constructor_exists():
    assert callable(behaviouralProgramMM_ArithmeticInfixOperator.__init__)


def test_behaviouralprogrammm_arithmeticinfixoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ArithmeticInfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_literal_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Literal)


def test_behaviouralprogrammm_literal_constructor_exists():
    assert callable(behaviouralProgramMM_Literal.__init__)


def test_behaviouralprogrammm_literal_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_behaviouralprogrammm_literal_has_Value():
    assert hasattr(behaviouralProgramMM_Literal, "Value")
    descriptor = None
    for klass in behaviouralProgramMM_Literal.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm_variable_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Variable)


def test_behaviouralprogrammm_variable_constructor_exists():
    assert callable(behaviouralProgramMM_Variable.__init__)


def test_behaviouralprogrammm_variable_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "VarName" in params, "Missing parameter 'VarName'"

def test_behaviouralprogrammm_variable_has_VarName():
    assert hasattr(behaviouralProgramMM_Variable, "VarName")
    descriptor = None
    for klass in behaviouralProgramMM_Variable.__mro__:
        if "VarName" in klass.__dict__:
            descriptor = klass.__dict__["VarName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_BinaryOperator)


def test_behaviouralprogrammm_binaryoperator_constructor_exists():
    assert callable(behaviouralProgramMM_BinaryOperator.__init__)


def test_behaviouralprogrammm_binaryoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_readline_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ReadLine)


def test_behaviouralprogrammm_readline_constructor_exists():
    assert callable(behaviouralProgramMM_ReadLine.__init__)


def test_behaviouralprogrammm_readline_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ReadLine.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_functioncall_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_FunctionCall)


def test_behaviouralprogrammm_functioncall_constructor_exists():
    assert callable(behaviouralProgramMM_FunctionCall.__init__)


def test_behaviouralprogrammm_functioncall_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "FuncName" in params, "Missing parameter 'FuncName'"

def test_behaviouralprogrammm_functioncall_has_FuncName():
    assert hasattr(behaviouralProgramMM_FunctionCall, "FuncName")
    descriptor = None
    for klass in behaviouralProgramMM_FunctionCall.__mro__:
        if "FuncName" in klass.__dict__:
            descriptor = klass.__dict__["FuncName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm_expression_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Expression)


def test_behaviouralprogrammm_expression_constructor_exists():
    assert callable(behaviouralProgramMM_Expression.__init__)


def test_behaviouralprogrammm_expression_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_instantiation_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Instantiation)


def test_behaviouralprogrammm_instantiation_constructor_exists():
    assert callable(behaviouralProgramMM_Instantiation.__init__)


def test_behaviouralprogrammm_instantiation_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Instantiation.__init__)
    params = list(sig.parameters.keys())
    assert "VarType" in params, "Missing parameter 'VarType'"
    assert "VarName" in params, "Missing parameter 'VarName'"

def test_behaviouralprogrammm_instantiation_has_VarType():
    assert hasattr(behaviouralProgramMM_Instantiation, "VarType")
    descriptor = None
    for klass in behaviouralProgramMM_Instantiation.__mro__:
        if "VarType" in klass.__dict__:
            descriptor = klass.__dict__["VarType"]
            break
    assert isinstance(descriptor, property)

def test_behaviouralprogrammm_instantiation_has_VarName():
    assert hasattr(behaviouralProgramMM_Instantiation, "VarName")
    descriptor = None
    for klass in behaviouralProgramMM_Instantiation.__mro__:
        if "VarName" in klass.__dict__:
            descriptor = klass.__dict__["VarName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm_loop_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Loop)


def test_behaviouralprogrammm_loop_constructor_exists():
    assert callable(behaviouralProgramMM_Loop.__init__)


def test_behaviouralprogrammm_loop_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Loop.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_raiseexception_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_RaiseException)


def test_behaviouralprogrammm_raiseexception_constructor_exists():
    assert callable(behaviouralProgramMM_RaiseException.__init__)


def test_behaviouralprogrammm_raiseexception_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_RaiseException.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_conditionalbranch_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_ConditionalBranch)


def test_behaviouralprogrammm_conditionalbranch_constructor_exists():
    assert callable(behaviouralProgramMM_ConditionalBranch.__init__)


def test_behaviouralprogrammm_conditionalbranch_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_ConditionalBranch.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_FunctionCallStatement)


def test_behaviouralprogrammm_functioncallstatement_constructor_exists():
    assert callable(behaviouralProgramMM_FunctionCallStatement.__init__)


def test_behaviouralprogrammm_functioncallstatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())
    assert "FuncName" in params, "Missing parameter 'FuncName'"

def test_behaviouralprogrammm_functioncallstatement_has_FuncName():
    assert hasattr(behaviouralProgramMM_FunctionCallStatement, "FuncName")
    descriptor = None
    for klass in behaviouralProgramMM_FunctionCallStatement.__mro__:
        if "FuncName" in klass.__dict__:
            descriptor = klass.__dict__["FuncName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm_assignment_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Assignment)


def test_behaviouralprogrammm_assignment_constructor_exists():
    assert callable(behaviouralProgramMM_Assignment.__init__)


def test_behaviouralprogrammm_assignment_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "VariableName" in params, "Missing parameter 'VariableName'"

def test_behaviouralprogrammm_assignment_has_VariableName():
    assert hasattr(behaviouralProgramMM_Assignment, "VariableName")
    descriptor = None
    for klass in behaviouralProgramMM_Assignment.__mro__:
        if "VariableName" in klass.__dict__:
            descriptor = klass.__dict__["VariableName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm_statement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Statement)


def test_behaviouralprogrammm_statement_constructor_exists():
    assert callable(behaviouralProgramMM_Statement.__init__)


def test_behaviouralprogrammm_statement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Statement.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_trycatch_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_TryCatch)


def test_behaviouralprogrammm_trycatch_constructor_exists():
    assert callable(behaviouralProgramMM_TryCatch.__init__)


def test_behaviouralprogrammm_trycatch_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_TryCatch.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_return_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Return)


def test_behaviouralprogrammm_return_constructor_exists():
    assert callable(behaviouralProgramMM_Return.__init__)


def test_behaviouralprogrammm_return_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Return.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm_function_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Function)


def test_behaviouralprogrammm_function_constructor_exists():
    assert callable(behaviouralProgramMM_Function.__init__)


def test_behaviouralprogrammm_function_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Function.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_behaviouralprogrammm_function_has_Name():
    assert hasattr(behaviouralProgramMM_Function, "Name")
    descriptor = None
    for klass in behaviouralProgramMM_Function.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm_behaviour_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM_Behaviour)


def test_behaviouralprogrammm_behaviour_constructor_exists():
    assert callable(behaviouralProgramMM_Behaviour.__init__)


def test_behaviouralprogrammm_behaviour_constructor_args():
    sig = inspect.signature(behaviouralProgramMM_Behaviour.__init__)
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
ComparsionOperator_strategy = st.builds(
    ComparsionOperator,
)
behaviouralProgramMM_Equals_strategy = st.builds(
    behaviouralProgramMM_Equals,
)
FunctionCallStatement_strategy = st.builds(
    FunctionCallStatement,
)
behaviouralProgramMM_WriteLineStatement_strategy = st.builds(
    behaviouralProgramMM_WriteLineStatement,
)
behaviouralProgramMM_ReadLineStatement_strategy = st.builds(
    behaviouralProgramMM_ReadLineStatement,
)
ArithmeticInfixOperator_strategy = st.builds(
    ArithmeticInfixOperator,
)
behaviouralProgramMM_Plus_strategy = st.builds(
    behaviouralProgramMM_Plus,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
behaviouralProgramMM_ComparsionOperator_strategy = st.builds(
    behaviouralProgramMM_ComparsionOperator,
)
behaviouralProgramMM_ArithmeticInfixOperator_strategy = st.builds(
    behaviouralProgramMM_ArithmeticInfixOperator,
)
Expression_strategy = st.builds(
    Expression,
)
behaviouralProgramMM_Literal_strategy = st.builds(
    behaviouralProgramMM_Literal,
    Value=
        safe_text
)
behaviouralProgramMM_Variable_strategy = st.builds(
    behaviouralProgramMM_Variable,
    VarName=
        safe_text
)
behaviouralProgramMM_BinaryOperator_strategy = st.builds(
    behaviouralProgramMM_BinaryOperator,
)
behaviouralProgramMM_ReadLine_strategy = st.builds(
    behaviouralProgramMM_ReadLine,
)
behaviouralProgramMM_FunctionCall_strategy = st.builds(
    behaviouralProgramMM_FunctionCall,
    FuncName=
        safe_text
)
behaviouralProgramMM_Expression_strategy = st.builds(
    behaviouralProgramMM_Expression,
)
Statement_strategy = st.builds(
    Statement,
)
behaviouralProgramMM_Instantiation_strategy = st.builds(
    behaviouralProgramMM_Instantiation,
    VarType=
        safe_text,
    VarName=
        safe_text
)
behaviouralProgramMM_Loop_strategy = st.builds(
    behaviouralProgramMM_Loop,
)
behaviouralProgramMM_RaiseException_strategy = st.builds(
    behaviouralProgramMM_RaiseException,
)
behaviouralProgramMM_ConditionalBranch_strategy = st.builds(
    behaviouralProgramMM_ConditionalBranch,
)
behaviouralProgramMM_FunctionCallStatement_strategy = st.builds(
    behaviouralProgramMM_FunctionCallStatement,
    FuncName=
        safe_text
)
behaviouralProgramMM_Assignment_strategy = st.builds(
    behaviouralProgramMM_Assignment,
    VariableName=
        safe_text
)
behaviouralProgramMM_Statement_strategy = st.builds(
    behaviouralProgramMM_Statement,
)
behaviouralProgramMM_TryCatch_strategy = st.builds(
    behaviouralProgramMM_TryCatch,
)
behaviouralProgramMM_Return_strategy = st.builds(
    behaviouralProgramMM_Return,
)
behaviouralProgramMM_Function_strategy = st.builds(
    behaviouralProgramMM_Function,
    Name=
        safe_text
)
behaviouralProgramMM_Behaviour_strategy = st.builds(
    behaviouralProgramMM_Behaviour,
)

@given(instance=ComparsionOperator_strategy)
@settings(max_examples=50)
def test_comparsionoperator_instantiation(instance):
    assert isinstance(instance, ComparsionOperator)

@given(instance=behaviouralProgramMM_Equals_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_equals_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Equals)

@given(instance=FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_functioncallstatement_instantiation(instance):
    assert isinstance(instance, FunctionCallStatement)

@given(instance=behaviouralProgramMM_WriteLineStatement_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_writelinestatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_WriteLineStatement)

@given(instance=behaviouralProgramMM_ReadLineStatement_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_readlinestatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ReadLineStatement)

@given(instance=ArithmeticInfixOperator_strategy)
@settings(max_examples=50)
def test_arithmeticinfixoperator_instantiation(instance):
    assert isinstance(instance, ArithmeticInfixOperator)

@given(instance=behaviouralProgramMM_Plus_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_plus_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Plus)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=behaviouralProgramMM_ComparsionOperator_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_comparsionoperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ComparsionOperator)

@given(instance=behaviouralProgramMM_ArithmeticInfixOperator_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_arithmeticinfixoperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ArithmeticInfixOperator)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=behaviouralProgramMM_Literal_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_literal_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Literal)



@given(instance=behaviouralProgramMM_Literal_strategy)
def test_behaviouralprogrammm_literal_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=behaviouralProgramMM_Variable_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_variable_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Variable)



@given(instance=behaviouralProgramMM_Variable_strategy)
def test_behaviouralprogrammm_variable_VarName_setter(instance):
    original = instance.VarName
    instance.VarName = original
    assert instance.VarName == original

@given(instance=behaviouralProgramMM_BinaryOperator_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_binaryoperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_BinaryOperator)

@given(instance=behaviouralProgramMM_ReadLine_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_readline_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ReadLine)

@given(instance=behaviouralProgramMM_FunctionCall_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_functioncall_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_FunctionCall)



@given(instance=behaviouralProgramMM_FunctionCall_strategy)
def test_behaviouralprogrammm_functioncall_FuncName_setter(instance):
    original = instance.FuncName
    instance.FuncName = original
    assert instance.FuncName == original

@given(instance=behaviouralProgramMM_Expression_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_expression_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=behaviouralProgramMM_Instantiation_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_instantiation_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Instantiation)



@given(instance=behaviouralProgramMM_Instantiation_strategy)
def test_behaviouralprogrammm_instantiation_VarType_setter(instance):
    original = instance.VarType
    instance.VarType = original
    assert instance.VarType == original



@given(instance=behaviouralProgramMM_Instantiation_strategy)
def test_behaviouralprogrammm_instantiation_VarName_setter(instance):
    original = instance.VarName
    instance.VarName = original
    assert instance.VarName == original

@given(instance=behaviouralProgramMM_Loop_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_loop_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Loop)

@given(instance=behaviouralProgramMM_RaiseException_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_raiseexception_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_RaiseException)

@given(instance=behaviouralProgramMM_ConditionalBranch_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_conditionalbranch_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_ConditionalBranch)

@given(instance=behaviouralProgramMM_FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_functioncallstatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_FunctionCallStatement)



@given(instance=behaviouralProgramMM_FunctionCallStatement_strategy)
def test_behaviouralprogrammm_functioncallstatement_FuncName_setter(instance):
    original = instance.FuncName
    instance.FuncName = original
    assert instance.FuncName == original

@given(instance=behaviouralProgramMM_Assignment_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_assignment_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Assignment)



@given(instance=behaviouralProgramMM_Assignment_strategy)
def test_behaviouralprogrammm_assignment_VariableName_setter(instance):
    original = instance.VariableName
    instance.VariableName = original
    assert instance.VariableName == original

@given(instance=behaviouralProgramMM_Statement_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_statement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Statement)

@given(instance=behaviouralProgramMM_TryCatch_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_trycatch_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_TryCatch)

@given(instance=behaviouralProgramMM_Return_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_return_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Return)

@given(instance=behaviouralProgramMM_Function_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_function_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Function)



@given(instance=behaviouralProgramMM_Function_strategy)
def test_behaviouralprogrammm_function_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=behaviouralProgramMM_Behaviour_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm_behaviour_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM_Behaviour)
