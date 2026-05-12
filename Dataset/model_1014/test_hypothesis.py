import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FSMActions_HALL_Component,
    ActionExpressionElement,
    HALL_FSMActions_GetData,
    HALL_FSMActions_BinaryOperator,
    HALL_FSMActions_UnaryOperator,
    HALL_FSMActions_VarRef,
    HALL_FSMActions_ActionExpressionElement,
    FSMActions_ActionExpressionElement,
    HALL_FSMActions_ActionExpression,
    HALL_FSMActions_DomainPropertySet,
    HALL_FSMActions_MessageInvocation,
    HALL_FSMActions_Let,
    HALL_FSMActions_DomainPropertyGet,
    HALL_FSMActions_Literal,
    HALL_FSMConditions_PreConditionExpressionElement,
    FSMConditions_PreConditionExpressionElement,
    HALL_FSMConditions_PreConditionExpression,
    FSMConditions_HALL_Component,
    PreConditionExpressionElement,
    HALL_FSMConditions_BinaryOperator,
    HALL_FSMConditions_Let,
    HALL_FSMConditions_DomainPropertyGet,
    HALL_FSMConditions_VarRef,
    HALL_FSMConditions_GetState,
    HALL_FSMConditions_UnaryOperator,
    HALL_FSMConditions_GetData,
    HALL_FSMConditions_Literal,
    PosConditionExpressionElement,
    HALL_FSMInstructions_DomainPropertyGet,
    HALL_FSMInstructions_Let,
    HALL_FSMInstructions_Literal,
    HALL_FSMInstructions_VarRef,
    HALL_FSMInstructions_PosConditionExpressionElement,
    FSMInstructions_PosConditionExpressionElement,
    HALL_FSMInstructions_PosConditionExpression,
    TriggerExpressionElement,
    HALL_Trigger_DomainEventFired,
    HALL_Trigger_MessageNotification,
    HALL_Trigger_TriggerExpressionElement,
    HALL_FSMInstructions_SetData,
    HALL_FSMInstructions_SetState,
    HALL_FSMInstructions_GetState,
    FSMInstructions_HALL_Component,
    HALL_FSMInstructions_GetData,
    HALL_FSMInstructions_UnaryOperator,
    HALL_FSMInstructions_BinaryOperator,
    State,
    HALL_FSM_InitialState,
    HALL_FSM_NamedState,
    NamedState,
    InitialState,
    FSM_HALL_Component,
    HALL_FSM_FSM,
    Trigger_TriggerExpressionElement,
    HALL_Trigger_TriggerExpression,
    Transition,
    HALL_FSM_State,
    Trigger_TriggerExpression,
    FSMActions_ActionExpression,
    FSMInstructions_PosConditionExpression,
    FSMConditions_PreConditionExpression,
    HALL_FSM_Transition,
    ActionMessageExpressionElement,
    HALL_Actions_Literal,
    HALL_Actions_Let,
    HALL_Actions_DomainPropertyGet,
    HALL_FSMActions_Enable,
    HALL_Actions_BinaryOperator,
    HALL_Actions_VarRef,
    HALL_Actions_ActionMessageExpressionElement,
    HALL_Actions_Enable,
    HALL_Actions_DomainPropertySet,
    Actions_HALL_Component,
    HALL_Actions_GetData,
    HALL_Actions_UnaryOperator,
    HALL_Actions_MessageInvocation,
    HALL_Actions_GetMessageParameter,
    HALL_Actions_GetMessageData,
    Conditions_HALL_Component,
    PreConditionMessageExpressionElement,
    HALL_Conditions_DomainPropertyGet,
    HALL_Conditions_GetMessageData,
    HALL_Conditions_Literal,
    HALL_Conditions_GetData,
    HALL_Conditions_GetState,
    HALL_Conditions_GetMessageParameter,
    HALL_Conditions_VarRef,
    HALL_Conditions_PreConditionMessageExpressionElement,
    Conditions_PreConditionMessageExpressionElement,
    Actions_ActionMessageExpressionElement,
    HALL_Actions_ActionMessageExpression,
    HALL_Conditions_BinaryOperator,
    HALL_Conditions_UnaryOperator,
    HALL_Conditions_Let,
    HALL_Conditions_PreConditionMessageExpression,
    HALL_Instructions_PosConditionMessageExpression,
    MessageTransition,
    HALL_Messages_MessageState,
    Messages_HALL_Component,
    InitialMessageState,
    NamedMessageState,
    HALL_Messages_MessageHandler,
    Messages_HALL_Data,
    Instructions_HALL_Component,
    PosConditionMessageExpressionElement,
    HALL_Instructions_GetMessageParameter,
    HALL_Instructions_GetData,
    HALL_Instructions_Let,
    HALL_Instructions_SetMessageParameter,
    HALL_Instructions_SetData,
    HALL_Instructions_SetTopDown,
    HALL_Instructions_DomainPropertyGet,
    HALL_Instructions_GetMessageData,
    HALL_Instructions_SetState,
    HALL_Instructions_GetState,
    HALL_Instructions_UnaryOperator,
    HALL_Instructions_BinaryOperator,
    HALL_Instructions_SetMessageData,
    HALL_Instructions_Literal,
    HALL_Instructions_VarRef,
    HALL_Instructions_PosConditionMessageExpressionElement,
    Instructions_PosConditionMessageExpressionElement,
    GeometryData2D,
    Point,
    HALL_Geometry_Point2D,
    HALL_Geometry_Point3D,
    GeometryData3D,
    Point3D,
    HALL_Geometry_Face,
    Point2D,
    Messages_HALL_Parameter,
    Messages_HALL_Model,
    HALL_Messages_MessageDefinition,
    Actions_ActionMessageExpression,
    Instructions_PosConditionMessageExpression,
    Conditions_PreConditionMessageExpression,
    MessageState,
    HALL_Messages_InitialMessageState,
    HALL_Messages_NamedMessageState,
    HALL_Messages_MessageTransition,
    HALL_Geometry_Point,
    HALL_Geometry_AlphaTransparency,
    AlphaTransparency,
    HALL_Geometry_ColorState,
    Face,
    HALL_Geometry_GeometryData,
    Geometry_HALL_VisualObject,
    NormalColors,
    DisabledColors,
    SelectedColors,
    HALL_Geometry_ColorData,
    HALL_Parameter,
    Color,
    HALL_Geometry_RGBColor,
    ColorState,
    HALL_Geometry_SelectedColors,
    HALL_Geometry_DisabledColors,
    HALL_Geometry_NormalColors,
    RGBColor,
    HALL_Geometry_Color,
    MessageDefinition,
    HALL_Goal,
    GeometryData,
    HALL_Geometry_GeometryData3D,
    HALL_Geometry_GeometryData2D,
    ColorData,
    Component,
    HALL_TaskObject,
    HALL_VisualObject,
    HALL_Model,
    HALL_SystemComponent,
    MessageHandler,
    FSM,
    HALL_Data,
    HALL_Component,
    HALL_UserProfile,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_fsmactions_hall_component_is_not_abstract():
    assert not inspect.isabstract(FSMActions_HALL_Component)


def test_fsmactions_hall_component_constructor_exists():
    assert callable(FSMActions_HALL_Component.__init__)


def test_fsmactions_hall_component_constructor_args():
    sig = inspect.signature(FSMActions_HALL_Component.__init__)
    params = list(sig.parameters.keys())



def test_actionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(ActionExpressionElement)


def test_actionexpressionelement_constructor_exists():
    assert callable(ActionExpressionElement.__init__)


def test_actionexpressionelement_constructor_args():
    sig = inspect.signature(ActionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsmactions_getdata_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_GetData)


def test_hall_fsmactions_getdata_constructor_exists():
    assert callable(HALL_FSMActions_GetData.__init__)


def test_hall_fsmactions_getdata_constructor_args():
    sig = inspect.signature(HALL_FSMActions_GetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_fsmactions_getdata_has_field():
    assert hasattr(HALL_FSMActions_GetData, "field")
    descriptor = None
    for klass in HALL_FSMActions_GetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_BinaryOperator)


def test_hall_fsmactions_binaryoperator_constructor_exists():
    assert callable(HALL_FSMActions_BinaryOperator.__init__)


def test_hall_fsmactions_binaryoperator_constructor_args():
    sig = inspect.signature(HALL_FSMActions_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_fsmactions_binaryoperator_has_operatorname():
    assert hasattr(HALL_FSMActions_BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_FSMActions_BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_UnaryOperator)


def test_hall_fsmactions_unaryoperator_constructor_exists():
    assert callable(HALL_FSMActions_UnaryOperator.__init__)


def test_hall_fsmactions_unaryoperator_constructor_args():
    sig = inspect.signature(HALL_FSMActions_UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_fsmactions_unaryoperator_has_operatorname():
    assert hasattr(HALL_FSMActions_UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_FSMActions_UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_varref_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_VarRef)


def test_hall_fsmactions_varref_constructor_exists():
    assert callable(HALL_FSMActions_VarRef.__init__)


def test_hall_fsmactions_varref_constructor_args():
    sig = inspect.signature(HALL_FSMActions_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_hall_fsmactions_varref_has_name():
    assert hasattr(HALL_FSMActions_VarRef, "name")
    descriptor = None
    for klass in HALL_FSMActions_VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hall_fsmactions_varref_has_type():
    assert hasattr(HALL_FSMActions_VarRef, "type")
    descriptor = None
    for klass in HALL_FSMActions_VarRef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_actionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_ActionExpressionElement)


def test_hall_fsmactions_actionexpressionelement_constructor_exists():
    assert callable(HALL_FSMActions_ActionExpressionElement.__init__)


def test_hall_fsmactions_actionexpressionelement_constructor_args():
    sig = inspect.signature(HALL_FSMActions_ActionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_fsmactions_actionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(FSMActions_ActionExpressionElement)


def test_fsmactions_actionexpressionelement_constructor_exists():
    assert callable(FSMActions_ActionExpressionElement.__init__)


def test_fsmactions_actionexpressionelement_constructor_args():
    sig = inspect.signature(FSMActions_ActionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsmactions_actionexpression_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_ActionExpression)


def test_hall_fsmactions_actionexpression_constructor_exists():
    assert callable(HALL_FSMActions_ActionExpression.__init__)


def test_hall_fsmactions_actionexpression_constructor_args():
    sig = inspect.signature(HALL_FSMActions_ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsmactions_domainpropertyset_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_DomainPropertySet)


def test_hall_fsmactions_domainpropertyset_constructor_exists():
    assert callable(HALL_FSMActions_DomainPropertySet.__init__)


def test_hall_fsmactions_domainpropertyset_constructor_args():
    sig = inspect.signature(HALL_FSMActions_DomainPropertySet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsmactions_domainpropertyset_has_name():
    assert hasattr(HALL_FSMActions_DomainPropertySet, "name")
    descriptor = None
    for klass in HALL_FSMActions_DomainPropertySet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_messageinvocation_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_MessageInvocation)


def test_hall_fsmactions_messageinvocation_constructor_exists():
    assert callable(HALL_FSMActions_MessageInvocation.__init__)


def test_hall_fsmactions_messageinvocation_constructor_args():
    sig = inspect.signature(HALL_FSMActions_MessageInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopDown" in params, "Missing parameter 'isTopDown'"
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsmactions_messageinvocation_has_isTopDown():
    assert hasattr(HALL_FSMActions_MessageInvocation, "isTopDown")
    descriptor = None
    for klass in HALL_FSMActions_MessageInvocation.__mro__:
        if "isTopDown" in klass.__dict__:
            descriptor = klass.__dict__["isTopDown"]
            break
    assert isinstance(descriptor, property)

def test_hall_fsmactions_messageinvocation_has_name():
    assert hasattr(HALL_FSMActions_MessageInvocation, "name")
    descriptor = None
    for klass in HALL_FSMActions_MessageInvocation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_let_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_Let)


def test_hall_fsmactions_let_constructor_exists():
    assert callable(HALL_FSMActions_Let.__init__)


def test_hall_fsmactions_let_constructor_args():
    sig = inspect.signature(HALL_FSMActions_Let.__init__)
    params = list(sig.parameters.keys())
    assert "namevar" in params, "Missing parameter 'namevar'"

def test_hall_fsmactions_let_has_namevar():
    assert hasattr(HALL_FSMActions_Let, "namevar")
    descriptor = None
    for klass in HALL_FSMActions_Let.__mro__:
        if "namevar" in klass.__dict__:
            descriptor = klass.__dict__["namevar"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_DomainPropertyGet)


def test_hall_fsmactions_domainpropertyget_constructor_exists():
    assert callable(HALL_FSMActions_DomainPropertyGet.__init__)


def test_hall_fsmactions_domainpropertyget_constructor_args():
    sig = inspect.signature(HALL_FSMActions_DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsmactions_domainpropertyget_has_name():
    assert hasattr(HALL_FSMActions_DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL_FSMActions_DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_literal_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_Literal)


def test_hall_fsmactions_literal_constructor_exists():
    assert callable(HALL_FSMActions_Literal.__init__)


def test_hall_fsmactions_literal_constructor_args():
    sig = inspect.signature(HALL_FSMActions_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall_fsmactions_literal_has_value():
    assert hasattr(HALL_FSMActions_Literal, "value")
    descriptor = None
    for klass in HALL_FSMActions_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmconditions_preconditionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_PreConditionExpressionElement)


def test_hall_fsmconditions_preconditionexpressionelement_constructor_exists():
    assert callable(HALL_FSMConditions_PreConditionExpressionElement.__init__)


def test_hall_fsmconditions_preconditionexpressionelement_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_PreConditionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_fsmconditions_preconditionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(FSMConditions_PreConditionExpressionElement)


def test_fsmconditions_preconditionexpressionelement_constructor_exists():
    assert callable(FSMConditions_PreConditionExpressionElement.__init__)


def test_fsmconditions_preconditionexpressionelement_constructor_args():
    sig = inspect.signature(FSMConditions_PreConditionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsmconditions_preconditionexpression_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_PreConditionExpression)


def test_hall_fsmconditions_preconditionexpression_constructor_exists():
    assert callable(HALL_FSMConditions_PreConditionExpression.__init__)


def test_hall_fsmconditions_preconditionexpression_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_PreConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsmconditions_hall_component_is_not_abstract():
    assert not inspect.isabstract(FSMConditions_HALL_Component)


def test_fsmconditions_hall_component_constructor_exists():
    assert callable(FSMConditions_HALL_Component.__init__)


def test_fsmconditions_hall_component_constructor_args():
    sig = inspect.signature(FSMConditions_HALL_Component.__init__)
    params = list(sig.parameters.keys())



def test_preconditionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(PreConditionExpressionElement)


def test_preconditionexpressionelement_constructor_exists():
    assert callable(PreConditionExpressionElement.__init__)


def test_preconditionexpressionelement_constructor_args():
    sig = inspect.signature(PreConditionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsmconditions_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_BinaryOperator)


def test_hall_fsmconditions_binaryoperator_constructor_exists():
    assert callable(HALL_FSMConditions_BinaryOperator.__init__)


def test_hall_fsmconditions_binaryoperator_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_fsmconditions_binaryoperator_has_operatorname():
    assert hasattr(HALL_FSMConditions_BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_FSMConditions_BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmconditions_let_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_Let)


def test_hall_fsmconditions_let_constructor_exists():
    assert callable(HALL_FSMConditions_Let.__init__)


def test_hall_fsmconditions_let_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_Let.__init__)
    params = list(sig.parameters.keys())
    assert "namevar" in params, "Missing parameter 'namevar'"

def test_hall_fsmconditions_let_has_namevar():
    assert hasattr(HALL_FSMConditions_Let, "namevar")
    descriptor = None
    for klass in HALL_FSMConditions_Let.__mro__:
        if "namevar" in klass.__dict__:
            descriptor = klass.__dict__["namevar"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmconditions_domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_DomainPropertyGet)


def test_hall_fsmconditions_domainpropertyget_constructor_exists():
    assert callable(HALL_FSMConditions_DomainPropertyGet.__init__)


def test_hall_fsmconditions_domainpropertyget_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsmconditions_domainpropertyget_has_name():
    assert hasattr(HALL_FSMConditions_DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL_FSMConditions_DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmconditions_varref_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_VarRef)


def test_hall_fsmconditions_varref_constructor_exists():
    assert callable(HALL_FSMConditions_VarRef.__init__)


def test_hall_fsmconditions_varref_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsmconditions_varref_has_type():
    assert hasattr(HALL_FSMConditions_VarRef, "type")
    descriptor = None
    for klass in HALL_FSMConditions_VarRef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hall_fsmconditions_varref_has_name():
    assert hasattr(HALL_FSMConditions_VarRef, "name")
    descriptor = None
    for klass in HALL_FSMConditions_VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmconditions_getstate_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_GetState)


def test_hall_fsmconditions_getstate_constructor_exists():
    assert callable(HALL_FSMConditions_GetState.__init__)


def test_hall_fsmconditions_getstate_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_GetState.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsmconditions_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_UnaryOperator)


def test_hall_fsmconditions_unaryoperator_constructor_exists():
    assert callable(HALL_FSMConditions_UnaryOperator.__init__)


def test_hall_fsmconditions_unaryoperator_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_fsmconditions_unaryoperator_has_operatorname():
    assert hasattr(HALL_FSMConditions_UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_FSMConditions_UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmconditions_getdata_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_GetData)


def test_hall_fsmconditions_getdata_constructor_exists():
    assert callable(HALL_FSMConditions_GetData.__init__)


def test_hall_fsmconditions_getdata_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_GetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_fsmconditions_getdata_has_field():
    assert hasattr(HALL_FSMConditions_GetData, "field")
    descriptor = None
    for klass in HALL_FSMConditions_GetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmconditions_literal_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMConditions_Literal)


