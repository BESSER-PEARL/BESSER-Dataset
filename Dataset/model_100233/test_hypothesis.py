import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    WordprocessingMLBasicDef_TabElt,
    WordprocessingMLBasicDef_PictureType,
    TabElt,
    WordprocessingMLBasicDef_StylesElt,
    WordprocessingMLBasicDef_ListsElt,
    WordprocessingMLBasicDef_FontsListElt,
    WordprocessingMLBasicDef_FldCharElt,
    FldCharElt,
    WordprocessingMLBasicDef_SectPrElt,
    WordprocessingMLBasicDef_NoteElt,
    WordprocessingMLBasicDef_SymElt,
    SymElt,
    PictureType,
    RunContentElt,
    WordprocessingMLBasicDef_Picture,
    WordprocessingMLBasicDef_NoBreakHyphen,
    WordprocessingMLBasicDef_Cr,
    WordprocessingMLBasicDef_FldChar,
    WordprocessingMLBasicDef_Tab,
    WordprocessingMLBasicDef_FootnoteRef,
    WordprocessingMLBasicDef_AnnotationRef,
    WordprocessingMLBasicDef_SoftHyphen,
    WordprocessingMLBasicDef_ContinuationSeparator,
    WordprocessingMLBasicDef_PgNum,
    WordprocessingMLBasicDef_EndnoteRef,
    WordprocessingMLBasicDef_Separator,
    WordprocessingMLBasicDef_Symbol,
    WordprocessingMLBasicDef_BreakElt,
    WordprocessingMLBasicDef_RunContentElt,
    RunElt,
    WordprocessingMLBasicDef_RunPrElt,
    ParaPrElt,
    BlockLevelChunkElt,
    WordprocessingMLBasicDef_RunLevelElt,
    WordprocessingMLBasicDef_ParaElt,
    RunPrElt,
    WordprocessingMLBasicDef_ParaContentElt,
    ParaElt,
    WordprocessingMLBasicDef_ParaPrElt,
    ParaContentElt,
    WordprocessingMLBasicDef_SubDocElt,
    WordprocessingMLBasicDef_HLinkElt,
    WordprocessingMLBasicDef_SimpleFieldElt,
    WordprocessingMLBasicDef_RunElt,
    WordprocessingMLBasicDef_BodyElt,
    NoteElt,
    WordprocessingMLBasicDef_Endnote,
    WordprocessingMLBasicDef_Footnote,
    WordprocessingMLBasicDef_BlockLevelElt,
    SectPrElt,
    BlockLevelElt,
    WordprocessingMLBasicDef_CfChunk,
    WordprocessingMLBasicDef_BlockLevelChunkElt,
    FontsListElt,
    WordprocessingMLBasicDef_DocPrElt,
    StringProperty,
    BodyElt,
    DocPrElt,
    StylesElt,
    ListsElt,
    DocumentPropertiesCollection,
    WordprocessingMLBasicDef_WordDocument,
    SmartTagType,
    WordprocessingMLBasicDef_StringType,
    StringType,
    WordprocessingMLBasicDef_DelText,
    WordprocessingMLBasicDef_Text,
    WordprocessingMLBasicDef_InstrText,
    WordprocessingMLBasicDef_DelInstrText,
    WordprocessingMLBasicDef_StringProperty,
    SmartTagsCollection,
    WordprocessingMLBasicDef_SmartTagType,
    CustomDocumentPropertiesCollection,
    WordprocessingMLBasicDef_SmartTagsCollection,
    WordprocessingMLBasicDef_CustomDocumentPropertiesCollection,
    WordprocessingMLBasicDef_CustomDocumentProperty,
    CustomDocumentProperty,
    VersionType,
    DateTimeType,
    ValueType,
    WordprocessingMLBasicDef_BooleanValue,
    WordprocessingMLBasicDef_FloatValue,
    WordprocessingMLBasicDef_DateTimeTypeValue,
    WordprocessingMLBasicDef_StringValue,
    WordprocessingMLBasicDef_ValueType,
    WordDocument,
    WordprocessingMLBasicDef_DocumentPropertiesCollection,
    WordprocessingMLBasicDef_DateTimeType,
    WordprocessingMLBasicDef_VersionType,
    FldCharTypeProperty,
    BreakType,
    NoteValue,
    OnOffType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_wordprocessingmlbasicdef_tabelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_TabElt)


def test_wordprocessingmlbasicdef_tabelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_TabElt.__init__)


def test_wordprocessingmlbasicdef_tabelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_TabElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_picturetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_PictureType)


def test_wordprocessingmlbasicdef_picturetype_constructor_exists():
    assert callable(WordprocessingMLBasicDef_PictureType.__init__)


def test_wordprocessingmlbasicdef_picturetype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_PictureType.__init__)
    params = list(sig.parameters.keys())



def test_tabelt_is_not_abstract():
    assert not inspect.isabstract(TabElt)


def test_tabelt_constructor_exists():
    assert callable(TabElt.__init__)


def test_tabelt_constructor_args():
    sig = inspect.signature(TabElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_styleselt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_StylesElt)


def test_wordprocessingmlbasicdef_styleselt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_StylesElt.__init__)


def test_wordprocessingmlbasicdef_styleselt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_StylesElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_listselt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_ListsElt)


def test_wordprocessingmlbasicdef_listselt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_ListsElt.__init__)


def test_wordprocessingmlbasicdef_listselt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_ListsElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_fontslistelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_FontsListElt)


def test_wordprocessingmlbasicdef_fontslistelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_FontsListElt.__init__)


def test_wordprocessingmlbasicdef_fontslistelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_FontsListElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_fldcharelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_FldCharElt)


def test_wordprocessingmlbasicdef_fldcharelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_FldCharElt.__init__)


def test_wordprocessingmlbasicdef_fldcharelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_FldCharElt.__init__)
    params = list(sig.parameters.keys())
    assert "fldLock" in params, "Missing parameter 'fldLock'"
    assert "fldCharType" in params, "Missing parameter 'fldCharType'"

