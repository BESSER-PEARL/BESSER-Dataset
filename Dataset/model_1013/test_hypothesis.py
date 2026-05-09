import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Messages::HALL::Parameter,
    Messages::HALL::Model,
    HALL::Messages::MessageDefinition,
    Actions::ActionMessage,
    Instructions::PosConditionMessage,
    Conditions::PreConditionMessage,
    MessageState,
    HALL::Messages::RegularMessageState,
    HALL::Messages::MessageTransition,
    HALL::Geometry::Point,
    GeometryData2D,
    HALL::Geometry::AlphaTransparency,
    AlphaTransparency,
    Point2D,
    Face,
    HALL::Geometry::GeometryData,
    Geometry::HALL::VisualObject,
    NormalColors,
    DisabledColors,
    SelectedColors,
    HALL::Geometry::ColorData,
    HALL::Parameter,
    HALL::Geometry::ColorState,
    Color,
    HALL::Geometry::RGBColor,
    ColorState,
    HALL::Geometry::SelectedColors,
    HALL::Geometry::DisabledColors,
    HALL::Geometry::NormalColors,
    RGBColor,
    HALL::Geometry::Color,
    Type,
    MessageDefinition,
    HALL::Goal,
    ColorData,
    Component,
    HALL::TaskObject,
    HALL::VisualObject,
    HALL::Model,
    HALL::SystemComponent,
    MessageHandler,
    FSM,
    HALL::Data,
    HALL::Component,
    HALL::UserProfile,
    GeometryData,
    HALL::Geometry::GeometryData3D,
    HALL::Geometry::GeometryData2D,
    FSMActions::Let,
    SimpleType,
    HALL::Types::Boolean,
    HALL::Types::Number,
    HALL::Types::String,
    HALL::Types::Set,
    Set,
    HALL::Types::SimpleType,
    HALL::Types::Type,
    FSMActions::HALL::Data,
    FSMConditions::HALL::Component,
    ActionExpression,
    HALL::FSMActions::VarRef,
    HALL::FSMActions::DomainPropertySet,
    HALL::FSMActions::UnaryOperator,
    HALL::FSMActions::Let,
    HALL::FSMActions::GetData,
    HALL::FSMActions::BinaryOperator,
    HALL::FSMActions::MessageInvocation,
    HALL::FSMActions::DomainPropertyGet,
    HALL::FSMActions::Literal,
    HALL::FSMActions::ActionExpression,
    FSMActions::ActionExpression,
    HALL::FSMActions::Action,
    FSMConditions::Let,
    FSMConditions::HALL::Data,
    PreConditionExpression,
    HALL::FSMConditions::DomainPropertyGet,
    HALL::FSMConditions::UnaryOperator,
    HALL::FSMConditions::VarRef,
    HALL::FSMConditions::GetState,
    HALL::FSMConditions::BinaryOperator,
    HALL::FSMConditions::GetData,
    HALL::FSMConditions::Let,
    HALL::FSMConditions::Literal,
    HALL::FSMConditions::PreConditionExpression,
    FSMConditions::PreConditionExpression,
    HALL::FSMConditions::PreCondition,
    FSMInstructions::Let,
    FSMInstructions::HALL::Data,
    TriggerExpression,
    HALL::Trigger::MessageNotification,
    HALL::Trigger::TriggerExpression,
    Trigger::TriggerExpression,
    HALL::Trigger::Trigger,
    FSMInstructions::HALL::Component,
    PosConditionExpression,
    HALL::FSMInstructions::UnaryOperator,
    HALL::FSMInstructions::Let,
    HALL::FSMInstructions::GetState,
    HALL::FSMInstructions::SetState,
    HALL::FSMInstructions::VarRef,
    HALL::FSMInstructions::BinaryOperator,
    HALL::FSMInstructions::GetData,
    HALL::FSMInstructions::SetData,
    HALL::FSMInstructions::DomainPropertyGet,
    HALL::FSMInstructions::Literal,
    HALL::FSMInstructions::PosConditionExpression,
    FSMInstructions::PosConditionExpression,
    HALL::FSMInstructions::PosCondition,
    HALL::Trigger::DomainEventFired,
    RegularState,
    InitialState,
    FSM::HALL::Component,
    HALL::FSM::FSM,
    Transition,
    HALL::FSM::State,
    Trigger::Trigger,
    FSMActions::Action,
    FSMInstructions::PosCondition,
    FSMConditions::PreCondition,
    HALL::FSM::Transition,
    Actions::HALL::Component,
    Actions::Let,
    ActionMessageExpression,
    HALL::Actions::UnaryOperator,
    HALL::Actions::GetMessageParameter,
    HALL::FSMActions::Enable,
    HALL::Actions::DomainPropertySet,
    HALL::Actions::Enable,
    HALL::Actions::MessageInvocation,
    HALL::Actions::GetMessageData,
    HALL::Actions::BinaryOperator,
    HALL::Actions::Literal,
    HALL::Actions::Let,
    HALL::Actions::DomainPropertyGet,
    HALL::Actions::GetData,
    HALL::Actions::VarRef,
    HALL::Actions::ActionMessageExpression,
    Actions::ActionMessageExpression,
    HALL::Actions::ActionMessage,
    Conditions::Let,
    Conditions::HALL::Data,
    Conditions::HALL::Component,
    PreConditionMessageExpression,
    HALL::Conditions::GetMessageData,
    HALL::Conditions::GetState,
    HALL::Conditions::UnaryOperator,
    HALL::Conditions::GetData,
    HALL::Conditions::VarRef,
    HALL::Conditions::Let,
    HALL::Conditions::GetMessageParameter,
    HALL::Conditions::DomainPropertyGet,
    HALL::Conditions::BinaryOperator,
    HALL::Conditions::Literal,
    HALL::Conditions::PreConditionMessageExpression,
    Conditions::PreConditionMessageExpression,
    HALL::Conditions::PreConditionMessage,
    Instructions::Let,
    Instructions::HALL::Component,
    Instructions::HALL::Data,
    State,
    HALL::FSM::RegularState,
    HALL::FSM::InitialState,
    RegularMessageState,
    HALL::Messages::MessageHandler,
    Messages::HALL::Data,
    PosConditionMessageExpression,
    HALL::Instructions::SetTopDown,
    HALL::Instructions::UnaryOperator,
    HALL::Instructions::GetData,
    HALL::Instructions::GetMessageData,
    HALL::Instructions::VarRef,
    HALL::Instructions::DomainPropertyGet,
    HALL::Instructions::Let,
    HALL::Instructions::SetMessageParameter,
    HALL::Instructions::SetMessageData,
    HALL::Instructions::SetState,
    HALL::Instructions::GetMessageParameter,
    HALL::Instructions::SetData,
    HALL::Instructions::GetState,
    HALL::Instructions::BinaryOperator,
    HALL::Instructions::Literal,
    HALL::Instructions::PosConditionMessageExpression,
    Instructions::PosConditionMessageExpression,
    HALL::Instructions::PosConditionMessage,
    HALL::Messages::InitialMessageState,
    MessageTransition,
    HALL::Messages::MessageState,
    Messages::HALL::Component,
    InitialMessageState,
    Point,
    HALL::Geometry::Point2D,
    HALL::Geometry::Point3D,
    GeometryData3D,
    Point3D,
    HALL::Geometry::Face,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_messages::hall::parameter_is_not_abstract():
    assert not inspect.isabstract(Messages::HALL::Parameter)


def test_messages::hall::parameter_constructor_exists():
    assert callable(Messages::HALL::Parameter.__init__)


def test_messages::hall::parameter_constructor_args():
    sig = inspect.signature(Messages::HALL::Parameter.__init__)
    params = list(sig.parameters.keys())



def test_messages::hall::model_is_not_abstract():
    assert not inspect.isabstract(Messages::HALL::Model)


def test_messages::hall::model_constructor_exists():
    assert callable(Messages::HALL::Model.__init__)


def test_messages::hall::model_constructor_args():
    sig = inspect.signature(Messages::HALL::Model.__init__)
    params = list(sig.parameters.keys())



def test_hall::messages::messagedefinition_is_not_abstract():
    assert not inspect.isabstract(HALL::Messages::MessageDefinition)


def test_hall::messages::messagedefinition_constructor_exists():
    assert callable(HALL::Messages::MessageDefinition.__init__)


def test_hall::messages::messagedefinition_constructor_args():
    sig = inspect.signature(HALL::Messages::MessageDefinition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::messages::messagedefinition_has_name():
    assert hasattr(HALL::Messages::MessageDefinition, "name")
    descriptor = None
    for klass in HALL::Messages::MessageDefinition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_actions::actionmessage_is_not_abstract():
    assert not inspect.isabstract(Actions::ActionMessage)


def test_actions::actionmessage_constructor_exists():
    assert callable(Actions::ActionMessage.__init__)


def test_actions::actionmessage_constructor_args():
    sig = inspect.signature(Actions::ActionMessage.__init__)
    params = list(sig.parameters.keys())



def test_instructions::posconditionmessage_is_not_abstract():
    assert not inspect.isabstract(Instructions::PosConditionMessage)


def test_instructions::posconditionmessage_constructor_exists():
    assert callable(Instructions::PosConditionMessage.__init__)


def test_instructions::posconditionmessage_constructor_args():
    sig = inspect.signature(Instructions::PosConditionMessage.__init__)
    params = list(sig.parameters.keys())



def test_conditions::preconditionmessage_is_not_abstract():
    assert not inspect.isabstract(Conditions::PreConditionMessage)


def test_conditions::preconditionmessage_constructor_exists():
    assert callable(Conditions::PreConditionMessage.__init__)


def test_conditions::preconditionmessage_constructor_args():
    sig = inspect.signature(Conditions::PreConditionMessage.__init__)
    params = list(sig.parameters.keys())



def test_messagestate_is_not_abstract():
    assert not inspect.isabstract(MessageState)


def test_messagestate_constructor_exists():
    assert callable(MessageState.__init__)


def test_messagestate_constructor_args():
    sig = inspect.signature(MessageState.__init__)
    params = list(sig.parameters.keys())



def test_hall::messages::regularmessagestate_is_not_abstract():
    assert not inspect.isabstract(HALL::Messages::RegularMessageState)


def test_hall::messages::regularmessagestate_constructor_exists():
    assert callable(HALL::Messages::RegularMessageState.__init__)


def test_hall::messages::regularmessagestate_constructor_args():
    sig = inspect.signature(HALL::Messages::RegularMessageState.__init__)
    params = list(sig.parameters.keys())



def test_hall::messages::messagetransition_is_not_abstract():
    assert not inspect.isabstract(HALL::Messages::MessageTransition)


def test_hall::messages::messagetransition_constructor_exists():
    assert callable(HALL::Messages::MessageTransition.__init__)


def test_hall::messages::messagetransition_constructor_args():
    sig = inspect.signature(HALL::Messages::MessageTransition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::messages::messagetransition_has_name():
    assert hasattr(HALL::Messages::MessageTransition, "name")
    descriptor = None
    for klass in HALL::Messages::MessageTransition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::geometry::point_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::Point)


def test_hall::geometry::point_constructor_exists():
    assert callable(HALL::Geometry::Point.__init__)


def test_hall::geometry::point_constructor_args():
    sig = inspect.signature(HALL::Geometry::Point.__init__)
    params = list(sig.parameters.keys())
    assert "yCoord" in params, "Missing parameter 'yCoord'"
    assert "xCoord" in params, "Missing parameter 'xCoord'"

def test_hall::geometry::point_has_yCoord():
    assert hasattr(HALL::Geometry::Point, "yCoord")
    descriptor = None
    for klass in HALL::Geometry::Point.__mro__:
        if "yCoord" in klass.__dict__:
            descriptor = klass.__dict__["yCoord"]
            break
    assert isinstance(descriptor, property)

def test_hall::geometry::point_has_xCoord():
    assert hasattr(HALL::Geometry::Point, "xCoord")
    descriptor = None
    for klass in HALL::Geometry::Point.__mro__:
        if "xCoord" in klass.__dict__:
            descriptor = klass.__dict__["xCoord"]
            break
    assert isinstance(descriptor, property)



def test_geometrydata2d_is_not_abstract():
    assert not inspect.isabstract(GeometryData2D)


def test_geometrydata2d_constructor_exists():
    assert callable(GeometryData2D.__init__)


def test_geometrydata2d_constructor_args():
    sig = inspect.signature(GeometryData2D.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::alphatransparency_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::AlphaTransparency)


def test_hall::geometry::alphatransparency_constructor_exists():
    assert callable(HALL::Geometry::AlphaTransparency.__init__)


def test_hall::geometry::alphatransparency_constructor_args():
    sig = inspect.signature(HALL::Geometry::AlphaTransparency.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall::geometry::alphatransparency_has_value():
    assert hasattr(HALL::Geometry::AlphaTransparency, "value")
    descriptor = None
    for klass in HALL::Geometry::AlphaTransparency.__mro__:
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



def test_point2d_is_not_abstract():
    assert not inspect.isabstract(Point2D)


def test_point2d_constructor_exists():
    assert callable(Point2D.__init__)


def test_point2d_constructor_args():
    sig = inspect.signature(Point2D.__init__)
    params = list(sig.parameters.keys())



def test_face_is_not_abstract():
    assert not inspect.isabstract(Face)


def test_face_constructor_exists():
    assert callable(Face.__init__)


def test_face_constructor_args():
    sig = inspect.signature(Face.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::geometrydata_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::GeometryData)


def test_hall::geometry::geometrydata_constructor_exists():
    assert callable(HALL::Geometry::GeometryData.__init__)


def test_hall::geometry::geometrydata_constructor_args():
    sig = inspect.signature(HALL::Geometry::GeometryData.__init__)
    params = list(sig.parameters.keys())



def test_geometry::hall::visualobject_is_not_abstract():
    assert not inspect.isabstract(Geometry::HALL::VisualObject)


def test_geometry::hall::visualobject_constructor_exists():
    assert callable(Geometry::HALL::VisualObject.__init__)


def test_geometry::hall::visualobject_constructor_args():
    sig = inspect.signature(Geometry::HALL::VisualObject.__init__)
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



def test_hall::geometry::colordata_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::ColorData)


def test_hall::geometry::colordata_constructor_exists():
    assert callable(HALL::Geometry::ColorData.__init__)


def test_hall::geometry::colordata_constructor_args():
    sig = inspect.signature(HALL::Geometry::ColorData.__init__)
    params = list(sig.parameters.keys())



def test_hall::parameter_is_not_abstract():
    assert not inspect.isabstract(HALL::Parameter)


def test_hall::parameter_constructor_exists():
    assert callable(HALL::Parameter.__init__)


def test_hall::parameter_constructor_args():
    sig = inspect.signature(HALL::Parameter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::parameter_has_name():
    assert hasattr(HALL::Parameter, "name")
    descriptor = None
    for klass in HALL::Parameter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::geometry::colorstate_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::ColorState)


def test_hall::geometry::colorstate_constructor_exists():
    assert callable(HALL::Geometry::ColorState.__init__)


def test_hall::geometry::colorstate_constructor_args():
    sig = inspect.signature(HALL::Geometry::ColorState.__init__)
    params = list(sig.parameters.keys())



def test_color_is_not_abstract():
    assert not inspect.isabstract(Color)


def test_color_constructor_exists():
    assert callable(Color.__init__)


def test_color_constructor_args():
    sig = inspect.signature(Color.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::rgbcolor_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::RGBColor)


def test_hall::geometry::rgbcolor_constructor_exists():
    assert callable(HALL::Geometry::RGBColor.__init__)


def test_hall::geometry::rgbcolor_constructor_args():
    sig = inspect.signature(HALL::Geometry::RGBColor.__init__)
    params = list(sig.parameters.keys())
    assert "blueValue" in params, "Missing parameter 'blueValue'"
    assert "greenValue" in params, "Missing parameter 'greenValue'"
    assert "redValue" in params, "Missing parameter 'redValue'"

def test_hall::geometry::rgbcolor_has_blueValue():
    assert hasattr(HALL::Geometry::RGBColor, "blueValue")
    descriptor = None
    for klass in HALL::Geometry::RGBColor.__mro__:
        if "blueValue" in klass.__dict__:
            descriptor = klass.__dict__["blueValue"]
            break
    assert isinstance(descriptor, property)

def test_hall::geometry::rgbcolor_has_greenValue():
    assert hasattr(HALL::Geometry::RGBColor, "greenValue")
    descriptor = None
    for klass in HALL::Geometry::RGBColor.__mro__:
        if "greenValue" in klass.__dict__:
            descriptor = klass.__dict__["greenValue"]
            break
    assert isinstance(descriptor, property)

def test_hall::geometry::rgbcolor_has_redValue():
    assert hasattr(HALL::Geometry::RGBColor, "redValue")
    descriptor = None
    for klass in HALL::Geometry::RGBColor.__mro__:
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



def test_hall::geometry::selectedcolors_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::SelectedColors)


def test_hall::geometry::selectedcolors_constructor_exists():
    assert callable(HALL::Geometry::SelectedColors.__init__)


def test_hall::geometry::selectedcolors_constructor_args():
    sig = inspect.signature(HALL::Geometry::SelectedColors.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::disabledcolors_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::DisabledColors)


def test_hall::geometry::disabledcolors_constructor_exists():
    assert callable(HALL::Geometry::DisabledColors.__init__)


def test_hall::geometry::disabledcolors_constructor_args():
    sig = inspect.signature(HALL::Geometry::DisabledColors.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::normalcolors_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::NormalColors)


def test_hall::geometry::normalcolors_constructor_exists():
    assert callable(HALL::Geometry::NormalColors.__init__)


def test_hall::geometry::normalcolors_constructor_args():
    sig = inspect.signature(HALL::Geometry::NormalColors.__init__)
    params = list(sig.parameters.keys())



def test_rgbcolor_is_not_abstract():
    assert not inspect.isabstract(RGBColor)


def test_rgbcolor_constructor_exists():
    assert callable(RGBColor.__init__)


def test_rgbcolor_constructor_args():
    sig = inspect.signature(RGBColor.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::color_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::Color)


def test_hall::geometry::color_constructor_exists():
    assert callable(HALL::Geometry::Color.__init__)


def test_hall::geometry::color_constructor_args():
    sig = inspect.signature(HALL::Geometry::Color.__init__)
    params = list(sig.parameters.keys())



def test_type_is_not_abstract():
    assert not inspect.isabstract(Type)


def test_type_constructor_exists():
    assert callable(Type.__init__)


def test_type_constructor_args():
    sig = inspect.signature(Type.__init__)
    params = list(sig.parameters.keys())



