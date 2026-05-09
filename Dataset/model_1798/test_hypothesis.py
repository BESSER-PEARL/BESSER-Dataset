import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    bibtexml::ArticleType,
    bibtexml::FileType,
    bibtexml::EStringToStringMapEntry,
    bibtexml::DocumentRoot,
    BibTeXMLEntriesClass,
    bibtexml::BibTeXMLEntryType,
    bibtexml::MiscType,
    bibtexml::UnpublishedType,
    bibtexml::ConferenceType,
    bibtexml::InproceedingsType,
    bibtexml::ProceedingsType,
    bibtexml::IncollectionType,
    bibtexml::InbookType,
    bibtexml::PhdthesisType,
    bibtexml::MastersthesisType,
    bibtexml::TechreportType,
    bibtexml::ManualType,
    bibtexml::BookletType,
    bibtexml::BookType,
    bibtexml::BibTeXMLEntriesClass,
    MonthStringType,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_bibtexml::articletype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::ArticleType)


def test_bibtexml::articletype_constructor_exists():
    assert callable(bibtexml::ArticleType.__init__)


def test_bibtexml::articletype_constructor_args():
    sig = inspect.signature(bibtexml::ArticleType.__init__)
    params = list(sig.parameters.keys())
    assert "volume" in params, "Missing parameter 'volume'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "url" in params, "Missing parameter 'url'"
    assert "note" in params, "Missing parameter 'note'"
    assert "author" in params, "Missing parameter 'author'"
    assert "journal" in params, "Missing parameter 'journal'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "month" in params, "Missing parameter 'month'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "key" in params, "Missing parameter 'key'"
    assert "year" in params, "Missing parameter 'year'"
    assert "number" in params, "Missing parameter 'number'"
    assert "title" in params, "Missing parameter 'title'"

def test_bibtexml::articletype_has_volume():
    assert hasattr(bibtexml::ArticleType, "volume")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_doi():
    assert hasattr(bibtexml::ArticleType, "doi")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_url():
    assert hasattr(bibtexml::ArticleType, "url")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_note():
    assert hasattr(bibtexml::ArticleType, "note")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_author():
    assert hasattr(bibtexml::ArticleType, "author")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_journal():
    assert hasattr(bibtexml::ArticleType, "journal")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "journal" in klass.__dict__:
            descriptor = klass.__dict__["journal"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_pages():
    assert hasattr(bibtexml::ArticleType, "pages")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_month():
    assert hasattr(bibtexml::ArticleType, "month")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_crossref():
    assert hasattr(bibtexml::ArticleType, "crossref")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_key():
    assert hasattr(bibtexml::ArticleType, "key")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_year():
    assert hasattr(bibtexml::ArticleType, "year")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_number():
    assert hasattr(bibtexml::ArticleType, "number")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::articletype_has_title():
    assert hasattr(bibtexml::ArticleType, "title")
    descriptor = None
    for klass in bibtexml::ArticleType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::filetype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::FileType)


def test_bibtexml::filetype_constructor_exists():
    assert callable(bibtexml::FileType.__init__)


def test_bibtexml::filetype_constructor_args():
    sig = inspect.signature(bibtexml::FileType.__init__)
    params = list(sig.parameters.keys())



def test_bibtexml::estringtostringmapentry_is_not_abstract():
    assert not inspect.isabstract(bibtexml::EStringToStringMapEntry)


def test_bibtexml::estringtostringmapentry_constructor_exists():
    assert callable(bibtexml::EStringToStringMapEntry.__init__)


def test_bibtexml::estringtostringmapentry_constructor_args():
    sig = inspect.signature(bibtexml::EStringToStringMapEntry.__init__)
    params = list(sig.parameters.keys())



def test_bibtexml::documentroot_is_not_abstract():
    assert not inspect.isabstract(bibtexml::DocumentRoot)


def test_bibtexml::documentroot_constructor_exists():
    assert callable(bibtexml::DocumentRoot.__init__)


