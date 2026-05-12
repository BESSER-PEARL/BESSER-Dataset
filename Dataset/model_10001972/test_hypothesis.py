import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    BowlingGame,
    Importer_Interface,
    Result,
    InitialData,
    FileImporter,
    Attempt,
    Game,
    Player,
    Match,
    ScoreType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bowlinggame_is_not_abstract():
    assert not inspect.isabstract(BowlingGame)


def test_bowlinggame_constructor_exists():
    assert callable(BowlingGame.__init__)


def test_bowlinggame_constructor_args():
    sig = inspect.signature(BowlingGame.__init__)
    params = list(sig.parameters.keys())
    assert "previousGame" in params, "Missing parameter 'previousGame'"
    assert "nextGames" in params, "Missing parameter 'nextGames'"
    assert "scoreType" in params, "Missing parameter 'scoreType'"
    assert "attempts" in params, "Missing parameter 'attempts'"

def test_bowlinggame_has_previousGame():
    assert hasattr(BowlingGame, "previousGame")
    descriptor = None
    for klass in BowlingGame.__mro__:
        if "previousGame" in klass.__dict__:
            descriptor = klass.__dict__["previousGame"]
            break
    assert isinstance(descriptor, property)

def test_bowlinggame_has_nextGames():
    assert hasattr(BowlingGame, "nextGames")
    descriptor = None
    for klass in BowlingGame.__mro__:
        if "nextGames" in klass.__dict__:
            descriptor = klass.__dict__["nextGames"]
            break
    assert isinstance(descriptor, property)

def test_bowlinggame_has_scoreType():
    assert hasattr(BowlingGame, "scoreType")
    descriptor = None
    for klass in BowlingGame.__mro__:
        if "scoreType" in klass.__dict__:
            descriptor = klass.__dict__["scoreType"]
            break
    assert isinstance(descriptor, property)

def test_bowlinggame_has_attempts():
    assert hasattr(BowlingGame, "attempts")
    descriptor = None
    for klass in BowlingGame.__mro__:
        if "attempts" in klass.__dict__:
            descriptor = klass.__dict__["attempts"]
            break
    assert isinstance(descriptor, property)



def test_importer_interface_is_not_abstract():
    assert not inspect.isabstract(Importer_Interface)


def test_importer_interface_constructor_exists():
    assert callable(Importer_Interface.__init__)


def test_importer_interface_constructor_args():
    sig = inspect.signature(Importer_Interface.__init__)
    params = list(sig.parameters.keys())



def test_result_is_not_abstract():
    assert not inspect.isabstract(Result)


def test_result_constructor_exists():
    assert callable(Result.__init__)


def test_result_constructor_args():
    sig = inspect.signature(Result.__init__)
    params = list(sig.parameters.keys())
    assert "score" in params, "Missing parameter 'score'"
    assert "player" in params, "Missing parameter 'player'"

def test_result_has_score():
    assert hasattr(Result, "score")
    descriptor = None
    for klass in Result.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)

def test_result_has_player():
    assert hasattr(Result, "player")
    descriptor = None
    for klass in Result.__mro__:
        if "player" in klass.__dict__:
            descriptor = klass.__dict__["player"]
            break
    assert isinstance(descriptor, property)



def test_initialdata_is_not_abstract():
    assert not inspect.isabstract(InitialData)


def test_initialdata_constructor_exists():
    assert callable(InitialData.__init__)