def test_messagedefinition_is_not_abstract():
    assert not inspect.isabstract(MessageDefinition)


def test_messagedefinition_constructor_exists():
    assert callable(MessageDefinition.__init__)


def test_messagedefinition_constructor_args():
    sig = inspect.signature(MessageDefinition.__init__)
    params = list(sig.parameters.keys())



def test_hall::goal_is_not_abstract():
    assert not inspect.isabstract(HALL::Goal)


def test_hall::goal_constructor_exists():
    assert callable(HALL::Goal.__init__)


def test_hall::goal_constructor_args():
    sig = inspect.signature(HALL::Goal.__init__)
    params = list(sig.parameters.keys())
    assert "condition" in params, "Missing parameter 'condition'"

def test_hall::goal_has_condition():
    assert hasattr(HALL::Goal, "condition")
    descriptor = None
    for klass in HALL::Goal.__mro__:
        if "condition" in klass.__dict__:
            descriptor = klass.__dict__["condition"]
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



def test_hall::taskobject_is_not_abstract():
    assert not inspect.isabstract(HALL::TaskObject)


def test_hall::taskobject_constructor_exists():
    assert callable(HALL::TaskObject.__init__)


def test_hall::taskobject_constructor_args():
    sig = inspect.signature(HALL::TaskObject.__init__)
    params = list(sig.parameters.keys())
    assert "numberofgoalscompleted" in params, "Missing parameter 'numberofgoalscompleted'"
    assert "completionTime" in params, "Missing parameter 'completionTime'"

def test_hall::taskobject_has_numberofgoalscompleted():
    assert hasattr(HALL::TaskObject, "numberofgoalscompleted")
    descriptor = None
    for klass in HALL::TaskObject.__mro__:
        if "numberofgoalscompleted" in klass.__dict__:
            descriptor = klass.__dict__["numberofgoalscompleted"]
            break
    assert isinstance(descriptor, property)

def test_hall::taskobject_has_completionTime():
    assert hasattr(HALL::TaskObject, "completionTime")
    descriptor = None
    for klass in HALL::TaskObject.__mro__:
        if "completionTime" in klass.__dict__:
            descriptor = klass.__dict__["completionTime"]
            break
    assert isinstance(descriptor, property)



def test_hall::visualobject_is_not_abstract():
    assert not inspect.isabstract(HALL::VisualObject)


def test_hall::visualobject_constructor_exists():
    assert callable(HALL::VisualObject.__init__)


def test_hall::visualobject_constructor_args():
    sig = inspect.signature(HALL::VisualObject.__init__)
    params = list(sig.parameters.keys())
    assert "vtype" in params, "Missing parameter 'vtype'"

def test_hall::visualobject_has_vtype():
    assert hasattr(HALL::VisualObject, "vtype")
    descriptor = None
    for klass in HALL::VisualObject.__mro__:
        if "vtype" in klass.__dict__:
            descriptor = klass.__dict__["vtype"]
            break
    assert isinstance(descriptor, property)



def test_hall::model_is_not_abstract():
    assert not inspect.isabstract(HALL::Model)


def test_hall::model_constructor_exists():
    assert callable(HALL::Model.__init__)


def test_hall::model_constructor_args():
    sig = inspect.signature(HALL::Model.__init__)
    params = list(sig.parameters.keys())



def test_hall::systemcomponent_is_not_abstract():
    assert not inspect.isabstract(HALL::SystemComponent)


def test_hall::systemcomponent_constructor_exists():
    assert callable(HALL::SystemComponent.__init__)


def test_hall::systemcomponent_constructor_args():
    sig = inspect.signature(HALL::SystemComponent.__init__)
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



def test_hall::data_is_not_abstract():
    assert not inspect.isabstract(HALL::Data)


def test_hall::data_constructor_exists():
    assert callable(HALL::Data.__init__)


def test_hall::data_constructor_args():
    sig = inspect.signature(HALL::Data.__init__)
    params = list(sig.parameters.keys())
    assert "initValue" in params, "Missing parameter 'initValue'"
    assert "name" in params, "Missing parameter 'name'"
    assert "currentValue" in params, "Missing parameter 'currentValue'"

def test_hall::data_has_initValue():
    assert hasattr(HALL::Data, "initValue")
    descriptor = None
    for klass in HALL::Data.__mro__:
        if "initValue" in klass.__dict__:
            descriptor = klass.__dict__["initValue"]
            break
    assert isinstance(descriptor, property)

def test_hall::data_has_name():
    assert hasattr(HALL::Data, "name")
    descriptor = None
    for klass in HALL::Data.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_hall::data_has_currentValue():
    assert hasattr(HALL::Data, "currentValue")
    descriptor = None
    for klass in HALL::Data.__mro__:
        if "currentValue" in klass.__dict__:
            descriptor = klass.__dict__["currentValue"]
            break
    assert isinstance(descriptor, property)



def test_hall::component_is_not_abstract():
    assert not inspect.isabstract(HALL::Component)


def test_hall::component_constructor_exists():
    assert callable(HALL::Component.__init__)


def test_hall::component_constructor_args():
    sig = inspect.signature(HALL::Component.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::component_has_name():
    assert hasattr(HALL::Component, "name")
    descriptor = None
    for klass in HALL::Component.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::userprofile_is_not_abstract():
    assert not inspect.isabstract(HALL::UserProfile)


def test_hall::userprofile_constructor_exists():
    assert callable(HALL::UserProfile.__init__)


def test_hall::userprofile_constructor_args():
    sig = inspect.signature(HALL::UserProfile.__init__)
    params = list(sig.parameters.keys())
    assert "numberofcompletedtasks" in params, "Missing parameter 'numberofcompletedtasks'"

def test_hall::userprofile_has_numberofcompletedtasks():
    assert hasattr(HALL::UserProfile, "numberofcompletedtasks")
    descriptor = None
    for klass in HALL::UserProfile.__mro__:
        if "numberofcompletedtasks" in klass.__dict__:
            descriptor = klass.__dict__["numberofcompletedtasks"]
            break
    assert isinstance(descriptor, property)



def test_geometrydata_is_not_abstract():
    assert not inspect.isabstract(GeometryData)


def test_geometrydata_constructor_exists():
    assert callable(GeometryData.__init__)


def test_geometrydata_constructor_args():
    sig = inspect.signature(GeometryData.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::geometrydata3d_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::GeometryData3D)


def test_hall::geometry::geometrydata3d_constructor_exists():
    assert callable(HALL::Geometry::GeometryData3D.__init__)


def test_hall::geometry::geometrydata3d_constructor_args():
    sig = inspect.signature(HALL::Geometry::GeometryData3D.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::geometrydata2d_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::GeometryData2D)


def test_hall::geometry::geometrydata2d_constructor_exists():
    assert callable(HALL::Geometry::GeometryData2D.__init__)


def test_hall::geometry::geometrydata2d_constructor_args():
    sig = inspect.signature(HALL::Geometry::GeometryData2D.__init__)
    params = list(sig.parameters.keys())
    assert "labelText" in params, "Missing parameter 'labelText'"

def test_hall::geometry::geometrydata2d_has_labelText():
    assert hasattr(HALL::Geometry::GeometryData2D, "labelText")
    descriptor = None
    for klass in HALL::Geometry::GeometryData2D.__mro__:
        if "labelText" in klass.__dict__:
            descriptor = klass.__dict__["labelText"]
            break
    assert isinstance(descriptor, property)



def test_fsmactions::let_is_not_abstract():
    assert not inspect.isabstract(FSMActions::Let)


def test_fsmactions::let_constructor_exists():
    assert callable(FSMActions::Let.__init__)


def test_fsmactions::let_constructor_args():
    sig = inspect.signature(FSMActions::Let.__init__)
    params = list(sig.parameters.keys())



def test_simpletype_is_not_abstract():
    assert not inspect.isabstract(SimpleType)


def test_simpletype_constructor_exists():
    assert callable(SimpleType.__init__)


def test_simpletype_constructor_args():
    sig = inspect.signature(SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hall::types::boolean_is_not_abstract():
    assert not inspect.isabstract(HALL::Types::Boolean)


def test_hall::types::boolean_constructor_exists():
    assert callable(HALL::Types::Boolean.__init__)


def test_hall::types::boolean_constructor_args():
    sig = inspect.signature(HALL::Types::Boolean.__init__)
    params = list(sig.parameters.keys())



def test_hall::types::number_is_not_abstract():
    assert not inspect.isabstract(HALL::Types::Number)


def test_hall::types::number_constructor_exists():
    assert callable(HALL::Types::Number.__init__)


def test_hall::types::number_constructor_args():
    sig = inspect.signature(HALL::Types::Number.__init__)
    params = list(sig.parameters.keys())



def test_hall::types::string_is_not_abstract():
    assert not inspect.isabstract(HALL::Types::String)


def test_hall::types::string_constructor_exists():
    assert callable(HALL::Types::String.__init__)


def test_hall::types::string_constructor_args():
    sig = inspect.signature(HALL::Types::String.__init__)
    params = list(sig.parameters.keys())



def test_hall::types::set_is_not_abstract():
    assert not inspect.isabstract(HALL::Types::Set)


def test_hall::types::set_constructor_exists():
    assert callable(HALL::Types::Set.__init__)


def test_hall::types::set_constructor_args():
    sig = inspect.signature(HALL::Types::Set.__init__)
    params = list(sig.parameters.keys())



def test_set_is_not_abstract():
    assert not inspect.isabstract(Set)


def test_set_constructor_exists():
    assert callable(Set.__init__)


def test_set_constructor_args():
    sig = inspect.signature(Set.__init__)
    params = list(sig.parameters.keys())



def test_hall::types::simpletype_is_not_abstract():
    assert not inspect.isabstract(HALL::Types::SimpleType)


def test_hall::types::simpletype_constructor_exists():
    assert callable(HALL::Types::SimpleType.__init__)


def test_hall::types::simpletype_constructor_args():
    sig = inspect.signature(HALL::Types::SimpleType.__init__)
    params = list(sig.parameters.keys())



def test_hall::types::type_is_not_abstract():
    assert not inspect.isabstract(HALL::Types::Type)


def test_hall::types::type_constructor_exists():
    assert callable(HALL::Types::Type.__init__)


def test_hall::types::type_constructor_args():
    sig = inspect.signature(HALL::Types::Type.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::types::type_has_name():
    assert hasattr(HALL::Types::Type, "name")
    descriptor = None
    for klass in HALL::Types::Type.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_fsmactions::hall::data_is_not_abstract():
    assert not inspect.isabstract(FSMActions::HALL::Data)


def test_fsmactions::hall::data_constructor_exists():
    assert callable(FSMActions::HALL::Data.__init__)


def test_fsmactions::hall::data_constructor_args():
    sig = inspect.signature(FSMActions::HALL::Data.__init__)
    params = list(sig.parameters.keys())



def test_fsmconditions::hall::component_is_not_abstract():
    assert not inspect.isabstract(FSMConditions::HALL::Component)


def test_fsmconditions::hall::component_constructor_exists():
    assert callable(FSMConditions::HALL::Component.__init__)


def test_fsmconditions::hall::component_constructor_args():
    sig = inspect.signature(FSMConditions::HALL::Component.__init__)
    params = list(sig.parameters.keys())



def test_actionexpression_is_not_abstract():
    assert not inspect.isabstract(ActionExpression)


def test_actionexpression_constructor_exists():
    assert callable(ActionExpression.__init__)


def test_actionexpression_constructor_args():
    sig = inspect.signature(ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmactions::varref_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::VarRef)


def test_hall::fsmactions::varref_constructor_exists():
    assert callable(HALL::FSMActions::VarRef.__init__)


def test_hall::fsmactions::varref_constructor_args():
    sig = inspect.signature(HALL::FSMActions::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmactions::domainpropertyset_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::DomainPropertySet)


def test_hall::fsmactions::domainpropertyset_constructor_exists():
    assert callable(HALL::FSMActions::DomainPropertySet.__init__)


def test_hall::fsmactions::domainpropertyset_constructor_args():
    sig = inspect.signature(HALL::FSMActions::DomainPropertySet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsmactions::domainpropertyset_has_name():
    assert hasattr(HALL::FSMActions::DomainPropertySet, "name")
    descriptor = None
    for klass in HALL::FSMActions::DomainPropertySet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmactions::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::UnaryOperator)


def test_hall::fsmactions::unaryoperator_constructor_exists():
    assert callable(HALL::FSMActions::UnaryOperator.__init__)


def test_hall::fsmactions::unaryoperator_constructor_args():
    sig = inspect.signature(HALL::FSMActions::UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::fsmactions::unaryoperator_has_operatorname():
    assert hasattr(HALL::FSMActions::UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::FSMActions::UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmactions::let_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::Let)


def test_hall::fsmactions::let_constructor_exists():
    assert callable(HALL::FSMActions::Let.__init__)


def test_hall::fsmactions::let_constructor_args():
    sig = inspect.signature(HALL::FSMActions::Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsmactions::let_has_name():
    assert hasattr(HALL::FSMActions::Let, "name")
    descriptor = None
    for klass in HALL::FSMActions::Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmactions::getdata_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::GetData)


def test_hall::fsmactions::getdata_constructor_exists():
    assert callable(HALL::FSMActions::GetData.__init__)


def test_hall::fsmactions::getdata_constructor_args():
    sig = inspect.signature(HALL::FSMActions::GetData.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmactions::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::BinaryOperator)


def test_hall::fsmactions::binaryoperator_constructor_exists():
    assert callable(HALL::FSMActions::BinaryOperator.__init__)


def test_hall::fsmactions::binaryoperator_constructor_args():
    sig = inspect.signature(HALL::FSMActions::BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::fsmactions::binaryoperator_has_operatorname():
    assert hasattr(HALL::FSMActions::BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::FSMActions::BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmactions::messageinvocation_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::MessageInvocation)


def test_hall::fsmactions::messageinvocation_constructor_exists():
    assert callable(HALL::FSMActions::MessageInvocation.__init__)


def test_hall::fsmactions::messageinvocation_constructor_args():
    sig = inspect.signature(HALL::FSMActions::MessageInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopDown" in params, "Missing parameter 'isTopDown'"

def test_hall::fsmactions::messageinvocation_has_isTopDown():
    assert hasattr(HALL::FSMActions::MessageInvocation, "isTopDown")
    descriptor = None
    for klass in HALL::FSMActions::MessageInvocation.__mro__:
        if "isTopDown" in klass.__dict__:
            descriptor = klass.__dict__["isTopDown"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmactions::domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::DomainPropertyGet)


def test_hall::fsmactions::domainpropertyget_constructor_exists():
    assert callable(HALL::FSMActions::DomainPropertyGet.__init__)


def test_hall::fsmactions::domainpropertyget_constructor_args():
    sig = inspect.signature(HALL::FSMActions::DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsmactions::domainpropertyget_has_name():
    assert hasattr(HALL::FSMActions::DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL::FSMActions::DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmactions::literal_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::Literal)


def test_hall::fsmactions::literal_constructor_exists():
    assert callable(HALL::FSMActions::Literal.__init__)


def test_hall::fsmactions::literal_constructor_args():
    sig = inspect.signature(HALL::FSMActions::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall::fsmactions::literal_has_value():
    assert hasattr(HALL::FSMActions::Literal, "value")
    descriptor = None
    for klass in HALL::FSMActions::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmactions::actionexpression_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::ActionExpression)


def test_hall::fsmactions::actionexpression_constructor_exists():
    assert callable(HALL::FSMActions::ActionExpression.__init__)


def test_hall::fsmactions::actionexpression_constructor_args():
    sig = inspect.signature(HALL::FSMActions::ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsmactions::actionexpression_is_not_abstract():
    assert not inspect.isabstract(FSMActions::ActionExpression)


def test_fsmactions::actionexpression_constructor_exists():
    assert callable(FSMActions::ActionExpression.__init__)


def test_fsmactions::actionexpression_constructor_args():
    sig = inspect.signature(FSMActions::ActionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmactions::action_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::Action)


def test_hall::fsmactions::action_constructor_exists():
    assert callable(HALL::FSMActions::Action.__init__)


def test_hall::fsmactions::action_constructor_args():
    sig = inspect.signature(HALL::FSMActions::Action.__init__)
    params = list(sig.parameters.keys())



def test_fsmconditions::let_is_not_abstract():
    assert not inspect.isabstract(FSMConditions::Let)


def test_fsmconditions::let_constructor_exists():
    assert callable(FSMConditions::Let.__init__)


def test_fsmconditions::let_constructor_args():
    sig = inspect.signature(FSMConditions::Let.__init__)
    params = list(sig.parameters.keys())



def test_fsmconditions::hall::data_is_not_abstract():
    assert not inspect.isabstract(FSMConditions::HALL::Data)


def test_fsmconditions::hall::data_constructor_exists():
    assert callable(FSMConditions::HALL::Data.__init__)


def test_fsmconditions::hall::data_constructor_args():
    sig = inspect.signature(FSMConditions::HALL::Data.__init__)
    params = list(sig.parameters.keys())



def test_preconditionexpression_is_not_abstract():
    assert not inspect.isabstract(PreConditionExpression)


def test_preconditionexpression_constructor_exists():
    assert callable(PreConditionExpression.__init__)


def test_preconditionexpression_constructor_args():
    sig = inspect.signature(PreConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmconditions::domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::DomainPropertyGet)


def test_hall::fsmconditions::domainpropertyget_constructor_exists():
    assert callable(HALL::FSMConditions::DomainPropertyGet.__init__)


def test_hall::fsmconditions::domainpropertyget_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsmconditions::domainpropertyget_has_name():
    assert hasattr(HALL::FSMConditions::DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL::FSMConditions::DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmconditions::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::UnaryOperator)


def test_hall::fsmconditions::unaryoperator_constructor_exists():
    assert callable(HALL::FSMConditions::UnaryOperator.__init__)


def test_hall::fsmconditions::unaryoperator_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::fsmconditions::unaryoperator_has_operatorname():
    assert hasattr(HALL::FSMConditions::UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::FSMConditions::UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmconditions::varref_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::VarRef)


def test_hall::fsmconditions::varref_constructor_exists():
    assert callable(HALL::FSMConditions::VarRef.__init__)


def test_hall::fsmconditions::varref_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmconditions::getstate_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::GetState)


def test_hall::fsmconditions::getstate_constructor_exists():
    assert callable(HALL::FSMConditions::GetState.__init__)


def test_hall::fsmconditions::getstate_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::GetState.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmconditions::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::BinaryOperator)


def test_hall::fsmconditions::binaryoperator_constructor_exists():
    assert callable(HALL::FSMConditions::BinaryOperator.__init__)


def test_hall::fsmconditions::binaryoperator_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::fsmconditions::binaryoperator_has_operatorname():
    assert hasattr(HALL::FSMConditions::BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::FSMConditions::BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmconditions::getdata_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::GetData)


def test_hall::fsmconditions::getdata_constructor_exists():
    assert callable(HALL::FSMConditions::GetData.__init__)


def test_hall::fsmconditions::getdata_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::GetData.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmconditions::let_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::Let)


def test_hall::fsmconditions::let_constructor_exists():
    assert callable(HALL::FSMConditions::Let.__init__)


def test_hall::fsmconditions::let_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsmconditions::let_has_name():
    assert hasattr(HALL::FSMConditions::Let, "name")
    descriptor = None
    for klass in HALL::FSMConditions::Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmconditions::literal_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::Literal)


def test_hall::fsmconditions::literal_constructor_exists():
    assert callable(HALL::FSMConditions::Literal.__init__)


def test_hall::fsmconditions::literal_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall::fsmconditions::literal_has_value():
    assert hasattr(HALL::FSMConditions::Literal, "value")
    descriptor = None
    for klass in HALL::FSMConditions::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmconditions::preconditionexpression_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::PreConditionExpression)


def test_hall::fsmconditions::preconditionexpression_constructor_exists():
    assert callable(HALL::FSMConditions::PreConditionExpression.__init__)


def test_hall::fsmconditions::preconditionexpression_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::PreConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsmconditions::preconditionexpression_is_not_abstract():
    assert not inspect.isabstract(FSMConditions::PreConditionExpression)


def test_fsmconditions::preconditionexpression_constructor_exists():
    assert callable(FSMConditions::PreConditionExpression.__init__)


def test_fsmconditions::preconditionexpression_constructor_args():
    sig = inspect.signature(FSMConditions::PreConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsmconditions::precondition_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMConditions::PreCondition)


def test_hall::fsmconditions::precondition_constructor_exists():
    assert callable(HALL::FSMConditions::PreCondition.__init__)


def test_hall::fsmconditions::precondition_constructor_args():
    sig = inspect.signature(HALL::FSMConditions::PreCondition.__init__)
    params = list(sig.parameters.keys())



def test_fsminstructions::let_is_not_abstract():
    assert not inspect.isabstract(FSMInstructions::Let)


def test_fsminstructions::let_constructor_exists():
    assert callable(FSMInstructions::Let.__init__)


def test_fsminstructions::let_constructor_args():
    sig = inspect.signature(FSMInstructions::Let.__init__)
    params = list(sig.parameters.keys())



def test_fsminstructions::hall::data_is_not_abstract():
    assert not inspect.isabstract(FSMInstructions::HALL::Data)


def test_fsminstructions::hall::data_constructor_exists():
    assert callable(FSMInstructions::HALL::Data.__init__)


def test_fsminstructions::hall::data_constructor_args():
    sig = inspect.signature(FSMInstructions::HALL::Data.__init__)
    params = list(sig.parameters.keys())



def test_triggerexpression_is_not_abstract():
    assert not inspect.isabstract(TriggerExpression)


def test_triggerexpression_constructor_exists():
    assert callable(TriggerExpression.__init__)


def test_triggerexpression_constructor_args():
    sig = inspect.signature(TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::trigger::messagenotification_is_not_abstract():
    assert not inspect.isabstract(HALL::Trigger::MessageNotification)


def test_hall::trigger::messagenotification_constructor_exists():
    assert callable(HALL::Trigger::MessageNotification.__init__)


def test_hall::trigger::messagenotification_constructor_args():
    sig = inspect.signature(HALL::Trigger::MessageNotification.__init__)
    params = list(sig.parameters.keys())



def test_hall::trigger::triggerexpression_is_not_abstract():
    assert not inspect.isabstract(HALL::Trigger::TriggerExpression)


def test_hall::trigger::triggerexpression_constructor_exists():
    assert callable(HALL::Trigger::TriggerExpression.__init__)


def test_hall::trigger::triggerexpression_constructor_args():
    sig = inspect.signature(HALL::Trigger::TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_trigger::triggerexpression_is_not_abstract():
    assert not inspect.isabstract(Trigger::TriggerExpression)


def test_trigger::triggerexpression_constructor_exists():
    assert callable(Trigger::TriggerExpression.__init__)


def test_trigger::triggerexpression_constructor_args():
    sig = inspect.signature(Trigger::TriggerExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::trigger::trigger_is_not_abstract():
    assert not inspect.isabstract(HALL::Trigger::Trigger)


def test_hall::trigger::trigger_constructor_exists():
    assert callable(HALL::Trigger::Trigger.__init__)


def test_hall::trigger::trigger_constructor_args():
    sig = inspect.signature(HALL::Trigger::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_fsminstructions::hall::component_is_not_abstract():
    assert not inspect.isabstract(FSMInstructions::HALL::Component)


def test_fsminstructions::hall::component_constructor_exists():
    assert callable(FSMInstructions::HALL::Component.__init__)


def test_fsminstructions::hall::component_constructor_args():
    sig = inspect.signature(FSMInstructions::HALL::Component.__init__)
    params = list(sig.parameters.keys())



def test_posconditionexpression_is_not_abstract():
    assert not inspect.isabstract(PosConditionExpression)


def test_posconditionexpression_constructor_exists():
    assert callable(PosConditionExpression.__init__)


def test_posconditionexpression_constructor_args():
    sig = inspect.signature(PosConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsminstructions::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::UnaryOperator)


def test_hall::fsminstructions::unaryoperator_constructor_exists():
    assert callable(HALL::FSMInstructions::UnaryOperator.__init__)


def test_hall::fsminstructions::unaryoperator_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::fsminstructions::unaryoperator_has_operatorname():
    assert hasattr(HALL::FSMInstructions::UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::FSMInstructions::UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsminstructions::let_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::Let)


def test_hall::fsminstructions::let_constructor_exists():
    assert callable(HALL::FSMInstructions::Let.__init__)


def test_hall::fsminstructions::let_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsminstructions::let_has_name():
    assert hasattr(HALL::FSMInstructions::Let, "name")
    descriptor = None
    for klass in HALL::FSMInstructions::Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsminstructions::getstate_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::GetState)


def test_hall::fsminstructions::getstate_constructor_exists():
    assert callable(HALL::FSMInstructions::GetState.__init__)


def test_hall::fsminstructions::getstate_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::GetState.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsminstructions::setstate_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::SetState)


def test_hall::fsminstructions::setstate_constructor_exists():
    assert callable(HALL::FSMInstructions::SetState.__init__)


def test_hall::fsminstructions::setstate_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::SetState.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsminstructions::varref_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::VarRef)


def test_hall::fsminstructions::varref_constructor_exists():
    assert callable(HALL::FSMInstructions::VarRef.__init__)


def test_hall::fsminstructions::varref_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsminstructions::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::BinaryOperator)


def test_hall::fsminstructions::binaryoperator_constructor_exists():
    assert callable(HALL::FSMInstructions::BinaryOperator.__init__)


def test_hall::fsminstructions::binaryoperator_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::fsminstructions::binaryoperator_has_operatorname():
    assert hasattr(HALL::FSMInstructions::BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::FSMInstructions::BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsminstructions::getdata_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::GetData)


def test_hall::fsminstructions::getdata_constructor_exists():
    assert callable(HALL::FSMInstructions::GetData.__init__)


def test_hall::fsminstructions::getdata_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::GetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::fsminstructions::getdata_has_field():
    assert hasattr(HALL::FSMInstructions::GetData, "field")
    descriptor = None
    for klass in HALL::FSMInstructions::GetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsminstructions::setdata_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::SetData)


def test_hall::fsminstructions::setdata_constructor_exists():
    assert callable(HALL::FSMInstructions::SetData.__init__)


def test_hall::fsminstructions::setdata_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::SetData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::fsminstructions::setdata_has_field():
    assert hasattr(HALL::FSMInstructions::SetData, "field")
    descriptor = None
    for klass in HALL::FSMInstructions::SetData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsminstructions::domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::DomainPropertyGet)


def test_hall::fsminstructions::domainpropertyget_constructor_exists():
    assert callable(HALL::FSMInstructions::DomainPropertyGet.__init__)


def test_hall::fsminstructions::domainpropertyget_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsminstructions::domainpropertyget_has_name():
    assert hasattr(HALL::FSMInstructions::DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL::FSMInstructions::DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsminstructions::literal_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::Literal)


def test_hall::fsminstructions::literal_constructor_exists():
    assert callable(HALL::FSMInstructions::Literal.__init__)


def test_hall::fsminstructions::literal_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall::fsminstructions::literal_has_value():
    assert hasattr(HALL::FSMInstructions::Literal, "value")
    descriptor = None
    for klass in HALL::FSMInstructions::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsminstructions::posconditionexpression_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::PosConditionExpression)