def test_wordprocessingmlbasicdef_fldcharelt_has_fldLock():
    assert hasattr(WordprocessingMLBasicDef_FldCharElt, "fldLock")
    descriptor = None
    for klass in WordprocessingMLBasicDef_FldCharElt.__mro__:
        if "fldLock" in klass.__dict__:
            descriptor = klass.__dict__["fldLock"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_fldcharelt_has_fldCharType():
    assert hasattr(WordprocessingMLBasicDef_FldCharElt, "fldCharType")
    descriptor = None
    for klass in WordprocessingMLBasicDef_FldCharElt.__mro__:
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



def test_wordprocessingmlbasicdef_sectprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_SectPrElt)


def test_wordprocessingmlbasicdef_sectprelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_SectPrElt.__init__)


def test_wordprocessingmlbasicdef_sectprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_SectPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_noteelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_NoteElt)


def test_wordprocessingmlbasicdef_noteelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_NoteElt.__init__)


def test_wordprocessingmlbasicdef_noteelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_NoteElt.__init__)
    params = list(sig.parameters.keys())
    assert "suppressRef" in params, "Missing parameter 'suppressRef'"
    assert "type" in params, "Missing parameter 'type'"

def test_wordprocessingmlbasicdef_noteelt_has_suppressRef():
    assert hasattr(WordprocessingMLBasicDef_NoteElt, "suppressRef")
    descriptor = None
    for klass in WordprocessingMLBasicDef_NoteElt.__mro__:
        if "suppressRef" in klass.__dict__:
            descriptor = klass.__dict__["suppressRef"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_noteelt_has_type():
    assert hasattr(WordprocessingMLBasicDef_NoteElt, "type")
    descriptor = None
    for klass in WordprocessingMLBasicDef_NoteElt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef_symelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_SymElt)


def test_wordprocessingmlbasicdef_symelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_SymElt.__init__)


def test_wordprocessingmlbasicdef_symelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_SymElt.__init__)
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



def test_wordprocessingmlbasicdef_picture_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_Picture)


def test_wordprocessingmlbasicdef_picture_constructor_exists():
    assert callable(WordprocessingMLBasicDef_Picture.__init__)


def test_wordprocessingmlbasicdef_picture_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_Picture.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_nobreakhyphen_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_NoBreakHyphen)


def test_wordprocessingmlbasicdef_nobreakhyphen_constructor_exists():
    assert callable(WordprocessingMLBasicDef_NoBreakHyphen.__init__)


def test_wordprocessingmlbasicdef_nobreakhyphen_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_NoBreakHyphen.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_cr_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_Cr)


def test_wordprocessingmlbasicdef_cr_constructor_exists():
    assert callable(WordprocessingMLBasicDef_Cr.__init__)


def test_wordprocessingmlbasicdef_cr_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_Cr.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_fldchar_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_FldChar)


def test_wordprocessingmlbasicdef_fldchar_constructor_exists():
    assert callable(WordprocessingMLBasicDef_FldChar.__init__)


def test_wordprocessingmlbasicdef_fldchar_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_FldChar.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_tab_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_Tab)


def test_wordprocessingmlbasicdef_tab_constructor_exists():
    assert callable(WordprocessingMLBasicDef_Tab.__init__)


def test_wordprocessingmlbasicdef_tab_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_Tab.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_footnoteref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_FootnoteRef)


def test_wordprocessingmlbasicdef_footnoteref_constructor_exists():
    assert callable(WordprocessingMLBasicDef_FootnoteRef.__init__)


def test_wordprocessingmlbasicdef_footnoteref_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_FootnoteRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_annotationref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_AnnotationRef)


def test_wordprocessingmlbasicdef_annotationref_constructor_exists():
    assert callable(WordprocessingMLBasicDef_AnnotationRef.__init__)


def test_wordprocessingmlbasicdef_annotationref_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_AnnotationRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_softhyphen_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_SoftHyphen)


def test_wordprocessingmlbasicdef_softhyphen_constructor_exists():
    assert callable(WordprocessingMLBasicDef_SoftHyphen.__init__)


def test_wordprocessingmlbasicdef_softhyphen_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_SoftHyphen.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_continuationseparator_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_ContinuationSeparator)


def test_wordprocessingmlbasicdef_continuationseparator_constructor_exists():
    assert callable(WordprocessingMLBasicDef_ContinuationSeparator.__init__)


def test_wordprocessingmlbasicdef_continuationseparator_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_ContinuationSeparator.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_pgnum_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_PgNum)


def test_wordprocessingmlbasicdef_pgnum_constructor_exists():
    assert callable(WordprocessingMLBasicDef_PgNum.__init__)


def test_wordprocessingmlbasicdef_pgnum_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_PgNum.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_endnoteref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_EndnoteRef)


def test_wordprocessingmlbasicdef_endnoteref_constructor_exists():
    assert callable(WordprocessingMLBasicDef_EndnoteRef.__init__)


def test_wordprocessingmlbasicdef_endnoteref_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_EndnoteRef.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_separator_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_Separator)


def test_wordprocessingmlbasicdef_separator_constructor_exists():
    assert callable(WordprocessingMLBasicDef_Separator.__init__)


def test_wordprocessingmlbasicdef_separator_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_Separator.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_symbol_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_Symbol)


def test_wordprocessingmlbasicdef_symbol_constructor_exists():
    assert callable(WordprocessingMLBasicDef_Symbol.__init__)


def test_wordprocessingmlbasicdef_symbol_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_breakelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_BreakElt)


def test_wordprocessingmlbasicdef_breakelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_BreakElt.__init__)


def test_wordprocessingmlbasicdef_breakelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_BreakElt.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_wordprocessingmlbasicdef_breakelt_has_type():
    assert hasattr(WordprocessingMLBasicDef_BreakElt, "type")
    descriptor = None
    for klass in WordprocessingMLBasicDef_BreakElt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef_runcontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_RunContentElt)


def test_wordprocessingmlbasicdef_runcontentelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_RunContentElt.__init__)


def test_wordprocessingmlbasicdef_runcontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_RunContentElt.__init__)
    params = list(sig.parameters.keys())



def test_runelt_is_not_abstract():
    assert not inspect.isabstract(RunElt)


def test_runelt_constructor_exists():
    assert callable(RunElt.__init__)


def test_runelt_constructor_args():
    sig = inspect.signature(RunElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_runprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_RunPrElt)


def test_wordprocessingmlbasicdef_runprelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_RunPrElt.__init__)


