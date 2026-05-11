import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Process,
    co2::PackageDeclaration,
    co2::CO2System,
    Placeholder,
    co2::IntPlaceholder,
    ActionType,
    co2::StringActionType,
    co2::IntActionType,
    co2::UnitActionType,
    Type,
    co2::StringType,
    co2::SessionType,
    co2::BooleanType,
    co2::IntType,
    co2::StringPlaceholder,
    co2::BoolPlaceholder,
    co2::RetractedProcess,
    Action,
    co2::ActionType,
    co2::Action,
    Expression,
    co2::Comparison,
    co2::Plus,
    co2::BooleanNegation,
    co2::VariableReference,
    co2::ArithmeticSigned,
    co2::Equals,
    co2::MultiOrDiv,
    co2::Minus,
    co2::OrExpression,
    co2::StringLiteral,
    co2::AndExpression,
    co2::NumberLiteral,
    co2::Case,
    co2::SwitchCase,
    Contract,
    co2::ContractReference,
    co2::IntSum,
    co2::ExtSum,
    co2::EmptyContract,
    VariableDeclaration,
    co2::Type,
    co2::Placeholder,
    co2::BooleanLiteral,
    co2::TellAndWait,
    co2::Session,
    co2::TellAndReturn,
    co2::ExtAction,
    co2::Input,
    ReceiveGroup,
    co2::Receive,
    co2::ReceiveGroup,
    SendGroup,
    co2::Send,
    co2::SendGroup,
    co2::TimeoutProcess,
    co2::IntAction,
    co2::Contract,
    co2::VariableDeclaration,
    Prefix,
    co2::Tau,
    co2::DoInput,
    co2::Retract,
    co2::Ask,
    co2::DoOutput,
    co2::Tell,
    co2::ParallelProcesses,
    co2::Variable,
    co2::ContractDefinition,
    co2::ProcessDefinition,
    co2::Import,
    co2::ContractsAndProcessesDeclaration,
    co2::HonestyDeclaration,
    co2::ProcessCall,
    co2::Expression,
    co2::IfThenElse,
    co2::Prefix,
    co2::Sum,
    co2::EmptyProcess,
    co2::Process,
    co2::DelimitedProcess,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_process_is_not_abstract():
    assert not inspect.isabstract(Process)


def test_process_constructor_exists():
    assert callable(Process.__init__)


def test_process_constructor_args():
    sig = inspect.signature(Process.__init__)
    params = list(sig.parameters.keys())



def test_co2::packagedeclaration_is_not_abstract():
    assert not inspect.isabstract(co2::PackageDeclaration)


def test_co2::packagedeclaration_constructor_exists():
    assert callable(co2::PackageDeclaration.__init__)


def test_co2::packagedeclaration_constructor_args():
    sig = inspect.signature(co2::PackageDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "single" in params, "Missing parameter 'single'"
    assert "name" in params, "Missing parameter 'name'"

def test_co2::packagedeclaration_has_single():
    assert hasattr(co2::PackageDeclaration, "single")
    descriptor = None
    for klass in co2::PackageDeclaration.__mro__:
        if "single" in klass.__dict__:
            descriptor = klass.__dict__["single"]
            break
    assert isinstance(descriptor, property)

def test_co2::packagedeclaration_has_name():
    assert hasattr(co2::PackageDeclaration, "name")
    descriptor = None
    for klass in co2::PackageDeclaration.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_co2::co2system_is_not_abstract():
    assert not inspect.isabstract(co2::CO2System)


def test_co2::co2system_constructor_exists():
    assert callable(co2::CO2System.__init__)


def test_co2::co2system_constructor_args():
    sig = inspect.signature(co2::CO2System.__init__)
    params = list(sig.parameters.keys())



def test_placeholder_is_not_abstract():
    assert not inspect.isabstract(Placeholder)


def test_placeholder_constructor_exists():
    assert callable(Placeholder.__init__)


def test_placeholder_constructor_args():
    sig = inspect.signature(Placeholder.__init__)
    params = list(sig.parameters.keys())



def test_co2::intplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2::IntPlaceholder)


def test_co2::intplaceholder_constructor_exists():
    assert callable(co2::IntPlaceholder.__init__)