def test_hall_fsmconditions_literal_constructor_exists():
    assert callable(HALL_FSMConditions_Literal.__init__)


def test_hall_fsmconditions_literal_constructor_args():
    sig = inspect.signature(HALL_FSMConditions_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall_fsmconditions_literal_has_value():
    assert hasattr(HALL_FSMConditions_Literal, "value")
    descriptor = None
    for klass in HALL_FSMConditions_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_posconditionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(PosConditionExpressionElement)


def test_posconditionexpressionelement_constructor_exists():
    assert callable(PosConditionExpressionElement.__init__)


def test_posconditionexpressionelement_constructor_args():
    sig = inspect.signature(PosConditionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsminstructions_domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_DomainPropertyGet)


def test_hall_fsminstructions_domainpropertyget_constructor_exists():
    assert callable(HALL_FSMInstructions_DomainPropertyGet.__init__)


def test_hall_fsminstructions_domainpropertyget_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsminstructions_domainpropertyget_has_name():
    assert hasattr(HALL_FSMInstructions_DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL_FSMInstructions_DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_let_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_Let)


def test_hall_fsminstructions_let_constructor_exists():
    assert callable(HALL_FSMInstructions_Let.__init__)


def test_hall_fsminstructions_let_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_Let.__init__)
    params = list(sig.parameters.keys())
    assert "namevar" in params, "Missing parameter 'namevar'"

def test_hall_fsminstructions_let_has_namevar():
    assert hasattr(HALL_FSMInstructions_Let, "namevar")
    descriptor = None
    for klass in HALL_FSMInstructions_Let.__mro__:
        if "namevar" in klass.__dict__:
            descriptor = klass.__dict__["namevar"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_literal_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_Literal)


def test_hall_fsminstructions_literal_constructor_exists():
    assert callable(HALL_FSMInstructions_Literal.__init__)


def test_hall_fsminstructions_literal_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall_fsminstructions_literal_has_value():
    assert hasattr(HALL_FSMInstructions_Literal, "value")
    descriptor = None
    for klass in HALL_FSMInstructions_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_varref_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_VarRef)


def test_hall_fsminstructions_varref_constructor_exists():
    assert callable(HALL_FSMInstructions_VarRef.__init__)


def test_hall_fsminstructions_varref_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsminstructions_varref_has_type():
    assert hasattr(HALL_FSMInstructions_VarRef, "type")
    descriptor = None
    for klass in HALL_FSMInstructions_VarRef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hall_fsminstructions_varref_has_name():
    assert hasattr(HALL_FSMInstructions_VarRef, "name")
    descriptor = None
    for klass in HALL_FSMInstructions_VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_posconditionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_PosConditionExpressionElement)


def test_hall_fsminstructions_posconditionexpressionelement_constructor_exists():
    assert callable(HALL_FSMInstructions_PosConditionExpressionElement.__init__)


def test_hall_fsminstructions_posconditionexpressionelement_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_PosConditionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_fsminstructions_posconditionexpressionelement_is_not_abstract():
    assert not inspect.isabstract(FSMInstructions_PosConditionExpressionElement)


def test_fsminstructions_posconditionexpressionelement_constructor_exists():
    assert callable(FSMInstructions_PosConditionExpressionElement.__init__)


def test_fsminstructions_posconditionexpressionelement_constructor_args():
    sig = inspect.signature(FSMInstructions_PosConditionExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsminstructions_posconditionexpression_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_PosConditionExpression)


def test_hall_fsminstructions_posconditionexpression_constructor_exists():
    assert callable(HALL_FSMInstructions_PosConditionExpression.__init__)


def test_hall_fsminstructions_posconditionexpression_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_PosConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_triggerexpressionelement_is_not_abstract():
    assert not inspect.isabstract(TriggerExpressionElement)


def test_triggerexpressionelement_constructor_exists():
    assert callable(TriggerExpressionElement.__init__)


def test_triggerexpressionelement_constructor_args():
    sig = inspect.signature(TriggerExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_trigger_domaineventfired_is_not_abstract():
    assert not inspect.isabstract(HALL_Trigger_DomainEventFired)


def test_hall_trigger_domaineventfired_constructor_exists():
    assert callable(HALL_Trigger_DomainEventFired.__init__)


def test_hall_trigger_domaineventfired_constructor_args():
    sig = inspect.signature(HALL_Trigger_DomainEventFired.__init__)
    params = list(sig.parameters.keys())



def test_hall_trigger_messagenotification_is_not_abstract():
    assert not inspect.isabstract(HALL_Trigger_MessageNotification)


def test_hall_trigger_messagenotification_constructor_exists():
    assert callable(HALL_Trigger_MessageNotification.__init__)


def test_hall_trigger_messagenotification_constructor_args():
    sig = inspect.signature(HALL_Trigger_MessageNotification.__init__)
    params = list(sig.parameters.keys())



def test_hall_trigger_triggerexpressionelement_is_not_abstract():
    assert not inspect.isabstract(HALL_Trigger_TriggerExpressionElement)


def test_hall_trigger_triggerexpressionelement_constructor_exists():
    assert callable(HALL_Trigger_TriggerExpressionElement.__init__)


def test_hall_trigger_triggerexpressionelement_constructor_args():
    sig = inspect.signature(HALL_Trigger_TriggerExpressionElement.__init__)
    params = list(sig.parameters.keys())
    assert "String" in params, "Missing parameter 'String'"

def test_hall_trigger_triggerexpressionelement_has_String():
    assert hasattr(HALL_Trigger_TriggerExpressionElement, "String")
    descriptor = None
    for klass in HALL_Trigger_TriggerExpressionElement.__mro__:
        if "String" in klass.__dict__:
            descriptor = klass.__dict__["String"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_setdata_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_SetData)


def test_hall_fsminstructions_setdata_constructor_exists():
    assert callable(HALL_FSMInstructions_SetData.__init__)


def test_hall_fsminstructions_setdata_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_SetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_fsminstructions_setdata_has_field():
    assert hasattr(HALL_FSMInstructions_SetData, "field")
    descriptor = None
    for klass in HALL_FSMInstructions_SetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_setstate_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_SetState)


def test_hall_fsminstructions_setstate_constructor_exists():
    assert callable(HALL_FSMInstructions_SetState.__init__)


def test_hall_fsminstructions_setstate_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_SetState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsminstructions_setstate_has_name():
    assert hasattr(HALL_FSMInstructions_SetState, "name")
    descriptor = None
    for klass in HALL_FSMInstructions_SetState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_getstate_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_GetState)


def test_hall_fsminstructions_getstate_constructor_exists():
    assert callable(HALL_FSMInstructions_GetState.__init__)


def test_hall_fsminstructions_getstate_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_GetState.__init__)
    params = list(sig.parameters.keys())



def test_fsminstructions_hall_component_is_not_abstract():
    assert not inspect.isabstract(FSMInstructions_HALL_Component)


def test_fsminstructions_hall_component_constructor_exists():
    assert callable(FSMInstructions_HALL_Component.__init__)


def test_fsminstructions_hall_component_constructor_args():
    sig = inspect.signature(FSMInstructions_HALL_Component.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsminstructions_getdata_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_GetData)


def test_hall_fsminstructions_getdata_constructor_exists():
    assert callable(HALL_FSMInstructions_GetData.__init__)


def test_hall_fsminstructions_getdata_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_GetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_fsminstructions_getdata_has_field():
    assert hasattr(HALL_FSMInstructions_GetData, "field")
    descriptor = None
    for klass in HALL_FSMInstructions_GetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_UnaryOperator)


def test_hall_fsminstructions_unaryoperator_constructor_exists():
    assert callable(HALL_FSMInstructions_UnaryOperator.__init__)


def test_hall_fsminstructions_unaryoperator_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_fsminstructions_unaryoperator_has_operatorname():
    assert hasattr(HALL_FSMInstructions_UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_FSMInstructions_UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsminstructions_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMInstructions_BinaryOperator)


def test_hall_fsminstructions_binaryoperator_constructor_exists():
    assert callable(HALL_FSMInstructions_BinaryOperator.__init__)


