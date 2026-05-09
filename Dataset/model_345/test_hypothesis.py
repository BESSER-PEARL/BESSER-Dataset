import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from classes import (
    extlibrary::Addressable,
    extlibrary::Lendable,
    extlibrary::Item,
    ::15N3gm60EeGkd4g88tZXfA,
    extlibrary::Employee,
    extlibrary::Writer,
    extlibrary::::15IX8G60EeGkd4g88tZXfA,
    extlibrary::Borrower,
    extlibrary::::15N3gm60EeGkd4g88tZXfA,
    extlibrary::Periodical,
    extlibrary::CirculatingItem,
    ::15OelG60EeGkd4g88tZXfA,
    extlibrary::Person,
    extlibrary::Library,
    extlibrary::::15CRUW60EeGkd4g88tZXfA,
    ::15LbQG60EeGkd4g88tZXfA,
    extlibrary::AudioVisualItem,
    extlibrary::VideoCassette,
    extlibrary::BookOnTape,
    extlibrary::Book,
    extlibrary::::148KsW60EeGkd4g88tZXfA,
    extlibrary::::146VgG60EeGkd4g88tZXfA,
    extlibrary::::15Hw4m60EeGkd4g88tZXfA,
    extlibrary::::15NQcW60EeGkd4g88tZXfA,
    extlibrary::::15OekG60EeGkd4g88tZXfA,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extlibrary::addressable_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Addressable)


def test_extlibrary::addressable_constructor_exists():
    assert callable(extlibrary::Addressable.__init__)


def test_extlibrary::addressable_constructor_args():
    sig = inspect.signature(extlibrary::Addressable.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_extlibrary::addressable_has_address():
    assert hasattr(extlibrary::Addressable, "address")
    descriptor = None
    for klass in extlibrary::Addressable.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::lendable_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Lendable)


def test_extlibrary::lendable_constructor_exists():
    assert callable(extlibrary::Lendable.__init__)


def test_extlibrary::lendable_constructor_args():
    sig = inspect.signature(extlibrary::Lendable.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"

def test_extlibrary::lendable_has_copies():
    assert hasattr(extlibrary::Lendable, "copies")
    descriptor = None
    for klass in extlibrary::Lendable.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::item_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Item)


def test_extlibrary::item_constructor_exists():
    assert callable(extlibrary::Item.__init__)


def test_extlibrary::item_constructor_args():
    sig = inspect.signature(extlibrary::Item.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_extlibrary::item_has_publicationDate():
    assert hasattr(extlibrary::Item, "publicationDate")
    descriptor = None
    for klass in extlibrary::Item.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test_::15n3gm60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(::15N3gm60EeGkd4g88tZXfA)


def test_::15n3gm60eegkd4g88tzxfa_constructor_exists():
    assert callable(::15N3gm60EeGkd4g88tZXfA.__init__)


def test_::15n3gm60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(::15N3gm60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::employee_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Employee)


def test_extlibrary::employee_constructor_exists():
    assert callable(extlibrary::Employee.__init__)


def test_extlibrary::employee_constructor_args():
    sig = inspect.signature(extlibrary::Employee.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::writer_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Writer)


def test_extlibrary::writer_constructor_exists():
    assert callable(extlibrary::Writer.__init__)


def test_extlibrary::writer_constructor_args():
    sig = inspect.signature(extlibrary::Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extlibrary::writer_has_name():
    assert hasattr(extlibrary::Writer, "name")
    descriptor = None
    for klass in extlibrary::Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::::15ix8g60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary::::15IX8G60EeGkd4g88tZXfA)


def test_extlibrary::::15ix8g60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary::::15IX8G60EeGkd4g88tZXfA.__init__)


def test_extlibrary::::15ix8g60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary::::15IX8G60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::borrower_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Borrower)


def test_extlibrary::borrower_constructor_exists():
    assert callable(extlibrary::Borrower.__init__)


def test_extlibrary::borrower_constructor_args():
    sig = inspect.signature(extlibrary::Borrower.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::::15n3gm60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary::::15N3gm60EeGkd4g88tZXfA)


