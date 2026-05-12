import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RunElt,
    WordprocessingMLTableElts_RunPrElt,
    RunContentElt,
    WordprocessingMLTableElts_NoBreakHyphen,
    WordprocessingMLTableElts_SoftHyphen,
    WordprocessingMLTableElts_AnnotationRef,
    RunPrElt,
    WordprocessingMLTableElts_ParaContentElt,
    WordprocessingMLTableElts_RunContentElt,
    ParaContentElt,
    WordprocessingMLTableElts_RunElt,
    ParaPrElt,
    BlockLevelChunkElt,
    WordprocessingMLTableElts_ParaElt,
    TableCellElt,
    NoteElt,
    ParaElt,
    WordprocessingMLTableElts_ParaPrElt,
    BlockLevelElt,
    WordprocessingMLTableElts_BlockLevelChunkElt,
    WordprocessingMLTableElts_BodyElt,
    WordprocessingMLTableElts_DocPrElt,
    BodyElt,
    WordprocessingMLTableElts_BlockLevelElt,
    SectPrElt,
    StylesElt,
    WordprocessingMLTableElts_TabElt,
    WordprocessingMLTableElts_PictureType,
    WordprocessingMLTableElts_SubDocElt,
    WordprocessingMLTableElts_RunLevelElt,
    WordprocessingMLTableElts_SectPrElt,
    WordprocessingMLTableElts_HLinkElt,
    WordprocessingMLTableElts_SimpleFieldElt,
    WordprocessingMLTableElts_CfChunk,
    WordprocessingMLTableElts_ListsElt,
    WordprocessingMLTableElts_FontsListElt,
    WordprocessingMLTableElts_TableCellPrElt,
    WordprocessingMLTableElts_StylesElt,
    WordprocessingMLTableElts_TableCellElt,
    WordprocessingMLTableElts_RowContentElt,
    TableCellPrElt,
    RowContentElt,
    TableRowPrElt,
    TablePrExElt,
    WordprocessingMLTableElts_RowElt,
    WordprocessingMLTableElts_TableRowPrElt,
    WordprocessingMLTableElts_TablePrExElt,
    RowElt,
    WordprocessingMLTableElts_TableContentElt,
    WordprocessingMLTableElts_TableGridElt,
    TableElt,
    RunLevelElt,
    TableGridElt,
    TablePrElt,
    WordprocessingMLTableElts_TableElt,
    WordprocessingMLTableElts_TablePrElt,
    TableContentElt,
    WordprocessingMLTableElts_FldCharElt,
    FldCharElt,
    WordprocessingMLTableElts_FldChar,
    TabElt,
    WordprocessingMLTableElts_Tab,
    WordprocessingMLTableElts_SymElt,
    WordprocessingMLTableElts_NoteElt,
    WordprocessingMLTableElts_Endnote,
    WordprocessingMLTableElts_Footnote,
    WordprocessingMLTableElts_Cr,
    WordprocessingMLTableElts_PgNum,
    WordprocessingMLTableElts_ContinuationSeparator,
    WordprocessingMLTableElts_Separator,
    WordprocessingMLTableElts_EndnoteRef,
    SymElt,
    WordprocessingMLTableElts_Symbol,
    PictureType,
    WordprocessingMLTableElts_Picture,
    WordprocessingMLTableElts_BreakElt,
    WordprocessingMLTableElts_FootnoteRef,
    ListsElt,
    FontsListElt,
    DocPrElt,
    DocumentPropertiesCollection,
    WordprocessingMLTableElts_WordDocument,
    StringProperty,
    WordprocessingMLTableElts_StringType,
    StringType,
    WordprocessingMLTableElts_DelText,
    WordprocessingMLTableElts_Text,
    WordprocessingMLTableElts_InstrText,
    WordprocessingMLTableElts_DelInstrText,
    WordprocessingMLTableElts_StringProperty,
    SmartTagType,
    WordprocessingMLTableElts_SmartTagsCollection,
    CustomDocumentPropertiesCollection,
    WordprocessingMLTableElts_CustomDocumentProperty,
    CustomDocumentProperty,
    SmartTagsCollection,
    WordprocessingMLTableElts_SmartTagType,
    WordprocessingMLTableElts_CustomDocumentPropertiesCollection,
    VersionType,
    WordDocument,
    WordprocessingMLTableElts_DocumentPropertiesCollection,
    ValueType,
    WordprocessingMLTableElts_FloatValue,
    WordprocessingMLTableElts_BooleanValue,
    WordprocessingMLTableElts_StringValue,
    WordprocessingMLTableElts_ValueType,
    WordprocessingMLTableElts_VersionType,
    DateTimeType,
    WordprocessingMLTableElts_DateTimeTypeValue,
    WordprocessingMLTableElts_DateTimeType,
    BreakType,
    OnOffType,
    NoteValue,
    FldCharTypeProperty,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_runelt_is_not_abstract():
    assert not inspect.isabstract(RunElt)


def test_runelt_constructor_exists():
    assert callable(RunElt.__init__)


def test_runelt_constructor_args():
    sig = inspect.signature(RunElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_runprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_RunPrElt)


def test_wordprocessingmltableelts_runprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_RunPrElt.__init__)


def test_wordprocessingmltableelts_runprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_RunPrElt.__init__)
    params = list(sig.parameters.keys())



def test_runcontentelt_is_not_abstract():
    assert not inspect.isabstract(RunContentElt)


def test_runcontentelt_constructor_exists():
    assert callable(RunContentElt.__init__)


def test_runcontentelt_constructor_args():
    sig = inspect.signature(RunContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_nobreakhyphen_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_NoBreakHyphen)


def test_wordprocessingmltableelts_nobreakhyphen_constructor_exists():
    assert callable(WordprocessingMLTableElts_NoBreakHyphen.__init__)


def test_wordprocessingmltableelts_nobreakhyphen_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_NoBreakHyphen.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_softhyphen_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_SoftHyphen)


def test_wordprocessingmltableelts_softhyphen_constructor_exists():
    assert callable(WordprocessingMLTableElts_SoftHyphen.__init__)


def test_wordprocessingmltableelts_softhyphen_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_SoftHyphen.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_annotationref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_AnnotationRef)


def test_wordprocessingmltableelts_annotationref_constructor_exists():
    assert callable(WordprocessingMLTableElts_AnnotationRef.__init__)


def test_wordprocessingmltableelts_annotationref_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_AnnotationRef.__init__)
    params = list(sig.parameters.keys())



def test_runprelt_is_not_abstract():
    assert not inspect.isabstract(RunPrElt)


def test_runprelt_constructor_exists():
    assert callable(RunPrElt.__init__)


def test_runprelt_constructor_args():
    sig = inspect.signature(RunPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_paracontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_ParaContentElt)


def test_wordprocessingmltableelts_paracontentelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_ParaContentElt.__init__)


def test_wordprocessingmltableelts_paracontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_ParaContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_runcontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_RunContentElt)


def test_wordprocessingmltableelts_runcontentelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_RunContentElt.__init__)


def test_wordprocessingmltableelts_runcontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_RunContentElt.__init__)
    params = list(sig.parameters.keys())



def test_paracontentelt_is_not_abstract():
    assert not inspect.isabstract(ParaContentElt)


def test_paracontentelt_constructor_exists():
    assert callable(ParaContentElt.__init__)


def test_paracontentelt_constructor_args():
    sig = inspect.signature(ParaContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_runelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_RunElt)


def test_wordprocessingmltableelts_runelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_RunElt.__init__)


def test_wordprocessingmltableelts_runelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_RunElt.__init__)
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



def test_wordprocessingmltableelts_paraelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_ParaElt)


def test_wordprocessingmltableelts_paraelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_ParaElt.__init__)


def test_wordprocessingmltableelts_paraelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_ParaElt.__init__)
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



def test_paraelt_is_not_abstract():
    assert not inspect.isabstract(ParaElt)


def test_paraelt_constructor_exists():
    assert callable(ParaElt.__init__)


def test_paraelt_constructor_args():
    sig = inspect.signature(ParaElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_paraprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_ParaPrElt)


def test_wordprocessingmltableelts_paraprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_ParaPrElt.__init__)


def test_wordprocessingmltableelts_paraprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_ParaPrElt.__init__)
    params = list(sig.parameters.keys())



