import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Action,
    co2_ActionType,
    co2_Action,
    Expression,
    co2_StringLiteral,
    co2_Equals,
    co2_Comparison,
    co2_Minus,
    co2_OrExpression,
    co2_AndExpression,
    co2_Plus,
    co2_NumberLiteral,
    co2_Case,
    Contract,
    co2_ExtSum,
    co2_IntSum,
    co2_EmptyContract,
    VariableDeclaration,
    co2_Type,
    co2_Placeholder,
    co2_BooleanLiteral,
    co2_Session,
    co2_ExtAction,
    co2_Input,
    ReceiveGroup,
    co2_Receive,
    SendGroup,
    co2_Send,
    co2_TimeoutProcess,
    co2_IntAction,
    co2_Contract,
    co2_VariableDeclaration,
    Prefix,
    co2_Ask,
    co2_DoOutput,
    co2_Retract,
    co2_Tau,
    co2_DoInput,
    co2_Tell,
    co2_Variable,
    co2_ContractDefinition,
    co2_ProcessDefinition,
    co2_Import,
    co2_ContractsAndProcessesDeclaration,
    co2_HonestyDeclaration,
    co2_Expression,
    co2_Prefix,
    co2_Process,
    co2_DelimitedProcess,
    Process,
    co2_Sum,
    co2_TellAndWait,
    co2_EmptyProcess,
    co2_ParallelProcesses,
    co2_SwitchCase,
    co2_IfThenElse,
    co2_TellAndReturn,
    co2_SendGroup,
    co2_ProcessCall,
    co2_ReceiveGroup,
    co2_RetractedProcess,
    co2_PackageDeclaration,
    co2_CO2System,
    Placeholder,
    co2_BoolPlaceholder,
    co2_IntPlaceholder,
    co2_VariableReference,
    co2_ArithmeticSigned,
    co2_BooleanNegation,
    co2_MultiOrDiv,
    ActionType,
    co2_IntActionType,
    co2_StringActionType,
    co2_UnitActionType,
    co2_ContractReference,
    Type,
    co2_SessionType,
    co2_BooleanType,
    co2_StringType,
    co2_IntType,
    co2_StringPlaceholder,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_co2_actiontype_is_not_abstract():
    assert not inspect.isabstract(co2_ActionType)


def test_co2_actiontype_constructor_exists():
    assert callable(co2_ActionType.__init__)


