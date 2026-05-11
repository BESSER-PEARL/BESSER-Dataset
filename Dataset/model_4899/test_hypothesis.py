import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ComparsionOperator,
    behaviouralProgramMM::Equals,
    FunctionCallStatement,
    behaviouralProgramMM::WriteLineStatement,
    behaviouralProgramMM::ReadLineStatement,
    ArithmeticInfixOperator,
    behaviouralProgramMM::Plus,
    BinaryOperator,
    behaviouralProgramMM::ComparsionOperator,
    behaviouralProgramMM::ArithmeticInfixOperator,
    Expression,
    behaviouralProgramMM::ReadLine,
    behaviouralProgramMM::Literal,
    behaviouralProgramMM::BinaryOperator,
    behaviouralProgramMM::Variable,
    behaviouralProgramMM::FunctionCall,
    behaviouralProgramMM::Expression,
    Statement,
    behaviouralProgramMM::ConditionalBranch,
    behaviouralProgramMM::Instantiation,
    behaviouralProgramMM::RaiseException,
    behaviouralProgramMM::FunctionCallStatement,
    behaviouralProgramMM::Loop,
    behaviouralProgramMM::Assignment,
    behaviouralProgramMM::Statement,
    behaviouralProgramMM::TryCatch,
    behaviouralProgramMM::Return,
    behaviouralProgramMM::Function,
    behaviouralProgramMM::Behaviour,
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



def test_behaviouralprogrammm::equals_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Equals)


def test_behaviouralprogrammm::equals_constructor_exists():
    assert callable(behaviouralProgramMM::Equals.__init__)


def test_behaviouralprogrammm::equals_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Equals.__init__)
    params = list(sig.parameters.keys())



def test_functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(FunctionCallStatement)


def test_functioncallstatement_constructor_exists():
    assert callable(FunctionCallStatement.__init__)


def test_functioncallstatement_constructor_args():
    sig = inspect.signature(FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::writelinestatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::WriteLineStatement)


def test_behaviouralprogrammm::writelinestatement_constructor_exists():
    assert callable(behaviouralProgramMM::WriteLineStatement.__init__)


def test_behaviouralprogrammm::writelinestatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::WriteLineStatement.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::readlinestatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::ReadLineStatement)


def test_behaviouralprogrammm::readlinestatement_constructor_exists():
    assert callable(behaviouralProgramMM::ReadLineStatement.__init__)


def test_behaviouralprogrammm::readlinestatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::ReadLineStatement.__init__)
    params = list(sig.parameters.keys())



def test_arithmeticinfixoperator_is_not_abstract():
    assert not inspect.isabstract(ArithmeticInfixOperator)


def test_arithmeticinfixoperator_constructor_exists():
    assert callable(ArithmeticInfixOperator.__init__)


def test_arithmeticinfixoperator_constructor_args():
    sig = inspect.signature(ArithmeticInfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::plus_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Plus)


def test_behaviouralprogrammm::plus_constructor_exists():
    assert callable(behaviouralProgramMM::Plus.__init__)


def test_behaviouralprogrammm::plus_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Plus.__init__)
    params = list(sig.parameters.keys())



def test_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(BinaryOperator)


def test_binaryoperator_constructor_exists():
    assert callable(BinaryOperator.__init__)


def test_binaryoperator_constructor_args():
    sig = inspect.signature(BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::comparsionoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::ComparsionOperator)


def test_behaviouralprogrammm::comparsionoperator_constructor_exists():
    assert callable(behaviouralProgramMM::ComparsionOperator.__init__)


def test_behaviouralprogrammm::comparsionoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::ComparsionOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::arithmeticinfixoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::ArithmeticInfixOperator)


def test_behaviouralprogrammm::arithmeticinfixoperator_constructor_exists():
    assert callable(behaviouralProgramMM::ArithmeticInfixOperator.__init__)


def test_behaviouralprogrammm::arithmeticinfixoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::ArithmeticInfixOperator.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::readline_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::ReadLine)


def test_behaviouralprogrammm::readline_constructor_exists():
    assert callable(behaviouralProgramMM::ReadLine.__init__)


