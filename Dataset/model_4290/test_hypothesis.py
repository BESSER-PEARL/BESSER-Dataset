import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Ball,
    model::ExtraBall,
    model::WicketBall,
    model::Game,
    model::Ball,
    model::Player,
    model::Over,
    model::Team,
    model::Innings,
    HowOut,
    ExtraType,
    BallType,
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



def test_model::extraball_is_not_abstract():
    assert not inspect.isabstract(model::ExtraBall)


def test_model::extraball_constructor_exists():
    assert callable(model::ExtraBall.__init__)


def test_model::extraball_constructor_args():
    sig = inspect.signature(model::ExtraBall.__init__)
    params = list(sig.parameters.keys())
    assert "extraType" in params, "Missing parameter 'extraType'"
    assert "isValidBall" in params, "Missing parameter 'isValidBall'"

def test_model::extraball_has_extraType():
    assert hasattr(model::ExtraBall, "extraType")
    descriptor = None
    for klass in model::ExtraBall.__mro__:
        if "extraType" in klass.__dict__:
            descriptor = klass.__dict__["extraType"]
            break
    assert isinstance(descriptor, property)

def test_model::extraball_has_isValidBall():
    assert hasattr(model::ExtraBall, "isValidBall")
    descriptor = None
    for klass in model::ExtraBall.__mro__:
        if "isValidBall" in klass.__dict__:
            descriptor = klass.__dict__["isValidBall"]
            break
    assert isinstance(descriptor, property)



def test_model::wicketball_is_not_abstract():
    assert not inspect.isabstract(model::WicketBall)


def test_model::wicketball_constructor_exists():
    assert callable(model::WicketBall.__init__)


def test_model::wicketball_constructor_args():
    sig = inspect.signature(model::WicketBall.__init__)
    params = list(sig.parameters.keys())
    assert "howOut" in params, "Missing parameter 'howOut'"

def test_model::wicketball_has_howOut():
    assert hasattr(model::WicketBall, "howOut")
    descriptor = None
    for klass in model::WicketBall.__mro__:
        if "howOut" in klass.__dict__:
            descriptor = klass.__dict__["howOut"]
            break
    assert isinstance(descriptor, property)



def test_model::game_is_not_abstract():
    assert not inspect.isabstract(model::Game)


def test_model::game_constructor_exists():
    assert callable(model::Game.__init__)


def test_model::game_constructor_args():
    sig = inspect.signature(model::Game.__init__)
    params = list(sig.parameters.keys())
    assert "venue" in params, "Missing parameter 'venue'"
    assert "date" in params, "Missing parameter 'date'"

def test_model::game_has_venue():
    assert hasattr(model::Game, "venue")
    descriptor = None
    for klass in model::Game.__mro__:
        if "venue" in klass.__dict__:
            descriptor = klass.__dict__["venue"]
            break
    assert isinstance(descriptor, property)

def test_model::game_has_date():
    assert hasattr(model::Game, "date")
    descriptor = None
    for klass in model::Game.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_model::ball_is_not_abstract():
    assert not inspect.isabstract(model::Ball)


def test_model::ball_constructor_exists():
    assert callable(model::Ball.__init__)


def test_model::ball_constructor_args():
    sig = inspect.signature(model::Ball.__init__)
    params = list(sig.parameters.keys())
    assert "runValue" in params, "Missing parameter 'runValue'"
    assert "runs" in params, "Missing parameter 'runs'"
    assert "switchEnds" in params, "Missing parameter 'switchEnds'"

def test_model::ball_has_runValue():
    assert hasattr(model::Ball, "runValue")
    descriptor = None
    for klass in model::Ball.__mro__:
        if "runValue" in klass.__dict__:
            descriptor = klass.__dict__["runValue"]
            break
    assert isinstance(descriptor, property)

def test_model::ball_has_runs():
    assert hasattr(model::Ball, "runs")
    descriptor = None
    for klass in model::Ball.__mro__:
        if "runs" in klass.__dict__:
            descriptor = klass.__dict__["runs"]
            break
    assert isinstance(descriptor, property)

def test_model::ball_has_switchEnds():
    assert hasattr(model::Ball, "switchEnds")
    descriptor = None
    for klass in model::Ball.__mro__:
        if "switchEnds" in klass.__dict__:
            descriptor = klass.__dict__["switchEnds"]
            break
    assert isinstance(descriptor, property)



