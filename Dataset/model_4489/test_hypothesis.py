import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Expression,
    dSL::ExpressionBracket,
    dSL::ORexpression,
    dSL::DepthLiteral,
    dSL::ANDexpression,
    dSL::TrueLiteral,
    dSL::EdgeLiteral,
    dSL::DistanceLiteral,
    dSL::ColorLiteral,
    dSL::TouchLiteral,
    dSL::MovementAction,
    Actions,
    dSL::LeftMovementAction,
    dSL::MeasurementAction,
    dSL::MoveAction,
    dSL::Actions,
    dSL::Expression,
    RotatePoints,
    dSL::RightRotatePoint,
    dSL::MiddleRotatePoint,
    dSL::LeftRotatePoint,
    RotateMovementAction,
    dSL::RotatePoints,
    dSL::RotateMovementAction,
    dSL::RightMovementAction,
    dSL::Behavior,
    dSL::Mission,
    dSL::MarsRoverExpedition,
    EndCondition,
    dSL::EndAfter,
    dSL::EndWhen,
    dSL::EndCondition,
    dSL::BehaviorName,
    MAEnum,
    BackEnum,
    EdgeEnum,
    FBEnum,
    TouchEnum,
    ColorEnum,
    ActionEnum,
    Tenum,
    LREnum,
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



def test_dsl::expressionbracket_is_not_abstract():
    assert not inspect.isabstract(dSL::ExpressionBracket)


def test_dsl::expressionbracket_constructor_exists():
    assert callable(dSL::ExpressionBracket.__init__)


def test_dsl::expressionbracket_constructor_args():
    sig = inspect.signature(dSL::ExpressionBracket.__init__)
    params = list(sig.parameters.keys())



def test_dsl::orexpression_is_not_abstract():
    assert not inspect.isabstract(dSL::ORexpression)


def test_dsl::orexpression_constructor_exists():
    assert callable(dSL::ORexpression.__init__)


