import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Docbook_VarListEntryType,
    Docbook_TermType,
    Docbook_SegType,
    Docbook_SegListItemType,
    Docbook_RevdescriptionType,
    Docbook_RevnumberType,
    Docbook_RevisionType,
    Docbook_SegmentedListType,
    Docbook_RefEntryTitleType,
    Docbook_RefSect1Type,
    Docbook_RefSynopsisDivType,
    Docbook_RefNameDivType,
    Docbook_RefMetaType,
    Docbook_RefEntryType,
    Docbook_SurnameType,
    Docbook_VariableListType,
    ItemizedlistType,
    Docbook_ParameterType,
    Docbook_RevhistoryType,
    Docbook_LegalNoticeType,
    Docbook_SubtitleType,
    Docbook_ParamdefType,
    Docbook_FuncprototypeType,
    Docbook_FuncsynopsisType,
    Docbook_FileNameType,
    Docbook_FunctionType,
    Docbook_FuncdefType,
    Docbook_FirstnameType,
    Docbook_EnvarType,
    Docbook_ExampleType,
    Docbook_TheadType,
    Docbook_TgroupType,
    Docbook_UlinkType,
    Docbook_TipType,
    Docbook_TbodyType,
    Docbook_TableType,
    Docbook_ProgramlistingType,
    Docbook_RowType,
    Docbook_PhraseType,
    Docbook_PublisherType,
    Docbook_OrderedlistType,
    Docbook_MediaobjectType,
    Docbook_ListitemType,
    Docbook_LinkType,
    Docbook_KeywordsetType,
    Docbook_LiteralType,
    Docbook_ImportantType,
    Docbook_ImageobjectType,
    Docbook_ImagedataType,
    Docbook_FootnoteType,
    Docbook_ItemizedlistType,
    Docbook_InformaltableType,
    Docbook_FigureType,
    Docbook_EntryType,
    Docbook_EmphasisType,
    Docbook_DateType,
    Docbook_CopyrightType,
    Docbook_ConfgroupType,
    Docbook_EStringToStringMapEntry,
    Docbook_DocumentRoot,
    Docbook_CommandType,
    Docbook_CmdsynopsisType,
    Docbook_ColspecType,
    Docbook_SectionType,
    Docbook_NoteType,
    Docbook_ReferenceType,
    Docbook_ChapterType,
    Docbook_PrefaceType,
    Docbook_InfoType,
    Docbook_BookType,
    Docbook_TitleType,
    Docbook_OtheraddrType,
    Docbook_PersonnameType,
    Docbook_AuthorType,
    Docbook_AuthorinitialsType,
    Docbook_ReplaceableType,
    Docbook_OptionType,
    Docbook_ArgType,
    Docbook_AddressType,
    Docbook_ParaType,
    Docbook_AbstractType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_docbook_varlistentrytype_is_not_abstract():
    assert not inspect.isabstract(Docbook_VarListEntryType)


def test_docbook_varlistentrytype_constructor_exists():
    assert callable(Docbook_VarListEntryType.__init__)


def test_docbook_varlistentrytype_constructor_args():
    sig = inspect.signature(Docbook_VarListEntryType.__init__)
    params = list(sig.parameters.keys())
    assert "termlength" in params, "Missing parameter 'termlength'"
    assert "spacing" in params, "Missing parameter 'spacing'"

def test_docbook_varlistentrytype_has_termlength():
    assert hasattr(Docbook_VarListEntryType, "termlength")
    descriptor = None
    for klass in Docbook_VarListEntryType.__mro__:
        if "termlength" in klass.__dict__:
            descriptor = klass.__dict__["termlength"]
            break
    assert isinstance(descriptor, property)

def test_docbook_varlistentrytype_has_spacing():
    assert hasattr(Docbook_VarListEntryType, "spacing")
    descriptor = None
    for klass in Docbook_VarListEntryType.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)



def test_docbook_termtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_TermType)


def test_docbook_termtype_constructor_exists():
    assert callable(Docbook_TermType.__init__)


def test_docbook_termtype_constructor_args():
    sig = inspect.signature(Docbook_TermType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_termtype_has_mixed():
    assert hasattr(Docbook_TermType, "mixed")
    descriptor = None
    for klass in Docbook_TermType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_segtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_SegType)


def test_docbook_segtype_constructor_exists():
    assert callable(Docbook_SegType.__init__)


def test_docbook_segtype_constructor_args():
    sig = inspect.signature(Docbook_SegType.__init__)
    params = list(sig.parameters.keys())
    assert "errortext" in params, "Missing parameter 'errortext'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"
    assert "errorcode" in params, "Missing parameter 'errorcode'"

def test_docbook_segtype_has_errortext():
    assert hasattr(Docbook_SegType, "errortext")
    descriptor = None
    for klass in Docbook_SegType.__mro__:
        if "errortext" in klass.__dict__:
            descriptor = klass.__dict__["errortext"]
            break
    assert isinstance(descriptor, property)

def test_docbook_segtype_has_mixed():
    assert hasattr(Docbook_SegType, "mixed")
    descriptor = None
    for klass in Docbook_SegType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook_segtype_has_group():
    assert hasattr(Docbook_SegType, "group")
    descriptor = None
    for klass in Docbook_SegType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook_segtype_has_errorcode():
    assert hasattr(Docbook_SegType, "errorcode")
    descriptor = None
    for klass in Docbook_SegType.__mro__:
        if "errorcode" in klass.__dict__:
            descriptor = klass.__dict__["errorcode"]
            break
    assert isinstance(descriptor, property)



def test_docbook_seglistitemtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_SegListItemType)


def test_docbook_seglistitemtype_constructor_exists():
    assert callable(Docbook_SegListItemType.__init__)


def test_docbook_seglistitemtype_constructor_args():
    sig = inspect.signature(Docbook_SegListItemType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_revdescriptiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RevdescriptionType)


def test_docbook_revdescriptiontype_constructor_exists():
    assert callable(Docbook_RevdescriptionType.__init__)


def test_docbook_revdescriptiontype_constructor_args():
    sig = inspect.signature(Docbook_RevdescriptionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_revdescriptiontype_has_mixed():
    assert hasattr(Docbook_RevdescriptionType, "mixed")
    descriptor = None
    for klass in Docbook_RevdescriptionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_revnumbertype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RevnumberType)


def test_docbook_revnumbertype_constructor_exists():
    assert callable(Docbook_RevnumberType.__init__)


def test_docbook_revnumbertype_constructor_args():
    sig = inspect.signature(Docbook_RevnumberType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_revnumbertype_has_mixed():
    assert hasattr(Docbook_RevnumberType, "mixed")
    descriptor = None
    for klass in Docbook_RevnumberType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_revisiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RevisionType)


def test_docbook_revisiontype_constructor_exists():
    assert callable(Docbook_RevisionType.__init__)


def test_docbook_revisiontype_constructor_args():
    sig = inspect.signature(Docbook_RevisionType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_segmentedlisttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_SegmentedListType)


def test_docbook_segmentedlisttype_constructor_exists():
    assert callable(Docbook_SegmentedListType.__init__)


def test_docbook_segmentedlisttype_constructor_args():
    sig = inspect.signature(Docbook_SegmentedListType.__init__)
    params = list(sig.parameters.keys())
    assert "segtitle" in params, "Missing parameter 'segtitle'"
    assert "group" in params, "Missing parameter 'group'"

def test_docbook_segmentedlisttype_has_segtitle():
    assert hasattr(Docbook_SegmentedListType, "segtitle")
    descriptor = None
    for klass in Docbook_SegmentedListType.__mro__:
        if "segtitle" in klass.__dict__:
            descriptor = klass.__dict__["segtitle"]
            break
    assert isinstance(descriptor, property)

def test_docbook_segmentedlisttype_has_group():
    assert hasattr(Docbook_SegmentedListType, "group")
    descriptor = None
    for klass in Docbook_SegmentedListType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook_refentrytitletype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RefEntryTitleType)


def test_docbook_refentrytitletype_constructor_exists():
    assert callable(Docbook_RefEntryTitleType.__init__)


def test_docbook_refentrytitletype_constructor_args():
    sig = inspect.signature(Docbook_RefEntryTitleType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_refentrytitletype_has_mixed():
    assert hasattr(Docbook_RefEntryTitleType, "mixed")
    descriptor = None
    for klass in Docbook_RefEntryTitleType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_refsect1type_is_not_abstract():
    assert not inspect.isabstract(Docbook_RefSect1Type)


def test_docbook_refsect1type_constructor_exists():
    assert callable(Docbook_RefSect1Type.__init__)


def test_docbook_refsect1type_constructor_args():
    sig = inspect.signature(Docbook_RefSect1Type.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "id" in params, "Missing parameter 'id'"

def test_docbook_refsect1type_has_group():
    assert hasattr(Docbook_RefSect1Type, "group")
    descriptor = None
    for klass in Docbook_RefSect1Type.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook_refsect1type_has_id():
    assert hasattr(Docbook_RefSect1Type, "id")
    descriptor = None
    for klass in Docbook_RefSect1Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook_refsynopsisdivtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RefSynopsisDivType)


def test_docbook_refsynopsisdivtype_constructor_exists():
    assert callable(Docbook_RefSynopsisDivType.__init__)


def test_docbook_refsynopsisdivtype_constructor_args():
    sig = inspect.signature(Docbook_RefSynopsisDivType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_refnamedivtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RefNameDivType)


def test_docbook_refnamedivtype_constructor_exists():
    assert callable(Docbook_RefNameDivType.__init__)


def test_docbook_refnamedivtype_constructor_args():
    sig = inspect.signature(Docbook_RefNameDivType.__init__)
    params = list(sig.parameters.keys())
    assert "refclass" in params, "Missing parameter 'refclass'"
    assert "refpurpose" in params, "Missing parameter 'refpurpose'"
    assert "refname" in params, "Missing parameter 'refname'"

def test_docbook_refnamedivtype_has_refclass():
    assert hasattr(Docbook_RefNameDivType, "refclass")
    descriptor = None
    for klass in Docbook_RefNameDivType.__mro__:
        if "refclass" in klass.__dict__:
            descriptor = klass.__dict__["refclass"]
            break
    assert isinstance(descriptor, property)

def test_docbook_refnamedivtype_has_refpurpose():
    assert hasattr(Docbook_RefNameDivType, "refpurpose")
    descriptor = None
    for klass in Docbook_RefNameDivType.__mro__:
        if "refpurpose" in klass.__dict__:
            descriptor = klass.__dict__["refpurpose"]
            break
    assert isinstance(descriptor, property)

def test_docbook_refnamedivtype_has_refname():
    assert hasattr(Docbook_RefNameDivType, "refname")
    descriptor = None
    for klass in Docbook_RefNameDivType.__mro__:
        if "refname" in klass.__dict__:
            descriptor = klass.__dict__["refname"]
            break
    assert isinstance(descriptor, property)



def test_docbook_refmetatype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RefMetaType)


def test_docbook_refmetatype_constructor_exists():
    assert callable(Docbook_RefMetaType.__init__)


def test_docbook_refmetatype_constructor_args():
    sig = inspect.signature(Docbook_RefMetaType.__init__)
    params = list(sig.parameters.keys())
    assert "manvolnum" in params, "Missing parameter 'manvolnum'"

def test_docbook_refmetatype_has_manvolnum():
    assert hasattr(Docbook_RefMetaType, "manvolnum")
    descriptor = None
    for klass in Docbook_RefMetaType.__mro__:
        if "manvolnum" in klass.__dict__:
            descriptor = klass.__dict__["manvolnum"]
            break
    assert isinstance(descriptor, property)



def test_docbook_refentrytype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RefEntryType)


def test_docbook_refentrytype_constructor_exists():
    assert callable(Docbook_RefEntryType.__init__)


