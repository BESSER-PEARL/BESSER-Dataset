import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    jointPackage::TrgPara,
    TrgSect2,
    TrgSection,
    jointPackage::TrgSect2,
    jointPackage::TrgSect1,
    TrgPara,
    TrgSect1,
    TrgTitledElement,
    jointPackage::TrgSection,
    jointPackage::TrgArticle,
    jointPackage::TrgTitledElement,
    TrgArticle,
    jointPackage::TrgBook,
    TrgBook,
    jointPackage::TrgDocBook,
    SrcTitledEntry,
    SrcDatedEntry,
    SrcAuthoredEntry,
    jointPackage::SrcThesisEntry,
    jointPackage::SrcArticle,
    SrcAuthor,
    jointPackage::SrcBibTeXEntry,
    jointPackage::SrcAuthor,
    SrcThesisEntry,
    jointPackage::SrcMasterThesis,
    jointPackage::SrcPhDThesis,
    SrcBook,
    jointPackage::SrcInBook,
    jointPackage::SrcBook,
    jointPackage::SrcBooklet,
    SrcBookTitledEntry,
    jointPackage::SrcInCollection,
    SrcProceedings,
    jointPackage::SrcInProceedings,
    jointPackage::SrcProceedings,
    jointPackage::SrcManual,
    jointPackage::SrcUnpublished,
    jointPackage::SrcTechReport,
    SrcBibTeXEntry,
    jointPackage::SrcDatedEntry,
    jointPackage::SrcTitledEntry,
    jointPackage::SrcBookTitledEntry,
    jointPackage::SrcMisc,
    jointPackage::SrcAuthoredEntry,
    jointPackage::SrcBibTeXFile,
    TrgDocBook,
    SrcMasterThesis,
    jointPackage::JointMM,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jointpackage::trgpara_is_not_abstract():
    assert not inspect.isabstract(jointPackage::TrgPara)


def test_jointpackage::trgpara_constructor_exists():
    assert callable(jointPackage::TrgPara.__init__)


