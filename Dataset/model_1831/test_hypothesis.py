import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    jointPackage_TrgPara,
    TrgSect2,
    TrgSection,
    jointPackage_TrgSect2,
    jointPackage_TrgSect1,
    TrgPara,
    TrgSect1,
    TrgTitledElement,
    jointPackage_TrgSection,
    jointPackage_TrgArticle,
    jointPackage_TrgTitledElement,
    TrgArticle,
    jointPackage_TrgBook,
    TrgBook,
    jointPackage_TrgDocBook,
    SrcTitledEntry,
    SrcDatedEntry,
    SrcAuthoredEntry,
    jointPackage_SrcThesisEntry,
    jointPackage_SrcArticle,
    SrcAuthor,
    jointPackage_SrcBibTeXEntry,
    jointPackage_SrcAuthor,
    SrcThesisEntry,
    jointPackage_SrcMasterThesis,
    jointPackage_SrcPhDThesis,
    SrcBook,
    jointPackage_SrcInBook,
    jointPackage_SrcBook,
    jointPackage_SrcBooklet,
    SrcBookTitledEntry,
    jointPackage_SrcInCollection,
    SrcProceedings,
    jointPackage_SrcInProceedings,
    jointPackage_SrcProceedings,
    jointPackage_SrcManual,
    jointPackage_SrcUnpublished,
    jointPackage_SrcTechReport,
    SrcBibTeXEntry,
    jointPackage_SrcAuthoredEntry,
    jointPackage_SrcDatedEntry,
    jointPackage_SrcTitledEntry,
    jointPackage_SrcBookTitledEntry,
    jointPackage_SrcMisc,
    jointPackage_SrcBibTeXFile,
    TrgDocBook,
    SrcMasterThesis,
    jointPackage_JointMM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jointpackage_trgpara_is_not_abstract():
    assert not inspect.isabstract(jointPackage_TrgPara)


def test_jointpackage_trgpara_constructor_exists():
    assert callable(jointPackage_TrgPara.__init__)


