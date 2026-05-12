import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Game_Start_external,
    Roll_First_external,
    Get_Instructions_external,
    Get_Player_Name_external,
    Play_Again_external,
    Announce_Winner_external,
    Next_Turn_external,
    Score_Roll_external,
    Roll_Dice_external,
    Computer_Turn_external,
    Display,
    Yahtzee_Players1,
    Yahtzee_Scoring1,
    Yahtzee_Turn1,
    Yahtzee_Display1,
    Player_Actor,
    Yahtzee_Component,
    Players,
    Turn,
    Scoring,
    Class1,
    Class,
    Yahtzee_Players,
    Yahtzee_Display,
    Yahtzee_Scoring,
    Yahtzee_Turn,
    Yahtzee_Game,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_game_start_external_is_not_abstract():
    assert not inspect.isabstract(Game_Start_external)


def test_game_start_external_constructor_exists():
    assert callable(Game_Start_external.__init__)


def test_game_start_external_constructor_args():
    sig = inspect.signature(Game_Start_external.__init__)
    params = list(sig.parameters.keys())



def test_roll_first_external_is_not_abstract():
    assert not inspect.isabstract(Roll_First_external)


def test_roll_first_external_constructor_exists():
    assert callable(Roll_First_external.__init__)


def test_roll_first_external_constructor_args():
    sig = inspect.signature(Roll_First_external.__init__)
    params = list(sig.parameters.keys())



def test_get_instructions_external_is_not_abstract():
    assert not inspect.isabstract(Get_Instructions_external)


def test_get_instructions_external_constructor_exists():
    assert callable(Get_Instructions_external.__init__)


def test_get_instructions_external_constructor_args():
    sig = inspect.signature(Get_Instructions_external.__init__)
    params = list(sig.parameters.keys())



def test_get_player_name_external_is_not_abstract():
    assert not inspect.isabstract(Get_Player_Name_external)


def test_get_player_name_external_constructor_exists():
    assert callable(Get_Player_Name_external.__init__)


def test_get_player_name_external_constructor_args():
    sig = inspect.signature(Get_Player_Name_external.__init__)
    params = list(sig.parameters.keys())



def test_play_again_external_is_not_abstract():
    assert not inspect.isabstract(Play_Again_external)


def test_play_again_external_constructor_exists():
    assert callable(Play_Again_external.__init__)


def test_play_again_external_constructor_args():
    sig = inspect.signature(Play_Again_external.__init__)
    params = list(sig.parameters.keys())



def test_announce_winner_external_is_not_abstract():
    assert not inspect.isabstract(Announce_Winner_external)


def test_announce_winner_external_constructor_exists():
    assert callable(Announce_Winner_external.__init__)


def test_announce_winner_external_constructor_args():
    sig = inspect.signature(Announce_Winner_external.__init__)
    params = list(sig.parameters.keys())



def test_next_turn_external_is_not_abstract():
    assert not inspect.isabstract(Next_Turn_external)


def test_next_turn_external_constructor_exists():
    assert callable(Next_Turn_external.__init__)


def test_next_turn_external_constructor_args():
    sig = inspect.signature(Next_Turn_external.__init__)
    params = list(sig.parameters.keys())



def test_score_roll_external_is_not_abstract():
    assert not inspect.isabstract(Score_Roll_external)


def test_score_roll_external_constructor_exists():
    assert callable(Score_Roll_external.__init__)


def test_score_roll_external_constructor_args():
    sig = inspect.signature(Score_Roll_external.__init__)
    params = list(sig.parameters.keys())



def test_roll_dice_external_is_not_abstract():
    assert not inspect.isabstract(Roll_Dice_external)


def test_roll_dice_external_constructor_exists():
    assert callable(Roll_Dice_external.__init__)


def test_roll_dice_external_constructor_args():
    sig = inspect.signature(Roll_Dice_external.__init__)
    params = list(sig.parameters.keys())



def test_computer_turn_external_is_not_abstract():
    assert not inspect.isabstract(Computer_Turn_external)


def test_computer_turn_external_constructor_exists():
    assert callable(Computer_Turn_external.__init__)


def test_computer_turn_external_constructor_args():
    sig = inspect.signature(Computer_Turn_external.__init__)
    params = list(sig.parameters.keys())