def test_blocklevelelt_is_not_abstract():
    assert not inspect.isabstract(BlockLevelElt)


def test_blocklevelelt_constructor_exists():
    assert callable(BlockLevelElt.__init__)


def test_blocklevelelt_constructor_args():
    sig = inspect.signature(BlockLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_blocklevelchunkelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_BlockLevelChunkElt)


def test_wordprocessingmltableelts_blocklevelchunkelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_BlockLevelChunkElt.__init__)


def test_wordprocessingmltableelts_blocklevelchunkelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_BlockLevelChunkElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_bodyelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_BodyElt)


def test_wordprocessingmltableelts_bodyelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_BodyElt.__init__)


def test_wordprocessingmltableelts_bodyelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_BodyElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_docprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_DocPrElt)


def test_wordprocessingmltableelts_docprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_DocPrElt.__init__)


def test_wordprocessingmltableelts_docprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_DocPrElt.__init__)
    params = list(sig.parameters.keys())



def test_bodyelt_is_not_abstract():
    assert not inspect.isabstract(BodyElt)


def test_bodyelt_constructor_exists():
    assert callable(BodyElt.__init__)


def test_bodyelt_constructor_args():
    sig = inspect.signature(BodyElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_blocklevelelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_BlockLevelElt)


def test_wordprocessingmltableelts_blocklevelelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_BlockLevelElt.__init__)


def test_wordprocessingmltableelts_blocklevelelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_BlockLevelElt.__init__)
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



def test_wordprocessingmltableelts_tabelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TabElt)


def test_wordprocessingmltableelts_tabelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TabElt.__init__)


def test_wordprocessingmltableelts_tabelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TabElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_picturetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_PictureType)


def test_wordprocessingmltableelts_picturetype_constructor_exists():
    assert callable(WordprocessingMLTableElts_PictureType.__init__)


def test_wordprocessingmltableelts_picturetype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_PictureType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_subdocelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_SubDocElt)


def test_wordprocessingmltableelts_subdocelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_SubDocElt.__init__)


def test_wordprocessingmltableelts_subdocelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_SubDocElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_runlevelelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_RunLevelElt)


def test_wordprocessingmltableelts_runlevelelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_RunLevelElt.__init__)


def test_wordprocessingmltableelts_runlevelelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_RunLevelElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_sectprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_SectPrElt)


def test_wordprocessingmltableelts_sectprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_SectPrElt.__init__)


def test_wordprocessingmltableelts_sectprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_SectPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_hlinkelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_HLinkElt)


def test_wordprocessingmltableelts_hlinkelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_HLinkElt.__init__)


def test_wordprocessingmltableelts_hlinkelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_HLinkElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_simplefieldelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_SimpleFieldElt)


def test_wordprocessingmltableelts_simplefieldelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_SimpleFieldElt.__init__)


def test_wordprocessingmltableelts_simplefieldelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_SimpleFieldElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_cfchunk_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_CfChunk)


def test_wordprocessingmltableelts_cfchunk_constructor_exists():
    assert callable(WordprocessingMLTableElts_CfChunk.__init__)


def test_wordprocessingmltableelts_cfchunk_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_CfChunk.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_listselt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_ListsElt)


def test_wordprocessingmltableelts_listselt_constructor_exists():
    assert callable(WordprocessingMLTableElts_ListsElt.__init__)


def test_wordprocessingmltableelts_listselt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_ListsElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_fontslistelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_FontsListElt)


def test_wordprocessingmltableelts_fontslistelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_FontsListElt.__init__)


def test_wordprocessingmltableelts_fontslistelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_FontsListElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_tablecellprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TableCellPrElt)


def test_wordprocessingmltableelts_tablecellprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TableCellPrElt.__init__)


def test_wordprocessingmltableelts_tablecellprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TableCellPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_styleselt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_StylesElt)


def test_wordprocessingmltableelts_styleselt_constructor_exists():
    assert callable(WordprocessingMLTableElts_StylesElt.__init__)


def test_wordprocessingmltableelts_styleselt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_StylesElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_tablecellelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TableCellElt)


def test_wordprocessingmltableelts_tablecellelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TableCellElt.__init__)


def test_wordprocessingmltableelts_tablecellelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TableCellElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_rowcontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_RowContentElt)


def test_wordprocessingmltableelts_rowcontentelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_RowContentElt.__init__)


def test_wordprocessingmltableelts_rowcontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_RowContentElt.__init__)
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



def test_wordprocessingmltableelts_rowelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_RowElt)


def test_wordprocessingmltableelts_rowelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_RowElt.__init__)


def test_wordprocessingmltableelts_rowelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_RowElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_tablerowprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TableRowPrElt)


def test_wordprocessingmltableelts_tablerowprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TableRowPrElt.__init__)


def test_wordprocessingmltableelts_tablerowprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TableRowPrElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_tableprexelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TablePrExElt)


def test_wordprocessingmltableelts_tableprexelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TablePrExElt.__init__)


def test_wordprocessingmltableelts_tableprexelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TablePrExElt.__init__)
    params = list(sig.parameters.keys())



def test_rowelt_is_not_abstract():
    assert not inspect.isabstract(RowElt)


def test_rowelt_constructor_exists():
    assert callable(RowElt.__init__)


def test_rowelt_constructor_args():
    sig = inspect.signature(RowElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_tablecontentelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TableContentElt)


def test_wordprocessingmltableelts_tablecontentelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TableContentElt.__init__)


def test_wordprocessingmltableelts_tablecontentelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TableContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_tablegridelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TableGridElt)


def test_wordprocessingmltableelts_tablegridelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TableGridElt.__init__)


def test_wordprocessingmltableelts_tablegridelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TableGridElt.__init__)
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



def test_wordprocessingmltableelts_tableelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TableElt)


def test_wordprocessingmltableelts_tableelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TableElt.__init__)


def test_wordprocessingmltableelts_tableelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TableElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_tableprelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_TablePrElt)


def test_wordprocessingmltableelts_tableprelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_TablePrElt.__init__)


def test_wordprocessingmltableelts_tableprelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_TablePrElt.__init__)
    params = list(sig.parameters.keys())



def test_tablecontentelt_is_not_abstract():
    assert not inspect.isabstract(TableContentElt)


def test_tablecontentelt_constructor_exists():
    assert callable(TableContentElt.__init__)


def test_tablecontentelt_constructor_args():
    sig = inspect.signature(TableContentElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_fldcharelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_FldCharElt)


def test_wordprocessingmltableelts_fldcharelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_FldCharElt.__init__)


def test_wordprocessingmltableelts_fldcharelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_FldCharElt.__init__)
    params = list(sig.parameters.keys())
    assert "fldCharType" in params, "Missing parameter 'fldCharType'"
    assert "fldLock" in params, "Missing parameter 'fldLock'"

def test_wordprocessingmltableelts_fldcharelt_has_fldCharType():
    assert hasattr(WordprocessingMLTableElts_FldCharElt, "fldCharType")
    descriptor = None
    for klass in WordprocessingMLTableElts_FldCharElt.__mro__:
        if "fldCharType" in klass.__dict__:
            descriptor = klass.__dict__["fldCharType"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_fldcharelt_has_fldLock():
    assert hasattr(WordprocessingMLTableElts_FldCharElt, "fldLock")
    descriptor = None
    for klass in WordprocessingMLTableElts_FldCharElt.__mro__:
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



def test_wordprocessingmltableelts_fldchar_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_FldChar)


def test_wordprocessingmltableelts_fldchar_constructor_exists():
    assert callable(WordprocessingMLTableElts_FldChar.__init__)


def test_wordprocessingmltableelts_fldchar_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_FldChar.__init__)
    params = list(sig.parameters.keys())



def test_tabelt_is_not_abstract():
    assert not inspect.isabstract(TabElt)


def test_tabelt_constructor_exists():
    assert callable(TabElt.__init__)


def test_tabelt_constructor_args():
    sig = inspect.signature(TabElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_tab_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_Tab)


def test_wordprocessingmltableelts_tab_constructor_exists():
    assert callable(WordprocessingMLTableElts_Tab.__init__)


def test_wordprocessingmltableelts_tab_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_Tab.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_symelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_SymElt)


def test_wordprocessingmltableelts_symelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_SymElt.__init__)