def test_co2::intplaceholder_constructor_args():
    sig = inspect.signature(co2::IntPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_actiontype_is_not_abstract():
    assert not inspect.isabstract(ActionType)


def test_actiontype_constructor_exists():
    assert callable(ActionType.__init__)


def test_actiontype_constructor_args():
    sig = inspect.signature(ActionType.__init__)
    params = list(sig.parameters.keys())



def test_co2::stringactiontype_is_not_abstract():
    assert not inspect.isabstract(co2::StringActionType)


def test_co2::stringactiontype_constructor_exists():
    assert callable(co2::StringActionType.__init__)


def test_co2::stringactiontype_constructor_args():
    sig = inspect.signature(co2::StringActionType.__init__)
    params = list(sig.parameters.keys())



def test_co2::intactiontype_is_not_abstract():
    assert not inspect.isabstract(co2::IntActionType)


def test_co2::intactiontype_constructor_exists():
    assert callable(co2::IntActionType.__init__)


def test_co2::intactiontype_constructor_args():
    sig = inspect.signature(co2::IntActionType.__init__)
    params = list(sig.parameters.keys())



def test_co2::unitactiontype_is_not_abstract():
    assert not inspect.isabstract(co2::UnitActionType)


def test_co2::unitactiontype_constructor_exists():
    assert callable(co2::UnitActionType.__init__)


def test_co2::unitactiontype_constructor_args():
    sig = inspect.signature(co2::UnitActionType.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_co2::stringtype_is_not_abstract():
    assert not inspect.isabstract(co2::StringType)


def test_co2::stringtype_constructor_exists():
    assert callable(co2::StringType.__init__)


def test_co2::stringtype_constructor_args():
    sig = inspect.signature(co2::StringType.__init__)
    params = list(sig.parameters.keys())



def test_co2::sessiontype_is_not_abstract():
    assert not inspect.isabstract(co2::SessionType)


def test_co2::sessiontype_constructor_exists():
    assert callable(co2::SessionType.__init__)


def test_co2::sessiontype_constructor_args():
    sig = inspect.signature(co2::SessionType.__init__)
    params = list(sig.parameters.keys())



def test_co2::booleantype_is_not_abstract():
    assert not inspect.isabstract(co2::BooleanType)


def test_co2::booleantype_constructor_exists():
    assert callable(co2::BooleanType.__init__)


def test_co2::booleantype_constructor_args():
    sig = inspect.signature(co2::BooleanType.__init__)
    params = list(sig.parameters.keys())



def test_co2::inttype_is_not_abstract():
    assert not inspect.isabstract(co2::IntType)


def test_co2::inttype_constructor_exists():
    assert callable(co2::IntType.__init__)


def test_co2::inttype_constructor_args():
    sig = inspect.signature(co2::IntType.__init__)
    params = list(sig.parameters.keys())



def test_co2::stringplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2::StringPlaceholder)


def test_co2::stringplaceholder_constructor_exists():
    assert callable(co2::StringPlaceholder.__init__)


def test_co2::stringplaceholder_constructor_args():
    sig = inspect.signature(co2::StringPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_co2::boolplaceholder_is_not_abstract():
    assert not inspect.isabstract(co2::BoolPlaceholder)


def test_co2::boolplaceholder_constructor_exists():
    assert callable(co2::BoolPlaceholder.__init__)


def test_co2::boolplaceholder_constructor_args():
    sig = inspect.signature(co2::BoolPlaceholder.__init__)
    params = list(sig.parameters.keys())



def test_co2::retractedprocess_is_not_abstract():
    assert not inspect.isabstract(co2::RetractedProcess)


def test_co2::retractedprocess_constructor_exists():
    assert callable(co2::RetractedProcess.__init__)


def test_co2::retractedprocess_constructor_args():
    sig = inspect.signature(co2::RetractedProcess.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_co2::actiontype_is_not_abstract():
    assert not inspect.isabstract(co2::ActionType)


def test_co2::actiontype_constructor_exists():
    assert callable(co2::ActionType.__init__)


def test_co2::actiontype_constructor_args():
    sig = inspect.signature(co2::ActionType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2::actiontype_has_value():
    assert hasattr(co2::ActionType, "value")
    descriptor = None
    for klass in co2::ActionType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2::action_is_not_abstract():
    assert not inspect.isabstract(co2::Action)


def test_co2::action_constructor_exists():
    assert callable(co2::Action.__init__)


def test_co2::action_constructor_args():
    sig = inspect.signature(co2::Action.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_co2::action_has_name():
    assert hasattr(co2::Action, "name")
    descriptor = None
    for klass in co2::Action.__mro__:
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



def test_co2::comparison_is_not_abstract():
    assert not inspect.isabstract(co2::Comparison)


def test_co2::comparison_constructor_exists():
    assert callable(co2::Comparison.__init__)


def test_co2::comparison_constructor_args():
    sig = inspect.signature(co2::Comparison.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_co2::comparison_has_op():
    assert hasattr(co2::Comparison, "op")
    descriptor = None
    for klass in co2::Comparison.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_co2::plus_is_not_abstract():
    assert not inspect.isabstract(co2::Plus)


def test_co2::plus_constructor_exists():
    assert callable(co2::Plus.__init__)


def test_co2::plus_constructor_args():
    sig = inspect.signature(co2::Plus.__init__)
    params = list(sig.parameters.keys())



def test_co2::booleannegation_is_not_abstract():
    assert not inspect.isabstract(co2::BooleanNegation)


def test_co2::booleannegation_constructor_exists():
    assert callable(co2::BooleanNegation.__init__)


def test_co2::booleannegation_constructor_args():
    sig = inspect.signature(co2::BooleanNegation.__init__)
    params = list(sig.parameters.keys())



def test_co2::variablereference_is_not_abstract():
    assert not inspect.isabstract(co2::VariableReference)


def test_co2::variablereference_constructor_exists():
    assert callable(co2::VariableReference.__init__)


def test_co2::variablereference_constructor_args():
    sig = inspect.signature(co2::VariableReference.__init__)
    params = list(sig.parameters.keys())



def test_co2::arithmeticsigned_is_not_abstract():
    assert not inspect.isabstract(co2::ArithmeticSigned)


def test_co2::arithmeticsigned_constructor_exists():
    assert callable(co2::ArithmeticSigned.__init__)


def test_co2::arithmeticsigned_constructor_args():
    sig = inspect.signature(co2::ArithmeticSigned.__init__)
    params = list(sig.parameters.keys())



def test_co2::equals_is_not_abstract():
    assert not inspect.isabstract(co2::Equals)


def test_co2::equals_constructor_exists():
    assert callable(co2::Equals.__init__)


def test_co2::equals_constructor_args():
    sig = inspect.signature(co2::Equals.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_co2::equals_has_op():
    assert hasattr(co2::Equals, "op")
    descriptor = None
    for klass in co2::Equals.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_co2::multiordiv_is_not_abstract():
    assert not inspect.isabstract(co2::MultiOrDiv)


def test_co2::multiordiv_constructor_exists():
    assert callable(co2::MultiOrDiv.__init__)


def test_co2::multiordiv_constructor_args():
    sig = inspect.signature(co2::MultiOrDiv.__init__)
    params = list(sig.parameters.keys())
    assert "op" in params, "Missing parameter 'op'"

def test_co2::multiordiv_has_op():
    assert hasattr(co2::MultiOrDiv, "op")
    descriptor = None
    for klass in co2::MultiOrDiv.__mro__:
        if "op" in klass.__dict__:
            descriptor = klass.__dict__["op"]
            break
    assert isinstance(descriptor, property)



def test_co2::minus_is_not_abstract():
    assert not inspect.isabstract(co2::Minus)


def test_co2::minus_constructor_exists():
    assert callable(co2::Minus.__init__)


def test_co2::minus_constructor_args():
    sig = inspect.signature(co2::Minus.__init__)
    params = list(sig.parameters.keys())



def test_co2::orexpression_is_not_abstract():
    assert not inspect.isabstract(co2::OrExpression)


def test_co2::orexpression_constructor_exists():
    assert callable(co2::OrExpression.__init__)


def test_co2::orexpression_constructor_args():
    sig = inspect.signature(co2::OrExpression.__init__)
    params = list(sig.parameters.keys())



def test_co2::stringliteral_is_not_abstract():
    assert not inspect.isabstract(co2::StringLiteral)


def test_co2::stringliteral_constructor_exists():
    assert callable(co2::StringLiteral.__init__)


def test_co2::stringliteral_constructor_args():
    sig = inspect.signature(co2::StringLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2::stringliteral_has_value():
    assert hasattr(co2::StringLiteral, "value")
    descriptor = None
    for klass in co2::StringLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2::andexpression_is_not_abstract():
    assert not inspect.isabstract(co2::AndExpression)


def test_co2::andexpression_constructor_exists():
    assert callable(co2::AndExpression.__init__)


def test_co2::andexpression_constructor_args():
    sig = inspect.signature(co2::AndExpression.__init__)
    params = list(sig.parameters.keys())



def test_co2::numberliteral_is_not_abstract():
    assert not inspect.isabstract(co2::NumberLiteral)


def test_co2::numberliteral_constructor_exists():
    assert callable(co2::NumberLiteral.__init__)


def test_co2::numberliteral_constructor_args():
    sig = inspect.signature(co2::NumberLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2::numberliteral_has_value():
    assert hasattr(co2::NumberLiteral, "value")
    descriptor = None
    for klass in co2::NumberLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2::case_is_not_abstract():
    assert not inspect.isabstract(co2::Case)


def test_co2::case_constructor_exists():
    assert callable(co2::Case.__init__)


def test_co2::case_constructor_args():
    sig = inspect.signature(co2::Case.__init__)
    params = list(sig.parameters.keys())



def test_co2::switchcase_is_not_abstract():
    assert not inspect.isabstract(co2::SwitchCase)


def test_co2::switchcase_constructor_exists():
    assert callable(co2::SwitchCase.__init__)


def test_co2::switchcase_constructor_args():
    sig = inspect.signature(co2::SwitchCase.__init__)
    params = list(sig.parameters.keys())
    assert "default" in params, "Missing parameter 'default'"

def test_co2::switchcase_has_default():
    assert hasattr(co2::SwitchCase, "default")
    descriptor = None
    for klass in co2::SwitchCase.__mro__:
        if "default" in klass.__dict__:
            descriptor = klass.__dict__["default"]
            break
    assert isinstance(descriptor, property)



def test_contract_is_not_abstract():
    assert not inspect.isabstract(Contract)


def test_contract_constructor_exists():
    assert callable(Contract.__init__)


def test_contract_constructor_args():
    sig = inspect.signature(Contract.__init__)
    params = list(sig.parameters.keys())



def test_co2::contractreference_is_not_abstract():
    assert not inspect.isabstract(co2::ContractReference)


def test_co2::contractreference_constructor_exists():
    assert callable(co2::ContractReference.__init__)


def test_co2::contractreference_constructor_args():
    sig = inspect.signature(co2::ContractReference.__init__)
    params = list(sig.parameters.keys())



def test_co2::intsum_is_not_abstract():
    assert not inspect.isabstract(co2::IntSum)


def test_co2::intsum_constructor_exists():
    assert callable(co2::IntSum.__init__)


def test_co2::intsum_constructor_args():
    sig = inspect.signature(co2::IntSum.__init__)
    params = list(sig.parameters.keys())



def test_co2::extsum_is_not_abstract():
    assert not inspect.isabstract(co2::ExtSum)


def test_co2::extsum_constructor_exists():
    assert callable(co2::ExtSum.__init__)


def test_co2::extsum_constructor_args():
    sig = inspect.signature(co2::ExtSum.__init__)
    params = list(sig.parameters.keys())



def test_co2::emptycontract_is_not_abstract():
    assert not inspect.isabstract(co2::EmptyContract)


def test_co2::emptycontract_constructor_exists():
    assert callable(co2::EmptyContract.__init__)


def test_co2::emptycontract_constructor_args():
    sig = inspect.signature(co2::EmptyContract.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2::emptycontract_has_value():
    assert hasattr(co2::EmptyContract, "value")
    descriptor = None
    for klass in co2::EmptyContract.__mro__:
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



def test_co2::type_is_not_abstract():
    assert not inspect.isabstract(co2::Type)


def test_co2::type_constructor_exists():
    assert callable(co2::Type.__init__)


def test_co2::type_constructor_args():
    sig = inspect.signature(co2::Type.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2::type_has_value():
    assert hasattr(co2::Type, "value")
    descriptor = None
    for klass in co2::Type.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2::placeholder_is_not_abstract():
    assert not inspect.isabstract(co2::Placeholder)


def test_co2::placeholder_constructor_exists():
    assert callable(co2::Placeholder.__init__)


def test_co2::placeholder_constructor_args():
    sig = inspect.signature(co2::Placeholder.__init__)
    params = list(sig.parameters.keys())



def test_co2::booleanliteral_is_not_abstract():
    assert not inspect.isabstract(co2::BooleanLiteral)


def test_co2::booleanliteral_constructor_exists():
    assert callable(co2::BooleanLiteral.__init__)


def test_co2::booleanliteral_constructor_args():
    sig = inspect.signature(co2::BooleanLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2::booleanliteral_has_value():
    assert hasattr(co2::BooleanLiteral, "value")
    descriptor = None
    for klass in co2::BooleanLiteral.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2::tellandwait_is_not_abstract():
    assert not inspect.isabstract(co2::TellAndWait)


def test_co2::tellandwait_constructor_exists():
    assert callable(co2::TellAndWait.__init__)


def test_co2::tellandwait_constructor_args():
    sig = inspect.signature(co2::TellAndWait.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_co2::tellandwait_has_timeout():
    assert hasattr(co2::TellAndWait, "timeout")
    descriptor = None
    for klass in co2::TellAndWait.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_co2::session_is_not_abstract():
    assert not inspect.isabstract(co2::Session)


def test_co2::session_constructor_exists():
    assert callable(co2::Session.__init__)


def test_co2::session_constructor_args():
    sig = inspect.signature(co2::Session.__init__)
    params = list(sig.parameters.keys())



def test_co2::tellandreturn_is_not_abstract():
    assert not inspect.isabstract(co2::TellAndReturn)


def test_co2::tellandreturn_constructor_exists():
    assert callable(co2::TellAndReturn.__init__)


def test_co2::tellandreturn_constructor_args():
    sig = inspect.signature(co2::TellAndReturn.__init__)
    params = list(sig.parameters.keys())



def test_co2::extaction_is_not_abstract():
    assert not inspect.isabstract(co2::ExtAction)


def test_co2::extaction_constructor_exists():
    assert callable(co2::ExtAction.__init__)


def test_co2::extaction_constructor_args():
    sig = inspect.signature(co2::ExtAction.__init__)
    params = list(sig.parameters.keys())



def test_co2::input_is_not_abstract():
    assert not inspect.isabstract(co2::Input)


def test_co2::input_constructor_exists():
    assert callable(co2::Input.__init__)


def test_co2::input_constructor_args():
    sig = inspect.signature(co2::Input.__init__)
    params = list(sig.parameters.keys())



def test_receivegroup_is_not_abstract():
    assert not inspect.isabstract(ReceiveGroup)


def test_receivegroup_constructor_exists():
    assert callable(ReceiveGroup.__init__)


def test_receivegroup_constructor_args():
    sig = inspect.signature(ReceiveGroup.__init__)
    params = list(sig.parameters.keys())



def test_co2::receive_is_not_abstract():
    assert not inspect.isabstract(co2::Receive)


def test_co2::receive_constructor_exists():
    assert callable(co2::Receive.__init__)


def test_co2::receive_constructor_args():
    sig = inspect.signature(co2::Receive.__init__)
    params = list(sig.parameters.keys())
    assert "timeout" in params, "Missing parameter 'timeout'"

def test_co2::receive_has_timeout():
    assert hasattr(co2::Receive, "timeout")
    descriptor = None
    for klass in co2::Receive.__mro__:
        if "timeout" in klass.__dict__:
            descriptor = klass.__dict__["timeout"]
            break
    assert isinstance(descriptor, property)



def test_co2::receivegroup_is_not_abstract():
    assert not inspect.isabstract(co2::ReceiveGroup)


def test_co2::receivegroup_constructor_exists():
    assert callable(co2::ReceiveGroup.__init__)


def test_co2::receivegroup_constructor_args():
    sig = inspect.signature(co2::ReceiveGroup.__init__)
    params = list(sig.parameters.keys())



def test_sendgroup_is_not_abstract():
    assert not inspect.isabstract(SendGroup)


def test_sendgroup_constructor_exists():
    assert callable(SendGroup.__init__)


def test_sendgroup_constructor_args():
    sig = inspect.signature(SendGroup.__init__)
    params = list(sig.parameters.keys())



def test_co2::send_is_not_abstract():
    assert not inspect.isabstract(co2::Send)


def test_co2::send_constructor_exists():
    assert callable(co2::Send.__init__)


def test_co2::send_constructor_args():
    sig = inspect.signature(co2::Send.__init__)
    params = list(sig.parameters.keys())



def test_co2::sendgroup_is_not_abstract():
    assert not inspect.isabstract(co2::SendGroup)


def test_co2::sendgroup_constructor_exists():
    assert callable(co2::SendGroup.__init__)


def test_co2::sendgroup_constructor_args():
    sig = inspect.signature(co2::SendGroup.__init__)
    params = list(sig.parameters.keys())



def test_co2::timeoutprocess_is_not_abstract():
    assert not inspect.isabstract(co2::TimeoutProcess)


def test_co2::timeoutprocess_constructor_exists():
    assert callable(co2::TimeoutProcess.__init__)


def test_co2::timeoutprocess_constructor_args():
    sig = inspect.signature(co2::TimeoutProcess.__init__)
    params = list(sig.parameters.keys())



def test_co2::intaction_is_not_abstract():
    assert not inspect.isabstract(co2::IntAction)


def test_co2::intaction_constructor_exists():
    assert callable(co2::IntAction.__init__)


def test_co2::intaction_constructor_args():
    sig = inspect.signature(co2::IntAction.__init__)
    params = list(sig.parameters.keys())



def test_co2::contract_is_not_abstract():
    assert not inspect.isabstract(co2::Contract)


def test_co2::contract_constructor_exists():
    assert callable(co2::Contract.__init__)


def test_co2::contract_constructor_args():
    sig = inspect.signature(co2::Contract.__init__)
    params = list(sig.parameters.keys())



def test_co2::variabledeclaration_is_not_abstract():
    assert not inspect.isabstract(co2::VariableDeclaration)


def test_co2::variabledeclaration_constructor_exists():
    assert callable(co2::VariableDeclaration.__init__)


def test_co2::variabledeclaration_constructor_args():
    sig = inspect.signature(co2::VariableDeclaration.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_co2::variabledeclaration_has_name():
    assert hasattr(co2::VariableDeclaration, "name")
    descriptor = None
    for klass in co2::VariableDeclaration.__mro__:
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



def test_co2::tau_is_not_abstract():
    assert not inspect.isabstract(co2::Tau)


def test_co2::tau_constructor_exists():
    assert callable(co2::Tau.__init__)


def test_co2::tau_constructor_args():
    sig = inspect.signature(co2::Tau.__init__)
    params = list(sig.parameters.keys())



def test_co2::doinput_is_not_abstract():
    assert not inspect.isabstract(co2::DoInput)


def test_co2::doinput_constructor_exists():
    assert callable(co2::DoInput.__init__)


def test_co2::doinput_constructor_args():
    sig = inspect.signature(co2::DoInput.__init__)
    params = list(sig.parameters.keys())



def test_co2::retract_is_not_abstract():
    assert not inspect.isabstract(co2::Retract)


def test_co2::retract_constructor_exists():
    assert callable(co2::Retract.__init__)


def test_co2::retract_constructor_args():
    sig = inspect.signature(co2::Retract.__init__)
    params = list(sig.parameters.keys())



def test_co2::ask_is_not_abstract():
    assert not inspect.isabstract(co2::Ask)


def test_co2::ask_constructor_exists():
    assert callable(co2::Ask.__init__)


def test_co2::ask_constructor_args():
    sig = inspect.signature(co2::Ask.__init__)
    params = list(sig.parameters.keys())
    assert "formula" in params, "Missing parameter 'formula'"

def test_co2::ask_has_formula():
    assert hasattr(co2::Ask, "formula")
    descriptor = None
    for klass in co2::Ask.__mro__:
        if "formula" in klass.__dict__:
            descriptor = klass.__dict__["formula"]
            break
    assert isinstance(descriptor, property)



def test_co2::dooutput_is_not_abstract():
    assert not inspect.isabstract(co2::DoOutput)


def test_co2::dooutput_constructor_exists():
    assert callable(co2::DoOutput.__init__)


def test_co2::dooutput_constructor_args():
    sig = inspect.signature(co2::DoOutput.__init__)
    params = list(sig.parameters.keys())



def test_co2::tell_is_not_abstract():
    assert not inspect.isabstract(co2::Tell)


def test_co2::tell_constructor_exists():
    assert callable(co2::Tell.__init__)


def test_co2::tell_constructor_args():
    sig = inspect.signature(co2::Tell.__init__)
    params = list(sig.parameters.keys())



def test_co2::parallelprocesses_is_not_abstract():
    assert not inspect.isabstract(co2::ParallelProcesses)


def test_co2::parallelprocesses_constructor_exists():
    assert callable(co2::ParallelProcesses.__init__)


def test_co2::parallelprocesses_constructor_args():
    sig = inspect.signature(co2::ParallelProcesses.__init__)
    params = list(sig.parameters.keys())



def test_co2::variable_is_not_abstract():
    assert not inspect.isabstract(co2::Variable)


def test_co2::variable_constructor_exists():
    assert callable(co2::Variable.__init__)


def test_co2::variable_constructor_args():
    sig = inspect.signature(co2::Variable.__init__)
    params = list(sig.parameters.keys())



def test_co2::contractdefinition_is_not_abstract():
    assert not inspect.isabstract(co2::ContractDefinition)


def test_co2::contractdefinition_constructor_exists():
    assert callable(co2::ContractDefinition.__init__)


def test_co2::contractdefinition_constructor_args():
    sig = inspect.signature(co2::ContractDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_co2::contractdefinition_has_name():
    assert hasattr(co2::ContractDefinition, "name")
    descriptor = None
    for klass in co2::ContractDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_co2::processdefinition_is_not_abstract():
    assert not inspect.isabstract(co2::ProcessDefinition)


def test_co2::processdefinition_constructor_exists():
    assert callable(co2::ProcessDefinition.__init__)


def test_co2::processdefinition_constructor_args():
    sig = inspect.signature(co2::ProcessDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "withoutRestrictions" in params, "Missing parameter 'withoutRestrictions'"

def test_co2::processdefinition_has_name():
    assert hasattr(co2::ProcessDefinition, "name")
    descriptor = None
    for klass in co2::ProcessDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_co2::processdefinition_has_withoutRestrictions():
    assert hasattr(co2::ProcessDefinition, "withoutRestrictions")
    descriptor = None
    for klass in co2::ProcessDefinition.__mro__:
        if "withoutRestrictions" in klass.__dict__:
            descriptor = klass.__dict__["withoutRestrictions"]
            break
    assert isinstance(descriptor, property)



def test_co2::import_is_not_abstract():
    assert not inspect.isabstract(co2::Import)


def test_co2::import_constructor_exists():
    assert callable(co2::Import.__init__)


def test_co2::import_constructor_args():
    sig = inspect.signature(co2::Import.__init__)
    params = list(sig.parameters.keys())
    assert "importedNamespace" in params, "Missing parameter 'importedNamespace'"

def test_co2::import_has_importedNamespace():
    assert hasattr(co2::Import, "importedNamespace")
    descriptor = None
    for klass in co2::Import.__mro__:
        if "importedNamespace" in klass.__dict__:
            descriptor = klass.__dict__["importedNamespace"]
            break
    assert isinstance(descriptor, property)



def test_co2::contractsandprocessesdeclaration_is_not_abstract():
    assert not inspect.isabstract(co2::ContractsAndProcessesDeclaration)


def test_co2::contractsandprocessesdeclaration_constructor_exists():
    assert callable(co2::ContractsAndProcessesDeclaration.__init__)


def test_co2::contractsandprocessesdeclaration_constructor_args():
    sig = inspect.signature(co2::ContractsAndProcessesDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_co2::honestydeclaration_is_not_abstract():
    assert not inspect.isabstract(co2::HonestyDeclaration)


def test_co2::honestydeclaration_constructor_exists():
    assert callable(co2::HonestyDeclaration.__init__)


def test_co2::honestydeclaration_constructor_args():
    sig = inspect.signature(co2::HonestyDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_co2::processcall_is_not_abstract():
    assert not inspect.isabstract(co2::ProcessCall)


def test_co2::processcall_constructor_exists():
    assert callable(co2::ProcessCall.__init__)


def test_co2::processcall_constructor_args():
    sig = inspect.signature(co2::ProcessCall.__init__)
    params = list(sig.parameters.keys())



def test_co2::expression_is_not_abstract():
    assert not inspect.isabstract(co2::Expression)


def test_co2::expression_constructor_exists():
    assert callable(co2::Expression.__init__)


def test_co2::expression_constructor_args():
    sig = inspect.signature(co2::Expression.__init__)
    params = list(sig.parameters.keys())



def test_co2::ifthenelse_is_not_abstract():
    assert not inspect.isabstract(co2::IfThenElse)


def test_co2::ifthenelse_constructor_exists():
    assert callable(co2::IfThenElse.__init__)


def test_co2::ifthenelse_constructor_args():
    sig = inspect.signature(co2::IfThenElse.__init__)
    params = list(sig.parameters.keys())



def test_co2::prefix_is_not_abstract():
    assert not inspect.isabstract(co2::Prefix)


def test_co2::prefix_constructor_exists():
    assert callable(co2::Prefix.__init__)


def test_co2::prefix_constructor_args():
    sig = inspect.signature(co2::Prefix.__init__)
    params = list(sig.parameters.keys())



def test_co2::sum_is_not_abstract():
    assert not inspect.isabstract(co2::Sum)


def test_co2::sum_constructor_exists():
    assert callable(co2::Sum.__init__)


def test_co2::sum_constructor_args():
    sig = inspect.signature(co2::Sum.__init__)
    params = list(sig.parameters.keys())



def test_co2::emptyprocess_is_not_abstract():
    assert not inspect.isabstract(co2::EmptyProcess)


def test_co2::emptyprocess_constructor_exists():
    assert callable(co2::EmptyProcess.__init__)


def test_co2::emptyprocess_constructor_args():
    sig = inspect.signature(co2::EmptyProcess.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_co2::emptyprocess_has_value():
    assert hasattr(co2::EmptyProcess, "value")
    descriptor = None
    for klass in co2::EmptyProcess.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_co2::process_is_not_abstract():
    assert not inspect.isabstract(co2::Process)


def test_co2::process_constructor_exists():
    assert callable(co2::Process.__init__)


def test_co2::process_constructor_args():
    sig = inspect.signature(co2::Process.__init__)
    params = list(sig.parameters.keys())



def test_co2::delimitedprocess_is_not_abstract():
    assert not inspect.isabstract(co2::DelimitedProcess)


def test_co2::delimitedprocess_constructor_exists():
    assert callable(co2::DelimitedProcess.__init__)


def test_co2::delimitedprocess_constructor_args():
    sig = inspect.signature(co2::DelimitedProcess.__init__)
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
Process_strategy = st.builds(
    Process,
)
co2::PackageDeclaration_strategy = st.builds(
    co2::PackageDeclaration,
    single=
        st.booleans(),
    name=
        safe_text
)
co2::CO2System_strategy = st.builds(
    co2::CO2System,
)
Placeholder_strategy = st.builds(
    Placeholder,
)
co2::IntPlaceholder_strategy = st.builds(
    co2::IntPlaceholder,
)
ActionType_strategy = st.builds(
    ActionType,
)
co2::StringActionType_strategy = st.builds(
    co2::StringActionType,
)
co2::IntActionType_strategy = st.builds(
    co2::IntActionType,
)
co2::UnitActionType_strategy = st.builds(
    co2::UnitActionType,
)
Type_strategy = st.builds(
    Type,
)
co2::StringType_strategy = st.builds(
    co2::StringType,
)
co2::SessionType_strategy = st.builds(
    co2::SessionType,
)
co2::BooleanType_strategy = st.builds(
    co2::BooleanType,
)
co2::IntType_strategy = st.builds(
    co2::IntType,
)
co2::StringPlaceholder_strategy = st.builds(
    co2::StringPlaceholder,
)
co2::BoolPlaceholder_strategy = st.builds(
    co2::BoolPlaceholder,
)
co2::RetractedProcess_strategy = st.builds(
    co2::RetractedProcess,
)
Action_strategy = st.builds(
    Action,
)
co2::ActionType_strategy = st.builds(
    co2::ActionType,
    value=
        safe_text
)
co2::Action_strategy = st.builds(
    co2::Action,
    name=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
co2::Comparison_strategy = st.builds(
    co2::Comparison,
    op=
        safe_text
)
co2::Plus_strategy = st.builds(
    co2::Plus,
)
co2::BooleanNegation_strategy = st.builds(
    co2::BooleanNegation,
)
co2::VariableReference_strategy = st.builds(
    co2::VariableReference,
)
co2::ArithmeticSigned_strategy = st.builds(
    co2::ArithmeticSigned,
)
co2::Equals_strategy = st.builds(
    co2::Equals,
    op=
        safe_text
)
co2::MultiOrDiv_strategy = st.builds(
    co2::MultiOrDiv,
    op=
        safe_text
)
co2::Minus_strategy = st.builds(
    co2::Minus,
)
co2::OrExpression_strategy = st.builds(
    co2::OrExpression,
)
co2::StringLiteral_strategy = st.builds(
    co2::StringLiteral,
    value=
        safe_text
)
co2::AndExpression_strategy = st.builds(
    co2::AndExpression,
)
co2::NumberLiteral_strategy = st.builds(
    co2::NumberLiteral,
    value=
        st.integers()
)
co2::Case_strategy = st.builds(
    co2::Case,
)
co2::SwitchCase_strategy = st.builds(
    co2::SwitchCase,
    default=
        st.booleans()
)
Contract_strategy = st.builds(
    Contract,
)
co2::ContractReference_strategy = st.builds(
    co2::ContractReference,
)
co2::IntSum_strategy = st.builds(
    co2::IntSum,
)
co2::ExtSum_strategy = st.builds(
    co2::ExtSum,
)
co2::EmptyContract_strategy = st.builds(
    co2::EmptyContract,
    value=
        safe_text
)
VariableDeclaration_strategy = st.builds(
    VariableDeclaration,
)
co2::Type_strategy = st.builds(
    co2::Type,
    value=
        safe_text
)
co2::Placeholder_strategy = st.builds(
    co2::Placeholder,
)
co2::BooleanLiteral_strategy = st.builds(
    co2::BooleanLiteral,
    value=
        safe_text
)
co2::TellAndWait_strategy = st.builds(
    co2::TellAndWait,
    timeout=
        st.booleans()
)
co2::Session_strategy = st.builds(
    co2::Session,
)
co2::TellAndReturn_strategy = st.builds(
    co2::TellAndReturn,
)
co2::ExtAction_strategy = st.builds(
    co2::ExtAction,
)
co2::Input_strategy = st.builds(
    co2::Input,
)
ReceiveGroup_strategy = st.builds(
    ReceiveGroup,
)
co2::Receive_strategy = st.builds(
    co2::Receive,
    timeout=
        st.booleans()
)
co2::ReceiveGroup_strategy = st.builds(
    co2::ReceiveGroup,
)
SendGroup_strategy = st.builds(
    SendGroup,
)
co2::Send_strategy = st.builds(
    co2::Send,
)
co2::SendGroup_strategy = st.builds(
    co2::SendGroup,
)
co2::TimeoutProcess_strategy = st.builds(
    co2::TimeoutProcess,
)
co2::IntAction_strategy = st.builds(
    co2::IntAction,
)
co2::Contract_strategy = st.builds(
    co2::Contract,
)
co2::VariableDeclaration_strategy = st.builds(
    co2::VariableDeclaration,
    name=
        safe_text
)
Prefix_strategy = st.builds(
    Prefix,
)
co2::Tau_strategy = st.builds(
    co2::Tau,
)
co2::DoInput_strategy = st.builds(
    co2::DoInput,
)
co2::Retract_strategy = st.builds(
    co2::Retract,
)
co2::Ask_strategy = st.builds(
    co2::Ask,
    formula=
        safe_text
)
co2::DoOutput_strategy = st.builds(
    co2::DoOutput,
)
co2::Tell_strategy = st.builds(
    co2::Tell,
)
co2::ParallelProcesses_strategy = st.builds(
    co2::ParallelProcesses,
)
co2::Variable_strategy = st.builds(
    co2::Variable,
)
co2::ContractDefinition_strategy = st.builds(
    co2::ContractDefinition,
    name=
        safe_text
)
co2::ProcessDefinition_strategy = st.builds(
    co2::ProcessDefinition,
    name=
        safe_text,
    withoutRestrictions=
        st.booleans()
)
co2::Import_strategy = st.builds(
    co2::Import,
    importedNamespace=
        safe_text
)
co2::ContractsAndProcessesDeclaration_strategy = st.builds(
    co2::ContractsAndProcessesDeclaration,
)
co2::HonestyDeclaration_strategy = st.builds(
    co2::HonestyDeclaration,
)
co2::ProcessCall_strategy = st.builds(
    co2::ProcessCall,
)
co2::Expression_strategy = st.builds(
    co2::Expression,
)
co2::IfThenElse_strategy = st.builds(
    co2::IfThenElse,
)
co2::Prefix_strategy = st.builds(
    co2::Prefix,
)
co2::Sum_strategy = st.builds(
    co2::Sum,
)
co2::EmptyProcess_strategy = st.builds(
    co2::EmptyProcess,
    value=
        safe_text
)
co2::Process_strategy = st.builds(
    co2::Process,
)
co2::DelimitedProcess_strategy = st.builds(
    co2::DelimitedProcess,
)

@given(instance=Process_strategy)
@settings(max_examples=50)
def test_process_instantiation(instance):
    assert isinstance(instance, Process)

@given(instance=co2::PackageDeclaration_strategy)
@settings(max_examples=50)
def test_co2::packagedeclaration_instantiation(instance):
    assert isinstance(instance, co2::PackageDeclaration)

@given(instance=co2::PackageDeclaration_strategy)
def test_co2::packagedeclaration_single_type(instance):
    assert isinstance(instance.single, bool)


@given(instance=co2::PackageDeclaration_strategy)
def test_co2::packagedeclaration_single_setter(instance):
    original = instance.single
    instance.single = original
    assert instance.single == original

@given(instance=co2::PackageDeclaration_strategy)
def test_co2::packagedeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=co2::PackageDeclaration_strategy)
def test_co2::packagedeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=co2::CO2System_strategy)
@settings(max_examples=50)
def test_co2::co2system_instantiation(instance):
    assert isinstance(instance, co2::CO2System)

@given(instance=Placeholder_strategy)
@settings(max_examples=50)
def test_placeholder_instantiation(instance):
    assert isinstance(instance, Placeholder)

@given(instance=co2::IntPlaceholder_strategy)
@settings(max_examples=50)
def test_co2::intplaceholder_instantiation(instance):
    assert isinstance(instance, co2::IntPlaceholder)

@given(instance=ActionType_strategy)
@settings(max_examples=50)
def test_actiontype_instantiation(instance):
    assert isinstance(instance, ActionType)

@given(instance=co2::StringActionType_strategy)
@settings(max_examples=50)
def test_co2::stringactiontype_instantiation(instance):
    assert isinstance(instance, co2::StringActionType)

@given(instance=co2::IntActionType_strategy)
@settings(max_examples=50)
def test_co2::intactiontype_instantiation(instance):
    assert isinstance(instance, co2::IntActionType)

@given(instance=co2::UnitActionType_strategy)
@settings(max_examples=50)
def test_co2::unitactiontype_instantiation(instance):
    assert isinstance(instance, co2::UnitActionType)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=co2::StringType_strategy)
@settings(max_examples=50)
def test_co2::stringtype_instantiation(instance):
    assert isinstance(instance, co2::StringType)

@given(instance=co2::SessionType_strategy)
@settings(max_examples=50)
def test_co2::sessiontype_instantiation(instance):
    assert isinstance(instance, co2::SessionType)

@given(instance=co2::BooleanType_strategy)
@settings(max_examples=50)
def test_co2::booleantype_instantiation(instance):
    assert isinstance(instance, co2::BooleanType)

@given(instance=co2::IntType_strategy)
@settings(max_examples=50)
def test_co2::inttype_instantiation(instance):
    assert isinstance(instance, co2::IntType)

@given(instance=co2::StringPlaceholder_strategy)
@settings(max_examples=50)
def test_co2::stringplaceholder_instantiation(instance):
    assert isinstance(instance, co2::StringPlaceholder)

@given(instance=co2::BoolPlaceholder_strategy)
@settings(max_examples=50)
def test_co2::boolplaceholder_instantiation(instance):
    assert isinstance(instance, co2::BoolPlaceholder)

@given(instance=co2::RetractedProcess_strategy)
@settings(max_examples=50)
def test_co2::retractedprocess_instantiation(instance):
    assert isinstance(instance, co2::RetractedProcess)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=co2::ActionType_strategy)
@settings(max_examples=50)
def test_co2::actiontype_instantiation(instance):
    assert isinstance(instance, co2::ActionType)

@given(instance=co2::ActionType_strategy)
def test_co2::actiontype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=co2::ActionType_strategy)
def test_co2::actiontype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2::Action_strategy)
@settings(max_examples=50)
def test_co2::action_instantiation(instance):
    assert isinstance(instance, co2::Action)

@given(instance=co2::Action_strategy)
def test_co2::action_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=co2::Action_strategy)
def test_co2::action_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=co2::Comparison_strategy)
@settings(max_examples=50)
def test_co2::comparison_instantiation(instance):
    assert isinstance(instance, co2::Comparison)

@given(instance=co2::Comparison_strategy)
def test_co2::comparison_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=co2::Comparison_strategy)
def test_co2::comparison_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=co2::Plus_strategy)
@settings(max_examples=50)
def test_co2::plus_instantiation(instance):
    assert isinstance(instance, co2::Plus)

@given(instance=co2::BooleanNegation_strategy)
@settings(max_examples=50)
def test_co2::booleannegation_instantiation(instance):
    assert isinstance(instance, co2::BooleanNegation)

@given(instance=co2::VariableReference_strategy)
@settings(max_examples=50)
def test_co2::variablereference_instantiation(instance):
    assert isinstance(instance, co2::VariableReference)

@given(instance=co2::ArithmeticSigned_strategy)
@settings(max_examples=50)
def test_co2::arithmeticsigned_instantiation(instance):
    assert isinstance(instance, co2::ArithmeticSigned)

@given(instance=co2::Equals_strategy)
@settings(max_examples=50)
def test_co2::equals_instantiation(instance):
    assert isinstance(instance, co2::Equals)

@given(instance=co2::Equals_strategy)
def test_co2::equals_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=co2::Equals_strategy)
def test_co2::equals_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=co2::MultiOrDiv_strategy)
@settings(max_examples=50)
def test_co2::multiordiv_instantiation(instance):
    assert isinstance(instance, co2::MultiOrDiv)

@given(instance=co2::MultiOrDiv_strategy)
def test_co2::multiordiv_op_type(instance):
    assert isinstance(instance.op, str)


@given(instance=co2::MultiOrDiv_strategy)
def test_co2::multiordiv_op_setter(instance):
    original = instance.op
    instance.op = original
    assert instance.op == original

@given(instance=co2::Minus_strategy)
@settings(max_examples=50)
def test_co2::minus_instantiation(instance):
    assert isinstance(instance, co2::Minus)

@given(instance=co2::OrExpression_strategy)
@settings(max_examples=50)
def test_co2::orexpression_instantiation(instance):
    assert isinstance(instance, co2::OrExpression)

@given(instance=co2::StringLiteral_strategy)
@settings(max_examples=50)
def test_co2::stringliteral_instantiation(instance):
    assert isinstance(instance, co2::StringLiteral)

@given(instance=co2::StringLiteral_strategy)
def test_co2::stringliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=co2::StringLiteral_strategy)
def test_co2::stringliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2::AndExpression_strategy)
@settings(max_examples=50)
def test_co2::andexpression_instantiation(instance):
    assert isinstance(instance, co2::AndExpression)

@given(instance=co2::NumberLiteral_strategy)
@settings(max_examples=50)
def test_co2::numberliteral_instantiation(instance):
    assert isinstance(instance, co2::NumberLiteral)

@given(instance=co2::NumberLiteral_strategy)
def test_co2::numberliteral_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=co2::NumberLiteral_strategy)
def test_co2::numberliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2::Case_strategy)
@settings(max_examples=50)
def test_co2::case_instantiation(instance):
    assert isinstance(instance, co2::Case)

@given(instance=co2::SwitchCase_strategy)
@settings(max_examples=50)
def test_co2::switchcase_instantiation(instance):
    assert isinstance(instance, co2::SwitchCase)

@given(instance=co2::SwitchCase_strategy)
def test_co2::switchcase_default_type(instance):
    assert isinstance(instance.default, bool)


@given(instance=co2::SwitchCase_strategy)
def test_co2::switchcase_default_setter(instance):
    original = instance.default
    instance.default = original
    assert instance.default == original

@given(instance=Contract_strategy)
@settings(max_examples=50)
def test_contract_instantiation(instance):
    assert isinstance(instance, Contract)

@given(instance=co2::ContractReference_strategy)
@settings(max_examples=50)
def test_co2::contractreference_instantiation(instance):
    assert isinstance(instance, co2::ContractReference)

@given(instance=co2::IntSum_strategy)
@settings(max_examples=50)
def test_co2::intsum_instantiation(instance):
    assert isinstance(instance, co2::IntSum)

@given(instance=co2::ExtSum_strategy)
@settings(max_examples=50)
def test_co2::extsum_instantiation(instance):
    assert isinstance(instance, co2::ExtSum)

@given(instance=co2::EmptyContract_strategy)
@settings(max_examples=50)
def test_co2::emptycontract_instantiation(instance):
    assert isinstance(instance, co2::EmptyContract)

@given(instance=co2::EmptyContract_strategy)
def test_co2::emptycontract_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=co2::EmptyContract_strategy)
def test_co2::emptycontract_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=VariableDeclaration_strategy)
@settings(max_examples=50)
def test_variabledeclaration_instantiation(instance):
    assert isinstance(instance, VariableDeclaration)

@given(instance=co2::Type_strategy)
@settings(max_examples=50)
def test_co2::type_instantiation(instance):
    assert isinstance(instance, co2::Type)

@given(instance=co2::Type_strategy)
def test_co2::type_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=co2::Type_strategy)
def test_co2::type_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2::Placeholder_strategy)
@settings(max_examples=50)
def test_co2::placeholder_instantiation(instance):
    assert isinstance(instance, co2::Placeholder)

