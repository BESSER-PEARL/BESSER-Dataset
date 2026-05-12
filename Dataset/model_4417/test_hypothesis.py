import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Sensor,
    mindstorms_UltrasonicSensor,
    mindstorms_ColorSensor,
    mindstorms_TouchSensor,
    Action,
    mindstorms_Rotate,
    mindstorms_GoTo,
    mindstorms_GoBackward,
    mindstorms_Grab,
    mindstorms_Delay,
    mindstorms_Release,
    mindstorms_ReturnToBase,
    mindstorms_GoForward,
    ConditionalFlow,
    mindstorms_While,
    mindstorms_If,
    Condition,
    mindstorms_Sensor,
    mindstorms_Condition,
    Flow,
    mindstorms_ConditionalFlow,
    mindstorms_Choregraphy,
    Instruction,
    mindstorms_Action,
    mindstorms_Reuse,
    mindstorms_Flow,
    mindstorms_Instruction,
    Color,
    OperatorKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sensor_is_not_abstract():
    assert not inspect.isabstract(Sensor)


def test_sensor_constructor_exists():
    assert callable(Sensor.__init__)


def test_sensor_constructor_args():
    sig = inspect.signature(Sensor.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_ultrasonicsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms_UltrasonicSensor)


def test_mindstorms_ultrasonicsensor_constructor_exists():
    assert callable(mindstorms_UltrasonicSensor.__init__)


def test_mindstorms_ultrasonicsensor_constructor_args():
    sig = inspect.signature(mindstorms_UltrasonicSensor.__init__)
    params = list(sig.parameters.keys())
    assert "operator" in params, "Missing parameter 'operator'"
    assert "value" in params, "Missing parameter 'value'"

def test_mindstorms_ultrasonicsensor_has_operator():
    assert hasattr(mindstorms_UltrasonicSensor, "operator")
    descriptor = None
    for klass in mindstorms_UltrasonicSensor.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms_ultrasonicsensor_has_value():
    assert hasattr(mindstorms_UltrasonicSensor, "value")
    descriptor = None
    for klass in mindstorms_UltrasonicSensor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_colorsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ColorSensor)


def test_mindstorms_colorsensor_constructor_exists():
    assert callable(mindstorms_ColorSensor.__init__)


def test_mindstorms_colorsensor_constructor_args():
    sig = inspect.signature(mindstorms_ColorSensor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_mindstorms_colorsensor_has_color():
    assert hasattr(mindstorms_ColorSensor, "color")
    descriptor = None
    for klass in mindstorms_ColorSensor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_touchsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms_TouchSensor)


def test_mindstorms_touchsensor_constructor_exists():
    assert callable(mindstorms_TouchSensor.__init__)


def test_mindstorms_touchsensor_constructor_args():
    sig = inspect.signature(mindstorms_TouchSensor.__init__)
    params = list(sig.parameters.keys())
    assert "isPressed" in params, "Missing parameter 'isPressed'"

def test_mindstorms_touchsensor_has_isPressed():
    assert hasattr(mindstorms_TouchSensor, "isPressed")
    descriptor = None
    for klass in mindstorms_TouchSensor.__mro__:
        if "isPressed" in klass.__dict__:
            descriptor = klass.__dict__["isPressed"]
            break
    assert isinstance(descriptor, property)



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_rotate_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Rotate)


def test_mindstorms_rotate_constructor_exists():
    assert callable(mindstorms_Rotate.__init__)


def test_mindstorms_rotate_constructor_args():
    sig = inspect.signature(mindstorms_Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "degrees" in params, "Missing parameter 'degrees'"
    assert "random" in params, "Missing parameter 'random'"

def test_mindstorms_rotate_has_degrees():
    assert hasattr(mindstorms_Rotate, "degrees")
    descriptor = None
    for klass in mindstorms_Rotate.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms_rotate_has_random():
    assert hasattr(mindstorms_Rotate, "random")
    descriptor = None
    for klass in mindstorms_Rotate.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_goto_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoTo)