def test_behaviouralprogrammm::readline_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::ReadLine.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::literal_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Literal)


def test_behaviouralprogrammm::literal_constructor_exists():
    assert callable(behaviouralProgramMM::Literal.__init__)


def test_behaviouralprogrammm::literal_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_behaviouralprogrammm::literal_has_Value():
    assert hasattr(behaviouralProgramMM::Literal, "Value")
    descriptor = None
    for klass in behaviouralProgramMM::Literal.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::BinaryOperator)


def test_behaviouralprogrammm::binaryoperator_constructor_exists():
    assert callable(behaviouralProgramMM::BinaryOperator.__init__)


def test_behaviouralprogrammm::binaryoperator_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::BinaryOperator.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::variable_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Variable)


def test_behaviouralprogrammm::variable_constructor_exists():
    assert callable(behaviouralProgramMM::Variable.__init__)


def test_behaviouralprogrammm::variable_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "VarName" in params, "Missing parameter 'VarName'"

def test_behaviouralprogrammm::variable_has_VarName():
    assert hasattr(behaviouralProgramMM::Variable, "VarName")
    descriptor = None
    for klass in behaviouralProgramMM::Variable.__mro__:
        if "VarName" in klass.__dict__:
            descriptor = klass.__dict__["VarName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm::functioncall_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::FunctionCall)


def test_behaviouralprogrammm::functioncall_constructor_exists():
    assert callable(behaviouralProgramMM::FunctionCall.__init__)


def test_behaviouralprogrammm::functioncall_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::FunctionCall.__init__)
    params = list(sig.parameters.keys())
    assert "FuncName" in params, "Missing parameter 'FuncName'"

def test_behaviouralprogrammm::functioncall_has_FuncName():
    assert hasattr(behaviouralProgramMM::FunctionCall, "FuncName")
    descriptor = None
    for klass in behaviouralProgramMM::FunctionCall.__mro__:
        if "FuncName" in klass.__dict__:
            descriptor = klass.__dict__["FuncName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm::expression_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Expression)


def test_behaviouralprogrammm::expression_constructor_exists():
    assert callable(behaviouralProgramMM::Expression.__init__)


def test_behaviouralprogrammm::expression_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Expression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::conditionalbranch_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::ConditionalBranch)


def test_behaviouralprogrammm::conditionalbranch_constructor_exists():
    assert callable(behaviouralProgramMM::ConditionalBranch.__init__)


def test_behaviouralprogrammm::conditionalbranch_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::ConditionalBranch.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::instantiation_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Instantiation)


def test_behaviouralprogrammm::instantiation_constructor_exists():
    assert callable(behaviouralProgramMM::Instantiation.__init__)


def test_behaviouralprogrammm::instantiation_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Instantiation.__init__)
    params = list(sig.parameters.keys())
    assert "VarType" in params, "Missing parameter 'VarType'"
    assert "VarName" in params, "Missing parameter 'VarName'"

def test_behaviouralprogrammm::instantiation_has_VarType():
    assert hasattr(behaviouralProgramMM::Instantiation, "VarType")
    descriptor = None
    for klass in behaviouralProgramMM::Instantiation.__mro__:
        if "VarType" in klass.__dict__:
            descriptor = klass.__dict__["VarType"]
            break
    assert isinstance(descriptor, property)

def test_behaviouralprogrammm::instantiation_has_VarName():
    assert hasattr(behaviouralProgramMM::Instantiation, "VarName")
    descriptor = None
    for klass in behaviouralProgramMM::Instantiation.__mro__:
        if "VarName" in klass.__dict__:
            descriptor = klass.__dict__["VarName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm::raiseexception_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::RaiseException)


def test_behaviouralprogrammm::raiseexception_constructor_exists():
    assert callable(behaviouralProgramMM::RaiseException.__init__)


def test_behaviouralprogrammm::raiseexception_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::RaiseException.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::functioncallstatement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::FunctionCallStatement)


def test_behaviouralprogrammm::functioncallstatement_constructor_exists():
    assert callable(behaviouralProgramMM::FunctionCallStatement.__init__)


