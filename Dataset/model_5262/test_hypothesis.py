import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    defaultname::FRAMESET,
    FRAME,
    defaultname::IFRAME,
    defaultname::NOFRAME,
    defaultname::FRAME,
    defaultname::TEXTAREA,
    defaultname::OBJECT,
    defaultname::PARAM,
    defaultname::APPLET,
    defaultname::DD,
    defaultname::DT,
    defaultname::DL,
    ListElement,
    defaultname::LI,
    defaultname::UL,
    defaultname::OL,
    defaultname::ListElement,
    defaultname::OPTION,
    defaultname::SELECT,
    TABLEElement,
    defaultname::TABLE,
    defaultname::INPUT,
    defaultname::FORM,
    TD,
    defaultname::TH,
    defaultname::TD,
    defaultname::TR,
    BODYElement,
    defaultname::TABLEElement,
    defaultname::A,
    defaultname::IMG,
    defaultname::B,
    defaultname::MAP,
    defaultname::STRONG,
    defaultname::EM,
    defaultname::EMBED,
    defaultname::STRIKE,
    defaultname::H2,
    defaultname::TT,
    defaultname::AREA,
    defaultname::BR,
    defaultname::SMALL,
    defaultname::H3,
    defaultname::SUP,
    defaultname::STYLE,
    defaultname::NOEMBED,
    defaultname::SUB,
    defaultname::H4,
    defaultname::PRE,
    defaultname::FONT,
    defaultname::P,
    defaultname::SPAN,
    defaultname::BIG,
    defaultname::I,
    defaultname::DIV,
    defaultname::H1,
    HEADElement,
    defaultname::TITLE,
    defaultname::LINK,
    HTMLElement,
    defaultname::BODYElement,
    defaultname::HEADElement,
    defaultname::BODY,
    defaultname::HTMLElement,
    defaultname::HEAD,
    defaultname::HTML,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_defaultname::frameset_is_not_abstract():
    assert not inspect.isabstract(defaultname::FRAMESET)


def test_defaultname::frameset_constructor_exists():
    assert callable(defaultname::FRAMESET.__init__)


def test_defaultname::frameset_constructor_args():
    sig = inspect.signature(defaultname::FRAMESET.__init__)
    params = list(sig.parameters.keys())
    assert "frameborder" in params, "Missing parameter 'frameborder'"
    assert "border" in params, "Missing parameter 'border'"
    assert "framespacing" in params, "Missing parameter 'framespacing'"
    assert "rows" in params, "Missing parameter 'rows'"
    assert "cols" in params, "Missing parameter 'cols'"

