import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    WordprocessingMLBasicDef::TabElt,
    WordprocessingMLBasicDef::PictureType,
    TabElt,
    WordprocessingMLBasicDef::StylesElt,
    WordprocessingMLBasicDef::ListsElt,
    WordprocessingMLBasicDef::FontsListElt,
    WordprocessingMLBasicDef::FldCharElt,
    FldCharElt,
    WordprocessingMLBasicDef::SectPrElt,
    WordprocessingMLBasicDef::NoteElt,
    WordprocessingMLBasicDef::SymElt,
    SymElt,
    PictureType,
    RunContentElt,
    WordprocessingMLBasicDef::Symbol,
    WordprocessingMLBasicDef::Tab,
    WordprocessingMLBasicDef::Separator,
    WordprocessingMLBasicDef::Picture,
    WordprocessingMLBasicDef::ContinuationSeparator,
    WordprocessingMLBasicDef::FldChar,
    WordprocessingMLBasicDef::AnnotationRef,
    WordprocessingMLBasicDef::SoftHyphen,
    WordprocessingMLBasicDef::Cr,
    WordprocessingMLBasicDef::FootnoteRef,
    WordprocessingMLBasicDef::PgNum,
    WordprocessingMLBasicDef::NoBreakHyphen,
    WordprocessingMLBasicDef::EndnoteRef,
    WordprocessingMLBasicDef::BreakElt,
    WordprocessingMLBasicDef::RunContentElt,
    RunElt,
    WordprocessingMLBasicDef::RunPrElt,
    ParaPrElt,
    BlockLevelChunkElt,
    WordprocessingMLBasicDef::RunLevelElt,
    WordprocessingMLBasicDef::ParaElt,
    RunPrElt,
    WordprocessingMLBasicDef::ParaContentElt,
    ParaElt,
    WordprocessingMLBasicDef::ParaPrElt,
    ParaContentElt,
    WordprocessingMLBasicDef::SimpleFieldElt,
    WordprocessingMLBasicDef::HLinkElt,
    WordprocessingMLBasicDef::SubDocElt,
    WordprocessingMLBasicDef::RunElt,
    WordprocessingMLBasicDef::BodyElt,
    NoteElt,
    WordprocessingMLBasicDef::Footnote,
    WordprocessingMLBasicDef::Endnote,
    WordprocessingMLBasicDef::BlockLevelElt,
    SectPrElt,
    BlockLevelElt,
    WordprocessingMLBasicDef::BlockLevelChunkElt,
    WordprocessingMLBasicDef::CfChunk,
    FontsListElt,
    WordprocessingMLBasicDef::DocPrElt,
    StringProperty,
    BodyElt,
    DocPrElt,
    StylesElt,
    ListsElt,
    DocumentPropertiesCollection,
    WordprocessingMLBasicDef::WordDocument,
    SmartTagType,
    WordprocessingMLBasicDef::StringType,
    StringType,
    WordprocessingMLBasicDef::InstrText,
    WordprocessingMLBasicDef::Text,
    WordprocessingMLBasicDef::DelInstrText,
    WordprocessingMLBasicDef::DelText,
    WordprocessingMLBasicDef::StringProperty,
    SmartTagsCollection,
    WordprocessingMLBasicDef::SmartTagType,
    CustomDocumentPropertiesCollection,
    WordprocessingMLBasicDef::SmartTagsCollection,
    WordprocessingMLBasicDef::CustomDocumentPropertiesCollection,
    WordprocessingMLBasicDef::CustomDocumentProperty,
    CustomDocumentProperty,
    VersionType,
    DateTimeType,
    ValueType,
    WordprocessingMLBasicDef::FloatValue,
    WordprocessingMLBasicDef::BooleanValue,
    WordprocessingMLBasicDef::DateTimeTypeValue,
    WordprocessingMLBasicDef::StringValue,
    WordprocessingMLBasicDef::ValueType,
    WordDocument,
    WordprocessingMLBasicDef::DocumentPropertiesCollection,
    WordprocessingMLBasicDef::DateTimeType,
    WordprocessingMLBasicDef::VersionType,
    FldCharTypeProperty,
    BreakType,
    OnOffType,
    NoteValue,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wordprocessingmlbasicdef::tabelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::TabElt)


def test_wordprocessingmlbasicdef::tabelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::TabElt.__init__)


def test_wordprocessingmlbasicdef::tabelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::TabElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::picturetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::PictureType)


def test_wordprocessingmlbasicdef::picturetype_constructor_exists():
    assert callable(WordprocessingMLBasicDef::PictureType.__init__)


def test_wordprocessingmlbasicdef::picturetype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::PictureType.__init__)
    params = list(sig.parameters.keys())



def test_tabelt_is_not_abstract():
    assert not inspect.isabstract(TabElt)


def test_tabelt_constructor_exists():
    assert callable(TabElt.__init__)


def test_tabelt_constructor_args():
    sig = inspect.signature(TabElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::styleselt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::StylesElt)


def test_wordprocessingmlbasicdef::styleselt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::StylesElt.__init__)


def test_wordprocessingmlbasicdef::styleselt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::StylesElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::listselt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::ListsElt)


def test_wordprocessingmlbasicdef::listselt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::ListsElt.__init__)


def test_wordprocessingmlbasicdef::listselt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::ListsElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::fontslistelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::FontsListElt)


def test_wordprocessingmlbasicdef::fontslistelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::FontsListElt.__init__)


def test_wordprocessingmlbasicdef::fontslistelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::FontsListElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::fldcharelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::FldCharElt)


def test_wordprocessingmlbasicdef::fldcharelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::FldCharElt.__init__)


def test_wordprocessingmlbasicdef::fldcharelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::FldCharElt.__init__)
    params = list(sig.parameters.keys())
    assert "fldLock" in params, "Missing parameter 'fldLock'"
    assert "fldCharType" in params, "Missing parameter 'fldCharType'"

def test_wordprocessingmlbasicdef::fldcharelt_has_fldLock():
    assert hasattr(WordprocessingMLBasicDef::FldCharElt, "fldLock")
    descriptor = None
    for klass in WordprocessingMLBasicDef::FldCharElt.__mro__:
        if "fldLock" in klass.__dict__:
            descriptor = klass.__dict__["fldLock"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::fldcharelt_has_fldCharType():
    assert hasattr(WordprocessingMLBasicDef::FldCharElt, "fldCharType")
    descriptor = None
    for klass in WordprocessingMLBasicDef::FldCharElt.__mro__:
        if "fldCharType" in klass.__dict__:
            descriptor = klass.__dict__["fldCharType"]
            break
    assert isinstance(descriptor, property)



def test_fldcharelt_is_not_abstract():
    assert not inspect.isabstract(FldCharElt)


def test_fldcharelt_constructor_exists():
    assert callable(FldCharElt.__init__)


def test_fldcharelt_constructor_args():
    sig = inspect.signature(FldCharElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::sectprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::SectPrElt)


def test_wordprocessingmlbasicdef::sectprelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::SectPrElt.__init__)


def test_wordprocessingmlbasicdef::sectprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::SectPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::noteelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::NoteElt)


def test_wordprocessingmlbasicdef::noteelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::NoteElt.__init__)


def test_wordprocessingmlbasicdef::noteelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::NoteElt.__init__)
    params = list(sig.parameters.keys())
    assert "suppressRef" in params, "Missing parameter 'suppressRef'"
    assert "type" in params, "Missing parameter 'type'"