def test_wordprocessingmltableelts_symelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_SymElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_noteelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_NoteElt)


def test_wordprocessingmltableelts_noteelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_NoteElt.__init__)


def test_wordprocessingmltableelts_noteelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_NoteElt.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "suppressRef" in params, "Missing parameter 'suppressRef'"

def test_wordprocessingmltableelts_noteelt_has_type():
    assert hasattr(WordprocessingMLTableElts_NoteElt, "type")
    descriptor = None
    for klass in WordprocessingMLTableElts_NoteElt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_noteelt_has_suppressRef():
    assert hasattr(WordprocessingMLTableElts_NoteElt, "suppressRef")
    descriptor = None
    for klass in WordprocessingMLTableElts_NoteElt.__mro__:
        if "suppressRef" in klass.__dict__:
            descriptor = klass.__dict__["suppressRef"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts_endnote_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_Endnote)


def test_wordprocessingmltableelts_endnote_constructor_exists():
    assert callable(WordprocessingMLTableElts_Endnote.__init__)


def test_wordprocessingmltableelts_endnote_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_Endnote.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_footnote_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_Footnote)


def test_wordprocessingmltableelts_footnote_constructor_exists():
    assert callable(WordprocessingMLTableElts_Footnote.__init__)


def test_wordprocessingmltableelts_footnote_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_Footnote.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_cr_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_Cr)


def test_wordprocessingmltableelts_cr_constructor_exists():
    assert callable(WordprocessingMLTableElts_Cr.__init__)


def test_wordprocessingmltableelts_cr_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_Cr.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_pgnum_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_PgNum)


def test_wordprocessingmltableelts_pgnum_constructor_exists():
    assert callable(WordprocessingMLTableElts_PgNum.__init__)


def test_wordprocessingmltableelts_pgnum_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_PgNum.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_continuationseparator_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_ContinuationSeparator)


def test_wordprocessingmltableelts_continuationseparator_constructor_exists():
    assert callable(WordprocessingMLTableElts_ContinuationSeparator.__init__)


def test_wordprocessingmltableelts_continuationseparator_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_ContinuationSeparator.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_separator_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_Separator)


def test_wordprocessingmltableelts_separator_constructor_exists():
    assert callable(WordprocessingMLTableElts_Separator.__init__)


def test_wordprocessingmltableelts_separator_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_Separator.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_endnoteref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_EndnoteRef)


def test_wordprocessingmltableelts_endnoteref_constructor_exists():
    assert callable(WordprocessingMLTableElts_EndnoteRef.__init__)


def test_wordprocessingmltableelts_endnoteref_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_EndnoteRef.__init__)
    params = list(sig.parameters.keys())



def test_symelt_is_not_abstract():
    assert not inspect.isabstract(SymElt)


def test_symelt_constructor_exists():
    assert callable(SymElt.__init__)


def test_symelt_constructor_args():
    sig = inspect.signature(SymElt.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_symbol_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_Symbol)


def test_wordprocessingmltableelts_symbol_constructor_exists():
    assert callable(WordprocessingMLTableElts_Symbol.__init__)


def test_wordprocessingmltableelts_symbol_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_Symbol.__init__)
    params = list(sig.parameters.keys())



def test_picturetype_is_not_abstract():
    assert not inspect.isabstract(PictureType)


def test_picturetype_constructor_exists():
    assert callable(PictureType.__init__)


def test_picturetype_constructor_args():
    sig = inspect.signature(PictureType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_picture_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_Picture)


def test_wordprocessingmltableelts_picture_constructor_exists():
    assert callable(WordprocessingMLTableElts_Picture.__init__)


def test_wordprocessingmltableelts_picture_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_Picture.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_breakelt_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_BreakElt)


def test_wordprocessingmltableelts_breakelt_constructor_exists():
    assert callable(WordprocessingMLTableElts_BreakElt.__init__)


def test_wordprocessingmltableelts_breakelt_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_BreakElt.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"

def test_wordprocessingmltableelts_breakelt_has_type():
    assert hasattr(WordprocessingMLTableElts_BreakElt, "type")
    descriptor = None
    for klass in WordprocessingMLTableElts_BreakElt.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts_footnoteref_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_FootnoteRef)


def test_wordprocessingmltableelts_footnoteref_constructor_exists():
    assert callable(WordprocessingMLTableElts_FootnoteRef.__init__)


def test_wordprocessingmltableelts_footnoteref_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_FootnoteRef.__init__)
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



def test_wordprocessingmltableelts_worddocument_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_WordDocument)


def test_wordprocessingmltableelts_worddocument_constructor_exists():
    assert callable(WordprocessingMLTableElts_WordDocument.__init__)


def test_wordprocessingmltableelts_worddocument_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_WordDocument.__init__)
    params = list(sig.parameters.keys())



def test_stringproperty_is_not_abstract():
    assert not inspect.isabstract(StringProperty)


def test_stringproperty_constructor_exists():
    assert callable(StringProperty.__init__)


def test_stringproperty_constructor_args():
    sig = inspect.signature(StringProperty.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_stringtype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_StringType)


def test_wordprocessingmltableelts_stringtype_constructor_exists():
    assert callable(WordprocessingMLTableElts_StringType.__init__)


def test_wordprocessingmltableelts_stringtype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_StringType.__init__)
    params = list(sig.parameters.keys())
    assert "val" in params, "Missing parameter 'val'"

def test_wordprocessingmltableelts_stringtype_has_val():
    assert hasattr(WordprocessingMLTableElts_StringType, "val")
    descriptor = None
    for klass in WordprocessingMLTableElts_StringType.__mro__:
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



def test_wordprocessingmltableelts_deltext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_DelText)


def test_wordprocessingmltableelts_deltext_constructor_exists():
    assert callable(WordprocessingMLTableElts_DelText.__init__)


def test_wordprocessingmltableelts_deltext_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_DelText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_text_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_Text)


def test_wordprocessingmltableelts_text_constructor_exists():
    assert callable(WordprocessingMLTableElts_Text.__init__)


def test_wordprocessingmltableelts_text_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_Text.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_instrtext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_InstrText)


def test_wordprocessingmltableelts_instrtext_constructor_exists():
    assert callable(WordprocessingMLTableElts_InstrText.__init__)


def test_wordprocessingmltableelts_instrtext_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_InstrText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_delinstrtext_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_DelInstrText)


def test_wordprocessingmltableelts_delinstrtext_constructor_exists():
    assert callable(WordprocessingMLTableElts_DelInstrText.__init__)


def test_wordprocessingmltableelts_delinstrtext_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_DelInstrText.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_stringproperty_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_StringProperty)


def test_wordprocessingmltableelts_stringproperty_constructor_exists():
    assert callable(WordprocessingMLTableElts_StringProperty.__init__)


def test_wordprocessingmltableelts_stringproperty_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_StringProperty.__init__)
    params = list(sig.parameters.keys())



def test_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(SmartTagType)


def test_smarttagtype_constructor_exists():
    assert callable(SmartTagType.__init__)


def test_smarttagtype_constructor_args():
    sig = inspect.signature(SmartTagType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_smarttagscollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_SmartTagsCollection)


def test_wordprocessingmltableelts_smarttagscollection_constructor_exists():
    assert callable(WordprocessingMLTableElts_SmartTagsCollection.__init__)


def test_wordprocessingmltableelts_smarttagscollection_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_SmartTagsCollection.__init__)
    params = list(sig.parameters.keys())



def test_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(CustomDocumentPropertiesCollection)


def test_customdocumentpropertiescollection_constructor_exists():
    assert callable(CustomDocumentPropertiesCollection.__init__)


def test_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(CustomDocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_customdocumentproperty_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_CustomDocumentProperty)


def test_wordprocessingmltableelts_customdocumentproperty_constructor_exists():
    assert callable(WordprocessingMLTableElts_CustomDocumentProperty.__init__)


def test_wordprocessingmltableelts_customdocumentproperty_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_CustomDocumentProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_wordprocessingmltableelts_customdocumentproperty_has_name():
    assert hasattr(WordprocessingMLTableElts_CustomDocumentProperty, "name")
    descriptor = None
    for klass in WordprocessingMLTableElts_CustomDocumentProperty.__mro__:
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



def test_wordprocessingmltableelts_smarttagtype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_SmartTagType)