def test_hall::fsminstructions::posconditionexpression_constructor_exists():
    assert callable(HALL::FSMInstructions::PosConditionExpression.__init__)


def test_hall::fsminstructions::posconditionexpression_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::PosConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_fsminstructions::posconditionexpression_is_not_abstract():
    assert not inspect.isabstract(FSMInstructions::PosConditionExpression)


def test_fsminstructions::posconditionexpression_constructor_exists():
    assert callable(FSMInstructions::PosConditionExpression.__init__)


def test_fsminstructions::posconditionexpression_constructor_args():
    sig = inspect.signature(FSMInstructions::PosConditionExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsminstructions::poscondition_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMInstructions::PosCondition)


def test_hall::fsminstructions::poscondition_constructor_exists():
    assert callable(HALL::FSMInstructions::PosCondition.__init__)


def test_hall::fsminstructions::poscondition_constructor_args():
    sig = inspect.signature(HALL::FSMInstructions::PosCondition.__init__)
    params = list(sig.parameters.keys())



def test_hall::trigger::domaineventfired_is_not_abstract():
    assert not inspect.isabstract(HALL::Trigger::DomainEventFired)


def test_hall::trigger::domaineventfired_constructor_exists():
    assert callable(HALL::Trigger::DomainEventFired.__init__)


