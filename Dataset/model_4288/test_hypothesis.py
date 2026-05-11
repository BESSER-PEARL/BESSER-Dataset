import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    hockeyleague::HockeyleagueObject,
    hockeyleague::GoalieStats,
    hockeyleague::PlayerStats,
    Player,
    hockeyleague::Forward,
    hockeyleague::Goalie,
    hockeyleague::Defence,
    HockeyleagueObject,
    hockeyleague::Team,
    hockeyleague::League,
    hockeyleague::Player,
    hockeyleague::Arena,
    ForwardPositionKind,
    HeightKind,
    ShotKind,
    WeightKind,
    DefencePositionKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hockeyleague::hockeyleagueobject_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::HockeyleagueObject)


def test_hockeyleague::hockeyleagueobject_constructor_exists():
    assert callable(hockeyleague::HockeyleagueObject.__init__)


def test_hockeyleague::hockeyleagueobject_constructor_args():
    sig = inspect.signature(hockeyleague::HockeyleagueObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hockeyleague::hockeyleagueobject_has_name():
    assert hasattr(hockeyleague::HockeyleagueObject, "name")
    descriptor = None
    for klass in hockeyleague::HockeyleagueObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague::goaliestats_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::GoalieStats)


def test_hockeyleague::goaliestats_constructor_exists():
    assert callable(hockeyleague::GoalieStats.__init__)


def test_hockeyleague::goaliestats_constructor_args():
    sig = inspect.signature(hockeyleague::GoalieStats.__init__)
    params = list(sig.parameters.keys())
    assert "losses" in params, "Missing parameter 'losses'"
    assert "shutouts" in params, "Missing parameter 'shutouts'"
    assert "gamesPlayedIn" in params, "Missing parameter 'gamesPlayedIn'"
    assert "goals" in params, "Missing parameter 'goals'"
    assert "goalsAgainstAverage" in params, "Missing parameter 'goalsAgainstAverage'"
    assert "minutesPlayedIn" in params, "Missing parameter 'minutesPlayedIn'"
    assert "ties" in params, "Missing parameter 'ties'"
    assert "points" in params, "Missing parameter 'points'"
    assert "wins" in params, "Missing parameter 'wins'"
    assert "saves" in params, "Missing parameter 'saves'"
    assert "goalsAgainst" in params, "Missing parameter 'goalsAgainst'"
    assert "assists" in params, "Missing parameter 'assists'"
    assert "year" in params, "Missing parameter 'year'"
    assert "emptyNetGoals" in params, "Missing parameter 'emptyNetGoals'"
    assert "penaltyMinutes" in params, "Missing parameter 'penaltyMinutes'"

