import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    sistedesMM_Editor,
    sistedesMM_Publisher,
    Person,
    sistedesMM_SistedesMember,
    sistedesMM_Edition,
    sistedesMM_Publication,
    sistedesMM_University,
    sistedesMM_Person,
    sistedesMM_Journal,
    Publication,
    sistedesMM_Book,
    sistedesMM_InProceedings,
    sistedesMM_Article,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_sistedesmm_editor_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Editor)


def test_sistedesmm_editor_constructor_exists():
    assert callable(sistedesMM_Editor.__init__)


def test_sistedesmm_editor_constructor_args():
    sig = inspect.signature(sistedesMM_Editor.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_sistedesmm_editor_has_name():
    assert hasattr(sistedesMM_Editor, "name")
    descriptor = None
    for klass in sistedesMM_Editor.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_sistedesmm_publisher_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Publisher)


def test_sistedesmm_publisher_constructor_exists():
    assert callable(sistedesMM_Publisher.__init__)


def test_sistedesmm_publisher_constructor_args():
    sig = inspect.signature(sistedesMM_Publisher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"

def test_sistedesmm_publisher_has_name():
    assert hasattr(sistedesMM_Publisher, "name")
    descriptor = None
    for klass in sistedesMM_Publisher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_publisher_has_address():
    assert hasattr(sistedesMM_Publisher, "address")
    descriptor = None
    for klass in sistedesMM_Publisher.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())



def test_sistedesmm_sistedesmember_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_SistedesMember)


def test_sistedesmm_sistedesmember_constructor_exists():
    assert callable(sistedesMM_SistedesMember.__init__)


def test_sistedesmm_sistedesmember_constructor_args():
    sig = inspect.signature(sistedesMM_SistedesMember.__init__)
    params = list(sig.parameters.keys())



def test_sistedesmm_edition_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Edition)


def test_sistedesmm_edition_constructor_exists():
    assert callable(sistedesMM_Edition.__init__)


def test_sistedesmm_edition_constructor_args():
    sig = inspect.signature(sistedesMM_Edition.__init__)
    params = list(sig.parameters.keys())
    assert "year" in params, "Missing parameter 'year'"
    assert "location" in params, "Missing parameter 'location'"

def test_sistedesmm_edition_has_year():
    assert hasattr(sistedesMM_Edition, "year")
    descriptor = None
    for klass in sistedesMM_Edition.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_edition_has_location():
    assert hasattr(sistedesMM_Edition, "location")
    descriptor = None
    for klass in sistedesMM_Edition.__mro__:
        if "location" in klass.__dict__:
            descriptor = klass.__dict__["location"]
            break
    assert isinstance(descriptor, property)



def test_sistedesmm_publication_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Publication)


def test_sistedesmm_publication_constructor_exists():
    assert callable(sistedesMM_Publication.__init__)


def test_sistedesmm_publication_constructor_args():
    sig = inspect.signature(sistedesMM_Publication.__init__)
    params = list(sig.parameters.keys())



def test_sistedesmm_university_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_University)


def test_sistedesmm_university_constructor_exists():
    assert callable(sistedesMM_University.__init__)


def test_sistedesmm_university_constructor_args():
    sig = inspect.signature(sistedesMM_University.__init__)
    params = list(sig.parameters.keys())
    assert "provinceOrState" in params, "Missing parameter 'provinceOrState'"
    assert "name" in params, "Missing parameter 'name'"
    assert "country" in params, "Missing parameter 'country'"
    assert "city" in params, "Missing parameter 'city'"