def test_display_is_not_abstract():
    assert not inspect.isabstract(Display)


def test_display_constructor_exists():
    assert callable(Display.__init__)


def test_display_constructor_args():
    sig = inspect.signature(Display.__init__)
    params = list(sig.parameters.keys())



def test_yahtzee_players1_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Players1)


def test_yahtzee_players1_constructor_exists():
    assert callable(Yahtzee_Players1.__init__)


def test_yahtzee_players1_constructor_args():
    sig = inspect.signature(Yahtzee_Players1.__init__)
    params = list(sig.parameters.keys())
    assert "playerScore" in params, "Missing parameter 'playerScore'"
    assert "compScore" in params, "Missing parameter 'compScore'"

def test_yahtzee_players1_has_playerScore():
    assert hasattr(Yahtzee_Players1, "playerScore")
    descriptor = None
    for klass in Yahtzee_Players1.__mro__:
        if "playerScore" in klass.__dict__:
            descriptor = klass.__dict__["playerScore"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_players1_has_compScore():
    assert hasattr(Yahtzee_Players1, "compScore")
    descriptor = None
    for klass in Yahtzee_Players1.__mro__:
        if "compScore" in klass.__dict__:
            descriptor = klass.__dict__["compScore"]
            break
    assert isinstance(descriptor, property)



def test_yahtzee_scoring1_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Scoring1)


def test_yahtzee_scoring1_constructor_exists():
    assert callable(Yahtzee_Scoring1.__init__)


def test_yahtzee_scoring1_constructor_args():
    sig = inspect.signature(Yahtzee_Scoring1.__init__)
    params = list(sig.parameters.keys())
    assert "Temp" in params, "Missing parameter 'Temp'"

def test_yahtzee_scoring1_has_Temp():
    assert hasattr(Yahtzee_Scoring1, "Temp")
    descriptor = None
    for klass in Yahtzee_Scoring1.__mro__:
        if "Temp" in klass.__dict__:
            descriptor = klass.__dict__["Temp"]
            break
    assert isinstance(descriptor, property)



def test_yahtzee_turn1_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Turn1)


def test_yahtzee_turn1_constructor_exists():
    assert callable(Yahtzee_Turn1.__init__)


def test_yahtzee_turn1_constructor_args():
    sig = inspect.signature(Yahtzee_Turn1.__init__)
    params = list(sig.parameters.keys())
    assert "Dice" in params, "Missing parameter 'Dice'"

def test_yahtzee_turn1_has_Dice():
    assert hasattr(Yahtzee_Turn1, "Dice")
    descriptor = None
    for klass in Yahtzee_Turn1.__mro__:
        if "Dice" in klass.__dict__:
            descriptor = klass.__dict__["Dice"]
            break
    assert isinstance(descriptor, property)



def test_yahtzee_display1_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Display1)


def test_yahtzee_display1_constructor_exists():
    assert callable(Yahtzee_Display1.__init__)


def test_yahtzee_display1_constructor_args():
    sig = inspect.signature(Yahtzee_Display1.__init__)
    params = list(sig.parameters.keys())
    assert "JButton" in params, "Missing parameter 'JButton'"
    assert "Jpanel" in params, "Missing parameter 'Jpanel'"
    assert "JTextField" in params, "Missing parameter 'JTextField'"
    assert "Player" in params, "Missing parameter 'Player'"
    assert "JRadioButton" in params, "Missing parameter 'JRadioButton'"
    assert "Jlabel" in params, "Missing parameter 'Jlabel'"
    assert "JScrollPanel" in params, "Missing parameter 'JScrollPanel'"
    assert "Computer" in params, "Missing parameter 'Computer'"
    assert "Temp1" in params, "Missing parameter 'Temp1'"
    assert "JFrame" in params, "Missing parameter 'JFrame'"
    assert "Temp" in params, "Missing parameter 'Temp'"
    assert "JImageIcon" in params, "Missing parameter 'JImageIcon'"