def test_wordprocessingmlbasicdef_runprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_RunPrElt.__init__)
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



def test_wordprocessingmlbasicdef_runlevelelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_RunLevelElt)


def test_wordprocessingmlbasicdef_runlevelelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_RunLevelElt.__init__)


def test_wordprocessingmlbasicdef_runlevelelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_RunLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_paraelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_ParaElt)


def test_wordprocessingmlbasicdef_paraelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_ParaElt.__init__)


def test_wordprocessingmlbasicdef_paraelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_ParaElt.__init__)
    params = list(sig.parameters.keys())



def test_runprelt_is_not_abstract():
    assert not inspect.isabstract(RunPrElt)


def test_runprelt_constructor_exists():
    assert callable(RunPrElt.__init__)


def test_runprelt_constructor_args():
    sig = inspect.signature(RunPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_paracontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_ParaContentElt)


def test_wordprocessingmlbasicdef_paracontentelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_ParaContentElt.__init__)


def test_wordprocessingmlbasicdef_paracontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_ParaContentElt.__init__)
    params = list(sig.parameters.keys())



def test_paraelt_is_not_abstract():
    assert not inspect.isabstract(ParaElt)


def test_paraelt_constructor_exists():
    assert callable(ParaElt.__init__)


def test_paraelt_constructor_args():
    sig = inspect.signature(ParaElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_paraprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_ParaPrElt)


def test_wordprocessingmlbasicdef_paraprelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_ParaPrElt.__init__)


def test_wordprocessingmlbasicdef_paraprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_ParaPrElt.__init__)
    params = list(sig.parameters.keys())



def test_paracontentelt_is_not_abstract():
    assert not inspect.isabstract(ParaContentElt)


def test_paracontentelt_constructor_exists():
    assert callable(ParaContentElt.__init__)


def test_paracontentelt_constructor_args():
    sig = inspect.signature(ParaContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_subdocelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_SubDocElt)


def test_wordprocessingmlbasicdef_subdocelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_SubDocElt.__init__)


def test_wordprocessingmlbasicdef_subdocelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_SubDocElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_hlinkelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_HLinkElt)


def test_wordprocessingmlbasicdef_hlinkelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_HLinkElt.__init__)


def test_wordprocessingmlbasicdef_hlinkelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_HLinkElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_simplefieldelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_SimpleFieldElt)


def test_wordprocessingmlbasicdef_simplefieldelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_SimpleFieldElt.__init__)


def test_wordprocessingmlbasicdef_simplefieldelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_SimpleFieldElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_runelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_RunElt)


def test_wordprocessingmlbasicdef_runelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_RunElt.__init__)


def test_wordprocessingmlbasicdef_runelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_RunElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_bodyelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_BodyElt)


def test_wordprocessingmlbasicdef_bodyelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_BodyElt.__init__)


def test_wordprocessingmlbasicdef_bodyelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_BodyElt.__init__)
    params = list(sig.parameters.keys())



def test_noteelt_is_not_abstract():
    assert not inspect.isabstract(NoteElt)


def test_noteelt_constructor_exists():
    assert callable(NoteElt.__init__)


def test_noteelt_constructor_args():
    sig = inspect.signature(NoteElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_endnote_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_Endnote)


def test_wordprocessingmlbasicdef_endnote_constructor_exists():
    assert callable(WordprocessingMLBasicDef_Endnote.__init__)


def test_wordprocessingmlbasicdef_endnote_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_Endnote.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_footnote_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_Footnote)


def test_wordprocessingmlbasicdef_footnote_constructor_exists():
    assert callable(WordprocessingMLBasicDef_Footnote.__init__)


def test_wordprocessingmlbasicdef_footnote_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_Footnote.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_blocklevelelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_BlockLevelElt)


def test_wordprocessingmlbasicdef_blocklevelelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_BlockLevelElt.__init__)


def test_wordprocessingmlbasicdef_blocklevelelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_BlockLevelElt.__init__)
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



def test_wordprocessingmlbasicdef_cfchunk_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_CfChunk)


def test_wordprocessingmlbasicdef_cfchunk_constructor_exists():
    assert callable(WordprocessingMLBasicDef_CfChunk.__init__)


def test_wordprocessingmlbasicdef_cfchunk_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_CfChunk.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_blocklevelchunkelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_BlockLevelChunkElt)


def test_wordprocessingmlbasicdef_blocklevelchunkelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_BlockLevelChunkElt.__init__)


def test_wordprocessingmlbasicdef_blocklevelchunkelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_BlockLevelChunkElt.__init__)
    params = list(sig.parameters.keys())



def test_fontslistelt_is_not_abstract():
    assert not inspect.isabstract(FontsListElt)


def test_fontslistelt_constructor_exists():
    assert callable(FontsListElt.__init__)


def test_fontslistelt_constructor_args():
    sig = inspect.signature(FontsListElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_docprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_DocPrElt)


def test_wordprocessingmlbasicdef_docprelt_constructor_exists():
    assert callable(WordprocessingMLBasicDef_DocPrElt.__init__)


def test_wordprocessingmlbasicdef_docprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_DocPrElt.__init__)
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



def test_wordprocessingmlbasicdef_worddocument_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_WordDocument)


def test_wordprocessingmlbasicdef_worddocument_constructor_exists():
    assert callable(WordprocessingMLBasicDef_WordDocument.__init__)


def test_wordprocessingmlbasicdef_worddocument_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_WordDocument.__init__)
    params = list(sig.parameters.keys())



def test_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SmartTagType)


def test_smarttagtype_constructor_exists():
    assert callable(SmartTagType.__init__)


def test_smarttagtype_constructor_args():
    sig = inspect.signature(SmartTagType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_stringtype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_StringType)


def test_wordprocessingmlbasicdef_stringtype_constructor_exists():
    assert callable(WordprocessingMLBasicDef_StringType.__init__)


def test_wordprocessingmlbasicdef_stringtype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_StringType.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_wordprocessingmlbasicdef_stringtype_has_val():
    assert hasattr(WordprocessingMLBasicDef_StringType, "val")
    descriptor = None
    for klass in WordprocessingMLBasicDef_StringType.__mro__:
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



def test_wordprocessingmlbasicdef_deltext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_DelText)


