import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    SupportOperation,
    aredsl::ArrangeElements,
    aredsl::Exit,
    aredsl::ShowSystemMenu,
    aredsl::MoveElement,
    Action,
    aredsl::VoiceAction,
    aredsl::GestureAction,
    aredsl::SensorBasedAction,
    TrackerAction,
    aredsl::MarkerLessTrackerAction,
    aredsl::MarkerBasedTrackerAction,
    aredsl::TactileAction,
    aredsl::MentalAction,
    Behaviour,
    aredsl::SupportOperation,
    aredsl::DomainOperation,
    DomainOperation,
    aredsl::RemoveOperation,
    aredsl::SetOperation,
    aredsl::UnsetOperation,
    aredsl::CreateInstanceOperation,
    aredsl::Action,
    aredsl::ChangeContextOperation,
    aredsl::Behaviour,
    aredsl::Tool,
    aredsl::EdgeStyle,
    aredsl::LabelStyle,
    aredsl::Label,
    aredsl::NodeStyle,
    NodeStyle,
    aredsl::GeometricShapeNodeStyle,
    aredsl::Image2DNodeStyle,
    aredsl::Model3DNodeStyle,
    aredsl::ToolSet,
    aredsl::Layer,
    aredsl::Editor,
    aredsl::TrackerAction,
    aredsl::Edge,
    aredsl::Node,
    ContainmentKind,
    IntegrityRestrictionKind,
    ShapeKind,
    QueryLanguageKind,
    LineKind,
    OutlineKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_supportoperation_is_not_abstract():
    assert not inspect.isabstract(SupportOperation)


def test_supportoperation_constructor_exists():
    assert callable(SupportOperation.__init__)


