import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    hockeyleague_HockeyleagueObject,
    hockeyleague_GoalieStats,
    hockeyleague_PlayerStats,
    Player,
    hockeyleague_Forward,
    hockeyleague_Goalie,
    hockeyleague_Defence,
    HockeyleagueObject,
    hockeyleague_Team,
    hockeyleague_Player,
    hockeyleague_League,
    hockeyleague_Arena,
    HeightKind,
    ForwardPositionKind,
    DefencePositionKind,
    WeightKind,
    ShotKind,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hockeyleague_hockeyleagueobject_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_HockeyleagueObject)


def test_hockeyleague_hockeyleagueobject_constructor_exists():
    assert callable(hockeyleague_HockeyleagueObject.__init__)


def test_hockeyleague_hockeyleagueobject_constructor_args():
    sig = inspect.signature(hockeyleague_HockeyleagueObject.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_hockeyleague_hockeyleagueobject_has_name():
    assert hasattr(hockeyleague_HockeyleagueObject, "name")
    descriptor = None
    for klass in hockeyleague_HockeyleagueObject.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague_goaliestats_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_GoalieStats)


def test_hockeyleague_goaliestats_constructor_exists():
    assert callable(hockeyleague_GoalieStats.__init__)


def test_hockeyleague_goaliestats_constructor_args():
    sig = inspect.signature(hockeyleague_GoalieStats.__init__)
    params = list(sig.parameters.keys())
    assert "goalsAgainstAverage" in params, "Missing parameter 'goalsAgainstAverage'"
    assert "assists" in params, "Missing parameter 'assists'"
    assert "emptyNetGoals" in params, "Missing parameter 'emptyNetGoals'"
    assert "year" in params, "Missing parameter 'year'"
    assert "gamesPlayedIn" in params, "Missing parameter 'gamesPlayedIn'"
    assert "ties" in params, "Missing parameter 'ties'"
    assert "goalsAgainst" in params, "Missing parameter 'goalsAgainst'"
    assert "minutesPlayedIn" in params, "Missing parameter 'minutesPlayedIn'"
    assert "shutouts" in params, "Missing parameter 'shutouts'"
    assert "points" in params, "Missing parameter 'points'"
    assert "penaltyMinutes" in params, "Missing parameter 'penaltyMinutes'"
    assert "saves" in params, "Missing parameter 'saves'"
    assert "losses" in params, "Missing parameter 'losses'"
    assert "wins" in params, "Missing parameter 'wins'"
    assert "goals" in params, "Missing parameter 'goals'"