def test_wordprocessingmlbasicdef_deltext_constructor_exists():
    assert callable(WordprocessingMLBasicDef_DelText.__init__)


def test_wordprocessingmlbasicdef_deltext_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_DelText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_text_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_Text)


def test_wordprocessingmlbasicdef_text_constructor_exists():
    assert callable(WordprocessingMLBasicDef_Text.__init__)


def test_wordprocessingmlbasicdef_text_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_Text.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_instrtext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_InstrText)


def test_wordprocessingmlbasicdef_instrtext_constructor_exists():
    assert callable(WordprocessingMLBasicDef_InstrText.__init__)


def test_wordprocessingmlbasicdef_instrtext_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_InstrText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_delinstrtext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_DelInstrText)


def test_wordprocessingmlbasicdef_delinstrtext_constructor_exists():
    assert callable(WordprocessingMLBasicDef_DelInstrText.__init__)


def test_wordprocessingmlbasicdef_delinstrtext_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_DelInstrText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_stringproperty_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_StringProperty)


def test_wordprocessingmlbasicdef_stringproperty_constructor_exists():
    assert callable(WordprocessingMLBasicDef_StringProperty.__init__)


def test_wordprocessingmlbasicdef_stringproperty_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_StringProperty.__init__)
    params = list(sig.parameters.keys())



def test_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(SmartTagsCollection)


def test_smarttagscollection_constructor_exists():
    assert callable(SmartTagsCollection.__init__)


def test_smarttagscollection_constructor_args():
    sig = inspect.signature(SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_SmartTagType)


def test_wordprocessingmlbasicdef_smarttagtype_constructor_exists():
    assert callable(WordprocessingMLBasicDef_SmartTagType.__init__)


def test_wordprocessingmlbasicdef_smarttagtype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"

def test_wordprocessingmlbasicdef_smarttagtype_has_namespaceuri():
    assert hasattr(WordprocessingMLBasicDef_SmartTagType, "namespaceuri")
    descriptor = None
    for klass in WordprocessingMLBasicDef_SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_smarttagtype_has_name():
    assert hasattr(WordprocessingMLBasicDef_SmartTagType, "name")
    descriptor = None
    for klass in WordprocessingMLBasicDef_SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_smarttagtype_has_url():
    assert hasattr(WordprocessingMLBasicDef_SmartTagType, "url")
    descriptor = None
    for klass in WordprocessingMLBasicDef_SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_SmartTagsCollection)


def test_wordprocessingmlbasicdef_smarttagscollection_constructor_exists():
    assert callable(WordprocessingMLBasicDef_SmartTagsCollection.__init__)


def test_wordprocessingmlbasicdef_smarttagscollection_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_CustomDocumentPropertiesCollection)


def test_wordprocessingmlbasicdef_customdocumentpropertiescollection_constructor_exists():
    assert callable(WordprocessingMLBasicDef_CustomDocumentPropertiesCollection.__init__)


def test_wordprocessingmlbasicdef_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_CustomDocumentProperty)


def test_wordprocessingmlbasicdef_customdocumentproperty_constructor_exists():
    assert callable(WordprocessingMLBasicDef_CustomDocumentProperty.__init__)


def test_wordprocessingmlbasicdef_customdocumentproperty_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wordprocessingmlbasicdef_customdocumentproperty_has_name():
    assert hasattr(WordprocessingMLBasicDef_CustomDocumentProperty, "name")
    descriptor = None
    for klass in WordprocessingMLBasicDef_CustomDocumentProperty.__mro__:
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



def test_wordprocessingmlbasicdef_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_BooleanValue)


def test_wordprocessingmlbasicdef_booleanvalue_constructor_exists():
    assert callable(WordprocessingMLBasicDef_BooleanValue.__init__)


def test_wordprocessingmlbasicdef_booleanvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmlbasicdef_booleanvalue_has_value():
    assert hasattr(WordprocessingMLBasicDef_BooleanValue, "value")
    descriptor = None
    for klass in WordprocessingMLBasicDef_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef_floatvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_FloatValue)


def test_wordprocessingmlbasicdef_floatvalue_constructor_exists():
    assert callable(WordprocessingMLBasicDef_FloatValue.__init__)


def test_wordprocessingmlbasicdef_floatvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_FloatValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmlbasicdef_floatvalue_has_value():
    assert hasattr(WordprocessingMLBasicDef_FloatValue, "value")
    descriptor = None
    for klass in WordprocessingMLBasicDef_FloatValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef_datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_DateTimeTypeValue)


def test_wordprocessingmlbasicdef_datetimetypevalue_constructor_exists():
    assert callable(WordprocessingMLBasicDef_DateTimeTypeValue.__init__)


def test_wordprocessingmlbasicdef_datetimetypevalue_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_stringvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_StringValue)


def test_wordprocessingmlbasicdef_stringvalue_constructor_exists():
    assert callable(WordprocessingMLBasicDef_StringValue.__init__)


def test_wordprocessingmlbasicdef_stringvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmlbasicdef_stringvalue_has_value():
    assert hasattr(WordprocessingMLBasicDef_StringValue, "value")
    descriptor = None
    for klass in WordprocessingMLBasicDef_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef_valuetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_ValueType)


def test_wordprocessingmlbasicdef_valuetype_constructor_exists():
    assert callable(WordprocessingMLBasicDef_ValueType.__init__)


def test_wordprocessingmlbasicdef_valuetype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_worddocument_is_not_abstract():
    assert not inspect.isabstract(WordDocument)


def test_worddocument_constructor_exists():
    assert callable(WordDocument.__init__)


def test_worddocument_constructor_args():
    sig = inspect.signature(WordDocument.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmlbasicdef_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_DocumentPropertiesCollection)


def test_wordprocessingmlbasicdef_documentpropertiescollection_constructor_exists():
    assert callable(WordprocessingMLBasicDef_DocumentPropertiesCollection.__init__)