def test_extlibrary::::15n3gm60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary::::15N3gm60EeGkd4g88tZXfA.__init__)


def test_extlibrary::::15n3gm60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary::::15N3gm60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::periodical_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Periodical)


def test_extlibrary::periodical_constructor_exists():
    assert callable(extlibrary::Periodical.__init__)


def test_extlibrary::periodical_constructor_args():
    sig = inspect.signature(extlibrary::Periodical.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "issuesPerYear" in params, "Missing parameter 'issuesPerYear'"
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_extlibrary::periodical_has_title():
    assert hasattr(extlibrary::Periodical, "title")
    descriptor = None
    for klass in extlibrary::Periodical.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::periodical_has_issuesPerYear():
    assert hasattr(extlibrary::Periodical, "issuesPerYear")
    descriptor = None
    for klass in extlibrary::Periodical.__mro__:
        if "issuesPerYear" in klass.__dict__:
            descriptor = klass.__dict__["issuesPerYear"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::periodical_has_publicationDate():
    assert hasattr(extlibrary::Periodical, "publicationDate")
    descriptor = None
    for klass in extlibrary::Periodical.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::circulatingitem_is_not_abstract():
    assert not inspect.isabstract(extlibrary::CirculatingItem)


def test_extlibrary::circulatingitem_constructor_exists():
    assert callable(extlibrary::CirculatingItem.__init__)


def test_extlibrary::circulatingitem_constructor_args():
    sig = inspect.signature(extlibrary::CirculatingItem.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"
    assert "copies" in params, "Missing parameter 'copies'"

def test_extlibrary::circulatingitem_has_publicationDate():
    assert hasattr(extlibrary::CirculatingItem, "publicationDate")
    descriptor = None
    for klass in extlibrary::CirculatingItem.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::circulatingitem_has_copies():
    assert hasattr(extlibrary::CirculatingItem, "copies")
    descriptor = None
    for klass in extlibrary::CirculatingItem.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_::15oelg60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(::15OelG60EeGkd4g88tZXfA)


def test_::15oelg60eegkd4g88tzxfa_constructor_exists():
    assert callable(::15OelG60EeGkd4g88tZXfA.__init__)


def test_::15oelg60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(::15OelG60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::person_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Person)


def test_extlibrary::person_constructor_exists():
    assert callable(extlibrary::Person.__init__)


def test_extlibrary::person_constructor_args():
    sig = inspect.signature(extlibrary::Person.__init__)
    params = list(sig.parameters.keys())
    assert "firstName" in params, "Missing parameter 'firstName'"
    assert "lastName" in params, "Missing parameter 'lastName'"

def test_extlibrary::person_has_firstName():
    assert hasattr(extlibrary::Person, "firstName")
    descriptor = None
    for klass in extlibrary::Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::person_has_lastName():
    assert hasattr(extlibrary::Person, "lastName")
    descriptor = None
    for klass in extlibrary::Person.__mro__:
        if "lastName" in klass.__dict__:
            descriptor = klass.__dict__["lastName"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::library_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Library)


def test_extlibrary::library_constructor_exists():
    assert callable(extlibrary::Library.__init__)


def test_extlibrary::library_constructor_args():
    sig = inspect.signature(extlibrary::Library.__init__)
    params = list(sig.parameters.keys())
    assert "people" in params, "Missing parameter 'people'"
    assert "name" in params, "Missing parameter 'name'"

def test_extlibrary::library_has_people():
    assert hasattr(extlibrary::Library, "people")
    descriptor = None
    for klass in extlibrary::Library.__mro__:
        if "people" in klass.__dict__:
            descriptor = klass.__dict__["people"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::library_has_name():
    assert hasattr(extlibrary::Library, "name")
    descriptor = None
    for klass in extlibrary::Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::::15cruw60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary::::15CRUW60EeGkd4g88tZXfA)


def test_extlibrary::::15cruw60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary::::15CRUW60EeGkd4g88tZXfA.__init__)


def test_extlibrary::::15cruw60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary::::15CRUW60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_::15lbqg60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(::15LbQG60EeGkd4g88tZXfA)


def test_::15lbqg60eegkd4g88tzxfa_constructor_exists():
    assert callable(::15LbQG60EeGkd4g88tZXfA.__init__)


def test_::15lbqg60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(::15LbQG60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(extlibrary::AudioVisualItem)


def test_extlibrary::audiovisualitem_constructor_exists():
    assert callable(extlibrary::AudioVisualItem.__init__)


def test_extlibrary::audiovisualitem_constructor_args():
    sig = inspect.signature(extlibrary::AudioVisualItem.__init__)
    params = list(sig.parameters.keys())
    assert "minutesLength" in params, "Missing parameter 'minutesLength'"
    assert "title" in params, "Missing parameter 'title'"
    assert "damaged" in params, "Missing parameter 'damaged'"

def test_extlibrary::audiovisualitem_has_minutesLength():
    assert hasattr(extlibrary::AudioVisualItem, "minutesLength")
    descriptor = None
    for klass in extlibrary::AudioVisualItem.__mro__:
        if "minutesLength" in klass.__dict__:
            descriptor = klass.__dict__["minutesLength"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::audiovisualitem_has_title():
    assert hasattr(extlibrary::AudioVisualItem, "title")
    descriptor = None
    for klass in extlibrary::AudioVisualItem.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::audiovisualitem_has_damaged():
    assert hasattr(extlibrary::AudioVisualItem, "damaged")
    descriptor = None
    for klass in extlibrary::AudioVisualItem.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::videocassette_is_not_abstract():
    assert not inspect.isabstract(extlibrary::VideoCassette)


def test_extlibrary::videocassette_constructor_exists():
    assert callable(extlibrary::VideoCassette.__init__)


def test_extlibrary::videocassette_constructor_args():
    sig = inspect.signature(extlibrary::VideoCassette.__init__)
    params = list(sig.parameters.keys())
    assert "minutesLength" in params, "Missing parameter 'minutesLength'"
    assert "title" in params, "Missing parameter 'title'"
    assert "damaged" in params, "Missing parameter 'damaged'"

def test_extlibrary::videocassette_has_minutesLength():
    assert hasattr(extlibrary::VideoCassette, "minutesLength")
    descriptor = None
    for klass in extlibrary::VideoCassette.__mro__:
        if "minutesLength" in klass.__dict__:
            descriptor = klass.__dict__["minutesLength"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::videocassette_has_title():
    assert hasattr(extlibrary::VideoCassette, "title")
    descriptor = None
    for klass in extlibrary::VideoCassette.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::videocassette_has_damaged():
    assert hasattr(extlibrary::VideoCassette, "damaged")
    descriptor = None
    for klass in extlibrary::VideoCassette.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::bookontape_is_not_abstract():
    assert not inspect.isabstract(extlibrary::BookOnTape)


def test_extlibrary::bookontape_constructor_exists():
    assert callable(extlibrary::BookOnTape.__init__)


def test_extlibrary::bookontape_constructor_args():
    sig = inspect.signature(extlibrary::BookOnTape.__init__)
    params = list(sig.parameters.keys())
    assert "minutesLength" in params, "Missing parameter 'minutesLength'"
    assert "title" in params, "Missing parameter 'title'"
    assert "damaged" in params, "Missing parameter 'damaged'"

def test_extlibrary::bookontape_has_minutesLength():
    assert hasattr(extlibrary::BookOnTape, "minutesLength")
    descriptor = None
    for klass in extlibrary::BookOnTape.__mro__:
        if "minutesLength" in klass.__dict__:
            descriptor = klass.__dict__["minutesLength"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::bookontape_has_title():
    assert hasattr(extlibrary::BookOnTape, "title")
    descriptor = None
    for klass in extlibrary::BookOnTape.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::bookontape_has_damaged():
    assert hasattr(extlibrary::BookOnTape, "damaged")
    descriptor = None
    for klass in extlibrary::BookOnTape.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::book_is_not_abstract():
    assert not inspect.isabstract(extlibrary::Book)


def test_extlibrary::book_constructor_exists():
    assert callable(extlibrary::Book.__init__)


def test_extlibrary::book_constructor_args():
    sig = inspect.signature(extlibrary::Book.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"
    assert "category" in params, "Missing parameter 'category'"
    assert "pages" in params, "Missing parameter 'pages'"

def test_extlibrary::book_has_title():
    assert hasattr(extlibrary::Book, "title")
    descriptor = None
    for klass in extlibrary::Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::book_has_category():
    assert hasattr(extlibrary::Book, "category")
    descriptor = None
    for klass in extlibrary::Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary::book_has_pages():
    assert hasattr(extlibrary::Book, "pages")
    descriptor = None
    for klass in extlibrary::Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary::::148ksw60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary::::148KsW60EeGkd4g88tZXfA)


def test_extlibrary::::148ksw60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary::::148KsW60EeGkd4g88tZXfA.__init__)


def test_extlibrary::::148ksw60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary::::148KsW60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::::146vgg60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary::::146VgG60EeGkd4g88tZXfA)


def test_extlibrary::::146vgg60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary::::146VgG60EeGkd4g88tZXfA.__init__)


def test_extlibrary::::146vgg60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary::::146VgG60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::::15hw4m60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary::::15Hw4m60EeGkd4g88tZXfA)


def test_extlibrary::::15hw4m60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary::::15Hw4m60EeGkd4g88tZXfA.__init__)


def test_extlibrary::::15hw4m60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary::::15Hw4m60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::::15nqcw60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary::::15NQcW60EeGkd4g88tZXfA)