def test_wordprocessingmltableelts_smarttagtype_constructor_exists():
    assert callable(WordprocessingMLTableElts_SmartTagType.__init__)


def test_wordprocessingmltableelts_smarttagtype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_SmartTagType.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "url" in params, "Missing parameter 'url'"
    assert "namespaceuri" in params, "Missing parameter 'namespaceuri'"

def test_wordprocessingmltableelts_smarttagtype_has_name():
    assert hasattr(WordprocessingMLTableElts_SmartTagType, "name")
    descriptor = None
    for klass in WordprocessingMLTableElts_SmartTagType.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_smarttagtype_has_url():
    assert hasattr(WordprocessingMLTableElts_SmartTagType, "url")
    descriptor = None
    for klass in WordprocessingMLTableElts_SmartTagType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_smarttagtype_has_namespaceuri():
    assert hasattr(WordprocessingMLTableElts_SmartTagType, "namespaceuri")
    descriptor = None
    for klass in WordprocessingMLTableElts_SmartTagType.__mro__:
        if "namespaceuri" in klass.__dict__:
            descriptor = klass.__dict__["namespaceuri"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts_customdocumentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_CustomDocumentPropertiesCollection)


def test_wordprocessingmltableelts_customdocumentpropertiescollection_constructor_exists():
    assert callable(WordprocessingMLTableElts_CustomDocumentPropertiesCollection.__init__)


def test_wordprocessingmltableelts_customdocumentpropertiescollection_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_CustomDocumentPropertiesCollection.__init__)
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



def test_wordprocessingmltableelts_documentpropertiescollection_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_DocumentPropertiesCollection)


def test_wordprocessingmltableelts_documentpropertiescollection_constructor_exists():
    assert callable(WordprocessingMLTableElts_DocumentPropertiesCollection.__init__)


def test_wordprocessingmltableelts_documentpropertiescollection_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_DocumentPropertiesCollection.__init__)
    params = list(sig.parameters.keys())
    assert "lines" in params, "Missing parameter 'lines'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "lastAuthor" in params, "Missing parameter 'lastAuthor'"
    assert "guid" in params, "Missing parameter 'guid'"
    assert "author" in params, "Missing parameter 'author'"
    assert "hyperlinkBase" in params, "Missing parameter 'hyperlinkBase'"
    assert "subject" in params, "Missing parameter 'subject'"
    assert "words" in params, "Missing parameter 'words'"
    assert "bytes" in params, "Missing parameter 'bytes'"
    assert "paragraphs" in params, "Missing parameter 'paragraphs'"
    assert "manager" in params, "Missing parameter 'manager'"
    assert "appName" in params, "Missing parameter 'appName'"
    assert "characters" in params, "Missing parameter 'characters'"
    assert "category" in params, "Missing parameter 'category'"
    assert "presentationFormat" in params, "Missing parameter 'presentationFormat'"
    assert "totalTime" in params, "Missing parameter 'totalTime'"
    assert "keywords" in params, "Missing parameter 'keywords'"
    assert "company" in params, "Missing parameter 'company'"
    assert "charactersWithSpaces" in params, "Missing parameter 'charactersWithSpaces'"
    assert "description" in params, "Missing parameter 'description'"
    assert "title" in params, "Missing parameter 'title'"
    assert "revision" in params, "Missing parameter 'revision'"

def test_wordprocessingmltableelts_documentpropertiescollection_has_lines():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "lines")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "lines" in klass.__dict__:
            descriptor = klass.__dict__["lines"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_pages():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "pages")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_lastAuthor():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "lastAuthor")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "lastAuthor" in klass.__dict__:
            descriptor = klass.__dict__["lastAuthor"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_guid():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "guid")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "guid" in klass.__dict__:
            descriptor = klass.__dict__["guid"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_author():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "author")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_hyperlinkBase():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "hyperlinkBase")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "hyperlinkBase" in klass.__dict__:
            descriptor = klass.__dict__["hyperlinkBase"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_subject():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "subject")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "subject" in klass.__dict__:
            descriptor = klass.__dict__["subject"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_words():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "words")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "words" in klass.__dict__:
            descriptor = klass.__dict__["words"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_bytes():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "bytes")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "bytes" in klass.__dict__:
            descriptor = klass.__dict__["bytes"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_paragraphs():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "paragraphs")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "paragraphs" in klass.__dict__:
            descriptor = klass.__dict__["paragraphs"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_manager():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "manager")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "manager" in klass.__dict__:
            descriptor = klass.__dict__["manager"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_appName():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "appName")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "appName" in klass.__dict__:
            descriptor = klass.__dict__["appName"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_characters():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "characters")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "characters" in klass.__dict__:
            descriptor = klass.__dict__["characters"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_category():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "category")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_presentationFormat():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "presentationFormat")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "presentationFormat" in klass.__dict__:
            descriptor = klass.__dict__["presentationFormat"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_totalTime():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "totalTime")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "totalTime" in klass.__dict__:
            descriptor = klass.__dict__["totalTime"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_keywords():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "keywords")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "keywords" in klass.__dict__:
            descriptor = klass.__dict__["keywords"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_company():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "company")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "company" in klass.__dict__:
            descriptor = klass.__dict__["company"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_charactersWithSpaces():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "charactersWithSpaces")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "charactersWithSpaces" in klass.__dict__:
            descriptor = klass.__dict__["charactersWithSpaces"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_description():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "description")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "description" in klass.__dict__:
            descriptor = klass.__dict__["description"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_title():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "title")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_documentpropertiescollection_has_revision():
    assert hasattr(WordprocessingMLTableElts_DocumentPropertiesCollection, "revision")
    descriptor = None
    for klass in WordprocessingMLTableElts_DocumentPropertiesCollection.__mro__:
        if "revision" in klass.__dict__:
            descriptor = klass.__dict__["revision"]
            break
    assert isinstance(descriptor, property)



def test_valuetype_is_not_abstract():
    assert not inspect.isabstract(ValueType)


def test_valuetype_constructor_exists():
    assert callable(ValueType.__init__)


def test_valuetype_constructor_args():
    sig = inspect.signature(ValueType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_floatvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_FloatValue)


def test_wordprocessingmltableelts_floatvalue_constructor_exists():
    assert callable(WordprocessingMLTableElts_FloatValue.__init__)


def test_wordprocessingmltableelts_floatvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_FloatValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmltableelts_floatvalue_has_value():
    assert hasattr(WordprocessingMLTableElts_FloatValue, "value")
    descriptor = None
    for klass in WordprocessingMLTableElts_FloatValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts_booleanvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_BooleanValue)


def test_wordprocessingmltableelts_booleanvalue_constructor_exists():
    assert callable(WordprocessingMLTableElts_BooleanValue.__init__)


def test_wordprocessingmltableelts_booleanvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_BooleanValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmltableelts_booleanvalue_has_value():
    assert hasattr(WordprocessingMLTableElts_BooleanValue, "value")
    descriptor = None
    for klass in WordprocessingMLTableElts_BooleanValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts_stringvalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_StringValue)


def test_wordprocessingmltableelts_stringvalue_constructor_exists():
    assert callable(WordprocessingMLTableElts_StringValue.__init__)


def test_wordprocessingmltableelts_stringvalue_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_StringValue.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"

def test_wordprocessingmltableelts_stringvalue_has_value():
    assert hasattr(WordprocessingMLTableElts_StringValue, "value")
    descriptor = None
    for klass in WordprocessingMLTableElts_StringValue.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_wordprocessingmltableelts_valuetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_ValueType)


def test_wordprocessingmltableelts_valuetype_constructor_exists():
    assert callable(WordprocessingMLTableElts_ValueType.__init__)


def test_wordprocessingmltableelts_valuetype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_ValueType.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_versiontype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_VersionType)


def test_wordprocessingmltableelts_versiontype_constructor_exists():
    assert callable(WordprocessingMLTableElts_VersionType.__init__)


def test_wordprocessingmltableelts_versiontype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_VersionType.__init__)
    params = list(sig.parameters.keys())
    assert "nn" in params, "Missing parameter 'nn'"
    assert "n" in params, "Missing parameter 'n'"