def test_jointpackage_trgpara_constructor_args():
    sig = inspect.signature(jointPackage_TrgPara.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_jointpackage_trgpara_has_content():
    assert hasattr(jointPackage_TrgPara, "content")
    descriptor = None
    for klass in jointPackage_TrgPara.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_trgsect2_is_not_abstract():
    assert not inspect.isabstract(TrgSect2)


def test_trgsect2_constructor_exists():
    assert callable(TrgSect2.__init__)


def test_trgsect2_constructor_args():
    sig = inspect.signature(TrgSect2.__init__)
    params = list(sig.parameters.keys())



def test_trgsection_is_not_abstract():
    assert not inspect.isabstract(TrgSection)


def test_trgsection_constructor_exists():
    assert callable(TrgSection.__init__)


def test_trgsection_constructor_args():
    sig = inspect.signature(TrgSection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_trgsect2_is_not_abstract():
    assert not inspect.isabstract(jointPackage_TrgSect2)


def test_jointpackage_trgsect2_constructor_exists():
    assert callable(jointPackage_TrgSect2.__init__)


def test_jointpackage_trgsect2_constructor_args():
    sig = inspect.signature(jointPackage_TrgSect2.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_trgsect1_is_not_abstract():
    assert not inspect.isabstract(jointPackage_TrgSect1)


def test_jointpackage_trgsect1_constructor_exists():
    assert callable(jointPackage_TrgSect1.__init__)


def test_jointpackage_trgsect1_constructor_args():
    sig = inspect.signature(jointPackage_TrgSect1.__init__)
    params = list(sig.parameters.keys())



def test_trgpara_is_not_abstract():
    assert not inspect.isabstract(TrgPara)


def test_trgpara_constructor_exists():
    assert callable(TrgPara.__init__)


def test_trgpara_constructor_args():
    sig = inspect.signature(TrgPara.__init__)
    params = list(sig.parameters.keys())



def test_trgsect1_is_not_abstract():
    assert not inspect.isabstract(TrgSect1)


def test_trgsect1_constructor_exists():
    assert callable(TrgSect1.__init__)


def test_trgsect1_constructor_args():
    sig = inspect.signature(TrgSect1.__init__)
    params = list(sig.parameters.keys())



def test_trgtitledelement_is_not_abstract():
    assert not inspect.isabstract(TrgTitledElement)


def test_trgtitledelement_constructor_exists():
    assert callable(TrgTitledElement.__init__)


def test_trgtitledelement_constructor_args():
    sig = inspect.signature(TrgTitledElement.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_trgsection_is_not_abstract():
    assert not inspect.isabstract(jointPackage_TrgSection)


def test_jointpackage_trgsection_constructor_exists():
    assert callable(jointPackage_TrgSection.__init__)


def test_jointpackage_trgsection_constructor_args():
    sig = inspect.signature(jointPackage_TrgSection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_trgarticle_is_not_abstract():
    assert not inspect.isabstract(jointPackage_TrgArticle)


def test_jointpackage_trgarticle_constructor_exists():
    assert callable(jointPackage_TrgArticle.__init__)


def test_jointpackage_trgarticle_constructor_args():
    sig = inspect.signature(jointPackage_TrgArticle.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_trgtitledelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage_TrgTitledElement)


def test_jointpackage_trgtitledelement_constructor_exists():
    assert callable(jointPackage_TrgTitledElement.__init__)


def test_jointpackage_trgtitledelement_constructor_args():
    sig = inspect.signature(jointPackage_TrgTitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_jointpackage_trgtitledelement_has_title():
    assert hasattr(jointPackage_TrgTitledElement, "title")
    descriptor = None
    for klass in jointPackage_TrgTitledElement.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_trgarticle_is_not_abstract():
    assert not inspect.isabstract(TrgArticle)


def test_trgarticle_constructor_exists():
    assert callable(TrgArticle.__init__)


def test_trgarticle_constructor_args():
    sig = inspect.signature(TrgArticle.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_trgbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage_TrgBook)


def test_jointpackage_trgbook_constructor_exists():
    assert callable(jointPackage_TrgBook.__init__)


def test_jointpackage_trgbook_constructor_args():
    sig = inspect.signature(jointPackage_TrgBook.__init__)
    params = list(sig.parameters.keys())



def test_trgbook_is_not_abstract():
    assert not inspect.isabstract(TrgBook)


def test_trgbook_constructor_exists():
    assert callable(TrgBook.__init__)


def test_trgbook_constructor_args():
    sig = inspect.signature(TrgBook.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_trgdocbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage_TrgDocBook)


def test_jointpackage_trgdocbook_constructor_exists():
    assert callable(jointPackage_TrgDocBook.__init__)


def test_jointpackage_trgdocbook_constructor_args():
    sig = inspect.signature(jointPackage_TrgDocBook.__init__)
    params = list(sig.parameters.keys())



def test_srctitledentry_is_not_abstract():
    assert not inspect.isabstract(SrcTitledEntry)


def test_srctitledentry_constructor_exists():
    assert callable(SrcTitledEntry.__init__)


def test_srctitledentry_constructor_args():
    sig = inspect.signature(SrcTitledEntry.__init__)
    params = list(sig.parameters.keys())



def test_srcdatedentry_is_not_abstract():
    assert not inspect.isabstract(SrcDatedEntry)


def test_srcdatedentry_constructor_exists():
    assert callable(SrcDatedEntry.__init__)


def test_srcdatedentry_constructor_args():
    sig = inspect.signature(SrcDatedEntry.__init__)
    params = list(sig.parameters.keys())



def test_srcauthoredentry_is_not_abstract():
    assert not inspect.isabstract(SrcAuthoredEntry)


def test_srcauthoredentry_constructor_exists():
    assert callable(SrcAuthoredEntry.__init__)


def test_srcauthoredentry_constructor_args():
    sig = inspect.signature(SrcAuthoredEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcthesisentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcThesisEntry)


def test_jointpackage_srcthesisentry_constructor_exists():
    assert callable(jointPackage_SrcThesisEntry.__init__)


def test_jointpackage_srcthesisentry_constructor_args():
    sig = inspect.signature(jointPackage_SrcThesisEntry.__init__)
    params = list(sig.parameters.keys())
    assert "school" in params, "Missing parameter 'school'"

def test_jointpackage_srcthesisentry_has_school():
    assert hasattr(jointPackage_SrcThesisEntry, "school")
    descriptor = None
    for klass in jointPackage_SrcThesisEntry.__mro__:
        if "school" in klass.__dict__:
            descriptor = klass.__dict__["school"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_srcarticle_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcArticle)


def test_jointpackage_srcarticle_constructor_exists():
    assert callable(jointPackage_SrcArticle.__init__)


def test_jointpackage_srcarticle_constructor_args():
    sig = inspect.signature(jointPackage_SrcArticle.__init__)
    params = list(sig.parameters.keys())
    assert "journal" in params, "Missing parameter 'journal'"

def test_jointpackage_srcarticle_has_journal():
    assert hasattr(jointPackage_SrcArticle, "journal")
    descriptor = None
    for klass in jointPackage_SrcArticle.__mro__:
        if "journal" in klass.__dict__:
            descriptor = klass.__dict__["journal"]
            break
    assert isinstance(descriptor, property)



def test_srcauthor_is_not_abstract():
    assert not inspect.isabstract(SrcAuthor)


def test_srcauthor_constructor_exists():
    assert callable(SrcAuthor.__init__)


def test_srcauthor_constructor_args():
    sig = inspect.signature(SrcAuthor.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcbibtexentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcBibTeXEntry)


def test_jointpackage_srcbibtexentry_constructor_exists():
    assert callable(jointPackage_SrcBibTeXEntry.__init__)


def test_jointpackage_srcbibtexentry_constructor_args():
    sig = inspect.signature(jointPackage_SrcBibTeXEntry.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_jointpackage_srcbibtexentry_has_id():
    assert hasattr(jointPackage_SrcBibTeXEntry, "id")
    descriptor = None
    for klass in jointPackage_SrcBibTeXEntry.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_srcauthor_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcAuthor)


def test_jointpackage_srcauthor_constructor_exists():
    assert callable(jointPackage_SrcAuthor.__init__)


def test_jointpackage_srcauthor_constructor_args():
    sig = inspect.signature(jointPackage_SrcAuthor.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"

def test_jointpackage_srcauthor_has_author():
    assert hasattr(jointPackage_SrcAuthor, "author")
    descriptor = None
    for klass in jointPackage_SrcAuthor.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_srcthesisentry_is_not_abstract():
    assert not inspect.isabstract(SrcThesisEntry)


def test_srcthesisentry_constructor_exists():
    assert callable(SrcThesisEntry.__init__)


def test_srcthesisentry_constructor_args():
    sig = inspect.signature(SrcThesisEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcmasterthesis_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcMasterThesis)


def test_jointpackage_srcmasterthesis_constructor_exists():
    assert callable(jointPackage_SrcMasterThesis.__init__)


def test_jointpackage_srcmasterthesis_constructor_args():
    sig = inspect.signature(jointPackage_SrcMasterThesis.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcphdthesis_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcPhDThesis)


def test_jointpackage_srcphdthesis_constructor_exists():
    assert callable(jointPackage_SrcPhDThesis.__init__)


def test_jointpackage_srcphdthesis_constructor_args():
    sig = inspect.signature(jointPackage_SrcPhDThesis.__init__)
    params = list(sig.parameters.keys())



def test_srcbook_is_not_abstract():
    assert not inspect.isabstract(SrcBook)


def test_srcbook_constructor_exists():
    assert callable(SrcBook.__init__)


def test_srcbook_constructor_args():
    sig = inspect.signature(SrcBook.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcinbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcInBook)


def test_jointpackage_srcinbook_constructor_exists():
    assert callable(jointPackage_SrcInBook.__init__)


def test_jointpackage_srcinbook_constructor_args():
    sig = inspect.signature(jointPackage_SrcInBook.__init__)
    params = list(sig.parameters.keys())
    assert "chapter" in params, "Missing parameter 'chapter'"

def test_jointpackage_srcinbook_has_chapter():
    assert hasattr(jointPackage_SrcInBook, "chapter")
    descriptor = None
    for klass in jointPackage_SrcInBook.__mro__:
        if "chapter" in klass.__dict__:
            descriptor = klass.__dict__["chapter"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_srcbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcBook)


def test_jointpackage_srcbook_constructor_exists():
    assert callable(jointPackage_SrcBook.__init__)


def test_jointpackage_srcbook_constructor_args():
    sig = inspect.signature(jointPackage_SrcBook.__init__)
    params = list(sig.parameters.keys())
    assert "publisher" in params, "Missing parameter 'publisher'"

def test_jointpackage_srcbook_has_publisher():
    assert hasattr(jointPackage_SrcBook, "publisher")
    descriptor = None
    for klass in jointPackage_SrcBook.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_srcbooklet_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcBooklet)


def test_jointpackage_srcbooklet_constructor_exists():
    assert callable(jointPackage_SrcBooklet.__init__)


def test_jointpackage_srcbooklet_constructor_args():
    sig = inspect.signature(jointPackage_SrcBooklet.__init__)
    params = list(sig.parameters.keys())



def test_srcbooktitledentry_is_not_abstract():
    assert not inspect.isabstract(SrcBookTitledEntry)


def test_srcbooktitledentry_constructor_exists():
    assert callable(SrcBookTitledEntry.__init__)


def test_srcbooktitledentry_constructor_args():
    sig = inspect.signature(SrcBookTitledEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcincollection_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcInCollection)


def test_jointpackage_srcincollection_constructor_exists():
    assert callable(jointPackage_SrcInCollection.__init__)


def test_jointpackage_srcincollection_constructor_args():
    sig = inspect.signature(jointPackage_SrcInCollection.__init__)
    params = list(sig.parameters.keys())



def test_srcproceedings_is_not_abstract():
    assert not inspect.isabstract(SrcProceedings)


def test_srcproceedings_constructor_exists():
    assert callable(SrcProceedings.__init__)


def test_srcproceedings_constructor_args():
    sig = inspect.signature(SrcProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcinproceedings_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcInProceedings)


def test_jointpackage_srcinproceedings_constructor_exists():
    assert callable(jointPackage_SrcInProceedings.__init__)


def test_jointpackage_srcinproceedings_constructor_args():
    sig = inspect.signature(jointPackage_SrcInProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcproceedings_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcProceedings)


def test_jointpackage_srcproceedings_constructor_exists():
    assert callable(jointPackage_SrcProceedings.__init__)


def test_jointpackage_srcproceedings_constructor_args():
    sig = inspect.signature(jointPackage_SrcProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcmanual_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcManual)


def test_jointpackage_srcmanual_constructor_exists():
    assert callable(jointPackage_SrcManual.__init__)


def test_jointpackage_srcmanual_constructor_args():
    sig = inspect.signature(jointPackage_SrcManual.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcunpublished_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcUnpublished)


def test_jointpackage_srcunpublished_constructor_exists():
    assert callable(jointPackage_SrcUnpublished.__init__)


def test_jointpackage_srcunpublished_constructor_args():
    sig = inspect.signature(jointPackage_SrcUnpublished.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_jointpackage_srcunpublished_has_note():
    assert hasattr(jointPackage_SrcUnpublished, "note")
    descriptor = None
    for klass in jointPackage_SrcUnpublished.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_srctechreport_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcTechReport)


def test_jointpackage_srctechreport_constructor_exists():
    assert callable(jointPackage_SrcTechReport.__init__)


def test_jointpackage_srctechreport_constructor_args():
    sig = inspect.signature(jointPackage_SrcTechReport.__init__)
    params = list(sig.parameters.keys())



def test_srcbibtexentry_is_not_abstract():
    assert not inspect.isabstract(SrcBibTeXEntry)


def test_srcbibtexentry_constructor_exists():
    assert callable(SrcBibTeXEntry.__init__)


def test_srcbibtexentry_constructor_args():
    sig = inspect.signature(SrcBibTeXEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcauthoredentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcAuthoredEntry)


def test_jointpackage_srcauthoredentry_constructor_exists():
    assert callable(jointPackage_SrcAuthoredEntry.__init__)


def test_jointpackage_srcauthoredentry_constructor_args():
    sig = inspect.signature(jointPackage_SrcAuthoredEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcdatedentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcDatedEntry)


def test_jointpackage_srcdatedentry_constructor_exists():
    assert callable(jointPackage_SrcDatedEntry.__init__)


def test_jointpackage_srcdatedentry_constructor_args():
    sig = inspect.signature(jointPackage_SrcDatedEntry.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_jointpackage_srcdatedentry_has_year():
    assert hasattr(jointPackage_SrcDatedEntry, "year")
    descriptor = None
    for klass in jointPackage_SrcDatedEntry.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_srctitledentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcTitledEntry)


def test_jointpackage_srctitledentry_constructor_exists():
    assert callable(jointPackage_SrcTitledEntry.__init__)


def test_jointpackage_srctitledentry_constructor_args():
    sig = inspect.signature(jointPackage_SrcTitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_jointpackage_srctitledentry_has_title():
    assert hasattr(jointPackage_SrcTitledEntry, "title")
    descriptor = None
    for klass in jointPackage_SrcTitledEntry.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_srcbooktitledentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcBookTitledEntry)


def test_jointpackage_srcbooktitledentry_constructor_exists():
    assert callable(jointPackage_SrcBookTitledEntry.__init__)


def test_jointpackage_srcbooktitledentry_constructor_args():
    sig = inspect.signature(jointPackage_SrcBookTitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "booktitle" in params, "Missing parameter 'booktitle'"

def test_jointpackage_srcbooktitledentry_has_booktitle():
    assert hasattr(jointPackage_SrcBookTitledEntry, "booktitle")
    descriptor = None
    for klass in jointPackage_SrcBookTitledEntry.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage_srcmisc_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcMisc)


def test_jointpackage_srcmisc_constructor_exists():
    assert callable(jointPackage_SrcMisc.__init__)


def test_jointpackage_srcmisc_constructor_args():
    sig = inspect.signature(jointPackage_SrcMisc.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_srcbibtexfile_is_not_abstract():
    assert not inspect.isabstract(jointPackage_SrcBibTeXFile)


def test_jointpackage_srcbibtexfile_constructor_exists():
    assert callable(jointPackage_SrcBibTeXFile.__init__)


def test_jointpackage_srcbibtexfile_constructor_args():
    sig = inspect.signature(jointPackage_SrcBibTeXFile.__init__)
    params = list(sig.parameters.keys())



def test_trgdocbook_is_not_abstract():
    assert not inspect.isabstract(TrgDocBook)


def test_trgdocbook_constructor_exists():
    assert callable(TrgDocBook.__init__)


def test_trgdocbook_constructor_args():
    sig = inspect.signature(TrgDocBook.__init__)
    params = list(sig.parameters.keys())



def test_srcmasterthesis_is_not_abstract():
    assert not inspect.isabstract(SrcMasterThesis)


def test_srcmasterthesis_constructor_exists():
    assert callable(SrcMasterThesis.__init__)


def test_srcmasterthesis_constructor_args():
    sig = inspect.signature(SrcMasterThesis.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage_jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage_JointMM)


def test_jointpackage_jointmm_constructor_exists():
    assert callable(jointPackage_JointMM.__init__)


def test_jointpackage_jointmm_constructor_args():
    sig = inspect.signature(jointPackage_JointMM.__init__)
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
jointPackage_TrgPara_strategy = st.builds(
    jointPackage_TrgPara,
    content=
        safe_text
)
TrgSect2_strategy = st.builds(
    TrgSect2,
)
TrgSection_strategy = st.builds(
    TrgSection,
)
jointPackage_TrgSect2_strategy = st.builds(
    jointPackage_TrgSect2,
)
jointPackage_TrgSect1_strategy = st.builds(
    jointPackage_TrgSect1,
)
TrgPara_strategy = st.builds(
    TrgPara,
)
TrgSect1_strategy = st.builds(
    TrgSect1,
)
TrgTitledElement_strategy = st.builds(
    TrgTitledElement,
)
jointPackage_TrgSection_strategy = st.builds(
    jointPackage_TrgSection,
)
jointPackage_TrgArticle_strategy = st.builds(
    jointPackage_TrgArticle,
)
jointPackage_TrgTitledElement_strategy = st.builds(
    jointPackage_TrgTitledElement,
    title=
        safe_text
)
TrgArticle_strategy = st.builds(
    TrgArticle,
)
jointPackage_TrgBook_strategy = st.builds(
    jointPackage_TrgBook,
)
TrgBook_strategy = st.builds(
    TrgBook,
)
jointPackage_TrgDocBook_strategy = st.builds(
    jointPackage_TrgDocBook,
)
SrcTitledEntry_strategy = st.builds(
    SrcTitledEntry,
)
SrcDatedEntry_strategy = st.builds(
    SrcDatedEntry,
)
SrcAuthoredEntry_strategy = st.builds(
    SrcAuthoredEntry,
)
jointPackage_SrcThesisEntry_strategy = st.builds(
    jointPackage_SrcThesisEntry,
    school=
        safe_text
)
jointPackage_SrcArticle_strategy = st.builds(
    jointPackage_SrcArticle,
    journal=
        safe_text
)
SrcAuthor_strategy = st.builds(
    SrcAuthor,
)
jointPackage_SrcBibTeXEntry_strategy = st.builds(
    jointPackage_SrcBibTeXEntry,
    id=
        safe_text
)
jointPackage_SrcAuthor_strategy = st.builds(
    jointPackage_SrcAuthor,
    author=
        safe_text
)
SrcThesisEntry_strategy = st.builds(
    SrcThesisEntry,
)
jointPackage_SrcMasterThesis_strategy = st.builds(
    jointPackage_SrcMasterThesis,
)
jointPackage_SrcPhDThesis_strategy = st.builds(
    jointPackage_SrcPhDThesis,
)
SrcBook_strategy = st.builds(
    SrcBook,
)
jointPackage_SrcInBook_strategy = st.builds(
    jointPackage_SrcInBook,
    chapter=
        st.integers()
)
jointPackage_SrcBook_strategy = st.builds(
    jointPackage_SrcBook,
    publisher=
        safe_text
)
jointPackage_SrcBooklet_strategy = st.builds(
    jointPackage_SrcBooklet,
)
SrcBookTitledEntry_strategy = st.builds(
    SrcBookTitledEntry,
)
jointPackage_SrcInCollection_strategy = st.builds(
    jointPackage_SrcInCollection,
)
SrcProceedings_strategy = st.builds(
    SrcProceedings,
)
jointPackage_SrcInProceedings_strategy = st.builds(
    jointPackage_SrcInProceedings,
)
jointPackage_SrcProceedings_strategy = st.builds(
    jointPackage_SrcProceedings,
)
jointPackage_SrcManual_strategy = st.builds(
    jointPackage_SrcManual,
)
jointPackage_SrcUnpublished_strategy = st.builds(
    jointPackage_SrcUnpublished,
    note=
        safe_text
)
jointPackage_SrcTechReport_strategy = st.builds(
    jointPackage_SrcTechReport,
)
SrcBibTeXEntry_strategy = st.builds(
    SrcBibTeXEntry,
)
jointPackage_SrcAuthoredEntry_strategy = st.builds(
    jointPackage_SrcAuthoredEntry,
)
jointPackage_SrcDatedEntry_strategy = st.builds(
    jointPackage_SrcDatedEntry,
    year=
        safe_text
)
jointPackage_SrcTitledEntry_strategy = st.builds(
    jointPackage_SrcTitledEntry,
    title=
        safe_text
)
jointPackage_SrcBookTitledEntry_strategy = st.builds(
    jointPackage_SrcBookTitledEntry,
    booktitle=
        safe_text
)
jointPackage_SrcMisc_strategy = st.builds(
    jointPackage_SrcMisc,
)
jointPackage_SrcBibTeXFile_strategy = st.builds(
    jointPackage_SrcBibTeXFile,
)
TrgDocBook_strategy = st.builds(
    TrgDocBook,
)
SrcMasterThesis_strategy = st.builds(
    SrcMasterThesis,
)
jointPackage_JointMM_strategy = st.builds(
    jointPackage_JointMM,
)

@given(instance=jointPackage_TrgPara_strategy)
@settings(max_examples=50)
def test_jointpackage_trgpara_instantiation(instance):
    assert isinstance(instance, jointPackage_TrgPara)



@given(instance=jointPackage_TrgPara_strategy)
def test_jointpackage_trgpara_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=TrgSect2_strategy)
@settings(max_examples=50)
def test_trgsect2_instantiation(instance):
    assert isinstance(instance, TrgSect2)

@given(instance=TrgSection_strategy)
@settings(max_examples=50)
def test_trgsection_instantiation(instance):
    assert isinstance(instance, TrgSection)

@given(instance=jointPackage_TrgSect2_strategy)
@settings(max_examples=50)
def test_jointpackage_trgsect2_instantiation(instance):
    assert isinstance(instance, jointPackage_TrgSect2)

@given(instance=jointPackage_TrgSect1_strategy)
@settings(max_examples=50)
def test_jointpackage_trgsect1_instantiation(instance):
    assert isinstance(instance, jointPackage_TrgSect1)

@given(instance=TrgPara_strategy)
@settings(max_examples=50)
def test_trgpara_instantiation(instance):
    assert isinstance(instance, TrgPara)

@given(instance=TrgSect1_strategy)
@settings(max_examples=50)
def test_trgsect1_instantiation(instance):
    assert isinstance(instance, TrgSect1)

@given(instance=TrgTitledElement_strategy)
@settings(max_examples=50)
def test_trgtitledelement_instantiation(instance):
    assert isinstance(instance, TrgTitledElement)

@given(instance=jointPackage_TrgSection_strategy)
@settings(max_examples=50)
def test_jointpackage_trgsection_instantiation(instance):
    assert isinstance(instance, jointPackage_TrgSection)

@given(instance=jointPackage_TrgArticle_strategy)
@settings(max_examples=50)
def test_jointpackage_trgarticle_instantiation(instance):
    assert isinstance(instance, jointPackage_TrgArticle)

@given(instance=jointPackage_TrgTitledElement_strategy)
@settings(max_examples=50)
def test_jointpackage_trgtitledelement_instantiation(instance):
    assert isinstance(instance, jointPackage_TrgTitledElement)



@given(instance=jointPackage_TrgTitledElement_strategy)
def test_jointpackage_trgtitledelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=TrgArticle_strategy)
@settings(max_examples=50)
def test_trgarticle_instantiation(instance):
    assert isinstance(instance, TrgArticle)

@given(instance=jointPackage_TrgBook_strategy)
@settings(max_examples=50)
def test_jointpackage_trgbook_instantiation(instance):
    assert isinstance(instance, jointPackage_TrgBook)

@given(instance=TrgBook_strategy)
@settings(max_examples=50)
def test_trgbook_instantiation(instance):
    assert isinstance(instance, TrgBook)

@given(instance=jointPackage_TrgDocBook_strategy)
@settings(max_examples=50)
def test_jointpackage_trgdocbook_instantiation(instance):
    assert isinstance(instance, jointPackage_TrgDocBook)

@given(instance=SrcTitledEntry_strategy)
@settings(max_examples=50)
def test_srctitledentry_instantiation(instance):
    assert isinstance(instance, SrcTitledEntry)

@given(instance=SrcDatedEntry_strategy)
@settings(max_examples=50)
def test_srcdatedentry_instantiation(instance):
    assert isinstance(instance, SrcDatedEntry)

@given(instance=SrcAuthoredEntry_strategy)
@settings(max_examples=50)
def test_srcauthoredentry_instantiation(instance):
    assert isinstance(instance, SrcAuthoredEntry)

@given(instance=jointPackage_SrcThesisEntry_strategy)
@settings(max_examples=50)
def test_jointpackage_srcthesisentry_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcThesisEntry)



@given(instance=jointPackage_SrcThesisEntry_strategy)
def test_jointpackage_srcthesisentry_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original

@given(instance=jointPackage_SrcArticle_strategy)
@settings(max_examples=50)
def test_jointpackage_srcarticle_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcArticle)



@given(instance=jointPackage_SrcArticle_strategy)
def test_jointpackage_srcarticle_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original

@given(instance=SrcAuthor_strategy)
@settings(max_examples=50)
def test_srcauthor_instantiation(instance):
    assert isinstance(instance, SrcAuthor)

@given(instance=jointPackage_SrcBibTeXEntry_strategy)
@settings(max_examples=50)
def test_jointpackage_srcbibtexentry_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcBibTeXEntry)



@given(instance=jointPackage_SrcBibTeXEntry_strategy)
def test_jointpackage_srcbibtexentry_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=jointPackage_SrcAuthor_strategy)
@settings(max_examples=50)
def test_jointpackage_srcauthor_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcAuthor)