def test_hall_fsminstructions_binaryoperator_constructor_args():
    sig = inspect.signature(HALL_FSMInstructions_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_fsminstructions_binaryoperator_has_operatorname():
    assert hasattr(HALL_FSMInstructions_BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_FSMInstructions_BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsm_initialstate_is_not_abstract():
    assert not inspect.isabstract(HALL_FSM_InitialState)


def test_hall_fsm_initialstate_constructor_exists():
    assert callable(HALL_FSM_InitialState.__init__)


def test_hall_fsm_initialstate_constructor_args():
    sig = inspect.signature(HALL_FSM_InitialState.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsm_namedstate_is_not_abstract():
    assert not inspect.isabstract(HALL_FSM_NamedState)


def test_hall_fsm_namedstate_constructor_exists():
    assert callable(HALL_FSM_NamedState.__init__)


def test_hall_fsm_namedstate_constructor_args():
    sig = inspect.signature(HALL_FSM_NamedState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsm_namedstate_has_name():
    assert hasattr(HALL_FSM_NamedState, "name")
    descriptor = None
    for klass in HALL_FSM_NamedState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_namedstate_is_not_abstract():
    assert not inspect.isabstract(NamedState)


def test_namedstate_constructor_exists():
    assert callable(NamedState.__init__)


def test_namedstate_constructor_args():
    sig = inspect.signature(NamedState.__init__)
    params = list(sig.parameters.keys())



def test_initialstate_is_not_abstract():
    assert not inspect.isabstract(InitialState)


def test_initialstate_constructor_exists():
    assert callable(InitialState.__init__)


def test_initialstate_constructor_args():
    sig = inspect.signature(InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm_hall_component_is_not_abstract():
    assert not inspect.isabstract(FSM_HALL_Component)


def test_fsm_hall_component_constructor_exists():
    assert callable(FSM_HALL_Component.__init__)


def test_fsm_hall_component_constructor_args():
    sig = inspect.signature(FSM_HALL_Component.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsm_fsm_is_not_abstract():
    assert not inspect.isabstract(HALL_FSM_FSM)


def test_hall_fsm_fsm_constructor_exists():
    assert callable(HALL_FSM_FSM.__init__)


def test_hall_fsm_fsm_constructor_args():
    sig = inspect.signature(HALL_FSM_FSM.__init__)
    params = list(sig.parameters.keys())



def test_trigger_triggerexpressionelement_is_not_abstract():
    assert not inspect.isabstract(Trigger_TriggerExpressionElement)


def test_trigger_triggerexpressionelement_constructor_exists():
    assert callable(Trigger_TriggerExpressionElement.__init__)


def test_trigger_triggerexpressionelement_constructor_args():
    sig = inspect.signature(Trigger_TriggerExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_trigger_triggerexpression_is_not_abstract():
    assert not inspect.isabstract(HALL_Trigger_TriggerExpression)


def test_hall_trigger_triggerexpression_constructor_exists():
    assert callable(HALL_Trigger_TriggerExpression.__init__)


def test_hall_trigger_triggerexpression_constructor_args():
    sig = inspect.signature(HALL_Trigger_TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsm_state_is_not_abstract():
    assert not inspect.isabstract(HALL_FSM_State)


def test_hall_fsm_state_constructor_exists():
    assert callable(HALL_FSM_State.__init__)


def test_hall_fsm_state_constructor_args():
    sig = inspect.signature(HALL_FSM_State.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"

def test_hall_fsm_state_has_isActive():
    assert hasattr(HALL_FSM_State, "isActive")
    descriptor = None
    for klass in HALL_FSM_State.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)



def test_trigger_triggerexpression_is_not_abstract():
    assert not inspect.isabstract(Trigger_TriggerExpression)


def test_trigger_triggerexpression_constructor_exists():
    assert callable(Trigger_TriggerExpression.__init__)


def test_trigger_triggerexpression_constructor_args():
    sig = inspect.signature(Trigger_TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsmactions_actionexpression_is_not_abstract():
    assert not inspect.isabstract(FSMActions_ActionExpression)


def test_fsmactions_actionexpression_constructor_exists():
    assert callable(FSMActions_ActionExpression.__init__)


def test_fsmactions_actionexpression_constructor_args():
    sig = inspect.signature(FSMActions_ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsminstructions_posconditionexpression_is_not_abstract():
    assert not inspect.isabstract(FSMInstructions_PosConditionExpression)


def test_fsminstructions_posconditionexpression_constructor_exists():
    assert callable(FSMInstructions_PosConditionExpression.__init__)


def test_fsminstructions_posconditionexpression_constructor_args():
    sig = inspect.signature(FSMInstructions_PosConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsmconditions_preconditionexpression_is_not_abstract():
    assert not inspect.isabstract(FSMConditions_PreConditionExpression)


def test_fsmconditions_preconditionexpression_constructor_exists():
    assert callable(FSMConditions_PreConditionExpression.__init__)


def test_fsmconditions_preconditionexpression_constructor_args():
    sig = inspect.signature(FSMConditions_PreConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall_fsm_transition_is_not_abstract():
    assert not inspect.isabstract(HALL_FSM_Transition)


def test_hall_fsm_transition_constructor_exists():
    assert callable(HALL_FSM_Transition.__init__)


def test_hall_fsm_transition_constructor_args():
    sig = inspect.signature(HALL_FSM_Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_fsm_transition_has_name():
    assert hasattr(HALL_FSM_Transition, "name")
    descriptor = None
    for klass in HALL_FSM_Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_actionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(ActionMessageExpressionElement)


def test_actionmessageexpressionelement_constructor_exists():
    assert callable(ActionMessageExpressionElement.__init__)


def test_actionmessageexpressionelement_constructor_args():
    sig = inspect.signature(ActionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_actions_literal_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_Literal)


def test_hall_actions_literal_constructor_exists():
    assert callable(HALL_Actions_Literal.__init__)


def test_hall_actions_literal_constructor_args():
    sig = inspect.signature(HALL_Actions_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall_actions_literal_has_value():
    assert hasattr(HALL_Actions_Literal, "value")
    descriptor = None
    for klass in HALL_Actions_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall_actions_let_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_Let)


def test_hall_actions_let_constructor_exists():
    assert callable(HALL_Actions_Let.__init__)


def test_hall_actions_let_constructor_args():
    sig = inspect.signature(HALL_Actions_Let.__init__)
    params = list(sig.parameters.keys())
    assert "namevar" in params, "Missing parameter 'namevar'"

def test_hall_actions_let_has_namevar():
    assert hasattr(HALL_Actions_Let, "namevar")
    descriptor = None
    for klass in HALL_Actions_Let.__mro__:
        if "namevar" in klass.__dict__:
            descriptor = klass.__dict__["namevar"]
            break
    assert isinstance(descriptor, property)



def test_hall_actions_domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_DomainPropertyGet)


def test_hall_actions_domainpropertyget_constructor_exists():
    assert callable(HALL_Actions_DomainPropertyGet.__init__)


def test_hall_actions_domainpropertyget_constructor_args():
    sig = inspect.signature(HALL_Actions_DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_actions_domainpropertyget_has_name():
    assert hasattr(HALL_Actions_DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL_Actions_DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_fsmactions_enable_is_not_abstract():
    assert not inspect.isabstract(HALL_FSMActions_Enable)


def test_hall_fsmactions_enable_constructor_exists():
    assert callable(HALL_FSMActions_Enable.__init__)


def test_hall_fsmactions_enable_constructor_args():
    sig = inspect.signature(HALL_FSMActions_Enable.__init__)
    params = list(sig.parameters.keys())



def test_hall_actions_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_BinaryOperator)


def test_hall_actions_binaryoperator_constructor_exists():
    assert callable(HALL_Actions_BinaryOperator.__init__)


def test_hall_actions_binaryoperator_constructor_args():
    sig = inspect.signature(HALL_Actions_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_actions_binaryoperator_has_operatorname():
    assert hasattr(HALL_Actions_BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_Actions_BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_actions_varref_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_VarRef)


def test_hall_actions_varref_constructor_exists():
    assert callable(HALL_Actions_VarRef.__init__)


def test_hall_actions_varref_constructor_args():
    sig = inspect.signature(HALL_Actions_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_hall_actions_varref_has_name():
    assert hasattr(HALL_Actions_VarRef, "name")
    descriptor = None
    for klass in HALL_Actions_VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hall_actions_varref_has_type():
    assert hasattr(HALL_Actions_VarRef, "type")
    descriptor = None
    for klass in HALL_Actions_VarRef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hall_actions_actionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_ActionMessageExpressionElement)


def test_hall_actions_actionmessageexpressionelement_constructor_exists():
    assert callable(HALL_Actions_ActionMessageExpressionElement.__init__)


def test_hall_actions_actionmessageexpressionelement_constructor_args():
    sig = inspect.signature(HALL_Actions_ActionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_actions_enable_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_Enable)


def test_hall_actions_enable_constructor_exists():
    assert callable(HALL_Actions_Enable.__init__)


def test_hall_actions_enable_constructor_args():
    sig = inspect.signature(HALL_Actions_Enable.__init__)
    params = list(sig.parameters.keys())



def test_hall_actions_domainpropertyset_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_DomainPropertySet)


def test_hall_actions_domainpropertyset_constructor_exists():
    assert callable(HALL_Actions_DomainPropertySet.__init__)


def test_hall_actions_domainpropertyset_constructor_args():
    sig = inspect.signature(HALL_Actions_DomainPropertySet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_actions_domainpropertyset_has_name():
    assert hasattr(HALL_Actions_DomainPropertySet, "name")
    descriptor = None
    for klass in HALL_Actions_DomainPropertySet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_actions_hall_component_is_not_abstract():
    assert not inspect.isabstract(Actions_HALL_Component)


def test_actions_hall_component_constructor_exists():
    assert callable(Actions_HALL_Component.__init__)


def test_actions_hall_component_constructor_args():
    sig = inspect.signature(Actions_HALL_Component.__init__)
    params = list(sig.parameters.keys())



def test_hall_actions_getdata_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_GetData)


def test_hall_actions_getdata_constructor_exists():
    assert callable(HALL_Actions_GetData.__init__)


def test_hall_actions_getdata_constructor_args():
    sig = inspect.signature(HALL_Actions_GetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_actions_getdata_has_field():
    assert hasattr(HALL_Actions_GetData, "field")
    descriptor = None
    for klass in HALL_Actions_GetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_actions_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_UnaryOperator)


def test_hall_actions_unaryoperator_constructor_exists():
    assert callable(HALL_Actions_UnaryOperator.__init__)


def test_hall_actions_unaryoperator_constructor_args():
    sig = inspect.signature(HALL_Actions_UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_actions_unaryoperator_has_operatorname():
    assert hasattr(HALL_Actions_UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_Actions_UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_actions_messageinvocation_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_MessageInvocation)


def test_hall_actions_messageinvocation_constructor_exists():
    assert callable(HALL_Actions_MessageInvocation.__init__)


def test_hall_actions_messageinvocation_constructor_args():
    sig = inspect.signature(HALL_Actions_MessageInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "isTopDown" in params, "Missing parameter 'isTopDown'"

def test_hall_actions_messageinvocation_has_name():
    assert hasattr(HALL_Actions_MessageInvocation, "name")
    descriptor = None
    for klass in HALL_Actions_MessageInvocation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hall_actions_messageinvocation_has_isTopDown():
    assert hasattr(HALL_Actions_MessageInvocation, "isTopDown")
    descriptor = None
    for klass in HALL_Actions_MessageInvocation.__mro__:
        if "isTopDown" in klass.__dict__:
            descriptor = klass.__dict__["isTopDown"]
            break
    assert isinstance(descriptor, property)



def test_hall_actions_getmessageparameter_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_GetMessageParameter)


def test_hall_actions_getmessageparameter_constructor_exists():
    assert callable(HALL_Actions_GetMessageParameter.__init__)


def test_hall_actions_getmessageparameter_constructor_args():
    sig = inspect.signature(HALL_Actions_GetMessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_actions_getmessageparameter_has_field():
    assert hasattr(HALL_Actions_GetMessageParameter, "field")
    descriptor = None
    for klass in HALL_Actions_GetMessageParameter.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_actions_getmessagedata_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_GetMessageData)


def test_hall_actions_getmessagedata_constructor_exists():
    assert callable(HALL_Actions_GetMessageData.__init__)


def test_hall_actions_getmessagedata_constructor_args():
    sig = inspect.signature(HALL_Actions_GetMessageData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_actions_getmessagedata_has_field():
    assert hasattr(HALL_Actions_GetMessageData, "field")
    descriptor = None
    for klass in HALL_Actions_GetMessageData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_conditions_hall_component_is_not_abstract():
    assert not inspect.isabstract(Conditions_HALL_Component)


def test_conditions_hall_component_constructor_exists():
    assert callable(Conditions_HALL_Component.__init__)


def test_conditions_hall_component_constructor_args():
    sig = inspect.signature(Conditions_HALL_Component.__init__)
    params = list(sig.parameters.keys())



def test_preconditionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(PreConditionMessageExpressionElement)


def test_preconditionmessageexpressionelement_constructor_exists():
    assert callable(PreConditionMessageExpressionElement.__init__)


def test_preconditionmessageexpressionelement_constructor_args():
    sig = inspect.signature(PreConditionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_conditions_domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_DomainPropertyGet)


def test_hall_conditions_domainpropertyget_constructor_exists():
    assert callable(HALL_Conditions_DomainPropertyGet.__init__)


def test_hall_conditions_domainpropertyget_constructor_args():
    sig = inspect.signature(HALL_Conditions_DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_conditions_domainpropertyget_has_name():
    assert hasattr(HALL_Conditions_DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL_Conditions_DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_getmessagedata_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_GetMessageData)


def test_hall_conditions_getmessagedata_constructor_exists():
    assert callable(HALL_Conditions_GetMessageData.__init__)


def test_hall_conditions_getmessagedata_constructor_args():
    sig = inspect.signature(HALL_Conditions_GetMessageData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_conditions_getmessagedata_has_field():
    assert hasattr(HALL_Conditions_GetMessageData, "field")
    descriptor = None
    for klass in HALL_Conditions_GetMessageData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_literal_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_Literal)


def test_hall_conditions_literal_constructor_exists():
    assert callable(HALL_Conditions_Literal.__init__)


def test_hall_conditions_literal_constructor_args():
    sig = inspect.signature(HALL_Conditions_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall_conditions_literal_has_value():
    assert hasattr(HALL_Conditions_Literal, "value")
    descriptor = None
    for klass in HALL_Conditions_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_getdata_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_GetData)


def test_hall_conditions_getdata_constructor_exists():
    assert callable(HALL_Conditions_GetData.__init__)


def test_hall_conditions_getdata_constructor_args():
    sig = inspect.signature(HALL_Conditions_GetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_conditions_getdata_has_field():
    assert hasattr(HALL_Conditions_GetData, "field")
    descriptor = None
    for klass in HALL_Conditions_GetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_getstate_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_GetState)


def test_hall_conditions_getstate_constructor_exists():
    assert callable(HALL_Conditions_GetState.__init__)


def test_hall_conditions_getstate_constructor_args():
    sig = inspect.signature(HALL_Conditions_GetState.__init__)
    params = list(sig.parameters.keys())



def test_hall_conditions_getmessageparameter_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_GetMessageParameter)


def test_hall_conditions_getmessageparameter_constructor_exists():
    assert callable(HALL_Conditions_GetMessageParameter.__init__)


def test_hall_conditions_getmessageparameter_constructor_args():
    sig = inspect.signature(HALL_Conditions_GetMessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_conditions_getmessageparameter_has_field():
    assert hasattr(HALL_Conditions_GetMessageParameter, "field")
    descriptor = None
    for klass in HALL_Conditions_GetMessageParameter.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_varref_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_VarRef)


def test_hall_conditions_varref_constructor_exists():
    assert callable(HALL_Conditions_VarRef.__init__)


def test_hall_conditions_varref_constructor_args():
    sig = inspect.signature(HALL_Conditions_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_hall_conditions_varref_has_name():
    assert hasattr(HALL_Conditions_VarRef, "name")
    descriptor = None
    for klass in HALL_Conditions_VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hall_conditions_varref_has_type():
    assert hasattr(HALL_Conditions_VarRef, "type")
    descriptor = None
    for klass in HALL_Conditions_VarRef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_preconditionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_PreConditionMessageExpressionElement)


def test_hall_conditions_preconditionmessageexpressionelement_constructor_exists():
    assert callable(HALL_Conditions_PreConditionMessageExpressionElement.__init__)


def test_hall_conditions_preconditionmessageexpressionelement_constructor_args():
    sig = inspect.signature(HALL_Conditions_PreConditionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_conditions_preconditionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(Conditions_PreConditionMessageExpressionElement)


def test_conditions_preconditionmessageexpressionelement_constructor_exists():
    assert callable(Conditions_PreConditionMessageExpressionElement.__init__)


def test_conditions_preconditionmessageexpressionelement_constructor_args():
    sig = inspect.signature(Conditions_PreConditionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_actions_actionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(Actions_ActionMessageExpressionElement)


def test_actions_actionmessageexpressionelement_constructor_exists():
    assert callable(Actions_ActionMessageExpressionElement.__init__)


def test_actions_actionmessageexpressionelement_constructor_args():
    sig = inspect.signature(Actions_ActionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_actions_actionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(HALL_Actions_ActionMessageExpression)


def test_hall_actions_actionmessageexpression_constructor_exists():
    assert callable(HALL_Actions_ActionMessageExpression.__init__)


def test_hall_actions_actionmessageexpression_constructor_args():
    sig = inspect.signature(HALL_Actions_ActionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall_conditions_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_BinaryOperator)


def test_hall_conditions_binaryoperator_constructor_exists():
    assert callable(HALL_Conditions_BinaryOperator.__init__)


def test_hall_conditions_binaryoperator_constructor_args():
    sig = inspect.signature(HALL_Conditions_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_conditions_binaryoperator_has_operatorname():
    assert hasattr(HALL_Conditions_BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_Conditions_BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_UnaryOperator)


def test_hall_conditions_unaryoperator_constructor_exists():
    assert callable(HALL_Conditions_UnaryOperator.__init__)


def test_hall_conditions_unaryoperator_constructor_args():
    sig = inspect.signature(HALL_Conditions_UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_conditions_unaryoperator_has_operatorname():
    assert hasattr(HALL_Conditions_UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_Conditions_UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_let_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_Let)


def test_hall_conditions_let_constructor_exists():
    assert callable(HALL_Conditions_Let.__init__)


def test_hall_conditions_let_constructor_args():
    sig = inspect.signature(HALL_Conditions_Let.__init__)
    params = list(sig.parameters.keys())
    assert "namevar" in params, "Missing parameter 'namevar'"

def test_hall_conditions_let_has_namevar():
    assert hasattr(HALL_Conditions_Let, "namevar")
    descriptor = None
    for klass in HALL_Conditions_Let.__mro__:
        if "namevar" in klass.__dict__:
            descriptor = klass.__dict__["namevar"]
            break
    assert isinstance(descriptor, property)



def test_hall_conditions_preconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(HALL_Conditions_PreConditionMessageExpression)


def test_hall_conditions_preconditionmessageexpression_constructor_exists():
    assert callable(HALL_Conditions_PreConditionMessageExpression.__init__)


def test_hall_conditions_preconditionmessageexpression_constructor_args():
    sig = inspect.signature(HALL_Conditions_PreConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall_instructions_posconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_PosConditionMessageExpression)


def test_hall_instructions_posconditionmessageexpression_constructor_exists():
    assert callable(HALL_Instructions_PosConditionMessageExpression.__init__)


def test_hall_instructions_posconditionmessageexpression_constructor_args():
    sig = inspect.signature(HALL_Instructions_PosConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_messagetransition_is_not_abstract():
    assert not inspect.isabstract(MessageTransition)


def test_messagetransition_constructor_exists():
    assert callable(MessageTransition.__init__)


def test_messagetransition_constructor_args():
    sig = inspect.signature(MessageTransition.__init__)
    params = list(sig.parameters.keys())



def test_hall_messages_messagestate_is_not_abstract():
    assert not inspect.isabstract(HALL_Messages_MessageState)


def test_hall_messages_messagestate_constructor_exists():
    assert callable(HALL_Messages_MessageState.__init__)


def test_hall_messages_messagestate_constructor_args():
    sig = inspect.signature(HALL_Messages_MessageState.__init__)
    params = list(sig.parameters.keys())
    assert "isContinue" in params, "Missing parameter 'isContinue'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"

def test_hall_messages_messagestate_has_isContinue():
    assert hasattr(HALL_Messages_MessageState, "isContinue")
    descriptor = None
    for klass in HALL_Messages_MessageState.__mro__:
        if "isContinue" in klass.__dict__:
            descriptor = klass.__dict__["isContinue"]
            break
    assert isinstance(descriptor, property)

def test_hall_messages_messagestate_has_isActive():
    assert hasattr(HALL_Messages_MessageState, "isActive")
    descriptor = None
    for klass in HALL_Messages_MessageState.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_hall_messages_messagestate_has_isEnd():
    assert hasattr(HALL_Messages_MessageState, "isEnd")
    descriptor = None
    for klass in HALL_Messages_MessageState.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)



def test_messages_hall_component_is_not_abstract():
    assert not inspect.isabstract(Messages_HALL_Component)


def test_messages_hall_component_constructor_exists():
    assert callable(Messages_HALL_Component.__init__)


def test_messages_hall_component_constructor_args():
    sig = inspect.signature(Messages_HALL_Component.__init__)
    params = list(sig.parameters.keys())



def test_initialmessagestate_is_not_abstract():
    assert not inspect.isabstract(InitialMessageState)


def test_initialmessagestate_constructor_exists():
    assert callable(InitialMessageState.__init__)


def test_initialmessagestate_constructor_args():
    sig = inspect.signature(InitialMessageState.__init__)
    params = list(sig.parameters.keys())



def test_namedmessagestate_is_not_abstract():
    assert not inspect.isabstract(NamedMessageState)


def test_namedmessagestate_constructor_exists():
    assert callable(NamedMessageState.__init__)


def test_namedmessagestate_constructor_args():
    sig = inspect.signature(NamedMessageState.__init__)
    params = list(sig.parameters.keys())



def test_hall_messages_messagehandler_is_not_abstract():
    assert not inspect.isabstract(HALL_Messages_MessageHandler)


def test_hall_messages_messagehandler_constructor_exists():
    assert callable(HALL_Messages_MessageHandler.__init__)


def test_hall_messages_messagehandler_constructor_args():
    sig = inspect.signature(HALL_Messages_MessageHandler.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_messages_messagehandler_has_name():
    assert hasattr(HALL_Messages_MessageHandler, "name")
    descriptor = None
    for klass in HALL_Messages_MessageHandler.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_messages_hall_data_is_not_abstract():
    assert not inspect.isabstract(Messages_HALL_Data)


def test_messages_hall_data_constructor_exists():
    assert callable(Messages_HALL_Data.__init__)


def test_messages_hall_data_constructor_args():
    sig = inspect.signature(Messages_HALL_Data.__init__)
    params = list(sig.parameters.keys())



def test_instructions_hall_component_is_not_abstract():
    assert not inspect.isabstract(Instructions_HALL_Component)


def test_instructions_hall_component_constructor_exists():
    assert callable(Instructions_HALL_Component.__init__)


def test_instructions_hall_component_constructor_args():
    sig = inspect.signature(Instructions_HALL_Component.__init__)
    params = list(sig.parameters.keys())



def test_posconditionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(PosConditionMessageExpressionElement)


def test_posconditionmessageexpressionelement_constructor_exists():
    assert callable(PosConditionMessageExpressionElement.__init__)


def test_posconditionmessageexpressionelement_constructor_args():
    sig = inspect.signature(PosConditionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_hall_instructions_getmessageparameter_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_GetMessageParameter)


def test_hall_instructions_getmessageparameter_constructor_exists():
    assert callable(HALL_Instructions_GetMessageParameter.__init__)


def test_hall_instructions_getmessageparameter_constructor_args():
    sig = inspect.signature(HALL_Instructions_GetMessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_instructions_getmessageparameter_has_field():
    assert hasattr(HALL_Instructions_GetMessageParameter, "field")
    descriptor = None
    for klass in HALL_Instructions_GetMessageParameter.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_getdata_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_GetData)


def test_hall_instructions_getdata_constructor_exists():
    assert callable(HALL_Instructions_GetData.__init__)


def test_hall_instructions_getdata_constructor_args():
    sig = inspect.signature(HALL_Instructions_GetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_instructions_getdata_has_field():
    assert hasattr(HALL_Instructions_GetData, "field")
    descriptor = None
    for klass in HALL_Instructions_GetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_let_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_Let)


def test_hall_instructions_let_constructor_exists():
    assert callable(HALL_Instructions_Let.__init__)


def test_hall_instructions_let_constructor_args():
    sig = inspect.signature(HALL_Instructions_Let.__init__)
    params = list(sig.parameters.keys())
    assert "namevar" in params, "Missing parameter 'namevar'"

def test_hall_instructions_let_has_namevar():
    assert hasattr(HALL_Instructions_Let, "namevar")
    descriptor = None
    for klass in HALL_Instructions_Let.__mro__:
        if "namevar" in klass.__dict__:
            descriptor = klass.__dict__["namevar"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_setmessageparameter_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_SetMessageParameter)


def test_hall_instructions_setmessageparameter_constructor_exists():
    assert callable(HALL_Instructions_SetMessageParameter.__init__)


def test_hall_instructions_setmessageparameter_constructor_args():
    sig = inspect.signature(HALL_Instructions_SetMessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_instructions_setmessageparameter_has_field():
    assert hasattr(HALL_Instructions_SetMessageParameter, "field")
    descriptor = None
    for klass in HALL_Instructions_SetMessageParameter.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_setdata_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_SetData)


def test_hall_instructions_setdata_constructor_exists():
    assert callable(HALL_Instructions_SetData.__init__)


def test_hall_instructions_setdata_constructor_args():
    sig = inspect.signature(HALL_Instructions_SetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_instructions_setdata_has_field():
    assert hasattr(HALL_Instructions_SetData, "field")
    descriptor = None
    for klass in HALL_Instructions_SetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_settopdown_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_SetTopDown)


def test_hall_instructions_settopdown_constructor_exists():
    assert callable(HALL_Instructions_SetTopDown.__init__)


def test_hall_instructions_settopdown_constructor_args():
    sig = inspect.signature(HALL_Instructions_SetTopDown.__init__)
    params = list(sig.parameters.keys())



def test_hall_instructions_domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_DomainPropertyGet)


def test_hall_instructions_domainpropertyget_constructor_exists():
    assert callable(HALL_Instructions_DomainPropertyGet.__init__)


def test_hall_instructions_domainpropertyget_constructor_args():
    sig = inspect.signature(HALL_Instructions_DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_instructions_domainpropertyget_has_name():
    assert hasattr(HALL_Instructions_DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL_Instructions_DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_getmessagedata_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_GetMessageData)


def test_hall_instructions_getmessagedata_constructor_exists():
    assert callable(HALL_Instructions_GetMessageData.__init__)


def test_hall_instructions_getmessagedata_constructor_args():
    sig = inspect.signature(HALL_Instructions_GetMessageData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_instructions_getmessagedata_has_field():
    assert hasattr(HALL_Instructions_GetMessageData, "field")
    descriptor = None
    for klass in HALL_Instructions_GetMessageData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_setstate_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_SetState)


def test_hall_instructions_setstate_constructor_exists():
    assert callable(HALL_Instructions_SetState.__init__)


def test_hall_instructions_setstate_constructor_args():
    sig = inspect.signature(HALL_Instructions_SetState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_instructions_setstate_has_name():
    assert hasattr(HALL_Instructions_SetState, "name")
    descriptor = None
    for klass in HALL_Instructions_SetState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_getstate_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_GetState)


def test_hall_instructions_getstate_constructor_exists():
    assert callable(HALL_Instructions_GetState.__init__)


def test_hall_instructions_getstate_constructor_args():
    sig = inspect.signature(HALL_Instructions_GetState.__init__)
    params = list(sig.parameters.keys())



def test_hall_instructions_unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_UnaryOperator)


def test_hall_instructions_unaryoperator_constructor_exists():
    assert callable(HALL_Instructions_UnaryOperator.__init__)


def test_hall_instructions_unaryoperator_constructor_args():
    sig = inspect.signature(HALL_Instructions_UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_instructions_unaryoperator_has_operatorname():
    assert hasattr(HALL_Instructions_UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_Instructions_UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_BinaryOperator)


def test_hall_instructions_binaryoperator_constructor_exists():
    assert callable(HALL_Instructions_BinaryOperator.__init__)


def test_hall_instructions_binaryoperator_constructor_args():
    sig = inspect.signature(HALL_Instructions_BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall_instructions_binaryoperator_has_operatorname():
    assert hasattr(HALL_Instructions_BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL_Instructions_BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_setmessagedata_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_SetMessageData)


def test_hall_instructions_setmessagedata_constructor_exists():
    assert callable(HALL_Instructions_SetMessageData.__init__)


def test_hall_instructions_setmessagedata_constructor_args():
    sig = inspect.signature(HALL_Instructions_SetMessageData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall_instructions_setmessagedata_has_field():
    assert hasattr(HALL_Instructions_SetMessageData, "field")
    descriptor = None
    for klass in HALL_Instructions_SetMessageData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_literal_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_Literal)


def test_hall_instructions_literal_constructor_exists():
    assert callable(HALL_Instructions_Literal.__init__)


def test_hall_instructions_literal_constructor_args():
    sig = inspect.signature(HALL_Instructions_Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall_instructions_literal_has_value():
    assert hasattr(HALL_Instructions_Literal, "value")
    descriptor = None
    for klass in HALL_Instructions_Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_varref_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_VarRef)


def test_hall_instructions_varref_constructor_exists():
    assert callable(HALL_Instructions_VarRef.__init__)


def test_hall_instructions_varref_constructor_args():
    sig = inspect.signature(HALL_Instructions_VarRef.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_hall_instructions_varref_has_name():
    assert hasattr(HALL_Instructions_VarRef, "name")
    descriptor = None
    for klass in HALL_Instructions_VarRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hall_instructions_varref_has_type():
    assert hasattr(HALL_Instructions_VarRef, "type")
    descriptor = None
    for klass in HALL_Instructions_VarRef.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_hall_instructions_posconditionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(HALL_Instructions_PosConditionMessageExpressionElement)


def test_hall_instructions_posconditionmessageexpressionelement_constructor_exists():
    assert callable(HALL_Instructions_PosConditionMessageExpressionElement.__init__)


def test_hall_instructions_posconditionmessageexpressionelement_constructor_args():
    sig = inspect.signature(HALL_Instructions_PosConditionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_instructions_posconditionmessageexpressionelement_is_not_abstract():
    assert not inspect.isabstract(Instructions_PosConditionMessageExpressionElement)


def test_instructions_posconditionmessageexpressionelement_constructor_exists():
    assert callable(Instructions_PosConditionMessageExpressionElement.__init__)


def test_instructions_posconditionmessageexpressionelement_constructor_args():
    sig = inspect.signature(Instructions_PosConditionMessageExpressionElement.__init__)
    params = list(sig.parameters.keys())



def test_geometrydata2d_is_not_abstract():
    assert not inspect.isabstract(GeometryData2D)


def test_geometrydata2d_constructor_exists():
    assert callable(GeometryData2D.__init__)


def test_geometrydata2d_constructor_args():
    sig = inspect.signature(GeometryData2D.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_point2d_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_Point2D)


def test_hall_geometry_point2d_constructor_exists():
    assert callable(HALL_Geometry_Point2D.__init__)


def test_hall_geometry_point2d_constructor_args():
    sig = inspect.signature(HALL_Geometry_Point2D.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_point3d_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_Point3D)


def test_hall_geometry_point3d_constructor_exists():
    assert callable(HALL_Geometry_Point3D.__init__)


def test_hall_geometry_point3d_constructor_args():
    sig = inspect.signature(HALL_Geometry_Point3D.__init__)
    params = list(sig.parameters.keys())
    assert "zCoord" in params, "Missing parameter 'zCoord'"

def test_hall_geometry_point3d_has_zCoord():
    assert hasattr(HALL_Geometry_Point3D, "zCoord")
    descriptor = None
    for klass in HALL_Geometry_Point3D.__mro__:
        if "zCoord" in klass.__dict__:
            descriptor = klass.__dict__["zCoord"]
            break
    assert isinstance(descriptor, property)



def test_geometrydata3d_is_not_abstract():
    assert not inspect.isabstract(GeometryData3D)


def test_geometrydata3d_constructor_exists():
    assert callable(GeometryData3D.__init__)


def test_geometrydata3d_constructor_args():
    sig = inspect.signature(GeometryData3D.__init__)
    params = list(sig.parameters.keys())



def test_point3d_is_not_abstract():
    assert not inspect.isabstract(Point3D)


def test_point3d_constructor_exists():
    assert callable(Point3D.__init__)


def test_point3d_constructor_args():
    sig = inspect.signature(Point3D.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_face_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_Face)


def test_hall_geometry_face_constructor_exists():
    assert callable(HALL_Geometry_Face.__init__)


def test_hall_geometry_face_constructor_args():
    sig = inspect.signature(HALL_Geometry_Face.__init__)
    params = list(sig.parameters.keys())
    assert "labelText" in params, "Missing parameter 'labelText'"

def test_hall_geometry_face_has_labelText():
    assert hasattr(HALL_Geometry_Face, "labelText")
    descriptor = None
    for klass in HALL_Geometry_Face.__mro__:
        if "labelText" in klass.__dict__:
            descriptor = klass.__dict__["labelText"]
            break
    assert isinstance(descriptor, property)



def test_point2d_is_not_abstract():
    assert not inspect.isabstract(Point2D)


def test_point2d_constructor_exists():
    assert callable(Point2D.__init__)


def test_point2d_constructor_args():
    sig = inspect.signature(Point2D.__init__)
    params = list(sig.parameters.keys())



def test_messages_hall_parameter_is_not_abstract():
    assert not inspect.isabstract(Messages_HALL_Parameter)


def test_messages_hall_parameter_constructor_exists():
    assert callable(Messages_HALL_Parameter.__init__)


def test_messages_hall_parameter_constructor_args():
    sig = inspect.signature(Messages_HALL_Parameter.__init__)
    params = list(sig.parameters.keys())



def test_messages_hall_model_is_not_abstract():
    assert not inspect.isabstract(Messages_HALL_Model)


def test_messages_hall_model_constructor_exists():
    assert callable(Messages_HALL_Model.__init__)


def test_messages_hall_model_constructor_args():
    sig = inspect.signature(Messages_HALL_Model.__init__)
    params = list(sig.parameters.keys())



def test_hall_messages_messagedefinition_is_not_abstract():
    assert not inspect.isabstract(HALL_Messages_MessageDefinition)


def test_hall_messages_messagedefinition_constructor_exists():
    assert callable(HALL_Messages_MessageDefinition.__init__)


def test_hall_messages_messagedefinition_constructor_args():
    sig = inspect.signature(HALL_Messages_MessageDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_messages_messagedefinition_has_name():
    assert hasattr(HALL_Messages_MessageDefinition, "name")
    descriptor = None
    for klass in HALL_Messages_MessageDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_actions_actionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(Actions_ActionMessageExpression)


def test_actions_actionmessageexpression_constructor_exists():
    assert callable(Actions_ActionMessageExpression.__init__)


def test_actions_actionmessageexpression_constructor_args():
    sig = inspect.signature(Actions_ActionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_instructions_posconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(Instructions_PosConditionMessageExpression)


def test_instructions_posconditionmessageexpression_constructor_exists():
    assert callable(Instructions_PosConditionMessageExpression.__init__)


def test_instructions_posconditionmessageexpression_constructor_args():
    sig = inspect.signature(Instructions_PosConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditions_preconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(Conditions_PreConditionMessageExpression)


def test_conditions_preconditionmessageexpression_constructor_exists():
    assert callable(Conditions_PreConditionMessageExpression.__init__)


def test_conditions_preconditionmessageexpression_constructor_args():
    sig = inspect.signature(Conditions_PreConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_messagestate_is_not_abstract():
    assert not inspect.isabstract(MessageState)


def test_messagestate_constructor_exists():
    assert callable(MessageState.__init__)


def test_messagestate_constructor_args():
    sig = inspect.signature(MessageState.__init__)
    params = list(sig.parameters.keys())



def test_hall_messages_initialmessagestate_is_not_abstract():
    assert not inspect.isabstract(HALL_Messages_InitialMessageState)


def test_hall_messages_initialmessagestate_constructor_exists():
    assert callable(HALL_Messages_InitialMessageState.__init__)


def test_hall_messages_initialmessagestate_constructor_args():
    sig = inspect.signature(HALL_Messages_InitialMessageState.__init__)
    params = list(sig.parameters.keys())



def test_hall_messages_namedmessagestate_is_not_abstract():
    assert not inspect.isabstract(HALL_Messages_NamedMessageState)


def test_hall_messages_namedmessagestate_constructor_exists():
    assert callable(HALL_Messages_NamedMessageState.__init__)


def test_hall_messages_namedmessagestate_constructor_args():
    sig = inspect.signature(HALL_Messages_NamedMessageState.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_messages_namedmessagestate_has_name():
    assert hasattr(HALL_Messages_NamedMessageState, "name")
    descriptor = None
    for klass in HALL_Messages_NamedMessageState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_messages_messagetransition_is_not_abstract():
    assert not inspect.isabstract(HALL_Messages_MessageTransition)


def test_hall_messages_messagetransition_constructor_exists():
    assert callable(HALL_Messages_MessageTransition.__init__)


def test_hall_messages_messagetransition_constructor_args():
    sig = inspect.signature(HALL_Messages_MessageTransition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_messages_messagetransition_has_name():
    assert hasattr(HALL_Messages_MessageTransition, "name")
    descriptor = None
    for klass in HALL_Messages_MessageTransition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_geometry_point_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_Point)


def test_hall_geometry_point_constructor_exists():
    assert callable(HALL_Geometry_Point.__init__)


def test_hall_geometry_point_constructor_args():
    sig = inspect.signature(HALL_Geometry_Point.__init__)
    params = list(sig.parameters.keys())
    assert "xCoord" in params, "Missing parameter 'xCoord'"
    assert "yCoord" in params, "Missing parameter 'yCoord'"

def test_hall_geometry_point_has_xCoord():
    assert hasattr(HALL_Geometry_Point, "xCoord")
    descriptor = None
    for klass in HALL_Geometry_Point.__mro__:
        if "xCoord" in klass.__dict__:
            descriptor = klass.__dict__["xCoord"]
            break
    assert isinstance(descriptor, property)

def test_hall_geometry_point_has_yCoord():
    assert hasattr(HALL_Geometry_Point, "yCoord")
    descriptor = None
    for klass in HALL_Geometry_Point.__mro__:
        if "yCoord" in klass.__dict__:
            descriptor = klass.__dict__["yCoord"]
            break
    assert isinstance(descriptor, property)



def test_hall_geometry_alphatransparency_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_AlphaTransparency)


def test_hall_geometry_alphatransparency_constructor_exists():
    assert callable(HALL_Geometry_AlphaTransparency.__init__)


def test_hall_geometry_alphatransparency_constructor_args():
    sig = inspect.signature(HALL_Geometry_AlphaTransparency.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall_geometry_alphatransparency_has_value():
    assert hasattr(HALL_Geometry_AlphaTransparency, "value")
    descriptor = None
    for klass in HALL_Geometry_AlphaTransparency.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_alphatransparency_is_not_abstract():
    assert not inspect.isabstract(AlphaTransparency)


def test_alphatransparency_constructor_exists():
    assert callable(AlphaTransparency.__init__)


def test_alphatransparency_constructor_args():
    sig = inspect.signature(AlphaTransparency.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_colorstate_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_ColorState)


def test_hall_geometry_colorstate_constructor_exists():
    assert callable(HALL_Geometry_ColorState.__init__)


def test_hall_geometry_colorstate_constructor_args():
    sig = inspect.signature(HALL_Geometry_ColorState.__init__)
    params = list(sig.parameters.keys())



def test_face_is_not_abstract():
    assert not inspect.isabstract(Face)


def test_face_constructor_exists():
    assert callable(Face.__init__)


def test_face_constructor_args():
    sig = inspect.signature(Face.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_geometrydata_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_GeometryData)


def test_hall_geometry_geometrydata_constructor_exists():
    assert callable(HALL_Geometry_GeometryData.__init__)


def test_hall_geometry_geometrydata_constructor_args():
    sig = inspect.signature(HALL_Geometry_GeometryData.__init__)
    params = list(sig.parameters.keys())



def test_geometry_hall_visualobject_is_not_abstract():
    assert not inspect.isabstract(Geometry_HALL_VisualObject)


def test_geometry_hall_visualobject_constructor_exists():
    assert callable(Geometry_HALL_VisualObject.__init__)


def test_geometry_hall_visualobject_constructor_args():
    sig = inspect.signature(Geometry_HALL_VisualObject.__init__)
    params = list(sig.parameters.keys())



def test_normalcolors_is_not_abstract():
    assert not inspect.isabstract(NormalColors)


def test_normalcolors_constructor_exists():
    assert callable(NormalColors.__init__)


def test_normalcolors_constructor_args():
    sig = inspect.signature(NormalColors.__init__)
    params = list(sig.parameters.keys())



def test_disabledcolors_is_not_abstract():
    assert not inspect.isabstract(DisabledColors)


def test_disabledcolors_constructor_exists():
    assert callable(DisabledColors.__init__)


def test_disabledcolors_constructor_args():
    sig = inspect.signature(DisabledColors.__init__)
    params = list(sig.parameters.keys())



def test_selectedcolors_is_not_abstract():
    assert not inspect.isabstract(SelectedColors)


def test_selectedcolors_constructor_exists():
    assert callable(SelectedColors.__init__)


def test_selectedcolors_constructor_args():
    sig = inspect.signature(SelectedColors.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_colordata_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_ColorData)


def test_hall_geometry_colordata_constructor_exists():
    assert callable(HALL_Geometry_ColorData.__init__)


def test_hall_geometry_colordata_constructor_args():
    sig = inspect.signature(HALL_Geometry_ColorData.__init__)
    params = list(sig.parameters.keys())



def test_hall_parameter_is_not_abstract():
    assert not inspect.isabstract(HALL_Parameter)


def test_hall_parameter_constructor_exists():
    assert callable(HALL_Parameter.__init__)


def test_hall_parameter_constructor_args():
    sig = inspect.signature(HALL_Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "type" in params, "Missing parameter 'type'"

def test_hall_parameter_has_name():
    assert hasattr(HALL_Parameter, "name")
    descriptor = None
    for klass in HALL_Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hall_parameter_has_type():
    assert hasattr(HALL_Parameter, "type")
    descriptor = None
    for klass in HALL_Parameter.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_color_constructor_exists():
    assert callable(Color.__init__)


def test_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_rgbcolor_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_RGBColor)


def test_hall_geometry_rgbcolor_constructor_exists():
    assert callable(HALL_Geometry_RGBColor.__init__)


def test_hall_geometry_rgbcolor_constructor_args():
    sig = inspect.signature(HALL_Geometry_RGBColor.__init__)
    params = list(sig.parameters.keys())
    assert "greenValue" in params, "Missing parameter 'greenValue'"
    assert "blueValue" in params, "Missing parameter 'blueValue'"
    assert "redValue" in params, "Missing parameter 'redValue'"

def test_hall_geometry_rgbcolor_has_greenValue():
    assert hasattr(HALL_Geometry_RGBColor, "greenValue")
    descriptor = None
    for klass in HALL_Geometry_RGBColor.__mro__:
        if "greenValue" in klass.__dict__:
            descriptor = klass.__dict__["greenValue"]
            break
    assert isinstance(descriptor, property)

def test_hall_geometry_rgbcolor_has_blueValue():
    assert hasattr(HALL_Geometry_RGBColor, "blueValue")
    descriptor = None
    for klass in HALL_Geometry_RGBColor.__mro__:
        if "blueValue" in klass.__dict__:
            descriptor = klass.__dict__["blueValue"]
            break
    assert isinstance(descriptor, property)

def test_hall_geometry_rgbcolor_has_redValue():
    assert hasattr(HALL_Geometry_RGBColor, "redValue")
    descriptor = None
    for klass in HALL_Geometry_RGBColor.__mro__:
        if "redValue" in klass.__dict__:
            descriptor = klass.__dict__["redValue"]
            break
    assert isinstance(descriptor, property)



def test_colorstate_is_not_abstract():
    assert not inspect.isabstract(ColorState)


def test_colorstate_constructor_exists():
    assert callable(ColorState.__init__)


def test_colorstate_constructor_args():
    sig = inspect.signature(ColorState.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_selectedcolors_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_SelectedColors)


def test_hall_geometry_selectedcolors_constructor_exists():
    assert callable(HALL_Geometry_SelectedColors.__init__)


def test_hall_geometry_selectedcolors_constructor_args():
    sig = inspect.signature(HALL_Geometry_SelectedColors.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_disabledcolors_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_DisabledColors)


def test_hall_geometry_disabledcolors_constructor_exists():
    assert callable(HALL_Geometry_DisabledColors.__init__)


def test_hall_geometry_disabledcolors_constructor_args():
    sig = inspect.signature(HALL_Geometry_DisabledColors.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_normalcolors_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_NormalColors)


def test_hall_geometry_normalcolors_constructor_exists():
    assert callable(HALL_Geometry_NormalColors.__init__)


def test_hall_geometry_normalcolors_constructor_args():
    sig = inspect.signature(HALL_Geometry_NormalColors.__init__)
    params = list(sig.parameters.keys())



def test_rgbcolor_is_not_abstract():
    assert not inspect.isabstract(RGBColor)


def test_rgbcolor_constructor_exists():
    assert callable(RGBColor.__init__)


def test_rgbcolor_constructor_args():
    sig = inspect.signature(RGBColor.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_color_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_Color)


def test_hall_geometry_color_constructor_exists():
    assert callable(HALL_Geometry_Color.__init__)


def test_hall_geometry_color_constructor_args():
    sig = inspect.signature(HALL_Geometry_Color.__init__)
    params = list(sig.parameters.keys())



def test_messagedefinition_is_not_abstract():
    assert not inspect.isabstract(MessageDefinition)


def test_messagedefinition_constructor_exists():
    assert callable(MessageDefinition.__init__)


def test_messagedefinition_constructor_args():
    sig = inspect.signature(MessageDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hall_goal_is_not_abstract():
    assert not inspect.isabstract(HALL_Goal)


def test_hall_goal_constructor_exists():
    assert callable(HALL_Goal.__init__)


def test_hall_goal_constructor_args():
    sig = inspect.signature(HALL_Goal.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_hall_goal_has_condition():
    assert hasattr(HALL_Goal, "condition")
    descriptor = None
    for klass in HALL_Goal.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
            break
    assert isinstance(descriptor, property)



def test_geometrydata_is_not_abstract():
    assert not inspect.isabstract(GeometryData)


def test_geometrydata_constructor_exists():
    assert callable(GeometryData.__init__)


def test_geometrydata_constructor_args():
    sig = inspect.signature(GeometryData.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_geometrydata3d_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_GeometryData3D)


def test_hall_geometry_geometrydata3d_constructor_exists():
    assert callable(HALL_Geometry_GeometryData3D.__init__)


def test_hall_geometry_geometrydata3d_constructor_args():
    sig = inspect.signature(HALL_Geometry_GeometryData3D.__init__)
    params = list(sig.parameters.keys())



def test_hall_geometry_geometrydata2d_is_not_abstract():
    assert not inspect.isabstract(HALL_Geometry_GeometryData2D)


def test_hall_geometry_geometrydata2d_constructor_exists():
    assert callable(HALL_Geometry_GeometryData2D.__init__)


def test_hall_geometry_geometrydata2d_constructor_args():
    sig = inspect.signature(HALL_Geometry_GeometryData2D.__init__)
    params = list(sig.parameters.keys())
    assert "labelText" in params, "Missing parameter 'labelText'"

def test_hall_geometry_geometrydata2d_has_labelText():
    assert hasattr(HALL_Geometry_GeometryData2D, "labelText")
    descriptor = None
    for klass in HALL_Geometry_GeometryData2D.__mro__:
        if "labelText" in klass.__dict__:
            descriptor = klass.__dict__["labelText"]
            break
    assert isinstance(descriptor, property)



def test_colordata_is_not_abstract():
    assert not inspect.isabstract(ColorData)


def test_colordata_constructor_exists():
    assert callable(ColorData.__init__)


def test_colordata_constructor_args():
    sig = inspect.signature(ColorData.__init__)
    params = list(sig.parameters.keys())



def test_component_is_not_abstract():
    assert not inspect.isabstract(Component)


def test_component_constructor_exists():
    assert callable(Component.__init__)


def test_component_constructor_args():
    sig = inspect.signature(Component.__init__)
    params = list(sig.parameters.keys())



def test_hall_taskobject_is_not_abstract():
    assert not inspect.isabstract(HALL_TaskObject)


def test_hall_taskobject_constructor_exists():
    assert callable(HALL_TaskObject.__init__)


def test_hall_taskobject_constructor_args():
    sig = inspect.signature(HALL_TaskObject.__init__)
    params = list(sig.parameters.keys())
    assert "completionTime" in params, "Missing parameter 'completionTime'"
    assert "numberofgoalscompleted" in params, "Missing parameter 'numberofgoalscompleted'"

def test_hall_taskobject_has_completionTime():
    assert hasattr(HALL_TaskObject, "completionTime")
    descriptor = None
    for klass in HALL_TaskObject.__mro__:
        if "completionTime" in klass.__dict__:
            descriptor = klass.__dict__["completionTime"]
            break
    assert isinstance(descriptor, property)

def test_hall_taskobject_has_numberofgoalscompleted():
    assert hasattr(HALL_TaskObject, "numberofgoalscompleted")
    descriptor = None
    for klass in HALL_TaskObject.__mro__:
        if "numberofgoalscompleted" in klass.__dict__:
            descriptor = klass.__dict__["numberofgoalscompleted"]
            break
    assert isinstance(descriptor, property)



def test_hall_visualobject_is_not_abstract():
    assert not inspect.isabstract(HALL_VisualObject)


def test_hall_visualobject_constructor_exists():
    assert callable(HALL_VisualObject.__init__)


def test_hall_visualobject_constructor_args():
    sig = inspect.signature(HALL_VisualObject.__init__)
    params = list(sig.parameters.keys())



def test_hall_model_is_not_abstract():
    assert not inspect.isabstract(HALL_Model)


def test_hall_model_constructor_exists():
    assert callable(HALL_Model.__init__)


def test_hall_model_constructor_args():
    sig = inspect.signature(HALL_Model.__init__)
    params = list(sig.parameters.keys())



def test_hall_systemcomponent_is_not_abstract():
    assert not inspect.isabstract(HALL_SystemComponent)


def test_hall_systemcomponent_constructor_exists():
    assert callable(HALL_SystemComponent.__init__)


def test_hall_systemcomponent_constructor_args():
    sig = inspect.signature(HALL_SystemComponent.__init__)
    params = list(sig.parameters.keys())



def test_messagehandler_is_not_abstract():
    assert not inspect.isabstract(MessageHandler)


def test_messagehandler_constructor_exists():
    assert callable(MessageHandler.__init__)


def test_messagehandler_constructor_args():
    sig = inspect.signature(MessageHandler.__init__)
    params = list(sig.parameters.keys())



def test_fsm_is_not_abstract():
    assert not inspect.isabstract(FSM)


def test_fsm_constructor_exists():
    assert callable(FSM.__init__)


def test_fsm_constructor_args():
    sig = inspect.signature(FSM.__init__)
    params = list(sig.parameters.keys())



def test_hall_data_is_not_abstract():
    assert not inspect.isabstract(HALL_Data)


def test_hall_data_constructor_exists():
    assert callable(HALL_Data.__init__)


def test_hall_data_constructor_args():
    sig = inspect.signature(HALL_Data.__init__)
    params = list(sig.parameters.keys())
    assert "initValue" in params, "Missing parameter 'initValue'"
    assert "type" in params, "Missing parameter 'type'"
    assert "currentValue" in params, "Missing parameter 'currentValue'"
    assert "name" in params, "Missing parameter 'name'"

def test_hall_data_has_initValue():
    assert hasattr(HALL_Data, "initValue")
    descriptor = None
    for klass in HALL_Data.__mro__:
        if "initValue" in klass.__dict__:
            descriptor = klass.__dict__["initValue"]
            break
    assert isinstance(descriptor, property)

def test_hall_data_has_type():
    assert hasattr(HALL_Data, "type")
    descriptor = None
    for klass in HALL_Data.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_hall_data_has_currentValue():
    assert hasattr(HALL_Data, "currentValue")
    descriptor = None
    for klass in HALL_Data.__mro__:
        if "currentValue" in klass.__dict__:
            descriptor = klass.__dict__["currentValue"]
            break
    assert isinstance(descriptor, property)

def test_hall_data_has_name():
    assert hasattr(HALL_Data, "name")
    descriptor = None
    for klass in HALL_Data.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_component_is_not_abstract():
    assert not inspect.isabstract(HALL_Component)


def test_hall_component_constructor_exists():
    assert callable(HALL_Component.__init__)


def test_hall_component_constructor_args():
    sig = inspect.signature(HALL_Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall_component_has_name():
    assert hasattr(HALL_Component, "name")
    descriptor = None
    for klass in HALL_Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall_userprofile_is_not_abstract():
    assert not inspect.isabstract(HALL_UserProfile)


def test_hall_userprofile_constructor_exists():
    assert callable(HALL_UserProfile.__init__)


def test_hall_userprofile_constructor_args():
    sig = inspect.signature(HALL_UserProfile.__init__)
    params = list(sig.parameters.keys())
    assert "numberofcompletedtasks" in params, "Missing parameter 'numberofcompletedtasks'"

def test_hall_userprofile_has_numberofcompletedtasks():
    assert hasattr(HALL_UserProfile, "numberofcompletedtasks")
    descriptor = None
    for klass in HALL_UserProfile.__mro__:
        if "numberofcompletedtasks" in klass.__dict__:
            descriptor = klass.__dict__["numberofcompletedtasks"]
            break
    assert isinstance(descriptor, property)


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
FSMActions_HALL_Component_strategy = st.builds(
    FSMActions_HALL_Component,
)
ActionExpressionElement_strategy = st.builds(
    ActionExpressionElement,
)
HALL_FSMActions_GetData_strategy = st.builds(
    HALL_FSMActions_GetData,
    field=
        safe_text
)
HALL_FSMActions_BinaryOperator_strategy = st.builds(
    HALL_FSMActions_BinaryOperator,
    operatorname=
        safe_text
)
HALL_FSMActions_UnaryOperator_strategy = st.builds(
    HALL_FSMActions_UnaryOperator,
    operatorname=
        safe_text
)
HALL_FSMActions_VarRef_strategy = st.builds(
    HALL_FSMActions_VarRef,
    name=
        safe_text,
    type=
        safe_text
)
HALL_FSMActions_ActionExpressionElement_strategy = st.builds(
    HALL_FSMActions_ActionExpressionElement,
)
FSMActions_ActionExpressionElement_strategy = st.builds(
    FSMActions_ActionExpressionElement,
)
HALL_FSMActions_ActionExpression_strategy = st.builds(
    HALL_FSMActions_ActionExpression,
)
HALL_FSMActions_DomainPropertySet_strategy = st.builds(
    HALL_FSMActions_DomainPropertySet,
    name=
        safe_text
)
HALL_FSMActions_MessageInvocation_strategy = st.builds(
    HALL_FSMActions_MessageInvocation,
    isTopDown=
        st.booleans(),
    name=
        safe_text
)
HALL_FSMActions_Let_strategy = st.builds(
    HALL_FSMActions_Let,
    namevar=
        safe_text
)
HALL_FSMActions_DomainPropertyGet_strategy = st.builds(
    HALL_FSMActions_DomainPropertyGet,
    name=
        safe_text
)
HALL_FSMActions_Literal_strategy = st.builds(
    HALL_FSMActions_Literal,
    value=
        safe_text
)
HALL_FSMConditions_PreConditionExpressionElement_strategy = st.builds(
    HALL_FSMConditions_PreConditionExpressionElement,
)
FSMConditions_PreConditionExpressionElement_strategy = st.builds(
    FSMConditions_PreConditionExpressionElement,
)
HALL_FSMConditions_PreConditionExpression_strategy = st.builds(
    HALL_FSMConditions_PreConditionExpression,
)
FSMConditions_HALL_Component_strategy = st.builds(
    FSMConditions_HALL_Component,
)
PreConditionExpressionElement_strategy = st.builds(
    PreConditionExpressionElement,
)
HALL_FSMConditions_BinaryOperator_strategy = st.builds(
    HALL_FSMConditions_BinaryOperator,
    operatorname=
        safe_text
)
HALL_FSMConditions_Let_strategy = st.builds(
    HALL_FSMConditions_Let,
    namevar=
        safe_text
)
HALL_FSMConditions_DomainPropertyGet_strategy = st.builds(
    HALL_FSMConditions_DomainPropertyGet,
    name=
        safe_text
)
HALL_FSMConditions_VarRef_strategy = st.builds(
    HALL_FSMConditions_VarRef,
    type=
        safe_text,
    name=
        safe_text
)
HALL_FSMConditions_GetState_strategy = st.builds(
    HALL_FSMConditions_GetState,
)
HALL_FSMConditions_UnaryOperator_strategy = st.builds(
    HALL_FSMConditions_UnaryOperator,
    operatorname=
        safe_text
)
HALL_FSMConditions_GetData_strategy = st.builds(
    HALL_FSMConditions_GetData,
    field=
        safe_text
)
HALL_FSMConditions_Literal_strategy = st.builds(
    HALL_FSMConditions_Literal,
    value=
        safe_text
)
PosConditionExpressionElement_strategy = st.builds(
    PosConditionExpressionElement,
)
HALL_FSMInstructions_DomainPropertyGet_strategy = st.builds(
    HALL_FSMInstructions_DomainPropertyGet,
    name=
        safe_text
)
HALL_FSMInstructions_Let_strategy = st.builds(
    HALL_FSMInstructions_Let,
    namevar=
        safe_text
)
HALL_FSMInstructions_Literal_strategy = st.builds(
    HALL_FSMInstructions_Literal,
    value=
        safe_text
)
HALL_FSMInstructions_VarRef_strategy = st.builds(
    HALL_FSMInstructions_VarRef,
    type=
        safe_text,
    name=
        safe_text
)
HALL_FSMInstructions_PosConditionExpressionElement_strategy = st.builds(
    HALL_FSMInstructions_PosConditionExpressionElement,
)
FSMInstructions_PosConditionExpressionElement_strategy = st.builds(
    FSMInstructions_PosConditionExpressionElement,
)
HALL_FSMInstructions_PosConditionExpression_strategy = st.builds(
    HALL_FSMInstructions_PosConditionExpression,
)
TriggerExpressionElement_strategy = st.builds(
    TriggerExpressionElement,
)
HALL_Trigger_DomainEventFired_strategy = st.builds(
    HALL_Trigger_DomainEventFired,
)
HALL_Trigger_MessageNotification_strategy = st.builds(
    HALL_Trigger_MessageNotification,
)
HALL_Trigger_TriggerExpressionElement_strategy = st.builds(
    HALL_Trigger_TriggerExpressionElement,
    String=
        safe_text
)
HALL_FSMInstructions_SetData_strategy = st.builds(
    HALL_FSMInstructions_SetData,
    field=
        safe_text
)
HALL_FSMInstructions_SetState_strategy = st.builds(
    HALL_FSMInstructions_SetState,
    name=
        safe_text
)
HALL_FSMInstructions_GetState_strategy = st.builds(
    HALL_FSMInstructions_GetState,
)
FSMInstructions_HALL_Component_strategy = st.builds(
    FSMInstructions_HALL_Component,
)
HALL_FSMInstructions_GetData_strategy = st.builds(
    HALL_FSMInstructions_GetData,
    field=
        safe_text
)
HALL_FSMInstructions_UnaryOperator_strategy = st.builds(
    HALL_FSMInstructions_UnaryOperator,
    operatorname=
        safe_text
)
HALL_FSMInstructions_BinaryOperator_strategy = st.builds(
    HALL_FSMInstructions_BinaryOperator,
    operatorname=
        safe_text
)
State_strategy = st.builds(
    State,
)
HALL_FSM_InitialState_strategy = st.builds(
    HALL_FSM_InitialState,
)
HALL_FSM_NamedState_strategy = st.builds(
    HALL_FSM_NamedState,
    name=
        safe_text
)
NamedState_strategy = st.builds(
    NamedState,
)
InitialState_strategy = st.builds(
    InitialState,
)
FSM_HALL_Component_strategy = st.builds(
    FSM_HALL_Component,
)
HALL_FSM_FSM_strategy = st.builds(
    HALL_FSM_FSM,
)
Trigger_TriggerExpressionElement_strategy = st.builds(
    Trigger_TriggerExpressionElement,
)
HALL_Trigger_TriggerExpression_strategy = st.builds(
    HALL_Trigger_TriggerExpression,
)
Transition_strategy = st.builds(
    Transition,
)
HALL_FSM_State_strategy = st.builds(
    HALL_FSM_State,
    isActive=
        st.booleans()
)
Trigger_TriggerExpression_strategy = st.builds(
    Trigger_TriggerExpression,
)
FSMActions_ActionExpression_strategy = st.builds(
    FSMActions_ActionExpression,
)
FSMInstructions_PosConditionExpression_strategy = st.builds(
    FSMInstructions_PosConditionExpression,
)
FSMConditions_PreConditionExpression_strategy = st.builds(
    FSMConditions_PreConditionExpression,
)
HALL_FSM_Transition_strategy = st.builds(
    HALL_FSM_Transition,
    name=
        safe_text
)
ActionMessageExpressionElement_strategy = st.builds(
    ActionMessageExpressionElement,
)
HALL_Actions_Literal_strategy = st.builds(
    HALL_Actions_Literal,
    value=
        safe_text
)
HALL_Actions_Let_strategy = st.builds(
    HALL_Actions_Let,
    namevar=
        safe_text
)
HALL_Actions_DomainPropertyGet_strategy = st.builds(
    HALL_Actions_DomainPropertyGet,
    name=
        safe_text
)
HALL_FSMActions_Enable_strategy = st.builds(
    HALL_FSMActions_Enable,
)
HALL_Actions_BinaryOperator_strategy = st.builds(
    HALL_Actions_BinaryOperator,
    operatorname=
        safe_text
)
HALL_Actions_VarRef_strategy = st.builds(
    HALL_Actions_VarRef,
    name=
        safe_text,
    type=
        safe_text
)
HALL_Actions_ActionMessageExpressionElement_strategy = st.builds(
    HALL_Actions_ActionMessageExpressionElement,
)
HALL_Actions_Enable_strategy = st.builds(
    HALL_Actions_Enable,
)
HALL_Actions_DomainPropertySet_strategy = st.builds(
    HALL_Actions_DomainPropertySet,
    name=
        safe_text
)
Actions_HALL_Component_strategy = st.builds(
    Actions_HALL_Component,
)
HALL_Actions_GetData_strategy = st.builds(
    HALL_Actions_GetData,
    field=
        safe_text
)
HALL_Actions_UnaryOperator_strategy = st.builds(
    HALL_Actions_UnaryOperator,
    operatorname=
        safe_text
)
HALL_Actions_MessageInvocation_strategy = st.builds(
    HALL_Actions_MessageInvocation,
    name=
        safe_text,
    isTopDown=
        st.booleans()
)
HALL_Actions_GetMessageParameter_strategy = st.builds(
    HALL_Actions_GetMessageParameter,
    field=
        safe_text
)
HALL_Actions_GetMessageData_strategy = st.builds(
    HALL_Actions_GetMessageData,
    field=
        safe_text
)
Conditions_HALL_Component_strategy = st.builds(
    Conditions_HALL_Component,
)
PreConditionMessageExpressionElement_strategy = st.builds(
    PreConditionMessageExpressionElement,
)
HALL_Conditions_DomainPropertyGet_strategy = st.builds(
    HALL_Conditions_DomainPropertyGet,
    name=
        safe_text
)
HALL_Conditions_GetMessageData_strategy = st.builds(
    HALL_Conditions_GetMessageData,
    field=
        safe_text
)
HALL_Conditions_Literal_strategy = st.builds(
    HALL_Conditions_Literal,
    value=
        safe_text
)
HALL_Conditions_GetData_strategy = st.builds(
    HALL_Conditions_GetData,
    field=
        safe_text
)
HALL_Conditions_GetState_strategy = st.builds(
    HALL_Conditions_GetState,
)
HALL_Conditions_GetMessageParameter_strategy = st.builds(
    HALL_Conditions_GetMessageParameter,
    field=
        safe_text
)
HALL_Conditions_VarRef_strategy = st.builds(
    HALL_Conditions_VarRef,
    name=
        safe_text,
    type=
        safe_text
)
HALL_Conditions_PreConditionMessageExpressionElement_strategy = st.builds(
    HALL_Conditions_PreConditionMessageExpressionElement,
)
Conditions_PreConditionMessageExpressionElement_strategy = st.builds(
    Conditions_PreConditionMessageExpressionElement,
)
Actions_ActionMessageExpressionElement_strategy = st.builds(
    Actions_ActionMessageExpressionElement,
)
HALL_Actions_ActionMessageExpression_strategy = st.builds(
    HALL_Actions_ActionMessageExpression,
)
HALL_Conditions_BinaryOperator_strategy = st.builds(
    HALL_Conditions_BinaryOperator,
    operatorname=
        safe_text
)
HALL_Conditions_UnaryOperator_strategy = st.builds(
    HALL_Conditions_UnaryOperator,
    operatorname=
        safe_text
)
HALL_Conditions_Let_strategy = st.builds(
    HALL_Conditions_Let,
    namevar=
        safe_text
)
HALL_Conditions_PreConditionMessageExpression_strategy = st.builds(
    HALL_Conditions_PreConditionMessageExpression,
)
HALL_Instructions_PosConditionMessageExpression_strategy = st.builds(
    HALL_Instructions_PosConditionMessageExpression,
)
MessageTransition_strategy = st.builds(
    MessageTransition,
)
HALL_Messages_MessageState_strategy = st.builds(
    HALL_Messages_MessageState,
    isContinue=
        st.booleans(),
    isActive=
        st.booleans(),
    isEnd=
        st.booleans()
)
Messages_HALL_Component_strategy = st.builds(
    Messages_HALL_Component,
)
InitialMessageState_strategy = st.builds(
    InitialMessageState,
)
NamedMessageState_strategy = st.builds(
    NamedMessageState,
)
HALL_Messages_MessageHandler_strategy = st.builds(
    HALL_Messages_MessageHandler,
    name=
        safe_text
)
Messages_HALL_Data_strategy = st.builds(
    Messages_HALL_Data,
)
Instructions_HALL_Component_strategy = st.builds(
    Instructions_HALL_Component,
)
PosConditionMessageExpressionElement_strategy = st.builds(
    PosConditionMessageExpressionElement,
)
HALL_Instructions_GetMessageParameter_strategy = st.builds(
    HALL_Instructions_GetMessageParameter,
    field=
        safe_text
)
HALL_Instructions_GetData_strategy = st.builds(
    HALL_Instructions_GetData,
    field=
        safe_text
)
HALL_Instructions_Let_strategy = st.builds(
    HALL_Instructions_Let,
    namevar=
        safe_text
)
HALL_Instructions_SetMessageParameter_strategy = st.builds(
    HALL_Instructions_SetMessageParameter,
    field=
        safe_text
)
HALL_Instructions_SetData_strategy = st.builds(
    HALL_Instructions_SetData,
    field=
        safe_text
)
HALL_Instructions_SetTopDown_strategy = st.builds(
    HALL_Instructions_SetTopDown,
)
HALL_Instructions_DomainPropertyGet_strategy = st.builds(
    HALL_Instructions_DomainPropertyGet,
    name=
        safe_text
)
HALL_Instructions_GetMessageData_strategy = st.builds(
    HALL_Instructions_GetMessageData,
    field=
        safe_text
)
HALL_Instructions_SetState_strategy = st.builds(
    HALL_Instructions_SetState,
    name=
        safe_text
)
HALL_Instructions_GetState_strategy = st.builds(
    HALL_Instructions_GetState,
)
HALL_Instructions_UnaryOperator_strategy = st.builds(
    HALL_Instructions_UnaryOperator,
    operatorname=
        safe_text
)
HALL_Instructions_BinaryOperator_strategy = st.builds(
    HALL_Instructions_BinaryOperator,
    operatorname=
        safe_text
)
HALL_Instructions_SetMessageData_strategy = st.builds(
    HALL_Instructions_SetMessageData,
    field=
        safe_text
)
HALL_Instructions_Literal_strategy = st.builds(
    HALL_Instructions_Literal,
    value=
        safe_text
)
HALL_Instructions_VarRef_strategy = st.builds(
    HALL_Instructions_VarRef,
    name=
        safe_text,
    type=
        safe_text
)
HALL_Instructions_PosConditionMessageExpressionElement_strategy = st.builds(
    HALL_Instructions_PosConditionMessageExpressionElement,
)
Instructions_PosConditionMessageExpressionElement_strategy = st.builds(
    Instructions_PosConditionMessageExpressionElement,
)
GeometryData2D_strategy = st.builds(
    GeometryData2D,
)
Point_strategy = st.builds(
    Point,
)
HALL_Geometry_Point2D_strategy = st.builds(
    HALL_Geometry_Point2D,
)
HALL_Geometry_Point3D_strategy = st.builds(
    HALL_Geometry_Point3D,
    zCoord=
        st.integers()
)
GeometryData3D_strategy = st.builds(
    GeometryData3D,
)
Point3D_strategy = st.builds(
    Point3D,
)
HALL_Geometry_Face_strategy = st.builds(
    HALL_Geometry_Face,
    labelText=
        safe_text
)
Point2D_strategy = st.builds(
    Point2D,
)
Messages_HALL_Parameter_strategy = st.builds(
    Messages_HALL_Parameter,
)
Messages_HALL_Model_strategy = st.builds(
    Messages_HALL_Model,
)
HALL_Messages_MessageDefinition_strategy = st.builds(
    HALL_Messages_MessageDefinition,
    name=
        safe_text
)
Actions_ActionMessageExpression_strategy = st.builds(
    Actions_ActionMessageExpression,
)
Instructions_PosConditionMessageExpression_strategy = st.builds(
    Instructions_PosConditionMessageExpression,
)
Conditions_PreConditionMessageExpression_strategy = st.builds(
    Conditions_PreConditionMessageExpression,
)
MessageState_strategy = st.builds(
    MessageState,
)
HALL_Messages_InitialMessageState_strategy = st.builds(
    HALL_Messages_InitialMessageState,
)
HALL_Messages_NamedMessageState_strategy = st.builds(
    HALL_Messages_NamedMessageState,
    name=
        safe_text
)
HALL_Messages_MessageTransition_strategy = st.builds(
    HALL_Messages_MessageTransition,
    name=
        safe_text
)
HALL_Geometry_Point_strategy = st.builds(
    HALL_Geometry_Point,
    xCoord=
        st.integers(),
    yCoord=
        st.integers()
)
HALL_Geometry_AlphaTransparency_strategy = st.builds(
    HALL_Geometry_AlphaTransparency,
    value=
        st.integers()
)
AlphaTransparency_strategy = st.builds(
    AlphaTransparency,
)
HALL_Geometry_ColorState_strategy = st.builds(
    HALL_Geometry_ColorState,
)
Face_strategy = st.builds(
    Face,
)
HALL_Geometry_GeometryData_strategy = st.builds(
    HALL_Geometry_GeometryData,
)
Geometry_HALL_VisualObject_strategy = st.builds(
    Geometry_HALL_VisualObject,
)
NormalColors_strategy = st.builds(
    NormalColors,
)
DisabledColors_strategy = st.builds(
    DisabledColors,
)
SelectedColors_strategy = st.builds(
    SelectedColors,
)
HALL_Geometry_ColorData_strategy = st.builds(
    HALL_Geometry_ColorData,
)
HALL_Parameter_strategy = st.builds(
    HALL_Parameter,
    name=
        safe_text,
    type=
        safe_text
)
Color_strategy = st.builds(
    Color,
)
HALL_Geometry_RGBColor_strategy = st.builds(
    HALL_Geometry_RGBColor,
    greenValue=
        st.integers(),
    blueValue=
        st.integers(),
    redValue=
        st.integers()
)
ColorState_strategy = st.builds(
    ColorState,
)
HALL_Geometry_SelectedColors_strategy = st.builds(
    HALL_Geometry_SelectedColors,
)
HALL_Geometry_DisabledColors_strategy = st.builds(
    HALL_Geometry_DisabledColors,
)
HALL_Geometry_NormalColors_strategy = st.builds(
    HALL_Geometry_NormalColors,
)
RGBColor_strategy = st.builds(
    RGBColor,
)
HALL_Geometry_Color_strategy = st.builds(
    HALL_Geometry_Color,
)
MessageDefinition_strategy = st.builds(
    MessageDefinition,
)
HALL_Goal_strategy = st.builds(
    HALL_Goal,
    condition=
        safe_text
)
GeometryData_strategy = st.builds(
    GeometryData,
)
HALL_Geometry_GeometryData3D_strategy = st.builds(
    HALL_Geometry_GeometryData3D,
)
HALL_Geometry_GeometryData2D_strategy = st.builds(
    HALL_Geometry_GeometryData2D,
    labelText=
        safe_text
)
ColorData_strategy = st.builds(
    ColorData,
)
Component_strategy = st.builds(
    Component,
)
HALL_TaskObject_strategy = st.builds(
    HALL_TaskObject,
    completionTime=
        st.integers(),
    numberofgoalscompleted=
        st.integers()
)
HALL_VisualObject_strategy = st.builds(
    HALL_VisualObject,
)
HALL_Model_strategy = st.builds(
    HALL_Model,
)
HALL_SystemComponent_strategy = st.builds(
    HALL_SystemComponent,
)
MessageHandler_strategy = st.builds(
    MessageHandler,
)
FSM_strategy = st.builds(
    FSM,
)
HALL_Data_strategy = st.builds(
    HALL_Data,
    initValue=
        safe_text,
    type=
        safe_text,
    currentValue=
        safe_text,
    name=
        safe_text
)
HALL_Component_strategy = st.builds(
    HALL_Component,
    name=
        safe_text
)
HALL_UserProfile_strategy = st.builds(
    HALL_UserProfile,
    numberofcompletedtasks=
        st.integers()
)

@given(instance=FSMActions_HALL_Component_strategy)
@settings(max_examples=50)
def test_fsmactions_hall_component_instantiation(instance):
    assert isinstance(instance, FSMActions_HALL_Component)

@given(instance=ActionExpressionElement_strategy)
@settings(max_examples=50)
def test_actionexpressionelement_instantiation(instance):
    assert isinstance(instance, ActionExpressionElement)

@given(instance=HALL_FSMActions_GetData_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_getdata_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_GetData)



@given(instance=HALL_FSMActions_GetData_strategy)
def test_hall_fsmactions_getdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_FSMActions_BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_BinaryOperator)



@given(instance=HALL_FSMActions_BinaryOperator_strategy)
def test_hall_fsmactions_binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_FSMActions_UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_UnaryOperator)



@given(instance=HALL_FSMActions_UnaryOperator_strategy)
def test_hall_fsmactions_unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_FSMActions_VarRef_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_varref_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_VarRef)



@given(instance=HALL_FSMActions_VarRef_strategy)
def test_hall_fsmactions_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=HALL_FSMActions_VarRef_strategy)
def test_hall_fsmactions_varref_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=HALL_FSMActions_ActionExpressionElement_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_actionexpressionelement_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_ActionExpressionElement)

@given(instance=FSMActions_ActionExpressionElement_strategy)
@settings(max_examples=50)
def test_fsmactions_actionexpressionelement_instantiation(instance):
    assert isinstance(instance, FSMActions_ActionExpressionElement)

@given(instance=HALL_FSMActions_ActionExpression_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_actionexpression_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_ActionExpression)

@given(instance=HALL_FSMActions_DomainPropertySet_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_domainpropertyset_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_DomainPropertySet)



@given(instance=HALL_FSMActions_DomainPropertySet_strategy)
def test_hall_fsmactions_domainpropertyset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMActions_MessageInvocation_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_messageinvocation_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_MessageInvocation)



@given(instance=HALL_FSMActions_MessageInvocation_strategy)
def test_hall_fsmactions_messageinvocation_isTopDown_setter(instance):
    original = instance.isTopDown
    instance.isTopDown = original
    assert instance.isTopDown == original



@given(instance=HALL_FSMActions_MessageInvocation_strategy)
def test_hall_fsmactions_messageinvocation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMActions_Let_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_let_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_Let)



@given(instance=HALL_FSMActions_Let_strategy)
def test_hall_fsmactions_let_namevar_setter(instance):
    original = instance.namevar
    instance.namevar = original
    assert instance.namevar == original

@given(instance=HALL_FSMActions_DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_DomainPropertyGet)



@given(instance=HALL_FSMActions_DomainPropertyGet_strategy)
def test_hall_fsmactions_domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMActions_Literal_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_literal_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_Literal)



@given(instance=HALL_FSMActions_Literal_strategy)
def test_hall_fsmactions_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL_FSMConditions_PreConditionExpressionElement_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_preconditionexpressionelement_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_PreConditionExpressionElement)

@given(instance=FSMConditions_PreConditionExpressionElement_strategy)
@settings(max_examples=50)
def test_fsmconditions_preconditionexpressionelement_instantiation(instance):
    assert isinstance(instance, FSMConditions_PreConditionExpressionElement)

@given(instance=HALL_FSMConditions_PreConditionExpression_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_preconditionexpression_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_PreConditionExpression)

@given(instance=FSMConditions_HALL_Component_strategy)
@settings(max_examples=50)
def test_fsmconditions_hall_component_instantiation(instance):
    assert isinstance(instance, FSMConditions_HALL_Component)

@given(instance=PreConditionExpressionElement_strategy)
@settings(max_examples=50)
def test_preconditionexpressionelement_instantiation(instance):
    assert isinstance(instance, PreConditionExpressionElement)

@given(instance=HALL_FSMConditions_BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_BinaryOperator)



@given(instance=HALL_FSMConditions_BinaryOperator_strategy)
def test_hall_fsmconditions_binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_FSMConditions_Let_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_let_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_Let)



@given(instance=HALL_FSMConditions_Let_strategy)
def test_hall_fsmconditions_let_namevar_setter(instance):
    original = instance.namevar
    instance.namevar = original
    assert instance.namevar == original

@given(instance=HALL_FSMConditions_DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_DomainPropertyGet)



@given(instance=HALL_FSMConditions_DomainPropertyGet_strategy)
def test_hall_fsmconditions_domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMConditions_VarRef_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_varref_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_VarRef)



@given(instance=HALL_FSMConditions_VarRef_strategy)
def test_hall_fsmconditions_varref_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=HALL_FSMConditions_VarRef_strategy)
def test_hall_fsmconditions_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMConditions_GetState_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_getstate_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_GetState)

@given(instance=HALL_FSMConditions_UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_UnaryOperator)



@given(instance=HALL_FSMConditions_UnaryOperator_strategy)
def test_hall_fsmconditions_unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_FSMConditions_GetData_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_getdata_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_GetData)



@given(instance=HALL_FSMConditions_GetData_strategy)
def test_hall_fsmconditions_getdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_FSMConditions_Literal_strategy)
@settings(max_examples=50)
def test_hall_fsmconditions_literal_instantiation(instance):
    assert isinstance(instance, HALL_FSMConditions_Literal)



@given(instance=HALL_FSMConditions_Literal_strategy)
def test_hall_fsmconditions_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=PosConditionExpressionElement_strategy)
@settings(max_examples=50)
def test_posconditionexpressionelement_instantiation(instance):
    assert isinstance(instance, PosConditionExpressionElement)

@given(instance=HALL_FSMInstructions_DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_DomainPropertyGet)



@given(instance=HALL_FSMInstructions_DomainPropertyGet_strategy)
def test_hall_fsminstructions_domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMInstructions_Let_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_let_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_Let)



@given(instance=HALL_FSMInstructions_Let_strategy)
def test_hall_fsminstructions_let_namevar_setter(instance):
    original = instance.namevar
    instance.namevar = original
    assert instance.namevar == original

@given(instance=HALL_FSMInstructions_Literal_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_literal_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_Literal)



@given(instance=HALL_FSMInstructions_Literal_strategy)
def test_hall_fsminstructions_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL_FSMInstructions_VarRef_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_varref_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_VarRef)



@given(instance=HALL_FSMInstructions_VarRef_strategy)
def test_hall_fsminstructions_varref_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=HALL_FSMInstructions_VarRef_strategy)
def test_hall_fsminstructions_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMInstructions_PosConditionExpressionElement_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_posconditionexpressionelement_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_PosConditionExpressionElement)

@given(instance=FSMInstructions_PosConditionExpressionElement_strategy)
@settings(max_examples=50)
def test_fsminstructions_posconditionexpressionelement_instantiation(instance):
    assert isinstance(instance, FSMInstructions_PosConditionExpressionElement)

@given(instance=HALL_FSMInstructions_PosConditionExpression_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_posconditionexpression_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_PosConditionExpression)

@given(instance=TriggerExpressionElement_strategy)
@settings(max_examples=50)
def test_triggerexpressionelement_instantiation(instance):
    assert isinstance(instance, TriggerExpressionElement)

@given(instance=HALL_Trigger_DomainEventFired_strategy)
@settings(max_examples=50)
def test_hall_trigger_domaineventfired_instantiation(instance):
    assert isinstance(instance, HALL_Trigger_DomainEventFired)

@given(instance=HALL_Trigger_MessageNotification_strategy)
@settings(max_examples=50)
def test_hall_trigger_messagenotification_instantiation(instance):
    assert isinstance(instance, HALL_Trigger_MessageNotification)

@given(instance=HALL_Trigger_TriggerExpressionElement_strategy)
@settings(max_examples=50)
def test_hall_trigger_triggerexpressionelement_instantiation(instance):
    assert isinstance(instance, HALL_Trigger_TriggerExpressionElement)



@given(instance=HALL_Trigger_TriggerExpressionElement_strategy)
def test_hall_trigger_triggerexpressionelement_String_setter(instance):
    original = instance.String
    instance.String = original
    assert instance.String == original

@given(instance=HALL_FSMInstructions_SetData_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_setdata_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_SetData)



@given(instance=HALL_FSMInstructions_SetData_strategy)
def test_hall_fsminstructions_setdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_FSMInstructions_SetState_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_setstate_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_SetState)



@given(instance=HALL_FSMInstructions_SetState_strategy)
def test_hall_fsminstructions_setstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMInstructions_GetState_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_getstate_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_GetState)

@given(instance=FSMInstructions_HALL_Component_strategy)
@settings(max_examples=50)
def test_fsminstructions_hall_component_instantiation(instance):
    assert isinstance(instance, FSMInstructions_HALL_Component)

@given(instance=HALL_FSMInstructions_GetData_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_getdata_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_GetData)



@given(instance=HALL_FSMInstructions_GetData_strategy)
def test_hall_fsminstructions_getdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_FSMInstructions_UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_UnaryOperator)



@given(instance=HALL_FSMInstructions_UnaryOperator_strategy)
def test_hall_fsminstructions_unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_FSMInstructions_BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall_fsminstructions_binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_FSMInstructions_BinaryOperator)



@given(instance=HALL_FSMInstructions_BinaryOperator_strategy)
def test_hall_fsminstructions_binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=HALL_FSM_InitialState_strategy)
@settings(max_examples=50)
def test_hall_fsm_initialstate_instantiation(instance):
    assert isinstance(instance, HALL_FSM_InitialState)

@given(instance=HALL_FSM_NamedState_strategy)
@settings(max_examples=50)
def test_hall_fsm_namedstate_instantiation(instance):
    assert isinstance(instance, HALL_FSM_NamedState)



@given(instance=HALL_FSM_NamedState_strategy)
def test_hall_fsm_namedstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=NamedState_strategy)
@settings(max_examples=50)
def test_namedstate_instantiation(instance):
    assert isinstance(instance, NamedState)

@given(instance=InitialState_strategy)
@settings(max_examples=50)
def test_initialstate_instantiation(instance):
    assert isinstance(instance, InitialState)

@given(instance=FSM_HALL_Component_strategy)
@settings(max_examples=50)
def test_fsm_hall_component_instantiation(instance):
    assert isinstance(instance, FSM_HALL_Component)

@given(instance=HALL_FSM_FSM_strategy)
@settings(max_examples=50)
def test_hall_fsm_fsm_instantiation(instance):
    assert isinstance(instance, HALL_FSM_FSM)

@given(instance=Trigger_TriggerExpressionElement_strategy)
@settings(max_examples=50)
def test_trigger_triggerexpressionelement_instantiation(instance):
    assert isinstance(instance, Trigger_TriggerExpressionElement)

@given(instance=HALL_Trigger_TriggerExpression_strategy)
@settings(max_examples=50)
def test_hall_trigger_triggerexpression_instantiation(instance):
    assert isinstance(instance, HALL_Trigger_TriggerExpression)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=HALL_FSM_State_strategy)
@settings(max_examples=50)
def test_hall_fsm_state_instantiation(instance):
    assert isinstance(instance, HALL_FSM_State)



@given(instance=HALL_FSM_State_strategy)
def test_hall_fsm_state_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=Trigger_TriggerExpression_strategy)
@settings(max_examples=50)
def test_trigger_triggerexpression_instantiation(instance):
    assert isinstance(instance, Trigger_TriggerExpression)

@given(instance=FSMActions_ActionExpression_strategy)
@settings(max_examples=50)
def test_fsmactions_actionexpression_instantiation(instance):
    assert isinstance(instance, FSMActions_ActionExpression)

@given(instance=FSMInstructions_PosConditionExpression_strategy)
@settings(max_examples=50)
def test_fsminstructions_posconditionexpression_instantiation(instance):
    assert isinstance(instance, FSMInstructions_PosConditionExpression)

@given(instance=FSMConditions_PreConditionExpression_strategy)
@settings(max_examples=50)
def test_fsmconditions_preconditionexpression_instantiation(instance):
    assert isinstance(instance, FSMConditions_PreConditionExpression)

@given(instance=HALL_FSM_Transition_strategy)
@settings(max_examples=50)
def test_hall_fsm_transition_instantiation(instance):
    assert isinstance(instance, HALL_FSM_Transition)



@given(instance=HALL_FSM_Transition_strategy)
def test_hall_fsm_transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=ActionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_actionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, ActionMessageExpressionElement)

@given(instance=HALL_Actions_Literal_strategy)
@settings(max_examples=50)
def test_hall_actions_literal_instantiation(instance):
    assert isinstance(instance, HALL_Actions_Literal)



@given(instance=HALL_Actions_Literal_strategy)
def test_hall_actions_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL_Actions_Let_strategy)
@settings(max_examples=50)
def test_hall_actions_let_instantiation(instance):
    assert isinstance(instance, HALL_Actions_Let)



@given(instance=HALL_Actions_Let_strategy)
def test_hall_actions_let_namevar_setter(instance):
    original = instance.namevar
    instance.namevar = original
    assert instance.namevar == original

@given(instance=HALL_Actions_DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall_actions_domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL_Actions_DomainPropertyGet)



@given(instance=HALL_Actions_DomainPropertyGet_strategy)
def test_hall_actions_domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_FSMActions_Enable_strategy)
@settings(max_examples=50)
def test_hall_fsmactions_enable_instantiation(instance):
    assert isinstance(instance, HALL_FSMActions_Enable)

@given(instance=HALL_Actions_BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall_actions_binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_Actions_BinaryOperator)



@given(instance=HALL_Actions_BinaryOperator_strategy)
def test_hall_actions_binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_Actions_VarRef_strategy)
@settings(max_examples=50)
def test_hall_actions_varref_instantiation(instance):
    assert isinstance(instance, HALL_Actions_VarRef)



