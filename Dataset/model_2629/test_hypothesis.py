import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SupportOperation,
    aredsl_ArrangeElements,
    aredsl_ShowSystemMenu,
    aredsl_Exit,
    aredsl_MoveElement,
    Action,
    aredsl_VoiceAction,
    aredsl_GestureAction,
    aredsl_SensorBasedAction,
    TrackerAction,
    aredsl_MarkerLessTrackerAction,
    aredsl_MarkerBasedTrackerAction,
    aredsl_TactileAction,
    aredsl_MentalAction,
    Behaviour,
    aredsl_SupportOperation,
    aredsl_DomainOperation,
    DomainOperation,
    aredsl_UnsetOperation,
    aredsl_RemoveOperation,
    aredsl_SetOperation,
    aredsl_CreateInstanceOperation,
    aredsl_Action,
    aredsl_ChangeContextOperation,
    aredsl_Behaviour,
    aredsl_Tool,
    aredsl_EdgeStyle,
    aredsl_LabelStyle,
    aredsl_Label,
    aredsl_NodeStyle,
    NodeStyle,
    aredsl_Image2DNodeStyle,
    aredsl_GeometricShapeNodeStyle,
    aredsl_Model3DNodeStyle,
    aredsl_ToolSet,
    aredsl_Layer,
    aredsl_Editor,
    aredsl_TrackerAction,
    aredsl_Edge,
    aredsl_Node,
    LineKind,
    QueryLanguageKind,
    ShapeKind,
    OutlineKind,
    IntegrityRestrictionKind,
    ContainmentKind,
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



def test_aredsl_arrangeelements_is_not_abstract():
    assert not inspect.isabstract(aredsl_ArrangeElements)


def test_aredsl_arrangeelements_constructor_exists():
    assert callable(aredsl_ArrangeElements.__init__)


