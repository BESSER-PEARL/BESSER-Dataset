import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    genmymodelreverse_javax_swing_JMenuItem,
    genmymodelreverse_javax_swing_JFrame,
    genmymodelreverse_javax_swing_JPanel,
    genmymodelreverse_javax_swing_JLabel,
    genmymodelreverse_java_awt_event_MouseEvent,
    genmymodelreverse_java_awt_event_MouseAdapter,
    genmymodelreverse_java_awt_Graphics,
    Mines,
    MinesAdapter,
    Board,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_genmymodelreverse_javax_swing_jmenuitem_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JMenuItem)


def test_genmymodelreverse_javax_swing_jmenuitem_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JMenuItem.__init__)


def test_genmymodelreverse_javax_swing_jmenuitem_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JMenuItem.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jframe_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JFrame)


def test_genmymodelreverse_javax_swing_jframe_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JFrame.__init__)


def test_genmymodelreverse_javax_swing_jframe_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JFrame.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jpanel_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JPanel)


def test_genmymodelreverse_javax_swing_jpanel_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JPanel.__init__)


def test_genmymodelreverse_javax_swing_jpanel_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JPanel.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_javax_swing_jlabel_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_javax_swing_JLabel)


def test_genmymodelreverse_javax_swing_jlabel_constructor_exists():
    assert callable(genmymodelreverse_javax_swing_JLabel.__init__)


def test_genmymodelreverse_javax_swing_jlabel_constructor_args():
    sig = inspect.signature(genmymodelreverse_javax_swing_JLabel.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_mouseevent_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_MouseEvent)


def test_genmymodelreverse_java_awt_event_mouseevent_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_MouseEvent.__init__)


def test_genmymodelreverse_java_awt_event_mouseevent_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_MouseEvent.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_event_mouseadapter_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_event_MouseAdapter)


def test_genmymodelreverse_java_awt_event_mouseadapter_constructor_exists():
    assert callable(genmymodelreverse_java_awt_event_MouseAdapter.__init__)


def test_genmymodelreverse_java_awt_event_mouseadapter_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_event_MouseAdapter.__init__)
    params = list(sig.parameters.keys())



def test_genmymodelreverse_java_awt_graphics_is_not_abstract():
    assert not inspect.isabstract(genmymodelreverse_java_awt_Graphics)


def test_genmymodelreverse_java_awt_graphics_constructor_exists():
    assert callable(genmymodelreverse_java_awt_Graphics.__init__)


def test_genmymodelreverse_java_awt_graphics_constructor_args():
    sig = inspect.signature(genmymodelreverse_java_awt_Graphics.__init__)
    params = list(sig.parameters.keys())



def test_mines_is_not_abstract():
    assert not inspect.isabstract(Mines)


def test_mines_constructor_exists():
    assert callable(Mines.__init__)


def test_mines_constructor_args():
    sig = inspect.signature(Mines.__init__)
    params = list(sig.parameters.keys())
    assert "timeBar" in params, "Missing parameter 'timeBar'"
    assert "FRAME_HEIGHT" in params, "Missing parameter 'FRAME_HEIGHT'"
    assert "FRAME_WIDTH" in params, "Missing parameter 'FRAME_WIDTH'"
    assert "statusbar" in params, "Missing parameter 'statusbar'"
    assert "hexCell" in params, "Missing parameter 'hexCell'"

def test_mines_has_timeBar():
    assert hasattr(Mines, "timeBar")
    descriptor = None
    for klass in Mines.__mro__:
        if "timeBar" in klass.__dict__:
            descriptor = klass.__dict__["timeBar"]
            break
    assert isinstance(descriptor, property)

def test_mines_has_FRAME_HEIGHT():
    assert hasattr(Mines, "FRAME_HEIGHT")
    descriptor = None
    for klass in Mines.__mro__:
        if "FRAME_HEIGHT" in klass.__dict__:
            descriptor = klass.__dict__["FRAME_HEIGHT"]
            break
    assert isinstance(descriptor, property)