@given(instance=jointPackage_SrcAuthor_strategy)
def test_jointpackage_srcauthor_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SrcThesisEntry_strategy)
@settings(max_examples=50)
def test_srcthesisentry_instantiation(instance):
    assert isinstance(instance, SrcThesisEntry)

@given(instance=jointPackage_SrcMasterThesis_strategy)
@settings(max_examples=50)
def test_jointpackage_srcmasterthesis_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcMasterThesis)

@given(instance=jointPackage_SrcPhDThesis_strategy)
@settings(max_examples=50)
def test_jointpackage_srcphdthesis_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcPhDThesis)

@given(instance=SrcBook_strategy)
@settings(max_examples=50)
def test_srcbook_instantiation(instance):
    assert isinstance(instance, SrcBook)

@given(instance=jointPackage_SrcInBook_strategy)
@settings(max_examples=50)
def test_jointpackage_srcinbook_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcInBook)



@given(instance=jointPackage_SrcInBook_strategy)
def test_jointpackage_srcinbook_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original

@given(instance=jointPackage_SrcBook_strategy)
@settings(max_examples=50)
def test_jointpackage_srcbook_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcBook)



@given(instance=jointPackage_SrcBook_strategy)
def test_jointpackage_srcbook_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=jointPackage_SrcBooklet_strategy)
@settings(max_examples=50)
def test_jointpackage_srcbooklet_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcBooklet)

