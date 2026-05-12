import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    xdoc::GlossaryEntry,
    xdoc::MarkupInCode,
    xdoc::Code,
    Part,
    xdoc::PartRef,
    xdoc::JvmDeclaredType,
    xdoc::ImageProxy,
    MarkupInCode,
    xdoc::Item,
    Identifiable,
    xdoc::TableData,
    xdoc::TableRow,
    MarkUp,
    xdoc::OrderedList,
    xdoc::CodeRef,
    xdoc::ImageRef,
    xdoc::Ref,
    xdoc::Anchor,
    xdoc::Todo,
    xdoc::UnorderedList,
    xdoc::Link,
    xdoc::Emphasize,
    xdoc::CodeBlock,
    xdoc::Table,
    xdoc::MarkUp,
    xdoc::TextPart,
    xdoc::EObject,
    xdoc::Identifiable,
    Chapter,
    xdoc::ChapterRef,
    Section2,
    xdoc::Section2Ref,
    Section,
    xdoc::SectionRef,
    xdoc::AbstractSection,
    xdoc::XdocFile,
    xdoc::Glossary,
    xdoc::LangDef,
    xdoc::TextOrMarkup,
    AbstractSection,
    xdoc::Section3,
    xdoc::Section4,
    xdoc::Part,
    xdoc::Section2,
    xdoc::Section,
    xdoc::Chapter,
    xdoc::Document,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xdoc::glossaryentry_is_not_abstract():
    assert not inspect.isabstract(xdoc::GlossaryEntry)


def test_xdoc::glossaryentry_constructor_exists():
    assert callable(xdoc::GlossaryEntry.__init__)


def test_xdoc::glossaryentry_constructor_args():
    sig = inspect.signature(xdoc::GlossaryEntry.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "alias" in params, "Missing parameter 'alias'"

def test_xdoc::glossaryentry_has_name():
    assert hasattr(xdoc::GlossaryEntry, "name")
    descriptor = None
    for klass in xdoc::GlossaryEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xdoc::glossaryentry_has_alias():
    assert hasattr(xdoc::GlossaryEntry, "alias")
    descriptor = None
    for klass in xdoc::GlossaryEntry.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)



def test_xdoc::markupincode_is_not_abstract():
    assert not inspect.isabstract(xdoc::MarkupInCode)


def test_xdoc::markupincode_constructor_exists():
    assert callable(xdoc::MarkupInCode.__init__)


