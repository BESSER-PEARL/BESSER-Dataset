import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Computer_Player_1_Actor,
    Human_Player_2_Actor,
    Human_Player_1_Actor,
    Checkers_Close_or_Exit_Game_UseCase,
    Checkers_Move_Game_Pieces_UseCase,
    Checkers_Start_New_Game_UseCase,
    Checkers_Select__Player_Mode__UseCase,
    Checkers_Select__Difficulty_Level__UseCase,
    Checkers_Toggle__Sound__UseCase,
    Checkers_Select__Help__UseCase,
    Checkers_Start_the_Game_GUI_UseCase,
    genmymodelreverse_java_lang_Exception,
    genmymodelreverse_javax_swing_JScrollPane,
    genmymodelreverse_java_awt_event_MouseEvent,
    genmymodelreverse_java_awt_event_ItemEvent,
    genmymodelreverse_java_awt_Point,
    genmymodelreverse_javax_swing_JComboBox,
    genmymodelreverse_javax_swing_JLabel,
    genmymodelreverse_javax_swing_JRadioButton,
    genmymodelreverse_javax_swing_ButtonGroup,
    genmymodelreverse_javax_swing_ImageIcon,
    genmymodelreverse_javax_swing_JTextArea,
    genmymodelreverse_java_awt_Graphics,
    genmymodelreverse_javax_swing_JButton,
    genmymodelreverse_java_lang_Thread,
    genmymodelreverse_javax_swing_JDialog,
    genmymodelreverse_java_awt_event_MouseListener_Interface,
    genmymodelreverse_java_awt_event_MouseMotionListener_Interface,
    genmymodelreverse_java_awt_event_ItemListener_Interface,
    genmymodelreverse_javax_swing_JPanel,
    genmymodelreverse_java_util_Vector,
    genmymodelreverse_javax_swing_JFrame,
    genmymodelreverse_java_awt_event_ActionEvent,
    checkers_CheckerFrame,
    checkers_GameEngine,
    checkers_StartPanel,
    checkers_PlaySound,
    checkers_IntelliChecker,
    checkers_Help,
    checkers_GameWin,
    checkers_Checkers,
    checkers_CheckerMove,
    checkers_Position,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_computer_player_1_actor_is_not_abstract():
    assert not inspect.isabstract(Computer_Player_1_Actor)


def test_computer_player_1_actor_constructor_exists():
    assert callable(Computer_Player_1_Actor.__init__)


def test_computer_player_1_actor_constructor_args():
    sig = inspect.signature(Computer_Player_1_Actor.__init__)
    params = list(sig.parameters.keys())



def test_human_player_2_actor_is_not_abstract():
    assert not inspect.isabstract(Human_Player_2_Actor)


def test_human_player_2_actor_constructor_exists():
    assert callable(Human_Player_2_Actor.__init__)


def test_human_player_2_actor_constructor_args():
    sig = inspect.signature(Human_Player_2_Actor.__init__)
    params = list(sig.parameters.keys())



def test_human_player_1_actor_is_not_abstract():
    assert not inspect.isabstract(Human_Player_1_Actor)


def test_human_player_1_actor_constructor_exists():
    assert callable(Human_Player_1_Actor.__init__)


def test_human_player_1_actor_constructor_args():
    sig = inspect.signature(Human_Player_1_Actor.__init__)
    params = list(sig.parameters.keys())



def test_checkers_close_or_exit_game_usecase_is_not_abstract():
    assert not inspect.isabstract(Checkers_Close_or_Exit_Game_UseCase)


def test_checkers_close_or_exit_game_usecase_constructor_exists():
    assert callable(Checkers_Close_or_Exit_Game_UseCase.__init__)


def test_checkers_close_or_exit_game_usecase_constructor_args():
    sig = inspect.signature(Checkers_Close_or_Exit_Game_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_checkers_move_game_pieces_usecase_is_not_abstract():
    assert not inspect.isabstract(Checkers_Move_Game_Pieces_UseCase)


def test_checkers_move_game_pieces_usecase_constructor_exists():
    assert callable(Checkers_Move_Game_Pieces_UseCase.__init__)


def test_checkers_move_game_pieces_usecase_constructor_args():
    sig = inspect.signature(Checkers_Move_Game_Pieces_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_checkers_start_new_game_usecase_is_not_abstract():
    assert not inspect.isabstract(Checkers_Start_New_Game_UseCase)


def test_checkers_start_new_game_usecase_constructor_exists():
    assert callable(Checkers_Start_New_Game_UseCase.__init__)


def test_checkers_start_new_game_usecase_constructor_args():
    sig = inspect.signature(Checkers_Start_New_Game_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_checkers_select__player_mode__usecase_is_not_abstract():
    assert not inspect.isabstract(Checkers_Select__Player_Mode__UseCase)


def test_checkers_select__player_mode__usecase_constructor_exists():
    assert callable(Checkers_Select__Player_Mode__UseCase.__init__)


def test_checkers_select__player_mode__usecase_constructor_args():
    sig = inspect.signature(Checkers_Select__Player_Mode__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_checkers_select__difficulty_level__usecase_is_not_abstract():
    assert not inspect.isabstract(Checkers_Select__Difficulty_Level__UseCase)


def test_checkers_select__difficulty_level__usecase_constructor_exists():
    assert callable(Checkers_Select__Difficulty_Level__UseCase.__init__)


def test_checkers_select__difficulty_level__usecase_constructor_args():
    sig = inspect.signature(Checkers_Select__Difficulty_Level__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_checkers_toggle__sound__usecase_is_not_abstract():
    assert not inspect.isabstract(Checkers_Toggle__Sound__UseCase)


def test_checkers_toggle__sound__usecase_constructor_exists():
    assert callable(Checkers_Toggle__Sound__UseCase.__init__)


def test_checkers_toggle__sound__usecase_constructor_args():
    sig = inspect.signature(Checkers_Toggle__Sound__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_checkers_select__help__usecase_is_not_abstract():
    assert not inspect.isabstract(Checkers_Select__Help__UseCase)


def test_checkers_select__help__usecase_constructor_exists():
    assert callable(Checkers_Select__Help__UseCase.__init__)


def test_checkers_select__help__usecase_constructor_args():
    sig = inspect.signature(Checkers_Select__Help__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_checkers_start_the_game_gui_usecase_is_not_abstract():
    assert not inspect.isabstract(Checkers_Start_the_Game_GUI_UseCase)


def test_checkers_start_the_game_gui_usecase_constructor_exists():
    assert callable(Checkers_Start_the_Game_GUI_UseCase.__init__)


def test_checkers_start_the_game_gui_usecase_constructor_args():
    sig = inspect.signature(Checkers_Start_the_Game_GUI_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_lang_exception_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Exception)


def test_genmymodelreverse_java_lang_exception_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Exception.__init__)


def test_genmymodelreverse_java_lang_exception_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Exception.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jscrollpane_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JScrollPane)


def test_genmymodelreverse_javax_swing_jscrollpane_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JScrollPane.__init__)


def test_genmymodelreverse_javax_swing_jscrollpane_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JScrollPane.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_mouseevent_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_MouseEvent)


def test_genmymodelreverse_java_awt_event_mouseevent_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_MouseEvent.__init__)


def test_genmymodelreverse_java_awt_event_mouseevent_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_MouseEvent.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_itemevent_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_ItemEvent)


def test_genmymodelreverse_java_awt_event_itemevent_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_ItemEvent.__init__)