def test_mindstorms_goto_constructor_exists():
    assert callable(mindstorms_GoTo.__init__)


def test_mindstorms_goto_constructor_args():
    sig = inspect.signature(mindstorms_GoTo.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_mindstorms_goto_has_y():
    assert hasattr(mindstorms_GoTo, "y")
    descriptor = None
    for klass in mindstorms_GoTo.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms_goto_has_x():
    assert hasattr(mindstorms_GoTo, "x")
    descriptor = None
    for klass in mindstorms_GoTo.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_gobackward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoBackward)


def test_mindstorms_gobackward_constructor_exists():
    assert callable(mindstorms_GoBackward.__init__)


def test_mindstorms_gobackward_constructor_args():
    sig = inspect.signature(mindstorms_GoBackward.__init__)
    params = list(sig.parameters.keys())
    assert "infinite" in params, "Missing parameter 'infinite'"
    assert "cm" in params, "Missing parameter 'cm'"

def test_mindstorms_gobackward_has_infinite():
    assert hasattr(mindstorms_GoBackward, "infinite")
    descriptor = None
    for klass in mindstorms_GoBackward.__mro__:
        if "infinite" in klass.__dict__:
            descriptor = klass.__dict__["infinite"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms_gobackward_has_cm():
    assert hasattr(mindstorms_GoBackward, "cm")
    descriptor = None
    for klass in mindstorms_GoBackward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_grab_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Grab)


def test_mindstorms_grab_constructor_exists():
    assert callable(mindstorms_Grab.__init__)


def test_mindstorms_grab_constructor_args():
    sig = inspect.signature(mindstorms_Grab.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_delay_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Delay)


def test_mindstorms_delay_constructor_exists():
    assert callable(mindstorms_Delay.__init__)


def test_mindstorms_delay_constructor_args():
    sig = inspect.signature(mindstorms_Delay.__init__)
    params = list(sig.parameters.keys())
    assert "ms" in params, "Missing parameter 'ms'"

def test_mindstorms_delay_has_ms():
    assert hasattr(mindstorms_Delay, "ms")
    descriptor = None
    for klass in mindstorms_Delay.__mro__:
        if "ms" in klass.__dict__:
            descriptor = klass.__dict__["ms"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms_release_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Release)


def test_mindstorms_release_constructor_exists():
    assert callable(mindstorms_Release.__init__)


def test_mindstorms_release_constructor_args():
    sig = inspect.signature(mindstorms_Release.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_returntobase_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ReturnToBase)


def test_mindstorms_returntobase_constructor_exists():
    assert callable(mindstorms_ReturnToBase.__init__)


def test_mindstorms_returntobase_constructor_args():
    sig = inspect.signature(mindstorms_ReturnToBase.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_goforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms_GoForward)


def test_mindstorms_goforward_constructor_exists():
    assert callable(mindstorms_GoForward.__init__)