def test_mines_has_FRAME_WIDTH():
    assert hasattr(Mines, "FRAME_WIDTH")
    descriptor = None
    for klass in Mines.__mro__:
        if "FRAME_WIDTH" in klass.__dict__:
            descriptor = klass.__dict__["FRAME_WIDTH"]
            break
    assert isinstance(descriptor, property)

def test_mines_has_statusbar():
    assert hasattr(Mines, "statusbar")
    descriptor = None
    for klass in Mines.__mro__:
        if "statusbar" in klass.__dict__:
            descriptor = klass.__dict__["statusbar"]
            break
    assert isinstance(descriptor, property)

def test_mines_has_hexCell():
    assert hasattr(Mines, "hexCell")
    descriptor = None
    for klass in Mines.__mro__:
        if "hexCell" in klass.__dict__:
            descriptor = klass.__dict__["hexCell"]
            break
    assert isinstance(descriptor, property)



def test_minesadapter_is_not_abstract():
    assert not inspect.isabstract(MinesAdapter)


def test_minesadapter_constructor_exists():
    assert callable(MinesAdapter.__init__)


def test_minesadapter_constructor_args():
    sig = inspect.signature(MinesAdapter.__init__)
    params = list(sig.parameters.keys())



def test_board_is_not_abstract():
    assert not inspect.isabstract(Board)


def test_board_constructor_exists():
    assert callable(Board.__init__)


def test_board_constructor_args():
    sig = inspect.signature(Board.__init__)
    params = list(sig.parameters.keys())
    assert "N_ROWS" in params, "Missing parameter 'N_ROWS'"
    assert "statusbar" in params, "Missing parameter 'statusbar'"
    assert "inGame" in params, "Missing parameter 'inGame'"
    assert "all_cells" in params, "Missing parameter 'all_cells'"
    assert "DRAW_MINE" in params, "Missing parameter 'DRAW_MINE'"
    assert "MARKED_MINE_CELL" in params, "Missing parameter 'MARKED_MINE_CELL'"
    assert "COVER_FOR_CELL" in params, "Missing parameter 'COVER_FOR_CELL'"
    assert "DRAW_WRONG_MARK" in params, "Missing parameter 'DRAW_WRONG_MARK'"
    assert "EMPTY_CELL" in params, "Missing parameter 'EMPTY_CELL'"
    assert "COVERED_MINE_CELL" in params, "Missing parameter 'COVERED_MINE_CELL'"
    assert "field" in params, "Missing parameter 'field'"
    assert "CELL_SIZE" in params, "Missing parameter 'CELL_SIZE'"
    assert "img" in params, "Missing parameter 'img'"
    assert "MINE_CELL" in params, "Missing parameter 'MINE_CELL'"
    assert "timeBar" in params, "Missing parameter 'timeBar'"
    assert "MARK_FOR_CELL" in params, "Missing parameter 'MARK_FOR_CELL'"
    assert "N_MINES" in params, "Missing parameter 'N_MINES'"
    assert "DRAW_MARK" in params, "Missing parameter 'DRAW_MARK'"
    assert "mines_left" in params, "Missing parameter 'mines_left'"
    assert "DRAW_COVER" in params, "Missing parameter 'DRAW_COVER'"
    assert "NUM_IMAGES" in params, "Missing parameter 'NUM_IMAGES'"
    assert "N_COLS" in params, "Missing parameter 'N_COLS'"

def test_board_has_N_ROWS():
    assert hasattr(Board, "N_ROWS")
    descriptor = None
    for klass in Board.__mro__:
        if "N_ROWS" in klass.__dict__:
            descriptor = klass.__dict__["N_ROWS"]
            break
    assert isinstance(descriptor, property)

