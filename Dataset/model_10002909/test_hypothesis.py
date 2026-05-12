import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    FreeParking,
    IncomeTax,
    PlayerIcon,
    JFrame,
    BoardGUI,
    Chance,
    Jail,
    AIPlayer,
    Dice,
    Board1,
    Money,
    Board,
    Random,
    Class,
    Player,
    Property,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_freeparking_is_not_abstract():
    assert not inspect.isabstract(FreeParking)


def test_freeparking_constructor_exists():
    assert callable(FreeParking.__init__)


def test_freeparking_constructor_args():
    sig = inspect.signature(FreeParking.__init__)
    params = list(sig.parameters.keys())



def test_incometax_is_not_abstract():
    assert not inspect.isabstract(IncomeTax)


def test_incometax_constructor_exists():
    assert callable(IncomeTax.__init__)


def test_incometax_constructor_args():
    sig = inspect.signature(IncomeTax.__init__)
    params = list(sig.parameters.keys())
    assert "taxRate" in params, "Missing parameter 'taxRate'"

def test_incometax_has_taxRate():
    assert hasattr(IncomeTax, "taxRate")
    descriptor = None
    for klass in IncomeTax.__mro__:
        if "taxRate" in klass.__dict__:
            descriptor = klass.__dict__["taxRate"]
            break
    assert isinstance(descriptor, property)



def test_playericon_is_not_abstract():
    assert not inspect.isabstract(PlayerIcon)


def test_playericon_constructor_exists():
    assert callable(PlayerIcon.__init__)


def test_playericon_constructor_args():
    sig = inspect.signature(PlayerIcon.__init__)
    params = list(sig.parameters.keys())
    assert "icon" in params, "Missing parameter 'icon'"

def test_playericon_has_icon():
    assert hasattr(PlayerIcon, "icon")
    descriptor = None
    for klass in PlayerIcon.__mro__:
        if "icon" in klass.__dict__:
            descriptor = klass.__dict__["icon"]
            break
    assert isinstance(descriptor, property)



def test_jframe_is_not_abstract():
    assert not inspect.isabstract(JFrame)


def test_jframe_constructor_exists():
    assert callable(JFrame.__init__)


def test_jframe_constructor_args():
    sig = inspect.signature(JFrame.__init__)
    params = list(sig.parameters.keys())



def test_boardgui_is_not_abstract():
    assert not inspect.isabstract(BoardGUI)


def test_boardgui_constructor_exists():
    assert callable(BoardGUI.__init__)


def test_boardgui_constructor_args():
    sig = inspect.signature(BoardGUI.__init__)
    params = list(sig.parameters.keys())
    assert "frame" in params, "Missing parameter 'frame'"

def test_boardgui_has_frame():
    assert hasattr(BoardGUI, "frame")
    descriptor = None
    for klass in BoardGUI.__mro__:
        if "frame" in klass.__dict__:
            descriptor = klass.__dict__["frame"]
            break
    assert isinstance(descriptor, property)



def test_chance_is_not_abstract():
    assert not inspect.isabstract(Chance)


def test_chance_constructor_exists():
    assert callable(Chance.__init__)


def test_chance_constructor_args():
    sig = inspect.signature(Chance.__init__)
    params = list(sig.parameters.keys())
    assert "amount" in params, "Missing parameter 'amount'"

def test_chance_has_amount():
    assert hasattr(Chance, "amount")
    descriptor = None
    for klass in Chance.__mro__:
        if "amount" in klass.__dict__:
            descriptor = klass.__dict__["amount"]
            break
    assert isinstance(descriptor, property)



def test_jail_is_not_abstract():
    assert not inspect.isabstract(Jail)


def test_jail_constructor_exists():
    assert callable(Jail.__init__)


def test_jail_constructor_args():
    sig = inspect.signature(Jail.__init__)
    params = list(sig.parameters.keys())
    assert "JailPosition" in params, "Missing parameter 'JailPosition'"
    assert "jailFine" in params, "Missing parameter 'jailFine'"