def test_wordprocessingmlbasicdef::noteelt_has_suppressRef():
    assert hasattr(WordprocessingMLBasicDef::NoteElt, "suppressRef")
    descriptor = None
    for klass in WordprocessingMLBasicDef::NoteElt.__mro__:
        if "suppressRef" in klass.__dict__:
            descriptor = klass.__dict__["suppressRef"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::noteelt_has_type():
    assert hasattr(WordprocessingMLBasicDef::NoteElt, "type")
    descriptor = None
    for klass in WordprocessingMLBasicDef::NoteElt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef::symelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::SymElt)


def test_wordprocessingmlbasicdef::symelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::SymElt.__init__)


def test_wordprocessingmlbasicdef::symelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::SymElt.__init__)
    params = list(sig.parameters.keys())



def test_symelt_is_not_abstract():
    assert not inspect.isabstract(SymElt)


def test_symelt_constructor_exists():
    assert callable(SymElt.__init__)


def test_symelt_constructor_args():
    sig = inspect.signature(SymElt.__init__)
    params = list(sig.parameters.keys())



def test_picturetype_is_not_abstract():
    assert not inspect.isabstract(PictureType)


def test_picturetype_constructor_exists():
    assert callable(PictureType.__init__)


def test_picturetype_constructor_args():
    sig = inspect.signature(PictureType.__init__)
    params = list(sig.parameters.keys())



def test_runcontentelt_is_not_abstract():
    assert not inspect.isabstract(RunContentElt)


def test_runcontentelt_constructor_exists():
    assert callable(RunContentElt.__init__)


def test_runcontentelt_constructor_args():
    sig = inspect.signature(RunContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::symbol_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::Symbol)


def test_wordprocessingmlbasicdef::symbol_constructor_exists():
    assert callable(WordprocessingMLBasicDef::Symbol.__init__)


def test_wordprocessingmlbasicdef::symbol_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::tab_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::Tab)


def test_wordprocessingmlbasicdef::tab_constructor_exists():
    assert callable(WordprocessingMLBasicDef::Tab.__init__)


def test_wordprocessingmlbasicdef::tab_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::Tab.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::separator_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::Separator)


def test_wordprocessingmlbasicdef::separator_constructor_exists():
    assert callable(WordprocessingMLBasicDef::Separator.__init__)


def test_wordprocessingmlbasicdef::separator_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::Separator.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::picture_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::Picture)


def test_wordprocessingmlbasicdef::picture_constructor_exists():
    assert callable(WordprocessingMLBasicDef::Picture.__init__)


def test_wordprocessingmlbasicdef::picture_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::Picture.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::continuationseparator_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::ContinuationSeparator)


def test_wordprocessingmlbasicdef::continuationseparator_constructor_exists():
    assert callable(WordprocessingMLBasicDef::ContinuationSeparator.__init__)


def test_wordprocessingmlbasicdef::continuationseparator_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::ContinuationSeparator.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::fldchar_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::FldChar)


def test_wordprocessingmlbasicdef::fldchar_constructor_exists():
    assert callable(WordprocessingMLBasicDef::FldChar.__init__)


def test_wordprocessingmlbasicdef::fldchar_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::FldChar.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::annotationref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::AnnotationRef)


def test_wordprocessingmlbasicdef::annotationref_constructor_exists():
    assert callable(WordprocessingMLBasicDef::AnnotationRef.__init__)


def test_wordprocessingmlbasicdef::annotationref_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::AnnotationRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::softhyphen_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::SoftHyphen)


def test_wordprocessingmlbasicdef::softhyphen_constructor_exists():
    assert callable(WordprocessingMLBasicDef::SoftHyphen.__init__)


def test_wordprocessingmlbasicdef::softhyphen_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::SoftHyphen.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::cr_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::Cr)


def test_wordprocessingmlbasicdef::cr_constructor_exists():
    assert callable(WordprocessingMLBasicDef::Cr.__init__)


def test_wordprocessingmlbasicdef::cr_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::Cr.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::footnoteref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::FootnoteRef)


def test_wordprocessingmlbasicdef::footnoteref_constructor_exists():
    assert callable(WordprocessingMLBasicDef::FootnoteRef.__init__)


def test_wordprocessingmlbasicdef::footnoteref_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::FootnoteRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::pgnum_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::PgNum)


def test_wordprocessingmlbasicdef::pgnum_constructor_exists():
    assert callable(WordprocessingMLBasicDef::PgNum.__init__)


def test_wordprocessingmlbasicdef::pgnum_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::PgNum.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::nobreakhyphen_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::NoBreakHyphen)


def test_wordprocessingmlbasicdef::nobreakhyphen_constructor_exists():
    assert callable(WordprocessingMLBasicDef::NoBreakHyphen.__init__)


def test_wordprocessingmlbasicdef::nobreakhyphen_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::NoBreakHyphen.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::endnoteref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::EndnoteRef)


def test_wordprocessingmlbasicdef::endnoteref_constructor_exists():
    assert callable(WordprocessingMLBasicDef::EndnoteRef.__init__)


def test_wordprocessingmlbasicdef::endnoteref_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::EndnoteRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::breakelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::BreakElt)


def test_wordprocessingmlbasicdef::breakelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::BreakElt.__init__)


def test_wordprocessingmlbasicdef::breakelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::BreakElt.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_wordprocessingmlbasicdef::breakelt_has_type():
    assert hasattr(WordprocessingMLBasicDef::BreakElt, "type")
    descriptor = None
    for klass in WordprocessingMLBasicDef::BreakElt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef::runcontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::RunContentElt)


def test_wordprocessingmlbasicdef::runcontentelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::RunContentElt.__init__)


def test_wordprocessingmlbasicdef::runcontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::RunContentElt.__init__)
    params = list(sig.parameters.keys())



def test_runelt_is_not_abstract():
    assert not inspect.isabstract(RunElt)


def test_runelt_constructor_exists():
    assert callable(RunElt.__init__)


def test_runelt_constructor_args():
    sig = inspect.signature(RunElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::runprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::RunPrElt)


def test_wordprocessingmlbasicdef::runprelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::RunPrElt.__init__)


def test_wordprocessingmlbasicdef::runprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::RunPrElt.__init__)
    params = list(sig.parameters.keys())



def test_paraprelt_is_not_abstract():
    assert not inspect.isabstract(ParaPrElt)


def test_paraprelt_constructor_exists():
    assert callable(ParaPrElt.__init__)


def test_paraprelt_constructor_args():
    sig = inspect.signature(ParaPrElt.__init__)
    params = list(sig.parameters.keys())



def test_blocklevelchunkelt_is_not_abstract():
    assert not inspect.isabstract(BlockLevelChunkElt)


def test_blocklevelchunkelt_constructor_exists():
    assert callable(BlockLevelChunkElt.__init__)


def test_blocklevelchunkelt_constructor_args():
    sig = inspect.signature(BlockLevelChunkElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::runlevelelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::RunLevelElt)


def test_wordprocessingmlbasicdef::runlevelelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::RunLevelElt.__init__)


def test_wordprocessingmlbasicdef::runlevelelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::RunLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::paraelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::ParaElt)


def test_wordprocessingmlbasicdef::paraelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::ParaElt.__init__)


def test_wordprocessingmlbasicdef::paraelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::ParaElt.__init__)
    params = list(sig.parameters.keys())



def test_runprelt_is_not_abstract():
    assert not inspect.isabstract(RunPrElt)