def test_xdoc::markupincode_constructor_args():
    sig = inspect.signature(xdoc::MarkupInCode.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::code_is_not_abstract():
    assert not inspect.isabstract(xdoc::Code)


def test_xdoc::code_constructor_exists():
    assert callable(xdoc::Code.__init__)


def test_xdoc::code_constructor_args():
    sig = inspect.signature(xdoc::Code.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"

def test_xdoc::code_has_contents():
    assert hasattr(xdoc::Code, "contents")
    descriptor = None
    for klass in xdoc::Code.__mro__:
        if "contents" in klass.__dict__:
            descriptor = klass.__dict__["contents"]
            break
    assert isinstance(descriptor, property)



def test_part_is_not_abstract():
    assert not inspect.isabstract(Part)


def test_part_constructor_exists():
    assert callable(Part.__init__)


def test_part_constructor_args():
    sig = inspect.signature(Part.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::partref_is_not_abstract():
    assert not inspect.isabstract(xdoc::PartRef)


def test_xdoc::partref_constructor_exists():
    assert callable(xdoc::PartRef.__init__)


def test_xdoc::partref_constructor_args():
    sig = inspect.signature(xdoc::PartRef.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::jvmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(xdoc::JvmDeclaredType)


def test_xdoc::jvmdeclaredtype_constructor_exists():
    assert callable(xdoc::JvmDeclaredType.__init__)


def test_xdoc::jvmdeclaredtype_constructor_args():
    sig = inspect.signature(xdoc::JvmDeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::imageproxy_is_not_abstract():
    assert not inspect.isabstract(xdoc::ImageProxy)


def test_xdoc::imageproxy_constructor_exists():
    assert callable(xdoc::ImageProxy.__init__)


def test_xdoc::imageproxy_constructor_args():
    sig = inspect.signature(xdoc::ImageProxy.__init__)
    params = list(sig.parameters.keys())



def test_markupincode_is_not_abstract():
    assert not inspect.isabstract(MarkupInCode)


def test_markupincode_constructor_exists():
    assert callable(MarkupInCode.__init__)


def test_markupincode_constructor_args():
    sig = inspect.signature(MarkupInCode.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::item_is_not_abstract():
    assert not inspect.isabstract(xdoc::Item)


def test_xdoc::item_constructor_exists():
    assert callable(xdoc::Item.__init__)


def test_xdoc::item_constructor_args():
    sig = inspect.signature(xdoc::Item.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::tabledata_is_not_abstract():
    assert not inspect.isabstract(xdoc::TableData)


def test_xdoc::tabledata_constructor_exists():
    assert callable(xdoc::TableData.__init__)


def test_xdoc::tabledata_constructor_args():
    sig = inspect.signature(xdoc::TableData.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::tablerow_is_not_abstract():
    assert not inspect.isabstract(xdoc::TableRow)


def test_xdoc::tablerow_constructor_exists():
    assert callable(xdoc::TableRow.__init__)


def test_xdoc::tablerow_constructor_args():
    sig = inspect.signature(xdoc::TableRow.__init__)
    params = list(sig.parameters.keys())



def test_markup_is_not_abstract():
    assert not inspect.isabstract(MarkUp)


def test_markup_constructor_exists():
    assert callable(MarkUp.__init__)


def test_markup_constructor_args():
    sig = inspect.signature(MarkUp.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::orderedlist_is_not_abstract():
    assert not inspect.isabstract(xdoc::OrderedList)


def test_xdoc::orderedlist_constructor_exists():
    assert callable(xdoc::OrderedList.__init__)


def test_xdoc::orderedlist_constructor_args():
    sig = inspect.signature(xdoc::OrderedList.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::coderef_is_not_abstract():
    assert not inspect.isabstract(xdoc::CodeRef)


def test_xdoc::coderef_constructor_exists():
    assert callable(xdoc::CodeRef.__init__)


def test_xdoc::coderef_constructor_args():
    sig = inspect.signature(xdoc::CodeRef.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::imageref_is_not_abstract():
    assert not inspect.isabstract(xdoc::ImageRef)


def test_xdoc::imageref_constructor_exists():
    assert callable(xdoc::ImageRef.__init__)


def test_xdoc::imageref_constructor_args():
    sig = inspect.signature(xdoc::ImageRef.__init__)
    params = list(sig.parameters.keys())
    assert "path" in params, "Missing parameter 'path'"
    assert "name" in params, "Missing parameter 'name'"
    assert "caption" in params, "Missing parameter 'caption'"
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "style" in params, "Missing parameter 'style'"

def test_xdoc::imageref_has_path():
    assert hasattr(xdoc::ImageRef, "path")
    descriptor = None
    for klass in xdoc::ImageRef.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_xdoc::imageref_has_name():
    assert hasattr(xdoc::ImageRef, "name")
    descriptor = None
    for klass in xdoc::ImageRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xdoc::imageref_has_caption():
    assert hasattr(xdoc::ImageRef, "caption")
    descriptor = None
    for klass in xdoc::ImageRef.__mro__:
        if "caption" in klass.__dict__:
            descriptor = klass.__dict__["caption"]
            break
    assert isinstance(descriptor, property)

def test_xdoc::imageref_has_clazz():
    assert hasattr(xdoc::ImageRef, "clazz")
    descriptor = None
    for klass in xdoc::ImageRef.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_xdoc::imageref_has_style():
    assert hasattr(xdoc::ImageRef, "style")
    descriptor = None
    for klass in xdoc::ImageRef.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)



def test_xdoc::ref_is_not_abstract():
    assert not inspect.isabstract(xdoc::Ref)


def test_xdoc::ref_constructor_exists():
    assert callable(xdoc::Ref.__init__)


def test_xdoc::ref_constructor_args():
    sig = inspect.signature(xdoc::Ref.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::anchor_is_not_abstract():
    assert not inspect.isabstract(xdoc::Anchor)


def test_xdoc::anchor_constructor_exists():
    assert callable(xdoc::Anchor.__init__)


def test_xdoc::anchor_constructor_args():
    sig = inspect.signature(xdoc::Anchor.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::todo_is_not_abstract():
    assert not inspect.isabstract(xdoc::Todo)


def test_xdoc::todo_constructor_exists():
    assert callable(xdoc::Todo.__init__)


def test_xdoc::todo_constructor_args():
    sig = inspect.signature(xdoc::Todo.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_xdoc::todo_has_text():
    assert hasattr(xdoc::Todo, "text")
    descriptor = None
    for klass in xdoc::Todo.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_xdoc::unorderedlist_is_not_abstract():
    assert not inspect.isabstract(xdoc::UnorderedList)


def test_xdoc::unorderedlist_constructor_exists():
    assert callable(xdoc::UnorderedList.__init__)


def test_xdoc::unorderedlist_constructor_args():
    sig = inspect.signature(xdoc::UnorderedList.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::link_is_not_abstract():
    assert not inspect.isabstract(xdoc::Link)


def test_xdoc::link_constructor_exists():
    assert callable(xdoc::Link.__init__)


def test_xdoc::link_constructor_args():
    sig = inspect.signature(xdoc::Link.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "text" in params, "Missing parameter 'text'"

def test_xdoc::link_has_url():
    assert hasattr(xdoc::Link, "url")
    descriptor = None
    for klass in xdoc::Link.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_xdoc::link_has_text():
    assert hasattr(xdoc::Link, "text")
    descriptor = None
    for klass in xdoc::Link.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_xdoc::emphasize_is_not_abstract():
    assert not inspect.isabstract(xdoc::Emphasize)


def test_xdoc::emphasize_constructor_exists():
    assert callable(xdoc::Emphasize.__init__)


def test_xdoc::emphasize_constructor_args():
    sig = inspect.signature(xdoc::Emphasize.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::codeblock_is_not_abstract():
    assert not inspect.isabstract(xdoc::CodeBlock)


def test_xdoc::codeblock_constructor_exists():
    assert callable(xdoc::CodeBlock.__init__)


def test_xdoc::codeblock_constructor_args():
    sig = inspect.signature(xdoc::CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::table_is_not_abstract():
    assert not inspect.isabstract(xdoc::Table)


def test_xdoc::table_constructor_exists():
    assert callable(xdoc::Table.__init__)


def test_xdoc::table_constructor_args():
    sig = inspect.signature(xdoc::Table.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::markup_is_not_abstract():
    assert not inspect.isabstract(xdoc::MarkUp)


def test_xdoc::markup_constructor_exists():
    assert callable(xdoc::MarkUp.__init__)


def test_xdoc::markup_constructor_args():
    sig = inspect.signature(xdoc::MarkUp.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::textpart_is_not_abstract():
    assert not inspect.isabstract(xdoc::TextPart)


def test_xdoc::textpart_constructor_exists():
    assert callable(xdoc::TextPart.__init__)


def test_xdoc::textpart_constructor_args():
    sig = inspect.signature(xdoc::TextPart.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_xdoc::textpart_has_text():
    assert hasattr(xdoc::TextPart, "text")
    descriptor = None
    for klass in xdoc::TextPart.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_xdoc::eobject_is_not_abstract():
    assert not inspect.isabstract(xdoc::EObject)


def test_xdoc::eobject_constructor_exists():
    assert callable(xdoc::EObject.__init__)


def test_xdoc::eobject_constructor_args():
    sig = inspect.signature(xdoc::EObject.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::identifiable_is_not_abstract():
    assert not inspect.isabstract(xdoc::Identifiable)


def test_xdoc::identifiable_constructor_exists():
    assert callable(xdoc::Identifiable.__init__)


def test_xdoc::identifiable_constructor_args():
    sig = inspect.signature(xdoc::Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xdoc::identifiable_has_name():
    assert hasattr(xdoc::Identifiable, "name")
    descriptor = None
    for klass in xdoc::Identifiable.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_chapter_is_not_abstract():
    assert not inspect.isabstract(Chapter)


def test_chapter_constructor_exists():
    assert callable(Chapter.__init__)


def test_chapter_constructor_args():
    sig = inspect.signature(Chapter.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::chapterref_is_not_abstract():
    assert not inspect.isabstract(xdoc::ChapterRef)


def test_xdoc::chapterref_constructor_exists():
    assert callable(xdoc::ChapterRef.__init__)


def test_xdoc::chapterref_constructor_args():
    sig = inspect.signature(xdoc::ChapterRef.__init__)
    params = list(sig.parameters.keys())



def test_section2_is_not_abstract():
    assert not inspect.isabstract(Section2)


def test_section2_constructor_exists():
    assert callable(Section2.__init__)


def test_section2_constructor_args():
    sig = inspect.signature(Section2.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::section2ref_is_not_abstract():
    assert not inspect.isabstract(xdoc::Section2Ref)


def test_xdoc::section2ref_constructor_exists():
    assert callable(xdoc::Section2Ref.__init__)


def test_xdoc::section2ref_constructor_args():
    sig = inspect.signature(xdoc::Section2Ref.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::sectionref_is_not_abstract():
    assert not inspect.isabstract(xdoc::SectionRef)


def test_xdoc::sectionref_constructor_exists():
    assert callable(xdoc::SectionRef.__init__)


def test_xdoc::sectionref_constructor_args():
    sig = inspect.signature(xdoc::SectionRef.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::abstractsection_is_not_abstract():
    assert not inspect.isabstract(xdoc::AbstractSection)


def test_xdoc::abstractsection_constructor_exists():
    assert callable(xdoc::AbstractSection.__init__)


def test_xdoc::abstractsection_constructor_args():
    sig = inspect.signature(xdoc::AbstractSection.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::xdocfile_is_not_abstract():
    assert not inspect.isabstract(xdoc::XdocFile)


def test_xdoc::xdocfile_constructor_exists():
    assert callable(xdoc::XdocFile.__init__)


def test_xdoc::xdocfile_constructor_args():
    sig = inspect.signature(xdoc::XdocFile.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::glossary_is_not_abstract():
    assert not inspect.isabstract(xdoc::Glossary)


def test_xdoc::glossary_constructor_exists():
    assert callable(xdoc::Glossary.__init__)


def test_xdoc::glossary_constructor_args():
    sig = inspect.signature(xdoc::Glossary.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::langdef_is_not_abstract():
    assert not inspect.isabstract(xdoc::LangDef)


def test_xdoc::langdef_constructor_exists():
    assert callable(xdoc::LangDef.__init__)


def test_xdoc::langdef_constructor_args():
    sig = inspect.signature(xdoc::LangDef.__init__)
    params = list(sig.parameters.keys())
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "name" in params, "Missing parameter 'name'"

def test_xdoc::langdef_has_keywords():
    assert hasattr(xdoc::LangDef, "keywords")
    descriptor = None
    for klass in xdoc::LangDef.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_xdoc::langdef_has_name():
    assert hasattr(xdoc::LangDef, "name")
    descriptor = None
    for klass in xdoc::LangDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xdoc::textormarkup_is_not_abstract():
    assert not inspect.isabstract(xdoc::TextOrMarkup)


def test_xdoc::textormarkup_constructor_exists():
    assert callable(xdoc::TextOrMarkup.__init__)


def test_xdoc::textormarkup_constructor_args():
    sig = inspect.signature(xdoc::TextOrMarkup.__init__)
    params = list(sig.parameters.keys())



def test_abstractsection_is_not_abstract():
    assert not inspect.isabstract(AbstractSection)


def test_abstractsection_constructor_exists():
    assert callable(AbstractSection.__init__)


def test_abstractsection_constructor_args():
    sig = inspect.signature(AbstractSection.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::section3_is_not_abstract():
    assert not inspect.isabstract(xdoc::Section3)


def test_xdoc::section3_constructor_exists():
    assert callable(xdoc::Section3.__init__)


def test_xdoc::section3_constructor_args():
    sig = inspect.signature(xdoc::Section3.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::section4_is_not_abstract():
    assert not inspect.isabstract(xdoc::Section4)


def test_xdoc::section4_constructor_exists():
    assert callable(xdoc::Section4.__init__)


def test_xdoc::section4_constructor_args():
    sig = inspect.signature(xdoc::Section4.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::part_is_not_abstract():
    assert not inspect.isabstract(xdoc::Part)


def test_xdoc::part_constructor_exists():
    assert callable(xdoc::Part.__init__)


def test_xdoc::part_constructor_args():
    sig = inspect.signature(xdoc::Part.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::section2_is_not_abstract():
    assert not inspect.isabstract(xdoc::Section2)


def test_xdoc::section2_constructor_exists():
    assert callable(xdoc::Section2.__init__)


def test_xdoc::section2_constructor_args():
    sig = inspect.signature(xdoc::Section2.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::section_is_not_abstract():
    assert not inspect.isabstract(xdoc::Section)


def test_xdoc::section_constructor_exists():
    assert callable(xdoc::Section.__init__)


def test_xdoc::section_constructor_args():
    sig = inspect.signature(xdoc::Section.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::chapter_is_not_abstract():
    assert not inspect.isabstract(xdoc::Chapter)


def test_xdoc::chapter_constructor_exists():
    assert callable(xdoc::Chapter.__init__)


def test_xdoc::chapter_constructor_args():
    sig = inspect.signature(xdoc::Chapter.__init__)
    params = list(sig.parameters.keys())



def test_xdoc::document_is_not_abstract():
    assert not inspect.isabstract(xdoc::Document)


def test_xdoc::document_constructor_exists():
    assert callable(xdoc::Document.__init__)


def test_xdoc::document_constructor_args():
    sig = inspect.signature(xdoc::Document.__init__)
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
xdoc::GlossaryEntry_strategy = st.builds(
    xdoc::GlossaryEntry,
    name=
        safe_text,
    alias=
        safe_text
)
xdoc::MarkupInCode_strategy = st.builds(
    xdoc::MarkupInCode,
)
xdoc::Code_strategy = st.builds(
    xdoc::Code,
    contents=
        safe_text
)
Part_strategy = st.builds(
    Part,
)
xdoc::PartRef_strategy = st.builds(
    xdoc::PartRef,
)
xdoc::JvmDeclaredType_strategy = st.builds(
    xdoc::JvmDeclaredType,
)
xdoc::ImageProxy_strategy = st.builds(
    xdoc::ImageProxy,
)
MarkupInCode_strategy = st.builds(
    MarkupInCode,
)
xdoc::Item_strategy = st.builds(
    xdoc::Item,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
xdoc::TableData_strategy = st.builds(
    xdoc::TableData,
)
xdoc::TableRow_strategy = st.builds(
    xdoc::TableRow,
)
MarkUp_strategy = st.builds(
    MarkUp,
)
xdoc::OrderedList_strategy = st.builds(
    xdoc::OrderedList,
)
xdoc::CodeRef_strategy = st.builds(
    xdoc::CodeRef,
)
xdoc::ImageRef_strategy = st.builds(
    xdoc::ImageRef,
    path=
        safe_text,
    name=
        safe_text,
    caption=
        safe_text,
    clazz=
        safe_text,
    style=
        safe_text
)
xdoc::Ref_strategy = st.builds(
    xdoc::Ref,
)
xdoc::Anchor_strategy = st.builds(
    xdoc::Anchor,
)
xdoc::Todo_strategy = st.builds(
    xdoc::Todo,
    text=
        safe_text
)
xdoc::UnorderedList_strategy = st.builds(
    xdoc::UnorderedList,
)
xdoc::Link_strategy = st.builds(
    xdoc::Link,
    url=
        safe_text,
    text=
        safe_text
)
xdoc::Emphasize_strategy = st.builds(
    xdoc::Emphasize,
)
xdoc::CodeBlock_strategy = st.builds(
    xdoc::CodeBlock,
)
xdoc::Table_strategy = st.builds(
    xdoc::Table,
)
xdoc::MarkUp_strategy = st.builds(
    xdoc::MarkUp,
)
xdoc::TextPart_strategy = st.builds(
    xdoc::TextPart,
    text=
        safe_text
)
xdoc::EObject_strategy = st.builds(
    xdoc::EObject,
)
xdoc::Identifiable_strategy = st.builds(
    xdoc::Identifiable,
    name=
        safe_text
)
Chapter_strategy = st.builds(
    Chapter,
)
xdoc::ChapterRef_strategy = st.builds(
    xdoc::ChapterRef,
)
Section2_strategy = st.builds(
    Section2,
)
xdoc::Section2Ref_strategy = st.builds(
    xdoc::Section2Ref,
)
Section_strategy = st.builds(
    Section,
)
xdoc::SectionRef_strategy = st.builds(
    xdoc::SectionRef,
)
xdoc::AbstractSection_strategy = st.builds(
    xdoc::AbstractSection,
)
xdoc::XdocFile_strategy = st.builds(
    xdoc::XdocFile,
)
xdoc::Glossary_strategy = st.builds(
    xdoc::Glossary,
)
xdoc::LangDef_strategy = st.builds(
    xdoc::LangDef,
    keywords=
        safe_text,
    name=
        safe_text
)
xdoc::TextOrMarkup_strategy = st.builds(
    xdoc::TextOrMarkup,
)
AbstractSection_strategy = st.builds(
    AbstractSection,
)
xdoc::Section3_strategy = st.builds(
    xdoc::Section3,
)
xdoc::Section4_strategy = st.builds(
    xdoc::Section4,
)
xdoc::Part_strategy = st.builds(
    xdoc::Part,
)
xdoc::Section2_strategy = st.builds(
    xdoc::Section2,
)
xdoc::Section_strategy = st.builds(
    xdoc::Section,
)
xdoc::Chapter_strategy = st.builds(
    xdoc::Chapter,
)
xdoc::Document_strategy = st.builds(
    xdoc::Document,
)

@given(instance=xdoc::GlossaryEntry_strategy)
@settings(max_examples=50)
def test_xdoc::glossaryentry_instantiation(instance):
    assert isinstance(instance, xdoc::GlossaryEntry)

@given(instance=xdoc::GlossaryEntry_strategy)
def test_xdoc::glossaryentry_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xdoc::GlossaryEntry_strategy)
def test_xdoc::glossaryentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xdoc::GlossaryEntry_strategy)
def test_xdoc::glossaryentry_alias_type(instance):
    assert isinstance(instance.alias, str)


@given(instance=xdoc::GlossaryEntry_strategy)
def test_xdoc::glossaryentry_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original

@given(instance=xdoc::MarkupInCode_strategy)
@settings(max_examples=50)
def test_xdoc::markupincode_instantiation(instance):
    assert isinstance(instance, xdoc::MarkupInCode)

@given(instance=xdoc::Code_strategy)
@settings(max_examples=50)
def test_xdoc::code_instantiation(instance):
    assert isinstance(instance, xdoc::Code)

@given(instance=xdoc::Code_strategy)
def test_xdoc::code_contents_type(instance):
    assert isinstance(instance.contents, str)


@given(instance=xdoc::Code_strategy)
def test_xdoc::code_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original

@given(instance=Part_strategy)
@settings(max_examples=50)
def test_part_instantiation(instance):
    assert isinstance(instance, Part)

@given(instance=xdoc::PartRef_strategy)
@settings(max_examples=50)
def test_xdoc::partref_instantiation(instance):
    assert isinstance(instance, xdoc::PartRef)

@given(instance=xdoc::JvmDeclaredType_strategy)
@settings(max_examples=50)
def test_xdoc::jvmdeclaredtype_instantiation(instance):
    assert isinstance(instance, xdoc::JvmDeclaredType)

@given(instance=xdoc::ImageProxy_strategy)
@settings(max_examples=50)
def test_xdoc::imageproxy_instantiation(instance):
    assert isinstance(instance, xdoc::ImageProxy)

@given(instance=MarkupInCode_strategy)
@settings(max_examples=50)
def test_markupincode_instantiation(instance):
    assert isinstance(instance, MarkupInCode)

@given(instance=xdoc::Item_strategy)
@settings(max_examples=50)
def test_xdoc::item_instantiation(instance):
    assert isinstance(instance, xdoc::Item)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=xdoc::TableData_strategy)
@settings(max_examples=50)
def test_xdoc::tabledata_instantiation(instance):
    assert isinstance(instance, xdoc::TableData)

@given(instance=xdoc::TableRow_strategy)
@settings(max_examples=50)
def test_xdoc::tablerow_instantiation(instance):
    assert isinstance(instance, xdoc::TableRow)

@given(instance=MarkUp_strategy)
@settings(max_examples=50)
def test_markup_instantiation(instance):
    assert isinstance(instance, MarkUp)

@given(instance=xdoc::OrderedList_strategy)
@settings(max_examples=50)
def test_xdoc::orderedlist_instantiation(instance):
    assert isinstance(instance, xdoc::OrderedList)

@given(instance=xdoc::CodeRef_strategy)
@settings(max_examples=50)
def test_xdoc::coderef_instantiation(instance):
    assert isinstance(instance, xdoc::CodeRef)

@given(instance=xdoc::ImageRef_strategy)
@settings(max_examples=50)
def test_xdoc::imageref_instantiation(instance):
    assert isinstance(instance, xdoc::ImageRef)

@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_path_type(instance):
    assert isinstance(instance.path, str)


@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original

@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_caption_type(instance):
    assert isinstance(instance.caption, str)


@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_caption_setter(instance):
    original = instance.caption
    instance.caption = original
    assert instance.caption == original

@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_clazz_type(instance):
    assert isinstance(instance.clazz, str)


@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original

@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_style_type(instance):
    assert isinstance(instance.style, str)


@given(instance=xdoc::ImageRef_strategy)
def test_xdoc::imageref_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original

@given(instance=xdoc::Ref_strategy)
@settings(max_examples=50)
def test_xdoc::ref_instantiation(instance):
    assert isinstance(instance, xdoc::Ref)

@given(instance=xdoc::Anchor_strategy)
@settings(max_examples=50)
def test_xdoc::anchor_instantiation(instance):
    assert isinstance(instance, xdoc::Anchor)

@given(instance=xdoc::Todo_strategy)
@settings(max_examples=50)
def test_xdoc::todo_instantiation(instance):
    assert isinstance(instance, xdoc::Todo)

@given(instance=xdoc::Todo_strategy)
def test_xdoc::todo_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=xdoc::Todo_strategy)
def test_xdoc::todo_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=xdoc::UnorderedList_strategy)
@settings(max_examples=50)
def test_xdoc::unorderedlist_instantiation(instance):
    assert isinstance(instance, xdoc::UnorderedList)

@given(instance=xdoc::Link_strategy)
@settings(max_examples=50)
def test_xdoc::link_instantiation(instance):
    assert isinstance(instance, xdoc::Link)

@given(instance=xdoc::Link_strategy)
def test_xdoc::link_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=xdoc::Link_strategy)
def test_xdoc::link_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=xdoc::Link_strategy)
def test_xdoc::link_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=xdoc::Link_strategy)
def test_xdoc::link_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=xdoc::Emphasize_strategy)
@settings(max_examples=50)
def test_xdoc::emphasize_instantiation(instance):
    assert isinstance(instance, xdoc::Emphasize)

@given(instance=xdoc::CodeBlock_strategy)
@settings(max_examples=50)
def test_xdoc::codeblock_instantiation(instance):
    assert isinstance(instance, xdoc::CodeBlock)

@given(instance=xdoc::Table_strategy)
@settings(max_examples=50)
def test_xdoc::table_instantiation(instance):
    assert isinstance(instance, xdoc::Table)

@given(instance=xdoc::MarkUp_strategy)
@settings(max_examples=50)
def test_xdoc::markup_instantiation(instance):
    assert isinstance(instance, xdoc::MarkUp)

@given(instance=xdoc::TextPart_strategy)
@settings(max_examples=50)
def test_xdoc::textpart_instantiation(instance):
    assert isinstance(instance, xdoc::TextPart)

@given(instance=xdoc::TextPart_strategy)
def test_xdoc::textpart_text_type(instance):
    assert isinstance(instance.text, str)


@given(instance=xdoc::TextPart_strategy)
def test_xdoc::textpart_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=xdoc::EObject_strategy)
@settings(max_examples=50)
def test_xdoc::eobject_instantiation(instance):
    assert isinstance(instance, xdoc::EObject)

@given(instance=xdoc::Identifiable_strategy)
@settings(max_examples=50)
def test_xdoc::identifiable_instantiation(instance):
    assert isinstance(instance, xdoc::Identifiable)

@given(instance=xdoc::Identifiable_strategy)
def test_xdoc::identifiable_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xdoc::Identifiable_strategy)
def test_xdoc::identifiable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Chapter_strategy)
@settings(max_examples=50)
def test_chapter_instantiation(instance):
    assert isinstance(instance, Chapter)

@given(instance=xdoc::ChapterRef_strategy)
@settings(max_examples=50)
def test_xdoc::chapterref_instantiation(instance):
    assert isinstance(instance, xdoc::ChapterRef)

@given(instance=Section2_strategy)
@settings(max_examples=50)
def test_section2_instantiation(instance):
    assert isinstance(instance, Section2)

@given(instance=xdoc::Section2Ref_strategy)
@settings(max_examples=50)
def test_xdoc::section2ref_instantiation(instance):
    assert isinstance(instance, xdoc::Section2Ref)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=xdoc::SectionRef_strategy)
@settings(max_examples=50)
def test_xdoc::sectionref_instantiation(instance):
    assert isinstance(instance, xdoc::SectionRef)

@given(instance=xdoc::AbstractSection_strategy)
@settings(max_examples=50)
def test_xdoc::abstractsection_instantiation(instance):
    assert isinstance(instance, xdoc::AbstractSection)

@given(instance=xdoc::XdocFile_strategy)
@settings(max_examples=50)
def test_xdoc::xdocfile_instantiation(instance):
    assert isinstance(instance, xdoc::XdocFile)

@given(instance=xdoc::Glossary_strategy)
@settings(max_examples=50)
def test_xdoc::glossary_instantiation(instance):
    assert isinstance(instance, xdoc::Glossary)

@given(instance=xdoc::LangDef_strategy)
@settings(max_examples=50)
def test_xdoc::langdef_instantiation(instance):
    assert isinstance(instance, xdoc::LangDef)

@given(instance=xdoc::LangDef_strategy)
def test_xdoc::langdef_keywords_type(instance):
    assert isinstance(instance.keywords, str)


@given(instance=xdoc::LangDef_strategy)
def test_xdoc::langdef_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=xdoc::LangDef_strategy)
def test_xdoc::langdef_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=xdoc::LangDef_strategy)
def test_xdoc::langdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xdoc::TextOrMarkup_strategy)
@settings(max_examples=50)
def test_xdoc::textormarkup_instantiation(instance):
    assert isinstance(instance, xdoc::TextOrMarkup)

@given(instance=AbstractSection_strategy)
@settings(max_examples=50)
def test_abstractsection_instantiation(instance):
    assert isinstance(instance, AbstractSection)

@given(instance=xdoc::Section3_strategy)
@settings(max_examples=50)
def test_xdoc::section3_instantiation(instance):
    assert isinstance(instance, xdoc::Section3)

@given(instance=xdoc::Section4_strategy)
@settings(max_examples=50)
def test_xdoc::section4_instantiation(instance):
    assert isinstance(instance, xdoc::Section4)

@given(instance=xdoc::Part_strategy)
@settings(max_examples=50)
def test_xdoc::part_instantiation(instance):
    assert isinstance(instance, xdoc::Part)

@given(instance=xdoc::Section2_strategy)
@settings(max_examples=50)
def test_xdoc::section2_instantiation(instance):
    assert isinstance(instance, xdoc::Section2)

@given(instance=xdoc::Section_strategy)
@settings(max_examples=50)
def test_xdoc::section_instantiation(instance):
    assert isinstance(instance, xdoc::Section)

@given(instance=xdoc::Chapter_strategy)
@settings(max_examples=50)
def test_xdoc::chapter_instantiation(instance):
    assert isinstance(instance, xdoc::Chapter)

@given(instance=xdoc::Document_strategy)
@settings(max_examples=50)
def test_xdoc::document_instantiation(instance):
    assert isinstance(instance, xdoc::Document)
