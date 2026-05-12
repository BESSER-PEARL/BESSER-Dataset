import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Persistence,
    Class,
    SaveGameWidget,
    LoadGameWidget,
    felhaszn_l__Actor,
    Model,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_persistence_is_not_abstract():
    assert not inspect.isabstract(Persistence)


def test_persistence_constructor_exists():
    assert callable(Persistence.__init__)


def test_persistence_constructor_args():
    sig = inspect.signature(Persistence.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_savegamewidget_is_not_abstract():
    assert not inspect.isabstract(SaveGameWidget)


def test_savegamewidget_constructor_exists():
    assert callable(SaveGameWidget.__init__)


def test_savegamewidget_constructor_args():
    sig = inspect.signature(SaveGameWidget.__init__)
    params = list(sig.parameters.keys())
    assert "_listWidget" in params, "Missing parameter '_listWidget'"
    assert "okButton" in params, "Missing parameter 'okButton'"
    assert "cancelButton" in params, "Missing parameter 'cancelButton'"

def test_savegamewidget_has__listWidget():
    assert hasattr(SaveGameWidget, "_listWidget")
    descriptor = None
    for klass in SaveGameWidget.__mro__:
        if "_listWidget" in klass.__dict__:
            descriptor = klass.__dict__["_listWidget"]
            break
    assert isinstance(descriptor, property)

def test_savegamewidget_has_okButton():
    assert hasattr(SaveGameWidget, "okButton")
    descriptor = None
    for klass in SaveGameWidget.__mro__:
        if "okButton" in klass.__dict__:
            descriptor = klass.__dict__["okButton"]
            break
    assert isinstance(descriptor, property)

def test_savegamewidget_has_cancelButton():
    assert hasattr(SaveGameWidget, "cancelButton")
    descriptor = None
    for klass in SaveGameWidget.__mro__:
        if "cancelButton" in klass.__dict__:
            descriptor = klass.__dict__["cancelButton"]
            break
    assert isinstance(descriptor, property)



def test_loadgamewidget_is_not_abstract():
    assert not inspect.isabstract(LoadGameWidget)


def test_loadgamewidget_constructor_exists():
    assert callable(LoadGameWidget.__init__)


def test_loadgamewidget_constructor_args():
    sig = inspect.signature(LoadGameWidget.__init__)
    params = list(sig.parameters.keys())



def test_felhaszn_l__actor_is_not_abstract():
    assert not inspect.isabstract(felhaszn_l__Actor)


def test_felhaszn_l__actor_constructor_exists():
    assert callable(felhaszn_l__Actor.__init__)


def test_felhaszn_l__actor_constructor_args():
    sig = inspect.signature(felhaszn_l__Actor.__init__)
    params = list(sig.parameters.keys())



def test_model_is_not_abstract():
    assert not inspect.isabstract(Model)


def test_model_constructor_exists():
    assert callable(Model.__init__)


def test_model_constructor_args():
    sig = inspect.signature(Model.__init__)
    params = list(sig.parameters.keys())
    assert "gameTable" in params, "Missing parameter 'gameTable'"
    assert "pl2points" in params, "Missing parameter 'pl2points'"
    assert "playerNr" in params, "Missing parameter 'playerNr'"
    assert "goodselected" in params, "Missing parameter 'goodselected'"
    assert "pl1" in params, "Missing parameter 'pl1'"
    assert "gameSize" in params, "Missing parameter 'gameSize'"
    assert "pl1points" in params, "Missing parameter 'pl1points'"
    assert "gameOver" in params, "Missing parameter 'gameOver'"
    assert "pl2" in params, "Missing parameter 'pl2'"
    assert "selected" in params, "Missing parameter 'selected'"
    assert "steps" in params, "Missing parameter 'steps'"

def test_model_has_gameTable():
    assert hasattr(Model, "gameTable")
    descriptor = None
    for klass in Model.__mro__:
        if "gameTable" in klass.__dict__:
            descriptor = klass.__dict__["gameTable"]
            break
    assert isinstance(descriptor, property)

def test_model_has_pl2points():
    assert hasattr(Model, "pl2points")
    descriptor = None
    for klass in Model.__mro__:
        if "pl2points" in klass.__dict__:
            descriptor = klass.__dict__["pl2points"]
            break
    assert isinstance(descriptor, property)

def test_model_has_playerNr():
    assert hasattr(Model, "playerNr")
    descriptor = None
    for klass in Model.__mro__:
        if "playerNr" in klass.__dict__:
            descriptor = klass.__dict__["playerNr"]
            break
    assert isinstance(descriptor, property)

def test_model_has_goodselected():
    assert hasattr(Model, "goodselected")
    descriptor = None
    for klass in Model.__mro__:
        if "goodselected" in klass.__dict__:
            descriptor = klass.__dict__["goodselected"]
            break
    assert isinstance(descriptor, property)

def test_model_has_pl1():
    assert hasattr(Model, "pl1")
    descriptor = None
    for klass in Model.__mro__:
        if "pl1" in klass.__dict__:
            descriptor = klass.__dict__["pl1"]
            break
    assert isinstance(descriptor, property)

def test_model_has_gameSize():
    assert hasattr(Model, "gameSize")
    descriptor = None
    for klass in Model.__mro__:
        if "gameSize" in klass.__dict__:
            descriptor = klass.__dict__["gameSize"]
            break
    assert isinstance(descriptor, property)

def test_model_has_pl1points():
    assert hasattr(Model, "pl1points")
    descriptor = None
    for klass in Model.__mro__:
        if "pl1points" in klass.__dict__:
            descriptor = klass.__dict__["pl1points"]
            break
    assert isinstance(descriptor, property)

def test_model_has_gameOver():
    assert hasattr(Model, "gameOver")
    descriptor = None
    for klass in Model.__mro__:
        if "gameOver" in klass.__dict__:
            descriptor = klass.__dict__["gameOver"]
            break
    assert isinstance(descriptor, property)

def test_model_has_pl2():
    assert hasattr(Model, "pl2")
    descriptor = None
    for klass in Model.__mro__:
        if "pl2" in klass.__dict__:
            descriptor = klass.__dict__["pl2"]
            break
    assert isinstance(descriptor, property)

def test_model_has_selected():
    assert hasattr(Model, "selected")
    descriptor = None
    for klass in Model.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_model_has_steps():
    assert hasattr(Model, "steps")
    descriptor = None
    for klass in Model.__mro__:
        if "steps" in klass.__dict__:
            descriptor = klass.__dict__["steps"]
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
Persistence_strategy = st.builds(
    Persistence,
)
Class_strategy = st.builds(
    Class,
)
SaveGameWidget_strategy = st.builds(
    SaveGameWidget,
    _listWidget=
        safe_text,
    okButton=
        safe_text,
    cancelButton=
        safe_text
)
LoadGameWidget_strategy = st.builds(
    LoadGameWidget,
)
felhaszn_l__Actor_strategy = st.builds(
    felhaszn_l__Actor,
)
Model_strategy = st.builds(
    Model,
    gameTable=
        safe_text,
    pl2points=
        safe_text,
    playerNr=
        safe_text,
    goodselected=
        st.booleans(),
    pl1=
        safe_text,
    gameSize=
        safe_text,
    pl1points=
        safe_text,
    gameOver=
        st.booleans(),
    pl2=
        safe_text,
    selected=
        safe_text,
    steps=
        safe_text
)

@given(instance=Persistence_strategy)
@settings(max_examples=50)
def test_persistence_instantiation(instance):
    assert isinstance(instance, Persistence)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=SaveGameWidget_strategy)