@given(instance=co2::BooleanLiteral_strategy)
@settings(max_examples=50)
def test_co2::booleanliteral_instantiation(instance):
    assert isinstance(instance, co2::BooleanLiteral)

@given(instance=co2::BooleanLiteral_strategy)
def test_co2::booleanliteral_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=co2::BooleanLiteral_strategy)
def test_co2::booleanliteral_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2::TellAndWait_strategy)
@settings(max_examples=50)
def test_co2::tellandwait_instantiation(instance):
    assert isinstance(instance, co2::TellAndWait)

@given(instance=co2::TellAndWait_strategy)
def test_co2::tellandwait_timeout_type(instance):
    assert isinstance(instance.timeout, bool)


@given(instance=co2::TellAndWait_strategy)
def test_co2::tellandwait_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=co2::Session_strategy)
@settings(max_examples=50)
def test_co2::session_instantiation(instance):
    assert isinstance(instance, co2::Session)

@given(instance=co2::TellAndReturn_strategy)
@settings(max_examples=50)
def test_co2::tellandreturn_instantiation(instance):
    assert isinstance(instance, co2::TellAndReturn)

@given(instance=co2::ExtAction_strategy)
@settings(max_examples=50)
def test_co2::extaction_instantiation(instance):
    assert isinstance(instance, co2::ExtAction)