def test_runprelt_constructor_exists():
    assert callable(RunPrElt.__init__)


def test_runprelt_constructor_args():
    sig = inspect.signature(RunPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::paracontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::ParaContentElt)


def test_wordprocessingmlbasicdef::paracontentelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::ParaContentElt.__init__)


def test_wordprocessingmlbasicdef::paracontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::ParaContentElt.__init__)
    params = list(sig.parameters.keys())



def test_paraelt_is_not_abstract():
    assert not inspect.isabstract(ParaElt)


def test_paraelt_constructor_exists():
    assert callable(ParaElt.__init__)


def test_paraelt_constructor_args():
    sig = inspect.signature(ParaElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::paraprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::ParaPrElt)


def test_wordprocessingmlbasicdef::paraprelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::ParaPrElt.__init__)


def test_wordprocessingmlbasicdef::paraprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::ParaPrElt.__init__)
    params = list(sig.parameters.keys())



def test_paracontentelt_is_not_abstract():
    assert not inspect.isabstract(ParaContentElt)


def test_paracontentelt_constructor_exists():
    assert callable(ParaContentElt.__init__)


def test_paracontentelt_constructor_args():
    sig = inspect.signature(ParaContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::simplefieldelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::SimpleFieldElt)


def test_wordprocessingmlbasicdef::simplefieldelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::SimpleFieldElt.__init__)


def test_wordprocessingmlbasicdef::simplefieldelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::SimpleFieldElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::hlinkelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::HLinkElt)


def test_wordprocessingmlbasicdef::hlinkelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::HLinkElt.__init__)


def test_wordprocessingmlbasicdef::hlinkelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::HLinkElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::subdocelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::SubDocElt)


def test_wordprocessingmlbasicdef::subdocelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::SubDocElt.__init__)


def test_wordprocessingmlbasicdef::subdocelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::SubDocElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::runelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::RunElt)


def test_wordprocessingmlbasicdef::runelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::RunElt.__init__)


def test_wordprocessingmlbasicdef::runelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::RunElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::bodyelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::BodyElt)


def test_wordprocessingmlbasicdef::bodyelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::BodyElt.__init__)


def test_wordprocessingmlbasicdef::bodyelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::BodyElt.__init__)
    params = list(sig.parameters.keys())



def test_noteelt_is_not_abstract():
    assert not inspect.isabstract(NoteElt)


def test_noteelt_constructor_exists():
    assert callable(NoteElt.__init__)


def test_noteelt_constructor_args():
    sig = inspect.signature(NoteElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::footnote_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::Footnote)


def test_wordprocessingmlbasicdef::footnote_constructor_exists():
    assert callable(WordprocessingMLBasicDef::Footnote.__init__)


def test_wordprocessingmlbasicdef::footnote_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::Footnote.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::endnote_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::Endnote)


def test_wordprocessingmlbasicdef::endnote_constructor_exists():
    assert callable(WordprocessingMLBasicDef::Endnote.__init__)


def test_wordprocessingmlbasicdef::endnote_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::Endnote.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::blocklevelelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::BlockLevelElt)


def test_wordprocessingmlbasicdef::blocklevelelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::BlockLevelElt.__init__)


def test_wordprocessingmlbasicdef::blocklevelelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::BlockLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_sectprelt_is_not_abstract():
    assert not inspect.isabstract(SectPrElt)


def test_sectprelt_constructor_exists():
    assert callable(SectPrElt.__init__)


def test_sectprelt_constructor_args():
    sig = inspect.signature(SectPrElt.__init__)
    params = list(sig.parameters.keys())



def test_blocklevelelt_is_not_abstract():
    assert not inspect.isabstract(BlockLevelElt)


def test_blocklevelelt_constructor_exists():
    assert callable(BlockLevelElt.__init__)


def test_blocklevelelt_constructor_args():
    sig = inspect.signature(BlockLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::blocklevelchunkelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::BlockLevelChunkElt)


def test_wordprocessingmlbasicdef::blocklevelchunkelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::BlockLevelChunkElt.__init__)


def test_wordprocessingmlbasicdef::blocklevelchunkelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::BlockLevelChunkElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::cfchunk_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::CfChunk)


def test_wordprocessingmlbasicdef::cfchunk_constructor_exists():
    assert callable(WordprocessingMLBasicDef::CfChunk.__init__)


def test_wordprocessingmlbasicdef::cfchunk_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::CfChunk.__init__)
    params = list(sig.parameters.keys())



def test_fontslistelt_is_not_abstract():
    assert not inspect.isabstract(FontsListElt)


def test_fontslistelt_constructor_exists():
    assert callable(FontsListElt.__init__)


def test_fontslistelt_constructor_args():
    sig = inspect.signature(FontsListElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::docprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::DocPrElt)


def test_wordprocessingmlbasicdef::docprelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef::DocPrElt.__init__)


def test_wordprocessingmlbasicdef::docprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::DocPrElt.__init__)
    params = list(sig.parameters.keys())



def test_stringproperty_is_not_abstract():
    assert not inspect.isabstract(StringProperty)


def test_stringproperty_constructor_exists():
    assert callable(StringProperty.__init__)


def test_stringproperty_constructor_args():
    sig = inspect.signature(StringProperty.__init__)
    params = list(sig.parameters.keys())



def test_bodyelt_is_not_abstract():
    assert not inspect.isabstract(BodyElt)


def test_bodyelt_constructor_exists():
    assert callable(BodyElt.__init__)


def test_bodyelt_constructor_args():
    sig = inspect.signature(BodyElt.__init__)
    params = list(sig.parameters.keys())



def test_docprelt_is_not_abstract():
    assert not inspect.isabstract(DocPrElt)


def test_docprelt_constructor_exists():
    assert callable(DocPrElt.__init__)


def test_docprelt_constructor_args():
    sig = inspect.signature(DocPrElt.__init__)
    params = list(sig.parameters.keys())



def test_styleselt_is_not_abstract():
    assert not inspect.isabstract(StylesElt)


def test_styleselt_constructor_exists():
    assert callable(StylesElt.__init__)


def test_styleselt_constructor_args():
    sig = inspect.signature(StylesElt.__init__)
    params = list(sig.parameters.keys())



def test_listselt_is_not_abstract():
    assert not inspect.isabstract(ListsElt)


def test_listselt_constructor_exists():
    assert callable(ListsElt.__init__)


def test_listselt_constructor_args():
    sig = inspect.signature(ListsElt.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::worddocument_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::WordDocument)


def test_wordprocessingmlbasicdef::worddocument_constructor_exists():
    assert callable(WordprocessingMLBasicDef::WordDocument.__init__)


def test_wordprocessingmlbasicdef::worddocument_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::WordDocument.__init__)
    params = list(sig.parameters.keys())



def test_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SmartTagType)


def test_smarttagtype_constructor_exists():
    assert callable(SmartTagType.__init__)


def test_smarttagtype_constructor_args():
    sig = inspect.signature(SmartTagType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::stringtype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::StringType)


def test_wordprocessingmlbasicdef::stringtype_constructor_exists():
    assert callable(WordprocessingMLBasicDef::StringType.__init__)


def test_wordprocessingmlbasicdef::stringtype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::StringType.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_wordprocessingmlbasicdef::stringtype_has_val():
    assert hasattr(WordprocessingMLBasicDef::StringType, "val")
    descriptor = None
    for klass in WordprocessingMLBasicDef::StringType.__mro__:
        if "val" in klass.__dict__:
            descriptor = klass.__dict__["val"]
            break
    assert isinstance(descriptor, property)



