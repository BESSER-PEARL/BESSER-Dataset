import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    jointPackage::BibTeX2DocBook::TrgPara,
    SrcAuthor,
    jointPackage::BibTeX2DocBook::SrcBibTeXEntry,
    jointPackage::BibTeX2DocBook::SrcAuthor,
    TrgSect2,
    TrgSection,
    jointPackage::BibTeX2DocBook::TrgSect2,
    jointPackage::BibTeX2DocBook::TrgSect1,
    TrgPara,
    TrgSect1,
    TrgTitledElement,
    jointPackage::BibTeX2DocBook::TrgSection,
    jointPackage::BibTeX2DocBook::TrgArticle,
    jointPackage::BibTeX2DocBook::TrgTitledElement,
    TrgArticle,
    jointPackage::BibTeX2DocBook::TrgBook,
    TrgBook,
    jointPackage::BibTeX2DocBook::TrgDocBook,
    SrcTitledEntry,
    SrcDatedEntry,
    SrcAuthoredEntry,
    jointPackage::BibTeX2DocBook::SrcThesisEntry,
    jointPackage::BibTeX2DocBook::SrcArticle,
    SrcBibTeXEntry,
    jointPackage::BibTeX2DocBook::SrcTitledEntry,
    jointPackage::BibTeX2DocBook::SrcDatedEntry,
    jointPackage::BibTeX2DocBook::SrcAuthoredEntry,
    jointPackage::BibTeX2DocBook::SrcBookTitledEntry,
    jointPackage::BibTeX2DocBook::SrcMisc,
    jointPackage::BibTeX2DocBook::SrcBibTeXFile,
    TrgDocBook,
    SrcMasterThesis,
    jointPackage::BibTeX2DocBook::JointMM,
    SrcThesisEntry,
    jointPackage::BibTeX2DocBook::SrcMasterThesis,
    jointPackage::BibTeX2DocBook::SrcPhDThesis,
    SrcBook,
    jointPackage::BibTeX2DocBook::SrcInBook,
    jointPackage::BibTeX2DocBook::SrcBook,
    jointPackage::BibTeX2DocBook::SrcBooklet,
    SrcBookTitledEntry,
    jointPackage::BibTeX2DocBook::SrcInCollection,
    SrcProceedings,
    jointPackage::BibTeX2DocBook::SrcInProceedings,
    jointPackage::BibTeX2DocBook::SrcProceedings,
    jointPackage::BibTeX2DocBook::SrcManual,
    jointPackage::BibTeX2DocBook::SrcUnpublished,
    jointPackage::BibTeX2DocBook::SrcTechReport,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_jointpackage::bibtex2docbook::trgpara_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::TrgPara)


def test_jointpackage::bibtex2docbook::trgpara_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::TrgPara.__init__)


def test_jointpackage::bibtex2docbook::trgpara_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::TrgPara.__init__)
    params = list(sig.parameters.keys())
    assert "content" in params, "Missing parameter 'content'"

def test_jointpackage::bibtex2docbook::trgpara_has_content():
    assert hasattr(jointPackage::BibTeX2DocBook::TrgPara, "content")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::TrgPara.__mro__:
        if "content" in klass.__dict__:
            descriptor = klass.__dict__["content"]
            break
    assert isinstance(descriptor, property)



def test_srcauthor_is_not_abstract():
    assert not inspect.isabstract(SrcAuthor)


def test_srcauthor_constructor_exists():
    assert callable(SrcAuthor.__init__)


def test_srcauthor_constructor_args():
    sig = inspect.signature(SrcAuthor.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcbibtexentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcBibTeXEntry)


def test_jointpackage::bibtex2docbook::srcbibtexentry_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcBibTeXEntry.__init__)


def test_jointpackage::bibtex2docbook::srcbibtexentry_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcBibTeXEntry.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_jointpackage::bibtex2docbook::srcbibtexentry_has_id():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcBibTeXEntry, "id")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcBibTeXEntry.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::bibtex2docbook::srcauthor_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcAuthor)


def test_jointpackage::bibtex2docbook::srcauthor_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcAuthor.__init__)


