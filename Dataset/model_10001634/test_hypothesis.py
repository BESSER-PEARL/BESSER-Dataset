import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genmymodelreverse_java_io_IOException,
    genmymodelreverse_java_io_PrintWriter,
    genmymodelreverse_java_io_BufferedReader,
    table_Table,
    table_Deck,
    table_Card,
    server_MultiServer,
    player_Players,
    player_Player,
    managers_LoginManager,
    managers_GameManager,
    common_Subject_Interface,
    common_Observer_Interface,
    common_Hand,
    calculations_PokerRules,
    common_Ranks,
    common_States,
    table_UpcomingCards,
    table_Rank,
    table_Suit,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genmymodelreverse_java_io_ioexception_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_io_IOException)


def test_genmymodelreverse_java_io_ioexception_constructor_exists():
    assert callable(genmymodelreverse_java_io_IOException.__init__)


def test_genmymodelreverse_java_io_ioexception_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_io_IOException.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_io_printwriter_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_io_PrintWriter)


def test_genmymodelreverse_java_io_printwriter_constructor_exists():
    assert callable(genmymodelreverse_java_io_PrintWriter.__init__)


def test_genmymodelreverse_java_io_printwriter_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_io_PrintWriter.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_io_bufferedreader_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_io_BufferedReader)


def test_genmymodelreverse_java_io_bufferedreader_constructor_exists():
    assert callable(genmymodelreverse_java_io_BufferedReader.__init__)


def test_genmymodelreverse_java_io_bufferedreader_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_io_BufferedReader.__init__)
    params = list(sig.parameters.keys())



def test_table_table_is_not_abstract():
    assert not inspect.isabstract(table_Table)


def test_table_table_constructor_exists():
    assert callable(table_Table.__init__)


def test_table_table_constructor_args():
    sig = inspect.signature(table_Table.__init__)
    params = list(sig.parameters.keys())
    assert "turnedCards" in params, "Missing parameter 'turnedCards'"
    assert "amountOfCards" in params, "Missing parameter 'amountOfCards'"
    assert "upcomingCards" in params, "Missing parameter 'upcomingCards'"

def test_table_table_has_turnedCards():
    assert hasattr(table_Table, "turnedCards")
    descriptor = None
    for klass in table_Table.__mro__:
        if "turnedCards" in klass.__dict__:
            descriptor = klass.__dict__["turnedCards"]
            break
    assert isinstance(descriptor, property)

def test_table_table_has_amountOfCards():
    assert hasattr(table_Table, "amountOfCards")
    descriptor = None
    for klass in table_Table.__mro__:
        if "amountOfCards" in klass.__dict__:
            descriptor = klass.__dict__["amountOfCards"]
            break
    assert isinstance(descriptor, property)

def test_table_table_has_upcomingCards():
    assert hasattr(table_Table, "upcomingCards")
    descriptor = None
    for klass in table_Table.__mro__:
        if "upcomingCards" in klass.__dict__:
            descriptor = klass.__dict__["upcomingCards"]
            break
    assert isinstance(descriptor, property)



def test_table_deck_is_not_abstract():
    assert not inspect.isabstract(table_Deck)


def test_table_deck_constructor_exists():
    assert callable(table_Deck.__init__)


def test_table_deck_constructor_args():
    sig = inspect.signature(table_Deck.__init__)
    params = list(sig.parameters.keys())
    assert "randomNumbers" in params, "Missing parameter 'randomNumbers'"
    assert "rank" in params, "Missing parameter 'rank'"
    assert "suit" in params, "Missing parameter 'suit'"
    assert "numCardsInDeck" in params, "Missing parameter 'numCardsInDeck'"

def test_table_deck_has_randomNumbers():
    assert hasattr(table_Deck, "randomNumbers")
    descriptor = None
    for klass in table_Deck.__mro__:
        if "randomNumbers" in klass.__dict__:
            descriptor = klass.__dict__["randomNumbers"]
            break
    assert isinstance(descriptor, property)

def test_table_deck_has_rank():
    assert hasattr(table_Deck, "rank")
    descriptor = None
    for klass in table_Deck.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)

