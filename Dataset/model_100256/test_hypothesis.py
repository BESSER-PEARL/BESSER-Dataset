import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    AnyText,
    wikiML::AbstractFormattedInlineContent,
    HyperLink,
    wikiML::External,
    wikiML::Internal,
    AbstractUnformattedInlineContent,
    wikiML::HyperLink,
    AbstractFormattedInlineContent,
    wikiML::Italic,
    wikiML::ItalicBold,
    wikiML::Bold,
    wikiML::UnorderListItem,
    wikiML::OrderListItem,
    wikiML::Text,
    wikiML::AbstractUnformattedInlineContent,
    wikiML::WikiPage,
    Template,
    wikiML::QuoteTemplate,
    wikiML::MainTemplate,
    wikiML::AboutTemplate,
    wikiML::AnyTextSequence,
    ParagraphTypes,
    wikiML::Paragraph,
    wikiML::Heading5,
    wikiML::UnorderedList,
    wikiML::Heading3,
    wikiML::AnyText,
    wikiML::Template,
    wikiML::Heading2,
    wikiML::OrderedList,
    wikiML::Image,
    wikiML::Heading4,
    wikiML::Category,
    wikiML::BlockQuote,
    wikiML::ParagraphTypes,
    HorizontalAlign,
    ViewType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_anytext_is_not_abstract():
    assert not inspect.isabstract(AnyText)


def test_anytext_constructor_exists():
    assert callable(AnyText.__init__)


