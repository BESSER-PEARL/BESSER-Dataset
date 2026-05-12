import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    extlibrary__15IX8G60EeGkd4g88tZXfA,
    extlibrary_TitledItem,
    extlibrary_Addressable,
    _15N3gm60EeGkd4g88tZXfA,
    extlibrary_Employee,
    extlibrary_Writer,
    extlibrary_Borrower,
    extlibrary__15N3gm60EeGkd4g88tZXfA,
    extlibrary_Lendable,
    extlibrary_Item,
    extlibrary_CirculatingItem,
    _9M9ys29IEeGekPcBm25hwQ,
    extlibrary_Periodical,
    extlibrary_Magazine,
    _15LbQG60EeGkd4g88tZXfA,
    extlibrary_AudioVisualItem,
    extlibrary_BookOnTape,
    extlibrary_VideoCassette,
    extlibrary_Book,
    extlibrary__148KsW60EeGkd4g88tZXfA,
    extlibrary__146VgG60EeGkd4g88tZXfA,
    extlibrary__15Hw4m60EeGkd4g88tZXfA,
    extlibrary__15NQcW60EeGkd4g88tZXfA,
    extlibrary__15OekG60EeGkd4g88tZXfA,
    _15OelG60EeGkd4g88tZXfA,
    extlibrary_Person,
    extlibrary_Library,
    extlibrary__15CRUW60EeGkd4g88tZXfA,
    BookCategory,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_extlibrary__15ix8g60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary__15IX8G60EeGkd4g88tZXfA)


def test_extlibrary__15ix8g60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary__15IX8G60EeGkd4g88tZXfA.__init__)


def test_extlibrary__15ix8g60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary__15IX8G60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_titleditem_is_not_abstract():
    assert not inspect.isabstract(extlibrary_TitledItem)


def test_extlibrary_titleditem_constructor_exists():
    assert callable(extlibrary_TitledItem.__init__)


def test_extlibrary_titleditem_constructor_args():
    sig = inspect.signature(extlibrary_TitledItem.__init__)
    params = list(sig.parameters.keys())
    assert "title" in params, "Missing parameter 'title'"

def test_extlibrary_titleditem_has_title():
    assert hasattr(extlibrary_TitledItem, "title")
    descriptor = None
    for klass in extlibrary_TitledItem.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_addressable_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Addressable)


def test_extlibrary_addressable_constructor_exists():
    assert callable(extlibrary_Addressable.__init__)


def test_extlibrary_addressable_constructor_args():
    sig = inspect.signature(extlibrary_Addressable.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"

def test_extlibrary_addressable_has_address():
    assert hasattr(extlibrary_Addressable, "address")
    descriptor = None
    for klass in extlibrary_Addressable.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)



def test__15n3gm60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(_15N3gm60EeGkd4g88tZXfA)


def test__15n3gm60eegkd4g88tzxfa_constructor_exists():
    assert callable(_15N3gm60EeGkd4g88tZXfA.__init__)


def test__15n3gm60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(_15N3gm60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_employee_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Employee)


def test_extlibrary_employee_constructor_exists():
    assert callable(extlibrary_Employee.__init__)


def test_extlibrary_employee_constructor_args():
    sig = inspect.signature(extlibrary_Employee.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_writer_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Writer)


def test_extlibrary_writer_constructor_exists():
    assert callable(extlibrary_Writer.__init__)


def test_extlibrary_writer_constructor_args():
    sig = inspect.signature(extlibrary_Writer.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"

def test_extlibrary_writer_has_name():
    assert hasattr(extlibrary_Writer, "name")
    descriptor = None
    for klass in extlibrary_Writer.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_borrower_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Borrower)


def test_extlibrary_borrower_constructor_exists():
    assert callable(extlibrary_Borrower.__init__)


def test_extlibrary_borrower_constructor_args():
    sig = inspect.signature(extlibrary_Borrower.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary__15n3gm60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary__15N3gm60EeGkd4g88tZXfA)


def test_extlibrary__15n3gm60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary__15N3gm60EeGkd4g88tZXfA.__init__)


