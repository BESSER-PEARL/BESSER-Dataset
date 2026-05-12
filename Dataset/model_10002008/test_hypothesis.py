import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genmymodelreverse_javax_swing_JFrame,
    genmymodelreverse_javax_swing_Timer,
    genmymodelreverse_javax_swing_JPanel,
    genmymodelreverse_java_awt_event_KeyEvent,
    genmymodelreverse_java_awt_event_KeyAdapter,
    genmymodelreverse_java_awt_event_ActionListener_Interface,
    genmymodelreverse_java_awt_event_ActionEvent,
    genmymodelreverse_java_awt_Graphics,
    genmymodelreverse_java_nio_charset_Charset,
    genmymodelreverse_java_io_IOException,
    genmymodelreverse_java_awt_Image,
    snake_Main,
    snake_TAdapter,
    snake_GameScene,
    snake_Backgrounds,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genmymodelreverse_javax_swing_jframe_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JFrame)


def test_genmymodelreverse_javax_swing_jframe_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JFrame.__init__)


def test_genmymodelreverse_javax_swing_jframe_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JFrame.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_timer_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_Timer)


def test_genmymodelreverse_javax_swing_timer_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_Timer.__init__)


def test_genmymodelreverse_javax_swing_timer_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_Timer.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jpanel_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JPanel)


def test_genmymodelreverse_javax_swing_jpanel_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JPanel.__init__)


def test_genmymodelreverse_javax_swing_jpanel_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JPanel.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_keyevent_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_KeyEvent)


def test_genmymodelreverse_java_awt_event_keyevent_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_KeyEvent.__init__)


def test_genmymodelreverse_java_awt_event_keyevent_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_KeyEvent.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_keyadapter_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_KeyAdapter)


def test_genmymodelreverse_java_awt_event_keyadapter_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_KeyAdapter.__init__)


def test_genmymodelreverse_java_awt_event_keyadapter_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_KeyAdapter.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_actionlistener_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_ActionListener_Interface)


def test_genmymodelreverse_java_awt_event_actionlistener_interface_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_ActionListener_Interface.__init__)


def test_genmymodelreverse_java_awt_event_actionlistener_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_ActionListener_Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_actionevent_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_ActionEvent)


def test_genmymodelreverse_java_awt_event_actionevent_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_ActionEvent.__init__)


def test_genmymodelreverse_java_awt_event_actionevent_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_ActionEvent.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_graphics_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_Graphics)


def test_genmymodelreverse_java_awt_graphics_constructor_exists():
    assert callable(genmymodelreverse_java_awt_Graphics.__init__)


def test_genmymodelreverse_java_awt_graphics_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_nio_charset_charset_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_nio_charset_Charset)


def test_genmymodelreverse_java_nio_charset_charset_constructor_exists():
    assert callable(genmymodelreverse_java_nio_charset_Charset.__init__)


def test_genmymodelreverse_java_nio_charset_charset_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_nio_charset_Charset.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_io_ioexception_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_io_IOException)


def test_genmymodelreverse_java_io_ioexception_constructor_exists():
    assert callable(genmymodelreverse_java_io_IOException.__init__)


def test_genmymodelreverse_java_io_ioexception_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_io_IOException.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_image_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_Image)


def test_genmymodelreverse_java_awt_image_constructor_exists():
    assert callable(genmymodelreverse_java_awt_Image.__init__)


def test_genmymodelreverse_java_awt_image_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_Image.__init__)
    params = list(sig.parameters.keys())



def test_snake_main_is_not_abstract():
    assert not inspect.isabstract(snake_Main)


def test_snake_main_constructor_exists():
    assert callable(snake_Main.__init__)


def test_snake_main_constructor_args():
    sig = inspect.signature(snake_Main.__init__)
    params = list(sig.parameters.keys())
    assert "serialVersionUID" in params, "Missing parameter 'serialVersionUID'"

def test_snake_main_has_serialVersionUID():
    assert hasattr(snake_Main, "serialVersionUID")
    descriptor = None
    for klass in snake_Main.__mro__:
        if "serialVersionUID" in klass.__dict__:
            descriptor = klass.__dict__["serialVersionUID"]
            break
    assert isinstance(descriptor, property)



def test_snake_tadapter_is_not_abstract():
    assert not inspect.isabstract(snake_TAdapter)


def test_snake_tadapter_constructor_exists():
    assert callable(snake_TAdapter.__init__)


def test_snake_tadapter_constructor_args():
    sig = inspect.signature(snake_TAdapter.__init__)
    params = list(sig.parameters.keys())



def test_snake_gamescene_is_not_abstract():
    assert not inspect.isabstract(snake_GameScene)


def test_snake_gamescene_constructor_exists():
    assert callable(snake_GameScene.__init__)


