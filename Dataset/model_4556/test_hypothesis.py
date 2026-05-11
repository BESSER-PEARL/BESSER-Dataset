import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    CMD,
    myDsl::TURTLE,
    myDsl::PENSTATE,
    myDsl::MOVE,
    myDsl::LEFT,
    myDsl::RIGHT,
    myDsl::PENCOLOUR,
    myDsl::PAPER,
    myDsl::CMD,
    myDsl::PROGRAM,
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



def test_mydsl::turtle_is_not_abstract():
    assert not inspect.isabstract(myDsl::TURTLE)


def test_mydsl::turtle_constructor_exists():
    assert callable(myDsl::TURTLE.__init__)


def test_mydsl::turtle_constructor_args():
    sig = inspect.signature(myDsl::TURTLE.__init__)
    params = list(sig.parameters.keys())
    assert "startPosX" in params, "Missing parameter 'startPosX'"
    assert "startPosY" in params, "Missing parameter 'startPosY'"

def test_mydsl::turtle_has_startPosX():
    assert hasattr(myDsl::TURTLE, "startPosX")
    descriptor = None
    for klass in myDsl::TURTLE.__mro__:
        if "startPosX" in klass.__dict__:
            descriptor = klass.__dict__["startPosX"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::turtle_has_startPosY():
    assert hasattr(myDsl::TURTLE, "startPosY")
    descriptor = None
    for klass in myDsl::TURTLE.__mro__:
        if "startPosY" in klass.__dict__:
            descriptor = klass.__dict__["startPosY"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::penstate_is_not_abstract():
    assert not inspect.isabstract(myDsl::PENSTATE)


def test_mydsl::penstate_constructor_exists():
    assert callable(myDsl::PENSTATE.__init__)


def test_mydsl::penstate_constructor_args():
    sig = inspect.signature(myDsl::PENSTATE.__init__)
    params = list(sig.parameters.keys())
    assert "penState" in params, "Missing parameter 'penState'"

def test_mydsl::penstate_has_penState():
    assert hasattr(myDsl::PENSTATE, "penState")
    descriptor = None
    for klass in myDsl::PENSTATE.__mro__:
        if "penState" in klass.__dict__:
            descriptor = klass.__dict__["penState"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::move_is_not_abstract():
    assert not inspect.isabstract(myDsl::MOVE)


def test_mydsl::move_constructor_exists():
    assert callable(myDsl::MOVE.__init__)


def test_mydsl::move_constructor_args():
    sig = inspect.signature(myDsl::MOVE.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_mydsl::move_has_amount():
    assert hasattr(myDsl::MOVE, "amount")
    descriptor = None
    for klass in myDsl::MOVE.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::left_is_not_abstract():
    assert not inspect.isabstract(myDsl::LEFT)


def test_mydsl::left_constructor_exists():
    assert callable(myDsl::LEFT.__init__)


def test_mydsl::left_constructor_args():
    sig = inspect.signature(myDsl::LEFT.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_mydsl::left_has_amount():
    assert hasattr(myDsl::LEFT, "amount")
    descriptor = None
    for klass in myDsl::LEFT.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::right_is_not_abstract():
    assert not inspect.isabstract(myDsl::RIGHT)


def test_mydsl::right_constructor_exists():
    assert callable(myDsl::RIGHT.__init__)


def test_mydsl::right_constructor_args():
    sig = inspect.signature(myDsl::RIGHT.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_mydsl::right_has_amount():
    assert hasattr(myDsl::RIGHT, "amount")
    descriptor = None
    for klass in myDsl::RIGHT.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::pencolour_is_not_abstract():
    assert not inspect.isabstract(myDsl::PENCOLOUR)


def test_mydsl::pencolour_constructor_exists():
    assert callable(myDsl::PENCOLOUR.__init__)


def test_mydsl::pencolour_constructor_args():
    sig = inspect.signature(myDsl::PENCOLOUR.__init__)
    params = list(sig.parameters.keys())
    assert "colour" in params, "Missing parameter 'colour'"

def test_mydsl::pencolour_has_colour():
    assert hasattr(myDsl::PENCOLOUR, "colour")
    descriptor = None
    for klass in myDsl::PENCOLOUR.__mro__:
        if "colour" in klass.__dict__:
            descriptor = klass.__dict__["colour"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::paper_is_not_abstract():
    assert not inspect.isabstract(myDsl::PAPER)


def test_mydsl::paper_constructor_exists():
    assert callable(myDsl::PAPER.__init__)


def test_mydsl::paper_constructor_args():
    sig = inspect.signature(myDsl::PAPER.__init__)
    params = list(sig.parameters.keys())
    assert "sizeY" in params, "Missing parameter 'sizeY'"
    assert "paperColour" in params, "Missing parameter 'paperColour'"
    assert "sizeX" in params, "Missing parameter 'sizeX'"

def test_mydsl::paper_has_sizeY():
    assert hasattr(myDsl::PAPER, "sizeY")
    descriptor = None
    for klass in myDsl::PAPER.__mro__:
        if "sizeY" in klass.__dict__:
            descriptor = klass.__dict__["sizeY"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::paper_has_paperColour():
    assert hasattr(myDsl::PAPER, "paperColour")
    descriptor = None
    for klass in myDsl::PAPER.__mro__:
        if "paperColour" in klass.__dict__:
            descriptor = klass.__dict__["paperColour"]
            break
    assert isinstance(descriptor, property)

def test_mydsl::paper_has_sizeX():
    assert hasattr(myDsl::PAPER, "sizeX")
    descriptor = None
    for klass in myDsl::PAPER.__mro__:
        if "sizeX" in klass.__dict__:
            descriptor = klass.__dict__["sizeX"]
            break
    assert isinstance(descriptor, property)



def test_mydsl::cmd_is_not_abstract():
    assert not inspect.isabstract(myDsl::CMD)


def test_mydsl::cmd_constructor_exists():
    assert callable(myDsl::CMD.__init__)


def test_mydsl::cmd_constructor_args():
    sig = inspect.signature(myDsl::CMD.__init__)
    params = list(sig.parameters.keys())



def test_mydsl::program_is_not_abstract():
    assert not inspect.isabstract(myDsl::PROGRAM)


def test_mydsl::program_constructor_exists():
    assert callable(myDsl::PROGRAM.__init__)


def test_mydsl::program_constructor_args():
    sig = inspect.signature(myDsl::PROGRAM.__init__)
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
myDsl::TURTLE_strategy = st.builds(
    myDsl::TURTLE,
    startPosX=
        st.integers(),
    startPosY=
        st.integers()
)
myDsl::PENSTATE_strategy = st.builds(
    myDsl::PENSTATE,
    penState=
        safe_text
)
myDsl::MOVE_strategy = st.builds(
    myDsl::MOVE,
    amount=
        st.integers()
)
myDsl::LEFT_strategy = st.builds(
    myDsl::LEFT,
    amount=
        st.integers()
)
myDsl::RIGHT_strategy = st.builds(
    myDsl::RIGHT,
    amount=
        st.integers()
)
myDsl::PENCOLOUR_strategy = st.builds(
    myDsl::PENCOLOUR,
    colour=
        safe_text
)
myDsl::PAPER_strategy = st.builds(
    myDsl::PAPER,
    sizeY=
        st.integers(),
    paperColour=
        safe_text,
    sizeX=
        st.integers()
)
myDsl::CMD_strategy = st.builds(
    myDsl::CMD,
)
myDsl::PROGRAM_strategy = st.builds(
    myDsl::PROGRAM,
)

@given(instance=CMD_strategy)
@settings(max_examples=50)
def test_cmd_instantiation(instance):
    assert isinstance(instance, CMD)

@given(instance=myDsl::TURTLE_strategy)
@settings(max_examples=50)
def test_mydsl::turtle_instantiation(instance):
    assert isinstance(instance, myDsl::TURTLE)

@given(instance=myDsl::TURTLE_strategy)
def test_mydsl::turtle_startPosX_type(instance):
    assert isinstance(instance.startPosX, int)


@given(instance=myDsl::TURTLE_strategy)
def test_mydsl::turtle_startPosX_setter(instance):
    original = instance.startPosX
    instance.startPosX = original
    assert instance.startPosX == original

@given(instance=myDsl::TURTLE_strategy)
def test_mydsl::turtle_startPosY_type(instance):
    assert isinstance(instance.startPosY, int)


@given(instance=myDsl::TURTLE_strategy)
def test_mydsl::turtle_startPosY_setter(instance):
    original = instance.startPosY
    instance.startPosY = original
    assert instance.startPosY == original

@given(instance=myDsl::PENSTATE_strategy)
@settings(max_examples=50)
def test_mydsl::penstate_instantiation(instance):
    assert isinstance(instance, myDsl::PENSTATE)

@given(instance=myDsl::PENSTATE_strategy)
def test_mydsl::penstate_penState_type(instance):
    assert isinstance(instance.penState, str)


@given(instance=myDsl::PENSTATE_strategy)
def test_mydsl::penstate_penState_setter(instance):
    original = instance.penState
    instance.penState = original
    assert instance.penState == original

@given(instance=myDsl::MOVE_strategy)
@settings(max_examples=50)
def test_mydsl::move_instantiation(instance):
    assert isinstance(instance, myDsl::MOVE)

@given(instance=myDsl::MOVE_strategy)
def test_mydsl::move_amount_type(instance):
    assert isinstance(instance.amount, int)


@given(instance=myDsl::MOVE_strategy)
def test_mydsl::move_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=myDsl::LEFT_strategy)
@settings(max_examples=50)
def test_mydsl::left_instantiation(instance):
    assert isinstance(instance, myDsl::LEFT)

@given(instance=myDsl::LEFT_strategy)
def test_mydsl::left_amount_type(instance):
    assert isinstance(instance.amount, int)


@given(instance=myDsl::LEFT_strategy)
def test_mydsl::left_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=myDsl::RIGHT_strategy)
@settings(max_examples=50)
def test_mydsl::right_instantiation(instance):
    assert isinstance(instance, myDsl::RIGHT)

@given(instance=myDsl::RIGHT_strategy)
def test_mydsl::right_amount_type(instance):
    assert isinstance(instance.amount, int)


@given(instance=myDsl::RIGHT_strategy)
def test_mydsl::right_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=myDsl::PENCOLOUR_strategy)
@settings(max_examples=50)
def test_mydsl::pencolour_instantiation(instance):
    assert isinstance(instance, myDsl::PENCOLOUR)

@given(instance=myDsl::PENCOLOUR_strategy)
def test_mydsl::pencolour_colour_type(instance):
    assert isinstance(instance.colour, str)


@given(instance=myDsl::PENCOLOUR_strategy)
def test_mydsl::pencolour_colour_setter(instance):
    original = instance.colour
    instance.colour = original
    assert instance.colour == original

@given(instance=myDsl::PAPER_strategy)
@settings(max_examples=50)
def test_mydsl::paper_instantiation(instance):
    assert isinstance(instance, myDsl::PAPER)

@given(instance=myDsl::PAPER_strategy)
def test_mydsl::paper_sizeY_type(instance):
    assert isinstance(instance.sizeY, int)


@given(instance=myDsl::PAPER_strategy)
def test_mydsl::paper_sizeY_setter(instance):
    original = instance.sizeY
    instance.sizeY = original
    assert instance.sizeY == original

@given(instance=myDsl::PAPER_strategy)
def test_mydsl::paper_paperColour_type(instance):
    assert isinstance(instance.paperColour, str)


@given(instance=myDsl::PAPER_strategy)
def test_mydsl::paper_paperColour_setter(instance):
    original = instance.paperColour
    instance.paperColour = original
    assert instance.paperColour == original

@given(instance=myDsl::PAPER_strategy)
def test_mydsl::paper_sizeX_type(instance):
    assert isinstance(instance.sizeX, int)


@given(instance=myDsl::PAPER_strategy)
def test_mydsl::paper_sizeX_setter(instance):
    original = instance.sizeX
    instance.sizeX = original
    assert instance.sizeX == original

@given(instance=myDsl::CMD_strategy)
@settings(max_examples=50)
def test_mydsl::cmd_instantiation(instance):
    assert isinstance(instance, myDsl::CMD)

@given(instance=myDsl::PROGRAM_strategy)
@settings(max_examples=50)
def test_mydsl::program_instantiation(instance):
    assert isinstance(instance, myDsl::PROGRAM)