def test_hall::trigger::domaineventfired_constructor_args():
    sig = inspect.signature(HALL::Trigger::DomainEventFired.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::trigger::domaineventfired_has_name():
    assert hasattr(HALL::Trigger::DomainEventFired, "name")
    descriptor = None
    for klass in HALL::Trigger::DomainEventFired.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_regularstate_is_not_abstract():
    assert not inspect.isabstract(RegularState)


def test_regularstate_constructor_exists():
    assert callable(RegularState.__init__)


def test_regularstate_constructor_args():
    sig = inspect.signature(RegularState.__init__)
    params = list(sig.parameters.keys())



def test_initialstate_is_not_abstract():
    assert not inspect.isabstract(InitialState)


def test_initialstate_constructor_exists():
    assert callable(InitialState.__init__)


def test_initialstate_constructor_args():
    sig = inspect.signature(InitialState.__init__)
    params = list(sig.parameters.keys())



def test_fsm::hall::component_is_not_abstract():
    assert not inspect.isabstract(FSM::HALL::Component)


def test_fsm::hall::component_constructor_exists():
    assert callable(FSM::HALL::Component.__init__)


def test_fsm::hall::component_constructor_args():
    sig = inspect.signature(FSM::HALL::Component.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsm::fsm_is_not_abstract():
    assert not inspect.isabstract(HALL::FSM::FSM)


def test_hall::fsm::fsm_constructor_exists():
    assert callable(HALL::FSM::FSM.__init__)


def test_hall::fsm::fsm_constructor_args():
    sig = inspect.signature(HALL::FSM::FSM.__init__)
    params = list(sig.parameters.keys())



def test_transition_is_not_abstract():
    assert not inspect.isabstract(Transition)


def test_transition_constructor_exists():
    assert callable(Transition.__init__)


def test_transition_constructor_args():
    sig = inspect.signature(Transition.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsm::state_is_not_abstract():
    assert not inspect.isabstract(HALL::FSM::State)


def test_hall::fsm::state_constructor_exists():
    assert callable(HALL::FSM::State.__init__)


def test_hall::fsm::state_constructor_args():
    sig = inspect.signature(HALL::FSM::State.__init__)
    params = list(sig.parameters.keys())
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsm::state_has_isActive():
    assert hasattr(HALL::FSM::State, "isActive")
    descriptor = None
    for klass in HALL::FSM::State.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_hall::fsm::state_has_name():
    assert hasattr(HALL::FSM::State, "name")
    descriptor = None
    for klass in HALL::FSM::State.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_trigger::trigger_is_not_abstract():
    assert not inspect.isabstract(Trigger::Trigger)


def test_trigger::trigger_constructor_exists():
    assert callable(Trigger::Trigger.__init__)


def test_trigger::trigger_constructor_args():
    sig = inspect.signature(Trigger::Trigger.__init__)
    params = list(sig.parameters.keys())



def test_fsmactions::action_is_not_abstract():
    assert not inspect.isabstract(FSMActions::Action)


def test_fsmactions::action_constructor_exists():
    assert callable(FSMActions::Action.__init__)


def test_fsmactions::action_constructor_args():
    sig = inspect.signature(FSMActions::Action.__init__)
    params = list(sig.parameters.keys())



def test_fsminstructions::poscondition_is_not_abstract():
    assert not inspect.isabstract(FSMInstructions::PosCondition)


def test_fsminstructions::poscondition_constructor_exists():
    assert callable(FSMInstructions::PosCondition.__init__)


def test_fsminstructions::poscondition_constructor_args():
    sig = inspect.signature(FSMInstructions::PosCondition.__init__)
    params = list(sig.parameters.keys())



def test_fsmconditions::precondition_is_not_abstract():
    assert not inspect.isabstract(FSMConditions::PreCondition)


def test_fsmconditions::precondition_constructor_exists():
    assert callable(FSMConditions::PreCondition.__init__)


def test_fsmconditions::precondition_constructor_args():
    sig = inspect.signature(FSMConditions::PreCondition.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsm::transition_is_not_abstract():
    assert not inspect.isabstract(HALL::FSM::Transition)


def test_hall::fsm::transition_constructor_exists():
    assert callable(HALL::FSM::Transition.__init__)


def test_hall::fsm::transition_constructor_args():
    sig = inspect.signature(HALL::FSM::Transition.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::fsm::transition_has_name():
    assert hasattr(HALL::FSM::Transition, "name")
    descriptor = None
    for klass in HALL::FSM::Transition.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_actions::hall::component_is_not_abstract():
    assert not inspect.isabstract(Actions::HALL::Component)


def test_actions::hall::component_constructor_exists():
    assert callable(Actions::HALL::Component.__init__)


def test_actions::hall::component_constructor_args():
    sig = inspect.signature(Actions::HALL::Component.__init__)
    params = list(sig.parameters.keys())



def test_actions::let_is_not_abstract():
    assert not inspect.isabstract(Actions::Let)


def test_actions::let_constructor_exists():
    assert callable(Actions::Let.__init__)


def test_actions::let_constructor_args():
    sig = inspect.signature(Actions::Let.__init__)
    params = list(sig.parameters.keys())



def test_actionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(ActionMessageExpression)


def test_actionmessageexpression_constructor_exists():
    assert callable(ActionMessageExpression.__init__)


def test_actionmessageexpression_constructor_args():
    sig = inspect.signature(ActionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::actions::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::UnaryOperator)


def test_hall::actions::unaryoperator_constructor_exists():
    assert callable(HALL::Actions::UnaryOperator.__init__)


def test_hall::actions::unaryoperator_constructor_args():
    sig = inspect.signature(HALL::Actions::UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::actions::unaryoperator_has_operatorname():
    assert hasattr(HALL::Actions::UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::Actions::UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::actions::getmessageparameter_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::GetMessageParameter)


def test_hall::actions::getmessageparameter_constructor_exists():
    assert callable(HALL::Actions::GetMessageParameter.__init__)


def test_hall::actions::getmessageparameter_constructor_args():
    sig = inspect.signature(HALL::Actions::GetMessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::actions::getmessageparameter_has_field():
    assert hasattr(HALL::Actions::GetMessageParameter, "field")
    descriptor = None
    for klass in HALL::Actions::GetMessageParameter.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::fsmactions::enable_is_not_abstract():
    assert not inspect.isabstract(HALL::FSMActions::Enable)


def test_hall::fsmactions::enable_constructor_exists():
    assert callable(HALL::FSMActions::Enable.__init__)


def test_hall::fsmactions::enable_constructor_args():
    sig = inspect.signature(HALL::FSMActions::Enable.__init__)
    params = list(sig.parameters.keys())



def test_hall::actions::domainpropertyset_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::DomainPropertySet)


def test_hall::actions::domainpropertyset_constructor_exists():
    assert callable(HALL::Actions::DomainPropertySet.__init__)


def test_hall::actions::domainpropertyset_constructor_args():
    sig = inspect.signature(HALL::Actions::DomainPropertySet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::actions::domainpropertyset_has_name():
    assert hasattr(HALL::Actions::DomainPropertySet, "name")
    descriptor = None
    for klass in HALL::Actions::DomainPropertySet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::actions::enable_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::Enable)


def test_hall::actions::enable_constructor_exists():
    assert callable(HALL::Actions::Enable.__init__)


def test_hall::actions::enable_constructor_args():
    sig = inspect.signature(HALL::Actions::Enable.__init__)
    params = list(sig.parameters.keys())



def test_hall::actions::messageinvocation_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::MessageInvocation)


def test_hall::actions::messageinvocation_constructor_exists():
    assert callable(HALL::Actions::MessageInvocation.__init__)


def test_hall::actions::messageinvocation_constructor_args():
    sig = inspect.signature(HALL::Actions::MessageInvocation.__init__)
    params = list(sig.parameters.keys())
    assert "isTopDown" in params, "Missing parameter 'isTopDown'"

def test_hall::actions::messageinvocation_has_isTopDown():
    assert hasattr(HALL::Actions::MessageInvocation, "isTopDown")
    descriptor = None
    for klass in HALL::Actions::MessageInvocation.__mro__:
        if "isTopDown" in klass.__dict__:
            descriptor = klass.__dict__["isTopDown"]
            break
    assert isinstance(descriptor, property)



def test_hall::actions::getmessagedata_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::GetMessageData)


def test_hall::actions::getmessagedata_constructor_exists():
    assert callable(HALL::Actions::GetMessageData.__init__)


def test_hall::actions::getmessagedata_constructor_args():
    sig = inspect.signature(HALL::Actions::GetMessageData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::actions::getmessagedata_has_field():
    assert hasattr(HALL::Actions::GetMessageData, "field")
    descriptor = None
    for klass in HALL::Actions::GetMessageData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::actions::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::BinaryOperator)


def test_hall::actions::binaryoperator_constructor_exists():
    assert callable(HALL::Actions::BinaryOperator.__init__)


def test_hall::actions::binaryoperator_constructor_args():
    sig = inspect.signature(HALL::Actions::BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::actions::binaryoperator_has_operatorname():
    assert hasattr(HALL::Actions::BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::Actions::BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::actions::literal_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::Literal)


def test_hall::actions::literal_constructor_exists():
    assert callable(HALL::Actions::Literal.__init__)


def test_hall::actions::literal_constructor_args():
    sig = inspect.signature(HALL::Actions::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall::actions::literal_has_value():
    assert hasattr(HALL::Actions::Literal, "value")
    descriptor = None
    for klass in HALL::Actions::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall::actions::let_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::Let)


def test_hall::actions::let_constructor_exists():
    assert callable(HALL::Actions::Let.__init__)


def test_hall::actions::let_constructor_args():
    sig = inspect.signature(HALL::Actions::Let.__init__)
    params = list(sig.parameters.keys())



def test_hall::actions::domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::DomainPropertyGet)


def test_hall::actions::domainpropertyget_constructor_exists():
    assert callable(HALL::Actions::DomainPropertyGet.__init__)


def test_hall::actions::domainpropertyget_constructor_args():
    sig = inspect.signature(HALL::Actions::DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::actions::domainpropertyget_has_name():
    assert hasattr(HALL::Actions::DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL::Actions::DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::actions::getdata_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::GetData)


def test_hall::actions::getdata_constructor_exists():
    assert callable(HALL::Actions::GetData.__init__)


def test_hall::actions::getdata_constructor_args():
    sig = inspect.signature(HALL::Actions::GetData.__init__)
    params = list(sig.parameters.keys())



def test_hall::actions::varref_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::VarRef)


def test_hall::actions::varref_constructor_exists():
    assert callable(HALL::Actions::VarRef.__init__)


def test_hall::actions::varref_constructor_args():
    sig = inspect.signature(HALL::Actions::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_hall::actions::actionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::ActionMessageExpression)


def test_hall::actions::actionmessageexpression_constructor_exists():
    assert callable(HALL::Actions::ActionMessageExpression.__init__)


def test_hall::actions::actionmessageexpression_constructor_args():
    sig = inspect.signature(HALL::Actions::ActionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_actions::actionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(Actions::ActionMessageExpression)


def test_actions::actionmessageexpression_constructor_exists():
    assert callable(Actions::ActionMessageExpression.__init__)


def test_actions::actionmessageexpression_constructor_args():
    sig = inspect.signature(Actions::ActionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::actions::actionmessage_is_not_abstract():
    assert not inspect.isabstract(HALL::Actions::ActionMessage)


def test_hall::actions::actionmessage_constructor_exists():
    assert callable(HALL::Actions::ActionMessage.__init__)


def test_hall::actions::actionmessage_constructor_args():
    sig = inspect.signature(HALL::Actions::ActionMessage.__init__)
    params = list(sig.parameters.keys())



def test_conditions::let_is_not_abstract():
    assert not inspect.isabstract(Conditions::Let)


def test_conditions::let_constructor_exists():
    assert callable(Conditions::Let.__init__)


def test_conditions::let_constructor_args():
    sig = inspect.signature(Conditions::Let.__init__)
    params = list(sig.parameters.keys())



def test_conditions::hall::data_is_not_abstract():
    assert not inspect.isabstract(Conditions::HALL::Data)


def test_conditions::hall::data_constructor_exists():
    assert callable(Conditions::HALL::Data.__init__)


def test_conditions::hall::data_constructor_args():
    sig = inspect.signature(Conditions::HALL::Data.__init__)
    params = list(sig.parameters.keys())



def test_conditions::hall::component_is_not_abstract():
    assert not inspect.isabstract(Conditions::HALL::Component)


def test_conditions::hall::component_constructor_exists():
    assert callable(Conditions::HALL::Component.__init__)


def test_conditions::hall::component_constructor_args():
    sig = inspect.signature(Conditions::HALL::Component.__init__)
    params = list(sig.parameters.keys())



def test_preconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(PreConditionMessageExpression)


def test_preconditionmessageexpression_constructor_exists():
    assert callable(PreConditionMessageExpression.__init__)


def test_preconditionmessageexpression_constructor_args():
    sig = inspect.signature(PreConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::conditions::getmessagedata_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::GetMessageData)


def test_hall::conditions::getmessagedata_constructor_exists():
    assert callable(HALL::Conditions::GetMessageData.__init__)


def test_hall::conditions::getmessagedata_constructor_args():
    sig = inspect.signature(HALL::Conditions::GetMessageData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::conditions::getmessagedata_has_field():
    assert hasattr(HALL::Conditions::GetMessageData, "field")
    descriptor = None
    for klass in HALL::Conditions::GetMessageData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::conditions::getstate_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::GetState)


def test_hall::conditions::getstate_constructor_exists():
    assert callable(HALL::Conditions::GetState.__init__)


def test_hall::conditions::getstate_constructor_args():
    sig = inspect.signature(HALL::Conditions::GetState.__init__)
    params = list(sig.parameters.keys())



def test_hall::conditions::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::UnaryOperator)


def test_hall::conditions::unaryoperator_constructor_exists():
    assert callable(HALL::Conditions::UnaryOperator.__init__)


def test_hall::conditions::unaryoperator_constructor_args():
    sig = inspect.signature(HALL::Conditions::UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::conditions::unaryoperator_has_operatorname():
    assert hasattr(HALL::Conditions::UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::Conditions::UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::conditions::getdata_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::GetData)


def test_hall::conditions::getdata_constructor_exists():
    assert callable(HALL::Conditions::GetData.__init__)


def test_hall::conditions::getdata_constructor_args():
    sig = inspect.signature(HALL::Conditions::GetData.__init__)
    params = list(sig.parameters.keys())



def test_hall::conditions::varref_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::VarRef)


def test_hall::conditions::varref_constructor_exists():
    assert callable(HALL::Conditions::VarRef.__init__)


def test_hall::conditions::varref_constructor_args():
    sig = inspect.signature(HALL::Conditions::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_hall::conditions::let_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::Let)


def test_hall::conditions::let_constructor_exists():
    assert callable(HALL::Conditions::Let.__init__)


def test_hall::conditions::let_constructor_args():
    sig = inspect.signature(HALL::Conditions::Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::conditions::let_has_name():
    assert hasattr(HALL::Conditions::Let, "name")
    descriptor = None
    for klass in HALL::Conditions::Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::conditions::getmessageparameter_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::GetMessageParameter)


def test_hall::conditions::getmessageparameter_constructor_exists():
    assert callable(HALL::Conditions::GetMessageParameter.__init__)


def test_hall::conditions::getmessageparameter_constructor_args():
    sig = inspect.signature(HALL::Conditions::GetMessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::conditions::getmessageparameter_has_field():
    assert hasattr(HALL::Conditions::GetMessageParameter, "field")
    descriptor = None
    for klass in HALL::Conditions::GetMessageParameter.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::conditions::domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::DomainPropertyGet)


def test_hall::conditions::domainpropertyget_constructor_exists():
    assert callable(HALL::Conditions::DomainPropertyGet.__init__)


def test_hall::conditions::domainpropertyget_constructor_args():
    sig = inspect.signature(HALL::Conditions::DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::conditions::domainpropertyget_has_name():
    assert hasattr(HALL::Conditions::DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL::Conditions::DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::conditions::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::BinaryOperator)


def test_hall::conditions::binaryoperator_constructor_exists():
    assert callable(HALL::Conditions::BinaryOperator.__init__)


def test_hall::conditions::binaryoperator_constructor_args():
    sig = inspect.signature(HALL::Conditions::BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::conditions::binaryoperator_has_operatorname():
    assert hasattr(HALL::Conditions::BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::Conditions::BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::conditions::literal_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::Literal)


def test_hall::conditions::literal_constructor_exists():
    assert callable(HALL::Conditions::Literal.__init__)


def test_hall::conditions::literal_constructor_args():
    sig = inspect.signature(HALL::Conditions::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall::conditions::literal_has_value():
    assert hasattr(HALL::Conditions::Literal, "value")
    descriptor = None
    for klass in HALL::Conditions::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall::conditions::preconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::PreConditionMessageExpression)


def test_hall::conditions::preconditionmessageexpression_constructor_exists():
    assert callable(HALL::Conditions::PreConditionMessageExpression.__init__)


def test_hall::conditions::preconditionmessageexpression_constructor_args():
    sig = inspect.signature(HALL::Conditions::PreConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_conditions::preconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(Conditions::PreConditionMessageExpression)


def test_conditions::preconditionmessageexpression_constructor_exists():
    assert callable(Conditions::PreConditionMessageExpression.__init__)


def test_conditions::preconditionmessageexpression_constructor_args():
    sig = inspect.signature(Conditions::PreConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::conditions::preconditionmessage_is_not_abstract():
    assert not inspect.isabstract(HALL::Conditions::PreConditionMessage)


def test_hall::conditions::preconditionmessage_constructor_exists():
    assert callable(HALL::Conditions::PreConditionMessage.__init__)


def test_hall::conditions::preconditionmessage_constructor_args():
    sig = inspect.signature(HALL::Conditions::PreConditionMessage.__init__)
    params = list(sig.parameters.keys())



def test_instructions::let_is_not_abstract():
    assert not inspect.isabstract(Instructions::Let)


def test_instructions::let_constructor_exists():
    assert callable(Instructions::Let.__init__)


def test_instructions::let_constructor_args():
    sig = inspect.signature(Instructions::Let.__init__)
    params = list(sig.parameters.keys())



def test_instructions::hall::component_is_not_abstract():
    assert not inspect.isabstract(Instructions::HALL::Component)


def test_instructions::hall::component_constructor_exists():
    assert callable(Instructions::HALL::Component.__init__)


def test_instructions::hall::component_constructor_args():
    sig = inspect.signature(Instructions::HALL::Component.__init__)
    params = list(sig.parameters.keys())



def test_instructions::hall::data_is_not_abstract():
    assert not inspect.isabstract(Instructions::HALL::Data)


def test_instructions::hall::data_constructor_exists():
    assert callable(Instructions::HALL::Data.__init__)


def test_instructions::hall::data_constructor_args():
    sig = inspect.signature(Instructions::HALL::Data.__init__)
    params = list(sig.parameters.keys())



def test_state_is_not_abstract():
    assert not inspect.isabstract(State)


def test_state_constructor_exists():
    assert callable(State.__init__)


def test_state_constructor_args():
    sig = inspect.signature(State.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsm::regularstate_is_not_abstract():
    assert not inspect.isabstract(HALL::FSM::RegularState)


def test_hall::fsm::regularstate_constructor_exists():
    assert callable(HALL::FSM::RegularState.__init__)


def test_hall::fsm::regularstate_constructor_args():
    sig = inspect.signature(HALL::FSM::RegularState.__init__)
    params = list(sig.parameters.keys())



def test_hall::fsm::initialstate_is_not_abstract():
    assert not inspect.isabstract(HALL::FSM::InitialState)


def test_hall::fsm::initialstate_constructor_exists():
    assert callable(HALL::FSM::InitialState.__init__)


def test_hall::fsm::initialstate_constructor_args():
    sig = inspect.signature(HALL::FSM::InitialState.__init__)
    params = list(sig.parameters.keys())



def test_regularmessagestate_is_not_abstract():
    assert not inspect.isabstract(RegularMessageState)


def test_regularmessagestate_constructor_exists():
    assert callable(RegularMessageState.__init__)


def test_regularmessagestate_constructor_args():
    sig = inspect.signature(RegularMessageState.__init__)
    params = list(sig.parameters.keys())



def test_hall::messages::messagehandler_is_not_abstract():
    assert not inspect.isabstract(HALL::Messages::MessageHandler)


def test_hall::messages::messagehandler_constructor_exists():
    assert callable(HALL::Messages::MessageHandler.__init__)


def test_hall::messages::messagehandler_constructor_args():
    sig = inspect.signature(HALL::Messages::MessageHandler.__init__)
    params = list(sig.parameters.keys())



def test_messages::hall::data_is_not_abstract():
    assert not inspect.isabstract(Messages::HALL::Data)


def test_messages::hall::data_constructor_exists():
    assert callable(Messages::HALL::Data.__init__)


def test_messages::hall::data_constructor_args():
    sig = inspect.signature(Messages::HALL::Data.__init__)
    params = list(sig.parameters.keys())



def test_posconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(PosConditionMessageExpression)


def test_posconditionmessageexpression_constructor_exists():
    assert callable(PosConditionMessageExpression.__init__)


def test_posconditionmessageexpression_constructor_args():
    sig = inspect.signature(PosConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::instructions::settopdown_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::SetTopDown)


def test_hall::instructions::settopdown_constructor_exists():
    assert callable(HALL::Instructions::SetTopDown.__init__)


def test_hall::instructions::settopdown_constructor_args():
    sig = inspect.signature(HALL::Instructions::SetTopDown.__init__)
    params = list(sig.parameters.keys())



def test_hall::instructions::unaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::UnaryOperator)


def test_hall::instructions::unaryoperator_constructor_exists():
    assert callable(HALL::Instructions::UnaryOperator.__init__)


def test_hall::instructions::unaryoperator_constructor_args():
    sig = inspect.signature(HALL::Instructions::UnaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::instructions::unaryoperator_has_operatorname():
    assert hasattr(HALL::Instructions::UnaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::Instructions::UnaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::getdata_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::GetData)


def test_hall::instructions::getdata_constructor_exists():
    assert callable(HALL::Instructions::GetData.__init__)


def test_hall::instructions::getdata_constructor_args():
    sig = inspect.signature(HALL::Instructions::GetData.__init__)
    params = list(sig.parameters.keys())



def test_hall::instructions::getmessagedata_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::GetMessageData)


def test_hall::instructions::getmessagedata_constructor_exists():
    assert callable(HALL::Instructions::GetMessageData.__init__)


def test_hall::instructions::getmessagedata_constructor_args():
    sig = inspect.signature(HALL::Instructions::GetMessageData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::instructions::getmessagedata_has_field():
    assert hasattr(HALL::Instructions::GetMessageData, "field")
    descriptor = None
    for klass in HALL::Instructions::GetMessageData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::varref_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::VarRef)


def test_hall::instructions::varref_constructor_exists():
    assert callable(HALL::Instructions::VarRef.__init__)


def test_hall::instructions::varref_constructor_args():
    sig = inspect.signature(HALL::Instructions::VarRef.__init__)
    params = list(sig.parameters.keys())



def test_hall::instructions::domainpropertyget_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::DomainPropertyGet)


def test_hall::instructions::domainpropertyget_constructor_exists():
    assert callable(HALL::Instructions::DomainPropertyGet.__init__)


def test_hall::instructions::domainpropertyget_constructor_args():
    sig = inspect.signature(HALL::Instructions::DomainPropertyGet.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::instructions::domainpropertyget_has_name():
    assert hasattr(HALL::Instructions::DomainPropertyGet, "name")
    descriptor = None
    for klass in HALL::Instructions::DomainPropertyGet.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::let_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::Let)


def test_hall::instructions::let_constructor_exists():
    assert callable(HALL::Instructions::Let.__init__)


def test_hall::instructions::let_constructor_args():
    sig = inspect.signature(HALL::Instructions::Let.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hall::instructions::let_has_name():
    assert hasattr(HALL::Instructions::Let, "name")
    descriptor = None
    for klass in HALL::Instructions::Let.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::setmessageparameter_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::SetMessageParameter)


def test_hall::instructions::setmessageparameter_constructor_exists():
    assert callable(HALL::Instructions::SetMessageParameter.__init__)


def test_hall::instructions::setmessageparameter_constructor_args():
    sig = inspect.signature(HALL::Instructions::SetMessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::instructions::setmessageparameter_has_field():
    assert hasattr(HALL::Instructions::SetMessageParameter, "field")
    descriptor = None
    for klass in HALL::Instructions::SetMessageParameter.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::setmessagedata_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::SetMessageData)


def test_hall::instructions::setmessagedata_constructor_exists():
    assert callable(HALL::Instructions::SetMessageData.__init__)


def test_hall::instructions::setmessagedata_constructor_args():
    sig = inspect.signature(HALL::Instructions::SetMessageData.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::instructions::setmessagedata_has_field():
    assert hasattr(HALL::Instructions::SetMessageData, "field")
    descriptor = None
    for klass in HALL::Instructions::SetMessageData.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::setstate_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::SetState)


def test_hall::instructions::setstate_constructor_exists():
    assert callable(HALL::Instructions::SetState.__init__)


def test_hall::instructions::setstate_constructor_args():
    sig = inspect.signature(HALL::Instructions::SetState.__init__)
    params = list(sig.parameters.keys())



def test_hall::instructions::getmessageparameter_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::GetMessageParameter)


def test_hall::instructions::getmessageparameter_constructor_exists():
    assert callable(HALL::Instructions::GetMessageParameter.__init__)


def test_hall::instructions::getmessageparameter_constructor_args():
    sig = inspect.signature(HALL::Instructions::GetMessageParameter.__init__)
    params = list(sig.parameters.keys())
    assert "field" in params, "Missing parameter 'field'"

def test_hall::instructions::getmessageparameter_has_field():
    assert hasattr(HALL::Instructions::GetMessageParameter, "field")
    descriptor = None
    for klass in HALL::Instructions::GetMessageParameter.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::setdata_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::SetData)


def test_hall::instructions::setdata_constructor_exists():
    assert callable(HALL::Instructions::SetData.__init__)


def test_hall::instructions::setdata_constructor_args():
    sig = inspect.signature(HALL::Instructions::SetData.__init__)
    params = list(sig.parameters.keys())



def test_hall::instructions::getstate_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::GetState)


def test_hall::instructions::getstate_constructor_exists():
    assert callable(HALL::Instructions::GetState.__init__)


def test_hall::instructions::getstate_constructor_args():
    sig = inspect.signature(HALL::Instructions::GetState.__init__)
    params = list(sig.parameters.keys())



def test_hall::instructions::binaryoperator_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::BinaryOperator)


def test_hall::instructions::binaryoperator_constructor_exists():
    assert callable(HALL::Instructions::BinaryOperator.__init__)


def test_hall::instructions::binaryoperator_constructor_args():
    sig = inspect.signature(HALL::Instructions::BinaryOperator.__init__)
    params = list(sig.parameters.keys())
    assert "operatorname" in params, "Missing parameter 'operatorname'"

def test_hall::instructions::binaryoperator_has_operatorname():
    assert hasattr(HALL::Instructions::BinaryOperator, "operatorname")
    descriptor = None
    for klass in HALL::Instructions::BinaryOperator.__mro__:
        if "operatorname" in klass.__dict__:
            descriptor = klass.__dict__["operatorname"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::literal_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::Literal)


def test_hall::instructions::literal_constructor_exists():
    assert callable(HALL::Instructions::Literal.__init__)


def test_hall::instructions::literal_constructor_args():
    sig = inspect.signature(HALL::Instructions::Literal.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_hall::instructions::literal_has_value():
    assert hasattr(HALL::Instructions::Literal, "value")
    descriptor = None
    for klass in HALL::Instructions::Literal.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_hall::instructions::posconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::PosConditionMessageExpression)


def test_hall::instructions::posconditionmessageexpression_constructor_exists():
    assert callable(HALL::Instructions::PosConditionMessageExpression.__init__)


def test_hall::instructions::posconditionmessageexpression_constructor_args():
    sig = inspect.signature(HALL::Instructions::PosConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_instructions::posconditionmessageexpression_is_not_abstract():
    assert not inspect.isabstract(Instructions::PosConditionMessageExpression)


def test_instructions::posconditionmessageexpression_constructor_exists():
    assert callable(Instructions::PosConditionMessageExpression.__init__)


def test_instructions::posconditionmessageexpression_constructor_args():
    sig = inspect.signature(Instructions::PosConditionMessageExpression.__init__)
    params = list(sig.parameters.keys())



def test_hall::instructions::posconditionmessage_is_not_abstract():
    assert not inspect.isabstract(HALL::Instructions::PosConditionMessage)


def test_hall::instructions::posconditionmessage_constructor_exists():
    assert callable(HALL::Instructions::PosConditionMessage.__init__)


def test_hall::instructions::posconditionmessage_constructor_args():
    sig = inspect.signature(HALL::Instructions::PosConditionMessage.__init__)
    params = list(sig.parameters.keys())



def test_hall::messages::initialmessagestate_is_not_abstract():
    assert not inspect.isabstract(HALL::Messages::InitialMessageState)


def test_hall::messages::initialmessagestate_constructor_exists():
    assert callable(HALL::Messages::InitialMessageState.__init__)


def test_hall::messages::initialmessagestate_constructor_args():
    sig = inspect.signature(HALL::Messages::InitialMessageState.__init__)
    params = list(sig.parameters.keys())



def test_messagetransition_is_not_abstract():
    assert not inspect.isabstract(MessageTransition)


def test_messagetransition_constructor_exists():
    assert callable(MessageTransition.__init__)


def test_messagetransition_constructor_args():
    sig = inspect.signature(MessageTransition.__init__)
    params = list(sig.parameters.keys())



def test_hall::messages::messagestate_is_not_abstract():
    assert not inspect.isabstract(HALL::Messages::MessageState)


def test_hall::messages::messagestate_constructor_exists():
    assert callable(HALL::Messages::MessageState.__init__)


def test_hall::messages::messagestate_constructor_args():
    sig = inspect.signature(HALL::Messages::MessageState.__init__)
    params = list(sig.parameters.keys())
    assert "isContinue" in params, "Missing parameter 'isContinue'"
    assert "isActive" in params, "Missing parameter 'isActive'"
    assert "isEnd" in params, "Missing parameter 'isEnd'"
    assert "name" in params, "Missing parameter 'name'"

def test_hall::messages::messagestate_has_isContinue():
    assert hasattr(HALL::Messages::MessageState, "isContinue")
    descriptor = None
    for klass in HALL::Messages::MessageState.__mro__:
        if "isContinue" in klass.__dict__:
            descriptor = klass.__dict__["isContinue"]
            break
    assert isinstance(descriptor, property)

def test_hall::messages::messagestate_has_isActive():
    assert hasattr(HALL::Messages::MessageState, "isActive")
    descriptor = None
    for klass in HALL::Messages::MessageState.__mro__:
        if "isActive" in klass.__dict__:
            descriptor = klass.__dict__["isActive"]
            break
    assert isinstance(descriptor, property)

def test_hall::messages::messagestate_has_isEnd():
    assert hasattr(HALL::Messages::MessageState, "isEnd")
    descriptor = None
    for klass in HALL::Messages::MessageState.__mro__:
        if "isEnd" in klass.__dict__:
            descriptor = klass.__dict__["isEnd"]
            break
    assert isinstance(descriptor, property)

def test_hall::messages::messagestate_has_name():
    assert hasattr(HALL::Messages::MessageState, "name")
    descriptor = None
    for klass in HALL::Messages::MessageState.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_messages::hall::component_is_not_abstract():
    assert not inspect.isabstract(Messages::HALL::Component)


def test_messages::hall::component_constructor_exists():
    assert callable(Messages::HALL::Component.__init__)


def test_messages::hall::component_constructor_args():
    sig = inspect.signature(Messages::HALL::Component.__init__)
    params = list(sig.parameters.keys())



def test_initialmessagestate_is_not_abstract():
    assert not inspect.isabstract(InitialMessageState)


def test_initialmessagestate_constructor_exists():
    assert callable(InitialMessageState.__init__)


def test_initialmessagestate_constructor_args():
    sig = inspect.signature(InitialMessageState.__init__)
    params = list(sig.parameters.keys())



def test_point_is_not_abstract():
    assert not inspect.isabstract(Point)


def test_point_constructor_exists():
    assert callable(Point.__init__)


def test_point_constructor_args():
    sig = inspect.signature(Point.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::point2d_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::Point2D)


def test_hall::geometry::point2d_constructor_exists():
    assert callable(HALL::Geometry::Point2D.__init__)


def test_hall::geometry::point2d_constructor_args():
    sig = inspect.signature(HALL::Geometry::Point2D.__init__)
    params = list(sig.parameters.keys())



def test_hall::geometry::point3d_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::Point3D)


def test_hall::geometry::point3d_constructor_exists():
    assert callable(HALL::Geometry::Point3D.__init__)


def test_hall::geometry::point3d_constructor_args():
    sig = inspect.signature(HALL::Geometry::Point3D.__init__)
    params = list(sig.parameters.keys())
    assert "zCoord" in params, "Missing parameter 'zCoord'"

def test_hall::geometry::point3d_has_zCoord():
    assert hasattr(HALL::Geometry::Point3D, "zCoord")
    descriptor = None
    for klass in HALL::Geometry::Point3D.__mro__:
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



def test_hall::geometry::face_is_not_abstract():
    assert not inspect.isabstract(HALL::Geometry::Face)


def test_hall::geometry::face_constructor_exists():
    assert callable(HALL::Geometry::Face.__init__)


def test_hall::geometry::face_constructor_args():
    sig = inspect.signature(HALL::Geometry::Face.__init__)
    params = list(sig.parameters.keys())
    assert "labelText" in params, "Missing parameter 'labelText'"

def test_hall::geometry::face_has_labelText():
    assert hasattr(HALL::Geometry::Face, "labelText")
    descriptor = None
    for klass in HALL::Geometry::Face.__mro__:
        if "labelText" in klass.__dict__:
            descriptor = klass.__dict__["labelText"]
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
Messages::HALL::Parameter_strategy = st.builds(
    Messages::HALL::Parameter,
)
Messages::HALL::Model_strategy = st.builds(
    Messages::HALL::Model,
)
HALL::Messages::MessageDefinition_strategy = st.builds(
    HALL::Messages::MessageDefinition,
    name=
        safe_text
)
Actions::ActionMessage_strategy = st.builds(
    Actions::ActionMessage,
)
Instructions::PosConditionMessage_strategy = st.builds(
    Instructions::PosConditionMessage,
)
Conditions::PreConditionMessage_strategy = st.builds(
    Conditions::PreConditionMessage,
)
MessageState_strategy = st.builds(
    MessageState,
)
HALL::Messages::RegularMessageState_strategy = st.builds(
    HALL::Messages::RegularMessageState,
)
HALL::Messages::MessageTransition_strategy = st.builds(
    HALL::Messages::MessageTransition,
    name=
        safe_text
)
HALL::Geometry::Point_strategy = st.builds(
    HALL::Geometry::Point,
    yCoord=
        st.integers(),
    xCoord=
        st.integers()
)
GeometryData2D_strategy = st.builds(
    GeometryData2D,
)
HALL::Geometry::AlphaTransparency_strategy = st.builds(
    HALL::Geometry::AlphaTransparency,
    value=
        st.integers()
)
AlphaTransparency_strategy = st.builds(
    AlphaTransparency,
)
Point2D_strategy = st.builds(
    Point2D,
)
Face_strategy = st.builds(
    Face,
)
HALL::Geometry::GeometryData_strategy = st.builds(
    HALL::Geometry::GeometryData,
)
Geometry::HALL::VisualObject_strategy = st.builds(
    Geometry::HALL::VisualObject,
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
HALL::Geometry::ColorData_strategy = st.builds(
    HALL::Geometry::ColorData,
)
HALL::Parameter_strategy = st.builds(
    HALL::Parameter,
    name=
        safe_text
)
HALL::Geometry::ColorState_strategy = st.builds(
    HALL::Geometry::ColorState,
)
Color_strategy = st.builds(
    Color,
)
HALL::Geometry::RGBColor_strategy = st.builds(
    HALL::Geometry::RGBColor,
    blueValue=
        st.integers(),
    greenValue=
        st.integers(),
    redValue=
        st.integers()
)
ColorState_strategy = st.builds(
    ColorState,
)
HALL::Geometry::SelectedColors_strategy = st.builds(
    HALL::Geometry::SelectedColors,
)
HALL::Geometry::DisabledColors_strategy = st.builds(
    HALL::Geometry::DisabledColors,
)
HALL::Geometry::NormalColors_strategy = st.builds(
    HALL::Geometry::NormalColors,
)
RGBColor_strategy = st.builds(
    RGBColor,
)
HALL::Geometry::Color_strategy = st.builds(
    HALL::Geometry::Color,
)
Type_strategy = st.builds(
    Type,
)
MessageDefinition_strategy = st.builds(
    MessageDefinition,
)
HALL::Goal_strategy = st.builds(
    HALL::Goal,
    condition=
        safe_text
)
ColorData_strategy = st.builds(
    ColorData,
)
Component_strategy = st.builds(
    Component,
)
HALL::TaskObject_strategy = st.builds(
    HALL::TaskObject,
    numberofgoalscompleted=
        st.integers(),
    completionTime=
        st.integers()
)
HALL::VisualObject_strategy = st.builds(
    HALL::VisualObject,
    vtype=
        safe_text
)
HALL::Model_strategy = st.builds(
    HALL::Model,
)
HALL::SystemComponent_strategy = st.builds(
    HALL::SystemComponent,
)
MessageHandler_strategy = st.builds(
    MessageHandler,
)
FSM_strategy = st.builds(
    FSM,
)
HALL::Data_strategy = st.builds(
    HALL::Data,
    initValue=
        safe_text,
    name=
        safe_text,
    currentValue=
        safe_text
)
HALL::Component_strategy = st.builds(
    HALL::Component,
    name=
        safe_text
)
HALL::UserProfile_strategy = st.builds(
    HALL::UserProfile,
    numberofcompletedtasks=
        st.integers()
)
GeometryData_strategy = st.builds(
    GeometryData,
)
HALL::Geometry::GeometryData3D_strategy = st.builds(
    HALL::Geometry::GeometryData3D,
)
HALL::Geometry::GeometryData2D_strategy = st.builds(
    HALL::Geometry::GeometryData2D,
    labelText=
        safe_text
)
FSMActions::Let_strategy = st.builds(
    FSMActions::Let,
)
SimpleType_strategy = st.builds(
    SimpleType,
)
HALL::Types::Boolean_strategy = st.builds(
    HALL::Types::Boolean,
)
HALL::Types::Number_strategy = st.builds(
    HALL::Types::Number,
)
HALL::Types::String_strategy = st.builds(
    HALL::Types::String,
)
HALL::Types::Set_strategy = st.builds(
    HALL::Types::Set,
)
Set_strategy = st.builds(
    Set,
)
HALL::Types::SimpleType_strategy = st.builds(
    HALL::Types::SimpleType,
)
HALL::Types::Type_strategy = st.builds(
    HALL::Types::Type,
    name=
        safe_text
)
FSMActions::HALL::Data_strategy = st.builds(
    FSMActions::HALL::Data,
)
FSMConditions::HALL::Component_strategy = st.builds(
    FSMConditions::HALL::Component,
)
ActionExpression_strategy = st.builds(
    ActionExpression,
)
HALL::FSMActions::VarRef_strategy = st.builds(
    HALL::FSMActions::VarRef,
)
HALL::FSMActions::DomainPropertySet_strategy = st.builds(
    HALL::FSMActions::DomainPropertySet,
    name=
        safe_text
)
HALL::FSMActions::UnaryOperator_strategy = st.builds(
    HALL::FSMActions::UnaryOperator,
    operatorname=
        safe_text
)
HALL::FSMActions::Let_strategy = st.builds(
    HALL::FSMActions::Let,
    name=
        safe_text
)
HALL::FSMActions::GetData_strategy = st.builds(
    HALL::FSMActions::GetData,
)
HALL::FSMActions::BinaryOperator_strategy = st.builds(
    HALL::FSMActions::BinaryOperator,
    operatorname=
        safe_text
)
HALL::FSMActions::MessageInvocation_strategy = st.builds(
    HALL::FSMActions::MessageInvocation,
    isTopDown=
        st.booleans()
)
HALL::FSMActions::DomainPropertyGet_strategy = st.builds(
    HALL::FSMActions::DomainPropertyGet,
    name=
        safe_text
)
HALL::FSMActions::Literal_strategy = st.builds(
    HALL::FSMActions::Literal,
    value=
        safe_text
)
HALL::FSMActions::ActionExpression_strategy = st.builds(
    HALL::FSMActions::ActionExpression,
)
FSMActions::ActionExpression_strategy = st.builds(
    FSMActions::ActionExpression,
)
HALL::FSMActions::Action_strategy = st.builds(
    HALL::FSMActions::Action,
)
FSMConditions::Let_strategy = st.builds(
    FSMConditions::Let,
)
FSMConditions::HALL::Data_strategy = st.builds(
    FSMConditions::HALL::Data,
)
PreConditionExpression_strategy = st.builds(
    PreConditionExpression,
)
HALL::FSMConditions::DomainPropertyGet_strategy = st.builds(
    HALL::FSMConditions::DomainPropertyGet,
    name=
        safe_text
)
HALL::FSMConditions::UnaryOperator_strategy = st.builds(
    HALL::FSMConditions::UnaryOperator,
    operatorname=
        safe_text
)
HALL::FSMConditions::VarRef_strategy = st.builds(
    HALL::FSMConditions::VarRef,
)
HALL::FSMConditions::GetState_strategy = st.builds(
    HALL::FSMConditions::GetState,
)
HALL::FSMConditions::BinaryOperator_strategy = st.builds(
    HALL::FSMConditions::BinaryOperator,
    operatorname=
        safe_text
)
HALL::FSMConditions::GetData_strategy = st.builds(
    HALL::FSMConditions::GetData,
)
HALL::FSMConditions::Let_strategy = st.builds(
    HALL::FSMConditions::Let,
    name=
        safe_text
)
HALL::FSMConditions::Literal_strategy = st.builds(
    HALL::FSMConditions::Literal,
    value=
        safe_text
)
HALL::FSMConditions::PreConditionExpression_strategy = st.builds(
    HALL::FSMConditions::PreConditionExpression,
)
FSMConditions::PreConditionExpression_strategy = st.builds(
    FSMConditions::PreConditionExpression,
)
HALL::FSMConditions::PreCondition_strategy = st.builds(
    HALL::FSMConditions::PreCondition,
)
FSMInstructions::Let_strategy = st.builds(
    FSMInstructions::Let,
)
FSMInstructions::HALL::Data_strategy = st.builds(
    FSMInstructions::HALL::Data,
)
TriggerExpression_strategy = st.builds(
    TriggerExpression,
)
HALL::Trigger::MessageNotification_strategy = st.builds(
    HALL::Trigger::MessageNotification,
)
HALL::Trigger::TriggerExpression_strategy = st.builds(
    HALL::Trigger::TriggerExpression,
)
Trigger::TriggerExpression_strategy = st.builds(
    Trigger::TriggerExpression,
)
HALL::Trigger::Trigger_strategy = st.builds(
    HALL::Trigger::Trigger,
)
FSMInstructions::HALL::Component_strategy = st.builds(
    FSMInstructions::HALL::Component,
)
PosConditionExpression_strategy = st.builds(
    PosConditionExpression,
)
HALL::FSMInstructions::UnaryOperator_strategy = st.builds(
    HALL::FSMInstructions::UnaryOperator,
    operatorname=
        safe_text
)
HALL::FSMInstructions::Let_strategy = st.builds(
    HALL::FSMInstructions::Let,
    name=
        safe_text
)
HALL::FSMInstructions::GetState_strategy = st.builds(
    HALL::FSMInstructions::GetState,
)
HALL::FSMInstructions::SetState_strategy = st.builds(
    HALL::FSMInstructions::SetState,
)
HALL::FSMInstructions::VarRef_strategy = st.builds(
    HALL::FSMInstructions::VarRef,
)
HALL::FSMInstructions::BinaryOperator_strategy = st.builds(
    HALL::FSMInstructions::BinaryOperator,
    operatorname=
        safe_text
)
HALL::FSMInstructions::GetData_strategy = st.builds(
    HALL::FSMInstructions::GetData,
    field=
        safe_text
)
HALL::FSMInstructions::SetData_strategy = st.builds(
    HALL::FSMInstructions::SetData,
    field=
        safe_text
)
HALL::FSMInstructions::DomainPropertyGet_strategy = st.builds(
    HALL::FSMInstructions::DomainPropertyGet,
    name=
        safe_text
)
HALL::FSMInstructions::Literal_strategy = st.builds(
    HALL::FSMInstructions::Literal,
    value=
        safe_text
)
HALL::FSMInstructions::PosConditionExpression_strategy = st.builds(
    HALL::FSMInstructions::PosConditionExpression,
)
FSMInstructions::PosConditionExpression_strategy = st.builds(
    FSMInstructions::PosConditionExpression,
)
HALL::FSMInstructions::PosCondition_strategy = st.builds(
    HALL::FSMInstructions::PosCondition,
)
HALL::Trigger::DomainEventFired_strategy = st.builds(
    HALL::Trigger::DomainEventFired,
    name=
        safe_text
)
RegularState_strategy = st.builds(
    RegularState,
)
InitialState_strategy = st.builds(
    InitialState,
)
FSM::HALL::Component_strategy = st.builds(
    FSM::HALL::Component,
)
HALL::FSM::FSM_strategy = st.builds(
    HALL::FSM::FSM,
)
Transition_strategy = st.builds(
    Transition,
)
HALL::FSM::State_strategy = st.builds(
    HALL::FSM::State,
    isActive=
        st.booleans(),
    name=
        safe_text
)
Trigger::Trigger_strategy = st.builds(
    Trigger::Trigger,
)
FSMActions::Action_strategy = st.builds(
    FSMActions::Action,
)
FSMInstructions::PosCondition_strategy = st.builds(
    FSMInstructions::PosCondition,
)
FSMConditions::PreCondition_strategy = st.builds(
    FSMConditions::PreCondition,
)
HALL::FSM::Transition_strategy = st.builds(
    HALL::FSM::Transition,
    name=
        safe_text
)
Actions::HALL::Component_strategy = st.builds(
    Actions::HALL::Component,
)
Actions::Let_strategy = st.builds(
    Actions::Let,
)
ActionMessageExpression_strategy = st.builds(
    ActionMessageExpression,
)
HALL::Actions::UnaryOperator_strategy = st.builds(
    HALL::Actions::UnaryOperator,
    operatorname=
        safe_text
)
HALL::Actions::GetMessageParameter_strategy = st.builds(
    HALL::Actions::GetMessageParameter,
    field=
        safe_text
)
HALL::FSMActions::Enable_strategy = st.builds(
    HALL::FSMActions::Enable,
)
HALL::Actions::DomainPropertySet_strategy = st.builds(
    HALL::Actions::DomainPropertySet,
    name=
        safe_text
)
HALL::Actions::Enable_strategy = st.builds(
    HALL::Actions::Enable,
)
HALL::Actions::MessageInvocation_strategy = st.builds(
    HALL::Actions::MessageInvocation,
    isTopDown=
        st.booleans()
)
HALL::Actions::GetMessageData_strategy = st.builds(
    HALL::Actions::GetMessageData,
    field=
        safe_text
)
HALL::Actions::BinaryOperator_strategy = st.builds(
    HALL::Actions::BinaryOperator,
    operatorname=
        safe_text
)
HALL::Actions::Literal_strategy = st.builds(
    HALL::Actions::Literal,
    value=
        safe_text
)
HALL::Actions::Let_strategy = st.builds(
    HALL::Actions::Let,
)
HALL::Actions::DomainPropertyGet_strategy = st.builds(
    HALL::Actions::DomainPropertyGet,
    name=
        safe_text
)
HALL::Actions::GetData_strategy = st.builds(
    HALL::Actions::GetData,
)
HALL::Actions::VarRef_strategy = st.builds(
    HALL::Actions::VarRef,
)
HALL::Actions::ActionMessageExpression_strategy = st.builds(
    HALL::Actions::ActionMessageExpression,
)
Actions::ActionMessageExpression_strategy = st.builds(
    Actions::ActionMessageExpression,
)
HALL::Actions::ActionMessage_strategy = st.builds(
    HALL::Actions::ActionMessage,
)
Conditions::Let_strategy = st.builds(
    Conditions::Let,
)
Conditions::HALL::Data_strategy = st.builds(
    Conditions::HALL::Data,
)
Conditions::HALL::Component_strategy = st.builds(
    Conditions::HALL::Component,
)
PreConditionMessageExpression_strategy = st.builds(
    PreConditionMessageExpression,
)
HALL::Conditions::GetMessageData_strategy = st.builds(
    HALL::Conditions::GetMessageData,
    field=
        safe_text
)
HALL::Conditions::GetState_strategy = st.builds(
    HALL::Conditions::GetState,
)
HALL::Conditions::UnaryOperator_strategy = st.builds(
    HALL::Conditions::UnaryOperator,
    operatorname=
        safe_text
)
HALL::Conditions::GetData_strategy = st.builds(
    HALL::Conditions::GetData,
)
HALL::Conditions::VarRef_strategy = st.builds(
    HALL::Conditions::VarRef,
)
HALL::Conditions::Let_strategy = st.builds(
    HALL::Conditions::Let,
    name=
        safe_text
)
HALL::Conditions::GetMessageParameter_strategy = st.builds(
    HALL::Conditions::GetMessageParameter,
    field=
        safe_text
)
HALL::Conditions::DomainPropertyGet_strategy = st.builds(
    HALL::Conditions::DomainPropertyGet,
    name=
        safe_text
)
HALL::Conditions::BinaryOperator_strategy = st.builds(
    HALL::Conditions::BinaryOperator,
    operatorname=
        safe_text
)
HALL::Conditions::Literal_strategy = st.builds(
    HALL::Conditions::Literal,
    value=
        safe_text
)
HALL::Conditions::PreConditionMessageExpression_strategy = st.builds(
    HALL::Conditions::PreConditionMessageExpression,
)
Conditions::PreConditionMessageExpression_strategy = st.builds(
    Conditions::PreConditionMessageExpression,
)
HALL::Conditions::PreConditionMessage_strategy = st.builds(
    HALL::Conditions::PreConditionMessage,
)
Instructions::Let_strategy = st.builds(
    Instructions::Let,
)
Instructions::HALL::Component_strategy = st.builds(
    Instructions::HALL::Component,
)
Instructions::HALL::Data_strategy = st.builds(
    Instructions::HALL::Data,
)
State_strategy = st.builds(
    State,
)
HALL::FSM::RegularState_strategy = st.builds(
    HALL::FSM::RegularState,
)
HALL::FSM::InitialState_strategy = st.builds(
    HALL::FSM::InitialState,
)
RegularMessageState_strategy = st.builds(
    RegularMessageState,
)
HALL::Messages::MessageHandler_strategy = st.builds(
    HALL::Messages::MessageHandler,
)
Messages::HALL::Data_strategy = st.builds(
    Messages::HALL::Data,
)
PosConditionMessageExpression_strategy = st.builds(
    PosConditionMessageExpression,
)
HALL::Instructions::SetTopDown_strategy = st.builds(
    HALL::Instructions::SetTopDown,
)
HALL::Instructions::UnaryOperator_strategy = st.builds(
    HALL::Instructions::UnaryOperator,
    operatorname=
        safe_text
)
HALL::Instructions::GetData_strategy = st.builds(
    HALL::Instructions::GetData,
)
HALL::Instructions::GetMessageData_strategy = st.builds(
    HALL::Instructions::GetMessageData,
    field=
        safe_text
)
HALL::Instructions::VarRef_strategy = st.builds(
    HALL::Instructions::VarRef,
)
HALL::Instructions::DomainPropertyGet_strategy = st.builds(
    HALL::Instructions::DomainPropertyGet,
    name=
        safe_text
)
HALL::Instructions::Let_strategy = st.builds(
    HALL::Instructions::Let,
    name=
        safe_text
)
HALL::Instructions::SetMessageParameter_strategy = st.builds(
    HALL::Instructions::SetMessageParameter,
    field=
        safe_text
)
HALL::Instructions::SetMessageData_strategy = st.builds(
    HALL::Instructions::SetMessageData,
    field=
        safe_text
)
HALL::Instructions::SetState_strategy = st.builds(
    HALL::Instructions::SetState,
)
HALL::Instructions::GetMessageParameter_strategy = st.builds(
    HALL::Instructions::GetMessageParameter,
    field=
        safe_text
)
HALL::Instructions::SetData_strategy = st.builds(
    HALL::Instructions::SetData,
)
HALL::Instructions::GetState_strategy = st.builds(
    HALL::Instructions::GetState,
)
HALL::Instructions::BinaryOperator_strategy = st.builds(
    HALL::Instructions::BinaryOperator,
    operatorname=
        safe_text
)
HALL::Instructions::Literal_strategy = st.builds(
    HALL::Instructions::Literal,
    value=
        safe_text
)
HALL::Instructions::PosConditionMessageExpression_strategy = st.builds(
    HALL::Instructions::PosConditionMessageExpression,
)
Instructions::PosConditionMessageExpression_strategy = st.builds(
    Instructions::PosConditionMessageExpression,
)
HALL::Instructions::PosConditionMessage_strategy = st.builds(
    HALL::Instructions::PosConditionMessage,
)
HALL::Messages::InitialMessageState_strategy = st.builds(
    HALL::Messages::InitialMessageState,
)
MessageTransition_strategy = st.builds(
    MessageTransition,
)
HALL::Messages::MessageState_strategy = st.builds(
    HALL::Messages::MessageState,
    isContinue=
        st.booleans(),
    isActive=
        st.booleans(),
    isEnd=
        st.booleans(),
    name=
        safe_text
)
Messages::HALL::Component_strategy = st.builds(
    Messages::HALL::Component,
)
InitialMessageState_strategy = st.builds(
    InitialMessageState,
)
Point_strategy = st.builds(
    Point,
)
HALL::Geometry::Point2D_strategy = st.builds(
    HALL::Geometry::Point2D,
)
HALL::Geometry::Point3D_strategy = st.builds(
    HALL::Geometry::Point3D,
    zCoord=
        st.integers()
)
GeometryData3D_strategy = st.builds(
    GeometryData3D,
)
Point3D_strategy = st.builds(
    Point3D,
)
HALL::Geometry::Face_strategy = st.builds(
    HALL::Geometry::Face,
    labelText=
        safe_text
)

@given(instance=Messages::HALL::Parameter_strategy)
@settings(max_examples=50)
def test_messages::hall::parameter_instantiation(instance):
    assert isinstance(instance, Messages::HALL::Parameter)

@given(instance=Messages::HALL::Model_strategy)
@settings(max_examples=50)
def test_messages::hall::model_instantiation(instance):
    assert isinstance(instance, Messages::HALL::Model)

@given(instance=HALL::Messages::MessageDefinition_strategy)
@settings(max_examples=50)
def test_hall::messages::messagedefinition_instantiation(instance):
    assert isinstance(instance, HALL::Messages::MessageDefinition)

@given(instance=HALL::Messages::MessageDefinition_strategy)
def test_hall::messages::messagedefinition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Messages::MessageDefinition_strategy)
def test_hall::messages::messagedefinition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Actions::ActionMessage_strategy)
@settings(max_examples=50)
def test_actions::actionmessage_instantiation(instance):
    assert isinstance(instance, Actions::ActionMessage)

@given(instance=Instructions::PosConditionMessage_strategy)
@settings(max_examples=50)
def test_instructions::posconditionmessage_instantiation(instance):
    assert isinstance(instance, Instructions::PosConditionMessage)

@given(instance=Conditions::PreConditionMessage_strategy)
@settings(max_examples=50)
def test_conditions::preconditionmessage_instantiation(instance):
    assert isinstance(instance, Conditions::PreConditionMessage)

@given(instance=MessageState_strategy)
@settings(max_examples=50)
def test_messagestate_instantiation(instance):
    assert isinstance(instance, MessageState)

@given(instance=HALL::Messages::RegularMessageState_strategy)
@settings(max_examples=50)
def test_hall::messages::regularmessagestate_instantiation(instance):
    assert isinstance(instance, HALL::Messages::RegularMessageState)

@given(instance=HALL::Messages::MessageTransition_strategy)
@settings(max_examples=50)
def test_hall::messages::messagetransition_instantiation(instance):
    assert isinstance(instance, HALL::Messages::MessageTransition)

@given(instance=HALL::Messages::MessageTransition_strategy)
def test_hall::messages::messagetransition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Messages::MessageTransition_strategy)
def test_hall::messages::messagetransition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Geometry::Point_strategy)
@settings(max_examples=50)
def test_hall::geometry::point_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::Point)