def test_snake_gamescene_constructor_args():
    sig = inspect.signature(snake_GameScene.__init__)
    params = list(sig.parameters.keys())
    assert "DOT_SIZE" in params, "Missing parameter 'DOT_SIZE'"
    assert "upDirection" in params, "Missing parameter 'upDirection'"
    assert "bg" in params, "Missing parameter 'bg'"
    assert "x" in params, "Missing parameter 'x'"
    assert "timer" in params, "Missing parameter 'timer'"
    assert "level" in params, "Missing parameter 'level'"
    assert "leftDirection" in params, "Missing parameter 'leftDirection'"
    assert "apple" in params, "Missing parameter 'apple'"
    assert "head" in params, "Missing parameter 'head'"
    assert "DELAY" in params, "Missing parameter 'DELAY'"
    assert "inGame" in params, "Missing parameter 'inGame'"
    assert "B_WIDTH" in params, "Missing parameter 'B_WIDTH'"
    assert "bodyLength" in params, "Missing parameter 'bodyLength'"
    assert "B_HEIGHT" in params, "Missing parameter 'B_HEIGHT'"
    assert "myScore" in params, "Missing parameter 'myScore'"
    assert "y" in params, "Missing parameter 'y'"
    assert "serialVersionUID" in params, "Missing parameter 'serialVersionUID'"
    assert "apple_x" in params, "Missing parameter 'apple_x'"
    assert "ALL_DOTS" in params, "Missing parameter 'ALL_DOTS'"
    assert "apple_y" in params, "Missing parameter 'apple_y'"
    assert "RAND_POS" in params, "Missing parameter 'RAND_POS'"
    assert "bodySegment" in params, "Missing parameter 'bodySegment'"
    assert "downDirection" in params, "Missing parameter 'downDirection'"
    assert "rightDirection" in params, "Missing parameter 'rightDirection'"