def test_supportoperation_constructor_args():
    sig = inspect.signature(SupportOperation.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::arrangeelements_is_not_abstract():
    assert not inspect.isabstract(aredsl::ArrangeElements)


def test_aredsl::arrangeelements_constructor_exists():
    assert callable(aredsl::ArrangeElements.__init__)


def test_aredsl::arrangeelements_constructor_args():
    sig = inspect.signature(aredsl::ArrangeElements.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::exit_is_not_abstract():
    assert not inspect.isabstract(aredsl::Exit)


def test_aredsl::exit_constructor_exists():
    assert callable(aredsl::Exit.__init__)


def test_aredsl::exit_constructor_args():
    sig = inspect.signature(aredsl::Exit.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::showsystemmenu_is_not_abstract():
    assert not inspect.isabstract(aredsl::ShowSystemMenu)


def test_aredsl::showsystemmenu_constructor_exists():
    assert callable(aredsl::ShowSystemMenu.__init__)


def test_aredsl::showsystemmenu_constructor_args():
    sig = inspect.signature(aredsl::ShowSystemMenu.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::moveelement_is_not_abstract():
    assert not inspect.isabstract(aredsl::MoveElement)


def test_aredsl::moveelement_constructor_exists():
    assert callable(aredsl::MoveElement.__init__)


def test_aredsl::moveelement_constructor_args():
    sig = inspect.signature(aredsl::MoveElement.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::voiceaction_is_not_abstract():
    assert not inspect.isabstract(aredsl::VoiceAction)


def test_aredsl::voiceaction_constructor_exists():
    assert callable(aredsl::VoiceAction.__init__)


def test_aredsl::voiceaction_constructor_args():
    sig = inspect.signature(aredsl::VoiceAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::gestureaction_is_not_abstract():
    assert not inspect.isabstract(aredsl::GestureAction)


def test_aredsl::gestureaction_constructor_exists():
    assert callable(aredsl::GestureAction.__init__)


def test_aredsl::gestureaction_constructor_args():
    sig = inspect.signature(aredsl::GestureAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::sensorbasedaction_is_not_abstract():
    assert not inspect.isabstract(aredsl::SensorBasedAction)


def test_aredsl::sensorbasedaction_constructor_exists():
    assert callable(aredsl::SensorBasedAction.__init__)


def test_aredsl::sensorbasedaction_constructor_args():
    sig = inspect.signature(aredsl::SensorBasedAction.__init__)
    params = list(sig.parameters.keys())



def test_trackeraction_is_not_abstract():
    assert not inspect.isabstract(TrackerAction)


def test_trackeraction_constructor_exists():
    assert callable(TrackerAction.__init__)


def test_trackeraction_constructor_args():
    sig = inspect.signature(TrackerAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::markerlesstrackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl::MarkerLessTrackerAction)


def test_aredsl::markerlesstrackeraction_constructor_exists():
    assert callable(aredsl::MarkerLessTrackerAction.__init__)


def test_aredsl::markerlesstrackeraction_constructor_args():
    sig = inspect.signature(aredsl::MarkerLessTrackerAction.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_aredsl::markerlesstrackeraction_has_file():
    assert hasattr(aredsl::MarkerLessTrackerAction, "file")
    descriptor = None
    for klass in aredsl::MarkerLessTrackerAction.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::markerbasedtrackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl::MarkerBasedTrackerAction)


def test_aredsl::markerbasedtrackeraction_constructor_exists():
    assert callable(aredsl::MarkerBasedTrackerAction.__init__)


def test_aredsl::markerbasedtrackeraction_constructor_args():
    sig = inspect.signature(aredsl::MarkerBasedTrackerAction.__init__)
    params = list(sig.parameters.keys())
    assert "markerId" in params, "Missing parameter 'markerId'"

def test_aredsl::markerbasedtrackeraction_has_markerId():
    assert hasattr(aredsl::MarkerBasedTrackerAction, "markerId")
    descriptor = None
    for klass in aredsl::MarkerBasedTrackerAction.__mro__:
        if "markerId" in klass.__dict__:
            descriptor = klass.__dict__["markerId"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::tactileaction_is_not_abstract():
    assert not inspect.isabstract(aredsl::TactileAction)


def test_aredsl::tactileaction_constructor_exists():
    assert callable(aredsl::TactileAction.__init__)


def test_aredsl::tactileaction_constructor_args():
    sig = inspect.signature(aredsl::TactileAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::mentalaction_is_not_abstract():
    assert not inspect.isabstract(aredsl::MentalAction)


def test_aredsl::mentalaction_constructor_exists():
    assert callable(aredsl::MentalAction.__init__)


def test_aredsl::mentalaction_constructor_args():
    sig = inspect.signature(aredsl::MentalAction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_is_not_abstract():
    assert not inspect.isabstract(Behaviour)


def test_behaviour_constructor_exists():
    assert callable(Behaviour.__init__)


def test_behaviour_constructor_args():
    sig = inspect.signature(Behaviour.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::supportoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl::SupportOperation)


def test_aredsl::supportoperation_constructor_exists():
    assert callable(aredsl::SupportOperation.__init__)


def test_aredsl::supportoperation_constructor_args():
    sig = inspect.signature(aredsl::SupportOperation.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::domainoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl::DomainOperation)


def test_aredsl::domainoperation_constructor_exists():
    assert callable(aredsl::DomainOperation.__init__)


def test_aredsl::domainoperation_constructor_args():
    sig = inspect.signature(aredsl::DomainOperation.__init__)
    params = list(sig.parameters.keys())



def test_domainoperation_is_not_abstract():
    assert not inspect.isabstract(DomainOperation)


def test_domainoperation_constructor_exists():
    assert callable(DomainOperation.__init__)


def test_domainoperation_constructor_args():
    sig = inspect.signature(DomainOperation.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::removeoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl::RemoveOperation)


def test_aredsl::removeoperation_constructor_exists():
    assert callable(aredsl::RemoveOperation.__init__)


def test_aredsl::removeoperation_constructor_args():
    sig = inspect.signature(aredsl::RemoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_aredsl::removeoperation_has_constraint():
    assert hasattr(aredsl::RemoveOperation, "constraint")
    descriptor = None
    for klass in aredsl::RemoveOperation.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::setoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl::SetOperation)


def test_aredsl::setoperation_constructor_exists():
    assert callable(aredsl::SetOperation.__init__)


def test_aredsl::setoperation_constructor_args():
    sig = inspect.signature(aredsl::SetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"
    assert "constraint" in params, "Missing parameter 'constraint'"
    assert "value" in params, "Missing parameter 'value'"

def test_aredsl::setoperation_has_feature():
    assert hasattr(aredsl::SetOperation, "feature")
    descriptor = None
    for klass in aredsl::SetOperation.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::setoperation_has_constraint():
    assert hasattr(aredsl::SetOperation, "constraint")
    descriptor = None
    for klass in aredsl::SetOperation.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::setoperation_has_value():
    assert hasattr(aredsl::SetOperation, "value")
    descriptor = None
    for klass in aredsl::SetOperation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::unsetoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl::UnsetOperation)


def test_aredsl::unsetoperation_constructor_exists():
    assert callable(aredsl::UnsetOperation.__init__)


def test_aredsl::unsetoperation_constructor_args():
    sig = inspect.signature(aredsl::UnsetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"
    assert "feature" in params, "Missing parameter 'feature'"

def test_aredsl::unsetoperation_has_constraint():
    assert hasattr(aredsl::UnsetOperation, "constraint")
    descriptor = None
    for klass in aredsl::UnsetOperation.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::unsetoperation_has_feature():
    assert hasattr(aredsl::UnsetOperation, "feature")
    descriptor = None
    for klass in aredsl::UnsetOperation.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::createinstanceoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl::CreateInstanceOperation)


def test_aredsl::createinstanceoperation_constructor_exists():
    assert callable(aredsl::CreateInstanceOperation.__init__)


def test_aredsl::createinstanceoperation_constructor_args():
    sig = inspect.signature(aredsl::CreateInstanceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "feature" in params, "Missing parameter 'feature'"
    assert "name" in params, "Missing parameter 'name'"

def test_aredsl::createinstanceoperation_has_type():
    assert hasattr(aredsl::CreateInstanceOperation, "type")
    descriptor = None
    for klass in aredsl::CreateInstanceOperation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::createinstanceoperation_has_feature():
    assert hasattr(aredsl::CreateInstanceOperation, "feature")
    descriptor = None
    for klass in aredsl::CreateInstanceOperation.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::createinstanceoperation_has_name():
    assert hasattr(aredsl::CreateInstanceOperation, "name")
    descriptor = None
    for klass in aredsl::CreateInstanceOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::action_is_not_abstract():
    assert not inspect.isabstract(aredsl::Action)


def test_aredsl::action_constructor_exists():
    assert callable(aredsl::Action.__init__)


def test_aredsl::action_constructor_args():
    sig = inspect.signature(aredsl::Action.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_aredsl::action_has_description():
    assert hasattr(aredsl::Action, "description")
    descriptor = None
    for klass in aredsl::Action.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::changecontextoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl::ChangeContextOperation)


def test_aredsl::changecontextoperation_constructor_exists():
    assert callable(aredsl::ChangeContextOperation.__init__)


def test_aredsl::changecontextoperation_constructor_args():
    sig = inspect.signature(aredsl::ChangeContextOperation.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_aredsl::changecontextoperation_has_expression():
    assert hasattr(aredsl::ChangeContextOperation, "expression")
    descriptor = None
    for klass in aredsl::ChangeContextOperation.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::behaviour_is_not_abstract():
    assert not inspect.isabstract(aredsl::Behaviour)


def test_aredsl::behaviour_constructor_exists():
    assert callable(aredsl::Behaviour.__init__)


def test_aredsl::behaviour_constructor_args():
    sig = inspect.signature(aredsl::Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_aredsl::behaviour_has_description():
    assert hasattr(aredsl::Behaviour, "description")
    descriptor = None
    for klass in aredsl::Behaviour.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::tool_is_not_abstract():
    assert not inspect.isabstract(aredsl::Tool)


def test_aredsl::tool_constructor_exists():
    assert callable(aredsl::Tool.__init__)


def test_aredsl::tool_constructor_args():
    sig = inspect.signature(aredsl::Tool.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "targetPrecondition" in params, "Missing parameter 'targetPrecondition'"
    assert "id" in params, "Missing parameter 'id'"

def test_aredsl::tool_has_description():
    assert hasattr(aredsl::Tool, "description")
    descriptor = None
    for klass in aredsl::Tool.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::tool_has_precondition():
    assert hasattr(aredsl::Tool, "precondition")
    descriptor = None
    for klass in aredsl::Tool.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::tool_has_targetPrecondition():
    assert hasattr(aredsl::Tool, "targetPrecondition")
    descriptor = None
    for klass in aredsl::Tool.__mro__:
        if "targetPrecondition" in klass.__dict__:
            descriptor = klass.__dict__["targetPrecondition"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::tool_has_id():
    assert hasattr(aredsl::Tool, "id")
    descriptor = None
    for klass in aredsl::Tool.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::edgestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl::EdgeStyle)


def test_aredsl::edgestyle_constructor_exists():
    assert callable(aredsl::EdgeStyle.__init__)


def test_aredsl::edgestyle_constructor_args():
    sig = inspect.signature(aredsl::EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"
    assert "color" in params, "Missing parameter 'color'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "width" in params, "Missing parameter 'width'"

def test_aredsl::edgestyle_has_semanticCondition():
    assert hasattr(aredsl::EdgeStyle, "semanticCondition")
    descriptor = None
    for klass in aredsl::EdgeStyle.__mro__:
        if "semanticCondition" in klass.__dict__:
            descriptor = klass.__dict__["semanticCondition"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::edgestyle_has_color():
    assert hasattr(aredsl::EdgeStyle, "color")
    descriptor = None
    for klass in aredsl::EdgeStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::edgestyle_has_kind():
    assert hasattr(aredsl::EdgeStyle, "kind")
    descriptor = None
    for klass in aredsl::EdgeStyle.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::edgestyle_has_width():
    assert hasattr(aredsl::EdgeStyle, "width")
    descriptor = None
    for klass in aredsl::EdgeStyle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::labelstyle_is_not_abstract():
    assert not inspect.isabstract(aredsl::LabelStyle)


def test_aredsl::labelstyle_constructor_exists():
    assert callable(aredsl::LabelStyle.__init__)


def test_aredsl::labelstyle_constructor_args():
    sig = inspect.signature(aredsl::LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "color" in params, "Missing parameter 'color'"
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"

def test_aredsl::labelstyle_has_height():
    assert hasattr(aredsl::LabelStyle, "height")
    descriptor = None
    for klass in aredsl::LabelStyle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::labelstyle_has_color():
    assert hasattr(aredsl::LabelStyle, "color")
    descriptor = None
    for klass in aredsl::LabelStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::labelstyle_has_semanticCondition():
    assert hasattr(aredsl::LabelStyle, "semanticCondition")
    descriptor = None
    for klass in aredsl::LabelStyle.__mro__:
        if "semanticCondition" in klass.__dict__:
            descriptor = klass.__dict__["semanticCondition"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::label_is_not_abstract():
    assert not inspect.isabstract(aredsl::Label)


def test_aredsl::label_constructor_exists():
    assert callable(aredsl::Label.__init__)


def test_aredsl::label_constructor_args():
    sig = inspect.signature(aredsl::Label.__init__)
    params = list(sig.parameters.keys())
    assert "semantics" in params, "Missing parameter 'semantics'"
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"

def test_aredsl::label_has_semantics():
    assert hasattr(aredsl::Label, "semantics")
    descriptor = None
    for klass in aredsl::Label.__mro__:
        if "semantics" in klass.__dict__:
            descriptor = klass.__dict__["semantics"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::label_has_id():
    assert hasattr(aredsl::Label, "id")
    descriptor = None
    for klass in aredsl::Label.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::label_has_description():
    assert hasattr(aredsl::Label, "description")
    descriptor = None
    for klass in aredsl::Label.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::nodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl::NodeStyle)


def test_aredsl::nodestyle_constructor_exists():
    assert callable(aredsl::NodeStyle.__init__)


def test_aredsl::nodestyle_constructor_args():
    sig = inspect.signature(aredsl::NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"
    assert "width" in params, "Missing parameter 'width'"

def test_aredsl::nodestyle_has_height():
    assert hasattr(aredsl::NodeStyle, "height")
    descriptor = None
    for klass in aredsl::NodeStyle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::nodestyle_has_semanticCondition():
    assert hasattr(aredsl::NodeStyle, "semanticCondition")
    descriptor = None
    for klass in aredsl::NodeStyle.__mro__:
        if "semanticCondition" in klass.__dict__:
            descriptor = klass.__dict__["semanticCondition"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::nodestyle_has_width():
    assert hasattr(aredsl::NodeStyle, "width")
    descriptor = None
    for klass in aredsl::NodeStyle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::geometricshapenodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl::GeometricShapeNodeStyle)


def test_aredsl::geometricshapenodestyle_constructor_exists():
    assert callable(aredsl::GeometricShapeNodeStyle.__init__)


def test_aredsl::geometricshapenodestyle_constructor_args():
    sig = inspect.signature(aredsl::GeometricShapeNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "outline" in params, "Missing parameter 'outline'"
    assert "color" in params, "Missing parameter 'color'"
    assert "kind" in params, "Missing parameter 'kind'"

def test_aredsl::geometricshapenodestyle_has_outline():
    assert hasattr(aredsl::GeometricShapeNodeStyle, "outline")
    descriptor = None
    for klass in aredsl::GeometricShapeNodeStyle.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::geometricshapenodestyle_has_color():
    assert hasattr(aredsl::GeometricShapeNodeStyle, "color")
    descriptor = None
    for klass in aredsl::GeometricShapeNodeStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::geometricshapenodestyle_has_kind():
    assert hasattr(aredsl::GeometricShapeNodeStyle, "kind")
    descriptor = None
    for klass in aredsl::GeometricShapeNodeStyle.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::image2dnodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl::Image2DNodeStyle)


def test_aredsl::image2dnodestyle_constructor_exists():
    assert callable(aredsl::Image2DNodeStyle.__init__)


def test_aredsl::image2dnodestyle_constructor_args():
    sig = inspect.signature(aredsl::Image2DNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_aredsl::image2dnodestyle_has_file():
    assert hasattr(aredsl::Image2DNodeStyle, "file")
    descriptor = None
    for klass in aredsl::Image2DNodeStyle.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::model3dnodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl::Model3DNodeStyle)


def test_aredsl::model3dnodestyle_constructor_exists():
    assert callable(aredsl::Model3DNodeStyle.__init__)


def test_aredsl::model3dnodestyle_constructor_args():
    sig = inspect.signature(aredsl::Model3DNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_aredsl::model3dnodestyle_has_file():
    assert hasattr(aredsl::Model3DNodeStyle, "file")
    descriptor = None
    for klass in aredsl::Model3DNodeStyle.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::toolset_is_not_abstract():
    assert not inspect.isabstract(aredsl::ToolSet)


def test_aredsl::toolset_constructor_exists():
    assert callable(aredsl::ToolSet.__init__)


def test_aredsl::toolset_constructor_args():
    sig = inspect.signature(aredsl::ToolSet.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "description" in params, "Missing parameter 'description'"

def test_aredsl::toolset_has_id():
    assert hasattr(aredsl::ToolSet, "id")
    descriptor = None
    for klass in aredsl::ToolSet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::toolset_has_description():
    assert hasattr(aredsl::ToolSet, "description")
    descriptor = None
    for klass in aredsl::ToolSet.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::layer_is_not_abstract():
    assert not inspect.isabstract(aredsl::Layer)


def test_aredsl::layer_constructor_exists():
    assert callable(aredsl::Layer.__init__)


def test_aredsl::layer_constructor_args():
    sig = inspect.signature(aredsl::Layer.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "semantics" in params, "Missing parameter 'semantics'"
    assert "description" in params, "Missing parameter 'description'"

def test_aredsl::layer_has_id():
    assert hasattr(aredsl::Layer, "id")
    descriptor = None
    for klass in aredsl::Layer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::layer_has_semantics():
    assert hasattr(aredsl::Layer, "semantics")
    descriptor = None
    for klass in aredsl::Layer.__mro__:
        if "semantics" in klass.__dict__:
            descriptor = klass.__dict__["semantics"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::layer_has_description():
    assert hasattr(aredsl::Layer, "description")
    descriptor = None
    for klass in aredsl::Layer.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::editor_is_not_abstract():
    assert not inspect.isabstract(aredsl::Editor)


def test_aredsl::editor_constructor_exists():
    assert callable(aredsl::Editor.__init__)


def test_aredsl::editor_constructor_args():
    sig = inspect.signature(aredsl::Editor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"
    assert "fileExtension" in params, "Missing parameter 'fileExtension'"
    assert "queryLanguageKind" in params, "Missing parameter 'queryLanguageKind'"

def test_aredsl::editor_has_name():
    assert hasattr(aredsl::Editor, "name")
    descriptor = None
    for klass in aredsl::Editor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::editor_has_description():
    assert hasattr(aredsl::Editor, "description")
    descriptor = None
    for klass in aredsl::Editor.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::editor_has_fileExtension():
    assert hasattr(aredsl::Editor, "fileExtension")
    descriptor = None
    for klass in aredsl::Editor.__mro__:
        if "fileExtension" in klass.__dict__:
            descriptor = klass.__dict__["fileExtension"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::editor_has_queryLanguageKind():
    assert hasattr(aredsl::Editor, "queryLanguageKind")
    descriptor = None
    for klass in aredsl::Editor.__mro__:
        if "queryLanguageKind" in klass.__dict__:
            descriptor = klass.__dict__["queryLanguageKind"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::trackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl::TrackerAction)


def test_aredsl::trackeraction_constructor_exists():
    assert callable(aredsl::TrackerAction.__init__)


def test_aredsl::trackeraction_constructor_args():
    sig = inspect.signature(aredsl::TrackerAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl::edge_is_not_abstract():
    assert not inspect.isabstract(aredsl::Edge)


def test_aredsl::edge_constructor_exists():
    assert callable(aredsl::Edge.__init__)


def test_aredsl::edge_constructor_args():
    sig = inspect.signature(aredsl::Edge.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "originSemantics" in params, "Missing parameter 'originSemantics'"
    assert "id" in params, "Missing parameter 'id'"
    assert "destinationSemantics" in params, "Missing parameter 'destinationSemantics'"

def test_aredsl::edge_has_description():
    assert hasattr(aredsl::Edge, "description")
    descriptor = None
    for klass in aredsl::Edge.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::edge_has_originSemantics():
    assert hasattr(aredsl::Edge, "originSemantics")
    descriptor = None
    for klass in aredsl::Edge.__mro__:
        if "originSemantics" in klass.__dict__:
            descriptor = klass.__dict__["originSemantics"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::edge_has_id():
    assert hasattr(aredsl::Edge, "id")
    descriptor = None
    for klass in aredsl::Edge.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::edge_has_destinationSemantics():
    assert hasattr(aredsl::Edge, "destinationSemantics")
    descriptor = None
    for klass in aredsl::Edge.__mro__:
        if "destinationSemantics" in klass.__dict__:
            descriptor = klass.__dict__["destinationSemantics"]
            break
    assert isinstance(descriptor, property)



def test_aredsl::node_is_not_abstract():
    assert not inspect.isabstract(aredsl::Node)


def test_aredsl::node_constructor_exists():
    assert callable(aredsl::Node.__init__)


def test_aredsl::node_constructor_args():
    sig = inspect.signature(aredsl::Node.__init__)
    params = list(sig.parameters.keys())
    assert "semantics" in params, "Missing parameter 'semantics'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "contaimentKind" in params, "Missing parameter 'contaimentKind'"

def test_aredsl::node_has_semantics():
    assert hasattr(aredsl::Node, "semantics")
    descriptor = None
    for klass in aredsl::Node.__mro__:
        if "semantics" in klass.__dict__:
            descriptor = klass.__dict__["semantics"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::node_has_description():
    assert hasattr(aredsl::Node, "description")
    descriptor = None
    for klass in aredsl::Node.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::node_has_id():
    assert hasattr(aredsl::Node, "id")
    descriptor = None
    for klass in aredsl::Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aredsl::node_has_contaimentKind():
    assert hasattr(aredsl::Node, "contaimentKind")
    descriptor = None
    for klass in aredsl::Node.__mro__:
        if "contaimentKind" in klass.__dict__:
            descriptor = klass.__dict__["contaimentKind"]
            break
    assert isinstance(descriptor, property)

def test_containmentkind_exists():
    # Check that the Enumeration exists
    assert ContainmentKind is not None

def test_containmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainmentKind]
    expected_literals = [
        "HORIZONTAL_ARRANGEMENT",
        "EXTERNAL_LINK",
        "VERTICAL_ARRANGEMENT",
        "FREE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainmentKind"

def test_integrityrestrictionkind_exists():
    # Check that the Enumeration exists
    assert IntegrityRestrictionKind is not None

def test_integrityrestrictionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in IntegrityRestrictionKind]
    expected_literals = [
        "NO_ACTION",
        "CASCADE",
        "SET_NULL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in IntegrityRestrictionKind"

def test_shapekind_exists():
    # Check that the Enumeration exists
    assert ShapeKind is not None

def test_shapekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShapeKind]
    expected_literals = [
        "RECTANGLE",
        "ELLIPSE",
        "CIRCLE",
        "TRIANGLE",
        "SQUARE",
        "DIAMOND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShapeKind"

def test_querylanguagekind_exists():
    # Check that the Enumeration exists
    assert QueryLanguageKind is not None

def test_querylanguagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueryLanguageKind]
    expected_literals = [
        "SQL",
        "OCL",
        "AQL",
        "JPQL",
        "LINQ",
        "XPATH_XQUERY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueryLanguageKind"

def test_linekind_exists():
    # Check that the Enumeration exists
    assert LineKind is not None

def test_linekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineKind]
    expected_literals = [
        "DASHED",
        "SOLID",
        "DOTTED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineKind"

def test_outlinekind_exists():
    # Check that the Enumeration exists
    assert OutlineKind is not None

def test_outlinekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OutlineKind]
    expected_literals = [
        "NONE",
        "DOUBLE",
        "SIMPLE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OutlineKind"


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
SupportOperation_strategy = st.builds(
    SupportOperation,
)
aredsl::ArrangeElements_strategy = st.builds(
    aredsl::ArrangeElements,
)
aredsl::Exit_strategy = st.builds(
    aredsl::Exit,
)
aredsl::ShowSystemMenu_strategy = st.builds(
    aredsl::ShowSystemMenu,
)
aredsl::MoveElement_strategy = st.builds(
    aredsl::MoveElement,
)
Action_strategy = st.builds(
    Action,
)
aredsl::VoiceAction_strategy = st.builds(
    aredsl::VoiceAction,
)
aredsl::GestureAction_strategy = st.builds(
    aredsl::GestureAction,
)
aredsl::SensorBasedAction_strategy = st.builds(
    aredsl::SensorBasedAction,
)
TrackerAction_strategy = st.builds(
    TrackerAction,
)
aredsl::MarkerLessTrackerAction_strategy = st.builds(
    aredsl::MarkerLessTrackerAction,
    file=
        safe_text
)
aredsl::MarkerBasedTrackerAction_strategy = st.builds(
    aredsl::MarkerBasedTrackerAction,
    markerId=
        st.integers()
)
aredsl::TactileAction_strategy = st.builds(
    aredsl::TactileAction,
)
aredsl::MentalAction_strategy = st.builds(
    aredsl::MentalAction,
)
Behaviour_strategy = st.builds(
    Behaviour,
)
aredsl::SupportOperation_strategy = st.builds(
    aredsl::SupportOperation,
)
aredsl::DomainOperation_strategy = st.builds(
    aredsl::DomainOperation,
)
DomainOperation_strategy = st.builds(
    DomainOperation,
)
aredsl::RemoveOperation_strategy = st.builds(
    aredsl::RemoveOperation,
    constraint=
        safe_text
)
aredsl::SetOperation_strategy = st.builds(
    aredsl::SetOperation,
    feature=
        safe_text,
    constraint=
        safe_text,
    value=
        safe_text
)
aredsl::UnsetOperation_strategy = st.builds(
    aredsl::UnsetOperation,
    constraint=
        safe_text,
    feature=
        safe_text
)
aredsl::CreateInstanceOperation_strategy = st.builds(
    aredsl::CreateInstanceOperation,
    type=
        safe_text,
    feature=
        safe_text,
    name=
        safe_text
)
aredsl::Action_strategy = st.builds(
    aredsl::Action,
    description=
        safe_text
)
aredsl::ChangeContextOperation_strategy = st.builds(
    aredsl::ChangeContextOperation,
    expression=
        safe_text
)
aredsl::Behaviour_strategy = st.builds(
    aredsl::Behaviour,
    description=
        safe_text
)
aredsl::Tool_strategy = st.builds(
    aredsl::Tool,
    description=
        safe_text,
    precondition=
        safe_text,
    targetPrecondition=
        safe_text,
    id=
        safe_text
)
aredsl::EdgeStyle_strategy = st.builds(
    aredsl::EdgeStyle,
    semanticCondition=
        safe_text,
    color=
        safe_text,
    kind=
        safe_text,
    width=
        st.integers()
)
aredsl::LabelStyle_strategy = st.builds(
    aredsl::LabelStyle,
    height=
        st.integers(),
    color=
        safe_text,
    semanticCondition=
        safe_text
)
aredsl::Label_strategy = st.builds(
    aredsl::Label,
    semantics=
        safe_text,
    id=
        safe_text,
    description=
        safe_text
)
aredsl::NodeStyle_strategy = st.builds(
    aredsl::NodeStyle,
    height=
        st.integers(),
    semanticCondition=
        safe_text,
    width=
        st.integers()
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
aredsl::GeometricShapeNodeStyle_strategy = st.builds(
    aredsl::GeometricShapeNodeStyle,
    outline=
        safe_text,
    color=
        safe_text,
    kind=
        safe_text
)
aredsl::Image2DNodeStyle_strategy = st.builds(
    aredsl::Image2DNodeStyle,
    file=
        safe_text
)
aredsl::Model3DNodeStyle_strategy = st.builds(
    aredsl::Model3DNodeStyle,
    file=
        safe_text
)
aredsl::ToolSet_strategy = st.builds(
    aredsl::ToolSet,
    id=
        safe_text,
    description=
        safe_text
)
aredsl::Layer_strategy = st.builds(
    aredsl::Layer,
    id=
        safe_text,
    semantics=
        safe_text,
    description=
        safe_text
)
aredsl::Editor_strategy = st.builds(
    aredsl::Editor,
    name=
        safe_text,
    description=
        safe_text,
    fileExtension=
        safe_text,
    queryLanguageKind=
        safe_text
)
aredsl::TrackerAction_strategy = st.builds(
    aredsl::TrackerAction,
)
aredsl::Edge_strategy = st.builds(
    aredsl::Edge,
    description=
        safe_text,
    originSemantics=
        safe_text,
    id=
        safe_text,
    destinationSemantics=
        safe_text
)
aredsl::Node_strategy = st.builds(
    aredsl::Node,
    semantics=
        safe_text,
    description=
        safe_text,
    id=
        safe_text,
    contaimentKind=
        safe_text
)

@given(instance=SupportOperation_strategy)
@settings(max_examples=50)
def test_supportoperation_instantiation(instance):
    assert isinstance(instance, SupportOperation)

@given(instance=aredsl::ArrangeElements_strategy)
@settings(max_examples=50)
def test_aredsl::arrangeelements_instantiation(instance):
    assert isinstance(instance, aredsl::ArrangeElements)

@given(instance=aredsl::Exit_strategy)
@settings(max_examples=50)
def test_aredsl::exit_instantiation(instance):
    assert isinstance(instance, aredsl::Exit)

@given(instance=aredsl::ShowSystemMenu_strategy)
@settings(max_examples=50)
def test_aredsl::showsystemmenu_instantiation(instance):
    assert isinstance(instance, aredsl::ShowSystemMenu)

@given(instance=aredsl::MoveElement_strategy)
@settings(max_examples=50)
def test_aredsl::moveelement_instantiation(instance):
    assert isinstance(instance, aredsl::MoveElement)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=aredsl::VoiceAction_strategy)
@settings(max_examples=50)
def test_aredsl::voiceaction_instantiation(instance):
    assert isinstance(instance, aredsl::VoiceAction)

@given(instance=aredsl::GestureAction_strategy)
@settings(max_examples=50)
def test_aredsl::gestureaction_instantiation(instance):
    assert isinstance(instance, aredsl::GestureAction)

@given(instance=aredsl::SensorBasedAction_strategy)
@settings(max_examples=50)
def test_aredsl::sensorbasedaction_instantiation(instance):
    assert isinstance(instance, aredsl::SensorBasedAction)

@given(instance=TrackerAction_strategy)
@settings(max_examples=50)
def test_trackeraction_instantiation(instance):
    assert isinstance(instance, TrackerAction)

@given(instance=aredsl::MarkerLessTrackerAction_strategy)
@settings(max_examples=50)
def test_aredsl::markerlesstrackeraction_instantiation(instance):
    assert isinstance(instance, aredsl::MarkerLessTrackerAction)

@given(instance=aredsl::MarkerLessTrackerAction_strategy)
def test_aredsl::markerlesstrackeraction_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=aredsl::MarkerLessTrackerAction_strategy)
def test_aredsl::markerlesstrackeraction_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=aredsl::MarkerBasedTrackerAction_strategy)
@settings(max_examples=50)
def test_aredsl::markerbasedtrackeraction_instantiation(instance):
    assert isinstance(instance, aredsl::MarkerBasedTrackerAction)

@given(instance=aredsl::MarkerBasedTrackerAction_strategy)
def test_aredsl::markerbasedtrackeraction_markerId_type(instance):
    assert isinstance(instance.markerId, int)


@given(instance=aredsl::MarkerBasedTrackerAction_strategy)
def test_aredsl::markerbasedtrackeraction_markerId_setter(instance):
    original = instance.markerId
    instance.markerId = original
    assert instance.markerId == original

@given(instance=aredsl::TactileAction_strategy)
@settings(max_examples=50)
def test_aredsl::tactileaction_instantiation(instance):
    assert isinstance(instance, aredsl::TactileAction)

@given(instance=aredsl::MentalAction_strategy)
@settings(max_examples=50)
def test_aredsl::mentalaction_instantiation(instance):
    assert isinstance(instance, aredsl::MentalAction)

@given(instance=Behaviour_strategy)
@settings(max_examples=50)
def test_behaviour_instantiation(instance):
    assert isinstance(instance, Behaviour)

@given(instance=aredsl::SupportOperation_strategy)
@settings(max_examples=50)
def test_aredsl::supportoperation_instantiation(instance):
    assert isinstance(instance, aredsl::SupportOperation)

@given(instance=aredsl::DomainOperation_strategy)
@settings(max_examples=50)
def test_aredsl::domainoperation_instantiation(instance):
    assert isinstance(instance, aredsl::DomainOperation)

@given(instance=DomainOperation_strategy)
@settings(max_examples=50)
def test_domainoperation_instantiation(instance):
    assert isinstance(instance, DomainOperation)

@given(instance=aredsl::RemoveOperation_strategy)
@settings(max_examples=50)
def test_aredsl::removeoperation_instantiation(instance):
    assert isinstance(instance, aredsl::RemoveOperation)

@given(instance=aredsl::RemoveOperation_strategy)
def test_aredsl::removeoperation_constraint_type(instance):
    assert isinstance(instance.constraint, str)


@given(instance=aredsl::RemoveOperation_strategy)
def test_aredsl::removeoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=aredsl::SetOperation_strategy)
@settings(max_examples=50)
def test_aredsl::setoperation_instantiation(instance):
    assert isinstance(instance, aredsl::SetOperation)

@given(instance=aredsl::SetOperation_strategy)
def test_aredsl::setoperation_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=aredsl::SetOperation_strategy)
def test_aredsl::setoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=aredsl::SetOperation_strategy)
def test_aredsl::setoperation_constraint_type(instance):
    assert isinstance(instance.constraint, str)


@given(instance=aredsl::SetOperation_strategy)
def test_aredsl::setoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=aredsl::SetOperation_strategy)
def test_aredsl::setoperation_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=aredsl::SetOperation_strategy)
def test_aredsl::setoperation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=aredsl::UnsetOperation_strategy)
@settings(max_examples=50)
def test_aredsl::unsetoperation_instantiation(instance):
    assert isinstance(instance, aredsl::UnsetOperation)

@given(instance=aredsl::UnsetOperation_strategy)
def test_aredsl::unsetoperation_constraint_type(instance):
    assert isinstance(instance.constraint, str)


@given(instance=aredsl::UnsetOperation_strategy)
def test_aredsl::unsetoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=aredsl::UnsetOperation_strategy)
def test_aredsl::unsetoperation_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=aredsl::UnsetOperation_strategy)
def test_aredsl::unsetoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=aredsl::CreateInstanceOperation_strategy)
@settings(max_examples=50)
def test_aredsl::createinstanceoperation_instantiation(instance):
    assert isinstance(instance, aredsl::CreateInstanceOperation)

@given(instance=aredsl::CreateInstanceOperation_strategy)
def test_aredsl::createinstanceoperation_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=aredsl::CreateInstanceOperation_strategy)
def test_aredsl::createinstanceoperation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=aredsl::CreateInstanceOperation_strategy)
def test_aredsl::createinstanceoperation_feature_type(instance):
    assert isinstance(instance.feature, str)


@given(instance=aredsl::CreateInstanceOperation_strategy)
def test_aredsl::createinstanceoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=aredsl::CreateInstanceOperation_strategy)
def test_aredsl::createinstanceoperation_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aredsl::CreateInstanceOperation_strategy)
def test_aredsl::createinstanceoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aredsl::Action_strategy)
@settings(max_examples=50)
def test_aredsl::action_instantiation(instance):
    assert isinstance(instance, aredsl::Action)

@given(instance=aredsl::Action_strategy)
def test_aredsl::action_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::Action_strategy)
def test_aredsl::action_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::ChangeContextOperation_strategy)
@settings(max_examples=50)
def test_aredsl::changecontextoperation_instantiation(instance):
    assert isinstance(instance, aredsl::ChangeContextOperation)

@given(instance=aredsl::ChangeContextOperation_strategy)
def test_aredsl::changecontextoperation_expression_type(instance):
    assert isinstance(instance.expression, str)


@given(instance=aredsl::ChangeContextOperation_strategy)
def test_aredsl::changecontextoperation_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=aredsl::Behaviour_strategy)
@settings(max_examples=50)
def test_aredsl::behaviour_instantiation(instance):
    assert isinstance(instance, aredsl::Behaviour)

@given(instance=aredsl::Behaviour_strategy)
def test_aredsl::behaviour_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::Behaviour_strategy)
def test_aredsl::behaviour_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::Tool_strategy)
@settings(max_examples=50)
def test_aredsl::tool_instantiation(instance):
    assert isinstance(instance, aredsl::Tool)

@given(instance=aredsl::Tool_strategy)
def test_aredsl::tool_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::Tool_strategy)
def test_aredsl::tool_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::Tool_strategy)
def test_aredsl::tool_precondition_type(instance):
    assert isinstance(instance.precondition, str)


@given(instance=aredsl::Tool_strategy)
def test_aredsl::tool_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original

@given(instance=aredsl::Tool_strategy)
def test_aredsl::tool_targetPrecondition_type(instance):
    assert isinstance(instance.targetPrecondition, str)


@given(instance=aredsl::Tool_strategy)
def test_aredsl::tool_targetPrecondition_setter(instance):
    original = instance.targetPrecondition
    instance.targetPrecondition = original
    assert instance.targetPrecondition == original

@given(instance=aredsl::Tool_strategy)
def test_aredsl::tool_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aredsl::Tool_strategy)
def test_aredsl::tool_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl::EdgeStyle_strategy)
@settings(max_examples=50)
def test_aredsl::edgestyle_instantiation(instance):
    assert isinstance(instance, aredsl::EdgeStyle)

@given(instance=aredsl::EdgeStyle_strategy)
def test_aredsl::edgestyle_semanticCondition_type(instance):
    assert isinstance(instance.semanticCondition, str)


@given(instance=aredsl::EdgeStyle_strategy)
def test_aredsl::edgestyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original

@given(instance=aredsl::EdgeStyle_strategy)
def test_aredsl::edgestyle_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=aredsl::EdgeStyle_strategy)
def test_aredsl::edgestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=aredsl::EdgeStyle_strategy)
def test_aredsl::edgestyle_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=aredsl::EdgeStyle_strategy)
def test_aredsl::edgestyle_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aredsl::EdgeStyle_strategy)
def test_aredsl::edgestyle_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=aredsl::EdgeStyle_strategy)
def test_aredsl::edgestyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=aredsl::LabelStyle_strategy)
@settings(max_examples=50)
def test_aredsl::labelstyle_instantiation(instance):
    assert isinstance(instance, aredsl::LabelStyle)