@given(instance=HALL::Geometry::Point_strategy)
def test_hall::geometry::point_yCoord_type(instance):
    assert isinstance(instance.yCoord, int)


@given(instance=HALL::Geometry::Point_strategy)
def test_hall::geometry::point_yCoord_setter(instance):
    original = instance.yCoord
    instance.yCoord = original
    assert instance.yCoord == original

@given(instance=HALL::Geometry::Point_strategy)
def test_hall::geometry::point_xCoord_type(instance):
    assert isinstance(instance.xCoord, int)


@given(instance=HALL::Geometry::Point_strategy)
def test_hall::geometry::point_xCoord_setter(instance):
    original = instance.xCoord
    instance.xCoord = original
    assert instance.xCoord == original

@given(instance=GeometryData2D_strategy)
@settings(max_examples=50)
def test_geometrydata2d_instantiation(instance):
    assert isinstance(instance, GeometryData2D)

@given(instance=HALL::Geometry::AlphaTransparency_strategy)
@settings(max_examples=50)
def test_hall::geometry::alphatransparency_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::AlphaTransparency)

@given(instance=HALL::Geometry::AlphaTransparency_strategy)
def test_hall::geometry::alphatransparency_value_type(instance):
    assert isinstance(instance.value, int)


@given(instance=HALL::Geometry::AlphaTransparency_strategy)
def test_hall::geometry::alphatransparency_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=AlphaTransparency_strategy)
@settings(max_examples=50)
def test_alphatransparency_instantiation(instance):
    assert isinstance(instance, AlphaTransparency)