def test_jail_has_JailPosition():
    assert hasattr(Jail, "JailPosition")
    descriptor = None
    for klass in Jail.__mro__:
        if "JailPosition" in klass.__dict__:
            descriptor = klass.__dict__["JailPosition"]
            break
    assert isinstance(descriptor, property)

def test_jail_has_jailFine():
    assert hasattr(Jail, "jailFine")
    descriptor = None
    for klass in Jail.__mro__:
        if "jailFine" in klass.__dict__:
            descriptor = klass.__dict__["jailFine"]
            break
    assert isinstance(descriptor, property)



def test_aiplayer_is_not_abstract():
    assert not inspect.isabstract(AIPlayer)


def test_aiplayer_constructor_exists():
    assert callable(AIPlayer.__init__)


def test_aiplayer_constructor_args():
    sig = inspect.signature(AIPlayer.__init__)
    params = list(sig.parameters.keys())



def test_dice_is_not_abstract():
    assert not inspect.isabstract(Dice)


def test_dice_constructor_exists():
    assert callable(Dice.__init__)


def test_dice_constructor_args():
    sig = inspect.signature(Dice.__init__)
    params = list(sig.parameters.keys())
    assert "secondValue" in params, "Missing parameter 'secondValue'"
    assert "randomNumber" in params, "Missing parameter 'randomNumber'"
    assert "firstValue" in params, "Missing parameter 'firstValue'"

def test_dice_has_secondValue():
    assert hasattr(Dice, "secondValue")
    descriptor = None
    for klass in Dice.__mro__:
        if "secondValue" in klass.__dict__:
            descriptor = klass.__dict__["secondValue"]
            break
    assert isinstance(descriptor, property)

def test_dice_has_randomNumber():
    assert hasattr(Dice, "randomNumber")
    descriptor = None
    for klass in Dice.__mro__:
        if "randomNumber" in klass.__dict__:
            descriptor = klass.__dict__["randomNumber"]
            break
    assert isinstance(descriptor, property)

def test_dice_has_firstValue():
    assert hasattr(Dice, "firstValue")
    descriptor = None
    for klass in Dice.__mro__:
        if "firstValue" in klass.__dict__:
            descriptor = klass.__dict__["firstValue"]
            break
    assert isinstance(descriptor, property)



def test_board1_is_not_abstract():
    assert not inspect.isabstract(Board1)


def test_board1_constructor_exists():
    assert callable(Board1.__init__)


def test_board1_constructor_args():
    sig = inspect.signature(Board1.__init__)
    params = list(sig.parameters.keys())
    assert "boardSize" in params, "Missing parameter 'boardSize'"

def test_board1_has_boardSize():
    assert hasattr(Board1, "boardSize")
    descriptor = None
    for klass in Board1.__mro__:
        if "boardSize" in klass.__dict__:
            descriptor = klass.__dict__["boardSize"]
            break
    assert isinstance(descriptor, property)



def test_money_is_not_abstract():
    assert not inspect.isabstract(Money)


def test_money_constructor_exists():
    assert callable(Money.__init__)


def test_money_constructor_args():
    sig = inspect.signature(Money.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"

def test_money_has_money():
    assert hasattr(Money, "money")
    descriptor = None
    for klass in Money.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)



def test_board_is_not_abstract():
    assert not inspect.isabstract(Board)


def test_board_constructor_exists():
    assert callable(Board.__init__)


def test_board_constructor_args():
    sig = inspect.signature(Board.__init__)
    params = list(sig.parameters.keys())



def test_random_is_not_abstract():
    assert not inspect.isabstract(Random)


def test_random_constructor_exists():
    assert callable(Random.__init__)


