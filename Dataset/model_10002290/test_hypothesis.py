import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Game,
    Snake1,
    Food1,
    Square,
    SnakeBody,
    Wall,
    Food,
    EmptyCell,
    Map,
    WallCell,
    MapCell,
    FoodCell,
    Player,
    Snake,
    GameSession,
    View_high_score_UseCase,
    Play_game_UseCase,
    Start_new_game_UseCase,
    User_Actor,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_game_is_not_abstract():
    assert not inspect.isabstract(Game)


def test_game_constructor_exists():
    assert callable(Game.__init__)


def test_game_constructor_args():
    sig = inspect.signature(Game.__init__)
    params = list(sig.parameters.keys())



def test_snake1_is_not_abstract():
    assert not inspect.isabstract(Snake1)


def test_snake1_constructor_exists():
    assert callable(Snake1.__init__)


def test_snake1_constructor_args():
    sig = inspect.signature(Snake1.__init__)
    params = list(sig.parameters.keys())



def test_food1_is_not_abstract():
    assert not inspect.isabstract(Food1)


def test_food1_constructor_exists():
    assert callable(Food1.__init__)


def test_food1_constructor_args():
    sig = inspect.signature(Food1.__init__)
    params = list(sig.parameters.keys())



def test_square_is_not_abstract():
    assert not inspect.isabstract(Square)


def test_square_constructor_exists():
    assert callable(Square.__init__)


def test_square_constructor_args():
    sig = inspect.signature(Square.__init__)
    params = list(sig.parameters.keys())



def test_snakebody_is_not_abstract():
    assert not inspect.isabstract(SnakeBody)


def test_snakebody_constructor_exists():
    assert callable(SnakeBody.__init__)


def test_snakebody_constructor_args():
    sig = inspect.signature(SnakeBody.__init__)
    params = list(sig.parameters.keys())



def test_wall_is_not_abstract():
    assert not inspect.isabstract(Wall)


def test_wall_constructor_exists():
    assert callable(Wall.__init__)


def test_wall_constructor_args():
    sig = inspect.signature(Wall.__init__)
    params = list(sig.parameters.keys())



def test_food_is_not_abstract():
    assert not inspect.isabstract(Food)


def test_food_constructor_exists():
    assert callable(Food.__init__)


def test_food_constructor_args():
    sig = inspect.signature(Food.__init__)
    params = list(sig.parameters.keys())



def test_emptycell_is_not_abstract():
    assert not inspect.isabstract(EmptyCell)


def test_emptycell_constructor_exists():
    assert callable(EmptyCell.__init__)


def test_emptycell_constructor_args():
    sig = inspect.signature(EmptyCell.__init__)
    params = list(sig.parameters.keys())



def test_map_is_not_abstract():
    assert not inspect.isabstract(Map)


def test_map_constructor_exists():
    assert callable(Map.__init__)


def test_map_constructor_args():
    sig = inspect.signature(Map.__init__)
    params = list(sig.parameters.keys())



def test_wallcell_is_not_abstract():
    assert not inspect.isabstract(WallCell)


def test_wallcell_constructor_exists():
    assert callable(WallCell.__init__)


def test_wallcell_constructor_args():
    sig = inspect.signature(WallCell.__init__)
    params = list(sig.parameters.keys())



def test_mapcell_is_not_abstract():
    assert not inspect.isabstract(MapCell)


def test_mapcell_constructor_exists():
    assert callable(MapCell.__init__)


def test_mapcell_constructor_args():
    sig = inspect.signature(MapCell.__init__)
    params = list(sig.parameters.keys())



def test_foodcell_is_not_abstract():
    assert not inspect.isabstract(FoodCell)


def test_foodcell_constructor_exists():
    assert callable(FoodCell.__init__)