def test_jointpackage::trgpara_constructor_args():
    sig = inspect.signature(jointPackage::TrgPara.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_jointpackage::trgpara_has_content():
    assert hasattr(jointPackage::TrgPara, "content")
    descriptor = None
    for klass in jointPackage::TrgPara.__mro__:
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



def test_jointpackage::trgsect2_is_not_abstract():
    assert not inspect.isabstract(jointPackage::TrgSect2)


def test_jointpackage::trgsect2_constructor_exists():
    assert callable(jointPackage::TrgSect2.__init__)


def test_jointpackage::trgsect2_constructor_args():
    sig = inspect.signature(jointPackage::TrgSect2.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::trgsect1_is_not_abstract():
    assert not inspect.isabstract(jointPackage::TrgSect1)


def test_jointpackage::trgsect1_constructor_exists():
    assert callable(jointPackage::TrgSect1.__init__)


def test_jointpackage::trgsect1_constructor_args():
    sig = inspect.signature(jointPackage::TrgSect1.__init__)
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



def test_jointpackage::trgsection_is_not_abstract():
    assert not inspect.isabstract(jointPackage::TrgSection)


def test_jointpackage::trgsection_constructor_exists():
    assert callable(jointPackage::TrgSection.__init__)


def test_jointpackage::trgsection_constructor_args():
    sig = inspect.signature(jointPackage::TrgSection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::trgarticle_is_not_abstract():
    assert not inspect.isabstract(jointPackage::TrgArticle)


def test_jointpackage::trgarticle_constructor_exists():
    assert callable(jointPackage::TrgArticle.__init__)


def test_jointpackage::trgarticle_constructor_args():
    sig = inspect.signature(jointPackage::TrgArticle.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::trgtitledelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::TrgTitledElement)


def test_jointpackage::trgtitledelement_constructor_exists():
    assert callable(jointPackage::TrgTitledElement.__init__)


def test_jointpackage::trgtitledelement_constructor_args():
    sig = inspect.signature(jointPackage::TrgTitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_jointpackage::trgtitledelement_has_title():
    assert hasattr(jointPackage::TrgTitledElement, "title")
    descriptor = None
    for klass in jointPackage::TrgTitledElement.__mro__:
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



def test_jointpackage::trgbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage::TrgBook)


def test_jointpackage::trgbook_constructor_exists():
    assert callable(jointPackage::TrgBook.__init__)


def test_jointpackage::trgbook_constructor_args():
    sig = inspect.signature(jointPackage::TrgBook.__init__)
    params = list(sig.parameters.keys())



def test_trgbook_is_not_abstract():
    assert not inspect.isabstract(TrgBook)


def test_trgbook_constructor_exists():
    assert callable(TrgBook.__init__)


def test_trgbook_constructor_args():
    sig = inspect.signature(TrgBook.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::trgdocbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage::TrgDocBook)


def test_jointpackage::trgdocbook_constructor_exists():
    assert callable(jointPackage::TrgDocBook.__init__)


def test_jointpackage::trgdocbook_constructor_args():
    sig = inspect.signature(jointPackage::TrgDocBook.__init__)
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



def test_jointpackage::srcthesisentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcThesisEntry)


def test_jointpackage::srcthesisentry_constructor_exists():
    assert callable(jointPackage::SrcThesisEntry.__init__)


def test_jointpackage::srcthesisentry_constructor_args():
    sig = inspect.signature(jointPackage::SrcThesisEntry.__init__)
    params = list(sig.parameters.keys())
    assert "school" in params, "Missing parameter 'school'"

def test_jointpackage::srcthesisentry_has_school():
    assert hasattr(jointPackage::SrcThesisEntry, "school")
    descriptor = None
    for klass in jointPackage::SrcThesisEntry.__mro__:
        if "school" in klass.__dict__:
            descriptor = klass.__dict__["school"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::srcarticle_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcArticle)


def test_jointpackage::srcarticle_constructor_exists():
    assert callable(jointPackage::SrcArticle.__init__)


def test_jointpackage::srcarticle_constructor_args():
    sig = inspect.signature(jointPackage::SrcArticle.__init__)
    params = list(sig.parameters.keys())
    assert "journal" in params, "Missing parameter 'journal'"

def test_jointpackage::srcarticle_has_journal():
    assert hasattr(jointPackage::SrcArticle, "journal")
    descriptor = None
    for klass in jointPackage::SrcArticle.__mro__:
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



def test_jointpackage::srcbibtexentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcBibTeXEntry)


def test_jointpackage::srcbibtexentry_constructor_exists():
    assert callable(jointPackage::SrcBibTeXEntry.__init__)


def test_jointpackage::srcbibtexentry_constructor_args():
    sig = inspect.signature(jointPackage::SrcBibTeXEntry.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_jointpackage::srcbibtexentry_has_id():
    assert hasattr(jointPackage::SrcBibTeXEntry, "id")
    descriptor = None
    for klass in jointPackage::SrcBibTeXEntry.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::srcauthor_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcAuthor)


def test_jointpackage::srcauthor_constructor_exists():
    assert callable(jointPackage::SrcAuthor.__init__)


def test_jointpackage::srcauthor_constructor_args():
    sig = inspect.signature(jointPackage::SrcAuthor.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"

def test_jointpackage::srcauthor_has_author():
    assert hasattr(jointPackage::SrcAuthor, "author")
    descriptor = None
    for klass in jointPackage::SrcAuthor.__mro__:
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



def test_jointpackage::srcmasterthesis_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcMasterThesis)


def test_jointpackage::srcmasterthesis_constructor_exists():
    assert callable(jointPackage::SrcMasterThesis.__init__)


def test_jointpackage::srcmasterthesis_constructor_args():
    sig = inspect.signature(jointPackage::SrcMasterThesis.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcphdthesis_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcPhDThesis)


def test_jointpackage::srcphdthesis_constructor_exists():
    assert callable(jointPackage::SrcPhDThesis.__init__)


def test_jointpackage::srcphdthesis_constructor_args():
    sig = inspect.signature(jointPackage::SrcPhDThesis.__init__)
    params = list(sig.parameters.keys())



def test_srcbook_is_not_abstract():
    assert not inspect.isabstract(SrcBook)


def test_srcbook_constructor_exists():
    assert callable(SrcBook.__init__)


def test_srcbook_constructor_args():
    sig = inspect.signature(SrcBook.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcinbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcInBook)


def test_jointpackage::srcinbook_constructor_exists():
    assert callable(jointPackage::SrcInBook.__init__)


def test_jointpackage::srcinbook_constructor_args():
    sig = inspect.signature(jointPackage::SrcInBook.__init__)
    params = list(sig.parameters.keys())
    assert "chapter" in params, "Missing parameter 'chapter'"

def test_jointpackage::srcinbook_has_chapter():
    assert hasattr(jointPackage::SrcInBook, "chapter")
    descriptor = None
    for klass in jointPackage::SrcInBook.__mro__:
        if "chapter" in klass.__dict__:
            descriptor = klass.__dict__["chapter"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::srcbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcBook)


def test_jointpackage::srcbook_constructor_exists():
    assert callable(jointPackage::SrcBook.__init__)


def test_jointpackage::srcbook_constructor_args():
    sig = inspect.signature(jointPackage::SrcBook.__init__)
    params = list(sig.parameters.keys())
    assert "publisher" in params, "Missing parameter 'publisher'"

def test_jointpackage::srcbook_has_publisher():
    assert hasattr(jointPackage::SrcBook, "publisher")
    descriptor = None
    for klass in jointPackage::SrcBook.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::srcbooklet_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcBooklet)


