import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    WordprocessingMLTableElts::TabElt,
    WordprocessingMLTableElts::PictureType,
    WordprocessingMLTableElts::SectPrElt,
    WordprocessingMLTableElts::ListsElt,
    WordprocessingMLTableElts::FontsListElt,
    WordprocessingMLTableElts::TableCellPrElt,
    WordprocessingMLTableElts::StylesElt,
    WordprocessingMLTableElts::TableCellElt,
    WordprocessingMLTableElts::RowContentElt,
    TableCellPrElt,
    RowContentElt,
    TableRowPrElt,
    TablePrExElt,
    WordprocessingMLTableElts::RowElt,
    WordprocessingMLTableElts::TableRowPrElt,
    WordprocessingMLTableElts::TablePrExElt,
    RowElt,
    WordprocessingMLTableElts::TableContentElt,
    WordprocessingMLTableElts::TableGridElt,
    TableElt,
    RunLevelElt,
    TableGridElt,
    TablePrElt,
    WordprocessingMLTableElts::TablePrElt,
    TableContentElt,
    WordprocessingMLTableElts::FldCharElt,
    FldCharElt,
    TabElt,
    WordprocessingMLTableElts::SymElt,
    WordprocessingMLTableElts::NoteElt,
    SymElt,
    PictureType,
    RunElt,
    WordprocessingMLTableElts::RunPrElt,
    RunContentElt,
    WordprocessingMLTableElts::AnnotationRef,
    WordprocessingMLTableElts::BreakElt,
    WordprocessingMLTableElts::FootnoteRef,
    WordprocessingMLTableElts::PgNum,
    WordprocessingMLTableElts::ContinuationSeparator,
    WordprocessingMLTableElts::FldChar,
    WordprocessingMLTableElts::NoBreakHyphen,
    WordprocessingMLTableElts::Picture,
    WordprocessingMLTableElts::Separator,
    WordprocessingMLTableElts::Tab,
    WordprocessingMLTableElts::EndnoteRef,
    WordprocessingMLTableElts::SoftHyphen,
    WordprocessingMLTableElts::Cr,
    WordprocessingMLTableElts::Symbol,
    RunPrElt,
    WordprocessingMLTableElts::ParaContentElt,
    WordprocessingMLTableElts::RunContentElt,
    ParaContentElt,
    WordprocessingMLTableElts::HLinkElt,
    WordprocessingMLTableElts::SubDocElt,
    WordprocessingMLTableElts::RunElt,
    WordprocessingMLTableElts::SimpleFieldElt,
    ParaPrElt,
    BlockLevelChunkElt,
    WordprocessingMLTableElts::TableElt,
    WordprocessingMLTableElts::RunLevelElt,
    WordprocessingMLTableElts::ParaElt,
    TableCellElt,
    NoteElt,
    WordprocessingMLTableElts::Endnote,
    WordprocessingMLTableElts::Footnote,
    ParaElt,
    WordprocessingMLTableElts::ParaPrElt,
    BlockLevelElt,
    WordprocessingMLTableElts::BlockLevelChunkElt,
    WordprocessingMLTableElts::CfChunk,
    WordprocessingMLTableElts::BodyElt,
    WordprocessingMLTableElts::DocPrElt,
    BodyElt,
    WordprocessingMLTableElts::BlockLevelElt,
    SectPrElt,
    StylesElt,
    ListsElt,
    FontsListElt,
    DocPrElt,
    DocumentPropertiesCollection,
    WordprocessingMLTableElts::WordDocument,
    StringProperty,
    WordprocessingMLTableElts::StringType,
    StringType,
    WordprocessingMLTableElts::InstrText,
    WordprocessingMLTableElts::Text,
    WordprocessingMLTableElts::DelText,
    WordprocessingMLTableElts::DelInstrText,
    WordprocessingMLTableElts::StringProperty,
    SmartTagType,
    WordprocessingMLTableElts::SmartTagsCollection,
    CustomDocumentPropertiesCollection,
    WordprocessingMLTableElts::CustomDocumentProperty,
    CustomDocumentProperty,
    SmartTagsCollection,
    WordprocessingMLTableElts::SmartTagType,
    WordprocessingMLTableElts::CustomDocumentPropertiesCollection,
    VersionType,
    WordDocument,
    WordprocessingMLTableElts::DocumentPropertiesCollection,
    ValueType,
    WordprocessingMLTableElts::FloatValue,
    WordprocessingMLTableElts::BooleanValue,
    WordprocessingMLTableElts::StringValue,
    WordprocessingMLTableElts::ValueType,
    WordprocessingMLTableElts::VersionType,
    DateTimeType,
    WordprocessingMLTableElts::DateTimeTypeValue,
    WordprocessingMLTableElts::DateTimeType,
    FldCharTypeProperty,
    OnOffType,
    NoteValue,
    BreakType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wordprocessingmltableelts::tabelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TabElt)


def test_wordprocessingmltableelts::tabelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TabElt.__init__)


def test_wordprocessingmltableelts::tabelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TabElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::picturetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::PictureType)


def test_wordprocessingmltableelts::picturetype_constructor_exists():
    assert callable(WordprocessingMLTableElts::PictureType.__init__)


def test_wordprocessingmltableelts::picturetype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::PictureType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::sectprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::SectPrElt)


def test_wordprocessingmltableelts::sectprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::SectPrElt.__init__)


def test_wordprocessingmltableelts::sectprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::SectPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::listselt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::ListsElt)


def test_wordprocessingmltableelts::listselt_constructor_exists():
    assert callable(WordprocessingMLTableElts::ListsElt.__init__)


def test_wordprocessingmltableelts::listselt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::ListsElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::fontslistelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::FontsListElt)


def test_wordprocessingmltableelts::fontslistelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::FontsListElt.__init__)


def test_wordprocessingmltableelts::fontslistelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::FontsListElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::tablecellprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TableCellPrElt)


def test_wordprocessingmltableelts::tablecellprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TableCellPrElt.__init__)


def test_wordprocessingmltableelts::tablecellprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TableCellPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::styleselt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::StylesElt)


def test_wordprocessingmltableelts::styleselt_constructor_exists():
    assert callable(WordprocessingMLTableElts::StylesElt.__init__)


def test_wordprocessingmltableelts::styleselt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::StylesElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::tablecellelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TableCellElt)


def test_wordprocessingmltableelts::tablecellelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TableCellElt.__init__)


def test_wordprocessingmltableelts::tablecellelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TableCellElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::rowcontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::RowContentElt)


def test_wordprocessingmltableelts::rowcontentelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::RowContentElt.__init__)


def test_wordprocessingmltableelts::rowcontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::RowContentElt.__init__)
    params = list(sig.parameters.keys())



def test_tablecellprelt_is_not_abstract():
    assert not inspect.isabstract(TableCellPrElt)


def test_tablecellprelt_constructor_exists():
    assert callable(TableCellPrElt.__init__)


def test_tablecellprelt_constructor_args():
    sig = inspect.signature(TableCellPrElt.__init__)
    params = list(sig.parameters.keys())



def test_rowcontentelt_is_not_abstract():
    assert not inspect.isabstract(RowContentElt)


def test_rowcontentelt_constructor_exists():
    assert callable(RowContentElt.__init__)


def test_rowcontentelt_constructor_args():
    sig = inspect.signature(RowContentElt.__init__)
    params = list(sig.parameters.keys())



def test_tablerowprelt_is_not_abstract():
    assert not inspect.isabstract(TableRowPrElt)


def test_tablerowprelt_constructor_exists():
    assert callable(TableRowPrElt.__init__)


def test_tablerowprelt_constructor_args():
    sig = inspect.signature(TableRowPrElt.__init__)
    params = list(sig.parameters.keys())



def test_tableprexelt_is_not_abstract():
    assert not inspect.isabstract(TablePrExElt)


def test_tableprexelt_constructor_exists():
    assert callable(TablePrExElt.__init__)


def test_tableprexelt_constructor_args():
    sig = inspect.signature(TablePrExElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::rowelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::RowElt)


def test_wordprocessingmltableelts::rowelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::RowElt.__init__)


def test_wordprocessingmltableelts::rowelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::RowElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::tablerowprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TableRowPrElt)


def test_wordprocessingmltableelts::tablerowprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TableRowPrElt.__init__)


def test_wordprocessingmltableelts::tablerowprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TableRowPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::tableprexelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TablePrExElt)


def test_wordprocessingmltableelts::tableprexelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TablePrExElt.__init__)


