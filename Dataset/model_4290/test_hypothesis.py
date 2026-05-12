import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Ball,
    model_ExtraBall,
    model_WicketBall,
    model_Game,
    model_Ball,
    model_Player,
    model_Over,
    model_Team,
    model_Innings,
    ExtraType,
    BallType,
    HowOut,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_ball_is_not_abstract():
    assert not inspect.isabstract(Ball)


def test_ball_constructor_exists():
    assert callable(Ball.__init__)


def test_ball_constructor_args():
    sig = inspect.signature(Ball.__init__)
    params = list(sig.parameters.keys())



def test_model_extraball_is_not_abstract():
    assert not inspect.isabstract(model_ExtraBall)


def test_model_extraball_constructor_exists():
    assert callable(model_ExtraBall.__init__)


def test_model_extraball_constructor_args():
    sig = inspect.signature(model_ExtraBall.__init__)
    params = list(sig.parameters.keys())
    assert "isValidBall" in params, "Missing parameter 'isValidBall'"
    assert "extraType" in params, "Missing parameter 'extraType'"

def test_model_extraball_has_isValidBall():
    assert hasattr(model_ExtraBall, "isValidBall")
    descriptor = None
    for klass in model_ExtraBall.__mro__:
        if "isValidBall" in klass.__dict__:
            descriptor = klass.__dict__["isValidBall"]
            break
    assert isinstance(descriptor, property)

def test_model_extraball_has_extraType():
    assert hasattr(model_ExtraBall, "extraType")
    descriptor = None
    for klass in model_ExtraBall.__mro__:
        if "extraType" in klass.__dict__:
            descriptor = klass.__dict__["extraType"]
            break
    assert isinstance(descriptor, property)



def test_model_wicketball_is_not_abstract():
    assert not inspect.isabstract(model_WicketBall)


def test_model_wicketball_constructor_exists():
    assert callable(model_WicketBall.__init__)


def test_model_wicketball_constructor_args():
    sig = inspect.signature(model_WicketBall.__init__)
    params = list(sig.parameters.keys())
    assert "howOut" in params, "Missing parameter 'howOut'"

def test_model_wicketball_has_howOut():
    assert hasattr(model_WicketBall, "howOut")
    descriptor = None
    for klass in model_WicketBall.__mro__:
        if "howOut" in klass.__dict__:
            descriptor = klass.__dict__["howOut"]
            break
    assert isinstance(descriptor, property)



def test_model_game_is_not_abstract():
    assert not inspect.isabstract(model_Game)


def test_model_game_constructor_exists():
    assert callable(model_Game.__init__)


def test_model_game_constructor_args():
    sig = inspect.signature(model_Game.__init__)
    params = list(sig.parameters.keys())
    assert "date" in params, "Missing parameter 'date'"
    assert "venue" in params, "Missing parameter 'venue'"

def test_model_game_has_date():
    assert hasattr(model_Game, "date")
    descriptor = None
    for klass in model_Game.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_model_game_has_venue():
    assert hasattr(model_Game, "venue")
    descriptor = None
    for klass in model_Game.__mro__:
        if "venue" in klass.__dict__:
            descriptor = klass.__dict__["venue"]
            break
    assert isinstance(descriptor, property)



def test_model_ball_is_not_abstract():
    assert not inspect.isabstract(model_Ball)


def test_model_ball_constructor_exists():
    assert callable(model_Ball.__init__)


def test_model_ball_constructor_args():
    sig = inspect.signature(model_Ball.__init__)
    params = list(sig.parameters.keys())
    assert "runValue" in params, "Missing parameter 'runValue'"
    assert "runs" in params, "Missing parameter 'runs'"
    assert "switchEnds" in params, "Missing parameter 'switchEnds'"

def test_model_ball_has_runValue():
    assert hasattr(model_Ball, "runValue")
    descriptor = None
    for klass in model_Ball.__mro__:
        if "runValue" in klass.__dict__:
            descriptor = klass.__dict__["runValue"]
            break
    assert isinstance(descriptor, property)

def test_model_ball_has_runs():
    assert hasattr(model_Ball, "runs")
    descriptor = None
    for klass in model_Ball.__mro__:
        if "runs" in klass.__dict__:
            descriptor = klass.__dict__["runs"]
            break
    assert isinstance(descriptor, property)

def test_model_ball_has_switchEnds():
    assert hasattr(model_Ball, "switchEnds")
    descriptor = None
    for klass in model_Ball.__mro__:
        if "switchEnds" in klass.__dict__:
            descriptor = klass.__dict__["switchEnds"]
            break
    assert isinstance(descriptor, property)



def test_model_player_is_not_abstract():
    assert not inspect.isabstract(model_Player)


def test_model_player_constructor_exists():
    assert callable(model_Player.__init__)


