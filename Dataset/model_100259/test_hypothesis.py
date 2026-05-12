import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    xdoc_Item,
    Identifiable,
    xdoc_TableData,
    xdoc_TableRow,
    MarkUp,
    xdoc_OrderedList,
    xdoc_Table,
    xdoc_MarkUp,
    xdoc_TextPart,
    xdoc_EObject,
    xdoc_Identifiable,
    Chapter,
    xdoc_ChapterRef,
    Section2,
    xdoc_Section2Ref,
    Section,
    xdoc_SectionRef,
    xdoc_AbstractSection,
    xdoc_XdocFile,
    xdoc_Glossary,
    xdoc_LangDef,
    xdoc_TextOrMarkup,
    AbstractSection,
    xdoc_Section4,
    xdoc_Section,
    xdoc_Part,
    xdoc_Section2,
    xdoc_Section3,
    xdoc_Chapter,
    xdoc_Document,
    xdoc_GlossaryEntry,
    xdoc_MarkupInCode,
    xdoc_Code,
    Part,
    xdoc_PartRef,
    xdoc_Link,
    xdoc_JvmDeclaredType,
    xdoc_CodeRef,
    xdoc_CodeBlock,
    xdoc_ImageProxy,
    xdoc_ImageRef,
    MarkupInCode,
    xdoc_Anchor,
    xdoc_Ref,
    xdoc_Todo,
    xdoc_Emphasize,
    xdoc_UnorderedList,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_xdoc_item_is_not_abstract():
    assert not inspect.isabstract(xdoc_Item)


def test_xdoc_item_constructor_exists():
    assert callable(xdoc_Item.__init__)


def test_xdoc_item_constructor_args():
    sig = inspect.signature(xdoc_Item.__init__)
    params = list(sig.parameters.keys())



def test_identifiable_is_not_abstract():
    assert not inspect.isabstract(Identifiable)


def test_identifiable_constructor_exists():
    assert callable(Identifiable.__init__)