@given(instance=SrcBookTitledEntry_strategy)
@settings(max_examples=50)
def test_srcbooktitledentry_instantiation(instance):
    assert isinstance(instance, SrcBookTitledEntry)

@given(instance=jointPackage_SrcInCollection_strategy)
@settings(max_examples=50)
def test_jointpackage_srcincollection_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcInCollection)

@given(instance=SrcProceedings_strategy)
@settings(max_examples=50)
def test_srcproceedings_instantiation(instance):
    assert isinstance(instance, SrcProceedings)

@given(instance=jointPackage_SrcInProceedings_strategy)
@settings(max_examples=50)
def test_jointpackage_srcinproceedings_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcInProceedings)

@given(instance=jointPackage_SrcProceedings_strategy)
@settings(max_examples=50)
def test_jointpackage_srcproceedings_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcProceedings)

@given(instance=jointPackage_SrcManual_strategy)
@settings(max_examples=50)
def test_jointpackage_srcmanual_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcManual)

@given(instance=jointPackage_SrcUnpublished_strategy)
@settings(max_examples=50)
def test_jointpackage_srcunpublished_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcUnpublished)



@given(instance=jointPackage_SrcUnpublished_strategy)
def test_jointpackage_srcunpublished_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=jointPackage_SrcTechReport_strategy)
@settings(max_examples=50)
def test_jointpackage_srctechreport_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcTechReport)