def test_jointpackage::bibtex2docbook::srcauthor_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcAuthor.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"

def test_jointpackage::bibtex2docbook::srcauthor_has_author():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcAuthor, "author")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcAuthor.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
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



def test_jointpackage::bibtex2docbook::trgsect2_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::TrgSect2)


def test_jointpackage::bibtex2docbook::trgsect2_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::TrgSect2.__init__)


def test_jointpackage::bibtex2docbook::trgsect2_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::TrgSect2.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::trgsect1_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::TrgSect1)


def test_jointpackage::bibtex2docbook::trgsect1_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::TrgSect1.__init__)


def test_jointpackage::bibtex2docbook::trgsect1_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::TrgSect1.__init__)
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



def test_jointpackage::bibtex2docbook::trgsection_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::TrgSection)


def test_jointpackage::bibtex2docbook::trgsection_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::TrgSection.__init__)


def test_jointpackage::bibtex2docbook::trgsection_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::TrgSection.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::trgarticle_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::TrgArticle)


def test_jointpackage::bibtex2docbook::trgarticle_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::TrgArticle.__init__)


def test_jointpackage::bibtex2docbook::trgarticle_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::TrgArticle.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::trgtitledelement_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::TrgTitledElement)


def test_jointpackage::bibtex2docbook::trgtitledelement_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::TrgTitledElement.__init__)


def test_jointpackage::bibtex2docbook::trgtitledelement_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::TrgTitledElement.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_jointpackage::bibtex2docbook::trgtitledelement_has_title():
    assert hasattr(jointPackage::BibTeX2DocBook::TrgTitledElement, "title")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::TrgTitledElement.__mro__:
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



def test_jointpackage::bibtex2docbook::trgbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::TrgBook)


def test_jointpackage::bibtex2docbook::trgbook_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::TrgBook.__init__)


def test_jointpackage::bibtex2docbook::trgbook_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::TrgBook.__init__)
    params = list(sig.parameters.keys())



def test_trgbook_is_not_abstract():
    assert not inspect.isabstract(TrgBook)


def test_trgbook_constructor_exists():
    assert callable(TrgBook.__init__)


def test_trgbook_constructor_args():
    sig = inspect.signature(TrgBook.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::trgdocbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::TrgDocBook)


def test_jointpackage::bibtex2docbook::trgdocbook_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::TrgDocBook.__init__)


def test_jointpackage::bibtex2docbook::trgdocbook_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::TrgDocBook.__init__)
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



def test_jointpackage::bibtex2docbook::srcthesisentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcThesisEntry)


def test_jointpackage::bibtex2docbook::srcthesisentry_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcThesisEntry.__init__)


def test_jointpackage::bibtex2docbook::srcthesisentry_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcThesisEntry.__init__)
    params = list(sig.parameters.keys())
    assert "school" in params, "Missing parameter 'school'"

def test_jointpackage::bibtex2docbook::srcthesisentry_has_school():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcThesisEntry, "school")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcThesisEntry.__mro__:
        if "school" in klass.__dict__:
            descriptor = klass.__dict__["school"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::bibtex2docbook::srcarticle_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcArticle)


def test_jointpackage::bibtex2docbook::srcarticle_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcArticle.__init__)


def test_jointpackage::bibtex2docbook::srcarticle_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcArticle.__init__)
    params = list(sig.parameters.keys())
    assert "journal" in params, "Missing parameter 'journal'"

def test_jointpackage::bibtex2docbook::srcarticle_has_journal():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcArticle, "journal")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcArticle.__mro__:
        if "journal" in klass.__dict__:
            descriptor = klass.__dict__["journal"]
            break
    assert isinstance(descriptor, property)



def test_srcbibtexentry_is_not_abstract():
    assert not inspect.isabstract(SrcBibTeXEntry)


def test_srcbibtexentry_constructor_exists():
    assert callable(SrcBibTeXEntry.__init__)


def test_srcbibtexentry_constructor_args():
    sig = inspect.signature(SrcBibTeXEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srctitledentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcTitledEntry)


def test_jointpackage::bibtex2docbook::srctitledentry_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcTitledEntry.__init__)


