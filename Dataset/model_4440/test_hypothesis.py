import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ValueExpression,
    roverDSL_BVarLiteral,
    roverDSL_ExpressionBinOp,
    roverDSL_BVLiteral,
    roverDSL_BBLiteral,
    roverDSL_ColorLiteral,
    roverDSL_ExpressionBinComp,
    roverDSL_BVBracket,
    roverDSL_BSensorLiteral,
    roverDSL_BNotExpr,
    Action,
    roverDSL_SoundAction,
    roverDSL_ShowAction,
    roverDSL_SAccelerationAction,
    roverDSL_StopAction,
    roverDSL_SSpeedAction,
    roverDSL_MeasureAction,
    roverDSL_FreeAction,
    roverDSL_SubRoutineAction,
    roverDSL_RotateAction,
    roverDSL_ForwardAction,
    roverDSL_Motor,
    Expression,
    roverDSL_Action,
    roverDSL_IFExpression,
    roverDSL_WHILEExpression,
    roverDSL_AssignExpression,
    roverDSL_ValExpr,
    roverDSL_Expression,
    roverDSL_SubRoutine,
    roverDSL_Implementation,
    roverDSL_ValueExpression,
    roverDSL_Static,
    roverDSL_Global,
    roverDSL_BehaviorName,
    roverDSL_Robot,
    Sound,
    Sensor,
    Color,
    EMotor,
    BBinaryOp,
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



def test_roverdsl_bvarliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL_BVarLiteral)


def test_roverdsl_bvarliteral_constructor_exists():
    assert callable(roverDSL_BVarLiteral.__init__)