@given(instance=Point2D_strategy)
@settings(max_examples=50)
def test_point2d_instantiation(instance):
    assert isinstance(instance, Point2D)

@given(instance=Face_strategy)
@settings(max_examples=50)
def test_face_instantiation(instance):
    assert isinstance(instance, Face)

@given(instance=HALL::Geometry::GeometryData_strategy)
@settings(max_examples=50)
def test_hall::geometry::geometrydata_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::GeometryData)

@given(instance=Geometry::HALL::VisualObject_strategy)
@settings(max_examples=50)
def test_geometry::hall::visualobject_instantiation(instance):
    assert isinstance(instance, Geometry::HALL::VisualObject)

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

@given(instance=HALL::Geometry::ColorData_strategy)
@settings(max_examples=50)
def test_hall::geometry::colordata_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::ColorData)

@given(instance=HALL::Parameter_strategy)
@settings(max_examples=50)
def test_hall::parameter_instantiation(instance):
    assert isinstance(instance, HALL::Parameter)

@given(instance=HALL::Parameter_strategy)
def test_hall::parameter_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Parameter_strategy)
def test_hall::parameter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Geometry::ColorState_strategy)
@settings(max_examples=50)
def test_hall::geometry::colorstate_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::ColorState)

@given(instance=Color_strategy)
@settings(max_examples=50)
def test_color_instantiation(instance):
    assert isinstance(instance, Color)

@given(instance=HALL::Geometry::RGBColor_strategy)
@settings(max_examples=50)
def test_hall::geometry::rgbcolor_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::RGBColor)

@given(instance=HALL::Geometry::RGBColor_strategy)
def test_hall::geometry::rgbcolor_blueValue_type(instance):
    assert isinstance(instance.blueValue, int)


@given(instance=HALL::Geometry::RGBColor_strategy)
def test_hall::geometry::rgbcolor_blueValue_setter(instance):
    original = instance.blueValue
    instance.blueValue = original
    assert instance.blueValue == original

@given(instance=HALL::Geometry::RGBColor_strategy)
def test_hall::geometry::rgbcolor_greenValue_type(instance):
    assert isinstance(instance.greenValue, int)


@given(instance=HALL::Geometry::RGBColor_strategy)
def test_hall::geometry::rgbcolor_greenValue_setter(instance):
    original = instance.greenValue
    instance.greenValue = original
    assert instance.greenValue == original

@given(instance=HALL::Geometry::RGBColor_strategy)
def test_hall::geometry::rgbcolor_redValue_type(instance):
    assert isinstance(instance.redValue, int)


@given(instance=HALL::Geometry::RGBColor_strategy)
def test_hall::geometry::rgbcolor_redValue_setter(instance):
    original = instance.redValue
    instance.redValue = original
    assert instance.redValue == original

@given(instance=ColorState_strategy)
@settings(max_examples=50)
def test_colorstate_instantiation(instance):
    assert isinstance(instance, ColorState)

@given(instance=HALL::Geometry::SelectedColors_strategy)
@settings(max_examples=50)
def test_hall::geometry::selectedcolors_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::SelectedColors)

@given(instance=HALL::Geometry::DisabledColors_strategy)
@settings(max_examples=50)
def test_hall::geometry::disabledcolors_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::DisabledColors)

@given(instance=HALL::Geometry::NormalColors_strategy)
@settings(max_examples=50)
def test_hall::geometry::normalcolors_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::NormalColors)

@given(instance=RGBColor_strategy)
@settings(max_examples=50)
def test_rgbcolor_instantiation(instance):
    assert isinstance(instance, RGBColor)

@given(instance=HALL::Geometry::Color_strategy)
@settings(max_examples=50)
def test_hall::geometry::color_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::Color)

@given(instance=Type_strategy)
@settings(max_examples=50)
def test_type_instantiation(instance):
    assert isinstance(instance, Type)

@given(instance=MessageDefinition_strategy)
@settings(max_examples=50)
def test_messagedefinition_instantiation(instance):
    assert isinstance(instance, MessageDefinition)

@given(instance=HALL::Goal_strategy)
@settings(max_examples=50)
def test_hall::goal_instantiation(instance):
    assert isinstance(instance, HALL::Goal)

@given(instance=HALL::Goal_strategy)
def test_hall::goal_condition_type(instance):
    assert isinstance(instance.condition, str)


@given(instance=HALL::Goal_strategy)
def test_hall::goal_condition_setter(instance):
    original = instance.condition
    instance.condition = original
    assert instance.condition == original

@given(instance=ColorData_strategy)
@settings(max_examples=50)
def test_colordata_instantiation(instance):
    assert isinstance(instance, ColorData)

@given(instance=Component_strategy)
@settings(max_examples=50)
def test_component_instantiation(instance):
    assert isinstance(instance, Component)

@given(instance=HALL::TaskObject_strategy)
@settings(max_examples=50)
def test_hall::taskobject_instantiation(instance):
    assert isinstance(instance, HALL::TaskObject)

@given(instance=HALL::TaskObject_strategy)
def test_hall::taskobject_numberofgoalscompleted_type(instance):
    assert isinstance(instance.numberofgoalscompleted, int)


@given(instance=HALL::TaskObject_strategy)
def test_hall::taskobject_numberofgoalscompleted_setter(instance):
    original = instance.numberofgoalscompleted
    instance.numberofgoalscompleted = original
    assert instance.numberofgoalscompleted == original

@given(instance=HALL::TaskObject_strategy)
def test_hall::taskobject_completionTime_type(instance):
    assert isinstance(instance.completionTime, int)


@given(instance=HALL::TaskObject_strategy)
def test_hall::taskobject_completionTime_setter(instance):
    original = instance.completionTime
    instance.completionTime = original
    assert instance.completionTime == original