def test_behaviouralprogrammm::functioncallstatement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::FunctionCallStatement.__init__)
    params = list(sig.parameters.keys())
    assert "FuncName" in params, "Missing parameter 'FuncName'"

def test_behaviouralprogrammm::functioncallstatement_has_FuncName():
    assert hasattr(behaviouralProgramMM::FunctionCallStatement, "FuncName")
    descriptor = None
    for klass in behaviouralProgramMM::FunctionCallStatement.__mro__:
        if "FuncName" in klass.__dict__:
            descriptor = klass.__dict__["FuncName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm::loop_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Loop)


def test_behaviouralprogrammm::loop_constructor_exists():
    assert callable(behaviouralProgramMM::Loop.__init__)


def test_behaviouralprogrammm::loop_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Loop.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::assignment_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Assignment)


def test_behaviouralprogrammm::assignment_constructor_exists():
    assert callable(behaviouralProgramMM::Assignment.__init__)


def test_behaviouralprogrammm::assignment_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Assignment.__init__)
    params = list(sig.parameters.keys())
    assert "VariableName" in params, "Missing parameter 'VariableName'"

def test_behaviouralprogrammm::assignment_has_VariableName():
    assert hasattr(behaviouralProgramMM::Assignment, "VariableName")
    descriptor = None
    for klass in behaviouralProgramMM::Assignment.__mro__:
        if "VariableName" in klass.__dict__:
            descriptor = klass.__dict__["VariableName"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm::statement_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Statement)


def test_behaviouralprogrammm::statement_constructor_exists():
    assert callable(behaviouralProgramMM::Statement.__init__)


def test_behaviouralprogrammm::statement_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Statement.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::trycatch_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::TryCatch)


def test_behaviouralprogrammm::trycatch_constructor_exists():
    assert callable(behaviouralProgramMM::TryCatch.__init__)


def test_behaviouralprogrammm::trycatch_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::TryCatch.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::return_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Return)


def test_behaviouralprogrammm::return_constructor_exists():
    assert callable(behaviouralProgramMM::Return.__init__)


def test_behaviouralprogrammm::return_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Return.__init__)
    params = list(sig.parameters.keys())



def test_behaviouralprogrammm::function_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Function)


def test_behaviouralprogrammm::function_constructor_exists():
    assert callable(behaviouralProgramMM::Function.__init__)


def test_behaviouralprogrammm::function_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Function.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_behaviouralprogrammm::function_has_Name():
    assert hasattr(behaviouralProgramMM::Function, "Name")
    descriptor = None
    for klass in behaviouralProgramMM::Function.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_behaviouralprogrammm::behaviour_is_not_abstract():
    assert not inspect.isabstract(behaviouralProgramMM::Behaviour)


def test_behaviouralprogrammm::behaviour_constructor_exists():
    assert callable(behaviouralProgramMM::Behaviour.__init__)