def test_stringtype_is_not_abstract():
    assert not inspect.isabstract(StringType)


def test_stringtype_constructor_exists():
    assert callable(StringType.__init__)


def test_stringtype_constructor_args():
    sig = inspect.signature(StringType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::instrtext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::InstrText)


def test_wordprocessingmlbasicdef::instrtext_constructor_exists():
    assert callable(WordprocessingMLBasicDef::InstrText.__init__)


def test_wordprocessingmlbasicdef::instrtext_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::InstrText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::text_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::Text)


def test_wordprocessingmlbasicdef::text_constructor_exists():
    assert callable(WordprocessingMLBasicDef::Text.__init__)


def test_wordprocessingmlbasicdef::text_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::Text.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::delinstrtext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::DelInstrText)


def test_wordprocessingmlbasicdef::delinstrtext_constructor_exists():
    assert callable(WordprocessingMLBasicDef::DelInstrText.__init__)


def test_wordprocessingmlbasicdef::delinstrtext_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::DelInstrText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::deltext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::DelText)


def test_wordprocessingmlbasicdef::deltext_constructor_exists():
    assert callable(WordprocessingMLBasicDef::DelText.__init__)


def test_wordprocessingmlbasicdef::deltext_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::DelText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::stringproperty_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::StringProperty)


def test_wordprocessingmlbasicdef::stringproperty_constructor_exists():
    assert callable(WordprocessingMLBasicDef::StringProperty.__init__)


def test_wordprocessingmlbasicdef::stringproperty_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::StringProperty.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::smarttagtype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::SmartTagType)


def test_wordprocessingmlbasicdef::smarttagtype_constructor_exists():
    assert callable(WordprocessingMLBasicDef::SmartTagType.__init__)


def test_wordprocessingmlbasicdef::smarttagtype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "url" in params, "Missing parameter 'url'"
    assert "name" in params, "Missing parameter 'name'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"

def test_wordprocessingmlbasicdef::smarttagtype_has_url():
    assert hasattr(WordprocessingMLBasicDef::SmartTagType, "url")
    descriptor = None
    for klass in WordprocessingMLBasicDef::SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::smarttagtype_has_name():
    assert hasattr(WordprocessingMLBasicDef::SmartTagType, "name")
    descriptor = None
    for klass in WordprocessingMLBasicDef::SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::smarttagtype_has_namespaceuri():
    assert hasattr(WordprocessingMLBasicDef::SmartTagType, "namespaceuri")
    descriptor = None
    for klass in WordprocessingMLBasicDef::SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::SmartTagsCollection)


def test_wordprocessingmlbasicdef::smarttagscollection_constructor_exists():
    assert callable(WordprocessingMLBasicDef::SmartTagsCollection.__init__)


def test_wordprocessingmlbasicdef::smarttagscollection_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::CustomDocumentPropertiesCollection)


def test_wordprocessingmlbasicdef::customdocumentpropertiescollection_constructor_exists():
    assert callable(WordprocessingMLBasicDef::CustomDocumentPropertiesCollection.__init__)


def test_wordprocessingmlbasicdef::customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::CustomDocumentProperty)


def test_wordprocessingmlbasicdef::customdocumentproperty_constructor_exists():
    assert callable(WordprocessingMLBasicDef::CustomDocumentProperty.__init__)


def test_wordprocessingmlbasicdef::customdocumentproperty_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wordprocessingmlbasicdef::customdocumentproperty_has_name():
    assert hasattr(WordprocessingMLBasicDef::CustomDocumentProperty, "name")
    descriptor = None
    for klass in WordprocessingMLBasicDef::CustomDocumentProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentProperty)


def test_customdocumentproperty_constructor_exists():
    assert callable(CustomDocumentProperty.__init__)


def test_customdocumentproperty_constructor_args():
    sig = inspect.signature(CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())



def test_versiontype_is_not_abstract():
    assert not inspect.isabstract(VersionType)


def test_versiontype_constructor_exists():
    assert callable(VersionType.__init__)


def test_versiontype_constructor_args():
    sig = inspect.signature(VersionType.__init__)
    params = list(sig.parameters.keys())



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::floatvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::FloatValue)


def test_wordprocessingmlbasicdef::floatvalue_constructor_exists():
    assert callable(WordprocessingMLBasicDef::FloatValue.__init__)


def test_wordprocessingmlbasicdef::floatvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::FloatValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmlbasicdef::floatvalue_has_value():
    assert hasattr(WordprocessingMLBasicDef::FloatValue, "value")
    descriptor = None
    for klass in WordprocessingMLBasicDef::FloatValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::BooleanValue)


def test_wordprocessingmlbasicdef::booleanvalue_constructor_exists():
    assert callable(WordprocessingMLBasicDef::BooleanValue.__init__)


def test_wordprocessingmlbasicdef::booleanvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmlbasicdef::booleanvalue_has_value():
    assert hasattr(WordprocessingMLBasicDef::BooleanValue, "value")
    descriptor = None
    for klass in WordprocessingMLBasicDef::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef::datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::DateTimeTypeValue)


def test_wordprocessingmlbasicdef::datetimetypevalue_constructor_exists():
    assert callable(WordprocessingMLBasicDef::DateTimeTypeValue.__init__)


def test_wordprocessingmlbasicdef::datetimetypevalue_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::stringvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::StringValue)


def test_wordprocessingmlbasicdef::stringvalue_constructor_exists():
    assert callable(WordprocessingMLBasicDef::StringValue.__init__)


def test_wordprocessingmlbasicdef::stringvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmlbasicdef::stringvalue_has_value():
    assert hasattr(WordprocessingMLBasicDef::StringValue, "value")
    descriptor = None
    for klass in WordprocessingMLBasicDef::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef::valuetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::ValueType)


def test_wordprocessingmlbasicdef::valuetype_constructor_exists():
    assert callable(WordprocessingMLBasicDef::ValueType.__init__)


def test_wordprocessingmlbasicdef::valuetype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_worddocument_is_not_abstract():
    assert not inspect.isabstract(WordDocument)


def test_worddocument_constructor_exists():
    assert callable(WordDocument.__init__)


def test_worddocument_constructor_args():
    sig = inspect.signature(WordDocument.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::DocumentPropertiesCollection)


def test_wordprocessingmlbasicdef::documentpropertiescollection_constructor_exists():
    assert callable(WordprocessingMLBasicDef::DocumentPropertiesCollection.__init__)


def test_wordprocessingmlbasicdef::documentpropertiescollection_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "lines" in params, "Missing parameter 'lines'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "title" in params, "Missing parameter 'title'"
    assert "words" in params, "Missing parameter 'words'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "description" in params, "Missing parameter 'description'"
    assert "author" in params, "Missing parameter 'author'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "company" in params, "Missing parameter 'company'"
    assert "keywords" in params, "Missing parameter 'keywords'"

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_lines():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_bytes():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_guid():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_manager():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_presentationFormat():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_characters():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_paragraphs():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_subject():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_title():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_words():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_totalTime():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_appName():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_category():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_pages():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_description():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_author():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_revision():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_lastAuthor():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_company():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::documentpropertiescollection_has_keywords():
    assert hasattr(WordprocessingMLBasicDef::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef::datetimetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::DateTimeType)


def test_wordprocessingmlbasicdef::datetimetype_constructor_exists():
    assert callable(WordprocessingMLBasicDef::DateTimeType.__init__)


