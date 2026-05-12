import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Validation_external,
    Register_Member_external,
    Return_Book_external,
    Requests_for_Book_Borrow_external,
    Pay_Fine_external,
    Issue_Book_external,
    Search_for_Books_external,
    Organise_Book_details_external,
    Librarian_Actor,
    User_Database_Actor,
    Books_Database_Actor,
    T,
    Library_Management_System_Component,
    User_Actor,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_validation_external_is_not_abstract():
    assert not inspect.isabstract(Validation_external)


def test_validation_external_constructor_exists():
    assert callable(Validation_external.__init__)


def test_validation_external_constructor_args():
    sig = inspect.signature(Validation_external.__init__)
    params = list(sig.parameters.keys())



def test_register_member_external_is_not_abstract():
    assert not inspect.isabstract(Register_Member_external)


def test_register_member_external_constructor_exists():
    assert callable(Register_Member_external.__init__)


def test_register_member_external_constructor_args():
    sig = inspect.signature(Register_Member_external.__init__)
    params = list(sig.parameters.keys())



def test_return_book_external_is_not_abstract():
    assert not inspect.isabstract(Return_Book_external)


def test_return_book_external_constructor_exists():
    assert callable(Return_Book_external.__init__)


def test_return_book_external_constructor_args():
    sig = inspect.signature(Return_Book_external.__init__)
    params = list(sig.parameters.keys())



def test_requests_for_book_borrow_external_is_not_abstract():
    assert not inspect.isabstract(Requests_for_Book_Borrow_external)


def test_requests_for_book_borrow_external_constructor_exists():
    assert callable(Requests_for_Book_Borrow_external.__init__)


def test_requests_for_book_borrow_external_constructor_args():
    sig = inspect.signature(Requests_for_Book_Borrow_external.__init__)
    params = list(sig.parameters.keys())



def test_pay_fine_external_is_not_abstract():
    assert not inspect.isabstract(Pay_Fine_external)


def test_pay_fine_external_constructor_exists():
    assert callable(Pay_Fine_external.__init__)


def test_pay_fine_external_constructor_args():
    sig = inspect.signature(Pay_Fine_external.__init__)
    params = list(sig.parameters.keys())



def test_issue_book_external_is_not_abstract():
    assert not inspect.isabstract(Issue_Book_external)


def test_issue_book_external_constructor_exists():
    assert callable(Issue_Book_external.__init__)


def test_issue_book_external_constructor_args():
    sig = inspect.signature(Issue_Book_external.__init__)
    params = list(sig.parameters.keys())



def test_search_for_books_external_is_not_abstract():
    assert not inspect.isabstract(Search_for_Books_external)


def test_search_for_books_external_constructor_exists():
    assert callable(Search_for_Books_external.__init__)


def test_search_for_books_external_constructor_args():
    sig = inspect.signature(Search_for_Books_external.__init__)
    params = list(sig.parameters.keys())



def test_organise_book_details_external_is_not_abstract():
    assert not inspect.isabstract(Organise_Book_details_external)


def test_organise_book_details_external_constructor_exists():
    assert callable(Organise_Book_details_external.__init__)


def test_organise_book_details_external_constructor_args():
    sig = inspect.signature(Organise_Book_details_external.__init__)
    params = list(sig.parameters.keys())



def test_librarian_actor_is_not_abstract():
    assert not inspect.isabstract(Librarian_Actor)


def test_librarian_actor_constructor_exists():
    assert callable(Librarian_Actor.__init__)


def test_librarian_actor_constructor_args():
    sig = inspect.signature(Librarian_Actor.__init__)
    params = list(sig.parameters.keys())



def test_user_database_actor_is_not_abstract():
    assert not inspect.isabstract(User_Database_Actor)


def test_user_database_actor_constructor_exists():
    assert callable(User_Database_Actor.__init__)


def test_user_database_actor_constructor_args():
    sig = inspect.signature(User_Database_Actor.__init__)
    params = list(sig.parameters.keys())



def test_books_database_actor_is_not_abstract():
    assert not inspect.isabstract(Books_Database_Actor)


def test_books_database_actor_constructor_exists():
    assert callable(Books_Database_Actor.__init__)


def test_books_database_actor_constructor_args():
    sig = inspect.signature(Books_Database_Actor.__init__)
    params = list(sig.parameters.keys())



def test_t_is_not_abstract():
    assert not inspect.isabstract(T)


def test_t_constructor_exists():
    assert callable(T.__init__)