def test_hockeyleague::goaliestats_has_losses():
    assert hasattr(hockeyleague::GoalieStats, "losses")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "losses" in klass.__dict__:
            descriptor = klass.__dict__["losses"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_shutouts():
    assert hasattr(hockeyleague::GoalieStats, "shutouts")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "shutouts" in klass.__dict__:
            descriptor = klass.__dict__["shutouts"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_gamesPlayedIn():
    assert hasattr(hockeyleague::GoalieStats, "gamesPlayedIn")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "gamesPlayedIn" in klass.__dict__:
            descriptor = klass.__dict__["gamesPlayedIn"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_goals():
    assert hasattr(hockeyleague::GoalieStats, "goals")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "goals" in klass.__dict__:
            descriptor = klass.__dict__["goals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_goalsAgainstAverage():
    assert hasattr(hockeyleague::GoalieStats, "goalsAgainstAverage")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "goalsAgainstAverage" in klass.__dict__:
            descriptor = klass.__dict__["goalsAgainstAverage"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_minutesPlayedIn():
    assert hasattr(hockeyleague::GoalieStats, "minutesPlayedIn")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "minutesPlayedIn" in klass.__dict__:
            descriptor = klass.__dict__["minutesPlayedIn"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_ties():
    assert hasattr(hockeyleague::GoalieStats, "ties")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "ties" in klass.__dict__:
            descriptor = klass.__dict__["ties"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_points():
    assert hasattr(hockeyleague::GoalieStats, "points")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_wins():
    assert hasattr(hockeyleague::GoalieStats, "wins")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "wins" in klass.__dict__:
            descriptor = klass.__dict__["wins"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_saves():
    assert hasattr(hockeyleague::GoalieStats, "saves")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "saves" in klass.__dict__:
            descriptor = klass.__dict__["saves"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_goalsAgainst():
    assert hasattr(hockeyleague::GoalieStats, "goalsAgainst")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "goalsAgainst" in klass.__dict__:
            descriptor = klass.__dict__["goalsAgainst"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_assists():
    assert hasattr(hockeyleague::GoalieStats, "assists")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "assists" in klass.__dict__:
            descriptor = klass.__dict__["assists"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_year():
    assert hasattr(hockeyleague::GoalieStats, "year")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_emptyNetGoals():
    assert hasattr(hockeyleague::GoalieStats, "emptyNetGoals")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "emptyNetGoals" in klass.__dict__:
            descriptor = klass.__dict__["emptyNetGoals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::goaliestats_has_penaltyMinutes():
    assert hasattr(hockeyleague::GoalieStats, "penaltyMinutes")
    descriptor = None
    for klass in hockeyleague::GoalieStats.__mro__:
        if "penaltyMinutes" in klass.__dict__:
            descriptor = klass.__dict__["penaltyMinutes"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague::playerstats_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::PlayerStats)


def test_hockeyleague::playerstats_constructor_exists():
    assert callable(hockeyleague::PlayerStats.__init__)


def test_hockeyleague::playerstats_constructor_args():
    sig = inspect.signature(hockeyleague::PlayerStats.__init__)
    params = list(sig.parameters.keys())
    assert "gamesPlayedIn" in params, "Missing parameter 'gamesPlayedIn'"
    assert "gameWinningGoals" in params, "Missing parameter 'gameWinningGoals'"
    assert "penaltyMinutes" in params, "Missing parameter 'penaltyMinutes'"
    assert "assists" in params, "Missing parameter 'assists'"
    assert "goals" in params, "Missing parameter 'goals'"
    assert "shots" in params, "Missing parameter 'shots'"
    assert "points" in params, "Missing parameter 'points'"
    assert "shortHandedGoals" in params, "Missing parameter 'shortHandedGoals'"
    assert "shotPercentage" in params, "Missing parameter 'shotPercentage'"
    assert "year" in params, "Missing parameter 'year'"
    assert "powerPlayGoals" in params, "Missing parameter 'powerPlayGoals'"
    assert "plusMinus" in params, "Missing parameter 'plusMinus'"

def test_hockeyleague::playerstats_has_gamesPlayedIn():
    assert hasattr(hockeyleague::PlayerStats, "gamesPlayedIn")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "gamesPlayedIn" in klass.__dict__:
            descriptor = klass.__dict__["gamesPlayedIn"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_gameWinningGoals():
    assert hasattr(hockeyleague::PlayerStats, "gameWinningGoals")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "gameWinningGoals" in klass.__dict__:
            descriptor = klass.__dict__["gameWinningGoals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_penaltyMinutes():
    assert hasattr(hockeyleague::PlayerStats, "penaltyMinutes")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "penaltyMinutes" in klass.__dict__:
            descriptor = klass.__dict__["penaltyMinutes"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_assists():
    assert hasattr(hockeyleague::PlayerStats, "assists")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "assists" in klass.__dict__:
            descriptor = klass.__dict__["assists"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_goals():
    assert hasattr(hockeyleague::PlayerStats, "goals")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "goals" in klass.__dict__:
            descriptor = klass.__dict__["goals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_shots():
    assert hasattr(hockeyleague::PlayerStats, "shots")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "shots" in klass.__dict__:
            descriptor = klass.__dict__["shots"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_points():
    assert hasattr(hockeyleague::PlayerStats, "points")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_shortHandedGoals():
    assert hasattr(hockeyleague::PlayerStats, "shortHandedGoals")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "shortHandedGoals" in klass.__dict__:
            descriptor = klass.__dict__["shortHandedGoals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_shotPercentage():
    assert hasattr(hockeyleague::PlayerStats, "shotPercentage")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "shotPercentage" in klass.__dict__:
            descriptor = klass.__dict__["shotPercentage"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_year():
    assert hasattr(hockeyleague::PlayerStats, "year")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_powerPlayGoals():
    assert hasattr(hockeyleague::PlayerStats, "powerPlayGoals")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "powerPlayGoals" in klass.__dict__:
            descriptor = klass.__dict__["powerPlayGoals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::playerstats_has_plusMinus():
    assert hasattr(hockeyleague::PlayerStats, "plusMinus")
    descriptor = None
    for klass in hockeyleague::PlayerStats.__mro__:
        if "plusMinus" in klass.__dict__:
            descriptor = klass.__dict__["plusMinus"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_hockeyleague::forward_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::Forward)


def test_hockeyleague::forward_constructor_exists():
    assert callable(hockeyleague::Forward.__init__)


def test_hockeyleague::forward_constructor_args():
    sig = inspect.signature(hockeyleague::Forward.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_hockeyleague::forward_has_position():
    assert hasattr(hockeyleague::Forward, "position")
    descriptor = None
    for klass in hockeyleague::Forward.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague::goalie_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::Goalie)


def test_hockeyleague::goalie_constructor_exists():
    assert callable(hockeyleague::Goalie.__init__)


def test_hockeyleague::goalie_constructor_args():
    sig = inspect.signature(hockeyleague::Goalie.__init__)
    params = list(sig.parameters.keys())



def test_hockeyleague::defence_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::Defence)


def test_hockeyleague::defence_constructor_exists():
    assert callable(hockeyleague::Defence.__init__)


def test_hockeyleague::defence_constructor_args():
    sig = inspect.signature(hockeyleague::Defence.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_hockeyleague::defence_has_position():
    assert hasattr(hockeyleague::Defence, "position")
    descriptor = None
    for klass in hockeyleague::Defence.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleagueobject_is_not_abstract():
    assert not inspect.isabstract(HockeyleagueObject)


def test_hockeyleagueobject_constructor_exists():
    assert callable(HockeyleagueObject.__init__)


def test_hockeyleagueobject_constructor_args():
    sig = inspect.signature(HockeyleagueObject.__init__)
    params = list(sig.parameters.keys())



def test_hockeyleague::team_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::Team)


def test_hockeyleague::team_constructor_exists():
    assert callable(hockeyleague::Team.__init__)


def test_hockeyleague::team_constructor_args():
    sig = inspect.signature(hockeyleague::Team.__init__)
    params = list(sig.parameters.keys())



def test_hockeyleague::league_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::League)


def test_hockeyleague::league_constructor_exists():
    assert callable(hockeyleague::League.__init__)


def test_hockeyleague::league_constructor_args():
    sig = inspect.signature(hockeyleague::League.__init__)
    params = list(sig.parameters.keys())
    assert "headoffice" in params, "Missing parameter 'headoffice'"

def test_hockeyleague::league_has_headoffice():
    assert hasattr(hockeyleague::League, "headoffice")
    descriptor = None
    for klass in hockeyleague::League.__mro__:
        if "headoffice" in klass.__dict__:
            descriptor = klass.__dict__["headoffice"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague::player_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::Player)


def test_hockeyleague::player_constructor_exists():
    assert callable(hockeyleague::Player.__init__)


def test_hockeyleague::player_constructor_args():
    sig = inspect.signature(hockeyleague::Player.__init__)
    params = list(sig.parameters.keys())
    assert "heightValue" in params, "Missing parameter 'heightValue'"
    assert "heightMesurement" in params, "Missing parameter 'heightMesurement'"
    assert "weightValue" in params, "Missing parameter 'weightValue'"
    assert "weightMesurement" in params, "Missing parameter 'weightMesurement'"
    assert "birthplace" in params, "Missing parameter 'birthplace'"
    assert "number" in params, "Missing parameter 'number'"
    assert "shot" in params, "Missing parameter 'shot'"
    assert "birthdate" in params, "Missing parameter 'birthdate'"

def test_hockeyleague::player_has_heightValue():
    assert hasattr(hockeyleague::Player, "heightValue")
    descriptor = None
    for klass in hockeyleague::Player.__mro__:
        if "heightValue" in klass.__dict__:
            descriptor = klass.__dict__["heightValue"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::player_has_heightMesurement():
    assert hasattr(hockeyleague::Player, "heightMesurement")
    descriptor = None
    for klass in hockeyleague::Player.__mro__:
        if "heightMesurement" in klass.__dict__:
            descriptor = klass.__dict__["heightMesurement"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::player_has_weightValue():
    assert hasattr(hockeyleague::Player, "weightValue")
    descriptor = None
    for klass in hockeyleague::Player.__mro__:
        if "weightValue" in klass.__dict__:
            descriptor = klass.__dict__["weightValue"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::player_has_weightMesurement():
    assert hasattr(hockeyleague::Player, "weightMesurement")
    descriptor = None
    for klass in hockeyleague::Player.__mro__:
        if "weightMesurement" in klass.__dict__:
            descriptor = klass.__dict__["weightMesurement"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::player_has_birthplace():
    assert hasattr(hockeyleague::Player, "birthplace")
    descriptor = None
    for klass in hockeyleague::Player.__mro__:
        if "birthplace" in klass.__dict__:
            descriptor = klass.__dict__["birthplace"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::player_has_number():
    assert hasattr(hockeyleague::Player, "number")
    descriptor = None
    for klass in hockeyleague::Player.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::player_has_shot():
    assert hasattr(hockeyleague::Player, "shot")
    descriptor = None
    for klass in hockeyleague::Player.__mro__:
        if "shot" in klass.__dict__:
            descriptor = klass.__dict__["shot"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::player_has_birthdate():
    assert hasattr(hockeyleague::Player, "birthdate")
    descriptor = None
    for klass in hockeyleague::Player.__mro__:
        if "birthdate" in klass.__dict__:
            descriptor = klass.__dict__["birthdate"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague::arena_is_not_abstract():
    assert not inspect.isabstract(hockeyleague::Arena)


def test_hockeyleague::arena_constructor_exists():
    assert callable(hockeyleague::Arena.__init__)


def test_hockeyleague::arena_constructor_args():
    sig = inspect.signature(hockeyleague::Arena.__init__)
    params = list(sig.parameters.keys())
    assert "capacity" in params, "Missing parameter 'capacity'"
    assert "address" in params, "Missing parameter 'address'"

def test_hockeyleague::arena_has_capacity():
    assert hasattr(hockeyleague::Arena, "capacity")
    descriptor = None
    for klass in hockeyleague::Arena.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague::arena_has_address():
    assert hasattr(hockeyleague::Arena, "address")
    descriptor = None
    for klass in hockeyleague::Arena.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_forwardpositionkind_exists():
    # Check that the Enumeration exists
    assert ForwardPositionKind is not None

def test_forwardpositionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ForwardPositionKind]
    expected_literals = [
        "center",
        "right_wing",
        "left_wing",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ForwardPositionKind"

def test_heightkind_exists():
    # Check that the Enumeration exists
    assert HeightKind is not None

def test_heightkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HeightKind]
    expected_literals = [
        "centimeters",
        "inches",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HeightKind"

def test_shotkind_exists():
    # Check that the Enumeration exists
    assert ShotKind is not None

def test_shotkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ShotKind]
    expected_literals = [
        "right",
        "left",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ShotKind"

def test_weightkind_exists():
    # Check that the Enumeration exists
    assert WeightKind is not None

def test_weightkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in WeightKind]
    expected_literals = [
        "pounds",
        "kilograms",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in WeightKind"

def test_defencepositionkind_exists():
    # Check that the Enumeration exists
    assert DefencePositionKind is not None

def test_defencepositionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefencePositionKind]
    expected_literals = [
        "left_defence",
        "right_defence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefencePositionKind"


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
hockeyleague::HockeyleagueObject_strategy = st.builds(
    hockeyleague::HockeyleagueObject,
    name=
        safe_text
)
hockeyleague::GoalieStats_strategy = st.builds(
    hockeyleague::GoalieStats,
    losses=
        st.integers(),
    shutouts=
        st.integers(),
    gamesPlayedIn=
        st.integers(),
    goals=
        st.integers(),
    goalsAgainstAverage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    minutesPlayedIn=
        st.integers(),
    ties=
        st.integers(),
    points=
        st.integers(),
    wins=
        st.integers(),
    saves=
        st.integers(),
    goalsAgainst=
        st.integers(),
    assists=
        st.integers(),
    year=
        safe_text,
    emptyNetGoals=
        st.integers(),
    penaltyMinutes=
        st.integers()
)
hockeyleague::PlayerStats_strategy = st.builds(
    hockeyleague::PlayerStats,
    gamesPlayedIn=
        st.integers(),
    gameWinningGoals=
        st.integers(),
    penaltyMinutes=
        st.integers(),
    assists=
        st.integers(),
    goals=
        st.integers(),
    shots=
        st.integers(),
    points=
        st.integers(),
    shortHandedGoals=
        st.integers(),
    shotPercentage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    year=
        safe_text,
    powerPlayGoals=
        st.integers(),
    plusMinus=
        st.integers()
)
Player_strategy = st.builds(
    Player,
)
hockeyleague::Forward_strategy = st.builds(
    hockeyleague::Forward,
    position=
        safe_text
)
hockeyleague::Goalie_strategy = st.builds(
    hockeyleague::Goalie,
)
hockeyleague::Defence_strategy = st.builds(
    hockeyleague::Defence,
    position=
        safe_text
)
HockeyleagueObject_strategy = st.builds(
    HockeyleagueObject,
)
hockeyleague::Team_strategy = st.builds(
    hockeyleague::Team,
)
hockeyleague::League_strategy = st.builds(
    hockeyleague::League,
    headoffice=
        safe_text
)
hockeyleague::Player_strategy = st.builds(
    hockeyleague::Player,
    heightValue=
        st.integers(),
    heightMesurement=
        safe_text,
    weightValue=
        st.integers(),
    weightMesurement=
        safe_text,
    birthplace=
        safe_text,
    number=
        st.integers(),
    shot=
        safe_text,
    birthdate=
        safe_text
)
hockeyleague::Arena_strategy = st.builds(
    hockeyleague::Arena,
    capacity=
        st.integers(),
    address=
        safe_text
)

@given(instance=hockeyleague::HockeyleagueObject_strategy)
@settings(max_examples=50)
def test_hockeyleague::hockeyleagueobject_instantiation(instance):
    assert isinstance(instance, hockeyleague::HockeyleagueObject)

@given(instance=hockeyleague::HockeyleagueObject_strategy)
def test_hockeyleague::hockeyleagueobject_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=hockeyleague::HockeyleagueObject_strategy)
def test_hockeyleague::hockeyleagueobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hockeyleague::GoalieStats_strategy)
@settings(max_examples=50)
def test_hockeyleague::goaliestats_instantiation(instance):
    assert isinstance(instance, hockeyleague::GoalieStats)

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_losses_type(instance):
    assert isinstance(instance.losses, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_losses_setter(instance):
    original = instance.losses
    instance.losses = original
    assert instance.losses == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_shutouts_type(instance):
    assert isinstance(instance.shutouts, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_shutouts_setter(instance):
    original = instance.shutouts
    instance.shutouts = original
    assert instance.shutouts == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_gamesPlayedIn_type(instance):
    assert isinstance(instance.gamesPlayedIn, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_gamesPlayedIn_setter(instance):
    original = instance.gamesPlayedIn
    instance.gamesPlayedIn = original
    assert instance.gamesPlayedIn == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_goals_type(instance):
    assert isinstance(instance.goals, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_goals_setter(instance):
    original = instance.goals
    instance.goals = original
    assert instance.goals == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_goalsAgainstAverage_type(instance):
    assert isinstance(instance.goalsAgainstAverage, float)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_goalsAgainstAverage_setter(instance):
    original = instance.goalsAgainstAverage
    instance.goalsAgainstAverage = original
    assert instance.goalsAgainstAverage == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_minutesPlayedIn_type(instance):
    assert isinstance(instance.minutesPlayedIn, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_minutesPlayedIn_setter(instance):
    original = instance.minutesPlayedIn
    instance.minutesPlayedIn = original
    assert instance.minutesPlayedIn == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_ties_type(instance):
    assert isinstance(instance.ties, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_ties_setter(instance):
    original = instance.ties
    instance.ties = original
    assert instance.ties == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_points_type(instance):
    assert isinstance(instance.points, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_wins_type(instance):
    assert isinstance(instance.wins, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_wins_setter(instance):
    original = instance.wins
    instance.wins = original
    assert instance.wins == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_saves_type(instance):
    assert isinstance(instance.saves, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_saves_setter(instance):
    original = instance.saves
    instance.saves = original
    assert instance.saves == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_goalsAgainst_type(instance):
    assert isinstance(instance.goalsAgainst, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_goalsAgainst_setter(instance):
    original = instance.goalsAgainst
    instance.goalsAgainst = original
    assert instance.goalsAgainst == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_assists_type(instance):
    assert isinstance(instance.assists, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_assists_setter(instance):
    original = instance.assists
    instance.assists = original
    assert instance.assists == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_emptyNetGoals_type(instance):
    assert isinstance(instance.emptyNetGoals, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_emptyNetGoals_setter(instance):
    original = instance.emptyNetGoals
    instance.emptyNetGoals = original
    assert instance.emptyNetGoals == original

@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_penaltyMinutes_type(instance):
    assert isinstance(instance.penaltyMinutes, int)


@given(instance=hockeyleague::GoalieStats_strategy)
def test_hockeyleague::goaliestats_penaltyMinutes_setter(instance):
    original = instance.penaltyMinutes
    instance.penaltyMinutes = original
    assert instance.penaltyMinutes == original

@given(instance=hockeyleague::PlayerStats_strategy)
@settings(max_examples=50)
def test_hockeyleague::playerstats_instantiation(instance):
    assert isinstance(instance, hockeyleague::PlayerStats)

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_gamesPlayedIn_type(instance):
    assert isinstance(instance.gamesPlayedIn, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_gamesPlayedIn_setter(instance):
    original = instance.gamesPlayedIn
    instance.gamesPlayedIn = original
    assert instance.gamesPlayedIn == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_gameWinningGoals_type(instance):
    assert isinstance(instance.gameWinningGoals, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_gameWinningGoals_setter(instance):
    original = instance.gameWinningGoals
    instance.gameWinningGoals = original
    assert instance.gameWinningGoals == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_penaltyMinutes_type(instance):
    assert isinstance(instance.penaltyMinutes, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_penaltyMinutes_setter(instance):
    original = instance.penaltyMinutes
    instance.penaltyMinutes = original
    assert instance.penaltyMinutes == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_assists_type(instance):
    assert isinstance(instance.assists, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_assists_setter(instance):
    original = instance.assists
    instance.assists = original
    assert instance.assists == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_goals_type(instance):
    assert isinstance(instance.goals, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_goals_setter(instance):
    original = instance.goals
    instance.goals = original
    assert instance.goals == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_shots_type(instance):
    assert isinstance(instance.shots, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_shots_setter(instance):
    original = instance.shots
    instance.shots = original
    assert instance.shots == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_points_type(instance):
    assert isinstance(instance.points, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_shortHandedGoals_type(instance):
    assert isinstance(instance.shortHandedGoals, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_shortHandedGoals_setter(instance):
    original = instance.shortHandedGoals
    instance.shortHandedGoals = original
    assert instance.shortHandedGoals == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_shotPercentage_type(instance):
    assert isinstance(instance.shotPercentage, float)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_shotPercentage_setter(instance):
    original = instance.shotPercentage
    instance.shotPercentage = original
    assert instance.shotPercentage == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_powerPlayGoals_type(instance):
    assert isinstance(instance.powerPlayGoals, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_powerPlayGoals_setter(instance):
    original = instance.powerPlayGoals
    instance.powerPlayGoals = original
    assert instance.powerPlayGoals == original

@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_plusMinus_type(instance):
    assert isinstance(instance.plusMinus, int)


@given(instance=hockeyleague::PlayerStats_strategy)
def test_hockeyleague::playerstats_plusMinus_setter(instance):
    original = instance.plusMinus
    instance.plusMinus = original
    assert instance.plusMinus == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=hockeyleague::Forward_strategy)
@settings(max_examples=50)
def test_hockeyleague::forward_instantiation(instance):
    assert isinstance(instance, hockeyleague::Forward)

@given(instance=hockeyleague::Forward_strategy)
def test_hockeyleague::forward_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=hockeyleague::Forward_strategy)
def test_hockeyleague::forward_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=hockeyleague::Goalie_strategy)
@settings(max_examples=50)
def test_hockeyleague::goalie_instantiation(instance):
    assert isinstance(instance, hockeyleague::Goalie)

@given(instance=hockeyleague::Defence_strategy)
@settings(max_examples=50)
def test_hockeyleague::defence_instantiation(instance):
    assert isinstance(instance, hockeyleague::Defence)

@given(instance=hockeyleague::Defence_strategy)
def test_hockeyleague::defence_position_type(instance):
    assert isinstance(instance.position, str)


@given(instance=hockeyleague::Defence_strategy)
def test_hockeyleague::defence_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=HockeyleagueObject_strategy)
@settings(max_examples=50)
def test_hockeyleagueobject_instantiation(instance):
    assert isinstance(instance, HockeyleagueObject)

@given(instance=hockeyleague::Team_strategy)
@settings(max_examples=50)
def test_hockeyleague::team_instantiation(instance):
    assert isinstance(instance, hockeyleague::Team)

@given(instance=hockeyleague::League_strategy)
@settings(max_examples=50)
def test_hockeyleague::league_instantiation(instance):
    assert isinstance(instance, hockeyleague::League)

@given(instance=hockeyleague::League_strategy)
def test_hockeyleague::league_headoffice_type(instance):
    assert isinstance(instance.headoffice, str)


@given(instance=hockeyleague::League_strategy)
def test_hockeyleague::league_headoffice_setter(instance):
    original = instance.headoffice
    instance.headoffice = original
    assert instance.headoffice == original

@given(instance=hockeyleague::Player_strategy)
@settings(max_examples=50)
def test_hockeyleague::player_instantiation(instance):
    assert isinstance(instance, hockeyleague::Player)

@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_heightValue_type(instance):
    assert isinstance(instance.heightValue, int)


@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_heightValue_setter(instance):
    original = instance.heightValue
    instance.heightValue = original
    assert instance.heightValue == original

@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_heightMesurement_type(instance):
    assert isinstance(instance.heightMesurement, str)


@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_heightMesurement_setter(instance):
    original = instance.heightMesurement
    instance.heightMesurement = original
    assert instance.heightMesurement == original

@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_weightValue_type(instance):
    assert isinstance(instance.weightValue, int)


@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_weightValue_setter(instance):
    original = instance.weightValue
    instance.weightValue = original
    assert instance.weightValue == original

@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_weightMesurement_type(instance):
    assert isinstance(instance.weightMesurement, str)


@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_weightMesurement_setter(instance):
    original = instance.weightMesurement
    instance.weightMesurement = original
    assert instance.weightMesurement == original

@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_birthplace_type(instance):
    assert isinstance(instance.birthplace, str)


@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_birthplace_setter(instance):
    original = instance.birthplace
    instance.birthplace = original
    assert instance.birthplace == original

@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_number_type(instance):
    assert isinstance(instance.number, int)


@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_shot_type(instance):
    assert isinstance(instance.shot, str)


@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_shot_setter(instance):
    original = instance.shot
    instance.shot = original
    assert instance.shot == original

@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_birthdate_type(instance):
    assert isinstance(instance.birthdate, str)


@given(instance=hockeyleague::Player_strategy)
def test_hockeyleague::player_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original

@given(instance=hockeyleague::Arena_strategy)
@settings(max_examples=50)
def test_hockeyleague::arena_instantiation(instance):
    assert isinstance(instance, hockeyleague::Arena)

@given(instance=hockeyleague::Arena_strategy)
def test_hockeyleague::arena_capacity_type(instance):
    assert isinstance(instance.capacity, int)


@given(instance=hockeyleague::Arena_strategy)
def test_hockeyleague::arena_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original

@given(instance=hockeyleague::Arena_strategy)
def test_hockeyleague::arena_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=hockeyleague::Arena_strategy)
def test_hockeyleague::arena_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original