def test_extlibrary__15n3gm60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary__15N3gm60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_lendable_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Lendable)


def test_extlibrary_lendable_constructor_exists():
    assert callable(extlibrary_Lendable.__init__)


def test_extlibrary_lendable_constructor_args():
    sig = inspect.signature(extlibrary_Lendable.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"

def test_extlibrary_lendable_has_copies():
    assert hasattr(extlibrary_Lendable, "copies")
    descriptor = None
    for klass in extlibrary_Lendable.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_item_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Item)


def test_extlibrary_item_constructor_exists():
    assert callable(extlibrary_Item.__init__)


def test_extlibrary_item_constructor_args():
    sig = inspect.signature(extlibrary_Item.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_extlibrary_item_has_publicationDate():
    assert hasattr(extlibrary_Item, "publicationDate")
    descriptor = None
    for klass in extlibrary_Item.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_circulatingitem_is_not_abstract():
    assert not inspect.isabstract(extlibrary_CirculatingItem)


def test_extlibrary_circulatingitem_constructor_exists():
    assert callable(extlibrary_CirculatingItem.__init__)


def test_extlibrary_circulatingitem_constructor_args():
    sig = inspect.signature(extlibrary_CirculatingItem.__init__)
    params = list(sig.parameters.keys())
    assert "copies" in params, "Missing parameter 'copies'"
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"

def test_extlibrary_circulatingitem_has_copies():
    assert hasattr(extlibrary_CirculatingItem, "copies")
    descriptor = None
    for klass in extlibrary_CirculatingItem.__mro__:
        if "copies" in klass.__dict__:
            descriptor = klass.__dict__["copies"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_circulatingitem_has_publicationDate():
    assert hasattr(extlibrary_CirculatingItem, "publicationDate")
    descriptor = None
    for klass in extlibrary_CirculatingItem.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)



def test__9m9ys29ieegekpcbm25hwq_is_not_abstract():
    assert not inspect.isabstract(_9M9ys29IEeGekPcBm25hwQ)


def test__9m9ys29ieegekpcbm25hwq_constructor_exists():
    assert callable(_9M9ys29IEeGekPcBm25hwQ.__init__)


def test__9m9ys29ieegekpcbm25hwq_constructor_args():
    sig = inspect.signature(_9M9ys29IEeGekPcBm25hwQ.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_periodical_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Periodical)


def test_extlibrary_periodical_constructor_exists():
    assert callable(extlibrary_Periodical.__init__)


def test_extlibrary_periodical_constructor_args():
    sig = inspect.signature(extlibrary_Periodical.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"
    assert "issuesPerYear" in params, "Missing parameter 'issuesPerYear'"

def test_extlibrary_periodical_has_publicationDate():
    assert hasattr(extlibrary_Periodical, "publicationDate")
    descriptor = None
    for klass in extlibrary_Periodical.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_periodical_has_issuesPerYear():
    assert hasattr(extlibrary_Periodical, "issuesPerYear")
    descriptor = None
    for klass in extlibrary_Periodical.__mro__:
        if "issuesPerYear" in klass.__dict__:
            descriptor = klass.__dict__["issuesPerYear"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_magazine_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Magazine)


def test_extlibrary_magazine_constructor_exists():
    assert callable(extlibrary_Magazine.__init__)


def test_extlibrary_magazine_constructor_args():
    sig = inspect.signature(extlibrary_Magazine.__init__)
    params = list(sig.parameters.keys())
    assert "publicationDate" in params, "Missing parameter 'publicationDate'"
    assert "issuesPerYear" in params, "Missing parameter 'issuesPerYear'"

def test_extlibrary_magazine_has_publicationDate():
    assert hasattr(extlibrary_Magazine, "publicationDate")
    descriptor = None
    for klass in extlibrary_Magazine.__mro__:
        if "publicationDate" in klass.__dict__:
            descriptor = klass.__dict__["publicationDate"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_magazine_has_issuesPerYear():
    assert hasattr(extlibrary_Magazine, "issuesPerYear")
    descriptor = None
    for klass in extlibrary_Magazine.__mro__:
        if "issuesPerYear" in klass.__dict__:
            descriptor = klass.__dict__["issuesPerYear"]
            break
    assert isinstance(descriptor, property)



def test__15lbqg60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(_15LbQG60EeGkd4g88tZXfA)


def test__15lbqg60eegkd4g88tzxfa_constructor_exists():
    assert callable(_15LbQG60EeGkd4g88tZXfA.__init__)


def test__15lbqg60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(_15LbQG60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_audiovisualitem_is_not_abstract():
    assert not inspect.isabstract(extlibrary_AudioVisualItem)


def test_extlibrary_audiovisualitem_constructor_exists():
    assert callable(extlibrary_AudioVisualItem.__init__)


def test_extlibrary_audiovisualitem_constructor_args():
    sig = inspect.signature(extlibrary_AudioVisualItem.__init__)
    params = list(sig.parameters.keys())
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "damaged" in params, "Missing parameter 'damaged'"

def test_extlibrary_audiovisualitem_has_minutes():
    assert hasattr(extlibrary_AudioVisualItem, "minutes")
    descriptor = None
    for klass in extlibrary_AudioVisualItem.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_audiovisualitem_has_damaged():
    assert hasattr(extlibrary_AudioVisualItem, "damaged")
    descriptor = None
    for klass in extlibrary_AudioVisualItem.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_bookontape_is_not_abstract():
    assert not inspect.isabstract(extlibrary_BookOnTape)


def test_extlibrary_bookontape_constructor_exists():
    assert callable(extlibrary_BookOnTape.__init__)


def test_extlibrary_bookontape_constructor_args():
    sig = inspect.signature(extlibrary_BookOnTape.__init__)
    params = list(sig.parameters.keys())
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "damaged" in params, "Missing parameter 'damaged'"

def test_extlibrary_bookontape_has_minutes():
    assert hasattr(extlibrary_BookOnTape, "minutes")
    descriptor = None
    for klass in extlibrary_BookOnTape.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_bookontape_has_damaged():
    assert hasattr(extlibrary_BookOnTape, "damaged")
    descriptor = None
    for klass in extlibrary_BookOnTape.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_videocassette_is_not_abstract():
    assert not inspect.isabstract(extlibrary_VideoCassette)


def test_extlibrary_videocassette_constructor_exists():
    assert callable(extlibrary_VideoCassette.__init__)


def test_extlibrary_videocassette_constructor_args():
    sig = inspect.signature(extlibrary_VideoCassette.__init__)
    params = list(sig.parameters.keys())
    assert "minutes" in params, "Missing parameter 'minutes'"
    assert "damaged" in params, "Missing parameter 'damaged'"

def test_extlibrary_videocassette_has_minutes():
    assert hasattr(extlibrary_VideoCassette, "minutes")
    descriptor = None
    for klass in extlibrary_VideoCassette.__mro__:
        if "minutes" in klass.__dict__:
            descriptor = klass.__dict__["minutes"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_videocassette_has_damaged():
    assert hasattr(extlibrary_VideoCassette, "damaged")
    descriptor = None
    for klass in extlibrary_VideoCassette.__mro__:
        if "damaged" in klass.__dict__:
            descriptor = klass.__dict__["damaged"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_book_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Book)


def test_extlibrary_book_constructor_exists():
    assert callable(extlibrary_Book.__init__)


def test_extlibrary_book_constructor_args():
    sig = inspect.signature(extlibrary_Book.__init__)
    params = list(sig.parameters.keys())
    assert "pages" in params, "Missing parameter 'pages'"
    assert "subtitle" in params, "Missing parameter 'subtitle'"
    assert "category" in params, "Missing parameter 'category'"

def test_extlibrary_book_has_pages():
    assert hasattr(extlibrary_Book, "pages")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_book_has_subtitle():
    assert hasattr(extlibrary_Book, "subtitle")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "subtitle" in klass.__dict__:
            descriptor = klass.__dict__["subtitle"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_book_has_category():
    assert hasattr(extlibrary_Book, "category")
    descriptor = None
    for klass in extlibrary_Book.__mro__:
        if "category" in klass.__dict__:
            descriptor = klass.__dict__["category"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary__148ksw60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary__148KsW60EeGkd4g88tZXfA)


def test_extlibrary__148ksw60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary__148KsW60EeGkd4g88tZXfA.__init__)


def test_extlibrary__148ksw60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary__148KsW60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary__146vgg60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary__146VgG60EeGkd4g88tZXfA)


def test_extlibrary__146vgg60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary__146VgG60EeGkd4g88tZXfA.__init__)


def test_extlibrary__146vgg60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary__146VgG60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary__15hw4m60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary__15Hw4m60EeGkd4g88tZXfA)


def test_extlibrary__15hw4m60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary__15Hw4m60EeGkd4g88tZXfA.__init__)


def test_extlibrary__15hw4m60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary__15Hw4m60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary__15nqcw60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary__15NQcW60EeGkd4g88tZXfA)


