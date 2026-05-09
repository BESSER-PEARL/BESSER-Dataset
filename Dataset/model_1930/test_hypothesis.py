import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    Docbook::VarListEntryType,
    Docbook::TermType,
    Docbook::SegType,
    Docbook::SegListItemType,
    Docbook::RevdescriptionType,
    Docbook::RevnumberType,
    Docbook::RevisionType,
    Docbook::SegmentedListType,
    Docbook::RefEntryTitleType,
    Docbook::RefSect1Type,
    Docbook::RefSynopsisDivType,
    Docbook::RefNameDivType,
    Docbook::RefMetaType,
    Docbook::RefEntryType,
    Docbook::SurnameType,
    Docbook::VariableListType,
    ItemizedlistType,
    Docbook::ParameterType,
    Docbook::RevhistoryType,
    Docbook::LegalNoticeType,
    Docbook::SubtitleType,
    Docbook::ParamdefType,
    Docbook::FuncprototypeType,
    Docbook::FuncsynopsisType,
    Docbook::FileNameType,
    Docbook::FunctionType,
    Docbook::FuncdefType,
    Docbook::FirstnameType,
    Docbook::EnvarType,
    Docbook::ExampleType,
    Docbook::TheadType,
    Docbook::TgroupType,
    Docbook::UlinkType,
    Docbook::TipType,
    Docbook::TbodyType,
    Docbook::TableType,
    Docbook::ProgramlistingType,
    Docbook::RowType,
    Docbook::PhraseType,
    Docbook::PublisherType,
    Docbook::OrderedlistType,
    Docbook::MediaobjectType,
    Docbook::ListitemType,
    Docbook::LinkType,
    Docbook::KeywordsetType,
    Docbook::LiteralType,
    Docbook::ImportantType,
    Docbook::ImageobjectType,
    Docbook::ImagedataType,
    Docbook::FootnoteType,
    Docbook::ItemizedlistType,
    Docbook::InformaltableType,
    Docbook::FigureType,
    Docbook::EntryType,
    Docbook::EmphasisType,
    Docbook::DateType,
    Docbook::CopyrightType,
    Docbook::ConfgroupType,
    Docbook::EStringToStringMapEntry,
    Docbook::DocumentRoot,
    Docbook::CommandType,
    Docbook::CmdsynopsisType,
    Docbook::ColspecType,
    Docbook::SectionType,
    Docbook::NoteType,
    Docbook::ReferenceType,
    Docbook::ChapterType,
    Docbook::ArgType,
    Docbook::AddressType,
    Docbook::ParaType,
    Docbook::AbstractType,
    Docbook::PrefaceType,
    Docbook::InfoType,
    Docbook::BookType,
    Docbook::TitleType,
    Docbook::OtheraddrType,
    Docbook::PersonnameType,
    Docbook::AuthorType,
    Docbook::AuthorinitialsType,
    Docbook::ReplaceableType,
    Docbook::OptionType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_docbook::varlistentrytype_is_not_abstract():
    assert not inspect.isabstract(Docbook::VarListEntryType)


def test_docbook::varlistentrytype_constructor_exists():
    assert callable(Docbook::VarListEntryType.__init__)


def test_docbook::varlistentrytype_constructor_args():
    sig = inspect.signature(Docbook::VarListEntryType.__init__)
    params = list(sig.parameters.keys())
    assert "spacing" in params, "Missing parameter 'spacing'"
    assert "termlength" in params, "Missing parameter 'termlength'"

def test_docbook::varlistentrytype_has_spacing():
    assert hasattr(Docbook::VarListEntryType, "spacing")
    descriptor = None
    for klass in Docbook::VarListEntryType.__mro__:
        if "spacing" in klass.__dict__:
            descriptor = klass.__dict__["spacing"]
            break
    assert isinstance(descriptor, property)

def test_docbook::varlistentrytype_has_termlength():
    assert hasattr(Docbook::VarListEntryType, "termlength")
    descriptor = None
    for klass in Docbook::VarListEntryType.__mro__:
        if "termlength" in klass.__dict__:
            descriptor = klass.__dict__["termlength"]
            break
    assert isinstance(descriptor, property)



def test_docbook::termtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::TermType)


def test_docbook::termtype_constructor_exists():
    assert callable(Docbook::TermType.__init__)


def test_docbook::termtype_constructor_args():
    sig = inspect.signature(Docbook::TermType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::termtype_has_mixed():
    assert hasattr(Docbook::TermType, "mixed")
    descriptor = None
    for klass in Docbook::TermType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::segtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::SegType)


def test_docbook::segtype_constructor_exists():
    assert callable(Docbook::SegType.__init__)


def test_docbook::segtype_constructor_args():
    sig = inspect.signature(Docbook::SegType.__init__)
    params = list(sig.parameters.keys())
    assert "errortext" in params, "Missing parameter 'errortext'"
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "errorcode" in params, "Missing parameter 'errorcode'"

def test_docbook::segtype_has_errortext():
    assert hasattr(Docbook::SegType, "errortext")
    descriptor = None
    for klass in Docbook::SegType.__mro__:
        if "errortext" in klass.__dict__:
            descriptor = klass.__dict__["errortext"]
            break
    assert isinstance(descriptor, property)

def test_docbook::segtype_has_group():
    assert hasattr(Docbook::SegType, "group")
    descriptor = None
    for klass in Docbook::SegType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::segtype_has_mixed():
    assert hasattr(Docbook::SegType, "mixed")
    descriptor = None
    for klass in Docbook::SegType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::segtype_has_errorcode():
    assert hasattr(Docbook::SegType, "errorcode")
    descriptor = None
    for klass in Docbook::SegType.__mro__:
        if "errorcode" in klass.__dict__:
            descriptor = klass.__dict__["errorcode"]
            break
    assert isinstance(descriptor, property)



def test_docbook::seglistitemtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::SegListItemType)


def test_docbook::seglistitemtype_constructor_exists():
    assert callable(Docbook::SegListItemType.__init__)


def test_docbook::seglistitemtype_constructor_args():
    sig = inspect.signature(Docbook::SegListItemType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::revdescriptiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RevdescriptionType)


def test_docbook::revdescriptiontype_constructor_exists():
    assert callable(Docbook::RevdescriptionType.__init__)


def test_docbook::revdescriptiontype_constructor_args():
    sig = inspect.signature(Docbook::RevdescriptionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::revdescriptiontype_has_mixed():
    assert hasattr(Docbook::RevdescriptionType, "mixed")
    descriptor = None
    for klass in Docbook::RevdescriptionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::revnumbertype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RevnumberType)


def test_docbook::revnumbertype_constructor_exists():
    assert callable(Docbook::RevnumberType.__init__)


def test_docbook::revnumbertype_constructor_args():
    sig = inspect.signature(Docbook::RevnumberType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::revnumbertype_has_mixed():
    assert hasattr(Docbook::RevnumberType, "mixed")
    descriptor = None
    for klass in Docbook::RevnumberType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::revisiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RevisionType)


def test_docbook::revisiontype_constructor_exists():
    assert callable(Docbook::RevisionType.__init__)


def test_docbook::revisiontype_constructor_args():
    sig = inspect.signature(Docbook::RevisionType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::segmentedlisttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::SegmentedListType)


def test_docbook::segmentedlisttype_constructor_exists():
    assert callable(Docbook::SegmentedListType.__init__)


def test_docbook::segmentedlisttype_constructor_args():
    sig = inspect.signature(Docbook::SegmentedListType.__init__)
    params = list(sig.parameters.keys())
    assert "segtitle" in params, "Missing parameter 'segtitle'"
    assert "group" in params, "Missing parameter 'group'"

def test_docbook::segmentedlisttype_has_segtitle():
    assert hasattr(Docbook::SegmentedListType, "segtitle")
    descriptor = None
    for klass in Docbook::SegmentedListType.__mro__:
        if "segtitle" in klass.__dict__:
            descriptor = klass.__dict__["segtitle"]
            break
    assert isinstance(descriptor, property)

def test_docbook::segmentedlisttype_has_group():
    assert hasattr(Docbook::SegmentedListType, "group")
    descriptor = None
    for klass in Docbook::SegmentedListType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook::refentrytitletype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RefEntryTitleType)


def test_docbook::refentrytitletype_constructor_exists():
    assert callable(Docbook::RefEntryTitleType.__init__)


def test_docbook::refentrytitletype_constructor_args():
    sig = inspect.signature(Docbook::RefEntryTitleType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::refentrytitletype_has_mixed():
    assert hasattr(Docbook::RefEntryTitleType, "mixed")
    descriptor = None
    for klass in Docbook::RefEntryTitleType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::refsect1type_is_not_abstract():
    assert not inspect.isabstract(Docbook::RefSect1Type)


def test_docbook::refsect1type_constructor_exists():
    assert callable(Docbook::RefSect1Type.__init__)


def test_docbook::refsect1type_constructor_args():
    sig = inspect.signature(Docbook::RefSect1Type.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "group" in params, "Missing parameter 'group'"

def test_docbook::refsect1type_has_id():
    assert hasattr(Docbook::RefSect1Type, "id")
    descriptor = None
    for klass in Docbook::RefSect1Type.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_docbook::refsect1type_has_group():
    assert hasattr(Docbook::RefSect1Type, "group")
    descriptor = None
    for klass in Docbook::RefSect1Type.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook::refsynopsisdivtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RefSynopsisDivType)


def test_docbook::refsynopsisdivtype_constructor_exists():
    assert callable(Docbook::RefSynopsisDivType.__init__)


def test_docbook::refsynopsisdivtype_constructor_args():
    sig = inspect.signature(Docbook::RefSynopsisDivType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::refnamedivtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RefNameDivType)


def test_docbook::refnamedivtype_constructor_exists():
    assert callable(Docbook::RefNameDivType.__init__)


def test_docbook::refnamedivtype_constructor_args():
    sig = inspect.signature(Docbook::RefNameDivType.__init__)
    params = list(sig.parameters.keys())
    assert "refname" in params, "Missing parameter 'refname'"
    assert "refpurpose" in params, "Missing parameter 'refpurpose'"
    assert "refclass" in params, "Missing parameter 'refclass'"

def test_docbook::refnamedivtype_has_refname():
    assert hasattr(Docbook::RefNameDivType, "refname")
    descriptor = None
    for klass in Docbook::RefNameDivType.__mro__:
        if "refname" in klass.__dict__:
            descriptor = klass.__dict__["refname"]
            break
    assert isinstance(descriptor, property)

def test_docbook::refnamedivtype_has_refpurpose():
    assert hasattr(Docbook::RefNameDivType, "refpurpose")
    descriptor = None
    for klass in Docbook::RefNameDivType.__mro__:
        if "refpurpose" in klass.__dict__:
            descriptor = klass.__dict__["refpurpose"]
            break
    assert isinstance(descriptor, property)

def test_docbook::refnamedivtype_has_refclass():
    assert hasattr(Docbook::RefNameDivType, "refclass")
    descriptor = None
    for klass in Docbook::RefNameDivType.__mro__:
        if "refclass" in klass.__dict__:
            descriptor = klass.__dict__["refclass"]
            break
    assert isinstance(descriptor, property)



def test_docbook::refmetatype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RefMetaType)


def test_docbook::refmetatype_constructor_exists():
    assert callable(Docbook::RefMetaType.__init__)


def test_docbook::refmetatype_constructor_args():
    sig = inspect.signature(Docbook::RefMetaType.__init__)
    params = list(sig.parameters.keys())
    assert "manvolnum" in params, "Missing parameter 'manvolnum'"

def test_docbook::refmetatype_has_manvolnum():
    assert hasattr(Docbook::RefMetaType, "manvolnum")
    descriptor = None
    for klass in Docbook::RefMetaType.__mro__:
        if "manvolnum" in klass.__dict__:
            descriptor = klass.__dict__["manvolnum"]
            break
    assert isinstance(descriptor, property)



def test_docbook::refentrytype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RefEntryType)


def test_docbook::refentrytype_constructor_exists():
    assert callable(Docbook::RefEntryType.__init__)


