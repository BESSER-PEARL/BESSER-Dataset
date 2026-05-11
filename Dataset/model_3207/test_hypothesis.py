import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    NQC::Case,
    CallStatement,
    NQC::SubroutineCall,
    NQC::FunctionCall,
    CompoundExpression,
    NQC::BinaryExpression,
    ConstantExpression,
    NQC::BooleanConstant,
    VariableExpression,
    NQC::ArrayExpression,
    ValueExpression,
    Expression,
    NQC::CompoundExpression,
    NQC::ValueExpression,
    NQC::VariableExpression,
    Statement,
    NQC::ControlStructure,
    NQC::EmptyStatement,
    NQC::ContinueStatement,
    NQC::CallStatement,
    NQC::BreakStatement,
    NQC::BlockStatement,
    NQC::Expression,
    NQC::AssignmentStatement,
    ControlStructure,
    NQC::RepeatStatement,
    NQC::WhileStatement,
    NQC::ForStatement,
    NQC::IfStatement,
    NQC::GoToStatement,
    NQC::UntilStatement,
    NQC::SwitchStatement,
    NQC::DoWhileStatement,
    NQC::StopStatement,
    NQC::StartStatement,
    NQC::ReturnStatement,
    NQC::Subroutine,
    NQC::Function,
    NQC::Task,
    NQC::Program,
    NQC::Label,
    NQC::IntegerConstant,
    NQC::ConstantExpression,
    NQC::Variable,
    Variable,
    NQC::GlobalVariable,
    NQC::Parameter,
    NQC::LocalVariable,
    NQC::Statement,
    AssignmentStatementEnum,
    TypeEnum,
    BinaryOperatorEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_nqc::case_is_not_abstract():
    assert not inspect.isabstract(NQC::Case)


def test_nqc::case_constructor_exists():
    assert callable(NQC::Case.__init__)


def test_nqc::case_constructor_args():
    sig = inspect.signature(NQC::Case.__init__)
    params = list(sig.parameters.keys())
    assert "IsDefault" in params, "Missing parameter 'IsDefault'"

def test_nqc::case_has_IsDefault():
    assert hasattr(NQC::Case, "IsDefault")
    descriptor = None
    for klass in NQC::Case.__mro__:
        if "IsDefault" in klass.__dict__:
            descriptor = klass.__dict__["IsDefault"]
            break
    assert isinstance(descriptor, property)



def test_callstatement_is_not_abstract():
    assert not inspect.isabstract(CallStatement)


def test_callstatement_constructor_exists():
    assert callable(CallStatement.__init__)