def test_wordprocessingmltableelts_versiontype_has_nn():
    assert hasattr(WordprocessingMLTableElts_VersionType, "nn")
    descriptor = None
    for klass in WordprocessingMLTableElts_VersionType.__mro__:
        if "nn" in klass.__dict__:
            descriptor = klass.__dict__["nn"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_versiontype_has_n():
    assert hasattr(WordprocessingMLTableElts_VersionType, "n")
    descriptor = None
    for klass in WordprocessingMLTableElts_VersionType.__mro__:
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



def test_wordprocessingmltableelts_datetimetypevalue_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_DateTimeTypeValue)


def test_wordprocessingmltableelts_datetimetypevalue_constructor_exists():
    assert callable(WordprocessingMLTableElts_DateTimeTypeValue.__init__)


def test_wordprocessingmltableelts_datetimetypevalue_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_DateTimeTypeValue.__init__)
    params = list(sig.parameters.keys())



def test_wordprocessingmltableelts_datetimetype_is_not_abstract():
    assert not inspect.isabstract(WordprocessingMLTableElts_DateTimeType)


def test_wordprocessingmltableelts_datetimetype_constructor_exists():
    assert callable(WordprocessingMLTableElts_DateTimeType.__init__)


def test_wordprocessingmltableelts_datetimetype_constructor_args():
    sig = inspect.signature(WordprocessingMLTableElts_DateTimeType.__init__)
    params = list(sig.parameters.keys())
    assert "second" in params, "Missing parameter 'second'"
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "minute" in params, "Missing parameter 'minute'"
    assert "hour" in params, "Missing parameter 'hour'"
    assert "day" in params, "Missing parameter 'day'"