def test_random_constructor_args():
    sig = inspect.signature(Random.__init__)
    params = list(sig.parameters.keys())



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "money" in params, "Missing parameter 'money'"
    assert "property" in params, "Missing parameter 'property'"
    assert "inJail" in params, "Missing parameter 'inJail'"
    assert "INITIAL_POSITION" in params, "Missing parameter 'INITIAL_POSITION'"
    assert "PASS_GO_MONEY" in params, "Missing parameter 'PASS_GO_MONEY'"
    assert "isBankrupt" in params, "Missing parameter 'isBankrupt'"
    assert "isRetire" in params, "Missing parameter 'isRetire'"
    assert "isAI" in params, "Missing parameter 'isAI'"
    assert "name" in params, "Missing parameter 'name'"
    assert "board" in params, "Missing parameter 'board'"
    assert "rand" in params, "Missing parameter 'rand'"
    assert "position" in params, "Missing parameter 'position'"
    assert "INITIAL_MONEY" in params, "Missing parameter 'INITIAL_MONEY'"

def test_player_has_money():
    assert hasattr(Player, "money")
    descriptor = None
    for klass in Player.__mro__:
        if "money" in klass.__dict__:
            descriptor = klass.__dict__["money"]
            break
    assert isinstance(descriptor, property)

def test_player_has_property():
    assert hasattr(Player, "property")
    descriptor = None
    for klass in Player.__mro__:
        if "property" in klass.__dict__:
            descriptor = klass.__dict__["property"]
            break
    assert isinstance(descriptor, property)

def test_player_has_inJail():
    assert hasattr(Player, "inJail")
    descriptor = None
    for klass in Player.__mro__:
        if "inJail" in klass.__dict__:
            descriptor = klass.__dict__["inJail"]
            break
    assert isinstance(descriptor, property)

def test_player_has_INITIAL_POSITION():
    assert hasattr(Player, "INITIAL_POSITION")
    descriptor = None
    for klass in Player.__mro__:
        if "INITIAL_POSITION" in klass.__dict__:
            descriptor = klass.__dict__["INITIAL_POSITION"]
            break
    assert isinstance(descriptor, property)

def test_player_has_PASS_GO_MONEY():
    assert hasattr(Player, "PASS_GO_MONEY")
    descriptor = None
    for klass in Player.__mro__:
        if "PASS_GO_MONEY" in klass.__dict__:
            descriptor = klass.__dict__["PASS_GO_MONEY"]
            break
    assert isinstance(descriptor, property)

def test_player_has_isBankrupt():
    assert hasattr(Player, "isBankrupt")
    descriptor = None
    for klass in Player.__mro__:
        if "isBankrupt" in klass.__dict__:
            descriptor = klass.__dict__["isBankrupt"]
            break
    assert isinstance(descriptor, property)

def test_player_has_isRetire():
    assert hasattr(Player, "isRetire")
    descriptor = None
    for klass in Player.__mro__:
        if "isRetire" in klass.__dict__:
            descriptor = klass.__dict__["isRetire"]
            break
    assert isinstance(descriptor, property)

def test_player_has_isAI():
    assert hasattr(Player, "isAI")
    descriptor = None
    for klass in Player.__mro__:
        if "isAI" in klass.__dict__:
            descriptor = klass.__dict__["isAI"]
            break
    assert isinstance(descriptor, property)

def test_player_has_name():
    assert hasattr(Player, "name")
    descriptor = None
    for klass in Player.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_player_has_board():
    assert hasattr(Player, "board")
    descriptor = None
    for klass in Player.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)

def test_player_has_rand():
    assert hasattr(Player, "rand")
    descriptor = None
    for klass in Player.__mro__:
        if "rand" in klass.__dict__:
            descriptor = klass.__dict__["rand"]
            break
    assert isinstance(descriptor, property)

