import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    RichStringListElement,
    BPMProcessDocument,
    DTODocument,
    EntityDocument,
    UIDocument,
    VaaclipseViewDocument,
    BPMHumanTaskDocument,
    RichStringTableData,
    RichStringElseIf,
    RichStringMarkup,
    luniferadoc_richstring_RichStringH1,
    luniferadoc_richstring_RichStringH6,
    luniferadoc_richstring_RichStringOrderedList,
    luniferadoc_richstring_RichStringH5,
    luniferadoc_richstring_RichStringItalic,
    luniferadoc_richstring_RichStringTableRow,
    luniferadoc_richstring_RichStringSection,
    luniferadoc_richstring_RichStringDTORef,
    luniferadoc_richstring_RichStringSkype,
    luniferadoc_richstring_RichStringH2,
    luniferadoc_richstring_RichStringSubsection,
    luniferadoc_richstring_RichStringListElement,
    luniferadoc_richstring_RichStringBold,
    luniferadoc_richstring_RichStringUIRef,
    luniferadoc_richstring_RichStringH3,
    luniferadoc_richstring_RichStringTaskRef,
    luniferadoc_richstring_RichStringChapter,
    luniferadoc_richstring_RichStringH4,
    luniferadoc_richstring_RichStringUnderline,
    luniferadoc_richstring_RichStringMailto,
    luniferadoc_richstring_RichStringURL,
    luniferadoc_richstring_RichStringRef,
    luniferadoc_richstring_RichStringList,
    luniferadoc_richstring_RichStringProcessRef,
    luniferadoc_richstring_RichStringSpan,
    luniferadoc_richstring_RichStringViewRef,
    luniferadoc_richstring_RichStringExample,
    XForLoopExpression,
    luniferadoc_richstring_RichStringForLoop,
    XStringLiteral,
    luniferadoc_richstring_RichStringLiteral,
    XBlockExpression,
    luniferadoc_richstring_RichString,
    XExpression,
    luniferadoc_richstring_RichStringMarkup,
    luniferadoc_richstring_RichStringIf,
    document_luniferadoc_XImportDeclaration,
    richstring_luniferadoc_XExpression,
    luniferadoc_richstring_RichStringElseIf,
    luniferadoc_document_VaaclipseViewDescription,
    VaaclipseViewDescription,
    document_luniferadoc_DocumentInclude,
    LuniferaDocLayout,
    luniferadoc_document_VaaclipseViewLayout,
    luniferadoc_document_DTOLayout,
    luniferadoc_document_UILayout,
    luniferadoc_document_BPMHumanTaskLayout,
    luniferadoc_document_BPMProcessLayout,
    luniferadoc_document_EntityLayout,
    luniferadoc_document_GeneralDocument,
    luniferadoc_document_UIDescription,
    UIDescription,
    luniferadoc_document_BPMProcessDescription,
    BPMProcessDescription,
    luniferadoc_document_DTOProperty,
    luniferadoc_document_BPMHumanTaskDescription,
    BPMHumanTaskDescription,
    DTODescription,
    DTOProperty,
    luniferadoc_document_DTOProperties,
    luniferadoc_document_DTODescription,
    DTOProperties,
    EntityFields,
    EntityDescription,
    NamedDocument,
    luniferadoc_document_LuniferaDocLayout,
    luniferadoc_document_LuniferaDocDocument,
    luniferadoc_document_EntityField,
    EntityField,
    luniferadoc_document_EntityFields,
    RichString,
    luniferadoc_document_EntityDescription,
    LuniferaDocDocument,
    luniferadoc_document_BPMProcessDocument,
    luniferadoc_document_DTODocument,
    luniferadoc_document_UIDocument,
    luniferadoc_document_EntityDocument,
    luniferadoc_document_BPMHumanTaskDocument,
    luniferadoc_document_VaaclipseViewDocument,
    luniferadoc_DocumentInclude,
    luniferadoc_NamedDocument,
    luniferadoc_richstring_RichStringEntityRef,
    luniferadoc_richstring_RichStringStartProcess,
    luniferadoc_richstring_RichStringOpenView,
    luniferadoc_richstring_RichStringTableData,
    luniferadoc_richstring_RichStringCode,
    luniferadoc_richstring_RichStringMovie,
    RichStringTableRow,
    luniferadoc_richstring_RichStringTable,
    luniferadoc_richstring_RichStringImg,
    DocType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_richstringlistelement_is_not_abstract():
    assert not inspect.isabstract(RichStringListElement)


def test_richstringlistelement_constructor_exists():
    assert callable(RichStringListElement.__init__)


def test_richstringlistelement_constructor_args():
    sig = inspect.signature(RichStringListElement.__init__)
    params = list(sig.parameters.keys())



def test_bpmprocessdocument_is_not_abstract():
    assert not inspect.isabstract(BPMProcessDocument)


def test_bpmprocessdocument_constructor_exists():
    assert callable(BPMProcessDocument.__init__)


def test_bpmprocessdocument_constructor_args():
    sig = inspect.signature(BPMProcessDocument.__init__)
    params = list(sig.parameters.keys())



def test_dtodocument_is_not_abstract():
    assert not inspect.isabstract(DTODocument)


def test_dtodocument_constructor_exists():
    assert callable(DTODocument.__init__)


def test_dtodocument_constructor_args():
    sig = inspect.signature(DTODocument.__init__)
    params = list(sig.parameters.keys())



def test_entitydocument_is_not_abstract():
    assert not inspect.isabstract(EntityDocument)


def test_entitydocument_constructor_exists():
    assert callable(EntityDocument.__init__)


def test_entitydocument_constructor_args():
    sig = inspect.signature(EntityDocument.__init__)
    params = list(sig.parameters.keys())



def test_uidocument_is_not_abstract():
    assert not inspect.isabstract(UIDocument)


def test_uidocument_constructor_exists():
    assert callable(UIDocument.__init__)


def test_uidocument_constructor_args():
    sig = inspect.signature(UIDocument.__init__)
    params = list(sig.parameters.keys())



def test_vaaclipseviewdocument_is_not_abstract():
    assert not inspect.isabstract(VaaclipseViewDocument)


def test_vaaclipseviewdocument_constructor_exists():
    assert callable(VaaclipseViewDocument.__init__)


def test_vaaclipseviewdocument_constructor_args():
    sig = inspect.signature(VaaclipseViewDocument.__init__)
    params = list(sig.parameters.keys())



def test_bpmhumantaskdocument_is_not_abstract():
    assert not inspect.isabstract(BPMHumanTaskDocument)


def test_bpmhumantaskdocument_constructor_exists():
    assert callable(BPMHumanTaskDocument.__init__)


def test_bpmhumantaskdocument_constructor_args():
    sig = inspect.signature(BPMHumanTaskDocument.__init__)
    params = list(sig.parameters.keys())



def test_richstringtabledata_is_not_abstract():
    assert not inspect.isabstract(RichStringTableData)


def test_richstringtabledata_constructor_exists():
    assert callable(RichStringTableData.__init__)


def test_richstringtabledata_constructor_args():
    sig = inspect.signature(RichStringTableData.__init__)
    params = list(sig.parameters.keys())



def test_richstringelseif_is_not_abstract():
    assert not inspect.isabstract(RichStringElseIf)


def test_richstringelseif_constructor_exists():
    assert callable(RichStringElseIf.__init__)


def test_richstringelseif_constructor_args():
    sig = inspect.signature(RichStringElseIf.__init__)
    params = list(sig.parameters.keys())



def test_richstringmarkup_is_not_abstract():
    assert not inspect.isabstract(RichStringMarkup)


def test_richstringmarkup_constructor_exists():
    assert callable(RichStringMarkup.__init__)


def test_richstringmarkup_constructor_args():
    sig = inspect.signature(RichStringMarkup.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringh1_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringH1)


def test_luniferadoc_richstring_richstringh1_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringH1.__init__)


def test_luniferadoc_richstring_richstringh1_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringH1.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringh6_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringH6)


def test_luniferadoc_richstring_richstringh6_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringH6.__init__)


def test_luniferadoc_richstring_richstringh6_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringH6.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringorderedlist_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringOrderedList)


def test_luniferadoc_richstring_richstringorderedlist_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringOrderedList.__init__)


def test_luniferadoc_richstring_richstringorderedlist_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringOrderedList.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringh5_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringH5)


def test_luniferadoc_richstring_richstringh5_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringH5.__init__)


def test_luniferadoc_richstring_richstringh5_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringH5.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringitalic_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringItalic)


def test_luniferadoc_richstring_richstringitalic_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringItalic.__init__)


def test_luniferadoc_richstring_richstringitalic_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringItalic.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringtablerow_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringTableRow)


def test_luniferadoc_richstring_richstringtablerow_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringTableRow.__init__)


def test_luniferadoc_richstring_richstringtablerow_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringTableRow.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringsection_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringSection)


def test_luniferadoc_richstring_richstringsection_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringSection.__init__)


def test_luniferadoc_richstring_richstringsection_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringSection.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_luniferadoc_richstring_richstringsection_has_name():
    assert hasattr(luniferadoc_richstring_RichStringSection, "name")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringSection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringdtoref_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringDTORef)