def test_wordprocessingmltableelts_datetimetype_has_second():
    assert hasattr(WordprocessingMLTableElts_DateTimeType, "second")
    descriptor = None
    for klass in WordprocessingMLTableElts_DateTimeType.__mro__:
        if "second" in klass.__dict__:
            descriptor = klass.__dict__["second"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_datetimetype_has_year():
    assert hasattr(WordprocessingMLTableElts_DateTimeType, "year")
    descriptor = None
    for klass in WordprocessingMLTableElts_DateTimeType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_datetimetype_has_month():
    assert hasattr(WordprocessingMLTableElts_DateTimeType, "month")
    descriptor = None
    for klass in WordprocessingMLTableElts_DateTimeType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_datetimetype_has_minute():
    assert hasattr(WordprocessingMLTableElts_DateTimeType, "minute")
    descriptor = None
    for klass in WordprocessingMLTableElts_DateTimeType.__mro__:
        if "minute" in klass.__dict__:
            descriptor = klass.__dict__["minute"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_datetimetype_has_hour():
    assert hasattr(WordprocessingMLTableElts_DateTimeType, "hour")
    descriptor = None
    for klass in WordprocessingMLTableElts_DateTimeType.__mro__:
        if "hour" in klass.__dict__:
            descriptor = klass.__dict__["hour"]
            break
    assert isinstance(descriptor, property)

def test_wordprocessingmltableelts_datetimetype_has_day():
    assert hasattr(WordprocessingMLTableElts_DateTimeType, "day")
    descriptor = None
    for klass in WordprocessingMLTableElts_DateTimeType.__mro__:
        if "day" in klass.__dict__:
            descriptor = klass.__dict__["day"]
            break
    assert isinstance(descriptor, property)

def test_breaktype_exists():
    # Check that the Enumeration exists
    assert BreakType is not None

def test_breaktype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BreakType]
    expected_literals = [
        "bt_page",
        "bt_column",
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
        "ftn_separator",
        "ftn_continuation_notice",
        "ftn_continuation_separator",
        "ftn_normal",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in NoteValue"

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
RunElt_strategy = st.builds(
    RunElt,
)
WordprocessingMLTableElts_RunPrElt_strategy = st.builds(
    WordprocessingMLTableElts_RunPrElt,
)
RunContentElt_strategy = st.builds(
    RunContentElt,
)
WordprocessingMLTableElts_NoBreakHyphen_strategy = st.builds(
    WordprocessingMLTableElts_NoBreakHyphen,
)
WordprocessingMLTableElts_SoftHyphen_strategy = st.builds(
    WordprocessingMLTableElts_SoftHyphen,
)
WordprocessingMLTableElts_AnnotationRef_strategy = st.builds(
    WordprocessingMLTableElts_AnnotationRef,
)
RunPrElt_strategy = st.builds(
    RunPrElt,
)
WordprocessingMLTableElts_ParaContentElt_strategy = st.builds(
    WordprocessingMLTableElts_ParaContentElt,
)
WordprocessingMLTableElts_RunContentElt_strategy = st.builds(
    WordprocessingMLTableElts_RunContentElt,
)
ParaContentElt_strategy = st.builds(
    ParaContentElt,
)
WordprocessingMLTableElts_RunElt_strategy = st.builds(
    WordprocessingMLTableElts_RunElt,
)
ParaPrElt_strategy = st.builds(
    ParaPrElt,
)
BlockLevelChunkElt_strategy = st.builds(
    BlockLevelChunkElt,
)
WordprocessingMLTableElts_ParaElt_strategy = st.builds(
    WordprocessingMLTableElts_ParaElt,
)
TableCellElt_strategy = st.builds(
    TableCellElt,
)
NoteElt_strategy = st.builds(
    NoteElt,
)
ParaElt_strategy = st.builds(
    ParaElt,
)
WordprocessingMLTableElts_ParaPrElt_strategy = st.builds(
    WordprocessingMLTableElts_ParaPrElt,
)
BlockLevelElt_strategy = st.builds(
    BlockLevelElt,
)
WordprocessingMLTableElts_BlockLevelChunkElt_strategy = st.builds(
    WordprocessingMLTableElts_BlockLevelChunkElt,
)
WordprocessingMLTableElts_BodyElt_strategy = st.builds(
    WordprocessingMLTableElts_BodyElt,
)
WordprocessingMLTableElts_DocPrElt_strategy = st.builds(
    WordprocessingMLTableElts_DocPrElt,
)
BodyElt_strategy = st.builds(
    BodyElt,
)
WordprocessingMLTableElts_BlockLevelElt_strategy = st.builds(
    WordprocessingMLTableElts_BlockLevelElt,
)
SectPrElt_strategy = st.builds(
    SectPrElt,
)
StylesElt_strategy = st.builds(
    StylesElt,
)
WordprocessingMLTableElts_TabElt_strategy = st.builds(
    WordprocessingMLTableElts_TabElt,
)
WordprocessingMLTableElts_PictureType_strategy = st.builds(
    WordprocessingMLTableElts_PictureType,
)
WordprocessingMLTableElts_SubDocElt_strategy = st.builds(
    WordprocessingMLTableElts_SubDocElt,
)
WordprocessingMLTableElts_RunLevelElt_strategy = st.builds(
    WordprocessingMLTableElts_RunLevelElt,
)
WordprocessingMLTableElts_SectPrElt_strategy = st.builds(
    WordprocessingMLTableElts_SectPrElt,
)
WordprocessingMLTableElts_HLinkElt_strategy = st.builds(
    WordprocessingMLTableElts_HLinkElt,
)
WordprocessingMLTableElts_SimpleFieldElt_strategy = st.builds(
    WordprocessingMLTableElts_SimpleFieldElt,
)
WordprocessingMLTableElts_CfChunk_strategy = st.builds(
    WordprocessingMLTableElts_CfChunk,
)
WordprocessingMLTableElts_ListsElt_strategy = st.builds(
    WordprocessingMLTableElts_ListsElt,
)
WordprocessingMLTableElts_FontsListElt_strategy = st.builds(
    WordprocessingMLTableElts_FontsListElt,
)
WordprocessingMLTableElts_TableCellPrElt_strategy = st.builds(
    WordprocessingMLTableElts_TableCellPrElt,
)
WordprocessingMLTableElts_StylesElt_strategy = st.builds(
    WordprocessingMLTableElts_StylesElt,
)
WordprocessingMLTableElts_TableCellElt_strategy = st.builds(
    WordprocessingMLTableElts_TableCellElt,
)
WordprocessingMLTableElts_RowContentElt_strategy = st.builds(
    WordprocessingMLTableElts_RowContentElt,
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
WordprocessingMLTableElts_RowElt_strategy = st.builds(
    WordprocessingMLTableElts_RowElt,
)
WordprocessingMLTableElts_TableRowPrElt_strategy = st.builds(
    WordprocessingMLTableElts_TableRowPrElt,
)
WordprocessingMLTableElts_TablePrExElt_strategy = st.builds(
    WordprocessingMLTableElts_TablePrExElt,
)
RowElt_strategy = st.builds(
    RowElt,
)
WordprocessingMLTableElts_TableContentElt_strategy = st.builds(
    WordprocessingMLTableElts_TableContentElt,
)
WordprocessingMLTableElts_TableGridElt_strategy = st.builds(
    WordprocessingMLTableElts_TableGridElt,
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
WordprocessingMLTableElts_TableElt_strategy = st.builds(
    WordprocessingMLTableElts_TableElt,
)
WordprocessingMLTableElts_TablePrElt_strategy = st.builds(
    WordprocessingMLTableElts_TablePrElt,
)
TableContentElt_strategy = st.builds(
    TableContentElt,
)
WordprocessingMLTableElts_FldCharElt_strategy = st.builds(
    WordprocessingMLTableElts_FldCharElt,
    fldCharType=
        st.none(),
    fldLock=
        st.none()
)
FldCharElt_strategy = st.builds(
    FldCharElt,
)
WordprocessingMLTableElts_FldChar_strategy = st.builds(
    WordprocessingMLTableElts_FldChar,
)
TabElt_strategy = st.builds(
    TabElt,
)
WordprocessingMLTableElts_Tab_strategy = st.builds(
    WordprocessingMLTableElts_Tab,
)
WordprocessingMLTableElts_SymElt_strategy = st.builds(
    WordprocessingMLTableElts_SymElt,
)
WordprocessingMLTableElts_NoteElt_strategy = st.builds(
    WordprocessingMLTableElts_NoteElt,
    type=
        st.none(),
    suppressRef=
        st.none()
)
WordprocessingMLTableElts_Endnote_strategy = st.builds(
    WordprocessingMLTableElts_Endnote,
)
WordprocessingMLTableElts_Footnote_strategy = st.builds(
    WordprocessingMLTableElts_Footnote,
)
WordprocessingMLTableElts_Cr_strategy = st.builds(
    WordprocessingMLTableElts_Cr,
)
WordprocessingMLTableElts_PgNum_strategy = st.builds(
    WordprocessingMLTableElts_PgNum,
)
WordprocessingMLTableElts_ContinuationSeparator_strategy = st.builds(
    WordprocessingMLTableElts_ContinuationSeparator,
)
WordprocessingMLTableElts_Separator_strategy = st.builds(
    WordprocessingMLTableElts_Separator,
)
WordprocessingMLTableElts_EndnoteRef_strategy = st.builds(
    WordprocessingMLTableElts_EndnoteRef,
)
SymElt_strategy = st.builds(
    SymElt,
)
WordprocessingMLTableElts_Symbol_strategy = st.builds(
    WordprocessingMLTableElts_Symbol,
)
PictureType_strategy = st.builds(
    PictureType,
)
WordprocessingMLTableElts_Picture_strategy = st.builds(
    WordprocessingMLTableElts_Picture,
)
WordprocessingMLTableElts_BreakElt_strategy = st.builds(
    WordprocessingMLTableElts_BreakElt,
    type=
        st.none()
)
WordprocessingMLTableElts_FootnoteRef_strategy = st.builds(
    WordprocessingMLTableElts_FootnoteRef,
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
WordprocessingMLTableElts_WordDocument_strategy = st.builds(
    WordprocessingMLTableElts_WordDocument,
)
StringProperty_strategy = st.builds(
    StringProperty,
)
WordprocessingMLTableElts_StringType_strategy = st.builds(
    WordprocessingMLTableElts_StringType,
    val=
        st.none()
)
StringType_strategy = st.builds(
    StringType,
)
WordprocessingMLTableElts_DelText_strategy = st.builds(
    WordprocessingMLTableElts_DelText,
)
WordprocessingMLTableElts_Text_strategy = st.builds(
    WordprocessingMLTableElts_Text,
)
WordprocessingMLTableElts_InstrText_strategy = st.builds(
    WordprocessingMLTableElts_InstrText,
)
WordprocessingMLTableElts_DelInstrText_strategy = st.builds(
    WordprocessingMLTableElts_DelInstrText,
)
WordprocessingMLTableElts_StringProperty_strategy = st.builds(
    WordprocessingMLTableElts_StringProperty,
)
SmartTagType_strategy = st.builds(
    SmartTagType,
)
WordprocessingMLTableElts_SmartTagsCollection_strategy = st.builds(
    WordprocessingMLTableElts_SmartTagsCollection,
)
CustomDocumentPropertiesCollection_strategy = st.builds(
    CustomDocumentPropertiesCollection,
)
WordprocessingMLTableElts_CustomDocumentProperty_strategy = st.builds(
    WordprocessingMLTableElts_CustomDocumentProperty,
    name=
        st.none()
)
CustomDocumentProperty_strategy = st.builds(
    CustomDocumentProperty,
)
SmartTagsCollection_strategy = st.builds(
    SmartTagsCollection,
)
WordprocessingMLTableElts_SmartTagType_strategy = st.builds(
    WordprocessingMLTableElts_SmartTagType,
    name=
        st.none(),
    url=
        st.none(),
    namespaceuri=
        st.none()
)
WordprocessingMLTableElts_CustomDocumentPropertiesCollection_strategy = st.builds(
    WordprocessingMLTableElts_CustomDocumentPropertiesCollection,
)
VersionType_strategy = st.builds(
    VersionType,
)
WordDocument_strategy = st.builds(
    WordDocument,
)
WordprocessingMLTableElts_DocumentPropertiesCollection_strategy = st.builds(
    WordprocessingMLTableElts_DocumentPropertiesCollection,
    lines=
        st.none(),
    pages=
        st.none(),
    lastAuthor=
        st.none(),
    guid=
        st.none(),
    author=
        st.none(),
    hyperlinkBase=
        st.none(),
    subject=
        st.none(),
    words=
        st.none(),
    bytes=
        st.none(),
    paragraphs=
        st.none(),
    manager=
        st.none(),
    appName=
        st.none(),
    characters=
        st.none(),
    category=
        st.none(),
    presentationFormat=
        st.none(),
    totalTime=
        st.none(),
    keywords=
        st.none(),
    company=
        st.none(),
    charactersWithSpaces=
        st.none(),
    description=
        st.none(),
    title=
        st.none(),
    revision=
        st.none()
)
ValueType_strategy = st.builds(
    ValueType,
)
WordprocessingMLTableElts_FloatValue_strategy = st.builds(
    WordprocessingMLTableElts_FloatValue,
    value=
        st.none()
)
WordprocessingMLTableElts_BooleanValue_strategy = st.builds(
    WordprocessingMLTableElts_BooleanValue,
    value=
        st.none()
)
WordprocessingMLTableElts_StringValue_strategy = st.builds(
    WordprocessingMLTableElts_StringValue,
    value=
        st.none()
)
WordprocessingMLTableElts_ValueType_strategy = st.builds(
    WordprocessingMLTableElts_ValueType,
)
WordprocessingMLTableElts_VersionType_strategy = st.builds(
    WordprocessingMLTableElts_VersionType,
    nn=
        st.none(),
    n=
        st.none()
)
DateTimeType_strategy = st.builds(
    DateTimeType,
)
WordprocessingMLTableElts_DateTimeTypeValue_strategy = st.builds(
    WordprocessingMLTableElts_DateTimeTypeValue,
)
WordprocessingMLTableElts_DateTimeType_strategy = st.builds(
    WordprocessingMLTableElts_DateTimeType,
    second=
        st.none(),
    year=
        st.none(),
    month=
        st.none(),
    minute=
        st.none(),
    hour=
        st.none(),
    day=
        st.none()
)

@given(instance=RunElt_strategy)
@settings(max_examples=50)
def test_runelt_instantiation(instance):
    assert isinstance(instance, RunElt)

@given(instance=WordprocessingMLTableElts_RunPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_runprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_RunPrElt)

@given(instance=RunContentElt_strategy)
@settings(max_examples=50)
def test_runcontentelt_instantiation(instance):
    assert isinstance(instance, RunContentElt)

@given(instance=WordprocessingMLTableElts_NoBreakHyphen_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_nobreakhyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_NoBreakHyphen)

@given(instance=WordprocessingMLTableElts_SoftHyphen_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_softhyphen_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_SoftHyphen)

@given(instance=WordprocessingMLTableElts_AnnotationRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_annotationref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_AnnotationRef)

@given(instance=RunPrElt_strategy)
@settings(max_examples=50)
def test_runprelt_instantiation(instance):
    assert isinstance(instance, RunPrElt)

@given(instance=WordprocessingMLTableElts_ParaContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_paracontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_ParaContentElt)

@given(instance=WordprocessingMLTableElts_RunContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_runcontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_RunContentElt)

@given(instance=ParaContentElt_strategy)
@settings(max_examples=50)
def test_paracontentelt_instantiation(instance):
    assert isinstance(instance, ParaContentElt)

@given(instance=WordprocessingMLTableElts_RunElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_runelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_RunElt)

@given(instance=ParaPrElt_strategy)
@settings(max_examples=50)
def test_paraprelt_instantiation(instance):
    assert isinstance(instance, ParaPrElt)

@given(instance=BlockLevelChunkElt_strategy)
@settings(max_examples=50)
def test_blocklevelchunkelt_instantiation(instance):
    assert isinstance(instance, BlockLevelChunkElt)

@given(instance=WordprocessingMLTableElts_ParaElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_paraelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_ParaElt)

@given(instance=TableCellElt_strategy)
@settings(max_examples=50)
def test_tablecellelt_instantiation(instance):
    assert isinstance(instance, TableCellElt)

@given(instance=NoteElt_strategy)
@settings(max_examples=50)
def test_noteelt_instantiation(instance):
    assert isinstance(instance, NoteElt)

@given(instance=ParaElt_strategy)
@settings(max_examples=50)
def test_paraelt_instantiation(instance):
    assert isinstance(instance, ParaElt)

@given(instance=WordprocessingMLTableElts_ParaPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_paraprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_ParaPrElt)

@given(instance=BlockLevelElt_strategy)
@settings(max_examples=50)
def test_blocklevelelt_instantiation(instance):
    assert isinstance(instance, BlockLevelElt)

@given(instance=WordprocessingMLTableElts_BlockLevelChunkElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_blocklevelchunkelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_BlockLevelChunkElt)

@given(instance=WordprocessingMLTableElts_BodyElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_bodyelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_BodyElt)

@given(instance=WordprocessingMLTableElts_DocPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_docprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_DocPrElt)

@given(instance=BodyElt_strategy)
@settings(max_examples=50)
def test_bodyelt_instantiation(instance):
    assert isinstance(instance, BodyElt)

@given(instance=WordprocessingMLTableElts_BlockLevelElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_blocklevelelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_BlockLevelElt)

@given(instance=SectPrElt_strategy)
@settings(max_examples=50)
def test_sectprelt_instantiation(instance):
    assert isinstance(instance, SectPrElt)

@given(instance=StylesElt_strategy)
@settings(max_examples=50)
def test_styleselt_instantiation(instance):
    assert isinstance(instance, StylesElt)

@given(instance=WordprocessingMLTableElts_TabElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tabelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TabElt)

@given(instance=WordprocessingMLTableElts_PictureType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_picturetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_PictureType)

@given(instance=WordprocessingMLTableElts_SubDocElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_subdocelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_SubDocElt)

@given(instance=WordprocessingMLTableElts_RunLevelElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_runlevelelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_RunLevelElt)

@given(instance=WordprocessingMLTableElts_SectPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_sectprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_SectPrElt)

@given(instance=WordprocessingMLTableElts_HLinkElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_hlinkelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_HLinkElt)

@given(instance=WordprocessingMLTableElts_SimpleFieldElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_simplefieldelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_SimpleFieldElt)

@given(instance=WordprocessingMLTableElts_CfChunk_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_cfchunk_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_CfChunk)

@given(instance=WordprocessingMLTableElts_ListsElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_listselt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_ListsElt)

@given(instance=WordprocessingMLTableElts_FontsListElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_fontslistelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_FontsListElt)

@given(instance=WordprocessingMLTableElts_TableCellPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tablecellprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TableCellPrElt)

@given(instance=WordprocessingMLTableElts_StylesElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_styleselt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_StylesElt)

@given(instance=WordprocessingMLTableElts_TableCellElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tablecellelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TableCellElt)

@given(instance=WordprocessingMLTableElts_RowContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_rowcontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_RowContentElt)

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

@given(instance=WordprocessingMLTableElts_RowElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_rowelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_RowElt)

@given(instance=WordprocessingMLTableElts_TableRowPrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tablerowprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TableRowPrElt)

@given(instance=WordprocessingMLTableElts_TablePrExElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tableprexelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TablePrExElt)

@given(instance=RowElt_strategy)
@settings(max_examples=50)
def test_rowelt_instantiation(instance):
    assert isinstance(instance, RowElt)

@given(instance=WordprocessingMLTableElts_TableContentElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tablecontentelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TableContentElt)

@given(instance=WordprocessingMLTableElts_TableGridElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tablegridelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TableGridElt)

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

@given(instance=WordprocessingMLTableElts_TableElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tableelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TableElt)

@given(instance=WordprocessingMLTableElts_TablePrElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tableprelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_TablePrElt)

@given(instance=TableContentElt_strategy)
@settings(max_examples=50)
def test_tablecontentelt_instantiation(instance):
    assert isinstance(instance, TableContentElt)

@given(instance=WordprocessingMLTableElts_FldCharElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_fldcharelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_FldCharElt)



@given(instance=WordprocessingMLTableElts_FldCharElt_strategy)
def test_wordprocessingmltableelts_fldcharelt_fldCharType_setter(instance):
    original = instance.fldCharType
    instance.fldCharType = original
    assert instance.fldCharType == original



@given(instance=WordprocessingMLTableElts_FldCharElt_strategy)
def test_wordprocessingmltableelts_fldcharelt_fldLock_setter(instance):
    original = instance.fldLock
    instance.fldLock = original
    assert instance.fldLock == original

@given(instance=FldCharElt_strategy)
@settings(max_examples=50)
def test_fldcharelt_instantiation(instance):
    assert isinstance(instance, FldCharElt)

@given(instance=WordprocessingMLTableElts_FldChar_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_fldchar_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_FldChar)

@given(instance=TabElt_strategy)
@settings(max_examples=50)
def test_tabelt_instantiation(instance):
    assert isinstance(instance, TabElt)

@given(instance=WordprocessingMLTableElts_Tab_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_tab_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_Tab)

@given(instance=WordprocessingMLTableElts_SymElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_symelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_SymElt)

@given(instance=WordprocessingMLTableElts_NoteElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_noteelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_NoteElt)



@given(instance=WordprocessingMLTableElts_NoteElt_strategy)
def test_wordprocessingmltableelts_noteelt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=WordprocessingMLTableElts_NoteElt_strategy)
def test_wordprocessingmltableelts_noteelt_suppressRef_setter(instance):
    original = instance.suppressRef
    instance.suppressRef = original
    assert instance.suppressRef == original

@given(instance=WordprocessingMLTableElts_Endnote_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_endnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_Endnote)

@given(instance=WordprocessingMLTableElts_Footnote_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_footnote_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_Footnote)

@given(instance=WordprocessingMLTableElts_Cr_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_cr_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_Cr)

@given(instance=WordprocessingMLTableElts_PgNum_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_pgnum_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_PgNum)

@given(instance=WordprocessingMLTableElts_ContinuationSeparator_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_continuationseparator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_ContinuationSeparator)

@given(instance=WordprocessingMLTableElts_Separator_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_separator_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_Separator)

@given(instance=WordprocessingMLTableElts_EndnoteRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_endnoteref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_EndnoteRef)

@given(instance=SymElt_strategy)
@settings(max_examples=50)
def test_symelt_instantiation(instance):
    assert isinstance(instance, SymElt)

@given(instance=WordprocessingMLTableElts_Symbol_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_symbol_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_Symbol)

@given(instance=PictureType_strategy)
@settings(max_examples=50)
def test_picturetype_instantiation(instance):
    assert isinstance(instance, PictureType)

@given(instance=WordprocessingMLTableElts_Picture_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_picture_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_Picture)

@given(instance=WordprocessingMLTableElts_BreakElt_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_breakelt_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_BreakElt)



@given(instance=WordprocessingMLTableElts_BreakElt_strategy)
def test_wordprocessingmltableelts_breakelt_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=WordprocessingMLTableElts_FootnoteRef_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_footnoteref_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_FootnoteRef)

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

@given(instance=WordprocessingMLTableElts_WordDocument_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_worddocument_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_WordDocument)

@given(instance=StringProperty_strategy)
@settings(max_examples=50)
def test_stringproperty_instantiation(instance):
    assert isinstance(instance, StringProperty)

@given(instance=WordprocessingMLTableElts_StringType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_stringtype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_StringType)



@given(instance=WordprocessingMLTableElts_StringType_strategy)
def test_wordprocessingmltableelts_stringtype_val_setter(instance):
    original = instance.val
    instance.val = original
    assert instance.val == original

@given(instance=StringType_strategy)
@settings(max_examples=50)
def test_stringtype_instantiation(instance):
    assert isinstance(instance, StringType)

@given(instance=WordprocessingMLTableElts_DelText_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_deltext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_DelText)

@given(instance=WordprocessingMLTableElts_Text_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_text_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_Text)

@given(instance=WordprocessingMLTableElts_InstrText_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_instrtext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_InstrText)

@given(instance=WordprocessingMLTableElts_DelInstrText_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_delinstrtext_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_DelInstrText)

@given(instance=WordprocessingMLTableElts_StringProperty_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_stringproperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_StringProperty)

@given(instance=SmartTagType_strategy)
@settings(max_examples=50)
def test_smarttagtype_instantiation(instance):
    assert isinstance(instance, SmartTagType)

@given(instance=WordprocessingMLTableElts_SmartTagsCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_smarttagscollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_SmartTagsCollection)

@given(instance=CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, CustomDocumentPropertiesCollection)

@given(instance=WordprocessingMLTableElts_CustomDocumentProperty_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_customdocumentproperty_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_CustomDocumentProperty)



@given(instance=WordprocessingMLTableElts_CustomDocumentProperty_strategy)
def test_wordprocessingmltableelts_customdocumentproperty_name_setter(instance):
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

@given(instance=WordprocessingMLTableElts_SmartTagType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_smarttagtype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_SmartTagType)



@given(instance=WordprocessingMLTableElts_SmartTagType_strategy)
def test_wordprocessingmltableelts_smarttagtype_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=WordprocessingMLTableElts_SmartTagType_strategy)
def test_wordprocessingmltableelts_smarttagtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=WordprocessingMLTableElts_SmartTagType_strategy)
def test_wordprocessingmltableelts_smarttagtype_namespaceuri_setter(instance):
    original = instance.namespaceuri
    instance.namespaceuri = original
    assert instance.namespaceuri == original

@given(instance=WordprocessingMLTableElts_CustomDocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_customdocumentpropertiescollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_CustomDocumentPropertiesCollection)

@given(instance=VersionType_strategy)
@settings(max_examples=50)
def test_versiontype_instantiation(instance):
    assert isinstance(instance, VersionType)

@given(instance=WordDocument_strategy)
@settings(max_examples=50)
def test_worddocument_instantiation(instance):
    assert isinstance(instance, WordDocument)

@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_documentpropertiescollection_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_DocumentPropertiesCollection)



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_lines_setter(instance):
    original = instance.lines
    instance.lines = original
    assert instance.lines == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_lastAuthor_setter(instance):
    original = instance.lastAuthor
    instance.lastAuthor = original
    assert instance.lastAuthor == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_guid_setter(instance):
    original = instance.guid
    instance.guid = original
    assert instance.guid == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_hyperlinkBase_setter(instance):
    original = instance.hyperlinkBase
    instance.hyperlinkBase = original
    assert instance.hyperlinkBase == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_subject_setter(instance):
    original = instance.subject
    instance.subject = original
    assert instance.subject == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_words_setter(instance):
    original = instance.words
    instance.words = original
    assert instance.words == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_bytes_setter(instance):
    original = instance.bytes
    instance.bytes = original
    assert instance.bytes == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_paragraphs_setter(instance):
    original = instance.paragraphs
    instance.paragraphs = original
    assert instance.paragraphs == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_manager_setter(instance):
    original = instance.manager
    instance.manager = original
    assert instance.manager == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_appName_setter(instance):
    original = instance.appName
    instance.appName = original
    assert instance.appName == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_characters_setter(instance):
    original = instance.characters
    instance.characters = original
    assert instance.characters == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_presentationFormat_setter(instance):
    original = instance.presentationFormat
    instance.presentationFormat = original
    assert instance.presentationFormat == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_totalTime_setter(instance):
    original = instance.totalTime
    instance.totalTime = original
    assert instance.totalTime == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_keywords_setter(instance):
    original = instance.keywords
    instance.keywords = original
    assert instance.keywords == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_company_setter(instance):
    original = instance.company
    instance.company = original
    assert instance.company == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_charactersWithSpaces_setter(instance):
    original = instance.charactersWithSpaces
    instance.charactersWithSpaces = original
    assert instance.charactersWithSpaces == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_description_setter(instance):
    original = instance.description
    instance.description = original
    assert instance.description == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=WordprocessingMLTableElts_DocumentPropertiesCollection_strategy)