def test_wordprocessingmlbasicdef::datetimetype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "month" in params, "Missing parameter 'month'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "second" in params, "Missing parameter 'second'"
    assert "year" in params, "Missing parameter 'year'"

def test_wordprocessingmlbasicdef::datetimetype_has_day():
    assert hasattr(WordprocessingMLBasicDef::DateTimeType, "day")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::datetimetype_has_hour():
    assert hasattr(WordprocessingMLBasicDef::DateTimeType, "hour")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::datetimetype_has_month():
    assert hasattr(WordprocessingMLBasicDef::DateTimeType, "month")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::datetimetype_has_minute():
    assert hasattr(WordprocessingMLBasicDef::DateTimeType, "minute")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::datetimetype_has_second():
    assert hasattr(WordprocessingMLBasicDef::DateTimeType, "second")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::datetimetype_has_year():
    assert hasattr(WordprocessingMLBasicDef::DateTimeType, "year")
    descriptor = None
    for klass in WordprocessingMLBasicDef::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef::versiontype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef::VersionType)


def test_wordprocessingmlbasicdef::versiontype_constructor_exists():
    assert callable(WordprocessingMLBasicDef::VersionType.__init__)


def test_wordprocessingmlbasicdef::versiontype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef::VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "nn" in params, "Missing parameter 'nn'"
    assert "n" in params, "Missing parameter 'n'"

def test_wordprocessingmlbasicdef::versiontype_has_nn():
    assert hasattr(WordprocessingMLBasicDef::VersionType, "nn")
    descriptor = None
    for klass in WordprocessingMLBasicDef::VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef::versiontype_has_n():
    assert hasattr(WordprocessingMLBasicDef::VersionType, "n")
    descriptor = None
    for klass in WordprocessingMLBasicDef::VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)

def test_fldchartypeproperty_exists():
    # Check that the Enumeration exists
    assert FldCharTypeProperty is not None