def test_docbook::refentrytype_constructor_args():
    sig = inspect.signature(Docbook::RefEntryType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_docbook::refentrytype_has_version():
    assert hasattr(Docbook::RefEntryType, "version")
    descriptor = None
    for klass in Docbook::RefEntryType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_docbook::surnametype_is_not_abstract():
    assert not inspect.isabstract(Docbook::SurnameType)


def test_docbook::surnametype_constructor_exists():
    assert callable(Docbook::SurnameType.__init__)


def test_docbook::surnametype_constructor_args():
    sig = inspect.signature(Docbook::SurnameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::surnametype_has_mixed():
    assert hasattr(Docbook::SurnameType, "mixed")
    descriptor = None
    for klass in Docbook::SurnameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::variablelisttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::VariableListType)


def test_docbook::variablelisttype_constructor_exists():
    assert callable(Docbook::VariableListType.__init__)


def test_docbook::variablelisttype_constructor_args():
    sig = inspect.signature(Docbook::VariableListType.__init__)
    params = list(sig.parameters.keys())



def test_itemizedlisttype_is_not_abstract():
    assert not inspect.isabstract(ItemizedlistType)


def test_itemizedlisttype_constructor_exists():
    assert callable(ItemizedlistType.__init__)


def test_itemizedlisttype_constructor_args():
    sig = inspect.signature(ItemizedlistType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::parametertype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ParameterType)


def test_docbook::parametertype_constructor_exists():
    assert callable(Docbook::ParameterType.__init__)


def test_docbook::parametertype_constructor_args():
    sig = inspect.signature(Docbook::ParameterType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::parametertype_has_mixed():
    assert hasattr(Docbook::ParameterType, "mixed")
    descriptor = None
    for klass in Docbook::ParameterType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::revhistorytype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RevhistoryType)


def test_docbook::revhistorytype_constructor_exists():
    assert callable(Docbook::RevhistoryType.__init__)


def test_docbook::revhistorytype_constructor_args():
    sig = inspect.signature(Docbook::RevhistoryType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::legalnoticetype_is_not_abstract():
    assert not inspect.isabstract(Docbook::LegalNoticeType)


def test_docbook::legalnoticetype_constructor_exists():
    assert callable(Docbook::LegalNoticeType.__init__)


def test_docbook::legalnoticetype_constructor_args():
    sig = inspect.signature(Docbook::LegalNoticeType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"

def test_docbook::legalnoticetype_has_group():
    assert hasattr(Docbook::LegalNoticeType, "group")
    descriptor = None
    for klass in Docbook::LegalNoticeType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook::subtitletype_is_not_abstract():
    assert not inspect.isabstract(Docbook::SubtitleType)


def test_docbook::subtitletype_constructor_exists():
    assert callable(Docbook::SubtitleType.__init__)


def test_docbook::subtitletype_constructor_args():
    sig = inspect.signature(Docbook::SubtitleType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::subtitletype_has_group():
    assert hasattr(Docbook::SubtitleType, "group")
    descriptor = None
    for klass in Docbook::SubtitleType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::subtitletype_has_mixed():
    assert hasattr(Docbook::SubtitleType, "mixed")
    descriptor = None
    for klass in Docbook::SubtitleType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::paramdeftype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ParamdefType)


def test_docbook::paramdeftype_constructor_exists():
    assert callable(Docbook::ParamdefType.__init__)


def test_docbook::paramdeftype_constructor_args():
    sig = inspect.signature(Docbook::ParamdefType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::paramdeftype_has_mixed():
    assert hasattr(Docbook::ParamdefType, "mixed")
    descriptor = None
    for klass in Docbook::ParamdefType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::funcprototypetype_is_not_abstract():
    assert not inspect.isabstract(Docbook::FuncprototypeType)


def test_docbook::funcprototypetype_constructor_exists():
    assert callable(Docbook::FuncprototypeType.__init__)


def test_docbook::funcprototypetype_constructor_args():
    sig = inspect.signature(Docbook::FuncprototypeType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::funcsynopsistype_is_not_abstract():
    assert not inspect.isabstract(Docbook::FuncsynopsisType)


def test_docbook::funcsynopsistype_constructor_exists():
    assert callable(Docbook::FuncsynopsisType.__init__)


def test_docbook::funcsynopsistype_constructor_args():
    sig = inspect.signature(Docbook::FuncsynopsisType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::filenametype_is_not_abstract():
    assert not inspect.isabstract(Docbook::FileNameType)


def test_docbook::filenametype_constructor_exists():
    assert callable(Docbook::FileNameType.__init__)


def test_docbook::filenametype_constructor_args():
    sig = inspect.signature(Docbook::FileNameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::filenametype_has_mixed():
    assert hasattr(Docbook::FileNameType, "mixed")
    descriptor = None
    for klass in Docbook::FileNameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::functiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook::FunctionType)


def test_docbook::functiontype_constructor_exists():
    assert callable(Docbook::FunctionType.__init__)


def test_docbook::functiontype_constructor_args():
    sig = inspect.signature(Docbook::FunctionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::functiontype_has_mixed():
    assert hasattr(Docbook::FunctionType, "mixed")
    descriptor = None
    for klass in Docbook::FunctionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::funcdeftype_is_not_abstract():
    assert not inspect.isabstract(Docbook::FuncdefType)


def test_docbook::funcdeftype_constructor_exists():
    assert callable(Docbook::FuncdefType.__init__)


def test_docbook::funcdeftype_constructor_args():
    sig = inspect.signature(Docbook::FuncdefType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::funcdeftype_has_mixed():
    assert hasattr(Docbook::FuncdefType, "mixed")
    descriptor = None
    for klass in Docbook::FuncdefType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::firstnametype_is_not_abstract():
    assert not inspect.isabstract(Docbook::FirstnameType)


def test_docbook::firstnametype_constructor_exists():
    assert callable(Docbook::FirstnameType.__init__)


def test_docbook::firstnametype_constructor_args():
    sig = inspect.signature(Docbook::FirstnameType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::firstnametype_has_mixed():
    assert hasattr(Docbook::FirstnameType, "mixed")
    descriptor = None
    for klass in Docbook::FirstnameType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::envartype_is_not_abstract():
    assert not inspect.isabstract(Docbook::EnvarType)


def test_docbook::envartype_constructor_exists():
    assert callable(Docbook::EnvarType.__init__)


def test_docbook::envartype_constructor_args():
    sig = inspect.signature(Docbook::EnvarType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::envartype_has_mixed():
    assert hasattr(Docbook::EnvarType, "mixed")
    descriptor = None
    for klass in Docbook::EnvarType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::exampletype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ExampleType)


def test_docbook::exampletype_constructor_exists():
    assert callable(Docbook::ExampleType.__init__)


def test_docbook::exampletype_constructor_args():
    sig = inspect.signature(Docbook::ExampleType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook::exampletype_has_id():
    assert hasattr(Docbook::ExampleType, "id")
    descriptor = None
    for klass in Docbook::ExampleType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook::theadtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::TheadType)


def test_docbook::theadtype_constructor_exists():
    assert callable(Docbook::TheadType.__init__)


def test_docbook::theadtype_constructor_args():
    sig = inspect.signature(Docbook::TheadType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::tgrouptype_is_not_abstract():
    assert not inspect.isabstract(Docbook::TgroupType)


def test_docbook::tgrouptype_constructor_exists():
    assert callable(Docbook::TgroupType.__init__)


def test_docbook::tgrouptype_constructor_args():
    sig = inspect.signature(Docbook::TgroupType.__init__)
    params = list(sig.parameters.keys())
    assert "colseq" in params, "Missing parameter 'colseq'"
    assert "cols" in params, "Missing parameter 'cols'"
    assert "rowseq" in params, "Missing parameter 'rowseq'"
    assert "align" in params, "Missing parameter 'align'"

def test_docbook::tgrouptype_has_colseq():
    assert hasattr(Docbook::TgroupType, "colseq")
    descriptor = None
    for klass in Docbook::TgroupType.__mro__:
        if "colseq" in klass.__dict__:
            descriptor = klass.__dict__["colseq"]
            break
    assert isinstance(descriptor, property)

def test_docbook::tgrouptype_has_cols():
    assert hasattr(Docbook::TgroupType, "cols")
    descriptor = None
    for klass in Docbook::TgroupType.__mro__:
        if "cols" in klass.__dict__:
            descriptor = klass.__dict__["cols"]
            break
    assert isinstance(descriptor, property)

def test_docbook::tgrouptype_has_rowseq():
    assert hasattr(Docbook::TgroupType, "rowseq")
    descriptor = None
    for klass in Docbook::TgroupType.__mro__:
        if "rowseq" in klass.__dict__:
            descriptor = klass.__dict__["rowseq"]
            break
    assert isinstance(descriptor, property)

def test_docbook::tgrouptype_has_align():
    assert hasattr(Docbook::TgroupType, "align")
    descriptor = None
    for klass in Docbook::TgroupType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)



def test_docbook::ulinktype_is_not_abstract():
    assert not inspect.isabstract(Docbook::UlinkType)


def test_docbook::ulinktype_constructor_exists():
    assert callable(Docbook::UlinkType.__init__)


def test_docbook::ulinktype_constructor_args():
    sig = inspect.signature(Docbook::UlinkType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "type" in params, "Missing parameter 'type'"
    assert "url" in params, "Missing parameter 'url'"

def test_docbook::ulinktype_has_mixed():
    assert hasattr(Docbook::UlinkType, "mixed")
    descriptor = None
    for klass in Docbook::UlinkType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::ulinktype_has_type():
    assert hasattr(Docbook::UlinkType, "type")
    descriptor = None
    for klass in Docbook::UlinkType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_docbook::ulinktype_has_url():
    assert hasattr(Docbook::UlinkType, "url")
    descriptor = None
    for klass in Docbook::UlinkType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_docbook::tiptype_is_not_abstract():
    assert not inspect.isabstract(Docbook::TipType)


def test_docbook::tiptype_constructor_exists():
    assert callable(Docbook::TipType.__init__)


def test_docbook::tiptype_constructor_args():
    sig = inspect.signature(Docbook::TipType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::tiptype_has_mixed():
    assert hasattr(Docbook::TipType, "mixed")
    descriptor = None
    for klass in Docbook::TipType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::tbodytype_is_not_abstract():
    assert not inspect.isabstract(Docbook::TbodyType)


def test_docbook::tbodytype_constructor_exists():
    assert callable(Docbook::TbodyType.__init__)


def test_docbook::tbodytype_constructor_args():
    sig = inspect.signature(Docbook::TbodyType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::tabletype_is_not_abstract():
    assert not inspect.isabstract(Docbook::TableType)


def test_docbook::tabletype_constructor_exists():
    assert callable(Docbook::TableType.__init__)


def test_docbook::tabletype_constructor_args():
    sig = inspect.signature(Docbook::TableType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook::tabletype_has_id():
    assert hasattr(Docbook::TableType, "id")
    descriptor = None
    for klass in Docbook::TableType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook::programlistingtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ProgramlistingType)


def test_docbook::programlistingtype_constructor_exists():
    assert callable(Docbook::ProgramlistingType.__init__)


def test_docbook::programlistingtype_constructor_args():
    sig = inspect.signature(Docbook::ProgramlistingType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"
    assert "language" in params, "Missing parameter 'language'"
    assert "superscript" in params, "Missing parameter 'superscript'"
    assert "linenumbering" in params, "Missing parameter 'linenumbering'"
    assert "format" in params, "Missing parameter 'format'"

def test_docbook::programlistingtype_has_mixed():
    assert hasattr(Docbook::ProgramlistingType, "mixed")
    descriptor = None
    for klass in Docbook::ProgramlistingType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::programlistingtype_has_group():
    assert hasattr(Docbook::ProgramlistingType, "group")
    descriptor = None
    for klass in Docbook::ProgramlistingType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::programlistingtype_has_language():
    assert hasattr(Docbook::ProgramlistingType, "language")
    descriptor = None
    for klass in Docbook::ProgramlistingType.__mro__:
        if "language" in klass.__dict__:
            descriptor = klass.__dict__["language"]
            break
    assert isinstance(descriptor, property)

def test_docbook::programlistingtype_has_superscript():
    assert hasattr(Docbook::ProgramlistingType, "superscript")
    descriptor = None
    for klass in Docbook::ProgramlistingType.__mro__:
        if "superscript" in klass.__dict__:
            descriptor = klass.__dict__["superscript"]
            break
    assert isinstance(descriptor, property)

def test_docbook::programlistingtype_has_linenumbering():
    assert hasattr(Docbook::ProgramlistingType, "linenumbering")
    descriptor = None
    for klass in Docbook::ProgramlistingType.__mro__:
        if "linenumbering" in klass.__dict__:
            descriptor = klass.__dict__["linenumbering"]
            break
    assert isinstance(descriptor, property)

def test_docbook::programlistingtype_has_format():
    assert hasattr(Docbook::ProgramlistingType, "format")
    descriptor = None
    for klass in Docbook::ProgramlistingType.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_docbook::rowtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::RowType)


def test_docbook::rowtype_constructor_exists():
    assert callable(Docbook::RowType.__init__)


def test_docbook::rowtype_constructor_args():
    sig = inspect.signature(Docbook::RowType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::phrasetype_is_not_abstract():
    assert not inspect.isabstract(Docbook::PhraseType)


def test_docbook::phrasetype_constructor_exists():
    assert callable(Docbook::PhraseType.__init__)


def test_docbook::phrasetype_constructor_args():
    sig = inspect.signature(Docbook::PhraseType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook::phrasetype_has_id():
    assert hasattr(Docbook::PhraseType, "id")
    descriptor = None
    for klass in Docbook::PhraseType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook::publishertype_is_not_abstract():
    assert not inspect.isabstract(Docbook::PublisherType)


def test_docbook::publishertype_constructor_exists():
    assert callable(Docbook::PublisherType.__init__)


def test_docbook::publishertype_constructor_args():
    sig = inspect.signature(Docbook::PublisherType.__init__)
    params = list(sig.parameters.keys())
    assert "publishername" in params, "Missing parameter 'publishername'"

def test_docbook::publishertype_has_publishername():
    assert hasattr(Docbook::PublisherType, "publishername")
    descriptor = None
    for klass in Docbook::PublisherType.__mro__:
        if "publishername" in klass.__dict__:
            descriptor = klass.__dict__["publishername"]
            break
    assert isinstance(descriptor, property)



def test_docbook::orderedlisttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::OrderedlistType)


def test_docbook::orderedlisttype_constructor_exists():
    assert callable(Docbook::OrderedlistType.__init__)


def test_docbook::orderedlisttype_constructor_args():
    sig = inspect.signature(Docbook::OrderedlistType.__init__)
    params = list(sig.parameters.keys())
    assert "inheritnum" in params, "Missing parameter 'inheritnum'"
    assert "continuation" in params, "Missing parameter 'continuation'"

def test_docbook::orderedlisttype_has_inheritnum():
    assert hasattr(Docbook::OrderedlistType, "inheritnum")
    descriptor = None
    for klass in Docbook::OrderedlistType.__mro__:
        if "inheritnum" in klass.__dict__:
            descriptor = klass.__dict__["inheritnum"]
            break
    assert isinstance(descriptor, property)

def test_docbook::orderedlisttype_has_continuation():
    assert hasattr(Docbook::OrderedlistType, "continuation")
    descriptor = None
    for klass in Docbook::OrderedlistType.__mro__:
        if "continuation" in klass.__dict__:
            descriptor = klass.__dict__["continuation"]
            break
    assert isinstance(descriptor, property)



def test_docbook::mediaobjecttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::MediaobjectType)


def test_docbook::mediaobjecttype_constructor_exists():
    assert callable(Docbook::MediaobjectType.__init__)


def test_docbook::mediaobjecttype_constructor_args():
    sig = inspect.signature(Docbook::MediaobjectType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::listitemtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ListitemType)


def test_docbook::listitemtype_constructor_exists():
    assert callable(Docbook::ListitemType.__init__)


def test_docbook::listitemtype_constructor_args():
    sig = inspect.signature(Docbook::ListitemType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::linktype_is_not_abstract():
    assert not inspect.isabstract(Docbook::LinkType)


def test_docbook::linktype_constructor_exists():
    assert callable(Docbook::LinkType.__init__)


def test_docbook::linktype_constructor_args():
    sig = inspect.signature(Docbook::LinkType.__init__)
    params = list(sig.parameters.keys())
    assert "linkend" in params, "Missing parameter 'linkend'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "value" in params, "Missing parameter 'value'"

def test_docbook::linktype_has_linkend():
    assert hasattr(Docbook::LinkType, "linkend")
    descriptor = None
    for klass in Docbook::LinkType.__mro__:
        if "linkend" in klass.__dict__:
            descriptor = klass.__dict__["linkend"]
            break
    assert isinstance(descriptor, property)

def test_docbook::linktype_has_mixed():
    assert hasattr(Docbook::LinkType, "mixed")
    descriptor = None
    for klass in Docbook::LinkType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::linktype_has_value():
    assert hasattr(Docbook::LinkType, "value")
    descriptor = None
    for klass in Docbook::LinkType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_docbook::keywordsettype_is_not_abstract():
    assert not inspect.isabstract(Docbook::KeywordsetType)


def test_docbook::keywordsettype_constructor_exists():
    assert callable(Docbook::KeywordsetType.__init__)


def test_docbook::keywordsettype_constructor_args():
    sig = inspect.signature(Docbook::KeywordsetType.__init__)
    params = list(sig.parameters.keys())
    assert "keyword" in params, "Missing parameter 'keyword'"

def test_docbook::keywordsettype_has_keyword():
    assert hasattr(Docbook::KeywordsetType, "keyword")
    descriptor = None
    for klass in Docbook::KeywordsetType.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)



def test_docbook::literaltype_is_not_abstract():
    assert not inspect.isabstract(Docbook::LiteralType)


def test_docbook::literaltype_constructor_exists():
    assert callable(Docbook::LiteralType.__init__)


def test_docbook::literaltype_constructor_args():
    sig = inspect.signature(Docbook::LiteralType.__init__)
    params = list(sig.parameters.keys())
    assert "moreinfo" in params, "Missing parameter 'moreinfo'"
    assert "value" in params, "Missing parameter 'value'"

def test_docbook::literaltype_has_moreinfo():
    assert hasattr(Docbook::LiteralType, "moreinfo")
    descriptor = None
    for klass in Docbook::LiteralType.__mro__:
        if "moreinfo" in klass.__dict__:
            descriptor = klass.__dict__["moreinfo"]
            break
    assert isinstance(descriptor, property)

def test_docbook::literaltype_has_value():
    assert hasattr(Docbook::LiteralType, "value")
    descriptor = None
    for klass in Docbook::LiteralType.__mro__:
        if "value" in klass.__dict__:
            descriptor = klass.__dict__["value"]
            break
    assert isinstance(descriptor, property)



def test_docbook::importanttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ImportantType)


def test_docbook::importanttype_constructor_exists():
    assert callable(Docbook::ImportantType.__init__)


def test_docbook::importanttype_constructor_args():
    sig = inspect.signature(Docbook::ImportantType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::importanttype_has_group():
    assert hasattr(Docbook::ImportantType, "group")
    descriptor = None
    for klass in Docbook::ImportantType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::importanttype_has_mixed():
    assert hasattr(Docbook::ImportantType, "mixed")
    descriptor = None
    for klass in Docbook::ImportantType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::imageobjecttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ImageobjectType)


def test_docbook::imageobjecttype_constructor_exists():
    assert callable(Docbook::ImageobjectType.__init__)


def test_docbook::imageobjecttype_constructor_args():
    sig = inspect.signature(Docbook::ImageobjectType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::imagedatatype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ImagedataType)


def test_docbook::imagedatatype_constructor_exists():
    assert callable(Docbook::ImagedataType.__init__)


def test_docbook::imagedatatype_constructor_args():
    sig = inspect.signature(Docbook::ImagedataType.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "align" in params, "Missing parameter 'align'"
    assert "fileref" in params, "Missing parameter 'fileref'"
    assert "depth" in params, "Missing parameter 'depth'"
    assert "scale" in params, "Missing parameter 'scale'"

def test_docbook::imagedatatype_has_width():
    assert hasattr(Docbook::ImagedataType, "width")
    descriptor = None
    for klass in Docbook::ImagedataType.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_docbook::imagedatatype_has_align():
    assert hasattr(Docbook::ImagedataType, "align")
    descriptor = None
    for klass in Docbook::ImagedataType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_docbook::imagedatatype_has_fileref():
    assert hasattr(Docbook::ImagedataType, "fileref")
    descriptor = None
    for klass in Docbook::ImagedataType.__mro__:
        if "fileref" in klass.__dict__:
            descriptor = klass.__dict__["fileref"]
            break
    assert isinstance(descriptor, property)

def test_docbook::imagedatatype_has_depth():
    assert hasattr(Docbook::ImagedataType, "depth")
    descriptor = None
    for klass in Docbook::ImagedataType.__mro__:
        if "depth" in klass.__dict__:
            descriptor = klass.__dict__["depth"]
            break
    assert isinstance(descriptor, property)

def test_docbook::imagedatatype_has_scale():
    assert hasattr(Docbook::ImagedataType, "scale")
    descriptor = None
    for klass in Docbook::ImagedataType.__mro__:
        if "scale" in klass.__dict__:
            descriptor = klass.__dict__["scale"]
            break
    assert isinstance(descriptor, property)



def test_docbook::footnotetype_is_not_abstract():
    assert not inspect.isabstract(Docbook::FootnoteType)


def test_docbook::footnotetype_constructor_exists():
    assert callable(Docbook::FootnoteType.__init__)


def test_docbook::footnotetype_constructor_args():
    sig = inspect.signature(Docbook::FootnoteType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_docbook::footnotetype_has_id():
    assert hasattr(Docbook::FootnoteType, "id")
    descriptor = None
    for klass in Docbook::FootnoteType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook::itemizedlisttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ItemizedlistType)


def test_docbook::itemizedlisttype_constructor_exists():
    assert callable(Docbook::ItemizedlistType.__init__)


def test_docbook::itemizedlisttype_constructor_args():
    sig = inspect.signature(Docbook::ItemizedlistType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::informaltabletype_is_not_abstract():
    assert not inspect.isabstract(Docbook::InformaltableType)


def test_docbook::informaltabletype_constructor_exists():
    assert callable(Docbook::InformaltableType.__init__)


def test_docbook::informaltabletype_constructor_args():
    sig = inspect.signature(Docbook::InformaltableType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::figuretype_is_not_abstract():
    assert not inspect.isabstract(Docbook::FigureType)


def test_docbook::figuretype_constructor_exists():
    assert callable(Docbook::FigureType.__init__)


def test_docbook::figuretype_constructor_args():
    sig = inspect.signature(Docbook::FigureType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "float" in params, "Missing parameter 'float'"

def test_docbook::figuretype_has_id():
    assert hasattr(Docbook::FigureType, "id")
    descriptor = None
    for klass in Docbook::FigureType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_docbook::figuretype_has_float():
    assert hasattr(Docbook::FigureType, "float")
    descriptor = None
    for klass in Docbook::FigureType.__mro__:
        if "float" in klass.__dict__:
            descriptor = klass.__dict__["float"]
            break
    assert isinstance(descriptor, property)



def test_docbook::entrytype_is_not_abstract():
    assert not inspect.isabstract(Docbook::EntryType)


def test_docbook::entrytype_constructor_exists():
    assert callable(Docbook::EntryType.__init__)


def test_docbook::entrytype_constructor_args():
    sig = inspect.signature(Docbook::EntryType.__init__)
    params = list(sig.parameters.keys())
    assert "align" in params, "Missing parameter 'align'"
    assert "valign" in params, "Missing parameter 'valign'"
    assert "nameend" in params, "Missing parameter 'nameend'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "namest" in params, "Missing parameter 'namest'"
    assert "morerows" in params, "Missing parameter 'morerows'"

def test_docbook::entrytype_has_align():
    assert hasattr(Docbook::EntryType, "align")
    descriptor = None
    for klass in Docbook::EntryType.__mro__:
        if "align" in klass.__dict__:
            descriptor = klass.__dict__["align"]
            break
    assert isinstance(descriptor, property)

def test_docbook::entrytype_has_valign():
    assert hasattr(Docbook::EntryType, "valign")
    descriptor = None
    for klass in Docbook::EntryType.__mro__:
        if "valign" in klass.__dict__:
            descriptor = klass.__dict__["valign"]
            break
    assert isinstance(descriptor, property)

def test_docbook::entrytype_has_nameend():
    assert hasattr(Docbook::EntryType, "nameend")
    descriptor = None
    for klass in Docbook::EntryType.__mro__:
        if "nameend" in klass.__dict__:
            descriptor = klass.__dict__["nameend"]
            break
    assert isinstance(descriptor, property)

def test_docbook::entrytype_has_mixed():
    assert hasattr(Docbook::EntryType, "mixed")
    descriptor = None
    for klass in Docbook::EntryType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::entrytype_has_namest():
    assert hasattr(Docbook::EntryType, "namest")
    descriptor = None
    for klass in Docbook::EntryType.__mro__:
        if "namest" in klass.__dict__:
            descriptor = klass.__dict__["namest"]
            break
    assert isinstance(descriptor, property)

def test_docbook::entrytype_has_morerows():
    assert hasattr(Docbook::EntryType, "morerows")
    descriptor = None
    for klass in Docbook::EntryType.__mro__:
        if "morerows" in klass.__dict__:
            descriptor = klass.__dict__["morerows"]
            break
    assert isinstance(descriptor, property)



def test_docbook::emphasistype_is_not_abstract():
    assert not inspect.isabstract(Docbook::EmphasisType)


def test_docbook::emphasistype_constructor_exists():
    assert callable(Docbook::EmphasisType.__init__)


def test_docbook::emphasistype_constructor_args():
    sig = inspect.signature(Docbook::EmphasisType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "role" in params, "Missing parameter 'role'"

def test_docbook::emphasistype_has_mixed():
    assert hasattr(Docbook::EmphasisType, "mixed")
    descriptor = None
    for klass in Docbook::EmphasisType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::emphasistype_has_role():
    assert hasattr(Docbook::EmphasisType, "role")
    descriptor = None
    for klass in Docbook::EmphasisType.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)



def test_docbook::datetype_is_not_abstract():
    assert not inspect.isabstract(Docbook::DateType)


def test_docbook::datetype_constructor_exists():
    assert callable(Docbook::DateType.__init__)


def test_docbook::datetype_constructor_args():
    sig = inspect.signature(Docbook::DateType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::datetype_has_mixed():
    assert hasattr(Docbook::DateType, "mixed")
    descriptor = None
    for klass in Docbook::DateType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::copyrighttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::CopyrightType)


def test_docbook::copyrighttype_constructor_exists():
    assert callable(Docbook::CopyrightType.__init__)


def test_docbook::copyrighttype_constructor_args():
    sig = inspect.signature(Docbook::CopyrightType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "year" in params, "Missing parameter 'year'"
    assert "holder" in params, "Missing parameter 'holder'"

def test_docbook::copyrighttype_has_group():
    assert hasattr(Docbook::CopyrightType, "group")
    descriptor = None
    for klass in Docbook::CopyrightType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::copyrighttype_has_year():
    assert hasattr(Docbook::CopyrightType, "year")
    descriptor = None
    for klass in Docbook::CopyrightType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_docbook::copyrighttype_has_holder():
    assert hasattr(Docbook::CopyrightType, "holder")
    descriptor = None
    for klass in Docbook::CopyrightType.__mro__:
        if "holder" in klass.__dict__:
            descriptor = klass.__dict__["holder"]
            break
    assert isinstance(descriptor, property)



def test_docbook::confgrouptype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ConfgroupType)


def test_docbook::confgrouptype_constructor_exists():
    assert callable(Docbook::ConfgroupType.__init__)


def test_docbook::confgrouptype_constructor_args():
    sig = inspect.signature(Docbook::ConfgroupType.__init__)
    params = list(sig.parameters.keys())
    assert "confnum" in params, "Missing parameter 'confnum'"
    assert "confsponsor" in params, "Missing parameter 'confsponsor'"
    assert "conftitle" in params, "Missing parameter 'conftitle'"

def test_docbook::confgrouptype_has_confnum():
    assert hasattr(Docbook::ConfgroupType, "confnum")
    descriptor = None
    for klass in Docbook::ConfgroupType.__mro__:
        if "confnum" in klass.__dict__:
            descriptor = klass.__dict__["confnum"]
            break
    assert isinstance(descriptor, property)

def test_docbook::confgrouptype_has_confsponsor():
    assert hasattr(Docbook::ConfgroupType, "confsponsor")
    descriptor = None
    for klass in Docbook::ConfgroupType.__mro__:
        if "confsponsor" in klass.__dict__:
            descriptor = klass.__dict__["confsponsor"]
            break
    assert isinstance(descriptor, property)

def test_docbook::confgrouptype_has_conftitle():
    assert hasattr(Docbook::ConfgroupType, "conftitle")
    descriptor = None
    for klass in Docbook::ConfgroupType.__mro__:
        if "conftitle" in klass.__dict__:
            descriptor = klass.__dict__["conftitle"]
            break
    assert isinstance(descriptor, property)



def test_docbook::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(Docbook::EStringToStringMapEntry)


def test_docbook::estringtostringmapentry_constructor_exists():
    assert callable(Docbook::EStringToStringMapEntry.__init__)


def test_docbook::estringtostringmapentry_constructor_args():
    sig = inspect.signature(Docbook::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_docbook::documentroot_is_not_abstract():
    assert not inspect.isabstract(Docbook::DocumentRoot)


def test_docbook::documentroot_constructor_exists():
    assert callable(Docbook::DocumentRoot.__init__)


def test_docbook::documentroot_constructor_args():
    sig = inspect.signature(Docbook::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "confsponsor" in params, "Missing parameter 'confsponsor'"
    assert "keyword" in params, "Missing parameter 'keyword'"
    assert "pubdate" in params, "Missing parameter 'pubdate'"
    assert "publishername" in params, "Missing parameter 'publishername'"
    assert "firstname" in params, "Missing parameter 'firstname'"
    assert "state" in params, "Missing parameter 'state'"
    assert "warning" in params, "Missing parameter 'warning'"
    assert "subtitle" in params, "Missing parameter 'subtitle'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "superscript" in params, "Missing parameter 'superscript'"
    assert "caution" in params, "Missing parameter 'caution'"
    assert "bibliomisc" in params, "Missing parameter 'bibliomisc'"
    assert "conftitle" in params, "Missing parameter 'conftitle'"
    assert "confnum" in params, "Missing parameter 'confnum'"
    assert "date" in params, "Missing parameter 'date'"

def test_docbook::documentroot_has_confsponsor():
    assert hasattr(Docbook::DocumentRoot, "confsponsor")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "confsponsor" in klass.__dict__:
            descriptor = klass.__dict__["confsponsor"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_keyword():
    assert hasattr(Docbook::DocumentRoot, "keyword")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "keyword" in klass.__dict__:
            descriptor = klass.__dict__["keyword"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_pubdate():
    assert hasattr(Docbook::DocumentRoot, "pubdate")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "pubdate" in klass.__dict__:
            descriptor = klass.__dict__["pubdate"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_publishername():
    assert hasattr(Docbook::DocumentRoot, "publishername")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "publishername" in klass.__dict__:
            descriptor = klass.__dict__["publishername"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_firstname():
    assert hasattr(Docbook::DocumentRoot, "firstname")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "firstname" in klass.__dict__:
            descriptor = klass.__dict__["firstname"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_state():
    assert hasattr(Docbook::DocumentRoot, "state")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_warning():
    assert hasattr(Docbook::DocumentRoot, "warning")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "warning" in klass.__dict__:
            descriptor = klass.__dict__["warning"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_subtitle():
    assert hasattr(Docbook::DocumentRoot, "subtitle")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "subtitle" in klass.__dict__:
            descriptor = klass.__dict__["subtitle"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_mixed():
    assert hasattr(Docbook::DocumentRoot, "mixed")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_superscript():
    assert hasattr(Docbook::DocumentRoot, "superscript")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "superscript" in klass.__dict__:
            descriptor = klass.__dict__["superscript"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_caution():
    assert hasattr(Docbook::DocumentRoot, "caution")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "caution" in klass.__dict__:
            descriptor = klass.__dict__["caution"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_bibliomisc():
    assert hasattr(Docbook::DocumentRoot, "bibliomisc")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "bibliomisc" in klass.__dict__:
            descriptor = klass.__dict__["bibliomisc"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_conftitle():
    assert hasattr(Docbook::DocumentRoot, "conftitle")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "conftitle" in klass.__dict__:
            descriptor = klass.__dict__["conftitle"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_confnum():
    assert hasattr(Docbook::DocumentRoot, "confnum")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "confnum" in klass.__dict__:
            descriptor = klass.__dict__["confnum"]
            break
    assert isinstance(descriptor, property)

def test_docbook::documentroot_has_date():
    assert hasattr(Docbook::DocumentRoot, "date")
    descriptor = None
    for klass in Docbook::DocumentRoot.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)



def test_docbook::commandtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::CommandType)


def test_docbook::commandtype_constructor_exists():
    assert callable(Docbook::CommandType.__init__)


def test_docbook::commandtype_constructor_args():
    sig = inspect.signature(Docbook::CommandType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::commandtype_has_mixed():
    assert hasattr(Docbook::CommandType, "mixed")
    descriptor = None
    for klass in Docbook::CommandType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::cmdsynopsistype_is_not_abstract():
    assert not inspect.isabstract(Docbook::CmdsynopsisType)


def test_docbook::cmdsynopsistype_constructor_exists():
    assert callable(Docbook::CmdsynopsisType.__init__)


def test_docbook::cmdsynopsistype_constructor_args():
    sig = inspect.signature(Docbook::CmdsynopsisType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::colspectype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ColspecType)


def test_docbook::colspectype_constructor_exists():
    assert callable(Docbook::ColspecType.__init__)


def test_docbook::colspectype_constructor_args():
    sig = inspect.signature(Docbook::ColspecType.__init__)
    params = list(sig.parameters.keys())
    assert "colname" in params, "Missing parameter 'colname'"
    assert "colwidth" in params, "Missing parameter 'colwidth'"

def test_docbook::colspectype_has_colname():
    assert hasattr(Docbook::ColspecType, "colname")
    descriptor = None
    for klass in Docbook::ColspecType.__mro__:
        if "colname" in klass.__dict__:
            descriptor = klass.__dict__["colname"]
            break
    assert isinstance(descriptor, property)

def test_docbook::colspectype_has_colwidth():
    assert hasattr(Docbook::ColspecType, "colwidth")
    descriptor = None
    for klass in Docbook::ColspecType.__mro__:
        if "colwidth" in klass.__dict__:
            descriptor = klass.__dict__["colwidth"]
            break
    assert isinstance(descriptor, property)



def test_docbook::sectiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook::SectionType)


def test_docbook::sectiontype_constructor_exists():
    assert callable(Docbook::SectionType.__init__)


def test_docbook::sectiontype_constructor_args():
    sig = inspect.signature(Docbook::SectionType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "annotations" in params, "Missing parameter 'annotations'"
    assert "warning" in params, "Missing parameter 'warning'"
    assert "caution" in params, "Missing parameter 'caution'"

def test_docbook::sectiontype_has_group():
    assert hasattr(Docbook::SectionType, "group")
    descriptor = None
    for klass in Docbook::SectionType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::sectiontype_has_annotations():
    assert hasattr(Docbook::SectionType, "annotations")
    descriptor = None
    for klass in Docbook::SectionType.__mro__:
        if "annotations" in klass.__dict__:
            descriptor = klass.__dict__["annotations"]
            break
    assert isinstance(descriptor, property)

def test_docbook::sectiontype_has_warning():
    assert hasattr(Docbook::SectionType, "warning")
    descriptor = None
    for klass in Docbook::SectionType.__mro__:
        if "warning" in klass.__dict__:
            descriptor = klass.__dict__["warning"]
            break
    assert isinstance(descriptor, property)

def test_docbook::sectiontype_has_caution():
    assert hasattr(Docbook::SectionType, "caution")
    descriptor = None
    for klass in Docbook::SectionType.__mro__:
        if "caution" in klass.__dict__:
            descriptor = klass.__dict__["caution"]
            break
    assert isinstance(descriptor, property)



def test_docbook::notetype_is_not_abstract():
    assert not inspect.isabstract(Docbook::NoteType)


def test_docbook::notetype_constructor_exists():
    assert callable(Docbook::NoteType.__init__)


def test_docbook::notetype_constructor_args():
    sig = inspect.signature(Docbook::NoteType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::notetype_has_group():
    assert hasattr(Docbook::NoteType, "group")
    descriptor = None
    for klass in Docbook::NoteType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::notetype_has_mixed():
    assert hasattr(Docbook::NoteType, "mixed")
    descriptor = None
    for klass in Docbook::NoteType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::referencetype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ReferenceType)


def test_docbook::referencetype_constructor_exists():
    assert callable(Docbook::ReferenceType.__init__)


def test_docbook::referencetype_constructor_args():
    sig = inspect.signature(Docbook::ReferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "version" in params, "Missing parameter 'version'"

def test_docbook::referencetype_has_version():
    assert hasattr(Docbook::ReferenceType, "version")
    descriptor = None
    for klass in Docbook::ReferenceType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)



def test_docbook::chaptertype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ChapterType)


def test_docbook::chaptertype_constructor_exists():
    assert callable(Docbook::ChapterType.__init__)


def test_docbook::chaptertype_constructor_args():
    sig = inspect.signature(Docbook::ChapterType.__init__)
    params = list(sig.parameters.keys())
    assert "annotations" in params, "Missing parameter 'annotations'"

def test_docbook::chaptertype_has_annotations():
    assert hasattr(Docbook::ChapterType, "annotations")
    descriptor = None
    for klass in Docbook::ChapterType.__mro__:
        if "annotations" in klass.__dict__:
            descriptor = klass.__dict__["annotations"]
            break
    assert isinstance(descriptor, property)



def test_docbook::argtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ArgType)


def test_docbook::argtype_constructor_exists():
    assert callable(Docbook::ArgType.__init__)


def test_docbook::argtype_constructor_args():
    sig = inspect.signature(Docbook::ArgType.__init__)
    params = list(sig.parameters.keys())
    assert "rep" in params, "Missing parameter 'rep'"
    assert "choice" in params, "Missing parameter 'choice'"
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::argtype_has_rep():
    assert hasattr(Docbook::ArgType, "rep")
    descriptor = None
    for klass in Docbook::ArgType.__mro__:
        if "rep" in klass.__dict__:
            descriptor = klass.__dict__["rep"]
            break
    assert isinstance(descriptor, property)

def test_docbook::argtype_has_choice():
    assert hasattr(Docbook::ArgType, "choice")
    descriptor = None
    for klass in Docbook::ArgType.__mro__:
        if "choice" in klass.__dict__:
            descriptor = klass.__dict__["choice"]
            break
    assert isinstance(descriptor, property)

def test_docbook::argtype_has_mixed():
    assert hasattr(Docbook::ArgType, "mixed")
    descriptor = None
    for klass in Docbook::ArgType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::addresstype_is_not_abstract():
    assert not inspect.isabstract(Docbook::AddressType)


def test_docbook::addresstype_constructor_exists():
    assert callable(Docbook::AddressType.__init__)


def test_docbook::addresstype_constructor_args():
    sig = inspect.signature(Docbook::AddressType.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"
    assert "state" in params, "Missing parameter 'state'"
    assert "format" in params, "Missing parameter 'format'"

def test_docbook::addresstype_has_email():
    assert hasattr(Docbook::AddressType, "email")
    descriptor = None
    for klass in Docbook::AddressType.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_docbook::addresstype_has_state():
    assert hasattr(Docbook::AddressType, "state")
    descriptor = None
    for klass in Docbook::AddressType.__mro__:
        if "state" in klass.__dict__:
            descriptor = klass.__dict__["state"]
            break
    assert isinstance(descriptor, property)

def test_docbook::addresstype_has_format():
    assert hasattr(Docbook::AddressType, "format")
    descriptor = None
    for klass in Docbook::AddressType.__mro__:
        if "format" in klass.__dict__:
            descriptor = klass.__dict__["format"]
            break
    assert isinstance(descriptor, property)



def test_docbook::paratype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ParaType)


def test_docbook::paratype_constructor_exists():
    assert callable(Docbook::ParaType.__init__)


def test_docbook::paratype_constructor_args():
    sig = inspect.signature(Docbook::ParaType.__init__)
    params = list(sig.parameters.keys())
    assert "group" in params, "Missing parameter 'group'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "role" in params, "Missing parameter 'role'"
    assert "id" in params, "Missing parameter 'id'"

def test_docbook::paratype_has_group():
    assert hasattr(Docbook::ParaType, "group")
    descriptor = None
    for klass in Docbook::ParaType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::paratype_has_mixed():
    assert hasattr(Docbook::ParaType, "mixed")
    descriptor = None
    for klass in Docbook::ParaType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::paratype_has_role():
    assert hasattr(Docbook::ParaType, "role")
    descriptor = None
    for klass in Docbook::ParaType.__mro__:
        if "role" in klass.__dict__:
            descriptor = klass.__dict__["role"]
            break
    assert isinstance(descriptor, property)

def test_docbook::paratype_has_id():
    assert hasattr(Docbook::ParaType, "id")
    descriptor = None
    for klass in Docbook::ParaType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_docbook::abstracttype_is_not_abstract():
    assert not inspect.isabstract(Docbook::AbstractType)


def test_docbook::abstracttype_constructor_exists():
    assert callable(Docbook::AbstractType.__init__)


def test_docbook::abstracttype_constructor_args():
    sig = inspect.signature(Docbook::AbstractType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::prefacetype_is_not_abstract():
    assert not inspect.isabstract(Docbook::PrefaceType)


def test_docbook::prefacetype_constructor_exists():
    assert callable(Docbook::PrefaceType.__init__)


def test_docbook::prefacetype_constructor_args():
    sig = inspect.signature(Docbook::PrefaceType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::infotype_is_not_abstract():
    assert not inspect.isabstract(Docbook::InfoType)


def test_docbook::infotype_constructor_exists():
    assert callable(Docbook::InfoType.__init__)


def test_docbook::infotype_constructor_args():
    sig = inspect.signature(Docbook::InfoType.__init__)
    params = list(sig.parameters.keys())
    assert "productname" in params, "Missing parameter 'productname'"
    assert "bibliomisc" in params, "Missing parameter 'bibliomisc'"
    assert "group" in params, "Missing parameter 'group'"
    assert "date" in params, "Missing parameter 'date'"
    assert "releaseinfo" in params, "Missing parameter 'releaseinfo'"
    assert "pubdate" in params, "Missing parameter 'pubdate'"

def test_docbook::infotype_has_productname():
    assert hasattr(Docbook::InfoType, "productname")
    descriptor = None
    for klass in Docbook::InfoType.__mro__:
        if "productname" in klass.__dict__:
            descriptor = klass.__dict__["productname"]
            break
    assert isinstance(descriptor, property)

def test_docbook::infotype_has_bibliomisc():
    assert hasattr(Docbook::InfoType, "bibliomisc")
    descriptor = None
    for klass in Docbook::InfoType.__mro__:
        if "bibliomisc" in klass.__dict__:
            descriptor = klass.__dict__["bibliomisc"]
            break
    assert isinstance(descriptor, property)

def test_docbook::infotype_has_group():
    assert hasattr(Docbook::InfoType, "group")
    descriptor = None
    for klass in Docbook::InfoType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)

def test_docbook::infotype_has_date():
    assert hasattr(Docbook::InfoType, "date")
    descriptor = None
    for klass in Docbook::InfoType.__mro__:
        if "date" in klass.__dict__:
            descriptor = klass.__dict__["date"]
            break
    assert isinstance(descriptor, property)

def test_docbook::infotype_has_releaseinfo():
    assert hasattr(Docbook::InfoType, "releaseinfo")
    descriptor = None
    for klass in Docbook::InfoType.__mro__:
        if "releaseinfo" in klass.__dict__:
            descriptor = klass.__dict__["releaseinfo"]
            break
    assert isinstance(descriptor, property)

def test_docbook::infotype_has_pubdate():
    assert hasattr(Docbook::InfoType, "pubdate")
    descriptor = None
    for klass in Docbook::InfoType.__mro__:
        if "pubdate" in klass.__dict__:
            descriptor = klass.__dict__["pubdate"]
            break
    assert isinstance(descriptor, property)



def test_docbook::booktype_is_not_abstract():
    assert not inspect.isabstract(Docbook::BookType)


def test_docbook::booktype_constructor_exists():
    assert callable(Docbook::BookType.__init__)


def test_docbook::booktype_constructor_args():
    sig = inspect.signature(Docbook::BookType.__init__)
    params = list(sig.parameters.keys())
    assert "label" in params, "Missing parameter 'label'"
    assert "version" in params, "Missing parameter 'version'"
    assert "lang" in params, "Missing parameter 'lang'"

def test_docbook::booktype_has_label():
    assert hasattr(Docbook::BookType, "label")
    descriptor = None
    for klass in Docbook::BookType.__mro__:
        if "label" in klass.__dict__:
            descriptor = klass.__dict__["label"]
            break
    assert isinstance(descriptor, property)

def test_docbook::booktype_has_version():
    assert hasattr(Docbook::BookType, "version")
    descriptor = None
    for klass in Docbook::BookType.__mro__:
        if "version" in klass.__dict__:
            descriptor = klass.__dict__["version"]
            break
    assert isinstance(descriptor, property)

def test_docbook::booktype_has_lang():
    assert hasattr(Docbook::BookType, "lang")
    descriptor = None
    for klass in Docbook::BookType.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)



def test_docbook::titletype_is_not_abstract():
    assert not inspect.isabstract(Docbook::TitleType)


def test_docbook::titletype_constructor_exists():
    assert callable(Docbook::TitleType.__init__)


def test_docbook::titletype_constructor_args():
    sig = inspect.signature(Docbook::TitleType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "group" in params, "Missing parameter 'group'"

def test_docbook::titletype_has_mixed():
    assert hasattr(Docbook::TitleType, "mixed")
    descriptor = None
    for klass in Docbook::TitleType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_docbook::titletype_has_group():
    assert hasattr(Docbook::TitleType, "group")
    descriptor = None
    for klass in Docbook::TitleType.__mro__:
        if "group" in klass.__dict__:
            descriptor = klass.__dict__["group"]
            break
    assert isinstance(descriptor, property)



def test_docbook::otheraddrtype_is_not_abstract():
    assert not inspect.isabstract(Docbook::OtheraddrType)


def test_docbook::otheraddrtype_constructor_exists():
    assert callable(Docbook::OtheraddrType.__init__)


def test_docbook::otheraddrtype_constructor_args():
    sig = inspect.signature(Docbook::OtheraddrType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::personnametype_is_not_abstract():
    assert not inspect.isabstract(Docbook::PersonnameType)


def test_docbook::personnametype_constructor_exists():
    assert callable(Docbook::PersonnameType.__init__)


def test_docbook::personnametype_constructor_args():
    sig = inspect.signature(Docbook::PersonnameType.__init__)
    params = list(sig.parameters.keys())



def test_docbook::authortype_is_not_abstract():
    assert not inspect.isabstract(Docbook::AuthorType)


def test_docbook::authortype_constructor_exists():
    assert callable(Docbook::AuthorType.__init__)


def test_docbook::authortype_constructor_args():
    sig = inspect.signature(Docbook::AuthorType.__init__)
    params = list(sig.parameters.keys())
    assert "contrib" in params, "Missing parameter 'contrib'"

def test_docbook::authortype_has_contrib():
    assert hasattr(Docbook::AuthorType, "contrib")
    descriptor = None
    for klass in Docbook::AuthorType.__mro__:
        if "contrib" in klass.__dict__:
            descriptor = klass.__dict__["contrib"]
            break
    assert isinstance(descriptor, property)



def test_docbook::authorinitialstype_is_not_abstract():
    assert not inspect.isabstract(Docbook::AuthorinitialsType)


def test_docbook::authorinitialstype_constructor_exists():
    assert callable(Docbook::AuthorinitialsType.__init__)


def test_docbook::authorinitialstype_constructor_args():
    sig = inspect.signature(Docbook::AuthorinitialsType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::authorinitialstype_has_mixed():
    assert hasattr(Docbook::AuthorinitialsType, "mixed")
    descriptor = None
    for klass in Docbook::AuthorinitialsType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::replaceabletype_is_not_abstract():
    assert not inspect.isabstract(Docbook::ReplaceableType)


def test_docbook::replaceabletype_constructor_exists():
    assert callable(Docbook::ReplaceableType.__init__)


def test_docbook::replaceabletype_constructor_args():
    sig = inspect.signature(Docbook::ReplaceableType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::replaceabletype_has_mixed():
    assert hasattr(Docbook::ReplaceableType, "mixed")
    descriptor = None
    for klass in Docbook::ReplaceableType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)



def test_docbook::optiontype_is_not_abstract():
    assert not inspect.isabstract(Docbook::OptionType)


def test_docbook::optiontype_constructor_exists():
    assert callable(Docbook::OptionType.__init__)


def test_docbook::optiontype_constructor_args():
    sig = inspect.signature(Docbook::OptionType.__init__)
    params = list(sig.parameters.keys())
    assert "mixed" in params, "Missing parameter 'mixed'"

def test_docbook::optiontype_has_mixed():
    assert hasattr(Docbook::OptionType, "mixed")
    descriptor = None
    for klass in Docbook::OptionType.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)


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
Docbook::VarListEntryType_strategy = st.builds(
    Docbook::VarListEntryType,
    spacing=
        safe_text,
    termlength=
        safe_text
)
Docbook::TermType_strategy = st.builds(
    Docbook::TermType,
    mixed=
        safe_text
)
Docbook::SegType_strategy = st.builds(
    Docbook::SegType,
    errortext=
        safe_text,
    group=
        safe_text,
    mixed=
        safe_text,
    errorcode=
        safe_text
)
Docbook::SegListItemType_strategy = st.builds(
    Docbook::SegListItemType,
)
Docbook::RevdescriptionType_strategy = st.builds(
    Docbook::RevdescriptionType,
    mixed=
        safe_text
)
Docbook::RevnumberType_strategy = st.builds(
    Docbook::RevnumberType,
    mixed=
        safe_text
)
Docbook::RevisionType_strategy = st.builds(
    Docbook::RevisionType,
)
Docbook::SegmentedListType_strategy = st.builds(
    Docbook::SegmentedListType,
    segtitle=
        safe_text,
    group=
        safe_text
)
Docbook::RefEntryTitleType_strategy = st.builds(
    Docbook::RefEntryTitleType,
    mixed=
        safe_text
)
Docbook::RefSect1Type_strategy = st.builds(
    Docbook::RefSect1Type,
    id=
        safe_text,
    group=
        safe_text
)
Docbook::RefSynopsisDivType_strategy = st.builds(
    Docbook::RefSynopsisDivType,
)
Docbook::RefNameDivType_strategy = st.builds(
    Docbook::RefNameDivType,
    refname=
        safe_text,
    refpurpose=
        safe_text,
    refclass=
        safe_text
)
Docbook::RefMetaType_strategy = st.builds(
    Docbook::RefMetaType,
    manvolnum=
        safe_text
)
Docbook::RefEntryType_strategy = st.builds(
    Docbook::RefEntryType,
    version=
        safe_text
)
Docbook::SurnameType_strategy = st.builds(
    Docbook::SurnameType,
    mixed=
        safe_text
)
Docbook::VariableListType_strategy = st.builds(
    Docbook::VariableListType,
)
ItemizedlistType_strategy = st.builds(
    ItemizedlistType,
)
Docbook::ParameterType_strategy = st.builds(
    Docbook::ParameterType,
    mixed=
        safe_text
)
Docbook::RevhistoryType_strategy = st.builds(
    Docbook::RevhistoryType,
)
Docbook::LegalNoticeType_strategy = st.builds(
    Docbook::LegalNoticeType,
    group=
        safe_text
)
Docbook::SubtitleType_strategy = st.builds(
    Docbook::SubtitleType,
    group=
        safe_text,
    mixed=
        safe_text
)
Docbook::ParamdefType_strategy = st.builds(
    Docbook::ParamdefType,
    mixed=
        safe_text
)
Docbook::FuncprototypeType_strategy = st.builds(
    Docbook::FuncprototypeType,
)
Docbook::FuncsynopsisType_strategy = st.builds(
    Docbook::FuncsynopsisType,
)
Docbook::FileNameType_strategy = st.builds(
    Docbook::FileNameType,
    mixed=
        safe_text
)
Docbook::FunctionType_strategy = st.builds(
    Docbook::FunctionType,
    mixed=
        safe_text
)
Docbook::FuncdefType_strategy = st.builds(
    Docbook::FuncdefType,
    mixed=
        safe_text
)
Docbook::FirstnameType_strategy = st.builds(
    Docbook::FirstnameType,
    mixed=
        safe_text
)
Docbook::EnvarType_strategy = st.builds(
    Docbook::EnvarType,
    mixed=
        safe_text
)
Docbook::ExampleType_strategy = st.builds(
    Docbook::ExampleType,
    id=
        safe_text
)
Docbook::TheadType_strategy = st.builds(
    Docbook::TheadType,
)
Docbook::TgroupType_strategy = st.builds(
    Docbook::TgroupType,
    colseq=
        safe_text,
    cols=
        safe_text,
    rowseq=
        safe_text,
    align=
        safe_text
)
Docbook::UlinkType_strategy = st.builds(
    Docbook::UlinkType,
    mixed=
        safe_text,
    type=
        safe_text,
    url=
        safe_text
)
Docbook::TipType_strategy = st.builds(
    Docbook::TipType,
    mixed=
        safe_text
)
Docbook::TbodyType_strategy = st.builds(
    Docbook::TbodyType,
)
Docbook::TableType_strategy = st.builds(
    Docbook::TableType,
    id=
        safe_text
)
Docbook::ProgramlistingType_strategy = st.builds(
    Docbook::ProgramlistingType,
    mixed=
        safe_text,
    group=
        safe_text,
    language=
        safe_text,
    superscript=
        safe_text,
    linenumbering=
        safe_text,
    format=
        safe_text
)
Docbook::RowType_strategy = st.builds(
    Docbook::RowType,
)
Docbook::PhraseType_strategy = st.builds(
    Docbook::PhraseType,
    id=
        safe_text
)
Docbook::PublisherType_strategy = st.builds(
    Docbook::PublisherType,
    publishername=
        safe_text
)
Docbook::OrderedlistType_strategy = st.builds(
    Docbook::OrderedlistType,
    inheritnum=
        safe_text,
    continuation=
        safe_text
)
Docbook::MediaobjectType_strategy = st.builds(
    Docbook::MediaobjectType,
)
Docbook::ListitemType_strategy = st.builds(
    Docbook::ListitemType,
)
Docbook::LinkType_strategy = st.builds(
    Docbook::LinkType,
    linkend=
        safe_text,
    mixed=
        safe_text,
    value=
        safe_text
)
Docbook::KeywordsetType_strategy = st.builds(
    Docbook::KeywordsetType,
    keyword=
        safe_text
)
Docbook::LiteralType_strategy = st.builds(
    Docbook::LiteralType,
    moreinfo=
        safe_text,
    value=
        safe_text
)
Docbook::ImportantType_strategy = st.builds(
    Docbook::ImportantType,
    group=
        safe_text,
    mixed=
        safe_text
)
Docbook::ImageobjectType_strategy = st.builds(
    Docbook::ImageobjectType,
)
Docbook::ImagedataType_strategy = st.builds(
    Docbook::ImagedataType,
    width=
        safe_text,
    align=
        safe_text,
    fileref=
        safe_text,
    depth=
        safe_text,
    scale=
        safe_text
)
Docbook::FootnoteType_strategy = st.builds(
    Docbook::FootnoteType,
    id=
        safe_text
)
Docbook::ItemizedlistType_strategy = st.builds(
    Docbook::ItemizedlistType,
)
Docbook::InformaltableType_strategy = st.builds(
    Docbook::InformaltableType,
)
Docbook::FigureType_strategy = st.builds(
    Docbook::FigureType,
    id=
        safe_text,
    float=
        safe_text
)
Docbook::EntryType_strategy = st.builds(
    Docbook::EntryType,
    align=
        safe_text,
    valign=
        safe_text,
    nameend=
        safe_text,
    mixed=
        safe_text,
    namest=
        safe_text,
    morerows=
        safe_text
)
Docbook::EmphasisType_strategy = st.builds(
    Docbook::EmphasisType,
    mixed=
        safe_text,
    role=
        safe_text
)
Docbook::DateType_strategy = st.builds(
    Docbook::DateType,
    mixed=
        safe_text
)
Docbook::CopyrightType_strategy = st.builds(
    Docbook::CopyrightType,
    group=
        safe_text,
    year=
        safe_text,
    holder=
        safe_text
)
Docbook::ConfgroupType_strategy = st.builds(
    Docbook::ConfgroupType,
    confnum=
        safe_text,
    confsponsor=
        safe_text,
    conftitle=
        safe_text
)
Docbook::EStringToStringMapEntry_strategy = st.builds(
    Docbook::EStringToStringMapEntry,
)
Docbook::DocumentRoot_strategy = st.builds(
    Docbook::DocumentRoot,
    confsponsor=
        safe_text,
    keyword=
        safe_text,
    pubdate=
        safe_text,
    publishername=
        safe_text,
    firstname=
        safe_text,
    state=
        safe_text,
    warning=
        safe_text,
    subtitle=
        safe_text,
    mixed=
        safe_text,
    superscript=
        safe_text,
    caution=
        safe_text,
    bibliomisc=
        safe_text,
    conftitle=
        safe_text,
    confnum=
        safe_text,
    date=
        safe_text
)
Docbook::CommandType_strategy = st.builds(
    Docbook::CommandType,
    mixed=
        safe_text
)
Docbook::CmdsynopsisType_strategy = st.builds(
    Docbook::CmdsynopsisType,
)
Docbook::ColspecType_strategy = st.builds(
    Docbook::ColspecType,
    colname=
        safe_text,
    colwidth=
        safe_text
)
Docbook::SectionType_strategy = st.builds(
    Docbook::SectionType,
    group=
        safe_text,
    annotations=
        safe_text,
    warning=
        safe_text,
    caution=
        safe_text
)
Docbook::NoteType_strategy = st.builds(
    Docbook::NoteType,
    group=
        safe_text,
    mixed=
        safe_text
)
Docbook::ReferenceType_strategy = st.builds(
    Docbook::ReferenceType,
    version=
        safe_text
)
Docbook::ChapterType_strategy = st.builds(
    Docbook::ChapterType,
    annotations=
        safe_text
)
Docbook::ArgType_strategy = st.builds(
    Docbook::ArgType,
    rep=
        safe_text,
    choice=
        safe_text,
    mixed=
        safe_text
)
Docbook::AddressType_strategy = st.builds(
    Docbook::AddressType,
    email=
        safe_text,
    state=
        safe_text,
    format=
        safe_text
)
Docbook::ParaType_strategy = st.builds(
    Docbook::ParaType,
    group=
        safe_text,
    mixed=
        safe_text,
    role=
        safe_text,
    id=
        safe_text
)
Docbook::AbstractType_strategy = st.builds(
    Docbook::AbstractType,
)
Docbook::PrefaceType_strategy = st.builds(
    Docbook::PrefaceType,
)
Docbook::InfoType_strategy = st.builds(
    Docbook::InfoType,
    productname=
        safe_text,
    bibliomisc=
        safe_text,
    group=
        safe_text,
    date=
        safe_text,
    releaseinfo=
        safe_text,
    pubdate=
        safe_text
)
Docbook::BookType_strategy = st.builds(
    Docbook::BookType,
    label=
        safe_text,
    version=
        safe_text,
    lang=
        safe_text
)
Docbook::TitleType_strategy = st.builds(
    Docbook::TitleType,
    mixed=
        safe_text,
    group=
        safe_text
)
Docbook::OtheraddrType_strategy = st.builds(
    Docbook::OtheraddrType,
)
Docbook::PersonnameType_strategy = st.builds(
    Docbook::PersonnameType,
)
Docbook::AuthorType_strategy = st.builds(
    Docbook::AuthorType,
    contrib=
        safe_text
)
Docbook::AuthorinitialsType_strategy = st.builds(
    Docbook::AuthorinitialsType,
    mixed=
        safe_text
)
Docbook::ReplaceableType_strategy = st.builds(
    Docbook::ReplaceableType,
    mixed=
        safe_text
)
Docbook::OptionType_strategy = st.builds(
    Docbook::OptionType,
    mixed=
        safe_text
)

@given(instance=Docbook::VarListEntryType_strategy)
@settings(max_examples=50)
def test_docbook::varlistentrytype_instantiation(instance):
    assert isinstance(instance, Docbook::VarListEntryType)

@given(instance=Docbook::VarListEntryType_strategy)
def test_docbook::varlistentrytype_spacing_type(instance):
    assert isinstance(instance.spacing, str)


@given(instance=Docbook::VarListEntryType_strategy)
def test_docbook::varlistentrytype_spacing_setter(instance):
    original = instance.spacing
    instance.spacing = original
    assert instance.spacing == original

@given(instance=Docbook::VarListEntryType_strategy)
def test_docbook::varlistentrytype_termlength_type(instance):
    assert isinstance(instance.termlength, str)


@given(instance=Docbook::VarListEntryType_strategy)
def test_docbook::varlistentrytype_termlength_setter(instance):
    original = instance.termlength
    instance.termlength = original
    assert instance.termlength == original

@given(instance=Docbook::TermType_strategy)
@settings(max_examples=50)
def test_docbook::termtype_instantiation(instance):
    assert isinstance(instance, Docbook::TermType)

@given(instance=Docbook::TermType_strategy)
def test_docbook::termtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::TermType_strategy)
def test_docbook::termtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::SegType_strategy)
@settings(max_examples=50)
def test_docbook::segtype_instantiation(instance):
    assert isinstance(instance, Docbook::SegType)

@given(instance=Docbook::SegType_strategy)
def test_docbook::segtype_errortext_type(instance):
    assert isinstance(instance.errortext, str)


@given(instance=Docbook::SegType_strategy)
def test_docbook::segtype_errortext_setter(instance):
    original = instance.errortext
    instance.errortext = original
    assert instance.errortext == original

@given(instance=Docbook::SegType_strategy)
def test_docbook::segtype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::SegType_strategy)
def test_docbook::segtype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::SegType_strategy)
def test_docbook::segtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::SegType_strategy)
def test_docbook::segtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::SegType_strategy)
def test_docbook::segtype_errorcode_type(instance):
    assert isinstance(instance.errorcode, str)


@given(instance=Docbook::SegType_strategy)
def test_docbook::segtype_errorcode_setter(instance):
    original = instance.errorcode
    instance.errorcode = original
    assert instance.errorcode == original

@given(instance=Docbook::SegListItemType_strategy)
@settings(max_examples=50)
def test_docbook::seglistitemtype_instantiation(instance):
    assert isinstance(instance, Docbook::SegListItemType)

@given(instance=Docbook::RevdescriptionType_strategy)
@settings(max_examples=50)
def test_docbook::revdescriptiontype_instantiation(instance):
    assert isinstance(instance, Docbook::RevdescriptionType)

@given(instance=Docbook::RevdescriptionType_strategy)
def test_docbook::revdescriptiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::RevdescriptionType_strategy)
def test_docbook::revdescriptiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::RevnumberType_strategy)
@settings(max_examples=50)
def test_docbook::revnumbertype_instantiation(instance):
    assert isinstance(instance, Docbook::RevnumberType)

@given(instance=Docbook::RevnumberType_strategy)
def test_docbook::revnumbertype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::RevnumberType_strategy)
def test_docbook::revnumbertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::RevisionType_strategy)
@settings(max_examples=50)
def test_docbook::revisiontype_instantiation(instance):
    assert isinstance(instance, Docbook::RevisionType)

@given(instance=Docbook::SegmentedListType_strategy)
@settings(max_examples=50)
def test_docbook::segmentedlisttype_instantiation(instance):
    assert isinstance(instance, Docbook::SegmentedListType)

@given(instance=Docbook::SegmentedListType_strategy)
def test_docbook::segmentedlisttype_segtitle_type(instance):
    assert isinstance(instance.segtitle, str)


@given(instance=Docbook::SegmentedListType_strategy)
def test_docbook::segmentedlisttype_segtitle_setter(instance):
    original = instance.segtitle
    instance.segtitle = original
    assert instance.segtitle == original

@given(instance=Docbook::SegmentedListType_strategy)
def test_docbook::segmentedlisttype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::SegmentedListType_strategy)
def test_docbook::segmentedlisttype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::RefEntryTitleType_strategy)
@settings(max_examples=50)
def test_docbook::refentrytitletype_instantiation(instance):
    assert isinstance(instance, Docbook::RefEntryTitleType)

@given(instance=Docbook::RefEntryTitleType_strategy)
def test_docbook::refentrytitletype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::RefEntryTitleType_strategy)
def test_docbook::refentrytitletype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::RefSect1Type_strategy)
@settings(max_examples=50)
def test_docbook::refsect1type_instantiation(instance):
    assert isinstance(instance, Docbook::RefSect1Type)

@given(instance=Docbook::RefSect1Type_strategy)
def test_docbook::refsect1type_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Docbook::RefSect1Type_strategy)
def test_docbook::refsect1type_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook::RefSect1Type_strategy)
def test_docbook::refsect1type_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::RefSect1Type_strategy)
def test_docbook::refsect1type_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::RefSynopsisDivType_strategy)
@settings(max_examples=50)
def test_docbook::refsynopsisdivtype_instantiation(instance):
    assert isinstance(instance, Docbook::RefSynopsisDivType)

@given(instance=Docbook::RefNameDivType_strategy)
@settings(max_examples=50)
def test_docbook::refnamedivtype_instantiation(instance):
    assert isinstance(instance, Docbook::RefNameDivType)

@given(instance=Docbook::RefNameDivType_strategy)
def test_docbook::refnamedivtype_refname_type(instance):
    assert isinstance(instance.refname, str)


@given(instance=Docbook::RefNameDivType_strategy)
def test_docbook::refnamedivtype_refname_setter(instance):
    original = instance.refname
    instance.refname = original
    assert instance.refname == original

@given(instance=Docbook::RefNameDivType_strategy)
def test_docbook::refnamedivtype_refpurpose_type(instance):
    assert isinstance(instance.refpurpose, str)


@given(instance=Docbook::RefNameDivType_strategy)
def test_docbook::refnamedivtype_refpurpose_setter(instance):
    original = instance.refpurpose
    instance.refpurpose = original
    assert instance.refpurpose == original

@given(instance=Docbook::RefNameDivType_strategy)
def test_docbook::refnamedivtype_refclass_type(instance):
    assert isinstance(instance.refclass, str)


@given(instance=Docbook::RefNameDivType_strategy)
def test_docbook::refnamedivtype_refclass_setter(instance):
    original = instance.refclass
    instance.refclass = original
    assert instance.refclass == original

@given(instance=Docbook::RefMetaType_strategy)
@settings(max_examples=50)
def test_docbook::refmetatype_instantiation(instance):
    assert isinstance(instance, Docbook::RefMetaType)

@given(instance=Docbook::RefMetaType_strategy)
def test_docbook::refmetatype_manvolnum_type(instance):
    assert isinstance(instance.manvolnum, str)


@given(instance=Docbook::RefMetaType_strategy)
def test_docbook::refmetatype_manvolnum_setter(instance):
    original = instance.manvolnum
    instance.manvolnum = original
    assert instance.manvolnum == original

@given(instance=Docbook::RefEntryType_strategy)
@settings(max_examples=50)
def test_docbook::refentrytype_instantiation(instance):
    assert isinstance(instance, Docbook::RefEntryType)

@given(instance=Docbook::RefEntryType_strategy)
def test_docbook::refentrytype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=Docbook::RefEntryType_strategy)
def test_docbook::refentrytype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Docbook::SurnameType_strategy)
@settings(max_examples=50)
def test_docbook::surnametype_instantiation(instance):
    assert isinstance(instance, Docbook::SurnameType)

@given(instance=Docbook::SurnameType_strategy)
def test_docbook::surnametype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::SurnameType_strategy)
def test_docbook::surnametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::VariableListType_strategy)
@settings(max_examples=50)
def test_docbook::variablelisttype_instantiation(instance):
    assert isinstance(instance, Docbook::VariableListType)

@given(instance=ItemizedlistType_strategy)
@settings(max_examples=50)
def test_itemizedlisttype_instantiation(instance):
    assert isinstance(instance, ItemizedlistType)

@given(instance=Docbook::ParameterType_strategy)
@settings(max_examples=50)
def test_docbook::parametertype_instantiation(instance):
    assert isinstance(instance, Docbook::ParameterType)

@given(instance=Docbook::ParameterType_strategy)
def test_docbook::parametertype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::ParameterType_strategy)
def test_docbook::parametertype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::RevhistoryType_strategy)
@settings(max_examples=50)
def test_docbook::revhistorytype_instantiation(instance):
    assert isinstance(instance, Docbook::RevhistoryType)

@given(instance=Docbook::LegalNoticeType_strategy)
@settings(max_examples=50)
def test_docbook::legalnoticetype_instantiation(instance):
    assert isinstance(instance, Docbook::LegalNoticeType)

@given(instance=Docbook::LegalNoticeType_strategy)
def test_docbook::legalnoticetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::LegalNoticeType_strategy)
def test_docbook::legalnoticetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::SubtitleType_strategy)
@settings(max_examples=50)
def test_docbook::subtitletype_instantiation(instance):
    assert isinstance(instance, Docbook::SubtitleType)

@given(instance=Docbook::SubtitleType_strategy)
def test_docbook::subtitletype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::SubtitleType_strategy)
def test_docbook::subtitletype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::SubtitleType_strategy)
def test_docbook::subtitletype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::SubtitleType_strategy)
def test_docbook::subtitletype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::ParamdefType_strategy)
@settings(max_examples=50)
def test_docbook::paramdeftype_instantiation(instance):
    assert isinstance(instance, Docbook::ParamdefType)