def test_luniferadoc_richstring_richstringdtoref_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringDTORef.__init__)


def test_luniferadoc_richstring_richstringdtoref_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringDTORef.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringskype_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringSkype)


def test_luniferadoc_richstring_richstringskype_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringSkype.__init__)


def test_luniferadoc_richstring_richstringskype_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringSkype.__init__)
    params = list(sig.parameters.keys())
    assert "target" in params, "Missing parameter 'target'"

def test_luniferadoc_richstring_richstringskype_has_target():
    assert hasattr(luniferadoc_richstring_RichStringSkype, "target")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringSkype.__mro__:
        if "target" in klass.__dict__:
            descriptor = klass.__dict__["target"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringh2_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringH2)


def test_luniferadoc_richstring_richstringh2_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringH2.__init__)


def test_luniferadoc_richstring_richstringh2_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringH2.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringsubsection_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringSubsection)


def test_luniferadoc_richstring_richstringsubsection_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringSubsection.__init__)


def test_luniferadoc_richstring_richstringsubsection_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringSubsection.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_luniferadoc_richstring_richstringsubsection_has_name():
    assert hasattr(luniferadoc_richstring_RichStringSubsection, "name")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringSubsection.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringlistelement_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringListElement)


def test_luniferadoc_richstring_richstringlistelement_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringListElement.__init__)


def test_luniferadoc_richstring_richstringlistelement_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringListElement.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringbold_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringBold)


def test_luniferadoc_richstring_richstringbold_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringBold.__init__)


def test_luniferadoc_richstring_richstringbold_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringBold.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringuiref_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringUIRef)


def test_luniferadoc_richstring_richstringuiref_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringUIRef.__init__)


def test_luniferadoc_richstring_richstringuiref_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringUIRef.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringh3_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringH3)


def test_luniferadoc_richstring_richstringh3_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringH3.__init__)


def test_luniferadoc_richstring_richstringh3_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringH3.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringtaskref_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringTaskRef)


def test_luniferadoc_richstring_richstringtaskref_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringTaskRef.__init__)


def test_luniferadoc_richstring_richstringtaskref_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringTaskRef.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringchapter_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringChapter)


def test_luniferadoc_richstring_richstringchapter_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringChapter.__init__)


def test_luniferadoc_richstring_richstringchapter_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringChapter.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_luniferadoc_richstring_richstringchapter_has_name():
    assert hasattr(luniferadoc_richstring_RichStringChapter, "name")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringChapter.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringh4_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringH4)


def test_luniferadoc_richstring_richstringh4_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringH4.__init__)


def test_luniferadoc_richstring_richstringh4_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringH4.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringunderline_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringUnderline)


def test_luniferadoc_richstring_richstringunderline_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringUnderline.__init__)


def test_luniferadoc_richstring_richstringunderline_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringUnderline.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringmailto_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringMailto)


def test_luniferadoc_richstring_richstringmailto_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringMailto.__init__)


def test_luniferadoc_richstring_richstringmailto_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringMailto.__init__)
    params = list(sig.parameters.keys())
    assert "email" in params, "Missing parameter 'email'"

def test_luniferadoc_richstring_richstringmailto_has_email():
    assert hasattr(luniferadoc_richstring_RichStringMailto, "email")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringMailto.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringurl_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringURL)


def test_luniferadoc_richstring_richstringurl_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringURL.__init__)


def test_luniferadoc_richstring_richstringurl_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringURL.__init__)
    params = list(sig.parameters.keys())
    assert "location" in params, "Missing parameter 'location'"

def test_luniferadoc_richstring_richstringurl_has_location():
    assert hasattr(luniferadoc_richstring_RichStringURL, "location")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringURL.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringref_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringRef)


def test_luniferadoc_richstring_richstringref_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringRef.__init__)


def test_luniferadoc_richstring_richstringref_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringRef.__init__)
    params = list(sig.parameters.keys())
    assert "refId" in params, "Missing parameter 'refId'"

def test_luniferadoc_richstring_richstringref_has_refId():
    assert hasattr(luniferadoc_richstring_RichStringRef, "refId")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringRef.__mro__:
        if "refId" in klass.__dict__:
            descriptor = klass.__dict__["refId"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringlist_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringList)


def test_luniferadoc_richstring_richstringlist_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringList.__init__)


def test_luniferadoc_richstring_richstringlist_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringList.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringprocessref_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringProcessRef)


def test_luniferadoc_richstring_richstringprocessref_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringProcessRef.__init__)


def test_luniferadoc_richstring_richstringprocessref_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringProcessRef.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringspan_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringSpan)


def test_luniferadoc_richstring_richstringspan_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringSpan.__init__)


def test_luniferadoc_richstring_richstringspan_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringSpan.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringviewref_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringViewRef)


def test_luniferadoc_richstring_richstringviewref_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringViewRef.__init__)


def test_luniferadoc_richstring_richstringviewref_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringViewRef.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringexample_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringExample)


def test_luniferadoc_richstring_richstringexample_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringExample.__init__)


def test_luniferadoc_richstring_richstringexample_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringExample.__init__)
    params = list(sig.parameters.keys())



def test_xforloopexpression_is_not_abstract():
    assert not inspect.isabstract(XForLoopExpression)


def test_xforloopexpression_constructor_exists():
    assert callable(XForLoopExpression.__init__)


def test_xforloopexpression_constructor_args():
    sig = inspect.signature(XForLoopExpression.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringforloop_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringForLoop)


def test_luniferadoc_richstring_richstringforloop_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringForLoop.__init__)


def test_luniferadoc_richstring_richstringforloop_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringForLoop.__init__)
    params = list(sig.parameters.keys())



def test_xstringliteral_is_not_abstract():
    assert not inspect.isabstract(XStringLiteral)


def test_xstringliteral_constructor_exists():
    assert callable(XStringLiteral.__init__)


def test_xstringliteral_constructor_args():
    sig = inspect.signature(XStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringliteral_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringLiteral)


def test_luniferadoc_richstring_richstringliteral_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringLiteral.__init__)


def test_luniferadoc_richstring_richstringliteral_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringLiteral.__init__)
    params = list(sig.parameters.keys())



def test_xblockexpression_is_not_abstract():
    assert not inspect.isabstract(XBlockExpression)


def test_xblockexpression_constructor_exists():
    assert callable(XBlockExpression.__init__)


def test_xblockexpression_constructor_args():
    sig = inspect.signature(XBlockExpression.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstring_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichString)


def test_luniferadoc_richstring_richstring_constructor_exists():
    assert callable(luniferadoc_richstring_RichString.__init__)


def test_luniferadoc_richstring_richstring_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichString.__init__)
    params = list(sig.parameters.keys())



def test_xexpression_is_not_abstract():
    assert not inspect.isabstract(XExpression)


def test_xexpression_constructor_exists():
    assert callable(XExpression.__init__)


def test_xexpression_constructor_args():
    sig = inspect.signature(XExpression.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringmarkup_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringMarkup)


def test_luniferadoc_richstring_richstringmarkup_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringMarkup.__init__)


def test_luniferadoc_richstring_richstringmarkup_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringMarkup.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "styleClass" in params, "Missing parameter 'styleClass'"

def test_luniferadoc_richstring_richstringmarkup_has_id():
    assert hasattr(luniferadoc_richstring_RichStringMarkup, "id")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringMarkup.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_richstring_richstringmarkup_has_styleClass():
    assert hasattr(luniferadoc_richstring_RichStringMarkup, "styleClass")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringMarkup.__mro__:
        if "styleClass" in klass.__dict__:
            descriptor = klass.__dict__["styleClass"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringif_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringIf)


def test_luniferadoc_richstring_richstringif_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringIf.__init__)


def test_luniferadoc_richstring_richstringif_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringIf.__init__)
    params = list(sig.parameters.keys())



def test_document_luniferadoc_ximportdeclaration_is_not_abstract():
    assert not inspect.isabstract(document_luniferadoc_XImportDeclaration)


def test_document_luniferadoc_ximportdeclaration_constructor_exists():
    assert callable(document_luniferadoc_XImportDeclaration.__init__)


def test_document_luniferadoc_ximportdeclaration_constructor_args():
    sig = inspect.signature(document_luniferadoc_XImportDeclaration.__init__)
    params = list(sig.parameters.keys())



def test_richstring_luniferadoc_xexpression_is_not_abstract():
    assert not inspect.isabstract(richstring_luniferadoc_XExpression)


def test_richstring_luniferadoc_xexpression_constructor_exists():
    assert callable(richstring_luniferadoc_XExpression.__init__)


def test_richstring_luniferadoc_xexpression_constructor_args():
    sig = inspect.signature(richstring_luniferadoc_XExpression.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringelseif_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringElseIf)


def test_luniferadoc_richstring_richstringelseif_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringElseIf.__init__)


def test_luniferadoc_richstring_richstringelseif_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringElseIf.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_vaaclipseviewdescription_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_VaaclipseViewDescription)


def test_luniferadoc_document_vaaclipseviewdescription_constructor_exists():
    assert callable(luniferadoc_document_VaaclipseViewDescription.__init__)