def test_jointpackage::bibtex2docbook::srctitledentry_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcTitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_jointpackage::bibtex2docbook::srctitledentry_has_title():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcTitledEntry, "title")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcTitledEntry.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::bibtex2docbook::srcdatedentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcDatedEntry)


def test_jointpackage::bibtex2docbook::srcdatedentry_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcDatedEntry.__init__)


def test_jointpackage::bibtex2docbook::srcdatedentry_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcDatedEntry.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"

def test_jointpackage::bibtex2docbook::srcdatedentry_has_year():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcDatedEntry, "year")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcDatedEntry.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::bibtex2docbook::srcauthoredentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcAuthoredEntry)


def test_jointpackage::bibtex2docbook::srcauthoredentry_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcAuthoredEntry.__init__)


def test_jointpackage::bibtex2docbook::srcauthoredentry_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcAuthoredEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcbooktitledentry_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcBookTitledEntry)


def test_jointpackage::bibtex2docbook::srcbooktitledentry_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcBookTitledEntry.__init__)


def test_jointpackage::bibtex2docbook::srcbooktitledentry_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcBookTitledEntry.__init__)
    params = list(sig.parameters.keys())
    assert "booktitle" in params, "Missing parameter 'booktitle'"

def test_jointpackage::bibtex2docbook::srcbooktitledentry_has_booktitle():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcBookTitledEntry, "booktitle")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcBookTitledEntry.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::bibtex2docbook::srcmisc_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcMisc)


def test_jointpackage::bibtex2docbook::srcmisc_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcMisc.__init__)


def test_jointpackage::bibtex2docbook::srcmisc_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcMisc.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcbibtexfile_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcBibTeXFile)


def test_jointpackage::bibtex2docbook::srcbibtexfile_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcBibTeXFile.__init__)


def test_jointpackage::bibtex2docbook::srcbibtexfile_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcBibTeXFile.__init__)
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



def test_jointpackage::bibtex2docbook::jointmm_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::JointMM)


def test_jointpackage::bibtex2docbook::jointmm_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::JointMM.__init__)


def test_jointpackage::bibtex2docbook::jointmm_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::JointMM.__init__)
    params = list(sig.parameters.keys())



def test_srcthesisentry_is_not_abstract():
    assert not inspect.isabstract(SrcThesisEntry)


def test_srcthesisentry_constructor_exists():
    assert callable(SrcThesisEntry.__init__)


def test_srcthesisentry_constructor_args():
    sig = inspect.signature(SrcThesisEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcmasterthesis_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcMasterThesis)


def test_jointpackage::bibtex2docbook::srcmasterthesis_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcMasterThesis.__init__)


def test_jointpackage::bibtex2docbook::srcmasterthesis_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcMasterThesis.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcphdthesis_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcPhDThesis)


def test_jointpackage::bibtex2docbook::srcphdthesis_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcPhDThesis.__init__)


def test_jointpackage::bibtex2docbook::srcphdthesis_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcPhDThesis.__init__)
    params = list(sig.parameters.keys())



def test_srcbook_is_not_abstract():
    assert not inspect.isabstract(SrcBook)


def test_srcbook_constructor_exists():
    assert callable(SrcBook.__init__)


def test_srcbook_constructor_args():
    sig = inspect.signature(SrcBook.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcinbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcInBook)


def test_jointpackage::bibtex2docbook::srcinbook_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcInBook.__init__)


def test_jointpackage::bibtex2docbook::srcinbook_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcInBook.__init__)
    params = list(sig.parameters.keys())
    assert "chapter" in params, "Missing parameter 'chapter'"

def test_jointpackage::bibtex2docbook::srcinbook_has_chapter():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcInBook, "chapter")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcInBook.__mro__:
        if "chapter" in klass.__dict__:
            descriptor = klass.__dict__["chapter"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::bibtex2docbook::srcbook_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcBook)


def test_jointpackage::bibtex2docbook::srcbook_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcBook.__init__)


def test_jointpackage::bibtex2docbook::srcbook_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcBook.__init__)
    params = list(sig.parameters.keys())
    assert "publisher" in params, "Missing parameter 'publisher'"