def test_wordprocessingmltableelts::tableprexelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TablePrExElt.__init__)
    params = list(sig.parameters.keys())



def test_rowelt_is_not_abstract():
    assert not inspect.isabstract(RowElt)


def test_rowelt_constructor_exists():
    assert callable(RowElt.__init__)


def test_rowelt_constructor_args():
    sig = inspect.signature(RowElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::tablecontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TableContentElt)


def test_wordprocessingmltableelts::tablecontentelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TableContentElt.__init__)


def test_wordprocessingmltableelts::tablecontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TableContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::tablegridelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TableGridElt)


def test_wordprocessingmltableelts::tablegridelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TableGridElt.__init__)


def test_wordprocessingmltableelts::tablegridelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TableGridElt.__init__)
    params = list(sig.parameters.keys())



def test_tableelt_is_not_abstract():
    assert not inspect.isabstract(TableElt)


def test_tableelt_constructor_exists():
    assert callable(TableElt.__init__)


def test_tableelt_constructor_args():
    sig = inspect.signature(TableElt.__init__)
    params = list(sig.parameters.keys())



def test_runlevelelt_is_not_abstract():
    assert not inspect.isabstract(RunLevelElt)


def test_runlevelelt_constructor_exists():
    assert callable(RunLevelElt.__init__)


def test_runlevelelt_constructor_args():
    sig = inspect.signature(RunLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_tablegridelt_is_not_abstract():
    assert not inspect.isabstract(TableGridElt)


def test_tablegridelt_constructor_exists():
    assert callable(TableGridElt.__init__)


def test_tablegridelt_constructor_args():
    sig = inspect.signature(TableGridElt.__init__)
    params = list(sig.parameters.keys())



def test_tableprelt_is_not_abstract():
    assert not inspect.isabstract(TablePrElt)


def test_tableprelt_constructor_exists():
    assert callable(TablePrElt.__init__)


def test_tableprelt_constructor_args():
    sig = inspect.signature(TablePrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::tableprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TablePrElt)


def test_wordprocessingmltableelts::tableprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TablePrElt.__init__)


def test_wordprocessingmltableelts::tableprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TablePrElt.__init__)
    params = list(sig.parameters.keys())



def test_tablecontentelt_is_not_abstract():
    assert not inspect.isabstract(TableContentElt)


def test_tablecontentelt_constructor_exists():
    assert callable(TableContentElt.__init__)


def test_tablecontentelt_constructor_args():
    sig = inspect.signature(TableContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::fldcharelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::FldCharElt)


def test_wordprocessingmltableelts::fldcharelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::FldCharElt.__init__)


def test_wordprocessingmltableelts::fldcharelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::FldCharElt.__init__)
    params = list(sig.parameters.keys())
    assert "fldCharType" in params, "Missing parameter 'fldCharType'"
    assert "fldLock" in params, "Missing parameter 'fldLock'"

def test_wordprocessingmltableelts::fldcharelt_has_fldCharType():
    assert hasattr(WordprocessingMLTableElts::FldCharElt, "fldCharType")
    descriptor = None
    for klass in WordprocessingMLTableElts::FldCharElt.__mro__:
        if "fldCharType" in klass.__dict__:
            descriptor = klass.__dict__["fldCharType"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::fldcharelt_has_fldLock():
    assert hasattr(WordprocessingMLTableElts::FldCharElt, "fldLock")
    descriptor = None
    for klass in WordprocessingMLTableElts::FldCharElt.__mro__:
        if "fldLock" in klass.__dict__:
            descriptor = klass.__dict__["fldLock"]
            break
    assert isinstance(descriptor, property)



def test_fldcharelt_is_not_abstract():
    assert not inspect.isabstract(FldCharElt)


def test_fldcharelt_constructor_exists():
    assert callable(FldCharElt.__init__)


def test_fldcharelt_constructor_args():
    sig = inspect.signature(FldCharElt.__init__)
    params = list(sig.parameters.keys())



def test_tabelt_is_not_abstract():
    assert not inspect.isabstract(TabElt)


def test_tabelt_constructor_exists():
    assert callable(TabElt.__init__)


def test_tabelt_constructor_args():
    sig = inspect.signature(TabElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::symelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::SymElt)


def test_wordprocessingmltableelts::symelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::SymElt.__init__)


def test_wordprocessingmltableelts::symelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::SymElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::noteelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::NoteElt)


def test_wordprocessingmltableelts::noteelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::NoteElt.__init__)


def test_wordprocessingmltableelts::noteelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::NoteElt.__init__)
    params = list(sig.parameters.keys())
    assert "suppressRef" in params, "Missing parameter 'suppressRef'"
    assert "type" in params, "Missing parameter 'type'"

def test_wordprocessingmltableelts::noteelt_has_suppressRef():
    assert hasattr(WordprocessingMLTableElts::NoteElt, "suppressRef")
    descriptor = None
    for klass in WordprocessingMLTableElts::NoteElt.__mro__:
        if "suppressRef" in klass.__dict__:
            descriptor = klass.__dict__["suppressRef"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::noteelt_has_type():
    assert hasattr(WordprocessingMLTableElts::NoteElt, "type")
    descriptor = None
    for klass in WordprocessingMLTableElts::NoteElt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



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



def test_runelt_is_not_abstract():
    assert not inspect.isabstract(RunElt)


def test_runelt_constructor_exists():
    assert callable(RunElt.__init__)


def test_runelt_constructor_args():
    sig = inspect.signature(RunElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::runprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::RunPrElt)


def test_wordprocessingmltableelts::runprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::RunPrElt.__init__)


def test_wordprocessingmltableelts::runprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::RunPrElt.__init__)
    params = list(sig.parameters.keys())



def test_runcontentelt_is_not_abstract():
    assert not inspect.isabstract(RunContentElt)


def test_runcontentelt_constructor_exists():
    assert callable(RunContentElt.__init__)


def test_runcontentelt_constructor_args():
    sig = inspect.signature(RunContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::annotationref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::AnnotationRef)


def test_wordprocessingmltableelts::annotationref_constructor_exists():
    assert callable(WordprocessingMLTableElts::AnnotationRef.__init__)


def test_wordprocessingmltableelts::annotationref_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::AnnotationRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::breakelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::BreakElt)


def test_wordprocessingmltableelts::breakelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::BreakElt.__init__)


def test_wordprocessingmltableelts::breakelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::BreakElt.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_wordprocessingmltableelts::breakelt_has_type():
    assert hasattr(WordprocessingMLTableElts::BreakElt, "type")
    descriptor = None
    for klass in WordprocessingMLTableElts::BreakElt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts::footnoteref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::FootnoteRef)


def test_wordprocessingmltableelts::footnoteref_constructor_exists():
    assert callable(WordprocessingMLTableElts::FootnoteRef.__init__)


def test_wordprocessingmltableelts::footnoteref_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::FootnoteRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::pgnum_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::PgNum)


def test_wordprocessingmltableelts::pgnum_constructor_exists():
    assert callable(WordprocessingMLTableElts::PgNum.__init__)


def test_wordprocessingmltableelts::pgnum_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::PgNum.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::continuationseparator_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::ContinuationSeparator)


def test_wordprocessingmltableelts::continuationseparator_constructor_exists():
    assert callable(WordprocessingMLTableElts::ContinuationSeparator.__init__)


def test_wordprocessingmltableelts::continuationseparator_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::ContinuationSeparator.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::fldchar_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::FldChar)


def test_wordprocessingmltableelts::fldchar_constructor_exists():
    assert callable(WordprocessingMLTableElts::FldChar.__init__)


def test_wordprocessingmltableelts::fldchar_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::FldChar.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::nobreakhyphen_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::NoBreakHyphen)


def test_wordprocessingmltableelts::nobreakhyphen_constructor_exists():
    assert callable(WordprocessingMLTableElts::NoBreakHyphen.__init__)


def test_wordprocessingmltableelts::nobreakhyphen_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::NoBreakHyphen.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::picture_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::Picture)


def test_wordprocessingmltableelts::picture_constructor_exists():
    assert callable(WordprocessingMLTableElts::Picture.__init__)


def test_wordprocessingmltableelts::picture_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::Picture.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::separator_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::Separator)


def test_wordprocessingmltableelts::separator_constructor_exists():
    assert callable(WordprocessingMLTableElts::Separator.__init__)


def test_wordprocessingmltableelts::separator_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::Separator.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::tab_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::Tab)


def test_wordprocessingmltableelts::tab_constructor_exists():
    assert callable(WordprocessingMLTableElts::Tab.__init__)


