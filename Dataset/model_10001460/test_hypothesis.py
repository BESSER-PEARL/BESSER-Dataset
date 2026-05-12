import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    SysMessage,
    ChatMessage,
    Room,
    Game,
    Player,
    Guardian,
    Seer,
    Wolf,
    Villager,
    BaseRole,
    NightAction,
    Enumeration,
    Role,
    State,
    Enumeration2,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sysmessage_is_not_abstract():
    assert not inspect.isabstract(SysMessage)


def test_sysmessage_constructor_exists():
    assert callable(SysMessage.__init__)


def test_sysmessage_constructor_args():
    sig = inspect.signature(SysMessage.__init__)
    params = list(sig.parameters.keys())



def test_chatmessage_is_not_abstract():
    assert not inspect.isabstract(ChatMessage)


def test_chatmessage_constructor_exists():
    assert callable(ChatMessage.__init__)


def test_chatmessage_constructor_args():
    sig = inspect.signature(ChatMessage.__init__)
    params = list(sig.parameters.keys())



def test_room_is_not_abstract():
    assert not inspect.isabstract(Room)


def test_room_constructor_exists():
    assert callable(Room.__init__)


def test_room_constructor_args():
    sig = inspect.signature(Room.__init__)
    params = list(sig.parameters.keys())



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())
    assert "turn_state" in params, "Missing parameter 'turn_state'"

def test_game_has_turn_state():
    assert hasattr(Game, "turn_state")
    descriptor = None
    for klass in Game.__mro__:
        if "turn_state" in klass.__dict__:
            descriptor = klass.__dict__["turn_state"]
            break
    assert isinstance(descriptor, property)



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())
    assert "isAlive" in params, "Missing parameter 'isAlive'"
    assert "role" in params, "Missing parameter 'role'"
    assert "votes" in params, "Missing parameter 'votes'"
    assert "night_target" in params, "Missing parameter 'night_target'"
    assert "vote_for" in params, "Missing parameter 'vote_for'"

def test_player_has_isAlive():
    assert hasattr(Player, "isAlive")
    descriptor = None
    for klass in Player.__mro__:
        if "isAlive" in klass.__dict__:
            descriptor = klass.__dict__["isAlive"]
            break
    assert isinstance(descriptor, property)

def test_player_has_role():
    assert hasattr(Player, "role")
    descriptor = None
    for klass in Player.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_player_has_votes():
    assert hasattr(Player, "votes")
    descriptor = None
    for klass in Player.__mro__:
        if "votes" in klass.__dict__:
            descriptor = klass.__dict__["votes"]
            break
    assert isinstance(descriptor, property)

def test_player_has_night_target():
    assert hasattr(Player, "night_target")
    descriptor = None
    for klass in Player.__mro__:
        if "night_target" in klass.__dict__:
            descriptor = klass.__dict__["night_target"]
            break
    assert isinstance(descriptor, property)

def test_player_has_vote_for():
    assert hasattr(Player, "vote_for")
    descriptor = None
    for klass in Player.__mro__:
        if "vote_for" in klass.__dict__:
            descriptor = klass.__dict__["vote_for"]
            break
    assert isinstance(descriptor, property)



def test_guardian_is_not_abstract():
    assert not inspect.isabstract(Guardian)


def test_guardian_constructor_exists():
    assert callable(Guardian.__init__)


def test_guardian_constructor_args():
    sig = inspect.signature(Guardian.__init__)
    params = list(sig.parameters.keys())



def test_seer_is_not_abstract():
    assert not inspect.isabstract(Seer)


def test_seer_constructor_exists():
    assert callable(Seer.__init__)


def test_seer_constructor_args():
    sig = inspect.signature(Seer.__init__)
    params = list(sig.parameters.keys())



def test_wolf_is_not_abstract():
    assert not inspect.isabstract(Wolf)


def test_wolf_constructor_exists():
    assert callable(Wolf.__init__)


def test_wolf_constructor_args():
    sig = inspect.signature(Wolf.__init__)
    params = list(sig.parameters.keys())



def test_villager_is_not_abstract():
    assert not inspect.isabstract(Villager)


def test_villager_constructor_exists():
    assert callable(Villager.__init__)


def test_villager_constructor_args():
    sig = inspect.signature(Villager.__init__)
    params = list(sig.parameters.keys())



def test_baserole_is_not_abstract():
    assert not inspect.isabstract(BaseRole)


def test_baserole_constructor_exists():
    assert callable(BaseRole.__init__)


def test_baserole_constructor_args():
    sig = inspect.signature(BaseRole.__init__)
    params = list(sig.parameters.keys())
    assert "appear_as" in params, "Missing parameter 'appear_as'"
    assert "night_action" in params, "Missing parameter 'night_action'"
    assert "wins_with" in params, "Missing parameter 'wins_with'"
    assert "role" in params, "Missing parameter 'role'"