def test_table_deck_has_suit():
    assert hasattr(table_Deck, "suit")
    descriptor = None
    for klass in table_Deck.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_table_deck_has_numCardsInDeck():
    assert hasattr(table_Deck, "numCardsInDeck")
    descriptor = None
    for klass in table_Deck.__mro__:
        if "numCardsInDeck" in klass.__dict__:
            descriptor = klass.__dict__["numCardsInDeck"]
            break
    assert isinstance(descriptor, property)



def test_table_card_is_not_abstract():
    assert not inspect.isabstract(table_Card)


def test_table_card_constructor_exists():
    assert callable(table_Card.__init__)


def test_table_card_constructor_args():
    sig = inspect.signature(table_Card.__init__)
    params = list(sig.parameters.keys())
    assert "suit" in params, "Missing parameter 'suit'"
    assert "rank" in params, "Missing parameter 'rank'"

def test_table_card_has_suit():
    assert hasattr(table_Card, "suit")
    descriptor = None
    for klass in table_Card.__mro__:
        if "suit" in klass.__dict__:
            descriptor = klass.__dict__["suit"]
            break
    assert isinstance(descriptor, property)

def test_table_card_has_rank():
    assert hasattr(table_Card, "rank")
    descriptor = None
    for klass in table_Card.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_server_multiserver_is_not_abstract():
    assert not inspect.isabstract(server_MultiServer)


def test_server_multiserver_constructor_exists():
    assert callable(server_MultiServer.__init__)


def test_server_multiserver_constructor_args():
    sig = inspect.signature(server_MultiServer.__init__)
    params = list(sig.parameters.keys())



def test_player_players_is_not_abstract():
    assert not inspect.isabstract(player_Players)


def test_player_players_constructor_exists():
    assert callable(player_Players.__init__)


def test_player_players_constructor_args():
    sig = inspect.signature(player_Players.__init__)
    params = list(sig.parameters.keys())
    assert "AmountOfPlayers" in params, "Missing parameter 'AmountOfPlayers'"
    assert "goodToGo" in params, "Missing parameter 'goodToGo'"
    assert "wealth" in params, "Missing parameter 'wealth'"
    assert "MaxAmountOfPlayers" in params, "Missing parameter 'MaxAmountOfPlayers'"

def test_player_players_has_AmountOfPlayers():
    assert hasattr(player_Players, "AmountOfPlayers")
    descriptor = None
    for klass in player_Players.__mro__:
        if "AmountOfPlayers" in klass.__dict__:
            descriptor = klass.__dict__["AmountOfPlayers"]
            break
    assert isinstance(descriptor, property)

def test_player_players_has_goodToGo():
    assert hasattr(player_Players, "goodToGo")
    descriptor = None
    for klass in player_Players.__mro__:
        if "goodToGo" in klass.__dict__:
            descriptor = klass.__dict__["goodToGo"]
            break
    assert isinstance(descriptor, property)

def test_player_players_has_wealth():
    assert hasattr(player_Players, "wealth")
    descriptor = None
    for klass in player_Players.__mro__:
        if "wealth" in klass.__dict__:
            descriptor = klass.__dict__["wealth"]
            break
    assert isinstance(descriptor, property)

def test_player_players_has_MaxAmountOfPlayers():
    assert hasattr(player_Players, "MaxAmountOfPlayers")
    descriptor = None
    for klass in player_Players.__mro__:
        if "MaxAmountOfPlayers" in klass.__dict__:
            descriptor = klass.__dict__["MaxAmountOfPlayers"]
            break
    assert isinstance(descriptor, property)



def test_player_player_is_not_abstract():
    assert not inspect.isabstract(player_Player)


def test_player_player_constructor_exists():
    assert callable(player_Player.__init__)


def test_player_player_constructor_args():
    sig = inspect.signature(player_Player.__init__)
    params = list(sig.parameters.keys())
    assert "observerID" in params, "Missing parameter 'observerID'"
    assert "bigB" in params, "Missing parameter 'bigB'"
    assert "observerIDTracker" in params, "Missing parameter 'observerIDTracker'"
    assert "state" in params, "Missing parameter 'state'"
    assert "name" in params, "Missing parameter 'name'"
    assert "dealer" in params, "Missing parameter 'dealer'"
    assert "wealth" in params, "Missing parameter 'wealth'"

