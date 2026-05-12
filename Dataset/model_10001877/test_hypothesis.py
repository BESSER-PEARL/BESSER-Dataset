import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Checked_Out_UseCase,
    Checked_In_UseCase,
    Acquired_UseCase,
    Retired_UseCase,
    Book_Actor,
    Library,
    Book,
    Librarian,
    Patron,
    Retirement_of_Books_UseCase,
    Acquisition_of_Books_UseCase,
    Mail_2_Week_Reminders_UseCase,
    Check_In_Book_UseCase,
    Check_Out_Book_UseCase,
    Reserve_Book_UseCase,
    Librarian_Actor,
    Patron_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_checked_out_usecase_is_not_abstract():
    assert not inspect.isabstract(Checked_Out_UseCase)


def test_checked_out_usecase_constructor_exists():
    assert callable(Checked_Out_UseCase.__init__)


def test_checked_out_usecase_constructor_args():
    sig = inspect.signature(Checked_Out_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_checked_in_usecase_is_not_abstract():
    assert not inspect.isabstract(Checked_In_UseCase)


def test_checked_in_usecase_constructor_exists():
    assert callable(Checked_In_UseCase.__init__)


def test_checked_in_usecase_constructor_args():
    sig = inspect.signature(Checked_In_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_acquired_usecase_is_not_abstract():
    assert not inspect.isabstract(Acquired_UseCase)


def test_acquired_usecase_constructor_exists():
    assert callable(Acquired_UseCase.__init__)


def test_acquired_usecase_constructor_args():
    sig = inspect.signature(Acquired_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_retired_usecase_is_not_abstract():
    assert not inspect.isabstract(Retired_UseCase)


def test_retired_usecase_constructor_exists():
    assert callable(Retired_UseCase.__init__)


def test_retired_usecase_constructor_args():
    sig = inspect.signature(Retired_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_book_actor_is_not_abstract():
    assert not inspect.isabstract(Book_Actor)


def test_book_actor_constructor_exists():
    assert callable(Book_Actor.__init__)


def test_book_actor_constructor_args():
    sig = inspect.signature(Book_Actor.__init__)
    params = list(sig.parameters.keys())



def test_library_is_not_abstract():
    assert not inspect.isabstract(Library)


def test_library_constructor_exists():
    assert callable(Library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(Library.__init__)
    params = list(sig.parameters.keys())
    assert "librarian_id" in params, "Missing parameter 'librarian_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_library_has_librarian_id():
    assert hasattr(Library, "librarian_id")
    descriptor = None
    for klass in Library.__mro__:
        if "librarian_id" in klass.__dict__:
            descriptor = klass.__dict__["librarian_id"]
            break
    assert isinstance(descriptor, property)

def test_library_has_id():
    assert hasattr(Library, "id")
    descriptor = None
    for klass in Library.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(Book)


def test_book_constructor_exists():
    assert callable(Book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(Book.__init__)
    params = list(sig.parameters.keys())
    assert "creation_date" in params, "Missing parameter 'creation_date'"
    assert "author" in params, "Missing parameter 'author'"
    assert "title" in params, "Missing parameter 'title'"
    assert "id" in params, "Missing parameter 'id'"
    assert "status" in params, "Missing parameter 'status'"

def test_book_has_creation_date():
    assert hasattr(Book, "creation_date")
    descriptor = None
    for klass in Book.__mro__:
        if "creation_date" in klass.__dict__:
            descriptor = klass.__dict__["creation_date"]
            break
    assert isinstance(descriptor, property)

def test_book_has_author():
    assert hasattr(Book, "author")
    descriptor = None
    for klass in Book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book_has_title():
    assert hasattr(Book, "title")
    descriptor = None
    for klass in Book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_book_has_id():
    assert hasattr(Book, "id")
    descriptor = None
    for klass in Book.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_book_has_status():
    assert hasattr(Book, "status")
    descriptor = None
    for klass in Book.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)



def test_librarian_is_not_abstract():
    assert not inspect.isabstract(Librarian)


def test_librarian_constructor_exists():
    assert callable(Librarian.__init__)


def test_librarian_constructor_args():
    sig = inspect.signature(Librarian.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"

def test_librarian_has_name():
    assert hasattr(Librarian, "name")
    descriptor = None
    for klass in Librarian.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_id():
    assert hasattr(Librarian, "id")
    descriptor = None
    for klass in Librarian.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_patron_is_not_abstract():
    assert not inspect.isabstract(Patron)


def test_patron_constructor_exists():
    assert callable(Patron.__init__)


def test_patron_constructor_args():
    sig = inspect.signature(Patron.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "address" in params, "Missing parameter 'address'"
    assert "id" in params, "Missing parameter 'id'"
    assert "num_books_checked_out" in params, "Missing parameter 'num_books_checked_out'"
    assert "name" in params, "Missing parameter 'name'"

def test_patron_has_status():
    assert hasattr(Patron, "status")
    descriptor = None
    for klass in Patron.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_address():
    assert hasattr(Patron, "address")
    descriptor = None
    for klass in Patron.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_id():
    assert hasattr(Patron, "id")
    descriptor = None
    for klass in Patron.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_num_books_checked_out():
    assert hasattr(Patron, "num_books_checked_out")
    descriptor = None
    for klass in Patron.__mro__:
        if "num_books_checked_out" in klass.__dict__:
            descriptor = klass.__dict__["num_books_checked_out"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_name():
    assert hasattr(Patron, "name")
    descriptor = None
    for klass in Patron.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)



def test_retirement_of_books_usecase_is_not_abstract():
    assert not inspect.isabstract(Retirement_of_Books_UseCase)


def test_retirement_of_books_usecase_constructor_exists():
    assert callable(Retirement_of_Books_UseCase.__init__)


def test_retirement_of_books_usecase_constructor_args():
    sig = inspect.signature(Retirement_of_Books_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_acquisition_of_books_usecase_is_not_abstract():
    assert not inspect.isabstract(Acquisition_of_Books_UseCase)


def test_acquisition_of_books_usecase_constructor_exists():
    assert callable(Acquisition_of_Books_UseCase.__init__)


def test_acquisition_of_books_usecase_constructor_args():
    sig = inspect.signature(Acquisition_of_Books_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_mail_2_week_reminders_usecase_is_not_abstract():
    assert not inspect.isabstract(Mail_2_Week_Reminders_UseCase)


def test_mail_2_week_reminders_usecase_constructor_exists():
    assert callable(Mail_2_Week_Reminders_UseCase.__init__)


def test_mail_2_week_reminders_usecase_constructor_args():
    sig = inspect.signature(Mail_2_Week_Reminders_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_in_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_In_Book_UseCase)


def test_check_in_book_usecase_constructor_exists():
    assert callable(Check_In_Book_UseCase.__init__)


def test_check_in_book_usecase_constructor_args():
    sig = inspect.signature(Check_In_Book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_out_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_Out_Book_UseCase)


def test_check_out_book_usecase_constructor_exists():
    assert callable(Check_Out_Book_UseCase.__init__)


def test_check_out_book_usecase_constructor_args():
    sig = inspect.signature(Check_Out_Book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_reserve_book_usecase_is_not_abstract():
    assert not inspect.isabstract(Reserve_Book_UseCase)


def test_reserve_book_usecase_constructor_exists():
    assert callable(Reserve_Book_UseCase.__init__)


def test_reserve_book_usecase_constructor_args():
    sig = inspect.signature(Reserve_Book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_librarian_actor_is_not_abstract():
    assert not inspect.isabstract(Librarian_Actor)


def test_librarian_actor_constructor_exists():
    assert callable(Librarian_Actor.__init__)


def test_librarian_actor_constructor_args():
    sig = inspect.signature(Librarian_Actor.__init__)
    params = list(sig.parameters.keys())



def test_patron_actor_is_not_abstract():
    assert not inspect.isabstract(Patron_Actor)


def test_patron_actor_constructor_exists():
    assert callable(Patron_Actor.__init__)


def test_patron_actor_constructor_args():
    sig = inspect.signature(Patron_Actor.__init__)
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
Checked_Out_UseCase_strategy = st.builds(
    Checked_Out_UseCase,
)
Checked_In_UseCase_strategy = st.builds(
    Checked_In_UseCase,
)
Acquired_UseCase_strategy = st.builds(
    Acquired_UseCase,
)
Retired_UseCase_strategy = st.builds(
    Retired_UseCase,
)
Book_Actor_strategy = st.builds(
    Book_Actor,
)
Library_strategy = st.builds(
    Library,
    librarian_id=
        st.integers(),
    id=
        st.integers()
)
Book_strategy = st.builds(
    Book,
    creation_date=
        safe_text,
    author=
        safe_text,
    title=
        safe_text,
    id=
        st.integers(),
    status=
        safe_text
)
Librarian_strategy = st.builds(
    Librarian,
    name=
        safe_text,
    id=
        st.integers()
)
Patron_strategy = st.builds(
    Patron,
    status=
        safe_text,
    address=
        safe_text,
    id=
        st.integers(),
    num_books_checked_out=
        st.integers(),
    name=
        safe_text
)
Retirement_of_Books_UseCase_strategy = st.builds(
    Retirement_of_Books_UseCase,
)
Acquisition_of_Books_UseCase_strategy = st.builds(
    Acquisition_of_Books_UseCase,
)
Mail_2_Week_Reminders_UseCase_strategy = st.builds(
    Mail_2_Week_Reminders_UseCase,
)
Check_In_Book_UseCase_strategy = st.builds(
    Check_In_Book_UseCase,
)
Check_Out_Book_UseCase_strategy = st.builds(
    Check_Out_Book_UseCase,
)
Reserve_Book_UseCase_strategy = st.builds(
    Reserve_Book_UseCase,
)
Librarian_Actor_strategy = st.builds(
    Librarian_Actor,
)
Patron_Actor_strategy = st.builds(
    Patron_Actor,
)

@given(instance=Checked_Out_UseCase_strategy)
@settings(max_examples=50)
def test_checked_out_usecase_instantiation(instance):
    assert isinstance(instance, Checked_Out_UseCase)

@given(instance=Checked_In_UseCase_strategy)
@settings(max_examples=50)
def test_checked_in_usecase_instantiation(instance):
    assert isinstance(instance, Checked_In_UseCase)

@given(instance=Acquired_UseCase_strategy)
@settings(max_examples=50)
def test_acquired_usecase_instantiation(instance):
    assert isinstance(instance, Acquired_UseCase)

@given(instance=Retired_UseCase_strategy)
@settings(max_examples=50)
def test_retired_usecase_instantiation(instance):
    assert isinstance(instance, Retired_UseCase)

@given(instance=Book_Actor_strategy)
@settings(max_examples=50)
def test_book_actor_instantiation(instance):
    assert isinstance(instance, Book_Actor)

@given(instance=Library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, Library)



@given(instance=Library_strategy)
def test_library_librarian_id_setter(instance):
    original = instance.librarian_id
    instance.librarian_id = original
    assert instance.librarian_id == original



@given(instance=Library_strategy)
def test_library_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, Book)



@given(instance=Book_strategy)
def test_book_creation_date_setter(instance):
    original = instance.creation_date
    instance.creation_date = original
    assert instance.creation_date == original



@given(instance=Book_strategy)
def test_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=Book_strategy)
def test_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Book_strategy)
def test_book_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Book_strategy)
def test_book_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original

@given(instance=Librarian_strategy)
@settings(max_examples=50)
def test_librarian_instantiation(instance):
    assert isinstance(instance, Librarian)



@given(instance=Librarian_strategy)
def test_librarian_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=Librarian_strategy)
def test_librarian_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Patron_strategy)
@settings(max_examples=50)
def test_patron_instantiation(instance):
    assert isinstance(instance, Patron)



@given(instance=Patron_strategy)
def test_patron_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Patron_strategy)
def test_patron_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Patron_strategy)
def test_patron_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Patron_strategy)
def test_patron_num_books_checked_out_setter(instance):
    original = instance.num_books_checked_out
    instance.num_books_checked_out = original
    assert instance.num_books_checked_out == original



@given(instance=Patron_strategy)
def test_patron_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=Retirement_of_Books_UseCase_strategy)
@settings(max_examples=50)
def test_retirement_of_books_usecase_instantiation(instance):
    assert isinstance(instance, Retirement_of_Books_UseCase)

@given(instance=Acquisition_of_Books_UseCase_strategy)
@settings(max_examples=50)
def test_acquisition_of_books_usecase_instantiation(instance):
    assert isinstance(instance, Acquisition_of_Books_UseCase)

@given(instance=Mail_2_Week_Reminders_UseCase_strategy)
@settings(max_examples=50)
def test_mail_2_week_reminders_usecase_instantiation(instance):
    assert isinstance(instance, Mail_2_Week_Reminders_UseCase)

@given(instance=Check_In_Book_UseCase_strategy)
@settings(max_examples=50)
def test_check_in_book_usecase_instantiation(instance):
    assert isinstance(instance, Check_In_Book_UseCase)

@given(instance=Check_Out_Book_UseCase_strategy)
@settings(max_examples=50)
def test_check_out_book_usecase_instantiation(instance):
    assert isinstance(instance, Check_Out_Book_UseCase)

@given(instance=Reserve_Book_UseCase_strategy)
@settings(max_examples=50)
def test_reserve_book_usecase_instantiation(instance):
    assert isinstance(instance, Reserve_Book_UseCase)

@given(instance=Librarian_Actor_strategy)
@settings(max_examples=50)
def test_librarian_actor_instantiation(instance):
    assert isinstance(instance, Librarian_Actor)

@given(instance=Patron_Actor_strategy)
@settings(max_examples=50)
def test_patron_actor_instantiation(instance):
    assert isinstance(instance, Patron_Actor)