def test_docbook_refentrytype_constructor_args():
    sig = inspect.signature(Docbook_RefEntryType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_docbook_refentrytype_has_version():
    assert hasattr(Docbook_RefEntryType, "version")
    descriptor = None
    for klass in Docbook_RefEntryType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_docbook_surnametype_is_not_abstract():
    assert not inspect.isabstract(Docbook_SurnameType)


def test_docbook_surnametype_constructor_exists():
    assert callable(Docbook_SurnameType.__init__)


def test_docbook_surnametype_constructor_args():
    sig = inspect.signature(Docbook_SurnameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_surnametype_has_mixed():
    assert hasattr(Docbook_SurnameType, "mixed")
    descriptor = None
    for klass in Docbook_SurnameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_variablelisttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_VariableListType)


def test_docbook_variablelisttype_constructor_exists():
    assert callable(Docbook_VariableListType.__init__)


def test_docbook_variablelisttype_constructor_args():
    sig = inspect.signature(Docbook_VariableListType.__init__)
    params = list(sig.parameters.keys())



def test_itemizedlisttype_is_not_abstract():
    assert not inspect.isabstract(ItemizedlistType)


def test_itemizedlisttype_constructor_exists():
    assert callable(ItemizedlistType.__init__)


def test_itemizedlisttype_constructor_args():
    sig = inspect.signature(ItemizedlistType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_parametertype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ParameterType)


def test_docbook_parametertype_constructor_exists():
    assert callable(Docbook_ParameterType.__init__)


def test_docbook_parametertype_constructor_args():
    sig = inspect.signature(Docbook_ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_parametertype_has_mixed():
    assert hasattr(Docbook_ParameterType, "mixed")
    descriptor = None
    for klass in Docbook_ParameterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_revhistorytype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RevhistoryType)


def test_docbook_revhistorytype_constructor_exists():
    assert callable(Docbook_RevhistoryType.__init__)


def test_docbook_revhistorytype_constructor_args():
    sig = inspect.signature(Docbook_RevhistoryType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_legalnoticetype_is_not_abstract():
    assert not inspect.isabstract(Docbook_LegalNoticeType)


def test_docbook_legalnoticetype_constructor_exists():
    assert callable(Docbook_LegalNoticeType.__init__)


def test_docbook_legalnoticetype_constructor_args():
    sig = inspect.signature(Docbook_LegalNoticeType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_docbook_legalnoticetype_has_group():
    assert hasattr(Docbook_LegalNoticeType, "group")
    descriptor = None
    for klass in Docbook_LegalNoticeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook_subtitletype_is_not_abstract():
    assert not inspect.isabstract(Docbook_SubtitleType)


def test_docbook_subtitletype_constructor_exists():
    assert callable(Docbook_SubtitleType.__init__)


def test_docbook_subtitletype_constructor_args():
    sig = inspect.signature(Docbook_SubtitleType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_docbook_subtitletype_has_mixed():
    assert hasattr(Docbook_SubtitleType, "mixed")
    descriptor = None
    for klass in Docbook_SubtitleType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook_subtitletype_has_group():
    assert hasattr(Docbook_SubtitleType, "group")
    descriptor = None
    for klass in Docbook_SubtitleType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook_paramdeftype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ParamdefType)


def test_docbook_paramdeftype_constructor_exists():
    assert callable(Docbook_ParamdefType.__init__)


def test_docbook_paramdeftype_constructor_args():
    sig = inspect.signature(Docbook_ParamdefType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_paramdeftype_has_mixed():
    assert hasattr(Docbook_ParamdefType, "mixed")
    descriptor = None
    for klass in Docbook_ParamdefType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_funcprototypetype_is_not_abstract():
    assert not inspect.isabstract(Docbook_FuncprototypeType)


def test_docbook_funcprototypetype_constructor_exists():
    assert callable(Docbook_FuncprototypeType.__init__)


def test_docbook_funcprototypetype_constructor_args():
    sig = inspect.signature(Docbook_FuncprototypeType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_funcsynopsistype_is_not_abstract():
    assert not inspect.isabstract(Docbook_FuncsynopsisType)


def test_docbook_funcsynopsistype_constructor_exists():
    assert callable(Docbook_FuncsynopsisType.__init__)


def test_docbook_funcsynopsistype_constructor_args():
    sig = inspect.signature(Docbook_FuncsynopsisType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_filenametype_is_not_abstract():
    assert not inspect.isabstract(Docbook_FileNameType)


def test_docbook_filenametype_constructor_exists():
    assert callable(Docbook_FileNameType.__init__)


def test_docbook_filenametype_constructor_args():
    sig = inspect.signature(Docbook_FileNameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_filenametype_has_mixed():
    assert hasattr(Docbook_FileNameType, "mixed")
    descriptor = None
    for klass in Docbook_FileNameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_functiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook_FunctionType)


def test_docbook_functiontype_constructor_exists():
    assert callable(Docbook_FunctionType.__init__)


def test_docbook_functiontype_constructor_args():
    sig = inspect.signature(Docbook_FunctionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_functiontype_has_mixed():
    assert hasattr(Docbook_FunctionType, "mixed")
    descriptor = None
    for klass in Docbook_FunctionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_funcdeftype_is_not_abstract():
    assert not inspect.isabstract(Docbook_FuncdefType)


def test_docbook_funcdeftype_constructor_exists():
    assert callable(Docbook_FuncdefType.__init__)


def test_docbook_funcdeftype_constructor_args():
    sig = inspect.signature(Docbook_FuncdefType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_funcdeftype_has_mixed():
    assert hasattr(Docbook_FuncdefType, "mixed")
    descriptor = None
    for klass in Docbook_FuncdefType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_firstnametype_is_not_abstract():
    assert not inspect.isabstract(Docbook_FirstnameType)


def test_docbook_firstnametype_constructor_exists():
    assert callable(Docbook_FirstnameType.__init__)


def test_docbook_firstnametype_constructor_args():
    sig = inspect.signature(Docbook_FirstnameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_firstnametype_has_mixed():
    assert hasattr(Docbook_FirstnameType, "mixed")
    descriptor = None
    for klass in Docbook_FirstnameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_envartype_is_not_abstract():
    assert not inspect.isabstract(Docbook_EnvarType)


def test_docbook_envartype_constructor_exists():
    assert callable(Docbook_EnvarType.__init__)


def test_docbook_envartype_constructor_args():
    sig = inspect.signature(Docbook_EnvarType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_envartype_has_mixed():
    assert hasattr(Docbook_EnvarType, "mixed")
    descriptor = None
    for klass in Docbook_EnvarType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_exampletype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ExampleType)


def test_docbook_exampletype_constructor_exists():
    assert callable(Docbook_ExampleType.__init__)


def test_docbook_exampletype_constructor_args():
    sig = inspect.signature(Docbook_ExampleType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook_exampletype_has_id():
    assert hasattr(Docbook_ExampleType, "id")
    descriptor = None
    for klass in Docbook_ExampleType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook_theadtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_TheadType)


def test_docbook_theadtype_constructor_exists():
    assert callable(Docbook_TheadType.__init__)


def test_docbook_theadtype_constructor_args():
    sig = inspect.signature(Docbook_TheadType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_tgrouptype_is_not_abstract():
    assert not inspect.isabstract(Docbook_TgroupType)


def test_docbook_tgrouptype_constructor_exists():
    assert callable(Docbook_TgroupType.__init__)


def test_docbook_tgrouptype_constructor_args():
    sig = inspect.signature(Docbook_TgroupType.__init__)
    params = list(sig.parameters.keys())
    assert "rowseq" in params, "Missing parameter 'rowseq'"
    assert "align" in params, "Missing parameter 'align'"
    assert "colseq" in params, "Missing parameter 'colseq'"
    assert "cols" in params, "Missing parameter 'cols'"

def test_docbook_tgrouptype_has_rowseq():
    assert hasattr(Docbook_TgroupType, "rowseq")
    descriptor = None
    for klass in Docbook_TgroupType.__mro__:
        if "rowseq" in klass.__dict__:
            descriptor = klass.__dict__["rowseq"]
            break
    assert isinstance(descriptor, property)

def test_docbook_tgrouptype_has_align():
    assert hasattr(Docbook_TgroupType, "align")
    descriptor = None
    for klass in Docbook_TgroupType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_docbook_tgrouptype_has_colseq():
    assert hasattr(Docbook_TgroupType, "colseq")
    descriptor = None
    for klass in Docbook_TgroupType.__mro__:
        if "colseq" in klass.__dict__:
            descriptor = klass.__dict__["colseq"]
            break
    assert isinstance(descriptor, property)

def test_docbook_tgrouptype_has_cols():
    assert hasattr(Docbook_TgroupType, "cols")
    descriptor = None
    for klass in Docbook_TgroupType.__mro__:
        if "cols" in klass.__dict__:
            descriptor = klass.__dict__["cols"]
            break
    assert isinstance(descriptor, property)



def test_docbook_ulinktype_is_not_abstract():
    assert not inspect.isabstract(Docbook_UlinkType)


def test_docbook_ulinktype_constructor_exists():
    assert callable(Docbook_UlinkType.__init__)


def test_docbook_ulinktype_constructor_args():
    sig = inspect.signature(Docbook_UlinkType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "url" in params, "Missing parameter 'url'"
    assert "type" in params, "Missing parameter 'type'"

def test_docbook_ulinktype_has_mixed():
    assert hasattr(Docbook_UlinkType, "mixed")
    descriptor = None
    for klass in Docbook_UlinkType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook_ulinktype_has_url():
    assert hasattr(Docbook_UlinkType, "url")
    descriptor = None
    for klass in Docbook_UlinkType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_docbook_ulinktype_has_type():
    assert hasattr(Docbook_UlinkType, "type")
    descriptor = None
    for klass in Docbook_UlinkType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_docbook_tiptype_is_not_abstract():
    assert not inspect.isabstract(Docbook_TipType)


def test_docbook_tiptype_constructor_exists():
    assert callable(Docbook_TipType.__init__)


def test_docbook_tiptype_constructor_args():
    sig = inspect.signature(Docbook_TipType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_tiptype_has_mixed():
    assert hasattr(Docbook_TipType, "mixed")
    descriptor = None
    for klass in Docbook_TipType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_tbodytype_is_not_abstract():
    assert not inspect.isabstract(Docbook_TbodyType)


def test_docbook_tbodytype_constructor_exists():
    assert callable(Docbook_TbodyType.__init__)


def test_docbook_tbodytype_constructor_args():
    sig = inspect.signature(Docbook_TbodyType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_tabletype_is_not_abstract():
    assert not inspect.isabstract(Docbook_TableType)


def test_docbook_tabletype_constructor_exists():
    assert callable(Docbook_TableType.__init__)


def test_docbook_tabletype_constructor_args():
    sig = inspect.signature(Docbook_TableType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook_tabletype_has_id():
    assert hasattr(Docbook_TableType, "id")
    descriptor = None
    for klass in Docbook_TableType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook_programlistingtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ProgramlistingType)


def test_docbook_programlistingtype_constructor_exists():
    assert callable(Docbook_ProgramlistingType.__init__)


def test_docbook_programlistingtype_constructor_args():
    sig = inspect.signature(Docbook_ProgramlistingType.__init__)
    params = list(sig.parameters.keys())
    assert "superscript" in params, "Missing parameter 'superscript'"
    assert "format" in params, "Missing parameter 'format'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"
    assert "linenumbering" in params, "Missing parameter 'linenumbering'"
    assert "language" in params, "Missing parameter 'language'"

def test_docbook_programlistingtype_has_superscript():
    assert hasattr(Docbook_ProgramlistingType, "superscript")
    descriptor = None
    for klass in Docbook_ProgramlistingType.__mro__:
        if "superscript" in klass.__dict__:
            descriptor = klass.__dict__["superscript"]
            break
    assert isinstance(descriptor, property)

def test_docbook_programlistingtype_has_format():
    assert hasattr(Docbook_ProgramlistingType, "format")
    descriptor = None
    for klass in Docbook_ProgramlistingType.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_docbook_programlistingtype_has_mixed():
    assert hasattr(Docbook_ProgramlistingType, "mixed")
    descriptor = None
    for klass in Docbook_ProgramlistingType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook_programlistingtype_has_group():
    assert hasattr(Docbook_ProgramlistingType, "group")
    descriptor = None
    for klass in Docbook_ProgramlistingType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook_programlistingtype_has_linenumbering():
    assert hasattr(Docbook_ProgramlistingType, "linenumbering")
    descriptor = None
    for klass in Docbook_ProgramlistingType.__mro__:
        if "linenumbering" in klass.__dict__:
            descriptor = klass.__dict__["linenumbering"]
            break
    assert isinstance(descriptor, property)

def test_docbook_programlistingtype_has_language():
    assert hasattr(Docbook_ProgramlistingType, "language")
    descriptor = None
    for klass in Docbook_ProgramlistingType.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)



def test_docbook_rowtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_RowType)


def test_docbook_rowtype_constructor_exists():
    assert callable(Docbook_RowType.__init__)


def test_docbook_rowtype_constructor_args():
    sig = inspect.signature(Docbook_RowType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_phrasetype_is_not_abstract():
    assert not inspect.isabstract(Docbook_PhraseType)


def test_docbook_phrasetype_constructor_exists():
    assert callable(Docbook_PhraseType.__init__)


def test_docbook_phrasetype_constructor_args():
    sig = inspect.signature(Docbook_PhraseType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook_phrasetype_has_id():
    assert hasattr(Docbook_PhraseType, "id")
    descriptor = None
    for klass in Docbook_PhraseType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook_publishertype_is_not_abstract():
    assert not inspect.isabstract(Docbook_PublisherType)


def test_docbook_publishertype_constructor_exists():
    assert callable(Docbook_PublisherType.__init__)


def test_docbook_publishertype_constructor_args():
    sig = inspect.signature(Docbook_PublisherType.__init__)
    params = list(sig.parameters.keys())
    assert "publishername" in params, "Missing parameter 'publishername'"

def test_docbook_publishertype_has_publishername():
    assert hasattr(Docbook_PublisherType, "publishername")
    descriptor = None
    for klass in Docbook_PublisherType.__mro__:
        if "publishername" in klass.__dict__:
            descriptor = klass.__dict__["publishername"]
            break
    assert isinstance(descriptor, property)



def test_docbook_orderedlisttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_OrderedlistType)


def test_docbook_orderedlisttype_constructor_exists():
    assert callable(Docbook_OrderedlistType.__init__)


def test_docbook_orderedlisttype_constructor_args():
    sig = inspect.signature(Docbook_OrderedlistType.__init__)
    params = list(sig.parameters.keys())
    assert "inheritnum" in params, "Missing parameter 'inheritnum'"
    assert "continuation" in params, "Missing parameter 'continuation'"

def test_docbook_orderedlisttype_has_inheritnum():
    assert hasattr(Docbook_OrderedlistType, "inheritnum")
    descriptor = None
    for klass in Docbook_OrderedlistType.__mro__:
        if "inheritnum" in klass.__dict__:
            descriptor = klass.__dict__["inheritnum"]
            break
    assert isinstance(descriptor, property)

def test_docbook_orderedlisttype_has_continuation():
    assert hasattr(Docbook_OrderedlistType, "continuation")
    descriptor = None
    for klass in Docbook_OrderedlistType.__mro__:
        if "continuation" in klass.__dict__:
            descriptor = klass.__dict__["continuation"]
            break
    assert isinstance(descriptor, property)



def test_docbook_mediaobjecttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_MediaobjectType)


def test_docbook_mediaobjecttype_constructor_exists():
    assert callable(Docbook_MediaobjectType.__init__)


def test_docbook_mediaobjecttype_constructor_args():
    sig = inspect.signature(Docbook_MediaobjectType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_listitemtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ListitemType)


def test_docbook_listitemtype_constructor_exists():
    assert callable(Docbook_ListitemType.__init__)


def test_docbook_listitemtype_constructor_args():
    sig = inspect.signature(Docbook_ListitemType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_linktype_is_not_abstract():
    assert not inspect.isabstract(Docbook_LinkType)


def test_docbook_linktype_constructor_exists():
    assert callable(Docbook_LinkType.__init__)


def test_docbook_linktype_constructor_args():
    sig = inspect.signature(Docbook_LinkType.__init__)
    params = list(sig.parameters.keys())
    assert "value" in params, "Missing parameter 'value'"
    assert "linkend" in params, "Missing parameter 'linkend'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_linktype_has_value():
    assert hasattr(Docbook_LinkType, "value")
    descriptor = None
    for klass in Docbook_LinkType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)

def test_docbook_linktype_has_linkend():
    assert hasattr(Docbook_LinkType, "linkend")
    descriptor = None
    for klass in Docbook_LinkType.__mro__:
        if "linkend" in klass.__dict__:
            descriptor = klass.__dict__["linkend"]
            break
    assert isinstance(descriptor, property)

def test_docbook_linktype_has_mixed():
    assert hasattr(Docbook_LinkType, "mixed")
    descriptor = None
    for klass in Docbook_LinkType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_keywordsettype_is_not_abstract():
    assert not inspect.isabstract(Docbook_KeywordsetType)


def test_docbook_keywordsettype_constructor_exists():
    assert callable(Docbook_KeywordsetType.__init__)


def test_docbook_keywordsettype_constructor_args():
    sig = inspect.signature(Docbook_KeywordsetType.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_docbook_keywordsettype_has_keyword():
    assert hasattr(Docbook_KeywordsetType, "keyword")
    descriptor = None
    for klass in Docbook_KeywordsetType.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_docbook_literaltype_is_not_abstract():
    assert not inspect.isabstract(Docbook_LiteralType)


def test_docbook_literaltype_constructor_exists():
    assert callable(Docbook_LiteralType.__init__)


def test_docbook_literaltype_constructor_args():
    sig = inspect.signature(Docbook_LiteralType.__init__)
    params = list(sig.parameters.keys())
    assert "moreinfo" in params, "Missing parameter 'moreinfo'"
    assert "value" in params, "Missing parameter 'value'"

def test_docbook_literaltype_has_moreinfo():
    assert hasattr(Docbook_LiteralType, "moreinfo")
    descriptor = None
    for klass in Docbook_LiteralType.__mro__:
        if "moreinfo" in klass.__dict__:
            descriptor = klass.__dict__["moreinfo"]
            break
    assert isinstance(descriptor, property)

def test_docbook_literaltype_has_value():
    assert hasattr(Docbook_LiteralType, "value")
    descriptor = None
    for klass in Docbook_LiteralType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_docbook_importanttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ImportantType)


def test_docbook_importanttype_constructor_exists():
    assert callable(Docbook_ImportantType.__init__)


def test_docbook_importanttype_constructor_args():
    sig = inspect.signature(Docbook_ImportantType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_importanttype_has_group():
    assert hasattr(Docbook_ImportantType, "group")
    descriptor = None
    for klass in Docbook_ImportantType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook_importanttype_has_mixed():
    assert hasattr(Docbook_ImportantType, "mixed")
    descriptor = None
    for klass in Docbook_ImportantType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_imageobjecttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ImageobjectType)


def test_docbook_imageobjecttype_constructor_exists():
    assert callable(Docbook_ImageobjectType.__init__)


def test_docbook_imageobjecttype_constructor_args():
    sig = inspect.signature(Docbook_ImageobjectType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_imagedatatype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ImagedataType)


def test_docbook_imagedatatype_constructor_exists():
    assert callable(Docbook_ImagedataType.__init__)


def test_docbook_imagedatatype_constructor_args():
    sig = inspect.signature(Docbook_ImagedataType.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "fileref" in params, "Missing parameter 'fileref'"
    assert "scale" in params, "Missing parameter 'scale'"
    assert "width" in params, "Missing parameter 'width'"
    assert "depth" in params, "Missing parameter 'depth'"

def test_docbook_imagedatatype_has_align():
    assert hasattr(Docbook_ImagedataType, "align")
    descriptor = None
    for klass in Docbook_ImagedataType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_docbook_imagedatatype_has_fileref():
    assert hasattr(Docbook_ImagedataType, "fileref")
    descriptor = None
    for klass in Docbook_ImagedataType.__mro__:
        if "fileref" in klass.__dict__:
            descriptor = klass.__dict__["fileref"]
            break
    assert isinstance(descriptor, property)

def test_docbook_imagedatatype_has_scale():
    assert hasattr(Docbook_ImagedataType, "scale")
    descriptor = None
    for klass in Docbook_ImagedataType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)

def test_docbook_imagedatatype_has_width():
    assert hasattr(Docbook_ImagedataType, "width")
    descriptor = None
    for klass in Docbook_ImagedataType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_docbook_imagedatatype_has_depth():
    assert hasattr(Docbook_ImagedataType, "depth")
    descriptor = None
    for klass in Docbook_ImagedataType.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)



def test_docbook_footnotetype_is_not_abstract():
    assert not inspect.isabstract(Docbook_FootnoteType)


def test_docbook_footnotetype_constructor_exists():
    assert callable(Docbook_FootnoteType.__init__)


def test_docbook_footnotetype_constructor_args():
    sig = inspect.signature(Docbook_FootnoteType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook_footnotetype_has_id():
    assert hasattr(Docbook_FootnoteType, "id")
    descriptor = None
    for klass in Docbook_FootnoteType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook_itemizedlisttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ItemizedlistType)


def test_docbook_itemizedlisttype_constructor_exists():
    assert callable(Docbook_ItemizedlistType.__init__)


def test_docbook_itemizedlisttype_constructor_args():
    sig = inspect.signature(Docbook_ItemizedlistType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_informaltabletype_is_not_abstract():
    assert not inspect.isabstract(Docbook_InformaltableType)


def test_docbook_informaltabletype_constructor_exists():
    assert callable(Docbook_InformaltableType.__init__)


def test_docbook_informaltabletype_constructor_args():
    sig = inspect.signature(Docbook_InformaltableType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_figuretype_is_not_abstract():
    assert not inspect.isabstract(Docbook_FigureType)


def test_docbook_figuretype_constructor_exists():
    assert callable(Docbook_FigureType.__init__)


def test_docbook_figuretype_constructor_args():
    sig = inspect.signature(Docbook_FigureType.__init__)
    params = list(sig.parameters.keys())
    assert "float" in params, "Missing parameter 'float'"
    assert "id" in params, "Missing parameter 'id'"

def test_docbook_figuretype_has_float():
    assert hasattr(Docbook_FigureType, "float")
    descriptor = None
    for klass in Docbook_FigureType.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)

def test_docbook_figuretype_has_id():
    assert hasattr(Docbook_FigureType, "id")
    descriptor = None
    for klass in Docbook_FigureType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook_entrytype_is_not_abstract():
    assert not inspect.isabstract(Docbook_EntryType)


def test_docbook_entrytype_constructor_exists():
    assert callable(Docbook_EntryType.__init__)


def test_docbook_entrytype_constructor_args():
    sig = inspect.signature(Docbook_EntryType.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "namest" in params, "Missing parameter 'namest'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "morerows" in params, "Missing parameter 'morerows'"
    assert "nameend" in params, "Missing parameter 'nameend'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_entrytype_has_align():
    assert hasattr(Docbook_EntryType, "align")
    descriptor = None
    for klass in Docbook_EntryType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_docbook_entrytype_has_namest():
    assert hasattr(Docbook_EntryType, "namest")
    descriptor = None
    for klass in Docbook_EntryType.__mro__:
        if "namest" in klass.__dict__:
            descriptor = klass.__dict__["namest"]
            break
    assert isinstance(descriptor, property)

def test_docbook_entrytype_has_valign():
    assert hasattr(Docbook_EntryType, "valign")
    descriptor = None
    for klass in Docbook_EntryType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_docbook_entrytype_has_morerows():
    assert hasattr(Docbook_EntryType, "morerows")
    descriptor = None
    for klass in Docbook_EntryType.__mro__:
        if "morerows" in klass.__dict__:
            descriptor = klass.__dict__["morerows"]
            break
    assert isinstance(descriptor, property)

def test_docbook_entrytype_has_nameend():
    assert hasattr(Docbook_EntryType, "nameend")
    descriptor = None
    for klass in Docbook_EntryType.__mro__:
        if "nameend" in klass.__dict__:
            descriptor = klass.__dict__["nameend"]
            break
    assert isinstance(descriptor, property)

def test_docbook_entrytype_has_mixed():
    assert hasattr(Docbook_EntryType, "mixed")
    descriptor = None
    for klass in Docbook_EntryType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_emphasistype_is_not_abstract():
    assert not inspect.isabstract(Docbook_EmphasisType)


def test_docbook_emphasistype_constructor_exists():
    assert callable(Docbook_EmphasisType.__init__)


def test_docbook_emphasistype_constructor_args():
    sig = inspect.signature(Docbook_EmphasisType.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_emphasistype_has_role():
    assert hasattr(Docbook_EmphasisType, "role")
    descriptor = None
    for klass in Docbook_EmphasisType.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_docbook_emphasistype_has_mixed():
    assert hasattr(Docbook_EmphasisType, "mixed")
    descriptor = None
    for klass in Docbook_EmphasisType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_datetype_is_not_abstract():
    assert not inspect.isabstract(Docbook_DateType)


def test_docbook_datetype_constructor_exists():
    assert callable(Docbook_DateType.__init__)


def test_docbook_datetype_constructor_args():
    sig = inspect.signature(Docbook_DateType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_datetype_has_mixed():
    assert hasattr(Docbook_DateType, "mixed")
    descriptor = None
    for klass in Docbook_DateType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_copyrighttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_CopyrightType)


def test_docbook_copyrighttype_constructor_exists():
    assert callable(Docbook_CopyrightType.__init__)


def test_docbook_copyrighttype_constructor_args():
    sig = inspect.signature(Docbook_CopyrightType.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "holder" in params, "Missing parameter 'holder'"
    assert "group" in params, "Missing parameter 'group'"

def test_docbook_copyrighttype_has_year():
    assert hasattr(Docbook_CopyrightType, "year")
    descriptor = None
    for klass in Docbook_CopyrightType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_docbook_copyrighttype_has_holder():
    assert hasattr(Docbook_CopyrightType, "holder")
    descriptor = None
    for klass in Docbook_CopyrightType.__mro__:
        if "holder" in klass.__dict__:
            descriptor = klass.__dict__["holder"]
            break
    assert isinstance(descriptor, property)

def test_docbook_copyrighttype_has_group():
    assert hasattr(Docbook_CopyrightType, "group")
    descriptor = None
    for klass in Docbook_CopyrightType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook_confgrouptype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ConfgroupType)


def test_docbook_confgrouptype_constructor_exists():
    assert callable(Docbook_ConfgroupType.__init__)


def test_docbook_confgrouptype_constructor_args():
    sig = inspect.signature(Docbook_ConfgroupType.__init__)
    params = list(sig.parameters.keys())
    assert "confsponsor" in params, "Missing parameter 'confsponsor'"
    assert "confnum" in params, "Missing parameter 'confnum'"
    assert "conftitle" in params, "Missing parameter 'conftitle'"

def test_docbook_confgrouptype_has_confsponsor():
    assert hasattr(Docbook_ConfgroupType, "confsponsor")
    descriptor = None
    for klass in Docbook_ConfgroupType.__mro__:
        if "confsponsor" in klass.__dict__:
            descriptor = klass.__dict__["confsponsor"]
            break
    assert isinstance(descriptor, property)

def test_docbook_confgrouptype_has_confnum():
    assert hasattr(Docbook_ConfgroupType, "confnum")
    descriptor = None
    for klass in Docbook_ConfgroupType.__mro__:
        if "confnum" in klass.__dict__:
            descriptor = klass.__dict__["confnum"]
            break
    assert isinstance(descriptor, property)

def test_docbook_confgrouptype_has_conftitle():
    assert hasattr(Docbook_ConfgroupType, "conftitle")
    descriptor = None
    for klass in Docbook_ConfgroupType.__mro__:
        if "conftitle" in klass.__dict__:
            descriptor = klass.__dict__["conftitle"]
            break
    assert isinstance(descriptor, property)



def test_docbook_estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(Docbook_EStringToStringMapEntry)


def test_docbook_estringtostringmapentry_constructor_exists():
    assert callable(Docbook_EStringToStringMapEntry.__init__)


def test_docbook_estringtostringmapentry_constructor_args():
    sig = inspect.signature(Docbook_EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_docbook_documentroot_is_not_abstract():
    assert not inspect.isabstract(Docbook_DocumentRoot)


def test_docbook_documentroot_constructor_exists():
    assert callable(Docbook_DocumentRoot.__init__)


def test_docbook_documentroot_constructor_args():
    sig = inspect.signature(Docbook_DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "bibliomisc" in params, "Missing parameter 'bibliomisc'"
    assert "superscript" in params, "Missing parameter 'superscript'"
    assert "confsponsor" in params, "Missing parameter 'confsponsor'"
    assert "date" in params, "Missing parameter 'date'"
    assert "subtitle" in params, "Missing parameter 'subtitle'"
    assert "confnum" in params, "Missing parameter 'confnum'"
    assert "publishername" in params, "Missing parameter 'publishername'"
    assert "state" in params, "Missing parameter 'state'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "warning" in params, "Missing parameter 'warning'"
    assert "keyword" in params, "Missing parameter 'keyword'"
    assert "conftitle" in params, "Missing parameter 'conftitle'"
    assert "pubdate" in params, "Missing parameter 'pubdate'"
    assert "caution" in params, "Missing parameter 'caution'"

def test_docbook_documentroot_has_bibliomisc():
    assert hasattr(Docbook_DocumentRoot, "bibliomisc")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "bibliomisc" in klass.__dict__:
            descriptor = klass.__dict__["bibliomisc"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_superscript():
    assert hasattr(Docbook_DocumentRoot, "superscript")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "superscript" in klass.__dict__:
            descriptor = klass.__dict__["superscript"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_confsponsor():
    assert hasattr(Docbook_DocumentRoot, "confsponsor")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "confsponsor" in klass.__dict__:
            descriptor = klass.__dict__["confsponsor"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_date():
    assert hasattr(Docbook_DocumentRoot, "date")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_subtitle():
    assert hasattr(Docbook_DocumentRoot, "subtitle")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "subtitle" in klass.__dict__:
            descriptor = klass.__dict__["subtitle"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_confnum():
    assert hasattr(Docbook_DocumentRoot, "confnum")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "confnum" in klass.__dict__:
            descriptor = klass.__dict__["confnum"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_publishername():
    assert hasattr(Docbook_DocumentRoot, "publishername")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "publishername" in klass.__dict__:
            descriptor = klass.__dict__["publishername"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_state():
    assert hasattr(Docbook_DocumentRoot, "state")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_mixed():
    assert hasattr(Docbook_DocumentRoot, "mixed")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_firstname():
    assert hasattr(Docbook_DocumentRoot, "firstname")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_warning():
    assert hasattr(Docbook_DocumentRoot, "warning")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "warning" in klass.__dict__:
            descriptor = klass.__dict__["warning"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_keyword():
    assert hasattr(Docbook_DocumentRoot, "keyword")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_conftitle():
    assert hasattr(Docbook_DocumentRoot, "conftitle")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "conftitle" in klass.__dict__:
            descriptor = klass.__dict__["conftitle"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_pubdate():
    assert hasattr(Docbook_DocumentRoot, "pubdate")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "pubdate" in klass.__dict__:
            descriptor = klass.__dict__["pubdate"]
            break
    assert isinstance(descriptor, property)

def test_docbook_documentroot_has_caution():
    assert hasattr(Docbook_DocumentRoot, "caution")
    descriptor = None
    for klass in Docbook_DocumentRoot.__mro__:
        if "caution" in klass.__dict__:
            descriptor = klass.__dict__["caution"]
            break
    assert isinstance(descriptor, property)



def test_docbook_commandtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_CommandType)


def test_docbook_commandtype_constructor_exists():
    assert callable(Docbook_CommandType.__init__)


def test_docbook_commandtype_constructor_args():
    sig = inspect.signature(Docbook_CommandType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_commandtype_has_mixed():
    assert hasattr(Docbook_CommandType, "mixed")
    descriptor = None
    for klass in Docbook_CommandType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_cmdsynopsistype_is_not_abstract():
    assert not inspect.isabstract(Docbook_CmdsynopsisType)


def test_docbook_cmdsynopsistype_constructor_exists():
    assert callable(Docbook_CmdsynopsisType.__init__)


def test_docbook_cmdsynopsistype_constructor_args():
    sig = inspect.signature(Docbook_CmdsynopsisType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_colspectype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ColspecType)


def test_docbook_colspectype_constructor_exists():
    assert callable(Docbook_ColspecType.__init__)


def test_docbook_colspectype_constructor_args():
    sig = inspect.signature(Docbook_ColspecType.__init__)
    params = list(sig.parameters.keys())
    assert "colwidth" in params, "Missing parameter 'colwidth'"
    assert "colname" in params, "Missing parameter 'colname'"

def test_docbook_colspectype_has_colwidth():
    assert hasattr(Docbook_ColspecType, "colwidth")
    descriptor = None
    for klass in Docbook_ColspecType.__mro__:
        if "colwidth" in klass.__dict__:
            descriptor = klass.__dict__["colwidth"]
            break
    assert isinstance(descriptor, property)

def test_docbook_colspectype_has_colname():
    assert hasattr(Docbook_ColspecType, "colname")
    descriptor = None
    for klass in Docbook_ColspecType.__mro__:
        if "colname" in klass.__dict__:
            descriptor = klass.__dict__["colname"]
            break
    assert isinstance(descriptor, property)



def test_docbook_sectiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook_SectionType)


def test_docbook_sectiontype_constructor_exists():
    assert callable(Docbook_SectionType.__init__)


def test_docbook_sectiontype_constructor_args():
    sig = inspect.signature(Docbook_SectionType.__init__)
    params = list(sig.parameters.keys())
    assert "warning" in params, "Missing parameter 'warning'"
    assert "group" in params, "Missing parameter 'group'"
    assert "caution" in params, "Missing parameter 'caution'"
    assert "annotations" in params, "Missing parameter 'annotations'"

def test_docbook_sectiontype_has_warning():
    assert hasattr(Docbook_SectionType, "warning")
    descriptor = None
    for klass in Docbook_SectionType.__mro__:
        if "warning" in klass.__dict__:
            descriptor = klass.__dict__["warning"]
            break
    assert isinstance(descriptor, property)

def test_docbook_sectiontype_has_group():
    assert hasattr(Docbook_SectionType, "group")
    descriptor = None
    for klass in Docbook_SectionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook_sectiontype_has_caution():
    assert hasattr(Docbook_SectionType, "caution")
    descriptor = None
    for klass in Docbook_SectionType.__mro__:
        if "caution" in klass.__dict__:
            descriptor = klass.__dict__["caution"]
            break
    assert isinstance(descriptor, property)

def test_docbook_sectiontype_has_annotations():
    assert hasattr(Docbook_SectionType, "annotations")
    descriptor = None
    for klass in Docbook_SectionType.__mro__:
        if "annotations" in klass.__dict__:
            descriptor = klass.__dict__["annotations"]
            break
    assert isinstance(descriptor, property)



def test_docbook_notetype_is_not_abstract():
    assert not inspect.isabstract(Docbook_NoteType)


def test_docbook_notetype_constructor_exists():
    assert callable(Docbook_NoteType.__init__)


def test_docbook_notetype_constructor_args():
    sig = inspect.signature(Docbook_NoteType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_notetype_has_group():
    assert hasattr(Docbook_NoteType, "group")
    descriptor = None
    for klass in Docbook_NoteType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook_notetype_has_mixed():
    assert hasattr(Docbook_NoteType, "mixed")
    descriptor = None
    for klass in Docbook_NoteType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_referencetype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ReferenceType)


def test_docbook_referencetype_constructor_exists():
    assert callable(Docbook_ReferenceType.__init__)


def test_docbook_referencetype_constructor_args():
    sig = inspect.signature(Docbook_ReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_docbook_referencetype_has_version():
    assert hasattr(Docbook_ReferenceType, "version")
    descriptor = None
    for klass in Docbook_ReferenceType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_docbook_chaptertype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ChapterType)


def test_docbook_chaptertype_constructor_exists():
    assert callable(Docbook_ChapterType.__init__)


def test_docbook_chaptertype_constructor_args():
    sig = inspect.signature(Docbook_ChapterType.__init__)
    params = list(sig.parameters.keys())
    assert "annotations" in params, "Missing parameter 'annotations'"

def test_docbook_chaptertype_has_annotations():
    assert hasattr(Docbook_ChapterType, "annotations")
    descriptor = None
    for klass in Docbook_ChapterType.__mro__:
        if "annotations" in klass.__dict__:
            descriptor = klass.__dict__["annotations"]
            break
    assert isinstance(descriptor, property)



def test_docbook_prefacetype_is_not_abstract():
    assert not inspect.isabstract(Docbook_PrefaceType)


def test_docbook_prefacetype_constructor_exists():
    assert callable(Docbook_PrefaceType.__init__)


def test_docbook_prefacetype_constructor_args():
    sig = inspect.signature(Docbook_PrefaceType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_infotype_is_not_abstract():
    assert not inspect.isabstract(Docbook_InfoType)


def test_docbook_infotype_constructor_exists():
    assert callable(Docbook_InfoType.__init__)


def test_docbook_infotype_constructor_args():
    sig = inspect.signature(Docbook_InfoType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "pubdate" in params, "Missing parameter 'pubdate'"
    assert "date" in params, "Missing parameter 'date'"
    assert "releaseinfo" in params, "Missing parameter 'releaseinfo'"
    assert "bibliomisc" in params, "Missing parameter 'bibliomisc'"
    assert "productname" in params, "Missing parameter 'productname'"

def test_docbook_infotype_has_group():
    assert hasattr(Docbook_InfoType, "group")
    descriptor = None
    for klass in Docbook_InfoType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook_infotype_has_pubdate():
    assert hasattr(Docbook_InfoType, "pubdate")
    descriptor = None
    for klass in Docbook_InfoType.__mro__:
        if "pubdate" in klass.__dict__:
            descriptor = klass.__dict__["pubdate"]
            break
    assert isinstance(descriptor, property)

def test_docbook_infotype_has_date():
    assert hasattr(Docbook_InfoType, "date")
    descriptor = None
    for klass in Docbook_InfoType.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_docbook_infotype_has_releaseinfo():
    assert hasattr(Docbook_InfoType, "releaseinfo")
    descriptor = None
    for klass in Docbook_InfoType.__mro__:
        if "releaseinfo" in klass.__dict__:
            descriptor = klass.__dict__["releaseinfo"]
            break
    assert isinstance(descriptor, property)

def test_docbook_infotype_has_bibliomisc():
    assert hasattr(Docbook_InfoType, "bibliomisc")
    descriptor = None
    for klass in Docbook_InfoType.__mro__:
        if "bibliomisc" in klass.__dict__:
            descriptor = klass.__dict__["bibliomisc"]
            break
    assert isinstance(descriptor, property)

def test_docbook_infotype_has_productname():
    assert hasattr(Docbook_InfoType, "productname")
    descriptor = None
    for klass in Docbook_InfoType.__mro__:
        if "productname" in klass.__dict__:
            descriptor = klass.__dict__["productname"]
            break
    assert isinstance(descriptor, property)



def test_docbook_booktype_is_not_abstract():
    assert not inspect.isabstract(Docbook_BookType)


def test_docbook_booktype_constructor_exists():
    assert callable(Docbook_BookType.__init__)


def test_docbook_booktype_constructor_args():
    sig = inspect.signature(Docbook_BookType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"
    assert "label" in params, "Missing parameter 'label'"
    assert "lang" in params, "Missing parameter 'lang'"

def test_docbook_booktype_has_version():
    assert hasattr(Docbook_BookType, "version")
    descriptor = None
    for klass in Docbook_BookType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_docbook_booktype_has_label():
    assert hasattr(Docbook_BookType, "label")
    descriptor = None
    for klass in Docbook_BookType.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_docbook_booktype_has_lang():
    assert hasattr(Docbook_BookType, "lang")
    descriptor = None
    for klass in Docbook_BookType.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)



def test_docbook_titletype_is_not_abstract():
    assert not inspect.isabstract(Docbook_TitleType)


def test_docbook_titletype_constructor_exists():
    assert callable(Docbook_TitleType.__init__)


def test_docbook_titletype_constructor_args():
    sig = inspect.signature(Docbook_TitleType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_titletype_has_group():
    assert hasattr(Docbook_TitleType, "group")
    descriptor = None
    for klass in Docbook_TitleType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook_titletype_has_mixed():
    assert hasattr(Docbook_TitleType, "mixed")
    descriptor = None
    for klass in Docbook_TitleType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_otheraddrtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_OtheraddrType)


def test_docbook_otheraddrtype_constructor_exists():
    assert callable(Docbook_OtheraddrType.__init__)


def test_docbook_otheraddrtype_constructor_args():
    sig = inspect.signature(Docbook_OtheraddrType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_personnametype_is_not_abstract():
    assert not inspect.isabstract(Docbook_PersonnameType)


def test_docbook_personnametype_constructor_exists():
    assert callable(Docbook_PersonnameType.__init__)


def test_docbook_personnametype_constructor_args():
    sig = inspect.signature(Docbook_PersonnameType.__init__)
    params = list(sig.parameters.keys())



def test_docbook_authortype_is_not_abstract():
    assert not inspect.isabstract(Docbook_AuthorType)


def test_docbook_authortype_constructor_exists():
    assert callable(Docbook_AuthorType.__init__)


def test_docbook_authortype_constructor_args():
    sig = inspect.signature(Docbook_AuthorType.__init__)
    params = list(sig.parameters.keys())
    assert "contrib" in params, "Missing parameter 'contrib'"

def test_docbook_authortype_has_contrib():
    assert hasattr(Docbook_AuthorType, "contrib")
    descriptor = None
    for klass in Docbook_AuthorType.__mro__:
        if "contrib" in klass.__dict__:
            descriptor = klass.__dict__["contrib"]
            break
    assert isinstance(descriptor, property)



def test_docbook_authorinitialstype_is_not_abstract():
    assert not inspect.isabstract(Docbook_AuthorinitialsType)


def test_docbook_authorinitialstype_constructor_exists():
    assert callable(Docbook_AuthorinitialsType.__init__)


def test_docbook_authorinitialstype_constructor_args():
    sig = inspect.signature(Docbook_AuthorinitialsType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_authorinitialstype_has_mixed():
    assert hasattr(Docbook_AuthorinitialsType, "mixed")
    descriptor = None
    for klass in Docbook_AuthorinitialsType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_replaceabletype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ReplaceableType)


def test_docbook_replaceabletype_constructor_exists():
    assert callable(Docbook_ReplaceableType.__init__)


def test_docbook_replaceabletype_constructor_args():
    sig = inspect.signature(Docbook_ReplaceableType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_replaceabletype_has_mixed():
    assert hasattr(Docbook_ReplaceableType, "mixed")
    descriptor = None
    for klass in Docbook_ReplaceableType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_optiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook_OptionType)


def test_docbook_optiontype_constructor_exists():
    assert callable(Docbook_OptionType.__init__)


def test_docbook_optiontype_constructor_args():
    sig = inspect.signature(Docbook_OptionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_optiontype_has_mixed():
    assert hasattr(Docbook_OptionType, "mixed")
    descriptor = None
    for klass in Docbook_OptionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_argtype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ArgType)


def test_docbook_argtype_constructor_exists():
    assert callable(Docbook_ArgType.__init__)


def test_docbook_argtype_constructor_args():
    sig = inspect.signature(Docbook_ArgType.__init__)
    params = list(sig.parameters.keys())
    assert "choice" in params, "Missing parameter 'choice'"
    assert "rep" in params, "Missing parameter 'rep'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook_argtype_has_choice():
    assert hasattr(Docbook_ArgType, "choice")
    descriptor = None
    for klass in Docbook_ArgType.__mro__:
        if "choice" in klass.__dict__:
            descriptor = klass.__dict__["choice"]
            break
    assert isinstance(descriptor, property)

def test_docbook_argtype_has_rep():
    assert hasattr(Docbook_ArgType, "rep")
    descriptor = None
    for klass in Docbook_ArgType.__mro__:
        if "rep" in klass.__dict__:
            descriptor = klass.__dict__["rep"]
            break
    assert isinstance(descriptor, property)

def test_docbook_argtype_has_mixed():
    assert hasattr(Docbook_ArgType, "mixed")
    descriptor = None
    for klass in Docbook_ArgType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook_addresstype_is_not_abstract():
    assert not inspect.isabstract(Docbook_AddressType)


def test_docbook_addresstype_constructor_exists():
    assert callable(Docbook_AddressType.__init__)


def test_docbook_addresstype_constructor_args():
    sig = inspect.signature(Docbook_AddressType.__init__)
    params = list(sig.parameters.keys())
    assert "state" in params, "Missing parameter 'state'"
    assert "format" in params, "Missing parameter 'format'"
    assert "email" in params, "Missing parameter 'email'"

def test_docbook_addresstype_has_state():
    assert hasattr(Docbook_AddressType, "state")
    descriptor = None
    for klass in Docbook_AddressType.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_docbook_addresstype_has_format():
    assert hasattr(Docbook_AddressType, "format")
    descriptor = None
    for klass in Docbook_AddressType.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)

def test_docbook_addresstype_has_email():
    assert hasattr(Docbook_AddressType, "email")
    descriptor = None
    for klass in Docbook_AddressType.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_docbook_paratype_is_not_abstract():
    assert not inspect.isabstract(Docbook_ParaType)


def test_docbook_paratype_constructor_exists():
    assert callable(Docbook_ParaType.__init__)


def test_docbook_paratype_constructor_args():
    sig = inspect.signature(Docbook_ParaType.__init__)
    params = list(sig.parameters.keys())
    assert "role" in params, "Missing parameter 'role'"
    assert "id" in params, "Missing parameter 'id'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_docbook_paratype_has_role():
    assert hasattr(Docbook_ParaType, "role")
    descriptor = None
    for klass in Docbook_ParaType.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_docbook_paratype_has_id():
    assert hasattr(Docbook_ParaType, "id")
    descriptor = None
    for klass in Docbook_ParaType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_docbook_paratype_has_mixed():
    assert hasattr(Docbook_ParaType, "mixed")
    descriptor = None
    for klass in Docbook_ParaType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook_paratype_has_group():
    assert hasattr(Docbook_ParaType, "group")
    descriptor = None
    for klass in Docbook_ParaType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook_abstracttype_is_not_abstract():
    assert not inspect.isabstract(Docbook_AbstractType)


def test_docbook_abstracttype_constructor_exists():
    assert callable(Docbook_AbstractType.__init__)


def test_docbook_abstracttype_constructor_args():
    sig = inspect.signature(Docbook_AbstractType.__init__)
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
Docbook_VarListEntryType_strategy = st.builds(
    Docbook_VarListEntryType,
    termlength=
        safe_text,
    spacing=
        safe_text
)
Docbook_TermType_strategy = st.builds(
    Docbook_TermType,
    mixed=
        safe_text
)
Docbook_SegType_strategy = st.builds(
    Docbook_SegType,
    errortext=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text,
    errorcode=
        safe_text
)
Docbook_SegListItemType_strategy = st.builds(
    Docbook_SegListItemType,
)
Docbook_RevdescriptionType_strategy = st.builds(
    Docbook_RevdescriptionType,
    mixed=
        safe_text
)
Docbook_RevnumberType_strategy = st.builds(
    Docbook_RevnumberType,
    mixed=
        safe_text
)
Docbook_RevisionType_strategy = st.builds(
    Docbook_RevisionType,
)
Docbook_SegmentedListType_strategy = st.builds(
    Docbook_SegmentedListType,
    segtitle=
        safe_text,
    group=
        safe_text
)
Docbook_RefEntryTitleType_strategy = st.builds(
    Docbook_RefEntryTitleType,
    mixed=
        safe_text
)
Docbook_RefSect1Type_strategy = st.builds(
    Docbook_RefSect1Type,
    group=
        safe_text,
    id=
        safe_text
)
Docbook_RefSynopsisDivType_strategy = st.builds(
    Docbook_RefSynopsisDivType,
)
Docbook_RefNameDivType_strategy = st.builds(
    Docbook_RefNameDivType,
    refclass=
        safe_text,
    refpurpose=
        safe_text,
    refname=
        safe_text
)
Docbook_RefMetaType_strategy = st.builds(
    Docbook_RefMetaType,
    manvolnum=
        safe_text
)
Docbook_RefEntryType_strategy = st.builds(
    Docbook_RefEntryType,
    version=
        safe_text
)
Docbook_SurnameType_strategy = st.builds(
    Docbook_SurnameType,
    mixed=
        safe_text
)
Docbook_VariableListType_strategy = st.builds(
    Docbook_VariableListType,
)
ItemizedlistType_strategy = st.builds(
    ItemizedlistType,
)
Docbook_ParameterType_strategy = st.builds(
    Docbook_ParameterType,
    mixed=
        safe_text
)
Docbook_RevhistoryType_strategy = st.builds(
    Docbook_RevhistoryType,
)
Docbook_LegalNoticeType_strategy = st.builds(
    Docbook_LegalNoticeType,
    group=
        safe_text
)
Docbook_SubtitleType_strategy = st.builds(
    Docbook_SubtitleType,
    mixed=
        safe_text,
    group=
        safe_text
)
Docbook_ParamdefType_strategy = st.builds(
    Docbook_ParamdefType,
    mixed=
        safe_text
)
Docbook_FuncprototypeType_strategy = st.builds(
    Docbook_FuncprototypeType,
)
Docbook_FuncsynopsisType_strategy = st.builds(
    Docbook_FuncsynopsisType,
)
Docbook_FileNameType_strategy = st.builds(
    Docbook_FileNameType,
    mixed=
        safe_text
)
Docbook_FunctionType_strategy = st.builds(
    Docbook_FunctionType,
    mixed=
        safe_text
)
Docbook_FuncdefType_strategy = st.builds(
    Docbook_FuncdefType,
    mixed=
        safe_text
)
Docbook_FirstnameType_strategy = st.builds(
    Docbook_FirstnameType,
    mixed=
        safe_text
)
Docbook_EnvarType_strategy = st.builds(
    Docbook_EnvarType,
    mixed=
        safe_text
)
Docbook_ExampleType_strategy = st.builds(
    Docbook_ExampleType,
    id=
        safe_text
)
Docbook_TheadType_strategy = st.builds(
    Docbook_TheadType,
)
Docbook_TgroupType_strategy = st.builds(
    Docbook_TgroupType,
    rowseq=
        safe_text,
    align=
        safe_text,
    colseq=
        safe_text,
    cols=
        safe_text
)
Docbook_UlinkType_strategy = st.builds(
    Docbook_UlinkType,
    mixed=
        safe_text,
    url=
        safe_text,
    type=
        safe_text
)
Docbook_TipType_strategy = st.builds(
    Docbook_TipType,
    mixed=
        safe_text
)
Docbook_TbodyType_strategy = st.builds(
    Docbook_TbodyType,
)
Docbook_TableType_strategy = st.builds(
    Docbook_TableType,
    id=
        safe_text
)
Docbook_ProgramlistingType_strategy = st.builds(
    Docbook_ProgramlistingType,
    superscript=
        safe_text,
    format=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text,
    linenumbering=
        safe_text,
    language=
        safe_text
)
Docbook_RowType_strategy = st.builds(
    Docbook_RowType,
)
Docbook_PhraseType_strategy = st.builds(
    Docbook_PhraseType,
    id=
        safe_text
)
Docbook_PublisherType_strategy = st.builds(
    Docbook_PublisherType,
    publishername=
        safe_text
)
Docbook_OrderedlistType_strategy = st.builds(
    Docbook_OrderedlistType,
    inheritnum=
        safe_text,
    continuation=
        safe_text
)
Docbook_MediaobjectType_strategy = st.builds(
    Docbook_MediaobjectType,
)
Docbook_ListitemType_strategy = st.builds(
    Docbook_ListitemType,
)
Docbook_LinkType_strategy = st.builds(
    Docbook_LinkType,
    value=
        safe_text,
    linkend=
        safe_text,
    mixed=
        safe_text
)
Docbook_KeywordsetType_strategy = st.builds(
    Docbook_KeywordsetType,
    keyword=
        safe_text
)
Docbook_LiteralType_strategy = st.builds(
    Docbook_LiteralType,
    moreinfo=
        safe_text,
    value=
        safe_text
)
Docbook_ImportantType_strategy = st.builds(
    Docbook_ImportantType,
    group=
        safe_text,
    mixed=
        safe_text
)
Docbook_ImageobjectType_strategy = st.builds(
    Docbook_ImageobjectType,
)
Docbook_ImagedataType_strategy = st.builds(
    Docbook_ImagedataType,
    align=
        safe_text,
    fileref=
        safe_text,
    scale=
        safe_text,
    width=
        safe_text,
    depth=
        safe_text
)
Docbook_FootnoteType_strategy = st.builds(
    Docbook_FootnoteType,
    id=
        safe_text
)
Docbook_ItemizedlistType_strategy = st.builds(
    Docbook_ItemizedlistType,
)
Docbook_InformaltableType_strategy = st.builds(
    Docbook_InformaltableType,
)
Docbook_FigureType_strategy = st.builds(
    Docbook_FigureType,
    float=
        safe_text,
    id=
        safe_text
)
Docbook_EntryType_strategy = st.builds(
    Docbook_EntryType,
    align=
        safe_text,
    namest=
        safe_text,
    valign=
        safe_text,
    morerows=
        safe_text,
    nameend=
        safe_text,
    mixed=
        safe_text
)
Docbook_EmphasisType_strategy = st.builds(
    Docbook_EmphasisType,
    role=
        safe_text,
    mixed=
        safe_text
)
Docbook_DateType_strategy = st.builds(
    Docbook_DateType,
    mixed=
        safe_text
)
Docbook_CopyrightType_strategy = st.builds(
    Docbook_CopyrightType,
    year=
        safe_text,
    holder=
        safe_text,
    group=
        safe_text
)
Docbook_ConfgroupType_strategy = st.builds(
    Docbook_ConfgroupType,
    confsponsor=
        safe_text,
    confnum=
        safe_text,
    conftitle=
        safe_text
)
Docbook_EStringToStringMapEntry_strategy = st.builds(
    Docbook_EStringToStringMapEntry,
)
Docbook_DocumentRoot_strategy = st.builds(
    Docbook_DocumentRoot,
    bibliomisc=
        safe_text,
    superscript=
        safe_text,
    confsponsor=
        safe_text,
    date=
        safe_text,
    subtitle=
        safe_text,
    confnum=
        safe_text,
    publishername=
        safe_text,
    state=
        safe_text,
    mixed=
        safe_text,
    firstname=
        safe_text,
    warning=
        safe_text,
    keyword=
        safe_text,
    conftitle=
        safe_text,
    pubdate=
        safe_text,
    caution=
        safe_text
)
Docbook_CommandType_strategy = st.builds(
    Docbook_CommandType,
    mixed=
        safe_text
)
Docbook_CmdsynopsisType_strategy = st.builds(
    Docbook_CmdsynopsisType,
)
Docbook_ColspecType_strategy = st.builds(
    Docbook_ColspecType,
    colwidth=
        safe_text,
    colname=
        safe_text
)
Docbook_SectionType_strategy = st.builds(
    Docbook_SectionType,
    warning=
        safe_text,
    group=
        safe_text,
    caution=
        safe_text,
    annotations=
        safe_text
)
Docbook_NoteType_strategy = st.builds(
    Docbook_NoteType,
    group=
        safe_text,
    mixed=
        safe_text
)
Docbook_ReferenceType_strategy = st.builds(
    Docbook_ReferenceType,
    version=
        safe_text
)
Docbook_ChapterType_strategy = st.builds(
    Docbook_ChapterType,
    annotations=
        safe_text
)
Docbook_PrefaceType_strategy = st.builds(
    Docbook_PrefaceType,
)
Docbook_InfoType_strategy = st.builds(
    Docbook_InfoType,
    group=
        safe_text,
    pubdate=
        safe_text,
    date=
        safe_text,
    releaseinfo=
        safe_text,
    bibliomisc=
        safe_text,
    productname=
        safe_text
)
Docbook_BookType_strategy = st.builds(
    Docbook_BookType,
    version=
        safe_text,
    label=
        safe_text,
    lang=
        safe_text
)
Docbook_TitleType_strategy = st.builds(
    Docbook_TitleType,
    group=
        safe_text,
    mixed=
        safe_text
)
Docbook_OtheraddrType_strategy = st.builds(
    Docbook_OtheraddrType,
)
Docbook_PersonnameType_strategy = st.builds(
    Docbook_PersonnameType,
)
Docbook_AuthorType_strategy = st.builds(
    Docbook_AuthorType,
    contrib=
        safe_text
)
Docbook_AuthorinitialsType_strategy = st.builds(
    Docbook_AuthorinitialsType,
    mixed=
        safe_text
)
Docbook_ReplaceableType_strategy = st.builds(
    Docbook_ReplaceableType,
    mixed=
        safe_text
)
Docbook_OptionType_strategy = st.builds(
    Docbook_OptionType,
    mixed=
        safe_text
)
Docbook_ArgType_strategy = st.builds(
    Docbook_ArgType,
    choice=
        safe_text,
    rep=
        safe_text,
    mixed=
        safe_text
)
Docbook_AddressType_strategy = st.builds(
    Docbook_AddressType,
    state=
        safe_text,
    format=
        safe_text,
    email=
        safe_text
)
Docbook_ParaType_strategy = st.builds(
    Docbook_ParaType,
    role=
        safe_text,
    id=
        safe_text,
    mixed=
        safe_text,
    group=
        safe_text
)
Docbook_AbstractType_strategy = st.builds(
    Docbook_AbstractType,
)

@given(instance=Docbook_VarListEntryType_strategy)
@settings(max_examples=50)
def test_docbook_varlistentrytype_instantiation(instance):
    assert isinstance(instance, Docbook_VarListEntryType)



@given(instance=Docbook_VarListEntryType_strategy)
def test_docbook_varlistentrytype_termlength_setter(instance):
    original = instance.termlength
    instance.termlength = original
    assert instance.termlength == original



@given(instance=Docbook_VarListEntryType_strategy)
def test_docbook_varlistentrytype_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original

@given(instance=Docbook_TermType_strategy)
@settings(max_examples=50)
def test_docbook_termtype_instantiation(instance):
    assert isinstance(instance, Docbook_TermType)



@given(instance=Docbook_TermType_strategy)
def test_docbook_termtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_SegType_strategy)
@settings(max_examples=50)
def test_docbook_segtype_instantiation(instance):
    assert isinstance(instance, Docbook_SegType)



@given(instance=Docbook_SegType_strategy)
def test_docbook_segtype_errortext_setter(instance):
    original = instance.errortext
    instance.errortext = original
    assert instance.errortext == original



@given(instance=Docbook_SegType_strategy)
def test_docbook_segtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Docbook_SegType_strategy)
def test_docbook_segtype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Docbook_SegType_strategy)
def test_docbook_segtype_errorcode_setter(instance):
    original = instance.errorcode
    instance.errorcode = original
    assert instance.errorcode == original

@given(instance=Docbook_SegListItemType_strategy)
@settings(max_examples=50)
def test_docbook_seglistitemtype_instantiation(instance):
    assert isinstance(instance, Docbook_SegListItemType)

@given(instance=Docbook_RevdescriptionType_strategy)
@settings(max_examples=50)
def test_docbook_revdescriptiontype_instantiation(instance):
    assert isinstance(instance, Docbook_RevdescriptionType)



@given(instance=Docbook_RevdescriptionType_strategy)
def test_docbook_revdescriptiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_RevnumberType_strategy)
@settings(max_examples=50)
def test_docbook_revnumbertype_instantiation(instance):
    assert isinstance(instance, Docbook_RevnumberType)



@given(instance=Docbook_RevnumberType_strategy)
def test_docbook_revnumbertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_RevisionType_strategy)
@settings(max_examples=50)
def test_docbook_revisiontype_instantiation(instance):
    assert isinstance(instance, Docbook_RevisionType)

@given(instance=Docbook_SegmentedListType_strategy)
@settings(max_examples=50)
def test_docbook_segmentedlisttype_instantiation(instance):
    assert isinstance(instance, Docbook_SegmentedListType)



@given(instance=Docbook_SegmentedListType_strategy)
def test_docbook_segmentedlisttype_segtitle_setter(instance):
    original = instance.segtitle
    instance.segtitle = original
    assert instance.segtitle == original



@given(instance=Docbook_SegmentedListType_strategy)
def test_docbook_segmentedlisttype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook_RefEntryTitleType_strategy)
@settings(max_examples=50)
def test_docbook_refentrytitletype_instantiation(instance):
    assert isinstance(instance, Docbook_RefEntryTitleType)



@given(instance=Docbook_RefEntryTitleType_strategy)
def test_docbook_refentrytitletype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_RefSect1Type_strategy)
@settings(max_examples=50)
def test_docbook_refsect1type_instantiation(instance):
    assert isinstance(instance, Docbook_RefSect1Type)



@given(instance=Docbook_RefSect1Type_strategy)
def test_docbook_refsect1type_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Docbook_RefSect1Type_strategy)
def test_docbook_refsect1type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook_RefSynopsisDivType_strategy)
@settings(max_examples=50)
def test_docbook_refsynopsisdivtype_instantiation(instance):
    assert isinstance(instance, Docbook_RefSynopsisDivType)

@given(instance=Docbook_RefNameDivType_strategy)
@settings(max_examples=50)
def test_docbook_refnamedivtype_instantiation(instance):
    assert isinstance(instance, Docbook_RefNameDivType)



@given(instance=Docbook_RefNameDivType_strategy)
def test_docbook_refnamedivtype_refclass_setter(instance):
    original = instance.refclass
    instance.refclass = original
    assert instance.refclass == original



@given(instance=Docbook_RefNameDivType_strategy)
def test_docbook_refnamedivtype_refpurpose_setter(instance):
    original = instance.refpurpose
    instance.refpurpose = original
    assert instance.refpurpose == original



@given(instance=Docbook_RefNameDivType_strategy)
def test_docbook_refnamedivtype_refname_setter(instance):
    original = instance.refname
    instance.refname = original
    assert instance.refname == original

@given(instance=Docbook_RefMetaType_strategy)
@settings(max_examples=50)
def test_docbook_refmetatype_instantiation(instance):
    assert isinstance(instance, Docbook_RefMetaType)



@given(instance=Docbook_RefMetaType_strategy)
def test_docbook_refmetatype_manvolnum_setter(instance):
    original = instance.manvolnum
    instance.manvolnum = original
    assert instance.manvolnum == original

@given(instance=Docbook_RefEntryType_strategy)
@settings(max_examples=50)
def test_docbook_refentrytype_instantiation(instance):
    assert isinstance(instance, Docbook_RefEntryType)



@given(instance=Docbook_RefEntryType_strategy)
def test_docbook_refentrytype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Docbook_SurnameType_strategy)
@settings(max_examples=50)
def test_docbook_surnametype_instantiation(instance):
    assert isinstance(instance, Docbook_SurnameType)



@given(instance=Docbook_SurnameType_strategy)
def test_docbook_surnametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_VariableListType_strategy)
@settings(max_examples=50)
def test_docbook_variablelisttype_instantiation(instance):
    assert isinstance(instance, Docbook_VariableListType)

@given(instance=ItemizedlistType_strategy)
@settings(max_examples=50)
def test_itemizedlisttype_instantiation(instance):
    assert isinstance(instance, ItemizedlistType)

@given(instance=Docbook_ParameterType_strategy)
@settings(max_examples=50)
def test_docbook_parametertype_instantiation(instance):
    assert isinstance(instance, Docbook_ParameterType)



@given(instance=Docbook_ParameterType_strategy)
def test_docbook_parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_RevhistoryType_strategy)
@settings(max_examples=50)
def test_docbook_revhistorytype_instantiation(instance):
    assert isinstance(instance, Docbook_RevhistoryType)

@given(instance=Docbook_LegalNoticeType_strategy)
@settings(max_examples=50)
def test_docbook_legalnoticetype_instantiation(instance):
    assert isinstance(instance, Docbook_LegalNoticeType)



@given(instance=Docbook_LegalNoticeType_strategy)
def test_docbook_legalnoticetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook_SubtitleType_strategy)
@settings(max_examples=50)
def test_docbook_subtitletype_instantiation(instance):
    assert isinstance(instance, Docbook_SubtitleType)



@given(instance=Docbook_SubtitleType_strategy)
def test_docbook_subtitletype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Docbook_SubtitleType_strategy)
def test_docbook_subtitletype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook_ParamdefType_strategy)
@settings(max_examples=50)
def test_docbook_paramdeftype_instantiation(instance):
    assert isinstance(instance, Docbook_ParamdefType)



@given(instance=Docbook_ParamdefType_strategy)
def test_docbook_paramdeftype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_FuncprototypeType_strategy)
@settings(max_examples=50)
def test_docbook_funcprototypetype_instantiation(instance):
    assert isinstance(instance, Docbook_FuncprototypeType)

@given(instance=Docbook_FuncsynopsisType_strategy)
@settings(max_examples=50)
def test_docbook_funcsynopsistype_instantiation(instance):
    assert isinstance(instance, Docbook_FuncsynopsisType)

@given(instance=Docbook_FileNameType_strategy)
@settings(max_examples=50)
def test_docbook_filenametype_instantiation(instance):
    assert isinstance(instance, Docbook_FileNameType)



@given(instance=Docbook_FileNameType_strategy)
def test_docbook_filenametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_FunctionType_strategy)
@settings(max_examples=50)
def test_docbook_functiontype_instantiation(instance):
    assert isinstance(instance, Docbook_FunctionType)



@given(instance=Docbook_FunctionType_strategy)
def test_docbook_functiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_FuncdefType_strategy)
@settings(max_examples=50)
def test_docbook_funcdeftype_instantiation(instance):
    assert isinstance(instance, Docbook_FuncdefType)



@given(instance=Docbook_FuncdefType_strategy)
def test_docbook_funcdeftype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_FirstnameType_strategy)
@settings(max_examples=50)
def test_docbook_firstnametype_instantiation(instance):
    assert isinstance(instance, Docbook_FirstnameType)



@given(instance=Docbook_FirstnameType_strategy)
def test_docbook_firstnametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_EnvarType_strategy)
@settings(max_examples=50)
def test_docbook_envartype_instantiation(instance):
    assert isinstance(instance, Docbook_EnvarType)



@given(instance=Docbook_EnvarType_strategy)
def test_docbook_envartype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_ExampleType_strategy)
@settings(max_examples=50)
def test_docbook_exampletype_instantiation(instance):
    assert isinstance(instance, Docbook_ExampleType)



@given(instance=Docbook_ExampleType_strategy)
def test_docbook_exampletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook_TheadType_strategy)
@settings(max_examples=50)
def test_docbook_theadtype_instantiation(instance):
    assert isinstance(instance, Docbook_TheadType)

@given(instance=Docbook_TgroupType_strategy)
@settings(max_examples=50)
def test_docbook_tgrouptype_instantiation(instance):
    assert isinstance(instance, Docbook_TgroupType)



@given(instance=Docbook_TgroupType_strategy)
def test_docbook_tgrouptype_rowseq_setter(instance):
    original = instance.rowseq
    instance.rowseq = original
    assert instance.rowseq == original



@given(instance=Docbook_TgroupType_strategy)
def test_docbook_tgrouptype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=Docbook_TgroupType_strategy)
def test_docbook_tgrouptype_colseq_setter(instance):
    original = instance.colseq
    instance.colseq = original
    assert instance.colseq == original



@given(instance=Docbook_TgroupType_strategy)
def test_docbook_tgrouptype_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original

@given(instance=Docbook_UlinkType_strategy)
@settings(max_examples=50)
def test_docbook_ulinktype_instantiation(instance):
    assert isinstance(instance, Docbook_UlinkType)



@given(instance=Docbook_UlinkType_strategy)
def test_docbook_ulinktype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Docbook_UlinkType_strategy)
def test_docbook_ulinktype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original