def test_board_has_statusbar():
    assert hasattr(Board, "statusbar")
    descriptor = None
    for klass in Board.__mro__:
        if "statusbar" in klass.__dict__:
            descriptor = klass.__dict__["statusbar"]
            break
    assert isinstance(descriptor, property)

def test_board_has_inGame():
    assert hasattr(Board, "inGame")
    descriptor = None
    for klass in Board.__mro__:
        if "inGame" in klass.__dict__:
            descriptor = klass.__dict__["inGame"]
            break
    assert isinstance(descriptor, property)

def test_board_has_all_cells():
    assert hasattr(Board, "all_cells")
    descriptor = None
    for klass in Board.__mro__:
        if "all_cells" in klass.__dict__:
            descriptor = klass.__dict__["all_cells"]
            break
    assert isinstance(descriptor, property)

def test_board_has_DRAW_MINE():
    assert hasattr(Board, "DRAW_MINE")
    descriptor = None
    for klass in Board.__mro__:
        if "DRAW_MINE" in klass.__dict__:
            descriptor = klass.__dict__["DRAW_MINE"]
            break
    assert isinstance(descriptor, property)

def test_board_has_MARKED_MINE_CELL():
    assert hasattr(Board, "MARKED_MINE_CELL")
    descriptor = None
    for klass in Board.__mro__:
        if "MARKED_MINE_CELL" in klass.__dict__:
            descriptor = klass.__dict__["MARKED_MINE_CELL"]
            break
    assert isinstance(descriptor, property)

def test_board_has_COVER_FOR_CELL():
    assert hasattr(Board, "COVER_FOR_CELL")
    descriptor = None
    for klass in Board.__mro__:
        if "COVER_FOR_CELL" in klass.__dict__:
            descriptor = klass.__dict__["COVER_FOR_CELL"]
            break
    assert isinstance(descriptor, property)

def test_board_has_DRAW_WRONG_MARK():
    assert hasattr(Board, "DRAW_WRONG_MARK")
    descriptor = None
    for klass in Board.__mro__:
        if "DRAW_WRONG_MARK" in klass.__dict__:
            descriptor = klass.__dict__["DRAW_WRONG_MARK"]
            break
    assert isinstance(descriptor, property)

def test_board_has_EMPTY_CELL():
    assert hasattr(Board, "EMPTY_CELL")
    descriptor = None
    for klass in Board.__mro__:
        if "EMPTY_CELL" in klass.__dict__:
            descriptor = klass.__dict__["EMPTY_CELL"]
            break
    assert isinstance(descriptor, property)

def test_board_has_COVERED_MINE_CELL():
    assert hasattr(Board, "COVERED_MINE_CELL")
    descriptor = None
    for klass in Board.__mro__:
        if "COVERED_MINE_CELL" in klass.__dict__:
            descriptor = klass.__dict__["COVERED_MINE_CELL"]
            break
    assert isinstance(descriptor, property)

def test_board_has_field():
    assert hasattr(Board, "field")
    descriptor = None
    for klass in Board.__mro__:
        if "field" in klass.__dict__:
            descriptor = klass.__dict__["field"]
            break
    assert isinstance(descriptor, property)

def test_board_has_CELL_SIZE():
    assert hasattr(Board, "CELL_SIZE")
    descriptor = None
    for klass in Board.__mro__:
        if "CELL_SIZE" in klass.__dict__:
            descriptor = klass.__dict__["CELL_SIZE"]
            break
    assert isinstance(descriptor, property)

def test_board_has_img():
    assert hasattr(Board, "img")
    descriptor = None
    for klass in Board.__mro__:
        if "img" in klass.__dict__:
            descriptor = klass.__dict__["img"]
            break
    assert isinstance(descriptor, property)

def test_board_has_MINE_CELL():
    assert hasattr(Board, "MINE_CELL")
    descriptor = None
    for klass in Board.__mro__:
        if "MINE_CELL" in klass.__dict__:
            descriptor = klass.__dict__["MINE_CELL"]
            break
    assert isinstance(descriptor, property)

