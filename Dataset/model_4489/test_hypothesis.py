import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Expression,
    dSL_ORexpression,
    dSL_DepthLiteral,
    dSL_ANDexpression,
    dSL_ExpressionBracket,
    dSL_TrueLiteral,
    dSL_EdgeLiteral,
    dSL_DistanceLiteral,
    dSL_ColorLiteral,
    dSL_TouchLiteral,
    dSL_MovementAction,
    Actions,
    dSL_LeftMovementAction,
    dSL_MeasurementAction,
    dSL_MoveAction,
    dSL_Actions,
    dSL_Expression,
    RotatePoints,
    dSL_RightRotatePoint,
    dSL_MiddleRotatePoint,
    dSL_LeftRotatePoint,
    RotateMovementAction,
    dSL_RotatePoints,
    dSL_RotateMovementAction,
    dSL_RightMovementAction,
    dSL_Behavior,
    dSL_Mission,
    dSL_MarsRoverExpedition,
    EndCondition,
    dSL_EndAfter,
    dSL_EndWhen,
    dSL_EndCondition,
    dSL_BehaviorName,
    ActionEnum,
    Tenum,
    EdgeEnum,
    TouchEnum,
    BackEnum,
    LREnum,
    FBEnum,
    ColorEnum,
    MAEnum,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_orexpression_is_not_abstract():
    assert not inspect.isabstract(dSL_ORexpression)


def test_dsl_orexpression_constructor_exists():
    assert callable(dSL_ORexpression.__init__)


def test_dsl_orexpression_constructor_args():
    sig = inspect.signature(dSL_ORexpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_depthliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_DepthLiteral)


def test_dsl_depthliteral_constructor_exists():
    assert callable(dSL_DepthLiteral.__init__)