@given(instance=Docbook::ParamdefType_strategy)
def test_docbook::paramdeftype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::ParamdefType_strategy)
def test_docbook::paramdeftype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::FuncprototypeType_strategy)
@settings(max_examples=50)
def test_docbook::funcprototypetype_instantiation(instance):
    assert isinstance(instance, Docbook::FuncprototypeType)

@given(instance=Docbook::FuncsynopsisType_strategy)
@settings(max_examples=50)
def test_docbook::funcsynopsistype_instantiation(instance):
    assert isinstance(instance, Docbook::FuncsynopsisType)

@given(instance=Docbook::FileNameType_strategy)
@settings(max_examples=50)
def test_docbook::filenametype_instantiation(instance):
    assert isinstance(instance, Docbook::FileNameType)

@given(instance=Docbook::FileNameType_strategy)
def test_docbook::filenametype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::FileNameType_strategy)
def test_docbook::filenametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::FunctionType_strategy)
@settings(max_examples=50)
def test_docbook::functiontype_instantiation(instance):
    assert isinstance(instance, Docbook::FunctionType)

@given(instance=Docbook::FunctionType_strategy)
def test_docbook::functiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::FunctionType_strategy)
def test_docbook::functiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::FuncdefType_strategy)
@settings(max_examples=50)
def test_docbook::funcdeftype_instantiation(instance):
    assert isinstance(instance, Docbook::FuncdefType)

