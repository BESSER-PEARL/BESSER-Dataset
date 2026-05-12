import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    IDREFS,
    XHTML::TrElement,
    TrElement,
    MultiLength,
    Tr,
    Cellvalign,
    Cellhalign,
    Col,
    XHTML::ColElement,
    Tbody,
    XHTML::TableElement,
    Pixels,
    Colgroup,
    TableElement,
    Tfoot,
    Thead,
    ColElement,
    Caption,
    XHTML::Cellvalign,
    XHTML::Cellhalign,
    XHTML::FieldsetElement,
    XHTML::SelectElement,
    Option,
    SelectElement,
    Inlineforms,
    Charsets,
    ContentTypes,
    MapContent,
    XHTML::MapElementContent,
    XHTML::MapElement,
    MapElement,
    XHTML::MapContent,
    UriList,
    XHTML::ObjectElement,
    ValuedElement,
    XHTML::CDATA,
    XHTML::ValuedElement,
    Fontstyle,
    Phrase,
    Focus,
    Specialpre,
    Coords,
    Blocktext,
    Datetime,
    Heading,
    DlElement,
    XHTML::Dt,
    XHTML::Dd,
    Li,
    Lists,
    Miscinline,
    EMPTY,
    XHTML::Base,
    XHTML::TitleBaseHeadElement,
    TitleBaseHeadElement,
    MediaDesc,
    LinkTypes,
    Attrs,
    XHTML::Button,
    XHTML::Ins,
    XHTML::Var,
    XHTML::Area,
    XHTML::Caption,
    XHTML::Blockquote,
    XHTML::Kbd,
    XHTML::Body,
    XHTML::H5,
    XHTML::Samp,
    XHTML::H4,
    XHTML::Code,
    XHTML::H3,
    XHTML::Dfn,
    XHTML::Thead,
    XHTML::H2,
    XHTML::Strong,
    XHTML::Optgroup,
    XHTML::Small,
    XHTML::H1,
    XHTML::Big,
    XHTML::Select,
    XHTML::B,
    XHTML::Dl,
    XHTML::Input,
    XHTML::I,
    XHTML::Tfoot,
    XHTML::Span,
    XHTML::Li,
    XHTML::Td,
    XHTML::Ol,
    XHTML::Tt,
    XHTML::Pre,
    XHTML::Sup,
    XHTML::Label,
    XHTML::Th,
    XHTML::Hr,
    XHTML::Sub,
    XHTML::Ul,
    XHTML::Q,
    XHTML::Address,
    XHTML::H6,
    XHTML::Acronym,
    XHTML::Col,
    XHTML::Abbr,
    XHTML::Cite,
    XHTML::Tr,
    XHTML::DlElement,
    XHTML::Colgroup,
    XHTML::Del,
    XHTML::Em,
    XHTML::Tbody,
    Html,
    HeadElement,
    HeadMisc,
    XHTML::Link,
    XHTML::Meta,
    XHTML::Head,
    XHTML::HeadMisc,
    Body,
    XHTML::BaseHeadElement,
    Base,
    XHTML::BaseTitleHeadElement,
    BaseTitleHeadElement,
    Title,
    XHTML::TitleHeadElement,
    XHTML::HeadElement,
    XHTML::AContent,
    XHTML::Flow,
    XHTML::Block,
    Head,
    XHTML::Html,
    XHTML::ButtonContent,
    XHTML::FormContent,
    XHTML::PreContent,
    AContent,
    ButtonContent,
    inline,
    XHTML::Special,
    PreContent,
    XHTML::Phrase,
    XHTML::A,
    XHTML::Fontstyle,
    Special,
    XHTML::Object,
    XHTML::Img,
    XHTML::Specialpre,
    Number,
    Character,
    XHTML::Focus,
    block,
    XHTML::Blocktext,
    XHTML::Div,
    XHTML::Table,
    XHTML::Fieldset,
    XHTML::Lists,
    XHTML::P,
    XHTML::Heading,
    PCDATA,
    XHTML::Option,
    XHTML::Title,
    XHTML::Script,
    XHTML::Style,
    XHTML::Textarea,
    FieldsetElement,
    XHTML::Legend,
    MapElementContent,
    ObjectElement,
    XHTML::Param,
    FormContent,
    Flow,
    XHTML::Inline,
    Block,
    XHTML::block,
    XHTML::Form,
    XHTML::Misc,
    Inline,
    XHTML::inline,
    Misc,
    XHTML::Noscript,
    XHTML::Miscinline,
    XHTML::Inlineforms,
    ScriptExpression,
    XHTML::Events,
    LanguageCode,
    XHTML::I18n,
    Events,
    I18n,
    XHTML::Map,
    CoreAttrs,
    XHTML::Br,
    XHTML::Bdo,
    XHTML::Attrs,
    URI,
    Text,
    StyleSheet,
    ID,
    XHTML::CoreAttrs,
    Length,
    XHTML::Coords,
    ContentType,
    XHTML::ContentTypes,
    CDATA,
    XHTML::ScriptExpression,
    XHTML::Pixels,
    XHTML::Datetime,
    XHTML::MultiLength,
    XHTML::Length,
    XHTML::StyleSheet,
    XHTML::Text,
    XHTML::ContentType,
    XHTML::EMPTY,
    XHTML::ID,
    IDREF,
    XHTML::IDREFS,
    XHTML::IDREF,
    XHTML::NMTOKEN,
    XHTML::UriList,
    XHTML::URI,
    XHTML::MediaDesc,
    XHTML::LinkTypes,
    XHTML::Number,
    XHTML::Character,
    NMTOKEN,
    XHTML::LanguageCode,
    Charset,
    XHTML::Charsets,
    XHTML::Charset,
    XHTML::PCDATA,
    ButtonType,
    Scope,
    CellHAlign,
    InputType,
    TRules,
    ValueType,
    Shape,
    FomeMethod,
    Direction,
    TFrame,
    CellVAlign,
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



def test_xhtml::trelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::TrElement)


def test_xhtml::trelement_constructor_exists():
    assert callable(XHTML::TrElement.__init__)


def test_xhtml::trelement_constructor_args():
    sig = inspect.signature(XHTML::TrElement.__init__)
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



def test_xhtml::colelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::ColElement)


def test_xhtml::colelement_constructor_exists():
    assert callable(XHTML::ColElement.__init__)


def test_xhtml::colelement_constructor_args():
    sig = inspect.signature(XHTML::ColElement.__init__)
    params = list(sig.parameters.keys())



def test_tbody_is_not_abstract():
    assert not inspect.isabstract(Tbody)


def test_tbody_constructor_exists():
    assert callable(Tbody.__init__)


def test_tbody_constructor_args():
    sig = inspect.signature(Tbody.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::tableelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::TableElement)


def test_xhtml::tableelement_constructor_exists():
    assert callable(XHTML::TableElement.__init__)


def test_xhtml::tableelement_constructor_args():
    sig = inspect.signature(XHTML::TableElement.__init__)
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



def test_xhtml::cellvalign_is_not_abstract():
    assert not inspect.isabstract(XHTML::Cellvalign)


def test_xhtml::cellvalign_constructor_exists():
    assert callable(XHTML::Cellvalign.__init__)


def test_xhtml::cellvalign_constructor_args():
    sig = inspect.signature(XHTML::Cellvalign.__init__)
    params = list(sig.parameters.keys())
    assert "valign" in params, "Missing parameter 'valign'"

def test_xhtml::cellvalign_has_valign():
    assert hasattr(XHTML::Cellvalign, "valign")
    descriptor = None
    for klass in XHTML::Cellvalign.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::cellhalign_is_not_abstract():
    assert not inspect.isabstract(XHTML::Cellhalign)


def test_xhtml::cellhalign_constructor_exists():
    assert callable(XHTML::Cellhalign.__init__)


def test_xhtml::cellhalign_constructor_args():
    sig = inspect.signature(XHTML::Cellhalign.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"

def test_xhtml::cellhalign_has_align():
    assert hasattr(XHTML::Cellhalign, "align")
    descriptor = None
    for klass in XHTML::Cellhalign.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::fieldsetelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::FieldsetElement)


def test_xhtml::fieldsetelement_constructor_exists():
    assert callable(XHTML::FieldsetElement.__init__)


def test_xhtml::fieldsetelement_constructor_args():
    sig = inspect.signature(XHTML::FieldsetElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::selectelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::SelectElement)


def test_xhtml::selectelement_constructor_exists():
    assert callable(XHTML::SelectElement.__init__)


def test_xhtml::selectelement_constructor_args():
    sig = inspect.signature(XHTML::SelectElement.__init__)
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



def test_xhtml::mapelementcontent_is_not_abstract():
    assert not inspect.isabstract(XHTML::MapElementContent)


def test_xhtml::mapelementcontent_constructor_exists():
    assert callable(XHTML::MapElementContent.__init__)


def test_xhtml::mapelementcontent_constructor_args():
    sig = inspect.signature(XHTML::MapElementContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::mapelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::MapElement)


def test_xhtml::mapelement_constructor_exists():
    assert callable(XHTML::MapElement.__init__)


def test_xhtml::mapelement_constructor_args():
    sig = inspect.signature(XHTML::MapElement.__init__)
    params = list(sig.parameters.keys())



def test_mapelement_is_not_abstract():
    assert not inspect.isabstract(MapElement)


def test_mapelement_constructor_exists():
    assert callable(MapElement.__init__)