@given(instance=Docbook_UlinkType_strategy)
def test_docbook_ulinktype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Docbook_TipType_strategy)
@settings(max_examples=50)
def test_docbook_tiptype_instantiation(instance):
    assert isinstance(instance, Docbook_TipType)



@given(instance=Docbook_TipType_strategy)
def test_docbook_tiptype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_TbodyType_strategy)
@settings(max_examples=50)
def test_docbook_tbodytype_instantiation(instance):
    assert isinstance(instance, Docbook_TbodyType)

@given(instance=Docbook_TableType_strategy)
@settings(max_examples=50)
def test_docbook_tabletype_instantiation(instance):
    assert isinstance(instance, Docbook_TableType)



@given(instance=Docbook_TableType_strategy)
def test_docbook_tabletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook_ProgramlistingType_strategy)
@settings(max_examples=50)
def test_docbook_programlistingtype_instantiation(instance):
    assert isinstance(instance, Docbook_ProgramlistingType)



@given(instance=Docbook_ProgramlistingType_strategy)
def test_docbook_programlistingtype_superscript_setter(instance):
    original = instance.superscript
    instance.superscript = original
    assert instance.superscript == original



@given(instance=Docbook_ProgramlistingType_strategy)
def test_docbook_programlistingtype_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=Docbook_ProgramlistingType_strategy)
def test_docbook_programlistingtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Docbook_ProgramlistingType_strategy)
def test_docbook_programlistingtype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Docbook_ProgramlistingType_strategy)
def test_docbook_programlistingtype_linenumbering_setter(instance):
    original = instance.linenumbering
    instance.linenumbering = original
    assert instance.linenumbering == original