def test_wordprocessingmltableelts_documentpropertiescollection_revision_setter(instance):
    original = instance.revision
    instance.revision = original
    assert instance.revision == original

@given(instance=ValueType_strategy)
@settings(max_examples=50)
def test_valuetype_instantiation(instance):
    assert isinstance(instance, ValueType)

@given(instance=WordprocessingMLTableElts_FloatValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_floatvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_FloatValue)



@given(instance=WordprocessingMLTableElts_FloatValue_strategy)
def test_wordprocessingmltableelts_floatvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLTableElts_BooleanValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_booleanvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_BooleanValue)



@given(instance=WordprocessingMLTableElts_BooleanValue_strategy)
def test_wordprocessingmltableelts_booleanvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLTableElts_StringValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_stringvalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_StringValue)



@given(instance=WordprocessingMLTableElts_StringValue_strategy)
def test_wordprocessingmltableelts_stringvalue_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=WordprocessingMLTableElts_ValueType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_valuetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_ValueType)

@given(instance=WordprocessingMLTableElts_VersionType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_versiontype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_VersionType)



@given(instance=WordprocessingMLTableElts_VersionType_strategy)
def test_wordprocessingmltableelts_versiontype_nn_setter(instance):
    original = instance.nn
    instance.nn = original
    assert instance.nn == original



