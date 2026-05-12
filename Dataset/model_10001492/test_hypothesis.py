import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date

from python_code import (
    publisher,
    book,
    DBA,
    loan_book,
    date,
    librarian,
    student,
    ordinary_user,
    user,
    remove_title_UseCase,
    buy_book_from_publisher_UseCase,
    check_account__UseCase,
    update_details_UseCase,
    add_book_UseCase,
    maintenance_database_UseCase,
    DBA_Actor,
    system_Component,
    display_details_UseCase,
    publish_book_UseCase,
    buy_book_from_author_UseCase,
    publisher_Actor,
    remove_reservation_UseCase,
    issue_book_UseCase,
    make_reservation_UseCase,
    search_for_book_UseCase,
    librarian_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_publisher_is_not_abstract():
    assert not inspect.isabstract(publisher)


def test_publisher_constructor_exists():
    assert callable(publisher.__init__)


def test_publisher_constructor_args():
    sig = inspect.signature(publisher.__init__)
    params = list(sig.parameters.keys())
    assert "name" in params, "Missing parameter 'name'"
    assert "id" in params, "Missing parameter 'id'"
    assert "email" in params, "Missing parameter 'email'"
    assert "address" in params, "Missing parameter 'address'"
    assert "website" in params, "Missing parameter 'website'"

def test_publisher_has_name():
    assert hasattr(publisher, "name")
    descriptor = None
    for klass in publisher.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_publisher_has_id():
    assert hasattr(publisher, "id")
    descriptor = None
    for klass in publisher.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_publisher_has_email():
    assert hasattr(publisher, "email")
    descriptor = None
    for klass in publisher.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_publisher_has_address():
    assert hasattr(publisher, "address")
    descriptor = None
    for klass in publisher.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_publisher_has_website():
    assert hasattr(publisher, "website")
    descriptor = None
    for klass in publisher.__mro__:
        if "website" in klass.__dict__:
            descriptor = klass.__dict__["website"]
            break
    assert isinstance(descriptor, property)



def test_book_is_not_abstract():
    assert not inspect.isabstract(book)


def test_book_constructor_exists():
    assert callable(book.__init__)


def test_book_constructor_args():
    sig = inspect.signature(book.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "pages" in params, "Missing parameter 'pages'"
    assert "title" in params, "Missing parameter 'title'"
    assert "ISBN" in params, "Missing parameter 'ISBN'"
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "type" in params, "Missing parameter 'type'"

def test_book_has_author():
    assert hasattr(book, "author")
    descriptor = None
    for klass in book.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book_has_pages():
    assert hasattr(book, "pages")
    descriptor = None
    for klass in book.__mro__:
        if "pages" in klass.__dict__:
            descriptor = klass.__dict__["pages"]
            break
    assert isinstance(descriptor, property)

def test_book_has_title():
    assert hasattr(book, "title")
    descriptor = None
    for klass in book.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_book_has_ISBN():
    assert hasattr(book, "ISBN")
    descriptor = None
    for klass in book.__mro__:
        if "ISBN" in klass.__dict__:
            descriptor = klass.__dict__["ISBN"]
            break
    assert isinstance(descriptor, property)

def test_book_has_publisher():
    assert hasattr(book, "publisher")
    descriptor = None
    for klass in book.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_book_has_type():
    assert hasattr(book, "type")
    descriptor = None
    for klass in book.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)



def test_dba_is_not_abstract():
    assert not inspect.isabstract(DBA)


def test_dba_constructor_exists():
    assert callable(DBA.__init__)


def test_dba_constructor_args():
    sig = inspect.signature(DBA.__init__)
    params = list(sig.parameters.keys())
    assert "ID" in params, "Missing parameter 'ID'"
    assert "name" in params, "Missing parameter 'name'"
    assert "email" in params, "Missing parameter 'email'"

def test_dba_has_ID():
    assert hasattr(DBA, "ID")
    descriptor = None
    for klass in DBA.__mro__:
        if "ID" in klass.__dict__:
            descriptor = klass.__dict__["ID"]
            break
    assert isinstance(descriptor, property)

def test_dba_has_name():
    assert hasattr(DBA, "name")
    descriptor = None
    for klass in DBA.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_dba_has_email():
    assert hasattr(DBA, "email")
    descriptor = None
    for klass in DBA.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_loan_book_is_not_abstract():
    assert not inspect.isabstract(loan_book)


def test_loan_book_constructor_exists():
    assert callable(loan_book.__init__)


def test_loan_book_constructor_args():
    sig = inspect.signature(loan_book.__init__)
    params = list(sig.parameters.keys())
    assert "cost" in params, "Missing parameter 'cost'"
    assert "loan_date" in params, "Missing parameter 'loan_date'"
    assert "due_date" in params, "Missing parameter 'due_date'"
    assert "returned_date" in params, "Missing parameter 'returned_date'"
    assert "id" in params, "Missing parameter 'id'"

def test_loan_book_has_cost():
    assert hasattr(loan_book, "cost")
    descriptor = None
    for klass in loan_book.__mro__:
        if "cost" in klass.__dict__:
            descriptor = klass.__dict__["cost"]
            break
    assert isinstance(descriptor, property)

def test_loan_book_has_loan_date():
    assert hasattr(loan_book, "loan_date")
    descriptor = None
    for klass in loan_book.__mro__:
        if "loan_date" in klass.__dict__:
            descriptor = klass.__dict__["loan_date"]
            break
    assert isinstance(descriptor, property)

def test_loan_book_has_due_date():
    assert hasattr(loan_book, "due_date")
    descriptor = None
    for klass in loan_book.__mro__:
        if "due_date" in klass.__dict__:
            descriptor = klass.__dict__["due_date"]
            break
    assert isinstance(descriptor, property)

def test_loan_book_has_returned_date():
    assert hasattr(loan_book, "returned_date")
    descriptor = None
    for klass in loan_book.__mro__:
        if "returned_date" in klass.__dict__:
            descriptor = klass.__dict__["returned_date"]
            break
    assert isinstance(descriptor, property)

def test_loan_book_has_id():
    assert hasattr(loan_book, "id")
    descriptor = None
    for klass in loan_book.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_date_is_not_abstract():
    assert not inspect.isabstract(date)


def test_date_constructor_exists():
    assert callable(date.__init__)


def test_date_constructor_args():
    sig = inspect.signature(date.__init__)
    params = list(sig.parameters.keys())



def test_librarian_is_not_abstract():
    assert not inspect.isabstract(librarian)


def test_librarian_constructor_exists():
    assert callable(librarian.__init__)


def test_librarian_constructor_args():
    sig = inspect.signature(librarian.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "email" in params, "Missing parameter 'email'"
    assert "birth_date" in params, "Missing parameter 'birth_date'"
    assert "id" in params, "Missing parameter 'id'"
    assert "name" in params, "Missing parameter 'name'"
    assert "hire_date" in params, "Missing parameter 'hire_date'"
    assert "job" in params, "Missing parameter 'job'"

def test_librarian_has_address():
    assert hasattr(librarian, "address")
    descriptor = None
    for klass in librarian.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_email():
    assert hasattr(librarian, "email")
    descriptor = None
    for klass in librarian.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_birth_date():
    assert hasattr(librarian, "birth_date")
    descriptor = None
    for klass in librarian.__mro__:
        if "birth_date" in klass.__dict__:
            descriptor = klass.__dict__["birth_date"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_id():
    assert hasattr(librarian, "id")
    descriptor = None
    for klass in librarian.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_name():
    assert hasattr(librarian, "name")
    descriptor = None
    for klass in librarian.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_hire_date():
    assert hasattr(librarian, "hire_date")
    descriptor = None
    for klass in librarian.__mro__:
        if "hire_date" in klass.__dict__:
            descriptor = klass.__dict__["hire_date"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_job():
    assert hasattr(librarian, "job")
    descriptor = None
    for klass in librarian.__mro__:
        if "job" in klass.__dict__:
            descriptor = klass.__dict__["job"]
            break
    assert isinstance(descriptor, property)



def test_student_is_not_abstract():
    assert not inspect.isabstract(student)


def test_student_constructor_exists():
    assert callable(student.__init__)


def test_student_constructor_args():
    sig = inspect.signature(student.__init__)
    params = list(sig.parameters.keys())
    assert "student_card" in params, "Missing parameter 'student_card'"

def test_student_has_student_card():
    assert hasattr(student, "student_card")
    descriptor = None
    for klass in student.__mro__:
        if "student_card" in klass.__dict__:
            descriptor = klass.__dict__["student_card"]
            break
    assert isinstance(descriptor, property)



def test_ordinary_user_is_not_abstract():
    assert not inspect.isabstract(ordinary_user)


def test_ordinary_user_constructor_exists():
    assert callable(ordinary_user.__init__)


def test_ordinary_user_constructor_args():
    sig = inspect.signature(ordinary_user.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_user_constructor_exists():
    assert callable(user.__init__)


def test_user_constructor_args():
    sig = inspect.signature(user.__init__)
    params = list(sig.parameters.keys())
    assert "last_name" in params, "Missing parameter 'last_name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "card" in params, "Missing parameter 'card'"
    assert "id" in params, "Missing parameter 'id'"
    assert "phone_number" in params, "Missing parameter 'phone_number'"
    assert "first_name" in params, "Missing parameter 'first_name'"
    assert "email" in params, "Missing parameter 'email'"

def test_user_has_last_name():
    assert hasattr(user, "last_name")
    descriptor = None
    for klass in user.__mro__:
        if "last_name" in klass.__dict__:
            descriptor = klass.__dict__["last_name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_address():
    assert hasattr(user, "address")
    descriptor = None
    for klass in user.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_user_has_card():
    assert hasattr(user, "card")
    descriptor = None
    for klass in user.__mro__:
        if "card" in klass.__dict__:
            descriptor = klass.__dict__["card"]
            break
    assert isinstance(descriptor, property)

def test_user_has_id():
    assert hasattr(user, "id")
    descriptor = None
    for klass in user.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_user_has_phone_number():
    assert hasattr(user, "phone_number")
    descriptor = None
    for klass in user.__mro__:
        if "phone_number" in klass.__dict__:
            descriptor = klass.__dict__["phone_number"]
            break
    assert isinstance(descriptor, property)

def test_user_has_first_name():
    assert hasattr(user, "first_name")
    descriptor = None
    for klass in user.__mro__:
        if "first_name" in klass.__dict__:
            descriptor = klass.__dict__["first_name"]
            break
    assert isinstance(descriptor, property)

def test_user_has_email():
    assert hasattr(user, "email")
    descriptor = None
    for klass in user.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)



def test_remove_title_usecase_is_not_abstract():
    assert not inspect.isabstract(remove_title_UseCase)


def test_remove_title_usecase_constructor_exists():
    assert callable(remove_title_UseCase.__init__)


def test_remove_title_usecase_constructor_args():
    sig = inspect.signature(remove_title_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_buy_book_from_publisher_usecase_is_not_abstract():
    assert not inspect.isabstract(buy_book_from_publisher_UseCase)


def test_buy_book_from_publisher_usecase_constructor_exists():
    assert callable(buy_book_from_publisher_UseCase.__init__)


def test_buy_book_from_publisher_usecase_constructor_args():
    sig = inspect.signature(buy_book_from_publisher_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_account__usecase_is_not_abstract():
    assert not inspect.isabstract(check_account__UseCase)


def test_check_account__usecase_constructor_exists():
    assert callable(check_account__UseCase.__init__)


def test_check_account__usecase_constructor_args():
    sig = inspect.signature(check_account__UseCase.__init__)
    params = list(sig.parameters.keys())



def test_update_details_usecase_is_not_abstract():
    assert not inspect.isabstract(update_details_UseCase)


def test_update_details_usecase_constructor_exists():
    assert callable(update_details_UseCase.__init__)


def test_update_details_usecase_constructor_args():
    sig = inspect.signature(update_details_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_add_book_usecase_is_not_abstract():
    assert not inspect.isabstract(add_book_UseCase)


def test_add_book_usecase_constructor_exists():
    assert callable(add_book_UseCase.__init__)


def test_add_book_usecase_constructor_args():
    sig = inspect.signature(add_book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_maintenance_database_usecase_is_not_abstract():
    assert not inspect.isabstract(maintenance_database_UseCase)


def test_maintenance_database_usecase_constructor_exists():
    assert callable(maintenance_database_UseCase.__init__)


def test_maintenance_database_usecase_constructor_args():
    sig = inspect.signature(maintenance_database_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_dba_actor_is_not_abstract():
    assert not inspect.isabstract(DBA_Actor)


def test_dba_actor_constructor_exists():
    assert callable(DBA_Actor.__init__)


def test_dba_actor_constructor_args():
    sig = inspect.signature(DBA_Actor.__init__)
    params = list(sig.parameters.keys())



def test_system_component_is_not_abstract():
    assert not inspect.isabstract(system_Component)


def test_system_component_constructor_exists():
    assert callable(system_Component.__init__)


def test_system_component_constructor_args():
    sig = inspect.signature(system_Component.__init__)
    params = list(sig.parameters.keys())



def test_display_details_usecase_is_not_abstract():
    assert not inspect.isabstract(display_details_UseCase)


def test_display_details_usecase_constructor_exists():
    assert callable(display_details_UseCase.__init__)


def test_display_details_usecase_constructor_args():
    sig = inspect.signature(display_details_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_publish_book_usecase_is_not_abstract():
    assert not inspect.isabstract(publish_book_UseCase)


def test_publish_book_usecase_constructor_exists():
    assert callable(publish_book_UseCase.__init__)


def test_publish_book_usecase_constructor_args():
    sig = inspect.signature(publish_book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_buy_book_from_author_usecase_is_not_abstract():
    assert not inspect.isabstract(buy_book_from_author_UseCase)


def test_buy_book_from_author_usecase_constructor_exists():
    assert callable(buy_book_from_author_UseCase.__init__)


def test_buy_book_from_author_usecase_constructor_args():
    sig = inspect.signature(buy_book_from_author_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_publisher_actor_is_not_abstract():
    assert not inspect.isabstract(publisher_Actor)


def test_publisher_actor_constructor_exists():
    assert callable(publisher_Actor.__init__)


def test_publisher_actor_constructor_args():
    sig = inspect.signature(publisher_Actor.__init__)
    params = list(sig.parameters.keys())



def test_remove_reservation_usecase_is_not_abstract():
    assert not inspect.isabstract(remove_reservation_UseCase)


def test_remove_reservation_usecase_constructor_exists():
    assert callable(remove_reservation_UseCase.__init__)


def test_remove_reservation_usecase_constructor_args():
    sig = inspect.signature(remove_reservation_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_issue_book_usecase_is_not_abstract():
    assert not inspect.isabstract(issue_book_UseCase)


def test_issue_book_usecase_constructor_exists():
    assert callable(issue_book_UseCase.__init__)


def test_issue_book_usecase_constructor_args():
    sig = inspect.signature(issue_book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_make_reservation_usecase_is_not_abstract():
    assert not inspect.isabstract(make_reservation_UseCase)


def test_make_reservation_usecase_constructor_exists():
    assert callable(make_reservation_UseCase.__init__)


def test_make_reservation_usecase_constructor_args():
    sig = inspect.signature(make_reservation_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_search_for_book_usecase_is_not_abstract():
    assert not inspect.isabstract(search_for_book_UseCase)


def test_search_for_book_usecase_constructor_exists():
    assert callable(search_for_book_UseCase.__init__)


def test_search_for_book_usecase_constructor_args():
    sig = inspect.signature(search_for_book_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_librarian_actor_is_not_abstract():
    assert not inspect.isabstract(librarian_Actor)


def test_librarian_actor_constructor_exists():
    assert callable(librarian_Actor.__init__)


def test_librarian_actor_constructor_args():
    sig = inspect.signature(librarian_Actor.__init__)
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
publisher_strategy = st.builds(
    publisher,
    name=
        safe_text,
    id=
        st.integers(),
    email=
        safe_text,
    address=
        safe_text,
    website=
        safe_text
)
book_strategy = st.builds(
    book,
    author=
        safe_text,
    pages=
        st.integers(),
    title=
        safe_text,
    ISBN=
        st.integers(),
    publisher=
        safe_text,
    type=
        safe_text
)
DBA_strategy = st.builds(
    DBA,
    ID=
        st.integers(),
    name=
        safe_text,
    email=
        safe_text
)
loan_book_strategy = st.builds(
    loan_book,
    cost=
        st.integers(),
    loan_date=
        st.dates(),
    due_date=
        st.dates(),
    returned_date=
        st.dates(),
    id=
        st.integers()
)
date_strategy = st.builds(
    date,
)
librarian_strategy = st.builds(
    librarian,
    address=
        safe_text,
    email=
        safe_text,
    birth_date=
        st.dates(),
    id=
        st.integers(),
    name=
        safe_text,
    hire_date=
        st.dates(),
    job=
        safe_text
)
student_strategy = st.builds(
    student,
    student_card=
        st.integers()
)
ordinary_user_strategy = st.builds(
    ordinary_user,
)
user_strategy = st.builds(
    user,
    last_name=
        safe_text,
    address=
        safe_text,
    card=
        st.integers(),
    id=
        st.integers(),
    phone_number=
        st.integers(),
    first_name=
        safe_text,
    email=
        safe_text
)
remove_title_UseCase_strategy = st.builds(
    remove_title_UseCase,
)
buy_book_from_publisher_UseCase_strategy = st.builds(
    buy_book_from_publisher_UseCase,
)
check_account__UseCase_strategy = st.builds(
    check_account__UseCase,
)
update_details_UseCase_strategy = st.builds(
    update_details_UseCase,
)
add_book_UseCase_strategy = st.builds(
    add_book_UseCase,
)
maintenance_database_UseCase_strategy = st.builds(
    maintenance_database_UseCase,
)
DBA_Actor_strategy = st.builds(
    DBA_Actor,
)
system_Component_strategy = st.builds(
    system_Component,
)
display_details_UseCase_strategy = st.builds(
    display_details_UseCase,
)
publish_book_UseCase_strategy = st.builds(
    publish_book_UseCase,
)
buy_book_from_author_UseCase_strategy = st.builds(
    buy_book_from_author_UseCase,
)
publisher_Actor_strategy = st.builds(
    publisher_Actor,
)
remove_reservation_UseCase_strategy = st.builds(
    remove_reservation_UseCase,
)
issue_book_UseCase_strategy = st.builds(
    issue_book_UseCase,
)
make_reservation_UseCase_strategy = st.builds(
    make_reservation_UseCase,
)
search_for_book_UseCase_strategy = st.builds(
    search_for_book_UseCase,
)
librarian_Actor_strategy = st.builds(
    librarian_Actor,
)

@given(instance=publisher_strategy)
@settings(max_examples=50)
def test_publisher_instantiation(instance):
    assert isinstance(instance, publisher)

@given(instance=publisher_strategy)
def test_publisher_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=publisher_strategy)
def test_publisher_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=publisher_strategy)
def test_publisher_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=publisher_strategy)
def test_publisher_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=publisher_strategy)
def test_publisher_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=publisher_strategy)
def test_publisher_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=publisher_strategy)
def test_publisher_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=publisher_strategy)
def test_publisher_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=publisher_strategy)
def test_publisher_website_type(instance):
    assert isinstance(instance.website, str)


@given(instance=publisher_strategy)
def test_publisher_website_setter(instance):
    original = instance.website
    instance.website = original
    assert instance.website == original

@given(instance=book_strategy)
@settings(max_examples=50)
def test_book_instantiation(instance):
    assert isinstance(instance, book)

@given(instance=book_strategy)
def test_book_author_type(instance):
    assert isinstance(instance.author, str)


@given(instance=book_strategy)
def test_book_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original

@given(instance=book_strategy)
def test_book_pages_type(instance):
    assert isinstance(instance.pages, int)


@given(instance=book_strategy)
def test_book_pages_setter(instance):
    original = instance.pages
    instance.pages = original
    assert instance.pages == original

@given(instance=book_strategy)
def test_book_title_type(instance):
    assert isinstance(instance.title, str)


@given(instance=book_strategy)
def test_book_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original

@given(instance=book_strategy)
def test_book_ISBN_type(instance):
    assert isinstance(instance.ISBN, int)


@given(instance=book_strategy)
def test_book_ISBN_setter(instance):
    original = instance.ISBN
    instance.ISBN = original
    assert instance.ISBN == original

@given(instance=book_strategy)
def test_book_publisher_type(instance):
    assert isinstance(instance.publisher, str)


@given(instance=book_strategy)
def test_book_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original

@given(instance=book_strategy)
def test_book_type_type(instance):
    assert isinstance(instance.type, str)


@given(instance=book_strategy)
def test_book_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original

@given(instance=DBA_strategy)
@settings(max_examples=50)
def test_dba_instantiation(instance):
    assert isinstance(instance, DBA)

@given(instance=DBA_strategy)
def test_dba_ID_type(instance):
    assert isinstance(instance.ID, int)


@given(instance=DBA_strategy)
def test_dba_ID_setter(instance):
    original = instance.ID
    instance.ID = original
    assert instance.ID == original

@given(instance=DBA_strategy)
def test_dba_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=DBA_strategy)
def test_dba_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=DBA_strategy)
def test_dba_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=DBA_strategy)
def test_dba_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=loan_book_strategy)
@settings(max_examples=50)
def test_loan_book_instantiation(instance):
    assert isinstance(instance, loan_book)

@given(instance=loan_book_strategy)
def test_loan_book_cost_type(instance):
    assert isinstance(instance.cost, int)


@given(instance=loan_book_strategy)
def test_loan_book_cost_setter(instance):
    original = instance.cost
    instance.cost = original
    assert instance.cost == original

@given(instance=loan_book_strategy)
def test_loan_book_loan_date_type(instance):
    assert isinstance(instance.loan_date, date)


@given(instance=loan_book_strategy)
def test_loan_book_loan_date_setter(instance):
    original = instance.loan_date
    instance.loan_date = original
    assert instance.loan_date == original

@given(instance=loan_book_strategy)
def test_loan_book_due_date_type(instance):
    assert isinstance(instance.due_date, date)


@given(instance=loan_book_strategy)
def test_loan_book_due_date_setter(instance):
    original = instance.due_date
    instance.due_date = original
    assert instance.due_date == original

@given(instance=loan_book_strategy)
def test_loan_book_returned_date_type(instance):
    assert isinstance(instance.returned_date, date)


@given(instance=loan_book_strategy)
def test_loan_book_returned_date_setter(instance):
    original = instance.returned_date
    instance.returned_date = original
    assert instance.returned_date == original

@given(instance=loan_book_strategy)
def test_loan_book_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=loan_book_strategy)
def test_loan_book_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=date_strategy)
@settings(max_examples=50)
def test_date_instantiation(instance):
    assert isinstance(instance, date)

@given(instance=librarian_strategy)
@settings(max_examples=50)
def test_librarian_instantiation(instance):
    assert isinstance(instance, librarian)

@given(instance=librarian_strategy)
def test_librarian_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=librarian_strategy)
def test_librarian_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=librarian_strategy)
def test_librarian_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=librarian_strategy)
def test_librarian_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=librarian_strategy)
def test_librarian_birth_date_type(instance):
    assert isinstance(instance.birth_date, date)