def test_extlibrary__15nqcw60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary__15NQcW60EeGkd4g88tZXfA.__init__)


def test_extlibrary__15nqcw60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary__15NQcW60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary__15oekg60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary__15OekG60EeGkd4g88tZXfA)


def test_extlibrary__15oekg60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary__15OekG60EeGkd4g88tZXfA.__init__)


def test_extlibrary__15oekg60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary__15OekG60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test__15oelg60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(_15OelG60EeGkd4g88tZXfA)


def test__15oelg60eegkd4g88tzxfa_constructor_exists():
    assert callable(_15OelG60EeGkd4g88tZXfA.__init__)


def test__15oelg60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(_15OelG60EeGkd4g88tZXfA.__init__)
    params = list(sig.parameters.keys())



def test_extlibrary_person_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Person)


def test_extlibrary_person_constructor_exists():
    assert callable(extlibrary_Person.__init__)


def test_extlibrary_person_constructor_args():
    sig = inspect.signature(extlibrary_Person.__init__)
    params = list(sig.parameters.keys())
    assert "familyName" in params, "Missing parameter 'familyName'"
    assert "firstName" in params, "Missing parameter 'firstName'"

def test_extlibrary_person_has_familyName():
    assert hasattr(extlibrary_Person, "familyName")
    descriptor = None
    for klass in extlibrary_Person.__mro__:
        if "familyName" in klass.__dict__:
            descriptor = klass.__dict__["familyName"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_person_has_firstName():
    assert hasattr(extlibrary_Person, "firstName")
    descriptor = None
    for klass in extlibrary_Person.__mro__:
        if "firstName" in klass.__dict__:
            descriptor = klass.__dict__["firstName"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary_library_is_not_abstract():
    assert not inspect.isabstract(extlibrary_Library)


def test_extlibrary_library_constructor_exists():
    assert callable(extlibrary_Library.__init__)


def test_extlibrary_library_constructor_args():
    sig = inspect.signature(extlibrary_Library.__init__)
    params = list(sig.parameters.keys())
    assert "people" in params, "Missing parameter 'people'"
    assert "name" in params, "Missing parameter 'name'"

def test_extlibrary_library_has_people():
    assert hasattr(extlibrary_Library, "people")
    descriptor = None
    for klass in extlibrary_Library.__mro__:
        if "people" in klass.__dict__:
            descriptor = klass.__dict__["people"]
            break
    assert isinstance(descriptor, property)

def test_extlibrary_library_has_name():
    assert hasattr(extlibrary_Library, "name")
    descriptor = None
    for klass in extlibrary_Library.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_extlibrary__15cruw60eegkd4g88tzxfa_is_not_abstract():
    assert not inspect.isabstract(extlibrary__15CRUW60EeGkd4g88tZXfA)


def test_extlibrary__15cruw60eegkd4g88tzxfa_constructor_exists():
    assert callable(extlibrary__15CRUW60EeGkd4g88tZXfA.__init__)


def test_extlibrary__15cruw60eegkd4g88tzxfa_constructor_args():
    sig = inspect.signature(extlibrary__15CRUW60EeGkd4g88tZXfA.__init__)
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
        "Manhwa",
        "ScienceFiction",
        "Manga",
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
extlibrary__15IX8G60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary__15IX8G60EeGkd4g88tZXfA,
)
extlibrary_TitledItem_strategy = st.builds(
    extlibrary_TitledItem,
    title=
        safe_text
)
extlibrary_Addressable_strategy = st.builds(
    extlibrary_Addressable,
    address=
        safe_text
)
_15N3gm60EeGkd4g88tZXfA_strategy = st.builds(
    _15N3gm60EeGkd4g88tZXfA,
)
extlibrary_Employee_strategy = st.builds(
    extlibrary_Employee,
)
extlibrary_Writer_strategy = st.builds(
    extlibrary_Writer,
    name=
        safe_text
)
extlibrary_Borrower_strategy = st.builds(
    extlibrary_Borrower,
)
extlibrary__15N3gm60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary__15N3gm60EeGkd4g88tZXfA,
)
extlibrary_Lendable_strategy = st.builds(
    extlibrary_Lendable,
    copies=
        st.integers()
)
extlibrary_Item_strategy = st.builds(
    extlibrary_Item,
    publicationDate=
        st.dates()
)
extlibrary_CirculatingItem_strategy = st.builds(
    extlibrary_CirculatingItem,
    copies=
        st.integers(),
    publicationDate=
        st.dates()
)
_9M9ys29IEeGekPcBm25hwQ_strategy = st.builds(
    _9M9ys29IEeGekPcBm25hwQ,
)
extlibrary_Periodical_strategy = st.builds(
    extlibrary_Periodical,
    publicationDate=
        st.dates(),
    issuesPerYear=
        st.integers()
)
extlibrary_Magazine_strategy = st.builds(
    extlibrary_Magazine,
    publicationDate=
        st.dates(),
    issuesPerYear=
        st.integers()
)
_15LbQG60EeGkd4g88tZXfA_strategy = st.builds(
    _15LbQG60EeGkd4g88tZXfA,
)
extlibrary_AudioVisualItem_strategy = st.builds(
    extlibrary_AudioVisualItem,
    minutes=
        st.integers(),
    damaged=
        st.booleans()
)
extlibrary_BookOnTape_strategy = st.builds(
    extlibrary_BookOnTape,
    minutes=
        st.integers(),
    damaged=
        st.booleans()
)
extlibrary_VideoCassette_strategy = st.builds(
    extlibrary_VideoCassette,
    minutes=
        st.integers(),
    damaged=
        st.booleans()
)
extlibrary_Book_strategy = st.builds(
    extlibrary_Book,
    pages=
        st.integers(),
    subtitle=
        safe_text,
    category=
        safe_text
)
extlibrary__148KsW60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary__148KsW60EeGkd4g88tZXfA,
)
extlibrary__146VgG60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary__146VgG60EeGkd4g88tZXfA,
)
extlibrary__15Hw4m60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary__15Hw4m60EeGkd4g88tZXfA,
)
extlibrary__15NQcW60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary__15NQcW60EeGkd4g88tZXfA,
)
extlibrary__15OekG60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary__15OekG60EeGkd4g88tZXfA,
)
_15OelG60EeGkd4g88tZXfA_strategy = st.builds(
    _15OelG60EeGkd4g88tZXfA,
)
extlibrary_Person_strategy = st.builds(
    extlibrary_Person,
    familyName=
        safe_text,
    firstName=
        safe_text
)
extlibrary_Library_strategy = st.builds(
    extlibrary_Library,
    people=
        safe_text,
    name=
        safe_text
)
extlibrary__15CRUW60EeGkd4g88tZXfA_strategy = st.builds(
    extlibrary__15CRUW60EeGkd4g88tZXfA,
)