def test_foodcell_constructor_args():
    sig = inspect.signature(FoodCell.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_snake_is_not_abstract():
    assert not inspect.isabstract(Snake)


def test_snake_constructor_exists():
    assert callable(Snake.__init__)


def test_snake_constructor_args():
    sig = inspect.signature(Snake.__init__)
    params = list(sig.parameters.keys())



def test_gamesession_is_not_abstract():
    assert not inspect.isabstract(GameSession)


def test_gamesession_constructor_exists():
    assert callable(GameSession.__init__)


def test_gamesession_constructor_args():
    sig = inspect.signature(GameSession.__init__)
    params = list(sig.parameters.keys())



def test_view_high_score_usecase_is_not_abstract():
    assert not inspect.isabstract(View_high_score_UseCase)


def test_view_high_score_usecase_constructor_exists():
    assert callable(View_high_score_UseCase.__init__)


def test_view_high_score_usecase_constructor_args():
    sig = inspect.signature(View_high_score_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_play_game_usecase_is_not_abstract():
    assert not inspect.isabstract(Play_game_UseCase)


def test_play_game_usecase_constructor_exists():
    assert callable(Play_game_UseCase.__init__)


def test_play_game_usecase_constructor_args():
    sig = inspect.signature(Play_game_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_start_new_game_usecase_is_not_abstract():
    assert not inspect.isabstract(Start_new_game_UseCase)


def test_start_new_game_usecase_constructor_exists():
    assert callable(Start_new_game_UseCase.__init__)


def test_start_new_game_usecase_constructor_args():
    sig = inspect.signature(Start_new_game_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
    params = list(sig.parameters.keys())

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
Game_strategy = st.builds(
    Game,
)
Snake1_strategy = st.builds(
    Snake1,
)
Food1_strategy = st.builds(
    Food1,
)
Square_strategy = st.builds(
    Square,
)
SnakeBody_strategy = st.builds(
    SnakeBody,
)
Wall_strategy = st.builds(
    Wall,
)
Food_strategy = st.builds(
    Food,
)
EmptyCell_strategy = st.builds(
    EmptyCell,
)
Map_strategy = st.builds(
    Map,
)
WallCell_strategy = st.builds(
    WallCell,
)
MapCell_strategy = st.builds(
    MapCell,
)
FoodCell_strategy = st.builds(
    FoodCell,
)
Player_strategy = st.builds(
    Player,
)
Snake_strategy = st.builds(
    Snake,
)
GameSession_strategy = st.builds(
    GameSession,
)
View_high_score_UseCase_strategy = st.builds(
    View_high_score_UseCase,
)
Play_game_UseCase_strategy = st.builds(
    Play_game_UseCase,
)
Start_new_game_UseCase_strategy = st.builds(
    Start_new_game_UseCase,
)
User_Actor_strategy = st.builds(
    User_Actor,
)

@given(instance=Game_strategy)
@settings(max_examples=50)
def test_game_instantiation(instance):
    assert isinstance(instance, Game)

@given(instance=Snake1_strategy)
@settings(max_examples=50)
def test_snake1_instantiation(instance):
    assert isinstance(instance, Snake1)

@given(instance=Food1_strategy)
@settings(max_examples=50)
def test_food1_instantiation(instance):
    assert isinstance(instance, Food1)

@given(instance=Square_strategy)
@settings(max_examples=50)
def test_square_instantiation(instance):
    assert isinstance(instance, Square)

@given(instance=SnakeBody_strategy)
@settings(max_examples=50)
def test_snakebody_instantiation(instance):
    assert isinstance(instance, SnakeBody)

@given(instance=Wall_strategy)
@settings(max_examples=50)
def test_wall_instantiation(instance):
    assert isinstance(instance, Wall)

@given(instance=Food_strategy)
@settings(max_examples=50)
def test_food_instantiation(instance):
    assert isinstance(instance, Food)

@given(instance=EmptyCell_strategy)
@settings(max_examples=50)
def test_emptycell_instantiation(instance):
    assert isinstance(instance, EmptyCell)

@given(instance=Map_strategy)
@settings(max_examples=50)
def test_map_instantiation(instance):
    assert isinstance(instance, Map)

@given(instance=WallCell_strategy)
@settings(max_examples=50)
def test_wallcell_instantiation(instance):
    assert isinstance(instance, WallCell)

@given(instance=MapCell_strategy)
@settings(max_examples=50)
def test_mapcell_instantiation(instance):
    assert isinstance(instance, MapCell)

@given(instance=FoodCell_strategy)
@settings(max_examples=50)
def test_foodcell_instantiation(instance):
    assert isinstance(instance, FoodCell)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=Snake_strategy)
@settings(max_examples=50)
def test_snake_instantiation(instance):
    assert isinstance(instance, Snake)

@given(instance=GameSession_strategy)
@settings(max_examples=50)
def test_gamesession_instantiation(instance):
    assert isinstance(instance, GameSession)

@given(instance=View_high_score_UseCase_strategy)
@settings(max_examples=50)
def test_view_high_score_usecase_instantiation(instance):
    assert isinstance(instance, View_high_score_UseCase)

@given(instance=Play_game_UseCase_strategy)
@settings(max_examples=50)
def test_play_game_usecase_instantiation(instance):
    assert isinstance(instance, Play_game_UseCase)

@given(instance=Start_new_game_UseCase_strategy)
@settings(max_examples=50)
def test_start_new_game_usecase_instantiation(instance):
    assert isinstance(instance, Start_new_game_UseCase)

@given(instance=User_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, User_Actor)