def test_behaviouralprogrammm::behaviour_constructor_args():
    sig = inspect.signature(behaviouralProgramMM::Behaviour.__init__)
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
behaviouralProgramMM::Equals_strategy = st.builds(
    behaviouralProgramMM::Equals,
)
FunctionCallStatement_strategy = st.builds(
    FunctionCallStatement,
)
behaviouralProgramMM::WriteLineStatement_strategy = st.builds(
    behaviouralProgramMM::WriteLineStatement,
)
behaviouralProgramMM::ReadLineStatement_strategy = st.builds(
    behaviouralProgramMM::ReadLineStatement,
)
ArithmeticInfixOperator_strategy = st.builds(
    ArithmeticInfixOperator,
)
behaviouralProgramMM::Plus_strategy = st.builds(
    behaviouralProgramMM::Plus,
)
BinaryOperator_strategy = st.builds(
    BinaryOperator,
)
behaviouralProgramMM::ComparsionOperator_strategy = st.builds(
    behaviouralProgramMM::ComparsionOperator,
)
behaviouralProgramMM::ArithmeticInfixOperator_strategy = st.builds(
    behaviouralProgramMM::ArithmeticInfixOperator,
)
Expression_strategy = st.builds(
    Expression,
)
behaviouralProgramMM::ReadLine_strategy = st.builds(
    behaviouralProgramMM::ReadLine,
)
behaviouralProgramMM::Literal_strategy = st.builds(
    behaviouralProgramMM::Literal,
    Value=
        safe_text
)
behaviouralProgramMM::BinaryOperator_strategy = st.builds(
    behaviouralProgramMM::BinaryOperator,
)
behaviouralProgramMM::Variable_strategy = st.builds(
    behaviouralProgramMM::Variable,
    VarName=
        safe_text
)
behaviouralProgramMM::FunctionCall_strategy = st.builds(
    behaviouralProgramMM::FunctionCall,
    FuncName=
        safe_text
)
behaviouralProgramMM::Expression_strategy = st.builds(
    behaviouralProgramMM::Expression,
)
Statement_strategy = st.builds(
    Statement,
)
behaviouralProgramMM::ConditionalBranch_strategy = st.builds(
    behaviouralProgramMM::ConditionalBranch,
)
behaviouralProgramMM::Instantiation_strategy = st.builds(
    behaviouralProgramMM::Instantiation,
    VarType=
        safe_text,
    VarName=
        safe_text
)
behaviouralProgramMM::RaiseException_strategy = st.builds(
    behaviouralProgramMM::RaiseException,
)
behaviouralProgramMM::FunctionCallStatement_strategy = st.builds(
    behaviouralProgramMM::FunctionCallStatement,
    FuncName=
        safe_text
)
behaviouralProgramMM::Loop_strategy = st.builds(
    behaviouralProgramMM::Loop,
)
behaviouralProgramMM::Assignment_strategy = st.builds(
    behaviouralProgramMM::Assignment,
    VariableName=
        safe_text
)
behaviouralProgramMM::Statement_strategy = st.builds(
    behaviouralProgramMM::Statement,
)
behaviouralProgramMM::TryCatch_strategy = st.builds(
    behaviouralProgramMM::TryCatch,
)
behaviouralProgramMM::Return_strategy = st.builds(
    behaviouralProgramMM::Return,
)
behaviouralProgramMM::Function_strategy = st.builds(
    behaviouralProgramMM::Function,
    Name=
        safe_text
)
behaviouralProgramMM::Behaviour_strategy = st.builds(
    behaviouralProgramMM::Behaviour,
)

@given(instance=ComparsionOperator_strategy)
@settings(max_examples=50)
def test_comparsionoperator_instantiation(instance):
    assert isinstance(instance, ComparsionOperator)

@given(instance=behaviouralProgramMM::Equals_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::equals_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Equals)

@given(instance=FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_functioncallstatement_instantiation(instance):
    assert isinstance(instance, FunctionCallStatement)

@given(instance=behaviouralProgramMM::WriteLineStatement_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::writelinestatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::WriteLineStatement)

@given(instance=behaviouralProgramMM::ReadLineStatement_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::readlinestatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::ReadLineStatement)

@given(instance=ArithmeticInfixOperator_strategy)
@settings(max_examples=50)
def test_arithmeticinfixoperator_instantiation(instance):
    assert isinstance(instance, ArithmeticInfixOperator)

@given(instance=behaviouralProgramMM::Plus_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::plus_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Plus)

@given(instance=BinaryOperator_strategy)
@settings(max_examples=50)
def test_binaryoperator_instantiation(instance):
    assert isinstance(instance, BinaryOperator)

@given(instance=behaviouralProgramMM::ComparsionOperator_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::comparsionoperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::ComparsionOperator)

@given(instance=behaviouralProgramMM::ArithmeticInfixOperator_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::arithmeticinfixoperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::ArithmeticInfixOperator)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=behaviouralProgramMM::ReadLine_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::readline_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::ReadLine)

@given(instance=behaviouralProgramMM::Literal_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::literal_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Literal)

@given(instance=behaviouralProgramMM::Literal_strategy)
def test_behaviouralprogrammm::literal_Value_type(instance):
    assert isinstance(instance.Value, str)


@given(instance=behaviouralProgramMM::Literal_strategy)
def test_behaviouralprogrammm::literal_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=behaviouralProgramMM::BinaryOperator_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::binaryoperator_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::BinaryOperator)