def test_fldchartypeproperty_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FldCharTypeProperty]
    expected_literals = [
        "fctp_separate",
        "fctp_end",
        "fctp_begin",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FldCharTypeProperty"

def test_breaktype_exists():
    # Check that the Enumeration exists
    assert BreakType is not None

def test_breaktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BreakType]
    expected_literals = [
        "bt_column",
        "bt_page",
        "bt_text_wrapping",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BreakType"

def test_onofftype_exists():
    # Check that the Enumeration exists
    assert OnOffType is not None

def test_onofftype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OnOffType]
    expected_literals = [
        "oot_off",
        "oot_on",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in OnOffType"

def test_notevalue_exists():
    # Check that the Enumeration exists
    assert NoteValue is not None

def test_notevalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NoteValue]
    expected_literals = [
        "ftn_continuation_separator",
        "ftn_separator",
        "ftn_normal",
        "ftn_continuation_notice",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NoteValue"


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
WordprocessingMLBasicDef::TabElt_strategy = st.builds(
    WordprocessingMLBasicDef::TabElt,
)
WordprocessingMLBasicDef::PictureType_strategy = st.builds(
    WordprocessingMLBasicDef::PictureType,
)
TabElt_strategy = st.builds(
    TabElt,
)
WordprocessingMLBasicDef::StylesElt_strategy = st.builds(
    WordprocessingMLBasicDef::StylesElt,
)
WordprocessingMLBasicDef::ListsElt_strategy = st.builds(
    WordprocessingMLBasicDef::ListsElt,
)
WordprocessingMLBasicDef::FontsListElt_strategy = st.builds(
    WordprocessingMLBasicDef::FontsListElt,
)
WordprocessingMLBasicDef::FldCharElt_strategy = st.builds(
    WordprocessingMLBasicDef::FldCharElt,
    fldLock=
        st.none(),
    fldCharType=
        st.none()
)
FldCharElt_strategy = st.builds(
    FldCharElt,
)
WordprocessingMLBasicDef::SectPrElt_strategy = st.builds(
    WordprocessingMLBasicDef::SectPrElt,
)
WordprocessingMLBasicDef::NoteElt_strategy = st.builds(
    WordprocessingMLBasicDef::NoteElt,
    suppressRef=
        st.none(),
    type=
        st.none()
)
WordprocessingMLBasicDef::SymElt_strategy = st.builds(
    WordprocessingMLBasicDef::SymElt,
)
SymElt_strategy = st.builds(
    SymElt,
)
PictureType_strategy = st.builds(
    PictureType,
)
RunContentElt_strategy = st.builds(
    RunContentElt,
)
WordprocessingMLBasicDef::Symbol_strategy = st.builds(
    WordprocessingMLBasicDef::Symbol,
)
WordprocessingMLBasicDef::Tab_strategy = st.builds(
    WordprocessingMLBasicDef::Tab,
)
WordprocessingMLBasicDef::Separator_strategy = st.builds(
    WordprocessingMLBasicDef::Separator,
)
WordprocessingMLBasicDef::Picture_strategy = st.builds(
    WordprocessingMLBasicDef::Picture,
)
WordprocessingMLBasicDef::ContinuationSeparator_strategy = st.builds(
    WordprocessingMLBasicDef::ContinuationSeparator,
)
WordprocessingMLBasicDef::FldChar_strategy = st.builds(
    WordprocessingMLBasicDef::FldChar,
)
WordprocessingMLBasicDef::AnnotationRef_strategy = st.builds(
    WordprocessingMLBasicDef::AnnotationRef,
)
WordprocessingMLBasicDef::SoftHyphen_strategy = st.builds(
    WordprocessingMLBasicDef::SoftHyphen,
)
WordprocessingMLBasicDef::Cr_strategy = st.builds(
    WordprocessingMLBasicDef::Cr,
)
WordprocessingMLBasicDef::FootnoteRef_strategy = st.builds(
    WordprocessingMLBasicDef::FootnoteRef,
)
WordprocessingMLBasicDef::PgNum_strategy = st.builds(
    WordprocessingMLBasicDef::PgNum,
)
WordprocessingMLBasicDef::NoBreakHyphen_strategy = st.builds(
    WordprocessingMLBasicDef::NoBreakHyphen,
)
WordprocessingMLBasicDef::EndnoteRef_strategy = st.builds(
    WordprocessingMLBasicDef::EndnoteRef,
)
WordprocessingMLBasicDef::BreakElt_strategy = st.builds(
    WordprocessingMLBasicDef::BreakElt,
    type=
        st.none()
)
WordprocessingMLBasicDef::RunContentElt_strategy = st.builds(
    WordprocessingMLBasicDef::RunContentElt,
)
RunElt_strategy = st.builds(
    RunElt,
)
WordprocessingMLBasicDef::RunPrElt_strategy = st.builds(
    WordprocessingMLBasicDef::RunPrElt,
)
ParaPrElt_strategy = st.builds(
    ParaPrElt,
)
BlockLevelChunkElt_strategy = st.builds(
    BlockLevelChunkElt,
)
WordprocessingMLBasicDef::RunLevelElt_strategy = st.builds(
    WordprocessingMLBasicDef::RunLevelElt,
)
WordprocessingMLBasicDef::ParaElt_strategy = st.builds(
    WordprocessingMLBasicDef::ParaElt,
)
RunPrElt_strategy = st.builds(
    RunPrElt,
)
WordprocessingMLBasicDef::ParaContentElt_strategy = st.builds(
    WordprocessingMLBasicDef::ParaContentElt,
)
ParaElt_strategy = st.builds(
    ParaElt,
)
WordprocessingMLBasicDef::ParaPrElt_strategy = st.builds(
    WordprocessingMLBasicDef::ParaPrElt,
)
ParaContentElt_strategy = st.builds(
    ParaContentElt,
)
WordprocessingMLBasicDef::SimpleFieldElt_strategy = st.builds(
    WordprocessingMLBasicDef::SimpleFieldElt,
)
WordprocessingMLBasicDef::HLinkElt_strategy = st.builds(
    WordprocessingMLBasicDef::HLinkElt,
)
WordprocessingMLBasicDef::SubDocElt_strategy = st.builds(
    WordprocessingMLBasicDef::SubDocElt,
)
WordprocessingMLBasicDef::RunElt_strategy = st.builds(
    WordprocessingMLBasicDef::RunElt,
)
WordprocessingMLBasicDef::BodyElt_strategy = st.builds(
    WordprocessingMLBasicDef::BodyElt,
)
NoteElt_strategy = st.builds(
    NoteElt,
)
WordprocessingMLBasicDef::Footnote_strategy = st.builds(
    WordprocessingMLBasicDef::Footnote,
)
WordprocessingMLBasicDef::Endnote_strategy = st.builds(
    WordprocessingMLBasicDef::Endnote,
)
WordprocessingMLBasicDef::BlockLevelElt_strategy = st.builds(
    WordprocessingMLBasicDef::BlockLevelElt,
)
SectPrElt_strategy = st.builds(
    SectPrElt,
)
BlockLevelElt_strategy = st.builds(
    BlockLevelElt,
)
WordprocessingMLBasicDef::BlockLevelChunkElt_strategy = st.builds(
    WordprocessingMLBasicDef::BlockLevelChunkElt,
)
WordprocessingMLBasicDef::CfChunk_strategy = st.builds(
    WordprocessingMLBasicDef::CfChunk,
)
FontsListElt_strategy = st.builds(
    FontsListElt,
)
WordprocessingMLBasicDef::DocPrElt_strategy = st.builds(
    WordprocessingMLBasicDef::DocPrElt,
)
StringProperty_strategy = st.builds(
    StringProperty,
)
BodyElt_strategy = st.builds(
    BodyElt,
)
DocPrElt_strategy = st.builds(
    DocPrElt,
)
StylesElt_strategy = st.builds(
    StylesElt,
)
ListsElt_strategy = st.builds(
    ListsElt,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
WordprocessingMLBasicDef::WordDocument_strategy = st.builds(
    WordprocessingMLBasicDef::WordDocument,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
WordprocessingMLBasicDef::StringType_strategy = st.builds(
    WordprocessingMLBasicDef::StringType,
    val=
        st.none()
)
StringType_strategy = st.builds(
    StringType,
)
WordprocessingMLBasicDef::InstrText_strategy = st.builds(
    WordprocessingMLBasicDef::InstrText,
)
WordprocessingMLBasicDef::Text_strategy = st.builds(
    WordprocessingMLBasicDef::Text,
)
WordprocessingMLBasicDef::DelInstrText_strategy = st.builds(
    WordprocessingMLBasicDef::DelInstrText,
)
WordprocessingMLBasicDef::DelText_strategy = st.builds(
    WordprocessingMLBasicDef::DelText,
)
WordprocessingMLBasicDef::StringProperty_strategy = st.builds(
    WordprocessingMLBasicDef::StringProperty,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
WordprocessingMLBasicDef::SmartTagType_strategy = st.builds(
    WordprocessingMLBasicDef::SmartTagType,
    url=
        st.none(),
    name=
        st.none(),
    namespaceuri=
        st.none()
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
WordprocessingMLBasicDef::SmartTagsCollection_strategy = st.builds(
    WordprocessingMLBasicDef::SmartTagsCollection,
)
WordprocessingMLBasicDef::CustomDocumentPropertiesCollection_strategy = st.builds(
    WordprocessingMLBasicDef::CustomDocumentPropertiesCollection,
)
WordprocessingMLBasicDef::CustomDocumentProperty_strategy = st.builds(
    WordprocessingMLBasicDef::CustomDocumentProperty,
    name=
        st.none()
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
VersionType_strategy = st.builds(
    VersionType,
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
ValueType_strategy = st.builds(
    ValueType,
)
WordprocessingMLBasicDef::FloatValue_strategy = st.builds(
    WordprocessingMLBasicDef::FloatValue,
    value=
        st.none()
)
WordprocessingMLBasicDef::BooleanValue_strategy = st.builds(
    WordprocessingMLBasicDef::BooleanValue,
    value=
        st.none()
)
WordprocessingMLBasicDef::DateTimeTypeValue_strategy = st.builds(
    WordprocessingMLBasicDef::DateTimeTypeValue,
)
WordprocessingMLBasicDef::StringValue_strategy = st.builds(
    WordprocessingMLBasicDef::StringValue,
    value=
        st.none()
)
WordprocessingMLBasicDef::ValueType_strategy = st.builds(
    WordprocessingMLBasicDef::ValueType,
)
WordDocument_strategy = st.builds(
    WordDocument,
)
WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy = st.builds(
    WordprocessingMLBasicDef::DocumentPropertiesCollection,
    lines=
        st.none(),
    bytes=
        st.none(),
    guid=
        st.none(),
    manager=
        st.none(),
    presentationFormat=
        st.none(),
    characters=
        st.none(),
    paragraphs=
        st.none(),
    subject=
        st.none(),
    charactersWithSpaces=
        st.none(),
    title=
        st.none(),
    words=
        st.none(),
    hyperlinkBase=
        st.none(),
    totalTime=
        st.none(),
    appName=
        st.none(),
    category=
        st.none(),
    pages=
        st.none(),
    description=
        st.none(),
    author=
        st.none(),
    revision=
        st.none(),
    lastAuthor=
        st.none(),
    company=
        st.none(),
    keywords=
        st.none()
)
WordprocessingMLBasicDef::DateTimeType_strategy = st.builds(
    WordprocessingMLBasicDef::DateTimeType,
    day=
        st.none(),
    hour=
        st.none(),
    month=
        st.none(),
    minute=
        st.none(),
    second=
        st.none(),
    year=
        st.none()
)
WordprocessingMLBasicDef::VersionType_strategy = st.builds(
    WordprocessingMLBasicDef::VersionType,
    nn=
        st.none(),
    n=
        st.none()
)

@given(instance=WordprocessingMLBasicDef::TabElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::tabelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::TabElt)

@given(instance=WordprocessingMLBasicDef::PictureType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::picturetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::PictureType)

@given(instance=TabElt_strategy)
@settings(max_examples=50)
def test_tabelt_instantiation(instance):
    assert isinstance(instance, TabElt)

@given(instance=WordprocessingMLBasicDef::StylesElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::styleselt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::StylesElt)

@given(instance=WordprocessingMLBasicDef::ListsElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::listselt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::ListsElt)

@given(instance=WordprocessingMLBasicDef::FontsListElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::fontslistelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::FontsListElt)

@given(instance=WordprocessingMLBasicDef::FldCharElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::fldcharelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::FldCharElt)

@given(instance=WordprocessingMLBasicDef::FldCharElt_strategy)
def test_wordprocessingmlbasicdef::fldcharelt_fldLock_type(instance):
    assert isinstance(instance.fldLock, stringtype)


@given(instance=WordprocessingMLBasicDef::FldCharElt_strategy)
def test_wordprocessingmlbasicdef::fldcharelt_fldLock_setter(instance):
    original = instance.fldLock
    instance.fldLock = original
    assert instance.fldLock == original

@given(instance=WordprocessingMLBasicDef::FldCharElt_strategy)
def test_wordprocessingmlbasicdef::fldcharelt_fldCharType_type(instance):
    assert isinstance(instance.fldCharType, stringtype)


@given(instance=WordprocessingMLBasicDef::FldCharElt_strategy)
def test_wordprocessingmlbasicdef::fldcharelt_fldCharType_setter(instance):
    original = instance.fldCharType
    instance.fldCharType = original
    assert instance.fldCharType == original

@given(instance=FldCharElt_strategy)
@settings(max_examples=50)
def test_fldcharelt_instantiation(instance):
    assert isinstance(instance, FldCharElt)

@given(instance=WordprocessingMLBasicDef::SectPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::sectprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::SectPrElt)

@given(instance=WordprocessingMLBasicDef::NoteElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::noteelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::NoteElt)

@given(instance=WordprocessingMLBasicDef::NoteElt_strategy)
def test_wordprocessingmlbasicdef::noteelt_suppressRef_type(instance):
    assert isinstance(instance.suppressRef, stringtype)


@given(instance=WordprocessingMLBasicDef::NoteElt_strategy)
def test_wordprocessingmlbasicdef::noteelt_suppressRef_setter(instance):
    original = instance.suppressRef
    instance.suppressRef = original
    assert instance.suppressRef == original

@given(instance=WordprocessingMLBasicDef::NoteElt_strategy)
def test_wordprocessingmlbasicdef::noteelt_type_type(instance):
    assert isinstance(instance.type, stringtype)


@given(instance=WordprocessingMLBasicDef::NoteElt_strategy)
def test_wordprocessingmlbasicdef::noteelt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=WordprocessingMLBasicDef::SymElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::symelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::SymElt)

@given(instance=SymElt_strategy)
@settings(max_examples=50)
def test_symelt_instantiation(instance):
    assert isinstance(instance, SymElt)

@given(instance=PictureType_strategy)
@settings(max_examples=50)
def test_picturetype_instantiation(instance):
    assert isinstance(instance, PictureType)

@given(instance=RunContentElt_strategy)
@settings(max_examples=50)
def test_runcontentelt_instantiation(instance):
    assert isinstance(instance, RunContentElt)

@given(instance=WordprocessingMLBasicDef::Symbol_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::symbol_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::Symbol)

@given(instance=WordprocessingMLBasicDef::Tab_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::tab_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::Tab)

@given(instance=WordprocessingMLBasicDef::Separator_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::separator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::Separator)

@given(instance=WordprocessingMLBasicDef::Picture_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::picture_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::Picture)

@given(instance=WordprocessingMLBasicDef::ContinuationSeparator_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::continuationseparator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::ContinuationSeparator)

@given(instance=WordprocessingMLBasicDef::FldChar_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::fldchar_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::FldChar)

@given(instance=WordprocessingMLBasicDef::AnnotationRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::annotationref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::AnnotationRef)

@given(instance=WordprocessingMLBasicDef::SoftHyphen_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::softhyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::SoftHyphen)

@given(instance=WordprocessingMLBasicDef::Cr_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::cr_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::Cr)

@given(instance=WordprocessingMLBasicDef::FootnoteRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::footnoteref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::FootnoteRef)

@given(instance=WordprocessingMLBasicDef::PgNum_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::pgnum_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::PgNum)

@given(instance=WordprocessingMLBasicDef::NoBreakHyphen_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::nobreakhyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::NoBreakHyphen)

@given(instance=WordprocessingMLBasicDef::EndnoteRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::endnoteref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::EndnoteRef)

@given(instance=WordprocessingMLBasicDef::BreakElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::breakelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::BreakElt)

@given(instance=WordprocessingMLBasicDef::BreakElt_strategy)
def test_wordprocessingmlbasicdef::breakelt_type_type(instance):
    assert isinstance(instance.type, stringtype)


@given(instance=WordprocessingMLBasicDef::BreakElt_strategy)
def test_wordprocessingmlbasicdef::breakelt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=WordprocessingMLBasicDef::RunContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::runcontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::RunContentElt)

@given(instance=RunElt_strategy)
@settings(max_examples=50)
def test_runelt_instantiation(instance):
    assert isinstance(instance, RunElt)

@given(instance=WordprocessingMLBasicDef::RunPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::runprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::RunPrElt)

@given(instance=ParaPrElt_strategy)
@settings(max_examples=50)
def test_paraprelt_instantiation(instance):
    assert isinstance(instance, ParaPrElt)

@given(instance=BlockLevelChunkElt_strategy)
@settings(max_examples=50)
def test_blocklevelchunkelt_instantiation(instance):
    assert isinstance(instance, BlockLevelChunkElt)

@given(instance=WordprocessingMLBasicDef::RunLevelElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::runlevelelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::RunLevelElt)

@given(instance=WordprocessingMLBasicDef::ParaElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::paraelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::ParaElt)

@given(instance=RunPrElt_strategy)
@settings(max_examples=50)
def test_runprelt_instantiation(instance):
    assert isinstance(instance, RunPrElt)

@given(instance=WordprocessingMLBasicDef::ParaContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::paracontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::ParaContentElt)

@given(instance=ParaElt_strategy)
@settings(max_examples=50)
def test_paraelt_instantiation(instance):
    assert isinstance(instance, ParaElt)

@given(instance=WordprocessingMLBasicDef::ParaPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::paraprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::ParaPrElt)

@given(instance=ParaContentElt_strategy)
@settings(max_examples=50)
def test_paracontentelt_instantiation(instance):
    assert isinstance(instance, ParaContentElt)

@given(instance=WordprocessingMLBasicDef::SimpleFieldElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::simplefieldelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::SimpleFieldElt)

@given(instance=WordprocessingMLBasicDef::HLinkElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::hlinkelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::HLinkElt)

@given(instance=WordprocessingMLBasicDef::SubDocElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::subdocelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::SubDocElt)

@given(instance=WordprocessingMLBasicDef::RunElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::runelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::RunElt)

@given(instance=WordprocessingMLBasicDef::BodyElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::bodyelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::BodyElt)

@given(instance=NoteElt_strategy)
@settings(max_examples=50)
def test_noteelt_instantiation(instance):
    assert isinstance(instance, NoteElt)

@given(instance=WordprocessingMLBasicDef::Footnote_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::footnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::Footnote)

@given(instance=WordprocessingMLBasicDef::Endnote_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::endnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::Endnote)

@given(instance=WordprocessingMLBasicDef::BlockLevelElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::blocklevelelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::BlockLevelElt)

@given(instance=SectPrElt_strategy)
@settings(max_examples=50)
def test_sectprelt_instantiation(instance):
    assert isinstance(instance, SectPrElt)

@given(instance=BlockLevelElt_strategy)
@settings(max_examples=50)
def test_blocklevelelt_instantiation(instance):
    assert isinstance(instance, BlockLevelElt)

@given(instance=WordprocessingMLBasicDef::BlockLevelChunkElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::blocklevelchunkelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::BlockLevelChunkElt)

@given(instance=WordprocessingMLBasicDef::CfChunk_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::cfchunk_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::CfChunk)

@given(instance=FontsListElt_strategy)
@settings(max_examples=50)
def test_fontslistelt_instantiation(instance):
    assert isinstance(instance, FontsListElt)

@given(instance=WordprocessingMLBasicDef::DocPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::docprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::DocPrElt)

@given(instance=StringProperty_strategy)
@settings(max_examples=50)
def test_stringproperty_instantiation(instance):
    assert isinstance(instance, StringProperty)

@given(instance=BodyElt_strategy)
@settings(max_examples=50)
def test_bodyelt_instantiation(instance):
    assert isinstance(instance, BodyElt)

@given(instance=DocPrElt_strategy)
@settings(max_examples=50)
def test_docprelt_instantiation(instance):
    assert isinstance(instance, DocPrElt)

@given(instance=StylesElt_strategy)
@settings(max_examples=50)
def test_styleselt_instantiation(instance):
    assert isinstance(instance, StylesElt)

@given(instance=ListsElt_strategy)
@settings(max_examples=50)
def test_listselt_instantiation(instance):
    assert isinstance(instance, ListsElt)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=WordprocessingMLBasicDef::WordDocument_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::worddocument_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::WordDocument)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=WordprocessingMLBasicDef::StringType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::stringtype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::StringType)

@given(instance=WordprocessingMLBasicDef::StringType_strategy)
def test_wordprocessingmlbasicdef::stringtype_val_type(instance):
    assert isinstance(instance.val, stringtype)


@given(instance=WordprocessingMLBasicDef::StringType_strategy)
def test_wordprocessingmlbasicdef::stringtype_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=StringType_strategy)
@settings(max_examples=50)
def test_stringtype_instantiation(instance):
    assert isinstance(instance, StringType)

@given(instance=WordprocessingMLBasicDef::InstrText_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::instrtext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::InstrText)

@given(instance=WordprocessingMLBasicDef::Text_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::text_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::Text)

@given(instance=WordprocessingMLBasicDef::DelInstrText_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::delinstrtext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::DelInstrText)

@given(instance=WordprocessingMLBasicDef::DelText_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::deltext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::DelText)

@given(instance=WordprocessingMLBasicDef::StringProperty_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::stringproperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::StringProperty)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=WordprocessingMLBasicDef::SmartTagType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::smarttagtype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::SmartTagType)

@given(instance=WordprocessingMLBasicDef::SmartTagType_strategy)
def test_wordprocessingmlbasicdef::smarttagtype_url_type(instance):
    assert isinstance(instance.url, stringtype)


@given(instance=WordprocessingMLBasicDef::SmartTagType_strategy)
def test_wordprocessingmlbasicdef::smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=WordprocessingMLBasicDef::SmartTagType_strategy)
def test_wordprocessingmlbasicdef::smarttagtype_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=WordprocessingMLBasicDef::SmartTagType_strategy)
def test_wordprocessingmlbasicdef::smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WordprocessingMLBasicDef::SmartTagType_strategy)
def test_wordprocessingmlbasicdef::smarttagtype_namespaceuri_type(instance):
    assert isinstance(instance.namespaceuri, stringtype)