@given(instance=aredsl::LabelStyle_strategy)
def test_aredsl::labelstyle_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=aredsl::LabelStyle_strategy)
def test_aredsl::labelstyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=aredsl::LabelStyle_strategy)
def test_aredsl::labelstyle_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=aredsl::LabelStyle_strategy)
def test_aredsl::labelstyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=aredsl::LabelStyle_strategy)
def test_aredsl::labelstyle_semanticCondition_type(instance):
    assert isinstance(instance.semanticCondition, str)


@given(instance=aredsl::LabelStyle_strategy)
def test_aredsl::labelstyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original

@given(instance=aredsl::Label_strategy)
@settings(max_examples=50)
def test_aredsl::label_instantiation(instance):
    assert isinstance(instance, aredsl::Label)

@given(instance=aredsl::Label_strategy)
def test_aredsl::label_semantics_type(instance):
    assert isinstance(instance.semantics, str)


@given(instance=aredsl::Label_strategy)
def test_aredsl::label_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original

@given(instance=aredsl::Label_strategy)
def test_aredsl::label_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aredsl::Label_strategy)
def test_aredsl::label_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl::Label_strategy)
def test_aredsl::label_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::Label_strategy)
def test_aredsl::label_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::NodeStyle_strategy)
@settings(max_examples=50)
def test_aredsl::nodestyle_instantiation(instance):
    assert isinstance(instance, aredsl::NodeStyle)

