import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Chat,
    Position,
    Class,
    MineField,
    Game,
    Timer,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_chat_is_not_abstract():
    assert not inspect.isabstract(Chat)


def test_chat_constructor_exists():
    assert callable(Chat.__init__)


def test_chat_constructor_args():
    sig = inspect.signature(Chat.__init__)
    params = list(sig.parameters.keys())
    assert "commands" in params, "Missing parameter 'commands'"
    assert "username" in params, "Missing parameter 'username'"

def test_chat_has_commands():
    assert hasattr(Chat, "commands")
    descriptor = None
    for klass in Chat.__mro__:
        if "commands" in klass.__dict__:
            descriptor = klass.__dict__["commands"]
            break
    assert isinstance(descriptor, property)

def test_chat_has_username():
    assert hasattr(Chat, "username")
    descriptor = None
    for klass in Chat.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_position_is_not_abstract():
    assert not inspect.isabstract(Position)


def test_position_constructor_exists():
    assert callable(Position.__init__)


def test_position_constructor_args():
    sig = inspect.signature(Position.__init__)
    params = list(sig.parameters.keys())
    assert "y" in params, "Missing parameter 'y'"
    assert "is_hidden" in params, "Missing parameter 'is_hidden'"
    assert "has_flag" in params, "Missing parameter 'has_flag'"
    assert "x" in params, "Missing parameter 'x'"

def test_position_has_y():
    assert hasattr(Position, "y")
    descriptor = None
    for klass in Position.__mro__:
        if "y" in klass.__dict__:
            descriptor = klass.__dict__["y"]
            break
    assert isinstance(descriptor, property)

def test_position_has_is_hidden():
    assert hasattr(Position, "is_hidden")
    descriptor = None
    for klass in Position.__mro__:
        if "is_hidden" in klass.__dict__:
            descriptor = klass.__dict__["is_hidden"]
            break
    assert isinstance(descriptor, property)

def test_position_has_has_flag():
    assert hasattr(Position, "has_flag")
    descriptor = None
    for klass in Position.__mro__:
        if "has_flag" in klass.__dict__:
            descriptor = klass.__dict__["has_flag"]
            break
    assert isinstance(descriptor, property)

def test_position_has_x():
    assert hasattr(Position, "x")
    descriptor = None
    for klass in Position.__mro__:
        if "x" in klass.__dict__:
            descriptor = klass.__dict__["x"]
            break
    assert isinstance(descriptor, property)



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_minefield_is_not_abstract():
    assert not inspect.isabstract(MineField)


def test_minefield_constructor_exists():
    assert callable(MineField.__init__)


def test_minefield_constructor_args():
    sig = inspect.signature(MineField.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "grid" in params, "Missing parameter 'grid'"

def test_minefield_has_height():
    assert hasattr(MineField, "height")
    descriptor = None
    for klass in MineField.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_minefield_has_width():
    assert hasattr(MineField, "width")
    descriptor = None
    for klass in MineField.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_minefield_has_grid():
    assert hasattr(MineField, "grid")
    descriptor = None
    for klass in MineField.__mro__:
        if "grid" in klass.__dict__:
            descriptor = klass.__dict__["grid"]
            break
    assert isinstance(descriptor, property)



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"
    assert "mine_field" in params, "Missing parameter 'mine_field'"
    assert "time_keeper" in params, "Missing parameter 'time_keeper'"

def test_game_has_score():
    assert hasattr(Game, "score")
    descriptor = None
    for klass in Game.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_game_has_mine_field():
    assert hasattr(Game, "mine_field")
    descriptor = None
    for klass in Game.__mro__:
        if "mine_field" in klass.__dict__:
            descriptor = klass.__dict__["mine_field"]
            break
    assert isinstance(descriptor, property)

def test_game_has_time_keeper():
    assert hasattr(Game, "time_keeper")
    descriptor = None
    for klass in Game.__mro__:
        if "time_keeper" in klass.__dict__:
            descriptor = klass.__dict__["time_keeper"]
            break
    assert isinstance(descriptor, property)



def test_timer_is_not_abstract():
    assert not inspect.isabstract(Timer)


def test_timer_constructor_exists():
    assert callable(Timer.__init__)


def test_timer_constructor_args():
    sig = inspect.signature(Timer.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"
    assert "ticks" in params, "Missing parameter 'ticks'"

def test_timer_has_start():
    assert hasattr(Timer, "start")
    descriptor = None
    for klass in Timer.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)

def test_timer_has_ticks():
    assert hasattr(Timer, "ticks")
    descriptor = None
    for klass in Timer.__mro__:
        if "ticks" in klass.__dict__:
            descriptor = klass.__dict__["ticks"]
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
Chat_strategy = st.builds(
    Chat,
    commands=
        safe_text,
    username=
        safe_text
)
Position_strategy = st.builds(
    Position,
    y=
        st.integers(),
    is_hidden=
        st.booleans(),
    has_flag=
        st.booleans(),
    x=
        st.integers()
)
Class_strategy = st.builds(
    Class,
)
MineField_strategy = st.builds(
    MineField,
    height=
        st.integers(),
    width=
        st.integers(),
    grid=
        safe_text
)
Game_strategy = st.builds(
    Game,
    score=
        st.integers(),
    mine_field=
        st.none(),
    time_keeper=
        st.none()
)
Timer_strategy = st.builds(
    Timer,
    start=
        st.integers(),
    ticks=
        st.integers()
)

@given(instance=Chat_strategy)
@settings(max_examples=50)
def test_chat_instantiation(instance):
    assert isinstance(instance, Chat)



@given(instance=Chat_strategy)
def test_chat_commands_setter(instance):
    original = instance.commands
    instance.commands = original
    assert instance.commands == original



@given(instance=Chat_strategy)
def test_chat_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Position_strategy)
@settings(max_examples=50)
def test_position_instantiation(instance):
    assert isinstance(instance, Position)



@given(instance=Position_strategy)
def test_position_y_setter(instance):
    original = instance.y
    instance.y = original
    assert instance.y == original



@given(instance=Position_strategy)
def test_position_is_hidden_setter(instance):
    original = instance.is_hidden
    instance.is_hidden = original
    assert instance.is_hidden == original



@given(instance=Position_strategy)
def test_position_has_flag_setter(instance):
    original = instance.has_flag
    instance.has_flag = original
    assert instance.has_flag == original



@given(instance=Position_strategy)
def test_position_x_setter(instance):
    original = instance.x
    instance.x = original
    assert instance.x == original

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=MineField_strategy)
@settings(max_examples=50)
def test_minefield_instantiation(instance):
    assert isinstance(instance, MineField)



@given(instance=MineField_strategy)
def test_minefield_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=MineField_strategy)
def test_minefield_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=MineField_strategy)
def test_minefield_grid_setter(instance):
    original = instance.grid
    instance.grid = original
    assert instance.grid == original

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=Game_strategy)
def test_game_mine_field_setter(instance):
    original = instance.mine_field
    instance.mine_field = original
    assert instance.mine_field == original



@given(instance=Game_strategy)
def test_game_time_keeper_setter(instance):
    original = instance.time_keeper
    instance.time_keeper = original
    assert instance.time_keeper == original

@given(instance=Timer_strategy)
@settings(max_examples=50)
def test_timer_instantiation(instance):
    assert isinstance(instance, Timer)



@given(instance=Timer_strategy)
def test_timer_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original



@given(instance=Timer_strategy)
def test_timer_ticks_setter(instance):
    original = instance.ticks
    instance.ticks = original
    assert instance.ticks == original