def test_board_has_timeBar():
    assert hasattr(Board, "timeBar")
    descriptor = None
    for klass in Board.__mro__:
        if "timeBar" in klass.__dict__:
            descriptor = klass.__dict__["timeBar"]
            break
    assert isinstance(descriptor, property)

def test_board_has_MARK_FOR_CELL():
    assert hasattr(Board, "MARK_FOR_CELL")
    descriptor = None
    for klass in Board.__mro__:
        if "MARK_FOR_CELL" in klass.__dict__:
            descriptor = klass.__dict__["MARK_FOR_CELL"]
            break
    assert isinstance(descriptor, property)

def test_board_has_N_MINES():
    assert hasattr(Board, "N_MINES")
    descriptor = None
    for klass in Board.__mro__:
        if "N_MINES" in klass.__dict__:
            descriptor = klass.__dict__["N_MINES"]
            break
    assert isinstance(descriptor, property)

def test_board_has_DRAW_MARK():
    assert hasattr(Board, "DRAW_MARK")
    descriptor = None
    for klass in Board.__mro__:
        if "DRAW_MARK" in klass.__dict__:
            descriptor = klass.__dict__["DRAW_MARK"]
            break
    assert isinstance(descriptor, property)

def test_board_has_mines_left():
    assert hasattr(Board, "mines_left")
    descriptor = None
    for klass in Board.__mro__:
        if "mines_left" in klass.__dict__:
            descriptor = klass.__dict__["mines_left"]
            break
    assert isinstance(descriptor, property)

def test_board_has_DRAW_COVER():
    assert hasattr(Board, "DRAW_COVER")
    descriptor = None
    for klass in Board.__mro__:
        if "DRAW_COVER" in klass.__dict__:
            descriptor = klass.__dict__["DRAW_COVER"]
            break
    assert isinstance(descriptor, property)

def test_board_has_NUM_IMAGES():
    assert hasattr(Board, "NUM_IMAGES")
    descriptor = None
    for klass in Board.__mro__:
        if "NUM_IMAGES" in klass.__dict__:
            descriptor = klass.__dict__["NUM_IMAGES"]
            break
    assert isinstance(descriptor, property)

def test_board_has_N_COLS():
    assert hasattr(Board, "N_COLS")
    descriptor = None
    for klass in Board.__mro__:
        if "N_COLS" in klass.__dict__:
            descriptor = klass.__dict__["N_COLS"]
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
genmymodelreverse_javax_swing_JMenuItem_strategy = st.builds(
    genmymodelreverse_javax_swing_JMenuItem,
)
genmymodelreverse_javax_swing_JFrame_strategy = st.builds(
    genmymodelreverse_javax_swing_JFrame,
)
genmymodelreverse_javax_swing_JPanel_strategy = st.builds(
    genmymodelreverse_javax_swing_JPanel,
)
genmymodelreverse_javax_swing_JLabel_strategy = st.builds(
    genmymodelreverse_javax_swing_JLabel,
)
genmymodelreverse_java_awt_event_MouseEvent_strategy = st.builds(
    genmymodelreverse_java_awt_event_MouseEvent,
)
genmymodelreverse_java_awt_event_MouseAdapter_strategy = st.builds(
    genmymodelreverse_java_awt_event_MouseAdapter,
)
genmymodelreverse_java_awt_Graphics_strategy = st.builds(
    genmymodelreverse_java_awt_Graphics,
)
Mines_strategy = st.builds(
    Mines,
    timeBar=
        st.none(),
    FRAME_HEIGHT=
        st.integers(),
    FRAME_WIDTH=
        st.integers(),
    statusbar=
        st.none(),
    hexCell=
        st.none()
)
MinesAdapter_strategy = st.builds(
    MinesAdapter,
)
Board_strategy = st.builds(
    Board,
    N_ROWS=
        st.integers(),
    statusbar=
        st.none(),
    inGame=
        st.booleans(),
    all_cells=
        st.integers(),
    DRAW_MINE=
        st.integers(),
    MARKED_MINE_CELL=
        st.integers(),
    COVER_FOR_CELL=
        st.integers(),
    DRAW_WRONG_MARK=
        st.integers(),
    EMPTY_CELL=
        st.integers(),
    COVERED_MINE_CELL=
        st.integers(),
    field=
        safe_text,
    CELL_SIZE=
        st.integers(),
    img=
        safe_text,
    MINE_CELL=
        st.integers(),
    timeBar=
        st.none(),
    MARK_FOR_CELL=
        st.integers(),
    N_MINES=
        st.integers(),
    DRAW_MARK=
        st.integers(),
    mines_left=
        st.integers(),
    DRAW_COVER=
        st.integers(),
    NUM_IMAGES=
        st.integers(),
    N_COLS=
        st.integers()
)