@given(instance=aredsl::NodeStyle_strategy)
def test_aredsl::nodestyle_height_type(instance):
    assert isinstance(instance.height, int)


@given(instance=aredsl::NodeStyle_strategy)
def test_aredsl::nodestyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=aredsl::NodeStyle_strategy)
def test_aredsl::nodestyle_semanticCondition_type(instance):
    assert isinstance(instance.semanticCondition, str)


@given(instance=aredsl::NodeStyle_strategy)
def test_aredsl::nodestyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original

@given(instance=aredsl::NodeStyle_strategy)
def test_aredsl::nodestyle_width_type(instance):
    assert isinstance(instance.width, int)


@given(instance=aredsl::NodeStyle_strategy)
def test_aredsl::nodestyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=NodeStyle_strategy)
@settings(max_examples=50)
def test_nodestyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)

@given(instance=aredsl::GeometricShapeNodeStyle_strategy)
@settings(max_examples=50)
def test_aredsl::geometricshapenodestyle_instantiation(instance):
    assert isinstance(instance, aredsl::GeometricShapeNodeStyle)

@given(instance=aredsl::GeometricShapeNodeStyle_strategy)
def test_aredsl::geometricshapenodestyle_outline_type(instance):
    assert isinstance(instance.outline, str)


@given(instance=aredsl::GeometricShapeNodeStyle_strategy)
def test_aredsl::geometricshapenodestyle_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=aredsl::GeometricShapeNodeStyle_strategy)
def test_aredsl::geometricshapenodestyle_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=aredsl::GeometricShapeNodeStyle_strategy)
def test_aredsl::geometricshapenodestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=aredsl::GeometricShapeNodeStyle_strategy)
def test_aredsl::geometricshapenodestyle_kind_type(instance):
    assert isinstance(instance.kind, str)