def test_co2_actiontype_constructor_args():
    sig = inspect.signature(co2_ActionType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2_actiontype_has_value():
    assert hasattr(co2_ActionType, "value")
    descriptor = None
    for klass in co2_ActionType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2_action_is_not_abstract():
    assert not inspect.isabstract(co2_Action)


def test_co2_action_constructor_exists():
    assert callable(co2_Action.__init__)


def test_co2_action_constructor_args():
    sig = inspect.signature(co2_Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_co2_action_has_name():
    assert hasattr(co2_Action, "name")
    descriptor = None
    for klass in co2_Action.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_co2_stringliteral_is_not_abstract():
    assert not inspect.isabstract(co2_StringLiteral)


def test_co2_stringliteral_constructor_exists():
    assert callable(co2_StringLiteral.__init__)


def test_co2_stringliteral_constructor_args():
    sig = inspect.signature(co2_StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2_stringliteral_has_value():
    assert hasattr(co2_StringLiteral, "value")
    descriptor = None
    for klass in co2_StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2_equals_is_not_abstract():
    assert not inspect.isabstract(co2_Equals)


def test_co2_equals_constructor_exists():
    assert callable(co2_Equals.__init__)


def test_co2_equals_constructor_args():
    sig = inspect.signature(co2_Equals.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_co2_equals_has_op():
    assert hasattr(co2_Equals, "op")
    descriptor = None
    for klass in co2_Equals.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_co2_comparison_is_not_abstract():
    assert not inspect.isabstract(co2_Comparison)


def test_co2_comparison_constructor_exists():
    assert callable(co2_Comparison.__init__)


def test_co2_comparison_constructor_args():
    sig = inspect.signature(co2_Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_co2_comparison_has_op():
    assert hasattr(co2_Comparison, "op")
    descriptor = None
    for klass in co2_Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_co2_minus_is_not_abstract():
    assert not inspect.isabstract(co2_Minus)


def test_co2_minus_constructor_exists():
    assert callable(co2_Minus.__init__)


def test_co2_minus_constructor_args():
    sig = inspect.signature(co2_Minus.__init__)
    params = list(sig.parameters.keys())



def test_co2_orexpression_is_not_abstract():
    assert not inspect.isabstract(co2_OrExpression)


def test_co2_orexpression_constructor_exists():
    assert callable(co2_OrExpression.__init__)


def test_co2_orexpression_constructor_args():
    sig = inspect.signature(co2_OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_co2_andexpression_is_not_abstract():
    assert not inspect.isabstract(co2_AndExpression)


def test_co2_andexpression_constructor_exists():
    assert callable(co2_AndExpression.__init__)


def test_co2_andexpression_constructor_args():
    sig = inspect.signature(co2_AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_co2_plus_is_not_abstract():
    assert not inspect.isabstract(co2_Plus)


def test_co2_plus_constructor_exists():
    assert callable(co2_Plus.__init__)


def test_co2_plus_constructor_args():
    sig = inspect.signature(co2_Plus.__init__)
    params = list(sig.parameters.keys())



def test_co2_numberliteral_is_not_abstract():
    assert not inspect.isabstract(co2_NumberLiteral)


def test_co2_numberliteral_constructor_exists():
    assert callable(co2_NumberLiteral.__init__)


def test_co2_numberliteral_constructor_args():
    sig = inspect.signature(co2_NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2_numberliteral_has_value():
    assert hasattr(co2_NumberLiteral, "value")
    descriptor = None
    for klass in co2_NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2_case_is_not_abstract():
    assert not inspect.isabstract(co2_Case)


def test_co2_case_constructor_exists():
    assert callable(co2_Case.__init__)


def test_co2_case_constructor_args():
    sig = inspect.signature(co2_Case.__init__)
    params = list(sig.parameters.keys())



def test_contract_is_not_abstract():
    assert not inspect.isabstract(Contract)


def test_contract_constructor_exists():
    assert callable(Contract.__init__)


def test_contract_constructor_args():
    sig = inspect.signature(Contract.__init__)
    params = list(sig.parameters.keys())



def test_co2_extsum_is_not_abstract():
    assert not inspect.isabstract(co2_ExtSum)


def test_co2_extsum_constructor_exists():
    assert callable(co2_ExtSum.__init__)


def test_co2_extsum_constructor_args():
    sig = inspect.signature(co2_ExtSum.__init__)
    params = list(sig.parameters.keys())



def test_co2_intsum_is_not_abstract():
    assert not inspect.isabstract(co2_IntSum)


def test_co2_intsum_constructor_exists():
    assert callable(co2_IntSum.__init__)


def test_co2_intsum_constructor_args():
    sig = inspect.signature(co2_IntSum.__init__)
    params = list(sig.parameters.keys())



def test_co2_emptycontract_is_not_abstract():
    assert not inspect.isabstract(co2_EmptyContract)


def test_co2_emptycontract_constructor_exists():
    assert callable(co2_EmptyContract.__init__)


def test_co2_emptycontract_constructor_args():
    sig = inspect.signature(co2_EmptyContract.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2_emptycontract_has_value():
    assert hasattr(co2_EmptyContract, "value")
    descriptor = None
    for klass in co2_EmptyContract.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(VariableDeclaration)


def test_variabledeclaration_constructor_exists():
    assert callable(VariableDeclaration.__init__)


def test_variabledeclaration_constructor_args():
    sig = inspect.signature(VariableDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_co2_type_is_not_abstract():
    assert not inspect.isabstract(co2_Type)


def test_co2_type_constructor_exists():
    assert callable(co2_Type.__init__)


def test_co2_type_constructor_args():
    sig = inspect.signature(co2_Type.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2_type_has_value():
    assert hasattr(co2_Type, "value")
    descriptor = None
    for klass in co2_Type.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2_placeholder_is_not_abstract():
    assert not inspect.isabstract(co2_Placeholder)


def test_co2_placeholder_constructor_exists():
    assert callable(co2_Placeholder.__init__)


def test_co2_placeholder_constructor_args():
    sig = inspect.signature(co2_Placeholder.__init__)
    params = list(sig.parameters.keys())



def test_co2_booleanliteral_is_not_abstract():
    assert not inspect.isabstract(co2_BooleanLiteral)


def test_co2_booleanliteral_constructor_exists():
    assert callable(co2_BooleanLiteral.__init__)


def test_co2_booleanliteral_constructor_args():
    sig = inspect.signature(co2_BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2_booleanliteral_has_value():
    assert hasattr(co2_BooleanLiteral, "value")
    descriptor = None
    for klass in co2_BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2_session_is_not_abstract():
    assert not inspect.isabstract(co2_Session)


def test_co2_session_constructor_exists():
    assert callable(co2_Session.__init__)


def test_co2_session_constructor_args():
    sig = inspect.signature(co2_Session.__init__)
    params = list(sig.parameters.keys())



def test_co2_extaction_is_not_abstract():
    assert not inspect.isabstract(co2_ExtAction)


def test_co2_extaction_constructor_exists():
    assert callable(co2_ExtAction.__init__)


def test_co2_extaction_constructor_args():
    sig = inspect.signature(co2_ExtAction.__init__)
    params = list(sig.parameters.keys())



def test_co2_input_is_not_abstract():
    assert not inspect.isabstract(co2_Input)


def test_co2_input_constructor_exists():
    assert callable(co2_Input.__init__)


def test_co2_input_constructor_args():
    sig = inspect.signature(co2_Input.__init__)
    params = list(sig.parameters.keys())



def test_receivegroup_is_not_abstract():
    assert not inspect.isabstract(ReceiveGroup)


def test_receivegroup_constructor_exists():
    assert callable(ReceiveGroup.__init__)


def test_receivegroup_constructor_args():
    sig = inspect.signature(ReceiveGroup.__init__)
    params = list(sig.parameters.keys())



def test_co2_receive_is_not_abstract():
    assert not inspect.isabstract(co2_Receive)


def test_co2_receive_constructor_exists():
    assert callable(co2_Receive.__init__)


def test_co2_receive_constructor_args():
    sig = inspect.signature(co2_Receive.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_co2_receive_has_timeout():
    assert hasattr(co2_Receive, "timeout")
    descriptor = None
    for klass in co2_Receive.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_sendgroup_is_not_abstract():
    assert not inspect.isabstract(SendGroup)


def test_sendgroup_constructor_exists():
    assert callable(SendGroup.__init__)


def test_sendgroup_constructor_args():
    sig = inspect.signature(SendGroup.__init__)
    params = list(sig.parameters.keys())



def test_co2_send_is_not_abstract():
    assert not inspect.isabstract(co2_Send)


def test_co2_send_constructor_exists():
    assert callable(co2_Send.__init__)


def test_co2_send_constructor_args():
    sig = inspect.signature(co2_Send.__init__)
    params = list(sig.parameters.keys())



def test_co2_timeoutprocess_is_not_abstract():
    assert not inspect.isabstract(co2_TimeoutProcess)


def test_co2_timeoutprocess_constructor_exists():
    assert callable(co2_TimeoutProcess.__init__)


def test_co2_timeoutprocess_constructor_args():
    sig = inspect.signature(co2_TimeoutProcess.__init__)
    params = list(sig.parameters.keys())



def test_co2_intaction_is_not_abstract():
    assert not inspect.isabstract(co2_IntAction)


def test_co2_intaction_constructor_exists():
    assert callable(co2_IntAction.__init__)


def test_co2_intaction_constructor_args():
    sig = inspect.signature(co2_IntAction.__init__)
    params = list(sig.parameters.keys())



def test_co2_contract_is_not_abstract():
    assert not inspect.isabstract(co2_Contract)


def test_co2_contract_constructor_exists():
    assert callable(co2_Contract.__init__)


def test_co2_contract_constructor_args():
    sig = inspect.signature(co2_Contract.__init__)
    params = list(sig.parameters.keys())



def test_co2_variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(co2_VariableDeclaration)


def test_co2_variabledeclaration_constructor_exists():
    assert callable(co2_VariableDeclaration.__init__)


def test_co2_variabledeclaration_constructor_args():
    sig = inspect.signature(co2_VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_co2_variabledeclaration_has_name():
    assert hasattr(co2_VariableDeclaration, "name")
    descriptor = None
    for klass in co2_VariableDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_prefix_is_not_abstract():
    assert not inspect.isabstract(Prefix)


def test_prefix_constructor_exists():
    assert callable(Prefix.__init__)


def test_prefix_constructor_args():
    sig = inspect.signature(Prefix.__init__)
    params = list(sig.parameters.keys())



def test_co2_ask_is_not_abstract():
    assert not inspect.isabstract(co2_Ask)


def test_co2_ask_constructor_exists():
    assert callable(co2_Ask.__init__)


def test_co2_ask_constructor_args():
    sig = inspect.signature(co2_Ask.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"

def test_co2_ask_has_formula():
    assert hasattr(co2_Ask, "formula")
    descriptor = None
    for klass in co2_Ask.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_co2_dooutput_is_not_abstract():
    assert not inspect.isabstract(co2_DoOutput)


def test_co2_dooutput_constructor_exists():
    assert callable(co2_DoOutput.__init__)


def test_co2_dooutput_constructor_args():
    sig = inspect.signature(co2_DoOutput.__init__)
    params = list(sig.parameters.keys())



def test_co2_retract_is_not_abstract():
    assert not inspect.isabstract(co2_Retract)


def test_co2_retract_constructor_exists():
    assert callable(co2_Retract.__init__)


def test_co2_retract_constructor_args():
    sig = inspect.signature(co2_Retract.__init__)
    params = list(sig.parameters.keys())



def test_co2_tau_is_not_abstract():
    assert not inspect.isabstract(co2_Tau)


def test_co2_tau_constructor_exists():
    assert callable(co2_Tau.__init__)


def test_co2_tau_constructor_args():
    sig = inspect.signature(co2_Tau.__init__)
    params = list(sig.parameters.keys())



def test_co2_doinput_is_not_abstract():
    assert not inspect.isabstract(co2_DoInput)


def test_co2_doinput_constructor_exists():
    assert callable(co2_DoInput.__init__)


def test_co2_doinput_constructor_args():
    sig = inspect.signature(co2_DoInput.__init__)
    params = list(sig.parameters.keys())



def test_co2_tell_is_not_abstract():
    assert not inspect.isabstract(co2_Tell)


def test_co2_tell_constructor_exists():
    assert callable(co2_Tell.__init__)


def test_co2_tell_constructor_args():
    sig = inspect.signature(co2_Tell.__init__)
    params = list(sig.parameters.keys())



def test_co2_variable_is_not_abstract():
    assert not inspect.isabstract(co2_Variable)


def test_co2_variable_constructor_exists():
    assert callable(co2_Variable.__init__)


def test_co2_variable_constructor_args():
    sig = inspect.signature(co2_Variable.__init__)
    params = list(sig.parameters.keys())



def test_co2_contractdefinition_is_not_abstract():
    assert not inspect.isabstract(co2_ContractDefinition)


def test_co2_contractdefinition_constructor_exists():
    assert callable(co2_ContractDefinition.__init__)


def test_co2_contractdefinition_constructor_args():
    sig = inspect.signature(co2_ContractDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_co2_contractdefinition_has_name():
    assert hasattr(co2_ContractDefinition, "name")
    descriptor = None
    for klass in co2_ContractDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_co2_processdefinition_is_not_abstract():
    assert not inspect.isabstract(co2_ProcessDefinition)


def test_co2_processdefinition_constructor_exists():
    assert callable(co2_ProcessDefinition.__init__)


def test_co2_processdefinition_constructor_args():
    sig = inspect.signature(co2_ProcessDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "withoutRestrictions" in params, "Missing parameter 'withoutRestrictions'"

def test_co2_processdefinition_has_name():
    assert hasattr(co2_ProcessDefinition, "name")
    descriptor = None
    for klass in co2_ProcessDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_co2_processdefinition_has_withoutRestrictions():
    assert hasattr(co2_ProcessDefinition, "withoutRestrictions")
    descriptor = None
    for klass in co2_ProcessDefinition.__mro__:
        if "withoutRestrictions" in klass.__dict__:
            descriptor = klass.__dict__["withoutRestrictions"]
            break
    assert isinstance(descriptor, property)



def test_co2_import_is_not_abstract():
    assert not inspect.isabstract(co2_Import)


def test_co2_import_constructor_exists():
    assert callable(co2_Import.__init__)


def test_co2_import_constructor_args():
    sig = inspect.signature(co2_Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_co2_import_has_importedNamespace():
    assert hasattr(co2_Import, "importedNamespace")
    descriptor = None
    for klass in co2_Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_co2_contractsandprocessesdeclaration_is_not_abstract():
    assert not inspect.isabstract(co2_ContractsAndProcessesDeclaration)


def test_co2_contractsandprocessesdeclaration_constructor_exists():
    assert callable(co2_ContractsAndProcessesDeclaration.__init__)


def test_co2_contractsandprocessesdeclaration_constructor_args():
    sig = inspect.signature(co2_ContractsAndProcessesDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_co2_honestydeclaration_is_not_abstract():
    assert not inspect.isabstract(co2_HonestyDeclaration)


def test_co2_honestydeclaration_constructor_exists():
    assert callable(co2_HonestyDeclaration.__init__)


def test_co2_honestydeclaration_constructor_args():
    sig = inspect.signature(co2_HonestyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_co2_expression_is_not_abstract():
    assert not inspect.isabstract(co2_Expression)


def test_co2_expression_constructor_exists():
    assert callable(co2_Expression.__init__)


def test_co2_expression_constructor_args():
    sig = inspect.signature(co2_Expression.__init__)
    params = list(sig.parameters.keys())



def test_co2_prefix_is_not_abstract():
    assert not inspect.isabstract(co2_Prefix)


def test_co2_prefix_constructor_exists():
    assert callable(co2_Prefix.__init__)


def test_co2_prefix_constructor_args():
    sig = inspect.signature(co2_Prefix.__init__)
    params = list(sig.parameters.keys())



def test_co2_process_is_not_abstract():
    assert not inspect.isabstract(co2_Process)


def test_co2_process_constructor_exists():
    assert callable(co2_Process.__init__)


def test_co2_process_constructor_args():
    sig = inspect.signature(co2_Process.__init__)
    params = list(sig.parameters.keys())



def test_co2_delimitedprocess_is_not_abstract():
    assert not inspect.isabstract(co2_DelimitedProcess)


def test_co2_delimitedprocess_constructor_exists():
    assert callable(co2_DelimitedProcess.__init__)


def test_co2_delimitedprocess_constructor_args():
    sig = inspect.signature(co2_DelimitedProcess.__init__)
    params = list(sig.parameters.keys())



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_co2_sum_is_not_abstract():
    assert not inspect.isabstract(co2_Sum)


def test_co2_sum_constructor_exists():
    assert callable(co2_Sum.__init__)


def test_co2_sum_constructor_args():
    sig = inspect.signature(co2_Sum.__init__)
    params = list(sig.parameters.keys())



def test_co2_tellandwait_is_not_abstract():
    assert not inspect.isabstract(co2_TellAndWait)


def test_co2_tellandwait_constructor_exists():
    assert callable(co2_TellAndWait.__init__)


def test_co2_tellandwait_constructor_args():
    sig = inspect.signature(co2_TellAndWait.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_co2_tellandwait_has_timeout():
    assert hasattr(co2_TellAndWait, "timeout")
    descriptor = None
    for klass in co2_TellAndWait.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_co2_emptyprocess_is_not_abstract():
    assert not inspect.isabstract(co2_EmptyProcess)


def test_co2_emptyprocess_constructor_exists():
    assert callable(co2_EmptyProcess.__init__)


def test_co2_emptyprocess_constructor_args():
    sig = inspect.signature(co2_EmptyProcess.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2_emptyprocess_has_value():
    assert hasattr(co2_EmptyProcess, "value")
    descriptor = None
    for klass in co2_EmptyProcess.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2_parallelprocesses_is_not_abstract():
    assert not inspect.isabstract(co2_ParallelProcesses)


def test_co2_parallelprocesses_constructor_exists():
    assert callable(co2_ParallelProcesses.__init__)


def test_co2_parallelprocesses_constructor_args():
    sig = inspect.signature(co2_ParallelProcesses.__init__)
    params = list(sig.parameters.keys())



def test_co2_switchcase_is_not_abstract():
    assert not inspect.isabstract(co2_SwitchCase)


def test_co2_switchcase_constructor_exists():
    assert callable(co2_SwitchCase.__init__)


def test_co2_switchcase_constructor_args():
    sig = inspect.signature(co2_SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_co2_switchcase_has_default():
    assert hasattr(co2_SwitchCase, "default")
    descriptor = None
    for klass in co2_SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_co2_ifthenelse_is_not_abstract():
    assert not inspect.isabstract(co2_IfThenElse)


def test_co2_ifthenelse_constructor_exists():
    assert callable(co2_IfThenElse.__init__)


def test_co2_ifthenelse_constructor_args():
    sig = inspect.signature(co2_IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_co2_tellandreturn_is_not_abstract():
    assert not inspect.isabstract(co2_TellAndReturn)


def test_co2_tellandreturn_constructor_exists():
    assert callable(co2_TellAndReturn.__init__)


def test_co2_tellandreturn_constructor_args():
    sig = inspect.signature(co2_TellAndReturn.__init__)
    params = list(sig.parameters.keys())



def test_co2_sendgroup_is_not_abstract():
    assert not inspect.isabstract(co2_SendGroup)


def test_co2_sendgroup_constructor_exists():
    assert callable(co2_SendGroup.__init__)


def test_co2_sendgroup_constructor_args():
    sig = inspect.signature(co2_SendGroup.__init__)
    params = list(sig.parameters.keys())



def test_co2_processcall_is_not_abstract():
    assert not inspect.isabstract(co2_ProcessCall)


def test_co2_processcall_constructor_exists():
    assert callable(co2_ProcessCall.__init__)


def test_co2_processcall_constructor_args():
    sig = inspect.signature(co2_ProcessCall.__init__)
    params = list(sig.parameters.keys())



def test_co2_receivegroup_is_not_abstract():
    assert not inspect.isabstract(co2_ReceiveGroup)


def test_co2_receivegroup_constructor_exists():
    assert callable(co2_ReceiveGroup.__init__)


def test_co2_receivegroup_constructor_args():
    sig = inspect.signature(co2_ReceiveGroup.__init__)
    params = list(sig.parameters.keys())



def test_co2_retractedprocess_is_not_abstract():
    assert not inspect.isabstract(co2_RetractedProcess)


def test_co2_retractedprocess_constructor_exists():
    assert callable(co2_RetractedProcess.__init__)


def test_co2_retractedprocess_constructor_args():
    sig = inspect.signature(co2_RetractedProcess.__init__)
    params = list(sig.parameters.keys())



def test_co2_packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(co2_PackageDeclaration)


def test_co2_packagedeclaration_constructor_exists():
    assert callable(co2_PackageDeclaration.__init__)


def test_co2_packagedeclaration_constructor_args():
    sig = inspect.signature(co2_PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "single" in params, "Missing parameter 'single'"
    assert "name" in params, "Missing parameter 'name'"

def test_co2_packagedeclaration_has_single():
    assert hasattr(co2_PackageDeclaration, "single")
    descriptor = None
    for klass in co2_PackageDeclaration.__mro__:
        if "single" in klass.__dict__:
            descriptor = klass.__dict__["single"]
            break
    assert isinstance(descriptor, property)

def test_co2_packagedeclaration_has_name():
    assert hasattr(co2_PackageDeclaration, "name")
    descriptor = None
    for klass in co2_PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_co2_co2system_is_not_abstract():
    assert not inspect.isabstract(co2_CO2System)


def test_co2_co2system_constructor_exists():
    assert callable(co2_CO2System.__init__)


def test_co2_co2system_constructor_args():
    sig = inspect.signature(co2_CO2System.__init__)
    params = list(sig.parameters.keys())



def test_placeholder_is_not_abstract():
    assert not inspect.isabstract(Placeholder)


def test_placeholder_constructor_exists():
    assert callable(Placeholder.__init__)


def test_placeholder_constructor_args():
    sig = inspect.signature(Placeholder.__init__)
    params = list(sig.parameters.keys())



def test_co2_boolplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2_BoolPlaceholder)


def test_co2_boolplaceholder_constructor_exists():
    assert callable(co2_BoolPlaceholder.__init__)


def test_co2_boolplaceholder_constructor_args():
    sig = inspect.signature(co2_BoolPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_co2_intplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2_IntPlaceholder)


def test_co2_intplaceholder_constructor_exists():
    assert callable(co2_IntPlaceholder.__init__)


def test_co2_intplaceholder_constructor_args():
    sig = inspect.signature(co2_IntPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_co2_variablereference_is_not_abstract():
    assert not inspect.isabstract(co2_VariableReference)


def test_co2_variablereference_constructor_exists():
    assert callable(co2_VariableReference.__init__)


def test_co2_variablereference_constructor_args():
    sig = inspect.signature(co2_VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_co2_arithmeticsigned_is_not_abstract():
    assert not inspect.isabstract(co2_ArithmeticSigned)


def test_co2_arithmeticsigned_constructor_exists():
    assert callable(co2_ArithmeticSigned.__init__)


def test_co2_arithmeticsigned_constructor_args():
    sig = inspect.signature(co2_ArithmeticSigned.__init__)
    params = list(sig.parameters.keys())



def test_co2_booleannegation_is_not_abstract():
    assert not inspect.isabstract(co2_BooleanNegation)


def test_co2_booleannegation_constructor_exists():
    assert callable(co2_BooleanNegation.__init__)


def test_co2_booleannegation_constructor_args():
    sig = inspect.signature(co2_BooleanNegation.__init__)
    params = list(sig.parameters.keys())



def test_co2_multiordiv_is_not_abstract():
    assert not inspect.isabstract(co2_MultiOrDiv)


def test_co2_multiordiv_constructor_exists():
    assert callable(co2_MultiOrDiv.__init__)


def test_co2_multiordiv_constructor_args():
    sig = inspect.signature(co2_MultiOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_co2_multiordiv_has_op():
    assert hasattr(co2_MultiOrDiv, "op")
    descriptor = None
    for klass in co2_MultiOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_actiontype_is_not_abstract():
    assert not inspect.isabstract(ActionType)


def test_actiontype_constructor_exists():
    assert callable(ActionType.__init__)


def test_actiontype_constructor_args():
    sig = inspect.signature(ActionType.__init__)
    params = list(sig.parameters.keys())



def test_co2_intactiontype_is_not_abstract():
    assert not inspect.isabstract(co2_IntActionType)


def test_co2_intactiontype_constructor_exists():
    assert callable(co2_IntActionType.__init__)


def test_co2_intactiontype_constructor_args():
    sig = inspect.signature(co2_IntActionType.__init__)
    params = list(sig.parameters.keys())



def test_co2_stringactiontype_is_not_abstract():
    assert not inspect.isabstract(co2_StringActionType)


def test_co2_stringactiontype_constructor_exists():
    assert callable(co2_StringActionType.__init__)


def test_co2_stringactiontype_constructor_args():
    sig = inspect.signature(co2_StringActionType.__init__)
    params = list(sig.parameters.keys())



def test_co2_unitactiontype_is_not_abstract():
    assert not inspect.isabstract(co2_UnitActionType)


def test_co2_unitactiontype_constructor_exists():
    assert callable(co2_UnitActionType.__init__)


def test_co2_unitactiontype_constructor_args():
    sig = inspect.signature(co2_UnitActionType.__init__)
    params = list(sig.parameters.keys())



def test_co2_contractreference_is_not_abstract():
    assert not inspect.isabstract(co2_ContractReference)


def test_co2_contractreference_constructor_exists():
    assert callable(co2_ContractReference.__init__)


def test_co2_contractreference_constructor_args():
    sig = inspect.signature(co2_ContractReference.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_co2_sessiontype_is_not_abstract():
    assert not inspect.isabstract(co2_SessionType)


def test_co2_sessiontype_constructor_exists():
    assert callable(co2_SessionType.__init__)


def test_co2_sessiontype_constructor_args():
    sig = inspect.signature(co2_SessionType.__init__)
    params = list(sig.parameters.keys())



def test_co2_booleantype_is_not_abstract():
    assert not inspect.isabstract(co2_BooleanType)


def test_co2_booleantype_constructor_exists():
    assert callable(co2_BooleanType.__init__)


def test_co2_booleantype_constructor_args():
    sig = inspect.signature(co2_BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_co2_stringtype_is_not_abstract():
    assert not inspect.isabstract(co2_StringType)


def test_co2_stringtype_constructor_exists():
    assert callable(co2_StringType.__init__)


def test_co2_stringtype_constructor_args():
    sig = inspect.signature(co2_StringType.__init__)
    params = list(sig.parameters.keys())



def test_co2_inttype_is_not_abstract():
    assert not inspect.isabstract(co2_IntType)


def test_co2_inttype_constructor_exists():
    assert callable(co2_IntType.__init__)


def test_co2_inttype_constructor_args():
    sig = inspect.signature(co2_IntType.__init__)
    params = list(sig.parameters.keys())



def test_co2_stringplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2_StringPlaceholder)


def test_co2_stringplaceholder_constructor_exists():
    assert callable(co2_StringPlaceholder.__init__)


def test_co2_stringplaceholder_constructor_args():
    sig = inspect.signature(co2_StringPlaceholder.__init__)
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
Action_strategy = st.builds(
    Action,
)
co2_ActionType_strategy = st.builds(
    co2_ActionType,
    value=
        safe_text
)
co2_Action_strategy = st.builds(
    co2_Action,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
co2_StringLiteral_strategy = st.builds(
    co2_StringLiteral,
    value=
        safe_text
)
co2_Equals_strategy = st.builds(
    co2_Equals,
    op=
        safe_text
)
co2_Comparison_strategy = st.builds(
    co2_Comparison,
    op=
        safe_text
)
co2_Minus_strategy = st.builds(
    co2_Minus,
)
co2_OrExpression_strategy = st.builds(
    co2_OrExpression,
)
co2_AndExpression_strategy = st.builds(
    co2_AndExpression,
)
co2_Plus_strategy = st.builds(
    co2_Plus,
)
co2_NumberLiteral_strategy = st.builds(
    co2_NumberLiteral,
    value=
        st.integers()
)
co2_Case_strategy = st.builds(
    co2_Case,
)
Contract_strategy = st.builds(
    Contract,
)
co2_ExtSum_strategy = st.builds(
    co2_ExtSum,
)
co2_IntSum_strategy = st.builds(
    co2_IntSum,
)
co2_EmptyContract_strategy = st.builds(
    co2_EmptyContract,
    value=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
co2_Type_strategy = st.builds(
    co2_Type,
    value=
        safe_text
)
co2_Placeholder_strategy = st.builds(
    co2_Placeholder,
)
co2_BooleanLiteral_strategy = st.builds(
    co2_BooleanLiteral,
    value=
        safe_text
)
co2_Session_strategy = st.builds(
    co2_Session,
)
co2_ExtAction_strategy = st.builds(
    co2_ExtAction,
)
co2_Input_strategy = st.builds(
    co2_Input,
)
ReceiveGroup_strategy = st.builds(
    ReceiveGroup,
)
co2_Receive_strategy = st.builds(
    co2_Receive,
    timeout=
        st.booleans()
)
SendGroup_strategy = st.builds(
    SendGroup,
)
co2_Send_strategy = st.builds(
    co2_Send,
)
co2_TimeoutProcess_strategy = st.builds(
    co2_TimeoutProcess,
)
co2_IntAction_strategy = st.builds(
    co2_IntAction,
)
co2_Contract_strategy = st.builds(
    co2_Contract,
)
co2_VariableDeclaration_strategy = st.builds(
    co2_VariableDeclaration,
    name=
        safe_text
)
Prefix_strategy = st.builds(
    Prefix,
)
co2_Ask_strategy = st.builds(
    co2_Ask,
    formula=
        safe_text
)
co2_DoOutput_strategy = st.builds(
    co2_DoOutput,
)
co2_Retract_strategy = st.builds(
    co2_Retract,
)
co2_Tau_strategy = st.builds(
    co2_Tau,
)
co2_DoInput_strategy = st.builds(
    co2_DoInput,
)
co2_Tell_strategy = st.builds(
    co2_Tell,
)
co2_Variable_strategy = st.builds(
    co2_Variable,
)
co2_ContractDefinition_strategy = st.builds(
    co2_ContractDefinition,
    name=
        safe_text
)
co2_ProcessDefinition_strategy = st.builds(
    co2_ProcessDefinition,
    name=
        safe_text,
    withoutRestrictions=
        st.booleans()
)
co2_Import_strategy = st.builds(
    co2_Import,
    importedNamespace=
        safe_text
)
co2_ContractsAndProcessesDeclaration_strategy = st.builds(
    co2_ContractsAndProcessesDeclaration,
)
co2_HonestyDeclaration_strategy = st.builds(
    co2_HonestyDeclaration,
)
co2_Expression_strategy = st.builds(
    co2_Expression,
)
co2_Prefix_strategy = st.builds(
    co2_Prefix,
)
co2_Process_strategy = st.builds(
    co2_Process,
)
co2_DelimitedProcess_strategy = st.builds(
    co2_DelimitedProcess,
)
Process_strategy = st.builds(
    Process,
)
co2_Sum_strategy = st.builds(
    co2_Sum,
)
co2_TellAndWait_strategy = st.builds(
    co2_TellAndWait,
    timeout=
        st.booleans()
)
co2_EmptyProcess_strategy = st.builds(
    co2_EmptyProcess,
    value=
        safe_text
)
co2_ParallelProcesses_strategy = st.builds(
    co2_ParallelProcesses,
)
co2_SwitchCase_strategy = st.builds(
    co2_SwitchCase,
    default=
        st.booleans()
)
co2_IfThenElse_strategy = st.builds(
    co2_IfThenElse,
)
co2_TellAndReturn_strategy = st.builds(
    co2_TellAndReturn,
)
co2_SendGroup_strategy = st.builds(
    co2_SendGroup,
)
co2_ProcessCall_strategy = st.builds(
    co2_ProcessCall,
)
co2_ReceiveGroup_strategy = st.builds(
    co2_ReceiveGroup,
)
co2_RetractedProcess_strategy = st.builds(
    co2_RetractedProcess,
)
co2_PackageDeclaration_strategy = st.builds(
    co2_PackageDeclaration,
    single=
        st.booleans(),
    name=
        safe_text
)
co2_CO2System_strategy = st.builds(
    co2_CO2System,
)
Placeholder_strategy = st.builds(
    Placeholder,
)
co2_BoolPlaceholder_strategy = st.builds(
    co2_BoolPlaceholder,
)
co2_IntPlaceholder_strategy = st.builds(
    co2_IntPlaceholder,
)
co2_VariableReference_strategy = st.builds(
    co2_VariableReference,
)
co2_ArithmeticSigned_strategy = st.builds(
    co2_ArithmeticSigned,
)
co2_BooleanNegation_strategy = st.builds(
    co2_BooleanNegation,
)
co2_MultiOrDiv_strategy = st.builds(
    co2_MultiOrDiv,
    op=
        safe_text
)
ActionType_strategy = st.builds(
    ActionType,
)
co2_IntActionType_strategy = st.builds(
    co2_IntActionType,
)
co2_StringActionType_strategy = st.builds(
    co2_StringActionType,
)
co2_UnitActionType_strategy = st.builds(
    co2_UnitActionType,
)
co2_ContractReference_strategy = st.builds(
    co2_ContractReference,
)
Type_strategy = st.builds(
    Type,
)
co2_SessionType_strategy = st.builds(
    co2_SessionType,
)
co2_BooleanType_strategy = st.builds(
    co2_BooleanType,
)
co2_StringType_strategy = st.builds(
    co2_StringType,
)
co2_IntType_strategy = st.builds(
    co2_IntType,
)
co2_StringPlaceholder_strategy = st.builds(
    co2_StringPlaceholder,
)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=co2_ActionType_strategy)
@settings(max_examples=50)
def test_co2_actiontype_instantiation(instance):
    assert isinstance(instance, co2_ActionType)



@given(instance=co2_ActionType_strategy)
def test_co2_actiontype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2_Action_strategy)
@settings(max_examples=50)
def test_co2_action_instantiation(instance):
    assert isinstance(instance, co2_Action)



@given(instance=co2_Action_strategy)
def test_co2_action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=co2_StringLiteral_strategy)
@settings(max_examples=50)
def test_co2_stringliteral_instantiation(instance):
    assert isinstance(instance, co2_StringLiteral)



@given(instance=co2_StringLiteral_strategy)
def test_co2_stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2_Equals_strategy)
@settings(max_examples=50)
def test_co2_equals_instantiation(instance):
    assert isinstance(instance, co2_Equals)



@given(instance=co2_Equals_strategy)
def test_co2_equals_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=co2_Comparison_strategy)
@settings(max_examples=50)
def test_co2_comparison_instantiation(instance):
    assert isinstance(instance, co2_Comparison)



@given(instance=co2_Comparison_strategy)
def test_co2_comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=co2_Minus_strategy)
@settings(max_examples=50)
def test_co2_minus_instantiation(instance):
    assert isinstance(instance, co2_Minus)

@given(instance=co2_OrExpression_strategy)
@settings(max_examples=50)
def test_co2_orexpression_instantiation(instance):
    assert isinstance(instance, co2_OrExpression)

@given(instance=co2_AndExpression_strategy)
@settings(max_examples=50)
def test_co2_andexpression_instantiation(instance):
    assert isinstance(instance, co2_AndExpression)

@given(instance=co2_Plus_strategy)
@settings(max_examples=50)
def test_co2_plus_instantiation(instance):
    assert isinstance(instance, co2_Plus)

@given(instance=co2_NumberLiteral_strategy)
@settings(max_examples=50)
def test_co2_numberliteral_instantiation(instance):
    assert isinstance(instance, co2_NumberLiteral)



@given(instance=co2_NumberLiteral_strategy)
def test_co2_numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2_Case_strategy)
@settings(max_examples=50)
def test_co2_case_instantiation(instance):
    assert isinstance(instance, co2_Case)

@given(instance=Contract_strategy)
@settings(max_examples=50)
def test_contract_instantiation(instance):
    assert isinstance(instance, Contract)

@given(instance=co2_ExtSum_strategy)
@settings(max_examples=50)
def test_co2_extsum_instantiation(instance):
    assert isinstance(instance, co2_ExtSum)

@given(instance=co2_IntSum_strategy)
@settings(max_examples=50)
def test_co2_intsum_instantiation(instance):
    assert isinstance(instance, co2_IntSum)

@given(instance=co2_EmptyContract_strategy)
@settings(max_examples=50)
def test_co2_emptycontract_instantiation(instance):
    assert isinstance(instance, co2_EmptyContract)



@given(instance=co2_EmptyContract_strategy)
def test_co2_emptycontract_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=co2_Type_strategy)
@settings(max_examples=50)
def test_co2_type_instantiation(instance):
    assert isinstance(instance, co2_Type)



@given(instance=co2_Type_strategy)
def test_co2_type_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2_Placeholder_strategy)
@settings(max_examples=50)
def test_co2_placeholder_instantiation(instance):
    assert isinstance(instance, co2_Placeholder)

@given(instance=co2_BooleanLiteral_strategy)
@settings(max_examples=50)
def test_co2_booleanliteral_instantiation(instance):
    assert isinstance(instance, co2_BooleanLiteral)



@given(instance=co2_BooleanLiteral_strategy)
def test_co2_booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2_Session_strategy)
@settings(max_examples=50)
def test_co2_session_instantiation(instance):
    assert isinstance(instance, co2_Session)

@given(instance=co2_ExtAction_strategy)
@settings(max_examples=50)
def test_co2_extaction_instantiation(instance):
    assert isinstance(instance, co2_ExtAction)

@given(instance=co2_Input_strategy)
@settings(max_examples=50)
def test_co2_input_instantiation(instance):
    assert isinstance(instance, co2_Input)

@given(instance=ReceiveGroup_strategy)
@settings(max_examples=50)
def test_receivegroup_instantiation(instance):
    assert isinstance(instance, ReceiveGroup)

@given(instance=co2_Receive_strategy)
@settings(max_examples=50)
def test_co2_receive_instantiation(instance):
    assert isinstance(instance, co2_Receive)



@given(instance=co2_Receive_strategy)
def test_co2_receive_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=SendGroup_strategy)
@settings(max_examples=50)
def test_sendgroup_instantiation(instance):
    assert isinstance(instance, SendGroup)

@given(instance=co2_Send_strategy)
@settings(max_examples=50)
def test_co2_send_instantiation(instance):
    assert isinstance(instance, co2_Send)

@given(instance=co2_TimeoutProcess_strategy)
@settings(max_examples=50)
def test_co2_timeoutprocess_instantiation(instance):
    assert isinstance(instance, co2_TimeoutProcess)

@given(instance=co2_IntAction_strategy)
@settings(max_examples=50)
def test_co2_intaction_instantiation(instance):
    assert isinstance(instance, co2_IntAction)

@given(instance=co2_Contract_strategy)
@settings(max_examples=50)
def test_co2_contract_instantiation(instance):
    assert isinstance(instance, co2_Contract)

@given(instance=co2_VariableDeclaration_strategy)
@settings(max_examples=50)
def test_co2_variabledeclaration_instantiation(instance):
    assert isinstance(instance, co2_VariableDeclaration)



@given(instance=co2_VariableDeclaration_strategy)
def test_co2_variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Prefix_strategy)
@settings(max_examples=50)
def test_prefix_instantiation(instance):
    assert isinstance(instance, Prefix)

@given(instance=co2_Ask_strategy)
@settings(max_examples=50)
def test_co2_ask_instantiation(instance):
    assert isinstance(instance, co2_Ask)



@given(instance=co2_Ask_strategy)
def test_co2_ask_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=co2_DoOutput_strategy)
@settings(max_examples=50)
def test_co2_dooutput_instantiation(instance):
    assert isinstance(instance, co2_DoOutput)

@given(instance=co2_Retract_strategy)
@settings(max_examples=50)
def test_co2_retract_instantiation(instance):
    assert isinstance(instance, co2_Retract)

@given(instance=co2_Tau_strategy)
@settings(max_examples=50)
def test_co2_tau_instantiation(instance):
    assert isinstance(instance, co2_Tau)

@given(instance=co2_DoInput_strategy)
@settings(max_examples=50)
def test_co2_doinput_instantiation(instance):
    assert isinstance(instance, co2_DoInput)

@given(instance=co2_Tell_strategy)
@settings(max_examples=50)
def test_co2_tell_instantiation(instance):
    assert isinstance(instance, co2_Tell)

@given(instance=co2_Variable_strategy)
@settings(max_examples=50)
def test_co2_variable_instantiation(instance):
    assert isinstance(instance, co2_Variable)

@given(instance=co2_ContractDefinition_strategy)
@settings(max_examples=50)
def test_co2_contractdefinition_instantiation(instance):
    assert isinstance(instance, co2_ContractDefinition)



@given(instance=co2_ContractDefinition_strategy)
def test_co2_contractdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=co2_ProcessDefinition_strategy)
@settings(max_examples=50)
def test_co2_processdefinition_instantiation(instance):
    assert isinstance(instance, co2_ProcessDefinition)



@given(instance=co2_ProcessDefinition_strategy)
def test_co2_processdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=co2_ProcessDefinition_strategy)
def test_co2_processdefinition_withoutRestrictions_setter(instance):
    original = instance.withoutRestrictions
    instance.withoutRestrictions = original
    assert instance.withoutRestrictions == original

@given(instance=co2_Import_strategy)
@settings(max_examples=50)
def test_co2_import_instantiation(instance):
    assert isinstance(instance, co2_Import)



@given(instance=co2_Import_strategy)
def test_co2_import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=co2_ContractsAndProcessesDeclaration_strategy)
@settings(max_examples=50)
def test_co2_contractsandprocessesdeclaration_instantiation(instance):
    assert isinstance(instance, co2_ContractsAndProcessesDeclaration)

@given(instance=co2_HonestyDeclaration_strategy)
@settings(max_examples=50)
def test_co2_honestydeclaration_instantiation(instance):
    assert isinstance(instance, co2_HonestyDeclaration)

@given(instance=co2_Expression_strategy)
@settings(max_examples=50)
def test_co2_expression_instantiation(instance):
    assert isinstance(instance, co2_Expression)

@given(instance=co2_Prefix_strategy)
@settings(max_examples=50)
def test_co2_prefix_instantiation(instance):
    assert isinstance(instance, co2_Prefix)

@given(instance=co2_Process_strategy)
@settings(max_examples=50)
def test_co2_process_instantiation(instance):
    assert isinstance(instance, co2_Process)

@given(instance=co2_DelimitedProcess_strategy)
@settings(max_examples=50)
def test_co2_delimitedprocess_instantiation(instance):
    assert isinstance(instance, co2_DelimitedProcess)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=co2_Sum_strategy)
@settings(max_examples=50)
def test_co2_sum_instantiation(instance):
    assert isinstance(instance, co2_Sum)

@given(instance=co2_TellAndWait_strategy)
@settings(max_examples=50)
def test_co2_tellandwait_instantiation(instance):
    assert isinstance(instance, co2_TellAndWait)



@given(instance=co2_TellAndWait_strategy)
def test_co2_tellandwait_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=co2_EmptyProcess_strategy)
@settings(max_examples=50)
def test_co2_emptyprocess_instantiation(instance):
    assert isinstance(instance, co2_EmptyProcess)



@given(instance=co2_EmptyProcess_strategy)
def test_co2_emptyprocess_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2_ParallelProcesses_strategy)
@settings(max_examples=50)
def test_co2_parallelprocesses_instantiation(instance):
    assert isinstance(instance, co2_ParallelProcesses)

@given(instance=co2_SwitchCase_strategy)
@settings(max_examples=50)
def test_co2_switchcase_instantiation(instance):
    assert isinstance(instance, co2_SwitchCase)



@given(instance=co2_SwitchCase_strategy)
def test_co2_switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=co2_IfThenElse_strategy)
@settings(max_examples=50)
def test_co2_ifthenelse_instantiation(instance):
    assert isinstance(instance, co2_IfThenElse)

@given(instance=co2_TellAndReturn_strategy)
@settings(max_examples=50)
def test_co2_tellandreturn_instantiation(instance):
    assert isinstance(instance, co2_TellAndReturn)

@given(instance=co2_SendGroup_strategy)
@settings(max_examples=50)
def test_co2_sendgroup_instantiation(instance):
    assert isinstance(instance, co2_SendGroup)

@given(instance=co2_ProcessCall_strategy)
@settings(max_examples=50)
def test_co2_processcall_instantiation(instance):
    assert isinstance(instance, co2_ProcessCall)

@given(instance=co2_ReceiveGroup_strategy)
@settings(max_examples=50)
def test_co2_receivegroup_instantiation(instance):
    assert isinstance(instance, co2_ReceiveGroup)

@given(instance=co2_RetractedProcess_strategy)
@settings(max_examples=50)
def test_co2_retractedprocess_instantiation(instance):
    assert isinstance(instance, co2_RetractedProcess)

@given(instance=co2_PackageDeclaration_strategy)
@settings(max_examples=50)
def test_co2_packagedeclaration_instantiation(instance):
    assert isinstance(instance, co2_PackageDeclaration)



@given(instance=co2_PackageDeclaration_strategy)
def test_co2_packagedeclaration_single_setter(instance):
    original = instance.single
    instance.single = original
    assert instance.single == original



@given(instance=co2_PackageDeclaration_strategy)
def test_co2_packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=co2_CO2System_strategy)
@settings(max_examples=50)
def test_co2_co2system_instantiation(instance):
    assert isinstance(instance, co2_CO2System)

@given(instance=Placeholder_strategy)
@settings(max_examples=50)
def test_placeholder_instantiation(instance):
    assert isinstance(instance, Placeholder)

@given(instance=co2_BoolPlaceholder_strategy)
@settings(max_examples=50)
def test_co2_boolplaceholder_instantiation(instance):
    assert isinstance(instance, co2_BoolPlaceholder)

@given(instance=co2_IntPlaceholder_strategy)
@settings(max_examples=50)
def test_co2_intplaceholder_instantiation(instance):
    assert isinstance(instance, co2_IntPlaceholder)

@given(instance=co2_VariableReference_strategy)
@settings(max_examples=50)
def test_co2_variablereference_instantiation(instance):
    assert isinstance(instance, co2_VariableReference)

@given(instance=co2_ArithmeticSigned_strategy)
@settings(max_examples=50)
def test_co2_arithmeticsigned_instantiation(instance):
    assert isinstance(instance, co2_ArithmeticSigned)

@given(instance=co2_BooleanNegation_strategy)
@settings(max_examples=50)
def test_co2_booleannegation_instantiation(instance):
    assert isinstance(instance, co2_BooleanNegation)

@given(instance=co2_MultiOrDiv_strategy)
@settings(max_examples=50)
def test_co2_multiordiv_instantiation(instance):
    assert isinstance(instance, co2_MultiOrDiv)



@given(instance=co2_MultiOrDiv_strategy)
def test_co2_multiordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=ActionType_strategy)
@settings(max_examples=50)
def test_actiontype_instantiation(instance):
    assert isinstance(instance, ActionType)

@given(instance=co2_IntActionType_strategy)
@settings(max_examples=50)
def test_co2_intactiontype_instantiation(instance):
    assert isinstance(instance, co2_IntActionType)

@given(instance=co2_StringActionType_strategy)
@settings(max_examples=50)
def test_co2_stringactiontype_instantiation(instance):
    assert isinstance(instance, co2_StringActionType)

@given(instance=co2_UnitActionType_strategy)
@settings(max_examples=50)
def test_co2_unitactiontype_instantiation(instance):
    assert isinstance(instance, co2_UnitActionType)

@given(instance=co2_ContractReference_strategy)
@settings(max_examples=50)
def test_co2_contractreference_instantiation(instance):
    assert isinstance(instance, co2_ContractReference)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=co2_SessionType_strategy)
@settings(max_examples=50)
def test_co2_sessiontype_instantiation(instance):
    assert isinstance(instance, co2_SessionType)

@given(instance=co2_BooleanType_strategy)
@settings(max_examples=50)
def test_co2_booleantype_instantiation(instance):
    assert isinstance(instance, co2_BooleanType)

@given(instance=co2_StringType_strategy)
@settings(max_examples=50)
def test_co2_stringtype_instantiation(instance):
    assert isinstance(instance, co2_StringType)

@given(instance=co2_IntType_strategy)
@settings(max_examples=50)
def test_co2_inttype_instantiation(instance):
    assert isinstance(instance, co2_IntType)

@given(instance=co2_StringPlaceholder_strategy)
@settings(max_examples=50)
def test_co2_stringplaceholder_instantiation(instance):
    assert isinstance(instance, co2_StringPlaceholder)