def test_identifiable_constructor_args():
    sig = inspect.signature(Identifiable.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_tabledata_is_not_abstract():
    assert not inspect.isabstract(xdoc_TableData)


def test_xdoc_tabledata_constructor_exists():
    assert callable(xdoc_TableData.__init__)


def test_xdoc_tabledata_constructor_args():
    sig = inspect.signature(xdoc_TableData.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_tablerow_is_not_abstract():
    assert not inspect.isabstract(xdoc_TableRow)


def test_xdoc_tablerow_constructor_exists():
    assert callable(xdoc_TableRow.__init__)


def test_xdoc_tablerow_constructor_args():
    sig = inspect.signature(xdoc_TableRow.__init__)
    params = list(sig.parameters.keys())



def test_markup_is_not_abstract():
    assert not inspect.isabstract(MarkUp)


def test_markup_constructor_exists():
    assert callable(MarkUp.__init__)


def test_markup_constructor_args():
    sig = inspect.signature(MarkUp.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_orderedlist_is_not_abstract():
    assert not inspect.isabstract(xdoc_OrderedList)


def test_xdoc_orderedlist_constructor_exists():
    assert callable(xdoc_OrderedList.__init__)


def test_xdoc_orderedlist_constructor_args():
    sig = inspect.signature(xdoc_OrderedList.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_table_is_not_abstract():
    assert not inspect.isabstract(xdoc_Table)


def test_xdoc_table_constructor_exists():
    assert callable(xdoc_Table.__init__)


def test_xdoc_table_constructor_args():
    sig = inspect.signature(xdoc_Table.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_markup_is_not_abstract():
    assert not inspect.isabstract(xdoc_MarkUp)


def test_xdoc_markup_constructor_exists():
    assert callable(xdoc_MarkUp.__init__)


def test_xdoc_markup_constructor_args():
    sig = inspect.signature(xdoc_MarkUp.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_textpart_is_not_abstract():
    assert not inspect.isabstract(xdoc_TextPart)


def test_xdoc_textpart_constructor_exists():
    assert callable(xdoc_TextPart.__init__)


def test_xdoc_textpart_constructor_args():
    sig = inspect.signature(xdoc_TextPart.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_xdoc_textpart_has_text():
    assert hasattr(xdoc_TextPart, "text")
    descriptor = None
    for klass in xdoc_TextPart.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_xdoc_eobject_is_not_abstract():
    assert not inspect.isabstract(xdoc_EObject)


def test_xdoc_eobject_constructor_exists():
    assert callable(xdoc_EObject.__init__)


def test_xdoc_eobject_constructor_args():
    sig = inspect.signature(xdoc_EObject.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_identifiable_is_not_abstract():
    assert not inspect.isabstract(xdoc_Identifiable)


def test_xdoc_identifiable_constructor_exists():
    assert callable(xdoc_Identifiable.__init__)


def test_xdoc_identifiable_constructor_args():
    sig = inspect.signature(xdoc_Identifiable.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_xdoc_identifiable_has_name():
    assert hasattr(xdoc_Identifiable, "name")
    descriptor = None
    for klass in xdoc_Identifiable.__mro__:
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



def test_xdoc_chapterref_is_not_abstract():
    assert not inspect.isabstract(xdoc_ChapterRef)


def test_xdoc_chapterref_constructor_exists():
    assert callable(xdoc_ChapterRef.__init__)


def test_xdoc_chapterref_constructor_args():
    sig = inspect.signature(xdoc_ChapterRef.__init__)
    params = list(sig.parameters.keys())



def test_section2_is_not_abstract():
    assert not inspect.isabstract(Section2)


def test_section2_constructor_exists():
    assert callable(Section2.__init__)


def test_section2_constructor_args():
    sig = inspect.signature(Section2.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_section2ref_is_not_abstract():
    assert not inspect.isabstract(xdoc_Section2Ref)


def test_xdoc_section2ref_constructor_exists():
    assert callable(xdoc_Section2Ref.__init__)


def test_xdoc_section2ref_constructor_args():
    sig = inspect.signature(xdoc_Section2Ref.__init__)
    params = list(sig.parameters.keys())



def test_section_is_not_abstract():
    assert not inspect.isabstract(Section)


def test_section_constructor_exists():
    assert callable(Section.__init__)


def test_section_constructor_args():
    sig = inspect.signature(Section.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_sectionref_is_not_abstract():
    assert not inspect.isabstract(xdoc_SectionRef)


def test_xdoc_sectionref_constructor_exists():
    assert callable(xdoc_SectionRef.__init__)


def test_xdoc_sectionref_constructor_args():
    sig = inspect.signature(xdoc_SectionRef.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_abstractsection_is_not_abstract():
    assert not inspect.isabstract(xdoc_AbstractSection)


def test_xdoc_abstractsection_constructor_exists():
    assert callable(xdoc_AbstractSection.__init__)


def test_xdoc_abstractsection_constructor_args():
    sig = inspect.signature(xdoc_AbstractSection.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_xdocfile_is_not_abstract():
    assert not inspect.isabstract(xdoc_XdocFile)


def test_xdoc_xdocfile_constructor_exists():
    assert callable(xdoc_XdocFile.__init__)


def test_xdoc_xdocfile_constructor_args():
    sig = inspect.signature(xdoc_XdocFile.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_glossary_is_not_abstract():
    assert not inspect.isabstract(xdoc_Glossary)


def test_xdoc_glossary_constructor_exists():
    assert callable(xdoc_Glossary.__init__)


def test_xdoc_glossary_constructor_args():
    sig = inspect.signature(xdoc_Glossary.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_langdef_is_not_abstract():
    assert not inspect.isabstract(xdoc_LangDef)


def test_xdoc_langdef_constructor_exists():
    assert callable(xdoc_LangDef.__init__)


def test_xdoc_langdef_constructor_args():
    sig = inspect.signature(xdoc_LangDef.__init__)
    params = list(sig.parameters.keys())
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "name" in params, "Missing parameter 'name'"

def test_xdoc_langdef_has_keywords():
    assert hasattr(xdoc_LangDef, "keywords")
    descriptor = None
    for klass in xdoc_LangDef.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_xdoc_langdef_has_name():
    assert hasattr(xdoc_LangDef, "name")
    descriptor = None
    for klass in xdoc_LangDef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xdoc_textormarkup_is_not_abstract():
    assert not inspect.isabstract(xdoc_TextOrMarkup)


def test_xdoc_textormarkup_constructor_exists():
    assert callable(xdoc_TextOrMarkup.__init__)


def test_xdoc_textormarkup_constructor_args():
    sig = inspect.signature(xdoc_TextOrMarkup.__init__)
    params = list(sig.parameters.keys())



def test_abstractsection_is_not_abstract():
    assert not inspect.isabstract(AbstractSection)


def test_abstractsection_constructor_exists():
    assert callable(AbstractSection.__init__)


def test_abstractsection_constructor_args():
    sig = inspect.signature(AbstractSection.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_section4_is_not_abstract():
    assert not inspect.isabstract(xdoc_Section4)


def test_xdoc_section4_constructor_exists():
    assert callable(xdoc_Section4.__init__)


def test_xdoc_section4_constructor_args():
    sig = inspect.signature(xdoc_Section4.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_section_is_not_abstract():
    assert not inspect.isabstract(xdoc_Section)


def test_xdoc_section_constructor_exists():
    assert callable(xdoc_Section.__init__)


def test_xdoc_section_constructor_args():
    sig = inspect.signature(xdoc_Section.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_part_is_not_abstract():
    assert not inspect.isabstract(xdoc_Part)


def test_xdoc_part_constructor_exists():
    assert callable(xdoc_Part.__init__)


def test_xdoc_part_constructor_args():
    sig = inspect.signature(xdoc_Part.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_section2_is_not_abstract():
    assert not inspect.isabstract(xdoc_Section2)


def test_xdoc_section2_constructor_exists():
    assert callable(xdoc_Section2.__init__)


def test_xdoc_section2_constructor_args():
    sig = inspect.signature(xdoc_Section2.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_section3_is_not_abstract():
    assert not inspect.isabstract(xdoc_Section3)


def test_xdoc_section3_constructor_exists():
    assert callable(xdoc_Section3.__init__)


def test_xdoc_section3_constructor_args():
    sig = inspect.signature(xdoc_Section3.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_chapter_is_not_abstract():
    assert not inspect.isabstract(xdoc_Chapter)


def test_xdoc_chapter_constructor_exists():
    assert callable(xdoc_Chapter.__init__)


def test_xdoc_chapter_constructor_args():
    sig = inspect.signature(xdoc_Chapter.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_document_is_not_abstract():
    assert not inspect.isabstract(xdoc_Document)


def test_xdoc_document_constructor_exists():
    assert callable(xdoc_Document.__init__)


def test_xdoc_document_constructor_args():
    sig = inspect.signature(xdoc_Document.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_glossaryentry_is_not_abstract():
    assert not inspect.isabstract(xdoc_GlossaryEntry)


def test_xdoc_glossaryentry_constructor_exists():
    assert callable(xdoc_GlossaryEntry.__init__)


def test_xdoc_glossaryentry_constructor_args():
    sig = inspect.signature(xdoc_GlossaryEntry.__init__)
    params = list(sig.parameters.keys())
    assert "alias" in params, "Missing parameter 'alias'"
    assert "name" in params, "Missing parameter 'name'"

def test_xdoc_glossaryentry_has_alias():
    assert hasattr(xdoc_GlossaryEntry, "alias")
    descriptor = None
    for klass in xdoc_GlossaryEntry.__mro__:
        if "alias" in klass.__dict__:
            descriptor = klass.__dict__["alias"]
            break
    assert isinstance(descriptor, property)

def test_xdoc_glossaryentry_has_name():
    assert hasattr(xdoc_GlossaryEntry, "name")
    descriptor = None
    for klass in xdoc_GlossaryEntry.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_xdoc_markupincode_is_not_abstract():
    assert not inspect.isabstract(xdoc_MarkupInCode)


def test_xdoc_markupincode_constructor_exists():
    assert callable(xdoc_MarkupInCode.__init__)


def test_xdoc_markupincode_constructor_args():
    sig = inspect.signature(xdoc_MarkupInCode.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_code_is_not_abstract():
    assert not inspect.isabstract(xdoc_Code)


def test_xdoc_code_constructor_exists():
    assert callable(xdoc_Code.__init__)


def test_xdoc_code_constructor_args():
    sig = inspect.signature(xdoc_Code.__init__)
    params = list(sig.parameters.keys())
    assert "contents" in params, "Missing parameter 'contents'"

def test_xdoc_code_has_contents():
    assert hasattr(xdoc_Code, "contents")
    descriptor = None
    for klass in xdoc_Code.__mro__:
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



def test_xdoc_partref_is_not_abstract():
    assert not inspect.isabstract(xdoc_PartRef)


def test_xdoc_partref_constructor_exists():
    assert callable(xdoc_PartRef.__init__)


def test_xdoc_partref_constructor_args():
    sig = inspect.signature(xdoc_PartRef.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_link_is_not_abstract():
    assert not inspect.isabstract(xdoc_Link)


def test_xdoc_link_constructor_exists():
    assert callable(xdoc_Link.__init__)


def test_xdoc_link_constructor_args():
    sig = inspect.signature(xdoc_Link.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "text" in params, "Missing parameter 'text'"

def test_xdoc_link_has_url():
    assert hasattr(xdoc_Link, "url")
    descriptor = None
    for klass in xdoc_Link.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_xdoc_link_has_text():
    assert hasattr(xdoc_Link, "text")
    descriptor = None
    for klass in xdoc_Link.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_xdoc_jvmdeclaredtype_is_not_abstract():
    assert not inspect.isabstract(xdoc_JvmDeclaredType)


def test_xdoc_jvmdeclaredtype_constructor_exists():
    assert callable(xdoc_JvmDeclaredType.__init__)


def test_xdoc_jvmdeclaredtype_constructor_args():
    sig = inspect.signature(xdoc_JvmDeclaredType.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_coderef_is_not_abstract():
    assert not inspect.isabstract(xdoc_CodeRef)


def test_xdoc_coderef_constructor_exists():
    assert callable(xdoc_CodeRef.__init__)


def test_xdoc_coderef_constructor_args():
    sig = inspect.signature(xdoc_CodeRef.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_codeblock_is_not_abstract():
    assert not inspect.isabstract(xdoc_CodeBlock)


def test_xdoc_codeblock_constructor_exists():
    assert callable(xdoc_CodeBlock.__init__)


def test_xdoc_codeblock_constructor_args():
    sig = inspect.signature(xdoc_CodeBlock.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_imageproxy_is_not_abstract():
    assert not inspect.isabstract(xdoc_ImageProxy)


def test_xdoc_imageproxy_constructor_exists():
    assert callable(xdoc_ImageProxy.__init__)


def test_xdoc_imageproxy_constructor_args():
    sig = inspect.signature(xdoc_ImageProxy.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_imageref_is_not_abstract():
    assert not inspect.isabstract(xdoc_ImageRef)


def test_xdoc_imageref_constructor_exists():
    assert callable(xdoc_ImageRef.__init__)


def test_xdoc_imageref_constructor_args():
    sig = inspect.signature(xdoc_ImageRef.__init__)
    params = list(sig.parameters.keys())
    assert "style" in params, "Missing parameter 'style'"
    assert "clazz" in params, "Missing parameter 'clazz'"
    assert "name" in params, "Missing parameter 'name'"
    assert "path" in params, "Missing parameter 'path'"
    assert "caption" in params, "Missing parameter 'caption'"

def test_xdoc_imageref_has_style():
    assert hasattr(xdoc_ImageRef, "style")
    descriptor = None
    for klass in xdoc_ImageRef.__mro__:
        if "style" in klass.__dict__:
            descriptor = klass.__dict__["style"]
            break
    assert isinstance(descriptor, property)

def test_xdoc_imageref_has_clazz():
    assert hasattr(xdoc_ImageRef, "clazz")
    descriptor = None
    for klass in xdoc_ImageRef.__mro__:
        if "clazz" in klass.__dict__:
            descriptor = klass.__dict__["clazz"]
            break
    assert isinstance(descriptor, property)

def test_xdoc_imageref_has_name():
    assert hasattr(xdoc_ImageRef, "name")
    descriptor = None
    for klass in xdoc_ImageRef.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_xdoc_imageref_has_path():
    assert hasattr(xdoc_ImageRef, "path")
    descriptor = None
    for klass in xdoc_ImageRef.__mro__:
        if "path" in klass.__dict__:
            descriptor = klass.__dict__["path"]
            break
    assert isinstance(descriptor, property)

def test_xdoc_imageref_has_caption():
    assert hasattr(xdoc_ImageRef, "caption")
    descriptor = None
    for klass in xdoc_ImageRef.__mro__:
        if "caption" in klass.__dict__:
            descriptor = klass.__dict__["caption"]
            break
    assert isinstance(descriptor, property)



def test_markupincode_is_not_abstract():
    assert not inspect.isabstract(MarkupInCode)


def test_markupincode_constructor_exists():
    assert callable(MarkupInCode.__init__)


def test_markupincode_constructor_args():
    sig = inspect.signature(MarkupInCode.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_anchor_is_not_abstract():
    assert not inspect.isabstract(xdoc_Anchor)


def test_xdoc_anchor_constructor_exists():
    assert callable(xdoc_Anchor.__init__)


def test_xdoc_anchor_constructor_args():
    sig = inspect.signature(xdoc_Anchor.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_ref_is_not_abstract():
    assert not inspect.isabstract(xdoc_Ref)


def test_xdoc_ref_constructor_exists():
    assert callable(xdoc_Ref.__init__)


def test_xdoc_ref_constructor_args():
    sig = inspect.signature(xdoc_Ref.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_todo_is_not_abstract():
    assert not inspect.isabstract(xdoc_Todo)


def test_xdoc_todo_constructor_exists():
    assert callable(xdoc_Todo.__init__)


def test_xdoc_todo_constructor_args():
    sig = inspect.signature(xdoc_Todo.__init__)
    params = list(sig.parameters.keys())
    assert "text" in params, "Missing parameter 'text'"

def test_xdoc_todo_has_text():
    assert hasattr(xdoc_Todo, "text")
    descriptor = None
    for klass in xdoc_Todo.__mro__:
        if "text" in klass.__dict__:
            descriptor = klass.__dict__["text"]
            break
    assert isinstance(descriptor, property)



def test_xdoc_emphasize_is_not_abstract():
    assert not inspect.isabstract(xdoc_Emphasize)


def test_xdoc_emphasize_constructor_exists():
    assert callable(xdoc_Emphasize.__init__)


def test_xdoc_emphasize_constructor_args():
    sig = inspect.signature(xdoc_Emphasize.__init__)
    params = list(sig.parameters.keys())



def test_xdoc_unorderedlist_is_not_abstract():
    assert not inspect.isabstract(xdoc_UnorderedList)


def test_xdoc_unorderedlist_constructor_exists():
    assert callable(xdoc_UnorderedList.__init__)


def test_xdoc_unorderedlist_constructor_args():
    sig = inspect.signature(xdoc_UnorderedList.__init__)
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
xdoc_Item_strategy = st.builds(
    xdoc_Item,
)
Identifiable_strategy = st.builds(
    Identifiable,
)
xdoc_TableData_strategy = st.builds(
    xdoc_TableData,
)
xdoc_TableRow_strategy = st.builds(
    xdoc_TableRow,
)
MarkUp_strategy = st.builds(
    MarkUp,
)
xdoc_OrderedList_strategy = st.builds(
    xdoc_OrderedList,
)
xdoc_Table_strategy = st.builds(
    xdoc_Table,
)
xdoc_MarkUp_strategy = st.builds(
    xdoc_MarkUp,
)
xdoc_TextPart_strategy = st.builds(
    xdoc_TextPart,
    text=
        safe_text
)
xdoc_EObject_strategy = st.builds(
    xdoc_EObject,
)
xdoc_Identifiable_strategy = st.builds(
    xdoc_Identifiable,
    name=
        safe_text
)
Chapter_strategy = st.builds(
    Chapter,
)
xdoc_ChapterRef_strategy = st.builds(
    xdoc_ChapterRef,
)
Section2_strategy = st.builds(
    Section2,
)
xdoc_Section2Ref_strategy = st.builds(
    xdoc_Section2Ref,
)
Section_strategy = st.builds(
    Section,
)
xdoc_SectionRef_strategy = st.builds(
    xdoc_SectionRef,
)
xdoc_AbstractSection_strategy = st.builds(
    xdoc_AbstractSection,
)
xdoc_XdocFile_strategy = st.builds(
    xdoc_XdocFile,
)
xdoc_Glossary_strategy = st.builds(
    xdoc_Glossary,
)
xdoc_LangDef_strategy = st.builds(
    xdoc_LangDef,
    keywords=
        safe_text,
    name=
        safe_text
)
xdoc_TextOrMarkup_strategy = st.builds(
    xdoc_TextOrMarkup,
)
AbstractSection_strategy = st.builds(
    AbstractSection,
)
xdoc_Section4_strategy = st.builds(
    xdoc_Section4,
)
xdoc_Section_strategy = st.builds(
    xdoc_Section,
)
xdoc_Part_strategy = st.builds(
    xdoc_Part,
)
xdoc_Section2_strategy = st.builds(
    xdoc_Section2,
)
xdoc_Section3_strategy = st.builds(
    xdoc_Section3,
)
xdoc_Chapter_strategy = st.builds(
    xdoc_Chapter,
)
xdoc_Document_strategy = st.builds(
    xdoc_Document,
)
xdoc_GlossaryEntry_strategy = st.builds(
    xdoc_GlossaryEntry,
    alias=
        safe_text,
    name=
        safe_text
)
xdoc_MarkupInCode_strategy = st.builds(
    xdoc_MarkupInCode,
)
xdoc_Code_strategy = st.builds(
    xdoc_Code,
    contents=
        safe_text
)
Part_strategy = st.builds(
    Part,
)
xdoc_PartRef_strategy = st.builds(
    xdoc_PartRef,
)
xdoc_Link_strategy = st.builds(
    xdoc_Link,
    url=
        safe_text,
    text=
        safe_text
)
xdoc_JvmDeclaredType_strategy = st.builds(
    xdoc_JvmDeclaredType,
)
xdoc_CodeRef_strategy = st.builds(
    xdoc_CodeRef,
)
xdoc_CodeBlock_strategy = st.builds(
    xdoc_CodeBlock,
)
xdoc_ImageProxy_strategy = st.builds(
    xdoc_ImageProxy,
)
xdoc_ImageRef_strategy = st.builds(
    xdoc_ImageRef,
    style=
        safe_text,
    clazz=
        safe_text,
    name=
        safe_text,
    path=
        safe_text,
    caption=
        safe_text
)
MarkupInCode_strategy = st.builds(
    MarkupInCode,
)
xdoc_Anchor_strategy = st.builds(
    xdoc_Anchor,
)
xdoc_Ref_strategy = st.builds(
    xdoc_Ref,
)
xdoc_Todo_strategy = st.builds(
    xdoc_Todo,
    text=
        safe_text
)
xdoc_Emphasize_strategy = st.builds(
    xdoc_Emphasize,
)
xdoc_UnorderedList_strategy = st.builds(
    xdoc_UnorderedList,
)

@given(instance=xdoc_Item_strategy)
@settings(max_examples=50)
def test_xdoc_item_instantiation(instance):
    assert isinstance(instance, xdoc_Item)

@given(instance=Identifiable_strategy)
@settings(max_examples=50)
def test_identifiable_instantiation(instance):
    assert isinstance(instance, Identifiable)

@given(instance=xdoc_TableData_strategy)
@settings(max_examples=50)
def test_xdoc_tabledata_instantiation(instance):
    assert isinstance(instance, xdoc_TableData)

@given(instance=xdoc_TableRow_strategy)
@settings(max_examples=50)
def test_xdoc_tablerow_instantiation(instance):
    assert isinstance(instance, xdoc_TableRow)

@given(instance=MarkUp_strategy)
@settings(max_examples=50)
def test_markup_instantiation(instance):
    assert isinstance(instance, MarkUp)

@given(instance=xdoc_OrderedList_strategy)
@settings(max_examples=50)
def test_xdoc_orderedlist_instantiation(instance):
    assert isinstance(instance, xdoc_OrderedList)

@given(instance=xdoc_Table_strategy)
@settings(max_examples=50)
def test_xdoc_table_instantiation(instance):
    assert isinstance(instance, xdoc_Table)

@given(instance=xdoc_MarkUp_strategy)
@settings(max_examples=50)
def test_xdoc_markup_instantiation(instance):
    assert isinstance(instance, xdoc_MarkUp)

@given(instance=xdoc_TextPart_strategy)
@settings(max_examples=50)
def test_xdoc_textpart_instantiation(instance):
    assert isinstance(instance, xdoc_TextPart)



@given(instance=xdoc_TextPart_strategy)
def test_xdoc_textpart_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=xdoc_EObject_strategy)
@settings(max_examples=50)
def test_xdoc_eobject_instantiation(instance):
    assert isinstance(instance, xdoc_EObject)

@given(instance=xdoc_Identifiable_strategy)
@settings(max_examples=50)
def test_xdoc_identifiable_instantiation(instance):
    assert isinstance(instance, xdoc_Identifiable)



@given(instance=xdoc_Identifiable_strategy)
def test_xdoc_identifiable_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Chapter_strategy)
@settings(max_examples=50)
def test_chapter_instantiation(instance):
    assert isinstance(instance, Chapter)

@given(instance=xdoc_ChapterRef_strategy)
@settings(max_examples=50)
def test_xdoc_chapterref_instantiation(instance):
    assert isinstance(instance, xdoc_ChapterRef)

@given(instance=Section2_strategy)
@settings(max_examples=50)
def test_section2_instantiation(instance):
    assert isinstance(instance, Section2)

@given(instance=xdoc_Section2Ref_strategy)
@settings(max_examples=50)
def test_xdoc_section2ref_instantiation(instance):
    assert isinstance(instance, xdoc_Section2Ref)

@given(instance=Section_strategy)
@settings(max_examples=50)
def test_section_instantiation(instance):
    assert isinstance(instance, Section)

@given(instance=xdoc_SectionRef_strategy)
@settings(max_examples=50)
def test_xdoc_sectionref_instantiation(instance):
    assert isinstance(instance, xdoc_SectionRef)

@given(instance=xdoc_AbstractSection_strategy)
@settings(max_examples=50)
def test_xdoc_abstractsection_instantiation(instance):
    assert isinstance(instance, xdoc_AbstractSection)

@given(instance=xdoc_XdocFile_strategy)
@settings(max_examples=50)
def test_xdoc_xdocfile_instantiation(instance):
    assert isinstance(instance, xdoc_XdocFile)

@given(instance=xdoc_Glossary_strategy)
@settings(max_examples=50)
def test_xdoc_glossary_instantiation(instance):
    assert isinstance(instance, xdoc_Glossary)

@given(instance=xdoc_LangDef_strategy)
@settings(max_examples=50)
def test_xdoc_langdef_instantiation(instance):
    assert isinstance(instance, xdoc_LangDef)



@given(instance=xdoc_LangDef_strategy)
def test_xdoc_langdef_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=xdoc_LangDef_strategy)
def test_xdoc_langdef_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xdoc_TextOrMarkup_strategy)
@settings(max_examples=50)
def test_xdoc_textormarkup_instantiation(instance):
    assert isinstance(instance, xdoc_TextOrMarkup)

@given(instance=AbstractSection_strategy)
@settings(max_examples=50)
def test_abstractsection_instantiation(instance):
    assert isinstance(instance, AbstractSection)

@given(instance=xdoc_Section4_strategy)
@settings(max_examples=50)
def test_xdoc_section4_instantiation(instance):
    assert isinstance(instance, xdoc_Section4)

@given(instance=xdoc_Section_strategy)
@settings(max_examples=50)
def test_xdoc_section_instantiation(instance):
    assert isinstance(instance, xdoc_Section)

@given(instance=xdoc_Part_strategy)
@settings(max_examples=50)
def test_xdoc_part_instantiation(instance):
    assert isinstance(instance, xdoc_Part)

@given(instance=xdoc_Section2_strategy)
@settings(max_examples=50)
def test_xdoc_section2_instantiation(instance):
    assert isinstance(instance, xdoc_Section2)

@given(instance=xdoc_Section3_strategy)
@settings(max_examples=50)
def test_xdoc_section3_instantiation(instance):
    assert isinstance(instance, xdoc_Section3)

@given(instance=xdoc_Chapter_strategy)
@settings(max_examples=50)
def test_xdoc_chapter_instantiation(instance):
    assert isinstance(instance, xdoc_Chapter)

@given(instance=xdoc_Document_strategy)
@settings(max_examples=50)
def test_xdoc_document_instantiation(instance):
    assert isinstance(instance, xdoc_Document)

@given(instance=xdoc_GlossaryEntry_strategy)
@settings(max_examples=50)
def test_xdoc_glossaryentry_instantiation(instance):
    assert isinstance(instance, xdoc_GlossaryEntry)



@given(instance=xdoc_GlossaryEntry_strategy)
def test_xdoc_glossaryentry_alias_setter(instance):
    original = instance.alias
    instance.alias = original
    assert instance.alias == original



@given(instance=xdoc_GlossaryEntry_strategy)
def test_xdoc_glossaryentry_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=xdoc_MarkupInCode_strategy)
@settings(max_examples=50)
def test_xdoc_markupincode_instantiation(instance):
    assert isinstance(instance, xdoc_MarkupInCode)

@given(instance=xdoc_Code_strategy)
@settings(max_examples=50)
def test_xdoc_code_instantiation(instance):
    assert isinstance(instance, xdoc_Code)



@given(instance=xdoc_Code_strategy)
def test_xdoc_code_contents_setter(instance):
    original = instance.contents
    instance.contents = original
    assert instance.contents == original

@given(instance=Part_strategy)
@settings(max_examples=50)
def test_part_instantiation(instance):
    assert isinstance(instance, Part)

@given(instance=xdoc_PartRef_strategy)
@settings(max_examples=50)
def test_xdoc_partref_instantiation(instance):
    assert isinstance(instance, xdoc_PartRef)

@given(instance=xdoc_Link_strategy)
@settings(max_examples=50)
def test_xdoc_link_instantiation(instance):
    assert isinstance(instance, xdoc_Link)



@given(instance=xdoc_Link_strategy)
def test_xdoc_link_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=xdoc_Link_strategy)
def test_xdoc_link_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=xdoc_JvmDeclaredType_strategy)
@settings(max_examples=50)
def test_xdoc_jvmdeclaredtype_instantiation(instance):
    assert isinstance(instance, xdoc_JvmDeclaredType)

@given(instance=xdoc_CodeRef_strategy)
@settings(max_examples=50)
def test_xdoc_coderef_instantiation(instance):
    assert isinstance(instance, xdoc_CodeRef)

@given(instance=xdoc_CodeBlock_strategy)
@settings(max_examples=50)
def test_xdoc_codeblock_instantiation(instance):
    assert isinstance(instance, xdoc_CodeBlock)

@given(instance=xdoc_ImageProxy_strategy)
@settings(max_examples=50)
def test_xdoc_imageproxy_instantiation(instance):
    assert isinstance(instance, xdoc_ImageProxy)

@given(instance=xdoc_ImageRef_strategy)
@settings(max_examples=50)
def test_xdoc_imageref_instantiation(instance):
    assert isinstance(instance, xdoc_ImageRef)



@given(instance=xdoc_ImageRef_strategy)
def test_xdoc_imageref_style_setter(instance):
    original = instance.style
    instance.style = original
    assert instance.style == original



@given(instance=xdoc_ImageRef_strategy)
def test_xdoc_imageref_clazz_setter(instance):
    original = instance.clazz
    instance.clazz = original
    assert instance.clazz == original



@given(instance=xdoc_ImageRef_strategy)
def test_xdoc_imageref_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=xdoc_ImageRef_strategy)
def test_xdoc_imageref_path_setter(instance):
    original = instance.path
    instance.path = original
    assert instance.path == original



@given(instance=xdoc_ImageRef_strategy)
def test_xdoc_imageref_caption_setter(instance):
    original = instance.caption
    instance.caption = original
    assert instance.caption == original

@given(instance=MarkupInCode_strategy)
@settings(max_examples=50)
def test_markupincode_instantiation(instance):
    assert isinstance(instance, MarkupInCode)

@given(instance=xdoc_Anchor_strategy)
@settings(max_examples=50)
def test_xdoc_anchor_instantiation(instance):
    assert isinstance(instance, xdoc_Anchor)

@given(instance=xdoc_Ref_strategy)
@settings(max_examples=50)
def test_xdoc_ref_instantiation(instance):
    assert isinstance(instance, xdoc_Ref)

@given(instance=xdoc_Todo_strategy)
@settings(max_examples=50)
def test_xdoc_todo_instantiation(instance):
    assert isinstance(instance, xdoc_Todo)



@given(instance=xdoc_Todo_strategy)
def test_xdoc_todo_text_setter(instance):
    original = instance.text
    instance.text = original
    assert instance.text == original

@given(instance=xdoc_Emphasize_strategy)
@settings(max_examples=50)
def test_xdoc_emphasize_instantiation(instance):
    assert isinstance(instance, xdoc_Emphasize)

@given(instance=xdoc_UnorderedList_strategy)
@settings(max_examples=50)
def test_xdoc_unorderedlist_instantiation(instance):
    assert isinstance(instance, xdoc_UnorderedList)