@given(instance=behaviouralProgramMM::Variable_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::variable_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Variable)

@given(instance=behaviouralProgramMM::Variable_strategy)
def test_behaviouralprogrammm::variable_VarName_type(instance):
    assert isinstance(instance.VarName, str)


@given(instance=behaviouralProgramMM::Variable_strategy)
def test_behaviouralprogrammm::variable_VarName_setter(instance):
    original = instance.VarName
    instance.VarName = original
    assert instance.VarName == original

@given(instance=behaviouralProgramMM::FunctionCall_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::functioncall_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::FunctionCall)

@given(instance=behaviouralProgramMM::FunctionCall_strategy)
def test_behaviouralprogrammm::functioncall_FuncName_type(instance):
    assert isinstance(instance.FuncName, str)


@given(instance=behaviouralProgramMM::FunctionCall_strategy)
def test_behaviouralprogrammm::functioncall_FuncName_setter(instance):
    original = instance.FuncName
    instance.FuncName = original
    assert instance.FuncName == original

@given(instance=behaviouralProgramMM::Expression_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::expression_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Expression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=behaviouralProgramMM::ConditionalBranch_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::conditionalbranch_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::ConditionalBranch)

@given(instance=behaviouralProgramMM::Instantiation_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::instantiation_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Instantiation)

@given(instance=behaviouralProgramMM::Instantiation_strategy)
def test_behaviouralprogrammm::instantiation_VarType_type(instance):
    assert isinstance(instance.VarType, str)


@given(instance=behaviouralProgramMM::Instantiation_strategy)
def test_behaviouralprogrammm::instantiation_VarType_setter(instance):
    original = instance.VarType
    instance.VarType = original
    assert instance.VarType == original

@given(instance=behaviouralProgramMM::Instantiation_strategy)
def test_behaviouralprogrammm::instantiation_VarName_type(instance):
    assert isinstance(instance.VarName, str)


@given(instance=behaviouralProgramMM::Instantiation_strategy)
def test_behaviouralprogrammm::instantiation_VarName_setter(instance):
    original = instance.VarName
    instance.VarName = original
    assert instance.VarName == original

@given(instance=behaviouralProgramMM::RaiseException_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::raiseexception_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::RaiseException)

@given(instance=behaviouralProgramMM::FunctionCallStatement_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::functioncallstatement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::FunctionCallStatement)

@given(instance=behaviouralProgramMM::FunctionCallStatement_strategy)
def test_behaviouralprogrammm::functioncallstatement_FuncName_type(instance):
    assert isinstance(instance.FuncName, str)


@given(instance=behaviouralProgramMM::FunctionCallStatement_strategy)
def test_behaviouralprogrammm::functioncallstatement_FuncName_setter(instance):
    original = instance.FuncName
    instance.FuncName = original
    assert instance.FuncName == original

@given(instance=behaviouralProgramMM::Loop_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::loop_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Loop)

@given(instance=behaviouralProgramMM::Assignment_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::assignment_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Assignment)

@given(instance=behaviouralProgramMM::Assignment_strategy)
def test_behaviouralprogrammm::assignment_VariableName_type(instance):
    assert isinstance(instance.VariableName, str)


@given(instance=behaviouralProgramMM::Assignment_strategy)
def test_behaviouralprogrammm::assignment_VariableName_setter(instance):
    original = instance.VariableName
    instance.VariableName = original
    assert instance.VariableName == original

@given(instance=behaviouralProgramMM::Statement_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::statement_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Statement)

@given(instance=behaviouralProgramMM::TryCatch_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::trycatch_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::TryCatch)

@given(instance=behaviouralProgramMM::Return_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::return_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Return)

@given(instance=behaviouralProgramMM::Function_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::function_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Function)

@given(instance=behaviouralProgramMM::Function_strategy)
def test_behaviouralprogrammm::function_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=behaviouralProgramMM::Function_strategy)
def test_behaviouralprogrammm::function_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=behaviouralProgramMM::Behaviour_strategy)
@settings(max_examples=50)
def test_behaviouralprogrammm::behaviour_instantiation(instance):
    assert isinstance(instance, behaviouralProgramMM::Behaviour)