@given(instance=HALL::VisualObject_strategy)
@settings(max_examples=50)
def test_hall::visualobject_instantiation(instance):
    assert isinstance(instance, HALL::VisualObject)

@given(instance=HALL::VisualObject_strategy)
def test_hall::visualobject_vtype_type(instance):
    assert isinstance(instance.vtype, str)


@given(instance=HALL::VisualObject_strategy)
def test_hall::visualobject_vtype_setter(instance):
    original = instance.vtype
    instance.vtype = original
    assert instance.vtype == original

@given(instance=HALL::Model_strategy)
@settings(max_examples=50)
def test_hall::model_instantiation(instance):
    assert isinstance(instance, HALL::Model)

@given(instance=HALL::SystemComponent_strategy)
@settings(max_examples=50)
def test_hall::systemcomponent_instantiation(instance):
    assert isinstance(instance, HALL::SystemComponent)

@given(instance=MessageHandler_strategy)
@settings(max_examples=50)
def test_messagehandler_instantiation(instance):
    assert isinstance(instance, MessageHandler)

@given(instance=FSM_strategy)
@settings(max_examples=50)
def test_fsm_instantiation(instance):
    assert isinstance(instance, FSM)

@given(instance=HALL::Data_strategy)
@settings(max_examples=50)
def test_hall::data_instantiation(instance):
    assert isinstance(instance, HALL::Data)

@given(instance=HALL::Data_strategy)
def test_hall::data_initValue_type(instance):
    assert isinstance(instance.initValue, str)


@given(instance=HALL::Data_strategy)
def test_hall::data_initValue_setter(instance):
    original = instance.initValue
    instance.initValue = original
    assert instance.initValue == original

@given(instance=HALL::Data_strategy)
def test_hall::data_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Data_strategy)
def test_hall::data_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Data_strategy)
def test_hall::data_currentValue_type(instance):
    assert isinstance(instance.currentValue, str)


@given(instance=HALL::Data_strategy)
def test_hall::data_currentValue_setter(instance):
    original = instance.currentValue
    instance.currentValue = original
    assert instance.currentValue == original

@given(instance=HALL::Component_strategy)
@settings(max_examples=50)
def test_hall::component_instantiation(instance):
    assert isinstance(instance, HALL::Component)

@given(instance=HALL::Component_strategy)
def test_hall::component_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Component_strategy)
def test_hall::component_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::UserProfile_strategy)
@settings(max_examples=50)
def test_hall::userprofile_instantiation(instance):
    assert isinstance(instance, HALL::UserProfile)

@given(instance=HALL::UserProfile_strategy)
def test_hall::userprofile_numberofcompletedtasks_type(instance):
    assert isinstance(instance.numberofcompletedtasks, int)


@given(instance=HALL::UserProfile_strategy)
def test_hall::userprofile_numberofcompletedtasks_setter(instance):
    original = instance.numberofcompletedtasks
    instance.numberofcompletedtasks = original
    assert instance.numberofcompletedtasks == original

@given(instance=GeometryData_strategy)
@settings(max_examples=50)
def test_geometrydata_instantiation(instance):
    assert isinstance(instance, GeometryData)

@given(instance=HALL::Geometry::GeometryData3D_strategy)
@settings(max_examples=50)
def test_hall::geometry::geometrydata3d_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::GeometryData3D)

@given(instance=HALL::Geometry::GeometryData2D_strategy)
@settings(max_examples=50)
def test_hall::geometry::geometrydata2d_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::GeometryData2D)

@given(instance=HALL::Geometry::GeometryData2D_strategy)
def test_hall::geometry::geometrydata2d_labelText_type(instance):
    assert isinstance(instance.labelText, str)


@given(instance=HALL::Geometry::GeometryData2D_strategy)
def test_hall::geometry::geometrydata2d_labelText_setter(instance):
    original = instance.labelText
    instance.labelText = original
    assert instance.labelText == original

@given(instance=FSMActions::Let_strategy)
@settings(max_examples=50)
def test_fsmactions::let_instantiation(instance):
    assert isinstance(instance, FSMActions::Let)

@given(instance=SimpleType_strategy)
@settings(max_examples=50)
def test_simpletype_instantiation(instance):
    assert isinstance(instance, SimpleType)

@given(instance=HALL::Types::Boolean_strategy)
@settings(max_examples=50)
def test_hall::types::boolean_instantiation(instance):
    assert isinstance(instance, HALL::Types::Boolean)

@given(instance=HALL::Types::Number_strategy)
@settings(max_examples=50)
def test_hall::types::number_instantiation(instance):
    assert isinstance(instance, HALL::Types::Number)

@given(instance=HALL::Types::String_strategy)
@settings(max_examples=50)
def test_hall::types::string_instantiation(instance):
    assert isinstance(instance, HALL::Types::String)

@given(instance=HALL::Types::Set_strategy)
@settings(max_examples=50)
def test_hall::types::set_instantiation(instance):
    assert isinstance(instance, HALL::Types::Set)

@given(instance=Set_strategy)
@settings(max_examples=50)
def test_set_instantiation(instance):
    assert isinstance(instance, Set)

@given(instance=HALL::Types::SimpleType_strategy)
@settings(max_examples=50)
def test_hall::types::simpletype_instantiation(instance):
    assert isinstance(instance, HALL::Types::SimpleType)

@given(instance=HALL::Types::Type_strategy)
@settings(max_examples=50)
def test_hall::types::type_instantiation(instance):
    assert isinstance(instance, HALL::Types::Type)

@given(instance=HALL::Types::Type_strategy)
def test_hall::types::type_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Types::Type_strategy)
def test_hall::types::type_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=FSMActions::HALL::Data_strategy)
@settings(max_examples=50)
def test_fsmactions::hall::data_instantiation(instance):
    assert isinstance(instance, FSMActions::HALL::Data)

@given(instance=FSMConditions::HALL::Component_strategy)
@settings(max_examples=50)
def test_fsmconditions::hall::component_instantiation(instance):
    assert isinstance(instance, FSMConditions::HALL::Component)

@given(instance=ActionExpression_strategy)
@settings(max_examples=50)
def test_actionexpression_instantiation(instance):
    assert isinstance(instance, ActionExpression)

@given(instance=HALL::FSMActions::VarRef_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::varref_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::VarRef)

@given(instance=HALL::FSMActions::DomainPropertySet_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::domainpropertyset_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::DomainPropertySet)

@given(instance=HALL::FSMActions::DomainPropertySet_strategy)
def test_hall::fsmactions::domainpropertyset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSMActions::DomainPropertySet_strategy)
def test_hall::fsmactions::domainpropertyset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::FSMActions::UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::UnaryOperator)

@given(instance=HALL::FSMActions::UnaryOperator_strategy)
def test_hall::fsmactions::unaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::FSMActions::UnaryOperator_strategy)
def test_hall::fsmactions::unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::FSMActions::Let_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::let_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::Let)

@given(instance=HALL::FSMActions::Let_strategy)
def test_hall::fsmactions::let_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSMActions::Let_strategy)
def test_hall::fsmactions::let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::FSMActions::GetData_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::getdata_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::GetData)

@given(instance=HALL::FSMActions::BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::BinaryOperator)

@given(instance=HALL::FSMActions::BinaryOperator_strategy)
def test_hall::fsmactions::binaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::FSMActions::BinaryOperator_strategy)
def test_hall::fsmactions::binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::FSMActions::MessageInvocation_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::messageinvocation_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::MessageInvocation)

@given(instance=HALL::FSMActions::MessageInvocation_strategy)
def test_hall::fsmactions::messageinvocation_isTopDown_type(instance):
    assert isinstance(instance.isTopDown, bool)


@given(instance=HALL::FSMActions::MessageInvocation_strategy)
def test_hall::fsmactions::messageinvocation_isTopDown_setter(instance):
    original = instance.isTopDown
    instance.isTopDown = original
    assert instance.isTopDown == original

@given(instance=HALL::FSMActions::DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::DomainPropertyGet)

@given(instance=HALL::FSMActions::DomainPropertyGet_strategy)
def test_hall::fsmactions::domainpropertyget_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSMActions::DomainPropertyGet_strategy)
def test_hall::fsmactions::domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::FSMActions::Literal_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::literal_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::Literal)

@given(instance=HALL::FSMActions::Literal_strategy)
def test_hall::fsmactions::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=HALL::FSMActions::Literal_strategy)
def test_hall::fsmactions::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL::FSMActions::ActionExpression_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::actionexpression_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::ActionExpression)

@given(instance=FSMActions::ActionExpression_strategy)
@settings(max_examples=50)
def test_fsmactions::actionexpression_instantiation(instance):
    assert isinstance(instance, FSMActions::ActionExpression)

@given(instance=HALL::FSMActions::Action_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::action_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::Action)

@given(instance=FSMConditions::Let_strategy)
@settings(max_examples=50)
def test_fsmconditions::let_instantiation(instance):
    assert isinstance(instance, FSMConditions::Let)

@given(instance=FSMConditions::HALL::Data_strategy)
@settings(max_examples=50)
def test_fsmconditions::hall::data_instantiation(instance):
    assert isinstance(instance, FSMConditions::HALL::Data)

@given(instance=PreConditionExpression_strategy)
@settings(max_examples=50)
def test_preconditionexpression_instantiation(instance):
    assert isinstance(instance, PreConditionExpression)

@given(instance=HALL::FSMConditions::DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::DomainPropertyGet)

@given(instance=HALL::FSMConditions::DomainPropertyGet_strategy)
def test_hall::fsmconditions::domainpropertyget_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSMConditions::DomainPropertyGet_strategy)
def test_hall::fsmconditions::domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::FSMConditions::UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::UnaryOperator)

@given(instance=HALL::FSMConditions::UnaryOperator_strategy)
def test_hall::fsmconditions::unaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::FSMConditions::UnaryOperator_strategy)
def test_hall::fsmconditions::unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::FSMConditions::VarRef_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::varref_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::VarRef)

@given(instance=HALL::FSMConditions::GetState_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::getstate_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::GetState)

@given(instance=HALL::FSMConditions::BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::BinaryOperator)

@given(instance=HALL::FSMConditions::BinaryOperator_strategy)
def test_hall::fsmconditions::binaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::FSMConditions::BinaryOperator_strategy)
def test_hall::fsmconditions::binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::FSMConditions::GetData_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::getdata_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::GetData)

@given(instance=HALL::FSMConditions::Let_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::let_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::Let)

@given(instance=HALL::FSMConditions::Let_strategy)
def test_hall::fsmconditions::let_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSMConditions::Let_strategy)
def test_hall::fsmconditions::let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::FSMConditions::Literal_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::literal_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::Literal)

@given(instance=HALL::FSMConditions::Literal_strategy)
def test_hall::fsmconditions::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=HALL::FSMConditions::Literal_strategy)
def test_hall::fsmconditions::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL::FSMConditions::PreConditionExpression_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::preconditionexpression_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::PreConditionExpression)

@given(instance=FSMConditions::PreConditionExpression_strategy)
@settings(max_examples=50)
def test_fsmconditions::preconditionexpression_instantiation(instance):
    assert isinstance(instance, FSMConditions::PreConditionExpression)

@given(instance=HALL::FSMConditions::PreCondition_strategy)
@settings(max_examples=50)
def test_hall::fsmconditions::precondition_instantiation(instance):
    assert isinstance(instance, HALL::FSMConditions::PreCondition)

@given(instance=FSMInstructions::Let_strategy)
@settings(max_examples=50)
def test_fsminstructions::let_instantiation(instance):
    assert isinstance(instance, FSMInstructions::Let)

@given(instance=FSMInstructions::HALL::Data_strategy)
@settings(max_examples=50)
def test_fsminstructions::hall::data_instantiation(instance):
    assert isinstance(instance, FSMInstructions::HALL::Data)

@given(instance=TriggerExpression_strategy)
@settings(max_examples=50)
def test_triggerexpression_instantiation(instance):
    assert isinstance(instance, TriggerExpression)

@given(instance=HALL::Trigger::MessageNotification_strategy)
@settings(max_examples=50)
def test_hall::trigger::messagenotification_instantiation(instance):
    assert isinstance(instance, HALL::Trigger::MessageNotification)

@given(instance=HALL::Trigger::TriggerExpression_strategy)
@settings(max_examples=50)
def test_hall::trigger::triggerexpression_instantiation(instance):
    assert isinstance(instance, HALL::Trigger::TriggerExpression)

@given(instance=Trigger::TriggerExpression_strategy)
@settings(max_examples=50)
def test_trigger::triggerexpression_instantiation(instance):
    assert isinstance(instance, Trigger::TriggerExpression)

@given(instance=HALL::Trigger::Trigger_strategy)
@settings(max_examples=50)
def test_hall::trigger::trigger_instantiation(instance):
    assert isinstance(instance, HALL::Trigger::Trigger)

@given(instance=FSMInstructions::HALL::Component_strategy)
@settings(max_examples=50)
def test_fsminstructions::hall::component_instantiation(instance):
    assert isinstance(instance, FSMInstructions::HALL::Component)

@given(instance=PosConditionExpression_strategy)
@settings(max_examples=50)
def test_posconditionexpression_instantiation(instance):
    assert isinstance(instance, PosConditionExpression)

@given(instance=HALL::FSMInstructions::UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::UnaryOperator)

@given(instance=HALL::FSMInstructions::UnaryOperator_strategy)
def test_hall::fsminstructions::unaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::FSMInstructions::UnaryOperator_strategy)
def test_hall::fsminstructions::unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::FSMInstructions::Let_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::let_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::Let)

@given(instance=HALL::FSMInstructions::Let_strategy)
def test_hall::fsminstructions::let_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSMInstructions::Let_strategy)
def test_hall::fsminstructions::let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::FSMInstructions::GetState_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::getstate_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::GetState)

@given(instance=HALL::FSMInstructions::SetState_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::setstate_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::SetState)

@given(instance=HALL::FSMInstructions::VarRef_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::varref_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::VarRef)

@given(instance=HALL::FSMInstructions::BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::BinaryOperator)

@given(instance=HALL::FSMInstructions::BinaryOperator_strategy)
def test_hall::fsminstructions::binaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::FSMInstructions::BinaryOperator_strategy)
def test_hall::fsminstructions::binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::FSMInstructions::GetData_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::getdata_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::GetData)

@given(instance=HALL::FSMInstructions::GetData_strategy)
def test_hall::fsminstructions::getdata_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::FSMInstructions::GetData_strategy)
def test_hall::fsminstructions::getdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::FSMInstructions::SetData_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::setdata_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::SetData)

@given(instance=HALL::FSMInstructions::SetData_strategy)
def test_hall::fsminstructions::setdata_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::FSMInstructions::SetData_strategy)
def test_hall::fsminstructions::setdata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::FSMInstructions::DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::DomainPropertyGet)

@given(instance=HALL::FSMInstructions::DomainPropertyGet_strategy)
def test_hall::fsminstructions::domainpropertyget_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSMInstructions::DomainPropertyGet_strategy)
def test_hall::fsminstructions::domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::FSMInstructions::Literal_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::literal_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::Literal)

@given(instance=HALL::FSMInstructions::Literal_strategy)
def test_hall::fsminstructions::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=HALL::FSMInstructions::Literal_strategy)
def test_hall::fsminstructions::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL::FSMInstructions::PosConditionExpression_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::posconditionexpression_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::PosConditionExpression)

@given(instance=FSMInstructions::PosConditionExpression_strategy)
@settings(max_examples=50)
def test_fsminstructions::posconditionexpression_instantiation(instance):
    assert isinstance(instance, FSMInstructions::PosConditionExpression)

@given(instance=HALL::FSMInstructions::PosCondition_strategy)
@settings(max_examples=50)
def test_hall::fsminstructions::poscondition_instantiation(instance):
    assert isinstance(instance, HALL::FSMInstructions::PosCondition)

@given(instance=HALL::Trigger::DomainEventFired_strategy)
@settings(max_examples=50)
def test_hall::trigger::domaineventfired_instantiation(instance):
    assert isinstance(instance, HALL::Trigger::DomainEventFired)

@given(instance=HALL::Trigger::DomainEventFired_strategy)
def test_hall::trigger::domaineventfired_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Trigger::DomainEventFired_strategy)
def test_hall::trigger::domaineventfired_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=RegularState_strategy)
@settings(max_examples=50)
def test_regularstate_instantiation(instance):
    assert isinstance(instance, RegularState)

@given(instance=InitialState_strategy)
@settings(max_examples=50)
def test_initialstate_instantiation(instance):
    assert isinstance(instance, InitialState)

@given(instance=FSM::HALL::Component_strategy)
@settings(max_examples=50)
def test_fsm::hall::component_instantiation(instance):
    assert isinstance(instance, FSM::HALL::Component)

@given(instance=HALL::FSM::FSM_strategy)
@settings(max_examples=50)
def test_hall::fsm::fsm_instantiation(instance):
    assert isinstance(instance, HALL::FSM::FSM)

@given(instance=Transition_strategy)
@settings(max_examples=50)
def test_transition_instantiation(instance):
    assert isinstance(instance, Transition)

@given(instance=HALL::FSM::State_strategy)
@settings(max_examples=50)
def test_hall::fsm::state_instantiation(instance):
    assert isinstance(instance, HALL::FSM::State)

@given(instance=HALL::FSM::State_strategy)
def test_hall::fsm::state_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=HALL::FSM::State_strategy)
def test_hall::fsm::state_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=HALL::FSM::State_strategy)
def test_hall::fsm::state_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSM::State_strategy)
def test_hall::fsm::state_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Trigger::Trigger_strategy)
@settings(max_examples=50)
def test_trigger::trigger_instantiation(instance):
    assert isinstance(instance, Trigger::Trigger)

@given(instance=FSMActions::Action_strategy)
@settings(max_examples=50)
def test_fsmactions::action_instantiation(instance):
    assert isinstance(instance, FSMActions::Action)

@given(instance=FSMInstructions::PosCondition_strategy)
@settings(max_examples=50)
def test_fsminstructions::poscondition_instantiation(instance):
    assert isinstance(instance, FSMInstructions::PosCondition)

@given(instance=FSMConditions::PreCondition_strategy)
@settings(max_examples=50)
def test_fsmconditions::precondition_instantiation(instance):
    assert isinstance(instance, FSMConditions::PreCondition)

@given(instance=HALL::FSM::Transition_strategy)
@settings(max_examples=50)
def test_hall::fsm::transition_instantiation(instance):
    assert isinstance(instance, HALL::FSM::Transition)

