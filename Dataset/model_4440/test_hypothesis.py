import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    ValueExpression,
    roverDSL::BVBracket,
    roverDSL::BVLiteral,
    roverDSL::ExpressionBinComp,
    roverDSL::ExpressionBinOp,
    roverDSL::BVarLiteral,
    roverDSL::BBLiteral,
    roverDSL::ColorLiteral,
    roverDSL::BSensorLiteral,
    roverDSL::BNotExpr,
    Action,
    roverDSL::MeasureAction,
    roverDSL::RotateAction,
    roverDSL::SSpeedAction,
    roverDSL::SubRoutineAction,
    roverDSL::StopAction,
    roverDSL::ShowAction,
    roverDSL::FreeAction,
    roverDSL::SoundAction,
    roverDSL::SAccelerationAction,
    roverDSL::ForwardAction,
    roverDSL::Motor,
    Expression,
    roverDSL::AssignExpression,
    roverDSL::WHILEExpression,
    roverDSL::IFExpression,
    roverDSL::Action,
    roverDSL::ValExpr,
    roverDSL::Expression,
    roverDSL::SubRoutine,
    roverDSL::Implementation,
    roverDSL::ValueExpression,
    roverDSL::Static,
    roverDSL::Global,
    roverDSL::BehaviorName,
    roverDSL::Robot,
    BBinaryOp,
    Sensor,
    Sound,
    EMotor,
    Color,
    CompareOp,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_valueexpression_is_not_abstract():
    assert not inspect.isabstract(ValueExpression)


def test_valueexpression_constructor_exists():
    assert callable(ValueExpression.__init__)