def test_luniferadoc_document_vaaclipseviewdescription_constructor_args():
    sig = inspect.signature(luniferadoc_document_VaaclipseViewDescription.__init__)
    params = list(sig.parameters.keys())



def test_vaaclipseviewdescription_is_not_abstract():
    assert not inspect.isabstract(VaaclipseViewDescription)


def test_vaaclipseviewdescription_constructor_exists():
    assert callable(VaaclipseViewDescription.__init__)


def test_vaaclipseviewdescription_constructor_args():
    sig = inspect.signature(VaaclipseViewDescription.__init__)
    params = list(sig.parameters.keys())



def test_document_luniferadoc_documentinclude_is_not_abstract():
    assert not inspect.isabstract(document_luniferadoc_DocumentInclude)


def test_document_luniferadoc_documentinclude_constructor_exists():
    assert callable(document_luniferadoc_DocumentInclude.__init__)


def test_document_luniferadoc_documentinclude_constructor_args():
    sig = inspect.signature(document_luniferadoc_DocumentInclude.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoclayout_is_not_abstract():
    assert not inspect.isabstract(LuniferaDocLayout)


def test_luniferadoclayout_constructor_exists():
    assert callable(LuniferaDocLayout.__init__)


def test_luniferadoclayout_constructor_args():
    sig = inspect.signature(LuniferaDocLayout.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_vaaclipseviewlayout_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_VaaclipseViewLayout)


def test_luniferadoc_document_vaaclipseviewlayout_constructor_exists():
    assert callable(luniferadoc_document_VaaclipseViewLayout.__init__)


def test_luniferadoc_document_vaaclipseviewlayout_constructor_args():
    sig = inspect.signature(luniferadoc_document_VaaclipseViewLayout.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_dtolayout_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_DTOLayout)


def test_luniferadoc_document_dtolayout_constructor_exists():
    assert callable(luniferadoc_document_DTOLayout.__init__)


def test_luniferadoc_document_dtolayout_constructor_args():
    sig = inspect.signature(luniferadoc_document_DTOLayout.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_uilayout_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_UILayout)


def test_luniferadoc_document_uilayout_constructor_exists():
    assert callable(luniferadoc_document_UILayout.__init__)


def test_luniferadoc_document_uilayout_constructor_args():
    sig = inspect.signature(luniferadoc_document_UILayout.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_bpmhumantasklayout_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_BPMHumanTaskLayout)


def test_luniferadoc_document_bpmhumantasklayout_constructor_exists():
    assert callable(luniferadoc_document_BPMHumanTaskLayout.__init__)


def test_luniferadoc_document_bpmhumantasklayout_constructor_args():
    sig = inspect.signature(luniferadoc_document_BPMHumanTaskLayout.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_bpmprocesslayout_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_BPMProcessLayout)


def test_luniferadoc_document_bpmprocesslayout_constructor_exists():
    assert callable(luniferadoc_document_BPMProcessLayout.__init__)


def test_luniferadoc_document_bpmprocesslayout_constructor_args():
    sig = inspect.signature(luniferadoc_document_BPMProcessLayout.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_entitylayout_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_EntityLayout)


def test_luniferadoc_document_entitylayout_constructor_exists():
    assert callable(luniferadoc_document_EntityLayout.__init__)


def test_luniferadoc_document_entitylayout_constructor_args():
    sig = inspect.signature(luniferadoc_document_EntityLayout.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_generaldocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_GeneralDocument)


def test_luniferadoc_document_generaldocument_constructor_exists():
    assert callable(luniferadoc_document_GeneralDocument.__init__)


def test_luniferadoc_document_generaldocument_constructor_args():
    sig = inspect.signature(luniferadoc_document_GeneralDocument.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_uidescription_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_UIDescription)


def test_luniferadoc_document_uidescription_constructor_exists():
    assert callable(luniferadoc_document_UIDescription.__init__)


def test_luniferadoc_document_uidescription_constructor_args():
    sig = inspect.signature(luniferadoc_document_UIDescription.__init__)
    params = list(sig.parameters.keys())



def test_uidescription_is_not_abstract():
    assert not inspect.isabstract(UIDescription)


def test_uidescription_constructor_exists():
    assert callable(UIDescription.__init__)


def test_uidescription_constructor_args():
    sig = inspect.signature(UIDescription.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_bpmprocessdescription_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_BPMProcessDescription)


def test_luniferadoc_document_bpmprocessdescription_constructor_exists():
    assert callable(luniferadoc_document_BPMProcessDescription.__init__)


def test_luniferadoc_document_bpmprocessdescription_constructor_args():
    sig = inspect.signature(luniferadoc_document_BPMProcessDescription.__init__)
    params = list(sig.parameters.keys())



def test_bpmprocessdescription_is_not_abstract():
    assert not inspect.isabstract(BPMProcessDescription)


def test_bpmprocessdescription_constructor_exists():
    assert callable(BPMProcessDescription.__init__)


def test_bpmprocessdescription_constructor_args():
    sig = inspect.signature(BPMProcessDescription.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_dtoproperty_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_DTOProperty)


def test_luniferadoc_document_dtoproperty_constructor_exists():
    assert callable(luniferadoc_document_DTOProperty.__init__)


def test_luniferadoc_document_dtoproperty_constructor_args():
    sig = inspect.signature(luniferadoc_document_DTOProperty.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_luniferadoc_document_dtoproperty_has_name():
    assert hasattr(luniferadoc_document_DTOProperty, "name")
    descriptor = None
    for klass in luniferadoc_document_DTOProperty.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_document_bpmhumantaskdescription_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_BPMHumanTaskDescription)


def test_luniferadoc_document_bpmhumantaskdescription_constructor_exists():
    assert callable(luniferadoc_document_BPMHumanTaskDescription.__init__)


def test_luniferadoc_document_bpmhumantaskdescription_constructor_args():
    sig = inspect.signature(luniferadoc_document_BPMHumanTaskDescription.__init__)
    params = list(sig.parameters.keys())



def test_bpmhumantaskdescription_is_not_abstract():
    assert not inspect.isabstract(BPMHumanTaskDescription)


def test_bpmhumantaskdescription_constructor_exists():
    assert callable(BPMHumanTaskDescription.__init__)


def test_bpmhumantaskdescription_constructor_args():
    sig = inspect.signature(BPMHumanTaskDescription.__init__)
    params = list(sig.parameters.keys())



def test_dtodescription_is_not_abstract():
    assert not inspect.isabstract(DTODescription)


def test_dtodescription_constructor_exists():
    assert callable(DTODescription.__init__)


def test_dtodescription_constructor_args():
    sig = inspect.signature(DTODescription.__init__)
    params = list(sig.parameters.keys())



def test_dtoproperty_is_not_abstract():
    assert not inspect.isabstract(DTOProperty)


def test_dtoproperty_constructor_exists():
    assert callable(DTOProperty.__init__)


def test_dtoproperty_constructor_args():
    sig = inspect.signature(DTOProperty.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_dtoproperties_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_DTOProperties)


def test_luniferadoc_document_dtoproperties_constructor_exists():
    assert callable(luniferadoc_document_DTOProperties.__init__)


def test_luniferadoc_document_dtoproperties_constructor_args():
    sig = inspect.signature(luniferadoc_document_DTOProperties.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_dtodescription_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_DTODescription)


def test_luniferadoc_document_dtodescription_constructor_exists():
    assert callable(luniferadoc_document_DTODescription.__init__)


def test_luniferadoc_document_dtodescription_constructor_args():
    sig = inspect.signature(luniferadoc_document_DTODescription.__init__)
    params = list(sig.parameters.keys())



def test_dtoproperties_is_not_abstract():
    assert not inspect.isabstract(DTOProperties)


def test_dtoproperties_constructor_exists():
    assert callable(DTOProperties.__init__)


def test_dtoproperties_constructor_args():
    sig = inspect.signature(DTOProperties.__init__)
    params = list(sig.parameters.keys())



def test_entityfields_is_not_abstract():
    assert not inspect.isabstract(EntityFields)


def test_entityfields_constructor_exists():
    assert callable(EntityFields.__init__)


def test_entityfields_constructor_args():
    sig = inspect.signature(EntityFields.__init__)
    params = list(sig.parameters.keys())



def test_entitydescription_is_not_abstract():
    assert not inspect.isabstract(EntityDescription)


def test_entitydescription_constructor_exists():
    assert callable(EntityDescription.__init__)


def test_entitydescription_constructor_args():
    sig = inspect.signature(EntityDescription.__init__)
    params = list(sig.parameters.keys())



def test_nameddocument_is_not_abstract():
    assert not inspect.isabstract(NamedDocument)


def test_nameddocument_constructor_exists():
    assert callable(NamedDocument.__init__)


def test_nameddocument_constructor_args():
    sig = inspect.signature(NamedDocument.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_luniferadoclayout_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_LuniferaDocLayout)


def test_luniferadoc_document_luniferadoclayout_constructor_exists():
    assert callable(luniferadoc_document_LuniferaDocLayout.__init__)


def test_luniferadoc_document_luniferadoclayout_constructor_args():
    sig = inspect.signature(luniferadoc_document_LuniferaDocLayout.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_luniferadocdocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_LuniferaDocDocument)


def test_luniferadoc_document_luniferadocdocument_constructor_exists():
    assert callable(luniferadoc_document_LuniferaDocDocument.__init__)


def test_luniferadoc_document_luniferadocdocument_constructor_args():
    sig = inspect.signature(luniferadoc_document_LuniferaDocDocument.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_entityfield_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_EntityField)


def test_luniferadoc_document_entityfield_constructor_exists():
    assert callable(luniferadoc_document_EntityField.__init__)


def test_luniferadoc_document_entityfield_constructor_args():
    sig = inspect.signature(luniferadoc_document_EntityField.__init__)
    params = list(sig.parameters.keys())
    assert "nullable" in params, "Missing parameter 'nullable'"
    assert "pk" in params, "Missing parameter 'pk'"
    assert "type" in params, "Missing parameter 'type'"
    assert "length" in params, "Missing parameter 'length'"
    assert "name" in params, "Missing parameter 'name'"

def test_luniferadoc_document_entityfield_has_nullable():
    assert hasattr(luniferadoc_document_EntityField, "nullable")
    descriptor = None
    for klass in luniferadoc_document_EntityField.__mro__:
        if "nullable" in klass.__dict__:
            descriptor = klass.__dict__["nullable"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_document_entityfield_has_pk():
    assert hasattr(luniferadoc_document_EntityField, "pk")
    descriptor = None
    for klass in luniferadoc_document_EntityField.__mro__:
        if "pk" in klass.__dict__:
            descriptor = klass.__dict__["pk"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_document_entityfield_has_type():
    assert hasattr(luniferadoc_document_EntityField, "type")
    descriptor = None
    for klass in luniferadoc_document_EntityField.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_document_entityfield_has_length():
    assert hasattr(luniferadoc_document_EntityField, "length")
    descriptor = None
    for klass in luniferadoc_document_EntityField.__mro__:
        if "length" in klass.__dict__:
            descriptor = klass.__dict__["length"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_document_entityfield_has_name():
    assert hasattr(luniferadoc_document_EntityField, "name")
    descriptor = None
    for klass in luniferadoc_document_EntityField.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_entityfield_is_not_abstract():
    assert not inspect.isabstract(EntityField)


def test_entityfield_constructor_exists():
    assert callable(EntityField.__init__)


def test_entityfield_constructor_args():
    sig = inspect.signature(EntityField.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_entityfields_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_EntityFields)


def test_luniferadoc_document_entityfields_constructor_exists():
    assert callable(luniferadoc_document_EntityFields.__init__)


def test_luniferadoc_document_entityfields_constructor_args():
    sig = inspect.signature(luniferadoc_document_EntityFields.__init__)
    params = list(sig.parameters.keys())



def test_richstring_is_not_abstract():
    assert not inspect.isabstract(RichString)


def test_richstring_constructor_exists():
    assert callable(RichString.__init__)


def test_richstring_constructor_args():
    sig = inspect.signature(RichString.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_entitydescription_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_EntityDescription)


def test_luniferadoc_document_entitydescription_constructor_exists():
    assert callable(luniferadoc_document_EntityDescription.__init__)


def test_luniferadoc_document_entitydescription_constructor_args():
    sig = inspect.signature(luniferadoc_document_EntityDescription.__init__)
    params = list(sig.parameters.keys())



def test_luniferadocdocument_is_not_abstract():
    assert not inspect.isabstract(LuniferaDocDocument)


def test_luniferadocdocument_constructor_exists():
    assert callable(LuniferaDocDocument.__init__)


def test_luniferadocdocument_constructor_args():
    sig = inspect.signature(LuniferaDocDocument.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_document_bpmprocessdocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_BPMProcessDocument)


def test_luniferadoc_document_bpmprocessdocument_constructor_exists():
    assert callable(luniferadoc_document_BPMProcessDocument.__init__)


def test_luniferadoc_document_bpmprocessdocument_constructor_args():
    sig = inspect.signature(luniferadoc_document_BPMProcessDocument.__init__)
    params = list(sig.parameters.keys())
    assert "process" in params, "Missing parameter 'process'"

def test_luniferadoc_document_bpmprocessdocument_has_process():
    assert hasattr(luniferadoc_document_BPMProcessDocument, "process")
    descriptor = None
    for klass in luniferadoc_document_BPMProcessDocument.__mro__:
        if "process" in klass.__dict__:
            descriptor = klass.__dict__["process"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_document_dtodocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_DTODocument)


def test_luniferadoc_document_dtodocument_constructor_exists():
    assert callable(luniferadoc_document_DTODocument.__init__)


def test_luniferadoc_document_dtodocument_constructor_args():
    sig = inspect.signature(luniferadoc_document_DTODocument.__init__)
    params = list(sig.parameters.keys())
    assert "dtoClass" in params, "Missing parameter 'dtoClass'"

def test_luniferadoc_document_dtodocument_has_dtoClass():
    assert hasattr(luniferadoc_document_DTODocument, "dtoClass")
    descriptor = None
    for klass in luniferadoc_document_DTODocument.__mro__:
        if "dtoClass" in klass.__dict__:
            descriptor = klass.__dict__["dtoClass"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_document_uidocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_UIDocument)


def test_luniferadoc_document_uidocument_constructor_exists():
    assert callable(luniferadoc_document_UIDocument.__init__)


def test_luniferadoc_document_uidocument_constructor_args():
    sig = inspect.signature(luniferadoc_document_UIDocument.__init__)
    params = list(sig.parameters.keys())
    assert "ui" in params, "Missing parameter 'ui'"

def test_luniferadoc_document_uidocument_has_ui():
    assert hasattr(luniferadoc_document_UIDocument, "ui")
    descriptor = None
    for klass in luniferadoc_document_UIDocument.__mro__:
        if "ui" in klass.__dict__:
            descriptor = klass.__dict__["ui"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_document_entitydocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_EntityDocument)


def test_luniferadoc_document_entitydocument_constructor_exists():
    assert callable(luniferadoc_document_EntityDocument.__init__)


def test_luniferadoc_document_entitydocument_constructor_args():
    sig = inspect.signature(luniferadoc_document_EntityDocument.__init__)
    params = list(sig.parameters.keys())
    assert "entityClass" in params, "Missing parameter 'entityClass'"

def test_luniferadoc_document_entitydocument_has_entityClass():
    assert hasattr(luniferadoc_document_EntityDocument, "entityClass")
    descriptor = None
    for klass in luniferadoc_document_EntityDocument.__mro__:
        if "entityClass" in klass.__dict__:
            descriptor = klass.__dict__["entityClass"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_document_bpmhumantaskdocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_BPMHumanTaskDocument)


def test_luniferadoc_document_bpmhumantaskdocument_constructor_exists():
    assert callable(luniferadoc_document_BPMHumanTaskDocument.__init__)


def test_luniferadoc_document_bpmhumantaskdocument_constructor_args():
    sig = inspect.signature(luniferadoc_document_BPMHumanTaskDocument.__init__)
    params = list(sig.parameters.keys())
    assert "task" in params, "Missing parameter 'task'"

def test_luniferadoc_document_bpmhumantaskdocument_has_task():
    assert hasattr(luniferadoc_document_BPMHumanTaskDocument, "task")
    descriptor = None
    for klass in luniferadoc_document_BPMHumanTaskDocument.__mro__:
        if "task" in klass.__dict__:
            descriptor = klass.__dict__["task"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_document_vaaclipseviewdocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_document_VaaclipseViewDocument)


def test_luniferadoc_document_vaaclipseviewdocument_constructor_exists():
    assert callable(luniferadoc_document_VaaclipseViewDocument.__init__)


def test_luniferadoc_document_vaaclipseviewdocument_constructor_args():
    sig = inspect.signature(luniferadoc_document_VaaclipseViewDocument.__init__)
    params = list(sig.parameters.keys())
    assert "view" in params, "Missing parameter 'view'"

def test_luniferadoc_document_vaaclipseviewdocument_has_view():
    assert hasattr(luniferadoc_document_VaaclipseViewDocument, "view")
    descriptor = None
    for klass in luniferadoc_document_VaaclipseViewDocument.__mro__:
        if "view" in klass.__dict__:
            descriptor = klass.__dict__["view"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_documentinclude_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_DocumentInclude)


def test_luniferadoc_documentinclude_constructor_exists():
    assert callable(luniferadoc_DocumentInclude.__init__)


def test_luniferadoc_documentinclude_constructor_args():
    sig = inspect.signature(luniferadoc_DocumentInclude.__init__)
    params = list(sig.parameters.keys())
    assert "varName" in params, "Missing parameter 'varName'"

def test_luniferadoc_documentinclude_has_varName():
    assert hasattr(luniferadoc_DocumentInclude, "varName")
    descriptor = None
    for klass in luniferadoc_DocumentInclude.__mro__:
        if "varName" in klass.__dict__:
            descriptor = klass.__dict__["varName"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_nameddocument_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_NamedDocument)


def test_luniferadoc_nameddocument_constructor_exists():
    assert callable(luniferadoc_NamedDocument.__init__)


def test_luniferadoc_nameddocument_constructor_args():
    sig = inspect.signature(luniferadoc_NamedDocument.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_luniferadoc_nameddocument_has_name():
    assert hasattr(luniferadoc_NamedDocument, "name")
    descriptor = None
    for klass in luniferadoc_NamedDocument.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringentityref_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringEntityRef)


def test_luniferadoc_richstring_richstringentityref_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringEntityRef.__init__)


def test_luniferadoc_richstring_richstringentityref_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringEntityRef.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringstartprocess_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringStartProcess)


def test_luniferadoc_richstring_richstringstartprocess_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringStartProcess.__init__)


def test_luniferadoc_richstring_richstringstartprocess_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringStartProcess.__init__)
    params = list(sig.parameters.keys())
    assert "processId" in params, "Missing parameter 'processId'"