@given(instance=co2::Input_strategy)
@settings(max_examples=50)
def test_co2::input_instantiation(instance):
    assert isinstance(instance, co2::Input)

@given(instance=ReceiveGroup_strategy)
@settings(max_examples=50)
def test_receivegroup_instantiation(instance):
    assert isinstance(instance, ReceiveGroup)

@given(instance=co2::Receive_strategy)
@settings(max_examples=50)
def test_co2::receive_instantiation(instance):
    assert isinstance(instance, co2::Receive)

@given(instance=co2::Receive_strategy)
def test_co2::receive_timeout_type(instance):
    assert isinstance(instance.timeout, bool)


@given(instance=co2::Receive_strategy)
def test_co2::receive_timeout_setter(instance):
    original = instance.timeout
    instance.timeout = original
    assert instance.timeout == original

@given(instance=co2::ReceiveGroup_strategy)
@settings(max_examples=50)
def test_co2::receivegroup_instantiation(instance):
    assert isinstance(instance, co2::ReceiveGroup)

@given(instance=SendGroup_strategy)
@settings(max_examples=50)
def test_sendgroup_instantiation(instance):
    assert isinstance(instance, SendGroup)

@given(instance=co2::Send_strategy)
@settings(max_examples=50)
def test_co2::send_instantiation(instance):
    assert isinstance(instance, co2::Send)