def test_sistedesmm_university_has_provinceOrState():
    assert hasattr(sistedesMM_University, "provinceOrState")
    descriptor = None
    for klass in sistedesMM_University.__mro__:
        if "provinceOrState" in klass.__dict__:
            descriptor = klass.__dict__["provinceOrState"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_university_has_name():
    assert hasattr(sistedesMM_University, "name")
    descriptor = None
    for klass in sistedesMM_University.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_university_has_country():
    assert hasattr(sistedesMM_University, "country")
    descriptor = None
    for klass in sistedesMM_University.__mro__:
        if "country" in klass.__dict__:
            descriptor = klass.__dict__["country"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_university_has_city():
    assert hasattr(sistedesMM_University, "city")
    descriptor = None
    for klass in sistedesMM_University.__mro__:
        if "city" in klass.__dict__:
            descriptor = klass.__dict__["city"]
            break
    assert isinstance(descriptor, property)



def test_sistedesmm_person_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Person)


def test_sistedesmm_person_constructor_exists():
    assert callable(sistedesMM_Person.__init__)


def test_sistedesmm_person_constructor_args():
    sig = inspect.signature(sistedesMM_Person.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"
    assert "surname" in params, "Missing parameter 'surname'"
    assert "nationality" in params, "Missing parameter 'nationality'"

def test_sistedesmm_person_has_name():
    assert hasattr(sistedesMM_Person, "name")
    descriptor = None
    for klass in sistedesMM_Person.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_person_has_email():
    assert hasattr(sistedesMM_Person, "email")
    descriptor = None
    for klass in sistedesMM_Person.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_person_has_surname():
    assert hasattr(sistedesMM_Person, "surname")
    descriptor = None
    for klass in sistedesMM_Person.__mro__:
        if "surname" in klass.__dict__:
            descriptor = klass.__dict__["surname"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_person_has_nationality():
    assert hasattr(sistedesMM_Person, "nationality")
    descriptor = None
    for klass in sistedesMM_Person.__mro__:
        if "nationality" in klass.__dict__:
            descriptor = klass.__dict__["nationality"]
            break
    assert isinstance(descriptor, property)



def test_sistedesmm_journal_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Journal)


def test_sistedesmm_journal_constructor_exists():
    assert callable(sistedesMM_Journal.__init__)


def test_sistedesmm_journal_constructor_args():
    sig = inspect.signature(sistedesMM_Journal.__init__)
    params = list(sig.parameters.keys())
    assert "jcrIndexed" in params, "Missing parameter 'jcrIndexed'"
    assert "name" in params, "Missing parameter 'name'"
    assert "acronym" in params, "Missing parameter 'acronym'"

def test_sistedesmm_journal_has_jcrIndexed():
    assert hasattr(sistedesMM_Journal, "jcrIndexed")
    descriptor = None
    for klass in sistedesMM_Journal.__mro__:
        if "jcrIndexed" in klass.__dict__:
            descriptor = klass.__dict__["jcrIndexed"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_journal_has_name():
    assert hasattr(sistedesMM_Journal, "name")
    descriptor = None
    for klass in sistedesMM_Journal.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_journal_has_acronym():
    assert hasattr(sistedesMM_Journal, "acronym")
    descriptor = None
    for klass in sistedesMM_Journal.__mro__:
        if "acronym" in klass.__dict__:
            descriptor = klass.__dict__["acronym"]
            break
    assert isinstance(descriptor, property)



def test_publication_is_not_abstract():
    assert not inspect.isabstract(Publication)


def test_publication_constructor_exists():
    assert callable(Publication.__init__)


def test_publication_constructor_args():
    sig = inspect.signature(Publication.__init__)
    params = list(sig.parameters.keys())



def test_sistedesmm_book_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Book)


def test_sistedesmm_book_constructor_exists():
    assert callable(sistedesMM_Book.__init__)


def test_sistedesmm_book_constructor_args():
    sig = inspect.signature(sistedesMM_Book.__init__)
    params = list(sig.parameters.keys())
    assert "series" in params, "Missing parameter 'series'"
    assert "year" in params, "Missing parameter 'year'"
    assert "edition" in params, "Missing parameter 'edition'"
    assert "volume" in params, "Missing parameter 'volume'"
    assert "title" in params, "Missing parameter 'title'"
    assert "month" in params, "Missing parameter 'month'"
    assert "isbn" in params, "Missing parameter 'isbn'"

def test_sistedesmm_book_has_series():
    assert hasattr(sistedesMM_Book, "series")
    descriptor = None
    for klass in sistedesMM_Book.__mro__:
        if "series" in klass.__dict__:
            descriptor = klass.__dict__["series"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_book_has_year():
    assert hasattr(sistedesMM_Book, "year")
    descriptor = None
    for klass in sistedesMM_Book.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_book_has_edition():
    assert hasattr(sistedesMM_Book, "edition")
    descriptor = None
    for klass in sistedesMM_Book.__mro__:
        if "edition" in klass.__dict__:
            descriptor = klass.__dict__["edition"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_book_has_volume():
    assert hasattr(sistedesMM_Book, "volume")
    descriptor = None
    for klass in sistedesMM_Book.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_book_has_title():
    assert hasattr(sistedesMM_Book, "title")
    descriptor = None
    for klass in sistedesMM_Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_book_has_month():
    assert hasattr(sistedesMM_Book, "month")
    descriptor = None
    for klass in sistedesMM_Book.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_book_has_isbn():
    assert hasattr(sistedesMM_Book, "isbn")
    descriptor = None
    for klass in sistedesMM_Book.__mro__:
        if "isbn" in klass.__dict__:
            descriptor = klass.__dict__["isbn"]
            break
    assert isinstance(descriptor, property)



def test_sistedesmm_inproceedings_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_InProceedings)


def test_sistedesmm_inproceedings_constructor_exists():
    assert callable(sistedesMM_InProceedings.__init__)


def test_sistedesmm_inproceedings_constructor_args():
    sig = inspect.signature(sistedesMM_InProceedings.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "title" in params, "Missing parameter 'title'"
    assert "year" in params, "Missing parameter 'year'"
    assert "bookTitle" in params, "Missing parameter 'bookTitle'"
    assert "toPage" in params, "Missing parameter 'toPage'"
    assert "fromPage" in params, "Missing parameter 'fromPage'"

def test_sistedesmm_inproceedings_has_month():
    assert hasattr(sistedesMM_InProceedings, "month")
    descriptor = None
    for klass in sistedesMM_InProceedings.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_inproceedings_has_title():
    assert hasattr(sistedesMM_InProceedings, "title")
    descriptor = None
    for klass in sistedesMM_InProceedings.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_inproceedings_has_year():
    assert hasattr(sistedesMM_InProceedings, "year")
    descriptor = None
    for klass in sistedesMM_InProceedings.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_inproceedings_has_bookTitle():
    assert hasattr(sistedesMM_InProceedings, "bookTitle")
    descriptor = None
    for klass in sistedesMM_InProceedings.__mro__:
        if "bookTitle" in klass.__dict__:
            descriptor = klass.__dict__["bookTitle"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_inproceedings_has_toPage():
    assert hasattr(sistedesMM_InProceedings, "toPage")
    descriptor = None
    for klass in sistedesMM_InProceedings.__mro__:
        if "toPage" in klass.__dict__:
            descriptor = klass.__dict__["toPage"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_inproceedings_has_fromPage():
    assert hasattr(sistedesMM_InProceedings, "fromPage")
    descriptor = None
    for klass in sistedesMM_InProceedings.__mro__:
        if "fromPage" in klass.__dict__:
            descriptor = klass.__dict__["fromPage"]
            break
    assert isinstance(descriptor, property)



def test_sistedesmm_article_is_not_abstract():
    assert not inspect.isabstract(sistedesMM_Article)


def test_sistedesmm_article_constructor_exists():
    assert callable(sistedesMM_Article.__init__)


def test_sistedesmm_article_constructor_args():
    sig = inspect.signature(sistedesMM_Article.__init__)
    params = list(sig.parameters.keys())
    assert "month" in params, "Missing parameter 'month'"
    assert "fromPage" in params, "Missing parameter 'fromPage'"
    assert "toPage" in params, "Missing parameter 'toPage'"
    assert "number" in params, "Missing parameter 'number'"
    assert "year" in params, "Missing parameter 'year'"
    assert "title" in params, "Missing parameter 'title'"
    assert "volume" in params, "Missing parameter 'volume'"

def test_sistedesmm_article_has_month():
    assert hasattr(sistedesMM_Article, "month")
    descriptor = None
    for klass in sistedesMM_Article.__mro__:
        if "month" in klass.__dict__:
            descriptor = klass.__dict__["month"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_article_has_fromPage():
    assert hasattr(sistedesMM_Article, "fromPage")
    descriptor = None
    for klass in sistedesMM_Article.__mro__:
        if "fromPage" in klass.__dict__:
            descriptor = klass.__dict__["fromPage"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_article_has_toPage():
    assert hasattr(sistedesMM_Article, "toPage")
    descriptor = None
    for klass in sistedesMM_Article.__mro__:
        if "toPage" in klass.__dict__:
            descriptor = klass.__dict__["toPage"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_article_has_number():
    assert hasattr(sistedesMM_Article, "number")
    descriptor = None
    for klass in sistedesMM_Article.__mro__:
        if "number" in klass.__dict__:
            descriptor = klass.__dict__["number"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_article_has_year():
    assert hasattr(sistedesMM_Article, "year")
    descriptor = None
    for klass in sistedesMM_Article.__mro__:
        if "year" in klass.__dict__:
            descriptor = klass.__dict__["year"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_article_has_title():
    assert hasattr(sistedesMM_Article, "title")
    descriptor = None
    for klass in sistedesMM_Article.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_sistedesmm_article_has_volume():
    assert hasattr(sistedesMM_Article, "volume")
    descriptor = None
    for klass in sistedesMM_Article.__mro__:
        if "volume" in klass.__dict__:
            descriptor = klass.__dict__["volume"]
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
sistedesMM_Editor_strategy = st.builds(
    sistedesMM_Editor,
    name=
        safe_text
)
sistedesMM_Publisher_strategy = st.builds(
    sistedesMM_Publisher,
    name=
        safe_text,
    address=
        safe_text
)
Person_strategy = st.builds(
    Person,
)
sistedesMM_SistedesMember_strategy = st.builds(
    sistedesMM_SistedesMember,
)
sistedesMM_Edition_strategy = st.builds(
    sistedesMM_Edition,
    year=
        st.integers(),
    location=
        safe_text
)
sistedesMM_Publication_strategy = st.builds(
    sistedesMM_Publication,
)
sistedesMM_University_strategy = st.builds(
    sistedesMM_University,
    provinceOrState=
        safe_text,
    name=
        safe_text,
    country=
        safe_text,
    city=
        safe_text
)
sistedesMM_Person_strategy = st.builds(
    sistedesMM_Person,
    name=
        safe_text,
    email=
        safe_text,
    surname=
        safe_text,
    nationality=
        safe_text
)
sistedesMM_Journal_strategy = st.builds(
    sistedesMM_Journal,
    jcrIndexed=
        st.booleans(),
    name=
        safe_text,
    acronym=
        safe_text
)
Publication_strategy = st.builds(
    Publication,
)
sistedesMM_Book_strategy = st.builds(
    sistedesMM_Book,
    series=
        safe_text,
    year=
        st.integers(),
    edition=
        st.integers(),
    volume=
        safe_text,
    title=
        safe_text,
    month=
        safe_text,
    isbn=
        safe_text
)
sistedesMM_InProceedings_strategy = st.builds(
    sistedesMM_InProceedings,
    month=
        safe_text,
    title=
        safe_text,
    year=
        st.integers(),
    bookTitle=
        safe_text,
    toPage=
        safe_text,
    fromPage=
        safe_text
)
sistedesMM_Article_strategy = st.builds(
    sistedesMM_Article,
    month=
        safe_text,
    fromPage=
        st.integers(),
    toPage=
        st.integers(),
    number=
        st.integers(),
    year=
        st.integers(),
    title=
        safe_text,
    volume=
        safe_text
)

@given(instance=sistedesMM_Editor_strategy)
@settings(max_examples=50)
def test_sistedesmm_editor_instantiation(instance):
    assert isinstance(instance, sistedesMM_Editor)



@given(instance=sistedesMM_Editor_strategy)
def test_sistedesmm_editor_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=sistedesMM_Publisher_strategy)
@settings(max_examples=50)
def test_sistedesmm_publisher_instantiation(instance):
    assert isinstance(instance, sistedesMM_Publisher)



@given(instance=sistedesMM_Publisher_strategy)
def test_sistedesmm_publisher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sistedesMM_Publisher_strategy)
def test_sistedesmm_publisher_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)

@given(instance=sistedesMM_SistedesMember_strategy)
@settings(max_examples=50)
def test_sistedesmm_sistedesmember_instantiation(instance):
    assert isinstance(instance, sistedesMM_SistedesMember)

@given(instance=sistedesMM_Edition_strategy)
@settings(max_examples=50)
def test_sistedesmm_edition_instantiation(instance):
    assert isinstance(instance, sistedesMM_Edition)



@given(instance=sistedesMM_Edition_strategy)
def test_sistedesmm_edition_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=sistedesMM_Edition_strategy)
def test_sistedesmm_edition_location_setter(instance):
    original = instance.location
    instance.location = original
    assert instance.location == original

@given(instance=sistedesMM_Publication_strategy)
@settings(max_examples=50)
def test_sistedesmm_publication_instantiation(instance):
    assert isinstance(instance, sistedesMM_Publication)

@given(instance=sistedesMM_University_strategy)
@settings(max_examples=50)
def test_sistedesmm_university_instantiation(instance):
    assert isinstance(instance, sistedesMM_University)



@given(instance=sistedesMM_University_strategy)
def test_sistedesmm_university_provinceOrState_setter(instance):
    original = instance.provinceOrState
    instance.provinceOrState = original
    assert instance.provinceOrState == original



@given(instance=sistedesMM_University_strategy)
def test_sistedesmm_university_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sistedesMM_University_strategy)
def test_sistedesmm_university_country_setter(instance):
    original = instance.country
    instance.country = original
    assert instance.country == original



@given(instance=sistedesMM_University_strategy)
def test_sistedesmm_university_city_setter(instance):
    original = instance.city
    instance.city = original
    assert instance.city == original

@given(instance=sistedesMM_Person_strategy)
@settings(max_examples=50)
def test_sistedesmm_person_instantiation(instance):
    assert isinstance(instance, sistedesMM_Person)



@given(instance=sistedesMM_Person_strategy)
def test_sistedesmm_person_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sistedesMM_Person_strategy)
def test_sistedesmm_person_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=sistedesMM_Person_strategy)
def test_sistedesmm_person_surname_setter(instance):
    original = instance.surname
    instance.surname = original
    assert instance.surname == original



@given(instance=sistedesMM_Person_strategy)
def test_sistedesmm_person_nationality_setter(instance):
    original = instance.nationality
    instance.nationality = original
    assert instance.nationality == original

@given(instance=sistedesMM_Journal_strategy)
@settings(max_examples=50)
def test_sistedesmm_journal_instantiation(instance):
    assert isinstance(instance, sistedesMM_Journal)



@given(instance=sistedesMM_Journal_strategy)
def test_sistedesmm_journal_jcrIndexed_setter(instance):
    original = instance.jcrIndexed
    instance.jcrIndexed = original
    assert instance.jcrIndexed == original



@given(instance=sistedesMM_Journal_strategy)
def test_sistedesmm_journal_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=sistedesMM_Journal_strategy)
def test_sistedesmm_journal_acronym_setter(instance):
    original = instance.acronym
    instance.acronym = original
    assert instance.acronym == original

@given(instance=Publication_strategy)
@settings(max_examples=50)
def test_publication_instantiation(instance):
    assert isinstance(instance, Publication)

@given(instance=sistedesMM_Book_strategy)
@settings(max_examples=50)
def test_sistedesmm_book_instantiation(instance):
    assert isinstance(instance, sistedesMM_Book)



@given(instance=sistedesMM_Book_strategy)
def test_sistedesmm_book_series_setter(instance):
    original = instance.series
    instance.series = original
    assert instance.series == original



@given(instance=sistedesMM_Book_strategy)
def test_sistedesmm_book_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=sistedesMM_Book_strategy)
def test_sistedesmm_book_edition_setter(instance):
    original = instance.edition
    instance.edition = original
    assert instance.edition == original



@given(instance=sistedesMM_Book_strategy)
def test_sistedesmm_book_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original



@given(instance=sistedesMM_Book_strategy)
def test_sistedesmm_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=sistedesMM_Book_strategy)
def test_sistedesmm_book_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=sistedesMM_Book_strategy)
def test_sistedesmm_book_isbn_setter(instance):
    original = instance.isbn
    instance.isbn = original
    assert instance.isbn == original