def test_yahtzee_display1_has_JButton():
    assert hasattr(Yahtzee_Display1, "JButton")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JButton" in klass.__dict__:
            descriptor = klass.__dict__["JButton"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_Jpanel():
    assert hasattr(Yahtzee_Display1, "Jpanel")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Jpanel" in klass.__dict__:
            descriptor = klass.__dict__["Jpanel"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_JTextField():
    assert hasattr(Yahtzee_Display1, "JTextField")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JTextField" in klass.__dict__:
            descriptor = klass.__dict__["JTextField"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_Player():
    assert hasattr(Yahtzee_Display1, "Player")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Player" in klass.__dict__:
            descriptor = klass.__dict__["Player"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_JRadioButton():
    assert hasattr(Yahtzee_Display1, "JRadioButton")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JRadioButton" in klass.__dict__:
            descriptor = klass.__dict__["JRadioButton"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_Jlabel():
    assert hasattr(Yahtzee_Display1, "Jlabel")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Jlabel" in klass.__dict__:
            descriptor = klass.__dict__["Jlabel"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_JScrollPanel():
    assert hasattr(Yahtzee_Display1, "JScrollPanel")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JScrollPanel" in klass.__dict__:
            descriptor = klass.__dict__["JScrollPanel"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_Computer():
    assert hasattr(Yahtzee_Display1, "Computer")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Computer" in klass.__dict__:
            descriptor = klass.__dict__["Computer"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_Temp1():
    assert hasattr(Yahtzee_Display1, "Temp1")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Temp1" in klass.__dict__:
            descriptor = klass.__dict__["Temp1"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_JFrame():
    assert hasattr(Yahtzee_Display1, "JFrame")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JFrame" in klass.__dict__:
            descriptor = klass.__dict__["JFrame"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_Temp():
    assert hasattr(Yahtzee_Display1, "Temp")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "Temp" in klass.__dict__:
            descriptor = klass.__dict__["Temp"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display1_has_JImageIcon():
    assert hasattr(Yahtzee_Display1, "JImageIcon")
    descriptor = None
    for klass in Yahtzee_Display1.__mro__:
        if "JImageIcon" in klass.__dict__:
            descriptor = klass.__dict__["JImageIcon"]
            break
    assert isinstance(descriptor, property)



def test_player_actor_is_not_abstract():
    assert not inspect.isabstract(Player_Actor)


def test_player_actor_constructor_exists():
    assert callable(Player_Actor.__init__)


def test_player_actor_constructor_args():
    sig = inspect.signature(Player_Actor.__init__)
    params = list(sig.parameters.keys())



def test_yahtzee_component_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Component)


def test_yahtzee_component_constructor_exists():
    assert callable(Yahtzee_Component.__init__)


def test_yahtzee_component_constructor_args():
    sig = inspect.signature(Yahtzee_Component.__init__)
    params = list(sig.parameters.keys())



def test_players_is_not_abstract():
    assert not inspect.isabstract(Players)


def test_players_constructor_exists():
    assert callable(Players.__init__)


def test_players_constructor_args():
    sig = inspect.signature(Players.__init__)
    params = list(sig.parameters.keys())



def test_turn_is_not_abstract():
    assert not inspect.isabstract(Turn)


def test_turn_constructor_exists():
    assert callable(Turn.__init__)


def test_turn_constructor_args():
    sig = inspect.signature(Turn.__init__)
    params = list(sig.parameters.keys())



def test_scoring_is_not_abstract():
    assert not inspect.isabstract(Scoring)


def test_scoring_constructor_exists():
    assert callable(Scoring.__init__)


def test_scoring_constructor_args():
    sig = inspect.signature(Scoring.__init__)
    params = list(sig.parameters.keys())



def test_class1_is_not_abstract():
    assert not inspect.isabstract(Class1)


def test_class1_constructor_exists():
    assert callable(Class1.__init__)


def test_class1_constructor_args():
    sig = inspect.signature(Class1.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_yahtzee_players_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Players)


def test_yahtzee_players_constructor_exists():
    assert callable(Yahtzee_Players.__init__)


def test_yahtzee_players_constructor_args():
    sig = inspect.signature(Yahtzee_Players.__init__)
    params = list(sig.parameters.keys())
    assert "Score" in params, "Missing parameter 'Score'"
    assert "Name" in params, "Missing parameter 'Name'"

def test_yahtzee_players_has_Score():
    assert hasattr(Yahtzee_Players, "Score")
    descriptor = None
    for klass in Yahtzee_Players.__mro__:
        if "Score" in klass.__dict__:
            descriptor = klass.__dict__["Score"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_players_has_Name():
    assert hasattr(Yahtzee_Players, "Name")
    descriptor = None
    for klass in Yahtzee_Players.__mro__:
        if "Name" in klass.__dict__:
            descriptor = klass.__dict__["Name"]
            break
    assert isinstance(descriptor, property)



def test_yahtzee_display_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Display)


def test_yahtzee_display_constructor_exists():
    assert callable(Yahtzee_Display.__init__)


def test_yahtzee_display_constructor_args():
    sig = inspect.signature(Yahtzee_Display.__init__)
    params = list(sig.parameters.keys())
    assert "PanelScorecard" in params, "Missing parameter 'PanelScorecard'"
    assert "PanelGameName" in params, "Missing parameter 'PanelGameName'"
    assert "PanelPrimary" in params, "Missing parameter 'PanelPrimary'"
    assert "PanelNames" in params, "Missing parameter 'PanelNames'"
    assert "PanelChoices" in params, "Missing parameter 'PanelChoices'"

def test_yahtzee_display_has_PanelScorecard():
    assert hasattr(Yahtzee_Display, "PanelScorecard")
    descriptor = None
    for klass in Yahtzee_Display.__mro__:
        if "PanelScorecard" in klass.__dict__:
            descriptor = klass.__dict__["PanelScorecard"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display_has_PanelGameName():
    assert hasattr(Yahtzee_Display, "PanelGameName")
    descriptor = None
    for klass in Yahtzee_Display.__mro__:
        if "PanelGameName" in klass.__dict__:
            descriptor = klass.__dict__["PanelGameName"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display_has_PanelPrimary():
    assert hasattr(Yahtzee_Display, "PanelPrimary")
    descriptor = None
    for klass in Yahtzee_Display.__mro__:
        if "PanelPrimary" in klass.__dict__:
            descriptor = klass.__dict__["PanelPrimary"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display_has_PanelNames():
    assert hasattr(Yahtzee_Display, "PanelNames")
    descriptor = None
    for klass in Yahtzee_Display.__mro__:
        if "PanelNames" in klass.__dict__:
            descriptor = klass.__dict__["PanelNames"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_display_has_PanelChoices():
    assert hasattr(Yahtzee_Display, "PanelChoices")
    descriptor = None
    for klass in Yahtzee_Display.__mro__:
        if "PanelChoices" in klass.__dict__:
            descriptor = klass.__dict__["PanelChoices"]
            break
    assert isinstance(descriptor, property)



def test_yahtzee_scoring_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Scoring)


def test_yahtzee_scoring_constructor_exists():
    assert callable(Yahtzee_Scoring.__init__)


def test_yahtzee_scoring_constructor_args():
    sig = inspect.signature(Yahtzee_Scoring.__init__)
    params = list(sig.parameters.keys())



def test_yahtzee_turn_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Turn)


def test_yahtzee_turn_constructor_exists():
    assert callable(Yahtzee_Turn.__init__)


def test_yahtzee_turn_constructor_args():
    sig = inspect.signature(Yahtzee_Turn.__init__)
    params = list(sig.parameters.keys())



def test_yahtzee_game_is_not_abstract():
    assert not inspect.isabstract(Yahtzee_Game)


def test_yahtzee_game_constructor_exists():
    assert callable(Yahtzee_Game.__init__)


def test_yahtzee_game_constructor_args():
    sig = inspect.signature(Yahtzee_Game.__init__)
    params = list(sig.parameters.keys())
    assert "First" in params, "Missing parameter 'First'"
    assert "Player" in params, "Missing parameter 'Player'"
    assert "CompPlayer" in params, "Missing parameter 'CompPlayer'"
    assert "Again" in params, "Missing parameter 'Again'"

def test_yahtzee_game_has_First():
    assert hasattr(Yahtzee_Game, "First")
    descriptor = None
    for klass in Yahtzee_Game.__mro__:
        if "First" in klass.__dict__:
            descriptor = klass.__dict__["First"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_game_has_Player():
    assert hasattr(Yahtzee_Game, "Player")
    descriptor = None
    for klass in Yahtzee_Game.__mro__:
        if "Player" in klass.__dict__:
            descriptor = klass.__dict__["Player"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_game_has_CompPlayer():
    assert hasattr(Yahtzee_Game, "CompPlayer")
    descriptor = None
    for klass in Yahtzee_Game.__mro__:
        if "CompPlayer" in klass.__dict__:
            descriptor = klass.__dict__["CompPlayer"]
            break
    assert isinstance(descriptor, property)

def test_yahtzee_game_has_Again():
    assert hasattr(Yahtzee_Game, "Again")
    descriptor = None
    for klass in Yahtzee_Game.__mro__:
        if "Again" in klass.__dict__:
            descriptor = klass.__dict__["Again"]
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
Game_Start_external_strategy = st.builds(
    Game_Start_external,
)
Roll_First_external_strategy = st.builds(
    Roll_First_external,
)
Get_Instructions_external_strategy = st.builds(
    Get_Instructions_external,
)
Get_Player_Name_external_strategy = st.builds(
    Get_Player_Name_external,
)
Play_Again_external_strategy = st.builds(
    Play_Again_external,
)
Announce_Winner_external_strategy = st.builds(
    Announce_Winner_external,
)
Next_Turn_external_strategy = st.builds(
    Next_Turn_external,
)
Score_Roll_external_strategy = st.builds(
    Score_Roll_external,
)
Roll_Dice_external_strategy = st.builds(
    Roll_Dice_external,
)
Computer_Turn_external_strategy = st.builds(
    Computer_Turn_external,
)
Display_strategy = st.builds(
    Display,
)
Yahtzee_Players1_strategy = st.builds(
    Yahtzee_Players1,
    playerScore=
        safe_text,
    compScore=
        safe_text
)
Yahtzee_Scoring1_strategy = st.builds(
    Yahtzee_Scoring1,
    Temp=
        safe_text
)
Yahtzee_Turn1_strategy = st.builds(
    Yahtzee_Turn1,
    Dice=
        safe_text
)
Yahtzee_Display1_strategy = st.builds(
    Yahtzee_Display1,
    JButton=
        st.none(),
    Jpanel=
        st.none(),
    JTextField=
        st.none(),
    Player=
        st.none(),
    JRadioButton=
        st.none(),
    Jlabel=
        st.none(),
    JScrollPanel=
        st.none(),
    Computer=
        st.none(),
    Temp1=
        st.integers(),
    JFrame=
        st.none(),
    Temp=
        st.integers(),
    JImageIcon=
        st.none()
)
Player_Actor_strategy = st.builds(
    Player_Actor,
)
Yahtzee_Component_strategy = st.builds(
    Yahtzee_Component,
)
Players_strategy = st.builds(
    Players,
)
Turn_strategy = st.builds(
    Turn,
)
Scoring_strategy = st.builds(
    Scoring,
)
Class1_strategy = st.builds(
    Class1,
)
Class_strategy = st.builds(
    Class,
)
Yahtzee_Players_strategy = st.builds(
    Yahtzee_Players,
    Score=
        safe_text,
    Name=
        safe_text
)
Yahtzee_Display_strategy = st.builds(
    Yahtzee_Display,
    PanelScorecard=
        safe_text,
    PanelGameName=
        safe_text,
    PanelPrimary=
        safe_text,
    PanelNames=
        safe_text,
    PanelChoices=
        safe_text
)
Yahtzee_Scoring_strategy = st.builds(
    Yahtzee_Scoring,
)
Yahtzee_Turn_strategy = st.builds(
    Yahtzee_Turn,
)
Yahtzee_Game_strategy = st.builds(
    Yahtzee_Game,
    First=
        st.integers(),
    Player=
        st.none(),
    CompPlayer=
        st.none(),
    Again=
        st.booleans()
)

@given(instance=Game_Start_external_strategy)
@settings(max_examples=50)
def test_game_start_external_instantiation(instance):
    assert isinstance(instance, Game_Start_external)

@given(instance=Roll_First_external_strategy)
@settings(max_examples=50)
def test_roll_first_external_instantiation(instance):
    assert isinstance(instance, Roll_First_external)

@given(instance=Get_Instructions_external_strategy)
@settings(max_examples=50)
def test_get_instructions_external_instantiation(instance):
    assert isinstance(instance, Get_Instructions_external)

@given(instance=Get_Player_Name_external_strategy)
@settings(max_examples=50)
def test_get_player_name_external_instantiation(instance):
    assert isinstance(instance, Get_Player_Name_external)

@given(instance=Play_Again_external_strategy)
@settings(max_examples=50)
def test_play_again_external_instantiation(instance):
    assert isinstance(instance, Play_Again_external)

@given(instance=Announce_Winner_external_strategy)
@settings(max_examples=50)
def test_announce_winner_external_instantiation(instance):
    assert isinstance(instance, Announce_Winner_external)

@given(instance=Next_Turn_external_strategy)
@settings(max_examples=50)
def test_next_turn_external_instantiation(instance):
    assert isinstance(instance, Next_Turn_external)

@given(instance=Score_Roll_external_strategy)
@settings(max_examples=50)
def test_score_roll_external_instantiation(instance):
    assert isinstance(instance, Score_Roll_external)

@given(instance=Roll_Dice_external_strategy)
@settings(max_examples=50)
def test_roll_dice_external_instantiation(instance):
    assert isinstance(instance, Roll_Dice_external)

@given(instance=Computer_Turn_external_strategy)
@settings(max_examples=50)
def test_computer_turn_external_instantiation(instance):
    assert isinstance(instance, Computer_Turn_external)

@given(instance=Display_strategy)
@settings(max_examples=50)
def test_display_instantiation(instance):
    assert isinstance(instance, Display)

@given(instance=Yahtzee_Players1_strategy)
@settings(max_examples=50)
def test_yahtzee_players1_instantiation(instance):
    assert isinstance(instance, Yahtzee_Players1)



@given(instance=Yahtzee_Players1_strategy)
def test_yahtzee_players1_playerScore_setter(instance):
    original = instance.playerScore
    instance.playerScore = original
    assert instance.playerScore == original



@given(instance=Yahtzee_Players1_strategy)
def test_yahtzee_players1_compScore_setter(instance):
    original = instance.compScore
    instance.compScore = original
    assert instance.compScore == original

@given(instance=Yahtzee_Scoring1_strategy)
@settings(max_examples=50)
def test_yahtzee_scoring1_instantiation(instance):
    assert isinstance(instance, Yahtzee_Scoring1)



@given(instance=Yahtzee_Scoring1_strategy)
def test_yahtzee_scoring1_Temp_setter(instance):
    original = instance.Temp
    instance.Temp = original
    assert instance.Temp == original

@given(instance=Yahtzee_Turn1_strategy)
@settings(max_examples=50)
def test_yahtzee_turn1_instantiation(instance):
    assert isinstance(instance, Yahtzee_Turn1)



@given(instance=Yahtzee_Turn1_strategy)
def test_yahtzee_turn1_Dice_setter(instance):
    original = instance.Dice
    instance.Dice = original
    assert instance.Dice == original

@given(instance=Yahtzee_Display1_strategy)
@settings(max_examples=50)
def test_yahtzee_display1_instantiation(instance):
    assert isinstance(instance, Yahtzee_Display1)



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_JButton_setter(instance):
    original = instance.JButton
    instance.JButton = original
    assert instance.JButton == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_Jpanel_setter(instance):
    original = instance.Jpanel
    instance.Jpanel = original
    assert instance.Jpanel == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_JTextField_setter(instance):
    original = instance.JTextField
    instance.JTextField = original
    assert instance.JTextField == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_Player_setter(instance):
    original = instance.Player
    instance.Player = original
    assert instance.Player == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_JRadioButton_setter(instance):
    original = instance.JRadioButton
    instance.JRadioButton = original
    assert instance.JRadioButton == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_Jlabel_setter(instance):
    original = instance.Jlabel
    instance.Jlabel = original
    assert instance.Jlabel == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_JScrollPanel_setter(instance):
    original = instance.JScrollPanel
    instance.JScrollPanel = original
    assert instance.JScrollPanel == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_Computer_setter(instance):
    original = instance.Computer
    instance.Computer = original
    assert instance.Computer == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_Temp1_setter(instance):
    original = instance.Temp1
    instance.Temp1 = original
    assert instance.Temp1 == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_JFrame_setter(instance):
    original = instance.JFrame
    instance.JFrame = original
    assert instance.JFrame == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_Temp_setter(instance):
    original = instance.Temp
    instance.Temp = original
    assert instance.Temp == original



@given(instance=Yahtzee_Display1_strategy)
def test_yahtzee_display1_JImageIcon_setter(instance):
    original = instance.JImageIcon
    instance.JImageIcon = original
    assert instance.JImageIcon == original

@given(instance=Player_Actor_strategy)
@settings(max_examples=50)
def test_player_actor_instantiation(instance):
    assert isinstance(instance, Player_Actor)

@given(instance=Yahtzee_Component_strategy)
@settings(max_examples=50)
def test_yahtzee_component_instantiation(instance):
    assert isinstance(instance, Yahtzee_Component)

@given(instance=Players_strategy)
@settings(max_examples=50)
def test_players_instantiation(instance):
    assert isinstance(instance, Players)

@given(instance=Turn_strategy)
@settings(max_examples=50)
def test_turn_instantiation(instance):
    assert isinstance(instance, Turn)

@given(instance=Scoring_strategy)
@settings(max_examples=50)
def test_scoring_instantiation(instance):
    assert isinstance(instance, Scoring)

@given(instance=Class1_strategy)
@settings(max_examples=50)
def test_class1_instantiation(instance):
    assert isinstance(instance, Class1)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Yahtzee_Players_strategy)
@settings(max_examples=50)
def test_yahtzee_players_instantiation(instance):
    assert isinstance(instance, Yahtzee_Players)



@given(instance=Yahtzee_Players_strategy)
def test_yahtzee_players_Score_setter(instance):
    original = instance.Score
    instance.Score = original
    assert instance.Score == original



@given(instance=Yahtzee_Players_strategy)
def test_yahtzee_players_Name_setter(instance):
    original = instance.Name
    instance.Name = original
    assert instance.Name == original

@given(instance=Yahtzee_Display_strategy)
@settings(max_examples=50)
def test_yahtzee_display_instantiation(instance):
    assert isinstance(instance, Yahtzee_Display)



@given(instance=Yahtzee_Display_strategy)
def test_yahtzee_display_PanelScorecard_setter(instance):
    original = instance.PanelScorecard
    instance.PanelScorecard = original
    assert instance.PanelScorecard == original



@given(instance=Yahtzee_Display_strategy)
def test_yahtzee_display_PanelGameName_setter(instance):
    original = instance.PanelGameName
    instance.PanelGameName = original
    assert instance.PanelGameName == original



@given(instance=Yahtzee_Display_strategy)
def test_yahtzee_display_PanelPrimary_setter(instance):
    original = instance.PanelPrimary
    instance.PanelPrimary = original
    assert instance.PanelPrimary == original



@given(instance=Yahtzee_Display_strategy)
def test_yahtzee_display_PanelNames_setter(instance):
    original = instance.PanelNames
    instance.PanelNames = original
    assert instance.PanelNames == original



@given(instance=Yahtzee_Display_strategy)
def test_yahtzee_display_PanelChoices_setter(instance):
    original = instance.PanelChoices
    instance.PanelChoices = original
    assert instance.PanelChoices == original

@given(instance=Yahtzee_Scoring_strategy)
@settings(max_examples=50)
def test_yahtzee_scoring_instantiation(instance):
    assert isinstance(instance, Yahtzee_Scoring)

@given(instance=Yahtzee_Turn_strategy)
@settings(max_examples=50)
def test_yahtzee_turn_instantiation(instance):
    assert isinstance(instance, Yahtzee_Turn)

@given(instance=Yahtzee_Game_strategy)
@settings(max_examples=50)
def test_yahtzee_game_instantiation(instance):
    assert isinstance(instance, Yahtzee_Game)



@given(instance=Yahtzee_Game_strategy)
def test_yahtzee_game_First_setter(instance):
    original = instance.First
    instance.First = original
    assert instance.First == original



@given(instance=Yahtzee_Game_strategy)
def test_yahtzee_game_Player_setter(instance):
    original = instance.Player
    instance.Player = original
    assert instance.Player == original



@given(instance=Yahtzee_Game_strategy)
def test_yahtzee_game_CompPlayer_setter(instance):
    original = instance.CompPlayer
    instance.CompPlayer = original
    assert instance.CompPlayer == original



@given(instance=Yahtzee_Game_strategy)
def test_yahtzee_game_Again_setter(instance):
    original = instance.Again
    instance.Again = original
    assert instance.Again == original