@given(instance=Docbook::FuncdefType_strategy)
def test_docbook::funcdeftype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::FuncdefType_strategy)
def test_docbook::funcdeftype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::FirstnameType_strategy)
@settings(max_examples=50)
def test_docbook::firstnametype_instantiation(instance):
    assert isinstance(instance, Docbook::FirstnameType)

@given(instance=Docbook::FirstnameType_strategy)
def test_docbook::firstnametype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::FirstnameType_strategy)
def test_docbook::firstnametype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::EnvarType_strategy)
@settings(max_examples=50)
def test_docbook::envartype_instantiation(instance):
    assert isinstance(instance, Docbook::EnvarType)

@given(instance=Docbook::EnvarType_strategy)
def test_docbook::envartype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::EnvarType_strategy)
def test_docbook::envartype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::ExampleType_strategy)
@settings(max_examples=50)
def test_docbook::exampletype_instantiation(instance):
    assert isinstance(instance, Docbook::ExampleType)

@given(instance=Docbook::ExampleType_strategy)
def test_docbook::exampletype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Docbook::ExampleType_strategy)
def test_docbook::exampletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook::TheadType_strategy)
@settings(max_examples=50)
def test_docbook::theadtype_instantiation(instance):
    assert isinstance(instance, Docbook::TheadType)