def test_wordprocessingmlbasicdef_documentpropertiescollection_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "lines" in params, "Missing parameter 'lines'"
    assert "category" in params, "Missing parameter 'category'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "words" in params, "Missing parameter 'words'"
    assert "company" in params, "Missing parameter 'company'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "author" in params, "Missing parameter 'author'"
    assert "description" in params, "Missing parameter 'description'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "title" in params, "Missing parameter 'title'"
    assert "revision" in params, "Missing parameter 'revision'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_keywords():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_guid():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_appName():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_bytes():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_manager():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_characters():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_lines():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_category():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_subject():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_totalTime():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_lastAuthor():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_words():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_company():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_presentationFormat():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_author():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_description():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_paragraphs():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_title():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_revision():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_documentpropertiescollection_has_pages():
    assert hasattr(WordprocessingMLBasicDef_DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef_datetimetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_DateTimeType)


def test_wordprocessingmlbasicdef_datetimetype_constructor_exists():
    assert callable(WordprocessingMLBasicDef_DateTimeType.__init__)


def test_wordprocessingmlbasicdef_datetimetype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "day" in params, "Missing parameter 'day'"
    assert "month" in params, "Missing parameter 'month'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "year" in params, "Missing parameter 'year'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "second" in params, "Missing parameter 'second'"

def test_wordprocessingmlbasicdef_datetimetype_has_day():
    assert hasattr(WordprocessingMLBasicDef_DateTimeType, "day")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_datetimetype_has_month():
    assert hasattr(WordprocessingMLBasicDef_DateTimeType, "month")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_datetimetype_has_hour():
    assert hasattr(WordprocessingMLBasicDef_DateTimeType, "hour")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_datetimetype_has_year():
    assert hasattr(WordprocessingMLBasicDef_DateTimeType, "year")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_datetimetype_has_minute():
    assert hasattr(WordprocessingMLBasicDef_DateTimeType, "minute")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_datetimetype_has_second():
    assert hasattr(WordprocessingMLBasicDef_DateTimeType, "second")
    descriptor = None
    for klass in WordprocessingMLBasicDef_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmlbasicdef_versiontype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLBasicDef_VersionType)


def test_wordprocessingmlbasicdef_versiontype_constructor_exists():
    assert callable(WordprocessingMLBasicDef_VersionType.__init__)