def test_jointpackage::bibtex2docbook::srcbook_has_publisher():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcBook, "publisher")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcBook.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::bibtex2docbook::srcbooklet_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcBooklet)


def test_jointpackage::bibtex2docbook::srcbooklet_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcBooklet.__init__)


def test_jointpackage::bibtex2docbook::srcbooklet_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcBooklet.__init__)
    params = list(sig.parameters.keys())



def test_srcbooktitledentry_is_not_abstract():
    assert not inspect.isabstract(SrcBookTitledEntry)


def test_srcbooktitledentry_constructor_exists():
    assert callable(SrcBookTitledEntry.__init__)


def test_srcbooktitledentry_constructor_args():
    sig = inspect.signature(SrcBookTitledEntry.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcincollection_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcInCollection)


def test_jointpackage::bibtex2docbook::srcincollection_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcInCollection.__init__)


def test_jointpackage::bibtex2docbook::srcincollection_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcInCollection.__init__)
    params = list(sig.parameters.keys())



def test_srcproceedings_is_not_abstract():
    assert not inspect.isabstract(SrcProceedings)


def test_srcproceedings_constructor_exists():
    assert callable(SrcProceedings.__init__)


def test_srcproceedings_constructor_args():
    sig = inspect.signature(SrcProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcinproceedings_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcInProceedings)


def test_jointpackage::bibtex2docbook::srcinproceedings_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcInProceedings.__init__)


def test_jointpackage::bibtex2docbook::srcinproceedings_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcInProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcproceedings_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcProceedings)


def test_jointpackage::bibtex2docbook::srcproceedings_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcProceedings.__init__)


def test_jointpackage::bibtex2docbook::srcproceedings_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcProceedings.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcmanual_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcManual)


def test_jointpackage::bibtex2docbook::srcmanual_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcManual.__init__)


def test_jointpackage::bibtex2docbook::srcmanual_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcManual.__init__)
    params = list(sig.parameters.keys())



def test_jointpackage::bibtex2docbook::srcunpublished_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcUnpublished)


def test_jointpackage::bibtex2docbook::srcunpublished_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcUnpublished.__init__)


def test_jointpackage::bibtex2docbook::srcunpublished_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcUnpublished.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"

def test_jointpackage::bibtex2docbook::srcunpublished_has_note():
    assert hasattr(jointPackage::BibTeX2DocBook::SrcUnpublished, "note")
    descriptor = None
    for klass in jointPackage::BibTeX2DocBook::SrcUnpublished.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_jointpackage::bibtex2docbook::srctechreport_is_not_abstract():
    assert not inspect.isabstract(jointPackage::BibTeX2DocBook::SrcTechReport)


def test_jointpackage::bibtex2docbook::srctechreport_constructor_exists():
    assert callable(jointPackage::BibTeX2DocBook::SrcTechReport.__init__)