@given(instance=Docbook::TgroupType_strategy)
@settings(max_examples=50)
def test_docbook::tgrouptype_instantiation(instance):
    assert isinstance(instance, Docbook::TgroupType)

@given(instance=Docbook::TgroupType_strategy)
def test_docbook::tgrouptype_colseq_type(instance):
    assert isinstance(instance.colseq, str)


@given(instance=Docbook::TgroupType_strategy)
def test_docbook::tgrouptype_colseq_setter(instance):
    original = instance.colseq
    instance.colseq = original
    assert instance.colseq == original

@given(instance=Docbook::TgroupType_strategy)
def test_docbook::tgrouptype_cols_type(instance):
    assert isinstance(instance.cols, str)


@given(instance=Docbook::TgroupType_strategy)
def test_docbook::tgrouptype_cols_setter(instance):
    original = instance.cols
    instance.cols = original
    assert instance.cols == original

@given(instance=Docbook::TgroupType_strategy)
def test_docbook::tgrouptype_rowseq_type(instance):
    assert isinstance(instance.rowseq, str)


@given(instance=Docbook::TgroupType_strategy)
def test_docbook::tgrouptype_rowseq_setter(instance):
    original = instance.rowseq
    instance.rowseq = original
    assert instance.rowseq == original

@given(instance=Docbook::TgroupType_strategy)
def test_docbook::tgrouptype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=Docbook::TgroupType_strategy)
def test_docbook::tgrouptype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=Docbook::UlinkType_strategy)
@settings(max_examples=50)
def test_docbook::ulinktype_instantiation(instance):
    assert isinstance(instance, Docbook::UlinkType)