def test_luniferadoc_richstring_richstringstartprocess_has_processId():
    assert hasattr(luniferadoc_richstring_RichStringStartProcess, "processId")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringStartProcess.__mro__:
        if "processId" in klass.__dict__:
            descriptor = klass.__dict__["processId"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringopenview_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringOpenView)


def test_luniferadoc_richstring_richstringopenview_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringOpenView.__init__)


def test_luniferadoc_richstring_richstringopenview_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringOpenView.__init__)
    params = list(sig.parameters.keys())
    assert "viewId" in params, "Missing parameter 'viewId'"

def test_luniferadoc_richstring_richstringopenview_has_viewId():
    assert hasattr(luniferadoc_richstring_RichStringOpenView, "viewId")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringOpenView.__mro__:
        if "viewId" in klass.__dict__:
            descriptor = klass.__dict__["viewId"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringtabledata_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringTableData)


def test_luniferadoc_richstring_richstringtabledata_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringTableData.__init__)


def test_luniferadoc_richstring_richstringtabledata_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringTableData.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringcode_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringCode)


def test_luniferadoc_richstring_richstringcode_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringCode.__init__)


def test_luniferadoc_richstring_richstringcode_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringCode.__init__)
    params = list(sig.parameters.keys())
    assert "lang" in params, "Missing parameter 'lang'"