def test_mapelement_constructor_args():
    sig = inspect.signature(MapElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::mapcontent_is_not_abstract():
    assert not inspect.isabstract(XHTML::MapContent)


def test_xhtml::mapcontent_constructor_exists():
    assert callable(XHTML::MapContent.__init__)


def test_xhtml::mapcontent_constructor_args():
    sig = inspect.signature(XHTML::MapContent.__init__)
    params = list(sig.parameters.keys())



def test_urilist_is_not_abstract():
    assert not inspect.isabstract(UriList)


def test_urilist_constructor_exists():
    assert callable(UriList.__init__)


def test_urilist_constructor_args():
    sig = inspect.signature(UriList.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::objectelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::ObjectElement)


def test_xhtml::objectelement_constructor_exists():
    assert callable(XHTML::ObjectElement.__init__)


def test_xhtml::objectelement_constructor_args():
    sig = inspect.signature(XHTML::ObjectElement.__init__)
    params = list(sig.parameters.keys())



def test_valuedelement_is_not_abstract():
    assert not inspect.isabstract(ValuedElement)


def test_valuedelement_constructor_exists():
    assert callable(ValuedElement.__init__)


def test_valuedelement_constructor_args():
    sig = inspect.signature(ValuedElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::cdata_is_not_abstract():
    assert not inspect.isabstract(XHTML::CDATA)


def test_xhtml::cdata_constructor_exists():
    assert callable(XHTML::CDATA.__init__)


def test_xhtml::cdata_constructor_args():
    sig = inspect.signature(XHTML::CDATA.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::valuedelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::ValuedElement)


def test_xhtml::valuedelement_constructor_exists():
    assert callable(XHTML::ValuedElement.__init__)


def test_xhtml::valuedelement_constructor_args():
    sig = inspect.signature(XHTML::ValuedElement.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_xhtml::valuedelement_has_value():
    assert hasattr(XHTML::ValuedElement, "value")
    descriptor = None
    for klass in XHTML::ValuedElement.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



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



def test_xhtml::dt_is_not_abstract():
    assert not inspect.isabstract(XHTML::Dt)


def test_xhtml::dt_constructor_exists():
    assert callable(XHTML::Dt.__init__)


def test_xhtml::dt_constructor_args():
    sig = inspect.signature(XHTML::Dt.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::dd_is_not_abstract():
    assert not inspect.isabstract(XHTML::Dd)


def test_xhtml::dd_constructor_exists():
    assert callable(XHTML::Dd.__init__)


def test_xhtml::dd_constructor_args():
    sig = inspect.signature(XHTML::Dd.__init__)
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



def test_xhtml::base_is_not_abstract():
    assert not inspect.isabstract(XHTML::Base)


def test_xhtml::base_constructor_exists():
    assert callable(XHTML::Base.__init__)


def test_xhtml::base_constructor_args():
    sig = inspect.signature(XHTML::Base.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::titlebaseheadelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::TitleBaseHeadElement)


def test_xhtml::titlebaseheadelement_constructor_exists():
    assert callable(XHTML::TitleBaseHeadElement.__init__)


def test_xhtml::titlebaseheadelement_constructor_args():
    sig = inspect.signature(XHTML::TitleBaseHeadElement.__init__)
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



def test_xhtml::button_is_not_abstract():
    assert not inspect.isabstract(XHTML::Button)


def test_xhtml::button_constructor_exists():
    assert callable(XHTML::Button.__init__)


def test_xhtml::button_constructor_args():
    sig = inspect.signature(XHTML::Button.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "type" in params, "Missing parameter 'type'"

def test_xhtml::button_has_disabled():
    assert hasattr(XHTML::Button, "disabled")
    descriptor = None
    for klass in XHTML::Button.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::button_has_type():
    assert hasattr(XHTML::Button, "type")
    descriptor = None
    for klass in XHTML::Button.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::ins_is_not_abstract():
    assert not inspect.isabstract(XHTML::Ins)


def test_xhtml::ins_constructor_exists():
    assert callable(XHTML::Ins.__init__)


def test_xhtml::ins_constructor_args():
    sig = inspect.signature(XHTML::Ins.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::var_is_not_abstract():
    assert not inspect.isabstract(XHTML::Var)


def test_xhtml::var_constructor_exists():
    assert callable(XHTML::Var.__init__)


def test_xhtml::var_constructor_args():
    sig = inspect.signature(XHTML::Var.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::area_is_not_abstract():
    assert not inspect.isabstract(XHTML::Area)


def test_xhtml::area_constructor_exists():
    assert callable(XHTML::Area.__init__)


def test_xhtml::area_constructor_args():
    sig = inspect.signature(XHTML::Area.__init__)
    params = list(sig.parameters.keys())
    assert "nohref" in params, "Missing parameter 'nohref'"
    assert "shape" in params, "Missing parameter 'shape'"

def test_xhtml::area_has_nohref():
    assert hasattr(XHTML::Area, "nohref")
    descriptor = None
    for klass in XHTML::Area.__mro__:
        if "nohref" in klass.__dict__:
            descriptor = klass.__dict__["nohref"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::area_has_shape():
    assert hasattr(XHTML::Area, "shape")
    descriptor = None
    for klass in XHTML::Area.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::caption_is_not_abstract():
    assert not inspect.isabstract(XHTML::Caption)


def test_xhtml::caption_constructor_exists():
    assert callable(XHTML::Caption.__init__)


def test_xhtml::caption_constructor_args():
    sig = inspect.signature(XHTML::Caption.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::blockquote_is_not_abstract():
    assert not inspect.isabstract(XHTML::Blockquote)


def test_xhtml::blockquote_constructor_exists():
    assert callable(XHTML::Blockquote.__init__)


def test_xhtml::blockquote_constructor_args():
    sig = inspect.signature(XHTML::Blockquote.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::kbd_is_not_abstract():
    assert not inspect.isabstract(XHTML::Kbd)


def test_xhtml::kbd_constructor_exists():
    assert callable(XHTML::Kbd.__init__)


def test_xhtml::kbd_constructor_args():
    sig = inspect.signature(XHTML::Kbd.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::body_is_not_abstract():
    assert not inspect.isabstract(XHTML::Body)


def test_xhtml::body_constructor_exists():
    assert callable(XHTML::Body.__init__)


def test_xhtml::body_constructor_args():
    sig = inspect.signature(XHTML::Body.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::h5_is_not_abstract():
    assert not inspect.isabstract(XHTML::H5)


def test_xhtml::h5_constructor_exists():
    assert callable(XHTML::H5.__init__)


def test_xhtml::h5_constructor_args():
    sig = inspect.signature(XHTML::H5.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::samp_is_not_abstract():
    assert not inspect.isabstract(XHTML::Samp)


def test_xhtml::samp_constructor_exists():
    assert callable(XHTML::Samp.__init__)


def test_xhtml::samp_constructor_args():
    sig = inspect.signature(XHTML::Samp.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::h4_is_not_abstract():
    assert not inspect.isabstract(XHTML::H4)


def test_xhtml::h4_constructor_exists():
    assert callable(XHTML::H4.__init__)


def test_xhtml::h4_constructor_args():
    sig = inspect.signature(XHTML::H4.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::code_is_not_abstract():
    assert not inspect.isabstract(XHTML::Code)


def test_xhtml::code_constructor_exists():
    assert callable(XHTML::Code.__init__)


def test_xhtml::code_constructor_args():
    sig = inspect.signature(XHTML::Code.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::h3_is_not_abstract():
    assert not inspect.isabstract(XHTML::H3)


def test_xhtml::h3_constructor_exists():
    assert callable(XHTML::H3.__init__)


def test_xhtml::h3_constructor_args():
    sig = inspect.signature(XHTML::H3.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::dfn_is_not_abstract():
    assert not inspect.isabstract(XHTML::Dfn)


def test_xhtml::dfn_constructor_exists():
    assert callable(XHTML::Dfn.__init__)


def test_xhtml::dfn_constructor_args():
    sig = inspect.signature(XHTML::Dfn.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::thead_is_not_abstract():
    assert not inspect.isabstract(XHTML::Thead)


def test_xhtml::thead_constructor_exists():
    assert callable(XHTML::Thead.__init__)


def test_xhtml::thead_constructor_args():
    sig = inspect.signature(XHTML::Thead.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::h2_is_not_abstract():
    assert not inspect.isabstract(XHTML::H2)


def test_xhtml::h2_constructor_exists():
    assert callable(XHTML::H2.__init__)


def test_xhtml::h2_constructor_args():
    sig = inspect.signature(XHTML::H2.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::strong_is_not_abstract():
    assert not inspect.isabstract(XHTML::Strong)


def test_xhtml::strong_constructor_exists():
    assert callable(XHTML::Strong.__init__)


def test_xhtml::strong_constructor_args():
    sig = inspect.signature(XHTML::Strong.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::optgroup_is_not_abstract():
    assert not inspect.isabstract(XHTML::Optgroup)


def test_xhtml::optgroup_constructor_exists():
    assert callable(XHTML::Optgroup.__init__)


def test_xhtml::optgroup_constructor_args():
    sig = inspect.signature(XHTML::Optgroup.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"

def test_xhtml::optgroup_has_disabled():
    assert hasattr(XHTML::Optgroup, "disabled")
    descriptor = None
    for klass in XHTML::Optgroup.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::small_is_not_abstract():
    assert not inspect.isabstract(XHTML::Small)


def test_xhtml::small_constructor_exists():
    assert callable(XHTML::Small.__init__)


def test_xhtml::small_constructor_args():
    sig = inspect.signature(XHTML::Small.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::h1_is_not_abstract():
    assert not inspect.isabstract(XHTML::H1)


def test_xhtml::h1_constructor_exists():
    assert callable(XHTML::H1.__init__)


def test_xhtml::h1_constructor_args():
    sig = inspect.signature(XHTML::H1.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::big_is_not_abstract():
    assert not inspect.isabstract(XHTML::Big)


def test_xhtml::big_constructor_exists():
    assert callable(XHTML::Big.__init__)


def test_xhtml::big_constructor_args():
    sig = inspect.signature(XHTML::Big.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::select_is_not_abstract():
    assert not inspect.isabstract(XHTML::Select)


def test_xhtml::select_constructor_exists():
    assert callable(XHTML::Select.__init__)


def test_xhtml::select_constructor_args():
    sig = inspect.signature(XHTML::Select.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "multiple" in params, "Missing parameter 'multiple'"

def test_xhtml::select_has_disabled():
    assert hasattr(XHTML::Select, "disabled")
    descriptor = None
    for klass in XHTML::Select.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::select_has_multiple():
    assert hasattr(XHTML::Select, "multiple")
    descriptor = None
    for klass in XHTML::Select.__mro__:
        if "multiple" in klass.__dict__:
            descriptor = klass.__dict__["multiple"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::b_is_not_abstract():
    assert not inspect.isabstract(XHTML::B)


def test_xhtml::b_constructor_exists():
    assert callable(XHTML::B.__init__)


def test_xhtml::b_constructor_args():
    sig = inspect.signature(XHTML::B.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::dl_is_not_abstract():
    assert not inspect.isabstract(XHTML::Dl)


def test_xhtml::dl_constructor_exists():
    assert callable(XHTML::Dl.__init__)


def test_xhtml::dl_constructor_args():
    sig = inspect.signature(XHTML::Dl.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::input_is_not_abstract():
    assert not inspect.isabstract(XHTML::Input)


def test_xhtml::input_constructor_exists():
    assert callable(XHTML::Input.__init__)


def test_xhtml::input_constructor_args():
    sig = inspect.signature(XHTML::Input.__init__)
    params = list(sig.parameters.keys())
    assert "readonly" in params, "Missing parameter 'readonly'"
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "checked" in params, "Missing parameter 'checked'"
    assert "type" in params, "Missing parameter 'type'"

def test_xhtml::input_has_readonly():
    assert hasattr(XHTML::Input, "readonly")
    descriptor = None
    for klass in XHTML::Input.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::input_has_disabled():
    assert hasattr(XHTML::Input, "disabled")
    descriptor = None
    for klass in XHTML::Input.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::input_has_checked():
    assert hasattr(XHTML::Input, "checked")
    descriptor = None
    for klass in XHTML::Input.__mro__:
        if "checked" in klass.__dict__:
            descriptor = klass.__dict__["checked"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::input_has_type():
    assert hasattr(XHTML::Input, "type")
    descriptor = None
    for klass in XHTML::Input.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::i_is_not_abstract():
    assert not inspect.isabstract(XHTML::I)


def test_xhtml::i_constructor_exists():
    assert callable(XHTML::I.__init__)


def test_xhtml::i_constructor_args():
    sig = inspect.signature(XHTML::I.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::tfoot_is_not_abstract():
    assert not inspect.isabstract(XHTML::Tfoot)


def test_xhtml::tfoot_constructor_exists():
    assert callable(XHTML::Tfoot.__init__)


def test_xhtml::tfoot_constructor_args():
    sig = inspect.signature(XHTML::Tfoot.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::span_is_not_abstract():
    assert not inspect.isabstract(XHTML::Span)


def test_xhtml::span_constructor_exists():
    assert callable(XHTML::Span.__init__)


def test_xhtml::span_constructor_args():
    sig = inspect.signature(XHTML::Span.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::li_is_not_abstract():
    assert not inspect.isabstract(XHTML::Li)


def test_xhtml::li_constructor_exists():
    assert callable(XHTML::Li.__init__)


def test_xhtml::li_constructor_args():
    sig = inspect.signature(XHTML::Li.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::td_is_not_abstract():
    assert not inspect.isabstract(XHTML::Td)


def test_xhtml::td_constructor_exists():
    assert callable(XHTML::Td.__init__)


def test_xhtml::td_constructor_args():
    sig = inspect.signature(XHTML::Td.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_xhtml::td_has_scope():
    assert hasattr(XHTML::Td, "scope")
    descriptor = None
    for klass in XHTML::Td.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::ol_is_not_abstract():
    assert not inspect.isabstract(XHTML::Ol)


def test_xhtml::ol_constructor_exists():
    assert callable(XHTML::Ol.__init__)


def test_xhtml::ol_constructor_args():
    sig = inspect.signature(XHTML::Ol.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::tt_is_not_abstract():
    assert not inspect.isabstract(XHTML::Tt)


def test_xhtml::tt_constructor_exists():
    assert callable(XHTML::Tt.__init__)


def test_xhtml::tt_constructor_args():
    sig = inspect.signature(XHTML::Tt.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::pre_is_not_abstract():
    assert not inspect.isabstract(XHTML::Pre)


def test_xhtml::pre_constructor_exists():
    assert callable(XHTML::Pre.__init__)


def test_xhtml::pre_constructor_args():
    sig = inspect.signature(XHTML::Pre.__init__)
    params = list(sig.parameters.keys())
    assert "xml_space" in params, "Missing parameter 'xml_space'"

def test_xhtml::pre_has_xml_space():
    assert hasattr(XHTML::Pre, "xml_space")
    descriptor = None
    for klass in XHTML::Pre.__mro__:
        if "xml_space" in klass.__dict__:
            descriptor = klass.__dict__["xml_space"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::sup_is_not_abstract():
    assert not inspect.isabstract(XHTML::Sup)


def test_xhtml::sup_constructor_exists():
    assert callable(XHTML::Sup.__init__)


def test_xhtml::sup_constructor_args():
    sig = inspect.signature(XHTML::Sup.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::label_is_not_abstract():
    assert not inspect.isabstract(XHTML::Label)


def test_xhtml::label_constructor_exists():
    assert callable(XHTML::Label.__init__)


def test_xhtml::label_constructor_args():
    sig = inspect.signature(XHTML::Label.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::th_is_not_abstract():
    assert not inspect.isabstract(XHTML::Th)


def test_xhtml::th_constructor_exists():
    assert callable(XHTML::Th.__init__)


def test_xhtml::th_constructor_args():
    sig = inspect.signature(XHTML::Th.__init__)
    params = list(sig.parameters.keys())
    assert "scope" in params, "Missing parameter 'scope'"

def test_xhtml::th_has_scope():
    assert hasattr(XHTML::Th, "scope")
    descriptor = None
    for klass in XHTML::Th.__mro__:
        if "scope" in klass.__dict__:
            descriptor = klass.__dict__["scope"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::hr_is_not_abstract():
    assert not inspect.isabstract(XHTML::Hr)


def test_xhtml::hr_constructor_exists():
    assert callable(XHTML::Hr.__init__)


def test_xhtml::hr_constructor_args():
    sig = inspect.signature(XHTML::Hr.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::sub_is_not_abstract():
    assert not inspect.isabstract(XHTML::Sub)


def test_xhtml::sub_constructor_exists():
    assert callable(XHTML::Sub.__init__)


def test_xhtml::sub_constructor_args():
    sig = inspect.signature(XHTML::Sub.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::ul_is_not_abstract():
    assert not inspect.isabstract(XHTML::Ul)


def test_xhtml::ul_constructor_exists():
    assert callable(XHTML::Ul.__init__)


def test_xhtml::ul_constructor_args():
    sig = inspect.signature(XHTML::Ul.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::q_is_not_abstract():
    assert not inspect.isabstract(XHTML::Q)


def test_xhtml::q_constructor_exists():
    assert callable(XHTML::Q.__init__)


def test_xhtml::q_constructor_args():
    sig = inspect.signature(XHTML::Q.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::address_is_not_abstract():
    assert not inspect.isabstract(XHTML::Address)


def test_xhtml::address_constructor_exists():
    assert callable(XHTML::Address.__init__)


def test_xhtml::address_constructor_args():
    sig = inspect.signature(XHTML::Address.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::h6_is_not_abstract():
    assert not inspect.isabstract(XHTML::H6)


def test_xhtml::h6_constructor_exists():
    assert callable(XHTML::H6.__init__)


def test_xhtml::h6_constructor_args():
    sig = inspect.signature(XHTML::H6.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::acronym_is_not_abstract():
    assert not inspect.isabstract(XHTML::Acronym)


def test_xhtml::acronym_constructor_exists():
    assert callable(XHTML::Acronym.__init__)


def test_xhtml::acronym_constructor_args():
    sig = inspect.signature(XHTML::Acronym.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::col_is_not_abstract():
    assert not inspect.isabstract(XHTML::Col)


def test_xhtml::col_constructor_exists():
    assert callable(XHTML::Col.__init__)


def test_xhtml::col_constructor_args():
    sig = inspect.signature(XHTML::Col.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::abbr_is_not_abstract():
    assert not inspect.isabstract(XHTML::Abbr)


def test_xhtml::abbr_constructor_exists():
    assert callable(XHTML::Abbr.__init__)


def test_xhtml::abbr_constructor_args():
    sig = inspect.signature(XHTML::Abbr.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::cite_is_not_abstract():
    assert not inspect.isabstract(XHTML::Cite)


def test_xhtml::cite_constructor_exists():
    assert callable(XHTML::Cite.__init__)


def test_xhtml::cite_constructor_args():
    sig = inspect.signature(XHTML::Cite.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::tr_is_not_abstract():
    assert not inspect.isabstract(XHTML::Tr)


def test_xhtml::tr_constructor_exists():
    assert callable(XHTML::Tr.__init__)


def test_xhtml::tr_constructor_args():
    sig = inspect.signature(XHTML::Tr.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::dlelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::DlElement)


def test_xhtml::dlelement_constructor_exists():
    assert callable(XHTML::DlElement.__init__)


def test_xhtml::dlelement_constructor_args():
    sig = inspect.signature(XHTML::DlElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::colgroup_is_not_abstract():
    assert not inspect.isabstract(XHTML::Colgroup)


def test_xhtml::colgroup_constructor_exists():
    assert callable(XHTML::Colgroup.__init__)


def test_xhtml::colgroup_constructor_args():
    sig = inspect.signature(XHTML::Colgroup.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::del_is_not_abstract():
    assert not inspect.isabstract(XHTML::Del)


def test_xhtml::del_constructor_exists():
    assert callable(XHTML::Del.__init__)


def test_xhtml::del_constructor_args():
    sig = inspect.signature(XHTML::Del.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::em_is_not_abstract():
    assert not inspect.isabstract(XHTML::Em)


def test_xhtml::em_constructor_exists():
    assert callable(XHTML::Em.__init__)


def test_xhtml::em_constructor_args():
    sig = inspect.signature(XHTML::Em.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::tbody_is_not_abstract():
    assert not inspect.isabstract(XHTML::Tbody)


def test_xhtml::tbody_constructor_exists():
    assert callable(XHTML::Tbody.__init__)


def test_xhtml::tbody_constructor_args():
    sig = inspect.signature(XHTML::Tbody.__init__)
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



def test_xhtml::link_is_not_abstract():
    assert not inspect.isabstract(XHTML::Link)


def test_xhtml::link_constructor_exists():
    assert callable(XHTML::Link.__init__)


def test_xhtml::link_constructor_args():
    sig = inspect.signature(XHTML::Link.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::meta_is_not_abstract():
    assert not inspect.isabstract(XHTML::Meta)


def test_xhtml::meta_constructor_exists():
    assert callable(XHTML::Meta.__init__)


def test_xhtml::meta_constructor_args():
    sig = inspect.signature(XHTML::Meta.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::head_is_not_abstract():
    assert not inspect.isabstract(XHTML::Head)


def test_xhtml::head_constructor_exists():
    assert callable(XHTML::Head.__init__)


def test_xhtml::head_constructor_args():
    sig = inspect.signature(XHTML::Head.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::headmisc_is_not_abstract():
    assert not inspect.isabstract(XHTML::HeadMisc)


def test_xhtml::headmisc_constructor_exists():
    assert callable(XHTML::HeadMisc.__init__)


def test_xhtml::headmisc_constructor_args():
    sig = inspect.signature(XHTML::HeadMisc.__init__)
    params = list(sig.parameters.keys())



def test_body_is_not_abstract():
    assert not inspect.isabstract(Body)


def test_body_constructor_exists():
    assert callable(Body.__init__)


def test_body_constructor_args():
    sig = inspect.signature(Body.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::baseheadelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::BaseHeadElement)


def test_xhtml::baseheadelement_constructor_exists():
    assert callable(XHTML::BaseHeadElement.__init__)


def test_xhtml::baseheadelement_constructor_args():
    sig = inspect.signature(XHTML::BaseHeadElement.__init__)
    params = list(sig.parameters.keys())



def test_base_is_not_abstract():
    assert not inspect.isabstract(Base)


def test_base_constructor_exists():
    assert callable(Base.__init__)


def test_base_constructor_args():
    sig = inspect.signature(Base.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::basetitleheadelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::BaseTitleHeadElement)


def test_xhtml::basetitleheadelement_constructor_exists():
    assert callable(XHTML::BaseTitleHeadElement.__init__)


def test_xhtml::basetitleheadelement_constructor_args():
    sig = inspect.signature(XHTML::BaseTitleHeadElement.__init__)
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



def test_xhtml::titleheadelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::TitleHeadElement)


def test_xhtml::titleheadelement_constructor_exists():
    assert callable(XHTML::TitleHeadElement.__init__)


def test_xhtml::titleheadelement_constructor_args():
    sig = inspect.signature(XHTML::TitleHeadElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::headelement_is_not_abstract():
    assert not inspect.isabstract(XHTML::HeadElement)


def test_xhtml::headelement_constructor_exists():
    assert callable(XHTML::HeadElement.__init__)


def test_xhtml::headelement_constructor_args():
    sig = inspect.signature(XHTML::HeadElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::acontent_is_not_abstract():
    assert not inspect.isabstract(XHTML::AContent)


def test_xhtml::acontent_constructor_exists():
    assert callable(XHTML::AContent.__init__)


def test_xhtml::acontent_constructor_args():
    sig = inspect.signature(XHTML::AContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::flow_is_not_abstract():
    assert not inspect.isabstract(XHTML::Flow)


def test_xhtml::flow_constructor_exists():
    assert callable(XHTML::Flow.__init__)


def test_xhtml::flow_constructor_args():
    sig = inspect.signature(XHTML::Flow.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::block_is_not_abstract():
    assert not inspect.isabstract(XHTML::Block)


def test_xhtml::block_constructor_exists():
    assert callable(XHTML::Block.__init__)


def test_xhtml::block_constructor_args():
    sig = inspect.signature(XHTML::Block.__init__)
    params = list(sig.parameters.keys())



def test_head_is_not_abstract():
    assert not inspect.isabstract(Head)


def test_head_constructor_exists():
    assert callable(Head.__init__)


def test_head_constructor_args():
    sig = inspect.signature(Head.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::html_is_not_abstract():
    assert not inspect.isabstract(XHTML::Html)


def test_xhtml::html_constructor_exists():
    assert callable(XHTML::Html.__init__)


def test_xhtml::html_constructor_args():
    sig = inspect.signature(XHTML::Html.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::buttoncontent_is_not_abstract():
    assert not inspect.isabstract(XHTML::ButtonContent)


def test_xhtml::buttoncontent_constructor_exists():
    assert callable(XHTML::ButtonContent.__init__)


def test_xhtml::buttoncontent_constructor_args():
    sig = inspect.signature(XHTML::ButtonContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::formcontent_is_not_abstract():
    assert not inspect.isabstract(XHTML::FormContent)


def test_xhtml::formcontent_constructor_exists():
    assert callable(XHTML::FormContent.__init__)


def test_xhtml::formcontent_constructor_args():
    sig = inspect.signature(XHTML::FormContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::precontent_is_not_abstract():
    assert not inspect.isabstract(XHTML::PreContent)


def test_xhtml::precontent_constructor_exists():
    assert callable(XHTML::PreContent.__init__)


def test_xhtml::precontent_constructor_args():
    sig = inspect.signature(XHTML::PreContent.__init__)
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



def test_xhtml::special_is_not_abstract():
    assert not inspect.isabstract(XHTML::Special)


def test_xhtml::special_constructor_exists():
    assert callable(XHTML::Special.__init__)


def test_xhtml::special_constructor_args():
    sig = inspect.signature(XHTML::Special.__init__)
    params = list(sig.parameters.keys())



def test_precontent_is_not_abstract():
    assert not inspect.isabstract(PreContent)


def test_precontent_constructor_exists():
    assert callable(PreContent.__init__)


def test_precontent_constructor_args():
    sig = inspect.signature(PreContent.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::phrase_is_not_abstract():
    assert not inspect.isabstract(XHTML::Phrase)


def test_xhtml::phrase_constructor_exists():
    assert callable(XHTML::Phrase.__init__)


def test_xhtml::phrase_constructor_args():
    sig = inspect.signature(XHTML::Phrase.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::a_is_not_abstract():
    assert not inspect.isabstract(XHTML::A)


def test_xhtml::a_constructor_exists():
    assert callable(XHTML::A.__init__)


def test_xhtml::a_constructor_args():
    sig = inspect.signature(XHTML::A.__init__)
    params = list(sig.parameters.keys())
    assert "shape" in params, "Missing parameter 'shape'"

def test_xhtml::a_has_shape():
    assert hasattr(XHTML::A, "shape")
    descriptor = None
    for klass in XHTML::A.__mro__:
        if "shape" in klass.__dict__:
            descriptor = klass.__dict__["shape"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::fontstyle_is_not_abstract():
    assert not inspect.isabstract(XHTML::Fontstyle)


def test_xhtml::fontstyle_constructor_exists():
    assert callable(XHTML::Fontstyle.__init__)


def test_xhtml::fontstyle_constructor_args():
    sig = inspect.signature(XHTML::Fontstyle.__init__)
    params = list(sig.parameters.keys())



def test_special_is_not_abstract():
    assert not inspect.isabstract(Special)


def test_special_constructor_exists():
    assert callable(Special.__init__)


def test_special_constructor_args():
    sig = inspect.signature(Special.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::object_is_not_abstract():
    assert not inspect.isabstract(XHTML::Object)


def test_xhtml::object_constructor_exists():
    assert callable(XHTML::Object.__init__)


def test_xhtml::object_constructor_args():
    sig = inspect.signature(XHTML::Object.__init__)
    params = list(sig.parameters.keys())
    assert "declare" in params, "Missing parameter 'declare'"

def test_xhtml::object_has_declare():
    assert hasattr(XHTML::Object, "declare")
    descriptor = None
    for klass in XHTML::Object.__mro__:
        if "declare" in klass.__dict__:
            descriptor = klass.__dict__["declare"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::img_is_not_abstract():
    assert not inspect.isabstract(XHTML::Img)


def test_xhtml::img_constructor_exists():
    assert callable(XHTML::Img.__init__)


def test_xhtml::img_constructor_args():
    sig = inspect.signature(XHTML::Img.__init__)
    params = list(sig.parameters.keys())
    assert "ismap" in params, "Missing parameter 'ismap'"

def test_xhtml::img_has_ismap():
    assert hasattr(XHTML::Img, "ismap")
    descriptor = None
    for klass in XHTML::Img.__mro__:
        if "ismap" in klass.__dict__:
            descriptor = klass.__dict__["ismap"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::specialpre_is_not_abstract():
    assert not inspect.isabstract(XHTML::Specialpre)


def test_xhtml::specialpre_constructor_exists():
    assert callable(XHTML::Specialpre.__init__)


def test_xhtml::specialpre_constructor_args():
    sig = inspect.signature(XHTML::Specialpre.__init__)
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



def test_xhtml::focus_is_not_abstract():
    assert not inspect.isabstract(XHTML::Focus)


def test_xhtml::focus_constructor_exists():
    assert callable(XHTML::Focus.__init__)


def test_xhtml::focus_constructor_args():
    sig = inspect.signature(XHTML::Focus.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(block)


def test_block_constructor_exists():
    assert callable(block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(block.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::blocktext_is_not_abstract():
    assert not inspect.isabstract(XHTML::Blocktext)


def test_xhtml::blocktext_constructor_exists():
    assert callable(XHTML::Blocktext.__init__)


def test_xhtml::blocktext_constructor_args():
    sig = inspect.signature(XHTML::Blocktext.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::div_is_not_abstract():
    assert not inspect.isabstract(XHTML::Div)


def test_xhtml::div_constructor_exists():
    assert callable(XHTML::Div.__init__)


def test_xhtml::div_constructor_args():
    sig = inspect.signature(XHTML::Div.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::table_is_not_abstract():
    assert not inspect.isabstract(XHTML::Table)


def test_xhtml::table_constructor_exists():
    assert callable(XHTML::Table.__init__)


def test_xhtml::table_constructor_args():
    sig = inspect.signature(XHTML::Table.__init__)
    params = list(sig.parameters.keys())
    assert "frame" in params, "Missing parameter 'frame'"
    assert "rules" in params, "Missing parameter 'rules'"

def test_xhtml::table_has_frame():
    assert hasattr(XHTML::Table, "frame")
    descriptor = None
    for klass in XHTML::Table.__mro__:
        if "frame" in klass.__dict__:
            descriptor = klass.__dict__["frame"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::table_has_rules():
    assert hasattr(XHTML::Table, "rules")
    descriptor = None
    for klass in XHTML::Table.__mro__:
        if "rules" in klass.__dict__:
            descriptor = klass.__dict__["rules"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::fieldset_is_not_abstract():
    assert not inspect.isabstract(XHTML::Fieldset)


def test_xhtml::fieldset_constructor_exists():
    assert callable(XHTML::Fieldset.__init__)


def test_xhtml::fieldset_constructor_args():
    sig = inspect.signature(XHTML::Fieldset.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::lists_is_not_abstract():
    assert not inspect.isabstract(XHTML::Lists)


def test_xhtml::lists_constructor_exists():
    assert callable(XHTML::Lists.__init__)


def test_xhtml::lists_constructor_args():
    sig = inspect.signature(XHTML::Lists.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::p_is_not_abstract():
    assert not inspect.isabstract(XHTML::P)


def test_xhtml::p_constructor_exists():
    assert callable(XHTML::P.__init__)


def test_xhtml::p_constructor_args():
    sig = inspect.signature(XHTML::P.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::heading_is_not_abstract():
    assert not inspect.isabstract(XHTML::Heading)


def test_xhtml::heading_constructor_exists():
    assert callable(XHTML::Heading.__init__)


def test_xhtml::heading_constructor_args():
    sig = inspect.signature(XHTML::Heading.__init__)
    params = list(sig.parameters.keys())



def test_pcdata_is_not_abstract():
    assert not inspect.isabstract(PCDATA)


def test_pcdata_constructor_exists():
    assert callable(PCDATA.__init__)


def test_pcdata_constructor_args():
    sig = inspect.signature(PCDATA.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::option_is_not_abstract():
    assert not inspect.isabstract(XHTML::Option)


def test_xhtml::option_constructor_exists():
    assert callable(XHTML::Option.__init__)


def test_xhtml::option_constructor_args():
    sig = inspect.signature(XHTML::Option.__init__)
    params = list(sig.parameters.keys())
    assert "selected" in params, "Missing parameter 'selected'"
    assert "disabled" in params, "Missing parameter 'disabled'"

def test_xhtml::option_has_selected():
    assert hasattr(XHTML::Option, "selected")
    descriptor = None
    for klass in XHTML::Option.__mro__:
        if "selected" in klass.__dict__:
            descriptor = klass.__dict__["selected"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::option_has_disabled():
    assert hasattr(XHTML::Option, "disabled")
    descriptor = None
    for klass in XHTML::Option.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::title_is_not_abstract():
    assert not inspect.isabstract(XHTML::Title)


def test_xhtml::title_constructor_exists():
    assert callable(XHTML::Title.__init__)


def test_xhtml::title_constructor_args():
    sig = inspect.signature(XHTML::Title.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::script_is_not_abstract():
    assert not inspect.isabstract(XHTML::Script)


def test_xhtml::script_constructor_exists():
    assert callable(XHTML::Script.__init__)


def test_xhtml::script_constructor_args():
    sig = inspect.signature(XHTML::Script.__init__)
    params = list(sig.parameters.keys())
    assert "xml_space" in params, "Missing parameter 'xml_space'"
    assert "defer" in params, "Missing parameter 'defer'"

def test_xhtml::script_has_xml_space():
    assert hasattr(XHTML::Script, "xml_space")
    descriptor = None
    for klass in XHTML::Script.__mro__:
        if "xml_space" in klass.__dict__:
            descriptor = klass.__dict__["xml_space"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::script_has_defer():
    assert hasattr(XHTML::Script, "defer")
    descriptor = None
    for klass in XHTML::Script.__mro__:
        if "defer" in klass.__dict__:
            descriptor = klass.__dict__["defer"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::style_is_not_abstract():
    assert not inspect.isabstract(XHTML::Style)


def test_xhtml::style_constructor_exists():
    assert callable(XHTML::Style.__init__)


def test_xhtml::style_constructor_args():
    sig = inspect.signature(XHTML::Style.__init__)
    params = list(sig.parameters.keys())
    assert "xml_space" in params, "Missing parameter 'xml_space'"

def test_xhtml::style_has_xml_space():
    assert hasattr(XHTML::Style, "xml_space")
    descriptor = None
    for klass in XHTML::Style.__mro__:
        if "xml_space" in klass.__dict__:
            descriptor = klass.__dict__["xml_space"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::textarea_is_not_abstract():
    assert not inspect.isabstract(XHTML::Textarea)


def test_xhtml::textarea_constructor_exists():
    assert callable(XHTML::Textarea.__init__)


def test_xhtml::textarea_constructor_args():
    sig = inspect.signature(XHTML::Textarea.__init__)
    params = list(sig.parameters.keys())
    assert "disabled" in params, "Missing parameter 'disabled'"
    assert "readonly" in params, "Missing parameter 'readonly'"

def test_xhtml::textarea_has_disabled():
    assert hasattr(XHTML::Textarea, "disabled")
    descriptor = None
    for klass in XHTML::Textarea.__mro__:
        if "disabled" in klass.__dict__:
            descriptor = klass.__dict__["disabled"]
            break
    assert isinstance(descriptor, property)

def test_xhtml::textarea_has_readonly():
    assert hasattr(XHTML::Textarea, "readonly")
    descriptor = None
    for klass in XHTML::Textarea.__mro__:
        if "readonly" in klass.__dict__:
            descriptor = klass.__dict__["readonly"]
            break
    assert isinstance(descriptor, property)



def test_fieldsetelement_is_not_abstract():
    assert not inspect.isabstract(FieldsetElement)


def test_fieldsetelement_constructor_exists():
    assert callable(FieldsetElement.__init__)


def test_fieldsetelement_constructor_args():
    sig = inspect.signature(FieldsetElement.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::legend_is_not_abstract():
    assert not inspect.isabstract(XHTML::Legend)


def test_xhtml::legend_constructor_exists():
    assert callable(XHTML::Legend.__init__)


def test_xhtml::legend_constructor_args():
    sig = inspect.signature(XHTML::Legend.__init__)
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



def test_xhtml::param_is_not_abstract():
    assert not inspect.isabstract(XHTML::Param)


def test_xhtml::param_constructor_exists():
    assert callable(XHTML::Param.__init__)


def test_xhtml::param_constructor_args():
    sig = inspect.signature(XHTML::Param.__init__)
    params = list(sig.parameters.keys())
    assert "valuetype" in params, "Missing parameter 'valuetype'"

def test_xhtml::param_has_valuetype():
    assert hasattr(XHTML::Param, "valuetype")
    descriptor = None
    for klass in XHTML::Param.__mro__:
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



def test_xhtml::inline_is_not_abstract():
    assert not inspect.isabstract(XHTML::Inline)


def test_xhtml::inline_constructor_exists():
    assert callable(XHTML::Inline.__init__)


def test_xhtml::inline_constructor_args():
    sig = inspect.signature(XHTML::Inline.__init__)
    params = list(sig.parameters.keys())



def test_block_is_not_abstract():
    assert not inspect.isabstract(Block)


def test_block_constructor_exists():
    assert callable(Block.__init__)


def test_block_constructor_args():
    sig = inspect.signature(Block.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::block_is_not_abstract():
    assert not inspect.isabstract(XHTML::block)


def test_xhtml::block_constructor_exists():
    assert callable(XHTML::block.__init__)


def test_xhtml::block_constructor_args():
    sig = inspect.signature(XHTML::block.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::form_is_not_abstract():
    assert not inspect.isabstract(XHTML::Form)


def test_xhtml::form_constructor_exists():
    assert callable(XHTML::Form.__init__)


def test_xhtml::form_constructor_args():
    sig = inspect.signature(XHTML::Form.__init__)
    params = list(sig.parameters.keys())
    assert "method" in params, "Missing parameter 'method'"

def test_xhtml::form_has_method():
    assert hasattr(XHTML::Form, "method")
    descriptor = None
    for klass in XHTML::Form.__mro__:
        if "method" in klass.__dict__:
            descriptor = klass.__dict__["method"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::misc_is_not_abstract():
    assert not inspect.isabstract(XHTML::Misc)


def test_xhtml::misc_constructor_exists():
    assert callable(XHTML::Misc.__init__)


def test_xhtml::misc_constructor_args():
    sig = inspect.signature(XHTML::Misc.__init__)
    params = list(sig.parameters.keys())



def test_inline_is_not_abstract():
    assert not inspect.isabstract(Inline)


def test_inline_constructor_exists():
    assert callable(Inline.__init__)


def test_inline_constructor_args():
    sig = inspect.signature(Inline.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::inline_is_not_abstract():
    assert not inspect.isabstract(XHTML::inline)


def test_xhtml::inline_constructor_exists():
    assert callable(XHTML::inline.__init__)


def test_xhtml::inline_constructor_args():
    sig = inspect.signature(XHTML::inline.__init__)
    params = list(sig.parameters.keys())



def test_misc_is_not_abstract():
    assert not inspect.isabstract(Misc)


def test_misc_constructor_exists():
    assert callable(Misc.__init__)


def test_misc_constructor_args():
    sig = inspect.signature(Misc.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::noscript_is_not_abstract():
    assert not inspect.isabstract(XHTML::Noscript)


def test_xhtml::noscript_constructor_exists():
    assert callable(XHTML::Noscript.__init__)


def test_xhtml::noscript_constructor_args():
    sig = inspect.signature(XHTML::Noscript.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::miscinline_is_not_abstract():
    assert not inspect.isabstract(XHTML::Miscinline)


def test_xhtml::miscinline_constructor_exists():
    assert callable(XHTML::Miscinline.__init__)


def test_xhtml::miscinline_constructor_args():
    sig = inspect.signature(XHTML::Miscinline.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::inlineforms_is_not_abstract():
    assert not inspect.isabstract(XHTML::Inlineforms)


def test_xhtml::inlineforms_constructor_exists():
    assert callable(XHTML::Inlineforms.__init__)


def test_xhtml::inlineforms_constructor_args():
    sig = inspect.signature(XHTML::Inlineforms.__init__)
    params = list(sig.parameters.keys())



def test_scriptexpression_is_not_abstract():
    assert not inspect.isabstract(ScriptExpression)


def test_scriptexpression_constructor_exists():
    assert callable(ScriptExpression.__init__)


def test_scriptexpression_constructor_args():
    sig = inspect.signature(ScriptExpression.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::events_is_not_abstract():
    assert not inspect.isabstract(XHTML::Events)


def test_xhtml::events_constructor_exists():
    assert callable(XHTML::Events.__init__)


def test_xhtml::events_constructor_args():
    sig = inspect.signature(XHTML::Events.__init__)
    params = list(sig.parameters.keys())



def test_languagecode_is_not_abstract():
    assert not inspect.isabstract(LanguageCode)


def test_languagecode_constructor_exists():
    assert callable(LanguageCode.__init__)


def test_languagecode_constructor_args():
    sig = inspect.signature(LanguageCode.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::i18n_is_not_abstract():
    assert not inspect.isabstract(XHTML::I18n)


def test_xhtml::i18n_constructor_exists():
    assert callable(XHTML::I18n.__init__)


def test_xhtml::i18n_constructor_args():
    sig = inspect.signature(XHTML::I18n.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_xhtml::i18n_has_dir():
    assert hasattr(XHTML::I18n, "dir")
    descriptor = None
    for klass in XHTML::I18n.__mro__:
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



def test_xhtml::map_is_not_abstract():
    assert not inspect.isabstract(XHTML::Map)


def test_xhtml::map_constructor_exists():
    assert callable(XHTML::Map.__init__)


def test_xhtml::map_constructor_args():
    sig = inspect.signature(XHTML::Map.__init__)
    params = list(sig.parameters.keys())



def test_coreattrs_is_not_abstract():
    assert not inspect.isabstract(CoreAttrs)


def test_coreattrs_constructor_exists():
    assert callable(CoreAttrs.__init__)


def test_coreattrs_constructor_args():
    sig = inspect.signature(CoreAttrs.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::br_is_not_abstract():
    assert not inspect.isabstract(XHTML::Br)


def test_xhtml::br_constructor_exists():
    assert callable(XHTML::Br.__init__)


def test_xhtml::br_constructor_args():
    sig = inspect.signature(XHTML::Br.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::bdo_is_not_abstract():
    assert not inspect.isabstract(XHTML::Bdo)


def test_xhtml::bdo_constructor_exists():
    assert callable(XHTML::Bdo.__init__)


def test_xhtml::bdo_constructor_args():
    sig = inspect.signature(XHTML::Bdo.__init__)
    params = list(sig.parameters.keys())
    assert "dir" in params, "Missing parameter 'dir'"

def test_xhtml::bdo_has_dir():
    assert hasattr(XHTML::Bdo, "dir")
    descriptor = None
    for klass in XHTML::Bdo.__mro__:
        if "dir" in klass.__dict__:
            descriptor = klass.__dict__["dir"]
            break
    assert isinstance(descriptor, property)



def test_xhtml::attrs_is_not_abstract():
    assert not inspect.isabstract(XHTML::Attrs)


def test_xhtml::attrs_constructor_exists():
    assert callable(XHTML::Attrs.__init__)


def test_xhtml::attrs_constructor_args():
    sig = inspect.signature(XHTML::Attrs.__init__)
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



def test_xhtml::coreattrs_is_not_abstract():
    assert not inspect.isabstract(XHTML::CoreAttrs)


def test_xhtml::coreattrs_constructor_exists():
    assert callable(XHTML::CoreAttrs.__init__)


def test_xhtml::coreattrs_constructor_args():
    sig = inspect.signature(XHTML::CoreAttrs.__init__)
    params = list(sig.parameters.keys())



def test_length_is_not_abstract():
    assert not inspect.isabstract(Length)


def test_length_constructor_exists():
    assert callable(Length.__init__)


def test_length_constructor_args():
    sig = inspect.signature(Length.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::coords_is_not_abstract():
    assert not inspect.isabstract(XHTML::Coords)


def test_xhtml::coords_constructor_exists():
    assert callable(XHTML::Coords.__init__)


def test_xhtml::coords_constructor_args():
    sig = inspect.signature(XHTML::Coords.__init__)
    params = list(sig.parameters.keys())



def test_contenttype_is_not_abstract():
    assert not inspect.isabstract(ContentType)


def test_contenttype_constructor_exists():
    assert callable(ContentType.__init__)


def test_contenttype_constructor_args():
    sig = inspect.signature(ContentType.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::contenttypes_is_not_abstract():
    assert not inspect.isabstract(XHTML::ContentTypes)


def test_xhtml::contenttypes_constructor_exists():
    assert callable(XHTML::ContentTypes.__init__)


def test_xhtml::contenttypes_constructor_args():
    sig = inspect.signature(XHTML::ContentTypes.__init__)
    params = list(sig.parameters.keys())



def test_cdata_is_not_abstract():
    assert not inspect.isabstract(CDATA)


def test_cdata_constructor_exists():
    assert callable(CDATA.__init__)


def test_cdata_constructor_args():
    sig = inspect.signature(CDATA.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::scriptexpression_is_not_abstract():
    assert not inspect.isabstract(XHTML::ScriptExpression)


def test_xhtml::scriptexpression_constructor_exists():
    assert callable(XHTML::ScriptExpression.__init__)


def test_xhtml::scriptexpression_constructor_args():
    sig = inspect.signature(XHTML::ScriptExpression.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::pixels_is_not_abstract():
    assert not inspect.isabstract(XHTML::Pixels)


def test_xhtml::pixels_constructor_exists():
    assert callable(XHTML::Pixels.__init__)


def test_xhtml::pixels_constructor_args():
    sig = inspect.signature(XHTML::Pixels.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::datetime_is_not_abstract():
    assert not inspect.isabstract(XHTML::Datetime)


def test_xhtml::datetime_constructor_exists():
    assert callable(XHTML::Datetime.__init__)


def test_xhtml::datetime_constructor_args():
    sig = inspect.signature(XHTML::Datetime.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::multilength_is_not_abstract():
    assert not inspect.isabstract(XHTML::MultiLength)


def test_xhtml::multilength_constructor_exists():
    assert callable(XHTML::MultiLength.__init__)


def test_xhtml::multilength_constructor_args():
    sig = inspect.signature(XHTML::MultiLength.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::length_is_not_abstract():
    assert not inspect.isabstract(XHTML::Length)


def test_xhtml::length_constructor_exists():
    assert callable(XHTML::Length.__init__)


def test_xhtml::length_constructor_args():
    sig = inspect.signature(XHTML::Length.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::stylesheet_is_not_abstract():
    assert not inspect.isabstract(XHTML::StyleSheet)


def test_xhtml::stylesheet_constructor_exists():
    assert callable(XHTML::StyleSheet.__init__)


def test_xhtml::stylesheet_constructor_args():
    sig = inspect.signature(XHTML::StyleSheet.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::text_is_not_abstract():
    assert not inspect.isabstract(XHTML::Text)


def test_xhtml::text_constructor_exists():
    assert callable(XHTML::Text.__init__)


def test_xhtml::text_constructor_args():
    sig = inspect.signature(XHTML::Text.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::contenttype_is_not_abstract():
    assert not inspect.isabstract(XHTML::ContentType)


def test_xhtml::contenttype_constructor_exists():
    assert callable(XHTML::ContentType.__init__)


def test_xhtml::contenttype_constructor_args():
    sig = inspect.signature(XHTML::ContentType.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::empty_is_not_abstract():
    assert not inspect.isabstract(XHTML::EMPTY)


def test_xhtml::empty_constructor_exists():
    assert callable(XHTML::EMPTY.__init__)


def test_xhtml::empty_constructor_args():
    sig = inspect.signature(XHTML::EMPTY.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::id_is_not_abstract():
    assert not inspect.isabstract(XHTML::ID)


def test_xhtml::id_constructor_exists():
    assert callable(XHTML::ID.__init__)


def test_xhtml::id_constructor_args():
    sig = inspect.signature(XHTML::ID.__init__)
    params = list(sig.parameters.keys())



def test_idref_is_not_abstract():
    assert not inspect.isabstract(IDREF)


def test_idref_constructor_exists():
    assert callable(IDREF.__init__)


def test_idref_constructor_args():
    sig = inspect.signature(IDREF.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::idrefs_is_not_abstract():
    assert not inspect.isabstract(XHTML::IDREFS)


def test_xhtml::idrefs_constructor_exists():
    assert callable(XHTML::IDREFS.__init__)


def test_xhtml::idrefs_constructor_args():
    sig = inspect.signature(XHTML::IDREFS.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::idref_is_not_abstract():
    assert not inspect.isabstract(XHTML::IDREF)


def test_xhtml::idref_constructor_exists():
    assert callable(XHTML::IDREF.__init__)


def test_xhtml::idref_constructor_args():
    sig = inspect.signature(XHTML::IDREF.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::nmtoken_is_not_abstract():
    assert not inspect.isabstract(XHTML::NMTOKEN)


def test_xhtml::nmtoken_constructor_exists():
    assert callable(XHTML::NMTOKEN.__init__)


def test_xhtml::nmtoken_constructor_args():
    sig = inspect.signature(XHTML::NMTOKEN.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::urilist_is_not_abstract():
    assert not inspect.isabstract(XHTML::UriList)


def test_xhtml::urilist_constructor_exists():
    assert callable(XHTML::UriList.__init__)


def test_xhtml::urilist_constructor_args():
    sig = inspect.signature(XHTML::UriList.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::uri_is_not_abstract():
    assert not inspect.isabstract(XHTML::URI)


def test_xhtml::uri_constructor_exists():
    assert callable(XHTML::URI.__init__)


def test_xhtml::uri_constructor_args():
    sig = inspect.signature(XHTML::URI.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::mediadesc_is_not_abstract():
    assert not inspect.isabstract(XHTML::MediaDesc)


def test_xhtml::mediadesc_constructor_exists():
    assert callable(XHTML::MediaDesc.__init__)


def test_xhtml::mediadesc_constructor_args():
    sig = inspect.signature(XHTML::MediaDesc.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::linktypes_is_not_abstract():
    assert not inspect.isabstract(XHTML::LinkTypes)


def test_xhtml::linktypes_constructor_exists():
    assert callable(XHTML::LinkTypes.__init__)


def test_xhtml::linktypes_constructor_args():
    sig = inspect.signature(XHTML::LinkTypes.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::number_is_not_abstract():
    assert not inspect.isabstract(XHTML::Number)


def test_xhtml::number_constructor_exists():
    assert callable(XHTML::Number.__init__)


def test_xhtml::number_constructor_args():
    sig = inspect.signature(XHTML::Number.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::character_is_not_abstract():
    assert not inspect.isabstract(XHTML::Character)


def test_xhtml::character_constructor_exists():
    assert callable(XHTML::Character.__init__)


def test_xhtml::character_constructor_args():
    sig = inspect.signature(XHTML::Character.__init__)
    params = list(sig.parameters.keys())



def test_nmtoken_is_not_abstract():
    assert not inspect.isabstract(NMTOKEN)


def test_nmtoken_constructor_exists():
    assert callable(NMTOKEN.__init__)


def test_nmtoken_constructor_args():
    sig = inspect.signature(NMTOKEN.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::languagecode_is_not_abstract():
    assert not inspect.isabstract(XHTML::LanguageCode)


def test_xhtml::languagecode_constructor_exists():
    assert callable(XHTML::LanguageCode.__init__)


def test_xhtml::languagecode_constructor_args():
    sig = inspect.signature(XHTML::LanguageCode.__init__)
    params = list(sig.parameters.keys())



def test_charset_is_not_abstract():
    assert not inspect.isabstract(Charset)


def test_charset_constructor_exists():
    assert callable(Charset.__init__)


def test_charset_constructor_args():
    sig = inspect.signature(Charset.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::charsets_is_not_abstract():
    assert not inspect.isabstract(XHTML::Charsets)


def test_xhtml::charsets_constructor_exists():
    assert callable(XHTML::Charsets.__init__)


def test_xhtml::charsets_constructor_args():
    sig = inspect.signature(XHTML::Charsets.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::charset_is_not_abstract():
    assert not inspect.isabstract(XHTML::Charset)


def test_xhtml::charset_constructor_exists():
    assert callable(XHTML::Charset.__init__)


def test_xhtml::charset_constructor_args():
    sig = inspect.signature(XHTML::Charset.__init__)
    params = list(sig.parameters.keys())



def test_xhtml::pcdata_is_not_abstract():
    assert not inspect.isabstract(XHTML::PCDATA)


def test_xhtml::pcdata_constructor_exists():
    assert callable(XHTML::PCDATA.__init__)


def test_xhtml::pcdata_constructor_args():
    sig = inspect.signature(XHTML::PCDATA.__init__)
    params = list(sig.parameters.keys())

def test_buttontype_exists():
    # Check that the Enumeration exists
    assert ButtonType is not None

def test_buttontype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ButtonType]
    expected_literals = [
        "reset",
        "submit",
        "button",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ButtonType"

def test_scope_exists():
    # Check that the Enumeration exists
    assert Scope is not None

def test_scope_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Scope]
    expected_literals = [
        "row",
        "colgroup",
        "rowgroup",
        "col",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Scope"

def test_cellhalign_exists():
    # Check that the Enumeration exists
    assert CellHAlign is not None

def test_cellhalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CellHAlign]
    expected_literals = [
        "right",
        "justify",
        "char",
        "left",
        "center",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CellHAlign"

def test_inputtype_exists():
    # Check that the Enumeration exists
    assert InputType is not None

def test_inputtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in InputType]
    expected_literals = [
        "file",
        "password",
        "hidden",
        "image",
        "radio",
        "checkbox",
        "submit",
        "button",
        "reset",
        "text",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in InputType"

def test_trules_exists():
    # Check that the Enumeration exists
    assert TRules is not None

def test_trules_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TRules]
    expected_literals = [
        "none",
        "groups",
        "rows",
        "cols",
        "all",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TRules"

def test_valuetype_exists():
    # Check that the Enumeration exists
    assert ValueType is not None

def test_valuetype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ValueType]
    expected_literals = [
        "ref",
        "data",
        "object",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ValueType"

def test_shape_exists():
    # Check that the Enumeration exists
    assert Shape is not None

def test_shape_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Shape]
    expected_literals = [
        "circle",
        "default",
        "poly",
        "rect",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Shape"

def test_fomemethod_exists():
    # Check that the Enumeration exists
    assert FomeMethod is not None

def test_fomemethod_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FomeMethod]
    expected_literals = [
        "get",
        "post",
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
        "ltr",
        "rtl",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Direction"

def test_tframe_exists():
    # Check that the Enumeration exists
    assert TFrame is not None

def test_tframe_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in TFrame]
    expected_literals = [
        "rhs",
        "void",
        "vsides",
        "above",
        "box",
        "below",
        "border",
        "hsides",
        "lhs",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in TFrame"

def test_cellvalign_exists():
    # Check that the Enumeration exists
    assert CellVAlign is not None

def test_cellvalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in CellVAlign]
    expected_literals = [
        "baseline",
        "bottom",
        "middle",
        "top",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in CellVAlign"


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
XHTML::TrElement_strategy = st.builds(
    XHTML::TrElement,
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
XHTML::ColElement_strategy = st.builds(
    XHTML::ColElement,
)
Tbody_strategy = st.builds(
    Tbody,
)
XHTML::TableElement_strategy = st.builds(
    XHTML::TableElement,
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
XHTML::Cellvalign_strategy = st.builds(
    XHTML::Cellvalign,
    valign=
        safe_text
)
XHTML::Cellhalign_strategy = st.builds(
    XHTML::Cellhalign,
    align=
        safe_text
)
XHTML::FieldsetElement_strategy = st.builds(
    XHTML::FieldsetElement,
)
XHTML::SelectElement_strategy = st.builds(
    XHTML::SelectElement,
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
XHTML::MapElementContent_strategy = st.builds(
    XHTML::MapElementContent,
)
XHTML::MapElement_strategy = st.builds(
    XHTML::MapElement,
)
MapElement_strategy = st.builds(
    MapElement,
)
XHTML::MapContent_strategy = st.builds(
    XHTML::MapContent,
)
UriList_strategy = st.builds(
    UriList,
)
XHTML::ObjectElement_strategy = st.builds(
    XHTML::ObjectElement,
)
ValuedElement_strategy = st.builds(
    ValuedElement,
)
XHTML::CDATA_strategy = st.builds(
    XHTML::CDATA,
)
XHTML::ValuedElement_strategy = st.builds(
    XHTML::ValuedElement,
    value=
        safe_text
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
XHTML::Dt_strategy = st.builds(
    XHTML::Dt,
)
XHTML::Dd_strategy = st.builds(
    XHTML::Dd,
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
XHTML::Base_strategy = st.builds(
    XHTML::Base,
)
XHTML::TitleBaseHeadElement_strategy = st.builds(
    XHTML::TitleBaseHeadElement,
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
XHTML::Button_strategy = st.builds(
    XHTML::Button,
    disabled=
        safe_text,
    type=
        safe_text
)
XHTML::Ins_strategy = st.builds(
    XHTML::Ins,
)
XHTML::Var_strategy = st.builds(
    XHTML::Var,
)
XHTML::Area_strategy = st.builds(
    XHTML::Area,
    nohref=
        safe_text,
    shape=
        safe_text
)
XHTML::Caption_strategy = st.builds(
    XHTML::Caption,
)
XHTML::Blockquote_strategy = st.builds(
    XHTML::Blockquote,
)
XHTML::Kbd_strategy = st.builds(
    XHTML::Kbd,
)
XHTML::Body_strategy = st.builds(
    XHTML::Body,
)
XHTML::H5_strategy = st.builds(
    XHTML::H5,
)
XHTML::Samp_strategy = st.builds(
    XHTML::Samp,
)
XHTML::H4_strategy = st.builds(
    XHTML::H4,
)
XHTML::Code_strategy = st.builds(
    XHTML::Code,
)
XHTML::H3_strategy = st.builds(
    XHTML::H3,
)
XHTML::Dfn_strategy = st.builds(
    XHTML::Dfn,
)
XHTML::Thead_strategy = st.builds(
    XHTML::Thead,
)
XHTML::H2_strategy = st.builds(
    XHTML::H2,
)
XHTML::Strong_strategy = st.builds(
    XHTML::Strong,
)
XHTML::Optgroup_strategy = st.builds(
    XHTML::Optgroup,
    disabled=
        safe_text
)
XHTML::Small_strategy = st.builds(
    XHTML::Small,
)
XHTML::H1_strategy = st.builds(
    XHTML::H1,
)
XHTML::Big_strategy = st.builds(
    XHTML::Big,
)
XHTML::Select_strategy = st.builds(
    XHTML::Select,
    disabled=
        safe_text,
    multiple=
        safe_text
)
XHTML::B_strategy = st.builds(
    XHTML::B,
)
XHTML::Dl_strategy = st.builds(
    XHTML::Dl,
)
XHTML::Input_strategy = st.builds(
    XHTML::Input,
    readonly=
        safe_text,
    disabled=
        safe_text,
    checked=
        safe_text,
    type=
        safe_text
)
XHTML::I_strategy = st.builds(
    XHTML::I,
)
XHTML::Tfoot_strategy = st.builds(
    XHTML::Tfoot,
)
XHTML::Span_strategy = st.builds(
    XHTML::Span,
)
XHTML::Li_strategy = st.builds(
    XHTML::Li,
)
XHTML::Td_strategy = st.builds(
    XHTML::Td,
    scope=
        safe_text
)
XHTML::Ol_strategy = st.builds(
    XHTML::Ol,
)
XHTML::Tt_strategy = st.builds(
    XHTML::Tt,
)
XHTML::Pre_strategy = st.builds(
    XHTML::Pre,
    xml_space=
        safe_text
)
XHTML::Sup_strategy = st.builds(
    XHTML::Sup,
)
XHTML::Label_strategy = st.builds(
    XHTML::Label,
)
XHTML::Th_strategy = st.builds(
    XHTML::Th,
    scope=
        safe_text
)
XHTML::Hr_strategy = st.builds(
    XHTML::Hr,
)
XHTML::Sub_strategy = st.builds(
    XHTML::Sub,
)
XHTML::Ul_strategy = st.builds(
    XHTML::Ul,
)
XHTML::Q_strategy = st.builds(
    XHTML::Q,
)
XHTML::Address_strategy = st.builds(
    XHTML::Address,
)
XHTML::H6_strategy = st.builds(
    XHTML::H6,
)
XHTML::Acronym_strategy = st.builds(
    XHTML::Acronym,
)
XHTML::Col_strategy = st.builds(
    XHTML::Col,
)
XHTML::Abbr_strategy = st.builds(
    XHTML::Abbr,
)
XHTML::Cite_strategy = st.builds(
    XHTML::Cite,
)
XHTML::Tr_strategy = st.builds(
    XHTML::Tr,
)
XHTML::DlElement_strategy = st.builds(
    XHTML::DlElement,
)
XHTML::Colgroup_strategy = st.builds(
    XHTML::Colgroup,
)
XHTML::Del_strategy = st.builds(
    XHTML::Del,
)
XHTML::Em_strategy = st.builds(
    XHTML::Em,
)
XHTML::Tbody_strategy = st.builds(
    XHTML::Tbody,
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
XHTML::Link_strategy = st.builds(
    XHTML::Link,
)
XHTML::Meta_strategy = st.builds(
    XHTML::Meta,
)
XHTML::Head_strategy = st.builds(
    XHTML::Head,
)
XHTML::HeadMisc_strategy = st.builds(
    XHTML::HeadMisc,
)
Body_strategy = st.builds(
    Body,
)
XHTML::BaseHeadElement_strategy = st.builds(
    XHTML::BaseHeadElement,
)
Base_strategy = st.builds(
    Base,
)
XHTML::BaseTitleHeadElement_strategy = st.builds(
    XHTML::BaseTitleHeadElement,
)
BaseTitleHeadElement_strategy = st.builds(
    BaseTitleHeadElement,
)
Title_strategy = st.builds(
    Title,
)
XHTML::TitleHeadElement_strategy = st.builds(
    XHTML::TitleHeadElement,
)
XHTML::HeadElement_strategy = st.builds(
    XHTML::HeadElement,
)
XHTML::AContent_strategy = st.builds(
    XHTML::AContent,
)
XHTML::Flow_strategy = st.builds(
    XHTML::Flow,
)
XHTML::Block_strategy = st.builds(
    XHTML::Block,
)
Head_strategy = st.builds(
    Head,
)
XHTML::Html_strategy = st.builds(
    XHTML::Html,
)
XHTML::ButtonContent_strategy = st.builds(
    XHTML::ButtonContent,
)
XHTML::FormContent_strategy = st.builds(
    XHTML::FormContent,
)
XHTML::PreContent_strategy = st.builds(
    XHTML::PreContent,
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
XHTML::Special_strategy = st.builds(
    XHTML::Special,
)
PreContent_strategy = st.builds(
    PreContent,
)
XHTML::Phrase_strategy = st.builds(
    XHTML::Phrase,
)
XHTML::A_strategy = st.builds(
    XHTML::A,
    shape=
        safe_text
)
XHTML::Fontstyle_strategy = st.builds(
    XHTML::Fontstyle,
)
Special_strategy = st.builds(
    Special,
)
XHTML::Object_strategy = st.builds(
    XHTML::Object,
    declare=
        safe_text
)
XHTML::Img_strategy = st.builds(
    XHTML::Img,
    ismap=
        safe_text
)
XHTML::Specialpre_strategy = st.builds(
    XHTML::Specialpre,
)
Number_strategy = st.builds(
    Number,
)
Character_strategy = st.builds(
    Character,
)
XHTML::Focus_strategy = st.builds(
    XHTML::Focus,
)
block_strategy = st.builds(
    block,
)
XHTML::Blocktext_strategy = st.builds(
    XHTML::Blocktext,
)
XHTML::Div_strategy = st.builds(
    XHTML::Div,
)
XHTML::Table_strategy = st.builds(
    XHTML::Table,
    frame=
        safe_text,
    rules=
        safe_text
)
XHTML::Fieldset_strategy = st.builds(
    XHTML::Fieldset,
)
XHTML::Lists_strategy = st.builds(
    XHTML::Lists,
)
XHTML::P_strategy = st.builds(
    XHTML::P,
)
XHTML::Heading_strategy = st.builds(
    XHTML::Heading,
)
PCDATA_strategy = st.builds(
    PCDATA,
)
XHTML::Option_strategy = st.builds(
    XHTML::Option,
    selected=
        safe_text,
    disabled=
        safe_text
)
XHTML::Title_strategy = st.builds(
    XHTML::Title,
)
XHTML::Script_strategy = st.builds(
    XHTML::Script,
    xml_space=
        safe_text,
    defer=
        safe_text
)
XHTML::Style_strategy = st.builds(
    XHTML::Style,
    xml_space=
        safe_text
)
XHTML::Textarea_strategy = st.builds(
    XHTML::Textarea,
    disabled=
        safe_text,
    readonly=
        safe_text
)
FieldsetElement_strategy = st.builds(
    FieldsetElement,
)
XHTML::Legend_strategy = st.builds(
    XHTML::Legend,
)
MapElementContent_strategy = st.builds(
    MapElementContent,
)
ObjectElement_strategy = st.builds(
    ObjectElement,
)
XHTML::Param_strategy = st.builds(
    XHTML::Param,
    valuetype=
        safe_text
)
FormContent_strategy = st.builds(
    FormContent,
)
Flow_strategy = st.builds(
    Flow,
)
XHTML::Inline_strategy = st.builds(
    XHTML::Inline,
)
Block_strategy = st.builds(
    Block,
)
XHTML::block_strategy = st.builds(
    XHTML::block,
)
XHTML::Form_strategy = st.builds(
    XHTML::Form,
    method=
        safe_text
)
XHTML::Misc_strategy = st.builds(
    XHTML::Misc,
)
Inline_strategy = st.builds(
    Inline,
)
XHTML::inline_strategy = st.builds(
    XHTML::inline,
)
Misc_strategy = st.builds(
    Misc,
)
XHTML::Noscript_strategy = st.builds(
    XHTML::Noscript,
)
XHTML::Miscinline_strategy = st.builds(
    XHTML::Miscinline,
)
XHTML::Inlineforms_strategy = st.builds(
    XHTML::Inlineforms,
)
ScriptExpression_strategy = st.builds(
    ScriptExpression,
)
XHTML::Events_strategy = st.builds(
    XHTML::Events,
)
LanguageCode_strategy = st.builds(
    LanguageCode,
)
XHTML::I18n_strategy = st.builds(
    XHTML::I18n,
    dir=
        safe_text
)
Events_strategy = st.builds(
    Events,
)
I18n_strategy = st.builds(
    I18n,
)
XHTML::Map_strategy = st.builds(
    XHTML::Map,
)
CoreAttrs_strategy = st.builds(
    CoreAttrs,
)
XHTML::Br_strategy = st.builds(
    XHTML::Br,
)
XHTML::Bdo_strategy = st.builds(
    XHTML::Bdo,
    dir=
        safe_text
)
XHTML::Attrs_strategy = st.builds(
    XHTML::Attrs,
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
XHTML::CoreAttrs_strategy = st.builds(
    XHTML::CoreAttrs,
)
Length_strategy = st.builds(
    Length,
)
XHTML::Coords_strategy = st.builds(
    XHTML::Coords,
)
ContentType_strategy = st.builds(
    ContentType,
)
XHTML::ContentTypes_strategy = st.builds(
    XHTML::ContentTypes,
)
CDATA_strategy = st.builds(
    CDATA,
)
XHTML::ScriptExpression_strategy = st.builds(
    XHTML::ScriptExpression,
)
XHTML::Pixels_strategy = st.builds(
    XHTML::Pixels,
)
XHTML::Datetime_strategy = st.builds(
    XHTML::Datetime,
)
XHTML::MultiLength_strategy = st.builds(
    XHTML::MultiLength,
)
XHTML::Length_strategy = st.builds(
    XHTML::Length,
)
XHTML::StyleSheet_strategy = st.builds(
    XHTML::StyleSheet,
)
XHTML::Text_strategy = st.builds(
    XHTML::Text,
)
XHTML::ContentType_strategy = st.builds(
    XHTML::ContentType,
)
XHTML::EMPTY_strategy = st.builds(
    XHTML::EMPTY,
)
XHTML::ID_strategy = st.builds(
    XHTML::ID,
)
IDREF_strategy = st.builds(
    IDREF,
)
XHTML::IDREFS_strategy = st.builds(
    XHTML::IDREFS,
)
XHTML::IDREF_strategy = st.builds(
    XHTML::IDREF,
)
XHTML::NMTOKEN_strategy = st.builds(
    XHTML::NMTOKEN,
)
XHTML::UriList_strategy = st.builds(
    XHTML::UriList,
)
XHTML::URI_strategy = st.builds(
    XHTML::URI,
)
XHTML::MediaDesc_strategy = st.builds(
    XHTML::MediaDesc,
)
XHTML::LinkTypes_strategy = st.builds(
    XHTML::LinkTypes,
)
XHTML::Number_strategy = st.builds(
    XHTML::Number,
)
XHTML::Character_strategy = st.builds(
    XHTML::Character,
)
NMTOKEN_strategy = st.builds(
    NMTOKEN,
)
XHTML::LanguageCode_strategy = st.builds(
    XHTML::LanguageCode,
)
Charset_strategy = st.builds(
    Charset,
)
XHTML::Charsets_strategy = st.builds(
    XHTML::Charsets,
)
XHTML::Charset_strategy = st.builds(
    XHTML::Charset,
)
XHTML::PCDATA_strategy = st.builds(
    XHTML::PCDATA,
)

@given(instance=IDREFS_strategy)
@settings(max_examples=50)
def test_idrefs_instantiation(instance):
    assert isinstance(instance, IDREFS)

@given(instance=XHTML::TrElement_strategy)
@settings(max_examples=50)
def test_xhtml::trelement_instantiation(instance):
    assert isinstance(instance, XHTML::TrElement)

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

@given(instance=XHTML::ColElement_strategy)
@settings(max_examples=50)
def test_xhtml::colelement_instantiation(instance):
    assert isinstance(instance, XHTML::ColElement)

@given(instance=Tbody_strategy)
@settings(max_examples=50)
def test_tbody_instantiation(instance):
    assert isinstance(instance, Tbody)

@given(instance=XHTML::TableElement_strategy)
@settings(max_examples=50)
def test_xhtml::tableelement_instantiation(instance):
    assert isinstance(instance, XHTML::TableElement)

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

@given(instance=XHTML::Cellvalign_strategy)
@settings(max_examples=50)
def test_xhtml::cellvalign_instantiation(instance):
    assert isinstance(instance, XHTML::Cellvalign)

@given(instance=XHTML::Cellvalign_strategy)
def test_xhtml::cellvalign_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=XHTML::Cellvalign_strategy)
def test_xhtml::cellvalign_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=XHTML::Cellhalign_strategy)
@settings(max_examples=50)
def test_xhtml::cellhalign_instantiation(instance):
    assert isinstance(instance, XHTML::Cellhalign)

@given(instance=XHTML::Cellhalign_strategy)
def test_xhtml::cellhalign_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=XHTML::Cellhalign_strategy)
def test_xhtml::cellhalign_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=XHTML::FieldsetElement_strategy)
@settings(max_examples=50)
def test_xhtml::fieldsetelement_instantiation(instance):
    assert isinstance(instance, XHTML::FieldsetElement)

@given(instance=XHTML::SelectElement_strategy)
@settings(max_examples=50)
def test_xhtml::selectelement_instantiation(instance):
    assert isinstance(instance, XHTML::SelectElement)

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

@given(instance=XHTML::MapElementContent_strategy)
@settings(max_examples=50)
def test_xhtml::mapelementcontent_instantiation(instance):
    assert isinstance(instance, XHTML::MapElementContent)

@given(instance=XHTML::MapElement_strategy)
@settings(max_examples=50)
def test_xhtml::mapelement_instantiation(instance):
    assert isinstance(instance, XHTML::MapElement)

@given(instance=MapElement_strategy)
@settings(max_examples=50)
def test_mapelement_instantiation(instance):
    assert isinstance(instance, MapElement)

@given(instance=XHTML::MapContent_strategy)
@settings(max_examples=50)
def test_xhtml::mapcontent_instantiation(instance):
    assert isinstance(instance, XHTML::MapContent)

@given(instance=UriList_strategy)
@settings(max_examples=50)
def test_urilist_instantiation(instance):
    assert isinstance(instance, UriList)

@given(instance=XHTML::ObjectElement_strategy)
@settings(max_examples=50)
def test_xhtml::objectelement_instantiation(instance):
    assert isinstance(instance, XHTML::ObjectElement)

@given(instance=ValuedElement_strategy)
@settings(max_examples=50)
def test_valuedelement_instantiation(instance):
    assert isinstance(instance, ValuedElement)

@given(instance=XHTML::CDATA_strategy)
@settings(max_examples=50)
def test_xhtml::cdata_instantiation(instance):
    assert isinstance(instance, XHTML::CDATA)

@given(instance=XHTML::ValuedElement_strategy)
@settings(max_examples=50)
def test_xhtml::valuedelement_instantiation(instance):
    assert isinstance(instance, XHTML::ValuedElement)

@given(instance=XHTML::ValuedElement_strategy)
def test_xhtml::valuedelement_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=XHTML::ValuedElement_strategy)
def test_xhtml::valuedelement_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

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

@given(instance=XHTML::Dt_strategy)
@settings(max_examples=50)
def test_xhtml::dt_instantiation(instance):
    assert isinstance(instance, XHTML::Dt)

@given(instance=XHTML::Dd_strategy)
@settings(max_examples=50)
def test_xhtml::dd_instantiation(instance):
    assert isinstance(instance, XHTML::Dd)

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

@given(instance=XHTML::Base_strategy)
@settings(max_examples=50)
def test_xhtml::base_instantiation(instance):
    assert isinstance(instance, XHTML::Base)

@given(instance=XHTML::TitleBaseHeadElement_strategy)
@settings(max_examples=50)
def test_xhtml::titlebaseheadelement_instantiation(instance):
    assert isinstance(instance, XHTML::TitleBaseHeadElement)

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

@given(instance=XHTML::Button_strategy)
@settings(max_examples=50)
def test_xhtml::button_instantiation(instance):
    assert isinstance(instance, XHTML::Button)

@given(instance=XHTML::Button_strategy)
def test_xhtml::button_disabled_type(instance):
    assert isinstance(instance.disabled, str)


@given(instance=XHTML::Button_strategy)
def test_xhtml::button_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML::Button_strategy)
def test_xhtml::button_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=XHTML::Button_strategy)
def test_xhtml::button_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=XHTML::Ins_strategy)
@settings(max_examples=50)
def test_xhtml::ins_instantiation(instance):
    assert isinstance(instance, XHTML::Ins)

@given(instance=XHTML::Var_strategy)
@settings(max_examples=50)
def test_xhtml::var_instantiation(instance):
    assert isinstance(instance, XHTML::Var)

@given(instance=XHTML::Area_strategy)
@settings(max_examples=50)
def test_xhtml::area_instantiation(instance):
    assert isinstance(instance, XHTML::Area)

@given(instance=XHTML::Area_strategy)
def test_xhtml::area_nohref_type(instance):
    assert isinstance(instance.nohref, str)


@given(instance=XHTML::Area_strategy)
def test_xhtml::area_nohref_setter(instance):
    original = instance.nohref
    instance.nohref = original
    assert instance.nohref == original

@given(instance=XHTML::Area_strategy)
def test_xhtml::area_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=XHTML::Area_strategy)
def test_xhtml::area_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=XHTML::Caption_strategy)
@settings(max_examples=50)
def test_xhtml::caption_instantiation(instance):
    assert isinstance(instance, XHTML::Caption)

@given(instance=XHTML::Blockquote_strategy)
@settings(max_examples=50)
def test_xhtml::blockquote_instantiation(instance):
    assert isinstance(instance, XHTML::Blockquote)

@given(instance=XHTML::Kbd_strategy)
@settings(max_examples=50)
def test_xhtml::kbd_instantiation(instance):
    assert isinstance(instance, XHTML::Kbd)

@given(instance=XHTML::Body_strategy)
@settings(max_examples=50)
def test_xhtml::body_instantiation(instance):
    assert isinstance(instance, XHTML::Body)

@given(instance=XHTML::H5_strategy)
@settings(max_examples=50)
def test_xhtml::h5_instantiation(instance):
    assert isinstance(instance, XHTML::H5)

@given(instance=XHTML::Samp_strategy)
@settings(max_examples=50)
def test_xhtml::samp_instantiation(instance):
    assert isinstance(instance, XHTML::Samp)

@given(instance=XHTML::H4_strategy)
@settings(max_examples=50)
def test_xhtml::h4_instantiation(instance):
    assert isinstance(instance, XHTML::H4)

@given(instance=XHTML::Code_strategy)
@settings(max_examples=50)
def test_xhtml::code_instantiation(instance):
    assert isinstance(instance, XHTML::Code)

@given(instance=XHTML::H3_strategy)
@settings(max_examples=50)
def test_xhtml::h3_instantiation(instance):
    assert isinstance(instance, XHTML::H3)

@given(instance=XHTML::Dfn_strategy)
@settings(max_examples=50)
def test_xhtml::dfn_instantiation(instance):
    assert isinstance(instance, XHTML::Dfn)

@given(instance=XHTML::Thead_strategy)
@settings(max_examples=50)
def test_xhtml::thead_instantiation(instance):
    assert isinstance(instance, XHTML::Thead)

@given(instance=XHTML::H2_strategy)
@settings(max_examples=50)
def test_xhtml::h2_instantiation(instance):
    assert isinstance(instance, XHTML::H2)

@given(instance=XHTML::Strong_strategy)
@settings(max_examples=50)
def test_xhtml::strong_instantiation(instance):
    assert isinstance(instance, XHTML::Strong)

@given(instance=XHTML::Optgroup_strategy)
@settings(max_examples=50)
def test_xhtml::optgroup_instantiation(instance):
    assert isinstance(instance, XHTML::Optgroup)

@given(instance=XHTML::Optgroup_strategy)
def test_xhtml::optgroup_disabled_type(instance):
    assert isinstance(instance.disabled, str)


@given(instance=XHTML::Optgroup_strategy)
def test_xhtml::optgroup_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML::Small_strategy)
@settings(max_examples=50)
def test_xhtml::small_instantiation(instance):
    assert isinstance(instance, XHTML::Small)

@given(instance=XHTML::H1_strategy)
@settings(max_examples=50)
def test_xhtml::h1_instantiation(instance):
    assert isinstance(instance, XHTML::H1)

@given(instance=XHTML::Big_strategy)
@settings(max_examples=50)
def test_xhtml::big_instantiation(instance):
    assert isinstance(instance, XHTML::Big)

@given(instance=XHTML::Select_strategy)
@settings(max_examples=50)
def test_xhtml::select_instantiation(instance):
    assert isinstance(instance, XHTML::Select)

@given(instance=XHTML::Select_strategy)
def test_xhtml::select_disabled_type(instance):
    assert isinstance(instance.disabled, str)


@given(instance=XHTML::Select_strategy)
def test_xhtml::select_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML::Select_strategy)
def test_xhtml::select_multiple_type(instance):
    assert isinstance(instance.multiple, str)


@given(instance=XHTML::Select_strategy)
def test_xhtml::select_multiple_setter(instance):
    original = instance.multiple
    instance.multiple = original
    assert instance.multiple == original

@given(instance=XHTML::B_strategy)
@settings(max_examples=50)
def test_xhtml::b_instantiation(instance):
    assert isinstance(instance, XHTML::B)

@given(instance=XHTML::Dl_strategy)
@settings(max_examples=50)
def test_xhtml::dl_instantiation(instance):
    assert isinstance(instance, XHTML::Dl)

@given(instance=XHTML::Input_strategy)
@settings(max_examples=50)
def test_xhtml::input_instantiation(instance):
    assert isinstance(instance, XHTML::Input)

@given(instance=XHTML::Input_strategy)
def test_xhtml::input_readonly_type(instance):
    assert isinstance(instance.readonly, str)


@given(instance=XHTML::Input_strategy)
def test_xhtml::input_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=XHTML::Input_strategy)
def test_xhtml::input_disabled_type(instance):
    assert isinstance(instance.disabled, str)


@given(instance=XHTML::Input_strategy)
def test_xhtml::input_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML::Input_strategy)
def test_xhtml::input_checked_type(instance):
    assert isinstance(instance.checked, str)


@given(instance=XHTML::Input_strategy)
def test_xhtml::input_checked_setter(instance):
    original = instance.checked
    instance.checked = original
    assert instance.checked == original

@given(instance=XHTML::Input_strategy)
def test_xhtml::input_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=XHTML::Input_strategy)
def test_xhtml::input_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=XHTML::I_strategy)
@settings(max_examples=50)
def test_xhtml::i_instantiation(instance):
    assert isinstance(instance, XHTML::I)

@given(instance=XHTML::Tfoot_strategy)
@settings(max_examples=50)
def test_xhtml::tfoot_instantiation(instance):
    assert isinstance(instance, XHTML::Tfoot)

@given(instance=XHTML::Span_strategy)
@settings(max_examples=50)
def test_xhtml::span_instantiation(instance):
    assert isinstance(instance, XHTML::Span)

@given(instance=XHTML::Li_strategy)
@settings(max_examples=50)
def test_xhtml::li_instantiation(instance):
    assert isinstance(instance, XHTML::Li)

@given(instance=XHTML::Td_strategy)
@settings(max_examples=50)
def test_xhtml::td_instantiation(instance):
    assert isinstance(instance, XHTML::Td)

@given(instance=XHTML::Td_strategy)
def test_xhtml::td_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=XHTML::Td_strategy)
def test_xhtml::td_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=XHTML::Ol_strategy)
@settings(max_examples=50)
def test_xhtml::ol_instantiation(instance):
    assert isinstance(instance, XHTML::Ol)

@given(instance=XHTML::Tt_strategy)
@settings(max_examples=50)
def test_xhtml::tt_instantiation(instance):
    assert isinstance(instance, XHTML::Tt)

@given(instance=XHTML::Pre_strategy)
@settings(max_examples=50)
def test_xhtml::pre_instantiation(instance):
    assert isinstance(instance, XHTML::Pre)

@given(instance=XHTML::Pre_strategy)
def test_xhtml::pre_xml_space_type(instance):
    assert isinstance(instance.xml_space, str)


@given(instance=XHTML::Pre_strategy)
def test_xhtml::pre_xml_space_setter(instance):
    original = instance.xml_space
    instance.xml_space = original
    assert instance.xml_space == original

@given(instance=XHTML::Sup_strategy)
@settings(max_examples=50)
def test_xhtml::sup_instantiation(instance):
    assert isinstance(instance, XHTML::Sup)

@given(instance=XHTML::Label_strategy)
@settings(max_examples=50)
def test_xhtml::label_instantiation(instance):
    assert isinstance(instance, XHTML::Label)

@given(instance=XHTML::Th_strategy)
@settings(max_examples=50)
def test_xhtml::th_instantiation(instance):
    assert isinstance(instance, XHTML::Th)

@given(instance=XHTML::Th_strategy)
def test_xhtml::th_scope_type(instance):
    assert isinstance(instance.scope, str)


@given(instance=XHTML::Th_strategy)
def test_xhtml::th_scope_setter(instance):
    original = instance.scope
    instance.scope = original
    assert instance.scope == original

@given(instance=XHTML::Hr_strategy)
@settings(max_examples=50)
def test_xhtml::hr_instantiation(instance):
    assert isinstance(instance, XHTML::Hr)

@given(instance=XHTML::Sub_strategy)
@settings(max_examples=50)
def test_xhtml::sub_instantiation(instance):
    assert isinstance(instance, XHTML::Sub)

@given(instance=XHTML::Ul_strategy)
@settings(max_examples=50)
def test_xhtml::ul_instantiation(instance):
    assert isinstance(instance, XHTML::Ul)

@given(instance=XHTML::Q_strategy)
@settings(max_examples=50)
def test_xhtml::q_instantiation(instance):
    assert isinstance(instance, XHTML::Q)

@given(instance=XHTML::Address_strategy)
@settings(max_examples=50)
def test_xhtml::address_instantiation(instance):
    assert isinstance(instance, XHTML::Address)

@given(instance=XHTML::H6_strategy)
@settings(max_examples=50)
def test_xhtml::h6_instantiation(instance):
    assert isinstance(instance, XHTML::H6)

@given(instance=XHTML::Acronym_strategy)
@settings(max_examples=50)
def test_xhtml::acronym_instantiation(instance):
    assert isinstance(instance, XHTML::Acronym)

@given(instance=XHTML::Col_strategy)
@settings(max_examples=50)
def test_xhtml::col_instantiation(instance):
    assert isinstance(instance, XHTML::Col)

@given(instance=XHTML::Abbr_strategy)
@settings(max_examples=50)
def test_xhtml::abbr_instantiation(instance):
    assert isinstance(instance, XHTML::Abbr)

@given(instance=XHTML::Cite_strategy)
@settings(max_examples=50)
def test_xhtml::cite_instantiation(instance):
    assert isinstance(instance, XHTML::Cite)

@given(instance=XHTML::Tr_strategy)
@settings(max_examples=50)
def test_xhtml::tr_instantiation(instance):
    assert isinstance(instance, XHTML::Tr)

@given(instance=XHTML::DlElement_strategy)
@settings(max_examples=50)
def test_xhtml::dlelement_instantiation(instance):
    assert isinstance(instance, XHTML::DlElement)

@given(instance=XHTML::Colgroup_strategy)
@settings(max_examples=50)
def test_xhtml::colgroup_instantiation(instance):
    assert isinstance(instance, XHTML::Colgroup)

@given(instance=XHTML::Del_strategy)
@settings(max_examples=50)
def test_xhtml::del_instantiation(instance):
    assert isinstance(instance, XHTML::Del)

@given(instance=XHTML::Em_strategy)
@settings(max_examples=50)
def test_xhtml::em_instantiation(instance):
    assert isinstance(instance, XHTML::Em)

@given(instance=XHTML::Tbody_strategy)
@settings(max_examples=50)
def test_xhtml::tbody_instantiation(instance):
    assert isinstance(instance, XHTML::Tbody)

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

@given(instance=XHTML::Link_strategy)
@settings(max_examples=50)
def test_xhtml::link_instantiation(instance):
    assert isinstance(instance, XHTML::Link)

@given(instance=XHTML::Meta_strategy)
@settings(max_examples=50)
def test_xhtml::meta_instantiation(instance):
    assert isinstance(instance, XHTML::Meta)

@given(instance=XHTML::Head_strategy)
@settings(max_examples=50)
def test_xhtml::head_instantiation(instance):
    assert isinstance(instance, XHTML::Head)

@given(instance=XHTML::HeadMisc_strategy)
@settings(max_examples=50)
def test_xhtml::headmisc_instantiation(instance):
    assert isinstance(instance, XHTML::HeadMisc)

@given(instance=Body_strategy)
@settings(max_examples=50)
def test_body_instantiation(instance):
    assert isinstance(instance, Body)

@given(instance=XHTML::BaseHeadElement_strategy)
@settings(max_examples=50)
def test_xhtml::baseheadelement_instantiation(instance):
    assert isinstance(instance, XHTML::BaseHeadElement)

@given(instance=Base_strategy)
@settings(max_examples=50)
def test_base_instantiation(instance):
    assert isinstance(instance, Base)

@given(instance=XHTML::BaseTitleHeadElement_strategy)
@settings(max_examples=50)
def test_xhtml::basetitleheadelement_instantiation(instance):
    assert isinstance(instance, XHTML::BaseTitleHeadElement)

@given(instance=BaseTitleHeadElement_strategy)
@settings(max_examples=50)
def test_basetitleheadelement_instantiation(instance):
    assert isinstance(instance, BaseTitleHeadElement)

@given(instance=Title_strategy)
@settings(max_examples=50)
def test_title_instantiation(instance):
    assert isinstance(instance, Title)

@given(instance=XHTML::TitleHeadElement_strategy)
@settings(max_examples=50)
def test_xhtml::titleheadelement_instantiation(instance):
    assert isinstance(instance, XHTML::TitleHeadElement)

@given(instance=XHTML::HeadElement_strategy)
@settings(max_examples=50)
def test_xhtml::headelement_instantiation(instance):
    assert isinstance(instance, XHTML::HeadElement)

@given(instance=XHTML::AContent_strategy)
@settings(max_examples=50)
def test_xhtml::acontent_instantiation(instance):
    assert isinstance(instance, XHTML::AContent)

@given(instance=XHTML::Flow_strategy)
@settings(max_examples=50)
def test_xhtml::flow_instantiation(instance):
    assert isinstance(instance, XHTML::Flow)

@given(instance=XHTML::Block_strategy)
@settings(max_examples=50)
def test_xhtml::block_instantiation(instance):
    assert isinstance(instance, XHTML::Block)

@given(instance=Head_strategy)
@settings(max_examples=50)
def test_head_instantiation(instance):
    assert isinstance(instance, Head)

@given(instance=XHTML::Html_strategy)
@settings(max_examples=50)
def test_xhtml::html_instantiation(instance):
    assert isinstance(instance, XHTML::Html)

@given(instance=XHTML::ButtonContent_strategy)
@settings(max_examples=50)
def test_xhtml::buttoncontent_instantiation(instance):
    assert isinstance(instance, XHTML::ButtonContent)

@given(instance=XHTML::FormContent_strategy)
@settings(max_examples=50)
def test_xhtml::formcontent_instantiation(instance):
    assert isinstance(instance, XHTML::FormContent)

@given(instance=XHTML::PreContent_strategy)
@settings(max_examples=50)
def test_xhtml::precontent_instantiation(instance):
    assert isinstance(instance, XHTML::PreContent)

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

@given(instance=XHTML::Special_strategy)
@settings(max_examples=50)
def test_xhtml::special_instantiation(instance):
    assert isinstance(instance, XHTML::Special)

@given(instance=PreContent_strategy)
@settings(max_examples=50)
def test_precontent_instantiation(instance):
    assert isinstance(instance, PreContent)

@given(instance=XHTML::Phrase_strategy)
@settings(max_examples=50)
def test_xhtml::phrase_instantiation(instance):
    assert isinstance(instance, XHTML::Phrase)

@given(instance=XHTML::A_strategy)
@settings(max_examples=50)
def test_xhtml::a_instantiation(instance):
    assert isinstance(instance, XHTML::A)

@given(instance=XHTML::A_strategy)
def test_xhtml::a_shape_type(instance):
    assert isinstance(instance.shape, str)


@given(instance=XHTML::A_strategy)
def test_xhtml::a_shape_setter(instance):
    original = instance.shape
    instance.shape = original
    assert instance.shape == original

@given(instance=XHTML::Fontstyle_strategy)
@settings(max_examples=50)
def test_xhtml::fontstyle_instantiation(instance):
    assert isinstance(instance, XHTML::Fontstyle)

@given(instance=Special_strategy)
@settings(max_examples=50)
def test_special_instantiation(instance):
    assert isinstance(instance, Special)

@given(instance=XHTML::Object_strategy)
@settings(max_examples=50)
def test_xhtml::object_instantiation(instance):
    assert isinstance(instance, XHTML::Object)

@given(instance=XHTML::Object_strategy)
def test_xhtml::object_declare_type(instance):
    assert isinstance(instance.declare, str)


@given(instance=XHTML::Object_strategy)
def test_xhtml::object_declare_setter(instance):
    original = instance.declare
    instance.declare = original
    assert instance.declare == original

@given(instance=XHTML::Img_strategy)
@settings(max_examples=50)
def test_xhtml::img_instantiation(instance):
    assert isinstance(instance, XHTML::Img)

@given(instance=XHTML::Img_strategy)
def test_xhtml::img_ismap_type(instance):
    assert isinstance(instance.ismap, str)


@given(instance=XHTML::Img_strategy)
def test_xhtml::img_ismap_setter(instance):
    original = instance.ismap
    instance.ismap = original
    assert instance.ismap == original

@given(instance=XHTML::Specialpre_strategy)
@settings(max_examples=50)
def test_xhtml::specialpre_instantiation(instance):
    assert isinstance(instance, XHTML::Specialpre)

@given(instance=Number_strategy)
@settings(max_examples=50)
def test_number_instantiation(instance):
    assert isinstance(instance, Number)

@given(instance=Character_strategy)
@settings(max_examples=50)
def test_character_instantiation(instance):
    assert isinstance(instance, Character)

@given(instance=XHTML::Focus_strategy)
@settings(max_examples=50)
def test_xhtml::focus_instantiation(instance):
    assert isinstance(instance, XHTML::Focus)

@given(instance=block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, block)

@given(instance=XHTML::Blocktext_strategy)
@settings(max_examples=50)
def test_xhtml::blocktext_instantiation(instance):
    assert isinstance(instance, XHTML::Blocktext)

@given(instance=XHTML::Div_strategy)
@settings(max_examples=50)
def test_xhtml::div_instantiation(instance):
    assert isinstance(instance, XHTML::Div)

@given(instance=XHTML::Table_strategy)
@settings(max_examples=50)
def test_xhtml::table_instantiation(instance):
    assert isinstance(instance, XHTML::Table)

@given(instance=XHTML::Table_strategy)
def test_xhtml::table_frame_type(instance):
    assert isinstance(instance.frame, str)


@given(instance=XHTML::Table_strategy)
def test_xhtml::table_frame_setter(instance):
    original = instance.frame
    instance.frame = original
    assert instance.frame == original

@given(instance=XHTML::Table_strategy)
def test_xhtml::table_rules_type(instance):
    assert isinstance(instance.rules, str)


@given(instance=XHTML::Table_strategy)
def test_xhtml::table_rules_setter(instance):
    original = instance.rules
    instance.rules = original
    assert instance.rules == original

@given(instance=XHTML::Fieldset_strategy)
@settings(max_examples=50)
def test_xhtml::fieldset_instantiation(instance):
    assert isinstance(instance, XHTML::Fieldset)

@given(instance=XHTML::Lists_strategy)
@settings(max_examples=50)
def test_xhtml::lists_instantiation(instance):
    assert isinstance(instance, XHTML::Lists)

@given(instance=XHTML::P_strategy)
@settings(max_examples=50)
def test_xhtml::p_instantiation(instance):
    assert isinstance(instance, XHTML::P)

@given(instance=XHTML::Heading_strategy)
@settings(max_examples=50)
def test_xhtml::heading_instantiation(instance):
    assert isinstance(instance, XHTML::Heading)

@given(instance=PCDATA_strategy)
@settings(max_examples=50)
def test_pcdata_instantiation(instance):
    assert isinstance(instance, PCDATA)

@given(instance=XHTML::Option_strategy)
@settings(max_examples=50)
def test_xhtml::option_instantiation(instance):
    assert isinstance(instance, XHTML::Option)

@given(instance=XHTML::Option_strategy)
def test_xhtml::option_selected_type(instance):
    assert isinstance(instance.selected, str)


@given(instance=XHTML::Option_strategy)
def test_xhtml::option_selected_setter(instance):
    original = instance.selected
    instance.selected = original
    assert instance.selected == original

@given(instance=XHTML::Option_strategy)
def test_xhtml::option_disabled_type(instance):
    assert isinstance(instance.disabled, str)


@given(instance=XHTML::Option_strategy)
def test_xhtml::option_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML::Title_strategy)
@settings(max_examples=50)
def test_xhtml::title_instantiation(instance):
    assert isinstance(instance, XHTML::Title)

@given(instance=XHTML::Script_strategy)
@settings(max_examples=50)
def test_xhtml::script_instantiation(instance):
    assert isinstance(instance, XHTML::Script)

@given(instance=XHTML::Script_strategy)
def test_xhtml::script_xml_space_type(instance):
    assert isinstance(instance.xml_space, str)


@given(instance=XHTML::Script_strategy)
def test_xhtml::script_xml_space_setter(instance):
    original = instance.xml_space
    instance.xml_space = original
    assert instance.xml_space == original

@given(instance=XHTML::Script_strategy)
def test_xhtml::script_defer_type(instance):
    assert isinstance(instance.defer, str)


@given(instance=XHTML::Script_strategy)
def test_xhtml::script_defer_setter(instance):
    original = instance.defer
    instance.defer = original
    assert instance.defer == original

@given(instance=XHTML::Style_strategy)
@settings(max_examples=50)
def test_xhtml::style_instantiation(instance):
    assert isinstance(instance, XHTML::Style)

@given(instance=XHTML::Style_strategy)
def test_xhtml::style_xml_space_type(instance):
    assert isinstance(instance.xml_space, str)


@given(instance=XHTML::Style_strategy)
def test_xhtml::style_xml_space_setter(instance):
    original = instance.xml_space
    instance.xml_space = original
    assert instance.xml_space == original

@given(instance=XHTML::Textarea_strategy)
@settings(max_examples=50)
def test_xhtml::textarea_instantiation(instance):
    assert isinstance(instance, XHTML::Textarea)

@given(instance=XHTML::Textarea_strategy)
def test_xhtml::textarea_disabled_type(instance):
    assert isinstance(instance.disabled, str)


@given(instance=XHTML::Textarea_strategy)
def test_xhtml::textarea_disabled_setter(instance):
    original = instance.disabled
    instance.disabled = original
    assert instance.disabled == original

@given(instance=XHTML::Textarea_strategy)
def test_xhtml::textarea_readonly_type(instance):
    assert isinstance(instance.readonly, str)


@given(instance=XHTML::Textarea_strategy)
def test_xhtml::textarea_readonly_setter(instance):
    original = instance.readonly
    instance.readonly = original
    assert instance.readonly == original

@given(instance=FieldsetElement_strategy)
@settings(max_examples=50)
def test_fieldsetelement_instantiation(instance):
    assert isinstance(instance, FieldsetElement)

@given(instance=XHTML::Legend_strategy)
@settings(max_examples=50)
def test_xhtml::legend_instantiation(instance):
    assert isinstance(instance, XHTML::Legend)

@given(instance=MapElementContent_strategy)
@settings(max_examples=50)
def test_mapelementcontent_instantiation(instance):
    assert isinstance(instance, MapElementContent)

@given(instance=ObjectElement_strategy)
@settings(max_examples=50)
def test_objectelement_instantiation(instance):
    assert isinstance(instance, ObjectElement)

@given(instance=XHTML::Param_strategy)
@settings(max_examples=50)
def test_xhtml::param_instantiation(instance):
    assert isinstance(instance, XHTML::Param)

@given(instance=XHTML::Param_strategy)
def test_xhtml::param_valuetype_type(instance):
    assert isinstance(instance.valuetype, str)


@given(instance=XHTML::Param_strategy)
def test_xhtml::param_valuetype_setter(instance):
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

@given(instance=XHTML::Inline_strategy)
@settings(max_examples=50)
def test_xhtml::inline_instantiation(instance):
    assert isinstance(instance, XHTML::Inline)

@given(instance=Block_strategy)
@settings(max_examples=50)
def test_block_instantiation(instance):
    assert isinstance(instance, Block)

@given(instance=XHTML::block_strategy)
@settings(max_examples=50)
def test_xhtml::block_instantiation(instance):
    assert isinstance(instance, XHTML::block)

@given(instance=XHTML::Form_strategy)
@settings(max_examples=50)
def test_xhtml::form_instantiation(instance):
    assert isinstance(instance, XHTML::Form)

@given(instance=XHTML::Form_strategy)
def test_xhtml::form_method_type(instance):
    assert isinstance(instance.method, str)


@given(instance=XHTML::Form_strategy)
def test_xhtml::form_method_setter(instance):
    original = instance.method
    instance.method = original
    assert instance.method == original

@given(instance=XHTML::Misc_strategy)
@settings(max_examples=50)
def test_xhtml::misc_instantiation(instance):
    assert isinstance(instance, XHTML::Misc)

@given(instance=Inline_strategy)
@settings(max_examples=50)
def test_inline_instantiation(instance):
    assert isinstance(instance, Inline)

@given(instance=XHTML::inline_strategy)
@settings(max_examples=50)
def test_xhtml::inline_instantiation(instance):
    assert isinstance(instance, XHTML::inline)

@given(instance=Misc_strategy)
@settings(max_examples=50)
def test_misc_instantiation(instance):
    assert isinstance(instance, Misc)

@given(instance=XHTML::Noscript_strategy)
@settings(max_examples=50)
def test_xhtml::noscript_instantiation(instance):
    assert isinstance(instance, XHTML::Noscript)

@given(instance=XHTML::Miscinline_strategy)
@settings(max_examples=50)
def test_xhtml::miscinline_instantiation(instance):
    assert isinstance(instance, XHTML::Miscinline)

@given(instance=XHTML::Inlineforms_strategy)
@settings(max_examples=50)
def test_xhtml::inlineforms_instantiation(instance):
    assert isinstance(instance, XHTML::Inlineforms)

@given(instance=ScriptExpression_strategy)
@settings(max_examples=50)
def test_scriptexpression_instantiation(instance):
    assert isinstance(instance, ScriptExpression)

@given(instance=XHTML::Events_strategy)
@settings(max_examples=50)
def test_xhtml::events_instantiation(instance):
    assert isinstance(instance, XHTML::Events)

@given(instance=LanguageCode_strategy)
@settings(max_examples=50)
def test_languagecode_instantiation(instance):
    assert isinstance(instance, LanguageCode)

@given(instance=XHTML::I18n_strategy)
@settings(max_examples=50)
def test_xhtml::i18n_instantiation(instance):
    assert isinstance(instance, XHTML::I18n)

@given(instance=XHTML::I18n_strategy)
def test_xhtml::i18n_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=XHTML::I18n_strategy)
def test_xhtml::i18n_dir_setter(instance):
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

@given(instance=XHTML::Map_strategy)
@settings(max_examples=50)
def test_xhtml::map_instantiation(instance):
    assert isinstance(instance, XHTML::Map)

@given(instance=CoreAttrs_strategy)
@settings(max_examples=50)
def test_coreattrs_instantiation(instance):
    assert isinstance(instance, CoreAttrs)

@given(instance=XHTML::Br_strategy)
@settings(max_examples=50)
def test_xhtml::br_instantiation(instance):
    assert isinstance(instance, XHTML::Br)

@given(instance=XHTML::Bdo_strategy)
@settings(max_examples=50)
def test_xhtml::bdo_instantiation(instance):
    assert isinstance(instance, XHTML::Bdo)

@given(instance=XHTML::Bdo_strategy)
def test_xhtml::bdo_dir_type(instance):
    assert isinstance(instance.dir, str)


@given(instance=XHTML::Bdo_strategy)
def test_xhtml::bdo_dir_setter(instance):
    original = instance.dir
    instance.dir = original
    assert instance.dir == original

@given(instance=XHTML::Attrs_strategy)
@settings(max_examples=50)
def test_xhtml::attrs_instantiation(instance):
    assert isinstance(instance, XHTML::Attrs)

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

@given(instance=XHTML::CoreAttrs_strategy)
@settings(max_examples=50)
def test_xhtml::coreattrs_instantiation(instance):
    assert isinstance(instance, XHTML::CoreAttrs)

@given(instance=Length_strategy)
@settings(max_examples=50)
def test_length_instantiation(instance):
    assert isinstance(instance, Length)

@given(instance=XHTML::Coords_strategy)
@settings(max_examples=50)
def test_xhtml::coords_instantiation(instance):
    assert isinstance(instance, XHTML::Coords)

@given(instance=ContentType_strategy)
@settings(max_examples=50)
def test_contenttype_instantiation(instance):
    assert isinstance(instance, ContentType)

@given(instance=XHTML::ContentTypes_strategy)
@settings(max_examples=50)
def test_xhtml::contenttypes_instantiation(instance):
    assert isinstance(instance, XHTML::ContentTypes)

@given(instance=CDATA_strategy)
@settings(max_examples=50)
def test_cdata_instantiation(instance):
    assert isinstance(instance, CDATA)

@given(instance=XHTML::ScriptExpression_strategy)
@settings(max_examples=50)
def test_xhtml::scriptexpression_instantiation(instance):
    assert isinstance(instance, XHTML::ScriptExpression)

@given(instance=XHTML::Pixels_strategy)
@settings(max_examples=50)
def test_xhtml::pixels_instantiation(instance):
    assert isinstance(instance, XHTML::Pixels)

@given(instance=XHTML::Datetime_strategy)
@settings(max_examples=50)
def test_xhtml::datetime_instantiation(instance):
    assert isinstance(instance, XHTML::Datetime)

@given(instance=XHTML::MultiLength_strategy)
@settings(max_examples=50)
def test_xhtml::multilength_instantiation(instance):
    assert isinstance(instance, XHTML::MultiLength)

@given(instance=XHTML::Length_strategy)
@settings(max_examples=50)
def test_xhtml::length_instantiation(instance):
    assert isinstance(instance, XHTML::Length)

@given(instance=XHTML::StyleSheet_strategy)
@settings(max_examples=50)
def test_xhtml::stylesheet_instantiation(instance):
    assert isinstance(instance, XHTML::StyleSheet)

@given(instance=XHTML::Text_strategy)
@settings(max_examples=50)
def test_xhtml::text_instantiation(instance):
    assert isinstance(instance, XHTML::Text)

@given(instance=XHTML::ContentType_strategy)
@settings(max_examples=50)
def test_xhtml::contenttype_instantiation(instance):
    assert isinstance(instance, XHTML::ContentType)

@given(instance=XHTML::EMPTY_strategy)
@settings(max_examples=50)
def test_xhtml::empty_instantiation(instance):
    assert isinstance(instance, XHTML::EMPTY)

@given(instance=XHTML::ID_strategy)
@settings(max_examples=50)
def test_xhtml::id_instantiation(instance):
    assert isinstance(instance, XHTML::ID)

@given(instance=IDREF_strategy)
@settings(max_examples=50)
def test_idref_instantiation(instance):
    assert isinstance(instance, IDREF)

@given(instance=XHTML::IDREFS_strategy)
@settings(max_examples=50)
def test_xhtml::idrefs_instantiation(instance):
    assert isinstance(instance, XHTML::IDREFS)

@given(instance=XHTML::IDREF_strategy)
@settings(max_examples=50)
def test_xhtml::idref_instantiation(instance):
    assert isinstance(instance, XHTML::IDREF)

@given(instance=XHTML::NMTOKEN_strategy)
@settings(max_examples=50)
def test_xhtml::nmtoken_instantiation(instance):
    assert isinstance(instance, XHTML::NMTOKEN)

@given(instance=XHTML::UriList_strategy)
@settings(max_examples=50)
def test_xhtml::urilist_instantiation(instance):
    assert isinstance(instance, XHTML::UriList)

@given(instance=XHTML::URI_strategy)
@settings(max_examples=50)
def test_xhtml::uri_instantiation(instance):
    assert isinstance(instance, XHTML::URI)

@given(instance=XHTML::MediaDesc_strategy)
@settings(max_examples=50)
def test_xhtml::mediadesc_instantiation(instance):
    assert isinstance(instance, XHTML::MediaDesc)

@given(instance=XHTML::LinkTypes_strategy)
@settings(max_examples=50)
def test_xhtml::linktypes_instantiation(instance):
    assert isinstance(instance, XHTML::LinkTypes)

@given(instance=XHTML::Number_strategy)
@settings(max_examples=50)
def test_xhtml::number_instantiation(instance):
    assert isinstance(instance, XHTML::Number)

@given(instance=XHTML::Character_strategy)
@settings(max_examples=50)
def test_xhtml::character_instantiation(instance):
    assert isinstance(instance, XHTML::Character)

@given(instance=NMTOKEN_strategy)
@settings(max_examples=50)
def test_nmtoken_instantiation(instance):
    assert isinstance(instance, NMTOKEN)

@given(instance=XHTML::LanguageCode_strategy)
@settings(max_examples=50)
def test_xhtml::languagecode_instantiation(instance):
    assert isinstance(instance, XHTML::LanguageCode)

@given(instance=Charset_strategy)
@settings(max_examples=50)
def test_charset_instantiation(instance):
    assert isinstance(instance, Charset)

@given(instance=XHTML::Charsets_strategy)
@settings(max_examples=50)
def test_xhtml::charsets_instantiation(instance):
    assert isinstance(instance, XHTML::Charsets)

@given(instance=XHTML::Charset_strategy)
@settings(max_examples=50)
def test_xhtml::charset_instantiation(instance):
    assert isinstance(instance, XHTML::Charset)

@given(instance=XHTML::PCDATA_strategy)
@settings(max_examples=50)
def test_xhtml::pcdata_instantiation(instance):
    assert isinstance(instance, XHTML::PCDATA)