@given(instance=Docbook::UlinkType_strategy)
def test_docbook::ulinktype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::UlinkType_strategy)
def test_docbook::ulinktype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::UlinkType_strategy)
def test_docbook::ulinktype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=Docbook::UlinkType_strategy)
def test_docbook::ulinktype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=Docbook::UlinkType_strategy)
def test_docbook::ulinktype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=Docbook::UlinkType_strategy)
def test_docbook::ulinktype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=Docbook::TipType_strategy)
@settings(max_examples=50)
def test_docbook::tiptype_instantiation(instance):
    assert isinstance(instance, Docbook::TipType)

@given(instance=Docbook::TipType_strategy)
def test_docbook::tiptype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::TipType_strategy)
def test_docbook::tiptype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::TbodyType_strategy)
@settings(max_examples=50)
def test_docbook::tbodytype_instantiation(instance):
    assert isinstance(instance, Docbook::TbodyType)

@given(instance=Docbook::TableType_strategy)
@settings(max_examples=50)
def test_docbook::tabletype_instantiation(instance):
    assert isinstance(instance, Docbook::TableType)

@given(instance=Docbook::TableType_strategy)
def test_docbook::tabletype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Docbook::TableType_strategy)
def test_docbook::tabletype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook::ProgramlistingType_strategy)
@settings(max_examples=50)
def test_docbook::programlistingtype_instantiation(instance):
    assert isinstance(instance, Docbook::ProgramlistingType)