def test_snake_gamescene_has_DOT_SIZE():
    assert hasattr(snake_GameScene, "DOT_SIZE")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "DOT_SIZE" in klass.__dict__:
            descriptor = klass.__dict__["DOT_SIZE"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_upDirection():
    assert hasattr(snake_GameScene, "upDirection")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "upDirection" in klass.__dict__:
            descriptor = klass.__dict__["upDirection"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_bg():
    assert hasattr(snake_GameScene, "bg")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "bg" in klass.__dict__:
            descriptor = klass.__dict__["bg"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_x():
    assert hasattr(snake_GameScene, "x")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_timer():
    assert hasattr(snake_GameScene, "timer")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "timer" in klass.__dict__:
            descriptor = klass.__dict__["timer"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_level():
    assert hasattr(snake_GameScene, "level")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_leftDirection():
    assert hasattr(snake_GameScene, "leftDirection")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "leftDirection" in klass.__dict__:
            descriptor = klass.__dict__["leftDirection"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_apple():
    assert hasattr(snake_GameScene, "apple")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "apple" in klass.__dict__:
            descriptor = klass.__dict__["apple"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_head():
    assert hasattr(snake_GameScene, "head")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "head" in klass.__dict__:
            descriptor = klass.__dict__["head"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_DELAY():
    assert hasattr(snake_GameScene, "DELAY")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "DELAY" in klass.__dict__:
            descriptor = klass.__dict__["DELAY"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_inGame():
    assert hasattr(snake_GameScene, "inGame")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "inGame" in klass.__dict__:
            descriptor = klass.__dict__["inGame"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_B_WIDTH():
    assert hasattr(snake_GameScene, "B_WIDTH")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "B_WIDTH" in klass.__dict__:
            descriptor = klass.__dict__["B_WIDTH"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_bodyLength():
    assert hasattr(snake_GameScene, "bodyLength")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "bodyLength" in klass.__dict__:
            descriptor = klass.__dict__["bodyLength"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_B_HEIGHT():
    assert hasattr(snake_GameScene, "B_HEIGHT")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "B_HEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["B_HEIGHT"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_myScore():
    assert hasattr(snake_GameScene, "myScore")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "myScore" in klass.__dict__:
            descriptor = klass.__dict__["myScore"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_y():
    assert hasattr(snake_GameScene, "y")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_serialVersionUID():
    assert hasattr(snake_GameScene, "serialVersionUID")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "serialVersionUID" in klass.__dict__:
            descriptor = klass.__dict__["serialVersionUID"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_apple_x():
    assert hasattr(snake_GameScene, "apple_x")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "apple_x" in klass.__dict__:
            descriptor = klass.__dict__["apple_x"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_ALL_DOTS():
    assert hasattr(snake_GameScene, "ALL_DOTS")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "ALL_DOTS" in klass.__dict__:
            descriptor = klass.__dict__["ALL_DOTS"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_apple_y():
    assert hasattr(snake_GameScene, "apple_y")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "apple_y" in klass.__dict__:
            descriptor = klass.__dict__["apple_y"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_RAND_POS():
    assert hasattr(snake_GameScene, "RAND_POS")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "RAND_POS" in klass.__dict__:
            descriptor = klass.__dict__["RAND_POS"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_bodySegment():
    assert hasattr(snake_GameScene, "bodySegment")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "bodySegment" in klass.__dict__:
            descriptor = klass.__dict__["bodySegment"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_downDirection():
    assert hasattr(snake_GameScene, "downDirection")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "downDirection" in klass.__dict__:
            descriptor = klass.__dict__["downDirection"]
            break
    assert isinstance(descriptor, property)

def test_snake_gamescene_has_rightDirection():
    assert hasattr(snake_GameScene, "rightDirection")
    descriptor = None
    for klass in snake_GameScene.__mro__:
        if "rightDirection" in klass.__dict__:
            descriptor = klass.__dict__["rightDirection"]
            break
    assert isinstance(descriptor, property)



def test_snake_backgrounds_is_not_abstract():
    assert not inspect.isabstract(snake_Backgrounds)


def test_snake_backgrounds_constructor_exists():
    assert callable(snake_Backgrounds.__init__)


def test_snake_backgrounds_constructor_args():
    sig = inspect.signature(snake_Backgrounds.__init__)
    params = list(sig.parameters.keys())
    assert "backgrounds" in params, "Missing parameter 'backgrounds'"

def test_snake_backgrounds_has_backgrounds():
    assert hasattr(snake_Backgrounds, "backgrounds")
    descriptor = None
    for klass in snake_Backgrounds.__mro__:
        if "backgrounds" in klass.__dict__:
            descriptor = klass.__dict__["backgrounds"]
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
genmymodelreverse_javax_swing_JFrame_strategy = st.builds(
    genmymodelreverse_javax_swing_JFrame,
)
genmymodelreverse_javax_swing_Timer_strategy = st.builds(
    genmymodelreverse_javax_swing_Timer,
)
genmymodelreverse_javax_swing_JPanel_strategy = st.builds(
    genmymodelreverse_javax_swing_JPanel,
)
genmymodelreverse_java_awt_event_KeyEvent_strategy = st.builds(
    genmymodelreverse_java_awt_event_KeyEvent,
)
genmymodelreverse_java_awt_event_KeyAdapter_strategy = st.builds(
    genmymodelreverse_java_awt_event_KeyAdapter,
)
genmymodelreverse_java_awt_event_ActionListener_Interface_strategy = st.builds(
    genmymodelreverse_java_awt_event_ActionListener_Interface,
)
genmymodelreverse_java_awt_event_ActionEvent_strategy = st.builds(
    genmymodelreverse_java_awt_event_ActionEvent,
)
genmymodelreverse_java_awt_Graphics_strategy = st.builds(
    genmymodelreverse_java_awt_Graphics,
)
genmymodelreverse_java_nio_charset_Charset_strategy = st.builds(
    genmymodelreverse_java_nio_charset_Charset,
)
genmymodelreverse_java_io_IOException_strategy = st.builds(
    genmymodelreverse_java_io_IOException,
)
genmymodelreverse_java_awt_Image_strategy = st.builds(
    genmymodelreverse_java_awt_Image,
)
snake_Main_strategy = st.builds(
    snake_Main,
    serialVersionUID=
        st.integers()
)
snake_TAdapter_strategy = st.builds(
    snake_TAdapter,
)
snake_GameScene_strategy = st.builds(
    snake_GameScene,
    DOT_SIZE=
        st.integers(),
    upDirection=
        st.booleans(),
    bg=
        st.none(),
    x=
        safe_text,
    timer=
        st.none(),
    level=
        st.integers(),
    leftDirection=
        st.booleans(),
    apple=
        st.none(),
    head=
        st.none(),
    DELAY=
        st.integers(),
    inGame=
        st.booleans(),
    B_WIDTH=
        st.integers(),
    bodyLength=
        st.integers(),
    B_HEIGHT=
        st.integers(),
    myScore=
        st.integers(),
    y=
        safe_text,
    serialVersionUID=
        st.integers(),
    apple_x=
        st.integers(),
    ALL_DOTS=
        st.integers(),
    apple_y=
        st.integers(),
    RAND_POS=
        st.integers(),
    bodySegment=
        st.none(),
    downDirection=
        st.booleans(),
    rightDirection=
        st.booleans()
)
snake_Backgrounds_strategy = st.builds(
    snake_Backgrounds,
    backgrounds=
        st.none()
)

@given(instance=genmymodelreverse_javax_swing_JFrame_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jframe_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JFrame)

@given(instance=genmymodelreverse_javax_swing_Timer_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_timer_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_Timer)

@given(instance=genmymodelreverse_javax_swing_JPanel_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jpanel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JPanel)

@given(instance=genmymodelreverse_java_awt_event_KeyEvent_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_keyevent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_KeyEvent)

@given(instance=genmymodelreverse_java_awt_event_KeyAdapter_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_keyadapter_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_KeyAdapter)

@given(instance=genmymodelreverse_java_awt_event_ActionListener_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_actionlistener_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_ActionListener_Interface)

@given(instance=genmymodelreverse_java_awt_event_ActionEvent_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_actionevent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_ActionEvent)

@given(instance=genmymodelreverse_java_awt_Graphics_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_graphics_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_Graphics)

@given(instance=genmymodelreverse_java_nio_charset_Charset_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_nio_charset_charset_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_nio_charset_Charset)

@given(instance=genmymodelreverse_java_io_IOException_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_io_ioexception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_io_IOException)

@given(instance=genmymodelreverse_java_awt_Image_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_image_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_Image)

@given(instance=snake_Main_strategy)
@settings(max_examples=50)
def test_snake_main_instantiation(instance):
    assert isinstance(instance, snake_Main)



@given(instance=snake_Main_strategy)
def test_snake_main_serialVersionUID_setter(instance):
    original = instance.serialVersionUID
    instance.serialVersionUID = original
    assert instance.serialVersionUID == original

@given(instance=snake_TAdapter_strategy)
@settings(max_examples=50)
def test_snake_tadapter_instantiation(instance):
    assert isinstance(instance, snake_TAdapter)

@given(instance=snake_GameScene_strategy)
@settings(max_examples=50)
def test_snake_gamescene_instantiation(instance):
    assert isinstance(instance, snake_GameScene)



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_DOT_SIZE_setter(instance):
    original = instance.DOT_SIZE
    instance.DOT_SIZE = original
    assert instance.DOT_SIZE == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_upDirection_setter(instance):
    original = instance.upDirection
    instance.upDirection = original
    assert instance.upDirection == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_bg_setter(instance):
    original = instance.bg
    instance.bg = original
    assert instance.bg == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_timer_setter(instance):
    original = instance.timer
    instance.timer = original
    assert instance.timer == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_leftDirection_setter(instance):
    original = instance.leftDirection
    instance.leftDirection = original
    assert instance.leftDirection == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_apple_setter(instance):
    original = instance.apple
    instance.apple = original
    assert instance.apple == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_head_setter(instance):
    original = instance.head
    instance.head = original
    assert instance.head == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_DELAY_setter(instance):
    original = instance.DELAY
    instance.DELAY = original
    assert instance.DELAY == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_inGame_setter(instance):
    original = instance.inGame
    instance.inGame = original
    assert instance.inGame == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_B_WIDTH_setter(instance):
    original = instance.B_WIDTH
    instance.B_WIDTH = original
    assert instance.B_WIDTH == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_bodyLength_setter(instance):
    original = instance.bodyLength
    instance.bodyLength = original
    assert instance.bodyLength == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_B_HEIGHT_setter(instance):
    original = instance.B_HEIGHT
    instance.B_HEIGHT = original
    assert instance.B_HEIGHT == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_myScore_setter(instance):
    original = instance.myScore
    instance.myScore = original
    assert instance.myScore == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_serialVersionUID_setter(instance):
    original = instance.serialVersionUID
    instance.serialVersionUID = original
    assert instance.serialVersionUID == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_apple_x_setter(instance):
    original = instance.apple_x
    instance.apple_x = original
    assert instance.apple_x == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_ALL_DOTS_setter(instance):
    original = instance.ALL_DOTS
    instance.ALL_DOTS = original
    assert instance.ALL_DOTS == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_apple_y_setter(instance):
    original = instance.apple_y
    instance.apple_y = original
    assert instance.apple_y == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_RAND_POS_setter(instance):
    original = instance.RAND_POS
    instance.RAND_POS = original
    assert instance.RAND_POS == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_bodySegment_setter(instance):
    original = instance.bodySegment
    instance.bodySegment = original
    assert instance.bodySegment == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_downDirection_setter(instance):
    original = instance.downDirection
    instance.downDirection = original
    assert instance.downDirection == original



@given(instance=snake_GameScene_strategy)
def test_snake_gamescene_rightDirection_setter(instance):
    original = instance.rightDirection
    instance.rightDirection = original
    assert instance.rightDirection == original

@given(instance=snake_Backgrounds_strategy)
@settings(max_examples=50)
def test_snake_backgrounds_instantiation(instance):
    assert isinstance(instance, snake_Backgrounds)



@given(instance=snake_Backgrounds_strategy)
def test_snake_backgrounds_backgrounds_setter(instance):
    original = instance.backgrounds
    instance.backgrounds = original
    assert instance.backgrounds == original