@given(instance=aredsl::GeometricShapeNodeStyle_strategy)
def test_aredsl::geometricshapenodestyle_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original

@given(instance=aredsl::Image2DNodeStyle_strategy)
@settings(max_examples=50)
def test_aredsl::image2dnodestyle_instantiation(instance):
    assert isinstance(instance, aredsl::Image2DNodeStyle)

@given(instance=aredsl::Image2DNodeStyle_strategy)
def test_aredsl::image2dnodestyle_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=aredsl::Image2DNodeStyle_strategy)
def test_aredsl::image2dnodestyle_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=aredsl::Model3DNodeStyle_strategy)
@settings(max_examples=50)
def test_aredsl::model3dnodestyle_instantiation(instance):
    assert isinstance(instance, aredsl::Model3DNodeStyle)

@given(instance=aredsl::Model3DNodeStyle_strategy)
def test_aredsl::model3dnodestyle_file_type(instance):
    assert isinstance(instance.file, str)


@given(instance=aredsl::Model3DNodeStyle_strategy)
def test_aredsl::model3dnodestyle_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=aredsl::ToolSet_strategy)
@settings(max_examples=50)
def test_aredsl::toolset_instantiation(instance):
    assert isinstance(instance, aredsl::ToolSet)

@given(instance=aredsl::ToolSet_strategy)
def test_aredsl::toolset_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aredsl::ToolSet_strategy)
def test_aredsl::toolset_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl::ToolSet_strategy)
def test_aredsl::toolset_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::ToolSet_strategy)
def test_aredsl::toolset_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::Layer_strategy)
@settings(max_examples=50)
def test_aredsl::layer_instantiation(instance):
    assert isinstance(instance, aredsl::Layer)