def test_genmymodelreverse_java_awt_event_itemevent_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_ItemEvent.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_point_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_Point)


def test_genmymodelreverse_java_awt_point_constructor_exists():
    assert callable(genmymodelreverse_java_awt_Point.__init__)


def test_genmymodelreverse_java_awt_point_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_Point.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jcombobox_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JComboBox)


def test_genmymodelreverse_javax_swing_jcombobox_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JComboBox.__init__)


def test_genmymodelreverse_javax_swing_jcombobox_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JComboBox.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jlabel_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JLabel)


def test_genmymodelreverse_javax_swing_jlabel_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JLabel.__init__)


def test_genmymodelreverse_javax_swing_jlabel_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JLabel.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jradiobutton_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JRadioButton)


def test_genmymodelreverse_javax_swing_jradiobutton_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JRadioButton.__init__)


def test_genmymodelreverse_javax_swing_jradiobutton_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JRadioButton.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_buttongroup_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_ButtonGroup)


def test_genmymodelreverse_javax_swing_buttongroup_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_ButtonGroup.__init__)


def test_genmymodelreverse_javax_swing_buttongroup_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_ButtonGroup.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_imageicon_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_ImageIcon)


def test_genmymodelreverse_javax_swing_imageicon_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_ImageIcon.__init__)


def test_genmymodelreverse_javax_swing_imageicon_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_ImageIcon.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jtextarea_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JTextArea)


def test_genmymodelreverse_javax_swing_jtextarea_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JTextArea.__init__)


def test_genmymodelreverse_javax_swing_jtextarea_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JTextArea.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_graphics_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_Graphics)


def test_genmymodelreverse_java_awt_graphics_constructor_exists():
    assert callable(genmymodelreverse_java_awt_Graphics.__init__)


def test_genmymodelreverse_java_awt_graphics_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jbutton_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JButton)


def test_genmymodelreverse_javax_swing_jbutton_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JButton.__init__)


def test_genmymodelreverse_javax_swing_jbutton_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JButton.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_lang_thread_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_lang_Thread)


def test_genmymodelreverse_java_lang_thread_constructor_exists():
    assert callable(genmymodelreverse_java_lang_Thread.__init__)


def test_genmymodelreverse_java_lang_thread_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_lang_Thread.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jdialog_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JDialog)


def test_genmymodelreverse_javax_swing_jdialog_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JDialog.__init__)


def test_genmymodelreverse_javax_swing_jdialog_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JDialog.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_mouselistener_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_MouseListener_Interface)


def test_genmymodelreverse_java_awt_event_mouselistener_interface_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_MouseListener_Interface.__init__)


def test_genmymodelreverse_java_awt_event_mouselistener_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_MouseListener_Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_mousemotionlistener_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_MouseMotionListener_Interface)


def test_genmymodelreverse_java_awt_event_mousemotionlistener_interface_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_MouseMotionListener_Interface.__init__)


def test_genmymodelreverse_java_awt_event_mousemotionlistener_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_MouseMotionListener_Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_itemlistener_interface_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_ItemListener_Interface)


def test_genmymodelreverse_java_awt_event_itemlistener_interface_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_ItemListener_Interface.__init__)


def test_genmymodelreverse_java_awt_event_itemlistener_interface_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_ItemListener_Interface.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jpanel_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JPanel)


def test_genmymodelreverse_javax_swing_jpanel_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JPanel.__init__)


def test_genmymodelreverse_javax_swing_jpanel_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JPanel.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_util_vector_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_util_Vector)


def test_genmymodelreverse_java_util_vector_constructor_exists():
    assert callable(genmymodelreverse_java_util_Vector.__init__)


def test_genmymodelreverse_java_util_vector_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_util_Vector.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jframe_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JFrame)


def test_genmymodelreverse_javax_swing_jframe_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JFrame.__init__)


def test_genmymodelreverse_javax_swing_jframe_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JFrame.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_actionevent_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_ActionEvent)


def test_genmymodelreverse_java_awt_event_actionevent_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_ActionEvent.__init__)


def test_genmymodelreverse_java_awt_event_actionevent_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_ActionEvent.__init__)
    params = list(sig.parameters.keys())



def test_checkers_checkerframe_is_not_abstract():
    assert not inspect.isabstract(checkers_CheckerFrame)


def test_checkers_checkerframe_constructor_exists():
    assert callable(checkers_CheckerFrame.__init__)


def test_checkers_checkerframe_constructor_args():
    sig = inspect.signature(checkers_CheckerFrame.__init__)
    params = list(sig.parameters.keys())
    assert "startButton" in params, "Missing parameter 'startButton'"
    assert "gamePanel" in params, "Missing parameter 'gamePanel'"

