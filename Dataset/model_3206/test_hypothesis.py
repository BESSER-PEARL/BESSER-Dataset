import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    VariableExpression,
    NQC_ArrayExpression,
    ValueExpression,
    Expression,
    NQC_ValueExpression,
    CallStatement,
    NQC_SubroutineCall,
    NQC_FunctionCall,
    CompoundExpression,
    NQC_BinaryExpression,
    NQC_CompoundExpression,
    ConstantExpression,
    NQC_BooleanConstant,
    NQC_Case,
    NQC_VariableExpression,
    ControlStructure,
    NQC_WhileStatement,
    NQC_IfStatement,
    NQC_RepeatStatement,
    NQC_SwitchStatement,
    NQC_GoToStatement,
    NQC_ForStatement,
    NQC_UntilStatement,
    NQC_DoWhileStatement,
    Variable,
    Statement,
    NQC_StopStatement,
    NQC_StartStatement,
    NQC_BreakStatement,
    NQC_CallStatement,
    NQC_EmptyStatement,
    NQC_ReturnStatement,
    NQC_BlockStatement,
    NQC_ControlStructure,
    NQC_ContinueStatement,
    NQC_Expression,
    NQC_AssignmentStatement,
    NQC_Label,
    NQC_IntegerConstant,
    NQC_ConstantExpression,
    NQC_Variable,
    NQC_Subroutine,
    NQC_Function,
    NQC_Task,
    NQC_Parameter,
    NQC_Program,
    NQC_LocalVariable,
    NQC_Statement,
    NQC_GlobalVariable,
    BinaryOperatorEnum,
    AssignmentStatementEnum,
    TypeEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_variableexpression_is_not_abstract():
    assert not inspect.isabstract(VariableExpression)


def test_variableexpression_constructor_exists():
    assert callable(VariableExpression.__init__)