def test_roverdsl_bvarliteral_constructor_args():
    sig = inspect.signature(roverDSL_BVarLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "var" in params, "Missing parameter 'var'"

def test_roverdsl_bvarliteral_has_var():
    assert hasattr(roverDSL_BVarLiteral, "var")
    descriptor = None
    for klass in roverDSL_BVarLiteral.__mro__:
        if "var" in klass.__dict__:
            descriptor = klass.__dict__["var"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_expressionbinop_is_not_abstract():
    assert not inspect.isabstract(roverDSL_ExpressionBinOp)


def test_roverdsl_expressionbinop_constructor_exists():
    assert callable(roverDSL_ExpressionBinOp.__init__)


def test_roverdsl_expressionbinop_constructor_args():
    sig = inspect.signature(roverDSL_ExpressionBinOp.__init__)
    params = list(sig.parameters.keys())
    assert "bop" in params, "Missing parameter 'bop'"

def test_roverdsl_expressionbinop_has_bop():
    assert hasattr(roverDSL_ExpressionBinOp, "bop")
    descriptor = None
    for klass in roverDSL_ExpressionBinOp.__mro__:
        if "bop" in klass.__dict__:
            descriptor = klass.__dict__["bop"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_bvliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL_BVLiteral)


def test_roverdsl_bvliteral_constructor_exists():
    assert callable(roverDSL_BVLiteral.__init__)


def test_roverdsl_bvliteral_constructor_args():
    sig = inspect.signature(roverDSL_BVLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "neg" in params, "Missing parameter 'neg'"
    assert "aValue" in params, "Missing parameter 'aValue'"

def test_roverdsl_bvliteral_has_neg():
    assert hasattr(roverDSL_BVLiteral, "neg")
    descriptor = None
    for klass in roverDSL_BVLiteral.__mro__:
        if "neg" in klass.__dict__:
            descriptor = klass.__dict__["neg"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl_bvliteral_has_aValue():
    assert hasattr(roverDSL_BVLiteral, "aValue")
    descriptor = None
    for klass in roverDSL_BVLiteral.__mro__:
        if "aValue" in klass.__dict__:
            descriptor = klass.__dict__["aValue"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_bbliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL_BBLiteral)


def test_roverdsl_bbliteral_constructor_exists():
    assert callable(roverDSL_BBLiteral.__init__)


def test_roverdsl_bbliteral_constructor_args():
    sig = inspect.signature(roverDSL_BBLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "bValue" in params, "Missing parameter 'bValue'"

def test_roverdsl_bbliteral_has_bValue():
    assert hasattr(roverDSL_BBLiteral, "bValue")
    descriptor = None
    for klass in roverDSL_BBLiteral.__mro__:
        if "bValue" in klass.__dict__:
            descriptor = klass.__dict__["bValue"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_colorliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL_ColorLiteral)


def test_roverdsl_colorliteral_constructor_exists():
    assert callable(roverDSL_ColorLiteral.__init__)


def test_roverdsl_colorliteral_constructor_args():
    sig = inspect.signature(roverDSL_ColorLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_roverdsl_colorliteral_has_color():
    assert hasattr(roverDSL_ColorLiteral, "color")
    descriptor = None
    for klass in roverDSL_ColorLiteral.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_expressionbincomp_is_not_abstract():
    assert not inspect.isabstract(roverDSL_ExpressionBinComp)


def test_roverdsl_expressionbincomp_constructor_exists():
    assert callable(roverDSL_ExpressionBinComp.__init__)


def test_roverdsl_expressionbincomp_constructor_args():
    sig = inspect.signature(roverDSL_ExpressionBinComp.__init__)
    params = list(sig.parameters.keys())
    assert "bcomp" in params, "Missing parameter 'bcomp'"

def test_roverdsl_expressionbincomp_has_bcomp():
    assert hasattr(roverDSL_ExpressionBinComp, "bcomp")
    descriptor = None
    for klass in roverDSL_ExpressionBinComp.__mro__:
        if "bcomp" in klass.__dict__:
            descriptor = klass.__dict__["bcomp"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_bvbracket_is_not_abstract():
    assert not inspect.isabstract(roverDSL_BVBracket)


def test_roverdsl_bvbracket_constructor_exists():
    assert callable(roverDSL_BVBracket.__init__)


def test_roverdsl_bvbracket_constructor_args():
    sig = inspect.signature(roverDSL_BVBracket.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_bsensorliteral_is_not_abstract():
    assert not inspect.isabstract(roverDSL_BSensorLiteral)


def test_roverdsl_bsensorliteral_constructor_exists():
    assert callable(roverDSL_BSensorLiteral.__init__)


def test_roverdsl_bsensorliteral_constructor_args():
    sig = inspect.signature(roverDSL_BSensorLiteral.__init__)
    params = list(sig.parameters.keys())
    assert "sensor" in params, "Missing parameter 'sensor'"

def test_roverdsl_bsensorliteral_has_sensor():
    assert hasattr(roverDSL_BSensorLiteral, "sensor")
    descriptor = None
    for klass in roverDSL_BSensorLiteral.__mro__:
        if "sensor" in klass.__dict__:
            descriptor = klass.__dict__["sensor"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_bnotexpr_is_not_abstract():
    assert not inspect.isabstract(roverDSL_BNotExpr)


def test_roverdsl_bnotexpr_constructor_exists():
    assert callable(roverDSL_BNotExpr.__init__)


def test_roverdsl_bnotexpr_constructor_args():
    sig = inspect.signature(roverDSL_BNotExpr.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_soundaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_SoundAction)


def test_roverdsl_soundaction_constructor_exists():
    assert callable(roverDSL_SoundAction.__init__)


def test_roverdsl_soundaction_constructor_args():
    sig = inspect.signature(roverDSL_SoundAction.__init__)
    params = list(sig.parameters.keys())
    assert "sound" in params, "Missing parameter 'sound'"

def test_roverdsl_soundaction_has_sound():
    assert hasattr(roverDSL_SoundAction, "sound")
    descriptor = None
    for klass in roverDSL_SoundAction.__mro__:
        if "sound" in klass.__dict__:
            descriptor = klass.__dict__["sound"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_showaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_ShowAction)


def test_roverdsl_showaction_constructor_exists():
    assert callable(roverDSL_ShowAction.__init__)


def test_roverdsl_showaction_constructor_args():
    sig = inspect.signature(roverDSL_ShowAction.__init__)
    params = list(sig.parameters.keys())
    assert "string" in params, "Missing parameter 'string'"
    assert "sensor" in params, "Missing parameter 'sensor'"

def test_roverdsl_showaction_has_string():
    assert hasattr(roverDSL_ShowAction, "string")
    descriptor = None
    for klass in roverDSL_ShowAction.__mro__:
        if "string" in klass.__dict__:
            descriptor = klass.__dict__["string"]
            break
    assert isinstance(descriptor, property)

def test_roverdsl_showaction_has_sensor():
    assert hasattr(roverDSL_ShowAction, "sensor")
    descriptor = None
    for klass in roverDSL_ShowAction.__mro__:
        if "sensor" in klass.__dict__:
            descriptor = klass.__dict__["sensor"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_saccelerationaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_SAccelerationAction)


def test_roverdsl_saccelerationaction_constructor_exists():
    assert callable(roverDSL_SAccelerationAction.__init__)


def test_roverdsl_saccelerationaction_constructor_args():
    sig = inspect.signature(roverDSL_SAccelerationAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_stopaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_StopAction)


def test_roverdsl_stopaction_constructor_exists():
    assert callable(roverDSL_StopAction.__init__)


def test_roverdsl_stopaction_constructor_args():
    sig = inspect.signature(roverDSL_StopAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_sspeedaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_SSpeedAction)


def test_roverdsl_sspeedaction_constructor_exists():
    assert callable(roverDSL_SSpeedAction.__init__)


def test_roverdsl_sspeedaction_constructor_args():
    sig = inspect.signature(roverDSL_SSpeedAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_measureaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_MeasureAction)


def test_roverdsl_measureaction_constructor_exists():
    assert callable(roverDSL_MeasureAction.__init__)


def test_roverdsl_measureaction_constructor_args():
    sig = inspect.signature(roverDSL_MeasureAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_freeaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_FreeAction)


def test_roverdsl_freeaction_constructor_exists():
    assert callable(roverDSL_FreeAction.__init__)


def test_roverdsl_freeaction_constructor_args():
    sig = inspect.signature(roverDSL_FreeAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_subroutineaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_SubRoutineAction)


def test_roverdsl_subroutineaction_constructor_exists():
    assert callable(roverDSL_SubRoutineAction.__init__)


def test_roverdsl_subroutineaction_constructor_args():
    sig = inspect.signature(roverDSL_SubRoutineAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_rotateaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_RotateAction)


def test_roverdsl_rotateaction_constructor_exists():
    assert callable(roverDSL_RotateAction.__init__)


def test_roverdsl_rotateaction_constructor_args():
    sig = inspect.signature(roverDSL_RotateAction.__init__)
    params = list(sig.parameters.keys())
    assert "blocking" in params, "Missing parameter 'blocking'"

def test_roverdsl_rotateaction_has_blocking():
    assert hasattr(roverDSL_RotateAction, "blocking")
    descriptor = None
    for klass in roverDSL_RotateAction.__mro__:
        if "blocking" in klass.__dict__:
            descriptor = klass.__dict__["blocking"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_forwardaction_is_not_abstract():
    assert not inspect.isabstract(roverDSL_ForwardAction)


def test_roverdsl_forwardaction_constructor_exists():
    assert callable(roverDSL_ForwardAction.__init__)


def test_roverdsl_forwardaction_constructor_args():
    sig = inspect.signature(roverDSL_ForwardAction.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_motor_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Motor)


def test_roverdsl_motor_constructor_exists():
    assert callable(roverDSL_Motor.__init__)


def test_roverdsl_motor_constructor_args():
    sig = inspect.signature(roverDSL_Motor.__init__)
    params = list(sig.parameters.keys())
    assert "m" in params, "Missing parameter 'm'"

def test_roverdsl_motor_has_m():
    assert hasattr(roverDSL_Motor, "m")
    descriptor = None
    for klass in roverDSL_Motor.__mro__:
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



def test_roverdsl_action_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Action)


def test_roverdsl_action_constructor_exists():
    assert callable(roverDSL_Action.__init__)


def test_roverdsl_action_constructor_args():
    sig = inspect.signature(roverDSL_Action.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_ifexpression_is_not_abstract():
    assert not inspect.isabstract(roverDSL_IFExpression)


def test_roverdsl_ifexpression_constructor_exists():
    assert callable(roverDSL_IFExpression.__init__)


def test_roverdsl_ifexpression_constructor_args():
    sig = inspect.signature(roverDSL_IFExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_whileexpression_is_not_abstract():
    assert not inspect.isabstract(roverDSL_WHILEExpression)


def test_roverdsl_whileexpression_constructor_exists():
    assert callable(roverDSL_WHILEExpression.__init__)


def test_roverdsl_whileexpression_constructor_args():
    sig = inspect.signature(roverDSL_WHILEExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_assignexpression_is_not_abstract():
    assert not inspect.isabstract(roverDSL_AssignExpression)


def test_roverdsl_assignexpression_constructor_exists():
    assert callable(roverDSL_AssignExpression.__init__)


def test_roverdsl_assignexpression_constructor_args():
    sig = inspect.signature(roverDSL_AssignExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_valexpr_is_not_abstract():
    assert not inspect.isabstract(roverDSL_ValExpr)


def test_roverdsl_valexpr_constructor_exists():
    assert callable(roverDSL_ValExpr.__init__)


def test_roverdsl_valexpr_constructor_args():
    sig = inspect.signature(roverDSL_ValExpr.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_expression_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Expression)


def test_roverdsl_expression_constructor_exists():
    assert callable(roverDSL_Expression.__init__)


def test_roverdsl_expression_constructor_args():
    sig = inspect.signature(roverDSL_Expression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_subroutine_is_not_abstract():
    assert not inspect.isabstract(roverDSL_SubRoutine)


def test_roverdsl_subroutine_constructor_exists():
    assert callable(roverDSL_SubRoutine.__init__)


def test_roverdsl_subroutine_constructor_args():
    sig = inspect.signature(roverDSL_SubRoutine.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverdsl_subroutine_has_name():
    assert hasattr(roverDSL_SubRoutine, "name")
    descriptor = None
    for klass in roverDSL_SubRoutine.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_implementation_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Implementation)


def test_roverdsl_implementation_constructor_exists():
    assert callable(roverDSL_Implementation.__init__)


def test_roverdsl_implementation_constructor_args():
    sig = inspect.signature(roverDSL_Implementation.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_valueexpression_is_not_abstract():
    assert not inspect.isabstract(roverDSL_ValueExpression)


def test_roverdsl_valueexpression_constructor_exists():
    assert callable(roverDSL_ValueExpression.__init__)


def test_roverdsl_valueexpression_constructor_args():
    sig = inspect.signature(roverDSL_ValueExpression.__init__)
    params = list(sig.parameters.keys())



def test_roverdsl_static_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Static)


def test_roverdsl_static_constructor_exists():
    assert callable(roverDSL_Static.__init__)


def test_roverdsl_static_constructor_args():
    sig = inspect.signature(roverDSL_Static.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverdsl_static_has_name():
    assert hasattr(roverDSL_Static, "name")
    descriptor = None
    for klass in roverDSL_Static.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_global_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Global)


def test_roverdsl_global_constructor_exists():
    assert callable(roverDSL_Global.__init__)


def test_roverdsl_global_constructor_args():
    sig = inspect.signature(roverDSL_Global.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverdsl_global_has_name():
    assert hasattr(roverDSL_Global, "name")
    descriptor = None
    for klass in roverDSL_Global.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_behaviorname_is_not_abstract():
    assert not inspect.isabstract(roverDSL_BehaviorName)


def test_roverdsl_behaviorname_constructor_exists():
    assert callable(roverDSL_BehaviorName.__init__)


def test_roverdsl_behaviorname_constructor_args():
    sig = inspect.signature(roverDSL_BehaviorName.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_roverdsl_behaviorname_has_name():
    assert hasattr(roverDSL_BehaviorName, "name")
    descriptor = None
    for klass in roverDSL_BehaviorName.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_roverdsl_robot_is_not_abstract():
    assert not inspect.isabstract(roverDSL_Robot)


def test_roverdsl_robot_constructor_exists():
    assert callable(roverDSL_Robot.__init__)


def test_roverdsl_robot_constructor_args():
    sig = inspect.signature(roverDSL_Robot.__init__)
    params = list(sig.parameters.keys())

def test_sound_exists():
    # Check that the Enumeration exists
    assert Sound is not None

def test_sound_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sound]
    expected_literals = [
        "BUZZ",
        "BEEP",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sound"

def test_sensor_exists():
    # Check that the Enumeration exists
    assert Sensor is not None

def test_sensor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Sensor]
    expected_literals = [
        "TOUCHSENSORR",
        "FRONTULTRASONICSENSOR",
        "REARULTRASONICSENSOR",
        "ANGLESENSOR",
        "COLORIDSENSOR",
        "RIGHTLIGHTSENSOR",
        "TOUCHSENSORL",
        "LEFTLIGHTSENSOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Sensor"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "LIGHT_GRAY",
        "WHITE",
        "GREEN",
        "RED",
        "PINK",
        "CYAN",
        "GRAY",
        "ORANGE",
        "YELLOW",
        "DARK_GRAY",
        "MAGENTA",
        "BLUE",
        "BROWN",
        "BLACK",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_emotor_exists():
    # Check that the Enumeration exists
    assert EMotor is not None

def test_emotor_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in EMotor]
    expected_literals = [
        "LEFTMOTOR",
        "RIGHTMOTOR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in EMotor"

def test_bbinaryop_exists():
    # Check that the Enumeration exists
    assert BBinaryOp is not None

def test_bbinaryop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BBinaryOp]
    expected_literals = [
        "AND",
        "OR",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BBinaryOp"

def test_compareop_exists():
    # Check that the Enumeration exists
    assert CompareOp is not None

def test_compareop_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CompareOp]
    expected_literals = [
        "EQ",
        "LT",
        "NEQ",
        "GT",
        "GEQ",
        "LEQ",
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
roverDSL_BVarLiteral_strategy = st.builds(
    roverDSL_BVarLiteral,
    var=
        safe_text
)
roverDSL_ExpressionBinOp_strategy = st.builds(
    roverDSL_ExpressionBinOp,
    bop=
        safe_text
)
roverDSL_BVLiteral_strategy = st.builds(
    roverDSL_BVLiteral,
    neg=
        st.booleans(),
    aValue=
        st.integers()
)
roverDSL_BBLiteral_strategy = st.builds(
    roverDSL_BBLiteral,
    bValue=
        st.booleans()
)
roverDSL_ColorLiteral_strategy = st.builds(
    roverDSL_ColorLiteral,
    color=
        safe_text
)
roverDSL_ExpressionBinComp_strategy = st.builds(
    roverDSL_ExpressionBinComp,
    bcomp=
        safe_text
)
roverDSL_BVBracket_strategy = st.builds(
    roverDSL_BVBracket,
)
roverDSL_BSensorLiteral_strategy = st.builds(
    roverDSL_BSensorLiteral,
    sensor=
        safe_text
)
roverDSL_BNotExpr_strategy = st.builds(
    roverDSL_BNotExpr,
)
Action_strategy = st.builds(
    Action,
)
roverDSL_SoundAction_strategy = st.builds(
    roverDSL_SoundAction,
    sound=
        safe_text
)
roverDSL_ShowAction_strategy = st.builds(
    roverDSL_ShowAction,
    string=
        safe_text,
    sensor=
        safe_text
)
roverDSL_SAccelerationAction_strategy = st.builds(
    roverDSL_SAccelerationAction,
)
roverDSL_StopAction_strategy = st.builds(
    roverDSL_StopAction,
)
roverDSL_SSpeedAction_strategy = st.builds(
    roverDSL_SSpeedAction,
)
roverDSL_MeasureAction_strategy = st.builds(
    roverDSL_MeasureAction,
)
roverDSL_FreeAction_strategy = st.builds(
    roverDSL_FreeAction,
)
roverDSL_SubRoutineAction_strategy = st.builds(
    roverDSL_SubRoutineAction,
)
roverDSL_RotateAction_strategy = st.builds(
    roverDSL_RotateAction,
    blocking=
        st.booleans()
)
roverDSL_ForwardAction_strategy = st.builds(
    roverDSL_ForwardAction,
)
roverDSL_Motor_strategy = st.builds(
    roverDSL_Motor,
    m=
        safe_text
)
Expression_strategy = st.builds(
    Expression,
)
roverDSL_Action_strategy = st.builds(
    roverDSL_Action,
)
roverDSL_IFExpression_strategy = st.builds(
    roverDSL_IFExpression,
)
roverDSL_WHILEExpression_strategy = st.builds(
    roverDSL_WHILEExpression,
)
roverDSL_AssignExpression_strategy = st.builds(
    roverDSL_AssignExpression,
)
roverDSL_ValExpr_strategy = st.builds(
    roverDSL_ValExpr,
)
roverDSL_Expression_strategy = st.builds(
    roverDSL_Expression,
)
roverDSL_SubRoutine_strategy = st.builds(
    roverDSL_SubRoutine,
    name=
        safe_text
)
roverDSL_Implementation_strategy = st.builds(
    roverDSL_Implementation,
)
roverDSL_ValueExpression_strategy = st.builds(
    roverDSL_ValueExpression,
)
roverDSL_Static_strategy = st.builds(
    roverDSL_Static,
    name=
        safe_text
)
roverDSL_Global_strategy = st.builds(
    roverDSL_Global,
    name=
        safe_text
)
roverDSL_BehaviorName_strategy = st.builds(
    roverDSL_BehaviorName,
    name=
        safe_text
)
roverDSL_Robot_strategy = st.builds(
    roverDSL_Robot,
)

@given(instance=ValueExpression_strategy)
@settings(max_examples=50)
def test_valueexpression_instantiation(instance):
    assert isinstance(instance, ValueExpression)

@given(instance=roverDSL_BVarLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl_bvarliteral_instantiation(instance):
    assert isinstance(instance, roverDSL_BVarLiteral)



@given(instance=roverDSL_BVarLiteral_strategy)
def test_roverdsl_bvarliteral_var_setter(instance):
    original = instance.var
    instance.var = original
    assert instance.var == original

@given(instance=roverDSL_ExpressionBinOp_strategy)
@settings(max_examples=50)
def test_roverdsl_expressionbinop_instantiation(instance):
    assert isinstance(instance, roverDSL_ExpressionBinOp)



@given(instance=roverDSL_ExpressionBinOp_strategy)
def test_roverdsl_expressionbinop_bop_setter(instance):
    original = instance.bop
    instance.bop = original
    assert instance.bop == original

@given(instance=roverDSL_BVLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl_bvliteral_instantiation(instance):
    assert isinstance(instance, roverDSL_BVLiteral)



@given(instance=roverDSL_BVLiteral_strategy)
def test_roverdsl_bvliteral_neg_setter(instance):
    original = instance.neg
    instance.neg = original
    assert instance.neg == original



@given(instance=roverDSL_BVLiteral_strategy)
def test_roverdsl_bvliteral_aValue_setter(instance):
    original = instance.aValue
    instance.aValue = original
    assert instance.aValue == original

@given(instance=roverDSL_BBLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl_bbliteral_instantiation(instance):
    assert isinstance(instance, roverDSL_BBLiteral)



@given(instance=roverDSL_BBLiteral_strategy)
def test_roverdsl_bbliteral_bValue_setter(instance):
    original = instance.bValue
    instance.bValue = original
    assert instance.bValue == original

@given(instance=roverDSL_ColorLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl_colorliteral_instantiation(instance):
    assert isinstance(instance, roverDSL_ColorLiteral)



@given(instance=roverDSL_ColorLiteral_strategy)
def test_roverdsl_colorliteral_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=roverDSL_ExpressionBinComp_strategy)
@settings(max_examples=50)
def test_roverdsl_expressionbincomp_instantiation(instance):
    assert isinstance(instance, roverDSL_ExpressionBinComp)



@given(instance=roverDSL_ExpressionBinComp_strategy)
def test_roverdsl_expressionbincomp_bcomp_setter(instance):
    original = instance.bcomp
    instance.bcomp = original
    assert instance.bcomp == original

@given(instance=roverDSL_BVBracket_strategy)
@settings(max_examples=50)
def test_roverdsl_bvbracket_instantiation(instance):
    assert isinstance(instance, roverDSL_BVBracket)

@given(instance=roverDSL_BSensorLiteral_strategy)
@settings(max_examples=50)
def test_roverdsl_bsensorliteral_instantiation(instance):
    assert isinstance(instance, roverDSL_BSensorLiteral)



@given(instance=roverDSL_BSensorLiteral_strategy)
def test_roverdsl_bsensorliteral_sensor_setter(instance):
    original = instance.sensor
    instance.sensor = original
    assert instance.sensor == original

@given(instance=roverDSL_BNotExpr_strategy)
@settings(max_examples=50)
def test_roverdsl_bnotexpr_instantiation(instance):
    assert isinstance(instance, roverDSL_BNotExpr)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=roverDSL_SoundAction_strategy)
@settings(max_examples=50)
def test_roverdsl_soundaction_instantiation(instance):
    assert isinstance(instance, roverDSL_SoundAction)



@given(instance=roverDSL_SoundAction_strategy)
def test_roverdsl_soundaction_sound_setter(instance):
    original = instance.sound
    instance.sound = original
    assert instance.sound == original

@given(instance=roverDSL_ShowAction_strategy)
@settings(max_examples=50)
def test_roverdsl_showaction_instantiation(instance):
    assert isinstance(instance, roverDSL_ShowAction)



@given(instance=roverDSL_ShowAction_strategy)
def test_roverdsl_showaction_string_setter(instance):
    original = instance.string
    instance.string = original
    assert instance.string == original



@given(instance=roverDSL_ShowAction_strategy)
def test_roverdsl_showaction_sensor_setter(instance):
    original = instance.sensor
    instance.sensor = original
    assert instance.sensor == original

@given(instance=roverDSL_SAccelerationAction_strategy)
@settings(max_examples=50)
def test_roverdsl_saccelerationaction_instantiation(instance):
    assert isinstance(instance, roverDSL_SAccelerationAction)

@given(instance=roverDSL_StopAction_strategy)
@settings(max_examples=50)
def test_roverdsl_stopaction_instantiation(instance):
    assert isinstance(instance, roverDSL_StopAction)

@given(instance=roverDSL_SSpeedAction_strategy)
@settings(max_examples=50)
def test_roverdsl_sspeedaction_instantiation(instance):
    assert isinstance(instance, roverDSL_SSpeedAction)

@given(instance=roverDSL_MeasureAction_strategy)
@settings(max_examples=50)
def test_roverdsl_measureaction_instantiation(instance):
    assert isinstance(instance, roverDSL_MeasureAction)

@given(instance=roverDSL_FreeAction_strategy)
@settings(max_examples=50)
def test_roverdsl_freeaction_instantiation(instance):
    assert isinstance(instance, roverDSL_FreeAction)

@given(instance=roverDSL_SubRoutineAction_strategy)
@settings(max_examples=50)
def test_roverdsl_subroutineaction_instantiation(instance):
    assert isinstance(instance, roverDSL_SubRoutineAction)

@given(instance=roverDSL_RotateAction_strategy)
@settings(max_examples=50)
def test_roverdsl_rotateaction_instantiation(instance):
    assert isinstance(instance, roverDSL_RotateAction)



@given(instance=roverDSL_RotateAction_strategy)
def test_roverdsl_rotateaction_blocking_setter(instance):
    original = instance.blocking
    instance.blocking = original
    assert instance.blocking == original

@given(instance=roverDSL_ForwardAction_strategy)
@settings(max_examples=50)
def test_roverdsl_forwardaction_instantiation(instance):
    assert isinstance(instance, roverDSL_ForwardAction)

@given(instance=roverDSL_Motor_strategy)
@settings(max_examples=50)
def test_roverdsl_motor_instantiation(instance):
    assert isinstance(instance, roverDSL_Motor)



@given(instance=roverDSL_Motor_strategy)
def test_roverdsl_motor_m_setter(instance):
    original = instance.m
    instance.m = original
    assert instance.m == original

@given(instance=Expression_strategy)
@settings(max_examples=50)
def test_expression_instantiation(instance):
    assert isinstance(instance, Expression)

@given(instance=roverDSL_Action_strategy)
@settings(max_examples=50)
def test_roverdsl_action_instantiation(instance):
    assert isinstance(instance, roverDSL_Action)

@given(instance=roverDSL_IFExpression_strategy)
@settings(max_examples=50)
def test_roverdsl_ifexpression_instantiation(instance):
    assert isinstance(instance, roverDSL_IFExpression)

@given(instance=roverDSL_WHILEExpression_strategy)
@settings(max_examples=50)
def test_roverdsl_whileexpression_instantiation(instance):
    assert isinstance(instance, roverDSL_WHILEExpression)

@given(instance=roverDSL_AssignExpression_strategy)
@settings(max_examples=50)
def test_roverdsl_assignexpression_instantiation(instance):
    assert isinstance(instance, roverDSL_AssignExpression)

@given(instance=roverDSL_ValExpr_strategy)
@settings(max_examples=50)
def test_roverdsl_valexpr_instantiation(instance):
    assert isinstance(instance, roverDSL_ValExpr)

@given(instance=roverDSL_Expression_strategy)
@settings(max_examples=50)
def test_roverdsl_expression_instantiation(instance):
    assert isinstance(instance, roverDSL_Expression)

@given(instance=roverDSL_SubRoutine_strategy)
@settings(max_examples=50)
def test_roverdsl_subroutine_instantiation(instance):
    assert isinstance(instance, roverDSL_SubRoutine)



@given(instance=roverDSL_SubRoutine_strategy)
def test_roverdsl_subroutine_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverDSL_Implementation_strategy)
@settings(max_examples=50)
def test_roverdsl_implementation_instantiation(instance):
    assert isinstance(instance, roverDSL_Implementation)

@given(instance=roverDSL_ValueExpression_strategy)
@settings(max_examples=50)
def test_roverdsl_valueexpression_instantiation(instance):
    assert isinstance(instance, roverDSL_ValueExpression)

@given(instance=roverDSL_Static_strategy)
@settings(max_examples=50)
def test_roverdsl_static_instantiation(instance):
    assert isinstance(instance, roverDSL_Static)



@given(instance=roverDSL_Static_strategy)
def test_roverdsl_static_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverDSL_Global_strategy)
@settings(max_examples=50)
def test_roverdsl_global_instantiation(instance):
    assert isinstance(instance, roverDSL_Global)



@given(instance=roverDSL_Global_strategy)
def test_roverdsl_global_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverDSL_BehaviorName_strategy)
@settings(max_examples=50)
def test_roverdsl_behaviorname_instantiation(instance):
    assert isinstance(instance, roverDSL_BehaviorName)



@given(instance=roverDSL_BehaviorName_strategy)
def test_roverdsl_behaviorname_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=roverDSL_Robot_strategy)
@settings(max_examples=50)
def test_roverdsl_robot_instantiation(instance):
    assert isinstance(instance, roverDSL_Robot)