@given(instance=co2::SendGroup_strategy)
@settings(max_examples=50)
def test_co2::sendgroup_instantiation(instance):
    assert isinstance(instance, co2::SendGroup)

@given(instance=co2::TimeoutProcess_strategy)
@settings(max_examples=50)
def test_co2::timeoutprocess_instantiation(instance):
    assert isinstance(instance, co2::TimeoutProcess)

@given(instance=co2::IntAction_strategy)
@settings(max_examples=50)
def test_co2::intaction_instantiation(instance):
    assert isinstance(instance, co2::IntAction)

@given(instance=co2::Contract_strategy)
@settings(max_examples=50)
def test_co2::contract_instantiation(instance):
    assert isinstance(instance, co2::Contract)

@given(instance=co2::VariableDeclaration_strategy)
@settings(max_examples=50)
def test_co2::variabledeclaration_instantiation(instance):
    assert isinstance(instance, co2::VariableDeclaration)

@given(instance=co2::VariableDeclaration_strategy)
def test_co2::variabledeclaration_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=co2::VariableDeclaration_strategy)
def test_co2::variabledeclaration_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Prefix_strategy)
@settings(max_examples=50)
def test_prefix_instantiation(instance):
    assert isinstance(instance, Prefix)

@given(instance=co2::Tau_strategy)
@settings(max_examples=50)
def test_co2::tau_instantiation(instance):
    assert isinstance(instance, co2::Tau)