@given(instance=SrcBibTeXEntry_strategy)
@settings(max_examples=50)
def test_srcbibtexentry_instantiation(instance):
    assert isinstance(instance, SrcBibTeXEntry)

@given(instance=jointPackage_SrcAuthoredEntry_strategy)
@settings(max_examples=50)
def test_jointpackage_srcauthoredentry_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcAuthoredEntry)

@given(instance=jointPackage_SrcDatedEntry_strategy)
@settings(max_examples=50)
def test_jointpackage_srcdatedentry_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcDatedEntry)



@given(instance=jointPackage_SrcDatedEntry_strategy)
def test_jointpackage_srcdatedentry_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=jointPackage_SrcTitledEntry_strategy)
@settings(max_examples=50)
def test_jointpackage_srctitledentry_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcTitledEntry)



@given(instance=jointPackage_SrcTitledEntry_strategy)
def test_jointpackage_srctitledentry_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=jointPackage_SrcBookTitledEntry_strategy)
@settings(max_examples=50)
def test_jointpackage_srcbooktitledentry_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcBookTitledEntry)



@given(instance=jointPackage_SrcBookTitledEntry_strategy)
def test_jointpackage_srcbooktitledentry_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=jointPackage_SrcMisc_strategy)
@settings(max_examples=50)
def test_jointpackage_srcmisc_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcMisc)

@given(instance=jointPackage_SrcBibTeXFile_strategy)
@settings(max_examples=50)
def test_jointpackage_srcbibtexfile_instantiation(instance):
    assert isinstance(instance, jointPackage_SrcBibTeXFile)

@given(instance=TrgDocBook_strategy)
@settings(max_examples=50)
def test_trgdocbook_instantiation(instance):
    assert isinstance(instance, TrgDocBook)

@given(instance=SrcMasterThesis_strategy)
@settings(max_examples=50)
def test_srcmasterthesis_instantiation(instance):
    assert isinstance(instance, SrcMasterThesis)

@given(instance=jointPackage_JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage_jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage_JointMM)