@given(instance=genmymodelreverse_javax_swing_JMenuItem_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jmenuitem_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JMenuItem)

@given(instance=genmymodelreverse_javax_swing_JFrame_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jframe_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JFrame)

@given(instance=genmymodelreverse_javax_swing_JPanel_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jpanel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JPanel)

@given(instance=genmymodelreverse_javax_swing_JLabel_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_javax_swing_jlabel_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_javax_swing_JLabel)

@given(instance=genmymodelreverse_java_awt_event_MouseEvent_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_mouseevent_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseEvent)

@given(instance=genmymodelreverse_java_awt_event_MouseAdapter_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_event_mouseadapter_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_event_MouseAdapter)

@given(instance=genmymodelreverse_java_awt_Graphics_strategy)
@settings(max_examples=50)
def test_genmymodelreverse_java_awt_graphics_instantiation(instance):
    assert isinstance(instance, genmymodelreverse_java_awt_Graphics)

@given(instance=Mines_strategy)
@settings(max_examples=50)
def test_mines_instantiation(instance):
    assert isinstance(instance, Mines)



@given(instance=Mines_strategy)
def test_mines_timeBar_setter(instance):
    original = instance.timeBar
    instance.timeBar = original
    assert instance.timeBar == original



@given(instance=Mines_strategy)
def test_mines_FRAME_HEIGHT_setter(instance):
    original = instance.FRAME_HEIGHT
    instance.FRAME_HEIGHT = original
    assert instance.FRAME_HEIGHT == original



@given(instance=Mines_strategy)
def test_mines_FRAME_WIDTH_setter(instance):
    original = instance.FRAME_WIDTH
    instance.FRAME_WIDTH = original
    assert instance.FRAME_WIDTH == original



@given(instance=Mines_strategy)
def test_mines_statusbar_setter(instance):
    original = instance.statusbar
    instance.statusbar = original
    assert instance.statusbar == original



@given(instance=Mines_strategy)
def test_mines_hexCell_setter(instance):
    original = instance.hexCell
    instance.hexCell = original
    assert instance.hexCell == original

@given(instance=MinesAdapter_strategy)
@settings(max_examples=50)
def test_minesadapter_instantiation(instance):
    assert isinstance(instance, MinesAdapter)

@given(instance=Board_strategy)
@settings(max_examples=50)
def test_board_instantiation(instance):
    assert isinstance(instance, Board)



@given(instance=Board_strategy)
def test_board_N_ROWS_setter(instance):
    original = instance.N_ROWS
    instance.N_ROWS = original
    assert instance.N_ROWS == original



@given(instance=Board_strategy)
def test_board_statusbar_setter(instance):
    original = instance.statusbar
    instance.statusbar = original
    assert instance.statusbar == original



@given(instance=Board_strategy)
def test_board_inGame_setter(instance):
    original = instance.inGame
    instance.inGame = original
    assert instance.inGame == original