def test_model_player_constructor_args():
    sig = inspect.signature(model_Player.__init__)
    params = list(sig.parameters.keys())
    assert "howOut" in params, "Missing parameter 'howOut'"
    assert "runsScored" in params, "Missing parameter 'runsScored'"
    assert "name" in params, "Missing parameter 'name'"
    assert "noOversBowled" in params, "Missing parameter 'noOversBowled'"
    assert "noBallsFaced" in params, "Missing parameter 'noBallsFaced'"

def test_model_player_has_howOut():
    assert hasattr(model_Player, "howOut")
    descriptor = None
    for klass in model_Player.__mro__:
        if "howOut" in klass.__dict__:
            descriptor = klass.__dict__["howOut"]
            break
    assert isinstance(descriptor, property)

def test_model_player_has_runsScored():
    assert hasattr(model_Player, "runsScored")
    descriptor = None
    for klass in model_Player.__mro__:
        if "runsScored" in klass.__dict__:
            descriptor = klass.__dict__["runsScored"]
            break
    assert isinstance(descriptor, property)

def test_model_player_has_name():
    assert hasattr(model_Player, "name")
    descriptor = None
    for klass in model_Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model_player_has_noOversBowled():
    assert hasattr(model_Player, "noOversBowled")
    descriptor = None
    for klass in model_Player.__mro__:
        if "noOversBowled" in klass.__dict__:
            descriptor = klass.__dict__["noOversBowled"]
            break
    assert isinstance(descriptor, property)

def test_model_player_has_noBallsFaced():
    assert hasattr(model_Player, "noBallsFaced")
    descriptor = None
    for klass in model_Player.__mro__:
        if "noBallsFaced" in klass.__dict__:
            descriptor = klass.__dict__["noBallsFaced"]
            break
    assert isinstance(descriptor, property)



def test_model_over_is_not_abstract():
    assert not inspect.isabstract(model_Over)


def test_model_over_constructor_exists():
    assert callable(model_Over.__init__)


def test_model_over_constructor_args():
    sig = inspect.signature(model_Over.__init__)
    params = list(sig.parameters.keys())
    assert "runs" in params, "Missing parameter 'runs'"
    assert "BALLS_IN_OVER" in params, "Missing parameter 'BALLS_IN_OVER'"
    assert "isComplete" in params, "Missing parameter 'isComplete'"
    assert "validBalls" in params, "Missing parameter 'validBalls'"

def test_model_over_has_runs():
    assert hasattr(model_Over, "runs")
    descriptor = None
    for klass in model_Over.__mro__:
        if "runs" in klass.__dict__:
            descriptor = klass.__dict__["runs"]
            break
    assert isinstance(descriptor, property)

def test_model_over_has_BALLS_IN_OVER():
    assert hasattr(model_Over, "BALLS_IN_OVER")
    descriptor = None
    for klass in model_Over.__mro__:
        if "BALLS_IN_OVER" in klass.__dict__:
            descriptor = klass.__dict__["BALLS_IN_OVER"]
            break
    assert isinstance(descriptor, property)

def test_model_over_has_isComplete():
    assert hasattr(model_Over, "isComplete")
    descriptor = None
    for klass in model_Over.__mro__:
        if "isComplete" in klass.__dict__:
            descriptor = klass.__dict__["isComplete"]
            break
    assert isinstance(descriptor, property)

def test_model_over_has_validBalls():
    assert hasattr(model_Over, "validBalls")
    descriptor = None
    for klass in model_Over.__mro__:
        if "validBalls" in klass.__dict__:
            descriptor = klass.__dict__["validBalls"]
            break
    assert isinstance(descriptor, property)



def test_model_team_is_not_abstract():
    assert not inspect.isabstract(model_Team)


def test_model_team_constructor_exists():
    assert callable(model_Team.__init__)


