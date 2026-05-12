import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    IDREFS,
    XHTML_TrElement,
    TrElement,
    MultiLength,
    Tr,
    Cellvalign,
    Cellhalign,
    Col,
    XHTML_ColElement,
    Tbody,
    XHTML_TableElement,
    Pixels,
    Colgroup,
    TableElement,
    Tfoot,
    Thead,
    ColElement,
    Caption,
    XHTML_Cellvalign,
    XHTML_Cellhalign,
    XHTML_FieldsetElement,
    XHTML_SelectElement,
    Option,
    SelectElement,
    Inlineforms,
    Charsets,
    ContentTypes,
    MapContent,
    XHTML_MapElementContent,
    XHTML_MapElement,
    MapElement,
    XHTML_MapContent,
    UriList,
    XHTML_ObjectElement,
    Fontstyle,
    Phrase,
    Focus,
    Specialpre,
    Coords,
    Blocktext,
    Datetime,
    Heading,
    DlElement,
    XHTML_Dt,
    XHTML_Dd,
    Li,
    Lists,
    Miscinline,
    EMPTY,
    XHTML_Base,
    XHTML_TitleBaseHeadElement,
    TitleBaseHeadElement,
    MediaDesc,
    LinkTypes,
    Attrs,
    XHTML_H2,
    XHTML_Dl,
    XHTML_Em,
    XHTML_Select,
    XHTML_H3,
    XHTML_Area,
    XHTML_DlElement,
    XHTML_H4,
    XHTML_Tbody,
    XHTML_Acronym,
    XHTML_Dfn,
    XHTML_Thead,
    XHTML_Pre,
    XHTML_Tr,
    XHTML_Tfoot,
    XHTML_Big,
    XHTML_Address,
    XHTML_Ins,
    XHTML_I,
    XHTML_Span,
    XHTML_Ol,
    XHTML_Li,
    XHTML_Col,
    XHTML_Ul,
    XHTML_Small,
    XHTML_Hr,
    XHTML_H1,
    XHTML_Label,
    XHTML_Samp,
    XHTML_H6,
    XHTML_Sub,
    XHTML_Input,
    XHTML_Optgroup,
    XHTML_B,
    XHTML_Abbr,
    XHTML_Var,
    XHTML_Strong,
    XHTML_Body,
    XHTML_Button,
    XHTML_Code,
    XHTML_Caption,
    XHTML_Kbd,
    XHTML_Tt,
    XHTML_Sup,
    XHTML_Q,
    XHTML_Cite,
    XHTML_Del,
    XHTML_H5,
    XHTML_Blockquote,
    XHTML_Td,
    XHTML_Th,
    XHTML_Colgroup,
    Html,
    HeadElement,
    HeadMisc,
    XHTML_Meta,
    XHTML_Link,
    XHTML_Head,
    XHTML_HeadMisc,
    Body,
    XHTML_BaseHeadElement,
    Base,
    XHTML_BaseTitleHeadElement,
    BaseTitleHeadElement,
    Title,
    XHTML_TitleHeadElement,
    XHTML_HeadElement,
    XHTML_AContent,
    XHTML_Flow,
    XHTML_Block,
    Head,
    XHTML_Html,
    XHTML_ButtonContent,
    XHTML_FormContent,
    XHTML_PreContent,
    AContent,
    ButtonContent,
    inline,
    XHTML_Special,
    PreContent,
    XHTML_Phrase,
    XHTML_Fontstyle,
    XHTML_A,
    Special,
    XHTML_Img,
    XHTML_Object,
    XHTML_Specialpre,
    Number,
    Character,
    XHTML_Focus,
    block,
    XHTML_Fieldset,
    XHTML_Lists,
    XHTML_Blocktext,
    XHTML_P,
    XHTML_Div,
    XHTML_Table,
    XHTML_Heading,
    PCDATA,
    XHTML_Style,
    XHTML_Script,
    XHTML_Textarea,
    XHTML_Option,
    XHTML_Title,
    FieldsetElement,
    XHTML_Legend,
    MapElementContent,
    ObjectElement,
    XHTML_Param,
    FormContent,
    Flow,
    XHTML_Inline,
    Block,
    XHTML_block,
    XHTML_Form,
    XHTML_Misc,
    Inline,
    XHTML_inline,
    Misc,
    XHTML_Noscript,
    XHTML_Miscinline,
    XHTML_Inlineforms,
    ScriptExpression,
    XHTML_Events,
    LanguageCode,
    XHTML_I18n,
    Events,
    I18n,
    XHTML_Map,
    CoreAttrs,
    XHTML_Br,
    XHTML_Bdo,
    XHTML_Attrs,
    URI,
    Text,
    StyleSheet,
    ID,
    XHTML_CoreAttrs,
    Length,
    XHTML_Coords,
    ContentType,
    XHTML_ContentTypes,
    CDATA,
    XHTML_Datetime,
    XHTML_StyleSheet,
    XHTML_Length,
    XHTML_Pixels,
    XHTML_MultiLength,
    XHTML_ScriptExpression,
    XHTML_Text,
    XHTML_ContentType,
    XHTML_EMPTY,
    IDREF,
    XHTML_IDREFS,
    XHTML_UriList,
    XHTML_URI,
    XHTML_MediaDesc,
    XHTML_LinkTypes,
    XHTML_Number,
    XHTML_Character,
    NMTOKEN,
    XHTML_LanguageCode,
    Charset,
    XHTML_Charsets,
    XHTML_Charset,
    ValuedElement,
    XHTML_IDREF,
    XHTML_NMTOKEN,
    XHTML_ID,
    XHTML_PCDATA,
    XHTML_CDATA,
    XHTML_ValuedElement,
    CellHAlign,
    TRules,
    CellVAlign,
    Shape,
    InputType,
    ButtonType,
    TFrame,
    ValueType,
    Scope,
    FomeMethod,
    Direction,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_idrefs_is_not_abstract():
    assert not inspect.isabstract(IDREFS)


def test_idrefs_constructor_exists():
    assert callable(IDREFS.__init__)


def test_idrefs_constructor_args():
    sig = inspect.signature(IDREFS.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_trelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_TrElement)


def test_xhtml_trelement_constructor_exists():
    assert callable(XHTML_TrElement.__init__)


def test_xhtml_trelement_constructor_args():
    sig = inspect.signature(XHTML_TrElement.__init__)
    params = list(sig.parameters.keys())



def test_trelement_is_not_abstract():
    assert not inspect.isabstract(TrElement)


def test_trelement_constructor_exists():
    assert callable(TrElement.__init__)


def test_trelement_constructor_args():
    sig = inspect.signature(TrElement.__init__)
    params = list(sig.parameters.keys())



def test_multilength_is_not_abstract():
    assert not inspect.isabstract(MultiLength)


def test_multilength_constructor_exists():
    assert callable(MultiLength.__init__)


def test_multilength_constructor_args():
    sig = inspect.signature(MultiLength.__init__)
    params = list(sig.parameters.keys())



def test_tr_is_not_abstract():
    assert not inspect.isabstract(Tr)


def test_tr_constructor_exists():
    assert callable(Tr.__init__)


def test_tr_constructor_args():
    sig = inspect.signature(Tr.__init__)
    params = list(sig.parameters.keys())



def test_cellvalign_is_not_abstract():
    assert not inspect.isabstract(Cellvalign)


def test_cellvalign_constructor_exists():
    assert callable(Cellvalign.__init__)


def test_cellvalign_constructor_args():
    sig = inspect.signature(Cellvalign.__init__)
    params = list(sig.parameters.keys())



def test_cellhalign_is_not_abstract():
    assert not inspect.isabstract(Cellhalign)


def test_cellhalign_constructor_exists():
    assert callable(Cellhalign.__init__)


def test_cellhalign_constructor_args():
    sig = inspect.signature(Cellhalign.__init__)
    params = list(sig.parameters.keys())



def test_col_is_not_abstract():
    assert not inspect.isabstract(Col)


def test_col_constructor_exists():
    assert callable(Col.__init__)


def test_col_constructor_args():
    sig = inspect.signature(Col.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_colelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_ColElement)


def test_xhtml_colelement_constructor_exists():
    assert callable(XHTML_ColElement.__init__)


def test_xhtml_colelement_constructor_args():
    sig = inspect.signature(XHTML_ColElement.__init__)
    params = list(sig.parameters.keys())



def test_tbody_is_not_abstract():
    assert not inspect.isabstract(Tbody)


def test_tbody_constructor_exists():
    assert callable(Tbody.__init__)


def test_tbody_constructor_args():
    sig = inspect.signature(Tbody.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_tableelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_TableElement)


def test_xhtml_tableelement_constructor_exists():
    assert callable(XHTML_TableElement.__init__)


def test_xhtml_tableelement_constructor_args():
    sig = inspect.signature(XHTML_TableElement.__init__)
    params = list(sig.parameters.keys())



def test_pixels_is_not_abstract():
    assert not inspect.isabstract(Pixels)


def test_pixels_constructor_exists():
    assert callable(Pixels.__init__)


def test_pixels_constructor_args():
    sig = inspect.signature(Pixels.__init__)
    params = list(sig.parameters.keys())



def test_colgroup_is_not_abstract():
    assert not inspect.isabstract(Colgroup)


def test_colgroup_constructor_exists():
    assert callable(Colgroup.__init__)


def test_colgroup_constructor_args():
    sig = inspect.signature(Colgroup.__init__)
    params = list(sig.parameters.keys())



def test_tableelement_is_not_abstract():
    assert not inspect.isabstract(TableElement)


def test_tableelement_constructor_exists():
    assert callable(TableElement.__init__)


def test_tableelement_constructor_args():
    sig = inspect.signature(TableElement.__init__)
    params = list(sig.parameters.keys())



def test_tfoot_is_not_abstract():
    assert not inspect.isabstract(Tfoot)


def test_tfoot_constructor_exists():
    assert callable(Tfoot.__init__)


def test_tfoot_constructor_args():
    sig = inspect.signature(Tfoot.__init__)
    params = list(sig.parameters.keys())



def test_thead_is_not_abstract():
    assert not inspect.isabstract(Thead)


def test_thead_constructor_exists():
    assert callable(Thead.__init__)


def test_thead_constructor_args():
    sig = inspect.signature(Thead.__init__)
    params = list(sig.parameters.keys())



def test_colelement_is_not_abstract():
    assert not inspect.isabstract(ColElement)


def test_colelement_constructor_exists():
    assert callable(ColElement.__init__)


def test_colelement_constructor_args():
    sig = inspect.signature(ColElement.__init__)
    params = list(sig.parameters.keys())



def test_caption_is_not_abstract():
    assert not inspect.isabstract(Caption)


def test_caption_constructor_exists():
    assert callable(Caption.__init__)