def test_extlibrary::::15nqcw60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary::::15NQcW60EeGkd4g88tZXfA.__init__)


def test_extlibrary::::15nqcw60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary::::15NQcW60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary::::15oekg60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary::::15OekG60EeGkd4g88tZXfA)


def test_extlibrary::::15oekg60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary::::15OekG60EeGkd4g88tZXfA.__init__)


def test_extlibrary::::15oekg60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary::::15OekG60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())

def test_bookcategory_exists():
    # Check that the Enumeration exists
    assert BookCategory is not None

def test_bookcategory_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in BookCategory]
    expected_literals = [
        "Mystery",
        "Biography",
        "ScienceFiction",
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in BookCategory"


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
extlibrary::Addressable_strategy = st.builds(
    extlibrary::Addressable,
    address=
        safe_text
)
extlibrary::Lendable_strategy = st.builds(
    extlibrary::Lendable,
    copies=
        st.integers()
)
extlibrary::Item_strategy = st.builds(
    extlibrary::Item,
    publicationDate=
        st.dates()
)
::15N3gm60EeGkd4g88tZXfA_strategy = st.builds(
    ::15N3gm60EeGkd4g88tZXfA,
)
extlibrary::Employee_strategy = st.builds(
    extlibrary::Employee,
)
extlibrary::Writer_strategy = st.builds(
    extlibrary::Writer,
    name=
        safe_text
)
extlibrary::::15IX8G60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary::::15IX8G60EeGkd4g88tZXfA,
)
extlibrary::Borrower_strategy = st.builds(
    extlibrary::Borrower,
)
extlibrary::::15N3gm60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary::::15N3gm60EeGkd4g88tZXfA,
)
extlibrary::Periodical_strategy = st.builds(
    extlibrary::Periodical,
    title=
        safe_text,
    issuesPerYear=
        st.integers(),
    publicationDate=
        st.dates()
)
extlibrary::CirculatingItem_strategy = st.builds(
    extlibrary::CirculatingItem,
    publicationDate=
        st.dates(),
    copies=
        st.integers()
)
::15OelG60EeGkd4g88tZXfA_strategy = st.builds(
    ::15OelG60EeGkd4g88tZXfA,
)
extlibrary::Person_strategy = st.builds(
    extlibrary::Person,
    firstName=
        safe_text,
    lastName=
        safe_text
)
extlibrary::Library_strategy = st.builds(
    extlibrary::Library,
    people=
        safe_text,
    name=
        safe_text
)
extlibrary::::15CRUW60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary::::15CRUW60EeGkd4g88tZXfA,
)
::15LbQG60EeGkd4g88tZXfA_strategy = st.builds(
    ::15LbQG60EeGkd4g88tZXfA,
)
extlibrary::AudioVisualItem_strategy = st.builds(
    extlibrary::AudioVisualItem,
    minutesLength=
        st.integers(),
    title=
        safe_text,
    damaged=
        st.booleans()
)
extlibrary::VideoCassette_strategy = st.builds(
    extlibrary::VideoCassette,
    minutesLength=
        st.integers(),
    title=
        safe_text,
    damaged=
        st.booleans()
)
extlibrary::BookOnTape_strategy = st.builds(
    extlibrary::BookOnTape,
    minutesLength=
        st.integers(),
    title=
        safe_text,
    damaged=
        st.booleans()
)
extlibrary::Book_strategy = st.builds(
    extlibrary::Book,
    title=
        safe_text,
    category=
        safe_text,
    pages=
        st.integers()
)
extlibrary::::148KsW60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary::::148KsW60EeGkd4g88tZXfA,
)
extlibrary::::146VgG60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary::::146VgG60EeGkd4g88tZXfA,
)
extlibrary::::15Hw4m60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary::::15Hw4m60EeGkd4g88tZXfA,
)
extlibrary::::15NQcW60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary::::15NQcW60EeGkd4g88tZXfA,
)
extlibrary::::15OekG60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary::::15OekG60EeGkd4g88tZXfA,
)

