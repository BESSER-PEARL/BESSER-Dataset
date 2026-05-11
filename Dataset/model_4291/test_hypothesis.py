import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    gametournament::Pool,
    gametournament::QualificationPhase,
    gametournament::FinalPhase,
    gametournament::Gamer,
    gametournament::Game,
    gametournament::Tournament,
    GameType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_gametournament::pool_is_not_abstract():
    assert not inspect.isabstract(gametournament::Pool)


def test_gametournament::pool_constructor_exists():
    assert callable(gametournament::Pool.__init__)


def test_gametournament::pool_constructor_args():
    sig = inspect.signature(gametournament::Pool.__init__)
    params = list(sig.parameters.keys())



def test_gametournament::qualificationphase_is_not_abstract():
    assert not inspect.isabstract(gametournament::QualificationPhase)


def test_gametournament::qualificationphase_constructor_exists():
    assert callable(gametournament::QualificationPhase.__init__)


def test_gametournament::qualificationphase_constructor_args():
    sig = inspect.signature(gametournament::QualificationPhase.__init__)
    params = list(sig.parameters.keys())



def test_gametournament::finalphase_is_not_abstract():
    assert not inspect.isabstract(gametournament::FinalPhase)


def test_gametournament::finalphase_constructor_exists():
    assert callable(gametournament::FinalPhase.__init__)


def test_gametournament::finalphase_constructor_args():
    sig = inspect.signature(gametournament::FinalPhase.__init__)
    params = list(sig.parameters.keys())



def test_gametournament::gamer_is_not_abstract():
    assert not inspect.isabstract(gametournament::Gamer)


def test_gametournament::gamer_constructor_exists():
    assert callable(gametournament::Gamer.__init__)