@given(instance=WordprocessingMLBasicDef::SmartTagType_strategy)
def test_wordprocessingmlbasicdef::smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=WordprocessingMLBasicDef::SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::smarttagscollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::SmartTagsCollection)

@given(instance=WordprocessingMLBasicDef::CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::CustomDocumentPropertiesCollection)

@given(instance=WordprocessingMLBasicDef::CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::customdocumentproperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::CustomDocumentProperty)

@given(instance=WordprocessingMLBasicDef::CustomDocumentProperty_strategy)
def test_wordprocessingmlbasicdef::customdocumentproperty_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=WordprocessingMLBasicDef::CustomDocumentProperty_strategy)
def test_wordprocessingmlbasicdef::customdocumentproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, CustomDocumentProperty)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=WordprocessingMLBasicDef::FloatValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::floatvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::FloatValue)

@given(instance=WordprocessingMLBasicDef::FloatValue_strategy)
def test_wordprocessingmlbasicdef::floatvalue_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=WordprocessingMLBasicDef::FloatValue_strategy)
def test_wordprocessingmlbasicdef::floatvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLBasicDef::BooleanValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::booleanvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::BooleanValue)

@given(instance=WordprocessingMLBasicDef::BooleanValue_strategy)
def test_wordprocessingmlbasicdef::booleanvalue_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=WordprocessingMLBasicDef::BooleanValue_strategy)
def test_wordprocessingmlbasicdef::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLBasicDef::DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::datetimetypevalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::DateTimeTypeValue)