def test_valueexpression_constructor_args():
    sig = inspect.signature(ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::bvbracket_is_not_abstract():
    assert not inspect.isabstract(roverDSL::BVBracket)


def test_roverdsl::bvbracket_constructor_exists():
    assert callable(roverDSL::BVBracket.__init__)


def test_roverdsl::bvbracket_constructor_args():
    sig = inspect.signature(roverDSL::BVBracket.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::bvliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL::BVLiteral)


def test_roverdsl::bvliteral_constructor_exists():
    assert callable(roverDSL::BVLiteral.__init__)


def test_roverdsl::bvliteral_constructor_args():
    sig = inspect.signature(roverDSL::BVLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "aValue" in params, "Missing parameter 'aValue'"
    assert "neg" in params, "Missing parameter 'neg'"

def test_roverdsl::bvliteral_has_aValue():
    assert hasattr(roverDSL::BVLiteral, "aValue")
    descriptor = None
    for klass in roverDSL::BVLiteral.__mro__:
        if "aValue" in klass.__dict__:
            descriptor = klass.__dict__["aValue"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl::bvliteral_has_neg():
    assert hasattr(roverDSL::BVLiteral, "neg")
    descriptor = None
    for klass in roverDSL::BVLiteral.__mro__:
        if "neg" in klass.__dict__:
            descriptor = klass.__dict__["neg"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::expressionbincomp_is_not_abstract():
    assert not inspect.isabstract(roverDSL::ExpressionBinComp)


def test_roverdsl::expressionbincomp_constructor_exists():
    assert callable(roverDSL::ExpressionBinComp.__init__)


def test_roverdsl::expressionbincomp_constructor_args():
    sig = inspect.signature(roverDSL::ExpressionBinComp.__init__)
    params = list(sig.parameters.keys())
    assert "bcomp" in params, "Missing parameter 'bcomp'"

def test_roverdsl::expressionbincomp_has_bcomp():
    assert hasattr(roverDSL::ExpressionBinComp, "bcomp")
    descriptor = None
    for klass in roverDSL::ExpressionBinComp.__mro__:
        if "bcomp" in klass.__dict__:
            descriptor = klass.__dict__["bcomp"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::expressionbinop_is_not_abstract():
    assert not inspect.isabstract(roverDSL::ExpressionBinOp)


def test_roverdsl::expressionbinop_constructor_exists():
    assert callable(roverDSL::ExpressionBinOp.__init__)


def test_roverdsl::expressionbinop_constructor_args():
    sig = inspect.signature(roverDSL::ExpressionBinOp.__init__)
    params = list(sig.parameters.keys())
    assert "bop" in params, "Missing parameter 'bop'"

def test_roverdsl::expressionbinop_has_bop():
    assert hasattr(roverDSL::ExpressionBinOp, "bop")
    descriptor = None
    for klass in roverDSL::ExpressionBinOp.__mro__:
        if "bop" in klass.__dict__:
            descriptor = klass.__dict__["bop"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::bvarliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL::BVarLiteral)


def test_roverdsl::bvarliteral_constructor_exists():
    assert callable(roverDSL::BVarLiteral.__init__)


def test_roverdsl::bvarliteral_constructor_args():
    sig = inspect.signature(roverDSL::BVarLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_roverdsl::bvarliteral_has_var():
    assert hasattr(roverDSL::BVarLiteral, "var")
    descriptor = None
    for klass in roverDSL::BVarLiteral.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::bbliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL::BBLiteral)


def test_roverdsl::bbliteral_constructor_exists():
    assert callable(roverDSL::BBLiteral.__init__)


def test_roverdsl::bbliteral_constructor_args():
    sig = inspect.signature(roverDSL::BBLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "bValue" in params, "Missing parameter 'bValue'"

def test_roverdsl::bbliteral_has_bValue():
    assert hasattr(roverDSL::BBLiteral, "bValue")
    descriptor = None
    for klass in roverDSL::BBLiteral.__mro__:
        if "bValue" in klass.__dict__:
            descriptor = klass.__dict__["bValue"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::colorliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL::ColorLiteral)


def test_roverdsl::colorliteral_constructor_exists():
    assert callable(roverDSL::ColorLiteral.__init__)


def test_roverdsl::colorliteral_constructor_args():
    sig = inspect.signature(roverDSL::ColorLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_roverdsl::colorliteral_has_color():
    assert hasattr(roverDSL::ColorLiteral, "color")
    descriptor = None
    for klass in roverDSL::ColorLiteral.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::bsensorliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL::BSensorLiteral)


def test_roverdsl::bsensorliteral_constructor_exists():
    assert callable(roverDSL::BSensorLiteral.__init__)


def test_roverdsl::bsensorliteral_constructor_args():
    sig = inspect.signature(roverDSL::BSensorLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "sensor" in params, "Missing parameter 'sensor'"

def test_roverdsl::bsensorliteral_has_sensor():
    assert hasattr(roverDSL::BSensorLiteral, "sensor")
    descriptor = None
    for klass in roverDSL::BSensorLiteral.__mro__:
        if "sensor" in klass.__dict__:
            descriptor = klass.__dict__["sensor"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::bnotexpr_is_not_abstract():
    assert not inspect.isabstract(roverDSL::BNotExpr)


def test_roverdsl::bnotexpr_constructor_exists():
    assert callable(roverDSL::BNotExpr.__init__)


def test_roverdsl::bnotexpr_constructor_args():
    sig = inspect.signature(roverDSL::BNotExpr.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::measureaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::MeasureAction)


def test_roverdsl::measureaction_constructor_exists():
    assert callable(roverDSL::MeasureAction.__init__)


def test_roverdsl::measureaction_constructor_args():
    sig = inspect.signature(roverDSL::MeasureAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::rotateaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::RotateAction)


def test_roverdsl::rotateaction_constructor_exists():
    assert callable(roverDSL::RotateAction.__init__)


def test_roverdsl::rotateaction_constructor_args():
    sig = inspect.signature(roverDSL::RotateAction.__init__)
    params = list(sig.parameters.keys())
    assert "blocking" in params, "Missing parameter 'blocking'"

def test_roverdsl::rotateaction_has_blocking():
    assert hasattr(roverDSL::RotateAction, "blocking")
    descriptor = None
    for klass in roverDSL::RotateAction.__mro__:
        if "blocking" in klass.__dict__:
            descriptor = klass.__dict__["blocking"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::sspeedaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::SSpeedAction)


def test_roverdsl::sspeedaction_constructor_exists():
    assert callable(roverDSL::SSpeedAction.__init__)


def test_roverdsl::sspeedaction_constructor_args():
    sig = inspect.signature(roverDSL::SSpeedAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::subroutineaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::SubRoutineAction)


def test_roverdsl::subroutineaction_constructor_exists():
    assert callable(roverDSL::SubRoutineAction.__init__)


def test_roverdsl::subroutineaction_constructor_args():
    sig = inspect.signature(roverDSL::SubRoutineAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::stopaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::StopAction)


def test_roverdsl::stopaction_constructor_exists():
    assert callable(roverDSL::StopAction.__init__)


def test_roverdsl::stopaction_constructor_args():
    sig = inspect.signature(roverDSL::StopAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::showaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::ShowAction)


def test_roverdsl::showaction_constructor_exists():
    assert callable(roverDSL::ShowAction.__init__)


def test_roverdsl::showaction_constructor_args():
    sig = inspect.signature(roverDSL::ShowAction.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "sensor" in params, "Missing parameter 'sensor'"

def test_roverdsl::showaction_has_string():
    assert hasattr(roverDSL::ShowAction, "string")
    descriptor = None
    for klass in roverDSL::ShowAction.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl::showaction_has_sensor():
    assert hasattr(roverDSL::ShowAction, "sensor")
    descriptor = None
    for klass in roverDSL::ShowAction.__mro__:
        if "sensor" in klass.__dict__:
            descriptor = klass.__dict__["sensor"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::freeaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::FreeAction)


def test_roverdsl::freeaction_constructor_exists():
    assert callable(roverDSL::FreeAction.__init__)


def test_roverdsl::freeaction_constructor_args():
    sig = inspect.signature(roverDSL::FreeAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::soundaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::SoundAction)


def test_roverdsl::soundaction_constructor_exists():
    assert callable(roverDSL::SoundAction.__init__)


def test_roverdsl::soundaction_constructor_args():
    sig = inspect.signature(roverDSL::SoundAction.__init__)
    params = list(sig.parameters.keys())
    assert "sound" in params, "Missing parameter 'sound'"

def test_roverdsl::soundaction_has_sound():
    assert hasattr(roverDSL::SoundAction, "sound")
    descriptor = None
    for klass in roverDSL::SoundAction.__mro__:
        if "sound" in klass.__dict__:
            descriptor = klass.__dict__["sound"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::saccelerationaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::SAccelerationAction)


def test_roverdsl::saccelerationaction_constructor_exists():
    assert callable(roverDSL::SAccelerationAction.__init__)


def test_roverdsl::saccelerationaction_constructor_args():
    sig = inspect.signature(roverDSL::SAccelerationAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::forwardaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL::ForwardAction)


def test_roverdsl::forwardaction_constructor_exists():
    assert callable(roverDSL::ForwardAction.__init__)


def test_roverdsl::forwardaction_constructor_args():
    sig = inspect.signature(roverDSL::ForwardAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::motor_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Motor)


def test_roverdsl::motor_constructor_exists():
    assert callable(roverDSL::Motor.__init__)


def test_roverdsl::motor_constructor_args():
    sig = inspect.signature(roverDSL::Motor.__init__)
    params = list(sig.parameters.keys())
    assert "m" in params, "Missing parameter 'm'"

def test_roverdsl::motor_has_m():
    assert hasattr(roverDSL::Motor, "m")
    descriptor = None
    for klass in roverDSL::Motor.__mro__:
        if "m" in klass.__dict__:
            descriptor = klass.__dict__["m"]
            break
    assert isinstance(descriptor, property)



def test_expression_is_not_abstract():
    assert not inspect.isabstract(Expression)


def test_expression_constructor_exists():
    assert callable(Expression.__init__)


def test_expression_constructor_args():
    sig = inspect.signature(Expression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::assignexpression_is_not_abstract():
    assert not inspect.isabstract(roverDSL::AssignExpression)


def test_roverdsl::assignexpression_constructor_exists():
    assert callable(roverDSL::AssignExpression.__init__)


def test_roverdsl::assignexpression_constructor_args():
    sig = inspect.signature(roverDSL::AssignExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::whileexpression_is_not_abstract():
    assert not inspect.isabstract(roverDSL::WHILEExpression)


def test_roverdsl::whileexpression_constructor_exists():
    assert callable(roverDSL::WHILEExpression.__init__)


def test_roverdsl::whileexpression_constructor_args():
    sig = inspect.signature(roverDSL::WHILEExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::ifexpression_is_not_abstract():
    assert not inspect.isabstract(roverDSL::IFExpression)


def test_roverdsl::ifexpression_constructor_exists():
    assert callable(roverDSL::IFExpression.__init__)


def test_roverdsl::ifexpression_constructor_args():
    sig = inspect.signature(roverDSL::IFExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::action_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Action)


def test_roverdsl::action_constructor_exists():
    assert callable(roverDSL::Action.__init__)


def test_roverdsl::action_constructor_args():
    sig = inspect.signature(roverDSL::Action.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::valexpr_is_not_abstract():
    assert not inspect.isabstract(roverDSL::ValExpr)


def test_roverdsl::valexpr_constructor_exists():
    assert callable(roverDSL::ValExpr.__init__)


def test_roverdsl::valexpr_constructor_args():
    sig = inspect.signature(roverDSL::ValExpr.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::expression_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Expression)


def test_roverdsl::expression_constructor_exists():
    assert callable(roverDSL::Expression.__init__)


def test_roverdsl::expression_constructor_args():
    sig = inspect.signature(roverDSL::Expression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::subroutine_is_not_abstract():
    assert not inspect.isabstract(roverDSL::SubRoutine)


def test_roverdsl::subroutine_constructor_exists():
    assert callable(roverDSL::SubRoutine.__init__)


def test_roverdsl::subroutine_constructor_args():
    sig = inspect.signature(roverDSL::SubRoutine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverdsl::subroutine_has_name():
    assert hasattr(roverDSL::SubRoutine, "name")
    descriptor = None
    for klass in roverDSL::SubRoutine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::implementation_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Implementation)


def test_roverdsl::implementation_constructor_exists():
    assert callable(roverDSL::Implementation.__init__)


def test_roverdsl::implementation_constructor_args():
    sig = inspect.signature(roverDSL::Implementation.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::valueexpression_is_not_abstract():
    assert not inspect.isabstract(roverDSL::ValueExpression)


def test_roverdsl::valueexpression_constructor_exists():
    assert callable(roverDSL::ValueExpression.__init__)


def test_roverdsl::valueexpression_constructor_args():
    sig = inspect.signature(roverDSL::ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl::static_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Static)


def test_roverdsl::static_constructor_exists():
    assert callable(roverDSL::Static.__init__)


def test_roverdsl::static_constructor_args():
    sig = inspect.signature(roverDSL::Static.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverdsl::static_has_name():
    assert hasattr(roverDSL::Static, "name")
    descriptor = None
    for klass in roverDSL::Static.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::global_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Global)


def test_roverdsl::global_constructor_exists():
    assert callable(roverDSL::Global.__init__)


def test_roverdsl::global_constructor_args():
    sig = inspect.signature(roverDSL::Global.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverdsl::global_has_name():
    assert hasattr(roverDSL::Global, "name")
    descriptor = None
    for klass in roverDSL::Global.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::behaviorname_is_not_abstract():
    assert not inspect.isabstract(roverDSL::BehaviorName)


def test_roverdsl::behaviorname_constructor_exists():
    assert callable(roverDSL::BehaviorName.__init__)


def test_roverdsl::behaviorname_constructor_args():
    sig = inspect.signature(roverDSL::BehaviorName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverdsl::behaviorname_has_name():
    assert hasattr(roverDSL::BehaviorName, "name")
    descriptor = None
    for klass in roverDSL::BehaviorName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl::robot_is_not_abstract():
    assert not inspect.isabstract(roverDSL::Robot)


def test_roverdsl::robot_constructor_exists():
    assert callable(roverDSL::Robot.__init__)


def test_roverdsl::robot_constructor_args():
    sig = inspect.signature(roverDSL::Robot.__init__)
    params = list(sig.parameters.keys())

def test_bbinaryop_exists():
    # Check that the Enumeration exists
    assert BBinaryOp is not None

def test_bbinaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BBinaryOp]
    expected_literals = [
        "OR",
        "AND",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BBinaryOp"

def test_sensor_exists():
    # Check that the Enumeration exists
    assert Sensor is not None

def test_sensor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sensor]
    expected_literals = [
        "RIGHTLIGHTSENSOR",
        "LEFTLIGHTSENSOR",
        "FRONTULTRASONICSENSOR",
        "TOUCHSENSORR",
        "ANGLESENSOR",
        "COLORIDSENSOR",
        "TOUCHSENSORL",
        "REARULTRASONICSENSOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sensor"

def test_sound_exists():
    # Check that the Enumeration exists
    assert Sound is not None

def test_sound_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sound]
    expected_literals = [
        "BEEP",
        "BUZZ",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sound"

def test_emotor_exists():
    # Check that the Enumeration exists
    assert EMotor is not None

def test_emotor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EMotor]
    expected_literals = [
        "RIGHTMOTOR",
        "LEFTMOTOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EMotor"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "GRAY",
        "MAGENTA",
        "GREEN",
        "ORANGE",
        "BROWN",
        "YELLOW",
        "BLUE",
        "BLACK",
        "DARK_GRAY",
        "PINK",
        "RED",
        "CYAN",
        "WHITE",
        "LIGHT_GRAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_compareop_exists():
    # Check that the Enumeration exists
    assert CompareOp is not None

def test_compareop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompareOp]
    expected_literals = [
        "LT",
        "LEQ",
        "NEQ",
        "EQ",
        "GEQ",
        "GT",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CompareOp"


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
ValueExpression_strategy = st.builds(
    ValueExpression,
)
roverDSL::BVBracket_strategy = st.builds(
    roverDSL::BVBracket,
)
roverDSL::BVLiteral_strategy = st.builds(
    roverDSL::BVLiteral,
    aValue=
        st.integers(),
    neg=
        st.booleans()
)
roverDSL::ExpressionBinComp_strategy = st.builds(
    roverDSL::ExpressionBinComp,
    bcomp=
        safe_text
)
roverDSL::ExpressionBinOp_strategy = st.builds(
    roverDSL::ExpressionBinOp,
    bop=
        safe_text
)
roverDSL::BVarLiteral_strategy = st.builds(
    roverDSL::BVarLiteral,
    var=
        safe_text
)
roverDSL::BBLiteral_strategy = st.builds(
    roverDSL::BBLiteral,
    bValue=
        st.booleans()
)
roverDSL::ColorLiteral_strategy = st.builds(
    roverDSL::ColorLiteral,
    color=
        safe_text
)
roverDSL::BSensorLiteral_strategy = st.builds(
    roverDSL::BSensorLiteral,
    sensor=
        safe_text
)
roverDSL::BNotExpr_strategy = st.builds(
    roverDSL::BNotExpr,
)
Action_strategy = st.builds(
    Action,
)
roverDSL::MeasureAction_strategy = st.builds(
    roverDSL::MeasureAction,
)
roverDSL::RotateAction_strategy = st.builds(
    roverDSL::RotateAction,
    blocking=
        st.booleans()
)
roverDSL::SSpeedAction_strategy = st.builds(
    roverDSL::SSpeedAction,
)
roverDSL::SubRoutineAction_strategy = st.builds(
    roverDSL::SubRoutineAction,
)
roverDSL::StopAction_strategy = st.builds(
    roverDSL::StopAction,
)
roverDSL::ShowAction_strategy = st.builds(
    roverDSL::ShowAction,
    string=
        safe_text,
    sensor=
        safe_text
)
roverDSL::FreeAction_strategy = st.builds(
    roverDSL::FreeAction,
)
roverDSL::SoundAction_strategy = st.builds(
    roverDSL::SoundAction,
    sound=
        safe_text
)
roverDSL::SAccelerationAction_strategy = st.builds(
    roverDSL::SAccelerationAction,
)
roverDSL::ForwardAction_strategy = st.builds(
    roverDSL::ForwardAction,
)
roverDSL::Motor_strategy = st.builds(
    roverDSL::Motor,
    m=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
roverDSL::AssignExpression_strategy = st.builds(
    roverDSL::AssignExpression,
)
roverDSL::WHILEExpression_strategy = st.builds(
    roverDSL::WHILEExpression,
)
roverDSL::IFExpression_strategy = st.builds(
    roverDSL::IFExpression,
)
roverDSL::Action_strategy = st.builds(
    roverDSL::Action,
)
roverDSL::ValExpr_strategy = st.builds(
    roverDSL::ValExpr,
)
roverDSL::Expression_strategy = st.builds(
    roverDSL::Expression,
)
roverDSL::SubRoutine_strategy = st.builds(
    roverDSL::SubRoutine,
    name=
        safe_text
)
roverDSL::Implementation_strategy = st.builds(
    roverDSL::Implementation,
)
roverDSL::ValueExpression_strategy = st.builds(
    roverDSL::ValueExpression,
)
roverDSL::Static_strategy = st.builds(
    roverDSL::Static,
    name=
        safe_text
)
roverDSL::Global_strategy = st.builds(
    roverDSL::Global,
    name=
        safe_text
)
roverDSL::BehaviorName_strategy = st.builds(
    roverDSL::BehaviorName,
    name=
        safe_text
)
roverDSL::Robot_strategy = st.builds(
    roverDSL::Robot,
)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=roverDSL::BVBracket_strategy)
@settings(max_examples=50)
def test_roverdsl::bvbracket_instantiation(instance):
    assert isinstance(instance, roverDSL::BVBracket)

@given(instance=roverDSL::BVLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl::bvliteral_instantiation(instance):
    assert isinstance(instance, roverDSL::BVLiteral)

@given(instance=roverDSL::BVLiteral_strategy)
def test_roverdsl::bvliteral_aValue_type(instance):
    assert isinstance(instance.aValue, int)


@given(instance=roverDSL::BVLiteral_strategy)
def test_roverdsl::bvliteral_aValue_setter(instance):
    original = instance.aValue
    instance.aValue = original
    assert instance.aValue == original

@given(instance=roverDSL::BVLiteral_strategy)
def test_roverdsl::bvliteral_neg_type(instance):
    assert isinstance(instance.neg, bool)


@given(instance=roverDSL::BVLiteral_strategy)
def test_roverdsl::bvliteral_neg_setter(instance):
    original = instance.neg
    instance.neg = original
    assert instance.neg == original

@given(instance=roverDSL::ExpressionBinComp_strategy)
@settings(max_examples=50)
def test_roverdsl::expressionbincomp_instantiation(instance):
    assert isinstance(instance, roverDSL::ExpressionBinComp)

@given(instance=roverDSL::ExpressionBinComp_strategy)
def test_roverdsl::expressionbincomp_bcomp_type(instance):
    assert isinstance(instance.bcomp, str)


@given(instance=roverDSL::ExpressionBinComp_strategy)
def test_roverdsl::expressionbincomp_bcomp_setter(instance):
    original = instance.bcomp
    instance.bcomp = original
    assert instance.bcomp == original

@given(instance=roverDSL::ExpressionBinOp_strategy)
@settings(max_examples=50)
def test_roverdsl::expressionbinop_instantiation(instance):
    assert isinstance(instance, roverDSL::ExpressionBinOp)

@given(instance=roverDSL::ExpressionBinOp_strategy)
def test_roverdsl::expressionbinop_bop_type(instance):
    assert isinstance(instance.bop, str)


@given(instance=roverDSL::ExpressionBinOp_strategy)
def test_roverdsl::expressionbinop_bop_setter(instance):
    original = instance.bop
    instance.bop = original
    assert instance.bop == original

@given(instance=roverDSL::BVarLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl::bvarliteral_instantiation(instance):
    assert isinstance(instance, roverDSL::BVarLiteral)

@given(instance=roverDSL::BVarLiteral_strategy)
def test_roverdsl::bvarliteral_var_type(instance):
    assert isinstance(instance.var, str)


@given(instance=roverDSL::BVarLiteral_strategy)
def test_roverdsl::bvarliteral_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=roverDSL::BBLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl::bbliteral_instantiation(instance):
    assert isinstance(instance, roverDSL::BBLiteral)

@given(instance=roverDSL::BBLiteral_strategy)
def test_roverdsl::bbliteral_bValue_type(instance):
    assert isinstance(instance.bValue, bool)


@given(instance=roverDSL::BBLiteral_strategy)
def test_roverdsl::bbliteral_bValue_setter(instance):
    original = instance.bValue
    instance.bValue = original
    assert instance.bValue == original

@given(instance=roverDSL::ColorLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl::colorliteral_instantiation(instance):
    assert isinstance(instance, roverDSL::ColorLiteral)

@given(instance=roverDSL::ColorLiteral_strategy)
def test_roverdsl::colorliteral_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=roverDSL::ColorLiteral_strategy)
def test_roverdsl::colorliteral_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=roverDSL::BSensorLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl::bsensorliteral_instantiation(instance):
    assert isinstance(instance, roverDSL::BSensorLiteral)

@given(instance=roverDSL::BSensorLiteral_strategy)
def test_roverdsl::bsensorliteral_sensor_type(instance):
    assert isinstance(instance.sensor, str)


@given(instance=roverDSL::BSensorLiteral_strategy)
def test_roverdsl::bsensorliteral_sensor_setter(instance):
    original = instance.sensor
    instance.sensor = original
    assert instance.sensor == original

@given(instance=roverDSL::BNotExpr_strategy)
@settings(max_examples=50)
def test_roverdsl::bnotexpr_instantiation(instance):
    assert isinstance(instance, roverDSL::BNotExpr)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=roverDSL::MeasureAction_strategy)
@settings(max_examples=50)
def test_roverdsl::measureaction_instantiation(instance):
    assert isinstance(instance, roverDSL::MeasureAction)

@given(instance=roverDSL::RotateAction_strategy)
@settings(max_examples=50)
def test_roverdsl::rotateaction_instantiation(instance):
    assert isinstance(instance, roverDSL::RotateAction)

@given(instance=roverDSL::RotateAction_strategy)
def test_roverdsl::rotateaction_blocking_type(instance):
    assert isinstance(instance.blocking, bool)


@given(instance=roverDSL::RotateAction_strategy)
def test_roverdsl::rotateaction_blocking_setter(instance):
    original = instance.blocking
    instance.blocking = original
    assert instance.blocking == original

@given(instance=roverDSL::SSpeedAction_strategy)
@settings(max_examples=50)
def test_roverdsl::sspeedaction_instantiation(instance):
    assert isinstance(instance, roverDSL::SSpeedAction)

@given(instance=roverDSL::SubRoutineAction_strategy)
@settings(max_examples=50)
def test_roverdsl::subroutineaction_instantiation(instance):
    assert isinstance(instance, roverDSL::SubRoutineAction)

@given(instance=roverDSL::StopAction_strategy)
@settings(max_examples=50)
def test_roverdsl::stopaction_instantiation(instance):
    assert isinstance(instance, roverDSL::StopAction)

@given(instance=roverDSL::ShowAction_strategy)
@settings(max_examples=50)
def test_roverdsl::showaction_instantiation(instance):
    assert isinstance(instance, roverDSL::ShowAction)

@given(instance=roverDSL::ShowAction_strategy)
def test_roverdsl::showaction_string_type(instance):
    assert isinstance(instance.string, str)


@given(instance=roverDSL::ShowAction_strategy)
def test_roverdsl::showaction_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original

@given(instance=roverDSL::ShowAction_strategy)
def test_roverdsl::showaction_sensor_type(instance):
    assert isinstance(instance.sensor, str)


@given(instance=roverDSL::ShowAction_strategy)
def test_roverdsl::showaction_sensor_setter(instance):
    original = instance.sensor
    instance.sensor = original
    assert instance.sensor == original

@given(instance=roverDSL::FreeAction_strategy)
@settings(max_examples=50)
def test_roverdsl::freeaction_instantiation(instance):
    assert isinstance(instance, roverDSL::FreeAction)

@given(instance=roverDSL::SoundAction_strategy)
@settings(max_examples=50)
def test_roverdsl::soundaction_instantiation(instance):
    assert isinstance(instance, roverDSL::SoundAction)

@given(instance=roverDSL::SoundAction_strategy)
def test_roverdsl::soundaction_sound_type(instance):
    assert isinstance(instance.sound, str)


@given(instance=roverDSL::SoundAction_strategy)
def test_roverdsl::soundaction_sound_setter(instance):
    original = instance.sound
    instance.sound = original
    assert instance.sound == original

@given(instance=roverDSL::SAccelerationAction_strategy)
@settings(max_examples=50)
def test_roverdsl::saccelerationaction_instantiation(instance):
    assert isinstance(instance, roverDSL::SAccelerationAction)

@given(instance=roverDSL::ForwardAction_strategy)
@settings(max_examples=50)
def test_roverdsl::forwardaction_instantiation(instance):
    assert isinstance(instance, roverDSL::ForwardAction)

@given(instance=roverDSL::Motor_strategy)
@settings(max_examples=50)
def test_roverdsl::motor_instantiation(instance):
    assert isinstance(instance, roverDSL::Motor)

@given(instance=roverDSL::Motor_strategy)
def test_roverdsl::motor_m_type(instance):
    assert isinstance(instance.m, str)


@given(instance=roverDSL::Motor_strategy)
def test_roverdsl::motor_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=roverDSL::AssignExpression_strategy)
@settings(max_examples=50)
def test_roverdsl::assignexpression_instantiation(instance):
    assert isinstance(instance, roverDSL::AssignExpression)

@given(instance=roverDSL::WHILEExpression_strategy)
@settings(max_examples=50)
def test_roverdsl::whileexpression_instantiation(instance):
    assert isinstance(instance, roverDSL::WHILEExpression)

@given(instance=roverDSL::IFExpression_strategy)
@settings(max_examples=50)
def test_roverdsl::ifexpression_instantiation(instance):
    assert isinstance(instance, roverDSL::IFExpression)

@given(instance=roverDSL::Action_strategy)
@settings(max_examples=50)
def test_roverdsl::action_instantiation(instance):
    assert isinstance(instance, roverDSL::Action)

@given(instance=roverDSL::ValExpr_strategy)
@settings(max_examples=50)
def test_roverdsl::valexpr_instantiation(instance):
    assert isinstance(instance, roverDSL::ValExpr)

@given(instance=roverDSL::Expression_strategy)
@settings(max_examples=50)
def test_roverdsl::expression_instantiation(instance):
    assert isinstance(instance, roverDSL::Expression)

@given(instance=roverDSL::SubRoutine_strategy)
@settings(max_examples=50)
def test_roverdsl::subroutine_instantiation(instance):
    assert isinstance(instance, roverDSL::SubRoutine)

@given(instance=roverDSL::SubRoutine_strategy)
def test_roverdsl::subroutine_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=roverDSL::SubRoutine_strategy)
def test_roverdsl::subroutine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverDSL::Implementation_strategy)
@settings(max_examples=50)
def test_roverdsl::implementation_instantiation(instance):
    assert isinstance(instance, roverDSL::Implementation)

@given(instance=roverDSL::ValueExpression_strategy)
@settings(max_examples=50)
def test_roverdsl::valueexpression_instantiation(instance):
    assert isinstance(instance, roverDSL::ValueExpression)

@given(instance=roverDSL::Static_strategy)
@settings(max_examples=50)
def test_roverdsl::static_instantiation(instance):
    assert isinstance(instance, roverDSL::Static)

@given(instance=roverDSL::Static_strategy)
def test_roverdsl::static_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=roverDSL::Static_strategy)
def test_roverdsl::static_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverDSL::Global_strategy)
@settings(max_examples=50)
def test_roverdsl::global_instantiation(instance):
    assert isinstance(instance, roverDSL::Global)

@given(instance=roverDSL::Global_strategy)
def test_roverdsl::global_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=roverDSL::Global_strategy)
def test_roverdsl::global_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverDSL::BehaviorName_strategy)
@settings(max_examples=50)
def test_roverdsl::behaviorname_instantiation(instance):
    assert isinstance(instance, roverDSL::BehaviorName)

@given(instance=roverDSL::BehaviorName_strategy)
def test_roverdsl::behaviorname_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=roverDSL::BehaviorName_strategy)
def test_roverdsl::behaviorname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverDSL::Robot_strategy)
@settings(max_examples=50)
def test_roverdsl::robot_instantiation(instance):
    assert isinstance(instance, roverDSL::Robot)