def test_mindstorms_goforward_constructor_args():
    sig = inspect.signature(mindstorms_GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "cm" in params, "Missing parameter 'cm'"
    assert "infinite" in params, "Missing parameter 'infinite'"

def test_mindstorms_goforward_has_cm():
    assert hasattr(mindstorms_GoForward, "cm")
    descriptor = None
    for klass in mindstorms_GoForward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms_goforward_has_infinite():
    assert hasattr(mindstorms_GoForward, "infinite")
    descriptor = None
    for klass in mindstorms_GoForward.__mro__:
        if "infinite" in klass.__dict__:
            descriptor = klass.__dict__["infinite"]
            break
    assert isinstance(descriptor, property)



def test_conditionalflow_is_not_abstract():
    assert not inspect.isabstract(ConditionalFlow)


def test_conditionalflow_constructor_exists():
    assert callable(ConditionalFlow.__init__)


def test_conditionalflow_constructor_args():
    sig = inspect.signature(ConditionalFlow.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_while_is_not_abstract():
    assert not inspect.isabstract(mindstorms_While)


def test_mindstorms_while_constructor_exists():
    assert callable(mindstorms_While.__init__)


def test_mindstorms_while_constructor_args():
    sig = inspect.signature(mindstorms_While.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_if_is_not_abstract():
    assert not inspect.isabstract(mindstorms_If)


def test_mindstorms_if_constructor_exists():
    assert callable(mindstorms_If.__init__)


def test_mindstorms_if_constructor_args():
    sig = inspect.signature(mindstorms_If.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_sensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Sensor)


def test_mindstorms_sensor_constructor_exists():
    assert callable(mindstorms_Sensor.__init__)


def test_mindstorms_sensor_constructor_args():
    sig = inspect.signature(mindstorms_Sensor.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_condition_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Condition)


def test_mindstorms_condition_constructor_exists():
    assert callable(mindstorms_Condition.__init__)


def test_mindstorms_condition_constructor_args():
    sig = inspect.signature(mindstorms_Condition.__init__)
    params = list(sig.parameters.keys())



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_conditionalflow_is_not_abstract():
    assert not inspect.isabstract(mindstorms_ConditionalFlow)


def test_mindstorms_conditionalflow_constructor_exists():
    assert callable(mindstorms_ConditionalFlow.__init__)


def test_mindstorms_conditionalflow_constructor_args():
    sig = inspect.signature(mindstorms_ConditionalFlow.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_choregraphy_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Choregraphy)


def test_mindstorms_choregraphy_constructor_exists():
    assert callable(mindstorms_Choregraphy.__init__)


def test_mindstorms_choregraphy_constructor_args():
    sig = inspect.signature(mindstorms_Choregraphy.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mindstorms_choregraphy_has_name():
    assert hasattr(mindstorms_Choregraphy, "name")
    descriptor = None
    for klass in mindstorms_Choregraphy.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_action_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Action)


def test_mindstorms_action_constructor_exists():
    assert callable(mindstorms_Action.__init__)


def test_mindstorms_action_constructor_args():
    sig = inspect.signature(mindstorms_Action.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_reuse_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Reuse)


def test_mindstorms_reuse_constructor_exists():
    assert callable(mindstorms_Reuse.__init__)


def test_mindstorms_reuse_constructor_args():
    sig = inspect.signature(mindstorms_Reuse.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_flow_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Flow)


def test_mindstorms_flow_constructor_exists():
    assert callable(mindstorms_Flow.__init__)


def test_mindstorms_flow_constructor_args():
    sig = inspect.signature(mindstorms_Flow.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms_instruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms_Instruction)


def test_mindstorms_instruction_constructor_exists():
    assert callable(mindstorms_Instruction.__init__)


def test_mindstorms_instruction_constructor_args():
    sig = inspect.signature(mindstorms_Instruction.__init__)
    params = list(sig.parameters.keys())

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "YELLOW",
        "MAGENTA",
        "CYAN",
        "LIGHT_GRAY",
        "NONE",
        "RED",
        "GRAY",
        "GREEN",
        "ORANGE",
        "BLACK",
        "DARK_GRAY",
        "WHITE",
        "BROWN",
        "PINK",
        "BLUE",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"

def test_operatorkind_exists():
    # Check that the Enumeration exists
    assert OperatorKind is not None

def test_operatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorKind]
    expected_literals = [
        "upperOrEqual",
        "lowerOrEqual",
        "notEqual",
        "equal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorKind"


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
Sensor_strategy = st.builds(
    Sensor,
)
mindstorms_UltrasonicSensor_strategy = st.builds(
    mindstorms_UltrasonicSensor,
    operator=
        safe_text,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
mindstorms_ColorSensor_strategy = st.builds(
    mindstorms_ColorSensor,
    color=
        safe_text
)
mindstorms_TouchSensor_strategy = st.builds(
    mindstorms_TouchSensor,
    isPressed=
        st.booleans()
)
Action_strategy = st.builds(
    Action,
)
mindstorms_Rotate_strategy = st.builds(
    mindstorms_Rotate,
    degrees=
        st.integers(),
    random=
        st.booleans()
)
mindstorms_GoTo_strategy = st.builds(
    mindstorms_GoTo,
    y=
        st.integers(),
    x=
        st.integers()
)
mindstorms_GoBackward_strategy = st.builds(
    mindstorms_GoBackward,
    infinite=
        st.booleans(),
    cm=
        st.integers()
)
mindstorms_Grab_strategy = st.builds(
    mindstorms_Grab,
)
mindstorms_Delay_strategy = st.builds(
    mindstorms_Delay,
    ms=
        st.integers()
)
mindstorms_Release_strategy = st.builds(
    mindstorms_Release,
)
mindstorms_ReturnToBase_strategy = st.builds(
    mindstorms_ReturnToBase,
)
mindstorms_GoForward_strategy = st.builds(
    mindstorms_GoForward,
    cm=
        st.integers(),
    infinite=
        st.booleans()
)
ConditionalFlow_strategy = st.builds(
    ConditionalFlow,
)
mindstorms_While_strategy = st.builds(
    mindstorms_While,
)
mindstorms_If_strategy = st.builds(
    mindstorms_If,
)
Condition_strategy = st.builds(
    Condition,
)
mindstorms_Sensor_strategy = st.builds(
    mindstorms_Sensor,
)
mindstorms_Condition_strategy = st.builds(
    mindstorms_Condition,
)
Flow_strategy = st.builds(
    Flow,
)
mindstorms_ConditionalFlow_strategy = st.builds(
    mindstorms_ConditionalFlow,
)
mindstorms_Choregraphy_strategy = st.builds(
    mindstorms_Choregraphy,
    name=
        safe_text
)
Instruction_strategy = st.builds(
    Instruction,
)
mindstorms_Action_strategy = st.builds(
    mindstorms_Action,
)
mindstorms_Reuse_strategy = st.builds(
    mindstorms_Reuse,
)
mindstorms_Flow_strategy = st.builds(
    mindstorms_Flow,
)
mindstorms_Instruction_strategy = st.builds(
    mindstorms_Instruction,
)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=mindstorms_UltrasonicSensor_strategy)
@settings(max_examples=50)
def test_mindstorms_ultrasonicsensor_instantiation(instance):
    assert isinstance(instance, mindstorms_UltrasonicSensor)



@given(instance=mindstorms_UltrasonicSensor_strategy)
def test_mindstorms_ultrasonicsensor_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original



@given(instance=mindstorms_UltrasonicSensor_strategy)
def test_mindstorms_ultrasonicsensor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mindstorms_ColorSensor_strategy)
@settings(max_examples=50)
def test_mindstorms_colorsensor_instantiation(instance):
    assert isinstance(instance, mindstorms_ColorSensor)



@given(instance=mindstorms_ColorSensor_strategy)
def test_mindstorms_colorsensor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=mindstorms_TouchSensor_strategy)
@settings(max_examples=50)
def test_mindstorms_touchsensor_instantiation(instance):
    assert isinstance(instance, mindstorms_TouchSensor)



@given(instance=mindstorms_TouchSensor_strategy)
def test_mindstorms_touchsensor_isPressed_setter(instance):
    original = instance.isPressed
    instance.isPressed = original
    assert instance.isPressed == original

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=mindstorms_Rotate_strategy)
@settings(max_examples=50)
def test_mindstorms_rotate_instantiation(instance):
    assert isinstance(instance, mindstorms_Rotate)