def test_jointpackage::srcbooklet_constructor_exists():
    assert callable(jointPackage::SrcBooklet.__init__)


def test_jointpackage::srcbooklet_constructor_args():
    sig = inspect.signature(jointPackage::SrcBooklet.__init__)
    params = list(sig.parameters.keys())



def test_srcbooktitledentry_is_not_abstract():
    assert not inspect.isabstract(SrcBookTitledEntry)


def test_srcbooktitledentry_constructor_exists():
    assert callable(SrcBookTitledEntry.__init__)


def test_srcbooktitledentry_constructor_args():
    sig = inspect.signature(SrcBookTitledEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcincollection_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcInCollection)


def test_jointpackage::srcincollection_constructor_exists():
    assert callable(jointPackage::SrcInCollection.__init__)


def test_jointpackage::srcincollection_constructor_args():
    sig = inspect.signature(jointPackage::SrcInCollection.__init__)
    params = list(sig.parameters.keys())



def test_srcproceedings_is_not_abstract():
    assert not inspect.isabstract(SrcProceedings)


def test_srcproceedings_constructor_exists():
    assert callable(SrcProceedings.__init__)


def test_srcproceedings_constructor_args():
    sig = inspect.signature(SrcProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcinproceedings_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcInProceedings)


def test_jointpackage::srcinproceedings_constructor_exists():
    assert callable(jointPackage::SrcInProceedings.__init__)


def test_jointpackage::srcinproceedings_constructor_args():
    sig = inspect.signature(jointPackage::SrcInProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcproceedings_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcProceedings)


def test_jointpackage::srcproceedings_constructor_exists():
    assert callable(jointPackage::SrcProceedings.__init__)


def test_jointpackage::srcproceedings_constructor_args():
    sig = inspect.signature(jointPackage::SrcProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcmanual_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcManual)


def test_jointpackage::srcmanual_constructor_exists():
    assert callable(jointPackage::SrcManual.__init__)


def test_jointpackage::srcmanual_constructor_args():
    sig = inspect.signature(jointPackage::SrcManual.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcunpublished_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcUnpublished)


def test_jointpackage::srcunpublished_constructor_exists():
    assert callable(jointPackage::SrcUnpublished.__init__)


def test_jointpackage::srcunpublished_constructor_args():
    sig = inspect.signature(jointPackage::SrcUnpublished.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_jointpackage::srcunpublished_has_note():
    assert hasattr(jointPackage::SrcUnpublished, "note")
    descriptor = None
    for klass in jointPackage::SrcUnpublished.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::srctechreport_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcTechReport)


def test_jointpackage::srctechreport_constructor_exists():
    assert callable(jointPackage::SrcTechReport.__init__)


def test_jointpackage::srctechreport_constructor_args():
    sig = inspect.signature(jointPackage::SrcTechReport.__init__)
    params = list(sig.parameters.keys())



def test_srcbibtexentry_is_not_abstract():
    assert not inspect.isabstract(SrcBibTeXEntry)