@given(instance=librarian_strategy)
def test_librarian_birth_date_setter(instance):
    original = instance.birth_date
    instance.birth_date = original
    assert instance.birth_date == original

@given(instance=librarian_strategy)
def test_librarian_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=librarian_strategy)
def test_librarian_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=librarian_strategy)
def test_librarian_name_type(instance):
    assert isinstance(instance.name, str)


@given(instance=librarian_strategy)
def test_librarian_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original

@given(instance=librarian_strategy)
def test_librarian_hire_date_type(instance):
    assert isinstance(instance.hire_date, date)


@given(instance=librarian_strategy)
def test_librarian_hire_date_setter(instance):
    original = instance.hire_date
    instance.hire_date = original
    assert instance.hire_date == original

@given(instance=librarian_strategy)
def test_librarian_job_type(instance):
    assert isinstance(instance.job, str)


@given(instance=librarian_strategy)
def test_librarian_job_setter(instance):
    original = instance.job
    instance.job = original
    assert instance.job == original

@given(instance=student_strategy)
@settings(max_examples=50)
def test_student_instantiation(instance):
    assert isinstance(instance, student)

@given(instance=student_strategy)
def test_student_student_card_type(instance):
    assert isinstance(instance.student_card, int)


@given(instance=student_strategy)
def test_student_student_card_setter(instance):
    original = instance.student_card
    instance.student_card = original
    assert instance.student_card == original