def test_player_player_has_observerID():
    assert hasattr(player_Player, "observerID")
    descriptor = None
    for klass in player_Player.__mro__:
        if "observerID" in klass.__dict__:
            descriptor = klass.__dict__["observerID"]
            break
    assert isinstance(descriptor, property)

def test_player_player_has_bigB():
    assert hasattr(player_Player, "bigB")
    descriptor = None
    for klass in player_Player.__mro__:
        if "bigB" in klass.__dict__:
            descriptor = klass.__dict__["bigB"]
            break
    assert isinstance(descriptor, property)

def test_player_player_has_observerIDTracker():
    assert hasattr(player_Player, "observerIDTracker")
    descriptor = None
    for klass in player_Player.__mro__:
        if "observerIDTracker" in klass.__dict__:
            descriptor = klass.__dict__["observerIDTracker"]
            break
    assert isinstance(descriptor, property)

def test_player_player_has_state():
    assert hasattr(player_Player, "state")
    descriptor = None
    for klass in player_Player.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_player_player_has_name():
    assert hasattr(player_Player, "name")
    descriptor = None
    for klass in player_Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_player_has_dealer():
    assert hasattr(player_Player, "dealer")
    descriptor = None
    for klass in player_Player.__mro__:
        if "dealer" in klass.__dict__:
            descriptor = klass.__dict__["dealer"]
            break
    assert isinstance(descriptor, property)

def test_player_player_has_wealth():
    assert hasattr(player_Player, "wealth")
    descriptor = None
    for klass in player_Player.__mro__:
        if "wealth" in klass.__dict__:
            descriptor = klass.__dict__["wealth"]
            break
    assert isinstance(descriptor, property)



def test_managers_loginmanager_is_not_abstract():
    assert not inspect.isabstract(managers_LoginManager)


def test_managers_loginmanager_constructor_exists():
    assert callable(managers_LoginManager.__init__)


def test_managers_loginmanager_constructor_args():
    sig = inspect.signature(managers_LoginManager.__init__)
    params = list(sig.parameters.keys())
    assert "out" in params, "Missing parameter 'out'"
    assert "inputLine" in params, "Missing parameter 'inputLine'"
    assert "in" in params, "Missing parameter 'in'"

def test_managers_loginmanager_has_out():
    assert hasattr(managers_LoginManager, "out")
    descriptor = None
    for klass in managers_LoginManager.__mro__:
        if "out" in klass.__dict__:
            descriptor = klass.__dict__["out"]
            break
    assert isinstance(descriptor, property)

def test_managers_loginmanager_has_inputLine():
    assert hasattr(managers_LoginManager, "inputLine")
    descriptor = None
    for klass in managers_LoginManager.__mro__:
        if "inputLine" in klass.__dict__:
            descriptor = klass.__dict__["inputLine"]
            break
    assert isinstance(descriptor, property)

def test_managers_loginmanager_has_in():
    assert hasattr(managers_LoginManager, "in")
    descriptor = None
    for klass in managers_LoginManager.__mro__:
        if "in" in klass.__dict__:
            descriptor = klass.__dict__["in"]
            break
    assert isinstance(descriptor, property)



def test_managers_gamemanager_is_not_abstract():
    assert not inspect.isabstract(managers_GameManager)


def test_managers_gamemanager_constructor_exists():
    assert callable(managers_GameManager.__init__)