@given(instance=HALL_Actions_VarRef_strategy)
def test_hall_actions_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=HALL_Actions_VarRef_strategy)
def test_hall_actions_varref_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=HALL_Actions_ActionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_hall_actions_actionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, HALL_Actions_ActionMessageExpressionElement)

@given(instance=HALL_Actions_Enable_strategy)
@settings(max_examples=50)
def test_hall_actions_enable_instantiation(instance):
    assert isinstance(instance, HALL_Actions_Enable)

@given(instance=HALL_Actions_DomainPropertySet_strategy)
@settings(max_examples=50)
def test_hall_actions_domainpropertyset_instantiation(instance):
    assert isinstance(instance, HALL_Actions_DomainPropertySet)



@given(instance=HALL_Actions_DomainPropertySet_strategy)
def test_hall_actions_domainpropertyset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Actions_HALL_Component_strategy)
@settings(max_examples=50)
def test_actions_hall_component_instantiation(instance):
    assert isinstance(instance, Actions_HALL_Component)

@given(instance=HALL_Actions_GetData_strategy)
@settings(max_examples=50)
def test_hall_actions_getdata_instantiation(instance):
    assert isinstance(instance, HALL_Actions_GetData)



@given(instance=HALL_Actions_GetData_strategy)
def test_hall_actions_getdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Actions_UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall_actions_unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_Actions_UnaryOperator)