@given(instance=aredsl::Layer_strategy)
def test_aredsl::layer_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aredsl::Layer_strategy)
def test_aredsl::layer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl::Layer_strategy)
def test_aredsl::layer_semantics_type(instance):
    assert isinstance(instance.semantics, str)


@given(instance=aredsl::Layer_strategy)
def test_aredsl::layer_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original

@given(instance=aredsl::Layer_strategy)
def test_aredsl::layer_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::Layer_strategy)
def test_aredsl::layer_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::Editor_strategy)
@settings(max_examples=50)
def test_aredsl::editor_instantiation(instance):
    assert isinstance(instance, aredsl::Editor)

@given(instance=aredsl::Editor_strategy)
def test_aredsl::editor_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=aredsl::Editor_strategy)
def test_aredsl::editor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aredsl::Editor_strategy)
def test_aredsl::editor_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::Editor_strategy)
def test_aredsl::editor_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::Editor_strategy)
def test_aredsl::editor_fileExtension_type(instance):
    assert isinstance(instance.fileExtension, str)


@given(instance=aredsl::Editor_strategy)
def test_aredsl::editor_fileExtension_setter(instance):
    original = instance.fileExtension
    instance.fileExtension = original
    assert instance.fileExtension == original

@given(instance=aredsl::Editor_strategy)
def test_aredsl::editor_queryLanguageKind_type(instance):
    assert isinstance(instance.queryLanguageKind, str)