def test_srcbibtexentry_constructor_exists():
    assert callable(SrcBibTeXEntry.__init__)


def test_srcbibtexentry_constructor_args():
    sig = inspect.signature(SrcBibTeXEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcdatedentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcDatedEntry)


def test_jointpackage::srcdatedentry_constructor_exists():
    assert callable(jointPackage::SrcDatedEntry.__init__)


def test_jointpackage::srcdatedentry_constructor_args():
    sig = inspect.signature(jointPackage::SrcDatedEntry.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_jointpackage::srcdatedentry_has_year():
    assert hasattr(jointPackage::SrcDatedEntry, "year")
    descriptor = None
    for klass in jointPackage::SrcDatedEntry.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::srctitledentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcTitledEntry)


def test_jointpackage::srctitledentry_constructor_exists():
    assert callable(jointPackage::SrcTitledEntry.__init__)


def test_jointpackage::srctitledentry_constructor_args():
    sig = inspect.signature(jointPackage::SrcTitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_jointpackage::srctitledentry_has_title():
    assert hasattr(jointPackage::SrcTitledEntry, "title")
    descriptor = None
    for klass in jointPackage::SrcTitledEntry.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::srcbooktitledentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcBookTitledEntry)


def test_jointpackage::srcbooktitledentry_constructor_exists():
    assert callable(jointPackage::SrcBookTitledEntry.__init__)


def test_jointpackage::srcbooktitledentry_constructor_args():
    sig = inspect.signature(jointPackage::SrcBookTitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "booktitle" in params, "Missing parameter 'booktitle'"

def test_jointpackage::srcbooktitledentry_has_booktitle():
    assert hasattr(jointPackage::SrcBookTitledEntry, "booktitle")
    descriptor = None
    for klass in jointPackage::SrcBookTitledEntry.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::srcmisc_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcMisc)


def test_jointpackage::srcmisc_constructor_exists():
    assert callable(jointPackage::SrcMisc.__init__)


def test_jointpackage::srcmisc_constructor_args():
    sig = inspect.signature(jointPackage::SrcMisc.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcauthoredentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcAuthoredEntry)


def test_jointpackage::srcauthoredentry_constructor_exists():
    assert callable(jointPackage::SrcAuthoredEntry.__init__)


def test_jointpackage::srcauthoredentry_constructor_args():
    sig = inspect.signature(jointPackage::SrcAuthoredEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::srcbibtexfile_is_not_abstract():
    assert not inspect.isabstract(jointPackage::SrcBibTeXFile)


def test_jointpackage::srcbibtexfile_constructor_exists():
    assert callable(jointPackage::SrcBibTeXFile.__init__)


def test_jointpackage::srcbibtexfile_constructor_args():
    sig = inspect.signature(jointPackage::SrcBibTeXFile.__init__)
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



def test_jointpackage::jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::JointMM)


def test_jointpackage::jointmm_constructor_exists():
    assert callable(jointPackage::JointMM.__init__)