@given(instance=extlibrary::Addressable_strategy)
@settings(max_examples=50)
def test_extlibrary::addressable_instantiation(instance):
    assert isinstance(instance, extlibrary::Addressable)

@given(instance=extlibrary::Addressable_strategy)
def test_extlibrary::addressable_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=extlibrary::Addressable_strategy)
def test_extlibrary::addressable_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=extlibrary::Lendable_strategy)
@settings(max_examples=50)
def test_extlibrary::lendable_instantiation(instance):
    assert isinstance(instance, extlibrary::Lendable)

@given(instance=extlibrary::Lendable_strategy)
def test_extlibrary::lendable_copies_type(instance):
    assert isinstance(instance.copies, int)


@given(instance=extlibrary::Lendable_strategy)
def test_extlibrary::lendable_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=extlibrary::Item_strategy)
@settings(max_examples=50)
def test_extlibrary::item_instantiation(instance):
    assert isinstance(instance, extlibrary::Item)

@given(instance=extlibrary::Item_strategy)
def test_extlibrary::item_publicationDate_type(instance):
    assert isinstance(instance.publicationDate, date)


@given(instance=extlibrary::Item_strategy)
def test_extlibrary::item_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=::15N3gm60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_::15n3gm60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, ::15N3gm60EeGkd4g88tZXfA)