def test_anytext_constructor_args():
    sig = inspect.signature(AnyText.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::abstractformattedinlinecontent_is_not_abstract():
    assert not inspect.isabstract(wikiML::AbstractFormattedInlineContent)


def test_wikiml::abstractformattedinlinecontent_constructor_exists():
    assert callable(wikiML::AbstractFormattedInlineContent.__init__)


def test_wikiml::abstractformattedinlinecontent_constructor_args():
    sig = inspect.signature(wikiML::AbstractFormattedInlineContent.__init__)
    params = list(sig.parameters.keys())



def test_hyperlink_is_not_abstract():
    assert not inspect.isabstract(HyperLink)


def test_hyperlink_constructor_exists():
    assert callable(HyperLink.__init__)


def test_hyperlink_constructor_args():
    sig = inspect.signature(HyperLink.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::external_is_not_abstract():
    assert not inspect.isabstract(wikiML::External)


def test_wikiml::external_constructor_exists():
    assert callable(wikiML::External.__init__)


def test_wikiml::external_constructor_args():
    sig = inspect.signature(wikiML::External.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wikiml::external_has_name():
    assert hasattr(wikiML::External, "name")
    descriptor = None
    for klass in wikiML::External.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wikiml::internal_is_not_abstract():
    assert not inspect.isabstract(wikiML::Internal)


def test_wikiml::internal_constructor_exists():
    assert callable(wikiML::Internal.__init__)


def test_wikiml::internal_constructor_args():
    sig = inspect.signature(wikiML::Internal.__init__)
    params = list(sig.parameters.keys())



def test_abstractunformattedinlinecontent_is_not_abstract():
    assert not inspect.isabstract(AbstractUnformattedInlineContent)


def test_abstractunformattedinlinecontent_constructor_exists():
    assert callable(AbstractUnformattedInlineContent.__init__)


def test_abstractunformattedinlinecontent_constructor_args():
    sig = inspect.signature(AbstractUnformattedInlineContent.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::hyperlink_is_not_abstract():
    assert not inspect.isabstract(wikiML::HyperLink)


def test_wikiml::hyperlink_constructor_exists():
    assert callable(wikiML::HyperLink.__init__)


def test_wikiml::hyperlink_constructor_args():
    sig = inspect.signature(wikiML::HyperLink.__init__)
    params = list(sig.parameters.keys())



def test_abstractformattedinlinecontent_is_not_abstract():
    assert not inspect.isabstract(AbstractFormattedInlineContent)


def test_abstractformattedinlinecontent_constructor_exists():
    assert callable(AbstractFormattedInlineContent.__init__)


def test_abstractformattedinlinecontent_constructor_args():
    sig = inspect.signature(AbstractFormattedInlineContent.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::italic_is_not_abstract():
    assert not inspect.isabstract(wikiML::Italic)


def test_wikiml::italic_constructor_exists():
    assert callable(wikiML::Italic.__init__)


def test_wikiml::italic_constructor_args():
    sig = inspect.signature(wikiML::Italic.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::italicbold_is_not_abstract():
    assert not inspect.isabstract(wikiML::ItalicBold)


def test_wikiml::italicbold_constructor_exists():
    assert callable(wikiML::ItalicBold.__init__)


def test_wikiml::italicbold_constructor_args():
    sig = inspect.signature(wikiML::ItalicBold.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::bold_is_not_abstract():
    assert not inspect.isabstract(wikiML::Bold)


def test_wikiml::bold_constructor_exists():
    assert callable(wikiML::Bold.__init__)


def test_wikiml::bold_constructor_args():
    sig = inspect.signature(wikiML::Bold.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::unorderlistitem_is_not_abstract():
    assert not inspect.isabstract(wikiML::UnorderListItem)


def test_wikiml::unorderlistitem_constructor_exists():
    assert callable(wikiML::UnorderListItem.__init__)


def test_wikiml::unorderlistitem_constructor_args():
    sig = inspect.signature(wikiML::UnorderListItem.__init__)
    params = list(sig.parameters.keys())
    assert "level" in params, "Missing parameter 'level'"

def test_wikiml::unorderlistitem_has_level():
    assert hasattr(wikiML::UnorderListItem, "level")
    descriptor = None
    for klass in wikiML::UnorderListItem.__mro__:
        if "level" in klass.__dict__:
            descriptor = klass.__dict__["level"]
            break
    assert isinstance(descriptor, property)



def test_wikiml::orderlistitem_is_not_abstract():
    assert not inspect.isabstract(wikiML::OrderListItem)


def test_wikiml::orderlistitem_constructor_exists():
    assert callable(wikiML::OrderListItem.__init__)


def test_wikiml::orderlistitem_constructor_args():
    sig = inspect.signature(wikiML::OrderListItem.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::text_is_not_abstract():
    assert not inspect.isabstract(wikiML::Text)


def test_wikiml::text_constructor_exists():
    assert callable(wikiML::Text.__init__)


def test_wikiml::text_constructor_args():
    sig = inspect.signature(wikiML::Text.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wikiml::text_has_name():
    assert hasattr(wikiML::Text, "name")
    descriptor = None
    for klass in wikiML::Text.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_wikiml::abstractunformattedinlinecontent_is_not_abstract():
    assert not inspect.isabstract(wikiML::AbstractUnformattedInlineContent)


def test_wikiml::abstractunformattedinlinecontent_constructor_exists():
    assert callable(wikiML::AbstractUnformattedInlineContent.__init__)


def test_wikiml::abstractunformattedinlinecontent_constructor_args():
    sig = inspect.signature(wikiML::AbstractUnformattedInlineContent.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::wikipage_is_not_abstract():
    assert not inspect.isabstract(wikiML::WikiPage)


def test_wikiml::wikipage_constructor_exists():
    assert callable(wikiML::WikiPage.__init__)


def test_wikiml::wikipage_constructor_args():
    sig = inspect.signature(wikiML::WikiPage.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wikiml::wikipage_has_name():
    assert hasattr(wikiML::WikiPage, "name")
    descriptor = None
    for klass in wikiML::WikiPage.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_template_is_not_abstract():
    assert not inspect.isabstract(Template)


def test_template_constructor_exists():
    assert callable(Template.__init__)


def test_template_constructor_args():
    sig = inspect.signature(Template.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::quotetemplate_is_not_abstract():
    assert not inspect.isabstract(wikiML::QuoteTemplate)


def test_wikiml::quotetemplate_constructor_exists():
    assert callable(wikiML::QuoteTemplate.__init__)


def test_wikiml::quotetemplate_constructor_args():
    sig = inspect.signature(wikiML::QuoteTemplate.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::maintemplate_is_not_abstract():
    assert not inspect.isabstract(wikiML::MainTemplate)


def test_wikiml::maintemplate_constructor_exists():
    assert callable(wikiML::MainTemplate.__init__)


def test_wikiml::maintemplate_constructor_args():
    sig = inspect.signature(wikiML::MainTemplate.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::abouttemplate_is_not_abstract():
    assert not inspect.isabstract(wikiML::AboutTemplate)


def test_wikiml::abouttemplate_constructor_exists():
    assert callable(wikiML::AboutTemplate.__init__)


def test_wikiml::abouttemplate_constructor_args():
    sig = inspect.signature(wikiML::AboutTemplate.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::anytextsequence_is_not_abstract():
    assert not inspect.isabstract(wikiML::AnyTextSequence)


def test_wikiml::anytextsequence_constructor_exists():
    assert callable(wikiML::AnyTextSequence.__init__)


def test_wikiml::anytextsequence_constructor_args():
    sig = inspect.signature(wikiML::AnyTextSequence.__init__)
    params = list(sig.parameters.keys())



def test_paragraphtypes_is_not_abstract():
    assert not inspect.isabstract(ParagraphTypes)


def test_paragraphtypes_constructor_exists():
    assert callable(ParagraphTypes.__init__)


def test_paragraphtypes_constructor_args():
    sig = inspect.signature(ParagraphTypes.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::paragraph_is_not_abstract():
    assert not inspect.isabstract(wikiML::Paragraph)


def test_wikiml::paragraph_constructor_exists():
    assert callable(wikiML::Paragraph.__init__)


def test_wikiml::paragraph_constructor_args():
    sig = inspect.signature(wikiML::Paragraph.__init__)
    params = list(sig.parameters.keys())
    assert "paragraph" in params, "Missing parameter 'paragraph'"

def test_wikiml::paragraph_has_paragraph():
    assert hasattr(wikiML::Paragraph, "paragraph")
    descriptor = None
    for klass in wikiML::Paragraph.__mro__:
        if "paragraph" in klass.__dict__:
            descriptor = klass.__dict__["paragraph"]
            break
    assert isinstance(descriptor, property)



def test_wikiml::heading5_is_not_abstract():
    assert not inspect.isabstract(wikiML::Heading5)


def test_wikiml::heading5_constructor_exists():
    assert callable(wikiML::Heading5.__init__)


def test_wikiml::heading5_constructor_args():
    sig = inspect.signature(wikiML::Heading5.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::unorderedlist_is_not_abstract():
    assert not inspect.isabstract(wikiML::UnorderedList)


def test_wikiml::unorderedlist_constructor_exists():
    assert callable(wikiML::UnorderedList.__init__)


def test_wikiml::unorderedlist_constructor_args():
    sig = inspect.signature(wikiML::UnorderedList.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::heading3_is_not_abstract():
    assert not inspect.isabstract(wikiML::Heading3)


def test_wikiml::heading3_constructor_exists():
    assert callable(wikiML::Heading3.__init__)


def test_wikiml::heading3_constructor_args():
    sig = inspect.signature(wikiML::Heading3.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::anytext_is_not_abstract():
    assert not inspect.isabstract(wikiML::AnyText)


def test_wikiml::anytext_constructor_exists():
    assert callable(wikiML::AnyText.__init__)


def test_wikiml::anytext_constructor_args():
    sig = inspect.signature(wikiML::AnyText.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::template_is_not_abstract():
    assert not inspect.isabstract(wikiML::Template)


def test_wikiml::template_constructor_exists():
    assert callable(wikiML::Template.__init__)


def test_wikiml::template_constructor_args():
    sig = inspect.signature(wikiML::Template.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_wikiml::template_has_type():
    assert hasattr(wikiML::Template, "type")
    descriptor = None
    for klass in wikiML::Template.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_wikiml::heading2_is_not_abstract():
    assert not inspect.isabstract(wikiML::Heading2)


def test_wikiml::heading2_constructor_exists():
    assert callable(wikiML::Heading2.__init__)


def test_wikiml::heading2_constructor_args():
    sig = inspect.signature(wikiML::Heading2.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::orderedlist_is_not_abstract():
    assert not inspect.isabstract(wikiML::OrderedList)


def test_wikiml::orderedlist_constructor_exists():
    assert callable(wikiML::OrderedList.__init__)


def test_wikiml::orderedlist_constructor_args():
    sig = inspect.signature(wikiML::OrderedList.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::image_is_not_abstract():
    assert not inspect.isabstract(wikiML::Image)


def test_wikiml::image_constructor_exists():
    assert callable(wikiML::Image.__init__)


def test_wikiml::image_constructor_args():
    sig = inspect.signature(wikiML::Image.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "hAlign" in params, "Missing parameter 'hAlign'"
    assert "type" in params, "Missing parameter 'type'"

def test_wikiml::image_has_name():
    assert hasattr(wikiML::Image, "name")
    descriptor = None
    for klass in wikiML::Image.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_wikiml::image_has_hAlign():
    assert hasattr(wikiML::Image, "hAlign")
    descriptor = None
    for klass in wikiML::Image.__mro__:
        if "hAlign" in klass.__dict__:
            descriptor = klass.__dict__["hAlign"]
            break
    assert isinstance(descriptor, property)

def test_wikiml::image_has_type():
    assert hasattr(wikiML::Image, "type")
    descriptor = None
    for klass in wikiML::Image.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_wikiml::heading4_is_not_abstract():
    assert not inspect.isabstract(wikiML::Heading4)


def test_wikiml::heading4_constructor_exists():
    assert callable(wikiML::Heading4.__init__)


def test_wikiml::heading4_constructor_args():
    sig = inspect.signature(wikiML::Heading4.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::category_is_not_abstract():
    assert not inspect.isabstract(wikiML::Category)


def test_wikiml::category_constructor_exists():
    assert callable(wikiML::Category.__init__)


def test_wikiml::category_constructor_args():
    sig = inspect.signature(wikiML::Category.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wikiml::category_has_value():
    assert hasattr(wikiML::Category, "value")
    descriptor = None
    for klass in wikiML::Category.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wikiml::blockquote_is_not_abstract():
    assert not inspect.isabstract(wikiML::BlockQuote)


def test_wikiml::blockquote_constructor_exists():
    assert callable(wikiML::BlockQuote.__init__)


def test_wikiml::blockquote_constructor_args():
    sig = inspect.signature(wikiML::BlockQuote.__init__)
    params = list(sig.parameters.keys())



def test_wikiml::paragraphtypes_is_not_abstract():
    assert not inspect.isabstract(wikiML::ParagraphTypes)


def test_wikiml::paragraphtypes_constructor_exists():
    assert callable(wikiML::ParagraphTypes.__init__)


def test_wikiml::paragraphtypes_constructor_args():
    sig = inspect.signature(wikiML::ParagraphTypes.__init__)
    params = list(sig.parameters.keys())

def test_horizontalalign_exists():
    # Check that the Enumeration exists
    assert HorizontalAlign is not None

def test_horizontalalign_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in HorizontalAlign]
    expected_literals = [
        "right",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in HorizontalAlign"

def test_viewtype_exists():
    # Check that the Enumeration exists
    assert ViewType is not None

def test_viewtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in ViewType]
    expected_literals = [
        "thumb",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in ViewType"


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
AnyText_strategy = st.builds(
    AnyText,
)
wikiML::AbstractFormattedInlineContent_strategy = st.builds(
    wikiML::AbstractFormattedInlineContent,
)
HyperLink_strategy = st.builds(
    HyperLink,
)
wikiML::External_strategy = st.builds(
    wikiML::External,
    name=
        safe_text
)
wikiML::Internal_strategy = st.builds(
    wikiML::Internal,
)
AbstractUnformattedInlineContent_strategy = st.builds(
    AbstractUnformattedInlineContent,
)
wikiML::HyperLink_strategy = st.builds(
    wikiML::HyperLink,
)
AbstractFormattedInlineContent_strategy = st.builds(
    AbstractFormattedInlineContent,
)
wikiML::Italic_strategy = st.builds(
    wikiML::Italic,
)
wikiML::ItalicBold_strategy = st.builds(
    wikiML::ItalicBold,
)
wikiML::Bold_strategy = st.builds(
    wikiML::Bold,
)
wikiML::UnorderListItem_strategy = st.builds(
    wikiML::UnorderListItem,
    level=
        safe_text
)
wikiML::OrderListItem_strategy = st.builds(
    wikiML::OrderListItem,
)
wikiML::Text_strategy = st.builds(
    wikiML::Text,
    name=
        safe_text
)
wikiML::AbstractUnformattedInlineContent_strategy = st.builds(
    wikiML::AbstractUnformattedInlineContent,
)
wikiML::WikiPage_strategy = st.builds(
    wikiML::WikiPage,
    name=
        safe_text
)
Template_strategy = st.builds(
    Template,
)
wikiML::QuoteTemplate_strategy = st.builds(
    wikiML::QuoteTemplate,
)
wikiML::MainTemplate_strategy = st.builds(
    wikiML::MainTemplate,
)
wikiML::AboutTemplate_strategy = st.builds(
    wikiML::AboutTemplate,
)
wikiML::AnyTextSequence_strategy = st.builds(
    wikiML::AnyTextSequence,
)
ParagraphTypes_strategy = st.builds(
    ParagraphTypes,
)
wikiML::Paragraph_strategy = st.builds(
    wikiML::Paragraph,
    paragraph=
        safe_text
)
wikiML::Heading5_strategy = st.builds(
    wikiML::Heading5,
)
wikiML::UnorderedList_strategy = st.builds(
    wikiML::UnorderedList,
)
wikiML::Heading3_strategy = st.builds(
    wikiML::Heading3,
)
wikiML::AnyText_strategy = st.builds(
    wikiML::AnyText,
)
wikiML::Template_strategy = st.builds(
    wikiML::Template,
    type=
        safe_text
)
wikiML::Heading2_strategy = st.builds(
    wikiML::Heading2,
)
wikiML::OrderedList_strategy = st.builds(
    wikiML::OrderedList,
)
wikiML::Image_strategy = st.builds(
    wikiML::Image,
    name=
        safe_text,
    hAlign=
        safe_text,
    type=
        safe_text
)
wikiML::Heading4_strategy = st.builds(
    wikiML::Heading4,
)
wikiML::Category_strategy = st.builds(
    wikiML::Category,
    value=
        safe_text
)
wikiML::BlockQuote_strategy = st.builds(
    wikiML::BlockQuote,
)
wikiML::ParagraphTypes_strategy = st.builds(
    wikiML::ParagraphTypes,
)

@given(instance=AnyText_strategy)
@settings(max_examples=50)
def test_anytext_instantiation(instance):
    assert isinstance(instance, AnyText)

@given(instance=wikiML::AbstractFormattedInlineContent_strategy)
@settings(max_examples=50)
def test_wikiml::abstractformattedinlinecontent_instantiation(instance):
    assert isinstance(instance, wikiML::AbstractFormattedInlineContent)

@given(instance=HyperLink_strategy)
@settings(max_examples=50)
def test_hyperlink_instantiation(instance):
    assert isinstance(instance, HyperLink)

@given(instance=wikiML::External_strategy)
@settings(max_examples=50)
def test_wikiml::external_instantiation(instance):
    assert isinstance(instance, wikiML::External)

@given(instance=wikiML::External_strategy)
def test_wikiml::external_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wikiML::External_strategy)
def test_wikiml::external_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wikiML::Internal_strategy)
@settings(max_examples=50)
def test_wikiml::internal_instantiation(instance):
    assert isinstance(instance, wikiML::Internal)

@given(instance=AbstractUnformattedInlineContent_strategy)
@settings(max_examples=50)
def test_abstractunformattedinlinecontent_instantiation(instance):
    assert isinstance(instance, AbstractUnformattedInlineContent)

@given(instance=wikiML::HyperLink_strategy)
@settings(max_examples=50)
def test_wikiml::hyperlink_instantiation(instance):
    assert isinstance(instance, wikiML::HyperLink)

@given(instance=AbstractFormattedInlineContent_strategy)
@settings(max_examples=50)
def test_abstractformattedinlinecontent_instantiation(instance):
    assert isinstance(instance, AbstractFormattedInlineContent)

@given(instance=wikiML::Italic_strategy)
@settings(max_examples=50)
def test_wikiml::italic_instantiation(instance):
    assert isinstance(instance, wikiML::Italic)

@given(instance=wikiML::ItalicBold_strategy)
@settings(max_examples=50)
def test_wikiml::italicbold_instantiation(instance):
    assert isinstance(instance, wikiML::ItalicBold)

@given(instance=wikiML::Bold_strategy)
@settings(max_examples=50)
def test_wikiml::bold_instantiation(instance):
    assert isinstance(instance, wikiML::Bold)

@given(instance=wikiML::UnorderListItem_strategy)
@settings(max_examples=50)
def test_wikiml::unorderlistitem_instantiation(instance):
    assert isinstance(instance, wikiML::UnorderListItem)

@given(instance=wikiML::UnorderListItem_strategy)
def test_wikiml::unorderlistitem_level_type(instance):
    assert isinstance(instance.level, str)


@given(instance=wikiML::UnorderListItem_strategy)
def test_wikiml::unorderlistitem_level_setter(instance):
    original = instance.level
    instance.level = original
    assert instance.level == original

@given(instance=wikiML::OrderListItem_strategy)
@settings(max_examples=50)
def test_wikiml::orderlistitem_instantiation(instance):
    assert isinstance(instance, wikiML::OrderListItem)

@given(instance=wikiML::Text_strategy)
@settings(max_examples=50)
def test_wikiml::text_instantiation(instance):
    assert isinstance(instance, wikiML::Text)

@given(instance=wikiML::Text_strategy)
def test_wikiml::text_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wikiML::Text_strategy)
def test_wikiml::text_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wikiML::AbstractUnformattedInlineContent_strategy)
@settings(max_examples=50)
def test_wikiml::abstractunformattedinlinecontent_instantiation(instance):
    assert isinstance(instance, wikiML::AbstractUnformattedInlineContent)

@given(instance=wikiML::WikiPage_strategy)
@settings(max_examples=50)
def test_wikiml::wikipage_instantiation(instance):
    assert isinstance(instance, wikiML::WikiPage)

@given(instance=wikiML::WikiPage_strategy)
def test_wikiml::wikipage_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wikiML::WikiPage_strategy)
def test_wikiml::wikipage_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Template_strategy)
@settings(max_examples=50)
def test_template_instantiation(instance):
    assert isinstance(instance, Template)

@given(instance=wikiML::QuoteTemplate_strategy)
@settings(max_examples=50)
def test_wikiml::quotetemplate_instantiation(instance):
    assert isinstance(instance, wikiML::QuoteTemplate)

@given(instance=wikiML::MainTemplate_strategy)
@settings(max_examples=50)
def test_wikiml::maintemplate_instantiation(instance):
    assert isinstance(instance, wikiML::MainTemplate)

@given(instance=wikiML::AboutTemplate_strategy)
@settings(max_examples=50)
def test_wikiml::abouttemplate_instantiation(instance):
    assert isinstance(instance, wikiML::AboutTemplate)

@given(instance=wikiML::AnyTextSequence_strategy)
@settings(max_examples=50)
def test_wikiml::anytextsequence_instantiation(instance):
    assert isinstance(instance, wikiML::AnyTextSequence)

@given(instance=ParagraphTypes_strategy)
@settings(max_examples=50)
def test_paragraphtypes_instantiation(instance):
    assert isinstance(instance, ParagraphTypes)

@given(instance=wikiML::Paragraph_strategy)
@settings(max_examples=50)
def test_wikiml::paragraph_instantiation(instance):
    assert isinstance(instance, wikiML::Paragraph)

@given(instance=wikiML::Paragraph_strategy)
def test_wikiml::paragraph_paragraph_type(instance):
    assert isinstance(instance.paragraph, str)


@given(instance=wikiML::Paragraph_strategy)
def test_wikiml::paragraph_paragraph_setter(instance):
    original = instance.paragraph
    instance.paragraph = original
    assert instance.paragraph == original

@given(instance=wikiML::Heading5_strategy)
@settings(max_examples=50)
def test_wikiml::heading5_instantiation(instance):
    assert isinstance(instance, wikiML::Heading5)

@given(instance=wikiML::UnorderedList_strategy)
@settings(max_examples=50)
def test_wikiml::unorderedlist_instantiation(instance):
    assert isinstance(instance, wikiML::UnorderedList)

@given(instance=wikiML::Heading3_strategy)
@settings(max_examples=50)
def test_wikiml::heading3_instantiation(instance):
    assert isinstance(instance, wikiML::Heading3)

@given(instance=wikiML::AnyText_strategy)
@settings(max_examples=50)
def test_wikiml::anytext_instantiation(instance):
    assert isinstance(instance, wikiML::AnyText)

@given(instance=wikiML::Template_strategy)
@settings(max_examples=50)
def test_wikiml::template_instantiation(instance):
    assert isinstance(instance, wikiML::Template)

@given(instance=wikiML::Template_strategy)
def test_wikiml::template_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=wikiML::Template_strategy)
def test_wikiml::template_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=wikiML::Heading2_strategy)
@settings(max_examples=50)
def test_wikiml::heading2_instantiation(instance):
    assert isinstance(instance, wikiML::Heading2)

@given(instance=wikiML::OrderedList_strategy)
@settings(max_examples=50)
def test_wikiml::orderedlist_instantiation(instance):
    assert isinstance(instance, wikiML::OrderedList)

@given(instance=wikiML::Image_strategy)
@settings(max_examples=50)
def test_wikiml::image_instantiation(instance):
    assert isinstance(instance, wikiML::Image)

@given(instance=wikiML::Image_strategy)
def test_wikiml::image_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=wikiML::Image_strategy)
def test_wikiml::image_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=wikiML::Image_strategy)
def test_wikiml::image_hAlign_type(instance):
    assert isinstance(instance.hAlign, str)


@given(instance=wikiML::Image_strategy)
def test_wikiml::image_hAlign_setter(instance):
    original = instance.hAlign
    instance.hAlign = original
    assert instance.hAlign == original

@given(instance=wikiML::Image_strategy)
def test_wikiml::image_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=wikiML::Image_strategy)
def test_wikiml::image_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=wikiML::Heading4_strategy)
@settings(max_examples=50)
def test_wikiml::heading4_instantiation(instance):
    assert isinstance(instance, wikiML::Heading4)

@given(instance=wikiML::Category_strategy)
@settings(max_examples=50)
def test_wikiml::category_instantiation(instance):
    assert isinstance(instance, wikiML::Category)

@given(instance=wikiML::Category_strategy)
def test_wikiml::category_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=wikiML::Category_strategy)
def test_wikiml::category_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=wikiML::BlockQuote_strategy)
@settings(max_examples=50)
def test_wikiml::blockquote_instantiation(instance):
    assert isinstance(instance, wikiML::BlockQuote)

@given(instance=wikiML::ParagraphTypes_strategy)
@settings(max_examples=50)
def test_wikiml::paragraphtypes_instantiation(instance):
    assert isinstance(instance, wikiML::ParagraphTypes)