def test_jointpackage::jointmm_constructor_args():
    sig = inspect.signature(jointPackage::JointMM.__init__)
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
jointPackage::TrgPara_strategy = st.builds(
    jointPackage::TrgPara,
    content=
        safe_text
)
TrgSect2_strategy = st.builds(
    TrgSect2,
)
TrgSection_strategy = st.builds(
    TrgSection,
)
jointPackage::TrgSect2_strategy = st.builds(
    jointPackage::TrgSect2,
)
jointPackage::TrgSect1_strategy = st.builds(
    jointPackage::TrgSect1,
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
jointPackage::TrgSection_strategy = st.builds(
    jointPackage::TrgSection,
)
jointPackage::TrgArticle_strategy = st.builds(
    jointPackage::TrgArticle,
)
jointPackage::TrgTitledElement_strategy = st.builds(
    jointPackage::TrgTitledElement,
    title=
        safe_text
)
TrgArticle_strategy = st.builds(
    TrgArticle,
)
jointPackage::TrgBook_strategy = st.builds(
    jointPackage::TrgBook,
)
TrgBook_strategy = st.builds(
    TrgBook,
)
jointPackage::TrgDocBook_strategy = st.builds(
    jointPackage::TrgDocBook,
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
jointPackage::SrcThesisEntry_strategy = st.builds(
    jointPackage::SrcThesisEntry,
    school=
        safe_text
)
jointPackage::SrcArticle_strategy = st.builds(
    jointPackage::SrcArticle,
    journal=
        safe_text
)
SrcAuthor_strategy = st.builds(
    SrcAuthor,
)
jointPackage::SrcBibTeXEntry_strategy = st.builds(
    jointPackage::SrcBibTeXEntry,
    id=
        safe_text
)
jointPackage::SrcAuthor_strategy = st.builds(
    jointPackage::SrcAuthor,
    author=
        safe_text
)
SrcThesisEntry_strategy = st.builds(
    SrcThesisEntry,
)
jointPackage::SrcMasterThesis_strategy = st.builds(
    jointPackage::SrcMasterThesis,
)
jointPackage::SrcPhDThesis_strategy = st.builds(
    jointPackage::SrcPhDThesis,
)
SrcBook_strategy = st.builds(
    SrcBook,
)
jointPackage::SrcInBook_strategy = st.builds(
    jointPackage::SrcInBook,
    chapter=
        st.integers()
)
jointPackage::SrcBook_strategy = st.builds(
    jointPackage::SrcBook,
    publisher=
        safe_text
)
jointPackage::SrcBooklet_strategy = st.builds(
    jointPackage::SrcBooklet,
)
SrcBookTitledEntry_strategy = st.builds(
    SrcBookTitledEntry,
)
jointPackage::SrcInCollection_strategy = st.builds(
    jointPackage::SrcInCollection,
)
SrcProceedings_strategy = st.builds(
    SrcProceedings,
)
jointPackage::SrcInProceedings_strategy = st.builds(
    jointPackage::SrcInProceedings,
)
jointPackage::SrcProceedings_strategy = st.builds(
    jointPackage::SrcProceedings,
)
jointPackage::SrcManual_strategy = st.builds(
    jointPackage::SrcManual,
)
jointPackage::SrcUnpublished_strategy = st.builds(
    jointPackage::SrcUnpublished,
    note=
        safe_text
)
jointPackage::SrcTechReport_strategy = st.builds(
    jointPackage::SrcTechReport,
)
SrcBibTeXEntry_strategy = st.builds(
    SrcBibTeXEntry,
)
jointPackage::SrcDatedEntry_strategy = st.builds(
    jointPackage::SrcDatedEntry,
    year=
        safe_text
)
jointPackage::SrcTitledEntry_strategy = st.builds(
    jointPackage::SrcTitledEntry,
    title=
        safe_text
)
jointPackage::SrcBookTitledEntry_strategy = st.builds(
    jointPackage::SrcBookTitledEntry,
    booktitle=
        safe_text
)
jointPackage::SrcMisc_strategy = st.builds(
    jointPackage::SrcMisc,
)
jointPackage::SrcAuthoredEntry_strategy = st.builds(
    jointPackage::SrcAuthoredEntry,
)
jointPackage::SrcBibTeXFile_strategy = st.builds(
    jointPackage::SrcBibTeXFile,
)
TrgDocBook_strategy = st.builds(
    TrgDocBook,
)
SrcMasterThesis_strategy = st.builds(
    SrcMasterThesis,
)
jointPackage::JointMM_strategy = st.builds(
    jointPackage::JointMM,
)

@given(instance=jointPackage::TrgPara_strategy)
@settings(max_examples=50)
def test_jointpackage::trgpara_instantiation(instance):
    assert isinstance(instance, jointPackage::TrgPara)

@given(instance=jointPackage::TrgPara_strategy)
def test_jointpackage::trgpara_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=jointPackage::TrgPara_strategy)
def test_jointpackage::trgpara_content_setter(instance):
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

@given(instance=jointPackage::TrgSect2_strategy)
@settings(max_examples=50)
def test_jointpackage::trgsect2_instantiation(instance):
    assert isinstance(instance, jointPackage::TrgSect2)

@given(instance=jointPackage::TrgSect1_strategy)
@settings(max_examples=50)
def test_jointpackage::trgsect1_instantiation(instance):
    assert isinstance(instance, jointPackage::TrgSect1)

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

@given(instance=jointPackage::TrgSection_strategy)
@settings(max_examples=50)
def test_jointpackage::trgsection_instantiation(instance):
    assert isinstance(instance, jointPackage::TrgSection)

@given(instance=jointPackage::TrgArticle_strategy)
@settings(max_examples=50)
def test_jointpackage::trgarticle_instantiation(instance):
    assert isinstance(instance, jointPackage::TrgArticle)

@given(instance=jointPackage::TrgTitledElement_strategy)
@settings(max_examples=50)
def test_jointpackage::trgtitledelement_instantiation(instance):
    assert isinstance(instance, jointPackage::TrgTitledElement)

@given(instance=jointPackage::TrgTitledElement_strategy)
def test_jointpackage::trgtitledelement_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=jointPackage::TrgTitledElement_strategy)
def test_jointpackage::trgtitledelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=TrgArticle_strategy)
@settings(max_examples=50)
def test_trgarticle_instantiation(instance):
    assert isinstance(instance, TrgArticle)