def test_model::player_is_not_abstract():
    assert not inspect.isabstract(model::Player)


def test_model::player_constructor_exists():
    assert callable(model::Player.__init__)


def test_model::player_constructor_args():
    sig = inspect.signature(model::Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "noOversBowled" in params, "Missing parameter 'noOversBowled'"
    assert "howOut" in params, "Missing parameter 'howOut'"
    assert "noBallsFaced" in params, "Missing parameter 'noBallsFaced'"
    assert "runsScored" in params, "Missing parameter 'runsScored'"

def test_model::player_has_name():
    assert hasattr(model::Player, "name")
    descriptor = None
    for klass in model::Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_model::player_has_noOversBowled():
    assert hasattr(model::Player, "noOversBowled")
    descriptor = None
    for klass in model::Player.__mro__:
        if "noOversBowled" in klass.__dict__:
            descriptor = klass.__dict__["noOversBowled"]
            break
    assert isinstance(descriptor, property)

def test_model::player_has_howOut():
    assert hasattr(model::Player, "howOut")
    descriptor = None
    for klass in model::Player.__mro__:
        if "howOut" in klass.__dict__:
            descriptor = klass.__dict__["howOut"]
            break
    assert isinstance(descriptor, property)

def test_model::player_has_noBallsFaced():
    assert hasattr(model::Player, "noBallsFaced")
    descriptor = None
    for klass in model::Player.__mro__:
        if "noBallsFaced" in klass.__dict__:
            descriptor = klass.__dict__["noBallsFaced"]
            break
    assert isinstance(descriptor, property)

def test_model::player_has_runsScored():
    assert hasattr(model::Player, "runsScored")
    descriptor = None
    for klass in model::Player.__mro__:
        if "runsScored" in klass.__dict__:
            descriptor = klass.__dict__["runsScored"]
            break
    assert isinstance(descriptor, property)



def test_model::over_is_not_abstract():
    assert not inspect.isabstract(model::Over)


def test_model::over_constructor_exists():
    assert callable(model::Over.__init__)


def test_model::over_constructor_args():
    sig = inspect.signature(model::Over.__init__)
    params = list(sig.parameters.keys())
    assert "validBalls" in params, "Missing parameter 'validBalls'"
    assert "runs" in params, "Missing parameter 'runs'"
    assert "isComplete" in params, "Missing parameter 'isComplete'"
    assert "BALLS_IN_OVER" in params, "Missing parameter 'BALLS_IN_OVER'"

def test_model::over_has_validBalls():
    assert hasattr(model::Over, "validBalls")
    descriptor = None
    for klass in model::Over.__mro__:
        if "validBalls" in klass.__dict__:
            descriptor = klass.__dict__["validBalls"]
            break
    assert isinstance(descriptor, property)

def test_model::over_has_runs():
    assert hasattr(model::Over, "runs")
    descriptor = None
    for klass in model::Over.__mro__:
        if "runs" in klass.__dict__:
            descriptor = klass.__dict__["runs"]
            break
    assert isinstance(descriptor, property)

def test_model::over_has_isComplete():
    assert hasattr(model::Over, "isComplete")
    descriptor = None
    for klass in model::Over.__mro__:
        if "isComplete" in klass.__dict__:
            descriptor = klass.__dict__["isComplete"]
            break
    assert isinstance(descriptor, property)

def test_model::over_has_BALLS_IN_OVER():
    assert hasattr(model::Over, "BALLS_IN_OVER")
    descriptor = None
    for klass in model::Over.__mro__:
        if "BALLS_IN_OVER" in klass.__dict__:
            descriptor = klass.__dict__["BALLS_IN_OVER"]
            break
    assert isinstance(descriptor, property)



def test_model::team_is_not_abstract():
    assert not inspect.isabstract(model::Team)


def test_model::team_constructor_exists():
    assert callable(model::Team.__init__)


def test_model::team_constructor_args():
    sig = inspect.signature(model::Team.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_model::team_has_name():
    assert hasattr(model::Team, "name")
    descriptor = None
    for klass in model::Team.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_model::innings_is_not_abstract():
    assert not inspect.isabstract(model::Innings)


def test_model::innings_constructor_exists():
    assert callable(model::Innings.__init__)


def test_model::innings_constructor_args():
    sig = inspect.signature(model::Innings.__init__)
    params = list(sig.parameters.keys())
    assert "total" in params, "Missing parameter 'total'"
    assert "overCount" in params, "Missing parameter 'overCount'"
    assert "Summary" in params, "Missing parameter 'Summary'"
    assert "noOvers" in params, "Missing parameter 'noOvers'"
    assert "wicketsDown" in params, "Missing parameter 'wicketsDown'"

def test_model::innings_has_total():
    assert hasattr(model::Innings, "total")
    descriptor = None
    for klass in model::Innings.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_model::innings_has_overCount():
    assert hasattr(model::Innings, "overCount")
    descriptor = None
    for klass in model::Innings.__mro__:
        if "overCount" in klass.__dict__:
            descriptor = klass.__dict__["overCount"]
            break
    assert isinstance(descriptor, property)

def test_model::innings_has_Summary():
    assert hasattr(model::Innings, "Summary")
    descriptor = None
    for klass in model::Innings.__mro__:
        if "Summary" in klass.__dict__:
            descriptor = klass.__dict__["Summary"]
            break
    assert isinstance(descriptor, property)

def test_model::innings_has_noOvers():
    assert hasattr(model::Innings, "noOvers")
    descriptor = None
    for klass in model::Innings.__mro__:
        if "noOvers" in klass.__dict__:
            descriptor = klass.__dict__["noOvers"]
            break
    assert isinstance(descriptor, property)

def test_model::innings_has_wicketsDown():
    assert hasattr(model::Innings, "wicketsDown")
    descriptor = None
    for klass in model::Innings.__mro__:
        if "wicketsDown" in klass.__dict__:
            descriptor = klass.__dict__["wicketsDown"]
            break
    assert isinstance(descriptor, property)

def test_howout_exists():
    # Check that the Enumeration exists
    assert HowOut is not None

def test_howout_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HowOut]
    expected_literals = [
        "Bowled",
        "Run_Out",
        "Stumped",
        "Lbw",
        "Caught",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HowOut"

def test_extratype_exists():
    # Check that the Enumeration exists
    assert ExtraType is not None

def test_extratype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ExtraType]
    expected_literals = [
        "Bye",
        "Wide",
        "NoBall",
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
        "one_run",
        "dot_ball",
        "three_runs",
        "six_runs",
        "two_runs",
        "four_runs",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BallType"


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
model::ExtraBall_strategy = st.builds(
    model::ExtraBall,
    extraType=
        safe_text,
    isValidBall=
        safe_text
)
model::WicketBall_strategy = st.builds(
    model::WicketBall,
    howOut=
        safe_text
)
model::Game_strategy = st.builds(
    model::Game,
    venue=
        safe_text,
    date=
        st.dates()
)
model::Ball_strategy = st.builds(
    model::Ball,
    runValue=
        st.integers(),
    runs=
        safe_text,
    switchEnds=
        safe_text
)
model::Player_strategy = st.builds(
    model::Player,
    name=
        safe_text,
    noOversBowled=
        safe_text,
    howOut=
        safe_text,
    noBallsFaced=
        st.integers(),
    runsScored=
        st.integers()
)
model::Over_strategy = st.builds(
    model::Over,
    validBalls=
        st.integers(),
    runs=
        st.integers(),
    isComplete=
        st.booleans(),
    BALLS_IN_OVER=
        st.integers()
)
model::Team_strategy = st.builds(
    model::Team,
    name=
        safe_text
)
model::Innings_strategy = st.builds(
    model::Innings,
    total=
        st.integers(),
    overCount=
        safe_text,
    Summary=
        safe_text,
    noOvers=
        st.integers(),
    wicketsDown=
        st.integers()
)

@given(instance=Ball_strategy)
@settings(max_examples=50)
def test_ball_instantiation(instance):
    assert isinstance(instance, Ball)

@given(instance=model::ExtraBall_strategy)
@settings(max_examples=50)
def test_model::extraball_instantiation(instance):
    assert isinstance(instance, model::ExtraBall)

@given(instance=model::ExtraBall_strategy)
def test_model::extraball_extraType_type(instance):
    assert isinstance(instance.extraType, str)


@given(instance=model::ExtraBall_strategy)
def test_model::extraball_extraType_setter(instance):
    original = instance.extraType
    instance.extraType = original
    assert instance.extraType == original

@given(instance=model::ExtraBall_strategy)
def test_model::extraball_isValidBall_type(instance):
    assert isinstance(instance.isValidBall, str)


@given(instance=model::ExtraBall_strategy)
def test_model::extraball_isValidBall_setter(instance):
    original = instance.isValidBall
    instance.isValidBall = original
    assert instance.isValidBall == original

@given(instance=model::WicketBall_strategy)
@settings(max_examples=50)
def test_model::wicketball_instantiation(instance):
    assert isinstance(instance, model::WicketBall)

@given(instance=model::WicketBall_strategy)
def test_model::wicketball_howOut_type(instance):
    assert isinstance(instance.howOut, str)


@given(instance=model::WicketBall_strategy)
def test_model::wicketball_howOut_setter(instance):
    original = instance.howOut
    instance.howOut = original
    assert instance.howOut == original

@given(instance=model::Game_strategy)
@settings(max_examples=50)
def test_model::game_instantiation(instance):
    assert isinstance(instance, model::Game)

@given(instance=model::Game_strategy)
def test_model::game_venue_type(instance):
    assert isinstance(instance.venue, str)


@given(instance=model::Game_strategy)
def test_model::game_venue_setter(instance):
    original = instance.venue
    instance.venue = original
    assert instance.venue == original

@given(instance=model::Game_strategy)
def test_model::game_date_type(instance):
    assert isinstance(instance.date, date)


@given(instance=model::Game_strategy)
def test_model::game_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=model::Ball_strategy)
@settings(max_examples=50)
def test_model::ball_instantiation(instance):
    assert isinstance(instance, model::Ball)

@given(instance=model::Ball_strategy)
def test_model::ball_runValue_type(instance):
    assert isinstance(instance.runValue, int)


@given(instance=model::Ball_strategy)
def test_model::ball_runValue_setter(instance):
    original = instance.runValue
    instance.runValue = original
    assert instance.runValue == original

@given(instance=model::Ball_strategy)
def test_model::ball_runs_type(instance):
    assert isinstance(instance.runs, str)


@given(instance=model::Ball_strategy)
def test_model::ball_runs_setter(instance):
    original = instance.runs
    instance.runs = original
    assert instance.runs == original

@given(instance=model::Ball_strategy)
def test_model::ball_switchEnds_type(instance):
    assert isinstance(instance.switchEnds, str)


@given(instance=model::Ball_strategy)
def test_model::ball_switchEnds_setter(instance):
    original = instance.switchEnds
    instance.switchEnds = original
    assert instance.switchEnds == original

@given(instance=model::Player_strategy)
@settings(max_examples=50)
def test_model::player_instantiation(instance):
    assert isinstance(instance, model::Player)

@given(instance=model::Player_strategy)
def test_model::player_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Player_strategy)
def test_model::player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Player_strategy)
def test_model::player_noOversBowled_type(instance):
    assert isinstance(instance.noOversBowled, str)