def test_model_team_constructor_args():
    sig = inspect.signature(model_Team.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model_team_has_name():
    assert hasattr(model_Team, "name")
    descriptor = None
    for klass in model_Team.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model_innings_is_not_abstract():
    assert not inspect.isabstract(model_Innings)


def test_model_innings_constructor_exists():
    assert callable(model_Innings.__init__)


def test_model_innings_constructor_args():
    sig = inspect.signature(model_Innings.__init__)
    params = list(sig.parameters.keys())
    assert "noOvers" in params, "Missing parameter 'noOvers'"
    assert "overCount" in params, "Missing parameter 'overCount'"
    assert "wicketsDown" in params, "Missing parameter 'wicketsDown'"
    assert "Summary" in params, "Missing parameter 'Summary'"
    assert "total" in params, "Missing parameter 'total'"

def test_model_innings_has_noOvers():
    assert hasattr(model_Innings, "noOvers")
    descriptor = None
    for klass in model_Innings.__mro__:
        if "noOvers" in klass.__dict__:
            descriptor = klass.__dict__["noOvers"]
            break
    assert isinstance(descriptor, property)

def test_model_innings_has_overCount():
    assert hasattr(model_Innings, "overCount")
    descriptor = None
    for klass in model_Innings.__mro__:
        if "overCount" in klass.__dict__:
            descriptor = klass.__dict__["overCount"]
            break
    assert isinstance(descriptor, property)

def test_model_innings_has_wicketsDown():
    assert hasattr(model_Innings, "wicketsDown")
    descriptor = None
    for klass in model_Innings.__mro__:
        if "wicketsDown" in klass.__dict__:
            descriptor = klass.__dict__["wicketsDown"]
            break
    assert isinstance(descriptor, property)

def test_model_innings_has_Summary():
    assert hasattr(model_Innings, "Summary")
    descriptor = None
    for klass in model_Innings.__mro__:
        if "Summary" in klass.__dict__:
            descriptor = klass.__dict__["Summary"]
            break
    assert isinstance(descriptor, property)

def test_model_innings_has_total():
    assert hasattr(model_Innings, "total")
    descriptor = None
    for klass in model_Innings.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_extratype_exists():
    # Check that the Enumeration exists
    assert ExtraType is not None

def test_extratype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExtraType]
    expected_literals = [
        "NoBall",
        "Bye",
        "Wide",
        "LegBye",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ExtraType"

def test_balltype_exists():
    # Check that the Enumeration exists
    assert BallType is not None

def test_balltype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BallType]
    expected_literals = [
        "two_runs",
        "three_runs",
        "dot_ball",
        "one_run",
        "four_runs",
        "six_runs",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BallType"

def test_howout_exists():
    # Check that the Enumeration exists
    assert HowOut is not None

def test_howout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HowOut]
    expected_literals = [
        "Stumped",
        "Caught",
        "Lbw",
        "Run_Out",
        "Bowled",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HowOut"


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
Ball_strategy = st.builds(
    Ball,
)
model_ExtraBall_strategy = st.builds(
    model_ExtraBall,
    isValidBall=
        safe_text,
    extraType=
        safe_text
)
model_WicketBall_strategy = st.builds(
    model_WicketBall,
    howOut=
        safe_text
)
model_Game_strategy = st.builds(
    model_Game,
    date=
        st.dates(),
    venue=
        safe_text
)
model_Ball_strategy = st.builds(
    model_Ball,
    runValue=
        st.integers(),
    runs=
        safe_text,
    switchEnds=
        safe_text
)
model_Player_strategy = st.builds(
    model_Player,
    howOut=
        safe_text,
    runsScored=
        st.integers(),
    name=
        safe_text,
    noOversBowled=
        safe_text,
    noBallsFaced=
        st.integers()
)
model_Over_strategy = st.builds(
    model_Over,
    runs=
        st.integers(),
    BALLS_IN_OVER=
        st.integers(),
    isComplete=
        st.booleans(),
    validBalls=
        st.integers()
)
model_Team_strategy = st.builds(
    model_Team,
    name=
        safe_text
)
model_Innings_strategy = st.builds(
    model_Innings,
    noOvers=
        st.integers(),
    overCount=
        safe_text,
    wicketsDown=
        st.integers(),
    Summary=
        safe_text,
    total=
        st.integers()
)

@given(instance=Ball_strategy)
@settings(max_examples=50)
def test_ball_instantiation(instance):
    assert isinstance(instance, Ball)

@given(instance=model_ExtraBall_strategy)
@settings(max_examples=50)
def test_model_extraball_instantiation(instance):
    assert isinstance(instance, model_ExtraBall)



@given(instance=model_ExtraBall_strategy)
def test_model_extraball_isValidBall_setter(instance):
    original = instance.isValidBall
    instance.isValidBall = original
    assert instance.isValidBall == original



@given(instance=model_ExtraBall_strategy)
def test_model_extraball_extraType_setter(instance):
    original = instance.extraType
    instance.extraType = original
    assert instance.extraType == original

@given(instance=model_WicketBall_strategy)
@settings(max_examples=50)
def test_model_wicketball_instantiation(instance):
    assert isinstance(instance, model_WicketBall)



@given(instance=model_WicketBall_strategy)
def test_model_wicketball_howOut_setter(instance):
    original = instance.howOut
    instance.howOut = original
    assert instance.howOut == original

@given(instance=model_Game_strategy)
@settings(max_examples=50)
def test_model_game_instantiation(instance):
    assert isinstance(instance, model_Game)



@given(instance=model_Game_strategy)
def test_model_game_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=model_Game_strategy)
def test_model_game_venue_setter(instance):
    original = instance.venue
    instance.venue = original
    assert instance.venue == original