@given(instance=ordinary_user_strategy)
@settings(max_examples=50)
def test_ordinary_user_instantiation(instance):
    assert isinstance(instance, ordinary_user)

@given(instance=user_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, user)

@given(instance=user_strategy)
def test_user_last_name_type(instance):
    assert isinstance(instance.last_name, str)


@given(instance=user_strategy)
def test_user_last_name_setter(instance):
    original = instance.last_name
    instance.last_name = original
    assert instance.last_name == original

@given(instance=user_strategy)
def test_user_address_type(instance):
    assert isinstance(instance.address, str)


@given(instance=user_strategy)
def test_user_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original

@given(instance=user_strategy)
def test_user_card_type(instance):
    assert isinstance(instance.card, int)


@given(instance=user_strategy)
def test_user_card_setter(instance):
    original = instance.card
    instance.card = original
    assert instance.card == original

@given(instance=user_strategy)
def test_user_id_type(instance):
    assert isinstance(instance.id, int)


@given(instance=user_strategy)
def test_user_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=user_strategy)
def test_user_phone_number_type(instance):
    assert isinstance(instance.phone_number, int)


@given(instance=user_strategy)
def test_user_phone_number_setter(instance):
    original = instance.phone_number
    instance.phone_number = original
    assert instance.phone_number == original