@given(instance=extlibrary::Employee_strategy)
@settings(max_examples=50)
def test_extlibrary::employee_instantiation(instance):
    assert isinstance(instance, extlibrary::Employee)

@given(instance=extlibrary::Writer_strategy)
@settings(max_examples=50)
def test_extlibrary::writer_instantiation(instance):
    assert isinstance(instance, extlibrary::Writer)

@given(instance=extlibrary::Writer_strategy)
def test_extlibrary::writer_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=extlibrary::Writer_strategy)
def test_extlibrary::writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extlibrary::::15IX8G60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary::::15ix8g60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary::::15IX8G60EeGkd4g88tZXfA)

@given(instance=extlibrary::Borrower_strategy)
@settings(max_examples=50)
def test_extlibrary::borrower_instantiation(instance):
    assert isinstance(instance, extlibrary::Borrower)

@given(instance=extlibrary::::15N3gm60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary::::15n3gm60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary::::15N3gm60EeGkd4g88tZXfA)

@given(instance=extlibrary::Periodical_strategy)
@settings(max_examples=50)
def test_extlibrary::periodical_instantiation(instance):
    assert isinstance(instance, extlibrary::Periodical)

@given(instance=extlibrary::Periodical_strategy)
def test_extlibrary::periodical_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=extlibrary::Periodical_strategy)
def test_extlibrary::periodical_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=extlibrary::Periodical_strategy)
def test_extlibrary::periodical_issuesPerYear_type(instance):
    assert isinstance(instance.issuesPerYear, int)