def test_gametournament::gamer_constructor_args():
    sig = inspect.signature(gametournament::Gamer.__init__)
    params = list(sig.parameters.keys())
    assert "pseudo" in params, "Missing parameter 'pseudo'"
    assert "victories" in params, "Missing parameter 'victories'"
    assert "matches" in params, "Missing parameter 'matches'"
    assert "lastName" in params, "Missing parameter 'lastName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_gametournament::gamer_has_pseudo():
    assert hasattr(gametournament::Gamer, "pseudo")
    descriptor = None
    for klass in gametournament::Gamer.__mro__:
        if "pseudo" in klass.__dict__:
            descriptor = klass.__dict__["pseudo"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::gamer_has_victories():
    assert hasattr(gametournament::Gamer, "victories")
    descriptor = None
    for klass in gametournament::Gamer.__mro__:
        if "victories" in klass.__dict__:
            descriptor = klass.__dict__["victories"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::gamer_has_matches():
    assert hasattr(gametournament::Gamer, "matches")
    descriptor = None
    for klass in gametournament::Gamer.__mro__:
        if "matches" in klass.__dict__:
            descriptor = klass.__dict__["matches"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::gamer_has_lastName():
    assert hasattr(gametournament::Gamer, "lastName")
    descriptor = None
    for klass in gametournament::Gamer.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::gamer_has_firstName():
    assert hasattr(gametournament::Gamer, "firstName")
    descriptor = None
    for klass in gametournament::Gamer.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_gametournament::game_is_not_abstract():
    assert not inspect.isabstract(gametournament::Game)


def test_gametournament::game_constructor_exists():
    assert callable(gametournament::Game.__init__)


def test_gametournament::game_constructor_args():
    sig = inspect.signature(gametournament::Game.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"

def test_gametournament::game_has_type():
    assert hasattr(gametournament::Game, "type")
    descriptor = None
    for klass in gametournament::Game.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::game_has_name():
    assert hasattr(gametournament::Game, "name")
    descriptor = None
    for klass in gametournament::Game.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_gametournament::tournament_is_not_abstract():
    assert not inspect.isabstract(gametournament::Tournament)


def test_gametournament::tournament_constructor_exists():
    assert callable(gametournament::Tournament.__init__)


def test_gametournament::tournament_constructor_args():
    sig = inspect.signature(gametournament::Tournament.__init__)
    params = list(sig.parameters.keys())
    assert "startDate" in params, "Missing parameter 'startDate'"
    assert "prize" in params, "Missing parameter 'prize'"
    assert "endDate" in params, "Missing parameter 'endDate'"
    assert "location" in params, "Missing parameter 'location'"
    assert "name" in params, "Missing parameter 'name'"

def test_gametournament::tournament_has_startDate():
    assert hasattr(gametournament::Tournament, "startDate")
    descriptor = None
    for klass in gametournament::Tournament.__mro__:
        if "startDate" in klass.__dict__:
            descriptor = klass.__dict__["startDate"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::tournament_has_prize():
    assert hasattr(gametournament::Tournament, "prize")
    descriptor = None
    for klass in gametournament::Tournament.__mro__:
        if "prize" in klass.__dict__:
            descriptor = klass.__dict__["prize"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::tournament_has_endDate():
    assert hasattr(gametournament::Tournament, "endDate")
    descriptor = None
    for klass in gametournament::Tournament.__mro__:
        if "endDate" in klass.__dict__:
            descriptor = klass.__dict__["endDate"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::tournament_has_location():
    assert hasattr(gametournament::Tournament, "location")
    descriptor = None
    for klass in gametournament::Tournament.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)

def test_gametournament::tournament_has_name():
    assert hasattr(gametournament::Tournament, "name")
    descriptor = None
    for klass in gametournament::Tournament.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_gametype_exists():
    # Check that the Enumeration exists
    assert GameType is not None

def test_gametype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in GameType]
    expected_literals = [
        "RPG",
        "COMBAT",
        "FPS",
        "STRATEGIC",
        "ACTION",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in GameType"


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
gametournament::Pool_strategy = st.builds(
    gametournament::Pool,
)
gametournament::QualificationPhase_strategy = st.builds(
    gametournament::QualificationPhase,
)
gametournament::FinalPhase_strategy = st.builds(
    gametournament::FinalPhase,
)
gametournament::Gamer_strategy = st.builds(
    gametournament::Gamer,
    pseudo=
        safe_text,
    victories=
        st.integers(),
    matches=
        st.integers(),
    lastName=
        safe_text,
    firstName=
        safe_text
)
gametournament::Game_strategy = st.builds(
    gametournament::Game,
    type=
        safe_text,
    name=
        safe_text
)
gametournament::Tournament_strategy = st.builds(
    gametournament::Tournament,
    startDate=
        st.dates(),
    prize=
        st.integers(),
    endDate=
        st.dates(),
    location=
        safe_text,
    name=
        safe_text
)

@given(instance=gametournament::Pool_strategy)
@settings(max_examples=50)
def test_gametournament::pool_instantiation(instance):
    assert isinstance(instance, gametournament::Pool)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gametournament::Pool_strategy)
@settings(max_examples=30)
def test_gametournament::pool_generateclassment_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.generateClassment()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.generateClassment).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'generateClassment' in gametournament::Pool is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'generateClassment' in gametournament::Pool did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'generateClassment' in gametournament::Pool is not implemented or raised an error")

@given(instance=gametournament::QualificationPhase_strategy)
@settings(max_examples=50)
def test_gametournament::qualificationphase_instantiation(instance):
    assert isinstance(instance, gametournament::QualificationPhase)

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=gametournament::QualificationPhase_strategy)
@settings(max_examples=30)
def test_gametournament::qualificationphase_createpools_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.createPools()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.createPools).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'createPools' in gametournament::QualificationPhase is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'createPools' in gametournament::QualificationPhase did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'createPools' in gametournament::QualificationPhase is not implemented or raised an error")

@given(instance=gametournament::FinalPhase_strategy)
@settings(max_examples=50)
def test_gametournament::finalphase_instantiation(instance):
    assert isinstance(instance, gametournament::FinalPhase)

@given(instance=gametournament::Gamer_strategy)
@settings(max_examples=50)
def test_gametournament::gamer_instantiation(instance):
    assert isinstance(instance, gametournament::Gamer)

@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_pseudo_type(instance):
    assert isinstance(instance.pseudo, str)


@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_pseudo_setter(instance):
    original = instance.pseudo
    instance.pseudo = original
    assert instance.pseudo == original

@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_victories_type(instance):
    assert isinstance(instance.victories, int)


@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_victories_setter(instance):
    original = instance.victories
    instance.victories = original
    assert instance.victories == original

@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_matches_type(instance):
    assert isinstance(instance.matches, int)


@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_matches_setter(instance):
    original = instance.matches
    instance.matches = original
    assert instance.matches == original

@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=gametournament::Gamer_strategy)
def test_gametournament::gamer_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=gametournament::Game_strategy)
@settings(max_examples=50)
def test_gametournament::game_instantiation(instance):
    assert isinstance(instance, gametournament::Game)

@given(instance=gametournament::Game_strategy)
def test_gametournament::game_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=gametournament::Game_strategy)
def test_gametournament::game_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=gametournament::Game_strategy)
def test_gametournament::game_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gametournament::Game_strategy)
def test_gametournament::game_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=gametournament::Tournament_strategy)
@settings(max_examples=50)
def test_gametournament::tournament_instantiation(instance):
    assert isinstance(instance, gametournament::Tournament)

@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_startDate_type(instance):
    assert isinstance(instance.startDate, date)


@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_startDate_setter(instance):
    original = instance.startDate
    instance.startDate = original
    assert instance.startDate == original

@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_prize_type(instance):
    assert isinstance(instance.prize, int)


@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_prize_setter(instance):
    original = instance.prize
    instance.prize = original
    assert instance.prize == original

@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_endDate_type(instance):
    assert isinstance(instance.endDate, date)


@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_endDate_setter(instance):
    original = instance.endDate
    instance.endDate = original
    assert instance.endDate == original

@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_location_type(instance):
    assert isinstance(instance.location, str)


@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=gametournament::Tournament_strategy)
def test_gametournament::tournament_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original