@given(instance=HALL_Actions_UnaryOperator_strategy)
def test_hall_actions_unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_Actions_MessageInvocation_strategy)
@settings(max_examples=50)
def test_hall_actions_messageinvocation_instantiation(instance):
    assert isinstance(instance, HALL_Actions_MessageInvocation)



@given(instance=HALL_Actions_MessageInvocation_strategy)
def test_hall_actions_messageinvocation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=HALL_Actions_MessageInvocation_strategy)
def test_hall_actions_messageinvocation_isTopDown_setter(instance):
    original = instance.isTopDown
    instance.isTopDown = original
    assert instance.isTopDown == original

@given(instance=HALL_Actions_GetMessageParameter_strategy)
@settings(max_examples=50)
def test_hall_actions_getmessageparameter_instantiation(instance):
    assert isinstance(instance, HALL_Actions_GetMessageParameter)



@given(instance=HALL_Actions_GetMessageParameter_strategy)
def test_hall_actions_getmessageparameter_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Actions_GetMessageData_strategy)
@settings(max_examples=50)
def test_hall_actions_getmessagedata_instantiation(instance):
    assert isinstance(instance, HALL_Actions_GetMessageData)



@given(instance=HALL_Actions_GetMessageData_strategy)
def test_hall_actions_getmessagedata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=Conditions_HALL_Component_strategy)
@settings(max_examples=50)
def test_conditions_hall_component_instantiation(instance):
    assert isinstance(instance, Conditions_HALL_Component)