def test_baserole_has_appear_as():
    assert hasattr(BaseRole, "appear_as")
    descriptor = None
    for klass in BaseRole.__mro__:
        if "appear_as" in klass.__dict__:
            descriptor = klass.__dict__["appear_as"]
            break
    assert isinstance(descriptor, property)

def test_baserole_has_night_action():
    assert hasattr(BaseRole, "night_action")
    descriptor = None
    for klass in BaseRole.__mro__:
        if "night_action" in klass.__dict__:
            descriptor = klass.__dict__["night_action"]
            break
    assert isinstance(descriptor, property)

def test_baserole_has_wins_with():
    assert hasattr(BaseRole, "wins_with")
    descriptor = None
    for klass in BaseRole.__mro__:
        if "wins_with" in klass.__dict__:
            descriptor = klass.__dict__["wins_with"]
            break
    assert isinstance(descriptor, property)

def test_baserole_has_role():
    assert hasattr(BaseRole, "role")
    descriptor = None
    for klass in BaseRole.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_nightaction_exists():
    # Check that the Enumeration exists
    assert NightAction is not None

def test_nightaction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NightAction]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NightAction"

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"

def test_role_exists():
    # Check that the Enumeration exists
    assert Role is not None

def test_role_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Role]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Role"

def test_state_exists():
    # Check that the Enumeration exists
    assert State is not None

def test_state_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in State]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in State"

def test_enumeration2_exists():
    # Check that the Enumeration exists
    assert Enumeration2 is not None

def test_enumeration2_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration2]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration2"


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
SysMessage_strategy = st.builds(
    SysMessage,
)
ChatMessage_strategy = st.builds(
    ChatMessage,
)
Room_strategy = st.builds(
    Room,
)
Game_strategy = st.builds(
    Game,
    turn_state=
        st.none()
)
Player_strategy = st.builds(
    Player,
    isAlive=
        st.booleans(),
    role=
        safe_text,
    votes=
        st.integers(),
    night_target=
        st.none(),
    vote_for=
        st.none()
)
Guardian_strategy = st.builds(
    Guardian,
)
Seer_strategy = st.builds(
    Seer,
)
Wolf_strategy = st.builds(
    Wolf,
)
Villager_strategy = st.builds(
    Villager,
)
BaseRole_strategy = st.builds(
    BaseRole,
    appear_as=
        st.none(),
    night_action=
        st.none(),
    wins_with=
        st.none(),
    role=
        st.none()
)

@given(instance=SysMessage_strategy)
@settings(max_examples=50)
def test_sysmessage_instantiation(instance):
    assert isinstance(instance, SysMessage)

@given(instance=ChatMessage_strategy)
@settings(max_examples=50)
def test_chatmessage_instantiation(instance):
    assert isinstance(instance, ChatMessage)

@given(instance=Room_strategy)
@settings(max_examples=50)
def test_room_instantiation(instance):
    assert isinstance(instance, Room)

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)



@given(instance=Game_strategy)
def test_game_turn_state_setter(instance):
    original = instance.turn_state
    instance.turn_state = original
    assert instance.turn_state == original

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)



@given(instance=Player_strategy)
def test_player_isAlive_setter(instance):
    original = instance.isAlive
    instance.isAlive = original
    assert instance.isAlive == original



@given(instance=Player_strategy)
def test_player_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=Player_strategy)
def test_player_votes_setter(instance):
    original = instance.votes
    instance.votes = original
    assert instance.votes == original



@given(instance=Player_strategy)
def test_player_night_target_setter(instance):
    original = instance.night_target
    instance.night_target = original
    assert instance.night_target == original



@given(instance=Player_strategy)
def test_player_vote_for_setter(instance):
    original = instance.vote_for
    instance.vote_for = original
    assert instance.vote_for == original

@given(instance=Guardian_strategy)
@settings(max_examples=50)
def test_guardian_instantiation(instance):
    assert isinstance(instance, Guardian)

@given(instance=Seer_strategy)
@settings(max_examples=50)
def test_seer_instantiation(instance):
    assert isinstance(instance, Seer)

@given(instance=Wolf_strategy)
@settings(max_examples=50)
def test_wolf_instantiation(instance):
    assert isinstance(instance, Wolf)

@given(instance=Villager_strategy)
@settings(max_examples=50)
def test_villager_instantiation(instance):
    assert isinstance(instance, Villager)

@given(instance=BaseRole_strategy)
@settings(max_examples=50)
def test_baserole_instantiation(instance):
    assert isinstance(instance, BaseRole)



@given(instance=BaseRole_strategy)
def test_baserole_appear_as_setter(instance):
    original = instance.appear_as
    instance.appear_as = original
    assert instance.appear_as == original



@given(instance=BaseRole_strategy)
def test_baserole_night_action_setter(instance):
    original = instance.night_action
    instance.night_action = original
    assert instance.night_action == original



@given(instance=BaseRole_strategy)
def test_baserole_wins_with_setter(instance):
    original = instance.wins_with
    instance.wins_with = original
    assert instance.wins_with == original



@given(instance=BaseRole_strategy)
def test_baserole_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original