@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_language_type(instance):
    assert isinstance(instance.language, str)


@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_language_setter(instance):
    original = instance.language
    instance.language = original
    assert instance.language == original

@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_superscript_type(instance):
    assert isinstance(instance.superscript, str)


@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_superscript_setter(instance):
    original = instance.superscript
    instance.superscript = original
    assert instance.superscript == original

@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_linenumbering_type(instance):
    assert isinstance(instance.linenumbering, str)


@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_linenumbering_setter(instance):
    original = instance.linenumbering
    instance.linenumbering = original
    assert instance.linenumbering == original

@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=Docbook::ProgramlistingType_strategy)
def test_docbook::programlistingtype_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=Docbook::RowType_strategy)
@settings(max_examples=50)
def test_docbook::rowtype_instantiation(instance):
    assert isinstance(instance, Docbook::RowType)

@given(instance=Docbook::PhraseType_strategy)
@settings(max_examples=50)
def test_docbook::phrasetype_instantiation(instance):
    assert isinstance(instance, Docbook::PhraseType)

@given(instance=Docbook::PhraseType_strategy)
def test_docbook::phrasetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Docbook::PhraseType_strategy)
def test_docbook::phrasetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook::PublisherType_strategy)
@settings(max_examples=50)
def test_docbook::publishertype_instantiation(instance):
    assert isinstance(instance, Docbook::PublisherType)

@given(instance=Docbook::PublisherType_strategy)
def test_docbook::publishertype_publishername_type(instance):
    assert isinstance(instance.publishername, str)


@given(instance=Docbook::PublisherType_strategy)
def test_docbook::publishertype_publishername_setter(instance):
    original = instance.publishername
    instance.publishername = original
    assert instance.publishername == original

@given(instance=Docbook::OrderedlistType_strategy)
@settings(max_examples=50)
def test_docbook::orderedlisttype_instantiation(instance):
    assert isinstance(instance, Docbook::OrderedlistType)

@given(instance=Docbook::OrderedlistType_strategy)
def test_docbook::orderedlisttype_inheritnum_type(instance):
    assert isinstance(instance.inheritnum, str)


@given(instance=Docbook::OrderedlistType_strategy)
def test_docbook::orderedlisttype_inheritnum_setter(instance):
    original = instance.inheritnum
    instance.inheritnum = original
    assert instance.inheritnum == original

@given(instance=Docbook::OrderedlistType_strategy)
def test_docbook::orderedlisttype_continuation_type(instance):
    assert isinstance(instance.continuation, str)


@given(instance=Docbook::OrderedlistType_strategy)
def test_docbook::orderedlisttype_continuation_setter(instance):
    original = instance.continuation
    instance.continuation = original
    assert instance.continuation == original

@given(instance=Docbook::MediaobjectType_strategy)
@settings(max_examples=50)
def test_docbook::mediaobjecttype_instantiation(instance):
    assert isinstance(instance, Docbook::MediaobjectType)

@given(instance=Docbook::ListitemType_strategy)
@settings(max_examples=50)
def test_docbook::listitemtype_instantiation(instance):
    assert isinstance(instance, Docbook::ListitemType)

@given(instance=Docbook::LinkType_strategy)
@settings(max_examples=50)
def test_docbook::linktype_instantiation(instance):
    assert isinstance(instance, Docbook::LinkType)

@given(instance=Docbook::LinkType_strategy)
def test_docbook::linktype_linkend_type(instance):
    assert isinstance(instance.linkend, str)


@given(instance=Docbook::LinkType_strategy)
def test_docbook::linktype_linkend_setter(instance):
    original = instance.linkend
    instance.linkend = original
    assert instance.linkend == original

@given(instance=Docbook::LinkType_strategy)
def test_docbook::linktype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::LinkType_strategy)
def test_docbook::linktype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::LinkType_strategy)
def test_docbook::linktype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Docbook::LinkType_strategy)
def test_docbook::linktype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Docbook::KeywordsetType_strategy)
@settings(max_examples=50)
def test_docbook::keywordsettype_instantiation(instance):
    assert isinstance(instance, Docbook::KeywordsetType)

@given(instance=Docbook::KeywordsetType_strategy)
def test_docbook::keywordsettype_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=Docbook::KeywordsetType_strategy)
def test_docbook::keywordsettype_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=Docbook::LiteralType_strategy)
@settings(max_examples=50)
def test_docbook::literaltype_instantiation(instance):
    assert isinstance(instance, Docbook::LiteralType)

@given(instance=Docbook::LiteralType_strategy)
def test_docbook::literaltype_moreinfo_type(instance):
    assert isinstance(instance.moreinfo, str)


@given(instance=Docbook::LiteralType_strategy)
def test_docbook::literaltype_moreinfo_setter(instance):
    original = instance.moreinfo
    instance.moreinfo = original
    assert instance.moreinfo == original

@given(instance=Docbook::LiteralType_strategy)
def test_docbook::literaltype_value_type(instance):
    assert isinstance(instance.value, str)


@given(instance=Docbook::LiteralType_strategy)
def test_docbook::literaltype_value_setter(instance):
    original = instance.value
    instance.value = original
    assert instance.value == original

@given(instance=Docbook::ImportantType_strategy)
@settings(max_examples=50)
def test_docbook::importanttype_instantiation(instance):
    assert isinstance(instance, Docbook::ImportantType)

@given(instance=Docbook::ImportantType_strategy)
def test_docbook::importanttype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::ImportantType_strategy)
def test_docbook::importanttype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::ImportantType_strategy)
def test_docbook::importanttype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::ImportantType_strategy)
def test_docbook::importanttype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::ImageobjectType_strategy)
@settings(max_examples=50)
def test_docbook::imageobjecttype_instantiation(instance):
    assert isinstance(instance, Docbook::ImageobjectType)

@given(instance=Docbook::ImagedataType_strategy)
@settings(max_examples=50)
def test_docbook::imagedatatype_instantiation(instance):
    assert isinstance(instance, Docbook::ImagedataType)

@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_width_type(instance):
    assert isinstance(instance.width, str)


@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original

@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_fileref_type(instance):
    assert isinstance(instance.fileref, str)


@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_fileref_setter(instance):
    original = instance.fileref
    instance.fileref = original
    assert instance.fileref == original

@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_depth_type(instance):
    assert isinstance(instance.depth, str)


@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_depth_setter(instance):
    original = instance.depth
    instance.depth = original
    assert instance.depth == original

@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_scale_type(instance):
    assert isinstance(instance.scale, str)


@given(instance=Docbook::ImagedataType_strategy)
def test_docbook::imagedatatype_scale_setter(instance):
    original = instance.scale
    instance.scale = original
    assert instance.scale == original

@given(instance=Docbook::FootnoteType_strategy)
@settings(max_examples=50)
def test_docbook::footnotetype_instantiation(instance):
    assert isinstance(instance, Docbook::FootnoteType)

@given(instance=Docbook::FootnoteType_strategy)
def test_docbook::footnotetype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Docbook::FootnoteType_strategy)
def test_docbook::footnotetype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook::ItemizedlistType_strategy)
@settings(max_examples=50)
def test_docbook::itemizedlisttype_instantiation(instance):
    assert isinstance(instance, Docbook::ItemizedlistType)

@given(instance=Docbook::InformaltableType_strategy)
@settings(max_examples=50)
def test_docbook::informaltabletype_instantiation(instance):
    assert isinstance(instance, Docbook::InformaltableType)

@given(instance=Docbook::FigureType_strategy)
@settings(max_examples=50)
def test_docbook::figuretype_instantiation(instance):
    assert isinstance(instance, Docbook::FigureType)

@given(instance=Docbook::FigureType_strategy)
def test_docbook::figuretype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Docbook::FigureType_strategy)
def test_docbook::figuretype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook::FigureType_strategy)
def test_docbook::figuretype_float_type(instance):
    assert isinstance(instance.float, str)


@given(instance=Docbook::FigureType_strategy)
def test_docbook::figuretype_float_setter(instance):
    original = instance.float
    instance.float = original
    assert instance.float == original

@given(instance=Docbook::EntryType_strategy)
@settings(max_examples=50)
def test_docbook::entrytype_instantiation(instance):
    assert isinstance(instance, Docbook::EntryType)

@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_align_type(instance):
    assert isinstance(instance.align, str)


@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_align_setter(instance):
    original = instance.align
    instance.align = original
    assert instance.align == original

@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_valign_type(instance):
    assert isinstance(instance.valign, str)


@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_valign_setter(instance):
    original = instance.valign
    instance.valign = original
    assert instance.valign == original

@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_nameend_type(instance):
    assert isinstance(instance.nameend, str)


@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_nameend_setter(instance):
    original = instance.nameend
    instance.nameend = original
    assert instance.nameend == original

@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_namest_type(instance):
    assert isinstance(instance.namest, str)


@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_namest_setter(instance):
    original = instance.namest
    instance.namest = original
    assert instance.namest == original

@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_morerows_type(instance):
    assert isinstance(instance.morerows, str)


@given(instance=Docbook::EntryType_strategy)
def test_docbook::entrytype_morerows_setter(instance):
    original = instance.morerows
    instance.morerows = original
    assert instance.morerows == original

@given(instance=Docbook::EmphasisType_strategy)
@settings(max_examples=50)
def test_docbook::emphasistype_instantiation(instance):
    assert isinstance(instance, Docbook::EmphasisType)

@given(instance=Docbook::EmphasisType_strategy)
def test_docbook::emphasistype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::EmphasisType_strategy)
def test_docbook::emphasistype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::EmphasisType_strategy)
def test_docbook::emphasistype_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=Docbook::EmphasisType_strategy)
def test_docbook::emphasistype_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=Docbook::DateType_strategy)
@settings(max_examples=50)
def test_docbook::datetype_instantiation(instance):
    assert isinstance(instance, Docbook::DateType)

@given(instance=Docbook::DateType_strategy)
def test_docbook::datetype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::DateType_strategy)
def test_docbook::datetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::CopyrightType_strategy)
@settings(max_examples=50)
def test_docbook::copyrighttype_instantiation(instance):
    assert isinstance(instance, Docbook::CopyrightType)

@given(instance=Docbook::CopyrightType_strategy)
def test_docbook::copyrighttype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::CopyrightType_strategy)
def test_docbook::copyrighttype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::CopyrightType_strategy)
def test_docbook::copyrighttype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=Docbook::CopyrightType_strategy)
def test_docbook::copyrighttype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=Docbook::CopyrightType_strategy)
def test_docbook::copyrighttype_holder_type(instance):
    assert isinstance(instance.holder, str)


@given(instance=Docbook::CopyrightType_strategy)
def test_docbook::copyrighttype_holder_setter(instance):
    original = instance.holder
    instance.holder = original
    assert instance.holder == original

@given(instance=Docbook::ConfgroupType_strategy)
@settings(max_examples=50)
def test_docbook::confgrouptype_instantiation(instance):
    assert isinstance(instance, Docbook::ConfgroupType)

@given(instance=Docbook::ConfgroupType_strategy)
def test_docbook::confgrouptype_confnum_type(instance):
    assert isinstance(instance.confnum, str)


@given(instance=Docbook::ConfgroupType_strategy)
def test_docbook::confgrouptype_confnum_setter(instance):
    original = instance.confnum
    instance.confnum = original
    assert instance.confnum == original

@given(instance=Docbook::ConfgroupType_strategy)
def test_docbook::confgrouptype_confsponsor_type(instance):
    assert isinstance(instance.confsponsor, str)


@given(instance=Docbook::ConfgroupType_strategy)
def test_docbook::confgrouptype_confsponsor_setter(instance):
    original = instance.confsponsor
    instance.confsponsor = original
    assert instance.confsponsor == original

@given(instance=Docbook::ConfgroupType_strategy)
def test_docbook::confgrouptype_conftitle_type(instance):
    assert isinstance(instance.conftitle, str)


@given(instance=Docbook::ConfgroupType_strategy)
def test_docbook::confgrouptype_conftitle_setter(instance):
    original = instance.conftitle
    instance.conftitle = original
    assert instance.conftitle == original