def test_dsl::orexpression_constructor_args():
    sig = inspect.signature(dSL::ORexpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::depthliteral_is_not_abstract():
    assert not inspect.isabstract(dSL::DepthLiteral)


def test_dsl::depthliteral_constructor_exists():
    assert callable(dSL::DepthLiteral.__init__)


def test_dsl::depthliteral_constructor_args():
    sig = inspect.signature(dSL::DepthLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "back" in params, "Missing parameter 'back'"

def test_dsl::depthliteral_has_back():
    assert hasattr(dSL::DepthLiteral, "back")
    descriptor = None
    for klass in dSL::DepthLiteral.__mro__:
        if "back" in klass.__dict__:
            descriptor = klass.__dict__["back"]
            break
    assert isinstance(descriptor, property)



def test_dsl::andexpression_is_not_abstract():
    assert not inspect.isabstract(dSL::ANDexpression)


def test_dsl::andexpression_constructor_exists():
    assert callable(dSL::ANDexpression.__init__)


def test_dsl::andexpression_constructor_args():
    sig = inspect.signature(dSL::ANDexpression.__init__)
    params = list(sig.parameters.keys())



def test_dsl::trueliteral_is_not_abstract():
    assert not inspect.isabstract(dSL::TrueLiteral)


def test_dsl::trueliteral_constructor_exists():
    assert callable(dSL::TrueLiteral.__init__)


def test_dsl::trueliteral_constructor_args():
    sig = inspect.signature(dSL::TrueLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "t" in params, "Missing parameter 't'"

def test_dsl::trueliteral_has_t():
    assert hasattr(dSL::TrueLiteral, "t")
    descriptor = None
    for klass in dSL::TrueLiteral.__mro__:
        if "t" in klass.__dict__:
            descriptor = klass.__dict__["t"]
            break
    assert isinstance(descriptor, property)



def test_dsl::edgeliteral_is_not_abstract():
    assert not inspect.isabstract(dSL::EdgeLiteral)


def test_dsl::edgeliteral_constructor_exists():
    assert callable(dSL::EdgeLiteral.__init__)


def test_dsl::edgeliteral_constructor_args():
    sig = inspect.signature(dSL::EdgeLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "edge" in params, "Missing parameter 'edge'"

def test_dsl::edgeliteral_has_edge():
    assert hasattr(dSL::EdgeLiteral, "edge")
    descriptor = None
    for klass in dSL::EdgeLiteral.__mro__:
        if "edge" in klass.__dict__:
            descriptor = klass.__dict__["edge"]
            break
    assert isinstance(descriptor, property)



def test_dsl::distanceliteral_is_not_abstract():
    assert not inspect.isabstract(dSL::DistanceLiteral)


def test_dsl::distanceliteral_constructor_exists():
    assert callable(dSL::DistanceLiteral.__init__)


def test_dsl::distanceliteral_constructor_args():
    sig = inspect.signature(dSL::DistanceLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "distance" in params, "Missing parameter 'distance'"

def test_dsl::distanceliteral_has_distance():
    assert hasattr(dSL::DistanceLiteral, "distance")
    descriptor = None
    for klass in dSL::DistanceLiteral.__mro__:
        if "distance" in klass.__dict__:
            descriptor = klass.__dict__["distance"]
            break
    assert isinstance(descriptor, property)



def test_dsl::colorliteral_is_not_abstract():
    assert not inspect.isabstract(dSL::ColorLiteral)


def test_dsl::colorliteral_constructor_exists():
    assert callable(dSL::ColorLiteral.__init__)


def test_dsl::colorliteral_constructor_args():
    sig = inspect.signature(dSL::ColorLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_dsl::colorliteral_has_color():
    assert hasattr(dSL::ColorLiteral, "color")
    descriptor = None
    for klass in dSL::ColorLiteral.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_dsl::touchliteral_is_not_abstract():
    assert not inspect.isabstract(dSL::TouchLiteral)


def test_dsl::touchliteral_constructor_exists():
    assert callable(dSL::TouchLiteral.__init__)


def test_dsl::touchliteral_constructor_args():
    sig = inspect.signature(dSL::TouchLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "touch" in params, "Missing parameter 'touch'"

def test_dsl::touchliteral_has_touch():
    assert hasattr(dSL::TouchLiteral, "touch")
    descriptor = None
    for klass in dSL::TouchLiteral.__mro__:
        if "touch" in klass.__dict__:
            descriptor = klass.__dict__["touch"]
            break
    assert isinstance(descriptor, property)



def test_dsl::movementaction_is_not_abstract():
    assert not inspect.isabstract(dSL::MovementAction)


def test_dsl::movementaction_constructor_exists():
    assert callable(dSL::MovementAction.__init__)


def test_dsl::movementaction_constructor_args():
    sig = inspect.signature(dSL::MovementAction.__init__)
    params = list(sig.parameters.keys())
    assert "actionenum" in params, "Missing parameter 'actionenum'"

def test_dsl::movementaction_has_actionenum():
    assert hasattr(dSL::MovementAction, "actionenum")
    descriptor = None
    for klass in dSL::MovementAction.__mro__:
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



def test_dsl::leftmovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL::LeftMovementAction)


def test_dsl::leftmovementaction_constructor_exists():
    assert callable(dSL::LeftMovementAction.__init__)


def test_dsl::leftmovementaction_constructor_args():
    sig = inspect.signature(dSL::LeftMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_dsl::measurementaction_is_not_abstract():
    assert not inspect.isabstract(dSL::MeasurementAction)


def test_dsl::measurementaction_constructor_exists():
    assert callable(dSL::MeasurementAction.__init__)


def test_dsl::measurementaction_constructor_args():
    sig = inspect.signature(dSL::MeasurementAction.__init__)
    params = list(sig.parameters.keys())
    assert "measure" in params, "Missing parameter 'measure'"

def test_dsl::measurementaction_has_measure():
    assert hasattr(dSL::MeasurementAction, "measure")
    descriptor = None
    for klass in dSL::MeasurementAction.__mro__:
        if "measure" in klass.__dict__:
            descriptor = klass.__dict__["measure"]
            break
    assert isinstance(descriptor, property)



def test_dsl::moveaction_is_not_abstract():
    assert not inspect.isabstract(dSL::MoveAction)


def test_dsl::moveaction_constructor_exists():
    assert callable(dSL::MoveAction.__init__)


def test_dsl::moveaction_constructor_args():
    sig = inspect.signature(dSL::MoveAction.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_dsl::moveaction_has_dir():
    assert hasattr(dSL::MoveAction, "dir")
    descriptor = None
    for klass in dSL::MoveAction.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_dsl::actions_is_not_abstract():
    assert not inspect.isabstract(dSL::Actions)


def test_dsl::actions_constructor_exists():
    assert callable(dSL::Actions.__init__)


def test_dsl::actions_constructor_args():
    sig = inspect.signature(dSL::Actions.__init__)
    params = list(sig.parameters.keys())



def test_dsl::expression_is_not_abstract():
    assert not inspect.isabstract(dSL::Expression)


def test_dsl::expression_constructor_exists():
    assert callable(dSL::Expression.__init__)


def test_dsl::expression_constructor_args():
    sig = inspect.signature(dSL::Expression.__init__)
    params = list(sig.parameters.keys())



def test_rotatepoints_is_not_abstract():
    assert not inspect.isabstract(RotatePoints)


def test_rotatepoints_constructor_exists():
    assert callable(RotatePoints.__init__)


def test_rotatepoints_constructor_args():
    sig = inspect.signature(RotatePoints.__init__)
    params = list(sig.parameters.keys())



def test_dsl::rightrotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL::RightRotatePoint)


def test_dsl::rightrotatepoint_constructor_exists():
    assert callable(dSL::RightRotatePoint.__init__)


def test_dsl::rightrotatepoint_constructor_args():
    sig = inspect.signature(dSL::RightRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "rightdir" in params, "Missing parameter 'rightdir'"

def test_dsl::rightrotatepoint_has_rightdir():
    assert hasattr(dSL::RightRotatePoint, "rightdir")
    descriptor = None
    for klass in dSL::RightRotatePoint.__mro__:
        if "rightdir" in klass.__dict__:
            descriptor = klass.__dict__["rightdir"]
            break
    assert isinstance(descriptor, property)



def test_dsl::middlerotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL::MiddleRotatePoint)


def test_dsl::middlerotatepoint_constructor_exists():
    assert callable(dSL::MiddleRotatePoint.__init__)


def test_dsl::middlerotatepoint_constructor_args():
    sig = inspect.signature(dSL::MiddleRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "middledir" in params, "Missing parameter 'middledir'"

def test_dsl::middlerotatepoint_has_middledir():
    assert hasattr(dSL::MiddleRotatePoint, "middledir")
    descriptor = None
    for klass in dSL::MiddleRotatePoint.__mro__:
        if "middledir" in klass.__dict__:
            descriptor = klass.__dict__["middledir"]
            break
    assert isinstance(descriptor, property)



def test_dsl::leftrotatepoint_is_not_abstract():
    assert not inspect.isabstract(dSL::LeftRotatePoint)


def test_dsl::leftrotatepoint_constructor_exists():
    assert callable(dSL::LeftRotatePoint.__init__)


def test_dsl::leftrotatepoint_constructor_args():
    sig = inspect.signature(dSL::LeftRotatePoint.__init__)
    params = list(sig.parameters.keys())
    assert "leftdir" in params, "Missing parameter 'leftdir'"

def test_dsl::leftrotatepoint_has_leftdir():
    assert hasattr(dSL::LeftRotatePoint, "leftdir")
    descriptor = None
    for klass in dSL::LeftRotatePoint.__mro__:
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



def test_dsl::rotatepoints_is_not_abstract():
    assert not inspect.isabstract(dSL::RotatePoints)


def test_dsl::rotatepoints_constructor_exists():
    assert callable(dSL::RotatePoints.__init__)


def test_dsl::rotatepoints_constructor_args():
    sig = inspect.signature(dSL::RotatePoints.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_dsl::rotatepoints_has_degrees():
    assert hasattr(dSL::RotatePoints, "degrees")
    descriptor = None
    for klass in dSL::RotatePoints.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_dsl::rotatemovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL::RotateMovementAction)


def test_dsl::rotatemovementaction_constructor_exists():
    assert callable(dSL::RotateMovementAction.__init__)


def test_dsl::rotatemovementaction_constructor_args():
    sig = inspect.signature(dSL::RotateMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_dsl::rightmovementaction_is_not_abstract():
    assert not inspect.isabstract(dSL::RightMovementAction)


def test_dsl::rightmovementaction_constructor_exists():
    assert callable(dSL::RightMovementAction.__init__)


def test_dsl::rightmovementaction_constructor_args():
    sig = inspect.signature(dSL::RightMovementAction.__init__)
    params = list(sig.parameters.keys())



def test_dsl::behavior_is_not_abstract():
    assert not inspect.isabstract(dSL::Behavior)


def test_dsl::behavior_constructor_exists():
    assert callable(dSL::Behavior.__init__)


def test_dsl::behavior_constructor_args():
    sig = inspect.signature(dSL::Behavior.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::behavior_has_name():
    assert hasattr(dSL::Behavior, "name")
    descriptor = None
    for klass in dSL::Behavior.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::mission_is_not_abstract():
    assert not inspect.isabstract(dSL::Mission)


def test_dsl::mission_constructor_exists():
    assert callable(dSL::Mission.__init__)


def test_dsl::mission_constructor_args():
    sig = inspect.signature(dSL::Mission.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::mission_has_name():
    assert hasattr(dSL::Mission, "name")
    descriptor = None
    for klass in dSL::Mission.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::marsroverexpedition_is_not_abstract():
    assert not inspect.isabstract(dSL::MarsRoverExpedition)


def test_dsl::marsroverexpedition_constructor_exists():
    assert callable(dSL::MarsRoverExpedition.__init__)


def test_dsl::marsroverexpedition_constructor_args():
    sig = inspect.signature(dSL::MarsRoverExpedition.__init__)
    params = list(sig.parameters.keys())



def test_endcondition_is_not_abstract():
    assert not inspect.isabstract(EndCondition)


def test_endcondition_constructor_exists():
    assert callable(EndCondition.__init__)


def test_endcondition_constructor_args():
    sig = inspect.signature(EndCondition.__init__)
    params = list(sig.parameters.keys())



def test_dsl::endafter_is_not_abstract():
    assert not inspect.isabstract(dSL::EndAfter)


def test_dsl::endafter_constructor_exists():
    assert callable(dSL::EndAfter.__init__)


def test_dsl::endafter_constructor_args():
    sig = inspect.signature(dSL::EndAfter.__init__)
    params = list(sig.parameters.keys())
    assert "time" in params, "Missing parameter 'time'"

def test_dsl::endafter_has_time():
    assert hasattr(dSL::EndAfter, "time")
    descriptor = None
    for klass in dSL::EndAfter.__mro__:
        if "time" in klass.__dict__:
            descriptor = klass.__dict__["time"]
            break
    assert isinstance(descriptor, property)



def test_dsl::endwhen_is_not_abstract():
    assert not inspect.isabstract(dSL::EndWhen)


def test_dsl::endwhen_constructor_exists():
    assert callable(dSL::EndWhen.__init__)


def test_dsl::endwhen_constructor_args():
    sig = inspect.signature(dSL::EndWhen.__init__)
    params = list(sig.parameters.keys())
    assert "times" in params, "Missing parameter 'times'"
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::endwhen_has_times():
    assert hasattr(dSL::EndWhen, "times")
    descriptor = None
    for klass in dSL::EndWhen.__mro__:
        if "times" in klass.__dict__:
            descriptor = klass.__dict__["times"]
            break
    assert isinstance(descriptor, property)

def test_dsl::endwhen_has_name():
    assert hasattr(dSL::EndWhen, "name")
    descriptor = None
    for klass in dSL::EndWhen.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_dsl::endcondition_is_not_abstract():
    assert not inspect.isabstract(dSL::EndCondition)


def test_dsl::endcondition_constructor_exists():
    assert callable(dSL::EndCondition.__init__)


def test_dsl::endcondition_constructor_args():
    sig = inspect.signature(dSL::EndCondition.__init__)
    params = list(sig.parameters.keys())



def test_dsl::behaviorname_is_not_abstract():
    assert not inspect.isabstract(dSL::BehaviorName)


def test_dsl::behaviorname_constructor_exists():
    assert callable(dSL::BehaviorName.__init__)


def test_dsl::behaviorname_constructor_args():
    sig = inspect.signature(dSL::BehaviorName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_dsl::behaviorname_has_name():
    assert hasattr(dSL::BehaviorName, "name")
    descriptor = None
    for klass in dSL::BehaviorName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

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

def test_edgeenum_exists():
    # Check that the Enumeration exists
    assert EdgeEnum is not None

def test_edgeenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EdgeEnum]
    expected_literals = [
        "BACK",
        "FRONTRIGHT",
        "FRONTLEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EdgeEnum"

def test_fbenum_exists():
    # Check that the Enumeration exists
    assert FBEnum is not None

def test_fbenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FBEnum]
    expected_literals = [
        "BACKWARD",
        "FORWARD",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FBEnum"

def test_touchenum_exists():
    # Check that the Enumeration exists
    assert TouchEnum is not None

def test_touchenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TouchEnum]
    expected_literals = [
        "LEFT",
        "RIGHT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TouchEnum"

def test_colorenum_exists():
    # Check that the Enumeration exists
    assert ColorEnum is not None

def test_colorenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ColorEnum]
    expected_literals = [
        "BLACK",
        "BROWN",
        "GREEN",
        "WHITE",
        "YELLOW",
        "RED",
        "NONE",
        "BLUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ColorEnum"

def test_actionenum_exists():
    # Check that the Enumeration exists
    assert ActionEnum is not None

def test_actionenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ActionEnum]
    expected_literals = [
        "BACKWARD",
        "FORWARD",
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

def test_lrenum_exists():
    # Check that the Enumeration exists
    assert LREnum is not None

def test_lrenum_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in LREnum]
    expected_literals = [
        "RIGHT",
        "LEFT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in LREnum"


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
dSL::ExpressionBracket_strategy = st.builds(
    dSL::ExpressionBracket,
)
dSL::ORexpression_strategy = st.builds(
    dSL::ORexpression,
)
dSL::DepthLiteral_strategy = st.builds(
    dSL::DepthLiteral,
    back=
        safe_text
)
dSL::ANDexpression_strategy = st.builds(
    dSL::ANDexpression,
)
dSL::TrueLiteral_strategy = st.builds(
    dSL::TrueLiteral,
    t=
        safe_text
)
dSL::EdgeLiteral_strategy = st.builds(
    dSL::EdgeLiteral,
    edge=
        safe_text
)
dSL::DistanceLiteral_strategy = st.builds(
    dSL::DistanceLiteral,
    distance=
        st.integers()
)
dSL::ColorLiteral_strategy = st.builds(
    dSL::ColorLiteral,
    color=
        safe_text
)
dSL::TouchLiteral_strategy = st.builds(
    dSL::TouchLiteral,
    touch=
        safe_text
)
dSL::MovementAction_strategy = st.builds(
    dSL::MovementAction,
    actionenum=
        safe_text
)
Actions_strategy = st.builds(
    Actions,
)
dSL::LeftMovementAction_strategy = st.builds(
    dSL::LeftMovementAction,
)
dSL::MeasurementAction_strategy = st.builds(
    dSL::MeasurementAction,
    measure=
        safe_text
)
dSL::MoveAction_strategy = st.builds(
    dSL::MoveAction,
    dir=
        safe_text
)
dSL::Actions_strategy = st.builds(
    dSL::Actions,
)
dSL::Expression_strategy = st.builds(
    dSL::Expression,
)
RotatePoints_strategy = st.builds(
    RotatePoints,
)
dSL::RightRotatePoint_strategy = st.builds(
    dSL::RightRotatePoint,
    rightdir=
        safe_text
)
dSL::MiddleRotatePoint_strategy = st.builds(
    dSL::MiddleRotatePoint,
    middledir=
        safe_text
)
dSL::LeftRotatePoint_strategy = st.builds(
    dSL::LeftRotatePoint,
    leftdir=
        safe_text
)
RotateMovementAction_strategy = st.builds(
    RotateMovementAction,
)
dSL::RotatePoints_strategy = st.builds(
    dSL::RotatePoints,
    degrees=
        st.integers()
)
dSL::RotateMovementAction_strategy = st.builds(
    dSL::RotateMovementAction,
)
dSL::RightMovementAction_strategy = st.builds(
    dSL::RightMovementAction,
)
dSL::Behavior_strategy = st.builds(
    dSL::Behavior,
    name=
        safe_text
)
dSL::Mission_strategy = st.builds(
    dSL::Mission,
    name=
        safe_text
)
dSL::MarsRoverExpedition_strategy = st.builds(
    dSL::MarsRoverExpedition,
)
EndCondition_strategy = st.builds(
    EndCondition,
)
dSL::EndAfter_strategy = st.builds(
    dSL::EndAfter,
    time=
        st.integers()
)
dSL::EndWhen_strategy = st.builds(
    dSL::EndWhen,
    times=
        st.integers(),
    name=
        safe_text
)
dSL::EndCondition_strategy = st.builds(
    dSL::EndCondition,
)
dSL::BehaviorName_strategy = st.builds(
    dSL::BehaviorName,
    name=
        safe_text
)

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=dSL::ExpressionBracket_strategy)
@settings(max_examples=50)
def test_dsl::expressionbracket_instantiation(instance):
    assert isinstance(instance, dSL::ExpressionBracket)

@given(instance=dSL::ORexpression_strategy)
@settings(max_examples=50)
def test_dsl::orexpression_instantiation(instance):
    assert isinstance(instance, dSL::ORexpression)

@given(instance=dSL::DepthLiteral_strategy)
@settings(max_examples=50)
def test_dsl::depthliteral_instantiation(instance):
    assert isinstance(instance, dSL::DepthLiteral)

@given(instance=dSL::DepthLiteral_strategy)
def test_dsl::depthliteral_back_type(instance):
    assert isinstance(instance.back, str)


@given(instance=dSL::DepthLiteral_strategy)
def test_dsl::depthliteral_back_setter(instance):
    original = instance.back
    instance.back = original
    assert instance.back == original

@given(instance=dSL::ANDexpression_strategy)
@settings(max_examples=50)
def test_dsl::andexpression_instantiation(instance):
    assert isinstance(instance, dSL::ANDexpression)

@given(instance=dSL::TrueLiteral_strategy)
@settings(max_examples=50)
def test_dsl::trueliteral_instantiation(instance):
    assert isinstance(instance, dSL::TrueLiteral)

@given(instance=dSL::TrueLiteral_strategy)
def test_dsl::trueliteral_t_type(instance):
    assert isinstance(instance.t, str)


@given(instance=dSL::TrueLiteral_strategy)
def test_dsl::trueliteral_t_setter(instance):
    original = instance.t
    instance.t = original
    assert instance.t == original

@given(instance=dSL::EdgeLiteral_strategy)
@settings(max_examples=50)
def test_dsl::edgeliteral_instantiation(instance):
    assert isinstance(instance, dSL::EdgeLiteral)

@given(instance=dSL::EdgeLiteral_strategy)
def test_dsl::edgeliteral_edge_type(instance):
    assert isinstance(instance.edge, str)


@given(instance=dSL::EdgeLiteral_strategy)
def test_dsl::edgeliteral_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original

@given(instance=dSL::DistanceLiteral_strategy)
@settings(max_examples=50)
def test_dsl::distanceliteral_instantiation(instance):
    assert isinstance(instance, dSL::DistanceLiteral)

@given(instance=dSL::DistanceLiteral_strategy)
def test_dsl::distanceliteral_distance_type(instance):
    assert isinstance(instance.distance, int)


@given(instance=dSL::DistanceLiteral_strategy)
def test_dsl::distanceliteral_distance_setter(instance):
    original = instance.distance
    instance.distance = original
    assert instance.distance == original

@given(instance=dSL::ColorLiteral_strategy)
@settings(max_examples=50)
def test_dsl::colorliteral_instantiation(instance):
    assert isinstance(instance, dSL::ColorLiteral)

@given(instance=dSL::ColorLiteral_strategy)
def test_dsl::colorliteral_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=dSL::ColorLiteral_strategy)
def test_dsl::colorliteral_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=dSL::TouchLiteral_strategy)
@settings(max_examples=50)
def test_dsl::touchliteral_instantiation(instance):
    assert isinstance(instance, dSL::TouchLiteral)

@given(instance=dSL::TouchLiteral_strategy)
def test_dsl::touchliteral_touch_type(instance):
    assert isinstance(instance.touch, str)


@given(instance=dSL::TouchLiteral_strategy)
def test_dsl::touchliteral_touch_setter(instance):
    original = instance.touch
    instance.touch = original
    assert instance.touch == original

@given(instance=dSL::MovementAction_strategy)
@settings(max_examples=50)
def test_dsl::movementaction_instantiation(instance):
    assert isinstance(instance, dSL::MovementAction)

@given(instance=dSL::MovementAction_strategy)
def test_dsl::movementaction_actionenum_type(instance):
    assert isinstance(instance.actionenum, str)


@given(instance=dSL::MovementAction_strategy)
def test_dsl::movementaction_actionenum_setter(instance):
    original = instance.actionenum
    instance.actionenum = original
    assert instance.actionenum == original

@given(instance=Actions_strategy)
@settings(max_examples=50)
def test_actions_instantiation(instance):
    assert isinstance(instance, Actions)

@given(instance=dSL::LeftMovementAction_strategy)
@settings(max_examples=50)
def test_dsl::leftmovementaction_instantiation(instance):
    assert isinstance(instance, dSL::LeftMovementAction)

@given(instance=dSL::MeasurementAction_strategy)
@settings(max_examples=50)
def test_dsl::measurementaction_instantiation(instance):
    assert isinstance(instance, dSL::MeasurementAction)

@given(instance=dSL::MeasurementAction_strategy)
def test_dsl::measurementaction_measure_type(instance):
    assert isinstance(instance.measure, str)


@given(instance=dSL::MeasurementAction_strategy)
def test_dsl::measurementaction_measure_setter(instance):
    original = instance.measure
    instance.measure = original
    assert instance.measure == original

@given(instance=dSL::MoveAction_strategy)
@settings(max_examples=50)
def test_dsl::moveaction_instantiation(instance):
    assert isinstance(instance, dSL::MoveAction)

@given(instance=dSL::MoveAction_strategy)
def test_dsl::moveaction_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=dSL::MoveAction_strategy)
def test_dsl::moveaction_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=dSL::Actions_strategy)
@settings(max_examples=50)
def test_dsl::actions_instantiation(instance):
    assert isinstance(instance, dSL::Actions)

@given(instance=dSL::Expression_strategy)
@settings(max_examples=50)
def test_dsl::expression_instantiation(instance):
    assert isinstance(instance, dSL::Expression)

@given(instance=RotatePoints_strategy)
@settings(max_examples=50)
def test_rotatepoints_instantiation(instance):
    assert isinstance(instance, RotatePoints)

@given(instance=dSL::RightRotatePoint_strategy)
@settings(max_examples=50)
def test_dsl::rightrotatepoint_instantiation(instance):
    assert isinstance(instance, dSL::RightRotatePoint)

@given(instance=dSL::RightRotatePoint_strategy)
def test_dsl::rightrotatepoint_rightdir_type(instance):
    assert isinstance(instance.rightdir, str)


@given(instance=dSL::RightRotatePoint_strategy)
def test_dsl::rightrotatepoint_rightdir_setter(instance):
    original = instance.rightdir
    instance.rightdir = original
    assert instance.rightdir == original

@given(instance=dSL::MiddleRotatePoint_strategy)
@settings(max_examples=50)
def test_dsl::middlerotatepoint_instantiation(instance):
    assert isinstance(instance, dSL::MiddleRotatePoint)

@given(instance=dSL::MiddleRotatePoint_strategy)
def test_dsl::middlerotatepoint_middledir_type(instance):
    assert isinstance(instance.middledir, str)


@given(instance=dSL::MiddleRotatePoint_strategy)
def test_dsl::middlerotatepoint_middledir_setter(instance):
    original = instance.middledir
    instance.middledir = original
    assert instance.middledir == original

@given(instance=dSL::LeftRotatePoint_strategy)
@settings(max_examples=50)
def test_dsl::leftrotatepoint_instantiation(instance):
    assert isinstance(instance, dSL::LeftRotatePoint)

@given(instance=dSL::LeftRotatePoint_strategy)
def test_dsl::leftrotatepoint_leftdir_type(instance):
    assert isinstance(instance.leftdir, str)


@given(instance=dSL::LeftRotatePoint_strategy)
def test_dsl::leftrotatepoint_leftdir_setter(instance):
    original = instance.leftdir
    instance.leftdir = original
    assert instance.leftdir == original

@given(instance=RotateMovementAction_strategy)
@settings(max_examples=50)
def test_rotatemovementaction_instantiation(instance):
    assert isinstance(instance, RotateMovementAction)

@given(instance=dSL::RotatePoints_strategy)
@settings(max_examples=50)
def test_dsl::rotatepoints_instantiation(instance):
    assert isinstance(instance, dSL::RotatePoints)

@given(instance=dSL::RotatePoints_strategy)
def test_dsl::rotatepoints_degrees_type(instance):
    assert isinstance(instance.degrees, int)


@given(instance=dSL::RotatePoints_strategy)
def test_dsl::rotatepoints_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=dSL::RotateMovementAction_strategy)
@settings(max_examples=50)
def test_dsl::rotatemovementaction_instantiation(instance):
    assert isinstance(instance, dSL::RotateMovementAction)

@given(instance=dSL::RightMovementAction_strategy)
@settings(max_examples=50)
def test_dsl::rightmovementaction_instantiation(instance):
    assert isinstance(instance, dSL::RightMovementAction)

@given(instance=dSL::Behavior_strategy)
@settings(max_examples=50)
def test_dsl::behavior_instantiation(instance):
    assert isinstance(instance, dSL::Behavior)

@given(instance=dSL::Behavior_strategy)
def test_dsl::behavior_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dSL::Behavior_strategy)
def test_dsl::behavior_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dSL::Mission_strategy)
@settings(max_examples=50)
def test_dsl::mission_instantiation(instance):
    assert isinstance(instance, dSL::Mission)

@given(instance=dSL::Mission_strategy)
def test_dsl::mission_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dSL::Mission_strategy)
def test_dsl::mission_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dSL::MarsRoverExpedition_strategy)
@settings(max_examples=50)
def test_dsl::marsroverexpedition_instantiation(instance):
    assert isinstance(instance, dSL::MarsRoverExpedition)

@given(instance=EndCondition_strategy)
@settings(max_examples=50)
def test_endcondition_instantiation(instance):
    assert isinstance(instance, EndCondition)

@given(instance=dSL::EndAfter_strategy)
@settings(max_examples=50)
def test_dsl::endafter_instantiation(instance):
    assert isinstance(instance, dSL::EndAfter)

@given(instance=dSL::EndAfter_strategy)
def test_dsl::endafter_time_type(instance):
    assert isinstance(instance.time, int)


@given(instance=dSL::EndAfter_strategy)
def test_dsl::endafter_time_setter(instance):
    original = instance.time
    instance.time = original
    assert instance.time == original

@given(instance=dSL::EndWhen_strategy)
@settings(max_examples=50)
def test_dsl::endwhen_instantiation(instance):
    assert isinstance(instance, dSL::EndWhen)

@given(instance=dSL::EndWhen_strategy)
def test_dsl::endwhen_times_type(instance):
    assert isinstance(instance.times, int)


@given(instance=dSL::EndWhen_strategy)
def test_dsl::endwhen_times_setter(instance):
    original = instance.times
    instance.times = original
    assert instance.times == original

@given(instance=dSL::EndWhen_strategy)
def test_dsl::endwhen_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dSL::EndWhen_strategy)
def test_dsl::endwhen_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=dSL::EndCondition_strategy)
@settings(max_examples=50)
def test_dsl::endcondition_instantiation(instance):
    assert isinstance(instance, dSL::EndCondition)

@given(instance=dSL::BehaviorName_strategy)
@settings(max_examples=50)
def test_dsl::behaviorname_instantiation(instance):
    assert isinstance(instance, dSL::BehaviorName)

@given(instance=dSL::BehaviorName_strategy)
def test_dsl::behaviorname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=dSL::BehaviorName_strategy)
def test_dsl::behaviorname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