def test_defaultname::frameset_has_frameborder():
    assert hasattr(defaultname::FRAMESET, "frameborder")
    descriptor = None
    for klass in defaultname::FRAMESET.__mro__:
        if "frameborder" in klass.__dict__:
            descriptor = klass.__dict__["frameborder"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frameset_has_border():
    assert hasattr(defaultname::FRAMESET, "border")
    descriptor = None
    for klass in defaultname::FRAMESET.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frameset_has_framespacing():
    assert hasattr(defaultname::FRAMESET, "framespacing")
    descriptor = None
    for klass in defaultname::FRAMESET.__mro__:
        if "framespacing" in klass.__dict__:
            descriptor = klass.__dict__["framespacing"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frameset_has_rows():
    assert hasattr(defaultname::FRAMESET, "rows")
    descriptor = None
    for klass in defaultname::FRAMESET.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frameset_has_cols():
    assert hasattr(defaultname::FRAMESET, "cols")
    descriptor = None
    for klass in defaultname::FRAMESET.__mro__:
        if "cols" in klass.__dict__:
            descriptor = klass.__dict__["cols"]
            break
    assert isinstance(descriptor, property)



def test_frame_is_not_abstract():
    assert not inspect.isabstract(FRAME)


def test_frame_constructor_exists():
    assert callable(FRAME.__init__)


def test_frame_constructor_args():
    sig = inspect.signature(FRAME.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::iframe_is_not_abstract():
    assert not inspect.isabstract(defaultname::IFRAME)


def test_defaultname::iframe_constructor_exists():
    assert callable(defaultname::IFRAME.__init__)


def test_defaultname::iframe_constructor_args():
    sig = inspect.signature(defaultname::IFRAME.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::noframe_is_not_abstract():
    assert not inspect.isabstract(defaultname::NOFRAME)


def test_defaultname::noframe_constructor_exists():
    assert callable(defaultname::NOFRAME.__init__)


def test_defaultname::noframe_constructor_args():
    sig = inspect.signature(defaultname::NOFRAME.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::frame_is_not_abstract():
    assert not inspect.isabstract(defaultname::FRAME)


def test_defaultname::frame_constructor_exists():
    assert callable(defaultname::FRAME.__init__)


def test_defaultname::frame_constructor_args():
    sig = inspect.signature(defaultname::FRAME.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "scrolling" in params, "Missing parameter 'scrolling'"
    assert "src" in params, "Missing parameter 'src'"
    assert "marginheight" in params, "Missing parameter 'marginheight'"
    assert "marginwidth" in params, "Missing parameter 'marginwidth'"
    assert "noresize" in params, "Missing parameter 'noresize'"

def test_defaultname::frame_has_name():
    assert hasattr(defaultname::FRAME, "name")
    descriptor = None
    for klass in defaultname::FRAME.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frame_has_scrolling():
    assert hasattr(defaultname::FRAME, "scrolling")
    descriptor = None
    for klass in defaultname::FRAME.__mro__:
        if "scrolling" in klass.__dict__:
            descriptor = klass.__dict__["scrolling"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frame_has_src():
    assert hasattr(defaultname::FRAME, "src")
    descriptor = None
    for klass in defaultname::FRAME.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frame_has_marginheight():
    assert hasattr(defaultname::FRAME, "marginheight")
    descriptor = None
    for klass in defaultname::FRAME.__mro__:
        if "marginheight" in klass.__dict__:
            descriptor = klass.__dict__["marginheight"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frame_has_marginwidth():
    assert hasattr(defaultname::FRAME, "marginwidth")
    descriptor = None
    for klass in defaultname::FRAME.__mro__:
        if "marginwidth" in klass.__dict__:
            descriptor = klass.__dict__["marginwidth"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::frame_has_noresize():
    assert hasattr(defaultname::FRAME, "noresize")
    descriptor = None
    for klass in defaultname::FRAME.__mro__:
        if "noresize" in klass.__dict__:
            descriptor = klass.__dict__["noresize"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::textarea_is_not_abstract():
    assert not inspect.isabstract(defaultname::TEXTAREA)


def test_defaultname::textarea_constructor_exists():
    assert callable(defaultname::TEXTAREA.__init__)


def test_defaultname::textarea_constructor_args():
    sig = inspect.signature(defaultname::TEXTAREA.__init__)
    params = list(sig.parameters.keys())
    assert "rows" in params, "Missing parameter 'rows'"
    assert "cols" in params, "Missing parameter 'cols'"
    assert "name" in params, "Missing parameter 'name'"

def test_defaultname::textarea_has_rows():
    assert hasattr(defaultname::TEXTAREA, "rows")
    descriptor = None
    for klass in defaultname::TEXTAREA.__mro__:
        if "rows" in klass.__dict__:
            descriptor = klass.__dict__["rows"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::textarea_has_cols():
    assert hasattr(defaultname::TEXTAREA, "cols")
    descriptor = None
    for klass in defaultname::TEXTAREA.__mro__:
        if "cols" in klass.__dict__:
            descriptor = klass.__dict__["cols"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::textarea_has_name():
    assert hasattr(defaultname::TEXTAREA, "name")
    descriptor = None
    for klass in defaultname::TEXTAREA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::object_is_not_abstract():
    assert not inspect.isabstract(defaultname::OBJECT)


def test_defaultname::object_constructor_exists():
    assert callable(defaultname::OBJECT.__init__)


def test_defaultname::object_constructor_args():
    sig = inspect.signature(defaultname::OBJECT.__init__)
    params = list(sig.parameters.keys())
    assert "standby" in params, "Missing parameter 'standby'"
    assert "type" in params, "Missing parameter 'type'"
    assert "data" in params, "Missing parameter 'data'"
    assert "classid" in params, "Missing parameter 'classid'"
    assert "id" in params, "Missing parameter 'id'"

def test_defaultname::object_has_standby():
    assert hasattr(defaultname::OBJECT, "standby")
    descriptor = None
    for klass in defaultname::OBJECT.__mro__:
        if "standby" in klass.__dict__:
            descriptor = klass.__dict__["standby"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::object_has_type():
    assert hasattr(defaultname::OBJECT, "type")
    descriptor = None
    for klass in defaultname::OBJECT.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::object_has_data():
    assert hasattr(defaultname::OBJECT, "data")
    descriptor = None
    for klass in defaultname::OBJECT.__mro__:
        if "data" in klass.__dict__:
            descriptor = klass.__dict__["data"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::object_has_classid():
    assert hasattr(defaultname::OBJECT, "classid")
    descriptor = None
    for klass in defaultname::OBJECT.__mro__:
        if "classid" in klass.__dict__:
            descriptor = klass.__dict__["classid"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::object_has_id():
    assert hasattr(defaultname::OBJECT, "id")
    descriptor = None
    for klass in defaultname::OBJECT.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::param_is_not_abstract():
    assert not inspect.isabstract(defaultname::PARAM)


def test_defaultname::param_constructor_exists():
    assert callable(defaultname::PARAM.__init__)


def test_defaultname::param_constructor_args():
    sig = inspect.signature(defaultname::PARAM.__init__)
    params = list(sig.parameters.keys())
    assert "paramValue" in params, "Missing parameter 'paramValue'"
    assert "name" in params, "Missing parameter 'name'"

def test_defaultname::param_has_paramValue():
    assert hasattr(defaultname::PARAM, "paramValue")
    descriptor = None
    for klass in defaultname::PARAM.__mro__:
        if "paramValue" in klass.__dict__:
            descriptor = klass.__dict__["paramValue"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::param_has_name():
    assert hasattr(defaultname::PARAM, "name")
    descriptor = None
    for klass in defaultname::PARAM.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::applet_is_not_abstract():
    assert not inspect.isabstract(defaultname::APPLET)


def test_defaultname::applet_constructor_exists():
    assert callable(defaultname::APPLET.__init__)


def test_defaultname::applet_constructor_args():
    sig = inspect.signature(defaultname::APPLET.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "applet" in params, "Missing parameter 'applet'"
    assert "src" in params, "Missing parameter 'src'"
    assert "class_" in params, "Missing parameter 'class_'"
    assert "width" in params, "Missing parameter 'width'"
    assert "height" in params, "Missing parameter 'height'"

def test_defaultname::applet_has_align():
    assert hasattr(defaultname::APPLET, "align")
    descriptor = None
    for klass in defaultname::APPLET.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::applet_has_applet():
    assert hasattr(defaultname::APPLET, "applet")
    descriptor = None
    for klass in defaultname::APPLET.__mro__:
        if "applet" in klass.__dict__:
            descriptor = klass.__dict__["applet"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::applet_has_src():
    assert hasattr(defaultname::APPLET, "src")
    descriptor = None
    for klass in defaultname::APPLET.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::applet_has_class_():
    assert hasattr(defaultname::APPLET, "class_")
    descriptor = None
    for klass in defaultname::APPLET.__mro__:
        if "class_" in klass.__dict__:
            descriptor = klass.__dict__["class_"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::applet_has_width():
    assert hasattr(defaultname::APPLET, "width")
    descriptor = None
    for klass in defaultname::APPLET.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::applet_has_height():
    assert hasattr(defaultname::APPLET, "height")
    descriptor = None
    for klass in defaultname::APPLET.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::dd_is_not_abstract():
    assert not inspect.isabstract(defaultname::DD)


def test_defaultname::dd_constructor_exists():
    assert callable(defaultname::DD.__init__)


def test_defaultname::dd_constructor_args():
    sig = inspect.signature(defaultname::DD.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::dt_is_not_abstract():
    assert not inspect.isabstract(defaultname::DT)


def test_defaultname::dt_constructor_exists():
    assert callable(defaultname::DT.__init__)


def test_defaultname::dt_constructor_args():
    sig = inspect.signature(defaultname::DT.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::dl_is_not_abstract():
    assert not inspect.isabstract(defaultname::DL)


def test_defaultname::dl_constructor_exists():
    assert callable(defaultname::DL.__init__)


def test_defaultname::dl_constructor_args():
    sig = inspect.signature(defaultname::DL.__init__)
    params = list(sig.parameters.keys())



def test_listelement_is_not_abstract():
    assert not inspect.isabstract(ListElement)


def test_listelement_constructor_exists():
    assert callable(ListElement.__init__)


def test_listelement_constructor_args():
    sig = inspect.signature(ListElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::li_is_not_abstract():
    assert not inspect.isabstract(defaultname::LI)


def test_defaultname::li_constructor_exists():
    assert callable(defaultname::LI.__init__)


def test_defaultname::li_constructor_args():
    sig = inspect.signature(defaultname::LI.__init__)
    params = list(sig.parameters.keys())
    assert "liValue" in params, "Missing parameter 'liValue'"

def test_defaultname::li_has_liValue():
    assert hasattr(defaultname::LI, "liValue")
    descriptor = None
    for klass in defaultname::LI.__mro__:
        if "liValue" in klass.__dict__:
            descriptor = klass.__dict__["liValue"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::ul_is_not_abstract():
    assert not inspect.isabstract(defaultname::UL)


def test_defaultname::ul_constructor_exists():
    assert callable(defaultname::UL.__init__)


def test_defaultname::ul_constructor_args():
    sig = inspect.signature(defaultname::UL.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::ol_is_not_abstract():
    assert not inspect.isabstract(defaultname::OL)


def test_defaultname::ol_constructor_exists():
    assert callable(defaultname::OL.__init__)


def test_defaultname::ol_constructor_args():
    sig = inspect.signature(defaultname::OL.__init__)
    params = list(sig.parameters.keys())
    assert "start" in params, "Missing parameter 'start'"

def test_defaultname::ol_has_start():
    assert hasattr(defaultname::OL, "start")
    descriptor = None
    for klass in defaultname::OL.__mro__:
        if "start" in klass.__dict__:
            descriptor = klass.__dict__["start"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::listelement_is_not_abstract():
    assert not inspect.isabstract(defaultname::ListElement)


def test_defaultname::listelement_constructor_exists():
    assert callable(defaultname::ListElement.__init__)


def test_defaultname::listelement_constructor_args():
    sig = inspect.signature(defaultname::ListElement.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_defaultname::listelement_has_type():
    assert hasattr(defaultname::ListElement, "type")
    descriptor = None
    for klass in defaultname::ListElement.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::option_is_not_abstract():
    assert not inspect.isabstract(defaultname::OPTION)


def test_defaultname::option_constructor_exists():
    assert callable(defaultname::OPTION.__init__)


def test_defaultname::option_constructor_args():
    sig = inspect.signature(defaultname::OPTION.__init__)
    params = list(sig.parameters.keys())
    assert "optionValue" in params, "Missing parameter 'optionValue'"
    assert "selected" in params, "Missing parameter 'selected'"

def test_defaultname::option_has_optionValue():
    assert hasattr(defaultname::OPTION, "optionValue")
    descriptor = None
    for klass in defaultname::OPTION.__mro__:
        if "optionValue" in klass.__dict__:
            descriptor = klass.__dict__["optionValue"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::option_has_selected():
    assert hasattr(defaultname::OPTION, "selected")
    descriptor = None
    for klass in defaultname::OPTION.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::select_is_not_abstract():
    assert not inspect.isabstract(defaultname::SELECT)


def test_defaultname::select_constructor_exists():
    assert callable(defaultname::SELECT.__init__)


def test_defaultname::select_constructor_args():
    sig = inspect.signature(defaultname::SELECT.__init__)
    params = list(sig.parameters.keys())
    assert "size" in params, "Missing parameter 'size'"
    assert "multiple" in params, "Missing parameter 'multiple'"
    assert "name" in params, "Missing parameter 'name'"

def test_defaultname::select_has_size():
    assert hasattr(defaultname::SELECT, "size")
    descriptor = None
    for klass in defaultname::SELECT.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::select_has_multiple():
    assert hasattr(defaultname::SELECT, "multiple")
    descriptor = None
    for klass in defaultname::SELECT.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::select_has_name():
    assert hasattr(defaultname::SELECT, "name")
    descriptor = None
    for klass in defaultname::SELECT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TABLEElement)


def test_tableelement_constructor_exists():
    assert callable(TABLEElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TABLEElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::table_is_not_abstract():
    assert not inspect.isabstract(defaultname::TABLE)


def test_defaultname::table_constructor_exists():
    assert callable(defaultname::TABLE.__init__)


def test_defaultname::table_constructor_args():
    sig = inspect.signature(defaultname::TABLE.__init__)
    params = list(sig.parameters.keys())
    assert "cellpadding" in params, "Missing parameter 'cellpadding'"
    assert "border" in params, "Missing parameter 'border'"
    assert "cellspacing" in params, "Missing parameter 'cellspacing'"
    assert "width" in params, "Missing parameter 'width'"

def test_defaultname::table_has_cellpadding():
    assert hasattr(defaultname::TABLE, "cellpadding")
    descriptor = None
    for klass in defaultname::TABLE.__mro__:
        if "cellpadding" in klass.__dict__:
            descriptor = klass.__dict__["cellpadding"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::table_has_border():
    assert hasattr(defaultname::TABLE, "border")
    descriptor = None
    for klass in defaultname::TABLE.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::table_has_cellspacing():
    assert hasattr(defaultname::TABLE, "cellspacing")
    descriptor = None
    for klass in defaultname::TABLE.__mro__:
        if "cellspacing" in klass.__dict__:
            descriptor = klass.__dict__["cellspacing"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::table_has_width():
    assert hasattr(defaultname::TABLE, "width")
    descriptor = None
    for klass in defaultname::TABLE.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::input_is_not_abstract():
    assert not inspect.isabstract(defaultname::INPUT)


def test_defaultname::input_constructor_exists():
    assert callable(defaultname::INPUT.__init__)


def test_defaultname::input_constructor_args():
    sig = inspect.signature(defaultname::INPUT.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "name" in params, "Missing parameter 'name'"
    assert "src" in params, "Missing parameter 'src'"
    assert "inputValue" in params, "Missing parameter 'inputValue'"
    assert "size" in params, "Missing parameter 'size'"
    assert "align" in params, "Missing parameter 'align'"
    assert "maxlength" in params, "Missing parameter 'maxlength'"
    assert "checked" in params, "Missing parameter 'checked'"

def test_defaultname::input_has_type():
    assert hasattr(defaultname::INPUT, "type")
    descriptor = None
    for klass in defaultname::INPUT.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::input_has_name():
    assert hasattr(defaultname::INPUT, "name")
    descriptor = None
    for klass in defaultname::INPUT.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::input_has_src():
    assert hasattr(defaultname::INPUT, "src")
    descriptor = None
    for klass in defaultname::INPUT.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::input_has_inputValue():
    assert hasattr(defaultname::INPUT, "inputValue")
    descriptor = None
    for klass in defaultname::INPUT.__mro__:
        if "inputValue" in klass.__dict__:
            descriptor = klass.__dict__["inputValue"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::input_has_size():
    assert hasattr(defaultname::INPUT, "size")
    descriptor = None
    for klass in defaultname::INPUT.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::input_has_align():
    assert hasattr(defaultname::INPUT, "align")
    descriptor = None
    for klass in defaultname::INPUT.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::input_has_maxlength():
    assert hasattr(defaultname::INPUT, "maxlength")
    descriptor = None
    for klass in defaultname::INPUT.__mro__:
        if "maxlength" in klass.__dict__:
            descriptor = klass.__dict__["maxlength"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::input_has_checked():
    assert hasattr(defaultname::INPUT, "checked")
    descriptor = None
    for klass in defaultname::INPUT.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::form_is_not_abstract():
    assert not inspect.isabstract(defaultname::FORM)


def test_defaultname::form_constructor_exists():
    assert callable(defaultname::FORM.__init__)


def test_defaultname::form_constructor_args():
    sig = inspect.signature(defaultname::FORM.__init__)
    params = list(sig.parameters.keys())
    assert "action" in params, "Missing parameter 'action'"
    assert "method" in params, "Missing parameter 'method'"

def test_defaultname::form_has_action():
    assert hasattr(defaultname::FORM, "action")
    descriptor = None
    for klass in defaultname::FORM.__mro__:
        if "action" in klass.__dict__:
            descriptor = klass.__dict__["action"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::form_has_method():
    assert hasattr(defaultname::FORM, "method")
    descriptor = None
    for klass in defaultname::FORM.__mro__:
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



def test_defaultname::th_is_not_abstract():
    assert not inspect.isabstract(defaultname::TH)


def test_defaultname::th_constructor_exists():
    assert callable(defaultname::TH.__init__)


def test_defaultname::th_constructor_args():
    sig = inspect.signature(defaultname::TH.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::td_is_not_abstract():
    assert not inspect.isabstract(defaultname::TD)


def test_defaultname::td_constructor_exists():
    assert callable(defaultname::TD.__init__)


def test_defaultname::td_constructor_args():
    sig = inspect.signature(defaultname::TD.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "rowspan" in params, "Missing parameter 'rowspan'"
    assert "colspan" in params, "Missing parameter 'colspan'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "width" in params, "Missing parameter 'width'"

def test_defaultname::td_has_align():
    assert hasattr(defaultname::TD, "align")
    descriptor = None
    for klass in defaultname::TD.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::td_has_rowspan():
    assert hasattr(defaultname::TD, "rowspan")
    descriptor = None
    for klass in defaultname::TD.__mro__:
        if "rowspan" in klass.__dict__:
            descriptor = klass.__dict__["rowspan"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::td_has_colspan():
    assert hasattr(defaultname::TD, "colspan")
    descriptor = None
    for klass in defaultname::TD.__mro__:
        if "colspan" in klass.__dict__:
            descriptor = klass.__dict__["colspan"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::td_has_valign():
    assert hasattr(defaultname::TD, "valign")
    descriptor = None
    for klass in defaultname::TD.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::td_has_width():
    assert hasattr(defaultname::TD, "width")
    descriptor = None
    for klass in defaultname::TD.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::tr_is_not_abstract():
    assert not inspect.isabstract(defaultname::TR)


def test_defaultname::tr_constructor_exists():
    assert callable(defaultname::TR.__init__)


def test_defaultname::tr_constructor_args():
    sig = inspect.signature(defaultname::TR.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"

def test_defaultname::tr_has_align():
    assert hasattr(defaultname::TR, "align")
    descriptor = None
    for klass in defaultname::TR.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::tr_has_valign():
    assert hasattr(defaultname::TR, "valign")
    descriptor = None
    for klass in defaultname::TR.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)



def test_bodyelement_is_not_abstract():
    assert not inspect.isabstract(BODYElement)


def test_bodyelement_constructor_exists():
    assert callable(BODYElement.__init__)


def test_bodyelement_constructor_args():
    sig = inspect.signature(BODYElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::tableelement_is_not_abstract():
    assert not inspect.isabstract(defaultname::TABLEElement)


def test_defaultname::tableelement_constructor_exists():
    assert callable(defaultname::TABLEElement.__init__)


def test_defaultname::tableelement_constructor_args():
    sig = inspect.signature(defaultname::TABLEElement.__init__)
    params = list(sig.parameters.keys())
    assert "background" in params, "Missing parameter 'background'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"

def test_defaultname::tableelement_has_background():
    assert hasattr(defaultname::TABLEElement, "background")
    descriptor = None
    for klass in defaultname::TABLEElement.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::tableelement_has_bgcolor():
    assert hasattr(defaultname::TABLEElement, "bgcolor")
    descriptor = None
    for klass in defaultname::TABLEElement.__mro__:
        if "bgcolor" in klass.__dict__:
            descriptor = klass.__dict__["bgcolor"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::a_is_not_abstract():
    assert not inspect.isabstract(defaultname::A)


def test_defaultname::a_constructor_exists():
    assert callable(defaultname::A.__init__)


def test_defaultname::a_constructor_args():
    sig = inspect.signature(defaultname::A.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "ahref" in params, "Missing parameter 'ahref'"
    assert "id" in params, "Missing parameter 'id'"

def test_defaultname::a_has_name():
    assert hasattr(defaultname::A, "name")
    descriptor = None
    for klass in defaultname::A.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::a_has_ahref():
    assert hasattr(defaultname::A, "ahref")
    descriptor = None
    for klass in defaultname::A.__mro__:
        if "ahref" in klass.__dict__:
            descriptor = klass.__dict__["ahref"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::a_has_id():
    assert hasattr(defaultname::A, "id")
    descriptor = None
    for klass in defaultname::A.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::img_is_not_abstract():
    assert not inspect.isabstract(defaultname::IMG)


def test_defaultname::img_constructor_exists():
    assert callable(defaultname::IMG.__init__)


def test_defaultname::img_constructor_args():
    sig = inspect.signature(defaultname::IMG.__init__)
    params = list(sig.parameters.keys())
    assert "usemap" in params, "Missing parameter 'usemap'"
    assert "vspace" in params, "Missing parameter 'vspace'"
    assert "hspace" in params, "Missing parameter 'hspace'"
    assert "alt" in params, "Missing parameter 'alt'"
    assert "ismap" in params, "Missing parameter 'ismap'"
    assert "src" in params, "Missing parameter 'src'"
    assert "border" in params, "Missing parameter 'border'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "align" in params, "Missing parameter 'align'"

def test_defaultname::img_has_usemap():
    assert hasattr(defaultname::IMG, "usemap")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "usemap" in klass.__dict__:
            descriptor = klass.__dict__["usemap"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_vspace():
    assert hasattr(defaultname::IMG, "vspace")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "vspace" in klass.__dict__:
            descriptor = klass.__dict__["vspace"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_hspace():
    assert hasattr(defaultname::IMG, "hspace")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "hspace" in klass.__dict__:
            descriptor = klass.__dict__["hspace"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_alt():
    assert hasattr(defaultname::IMG, "alt")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "alt" in klass.__dict__:
            descriptor = klass.__dict__["alt"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_ismap():
    assert hasattr(defaultname::IMG, "ismap")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "ismap" in klass.__dict__:
            descriptor = klass.__dict__["ismap"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_src():
    assert hasattr(defaultname::IMG, "src")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_border():
    assert hasattr(defaultname::IMG, "border")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_height():
    assert hasattr(defaultname::IMG, "height")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_width():
    assert hasattr(defaultname::IMG, "width")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::img_has_align():
    assert hasattr(defaultname::IMG, "align")
    descriptor = None
    for klass in defaultname::IMG.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::b_is_not_abstract():
    assert not inspect.isabstract(defaultname::B)


def test_defaultname::b_constructor_exists():
    assert callable(defaultname::B.__init__)


def test_defaultname::b_constructor_args():
    sig = inspect.signature(defaultname::B.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::map_is_not_abstract():
    assert not inspect.isabstract(defaultname::MAP)


def test_defaultname::map_constructor_exists():
    assert callable(defaultname::MAP.__init__)


def test_defaultname::map_constructor_args():
    sig = inspect.signature(defaultname::MAP.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::strong_is_not_abstract():
    assert not inspect.isabstract(defaultname::STRONG)


def test_defaultname::strong_constructor_exists():
    assert callable(defaultname::STRONG.__init__)


def test_defaultname::strong_constructor_args():
    sig = inspect.signature(defaultname::STRONG.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::em_is_not_abstract():
    assert not inspect.isabstract(defaultname::EM)


def test_defaultname::em_constructor_exists():
    assert callable(defaultname::EM.__init__)


def test_defaultname::em_constructor_args():
    sig = inspect.signature(defaultname::EM.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::embed_is_not_abstract():
    assert not inspect.isabstract(defaultname::EMBED)


def test_defaultname::embed_constructor_exists():
    assert callable(defaultname::EMBED.__init__)


def test_defaultname::embed_constructor_args():
    sig = inspect.signature(defaultname::EMBED.__init__)
    params = list(sig.parameters.keys())
    assert "border" in params, "Missing parameter 'border'"
    assert "src" in params, "Missing parameter 'src'"
    assert "vspace" in params, "Missing parameter 'vspace'"
    assert "hspace" in params, "Missing parameter 'hspace'"
    assert "height" in params, "Missing parameter 'height'"
    assert "width" in params, "Missing parameter 'width'"
    assert "align" in params, "Missing parameter 'align'"

def test_defaultname::embed_has_border():
    assert hasattr(defaultname::EMBED, "border")
    descriptor = None
    for klass in defaultname::EMBED.__mro__:
        if "border" in klass.__dict__:
            descriptor = klass.__dict__["border"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::embed_has_src():
    assert hasattr(defaultname::EMBED, "src")
    descriptor = None
    for klass in defaultname::EMBED.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::embed_has_vspace():
    assert hasattr(defaultname::EMBED, "vspace")
    descriptor = None
    for klass in defaultname::EMBED.__mro__:
        if "vspace" in klass.__dict__:
            descriptor = klass.__dict__["vspace"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::embed_has_hspace():
    assert hasattr(defaultname::EMBED, "hspace")
    descriptor = None
    for klass in defaultname::EMBED.__mro__:
        if "hspace" in klass.__dict__:
            descriptor = klass.__dict__["hspace"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::embed_has_height():
    assert hasattr(defaultname::EMBED, "height")
    descriptor = None
    for klass in defaultname::EMBED.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::embed_has_width():
    assert hasattr(defaultname::EMBED, "width")
    descriptor = None
    for klass in defaultname::EMBED.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::embed_has_align():
    assert hasattr(defaultname::EMBED, "align")
    descriptor = None
    for klass in defaultname::EMBED.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::strike_is_not_abstract():
    assert not inspect.isabstract(defaultname::STRIKE)


def test_defaultname::strike_constructor_exists():
    assert callable(defaultname::STRIKE.__init__)


def test_defaultname::strike_constructor_args():
    sig = inspect.signature(defaultname::STRIKE.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::h2_is_not_abstract():
    assert not inspect.isabstract(defaultname::H2)


def test_defaultname::h2_constructor_exists():
    assert callable(defaultname::H2.__init__)


def test_defaultname::h2_constructor_args():
    sig = inspect.signature(defaultname::H2.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::tt_is_not_abstract():
    assert not inspect.isabstract(defaultname::TT)


def test_defaultname::tt_constructor_exists():
    assert callable(defaultname::TT.__init__)


def test_defaultname::tt_constructor_args():
    sig = inspect.signature(defaultname::TT.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::area_is_not_abstract():
    assert not inspect.isabstract(defaultname::AREA)


def test_defaultname::area_constructor_exists():
    assert callable(defaultname::AREA.__init__)


def test_defaultname::area_constructor_args():
    sig = inspect.signature(defaultname::AREA.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "ahref" in params, "Missing parameter 'ahref'"
    assert "coords" in params, "Missing parameter 'coords'"

def test_defaultname::area_has_shape():
    assert hasattr(defaultname::AREA, "shape")
    descriptor = None
    for klass in defaultname::AREA.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::area_has_ahref():
    assert hasattr(defaultname::AREA, "ahref")
    descriptor = None
    for klass in defaultname::AREA.__mro__:
        if "ahref" in klass.__dict__:
            descriptor = klass.__dict__["ahref"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::area_has_coords():
    assert hasattr(defaultname::AREA, "coords")
    descriptor = None
    for klass in defaultname::AREA.__mro__:
        if "coords" in klass.__dict__:
            descriptor = klass.__dict__["coords"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::br_is_not_abstract():
    assert not inspect.isabstract(defaultname::BR)


def test_defaultname::br_constructor_exists():
    assert callable(defaultname::BR.__init__)


def test_defaultname::br_constructor_args():
    sig = inspect.signature(defaultname::BR.__init__)
    params = list(sig.parameters.keys())
    assert "clear" in params, "Missing parameter 'clear'"

def test_defaultname::br_has_clear():
    assert hasattr(defaultname::BR, "clear")
    descriptor = None
    for klass in defaultname::BR.__mro__:
        if "clear" in klass.__dict__:
            descriptor = klass.__dict__["clear"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::small_is_not_abstract():
    assert not inspect.isabstract(defaultname::SMALL)


def test_defaultname::small_constructor_exists():
    assert callable(defaultname::SMALL.__init__)


def test_defaultname::small_constructor_args():
    sig = inspect.signature(defaultname::SMALL.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::h3_is_not_abstract():
    assert not inspect.isabstract(defaultname::H3)


def test_defaultname::h3_constructor_exists():
    assert callable(defaultname::H3.__init__)


def test_defaultname::h3_constructor_args():
    sig = inspect.signature(defaultname::H3.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::sup_is_not_abstract():
    assert not inspect.isabstract(defaultname::SUP)


def test_defaultname::sup_constructor_exists():
    assert callable(defaultname::SUP.__init__)


def test_defaultname::sup_constructor_args():
    sig = inspect.signature(defaultname::SUP.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::style_is_not_abstract():
    assert not inspect.isabstract(defaultname::STYLE)


def test_defaultname::style_constructor_exists():
    assert callable(defaultname::STYLE.__init__)


def test_defaultname::style_constructor_args():
    sig = inspect.signature(defaultname::STYLE.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::noembed_is_not_abstract():
    assert not inspect.isabstract(defaultname::NOEMBED)


def test_defaultname::noembed_constructor_exists():
    assert callable(defaultname::NOEMBED.__init__)


def test_defaultname::noembed_constructor_args():
    sig = inspect.signature(defaultname::NOEMBED.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::sub_is_not_abstract():
    assert not inspect.isabstract(defaultname::SUB)


def test_defaultname::sub_constructor_exists():
    assert callable(defaultname::SUB.__init__)


def test_defaultname::sub_constructor_args():
    sig = inspect.signature(defaultname::SUB.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::h4_is_not_abstract():
    assert not inspect.isabstract(defaultname::H4)


def test_defaultname::h4_constructor_exists():
    assert callable(defaultname::H4.__init__)


def test_defaultname::h4_constructor_args():
    sig = inspect.signature(defaultname::H4.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::pre_is_not_abstract():
    assert not inspect.isabstract(defaultname::PRE)


def test_defaultname::pre_constructor_exists():
    assert callable(defaultname::PRE.__init__)


def test_defaultname::pre_constructor_args():
    sig = inspect.signature(defaultname::PRE.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::font_is_not_abstract():
    assert not inspect.isabstract(defaultname::FONT)


def test_defaultname::font_constructor_exists():
    assert callable(defaultname::FONT.__init__)


def test_defaultname::font_constructor_args():
    sig = inspect.signature(defaultname::FONT.__init__)
    params = list(sig.parameters.keys())
    assert "face" in params, "Missing parameter 'face'"
    assert "color" in params, "Missing parameter 'color'"
    assert "size" in params, "Missing parameter 'size'"

def test_defaultname::font_has_face():
    assert hasattr(defaultname::FONT, "face")
    descriptor = None
    for klass in defaultname::FONT.__mro__:
        if "face" in klass.__dict__:
            descriptor = klass.__dict__["face"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::font_has_color():
    assert hasattr(defaultname::FONT, "color")
    descriptor = None
    for klass in defaultname::FONT.__mro__:
        if "color" in klass.__dict__:
            descriptor = klass.__dict__["color"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::font_has_size():
    assert hasattr(defaultname::FONT, "size")
    descriptor = None
    for klass in defaultname::FONT.__mro__:
        if "size" in klass.__dict__:
            descriptor = klass.__dict__["size"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::p_is_not_abstract():
    assert not inspect.isabstract(defaultname::P)


def test_defaultname::p_constructor_exists():
    assert callable(defaultname::P.__init__)


def test_defaultname::p_constructor_args():
    sig = inspect.signature(defaultname::P.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::span_is_not_abstract():
    assert not inspect.isabstract(defaultname::SPAN)


def test_defaultname::span_constructor_exists():
    assert callable(defaultname::SPAN.__init__)


def test_defaultname::span_constructor_args():
    sig = inspect.signature(defaultname::SPAN.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"

def test_defaultname::span_has_style():
    assert hasattr(defaultname::SPAN, "style")
    descriptor = None
    for klass in defaultname::SPAN.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::big_is_not_abstract():
    assert not inspect.isabstract(defaultname::BIG)


def test_defaultname::big_constructor_exists():
    assert callable(defaultname::BIG.__init__)


def test_defaultname::big_constructor_args():
    sig = inspect.signature(defaultname::BIG.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::i_is_not_abstract():
    assert not inspect.isabstract(defaultname::I)


def test_defaultname::i_constructor_exists():
    assert callable(defaultname::I.__init__)


def test_defaultname::i_constructor_args():
    sig = inspect.signature(defaultname::I.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::div_is_not_abstract():
    assert not inspect.isabstract(defaultname::DIV)


def test_defaultname::div_constructor_exists():
    assert callable(defaultname::DIV.__init__)


def test_defaultname::div_constructor_args():
    sig = inspect.signature(defaultname::DIV.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_defaultname::div_has_align():
    assert hasattr(defaultname::DIV, "align")
    descriptor = None
    for klass in defaultname::DIV.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::h1_is_not_abstract():
    assert not inspect.isabstract(defaultname::H1)


def test_defaultname::h1_constructor_exists():
    assert callable(defaultname::H1.__init__)


def test_defaultname::h1_constructor_args():
    sig = inspect.signature(defaultname::H1.__init__)
    params = list(sig.parameters.keys())



def test_headelement_is_not_abstract():
    assert not inspect.isabstract(HEADElement)


def test_headelement_constructor_exists():
    assert callable(HEADElement.__init__)


def test_headelement_constructor_args():
    sig = inspect.signature(HEADElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::title_is_not_abstract():
    assert not inspect.isabstract(defaultname::TITLE)


def test_defaultname::title_constructor_exists():
    assert callable(defaultname::TITLE.__init__)


def test_defaultname::title_constructor_args():
    sig = inspect.signature(defaultname::TITLE.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::link_is_not_abstract():
    assert not inspect.isabstract(defaultname::LINK)


def test_defaultname::link_constructor_exists():
    assert callable(defaultname::LINK.__init__)


def test_defaultname::link_constructor_args():
    sig = inspect.signature(defaultname::LINK.__init__)
    params = list(sig.parameters.keys())
    assert "ahref" in params, "Missing parameter 'ahref'"
    assert "title" in params, "Missing parameter 'title'"
    assert "type" in params, "Missing parameter 'type'"
    assert "rel" in params, "Missing parameter 'rel'"

def test_defaultname::link_has_ahref():
    assert hasattr(defaultname::LINK, "ahref")
    descriptor = None
    for klass in defaultname::LINK.__mro__:
        if "ahref" in klass.__dict__:
            descriptor = klass.__dict__["ahref"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::link_has_title():
    assert hasattr(defaultname::LINK, "title")
    descriptor = None
    for klass in defaultname::LINK.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::link_has_type():
    assert hasattr(defaultname::LINK, "type")
    descriptor = None
    for klass in defaultname::LINK.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::link_has_rel():
    assert hasattr(defaultname::LINK, "rel")
    descriptor = None
    for klass in defaultname::LINK.__mro__:
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



def test_defaultname::bodyelement_is_not_abstract():
    assert not inspect.isabstract(defaultname::BODYElement)


def test_defaultname::bodyelement_constructor_exists():
    assert callable(defaultname::BODYElement.__init__)


def test_defaultname::bodyelement_constructor_args():
    sig = inspect.signature(defaultname::BODYElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::headelement_is_not_abstract():
    assert not inspect.isabstract(defaultname::HEADElement)


def test_defaultname::headelement_constructor_exists():
    assert callable(defaultname::HEADElement.__init__)


def test_defaultname::headelement_constructor_args():
    sig = inspect.signature(defaultname::HEADElement.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::body_is_not_abstract():
    assert not inspect.isabstract(defaultname::BODY)


def test_defaultname::body_constructor_exists():
    assert callable(defaultname::BODY.__init__)


def test_defaultname::body_constructor_args():
    sig = inspect.signature(defaultname::BODY.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"
    assert "alink" in params, "Missing parameter 'alink'"
    assert "vlink" in params, "Missing parameter 'vlink'"
    assert "background" in params, "Missing parameter 'background'"
    assert "link" in params, "Missing parameter 'link'"
    assert "bgcolor" in params, "Missing parameter 'bgcolor'"

def test_defaultname::body_has_text():
    assert hasattr(defaultname::BODY, "text")
    descriptor = None
    for klass in defaultname::BODY.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::body_has_alink():
    assert hasattr(defaultname::BODY, "alink")
    descriptor = None
    for klass in defaultname::BODY.__mro__:
        if "alink" in klass.__dict__:
            descriptor = klass.__dict__["alink"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::body_has_vlink():
    assert hasattr(defaultname::BODY, "vlink")
    descriptor = None
    for klass in defaultname::BODY.__mro__:
        if "vlink" in klass.__dict__:
            descriptor = klass.__dict__["vlink"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::body_has_background():
    assert hasattr(defaultname::BODY, "background")
    descriptor = None
    for klass in defaultname::BODY.__mro__:
        if "background" in klass.__dict__:
            descriptor = klass.__dict__["background"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::body_has_link():
    assert hasattr(defaultname::BODY, "link")
    descriptor = None
    for klass in defaultname::BODY.__mro__:
        if "link" in klass.__dict__:
            descriptor = klass.__dict__["link"]
            break
    assert isinstance(descriptor, property)

def test_defaultname::body_has_bgcolor():
    assert hasattr(defaultname::BODY, "bgcolor")
    descriptor = None
    for klass in defaultname::BODY.__mro__:
        if "bgcolor" in klass.__dict__:
            descriptor = klass.__dict__["bgcolor"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::htmlelement_is_not_abstract():
    assert not inspect.isabstract(defaultname::HTMLElement)


def test_defaultname::htmlelement_constructor_exists():
    assert callable(defaultname::HTMLElement.__init__)


def test_defaultname::htmlelement_constructor_args():
    sig = inspect.signature(defaultname::HTMLElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_defaultname::htmlelement_has_value():
    assert hasattr(defaultname::HTMLElement, "value")
    descriptor = None
    for klass in defaultname::HTMLElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_defaultname::head_is_not_abstract():
    assert not inspect.isabstract(defaultname::HEAD)


def test_defaultname::head_constructor_exists():
    assert callable(defaultname::HEAD.__init__)


def test_defaultname::head_constructor_args():
    sig = inspect.signature(defaultname::HEAD.__init__)
    params = list(sig.parameters.keys())



def test_defaultname::html_is_not_abstract():
    assert not inspect.isabstract(defaultname::HTML)


def test_defaultname::html_constructor_exists():
    assert callable(defaultname::HTML.__init__)


def test_defaultname::html_constructor_args():
    sig = inspect.signature(defaultname::HTML.__init__)
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
defaultname::FRAMESET_strategy = st.builds(
    defaultname::FRAMESET,
    frameborder=
        safe_text,
    border=
        safe_text,
    framespacing=
        safe_text,
    rows=
        safe_text,
    cols=
        safe_text
)
FRAME_strategy = st.builds(
    FRAME,
)
defaultname::IFRAME_strategy = st.builds(
    defaultname::IFRAME,
)
defaultname::NOFRAME_strategy = st.builds(
    defaultname::NOFRAME,
)
defaultname::FRAME_strategy = st.builds(
    defaultname::FRAME,
    name=
        safe_text,
    scrolling=
        safe_text,
    src=
        safe_text,
    marginheight=
        safe_text,
    marginwidth=
        safe_text,
    noresize=
        safe_text
)
defaultname::TEXTAREA_strategy = st.builds(
    defaultname::TEXTAREA,
    rows=
        safe_text,
    cols=
        safe_text,
    name=
        safe_text
)
defaultname::OBJECT_strategy = st.builds(
    defaultname::OBJECT,
    standby=
        safe_text,
    type=
        safe_text,
    data=
        safe_text,
    classid=
        safe_text,
    id=
        safe_text
)
defaultname::PARAM_strategy = st.builds(
    defaultname::PARAM,
    paramValue=
        safe_text,
    name=
        safe_text
)
defaultname::APPLET_strategy = st.builds(
    defaultname::APPLET,
    align=
        safe_text,
    applet=
        safe_text,
    src=
        safe_text,
    class_=
        safe_text,
    width=
        safe_text,
    height=
        safe_text
)
defaultname::DD_strategy = st.builds(
    defaultname::DD,
)
defaultname::DT_strategy = st.builds(
    defaultname::DT,
)
defaultname::DL_strategy = st.builds(
    defaultname::DL,
)
ListElement_strategy = st.builds(
    ListElement,
)
defaultname::LI_strategy = st.builds(
    defaultname::LI,
    liValue=
        safe_text
)
defaultname::UL_strategy = st.builds(
    defaultname::UL,
)
defaultname::OL_strategy = st.builds(
    defaultname::OL,
    start=
        safe_text
)
defaultname::ListElement_strategy = st.builds(
    defaultname::ListElement,
    type=
        safe_text
)
defaultname::OPTION_strategy = st.builds(
    defaultname::OPTION,
    optionValue=
        safe_text,
    selected=
        safe_text
)
defaultname::SELECT_strategy = st.builds(
    defaultname::SELECT,
    size=
        safe_text,
    multiple=
        safe_text,
    name=
        safe_text
)
TABLEElement_strategy = st.builds(
    TABLEElement,
)
defaultname::TABLE_strategy = st.builds(
    defaultname::TABLE,
    cellpadding=
        safe_text,
    border=
        safe_text,
    cellspacing=
        safe_text,
    width=
        safe_text
)
defaultname::INPUT_strategy = st.builds(
    defaultname::INPUT,
    type=
        safe_text,
    name=
        safe_text,
    src=
        safe_text,
    inputValue=
        safe_text,
    size=
        safe_text,
    align=
        safe_text,
    maxlength=
        safe_text,
    checked=
        safe_text
)
defaultname::FORM_strategy = st.builds(
    defaultname::FORM,
    action=
        safe_text,
    method=
        safe_text
)
TD_strategy = st.builds(
    TD,
)
defaultname::TH_strategy = st.builds(
    defaultname::TH,
)
defaultname::TD_strategy = st.builds(
    defaultname::TD,
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
defaultname::TR_strategy = st.builds(
    defaultname::TR,
    align=
        safe_text,
    valign=
        safe_text
)
BODYElement_strategy = st.builds(
    BODYElement,
)
defaultname::TABLEElement_strategy = st.builds(
    defaultname::TABLEElement,
    background=
        safe_text,
    bgcolor=
        safe_text
)
defaultname::A_strategy = st.builds(
    defaultname::A,
    name=
        safe_text,
    ahref=
        safe_text,
    id=
        safe_text
)
defaultname::IMG_strategy = st.builds(
    defaultname::IMG,
    usemap=
        safe_text,
    vspace=
        safe_text,
    hspace=
        safe_text,
    alt=
        safe_text,
    ismap=
        safe_text,
    src=
        safe_text,
    border=
        safe_text,
    height=
        safe_text,
    width=
        safe_text,
    align=
        safe_text
)
defaultname::B_strategy = st.builds(
    defaultname::B,
)
defaultname::MAP_strategy = st.builds(
    defaultname::MAP,
)
defaultname::STRONG_strategy = st.builds(
    defaultname::STRONG,
)
defaultname::EM_strategy = st.builds(
    defaultname::EM,
)
defaultname::EMBED_strategy = st.builds(
    defaultname::EMBED,
    border=
        safe_text,
    src=
        safe_text,
    vspace=
        safe_text,
    hspace=
        safe_text,
    height=
        safe_text,
    width=
        safe_text,
    align=
        safe_text
)
defaultname::STRIKE_strategy = st.builds(
    defaultname::STRIKE,
)
defaultname::H2_strategy = st.builds(
    defaultname::H2,
)
defaultname::TT_strategy = st.builds(
    defaultname::TT,
)
defaultname::AREA_strategy = st.builds(
    defaultname::AREA,
    shape=
        safe_text,
    ahref=
        safe_text,
    coords=
        safe_text
)
defaultname::BR_strategy = st.builds(
    defaultname::BR,
    clear=
        safe_text
)
defaultname::SMALL_strategy = st.builds(
    defaultname::SMALL,
)
defaultname::H3_strategy = st.builds(
    defaultname::H3,
)
defaultname::SUP_strategy = st.builds(
    defaultname::SUP,
)
defaultname::STYLE_strategy = st.builds(
    defaultname::STYLE,
)
defaultname::NOEMBED_strategy = st.builds(
    defaultname::NOEMBED,
)
defaultname::SUB_strategy = st.builds(
    defaultname::SUB,
)
defaultname::H4_strategy = st.builds(
    defaultname::H4,
)
defaultname::PRE_strategy = st.builds(
    defaultname::PRE,
)
defaultname::FONT_strategy = st.builds(
    defaultname::FONT,
    face=
        safe_text,
    color=
        safe_text,
    size=
        safe_text
)
defaultname::P_strategy = st.builds(
    defaultname::P,
)
defaultname::SPAN_strategy = st.builds(
    defaultname::SPAN,
    style=
        safe_text
)
defaultname::BIG_strategy = st.builds(
    defaultname::BIG,
)
defaultname::I_strategy = st.builds(
    defaultname::I,
)
defaultname::DIV_strategy = st.builds(
    defaultname::DIV,
    align=
        safe_text
)
defaultname::H1_strategy = st.builds(
    defaultname::H1,
)
HEADElement_strategy = st.builds(
    HEADElement,
)
defaultname::TITLE_strategy = st.builds(
    defaultname::TITLE,
)
defaultname::LINK_strategy = st.builds(
    defaultname::LINK,
    ahref=
        safe_text,
    title=
        safe_text,
    type=
        safe_text,
    rel=
        safe_text
)
HTMLElement_strategy = st.builds(
    HTMLElement,
)
defaultname::BODYElement_strategy = st.builds(
    defaultname::BODYElement,
)
defaultname::HEADElement_strategy = st.builds(
    defaultname::HEADElement,
)
defaultname::BODY_strategy = st.builds(
    defaultname::BODY,
    text=
        safe_text,
    alink=
        safe_text,
    vlink=
        safe_text,
    background=
        safe_text,
    link=
        safe_text,
    bgcolor=
        safe_text
)
defaultname::HTMLElement_strategy = st.builds(
    defaultname::HTMLElement,
    value=
        safe_text
)
defaultname::HEAD_strategy = st.builds(
    defaultname::HEAD,
)
defaultname::HTML_strategy = st.builds(
    defaultname::HTML,
)

@given(instance=defaultname::FRAMESET_strategy)
@settings(max_examples=50)
def test_defaultname::frameset_instantiation(instance):
    assert isinstance(instance, defaultname::FRAMESET)

@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_frameborder_type(instance):
    assert isinstance(instance.frameborder, str)


@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_frameborder_setter(instance):
    original = instance.frameborder
    instance.frameborder = original
    assert instance.frameborder == original

@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_border_type(instance):
    assert isinstance(instance.border, str)


@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_framespacing_type(instance):
    assert isinstance(instance.framespacing, str)


@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_framespacing_setter(instance):
    original = instance.framespacing
    instance.framespacing = original
    assert instance.framespacing == original

@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_rows_type(instance):
    assert isinstance(instance.rows, str)


@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_cols_type(instance):
    assert isinstance(instance.cols, str)


@given(instance=defaultname::FRAMESET_strategy)
def test_defaultname::frameset_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original

@given(instance=FRAME_strategy)
@settings(max_examples=50)
def test_frame_instantiation(instance):
    assert isinstance(instance, FRAME)

@given(instance=defaultname::IFRAME_strategy)
@settings(max_examples=50)
def test_defaultname::iframe_instantiation(instance):
    assert isinstance(instance, defaultname::IFRAME)

@given(instance=defaultname::NOFRAME_strategy)
@settings(max_examples=50)
def test_defaultname::noframe_instantiation(instance):
    assert isinstance(instance, defaultname::NOFRAME)

@given(instance=defaultname::FRAME_strategy)
@settings(max_examples=50)
def test_defaultname::frame_instantiation(instance):
    assert isinstance(instance, defaultname::FRAME)

@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_scrolling_type(instance):
    assert isinstance(instance.scrolling, str)


@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_scrolling_setter(instance):
    original = instance.scrolling
    instance.scrolling = original
    assert instance.scrolling == original

@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_marginheight_type(instance):
    assert isinstance(instance.marginheight, str)


@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_marginheight_setter(instance):
    original = instance.marginheight
    instance.marginheight = original
    assert instance.marginheight == original

@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_marginwidth_type(instance):
    assert isinstance(instance.marginwidth, str)


@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_marginwidth_setter(instance):
    original = instance.marginwidth
    instance.marginwidth = original
    assert instance.marginwidth == original

@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_noresize_type(instance):
    assert isinstance(instance.noresize, str)


@given(instance=defaultname::FRAME_strategy)
def test_defaultname::frame_noresize_setter(instance):
    original = instance.noresize
    instance.noresize = original
    assert instance.noresize == original

@given(instance=defaultname::TEXTAREA_strategy)
@settings(max_examples=50)
def test_defaultname::textarea_instantiation(instance):
    assert isinstance(instance, defaultname::TEXTAREA)

@given(instance=defaultname::TEXTAREA_strategy)
def test_defaultname::textarea_rows_type(instance):
    assert isinstance(instance.rows, str)


@given(instance=defaultname::TEXTAREA_strategy)
def test_defaultname::textarea_rows_setter(instance):
    original = instance.rows
    instance.rows = original
    assert instance.rows == original

@given(instance=defaultname::TEXTAREA_strategy)
def test_defaultname::textarea_cols_type(instance):
    assert isinstance(instance.cols, str)


@given(instance=defaultname::TEXTAREA_strategy)
def test_defaultname::textarea_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original

@given(instance=defaultname::TEXTAREA_strategy)
def test_defaultname::textarea_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=defaultname::TEXTAREA_strategy)
def test_defaultname::textarea_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=defaultname::OBJECT_strategy)
@settings(max_examples=50)
def test_defaultname::object_instantiation(instance):
    assert isinstance(instance, defaultname::OBJECT)

@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_standby_type(instance):
    assert isinstance(instance.standby, str)


@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_standby_setter(instance):
    original = instance.standby
    instance.standby = original
    assert instance.standby == original

@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_data_type(instance):
    assert isinstance(instance.data, str)


@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_data_setter(instance):
    original = instance.data
    instance.data = original
    assert instance.data == original

@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_classid_type(instance):
    assert isinstance(instance.classid, str)


@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_classid_setter(instance):
    original = instance.classid
    instance.classid = original
    assert instance.classid == original

@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=defaultname::OBJECT_strategy)
def test_defaultname::object_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=defaultname::PARAM_strategy)
@settings(max_examples=50)
def test_defaultname::param_instantiation(instance):
    assert isinstance(instance, defaultname::PARAM)

@given(instance=defaultname::PARAM_strategy)
def test_defaultname::param_paramValue_type(instance):
    assert isinstance(instance.paramValue, str)


@given(instance=defaultname::PARAM_strategy)
def test_defaultname::param_paramValue_setter(instance):
    original = instance.paramValue
    instance.paramValue = original
    assert instance.paramValue == original

@given(instance=defaultname::PARAM_strategy)
def test_defaultname::param_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=defaultname::PARAM_strategy)
def test_defaultname::param_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=defaultname::APPLET_strategy)
@settings(max_examples=50)
def test_defaultname::applet_instantiation(instance):
    assert isinstance(instance, defaultname::APPLET)

@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_applet_type(instance):
    assert isinstance(instance.applet, str)


@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_applet_setter(instance):
    original = instance.applet
    instance.applet = original
    assert instance.applet == original

@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_class__type(instance):
    assert isinstance(instance.class_, str)


@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_class__setter(instance):
    original = instance.class_
    instance.class_ = original
    assert instance.class_ == original

@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=defaultname::APPLET_strategy)
def test_defaultname::applet_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=defaultname::DD_strategy)
@settings(max_examples=50)
def test_defaultname::dd_instantiation(instance):
    assert isinstance(instance, defaultname::DD)

@given(instance=defaultname::DT_strategy)
@settings(max_examples=50)
def test_defaultname::dt_instantiation(instance):
    assert isinstance(instance, defaultname::DT)

@given(instance=defaultname::DL_strategy)
@settings(max_examples=50)
def test_defaultname::dl_instantiation(instance):
    assert isinstance(instance, defaultname::DL)

@given(instance=ListElement_strategy)
@settings(max_examples=50)
def test_listelement_instantiation(instance):
    assert isinstance(instance, ListElement)

@given(instance=defaultname::LI_strategy)
@settings(max_examples=50)
def test_defaultname::li_instantiation(instance):
    assert isinstance(instance, defaultname::LI)

@given(instance=defaultname::LI_strategy)
def test_defaultname::li_liValue_type(instance):
    assert isinstance(instance.liValue, str)


@given(instance=defaultname::LI_strategy)
def test_defaultname::li_liValue_setter(instance):
    original = instance.liValue
    instance.liValue = original
    assert instance.liValue == original

@given(instance=defaultname::UL_strategy)
@settings(max_examples=50)
def test_defaultname::ul_instantiation(instance):
    assert isinstance(instance, defaultname::UL)

@given(instance=defaultname::OL_strategy)
@settings(max_examples=50)
def test_defaultname::ol_instantiation(instance):
    assert isinstance(instance, defaultname::OL)

@given(instance=defaultname::OL_strategy)
def test_defaultname::ol_start_type(instance):
    assert isinstance(instance.start, str)


@given(instance=defaultname::OL_strategy)
def test_defaultname::ol_start_setter(instance):
    original = instance.start
    instance.start = original
    assert instance.start == original

@given(instance=defaultname::ListElement_strategy)
@settings(max_examples=50)
def test_defaultname::listelement_instantiation(instance):
    assert isinstance(instance, defaultname::ListElement)

@given(instance=defaultname::ListElement_strategy)
def test_defaultname::listelement_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=defaultname::ListElement_strategy)
def test_defaultname::listelement_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=defaultname::OPTION_strategy)
@settings(max_examples=50)
def test_defaultname::option_instantiation(instance):
    assert isinstance(instance, defaultname::OPTION)

@given(instance=defaultname::OPTION_strategy)
def test_defaultname::option_optionValue_type(instance):
    assert isinstance(instance.optionValue, str)


@given(instance=defaultname::OPTION_strategy)
def test_defaultname::option_optionValue_setter(instance):
    original = instance.optionValue
    instance.optionValue = original
    assert instance.optionValue == original

@given(instance=defaultname::OPTION_strategy)
def test_defaultname::option_selected_type(instance):
    assert isinstance(instance.selected, str)


@given(instance=defaultname::OPTION_strategy)
def test_defaultname::option_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=defaultname::SELECT_strategy)
@settings(max_examples=50)
def test_defaultname::select_instantiation(instance):
    assert isinstance(instance, defaultname::SELECT)

@given(instance=defaultname::SELECT_strategy)
def test_defaultname::select_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=defaultname::SELECT_strategy)
def test_defaultname::select_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=defaultname::SELECT_strategy)
def test_defaultname::select_multiple_type(instance):
    assert isinstance(instance.multiple, str)


@given(instance=defaultname::SELECT_strategy)
def test_defaultname::select_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=defaultname::SELECT_strategy)
def test_defaultname::select_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=defaultname::SELECT_strategy)
def test_defaultname::select_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=TABLEElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TABLEElement)

@given(instance=defaultname::TABLE_strategy)
@settings(max_examples=50)
def test_defaultname::table_instantiation(instance):
    assert isinstance(instance, defaultname::TABLE)

@given(instance=defaultname::TABLE_strategy)
def test_defaultname::table_cellpadding_type(instance):
    assert isinstance(instance.cellpadding, str)


@given(instance=defaultname::TABLE_strategy)
def test_defaultname::table_cellpadding_setter(instance):
    original = instance.cellpadding
    instance.cellpadding = original
    assert instance.cellpadding == original

@given(instance=defaultname::TABLE_strategy)
def test_defaultname::table_border_type(instance):
    assert isinstance(instance.border, str)


@given(instance=defaultname::TABLE_strategy)
def test_defaultname::table_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=defaultname::TABLE_strategy)
def test_defaultname::table_cellspacing_type(instance):
    assert isinstance(instance.cellspacing, str)


@given(instance=defaultname::TABLE_strategy)
def test_defaultname::table_cellspacing_setter(instance):
    original = instance.cellspacing
    instance.cellspacing = original
    assert instance.cellspacing == original

@given(instance=defaultname::TABLE_strategy)
def test_defaultname::table_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=defaultname::TABLE_strategy)
def test_defaultname::table_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=defaultname::INPUT_strategy)
@settings(max_examples=50)
def test_defaultname::input_instantiation(instance):
    assert isinstance(instance, defaultname::INPUT)

@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_inputValue_type(instance):
    assert isinstance(instance.inputValue, str)


@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_inputValue_setter(instance):
    original = instance.inputValue
    instance.inputValue = original
    assert instance.inputValue == original

@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_maxlength_type(instance):
    assert isinstance(instance.maxlength, str)


@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_maxlength_setter(instance):
    original = instance.maxlength
    instance.maxlength = original
    assert instance.maxlength == original

@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_checked_type(instance):
    assert isinstance(instance.checked, str)


@given(instance=defaultname::INPUT_strategy)
def test_defaultname::input_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=defaultname::FORM_strategy)
@settings(max_examples=50)
def test_defaultname::form_instantiation(instance):
    assert isinstance(instance, defaultname::FORM)

@given(instance=defaultname::FORM_strategy)
def test_defaultname::form_action_type(instance):
    assert isinstance(instance.action, str)


@given(instance=defaultname::FORM_strategy)
def test_defaultname::form_action_setter(instance):
    original = instance.action
    instance.action = original
    assert instance.action == original

@given(instance=defaultname::FORM_strategy)
def test_defaultname::form_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=defaultname::FORM_strategy)
def test_defaultname::form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=TD_strategy)
@settings(max_examples=50)
def test_td_instantiation(instance):
    assert isinstance(instance, TD)

@given(instance=defaultname::TH_strategy)
@settings(max_examples=50)
def test_defaultname::th_instantiation(instance):
    assert isinstance(instance, defaultname::TH)

@given(instance=defaultname::TD_strategy)
@settings(max_examples=50)
def test_defaultname::td_instantiation(instance):
    assert isinstance(instance, defaultname::TD)

@given(instance=defaultname::TD_strategy)
def test_defaultname::td_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=defaultname::TD_strategy)
def test_defaultname::td_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname::TD_strategy)
def test_defaultname::td_rowspan_type(instance):
    assert isinstance(instance.rowspan, str)


@given(instance=defaultname::TD_strategy)
def test_defaultname::td_rowspan_setter(instance):
    original = instance.rowspan
    instance.rowspan = original
    assert instance.rowspan == original

@given(instance=defaultname::TD_strategy)
def test_defaultname::td_colspan_type(instance):
    assert isinstance(instance.colspan, str)


@given(instance=defaultname::TD_strategy)
def test_defaultname::td_colspan_setter(instance):
    original = instance.colspan
    instance.colspan = original
    assert instance.colspan == original

@given(instance=defaultname::TD_strategy)
def test_defaultname::td_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=defaultname::TD_strategy)
def test_defaultname::td_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=defaultname::TD_strategy)
def test_defaultname::td_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=defaultname::TD_strategy)
def test_defaultname::td_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=defaultname::TR_strategy)
@settings(max_examples=50)
def test_defaultname::tr_instantiation(instance):
    assert isinstance(instance, defaultname::TR)

@given(instance=defaultname::TR_strategy)
def test_defaultname::tr_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=defaultname::TR_strategy)
def test_defaultname::tr_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname::TR_strategy)
def test_defaultname::tr_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=defaultname::TR_strategy)
def test_defaultname::tr_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=BODYElement_strategy)
@settings(max_examples=50)
def test_bodyelement_instantiation(instance):
    assert isinstance(instance, BODYElement)

@given(instance=defaultname::TABLEElement_strategy)
@settings(max_examples=50)
def test_defaultname::tableelement_instantiation(instance):
    assert isinstance(instance, defaultname::TABLEElement)

@given(instance=defaultname::TABLEElement_strategy)
def test_defaultname::tableelement_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=defaultname::TABLEElement_strategy)
def test_defaultname::tableelement_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=defaultname::TABLEElement_strategy)
def test_defaultname::tableelement_bgcolor_type(instance):
    assert isinstance(instance.bgcolor, str)


@given(instance=defaultname::TABLEElement_strategy)
def test_defaultname::tableelement_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original

@given(instance=defaultname::A_strategy)
@settings(max_examples=50)
def test_defaultname::a_instantiation(instance):
    assert isinstance(instance, defaultname::A)

@given(instance=defaultname::A_strategy)
def test_defaultname::a_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=defaultname::A_strategy)
def test_defaultname::a_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=defaultname::A_strategy)
def test_defaultname::a_ahref_type(instance):
    assert isinstance(instance.ahref, str)


@given(instance=defaultname::A_strategy)
def test_defaultname::a_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original

@given(instance=defaultname::A_strategy)
def test_defaultname::a_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=defaultname::A_strategy)
def test_defaultname::a_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=defaultname::IMG_strategy)
@settings(max_examples=50)
def test_defaultname::img_instantiation(instance):
    assert isinstance(instance, defaultname::IMG)

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_usemap_type(instance):
    assert isinstance(instance.usemap, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_usemap_setter(instance):
    original = instance.usemap
    instance.usemap = original
    assert instance.usemap == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_vspace_type(instance):
    assert isinstance(instance.vspace, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_vspace_setter(instance):
    original = instance.vspace
    instance.vspace = original
    assert instance.vspace == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_hspace_type(instance):
    assert isinstance(instance.hspace, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_hspace_setter(instance):
    original = instance.hspace
    instance.hspace = original
    assert instance.hspace == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_alt_type(instance):
    assert isinstance(instance.alt, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_ismap_type(instance):
    assert isinstance(instance.ismap, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_ismap_setter(instance):
    original = instance.ismap
    instance.ismap = original
    assert instance.ismap == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_border_type(instance):
    assert isinstance(instance.border, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=defaultname::IMG_strategy)
def test_defaultname::img_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname::B_strategy)
@settings(max_examples=50)
def test_defaultname::b_instantiation(instance):
    assert isinstance(instance, defaultname::B)

@given(instance=defaultname::MAP_strategy)
@settings(max_examples=50)
def test_defaultname::map_instantiation(instance):
    assert isinstance(instance, defaultname::MAP)

@given(instance=defaultname::STRONG_strategy)
@settings(max_examples=50)
def test_defaultname::strong_instantiation(instance):
    assert isinstance(instance, defaultname::STRONG)

@given(instance=defaultname::EM_strategy)
@settings(max_examples=50)
def test_defaultname::em_instantiation(instance):
    assert isinstance(instance, defaultname::EM)

@given(instance=defaultname::EMBED_strategy)
@settings(max_examples=50)
def test_defaultname::embed_instantiation(instance):
    assert isinstance(instance, defaultname::EMBED)

@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_border_type(instance):
    assert isinstance(instance.border, str)


@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_border_setter(instance):
    original = instance.border
    instance.border = original
    assert instance.border == original

@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_src_type(instance):
    assert isinstance(instance.src, str)


@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original

@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_vspace_type(instance):
    assert isinstance(instance.vspace, str)


@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_vspace_setter(instance):
    original = instance.vspace
    instance.vspace = original
    assert instance.vspace == original

@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_hspace_type(instance):
    assert isinstance(instance.hspace, str)


@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_hspace_setter(instance):
    original = instance.hspace
    instance.hspace = original
    assert instance.hspace == original

@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_height_type(instance):
    assert isinstance(instance.height, str)


@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=defaultname::EMBED_strategy)
def test_defaultname::embed_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname::STRIKE_strategy)
@settings(max_examples=50)
def test_defaultname::strike_instantiation(instance):
    assert isinstance(instance, defaultname::STRIKE)

@given(instance=defaultname::H2_strategy)
@settings(max_examples=50)
def test_defaultname::h2_instantiation(instance):
    assert isinstance(instance, defaultname::H2)

@given(instance=defaultname::TT_strategy)
@settings(max_examples=50)
def test_defaultname::tt_instantiation(instance):
    assert isinstance(instance, defaultname::TT)

@given(instance=defaultname::AREA_strategy)
@settings(max_examples=50)
def test_defaultname::area_instantiation(instance):
    assert isinstance(instance, defaultname::AREA)

@given(instance=defaultname::AREA_strategy)
def test_defaultname::area_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=defaultname::AREA_strategy)
def test_defaultname::area_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=defaultname::AREA_strategy)
def test_defaultname::area_ahref_type(instance):
    assert isinstance(instance.ahref, str)


@given(instance=defaultname::AREA_strategy)
def test_defaultname::area_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original

@given(instance=defaultname::AREA_strategy)
def test_defaultname::area_coords_type(instance):
    assert isinstance(instance.coords, str)


@given(instance=defaultname::AREA_strategy)
def test_defaultname::area_coords_setter(instance):
    original = instance.coords
    instance.coords = original
    assert instance.coords == original

@given(instance=defaultname::BR_strategy)
@settings(max_examples=50)
def test_defaultname::br_instantiation(instance):
    assert isinstance(instance, defaultname::BR)

@given(instance=defaultname::BR_strategy)
def test_defaultname::br_clear_type(instance):
    assert isinstance(instance.clear, str)


@given(instance=defaultname::BR_strategy)
def test_defaultname::br_clear_setter(instance):
    original = instance.clear
    instance.clear = original
    assert instance.clear == original

@given(instance=defaultname::SMALL_strategy)
@settings(max_examples=50)
def test_defaultname::small_instantiation(instance):
    assert isinstance(instance, defaultname::SMALL)

@given(instance=defaultname::H3_strategy)
@settings(max_examples=50)
def test_defaultname::h3_instantiation(instance):
    assert isinstance(instance, defaultname::H3)

@given(instance=defaultname::SUP_strategy)
@settings(max_examples=50)
def test_defaultname::sup_instantiation(instance):
    assert isinstance(instance, defaultname::SUP)

@given(instance=defaultname::STYLE_strategy)
@settings(max_examples=50)
def test_defaultname::style_instantiation(instance):
    assert isinstance(instance, defaultname::STYLE)

@given(instance=defaultname::NOEMBED_strategy)
@settings(max_examples=50)
def test_defaultname::noembed_instantiation(instance):
    assert isinstance(instance, defaultname::NOEMBED)

@given(instance=defaultname::SUB_strategy)
@settings(max_examples=50)
def test_defaultname::sub_instantiation(instance):
    assert isinstance(instance, defaultname::SUB)

@given(instance=defaultname::H4_strategy)
@settings(max_examples=50)
def test_defaultname::h4_instantiation(instance):
    assert isinstance(instance, defaultname::H4)

@given(instance=defaultname::PRE_strategy)
@settings(max_examples=50)
def test_defaultname::pre_instantiation(instance):
    assert isinstance(instance, defaultname::PRE)

@given(instance=defaultname::FONT_strategy)
@settings(max_examples=50)
def test_defaultname::font_instantiation(instance):
    assert isinstance(instance, defaultname::FONT)

@given(instance=defaultname::FONT_strategy)
def test_defaultname::font_face_type(instance):
    assert isinstance(instance.face, str)


@given(instance=defaultname::FONT_strategy)
def test_defaultname::font_face_setter(instance):
    original = instance.face
    instance.face = original
    assert instance.face == original

@given(instance=defaultname::FONT_strategy)
def test_defaultname::font_color_type(instance):
    assert isinstance(instance.color, str)


@given(instance=defaultname::FONT_strategy)
def test_defaultname::font_color_setter(instance):
    original = instance.color
    instance.color = original
    assert instance.color == original

@given(instance=defaultname::FONT_strategy)
def test_defaultname::font_size_type(instance):
    assert isinstance(instance.size, str)


@given(instance=defaultname::FONT_strategy)
def test_defaultname::font_size_setter(instance):
    original = instance.size
    instance.size = original
    assert instance.size == original

@given(instance=defaultname::P_strategy)
@settings(max_examples=50)
def test_defaultname::p_instantiation(instance):
    assert isinstance(instance, defaultname::P)

@given(instance=defaultname::SPAN_strategy)
@settings(max_examples=50)
def test_defaultname::span_instantiation(instance):
    assert isinstance(instance, defaultname::SPAN)

@given(instance=defaultname::SPAN_strategy)
def test_defaultname::span_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=defaultname::SPAN_strategy)
def test_defaultname::span_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=defaultname::BIG_strategy)
@settings(max_examples=50)
def test_defaultname::big_instantiation(instance):
    assert isinstance(instance, defaultname::BIG)

@given(instance=defaultname::I_strategy)
@settings(max_examples=50)
def test_defaultname::i_instantiation(instance):
    assert isinstance(instance, defaultname::I)

@given(instance=defaultname::DIV_strategy)
@settings(max_examples=50)
def test_defaultname::div_instantiation(instance):
    assert isinstance(instance, defaultname::DIV)

@given(instance=defaultname::DIV_strategy)
def test_defaultname::div_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=defaultname::DIV_strategy)
def test_defaultname::div_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=defaultname::H1_strategy)
@settings(max_examples=50)
def test_defaultname::h1_instantiation(instance):
    assert isinstance(instance, defaultname::H1)

@given(instance=HEADElement_strategy)
@settings(max_examples=50)
def test_headelement_instantiation(instance):
    assert isinstance(instance, HEADElement)

@given(instance=defaultname::TITLE_strategy)
@settings(max_examples=50)
def test_defaultname::title_instantiation(instance):
    assert isinstance(instance, defaultname::TITLE)

@given(instance=defaultname::LINK_strategy)
@settings(max_examples=50)
def test_defaultname::link_instantiation(instance):
    assert isinstance(instance, defaultname::LINK)

@given(instance=defaultname::LINK_strategy)
def test_defaultname::link_ahref_type(instance):
    assert isinstance(instance.ahref, str)


@given(instance=defaultname::LINK_strategy)
def test_defaultname::link_ahref_setter(instance):
    original = instance.ahref
    instance.ahref = original
    assert instance.ahref == original

@given(instance=defaultname::LINK_strategy)
def test_defaultname::link_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=defaultname::LINK_strategy)
def test_defaultname::link_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=defaultname::LINK_strategy)
def test_defaultname::link_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=defaultname::LINK_strategy)
def test_defaultname::link_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=defaultname::LINK_strategy)
def test_defaultname::link_rel_type(instance):
    assert isinstance(instance.rel, str)


@given(instance=defaultname::LINK_strategy)
def test_defaultname::link_rel_setter(instance):
    original = instance.rel
    instance.rel = original
    assert instance.rel == original

@given(instance=HTMLElement_strategy)
@settings(max_examples=50)
def test_htmlelement_instantiation(instance):
    assert isinstance(instance, HTMLElement)

@given(instance=defaultname::BODYElement_strategy)
@settings(max_examples=50)
def test_defaultname::bodyelement_instantiation(instance):
    assert isinstance(instance, defaultname::BODYElement)

@given(instance=defaultname::HEADElement_strategy)
@settings(max_examples=50)
def test_defaultname::headelement_instantiation(instance):
    assert isinstance(instance, defaultname::HEADElement)

@given(instance=defaultname::BODY_strategy)
@settings(max_examples=50)
def test_defaultname::body_instantiation(instance):
    assert isinstance(instance, defaultname::BODY)

@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_alink_type(instance):
    assert isinstance(instance.alink, str)


@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_alink_setter(instance):
    original = instance.alink
    instance.alink = original
    assert instance.alink == original

@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_vlink_type(instance):
    assert isinstance(instance.vlink, str)


@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_vlink_setter(instance):
    original = instance.vlink
    instance.vlink = original
    assert instance.vlink == original

@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_background_type(instance):
    assert isinstance(instance.background, str)


@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_background_setter(instance):
    original = instance.background
    instance.background = original
    assert instance.background == original

@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_link_type(instance):
    assert isinstance(instance.link, str)


@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_link_setter(instance):
    original = instance.link
    instance.link = original
    assert instance.link == original

@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_bgcolor_type(instance):
    assert isinstance(instance.bgcolor, str)


@given(instance=defaultname::BODY_strategy)
def test_defaultname::body_bgcolor_setter(instance):
    original = instance.bgcolor
    instance.bgcolor = original
    assert instance.bgcolor == original

@given(instance=defaultname::HTMLElement_strategy)
@settings(max_examples=50)
def test_defaultname::htmlelement_instantiation(instance):
    assert isinstance(instance, defaultname::HTMLElement)

@given(instance=defaultname::HTMLElement_strategy)
def test_defaultname::htmlelement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=defaultname::HTMLElement_strategy)
def test_defaultname::htmlelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=defaultname::HEAD_strategy)
@settings(max_examples=50)
def test_defaultname::head_instantiation(instance):
    assert isinstance(instance, defaultname::HEAD)

@given(instance=defaultname::HTML_strategy)
@settings(max_examples=50)
def test_defaultname::html_instantiation(instance):
    assert isinstance(instance, defaultname::HTML)