@given(instance=model::Player_strategy)
def test_model::player_noOversBowled_setter(instance):
    original = instance.noOversBowled
    instance.noOversBowled = original
    assert instance.noOversBowled == original

@given(instance=model::Player_strategy)
def test_model::player_howOut_type(instance):
    assert isinstance(instance.howOut, str)


@given(instance=model::Player_strategy)
def test_model::player_howOut_setter(instance):
    original = instance.howOut
    instance.howOut = original
    assert instance.howOut == original

@given(instance=model::Player_strategy)
def test_model::player_noBallsFaced_type(instance):
    assert isinstance(instance.noBallsFaced, int)


@given(instance=model::Player_strategy)
def test_model::player_noBallsFaced_setter(instance):
    original = instance.noBallsFaced
    instance.noBallsFaced = original
    assert instance.noBallsFaced == original

@given(instance=model::Player_strategy)
def test_model::player_runsScored_type(instance):
    assert isinstance(instance.runsScored, int)


@given(instance=model::Player_strategy)
def test_model::player_runsScored_setter(instance):
    original = instance.runsScored
    instance.runsScored = original
    assert instance.runsScored == original

@given(instance=model::Over_strategy)
@settings(max_examples=50)
def test_model::over_instantiation(instance):
    assert isinstance(instance, model::Over)