def test_wordprocessingmlbasicdef_versiontype_constructor_args():
    sig = inspect.signature(WordprocessingMLBasicDef_VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "nn" in params, "Missing parameter 'nn'"
    assert "n" in params, "Missing parameter 'n'"

def test_wordprocessingmlbasicdef_versiontype_has_nn():
    assert hasattr(WordprocessingMLBasicDef_VersionType, "nn")
    descriptor = None
    for klass in WordprocessingMLBasicDef_VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmlbasicdef_versiontype_has_n():
    assert hasattr(WordprocessingMLBasicDef_VersionType, "n")
    descriptor = None
    for klass in WordprocessingMLBasicDef_VersionType.__mro__:
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
        "fctp_begin",
        "fctp_end",
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
        "bt_text_wrapping",
        "bt_page",
        "bt_column",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BreakType"

def test_notevalue_exists():
    # Check that the Enumeration exists
    assert NoteValue is not None

def test_notevalue_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in NoteValue]
    expected_literals = [
        "ftn_continuation_notice",
        "ftn_separator",
        "ftn_continuation_separator",
        "ftn_normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NoteValue"

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
WordprocessingMLBasicDef_TabElt_strategy = st.builds(
    WordprocessingMLBasicDef_TabElt,
)
WordprocessingMLBasicDef_PictureType_strategy = st.builds(
    WordprocessingMLBasicDef_PictureType,
)
TabElt_strategy = st.builds(
    TabElt,
)
WordprocessingMLBasicDef_StylesElt_strategy = st.builds(
    WordprocessingMLBasicDef_StylesElt,
)
WordprocessingMLBasicDef_ListsElt_strategy = st.builds(
    WordprocessingMLBasicDef_ListsElt,
)
WordprocessingMLBasicDef_FontsListElt_strategy = st.builds(
    WordprocessingMLBasicDef_FontsListElt,
)
WordprocessingMLBasicDef_FldCharElt_strategy = st.builds(
    WordprocessingMLBasicDef_FldCharElt,
    fldLock=
        st.none(),
    fldCharType=
        st.none()
)
FldCharElt_strategy = st.builds(
    FldCharElt,
)
WordprocessingMLBasicDef_SectPrElt_strategy = st.builds(
    WordprocessingMLBasicDef_SectPrElt,
)
WordprocessingMLBasicDef_NoteElt_strategy = st.builds(
    WordprocessingMLBasicDef_NoteElt,
    suppressRef=
        st.none(),
    type=
        st.none()
)
WordprocessingMLBasicDef_SymElt_strategy = st.builds(
    WordprocessingMLBasicDef_SymElt,
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
WordprocessingMLBasicDef_Picture_strategy = st.builds(
    WordprocessingMLBasicDef_Picture,
)
WordprocessingMLBasicDef_NoBreakHyphen_strategy = st.builds(
    WordprocessingMLBasicDef_NoBreakHyphen,
)
WordprocessingMLBasicDef_Cr_strategy = st.builds(
    WordprocessingMLBasicDef_Cr,
)
WordprocessingMLBasicDef_FldChar_strategy = st.builds(
    WordprocessingMLBasicDef_FldChar,
)
WordprocessingMLBasicDef_Tab_strategy = st.builds(
    WordprocessingMLBasicDef_Tab,
)
WordprocessingMLBasicDef_FootnoteRef_strategy = st.builds(
    WordprocessingMLBasicDef_FootnoteRef,
)
WordprocessingMLBasicDef_AnnotationRef_strategy = st.builds(
    WordprocessingMLBasicDef_AnnotationRef,
)
WordprocessingMLBasicDef_SoftHyphen_strategy = st.builds(
    WordprocessingMLBasicDef_SoftHyphen,
)
WordprocessingMLBasicDef_ContinuationSeparator_strategy = st.builds(
    WordprocessingMLBasicDef_ContinuationSeparator,
)
WordprocessingMLBasicDef_PgNum_strategy = st.builds(
    WordprocessingMLBasicDef_PgNum,
)
WordprocessingMLBasicDef_EndnoteRef_strategy = st.builds(
    WordprocessingMLBasicDef_EndnoteRef,
)
WordprocessingMLBasicDef_Separator_strategy = st.builds(
    WordprocessingMLBasicDef_Separator,
)
WordprocessingMLBasicDef_Symbol_strategy = st.builds(
    WordprocessingMLBasicDef_Symbol,
)
WordprocessingMLBasicDef_BreakElt_strategy = st.builds(
    WordprocessingMLBasicDef_BreakElt,
    type=
        st.none()
)
WordprocessingMLBasicDef_RunContentElt_strategy = st.builds(
    WordprocessingMLBasicDef_RunContentElt,
)
RunElt_strategy = st.builds(
    RunElt,
)
WordprocessingMLBasicDef_RunPrElt_strategy = st.builds(
    WordprocessingMLBasicDef_RunPrElt,
)
ParaPrElt_strategy = st.builds(
    ParaPrElt,
)
BlockLevelChunkElt_strategy = st.builds(
    BlockLevelChunkElt,
)
WordprocessingMLBasicDef_RunLevelElt_strategy = st.builds(
    WordprocessingMLBasicDef_RunLevelElt,
)
WordprocessingMLBasicDef_ParaElt_strategy = st.builds(
    WordprocessingMLBasicDef_ParaElt,
)
RunPrElt_strategy = st.builds(
    RunPrElt,
)
WordprocessingMLBasicDef_ParaContentElt_strategy = st.builds(
    WordprocessingMLBasicDef_ParaContentElt,
)
ParaElt_strategy = st.builds(
    ParaElt,
)
WordprocessingMLBasicDef_ParaPrElt_strategy = st.builds(
    WordprocessingMLBasicDef_ParaPrElt,
)
ParaContentElt_strategy = st.builds(
    ParaContentElt,
)
WordprocessingMLBasicDef_SubDocElt_strategy = st.builds(
    WordprocessingMLBasicDef_SubDocElt,
)
WordprocessingMLBasicDef_HLinkElt_strategy = st.builds(
    WordprocessingMLBasicDef_HLinkElt,
)
WordprocessingMLBasicDef_SimpleFieldElt_strategy = st.builds(
    WordprocessingMLBasicDef_SimpleFieldElt,
)
WordprocessingMLBasicDef_RunElt_strategy = st.builds(
    WordprocessingMLBasicDef_RunElt,
)
WordprocessingMLBasicDef_BodyElt_strategy = st.builds(
    WordprocessingMLBasicDef_BodyElt,
)
NoteElt_strategy = st.builds(
    NoteElt,
)
WordprocessingMLBasicDef_Endnote_strategy = st.builds(
    WordprocessingMLBasicDef_Endnote,
)
WordprocessingMLBasicDef_Footnote_strategy = st.builds(
    WordprocessingMLBasicDef_Footnote,
)
WordprocessingMLBasicDef_BlockLevelElt_strategy = st.builds(
    WordprocessingMLBasicDef_BlockLevelElt,
)
SectPrElt_strategy = st.builds(
    SectPrElt,
)
BlockLevelElt_strategy = st.builds(
    BlockLevelElt,
)
WordprocessingMLBasicDef_CfChunk_strategy = st.builds(
    WordprocessingMLBasicDef_CfChunk,
)
WordprocessingMLBasicDef_BlockLevelChunkElt_strategy = st.builds(
    WordprocessingMLBasicDef_BlockLevelChunkElt,
)
FontsListElt_strategy = st.builds(
    FontsListElt,
)
WordprocessingMLBasicDef_DocPrElt_strategy = st.builds(
    WordprocessingMLBasicDef_DocPrElt,
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
WordprocessingMLBasicDef_WordDocument_strategy = st.builds(
    WordprocessingMLBasicDef_WordDocument,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
WordprocessingMLBasicDef_StringType_strategy = st.builds(
    WordprocessingMLBasicDef_StringType,
    val=
        st.none()
)
StringType_strategy = st.builds(
    StringType,
)
WordprocessingMLBasicDef_DelText_strategy = st.builds(
    WordprocessingMLBasicDef_DelText,
)
WordprocessingMLBasicDef_Text_strategy = st.builds(
    WordprocessingMLBasicDef_Text,
)
WordprocessingMLBasicDef_InstrText_strategy = st.builds(
    WordprocessingMLBasicDef_InstrText,
)
WordprocessingMLBasicDef_DelInstrText_strategy = st.builds(
    WordprocessingMLBasicDef_DelInstrText,
)
WordprocessingMLBasicDef_StringProperty_strategy = st.builds(
    WordprocessingMLBasicDef_StringProperty,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
WordprocessingMLBasicDef_SmartTagType_strategy = st.builds(
    WordprocessingMLBasicDef_SmartTagType,
    namespaceuri=
        st.none(),
    name=
        st.none(),
    url=
        st.none()
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
WordprocessingMLBasicDef_SmartTagsCollection_strategy = st.builds(
    WordprocessingMLBasicDef_SmartTagsCollection,
)
WordprocessingMLBasicDef_CustomDocumentPropertiesCollection_strategy = st.builds(
    WordprocessingMLBasicDef_CustomDocumentPropertiesCollection,
)
WordprocessingMLBasicDef_CustomDocumentProperty_strategy = st.builds(
    WordprocessingMLBasicDef_CustomDocumentProperty,
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
WordprocessingMLBasicDef_BooleanValue_strategy = st.builds(
    WordprocessingMLBasicDef_BooleanValue,
    value=
        st.none()
)
WordprocessingMLBasicDef_FloatValue_strategy = st.builds(
    WordprocessingMLBasicDef_FloatValue,
    value=
        st.none()
)
WordprocessingMLBasicDef_DateTimeTypeValue_strategy = st.builds(
    WordprocessingMLBasicDef_DateTimeTypeValue,
)
WordprocessingMLBasicDef_StringValue_strategy = st.builds(
    WordprocessingMLBasicDef_StringValue,
    value=
        st.none()
)
WordprocessingMLBasicDef_ValueType_strategy = st.builds(
    WordprocessingMLBasicDef_ValueType,
)
WordDocument_strategy = st.builds(
    WordDocument,
)
WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy = st.builds(
    WordprocessingMLBasicDef_DocumentPropertiesCollection,
    hyperlinkBase=
        st.none(),
    keywords=
        st.none(),
    guid=
        st.none(),
    charactersWithSpaces=
        st.none(),
    appName=
        st.none(),
    bytes=
        st.none(),
    manager=
        st.none(),
    characters=
        st.none(),
    lines=
        st.none(),
    category=
        st.none(),
    subject=
        st.none(),
    totalTime=
        st.none(),
    lastAuthor=
        st.none(),
    words=
        st.none(),
    company=
        st.none(),
    presentationFormat=
        st.none(),
    author=
        st.none(),
    description=
        st.none(),
    paragraphs=
        st.none(),
    title=
        st.none(),
    revision=
        st.none(),
    pages=
        st.none()
)
WordprocessingMLBasicDef_DateTimeType_strategy = st.builds(
    WordprocessingMLBasicDef_DateTimeType,
    day=
        st.none(),
    month=
        st.none(),
    hour=
        st.none(),
    year=
        st.none(),
    minute=
        st.none(),
    second=
        st.none()
)
WordprocessingMLBasicDef_VersionType_strategy = st.builds(
    WordprocessingMLBasicDef_VersionType,
    nn=
        st.none(),
    n=
        st.none()
)

@given(instance=WordprocessingMLBasicDef_TabElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_tabelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_TabElt)

@given(instance=WordprocessingMLBasicDef_PictureType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_picturetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_PictureType)

@given(instance=TabElt_strategy)
@settings(max_examples=50)
def test_tabelt_instantiation(instance):
    assert isinstance(instance, TabElt)

@given(instance=WordprocessingMLBasicDef_StylesElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_styleselt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_StylesElt)

@given(instance=WordprocessingMLBasicDef_ListsElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_listselt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ListsElt)

@given(instance=WordprocessingMLBasicDef_FontsListElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_fontslistelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_FontsListElt)

@given(instance=WordprocessingMLBasicDef_FldCharElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_fldcharelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_FldCharElt)



@given(instance=WordprocessingMLBasicDef_FldCharElt_strategy)
def test_wordprocessingmlbasicdef_fldcharelt_fldLock_setter(instance):
    original = instance.fldLock
    instance.fldLock = original
    assert instance.fldLock == original



@given(instance=WordprocessingMLBasicDef_FldCharElt_strategy)
def test_wordprocessingmlbasicdef_fldcharelt_fldCharType_setter(instance):
    original = instance.fldCharType
    instance.fldCharType = original
    assert instance.fldCharType == original

@given(instance=FldCharElt_strategy)
@settings(max_examples=50)
def test_fldcharelt_instantiation(instance):
    assert isinstance(instance, FldCharElt)

@given(instance=WordprocessingMLBasicDef_SectPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_sectprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SectPrElt)

@given(instance=WordprocessingMLBasicDef_NoteElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_noteelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_NoteElt)



@given(instance=WordprocessingMLBasicDef_NoteElt_strategy)
def test_wordprocessingmlbasicdef_noteelt_suppressRef_setter(instance):
    original = instance.suppressRef
    instance.suppressRef = original
    assert instance.suppressRef == original



@given(instance=WordprocessingMLBasicDef_NoteElt_strategy)
def test_wordprocessingmlbasicdef_noteelt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=WordprocessingMLBasicDef_SymElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_symelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SymElt)

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

@given(instance=WordprocessingMLBasicDef_Picture_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_picture_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Picture)

@given(instance=WordprocessingMLBasicDef_NoBreakHyphen_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_nobreakhyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_NoBreakHyphen)

@given(instance=WordprocessingMLBasicDef_Cr_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_cr_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Cr)

@given(instance=WordprocessingMLBasicDef_FldChar_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_fldchar_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_FldChar)

@given(instance=WordprocessingMLBasicDef_Tab_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_tab_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Tab)

@given(instance=WordprocessingMLBasicDef_FootnoteRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_footnoteref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_FootnoteRef)

@given(instance=WordprocessingMLBasicDef_AnnotationRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_annotationref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_AnnotationRef)

@given(instance=WordprocessingMLBasicDef_SoftHyphen_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_softhyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SoftHyphen)

@given(instance=WordprocessingMLBasicDef_ContinuationSeparator_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_continuationseparator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ContinuationSeparator)

@given(instance=WordprocessingMLBasicDef_PgNum_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_pgnum_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_PgNum)

@given(instance=WordprocessingMLBasicDef_EndnoteRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_endnoteref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_EndnoteRef)

@given(instance=WordprocessingMLBasicDef_Separator_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_separator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Separator)

@given(instance=WordprocessingMLBasicDef_Symbol_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_symbol_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Symbol)

@given(instance=WordprocessingMLBasicDef_BreakElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_breakelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_BreakElt)



@given(instance=WordprocessingMLBasicDef_BreakElt_strategy)
def test_wordprocessingmlbasicdef_breakelt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=WordprocessingMLBasicDef_RunContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_runcontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_RunContentElt)

@given(instance=RunElt_strategy)
@settings(max_examples=50)
def test_runelt_instantiation(instance):
    assert isinstance(instance, RunElt)

@given(instance=WordprocessingMLBasicDef_RunPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_runprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_RunPrElt)

@given(instance=ParaPrElt_strategy)
@settings(max_examples=50)
def test_paraprelt_instantiation(instance):
    assert isinstance(instance, ParaPrElt)

@given(instance=BlockLevelChunkElt_strategy)
@settings(max_examples=50)
def test_blocklevelchunkelt_instantiation(instance):
    assert isinstance(instance, BlockLevelChunkElt)

@given(instance=WordprocessingMLBasicDef_RunLevelElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_runlevelelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_RunLevelElt)

@given(instance=WordprocessingMLBasicDef_ParaElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_paraelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ParaElt)

@given(instance=RunPrElt_strategy)
@settings(max_examples=50)
def test_runprelt_instantiation(instance):
    assert isinstance(instance, RunPrElt)

@given(instance=WordprocessingMLBasicDef_ParaContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_paracontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ParaContentElt)

@given(instance=ParaElt_strategy)
@settings(max_examples=50)
def test_paraelt_instantiation(instance):
    assert isinstance(instance, ParaElt)

@given(instance=WordprocessingMLBasicDef_ParaPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_paraprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ParaPrElt)

@given(instance=ParaContentElt_strategy)
@settings(max_examples=50)
def test_paracontentelt_instantiation(instance):
    assert isinstance(instance, ParaContentElt)

@given(instance=WordprocessingMLBasicDef_SubDocElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_subdocelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SubDocElt)

@given(instance=WordprocessingMLBasicDef_HLinkElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_hlinkelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_HLinkElt)

@given(instance=WordprocessingMLBasicDef_SimpleFieldElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_simplefieldelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SimpleFieldElt)

@given(instance=WordprocessingMLBasicDef_RunElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_runelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_RunElt)

@given(instance=WordprocessingMLBasicDef_BodyElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_bodyelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_BodyElt)

@given(instance=NoteElt_strategy)
@settings(max_examples=50)
def test_noteelt_instantiation(instance):
    assert isinstance(instance, NoteElt)

@given(instance=WordprocessingMLBasicDef_Endnote_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_endnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Endnote)

@given(instance=WordprocessingMLBasicDef_Footnote_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_footnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Footnote)

@given(instance=WordprocessingMLBasicDef_BlockLevelElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_blocklevelelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_BlockLevelElt)

@given(instance=SectPrElt_strategy)
@settings(max_examples=50)
def test_sectprelt_instantiation(instance):
    assert isinstance(instance, SectPrElt)

@given(instance=BlockLevelElt_strategy)
@settings(max_examples=50)
def test_blocklevelelt_instantiation(instance):
    assert isinstance(instance, BlockLevelElt)

@given(instance=WordprocessingMLBasicDef_CfChunk_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_cfchunk_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_CfChunk)

@given(instance=WordprocessingMLBasicDef_BlockLevelChunkElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_blocklevelchunkelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_BlockLevelChunkElt)

@given(instance=FontsListElt_strategy)
@settings(max_examples=50)
def test_fontslistelt_instantiation(instance):
    assert isinstance(instance, FontsListElt)

@given(instance=WordprocessingMLBasicDef_DocPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_docprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DocPrElt)

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

@given(instance=WordprocessingMLBasicDef_WordDocument_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_worddocument_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_WordDocument)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=WordprocessingMLBasicDef_StringType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_stringtype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_StringType)



@given(instance=WordprocessingMLBasicDef_StringType_strategy)
def test_wordprocessingmlbasicdef_stringtype_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=StringType_strategy)
@settings(max_examples=50)
def test_stringtype_instantiation(instance):
    assert isinstance(instance, StringType)

@given(instance=WordprocessingMLBasicDef_DelText_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_deltext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DelText)

@given(instance=WordprocessingMLBasicDef_Text_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_text_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_Text)

@given(instance=WordprocessingMLBasicDef_InstrText_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_instrtext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_InstrText)

@given(instance=WordprocessingMLBasicDef_DelInstrText_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_delinstrtext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DelInstrText)

@given(instance=WordprocessingMLBasicDef_StringProperty_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_stringproperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_StringProperty)

@given(instance=SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_smarttagscollection_instantiation(instance):
    assert isinstance(instance, SmartTagsCollection)

@given(instance=WordprocessingMLBasicDef_SmartTagType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_smarttagtype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SmartTagType)



@given(instance=WordprocessingMLBasicDef_SmartTagType_strategy)
def test_wordprocessingmlbasicdef_smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original



@given(instance=WordprocessingMLBasicDef_SmartTagType_strategy)
def test_wordprocessingmlbasicdef_smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=WordprocessingMLBasicDef_SmartTagType_strategy)
def test_wordprocessingmlbasicdef_smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=WordprocessingMLBasicDef_SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_smarttagscollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_SmartTagsCollection)

@given(instance=WordprocessingMLBasicDef_CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_CustomDocumentPropertiesCollection)

@given(instance=WordprocessingMLBasicDef_CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_CustomDocumentProperty)



@given(instance=WordprocessingMLBasicDef_CustomDocumentProperty_strategy)
def test_wordprocessingmlbasicdef_customdocumentproperty_name_setter(instance):
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

@given(instance=WordprocessingMLBasicDef_BooleanValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_booleanvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_BooleanValue)



@given(instance=WordprocessingMLBasicDef_BooleanValue_strategy)
def test_wordprocessingmlbasicdef_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLBasicDef_FloatValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_floatvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_FloatValue)



@given(instance=WordprocessingMLBasicDef_FloatValue_strategy)
def test_wordprocessingmlbasicdef_floatvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLBasicDef_DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_datetimetypevalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DateTimeTypeValue)