def test_luniferadoc_richstring_richstringcode_has_lang():
    assert hasattr(luniferadoc_richstring_RichStringCode, "lang")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringCode.__mro__:
        if "lang" in klass.__dict__:
            descriptor = klass.__dict__["lang"]
            break
    assert isinstance(descriptor, property)



def test_luniferadoc_richstring_richstringmovie_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringMovie)


def test_luniferadoc_richstring_richstringmovie_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringMovie.__init__)


def test_luniferadoc_richstring_richstringmovie_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringMovie.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "type" in params, "Missing parameter 'type'"
    assert "src" in params, "Missing parameter 'src'"
    assert "height" in params, "Missing parameter 'height'"

def test_luniferadoc_richstring_richstringmovie_has_width():
    assert hasattr(luniferadoc_richstring_RichStringMovie, "width")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringMovie.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_richstring_richstringmovie_has_type():
    assert hasattr(luniferadoc_richstring_RichStringMovie, "type")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringMovie.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_richstring_richstringmovie_has_src():
    assert hasattr(luniferadoc_richstring_RichStringMovie, "src")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringMovie.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_richstring_richstringmovie_has_height():
    assert hasattr(luniferadoc_richstring_RichStringMovie, "height")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringMovie.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)



def test_richstringtablerow_is_not_abstract():
    assert not inspect.isabstract(RichStringTableRow)


def test_richstringtablerow_constructor_exists():
    assert callable(RichStringTableRow.__init__)


def test_richstringtablerow_constructor_args():
    sig = inspect.signature(RichStringTableRow.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringtable_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringTable)


def test_luniferadoc_richstring_richstringtable_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringTable.__init__)


def test_luniferadoc_richstring_richstringtable_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringTable.__init__)
    params = list(sig.parameters.keys())



def test_luniferadoc_richstring_richstringimg_is_not_abstract():
    assert not inspect.isabstract(luniferadoc_richstring_RichStringImg)


def test_luniferadoc_richstring_richstringimg_constructor_exists():
    assert callable(luniferadoc_richstring_RichStringImg.__init__)


def test_luniferadoc_richstring_richstringimg_constructor_args():
    sig = inspect.signature(luniferadoc_richstring_RichStringImg.__init__)
    params = list(sig.parameters.keys())
    assert "width" in params, "Missing parameter 'width'"
    assert "alt" in params, "Missing parameter 'alt'"
    assert "height" in params, "Missing parameter 'height'"
    assert "src" in params, "Missing parameter 'src'"

