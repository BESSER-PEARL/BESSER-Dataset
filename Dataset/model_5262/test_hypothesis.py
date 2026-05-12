import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    defaultname_FRAMESET,
    FRAME,
    defaultname_IFRAME,
    defaultname_NOFRAME,
    defaultname_FRAME,
    defaultname_TEXTAREA,
    defaultname_OBJECT,
    defaultname_PARAM,
    defaultname_APPLET,
    defaultname_DD,
    defaultname_DT,
    defaultname_DL,
    ListElement,
    defaultname_LI,
    defaultname_UL,
    defaultname_OL,
    defaultname_ListElement,
    defaultname_OPTION,
    defaultname_SELECT,
    TABLEElement,
    defaultname_TABLE,
    defaultname_INPUT,
    defaultname_FORM,
    TD,
    defaultname_TH,
    defaultname_TD,
    defaultname_TR,
    BODYElement,
    defaultname_AREA,
    defaultname_DIV,
    defaultname_PRE,
    defaultname_H3,
    defaultname_MAP,
    defaultname_P,
    defaultname_B,
    defaultname_I,
    defaultname_BR,
    defaultname_FONT,
    defaultname_H2,
    defaultname_SMALL,
    defaultname_SUB,
    defaultname_A,
    defaultname_SUP,
    defaultname_IMG,
    defaultname_STRIKE,
    defaultname_EM,
    defaultname_EMBED,
    defaultname_BIG,
    defaultname_SPAN,
    defaultname_STRONG,
    defaultname_H4,
    defaultname_TT,
    defaultname_NOEMBED,
    defaultname_TABLEElement,
    defaultname_STYLE,
    defaultname_H1,
    HEADElement,
    defaultname_TITLE,
    defaultname_LINK,
    HTMLElement,
    defaultname_HEADElement,
    defaultname_BODYElement,
    defaultname_BODY,
    defaultname_HTMLElement,
    defaultname_HEAD,
    defaultname_HTML,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_defaultname_frameset_is_not_abstract():
    assert not inspect.isabstract(defaultname_FRAMESET)


def test_defaultname_frameset_constructor_exists():
    assert callable(defaultname_FRAMESET.__init__)


def test_defaultname_frameset_constructor_args():
    sig = inspect.signature(defaultname_FRAMESET.__init__)
    params = list(sig.parameters.keys())
    assert "border" in params, "Missing parameter 'border'"
    assert "framespacing" in params, "Missing parameter 'framespacing'"
    assert "frameborder" in params, "Missing parameter 'frameborder'"
    assert "cols" in params, "Missing parameter 'cols'"
    assert "rows" in params, "Missing parameter 'rows'"