@given(instance=sistedesMM_InProceedings_strategy)
@settings(max_examples=50)
def test_sistedesmm_inproceedings_instantiation(instance):
    assert isinstance(instance, sistedesMM_InProceedings)



@given(instance=sistedesMM_InProceedings_strategy)
def test_sistedesmm_inproceedings_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_sistedesmm_inproceedings_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_sistedesmm_inproceedings_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_sistedesmm_inproceedings_bookTitle_setter(instance):
    original = instance.bookTitle
    instance.bookTitle = original
    assert instance.bookTitle == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_sistedesmm_inproceedings_toPage_setter(instance):
    original = instance.toPage
    instance.toPage = original
    assert instance.toPage == original



@given(instance=sistedesMM_InProceedings_strategy)
def test_sistedesmm_inproceedings_fromPage_setter(instance):
    original = instance.fromPage
    instance.fromPage = original
    assert instance.fromPage == original

@given(instance=sistedesMM_Article_strategy)
@settings(max_examples=50)
def test_sistedesmm_article_instantiation(instance):
    assert isinstance(instance, sistedesMM_Article)



@given(instance=sistedesMM_Article_strategy)
def test_sistedesmm_article_month_setter(instance):
    original = instance.month
    instance.month = original
    assert instance.month == original



@given(instance=sistedesMM_Article_strategy)
def test_sistedesmm_article_fromPage_setter(instance):
    original = instance.fromPage
    instance.fromPage = original
    assert instance.fromPage == original



@given(instance=sistedesMM_Article_strategy)
def test_sistedesmm_article_toPage_setter(instance):
    original = instance.toPage
    instance.toPage = original
    assert instance.toPage == original



@given(instance=sistedesMM_Article_strategy)
def test_sistedesmm_article_number_setter(instance):
    original = instance.number
    instance.number = original
    assert instance.number == original



@given(instance=sistedesMM_Article_strategy)
def test_sistedesmm_article_year_setter(instance):
    original = instance.year
    instance.year = original
    assert instance.year == original



@given(instance=sistedesMM_Article_strategy)
def test_sistedesmm_article_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=sistedesMM_Article_strategy)
def test_sistedesmm_article_volume_setter(instance):
    original = instance.volume
    instance.volume = original
    assert instance.volume == original