def test_luniferadoc_richstring_richstringimg_has_width():
    assert hasattr(luniferadoc_richstring_RichStringImg, "width")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringImg.__mro__:
        if "width" in klass.__dict__:
            descriptor = klass.__dict__["width"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_richstring_richstringimg_has_alt():
    assert hasattr(luniferadoc_richstring_RichStringImg, "alt")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringImg.__mro__:
        if "alt" in klass.__dict__:
            descriptor = klass.__dict__["alt"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_richstring_richstringimg_has_height():
    assert hasattr(luniferadoc_richstring_RichStringImg, "height")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringImg.__mro__:
        if "height" in klass.__dict__:
            descriptor = klass.__dict__["height"]
            break
    assert isinstance(descriptor, property)

def test_luniferadoc_richstring_richstringimg_has_src():
    assert hasattr(luniferadoc_richstring_RichStringImg, "src")
    descriptor = None
    for klass in luniferadoc_richstring_RichStringImg.__mro__:
        if "src" in klass.__dict__:
            descriptor = klass.__dict__["src"]
            break
    assert isinstance(descriptor, property)

def test_doctype_exists():
    # Check that the Enumeration exists
    assert DocType is not None

def test_doctype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in DocType]
    expected_literals = [
        "BPM_TASK",
        "VAACLIPSE_VIEW",
        "BPM_PROCESS",
        "DTO",
        "ENTITY",
        "UI",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in DocType"


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
RichStringListElement_strategy = st.builds(
    RichStringListElement,
)
BPMProcessDocument_strategy = st.builds(
    BPMProcessDocument,
)
DTODocument_strategy = st.builds(
    DTODocument,
)
EntityDocument_strategy = st.builds(
    EntityDocument,
)
UIDocument_strategy = st.builds(
    UIDocument,
)
VaaclipseViewDocument_strategy = st.builds(
    VaaclipseViewDocument,
)
BPMHumanTaskDocument_strategy = st.builds(
    BPMHumanTaskDocument,
)
RichStringTableData_strategy = st.builds(
    RichStringTableData,
)
RichStringElseIf_strategy = st.builds(
    RichStringElseIf,
)
RichStringMarkup_strategy = st.builds(
    RichStringMarkup,
)
luniferadoc_richstring_RichStringH1_strategy = st.builds(
    luniferadoc_richstring_RichStringH1,
)
luniferadoc_richstring_RichStringH6_strategy = st.builds(
    luniferadoc_richstring_RichStringH6,
)
luniferadoc_richstring_RichStringOrderedList_strategy = st.builds(
    luniferadoc_richstring_RichStringOrderedList,
)
luniferadoc_richstring_RichStringH5_strategy = st.builds(
    luniferadoc_richstring_RichStringH5,
)
luniferadoc_richstring_RichStringItalic_strategy = st.builds(
    luniferadoc_richstring_RichStringItalic,
)
luniferadoc_richstring_RichStringTableRow_strategy = st.builds(
    luniferadoc_richstring_RichStringTableRow,
)
luniferadoc_richstring_RichStringSection_strategy = st.builds(
    luniferadoc_richstring_RichStringSection,
    name=
        safe_text
)
luniferadoc_richstring_RichStringDTORef_strategy = st.builds(
    luniferadoc_richstring_RichStringDTORef,
)
luniferadoc_richstring_RichStringSkype_strategy = st.builds(
    luniferadoc_richstring_RichStringSkype,
    target=
        safe_text
)
luniferadoc_richstring_RichStringH2_strategy = st.builds(
    luniferadoc_richstring_RichStringH2,
)
luniferadoc_richstring_RichStringSubsection_strategy = st.builds(
    luniferadoc_richstring_RichStringSubsection,
    name=
        safe_text
)
luniferadoc_richstring_RichStringListElement_strategy = st.builds(
    luniferadoc_richstring_RichStringListElement,
)
luniferadoc_richstring_RichStringBold_strategy = st.builds(
    luniferadoc_richstring_RichStringBold,
)
luniferadoc_richstring_RichStringUIRef_strategy = st.builds(
    luniferadoc_richstring_RichStringUIRef,
)
luniferadoc_richstring_RichStringH3_strategy = st.builds(
    luniferadoc_richstring_RichStringH3,
)
luniferadoc_richstring_RichStringTaskRef_strategy = st.builds(
    luniferadoc_richstring_RichStringTaskRef,
)
luniferadoc_richstring_RichStringChapter_strategy = st.builds(
    luniferadoc_richstring_RichStringChapter,
    name=
        safe_text
)
luniferadoc_richstring_RichStringH4_strategy = st.builds(
    luniferadoc_richstring_RichStringH4,
)
luniferadoc_richstring_RichStringUnderline_strategy = st.builds(
    luniferadoc_richstring_RichStringUnderline,
)
luniferadoc_richstring_RichStringMailto_strategy = st.builds(
    luniferadoc_richstring_RichStringMailto,
    email=
        safe_text
)
luniferadoc_richstring_RichStringURL_strategy = st.builds(
    luniferadoc_richstring_RichStringURL,
    location=
        safe_text
)
luniferadoc_richstring_RichStringRef_strategy = st.builds(
    luniferadoc_richstring_RichStringRef,
    refId=
        safe_text
)
luniferadoc_richstring_RichStringList_strategy = st.builds(
    luniferadoc_richstring_RichStringList,
)
luniferadoc_richstring_RichStringProcessRef_strategy = st.builds(
    luniferadoc_richstring_RichStringProcessRef,
)
luniferadoc_richstring_RichStringSpan_strategy = st.builds(
    luniferadoc_richstring_RichStringSpan,
)
luniferadoc_richstring_RichStringViewRef_strategy = st.builds(
    luniferadoc_richstring_RichStringViewRef,
)
luniferadoc_richstring_RichStringExample_strategy = st.builds(
    luniferadoc_richstring_RichStringExample,
)
XForLoopExpression_strategy = st.builds(
    XForLoopExpression,
)
luniferadoc_richstring_RichStringForLoop_strategy = st.builds(
    luniferadoc_richstring_RichStringForLoop,
)
XStringLiteral_strategy = st.builds(
    XStringLiteral,
)
luniferadoc_richstring_RichStringLiteral_strategy = st.builds(
    luniferadoc_richstring_RichStringLiteral,
)
XBlockExpression_strategy = st.builds(
    XBlockExpression,
)
luniferadoc_richstring_RichString_strategy = st.builds(
    luniferadoc_richstring_RichString,
)
XExpression_strategy = st.builds(
    XExpression,
)
luniferadoc_richstring_RichStringMarkup_strategy = st.builds(
    luniferadoc_richstring_RichStringMarkup,
    id=
        safe_text,
    styleClass=
        safe_text
)
luniferadoc_richstring_RichStringIf_strategy = st.builds(
    luniferadoc_richstring_RichStringIf,
)
document_luniferadoc_XImportDeclaration_strategy = st.builds(
    document_luniferadoc_XImportDeclaration,
)
richstring_luniferadoc_XExpression_strategy = st.builds(
    richstring_luniferadoc_XExpression,
)
luniferadoc_richstring_RichStringElseIf_strategy = st.builds(
    luniferadoc_richstring_RichStringElseIf,
)
luniferadoc_document_VaaclipseViewDescription_strategy = st.builds(
    luniferadoc_document_VaaclipseViewDescription,
)
VaaclipseViewDescription_strategy = st.builds(
    VaaclipseViewDescription,
)
document_luniferadoc_DocumentInclude_strategy = st.builds(
    document_luniferadoc_DocumentInclude,
)
LuniferaDocLayout_strategy = st.builds(
    LuniferaDocLayout,
)
luniferadoc_document_VaaclipseViewLayout_strategy = st.builds(
    luniferadoc_document_VaaclipseViewLayout,
)
luniferadoc_document_DTOLayout_strategy = st.builds(
    luniferadoc_document_DTOLayout,
)
luniferadoc_document_UILayout_strategy = st.builds(
    luniferadoc_document_UILayout,
)
luniferadoc_document_BPMHumanTaskLayout_strategy = st.builds(
    luniferadoc_document_BPMHumanTaskLayout,
)
luniferadoc_document_BPMProcessLayout_strategy = st.builds(
    luniferadoc_document_BPMProcessLayout,
)
luniferadoc_document_EntityLayout_strategy = st.builds(
    luniferadoc_document_EntityLayout,
)
luniferadoc_document_GeneralDocument_strategy = st.builds(
    luniferadoc_document_GeneralDocument,
)
luniferadoc_document_UIDescription_strategy = st.builds(
    luniferadoc_document_UIDescription,
)
UIDescription_strategy = st.builds(
    UIDescription,
)
luniferadoc_document_BPMProcessDescription_strategy = st.builds(
    luniferadoc_document_BPMProcessDescription,
)
BPMProcessDescription_strategy = st.builds(
    BPMProcessDescription,
)
luniferadoc_document_DTOProperty_strategy = st.builds(
    luniferadoc_document_DTOProperty,
    name=
        safe_text
)
luniferadoc_document_BPMHumanTaskDescription_strategy = st.builds(
    luniferadoc_document_BPMHumanTaskDescription,
)
BPMHumanTaskDescription_strategy = st.builds(
    BPMHumanTaskDescription,
)
DTODescription_strategy = st.builds(
    DTODescription,
)
DTOProperty_strategy = st.builds(
    DTOProperty,
)
luniferadoc_document_DTOProperties_strategy = st.builds(
    luniferadoc_document_DTOProperties,
)
luniferadoc_document_DTODescription_strategy = st.builds(
    luniferadoc_document_DTODescription,
)
DTOProperties_strategy = st.builds(
    DTOProperties,
)
EntityFields_strategy = st.builds(
    EntityFields,
)
EntityDescription_strategy = st.builds(
    EntityDescription,
)
NamedDocument_strategy = st.builds(
    NamedDocument,
)
luniferadoc_document_LuniferaDocLayout_strategy = st.builds(
    luniferadoc_document_LuniferaDocLayout,
)
luniferadoc_document_LuniferaDocDocument_strategy = st.builds(
    luniferadoc_document_LuniferaDocDocument,
)
luniferadoc_document_EntityField_strategy = st.builds(
    luniferadoc_document_EntityField,
    nullable=
        st.booleans(),
    pk=
        st.booleans(),
    type=
        safe_text,
    length=
        st.integers(),
    name=
        safe_text
)
EntityField_strategy = st.builds(
    EntityField,
)
luniferadoc_document_EntityFields_strategy = st.builds(
    luniferadoc_document_EntityFields,
)
RichString_strategy = st.builds(
    RichString,
)
luniferadoc_document_EntityDescription_strategy = st.builds(
    luniferadoc_document_EntityDescription,
)
LuniferaDocDocument_strategy = st.builds(
    LuniferaDocDocument,
)
luniferadoc_document_BPMProcessDocument_strategy = st.builds(
    luniferadoc_document_BPMProcessDocument,
    process=
        safe_text
)
luniferadoc_document_DTODocument_strategy = st.builds(
    luniferadoc_document_DTODocument,
    dtoClass=
        safe_text
)
luniferadoc_document_UIDocument_strategy = st.builds(
    luniferadoc_document_UIDocument,
    ui=
        safe_text
)
luniferadoc_document_EntityDocument_strategy = st.builds(
    luniferadoc_document_EntityDocument,
    entityClass=
        safe_text
)
luniferadoc_document_BPMHumanTaskDocument_strategy = st.builds(
    luniferadoc_document_BPMHumanTaskDocument,
    task=
        safe_text
)
luniferadoc_document_VaaclipseViewDocument_strategy = st.builds(
    luniferadoc_document_VaaclipseViewDocument,
    view=
        safe_text
)
luniferadoc_DocumentInclude_strategy = st.builds(
    luniferadoc_DocumentInclude,
    varName=
        safe_text
)
luniferadoc_NamedDocument_strategy = st.builds(
    luniferadoc_NamedDocument,
    name=
        safe_text
)
luniferadoc_richstring_RichStringEntityRef_strategy = st.builds(
    luniferadoc_richstring_RichStringEntityRef,
)
luniferadoc_richstring_RichStringStartProcess_strategy = st.builds(
    luniferadoc_richstring_RichStringStartProcess,
    processId=
        safe_text
)
luniferadoc_richstring_RichStringOpenView_strategy = st.builds(
    luniferadoc_richstring_RichStringOpenView,
    viewId=
        safe_text
)
luniferadoc_richstring_RichStringTableData_strategy = st.builds(
    luniferadoc_richstring_RichStringTableData,
)
luniferadoc_richstring_RichStringCode_strategy = st.builds(
    luniferadoc_richstring_RichStringCode,
    lang=
        safe_text
)
luniferadoc_richstring_RichStringMovie_strategy = st.builds(
    luniferadoc_richstring_RichStringMovie,
    width=
        safe_text,
    type=
        safe_text,
    src=
        safe_text,
    height=
        safe_text
)
RichStringTableRow_strategy = st.builds(
    RichStringTableRow,
)
luniferadoc_richstring_RichStringTable_strategy = st.builds(
    luniferadoc_richstring_RichStringTable,
)
luniferadoc_richstring_RichStringImg_strategy = st.builds(
    luniferadoc_richstring_RichStringImg,
    width=
        safe_text,
    alt=
        safe_text,
    height=
        safe_text,
    src=
        safe_text
)

@given(instance=RichStringListElement_strategy)
@settings(max_examples=50)
def test_richstringlistelement_instantiation(instance):
    assert isinstance(instance, RichStringListElement)

@given(instance=BPMProcessDocument_strategy)
@settings(max_examples=50)
def test_bpmprocessdocument_instantiation(instance):
    assert isinstance(instance, BPMProcessDocument)

@given(instance=DTODocument_strategy)
@settings(max_examples=50)
def test_dtodocument_instantiation(instance):
    assert isinstance(instance, DTODocument)

@given(instance=EntityDocument_strategy)
@settings(max_examples=50)
def test_entitydocument_instantiation(instance):
    assert isinstance(instance, EntityDocument)

@given(instance=UIDocument_strategy)
@settings(max_examples=50)
def test_uidocument_instantiation(instance):
    assert isinstance(instance, UIDocument)

@given(instance=VaaclipseViewDocument_strategy)
@settings(max_examples=50)
def test_vaaclipseviewdocument_instantiation(instance):
    assert isinstance(instance, VaaclipseViewDocument)

@given(instance=BPMHumanTaskDocument_strategy)
@settings(max_examples=50)
def test_bpmhumantaskdocument_instantiation(instance):
    assert isinstance(instance, BPMHumanTaskDocument)

@given(instance=RichStringTableData_strategy)
@settings(max_examples=50)
def test_richstringtabledata_instantiation(instance):
    assert isinstance(instance, RichStringTableData)

@given(instance=RichStringElseIf_strategy)
@settings(max_examples=50)
def test_richstringelseif_instantiation(instance):
    assert isinstance(instance, RichStringElseIf)

@given(instance=RichStringMarkup_strategy)
@settings(max_examples=50)
def test_richstringmarkup_instantiation(instance):
    assert isinstance(instance, RichStringMarkup)

@given(instance=luniferadoc_richstring_RichStringH1_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringh1_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringH1)

@given(instance=luniferadoc_richstring_RichStringH6_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringh6_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringH6)

@given(instance=luniferadoc_richstring_RichStringOrderedList_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringorderedlist_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringOrderedList)

@given(instance=luniferadoc_richstring_RichStringH5_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringh5_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringH5)

@given(instance=luniferadoc_richstring_RichStringItalic_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringitalic_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringItalic)

@given(instance=luniferadoc_richstring_RichStringTableRow_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringtablerow_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringTableRow)

@given(instance=luniferadoc_richstring_RichStringSection_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringsection_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringSection)



@given(instance=luniferadoc_richstring_RichStringSection_strategy)
def test_luniferadoc_richstring_richstringsection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=luniferadoc_richstring_RichStringDTORef_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringdtoref_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringDTORef)

@given(instance=luniferadoc_richstring_RichStringSkype_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringskype_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringSkype)



@given(instance=luniferadoc_richstring_RichStringSkype_strategy)
def test_luniferadoc_richstring_richstringskype_target_setter(instance):
    original = instance.target
    instance.target = original
    assert instance.target == original

@given(instance=luniferadoc_richstring_RichStringH2_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringh2_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringH2)

@given(instance=luniferadoc_richstring_RichStringSubsection_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringsubsection_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringSubsection)



@given(instance=luniferadoc_richstring_RichStringSubsection_strategy)
def test_luniferadoc_richstring_richstringsubsection_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=luniferadoc_richstring_RichStringListElement_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringlistelement_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringListElement)