def test_jointpackage::bibtex2docbook::srctechreport_constructor_args():
    sig = inspect.signature(jointPackage::BibTeX2DocBook::SrcTechReport.__init__)
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
jointPackage::BibTeX2DocBook::TrgPara_strategy = st.builds(
    jointPackage::BibTeX2DocBook::TrgPara,
    content=
        safe_text
)
SrcAuthor_strategy = st.builds(
    SrcAuthor,
)
jointPackage::BibTeX2DocBook::SrcBibTeXEntry_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcBibTeXEntry,
    id=
        safe_text
)
jointPackage::BibTeX2DocBook::SrcAuthor_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcAuthor,
    author=
        safe_text
)
TrgSect2_strategy = st.builds(
    TrgSect2,
)
TrgSection_strategy = st.builds(
    TrgSection,
)
jointPackage::BibTeX2DocBook::TrgSect2_strategy = st.builds(
    jointPackage::BibTeX2DocBook::TrgSect2,
)
jointPackage::BibTeX2DocBook::TrgSect1_strategy = st.builds(
    jointPackage::BibTeX2DocBook::TrgSect1,
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
jointPackage::BibTeX2DocBook::TrgSection_strategy = st.builds(
    jointPackage::BibTeX2DocBook::TrgSection,
)
jointPackage::BibTeX2DocBook::TrgArticle_strategy = st.builds(
    jointPackage::BibTeX2DocBook::TrgArticle,
)
jointPackage::BibTeX2DocBook::TrgTitledElement_strategy = st.builds(
    jointPackage::BibTeX2DocBook::TrgTitledElement,
    title=
        safe_text
)
TrgArticle_strategy = st.builds(
    TrgArticle,
)
jointPackage::BibTeX2DocBook::TrgBook_strategy = st.builds(
    jointPackage::BibTeX2DocBook::TrgBook,
)
TrgBook_strategy = st.builds(
    TrgBook,
)
jointPackage::BibTeX2DocBook::TrgDocBook_strategy = st.builds(
    jointPackage::BibTeX2DocBook::TrgDocBook,
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
jointPackage::BibTeX2DocBook::SrcThesisEntry_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcThesisEntry,
    school=
        safe_text
)
jointPackage::BibTeX2DocBook::SrcArticle_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcArticle,
    journal=
        safe_text
)
SrcBibTeXEntry_strategy = st.builds(
    SrcBibTeXEntry,
)
jointPackage::BibTeX2DocBook::SrcTitledEntry_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcTitledEntry,
    title=
        safe_text
)
jointPackage::BibTeX2DocBook::SrcDatedEntry_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcDatedEntry,
    year=
        safe_text
)
jointPackage::BibTeX2DocBook::SrcAuthoredEntry_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcAuthoredEntry,
)
jointPackage::BibTeX2DocBook::SrcBookTitledEntry_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcBookTitledEntry,
    booktitle=
        safe_text
)
jointPackage::BibTeX2DocBook::SrcMisc_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcMisc,
)
jointPackage::BibTeX2DocBook::SrcBibTeXFile_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcBibTeXFile,
)
TrgDocBook_strategy = st.builds(
    TrgDocBook,
)
SrcMasterThesis_strategy = st.builds(
    SrcMasterThesis,
)
jointPackage::BibTeX2DocBook::JointMM_strategy = st.builds(
    jointPackage::BibTeX2DocBook::JointMM,
)
SrcThesisEntry_strategy = st.builds(
    SrcThesisEntry,
)
jointPackage::BibTeX2DocBook::SrcMasterThesis_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcMasterThesis,
)
jointPackage::BibTeX2DocBook::SrcPhDThesis_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcPhDThesis,
)
SrcBook_strategy = st.builds(
    SrcBook,
)
jointPackage::BibTeX2DocBook::SrcInBook_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcInBook,
    chapter=
        st.integers()
)
jointPackage::BibTeX2DocBook::SrcBook_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcBook,
    publisher=
        safe_text
)
jointPackage::BibTeX2DocBook::SrcBooklet_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcBooklet,
)
SrcBookTitledEntry_strategy = st.builds(
    SrcBookTitledEntry,
)
jointPackage::BibTeX2DocBook::SrcInCollection_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcInCollection,
)
SrcProceedings_strategy = st.builds(
    SrcProceedings,
)
jointPackage::BibTeX2DocBook::SrcInProceedings_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcInProceedings,
)
jointPackage::BibTeX2DocBook::SrcProceedings_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcProceedings,
)
jointPackage::BibTeX2DocBook::SrcManual_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcManual,
)
jointPackage::BibTeX2DocBook::SrcUnpublished_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcUnpublished,
    note=
        safe_text
)
jointPackage::BibTeX2DocBook::SrcTechReport_strategy = st.builds(
    jointPackage::BibTeX2DocBook::SrcTechReport,
)

@given(instance=jointPackage::BibTeX2DocBook::TrgPara_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::trgpara_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::TrgPara)

@given(instance=jointPackage::BibTeX2DocBook::TrgPara_strategy)
def test_jointpackage::bibtex2docbook::trgpara_content_type(instance):
    assert isinstance(instance.content, str)


@given(instance=jointPackage::BibTeX2DocBook::TrgPara_strategy)
def test_jointpackage::bibtex2docbook::trgpara_content_setter(instance):
    original = instance.content
    instance.content = original
    assert instance.content == original

@given(instance=SrcAuthor_strategy)
@settings(max_examples=50)
def test_srcauthor_instantiation(instance):
    assert isinstance(instance, SrcAuthor)