@given(instance=Board_strategy)
def test_board_all_cells_setter(instance):
    original = instance.all_cells
    instance.all_cells = original
    assert instance.all_cells == original



@given(instance=Board_strategy)
def test_board_DRAW_MINE_setter(instance):
    original = instance.DRAW_MINE
    instance.DRAW_MINE = original
    assert instance.DRAW_MINE == original



@given(instance=Board_strategy)
def test_board_MARKED_MINE_CELL_setter(instance):
    original = instance.MARKED_MINE_CELL
    instance.MARKED_MINE_CELL = original
    assert instance.MARKED_MINE_CELL == original



@given(instance=Board_strategy)
def test_board_COVER_FOR_CELL_setter(instance):
    original = instance.COVER_FOR_CELL
    instance.COVER_FOR_CELL = original
    assert instance.COVER_FOR_CELL == original



@given(instance=Board_strategy)
def test_board_DRAW_WRONG_MARK_setter(instance):
    original = instance.DRAW_WRONG_MARK
    instance.DRAW_WRONG_MARK = original
    assert instance.DRAW_WRONG_MARK == original



@given(instance=Board_strategy)
def test_board_EMPTY_CELL_setter(instance):
    original = instance.EMPTY_CELL
    instance.EMPTY_CELL = original
    assert instance.EMPTY_CELL == original



@given(instance=Board_strategy)
def test_board_COVERED_MINE_CELL_setter(instance):
    original = instance.COVERED_MINE_CELL
    instance.COVERED_MINE_CELL = original
    assert instance.COVERED_MINE_CELL == original



@given(instance=Board_strategy)
def test_board_field_setter(instance):
    original = instance.field
    instance.field = original
    assert instance.field == original



@given(instance=Board_strategy)
def test_board_CELL_SIZE_setter(instance):
    original = instance.CELL_SIZE
    instance.CELL_SIZE = original
    assert instance.CELL_SIZE == original



@given(instance=Board_strategy)
def test_board_img_setter(instance):
    original = instance.img
    instance.img = original
    assert instance.img == original



@given(instance=Board_strategy)
def test_board_MINE_CELL_setter(instance):
    original = instance.MINE_CELL
    instance.MINE_CELL = original
    assert instance.MINE_CELL == original



@given(instance=Board_strategy)
def test_board_timeBar_setter(instance):
    original = instance.timeBar
    instance.timeBar = original
    assert instance.timeBar == original



@given(instance=Board_strategy)
def test_board_MARK_FOR_CELL_setter(instance):
    original = instance.MARK_FOR_CELL
    instance.MARK_FOR_CELL = original
    assert instance.MARK_FOR_CELL == original



@given(instance=Board_strategy)
def test_board_N_MINES_setter(instance):
    original = instance.N_MINES
    instance.N_MINES = original
    assert instance.N_MINES == original



@given(instance=Board_strategy)
def test_board_DRAW_MARK_setter(instance):
    original = instance.DRAW_MARK
    instance.DRAW_MARK = original
    assert instance.DRAW_MARK == original



@given(instance=Board_strategy)
def test_board_mines_left_setter(instance):
    original = instance.mines_left
    instance.mines_left = original
    assert instance.mines_left == original



@given(instance=Board_strategy)
def test_board_DRAW_COVER_setter(instance):
    original = instance.DRAW_COVER
    instance.DRAW_COVER = original
    assert instance.DRAW_COVER == original



@given(instance=Board_strategy)
def test_board_NUM_IMAGES_setter(instance):
    original = instance.NUM_IMAGES
    instance.NUM_IMAGES = original
    assert instance.NUM_IMAGES == original



@given(instance=Board_strategy)
def test_board_N_COLS_setter(instance):
    original = instance.N_COLS
    instance.N_COLS = original
    assert instance.N_COLS == original