def test_callstatement_constructor_args():
    sig = inspect.signature(CallStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::subroutinecall_is_not_abstract():
    assert not inspect.isabstract(NQC::SubroutineCall)


def test_nqc::subroutinecall_constructor_exists():
    assert callable(NQC::SubroutineCall.__init__)


def test_nqc::subroutinecall_constructor_args():
    sig = inspect.signature(NQC::SubroutineCall.__init__)
    params = list(sig.parameters.keys())



def test_nqc::functioncall_is_not_abstract():
    assert not inspect.isabstract(NQC::FunctionCall)


def test_nqc::functioncall_constructor_exists():
    assert callable(NQC::FunctionCall.__init__)


def test_nqc::functioncall_constructor_args():
    sig = inspect.signature(NQC::FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_compoundexpression_is_not_abstract():
    assert not inspect.isabstract(CompoundExpression)


def test_compoundexpression_constructor_exists():
    assert callable(CompoundExpression.__init__)


def test_compoundexpression_constructor_args():
    sig = inspect.signature(CompoundExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc::binaryexpression_is_not_abstract():
    assert not inspect.isabstract(NQC::BinaryExpression)


def test_nqc::binaryexpression_constructor_exists():
    assert callable(NQC::BinaryExpression.__init__)


def test_nqc::binaryexpression_constructor_args():
    sig = inspect.signature(NQC::BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "Operator" in params, "Missing parameter 'Operator'"

def test_nqc::binaryexpression_has_Operator():
    assert hasattr(NQC::BinaryExpression, "Operator")
    descriptor = None
    for klass in NQC::BinaryExpression.__mro__:
        if "Operator" in klass.__dict__:
            descriptor = klass.__dict__["Operator"]
            break
    assert isinstance(descriptor, property)



def test_constantexpression_is_not_abstract():
    assert not inspect.isabstract(ConstantExpression)


def test_constantexpression_constructor_exists():
    assert callable(ConstantExpression.__init__)


def test_constantexpression_constructor_args():
    sig = inspect.signature(ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc::booleanconstant_is_not_abstract():
    assert not inspect.isabstract(NQC::BooleanConstant)


def test_nqc::booleanconstant_constructor_exists():
    assert callable(NQC::BooleanConstant.__init__)


def test_nqc::booleanconstant_constructor_args():
    sig = inspect.signature(NQC::BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_nqc::booleanconstant_has_Value():
    assert hasattr(NQC::BooleanConstant, "Value")
    descriptor = None
    for klass in NQC::BooleanConstant.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_variableexpression_is_not_abstract():
    assert not inspect.isabstract(VariableExpression)


def test_variableexpression_constructor_exists():
    assert callable(VariableExpression.__init__)


def test_variableexpression_constructor_args():
    sig = inspect.signature(VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc::arrayexpression_is_not_abstract():
    assert not inspect.isabstract(NQC::ArrayExpression)


def test_nqc::arrayexpression_constructor_exists():
    assert callable(NQC::ArrayExpression.__init__)


def test_nqc::arrayexpression_constructor_args():
    sig = inspect.signature(NQC::ArrayExpression.__init__)
    params = list(sig.parameters.keys())



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_nqc::compoundexpression_is_not_abstract():
    assert not inspect.isabstract(NQC::CompoundExpression)


def test_nqc::compoundexpression_constructor_exists():
    assert callable(NQC::CompoundExpression.__init__)


def test_nqc::compoundexpression_constructor_args():
    sig = inspect.signature(NQC::CompoundExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc::valueexpression_is_not_abstract():
    assert not inspect.isabstract(NQC::ValueExpression)


def test_nqc::valueexpression_constructor_exists():
    assert callable(NQC::ValueExpression.__init__)


def test_nqc::valueexpression_constructor_args():
    sig = inspect.signature(NQC::ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc::variableexpression_is_not_abstract():
    assert not inspect.isabstract(NQC::VariableExpression)


def test_nqc::variableexpression_constructor_exists():
    assert callable(NQC::VariableExpression.__init__)


def test_nqc::variableexpression_constructor_args():
    sig = inspect.signature(NQC::VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::controlstructure_is_not_abstract():
    assert not inspect.isabstract(NQC::ControlStructure)


def test_nqc::controlstructure_constructor_exists():
    assert callable(NQC::ControlStructure.__init__)


def test_nqc::controlstructure_constructor_args():
    sig = inspect.signature(NQC::ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_nqc::emptystatement_is_not_abstract():
    assert not inspect.isabstract(NQC::EmptyStatement)


def test_nqc::emptystatement_constructor_exists():
    assert callable(NQC::EmptyStatement.__init__)


def test_nqc::emptystatement_constructor_args():
    sig = inspect.signature(NQC::EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::continuestatement_is_not_abstract():
    assert not inspect.isabstract(NQC::ContinueStatement)


def test_nqc::continuestatement_constructor_exists():
    assert callable(NQC::ContinueStatement.__init__)


def test_nqc::continuestatement_constructor_args():
    sig = inspect.signature(NQC::ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::callstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::CallStatement)


def test_nqc::callstatement_constructor_exists():
    assert callable(NQC::CallStatement.__init__)


def test_nqc::callstatement_constructor_args():
    sig = inspect.signature(NQC::CallStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::breakstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::BreakStatement)


def test_nqc::breakstatement_constructor_exists():
    assert callable(NQC::BreakStatement.__init__)


def test_nqc::breakstatement_constructor_args():
    sig = inspect.signature(NQC::BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::blockstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::BlockStatement)


def test_nqc::blockstatement_constructor_exists():
    assert callable(NQC::BlockStatement.__init__)


def test_nqc::blockstatement_constructor_args():
    sig = inspect.signature(NQC::BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::expression_is_not_abstract():
    assert not inspect.isabstract(NQC::Expression)


def test_nqc::expression_constructor_exists():
    assert callable(NQC::Expression.__init__)


def test_nqc::expression_constructor_args():
    sig = inspect.signature(NQC::Expression.__init__)
    params = list(sig.parameters.keys())



def test_nqc::assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::AssignmentStatement)


def test_nqc::assignmentstatement_constructor_exists():
    assert callable(NQC::AssignmentStatement.__init__)


def test_nqc::assignmentstatement_constructor_args():
    sig = inspect.signature(NQC::AssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "Operator" in params, "Missing parameter 'Operator'"

def test_nqc::assignmentstatement_has_Operator():
    assert hasattr(NQC::AssignmentStatement, "Operator")
    descriptor = None
    for klass in NQC::AssignmentStatement.__mro__:
        if "Operator" in klass.__dict__:
            descriptor = klass.__dict__["Operator"]
            break
    assert isinstance(descriptor, property)



def test_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_nqc::repeatstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::RepeatStatement)


def test_nqc::repeatstatement_constructor_exists():
    assert callable(NQC::RepeatStatement.__init__)


def test_nqc::repeatstatement_constructor_args():
    sig = inspect.signature(NQC::RepeatStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::whilestatement_is_not_abstract():
    assert not inspect.isabstract(NQC::WhileStatement)


def test_nqc::whilestatement_constructor_exists():
    assert callable(NQC::WhileStatement.__init__)


def test_nqc::whilestatement_constructor_args():
    sig = inspect.signature(NQC::WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::forstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::ForStatement)


def test_nqc::forstatement_constructor_exists():
    assert callable(NQC::ForStatement.__init__)


def test_nqc::forstatement_constructor_args():
    sig = inspect.signature(NQC::ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::ifstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::IfStatement)


def test_nqc::ifstatement_constructor_exists():
    assert callable(NQC::IfStatement.__init__)


def test_nqc::ifstatement_constructor_args():
    sig = inspect.signature(NQC::IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::gotostatement_is_not_abstract():
    assert not inspect.isabstract(NQC::GoToStatement)


def test_nqc::gotostatement_constructor_exists():
    assert callable(NQC::GoToStatement.__init__)


def test_nqc::gotostatement_constructor_args():
    sig = inspect.signature(NQC::GoToStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::untilstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::UntilStatement)


def test_nqc::untilstatement_constructor_exists():
    assert callable(NQC::UntilStatement.__init__)


def test_nqc::untilstatement_constructor_args():
    sig = inspect.signature(NQC::UntilStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::switchstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::SwitchStatement)


def test_nqc::switchstatement_constructor_exists():
    assert callable(NQC::SwitchStatement.__init__)


def test_nqc::switchstatement_constructor_args():
    sig = inspect.signature(NQC::SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(NQC::DoWhileStatement)


def test_nqc::dowhilestatement_constructor_exists():
    assert callable(NQC::DoWhileStatement.__init__)


def test_nqc::dowhilestatement_constructor_args():
    sig = inspect.signature(NQC::DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::stopstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::StopStatement)


def test_nqc::stopstatement_constructor_exists():
    assert callable(NQC::StopStatement.__init__)


def test_nqc::stopstatement_constructor_args():
    sig = inspect.signature(NQC::StopStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::startstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::StartStatement)


def test_nqc::startstatement_constructor_exists():
    assert callable(NQC::StartStatement.__init__)


def test_nqc::startstatement_constructor_args():
    sig = inspect.signature(NQC::StartStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::returnstatement_is_not_abstract():
    assert not inspect.isabstract(NQC::ReturnStatement)


def test_nqc::returnstatement_constructor_exists():
    assert callable(NQC::ReturnStatement.__init__)


def test_nqc::returnstatement_constructor_args():
    sig = inspect.signature(NQC::ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc::subroutine_is_not_abstract():
    assert not inspect.isabstract(NQC::Subroutine)


def test_nqc::subroutine_constructor_exists():
    assert callable(NQC::Subroutine.__init__)


def test_nqc::subroutine_constructor_args():
    sig = inspect.signature(NQC::Subroutine.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc::subroutine_has_Name():
    assert hasattr(NQC::Subroutine, "Name")
    descriptor = None
    for klass in NQC::Subroutine.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_nqc::function_is_not_abstract():
    assert not inspect.isabstract(NQC::Function)


def test_nqc::function_constructor_exists():
    assert callable(NQC::Function.__init__)


def test_nqc::function_constructor_args():
    sig = inspect.signature(NQC::Function.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc::function_has_Name():
    assert hasattr(NQC::Function, "Name")
    descriptor = None
    for klass in NQC::Function.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_nqc::task_is_not_abstract():
    assert not inspect.isabstract(NQC::Task)


def test_nqc::task_constructor_exists():
    assert callable(NQC::Task.__init__)


def test_nqc::task_constructor_args():
    sig = inspect.signature(NQC::Task.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc::task_has_Name():
    assert hasattr(NQC::Task, "Name")
    descriptor = None
    for klass in NQC::Task.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_nqc::program_is_not_abstract():
    assert not inspect.isabstract(NQC::Program)


def test_nqc::program_constructor_exists():
    assert callable(NQC::Program.__init__)


def test_nqc::program_constructor_args():
    sig = inspect.signature(NQC::Program.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc::program_has_Name():
    assert hasattr(NQC::Program, "Name")
    descriptor = None
    for klass in NQC::Program.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_nqc::label_is_not_abstract():
    assert not inspect.isabstract(NQC::Label)


def test_nqc::label_constructor_exists():
    assert callable(NQC::Label.__init__)


def test_nqc::label_constructor_args():
    sig = inspect.signature(NQC::Label.__init__)
    params = list(sig.parameters.keys())
    assert "Label" in params, "Missing parameter 'Label'"

def test_nqc::label_has_Label():
    assert hasattr(NQC::Label, "Label")
    descriptor = None
    for klass in NQC::Label.__mro__:
        if "Label" in klass.__dict__:
            descriptor = klass.__dict__["Label"]
            break
    assert isinstance(descriptor, property)



def test_nqc::integerconstant_is_not_abstract():
    assert not inspect.isabstract(NQC::IntegerConstant)


def test_nqc::integerconstant_constructor_exists():
    assert callable(NQC::IntegerConstant.__init__)


def test_nqc::integerconstant_constructor_args():
    sig = inspect.signature(NQC::IntegerConstant.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_nqc::integerconstant_has_Value():
    assert hasattr(NQC::IntegerConstant, "Value")
    descriptor = None
    for klass in NQC::IntegerConstant.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_nqc::constantexpression_is_not_abstract():
    assert not inspect.isabstract(NQC::ConstantExpression)


def test_nqc::constantexpression_constructor_exists():
    assert callable(NQC::ConstantExpression.__init__)


def test_nqc::constantexpression_constructor_args():
    sig = inspect.signature(NQC::ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc::variable_is_not_abstract():
    assert not inspect.isabstract(NQC::Variable)


def test_nqc::variable_constructor_exists():
    assert callable(NQC::Variable.__init__)


def test_nqc::variable_constructor_args():
    sig = inspect.signature(NQC::Variable.__init__)
    params = list(sig.parameters.keys())
    assert "Type" in params, "Missing parameter 'Type'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc::variable_has_Type():
    assert hasattr(NQC::Variable, "Type")
    descriptor = None
    for klass in NQC::Variable.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)

def test_nqc::variable_has_Name():
    assert hasattr(NQC::Variable, "Name")
    descriptor = None
    for klass in NQC::Variable.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_nqc::globalvariable_is_not_abstract():
    assert not inspect.isabstract(NQC::GlobalVariable)


def test_nqc::globalvariable_constructor_exists():
    assert callable(NQC::GlobalVariable.__init__)


def test_nqc::globalvariable_constructor_args():
    sig = inspect.signature(NQC::GlobalVariable.__init__)
    params = list(sig.parameters.keys())



def test_nqc::parameter_is_not_abstract():
    assert not inspect.isabstract(NQC::Parameter)


def test_nqc::parameter_constructor_exists():
    assert callable(NQC::Parameter.__init__)


def test_nqc::parameter_constructor_args():
    sig = inspect.signature(NQC::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_nqc::localvariable_is_not_abstract():
    assert not inspect.isabstract(NQC::LocalVariable)


def test_nqc::localvariable_constructor_exists():
    assert callable(NQC::LocalVariable.__init__)


def test_nqc::localvariable_constructor_args():
    sig = inspect.signature(NQC::LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_nqc::statement_is_not_abstract():
    assert not inspect.isabstract(NQC::Statement)


def test_nqc::statement_constructor_exists():
    assert callable(NQC::Statement.__init__)


def test_nqc::statement_constructor_args():
    sig = inspect.signature(NQC::Statement.__init__)
    params = list(sig.parameters.keys())

def test_assignmentstatementenum_exists():
    # Check that the Enumeration exists
    assert AssignmentStatementEnum is not None

def test_assignmentstatementenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in AssignmentStatementEnum]
    expected_literals = [
        "assign",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in AssignmentStatementEnum"

def test_typeenum_exists():
    # Check that the Enumeration exists
    assert TypeEnum is not None

def test_typeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TypeEnum]
    expected_literals = [
        "Integer",
        "IntegerArray",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TypeEnum"

def test_binaryoperatorenum_exists():
    # Check that the Enumeration exists
    assert BinaryOperatorEnum is not None

def test_binaryoperatorenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperatorEnum]
    expected_literals = [
        "equal",
        "leq",
        "greater",
        "bitor",
        "minus",
        "plus",
        "less",
        "div",
        "geq",
        "times",
        "mod",
        "and_",
        "or_",
        "bitand",
        "notequal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperatorEnum"


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
NQC::Case_strategy = st.builds(
    NQC::Case,
    IsDefault=
        st.booleans()
)
CallStatement_strategy = st.builds(
    CallStatement,
)
NQC::SubroutineCall_strategy = st.builds(
    NQC::SubroutineCall,
)
NQC::FunctionCall_strategy = st.builds(
    NQC::FunctionCall,
)
CompoundExpression_strategy = st.builds(
    CompoundExpression,
)
NQC::BinaryExpression_strategy = st.builds(
    NQC::BinaryExpression,
    Operator=
        safe_text
)
ConstantExpression_strategy = st.builds(
    ConstantExpression,
)
NQC::BooleanConstant_strategy = st.builds(
    NQC::BooleanConstant,
    Value=
        st.booleans()
)
VariableExpression_strategy = st.builds(
    VariableExpression,
)
NQC::ArrayExpression_strategy = st.builds(
    NQC::ArrayExpression,
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
Expression_strategy = st.builds(
    Expression,
)
NQC::CompoundExpression_strategy = st.builds(
    NQC::CompoundExpression,
)
NQC::ValueExpression_strategy = st.builds(
    NQC::ValueExpression,
)
NQC::VariableExpression_strategy = st.builds(
    NQC::VariableExpression,
)
Statement_strategy = st.builds(
    Statement,
)
NQC::ControlStructure_strategy = st.builds(
    NQC::ControlStructure,
)
NQC::EmptyStatement_strategy = st.builds(
    NQC::EmptyStatement,
)
NQC::ContinueStatement_strategy = st.builds(
    NQC::ContinueStatement,
)
NQC::CallStatement_strategy = st.builds(
    NQC::CallStatement,
)
NQC::BreakStatement_strategy = st.builds(
    NQC::BreakStatement,
)
NQC::BlockStatement_strategy = st.builds(
    NQC::BlockStatement,
)
NQC::Expression_strategy = st.builds(
    NQC::Expression,
)
NQC::AssignmentStatement_strategy = st.builds(
    NQC::AssignmentStatement,
    Operator=
        safe_text
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
NQC::RepeatStatement_strategy = st.builds(
    NQC::RepeatStatement,
)
NQC::WhileStatement_strategy = st.builds(
    NQC::WhileStatement,
)
NQC::ForStatement_strategy = st.builds(
    NQC::ForStatement,
)
NQC::IfStatement_strategy = st.builds(
    NQC::IfStatement,
)
NQC::GoToStatement_strategy = st.builds(
    NQC::GoToStatement,
)
NQC::UntilStatement_strategy = st.builds(
    NQC::UntilStatement,
)
NQC::SwitchStatement_strategy = st.builds(
    NQC::SwitchStatement,
)
NQC::DoWhileStatement_strategy = st.builds(
    NQC::DoWhileStatement,
)
NQC::StopStatement_strategy = st.builds(
    NQC::StopStatement,
)
NQC::StartStatement_strategy = st.builds(
    NQC::StartStatement,
)
NQC::ReturnStatement_strategy = st.builds(
    NQC::ReturnStatement,
)
NQC::Subroutine_strategy = st.builds(
    NQC::Subroutine,
    Name=
        safe_text
)
NQC::Function_strategy = st.builds(
    NQC::Function,
    Name=
        safe_text
)
NQC::Task_strategy = st.builds(
    NQC::Task,
    Name=
        safe_text
)
NQC::Program_strategy = st.builds(
    NQC::Program,
    Name=
        safe_text
)
NQC::Label_strategy = st.builds(
    NQC::Label,
    Label=
        safe_text
)
NQC::IntegerConstant_strategy = st.builds(
    NQC::IntegerConstant,
    Value=
        st.integers()
)
NQC::ConstantExpression_strategy = st.builds(
    NQC::ConstantExpression,
)
NQC::Variable_strategy = st.builds(
    NQC::Variable,
    Type=
        safe_text,
    Name=
        safe_text
)
Variable_strategy = st.builds(
    Variable,
)
NQC::GlobalVariable_strategy = st.builds(
    NQC::GlobalVariable,
)
NQC::Parameter_strategy = st.builds(
    NQC::Parameter,
)
NQC::LocalVariable_strategy = st.builds(
    NQC::LocalVariable,
)
NQC::Statement_strategy = st.builds(
    NQC::Statement,
)

@given(instance=NQC::Case_strategy)
@settings(max_examples=50)
def test_nqc::case_instantiation(instance):
    assert isinstance(instance, NQC::Case)

@given(instance=NQC::Case_strategy)
def test_nqc::case_IsDefault_type(instance):
    assert isinstance(instance.IsDefault, bool)


@given(instance=NQC::Case_strategy)
def test_nqc::case_IsDefault_setter(instance):
    original = instance.IsDefault
    instance.IsDefault = original
    assert instance.IsDefault == original

@given(instance=CallStatement_strategy)
@settings(max_examples=50)
def test_callstatement_instantiation(instance):
    assert isinstance(instance, CallStatement)

@given(instance=NQC::SubroutineCall_strategy)
@settings(max_examples=50)
def test_nqc::subroutinecall_instantiation(instance):
    assert isinstance(instance, NQC::SubroutineCall)

@given(instance=NQC::FunctionCall_strategy)
@settings(max_examples=50)
def test_nqc::functioncall_instantiation(instance):
    assert isinstance(instance, NQC::FunctionCall)

@given(instance=CompoundExpression_strategy)
@settings(max_examples=50)
def test_compoundexpression_instantiation(instance):
    assert isinstance(instance, CompoundExpression)

@given(instance=NQC::BinaryExpression_strategy)
@settings(max_examples=50)
def test_nqc::binaryexpression_instantiation(instance):
    assert isinstance(instance, NQC::BinaryExpression)

@given(instance=NQC::BinaryExpression_strategy)
def test_nqc::binaryexpression_Operator_type(instance):
    assert isinstance(instance.Operator, str)


@given(instance=NQC::BinaryExpression_strategy)
def test_nqc::binaryexpression_Operator_setter(instance):
    original = instance.Operator
    instance.Operator = original
    assert instance.Operator == original

@given(instance=ConstantExpression_strategy)
@settings(max_examples=50)
def test_constantexpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)

@given(instance=NQC::BooleanConstant_strategy)
@settings(max_examples=50)
def test_nqc::booleanconstant_instantiation(instance):
    assert isinstance(instance, NQC::BooleanConstant)

@given(instance=NQC::BooleanConstant_strategy)
def test_nqc::booleanconstant_Value_type(instance):
    assert isinstance(instance.Value, bool)


@given(instance=NQC::BooleanConstant_strategy)
def test_nqc::booleanconstant_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=VariableExpression_strategy)
@settings(max_examples=50)
def test_variableexpression_instantiation(instance):
    assert isinstance(instance, VariableExpression)

@given(instance=NQC::ArrayExpression_strategy)
@settings(max_examples=50)
def test_nqc::arrayexpression_instantiation(instance):
    assert isinstance(instance, NQC::ArrayExpression)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=NQC::CompoundExpression_strategy)
@settings(max_examples=50)
def test_nqc::compoundexpression_instantiation(instance):
    assert isinstance(instance, NQC::CompoundExpression)

@given(instance=NQC::ValueExpression_strategy)
@settings(max_examples=50)
def test_nqc::valueexpression_instantiation(instance):
    assert isinstance(instance, NQC::ValueExpression)

@given(instance=NQC::VariableExpression_strategy)
@settings(max_examples=50)
def test_nqc::variableexpression_instantiation(instance):
    assert isinstance(instance, NQC::VariableExpression)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=NQC::ControlStructure_strategy)
@settings(max_examples=50)
def test_nqc::controlstructure_instantiation(instance):
    assert isinstance(instance, NQC::ControlStructure)

@given(instance=NQC::EmptyStatement_strategy)
@settings(max_examples=50)
def test_nqc::emptystatement_instantiation(instance):
    assert isinstance(instance, NQC::EmptyStatement)

@given(instance=NQC::ContinueStatement_strategy)
@settings(max_examples=50)
def test_nqc::continuestatement_instantiation(instance):
    assert isinstance(instance, NQC::ContinueStatement)

@given(instance=NQC::CallStatement_strategy)
@settings(max_examples=50)
def test_nqc::callstatement_instantiation(instance):
    assert isinstance(instance, NQC::CallStatement)

@given(instance=NQC::BreakStatement_strategy)
@settings(max_examples=50)
def test_nqc::breakstatement_instantiation(instance):
    assert isinstance(instance, NQC::BreakStatement)

@given(instance=NQC::BlockStatement_strategy)
@settings(max_examples=50)
def test_nqc::blockstatement_instantiation(instance):
    assert isinstance(instance, NQC::BlockStatement)

@given(instance=NQC::Expression_strategy)
@settings(max_examples=50)
def test_nqc::expression_instantiation(instance):
    assert isinstance(instance, NQC::Expression)

@given(instance=NQC::AssignmentStatement_strategy)
@settings(max_examples=50)
def test_nqc::assignmentstatement_instantiation(instance):
    assert isinstance(instance, NQC::AssignmentStatement)

@given(instance=NQC::AssignmentStatement_strategy)
def test_nqc::assignmentstatement_Operator_type(instance):
    assert isinstance(instance.Operator, str)


@given(instance=NQC::AssignmentStatement_strategy)
def test_nqc::assignmentstatement_Operator_setter(instance):
    original = instance.Operator
    instance.Operator = original
    assert instance.Operator == original

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=NQC::RepeatStatement_strategy)
@settings(max_examples=50)
def test_nqc::repeatstatement_instantiation(instance):
    assert isinstance(instance, NQC::RepeatStatement)

@given(instance=NQC::WhileStatement_strategy)
@settings(max_examples=50)
def test_nqc::whilestatement_instantiation(instance):
    assert isinstance(instance, NQC::WhileStatement)

@given(instance=NQC::ForStatement_strategy)
@settings(max_examples=50)
def test_nqc::forstatement_instantiation(instance):
    assert isinstance(instance, NQC::ForStatement)

@given(instance=NQC::IfStatement_strategy)
@settings(max_examples=50)
def test_nqc::ifstatement_instantiation(instance):
    assert isinstance(instance, NQC::IfStatement)

@given(instance=NQC::GoToStatement_strategy)
@settings(max_examples=50)
def test_nqc::gotostatement_instantiation(instance):
    assert isinstance(instance, NQC::GoToStatement)

@given(instance=NQC::UntilStatement_strategy)
@settings(max_examples=50)
def test_nqc::untilstatement_instantiation(instance):
    assert isinstance(instance, NQC::UntilStatement)

@given(instance=NQC::SwitchStatement_strategy)
@settings(max_examples=50)
def test_nqc::switchstatement_instantiation(instance):
    assert isinstance(instance, NQC::SwitchStatement)

@given(instance=NQC::DoWhileStatement_strategy)
@settings(max_examples=50)
def test_nqc::dowhilestatement_instantiation(instance):
    assert isinstance(instance, NQC::DoWhileStatement)

@given(instance=NQC::StopStatement_strategy)
@settings(max_examples=50)
def test_nqc::stopstatement_instantiation(instance):
    assert isinstance(instance, NQC::StopStatement)

@given(instance=NQC::StartStatement_strategy)
@settings(max_examples=50)
def test_nqc::startstatement_instantiation(instance):
    assert isinstance(instance, NQC::StartStatement)

@given(instance=NQC::ReturnStatement_strategy)
@settings(max_examples=50)
def test_nqc::returnstatement_instantiation(instance):
    assert isinstance(instance, NQC::ReturnStatement)

@given(instance=NQC::Subroutine_strategy)
@settings(max_examples=50)
def test_nqc::subroutine_instantiation(instance):
    assert isinstance(instance, NQC::Subroutine)

@given(instance=NQC::Subroutine_strategy)
def test_nqc::subroutine_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=NQC::Subroutine_strategy)
def test_nqc::subroutine_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NQC::Function_strategy)
@settings(max_examples=50)
def test_nqc::function_instantiation(instance):
    assert isinstance(instance, NQC::Function)

@given(instance=NQC::Function_strategy)
def test_nqc::function_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=NQC::Function_strategy)
def test_nqc::function_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NQC::Task_strategy)
@settings(max_examples=50)
def test_nqc::task_instantiation(instance):
    assert isinstance(instance, NQC::Task)

@given(instance=NQC::Task_strategy)
def test_nqc::task_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=NQC::Task_strategy)
def test_nqc::task_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NQC::Program_strategy)
@settings(max_examples=50)
def test_nqc::program_instantiation(instance):
    assert isinstance(instance, NQC::Program)

@given(instance=NQC::Program_strategy)
def test_nqc::program_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=NQC::Program_strategy)
def test_nqc::program_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NQC::Label_strategy)
@settings(max_examples=50)
def test_nqc::label_instantiation(instance):
    assert isinstance(instance, NQC::Label)

@given(instance=NQC::Label_strategy)
def test_nqc::label_Label_type(instance):
    assert isinstance(instance.Label, str)


@given(instance=NQC::Label_strategy)
def test_nqc::label_Label_setter(instance):
    original = instance.Label
    instance.Label = original
    assert instance.Label == original

@given(instance=NQC::IntegerConstant_strategy)
@settings(max_examples=50)
def test_nqc::integerconstant_instantiation(instance):
    assert isinstance(instance, NQC::IntegerConstant)

@given(instance=NQC::IntegerConstant_strategy)
def test_nqc::integerconstant_Value_type(instance):
    assert isinstance(instance.Value, int)


@given(instance=NQC::IntegerConstant_strategy)
def test_nqc::integerconstant_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=NQC::ConstantExpression_strategy)
@settings(max_examples=50)
def test_nqc::constantexpression_instantiation(instance):
    assert isinstance(instance, NQC::ConstantExpression)

@given(instance=NQC::Variable_strategy)
@settings(max_examples=50)
def test_nqc::variable_instantiation(instance):
    assert isinstance(instance, NQC::Variable)

@given(instance=NQC::Variable_strategy)
def test_nqc::variable_Type_type(instance):
    assert isinstance(instance.Type, str)


@given(instance=NQC::Variable_strategy)
def test_nqc::variable_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=NQC::Variable_strategy)
def test_nqc::variable_Name_type(instance):
    assert isinstance(instance.Name, str)


@given(instance=NQC::Variable_strategy)
def test_nqc::variable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=NQC::GlobalVariable_strategy)
@settings(max_examples=50)
def test_nqc::globalvariable_instantiation(instance):
    assert isinstance(instance, NQC::GlobalVariable)

@given(instance=NQC::Parameter_strategy)
@settings(max_examples=50)
def test_nqc::parameter_instantiation(instance):
    assert isinstance(instance, NQC::Parameter)

@given(instance=NQC::LocalVariable_strategy)
@settings(max_examples=50)
def test_nqc::localvariable_instantiation(instance):
    assert isinstance(instance, NQC::LocalVariable)

@given(instance=NQC::Statement_strategy)
@settings(max_examples=50)
def test_nqc::statement_instantiation(instance):
    assert isinstance(instance, NQC::Statement)