@given(instance=PreConditionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_preconditionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, PreConditionMessageExpressionElement)

@given(instance=HALL_Conditions_DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall_conditions_domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_DomainPropertyGet)



@given(instance=HALL_Conditions_DomainPropertyGet_strategy)
def test_hall_conditions_domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_Conditions_GetMessageData_strategy)
@settings(max_examples=50)
def test_hall_conditions_getmessagedata_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_GetMessageData)



@given(instance=HALL_Conditions_GetMessageData_strategy)
def test_hall_conditions_getmessagedata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Conditions_Literal_strategy)
@settings(max_examples=50)
def test_hall_conditions_literal_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_Literal)



@given(instance=HALL_Conditions_Literal_strategy)
def test_hall_conditions_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL_Conditions_GetData_strategy)
@settings(max_examples=50)
def test_hall_conditions_getdata_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_GetData)



@given(instance=HALL_Conditions_GetData_strategy)
def test_hall_conditions_getdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Conditions_GetState_strategy)
@settings(max_examples=50)
def test_hall_conditions_getstate_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_GetState)

@given(instance=HALL_Conditions_GetMessageParameter_strategy)
@settings(max_examples=50)
def test_hall_conditions_getmessageparameter_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_GetMessageParameter)



@given(instance=HALL_Conditions_GetMessageParameter_strategy)
def test_hall_conditions_getmessageparameter_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Conditions_VarRef_strategy)
@settings(max_examples=50)
def test_hall_conditions_varref_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_VarRef)



