import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Sensor,
    mindstorms::ColorSensor,
    mindstorms::UltrasonicSensor,
    mindstorms::TouchSensor,
    Behavior,
    mindstorms::ExploreForward,
    mindstorms::ReturnBottleToBase,
    mindstorms::AvoidObstacle,
    mindstorms::ConditionContainer,
    ConditionContainer,
    BlockContainer,
    Instruction,
    mindstorms::Arbitrator,
    mindstorms::ReuseInstruction,
    mindstorms::Procedure,
    mindstorms::Block,
    mindstorms::BlockContainer,
    NamedElement,
    mindstorms::Behavior,
    mindstorms::Instruction,
    mindstorms::Main,
    Action,
    mindstorms::GoBackward,
    mindstorms::GoToEnemy,
    mindstorms::ReturnToBase,
    mindstorms::Delay,
    mindstorms::GoTo,
    mindstorms::Grab,
    mindstorms::Release,
    mindstorms::Rotate,
    mindstorms::GoForward,
    Flow,
    mindstorms::While,
    mindstorms::If,
    mindstorms::Condition,
    Condition,
    mindstorms::Sensor,
    Block,
    mindstorms::Flow,
    mindstorms::Action,
    mindstorms::NamedElement,
    OperatorKind,
    Color,
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



def test_mindstorms::colorsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms::ColorSensor)


def test_mindstorms::colorsensor_constructor_exists():
    assert callable(mindstorms::ColorSensor.__init__)


def test_mindstorms::colorsensor_constructor_args():
    sig = inspect.signature(mindstorms::ColorSensor.__init__)
    params = list(sig.parameters.keys())
    assert "color" in params, "Missing parameter 'color'"

def test_mindstorms::colorsensor_has_color():
    assert hasattr(mindstorms::ColorSensor, "color")
    descriptor = None
    for klass in mindstorms::ColorSensor.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::ultrasonicsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms::UltrasonicSensor)


def test_mindstorms::ultrasonicsensor_constructor_exists():
    assert callable(mindstorms::UltrasonicSensor.__init__)