@given(instance=WordprocessingMLBasicDef_StringValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_stringvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_StringValue)



@given(instance=WordprocessingMLBasicDef_StringValue_strategy)
def test_wordprocessingmlbasicdef_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLBasicDef_ValueType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_valuetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_ValueType)

@given(instance=WordDocument_strategy)
@settings(max_examples=50)
def test_worddocument_instantiation(instance):
    assert isinstance(instance, WordDocument)

@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DocumentPropertiesCollection)



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original



@given(instance=WordprocessingMLBasicDef_DocumentPropertiesCollection_strategy)
def test_wordprocessingmlbasicdef_documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=WordprocessingMLBasicDef_DateTimeType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_datetimetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_DateTimeType)



@given(instance=WordprocessingMLBasicDef_DateTimeType_strategy)
def test_wordprocessingmlbasicdef_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original



@given(instance=WordprocessingMLBasicDef_DateTimeType_strategy)
def test_wordprocessingmlbasicdef_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=WordprocessingMLBasicDef_DateTimeType_strategy)
def test_wordprocessingmlbasicdef_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=WordprocessingMLBasicDef_DateTimeType_strategy)
def test_wordprocessingmlbasicdef_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=WordprocessingMLBasicDef_DateTimeType_strategy)
def test_wordprocessingmlbasicdef_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=WordprocessingMLBasicDef_DateTimeType_strategy)
def test_wordprocessingmlbasicdef_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original

@given(instance=WordprocessingMLBasicDef_VersionType_strategy)
@settings(max_examples=50)
def test_wordprocessingmlbasicdef_versiontype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLBasicDef_VersionType)



@given(instance=WordprocessingMLBasicDef_VersionType_strategy)
def test_wordprocessingmlbasicdef_versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original



@given(instance=WordprocessingMLBasicDef_VersionType_strategy)
def test_wordprocessingmlbasicdef_versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original