@given(instance=extlibrary::Periodical_strategy)
def test_extlibrary::periodical_issuesPerYear_setter(instance):
    original = instance.issuesPerYear
    instance.issuesPerYear = original
    assert instance.issuesPerYear == original

@given(instance=extlibrary::Periodical_strategy)
def test_extlibrary::periodical_publicationDate_type(instance):
    assert isinstance(instance.publicationDate, date)


@given(instance=extlibrary::Periodical_strategy)
def test_extlibrary::periodical_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=extlibrary::CirculatingItem_strategy)
@settings(max_examples=50)
def test_extlibrary::circulatingitem_instantiation(instance):
    assert isinstance(instance, extlibrary::CirculatingItem)

@given(instance=extlibrary::CirculatingItem_strategy)
def test_extlibrary::circulatingitem_publicationDate_type(instance):
    assert isinstance(instance.publicationDate, date)


@given(instance=extlibrary::CirculatingItem_strategy)
def test_extlibrary::circulatingitem_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=extlibrary::CirculatingItem_strategy)
def test_extlibrary::circulatingitem_copies_type(instance):
    assert isinstance(instance.copies, int)


@given(instance=extlibrary::CirculatingItem_strategy)
def test_extlibrary::circulatingitem_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=::15OelG60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_::15oelg60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, ::15OelG60EeGkd4g88tZXfA)

@given(instance=extlibrary::Person_strategy)
@settings(max_examples=50)
def test_extlibrary::person_instantiation(instance):
    assert isinstance(instance, extlibrary::Person)

@given(instance=extlibrary::Person_strategy)
def test_extlibrary::person_firstName_type(instance):
    assert isinstance(instance.firstName, str)


@given(instance=extlibrary::Person_strategy)
def test_extlibrary::person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=extlibrary::Person_strategy)
def test_extlibrary::person_lastName_type(instance):
    assert isinstance(instance.lastName, str)


@given(instance=extlibrary::Person_strategy)
def test_extlibrary::person_lastName_setter(instance):
    original = instance.lastName
    instance.lastName = original
    assert instance.lastName == original

@given(instance=extlibrary::Library_strategy)
@settings(max_examples=50)
def test_extlibrary::library_instantiation(instance):
    assert isinstance(instance, extlibrary::Library)

@given(instance=extlibrary::Library_strategy)
def test_extlibrary::library_people_type(instance):
    assert isinstance(instance.people, str)


@given(instance=extlibrary::Library_strategy)
def test_extlibrary::library_people_setter(instance):
    original = instance.people
    instance.people = original
    assert instance.people == original

@given(instance=extlibrary::Library_strategy)
def test_extlibrary::library_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=extlibrary::Library_strategy)
def test_extlibrary::library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extlibrary::::15CRUW60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary::::15cruw60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary::::15CRUW60EeGkd4g88tZXfA)

@given(instance=::15LbQG60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_::15lbqg60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, ::15LbQG60EeGkd4g88tZXfA)

@given(instance=extlibrary::AudioVisualItem_strategy)
@settings(max_examples=50)
def test_extlibrary::audiovisualitem_instantiation(instance):
    assert isinstance(instance, extlibrary::AudioVisualItem)

@given(instance=extlibrary::AudioVisualItem_strategy)
def test_extlibrary::audiovisualitem_minutesLength_type(instance):
    assert isinstance(instance.minutesLength, int)