def test_dsl_depthliteral_constructor_args():
    sig = inspect.signature(dSL_DepthLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "back" in params, "Missing parameter 'back'"

def test_dsl_depthliteral_has_back():
    assert hasattr(dSL_DepthLiteral, "back")
    descriptor = None
    for klass in dSL_DepthLiteral.__mro__:
        if "back" in klass.__dict__:
            descriptor = klass.__dict__["back"]
            break
    assert isinstance(descriptor, property)



def test_dsl_andexpression_is_not_abstract():
    assert not inspect.isabstract(dSL_ANDexpression)


def test_dsl_andexpression_constructor_exists():
    assert callable(dSL_ANDexpression.__init__)


def test_dsl_andexpression_constructor_args():
    sig = inspect.signature(dSL_ANDexpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl_expressionbracket_is_not_abstract():
    assert not inspect.isabstract(dSL_ExpressionBracket)


def test_dsl_expressionbracket_constructor_exists():
    assert callable(dSL_ExpressionBracket.__init__)


def test_dsl_expressionbracket_constructor_args():
    sig = inspect.signature(dSL_ExpressionBracket.__init__)
    params = list(sig.parameters.keys())



def test_dsl_trueliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_TrueLiteral)


def test_dsl_trueliteral_constructor_exists():
    assert callable(dSL_TrueLiteral.__init__)


def test_dsl_trueliteral_constructor_args():
    sig = inspect.signature(dSL_TrueLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "t" in params, "Missing parameter 't'"

def test_dsl_trueliteral_has_t():
    assert hasattr(dSL_TrueLiteral, "t")
    descriptor = None
    for klass in dSL_TrueLiteral.__mro__:
        if "t" in klass.__dict__:
            descriptor = klass.__dict__["t"]
            break
    assert isinstance(descriptor, property)



def test_dsl_edgeliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_EdgeLiteral)


def test_dsl_edgeliteral_constructor_exists():
    assert callable(dSL_EdgeLiteral.__init__)


def test_dsl_edgeliteral_constructor_args():
    sig = inspect.signature(dSL_EdgeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "edge" in params, "Missing parameter 'edge'"

def test_dsl_edgeliteral_has_edge():
    assert hasattr(dSL_EdgeLiteral, "edge")
    descriptor = None
    for klass in dSL_EdgeLiteral.__mro__:
        if "edge" in klass.__dict__:
            descriptor = klass.__dict__["edge"]
            break
    assert isinstance(descriptor, property)



def test_dsl_distanceliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_DistanceLiteral)


def test_dsl_distanceliteral_constructor_exists():
    assert callable(dSL_DistanceLiteral.__init__)


def test_dsl_distanceliteral_constructor_args():
    sig = inspect.signature(dSL_DistanceLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_dsl_distanceliteral_has_distance():
    assert hasattr(dSL_DistanceLiteral, "distance")
    descriptor = None
    for klass in dSL_DistanceLiteral.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_dsl_colorliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_ColorLiteral)


def test_dsl_colorliteral_constructor_exists():
    assert callable(dSL_ColorLiteral.__init__)


def test_dsl_colorliteral_constructor_args():
    sig = inspect.signature(dSL_ColorLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_dsl_colorliteral_has_color():
    assert hasattr(dSL_ColorLiteral, "color")
    descriptor = None
    for klass in dSL_ColorLiteral.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_dsl_touchliteral_is_not_abstract():
    assert not inspect.isabstract(dSL_TouchLiteral)


def test_dsl_touchliteral_constructor_exists():
    assert callable(dSL_TouchLiteral.__init__)


def test_dsl_touchliteral_constructor_args():
    sig = inspect.signature(dSL_TouchLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "touch" in params, "Missing parameter 'touch'"

def test_dsl_touchliteral_has_touch():
    assert hasattr(dSL_TouchLiteral, "touch")
    descriptor = None
    for klass in dSL_TouchLiteral.__mro__:
        if "touch" in klass.__dict__:
            descriptor = klass.__dict__["touch"]
            break
    assert isinstance(descriptor, property)



def test_dsl_movementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_MovementAction)


def test_dsl_movementaction_constructor_exists():
    assert callable(dSL_MovementAction.__init__)


def test_dsl_movementaction_constructor_args():
    sig = inspect.signature(dSL_MovementAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionenum" in params, "Missing parameter 'actionenum'"

def test_dsl_movementaction_has_actionenum():
    assert hasattr(dSL_MovementAction, "actionenum")
    descriptor = None
    for klass in dSL_MovementAction.__mro__:
        if "actionenum" in klass.__dict__:
            descriptor = klass.__dict__["actionenum"]
            break
    assert isinstance(descriptor, property)



def test_actions_is_not_abstract():
    assert not inspect.isabstract(Actions)


def test_actions_constructor_exists():
    assert callable(Actions.__init__)


def test_actions_constructor_args():
    sig = inspect.signature(Actions.__init__)
    params = list(sig.parameters.keys())



def test_dsl_leftmovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_LeftMovementAction)


def test_dsl_leftmovementaction_constructor_exists():
    assert callable(dSL_LeftMovementAction.__init__)


def test_dsl_leftmovementaction_constructor_args():
    sig = inspect.signature(dSL_LeftMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_dsl_measurementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_MeasurementAction)


def test_dsl_measurementaction_constructor_exists():
    assert callable(dSL_MeasurementAction.__init__)


def test_dsl_measurementaction_constructor_args():
    sig = inspect.signature(dSL_MeasurementAction.__init__)
    params = list(sig.parameters.keys())
    assert "measure" in params, "Missing parameter 'measure'"

def test_dsl_measurementaction_has_measure():
    assert hasattr(dSL_MeasurementAction, "measure")
    descriptor = None
    for klass in dSL_MeasurementAction.__mro__:
        if "measure" in klass.__dict__:
            descriptor = klass.__dict__["measure"]
            break
    assert isinstance(descriptor, property)



def test_dsl_moveaction_is_not_abstract():
    assert not inspect.isabstract(dSL_MoveAction)


def test_dsl_moveaction_constructor_exists():
    assert callable(dSL_MoveAction.__init__)


def test_dsl_moveaction_constructor_args():
    sig = inspect.signature(dSL_MoveAction.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_dsl_moveaction_has_dir():
    assert hasattr(dSL_MoveAction, "dir")
    descriptor = None
    for klass in dSL_MoveAction.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_dsl_actions_is_not_abstract():
    assert not inspect.isabstract(dSL_Actions)


def test_dsl_actions_constructor_exists():
    assert callable(dSL_Actions.__init__)


def test_dsl_actions_constructor_args():
    sig = inspect.signature(dSL_Actions.__init__)
    params = list(sig.parameters.keys())



def test_dsl_expression_is_not_abstract():
    assert not inspect.isabstract(dSL_Expression)


def test_dsl_expression_constructor_exists():
    assert callable(dSL_Expression.__init__)


def test_dsl_expression_constructor_args():
    sig = inspect.signature(dSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_rotatepoints_is_not_abstract():
    assert not inspect.isabstract(RotatePoints)


def test_rotatepoints_constructor_exists():
    assert callable(RotatePoints.__init__)


def test_rotatepoints_constructor_args():
    sig = inspect.signature(RotatePoints.__init__)
    params = list(sig.parameters.keys())



def test_dsl_rightrotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL_RightRotatePoint)


def test_dsl_rightrotatepoint_constructor_exists():
    assert callable(dSL_RightRotatePoint.__init__)


def test_dsl_rightrotatepoint_constructor_args():
    sig = inspect.signature(dSL_RightRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "rightdir" in params, "Missing parameter 'rightdir'"

def test_dsl_rightrotatepoint_has_rightdir():
    assert hasattr(dSL_RightRotatePoint, "rightdir")
    descriptor = None
    for klass in dSL_RightRotatePoint.__mro__:
        if "rightdir" in klass.__dict__:
            descriptor = klass.__dict__["rightdir"]
            break
    assert isinstance(descriptor, property)



def test_dsl_middlerotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL_MiddleRotatePoint)


def test_dsl_middlerotatepoint_constructor_exists():
    assert callable(dSL_MiddleRotatePoint.__init__)


def test_dsl_middlerotatepoint_constructor_args():
    sig = inspect.signature(dSL_MiddleRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "middledir" in params, "Missing parameter 'middledir'"

def test_dsl_middlerotatepoint_has_middledir():
    assert hasattr(dSL_MiddleRotatePoint, "middledir")
    descriptor = None
    for klass in dSL_MiddleRotatePoint.__mro__:
        if "middledir" in klass.__dict__:
            descriptor = klass.__dict__["middledir"]
            break
    assert isinstance(descriptor, property)



def test_dsl_leftrotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL_LeftRotatePoint)


def test_dsl_leftrotatepoint_constructor_exists():
    assert callable(dSL_LeftRotatePoint.__init__)


def test_dsl_leftrotatepoint_constructor_args():
    sig = inspect.signature(dSL_LeftRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "leftdir" in params, "Missing parameter 'leftdir'"

def test_dsl_leftrotatepoint_has_leftdir():
    assert hasattr(dSL_LeftRotatePoint, "leftdir")
    descriptor = None
    for klass in dSL_LeftRotatePoint.__mro__:
        if "leftdir" in klass.__dict__:
            descriptor = klass.__dict__["leftdir"]
            break
    assert isinstance(descriptor, property)



def test_rotatemovementaction_is_not_abstract():
    assert not inspect.isabstract(RotateMovementAction)


def test_rotatemovementaction_constructor_exists():
    assert callable(RotateMovementAction.__init__)


def test_rotatemovementaction_constructor_args():
    sig = inspect.signature(RotateMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_dsl_rotatepoints_is_not_abstract():
    assert not inspect.isabstract(dSL_RotatePoints)


def test_dsl_rotatepoints_constructor_exists():
    assert callable(dSL_RotatePoints.__init__)


def test_dsl_rotatepoints_constructor_args():
    sig = inspect.signature(dSL_RotatePoints.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_dsl_rotatepoints_has_degrees():
    assert hasattr(dSL_RotatePoints, "degrees")
    descriptor = None
    for klass in dSL_RotatePoints.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_dsl_rotatemovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_RotateMovementAction)


def test_dsl_rotatemovementaction_constructor_exists():
    assert callable(dSL_RotateMovementAction.__init__)


def test_dsl_rotatemovementaction_constructor_args():
    sig = inspect.signature(dSL_RotateMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_dsl_rightmovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL_RightMovementAction)


def test_dsl_rightmovementaction_constructor_exists():
    assert callable(dSL_RightMovementAction.__init__)


def test_dsl_rightmovementaction_constructor_args():
    sig = inspect.signature(dSL_RightMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_dsl_behavior_is_not_abstract():
    assert not inspect.isabstract(dSL_Behavior)


def test_dsl_behavior_constructor_exists():
    assert callable(dSL_Behavior.__init__)


def test_dsl_behavior_constructor_args():
    sig = inspect.signature(dSL_Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_behavior_has_name():
    assert hasattr(dSL_Behavior, "name")
    descriptor = None
    for klass in dSL_Behavior.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_mission_is_not_abstract():
    assert not inspect.isabstract(dSL_Mission)


def test_dsl_mission_constructor_exists():
    assert callable(dSL_Mission.__init__)


def test_dsl_mission_constructor_args():
    sig = inspect.signature(dSL_Mission.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_mission_has_name():
    assert hasattr(dSL_Mission, "name")
    descriptor = None
    for klass in dSL_Mission.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_marsroverexpedition_is_not_abstract():
    assert not inspect.isabstract(dSL_MarsRoverExpedition)


def test_dsl_marsroverexpedition_constructor_exists():
    assert callable(dSL_MarsRoverExpedition.__init__)


def test_dsl_marsroverexpedition_constructor_args():
    sig = inspect.signature(dSL_MarsRoverExpedition.__init__)
    params = list(sig.parameters.keys())



def test_endcondition_is_not_abstract():
    assert not inspect.isabstract(EndCondition)


def test_endcondition_constructor_exists():
    assert callable(EndCondition.__init__)


def test_endcondition_constructor_args():
    sig = inspect.signature(EndCondition.__init__)
    params = list(sig.parameters.keys())



def test_dsl_endafter_is_not_abstract():
    assert not inspect.isabstract(dSL_EndAfter)


def test_dsl_endafter_constructor_exists():
    assert callable(dSL_EndAfter.__init__)


def test_dsl_endafter_constructor_args():
    sig = inspect.signature(dSL_EndAfter.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_dsl_endafter_has_time():
    assert hasattr(dSL_EndAfter, "time")
    descriptor = None
    for klass in dSL_EndAfter.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_dsl_endwhen_is_not_abstract():
    assert not inspect.isabstract(dSL_EndWhen)


def test_dsl_endwhen_constructor_exists():
    assert callable(dSL_EndWhen.__init__)


def test_dsl_endwhen_constructor_args():
    sig = inspect.signature(dSL_EndWhen.__init__)
    params = list(sig.parameters.keys())
    assert "times" in params, "Missing parameter 'times'"
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_endwhen_has_times():
    assert hasattr(dSL_EndWhen, "times")
    descriptor = None
    for klass in dSL_EndWhen.__mro__:
        if "times" in klass.__dict__:
            descriptor = klass.__dict__["times"]
            break
    assert isinstance(descriptor, property)

def test_dsl_endwhen_has_name():
    assert hasattr(dSL_EndWhen, "name")
    descriptor = None
    for klass in dSL_EndWhen.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl_endcondition_is_not_abstract():
    assert not inspect.isabstract(dSL_EndCondition)


def test_dsl_endcondition_constructor_exists():
    assert callable(dSL_EndCondition.__init__)


def test_dsl_endcondition_constructor_args():
    sig = inspect.signature(dSL_EndCondition.__init__)
    params = list(sig.parameters.keys())



def test_dsl_behaviorname_is_not_abstract():
    assert not inspect.isabstract(dSL_BehaviorName)


def test_dsl_behaviorname_constructor_exists():
    assert callable(dSL_BehaviorName.__init__)


def test_dsl_behaviorname_constructor_args():
    sig = inspect.signature(dSL_BehaviorName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl_behaviorname_has_name():
    assert hasattr(dSL_BehaviorName, "name")
    descriptor = None
    for klass in dSL_BehaviorName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_actionenum_exists():
    # Check that the Enumeration exists
    assert ActionEnum is not None

def test_actionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionEnum]
    expected_literals = [
        "FORWARD",
        "BACKWARD",
        "STOP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ActionEnum"

def test_tenum_exists():
    # Check that the Enumeration exists
    assert Tenum is not None

def test_tenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Tenum]
    expected_literals = [
        "TRUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Tenum"

def test_edgeenum_exists():
    # Check that the Enumeration exists
    assert EdgeEnum is not None

def test_edgeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeEnum]
    expected_literals = [
        "BACK",
        "FRONTLEFT",
        "FRONTRIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeEnum"

def test_touchenum_exists():
    # Check that the Enumeration exists
    assert TouchEnum is not None

def test_touchenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TouchEnum]
    expected_literals = [
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TouchEnum"

def test_backenum_exists():
    # Check that the Enumeration exists
    assert BackEnum is not None

def test_backenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BackEnum]
    expected_literals = [
        "BACK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BackEnum"

def test_lrenum_exists():
    # Check that the Enumeration exists
    assert LREnum is not None

def test_lrenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LREnum]
    expected_literals = [
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LREnum"

def test_fbenum_exists():
    # Check that the Enumeration exists
    assert FBEnum is not None

def test_fbenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FBEnum]
    expected_literals = [
        "FORWARD",
        "BACKWARD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FBEnum"

def test_colorenum_exists():
    # Check that the Enumeration exists
    assert ColorEnum is not None

def test_colorenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorEnum]
    expected_literals = [
        "YELLOW",
        "GREEN",
        "WHITE",
        "BLACK",
        "BROWN",
        "NONE",
        "BLUE",
        "RED",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorEnum"

def test_maenum_exists():
    # Check that the Enumeration exists
    assert MAEnum is not None

def test_maenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MAEnum]
    expected_literals = [
        "MEASURE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MAEnum"


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
Expression_strategy = st.builds(
    Expression,
)
dSL_ORexpression_strategy = st.builds(
    dSL_ORexpression,
)
dSL_DepthLiteral_strategy = st.builds(
    dSL_DepthLiteral,
    back=
        safe_text
)
dSL_ANDexpression_strategy = st.builds(
    dSL_ANDexpression,
)
dSL_ExpressionBracket_strategy = st.builds(
    dSL_ExpressionBracket,
)
dSL_TrueLiteral_strategy = st.builds(
    dSL_TrueLiteral,
    t=
        safe_text
)
dSL_EdgeLiteral_strategy = st.builds(
    dSL_EdgeLiteral,
    edge=
        safe_text
)
dSL_DistanceLiteral_strategy = st.builds(
    dSL_DistanceLiteral,
    distance=
        st.integers()
)
dSL_ColorLiteral_strategy = st.builds(
    dSL_ColorLiteral,
    color=
        safe_text
)
dSL_TouchLiteral_strategy = st.builds(
    dSL_TouchLiteral,
    touch=
        safe_text
)
dSL_MovementAction_strategy = st.builds(
    dSL_MovementAction,
    actionenum=
        safe_text
)
Actions_strategy = st.builds(
    Actions,
)
dSL_LeftMovementAction_strategy = st.builds(
    dSL_LeftMovementAction,
)
dSL_MeasurementAction_strategy = st.builds(
    dSL_MeasurementAction,
    measure=
        safe_text
)
dSL_MoveAction_strategy = st.builds(
    dSL_MoveAction,
    dir=
        safe_text
)
dSL_Actions_strategy = st.builds(
    dSL_Actions,
)
dSL_Expression_strategy = st.builds(
    dSL_Expression,
)
RotatePoints_strategy = st.builds(
    RotatePoints,
)
dSL_RightRotatePoint_strategy = st.builds(
    dSL_RightRotatePoint,
    rightdir=
        safe_text
)
dSL_MiddleRotatePoint_strategy = st.builds(
    dSL_MiddleRotatePoint,
    middledir=
        safe_text
)
dSL_LeftRotatePoint_strategy = st.builds(
    dSL_LeftRotatePoint,
    leftdir=
        safe_text
)
RotateMovementAction_strategy = st.builds(
    RotateMovementAction,
)
dSL_RotatePoints_strategy = st.builds(
    dSL_RotatePoints,
    degrees=
        st.integers()
)
dSL_RotateMovementAction_strategy = st.builds(
    dSL_RotateMovementAction,
)
dSL_RightMovementAction_strategy = st.builds(
    dSL_RightMovementAction,
)
dSL_Behavior_strategy = st.builds(
    dSL_Behavior,
    name=
        safe_text
)
dSL_Mission_strategy = st.builds(
    dSL_Mission,
    name=
        safe_text
)
dSL_MarsRoverExpedition_strategy = st.builds(
    dSL_MarsRoverExpedition,
)
EndCondition_strategy = st.builds(
    EndCondition,
)
dSL_EndAfter_strategy = st.builds(
    dSL_EndAfter,
    time=
        st.integers()
)
dSL_EndWhen_strategy = st.builds(
    dSL_EndWhen,
    times=
        st.integers(),
    name=
        safe_text
)
dSL_EndCondition_strategy = st.builds(
    dSL_EndCondition,
)
dSL_BehaviorName_strategy = st.builds(
    dSL_BehaviorName,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dSL_ORexpression_strategy)
@settings(max_examples=50)
def test_dsl_orexpression_instantiation(instance):
    assert isinstance(instance, dSL_ORexpression)

@given(instance=dSL_DepthLiteral_strategy)
@settings(max_examples=50)
def test_dsl_depthliteral_instantiation(instance):
    assert isinstance(instance, dSL_DepthLiteral)



@given(instance=dSL_DepthLiteral_strategy)
def test_dsl_depthliteral_back_setter(instance):
    original = instance.back
    instance.back = original
    assert instance.back == original

@given(instance=dSL_ANDexpression_strategy)
@settings(max_examples=50)
def test_dsl_andexpression_instantiation(instance):
    assert isinstance(instance, dSL_ANDexpression)

@given(instance=dSL_ExpressionBracket_strategy)
@settings(max_examples=50)
def test_dsl_expressionbracket_instantiation(instance):
    assert isinstance(instance, dSL_ExpressionBracket)

@given(instance=dSL_TrueLiteral_strategy)
@settings(max_examples=50)
def test_dsl_trueliteral_instantiation(instance):
    assert isinstance(instance, dSL_TrueLiteral)



@given(instance=dSL_TrueLiteral_strategy)
def test_dsl_trueliteral_t_setter(instance):
    original = instance.t
    instance.t = original
    assert instance.t == original

@given(instance=dSL_EdgeLiteral_strategy)
@settings(max_examples=50)
def test_dsl_edgeliteral_instantiation(instance):
    assert isinstance(instance, dSL_EdgeLiteral)



@given(instance=dSL_EdgeLiteral_strategy)
def test_dsl_edgeliteral_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original

@given(instance=dSL_DistanceLiteral_strategy)
@settings(max_examples=50)
def test_dsl_distanceliteral_instantiation(instance):
    assert isinstance(instance, dSL_DistanceLiteral)



@given(instance=dSL_DistanceLiteral_strategy)
def test_dsl_distanceliteral_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=dSL_ColorLiteral_strategy)
@settings(max_examples=50)
def test_dsl_colorliteral_instantiation(instance):
    assert isinstance(instance, dSL_ColorLiteral)



@given(instance=dSL_ColorLiteral_strategy)
def test_dsl_colorliteral_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=dSL_TouchLiteral_strategy)
@settings(max_examples=50)
def test_dsl_touchliteral_instantiation(instance):
    assert isinstance(instance, dSL_TouchLiteral)



@given(instance=dSL_TouchLiteral_strategy)
def test_dsl_touchliteral_touch_setter(instance):
    original = instance.touch
    instance.touch = original
    assert instance.touch == original

@given(instance=dSL_MovementAction_strategy)
@settings(max_examples=50)
def test_dsl_movementaction_instantiation(instance):
    assert isinstance(instance, dSL_MovementAction)



@given(instance=dSL_MovementAction_strategy)
def test_dsl_movementaction_actionenum_setter(instance):
    original = instance.actionenum
    instance.actionenum = original
    assert instance.actionenum == original

@given(instance=Actions_strategy)
@settings(max_examples=50)
def test_actions_instantiation(instance):
    assert isinstance(instance, Actions)

@given(instance=dSL_LeftMovementAction_strategy)
@settings(max_examples=50)
def test_dsl_leftmovementaction_instantiation(instance):
    assert isinstance(instance, dSL_LeftMovementAction)

@given(instance=dSL_MeasurementAction_strategy)
@settings(max_examples=50)
def test_dsl_measurementaction_instantiation(instance):
    assert isinstance(instance, dSL_MeasurementAction)



@given(instance=dSL_MeasurementAction_strategy)
def test_dsl_measurementaction_measure_setter(instance):
    original = instance.measure
    instance.measure = original
    assert instance.measure == original

@given(instance=dSL_MoveAction_strategy)
@settings(max_examples=50)
def test_dsl_moveaction_instantiation(instance):
    assert isinstance(instance, dSL_MoveAction)



@given(instance=dSL_MoveAction_strategy)
def test_dsl_moveaction_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=dSL_Actions_strategy)
@settings(max_examples=50)
def test_dsl_actions_instantiation(instance):
    assert isinstance(instance, dSL_Actions)

@given(instance=dSL_Expression_strategy)
@settings(max_examples=50)
def test_dsl_expression_instantiation(instance):
    assert isinstance(instance, dSL_Expression)

@given(instance=RotatePoints_strategy)
@settings(max_examples=50)
def test_rotatepoints_instantiation(instance):
    assert isinstance(instance, RotatePoints)

@given(instance=dSL_RightRotatePoint_strategy)
@settings(max_examples=50)
def test_dsl_rightrotatepoint_instantiation(instance):
    assert isinstance(instance, dSL_RightRotatePoint)



@given(instance=dSL_RightRotatePoint_strategy)
def test_dsl_rightrotatepoint_rightdir_setter(instance):
    original = instance.rightdir
    instance.rightdir = original
    assert instance.rightdir == original

@given(instance=dSL_MiddleRotatePoint_strategy)
@settings(max_examples=50)
def test_dsl_middlerotatepoint_instantiation(instance):
    assert isinstance(instance, dSL_MiddleRotatePoint)



@given(instance=dSL_MiddleRotatePoint_strategy)
def test_dsl_middlerotatepoint_middledir_setter(instance):
    original = instance.middledir
    instance.middledir = original
    assert instance.middledir == original

@given(instance=dSL_LeftRotatePoint_strategy)
@settings(max_examples=50)
def test_dsl_leftrotatepoint_instantiation(instance):
    assert isinstance(instance, dSL_LeftRotatePoint)



@given(instance=dSL_LeftRotatePoint_strategy)
def test_dsl_leftrotatepoint_leftdir_setter(instance):
    original = instance.leftdir
    instance.leftdir = original
    assert instance.leftdir == original

@given(instance=RotateMovementAction_strategy)
@settings(max_examples=50)
def test_rotatemovementaction_instantiation(instance):
    assert isinstance(instance, RotateMovementAction)

@given(instance=dSL_RotatePoints_strategy)
@settings(max_examples=50)
def test_dsl_rotatepoints_instantiation(instance):
    assert isinstance(instance, dSL_RotatePoints)



@given(instance=dSL_RotatePoints_strategy)
def test_dsl_rotatepoints_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=dSL_RotateMovementAction_strategy)
@settings(max_examples=50)
def test_dsl_rotatemovementaction_instantiation(instance):
    assert isinstance(instance, dSL_RotateMovementAction)

@given(instance=dSL_RightMovementAction_strategy)
@settings(max_examples=50)
def test_dsl_rightmovementaction_instantiation(instance):
    assert isinstance(instance, dSL_RightMovementAction)

@given(instance=dSL_Behavior_strategy)
@settings(max_examples=50)
def test_dsl_behavior_instantiation(instance):
    assert isinstance(instance, dSL_Behavior)



@given(instance=dSL_Behavior_strategy)
def test_dsl_behavior_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dSL_Mission_strategy)
@settings(max_examples=50)
def test_dsl_mission_instantiation(instance):
    assert isinstance(instance, dSL_Mission)



@given(instance=dSL_Mission_strategy)
def test_dsl_mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dSL_MarsRoverExpedition_strategy)
@settings(max_examples=50)
def test_dsl_marsroverexpedition_instantiation(instance):
    assert isinstance(instance, dSL_MarsRoverExpedition)

@given(instance=EndCondition_strategy)
@settings(max_examples=50)
def test_endcondition_instantiation(instance):
    assert isinstance(instance, EndCondition)

@given(instance=dSL_EndAfter_strategy)
@settings(max_examples=50)
def test_dsl_endafter_instantiation(instance):
    assert isinstance(instance, dSL_EndAfter)



@given(instance=dSL_EndAfter_strategy)
def test_dsl_endafter_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=dSL_EndWhen_strategy)
@settings(max_examples=50)
def test_dsl_endwhen_instantiation(instance):
    assert isinstance(instance, dSL_EndWhen)



@given(instance=dSL_EndWhen_strategy)
def test_dsl_endwhen_times_setter(instance):
    original = instance.times
    instance.times = original
    assert instance.times == original



@given(instance=dSL_EndWhen_strategy)
def test_dsl_endwhen_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dSL_EndCondition_strategy)
@settings(max_examples=50)
def test_dsl_endcondition_instantiation(instance):
    assert isinstance(instance, dSL_EndCondition)

@given(instance=dSL_BehaviorName_strategy)
@settings(max_examples=50)
def test_dsl_behaviorname_instantiation(instance):
    assert isinstance(instance, dSL_BehaviorName)



@given(instance=dSL_BehaviorName_strategy)
def test_dsl_behaviorname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