def test_wordprocessingmltableelts::tab_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::Tab.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::endnoteref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::EndnoteRef)


def test_wordprocessingmltableelts::endnoteref_constructor_exists():
    assert callable(WordprocessingMLTableElts::EndnoteRef.__init__)


def test_wordprocessingmltableelts::endnoteref_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::EndnoteRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::softhyphen_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::SoftHyphen)


def test_wordprocessingmltableelts::softhyphen_constructor_exists():
    assert callable(WordprocessingMLTableElts::SoftHyphen.__init__)


def test_wordprocessingmltableelts::softhyphen_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::SoftHyphen.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::cr_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::Cr)


def test_wordprocessingmltableelts::cr_constructor_exists():
    assert callable(WordprocessingMLTableElts::Cr.__init__)


def test_wordprocessingmltableelts::cr_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::Cr.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::symbol_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::Symbol)


def test_wordprocessingmltableelts::symbol_constructor_exists():
    assert callable(WordprocessingMLTableElts::Symbol.__init__)


def test_wordprocessingmltableelts::symbol_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::Symbol.__init__)
    params = list(sig.parameters.keys())



def test_runprelt_is_not_abstract():
    assert not inspect.isabstract(RunPrElt)


def test_runprelt_constructor_exists():
    assert callable(RunPrElt.__init__)


def test_runprelt_constructor_args():
    sig = inspect.signature(RunPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::paracontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::ParaContentElt)


def test_wordprocessingmltableelts::paracontentelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::ParaContentElt.__init__)


def test_wordprocessingmltableelts::paracontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::ParaContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::runcontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::RunContentElt)


def test_wordprocessingmltableelts::runcontentelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::RunContentElt.__init__)


def test_wordprocessingmltableelts::runcontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::RunContentElt.__init__)
    params = list(sig.parameters.keys())



def test_paracontentelt_is_not_abstract():
    assert not inspect.isabstract(ParaContentElt)


def test_paracontentelt_constructor_exists():
    assert callable(ParaContentElt.__init__)


def test_paracontentelt_constructor_args():
    sig = inspect.signature(ParaContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::hlinkelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::HLinkElt)


def test_wordprocessingmltableelts::hlinkelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::HLinkElt.__init__)


def test_wordprocessingmltableelts::hlinkelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::HLinkElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::subdocelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::SubDocElt)


def test_wordprocessingmltableelts::subdocelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::SubDocElt.__init__)


def test_wordprocessingmltableelts::subdocelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::SubDocElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::runelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::RunElt)


def test_wordprocessingmltableelts::runelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::RunElt.__init__)


def test_wordprocessingmltableelts::runelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::RunElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::simplefieldelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::SimpleFieldElt)


def test_wordprocessingmltableelts::simplefieldelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::SimpleFieldElt.__init__)


def test_wordprocessingmltableelts::simplefieldelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::SimpleFieldElt.__init__)
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



def test_wordprocessingmltableelts::tableelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::TableElt)


def test_wordprocessingmltableelts::tableelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::TableElt.__init__)


def test_wordprocessingmltableelts::tableelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::TableElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::runlevelelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::RunLevelElt)


def test_wordprocessingmltableelts::runlevelelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::RunLevelElt.__init__)


def test_wordprocessingmltableelts::runlevelelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::RunLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::paraelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::ParaElt)


def test_wordprocessingmltableelts::paraelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::ParaElt.__init__)


def test_wordprocessingmltableelts::paraelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::ParaElt.__init__)
    params = list(sig.parameters.keys())



def test_tablecellelt_is_not_abstract():
    assert not inspect.isabstract(TableCellElt)


def test_tablecellelt_constructor_exists():
    assert callable(TableCellElt.__init__)


def test_tablecellelt_constructor_args():
    sig = inspect.signature(TableCellElt.__init__)
    params = list(sig.parameters.keys())



def test_noteelt_is_not_abstract():
    assert not inspect.isabstract(NoteElt)


def test_noteelt_constructor_exists():
    assert callable(NoteElt.__init__)


def test_noteelt_constructor_args():
    sig = inspect.signature(NoteElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::endnote_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::Endnote)


def test_wordprocessingmltableelts::endnote_constructor_exists():
    assert callable(WordprocessingMLTableElts::Endnote.__init__)


def test_wordprocessingmltableelts::endnote_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::Endnote.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::footnote_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::Footnote)


def test_wordprocessingmltableelts::footnote_constructor_exists():
    assert callable(WordprocessingMLTableElts::Footnote.__init__)


def test_wordprocessingmltableelts::footnote_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::Footnote.__init__)
    params = list(sig.parameters.keys())



def test_paraelt_is_not_abstract():
    assert not inspect.isabstract(ParaElt)


def test_paraelt_constructor_exists():
    assert callable(ParaElt.__init__)


def test_paraelt_constructor_args():
    sig = inspect.signature(ParaElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::paraprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::ParaPrElt)


def test_wordprocessingmltableelts::paraprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::ParaPrElt.__init__)


def test_wordprocessingmltableelts::paraprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::ParaPrElt.__init__)
    params = list(sig.parameters.keys())



def test_blocklevelelt_is_not_abstract():
    assert not inspect.isabstract(BlockLevelElt)


def test_blocklevelelt_constructor_exists():
    assert callable(BlockLevelElt.__init__)


def test_blocklevelelt_constructor_args():
    sig = inspect.signature(BlockLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::blocklevelchunkelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::BlockLevelChunkElt)


def test_wordprocessingmltableelts::blocklevelchunkelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::BlockLevelChunkElt.__init__)


def test_wordprocessingmltableelts::blocklevelchunkelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::BlockLevelChunkElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::cfchunk_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::CfChunk)


def test_wordprocessingmltableelts::cfchunk_constructor_exists():
    assert callable(WordprocessingMLTableElts::CfChunk.__init__)


def test_wordprocessingmltableelts::cfchunk_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::CfChunk.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::bodyelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::BodyElt)


def test_wordprocessingmltableelts::bodyelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::BodyElt.__init__)


def test_wordprocessingmltableelts::bodyelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::BodyElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::docprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::DocPrElt)


def test_wordprocessingmltableelts::docprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::DocPrElt.__init__)


def test_wordprocessingmltableelts::docprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::DocPrElt.__init__)
    params = list(sig.parameters.keys())



def test_bodyelt_is_not_abstract():
    assert not inspect.isabstract(BodyElt)


def test_bodyelt_constructor_exists():
    assert callable(BodyElt.__init__)


def test_bodyelt_constructor_args():
    sig = inspect.signature(BodyElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::blocklevelelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::BlockLevelElt)


def test_wordprocessingmltableelts::blocklevelelt_constructor_exists():
    assert callable(WordprocessingMLTableElts::BlockLevelElt.__init__)


def test_wordprocessingmltableelts::blocklevelelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::BlockLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_sectprelt_is_not_abstract():
    assert not inspect.isabstract(SectPrElt)


def test_sectprelt_constructor_exists():
    assert callable(SectPrElt.__init__)


def test_sectprelt_constructor_args():
    sig = inspect.signature(SectPrElt.__init__)
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



def test_fontslistelt_is_not_abstract():
    assert not inspect.isabstract(FontsListElt)


def test_fontslistelt_constructor_exists():
    assert callable(FontsListElt.__init__)


def test_fontslistelt_constructor_args():
    sig = inspect.signature(FontsListElt.__init__)
    params = list(sig.parameters.keys())



def test_docprelt_is_not_abstract():
    assert not inspect.isabstract(DocPrElt)


def test_docprelt_constructor_exists():
    assert callable(DocPrElt.__init__)


def test_docprelt_constructor_args():
    sig = inspect.signature(DocPrElt.__init__)
    params = list(sig.parameters.keys())



def test_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(DocumentPropertiesCollection)


def test_documentpropertiescollection_constructor_exists():
    assert callable(DocumentPropertiesCollection.__init__)


def test_documentpropertiescollection_constructor_args():
    sig = inspect.signature(DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::worddocument_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::WordDocument)


def test_wordprocessingmltableelts::worddocument_constructor_exists():
    assert callable(WordprocessingMLTableElts::WordDocument.__init__)


def test_wordprocessingmltableelts::worddocument_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::WordDocument.__init__)
    params = list(sig.parameters.keys())



def test_stringproperty_is_not_abstract():
    assert not inspect.isabstract(StringProperty)


def test_stringproperty_constructor_exists():
    assert callable(StringProperty.__init__)


def test_stringproperty_constructor_args():
    sig = inspect.signature(StringProperty.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::stringtype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::StringType)