def test_variableexpression_constructor_args():
    sig = inspect.signature(VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc_arrayexpression_is_not_abstract():
    assert not inspect.isabstract(NQC_ArrayExpression)


def test_nqc_arrayexpression_constructor_exists():
    assert callable(NQC_ArrayExpression.__init__)


def test_nqc_arrayexpression_constructor_args():
    sig = inspect.signature(NQC_ArrayExpression.__init__)
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



def test_nqc_valueexpression_is_not_abstract():
    assert not inspect.isabstract(NQC_ValueExpression)


def test_nqc_valueexpression_constructor_exists():
    assert callable(NQC_ValueExpression.__init__)


def test_nqc_valueexpression_constructor_args():
    sig = inspect.signature(NQC_ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_callstatement_is_not_abstract():
    assert not inspect.isabstract(CallStatement)


def test_callstatement_constructor_exists():
    assert callable(CallStatement.__init__)


def test_callstatement_constructor_args():
    sig = inspect.signature(CallStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_subroutinecall_is_not_abstract():
    assert not inspect.isabstract(NQC_SubroutineCall)


def test_nqc_subroutinecall_constructor_exists():
    assert callable(NQC_SubroutineCall.__init__)


def test_nqc_subroutinecall_constructor_args():
    sig = inspect.signature(NQC_SubroutineCall.__init__)
    params = list(sig.parameters.keys())



def test_nqc_functioncall_is_not_abstract():
    assert not inspect.isabstract(NQC_FunctionCall)


def test_nqc_functioncall_constructor_exists():
    assert callable(NQC_FunctionCall.__init__)


def test_nqc_functioncall_constructor_args():
    sig = inspect.signature(NQC_FunctionCall.__init__)
    params = list(sig.parameters.keys())



def test_compoundexpression_is_not_abstract():
    assert not inspect.isabstract(CompoundExpression)


def test_compoundexpression_constructor_exists():
    assert callable(CompoundExpression.__init__)


def test_compoundexpression_constructor_args():
    sig = inspect.signature(CompoundExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc_binaryexpression_is_not_abstract():
    assert not inspect.isabstract(NQC_BinaryExpression)


def test_nqc_binaryexpression_constructor_exists():
    assert callable(NQC_BinaryExpression.__init__)


def test_nqc_binaryexpression_constructor_args():
    sig = inspect.signature(NQC_BinaryExpression.__init__)
    params = list(sig.parameters.keys())
    assert "Operator" in params, "Missing parameter 'Operator'"

def test_nqc_binaryexpression_has_Operator():
    assert hasattr(NQC_BinaryExpression, "Operator")
    descriptor = None
    for klass in NQC_BinaryExpression.__mro__:
        if "Operator" in klass.__dict__:
            descriptor = klass.__dict__["Operator"]
            break
    assert isinstance(descriptor, property)



def test_nqc_compoundexpression_is_not_abstract():
    assert not inspect.isabstract(NQC_CompoundExpression)


def test_nqc_compoundexpression_constructor_exists():
    assert callable(NQC_CompoundExpression.__init__)


def test_nqc_compoundexpression_constructor_args():
    sig = inspect.signature(NQC_CompoundExpression.__init__)
    params = list(sig.parameters.keys())



def test_constantexpression_is_not_abstract():
    assert not inspect.isabstract(ConstantExpression)


def test_constantexpression_constructor_exists():
    assert callable(ConstantExpression.__init__)


def test_constantexpression_constructor_args():
    sig = inspect.signature(ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc_booleanconstant_is_not_abstract():
    assert not inspect.isabstract(NQC_BooleanConstant)


def test_nqc_booleanconstant_constructor_exists():
    assert callable(NQC_BooleanConstant.__init__)


def test_nqc_booleanconstant_constructor_args():
    sig = inspect.signature(NQC_BooleanConstant.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_nqc_booleanconstant_has_Value():
    assert hasattr(NQC_BooleanConstant, "Value")
    descriptor = None
    for klass in NQC_BooleanConstant.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_nqc_case_is_not_abstract():
    assert not inspect.isabstract(NQC_Case)


def test_nqc_case_constructor_exists():
    assert callable(NQC_Case.__init__)


def test_nqc_case_constructor_args():
    sig = inspect.signature(NQC_Case.__init__)
    params = list(sig.parameters.keys())
    assert "IsDefault" in params, "Missing parameter 'IsDefault'"

def test_nqc_case_has_IsDefault():
    assert hasattr(NQC_Case, "IsDefault")
    descriptor = None
    for klass in NQC_Case.__mro__:
        if "IsDefault" in klass.__dict__:
            descriptor = klass.__dict__["IsDefault"]
            break
    assert isinstance(descriptor, property)



def test_nqc_variableexpression_is_not_abstract():
    assert not inspect.isabstract(NQC_VariableExpression)


def test_nqc_variableexpression_constructor_exists():
    assert callable(NQC_VariableExpression.__init__)


def test_nqc_variableexpression_constructor_args():
    sig = inspect.signature(NQC_VariableExpression.__init__)
    params = list(sig.parameters.keys())



def test_controlstructure_is_not_abstract():
    assert not inspect.isabstract(ControlStructure)


def test_controlstructure_constructor_exists():
    assert callable(ControlStructure.__init__)


def test_controlstructure_constructor_args():
    sig = inspect.signature(ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_nqc_whilestatement_is_not_abstract():
    assert not inspect.isabstract(NQC_WhileStatement)


def test_nqc_whilestatement_constructor_exists():
    assert callable(NQC_WhileStatement.__init__)


def test_nqc_whilestatement_constructor_args():
    sig = inspect.signature(NQC_WhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_ifstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_IfStatement)


def test_nqc_ifstatement_constructor_exists():
    assert callable(NQC_IfStatement.__init__)


def test_nqc_ifstatement_constructor_args():
    sig = inspect.signature(NQC_IfStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_repeatstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_RepeatStatement)


def test_nqc_repeatstatement_constructor_exists():
    assert callable(NQC_RepeatStatement.__init__)


def test_nqc_repeatstatement_constructor_args():
    sig = inspect.signature(NQC_RepeatStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_switchstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_SwitchStatement)


def test_nqc_switchstatement_constructor_exists():
    assert callable(NQC_SwitchStatement.__init__)


def test_nqc_switchstatement_constructor_args():
    sig = inspect.signature(NQC_SwitchStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_gotostatement_is_not_abstract():
    assert not inspect.isabstract(NQC_GoToStatement)


def test_nqc_gotostatement_constructor_exists():
    assert callable(NQC_GoToStatement.__init__)


def test_nqc_gotostatement_constructor_args():
    sig = inspect.signature(NQC_GoToStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_forstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_ForStatement)


def test_nqc_forstatement_constructor_exists():
    assert callable(NQC_ForStatement.__init__)


def test_nqc_forstatement_constructor_args():
    sig = inspect.signature(NQC_ForStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_untilstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_UntilStatement)


def test_nqc_untilstatement_constructor_exists():
    assert callable(NQC_UntilStatement.__init__)


def test_nqc_untilstatement_constructor_args():
    sig = inspect.signature(NQC_UntilStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_dowhilestatement_is_not_abstract():
    assert not inspect.isabstract(NQC_DoWhileStatement)


def test_nqc_dowhilestatement_constructor_exists():
    assert callable(NQC_DoWhileStatement.__init__)


def test_nqc_dowhilestatement_constructor_args():
    sig = inspect.signature(NQC_DoWhileStatement.__init__)
    params = list(sig.parameters.keys())



def test_variable_is_not_abstract():
    assert not inspect.isabstract(Variable)


def test_variable_constructor_exists():
    assert callable(Variable.__init__)


def test_variable_constructor_args():
    sig = inspect.signature(Variable.__init__)
    params = list(sig.parameters.keys())



def test_statement_is_not_abstract():
    assert not inspect.isabstract(Statement)


def test_statement_constructor_exists():
    assert callable(Statement.__init__)


def test_statement_constructor_args():
    sig = inspect.signature(Statement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_stopstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_StopStatement)


def test_nqc_stopstatement_constructor_exists():
    assert callable(NQC_StopStatement.__init__)


def test_nqc_stopstatement_constructor_args():
    sig = inspect.signature(NQC_StopStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_startstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_StartStatement)


def test_nqc_startstatement_constructor_exists():
    assert callable(NQC_StartStatement.__init__)


def test_nqc_startstatement_constructor_args():
    sig = inspect.signature(NQC_StartStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_breakstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_BreakStatement)


def test_nqc_breakstatement_constructor_exists():
    assert callable(NQC_BreakStatement.__init__)


def test_nqc_breakstatement_constructor_args():
    sig = inspect.signature(NQC_BreakStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_callstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_CallStatement)


def test_nqc_callstatement_constructor_exists():
    assert callable(NQC_CallStatement.__init__)


def test_nqc_callstatement_constructor_args():
    sig = inspect.signature(NQC_CallStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_emptystatement_is_not_abstract():
    assert not inspect.isabstract(NQC_EmptyStatement)


def test_nqc_emptystatement_constructor_exists():
    assert callable(NQC_EmptyStatement.__init__)


def test_nqc_emptystatement_constructor_args():
    sig = inspect.signature(NQC_EmptyStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_returnstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_ReturnStatement)


def test_nqc_returnstatement_constructor_exists():
    assert callable(NQC_ReturnStatement.__init__)


def test_nqc_returnstatement_constructor_args():
    sig = inspect.signature(NQC_ReturnStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_blockstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_BlockStatement)


def test_nqc_blockstatement_constructor_exists():
    assert callable(NQC_BlockStatement.__init__)


def test_nqc_blockstatement_constructor_args():
    sig = inspect.signature(NQC_BlockStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_controlstructure_is_not_abstract():
    assert not inspect.isabstract(NQC_ControlStructure)


def test_nqc_controlstructure_constructor_exists():
    assert callable(NQC_ControlStructure.__init__)


def test_nqc_controlstructure_constructor_args():
    sig = inspect.signature(NQC_ControlStructure.__init__)
    params = list(sig.parameters.keys())



def test_nqc_continuestatement_is_not_abstract():
    assert not inspect.isabstract(NQC_ContinueStatement)


def test_nqc_continuestatement_constructor_exists():
    assert callable(NQC_ContinueStatement.__init__)


def test_nqc_continuestatement_constructor_args():
    sig = inspect.signature(NQC_ContinueStatement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_expression_is_not_abstract():
    assert not inspect.isabstract(NQC_Expression)


def test_nqc_expression_constructor_exists():
    assert callable(NQC_Expression.__init__)


def test_nqc_expression_constructor_args():
    sig = inspect.signature(NQC_Expression.__init__)
    params = list(sig.parameters.keys())



def test_nqc_assignmentstatement_is_not_abstract():
    assert not inspect.isabstract(NQC_AssignmentStatement)


def test_nqc_assignmentstatement_constructor_exists():
    assert callable(NQC_AssignmentStatement.__init__)


def test_nqc_assignmentstatement_constructor_args():
    sig = inspect.signature(NQC_AssignmentStatement.__init__)
    params = list(sig.parameters.keys())
    assert "Operator" in params, "Missing parameter 'Operator'"

def test_nqc_assignmentstatement_has_Operator():
    assert hasattr(NQC_AssignmentStatement, "Operator")
    descriptor = None
    for klass in NQC_AssignmentStatement.__mro__:
        if "Operator" in klass.__dict__:
            descriptor = klass.__dict__["Operator"]
            break
    assert isinstance(descriptor, property)



def test_nqc_label_is_not_abstract():
    assert not inspect.isabstract(NQC_Label)


def test_nqc_label_constructor_exists():
    assert callable(NQC_Label.__init__)


def test_nqc_label_constructor_args():
    sig = inspect.signature(NQC_Label.__init__)
    params = list(sig.parameters.keys())
    assert "Label" in params, "Missing parameter 'Label'"

def test_nqc_label_has_Label():
    assert hasattr(NQC_Label, "Label")
    descriptor = None
    for klass in NQC_Label.__mro__:
        if "Label" in klass.__dict__:
            descriptor = klass.__dict__["Label"]
            break
    assert isinstance(descriptor, property)



def test_nqc_integerconstant_is_not_abstract():
    assert not inspect.isabstract(NQC_IntegerConstant)


def test_nqc_integerconstant_constructor_exists():
    assert callable(NQC_IntegerConstant.__init__)


def test_nqc_integerconstant_constructor_args():
    sig = inspect.signature(NQC_IntegerConstant.__init__)
    params = list(sig.parameters.keys())
    assert "Value" in params, "Missing parameter 'Value'"

def test_nqc_integerconstant_has_Value():
    assert hasattr(NQC_IntegerConstant, "Value")
    descriptor = None
    for klass in NQC_IntegerConstant.__mro__:
        if "Value" in klass.__dict__:
            descriptor = klass.__dict__["Value"]
            break
    assert isinstance(descriptor, property)



def test_nqc_constantexpression_is_not_abstract():
    assert not inspect.isabstract(NQC_ConstantExpression)


def test_nqc_constantexpression_constructor_exists():
    assert callable(NQC_ConstantExpression.__init__)


def test_nqc_constantexpression_constructor_args():
    sig = inspect.signature(NQC_ConstantExpression.__init__)
    params = list(sig.parameters.keys())



def test_nqc_variable_is_not_abstract():
    assert not inspect.isabstract(NQC_Variable)


def test_nqc_variable_constructor_exists():
    assert callable(NQC_Variable.__init__)


def test_nqc_variable_constructor_args():
    sig = inspect.signature(NQC_Variable.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"
    assert "Type" in params, "Missing parameter 'Type'"

def test_nqc_variable_has_Name():
    assert hasattr(NQC_Variable, "Name")
    descriptor = None
    for klass in NQC_Variable.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)

def test_nqc_variable_has_Type():
    assert hasattr(NQC_Variable, "Type")
    descriptor = None
    for klass in NQC_Variable.__mro__:
        if "Type" in klass.__dict__:
            descriptor = klass.__dict__["Type"]
            break
    assert isinstance(descriptor, property)



def test_nqc_subroutine_is_not_abstract():
    assert not inspect.isabstract(NQC_Subroutine)


def test_nqc_subroutine_constructor_exists():
    assert callable(NQC_Subroutine.__init__)


def test_nqc_subroutine_constructor_args():
    sig = inspect.signature(NQC_Subroutine.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc_subroutine_has_Name():
    assert hasattr(NQC_Subroutine, "Name")
    descriptor = None
    for klass in NQC_Subroutine.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_nqc_function_is_not_abstract():
    assert not inspect.isabstract(NQC_Function)


def test_nqc_function_constructor_exists():
    assert callable(NQC_Function.__init__)


def test_nqc_function_constructor_args():
    sig = inspect.signature(NQC_Function.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc_function_has_Name():
    assert hasattr(NQC_Function, "Name")
    descriptor = None
    for klass in NQC_Function.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_nqc_task_is_not_abstract():
    assert not inspect.isabstract(NQC_Task)


def test_nqc_task_constructor_exists():
    assert callable(NQC_Task.__init__)


def test_nqc_task_constructor_args():
    sig = inspect.signature(NQC_Task.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc_task_has_Name():
    assert hasattr(NQC_Task, "Name")
    descriptor = None
    for klass in NQC_Task.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_nqc_parameter_is_not_abstract():
    assert not inspect.isabstract(NQC_Parameter)


def test_nqc_parameter_constructor_exists():
    assert callable(NQC_Parameter.__init__)


def test_nqc_parameter_constructor_args():
    sig = inspect.signature(NQC_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_nqc_program_is_not_abstract():
    assert not inspect.isabstract(NQC_Program)


def test_nqc_program_constructor_exists():
    assert callable(NQC_Program.__init__)


def test_nqc_program_constructor_args():
    sig = inspect.signature(NQC_Program.__init__)
    params = list(sig.parameters.keys())
    assert "Name" in params, "Missing parameter 'Name'"

def test_nqc_program_has_Name():
    assert hasattr(NQC_Program, "Name")
    descriptor = None
    for klass in NQC_Program.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_nqc_localvariable_is_not_abstract():
    assert not inspect.isabstract(NQC_LocalVariable)


def test_nqc_localvariable_constructor_exists():
    assert callable(NQC_LocalVariable.__init__)


def test_nqc_localvariable_constructor_args():
    sig = inspect.signature(NQC_LocalVariable.__init__)
    params = list(sig.parameters.keys())



def test_nqc_statement_is_not_abstract():
    assert not inspect.isabstract(NQC_Statement)


def test_nqc_statement_constructor_exists():
    assert callable(NQC_Statement.__init__)


def test_nqc_statement_constructor_args():
    sig = inspect.signature(NQC_Statement.__init__)
    params = list(sig.parameters.keys())



def test_nqc_globalvariable_is_not_abstract():
    assert not inspect.isabstract(NQC_GlobalVariable)


def test_nqc_globalvariable_constructor_exists():
    assert callable(NQC_GlobalVariable.__init__)


def test_nqc_globalvariable_constructor_args():
    sig = inspect.signature(NQC_GlobalVariable.__init__)
    params = list(sig.parameters.keys())

def test_binaryoperatorenum_exists():
    # Check that the Enumeration exists
    assert BinaryOperatorEnum is not None

def test_binaryoperatorenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BinaryOperatorEnum]
    expected_literals = [
        "bitand",
        "times",
        "greater",
        "div",
        "geq",
        "bitor",
        "minus",
        "notequal",
        "or_",
        "and_",
        "mod",
        "less",
        "leq",
        "plus",
        "equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BinaryOperatorEnum"

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
VariableExpression_strategy = st.builds(
    VariableExpression,
)
NQC_ArrayExpression_strategy = st.builds(
    NQC_ArrayExpression,
)
ValueExpression_strategy = st.builds(
    ValueExpression,
)
Expression_strategy = st.builds(
    Expression,
)
NQC_ValueExpression_strategy = st.builds(
    NQC_ValueExpression,
)
CallStatement_strategy = st.builds(
    CallStatement,
)
NQC_SubroutineCall_strategy = st.builds(
    NQC_SubroutineCall,
)
NQC_FunctionCall_strategy = st.builds(
    NQC_FunctionCall,
)
CompoundExpression_strategy = st.builds(
    CompoundExpression,
)
NQC_BinaryExpression_strategy = st.builds(
    NQC_BinaryExpression,
    Operator=
        safe_text
)
NQC_CompoundExpression_strategy = st.builds(
    NQC_CompoundExpression,
)
ConstantExpression_strategy = st.builds(
    ConstantExpression,
)
NQC_BooleanConstant_strategy = st.builds(
    NQC_BooleanConstant,
    Value=
        st.booleans()
)
NQC_Case_strategy = st.builds(
    NQC_Case,
    IsDefault=
        st.booleans()
)
NQC_VariableExpression_strategy = st.builds(
    NQC_VariableExpression,
)
ControlStructure_strategy = st.builds(
    ControlStructure,
)
NQC_WhileStatement_strategy = st.builds(
    NQC_WhileStatement,
)
NQC_IfStatement_strategy = st.builds(
    NQC_IfStatement,
)
NQC_RepeatStatement_strategy = st.builds(
    NQC_RepeatStatement,
)
NQC_SwitchStatement_strategy = st.builds(
    NQC_SwitchStatement,
)
NQC_GoToStatement_strategy = st.builds(
    NQC_GoToStatement,
)
NQC_ForStatement_strategy = st.builds(
    NQC_ForStatement,
)
NQC_UntilStatement_strategy = st.builds(
    NQC_UntilStatement,
)
NQC_DoWhileStatement_strategy = st.builds(
    NQC_DoWhileStatement,
)
Variable_strategy = st.builds(
    Variable,
)
Statement_strategy = st.builds(
    Statement,
)
NQC_StopStatement_strategy = st.builds(
    NQC_StopStatement,
)
NQC_StartStatement_strategy = st.builds(
    NQC_StartStatement,
)
NQC_BreakStatement_strategy = st.builds(
    NQC_BreakStatement,
)
NQC_CallStatement_strategy = st.builds(
    NQC_CallStatement,
)
NQC_EmptyStatement_strategy = st.builds(
    NQC_EmptyStatement,
)
NQC_ReturnStatement_strategy = st.builds(
    NQC_ReturnStatement,
)
NQC_BlockStatement_strategy = st.builds(
    NQC_BlockStatement,
)
NQC_ControlStructure_strategy = st.builds(
    NQC_ControlStructure,
)
NQC_ContinueStatement_strategy = st.builds(
    NQC_ContinueStatement,
)
NQC_Expression_strategy = st.builds(
    NQC_Expression,
)
NQC_AssignmentStatement_strategy = st.builds(
    NQC_AssignmentStatement,
    Operator=
        safe_text
)
NQC_Label_strategy = st.builds(
    NQC_Label,
    Label=
        safe_text
)
NQC_IntegerConstant_strategy = st.builds(
    NQC_IntegerConstant,
    Value=
        st.integers()
)
NQC_ConstantExpression_strategy = st.builds(
    NQC_ConstantExpression,
)
NQC_Variable_strategy = st.builds(
    NQC_Variable,
    Name=
        safe_text,
    Type=
        safe_text
)
NQC_Subroutine_strategy = st.builds(
    NQC_Subroutine,
    Name=
        safe_text
)
NQC_Function_strategy = st.builds(
    NQC_Function,
    Name=
        safe_text
)
NQC_Task_strategy = st.builds(
    NQC_Task,
    Name=
        safe_text
)
NQC_Parameter_strategy = st.builds(
    NQC_Parameter,
)
NQC_Program_strategy = st.builds(
    NQC_Program,
    Name=
        safe_text
)
NQC_LocalVariable_strategy = st.builds(
    NQC_LocalVariable,
)
NQC_Statement_strategy = st.builds(
    NQC_Statement,
)
NQC_GlobalVariable_strategy = st.builds(
    NQC_GlobalVariable,
)

@given(instance=VariableExpression_strategy)
@settings(max_examples=50)
def test_variableexpression_instantiation(instance):
    assert isinstance(instance, VariableExpression)

@given(instance=NQC_ArrayExpression_strategy)
@settings(max_examples=50)
def test_nqc_arrayexpression_instantiation(instance):
    assert isinstance(instance, NQC_ArrayExpression)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=NQC_ValueExpression_strategy)
@settings(max_examples=50)
def test_nqc_valueexpression_instantiation(instance):
    assert isinstance(instance, NQC_ValueExpression)

@given(instance=CallStatement_strategy)
@settings(max_examples=50)
def test_callstatement_instantiation(instance):
    assert isinstance(instance, CallStatement)

@given(instance=NQC_SubroutineCall_strategy)
@settings(max_examples=50)
def test_nqc_subroutinecall_instantiation(instance):
    assert isinstance(instance, NQC_SubroutineCall)

@given(instance=NQC_FunctionCall_strategy)
@settings(max_examples=50)
def test_nqc_functioncall_instantiation(instance):
    assert isinstance(instance, NQC_FunctionCall)

@given(instance=CompoundExpression_strategy)
@settings(max_examples=50)
def test_compoundexpression_instantiation(instance):
    assert isinstance(instance, CompoundExpression)

@given(instance=NQC_BinaryExpression_strategy)
@settings(max_examples=50)
def test_nqc_binaryexpression_instantiation(instance):
    assert isinstance(instance, NQC_BinaryExpression)



@given(instance=NQC_BinaryExpression_strategy)
def test_nqc_binaryexpression_Operator_setter(instance):
    original = instance.Operator
    instance.Operator = original
    assert instance.Operator == original

@given(instance=NQC_CompoundExpression_strategy)
@settings(max_examples=50)
def test_nqc_compoundexpression_instantiation(instance):
    assert isinstance(instance, NQC_CompoundExpression)

@given(instance=ConstantExpression_strategy)
@settings(max_examples=50)
def test_constantexpression_instantiation(instance):
    assert isinstance(instance, ConstantExpression)

@given(instance=NQC_BooleanConstant_strategy)
@settings(max_examples=50)
def test_nqc_booleanconstant_instantiation(instance):
    assert isinstance(instance, NQC_BooleanConstant)



@given(instance=NQC_BooleanConstant_strategy)
def test_nqc_booleanconstant_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=NQC_Case_strategy)
@settings(max_examples=50)
def test_nqc_case_instantiation(instance):
    assert isinstance(instance, NQC_Case)



@given(instance=NQC_Case_strategy)
def test_nqc_case_IsDefault_setter(instance):
    original = instance.IsDefault
    instance.IsDefault = original
    assert instance.IsDefault == original

@given(instance=NQC_VariableExpression_strategy)
@settings(max_examples=50)
def test_nqc_variableexpression_instantiation(instance):
    assert isinstance(instance, NQC_VariableExpression)

@given(instance=ControlStructure_strategy)
@settings(max_examples=50)
def test_controlstructure_instantiation(instance):
    assert isinstance(instance, ControlStructure)

@given(instance=NQC_WhileStatement_strategy)
@settings(max_examples=50)
def test_nqc_whilestatement_instantiation(instance):
    assert isinstance(instance, NQC_WhileStatement)

@given(instance=NQC_IfStatement_strategy)
@settings(max_examples=50)
def test_nqc_ifstatement_instantiation(instance):
    assert isinstance(instance, NQC_IfStatement)

@given(instance=NQC_RepeatStatement_strategy)
@settings(max_examples=50)
def test_nqc_repeatstatement_instantiation(instance):
    assert isinstance(instance, NQC_RepeatStatement)

@given(instance=NQC_SwitchStatement_strategy)
@settings(max_examples=50)
def test_nqc_switchstatement_instantiation(instance):
    assert isinstance(instance, NQC_SwitchStatement)

@given(instance=NQC_GoToStatement_strategy)
@settings(max_examples=50)
def test_nqc_gotostatement_instantiation(instance):
    assert isinstance(instance, NQC_GoToStatement)

@given(instance=NQC_ForStatement_strategy)
@settings(max_examples=50)
def test_nqc_forstatement_instantiation(instance):
    assert isinstance(instance, NQC_ForStatement)

@given(instance=NQC_UntilStatement_strategy)
@settings(max_examples=50)
def test_nqc_untilstatement_instantiation(instance):
    assert isinstance(instance, NQC_UntilStatement)

@given(instance=NQC_DoWhileStatement_strategy)
@settings(max_examples=50)
def test_nqc_dowhilestatement_instantiation(instance):
    assert isinstance(instance, NQC_DoWhileStatement)

@given(instance=Variable_strategy)
@settings(max_examples=50)
def test_variable_instantiation(instance):
    assert isinstance(instance, Variable)

@given(instance=Statement_strategy)
@settings(max_examples=50)
def test_statement_instantiation(instance):
    assert isinstance(instance, Statement)

@given(instance=NQC_StopStatement_strategy)
@settings(max_examples=50)
def test_nqc_stopstatement_instantiation(instance):
    assert isinstance(instance, NQC_StopStatement)

@given(instance=NQC_StartStatement_strategy)
@settings(max_examples=50)
def test_nqc_startstatement_instantiation(instance):
    assert isinstance(instance, NQC_StartStatement)

@given(instance=NQC_BreakStatement_strategy)
@settings(max_examples=50)
def test_nqc_breakstatement_instantiation(instance):
    assert isinstance(instance, NQC_BreakStatement)

@given(instance=NQC_CallStatement_strategy)
@settings(max_examples=50)
def test_nqc_callstatement_instantiation(instance):
    assert isinstance(instance, NQC_CallStatement)

@given(instance=NQC_EmptyStatement_strategy)
@settings(max_examples=50)
def test_nqc_emptystatement_instantiation(instance):
    assert isinstance(instance, NQC_EmptyStatement)

@given(instance=NQC_ReturnStatement_strategy)
@settings(max_examples=50)
def test_nqc_returnstatement_instantiation(instance):
    assert isinstance(instance, NQC_ReturnStatement)

@given(instance=NQC_BlockStatement_strategy)
@settings(max_examples=50)
def test_nqc_blockstatement_instantiation(instance):
    assert isinstance(instance, NQC_BlockStatement)

@given(instance=NQC_ControlStructure_strategy)
@settings(max_examples=50)
def test_nqc_controlstructure_instantiation(instance):
    assert isinstance(instance, NQC_ControlStructure)

@given(instance=NQC_ContinueStatement_strategy)
@settings(max_examples=50)
def test_nqc_continuestatement_instantiation(instance):
    assert isinstance(instance, NQC_ContinueStatement)

@given(instance=NQC_Expression_strategy)
@settings(max_examples=50)
def test_nqc_expression_instantiation(instance):
    assert isinstance(instance, NQC_Expression)

@given(instance=NQC_AssignmentStatement_strategy)
@settings(max_examples=50)
def test_nqc_assignmentstatement_instantiation(instance):
    assert isinstance(instance, NQC_AssignmentStatement)



@given(instance=NQC_AssignmentStatement_strategy)
def test_nqc_assignmentstatement_Operator_setter(instance):
    original = instance.Operator
    instance.Operator = original
    assert instance.Operator == original

@given(instance=NQC_Label_strategy)
@settings(max_examples=50)
def test_nqc_label_instantiation(instance):
    assert isinstance(instance, NQC_Label)



@given(instance=NQC_Label_strategy)
def test_nqc_label_Label_setter(instance):
    original = instance.Label
    instance.Label = original
    assert instance.Label == original

@given(instance=NQC_IntegerConstant_strategy)
@settings(max_examples=50)
def test_nqc_integerconstant_instantiation(instance):
    assert isinstance(instance, NQC_IntegerConstant)



@given(instance=NQC_IntegerConstant_strategy)
def test_nqc_integerconstant_Value_setter(instance):
    original = instance.Value
    instance.Value = original
    assert instance.Value == original

@given(instance=NQC_ConstantExpression_strategy)
@settings(max_examples=50)
def test_nqc_constantexpression_instantiation(instance):
    assert isinstance(instance, NQC_ConstantExpression)

@given(instance=NQC_Variable_strategy)
@settings(max_examples=50)
def test_nqc_variable_instantiation(instance):
    assert isinstance(instance, NQC_Variable)



@given(instance=NQC_Variable_strategy)
def test_nqc_variable_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original



@given(instance=NQC_Variable_strategy)
def test_nqc_variable_Type_setter(instance):
    original = instance.Type
    instance.Type = original
    assert instance.Type == original

@given(instance=NQC_Subroutine_strategy)
@settings(max_examples=50)
def test_nqc_subroutine_instantiation(instance):
    assert isinstance(instance, NQC_Subroutine)



@given(instance=NQC_Subroutine_strategy)
def test_nqc_subroutine_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NQC_Function_strategy)
@settings(max_examples=50)
def test_nqc_function_instantiation(instance):
    assert isinstance(instance, NQC_Function)



@given(instance=NQC_Function_strategy)
def test_nqc_function_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NQC_Task_strategy)
@settings(max_examples=50)
def test_nqc_task_instantiation(instance):
    assert isinstance(instance, NQC_Task)



@given(instance=NQC_Task_strategy)
def test_nqc_task_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NQC_Parameter_strategy)
@settings(max_examples=50)
def test_nqc_parameter_instantiation(instance):
    assert isinstance(instance, NQC_Parameter)

@given(instance=NQC_Program_strategy)
@settings(max_examples=50)
def test_nqc_program_instantiation(instance):
    assert isinstance(instance, NQC_Program)



@given(instance=NQC_Program_strategy)
def test_nqc_program_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=NQC_LocalVariable_strategy)
@settings(max_examples=50)
def test_nqc_localvariable_instantiation(instance):
    assert isinstance(instance, NQC_LocalVariable)

@given(instance=NQC_Statement_strategy)
@settings(max_examples=50)
def test_nqc_statement_instantiation(instance):
    assert isinstance(instance, NQC_Statement)

@given(instance=NQC_GlobalVariable_strategy)
@settings(max_examples=50)
def test_nqc_globalvariable_instantiation(instance):
    assert isinstance(instance, NQC_GlobalVariable)