@given(instance=jointPackage::TrgBook_strategy)
@settings(max_examples=50)
def test_jointpackage::trgbook_instantiation(instance):
    assert isinstance(instance, jointPackage::TrgBook)

@given(instance=TrgBook_strategy)
@settings(max_examples=50)
def test_trgbook_instantiation(instance):
    assert isinstance(instance, TrgBook)

@given(instance=jointPackage::TrgDocBook_strategy)
@settings(max_examples=50)
def test_jointpackage::trgdocbook_instantiation(instance):
    assert isinstance(instance, jointPackage::TrgDocBook)

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

@given(instance=jointPackage::SrcThesisEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::srcthesisentry_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcThesisEntry)

@given(instance=jointPackage::SrcThesisEntry_strategy)
def test_jointpackage::srcthesisentry_school_type(instance):
    assert isinstance(instance.school, str)


@given(instance=jointPackage::SrcThesisEntry_strategy)
def test_jointpackage::srcthesisentry_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original

@given(instance=jointPackage::SrcArticle_strategy)
@settings(max_examples=50)
def test_jointpackage::srcarticle_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcArticle)

@given(instance=jointPackage::SrcArticle_strategy)
def test_jointpackage::srcarticle_journal_type(instance):
    assert isinstance(instance.journal, str)


@given(instance=jointPackage::SrcArticle_strategy)
def test_jointpackage::srcarticle_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original

@given(instance=SrcAuthor_strategy)
@settings(max_examples=50)
def test_srcauthor_instantiation(instance):
    assert isinstance(instance, SrcAuthor)

@given(instance=jointPackage::SrcBibTeXEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::srcbibtexentry_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcBibTeXEntry)

@given(instance=jointPackage::SrcBibTeXEntry_strategy)
def test_jointpackage::srcbibtexentry_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=jointPackage::SrcBibTeXEntry_strategy)
def test_jointpackage::srcbibtexentry_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=jointPackage::SrcAuthor_strategy)
@settings(max_examples=50)
def test_jointpackage::srcauthor_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcAuthor)

@given(instance=jointPackage::SrcAuthor_strategy)
def test_jointpackage::srcauthor_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=jointPackage::SrcAuthor_strategy)
def test_jointpackage::srcauthor_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=SrcThesisEntry_strategy)
@settings(max_examples=50)
def test_srcthesisentry_instantiation(instance):
    assert isinstance(instance, SrcThesisEntry)

@given(instance=jointPackage::SrcMasterThesis_strategy)
@settings(max_examples=50)
def test_jointpackage::srcmasterthesis_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcMasterThesis)

@given(instance=jointPackage::SrcPhDThesis_strategy)
@settings(max_examples=50)
def test_jointpackage::srcphdthesis_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcPhDThesis)

@given(instance=SrcBook_strategy)
@settings(max_examples=50)
def test_srcbook_instantiation(instance):
    assert isinstance(instance, SrcBook)

@given(instance=jointPackage::SrcInBook_strategy)
@settings(max_examples=50)
def test_jointpackage::srcinbook_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcInBook)

@given(instance=jointPackage::SrcInBook_strategy)
def test_jointpackage::srcinbook_chapter_type(instance):
    assert isinstance(instance.chapter, int)