@given(instance=model::Over_strategy)
def test_model::over_validBalls_type(instance):
    assert isinstance(instance.validBalls, int)


@given(instance=model::Over_strategy)
def test_model::over_validBalls_setter(instance):
    original = instance.validBalls
    instance.validBalls = original
    assert instance.validBalls == original

@given(instance=model::Over_strategy)
def test_model::over_runs_type(instance):
    assert isinstance(instance.runs, int)


@given(instance=model::Over_strategy)
def test_model::over_runs_setter(instance):
    original = instance.runs
    instance.runs = original
    assert instance.runs == original

@given(instance=model::Over_strategy)
def test_model::over_isComplete_type(instance):
    assert isinstance(instance.isComplete, bool)


@given(instance=model::Over_strategy)
def test_model::over_isComplete_setter(instance):
    original = instance.isComplete
    instance.isComplete = original
    assert instance.isComplete == original

@given(instance=model::Over_strategy)
def test_model::over_BALLS_IN_OVER_type(instance):
    assert isinstance(instance.BALLS_IN_OVER, int)


@given(instance=model::Over_strategy)
def test_model::over_BALLS_IN_OVER_setter(instance):
    original = instance.BALLS_IN_OVER
    instance.BALLS_IN_OVER = original
    assert instance.BALLS_IN_OVER == original