def test_initialdata_constructor_args():
    sig = inspect.signature(InitialData.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "playerName" in params, "Missing parameter 'playerName'"

def test_initialdata_has_points():
    assert hasattr(InitialData, "points")
    descriptor = None
    for klass in InitialData.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_initialdata_has_playerName():
    assert hasattr(InitialData, "playerName")
    descriptor = None
    for klass in InitialData.__mro__:
        if "playerName" in klass.__dict__:
            descriptor = klass.__dict__["playerName"]
            break
    assert isinstance(descriptor, property)



def test_fileimporter_is_not_abstract():
    assert not inspect.isabstract(FileImporter)


def test_fileimporter_constructor_exists():
    assert callable(FileImporter.__init__)


def test_fileimporter_constructor_args():
    sig = inspect.signature(FileImporter.__init__)
    params = list(sig.parameters.keys())
    assert "INITIAL_DATAFILE" in params, "Missing parameter 'INITIAL_DATAFILE'"

def test_fileimporter_has_INITIAL_DATAFILE():
    assert hasattr(FileImporter, "INITIAL_DATAFILE")
    descriptor = None
    for klass in FileImporter.__mro__:
        if "INITIAL_DATAFILE" in klass.__dict__:
            descriptor = klass.__dict__["INITIAL_DATAFILE"]
            break
    assert isinstance(descriptor, property)



def test_attempt_is_not_abstract():
    assert not inspect.isabstract(Attempt)


def test_attempt_constructor_exists():
    assert callable(Attempt.__init__)


def test_attempt_constructor_args():
    sig = inspect.signature(Attempt.__init__)
    params = list(sig.parameters.keys())
    assert "points" in params, "Missing parameter 'points'"
    assert "number" in params, "Missing parameter 'number'"

def test_attempt_has_points():
    assert hasattr(Attempt, "points")
    descriptor = None
    for klass in Attempt.__mro__:
        if "points" in klass.__dict__:
            descriptor = klass.__dict__["points"]
            break
    assert isinstance(descriptor, property)

def test_attempt_has_number():
    assert hasattr(Attempt, "number")
    descriptor = None
    for klass in Attempt.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "number" in params, "Missing parameter 'number'"
    assert "score" in params, "Missing parameter 'score'"

def test_game_has_number():
    assert hasattr(Game, "number")
    descriptor = None
    for klass in Game.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_game_has_score():
    assert hasattr(Game, "score")
    descriptor = None
    for klass in Game.__mro__:
        if "score" in klass.__dict__:
            descriptor = klass.__dict__["score"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "totalScore" in params, "Missing parameter 'totalScore'"
    assert "games" in params, "Missing parameter 'games'"

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_has_totalScore():
    assert hasattr(Player, "totalScore")
    descriptor = None
    for klass in Player.__mro__:
        if "totalScore" in klass.__dict__:
            descriptor = klass.__dict__["totalScore"]
            break
    assert isinstance(descriptor, property)

def test_player_has_games():
    assert hasattr(Player, "games")
    descriptor = None
    for klass in Player.__mro__:
        if "games" in klass.__dict__:
            descriptor = klass.__dict__["games"]
            break
    assert isinstance(descriptor, property)



def test_match_is_not_abstract():
    assert not inspect.isabstract(Match)


def test_match_constructor_exists():
    assert callable(Match.__init__)


def test_match_constructor_args():
    sig = inspect.signature(Match.__init__)
    params = list(sig.parameters.keys())
    assert "winner" in params, "Missing parameter 'winner'"
    assert "date" in params, "Missing parameter 'date'"
    assert "name" in params, "Missing parameter 'name'"
    assert "players" in params, "Missing parameter 'players'"

def test_match_has_winner():
    assert hasattr(Match, "winner")
    descriptor = None
    for klass in Match.__mro__:
        if "winner" in klass.__dict__:
            descriptor = klass.__dict__["winner"]
            break
    assert isinstance(descriptor, property)

def test_match_has_date():
    assert hasattr(Match, "date")
    descriptor = None
    for klass in Match.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_match_has_name():
    assert hasattr(Match, "name")
    descriptor = None
    for klass in Match.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_match_has_players():
    assert hasattr(Match, "players")
    descriptor = None
    for klass in Match.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_scoretype_exists():
    # Check that the Enumeration exists
    assert ScoreType is not None

def test_scoretype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ScoreType]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ScoreType"


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
BowlingGame_strategy = st.builds(
    BowlingGame,
    previousGame=
        st.none(),
    nextGames=
        safe_text,
    scoreType=
        st.none(),
    attempts=
        safe_text
)
Importer_Interface_strategy = st.builds(
    Importer_Interface,
)
Result_strategy = st.builds(
    Result,
    score=
        st.integers(),
    player=
        safe_text
)
InitialData_strategy = st.builds(
    InitialData,
    points=
        safe_text,
    playerName=
        safe_text
)
FileImporter_strategy = st.builds(
    FileImporter,
    INITIAL_DATAFILE=
        safe_text
)
Attempt_strategy = st.builds(
    Attempt,
    points=
        st.integers(),
    number=
        st.integers()
)
Game_strategy = st.builds(
    Game,
    number=
        st.integers(),
    score=
        st.integers()
)
Player_strategy = st.builds(
    Player,
    name=
        safe_text,
    totalScore=
        st.integers(),
    games=
        st.none()
)
Match_strategy = st.builds(
    Match,
    winner=
        st.none(),
    date=
        safe_text,
    name=
        safe_text,
    players=
        safe_text
)

@given(instance=BowlingGame_strategy)
@settings(max_examples=50)
def test_bowlinggame_instantiation(instance):
    assert isinstance(instance, BowlingGame)



@given(instance=BowlingGame_strategy)
def test_bowlinggame_previousGame_setter(instance):
    original = instance.previousGame
    instance.previousGame = original
    assert instance.previousGame == original



@given(instance=BowlingGame_strategy)
def test_bowlinggame_nextGames_setter(instance):
    original = instance.nextGames
    instance.nextGames = original
    assert instance.nextGames == original



@given(instance=BowlingGame_strategy)
def test_bowlinggame_scoreType_setter(instance):
    original = instance.scoreType
    instance.scoreType = original
    assert instance.scoreType == original



@given(instance=BowlingGame_strategy)
def test_bowlinggame_attempts_setter(instance):
    original = instance.attempts
    instance.attempts = original
    assert instance.attempts == original

@given(instance=Importer_Interface_strategy)
@settings(max_examples=50)
def test_importer_interface_instantiation(instance):
    assert isinstance(instance, Importer_Interface)

@given(instance=Result_strategy)
@settings(max_examples=50)
def test_result_instantiation(instance):
    assert isinstance(instance, Result)



@given(instance=Result_strategy)
def test_result_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original



@given(instance=Result_strategy)
def test_result_player_setter(instance):
    original = instance.player
    instance.player = original
    assert instance.player == original

@given(instance=InitialData_strategy)
@settings(max_examples=50)
def test_initialdata_instantiation(instance):
    assert isinstance(instance, InitialData)



@given(instance=InitialData_strategy)
def test_initialdata_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=InitialData_strategy)
def test_initialdata_playerName_setter(instance):
    original = instance.playerName
    instance.playerName = original
    assert instance.playerName == original