@given(instance=WordprocessingMLTableElts_VersionType_strategy)
def test_wordprocessingmltableelts_versiontype_n_setter(instance):
    original = instance.n
    instance.n = original
    assert instance.n == original

@given(instance=DateTimeType_strategy)
@settings(max_examples=50)
def test_datetimetype_instantiation(instance):
    assert isinstance(instance, DateTimeType)

@given(instance=WordprocessingMLTableElts_DateTimeTypeValue_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_datetimetypevalue_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_DateTimeTypeValue)

@given(instance=WordprocessingMLTableElts_DateTimeType_strategy)
@settings(max_examples=50)
def test_wordprocessingmltableelts_datetimetype_instantiation(instance):
    assert isinstance(instance, WordprocessingMLTableElts_DateTimeType)



@given(instance=WordprocessingMLTableElts_DateTimeType_strategy)
def test_wordprocessingmltableelts_datetimetype_second_setter(instance):
    original = instance.second
    instance.second = original
    assert instance.second == original



@given(instance=WordprocessingMLTableElts_DateTimeType_strategy)
def test_wordprocessingmltableelts_datetimetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=WordprocessingMLTableElts_DateTimeType_strategy)
def test_wordprocessingmltableelts_datetimetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=WordprocessingMLTableElts_DateTimeType_strategy)
def test_wordprocessingmltableelts_datetimetype_minute_setter(instance):
    original = instance.minute
    instance.minute = original
    assert instance.minute == original



@given(instance=WordprocessingMLTableElts_DateTimeType_strategy)
def test_wordprocessingmltableelts_datetimetype_hour_setter(instance):
    original = instance.hour
    instance.hour = original
    assert instance.hour == original



@given(instance=WordprocessingMLTableElts_DateTimeType_strategy)
def test_wordprocessingmltableelts_datetimetype_day_setter(instance):
    original = instance.day
    instance.day = original
    assert instance.day == original