@given(instance=co2::DoInput_strategy)
@settings(max_examples=50)
def test_co2::doinput_instantiation(instance):
    assert isinstance(instance, co2::DoInput)

@given(instance=co2::Retract_strategy)
@settings(max_examples=50)
def test_co2::retract_instantiation(instance):
    assert isinstance(instance, co2::Retract)

@given(instance=co2::Ask_strategy)
@settings(max_examples=50)
def test_co2::ask_instantiation(instance):
    assert isinstance(instance, co2::Ask)

@given(instance=co2::Ask_strategy)
def test_co2::ask_formula_type(instance):
    assert isinstance(instance.formula, str)


@given(instance=co2::Ask_strategy)
def test_co2::ask_formula_setter(instance):
    original = instance.formula
    instance.formula = original
    assert instance.formula == original

@given(instance=co2::DoOutput_strategy)
@settings(max_examples=50)
def test_co2::dooutput_instantiation(instance):
    assert isinstance(instance, co2::DoOutput)

@given(instance=co2::Tell_strategy)
@settings(max_examples=50)
def test_co2::tell_instantiation(instance):
    assert isinstance(instance, co2::Tell)

@given(instance=co2::ParallelProcesses_strategy)
@settings(max_examples=50)
def test_co2::parallelprocesses_instantiation(instance):
    assert isinstance(instance, co2::ParallelProcesses)