def test_aredsl_arrangeelements_constructor_args():
    sig = inspect.signature(aredsl_ArrangeElements.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_showsystemmenu_is_not_abstract():
    assert not inspect.isabstract(aredsl_ShowSystemMenu)


def test_aredsl_showsystemmenu_constructor_exists():
    assert callable(aredsl_ShowSystemMenu.__init__)


def test_aredsl_showsystemmenu_constructor_args():
    sig = inspect.signature(aredsl_ShowSystemMenu.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_exit_is_not_abstract():
    assert not inspect.isabstract(aredsl_Exit)


def test_aredsl_exit_constructor_exists():
    assert callable(aredsl_Exit.__init__)


def test_aredsl_exit_constructor_args():
    sig = inspect.signature(aredsl_Exit.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_moveelement_is_not_abstract():
    assert not inspect.isabstract(aredsl_MoveElement)


def test_aredsl_moveelement_constructor_exists():
    assert callable(aredsl_MoveElement.__init__)


def test_aredsl_moveelement_constructor_args():
    sig = inspect.signature(aredsl_MoveElement.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_voiceaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_VoiceAction)


def test_aredsl_voiceaction_constructor_exists():
    assert callable(aredsl_VoiceAction.__init__)


def test_aredsl_voiceaction_constructor_args():
    sig = inspect.signature(aredsl_VoiceAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_gestureaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_GestureAction)


def test_aredsl_gestureaction_constructor_exists():
    assert callable(aredsl_GestureAction.__init__)


def test_aredsl_gestureaction_constructor_args():
    sig = inspect.signature(aredsl_GestureAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_sensorbasedaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_SensorBasedAction)


def test_aredsl_sensorbasedaction_constructor_exists():
    assert callable(aredsl_SensorBasedAction.__init__)


def test_aredsl_sensorbasedaction_constructor_args():
    sig = inspect.signature(aredsl_SensorBasedAction.__init__)
    params = list(sig.parameters.keys())



def test_trackeraction_is_not_abstract():
    assert not inspect.isabstract(TrackerAction)


def test_trackeraction_constructor_exists():
    assert callable(TrackerAction.__init__)


def test_trackeraction_constructor_args():
    sig = inspect.signature(TrackerAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_markerlesstrackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl_MarkerLessTrackerAction)


def test_aredsl_markerlesstrackeraction_constructor_exists():
    assert callable(aredsl_MarkerLessTrackerAction.__init__)


def test_aredsl_markerlesstrackeraction_constructor_args():
    sig = inspect.signature(aredsl_MarkerLessTrackerAction.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_aredsl_markerlesstrackeraction_has_file():
    assert hasattr(aredsl_MarkerLessTrackerAction, "file")
    descriptor = None
    for klass in aredsl_MarkerLessTrackerAction.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_markerbasedtrackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl_MarkerBasedTrackerAction)


def test_aredsl_markerbasedtrackeraction_constructor_exists():
    assert callable(aredsl_MarkerBasedTrackerAction.__init__)


def test_aredsl_markerbasedtrackeraction_constructor_args():
    sig = inspect.signature(aredsl_MarkerBasedTrackerAction.__init__)
    params = list(sig.parameters.keys())
    assert "markerId" in params, "Missing parameter 'markerId'"

def test_aredsl_markerbasedtrackeraction_has_markerId():
    assert hasattr(aredsl_MarkerBasedTrackerAction, "markerId")
    descriptor = None
    for klass in aredsl_MarkerBasedTrackerAction.__mro__:
        if "markerId" in klass.__dict__:
            descriptor = klass.__dict__["markerId"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_tactileaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_TactileAction)


def test_aredsl_tactileaction_constructor_exists():
    assert callable(aredsl_TactileAction.__init__)


def test_aredsl_tactileaction_constructor_args():
    sig = inspect.signature(aredsl_TactileAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_mentalaction_is_not_abstract():
    assert not inspect.isabstract(aredsl_MentalAction)


def test_aredsl_mentalaction_constructor_exists():
    assert callable(aredsl_MentalAction.__init__)


def test_aredsl_mentalaction_constructor_args():
    sig = inspect.signature(aredsl_MentalAction.__init__)
    params = list(sig.parameters.keys())



def test_behaviour_is_not_abstract():
    assert not inspect.isabstract(Behaviour)


def test_behaviour_constructor_exists():
    assert callable(Behaviour.__init__)


def test_behaviour_constructor_args():
    sig = inspect.signature(Behaviour.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_supportoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_SupportOperation)


def test_aredsl_supportoperation_constructor_exists():
    assert callable(aredsl_SupportOperation.__init__)


def test_aredsl_supportoperation_constructor_args():
    sig = inspect.signature(aredsl_SupportOperation.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_domainoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_DomainOperation)


def test_aredsl_domainoperation_constructor_exists():
    assert callable(aredsl_DomainOperation.__init__)


def test_aredsl_domainoperation_constructor_args():
    sig = inspect.signature(aredsl_DomainOperation.__init__)
    params = list(sig.parameters.keys())



def test_domainoperation_is_not_abstract():
    assert not inspect.isabstract(DomainOperation)


def test_domainoperation_constructor_exists():
    assert callable(DomainOperation.__init__)


def test_domainoperation_constructor_args():
    sig = inspect.signature(DomainOperation.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_unsetoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_UnsetOperation)


def test_aredsl_unsetoperation_constructor_exists():
    assert callable(aredsl_UnsetOperation.__init__)


def test_aredsl_unsetoperation_constructor_args():
    sig = inspect.signature(aredsl_UnsetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"
    assert "feature" in params, "Missing parameter 'feature'"

def test_aredsl_unsetoperation_has_constraint():
    assert hasattr(aredsl_UnsetOperation, "constraint")
    descriptor = None
    for klass in aredsl_UnsetOperation.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_unsetoperation_has_feature():
    assert hasattr(aredsl_UnsetOperation, "feature")
    descriptor = None
    for klass in aredsl_UnsetOperation.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_removeoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_RemoveOperation)


def test_aredsl_removeoperation_constructor_exists():
    assert callable(aredsl_RemoveOperation.__init__)


def test_aredsl_removeoperation_constructor_args():
    sig = inspect.signature(aredsl_RemoveOperation.__init__)
    params = list(sig.parameters.keys())
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_aredsl_removeoperation_has_constraint():
    assert hasattr(aredsl_RemoveOperation, "constraint")
    descriptor = None
    for klass in aredsl_RemoveOperation.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_setoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_SetOperation)


def test_aredsl_setoperation_constructor_exists():
    assert callable(aredsl_SetOperation.__init__)


def test_aredsl_setoperation_constructor_args():
    sig = inspect.signature(aredsl_SetOperation.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"
    assert "value" in params, "Missing parameter 'value'"
    assert "constraint" in params, "Missing parameter 'constraint'"

def test_aredsl_setoperation_has_feature():
    assert hasattr(aredsl_SetOperation, "feature")
    descriptor = None
    for klass in aredsl_SetOperation.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_setoperation_has_value():
    assert hasattr(aredsl_SetOperation, "value")
    descriptor = None
    for klass in aredsl_SetOperation.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_setoperation_has_constraint():
    assert hasattr(aredsl_SetOperation, "constraint")
    descriptor = None
    for klass in aredsl_SetOperation.__mro__:
        if "constraint" in klass.__dict__:
            descriptor = klass.__dict__["constraint"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_createinstanceoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_CreateInstanceOperation)


def test_aredsl_createinstanceoperation_constructor_exists():
    assert callable(aredsl_CreateInstanceOperation.__init__)


def test_aredsl_createinstanceoperation_constructor_args():
    sig = inspect.signature(aredsl_CreateInstanceOperation.__init__)
    params = list(sig.parameters.keys())
    assert "feature" in params, "Missing parameter 'feature'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_aredsl_createinstanceoperation_has_feature():
    assert hasattr(aredsl_CreateInstanceOperation, "feature")
    descriptor = None
    for klass in aredsl_CreateInstanceOperation.__mro__:
        if "feature" in klass.__dict__:
            descriptor = klass.__dict__["feature"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_createinstanceoperation_has_type():
    assert hasattr(aredsl_CreateInstanceOperation, "type")
    descriptor = None
    for klass in aredsl_CreateInstanceOperation.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_createinstanceoperation_has_name():
    assert hasattr(aredsl_CreateInstanceOperation, "name")
    descriptor = None
    for klass in aredsl_CreateInstanceOperation.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_action_is_not_abstract():
    assert not inspect.isabstract(aredsl_Action)


def test_aredsl_action_constructor_exists():
    assert callable(aredsl_Action.__init__)


def test_aredsl_action_constructor_args():
    sig = inspect.signature(aredsl_Action.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_aredsl_action_has_description():
    assert hasattr(aredsl_Action, "description")
    descriptor = None
    for klass in aredsl_Action.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_changecontextoperation_is_not_abstract():
    assert not inspect.isabstract(aredsl_ChangeContextOperation)


def test_aredsl_changecontextoperation_constructor_exists():
    assert callable(aredsl_ChangeContextOperation.__init__)


def test_aredsl_changecontextoperation_constructor_args():
    sig = inspect.signature(aredsl_ChangeContextOperation.__init__)
    params = list(sig.parameters.keys())
    assert "expression" in params, "Missing parameter 'expression'"

def test_aredsl_changecontextoperation_has_expression():
    assert hasattr(aredsl_ChangeContextOperation, "expression")
    descriptor = None
    for klass in aredsl_ChangeContextOperation.__mro__:
        if "expression" in klass.__dict__:
            descriptor = klass.__dict__["expression"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_behaviour_is_not_abstract():
    assert not inspect.isabstract(aredsl_Behaviour)


def test_aredsl_behaviour_constructor_exists():
    assert callable(aredsl_Behaviour.__init__)


def test_aredsl_behaviour_constructor_args():
    sig = inspect.signature(aredsl_Behaviour.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"

def test_aredsl_behaviour_has_description():
    assert hasattr(aredsl_Behaviour, "description")
    descriptor = None
    for klass in aredsl_Behaviour.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_tool_is_not_abstract():
    assert not inspect.isabstract(aredsl_Tool)


def test_aredsl_tool_constructor_exists():
    assert callable(aredsl_Tool.__init__)


def test_aredsl_tool_constructor_args():
    sig = inspect.signature(aredsl_Tool.__init__)
    params = list(sig.parameters.keys())
    assert "precondition" in params, "Missing parameter 'precondition'"
    assert "targetPrecondition" in params, "Missing parameter 'targetPrecondition'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_aredsl_tool_has_precondition():
    assert hasattr(aredsl_Tool, "precondition")
    descriptor = None
    for klass in aredsl_Tool.__mro__:
        if "precondition" in klass.__dict__:
            descriptor = klass.__dict__["precondition"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_tool_has_targetPrecondition():
    assert hasattr(aredsl_Tool, "targetPrecondition")
    descriptor = None
    for klass in aredsl_Tool.__mro__:
        if "targetPrecondition" in klass.__dict__:
            descriptor = klass.__dict__["targetPrecondition"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_tool_has_description():
    assert hasattr(aredsl_Tool, "description")
    descriptor = None
    for klass in aredsl_Tool.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_tool_has_id():
    assert hasattr(aredsl_Tool, "id")
    descriptor = None
    for klass in aredsl_Tool.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_edgestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_EdgeStyle)


def test_aredsl_edgestyle_constructor_exists():
    assert callable(aredsl_EdgeStyle.__init__)


def test_aredsl_edgestyle_constructor_args():
    sig = inspect.signature(aredsl_EdgeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "color" in params, "Missing parameter 'color'"
    assert "width" in params, "Missing parameter 'width'"

def test_aredsl_edgestyle_has_semanticCondition():
    assert hasattr(aredsl_EdgeStyle, "semanticCondition")
    descriptor = None
    for klass in aredsl_EdgeStyle.__mro__:
        if "semanticCondition" in klass.__dict__:
            descriptor = klass.__dict__["semanticCondition"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_edgestyle_has_kind():
    assert hasattr(aredsl_EdgeStyle, "kind")
    descriptor = None
    for klass in aredsl_EdgeStyle.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_edgestyle_has_color():
    assert hasattr(aredsl_EdgeStyle, "color")
    descriptor = None
    for klass in aredsl_EdgeStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_edgestyle_has_width():
    assert hasattr(aredsl_EdgeStyle, "width")
    descriptor = None
    for klass in aredsl_EdgeStyle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_labelstyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_LabelStyle)


def test_aredsl_labelstyle_constructor_exists():
    assert callable(aredsl_LabelStyle.__init__)


def test_aredsl_labelstyle_constructor_args():
    sig = inspect.signature(aredsl_LabelStyle.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "color" in params, "Missing parameter 'color'"
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"

def test_aredsl_labelstyle_has_height():
    assert hasattr(aredsl_LabelStyle, "height")
    descriptor = None
    for klass in aredsl_LabelStyle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_labelstyle_has_color():
    assert hasattr(aredsl_LabelStyle, "color")
    descriptor = None
    for klass in aredsl_LabelStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_labelstyle_has_semanticCondition():
    assert hasattr(aredsl_LabelStyle, "semanticCondition")
    descriptor = None
    for klass in aredsl_LabelStyle.__mro__:
        if "semanticCondition" in klass.__dict__:
            descriptor = klass.__dict__["semanticCondition"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_label_is_not_abstract():
    assert not inspect.isabstract(aredsl_Label)


def test_aredsl_label_constructor_exists():
    assert callable(aredsl_Label.__init__)


def test_aredsl_label_constructor_args():
    sig = inspect.signature(aredsl_Label.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "semantics" in params, "Missing parameter 'semantics'"

def test_aredsl_label_has_description():
    assert hasattr(aredsl_Label, "description")
    descriptor = None
    for klass in aredsl_Label.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_label_has_id():
    assert hasattr(aredsl_Label, "id")
    descriptor = None
    for klass in aredsl_Label.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_label_has_semantics():
    assert hasattr(aredsl_Label, "semantics")
    descriptor = None
    for klass in aredsl_Label.__mro__:
        if "semantics" in klass.__dict__:
            descriptor = klass.__dict__["semantics"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_nodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_NodeStyle)


def test_aredsl_nodestyle_constructor_exists():
    assert callable(aredsl_NodeStyle.__init__)


def test_aredsl_nodestyle_constructor_args():
    sig = inspect.signature(aredsl_NodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "semanticCondition" in params, "Missing parameter 'semanticCondition'"
    assert "height" in params, "Missing parameter 'height'"

def test_aredsl_nodestyle_has_width():
    assert hasattr(aredsl_NodeStyle, "width")
    descriptor = None
    for klass in aredsl_NodeStyle.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_nodestyle_has_semanticCondition():
    assert hasattr(aredsl_NodeStyle, "semanticCondition")
    descriptor = None
    for klass in aredsl_NodeStyle.__mro__:
        if "semanticCondition" in klass.__dict__:
            descriptor = klass.__dict__["semanticCondition"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_nodestyle_has_height():
    assert hasattr(aredsl_NodeStyle, "height")
    descriptor = None
    for klass in aredsl_NodeStyle.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_nodestyle_is_not_abstract():
    assert not inspect.isabstract(NodeStyle)


def test_nodestyle_constructor_exists():
    assert callable(NodeStyle.__init__)


def test_nodestyle_constructor_args():
    sig = inspect.signature(NodeStyle.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_image2dnodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_Image2DNodeStyle)


def test_aredsl_image2dnodestyle_constructor_exists():
    assert callable(aredsl_Image2DNodeStyle.__init__)


def test_aredsl_image2dnodestyle_constructor_args():
    sig = inspect.signature(aredsl_Image2DNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_aredsl_image2dnodestyle_has_file():
    assert hasattr(aredsl_Image2DNodeStyle, "file")
    descriptor = None
    for klass in aredsl_Image2DNodeStyle.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_geometricshapenodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_GeometricShapeNodeStyle)


def test_aredsl_geometricshapenodestyle_constructor_exists():
    assert callable(aredsl_GeometricShapeNodeStyle.__init__)


def test_aredsl_geometricshapenodestyle_constructor_args():
    sig = inspect.signature(aredsl_GeometricShapeNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"
    assert "kind" in params, "Missing parameter 'kind'"
    assert "outline" in params, "Missing parameter 'outline'"

def test_aredsl_geometricshapenodestyle_has_color():
    assert hasattr(aredsl_GeometricShapeNodeStyle, "color")
    descriptor = None
    for klass in aredsl_GeometricShapeNodeStyle.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_geometricshapenodestyle_has_kind():
    assert hasattr(aredsl_GeometricShapeNodeStyle, "kind")
    descriptor = None
    for klass in aredsl_GeometricShapeNodeStyle.__mro__:
        if "kind" in klass.__dict__:
            descriptor = klass.__dict__["kind"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_geometricshapenodestyle_has_outline():
    assert hasattr(aredsl_GeometricShapeNodeStyle, "outline")
    descriptor = None
    for klass in aredsl_GeometricShapeNodeStyle.__mro__:
        if "outline" in klass.__dict__:
            descriptor = klass.__dict__["outline"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_model3dnodestyle_is_not_abstract():
    assert not inspect.isabstract(aredsl_Model3DNodeStyle)


def test_aredsl_model3dnodestyle_constructor_exists():
    assert callable(aredsl_Model3DNodeStyle.__init__)


def test_aredsl_model3dnodestyle_constructor_args():
    sig = inspect.signature(aredsl_Model3DNodeStyle.__init__)
    params = list(sig.parameters.keys())
    assert "file" in params, "Missing parameter 'file'"

def test_aredsl_model3dnodestyle_has_file():
    assert hasattr(aredsl_Model3DNodeStyle, "file")
    descriptor = None
    for klass in aredsl_Model3DNodeStyle.__mro__:
        if "file" in klass.__dict__:
            descriptor = klass.__dict__["file"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_toolset_is_not_abstract():
    assert not inspect.isabstract(aredsl_ToolSet)


def test_aredsl_toolset_constructor_exists():
    assert callable(aredsl_ToolSet.__init__)


def test_aredsl_toolset_constructor_args():
    sig = inspect.signature(aredsl_ToolSet.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_aredsl_toolset_has_description():
    assert hasattr(aredsl_ToolSet, "description")
    descriptor = None
    for klass in aredsl_ToolSet.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_toolset_has_id():
    assert hasattr(aredsl_ToolSet, "id")
    descriptor = None
    for klass in aredsl_ToolSet.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_layer_is_not_abstract():
    assert not inspect.isabstract(aredsl_Layer)


def test_aredsl_layer_constructor_exists():
    assert callable(aredsl_Layer.__init__)


def test_aredsl_layer_constructor_args():
    sig = inspect.signature(aredsl_Layer.__init__)
    params = list(sig.parameters.keys())
    assert "description" in params, "Missing parameter 'description'"
    assert "semantics" in params, "Missing parameter 'semantics'"
    assert "id" in params, "Missing parameter 'id'"

def test_aredsl_layer_has_description():
    assert hasattr(aredsl_Layer, "description")
    descriptor = None
    for klass in aredsl_Layer.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_layer_has_semantics():
    assert hasattr(aredsl_Layer, "semantics")
    descriptor = None
    for klass in aredsl_Layer.__mro__:
        if "semantics" in klass.__dict__:
            descriptor = klass.__dict__["semantics"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_layer_has_id():
    assert hasattr(aredsl_Layer, "id")
    descriptor = None
    for klass in aredsl_Layer.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_editor_is_not_abstract():
    assert not inspect.isabstract(aredsl_Editor)


def test_aredsl_editor_constructor_exists():
    assert callable(aredsl_Editor.__init__)


def test_aredsl_editor_constructor_args():
    sig = inspect.signature(aredsl_Editor.__init__)
    params = list(sig.parameters.keys())
    assert "fileExtension" in params, "Missing parameter 'fileExtension'"
    assert "queryLanguageKind" in params, "Missing parameter 'queryLanguageKind'"
    assert "name" in params, "Missing parameter 'name'"
    assert "description" in params, "Missing parameter 'description'"

def test_aredsl_editor_has_fileExtension():
    assert hasattr(aredsl_Editor, "fileExtension")
    descriptor = None
    for klass in aredsl_Editor.__mro__:
        if "fileExtension" in klass.__dict__:
            descriptor = klass.__dict__["fileExtension"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_editor_has_queryLanguageKind():
    assert hasattr(aredsl_Editor, "queryLanguageKind")
    descriptor = None
    for klass in aredsl_Editor.__mro__:
        if "queryLanguageKind" in klass.__dict__:
            descriptor = klass.__dict__["queryLanguageKind"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_editor_has_name():
    assert hasattr(aredsl_Editor, "name")
    descriptor = None
    for klass in aredsl_Editor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_editor_has_description():
    assert hasattr(aredsl_Editor, "description")
    descriptor = None
    for klass in aredsl_Editor.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_trackeraction_is_not_abstract():
    assert not inspect.isabstract(aredsl_TrackerAction)


def test_aredsl_trackeraction_constructor_exists():
    assert callable(aredsl_TrackerAction.__init__)


def test_aredsl_trackeraction_constructor_args():
    sig = inspect.signature(aredsl_TrackerAction.__init__)
    params = list(sig.parameters.keys())



def test_aredsl_edge_is_not_abstract():
    assert not inspect.isabstract(aredsl_Edge)


def test_aredsl_edge_constructor_exists():
    assert callable(aredsl_Edge.__init__)


def test_aredsl_edge_constructor_args():
    sig = inspect.signature(aredsl_Edge.__init__)
    params = list(sig.parameters.keys())
    assert "destinationSemantics" in params, "Missing parameter 'destinationSemantics'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"
    assert "originSemantics" in params, "Missing parameter 'originSemantics'"

def test_aredsl_edge_has_destinationSemantics():
    assert hasattr(aredsl_Edge, "destinationSemantics")
    descriptor = None
    for klass in aredsl_Edge.__mro__:
        if "destinationSemantics" in klass.__dict__:
            descriptor = klass.__dict__["destinationSemantics"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_edge_has_description():
    assert hasattr(aredsl_Edge, "description")
    descriptor = None
    for klass in aredsl_Edge.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_edge_has_id():
    assert hasattr(aredsl_Edge, "id")
    descriptor = None
    for klass in aredsl_Edge.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_edge_has_originSemantics():
    assert hasattr(aredsl_Edge, "originSemantics")
    descriptor = None
    for klass in aredsl_Edge.__mro__:
        if "originSemantics" in klass.__dict__:
            descriptor = klass.__dict__["originSemantics"]
            break
    assert isinstance(descriptor, property)



def test_aredsl_node_is_not_abstract():
    assert not inspect.isabstract(aredsl_Node)


def test_aredsl_node_constructor_exists():
    assert callable(aredsl_Node.__init__)


def test_aredsl_node_constructor_args():
    sig = inspect.signature(aredsl_Node.__init__)
    params = list(sig.parameters.keys())
    assert "semantics" in params, "Missing parameter 'semantics'"
    assert "contaimentKind" in params, "Missing parameter 'contaimentKind'"
    assert "description" in params, "Missing parameter 'description'"
    assert "id" in params, "Missing parameter 'id'"

def test_aredsl_node_has_semantics():
    assert hasattr(aredsl_Node, "semantics")
    descriptor = None
    for klass in aredsl_Node.__mro__:
        if "semantics" in klass.__dict__:
            descriptor = klass.__dict__["semantics"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_node_has_contaimentKind():
    assert hasattr(aredsl_Node, "contaimentKind")
    descriptor = None
    for klass in aredsl_Node.__mro__:
        if "contaimentKind" in klass.__dict__:
            descriptor = klass.__dict__["contaimentKind"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_node_has_description():
    assert hasattr(aredsl_Node, "description")
    descriptor = None
    for klass in aredsl_Node.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_aredsl_node_has_id():
    assert hasattr(aredsl_Node, "id")
    descriptor = None
    for klass in aredsl_Node.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_linekind_exists():
    # Check that the Enumeration exists
    assert LineKind is not None

def test_linekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LineKind]
    expected_literals = [
        "DOTTED",
        "DASHED",
        "SOLID",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LineKind"

def test_querylanguagekind_exists():
    # Check that the Enumeration exists
    assert QueryLanguageKind is not None

def test_querylanguagekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in QueryLanguageKind]
    expected_literals = [
        "OCL",
        "JPQL",
        "XPATH_XQUERY",
        "LINQ",
        "AQL",
        "SQL",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in QueryLanguageKind"

def test_shapekind_exists():
    # Check that the Enumeration exists
    assert ShapeKind is not None

def test_shapekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShapeKind]
    expected_literals = [
        "TRIANGLE",
        "CIRCLE",
        "ELLIPSE",
        "DIAMOND",
        "RECTANGLE",
        "SQUARE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShapeKind"

def test_outlinekind_exists():
    # Check that the Enumeration exists
    assert OutlineKind is not None

def test_outlinekind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OutlineKind]
    expected_literals = [
        "DOUBLE",
        "SIMPLE",
        "NONE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OutlineKind"

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

def test_containmentkind_exists():
    # Check that the Enumeration exists
    assert ContainmentKind is not None

def test_containmentkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ContainmentKind]
    expected_literals = [
        "EXTERNAL_LINK",
        "HORIZONTAL_ARRANGEMENT",
        "VERTICAL_ARRANGEMENT",
        "FREE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ContainmentKind"


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
aredsl_ArrangeElements_strategy = st.builds(
    aredsl_ArrangeElements,
)
aredsl_ShowSystemMenu_strategy = st.builds(
    aredsl_ShowSystemMenu,
)
aredsl_Exit_strategy = st.builds(
    aredsl_Exit,
)
aredsl_MoveElement_strategy = st.builds(
    aredsl_MoveElement,
)
Action_strategy = st.builds(
    Action,
)
aredsl_VoiceAction_strategy = st.builds(
    aredsl_VoiceAction,
)
aredsl_GestureAction_strategy = st.builds(
    aredsl_GestureAction,
)
aredsl_SensorBasedAction_strategy = st.builds(
    aredsl_SensorBasedAction,
)
TrackerAction_strategy = st.builds(
    TrackerAction,
)
aredsl_MarkerLessTrackerAction_strategy = st.builds(
    aredsl_MarkerLessTrackerAction,
    file=
        safe_text
)
aredsl_MarkerBasedTrackerAction_strategy = st.builds(
    aredsl_MarkerBasedTrackerAction,
    markerId=
        st.integers()
)
aredsl_TactileAction_strategy = st.builds(
    aredsl_TactileAction,
)
aredsl_MentalAction_strategy = st.builds(
    aredsl_MentalAction,
)
Behaviour_strategy = st.builds(
    Behaviour,
)
aredsl_SupportOperation_strategy = st.builds(
    aredsl_SupportOperation,
)
aredsl_DomainOperation_strategy = st.builds(
    aredsl_DomainOperation,
)
DomainOperation_strategy = st.builds(
    DomainOperation,
)
aredsl_UnsetOperation_strategy = st.builds(
    aredsl_UnsetOperation,
    constraint=
        safe_text,
    feature=
        safe_text
)
aredsl_RemoveOperation_strategy = st.builds(
    aredsl_RemoveOperation,
    constraint=
        safe_text
)
aredsl_SetOperation_strategy = st.builds(
    aredsl_SetOperation,
    feature=
        safe_text,
    value=
        safe_text,
    constraint=
        safe_text
)
aredsl_CreateInstanceOperation_strategy = st.builds(
    aredsl_CreateInstanceOperation,
    feature=
        safe_text,
    type=
        safe_text,
    name=
        safe_text
)
aredsl_Action_strategy = st.builds(
    aredsl_Action,
    description=
        safe_text
)
aredsl_ChangeContextOperation_strategy = st.builds(
    aredsl_ChangeContextOperation,
    expression=
        safe_text
)
aredsl_Behaviour_strategy = st.builds(
    aredsl_Behaviour,
    description=
        safe_text
)
aredsl_Tool_strategy = st.builds(
    aredsl_Tool,
    precondition=
        safe_text,
    targetPrecondition=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)
aredsl_EdgeStyle_strategy = st.builds(
    aredsl_EdgeStyle,
    semanticCondition=
        safe_text,
    kind=
        safe_text,
    color=
        safe_text,
    width=
        st.integers()
)
aredsl_LabelStyle_strategy = st.builds(
    aredsl_LabelStyle,
    height=
        st.integers(),
    color=
        safe_text,
    semanticCondition=
        safe_text
)
aredsl_Label_strategy = st.builds(
    aredsl_Label,
    description=
        safe_text,
    id=
        safe_text,
    semantics=
        safe_text
)
aredsl_NodeStyle_strategy = st.builds(
    aredsl_NodeStyle,
    width=
        st.integers(),
    semanticCondition=
        safe_text,
    height=
        st.integers()
)
NodeStyle_strategy = st.builds(
    NodeStyle,
)
aredsl_Image2DNodeStyle_strategy = st.builds(
    aredsl_Image2DNodeStyle,
    file=
        safe_text
)
aredsl_GeometricShapeNodeStyle_strategy = st.builds(
    aredsl_GeometricShapeNodeStyle,
    color=
        safe_text,
    kind=
        safe_text,
    outline=
        safe_text
)
aredsl_Model3DNodeStyle_strategy = st.builds(
    aredsl_Model3DNodeStyle,
    file=
        safe_text
)
aredsl_ToolSet_strategy = st.builds(
    aredsl_ToolSet,
    description=
        safe_text,
    id=
        safe_text
)
aredsl_Layer_strategy = st.builds(
    aredsl_Layer,
    description=
        safe_text,
    semantics=
        safe_text,
    id=
        safe_text
)
aredsl_Editor_strategy = st.builds(
    aredsl_Editor,
    fileExtension=
        safe_text,
    queryLanguageKind=
        safe_text,
    name=
        safe_text,
    description=
        safe_text
)
aredsl_TrackerAction_strategy = st.builds(
    aredsl_TrackerAction,
)
aredsl_Edge_strategy = st.builds(
    aredsl_Edge,
    destinationSemantics=
        safe_text,
    description=
        safe_text,
    id=
        safe_text,
    originSemantics=
        safe_text
)
aredsl_Node_strategy = st.builds(
    aredsl_Node,
    semantics=
        safe_text,
    contaimentKind=
        safe_text,
    description=
        safe_text,
    id=
        safe_text
)

@given(instance=SupportOperation_strategy)
@settings(max_examples=50)
def test_supportoperation_instantiation(instance):
    assert isinstance(instance, SupportOperation)

@given(instance=aredsl_ArrangeElements_strategy)
@settings(max_examples=50)
def test_aredsl_arrangeelements_instantiation(instance):
    assert isinstance(instance, aredsl_ArrangeElements)

@given(instance=aredsl_ShowSystemMenu_strategy)
@settings(max_examples=50)
def test_aredsl_showsystemmenu_instantiation(instance):
    assert isinstance(instance, aredsl_ShowSystemMenu)

@given(instance=aredsl_Exit_strategy)
@settings(max_examples=50)
def test_aredsl_exit_instantiation(instance):
    assert isinstance(instance, aredsl_Exit)

@given(instance=aredsl_MoveElement_strategy)
@settings(max_examples=50)
def test_aredsl_moveelement_instantiation(instance):
    assert isinstance(instance, aredsl_MoveElement)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=aredsl_VoiceAction_strategy)
@settings(max_examples=50)
def test_aredsl_voiceaction_instantiation(instance):
    assert isinstance(instance, aredsl_VoiceAction)

@given(instance=aredsl_GestureAction_strategy)
@settings(max_examples=50)
def test_aredsl_gestureaction_instantiation(instance):
    assert isinstance(instance, aredsl_GestureAction)

@given(instance=aredsl_SensorBasedAction_strategy)
@settings(max_examples=50)
def test_aredsl_sensorbasedaction_instantiation(instance):
    assert isinstance(instance, aredsl_SensorBasedAction)

@given(instance=TrackerAction_strategy)
@settings(max_examples=50)
def test_trackeraction_instantiation(instance):
    assert isinstance(instance, TrackerAction)

@given(instance=aredsl_MarkerLessTrackerAction_strategy)
@settings(max_examples=50)
def test_aredsl_markerlesstrackeraction_instantiation(instance):
    assert isinstance(instance, aredsl_MarkerLessTrackerAction)



@given(instance=aredsl_MarkerLessTrackerAction_strategy)
def test_aredsl_markerlesstrackeraction_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=aredsl_MarkerBasedTrackerAction_strategy)
@settings(max_examples=50)
def test_aredsl_markerbasedtrackeraction_instantiation(instance):
    assert isinstance(instance, aredsl_MarkerBasedTrackerAction)



@given(instance=aredsl_MarkerBasedTrackerAction_strategy)
def test_aredsl_markerbasedtrackeraction_markerId_setter(instance):
    original = instance.markerId
    instance.markerId = original
    assert instance.markerId == original

@given(instance=aredsl_TactileAction_strategy)
@settings(max_examples=50)
def test_aredsl_tactileaction_instantiation(instance):
    assert isinstance(instance, aredsl_TactileAction)

@given(instance=aredsl_MentalAction_strategy)
@settings(max_examples=50)
def test_aredsl_mentalaction_instantiation(instance):
    assert isinstance(instance, aredsl_MentalAction)

@given(instance=Behaviour_strategy)
@settings(max_examples=50)
def test_behaviour_instantiation(instance):
    assert isinstance(instance, Behaviour)

@given(instance=aredsl_SupportOperation_strategy)
@settings(max_examples=50)
def test_aredsl_supportoperation_instantiation(instance):
    assert isinstance(instance, aredsl_SupportOperation)

@given(instance=aredsl_DomainOperation_strategy)
@settings(max_examples=50)
def test_aredsl_domainoperation_instantiation(instance):
    assert isinstance(instance, aredsl_DomainOperation)

@given(instance=DomainOperation_strategy)
@settings(max_examples=50)
def test_domainoperation_instantiation(instance):
    assert isinstance(instance, DomainOperation)

@given(instance=aredsl_UnsetOperation_strategy)
@settings(max_examples=50)
def test_aredsl_unsetoperation_instantiation(instance):
    assert isinstance(instance, aredsl_UnsetOperation)



@given(instance=aredsl_UnsetOperation_strategy)
def test_aredsl_unsetoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original



@given(instance=aredsl_UnsetOperation_strategy)
def test_aredsl_unsetoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original

@given(instance=aredsl_RemoveOperation_strategy)
@settings(max_examples=50)
def test_aredsl_removeoperation_instantiation(instance):
    assert isinstance(instance, aredsl_RemoveOperation)



@given(instance=aredsl_RemoveOperation_strategy)
def test_aredsl_removeoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=aredsl_SetOperation_strategy)
@settings(max_examples=50)
def test_aredsl_setoperation_instantiation(instance):
    assert isinstance(instance, aredsl_SetOperation)



@given(instance=aredsl_SetOperation_strategy)
def test_aredsl_setoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original



@given(instance=aredsl_SetOperation_strategy)
def test_aredsl_setoperation_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=aredsl_SetOperation_strategy)
def test_aredsl_setoperation_constraint_setter(instance):
    original = instance.constraint
    instance.constraint = original
    assert instance.constraint == original

@given(instance=aredsl_CreateInstanceOperation_strategy)
@settings(max_examples=50)
def test_aredsl_createinstanceoperation_instantiation(instance):
    assert isinstance(instance, aredsl_CreateInstanceOperation)



@given(instance=aredsl_CreateInstanceOperation_strategy)
def test_aredsl_createinstanceoperation_feature_setter(instance):
    original = instance.feature
    instance.feature = original
    assert instance.feature == original



@given(instance=aredsl_CreateInstanceOperation_strategy)
def test_aredsl_createinstanceoperation_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=aredsl_CreateInstanceOperation_strategy)
def test_aredsl_createinstanceoperation_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=aredsl_Action_strategy)
@settings(max_examples=50)
def test_aredsl_action_instantiation(instance):
    assert isinstance(instance, aredsl_Action)



@given(instance=aredsl_Action_strategy)
def test_aredsl_action_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl_ChangeContextOperation_strategy)
@settings(max_examples=50)
def test_aredsl_changecontextoperation_instantiation(instance):
    assert isinstance(instance, aredsl_ChangeContextOperation)



@given(instance=aredsl_ChangeContextOperation_strategy)
def test_aredsl_changecontextoperation_expression_setter(instance):
    original = instance.expression
    instance.expression = original
    assert instance.expression == original

@given(instance=aredsl_Behaviour_strategy)
@settings(max_examples=50)
def test_aredsl_behaviour_instantiation(instance):
    assert isinstance(instance, aredsl_Behaviour)



@given(instance=aredsl_Behaviour_strategy)
def test_aredsl_behaviour_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl_Tool_strategy)
@settings(max_examples=50)
def test_aredsl_tool_instantiation(instance):
    assert isinstance(instance, aredsl_Tool)



@given(instance=aredsl_Tool_strategy)
def test_aredsl_tool_precondition_setter(instance):
    original = instance.precondition
    instance.precondition = original
    assert instance.precondition == original



@given(instance=aredsl_Tool_strategy)
def test_aredsl_tool_targetPrecondition_setter(instance):
    original = instance.targetPrecondition
    instance.targetPrecondition = original
    assert instance.targetPrecondition == original



@given(instance=aredsl_Tool_strategy)
def test_aredsl_tool_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Tool_strategy)
def test_aredsl_tool_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl_EdgeStyle_strategy)
@settings(max_examples=50)
def test_aredsl_edgestyle_instantiation(instance):
    assert isinstance(instance, aredsl_EdgeStyle)



@given(instance=aredsl_EdgeStyle_strategy)
def test_aredsl_edgestyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original



@given(instance=aredsl_EdgeStyle_strategy)
def test_aredsl_edgestyle_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=aredsl_EdgeStyle_strategy)
def test_aredsl_edgestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=aredsl_EdgeStyle_strategy)
def test_aredsl_edgestyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=aredsl_LabelStyle_strategy)
@settings(max_examples=50)
def test_aredsl_labelstyle_instantiation(instance):
    assert isinstance(instance, aredsl_LabelStyle)



@given(instance=aredsl_LabelStyle_strategy)
def test_aredsl_labelstyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=aredsl_LabelStyle_strategy)
def test_aredsl_labelstyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=aredsl_LabelStyle_strategy)
def test_aredsl_labelstyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original

@given(instance=aredsl_Label_strategy)
@settings(max_examples=50)
def test_aredsl_label_instantiation(instance):
    assert isinstance(instance, aredsl_Label)



@given(instance=aredsl_Label_strategy)
def test_aredsl_label_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Label_strategy)
def test_aredsl_label_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aredsl_Label_strategy)
def test_aredsl_label_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original

@given(instance=aredsl_NodeStyle_strategy)
@settings(max_examples=50)
def test_aredsl_nodestyle_instantiation(instance):
    assert isinstance(instance, aredsl_NodeStyle)



@given(instance=aredsl_NodeStyle_strategy)
def test_aredsl_nodestyle_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=aredsl_NodeStyle_strategy)
def test_aredsl_nodestyle_semanticCondition_setter(instance):
    original = instance.semanticCondition
    instance.semanticCondition = original
    assert instance.semanticCondition == original



@given(instance=aredsl_NodeStyle_strategy)
def test_aredsl_nodestyle_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=NodeStyle_strategy)
@settings(max_examples=50)
def test_nodestyle_instantiation(instance):
    assert isinstance(instance, NodeStyle)

@given(instance=aredsl_Image2DNodeStyle_strategy)
@settings(max_examples=50)
def test_aredsl_image2dnodestyle_instantiation(instance):
    assert isinstance(instance, aredsl_Image2DNodeStyle)



@given(instance=aredsl_Image2DNodeStyle_strategy)
def test_aredsl_image2dnodestyle_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=aredsl_GeometricShapeNodeStyle_strategy)
@settings(max_examples=50)
def test_aredsl_geometricshapenodestyle_instantiation(instance):
    assert isinstance(instance, aredsl_GeometricShapeNodeStyle)



@given(instance=aredsl_GeometricShapeNodeStyle_strategy)
def test_aredsl_geometricshapenodestyle_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=aredsl_GeometricShapeNodeStyle_strategy)
def test_aredsl_geometricshapenodestyle_kind_setter(instance):
    original = instance.kind
    instance.kind = original
    assert instance.kind == original



@given(instance=aredsl_GeometricShapeNodeStyle_strategy)
def test_aredsl_geometricshapenodestyle_outline_setter(instance):
    original = instance.outline
    instance.outline = original
    assert instance.outline == original

@given(instance=aredsl_Model3DNodeStyle_strategy)
@settings(max_examples=50)
def test_aredsl_model3dnodestyle_instantiation(instance):
    assert isinstance(instance, aredsl_Model3DNodeStyle)



@given(instance=aredsl_Model3DNodeStyle_strategy)
def test_aredsl_model3dnodestyle_file_setter(instance):
    original = instance.file
    instance.file = original
    assert instance.file == original

@given(instance=aredsl_ToolSet_strategy)
@settings(max_examples=50)
def test_aredsl_toolset_instantiation(instance):
    assert isinstance(instance, aredsl_ToolSet)



@given(instance=aredsl_ToolSet_strategy)
def test_aredsl_toolset_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_ToolSet_strategy)
def test_aredsl_toolset_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl_Layer_strategy)
@settings(max_examples=50)
def test_aredsl_layer_instantiation(instance):
    assert isinstance(instance, aredsl_Layer)



@given(instance=aredsl_Layer_strategy)
def test_aredsl_layer_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Layer_strategy)
def test_aredsl_layer_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original



@given(instance=aredsl_Layer_strategy)
def test_aredsl_layer_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=aredsl_Editor_strategy)
@settings(max_examples=50)
def test_aredsl_editor_instantiation(instance):
    assert isinstance(instance, aredsl_Editor)



@given(instance=aredsl_Editor_strategy)
def test_aredsl_editor_fileExtension_setter(instance):
    original = instance.fileExtension
    instance.fileExtension = original
    assert instance.fileExtension == original



@given(instance=aredsl_Editor_strategy)
def test_aredsl_editor_queryLanguageKind_setter(instance):
    original = instance.queryLanguageKind
    instance.queryLanguageKind = original
    assert instance.queryLanguageKind == original



@given(instance=aredsl_Editor_strategy)
def test_aredsl_editor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=aredsl_Editor_strategy)
def test_aredsl_editor_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=aredsl_TrackerAction_strategy)
@settings(max_examples=50)
def test_aredsl_trackeraction_instantiation(instance):
    assert isinstance(instance, aredsl_TrackerAction)