def test_checkers_checkerframe_has_startButton():
    assert hasattr(checkers_CheckerFrame, "startButton")
    descriptor = None
    for klass in checkers_CheckerFrame.__mro__:
        if "startButton" in klass.__dict__:
            descriptor = klass.__dict__["startButton"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkerframe_has_gamePanel():
    assert hasattr(checkers_CheckerFrame, "gamePanel")
    descriptor = None
    for klass in checkers_CheckerFrame.__mro__:
        if "gamePanel" in klass.__dict__:
            descriptor = klass.__dict__["gamePanel"]
            break
    assert isinstance(descriptor, property)



def test_checkers_gameengine_is_not_abstract():
    assert not inspect.isabstract(checkers_GameEngine)


def test_checkers_gameengine_constructor_exists():
    assert callable(checkers_GameEngine.__init__)


def test_checkers_gameengine_constructor_args():
    sig = inspect.signature(checkers_GameEngine.__init__)
    params = list(sig.parameters.keys())
    assert "edge" in params, "Missing parameter 'edge'"
    assert "inf" in params, "Missing parameter 'inf'"
    assert "normal" in params, "Missing parameter 'normal'"
    assert "king" in params, "Missing parameter 'king'"
    assert "pos" in params, "Missing parameter 'pos'"

def test_checkers_gameengine_has_edge():
    assert hasattr(checkers_GameEngine, "edge")
    descriptor = None
    for klass in checkers_GameEngine.__mro__:
        if "edge" in klass.__dict__:
            descriptor = klass.__dict__["edge"]
            break
    assert isinstance(descriptor, property)

def test_checkers_gameengine_has_inf():
    assert hasattr(checkers_GameEngine, "inf")
    descriptor = None
    for klass in checkers_GameEngine.__mro__:
        if "inf" in klass.__dict__:
            descriptor = klass.__dict__["inf"]
            break
    assert isinstance(descriptor, property)

def test_checkers_gameengine_has_normal():
    assert hasattr(checkers_GameEngine, "normal")
    descriptor = None
    for klass in checkers_GameEngine.__mro__:
        if "normal" in klass.__dict__:
            descriptor = klass.__dict__["normal"]
            break
    assert isinstance(descriptor, property)

def test_checkers_gameengine_has_king():
    assert hasattr(checkers_GameEngine, "king")
    descriptor = None
    for klass in checkers_GameEngine.__mro__:
        if "king" in klass.__dict__:
            descriptor = klass.__dict__["king"]
            break
    assert isinstance(descriptor, property)

def test_checkers_gameengine_has_pos():
    assert hasattr(checkers_GameEngine, "pos")
    descriptor = None
    for klass in checkers_GameEngine.__mro__:
        if "pos" in klass.__dict__:
            descriptor = klass.__dict__["pos"]
            break
    assert isinstance(descriptor, property)



def test_checkers_startpanel_is_not_abstract():
    assert not inspect.isabstract(checkers_StartPanel)


def test_checkers_startpanel_constructor_exists():
    assert callable(checkers_StartPanel.__init__)


def test_checkers_startpanel_constructor_args():
    sig = inspect.signature(checkers_StartPanel.__init__)
    params = list(sig.parameters.keys())



def test_checkers_playsound_is_not_abstract():
    assert not inspect.isabstract(checkers_PlaySound)


def test_checkers_playsound_constructor_exists():
    assert callable(checkers_PlaySound.__init__)


def test_checkers_playsound_constructor_args():
    sig = inspect.signature(checkers_PlaySound.__init__)
    params = list(sig.parameters.keys())
    assert "EXTERNAL_BUFFER_SIZE" in params, "Missing parameter 'EXTERNAL_BUFFER_SIZE'"
    assert "filename" in params, "Missing parameter 'filename'"

def test_checkers_playsound_has_EXTERNAL_BUFFER_SIZE():
    assert hasattr(checkers_PlaySound, "EXTERNAL_BUFFER_SIZE")
    descriptor = None
    for klass in checkers_PlaySound.__mro__:
        if "EXTERNAL_BUFFER_SIZE" in klass.__dict__:
            descriptor = klass.__dict__["EXTERNAL_BUFFER_SIZE"]
            break
    assert isinstance(descriptor, property)

def test_checkers_playsound_has_filename():
    assert hasattr(checkers_PlaySound, "filename")
    descriptor = None
    for klass in checkers_PlaySound.__mro__:
        if "filename" in klass.__dict__:
            descriptor = klass.__dict__["filename"]
            break
    assert isinstance(descriptor, property)



def test_checkers_intellichecker_is_not_abstract():
    assert not inspect.isabstract(checkers_IntelliChecker)


def test_checkers_intellichecker_constructor_exists():
    assert callable(checkers_IntelliChecker.__init__)


def test_checkers_intellichecker_constructor_args():
    sig = inspect.signature(checkers_IntelliChecker.__init__)
    params = list(sig.parameters.keys())



def test_checkers_help_is_not_abstract():
    assert not inspect.isabstract(checkers_Help)


def test_checkers_help_constructor_exists():
    assert callable(checkers_Help.__init__)


def test_checkers_help_constructor_args():
    sig = inspect.signature(checkers_Help.__init__)
    params = list(sig.parameters.keys())
    assert "txt" in params, "Missing parameter 'txt'"
    assert "hlp" in params, "Missing parameter 'hlp'"

def test_checkers_help_has_txt():
    assert hasattr(checkers_Help, "txt")
    descriptor = None
    for klass in checkers_Help.__mro__:
        if "txt" in klass.__dict__:
            descriptor = klass.__dict__["txt"]
            break
    assert isinstance(descriptor, property)

def test_checkers_help_has_hlp():
    assert hasattr(checkers_Help, "hlp")
    descriptor = None
    for klass in checkers_Help.__mro__:
        if "hlp" in klass.__dict__:
            descriptor = klass.__dict__["hlp"]
            break
    assert isinstance(descriptor, property)



def test_checkers_gamewin_is_not_abstract():
    assert not inspect.isabstract(checkers_GameWin)


def test_checkers_gamewin_constructor_exists():
    assert callable(checkers_GameWin.__init__)


def test_checkers_gamewin_constructor_args():
    sig = inspect.signature(checkers_GameWin.__init__)
    params = list(sig.parameters.keys())
    assert "masseage" in params, "Missing parameter 'masseage'"
    assert "p" in params, "Missing parameter 'p'"

def test_checkers_gamewin_has_masseage():
    assert hasattr(checkers_GameWin, "masseage")
    descriptor = None
    for klass in checkers_GameWin.__mro__:
        if "masseage" in klass.__dict__:
            descriptor = klass.__dict__["masseage"]
            break
    assert isinstance(descriptor, property)

def test_checkers_gamewin_has_p():
    assert hasattr(checkers_GameWin, "p")
    descriptor = None
    for klass in checkers_GameWin.__mro__:
        if "p" in klass.__dict__:
            descriptor = klass.__dict__["p"]
            break
    assert isinstance(descriptor, property)



def test_checkers_checkers_is_not_abstract():
    assert not inspect.isabstract(checkers_Checkers)


def test_checkers_checkers_constructor_exists():
    assert callable(checkers_Checkers.__init__)


def test_checkers_checkers_constructor_args():
    sig = inspect.signature(checkers_Checkers.__init__)
    params = list(sig.parameters.keys())
    assert "toMove" in params, "Missing parameter 'toMove'"
    assert "redK" in params, "Missing parameter 'redK'"
    assert "board" in params, "Missing parameter 'board'"
    assert "hlp" in params, "Missing parameter 'hlp'"
    assert "yellowKing" in params, "Missing parameter 'yellowKing'"
    assert "undoCount" in params, "Missing parameter 'undoCount'"
    assert "selectedColor" in params, "Missing parameter 'selectedColor'"
    assert "preBoard3" in params, "Missing parameter 'preBoard3'"
    assert "rk" in params, "Missing parameter 'rk'"
    assert "empty" in params, "Missing parameter 'empty'"
    assert "yellowN" in params, "Missing parameter 'yellowN'"
    assert "colors" in params, "Missing parameter 'colors'"
    assert "preToMove3" in params, "Missing parameter 'preToMove3'"
    assert "rkt" in params, "Missing parameter 'rkt'"
    assert "bk" in params, "Missing parameter 'bk'"
    assert "won" in params, "Missing parameter 'won'"
    assert "snp" in params, "Missing parameter 'snp'"
    assert "rpt" in params, "Missing parameter 'rpt'"
    assert "rp" in params, "Missing parameter 'rp'"
    assert "preToMove2" in params, "Missing parameter 'preToMove2'"
    assert "msg" in params, "Missing parameter 'msg'"
    assert "currType" in params, "Missing parameter 'currType'"
    assert "yellowNormal" in params, "Missing parameter 'yellowNormal'"
    assert "redN" in params, "Missing parameter 'redN'"
    assert "winPoint" in params, "Missing parameter 'winPoint'"
    assert "mode" in params, "Missing parameter 'mode'"
    assert "endY" in params, "Missing parameter 'endY'"
    assert "preToMove1" in params, "Missing parameter 'preToMove1'"
    assert "redNormal" in params, "Missing parameter 'redNormal'"
    assert "bp" in params, "Missing parameter 'bp'"
    assert "preBoard2" in params, "Missing parameter 'preBoard2'"
    assert "highlight" in params, "Missing parameter 'highlight'"
    assert "p1" in params, "Missing parameter 'p1'"
    assert "snB" in params, "Missing parameter 'snB'"
    assert "g" in params, "Missing parameter 'g'"
    assert "incomplete" in params, "Missing parameter 'incomplete'"
    assert "c2" in params, "Missing parameter 'c2'"
    assert "nwB" in params, "Missing parameter 'nwB'"
    assert "diff" in params, "Missing parameter 'diff'"
    assert "bpt" in params, "Missing parameter 'bpt'"
    assert "preBoard1" in params, "Missing parameter 'preBoard1'"
    assert "selectedMode" in params, "Missing parameter 'selectedMode'"
    assert "hlpB" in params, "Missing parameter 'hlpB'"
    assert "silent" in params, "Missing parameter 'silent'"
    assert "difficulty" in params, "Missing parameter 'difficulty'"
    assert "mup" in params, "Missing parameter 'mup'"
    assert "c1" in params, "Missing parameter 'c1'"
    assert "bkt" in params, "Missing parameter 'bkt'"
    assert "loser" in params, "Missing parameter 'loser'"
    assert "p2" in params, "Missing parameter 'p2'"
    assert "col" in params, "Missing parameter 'col'"
    assert "yellowK" in params, "Missing parameter 'yellowK'"
    assert "level" in params, "Missing parameter 'level'"
    assert "movable" in params, "Missing parameter 'movable'"
    assert "redKing" in params, "Missing parameter 'redKing'"
    assert "unB" in params, "Missing parameter 'unB'"
    assert "players" in params, "Missing parameter 'players'"

def test_checkers_checkers_has_toMove():
    assert hasattr(checkers_Checkers, "toMove")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "toMove" in klass.__dict__:
            descriptor = klass.__dict__["toMove"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_redK():
    assert hasattr(checkers_Checkers, "redK")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "redK" in klass.__dict__:
            descriptor = klass.__dict__["redK"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_board():
    assert hasattr(checkers_Checkers, "board")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "board" in klass.__dict__:
            descriptor = klass.__dict__["board"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_hlp():
    assert hasattr(checkers_Checkers, "hlp")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "hlp" in klass.__dict__:
            descriptor = klass.__dict__["hlp"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_yellowKing():
    assert hasattr(checkers_Checkers, "yellowKing")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "yellowKing" in klass.__dict__:
            descriptor = klass.__dict__["yellowKing"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_undoCount():
    assert hasattr(checkers_Checkers, "undoCount")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "undoCount" in klass.__dict__:
            descriptor = klass.__dict__["undoCount"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_selectedColor():
    assert hasattr(checkers_Checkers, "selectedColor")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "selectedColor" in klass.__dict__:
            descriptor = klass.__dict__["selectedColor"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_preBoard3():
    assert hasattr(checkers_Checkers, "preBoard3")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "preBoard3" in klass.__dict__:
            descriptor = klass.__dict__["preBoard3"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_rk():
    assert hasattr(checkers_Checkers, "rk")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "rk" in klass.__dict__:
            descriptor = klass.__dict__["rk"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_empty():
    assert hasattr(checkers_Checkers, "empty")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "empty" in klass.__dict__:
            descriptor = klass.__dict__["empty"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_yellowN():
    assert hasattr(checkers_Checkers, "yellowN")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "yellowN" in klass.__dict__:
            descriptor = klass.__dict__["yellowN"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_colors():
    assert hasattr(checkers_Checkers, "colors")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "colors" in klass.__dict__:
            descriptor = klass.__dict__["colors"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_preToMove3():
    assert hasattr(checkers_Checkers, "preToMove3")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "preToMove3" in klass.__dict__:
            descriptor = klass.__dict__["preToMove3"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_rkt():
    assert hasattr(checkers_Checkers, "rkt")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "rkt" in klass.__dict__:
            descriptor = klass.__dict__["rkt"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_bk():
    assert hasattr(checkers_Checkers, "bk")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "bk" in klass.__dict__:
            descriptor = klass.__dict__["bk"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_won():
    assert hasattr(checkers_Checkers, "won")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "won" in klass.__dict__:
            descriptor = klass.__dict__["won"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_snp():
    assert hasattr(checkers_Checkers, "snp")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "snp" in klass.__dict__:
            descriptor = klass.__dict__["snp"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_rpt():
    assert hasattr(checkers_Checkers, "rpt")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "rpt" in klass.__dict__:
            descriptor = klass.__dict__["rpt"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_rp():
    assert hasattr(checkers_Checkers, "rp")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "rp" in klass.__dict__:
            descriptor = klass.__dict__["rp"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_preToMove2():
    assert hasattr(checkers_Checkers, "preToMove2")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "preToMove2" in klass.__dict__:
            descriptor = klass.__dict__["preToMove2"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_msg():
    assert hasattr(checkers_Checkers, "msg")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "msg" in klass.__dict__:
            descriptor = klass.__dict__["msg"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_currType():
    assert hasattr(checkers_Checkers, "currType")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "currType" in klass.__dict__:
            descriptor = klass.__dict__["currType"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_yellowNormal():
    assert hasattr(checkers_Checkers, "yellowNormal")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "yellowNormal" in klass.__dict__:
            descriptor = klass.__dict__["yellowNormal"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_redN():
    assert hasattr(checkers_Checkers, "redN")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "redN" in klass.__dict__:
            descriptor = klass.__dict__["redN"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_winPoint():
    assert hasattr(checkers_Checkers, "winPoint")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "winPoint" in klass.__dict__:
            descriptor = klass.__dict__["winPoint"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_mode():
    assert hasattr(checkers_Checkers, "mode")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "mode" in klass.__dict__:
            descriptor = klass.__dict__["mode"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_endY():
    assert hasattr(checkers_Checkers, "endY")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "endY" in klass.__dict__:
            descriptor = klass.__dict__["endY"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_preToMove1():
    assert hasattr(checkers_Checkers, "preToMove1")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "preToMove1" in klass.__dict__:
            descriptor = klass.__dict__["preToMove1"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_redNormal():
    assert hasattr(checkers_Checkers, "redNormal")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "redNormal" in klass.__dict__:
            descriptor = klass.__dict__["redNormal"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_bp():
    assert hasattr(checkers_Checkers, "bp")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "bp" in klass.__dict__:
            descriptor = klass.__dict__["bp"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_preBoard2():
    assert hasattr(checkers_Checkers, "preBoard2")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "preBoard2" in klass.__dict__:
            descriptor = klass.__dict__["preBoard2"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_highlight():
    assert hasattr(checkers_Checkers, "highlight")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "highlight" in klass.__dict__:
            descriptor = klass.__dict__["highlight"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_p1():
    assert hasattr(checkers_Checkers, "p1")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "p1" in klass.__dict__:
            descriptor = klass.__dict__["p1"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_snB():
    assert hasattr(checkers_Checkers, "snB")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "snB" in klass.__dict__:
            descriptor = klass.__dict__["snB"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_g():
    assert hasattr(checkers_Checkers, "g")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "g" in klass.__dict__:
            descriptor = klass.__dict__["g"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_incomplete():
    assert hasattr(checkers_Checkers, "incomplete")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "incomplete" in klass.__dict__:
            descriptor = klass.__dict__["incomplete"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_c2():
    assert hasattr(checkers_Checkers, "c2")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "c2" in klass.__dict__:
            descriptor = klass.__dict__["c2"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_nwB():
    assert hasattr(checkers_Checkers, "nwB")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "nwB" in klass.__dict__:
            descriptor = klass.__dict__["nwB"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_diff():
    assert hasattr(checkers_Checkers, "diff")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "diff" in klass.__dict__:
            descriptor = klass.__dict__["diff"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_bpt():
    assert hasattr(checkers_Checkers, "bpt")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "bpt" in klass.__dict__:
            descriptor = klass.__dict__["bpt"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_preBoard1():
    assert hasattr(checkers_Checkers, "preBoard1")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "preBoard1" in klass.__dict__:
            descriptor = klass.__dict__["preBoard1"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_selectedMode():
    assert hasattr(checkers_Checkers, "selectedMode")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "selectedMode" in klass.__dict__:
            descriptor = klass.__dict__["selectedMode"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_hlpB():
    assert hasattr(checkers_Checkers, "hlpB")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "hlpB" in klass.__dict__:
            descriptor = klass.__dict__["hlpB"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_silent():
    assert hasattr(checkers_Checkers, "silent")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "silent" in klass.__dict__:
            descriptor = klass.__dict__["silent"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_difficulty():
    assert hasattr(checkers_Checkers, "difficulty")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "difficulty" in klass.__dict__:
            descriptor = klass.__dict__["difficulty"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_mup():
    assert hasattr(checkers_Checkers, "mup")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "mup" in klass.__dict__:
            descriptor = klass.__dict__["mup"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_c1():
    assert hasattr(checkers_Checkers, "c1")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "c1" in klass.__dict__:
            descriptor = klass.__dict__["c1"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_bkt():
    assert hasattr(checkers_Checkers, "bkt")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "bkt" in klass.__dict__:
            descriptor = klass.__dict__["bkt"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_loser():
    assert hasattr(checkers_Checkers, "loser")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "loser" in klass.__dict__:
            descriptor = klass.__dict__["loser"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_p2():
    assert hasattr(checkers_Checkers, "p2")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "p2" in klass.__dict__:
            descriptor = klass.__dict__["p2"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_col():
    assert hasattr(checkers_Checkers, "col")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "col" in klass.__dict__:
            descriptor = klass.__dict__["col"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_yellowK():
    assert hasattr(checkers_Checkers, "yellowK")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "yellowK" in klass.__dict__:
            descriptor = klass.__dict__["yellowK"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_level():
    assert hasattr(checkers_Checkers, "level")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_movable():
    assert hasattr(checkers_Checkers, "movable")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "movable" in klass.__dict__:
            descriptor = klass.__dict__["movable"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_redKing():
    assert hasattr(checkers_Checkers, "redKing")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "redKing" in klass.__dict__:
            descriptor = klass.__dict__["redKing"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_unB():
    assert hasattr(checkers_Checkers, "unB")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "unB" in klass.__dict__:
            descriptor = klass.__dict__["unB"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkers_has_players():
    assert hasattr(checkers_Checkers, "players")
    descriptor = None
    for klass in checkers_Checkers.__mro__:
        if "players" in klass.__dict__:
            descriptor = klass.__dict__["players"]
            break
    assert isinstance(descriptor, property)



def test_checkers_checkermove_is_not_abstract():
    assert not inspect.isabstract(checkers_CheckerMove)


def test_checkers_checkermove_constructor_exists():
    assert callable(checkers_CheckerMove.__init__)


def test_checkers_checkermove_constructor_args():
    sig = inspect.signature(checkers_CheckerMove.__init__)
    params = list(sig.parameters.keys())
    assert "legalMove" in params, "Missing parameter 'legalMove'"
    assert "incompleteMove" in params, "Missing parameter 'incompleteMove'"
    assert "illegalMove" in params, "Missing parameter 'illegalMove'"

def test_checkers_checkermove_has_legalMove():
    assert hasattr(checkers_CheckerMove, "legalMove")
    descriptor = None
    for klass in checkers_CheckerMove.__mro__:
        if "legalMove" in klass.__dict__:
            descriptor = klass.__dict__["legalMove"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkermove_has_incompleteMove():
    assert hasattr(checkers_CheckerMove, "incompleteMove")
    descriptor = None
    for klass in checkers_CheckerMove.__mro__:
        if "incompleteMove" in klass.__dict__:
            descriptor = klass.__dict__["incompleteMove"]
            break
    assert isinstance(descriptor, property)

def test_checkers_checkermove_has_illegalMove():
    assert hasattr(checkers_CheckerMove, "illegalMove")
    descriptor = None
    for klass in checkers_CheckerMove.__mro__:
        if "illegalMove" in klass.__dict__:
            descriptor = klass.__dict__["illegalMove"]
            break
    assert isinstance(descriptor, property)

def test_checkers_position_exists():
    # Check that the Enumeration exists
    assert checkers_Position is not None

def test_checkers_position_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in checkers_Position]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in checkers_Position"


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
Computer_Player_1_Actor_strategy = st.builds(
    Computer_Player_1_Actor,
)
Human_Player_2_Actor_strategy = st.builds(
    Human_Player_2_Actor,
)
Human_Player_1_Actor_strategy = st.builds(
    Human_Player_1_Actor,
)
Checkers_Close_or_Exit_Game_UseCase_strategy = st.builds(
    Checkers_Close_or_Exit_Game_UseCase,
)
Checkers_Move_Game_Pieces_UseCase_strategy = st.builds(
    Checkers_Move_Game_Pieces_UseCase,
)
Checkers_Start_New_Game_UseCase_strategy = st.builds(
    Checkers_Start_New_Game_UseCase,
)
Checkers_Select__Player_Mode__UseCase_strategy = st.builds(
    Checkers_Select__Player_Mode__UseCase,
)
Checkers_Select__Difficulty_Level__UseCase_strategy = st.builds(
    Checkers_Select__Difficulty_Level__UseCase,
)
Checkers_Toggle__Sound__UseCase_strategy = st.builds(
    Checkers_Toggle__Sound__UseCase,
)
Checkers_Select__Help__UseCase_strategy = st.builds(
    Checkers_Select__Help__UseCase,
)
Checkers_Start_the_Game_GUI_UseCase_strategy = st.builds(
    Checkers_Start_the_Game_GUI_UseCase,
)
genmymodelreverse_java_lang_Exception_strategy = st.builds(
    genmymodelreverse_java_lang_Exception,
)
genmymodelreverse_javax_swing_JScrollPane_strategy = st.builds(
    genmymodelreverse_javax_swing_JScrollPane,
)
genmymodelreverse_java_awt_event_MouseEvent_strategy = st.builds(
    genmymodelreverse_java_awt_event_MouseEvent,
)
genmymodelreverse_java_awt_event_ItemEvent_strategy = st.builds(
    genmymodelreverse_java_awt_event_ItemEvent,
)
genmymodelreverse_java_awt_Point_strategy = st.builds(
    genmymodelreverse_java_awt_Point,
)
genmymodelreverse_javax_swing_JComboBox_strategy = st.builds(
    genmymodelreverse_javax_swing_JComboBox,
)
genmymodelreverse_javax_swing_JLabel_strategy = st.builds(
    genmymodelreverse_javax_swing_JLabel,
)
genmymodelreverse_javax_swing_JRadioButton_strategy = st.builds(
    genmymodelreverse_javax_swing_JRadioButton,
)
genmymodelreverse_javax_swing_ButtonGroup_strategy = st.builds(
    genmymodelreverse_javax_swing_ButtonGroup,
)
genmymodelreverse_javax_swing_ImageIcon_strategy = st.builds(
    genmymodelreverse_javax_swing_ImageIcon,
)
genmymodelreverse_javax_swing_JTextArea_strategy = st.builds(
    genmymodelreverse_javax_swing_JTextArea,
)
genmymodelreverse_java_awt_Graphics_strategy = st.builds(
    genmymodelreverse_java_awt_Graphics,
)
genmymodelreverse_javax_swing_JButton_strategy = st.builds(
    genmymodelreverse_javax_swing_JButton,
)
genmymodelreverse_java_lang_Thread_strategy = st.builds(
    genmymodelreverse_java_lang_Thread,
)
genmymodelreverse_javax_swing_JDialog_strategy = st.builds(
    genmymodelreverse_javax_swing_JDialog,
)
genmymodelreverse_java_awt_event_MouseListener_Interface_strategy = st.builds(
    genmymodelreverse_java_awt_event_MouseListener_Interface,
)
genmymodelreverse_java_awt_event_MouseMotionListener_Interface_strategy = st.builds(
    genmymodelreverse_java_awt_event_MouseMotionListener_Interface,
)
genmymodelreverse_java_awt_event_ItemListener_Interface_strategy = st.builds(
    genmymodelreverse_java_awt_event_ItemListener_Interface,
)
genmymodelreverse_javax_swing_JPanel_strategy = st.builds(
    genmymodelreverse_javax_swing_JPanel,
)
genmymodelreverse_java_util_Vector_strategy = st.builds(
    genmymodelreverse_java_util_Vector,
)
genmymodelreverse_javax_swing_JFrame_strategy = st.builds(
    genmymodelreverse_javax_swing_JFrame,
)
genmymodelreverse_java_awt_event_ActionEvent_strategy = st.builds(
    genmymodelreverse_java_awt_event_ActionEvent,
)
checkers_CheckerFrame_strategy = st.builds(
    checkers_CheckerFrame,
    startButton=
        safe_text,
    gamePanel=
        safe_text
)
checkers_GameEngine_strategy = st.builds(
    checkers_GameEngine,
    edge=
        st.integers(),
    inf=
        st.integers(),
    normal=
        st.integers(),
    king=
        st.integers(),
    pos=
        st.integers()
)
checkers_StartPanel_strategy = st.builds(
    checkers_StartPanel,
)
checkers_PlaySound_strategy = st.builds(
    checkers_PlaySound,
    EXTERNAL_BUFFER_SIZE=
        st.integers(),
    filename=
        safe_text
)
checkers_IntelliChecker_strategy = st.builds(
    checkers_IntelliChecker,
)
checkers_Help_strategy = st.builds(
    checkers_Help,
    txt=
        st.none(),
    hlp=
        st.none()
)
checkers_GameWin_strategy = st.builds(
    checkers_GameWin,
    masseage=
        st.none(),
    p=
        st.none()
)
checkers_Checkers_strategy = st.builds(
    checkers_Checkers,
    toMove=
        st.integers(),
    redK=
        st.none(),
    board=
        safe_text,
    hlp=
        st.none(),
    yellowKing=
        st.integers(),
    undoCount=
        st.integers(),
    selectedColor=
        safe_text,
    preBoard3=
        safe_text,
    rk=
        st.none(),
    empty=
        st.integers(),
    yellowN=
        st.none(),
    colors=
        st.none(),
    preToMove3=
        st.integers(),
    rkt=
        st.none(),
    bk=
        st.none(),
    won=
        st.integers(),
    snp=
        st.none(),
    rpt=
        st.none(),
    rp=
        st.none(),
    preToMove2=
        st.integers(),
    msg=
        st.none(),
    currType=
        st.integers(),
    yellowNormal=
        st.integers(),
    redN=
        st.none(),
    winPoint=
        st.none(),
    mode=
        st.none(),
    endY=
        st.integers(),
    preToMove1=
        st.integers(),
    redNormal=
        st.integers(),
    bp=
        st.none(),
    preBoard2=
        safe_text,
    highlight=
        st.booleans(),
    p1=
        st.none(),
    snB=
        st.none(),
    g=
        st.none(),
    incomplete=
        st.booleans(),
    c2=
        st.none(),
    nwB=
        st.none(),
    diff=
        st.none(),
    bpt=
        st.none(),
    preBoard1=
        safe_text,
    selectedMode=
        st.integers(),
    hlpB=
        st.none(),
    silent=
        st.booleans(),
    difficulty=
        st.integers(),
    mup=
        st.none(),
    c1=
        st.none(),
    bkt=
        st.none(),
    loser=
        st.integers(),
    p2=
        st.none(),
    col=
        st.none(),
    yellowK=
        st.none(),
    level=
        st.none(),
    movable=
        st.booleans(),
    redKing=
        st.integers(),
    unB=
        st.none(),
    players=
        st.none()
)
checkers_CheckerMove_strategy = st.builds(
    checkers_CheckerMove,
    legalMove=
        st.integers(),
    incompleteMove=
        st.integers(),
    illegalMove=
        st.integers()
)

@given(instance=Computer_Player_1_Actor_strategy)
@settings(max_examples=50)
def test_computer_player_1_actor_instantiation(instance):
    assert isinstance(instance, Computer_Player_1_Actor)

@given(instance=Human_Player_2_Actor_strategy)
@settings(max_examples=50)
def test_human_player_2_actor_instantiation(instance):
    assert isinstance(instance, Human_Player_2_Actor)

@given(instance=Human_Player_1_Actor_strategy)
@settings(max_examples=50)
def test_human_player_1_actor_instantiation(instance):
    assert isinstance(instance, Human_Player_1_Actor)

@given(instance=Checkers_Close_or_Exit_Game_UseCase_strategy)
@settings(max_examples=50)
def test_checkers_close_or_exit_game_usecase_instantiation(instance):
    assert isinstance(instance, Checkers_Close_or_Exit_Game_UseCase)

@given(instance=Checkers_Move_Game_Pieces_UseCase_strategy)
@settings(max_examples=50)
def test_checkers_move_game_pieces_usecase_instantiation(instance):
    assert isinstance(instance, Checkers_Move_Game_Pieces_UseCase)

@given(instance=Checkers_Start_New_Game_UseCase_strategy)
@settings(max_examples=50)
def test_checkers_start_new_game_usecase_instantiation(instance):
    assert isinstance(instance, Checkers_Start_New_Game_UseCase)

@given(instance=Checkers_Select__Player_Mode__UseCase_strategy)
@settings(max_examples=50)
def test_checkers_select__player_mode__usecase_instantiation(instance):
    assert isinstance(instance, Checkers_Select__Player_Mode__UseCase)

@given(instance=Checkers_Select__Difficulty_Level__UseCase_strategy)
@settings(max_examples=50)
def test_checkers_select__difficulty_level__usecase_instantiation(instance):
    assert isinstance(instance, Checkers_Select__Difficulty_Level__UseCase)

@given(instance=Checkers_Toggle__Sound__UseCase_strategy)
@settings(max_examples=50)
def test_checkers_toggle__sound__usecase_instantiation(instance):
    assert isinstance(instance, Checkers_Toggle__Sound__UseCase)

@given(instance=Checkers_Select__Help__UseCase_strategy)
@settings(max_examples=50)
def test_checkers_select__help__usecase_instantiation(instance):
    assert isinstance(instance, Checkers_Select__Help__UseCase)

@given(instance=Checkers_Start_the_Game_GUI_UseCase_strategy)
@settings(max_examples=50)
def test_checkers_start_the_game_gui_usecase_instantiation(instance):
    assert isinstance(instance, Checkers_Start_the_Game_GUI_UseCase)

@given(instance=genmymodelreverse_java_lang_Exception_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_lang_exception_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Exception)

@given(instance=genmymodelreverse_javax_swing_JScrollPane_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jscrollpane_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JScrollPane)

@given(instance=genmymodelreverse_java_awt_event_MouseEvent_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_mouseevent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseEvent)

@given(instance=genmymodelreverse_java_awt_event_ItemEvent_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_itemevent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_ItemEvent)

@given(instance=genmymodelreverse_java_awt_Point_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_point_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_Point)

@given(instance=genmymodelreverse_javax_swing_JComboBox_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jcombobox_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JComboBox)

@given(instance=genmymodelreverse_javax_swing_JLabel_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jlabel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JLabel)

@given(instance=genmymodelreverse_javax_swing_JRadioButton_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jradiobutton_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JRadioButton)

@given(instance=genmymodelreverse_javax_swing_ButtonGroup_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_buttongroup_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_ButtonGroup)

@given(instance=genmymodelreverse_javax_swing_ImageIcon_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_imageicon_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_ImageIcon)

@given(instance=genmymodelreverse_javax_swing_JTextArea_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jtextarea_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JTextArea)

@given(instance=genmymodelreverse_java_awt_Graphics_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_graphics_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_Graphics)

@given(instance=genmymodelreverse_javax_swing_JButton_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jbutton_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JButton)

@given(instance=genmymodelreverse_java_lang_Thread_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_lang_thread_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_lang_Thread)

@given(instance=genmymodelreverse_javax_swing_JDialog_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jdialog_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JDialog)

@given(instance=genmymodelreverse_java_awt_event_MouseListener_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_mouselistener_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseListener_Interface)

@given(instance=genmymodelreverse_java_awt_event_MouseMotionListener_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_mousemotionlistener_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseMotionListener_Interface)

@given(instance=genmymodelreverse_java_awt_event_ItemListener_Interface_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_itemlistener_interface_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_ItemListener_Interface)

@given(instance=genmymodelreverse_javax_swing_JPanel_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jpanel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JPanel)

@given(instance=genmymodelreverse_java_util_Vector_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_util_vector_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_util_Vector)

@given(instance=genmymodelreverse_javax_swing_JFrame_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jframe_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JFrame)

@given(instance=genmymodelreverse_java_awt_event_ActionEvent_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_actionevent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_ActionEvent)

@given(instance=checkers_CheckerFrame_strategy)
@settings(max_examples=50)
def test_checkers_checkerframe_instantiation(instance):
    assert isinstance(instance, checkers_CheckerFrame)



@given(instance=checkers_CheckerFrame_strategy)
def test_checkers_checkerframe_startButton_setter(instance):
    original = instance.startButton
    instance.startButton = original
    assert instance.startButton == original



@given(instance=checkers_CheckerFrame_strategy)
def test_checkers_checkerframe_gamePanel_setter(instance):
    original = instance.gamePanel
    instance.gamePanel = original
    assert instance.gamePanel == original

@given(instance=checkers_GameEngine_strategy)
@settings(max_examples=50)
def test_checkers_gameengine_instantiation(instance):
    assert isinstance(instance, checkers_GameEngine)



@given(instance=checkers_GameEngine_strategy)
def test_checkers_gameengine_edge_setter(instance):
    original = instance.edge
    instance.edge = original
    assert instance.edge == original



@given(instance=checkers_GameEngine_strategy)
def test_checkers_gameengine_inf_setter(instance):
    original = instance.inf
    instance.inf = original
    assert instance.inf == original



@given(instance=checkers_GameEngine_strategy)
def test_checkers_gameengine_normal_setter(instance):
    original = instance.normal
    instance.normal = original
    assert instance.normal == original



@given(instance=checkers_GameEngine_strategy)
def test_checkers_gameengine_king_setter(instance):
    original = instance.king
    instance.king = original
    assert instance.king == original



@given(instance=checkers_GameEngine_strategy)
def test_checkers_gameengine_pos_setter(instance):
    original = instance.pos
    instance.pos = original
    assert instance.pos == original

@given(instance=checkers_StartPanel_strategy)
@settings(max_examples=50)
def test_checkers_startpanel_instantiation(instance):
    assert isinstance(instance, checkers_StartPanel)

@given(instance=checkers_PlaySound_strategy)
@settings(max_examples=50)
def test_checkers_playsound_instantiation(instance):
    assert isinstance(instance, checkers_PlaySound)



@given(instance=checkers_PlaySound_strategy)
def test_checkers_playsound_EXTERNAL_BUFFER_SIZE_setter(instance):
    original = instance.EXTERNAL_BUFFER_SIZE
    instance.EXTERNAL_BUFFER_SIZE = original
    assert instance.EXTERNAL_BUFFER_SIZE == original



@given(instance=checkers_PlaySound_strategy)
def test_checkers_playsound_filename_setter(instance):
    original = instance.filename
    instance.filename = original
    assert instance.filename == original

@given(instance=checkers_IntelliChecker_strategy)
@settings(max_examples=50)
def test_checkers_intellichecker_instantiation(instance):
    assert isinstance(instance, checkers_IntelliChecker)

@given(instance=checkers_Help_strategy)
@settings(max_examples=50)
def test_checkers_help_instantiation(instance):
    assert isinstance(instance, checkers_Help)



@given(instance=checkers_Help_strategy)
def test_checkers_help_txt_setter(instance):
    original = instance.txt
    instance.txt = original
    assert instance.txt == original



@given(instance=checkers_Help_strategy)
def test_checkers_help_hlp_setter(instance):
    original = instance.hlp
    instance.hlp = original
    assert instance.hlp == original

@given(instance=checkers_GameWin_strategy)
@settings(max_examples=50)
def test_checkers_gamewin_instantiation(instance):
    assert isinstance(instance, checkers_GameWin)



@given(instance=checkers_GameWin_strategy)
def test_checkers_gamewin_masseage_setter(instance):
    original = instance.masseage
    instance.masseage = original
    assert instance.masseage == original



@given(instance=checkers_GameWin_strategy)
def test_checkers_gamewin_p_setter(instance):
    original = instance.p
    instance.p = original
    assert instance.p == original

@given(instance=checkers_Checkers_strategy)
@settings(max_examples=50)
def test_checkers_checkers_instantiation(instance):
    assert isinstance(instance, checkers_Checkers)



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_toMove_setter(instance):
    original = instance.toMove
    instance.toMove = original
    assert instance.toMove == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_redK_setter(instance):
    original = instance.redK
    instance.redK = original
    assert instance.redK == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_board_setter(instance):
    original = instance.board
    instance.board = original
    assert instance.board == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_hlp_setter(instance):
    original = instance.hlp
    instance.hlp = original
    assert instance.hlp == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_yellowKing_setter(instance):
    original = instance.yellowKing
    instance.yellowKing = original
    assert instance.yellowKing == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_undoCount_setter(instance):
    original = instance.undoCount
    instance.undoCount = original
    assert instance.undoCount == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_selectedColor_setter(instance):
    original = instance.selectedColor
    instance.selectedColor = original
    assert instance.selectedColor == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_preBoard3_setter(instance):
    original = instance.preBoard3
    instance.preBoard3 = original
    assert instance.preBoard3 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_rk_setter(instance):
    original = instance.rk
    instance.rk = original
    assert instance.rk == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_empty_setter(instance):
    original = instance.empty
    instance.empty = original
    assert instance.empty == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_yellowN_setter(instance):
    original = instance.yellowN
    instance.yellowN = original
    assert instance.yellowN == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_colors_setter(instance):
    original = instance.colors
    instance.colors = original
    assert instance.colors == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_preToMove3_setter(instance):
    original = instance.preToMove3
    instance.preToMove3 = original
    assert instance.preToMove3 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_rkt_setter(instance):
    original = instance.rkt
    instance.rkt = original
    assert instance.rkt == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_bk_setter(instance):
    original = instance.bk
    instance.bk = original
    assert instance.bk == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_won_setter(instance):
    original = instance.won
    instance.won = original
    assert instance.won == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_snp_setter(instance):
    original = instance.snp
    instance.snp = original
    assert instance.snp == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_rpt_setter(instance):
    original = instance.rpt
    instance.rpt = original
    assert instance.rpt == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_rp_setter(instance):
    original = instance.rp
    instance.rp = original
    assert instance.rp == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_preToMove2_setter(instance):
    original = instance.preToMove2
    instance.preToMove2 = original
    assert instance.preToMove2 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_msg_setter(instance):
    original = instance.msg
    instance.msg = original
    assert instance.msg == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_currType_setter(instance):
    original = instance.currType
    instance.currType = original
    assert instance.currType == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_yellowNormal_setter(instance):
    original = instance.yellowNormal
    instance.yellowNormal = original
    assert instance.yellowNormal == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_redN_setter(instance):
    original = instance.redN
    instance.redN = original
    assert instance.redN == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_winPoint_setter(instance):
    original = instance.winPoint
    instance.winPoint = original
    assert instance.winPoint == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_mode_setter(instance):
    original = instance.mode
    instance.mode = original
    assert instance.mode == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_endY_setter(instance):
    original = instance.endY
    instance.endY = original
    assert instance.endY == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_preToMove1_setter(instance):
    original = instance.preToMove1
    instance.preToMove1 = original
    assert instance.preToMove1 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_redNormal_setter(instance):
    original = instance.redNormal
    instance.redNormal = original
    assert instance.redNormal == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_bp_setter(instance):
    original = instance.bp
    instance.bp = original
    assert instance.bp == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_preBoard2_setter(instance):
    original = instance.preBoard2
    instance.preBoard2 = original
    assert instance.preBoard2 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_highlight_setter(instance):
    original = instance.highlight
    instance.highlight = original
    assert instance.highlight == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_p1_setter(instance):
    original = instance.p1
    instance.p1 = original
    assert instance.p1 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_snB_setter(instance):
    original = instance.snB
    instance.snB = original
    assert instance.snB == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_g_setter(instance):
    original = instance.g
    instance.g = original
    assert instance.g == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_incomplete_setter(instance):
    original = instance.incomplete
    instance.incomplete = original
    assert instance.incomplete == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_c2_setter(instance):
    original = instance.c2
    instance.c2 = original
    assert instance.c2 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_nwB_setter(instance):
    original = instance.nwB
    instance.nwB = original
    assert instance.nwB == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_diff_setter(instance):
    original = instance.diff
    instance.diff = original
    assert instance.diff == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_bpt_setter(instance):
    original = instance.bpt
    instance.bpt = original
    assert instance.bpt == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_preBoard1_setter(instance):
    original = instance.preBoard1
    instance.preBoard1 = original
    assert instance.preBoard1 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_selectedMode_setter(instance):
    original = instance.selectedMode
    instance.selectedMode = original
    assert instance.selectedMode == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_hlpB_setter(instance):
    original = instance.hlpB
    instance.hlpB = original
    assert instance.hlpB == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_silent_setter(instance):
    original = instance.silent
    instance.silent = original
    assert instance.silent == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_difficulty_setter(instance):
    original = instance.difficulty
    instance.difficulty = original
    assert instance.difficulty == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_mup_setter(instance):
    original = instance.mup
    instance.mup = original
    assert instance.mup == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_c1_setter(instance):
    original = instance.c1
    instance.c1 = original
    assert instance.c1 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_bkt_setter(instance):
    original = instance.bkt
    instance.bkt = original
    assert instance.bkt == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_loser_setter(instance):
    original = instance.loser
    instance.loser = original
    assert instance.loser == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_p2_setter(instance):
    original = instance.p2
    instance.p2 = original
    assert instance.p2 == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_col_setter(instance):
    original = instance.col
    instance.col = original
    assert instance.col == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_yellowK_setter(instance):
    original = instance.yellowK
    instance.yellowK = original
    assert instance.yellowK == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_movable_setter(instance):
    original = instance.movable
    instance.movable = original
    assert instance.movable == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_redKing_setter(instance):
    original = instance.redKing
    instance.redKing = original
    assert instance.redKing == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_unB_setter(instance):
    original = instance.unB
    instance.unB = original
    assert instance.unB == original



@given(instance=checkers_Checkers_strategy)
def test_checkers_checkers_players_setter(instance):
    original = instance.players
    instance.players = original
    assert instance.players == original

@given(instance=checkers_CheckerMove_strategy)
@settings(max_examples=50)
def test_checkers_checkermove_instantiation(instance):
    assert isinstance(instance, checkers_CheckerMove)



@given(instance=checkers_CheckerMove_strategy)
def test_checkers_checkermove_legalMove_setter(instance):
    original = instance.legalMove
    instance.legalMove = original
    assert instance.legalMove == original



@given(instance=checkers_CheckerMove_strategy)
def test_checkers_checkermove_incompleteMove_setter(instance):
    original = instance.incompleteMove
    instance.incompleteMove = original
    assert instance.incompleteMove == original



@given(instance=checkers_CheckerMove_strategy)
def test_checkers_checkermove_illegalMove_setter(instance):
    original = instance.illegalMove
    instance.illegalMove = original
    assert instance.illegalMove == original