@given(instance=luniferadoc_richstring_RichStringBold_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringbold_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringBold)

@given(instance=luniferadoc_richstring_RichStringUIRef_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringuiref_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringUIRef)

@given(instance=luniferadoc_richstring_RichStringH3_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringh3_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringH3)

@given(instance=luniferadoc_richstring_RichStringTaskRef_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringtaskref_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringTaskRef)

@given(instance=luniferadoc_richstring_RichStringChapter_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringchapter_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringChapter)



@given(instance=luniferadoc_richstring_RichStringChapter_strategy)
def test_luniferadoc_richstring_richstringchapter_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=luniferadoc_richstring_RichStringH4_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringh4_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringH4)

@given(instance=luniferadoc_richstring_RichStringUnderline_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringunderline_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringUnderline)

@given(instance=luniferadoc_richstring_RichStringMailto_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringmailto_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringMailto)



@given(instance=luniferadoc_richstring_RichStringMailto_strategy)
def test_luniferadoc_richstring_richstringmailto_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=luniferadoc_richstring_RichStringURL_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringurl_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringURL)



@given(instance=luniferadoc_richstring_RichStringURL_strategy)
def test_luniferadoc_richstring_richstringurl_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=luniferadoc_richstring_RichStringRef_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringref_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringRef)



@given(instance=luniferadoc_richstring_RichStringRef_strategy)
def test_luniferadoc_richstring_richstringref_refId_setter(instance):
    original = instance.refId
    instance.refId = original
    assert instance.refId == original

@given(instance=luniferadoc_richstring_RichStringList_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringlist_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringList)

@given(instance=luniferadoc_richstring_RichStringProcessRef_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringprocessref_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringProcessRef)

@given(instance=luniferadoc_richstring_RichStringSpan_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringspan_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringSpan)

@given(instance=luniferadoc_richstring_RichStringViewRef_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringviewref_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringViewRef)

@given(instance=luniferadoc_richstring_RichStringExample_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringexample_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringExample)

@given(instance=XForLoopExpression_strategy)
@settings(max_examples=50)
def test_xforloopexpression_instantiation(instance):
    assert isinstance(instance, XForLoopExpression)

@given(instance=luniferadoc_richstring_RichStringForLoop_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringforloop_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringForLoop)

@given(instance=XStringLiteral_strategy)
@settings(max_examples=50)
def test_xstringliteral_instantiation(instance):
    assert isinstance(instance, XStringLiteral)

@given(instance=luniferadoc_richstring_RichStringLiteral_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringliteral_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringLiteral)

@given(instance=XBlockExpression_strategy)
@settings(max_examples=50)
def test_xblockexpression_instantiation(instance):
    assert isinstance(instance, XBlockExpression)

@given(instance=luniferadoc_richstring_RichString_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstring_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichString)

@given(instance=XExpression_strategy)
@settings(max_examples=50)
def test_xexpression_instantiation(instance):
    assert isinstance(instance, XExpression)

@given(instance=luniferadoc_richstring_RichStringMarkup_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringmarkup_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringMarkup)



@given(instance=luniferadoc_richstring_RichStringMarkup_strategy)
def test_luniferadoc_richstring_richstringmarkup_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=luniferadoc_richstring_RichStringMarkup_strategy)
def test_luniferadoc_richstring_richstringmarkup_styleClass_setter(instance):
    original = instance.styleClass
    instance.styleClass = original
    assert instance.styleClass == original

@given(instance=luniferadoc_richstring_RichStringIf_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringif_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringIf)

@given(instance=document_luniferadoc_XImportDeclaration_strategy)
@settings(max_examples=50)
def test_document_luniferadoc_ximportdeclaration_instantiation(instance):
    assert isinstance(instance, document_luniferadoc_XImportDeclaration)

@given(instance=richstring_luniferadoc_XExpression_strategy)
@settings(max_examples=50)
def test_richstring_luniferadoc_xexpression_instantiation(instance):
    assert isinstance(instance, richstring_luniferadoc_XExpression)

@given(instance=luniferadoc_richstring_RichStringElseIf_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringelseif_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringElseIf)

@given(instance=luniferadoc_document_VaaclipseViewDescription_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_vaaclipseviewdescription_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_VaaclipseViewDescription)

@given(instance=VaaclipseViewDescription_strategy)
@settings(max_examples=50)
def test_vaaclipseviewdescription_instantiation(instance):
    assert isinstance(instance, VaaclipseViewDescription)

@given(instance=document_luniferadoc_DocumentInclude_strategy)
@settings(max_examples=50)
def test_document_luniferadoc_documentinclude_instantiation(instance):
    assert isinstance(instance, document_luniferadoc_DocumentInclude)

@given(instance=LuniferaDocLayout_strategy)
@settings(max_examples=50)
def test_luniferadoclayout_instantiation(instance):
    assert isinstance(instance, LuniferaDocLayout)

@given(instance=luniferadoc_document_VaaclipseViewLayout_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_vaaclipseviewlayout_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_VaaclipseViewLayout)

@given(instance=luniferadoc_document_DTOLayout_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_dtolayout_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_DTOLayout)

@given(instance=luniferadoc_document_UILayout_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_uilayout_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_UILayout)

@given(instance=luniferadoc_document_BPMHumanTaskLayout_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_bpmhumantasklayout_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_BPMHumanTaskLayout)

@given(instance=luniferadoc_document_BPMProcessLayout_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_bpmprocesslayout_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_BPMProcessLayout)

@given(instance=luniferadoc_document_EntityLayout_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_entitylayout_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_EntityLayout)

@given(instance=luniferadoc_document_GeneralDocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_generaldocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_GeneralDocument)

@given(instance=luniferadoc_document_UIDescription_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_uidescription_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_UIDescription)

@given(instance=UIDescription_strategy)
@settings(max_examples=50)
def test_uidescription_instantiation(instance):
    assert isinstance(instance, UIDescription)

@given(instance=luniferadoc_document_BPMProcessDescription_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_bpmprocessdescription_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_BPMProcessDescription)

@given(instance=BPMProcessDescription_strategy)
@settings(max_examples=50)
def test_bpmprocessdescription_instantiation(instance):
    assert isinstance(instance, BPMProcessDescription)

@given(instance=luniferadoc_document_DTOProperty_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_dtoproperty_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_DTOProperty)