@given(instance=extlibrary__15IX8G60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary__15ix8g60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary__15IX8G60EeGkd4g88tZXfA)

@given(instance=extlibrary_TitledItem_strategy)
@settings(max_examples=50)
def test_extlibrary_titleditem_instantiation(instance):
    assert isinstance(instance, extlibrary_TitledItem)



@given(instance=extlibrary_TitledItem_strategy)
def test_extlibrary_titleditem_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=extlibrary_Addressable_strategy)
@settings(max_examples=50)
def test_extlibrary_addressable_instantiation(instance):
    assert isinstance(instance, extlibrary_Addressable)



@given(instance=extlibrary_Addressable_strategy)
def test_extlibrary_addressable_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=_15N3gm60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test__15n3gm60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, _15N3gm60EeGkd4g88tZXfA)

@given(instance=extlibrary_Employee_strategy)
@settings(max_examples=50)
def test_extlibrary_employee_instantiation(instance):
    assert isinstance(instance, extlibrary_Employee)

@given(instance=extlibrary_Writer_strategy)
@settings(max_examples=50)
def test_extlibrary_writer_instantiation(instance):
    assert isinstance(instance, extlibrary_Writer)



@given(instance=extlibrary_Writer_strategy)
def test_extlibrary_writer_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extlibrary_Borrower_strategy)
@settings(max_examples=50)
def test_extlibrary_borrower_instantiation(instance):
    assert isinstance(instance, extlibrary_Borrower)