def test_wordprocessingmltableelts::stringtype_constructor_exists():
    assert callable(WordprocessingMLTableElts::StringType.__init__)


def test_wordprocessingmltableelts::stringtype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::StringType.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_wordprocessingmltableelts::stringtype_has_val():
    assert hasattr(WordprocessingMLTableElts::StringType, "val")
    descriptor = None
    for klass in WordprocessingMLTableElts::StringType.__mro__:
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



def test_wordprocessingmltableelts::instrtext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::InstrText)


def test_wordprocessingmltableelts::instrtext_constructor_exists():
    assert callable(WordprocessingMLTableElts::InstrText.__init__)


def test_wordprocessingmltableelts::instrtext_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::InstrText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::text_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::Text)


def test_wordprocessingmltableelts::text_constructor_exists():
    assert callable(WordprocessingMLTableElts::Text.__init__)


def test_wordprocessingmltableelts::text_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::Text.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::deltext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::DelText)


def test_wordprocessingmltableelts::deltext_constructor_exists():
    assert callable(WordprocessingMLTableElts::DelText.__init__)


def test_wordprocessingmltableelts::deltext_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::DelText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::delinstrtext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::DelInstrText)


def test_wordprocessingmltableelts::delinstrtext_constructor_exists():
    assert callable(WordprocessingMLTableElts::DelInstrText.__init__)


def test_wordprocessingmltableelts::delinstrtext_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::DelInstrText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::stringproperty_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::StringProperty)


def test_wordprocessingmltableelts::stringproperty_constructor_exists():
    assert callable(WordprocessingMLTableElts::StringProperty.__init__)


def test_wordprocessingmltableelts::stringproperty_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::StringProperty.__init__)
    params = list(sig.parameters.keys())



def test_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SmartTagType)


def test_smarttagtype_constructor_exists():
    assert callable(SmartTagType.__init__)


def test_smarttagtype_constructor_args():
    sig = inspect.signature(SmartTagType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::SmartTagsCollection)


def test_wordprocessingmltableelts::smarttagscollection_constructor_exists():
    assert callable(WordprocessingMLTableElts::SmartTagsCollection.__init__)


def test_wordprocessingmltableelts::smarttagscollection_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::CustomDocumentProperty)


def test_wordprocessingmltableelts::customdocumentproperty_constructor_exists():
    assert callable(WordprocessingMLTableElts::CustomDocumentProperty.__init__)


def test_wordprocessingmltableelts::customdocumentproperty_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wordprocessingmltableelts::customdocumentproperty_has_name():
    assert hasattr(WordprocessingMLTableElts::CustomDocumentProperty, "name")
    descriptor = None
    for klass in WordprocessingMLTableElts::CustomDocumentProperty.__mro__:
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



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::smarttagtype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::SmartTagType)


def test_wordprocessingmltableelts::smarttagtype_constructor_exists():
    assert callable(WordprocessingMLTableElts::SmartTagType.__init__)


def test_wordprocessingmltableelts::smarttagtype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"

def test_wordprocessingmltableelts::smarttagtype_has_namespaceuri():
    assert hasattr(WordprocessingMLTableElts::SmartTagType, "namespaceuri")
    descriptor = None
    for klass in WordprocessingMLTableElts::SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::smarttagtype_has_name():
    assert hasattr(WordprocessingMLTableElts::SmartTagType, "name")
    descriptor = None
    for klass in WordprocessingMLTableElts::SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::smarttagtype_has_url():
    assert hasattr(WordprocessingMLTableElts::SmartTagType, "url")
    descriptor = None
    for klass in WordprocessingMLTableElts::SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts::customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::CustomDocumentPropertiesCollection)


def test_wordprocessingmltableelts::customdocumentpropertiescollection_constructor_exists():
    assert callable(WordprocessingMLTableElts::CustomDocumentPropertiesCollection.__init__)


def test_wordprocessingmltableelts::customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_versiontype_is_not_abstract():
    assert not inspect.isabstract(VersionType)


def test_versiontype_constructor_exists():
    assert callable(VersionType.__init__)


def test_versiontype_constructor_args():
    sig = inspect.signature(VersionType.__init__)
    params = list(sig.parameters.keys())



def test_worddocument_is_not_abstract():
    assert not inspect.isabstract(WordDocument)


def test_worddocument_constructor_exists():
    assert callable(WordDocument.__init__)


def test_worddocument_constructor_args():
    sig = inspect.signature(WordDocument.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::DocumentPropertiesCollection)


def test_wordprocessingmltableelts::documentpropertiescollection_constructor_exists():
    assert callable(WordprocessingMLTableElts::DocumentPropertiesCollection.__init__)


def test_wordprocessingmltableelts::documentpropertiescollection_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "description" in params, "Missing parameter 'description'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "category" in params, "Missing parameter 'category'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "words" in params, "Missing parameter 'words'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "company" in params, "Missing parameter 'company'"

def test_wordprocessingmltableelts::documentpropertiescollection_has_bytes():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_manager():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_lastAuthor():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_lines():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_presentationFormat():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_description():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_characters():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_paragraphs():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_category():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_appName():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_pages():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_words():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_guid():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_subject():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_keywords():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_author():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_title():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_revision():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_totalTime():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::documentpropertiescollection_has_company():
    assert hasattr(WordprocessingMLTableElts::DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in WordprocessingMLTableElts::DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::floatvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::FloatValue)


def test_wordprocessingmltableelts::floatvalue_constructor_exists():
    assert callable(WordprocessingMLTableElts::FloatValue.__init__)


def test_wordprocessingmltableelts::floatvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::FloatValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmltableelts::floatvalue_has_value():
    assert hasattr(WordprocessingMLTableElts::FloatValue, "value")
    descriptor = None
    for klass in WordprocessingMLTableElts::FloatValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts::booleanvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::BooleanValue)


def test_wordprocessingmltableelts::booleanvalue_constructor_exists():
    assert callable(WordprocessingMLTableElts::BooleanValue.__init__)


def test_wordprocessingmltableelts::booleanvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmltableelts::booleanvalue_has_value():
    assert hasattr(WordprocessingMLTableElts::BooleanValue, "value")
    descriptor = None
    for klass in WordprocessingMLTableElts::BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts::stringvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::StringValue)


def test_wordprocessingmltableelts::stringvalue_constructor_exists():
    assert callable(WordprocessingMLTableElts::StringValue.__init__)


def test_wordprocessingmltableelts::stringvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmltableelts::stringvalue_has_value():
    assert hasattr(WordprocessingMLTableElts::StringValue, "value")
    descriptor = None
    for klass in WordprocessingMLTableElts::StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts::valuetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::ValueType)


def test_wordprocessingmltableelts::valuetype_constructor_exists():
    assert callable(WordprocessingMLTableElts::ValueType.__init__)


def test_wordprocessingmltableelts::valuetype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::ValueType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::versiontype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::VersionType)


def test_wordprocessingmltableelts::versiontype_constructor_exists():
    assert callable(WordprocessingMLTableElts::VersionType.__init__)


def test_wordprocessingmltableelts::versiontype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "nn" in params, "Missing parameter 'nn'"
    assert "n" in params, "Missing parameter 'n'"

def test_wordprocessingmltableelts::versiontype_has_nn():
    assert hasattr(WordprocessingMLTableElts::VersionType, "nn")
    descriptor = None
    for klass in WordprocessingMLTableElts::VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::versiontype_has_n():
    assert hasattr(WordprocessingMLTableElts::VersionType, "n")
    descriptor = None
    for klass in WordprocessingMLTableElts::VersionType.__mro__:
        if "n" in klass.__dict__:
            descriptor = klass.__dict__["n"]
            break
    assert isinstance(descriptor, property)



def test_datetimetype_is_not_abstract():
    assert not inspect.isabstract(DateTimeType)


def test_datetimetype_constructor_exists():
    assert callable(DateTimeType.__init__)


def test_datetimetype_constructor_args():
    sig = inspect.signature(DateTimeType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::DateTimeTypeValue)


def test_wordprocessingmltableelts::datetimetypevalue_constructor_exists():
    assert callable(WordprocessingMLTableElts::DateTimeTypeValue.__init__)


def test_wordprocessingmltableelts::datetimetypevalue_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts::datetimetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts::DateTimeType)


def test_wordprocessingmltableelts::datetimetype_constructor_exists():
    assert callable(WordprocessingMLTableElts::DateTimeType.__init__)


def test_wordprocessingmltableelts::datetimetype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts::DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "hour" in params, "Missing parameter 'hour'"
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "second" in params, "Missing parameter 'second'"
    assert "day" in params, "Missing parameter 'day'"