def test_player_has_position():
    assert hasattr(Player, "position")
    descriptor = None
    for klass in Player.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_player_has_INITIAL_MONEY():
    assert hasattr(Player, "INITIAL_MONEY")
    descriptor = None
    for klass in Player.__mro__:
        if "INITIAL_MONEY" in klass.__dict__:
            descriptor = klass.__dict__["INITIAL_MONEY"]
            break
    assert isinstance(descriptor, property)

def test_property_exists():
    # Check that the Enumeration exists
    assert Property is not None

def test_property_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Property]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Property"


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
FreeParking_strategy = st.builds(
    FreeParking,
)
IncomeTax_strategy = st.builds(
    IncomeTax,
    taxRate=
        st.floats(min_value=0, max_value=1000,allow_nan=False, allow_infinity=False)
)
PlayerIcon_strategy = st.builds(
    PlayerIcon,
    icon=
        safe_text
)
JFrame_strategy = st.builds(
    JFrame,
)
BoardGUI_strategy = st.builds(
    BoardGUI,
    frame=
        st.none()
)
Chance_strategy = st.builds(
    Chance,
    amount=
        st.none()
)
Jail_strategy = st.builds(
    Jail,
    JailPosition=
        st.integers(),
    jailFine=
        st.integers()
)
AIPlayer_strategy = st.builds(
    AIPlayer,
)
Dice_strategy = st.builds(
    Dice,
    secondValue=
        st.integers(),
    randomNumber=
        st.none(),
    firstValue=
        st.integers()
)
Board1_strategy = st.builds(
    Board1,
    boardSize=
        st.integers()
)
Money_strategy = st.builds(
    Money,
    money=
        st.integers()
)
Board_strategy = st.builds(
    Board,
)
Random_strategy = st.builds(
    Random,
)
Class_strategy = st.builds(
    Class,
)
Player_strategy = st.builds(
    Player,
    money=
        st.none(),
    property=
        safe_text,
    inJail=
        st.booleans(),
    INITIAL_POSITION=
        st.integers(),
    PASS_GO_MONEY=
        st.integers(),
    isBankrupt=
        st.booleans(),
    isRetire=
        st.booleans(),
    isAI=
        st.booleans(),
    name=
        safe_text,
    board=
        st.none(),
    rand=
        st.none(),
    position=
        st.integers(),
    INITIAL_MONEY=
        st.integers()
)

@given(instance=FreeParking_strategy)
@settings(max_examples=50)
def test_freeparking_instantiation(instance):
    assert isinstance(instance, FreeParking)

@given(instance=IncomeTax_strategy)
@settings(max_examples=50)
def test_incometax_instantiation(instance):
    assert isinstance(instance, IncomeTax)



@given(instance=IncomeTax_strategy)
def test_incometax_taxRate_setter(instance):
    original = instance.taxRate
    instance.taxRate = original
    assert instance.taxRate == original

@given(instance=PlayerIcon_strategy)
@settings(max_examples=50)
def test_playericon_instantiation(instance):
    assert isinstance(instance, PlayerIcon)



@given(instance=PlayerIcon_strategy)
def test_playericon_icon_setter(instance):
    original = instance.icon
    instance.icon = original
    assert instance.icon == original

@given(instance=JFrame_strategy)
@settings(max_examples=50)
def test_jframe_instantiation(instance):
    assert isinstance(instance, JFrame)

@given(instance=BoardGUI_strategy)
@settings(max_examples=50)
def test_boardgui_instantiation(instance):
    assert isinstance(instance, BoardGUI)



@given(instance=BoardGUI_strategy)
def test_boardgui_frame_setter(instance):
    original = instance.frame
    instance.frame = original
    assert instance.frame == original

@given(instance=Chance_strategy)
@settings(max_examples=50)
def test_chance_instantiation(instance):
    assert isinstance(instance, Chance)



@given(instance=Chance_strategy)
def test_chance_amount_setter(instance):
    original = instance.amount
    instance.amount = original
    assert instance.amount == original

@given(instance=Jail_strategy)
@settings(max_examples=50)
def test_jail_instantiation(instance):
    assert isinstance(instance, Jail)