@given(instance=user_strategy)
def test_user_first_name_type(instance):
    assert isinstance(instance.first_name, str)


@given(instance=user_strategy)
def test_user_first_name_setter(instance):
    original = instance.first_name
    instance.first_name = original
    assert instance.first_name == original

@given(instance=user_strategy)
def test_user_email_type(instance):
    assert isinstance(instance.email, str)


@given(instance=user_strategy)
def test_user_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original

@given(instance=remove_title_UseCase_strategy)
@settings(max_examples=50)
def test_remove_title_usecase_instantiation(instance):
    assert isinstance(instance, remove_title_UseCase)

@given(instance=buy_book_from_publisher_UseCase_strategy)
@settings(max_examples=50)
def test_buy_book_from_publisher_usecase_instantiation(instance):
    assert isinstance(instance, buy_book_from_publisher_UseCase)

@given(instance=check_account__UseCase_strategy)
@settings(max_examples=50)
def test_check_account__usecase_instantiation(instance):
    assert isinstance(instance, check_account__UseCase)

@given(instance=update_details_UseCase_strategy)
@settings(max_examples=50)
def test_update_details_usecase_instantiation(instance):
    assert isinstance(instance, update_details_UseCase)

@given(instance=add_book_UseCase_strategy)
@settings(max_examples=50)
def test_add_book_usecase_instantiation(instance):
    assert isinstance(instance, add_book_UseCase)