def test_t_constructor_args():
    sig = inspect.signature(T.__init__)
    params = list(sig.parameters.keys())



def test_library_management_system_component_is_not_abstract():
    assert not inspect.isabstract(Library_Management_System_Component)


def test_library_management_system_component_constructor_exists():
    assert callable(Library_Management_System_Component.__init__)


def test_library_management_system_component_constructor_args():
    sig = inspect.signature(Library_Management_System_Component.__init__)
    params = list(sig.parameters.keys())



def test_user_actor_is_not_abstract():
    assert not inspect.isabstract(User_Actor)


def test_user_actor_constructor_exists():
    assert callable(User_Actor.__init__)


def test_user_actor_constructor_args():
    sig = inspect.signature(User_Actor.__init__)
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
Validation_external_strategy = st.builds(
    Validation_external,
)
Register_Member_external_strategy = st.builds(
    Register_Member_external,
)
Return_Book_external_strategy = st.builds(
    Return_Book_external,
)
Requests_for_Book_Borrow_external_strategy = st.builds(
    Requests_for_Book_Borrow_external,
)
Pay_Fine_external_strategy = st.builds(
    Pay_Fine_external,
)
Issue_Book_external_strategy = st.builds(
    Issue_Book_external,
)
Search_for_Books_external_strategy = st.builds(
    Search_for_Books_external,
)
Organise_Book_details_external_strategy = st.builds(
    Organise_Book_details_external,
)
Librarian_Actor_strategy = st.builds(
    Librarian_Actor,
)
User_Database_Actor_strategy = st.builds(
    User_Database_Actor,
)
Books_Database_Actor_strategy = st.builds(
    Books_Database_Actor,
)
T_strategy = st.builds(
    T,
)
Library_Management_System_Component_strategy = st.builds(
    Library_Management_System_Component,
)
User_Actor_strategy = st.builds(
    User_Actor,
)

@given(instance=Validation_external_strategy)
@settings(max_examples=50)
def test_validation_external_instantiation(instance):
    assert isinstance(instance, Validation_external)

@given(instance=Register_Member_external_strategy)
@settings(max_examples=50)
def test_register_member_external_instantiation(instance):
    assert isinstance(instance, Register_Member_external)

@given(instance=Return_Book_external_strategy)
@settings(max_examples=50)
def test_return_book_external_instantiation(instance):
    assert isinstance(instance, Return_Book_external)

@given(instance=Requests_for_Book_Borrow_external_strategy)
@settings(max_examples=50)
def test_requests_for_book_borrow_external_instantiation(instance):
    assert isinstance(instance, Requests_for_Book_Borrow_external)

@given(instance=Pay_Fine_external_strategy)
@settings(max_examples=50)
def test_pay_fine_external_instantiation(instance):
    assert isinstance(instance, Pay_Fine_external)

@given(instance=Issue_Book_external_strategy)
@settings(max_examples=50)
def test_issue_book_external_instantiation(instance):
    assert isinstance(instance, Issue_Book_external)

@given(instance=Search_for_Books_external_strategy)
@settings(max_examples=50)
def test_search_for_books_external_instantiation(instance):
    assert isinstance(instance, Search_for_Books_external)

@given(instance=Organise_Book_details_external_strategy)
@settings(max_examples=50)
def test_organise_book_details_external_instantiation(instance):
    assert isinstance(instance, Organise_Book_details_external)

@given(instance=Librarian_Actor_strategy)
@settings(max_examples=50)
def test_librarian_actor_instantiation(instance):
    assert isinstance(instance, Librarian_Actor)

@given(instance=User_Database_Actor_strategy)
@settings(max_examples=50)
def test_user_database_actor_instantiation(instance):
    assert isinstance(instance, User_Database_Actor)

@given(instance=Books_Database_Actor_strategy)
@settings(max_examples=50)
def test_books_database_actor_instantiation(instance):
    assert isinstance(instance, Books_Database_Actor)

@given(instance=T_strategy)
@settings(max_examples=50)
def test_t_instantiation(instance):
    assert isinstance(instance, T)

@given(instance=Library_Management_System_Component_strategy)
@settings(max_examples=50)
def test_library_management_system_component_instantiation(instance):
    assert isinstance(instance, Library_Management_System_Component)

@given(instance=User_Actor_strategy)
@settings(max_examples=50)
def test_user_actor_instantiation(instance):
    assert isinstance(instance, User_Actor)