@given(instance=Docbook_ProgramlistingType_strategy)
def test_docbook_programlistingtype_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Docbook_RowType_strategy)
@settings(max_examples=50)
def test_docbook_rowtype_instantiation(instance):
    assert isinstance(instance, Docbook_RowType)

@given(instance=Docbook_PhraseType_strategy)
@settings(max_examples=50)
def test_docbook_phrasetype_instantiation(instance):
    assert isinstance(instance, Docbook_PhraseType)



@given(instance=Docbook_PhraseType_strategy)
def test_docbook_phrasetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook_PublisherType_strategy)
@settings(max_examples=50)
def test_docbook_publishertype_instantiation(instance):
    assert isinstance(instance, Docbook_PublisherType)



@given(instance=Docbook_PublisherType_strategy)
def test_docbook_publishertype_publishername_setter(instance):
    original = instance.publishername
    instance.publishername = original
    assert instance.publishername == original

@given(instance=Docbook_OrderedlistType_strategy)
@settings(max_examples=50)
def test_docbook_orderedlisttype_instantiation(instance):
    assert isinstance(instance, Docbook_OrderedlistType)



@given(instance=Docbook_OrderedlistType_strategy)
def test_docbook_orderedlisttype_inheritnum_setter(instance):
    original = instance.inheritnum
    instance.inheritnum = original
    assert instance.inheritnum == original