@given(instance=maintenance_database_UseCase_strategy)
@settings(max_examples=50)
def test_maintenance_database_usecase_instantiation(instance):
    assert isinstance(instance, maintenance_database_UseCase)

@given(instance=DBA_Actor_strategy)
@settings(max_examples=50)
def test_dba_actor_instantiation(instance):
    assert isinstance(instance, DBA_Actor)

@given(instance=system_Component_strategy)
@settings(max_examples=50)
def test_system_component_instantiation(instance):
    assert isinstance(instance, system_Component)

@given(instance=display_details_UseCase_strategy)
@settings(max_examples=50)
def test_display_details_usecase_instantiation(instance):
    assert isinstance(instance, display_details_UseCase)

@given(instance=publish_book_UseCase_strategy)
@settings(max_examples=50)
def test_publish_book_usecase_instantiation(instance):
    assert isinstance(instance, publish_book_UseCase)

@given(instance=buy_book_from_author_UseCase_strategy)
@settings(max_examples=50)
def test_buy_book_from_author_usecase_instantiation(instance):
    assert isinstance(instance, buy_book_from_author_UseCase)

@given(instance=publisher_Actor_strategy)
@settings(max_examples=50)
def test_publisher_actor_instantiation(instance):
    assert isinstance(instance, publisher_Actor)

@given(instance=remove_reservation_UseCase_strategy)
@settings(max_examples=50)
def test_remove_reservation_usecase_instantiation(instance):
    assert isinstance(instance, remove_reservation_UseCase)

@given(instance=issue_book_UseCase_strategy)
@settings(max_examples=50)
def test_issue_book_usecase_instantiation(instance):
    assert isinstance(instance, issue_book_UseCase)

@given(instance=make_reservation_UseCase_strategy)
@settings(max_examples=50)
def test_make_reservation_usecase_instantiation(instance):
    assert isinstance(instance, make_reservation_UseCase)

@given(instance=search_for_book_UseCase_strategy)
@settings(max_examples=50)
def test_search_for_book_usecase_instantiation(instance):
    assert isinstance(instance, search_for_book_UseCase)

@given(instance=librarian_Actor_strategy)
@settings(max_examples=50)
def test_librarian_actor_instantiation(instance):
    assert isinstance(instance, librarian_Actor)