def test_bibtexml::documentroot_constructor_args():
    sig = inspect.signature(bibtexml::DocumentRoot.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "editor" in params, "Missing parameter 'editor'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "key" in params, "Missing parameter 'key'"
    assert "author" in params, "Missing parameter 'author'"
    assert "series" in params, "Missing parameter 'series'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "number" in params, "Missing parameter 'number'"
    assert "type" in params, "Missing parameter 'type'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "title" in params, "Missing parameter 'title'"
    assert "journal" in params, "Missing parameter 'journal'"
    assert "address" in params, "Missing parameter 'address'"
    assert "note" in params, "Missing parameter 'note'"
    assert "school" in params, "Missing parameter 'school'"
    assert "annote" in params, "Missing parameter 'annote'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "howpublished" in params, "Missing parameter 'howpublished'"
    assert "booktitle" in params, "Missing parameter 'booktitle'"
    assert "institution" in params, "Missing parameter 'institution'"
    assert "mixed" in params, "Missing parameter 'mixed'"
    assert "chapter" in params, "Missing parameter 'chapter'"
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "year" in params, "Missing parameter 'year'"
    assert "url" in params, "Missing parameter 'url'"
    assert "month" in params, "Missing parameter 'month'"

def test_bibtexml::documentroot_has_pages():
    assert hasattr(bibtexml::DocumentRoot, "pages")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_editor():
    assert hasattr(bibtexml::DocumentRoot, "editor")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "editor" in klass.__dict__:
            descriptor = klass.__dict__["editor"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_doi():
    assert hasattr(bibtexml::DocumentRoot, "doi")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_edition():
    assert hasattr(bibtexml::DocumentRoot, "edition")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_key():
    assert hasattr(bibtexml::DocumentRoot, "key")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_author():
    assert hasattr(bibtexml::DocumentRoot, "author")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_series():
    assert hasattr(bibtexml::DocumentRoot, "series")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_organization():
    assert hasattr(bibtexml::DocumentRoot, "organization")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_number():
    assert hasattr(bibtexml::DocumentRoot, "number")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_type():
    assert hasattr(bibtexml::DocumentRoot, "type")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_volume():
    assert hasattr(bibtexml::DocumentRoot, "volume")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_title():
    assert hasattr(bibtexml::DocumentRoot, "title")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_journal():
    assert hasattr(bibtexml::DocumentRoot, "journal")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "journal" in klass.__dict__:
            descriptor = klass.__dict__["journal"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_address():
    assert hasattr(bibtexml::DocumentRoot, "address")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_note():
    assert hasattr(bibtexml::DocumentRoot, "note")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_school():
    assert hasattr(bibtexml::DocumentRoot, "school")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "school" in klass.__dict__:
            descriptor = klass.__dict__["school"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_annote():
    assert hasattr(bibtexml::DocumentRoot, "annote")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "annote" in klass.__dict__:
            descriptor = klass.__dict__["annote"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_crossref():
    assert hasattr(bibtexml::DocumentRoot, "crossref")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_howpublished():
    assert hasattr(bibtexml::DocumentRoot, "howpublished")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "howpublished" in klass.__dict__:
            descriptor = klass.__dict__["howpublished"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_booktitle():
    assert hasattr(bibtexml::DocumentRoot, "booktitle")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_institution():
    assert hasattr(bibtexml::DocumentRoot, "institution")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "institution" in klass.__dict__:
            descriptor = klass.__dict__["institution"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_mixed():
    assert hasattr(bibtexml::DocumentRoot, "mixed")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "mixed" in klass.__dict__:
            descriptor = klass.__dict__["mixed"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_chapter():
    assert hasattr(bibtexml::DocumentRoot, "chapter")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "chapter" in klass.__dict__:
            descriptor = klass.__dict__["chapter"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_publisher():
    assert hasattr(bibtexml::DocumentRoot, "publisher")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_year():
    assert hasattr(bibtexml::DocumentRoot, "year")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_url():
    assert hasattr(bibtexml::DocumentRoot, "url")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::documentroot_has_month():
    assert hasattr(bibtexml::DocumentRoot, "month")
    descriptor = None
    for klass in bibtexml::DocumentRoot.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)



def test_bibtexmlentriesclass_is_not_abstract():
    assert not inspect.isabstract(BibTeXMLEntriesClass)


def test_bibtexmlentriesclass_constructor_exists():
    assert callable(BibTeXMLEntriesClass.__init__)


def test_bibtexmlentriesclass_constructor_args():
    sig = inspect.signature(BibTeXMLEntriesClass.__init__)
    params = list(sig.parameters.keys())



def test_bibtexml::bibtexmlentrytype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::BibTeXMLEntryType)


def test_bibtexml::bibtexmlentrytype_constructor_exists():
    assert callable(bibtexml::BibTeXMLEntryType.__init__)


def test_bibtexml::bibtexmlentrytype_constructor_args():
    sig = inspect.signature(bibtexml::BibTeXMLEntryType.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_bibtexml::bibtexmlentrytype_has_id():
    assert hasattr(bibtexml::BibTeXMLEntryType, "id")
    descriptor = None
    for klass in bibtexml::BibTeXMLEntryType.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::misctype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::MiscType)


def test_bibtexml::misctype_constructor_exists():
    assert callable(bibtexml::MiscType.__init__)


def test_bibtexml::misctype_constructor_args():
    sig = inspect.signature(bibtexml::MiscType.__init__)
    params = list(sig.parameters.keys())
    assert "howpublished" in params, "Missing parameter 'howpublished'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "title" in params, "Missing parameter 'title'"
    assert "month" in params, "Missing parameter 'month'"
    assert "note" in params, "Missing parameter 'note'"
    assert "author" in params, "Missing parameter 'author'"
    assert "key" in params, "Missing parameter 'key'"
    assert "url" in params, "Missing parameter 'url'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "year" in params, "Missing parameter 'year'"

def test_bibtexml::misctype_has_howpublished():
    assert hasattr(bibtexml::MiscType, "howpublished")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "howpublished" in klass.__dict__:
            descriptor = klass.__dict__["howpublished"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_doi():
    assert hasattr(bibtexml::MiscType, "doi")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_title():
    assert hasattr(bibtexml::MiscType, "title")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_month():
    assert hasattr(bibtexml::MiscType, "month")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_note():
    assert hasattr(bibtexml::MiscType, "note")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_author():
    assert hasattr(bibtexml::MiscType, "author")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_key():
    assert hasattr(bibtexml::MiscType, "key")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_url():
    assert hasattr(bibtexml::MiscType, "url")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_crossref():
    assert hasattr(bibtexml::MiscType, "crossref")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::misctype_has_year():
    assert hasattr(bibtexml::MiscType, "year")
    descriptor = None
    for klass in bibtexml::MiscType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::unpublishedtype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::UnpublishedType)


def test_bibtexml::unpublishedtype_constructor_exists():
    assert callable(bibtexml::UnpublishedType.__init__)


def test_bibtexml::unpublishedtype_constructor_args():
    sig = inspect.signature(bibtexml::UnpublishedType.__init__)
    params = list(sig.parameters.keys())
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "month" in params, "Missing parameter 'month'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "url" in params, "Missing parameter 'url'"
    assert "note" in params, "Missing parameter 'note'"
    assert "key" in params, "Missing parameter 'key'"
    assert "year" in params, "Missing parameter 'year'"

def test_bibtexml::unpublishedtype_has_crossref():
    assert hasattr(bibtexml::UnpublishedType, "crossref")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::unpublishedtype_has_title():
    assert hasattr(bibtexml::UnpublishedType, "title")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::unpublishedtype_has_author():
    assert hasattr(bibtexml::UnpublishedType, "author")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::unpublishedtype_has_month():
    assert hasattr(bibtexml::UnpublishedType, "month")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::unpublishedtype_has_doi():
    assert hasattr(bibtexml::UnpublishedType, "doi")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::unpublishedtype_has_url():
    assert hasattr(bibtexml::UnpublishedType, "url")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::unpublishedtype_has_note():
    assert hasattr(bibtexml::UnpublishedType, "note")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::unpublishedtype_has_key():
    assert hasattr(bibtexml::UnpublishedType, "key")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::unpublishedtype_has_year():
    assert hasattr(bibtexml::UnpublishedType, "year")
    descriptor = None
    for klass in bibtexml::UnpublishedType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::conferencetype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::ConferenceType)


def test_bibtexml::conferencetype_constructor_exists():
    assert callable(bibtexml::ConferenceType.__init__)


def test_bibtexml::conferencetype_constructor_args():
    sig = inspect.signature(bibtexml::ConferenceType.__init__)
    params = list(sig.parameters.keys())
    assert "booktitle" in params, "Missing parameter 'booktitle'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "number" in params, "Missing parameter 'number'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "address" in params, "Missing parameter 'address'"
    assert "author" in params, "Missing parameter 'author'"
    assert "url" in params, "Missing parameter 'url'"
    assert "series" in params, "Missing parameter 'series'"
    assert "title" in params, "Missing parameter 'title'"
    assert "editor" in params, "Missing parameter 'editor'"
    assert "key" in params, "Missing parameter 'key'"
    assert "month" in params, "Missing parameter 'month'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "year" in params, "Missing parameter 'year'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "note" in params, "Missing parameter 'note'"
    assert "publisher" in params, "Missing parameter 'publisher'"

def test_bibtexml::conferencetype_has_booktitle():
    assert hasattr(bibtexml::ConferenceType, "booktitle")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_crossref():
    assert hasattr(bibtexml::ConferenceType, "crossref")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_volume():
    assert hasattr(bibtexml::ConferenceType, "volume")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_number():
    assert hasattr(bibtexml::ConferenceType, "number")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_doi():
    assert hasattr(bibtexml::ConferenceType, "doi")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_address():
    assert hasattr(bibtexml::ConferenceType, "address")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_author():
    assert hasattr(bibtexml::ConferenceType, "author")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_url():
    assert hasattr(bibtexml::ConferenceType, "url")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_series():
    assert hasattr(bibtexml::ConferenceType, "series")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_title():
    assert hasattr(bibtexml::ConferenceType, "title")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_editor():
    assert hasattr(bibtexml::ConferenceType, "editor")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "editor" in klass.__dict__:
            descriptor = klass.__dict__["editor"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_key():
    assert hasattr(bibtexml::ConferenceType, "key")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_month():
    assert hasattr(bibtexml::ConferenceType, "month")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_pages():
    assert hasattr(bibtexml::ConferenceType, "pages")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_year():
    assert hasattr(bibtexml::ConferenceType, "year")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_organization():
    assert hasattr(bibtexml::ConferenceType, "organization")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_note():
    assert hasattr(bibtexml::ConferenceType, "note")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::conferencetype_has_publisher():
    assert hasattr(bibtexml::ConferenceType, "publisher")
    descriptor = None
    for klass in bibtexml::ConferenceType.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::inproceedingstype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::InproceedingsType)


def test_bibtexml::inproceedingstype_constructor_exists():
    assert callable(bibtexml::InproceedingsType.__init__)


def test_bibtexml::inproceedingstype_constructor_args():
    sig = inspect.signature(bibtexml::InproceedingsType.__init__)
    params = list(sig.parameters.keys())
    assert "doi" in params, "Missing parameter 'doi'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "address" in params, "Missing parameter 'address'"
    assert "title" in params, "Missing parameter 'title'"
    assert "year" in params, "Missing parameter 'year'"
    assert "booktitle" in params, "Missing parameter 'booktitle'"
    assert "month" in params, "Missing parameter 'month'"
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "number" in params, "Missing parameter 'number'"
    assert "url" in params, "Missing parameter 'url'"
    assert "author" in params, "Missing parameter 'author'"
    assert "note" in params, "Missing parameter 'note'"
    assert "series" in params, "Missing parameter 'series'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "editor" in params, "Missing parameter 'editor'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "key" in params, "Missing parameter 'key'"

def test_bibtexml::inproceedingstype_has_doi():
    assert hasattr(bibtexml::InproceedingsType, "doi")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_volume():
    assert hasattr(bibtexml::InproceedingsType, "volume")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_address():
    assert hasattr(bibtexml::InproceedingsType, "address")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_title():
    assert hasattr(bibtexml::InproceedingsType, "title")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_year():
    assert hasattr(bibtexml::InproceedingsType, "year")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_booktitle():
    assert hasattr(bibtexml::InproceedingsType, "booktitle")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_month():
    assert hasattr(bibtexml::InproceedingsType, "month")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_publisher():
    assert hasattr(bibtexml::InproceedingsType, "publisher")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_number():
    assert hasattr(bibtexml::InproceedingsType, "number")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_url():
    assert hasattr(bibtexml::InproceedingsType, "url")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_author():
    assert hasattr(bibtexml::InproceedingsType, "author")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_note():
    assert hasattr(bibtexml::InproceedingsType, "note")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_series():
    assert hasattr(bibtexml::InproceedingsType, "series")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_organization():
    assert hasattr(bibtexml::InproceedingsType, "organization")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_crossref():
    assert hasattr(bibtexml::InproceedingsType, "crossref")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_editor():
    assert hasattr(bibtexml::InproceedingsType, "editor")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "editor" in klass.__dict__:
            descriptor = klass.__dict__["editor"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_pages():
    assert hasattr(bibtexml::InproceedingsType, "pages")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inproceedingstype_has_key():
    assert hasattr(bibtexml::InproceedingsType, "key")
    descriptor = None
    for klass in bibtexml::InproceedingsType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::proceedingstype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::ProceedingsType)


def test_bibtexml::proceedingstype_constructor_exists():
    assert callable(bibtexml::ProceedingsType.__init__)


def test_bibtexml::proceedingstype_constructor_args():
    sig = inspect.signature(bibtexml::ProceedingsType.__init__)
    params = list(sig.parameters.keys())
    assert "doi" in params, "Missing parameter 'doi'"
    assert "number" in params, "Missing parameter 'number'"
    assert "title" in params, "Missing parameter 'title'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "editor" in params, "Missing parameter 'editor'"
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "address" in params, "Missing parameter 'address'"
    assert "url" in params, "Missing parameter 'url'"
    assert "key" in params, "Missing parameter 'key'"
    assert "series" in params, "Missing parameter 'series'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "note" in params, "Missing parameter 'note'"

def test_bibtexml::proceedingstype_has_doi():
    assert hasattr(bibtexml::ProceedingsType, "doi")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_number():
    assert hasattr(bibtexml::ProceedingsType, "number")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_title():
    assert hasattr(bibtexml::ProceedingsType, "title")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_organization():
    assert hasattr(bibtexml::ProceedingsType, "organization")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_editor():
    assert hasattr(bibtexml::ProceedingsType, "editor")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "editor" in klass.__dict__:
            descriptor = klass.__dict__["editor"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_month():
    assert hasattr(bibtexml::ProceedingsType, "month")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_year():
    assert hasattr(bibtexml::ProceedingsType, "year")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_volume():
    assert hasattr(bibtexml::ProceedingsType, "volume")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_publisher():
    assert hasattr(bibtexml::ProceedingsType, "publisher")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_address():
    assert hasattr(bibtexml::ProceedingsType, "address")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_url():
    assert hasattr(bibtexml::ProceedingsType, "url")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_key():
    assert hasattr(bibtexml::ProceedingsType, "key")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_series():
    assert hasattr(bibtexml::ProceedingsType, "series")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_crossref():
    assert hasattr(bibtexml::ProceedingsType, "crossref")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::proceedingstype_has_note():
    assert hasattr(bibtexml::ProceedingsType, "note")
    descriptor = None
    for klass in bibtexml::ProceedingsType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::incollectiontype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::IncollectionType)


def test_bibtexml::incollectiontype_constructor_exists():
    assert callable(bibtexml::IncollectionType.__init__)


def test_bibtexml::incollectiontype_constructor_args():
    sig = inspect.signature(bibtexml::IncollectionType.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "url" in params, "Missing parameter 'url'"
    assert "title" in params, "Missing parameter 'title'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "chapter" in params, "Missing parameter 'chapter'"
    assert "author" in params, "Missing parameter 'author'"
    assert "year" in params, "Missing parameter 'year'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "booktitle" in params, "Missing parameter 'booktitle'"
    assert "key" in params, "Missing parameter 'key'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "editor" in params, "Missing parameter 'editor'"
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "note" in params, "Missing parameter 'note'"
    assert "address" in params, "Missing parameter 'address'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "number" in params, "Missing parameter 'number'"
    assert "series" in params, "Missing parameter 'series'"
    assert "type" in params, "Missing parameter 'type'"

def test_bibtexml::incollectiontype_has_month():
    assert hasattr(bibtexml::IncollectionType, "month")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_url():
    assert hasattr(bibtexml::IncollectionType, "url")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_title():
    assert hasattr(bibtexml::IncollectionType, "title")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_doi():
    assert hasattr(bibtexml::IncollectionType, "doi")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_edition():
    assert hasattr(bibtexml::IncollectionType, "edition")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_chapter():
    assert hasattr(bibtexml::IncollectionType, "chapter")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "chapter" in klass.__dict__:
            descriptor = klass.__dict__["chapter"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_author():
    assert hasattr(bibtexml::IncollectionType, "author")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_year():
    assert hasattr(bibtexml::IncollectionType, "year")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_pages():
    assert hasattr(bibtexml::IncollectionType, "pages")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_booktitle():
    assert hasattr(bibtexml::IncollectionType, "booktitle")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_key():
    assert hasattr(bibtexml::IncollectionType, "key")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_volume():
    assert hasattr(bibtexml::IncollectionType, "volume")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_editor():
    assert hasattr(bibtexml::IncollectionType, "editor")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "editor" in klass.__dict__:
            descriptor = klass.__dict__["editor"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_publisher():
    assert hasattr(bibtexml::IncollectionType, "publisher")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_note():
    assert hasattr(bibtexml::IncollectionType, "note")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_address():
    assert hasattr(bibtexml::IncollectionType, "address")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_crossref():
    assert hasattr(bibtexml::IncollectionType, "crossref")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_number():
    assert hasattr(bibtexml::IncollectionType, "number")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_series():
    assert hasattr(bibtexml::IncollectionType, "series")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::incollectiontype_has_type():
    assert hasattr(bibtexml::IncollectionType, "type")
    descriptor = None
    for klass in bibtexml::IncollectionType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::inbooktype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::InbookType)


def test_bibtexml::inbooktype_constructor_exists():
    assert callable(bibtexml::InbookType.__init__)


def test_bibtexml::inbooktype_constructor_args():
    sig = inspect.signature(bibtexml::InbookType.__init__)
    params = list(sig.parameters.keys())
    assert "edition" in params, "Missing parameter 'edition'"
    assert "number" in params, "Missing parameter 'number'"
    assert "month" in params, "Missing parameter 'month'"
    assert "address" in params, "Missing parameter 'address'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "type" in params, "Missing parameter 'type'"
    assert "series" in params, "Missing parameter 'series'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "title" in params, "Missing parameter 'title'"
    assert "key" in params, "Missing parameter 'key'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "pages1" in params, "Missing parameter 'pages1'"
    assert "author" in params, "Missing parameter 'author'"
    assert "chapter" in params, "Missing parameter 'chapter'"
    assert "year" in params, "Missing parameter 'year'"
    assert "editor" in params, "Missing parameter 'editor'"
    assert "note" in params, "Missing parameter 'note'"
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "url" in params, "Missing parameter 'url'"

def test_bibtexml::inbooktype_has_edition():
    assert hasattr(bibtexml::InbookType, "edition")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_number():
    assert hasattr(bibtexml::InbookType, "number")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_month():
    assert hasattr(bibtexml::InbookType, "month")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_address():
    assert hasattr(bibtexml::InbookType, "address")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_crossref():
    assert hasattr(bibtexml::InbookType, "crossref")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_type():
    assert hasattr(bibtexml::InbookType, "type")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_series():
    assert hasattr(bibtexml::InbookType, "series")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_volume():
    assert hasattr(bibtexml::InbookType, "volume")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_title():
    assert hasattr(bibtexml::InbookType, "title")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_key():
    assert hasattr(bibtexml::InbookType, "key")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_pages():
    assert hasattr(bibtexml::InbookType, "pages")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_pages1():
    assert hasattr(bibtexml::InbookType, "pages1")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "pages1" in klass.__dict__:
            descriptor = klass.__dict__["pages1"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_author():
    assert hasattr(bibtexml::InbookType, "author")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_chapter():
    assert hasattr(bibtexml::InbookType, "chapter")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "chapter" in klass.__dict__:
            descriptor = klass.__dict__["chapter"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_year():
    assert hasattr(bibtexml::InbookType, "year")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_editor():
    assert hasattr(bibtexml::InbookType, "editor")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "editor" in klass.__dict__:
            descriptor = klass.__dict__["editor"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_note():
    assert hasattr(bibtexml::InbookType, "note")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_publisher():
    assert hasattr(bibtexml::InbookType, "publisher")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_doi():
    assert hasattr(bibtexml::InbookType, "doi")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::inbooktype_has_url():
    assert hasattr(bibtexml::InbookType, "url")
    descriptor = None
    for klass in bibtexml::InbookType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::phdthesistype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::PhdthesisType)


def test_bibtexml::phdthesistype_constructor_exists():
    assert callable(bibtexml::PhdthesisType.__init__)


def test_bibtexml::phdthesistype_constructor_args():
    sig = inspect.signature(bibtexml::PhdthesisType.__init__)
    params = list(sig.parameters.keys())
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "note" in params, "Missing parameter 'note'"
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"
    assert "address" in params, "Missing parameter 'address'"
    assert "title" in params, "Missing parameter 'title'"
    assert "author" in params, "Missing parameter 'author'"
    assert "type" in params, "Missing parameter 'type'"
    assert "school" in params, "Missing parameter 'school'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "url" in params, "Missing parameter 'url'"
    assert "key" in params, "Missing parameter 'key'"

def test_bibtexml::phdthesistype_has_crossref():
    assert hasattr(bibtexml::PhdthesisType, "crossref")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_note():
    assert hasattr(bibtexml::PhdthesisType, "note")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_month():
    assert hasattr(bibtexml::PhdthesisType, "month")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_year():
    assert hasattr(bibtexml::PhdthesisType, "year")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_address():
    assert hasattr(bibtexml::PhdthesisType, "address")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_title():
    assert hasattr(bibtexml::PhdthesisType, "title")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_author():
    assert hasattr(bibtexml::PhdthesisType, "author")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_type():
    assert hasattr(bibtexml::PhdthesisType, "type")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_school():
    assert hasattr(bibtexml::PhdthesisType, "school")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "school" in klass.__dict__:
            descriptor = klass.__dict__["school"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_doi():
    assert hasattr(bibtexml::PhdthesisType, "doi")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_url():
    assert hasattr(bibtexml::PhdthesisType, "url")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::phdthesistype_has_key():
    assert hasattr(bibtexml::PhdthesisType, "key")
    descriptor = None
    for klass in bibtexml::PhdthesisType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::mastersthesistype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::MastersthesisType)


def test_bibtexml::mastersthesistype_constructor_exists():
    assert callable(bibtexml::MastersthesisType.__init__)


def test_bibtexml::mastersthesistype_constructor_args():
    sig = inspect.signature(bibtexml::MastersthesisType.__init__)
    params = list(sig.parameters.keys())
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "type" in params, "Missing parameter 'type'"
    assert "author" in params, "Missing parameter 'author'"
    assert "school" in params, "Missing parameter 'school'"
    assert "year" in params, "Missing parameter 'year'"
    assert "month" in params, "Missing parameter 'month'"
    assert "address" in params, "Missing parameter 'address'"
    assert "url" in params, "Missing parameter 'url'"
    assert "title" in params, "Missing parameter 'title'"
    assert "key" in params, "Missing parameter 'key'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "note" in params, "Missing parameter 'note'"

def test_bibtexml::mastersthesistype_has_crossref():
    assert hasattr(bibtexml::MastersthesisType, "crossref")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_type():
    assert hasattr(bibtexml::MastersthesisType, "type")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_author():
    assert hasattr(bibtexml::MastersthesisType, "author")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_school():
    assert hasattr(bibtexml::MastersthesisType, "school")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "school" in klass.__dict__:
            descriptor = klass.__dict__["school"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_year():
    assert hasattr(bibtexml::MastersthesisType, "year")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_month():
    assert hasattr(bibtexml::MastersthesisType, "month")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_address():
    assert hasattr(bibtexml::MastersthesisType, "address")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_url():
    assert hasattr(bibtexml::MastersthesisType, "url")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_title():
    assert hasattr(bibtexml::MastersthesisType, "title")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_key():
    assert hasattr(bibtexml::MastersthesisType, "key")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_doi():
    assert hasattr(bibtexml::MastersthesisType, "doi")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::mastersthesistype_has_note():
    assert hasattr(bibtexml::MastersthesisType, "note")
    descriptor = None
    for klass in bibtexml::MastersthesisType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::techreporttype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::TechreportType)


def test_bibtexml::techreporttype_constructor_exists():
    assert callable(bibtexml::TechreportType.__init__)


def test_bibtexml::techreporttype_constructor_args():
    sig = inspect.signature(bibtexml::TechreportType.__init__)
    params = list(sig.parameters.keys())
    assert "type" in params, "Missing parameter 'type'"
    assert "address" in params, "Missing parameter 'address'"
    assert "key" in params, "Missing parameter 'key'"
    assert "url" in params, "Missing parameter 'url'"
    assert "note" in params, "Missing parameter 'note'"
    assert "author" in params, "Missing parameter 'author'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "year" in params, "Missing parameter 'year'"
    assert "institution" in params, "Missing parameter 'institution'"
    assert "number" in params, "Missing parameter 'number'"
    assert "title" in params, "Missing parameter 'title'"
    assert "month" in params, "Missing parameter 'month'"
    assert "crossref" in params, "Missing parameter 'crossref'"

def test_bibtexml::techreporttype_has_type():
    assert hasattr(bibtexml::TechreportType, "type")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_address():
    assert hasattr(bibtexml::TechreportType, "address")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_key():
    assert hasattr(bibtexml::TechreportType, "key")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_url():
    assert hasattr(bibtexml::TechreportType, "url")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_note():
    assert hasattr(bibtexml::TechreportType, "note")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_author():
    assert hasattr(bibtexml::TechreportType, "author")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_doi():
    assert hasattr(bibtexml::TechreportType, "doi")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_year():
    assert hasattr(bibtexml::TechreportType, "year")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_institution():
    assert hasattr(bibtexml::TechreportType, "institution")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "institution" in klass.__dict__:
            descriptor = klass.__dict__["institution"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_number():
    assert hasattr(bibtexml::TechreportType, "number")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_title():
    assert hasattr(bibtexml::TechreportType, "title")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_month():
    assert hasattr(bibtexml::TechreportType, "month")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::techreporttype_has_crossref():
    assert hasattr(bibtexml::TechreportType, "crossref")
    descriptor = None
    for klass in bibtexml::TechreportType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::manualtype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::ManualType)


def test_bibtexml::manualtype_constructor_exists():
    assert callable(bibtexml::ManualType.__init__)


def test_bibtexml::manualtype_constructor_args():
    sig = inspect.signature(bibtexml::ManualType.__init__)
    params = list(sig.parameters.keys())
    assert "note" in params, "Missing parameter 'note'"
    assert "address" in params, "Missing parameter 'address'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "url" in params, "Missing parameter 'url'"
    assert "key" in params, "Missing parameter 'key'"
    assert "author" in params, "Missing parameter 'author'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "month" in params, "Missing parameter 'month'"
    assert "organization" in params, "Missing parameter 'organization'"
    assert "title" in params, "Missing parameter 'title'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "year" in params, "Missing parameter 'year'"

def test_bibtexml::manualtype_has_note():
    assert hasattr(bibtexml::ManualType, "note")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_address():
    assert hasattr(bibtexml::ManualType, "address")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_crossref():
    assert hasattr(bibtexml::ManualType, "crossref")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_url():
    assert hasattr(bibtexml::ManualType, "url")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_key():
    assert hasattr(bibtexml::ManualType, "key")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_author():
    assert hasattr(bibtexml::ManualType, "author")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_doi():
    assert hasattr(bibtexml::ManualType, "doi")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_month():
    assert hasattr(bibtexml::ManualType, "month")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_organization():
    assert hasattr(bibtexml::ManualType, "organization")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "organization" in klass.__dict__:
            descriptor = klass.__dict__["organization"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_title():
    assert hasattr(bibtexml::ManualType, "title")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_edition():
    assert hasattr(bibtexml::ManualType, "edition")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::manualtype_has_year():
    assert hasattr(bibtexml::ManualType, "year")
    descriptor = None
    for klass in bibtexml::ManualType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::booklettype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::BookletType)


def test_bibtexml::booklettype_constructor_exists():
    assert callable(bibtexml::BookletType.__init__)


def test_bibtexml::booklettype_constructor_args():
    sig = inspect.signature(bibtexml::BookletType.__init__)
    params = list(sig.parameters.keys())
    assert "doi" in params, "Missing parameter 'doi'"
    assert "key" in params, "Missing parameter 'key'"
    assert "url" in params, "Missing parameter 'url'"
    assert "howpublished" in params, "Missing parameter 'howpublished'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "address" in params, "Missing parameter 'address'"
    assert "title" in params, "Missing parameter 'title'"
    assert "note" in params, "Missing parameter 'note'"
    assert "month" in params, "Missing parameter 'month'"
    assert "year" in params, "Missing parameter 'year'"
    assert "author" in params, "Missing parameter 'author'"

def test_bibtexml::booklettype_has_doi():
    assert hasattr(bibtexml::BookletType, "doi")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_key():
    assert hasattr(bibtexml::BookletType, "key")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_url():
    assert hasattr(bibtexml::BookletType, "url")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_howpublished():
    assert hasattr(bibtexml::BookletType, "howpublished")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "howpublished" in klass.__dict__:
            descriptor = klass.__dict__["howpublished"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_crossref():
    assert hasattr(bibtexml::BookletType, "crossref")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_address():
    assert hasattr(bibtexml::BookletType, "address")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_title():
    assert hasattr(bibtexml::BookletType, "title")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_note():
    assert hasattr(bibtexml::BookletType, "note")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_month():
    assert hasattr(bibtexml::BookletType, "month")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_year():
    assert hasattr(bibtexml::BookletType, "year")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booklettype_has_author():
    assert hasattr(bibtexml::BookletType, "author")
    descriptor = None
    for klass in bibtexml::BookletType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::booktype_is_not_abstract():
    assert not inspect.isabstract(bibtexml::BookType)


def test_bibtexml::booktype_constructor_exists():
    assert callable(bibtexml::BookType.__init__)


def test_bibtexml::booktype_constructor_args():
    sig = inspect.signature(bibtexml::BookType.__init__)
    params = list(sig.parameters.keys())
    assert "volume" in params, "Missing parameter 'volume'"
    assert "url" in params, "Missing parameter 'url'"
    assert "month" in params, "Missing parameter 'month'"
    assert "crossref" in params, "Missing parameter 'crossref'"
    assert "author" in params, "Missing parameter 'author'"
    assert "key" in params, "Missing parameter 'key'"
    assert "editor" in params, "Missing parameter 'editor'"
    assert "year" in params, "Missing parameter 'year'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "note" in params, "Missing parameter 'note'"
    assert "number" in params, "Missing parameter 'number'"
    assert "series" in params, "Missing parameter 'series'"
    assert "doi" in params, "Missing parameter 'doi'"
    assert "address" in params, "Missing parameter 'address'"
    assert "title" in params, "Missing parameter 'title'"

def test_bibtexml::booktype_has_volume():
    assert hasattr(bibtexml::BookType, "volume")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_url():
    assert hasattr(bibtexml::BookType, "url")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "url" in klass.__dict__:
            descriptor = klass.__dict__["url"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_month():
    assert hasattr(bibtexml::BookType, "month")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_crossref():
    assert hasattr(bibtexml::BookType, "crossref")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "crossref" in klass.__dict__:
            descriptor = klass.__dict__["crossref"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_author():
    assert hasattr(bibtexml::BookType, "author")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_key():
    assert hasattr(bibtexml::BookType, "key")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "key" in klass.__dict__:
            descriptor = klass.__dict__["key"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_editor():
    assert hasattr(bibtexml::BookType, "editor")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "editor" in klass.__dict__:
            descriptor = klass.__dict__["editor"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_year():
    assert hasattr(bibtexml::BookType, "year")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_edition():
    assert hasattr(bibtexml::BookType, "edition")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_publisher():
    assert hasattr(bibtexml::BookType, "publisher")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_note():
    assert hasattr(bibtexml::BookType, "note")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "note" in klass.__dict__:
            descriptor = klass.__dict__["note"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_number():
    assert hasattr(bibtexml::BookType, "number")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_series():
    assert hasattr(bibtexml::BookType, "series")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_doi():
    assert hasattr(bibtexml::BookType, "doi")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "doi" in klass.__dict__:
            descriptor = klass.__dict__["doi"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_address():
    assert hasattr(bibtexml::BookType, "address")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_bibtexml::booktype_has_title():
    assert hasattr(bibtexml::BookType, "title")
    descriptor = None
    for klass in bibtexml::BookType.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_bibtexml::bibtexmlentriesclass_is_not_abstract():
    assert not inspect.isabstract(bibtexml::BibTeXMLEntriesClass)


def test_bibtexml::bibtexmlentriesclass_constructor_exists():
    assert callable(bibtexml::BibTeXMLEntriesClass.__init__)


def test_bibtexml::bibtexmlentriesclass_constructor_args():
    sig = inspect.signature(bibtexml::BibTeXMLEntriesClass.__init__)
    params = list(sig.parameters.keys())

def test_monthstringtype_exists():
    # Check that the Enumeration exists
    assert MonthStringType is not None

def test_monthstringtype_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in MonthStringType]
    expected_literals = [
        "Dec",
        "Aug",
        "Apr",
        "Jul",
        "Sep",
        "Oct",
        "May",
        "Jan",
        "Jun",
        "Mar",
        "Nov",
        "Feb",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in MonthStringType"


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
bibtexml::ArticleType_strategy = st.builds(
    bibtexml::ArticleType,
    volume=
        safe_text,
    doi=
        safe_text,
    url=
        safe_text,
    note=
        safe_text,
    author=
        safe_text,
    journal=
        safe_text,
    pages=
        safe_text,
    month=
        safe_text,
    crossref=
        safe_text,
    key=
        safe_text,
    year=
        safe_text,
    number=
        safe_text,
    title=
        safe_text
)
bibtexml::FileType_strategy = st.builds(
    bibtexml::FileType,
)
bibtexml::EStringToStringMapEntry_strategy = st.builds(
    bibtexml::EStringToStringMapEntry,
)
bibtexml::DocumentRoot_strategy = st.builds(
    bibtexml::DocumentRoot,
    pages=
        safe_text,
    editor=
        safe_text,
    doi=
        safe_text,
    edition=
        safe_text,
    key=
        safe_text,
    author=
        safe_text,
    series=
        safe_text,
    organization=
        safe_text,
    number=
        safe_text,
    type=
        safe_text,
    volume=
        safe_text,
    title=
        safe_text,
    journal=
        safe_text,
    address=
        safe_text,
    note=
        safe_text,
    school=
        safe_text,
    annote=
        safe_text,
    crossref=
        safe_text,
    howpublished=
        safe_text,
    booktitle=
        safe_text,
    institution=
        safe_text,
    mixed=
        safe_text,
    chapter=
        safe_text,
    publisher=
        safe_text,
    year=
        safe_text,
    url=
        safe_text,
    month=
        safe_text
)
BibTeXMLEntriesClass_strategy = st.builds(
    BibTeXMLEntriesClass,
)
bibtexml::BibTeXMLEntryType_strategy = st.builds(
    bibtexml::BibTeXMLEntryType,
    id=
        safe_text
)
bibtexml::MiscType_strategy = st.builds(
    bibtexml::MiscType,
    howpublished=
        safe_text,
    doi=
        safe_text,
    title=
        safe_text,
    month=
        safe_text,
    note=
        safe_text,
    author=
        safe_text,
    key=
        safe_text,
    url=
        safe_text,
    crossref=
        safe_text,
    year=
        safe_text
)
bibtexml::UnpublishedType_strategy = st.builds(
    bibtexml::UnpublishedType,
    crossref=
        safe_text,
    title=
        safe_text,
    author=
        safe_text,
    month=
        safe_text,
    doi=
        safe_text,
    url=
        safe_text,
    note=
        safe_text,
    key=
        safe_text,
    year=
        safe_text
)
bibtexml::ConferenceType_strategy = st.builds(
    bibtexml::ConferenceType,
    booktitle=
        safe_text,
    crossref=
        safe_text,
    volume=
        safe_text,
    number=
        safe_text,
    doi=
        safe_text,
    address=
        safe_text,
    author=
        safe_text,
    url=
        safe_text,
    series=
        safe_text,
    title=
        safe_text,
    editor=
        safe_text,
    key=
        safe_text,
    month=
        safe_text,
    pages=
        safe_text,
    year=
        safe_text,
    organization=
        safe_text,
    note=
        safe_text,
    publisher=
        safe_text
)
bibtexml::InproceedingsType_strategy = st.builds(
    bibtexml::InproceedingsType,
    doi=
        safe_text,
    volume=
        safe_text,
    address=
        safe_text,
    title=
        safe_text,
    year=
        safe_text,
    booktitle=
        safe_text,
    month=
        safe_text,
    publisher=
        safe_text,
    number=
        safe_text,
    url=
        safe_text,
    author=
        safe_text,
    note=
        safe_text,
    series=
        safe_text,
    organization=
        safe_text,
    crossref=
        safe_text,
    editor=
        safe_text,
    pages=
        safe_text,
    key=
        safe_text
)
bibtexml::ProceedingsType_strategy = st.builds(
    bibtexml::ProceedingsType,
    doi=
        safe_text,
    number=
        safe_text,
    title=
        safe_text,
    organization=
        safe_text,
    editor=
        safe_text,
    month=
        safe_text,
    year=
        safe_text,
    volume=
        safe_text,
    publisher=
        safe_text,
    address=
        safe_text,
    url=
        safe_text,
    key=
        safe_text,
    series=
        safe_text,
    crossref=
        safe_text,
    note=
        safe_text
)
bibtexml::IncollectionType_strategy = st.builds(
    bibtexml::IncollectionType,
    month=
        safe_text,
    url=
        safe_text,
    title=
        safe_text,
    doi=
        safe_text,
    edition=
        safe_text,
    chapter=
        safe_text,
    author=
        safe_text,
    year=
        safe_text,
    pages=
        safe_text,
    booktitle=
        safe_text,
    key=
        safe_text,
    volume=
        safe_text,
    editor=
        safe_text,
    publisher=
        safe_text,
    note=
        safe_text,
    address=
        safe_text,
    crossref=
        safe_text,
    number=
        safe_text,
    series=
        safe_text,
    type=
        safe_text
)
bibtexml::InbookType_strategy = st.builds(
    bibtexml::InbookType,
    edition=
        safe_text,
    number=
        safe_text,
    month=
        safe_text,
    address=
        safe_text,
    crossref=
        safe_text,
    type=
        safe_text,
    series=
        safe_text,
    volume=
        safe_text,
    title=
        safe_text,
    key=
        safe_text,
    pages=
        safe_text,
    pages1=
        safe_text,
    author=
        safe_text,
    chapter=
        safe_text,
    year=
        safe_text,
    editor=
        safe_text,
    note=
        safe_text,
    publisher=
        safe_text,
    doi=
        safe_text,
    url=
        safe_text
)
bibtexml::PhdthesisType_strategy = st.builds(
    bibtexml::PhdthesisType,
    crossref=
        safe_text,
    note=
        safe_text,
    month=
        safe_text,
    year=
        safe_text,
    address=
        safe_text,
    title=
        safe_text,
    author=
        safe_text,
    type=
        safe_text,
    school=
        safe_text,
    doi=
        safe_text,
    url=
        safe_text,
    key=
        safe_text
)
bibtexml::MastersthesisType_strategy = st.builds(
    bibtexml::MastersthesisType,
    crossref=
        safe_text,
    type=
        safe_text,
    author=
        safe_text,
    school=
        safe_text,
    year=
        safe_text,
    month=
        safe_text,
    address=
        safe_text,
    url=
        safe_text,
    title=
        safe_text,
    key=
        safe_text,
    doi=
        safe_text,
    note=
        safe_text
)
bibtexml::TechreportType_strategy = st.builds(
    bibtexml::TechreportType,
    type=
        safe_text,
    address=
        safe_text,
    key=
        safe_text,
    url=
        safe_text,
    note=
        safe_text,
    author=
        safe_text,
    doi=
        safe_text,
    year=
        safe_text,
    institution=
        safe_text,
    number=
        safe_text,
    title=
        safe_text,
    month=
        safe_text,
    crossref=
        safe_text
)
bibtexml::ManualType_strategy = st.builds(
    bibtexml::ManualType,
    note=
        safe_text,
    address=
        safe_text,
    crossref=
        safe_text,
    url=
        safe_text,
    key=
        safe_text,
    author=
        safe_text,
    doi=
        safe_text,
    month=
        safe_text,
    organization=
        safe_text,
    title=
        safe_text,
    edition=
        safe_text,
    year=
        safe_text
)
bibtexml::BookletType_strategy = st.builds(
    bibtexml::BookletType,
    doi=
        safe_text,
    key=
        safe_text,
    url=
        safe_text,
    howpublished=
        safe_text,
    crossref=
        safe_text,
    address=
        safe_text,
    title=
        safe_text,
    note=
        safe_text,
    month=
        safe_text,
    year=
        safe_text,
    author=
        safe_text
)
bibtexml::BookType_strategy = st.builds(
    bibtexml::BookType,
    volume=
        safe_text,
    url=
        safe_text,
    month=
        safe_text,
    crossref=
        safe_text,
    author=
        safe_text,
    key=
        safe_text,
    editor=
        safe_text,
    year=
        safe_text,
    edition=
        safe_text,
    publisher=
        safe_text,
    note=
        safe_text,
    number=
        safe_text,
    series=
        safe_text,
    doi=
        safe_text,
    address=
        safe_text,
    title=
        safe_text
)
bibtexml::BibTeXMLEntriesClass_strategy = st.builds(
    bibtexml::BibTeXMLEntriesClass,
)

@given(instance=bibtexml::ArticleType_strategy)
@settings(max_examples=50)
def test_bibtexml::articletype_instantiation(instance):
    assert isinstance(instance, bibtexml::ArticleType)

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_journal_type(instance):
    assert isinstance(instance.journal, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::ArticleType_strategy)
def test_bibtexml::articletype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::FileType_strategy)
@settings(max_examples=50)
def test_bibtexml::filetype_instantiation(instance):
    assert isinstance(instance, bibtexml::FileType)

@given(instance=bibtexml::EStringToStringMapEntry_strategy)
@settings(max_examples=50)
def test_bibtexml::estringtostringmapentry_instantiation(instance):
    assert isinstance(instance, bibtexml::EStringToStringMapEntry)

@given(instance=bibtexml::DocumentRoot_strategy)
@settings(max_examples=50)
def test_bibtexml::documentroot_instantiation(instance):
    assert isinstance(instance, bibtexml::DocumentRoot)

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_editor_type(instance):
    assert isinstance(instance.editor, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_journal_type(instance):
    assert isinstance(instance.journal, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_journal_setter(instance):
    original = instance.journal
    instance.journal = original
    assert instance.journal == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_school_type(instance):
    assert isinstance(instance.school, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_annote_type(instance):
    assert isinstance(instance.annote, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_annote_setter(instance):
    original = instance.annote
    instance.annote = original
    assert instance.annote == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_howpublished_type(instance):
    assert isinstance(instance.howpublished, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_howpublished_setter(instance):
    original = instance.howpublished
    instance.howpublished = original
    assert instance.howpublished == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_booktitle_type(instance):
    assert isinstance(instance.booktitle, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_institution_type(instance):
    assert isinstance(instance.institution, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_institution_setter(instance):
    original = instance.institution
    instance.institution = original
    assert instance.institution == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_mixed_type(instance):
    assert isinstance(instance.mixed, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_mixed_setter(instance):
    original = instance.mixed
    instance.mixed = original
    assert instance.mixed == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_chapter_type(instance):
    assert isinstance(instance.chapter, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::DocumentRoot_strategy)
def test_bibtexml::documentroot_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=BibTeXMLEntriesClass_strategy)
@settings(max_examples=50)
def test_bibtexmlentriesclass_instantiation(instance):
    assert isinstance(instance, BibTeXMLEntriesClass)

@given(instance=bibtexml::BibTeXMLEntryType_strategy)
@settings(max_examples=50)
def test_bibtexml::bibtexmlentrytype_instantiation(instance):
    assert isinstance(instance, bibtexml::BibTeXMLEntryType)

@given(instance=bibtexml::BibTeXMLEntryType_strategy)
def test_bibtexml::bibtexmlentrytype_id_type(instance):
    assert isinstance(instance.id, str)


@given(instance=bibtexml::BibTeXMLEntryType_strategy)
def test_bibtexml::bibtexmlentrytype_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=bibtexml::MiscType_strategy)
@settings(max_examples=50)
def test_bibtexml::misctype_instantiation(instance):
    assert isinstance(instance, bibtexml::MiscType)

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_howpublished_type(instance):
    assert isinstance(instance.howpublished, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_howpublished_setter(instance):
    original = instance.howpublished
    instance.howpublished = original
    assert instance.howpublished == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::MiscType_strategy)
def test_bibtexml::misctype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::UnpublishedType_strategy)
@settings(max_examples=50)
def test_bibtexml::unpublishedtype_instantiation(instance):
    assert isinstance(instance, bibtexml::UnpublishedType)

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::UnpublishedType_strategy)
def test_bibtexml::unpublishedtype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::ConferenceType_strategy)
@settings(max_examples=50)
def test_bibtexml::conferencetype_instantiation(instance):
    assert isinstance(instance, bibtexml::ConferenceType)

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_booktitle_type(instance):
    assert isinstance(instance.booktitle, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_editor_type(instance):
    assert isinstance(instance.editor, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=bibtexml::ConferenceType_strategy)
def test_bibtexml::conferencetype_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=bibtexml::InproceedingsType_strategy)
@settings(max_examples=50)
def test_bibtexml::inproceedingstype_instantiation(instance):
    assert isinstance(instance, bibtexml::InproceedingsType)

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_booktitle_type(instance):
    assert isinstance(instance.booktitle, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_editor_type(instance):
    assert isinstance(instance.editor, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::InproceedingsType_strategy)
def test_bibtexml::inproceedingstype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::ProceedingsType_strategy)
@settings(max_examples=50)
def test_bibtexml::proceedingstype_instantiation(instance):
    assert isinstance(instance, bibtexml::ProceedingsType)

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_editor_type(instance):
    assert isinstance(instance.editor, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::ProceedingsType_strategy)
def test_bibtexml::proceedingstype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::IncollectionType_strategy)
@settings(max_examples=50)
def test_bibtexml::incollectiontype_instantiation(instance):
    assert isinstance(instance, bibtexml::IncollectionType)

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_chapter_type(instance):
    assert isinstance(instance.chapter, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_booktitle_type(instance):
    assert isinstance(instance.booktitle, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_editor_type(instance):
    assert isinstance(instance.editor, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bibtexml::IncollectionType_strategy)
def test_bibtexml::incollectiontype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bibtexml::InbookType_strategy)
@settings(max_examples=50)
def test_bibtexml::inbooktype_instantiation(instance):
    assert isinstance(instance, bibtexml::InbookType)

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_pages_type(instance):
    assert isinstance(instance.pages, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_pages1_type(instance):
    assert isinstance(instance.pages1, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_pages1_setter(instance):
    original = instance.pages1
    instance.pages1 = original
    assert instance.pages1 == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_chapter_type(instance):
    assert isinstance(instance.chapter, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_chapter_setter(instance):
    original = instance.chapter
    instance.chapter = original
    assert instance.chapter == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_editor_type(instance):
    assert isinstance(instance.editor, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::InbookType_strategy)
def test_bibtexml::inbooktype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::PhdthesisType_strategy)
@settings(max_examples=50)
def test_bibtexml::phdthesistype_instantiation(instance):
    assert isinstance(instance, bibtexml::PhdthesisType)

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_school_type(instance):
    assert isinstance(instance.school, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::PhdthesisType_strategy)
def test_bibtexml::phdthesistype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::MastersthesisType_strategy)
@settings(max_examples=50)
def test_bibtexml::mastersthesistype_instantiation(instance):
    assert isinstance(instance, bibtexml::MastersthesisType)

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_school_type(instance):
    assert isinstance(instance.school, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_school_setter(instance):
    original = instance.school
    instance.school = original
    assert instance.school == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::MastersthesisType_strategy)
def test_bibtexml::mastersthesistype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::TechreportType_strategy)
@settings(max_examples=50)
def test_bibtexml::techreporttype_instantiation(instance):
    assert isinstance(instance, bibtexml::TechreportType)

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_institution_type(instance):
    assert isinstance(instance.institution, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_institution_setter(instance):
    original = instance.institution
    instance.institution = original
    assert instance.institution == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::TechreportType_strategy)
def test_bibtexml::techreporttype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::ManualType_strategy)
@settings(max_examples=50)
def test_bibtexml::manualtype_instantiation(instance):
    assert isinstance(instance, bibtexml::ManualType)

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_organization_type(instance):
    assert isinstance(instance.organization, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_organization_setter(instance):
    original = instance.organization
    instance.organization = original
    assert instance.organization == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::ManualType_strategy)
def test_bibtexml::manualtype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::BookletType_strategy)
@settings(max_examples=50)
def test_bibtexml::booklettype_instantiation(instance):
    assert isinstance(instance, bibtexml::BookletType)

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_howpublished_type(instance):
    assert isinstance(instance.howpublished, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_howpublished_setter(instance):
    original = instance.howpublished
    instance.howpublished = original
    assert instance.howpublished == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::BookletType_strategy)
def test_bibtexml::booklettype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::BookType_strategy)
@settings(max_examples=50)
def test_bibtexml::booktype_instantiation(instance):
    assert isinstance(instance, bibtexml::BookType)

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_volume_type(instance):
    assert isinstance(instance.volume, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_url_type(instance):
    assert isinstance(instance.url, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_url_setter(instance):
    original = instance.url
    instance.url = original
    assert instance.url == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_month_type(instance):
    assert isinstance(instance.month, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_crossref_type(instance):
    assert isinstance(instance.crossref, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_crossref_setter(instance):
    original = instance.crossref
    instance.crossref = original
    assert instance.crossref == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_key_type(instance):
    assert isinstance(instance.key, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_key_setter(instance):
    original = instance.key
    instance.key = original
    assert instance.key == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_editor_type(instance):
    assert isinstance(instance.editor, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_editor_setter(instance):
    original = instance.editor
    instance.editor = original
    assert instance.editor == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_year_type(instance):
    assert isinstance(instance.year, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_edition_type(instance):
    assert isinstance(instance.edition, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_note_type(instance):
    assert isinstance(instance.note, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_note_setter(instance):
    original = instance.note
    instance.note = original
    assert instance.note == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_number_type(instance):
    assert isinstance(instance.number, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_series_type(instance):
    assert isinstance(instance.series, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_doi_type(instance):
    assert isinstance(instance.doi, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_doi_setter(instance):
    original = instance.doi
    instance.doi = original
    assert instance.doi == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=bibtexml::BookType_strategy)
def test_bibtexml::booktype_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=bibtexml::BibTeXMLEntriesClass_strategy)
@settings(max_examples=50)
def test_bibtexml::bibtexmlentriesclass_instantiation(instance):
    assert isinstance(instance, bibtexml::BibTeXMLEntriesClass)