@given(instance=aredsl::Editor_strategy)
def test_aredsl::editor_queryLanguageKind_setter(instance):
    original = instance.queryLanguageKind
    instance.queryLanguageKind = original
    assert instance.queryLanguageKind == original

@given(instance=aredsl::TrackerAction_strategy)
@settings(max_examples=50)
def test_aredsl::trackeraction_instantiation(instance):
    assert isinstance(instance, aredsl::TrackerAction)

@given(instance=aredsl::Edge_strategy)
@settings(max_examples=50)
def test_aredsl::edge_instantiation(instance):
    assert isinstance(instance, aredsl::Edge)

@given(instance=aredsl::Edge_strategy)
def test_aredsl::edge_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::Edge_strategy)
def test_aredsl::edge_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::Edge_strategy)
def test_aredsl::edge_originSemantics_type(instance):
    assert isinstance(instance.originSemantics, str)


@given(instance=aredsl::Edge_strategy)
def test_aredsl::edge_originSemantics_setter(instance):
    original = instance.originSemantics
    instance.originSemantics = original
    assert instance.originSemantics == original

@given(instance=aredsl::Edge_strategy)
def test_aredsl::edge_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aredsl::Edge_strategy)
def test_aredsl::edge_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl::Edge_strategy)
def test_aredsl::edge_destinationSemantics_type(instance):
    assert isinstance(instance.destinationSemantics, str)