@given(instance=jointPackage::SrcInBook_strategy)
def test_jointpackage::srcinbook_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original

@given(instance=jointPackage::SrcBook_strategy)
@settings(max_examples=50)
def test_jointpackage::srcbook_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcBook)

@given(instance=jointPackage::SrcBook_strategy)
def test_jointpackage::srcbook_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=jointPackage::SrcBook_strategy)
def test_jointpackage::srcbook_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=jointPackage::SrcBooklet_strategy)
@settings(max_examples=50)
def test_jointpackage::srcbooklet_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcBooklet)

@given(instance=SrcBookTitledEntry_strategy)
@settings(max_examples=50)
def test_srcbooktitledentry_instantiation(instance):
    assert isinstance(instance, SrcBookTitledEntry)

@given(instance=jointPackage::SrcInCollection_strategy)
@settings(max_examples=50)
def test_jointpackage::srcincollection_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcInCollection)

@given(instance=SrcProceedings_strategy)
@settings(max_examples=50)
def test_srcproceedings_instantiation(instance):
    assert isinstance(instance, SrcProceedings)

@given(instance=jointPackage::SrcInProceedings_strategy)
@settings(max_examples=50)
def test_jointpackage::srcinproceedings_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcInProceedings)

@given(instance=jointPackage::SrcProceedings_strategy)
@settings(max_examples=50)
def test_jointpackage::srcproceedings_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcProceedings)

@given(instance=jointPackage::SrcManual_strategy)
@settings(max_examples=50)
def test_jointpackage::srcmanual_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcManual)

@given(instance=jointPackage::SrcUnpublished_strategy)
@settings(max_examples=50)
def test_jointpackage::srcunpublished_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcUnpublished)

@given(instance=jointPackage::SrcUnpublished_strategy)
def test_jointpackage::srcunpublished_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=jointPackage::SrcUnpublished_strategy)
def test_jointpackage::srcunpublished_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=jointPackage::SrcTechReport_strategy)
@settings(max_examples=50)
def test_jointpackage::srctechreport_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcTechReport)

@given(instance=SrcBibTeXEntry_strategy)
@settings(max_examples=50)
def test_srcbibtexentry_instantiation(instance):
    assert isinstance(instance, SrcBibTeXEntry)

@given(instance=jointPackage::SrcDatedEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::srcdatedentry_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcDatedEntry)

@given(instance=jointPackage::SrcDatedEntry_strategy)
def test_jointpackage::srcdatedentry_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=jointPackage::SrcDatedEntry_strategy)
def test_jointpackage::srcdatedentry_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=jointPackage::SrcTitledEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::srctitledentry_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcTitledEntry)

@given(instance=jointPackage::SrcTitledEntry_strategy)
def test_jointpackage::srctitledentry_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=jointPackage::SrcTitledEntry_strategy)
def test_jointpackage::srctitledentry_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=jointPackage::SrcBookTitledEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::srcbooktitledentry_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcBookTitledEntry)

@given(instance=jointPackage::SrcBookTitledEntry_strategy)
def test_jointpackage::srcbooktitledentry_booktitle_type(instance):
    assert isinstance(instance.booktitle, str)


@given(instance=jointPackage::SrcBookTitledEntry_strategy)
def test_jointpackage::srcbooktitledentry_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=jointPackage::SrcMisc_strategy)
@settings(max_examples=50)
def test_jointpackage::srcmisc_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcMisc)

@given(instance=jointPackage::SrcAuthoredEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::srcauthoredentry_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcAuthoredEntry)

@given(instance=jointPackage::SrcBibTeXFile_strategy)
@settings(max_examples=50)
def test_jointpackage::srcbibtexfile_instantiation(instance):
    assert isinstance(instance, jointPackage::SrcBibTeXFile)

@given(instance=TrgDocBook_strategy)
@settings(max_examples=50)
def test_trgdocbook_instantiation(instance):
    assert isinstance(instance, TrgDocBook)

@given(instance=SrcMasterThesis_strategy)
@settings(max_examples=50)
def test_srcmasterthesis_instantiation(instance):
    assert isinstance(instance, SrcMasterThesis)

@given(instance=jointPackage::JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage::jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage::JointMM)
