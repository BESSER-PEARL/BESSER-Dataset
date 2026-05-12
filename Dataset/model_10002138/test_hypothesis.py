import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    ImageIcon,
    Listener_Interface,
    Player,
    connect_four_gui_Circle,
    connect_four_gui_Connect4Constant_Interface,
    connect_four_gui_GameOverPanel,
    connect_four_gui_stage,
    connect_four_gui_StartMenu,
    connect_four_gui_GUIPlayer,
    connect_four_gui_red,
    connect_four_gui_Token,
    connect_four_gui_Connect4GUI,
    connect_four_gui_GamePanel,
    Compute_Column_external,
    Select_Column_external,
    Enter_Name_external,
    Choose_how_many_Players_external,
    BorderPane,
    VBox,
    HBox,
    Button,
    Label,
    List_Token_,
    Connect_Four_Component,
    Player_2_Actor,
    Computer_AI_Actor,
    Player_1_Actor,
    javax_swing_JTextField,
    javax_swing_JButton,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_imageicon_is_not_abstract():
    assert not inspect.isabstract(ImageIcon)


def test_imageicon_constructor_exists():
    assert callable(ImageIcon.__init__)


def test_imageicon_constructor_args():
    sig = inspect.signature(ImageIcon.__init__)
    params = list(sig.parameters.keys())



def test_listener_interface_is_not_abstract():
    assert not inspect.isabstract(Listener_Interface)


def test_listener_interface_constructor_exists():
    assert callable(Listener_Interface.__init__)


def test_listener_interface_constructor_args():
    sig = inspect.signature(Listener_Interface.__init__)
    params = list(sig.parameters.keys())



def test_player_is_not_abstract():
    assert not inspect.isabstract(Player)


def test_player_constructor_exists():
    assert callable(Player.__init__)


def test_player_constructor_args():
    sig = inspect.signature(Player.__init__)
    params = list(sig.parameters.keys())



def test_connect_four_gui_circle_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_Circle)


def test_connect_four_gui_circle_constructor_exists():
    assert callable(connect_four_gui_Circle.__init__)


def test_connect_four_gui_circle_constructor_args():
    sig = inspect.signature(connect_four_gui_Circle.__init__)
    params = list(sig.parameters.keys())



def test_connect_four_gui_connect4constant_interface_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_Connect4Constant_Interface)


def test_connect_four_gui_connect4constant_interface_constructor_exists():
    assert callable(connect_four_gui_Connect4Constant_Interface.__init__)


def test_connect_four_gui_connect4constant_interface_constructor_args():
    sig = inspect.signature(connect_four_gui_Connect4Constant_Interface.__init__)
    params = list(sig.parameters.keys())



def test_connect_four_gui_gameoverpanel_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_GameOverPanel)


def test_connect_four_gui_gameoverpanel_constructor_exists():
    assert callable(connect_four_gui_GameOverPanel.__init__)


def test_connect_four_gui_gameoverpanel_constructor_args():
    sig = inspect.signature(connect_four_gui_GameOverPanel.__init__)
    params = list(sig.parameters.keys())
    assert "winner" in params, "Missing parameter 'winner'"
    assert "winnerDisplay" in params, "Missing parameter 'winnerDisplay'"
    assert "butPlayAgain" in params, "Missing parameter 'butPlayAgain'"
    assert "gui" in params, "Missing parameter 'gui'"
    assert "labelGameOVer" in params, "Missing parameter 'labelGameOVer'"
    assert "butMainMenu" in params, "Missing parameter 'butMainMenu'"