@given(instance=Docbook::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_docbook::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, Docbook::EStringToStringMapEntry)

@given(instance=Docbook::DocumentRoot_strategy)
@settings(max_examples=50)
def test_docbook::documentroot_instantiation(instance):
    assert isinstance(instance, Docbook::DocumentRoot)

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_confsponsor_type(instance):
    assert isinstance(instance.confsponsor, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_confsponsor_setter(instance):
    original = instance.confsponsor
    instance.confsponsor = original
    assert instance.confsponsor == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_keyword_type(instance):
    assert isinstance(instance.keyword, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_keyword_setter(instance):
    original = instance.keyword
    instance.keyword = original
    assert instance.keyword == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_pubdate_type(instance):
    assert isinstance(instance.pubdate, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_pubdate_setter(instance):
    original = instance.pubdate
    instance.pubdate = original
    assert instance.pubdate == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_publishername_type(instance):
    assert isinstance(instance.publishername, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_publishername_setter(instance):
    original = instance.publishername
    instance.publishername = original
    assert instance.publishername == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_firstname_type(instance):
    assert isinstance(instance.firstname, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_firstname_setter(instance):
    original = instance.firstname
    instance.firstname = original
    assert instance.firstname == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_warning_type(instance):
    assert isinstance(instance.warning, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_warning_setter(instance):
    original = instance.warning
    instance.warning = original
    assert instance.warning == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_subtitle_type(instance):
    assert isinstance(instance.subtitle, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_subtitle_setter(instance):
    original = instance.subtitle
    instance.subtitle = original
    assert instance.subtitle == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_superscript_type(instance):
    assert isinstance(instance.superscript, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_superscript_setter(instance):
    original = instance.superscript
    instance.superscript = original
    assert instance.superscript == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_caution_type(instance):
    assert isinstance(instance.caution, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_caution_setter(instance):
    original = instance.caution
    instance.caution = original
    assert instance.caution == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_bibliomisc_type(instance):
    assert isinstance(instance.bibliomisc, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_bibliomisc_setter(instance):
    original = instance.bibliomisc
    instance.bibliomisc = original
    assert instance.bibliomisc == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_conftitle_type(instance):
    assert isinstance(instance.conftitle, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_conftitle_setter(instance):
    original = instance.conftitle
    instance.conftitle = original
    assert instance.conftitle == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_confnum_type(instance):
    assert isinstance(instance.confnum, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_confnum_setter(instance):
    original = instance.confnum
    instance.confnum = original
    assert instance.confnum == original

@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=Docbook::DocumentRoot_strategy)
def test_docbook::documentroot_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Docbook::CommandType_strategy)
@settings(max_examples=50)
def test_docbook::commandtype_instantiation(instance):
    assert isinstance(instance, Docbook::CommandType)

@given(instance=Docbook::CommandType_strategy)
def test_docbook::commandtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::CommandType_strategy)
def test_docbook::commandtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::CmdsynopsisType_strategy)
@settings(max_examples=50)
def test_docbook::cmdsynopsistype_instantiation(instance):
    assert isinstance(instance, Docbook::CmdsynopsisType)

@given(instance=Docbook::ColspecType_strategy)
@settings(max_examples=50)
def test_docbook::colspectype_instantiation(instance):
    assert isinstance(instance, Docbook::ColspecType)

@given(instance=Docbook::ColspecType_strategy)
def test_docbook::colspectype_colname_type(instance):
    assert isinstance(instance.colname, str)


@given(instance=Docbook::ColspecType_strategy)
def test_docbook::colspectype_colname_setter(instance):
    original = instance.colname
    instance.colname = original
    assert instance.colname == original

@given(instance=Docbook::ColspecType_strategy)
def test_docbook::colspectype_colwidth_type(instance):
    assert isinstance(instance.colwidth, str)


@given(instance=Docbook::ColspecType_strategy)
def test_docbook::colspectype_colwidth_setter(instance):
    original = instance.colwidth
    instance.colwidth = original
    assert instance.colwidth == original

@given(instance=Docbook::SectionType_strategy)
@settings(max_examples=50)
def test_docbook::sectiontype_instantiation(instance):
    assert isinstance(instance, Docbook::SectionType)

@given(instance=Docbook::SectionType_strategy)
def test_docbook::sectiontype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::SectionType_strategy)
def test_docbook::sectiontype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::SectionType_strategy)
def test_docbook::sectiontype_annotations_type(instance):
    assert isinstance(instance.annotations, str)


@given(instance=Docbook::SectionType_strategy)
def test_docbook::sectiontype_annotations_setter(instance):
    original = instance.annotations
    instance.annotations = original
    assert instance.annotations == original

@given(instance=Docbook::SectionType_strategy)
def test_docbook::sectiontype_warning_type(instance):
    assert isinstance(instance.warning, str)


@given(instance=Docbook::SectionType_strategy)
def test_docbook::sectiontype_warning_setter(instance):
    original = instance.warning
    instance.warning = original
    assert instance.warning == original

@given(instance=Docbook::SectionType_strategy)
def test_docbook::sectiontype_caution_type(instance):
    assert isinstance(instance.caution, str)


@given(instance=Docbook::SectionType_strategy)
def test_docbook::sectiontype_caution_setter(instance):
    original = instance.caution
    instance.caution = original
    assert instance.caution == original

@given(instance=Docbook::NoteType_strategy)
@settings(max_examples=50)
def test_docbook::notetype_instantiation(instance):
    assert isinstance(instance, Docbook::NoteType)

@given(instance=Docbook::NoteType_strategy)
def test_docbook::notetype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::NoteType_strategy)
def test_docbook::notetype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::NoteType_strategy)
def test_docbook::notetype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::NoteType_strategy)
def test_docbook::notetype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::ReferenceType_strategy)
@settings(max_examples=50)
def test_docbook::referencetype_instantiation(instance):
    assert isinstance(instance, Docbook::ReferenceType)

@given(instance=Docbook::ReferenceType_strategy)
def test_docbook::referencetype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=Docbook::ReferenceType_strategy)
def test_docbook::referencetype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Docbook::ChapterType_strategy)
@settings(max_examples=50)
def test_docbook::chaptertype_instantiation(instance):
    assert isinstance(instance, Docbook::ChapterType)

@given(instance=Docbook::ChapterType_strategy)
def test_docbook::chaptertype_annotations_type(instance):
    assert isinstance(instance.annotations, str)


@given(instance=Docbook::ChapterType_strategy)
def test_docbook::chaptertype_annotations_setter(instance):
    original = instance.annotations
    instance.annotations = original
    assert instance.annotations == original

@given(instance=Docbook::ArgType_strategy)
@settings(max_examples=50)
def test_docbook::argtype_instantiation(instance):
    assert isinstance(instance, Docbook::ArgType)

@given(instance=Docbook::ArgType_strategy)
def test_docbook::argtype_rep_type(instance):
    assert isinstance(instance.rep, str)


@given(instance=Docbook::ArgType_strategy)
def test_docbook::argtype_rep_setter(instance):
    original = instance.rep
    instance.rep = original
    assert instance.rep == original

@given(instance=Docbook::ArgType_strategy)
def test_docbook::argtype_choice_type(instance):
    assert isinstance(instance.choice, str)


@given(instance=Docbook::ArgType_strategy)
def test_docbook::argtype_choice_setter(instance):
    original = instance.choice
    instance.choice = original
    assert instance.choice == original

@given(instance=Docbook::ArgType_strategy)
def test_docbook::argtype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::ArgType_strategy)
def test_docbook::argtype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::AddressType_strategy)
@settings(max_examples=50)
def test_docbook::addresstype_instantiation(instance):
    assert isinstance(instance, Docbook::AddressType)

@given(instance=Docbook::AddressType_strategy)
def test_docbook::addresstype_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=Docbook::AddressType_strategy)
def test_docbook::addresstype_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=Docbook::AddressType_strategy)
def test_docbook::addresstype_state_type(instance):
    assert isinstance(instance.state, str)


@given(instance=Docbook::AddressType_strategy)
def test_docbook::addresstype_state_setter(instance):
    original = instance.state
    instance.state = original
    assert instance.state == original

@given(instance=Docbook::AddressType_strategy)
def test_docbook::addresstype_format_type(instance):
    assert isinstance(instance.format, str)


@given(instance=Docbook::AddressType_strategy)
def test_docbook::addresstype_format_setter(instance):
    original = instance.format
    instance.format = original
    assert instance.format == original

@given(instance=Docbook::ParaType_strategy)
@settings(max_examples=50)
def test_docbook::paratype_instantiation(instance):
    assert isinstance(instance, Docbook::ParaType)

@given(instance=Docbook::ParaType_strategy)
def test_docbook::paratype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::ParaType_strategy)
def test_docbook::paratype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::ParaType_strategy)
def test_docbook::paratype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::ParaType_strategy)
def test_docbook::paratype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::ParaType_strategy)
def test_docbook::paratype_role_type(instance):
    assert isinstance(instance.role, str)


@given(instance=Docbook::ParaType_strategy)
def test_docbook::paratype_role_setter(instance):
    original = instance.role
    instance.role = original
    assert instance.role == original

@given(instance=Docbook::ParaType_strategy)
def test_docbook::paratype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=Docbook::ParaType_strategy)
def test_docbook::paratype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Docbook::AbstractType_strategy)
@settings(max_examples=50)
def test_docbook::abstracttype_instantiation(instance):
    assert isinstance(instance, Docbook::AbstractType)

@given(instance=Docbook::PrefaceType_strategy)
@settings(max_examples=50)
def test_docbook::prefacetype_instantiation(instance):
    assert isinstance(instance, Docbook::PrefaceType)

@given(instance=Docbook::InfoType_strategy)
@settings(max_examples=50)
def test_docbook::infotype_instantiation(instance):
    assert isinstance(instance, Docbook::InfoType)

@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_productname_type(instance):
    assert isinstance(instance.productname, str)


@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_productname_setter(instance):
    original = instance.productname
    instance.productname = original
    assert instance.productname == original

@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_bibliomisc_type(instance):
    assert isinstance(instance.bibliomisc, str)


@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_bibliomisc_setter(instance):
    original = instance.bibliomisc
    instance.bibliomisc = original
    assert instance.bibliomisc == original

@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_date_type(instance):
    assert isinstance(instance.date, str)


@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_date_setter(instance):
    original = instance.date
    instance.date = original
    assert instance.date == original

@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_releaseinfo_type(instance):
    assert isinstance(instance.releaseinfo, str)


@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_releaseinfo_setter(instance):
    original = instance.releaseinfo
    instance.releaseinfo = original
    assert instance.releaseinfo == original

@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_pubdate_type(instance):
    assert isinstance(instance.pubdate, str)


@given(instance=Docbook::InfoType_strategy)
def test_docbook::infotype_pubdate_setter(instance):
    original = instance.pubdate
    instance.pubdate = original
    assert instance.pubdate == original

@given(instance=Docbook::BookType_strategy)
@settings(max_examples=50)
def test_docbook::booktype_instantiation(instance):
    assert isinstance(instance, Docbook::BookType)

@given(instance=Docbook::BookType_strategy)
def test_docbook::booktype_label_type(instance):
    assert isinstance(instance.label, str)


@given(instance=Docbook::BookType_strategy)
def test_docbook::booktype_label_setter(instance):
    original = instance.label
    instance.label = original
    assert instance.label == original

@given(instance=Docbook::BookType_strategy)
def test_docbook::booktype_version_type(instance):
    assert isinstance(instance.version, str)


@given(instance=Docbook::BookType_strategy)
def test_docbook::booktype_version_setter(instance):
    original = instance.version
    instance.version = original
    assert instance.version == original

@given(instance=Docbook::BookType_strategy)
def test_docbook::booktype_lang_type(instance):
    assert isinstance(instance.lang, str)


@given(instance=Docbook::BookType_strategy)
def test_docbook::booktype_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=Docbook::TitleType_strategy)
@settings(max_examples=50)
def test_docbook::titletype_instantiation(instance):
    assert isinstance(instance, Docbook::TitleType)

@given(instance=Docbook::TitleType_strategy)
def test_docbook::titletype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::TitleType_strategy)
def test_docbook::titletype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::TitleType_strategy)
def test_docbook::titletype_group_type(instance):
    assert isinstance(instance.group, str)


@given(instance=Docbook::TitleType_strategy)
def test_docbook::titletype_group_setter(instance):
    original = instance.group
    instance.group = original
    assert instance.group == original

@given(instance=Docbook::OtheraddrType_strategy)
@settings(max_examples=50)
def test_docbook::otheraddrtype_instantiation(instance):
    assert isinstance(instance, Docbook::OtheraddrType)

@given(instance=Docbook::PersonnameType_strategy)
@settings(max_examples=50)
def test_docbook::personnametype_instantiation(instance):
    assert isinstance(instance, Docbook::PersonnameType)

@given(instance=Docbook::AuthorType_strategy)
@settings(max_examples=50)
def test_docbook::authortype_instantiation(instance):
    assert isinstance(instance, Docbook::AuthorType)

@given(instance=Docbook::AuthorType_strategy)
def test_docbook::authortype_contrib_type(instance):
    assert isinstance(instance.contrib, str)


@given(instance=Docbook::AuthorType_strategy)
def test_docbook::authortype_contrib_setter(instance):
    original = instance.contrib
    instance.contrib = original
    assert instance.contrib == original

@given(instance=Docbook::AuthorinitialsType_strategy)
@settings(max_examples=50)
def test_docbook::authorinitialstype_instantiation(instance):
    assert isinstance(instance, Docbook::AuthorinitialsType)

@given(instance=Docbook::AuthorinitialsType_strategy)
def test_docbook::authorinitialstype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::AuthorinitialsType_strategy)
def test_docbook::authorinitialstype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::ReplaceableType_strategy)
@settings(max_examples=50)
def test_docbook::replaceabletype_instantiation(instance):
    assert isinstance(instance, Docbook::ReplaceableType)

@given(instance=Docbook::ReplaceableType_strategy)
def test_docbook::replaceabletype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::ReplaceableType_strategy)
def test_docbook::replaceabletype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=Docbook::OptionType_strategy)
@settings(max_examples=50)
def test_docbook::optiontype_instantiation(instance):
    assert isinstance(instance, Docbook::OptionType)

@given(instance=Docbook::OptionType_strategy)
def test_docbook::optiontype_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=Docbook::OptionType_strategy)
def test_docbook::optiontype_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original