@given(instance=Docbook_OrderedlistType_strategy)
def test_docbook_orderedlisttype_continuation_setter(instance):
    original = instance.continuation
    instance.continuation = original
    assert instance.continuation == original

@given(instance=Docbook_MediaobjectType_strategy)
@settings(max_examples=50)
def test_docbook_mediaobjecttype_instantiation(instance):
    assert isinstance(instance, Docbook_MediaobjectType)

@given(instance=Docbook_ListitemType_strategy)
@settings(max_examples=50)
def test_docbook_listitemtype_instantiation(instance):
    assert isinstance(instance, Docbook_ListitemType)

@given(instance=Docbook_LinkType_strategy)
@settings(max_examples=50)
def test_docbook_linktype_instantiation(instance):
    assert isinstance(instance, Docbook_LinkType)



@given(instance=Docbook_LinkType_strategy)
def test_docbook_linktype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original



@given(instance=Docbook_LinkType_strategy)
def test_docbook_linktype_linkend_setter(instance):
    original = instance.linkend
    instance.linkend = original
    assert instance.linkend == original



@given(instance=Docbook_LinkType_strategy)
def test_docbook_linktype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_KeywordsetType_strategy)
@settings(max_examples=50)
def test_docbook_keywordsettype_instantiation(instance):
    assert isinstance(instance, Docbook_KeywordsetType)