def test_connect_four_gui_gameoverpanel_has_winner():
    assert hasattr(connect_four_gui_GameOverPanel, "winner")
    descriptor = None
    for klass in connect_four_gui_GameOverPanel.__mro__:
        if "winner" in klass.__dict__:
            descriptor = klass.__dict__["winner"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gameoverpanel_has_winnerDisplay():
    assert hasattr(connect_four_gui_GameOverPanel, "winnerDisplay")
    descriptor = None
    for klass in connect_four_gui_GameOverPanel.__mro__:
        if "winnerDisplay" in klass.__dict__:
            descriptor = klass.__dict__["winnerDisplay"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gameoverpanel_has_butPlayAgain():
    assert hasattr(connect_four_gui_GameOverPanel, "butPlayAgain")
    descriptor = None
    for klass in connect_four_gui_GameOverPanel.__mro__:
        if "butPlayAgain" in klass.__dict__:
            descriptor = klass.__dict__["butPlayAgain"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gameoverpanel_has_gui():
    assert hasattr(connect_four_gui_GameOverPanel, "gui")
    descriptor = None
    for klass in connect_four_gui_GameOverPanel.__mro__:
        if "gui" in klass.__dict__:
            descriptor = klass.__dict__["gui"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gameoverpanel_has_labelGameOVer():
    assert hasattr(connect_four_gui_GameOverPanel, "labelGameOVer")
    descriptor = None
    for klass in connect_four_gui_GameOverPanel.__mro__:
        if "labelGameOVer" in klass.__dict__:
            descriptor = klass.__dict__["labelGameOVer"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gameoverpanel_has_butMainMenu():
    assert hasattr(connect_four_gui_GameOverPanel, "butMainMenu")
    descriptor = None
    for klass in connect_four_gui_GameOverPanel.__mro__:
        if "butMainMenu" in klass.__dict__:
            descriptor = klass.__dict__["butMainMenu"]
            break
    assert isinstance(descriptor, property)



def test_connect_four_gui_stage_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_stage)


def test_connect_four_gui_stage_constructor_exists():
    assert callable(connect_four_gui_stage.__init__)


def test_connect_four_gui_stage_constructor_args():
    sig = inspect.signature(connect_four_gui_stage.__init__)
    params = list(sig.parameters.keys())



def test_connect_four_gui_startmenu_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_StartMenu)


def test_connect_four_gui_startmenu_constructor_exists():
    assert callable(connect_four_gui_StartMenu.__init__)


def test_connect_four_gui_startmenu_constructor_args():
    sig = inspect.signature(connect_four_gui_StartMenu.__init__)
    params = list(sig.parameters.keys())
    assert "bStart" in params, "Missing parameter 'bStart'"
    assert "bPlay" in params, "Missing parameter 'bPlay'"
    assert "startLabel" in params, "Missing parameter 'startLabel'"
    assert "bp" in params, "Missing parameter 'bp'"
    assert "label" in params, "Missing parameter 'label'"
    assert "window" in params, "Missing parameter 'window'"

def test_connect_four_gui_startmenu_has_bStart():
    assert hasattr(connect_four_gui_StartMenu, "bStart")
    descriptor = None
    for klass in connect_four_gui_StartMenu.__mro__:
        if "bStart" in klass.__dict__:
            descriptor = klass.__dict__["bStart"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_startmenu_has_bPlay():
    assert hasattr(connect_four_gui_StartMenu, "bPlay")
    descriptor = None
    for klass in connect_four_gui_StartMenu.__mro__:
        if "bPlay" in klass.__dict__:
            descriptor = klass.__dict__["bPlay"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_startmenu_has_startLabel():
    assert hasattr(connect_four_gui_StartMenu, "startLabel")
    descriptor = None
    for klass in connect_four_gui_StartMenu.__mro__:
        if "startLabel" in klass.__dict__:
            descriptor = klass.__dict__["startLabel"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_startmenu_has_bp():
    assert hasattr(connect_four_gui_StartMenu, "bp")
    descriptor = None
    for klass in connect_four_gui_StartMenu.__mro__:
        if "bp" in klass.__dict__:
            descriptor = klass.__dict__["bp"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_startmenu_has_label():
    assert hasattr(connect_four_gui_StartMenu, "label")
    descriptor = None
    for klass in connect_four_gui_StartMenu.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_startmenu_has_window():
    assert hasattr(connect_four_gui_StartMenu, "window")
    descriptor = None
    for klass in connect_four_gui_StartMenu.__mro__:
        if "window" in klass.__dict__:
            descriptor = klass.__dict__["window"]
            break
    assert isinstance(descriptor, property)



def test_connect_four_gui_guiplayer_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_GUIPlayer)


def test_connect_four_gui_guiplayer_constructor_exists():
    assert callable(connect_four_gui_GUIPlayer.__init__)


def test_connect_four_gui_guiplayer_constructor_args():
    sig = inspect.signature(connect_four_gui_GUIPlayer.__init__)
    params = list(sig.parameters.keys())
    assert "board" in params, "Missing parameter 'board'"
    assert "gpGUI" in params, "Missing parameter 'gpGUI'"
    assert "m_name" in params, "Missing parameter 'm_name'"

def test_connect_four_gui_guiplayer_has_board():
    assert hasattr(connect_four_gui_GUIPlayer, "board")
    descriptor = None
    for klass in connect_four_gui_GUIPlayer.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_guiplayer_has_gpGUI():
    assert hasattr(connect_four_gui_GUIPlayer, "gpGUI")
    descriptor = None
    for klass in connect_four_gui_GUIPlayer.__mro__:
        if "gpGUI" in klass.__dict__:
            descriptor = klass.__dict__["gpGUI"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_guiplayer_has_m_name():
    assert hasattr(connect_four_gui_GUIPlayer, "m_name")
    descriptor = None
    for klass in connect_four_gui_GUIPlayer.__mro__:
        if "m_name" in klass.__dict__:
            descriptor = klass.__dict__["m_name"]
            break
    assert isinstance(descriptor, property)



def test_connect_four_gui_red_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_red)


def test_connect_four_gui_red_constructor_exists():
    assert callable(connect_four_gui_red.__init__)


def test_connect_four_gui_red_constructor_args():
    sig = inspect.signature(connect_four_gui_red.__init__)
    params = list(sig.parameters.keys())



def test_connect_four_gui_token_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_Token)


def test_connect_four_gui_token_constructor_exists():
    assert callable(connect_four_gui_Token.__init__)


def test_connect_four_gui_token_constructor_args():
    sig = inspect.signature(connect_four_gui_Token.__init__)
    params = list(sig.parameters.keys())
    assert "X" in params, "Missing parameter 'X'"
    assert "Y" in params, "Missing parameter 'Y'"
    assert "red" in params, "Missing parameter 'red'"

def test_connect_four_gui_token_has_X():
    assert hasattr(connect_four_gui_Token, "X")
    descriptor = None
    for klass in connect_four_gui_Token.__mro__:
        if "X" in klass.__dict__:
            descriptor = klass.__dict__["X"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_token_has_Y():
    assert hasattr(connect_four_gui_Token, "Y")
    descriptor = None
    for klass in connect_four_gui_Token.__mro__:
        if "Y" in klass.__dict__:
            descriptor = klass.__dict__["Y"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_token_has_red():
    assert hasattr(connect_four_gui_Token, "red")
    descriptor = None
    for klass in connect_four_gui_Token.__mro__:
        if "red" in klass.__dict__:
            descriptor = klass.__dict__["red"]
            break
    assert isinstance(descriptor, property)



def test_connect_four_gui_connect4gui_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_Connect4GUI)


def test_connect_four_gui_connect4gui_constructor_exists():
    assert callable(connect_four_gui_Connect4GUI.__init__)


def test_connect_four_gui_connect4gui_constructor_args():
    sig = inspect.signature(connect_four_gui_Connect4GUI.__init__)
    params = list(sig.parameters.keys())
    assert "redToken" in params, "Missing parameter 'redToken'"
    assert "startUp" in params, "Missing parameter 'startUp'"
    assert "window" in params, "Missing parameter 'window'"
    assert "cpList" in params, "Missing parameter 'cpList'"
    assert "comp" in params, "Missing parameter 'comp'"
    assert "gridBoard" in params, "Missing parameter 'gridBoard'"
    assert "tokenRoot" in params, "Missing parameter 'tokenRoot'"

def test_connect_four_gui_connect4gui_has_redToken():
    assert hasattr(connect_four_gui_Connect4GUI, "redToken")
    descriptor = None
    for klass in connect_four_gui_Connect4GUI.__mro__:
        if "redToken" in klass.__dict__:
            descriptor = klass.__dict__["redToken"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_connect4gui_has_startUp():
    assert hasattr(connect_four_gui_Connect4GUI, "startUp")
    descriptor = None
    for klass in connect_four_gui_Connect4GUI.__mro__:
        if "startUp" in klass.__dict__:
            descriptor = klass.__dict__["startUp"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_connect4gui_has_window():
    assert hasattr(connect_four_gui_Connect4GUI, "window")
    descriptor = None
    for klass in connect_four_gui_Connect4GUI.__mro__:
        if "window" in klass.__dict__:
            descriptor = klass.__dict__["window"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_connect4gui_has_cpList():
    assert hasattr(connect_four_gui_Connect4GUI, "cpList")
    descriptor = None
    for klass in connect_four_gui_Connect4GUI.__mro__:
        if "cpList" in klass.__dict__:
            descriptor = klass.__dict__["cpList"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_connect4gui_has_comp():
    assert hasattr(connect_four_gui_Connect4GUI, "comp")
    descriptor = None
    for klass in connect_four_gui_Connect4GUI.__mro__:
        if "comp" in klass.__dict__:
            descriptor = klass.__dict__["comp"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_connect4gui_has_gridBoard():
    assert hasattr(connect_four_gui_Connect4GUI, "gridBoard")
    descriptor = None
    for klass in connect_four_gui_Connect4GUI.__mro__:
        if "gridBoard" in klass.__dict__:
            descriptor = klass.__dict__["gridBoard"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_connect4gui_has_tokenRoot():
    assert hasattr(connect_four_gui_Connect4GUI, "tokenRoot")
    descriptor = None
    for klass in connect_four_gui_Connect4GUI.__mro__:
        if "tokenRoot" in klass.__dict__:
            descriptor = klass.__dict__["tokenRoot"]
            break
    assert isinstance(descriptor, property)



def test_connect_four_gui_gamepanel_is_not_abstract():
    assert not inspect.isabstract(connect_four_gui_GamePanel)


def test_connect_four_gui_gamepanel_constructor_exists():
    assert callable(connect_four_gui_GamePanel.__init__)


def test_connect_four_gui_gamepanel_constructor_args():
    sig = inspect.signature(connect_four_gui_GamePanel.__init__)
    params = list(sig.parameters.keys())
    assert "newColumnNum" in params, "Missing parameter 'newColumnNum'"
    assert "board" in params, "Missing parameter 'board'"
    assert "game" in params, "Missing parameter 'game'"
    assert "pieces" in params, "Missing parameter 'pieces'"
    assert "players" in params, "Missing parameter 'players'"
    assert "isComputerEnabled" in params, "Missing parameter 'isComputerEnabled'"
    assert "windows" in params, "Missing parameter 'windows'"
    assert "justWon" in params, "Missing parameter 'justWon'"
    assert "whoPlayed" in params, "Missing parameter 'whoPlayed'"
    assert "startUp" in params, "Missing parameter 'startUp'"
    assert "columnNum" in params, "Missing parameter 'columnNum'"
    assert "newDrawPos" in params, "Missing parameter 'newDrawPos'"
    assert "Connect4_GUI" in params, "Missing parameter 'Connect4_GUI'"
    assert "turnNum" in params, "Missing parameter 'turnNum'"

def test_connect_four_gui_gamepanel_has_newColumnNum():
    assert hasattr(connect_four_gui_GamePanel, "newColumnNum")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "newColumnNum" in klass.__dict__:
            descriptor = klass.__dict__["newColumnNum"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_board():
    assert hasattr(connect_four_gui_GamePanel, "board")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_game():
    assert hasattr(connect_four_gui_GamePanel, "game")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "game" in klass.__dict__:
            descriptor = klass.__dict__["game"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_pieces():
    assert hasattr(connect_four_gui_GamePanel, "pieces")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "pieces" in klass.__dict__:
            descriptor = klass.__dict__["pieces"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_players():
    assert hasattr(connect_four_gui_GamePanel, "players")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_isComputerEnabled():
    assert hasattr(connect_four_gui_GamePanel, "isComputerEnabled")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "isComputerEnabled" in klass.__dict__:
            descriptor = klass.__dict__["isComputerEnabled"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_windows():
    assert hasattr(connect_four_gui_GamePanel, "windows")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "windows" in klass.__dict__:
            descriptor = klass.__dict__["windows"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_justWon():
    assert hasattr(connect_four_gui_GamePanel, "justWon")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "justWon" in klass.__dict__:
            descriptor = klass.__dict__["justWon"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_whoPlayed():
    assert hasattr(connect_four_gui_GamePanel, "whoPlayed")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "whoPlayed" in klass.__dict__:
            descriptor = klass.__dict__["whoPlayed"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_startUp():
    assert hasattr(connect_four_gui_GamePanel, "startUp")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "startUp" in klass.__dict__:
            descriptor = klass.__dict__["startUp"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_columnNum():
    assert hasattr(connect_four_gui_GamePanel, "columnNum")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "columnNum" in klass.__dict__:
            descriptor = klass.__dict__["columnNum"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_newDrawPos():
    assert hasattr(connect_four_gui_GamePanel, "newDrawPos")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "newDrawPos" in klass.__dict__:
            descriptor = klass.__dict__["newDrawPos"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_Connect4_GUI():
    assert hasattr(connect_four_gui_GamePanel, "Connect4_GUI")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "Connect4_GUI" in klass.__dict__:
            descriptor = klass.__dict__["Connect4_GUI"]
            break
    assert isinstance(descriptor, property)

def test_connect_four_gui_gamepanel_has_turnNum():
    assert hasattr(connect_four_gui_GamePanel, "turnNum")
    descriptor = None
    for klass in connect_four_gui_GamePanel.__mro__:
        if "turnNum" in klass.__dict__:
            descriptor = klass.__dict__["turnNum"]
            break
    assert isinstance(descriptor, property)



def test_compute_column_external_is_not_abstract():
    assert not inspect.isabstract(Compute_Column_external)


def test_compute_column_external_constructor_exists():
    assert callable(Compute_Column_external.__init__)


def test_compute_column_external_constructor_args():
    sig = inspect.signature(Compute_Column_external.__init__)
    params = list(sig.parameters.keys())



def test_select_column_external_is_not_abstract():
    assert not inspect.isabstract(Select_Column_external)


def test_select_column_external_constructor_exists():
    assert callable(Select_Column_external.__init__)


def test_select_column_external_constructor_args():
    sig = inspect.signature(Select_Column_external.__init__)
    params = list(sig.parameters.keys())



def test_enter_name_external_is_not_abstract():
    assert not inspect.isabstract(Enter_Name_external)


def test_enter_name_external_constructor_exists():
    assert callable(Enter_Name_external.__init__)


def test_enter_name_external_constructor_args():
    sig = inspect.signature(Enter_Name_external.__init__)
    params = list(sig.parameters.keys())



def test_choose_how_many_players_external_is_not_abstract():
    assert not inspect.isabstract(Choose_how_many_Players_external)


def test_choose_how_many_players_external_constructor_exists():
    assert callable(Choose_how_many_Players_external.__init__)


def test_choose_how_many_players_external_constructor_args():
    sig = inspect.signature(Choose_how_many_Players_external.__init__)
    params = list(sig.parameters.keys())



def test_borderpane_is_not_abstract():
    assert not inspect.isabstract(BorderPane)


def test_borderpane_constructor_exists():
    assert callable(BorderPane.__init__)


def test_borderpane_constructor_args():
    sig = inspect.signature(BorderPane.__init__)
    params = list(sig.parameters.keys())



def test_vbox_is_not_abstract():
    assert not inspect.isabstract(VBox)


def test_vbox_constructor_exists():
    assert callable(VBox.__init__)


def test_vbox_constructor_args():
    sig = inspect.signature(VBox.__init__)
    params = list(sig.parameters.keys())



def test_hbox_is_not_abstract():
    assert not inspect.isabstract(HBox)


def test_hbox_constructor_exists():
    assert callable(HBox.__init__)


def test_hbox_constructor_args():
    sig = inspect.signature(HBox.__init__)
    params = list(sig.parameters.keys())



def test_button_is_not_abstract():
    assert not inspect.isabstract(Button)


def test_button_constructor_exists():
    assert callable(Button.__init__)


def test_button_constructor_args():
    sig = inspect.signature(Button.__init__)
    params = list(sig.parameters.keys())



def test_label_is_not_abstract():
    assert not inspect.isabstract(Label)


def test_label_constructor_exists():
    assert callable(Label.__init__)


def test_label_constructor_args():
    sig = inspect.signature(Label.__init__)
    params = list(sig.parameters.keys())



def test_list_token__is_not_abstract():
    assert not inspect.isabstract(List_Token_)


def test_list_token__constructor_exists():
    assert callable(List_Token_.__init__)


def test_list_token__constructor_args():
    sig = inspect.signature(List_Token_.__init__)
    params = list(sig.parameters.keys())



def test_connect_four_component_is_not_abstract():
    assert not inspect.isabstract(Connect_Four_Component)


def test_connect_four_component_constructor_exists():
    assert callable(Connect_Four_Component.__init__)


def test_connect_four_component_constructor_args():
    sig = inspect.signature(Connect_Four_Component.__init__)
    params = list(sig.parameters.keys())



def test_player_2_actor_is_not_abstract():
    assert not inspect.isabstract(Player_2_Actor)


def test_player_2_actor_constructor_exists():
    assert callable(Player_2_Actor.__init__)


def test_player_2_actor_constructor_args():
    sig = inspect.signature(Player_2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_computer_ai_actor_is_not_abstract():
    assert not inspect.isabstract(Computer_AI_Actor)


def test_computer_ai_actor_constructor_exists():
    assert callable(Computer_AI_Actor.__init__)


def test_computer_ai_actor_constructor_args():
    sig = inspect.signature(Computer_AI_Actor.__init__)
    params = list(sig.parameters.keys())



def test_player_1_actor_is_not_abstract():
    assert not inspect.isabstract(Player_1_Actor)


def test_player_1_actor_constructor_exists():
    assert callable(Player_1_Actor.__init__)


def test_player_1_actor_constructor_args():
    sig = inspect.signature(Player_1_Actor.__init__)
    params = list(sig.parameters.keys())



def test_javax_swing_jtextfield_is_not_abstract():
    assert not inspect.isabstract(javax_swing_JTextField)


def test_javax_swing_jtextfield_constructor_exists():
    assert callable(javax_swing_JTextField.__init__)


def test_javax_swing_jtextfield_constructor_args():
    sig = inspect.signature(javax_swing_JTextField.__init__)
    params = list(sig.parameters.keys())



def test_javax_swing_jbutton_is_not_abstract():
    assert not inspect.isabstract(javax_swing_JButton)


def test_javax_swing_jbutton_constructor_exists():
    assert callable(javax_swing_JButton.__init__)


def test_javax_swing_jbutton_constructor_args():
    sig = inspect.signature(javax_swing_JButton.__init__)
    params = list(sig.parameters.keys())


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
ImageIcon_strategy = st.builds(
    ImageIcon,
)
Listener_Interface_strategy = st.builds(
    Listener_Interface,
)
Player_strategy = st.builds(
    Player,
)
connect_four_gui_Circle_strategy = st.builds(
    connect_four_gui_Circle,
)
connect_four_gui_Connect4Constant_Interface_strategy = st.builds(
    connect_four_gui_Connect4Constant_Interface,
)
connect_four_gui_GameOverPanel_strategy = st.builds(
    connect_four_gui_GameOverPanel,
    winner=
        safe_text,
    winnerDisplay=
        safe_text,
    butPlayAgain=
        st.none(),
    gui=
        st.none(),
    labelGameOVer=
        safe_text,
    butMainMenu=
        st.none()
)
connect_four_gui_stage_strategy = st.builds(
    connect_four_gui_stage,
)
connect_four_gui_StartMenu_strategy = st.builds(
    connect_four_gui_StartMenu,
    bStart=
        st.none(),
    bPlay=
        st.none(),
    startLabel=
        st.none(),
    bp=
        st.none(),
    label=
        st.none(),
    window=
        safe_text
)
connect_four_gui_GUIPlayer_strategy = st.builds(
    connect_four_gui_GUIPlayer,
    board=
        safe_text,
    gpGUI=
        st.none(),
    m_name=
        safe_text
)
connect_four_gui_red_strategy = st.builds(
    connect_four_gui_red,
)
connect_four_gui_Token_strategy = st.builds(
    connect_four_gui_Token,
    X=
        safe_text,
    Y=
        safe_text,
    red=
        st.booleans()
)
connect_four_gui_Connect4GUI_strategy = st.builds(
    connect_four_gui_Connect4GUI,
    redToken=
        st.booleans(),
    startUp=
        safe_text,
    window=
        safe_text,
    cpList=
        st.none(),
    comp=
        st.booleans(),
    gridBoard=
        safe_text,
    tokenRoot=
        safe_text
)
connect_four_gui_GamePanel_strategy = st.builds(
    connect_four_gui_GamePanel,
    newColumnNum=
        st.integers(),
    board=
        safe_text,
    game=
        safe_text,
    pieces=
        safe_text,
    players=
        safe_text,
    isComputerEnabled=
        st.booleans(),
    windows=
        safe_text,
    justWon=
        st.booleans(),
    whoPlayed=
        st.integers(),
    startUp=
        safe_text,
    columnNum=
        st.integers(),
    newDrawPos=
        st.integers(),
    Connect4_GUI=
        st.none(),
    turnNum=
        st.integers()
)
Compute_Column_external_strategy = st.builds(
    Compute_Column_external,
)
Select_Column_external_strategy = st.builds(
    Select_Column_external,
)
Enter_Name_external_strategy = st.builds(
    Enter_Name_external,
)
Choose_how_many_Players_external_strategy = st.builds(
    Choose_how_many_Players_external,
)
BorderPane_strategy = st.builds(
    BorderPane,
)
VBox_strategy = st.builds(
    VBox,
)
HBox_strategy = st.builds(
    HBox,
)
Button_strategy = st.builds(
    Button,
)
Label_strategy = st.builds(
    Label,
)
List_Token__strategy = st.builds(
    List_Token_,
)
Connect_Four_Component_strategy = st.builds(
    Connect_Four_Component,
)
Player_2_Actor_strategy = st.builds(
    Player_2_Actor,
)
Computer_AI_Actor_strategy = st.builds(
    Computer_AI_Actor,
)
Player_1_Actor_strategy = st.builds(
    Player_1_Actor,
)
javax_swing_JTextField_strategy = st.builds(
    javax_swing_JTextField,
)
javax_swing_JButton_strategy = st.builds(
    javax_swing_JButton,
)

@given(instance=ImageIcon_strategy)
@settings(max_examples=50)
def test_imageicon_instantiation(instance):
    assert isinstance(instance, ImageIcon)

@given(instance=Listener_Interface_strategy)
@settings(max_examples=50)
def test_listener_interface_instantiation(instance):
    assert isinstance(instance, Listener_Interface)

@given(instance=Player_strategy)
@settings(max_examples=50)
def test_player_instantiation(instance):
    assert isinstance(instance, Player)

@given(instance=connect_four_gui_Circle_strategy)
@settings(max_examples=50)
def test_connect_four_gui_circle_instantiation(instance):
    assert isinstance(instance, connect_four_gui_Circle)

@given(instance=connect_four_gui_Connect4Constant_Interface_strategy)
@settings(max_examples=50)
def test_connect_four_gui_connect4constant_interface_instantiation(instance):
    assert isinstance(instance, connect_four_gui_Connect4Constant_Interface)

@given(instance=connect_four_gui_GameOverPanel_strategy)
@settings(max_examples=50)
def test_connect_four_gui_gameoverpanel_instantiation(instance):
    assert isinstance(instance, connect_four_gui_GameOverPanel)



@given(instance=connect_four_gui_GameOverPanel_strategy)
def test_connect_four_gui_gameoverpanel_winner_setter(instance):
    original = instance.winner
    instance.winner = original
    assert instance.winner == original



@given(instance=connect_four_gui_GameOverPanel_strategy)
def test_connect_four_gui_gameoverpanel_winnerDisplay_setter(instance):
    original = instance.winnerDisplay
    instance.winnerDisplay = original
    assert instance.winnerDisplay == original



@given(instance=connect_four_gui_GameOverPanel_strategy)
def test_connect_four_gui_gameoverpanel_butPlayAgain_setter(instance):
    original = instance.butPlayAgain
    instance.butPlayAgain = original
    assert instance.butPlayAgain == original



@given(instance=connect_four_gui_GameOverPanel_strategy)
def test_connect_four_gui_gameoverpanel_gui_setter(instance):
    original = instance.gui
    instance.gui = original
    assert instance.gui == original



@given(instance=connect_four_gui_GameOverPanel_strategy)
def test_connect_four_gui_gameoverpanel_labelGameOVer_setter(instance):
    original = instance.labelGameOVer
    instance.labelGameOVer = original
    assert instance.labelGameOVer == original



@given(instance=connect_four_gui_GameOverPanel_strategy)
def test_connect_four_gui_gameoverpanel_butMainMenu_setter(instance):
    original = instance.butMainMenu
    instance.butMainMenu = original
    assert instance.butMainMenu == original

@given(instance=connect_four_gui_stage_strategy)
@settings(max_examples=50)
def test_connect_four_gui_stage_instantiation(instance):
    assert isinstance(instance, connect_four_gui_stage)

@given(instance=connect_four_gui_StartMenu_strategy)
@settings(max_examples=50)
def test_connect_four_gui_startmenu_instantiation(instance):
    assert isinstance(instance, connect_four_gui_StartMenu)



@given(instance=connect_four_gui_StartMenu_strategy)
def test_connect_four_gui_startmenu_bStart_setter(instance):
    original = instance.bStart
    instance.bStart = original
    assert instance.bStart == original



@given(instance=connect_four_gui_StartMenu_strategy)
def test_connect_four_gui_startmenu_bPlay_setter(instance):
    original = instance.bPlay
    instance.bPlay = original
    assert instance.bPlay == original



@given(instance=connect_four_gui_StartMenu_strategy)
def test_connect_four_gui_startmenu_startLabel_setter(instance):
    original = instance.startLabel
    instance.startLabel = original
    assert instance.startLabel == original



@given(instance=connect_four_gui_StartMenu_strategy)
def test_connect_four_gui_startmenu_bp_setter(instance):
    original = instance.bp
    instance.bp = original
    assert instance.bp == original



@given(instance=connect_four_gui_StartMenu_strategy)
def test_connect_four_gui_startmenu_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=connect_four_gui_StartMenu_strategy)
def test_connect_four_gui_startmenu_window_setter(instance):
    original = instance.window
    instance.window = original
    assert instance.window == original

@given(instance=connect_four_gui_GUIPlayer_strategy)
@settings(max_examples=50)
def test_connect_four_gui_guiplayer_instantiation(instance):
    assert isinstance(instance, connect_four_gui_GUIPlayer)



@given(instance=connect_four_gui_GUIPlayer_strategy)
def test_connect_four_gui_guiplayer_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original



@given(instance=connect_four_gui_GUIPlayer_strategy)
def test_connect_four_gui_guiplayer_gpGUI_setter(instance):
    original = instance.gpGUI
    instance.gpGUI = original
    assert instance.gpGUI == original



@given(instance=connect_four_gui_GUIPlayer_strategy)
def test_connect_four_gui_guiplayer_m_name_setter(instance):
    original = instance.m_name
    instance.m_name = original
    assert instance.m_name == original

@given(instance=connect_four_gui_red_strategy)
@settings(max_examples=50)
def test_connect_four_gui_red_instantiation(instance):
    assert isinstance(instance, connect_four_gui_red)

@given(instance=connect_four_gui_Token_strategy)
@settings(max_examples=50)
def test_connect_four_gui_token_instantiation(instance):
    assert isinstance(instance, connect_four_gui_Token)



@given(instance=connect_four_gui_Token_strategy)
def test_connect_four_gui_token_X_setter(instance):
    original = instance.X
    instance.X = original
    assert instance.X == original



@given(instance=connect_four_gui_Token_strategy)
def test_connect_four_gui_token_Y_setter(instance):
    original = instance.Y
    instance.Y = original
    assert instance.Y == original



@given(instance=connect_four_gui_Token_strategy)
def test_connect_four_gui_token_red_setter(instance):
    original = instance.red
    instance.red = original
    assert instance.red == original

@given(instance=connect_four_gui_Connect4GUI_strategy)
@settings(max_examples=50)
def test_connect_four_gui_connect4gui_instantiation(instance):
    assert isinstance(instance, connect_four_gui_Connect4GUI)



@given(instance=connect_four_gui_Connect4GUI_strategy)
def test_connect_four_gui_connect4gui_redToken_setter(instance):
    original = instance.redToken
    instance.redToken = original
    assert instance.redToken == original



@given(instance=connect_four_gui_Connect4GUI_strategy)
def test_connect_four_gui_connect4gui_startUp_setter(instance):
    original = instance.startUp
    instance.startUp = original
    assert instance.startUp == original



@given(instance=connect_four_gui_Connect4GUI_strategy)
def test_connect_four_gui_connect4gui_window_setter(instance):
    original = instance.window
    instance.window = original
    assert instance.window == original



@given(instance=connect_four_gui_Connect4GUI_strategy)
def test_connect_four_gui_connect4gui_cpList_setter(instance):
    original = instance.cpList
    instance.cpList = original
    assert instance.cpList == original



@given(instance=connect_four_gui_Connect4GUI_strategy)
def test_connect_four_gui_connect4gui_comp_setter(instance):
    original = instance.comp
    instance.comp = original
    assert instance.comp == original



@given(instance=connect_four_gui_Connect4GUI_strategy)
def test_connect_four_gui_connect4gui_gridBoard_setter(instance):
    original = instance.gridBoard
    instance.gridBoard = original
    assert instance.gridBoard == original



@given(instance=connect_four_gui_Connect4GUI_strategy)
def test_connect_four_gui_connect4gui_tokenRoot_setter(instance):
    original = instance.tokenRoot
    instance.tokenRoot = original
    assert instance.tokenRoot == original

@given(instance=connect_four_gui_GamePanel_strategy)
@settings(max_examples=50)
def test_connect_four_gui_gamepanel_instantiation(instance):
    assert isinstance(instance, connect_four_gui_GamePanel)



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_newColumnNum_setter(instance):
    original = instance.newColumnNum
    instance.newColumnNum = original
    assert instance.newColumnNum == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_game_setter(instance):
    original = instance.game
    instance.game = original
    assert instance.game == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_pieces_setter(instance):
    original = instance.pieces
    instance.pieces = original
    assert instance.pieces == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_isComputerEnabled_setter(instance):
    original = instance.isComputerEnabled
    instance.isComputerEnabled = original
    assert instance.isComputerEnabled == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_windows_setter(instance):
    original = instance.windows
    instance.windows = original
    assert instance.windows == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_justWon_setter(instance):
    original = instance.justWon
    instance.justWon = original
    assert instance.justWon == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_whoPlayed_setter(instance):
    original = instance.whoPlayed
    instance.whoPlayed = original
    assert instance.whoPlayed == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_startUp_setter(instance):
    original = instance.startUp
    instance.startUp = original
    assert instance.startUp == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_columnNum_setter(instance):
    original = instance.columnNum
    instance.columnNum = original
    assert instance.columnNum == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_newDrawPos_setter(instance):
    original = instance.newDrawPos
    instance.newDrawPos = original
    assert instance.newDrawPos == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_Connect4_GUI_setter(instance):
    original = instance.Connect4_GUI
    instance.Connect4_GUI = original
    assert instance.Connect4_GUI == original



@given(instance=connect_four_gui_GamePanel_strategy)
def test_connect_four_gui_gamepanel_turnNum_setter(instance):
    original = instance.turnNum
    instance.turnNum = original
    assert instance.turnNum == original

@given(instance=Compute_Column_external_strategy)
@settings(max_examples=50)
def test_compute_column_external_instantiation(instance):
    assert isinstance(instance, Compute_Column_external)

@given(instance=Select_Column_external_strategy)
@settings(max_examples=50)
def test_select_column_external_instantiation(instance):
    assert isinstance(instance, Select_Column_external)

@given(instance=Enter_Name_external_strategy)
@settings(max_examples=50)
def test_enter_name_external_instantiation(instance):
    assert isinstance(instance, Enter_Name_external)

@given(instance=Choose_how_many_Players_external_strategy)
@settings(max_examples=50)
def test_choose_how_many_players_external_instantiation(instance):
    assert isinstance(instance, Choose_how_many_Players_external)

@given(instance=BorderPane_strategy)
@settings(max_examples=50)
def test_borderpane_instantiation(instance):
    assert isinstance(instance, BorderPane)

@given(instance=VBox_strategy)
@settings(max_examples=50)
def test_vbox_instantiation(instance):
    assert isinstance(instance, VBox)

@given(instance=HBox_strategy)
@settings(max_examples=50)
def test_hbox_instantiation(instance):
    assert isinstance(instance, HBox)

@given(instance=Button_strategy)
@settings(max_examples=50)
def test_button_instantiation(instance):
    assert isinstance(instance, Button)

@given(instance=Label_strategy)
@settings(max_examples=50)
def test_label_instantiation(instance):
    assert isinstance(instance, Label)

@given(instance=List_Token__strategy)
@settings(max_examples=50)
def test_list_token__instantiation(instance):
    assert isinstance(instance, List_Token_)

@given(instance=Connect_Four_Component_strategy)
@settings(max_examples=50)
def test_connect_four_component_instantiation(instance):
    assert isinstance(instance, Connect_Four_Component)

@given(instance=Player_2_Actor_strategy)
@settings(max_examples=50)
def test_player_2_actor_instantiation(instance):
    assert isinstance(instance, Player_2_Actor)

@given(instance=Computer_AI_Actor_strategy)
@settings(max_examples=50)
def test_computer_ai_actor_instantiation(instance):
    assert isinstance(instance, Computer_AI_Actor)

@given(instance=Player_1_Actor_strategy)
@settings(max_examples=50)
def test_player_1_actor_instantiation(instance):
    assert isinstance(instance, Player_1_Actor)

@given(instance=javax_swing_JTextField_strategy)
@settings(max_examples=50)
def test_javax_swing_jtextfield_instantiation(instance):
    assert isinstance(instance, javax_swing_JTextField)

@given(instance=javax_swing_JButton_strategy)
@settings(max_examples=50)
def test_javax_swing_jbutton_instantiation(instance):
    assert isinstance(instance, javax_swing_JButton)