@settings(max_examples=50)
def test_savegamewidget_instantiation(instance):
    assert isinstance(instance, SaveGameWidget)



@given(instance=SaveGameWidget_strategy)
def test_savegamewidget__listWidget_setter(instance):
    original = instance._listWidget
    instance._listWidget = original
    assert instance._listWidget == original



@given(instance=SaveGameWidget_strategy)
def test_savegamewidget_okButton_setter(instance):
    original = instance.okButton
    instance.okButton = original
    assert instance.okButton == original



@given(instance=SaveGameWidget_strategy)
def test_savegamewidget_cancelButton_setter(instance):
    original = instance.cancelButton
    instance.cancelButton = original
    assert instance.cancelButton == original

@given(instance=LoadGameWidget_strategy)
@settings(max_examples=50)
def test_loadgamewidget_instantiation(instance):
    assert isinstance(instance, LoadGameWidget)

@given(instance=felhaszn_l__Actor_strategy)
@settings(max_examples=50)
def test_felhaszn_l__actor_instantiation(instance):
    assert isinstance(instance, felhaszn_l__Actor)

@given(instance=Model_strategy)
@settings(max_examples=50)
def test_model_instantiation(instance):
    assert isinstance(instance, Model)



@given(instance=Model_strategy)
def test_model_gameTable_setter(instance):
    original = instance.gameTable
    instance.gameTable = original
    assert instance.gameTable == original



@given(instance=Model_strategy)
def test_model_pl2points_setter(instance):
    original = instance.pl2points
    instance.pl2points = original
    assert instance.pl2points == original



@given(instance=Model_strategy)
def test_model_playerNr_setter(instance):
    original = instance.playerNr
    instance.playerNr = original
    assert instance.playerNr == original



@given(instance=Model_strategy)
def test_model_goodselected_setter(instance):
    original = instance.goodselected
    instance.goodselected = original
    assert instance.goodselected == original



@given(instance=Model_strategy)
def test_model_pl1_setter(instance):
    original = instance.pl1
    instance.pl1 = original
    assert instance.pl1 == original



@given(instance=Model_strategy)
def test_model_gameSize_setter(instance):
    original = instance.gameSize
    instance.gameSize = original
    assert instance.gameSize == original



@given(instance=Model_strategy)
def test_model_pl1points_setter(instance):
    original = instance.pl1points
    instance.pl1points = original
    assert instance.pl1points == original



@given(instance=Model_strategy)
def test_model_gameOver_setter(instance):
    original = instance.gameOver
    instance.gameOver = original
    assert instance.gameOver == original



@given(instance=Model_strategy)
def test_model_pl2_setter(instance):
    original = instance.pl2
    instance.pl2 = original
    assert instance.pl2 == original



@given(instance=Model_strategy)
def test_model_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original



@given(instance=Model_strategy)
def test_model_steps_setter(instance):
    original = instance.steps
    instance.steps = original
    assert instance.steps == original