@given(instance=Docbook_KeywordsetType_strategy)
def test_docbook_keywordsettype_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=Docbook_LiteralType_strategy)
@settings(max_examples=50)
def test_docbook_literaltype_instantiation(instance):
    assert isinstance(instance, Docbook_LiteralType)



@given(instance=Docbook_LiteralType_strategy)
def test_docbook_literaltype_moreinfo_setter(instance):
    original = instance.moreinfo
    instance.moreinfo = original
    assert instance.moreinfo == original



@given(instance=Docbook_LiteralType_strategy)
def test_docbook_literaltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Docbook_ImportantType_strategy)
@settings(max_examples=50)
def test_docbook_importanttype_instantiation(instance):
    assert isinstance(instance, Docbook_ImportantType)



@given(instance=Docbook_ImportantType_strategy)
def test_docbook_importanttype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Docbook_ImportantType_strategy)
def test_docbook_importanttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_ImageobjectType_strategy)
@settings(max_examples=50)
def test_docbook_imageobjecttype_instantiation(instance):
    assert isinstance(instance, Docbook_ImageobjectType)

@given(instance=Docbook_ImagedataType_strategy)
@settings(max_examples=50)
def test_docbook_imagedatatype_instantiation(instance):
    assert isinstance(instance, Docbook_ImagedataType)