@given(instance=aredsl::Edge_strategy)
def test_aredsl::edge_destinationSemantics_setter(instance):
    original = instance.destinationSemantics
    instance.destinationSemantics = original
    assert instance.destinationSemantics == original

@given(instance=aredsl::Node_strategy)
@settings(max_examples=50)
def test_aredsl::node_instantiation(instance):
    assert isinstance(instance, aredsl::Node)

@given(instance=aredsl::Node_strategy)
def test_aredsl::node_semantics_type(instance):
    assert isinstance(instance.semantics, str)


@given(instance=aredsl::Node_strategy)
def test_aredsl::node_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original

@given(instance=aredsl::Node_strategy)
def test_aredsl::node_description_type(instance):
    assert isinstance(instance.description, str)


@given(instance=aredsl::Node_strategy)
def test_aredsl::node_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl::Node_strategy)
def test_aredsl::node_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=aredsl::Node_strategy)
def test_aredsl::node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl::Node_strategy)
def test_aredsl::node_contaimentKind_type(instance):
    assert isinstance(instance.contaimentKind, str)


@given(instance=aredsl::Node_strategy)
def test_aredsl::node_contaimentKind_setter(instance):
    original = instance.contaimentKind
    instance.contaimentKind = original
    assert instance.contaimentKind == original