def test_defaultname_frameset_has_border():
    assert hasattr(defaultname_FRAMESET, "border")
    descriptor = None
    for klass in defaultname_FRAMESET.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frameset_has_framespacing():
    assert hasattr(defaultname_FRAMESET, "framespacing")
    descriptor = None
    for klass in defaultname_FRAMESET.__mro__:
        if "framespacing" in klass.__dict__:
            descriptor = klass.__dict__["framespacing"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frameset_has_frameborder():
    assert hasattr(defaultname_FRAMESET, "frameborder")
    descriptor = None
    for klass in defaultname_FRAMESET.__mro__:
        if "frameborder" in klass.__dict__:
            descriptor = klass.__dict__["frameborder"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frameset_has_cols():
    assert hasattr(defaultname_FRAMESET, "cols")
    descriptor = None
    for klass in defaultname_FRAMESET.__mro__:
        if "cols" in klass.__dict__:
            descriptor = klass.__dict__["cols"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frameset_has_rows():
    assert hasattr(defaultname_FRAMESET, "rows")
    descriptor = None
    for klass in defaultname_FRAMESET.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)



def test_frame_is_not_abstract():
    assert not inspect.isabstract(FRAME)


def test_frame_constructor_exists():
    assert callable(FRAME.__init__)


def test_frame_constructor_args():
    sig = inspect.signature(FRAME.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_iframe_is_not_abstract():
    assert not inspect.isabstract(defaultname_IFRAME)


def test_defaultname_iframe_constructor_exists():
    assert callable(defaultname_IFRAME.__init__)


def test_defaultname_iframe_constructor_args():
    sig = inspect.signature(defaultname_IFRAME.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_noframe_is_not_abstract():
    assert not inspect.isabstract(defaultname_NOFRAME)


def test_defaultname_noframe_constructor_exists():
    assert callable(defaultname_NOFRAME.__init__)


def test_defaultname_noframe_constructor_args():
    sig = inspect.signature(defaultname_NOFRAME.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_frame_is_not_abstract():
    assert not inspect.isabstract(defaultname_FRAME)


def test_defaultname_frame_constructor_exists():
    assert callable(defaultname_FRAME.__init__)


def test_defaultname_frame_constructor_args():
    sig = inspect.signature(defaultname_FRAME.__init__)
    params = list(sig.parameters.keys())
    assert "scrolling" in params, "Missing parameter 'scrolling'"
    assert "marginheight" in params, "Missing parameter 'marginheight'"
    assert "marginwidth" in params, "Missing parameter 'marginwidth'"
    assert "noresize" in params, "Missing parameter 'noresize'"
    assert "src" in params, "Missing parameter 'src'"
    assert "name" in params, "Missing parameter 'name'"

def test_defaultname_frame_has_scrolling():
    assert hasattr(defaultname_FRAME, "scrolling")
    descriptor = None
    for klass in defaultname_FRAME.__mro__:
        if "scrolling" in klass.__dict__:
            descriptor = klass.__dict__["scrolling"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frame_has_marginheight():
    assert hasattr(defaultname_FRAME, "marginheight")
    descriptor = None
    for klass in defaultname_FRAME.__mro__:
        if "marginheight" in klass.__dict__:
            descriptor = klass.__dict__["marginheight"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frame_has_marginwidth():
    assert hasattr(defaultname_FRAME, "marginwidth")
    descriptor = None
    for klass in defaultname_FRAME.__mro__:
        if "marginwidth" in klass.__dict__:
            descriptor = klass.__dict__["marginwidth"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frame_has_noresize():
    assert hasattr(defaultname_FRAME, "noresize")
    descriptor = None
    for klass in defaultname_FRAME.__mro__:
        if "noresize" in klass.__dict__:
            descriptor = klass.__dict__["noresize"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frame_has_src():
    assert hasattr(defaultname_FRAME, "src")
    descriptor = None
    for klass in defaultname_FRAME.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_frame_has_name():
    assert hasattr(defaultname_FRAME, "name")
    descriptor = None
    for klass in defaultname_FRAME.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_textarea_is_not_abstract():
    assert not inspect.isabstract(defaultname_TEXTAREA)


def test_defaultname_textarea_constructor_exists():
    assert callable(defaultname_TEXTAREA.__init__)


def test_defaultname_textarea_constructor_args():
    sig = inspect.signature(defaultname_TEXTAREA.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "cols" in params, "Missing parameter 'cols'"
    assert "rows" in params, "Missing parameter 'rows'"

def test_defaultname_textarea_has_name():
    assert hasattr(defaultname_TEXTAREA, "name")
    descriptor = None
    for klass in defaultname_TEXTAREA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_textarea_has_cols():
    assert hasattr(defaultname_TEXTAREA, "cols")
    descriptor = None
    for klass in defaultname_TEXTAREA.__mro__:
        if "cols" in klass.__dict__:
            descriptor = klass.__dict__["cols"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_textarea_has_rows():
    assert hasattr(defaultname_TEXTAREA, "rows")
    descriptor = None
    for klass in defaultname_TEXTAREA.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_object_is_not_abstract():
    assert not inspect.isabstract(defaultname_OBJECT)


def test_defaultname_object_constructor_exists():
    assert callable(defaultname_OBJECT.__init__)


def test_defaultname_object_constructor_args():
    sig = inspect.signature(defaultname_OBJECT.__init__)
    params = list(sig.parameters.keys())
    assert "standby" in params, "Missing parameter 'standby'"
    assert "type" in params, "Missing parameter 'type'"
    assert "classid" in params, "Missing parameter 'classid'"
    assert "id" in params, "Missing parameter 'id'"
    assert "data" in params, "Missing parameter 'data'"

def test_defaultname_object_has_standby():
    assert hasattr(defaultname_OBJECT, "standby")
    descriptor = None
    for klass in defaultname_OBJECT.__mro__:
        if "standby" in klass.__dict__:
            descriptor = klass.__dict__["standby"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_object_has_type():
    assert hasattr(defaultname_OBJECT, "type")
    descriptor = None
    for klass in defaultname_OBJECT.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_object_has_classid():
    assert hasattr(defaultname_OBJECT, "classid")
    descriptor = None
    for klass in defaultname_OBJECT.__mro__:
        if "classid" in klass.__dict__:
            descriptor = klass.__dict__["classid"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_object_has_id():
    assert hasattr(defaultname_OBJECT, "id")
    descriptor = None
    for klass in defaultname_OBJECT.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_object_has_data():
    assert hasattr(defaultname_OBJECT, "data")
    descriptor = None
    for klass in defaultname_OBJECT.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_param_is_not_abstract():
    assert not inspect.isabstract(defaultname_PARAM)


def test_defaultname_param_constructor_exists():
    assert callable(defaultname_PARAM.__init__)


def test_defaultname_param_constructor_args():
    sig = inspect.signature(defaultname_PARAM.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "paramValue" in params, "Missing parameter 'paramValue'"

def test_defaultname_param_has_name():
    assert hasattr(defaultname_PARAM, "name")
    descriptor = None
    for klass in defaultname_PARAM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_param_has_paramValue():
    assert hasattr(defaultname_PARAM, "paramValue")
    descriptor = None
    for klass in defaultname_PARAM.__mro__:
        if "paramValue" in klass.__dict__:
            descriptor = klass.__dict__["paramValue"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_applet_is_not_abstract():
    assert not inspect.isabstract(defaultname_APPLET)


def test_defaultname_applet_constructor_exists():
    assert callable(defaultname_APPLET.__init__)


def test_defaultname_applet_constructor_args():
    sig = inspect.signature(defaultname_APPLET.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "src" in params, "Missing parameter 'src'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "width" in params, "Missing parameter 'width'"
    assert "applet" in params, "Missing parameter 'applet'"
    assert "align" in params, "Missing parameter 'align'"

def test_defaultname_applet_has_height():
    assert hasattr(defaultname_APPLET, "height")
    descriptor = None
    for klass in defaultname_APPLET.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_applet_has_src():
    assert hasattr(defaultname_APPLET, "src")
    descriptor = None
    for klass in defaultname_APPLET.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_applet_has_class_():
    assert hasattr(defaultname_APPLET, "class_")
    descriptor = None
    for klass in defaultname_APPLET.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_applet_has_width():
    assert hasattr(defaultname_APPLET, "width")
    descriptor = None
    for klass in defaultname_APPLET.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_applet_has_applet():
    assert hasattr(defaultname_APPLET, "applet")
    descriptor = None
    for klass in defaultname_APPLET.__mro__:
        if "applet" in klass.__dict__:
            descriptor = klass.__dict__["applet"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_applet_has_align():
    assert hasattr(defaultname_APPLET, "align")
    descriptor = None
    for klass in defaultname_APPLET.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_dd_is_not_abstract():
    assert not inspect.isabstract(defaultname_DD)


def test_defaultname_dd_constructor_exists():
    assert callable(defaultname_DD.__init__)


def test_defaultname_dd_constructor_args():
    sig = inspect.signature(defaultname_DD.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_dt_is_not_abstract():
    assert not inspect.isabstract(defaultname_DT)


def test_defaultname_dt_constructor_exists():
    assert callable(defaultname_DT.__init__)


def test_defaultname_dt_constructor_args():
    sig = inspect.signature(defaultname_DT.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_dl_is_not_abstract():
    assert not inspect.isabstract(defaultname_DL)


def test_defaultname_dl_constructor_exists():
    assert callable(defaultname_DL.__init__)


def test_defaultname_dl_constructor_args():
    sig = inspect.signature(defaultname_DL.__init__)
    params = list(sig.parameters.keys())



def test_listelement_is_not_abstract():
    assert not inspect.isabstract(ListElement)


def test_listelement_constructor_exists():
    assert callable(ListElement.__init__)


def test_listelement_constructor_args():
    sig = inspect.signature(ListElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_li_is_not_abstract():
    assert not inspect.isabstract(defaultname_LI)


def test_defaultname_li_constructor_exists():
    assert callable(defaultname_LI.__init__)


def test_defaultname_li_constructor_args():
    sig = inspect.signature(defaultname_LI.__init__)
    params = list(sig.parameters.keys())
    assert "liValue" in params, "Missing parameter 'liValue'"

def test_defaultname_li_has_liValue():
    assert hasattr(defaultname_LI, "liValue")
    descriptor = None
    for klass in defaultname_LI.__mro__:
        if "liValue" in klass.__dict__:
            descriptor = klass.__dict__["liValue"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_ul_is_not_abstract():
    assert not inspect.isabstract(defaultname_UL)


def test_defaultname_ul_constructor_exists():
    assert callable(defaultname_UL.__init__)


def test_defaultname_ul_constructor_args():
    sig = inspect.signature(defaultname_UL.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_ol_is_not_abstract():
    assert not inspect.isabstract(defaultname_OL)


def test_defaultname_ol_constructor_exists():
    assert callable(defaultname_OL.__init__)


def test_defaultname_ol_constructor_args():
    sig = inspect.signature(defaultname_OL.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"

def test_defaultname_ol_has_start():
    assert hasattr(defaultname_OL, "start")
    descriptor = None
    for klass in defaultname_OL.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_listelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_ListElement)


def test_defaultname_listelement_constructor_exists():
    assert callable(defaultname_ListElement.__init__)


def test_defaultname_listelement_constructor_args():
    sig = inspect.signature(defaultname_ListElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_defaultname_listelement_has_type():
    assert hasattr(defaultname_ListElement, "type")
    descriptor = None
    for klass in defaultname_ListElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_option_is_not_abstract():
    assert not inspect.isabstract(defaultname_OPTION)


def test_defaultname_option_constructor_exists():
    assert callable(defaultname_OPTION.__init__)


def test_defaultname_option_constructor_args():
    sig = inspect.signature(defaultname_OPTION.__init__)
    params = list(sig.parameters.keys())
    assert "optionValue" in params, "Missing parameter 'optionValue'"
    assert "selected" in params, "Missing parameter 'selected'"

def test_defaultname_option_has_optionValue():
    assert hasattr(defaultname_OPTION, "optionValue")
    descriptor = None
    for klass in defaultname_OPTION.__mro__:
        if "optionValue" in klass.__dict__:
            descriptor = klass.__dict__["optionValue"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_option_has_selected():
    assert hasattr(defaultname_OPTION, "selected")
    descriptor = None
    for klass in defaultname_OPTION.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_select_is_not_abstract():
    assert not inspect.isabstract(defaultname_SELECT)


def test_defaultname_select_constructor_exists():
    assert callable(defaultname_SELECT.__init__)


def test_defaultname_select_constructor_args():
    sig = inspect.signature(defaultname_SELECT.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "size" in params, "Missing parameter 'size'"
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_defaultname_select_has_name():
    assert hasattr(defaultname_SELECT, "name")
    descriptor = None
    for klass in defaultname_SELECT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_select_has_size():
    assert hasattr(defaultname_SELECT, "size")
    descriptor = None
    for klass in defaultname_SELECT.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_select_has_multiple():
    assert hasattr(defaultname_SELECT, "multiple")
    descriptor = None
    for klass in defaultname_SELECT.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TABLEElement)


def test_tableelement_constructor_exists():
    assert callable(TABLEElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TABLEElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_table_is_not_abstract():
    assert not inspect.isabstract(defaultname_TABLE)


def test_defaultname_table_constructor_exists():
    assert callable(defaultname_TABLE.__init__)


def test_defaultname_table_constructor_args():
    sig = inspect.signature(defaultname_TABLE.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "cellspacing" in params, "Missing parameter 'cellspacing'"
    assert "border" in params, "Missing parameter 'border'"
    assert "cellpadding" in params, "Missing parameter 'cellpadding'"

def test_defaultname_table_has_width():
    assert hasattr(defaultname_TABLE, "width")
    descriptor = None
    for klass in defaultname_TABLE.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_table_has_cellspacing():
    assert hasattr(defaultname_TABLE, "cellspacing")
    descriptor = None
    for klass in defaultname_TABLE.__mro__:
        if "cellspacing" in klass.__dict__:
            descriptor = klass.__dict__["cellspacing"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_table_has_border():
    assert hasattr(defaultname_TABLE, "border")
    descriptor = None
    for klass in defaultname_TABLE.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_table_has_cellpadding():
    assert hasattr(defaultname_TABLE, "cellpadding")
    descriptor = None
    for klass in defaultname_TABLE.__mro__:
        if "cellpadding" in klass.__dict__:
            descriptor = klass.__dict__["cellpadding"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_input_is_not_abstract():
    assert not inspect.isabstract(defaultname_INPUT)


def test_defaultname_input_constructor_exists():
    assert callable(defaultname_INPUT.__init__)


def test_defaultname_input_constructor_args():
    sig = inspect.signature(defaultname_INPUT.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "src" in params, "Missing parameter 'src'"
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "maxlength" in params, "Missing parameter 'maxlength'"
    assert "inputValue" in params, "Missing parameter 'inputValue'"
    assert "checked" in params, "Missing parameter 'checked'"
    assert "align" in params, "Missing parameter 'align'"

def test_defaultname_input_has_size():
    assert hasattr(defaultname_INPUT, "size")
    descriptor = None
    for klass in defaultname_INPUT.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_input_has_src():
    assert hasattr(defaultname_INPUT, "src")
    descriptor = None
    for klass in defaultname_INPUT.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_input_has_type():
    assert hasattr(defaultname_INPUT, "type")
    descriptor = None
    for klass in defaultname_INPUT.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_input_has_name():
    assert hasattr(defaultname_INPUT, "name")
    descriptor = None
    for klass in defaultname_INPUT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_input_has_maxlength():
    assert hasattr(defaultname_INPUT, "maxlength")
    descriptor = None
    for klass in defaultname_INPUT.__mro__:
        if "maxlength" in klass.__dict__:
            descriptor = klass.__dict__["maxlength"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_input_has_inputValue():
    assert hasattr(defaultname_INPUT, "inputValue")
    descriptor = None
    for klass in defaultname_INPUT.__mro__:
        if "inputValue" in klass.__dict__:
            descriptor = klass.__dict__["inputValue"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_input_has_checked():
    assert hasattr(defaultname_INPUT, "checked")
    descriptor = None
    for klass in defaultname_INPUT.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_input_has_align():
    assert hasattr(defaultname_INPUT, "align")
    descriptor = None
    for klass in defaultname_INPUT.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_form_is_not_abstract():
    assert not inspect.isabstract(defaultname_FORM)


def test_defaultname_form_constructor_exists():
    assert callable(defaultname_FORM.__init__)


def test_defaultname_form_constructor_args():
    sig = inspect.signature(defaultname_FORM.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "method" in params, "Missing parameter 'method'"

def test_defaultname_form_has_action():
    assert hasattr(defaultname_FORM, "action")
    descriptor = None
    for klass in defaultname_FORM.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_form_has_method():
    assert hasattr(defaultname_FORM, "method")
    descriptor = None
    for klass in defaultname_FORM.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_td_is_not_abstract():
    assert not inspect.isabstract(TD)


def test_td_constructor_exists():
    assert callable(TD.__init__)


def test_td_constructor_args():
    sig = inspect.signature(TD.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_th_is_not_abstract():
    assert not inspect.isabstract(defaultname_TH)


def test_defaultname_th_constructor_exists():
    assert callable(defaultname_TH.__init__)


def test_defaultname_th_constructor_args():
    sig = inspect.signature(defaultname_TH.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_td_is_not_abstract():
    assert not inspect.isabstract(defaultname_TD)


def test_defaultname_td_constructor_exists():
    assert callable(defaultname_TD.__init__)


def test_defaultname_td_constructor_args():
    sig = inspect.signature(defaultname_TD.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "width" in params, "Missing parameter 'width'"

def test_defaultname_td_has_align():
    assert hasattr(defaultname_TD, "align")
    descriptor = None
    for klass in defaultname_TD.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_td_has_rowspan():
    assert hasattr(defaultname_TD, "rowspan")
    descriptor = None
    for klass in defaultname_TD.__mro__:
        if "rowspan" in klass.__dict__:
            descriptor = klass.__dict__["rowspan"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_td_has_colspan():
    assert hasattr(defaultname_TD, "colspan")
    descriptor = None
    for klass in defaultname_TD.__mro__:
        if "colspan" in klass.__dict__:
            descriptor = klass.__dict__["colspan"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_td_has_valign():
    assert hasattr(defaultname_TD, "valign")
    descriptor = None
    for klass in defaultname_TD.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_td_has_width():
    assert hasattr(defaultname_TD, "width")
    descriptor = None
    for klass in defaultname_TD.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_tr_is_not_abstract():
    assert not inspect.isabstract(defaultname_TR)


def test_defaultname_tr_constructor_exists():
    assert callable(defaultname_TR.__init__)


def test_defaultname_tr_constructor_args():
    sig = inspect.signature(defaultname_TR.__init__)
    params = list(sig.parameters.keys())
    assert "valign" in params, "Missing parameter 'valign'"
    assert "align" in params, "Missing parameter 'align'"

def test_defaultname_tr_has_valign():
    assert hasattr(defaultname_TR, "valign")
    descriptor = None
    for klass in defaultname_TR.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_tr_has_align():
    assert hasattr(defaultname_TR, "align")
    descriptor = None
    for klass in defaultname_TR.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_bodyelement_is_not_abstract():
    assert not inspect.isabstract(BODYElement)


def test_bodyelement_constructor_exists():
    assert callable(BODYElement.__init__)


def test_bodyelement_constructor_args():
    sig = inspect.signature(BODYElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_area_is_not_abstract():
    assert not inspect.isabstract(defaultname_AREA)


def test_defaultname_area_constructor_exists():
    assert callable(defaultname_AREA.__init__)


def test_defaultname_area_constructor_args():
    sig = inspect.signature(defaultname_AREA.__init__)
    params = list(sig.parameters.keys())
    assert "ahref" in params, "Missing parameter 'ahref'"
    assert "coords" in params, "Missing parameter 'coords'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_defaultname_area_has_ahref():
    assert hasattr(defaultname_AREA, "ahref")
    descriptor = None
    for klass in defaultname_AREA.__mro__:
        if "ahref" in klass.__dict__:
            descriptor = klass.__dict__["ahref"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_area_has_coords():
    assert hasattr(defaultname_AREA, "coords")
    descriptor = None
    for klass in defaultname_AREA.__mro__:
        if "coords" in klass.__dict__:
            descriptor = klass.__dict__["coords"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_area_has_shape():
    assert hasattr(defaultname_AREA, "shape")
    descriptor = None
    for klass in defaultname_AREA.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_div_is_not_abstract():
    assert not inspect.isabstract(defaultname_DIV)


def test_defaultname_div_constructor_exists():
    assert callable(defaultname_DIV.__init__)


def test_defaultname_div_constructor_args():
    sig = inspect.signature(defaultname_DIV.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_defaultname_div_has_align():
    assert hasattr(defaultname_DIV, "align")
    descriptor = None
    for klass in defaultname_DIV.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_pre_is_not_abstract():
    assert not inspect.isabstract(defaultname_PRE)


def test_defaultname_pre_constructor_exists():
    assert callable(defaultname_PRE.__init__)


def test_defaultname_pre_constructor_args():
    sig = inspect.signature(defaultname_PRE.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_h3_is_not_abstract():
    assert not inspect.isabstract(defaultname_H3)


def test_defaultname_h3_constructor_exists():
    assert callable(defaultname_H3.__init__)


def test_defaultname_h3_constructor_args():
    sig = inspect.signature(defaultname_H3.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_map_is_not_abstract():
    assert not inspect.isabstract(defaultname_MAP)


def test_defaultname_map_constructor_exists():
    assert callable(defaultname_MAP.__init__)


def test_defaultname_map_constructor_args():
    sig = inspect.signature(defaultname_MAP.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_p_is_not_abstract():
    assert not inspect.isabstract(defaultname_P)


def test_defaultname_p_constructor_exists():
    assert callable(defaultname_P.__init__)


def test_defaultname_p_constructor_args():
    sig = inspect.signature(defaultname_P.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_b_is_not_abstract():
    assert not inspect.isabstract(defaultname_B)


def test_defaultname_b_constructor_exists():
    assert callable(defaultname_B.__init__)


def test_defaultname_b_constructor_args():
    sig = inspect.signature(defaultname_B.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_i_is_not_abstract():
    assert not inspect.isabstract(defaultname_I)


def test_defaultname_i_constructor_exists():
    assert callable(defaultname_I.__init__)


def test_defaultname_i_constructor_args():
    sig = inspect.signature(defaultname_I.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_br_is_not_abstract():
    assert not inspect.isabstract(defaultname_BR)


def test_defaultname_br_constructor_exists():
    assert callable(defaultname_BR.__init__)


def test_defaultname_br_constructor_args():
    sig = inspect.signature(defaultname_BR.__init__)
    params = list(sig.parameters.keys())
    assert "clear" in params, "Missing parameter 'clear'"

def test_defaultname_br_has_clear():
    assert hasattr(defaultname_BR, "clear")
    descriptor = None
    for klass in defaultname_BR.__mro__:
        if "clear" in klass.__dict__:
            descriptor = klass.__dict__["clear"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_font_is_not_abstract():
    assert not inspect.isabstract(defaultname_FONT)


def test_defaultname_font_constructor_exists():
    assert callable(defaultname_FONT.__init__)


def test_defaultname_font_constructor_args():
    sig = inspect.signature(defaultname_FONT.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "color" in params, "Missing parameter 'color'"
    assert "face" in params, "Missing parameter 'face'"

def test_defaultname_font_has_size():
    assert hasattr(defaultname_FONT, "size")
    descriptor = None
    for klass in defaultname_FONT.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_font_has_color():
    assert hasattr(defaultname_FONT, "color")
    descriptor = None
    for klass in defaultname_FONT.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_font_has_face():
    assert hasattr(defaultname_FONT, "face")
    descriptor = None
    for klass in defaultname_FONT.__mro__:
        if "face" in klass.__dict__:
            descriptor = klass.__dict__["face"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_h2_is_not_abstract():
    assert not inspect.isabstract(defaultname_H2)


def test_defaultname_h2_constructor_exists():
    assert callable(defaultname_H2.__init__)


def test_defaultname_h2_constructor_args():
    sig = inspect.signature(defaultname_H2.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_small_is_not_abstract():
    assert not inspect.isabstract(defaultname_SMALL)


def test_defaultname_small_constructor_exists():
    assert callable(defaultname_SMALL.__init__)


def test_defaultname_small_constructor_args():
    sig = inspect.signature(defaultname_SMALL.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_sub_is_not_abstract():
    assert not inspect.isabstract(defaultname_SUB)


def test_defaultname_sub_constructor_exists():
    assert callable(defaultname_SUB.__init__)


def test_defaultname_sub_constructor_args():
    sig = inspect.signature(defaultname_SUB.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_a_is_not_abstract():
    assert not inspect.isabstract(defaultname_A)


def test_defaultname_a_constructor_exists():
    assert callable(defaultname_A.__init__)


def test_defaultname_a_constructor_args():
    sig = inspect.signature(defaultname_A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "ahref" in params, "Missing parameter 'ahref'"

def test_defaultname_a_has_name():
    assert hasattr(defaultname_A, "name")
    descriptor = None
    for klass in defaultname_A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_a_has_id():
    assert hasattr(defaultname_A, "id")
    descriptor = None
    for klass in defaultname_A.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_a_has_ahref():
    assert hasattr(defaultname_A, "ahref")
    descriptor = None
    for klass in defaultname_A.__mro__:
        if "ahref" in klass.__dict__:
            descriptor = klass.__dict__["ahref"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_sup_is_not_abstract():
    assert not inspect.isabstract(defaultname_SUP)


def test_defaultname_sup_constructor_exists():
    assert callable(defaultname_SUP.__init__)


def test_defaultname_sup_constructor_args():
    sig = inspect.signature(defaultname_SUP.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_img_is_not_abstract():
    assert not inspect.isabstract(defaultname_IMG)


def test_defaultname_img_constructor_exists():
    assert callable(defaultname_IMG.__init__)


def test_defaultname_img_constructor_args():
    sig = inspect.signature(defaultname_IMG.__init__)
    params = list(sig.parameters.keys())
    assert "height" in params, "Missing parameter 'height'"
    assert "src" in params, "Missing parameter 'src'"
    assert "align" in params, "Missing parameter 'align'"
    assert "width" in params, "Missing parameter 'width'"
    assert "hspace" in params, "Missing parameter 'hspace'"
    assert "usemap" in params, "Missing parameter 'usemap'"
    assert "alt" in params, "Missing parameter 'alt'"
    assert "vspace" in params, "Missing parameter 'vspace'"
    assert "ismap" in params, "Missing parameter 'ismap'"
    assert "border" in params, "Missing parameter 'border'"

def test_defaultname_img_has_height():
    assert hasattr(defaultname_IMG, "height")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_src():
    assert hasattr(defaultname_IMG, "src")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_align():
    assert hasattr(defaultname_IMG, "align")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_width():
    assert hasattr(defaultname_IMG, "width")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_hspace():
    assert hasattr(defaultname_IMG, "hspace")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "hspace" in klass.__dict__:
            descriptor = klass.__dict__["hspace"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_usemap():
    assert hasattr(defaultname_IMG, "usemap")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "usemap" in klass.__dict__:
            descriptor = klass.__dict__["usemap"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_alt():
    assert hasattr(defaultname_IMG, "alt")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "alt" in klass.__dict__:
            descriptor = klass.__dict__["alt"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_vspace():
    assert hasattr(defaultname_IMG, "vspace")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "vspace" in klass.__dict__:
            descriptor = klass.__dict__["vspace"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_ismap():
    assert hasattr(defaultname_IMG, "ismap")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "ismap" in klass.__dict__:
            descriptor = klass.__dict__["ismap"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_img_has_border():
    assert hasattr(defaultname_IMG, "border")
    descriptor = None
    for klass in defaultname_IMG.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_strike_is_not_abstract():
    assert not inspect.isabstract(defaultname_STRIKE)


def test_defaultname_strike_constructor_exists():
    assert callable(defaultname_STRIKE.__init__)


def test_defaultname_strike_constructor_args():
    sig = inspect.signature(defaultname_STRIKE.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_em_is_not_abstract():
    assert not inspect.isabstract(defaultname_EM)


def test_defaultname_em_constructor_exists():
    assert callable(defaultname_EM.__init__)


def test_defaultname_em_constructor_args():
    sig = inspect.signature(defaultname_EM.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_embed_is_not_abstract():
    assert not inspect.isabstract(defaultname_EMBED)


def test_defaultname_embed_constructor_exists():
    assert callable(defaultname_EMBED.__init__)


def test_defaultname_embed_constructor_args():
    sig = inspect.signature(defaultname_EMBED.__init__)
    params = list(sig.parameters.keys())
    assert "src" in params, "Missing parameter 'src'"
    assert "hspace" in params, "Missing parameter 'hspace'"
    assert "align" in params, "Missing parameter 'align'"
    assert "width" in params, "Missing parameter 'width'"
    assert "border" in params, "Missing parameter 'border'"
    assert "vspace" in params, "Missing parameter 'vspace'"
    assert "height" in params, "Missing parameter 'height'"

def test_defaultname_embed_has_src():
    assert hasattr(defaultname_EMBED, "src")
    descriptor = None
    for klass in defaultname_EMBED.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_embed_has_hspace():
    assert hasattr(defaultname_EMBED, "hspace")
    descriptor = None
    for klass in defaultname_EMBED.__mro__:
        if "hspace" in klass.__dict__:
            descriptor = klass.__dict__["hspace"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_embed_has_align():
    assert hasattr(defaultname_EMBED, "align")
    descriptor = None
    for klass in defaultname_EMBED.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_embed_has_width():
    assert hasattr(defaultname_EMBED, "width")
    descriptor = None
    for klass in defaultname_EMBED.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_embed_has_border():
    assert hasattr(defaultname_EMBED, "border")
    descriptor = None
    for klass in defaultname_EMBED.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_embed_has_vspace():
    assert hasattr(defaultname_EMBED, "vspace")
    descriptor = None
    for klass in defaultname_EMBED.__mro__:
        if "vspace" in klass.__dict__:
            descriptor = klass.__dict__["vspace"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_embed_has_height():
    assert hasattr(defaultname_EMBED, "height")
    descriptor = None
    for klass in defaultname_EMBED.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_big_is_not_abstract():
    assert not inspect.isabstract(defaultname_BIG)


def test_defaultname_big_constructor_exists():
    assert callable(defaultname_BIG.__init__)


def test_defaultname_big_constructor_args():
    sig = inspect.signature(defaultname_BIG.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_span_is_not_abstract():
    assert not inspect.isabstract(defaultname_SPAN)


def test_defaultname_span_constructor_exists():
    assert callable(defaultname_SPAN.__init__)


def test_defaultname_span_constructor_args():
    sig = inspect.signature(defaultname_SPAN.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"

def test_defaultname_span_has_style():
    assert hasattr(defaultname_SPAN, "style")
    descriptor = None
    for klass in defaultname_SPAN.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_strong_is_not_abstract():
    assert not inspect.isabstract(defaultname_STRONG)


def test_defaultname_strong_constructor_exists():
    assert callable(defaultname_STRONG.__init__)


def test_defaultname_strong_constructor_args():
    sig = inspect.signature(defaultname_STRONG.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_h4_is_not_abstract():
    assert not inspect.isabstract(defaultname_H4)


def test_defaultname_h4_constructor_exists():
    assert callable(defaultname_H4.__init__)


def test_defaultname_h4_constructor_args():
    sig = inspect.signature(defaultname_H4.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_tt_is_not_abstract():
    assert not inspect.isabstract(defaultname_TT)


def test_defaultname_tt_constructor_exists():
    assert callable(defaultname_TT.__init__)


def test_defaultname_tt_constructor_args():
    sig = inspect.signature(defaultname_TT.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_noembed_is_not_abstract():
    assert not inspect.isabstract(defaultname_NOEMBED)


def test_defaultname_noembed_constructor_exists():
    assert callable(defaultname_NOEMBED.__init__)


def test_defaultname_noembed_constructor_args():
    sig = inspect.signature(defaultname_NOEMBED.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_tableelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_TABLEElement)


def test_defaultname_tableelement_constructor_exists():
    assert callable(defaultname_TABLEElement.__init__)


def test_defaultname_tableelement_constructor_args():
    sig = inspect.signature(defaultname_TABLEElement.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"

def test_defaultname_tableelement_has_background():
    assert hasattr(defaultname_TABLEElement, "background")
    descriptor = None
    for klass in defaultname_TABLEElement.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_tableelement_has_bgcolor():
    assert hasattr(defaultname_TABLEElement, "bgcolor")
    descriptor = None
    for klass in defaultname_TABLEElement.__mro__:
        if "bgcolor" in klass.__dict__:
            descriptor = klass.__dict__["bgcolor"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_style_is_not_abstract():
    assert not inspect.isabstract(defaultname_STYLE)


def test_defaultname_style_constructor_exists():
    assert callable(defaultname_STYLE.__init__)


def test_defaultname_style_constructor_args():
    sig = inspect.signature(defaultname_STYLE.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_h1_is_not_abstract():
    assert not inspect.isabstract(defaultname_H1)


def test_defaultname_h1_constructor_exists():
    assert callable(defaultname_H1.__init__)


def test_defaultname_h1_constructor_args():
    sig = inspect.signature(defaultname_H1.__init__)
    params = list(sig.parameters.keys())



def test_headelement_is_not_abstract():
    assert not inspect.isabstract(HEADElement)


def test_headelement_constructor_exists():
    assert callable(HEADElement.__init__)


def test_headelement_constructor_args():
    sig = inspect.signature(HEADElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_title_is_not_abstract():
    assert not inspect.isabstract(defaultname_TITLE)


def test_defaultname_title_constructor_exists():
    assert callable(defaultname_TITLE.__init__)


def test_defaultname_title_constructor_args():
    sig = inspect.signature(defaultname_TITLE.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_link_is_not_abstract():
    assert not inspect.isabstract(defaultname_LINK)


def test_defaultname_link_constructor_exists():
    assert callable(defaultname_LINK.__init__)


def test_defaultname_link_constructor_args():
    sig = inspect.signature(defaultname_LINK.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "type" in params, "Missing parameter 'type'"
    assert "ahref" in params, "Missing parameter 'ahref'"
    assert "rel" in params, "Missing parameter 'rel'"

def test_defaultname_link_has_title():
    assert hasattr(defaultname_LINK, "title")
    descriptor = None
    for klass in defaultname_LINK.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_link_has_type():
    assert hasattr(defaultname_LINK, "type")
    descriptor = None
    for klass in defaultname_LINK.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_link_has_ahref():
    assert hasattr(defaultname_LINK, "ahref")
    descriptor = None
    for klass in defaultname_LINK.__mro__:
        if "ahref" in klass.__dict__:
            descriptor = klass.__dict__["ahref"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_link_has_rel():
    assert hasattr(defaultname_LINK, "rel")
    descriptor = None
    for klass in defaultname_LINK.__mro__:
        if "rel" in klass.__dict__:
            descriptor = klass.__dict__["rel"]
            break
    assert isinstance(descriptor, property)



def test_htmlelement_is_not_abstract():
    assert not inspect.isabstract(HTMLElement)


def test_htmlelement_constructor_exists():
    assert callable(HTMLElement.__init__)


def test_htmlelement_constructor_args():
    sig = inspect.signature(HTMLElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_headelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_HEADElement)


def test_defaultname_headelement_constructor_exists():
    assert callable(defaultname_HEADElement.__init__)


def test_defaultname_headelement_constructor_args():
    sig = inspect.signature(defaultname_HEADElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_bodyelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_BODYElement)


def test_defaultname_bodyelement_constructor_exists():
    assert callable(defaultname_BODYElement.__init__)


def test_defaultname_bodyelement_constructor_args():
    sig = inspect.signature(defaultname_BODYElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_body_is_not_abstract():
    assert not inspect.isabstract(defaultname_BODY)


def test_defaultname_body_constructor_exists():
    assert callable(defaultname_BODY.__init__)


def test_defaultname_body_constructor_args():
    sig = inspect.signature(defaultname_BODY.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "vlink" in params, "Missing parameter 'vlink'"
    assert "link" in params, "Missing parameter 'link'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"
    assert "alink" in params, "Missing parameter 'alink'"
    assert "text" in params, "Missing parameter 'text'"

def test_defaultname_body_has_background():
    assert hasattr(defaultname_BODY, "background")
    descriptor = None
    for klass in defaultname_BODY.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_body_has_vlink():
    assert hasattr(defaultname_BODY, "vlink")
    descriptor = None
    for klass in defaultname_BODY.__mro__:
        if "vlink" in klass.__dict__:
            descriptor = klass.__dict__["vlink"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_body_has_link():
    assert hasattr(defaultname_BODY, "link")
    descriptor = None
    for klass in defaultname_BODY.__mro__:
        if "link" in klass.__dict__:
            descriptor = klass.__dict__["link"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_body_has_bgcolor():
    assert hasattr(defaultname_BODY, "bgcolor")
    descriptor = None
    for klass in defaultname_BODY.__mro__:
        if "bgcolor" in klass.__dict__:
            descriptor = klass.__dict__["bgcolor"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_body_has_alink():
    assert hasattr(defaultname_BODY, "alink")
    descriptor = None
    for klass in defaultname_BODY.__mro__:
        if "alink" in klass.__dict__:
            descriptor = klass.__dict__["alink"]
            break
    assert isinstance(descriptor, property)

def test_defaultname_body_has_text():
    assert hasattr(defaultname_BODY, "text")
    descriptor = None
    for klass in defaultname_BODY.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_htmlelement_is_not_abstract():
    assert not inspect.isabstract(defaultname_HTMLElement)


def test_defaultname_htmlelement_constructor_exists():
    assert callable(defaultname_HTMLElement.__init__)


def test_defaultname_htmlelement_constructor_args():
    sig = inspect.signature(defaultname_HTMLElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_defaultname_htmlelement_has_value():
    assert hasattr(defaultname_HTMLElement, "value")
    descriptor = None
    for klass in defaultname_HTMLElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_defaultname_head_is_not_abstract():
    assert not inspect.isabstract(defaultname_HEAD)


def test_defaultname_head_constructor_exists():
    assert callable(defaultname_HEAD.__init__)


def test_defaultname_head_constructor_args():
    sig = inspect.signature(defaultname_HEAD.__init__)
    params = list(sig.parameters.keys())



def test_defaultname_html_is_not_abstract():
    assert not inspect.isabstract(defaultname_HTML)


def test_defaultname_html_constructor_exists():
    assert callable(defaultname_HTML.__init__)


def test_defaultname_html_constructor_args():
    sig = inspect.signature(defaultname_HTML.__init__)
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
defaultname_FRAMESET_strategy = st.builds(
    defaultname_FRAMESET,
    border=
        safe_text,
    framespacing=
        safe_text,
    frameborder=
        safe_text,
    cols=
        safe_text,
    rows=
        safe_text
)
FRAME_strategy = st.builds(
    FRAME,
)
defaultname_IFRAME_strategy = st.builds(
    defaultname_IFRAME,
)
defaultname_NOFRAME_strategy = st.builds(
    defaultname_NOFRAME,
)
defaultname_FRAME_strategy = st.builds(
    defaultname_FRAME,
    scrolling=
        safe_text,
    marginheight=
        safe_text,
    marginwidth=
        safe_text,
    noresize=
        safe_text,
    src=
        safe_text,
    name=
        safe_text
)
defaultname_TEXTAREA_strategy = st.builds(
    defaultname_TEXTAREA,
    name=
        safe_text,
    cols=
        safe_text,
    rows=
        safe_text
)
defaultname_OBJECT_strategy = st.builds(
    defaultname_OBJECT,
    standby=
        safe_text,
    type=
        safe_text,
    classid=
        safe_text,
    id=
        safe_text,
    data=
        safe_text
)
defaultname_PARAM_strategy = st.builds(
    defaultname_PARAM,
    name=
        safe_text,
    paramValue=
        safe_text
)
defaultname_APPLET_strategy = st.builds(
    defaultname_APPLET,
    height=
        safe_text,
    src=
        safe_text,
    class_=
        safe_text,
    width=
        safe_text,
    applet=
        safe_text,
    align=
        safe_text
)
defaultname_DD_strategy = st.builds(
    defaultname_DD,
)
defaultname_DT_strategy = st.builds(
    defaultname_DT,
)
defaultname_DL_strategy = st.builds(
    defaultname_DL,
)
ListElement_strategy = st.builds(
    ListElement,
)
defaultname_LI_strategy = st.builds(
    defaultname_LI,
    liValue=
        safe_text
)
defaultname_UL_strategy = st.builds(
    defaultname_UL,
)
defaultname_OL_strategy = st.builds(
    defaultname_OL,
    start=
        safe_text
)
defaultname_ListElement_strategy = st.builds(
    defaultname_ListElement,
    type=
        safe_text
)
defaultname_OPTION_strategy = st.builds(
    defaultname_OPTION,
    optionValue=
        safe_text,
    selected=
        safe_text
)
defaultname_SELECT_strategy = st.builds(
    defaultname_SELECT,
    name=
        safe_text,
    size=
        safe_text,
    multiple=
        safe_text
)
TABLEElement_strategy = st.builds(
    TABLEElement,
)
defaultname_TABLE_strategy = st.builds(
    defaultname_TABLE,
    width=
        safe_text,
    cellspacing=
        safe_text,
    border=
        safe_text,
    cellpadding=
        safe_text
)
defaultname_INPUT_strategy = st.builds(
    defaultname_INPUT,
    size=
        safe_text,
    src=
        safe_text,
    type=
        safe_text,
    name=
        safe_text,
    maxlength=
        safe_text,
    inputValue=
        safe_text,
    checked=
        safe_text,
    align=
        safe_text
)
defaultname_FORM_strategy = st.builds(
    defaultname_FORM,
    action=
        safe_text,
    method=
        safe_text
)
TD_strategy = st.builds(
    TD,
)
defaultname_TH_strategy = st.builds(
    defaultname_TH,
)
defaultname_TD_strategy = st.builds(
    defaultname_TD,
    align=
        safe_text,
    rowspan=
        safe_text,
    colspan=
        safe_text,
    valign=
        safe_text,
    width=
        safe_text
)
defaultname_TR_strategy = st.builds(
    defaultname_TR,
    valign=
        safe_text,
    align=
        safe_text
)
BODYElement_strategy = st.builds(
    BODYElement,
)
defaultname_AREA_strategy = st.builds(
    defaultname_AREA,
    ahref=
        safe_text,
    coords=
        safe_text,
    shape=
        safe_text
)
defaultname_DIV_strategy = st.builds(
    defaultname_DIV,
    align=
        safe_text
)
defaultname_PRE_strategy = st.builds(
    defaultname_PRE,
)
defaultname_H3_strategy = st.builds(
    defaultname_H3,
)
defaultname_MAP_strategy = st.builds(
    defaultname_MAP,
)
defaultname_P_strategy = st.builds(
    defaultname_P,
)
defaultname_B_strategy = st.builds(
    defaultname_B,
)
defaultname_I_strategy = st.builds(
    defaultname_I,
)
defaultname_BR_strategy = st.builds(
    defaultname_BR,
    clear=
        safe_text
)
defaultname_FONT_strategy = st.builds(
    defaultname_FONT,
    size=
        safe_text,
    color=
        safe_text,
    face=
        safe_text
)
defaultname_H2_strategy = st.builds(
    defaultname_H2,
)
defaultname_SMALL_strategy = st.builds(
    defaultname_SMALL,
)
defaultname_SUB_strategy = st.builds(
    defaultname_SUB,
)
defaultname_A_strategy = st.builds(
    defaultname_A,
    name=
        safe_text,
    id=
        safe_text,
    ahref=
        safe_text
)
defaultname_SUP_strategy = st.builds(
    defaultname_SUP,
)
defaultname_IMG_strategy = st.builds(
    defaultname_IMG,
    height=
        safe_text,
    src=
        safe_text,
    align=
        safe_text,
    width=
        safe_text,
    hspace=
        safe_text,
    usemap=
        safe_text,
    alt=
        safe_text,
    vspace=
        safe_text,
    ismap=
        safe_text,
    border=
        safe_text
)
defaultname_STRIKE_strategy = st.builds(
    defaultname_STRIKE,
)
defaultname_EM_strategy = st.builds(
    defaultname_EM,
)
defaultname_EMBED_strategy = st.builds(
    defaultname_EMBED,
    src=
        safe_text,
    hspace=
        safe_text,
    align=
        safe_text,
    width=
        safe_text,
    border=
        safe_text,
    vspace=
        safe_text,
    height=
        safe_text
)
defaultname_BIG_strategy = st.builds(
    defaultname_BIG,
)
defaultname_SPAN_strategy = st.builds(
    defaultname_SPAN,
    style=
        safe_text
)
defaultname_STRONG_strategy = st.builds(
    defaultname_STRONG,
)
defaultname_H4_strategy = st.builds(
    defaultname_H4,
)
defaultname_TT_strategy = st.builds(
    defaultname_TT,
)
defaultname_NOEMBED_strategy = st.builds(
    defaultname_NOEMBED,
)
defaultname_TABLEElement_strategy = st.builds(
    defaultname_TABLEElement,
    background=
        safe_text,
    bgcolor=
        safe_text
)
defaultname_STYLE_strategy = st.builds(
    defaultname_STYLE,
)
defaultname_H1_strategy = st.builds(
    defaultname_H1,
)
HEADElement_strategy = st.builds(
    HEADElement,
)
defaultname_TITLE_strategy = st.builds(
    defaultname_TITLE,
)
defaultname_LINK_strategy = st.builds(
    defaultname_LINK,
    title=
        safe_text,
    type=
        safe_text,
    ahref=
        safe_text,
    rel=
        safe_text
)
HTMLElement_strategy = st.builds(
    HTMLElement,
)
defaultname_HEADElement_strategy = st.builds(
    defaultname_HEADElement,
)
defaultname_BODYElement_strategy = st.builds(
    defaultname_BODYElement,
)
defaultname_BODY_strategy = st.builds(
    defaultname_BODY,
    background=
        safe_text,
    vlink=
        safe_text,
    link=
        safe_text,
    bgcolor=
        safe_text,
    alink=
        safe_text,
    text=
        safe_text
)
defaultname_HTMLElement_strategy = st.builds(
    defaultname_HTMLElement,
    value=
        safe_text
)
defaultname_HEAD_strategy = st.builds(
    defaultname_HEAD,
)
defaultname_HTML_strategy = st.builds(
    defaultname_HTML,
)

@given(instance=defaultname_FRAMESET_strategy)
@settings(max_examples=50)
def test_defaultname_frameset_instantiation(instance):
    assert isinstance(instance, defaultname_FRAMESET)



@given(instance=defaultname_FRAMESET_strategy)
def test_defaultname_frameset_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=defaultname_FRAMESET_strategy)
def test_defaultname_frameset_framespacing_setter(instance):
    original = instance.framespacing
    instance.framespacing = original
    assert instance.framespacing == original



@given(instance=defaultname_FRAMESET_strategy)
def test_defaultname_frameset_frameborder_setter(instance):
    original = instance.frameborder
    instance.frameborder = original
    assert instance.frameborder == original



@given(instance=defaultname_FRAMESET_strategy)
def test_defaultname_frameset_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original



@given(instance=defaultname_FRAMESET_strategy)
def test_defaultname_frameset_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=FRAME_strategy)
@settings(max_examples=50)
def test_frame_instantiation(instance):
    assert isinstance(instance, FRAME)

@given(instance=defaultname_IFRAME_strategy)
@settings(max_examples=50)
def test_defaultname_iframe_instantiation(instance):
    assert isinstance(instance, defaultname_IFRAME)

@given(instance=defaultname_NOFRAME_strategy)
@settings(max_examples=50)
def test_defaultname_noframe_instantiation(instance):
    assert isinstance(instance, defaultname_NOFRAME)

@given(instance=defaultname_FRAME_strategy)
@settings(max_examples=50)
def test_defaultname_frame_instantiation(instance):
    assert isinstance(instance, defaultname_FRAME)



@given(instance=defaultname_FRAME_strategy)
def test_defaultname_frame_scrolling_setter(instance):
    original = instance.scrolling
    instance.scrolling = original
    assert instance.scrolling == original



@given(instance=defaultname_FRAME_strategy)
def test_defaultname_frame_marginheight_setter(instance):
    original = instance.marginheight
    instance.marginheight = original
    assert instance.marginheight == original



@given(instance=defaultname_FRAME_strategy)
def test_defaultname_frame_marginwidth_setter(instance):
    original = instance.marginwidth
    instance.marginwidth = original
    assert instance.marginwidth == original



@given(instance=defaultname_FRAME_strategy)
def test_defaultname_frame_noresize_setter(instance):
    original = instance.noresize
    instance.noresize = original
    assert instance.noresize == original



@given(instance=defaultname_FRAME_strategy)
def test_defaultname_frame_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_FRAME_strategy)
def test_defaultname_frame_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=defaultname_TEXTAREA_strategy)
@settings(max_examples=50)
def test_defaultname_textarea_instantiation(instance):
    assert isinstance(instance, defaultname_TEXTAREA)



@given(instance=defaultname_TEXTAREA_strategy)
def test_defaultname_textarea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_TEXTAREA_strategy)
def test_defaultname_textarea_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original



@given(instance=defaultname_TEXTAREA_strategy)
def test_defaultname_textarea_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=defaultname_OBJECT_strategy)
@settings(max_examples=50)
def test_defaultname_object_instantiation(instance):
    assert isinstance(instance, defaultname_OBJECT)



@given(instance=defaultname_OBJECT_strategy)
def test_defaultname_object_standby_setter(instance):
    original = instance.standby
    instance.standby = original
    assert instance.standby == original



@given(instance=defaultname_OBJECT_strategy)
def test_defaultname_object_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=defaultname_OBJECT_strategy)
def test_defaultname_object_classid_setter(instance):
    original = instance.classid
    instance.classid = original
    assert instance.classid == original



@given(instance=defaultname_OBJECT_strategy)
def test_defaultname_object_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=defaultname_OBJECT_strategy)
def test_defaultname_object_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=defaultname_PARAM_strategy)
@settings(max_examples=50)
def test_defaultname_param_instantiation(instance):
    assert isinstance(instance, defaultname_PARAM)



@given(instance=defaultname_PARAM_strategy)
def test_defaultname_param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_PARAM_strategy)
def test_defaultname_param_paramValue_setter(instance):
    original = instance.paramValue
    instance.paramValue = original
    assert instance.paramValue == original

@given(instance=defaultname_APPLET_strategy)
@settings(max_examples=50)
def test_defaultname_applet_instantiation(instance):
    assert isinstance(instance, defaultname_APPLET)



@given(instance=defaultname_APPLET_strategy)
def test_defaultname_applet_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=defaultname_APPLET_strategy)
def test_defaultname_applet_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_APPLET_strategy)
def test_defaultname_applet_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original



@given(instance=defaultname_APPLET_strategy)
def test_defaultname_applet_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=defaultname_APPLET_strategy)
def test_defaultname_applet_applet_setter(instance):
    original = instance.applet
    instance.applet = original
    assert instance.applet == original



@given(instance=defaultname_APPLET_strategy)
def test_defaultname_applet_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname_DD_strategy)
@settings(max_examples=50)
def test_defaultname_dd_instantiation(instance):
    assert isinstance(instance, defaultname_DD)

@given(instance=defaultname_DT_strategy)
@settings(max_examples=50)
def test_defaultname_dt_instantiation(instance):
    assert isinstance(instance, defaultname_DT)

@given(instance=defaultname_DL_strategy)
@settings(max_examples=50)
def test_defaultname_dl_instantiation(instance):
    assert isinstance(instance, defaultname_DL)

@given(instance=ListElement_strategy)
@settings(max_examples=50)
def test_listelement_instantiation(instance):
    assert isinstance(instance, ListElement)

@given(instance=defaultname_LI_strategy)
@settings(max_examples=50)
def test_defaultname_li_instantiation(instance):
    assert isinstance(instance, defaultname_LI)



@given(instance=defaultname_LI_strategy)
def test_defaultname_li_liValue_setter(instance):
    original = instance.liValue
    instance.liValue = original
    assert instance.liValue == original

@given(instance=defaultname_UL_strategy)
@settings(max_examples=50)
def test_defaultname_ul_instantiation(instance):
    assert isinstance(instance, defaultname_UL)

@given(instance=defaultname_OL_strategy)
@settings(max_examples=50)
def test_defaultname_ol_instantiation(instance):
    assert isinstance(instance, defaultname_OL)



@given(instance=defaultname_OL_strategy)
def test_defaultname_ol_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=defaultname_ListElement_strategy)
@settings(max_examples=50)
def test_defaultname_listelement_instantiation(instance):
    assert isinstance(instance, defaultname_ListElement)



@given(instance=defaultname_ListElement_strategy)
def test_defaultname_listelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=defaultname_OPTION_strategy)
@settings(max_examples=50)
def test_defaultname_option_instantiation(instance):
    assert isinstance(instance, defaultname_OPTION)



@given(instance=defaultname_OPTION_strategy)
def test_defaultname_option_optionValue_setter(instance):
    original = instance.optionValue
    instance.optionValue = original
    assert instance.optionValue == original



@given(instance=defaultname_OPTION_strategy)
def test_defaultname_option_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=defaultname_SELECT_strategy)
@settings(max_examples=50)
def test_defaultname_select_instantiation(instance):
    assert isinstance(instance, defaultname_SELECT)



@given(instance=defaultname_SELECT_strategy)
def test_defaultname_select_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_SELECT_strategy)
def test_defaultname_select_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=defaultname_SELECT_strategy)
def test_defaultname_select_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=TABLEElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TABLEElement)

@given(instance=defaultname_TABLE_strategy)
@settings(max_examples=50)
def test_defaultname_table_instantiation(instance):
    assert isinstance(instance, defaultname_TABLE)



@given(instance=defaultname_TABLE_strategy)
def test_defaultname_table_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=defaultname_TABLE_strategy)
def test_defaultname_table_cellspacing_setter(instance):
    original = instance.cellspacing
    instance.cellspacing = original
    assert instance.cellspacing == original



@given(instance=defaultname_TABLE_strategy)
def test_defaultname_table_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=defaultname_TABLE_strategy)
def test_defaultname_table_cellpadding_setter(instance):
    original = instance.cellpadding
    instance.cellpadding = original
    assert instance.cellpadding == original

@given(instance=defaultname_INPUT_strategy)
@settings(max_examples=50)
def test_defaultname_input_instantiation(instance):
    assert isinstance(instance, defaultname_INPUT)



@given(instance=defaultname_INPUT_strategy)
def test_defaultname_input_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=defaultname_INPUT_strategy)
def test_defaultname_input_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_INPUT_strategy)
def test_defaultname_input_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=defaultname_INPUT_strategy)
def test_defaultname_input_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_INPUT_strategy)
def test_defaultname_input_maxlength_setter(instance):
    original = instance.maxlength
    instance.maxlength = original
    assert instance.maxlength == original



@given(instance=defaultname_INPUT_strategy)
def test_defaultname_input_inputValue_setter(instance):
    original = instance.inputValue
    instance.inputValue = original
    assert instance.inputValue == original



@given(instance=defaultname_INPUT_strategy)
def test_defaultname_input_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original



@given(instance=defaultname_INPUT_strategy)
def test_defaultname_input_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname_FORM_strategy)
@settings(max_examples=50)
def test_defaultname_form_instantiation(instance):
    assert isinstance(instance, defaultname_FORM)



@given(instance=defaultname_FORM_strategy)
def test_defaultname_form_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original



@given(instance=defaultname_FORM_strategy)
def test_defaultname_form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=TD_strategy)
@settings(max_examples=50)
def test_td_instantiation(instance):
    assert isinstance(instance, TD)

@given(instance=defaultname_TH_strategy)
@settings(max_examples=50)
def test_defaultname_th_instantiation(instance):
    assert isinstance(instance, defaultname_TH)

@given(instance=defaultname_TD_strategy)
@settings(max_examples=50)
def test_defaultname_td_instantiation(instance):
    assert isinstance(instance, defaultname_TD)



@given(instance=defaultname_TD_strategy)
def test_defaultname_td_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=defaultname_TD_strategy)
def test_defaultname_td_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original



@given(instance=defaultname_TD_strategy)
def test_defaultname_td_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original



@given(instance=defaultname_TD_strategy)
def test_defaultname_td_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=defaultname_TD_strategy)
def test_defaultname_td_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=defaultname_TR_strategy)
@settings(max_examples=50)
def test_defaultname_tr_instantiation(instance):
    assert isinstance(instance, defaultname_TR)



@given(instance=defaultname_TR_strategy)
def test_defaultname_tr_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=defaultname_TR_strategy)
def test_defaultname_tr_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=BODYElement_strategy)
@settings(max_examples=50)
def test_bodyelement_instantiation(instance):
    assert isinstance(instance, BODYElement)

@given(instance=defaultname_AREA_strategy)
@settings(max_examples=50)
def test_defaultname_area_instantiation(instance):
    assert isinstance(instance, defaultname_AREA)



@given(instance=defaultname_AREA_strategy)
def test_defaultname_area_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original



@given(instance=defaultname_AREA_strategy)
def test_defaultname_area_coords_setter(instance):
    original = instance.coords
    instance.coords = original
    assert instance.coords == original



@given(instance=defaultname_AREA_strategy)
def test_defaultname_area_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=defaultname_DIV_strategy)
@settings(max_examples=50)
def test_defaultname_div_instantiation(instance):
    assert isinstance(instance, defaultname_DIV)



@given(instance=defaultname_DIV_strategy)
def test_defaultname_div_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname_PRE_strategy)
@settings(max_examples=50)
def test_defaultname_pre_instantiation(instance):
    assert isinstance(instance, defaultname_PRE)

@given(instance=defaultname_H3_strategy)
@settings(max_examples=50)
def test_defaultname_h3_instantiation(instance):
    assert isinstance(instance, defaultname_H3)

@given(instance=defaultname_MAP_strategy)
@settings(max_examples=50)
def test_defaultname_map_instantiation(instance):
    assert isinstance(instance, defaultname_MAP)

@given(instance=defaultname_P_strategy)
@settings(max_examples=50)
def test_defaultname_p_instantiation(instance):
    assert isinstance(instance, defaultname_P)

@given(instance=defaultname_B_strategy)
@settings(max_examples=50)
def test_defaultname_b_instantiation(instance):
    assert isinstance(instance, defaultname_B)

@given(instance=defaultname_I_strategy)
@settings(max_examples=50)
def test_defaultname_i_instantiation(instance):
    assert isinstance(instance, defaultname_I)

@given(instance=defaultname_BR_strategy)
@settings(max_examples=50)
def test_defaultname_br_instantiation(instance):
    assert isinstance(instance, defaultname_BR)



@given(instance=defaultname_BR_strategy)
def test_defaultname_br_clear_setter(instance):
    original = instance.clear
    instance.clear = original
    assert instance.clear == original

@given(instance=defaultname_FONT_strategy)
@settings(max_examples=50)
def test_defaultname_font_instantiation(instance):
    assert isinstance(instance, defaultname_FONT)



@given(instance=defaultname_FONT_strategy)
def test_defaultname_font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original



@given(instance=defaultname_FONT_strategy)
def test_defaultname_font_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original



@given(instance=defaultname_FONT_strategy)
def test_defaultname_font_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original

@given(instance=defaultname_H2_strategy)
@settings(max_examples=50)
def test_defaultname_h2_instantiation(instance):
    assert isinstance(instance, defaultname_H2)

@given(instance=defaultname_SMALL_strategy)
@settings(max_examples=50)
def test_defaultname_small_instantiation(instance):
    assert isinstance(instance, defaultname_SMALL)

@given(instance=defaultname_SUB_strategy)
@settings(max_examples=50)
def test_defaultname_sub_instantiation(instance):
    assert isinstance(instance, defaultname_SUB)

@given(instance=defaultname_A_strategy)
@settings(max_examples=50)
def test_defaultname_a_instantiation(instance):
    assert isinstance(instance, defaultname_A)



@given(instance=defaultname_A_strategy)
def test_defaultname_a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=defaultname_A_strategy)
def test_defaultname_a_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=defaultname_A_strategy)
def test_defaultname_a_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original

@given(instance=defaultname_SUP_strategy)
@settings(max_examples=50)
def test_defaultname_sup_instantiation(instance):
    assert isinstance(instance, defaultname_SUP)

@given(instance=defaultname_IMG_strategy)
@settings(max_examples=50)
def test_defaultname_img_instantiation(instance):
    assert isinstance(instance, defaultname_IMG)



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_hspace_setter(instance):
    original = instance.hspace
    instance.hspace = original
    assert instance.hspace == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_usemap_setter(instance):
    original = instance.usemap
    instance.usemap = original
    assert instance.usemap == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_vspace_setter(instance):
    original = instance.vspace
    instance.vspace = original
    assert instance.vspace == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_ismap_setter(instance):
    original = instance.ismap
    instance.ismap = original
    assert instance.ismap == original



@given(instance=defaultname_IMG_strategy)
def test_defaultname_img_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=defaultname_STRIKE_strategy)
@settings(max_examples=50)
def test_defaultname_strike_instantiation(instance):
    assert isinstance(instance, defaultname_STRIKE)

@given(instance=defaultname_EM_strategy)
@settings(max_examples=50)
def test_defaultname_em_instantiation(instance):
    assert isinstance(instance, defaultname_EM)

@given(instance=defaultname_EMBED_strategy)
@settings(max_examples=50)
def test_defaultname_embed_instantiation(instance):
    assert isinstance(instance, defaultname_EMBED)



@given(instance=defaultname_EMBED_strategy)
def test_defaultname_embed_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=defaultname_EMBED_strategy)
def test_defaultname_embed_hspace_setter(instance):
    original = instance.hspace
    instance.hspace = original
    assert instance.hspace == original



@given(instance=defaultname_EMBED_strategy)
def test_defaultname_embed_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=defaultname_EMBED_strategy)
def test_defaultname_embed_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=defaultname_EMBED_strategy)
def test_defaultname_embed_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original



@given(instance=defaultname_EMBED_strategy)
def test_defaultname_embed_vspace_setter(instance):
    original = instance.vspace
    instance.vspace = original
    assert instance.vspace == original



@given(instance=defaultname_EMBED_strategy)
def test_defaultname_embed_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=defaultname_BIG_strategy)
@settings(max_examples=50)
def test_defaultname_big_instantiation(instance):
    assert isinstance(instance, defaultname_BIG)

@given(instance=defaultname_SPAN_strategy)
@settings(max_examples=50)
def test_defaultname_span_instantiation(instance):
    assert isinstance(instance, defaultname_SPAN)



@given(instance=defaultname_SPAN_strategy)
def test_defaultname_span_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=defaultname_STRONG_strategy)
@settings(max_examples=50)
def test_defaultname_strong_instantiation(instance):
    assert isinstance(instance, defaultname_STRONG)

@given(instance=defaultname_H4_strategy)
@settings(max_examples=50)
def test_defaultname_h4_instantiation(instance):
    assert isinstance(instance, defaultname_H4)

@given(instance=defaultname_TT_strategy)
@settings(max_examples=50)
def test_defaultname_tt_instantiation(instance):
    assert isinstance(instance, defaultname_TT)

@given(instance=defaultname_NOEMBED_strategy)
@settings(max_examples=50)
def test_defaultname_noembed_instantiation(instance):
    assert isinstance(instance, defaultname_NOEMBED)

@given(instance=defaultname_TABLEElement_strategy)
@settings(max_examples=50)
def test_defaultname_tableelement_instantiation(instance):
    assert isinstance(instance, defaultname_TABLEElement)



@given(instance=defaultname_TABLEElement_strategy)
def test_defaultname_tableelement_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=defaultname_TABLEElement_strategy)
def test_defaultname_tableelement_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original

@given(instance=defaultname_STYLE_strategy)
@settings(max_examples=50)
def test_defaultname_style_instantiation(instance):
    assert isinstance(instance, defaultname_STYLE)

@given(instance=defaultname_H1_strategy)
@settings(max_examples=50)
def test_defaultname_h1_instantiation(instance):
    assert isinstance(instance, defaultname_H1)

@given(instance=HEADElement_strategy)
@settings(max_examples=50)
def test_headelement_instantiation(instance):
    assert isinstance(instance, HEADElement)

@given(instance=defaultname_TITLE_strategy)
@settings(max_examples=50)
def test_defaultname_title_instantiation(instance):
    assert isinstance(instance, defaultname_TITLE)

@given(instance=defaultname_LINK_strategy)
@settings(max_examples=50)
def test_defaultname_link_instantiation(instance):
    assert isinstance(instance, defaultname_LINK)



@given(instance=defaultname_LINK_strategy)
def test_defaultname_link_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=defaultname_LINK_strategy)
def test_defaultname_link_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=defaultname_LINK_strategy)
def test_defaultname_link_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original



@given(instance=defaultname_LINK_strategy)
def test_defaultname_link_rel_setter(instance):
    original = instance.rel
    instance.rel = original
    assert instance.rel == original

@given(instance=HTMLElement_strategy)
@settings(max_examples=50)
def test_htmlelement_instantiation(instance):
    assert isinstance(instance, HTMLElement)

@given(instance=defaultname_HEADElement_strategy)
@settings(max_examples=50)
def test_defaultname_headelement_instantiation(instance):
    assert isinstance(instance, defaultname_HEADElement)

@given(instance=defaultname_BODYElement_strategy)
@settings(max_examples=50)
def test_defaultname_bodyelement_instantiation(instance):
    assert isinstance(instance, defaultname_BODYElement)

@given(instance=defaultname_BODY_strategy)
@settings(max_examples=50)
def test_defaultname_body_instantiation(instance):
    assert isinstance(instance, defaultname_BODY)



@given(instance=defaultname_BODY_strategy)
def test_defaultname_body_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original



@given(instance=defaultname_BODY_strategy)
def test_defaultname_body_vlink_setter(instance):
    original = instance.vlink
    instance.vlink = original
    assert instance.vlink == original



@given(instance=defaultname_BODY_strategy)
def test_defaultname_body_link_setter(instance):
    original = instance.link
    instance.link = original
    assert instance.link == original



@given(instance=defaultname_BODY_strategy)
def test_defaultname_body_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original



@given(instance=defaultname_BODY_strategy)
def test_defaultname_body_alink_setter(instance):
    original = instance.alink
    instance.alink = original
    assert instance.alink == original



@given(instance=defaultname_BODY_strategy)
def test_defaultname_body_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=defaultname_HTMLElement_strategy)
@settings(max_examples=50)
def test_defaultname_htmlelement_instantiation(instance):
    assert isinstance(instance, defaultname_HTMLElement)



@given(instance=defaultname_HTMLElement_strategy)
def test_defaultname_htmlelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=defaultname_HEAD_strategy)
@settings(max_examples=50)
def test_defaultname_head_instantiation(instance):
    assert isinstance(instance, defaultname_HEAD)

@given(instance=defaultname_HTML_strategy)
@settings(max_examples=50)
def test_defaultname_html_instantiation(instance):
    assert isinstance(instance, defaultname_HTML)