@given(instance=Docbook_ImagedataType_strategy)
def test_docbook_imagedatatype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=Docbook_ImagedataType_strategy)
def test_docbook_imagedatatype_fileref_setter(instance):
    original = instance.fileref
    instance.fileref = original
    assert instance.fileref == original



@given(instance=Docbook_ImagedataType_strategy)
def test_docbook_imagedatatype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original



@given(instance=Docbook_ImagedataType_strategy)
def test_docbook_imagedatatype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=Docbook_ImagedataType_strategy)
def test_docbook_imagedatatype_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original

@given(instance=Docbook_FootnoteType_strategy)
@settings(max_examples=50)
def test_docbook_footnotetype_instantiation(instance):
    assert isinstance(instance, Docbook_FootnoteType)



@given(instance=Docbook_FootnoteType_strategy)
def test_docbook_footnotetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook_ItemizedlistType_strategy)
@settings(max_examples=50)
def test_docbook_itemizedlisttype_instantiation(instance):
    assert isinstance(instance, Docbook_ItemizedlistType)

@given(instance=Docbook_InformaltableType_strategy)
@settings(max_examples=50)
def test_docbook_informaltabletype_instantiation(instance):
    assert isinstance(instance, Docbook_InformaltableType)

@given(instance=Docbook_FigureType_strategy)
@settings(max_examples=50)
def test_docbook_figuretype_instantiation(instance):
    assert isinstance(instance, Docbook_FigureType)



@given(instance=Docbook_FigureType_strategy)
def test_docbook_figuretype_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original