@given(instance=extlibrary__15N3gm60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary__15n3gm60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary__15N3gm60EeGkd4g88tZXfA)

@given(instance=extlibrary_Lendable_strategy)
@settings(max_examples=50)
def test_extlibrary_lendable_instantiation(instance):
    assert isinstance(instance, extlibrary_Lendable)



@given(instance=extlibrary_Lendable_strategy)
def test_extlibrary_lendable_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original

@given(instance=extlibrary_Item_strategy)
@settings(max_examples=50)
def test_extlibrary_item_instantiation(instance):
    assert isinstance(instance, extlibrary_Item)



@given(instance=extlibrary_Item_strategy)
def test_extlibrary_item_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=extlibrary_CirculatingItem_strategy)
@settings(max_examples=50)
def test_extlibrary_circulatingitem_instantiation(instance):
    assert isinstance(instance, extlibrary_CirculatingItem)



@given(instance=extlibrary_CirculatingItem_strategy)
def test_extlibrary_circulatingitem_copies_setter(instance):
    original = instance.copies
    instance.copies = original
    assert instance.copies == original



@given(instance=extlibrary_CirculatingItem_strategy)
def test_extlibrary_circulatingitem_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original

@given(instance=_9M9ys29IEeGekPcBm25hwQ_strategy)
@settings(max_examples=50)
def test__9m9ys29ieegekpcbm25hwq_instantiation(instance):
    assert isinstance(instance, _9M9ys29IEeGekPcBm25hwQ)