@given(instance=luniferadoc_document_DTOProperty_strategy)
def test_luniferadoc_document_dtoproperty_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=luniferadoc_document_BPMHumanTaskDescription_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_bpmhumantaskdescription_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_BPMHumanTaskDescription)

@given(instance=BPMHumanTaskDescription_strategy)
@settings(max_examples=50)
def test_bpmhumantaskdescription_instantiation(instance):
    assert isinstance(instance, BPMHumanTaskDescription)

@given(instance=DTODescription_strategy)
@settings(max_examples=50)
def test_dtodescription_instantiation(instance):
    assert isinstance(instance, DTODescription)

@given(instance=DTOProperty_strategy)
@settings(max_examples=50)
def test_dtoproperty_instantiation(instance):
    assert isinstance(instance, DTOProperty)

@given(instance=luniferadoc_document_DTOProperties_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_dtoproperties_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_DTOProperties)

@given(instance=luniferadoc_document_DTODescription_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_dtodescription_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_DTODescription)

@given(instance=DTOProperties_strategy)
@settings(max_examples=50)
def test_dtoproperties_instantiation(instance):
    assert isinstance(instance, DTOProperties)

@given(instance=EntityFields_strategy)
@settings(max_examples=50)
def test_entityfields_instantiation(instance):
    assert isinstance(instance, EntityFields)

@given(instance=EntityDescription_strategy)
@settings(max_examples=50)
def test_entitydescription_instantiation(instance):
    assert isinstance(instance, EntityDescription)

@given(instance=NamedDocument_strategy)
@settings(max_examples=50)
def test_nameddocument_instantiation(instance):
    assert isinstance(instance, NamedDocument)

@given(instance=luniferadoc_document_LuniferaDocLayout_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_luniferadoclayout_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_LuniferaDocLayout)

@given(instance=luniferadoc_document_LuniferaDocDocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_luniferadocdocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_LuniferaDocDocument)

@given(instance=luniferadoc_document_EntityField_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_entityfield_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_EntityField)



@given(instance=luniferadoc_document_EntityField_strategy)
def test_luniferadoc_document_entityfield_nullable_setter(instance):
    original = instance.nullable
    instance.nullable = original
    assert instance.nullable == original



@given(instance=luniferadoc_document_EntityField_strategy)
def test_luniferadoc_document_entityfield_pk_setter(instance):
    original = instance.pk
    instance.pk = original
    assert instance.pk == original



@given(instance=luniferadoc_document_EntityField_strategy)
def test_luniferadoc_document_entityfield_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=luniferadoc_document_EntityField_strategy)
def test_luniferadoc_document_entityfield_length_setter(instance):
    original = instance.length
    instance.length = original
    assert instance.length == original



@given(instance=luniferadoc_document_EntityField_strategy)
def test_luniferadoc_document_entityfield_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=EntityField_strategy)
@settings(max_examples=50)
def test_entityfield_instantiation(instance):
    assert isinstance(instance, EntityField)

@given(instance=luniferadoc_document_EntityFields_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_entityfields_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_EntityFields)

@given(instance=RichString_strategy)
@settings(max_examples=50)
def test_richstring_instantiation(instance):
    assert isinstance(instance, RichString)

@given(instance=luniferadoc_document_EntityDescription_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_entitydescription_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_EntityDescription)

@given(instance=LuniferaDocDocument_strategy)
@settings(max_examples=50)
def test_luniferadocdocument_instantiation(instance):
    assert isinstance(instance, LuniferaDocDocument)

@given(instance=luniferadoc_document_BPMProcessDocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_bpmprocessdocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_BPMProcessDocument)



@given(instance=luniferadoc_document_BPMProcessDocument_strategy)
def test_luniferadoc_document_bpmprocessdocument_process_setter(instance):
    original = instance.process
    instance.process = original
    assert instance.process == original

@given(instance=luniferadoc_document_DTODocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_dtodocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_DTODocument)



@given(instance=luniferadoc_document_DTODocument_strategy)
def test_luniferadoc_document_dtodocument_dtoClass_setter(instance):
    original = instance.dtoClass
    instance.dtoClass = original
    assert instance.dtoClass == original

@given(instance=luniferadoc_document_UIDocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_uidocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_UIDocument)



@given(instance=luniferadoc_document_UIDocument_strategy)
def test_luniferadoc_document_uidocument_ui_setter(instance):
    original = instance.ui
    instance.ui = original
    assert instance.ui == original

@given(instance=luniferadoc_document_EntityDocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_entitydocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_EntityDocument)



@given(instance=luniferadoc_document_EntityDocument_strategy)
def test_luniferadoc_document_entitydocument_entityClass_setter(instance):
    original = instance.entityClass
    instance.entityClass = original
    assert instance.entityClass == original

@given(instance=luniferadoc_document_BPMHumanTaskDocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_bpmhumantaskdocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_BPMHumanTaskDocument)



@given(instance=luniferadoc_document_BPMHumanTaskDocument_strategy)
def test_luniferadoc_document_bpmhumantaskdocument_task_setter(instance):
    original = instance.task
    instance.task = original
    assert instance.task == original

@given(instance=luniferadoc_document_VaaclipseViewDocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_document_vaaclipseviewdocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_document_VaaclipseViewDocument)



@given(instance=luniferadoc_document_VaaclipseViewDocument_strategy)
def test_luniferadoc_document_vaaclipseviewdocument_view_setter(instance):
    original = instance.view
    instance.view = original
    assert instance.view == original

@given(instance=luniferadoc_DocumentInclude_strategy)
@settings(max_examples=50)
def test_luniferadoc_documentinclude_instantiation(instance):
    assert isinstance(instance, luniferadoc_DocumentInclude)



@given(instance=luniferadoc_DocumentInclude_strategy)
def test_luniferadoc_documentinclude_varName_setter(instance):
    original = instance.varName
    instance.varName = original
    assert instance.varName == original

@given(instance=luniferadoc_NamedDocument_strategy)
@settings(max_examples=50)
def test_luniferadoc_nameddocument_instantiation(instance):
    assert isinstance(instance, luniferadoc_NamedDocument)



@given(instance=luniferadoc_NamedDocument_strategy)
def test_luniferadoc_nameddocument_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=luniferadoc_richstring_RichStringEntityRef_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringentityref_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringEntityRef)

@given(instance=luniferadoc_richstring_RichStringStartProcess_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringstartprocess_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringStartProcess)



@given(instance=luniferadoc_richstring_RichStringStartProcess_strategy)
def test_luniferadoc_richstring_richstringstartprocess_processId_setter(instance):
    original = instance.processId
    instance.processId = original
    assert instance.processId == original

@given(instance=luniferadoc_richstring_RichStringOpenView_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringopenview_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringOpenView)



@given(instance=luniferadoc_richstring_RichStringOpenView_strategy)
def test_luniferadoc_richstring_richstringopenview_viewId_setter(instance):
    original = instance.viewId
    instance.viewId = original
    assert instance.viewId == original

@given(instance=luniferadoc_richstring_RichStringTableData_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringtabledata_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringTableData)

@given(instance=luniferadoc_richstring_RichStringCode_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringcode_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringCode)



@given(instance=luniferadoc_richstring_RichStringCode_strategy)
def test_luniferadoc_richstring_richstringcode_lang_setter(instance):
    original = instance.lang
    instance.lang = original
    assert instance.lang == original

@given(instance=luniferadoc_richstring_RichStringMovie_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringmovie_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringMovie)



@given(instance=luniferadoc_richstring_RichStringMovie_strategy)
def test_luniferadoc_richstring_richstringmovie_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=luniferadoc_richstring_RichStringMovie_strategy)
def test_luniferadoc_richstring_richstringmovie_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=luniferadoc_richstring_RichStringMovie_strategy)
def test_luniferadoc_richstring_richstringmovie_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original



@given(instance=luniferadoc_richstring_RichStringMovie_strategy)
def test_luniferadoc_richstring_richstringmovie_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original

@given(instance=RichStringTableRow_strategy)
@settings(max_examples=50)
def test_richstringtablerow_instantiation(instance):
    assert isinstance(instance, RichStringTableRow)

@given(instance=luniferadoc_richstring_RichStringTable_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringtable_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringTable)

@given(instance=luniferadoc_richstring_RichStringImg_strategy)
@settings(max_examples=50)
def test_luniferadoc_richstring_richstringimg_instantiation(instance):
    assert isinstance(instance, luniferadoc_richstring_RichStringImg)



@given(instance=luniferadoc_richstring_RichStringImg_strategy)
def test_luniferadoc_richstring_richstringimg_width_setter(instance):
    original = instance.width
    instance.width = original
    assert instance.width == original



@given(instance=luniferadoc_richstring_RichStringImg_strategy)
def test_luniferadoc_richstring_richstringimg_alt_setter(instance):
    original = instance.alt
    instance.alt = original
    assert instance.alt == original



@given(instance=luniferadoc_richstring_RichStringImg_strategy)
def test_luniferadoc_richstring_richstringimg_height_setter(instance):
    original = instance.height
    instance.height = original
    assert instance.height == original



@given(instance=luniferadoc_richstring_RichStringImg_strategy)
def test_luniferadoc_richstring_richstringimg_src_setter(instance):
    original = instance.src
    instance.src = original
    assert instance.src == original