@given(instance=Docbook_FigureType_strategy)
def test_docbook_figuretype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook_EntryType_strategy)
@settings(max_examples=50)
def test_docbook_entrytype_instantiation(instance):
    assert isinstance(instance, Docbook_EntryType)



@given(instance=Docbook_EntryType_strategy)
def test_docbook_entrytype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original



@given(instance=Docbook_EntryType_strategy)
def test_docbook_entrytype_namest_setter(instance):
    original = instance.namest
    instance.namest = original
    assert instance.namest == original



@given(instance=Docbook_EntryType_strategy)
def test_docbook_entrytype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original



@given(instance=Docbook_EntryType_strategy)
def test_docbook_entrytype_morerows_setter(instance):
    original = instance.morerows
    instance.morerows = original
    assert instance.morerows == original



@given(instance=Docbook_EntryType_strategy)
def test_docbook_entrytype_nameend_setter(instance):
    original = instance.nameend
    instance.nameend = original
    assert instance.nameend == original



@given(instance=Docbook_EntryType_strategy)
def test_docbook_entrytype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_EmphasisType_strategy)
@settings(max_examples=50)
def test_docbook_emphasistype_instantiation(instance):
    assert isinstance(instance, Docbook_EmphasisType)



@given(instance=Docbook_EmphasisType_strategy)
def test_docbook_emphasistype_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=Docbook_EmphasisType_strategy)
def test_docbook_emphasistype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_DateType_strategy)
@settings(max_examples=50)
def test_docbook_datetype_instantiation(instance):
    assert isinstance(instance, Docbook_DateType)



@given(instance=Docbook_DateType_strategy)
def test_docbook_datetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_CopyrightType_strategy)
@settings(max_examples=50)
def test_docbook_copyrighttype_instantiation(instance):
    assert isinstance(instance, Docbook_CopyrightType)



@given(instance=Docbook_CopyrightType_strategy)
def test_docbook_copyrighttype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=Docbook_CopyrightType_strategy)
def test_docbook_copyrighttype_holder_setter(instance):
    original = instance.holder
    instance.holder = original
    assert instance.holder == original



@given(instance=Docbook_CopyrightType_strategy)
def test_docbook_copyrighttype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook_ConfgroupType_strategy)
@settings(max_examples=50)
def test_docbook_confgrouptype_instantiation(instance):
    assert isinstance(instance, Docbook_ConfgroupType)



@given(instance=Docbook_ConfgroupType_strategy)
def test_docbook_confgrouptype_confsponsor_setter(instance):
    original = instance.confsponsor
    instance.confsponsor = original
    assert instance.confsponsor == original



@given(instance=Docbook_ConfgroupType_strategy)
def test_docbook_confgrouptype_confnum_setter(instance):
    original = instance.confnum
    instance.confnum = original
    assert instance.confnum == original



@given(instance=Docbook_ConfgroupType_strategy)
def test_docbook_confgrouptype_conftitle_setter(instance):
    original = instance.conftitle
    instance.conftitle = original
    assert instance.conftitle == original

@given(instance=Docbook_EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_docbook_estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, Docbook_EStringToStringMapEntry)

@given(instance=Docbook_DocumentRoot_strategy)
@settings(max_examples=50)
def test_docbook_documentroot_instantiation(instance):
    assert isinstance(instance, Docbook_DocumentRoot)



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_bibliomisc_setter(instance):
    original = instance.bibliomisc
    instance.bibliomisc = original
    assert instance.bibliomisc == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_superscript_setter(instance):
    original = instance.superscript
    instance.superscript = original
    assert instance.superscript == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_confsponsor_setter(instance):
    original = instance.confsponsor
    instance.confsponsor = original
    assert instance.confsponsor == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_subtitle_setter(instance):
    original = instance.subtitle
    instance.subtitle = original
    assert instance.subtitle == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_confnum_setter(instance):
    original = instance.confnum
    instance.confnum = original
    assert instance.confnum == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_publishername_setter(instance):
    original = instance.publishername
    instance.publishername = original
    assert instance.publishername == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_warning_setter(instance):
    original = instance.warning
    instance.warning = original
    assert instance.warning == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_conftitle_setter(instance):
    original = instance.conftitle
    instance.conftitle = original
    assert instance.conftitle == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_pubdate_setter(instance):
    original = instance.pubdate
    instance.pubdate = original
    assert instance.pubdate == original



@given(instance=Docbook_DocumentRoot_strategy)
def test_docbook_documentroot_caution_setter(instance):
    original = instance.caution
    instance.caution = original
    assert instance.caution == original

@given(instance=Docbook_CommandType_strategy)
@settings(max_examples=50)
def test_docbook_commandtype_instantiation(instance):
    assert isinstance(instance, Docbook_CommandType)



@given(instance=Docbook_CommandType_strategy)
def test_docbook_commandtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_CmdsynopsisType_strategy)
@settings(max_examples=50)
def test_docbook_cmdsynopsistype_instantiation(instance):
    assert isinstance(instance, Docbook_CmdsynopsisType)

@given(instance=Docbook_ColspecType_strategy)
@settings(max_examples=50)
def test_docbook_colspectype_instantiation(instance):
    assert isinstance(instance, Docbook_ColspecType)



@given(instance=Docbook_ColspecType_strategy)
def test_docbook_colspectype_colwidth_setter(instance):
    original = instance.colwidth
    instance.colwidth = original
    assert instance.colwidth == original



@given(instance=Docbook_ColspecType_strategy)
def test_docbook_colspectype_colname_setter(instance):
    original = instance.colname
    instance.colname = original
    assert instance.colname == original

@given(instance=Docbook_SectionType_strategy)
@settings(max_examples=50)
def test_docbook_sectiontype_instantiation(instance):
    assert isinstance(instance, Docbook_SectionType)



@given(instance=Docbook_SectionType_strategy)
def test_docbook_sectiontype_warning_setter(instance):
    original = instance.warning
    instance.warning = original
    assert instance.warning == original



@given(instance=Docbook_SectionType_strategy)
def test_docbook_sectiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Docbook_SectionType_strategy)
def test_docbook_sectiontype_caution_setter(instance):
    original = instance.caution
    instance.caution = original
    assert instance.caution == original



@given(instance=Docbook_SectionType_strategy)
def test_docbook_sectiontype_annotations_setter(instance):
    original = instance.annotations
    instance.annotations = original
    assert instance.annotations == original

@given(instance=Docbook_NoteType_strategy)
@settings(max_examples=50)
def test_docbook_notetype_instantiation(instance):
    assert isinstance(instance, Docbook_NoteType)



@given(instance=Docbook_NoteType_strategy)
def test_docbook_notetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Docbook_NoteType_strategy)
def test_docbook_notetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_ReferenceType_strategy)
@settings(max_examples=50)
def test_docbook_referencetype_instantiation(instance):
    assert isinstance(instance, Docbook_ReferenceType)



@given(instance=Docbook_ReferenceType_strategy)
def test_docbook_referencetype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Docbook_ChapterType_strategy)
@settings(max_examples=50)
def test_docbook_chaptertype_instantiation(instance):
    assert isinstance(instance, Docbook_ChapterType)



@given(instance=Docbook_ChapterType_strategy)
def test_docbook_chaptertype_annotations_setter(instance):
    original = instance.annotations
    instance.annotations = original
    assert instance.annotations == original

@given(instance=Docbook_PrefaceType_strategy)
@settings(max_examples=50)
def test_docbook_prefacetype_instantiation(instance):
    assert isinstance(instance, Docbook_PrefaceType)

@given(instance=Docbook_InfoType_strategy)
@settings(max_examples=50)
def test_docbook_infotype_instantiation(instance):
    assert isinstance(instance, Docbook_InfoType)



@given(instance=Docbook_InfoType_strategy)
def test_docbook_infotype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Docbook_InfoType_strategy)
def test_docbook_infotype_pubdate_setter(instance):
    original = instance.pubdate
    instance.pubdate = original
    assert instance.pubdate == original



@given(instance=Docbook_InfoType_strategy)
def test_docbook_infotype_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original



@given(instance=Docbook_InfoType_strategy)
def test_docbook_infotype_releaseinfo_setter(instance):
    original = instance.releaseinfo
    instance.releaseinfo = original
    assert instance.releaseinfo == original



@given(instance=Docbook_InfoType_strategy)
def test_docbook_infotype_bibliomisc_setter(instance):
    original = instance.bibliomisc
    instance.bibliomisc = original
    assert instance.bibliomisc == original



@given(instance=Docbook_InfoType_strategy)
def test_docbook_infotype_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original

@given(instance=Docbook_BookType_strategy)
@settings(max_examples=50)
def test_docbook_booktype_instantiation(instance):
    assert isinstance(instance, Docbook_BookType)



@given(instance=Docbook_BookType_strategy)
def test_docbook_booktype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original



@given(instance=Docbook_BookType_strategy)
def test_docbook_booktype_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original



@given(instance=Docbook_BookType_strategy)
def test_docbook_booktype_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=Docbook_TitleType_strategy)
@settings(max_examples=50)
def test_docbook_titletype_instantiation(instance):
    assert isinstance(instance, Docbook_TitleType)



@given(instance=Docbook_TitleType_strategy)
def test_docbook_titletype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original



@given(instance=Docbook_TitleType_strategy)
def test_docbook_titletype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_OtheraddrType_strategy)
@settings(max_examples=50)
def test_docbook_otheraddrtype_instantiation(instance):
    assert isinstance(instance, Docbook_OtheraddrType)

@given(instance=Docbook_PersonnameType_strategy)
@settings(max_examples=50)
def test_docbook_personnametype_instantiation(instance):
    assert isinstance(instance, Docbook_PersonnameType)

@given(instance=Docbook_AuthorType_strategy)
@settings(max_examples=50)
def test_docbook_authortype_instantiation(instance):
    assert isinstance(instance, Docbook_AuthorType)



@given(instance=Docbook_AuthorType_strategy)
def test_docbook_authortype_contrib_setter(instance):
    original = instance.contrib
    instance.contrib = original
    assert instance.contrib == original

@given(instance=Docbook_AuthorinitialsType_strategy)
@settings(max_examples=50)
def test_docbook_authorinitialstype_instantiation(instance):
    assert isinstance(instance, Docbook_AuthorinitialsType)



@given(instance=Docbook_AuthorinitialsType_strategy)
def test_docbook_authorinitialstype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_ReplaceableType_strategy)
@settings(max_examples=50)
def test_docbook_replaceabletype_instantiation(instance):
    assert isinstance(instance, Docbook_ReplaceableType)



@given(instance=Docbook_ReplaceableType_strategy)
def test_docbook_replaceabletype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_OptionType_strategy)
@settings(max_examples=50)
def test_docbook_optiontype_instantiation(instance):
    assert isinstance(instance, Docbook_OptionType)



@given(instance=Docbook_OptionType_strategy)
def test_docbook_optiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_ArgType_strategy)
@settings(max_examples=50)
def test_docbook_argtype_instantiation(instance):
    assert isinstance(instance, Docbook_ArgType)



@given(instance=Docbook_ArgType_strategy)
def test_docbook_argtype_choice_setter(instance):
    original = instance.choice
    instance.choice = original
    assert instance.choice == original



@given(instance=Docbook_ArgType_strategy)
def test_docbook_argtype_rep_setter(instance):
    original = instance.rep
    instance.rep = original
    assert instance.rep == original



@given(instance=Docbook_ArgType_strategy)
def test_docbook_argtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook_AddressType_strategy)
@settings(max_examples=50)
def test_docbook_addresstype_instantiation(instance):
    assert isinstance(instance, Docbook_AddressType)



@given(instance=Docbook_AddressType_strategy)
def test_docbook_addresstype_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original



@given(instance=Docbook_AddressType_strategy)
def test_docbook_addresstype_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original



@given(instance=Docbook_AddressType_strategy)
def test_docbook_addresstype_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Docbook_ParaType_strategy)
@settings(max_examples=50)
def test_docbook_paratype_instantiation(instance):
    assert isinstance(instance, Docbook_ParaType)



@given(instance=Docbook_ParaType_strategy)
def test_docbook_paratype_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original



@given(instance=Docbook_ParaType_strategy)
def test_docbook_paratype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Docbook_ParaType_strategy)
def test_docbook_paratype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original



@given(instance=Docbook_ParaType_strategy)
def test_docbook_paratype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook_AbstractType_strategy)
@settings(max_examples=50)
def test_docbook_abstracttype_instantiation(instance):
    assert isinstance(instance, Docbook_AbstractType)