@given(instance=aredsl_Edge_strategy)
@settings(max_examples=50)
def test_aredsl_edge_instantiation(instance):
    assert isinstance(instance, aredsl_Edge)



@given(instance=aredsl_Edge_strategy)
def test_aredsl_edge_destinationSemantics_setter(instance):
    original = instance.destinationSemantics
    instance.destinationSemantics = original
    assert instance.destinationSemantics == original



@given(instance=aredsl_Edge_strategy)
def test_aredsl_edge_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Edge_strategy)
def test_aredsl_edge_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=aredsl_Edge_strategy)
def test_aredsl_edge_originSemantics_setter(instance):
    original = instance.originSemantics
    instance.originSemantics = original
    assert instance.originSemantics == original

@given(instance=aredsl_Node_strategy)
@settings(max_examples=50)
def test_aredsl_node_instantiation(instance):
    assert isinstance(instance, aredsl_Node)



@given(instance=aredsl_Node_strategy)
def test_aredsl_node_semantics_setter(instance):
    original = instance.semantics
    instance.semantics = original
    assert instance.semantics == original



@given(instance=aredsl_Node_strategy)
def test_aredsl_node_contaimentKind_setter(instance):
    original = instance.contaimentKind
    instance.contaimentKind = original
    assert instance.contaimentKind == original



@given(instance=aredsl_Node_strategy)
def test_aredsl_node_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=aredsl_Node_strategy)
def test_aredsl_node_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original