@given(instance=extlibrary::AudioVisualItem_strategy)
def test_extlibrary::audiovisualitem_minutesLength_setter(instance):
    original = instance.minutesLength
    instance.minutesLength = original
    assert instance.minutesLength == original

@given(instance=extlibrary::AudioVisualItem_strategy)
def test_extlibrary::audiovisualitem_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=extlibrary::AudioVisualItem_strategy)
def test_extlibrary::audiovisualitem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=extlibrary::AudioVisualItem_strategy)
def test_extlibrary::audiovisualitem_damaged_type(instance):
    assert isinstance(instance.damaged, bool)


@given(instance=extlibrary::AudioVisualItem_strategy)
def test_extlibrary::audiovisualitem_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=extlibrary::VideoCassette_strategy)
@settings(max_examples=50)
def test_extlibrary::videocassette_instantiation(instance):
    assert isinstance(instance, extlibrary::VideoCassette)

@given(instance=extlibrary::VideoCassette_strategy)
def test_extlibrary::videocassette_minutesLength_type(instance):
    assert isinstance(instance.minutesLength, int)


@given(instance=extlibrary::VideoCassette_strategy)
def test_extlibrary::videocassette_minutesLength_setter(instance):
    original = instance.minutesLength
    instance.minutesLength = original
    assert instance.minutesLength == original

@given(instance=extlibrary::VideoCassette_strategy)
def test_extlibrary::videocassette_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=extlibrary::VideoCassette_strategy)
def test_extlibrary::videocassette_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=extlibrary::VideoCassette_strategy)
def test_extlibrary::videocassette_damaged_type(instance):
    assert isinstance(instance.damaged, bool)


@given(instance=extlibrary::VideoCassette_strategy)
def test_extlibrary::videocassette_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=extlibrary::BookOnTape_strategy)
@settings(max_examples=50)
def test_extlibrary::bookontape_instantiation(instance):
    assert isinstance(instance, extlibrary::BookOnTape)

@given(instance=extlibrary::BookOnTape_strategy)
def test_extlibrary::bookontape_minutesLength_type(instance):
    assert isinstance(instance.minutesLength, int)


@given(instance=extlibrary::BookOnTape_strategy)
def test_extlibrary::bookontape_minutesLength_setter(instance):
    original = instance.minutesLength
    instance.minutesLength = original
    assert instance.minutesLength == original

@given(instance=extlibrary::BookOnTape_strategy)
def test_extlibrary::bookontape_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=extlibrary::BookOnTape_strategy)
def test_extlibrary::bookontape_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=extlibrary::BookOnTape_strategy)
def test_extlibrary::bookontape_damaged_type(instance):
    assert isinstance(instance.damaged, bool)


@given(instance=extlibrary::BookOnTape_strategy)
def test_extlibrary::bookontape_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=extlibrary::Book_strategy)
@settings(max_examples=50)
def test_extlibrary::book_instantiation(instance):
    assert isinstance(instance, extlibrary::Book)

@given(instance=extlibrary::Book_strategy)
def test_extlibrary::book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=extlibrary::Book_strategy)
def test_extlibrary::book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=extlibrary::Book_strategy)
def test_extlibrary::book_category_type(instance):
    assert isinstance(instance.category, str)


@given(instance=extlibrary::Book_strategy)
def test_extlibrary::book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=extlibrary::Book_strategy)
def test_extlibrary::book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=extlibrary::Book_strategy)
def test_extlibrary::book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=extlibrary::::148KsW60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary::::148ksw60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary::::148KsW60EeGkd4g88tZXfA)

@given(instance=extlibrary::::146VgG60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary::::146vgg60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary::::146VgG60EeGkd4g88tZXfA)

@given(instance=extlibrary::::15Hw4m60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary::::15hw4m60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary::::15Hw4m60EeGkd4g88tZXfA)

@given(instance=extlibrary::::15NQcW60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary::::15nqcw60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary::::15NQcW60EeGkd4g88tZXfA)

@given(instance=extlibrary::::15OekG60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary::::15oekg60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary::::15OekG60EeGkd4g88tZXfA)