@given(instance=co2::Variable_strategy)
@settings(max_examples=50)
def test_co2::variable_instantiation(instance):
    assert isinstance(instance, co2::Variable)

@given(instance=co2::ContractDefinition_strategy)
@settings(max_examples=50)
def test_co2::contractdefinition_instantiation(instance):
    assert isinstance(instance, co2::ContractDefinition)

@given(instance=co2::ContractDefinition_strategy)
def test_co2::contractdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=co2::ContractDefinition_strategy)
def test_co2::contractdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=co2::ProcessDefinition_strategy)
@settings(max_examples=50)
def test_co2::processdefinition_instantiation(instance):
    assert isinstance(instance, co2::ProcessDefinition)

@given(instance=co2::ProcessDefinition_strategy)
def test_co2::processdefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=co2::ProcessDefinition_strategy)
def test_co2::processdefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=co2::ProcessDefinition_strategy)
def test_co2::processdefinition_withoutRestrictions_type(instance):
    assert isinstance(instance.withoutRestrictions, bool)


@given(instance=co2::ProcessDefinition_strategy)
def test_co2::processdefinition_withoutRestrictions_setter(instance):
    original = instance.withoutRestrictions
    instance.withoutRestrictions = original
    assert instance.withoutRestrictions == original

@given(instance=co2::Import_strategy)
@settings(max_examples=50)
def test_co2::import_instantiation(instance):
    assert isinstance(instance, co2::Import)