def test_mindstorms::ultrasonicsensor_constructor_args():
    sig = inspect.signature(mindstorms::UltrasonicSensor.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "operator" in params, "Missing parameter 'operator'"

def test_mindstorms::ultrasonicsensor_has_value():
    assert hasattr(mindstorms::UltrasonicSensor, "value")
    descriptor = None
    for klass in mindstorms::UltrasonicSensor.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms::ultrasonicsensor_has_operator():
    assert hasattr(mindstorms::UltrasonicSensor, "operator")
    descriptor = None
    for klass in mindstorms::UltrasonicSensor.__mro__:
        if "operator" in klass.__dict__:
            descriptor = klass.__dict__["operator"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::touchsensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms::TouchSensor)


def test_mindstorms::touchsensor_constructor_exists():
    assert callable(mindstorms::TouchSensor.__init__)


def test_mindstorms::touchsensor_constructor_args():
    sig = inspect.signature(mindstorms::TouchSensor.__init__)
    params = list(sig.parameters.keys())
    assert "isPressed" in params, "Missing parameter 'isPressed'"

def test_mindstorms::touchsensor_has_isPressed():
    assert hasattr(mindstorms::TouchSensor, "isPressed")
    descriptor = None
    for klass in mindstorms::TouchSensor.__mro__:
        if "isPressed" in klass.__dict__:
            descriptor = klass.__dict__["isPressed"]
            break
    assert isinstance(descriptor, property)



def test_behavior_is_not_abstract():
    assert not inspect.isabstract(Behavior)


def test_behavior_constructor_exists():
    assert callable(Behavior.__init__)


def test_behavior_constructor_args():
    sig = inspect.signature(Behavior.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::exploreforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms::ExploreForward)


def test_mindstorms::exploreforward_constructor_exists():
    assert callable(mindstorms::ExploreForward.__init__)


def test_mindstorms::exploreforward_constructor_args():
    sig = inspect.signature(mindstorms::ExploreForward.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::returnbottletobase_is_not_abstract():
    assert not inspect.isabstract(mindstorms::ReturnBottleToBase)


def test_mindstorms::returnbottletobase_constructor_exists():
    assert callable(mindstorms::ReturnBottleToBase.__init__)


def test_mindstorms::returnbottletobase_constructor_args():
    sig = inspect.signature(mindstorms::ReturnBottleToBase.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::avoidobstacle_is_not_abstract():
    assert not inspect.isabstract(mindstorms::AvoidObstacle)


def test_mindstorms::avoidobstacle_constructor_exists():
    assert callable(mindstorms::AvoidObstacle.__init__)


def test_mindstorms::avoidobstacle_constructor_args():
    sig = inspect.signature(mindstorms::AvoidObstacle.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::conditioncontainer_is_not_abstract():
    assert not inspect.isabstract(mindstorms::ConditionContainer)


def test_mindstorms::conditioncontainer_constructor_exists():
    assert callable(mindstorms::ConditionContainer.__init__)


def test_mindstorms::conditioncontainer_constructor_args():
    sig = inspect.signature(mindstorms::ConditionContainer.__init__)
    params = list(sig.parameters.keys())



def test_conditioncontainer_is_not_abstract():
    assert not inspect.isabstract(ConditionContainer)


def test_conditioncontainer_constructor_exists():
    assert callable(ConditionContainer.__init__)


def test_conditioncontainer_constructor_args():
    sig = inspect.signature(ConditionContainer.__init__)
    params = list(sig.parameters.keys())



def test_blockcontainer_is_not_abstract():
    assert not inspect.isabstract(BlockContainer)


def test_blockcontainer_constructor_exists():
    assert callable(BlockContainer.__init__)


def test_blockcontainer_constructor_args():
    sig = inspect.signature(BlockContainer.__init__)
    params = list(sig.parameters.keys())



def test_instruction_is_not_abstract():
    assert not inspect.isabstract(Instruction)


def test_instruction_constructor_exists():
    assert callable(Instruction.__init__)


def test_instruction_constructor_args():
    sig = inspect.signature(Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::arbitrator_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Arbitrator)


def test_mindstorms::arbitrator_constructor_exists():
    assert callable(mindstorms::Arbitrator.__init__)


def test_mindstorms::arbitrator_constructor_args():
    sig = inspect.signature(mindstorms::Arbitrator.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::reuseinstruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms::ReuseInstruction)


def test_mindstorms::reuseinstruction_constructor_exists():
    assert callable(mindstorms::ReuseInstruction.__init__)


def test_mindstorms::reuseinstruction_constructor_args():
    sig = inspect.signature(mindstorms::ReuseInstruction.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::procedure_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Procedure)


def test_mindstorms::procedure_constructor_exists():
    assert callable(mindstorms::Procedure.__init__)


def test_mindstorms::procedure_constructor_args():
    sig = inspect.signature(mindstorms::Procedure.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::block_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Block)


def test_mindstorms::block_constructor_exists():
    assert callable(mindstorms::Block.__init__)


def test_mindstorms::block_constructor_args():
    sig = inspect.signature(mindstorms::Block.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::blockcontainer_is_not_abstract():
    assert not inspect.isabstract(mindstorms::BlockContainer)


def test_mindstorms::blockcontainer_constructor_exists():
    assert callable(mindstorms::BlockContainer.__init__)


def test_mindstorms::blockcontainer_constructor_args():
    sig = inspect.signature(mindstorms::BlockContainer.__init__)
    params = list(sig.parameters.keys())



def test_namedelement_is_not_abstract():
    assert not inspect.isabstract(NamedElement)


def test_namedelement_constructor_exists():
    assert callable(NamedElement.__init__)


def test_namedelement_constructor_args():
    sig = inspect.signature(NamedElement.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::behavior_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Behavior)


def test_mindstorms::behavior_constructor_exists():
    assert callable(mindstorms::Behavior.__init__)


def test_mindstorms::behavior_constructor_args():
    sig = inspect.signature(mindstorms::Behavior.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::instruction_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Instruction)


def test_mindstorms::instruction_constructor_exists():
    assert callable(mindstorms::Instruction.__init__)


def test_mindstorms::instruction_constructor_args():
    sig = inspect.signature(mindstorms::Instruction.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::main_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Main)


def test_mindstorms::main_constructor_exists():
    assert callable(mindstorms::Main.__init__)


def test_mindstorms::main_constructor_args():
    sig = inspect.signature(mindstorms::Main.__init__)
    params = list(sig.parameters.keys())



def test_action_is_not_abstract():
    assert not inspect.isabstract(Action)


def test_action_constructor_exists():
    assert callable(Action.__init__)


def test_action_constructor_args():
    sig = inspect.signature(Action.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::gobackward_is_not_abstract():
    assert not inspect.isabstract(mindstorms::GoBackward)


def test_mindstorms::gobackward_constructor_exists():
    assert callable(mindstorms::GoBackward.__init__)


def test_mindstorms::gobackward_constructor_args():
    sig = inspect.signature(mindstorms::GoBackward.__init__)
    params = list(sig.parameters.keys())
    assert "infinite" in params, "Missing parameter 'infinite'"
    assert "cm" in params, "Missing parameter 'cm'"

def test_mindstorms::gobackward_has_infinite():
    assert hasattr(mindstorms::GoBackward, "infinite")
    descriptor = None
    for klass in mindstorms::GoBackward.__mro__:
        if "infinite" in klass.__dict__:
            descriptor = klass.__dict__["infinite"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms::gobackward_has_cm():
    assert hasattr(mindstorms::GoBackward, "cm")
    descriptor = None
    for klass in mindstorms::GoBackward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::gotoenemy_is_not_abstract():
    assert not inspect.isabstract(mindstorms::GoToEnemy)


def test_mindstorms::gotoenemy_constructor_exists():
    assert callable(mindstorms::GoToEnemy.__init__)


def test_mindstorms::gotoenemy_constructor_args():
    sig = inspect.signature(mindstorms::GoToEnemy.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::returntobase_is_not_abstract():
    assert not inspect.isabstract(mindstorms::ReturnToBase)


def test_mindstorms::returntobase_constructor_exists():
    assert callable(mindstorms::ReturnToBase.__init__)


def test_mindstorms::returntobase_constructor_args():
    sig = inspect.signature(mindstorms::ReturnToBase.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::delay_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Delay)


def test_mindstorms::delay_constructor_exists():
    assert callable(mindstorms::Delay.__init__)


def test_mindstorms::delay_constructor_args():
    sig = inspect.signature(mindstorms::Delay.__init__)
    params = list(sig.parameters.keys())
    assert "ms" in params, "Missing parameter 'ms'"

def test_mindstorms::delay_has_ms():
    assert hasattr(mindstorms::Delay, "ms")
    descriptor = None
    for klass in mindstorms::Delay.__mro__:
        if "ms" in klass.__dict__:
            descriptor = klass.__dict__["ms"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::goto_is_not_abstract():
    assert not inspect.isabstract(mindstorms::GoTo)


def test_mindstorms::goto_constructor_exists():
    assert callable(mindstorms::GoTo.__init__)


def test_mindstorms::goto_constructor_args():
    sig = inspect.signature(mindstorms::GoTo.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "x" in params, "Missing parameter 'x'"

def test_mindstorms::goto_has_y():
    assert hasattr(mindstorms::GoTo, "y")
    descriptor = None
    for klass in mindstorms::GoTo.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms::goto_has_x():
    assert hasattr(mindstorms::GoTo, "x")
    descriptor = None
    for klass in mindstorms::GoTo.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::grab_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Grab)


def test_mindstorms::grab_constructor_exists():
    assert callable(mindstorms::Grab.__init__)


def test_mindstorms::grab_constructor_args():
    sig = inspect.signature(mindstorms::Grab.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::release_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Release)


def test_mindstorms::release_constructor_exists():
    assert callable(mindstorms::Release.__init__)


def test_mindstorms::release_constructor_args():
    sig = inspect.signature(mindstorms::Release.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::rotate_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Rotate)


def test_mindstorms::rotate_constructor_exists():
    assert callable(mindstorms::Rotate.__init__)


def test_mindstorms::rotate_constructor_args():
    sig = inspect.signature(mindstorms::Rotate.__init__)
    params = list(sig.parameters.keys())
    assert "random" in params, "Missing parameter 'random'"
    assert "degrees" in params, "Missing parameter 'degrees'"

def test_mindstorms::rotate_has_random():
    assert hasattr(mindstorms::Rotate, "random")
    descriptor = None
    for klass in mindstorms::Rotate.__mro__:
        if "random" in klass.__dict__:
            descriptor = klass.__dict__["random"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms::rotate_has_degrees():
    assert hasattr(mindstorms::Rotate, "degrees")
    descriptor = None
    for klass in mindstorms::Rotate.__mro__:
        if "degrees" in klass.__dict__:
            descriptor = klass.__dict__["degrees"]
            break
    assert isinstance(descriptor, property)



def test_mindstorms::goforward_is_not_abstract():
    assert not inspect.isabstract(mindstorms::GoForward)


def test_mindstorms::goforward_constructor_exists():
    assert callable(mindstorms::GoForward.__init__)


def test_mindstorms::goforward_constructor_args():
    sig = inspect.signature(mindstorms::GoForward.__init__)
    params = list(sig.parameters.keys())
    assert "infinite" in params, "Missing parameter 'infinite'"
    assert "cm" in params, "Missing parameter 'cm'"

def test_mindstorms::goforward_has_infinite():
    assert hasattr(mindstorms::GoForward, "infinite")
    descriptor = None
    for klass in mindstorms::GoForward.__mro__:
        if "infinite" in klass.__dict__:
            descriptor = klass.__dict__["infinite"]
            break
    assert isinstance(descriptor, property)

def test_mindstorms::goforward_has_cm():
    assert hasattr(mindstorms::GoForward, "cm")
    descriptor = None
    for klass in mindstorms::GoForward.__mro__:
        if "cm" in klass.__dict__:
            descriptor = klass.__dict__["cm"]
            break
    assert isinstance(descriptor, property)



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::while_is_not_abstract():
    assert not inspect.isabstract(mindstorms::While)


def test_mindstorms::while_constructor_exists():
    assert callable(mindstorms::While.__init__)


def test_mindstorms::while_constructor_args():
    sig = inspect.signature(mindstorms::While.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::if_is_not_abstract():
    assert not inspect.isabstract(mindstorms::If)


def test_mindstorms::if_constructor_exists():
    assert callable(mindstorms::If.__init__)


def test_mindstorms::if_constructor_args():
    sig = inspect.signature(mindstorms::If.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::condition_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Condition)


def test_mindstorms::condition_constructor_exists():
    assert callable(mindstorms::Condition.__init__)


def test_mindstorms::condition_constructor_args():
    sig = inspect.signature(mindstorms::Condition.__init__)
    params = list(sig.parameters.keys())



def test_condition_is_not_abstract():
    assert not inspect.isabstract(Condition)


def test_condition_constructor_exists():
    assert callable(Condition.__init__)


def test_condition_constructor_args():
    sig = inspect.signature(Condition.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::sensor_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Sensor)


def test_mindstorms::sensor_constructor_exists():
    assert callable(mindstorms::Sensor.__init__)


def test_mindstorms::sensor_constructor_args():
    sig = inspect.signature(mindstorms::Sensor.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::flow_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Flow)


def test_mindstorms::flow_constructor_exists():
    assert callable(mindstorms::Flow.__init__)


def test_mindstorms::flow_constructor_args():
    sig = inspect.signature(mindstorms::Flow.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::action_is_not_abstract():
    assert not inspect.isabstract(mindstorms::Action)


def test_mindstorms::action_constructor_exists():
    assert callable(mindstorms::Action.__init__)


def test_mindstorms::action_constructor_args():
    sig = inspect.signature(mindstorms::Action.__init__)
    params = list(sig.parameters.keys())



def test_mindstorms::namedelement_is_not_abstract():
    assert not inspect.isabstract(mindstorms::NamedElement)


def test_mindstorms::namedelement_constructor_exists():
    assert callable(mindstorms::NamedElement.__init__)


def test_mindstorms::namedelement_constructor_args():
    sig = inspect.signature(mindstorms::NamedElement.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_mindstorms::namedelement_has_name():
    assert hasattr(mindstorms::NamedElement, "name")
    descriptor = None
    for klass in mindstorms::NamedElement.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_operatorkind_exists():
    # Check that the Enumeration exists
    assert OperatorKind is not None

def test_operatorkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OperatorKind]
    expected_literals = [
        "notEqual",
        "lowerOrEqual",
        "equal",
        "upperOrEqual",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OperatorKind"

def test_color_exists():
    # Check that the Enumeration exists
    assert Color is not None

def test_color_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Color]
    expected_literals = [
        "NONE",
        "MAGENTA",
        "WHITE",
        "GRAY",
        "BLUE",
        "PINK",
        "CYAN",
        "BROWN",
        "RED",
        "DARK_GRAY",
        "ORANGE",
        "GREEN",
        "BLACK",
        "YELLOW",
        "LIGHT_GRAY",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Color"


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
mindstorms::ColorSensor_strategy = st.builds(
    mindstorms::ColorSensor,
    color=
        safe_text
)
mindstorms::UltrasonicSensor_strategy = st.builds(
    mindstorms::UltrasonicSensor,
    value=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    operator=
        safe_text
)
mindstorms::TouchSensor_strategy = st.builds(
    mindstorms::TouchSensor,
    isPressed=
        st.booleans()
)
Behavior_strategy = st.builds(
    Behavior,
)
mindstorms::ExploreForward_strategy = st.builds(
    mindstorms::ExploreForward,
)
mindstorms::ReturnBottleToBase_strategy = st.builds(
    mindstorms::ReturnBottleToBase,
)
mindstorms::AvoidObstacle_strategy = st.builds(
    mindstorms::AvoidObstacle,
)
mindstorms::ConditionContainer_strategy = st.builds(
    mindstorms::ConditionContainer,
)
ConditionContainer_strategy = st.builds(
    ConditionContainer,
)
BlockContainer_strategy = st.builds(
    BlockContainer,
)
Instruction_strategy = st.builds(
    Instruction,
)
mindstorms::Arbitrator_strategy = st.builds(
    mindstorms::Arbitrator,
)
mindstorms::ReuseInstruction_strategy = st.builds(
    mindstorms::ReuseInstruction,
)
mindstorms::Procedure_strategy = st.builds(
    mindstorms::Procedure,
)
mindstorms::Block_strategy = st.builds(
    mindstorms::Block,
)
mindstorms::BlockContainer_strategy = st.builds(
    mindstorms::BlockContainer,
)
NamedElement_strategy = st.builds(
    NamedElement,
)
mindstorms::Behavior_strategy = st.builds(
    mindstorms::Behavior,
)
mindstorms::Instruction_strategy = st.builds(
    mindstorms::Instruction,
)
mindstorms::Main_strategy = st.builds(
    mindstorms::Main,
)
Action_strategy = st.builds(
    Action,
)
mindstorms::GoBackward_strategy = st.builds(
    mindstorms::GoBackward,
    infinite=
        st.booleans(),
    cm=
        st.integers()
)
mindstorms::GoToEnemy_strategy = st.builds(
    mindstorms::GoToEnemy,
)
mindstorms::ReturnToBase_strategy = st.builds(
    mindstorms::ReturnToBase,
)
mindstorms::Delay_strategy = st.builds(
    mindstorms::Delay,
    ms=
        st.integers()
)
mindstorms::GoTo_strategy = st.builds(
    mindstorms::GoTo,
    y=
        st.integers(),
    x=
        st.integers()
)
mindstorms::Grab_strategy = st.builds(
    mindstorms::Grab,
)
mindstorms::Release_strategy = st.builds(
    mindstorms::Release,
)
mindstorms::Rotate_strategy = st.builds(
    mindstorms::Rotate,
    random=
        st.booleans(),
    degrees=
        st.integers()
)
mindstorms::GoForward_strategy = st.builds(
    mindstorms::GoForward,
    infinite=
        st.booleans(),
    cm=
        st.integers()
)
Flow_strategy = st.builds(
    Flow,
)
mindstorms::While_strategy = st.builds(
    mindstorms::While,
)
mindstorms::If_strategy = st.builds(
    mindstorms::If,
)
mindstorms::Condition_strategy = st.builds(
    mindstorms::Condition,
)
Condition_strategy = st.builds(
    Condition,
)
mindstorms::Sensor_strategy = st.builds(
    mindstorms::Sensor,
)
Block_strategy = st.builds(
    Block,
)
mindstorms::Flow_strategy = st.builds(
    mindstorms::Flow,
)
mindstorms::Action_strategy = st.builds(
    mindstorms::Action,
)
mindstorms::NamedElement_strategy = st.builds(
    mindstorms::NamedElement,
    name=
        safe_text
)

@given(instance=Sensor_strategy)
@settings(max_examples=50)
def test_sensor_instantiation(instance):
    assert isinstance(instance, Sensor)

@given(instance=mindstorms::ColorSensor_strategy)
@settings(max_examples=50)
def test_mindstorms::colorsensor_instantiation(instance):
    assert isinstance(instance, mindstorms::ColorSensor)

@given(instance=mindstorms::ColorSensor_strategy)
def test_mindstorms::colorsensor_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=mindstorms::ColorSensor_strategy)
def test_mindstorms::colorsensor_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=mindstorms::UltrasonicSensor_strategy)
@settings(max_examples=50)
def test_mindstorms::ultrasonicsensor_instantiation(instance):
    assert isinstance(instance, mindstorms::UltrasonicSensor)

@given(instance=mindstorms::UltrasonicSensor_strategy)
def test_mindstorms::ultrasonicsensor_value_type(instance):
    assert isinstance(instance.value, float)


@given(instance=mindstorms::UltrasonicSensor_strategy)
def test_mindstorms::ultrasonicsensor_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=mindstorms::UltrasonicSensor_strategy)
def test_mindstorms::ultrasonicsensor_operator_type(instance):
    assert isinstance(instance.operator, str)


@given(instance=mindstorms::UltrasonicSensor_strategy)
def test_mindstorms::ultrasonicsensor_operator_setter(instance):
    original = instance.operator
    instance.operator = original
    assert instance.operator == original

@given(instance=mindstorms::TouchSensor_strategy)
@settings(max_examples=50)
def test_mindstorms::touchsensor_instantiation(instance):
    assert isinstance(instance, mindstorms::TouchSensor)

@given(instance=mindstorms::TouchSensor_strategy)
def test_mindstorms::touchsensor_isPressed_type(instance):
    assert isinstance(instance.isPressed, bool)


@given(instance=mindstorms::TouchSensor_strategy)
def test_mindstorms::touchsensor_isPressed_setter(instance):
    original = instance.isPressed
    instance.isPressed = original
    assert instance.isPressed == original

@given(instance=Behavior_strategy)
@settings(max_examples=50)
def test_behavior_instantiation(instance):
    assert isinstance(instance, Behavior)

@given(instance=mindstorms::ExploreForward_strategy)
@settings(max_examples=50)
def test_mindstorms::exploreforward_instantiation(instance):
    assert isinstance(instance, mindstorms::ExploreForward)

@given(instance=mindstorms::ReturnBottleToBase_strategy)
@settings(max_examples=50)
def test_mindstorms::returnbottletobase_instantiation(instance):
    assert isinstance(instance, mindstorms::ReturnBottleToBase)

@given(instance=mindstorms::AvoidObstacle_strategy)
@settings(max_examples=50)
def test_mindstorms::avoidobstacle_instantiation(instance):
    assert isinstance(instance, mindstorms::AvoidObstacle)

@given(instance=mindstorms::ConditionContainer_strategy)
@settings(max_examples=50)
def test_mindstorms::conditioncontainer_instantiation(instance):
    assert isinstance(instance, mindstorms::ConditionContainer)

@given(instance=ConditionContainer_strategy)
@settings(max_examples=50)
def test_conditioncontainer_instantiation(instance):
    assert isinstance(instance, ConditionContainer)

@given(instance=BlockContainer_strategy)
@settings(max_examples=50)
def test_blockcontainer_instantiation(instance):
    assert isinstance(instance, BlockContainer)

@given(instance=Instruction_strategy)
@settings(max_examples=50)
def test_instruction_instantiation(instance):
    assert isinstance(instance, Instruction)

@given(instance=mindstorms::Arbitrator_strategy)
@settings(max_examples=50)
def test_mindstorms::arbitrator_instantiation(instance):
    assert isinstance(instance, mindstorms::Arbitrator)

@given(instance=mindstorms::ReuseInstruction_strategy)
@settings(max_examples=50)
def test_mindstorms::reuseinstruction_instantiation(instance):
    assert isinstance(instance, mindstorms::ReuseInstruction)

@given(instance=mindstorms::Procedure_strategy)
@settings(max_examples=50)
def test_mindstorms::procedure_instantiation(instance):
    assert isinstance(instance, mindstorms::Procedure)

@given(instance=mindstorms::Block_strategy)
@settings(max_examples=50)
def test_mindstorms::block_instantiation(instance):
    assert isinstance(instance, mindstorms::Block)

@given(instance=mindstorms::BlockContainer_strategy)
@settings(max_examples=50)
def test_mindstorms::blockcontainer_instantiation(instance):
    assert isinstance(instance, mindstorms::BlockContainer)

@given(instance=NamedElement_strategy)
@settings(max_examples=50)
def test_namedelement_instantiation(instance):
    assert isinstance(instance, NamedElement)

@given(instance=mindstorms::Behavior_strategy)
@settings(max_examples=50)
def test_mindstorms::behavior_instantiation(instance):
    assert isinstance(instance, mindstorms::Behavior)

@given(instance=mindstorms::Instruction_strategy)
@settings(max_examples=50)
def test_mindstorms::instruction_instantiation(instance):
    assert isinstance(instance, mindstorms::Instruction)

@given(instance=mindstorms::Main_strategy)
@settings(max_examples=50)
def test_mindstorms::main_instantiation(instance):
    assert isinstance(instance, mindstorms::Main)

@given(instance=Action_strategy)
@settings(max_examples=50)
def test_action_instantiation(instance):
    assert isinstance(instance, Action)

@given(instance=mindstorms::GoBackward_strategy)
@settings(max_examples=50)
def test_mindstorms::gobackward_instantiation(instance):
    assert isinstance(instance, mindstorms::GoBackward)

@given(instance=mindstorms::GoBackward_strategy)
def test_mindstorms::gobackward_infinite_type(instance):
    assert isinstance(instance.infinite, bool)


@given(instance=mindstorms::GoBackward_strategy)
def test_mindstorms::gobackward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original

@given(instance=mindstorms::GoBackward_strategy)
def test_mindstorms::gobackward_cm_type(instance):
    assert isinstance(instance.cm, int)


@given(instance=mindstorms::GoBackward_strategy)
def test_mindstorms::gobackward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=mindstorms::GoToEnemy_strategy)
@settings(max_examples=50)
def test_mindstorms::gotoenemy_instantiation(instance):
    assert isinstance(instance, mindstorms::GoToEnemy)

@given(instance=mindstorms::ReturnToBase_strategy)
@settings(max_examples=50)
def test_mindstorms::returntobase_instantiation(instance):
    assert isinstance(instance, mindstorms::ReturnToBase)

@given(instance=mindstorms::Delay_strategy)
@settings(max_examples=50)
def test_mindstorms::delay_instantiation(instance):
    assert isinstance(instance, mindstorms::Delay)

@given(instance=mindstorms::Delay_strategy)
def test_mindstorms::delay_ms_type(instance):
    assert isinstance(instance.ms, int)


@given(instance=mindstorms::Delay_strategy)
def test_mindstorms::delay_ms_setter(instance):
    original = instance.ms
    instance.ms = original
    assert instance.ms == original

@given(instance=mindstorms::GoTo_strategy)
@settings(max_examples=50)
def test_mindstorms::goto_instantiation(instance):
    assert isinstance(instance, mindstorms::GoTo)

@given(instance=mindstorms::GoTo_strategy)
def test_mindstorms::goto_y_type(instance):
    assert isinstance(instance.y, int)


@given(instance=mindstorms::GoTo_strategy)
def test_mindstorms::goto_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original

@given(instance=mindstorms::GoTo_strategy)
def test_mindstorms::goto_x_type(instance):
    assert isinstance(instance.x, int)


@given(instance=mindstorms::GoTo_strategy)
def test_mindstorms::goto_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=mindstorms::Grab_strategy)
@settings(max_examples=50)
def test_mindstorms::grab_instantiation(instance):
    assert isinstance(instance, mindstorms::Grab)

@given(instance=mindstorms::Release_strategy)
@settings(max_examples=50)
def test_mindstorms::release_instantiation(instance):
    assert isinstance(instance, mindstorms::Release)

@given(instance=mindstorms::Rotate_strategy)
@settings(max_examples=50)
def test_mindstorms::rotate_instantiation(instance):
    assert isinstance(instance, mindstorms::Rotate)

@given(instance=mindstorms::Rotate_strategy)
def test_mindstorms::rotate_random_type(instance):
    assert isinstance(instance.random, bool)


@given(instance=mindstorms::Rotate_strategy)
def test_mindstorms::rotate_random_setter(instance):
    original = instance.random
    instance.random = original
    assert instance.random == original

@given(instance=mindstorms::Rotate_strategy)
def test_mindstorms::rotate_degrees_type(instance):
    assert isinstance(instance.degrees, int)


@given(instance=mindstorms::Rotate_strategy)
def test_mindstorms::rotate_degrees_setter(instance):
    original = instance.degrees
    instance.degrees = original
    assert instance.degrees == original

@given(instance=mindstorms::GoForward_strategy)
@settings(max_examples=50)
def test_mindstorms::goforward_instantiation(instance):
    assert isinstance(instance, mindstorms::GoForward)

@given(instance=mindstorms::GoForward_strategy)
def test_mindstorms::goforward_infinite_type(instance):
    assert isinstance(instance.infinite, bool)


@given(instance=mindstorms::GoForward_strategy)
def test_mindstorms::goforward_infinite_setter(instance):
    original = instance.infinite
    instance.infinite = original
    assert instance.infinite == original

@given(instance=mindstorms::GoForward_strategy)
def test_mindstorms::goforward_cm_type(instance):
    assert isinstance(instance.cm, int)


@given(instance=mindstorms::GoForward_strategy)
def test_mindstorms::goforward_cm_setter(instance):
    original = instance.cm
    instance.cm = original
    assert instance.cm == original

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=mindstorms::While_strategy)
@settings(max_examples=50)
def test_mindstorms::while_instantiation(instance):
    assert isinstance(instance, mindstorms::While)

@given(instance=mindstorms::If_strategy)
@settings(max_examples=50)
def test_mindstorms::if_instantiation(instance):
    assert isinstance(instance, mindstorms::If)

@given(instance=mindstorms::Condition_strategy)
@settings(max_examples=50)
def test_mindstorms::condition_instantiation(instance):
    assert isinstance(instance, mindstorms::Condition)

@given(instance=Condition_strategy)
@settings(max_examples=50)
def test_condition_instantiation(instance):
    assert isinstance(instance, Condition)

@given(instance=mindstorms::Sensor_strategy)
@settings(max_examples=50)
def test_mindstorms::sensor_instantiation(instance):
    assert isinstance(instance, mindstorms::Sensor)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=mindstorms::Flow_strategy)
@settings(max_examples=50)
def test_mindstorms::flow_instantiation(instance):
    assert isinstance(instance, mindstorms::Flow)

@given(instance=mindstorms::Action_strategy)
@settings(max_examples=50)
def test_mindstorms::action_instantiation(instance):
    assert isinstance(instance, mindstorms::Action)

@given(instance=mindstorms::NamedElement_strategy)
@settings(max_examples=50)
def test_mindstorms::namedelement_instantiation(instance):
    assert isinstance(instance, mindstorms::NamedElement)

@given(instance=mindstorms::NamedElement_strategy)
def test_mindstorms::namedelement_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=mindstorms::NamedElement_strategy)
def test_mindstorms::namedelement_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