@given(instance=FileImporter_strategy)
@settings(max_examples=50)
def test_fileimporter_instantiation(instance):
    assert isinstance(instance, FileImporter)



@given(instance=FileImporter_strategy)
def test_fileimporter_INITIAL_DATAFILE_setter(instance):
    original = instance.INITIAL_DATAFILE
    instance.INITIAL_DATAFILE = original
    assert instance.INITIAL_DATAFILE == original

@given(instance=Attempt_strategy)
@settings(max_examples=50)
def test_attempt_instantiation(instance):
    assert isinstance(instance, Attempt)



@given(instance=Attempt_strategy)
def test_attempt_points_setter(instance):
    original = instance.points
    instance.points = original
    assert instance.points == original



@given(instance=Attempt_strategy)
def test_attempt_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=Game_strategy)
def test_game_score_setter(instance):
    original = instance.score
    instance.score = original
    assert instance.score == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_player_totalScore_setter(instance):
    original = instance.totalScore
    instance.totalScore = original
    assert instance.totalScore == original



@given(instance=Player_strategy)
def test_player_games_setter(instance):
    original = instance.games
    instance.games = original
    assert instance.games == original

@given(instance=Match_strategy)
@settings(max_examples=50)
def test_match_instantiation(instance):
    assert isinstance(instance, Match)



@given(instance=Match_strategy)
def test_match_winner_setter(instance):
    original = instance.winner
    instance.winner = original
    assert instance.winner == original



@given(instance=Match_strategy)
def test_match_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Match_strategy)
def test_match_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Match_strategy)
def test_match_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original