@given(instance=co2::Import_strategy)
def test_co2::import_importedNamespace_type(instance):
    assert isinstance(instance.importedNamespace, str)


@given(instance=co2::Import_strategy)
def test_co2::import_importedNamespace_setter(instance):
    original = instance.importedNamespace
    instance.importedNamespace = original
    assert instance.importedNamespace == original

@given(instance=co2::ContractsAndProcessesDeclaration_strategy)
@settings(max_examples=50)
def test_co2::contractsandprocessesdeclaration_instantiation(instance):
    assert isinstance(instance, co2::ContractsAndProcessesDeclaration)

@given(instance=co2::HonestyDeclaration_strategy)
@settings(max_examples=50)
def test_co2::honestydeclaration_instantiation(instance):
    assert isinstance(instance, co2::HonestyDeclaration)

@given(instance=co2::ProcessCall_strategy)
@settings(max_examples=50)
def test_co2::processcall_instantiation(instance):
    assert isinstance(instance, co2::ProcessCall)

@given(instance=co2::Expression_strategy)
@settings(max_examples=50)
def test_co2::expression_instantiation(instance):
    assert isinstance(instance, co2::Expression)

@given(instance=co2::IfThenElse_strategy)
@settings(max_examples=50)
def test_co2::ifthenelse_instantiation(instance):
    assert isinstance(instance, co2::IfThenElse)

@given(instance=co2::Prefix_strategy)
@settings(max_examples=50)
def test_co2::prefix_instantiation(instance):
    assert isinstance(instance, co2::Prefix)

@given(instance=co2::Sum_strategy)
@settings(max_examples=50)
def test_co2::sum_instantiation(instance):
    assert isinstance(instance, co2::Sum)

@given(instance=co2::EmptyProcess_strategy)
@settings(max_examples=50)
def test_co2::emptyprocess_instantiation(instance):
    assert isinstance(instance, co2::EmptyProcess)

@given(instance=co2::EmptyProcess_strategy)
def test_co2::emptyprocess_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=co2::EmptyProcess_strategy)
def test_co2::emptyprocess_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=co2::Process_strategy)
@settings(max_examples=50)
def test_co2::process_instantiation(instance):
    assert isinstance(instance, co2::Process)

@given(instance=co2::DelimitedProcess_strategy)
@settings(max_examples=50)
def test_co2::delimitedprocess_instantiation(instance):
    assert isinstance(instance, co2::DelimitedProcess)