def test_caption_constructor_args():
    sig = inspect.signature(Caption.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_cellvalign_is_not_abstract():
    assert not inspect.isabstract(XHTML_Cellvalign)


def test_xhtml_cellvalign_constructor_exists():
    assert callable(XHTML_Cellvalign.__init__)


def test_xhtml_cellvalign_constructor_args():
    sig = inspect.signature(XHTML_Cellvalign.__init__)
    params = list(sig.parameters.keys())
    assert "valign" in params, "Missing parameter 'valign'"

def test_xhtml_cellvalign_has_valign():
    assert hasattr(XHTML_Cellvalign, "valign")
    descriptor = None
    for klass in XHTML_Cellvalign.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_cellhalign_is_not_abstract():
    assert not inspect.isabstract(XHTML_Cellhalign)


def test_xhtml_cellhalign_constructor_exists():
    assert callable(XHTML_Cellhalign.__init__)


def test_xhtml_cellhalign_constructor_args():
    sig = inspect.signature(XHTML_Cellhalign.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_xhtml_cellhalign_has_align():
    assert hasattr(XHTML_Cellhalign, "align")
    descriptor = None
    for klass in XHTML_Cellhalign.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_fieldsetelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_FieldsetElement)


def test_xhtml_fieldsetelement_constructor_exists():
    assert callable(XHTML_FieldsetElement.__init__)


def test_xhtml_fieldsetelement_constructor_args():
    sig = inspect.signature(XHTML_FieldsetElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_selectelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_SelectElement)


def test_xhtml_selectelement_constructor_exists():
    assert callable(XHTML_SelectElement.__init__)


def test_xhtml_selectelement_constructor_args():
    sig = inspect.signature(XHTML_SelectElement.__init__)
    params = list(sig.parameters.keys())



def test_option_is_not_abstract():
    assert not inspect.isabstract(Option)


def test_option_constructor_exists():
    assert callable(Option.__init__)


def test_option_constructor_args():
    sig = inspect.signature(Option.__init__)
    params = list(sig.parameters.keys())



def test_selectelement_is_not_abstract():
    assert not inspect.isabstract(SelectElement)


def test_selectelement_constructor_exists():
    assert callable(SelectElement.__init__)


def test_selectelement_constructor_args():
    sig = inspect.signature(SelectElement.__init__)
    params = list(sig.parameters.keys())



def test_inlineforms_is_not_abstract():
    assert not inspect.isabstract(Inlineforms)


def test_inlineforms_constructor_exists():
    assert callable(Inlineforms.__init__)


def test_inlineforms_constructor_args():
    sig = inspect.signature(Inlineforms.__init__)
    params = list(sig.parameters.keys())



def test_charsets_is_not_abstract():
    assert not inspect.isabstract(Charsets)


def test_charsets_constructor_exists():
    assert callable(Charsets.__init__)


def test_charsets_constructor_args():
    sig = inspect.signature(Charsets.__init__)
    params = list(sig.parameters.keys())



def test_contenttypes_is_not_abstract():
    assert not inspect.isabstract(ContentTypes)


def test_contenttypes_constructor_exists():
    assert callable(ContentTypes.__init__)


def test_contenttypes_constructor_args():
    sig = inspect.signature(ContentTypes.__init__)
    params = list(sig.parameters.keys())



def test_mapcontent_is_not_abstract():
    assert not inspect.isabstract(MapContent)


def test_mapcontent_constructor_exists():
    assert callable(MapContent.__init__)


def test_mapcontent_constructor_args():
    sig = inspect.signature(MapContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_mapelementcontent_is_not_abstract():
    assert not inspect.isabstract(XHTML_MapElementContent)


def test_xhtml_mapelementcontent_constructor_exists():
    assert callable(XHTML_MapElementContent.__init__)


def test_xhtml_mapelementcontent_constructor_args():
    sig = inspect.signature(XHTML_MapElementContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_mapelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_MapElement)


def test_xhtml_mapelement_constructor_exists():
    assert callable(XHTML_MapElement.__init__)


def test_xhtml_mapelement_constructor_args():
    sig = inspect.signature(XHTML_MapElement.__init__)
    params = list(sig.parameters.keys())



def test_mapelement_is_not_abstract():
    assert not inspect.isabstract(MapElement)


def test_mapelement_constructor_exists():
    assert callable(MapElement.__init__)


def test_mapelement_constructor_args():
    sig = inspect.signature(MapElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_mapcontent_is_not_abstract():
    assert not inspect.isabstract(XHTML_MapContent)


def test_xhtml_mapcontent_constructor_exists():
    assert callable(XHTML_MapContent.__init__)


def test_xhtml_mapcontent_constructor_args():
    sig = inspect.signature(XHTML_MapContent.__init__)
    params = list(sig.parameters.keys())



def test_urilist_is_not_abstract():
    assert not inspect.isabstract(UriList)


def test_urilist_constructor_exists():
    assert callable(UriList.__init__)


def test_urilist_constructor_args():
    sig = inspect.signature(UriList.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_objectelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_ObjectElement)


def test_xhtml_objectelement_constructor_exists():
    assert callable(XHTML_ObjectElement.__init__)


def test_xhtml_objectelement_constructor_args():
    sig = inspect.signature(XHTML_ObjectElement.__init__)
    params = list(sig.parameters.keys())



def test_fontstyle_is_not_abstract():
    assert not inspect.isabstract(Fontstyle)


def test_fontstyle_constructor_exists():
    assert callable(Fontstyle.__init__)


def test_fontstyle_constructor_args():
    sig = inspect.signature(Fontstyle.__init__)
    params = list(sig.parameters.keys())



def test_phrase_is_not_abstract():
    assert not inspect.isabstract(Phrase)


def test_phrase_constructor_exists():
    assert callable(Phrase.__init__)


def test_phrase_constructor_args():
    sig = inspect.signature(Phrase.__init__)
    params = list(sig.parameters.keys())



def test_focus_is_not_abstract():
    assert not inspect.isabstract(Focus)


def test_focus_constructor_exists():
    assert callable(Focus.__init__)


def test_focus_constructor_args():
    sig = inspect.signature(Focus.__init__)
    params = list(sig.parameters.keys())



def test_specialpre_is_not_abstract():
    assert not inspect.isabstract(Specialpre)


def test_specialpre_constructor_exists():
    assert callable(Specialpre.__init__)


def test_specialpre_constructor_args():
    sig = inspect.signature(Specialpre.__init__)
    params = list(sig.parameters.keys())



def test_coords_is_not_abstract():
    assert not inspect.isabstract(Coords)


def test_coords_constructor_exists():
    assert callable(Coords.__init__)


def test_coords_constructor_args():
    sig = inspect.signature(Coords.__init__)
    params = list(sig.parameters.keys())



def test_blocktext_is_not_abstract():
    assert not inspect.isabstract(Blocktext)


def test_blocktext_constructor_exists():
    assert callable(Blocktext.__init__)


def test_blocktext_constructor_args():
    sig = inspect.signature(Blocktext.__init__)
    params = list(sig.parameters.keys())



def test_datetime_is_not_abstract():
    assert not inspect.isabstract(Datetime)


def test_datetime_constructor_exists():
    assert callable(Datetime.__init__)


def test_datetime_constructor_args():
    sig = inspect.signature(Datetime.__init__)
    params = list(sig.parameters.keys())



def test_heading_is_not_abstract():
    assert not inspect.isabstract(Heading)


def test_heading_constructor_exists():
    assert callable(Heading.__init__)


def test_heading_constructor_args():
    sig = inspect.signature(Heading.__init__)
    params = list(sig.parameters.keys())



def test_dlelement_is_not_abstract():
    assert not inspect.isabstract(DlElement)


def test_dlelement_constructor_exists():
    assert callable(DlElement.__init__)


def test_dlelement_constructor_args():
    sig = inspect.signature(DlElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_dt_is_not_abstract():
    assert not inspect.isabstract(XHTML_Dt)


def test_xhtml_dt_constructor_exists():
    assert callable(XHTML_Dt.__init__)


def test_xhtml_dt_constructor_args():
    sig = inspect.signature(XHTML_Dt.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_dd_is_not_abstract():
    assert not inspect.isabstract(XHTML_Dd)


def test_xhtml_dd_constructor_exists():
    assert callable(XHTML_Dd.__init__)


def test_xhtml_dd_constructor_args():
    sig = inspect.signature(XHTML_Dd.__init__)
    params = list(sig.parameters.keys())



def test_li_is_not_abstract():
    assert not inspect.isabstract(Li)


def test_li_constructor_exists():
    assert callable(Li.__init__)


def test_li_constructor_args():
    sig = inspect.signature(Li.__init__)
    params = list(sig.parameters.keys())



def test_lists_is_not_abstract():
    assert not inspect.isabstract(Lists)


def test_lists_constructor_exists():
    assert callable(Lists.__init__)


def test_lists_constructor_args():
    sig = inspect.signature(Lists.__init__)
    params = list(sig.parameters.keys())



def test_miscinline_is_not_abstract():
    assert not inspect.isabstract(Miscinline)


def test_miscinline_constructor_exists():
    assert callable(Miscinline.__init__)


def test_miscinline_constructor_args():
    sig = inspect.signature(Miscinline.__init__)
    params = list(sig.parameters.keys())



def test_empty_is_not_abstract():
    assert not inspect.isabstract(EMPTY)


def test_empty_constructor_exists():
    assert callable(EMPTY.__init__)


def test_empty_constructor_args():
    sig = inspect.signature(EMPTY.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_base_is_not_abstract():
    assert not inspect.isabstract(XHTML_Base)


def test_xhtml_base_constructor_exists():
    assert callable(XHTML_Base.__init__)


def test_xhtml_base_constructor_args():
    sig = inspect.signature(XHTML_Base.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_titlebaseheadelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_TitleBaseHeadElement)


def test_xhtml_titlebaseheadelement_constructor_exists():
    assert callable(XHTML_TitleBaseHeadElement.__init__)


def test_xhtml_titlebaseheadelement_constructor_args():
    sig = inspect.signature(XHTML_TitleBaseHeadElement.__init__)
    params = list(sig.parameters.keys())



def test_titlebaseheadelement_is_not_abstract():
    assert not inspect.isabstract(TitleBaseHeadElement)


def test_titlebaseheadelement_constructor_exists():
    assert callable(TitleBaseHeadElement.__init__)


def test_titlebaseheadelement_constructor_args():
    sig = inspect.signature(TitleBaseHeadElement.__init__)
    params = list(sig.parameters.keys())



def test_mediadesc_is_not_abstract():
    assert not inspect.isabstract(MediaDesc)


def test_mediadesc_constructor_exists():
    assert callable(MediaDesc.__init__)


def test_mediadesc_constructor_args():
    sig = inspect.signature(MediaDesc.__init__)
    params = list(sig.parameters.keys())



def test_linktypes_is_not_abstract():
    assert not inspect.isabstract(LinkTypes)


def test_linktypes_constructor_exists():
    assert callable(LinkTypes.__init__)


def test_linktypes_constructor_args():
    sig = inspect.signature(LinkTypes.__init__)
    params = list(sig.parameters.keys())



def test_attrs_is_not_abstract():
    assert not inspect.isabstract(Attrs)


def test_attrs_constructor_exists():
    assert callable(Attrs.__init__)


def test_attrs_constructor_args():
    sig = inspect.signature(Attrs.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_h2_is_not_abstract():
    assert not inspect.isabstract(XHTML_H2)


def test_xhtml_h2_constructor_exists():
    assert callable(XHTML_H2.__init__)


def test_xhtml_h2_constructor_args():
    sig = inspect.signature(XHTML_H2.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_dl_is_not_abstract():
    assert not inspect.isabstract(XHTML_Dl)


def test_xhtml_dl_constructor_exists():
    assert callable(XHTML_Dl.__init__)


def test_xhtml_dl_constructor_args():
    sig = inspect.signature(XHTML_Dl.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_em_is_not_abstract():
    assert not inspect.isabstract(XHTML_Em)


def test_xhtml_em_constructor_exists():
    assert callable(XHTML_Em.__init__)


def test_xhtml_em_constructor_args():
    sig = inspect.signature(XHTML_Em.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_select_is_not_abstract():
    assert not inspect.isabstract(XHTML_Select)


def test_xhtml_select_constructor_exists():
    assert callable(XHTML_Select.__init__)


def test_xhtml_select_constructor_args():
    sig = inspect.signature(XHTML_Select.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_xhtml_select_has_disabled():
    assert hasattr(XHTML_Select, "disabled")
    descriptor = None
    for klass in XHTML_Select.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_select_has_multiple():
    assert hasattr(XHTML_Select, "multiple")
    descriptor = None
    for klass in XHTML_Select.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_h3_is_not_abstract():
    assert not inspect.isabstract(XHTML_H3)


def test_xhtml_h3_constructor_exists():
    assert callable(XHTML_H3.__init__)


def test_xhtml_h3_constructor_args():
    sig = inspect.signature(XHTML_H3.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_area_is_not_abstract():
    assert not inspect.isabstract(XHTML_Area)


def test_xhtml_area_constructor_exists():
    assert callable(XHTML_Area.__init__)


def test_xhtml_area_constructor_args():
    sig = inspect.signature(XHTML_Area.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"
    assert "nohref" in params, "Missing parameter 'nohref'"

def test_xhtml_area_has_shape():
    assert hasattr(XHTML_Area, "shape")
    descriptor = None
    for klass in XHTML_Area.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_area_has_nohref():
    assert hasattr(XHTML_Area, "nohref")
    descriptor = None
    for klass in XHTML_Area.__mro__:
        if "nohref" in klass.__dict__:
            descriptor = klass.__dict__["nohref"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_dlelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_DlElement)


def test_xhtml_dlelement_constructor_exists():
    assert callable(XHTML_DlElement.__init__)


def test_xhtml_dlelement_constructor_args():
    sig = inspect.signature(XHTML_DlElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_h4_is_not_abstract():
    assert not inspect.isabstract(XHTML_H4)


def test_xhtml_h4_constructor_exists():
    assert callable(XHTML_H4.__init__)


def test_xhtml_h4_constructor_args():
    sig = inspect.signature(XHTML_H4.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_tbody_is_not_abstract():
    assert not inspect.isabstract(XHTML_Tbody)


def test_xhtml_tbody_constructor_exists():
    assert callable(XHTML_Tbody.__init__)


def test_xhtml_tbody_constructor_args():
    sig = inspect.signature(XHTML_Tbody.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_acronym_is_not_abstract():
    assert not inspect.isabstract(XHTML_Acronym)


def test_xhtml_acronym_constructor_exists():
    assert callable(XHTML_Acronym.__init__)


def test_xhtml_acronym_constructor_args():
    sig = inspect.signature(XHTML_Acronym.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_dfn_is_not_abstract():
    assert not inspect.isabstract(XHTML_Dfn)


def test_xhtml_dfn_constructor_exists():
    assert callable(XHTML_Dfn.__init__)


def test_xhtml_dfn_constructor_args():
    sig = inspect.signature(XHTML_Dfn.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_thead_is_not_abstract():
    assert not inspect.isabstract(XHTML_Thead)


def test_xhtml_thead_constructor_exists():
    assert callable(XHTML_Thead.__init__)


def test_xhtml_thead_constructor_args():
    sig = inspect.signature(XHTML_Thead.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_pre_is_not_abstract():
    assert not inspect.isabstract(XHTML_Pre)


def test_xhtml_pre_constructor_exists():
    assert callable(XHTML_Pre.__init__)


def test_xhtml_pre_constructor_args():
    sig = inspect.signature(XHTML_Pre.__init__)
    params = list(sig.parameters.keys())
    assert "xml_space" in params, "Missing parameter 'xml_space'"

def test_xhtml_pre_has_xml_space():
    assert hasattr(XHTML_Pre, "xml_space")
    descriptor = None
    for klass in XHTML_Pre.__mro__:
        if "xml_space" in klass.__dict__:
            descriptor = klass.__dict__["xml_space"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_tr_is_not_abstract():
    assert not inspect.isabstract(XHTML_Tr)


def test_xhtml_tr_constructor_exists():
    assert callable(XHTML_Tr.__init__)


def test_xhtml_tr_constructor_args():
    sig = inspect.signature(XHTML_Tr.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_tfoot_is_not_abstract():
    assert not inspect.isabstract(XHTML_Tfoot)


def test_xhtml_tfoot_constructor_exists():
    assert callable(XHTML_Tfoot.__init__)


def test_xhtml_tfoot_constructor_args():
    sig = inspect.signature(XHTML_Tfoot.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_big_is_not_abstract():
    assert not inspect.isabstract(XHTML_Big)


def test_xhtml_big_constructor_exists():
    assert callable(XHTML_Big.__init__)


def test_xhtml_big_constructor_args():
    sig = inspect.signature(XHTML_Big.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_address_is_not_abstract():
    assert not inspect.isabstract(XHTML_Address)


def test_xhtml_address_constructor_exists():
    assert callable(XHTML_Address.__init__)


def test_xhtml_address_constructor_args():
    sig = inspect.signature(XHTML_Address.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_ins_is_not_abstract():
    assert not inspect.isabstract(XHTML_Ins)


def test_xhtml_ins_constructor_exists():
    assert callable(XHTML_Ins.__init__)


def test_xhtml_ins_constructor_args():
    sig = inspect.signature(XHTML_Ins.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_i_is_not_abstract():
    assert not inspect.isabstract(XHTML_I)


def test_xhtml_i_constructor_exists():
    assert callable(XHTML_I.__init__)


def test_xhtml_i_constructor_args():
    sig = inspect.signature(XHTML_I.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_span_is_not_abstract():
    assert not inspect.isabstract(XHTML_Span)


def test_xhtml_span_constructor_exists():
    assert callable(XHTML_Span.__init__)


def test_xhtml_span_constructor_args():
    sig = inspect.signature(XHTML_Span.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_ol_is_not_abstract():
    assert not inspect.isabstract(XHTML_Ol)


def test_xhtml_ol_constructor_exists():
    assert callable(XHTML_Ol.__init__)


def test_xhtml_ol_constructor_args():
    sig = inspect.signature(XHTML_Ol.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_li_is_not_abstract():
    assert not inspect.isabstract(XHTML_Li)


def test_xhtml_li_constructor_exists():
    assert callable(XHTML_Li.__init__)


def test_xhtml_li_constructor_args():
    sig = inspect.signature(XHTML_Li.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_col_is_not_abstract():
    assert not inspect.isabstract(XHTML_Col)


def test_xhtml_col_constructor_exists():
    assert callable(XHTML_Col.__init__)


def test_xhtml_col_constructor_args():
    sig = inspect.signature(XHTML_Col.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_ul_is_not_abstract():
    assert not inspect.isabstract(XHTML_Ul)


def test_xhtml_ul_constructor_exists():
    assert callable(XHTML_Ul.__init__)


def test_xhtml_ul_constructor_args():
    sig = inspect.signature(XHTML_Ul.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_small_is_not_abstract():
    assert not inspect.isabstract(XHTML_Small)


def test_xhtml_small_constructor_exists():
    assert callable(XHTML_Small.__init__)


def test_xhtml_small_constructor_args():
    sig = inspect.signature(XHTML_Small.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_hr_is_not_abstract():
    assert not inspect.isabstract(XHTML_Hr)


def test_xhtml_hr_constructor_exists():
    assert callable(XHTML_Hr.__init__)


def test_xhtml_hr_constructor_args():
    sig = inspect.signature(XHTML_Hr.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_h1_is_not_abstract():
    assert not inspect.isabstract(XHTML_H1)


def test_xhtml_h1_constructor_exists():
    assert callable(XHTML_H1.__init__)


def test_xhtml_h1_constructor_args():
    sig = inspect.signature(XHTML_H1.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_label_is_not_abstract():
    assert not inspect.isabstract(XHTML_Label)


def test_xhtml_label_constructor_exists():
    assert callable(XHTML_Label.__init__)


def test_xhtml_label_constructor_args():
    sig = inspect.signature(XHTML_Label.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_samp_is_not_abstract():
    assert not inspect.isabstract(XHTML_Samp)


def test_xhtml_samp_constructor_exists():
    assert callable(XHTML_Samp.__init__)


def test_xhtml_samp_constructor_args():
    sig = inspect.signature(XHTML_Samp.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_h6_is_not_abstract():
    assert not inspect.isabstract(XHTML_H6)


def test_xhtml_h6_constructor_exists():
    assert callable(XHTML_H6.__init__)


def test_xhtml_h6_constructor_args():
    sig = inspect.signature(XHTML_H6.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_sub_is_not_abstract():
    assert not inspect.isabstract(XHTML_Sub)


def test_xhtml_sub_constructor_exists():
    assert callable(XHTML_Sub.__init__)


def test_xhtml_sub_constructor_args():
    sig = inspect.signature(XHTML_Sub.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_input_is_not_abstract():
    assert not inspect.isabstract(XHTML_Input)


def test_xhtml_input_constructor_exists():
    assert callable(XHTML_Input.__init__)


def test_xhtml_input_constructor_args():
    sig = inspect.signature(XHTML_Input.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "checked" in params, "Missing parameter 'checked'"
    assert "type" in params, "Missing parameter 'type'"
    assert "readonly" in params, "Missing parameter 'readonly'"

def test_xhtml_input_has_disabled():
    assert hasattr(XHTML_Input, "disabled")
    descriptor = None
    for klass in XHTML_Input.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_input_has_checked():
    assert hasattr(XHTML_Input, "checked")
    descriptor = None
    for klass in XHTML_Input.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_input_has_type():
    assert hasattr(XHTML_Input, "type")
    descriptor = None
    for klass in XHTML_Input.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_input_has_readonly():
    assert hasattr(XHTML_Input, "readonly")
    descriptor = None
    for klass in XHTML_Input.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_optgroup_is_not_abstract():
    assert not inspect.isabstract(XHTML_Optgroup)


def test_xhtml_optgroup_constructor_exists():
    assert callable(XHTML_Optgroup.__init__)


def test_xhtml_optgroup_constructor_args():
    sig = inspect.signature(XHTML_Optgroup.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"

def test_xhtml_optgroup_has_disabled():
    assert hasattr(XHTML_Optgroup, "disabled")
    descriptor = None
    for klass in XHTML_Optgroup.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_b_is_not_abstract():
    assert not inspect.isabstract(XHTML_B)


def test_xhtml_b_constructor_exists():
    assert callable(XHTML_B.__init__)


def test_xhtml_b_constructor_args():
    sig = inspect.signature(XHTML_B.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_abbr_is_not_abstract():
    assert not inspect.isabstract(XHTML_Abbr)


def test_xhtml_abbr_constructor_exists():
    assert callable(XHTML_Abbr.__init__)


def test_xhtml_abbr_constructor_args():
    sig = inspect.signature(XHTML_Abbr.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_var_is_not_abstract():
    assert not inspect.isabstract(XHTML_Var)


def test_xhtml_var_constructor_exists():
    assert callable(XHTML_Var.__init__)


def test_xhtml_var_constructor_args():
    sig = inspect.signature(XHTML_Var.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_strong_is_not_abstract():
    assert not inspect.isabstract(XHTML_Strong)


def test_xhtml_strong_constructor_exists():
    assert callable(XHTML_Strong.__init__)


def test_xhtml_strong_constructor_args():
    sig = inspect.signature(XHTML_Strong.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_body_is_not_abstract():
    assert not inspect.isabstract(XHTML_Body)


def test_xhtml_body_constructor_exists():
    assert callable(XHTML_Body.__init__)


def test_xhtml_body_constructor_args():
    sig = inspect.signature(XHTML_Body.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_button_is_not_abstract():
    assert not inspect.isabstract(XHTML_Button)


def test_xhtml_button_constructor_exists():
    assert callable(XHTML_Button.__init__)


def test_xhtml_button_constructor_args():
    sig = inspect.signature(XHTML_Button.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "disabled" in params, "Missing parameter 'disabled'"

def test_xhtml_button_has_type():
    assert hasattr(XHTML_Button, "type")
    descriptor = None
    for klass in XHTML_Button.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_button_has_disabled():
    assert hasattr(XHTML_Button, "disabled")
    descriptor = None
    for klass in XHTML_Button.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_code_is_not_abstract():
    assert not inspect.isabstract(XHTML_Code)


def test_xhtml_code_constructor_exists():
    assert callable(XHTML_Code.__init__)


def test_xhtml_code_constructor_args():
    sig = inspect.signature(XHTML_Code.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_caption_is_not_abstract():
    assert not inspect.isabstract(XHTML_Caption)


def test_xhtml_caption_constructor_exists():
    assert callable(XHTML_Caption.__init__)


def test_xhtml_caption_constructor_args():
    sig = inspect.signature(XHTML_Caption.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_kbd_is_not_abstract():
    assert not inspect.isabstract(XHTML_Kbd)


def test_xhtml_kbd_constructor_exists():
    assert callable(XHTML_Kbd.__init__)


def test_xhtml_kbd_constructor_args():
    sig = inspect.signature(XHTML_Kbd.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_tt_is_not_abstract():
    assert not inspect.isabstract(XHTML_Tt)


def test_xhtml_tt_constructor_exists():
    assert callable(XHTML_Tt.__init__)


def test_xhtml_tt_constructor_args():
    sig = inspect.signature(XHTML_Tt.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_sup_is_not_abstract():
    assert not inspect.isabstract(XHTML_Sup)


def test_xhtml_sup_constructor_exists():
    assert callable(XHTML_Sup.__init__)


def test_xhtml_sup_constructor_args():
    sig = inspect.signature(XHTML_Sup.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_q_is_not_abstract():
    assert not inspect.isabstract(XHTML_Q)


def test_xhtml_q_constructor_exists():
    assert callable(XHTML_Q.__init__)


def test_xhtml_q_constructor_args():
    sig = inspect.signature(XHTML_Q.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_cite_is_not_abstract():
    assert not inspect.isabstract(XHTML_Cite)


def test_xhtml_cite_constructor_exists():
    assert callable(XHTML_Cite.__init__)


def test_xhtml_cite_constructor_args():
    sig = inspect.signature(XHTML_Cite.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_del_is_not_abstract():
    assert not inspect.isabstract(XHTML_Del)


def test_xhtml_del_constructor_exists():
    assert callable(XHTML_Del.__init__)


def test_xhtml_del_constructor_args():
    sig = inspect.signature(XHTML_Del.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_h5_is_not_abstract():
    assert not inspect.isabstract(XHTML_H5)


def test_xhtml_h5_constructor_exists():
    assert callable(XHTML_H5.__init__)


def test_xhtml_h5_constructor_args():
    sig = inspect.signature(XHTML_H5.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_blockquote_is_not_abstract():
    assert not inspect.isabstract(XHTML_Blockquote)


def test_xhtml_blockquote_constructor_exists():
    assert callable(XHTML_Blockquote.__init__)


def test_xhtml_blockquote_constructor_args():
    sig = inspect.signature(XHTML_Blockquote.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_td_is_not_abstract():
    assert not inspect.isabstract(XHTML_Td)


def test_xhtml_td_constructor_exists():
    assert callable(XHTML_Td.__init__)


def test_xhtml_td_constructor_args():
    sig = inspect.signature(XHTML_Td.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_xhtml_td_has_scope():
    assert hasattr(XHTML_Td, "scope")
    descriptor = None
    for klass in XHTML_Td.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_th_is_not_abstract():
    assert not inspect.isabstract(XHTML_Th)


def test_xhtml_th_constructor_exists():
    assert callable(XHTML_Th.__init__)


def test_xhtml_th_constructor_args():
    sig = inspect.signature(XHTML_Th.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_xhtml_th_has_scope():
    assert hasattr(XHTML_Th, "scope")
    descriptor = None
    for klass in XHTML_Th.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_colgroup_is_not_abstract():
    assert not inspect.isabstract(XHTML_Colgroup)


def test_xhtml_colgroup_constructor_exists():
    assert callable(XHTML_Colgroup.__init__)


def test_xhtml_colgroup_constructor_args():
    sig = inspect.signature(XHTML_Colgroup.__init__)
    params = list(sig.parameters.keys())



def test_html_is_not_abstract():
    assert not inspect.isabstract(Html)


def test_html_constructor_exists():
    assert callable(Html.__init__)


def test_html_constructor_args():
    sig = inspect.signature(Html.__init__)
    params = list(sig.parameters.keys())



def test_headelement_is_not_abstract():
    assert not inspect.isabstract(HeadElement)


def test_headelement_constructor_exists():
    assert callable(HeadElement.__init__)


def test_headelement_constructor_args():
    sig = inspect.signature(HeadElement.__init__)
    params = list(sig.parameters.keys())



def test_headmisc_is_not_abstract():
    assert not inspect.isabstract(HeadMisc)


def test_headmisc_constructor_exists():
    assert callable(HeadMisc.__init__)


def test_headmisc_constructor_args():
    sig = inspect.signature(HeadMisc.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_meta_is_not_abstract():
    assert not inspect.isabstract(XHTML_Meta)


def test_xhtml_meta_constructor_exists():
    assert callable(XHTML_Meta.__init__)


def test_xhtml_meta_constructor_args():
    sig = inspect.signature(XHTML_Meta.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_link_is_not_abstract():
    assert not inspect.isabstract(XHTML_Link)


def test_xhtml_link_constructor_exists():
    assert callable(XHTML_Link.__init__)


def test_xhtml_link_constructor_args():
    sig = inspect.signature(XHTML_Link.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_head_is_not_abstract():
    assert not inspect.isabstract(XHTML_Head)


def test_xhtml_head_constructor_exists():
    assert callable(XHTML_Head.__init__)


def test_xhtml_head_constructor_args():
    sig = inspect.signature(XHTML_Head.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_headmisc_is_not_abstract():
    assert not inspect.isabstract(XHTML_HeadMisc)


def test_xhtml_headmisc_constructor_exists():
    assert callable(XHTML_HeadMisc.__init__)


def test_xhtml_headmisc_constructor_args():
    sig = inspect.signature(XHTML_HeadMisc.__init__)
    params = list(sig.parameters.keys())



def test_body_is_not_abstract():
    assert not inspect.isabstract(Body)


def test_body_constructor_exists():
    assert callable(Body.__init__)


def test_body_constructor_args():
    sig = inspect.signature(Body.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_baseheadelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_BaseHeadElement)


def test_xhtml_baseheadelement_constructor_exists():
    assert callable(XHTML_BaseHeadElement.__init__)


def test_xhtml_baseheadelement_constructor_args():
    sig = inspect.signature(XHTML_BaseHeadElement.__init__)
    params = list(sig.parameters.keys())



def test_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_base_constructor_exists():
    assert callable(Base.__init__)


def test_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_basetitleheadelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_BaseTitleHeadElement)


def test_xhtml_basetitleheadelement_constructor_exists():
    assert callable(XHTML_BaseTitleHeadElement.__init__)


def test_xhtml_basetitleheadelement_constructor_args():
    sig = inspect.signature(XHTML_BaseTitleHeadElement.__init__)
    params = list(sig.parameters.keys())



def test_basetitleheadelement_is_not_abstract():
    assert not inspect.isabstract(BaseTitleHeadElement)


def test_basetitleheadelement_constructor_exists():
    assert callable(BaseTitleHeadElement.__init__)


def test_basetitleheadelement_constructor_args():
    sig = inspect.signature(BaseTitleHeadElement.__init__)
    params = list(sig.parameters.keys())



def test_title_is_not_abstract():
    assert not inspect.isabstract(Title)


def test_title_constructor_exists():
    assert callable(Title.__init__)


def test_title_constructor_args():
    sig = inspect.signature(Title.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_titleheadelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_TitleHeadElement)


def test_xhtml_titleheadelement_constructor_exists():
    assert callable(XHTML_TitleHeadElement.__init__)


def test_xhtml_titleheadelement_constructor_args():
    sig = inspect.signature(XHTML_TitleHeadElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_headelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_HeadElement)


def test_xhtml_headelement_constructor_exists():
    assert callable(XHTML_HeadElement.__init__)


def test_xhtml_headelement_constructor_args():
    sig = inspect.signature(XHTML_HeadElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_acontent_is_not_abstract():
    assert not inspect.isabstract(XHTML_AContent)


def test_xhtml_acontent_constructor_exists():
    assert callable(XHTML_AContent.__init__)


def test_xhtml_acontent_constructor_args():
    sig = inspect.signature(XHTML_AContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_flow_is_not_abstract():
    assert not inspect.isabstract(XHTML_Flow)


def test_xhtml_flow_constructor_exists():
    assert callable(XHTML_Flow.__init__)


def test_xhtml_flow_constructor_args():
    sig = inspect.signature(XHTML_Flow.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_block_is_not_abstract():
    assert not inspect.isabstract(XHTML_Block)


def test_xhtml_block_constructor_exists():
    assert callable(XHTML_Block.__init__)


def test_xhtml_block_constructor_args():
    sig = inspect.signature(XHTML_Block.__init__)
    params = list(sig.parameters.keys())



def test_head_is_not_abstract():
    assert not inspect.isabstract(Head)


def test_head_constructor_exists():
    assert callable(Head.__init__)


def test_head_constructor_args():
    sig = inspect.signature(Head.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_html_is_not_abstract():
    assert not inspect.isabstract(XHTML_Html)


def test_xhtml_html_constructor_exists():
    assert callable(XHTML_Html.__init__)


def test_xhtml_html_constructor_args():
    sig = inspect.signature(XHTML_Html.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_buttoncontent_is_not_abstract():
    assert not inspect.isabstract(XHTML_ButtonContent)


def test_xhtml_buttoncontent_constructor_exists():
    assert callable(XHTML_ButtonContent.__init__)


def test_xhtml_buttoncontent_constructor_args():
    sig = inspect.signature(XHTML_ButtonContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_formcontent_is_not_abstract():
    assert not inspect.isabstract(XHTML_FormContent)


def test_xhtml_formcontent_constructor_exists():
    assert callable(XHTML_FormContent.__init__)


def test_xhtml_formcontent_constructor_args():
    sig = inspect.signature(XHTML_FormContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_precontent_is_not_abstract():
    assert not inspect.isabstract(XHTML_PreContent)


def test_xhtml_precontent_constructor_exists():
    assert callable(XHTML_PreContent.__init__)


def test_xhtml_precontent_constructor_args():
    sig = inspect.signature(XHTML_PreContent.__init__)
    params = list(sig.parameters.keys())



def test_acontent_is_not_abstract():
    assert not inspect.isabstract(AContent)


def test_acontent_constructor_exists():
    assert callable(AContent.__init__)


def test_acontent_constructor_args():
    sig = inspect.signature(AContent.__init__)
    params = list(sig.parameters.keys())



def test_buttoncontent_is_not_abstract():
    assert not inspect.isabstract(ButtonContent)


def test_buttoncontent_constructor_exists():
    assert callable(ButtonContent.__init__)


def test_buttoncontent_constructor_args():
    sig = inspect.signature(ButtonContent.__init__)
    params = list(sig.parameters.keys())



def test_inline_is_not_abstract():
    assert not inspect.isabstract(inline)


def test_inline_constructor_exists():
    assert callable(inline.__init__)


def test_inline_constructor_args():
    sig = inspect.signature(inline.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_special_is_not_abstract():
    assert not inspect.isabstract(XHTML_Special)


def test_xhtml_special_constructor_exists():
    assert callable(XHTML_Special.__init__)


def test_xhtml_special_constructor_args():
    sig = inspect.signature(XHTML_Special.__init__)
    params = list(sig.parameters.keys())



def test_precontent_is_not_abstract():
    assert not inspect.isabstract(PreContent)


def test_precontent_constructor_exists():
    assert callable(PreContent.__init__)


def test_precontent_constructor_args():
    sig = inspect.signature(PreContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_phrase_is_not_abstract():
    assert not inspect.isabstract(XHTML_Phrase)


def test_xhtml_phrase_constructor_exists():
    assert callable(XHTML_Phrase.__init__)


def test_xhtml_phrase_constructor_args():
    sig = inspect.signature(XHTML_Phrase.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_fontstyle_is_not_abstract():
    assert not inspect.isabstract(XHTML_Fontstyle)


def test_xhtml_fontstyle_constructor_exists():
    assert callable(XHTML_Fontstyle.__init__)


def test_xhtml_fontstyle_constructor_args():
    sig = inspect.signature(XHTML_Fontstyle.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_a_is_not_abstract():
    assert not inspect.isabstract(XHTML_A)


def test_xhtml_a_constructor_exists():
    assert callable(XHTML_A.__init__)


def test_xhtml_a_constructor_args():
    sig = inspect.signature(XHTML_A.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_xhtml_a_has_shape():
    assert hasattr(XHTML_A, "shape")
    descriptor = None
    for klass in XHTML_A.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_special_is_not_abstract():
    assert not inspect.isabstract(Special)


def test_special_constructor_exists():
    assert callable(Special.__init__)


def test_special_constructor_args():
    sig = inspect.signature(Special.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_img_is_not_abstract():
    assert not inspect.isabstract(XHTML_Img)


def test_xhtml_img_constructor_exists():
    assert callable(XHTML_Img.__init__)


def test_xhtml_img_constructor_args():
    sig = inspect.signature(XHTML_Img.__init__)
    params = list(sig.parameters.keys())
    assert "ismap" in params, "Missing parameter 'ismap'"

def test_xhtml_img_has_ismap():
    assert hasattr(XHTML_Img, "ismap")
    descriptor = None
    for klass in XHTML_Img.__mro__:
        if "ismap" in klass.__dict__:
            descriptor = klass.__dict__["ismap"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_object_is_not_abstract():
    assert not inspect.isabstract(XHTML_Object)


def test_xhtml_object_constructor_exists():
    assert callable(XHTML_Object.__init__)


def test_xhtml_object_constructor_args():
    sig = inspect.signature(XHTML_Object.__init__)
    params = list(sig.parameters.keys())
    assert "declare" in params, "Missing parameter 'declare'"

def test_xhtml_object_has_declare():
    assert hasattr(XHTML_Object, "declare")
    descriptor = None
    for klass in XHTML_Object.__mro__:
        if "declare" in klass.__dict__:
            descriptor = klass.__dict__["declare"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_specialpre_is_not_abstract():
    assert not inspect.isabstract(XHTML_Specialpre)


def test_xhtml_specialpre_constructor_exists():
    assert callable(XHTML_Specialpre.__init__)


def test_xhtml_specialpre_constructor_args():
    sig = inspect.signature(XHTML_Specialpre.__init__)
    params = list(sig.parameters.keys())



def test_number_is_not_abstract():
    assert not inspect.isabstract(Number)


def test_number_constructor_exists():
    assert callable(Number.__init__)


def test_number_constructor_args():
    sig = inspect.signature(Number.__init__)
    params = list(sig.parameters.keys())



def test_character_is_not_abstract():
    assert not inspect.isabstract(Character)


def test_character_constructor_exists():
    assert callable(Character.__init__)


def test_character_constructor_args():
    sig = inspect.signature(Character.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_focus_is_not_abstract():
    assert not inspect.isabstract(XHTML_Focus)


def test_xhtml_focus_constructor_exists():
    assert callable(XHTML_Focus.__init__)


def test_xhtml_focus_constructor_args():
    sig = inspect.signature(XHTML_Focus.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(block)


def test_block_constructor_exists():
    assert callable(block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(block.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_fieldset_is_not_abstract():
    assert not inspect.isabstract(XHTML_Fieldset)


def test_xhtml_fieldset_constructor_exists():
    assert callable(XHTML_Fieldset.__init__)


def test_xhtml_fieldset_constructor_args():
    sig = inspect.signature(XHTML_Fieldset.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_lists_is_not_abstract():
    assert not inspect.isabstract(XHTML_Lists)


def test_xhtml_lists_constructor_exists():
    assert callable(XHTML_Lists.__init__)


def test_xhtml_lists_constructor_args():
    sig = inspect.signature(XHTML_Lists.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_blocktext_is_not_abstract():
    assert not inspect.isabstract(XHTML_Blocktext)


def test_xhtml_blocktext_constructor_exists():
    assert callable(XHTML_Blocktext.__init__)


def test_xhtml_blocktext_constructor_args():
    sig = inspect.signature(XHTML_Blocktext.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_p_is_not_abstract():
    assert not inspect.isabstract(XHTML_P)


def test_xhtml_p_constructor_exists():
    assert callable(XHTML_P.__init__)


def test_xhtml_p_constructor_args():
    sig = inspect.signature(XHTML_P.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_div_is_not_abstract():
    assert not inspect.isabstract(XHTML_Div)


def test_xhtml_div_constructor_exists():
    assert callable(XHTML_Div.__init__)


def test_xhtml_div_constructor_args():
    sig = inspect.signature(XHTML_Div.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_table_is_not_abstract():
    assert not inspect.isabstract(XHTML_Table)


def test_xhtml_table_constructor_exists():
    assert callable(XHTML_Table.__init__)


def test_xhtml_table_constructor_args():
    sig = inspect.signature(XHTML_Table.__init__)
    params = list(sig.parameters.keys())
    assert "frame" in params, "Missing parameter 'frame'"
    assert "rules" in params, "Missing parameter 'rules'"

def test_xhtml_table_has_frame():
    assert hasattr(XHTML_Table, "frame")
    descriptor = None
    for klass in XHTML_Table.__mro__:
        if "frame" in klass.__dict__:
            descriptor = klass.__dict__["frame"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_table_has_rules():
    assert hasattr(XHTML_Table, "rules")
    descriptor = None
    for klass in XHTML_Table.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_heading_is_not_abstract():
    assert not inspect.isabstract(XHTML_Heading)


def test_xhtml_heading_constructor_exists():
    assert callable(XHTML_Heading.__init__)


def test_xhtml_heading_constructor_args():
    sig = inspect.signature(XHTML_Heading.__init__)
    params = list(sig.parameters.keys())



def test_pcdata_is_not_abstract():
    assert not inspect.isabstract(PCDATA)


def test_pcdata_constructor_exists():
    assert callable(PCDATA.__init__)


def test_pcdata_constructor_args():
    sig = inspect.signature(PCDATA.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_style_is_not_abstract():
    assert not inspect.isabstract(XHTML_Style)


def test_xhtml_style_constructor_exists():
    assert callable(XHTML_Style.__init__)


def test_xhtml_style_constructor_args():
    sig = inspect.signature(XHTML_Style.__init__)
    params = list(sig.parameters.keys())
    assert "xml_space" in params, "Missing parameter 'xml_space'"

def test_xhtml_style_has_xml_space():
    assert hasattr(XHTML_Style, "xml_space")
    descriptor = None
    for klass in XHTML_Style.__mro__:
        if "xml_space" in klass.__dict__:
            descriptor = klass.__dict__["xml_space"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_script_is_not_abstract():
    assert not inspect.isabstract(XHTML_Script)


def test_xhtml_script_constructor_exists():
    assert callable(XHTML_Script.__init__)


def test_xhtml_script_constructor_args():
    sig = inspect.signature(XHTML_Script.__init__)
    params = list(sig.parameters.keys())
    assert "defer" in params, "Missing parameter 'defer'"
    assert "xml_space" in params, "Missing parameter 'xml_space'"

def test_xhtml_script_has_defer():
    assert hasattr(XHTML_Script, "defer")
    descriptor = None
    for klass in XHTML_Script.__mro__:
        if "defer" in klass.__dict__:
            descriptor = klass.__dict__["defer"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_script_has_xml_space():
    assert hasattr(XHTML_Script, "xml_space")
    descriptor = None
    for klass in XHTML_Script.__mro__:
        if "xml_space" in klass.__dict__:
            descriptor = klass.__dict__["xml_space"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_textarea_is_not_abstract():
    assert not inspect.isabstract(XHTML_Textarea)


def test_xhtml_textarea_constructor_exists():
    assert callable(XHTML_Textarea.__init__)


def test_xhtml_textarea_constructor_args():
    sig = inspect.signature(XHTML_Textarea.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "readonly" in params, "Missing parameter 'readonly'"

def test_xhtml_textarea_has_disabled():
    assert hasattr(XHTML_Textarea, "disabled")
    descriptor = None
    for klass in XHTML_Textarea.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_textarea_has_readonly():
    assert hasattr(XHTML_Textarea, "readonly")
    descriptor = None
    for klass in XHTML_Textarea.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_option_is_not_abstract():
    assert not inspect.isabstract(XHTML_Option)


def test_xhtml_option_constructor_exists():
    assert callable(XHTML_Option.__init__)


def test_xhtml_option_constructor_args():
    sig = inspect.signature(XHTML_Option.__init__)
    params = list(sig.parameters.keys())
    assert "selected" in params, "Missing parameter 'selected'"
    assert "disabled" in params, "Missing parameter 'disabled'"

def test_xhtml_option_has_selected():
    assert hasattr(XHTML_Option, "selected")
    descriptor = None
    for klass in XHTML_Option.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_xhtml_option_has_disabled():
    assert hasattr(XHTML_Option, "disabled")
    descriptor = None
    for klass in XHTML_Option.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_title_is_not_abstract():
    assert not inspect.isabstract(XHTML_Title)


def test_xhtml_title_constructor_exists():
    assert callable(XHTML_Title.__init__)


def test_xhtml_title_constructor_args():
    sig = inspect.signature(XHTML_Title.__init__)
    params = list(sig.parameters.keys())



def test_fieldsetelement_is_not_abstract():
    assert not inspect.isabstract(FieldsetElement)


def test_fieldsetelement_constructor_exists():
    assert callable(FieldsetElement.__init__)


def test_fieldsetelement_constructor_args():
    sig = inspect.signature(FieldsetElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_legend_is_not_abstract():
    assert not inspect.isabstract(XHTML_Legend)


def test_xhtml_legend_constructor_exists():
    assert callable(XHTML_Legend.__init__)


def test_xhtml_legend_constructor_args():
    sig = inspect.signature(XHTML_Legend.__init__)
    params = list(sig.parameters.keys())



def test_mapelementcontent_is_not_abstract():
    assert not inspect.isabstract(MapElementContent)


def test_mapelementcontent_constructor_exists():
    assert callable(MapElementContent.__init__)


def test_mapelementcontent_constructor_args():
    sig = inspect.signature(MapElementContent.__init__)
    params = list(sig.parameters.keys())



def test_objectelement_is_not_abstract():
    assert not inspect.isabstract(ObjectElement)


def test_objectelement_constructor_exists():
    assert callable(ObjectElement.__init__)


def test_objectelement_constructor_args():
    sig = inspect.signature(ObjectElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_param_is_not_abstract():
    assert not inspect.isabstract(XHTML_Param)


def test_xhtml_param_constructor_exists():
    assert callable(XHTML_Param.__init__)


def test_xhtml_param_constructor_args():
    sig = inspect.signature(XHTML_Param.__init__)
    params = list(sig.parameters.keys())
    assert "valuetype" in params, "Missing parameter 'valuetype'"

def test_xhtml_param_has_valuetype():
    assert hasattr(XHTML_Param, "valuetype")
    descriptor = None
    for klass in XHTML_Param.__mro__:
        if "valuetype" in klass.__dict__:
            descriptor = klass.__dict__["valuetype"]
            break
    assert isinstance(descriptor, property)



def test_formcontent_is_not_abstract():
    assert not inspect.isabstract(FormContent)


def test_formcontent_constructor_exists():
    assert callable(FormContent.__init__)


def test_formcontent_constructor_args():
    sig = inspect.signature(FormContent.__init__)
    params = list(sig.parameters.keys())



def test_flow_is_not_abstract():
    assert not inspect.isabstract(Flow)


def test_flow_constructor_exists():
    assert callable(Flow.__init__)


def test_flow_constructor_args():
    sig = inspect.signature(Flow.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_inline_is_not_abstract():
    assert not inspect.isabstract(XHTML_Inline)


def test_xhtml_inline_constructor_exists():
    assert callable(XHTML_Inline.__init__)


def test_xhtml_inline_constructor_args():
    sig = inspect.signature(XHTML_Inline.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_block_is_not_abstract():
    assert not inspect.isabstract(XHTML_block)


def test_xhtml_block_constructor_exists():
    assert callable(XHTML_block.__init__)


def test_xhtml_block_constructor_args():
    sig = inspect.signature(XHTML_block.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_form_is_not_abstract():
    assert not inspect.isabstract(XHTML_Form)


def test_xhtml_form_constructor_exists():
    assert callable(XHTML_Form.__init__)


def test_xhtml_form_constructor_args():
    sig = inspect.signature(XHTML_Form.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"

def test_xhtml_form_has_method():
    assert hasattr(XHTML_Form, "method")
    descriptor = None
    for klass in XHTML_Form.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_misc_is_not_abstract():
    assert not inspect.isabstract(XHTML_Misc)


def test_xhtml_misc_constructor_exists():
    assert callable(XHTML_Misc.__init__)


def test_xhtml_misc_constructor_args():
    sig = inspect.signature(XHTML_Misc.__init__)
    params = list(sig.parameters.keys())



def test_inline_is_not_abstract():
    assert not inspect.isabstract(Inline)


def test_inline_constructor_exists():
    assert callable(Inline.__init__)


def test_inline_constructor_args():
    sig = inspect.signature(Inline.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_inline_is_not_abstract():
    assert not inspect.isabstract(XHTML_inline)


def test_xhtml_inline_constructor_exists():
    assert callable(XHTML_inline.__init__)


def test_xhtml_inline_constructor_args():
    sig = inspect.signature(XHTML_inline.__init__)
    params = list(sig.parameters.keys())



def test_misc_is_not_abstract():
    assert not inspect.isabstract(Misc)


def test_misc_constructor_exists():
    assert callable(Misc.__init__)


def test_misc_constructor_args():
    sig = inspect.signature(Misc.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_noscript_is_not_abstract():
    assert not inspect.isabstract(XHTML_Noscript)


def test_xhtml_noscript_constructor_exists():
    assert callable(XHTML_Noscript.__init__)


def test_xhtml_noscript_constructor_args():
    sig = inspect.signature(XHTML_Noscript.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_miscinline_is_not_abstract():
    assert not inspect.isabstract(XHTML_Miscinline)


def test_xhtml_miscinline_constructor_exists():
    assert callable(XHTML_Miscinline.__init__)


def test_xhtml_miscinline_constructor_args():
    sig = inspect.signature(XHTML_Miscinline.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_inlineforms_is_not_abstract():
    assert not inspect.isabstract(XHTML_Inlineforms)


def test_xhtml_inlineforms_constructor_exists():
    assert callable(XHTML_Inlineforms.__init__)


def test_xhtml_inlineforms_constructor_args():
    sig = inspect.signature(XHTML_Inlineforms.__init__)
    params = list(sig.parameters.keys())



def test_scriptexpression_is_not_abstract():
    assert not inspect.isabstract(ScriptExpression)


def test_scriptexpression_constructor_exists():
    assert callable(ScriptExpression.__init__)


def test_scriptexpression_constructor_args():
    sig = inspect.signature(ScriptExpression.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_events_is_not_abstract():
    assert not inspect.isabstract(XHTML_Events)


def test_xhtml_events_constructor_exists():
    assert callable(XHTML_Events.__init__)


def test_xhtml_events_constructor_args():
    sig = inspect.signature(XHTML_Events.__init__)
    params = list(sig.parameters.keys())



def test_languagecode_is_not_abstract():
    assert not inspect.isabstract(LanguageCode)


def test_languagecode_constructor_exists():
    assert callable(LanguageCode.__init__)


def test_languagecode_constructor_args():
    sig = inspect.signature(LanguageCode.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_i18n_is_not_abstract():
    assert not inspect.isabstract(XHTML_I18n)


def test_xhtml_i18n_constructor_exists():
    assert callable(XHTML_I18n.__init__)


def test_xhtml_i18n_constructor_args():
    sig = inspect.signature(XHTML_I18n.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_xhtml_i18n_has_dir():
    assert hasattr(XHTML_I18n, "dir")
    descriptor = None
    for klass in XHTML_I18n.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_events_is_not_abstract():
    assert not inspect.isabstract(Events)


def test_events_constructor_exists():
    assert callable(Events.__init__)


def test_events_constructor_args():
    sig = inspect.signature(Events.__init__)
    params = list(sig.parameters.keys())



def test_i18n_is_not_abstract():
    assert not inspect.isabstract(I18n)


def test_i18n_constructor_exists():
    assert callable(I18n.__init__)


def test_i18n_constructor_args():
    sig = inspect.signature(I18n.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_map_is_not_abstract():
    assert not inspect.isabstract(XHTML_Map)


def test_xhtml_map_constructor_exists():
    assert callable(XHTML_Map.__init__)


def test_xhtml_map_constructor_args():
    sig = inspect.signature(XHTML_Map.__init__)
    params = list(sig.parameters.keys())



def test_coreattrs_is_not_abstract():
    assert not inspect.isabstract(CoreAttrs)


def test_coreattrs_constructor_exists():
    assert callable(CoreAttrs.__init__)


def test_coreattrs_constructor_args():
    sig = inspect.signature(CoreAttrs.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_br_is_not_abstract():
    assert not inspect.isabstract(XHTML_Br)


def test_xhtml_br_constructor_exists():
    assert callable(XHTML_Br.__init__)


def test_xhtml_br_constructor_args():
    sig = inspect.signature(XHTML_Br.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_bdo_is_not_abstract():
    assert not inspect.isabstract(XHTML_Bdo)


def test_xhtml_bdo_constructor_exists():
    assert callable(XHTML_Bdo.__init__)


def test_xhtml_bdo_constructor_args():
    sig = inspect.signature(XHTML_Bdo.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_xhtml_bdo_has_dir():
    assert hasattr(XHTML_Bdo, "dir")
    descriptor = None
    for klass in XHTML_Bdo.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_xhtml_attrs_is_not_abstract():
    assert not inspect.isabstract(XHTML_Attrs)


def test_xhtml_attrs_constructor_exists():
    assert callable(XHTML_Attrs.__init__)


def test_xhtml_attrs_constructor_args():
    sig = inspect.signature(XHTML_Attrs.__init__)
    params = list(sig.parameters.keys())



def test_uri_is_not_abstract():
    assert not inspect.isabstract(URI)


def test_uri_constructor_exists():
    assert callable(URI.__init__)


def test_uri_constructor_args():
    sig = inspect.signature(URI.__init__)
    params = list(sig.parameters.keys())



def test_text_is_not_abstract():
    assert not inspect.isabstract(Text)


def test_text_constructor_exists():
    assert callable(Text.__init__)


def test_text_constructor_args():
    sig = inspect.signature(Text.__init__)
    params = list(sig.parameters.keys())



def test_stylesheet_is_not_abstract():
    assert not inspect.isabstract(StyleSheet)


def test_stylesheet_constructor_exists():
    assert callable(StyleSheet.__init__)


def test_stylesheet_constructor_args():
    sig = inspect.signature(StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_id_is_not_abstract():
    assert not inspect.isabstract(ID)


def test_id_constructor_exists():
    assert callable(ID.__init__)


def test_id_constructor_args():
    sig = inspect.signature(ID.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_coreattrs_is_not_abstract():
    assert not inspect.isabstract(XHTML_CoreAttrs)


def test_xhtml_coreattrs_constructor_exists():
    assert callable(XHTML_CoreAttrs.__init__)


def test_xhtml_coreattrs_constructor_args():
    sig = inspect.signature(XHTML_CoreAttrs.__init__)
    params = list(sig.parameters.keys())



def test_length_is_not_abstract():
    assert not inspect.isabstract(Length)


def test_length_constructor_exists():
    assert callable(Length.__init__)


def test_length_constructor_args():
    sig = inspect.signature(Length.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_coords_is_not_abstract():
    assert not inspect.isabstract(XHTML_Coords)


def test_xhtml_coords_constructor_exists():
    assert callable(XHTML_Coords.__init__)


def test_xhtml_coords_constructor_args():
    sig = inspect.signature(XHTML_Coords.__init__)
    params = list(sig.parameters.keys())



def test_contenttype_is_not_abstract():
    assert not inspect.isabstract(ContentType)


def test_contenttype_constructor_exists():
    assert callable(ContentType.__init__)


def test_contenttype_constructor_args():
    sig = inspect.signature(ContentType.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_contenttypes_is_not_abstract():
    assert not inspect.isabstract(XHTML_ContentTypes)


def test_xhtml_contenttypes_constructor_exists():
    assert callable(XHTML_ContentTypes.__init__)


def test_xhtml_contenttypes_constructor_args():
    sig = inspect.signature(XHTML_ContentTypes.__init__)
    params = list(sig.parameters.keys())



def test_cdata_is_not_abstract():
    assert not inspect.isabstract(CDATA)


def test_cdata_constructor_exists():
    assert callable(CDATA.__init__)


def test_cdata_constructor_args():
    sig = inspect.signature(CDATA.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_datetime_is_not_abstract():
    assert not inspect.isabstract(XHTML_Datetime)


def test_xhtml_datetime_constructor_exists():
    assert callable(XHTML_Datetime.__init__)


def test_xhtml_datetime_constructor_args():
    sig = inspect.signature(XHTML_Datetime.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_stylesheet_is_not_abstract():
    assert not inspect.isabstract(XHTML_StyleSheet)


def test_xhtml_stylesheet_constructor_exists():
    assert callable(XHTML_StyleSheet.__init__)


def test_xhtml_stylesheet_constructor_args():
    sig = inspect.signature(XHTML_StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_length_is_not_abstract():
    assert not inspect.isabstract(XHTML_Length)


def test_xhtml_length_constructor_exists():
    assert callable(XHTML_Length.__init__)


def test_xhtml_length_constructor_args():
    sig = inspect.signature(XHTML_Length.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_pixels_is_not_abstract():
    assert not inspect.isabstract(XHTML_Pixels)


def test_xhtml_pixels_constructor_exists():
    assert callable(XHTML_Pixels.__init__)


def test_xhtml_pixels_constructor_args():
    sig = inspect.signature(XHTML_Pixels.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_multilength_is_not_abstract():
    assert not inspect.isabstract(XHTML_MultiLength)


def test_xhtml_multilength_constructor_exists():
    assert callable(XHTML_MultiLength.__init__)


def test_xhtml_multilength_constructor_args():
    sig = inspect.signature(XHTML_MultiLength.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_scriptexpression_is_not_abstract():
    assert not inspect.isabstract(XHTML_ScriptExpression)


def test_xhtml_scriptexpression_constructor_exists():
    assert callable(XHTML_ScriptExpression.__init__)


def test_xhtml_scriptexpression_constructor_args():
    sig = inspect.signature(XHTML_ScriptExpression.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_text_is_not_abstract():
    assert not inspect.isabstract(XHTML_Text)


def test_xhtml_text_constructor_exists():
    assert callable(XHTML_Text.__init__)


def test_xhtml_text_constructor_args():
    sig = inspect.signature(XHTML_Text.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_contenttype_is_not_abstract():
    assert not inspect.isabstract(XHTML_ContentType)


def test_xhtml_contenttype_constructor_exists():
    assert callable(XHTML_ContentType.__init__)


def test_xhtml_contenttype_constructor_args():
    sig = inspect.signature(XHTML_ContentType.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_empty_is_not_abstract():
    assert not inspect.isabstract(XHTML_EMPTY)


def test_xhtml_empty_constructor_exists():
    assert callable(XHTML_EMPTY.__init__)


def test_xhtml_empty_constructor_args():
    sig = inspect.signature(XHTML_EMPTY.__init__)
    params = list(sig.parameters.keys())



def test_idref_is_not_abstract():
    assert not inspect.isabstract(IDREF)


def test_idref_constructor_exists():
    assert callable(IDREF.__init__)


def test_idref_constructor_args():
    sig = inspect.signature(IDREF.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_idrefs_is_not_abstract():
    assert not inspect.isabstract(XHTML_IDREFS)


def test_xhtml_idrefs_constructor_exists():
    assert callable(XHTML_IDREFS.__init__)


def test_xhtml_idrefs_constructor_args():
    sig = inspect.signature(XHTML_IDREFS.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_urilist_is_not_abstract():
    assert not inspect.isabstract(XHTML_UriList)


def test_xhtml_urilist_constructor_exists():
    assert callable(XHTML_UriList.__init__)


def test_xhtml_urilist_constructor_args():
    sig = inspect.signature(XHTML_UriList.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_uri_is_not_abstract():
    assert not inspect.isabstract(XHTML_URI)


def test_xhtml_uri_constructor_exists():
    assert callable(XHTML_URI.__init__)


def test_xhtml_uri_constructor_args():
    sig = inspect.signature(XHTML_URI.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_mediadesc_is_not_abstract():
    assert not inspect.isabstract(XHTML_MediaDesc)


def test_xhtml_mediadesc_constructor_exists():
    assert callable(XHTML_MediaDesc.__init__)


def test_xhtml_mediadesc_constructor_args():
    sig = inspect.signature(XHTML_MediaDesc.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_linktypes_is_not_abstract():
    assert not inspect.isabstract(XHTML_LinkTypes)


def test_xhtml_linktypes_constructor_exists():
    assert callable(XHTML_LinkTypes.__init__)


def test_xhtml_linktypes_constructor_args():
    sig = inspect.signature(XHTML_LinkTypes.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_number_is_not_abstract():
    assert not inspect.isabstract(XHTML_Number)


def test_xhtml_number_constructor_exists():
    assert callable(XHTML_Number.__init__)


def test_xhtml_number_constructor_args():
    sig = inspect.signature(XHTML_Number.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_character_is_not_abstract():
    assert not inspect.isabstract(XHTML_Character)


def test_xhtml_character_constructor_exists():
    assert callable(XHTML_Character.__init__)


def test_xhtml_character_constructor_args():
    sig = inspect.signature(XHTML_Character.__init__)
    params = list(sig.parameters.keys())



def test_nmtoken_is_not_abstract():
    assert not inspect.isabstract(NMTOKEN)


def test_nmtoken_constructor_exists():
    assert callable(NMTOKEN.__init__)


def test_nmtoken_constructor_args():
    sig = inspect.signature(NMTOKEN.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_languagecode_is_not_abstract():
    assert not inspect.isabstract(XHTML_LanguageCode)


def test_xhtml_languagecode_constructor_exists():
    assert callable(XHTML_LanguageCode.__init__)


def test_xhtml_languagecode_constructor_args():
    sig = inspect.signature(XHTML_LanguageCode.__init__)
    params = list(sig.parameters.keys())



def test_charset_is_not_abstract():
    assert not inspect.isabstract(Charset)


def test_charset_constructor_exists():
    assert callable(Charset.__init__)


def test_charset_constructor_args():
    sig = inspect.signature(Charset.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_charsets_is_not_abstract():
    assert not inspect.isabstract(XHTML_Charsets)


def test_xhtml_charsets_constructor_exists():
    assert callable(XHTML_Charsets.__init__)


def test_xhtml_charsets_constructor_args():
    sig = inspect.signature(XHTML_Charsets.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_charset_is_not_abstract():
    assert not inspect.isabstract(XHTML_Charset)


def test_xhtml_charset_constructor_exists():
    assert callable(XHTML_Charset.__init__)


def test_xhtml_charset_constructor_args():
    sig = inspect.signature(XHTML_Charset.__init__)
    params = list(sig.parameters.keys())



def test_valuedelement_is_not_abstract():
    assert not inspect.isabstract(ValuedElement)


def test_valuedelement_constructor_exists():
    assert callable(ValuedElement.__init__)


def test_valuedelement_constructor_args():
    sig = inspect.signature(ValuedElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_idref_is_not_abstract():
    assert not inspect.isabstract(XHTML_IDREF)


def test_xhtml_idref_constructor_exists():
    assert callable(XHTML_IDREF.__init__)


def test_xhtml_idref_constructor_args():
    sig = inspect.signature(XHTML_IDREF.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_nmtoken_is_not_abstract():
    assert not inspect.isabstract(XHTML_NMTOKEN)


def test_xhtml_nmtoken_constructor_exists():
    assert callable(XHTML_NMTOKEN.__init__)


def test_xhtml_nmtoken_constructor_args():
    sig = inspect.signature(XHTML_NMTOKEN.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_id_is_not_abstract():
    assert not inspect.isabstract(XHTML_ID)


def test_xhtml_id_constructor_exists():
    assert callable(XHTML_ID.__init__)


def test_xhtml_id_constructor_args():
    sig = inspect.signature(XHTML_ID.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_pcdata_is_not_abstract():
    assert not inspect.isabstract(XHTML_PCDATA)


def test_xhtml_pcdata_constructor_exists():
    assert callable(XHTML_PCDATA.__init__)


def test_xhtml_pcdata_constructor_args():
    sig = inspect.signature(XHTML_PCDATA.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_cdata_is_not_abstract():
    assert not inspect.isabstract(XHTML_CDATA)


def test_xhtml_cdata_constructor_exists():
    assert callable(XHTML_CDATA.__init__)


def test_xhtml_cdata_constructor_args():
    sig = inspect.signature(XHTML_CDATA.__init__)
    params = list(sig.parameters.keys())



def test_xhtml_valuedelement_is_not_abstract():
    assert not inspect.isabstract(XHTML_ValuedElement)


def test_xhtml_valuedelement_constructor_exists():
    assert callable(XHTML_ValuedElement.__init__)


def test_xhtml_valuedelement_constructor_args():
    sig = inspect.signature(XHTML_ValuedElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xhtml_valuedelement_has_value():
    assert hasattr(XHTML_ValuedElement, "value")
    descriptor = None
    for klass in XHTML_ValuedElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_cellhalign_exists():
    # Check that the Enumeration exists
    assert CellHAlign is not None

def test_cellhalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CellHAlign]
    expected_literals = [
        "char",
        "left",
        "center",
        "right",
        "justify",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CellHAlign"

def test_trules_exists():
    # Check that the Enumeration exists
    assert TRules is not None

def test_trules_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TRules]
    expected_literals = [
        "none",
        "rows",
        "groups",
        "all",
        "cols",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TRules"

def test_cellvalign_exists():
    # Check that the Enumeration exists
    assert CellVAlign is not None

def test_cellvalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CellVAlign]
    expected_literals = [
        "top",
        "middle",
        "baseline",
        "bottom",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CellVAlign"

def test_shape_exists():
    # Check that the Enumeration exists
    assert Shape is not None

def test_shape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Shape]
    expected_literals = [
        "default",
        "poly",
        "circle",
        "rect",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Shape"

def test_inputtype_exists():
    # Check that the Enumeration exists
    assert InputType is not None

def test_inputtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InputType]
    expected_literals = [
        "image",
        "reset",
        "password",
        "hidden",
        "button",
        "file",
        "submit",
        "radio",
        "checkbox",
        "text",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InputType"

def test_buttontype_exists():
    # Check that the Enumeration exists
    assert ButtonType is not None

def test_buttontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ButtonType]
    expected_literals = [
        "reset",
        "button",
        "submit",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ButtonType"

def test_tframe_exists():
    # Check that the Enumeration exists
    assert TFrame is not None

def test_tframe_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TFrame]
    expected_literals = [
        "lhs",
        "below",
        "rhs",
        "above",
        "void",
        "box",
        "border",
        "vsides",
        "hsides",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TFrame"

def test_valuetype_exists():
    # Check that the Enumeration exists
    assert ValueType is not None

def test_valuetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueType]
    expected_literals = [
        "data",
        "object",
        "ref",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueType"

def test_scope_exists():
    # Check that the Enumeration exists
    assert Scope is not None

def test_scope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Scope]
    expected_literals = [
        "colgroup",
        "col",
        "rowgroup",
        "row",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Scope"

def test_fomemethod_exists():
    # Check that the Enumeration exists
    assert FomeMethod is not None

def test_fomemethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FomeMethod]
    expected_literals = [
        "post",
        "get",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FomeMethod"

def test_direction_exists():
    # Check that the Enumeration exists
    assert Direction is not None

def test_direction_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Direction]
    expected_literals = [
        "rtl",
        "ltr",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"


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
IDREFS_strategy = st.builds(
    IDREFS,
)
XHTML_TrElement_strategy = st.builds(
    XHTML_TrElement,
)
TrElement_strategy = st.builds(
    TrElement,
)
MultiLength_strategy = st.builds(
    MultiLength,
)
Tr_strategy = st.builds(
    Tr,
)
Cellvalign_strategy = st.builds(
    Cellvalign,
)
Cellhalign_strategy = st.builds(
    Cellhalign,
)
Col_strategy = st.builds(
    Col,
)
XHTML_ColElement_strategy = st.builds(
    XHTML_ColElement,
)
Tbody_strategy = st.builds(
    Tbody,
)
XHTML_TableElement_strategy = st.builds(
    XHTML_TableElement,
)
Pixels_strategy = st.builds(
    Pixels,
)
Colgroup_strategy = st.builds(
    Colgroup,
)
TableElement_strategy = st.builds(
    TableElement,
)
Tfoot_strategy = st.builds(
    Tfoot,
)
Thead_strategy = st.builds(
    Thead,
)
ColElement_strategy = st.builds(
    ColElement,
)
Caption_strategy = st.builds(
    Caption,
)
XHTML_Cellvalign_strategy = st.builds(
    XHTML_Cellvalign,
    valign=
        safe_text
)
XHTML_Cellhalign_strategy = st.builds(
    XHTML_Cellhalign,
    align=
        safe_text
)
XHTML_FieldsetElement_strategy = st.builds(
    XHTML_FieldsetElement,
)
XHTML_SelectElement_strategy = st.builds(
    XHTML_SelectElement,
)
Option_strategy = st.builds(
    Option,
)
SelectElement_strategy = st.builds(
    SelectElement,
)
Inlineforms_strategy = st.builds(
    Inlineforms,
)
Charsets_strategy = st.builds(
    Charsets,
)
ContentTypes_strategy = st.builds(
    ContentTypes,
)
MapContent_strategy = st.builds(
    MapContent,
)
XHTML_MapElementContent_strategy = st.builds(
    XHTML_MapElementContent,
)
XHTML_MapElement_strategy = st.builds(
    XHTML_MapElement,
)
MapElement_strategy = st.builds(
    MapElement,
)
XHTML_MapContent_strategy = st.builds(
    XHTML_MapContent,
)
UriList_strategy = st.builds(
    UriList,
)
XHTML_ObjectElement_strategy = st.builds(
    XHTML_ObjectElement,
)
Fontstyle_strategy = st.builds(
    Fontstyle,
)
Phrase_strategy = st.builds(
    Phrase,
)
Focus_strategy = st.builds(
    Focus,
)
Specialpre_strategy = st.builds(
    Specialpre,
)
Coords_strategy = st.builds(
    Coords,
)
Blocktext_strategy = st.builds(
    Blocktext,
)
Datetime_strategy = st.builds(
    Datetime,
)
Heading_strategy = st.builds(
    Heading,
)
DlElement_strategy = st.builds(
    DlElement,
)
XHTML_Dt_strategy = st.builds(
    XHTML_Dt,
)
XHTML_Dd_strategy = st.builds(
    XHTML_Dd,
)
Li_strategy = st.builds(
    Li,
)
Lists_strategy = st.builds(
    Lists,
)
Miscinline_strategy = st.builds(
    Miscinline,
)
EMPTY_strategy = st.builds(
    EMPTY,
)
XHTML_Base_strategy = st.builds(
    XHTML_Base,
)
XHTML_TitleBaseHeadElement_strategy = st.builds(
    XHTML_TitleBaseHeadElement,
)
TitleBaseHeadElement_strategy = st.builds(
    TitleBaseHeadElement,
)
MediaDesc_strategy = st.builds(
    MediaDesc,
)
LinkTypes_strategy = st.builds(
    LinkTypes,
)
Attrs_strategy = st.builds(
    Attrs,
)
XHTML_H2_strategy = st.builds(
    XHTML_H2,
)
XHTML_Dl_strategy = st.builds(
    XHTML_Dl,
)
XHTML_Em_strategy = st.builds(
    XHTML_Em,
)
XHTML_Select_strategy = st.builds(
    XHTML_Select,
    disabled=
        safe_text,
    multiple=
        safe_text
)
XHTML_H3_strategy = st.builds(
    XHTML_H3,
)
XHTML_Area_strategy = st.builds(
    XHTML_Area,
    shape=
        safe_text,
    nohref=
        safe_text
)
XHTML_DlElement_strategy = st.builds(
    XHTML_DlElement,
)
XHTML_H4_strategy = st.builds(
    XHTML_H4,
)
XHTML_Tbody_strategy = st.builds(
    XHTML_Tbody,
)
XHTML_Acronym_strategy = st.builds(
    XHTML_Acronym,
)
XHTML_Dfn_strategy = st.builds(
    XHTML_Dfn,
)
XHTML_Thead_strategy = st.builds(
    XHTML_Thead,
)
XHTML_Pre_strategy = st.builds(
    XHTML_Pre,
    xml_space=
        safe_text
)
XHTML_Tr_strategy = st.builds(
    XHTML_Tr,
)
XHTML_Tfoot_strategy = st.builds(
    XHTML_Tfoot,
)
XHTML_Big_strategy = st.builds(
    XHTML_Big,
)
XHTML_Address_strategy = st.builds(
    XHTML_Address,
)
XHTML_Ins_strategy = st.builds(
    XHTML_Ins,
)
XHTML_I_strategy = st.builds(
    XHTML_I,
)
XHTML_Span_strategy = st.builds(
    XHTML_Span,
)
XHTML_Ol_strategy = st.builds(
    XHTML_Ol,
)
XHTML_Li_strategy = st.builds(
    XHTML_Li,
)
XHTML_Col_strategy = st.builds(
    XHTML_Col,
)
XHTML_Ul_strategy = st.builds(
    XHTML_Ul,
)
XHTML_Small_strategy = st.builds(
    XHTML_Small,
)
XHTML_Hr_strategy = st.builds(
    XHTML_Hr,
)
XHTML_H1_strategy = st.builds(
    XHTML_H1,
)
XHTML_Label_strategy = st.builds(
    XHTML_Label,
)
XHTML_Samp_strategy = st.builds(
    XHTML_Samp,
)
XHTML_H6_strategy = st.builds(
    XHTML_H6,
)
XHTML_Sub_strategy = st.builds(
    XHTML_Sub,
)
XHTML_Input_strategy = st.builds(
    XHTML_Input,
    disabled=
        safe_text,
    checked=
        safe_text,
    type=
        safe_text,
    readonly=
        safe_text
)
XHTML_Optgroup_strategy = st.builds(
    XHTML_Optgroup,
    disabled=
        safe_text
)
XHTML_B_strategy = st.builds(
    XHTML_B,
)
XHTML_Abbr_strategy = st.builds(
    XHTML_Abbr,
)
XHTML_Var_strategy = st.builds(
    XHTML_Var,
)
XHTML_Strong_strategy = st.builds(
    XHTML_Strong,
)
XHTML_Body_strategy = st.builds(
    XHTML_Body,
)
XHTML_Button_strategy = st.builds(
    XHTML_Button,
    type=
        safe_text,
    disabled=
        safe_text
)
XHTML_Code_strategy = st.builds(
    XHTML_Code,
)
XHTML_Caption_strategy = st.builds(
    XHTML_Caption,
)
XHTML_Kbd_strategy = st.builds(
    XHTML_Kbd,
)
XHTML_Tt_strategy = st.builds(
    XHTML_Tt,
)
XHTML_Sup_strategy = st.builds(
    XHTML_Sup,
)
XHTML_Q_strategy = st.builds(
    XHTML_Q,
)
XHTML_Cite_strategy = st.builds(
    XHTML_Cite,
)
XHTML_Del_strategy = st.builds(
    XHTML_Del,
)
XHTML_H5_strategy = st.builds(
    XHTML_H5,
)
XHTML_Blockquote_strategy = st.builds(
    XHTML_Blockquote,
)
XHTML_Td_strategy = st.builds(
    XHTML_Td,
    scope=
        safe_text
)
XHTML_Th_strategy = st.builds(
    XHTML_Th,
    scope=
        safe_text
)
XHTML_Colgroup_strategy = st.builds(
    XHTML_Colgroup,
)
Html_strategy = st.builds(
    Html,
)
HeadElement_strategy = st.builds(
    HeadElement,
)
HeadMisc_strategy = st.builds(
    HeadMisc,
)
XHTML_Meta_strategy = st.builds(
    XHTML_Meta,
)
XHTML_Link_strategy = st.builds(
    XHTML_Link,
)
XHTML_Head_strategy = st.builds(
    XHTML_Head,
)
XHTML_HeadMisc_strategy = st.builds(
    XHTML_HeadMisc,
)
Body_strategy = st.builds(
    Body,
)
XHTML_BaseHeadElement_strategy = st.builds(
    XHTML_BaseHeadElement,
)
Base_strategy = st.builds(
    Base,
)
XHTML_BaseTitleHeadElement_strategy = st.builds(
    XHTML_BaseTitleHeadElement,
)
BaseTitleHeadElement_strategy = st.builds(
    BaseTitleHeadElement,
)
Title_strategy = st.builds(
    Title,
)
XHTML_TitleHeadElement_strategy = st.builds(
    XHTML_TitleHeadElement,
)
XHTML_HeadElement_strategy = st.builds(
    XHTML_HeadElement,
)
XHTML_AContent_strategy = st.builds(
    XHTML_AContent,
)
XHTML_Flow_strategy = st.builds(
    XHTML_Flow,
)
XHTML_Block_strategy = st.builds(
    XHTML_Block,
)
Head_strategy = st.builds(
    Head,
)
XHTML_Html_strategy = st.builds(
    XHTML_Html,
)
XHTML_ButtonContent_strategy = st.builds(
    XHTML_ButtonContent,
)
XHTML_FormContent_strategy = st.builds(
    XHTML_FormContent,
)
XHTML_PreContent_strategy = st.builds(
    XHTML_PreContent,
)
AContent_strategy = st.builds(
    AContent,
)
ButtonContent_strategy = st.builds(
    ButtonContent,
)
inline_strategy = st.builds(
    inline,
)
XHTML_Special_strategy = st.builds(
    XHTML_Special,
)
PreContent_strategy = st.builds(
    PreContent,
)
XHTML_Phrase_strategy = st.builds(
    XHTML_Phrase,
)
XHTML_Fontstyle_strategy = st.builds(
    XHTML_Fontstyle,
)
XHTML_A_strategy = st.builds(
    XHTML_A,
    shape=
        safe_text
)
Special_strategy = st.builds(
    Special,
)
XHTML_Img_strategy = st.builds(
    XHTML_Img,
    ismap=
        safe_text
)
XHTML_Object_strategy = st.builds(
    XHTML_Object,
    declare=
        safe_text
)
XHTML_Specialpre_strategy = st.builds(
    XHTML_Specialpre,
)
Number_strategy = st.builds(
    Number,
)
Character_strategy = st.builds(
    Character,
)
XHTML_Focus_strategy = st.builds(
    XHTML_Focus,
)
block_strategy = st.builds(
    block,
)
XHTML_Fieldset_strategy = st.builds(
    XHTML_Fieldset,
)
XHTML_Lists_strategy = st.builds(
    XHTML_Lists,
)
XHTML_Blocktext_strategy = st.builds(
    XHTML_Blocktext,
)
XHTML_P_strategy = st.builds(
    XHTML_P,
)
XHTML_Div_strategy = st.builds(
    XHTML_Div,
)
XHTML_Table_strategy = st.builds(
    XHTML_Table,
    frame=
        safe_text,
    rules=
        safe_text
)
XHTML_Heading_strategy = st.builds(
    XHTML_Heading,
)
PCDATA_strategy = st.builds(
    PCDATA,
)
XHTML_Style_strategy = st.builds(
    XHTML_Style,
    xml_space=
        safe_text
)
XHTML_Script_strategy = st.builds(
    XHTML_Script,
    defer=
        safe_text,
    xml_space=
        safe_text
)
XHTML_Textarea_strategy = st.builds(
    XHTML_Textarea,
    disabled=
        safe_text,
    readonly=
        safe_text
)
XHTML_Option_strategy = st.builds(
    XHTML_Option,
    selected=
        safe_text,
    disabled=
        safe_text
)
XHTML_Title_strategy = st.builds(
    XHTML_Title,
)
FieldsetElement_strategy = st.builds(
    FieldsetElement,
)
XHTML_Legend_strategy = st.builds(
    XHTML_Legend,
)
MapElementContent_strategy = st.builds(
    MapElementContent,
)
ObjectElement_strategy = st.builds(
    ObjectElement,
)
XHTML_Param_strategy = st.builds(
    XHTML_Param,
    valuetype=
        safe_text
)
FormContent_strategy = st.builds(
    FormContent,
)
Flow_strategy = st.builds(
    Flow,
)
XHTML_Inline_strategy = st.builds(
    XHTML_Inline,
)
Block_strategy = st.builds(
    Block,
)
XHTML_block_strategy = st.builds(
    XHTML_block,
)
XHTML_Form_strategy = st.builds(
    XHTML_Form,
    method=
        safe_text
)
XHTML_Misc_strategy = st.builds(
    XHTML_Misc,
)
Inline_strategy = st.builds(
    Inline,
)
XHTML_inline_strategy = st.builds(
    XHTML_inline,
)
Misc_strategy = st.builds(
    Misc,
)
XHTML_Noscript_strategy = st.builds(
    XHTML_Noscript,
)
XHTML_Miscinline_strategy = st.builds(
    XHTML_Miscinline,
)
XHTML_Inlineforms_strategy = st.builds(
    XHTML_Inlineforms,
)
ScriptExpression_strategy = st.builds(
    ScriptExpression,
)
XHTML_Events_strategy = st.builds(
    XHTML_Events,
)
LanguageCode_strategy = st.builds(
    LanguageCode,
)
XHTML_I18n_strategy = st.builds(
    XHTML_I18n,
    dir=
        safe_text
)
Events_strategy = st.builds(
    Events,
)
I18n_strategy = st.builds(
    I18n,
)
XHTML_Map_strategy = st.builds(
    XHTML_Map,
)
CoreAttrs_strategy = st.builds(
    CoreAttrs,
)
XHTML_Br_strategy = st.builds(
    XHTML_Br,
)
XHTML_Bdo_strategy = st.builds(
    XHTML_Bdo,
    dir=
        safe_text
)
XHTML_Attrs_strategy = st.builds(
    XHTML_Attrs,
)
URI_strategy = st.builds(
    URI,
)
Text_strategy = st.builds(
    Text,
)
StyleSheet_strategy = st.builds(
    StyleSheet,
)
ID_strategy = st.builds(
    ID,
)
XHTML_CoreAttrs_strategy = st.builds(
    XHTML_CoreAttrs,
)
Length_strategy = st.builds(
    Length,
)
XHTML_Coords_strategy = st.builds(
    XHTML_Coords,
)
ContentType_strategy = st.builds(
    ContentType,
)
XHTML_ContentTypes_strategy = st.builds(
    XHTML_ContentTypes,
)
CDATA_strategy = st.builds(
    CDATA,
)
XHTML_Datetime_strategy = st.builds(
    XHTML_Datetime,
)
XHTML_StyleSheet_strategy = st.builds(
    XHTML_StyleSheet,
)
XHTML_Length_strategy = st.builds(
    XHTML_Length,
)
XHTML_Pixels_strategy = st.builds(
    XHTML_Pixels,
)
XHTML_MultiLength_strategy = st.builds(
    XHTML_MultiLength,
)
XHTML_ScriptExpression_strategy = st.builds(
    XHTML_ScriptExpression,
)
XHTML_Text_strategy = st.builds(
    XHTML_Text,
)
XHTML_ContentType_strategy = st.builds(
    XHTML_ContentType,
)
XHTML_EMPTY_strategy = st.builds(
    XHTML_EMPTY,
)
IDREF_strategy = st.builds(
    IDREF,
)
XHTML_IDREFS_strategy = st.builds(
    XHTML_IDREFS,
)
XHTML_UriList_strategy = st.builds(
    XHTML_UriList,
)
XHTML_URI_strategy = st.builds(
    XHTML_URI,
)
XHTML_MediaDesc_strategy = st.builds(
    XHTML_MediaDesc,
)
XHTML_LinkTypes_strategy = st.builds(
    XHTML_LinkTypes,
)
XHTML_Number_strategy = st.builds(
    XHTML_Number,
)
XHTML_Character_strategy = st.builds(
    XHTML_Character,
)
NMTOKEN_strategy = st.builds(
    NMTOKEN,
)
XHTML_LanguageCode_strategy = st.builds(
    XHTML_LanguageCode,
)
Charset_strategy = st.builds(
    Charset,
)
XHTML_Charsets_strategy = st.builds(
    XHTML_Charsets,
)
XHTML_Charset_strategy = st.builds(
    XHTML_Charset,
)
ValuedElement_strategy = st.builds(
    ValuedElement,
)
XHTML_IDREF_strategy = st.builds(
    XHTML_IDREF,
)
XHTML_NMTOKEN_strategy = st.builds(
    XHTML_NMTOKEN,
)
XHTML_ID_strategy = st.builds(
    XHTML_ID,
)
XHTML_PCDATA_strategy = st.builds(
    XHTML_PCDATA,
)
XHTML_CDATA_strategy = st.builds(
    XHTML_CDATA,
)
XHTML_ValuedElement_strategy = st.builds(
    XHTML_ValuedElement,
    value=
        safe_text
)

@given(instance=IDREFS_strategy)
@settings(max_examples=50)
def test_idrefs_instantiation(instance):
    assert isinstance(instance, IDREFS)

@given(instance=XHTML_TrElement_strategy)
@settings(max_examples=50)
def test_xhtml_trelement_instantiation(instance):
    assert isinstance(instance, XHTML_TrElement)

@given(instance=TrElement_strategy)
@settings(max_examples=50)
def test_trelement_instantiation(instance):
    assert isinstance(instance, TrElement)

@given(instance=MultiLength_strategy)
@settings(max_examples=50)
def test_multilength_instantiation(instance):
    assert isinstance(instance, MultiLength)

@given(instance=Tr_strategy)
@settings(max_examples=50)
def test_tr_instantiation(instance):
    assert isinstance(instance, Tr)

@given(instance=Cellvalign_strategy)
@settings(max_examples=50)
def test_cellvalign_instantiation(instance):
    assert isinstance(instance, Cellvalign)

@given(instance=Cellhalign_strategy)
@settings(max_examples=50)
def test_cellhalign_instantiation(instance):
    assert isinstance(instance, Cellhalign)

@given(instance=Col_strategy)
@settings(max_examples=50)
def test_col_instantiation(instance):
    assert isinstance(instance, Col)

@given(instance=XHTML_ColElement_strategy)
@settings(max_examples=50)
def test_xhtml_colelement_instantiation(instance):
    assert isinstance(instance, XHTML_ColElement)

@given(instance=Tbody_strategy)
@settings(max_examples=50)
def test_tbody_instantiation(instance):
    assert isinstance(instance, Tbody)

@given(instance=XHTML_TableElement_strategy)
@settings(max_examples=50)
def test_xhtml_tableelement_instantiation(instance):
    assert isinstance(instance, XHTML_TableElement)

@given(instance=Pixels_strategy)
@settings(max_examples=50)
def test_pixels_instantiation(instance):
    assert isinstance(instance, Pixels)

@given(instance=Colgroup_strategy)
@settings(max_examples=50)
def test_colgroup_instantiation(instance):
    assert isinstance(instance, Colgroup)

@given(instance=TableElement_strategy)
@settings(max_examples=50)
def test_tableelement_instantiation(instance):
    assert isinstance(instance, TableElement)

@given(instance=Tfoot_strategy)
@settings(max_examples=50)
def test_tfoot_instantiation(instance):
    assert isinstance(instance, Tfoot)

@given(instance=Thead_strategy)
@settings(max_examples=50)
def test_thead_instantiation(instance):
    assert isinstance(instance, Thead)

@given(instance=ColElement_strategy)
@settings(max_examples=50)
def test_colelement_instantiation(instance):
    assert isinstance(instance, ColElement)

@given(instance=Caption_strategy)
@settings(max_examples=50)
def test_caption_instantiation(instance):
    assert isinstance(instance, Caption)

@given(instance=XHTML_Cellvalign_strategy)
@settings(max_examples=50)
def test_xhtml_cellvalign_instantiation(instance):
    assert isinstance(instance, XHTML_Cellvalign)



@given(instance=XHTML_Cellvalign_strategy)
def test_xhtml_cellvalign_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=XHTML_Cellhalign_strategy)
@settings(max_examples=50)
def test_xhtml_cellhalign_instantiation(instance):
    assert isinstance(instance, XHTML_Cellhalign)



@given(instance=XHTML_Cellhalign_strategy)
def test_xhtml_cellhalign_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=XHTML_FieldsetElement_strategy)
@settings(max_examples=50)
def test_xhtml_fieldsetelement_instantiation(instance):
    assert isinstance(instance, XHTML_FieldsetElement)

@given(instance=XHTML_SelectElement_strategy)
@settings(max_examples=50)
def test_xhtml_selectelement_instantiation(instance):
    assert isinstance(instance, XHTML_SelectElement)

@given(instance=Option_strategy)
@settings(max_examples=50)
def test_option_instantiation(instance):
    assert isinstance(instance, Option)

@given(instance=SelectElement_strategy)
@settings(max_examples=50)
def test_selectelement_instantiation(instance):
    assert isinstance(instance, SelectElement)

@given(instance=Inlineforms_strategy)
@settings(max_examples=50)
def test_inlineforms_instantiation(instance):
    assert isinstance(instance, Inlineforms)

@given(instance=Charsets_strategy)
@settings(max_examples=50)
def test_charsets_instantiation(instance):
    assert isinstance(instance, Charsets)

@given(instance=ContentTypes_strategy)
@settings(max_examples=50)
def test_contenttypes_instantiation(instance):
    assert isinstance(instance, ContentTypes)

@given(instance=MapContent_strategy)
@settings(max_examples=50)
def test_mapcontent_instantiation(instance):
    assert isinstance(instance, MapContent)

@given(instance=XHTML_MapElementContent_strategy)
@settings(max_examples=50)
def test_xhtml_mapelementcontent_instantiation(instance):
    assert isinstance(instance, XHTML_MapElementContent)

@given(instance=XHTML_MapElement_strategy)
@settings(max_examples=50)
def test_xhtml_mapelement_instantiation(instance):
    assert isinstance(instance, XHTML_MapElement)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=XHTML_MapContent_strategy)
@settings(max_examples=50)
def test_xhtml_mapcontent_instantiation(instance):
    assert isinstance(instance, XHTML_MapContent)

@given(instance=UriList_strategy)
@settings(max_examples=50)
def test_urilist_instantiation(instance):
    assert isinstance(instance, UriList)

@given(instance=XHTML_ObjectElement_strategy)
@settings(max_examples=50)
def test_xhtml_objectelement_instantiation(instance):
    assert isinstance(instance, XHTML_ObjectElement)

@given(instance=Fontstyle_strategy)
@settings(max_examples=50)
def test_fontstyle_instantiation(instance):
    assert isinstance(instance, Fontstyle)

@given(instance=Phrase_strategy)
@settings(max_examples=50)
def test_phrase_instantiation(instance):
    assert isinstance(instance, Phrase)

@given(instance=Focus_strategy)
@settings(max_examples=50)
def test_focus_instantiation(instance):
    assert isinstance(instance, Focus)

@given(instance=Specialpre_strategy)
@settings(max_examples=50)
def test_specialpre_instantiation(instance):
    assert isinstance(instance, Specialpre)

@given(instance=Coords_strategy)
@settings(max_examples=50)
def test_coords_instantiation(instance):
    assert isinstance(instance, Coords)

@given(instance=Blocktext_strategy)
@settings(max_examples=50)
def test_blocktext_instantiation(instance):
    assert isinstance(instance, Blocktext)

@given(instance=Datetime_strategy)
@settings(max_examples=50)
def test_datetime_instantiation(instance):
    assert isinstance(instance, Datetime)

@given(instance=Heading_strategy)
@settings(max_examples=50)
def test_heading_instantiation(instance):
    assert isinstance(instance, Heading)

@given(instance=DlElement_strategy)
@settings(max_examples=50)
def test_dlelement_instantiation(instance):
    assert isinstance(instance, DlElement)

@given(instance=XHTML_Dt_strategy)
@settings(max_examples=50)
def test_xhtml_dt_instantiation(instance):
    assert isinstance(instance, XHTML_Dt)

@given(instance=XHTML_Dd_strategy)
@settings(max_examples=50)
def test_xhtml_dd_instantiation(instance):
    assert isinstance(instance, XHTML_Dd)

@given(instance=Li_strategy)
@settings(max_examples=50)
def test_li_instantiation(instance):
    assert isinstance(instance, Li)

@given(instance=Lists_strategy)
@settings(max_examples=50)
def test_lists_instantiation(instance):
    assert isinstance(instance, Lists)

@given(instance=Miscinline_strategy)
@settings(max_examples=50)
def test_miscinline_instantiation(instance):
    assert isinstance(instance, Miscinline)

@given(instance=EMPTY_strategy)
@settings(max_examples=50)
def test_empty_instantiation(instance):
    assert isinstance(instance, EMPTY)

@given(instance=XHTML_Base_strategy)
@settings(max_examples=50)
def test_xhtml_base_instantiation(instance):
    assert isinstance(instance, XHTML_Base)

@given(instance=XHTML_TitleBaseHeadElement_strategy)
@settings(max_examples=50)
def test_xhtml_titlebaseheadelement_instantiation(instance):
    assert isinstance(instance, XHTML_TitleBaseHeadElement)

@given(instance=TitleBaseHeadElement_strategy)
@settings(max_examples=50)
def test_titlebaseheadelement_instantiation(instance):
    assert isinstance(instance, TitleBaseHeadElement)

@given(instance=MediaDesc_strategy)
@settings(max_examples=50)
def test_mediadesc_instantiation(instance):
    assert isinstance(instance, MediaDesc)

@given(instance=LinkTypes_strategy)
@settings(max_examples=50)
def test_linktypes_instantiation(instance):
    assert isinstance(instance, LinkTypes)

@given(instance=Attrs_strategy)
@settings(max_examples=50)
def test_attrs_instantiation(instance):
    assert isinstance(instance, Attrs)

@given(instance=XHTML_H2_strategy)
@settings(max_examples=50)
def test_xhtml_h2_instantiation(instance):
    assert isinstance(instance, XHTML_H2)

@given(instance=XHTML_Dl_strategy)
@settings(max_examples=50)
def test_xhtml_dl_instantiation(instance):
    assert isinstance(instance, XHTML_Dl)

@given(instance=XHTML_Em_strategy)
@settings(max_examples=50)
def test_xhtml_em_instantiation(instance):
    assert isinstance(instance, XHTML_Em)

@given(instance=XHTML_Select_strategy)
@settings(max_examples=50)
def test_xhtml_select_instantiation(instance):
    assert isinstance(instance, XHTML_Select)



@given(instance=XHTML_Select_strategy)
def test_xhtml_select_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=XHTML_Select_strategy)
def test_xhtml_select_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=XHTML_H3_strategy)
@settings(max_examples=50)
def test_xhtml_h3_instantiation(instance):
    assert isinstance(instance, XHTML_H3)

@given(instance=XHTML_Area_strategy)
@settings(max_examples=50)
def test_xhtml_area_instantiation(instance):
    assert isinstance(instance, XHTML_Area)



@given(instance=XHTML_Area_strategy)
def test_xhtml_area_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original



@given(instance=XHTML_Area_strategy)
def test_xhtml_area_nohref_setter(instance):
    original = instance.nohref
    instance.nohref = original
    assert instance.nohref == original

@given(instance=XHTML_DlElement_strategy)
@settings(max_examples=50)
def test_xhtml_dlelement_instantiation(instance):
    assert isinstance(instance, XHTML_DlElement)

@given(instance=XHTML_H4_strategy)
@settings(max_examples=50)
def test_xhtml_h4_instantiation(instance):
    assert isinstance(instance, XHTML_H4)

@given(instance=XHTML_Tbody_strategy)
@settings(max_examples=50)
def test_xhtml_tbody_instantiation(instance):
    assert isinstance(instance, XHTML_Tbody)

@given(instance=XHTML_Acronym_strategy)
@settings(max_examples=50)
def test_xhtml_acronym_instantiation(instance):
    assert isinstance(instance, XHTML_Acronym)

@given(instance=XHTML_Dfn_strategy)
@settings(max_examples=50)
def test_xhtml_dfn_instantiation(instance):
    assert isinstance(instance, XHTML_Dfn)

@given(instance=XHTML_Thead_strategy)
@settings(max_examples=50)
def test_xhtml_thead_instantiation(instance):
    assert isinstance(instance, XHTML_Thead)

@given(instance=XHTML_Pre_strategy)
@settings(max_examples=50)
def test_xhtml_pre_instantiation(instance):
    assert isinstance(instance, XHTML_Pre)



@given(instance=XHTML_Pre_strategy)
def test_xhtml_pre_xml_space_setter(instance):
    original = instance.xml_space
    instance.xml_space = original
    assert instance.xml_space == original

@given(instance=XHTML_Tr_strategy)
@settings(max_examples=50)
def test_xhtml_tr_instantiation(instance):
    assert isinstance(instance, XHTML_Tr)

@given(instance=XHTML_Tfoot_strategy)
@settings(max_examples=50)
def test_xhtml_tfoot_instantiation(instance):
    assert isinstance(instance, XHTML_Tfoot)

@given(instance=XHTML_Big_strategy)
@settings(max_examples=50)
def test_xhtml_big_instantiation(instance):
    assert isinstance(instance, XHTML_Big)

@given(instance=XHTML_Address_strategy)
@settings(max_examples=50)
def test_xhtml_address_instantiation(instance):
    assert isinstance(instance, XHTML_Address)

@given(instance=XHTML_Ins_strategy)
@settings(max_examples=50)
def test_xhtml_ins_instantiation(instance):
    assert isinstance(instance, XHTML_Ins)

@given(instance=XHTML_I_strategy)
@settings(max_examples=50)
def test_xhtml_i_instantiation(instance):
    assert isinstance(instance, XHTML_I)

@given(instance=XHTML_Span_strategy)
@settings(max_examples=50)
def test_xhtml_span_instantiation(instance):
    assert isinstance(instance, XHTML_Span)

@given(instance=XHTML_Ol_strategy)
@settings(max_examples=50)
def test_xhtml_ol_instantiation(instance):
    assert isinstance(instance, XHTML_Ol)

@given(instance=XHTML_Li_strategy)
@settings(max_examples=50)
def test_xhtml_li_instantiation(instance):
    assert isinstance(instance, XHTML_Li)

@given(instance=XHTML_Col_strategy)
@settings(max_examples=50)
def test_xhtml_col_instantiation(instance):
    assert isinstance(instance, XHTML_Col)

@given(instance=XHTML_Ul_strategy)
@settings(max_examples=50)
def test_xhtml_ul_instantiation(instance):
    assert isinstance(instance, XHTML_Ul)

@given(instance=XHTML_Small_strategy)
@settings(max_examples=50)
def test_xhtml_small_instantiation(instance):
    assert isinstance(instance, XHTML_Small)

@given(instance=XHTML_Hr_strategy)
@settings(max_examples=50)
def test_xhtml_hr_instantiation(instance):
    assert isinstance(instance, XHTML_Hr)

@given(instance=XHTML_H1_strategy)
@settings(max_examples=50)
def test_xhtml_h1_instantiation(instance):
    assert isinstance(instance, XHTML_H1)

@given(instance=XHTML_Label_strategy)
@settings(max_examples=50)
def test_xhtml_label_instantiation(instance):
    assert isinstance(instance, XHTML_Label)

@given(instance=XHTML_Samp_strategy)
@settings(max_examples=50)
def test_xhtml_samp_instantiation(instance):
    assert isinstance(instance, XHTML_Samp)

@given(instance=XHTML_H6_strategy)
@settings(max_examples=50)
def test_xhtml_h6_instantiation(instance):
    assert isinstance(instance, XHTML_H6)

@given(instance=XHTML_Sub_strategy)
@settings(max_examples=50)
def test_xhtml_sub_instantiation(instance):
    assert isinstance(instance, XHTML_Sub)

@given(instance=XHTML_Input_strategy)
@settings(max_examples=50)
def test_xhtml_input_instantiation(instance):
    assert isinstance(instance, XHTML_Input)



@given(instance=XHTML_Input_strategy)
def test_xhtml_input_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=XHTML_Input_strategy)
def test_xhtml_input_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original



@given(instance=XHTML_Input_strategy)
def test_xhtml_input_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=XHTML_Input_strategy)
def test_xhtml_input_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=XHTML_Optgroup_strategy)
@settings(max_examples=50)
def test_xhtml_optgroup_instantiation(instance):
    assert isinstance(instance, XHTML_Optgroup)



@given(instance=XHTML_Optgroup_strategy)
def test_xhtml_optgroup_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML_B_strategy)
@settings(max_examples=50)
def test_xhtml_b_instantiation(instance):
    assert isinstance(instance, XHTML_B)

@given(instance=XHTML_Abbr_strategy)
@settings(max_examples=50)
def test_xhtml_abbr_instantiation(instance):
    assert isinstance(instance, XHTML_Abbr)

@given(instance=XHTML_Var_strategy)
@settings(max_examples=50)
def test_xhtml_var_instantiation(instance):
    assert isinstance(instance, XHTML_Var)

@given(instance=XHTML_Strong_strategy)
@settings(max_examples=50)
def test_xhtml_strong_instantiation(instance):
    assert isinstance(instance, XHTML_Strong)

@given(instance=XHTML_Body_strategy)
@settings(max_examples=50)
def test_xhtml_body_instantiation(instance):
    assert isinstance(instance, XHTML_Body)

@given(instance=XHTML_Button_strategy)
@settings(max_examples=50)
def test_xhtml_button_instantiation(instance):
    assert isinstance(instance, XHTML_Button)



@given(instance=XHTML_Button_strategy)
def test_xhtml_button_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=XHTML_Button_strategy)
def test_xhtml_button_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML_Code_strategy)
@settings(max_examples=50)
def test_xhtml_code_instantiation(instance):
    assert isinstance(instance, XHTML_Code)

@given(instance=XHTML_Caption_strategy)
@settings(max_examples=50)
def test_xhtml_caption_instantiation(instance):
    assert isinstance(instance, XHTML_Caption)

@given(instance=XHTML_Kbd_strategy)
@settings(max_examples=50)
def test_xhtml_kbd_instantiation(instance):
    assert isinstance(instance, XHTML_Kbd)

@given(instance=XHTML_Tt_strategy)
@settings(max_examples=50)
def test_xhtml_tt_instantiation(instance):
    assert isinstance(instance, XHTML_Tt)

@given(instance=XHTML_Sup_strategy)
@settings(max_examples=50)
def test_xhtml_sup_instantiation(instance):
    assert isinstance(instance, XHTML_Sup)

@given(instance=XHTML_Q_strategy)
@settings(max_examples=50)
def test_xhtml_q_instantiation(instance):
    assert isinstance(instance, XHTML_Q)

@given(instance=XHTML_Cite_strategy)
@settings(max_examples=50)
def test_xhtml_cite_instantiation(instance):
    assert isinstance(instance, XHTML_Cite)

@given(instance=XHTML_Del_strategy)
@settings(max_examples=50)
def test_xhtml_del_instantiation(instance):
    assert isinstance(instance, XHTML_Del)

@given(instance=XHTML_H5_strategy)
@settings(max_examples=50)
def test_xhtml_h5_instantiation(instance):
    assert isinstance(instance, XHTML_H5)

@given(instance=XHTML_Blockquote_strategy)
@settings(max_examples=50)
def test_xhtml_blockquote_instantiation(instance):
    assert isinstance(instance, XHTML_Blockquote)

@given(instance=XHTML_Td_strategy)
@settings(max_examples=50)
def test_xhtml_td_instantiation(instance):
    assert isinstance(instance, XHTML_Td)



@given(instance=XHTML_Td_strategy)
def test_xhtml_td_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=XHTML_Th_strategy)
@settings(max_examples=50)
def test_xhtml_th_instantiation(instance):
    assert isinstance(instance, XHTML_Th)



@given(instance=XHTML_Th_strategy)
def test_xhtml_th_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=XHTML_Colgroup_strategy)
@settings(max_examples=50)
def test_xhtml_colgroup_instantiation(instance):
    assert isinstance(instance, XHTML_Colgroup)

@given(instance=Html_strategy)
@settings(max_examples=50)
def test_html_instantiation(instance):
    assert isinstance(instance, Html)

@given(instance=HeadElement_strategy)
@settings(max_examples=50)
def test_headelement_instantiation(instance):
    assert isinstance(instance, HeadElement)

@given(instance=HeadMisc_strategy)
@settings(max_examples=50)
def test_headmisc_instantiation(instance):
    assert isinstance(instance, HeadMisc)

@given(instance=XHTML_Meta_strategy)
@settings(max_examples=50)
def test_xhtml_meta_instantiation(instance):
    assert isinstance(instance, XHTML_Meta)

@given(instance=XHTML_Link_strategy)
@settings(max_examples=50)
def test_xhtml_link_instantiation(instance):
    assert isinstance(instance, XHTML_Link)

@given(instance=XHTML_Head_strategy)
@settings(max_examples=50)
def test_xhtml_head_instantiation(instance):
    assert isinstance(instance, XHTML_Head)

@given(instance=XHTML_HeadMisc_strategy)
@settings(max_examples=50)
def test_xhtml_headmisc_instantiation(instance):
    assert isinstance(instance, XHTML_HeadMisc)

@given(instance=Body_strategy)
@settings(max_examples=50)
def test_body_instantiation(instance):
    assert isinstance(instance, Body)

@given(instance=XHTML_BaseHeadElement_strategy)
@settings(max_examples=50)
def test_xhtml_baseheadelement_instantiation(instance):
    assert isinstance(instance, XHTML_BaseHeadElement)

@given(instance=Base_strategy)
@settings(max_examples=50)
def test_base_instantiation(instance):
    assert isinstance(instance, Base)

@given(instance=XHTML_BaseTitleHeadElement_strategy)
@settings(max_examples=50)
def test_xhtml_basetitleheadelement_instantiation(instance):
    assert isinstance(instance, XHTML_BaseTitleHeadElement)

@given(instance=BaseTitleHeadElement_strategy)
@settings(max_examples=50)
def test_basetitleheadelement_instantiation(instance):
    assert isinstance(instance, BaseTitleHeadElement)

@given(instance=Title_strategy)
@settings(max_examples=50)
def test_title_instantiation(instance):
    assert isinstance(instance, Title)

@given(instance=XHTML_TitleHeadElement_strategy)
@settings(max_examples=50)
def test_xhtml_titleheadelement_instantiation(instance):
    assert isinstance(instance, XHTML_TitleHeadElement)

@given(instance=XHTML_HeadElement_strategy)
@settings(max_examples=50)
def test_xhtml_headelement_instantiation(instance):
    assert isinstance(instance, XHTML_HeadElement)

@given(instance=XHTML_AContent_strategy)
@settings(max_examples=50)
def test_xhtml_acontent_instantiation(instance):
    assert isinstance(instance, XHTML_AContent)

@given(instance=XHTML_Flow_strategy)
@settings(max_examples=50)
def test_xhtml_flow_instantiation(instance):
    assert isinstance(instance, XHTML_Flow)

@given(instance=XHTML_Block_strategy)
@settings(max_examples=50)
def test_xhtml_block_instantiation(instance):
    assert isinstance(instance, XHTML_Block)

@given(instance=Head_strategy)
@settings(max_examples=50)
def test_head_instantiation(instance):
    assert isinstance(instance, Head)

@given(instance=XHTML_Html_strategy)
@settings(max_examples=50)
def test_xhtml_html_instantiation(instance):
    assert isinstance(instance, XHTML_Html)

@given(instance=XHTML_ButtonContent_strategy)
@settings(max_examples=50)
def test_xhtml_buttoncontent_instantiation(instance):
    assert isinstance(instance, XHTML_ButtonContent)

@given(instance=XHTML_FormContent_strategy)
@settings(max_examples=50)
def test_xhtml_formcontent_instantiation(instance):
    assert isinstance(instance, XHTML_FormContent)

@given(instance=XHTML_PreContent_strategy)
@settings(max_examples=50)
def test_xhtml_precontent_instantiation(instance):
    assert isinstance(instance, XHTML_PreContent)

@given(instance=AContent_strategy)
@settings(max_examples=50)
def test_acontent_instantiation(instance):
    assert isinstance(instance, AContent)

@given(instance=ButtonContent_strategy)
@settings(max_examples=50)
def test_buttoncontent_instantiation(instance):
    assert isinstance(instance, ButtonContent)

@given(instance=inline_strategy)
@settings(max_examples=50)
def test_inline_instantiation(instance):
    assert isinstance(instance, inline)

@given(instance=XHTML_Special_strategy)
@settings(max_examples=50)
def test_xhtml_special_instantiation(instance):
    assert isinstance(instance, XHTML_Special)

@given(instance=PreContent_strategy)
@settings(max_examples=50)
def test_precontent_instantiation(instance):
    assert isinstance(instance, PreContent)

@given(instance=XHTML_Phrase_strategy)
@settings(max_examples=50)
def test_xhtml_phrase_instantiation(instance):
    assert isinstance(instance, XHTML_Phrase)

@given(instance=XHTML_Fontstyle_strategy)
@settings(max_examples=50)
def test_xhtml_fontstyle_instantiation(instance):
    assert isinstance(instance, XHTML_Fontstyle)

@given(instance=XHTML_A_strategy)
@settings(max_examples=50)
def test_xhtml_a_instantiation(instance):
    assert isinstance(instance, XHTML_A)



@given(instance=XHTML_A_strategy)
def test_xhtml_a_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=Special_strategy)
@settings(max_examples=50)
def test_special_instantiation(instance):
    assert isinstance(instance, Special)

@given(instance=XHTML_Img_strategy)
@settings(max_examples=50)
def test_xhtml_img_instantiation(instance):
    assert isinstance(instance, XHTML_Img)



@given(instance=XHTML_Img_strategy)
def test_xhtml_img_ismap_setter(instance):
    original = instance.ismap
    instance.ismap = original
    assert instance.ismap == original

@given(instance=XHTML_Object_strategy)
@settings(max_examples=50)
def test_xhtml_object_instantiation(instance):
    assert isinstance(instance, XHTML_Object)



@given(instance=XHTML_Object_strategy)
def test_xhtml_object_declare_setter(instance):
    original = instance.declare
    instance.declare = original
    assert instance.declare == original

@given(instance=XHTML_Specialpre_strategy)
@settings(max_examples=50)
def test_xhtml_specialpre_instantiation(instance):
    assert isinstance(instance, XHTML_Specialpre)

@given(instance=Number_strategy)
@settings(max_examples=50)
def test_number_instantiation(instance):
    assert isinstance(instance, Number)

@given(instance=Character_strategy)
@settings(max_examples=50)
def test_character_instantiation(instance):
    assert isinstance(instance, Character)

@given(instance=XHTML_Focus_strategy)
@settings(max_examples=50)
def test_xhtml_focus_instantiation(instance):
    assert isinstance(instance, XHTML_Focus)

@given(instance=block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, block)

@given(instance=XHTML_Fieldset_strategy)
@settings(max_examples=50)
def test_xhtml_fieldset_instantiation(instance):
    assert isinstance(instance, XHTML_Fieldset)

@given(instance=XHTML_Lists_strategy)
@settings(max_examples=50)
def test_xhtml_lists_instantiation(instance):
    assert isinstance(instance, XHTML_Lists)

@given(instance=XHTML_Blocktext_strategy)
@settings(max_examples=50)
def test_xhtml_blocktext_instantiation(instance):
    assert isinstance(instance, XHTML_Blocktext)

@given(instance=XHTML_P_strategy)
@settings(max_examples=50)
def test_xhtml_p_instantiation(instance):
    assert isinstance(instance, XHTML_P)

@given(instance=XHTML_Div_strategy)
@settings(max_examples=50)
def test_xhtml_div_instantiation(instance):
    assert isinstance(instance, XHTML_Div)

@given(instance=XHTML_Table_strategy)
@settings(max_examples=50)
def test_xhtml_table_instantiation(instance):
    assert isinstance(instance, XHTML_Table)



@given(instance=XHTML_Table_strategy)
def test_xhtml_table_frame_setter(instance):
    original = instance.frame
    instance.frame = original
    assert instance.frame == original



@given(instance=XHTML_Table_strategy)
def test_xhtml_table_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=XHTML_Heading_strategy)
@settings(max_examples=50)
def test_xhtml_heading_instantiation(instance):
    assert isinstance(instance, XHTML_Heading)

@given(instance=PCDATA_strategy)
@settings(max_examples=50)
def test_pcdata_instantiation(instance):
    assert isinstance(instance, PCDATA)

@given(instance=XHTML_Style_strategy)
@settings(max_examples=50)
def test_xhtml_style_instantiation(instance):
    assert isinstance(instance, XHTML_Style)



@given(instance=XHTML_Style_strategy)
def test_xhtml_style_xml_space_setter(instance):
    original = instance.xml_space
    instance.xml_space = original
    assert instance.xml_space == original

@given(instance=XHTML_Script_strategy)
@settings(max_examples=50)
def test_xhtml_script_instantiation(instance):
    assert isinstance(instance, XHTML_Script)



@given(instance=XHTML_Script_strategy)
def test_xhtml_script_defer_setter(instance):
    original = instance.defer
    instance.defer = original
    assert instance.defer == original



@given(instance=XHTML_Script_strategy)
def test_xhtml_script_xml_space_setter(instance):
    original = instance.xml_space
    instance.xml_space = original
    assert instance.xml_space == original

@given(instance=XHTML_Textarea_strategy)
@settings(max_examples=50)
def test_xhtml_textarea_instantiation(instance):
    assert isinstance(instance, XHTML_Textarea)



@given(instance=XHTML_Textarea_strategy)
def test_xhtml_textarea_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original



@given(instance=XHTML_Textarea_strategy)
def test_xhtml_textarea_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=XHTML_Option_strategy)
@settings(max_examples=50)
def test_xhtml_option_instantiation(instance):
    assert isinstance(instance, XHTML_Option)



@given(instance=XHTML_Option_strategy)
def test_xhtml_option_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original



@given(instance=XHTML_Option_strategy)
def test_xhtml_option_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML_Title_strategy)
@settings(max_examples=50)
def test_xhtml_title_instantiation(instance):
    assert isinstance(instance, XHTML_Title)

@given(instance=FieldsetElement_strategy)
@settings(max_examples=50)
def test_fieldsetelement_instantiation(instance):
    assert isinstance(instance, FieldsetElement)

@given(instance=XHTML_Legend_strategy)
@settings(max_examples=50)
def test_xhtml_legend_instantiation(instance):
    assert isinstance(instance, XHTML_Legend)

@given(instance=MapElementContent_strategy)
@settings(max_examples=50)
def test_mapelementcontent_instantiation(instance):
    assert isinstance(instance, MapElementContent)

@given(instance=ObjectElement_strategy)
@settings(max_examples=50)
def test_objectelement_instantiation(instance):
    assert isinstance(instance, ObjectElement)

@given(instance=XHTML_Param_strategy)
@settings(max_examples=50)
def test_xhtml_param_instantiation(instance):
    assert isinstance(instance, XHTML_Param)



@given(instance=XHTML_Param_strategy)
def test_xhtml_param_valuetype_setter(instance):
    original = instance.valuetype
    instance.valuetype = original
    assert instance.valuetype == original

@given(instance=FormContent_strategy)
@settings(max_examples=50)
def test_formcontent_instantiation(instance):
    assert isinstance(instance, FormContent)

@given(instance=Flow_strategy)
@settings(max_examples=50)
def test_flow_instantiation(instance):
    assert isinstance(instance, Flow)

@given(instance=XHTML_Inline_strategy)
@settings(max_examples=50)
def test_xhtml_inline_instantiation(instance):
    assert isinstance(instance, XHTML_Inline)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=XHTML_block_strategy)
@settings(max_examples=50)
def test_xhtml_block_instantiation(instance):
    assert isinstance(instance, XHTML_block)

@given(instance=XHTML_Form_strategy)
@settings(max_examples=50)
def test_xhtml_form_instantiation(instance):
    assert isinstance(instance, XHTML_Form)



@given(instance=XHTML_Form_strategy)
def test_xhtml_form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=XHTML_Misc_strategy)
@settings(max_examples=50)
def test_xhtml_misc_instantiation(instance):
    assert isinstance(instance, XHTML_Misc)

@given(instance=Inline_strategy)
@settings(max_examples=50)
def test_inline_instantiation(instance):
    assert isinstance(instance, Inline)

@given(instance=XHTML_inline_strategy)
@settings(max_examples=50)
def test_xhtml_inline_instantiation(instance):
    assert isinstance(instance, XHTML_inline)

@given(instance=Misc_strategy)
@settings(max_examples=50)
def test_misc_instantiation(instance):
    assert isinstance(instance, Misc)

@given(instance=XHTML_Noscript_strategy)
@settings(max_examples=50)
def test_xhtml_noscript_instantiation(instance):
    assert isinstance(instance, XHTML_Noscript)

@given(instance=XHTML_Miscinline_strategy)
@settings(max_examples=50)
def test_xhtml_miscinline_instantiation(instance):
    assert isinstance(instance, XHTML_Miscinline)

@given(instance=XHTML_Inlineforms_strategy)
@settings(max_examples=50)
def test_xhtml_inlineforms_instantiation(instance):
    assert isinstance(instance, XHTML_Inlineforms)

@given(instance=ScriptExpression_strategy)
@settings(max_examples=50)
def test_scriptexpression_instantiation(instance):
    assert isinstance(instance, ScriptExpression)

@given(instance=XHTML_Events_strategy)
@settings(max_examples=50)
def test_xhtml_events_instantiation(instance):
    assert isinstance(instance, XHTML_Events)

@given(instance=LanguageCode_strategy)
@settings(max_examples=50)
def test_languagecode_instantiation(instance):
    assert isinstance(instance, LanguageCode)

@given(instance=XHTML_I18n_strategy)
@settings(max_examples=50)
def test_xhtml_i18n_instantiation(instance):
    assert isinstance(instance, XHTML_I18n)



@given(instance=XHTML_I18n_strategy)
def test_xhtml_i18n_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=Events_strategy)
@settings(max_examples=50)
def test_events_instantiation(instance):
    assert isinstance(instance, Events)

@given(instance=I18n_strategy)
@settings(max_examples=50)
def test_i18n_instantiation(instance):
    assert isinstance(instance, I18n)

@given(instance=XHTML_Map_strategy)
@settings(max_examples=50)
def test_xhtml_map_instantiation(instance):
    assert isinstance(instance, XHTML_Map)

@given(instance=CoreAttrs_strategy)
@settings(max_examples=50)
def test_coreattrs_instantiation(instance):
    assert isinstance(instance, CoreAttrs)

@given(instance=XHTML_Br_strategy)
@settings(max_examples=50)
def test_xhtml_br_instantiation(instance):
    assert isinstance(instance, XHTML_Br)

@given(instance=XHTML_Bdo_strategy)
@settings(max_examples=50)
def test_xhtml_bdo_instantiation(instance):
    assert isinstance(instance, XHTML_Bdo)



@given(instance=XHTML_Bdo_strategy)
def test_xhtml_bdo_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=XHTML_Attrs_strategy)
@settings(max_examples=50)
def test_xhtml_attrs_instantiation(instance):
    assert isinstance(instance, XHTML_Attrs)

@given(instance=URI_strategy)
@settings(max_examples=50)
def test_uri_instantiation(instance):
    assert isinstance(instance, URI)

@given(instance=Text_strategy)
@settings(max_examples=50)
def test_text_instantiation(instance):
    assert isinstance(instance, Text)

@given(instance=StyleSheet_strategy)
@settings(max_examples=50)
def test_stylesheet_instantiation(instance):
    assert isinstance(instance, StyleSheet)

@given(instance=ID_strategy)
@settings(max_examples=50)
def test_id_instantiation(instance):
    assert isinstance(instance, ID)

@given(instance=XHTML_CoreAttrs_strategy)
@settings(max_examples=50)
def test_xhtml_coreattrs_instantiation(instance):
    assert isinstance(instance, XHTML_CoreAttrs)

@given(instance=Length_strategy)
@settings(max_examples=50)
def test_length_instantiation(instance):
    assert isinstance(instance, Length)

@given(instance=XHTML_Coords_strategy)
@settings(max_examples=50)
def test_xhtml_coords_instantiation(instance):
    assert isinstance(instance, XHTML_Coords)

@given(instance=ContentType_strategy)
@settings(max_examples=50)
def test_contenttype_instantiation(instance):
    assert isinstance(instance, ContentType)

@given(instance=XHTML_ContentTypes_strategy)
@settings(max_examples=50)
def test_xhtml_contenttypes_instantiation(instance):
    assert isinstance(instance, XHTML_ContentTypes)

@given(instance=CDATA_strategy)
@settings(max_examples=50)
def test_cdata_instantiation(instance):
    assert isinstance(instance, CDATA)

@given(instance=XHTML_Datetime_strategy)
@settings(max_examples=50)
def test_xhtml_datetime_instantiation(instance):
    assert isinstance(instance, XHTML_Datetime)

@given(instance=XHTML_StyleSheet_strategy)
@settings(max_examples=50)
def test_xhtml_stylesheet_instantiation(instance):
    assert isinstance(instance, XHTML_StyleSheet)

@given(instance=XHTML_Length_strategy)
@settings(max_examples=50)
def test_xhtml_length_instantiation(instance):
    assert isinstance(instance, XHTML_Length)

@given(instance=XHTML_Pixels_strategy)
@settings(max_examples=50)
def test_xhtml_pixels_instantiation(instance):
    assert isinstance(instance, XHTML_Pixels)

@given(instance=XHTML_MultiLength_strategy)
@settings(max_examples=50)
def test_xhtml_multilength_instantiation(instance):
    assert isinstance(instance, XHTML_MultiLength)

@given(instance=XHTML_ScriptExpression_strategy)
@settings(max_examples=50)
def test_xhtml_scriptexpression_instantiation(instance):
    assert isinstance(instance, XHTML_ScriptExpression)

@given(instance=XHTML_Text_strategy)
@settings(max_examples=50)
def test_xhtml_text_instantiation(instance):
    assert isinstance(instance, XHTML_Text)

@given(instance=XHTML_ContentType_strategy)
@settings(max_examples=50)
def test_xhtml_contenttype_instantiation(instance):
    assert isinstance(instance, XHTML_ContentType)

@given(instance=XHTML_EMPTY_strategy)
@settings(max_examples=50)
def test_xhtml_empty_instantiation(instance):
    assert isinstance(instance, XHTML_EMPTY)

@given(instance=IDREF_strategy)
@settings(max_examples=50)
def test_idref_instantiation(instance):
    assert isinstance(instance, IDREF)

@given(instance=XHTML_IDREFS_strategy)
@settings(max_examples=50)
def test_xhtml_idrefs_instantiation(instance):
    assert isinstance(instance, XHTML_IDREFS)

@given(instance=XHTML_UriList_strategy)
@settings(max_examples=50)
def test_xhtml_urilist_instantiation(instance):
    assert isinstance(instance, XHTML_UriList)

@given(instance=XHTML_URI_strategy)
@settings(max_examples=50)
def test_xhtml_uri_instantiation(instance):
    assert isinstance(instance, XHTML_URI)

@given(instance=XHTML_MediaDesc_strategy)
@settings(max_examples=50)
def test_xhtml_mediadesc_instantiation(instance):
    assert isinstance(instance, XHTML_MediaDesc)

@given(instance=XHTML_LinkTypes_strategy)
@settings(max_examples=50)
def test_xhtml_linktypes_instantiation(instance):
    assert isinstance(instance, XHTML_LinkTypes)

@given(instance=XHTML_Number_strategy)
@settings(max_examples=50)
def test_xhtml_number_instantiation(instance):
    assert isinstance(instance, XHTML_Number)

@given(instance=XHTML_Character_strategy)
@settings(max_examples=50)
def test_xhtml_character_instantiation(instance):
    assert isinstance(instance, XHTML_Character)

@given(instance=NMTOKEN_strategy)
@settings(max_examples=50)
def test_nmtoken_instantiation(instance):
    assert isinstance(instance, NMTOKEN)

@given(instance=XHTML_LanguageCode_strategy)
@settings(max_examples=50)
def test_xhtml_languagecode_instantiation(instance):
    assert isinstance(instance, XHTML_LanguageCode)

@given(instance=Charset_strategy)
@settings(max_examples=50)
def test_charset_instantiation(instance):
    assert isinstance(instance, Charset)

@given(instance=XHTML_Charsets_strategy)
@settings(max_examples=50)
def test_xhtml_charsets_instantiation(instance):
    assert isinstance(instance, XHTML_Charsets)

@given(instance=XHTML_Charset_strategy)
@settings(max_examples=50)
def test_xhtml_charset_instantiation(instance):
    assert isinstance(instance, XHTML_Charset)

@given(instance=ValuedElement_strategy)
@settings(max_examples=50)
def test_valuedelement_instantiation(instance):
    assert isinstance(instance, ValuedElement)

@given(instance=XHTML_IDREF_strategy)
@settings(max_examples=50)
def test_xhtml_idref_instantiation(instance):
    assert isinstance(instance, XHTML_IDREF)

@given(instance=XHTML_NMTOKEN_strategy)
@settings(max_examples=50)
def test_xhtml_nmtoken_instantiation(instance):
    assert isinstance(instance, XHTML_NMTOKEN)

@given(instance=XHTML_ID_strategy)
@settings(max_examples=50)
def test_xhtml_id_instantiation(instance):
    assert isinstance(instance, XHTML_ID)

@given(instance=XHTML_PCDATA_strategy)
@settings(max_examples=50)
def test_xhtml_pcdata_instantiation(instance):
    assert isinstance(instance, XHTML_PCDATA)

@given(instance=XHTML_CDATA_strategy)
@settings(max_examples=50)
def test_xhtml_cdata_instantiation(instance):
    assert isinstance(instance, XHTML_CDATA)

@given(instance=XHTML_ValuedElement_strategy)
@settings(max_examples=50)
def test_xhtml_valuedelement_instantiation(instance):
    assert isinstance(instance, XHTML_ValuedElement)



@given(instance=XHTML_ValuedElement_strategy)
def test_xhtml_valuedelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original