@given(instance=mindstorms_Rotate_strategy)
def test_mindstorms_rotate_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original



@given(instance=mindstorms_Rotate_strategy)
def test_mindstorms_rotate_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original

@given(instance=mindstorms_GoTo_strategy)
@settings(max_examples=50)
def test_mindstorms_goto_instantiation(instance):
    assert isinstance(instance, mindstorms_GoTo)



@given(instance=mindstorms_GoTo_strategy)
def test_mindstorms_goto_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=mindstorms_GoTo_strategy)
def test_mindstorms_goto_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mindstorms_GoBackward_strategy)
@settings(max_examples=50)
def test_mindstorms_gobackward_instantiation(instance):
    assert isinstance(instance, mindstorms_GoBackward)



@given(instance=mindstorms_GoBackward_strategy)
def test_mindstorms_gobackward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original



@given(instance=mindstorms_GoBackward_strategy)
def test_mindstorms_gobackward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=mindstorms_Grab_strategy)
@settings(max_examples=50)
def test_mindstorms_grab_instantiation(instance):
    assert isinstance(instance, mindstorms_Grab)

@given(instance=mindstorms_Delay_strategy)
@settings(max_examples=50)
def test_mindstorms_delay_instantiation(instance):
    assert isinstance(instance, mindstorms_Delay)