@given(instance=WordprocessingMLBasicDef::StringValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::stringvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::StringValue)

@given(instance=WordprocessingMLBasicDef::StringValue_strategy)
def test_wordprocessingmlbasicdef::stringvalue_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=WordprocessingMLBasicDef::StringValue_strategy)
def test_wordprocessingmlbasicdef::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLBasicDef::ValueType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::valuetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::ValueType)

@given(instance=WordDocument_strategy)
@settings(max_examples=50)
def test_worddocument_instantiation(instance):
    assert isinstance(instance, WordDocument)

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::DocumentPropertiesCollection)

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_lines_type(instance):
    assert isinstance(instance.lines, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_bytes_type(instance):
    assert isinstance(instance.bytes, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_guid_type(instance):
    assert isinstance(instance.guid, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_presentationFormat_type(instance):
    assert isinstance(instance.presentationFormat, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_characters_type(instance):
    assert isinstance(instance.characters, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_paragraphs_type(instance):
    assert isinstance(instance.paragraphs, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_charactersWithSpaces_type(instance):
    assert isinstance(instance.charactersWithSpaces, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_words_type(instance):
    assert isinstance(instance.words, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_hyperlinkBase_type(instance):
    assert isinstance(instance.hyperlinkBase, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_totalTime_type(instance):
    assert isinstance(instance.totalTime, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_appName_type(instance):
    assert isinstance(instance.appName, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_pages_type(instance):
    assert isinstance(instance.pages, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_author_type(instance):
    assert isinstance(instance.author, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_revision_type(instance):
    assert isinstance(instance.revision, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_lastAuthor_type(instance):
    assert isinstance(instance.lastAuthor, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, stringtype)


@given(instance=WordprocessingMLBasicDef::DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::datetimetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::DateTimeType)

@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_day_type(instance):
    assert isinstance(instance.day, stringtype)


@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original

@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, stringtype)


@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_month_type(instance):
    assert isinstance(instance.month, stringtype)


@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, stringtype)


@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_second_type(instance):
    assert isinstance(instance.second, stringtype)


@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_year_type(instance):
    assert isinstance(instance.year, stringtype)


@given(instance=WordprocessingMLBasicDef::DateTimeType_strategy)
def test_wordprocessingmlbasicdef::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=WordprocessingMLBasicDef::VersionType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef::versiontype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef::VersionType)

@given(instance=WordprocessingMLBasicDef::VersionType_strategy)
def test_wordprocessingmlbasicdef::versiontype_nn_type(instance):
    assert isinstance(instance.nn, stringtype)


@given(instance=WordprocessingMLBasicDef::VersionType_strategy)
def test_wordprocessingmlbasicdef::versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original

@given(instance=WordprocessingMLBasicDef::VersionType_strategy)
def test_wordprocessingmlbasicdef::versiontype_n_type(instance):
    assert isinstance(instance.n, stringtype)


@given(instance=WordprocessingMLBasicDef::VersionType_strategy)
def test_wordprocessingmlbasicdef::versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original