@given(instance=extlibrary_Periodical_strategy)
@settings(max_examples=50)
def test_extlibrary_periodical_instantiation(instance):
    assert isinstance(instance, extlibrary_Periodical)



@given(instance=extlibrary_Periodical_strategy)
def test_extlibrary_periodical_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original



@given(instance=extlibrary_Periodical_strategy)
def test_extlibrary_periodical_issuesPerYear_setter(instance):
    original = instance.issuesPerYear
    instance.issuesPerYear = original
    assert instance.issuesPerYear == original

@given(instance=extlibrary_Magazine_strategy)
@settings(max_examples=50)
def test_extlibrary_magazine_instantiation(instance):
    assert isinstance(instance, extlibrary_Magazine)



@given(instance=extlibrary_Magazine_strategy)
def test_extlibrary_magazine_publicationDate_setter(instance):
    original = instance.publicationDate
    instance.publicationDate = original
    assert instance.publicationDate == original



@given(instance=extlibrary_Magazine_strategy)
def test_extlibrary_magazine_issuesPerYear_setter(instance):
    original = instance.issuesPerYear
    instance.issuesPerYear = original
    assert instance.issuesPerYear == original

@given(instance=_15LbQG60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test__15lbqg60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, _15LbQG60EeGkd4g88tZXfA)