@given(instance=mindstorms_Delay_strategy)
def test_mindstorms_delay_ms_setter(instance):
    original = instance.ms
    instance.ms = original
    assert instance.ms == original

@given(instance=mindstorms_Release_strategy)
@settings(max_examples=50)
def test_mindstorms_release_instantiation(instance):
    assert isinstance(instance, mindstorms_Release)

@given(instance=mindstorms_ReturnToBase_strategy)
@settings(max_examples=50)
def test_mindstorms_returntobase_instantiation(instance):
    assert isinstance(instance, mindstorms_ReturnToBase)

@given(instance=mindstorms_GoForward_strategy)
@settings(max_examples=50)
def test_mindstorms_goforward_instantiation(instance):
    assert isinstance(instance, mindstorms_GoForward)



@given(instance=mindstorms_GoForward_strategy)
def test_mindstorms_goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original



@given(instance=mindstorms_GoForward_strategy)
def test_mindstorms_goforward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original

@given(instance=ConditionalFlow_strategy)
@settings(max_examples=50)
def test_conditionalflow_instantiation(instance):
    assert isinstance(instance, ConditionalFlow)

@given(instance=mindstorms_While_strategy)
@settings(max_examples=50)
def test_mindstorms_while_instantiation(instance):
    assert isinstance(instance, mindstorms_While)

@given(instance=mindstorms_If_strategy)
@settings(max_examples=50)
def test_mindstorms_if_instantiation(instance):
    assert isinstance(instance, mindstorms_If)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=mindstorms_Sensor_strategy)
@settings(max_examples=50)
def test_mindstorms_sensor_instantiation(instance):
    assert isinstance(instance, mindstorms_Sensor)

@given(instance=mindstorms_Condition_strategy)
@settings(max_examples=50)
def test_mindstorms_condition_instantiation(instance):
    assert isinstance(instance, mindstorms_Condition)

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=mindstorms_ConditionalFlow_strategy)
@settings(max_examples=50)
def test_mindstorms_conditionalflow_instantiation(instance):
    assert isinstance(instance, mindstorms_ConditionalFlow)

@given(instance=mindstorms_Choregraphy_strategy)
@settings(max_examples=50)
def test_mindstorms_choregraphy_instantiation(instance):
    assert isinstance(instance, mindstorms_Choregraphy)



@given(instance=mindstorms_Choregraphy_strategy)
def test_mindstorms_choregraphy_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=mindstorms_Action_strategy)
@settings(max_examples=50)
def test_mindstorms_action_instantiation(instance):
    assert isinstance(instance, mindstorms_Action)

@given(instance=mindstorms_Reuse_strategy)
@settings(max_examples=50)
def test_mindstorms_reuse_instantiation(instance):
    assert isinstance(instance, mindstorms_Reuse)

@given(instance=mindstorms_Flow_strategy)
@settings(max_examples=50)
def test_mindstorms_flow_instantiation(instance):
    assert isinstance(instance, mindstorms_Flow)

@given(instance=mindstorms_Instruction_strategy)
@settings(max_examples=50)
def test_mindstorms_instruction_instantiation(instance):
    assert isinstance(instance, mindstorms_Instruction)