@given(instance=HALL_Conditions_VarRef_strategy)
def test_hall_conditions_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=HALL_Conditions_VarRef_strategy)
def test_hall_conditions_varref_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=HALL_Conditions_PreConditionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_hall_conditions_preconditionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_PreConditionMessageExpressionElement)

@given(instance=Conditions_PreConditionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_conditions_preconditionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, Conditions_PreConditionMessageExpressionElement)

@given(instance=Actions_ActionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_actions_actionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, Actions_ActionMessageExpressionElement)

@given(instance=HALL_Actions_ActionMessageExpression_strategy)
@settings(max_examples=50)
def test_hall_actions_actionmessageexpression_instantiation(instance):
    assert isinstance(instance, HALL_Actions_ActionMessageExpression)

@given(instance=HALL_Conditions_BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall_conditions_binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_BinaryOperator)



@given(instance=HALL_Conditions_BinaryOperator_strategy)
def test_hall_conditions_binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_Conditions_UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall_conditions_unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_UnaryOperator)



@given(instance=HALL_Conditions_UnaryOperator_strategy)
def test_hall_conditions_unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_Conditions_Let_strategy)
@settings(max_examples=50)
def test_hall_conditions_let_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_Let)



@given(instance=HALL_Conditions_Let_strategy)
def test_hall_conditions_let_namevar_setter(instance):
    original = instance.namevar
    instance.namevar = original
    assert instance.namevar == original

@given(instance=HALL_Conditions_PreConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_hall_conditions_preconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, HALL_Conditions_PreConditionMessageExpression)

@given(instance=HALL_Instructions_PosConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_hall_instructions_posconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_PosConditionMessageExpression)

@given(instance=MessageTransition_strategy)
@settings(max_examples=50)
def test_messagetransition_instantiation(instance):
    assert isinstance(instance, MessageTransition)

@given(instance=HALL_Messages_MessageState_strategy)
@settings(max_examples=50)
def test_hall_messages_messagestate_instantiation(instance):
    assert isinstance(instance, HALL_Messages_MessageState)