@given(instance=Jail_strategy)
def test_jail_JailPosition_setter(instance):
    original = instance.JailPosition
    instance.JailPosition = original
    assert instance.JailPosition == original



@given(instance=Jail_strategy)
def test_jail_jailFine_setter(instance):
    original = instance.jailFine
    instance.jailFine = original
    assert instance.jailFine == original

@given(instance=AIPlayer_strategy)
@settings(max_examples=50)
def test_aiplayer_instantiation(instance):
    assert isinstance(instance, AIPlayer)

@given(instance=Dice_strategy)
@settings(max_examples=50)
def test_dice_instantiation(instance):
    assert isinstance(instance, Dice)



@given(instance=Dice_strategy)
def test_dice_secondValue_setter(instance):
    original = instance.secondValue
    instance.secondValue = original
    assert instance.secondValue == original



@given(instance=Dice_strategy)
def test_dice_randomNumber_setter(instance):
    original = instance.randomNumber
    instance.randomNumber = original
    assert instance.randomNumber == original



@given(instance=Dice_strategy)
def test_dice_firstValue_setter(instance):
    original = instance.firstValue
    instance.firstValue = original
    assert instance.firstValue == original

@given(instance=Board1_strategy)
@settings(max_examples=50)
def test_board1_instantiation(instance):
    assert isinstance(instance, Board1)



@given(instance=Board1_strategy)
def test_board1_boardSize_setter(instance):
    original = instance.boardSize
    instance.boardSize = original
    assert instance.boardSize == original

@given(instance=Money_strategy)
@settings(max_examples=50)
def test_money_instantiation(instance):
    assert isinstance(instance, Money)



@given(instance=Money_strategy)
def test_money_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original

@given(instance=Board_strategy)
@settings(max_examples=50)
def test_board_instantiation(instance):
    assert isinstance(instance, Board)

@given(instance=Random_strategy)
@settings(max_examples=50)
def test_random_instantiation(instance):
    assert isinstance(instance, Random)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_money_setter(instance):
    original = instance.money
    instance.money = original
    assert instance.money == original



@given(instance=Player_strategy)
def test_player_property_setter(instance):
    original = instance.property
    instance.property = original
    assert instance.property == original



@given(instance=Player_strategy)
def test_player_inJail_setter(instance):
    original = instance.inJail
    instance.inJail = original
    assert instance.inJail == original



@given(instance=Player_strategy)
def test_player_INITIAL_POSITION_setter(instance):
    original = instance.INITIAL_POSITION
    instance.INITIAL_POSITION = original
    assert instance.INITIAL_POSITION == original



@given(instance=Player_strategy)
def test_player_PASS_GO_MONEY_setter(instance):
    original = instance.PASS_GO_MONEY
    instance.PASS_GO_MONEY = original
    assert instance.PASS_GO_MONEY == original



@given(instance=Player_strategy)
def test_player_isBankrupt_setter(instance):
    original = instance.isBankrupt
    instance.isBankrupt = original
    assert instance.isBankrupt == original



@given(instance=Player_strategy)
def test_player_isRetire_setter(instance):
    original = instance.isRetire
    instance.isRetire = original
    assert instance.isRetire == original



@given(instance=Player_strategy)
def test_player_isAI_setter(instance):
    original = instance.isAI
    instance.isAI = original
    assert instance.isAI == original



@given(instance=Player_strategy)
def test_player_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Player_strategy)
def test_player_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original



@given(instance=Player_strategy)
def test_player_rand_setter(instance):
    original = instance.rand
    instance.rand = original
    assert instance.rand == original



@given(instance=Player_strategy)
def test_player_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Player_strategy)
def test_player_INITIAL_MONEY_setter(instance):
    original = instance.INITIAL_MONEY
    instance.INITIAL_MONEY = original
    assert instance.INITIAL_MONEY == original