@given(instance=jointPackage::BibTeX2DocBook::SrcBibTeXEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcbibtexentry_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcBibTeXEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcBibTeXEntry_strategy)
def test_jointpackage::bibtex2docbook::srcbibtexentry_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcBibTeXEntry_strategy)
def test_jointpackage::bibtex2docbook::srcbibtexentry_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=jointPackage::BibTeX2DocBook::SrcAuthor_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcauthor_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcAuthor)

@given(instance=jointPackage::BibTeX2DocBook::SrcAuthor_strategy)
def test_jointpackage::bibtex2docbook::srcauthor_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcAuthor_strategy)
def test_jointpackage::bibtex2docbook::srcauthor_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=TrgSect2_strategy)
@settings(max_examples=50)
def test_trgsect2_instantiation(instance):
    assert isinstance(instance, TrgSect2)

@given(instance=TrgSection_strategy)
@settings(max_examples=50)
def test_trgsection_instantiation(instance):
    assert isinstance(instance, TrgSection)

@given(instance=jointPackage::BibTeX2DocBook::TrgSect2_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::trgsect2_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::TrgSect2)

@given(instance=jointPackage::BibTeX2DocBook::TrgSect1_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::trgsect1_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::TrgSect1)

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

@given(instance=jointPackage::BibTeX2DocBook::TrgSection_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::trgsection_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::TrgSection)

@given(instance=jointPackage::BibTeX2DocBook::TrgArticle_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::trgarticle_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::TrgArticle)

@given(instance=jointPackage::BibTeX2DocBook::TrgTitledElement_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::trgtitledelement_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::TrgTitledElement)

@given(instance=jointPackage::BibTeX2DocBook::TrgTitledElement_strategy)
def test_jointpackage::bibtex2docbook::trgtitledelement_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=jointPackage::BibTeX2DocBook::TrgTitledElement_strategy)
def test_jointpackage::bibtex2docbook::trgtitledelement_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=TrgArticle_strategy)
@settings(max_examples=50)
def test_trgarticle_instantiation(instance):
    assert isinstance(instance, TrgArticle)

@given(instance=jointPackage::BibTeX2DocBook::TrgBook_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::trgbook_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::TrgBook)

@given(instance=TrgBook_strategy)
@settings(max_examples=50)
def test_trgbook_instantiation(instance):
    assert isinstance(instance, TrgBook)

@given(instance=jointPackage::BibTeX2DocBook::TrgDocBook_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::trgdocbook_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::TrgDocBook)

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

@given(instance=jointPackage::BibTeX2DocBook::SrcThesisEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcthesisentry_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcThesisEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcThesisEntry_strategy)
def test_jointpackage::bibtex2docbook::srcthesisentry_school_type(instance):
    assert isinstance(instance.school, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcThesisEntry_strategy)
def test_jointpackage::bibtex2docbook::srcthesisentry_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original

@given(instance=jointPackage::BibTeX2DocBook::SrcArticle_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcarticle_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcArticle)

@given(instance=jointPackage::BibTeX2DocBook::SrcArticle_strategy)
def test_jointpackage::bibtex2docbook::srcarticle_journal_type(instance):
    assert isinstance(instance.journal, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcArticle_strategy)
def test_jointpackage::bibtex2docbook::srcarticle_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original

@given(instance=SrcBibTeXEntry_strategy)
@settings(max_examples=50)
def test_srcbibtexentry_instantiation(instance):
    assert isinstance(instance, SrcBibTeXEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcTitledEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srctitledentry_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcTitledEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcTitledEntry_strategy)
def test_jointpackage::bibtex2docbook::srctitledentry_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcTitledEntry_strategy)
def test_jointpackage::bibtex2docbook::srctitledentry_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=jointPackage::BibTeX2DocBook::SrcDatedEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcdatedentry_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcDatedEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcDatedEntry_strategy)
def test_jointpackage::bibtex2docbook::srcdatedentry_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcDatedEntry_strategy)
def test_jointpackage::bibtex2docbook::srcdatedentry_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=jointPackage::BibTeX2DocBook::SrcAuthoredEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcauthoredentry_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcAuthoredEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcBookTitledEntry_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcbooktitledentry_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcBookTitledEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcBookTitledEntry_strategy)
def test_jointpackage::bibtex2docbook::srcbooktitledentry_booktitle_type(instance):
    assert isinstance(instance.booktitle, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcBookTitledEntry_strategy)