def test_wordprocessingmltableelts::datetimetype_has_hour():
    assert hasattr(WordprocessingMLTableElts::DateTimeType, "hour")
    descriptor = None
    for klass in WordprocessingMLTableElts::DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::datetimetype_has_month():
    assert hasattr(WordprocessingMLTableElts::DateTimeType, "month")
    descriptor = None
    for klass in WordprocessingMLTableElts::DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::datetimetype_has_year():
    assert hasattr(WordprocessingMLTableElts::DateTimeType, "year")
    descriptor = None
    for klass in WordprocessingMLTableElts::DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::datetimetype_has_minute():
    assert hasattr(WordprocessingMLTableElts::DateTimeType, "minute")
    descriptor = None
    for klass in WordprocessingMLTableElts::DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::datetimetype_has_second():
    assert hasattr(WordprocessingMLTableElts::DateTimeType, "second")
    descriptor = None
    for klass in WordprocessingMLTableElts::DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts::datetimetype_has_day():
    assert hasattr(WordprocessingMLTableElts::DateTimeType, "day")
    descriptor = None
    for klass in WordprocessingMLTableElts::DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_fldchartypeproperty_exists():
    # Check that the Enumeration exists
    assert FldCharTypeProperty is not None

def test_fldchartypeproperty_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in FldCharTypeProperty]
    expected_literals = [
        "fctp_begin",
        "fctp_separate",
        "fctp_end",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in FldCharTypeProperty"

def test_onofftype_exists():
    # Check that the Enumeration exists
    assert OnOffType is not None

def test_onofftype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in OnOffType]
    expected_literals = [
        "oot_on",
        "oot_off",
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
        "ftn_normal",
        "ftn_separator",
        "ftn_continuation_separator",
        "ftn_continuation_notice",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NoteValue"

def test_breaktype_exists():
    # Check that the Enumeration exists
    assert BreakType is not None

def test_breaktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BreakType]
    expected_literals = [
        "bt_page",
        "bt_text_wrapping",
        "bt_column",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BreakType"


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
WordprocessingMLTableElts::TabElt_strategy = st.builds(
    WordprocessingMLTableElts::TabElt,
)
WordprocessingMLTableElts::PictureType_strategy = st.builds(
    WordprocessingMLTableElts::PictureType,
)
WordprocessingMLTableElts::SectPrElt_strategy = st.builds(
    WordprocessingMLTableElts::SectPrElt,
)
WordprocessingMLTableElts::ListsElt_strategy = st.builds(
    WordprocessingMLTableElts::ListsElt,
)
WordprocessingMLTableElts::FontsListElt_strategy = st.builds(
    WordprocessingMLTableElts::FontsListElt,
)
WordprocessingMLTableElts::TableCellPrElt_strategy = st.builds(
    WordprocessingMLTableElts::TableCellPrElt,
)
WordprocessingMLTableElts::StylesElt_strategy = st.builds(
    WordprocessingMLTableElts::StylesElt,
)
WordprocessingMLTableElts::TableCellElt_strategy = st.builds(
    WordprocessingMLTableElts::TableCellElt,
)
WordprocessingMLTableElts::RowContentElt_strategy = st.builds(
    WordprocessingMLTableElts::RowContentElt,
)
TableCellPrElt_strategy = st.builds(
    TableCellPrElt,
)
RowContentElt_strategy = st.builds(
    RowContentElt,
)
TableRowPrElt_strategy = st.builds(
    TableRowPrElt,
)
TablePrExElt_strategy = st.builds(
    TablePrExElt,
)
WordprocessingMLTableElts::RowElt_strategy = st.builds(
    WordprocessingMLTableElts::RowElt,
)
WordprocessingMLTableElts::TableRowPrElt_strategy = st.builds(
    WordprocessingMLTableElts::TableRowPrElt,
)
WordprocessingMLTableElts::TablePrExElt_strategy = st.builds(
    WordprocessingMLTableElts::TablePrExElt,
)
RowElt_strategy = st.builds(
    RowElt,
)
WordprocessingMLTableElts::TableContentElt_strategy = st.builds(
    WordprocessingMLTableElts::TableContentElt,
)
WordprocessingMLTableElts::TableGridElt_strategy = st.builds(
    WordprocessingMLTableElts::TableGridElt,
)
TableElt_strategy = st.builds(
    TableElt,
)
RunLevelElt_strategy = st.builds(
    RunLevelElt,
)
TableGridElt_strategy = st.builds(
    TableGridElt,
)
TablePrElt_strategy = st.builds(
    TablePrElt,
)
WordprocessingMLTableElts::TablePrElt_strategy = st.builds(
    WordprocessingMLTableElts::TablePrElt,
)
TableContentElt_strategy = st.builds(
    TableContentElt,
)
WordprocessingMLTableElts::FldCharElt_strategy = st.builds(
    WordprocessingMLTableElts::FldCharElt,
    fldCharType=
        st.none(),
    fldLock=
        st.none()
)
FldCharElt_strategy = st.builds(
    FldCharElt,
)
TabElt_strategy = st.builds(
    TabElt,
)
WordprocessingMLTableElts::SymElt_strategy = st.builds(
    WordprocessingMLTableElts::SymElt,
)
WordprocessingMLTableElts::NoteElt_strategy = st.builds(
    WordprocessingMLTableElts::NoteElt,
    suppressRef=
        st.none(),
    type=
        st.none()
)
SymElt_strategy = st.builds(
    SymElt,
)
PictureType_strategy = st.builds(
    PictureType,
)
RunElt_strategy = st.builds(
    RunElt,
)
WordprocessingMLTableElts::RunPrElt_strategy = st.builds(
    WordprocessingMLTableElts::RunPrElt,
)
RunContentElt_strategy = st.builds(
    RunContentElt,
)
WordprocessingMLTableElts::AnnotationRef_strategy = st.builds(
    WordprocessingMLTableElts::AnnotationRef,
)
WordprocessingMLTableElts::BreakElt_strategy = st.builds(
    WordprocessingMLTableElts::BreakElt,
    type=
        st.none()
)
WordprocessingMLTableElts::FootnoteRef_strategy = st.builds(
    WordprocessingMLTableElts::FootnoteRef,
)
WordprocessingMLTableElts::PgNum_strategy = st.builds(
    WordprocessingMLTableElts::PgNum,
)
WordprocessingMLTableElts::ContinuationSeparator_strategy = st.builds(
    WordprocessingMLTableElts::ContinuationSeparator,
)
WordprocessingMLTableElts::FldChar_strategy = st.builds(
    WordprocessingMLTableElts::FldChar,
)
WordprocessingMLTableElts::NoBreakHyphen_strategy = st.builds(
    WordprocessingMLTableElts::NoBreakHyphen,
)
WordprocessingMLTableElts::Picture_strategy = st.builds(
    WordprocessingMLTableElts::Picture,
)
WordprocessingMLTableElts::Separator_strategy = st.builds(
    WordprocessingMLTableElts::Separator,
)
WordprocessingMLTableElts::Tab_strategy = st.builds(
    WordprocessingMLTableElts::Tab,
)
WordprocessingMLTableElts::EndnoteRef_strategy = st.builds(
    WordprocessingMLTableElts::EndnoteRef,
)
WordprocessingMLTableElts::SoftHyphen_strategy = st.builds(
    WordprocessingMLTableElts::SoftHyphen,
)
WordprocessingMLTableElts::Cr_strategy = st.builds(
    WordprocessingMLTableElts::Cr,
)
WordprocessingMLTableElts::Symbol_strategy = st.builds(
    WordprocessingMLTableElts::Symbol,
)
RunPrElt_strategy = st.builds(
    RunPrElt,
)
WordprocessingMLTableElts::ParaContentElt_strategy = st.builds(
    WordprocessingMLTableElts::ParaContentElt,
)
WordprocessingMLTableElts::RunContentElt_strategy = st.builds(
    WordprocessingMLTableElts::RunContentElt,
)
ParaContentElt_strategy = st.builds(
    ParaContentElt,
)
WordprocessingMLTableElts::HLinkElt_strategy = st.builds(
    WordprocessingMLTableElts::HLinkElt,
)
WordprocessingMLTableElts::SubDocElt_strategy = st.builds(
    WordprocessingMLTableElts::SubDocElt,
)
WordprocessingMLTableElts::RunElt_strategy = st.builds(
    WordprocessingMLTableElts::RunElt,
)
WordprocessingMLTableElts::SimpleFieldElt_strategy = st.builds(
    WordprocessingMLTableElts::SimpleFieldElt,
)
ParaPrElt_strategy = st.builds(
    ParaPrElt,
)
BlockLevelChunkElt_strategy = st.builds(
    BlockLevelChunkElt,
)
WordprocessingMLTableElts::TableElt_strategy = st.builds(
    WordprocessingMLTableElts::TableElt,
)
WordprocessingMLTableElts::RunLevelElt_strategy = st.builds(
    WordprocessingMLTableElts::RunLevelElt,
)
WordprocessingMLTableElts::ParaElt_strategy = st.builds(
    WordprocessingMLTableElts::ParaElt,
)
TableCellElt_strategy = st.builds(
    TableCellElt,
)
NoteElt_strategy = st.builds(
    NoteElt,
)
WordprocessingMLTableElts::Endnote_strategy = st.builds(
    WordprocessingMLTableElts::Endnote,
)
WordprocessingMLTableElts::Footnote_strategy = st.builds(
    WordprocessingMLTableElts::Footnote,
)
ParaElt_strategy = st.builds(
    ParaElt,
)
WordprocessingMLTableElts::ParaPrElt_strategy = st.builds(
    WordprocessingMLTableElts::ParaPrElt,
)
BlockLevelElt_strategy = st.builds(
    BlockLevelElt,
)
WordprocessingMLTableElts::BlockLevelChunkElt_strategy = st.builds(
    WordprocessingMLTableElts::BlockLevelChunkElt,
)
WordprocessingMLTableElts::CfChunk_strategy = st.builds(
    WordprocessingMLTableElts::CfChunk,
)
WordprocessingMLTableElts::BodyElt_strategy = st.builds(
    WordprocessingMLTableElts::BodyElt,
)
WordprocessingMLTableElts::DocPrElt_strategy = st.builds(
    WordprocessingMLTableElts::DocPrElt,
)
BodyElt_strategy = st.builds(
    BodyElt,
)
WordprocessingMLTableElts::BlockLevelElt_strategy = st.builds(
    WordprocessingMLTableElts::BlockLevelElt,
)
SectPrElt_strategy = st.builds(
    SectPrElt,
)
StylesElt_strategy = st.builds(
    StylesElt,
)
ListsElt_strategy = st.builds(
    ListsElt,
)
FontsListElt_strategy = st.builds(
    FontsListElt,
)
DocPrElt_strategy = st.builds(
    DocPrElt,
)
DocumentPropertiesCollection_strategy = st.builds(
    DocumentPropertiesCollection,
)
WordprocessingMLTableElts::WordDocument_strategy = st.builds(
    WordprocessingMLTableElts::WordDocument,
)
StringProperty_strategy = st.builds(
    StringProperty,
)
WordprocessingMLTableElts::StringType_strategy = st.builds(
    WordprocessingMLTableElts::StringType,
    val=
        st.none()
)
StringType_strategy = st.builds(
    StringType,
)
WordprocessingMLTableElts::InstrText_strategy = st.builds(
    WordprocessingMLTableElts::InstrText,
)
WordprocessingMLTableElts::Text_strategy = st.builds(
    WordprocessingMLTableElts::Text,
)
WordprocessingMLTableElts::DelText_strategy = st.builds(
    WordprocessingMLTableElts::DelText,
)
WordprocessingMLTableElts::DelInstrText_strategy = st.builds(
    WordprocessingMLTableElts::DelInstrText,
)
WordprocessingMLTableElts::StringProperty_strategy = st.builds(
    WordprocessingMLTableElts::StringProperty,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
WordprocessingMLTableElts::SmartTagsCollection_strategy = st.builds(
    WordprocessingMLTableElts::SmartTagsCollection,
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
WordprocessingMLTableElts::CustomDocumentProperty_strategy = st.builds(
    WordprocessingMLTableElts::CustomDocumentProperty,
    name=
        st.none()
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
WordprocessingMLTableElts::SmartTagType_strategy = st.builds(
    WordprocessingMLTableElts::SmartTagType,
    namespaceuri=
        st.none(),
    name=
        st.none(),
    url=
        st.none()
)
WordprocessingMLTableElts::CustomDocumentPropertiesCollection_strategy = st.builds(
    WordprocessingMLTableElts::CustomDocumentPropertiesCollection,
)
VersionType_strategy = st.builds(
    VersionType,
)
WordDocument_strategy = st.builds(
    WordDocument,
)
WordprocessingMLTableElts::DocumentPropertiesCollection_strategy = st.builds(
    WordprocessingMLTableElts::DocumentPropertiesCollection,
    bytes=
        st.none(),
    manager=
        st.none(),
    lastAuthor=
        st.none(),
    lines=
        st.none(),
    presentationFormat=
        st.none(),
    hyperlinkBase=
        st.none(),
    description=
        st.none(),
    characters=
        st.none(),
    paragraphs=
        st.none(),
    category=
        st.none(),
    appName=
        st.none(),
    pages=
        st.none(),
    words=
        st.none(),
    charactersWithSpaces=
        st.none(),
    guid=
        st.none(),
    subject=
        st.none(),
    keywords=
        st.none(),
    author=
        st.none(),
    title=
        st.none(),
    revision=
        st.none(),
    totalTime=
        st.none(),
    company=
        st.none()
)
ValueType_strategy = st.builds(
    ValueType,
)
WordprocessingMLTableElts::FloatValue_strategy = st.builds(
    WordprocessingMLTableElts::FloatValue,
    value=
        st.none()
)
WordprocessingMLTableElts::BooleanValue_strategy = st.builds(
    WordprocessingMLTableElts::BooleanValue,
    value=
        st.none()
)
WordprocessingMLTableElts::StringValue_strategy = st.builds(
    WordprocessingMLTableElts::StringValue,
    value=
        st.none()
)
WordprocessingMLTableElts::ValueType_strategy = st.builds(
    WordprocessingMLTableElts::ValueType,
)
WordprocessingMLTableElts::VersionType_strategy = st.builds(
    WordprocessingMLTableElts::VersionType,
    nn=
        st.none(),
    n=
        st.none()
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
WordprocessingMLTableElts::DateTimeTypeValue_strategy = st.builds(
    WordprocessingMLTableElts::DateTimeTypeValue,
)
WordprocessingMLTableElts::DateTimeType_strategy = st.builds(
    WordprocessingMLTableElts::DateTimeType,
    hour=
        st.none(),
    month=
        st.none(),
    year=
        st.none(),
    minute=
        st.none(),
    second=
        st.none(),
    day=
        st.none()
)

@given(instance=WordprocessingMLTableElts::TabElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tabelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TabElt)

@given(instance=WordprocessingMLTableElts::PictureType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::picturetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::PictureType)

@given(instance=WordprocessingMLTableElts::SectPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::sectprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::SectPrElt)

@given(instance=WordprocessingMLTableElts::ListsElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::listselt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::ListsElt)

@given(instance=WordprocessingMLTableElts::FontsListElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::fontslistelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::FontsListElt)

@given(instance=WordprocessingMLTableElts::TableCellPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tablecellprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TableCellPrElt)

@given(instance=WordprocessingMLTableElts::StylesElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::styleselt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::StylesElt)

@given(instance=WordprocessingMLTableElts::TableCellElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tablecellelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TableCellElt)

@given(instance=WordprocessingMLTableElts::RowContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::rowcontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::RowContentElt)

@given(instance=TableCellPrElt_strategy)
@settings(max_examples=50)
def test_tablecellprelt_instantiation(instance):
    assert isinstance(instance, TableCellPrElt)

@given(instance=RowContentElt_strategy)
@settings(max_examples=50)
def test_rowcontentelt_instantiation(instance):
    assert isinstance(instance, RowContentElt)

@given(instance=TableRowPrElt_strategy)
@settings(max_examples=50)
def test_tablerowprelt_instantiation(instance):
    assert isinstance(instance, TableRowPrElt)

@given(instance=TablePrExElt_strategy)
@settings(max_examples=50)
def test_tableprexelt_instantiation(instance):
    assert isinstance(instance, TablePrExElt)

@given(instance=WordprocessingMLTableElts::RowElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::rowelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::RowElt)

@given(instance=WordprocessingMLTableElts::TableRowPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tablerowprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TableRowPrElt)

@given(instance=WordprocessingMLTableElts::TablePrExElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tableprexelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TablePrExElt)

@given(instance=RowElt_strategy)
@settings(max_examples=50)
def test_rowelt_instantiation(instance):
    assert isinstance(instance, RowElt)

@given(instance=WordprocessingMLTableElts::TableContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tablecontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TableContentElt)

@given(instance=WordprocessingMLTableElts::TableGridElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tablegridelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TableGridElt)

@given(instance=TableElt_strategy)
@settings(max_examples=50)
def test_tableelt_instantiation(instance):
    assert isinstance(instance, TableElt)

@given(instance=RunLevelElt_strategy)
@settings(max_examples=50)
def test_runlevelelt_instantiation(instance):
    assert isinstance(instance, RunLevelElt)

@given(instance=TableGridElt_strategy)
@settings(max_examples=50)
def test_tablegridelt_instantiation(instance):
    assert isinstance(instance, TableGridElt)

@given(instance=TablePrElt_strategy)
@settings(max_examples=50)
def test_tableprelt_instantiation(instance):
    assert isinstance(instance, TablePrElt)

@given(instance=WordprocessingMLTableElts::TablePrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tableprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TablePrElt)

@given(instance=TableContentElt_strategy)
@settings(max_examples=50)
def test_tablecontentelt_instantiation(instance):
    assert isinstance(instance, TableContentElt)

@given(instance=WordprocessingMLTableElts::FldCharElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::fldcharelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::FldCharElt)

@given(instance=WordprocessingMLTableElts::FldCharElt_strategy)
def test_wordprocessingmltableelts::fldcharelt_fldCharType_type(instance):
    assert isinstance(instance.fldCharType, stringtype)


@given(instance=WordprocessingMLTableElts::FldCharElt_strategy)
def test_wordprocessingmltableelts::fldcharelt_fldCharType_setter(instance):
    original = instance.fldCharType
    instance.fldCharType = original
    assert instance.fldCharType == original

@given(instance=WordprocessingMLTableElts::FldCharElt_strategy)
def test_wordprocessingmltableelts::fldcharelt_fldLock_type(instance):
    assert isinstance(instance.fldLock, stringtype)


@given(instance=WordprocessingMLTableElts::FldCharElt_strategy)
def test_wordprocessingmltableelts::fldcharelt_fldLock_setter(instance):
    original = instance.fldLock
    instance.fldLock = original
    assert instance.fldLock == original

@given(instance=FldCharElt_strategy)
@settings(max_examples=50)
def test_fldcharelt_instantiation(instance):
    assert isinstance(instance, FldCharElt)

@given(instance=TabElt_strategy)
@settings(max_examples=50)
def test_tabelt_instantiation(instance):
    assert isinstance(instance, TabElt)

@given(instance=WordprocessingMLTableElts::SymElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::symelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::SymElt)

@given(instance=WordprocessingMLTableElts::NoteElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::noteelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::NoteElt)

@given(instance=WordprocessingMLTableElts::NoteElt_strategy)
def test_wordprocessingmltableelts::noteelt_suppressRef_type(instance):
    assert isinstance(instance.suppressRef, stringtype)


@given(instance=WordprocessingMLTableElts::NoteElt_strategy)
def test_wordprocessingmltableelts::noteelt_suppressRef_setter(instance):
    original = instance.suppressRef
    instance.suppressRef = original
    assert instance.suppressRef == original

@given(instance=WordprocessingMLTableElts::NoteElt_strategy)
def test_wordprocessingmltableelts::noteelt_type_type(instance):
    assert isinstance(instance.type, stringtype)


@given(instance=WordprocessingMLTableElts::NoteElt_strategy)
def test_wordprocessingmltableelts::noteelt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=SymElt_strategy)
@settings(max_examples=50)
def test_symelt_instantiation(instance):
    assert isinstance(instance, SymElt)

@given(instance=PictureType_strategy)
@settings(max_examples=50)
def test_picturetype_instantiation(instance):
    assert isinstance(instance, PictureType)

@given(instance=RunElt_strategy)
@settings(max_examples=50)
def test_runelt_instantiation(instance):
    assert isinstance(instance, RunElt)

@given(instance=WordprocessingMLTableElts::RunPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::runprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::RunPrElt)

@given(instance=RunContentElt_strategy)
@settings(max_examples=50)
def test_runcontentelt_instantiation(instance):
    assert isinstance(instance, RunContentElt)

@given(instance=WordprocessingMLTableElts::AnnotationRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::annotationref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::AnnotationRef)

@given(instance=WordprocessingMLTableElts::BreakElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::breakelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::BreakElt)

@given(instance=WordprocessingMLTableElts::BreakElt_strategy)
def test_wordprocessingmltableelts::breakelt_type_type(instance):
    assert isinstance(instance.type, stringtype)


@given(instance=WordprocessingMLTableElts::BreakElt_strategy)
def test_wordprocessingmltableelts::breakelt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=WordprocessingMLTableElts::FootnoteRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::footnoteref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::FootnoteRef)

@given(instance=WordprocessingMLTableElts::PgNum_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::pgnum_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::PgNum)

@given(instance=WordprocessingMLTableElts::ContinuationSeparator_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::continuationseparator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::ContinuationSeparator)

@given(instance=WordprocessingMLTableElts::FldChar_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::fldchar_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::FldChar)

@given(instance=WordprocessingMLTableElts::NoBreakHyphen_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::nobreakhyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::NoBreakHyphen)

@given(instance=WordprocessingMLTableElts::Picture_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::picture_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::Picture)

@given(instance=WordprocessingMLTableElts::Separator_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::separator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::Separator)

@given(instance=WordprocessingMLTableElts::Tab_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tab_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::Tab)

@given(instance=WordprocessingMLTableElts::EndnoteRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::endnoteref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::EndnoteRef)

@given(instance=WordprocessingMLTableElts::SoftHyphen_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::softhyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::SoftHyphen)

@given(instance=WordprocessingMLTableElts::Cr_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::cr_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::Cr)

@given(instance=WordprocessingMLTableElts::Symbol_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::symbol_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::Symbol)

@given(instance=RunPrElt_strategy)
@settings(max_examples=50)
def test_runprelt_instantiation(instance):
    assert isinstance(instance, RunPrElt)

@given(instance=WordprocessingMLTableElts::ParaContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::paracontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::ParaContentElt)

@given(instance=WordprocessingMLTableElts::RunContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::runcontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::RunContentElt)

@given(instance=ParaContentElt_strategy)
@settings(max_examples=50)
def test_paracontentelt_instantiation(instance):
    assert isinstance(instance, ParaContentElt)

@given(instance=WordprocessingMLTableElts::HLinkElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::hlinkelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::HLinkElt)

@given(instance=WordprocessingMLTableElts::SubDocElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::subdocelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::SubDocElt)

@given(instance=WordprocessingMLTableElts::RunElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::runelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::RunElt)

@given(instance=WordprocessingMLTableElts::SimpleFieldElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::simplefieldelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::SimpleFieldElt)

@given(instance=ParaPrElt_strategy)
@settings(max_examples=50)
def test_paraprelt_instantiation(instance):
    assert isinstance(instance, ParaPrElt)

@given(instance=BlockLevelChunkElt_strategy)
@settings(max_examples=50)
def test_blocklevelchunkelt_instantiation(instance):
    assert isinstance(instance, BlockLevelChunkElt)

@given(instance=WordprocessingMLTableElts::TableElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::tableelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::TableElt)

@given(instance=WordprocessingMLTableElts::RunLevelElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::runlevelelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::RunLevelElt)

@given(instance=WordprocessingMLTableElts::ParaElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::paraelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::ParaElt)

@given(instance=TableCellElt_strategy)
@settings(max_examples=50)
def test_tablecellelt_instantiation(instance):
    assert isinstance(instance, TableCellElt)

@given(instance=NoteElt_strategy)
@settings(max_examples=50)
def test_noteelt_instantiation(instance):
    assert isinstance(instance, NoteElt)

@given(instance=WordprocessingMLTableElts::Endnote_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::endnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::Endnote)

@given(instance=WordprocessingMLTableElts::Footnote_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::footnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::Footnote)

@given(instance=ParaElt_strategy)
@settings(max_examples=50)
def test_paraelt_instantiation(instance):
    assert isinstance(instance, ParaElt)

@given(instance=WordprocessingMLTableElts::ParaPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::paraprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::ParaPrElt)

@given(instance=BlockLevelElt_strategy)
@settings(max_examples=50)
def test_blocklevelelt_instantiation(instance):
    assert isinstance(instance, BlockLevelElt)

@given(instance=WordprocessingMLTableElts::BlockLevelChunkElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::blocklevelchunkelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::BlockLevelChunkElt)

@given(instance=WordprocessingMLTableElts::CfChunk_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::cfchunk_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::CfChunk)

@given(instance=WordprocessingMLTableElts::BodyElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::bodyelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::BodyElt)

@given(instance=WordprocessingMLTableElts::DocPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::docprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::DocPrElt)

@given(instance=BodyElt_strategy)
@settings(max_examples=50)
def test_bodyelt_instantiation(instance):
    assert isinstance(instance, BodyElt)

@given(instance=WordprocessingMLTableElts::BlockLevelElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::blocklevelelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::BlockLevelElt)

@given(instance=SectPrElt_strategy)
@settings(max_examples=50)
def test_sectprelt_instantiation(instance):
    assert isinstance(instance, SectPrElt)

@given(instance=StylesElt_strategy)
@settings(max_examples=50)
def test_styleselt_instantiation(instance):
    assert isinstance(instance, StylesElt)

@given(instance=ListsElt_strategy)
@settings(max_examples=50)
def test_listselt_instantiation(instance):
    assert isinstance(instance, ListsElt)

@given(instance=FontsListElt_strategy)
@settings(max_examples=50)
def test_fontslistelt_instantiation(instance):
    assert isinstance(instance, FontsListElt)

@given(instance=DocPrElt_strategy)
@settings(max_examples=50)
def test_docprelt_instantiation(instance):
    assert isinstance(instance, DocPrElt)

@given(instance=DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, DocumentPropertiesCollection)

@given(instance=WordprocessingMLTableElts::WordDocument_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::worddocument_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::WordDocument)

@given(instance=StringProperty_strategy)
@settings(max_examples=50)
def test_stringproperty_instantiation(instance):
    assert isinstance(instance, StringProperty)

@given(instance=WordprocessingMLTableElts::StringType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::stringtype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::StringType)

@given(instance=WordprocessingMLTableElts::StringType_strategy)
def test_wordprocessingmltableelts::stringtype_val_type(instance):
    assert isinstance(instance.val, stringtype)


@given(instance=WordprocessingMLTableElts::StringType_strategy)
def test_wordprocessingmltableelts::stringtype_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=StringType_strategy)
@settings(max_examples=50)
def test_stringtype_instantiation(instance):
    assert isinstance(instance, StringType)

@given(instance=WordprocessingMLTableElts::InstrText_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::instrtext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::InstrText)

@given(instance=WordprocessingMLTableElts::Text_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::text_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::Text)

@given(instance=WordprocessingMLTableElts::DelText_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::deltext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::DelText)

@given(instance=WordprocessingMLTableElts::DelInstrText_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::delinstrtext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::DelInstrText)

@given(instance=WordprocessingMLTableElts::StringProperty_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::stringproperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::StringProperty)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=WordprocessingMLTableElts::SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::smarttagscollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::SmartTagsCollection)

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=WordprocessingMLTableElts::CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::customdocumentproperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::CustomDocumentProperty)