@given(instance=model::Team_strategy)
@settings(max_examples=50)
def test_model::team_instantiation(instance):
    assert isinstance(instance, model::Team)

@given(instance=model::Team_strategy)
def test_model::team_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=model::Team_strategy)
def test_model::team_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=model::Innings_strategy)
@settings(max_examples=50)
def test_model::innings_instantiation(instance):
    assert isinstance(instance, model::Innings)

@given(instance=model::Innings_strategy)
def test_model::innings_total_type(instance):
    assert isinstance(instance.total, int)


@given(instance=model::Innings_strategy)
def test_model::innings_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original

@given(instance=model::Innings_strategy)
def test_model::innings_overCount_type(instance):
    assert isinstance(instance.overCount, str)


@given(instance=model::Innings_strategy)
def test_model::innings_overCount_setter(instance):
    original = instance.overCount
    instance.overCount = original
    assert instance.overCount == original

@given(instance=model::Innings_strategy)
def test_model::innings_Summary_type(instance):
    assert isinstance(instance.Summary, str)


@given(instance=model::Innings_strategy)
def test_model::innings_Summary_setter(instance):
    original = instance.Summary
    instance.Summary = original
    assert instance.Summary == original

@given(instance=model::Innings_strategy)
def test_model::innings_noOvers_type(instance):
    assert isinstance(instance.noOvers, int)


@given(instance=model::Innings_strategy)
def test_model::innings_noOvers_setter(instance):
    original = instance.noOvers
    instance.noOvers = original
    assert instance.noOvers == original

@given(instance=model::Innings_strategy)
def test_model::innings_wicketsDown_type(instance):
    assert isinstance(instance.wicketsDown, int)


@given(instance=model::Innings_strategy)
def test_model::innings_wicketsDown_setter(instance):
    original = instance.wicketsDown
    instance.wicketsDown = original
    assert instance.wicketsDown == original

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model::Innings_strategy)
@settings(max_examples=30)
def test_model::innings_newover_changes_state(instance):
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
        assert has_statements, f"Function 'newOver' in model::Innings is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'newOver' in model::Innings did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'newOver' in model::Innings is not implemented or raised an error")

import warnings
import copy
import inspect
import ast
from hypothesis import given, settings

@given(instance=model::Innings_strategy)
@settings(max_examples=30)
def test_model::innings_bowlball_changes_state(instance):
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
        assert has_statements, f"Function 'bowlBall' in model::Innings is empty"

        # Check for state change (WARN if no change)
        if instance.__dict__ == before.__dict__:
            warnings.warn(f"Operation 'bowlBall' in model::Innings did not change state; check implementation")

    except (AttributeError, NotImplementedError, TypeError):
        warnings.warn(f"Operation 'bowlBall' in model::Innings is not implemented or raised an error")