def test_hockeyleague_goaliestats_has_goalsAgainstAverage():
    assert hasattr(hockeyleague_GoalieStats, "goalsAgainstAverage")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "goalsAgainstAverage" in klass.__dict__:
            descriptor = klass.__dict__["goalsAgainstAverage"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_assists():
    assert hasattr(hockeyleague_GoalieStats, "assists")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "assists" in klass.__dict__:
            descriptor = klass.__dict__["assists"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_emptyNetGoals():
    assert hasattr(hockeyleague_GoalieStats, "emptyNetGoals")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "emptyNetGoals" in klass.__dict__:
            descriptor = klass.__dict__["emptyNetGoals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_year():
    assert hasattr(hockeyleague_GoalieStats, "year")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_gamesPlayedIn():
    assert hasattr(hockeyleague_GoalieStats, "gamesPlayedIn")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "gamesPlayedIn" in klass.__dict__:
            descriptor = klass.__dict__["gamesPlayedIn"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_ties():
    assert hasattr(hockeyleague_GoalieStats, "ties")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "ties" in klass.__dict__:
            descriptor = klass.__dict__["ties"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_goalsAgainst():
    assert hasattr(hockeyleague_GoalieStats, "goalsAgainst")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "goalsAgainst" in klass.__dict__:
            descriptor = klass.__dict__["goalsAgainst"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_minutesPlayedIn():
    assert hasattr(hockeyleague_GoalieStats, "minutesPlayedIn")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "minutesPlayedIn" in klass.__dict__:
            descriptor = klass.__dict__["minutesPlayedIn"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_shutouts():
    assert hasattr(hockeyleague_GoalieStats, "shutouts")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "shutouts" in klass.__dict__:
            descriptor = klass.__dict__["shutouts"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_points():
    assert hasattr(hockeyleague_GoalieStats, "points")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_penaltyMinutes():
    assert hasattr(hockeyleague_GoalieStats, "penaltyMinutes")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "penaltyMinutes" in klass.__dict__:
            descriptor = klass.__dict__["penaltyMinutes"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_saves():
    assert hasattr(hockeyleague_GoalieStats, "saves")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "saves" in klass.__dict__:
            descriptor = klass.__dict__["saves"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_losses():
    assert hasattr(hockeyleague_GoalieStats, "losses")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "losses" in klass.__dict__:
            descriptor = klass.__dict__["losses"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_wins():
    assert hasattr(hockeyleague_GoalieStats, "wins")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "wins" in klass.__dict__:
            descriptor = klass.__dict__["wins"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_goaliestats_has_goals():
    assert hasattr(hockeyleague_GoalieStats, "goals")
    descriptor = None
    for klass in hockeyleague_GoalieStats.__mro__:
        if "goals" in klass.__dict__:
            descriptor = klass.__dict__["goals"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague_playerstats_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_PlayerStats)


def test_hockeyleague_playerstats_constructor_exists():
    assert callable(hockeyleague_PlayerStats.__init__)


def test_hockeyleague_playerstats_constructor_args():
    sig = inspect.signature(hockeyleague_PlayerStats.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "year" in params, "Missing parameter 'year'"
    assert "powerPlayGoals" in params, "Missing parameter 'powerPlayGoals'"
    assert "gamesPlayedIn" in params, "Missing parameter 'gamesPlayedIn'"
    assert "goals" in params, "Missing parameter 'goals'"
    assert "gameWinningGoals" in params, "Missing parameter 'gameWinningGoals'"
    assert "plusMinus" in params, "Missing parameter 'plusMinus'"
    assert "penaltyMinutes" in params, "Missing parameter 'penaltyMinutes'"
    assert "assists" in params, "Missing parameter 'assists'"
    assert "shots" in params, "Missing parameter 'shots'"
    assert "shortHandedGoals" in params, "Missing parameter 'shortHandedGoals'"
    assert "shotPercentage" in params, "Missing parameter 'shotPercentage'"

def test_hockeyleague_playerstats_has_points():
    assert hasattr(hockeyleague_PlayerStats, "points")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_year():
    assert hasattr(hockeyleague_PlayerStats, "year")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_powerPlayGoals():
    assert hasattr(hockeyleague_PlayerStats, "powerPlayGoals")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "powerPlayGoals" in klass.__dict__:
            descriptor = klass.__dict__["powerPlayGoals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_gamesPlayedIn():
    assert hasattr(hockeyleague_PlayerStats, "gamesPlayedIn")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "gamesPlayedIn" in klass.__dict__:
            descriptor = klass.__dict__["gamesPlayedIn"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_goals():
    assert hasattr(hockeyleague_PlayerStats, "goals")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "goals" in klass.__dict__:
            descriptor = klass.__dict__["goals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_gameWinningGoals():
    assert hasattr(hockeyleague_PlayerStats, "gameWinningGoals")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "gameWinningGoals" in klass.__dict__:
            descriptor = klass.__dict__["gameWinningGoals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_plusMinus():
    assert hasattr(hockeyleague_PlayerStats, "plusMinus")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "plusMinus" in klass.__dict__:
            descriptor = klass.__dict__["plusMinus"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_penaltyMinutes():
    assert hasattr(hockeyleague_PlayerStats, "penaltyMinutes")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "penaltyMinutes" in klass.__dict__:
            descriptor = klass.__dict__["penaltyMinutes"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_assists():
    assert hasattr(hockeyleague_PlayerStats, "assists")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "assists" in klass.__dict__:
            descriptor = klass.__dict__["assists"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_shots():
    assert hasattr(hockeyleague_PlayerStats, "shots")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "shots" in klass.__dict__:
            descriptor = klass.__dict__["shots"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_shortHandedGoals():
    assert hasattr(hockeyleague_PlayerStats, "shortHandedGoals")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "shortHandedGoals" in klass.__dict__:
            descriptor = klass.__dict__["shortHandedGoals"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_playerstats_has_shotPercentage():
    assert hasattr(hockeyleague_PlayerStats, "shotPercentage")
    descriptor = None
    for klass in hockeyleague_PlayerStats.__mro__:
        if "shotPercentage" in klass.__dict__:
            descriptor = klass.__dict__["shotPercentage"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_hockeyleague_forward_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_Forward)


def test_hockeyleague_forward_constructor_exists():
    assert callable(hockeyleague_Forward.__init__)


def test_hockeyleague_forward_constructor_args():
    sig = inspect.signature(hockeyleague_Forward.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_hockeyleague_forward_has_position():
    assert hasattr(hockeyleague_Forward, "position")
    descriptor = None
    for klass in hockeyleague_Forward.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague_goalie_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_Goalie)


def test_hockeyleague_goalie_constructor_exists():
    assert callable(hockeyleague_Goalie.__init__)


def test_hockeyleague_goalie_constructor_args():
    sig = inspect.signature(hockeyleague_Goalie.__init__)
    params = list(sig.parameters.keys())



def test_hockeyleague_defence_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_Defence)


def test_hockeyleague_defence_constructor_exists():
    assert callable(hockeyleague_Defence.__init__)


def test_hockeyleague_defence_constructor_args():
    sig = inspect.signature(hockeyleague_Defence.__init__)
    params = list(sig.parameters.keys())
    assert "position" in params, "Missing parameter 'position'"

def test_hockeyleague_defence_has_position():
    assert hasattr(hockeyleague_Defence, "position")
    descriptor = None
    for klass in hockeyleague_Defence.__mro__:
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



def test_hockeyleague_team_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_Team)


def test_hockeyleague_team_constructor_exists():
    assert callable(hockeyleague_Team.__init__)


def test_hockeyleague_team_constructor_args():
    sig = inspect.signature(hockeyleague_Team.__init__)
    params = list(sig.parameters.keys())



def test_hockeyleague_player_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_Player)


def test_hockeyleague_player_constructor_exists():
    assert callable(hockeyleague_Player.__init__)


def test_hockeyleague_player_constructor_args():
    sig = inspect.signature(hockeyleague_Player.__init__)
    params = list(sig.parameters.keys())
    assert "weightValue" in params, "Missing parameter 'weightValue'"
    assert "shot" in params, "Missing parameter 'shot'"
    assert "birthplace" in params, "Missing parameter 'birthplace'"
    assert "birthdate" in params, "Missing parameter 'birthdate'"
    assert "heightValue" in params, "Missing parameter 'heightValue'"
    assert "number" in params, "Missing parameter 'number'"
    assert "weightMesurement" in params, "Missing parameter 'weightMesurement'"
    assert "heightMesurement" in params, "Missing parameter 'heightMesurement'"

def test_hockeyleague_player_has_weightValue():
    assert hasattr(hockeyleague_Player, "weightValue")
    descriptor = None
    for klass in hockeyleague_Player.__mro__:
        if "weightValue" in klass.__dict__:
            descriptor = klass.__dict__["weightValue"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_player_has_shot():
    assert hasattr(hockeyleague_Player, "shot")
    descriptor = None
    for klass in hockeyleague_Player.__mro__:
        if "shot" in klass.__dict__:
            descriptor = klass.__dict__["shot"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_player_has_birthplace():
    assert hasattr(hockeyleague_Player, "birthplace")
    descriptor = None
    for klass in hockeyleague_Player.__mro__:
        if "birthplace" in klass.__dict__:
            descriptor = klass.__dict__["birthplace"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_player_has_birthdate():
    assert hasattr(hockeyleague_Player, "birthdate")
    descriptor = None
    for klass in hockeyleague_Player.__mro__:
        if "birthdate" in klass.__dict__:
            descriptor = klass.__dict__["birthdate"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_player_has_heightValue():
    assert hasattr(hockeyleague_Player, "heightValue")
    descriptor = None
    for klass in hockeyleague_Player.__mro__:
        if "heightValue" in klass.__dict__:
            descriptor = klass.__dict__["heightValue"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_player_has_number():
    assert hasattr(hockeyleague_Player, "number")
    descriptor = None
    for klass in hockeyleague_Player.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_player_has_weightMesurement():
    assert hasattr(hockeyleague_Player, "weightMesurement")
    descriptor = None
    for klass in hockeyleague_Player.__mro__:
        if "weightMesurement" in klass.__dict__:
            descriptor = klass.__dict__["weightMesurement"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_player_has_heightMesurement():
    assert hasattr(hockeyleague_Player, "heightMesurement")
    descriptor = None
    for klass in hockeyleague_Player.__mro__:
        if "heightMesurement" in klass.__dict__:
            descriptor = klass.__dict__["heightMesurement"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague_league_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_League)


def test_hockeyleague_league_constructor_exists():
    assert callable(hockeyleague_League.__init__)


def test_hockeyleague_league_constructor_args():
    sig = inspect.signature(hockeyleague_League.__init__)
    params = list(sig.parameters.keys())
    assert "headoffice" in params, "Missing parameter 'headoffice'"

def test_hockeyleague_league_has_headoffice():
    assert hasattr(hockeyleague_League, "headoffice")
    descriptor = None
    for klass in hockeyleague_League.__mro__:
        if "headoffice" in klass.__dict__:
            descriptor = klass.__dict__["headoffice"]
            break
    assert isinstance(descriptor, property)



def test_hockeyleague_arena_is_not_abstract():
    assert not inspect.isabstract(hockeyleague_Arena)


def test_hockeyleague_arena_constructor_exists():
    assert callable(hockeyleague_Arena.__init__)


def test_hockeyleague_arena_constructor_args():
    sig = inspect.signature(hockeyleague_Arena.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "capacity" in params, "Missing parameter 'capacity'"

def test_hockeyleague_arena_has_address():
    assert hasattr(hockeyleague_Arena, "address")
    descriptor = None
    for klass in hockeyleague_Arena.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_hockeyleague_arena_has_capacity():
    assert hasattr(hockeyleague_Arena, "capacity")
    descriptor = None
    for klass in hockeyleague_Arena.__mro__:
        if "capacity" in klass.__dict__:
            descriptor = klass.__dict__["capacity"]
            break
    assert isinstance(descriptor, property)

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

def test_forwardpositionkind_exists():
    # Check that the Enumeration exists
    assert ForwardPositionKind is not None

def test_forwardpositionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ForwardPositionKind]
    expected_literals = [
        "left_wing",
        "right_wing",
        "center",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ForwardPositionKind"

def test_defencepositionkind_exists():
    # Check that the Enumeration exists
    assert DefencePositionKind is not None

def test_defencepositionkind_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DefencePositionKind]
    expected_literals = [
        "right_defence",
        "left_defence",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DefencePositionKind"

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
hockeyleague_HockeyleagueObject_strategy = st.builds(
    hockeyleague_HockeyleagueObject,
    name=
        safe_text
)
hockeyleague_GoalieStats_strategy = st.builds(
    hockeyleague_GoalieStats,
    goalsAgainstAverage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    assists=
        st.integers(),
    emptyNetGoals=
        st.integers(),
    year=
        safe_text,
    gamesPlayedIn=
        st.integers(),
    ties=
        st.integers(),
    goalsAgainst=
        st.integers(),
    minutesPlayedIn=
        st.integers(),
    shutouts=
        st.integers(),
    points=
        st.integers(),
    penaltyMinutes=
        st.integers(),
    saves=
        st.integers(),
    losses=
        st.integers(),
    wins=
        st.integers(),
    goals=
        st.integers()
)
hockeyleague_PlayerStats_strategy = st.builds(
    hockeyleague_PlayerStats,
    points=
        st.integers(),
    year=
        safe_text,
    powerPlayGoals=
        st.integers(),
    gamesPlayedIn=
        st.integers(),
    goals=
        st.integers(),
    gameWinningGoals=
        st.integers(),
    plusMinus=
        st.integers(),
    penaltyMinutes=
        st.integers(),
    assists=
        st.integers(),
    shots=
        st.integers(),
    shortHandedGoals=
        st.integers(),
    shotPercentage=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
Player_strategy = st.builds(
    Player,
)
hockeyleague_Forward_strategy = st.builds(
    hockeyleague_Forward,
    position=
        safe_text
)
hockeyleague_Goalie_strategy = st.builds(
    hockeyleague_Goalie,
)
hockeyleague_Defence_strategy = st.builds(
    hockeyleague_Defence,
    position=
        safe_text
)
HockeyleagueObject_strategy = st.builds(
    HockeyleagueObject,
)
hockeyleague_Team_strategy = st.builds(
    hockeyleague_Team,
)
hockeyleague_Player_strategy = st.builds(
    hockeyleague_Player,
    weightValue=
        st.integers(),
    shot=
        safe_text,
    birthplace=
        safe_text,
    birthdate=
        safe_text,
    heightValue=
        st.integers(),
    number=
        st.integers(),
    weightMesurement=
        safe_text,
    heightMesurement=
        safe_text
)
hockeyleague_League_strategy = st.builds(
    hockeyleague_League,
    headoffice=
        safe_text
)
hockeyleague_Arena_strategy = st.builds(
    hockeyleague_Arena,
    address=
        safe_text,
    capacity=
        st.integers()
)

@given(instance=hockeyleague_HockeyleagueObject_strategy)
@settings(max_examples=50)
def test_hockeyleague_hockeyleagueobject_instantiation(instance):
    assert isinstance(instance, hockeyleague_HockeyleagueObject)



@given(instance=hockeyleague_HockeyleagueObject_strategy)
def test_hockeyleague_hockeyleagueobject_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=hockeyleague_GoalieStats_strategy)
@settings(max_examples=50)
def test_hockeyleague_goaliestats_instantiation(instance):
    assert isinstance(instance, hockeyleague_GoalieStats)



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_goalsAgainstAverage_setter(instance):
    original = instance.goalsAgainstAverage
    instance.goalsAgainstAverage = original
    assert instance.goalsAgainstAverage == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_assists_setter(instance):
    original = instance.assists
    instance.assists = original
    assert instance.assists == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_emptyNetGoals_setter(instance):
    original = instance.emptyNetGoals
    instance.emptyNetGoals = original
    assert instance.emptyNetGoals == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_gamesPlayedIn_setter(instance):
    original = instance.gamesPlayedIn
    instance.gamesPlayedIn = original
    assert instance.gamesPlayedIn == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_ties_setter(instance):
    original = instance.ties
    instance.ties = original
    assert instance.ties == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_goalsAgainst_setter(instance):
    original = instance.goalsAgainst
    instance.goalsAgainst = original
    assert instance.goalsAgainst == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_minutesPlayedIn_setter(instance):
    original = instance.minutesPlayedIn
    instance.minutesPlayedIn = original
    assert instance.minutesPlayedIn == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_shutouts_setter(instance):
    original = instance.shutouts
    instance.shutouts = original
    assert instance.shutouts == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_penaltyMinutes_setter(instance):
    original = instance.penaltyMinutes
    instance.penaltyMinutes = original
    assert instance.penaltyMinutes == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_saves_setter(instance):
    original = instance.saves
    instance.saves = original
    assert instance.saves == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_losses_setter(instance):
    original = instance.losses
    instance.losses = original
    assert instance.losses == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_wins_setter(instance):
    original = instance.wins
    instance.wins = original
    assert instance.wins == original



@given(instance=hockeyleague_GoalieStats_strategy)
def test_hockeyleague_goaliestats_goals_setter(instance):
    original = instance.goals
    instance.goals = original
    assert instance.goals == original

@given(instance=hockeyleague_PlayerStats_strategy)
@settings(max_examples=50)
def test_hockeyleague_playerstats_instantiation(instance):
    assert isinstance(instance, hockeyleague_PlayerStats)



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_powerPlayGoals_setter(instance):
    original = instance.powerPlayGoals
    instance.powerPlayGoals = original
    assert instance.powerPlayGoals == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_gamesPlayedIn_setter(instance):
    original = instance.gamesPlayedIn
    instance.gamesPlayedIn = original
    assert instance.gamesPlayedIn == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_goals_setter(instance):
    original = instance.goals
    instance.goals = original
    assert instance.goals == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_gameWinningGoals_setter(instance):
    original = instance.gameWinningGoals
    instance.gameWinningGoals = original
    assert instance.gameWinningGoals == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_plusMinus_setter(instance):
    original = instance.plusMinus
    instance.plusMinus = original
    assert instance.plusMinus == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_penaltyMinutes_setter(instance):
    original = instance.penaltyMinutes
    instance.penaltyMinutes = original
    assert instance.penaltyMinutes == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_assists_setter(instance):
    original = instance.assists
    instance.assists = original
    assert instance.assists == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_shots_setter(instance):
    original = instance.shots
    instance.shots = original
    assert instance.shots == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_shortHandedGoals_setter(instance):
    original = instance.shortHandedGoals
    instance.shortHandedGoals = original
    assert instance.shortHandedGoals == original



@given(instance=hockeyleague_PlayerStats_strategy)
def test_hockeyleague_playerstats_shotPercentage_setter(instance):
    original = instance.shotPercentage
    instance.shotPercentage = original
    assert instance.shotPercentage == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=hockeyleague_Forward_strategy)
@settings(max_examples=50)
def test_hockeyleague_forward_instantiation(instance):
    assert isinstance(instance, hockeyleague_Forward)



@given(instance=hockeyleague_Forward_strategy)
def test_hockeyleague_forward_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=hockeyleague_Goalie_strategy)
@settings(max_examples=50)
def test_hockeyleague_goalie_instantiation(instance):
    assert isinstance(instance, hockeyleague_Goalie)

@given(instance=hockeyleague_Defence_strategy)
@settings(max_examples=50)
def test_hockeyleague_defence_instantiation(instance):
    assert isinstance(instance, hockeyleague_Defence)



@given(instance=hockeyleague_Defence_strategy)
def test_hockeyleague_defence_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original

@given(instance=HockeyleagueObject_strategy)
@settings(max_examples=50)
def test_hockeyleagueobject_instantiation(instance):
    assert isinstance(instance, HockeyleagueObject)

@given(instance=hockeyleague_Team_strategy)
@settings(max_examples=50)
def test_hockeyleague_team_instantiation(instance):
    assert isinstance(instance, hockeyleague_Team)

@given(instance=hockeyleague_Player_strategy)
@settings(max_examples=50)
def test_hockeyleague_player_instantiation(instance):
    assert isinstance(instance, hockeyleague_Player)



@given(instance=hockeyleague_Player_strategy)
def test_hockeyleague_player_weightValue_setter(instance):
    original = instance.weightValue
    instance.weightValue = original
    assert instance.weightValue == original



@given(instance=hockeyleague_Player_strategy)
def test_hockeyleague_player_shot_setter(instance):
    original = instance.shot
    instance.shot = original
    assert instance.shot == original



@given(instance=hockeyleague_Player_strategy)
def test_hockeyleague_player_birthplace_setter(instance):
    original = instance.birthplace
    instance.birthplace = original
    assert instance.birthplace == original



@given(instance=hockeyleague_Player_strategy)
def test_hockeyleague_player_birthdate_setter(instance):
    original = instance.birthdate
    instance.birthdate = original
    assert instance.birthdate == original



@given(instance=hockeyleague_Player_strategy)
def test_hockeyleague_player_heightValue_setter(instance):
    original = instance.heightValue
    instance.heightValue = original
    assert instance.heightValue == original



@given(instance=hockeyleague_Player_strategy)
def test_hockeyleague_player_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=hockeyleague_Player_strategy)
def test_hockeyleague_player_weightMesurement_setter(instance):
    original = instance.weightMesurement
    instance.weightMesurement = original
    assert instance.weightMesurement == original



@given(instance=hockeyleague_Player_strategy)
def test_hockeyleague_player_heightMesurement_setter(instance):
    original = instance.heightMesurement
    instance.heightMesurement = original
    assert instance.heightMesurement == original

@given(instance=hockeyleague_League_strategy)
@settings(max_examples=50)
def test_hockeyleague_league_instantiation(instance):
    assert isinstance(instance, hockeyleague_League)



@given(instance=hockeyleague_League_strategy)
def test_hockeyleague_league_headoffice_setter(instance):
    original = instance.headoffice
    instance.headoffice = original
    assert instance.headoffice == original

@given(instance=hockeyleague_Arena_strategy)
@settings(max_examples=50)
def test_hockeyleague_arena_instantiation(instance):
    assert isinstance(instance, hockeyleague_Arena)



@given(instance=hockeyleague_Arena_strategy)
def test_hockeyleague_arena_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=hockeyleague_Arena_strategy)
def test_hockeyleague_arena_capacity_setter(instance):
    original = instance.capacity
    instance.capacity = original
    assert instance.capacity == original