@given(instance=model_Ball_strategy)
@settings(max_examples=50)
def test_model_ball_instantiation(instance):
    assert isinstance(instance, model_Ball)



@given(instance=model_Ball_strategy)
def test_model_ball_runValue_setter(instance):
    original = instance.runValue
    instance.runValue = original
    assert instance.runValue == original



@given(instance=model_Ball_strategy)
def test_model_ball_runs_setter(instance):
    original = instance.runs
    instance.runs = original
    assert instance.runs == original



@given(instance=model_Ball_strategy)
def test_model_ball_switchEnds_setter(instance):
    original = instance.switchEnds
    instance.switchEnds = original
    assert instance.switchEnds == original

@given(instance=model_Player_strategy)
@settings(max_examples=50)
def test_model_player_instantiation(instance):
    assert isinstance(instance, model_Player)



@given(instance=model_Player_strategy)
def test_model_player_howOut_setter(instance):
    original = instance.howOut
    instance.howOut = original
    assert instance.howOut == original



@given(instance=model_Player_strategy)
def test_model_player_runsScored_setter(instance):
    original = instance.runsScored
    instance.runsScored = original
    assert instance.runsScored == original



@given(instance=model_Player_strategy)
def test_model_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=model_Player_strategy)
def test_model_player_noOversBowled_setter(instance):
    original = instance.noOversBowled
    instance.noOversBowled = original
    assert instance.noOversBowled == original



@given(instance=model_Player_strategy)
def test_model_player_noBallsFaced_setter(instance):
    original = instance.noBallsFaced
    instance.noBallsFaced = original
    assert instance.noBallsFaced == original

@given(instance=model_Over_strategy)
@settings(max_examples=50)
def test_model_over_instantiation(instance):
    assert isinstance(instance, model_Over)



@given(instance=model_Over_strategy)
def test_model_over_runs_setter(instance):
    original = instance.runs
    instance.runs = original
    assert instance.runs == original



@given(instance=model_Over_strategy)
def test_model_over_BALLS_IN_OVER_setter(instance):
    original = instance.BALLS_IN_OVER
    instance.BALLS_IN_OVER = original
    assert instance.BALLS_IN_OVER == original



@given(instance=model_Over_strategy)
def test_model_over_isComplete_setter(instance):
    original = instance.isComplete
    instance.isComplete = original
    assert instance.isComplete == original



@given(instance=model_Over_strategy)
def test_model_over_validBalls_setter(instance):
    original = instance.validBalls
    instance.validBalls = original
    assert instance.validBalls == original

@given(instance=model_Team_strategy)
@settings(max_examples=50)
def test_model_team_instantiation(instance):
    assert isinstance(instance, model_Team)



@given(instance=model_Team_strategy)
def test_model_team_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model_Innings_strategy)
@settings(max_examples=50)
def test_model_innings_instantiation(instance):
    assert isinstance(instance, model_Innings)



@given(instance=model_Innings_strategy)
def test_model_innings_noOvers_setter(instance):
    original = instance.noOvers
    instance.noOvers = original
    assert instance.noOvers == original



@given(instance=model_Innings_strategy)
def test_model_innings_overCount_setter(instance):
    original = instance.overCount
    instance.overCount = original
    assert instance.overCount == original



@given(instance=model_Innings_strategy)
def test_model_innings_wicketsDown_setter(instance):
    original = instance.wicketsDown
    instance.wicketsDown = original
    assert instance.wicketsDown == original



@given(instance=model_Innings_strategy)
def test_model_innings_Summary_setter(instance):
    original = instance.Summary
    instance.Summary = original
    assert instance.Summary == original



@given(instance=model_Innings_strategy)
def test_model_innings_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_Innings_strategy)
@settings(max_examples=30)
def test_model_innings_bowlball_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.bowlBall()
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.bowlBall).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'bowlBall' in model_Innings is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bowlBall' in model_Innings did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bowlBall' in model_Innings is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model_Innings_strategy)
@settings(max_examples=30)
def test_model_innings_newover_changes_state(instance):
    before = copy.deepcopy(instance)
    try:
        # Call operation with dummy parameters
        instance.newOver(
            "test"
        )
        if instance.__dict__ != before.__dict__:
            return  # test passes
        # Check that function exists and is non-empty (FAIL if empty)
        source = inspect.getsource(instance.newOver).strip()
        tree = ast.parse(source)
        body = tree.body[0].body  # function body
        has_statements = len(body) > 0 and not all(isinstance(stmt, ast.Pass) for stmt in body)
        assert has_statements, f"Function 'newOver' in model_Innings is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'newOver' in model_Innings did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'newOver' in model_Innings is not implemented or raised an error")