def test_jointpackage::bibtex2docbook::srcbooktitledentry_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=jointPackage::BibTeX2DocBook::SrcMisc_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcmisc_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcMisc)

@given(instance=jointPackage::BibTeX2DocBook::SrcBibTeXFile_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcbibtexfile_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcBibTeXFile)

@given(instance=TrgDocBook_strategy)
@settings(max_examples=50)
def test_trgdocbook_instantiation(instance):
    assert isinstance(instance, TrgDocBook)

@given(instance=SrcMasterThesis_strategy)
@settings(max_examples=50)
def test_srcmasterthesis_instantiation(instance):
    assert isinstance(instance, SrcMasterThesis)

@given(instance=jointPackage::BibTeX2DocBook::JointMM_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::jointmm_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::JointMM)

@given(instance=SrcThesisEntry_strategy)
@settings(max_examples=50)
def test_srcthesisentry_instantiation(instance):
    assert isinstance(instance, SrcThesisEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcMasterThesis_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcmasterthesis_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcMasterThesis)

@given(instance=jointPackage::BibTeX2DocBook::SrcPhDThesis_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcphdthesis_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcPhDThesis)

@given(instance=SrcBook_strategy)
@settings(max_examples=50)
def test_srcbook_instantiation(instance):
    assert isinstance(instance, SrcBook)

@given(instance=jointPackage::BibTeX2DocBook::SrcInBook_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcinbook_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcInBook)

@given(instance=jointPackage::BibTeX2DocBook::SrcInBook_strategy)
def test_jointpackage::bibtex2docbook::srcinbook_chapter_type(instance):
    assert isinstance(instance.chapter, int)


@given(instance=jointPackage::BibTeX2DocBook::SrcInBook_strategy)
def test_jointpackage::bibtex2docbook::srcinbook_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original

@given(instance=jointPackage::BibTeX2DocBook::SrcBook_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcbook_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcBook)

@given(instance=jointPackage::BibTeX2DocBook::SrcBook_strategy)
def test_jointpackage::bibtex2docbook::srcbook_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcBook_strategy)
def test_jointpackage::bibtex2docbook::srcbook_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=jointPackage::BibTeX2DocBook::SrcBooklet_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcbooklet_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcBooklet)

@given(instance=SrcBookTitledEntry_strategy)
@settings(max_examples=50)
def test_srcbooktitledentry_instantiation(instance):
    assert isinstance(instance, SrcBookTitledEntry)

@given(instance=jointPackage::BibTeX2DocBook::SrcInCollection_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcincollection_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcInCollection)

@given(instance=SrcProceedings_strategy)
@settings(max_examples=50)
def test_srcproceedings_instantiation(instance):
    assert isinstance(instance, SrcProceedings)

@given(instance=jointPackage::BibTeX2DocBook::SrcInProceedings_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcinproceedings_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcInProceedings)

@given(instance=jointPackage::BibTeX2DocBook::SrcProceedings_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcproceedings_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcProceedings)

@given(instance=jointPackage::BibTeX2DocBook::SrcManual_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcmanual_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcManual)

@given(instance=jointPackage::BibTeX2DocBook::SrcUnpublished_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srcunpublished_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcUnpublished)

@given(instance=jointPackage::BibTeX2DocBook::SrcUnpublished_strategy)
def test_jointpackage::bibtex2docbook::srcunpublished_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=jointPackage::BibTeX2DocBook::SrcUnpublished_strategy)
def test_jointpackage::bibtex2docbook::srcunpublished_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=jointPackage::BibTeX2DocBook::SrcTechReport_strategy)
@settings(max_examples=50)
def test_jointpackage::bibtex2docbook::srctechreport_instantiation(instance):
    assert isinstance(instance, jointPackage::BibTeX2DocBook::SrcTechReport)