@given(instance=HALL_Messages_MessageState_strategy)
def test_hall_messages_messagestate_isContinue_setter(instance):
    original = instance.isContinue
    instance.isContinue = original
    assert instance.isContinue == original



@given(instance=HALL_Messages_MessageState_strategy)
def test_hall_messages_messagestate_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original



@given(instance=HALL_Messages_MessageState_strategy)
def test_hall_messages_messagestate_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original

@given(instance=Messages_HALL_Component_strategy)
@settings(max_examples=50)
def test_messages_hall_component_instantiation(instance):
    assert isinstance(instance, Messages_HALL_Component)

@given(instance=InitialMessageState_strategy)
@settings(max_examples=50)
def test_initialmessagestate_instantiation(instance):
    assert isinstance(instance, InitialMessageState)

@given(instance=NamedMessageState_strategy)
@settings(max_examples=50)
def test_namedmessagestate_instantiation(instance):
    assert isinstance(instance, NamedMessageState)

@given(instance=HALL_Messages_MessageHandler_strategy)
@settings(max_examples=50)
def test_hall_messages_messagehandler_instantiation(instance):
    assert isinstance(instance, HALL_Messages_MessageHandler)



@given(instance=HALL_Messages_MessageHandler_strategy)
def test_hall_messages_messagehandler_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Messages_HALL_Data_strategy)
@settings(max_examples=50)
def test_messages_hall_data_instantiation(instance):
    assert isinstance(instance, Messages_HALL_Data)

@given(instance=Instructions_HALL_Component_strategy)
@settings(max_examples=50)
def test_instructions_hall_component_instantiation(instance):
    assert isinstance(instance, Instructions_HALL_Component)

@given(instance=PosConditionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_posconditionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, PosConditionMessageExpressionElement)

@given(instance=HALL_Instructions_GetMessageParameter_strategy)
@settings(max_examples=50)
def test_hall_instructions_getmessageparameter_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_GetMessageParameter)



@given(instance=HALL_Instructions_GetMessageParameter_strategy)
def test_hall_instructions_getmessageparameter_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Instructions_GetData_strategy)
@settings(max_examples=50)
def test_hall_instructions_getdata_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_GetData)



@given(instance=HALL_Instructions_GetData_strategy)
def test_hall_instructions_getdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Instructions_Let_strategy)
@settings(max_examples=50)
def test_hall_instructions_let_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_Let)



@given(instance=HALL_Instructions_Let_strategy)
def test_hall_instructions_let_namevar_setter(instance):
    original = instance.namevar
    instance.namevar = original
    assert instance.namevar == original

@given(instance=HALL_Instructions_SetMessageParameter_strategy)
@settings(max_examples=50)
def test_hall_instructions_setmessageparameter_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_SetMessageParameter)



@given(instance=HALL_Instructions_SetMessageParameter_strategy)
def test_hall_instructions_setmessageparameter_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Instructions_SetData_strategy)
@settings(max_examples=50)
def test_hall_instructions_setdata_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_SetData)



@given(instance=HALL_Instructions_SetData_strategy)
def test_hall_instructions_setdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Instructions_SetTopDown_strategy)
@settings(max_examples=50)
def test_hall_instructions_settopdown_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_SetTopDown)

@given(instance=HALL_Instructions_DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall_instructions_domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_DomainPropertyGet)



@given(instance=HALL_Instructions_DomainPropertyGet_strategy)
def test_hall_instructions_domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_Instructions_GetMessageData_strategy)
@settings(max_examples=50)
def test_hall_instructions_getmessagedata_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_GetMessageData)



@given(instance=HALL_Instructions_GetMessageData_strategy)
def test_hall_instructions_getmessagedata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Instructions_SetState_strategy)
@settings(max_examples=50)
def test_hall_instructions_setstate_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_SetState)



@given(instance=HALL_Instructions_SetState_strategy)
def test_hall_instructions_setstate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_Instructions_GetState_strategy)
@settings(max_examples=50)
def test_hall_instructions_getstate_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_GetState)

@given(instance=HALL_Instructions_UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall_instructions_unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_UnaryOperator)



@given(instance=HALL_Instructions_UnaryOperator_strategy)
def test_hall_instructions_unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_Instructions_BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall_instructions_binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_BinaryOperator)



@given(instance=HALL_Instructions_BinaryOperator_strategy)
def test_hall_instructions_binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL_Instructions_SetMessageData_strategy)
@settings(max_examples=50)
def test_hall_instructions_setmessagedata_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_SetMessageData)



@given(instance=HALL_Instructions_SetMessageData_strategy)
def test_hall_instructions_setmessagedata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL_Instructions_Literal_strategy)
@settings(max_examples=50)
def test_hall_instructions_literal_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_Literal)



@given(instance=HALL_Instructions_Literal_strategy)
def test_hall_instructions_literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL_Instructions_VarRef_strategy)
@settings(max_examples=50)
def test_hall_instructions_varref_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_VarRef)



@given(instance=HALL_Instructions_VarRef_strategy)
def test_hall_instructions_varref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=HALL_Instructions_VarRef_strategy)
def test_hall_instructions_varref_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=HALL_Instructions_PosConditionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_hall_instructions_posconditionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, HALL_Instructions_PosConditionMessageExpressionElement)

@given(instance=Instructions_PosConditionMessageExpressionElement_strategy)
@settings(max_examples=50)
def test_instructions_posconditionmessageexpressionelement_instantiation(instance):
    assert isinstance(instance, Instructions_PosConditionMessageExpressionElement)

@given(instance=GeometryData2D_strategy)
@settings(max_examples=50)
def test_geometrydata2d_instantiation(instance):
    assert isinstance(instance, GeometryData2D)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=HALL_Geometry_Point2D_strategy)
@settings(max_examples=50)
def test_hall_geometry_point2d_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_Point2D)

@given(instance=HALL_Geometry_Point3D_strategy)
@settings(max_examples=50)
def test_hall_geometry_point3d_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_Point3D)



@given(instance=HALL_Geometry_Point3D_strategy)
def test_hall_geometry_point3d_zCoord_setter(instance):
    original = instance.zCoord
    instance.zCoord = original
    assert instance.zCoord == original

@given(instance=GeometryData3D_strategy)
@settings(max_examples=50)
def test_geometrydata3d_instantiation(instance):
    assert isinstance(instance, GeometryData3D)

@given(instance=Point3D_strategy)
@settings(max_examples=50)
def test_point3d_instantiation(instance):
    assert isinstance(instance, Point3D)

@given(instance=HALL_Geometry_Face_strategy)
@settings(max_examples=50)
def test_hall_geometry_face_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_Face)



@given(instance=HALL_Geometry_Face_strategy)
def test_hall_geometry_face_labelText_setter(instance):
    original = instance.labelText
    instance.labelText = original
    assert instance.labelText == original

@given(instance=Point2D_strategy)
@settings(max_examples=50)
def test_point2d_instantiation(instance):
    assert isinstance(instance, Point2D)

@given(instance=Messages_HALL_Parameter_strategy)
@settings(max_examples=50)
def test_messages_hall_parameter_instantiation(instance):
    assert isinstance(instance, Messages_HALL_Parameter)

@given(instance=Messages_HALL_Model_strategy)
@settings(max_examples=50)
def test_messages_hall_model_instantiation(instance):
    assert isinstance(instance, Messages_HALL_Model)

@given(instance=HALL_Messages_MessageDefinition_strategy)
@settings(max_examples=50)
def test_hall_messages_messagedefinition_instantiation(instance):
    assert isinstance(instance, HALL_Messages_MessageDefinition)



@given(instance=HALL_Messages_MessageDefinition_strategy)
def test_hall_messages_messagedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Actions_ActionMessageExpression_strategy)
@settings(max_examples=50)
def test_actions_actionmessageexpression_instantiation(instance):
    assert isinstance(instance, Actions_ActionMessageExpression)

@given(instance=Instructions_PosConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_instructions_posconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, Instructions_PosConditionMessageExpression)

@given(instance=Conditions_PreConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_conditions_preconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, Conditions_PreConditionMessageExpression)

@given(instance=MessageState_strategy)
@settings(max_examples=50)
def test_messagestate_instantiation(instance):
    assert isinstance(instance, MessageState)

@given(instance=HALL_Messages_InitialMessageState_strategy)
@settings(max_examples=50)
def test_hall_messages_initialmessagestate_instantiation(instance):
    assert isinstance(instance, HALL_Messages_InitialMessageState)

@given(instance=HALL_Messages_NamedMessageState_strategy)
@settings(max_examples=50)
def test_hall_messages_namedmessagestate_instantiation(instance):
    assert isinstance(instance, HALL_Messages_NamedMessageState)



@given(instance=HALL_Messages_NamedMessageState_strategy)
def test_hall_messages_namedmessagestate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_Messages_MessageTransition_strategy)
@settings(max_examples=50)
def test_hall_messages_messagetransition_instantiation(instance):
    assert isinstance(instance, HALL_Messages_MessageTransition)



@given(instance=HALL_Messages_MessageTransition_strategy)
def test_hall_messages_messagetransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_Geometry_Point_strategy)
@settings(max_examples=50)
def test_hall_geometry_point_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_Point)



@given(instance=HALL_Geometry_Point_strategy)
def test_hall_geometry_point_xCoord_setter(instance):
    original = instance.xCoord
    instance.xCoord = original
    assert instance.xCoord == original



@given(instance=HALL_Geometry_Point_strategy)
def test_hall_geometry_point_yCoord_setter(instance):
    original = instance.yCoord
    instance.yCoord = original
    assert instance.yCoord == original

@given(instance=HALL_Geometry_AlphaTransparency_strategy)
@settings(max_examples=50)
def test_hall_geometry_alphatransparency_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_AlphaTransparency)



@given(instance=HALL_Geometry_AlphaTransparency_strategy)
def test_hall_geometry_alphatransparency_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AlphaTransparency_strategy)
@settings(max_examples=50)
def test_alphatransparency_instantiation(instance):
    assert isinstance(instance, AlphaTransparency)

@given(instance=HALL_Geometry_ColorState_strategy)
@settings(max_examples=50)
def test_hall_geometry_colorstate_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_ColorState)

@given(instance=Face_strategy)
@settings(max_examples=50)
def test_face_instantiation(instance):
    assert isinstance(instance, Face)

@given(instance=HALL_Geometry_GeometryData_strategy)
@settings(max_examples=50)
def test_hall_geometry_geometrydata_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_GeometryData)

@given(instance=Geometry_HALL_VisualObject_strategy)
@settings(max_examples=50)
def test_geometry_hall_visualobject_instantiation(instance):
    assert isinstance(instance, Geometry_HALL_VisualObject)

@given(instance=NormalColors_strategy)
@settings(max_examples=50)
def test_normalcolors_instantiation(instance):
    assert isinstance(instance, NormalColors)

@given(instance=DisabledColors_strategy)
@settings(max_examples=50)
def test_disabledcolors_instantiation(instance):
    assert isinstance(instance, DisabledColors)

@given(instance=SelectedColors_strategy)
@settings(max_examples=50)
def test_selectedcolors_instantiation(instance):
    assert isinstance(instance, SelectedColors)

@given(instance=HALL_Geometry_ColorData_strategy)
@settings(max_examples=50)
def test_hall_geometry_colordata_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_ColorData)

@given(instance=HALL_Parameter_strategy)
@settings(max_examples=50)
def test_hall_parameter_instantiation(instance):
    assert isinstance(instance, HALL_Parameter)



@given(instance=HALL_Parameter_strategy)
def test_hall_parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=HALL_Parameter_strategy)
def test_hall_parameter_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Color_strategy)
@settings(max_examples=50)
def test_color_instantiation(instance):
    assert isinstance(instance, Color)

@given(instance=HALL_Geometry_RGBColor_strategy)
@settings(max_examples=50)
def test_hall_geometry_rgbcolor_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_RGBColor)



@given(instance=HALL_Geometry_RGBColor_strategy)
def test_hall_geometry_rgbcolor_greenValue_setter(instance):
    original = instance.greenValue
    instance.greenValue = original
    assert instance.greenValue == original



@given(instance=HALL_Geometry_RGBColor_strategy)
def test_hall_geometry_rgbcolor_blueValue_setter(instance):
    original = instance.blueValue
    instance.blueValue = original
    assert instance.blueValue == original



@given(instance=HALL_Geometry_RGBColor_strategy)
def test_hall_geometry_rgbcolor_redValue_setter(instance):
    original = instance.redValue
    instance.redValue = original
    assert instance.redValue == original

@given(instance=ColorState_strategy)
@settings(max_examples=50)
def test_colorstate_instantiation(instance):
    assert isinstance(instance, ColorState)

@given(instance=HALL_Geometry_SelectedColors_strategy)
@settings(max_examples=50)
def test_hall_geometry_selectedcolors_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_SelectedColors)

@given(instance=HALL_Geometry_DisabledColors_strategy)
@settings(max_examples=50)
def test_hall_geometry_disabledcolors_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_DisabledColors)

@given(instance=HALL_Geometry_NormalColors_strategy)
@settings(max_examples=50)
def test_hall_geometry_normalcolors_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_NormalColors)

@given(instance=RGBColor_strategy)
@settings(max_examples=50)
def test_rgbcolor_instantiation(instance):
    assert isinstance(instance, RGBColor)

@given(instance=HALL_Geometry_Color_strategy)
@settings(max_examples=50)
def test_hall_geometry_color_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_Color)

@given(instance=MessageDefinition_strategy)
@settings(max_examples=50)
def test_messagedefinition_instantiation(instance):
    assert isinstance(instance, MessageDefinition)

@given(instance=HALL_Goal_strategy)
@settings(max_examples=50)
def test_hall_goal_instantiation(instance):
    assert isinstance(instance, HALL_Goal)



@given(instance=HALL_Goal_strategy)
def test_hall_goal_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=GeometryData_strategy)
@settings(max_examples=50)
def test_geometrydata_instantiation(instance):
    assert isinstance(instance, GeometryData)

@given(instance=HALL_Geometry_GeometryData3D_strategy)
@settings(max_examples=50)
def test_hall_geometry_geometrydata3d_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_GeometryData3D)

@given(instance=HALL_Geometry_GeometryData2D_strategy)
@settings(max_examples=50)
def test_hall_geometry_geometrydata2d_instantiation(instance):
    assert isinstance(instance, HALL_Geometry_GeometryData2D)



@given(instance=HALL_Geometry_GeometryData2D_strategy)
def test_hall_geometry_geometrydata2d_labelText_setter(instance):
    original = instance.labelText
    instance.labelText = original
    assert instance.labelText == original

@given(instance=ColorData_strategy)
@settings(max_examples=50)
def test_colordata_instantiation(instance):
    assert isinstance(instance, ColorData)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=HALL_TaskObject_strategy)
@settings(max_examples=50)
def test_hall_taskobject_instantiation(instance):
    assert isinstance(instance, HALL_TaskObject)



@given(instance=HALL_TaskObject_strategy)
def test_hall_taskobject_completionTime_setter(instance):
    original = instance.completionTime
    instance.completionTime = original
    assert instance.completionTime == original



@given(instance=HALL_TaskObject_strategy)
def test_hall_taskobject_numberofgoalscompleted_setter(instance):
    original = instance.numberofgoalscompleted
    instance.numberofgoalscompleted = original
    assert instance.numberofgoalscompleted == original

@given(instance=HALL_VisualObject_strategy)
@settings(max_examples=50)
def test_hall_visualobject_instantiation(instance):
    assert isinstance(instance, HALL_VisualObject)

@given(instance=HALL_Model_strategy)
@settings(max_examples=50)
def test_hall_model_instantiation(instance):
    assert isinstance(instance, HALL_Model)

@given(instance=HALL_SystemComponent_strategy)
@settings(max_examples=50)
def test_hall_systemcomponent_instantiation(instance):
    assert isinstance(instance, HALL_SystemComponent)

@given(instance=MessageHandler_strategy)
@settings(max_examples=50)
def test_messagehandler_instantiation(instance):
    assert isinstance(instance, MessageHandler)

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=HALL_Data_strategy)
@settings(max_examples=50)
def test_hall_data_instantiation(instance):
    assert isinstance(instance, HALL_Data)



@given(instance=HALL_Data_strategy)
def test_hall_data_initValue_setter(instance):
    original = instance.initValue
    instance.initValue = original
    assert instance.initValue == original



@given(instance=HALL_Data_strategy)
def test_hall_data_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=HALL_Data_strategy)
def test_hall_data_currentValue_setter(instance):
    original = instance.currentValue
    instance.currentValue = original
    assert instance.currentValue == original



@given(instance=HALL_Data_strategy)
def test_hall_data_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_Component_strategy)
@settings(max_examples=50)
def test_hall_component_instantiation(instance):
    assert isinstance(instance, HALL_Component)



@given(instance=HALL_Component_strategy)
def test_hall_component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL_UserProfile_strategy)
@settings(max_examples=50)
def test_hall_userprofile_instantiation(instance):
    assert isinstance(instance, HALL_UserProfile)



@given(instance=HALL_UserProfile_strategy)
def test_hall_userprofile_numberofcompletedtasks_setter(instance):
    original = instance.numberofcompletedtasks
    instance.numberofcompletedtasks = original
    assert instance.numberofcompletedtasks == original