def test_managers_gamemanager_constructor_args():
    sig = inspect.signature(managers_GameManager.__init__)
    params = list(sig.parameters.keys())
    assert "dealer" in params, "Missing parameter 'dealer'"
    assert "minimumState" in params, "Missing parameter 'minimumState'"
    assert "newRound" in params, "Missing parameter 'newRound'"
    assert "playersLeftInTheGame" in params, "Missing parameter 'playersLeftInTheGame'"
    assert "initialSmallID" in params, "Missing parameter 'initialSmallID'"
    assert "stateOfPlayersArr" in params, "Missing parameter 'stateOfPlayersArr'"
    assert "smallblind" in params, "Missing parameter 'smallblind'"
    assert "playerNames" in params, "Missing parameter 'playerNames'"
    assert "raise" in params, "Missing parameter 'raise'"
    assert "playerTurn" in params, "Missing parameter 'playerTurn'"
    assert "playerIDs" in params, "Missing parameter 'playerIDs'"
    assert "tableCards" in params, "Missing parameter 'tableCards'"
    assert "initialBigID" in params, "Missing parameter 'initialBigID'"
    assert "playerHands" in params, "Missing parameter 'playerHands'"
    assert "playerBets" in params, "Missing parameter 'playerBets'"

def test_managers_gamemanager_has_dealer():
    assert hasattr(managers_GameManager, "dealer")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "dealer" in klass.__dict__:
            descriptor = klass.__dict__["dealer"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_minimumState():
    assert hasattr(managers_GameManager, "minimumState")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "minimumState" in klass.__dict__:
            descriptor = klass.__dict__["minimumState"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_newRound():
    assert hasattr(managers_GameManager, "newRound")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "newRound" in klass.__dict__:
            descriptor = klass.__dict__["newRound"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_playersLeftInTheGame():
    assert hasattr(managers_GameManager, "playersLeftInTheGame")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "playersLeftInTheGame" in klass.__dict__:
            descriptor = klass.__dict__["playersLeftInTheGame"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_initialSmallID():
    assert hasattr(managers_GameManager, "initialSmallID")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "initialSmallID" in klass.__dict__:
            descriptor = klass.__dict__["initialSmallID"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_stateOfPlayersArr():
    assert hasattr(managers_GameManager, "stateOfPlayersArr")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "stateOfPlayersArr" in klass.__dict__:
            descriptor = klass.__dict__["stateOfPlayersArr"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_smallblind():
    assert hasattr(managers_GameManager, "smallblind")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "smallblind" in klass.__dict__:
            descriptor = klass.__dict__["smallblind"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_playerNames():
    assert hasattr(managers_GameManager, "playerNames")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "playerNames" in klass.__dict__:
            descriptor = klass.__dict__["playerNames"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_raise():
    assert hasattr(managers_GameManager, "raise")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "raise" in klass.__dict__:
            descriptor = klass.__dict__["raise"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_playerTurn():
    assert hasattr(managers_GameManager, "playerTurn")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "playerTurn" in klass.__dict__:
            descriptor = klass.__dict__["playerTurn"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_playerIDs():
    assert hasattr(managers_GameManager, "playerIDs")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "playerIDs" in klass.__dict__:
            descriptor = klass.__dict__["playerIDs"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_tableCards():
    assert hasattr(managers_GameManager, "tableCards")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "tableCards" in klass.__dict__:
            descriptor = klass.__dict__["tableCards"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_initialBigID():
    assert hasattr(managers_GameManager, "initialBigID")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "initialBigID" in klass.__dict__:
            descriptor = klass.__dict__["initialBigID"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_playerHands():
    assert hasattr(managers_GameManager, "playerHands")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "playerHands" in klass.__dict__:
            descriptor = klass.__dict__["playerHands"]
            break
    assert isinstance(descriptor, property)

def test_managers_gamemanager_has_playerBets():
    assert hasattr(managers_GameManager, "playerBets")
    descriptor = None
    for klass in managers_GameManager.__mro__:
        if "playerBets" in klass.__dict__:
            descriptor = klass.__dict__["playerBets"]
            break
    assert isinstance(descriptor, property)



def test_common_subject_interface_is_not_abstract():
    assert not inspect.isabstract(common_Subject_Interface)


def test_common_subject_interface_constructor_exists():
    assert callable(common_Subject_Interface.__init__)


def test_common_subject_interface_constructor_args():
    sig = inspect.signature(common_Subject_Interface.__init__)
    params = list(sig.parameters.keys())



def test_common_observer_interface_is_not_abstract():
    assert not inspect.isabstract(common_Observer_Interface)


def test_common_observer_interface_constructor_exists():
    assert callable(common_Observer_Interface.__init__)


def test_common_observer_interface_constructor_args():
    sig = inspect.signature(common_Observer_Interface.__init__)
    params = list(sig.parameters.keys())



def test_common_hand_is_not_abstract():
    assert not inspect.isabstract(common_Hand)


def test_common_hand_constructor_exists():
    assert callable(common_Hand.__init__)


def test_common_hand_constructor_args():
    sig = inspect.signature(common_Hand.__init__)
    params = list(sig.parameters.keys())
    assert "rank" in params, "Missing parameter 'rank'"

def test_common_hand_has_rank():
    assert hasattr(common_Hand, "rank")
    descriptor = None
    for klass in common_Hand.__mro__:
        if "rank" in klass.__dict__:
            descriptor = klass.__dict__["rank"]
            break
    assert isinstance(descriptor, property)



def test_calculations_pokerrules_is_not_abstract():
    assert not inspect.isabstract(calculations_PokerRules)


def test_calculations_pokerrules_constructor_exists():
    assert callable(calculations_PokerRules.__init__)


def test_calculations_pokerrules_constructor_args():
    sig = inspect.signature(calculations_PokerRules.__init__)
    params = list(sig.parameters.keys())
    assert "highestCardStraight" in params, "Missing parameter 'highestCardStraight'"
    assert "numberOfPlayers" in params, "Missing parameter 'numberOfPlayers'"
    assert "tableCardRank" in params, "Missing parameter 'tableCardRank'"
    assert "arrayWithHands" in params, "Missing parameter 'arrayWithHands'"
    assert "cardsOnTable" in params, "Missing parameter 'cardsOnTable'"

def test_calculations_pokerrules_has_highestCardStraight():
    assert hasattr(calculations_PokerRules, "highestCardStraight")
    descriptor = None
    for klass in calculations_PokerRules.__mro__:
        if "highestCardStraight" in klass.__dict__:
            descriptor = klass.__dict__["highestCardStraight"]
            break
    assert isinstance(descriptor, property)

def test_calculations_pokerrules_has_numberOfPlayers():
    assert hasattr(calculations_PokerRules, "numberOfPlayers")
    descriptor = None
    for klass in calculations_PokerRules.__mro__:
        if "numberOfPlayers" in klass.__dict__:
            descriptor = klass.__dict__["numberOfPlayers"]
            break
    assert isinstance(descriptor, property)

def test_calculations_pokerrules_has_tableCardRank():
    assert hasattr(calculations_PokerRules, "tableCardRank")
    descriptor = None
    for klass in calculations_PokerRules.__mro__:
        if "tableCardRank" in klass.__dict__:
            descriptor = klass.__dict__["tableCardRank"]
            break
    assert isinstance(descriptor, property)

def test_calculations_pokerrules_has_arrayWithHands():
    assert hasattr(calculations_PokerRules, "arrayWithHands")
    descriptor = None
    for klass in calculations_PokerRules.__mro__:
        if "arrayWithHands" in klass.__dict__:
            descriptor = klass.__dict__["arrayWithHands"]
            break
    assert isinstance(descriptor, property)

def test_calculations_pokerrules_has_cardsOnTable():
    assert hasattr(calculations_PokerRules, "cardsOnTable")
    descriptor = None
    for klass in calculations_PokerRules.__mro__:
        if "cardsOnTable" in klass.__dict__:
            descriptor = klass.__dict__["cardsOnTable"]
            break
    assert isinstance(descriptor, property)

def test_common_ranks_exists():
    # Check that the Enumeration exists
    assert common_Ranks is not None

def test_common_ranks_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in common_Ranks]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in common_Ranks"

def test_common_states_exists():
    # Check that the Enumeration exists
    assert common_States is not None

def test_common_states_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in common_States]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in common_States"

def test_table_upcomingcards_exists():
    # Check that the Enumeration exists
    assert table_UpcomingCards is not None

def test_table_upcomingcards_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in table_UpcomingCards]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in table_UpcomingCards"

def test_table_rank_exists():
    # Check that the Enumeration exists
    assert table_Rank is not None

def test_table_rank_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in table_Rank]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in table_Rank"

def test_table_suit_exists():
    # Check that the Enumeration exists
    assert table_Suit is not None

def test_table_suit_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in table_Suit]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in table_Suit"


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
genmymodelreverse_java_io_IOException_strategy = st.builds(
    genmymodelreverse_java_io_IOException,
)
genmymodelreverse_java_io_PrintWriter_strategy = st.builds(
    genmymodelreverse_java_io_PrintWriter,
)
genmymodelreverse_java_io_BufferedReader_strategy = st.builds(
    genmymodelreverse_java_io_BufferedReader,
)
table_Table_strategy = st.builds(
    table_Table,
    turnedCards=
        safe_text,
    amountOfCards=
        st.integers(),
    upcomingCards=
        st.none()
)
table_Deck_strategy = st.builds(
    table_Deck,
    randomNumbers=
        st.integers(),
    rank=
        st.none(),
    suit=
        st.none(),
    numCardsInDeck=
        st.integers()
)
table_Card_strategy = st.builds(
    table_Card,
    suit=
        st.none(),
    rank=
        st.none()
)
server_MultiServer_strategy = st.builds(
    server_MultiServer,
)
player_Players_strategy = st.builds(
    player_Players,
    AmountOfPlayers=
        st.integers(),
    goodToGo=
        st.booleans(),
    wealth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    MaxAmountOfPlayers=
        st.integers()
)
player_Player_strategy = st.builds(
    player_Player,
    observerID=
        st.integers(),
    bigB=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    observerIDTracker=
        st.integers(),
    state=
        st.none(),
    name=
        safe_text,
    dealer=
        st.booleans(),
    wealth=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
managers_LoginManager_strategy = st.builds(
    managers_LoginManager,
    out=
        st.none(),
    inputLine=
        safe_text,
    in=
        st.none()
)
managers_GameManager_strategy = st.builds(
    managers_GameManager,
    dealer=
        st.integers(),
    minimumState=
        st.none(),
    newRound=
        st.booleans(),
    playersLeftInTheGame=
        st.integers(),
    initialSmallID=
        st.integers(),
    stateOfPlayersArr=
        safe_text,
    smallblind=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    playerNames=
        safe_text,
    raise=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False),
    playerTurn=
        st.integers(),
    playerIDs=
        safe_text,
    tableCards=
        safe_text,
    initialBigID=
        st.integers(),
    playerHands=
        safe_text,
    playerBets=
        safe_text
)
common_Subject_Interface_strategy = st.builds(
    common_Subject_Interface,
)
common_Observer_Interface_strategy = st.builds(
    common_Observer_Interface,
)
common_Hand_strategy = st.builds(
    common_Hand,
    rank=
        st.none()
)
calculations_PokerRules_strategy = st.builds(
    calculations_PokerRules,
    highestCardStraight=
        safe_text,
    numberOfPlayers=
        st.integers(),
    tableCardRank=
        st.none(),
    arrayWithHands=
        safe_text,
    cardsOnTable=
        safe_text
)

@given(instance=genmymodelreverse_java_io_IOException_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_io_ioexception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_io_IOException)

@given(instance=genmymodelreverse_java_io_PrintWriter_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_io_printwriter_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_io_PrintWriter)

@given(instance=genmymodelreverse_java_io_BufferedReader_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_io_bufferedreader_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_io_BufferedReader)

@given(instance=table_Table_strategy)
@settings(max_examples=50)
def test_table_table_instantiation(instance):
    assert isinstance(instance, table_Table)



@given(instance=table_Table_strategy)
def test_table_table_turnedCards_setter(instance):
    original = instance.turnedCards
    instance.turnedCards = original
    assert instance.turnedCards == original



@given(instance=table_Table_strategy)
def test_table_table_amountOfCards_setter(instance):
    original = instance.amountOfCards
    instance.amountOfCards = original
    assert instance.amountOfCards == original



@given(instance=table_Table_strategy)
def test_table_table_upcomingCards_setter(instance):
    original = instance.upcomingCards
    instance.upcomingCards = original
    assert instance.upcomingCards == original

@given(instance=table_Deck_strategy)
@settings(max_examples=50)
def test_table_deck_instantiation(instance):
    assert isinstance(instance, table_Deck)



@given(instance=table_Deck_strategy)
def test_table_deck_randomNumbers_setter(instance):
    original = instance.randomNumbers
    instance.randomNumbers = original
    assert instance.randomNumbers == original



@given(instance=table_Deck_strategy)
def test_table_deck_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original



@given(instance=table_Deck_strategy)
def test_table_deck_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=table_Deck_strategy)
def test_table_deck_numCardsInDeck_setter(instance):
    original = instance.numCardsInDeck
    instance.numCardsInDeck = original
    assert instance.numCardsInDeck == original

@given(instance=table_Card_strategy)
@settings(max_examples=50)
def test_table_card_instantiation(instance):
    assert isinstance(instance, table_Card)



@given(instance=table_Card_strategy)
def test_table_card_suit_setter(instance):
    original = instance.suit
    instance.suit = original
    assert instance.suit == original



@given(instance=table_Card_strategy)
def test_table_card_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=server_MultiServer_strategy)
@settings(max_examples=50)
def test_server_multiserver_instantiation(instance):
    assert isinstance(instance, server_MultiServer)

@given(instance=player_Players_strategy)
@settings(max_examples=50)
def test_player_players_instantiation(instance):
    assert isinstance(instance, player_Players)



@given(instance=player_Players_strategy)
def test_player_players_AmountOfPlayers_setter(instance):
    original = instance.AmountOfPlayers
    instance.AmountOfPlayers = original
    assert instance.AmountOfPlayers == original



@given(instance=player_Players_strategy)
def test_player_players_goodToGo_setter(instance):
    original = instance.goodToGo
    instance.goodToGo = original
    assert instance.goodToGo == original



@given(instance=player_Players_strategy)
def test_player_players_wealth_setter(instance):
    original = instance.wealth
    instance.wealth = original
    assert instance.wealth == original



@given(instance=player_Players_strategy)
def test_player_players_MaxAmountOfPlayers_setter(instance):
    original = instance.MaxAmountOfPlayers
    instance.MaxAmountOfPlayers = original
    assert instance.MaxAmountOfPlayers == original

@given(instance=player_Player_strategy)
@settings(max_examples=50)
def test_player_player_instantiation(instance):
    assert isinstance(instance, player_Player)



@given(instance=player_Player_strategy)
def test_player_player_observerID_setter(instance):
    original = instance.observerID
    instance.observerID = original
    assert instance.observerID == original



@given(instance=player_Player_strategy)
def test_player_player_bigB_setter(instance):
    original = instance.bigB
    instance.bigB = original
    assert instance.bigB == original



@given(instance=player_Player_strategy)
def test_player_player_observerIDTracker_setter(instance):
    original = instance.observerIDTracker
    instance.observerIDTracker = original
    assert instance.observerIDTracker == original



@given(instance=player_Player_strategy)
def test_player_player_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=player_Player_strategy)
def test_player_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=player_Player_strategy)
def test_player_player_dealer_setter(instance):
    original = instance.dealer
    instance.dealer = original
    assert instance.dealer == original



@given(instance=player_Player_strategy)
def test_player_player_wealth_setter(instance):
    original = instance.wealth
    instance.wealth = original
    assert instance.wealth == original

@given(instance=managers_LoginManager_strategy)
@settings(max_examples=50)
def test_managers_loginmanager_instantiation(instance):
    assert isinstance(instance, managers_LoginManager)



@given(instance=managers_LoginManager_strategy)
def test_managers_loginmanager_out_setter(instance):
    original = instance.out
    instance.out = original
    assert instance.out == original



@given(instance=managers_LoginManager_strategy)
def test_managers_loginmanager_inputLine_setter(instance):
    original = instance.inputLine
    instance.inputLine = original
    assert instance.inputLine == original



@given(instance=managers_LoginManager_strategy)
def test_managers_loginmanager_in_setter(instance):
    original = instance.in
    instance.in = original
    assert instance.in == original

@given(instance=managers_GameManager_strategy)
@settings(max_examples=50)
def test_managers_gamemanager_instantiation(instance):
    assert isinstance(instance, managers_GameManager)



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_dealer_setter(instance):
    original = instance.dealer
    instance.dealer = original
    assert instance.dealer == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_minimumState_setter(instance):
    original = instance.minimumState
    instance.minimumState = original
    assert instance.minimumState == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_newRound_setter(instance):
    original = instance.newRound
    instance.newRound = original
    assert instance.newRound == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_playersLeftInTheGame_setter(instance):
    original = instance.playersLeftInTheGame
    instance.playersLeftInTheGame = original
    assert instance.playersLeftInTheGame == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_initialSmallID_setter(instance):
    original = instance.initialSmallID
    instance.initialSmallID = original
    assert instance.initialSmallID == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_stateOfPlayersArr_setter(instance):
    original = instance.stateOfPlayersArr
    instance.stateOfPlayersArr = original
    assert instance.stateOfPlayersArr == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_smallblind_setter(instance):
    original = instance.smallblind
    instance.smallblind = original
    assert instance.smallblind == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_playerNames_setter(instance):
    original = instance.playerNames
    instance.playerNames = original
    assert instance.playerNames == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_raise_setter(instance):
    original = instance.raise
    instance.raise = original
    assert instance.raise == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_playerTurn_setter(instance):
    original = instance.playerTurn
    instance.playerTurn = original
    assert instance.playerTurn == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_playerIDs_setter(instance):
    original = instance.playerIDs
    instance.playerIDs = original
    assert instance.playerIDs == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_tableCards_setter(instance):
    original = instance.tableCards
    instance.tableCards = original
    assert instance.tableCards == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_initialBigID_setter(instance):
    original = instance.initialBigID
    instance.initialBigID = original
    assert instance.initialBigID == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_playerHands_setter(instance):
    original = instance.playerHands
    instance.playerHands = original
    assert instance.playerHands == original



@given(instance=managers_GameManager_strategy)
def test_managers_gamemanager_playerBets_setter(instance):
    original = instance.playerBets
    instance.playerBets = original
    assert instance.playerBets == original

@given(instance=common_Subject_Interface_strategy)
@settings(max_examples=50)
def test_common_subject_interface_instantiation(instance):
    assert isinstance(instance, common_Subject_Interface)

@given(instance=common_Observer_Interface_strategy)
@settings(max_examples=50)
def test_common_observer_interface_instantiation(instance):
    assert isinstance(instance, common_Observer_Interface)

@given(instance=common_Hand_strategy)
@settings(max_examples=50)
def test_common_hand_instantiation(instance):
    assert isinstance(instance, common_Hand)



@given(instance=common_Hand_strategy)
def test_common_hand_rank_setter(instance):
    original = instance.rank
    instance.rank = original
    assert instance.rank == original

@given(instance=calculations_PokerRules_strategy)
@settings(max_examples=50)
def test_calculations_pokerrules_instantiation(instance):
    assert isinstance(instance, calculations_PokerRules)



@given(instance=calculations_PokerRules_strategy)
def test_calculations_pokerrules_highestCardStraight_setter(instance):
    original = instance.highestCardStraight
    instance.highestCardStraight = original
    assert instance.highestCardStraight == original



@given(instance=calculations_PokerRules_strategy)
def test_calculations_pokerrules_numberOfPlayers_setter(instance):
    original = instance.numberOfPlayers
    instance.numberOfPlayers = original
    assert instance.numberOfPlayers == original



@given(instance=calculations_PokerRules_strategy)
def test_calculations_pokerrules_tableCardRank_setter(instance):
    original = instance.tableCardRank
    instance.tableCardRank = original
    assert instance.tableCardRank == original



@given(instance=calculations_PokerRules_strategy)
def test_calculations_pokerrules_arrayWithHands_setter(instance):
    original = instance.arrayWithHands
    instance.arrayWithHands = original
    assert instance.arrayWithHands == original



@given(instance=calculations_PokerRules_strategy)
def test_calculations_pokerrules_cardsOnTable_setter(instance):
    original = instance.cardsOnTable
    instance.cardsOnTable = original
    assert instance.cardsOnTable == original