@given(instance=HALL::FSM::Transition_strategy)
def test_hall::fsm::transition_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::FSM::Transition_strategy)
def test_hall::fsm::transition_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Actions::HALL::Component_strategy)
@settings(max_examples=50)
def test_actions::hall::component_instantiation(instance):
    assert isinstance(instance, Actions::HALL::Component)

@given(instance=Actions::Let_strategy)
@settings(max_examples=50)
def test_actions::let_instantiation(instance):
    assert isinstance(instance, Actions::Let)

@given(instance=ActionMessageExpression_strategy)
@settings(max_examples=50)
def test_actionmessageexpression_instantiation(instance):
    assert isinstance(instance, ActionMessageExpression)

@given(instance=HALL::Actions::UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall::actions::unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::Actions::UnaryOperator)

@given(instance=HALL::Actions::UnaryOperator_strategy)
def test_hall::actions::unaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::Actions::UnaryOperator_strategy)
def test_hall::actions::unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::Actions::GetMessageParameter_strategy)
@settings(max_examples=50)
def test_hall::actions::getmessageparameter_instantiation(instance):
    assert isinstance(instance, HALL::Actions::GetMessageParameter)

@given(instance=HALL::Actions::GetMessageParameter_strategy)
def test_hall::actions::getmessageparameter_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::Actions::GetMessageParameter_strategy)
def test_hall::actions::getmessageparameter_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::FSMActions::Enable_strategy)
@settings(max_examples=50)
def test_hall::fsmactions::enable_instantiation(instance):
    assert isinstance(instance, HALL::FSMActions::Enable)

@given(instance=HALL::Actions::DomainPropertySet_strategy)
@settings(max_examples=50)
def test_hall::actions::domainpropertyset_instantiation(instance):
    assert isinstance(instance, HALL::Actions::DomainPropertySet)

@given(instance=HALL::Actions::DomainPropertySet_strategy)
def test_hall::actions::domainpropertyset_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Actions::DomainPropertySet_strategy)
def test_hall::actions::domainpropertyset_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Actions::Enable_strategy)
@settings(max_examples=50)
def test_hall::actions::enable_instantiation(instance):
    assert isinstance(instance, HALL::Actions::Enable)

@given(instance=HALL::Actions::MessageInvocation_strategy)
@settings(max_examples=50)
def test_hall::actions::messageinvocation_instantiation(instance):
    assert isinstance(instance, HALL::Actions::MessageInvocation)

@given(instance=HALL::Actions::MessageInvocation_strategy)
def test_hall::actions::messageinvocation_isTopDown_type(instance):
    assert isinstance(instance.isTopDown, bool)


@given(instance=HALL::Actions::MessageInvocation_strategy)
def test_hall::actions::messageinvocation_isTopDown_setter(instance):
    original = instance.isTopDown
    instance.isTopDown = original
    assert instance.isTopDown == original

@given(instance=HALL::Actions::GetMessageData_strategy)
@settings(max_examples=50)
def test_hall::actions::getmessagedata_instantiation(instance):
    assert isinstance(instance, HALL::Actions::GetMessageData)

@given(instance=HALL::Actions::GetMessageData_strategy)
def test_hall::actions::getmessagedata_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::Actions::GetMessageData_strategy)
def test_hall::actions::getmessagedata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::Actions::BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall::actions::binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::Actions::BinaryOperator)

@given(instance=HALL::Actions::BinaryOperator_strategy)
def test_hall::actions::binaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::Actions::BinaryOperator_strategy)
def test_hall::actions::binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::Actions::Literal_strategy)
@settings(max_examples=50)
def test_hall::actions::literal_instantiation(instance):
    assert isinstance(instance, HALL::Actions::Literal)

@given(instance=HALL::Actions::Literal_strategy)
def test_hall::actions::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=HALL::Actions::Literal_strategy)
def test_hall::actions::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL::Actions::Let_strategy)
@settings(max_examples=50)
def test_hall::actions::let_instantiation(instance):
    assert isinstance(instance, HALL::Actions::Let)

@given(instance=HALL::Actions::DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall::actions::domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL::Actions::DomainPropertyGet)

@given(instance=HALL::Actions::DomainPropertyGet_strategy)
def test_hall::actions::domainpropertyget_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Actions::DomainPropertyGet_strategy)
def test_hall::actions::domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Actions::GetData_strategy)
@settings(max_examples=50)
def test_hall::actions::getdata_instantiation(instance):
    assert isinstance(instance, HALL::Actions::GetData)

@given(instance=HALL::Actions::VarRef_strategy)
@settings(max_examples=50)
def test_hall::actions::varref_instantiation(instance):
    assert isinstance(instance, HALL::Actions::VarRef)

@given(instance=HALL::Actions::ActionMessageExpression_strategy)
@settings(max_examples=50)
def test_hall::actions::actionmessageexpression_instantiation(instance):
    assert isinstance(instance, HALL::Actions::ActionMessageExpression)

@given(instance=Actions::ActionMessageExpression_strategy)
@settings(max_examples=50)
def test_actions::actionmessageexpression_instantiation(instance):
    assert isinstance(instance, Actions::ActionMessageExpression)

@given(instance=HALL::Actions::ActionMessage_strategy)
@settings(max_examples=50)
def test_hall::actions::actionmessage_instantiation(instance):
    assert isinstance(instance, HALL::Actions::ActionMessage)

@given(instance=Conditions::Let_strategy)
@settings(max_examples=50)
def test_conditions::let_instantiation(instance):
    assert isinstance(instance, Conditions::Let)

@given(instance=Conditions::HALL::Data_strategy)
@settings(max_examples=50)
def test_conditions::hall::data_instantiation(instance):
    assert isinstance(instance, Conditions::HALL::Data)

@given(instance=Conditions::HALL::Component_strategy)
@settings(max_examples=50)
def test_conditions::hall::component_instantiation(instance):
    assert isinstance(instance, Conditions::HALL::Component)

@given(instance=PreConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_preconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, PreConditionMessageExpression)

@given(instance=HALL::Conditions::GetMessageData_strategy)
@settings(max_examples=50)
def test_hall::conditions::getmessagedata_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::GetMessageData)

@given(instance=HALL::Conditions::GetMessageData_strategy)
def test_hall::conditions::getmessagedata_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::Conditions::GetMessageData_strategy)
def test_hall::conditions::getmessagedata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::Conditions::GetState_strategy)
@settings(max_examples=50)
def test_hall::conditions::getstate_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::GetState)

@given(instance=HALL::Conditions::UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall::conditions::unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::UnaryOperator)

@given(instance=HALL::Conditions::UnaryOperator_strategy)
def test_hall::conditions::unaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::Conditions::UnaryOperator_strategy)
def test_hall::conditions::unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::Conditions::GetData_strategy)
@settings(max_examples=50)
def test_hall::conditions::getdata_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::GetData)

@given(instance=HALL::Conditions::VarRef_strategy)
@settings(max_examples=50)
def test_hall::conditions::varref_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::VarRef)

@given(instance=HALL::Conditions::Let_strategy)
@settings(max_examples=50)
def test_hall::conditions::let_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::Let)

@given(instance=HALL::Conditions::Let_strategy)
def test_hall::conditions::let_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Conditions::Let_strategy)
def test_hall::conditions::let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Conditions::GetMessageParameter_strategy)
@settings(max_examples=50)
def test_hall::conditions::getmessageparameter_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::GetMessageParameter)

@given(instance=HALL::Conditions::GetMessageParameter_strategy)
def test_hall::conditions::getmessageparameter_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::Conditions::GetMessageParameter_strategy)
def test_hall::conditions::getmessageparameter_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::Conditions::DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall::conditions::domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::DomainPropertyGet)

@given(instance=HALL::Conditions::DomainPropertyGet_strategy)
def test_hall::conditions::domainpropertyget_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Conditions::DomainPropertyGet_strategy)
def test_hall::conditions::domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Conditions::BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall::conditions::binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::BinaryOperator)

@given(instance=HALL::Conditions::BinaryOperator_strategy)
def test_hall::conditions::binaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::Conditions::BinaryOperator_strategy)
def test_hall::conditions::binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::Conditions::Literal_strategy)
@settings(max_examples=50)
def test_hall::conditions::literal_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::Literal)

@given(instance=HALL::Conditions::Literal_strategy)
def test_hall::conditions::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=HALL::Conditions::Literal_strategy)
def test_hall::conditions::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL::Conditions::PreConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_hall::conditions::preconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::PreConditionMessageExpression)

@given(instance=Conditions::PreConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_conditions::preconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, Conditions::PreConditionMessageExpression)

@given(instance=HALL::Conditions::PreConditionMessage_strategy)
@settings(max_examples=50)
def test_hall::conditions::preconditionmessage_instantiation(instance):
    assert isinstance(instance, HALL::Conditions::PreConditionMessage)

@given(instance=Instructions::Let_strategy)
@settings(max_examples=50)
def test_instructions::let_instantiation(instance):
    assert isinstance(instance, Instructions::Let)

@given(instance=Instructions::HALL::Component_strategy)
@settings(max_examples=50)
def test_instructions::hall::component_instantiation(instance):
    assert isinstance(instance, Instructions::HALL::Component)

@given(instance=Instructions::HALL::Data_strategy)
@settings(max_examples=50)
def test_instructions::hall::data_instantiation(instance):
    assert isinstance(instance, Instructions::HALL::Data)

@given(instance=State_strategy)
@settings(max_examples=50)
def test_state_instantiation(instance):
    assert isinstance(instance, State)

@given(instance=HALL::FSM::RegularState_strategy)
@settings(max_examples=50)
def test_hall::fsm::regularstate_instantiation(instance):
    assert isinstance(instance, HALL::FSM::RegularState)

@given(instance=HALL::FSM::InitialState_strategy)
@settings(max_examples=50)
def test_hall::fsm::initialstate_instantiation(instance):
    assert isinstance(instance, HALL::FSM::InitialState)

@given(instance=RegularMessageState_strategy)
@settings(max_examples=50)
def test_regularmessagestate_instantiation(instance):
    assert isinstance(instance, RegularMessageState)

@given(instance=HALL::Messages::MessageHandler_strategy)
@settings(max_examples=50)
def test_hall::messages::messagehandler_instantiation(instance):
    assert isinstance(instance, HALL::Messages::MessageHandler)

@given(instance=Messages::HALL::Data_strategy)
@settings(max_examples=50)
def test_messages::hall::data_instantiation(instance):
    assert isinstance(instance, Messages::HALL::Data)

@given(instance=PosConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_posconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, PosConditionMessageExpression)

@given(instance=HALL::Instructions::SetTopDown_strategy)
@settings(max_examples=50)
def test_hall::instructions::settopdown_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::SetTopDown)

@given(instance=HALL::Instructions::UnaryOperator_strategy)
@settings(max_examples=50)
def test_hall::instructions::unaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::UnaryOperator)

@given(instance=HALL::Instructions::UnaryOperator_strategy)
def test_hall::instructions::unaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::Instructions::UnaryOperator_strategy)
def test_hall::instructions::unaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::Instructions::GetData_strategy)
@settings(max_examples=50)
def test_hall::instructions::getdata_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::GetData)

@given(instance=HALL::Instructions::GetMessageData_strategy)
@settings(max_examples=50)
def test_hall::instructions::getmessagedata_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::GetMessageData)

@given(instance=HALL::Instructions::GetMessageData_strategy)
def test_hall::instructions::getmessagedata_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::Instructions::GetMessageData_strategy)
def test_hall::instructions::getmessagedata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::Instructions::VarRef_strategy)
@settings(max_examples=50)
def test_hall::instructions::varref_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::VarRef)

@given(instance=HALL::Instructions::DomainPropertyGet_strategy)
@settings(max_examples=50)
def test_hall::instructions::domainpropertyget_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::DomainPropertyGet)

@given(instance=HALL::Instructions::DomainPropertyGet_strategy)
def test_hall::instructions::domainpropertyget_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Instructions::DomainPropertyGet_strategy)
def test_hall::instructions::domainpropertyget_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Instructions::Let_strategy)
@settings(max_examples=50)
def test_hall::instructions::let_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::Let)

@given(instance=HALL::Instructions::Let_strategy)
def test_hall::instructions::let_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Instructions::Let_strategy)
def test_hall::instructions::let_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=HALL::Instructions::SetMessageParameter_strategy)
@settings(max_examples=50)
def test_hall::instructions::setmessageparameter_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::SetMessageParameter)

@given(instance=HALL::Instructions::SetMessageParameter_strategy)
def test_hall::instructions::setmessageparameter_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::Instructions::SetMessageParameter_strategy)
def test_hall::instructions::setmessageparameter_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::Instructions::SetMessageData_strategy)
@settings(max_examples=50)
def test_hall::instructions::setmessagedata_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::SetMessageData)

@given(instance=HALL::Instructions::SetMessageData_strategy)
def test_hall::instructions::setmessagedata_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::Instructions::SetMessageData_strategy)
def test_hall::instructions::setmessagedata_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::Instructions::SetState_strategy)
@settings(max_examples=50)
def test_hall::instructions::setstate_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::SetState)

@given(instance=HALL::Instructions::GetMessageParameter_strategy)
@settings(max_examples=50)
def test_hall::instructions::getmessageparameter_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::GetMessageParameter)

@given(instance=HALL::Instructions::GetMessageParameter_strategy)
def test_hall::instructions::getmessageparameter_field_type(instance):
    assert isinstance(instance.field, str)


@given(instance=HALL::Instructions::GetMessageParameter_strategy)
def test_hall::instructions::getmessageparameter_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original

@given(instance=HALL::Instructions::SetData_strategy)
@settings(max_examples=50)
def test_hall::instructions::setdata_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::SetData)

@given(instance=HALL::Instructions::GetState_strategy)
@settings(max_examples=50)
def test_hall::instructions::getstate_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::GetState)

@given(instance=HALL::Instructions::BinaryOperator_strategy)
@settings(max_examples=50)
def test_hall::instructions::binaryoperator_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::BinaryOperator)

@given(instance=HALL::Instructions::BinaryOperator_strategy)
def test_hall::instructions::binaryoperator_operatorname_type(instance):
    assert isinstance(instance.operatorname, str)


@given(instance=HALL::Instructions::BinaryOperator_strategy)
def test_hall::instructions::binaryoperator_operatorname_setter(instance):
    original = instance.operatorname
    instance.operatorname = original
    assert instance.operatorname == original

@given(instance=HALL::Instructions::Literal_strategy)
@settings(max_examples=50)
def test_hall::instructions::literal_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::Literal)

@given(instance=HALL::Instructions::Literal_strategy)
def test_hall::instructions::literal_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=HALL::Instructions::Literal_strategy)
def test_hall::instructions::literal_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=HALL::Instructions::PosConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_hall::instructions::posconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::PosConditionMessageExpression)

@given(instance=Instructions::PosConditionMessageExpression_strategy)
@settings(max_examples=50)
def test_instructions::posconditionmessageexpression_instantiation(instance):
    assert isinstance(instance, Instructions::PosConditionMessageExpression)

@given(instance=HALL::Instructions::PosConditionMessage_strategy)
@settings(max_examples=50)
def test_hall::instructions::posconditionmessage_instantiation(instance):
    assert isinstance(instance, HALL::Instructions::PosConditionMessage)

@given(instance=HALL::Messages::InitialMessageState_strategy)
@settings(max_examples=50)
def test_hall::messages::initialmessagestate_instantiation(instance):
    assert isinstance(instance, HALL::Messages::InitialMessageState)

@given(instance=MessageTransition_strategy)
@settings(max_examples=50)
def test_messagetransition_instantiation(instance):
    assert isinstance(instance, MessageTransition)

@given(instance=HALL::Messages::MessageState_strategy)
@settings(max_examples=50)
def test_hall::messages::messagestate_instantiation(instance):
    assert isinstance(instance, HALL::Messages::MessageState)

@given(instance=HALL::Messages::MessageState_strategy)
def test_hall::messages::messagestate_isContinue_type(instance):
    assert isinstance(instance.isContinue, bool)


@given(instance=HALL::Messages::MessageState_strategy)
def test_hall::messages::messagestate_isContinue_setter(instance):
    original = instance.isContinue
    instance.isContinue = original
    assert instance.isContinue == original

@given(instance=HALL::Messages::MessageState_strategy)
def test_hall::messages::messagestate_isActive_type(instance):
    assert isinstance(instance.isActive, bool)


@given(instance=HALL::Messages::MessageState_strategy)
def test_hall::messages::messagestate_isActive_setter(instance):
    original = instance.isActive
    instance.isActive = original
    assert instance.isActive == original

@given(instance=HALL::Messages::MessageState_strategy)
def test_hall::messages::messagestate_isEnd_type(instance):
    assert isinstance(instance.isEnd, bool)


@given(instance=HALL::Messages::MessageState_strategy)
def test_hall::messages::messagestate_isEnd_setter(instance):
    original = instance.isEnd
    instance.isEnd = original
    assert instance.isEnd == original

@given(instance=HALL::Messages::MessageState_strategy)
def test_hall::messages::messagestate_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=HALL::Messages::MessageState_strategy)
def test_hall::messages::messagestate_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Messages::HALL::Component_strategy)
@settings(max_examples=50)
def test_messages::hall::component_instantiation(instance):
    assert isinstance(instance, Messages::HALL::Component)

@given(instance=InitialMessageState_strategy)
@settings(max_examples=50)
def test_initialmessagestate_instantiation(instance):
    assert isinstance(instance, InitialMessageState)

@given(instance=Point_strategy)
@settings(max_examples=50)
def test_point_instantiation(instance):
    assert isinstance(instance, Point)

@given(instance=HALL::Geometry::Point2D_strategy)
@settings(max_examples=50)
def test_hall::geometry::point2d_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::Point2D)

@given(instance=HALL::Geometry::Point3D_strategy)
@settings(max_examples=50)
def test_hall::geometry::point3d_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::Point3D)

@given(instance=HALL::Geometry::Point3D_strategy)
def test_hall::geometry::point3d_zCoord_type(instance):
    assert isinstance(instance.zCoord, int)


@given(instance=HALL::Geometry::Point3D_strategy)
def test_hall::geometry::point3d_zCoord_setter(instance):
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

@given(instance=HALL::Geometry::Face_strategy)
@settings(max_examples=50)
def test_hall::geometry::face_instantiation(instance):
    assert isinstance(instance, HALL::Geometry::Face)

@given(instance=HALL::Geometry::Face_strategy)
def test_hall::geometry::face_labelText_type(instance):
    assert isinstance(instance.labelText, str)


@given(instance=HALL::Geometry::Face_strategy)
def test_hall::geometry::face_labelText_setter(instance):
    original = instance.labelText
    instance.labelText = original
    assert instance.labelText == original