@given(instance=WordprocessingMLTableElts::CustomDocumentProperty_strategy)
def test_wordprocessingmltableelts::customdocumentproperty_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=WordprocessingMLTableElts::CustomDocumentProperty_strategy)
def test_wordprocessingmltableelts::customdocumentproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, CustomDocumentProperty)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=WordprocessingMLTableElts::SmartTagType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::smarttagtype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::SmartTagType)

@given(instance=WordprocessingMLTableElts::SmartTagType_strategy)
def test_wordprocessingmltableelts::smarttagtype_namespaceuri_type(instance):
    assert isinstance(instance.namespaceuri, stringtype)


@given(instance=WordprocessingMLTableElts::SmartTagType_strategy)
def test_wordprocessingmltableelts::smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original

@given(instance=WordprocessingMLTableElts::SmartTagType_strategy)
def test_wordprocessingmltableelts::smarttagtype_name_type(instance):
    assert isinstance(instance.name, stringtype)


@given(instance=WordprocessingMLTableElts::SmartTagType_strategy)
def test_wordprocessingmltableelts::smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=WordprocessingMLTableElts::SmartTagType_strategy)
def test_wordprocessingmltableelts::smarttagtype_url_type(instance):
    assert isinstance(instance.url, stringtype)


@given(instance=WordprocessingMLTableElts::SmartTagType_strategy)
def test_wordprocessingmltableelts::smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=WordprocessingMLTableElts::CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::CustomDocumentPropertiesCollection)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=WordDocument_strategy)
@settings(max_examples=50)
def test_worddocument_instantiation(instance):
    assert isinstance(instance, WordDocument)

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::DocumentPropertiesCollection)

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_bytes_type(instance):
    assert isinstance(instance.bytes, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_manager_type(instance):
    assert isinstance(instance.manager, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_lastAuthor_type(instance):
    assert isinstance(instance.lastAuthor, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_lines_type(instance):
    assert isinstance(instance.lines, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_presentationFormat_type(instance):
    assert isinstance(instance.presentationFormat, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_hyperlinkBase_type(instance):
    assert isinstance(instance.hyperlinkBase, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_description_type(instance):
    assert isinstance(instance.description, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_characters_type(instance):
    assert isinstance(instance.characters, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_paragraphs_type(instance):
    assert isinstance(instance.paragraphs, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_category_type(instance):
    assert isinstance(instance.category, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_appName_type(instance):
    assert isinstance(instance.appName, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_pages_type(instance):
    assert isinstance(instance.pages, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_words_type(instance):
    assert isinstance(instance.words, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_charactersWithSpaces_type(instance):
    assert isinstance(instance.charactersWithSpaces, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_guid_type(instance):
    assert isinstance(instance.guid, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_subject_type(instance):
    assert isinstance(instance.subject, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_keywords_type(instance):
    assert isinstance(instance.keywords, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_author_type(instance):
    assert isinstance(instance.author, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_title_type(instance):
    assert isinstance(instance.title, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_revision_type(instance):
    assert isinstance(instance.revision, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_totalTime_type(instance):
    assert isinstance(instance.totalTime, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original

@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_company_type(instance):
    assert isinstance(instance.company, stringtype)


@given(instance=WordprocessingMLTableElts::DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts::documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=WordprocessingMLTableElts::FloatValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::floatvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::FloatValue)

@given(instance=WordprocessingMLTableElts::FloatValue_strategy)
def test_wordprocessingmltableelts::floatvalue_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=WordprocessingMLTableElts::FloatValue_strategy)
def test_wordprocessingmltableelts::floatvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLTableElts::BooleanValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::booleanvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::BooleanValue)

@given(instance=WordprocessingMLTableElts::BooleanValue_strategy)
def test_wordprocessingmltableelts::booleanvalue_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=WordprocessingMLTableElts::BooleanValue_strategy)
def test_wordprocessingmltableelts::booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLTableElts::StringValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::stringvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::StringValue)

@given(instance=WordprocessingMLTableElts::StringValue_strategy)
def test_wordprocessingmltableelts::stringvalue_value_type(instance):
    assert isinstance(instance.value, stringtype)


@given(instance=WordprocessingMLTableElts::StringValue_strategy)
def test_wordprocessingmltableelts::stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLTableElts::ValueType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::valuetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::ValueType)

@given(instance=WordprocessingMLTableElts::VersionType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::versiontype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::VersionType)

@given(instance=WordprocessingMLTableElts::VersionType_strategy)
def test_wordprocessingmltableelts::versiontype_nn_type(instance):
    assert isinstance(instance.nn, stringtype)


@given(instance=WordprocessingMLTableElts::VersionType_strategy)
def test_wordprocessingmltableelts::versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original

@given(instance=WordprocessingMLTableElts::VersionType_strategy)
def test_wordprocessingmltableelts::versiontype_n_type(instance):
    assert isinstance(instance.n, stringtype)


@given(instance=WordprocessingMLTableElts::VersionType_strategy)
def test_wordprocessingmltableelts::versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=WordprocessingMLTableElts::DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::datetimetypevalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::DateTimeTypeValue)

@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts::datetimetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts::DateTimeType)

@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_hour_type(instance):
    assert isinstance(instance.hour, stringtype)


@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original

@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_month_type(instance):
    assert isinstance(instance.month, stringtype)


@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_year_type(instance):
    assert isinstance(instance.year, stringtype)


@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_minute_type(instance):
    assert isinstance(instance.minute, stringtype)


@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original

@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_second_type(instance):
    assert isinstance(instance.second, stringtype)


@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_day_type(instance):
    assert isinstance(instance.day, stringtype)


@given(instance=WordprocessingMLTableElts::DateTimeType_strategy)
def test_wordprocessingmltableelts::datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original