@given(instance=extlibrary_AudioVisualItem_strategy)
@settings(max_examples=50)
def test_extlibrary_audiovisualitem_instantiation(instance):
    assert isinstance(instance, extlibrary_AudioVisualItem)



@given(instance=extlibrary_AudioVisualItem_strategy)
def test_extlibrary_audiovisualitem_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original



@given(instance=extlibrary_AudioVisualItem_strategy)
def test_extlibrary_audiovisualitem_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=extlibrary_BookOnTape_strategy)
@settings(max_examples=50)
def test_extlibrary_bookontape_instantiation(instance):
    assert isinstance(instance, extlibrary_BookOnTape)



@given(instance=extlibrary_BookOnTape_strategy)
def test_extlibrary_bookontape_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original



@given(instance=extlibrary_BookOnTape_strategy)
def test_extlibrary_bookontape_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=extlibrary_VideoCassette_strategy)
@settings(max_examples=50)
def test_extlibrary_videocassette_instantiation(instance):
    assert isinstance(instance, extlibrary_VideoCassette)



@given(instance=extlibrary_VideoCassette_strategy)
def test_extlibrary_videocassette_minutes_setter(instance):
    original = instance.minutes
    instance.minutes = original
    assert instance.minutes == original



@given(instance=extlibrary_VideoCassette_strategy)
def test_extlibrary_videocassette_damaged_setter(instance):
    original = instance.damaged
    instance.damaged = original
    assert instance.damaged == original

@given(instance=extlibrary_Book_strategy)
@settings(max_examples=50)
def test_extlibrary_book_instantiation(instance):
    assert isinstance(instance, extlibrary_Book)



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_subtitle_setter(instance):
    original = instance.subtitle
    instance.subtitle = original
    assert instance.subtitle == original



@given(instance=extlibrary_Book_strategy)
def test_extlibrary_book_category_setter(instance):
    original = instance.category
    instance.category = original
    assert instance.category == original

@given(instance=extlibrary__148KsW60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary__148ksw60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary__148KsW60EeGkd4g88tZXfA)

@given(instance=extlibrary__146VgG60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary__146vgg60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary__146VgG60EeGkd4g88tZXfA)

@given(instance=extlibrary__15Hw4m60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary__15hw4m60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary__15Hw4m60EeGkd4g88tZXfA)

@given(instance=extlibrary__15NQcW60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary__15nqcw60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary__15NQcW60EeGkd4g88tZXfA)

@given(instance=extlibrary__15OekG60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary__15oekg60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary__15OekG60EeGkd4g88tZXfA)

@given(instance=_15OelG60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test__15oelg60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, _15OelG60EeGkd4g88tZXfA)

@given(instance=extlibrary_Person_strategy)
@settings(max_examples=50)
def test_extlibrary_person_instantiation(instance):
    assert isinstance(instance, extlibrary_Person)



@given(instance=extlibrary_Person_strategy)
def test_extlibrary_person_familyName_setter(instance):
    original = instance.familyName
    instance.familyName = original
    assert instance.familyName == original



@given(instance=extlibrary_Person_strategy)
def test_extlibrary_person_firstName_setter(instance):
    original = instance.firstName
    instance.firstName = original
    assert instance.firstName == original

@given(instance=extlibrary_Library_strategy)
@settings(max_examples=50)
def test_extlibrary_library_instantiation(instance):
    assert isinstance(instance, extlibrary_Library)



@given(instance=extlibrary_Library_strategy)
def test_extlibrary_library_people_setter(instance):
    original = instance.people
    instance.people = original
    assert instance.people == original



@given(instance=extlibrary_Library_strategy)
def test_extlibrary_library_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=extlibrary__15CRUW60EeGkd4g88tZXfA_strategy)
@settings(max_examples=50)
def test_extlibrary__15cruw60eegkd4g88tzxfa_instantiation(instance):
    assert isinstance(instance, extlibrary__15CRUW60EeGkd4g88tZXfA)
