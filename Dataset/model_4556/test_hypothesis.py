import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    CMD,
    myDsl_TURTLE,
    myDsl_PENSTATE,
    myDsl_RIGHT,
    myDsl_MOVE,
    myDsl_PENCOLOUR,
    myDsl_LEFT,
    myDsl_PAPER,
    myDsl_CMD,
    myDsl_PROGRAM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_cmd_is_not_abstract():
    assert not inspect.isabstract(CMD)


def test_cmd_constructor_exists():
    assert callable(CMD.__init__)


def test_cmd_constructor_args():
    sig = inspect.signature(CMD.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_turtle_is_not_abstract():
    assert not inspect.isabstract(myDsl_TURTLE)


def test_mydsl_turtle_constructor_exists():
    assert callable(myDsl_TURTLE.__init__)


def test_mydsl_turtle_constructor_args():
    sig = inspect.signature(myDsl_TURTLE.__init__)
    params = list(sig.parameters.keys())
    assert "startPosY" in params, "Missing parameter 'startPosY'"
    assert "startPosX" in params, "Missing parameter 'startPosX'"

def test_mydsl_turtle_has_startPosY():
    assert hasattr(myDsl_TURTLE, "startPosY")
    descriptor = None
    for klass in myDsl_TURTLE.__mro__:
        if "startPosY" in klass.__dict__:
            descriptor = klass.__dict__["startPosY"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_turtle_has_startPosX():
    assert hasattr(myDsl_TURTLE, "startPosX")
    descriptor = None
    for klass in myDsl_TURTLE.__mro__:
        if "startPosX" in klass.__dict__:
            descriptor = klass.__dict__["startPosX"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_penstate_is_not_abstract():
    assert not inspect.isabstract(myDsl_PENSTATE)


def test_mydsl_penstate_constructor_exists():
    assert callable(myDsl_PENSTATE.__init__)


def test_mydsl_penstate_constructor_args():
    sig = inspect.signature(myDsl_PENSTATE.__init__)
    params = list(sig.parameters.keys())
    assert "penState" in params, "Missing parameter 'penState'"

def test_mydsl_penstate_has_penState():
    assert hasattr(myDsl_PENSTATE, "penState")
    descriptor = None
    for klass in myDsl_PENSTATE.__mro__:
        if "penState" in klass.__dict__:
            descriptor = klass.__dict__["penState"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_right_is_not_abstract():
    assert not inspect.isabstract(myDsl_RIGHT)


def test_mydsl_right_constructor_exists():
    assert callable(myDsl_RIGHT.__init__)


def test_mydsl_right_constructor_args():
    sig = inspect.signature(myDsl_RIGHT.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_mydsl_right_has_amount():
    assert hasattr(myDsl_RIGHT, "amount")
    descriptor = None
    for klass in myDsl_RIGHT.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_move_is_not_abstract():
    assert not inspect.isabstract(myDsl_MOVE)


def test_mydsl_move_constructor_exists():
    assert callable(myDsl_MOVE.__init__)


def test_mydsl_move_constructor_args():
    sig = inspect.signature(myDsl_MOVE.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_mydsl_move_has_amount():
    assert hasattr(myDsl_MOVE, "amount")
    descriptor = None
    for klass in myDsl_MOVE.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_pencolour_is_not_abstract():
    assert not inspect.isabstract(myDsl_PENCOLOUR)


def test_mydsl_pencolour_constructor_exists():
    assert callable(myDsl_PENCOLOUR.__init__)


def test_mydsl_pencolour_constructor_args():
    sig = inspect.signature(myDsl_PENCOLOUR.__init__)
    params = list(sig.parameters.keys())
    assert "colour" in params, "Missing parameter 'colour'"

def test_mydsl_pencolour_has_colour():
    assert hasattr(myDsl_PENCOLOUR, "colour")
    descriptor = None
    for klass in myDsl_PENCOLOUR.__mro__:
        if "colour" in klass.__dict__:
            descriptor = klass.__dict__["colour"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_left_is_not_abstract():
    assert not inspect.isabstract(myDsl_LEFT)


def test_mydsl_left_constructor_exists():
    assert callable(myDsl_LEFT.__init__)


def test_mydsl_left_constructor_args():
    sig = inspect.signature(myDsl_LEFT.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_mydsl_left_has_amount():
    assert hasattr(myDsl_LEFT, "amount")
    descriptor = None
    for klass in myDsl_LEFT.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_paper_is_not_abstract():
    assert not inspect.isabstract(myDsl_PAPER)


def test_mydsl_paper_constructor_exists():
    assert callable(myDsl_PAPER.__init__)


def test_mydsl_paper_constructor_args():
    sig = inspect.signature(myDsl_PAPER.__init__)
    params = list(sig.parameters.keys())
    assert "paperColour" in params, "Missing parameter 'paperColour'"
    assert "sizeY" in params, "Missing parameter 'sizeY'"
    assert "sizeX" in params, "Missing parameter 'sizeX'"

def test_mydsl_paper_has_paperColour():
    assert hasattr(myDsl_PAPER, "paperColour")
    descriptor = None
    for klass in myDsl_PAPER.__mro__:
        if "paperColour" in klass.__dict__:
            descriptor = klass.__dict__["paperColour"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_paper_has_sizeY():
    assert hasattr(myDsl_PAPER, "sizeY")
    descriptor = None
    for klass in myDsl_PAPER.__mro__:
        if "sizeY" in klass.__dict__:
            descriptor = klass.__dict__["sizeY"]
            break
    assert isinstance(descriptor, property)

def test_mydsl_paper_has_sizeX():
    assert hasattr(myDsl_PAPER, "sizeX")
    descriptor = None
    for klass in myDsl_PAPER.__mro__:
        if "sizeX" in klass.__dict__:
            descriptor = klass.__dict__["sizeX"]
            break
    assert isinstance(descriptor, property)



def test_mydsl_cmd_is_not_abstract():
    assert not inspect.isabstract(myDsl_CMD)


def test_mydsl_cmd_constructor_exists():
    assert callable(myDsl_CMD.__init__)


def test_mydsl_cmd_constructor_args():
    sig = inspect.signature(myDsl_CMD.__init__)
    params = list(sig.parameters.keys())



def test_mydsl_program_is_not_abstract():
    assert not inspect.isabstract(myDsl_PROGRAM)


def test_mydsl_program_constructor_exists():
    assert callable(myDsl_PROGRAM.__init__)


def test_mydsl_program_constructor_args():
    sig = inspect.signature(myDsl_PROGRAM.__init__)
    params = list(sig.parameters.keys())


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
CMD_strategy = st.builds(
    CMD,
)
myDsl_TURTLE_strategy = st.builds(
    myDsl_TURTLE,
    startPosY=
        st.integers(),
    startPosX=
        st.integers()
)
myDsl_PENSTATE_strategy = st.builds(
    myDsl_PENSTATE,
    penState=
        safe_text
)
myDsl_RIGHT_strategy = st.builds(
    myDsl_RIGHT,
    amount=
        st.integers()
)
myDsl_MOVE_strategy = st.builds(
    myDsl_MOVE,
    amount=
        st.integers()
)
myDsl_PENCOLOUR_strategy = st.builds(
    myDsl_PENCOLOUR,
    colour=
        safe_text
)
myDsl_LEFT_strategy = st.builds(
    myDsl_LEFT,
    amount=
        st.integers()
)
myDsl_PAPER_strategy = st.builds(
    myDsl_PAPER,
    paperColour=
        safe_text,
    sizeY=
        st.integers(),
    sizeX=
        st.integers()
)
myDsl_CMD_strategy = st.builds(
    myDsl_CMD,
)
myDsl_PROGRAM_strategy = st.builds(
    myDsl_PROGRAM,
)

@given(instance=CMD_strategy)
@settings(max_examples=50)
def test_cmd_instantiation(instance):
    assert isinstance(instance, CMD)

@given(instance=myDsl_TURTLE_strategy)
@settings(max_examples=50)
def test_mydsl_turtle_instantiation(instance):
    assert isinstance(instance, myDsl_TURTLE)



@given(instance=myDsl_TURTLE_strategy)
def test_mydsl_turtle_startPosY_setter(instance):
    original = instance.startPosY
    instance.startPosY = original
    assert instance.startPosY == original



@given(instance=myDsl_TURTLE_strategy)
def test_mydsl_turtle_startPosX_setter(instance):
    original = instance.startPosX
    instance.startPosX = original
    assert instance.startPosX == original

@given(instance=myDsl_PENSTATE_strategy)
@settings(max_examples=50)
def test_mydsl_penstate_instantiation(instance):
    assert isinstance(instance, myDsl_PENSTATE)



@given(instance=myDsl_PENSTATE_strategy)
def test_mydsl_penstate_penState_setter(instance):
    original = instance.penState
    instance.penState = original
    assert instance.penState == original

@given(instance=myDsl_RIGHT_strategy)
@settings(max_examples=50)
def test_mydsl_right_instantiation(instance):
    assert isinstance(instance, myDsl_RIGHT)



@given(instance=myDsl_RIGHT_strategy)
def test_mydsl_right_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=myDsl_MOVE_strategy)
@settings(max_examples=50)
def test_mydsl_move_instantiation(instance):
    assert isinstance(instance, myDsl_MOVE)



@given(instance=myDsl_MOVE_strategy)
def test_mydsl_move_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=myDsl_PENCOLOUR_strategy)
@settings(max_examples=50)
def test_mydsl_pencolour_instantiation(instance):
    assert isinstance(instance, myDsl_PENCOLOUR)



@given(instance=myDsl_PENCOLOUR_strategy)
def test_mydsl_pencolour_colour_setter(instance):
    original = instance.colour
    instance.colour = original
    assert instance.colour == original

@given(instance=myDsl_LEFT_strategy)
@settings(max_examples=50)
def test_mydsl_left_instantiation(instance):
    assert isinstance(instance, myDsl_LEFT)



@given(instance=myDsl_LEFT_strategy)
def test_mydsl_left_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=myDsl_PAPER_strategy)
@settings(max_examples=50)
def test_mydsl_paper_instantiation(instance):
    assert isinstance(instance, myDsl_PAPER)



@given(instance=myDsl_PAPER_strategy)
def test_mydsl_paper_paperColour_setter(instance):
    original = instance.paperColour
    instance.paperColour = original
    assert instance.paperColour == original



@given(instance=myDsl_PAPER_strategy)
def test_mydsl_paper_sizeY_setter(instance):
    original = instance.sizeY
    instance.sizeY = original
    assert instance.sizeY == original



@given(instance=myDsl_PAPER_strategy)
def test_mydsl_paper_sizeX_setter(instance):
    original = instance.sizeX
    instance.sizeX = original
    assert instance.sizeX == original

@given(instance=myDsl_CMD_strategy)
@settings(max_examples=50)
def test_mydsl_cmd_instantiation(instance):
    assert isinstance(instance, myDsl_CMD)

@given(instance=myDsl_PROGRAM_strategy)
@settings(max_examples=50)
def test_mydsl_program_instantiation(instance):
    assert isinstance(instance, myDsl_PROGRAM)
