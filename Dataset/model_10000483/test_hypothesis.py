import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Update_member_profile_external,
    Return_book_external,
    Issue_book_external,
    Issue_member_card_external,
    Person,
    Customer,
    Search_books_UseCase,
    Librarian_Actor,
    Member_Actor,
    Library_Management_Component,
    Request_book_return_external,
    Request_book_external,
    Inquiry_for_membership_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_update_member_profile_external_is_not_abstract():
    assert not inspect.isabstract(Update_member_profile_external)


def test_update_member_profile_external_constructor_exists():
    assert callable(Update_member_profile_external.__init__)


def test_update_member_profile_external_constructor_args():
    sig = inspect.signature(Update_member_profile_external.__init__)
    params = list(sig.parameters.keys())



def test_return_book_external_is_not_abstract():
    assert not inspect.isabstract(Return_book_external)


def test_return_book_external_constructor_exists():
    assert callable(Return_book_external.__init__)


def test_return_book_external_constructor_args():
    sig = inspect.signature(Return_book_external.__init__)
    params = list(sig.parameters.keys())



def test_issue_book_external_is_not_abstract():
    assert not inspect.isabstract(Issue_book_external)


def test_issue_book_external_constructor_exists():
    assert callable(Issue_book_external.__init__)


def test_issue_book_external_constructor_args():
    sig = inspect.signature(Issue_book_external.__init__)
    params = list(sig.parameters.keys())



def test_issue_member_card_external_is_not_abstract():
    assert not inspect.isabstract(Issue_member_card_external)


def test_issue_member_card_external_constructor_exists():
    assert callable(Issue_member_card_external.__init__)


def test_issue_member_card_external_constructor_args():
    sig = inspect.signature(Issue_member_card_external.__init__)
    params = list(sig.parameters.keys())



def test_person_is_not_abstract():
    assert not inspect.isabstract(Person)


def test_person_constructor_exists():
    assert callable(Person.__init__)


def test_person_constructor_args():
    sig = inspect.signature(Person.__init__)
    params = list(sig.parameters.keys())
    assert "address" in params, "Missing parameter 'address'"
    assert "phone" in params, "Missing parameter 'phone'"

def test_person_has_address():
    assert hasattr(Person, "address")
    descriptor = None
    for klass in Person.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_person_has_phone():
    assert hasattr(Person, "phone")
    descriptor = None
    for klass in Person.__mro__:
        if "phone" in klass.__dict__:
            descriptor = klass.__dict__["phone"]
            break
    assert isinstance(descriptor, property)



def test_customer_is_not_abstract():
    assert not inspect.isabstract(Customer)


def test_customer_constructor_exists():
    assert callable(Customer.__init__)


def test_customer_constructor_args():
    sig = inspect.signature(Customer.__init__)
    params = list(sig.parameters.keys())
    assert "recruitmentDate" in params, "Missing parameter 'recruitmentDate'"

def test_customer_has_recruitmentDate():
    assert hasattr(Customer, "recruitmentDate")
    descriptor = None
    for klass in Customer.__mro__:
        if "recruitmentDate" in klass.__dict__:
            descriptor = klass.__dict__["recruitmentDate"]
            break
    assert isinstance(descriptor, property)



def test_search_books_usecase_is_not_abstract():
    assert not inspect.isabstract(Search_books_UseCase)


def test_search_books_usecase_constructor_exists():
    assert callable(Search_books_UseCase.__init__)


def test_search_books_usecase_constructor_args():
    sig = inspect.signature(Search_books_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_librarian_actor_is_not_abstract():
    assert not inspect.isabstract(Librarian_Actor)


def test_librarian_actor_constructor_exists():
    assert callable(Librarian_Actor.__init__)


def test_librarian_actor_constructor_args():
    sig = inspect.signature(Librarian_Actor.__init__)
    params = list(sig.parameters.keys())



def test_member_actor_is_not_abstract():
    assert not inspect.isabstract(Member_Actor)


def test_member_actor_constructor_exists():
    assert callable(Member_Actor.__init__)


def test_member_actor_constructor_args():
    sig = inspect.signature(Member_Actor.__init__)
    params = list(sig.parameters.keys())



def test_library_management_component_is_not_abstract():
    assert not inspect.isabstract(Library_Management_Component)


def test_library_management_component_constructor_exists():
    assert callable(Library_Management_Component.__init__)


def test_library_management_component_constructor_args():
    sig = inspect.signature(Library_Management_Component.__init__)
    params = list(sig.parameters.keys())



def test_request_book_return_external_is_not_abstract():
    assert not inspect.isabstract(Request_book_return_external)


def test_request_book_return_external_constructor_exists():
    assert callable(Request_book_return_external.__init__)


def test_request_book_return_external_constructor_args():
    sig = inspect.signature(Request_book_return_external.__init__)
    params = list(sig.parameters.keys())



def test_request_book_external_is_not_abstract():
    assert not inspect.isabstract(Request_book_external)


def test_request_book_external_constructor_exists():
    assert callable(Request_book_external.__init__)


def test_request_book_external_constructor_args():
    sig = inspect.signature(Request_book_external.__init__)
    params = list(sig.parameters.keys())



def test_inquiry_for_membership_external_is_not_abstract():
    assert not inspect.isabstract(Inquiry_for_membership_external)


def test_inquiry_for_membership_external_constructor_exists():
    assert callable(Inquiry_for_membership_external.__init__)


def test_inquiry_for_membership_external_constructor_args():
    sig = inspect.signature(Inquiry_for_membership_external.__init__)
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
Update_member_profile_external_strategy = st.builds(
    Update_member_profile_external,
)
Return_book_external_strategy = st.builds(
    Return_book_external,
)
Issue_book_external_strategy = st.builds(
    Issue_book_external,
)
Issue_member_card_external_strategy = st.builds(
    Issue_member_card_external,
)
Person_strategy = st.builds(
    Person,
    address=
        safe_text,
    phone=
        safe_text
)
Customer_strategy = st.builds(
    Customer,
    recruitmentDate=
        st.dates()
)
Search_books_UseCase_strategy = st.builds(
    Search_books_UseCase,
)
Librarian_Actor_strategy = st.builds(
    Librarian_Actor,
)
Member_Actor_strategy = st.builds(
    Member_Actor,
)
Library_Management_Component_strategy = st.builds(
    Library_Management_Component,
)
Request_book_return_external_strategy = st.builds(
    Request_book_return_external,
)
Request_book_external_strategy = st.builds(
    Request_book_external,
)
Inquiry_for_membership_external_strategy = st.builds(
    Inquiry_for_membership_external,
)

@given(instance=Update_member_profile_external_strategy)
@settings(max_examples=50)
def test_update_member_profile_external_instantiation(instance):
    assert isinstance(instance, Update_member_profile_external)

@given(instance=Return_book_external_strategy)
@settings(max_examples=50)
def test_return_book_external_instantiation(instance):
    assert isinstance(instance, Return_book_external)

@given(instance=Issue_book_external_strategy)
@settings(max_examples=50)
def test_issue_book_external_instantiation(instance):
    assert isinstance(instance, Issue_book_external)

@given(instance=Issue_member_card_external_strategy)
@settings(max_examples=50)
def test_issue_member_card_external_instantiation(instance):
    assert isinstance(instance, Issue_member_card_external)

@given(instance=Person_strategy)
@settings(max_examples=50)
def test_person_instantiation(instance):
    assert isinstance(instance, Person)



@given(instance=Person_strategy)
def test_person_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Person_strategy)
def test_person_phone_setter(instance):
    original = instance.phone
    instance.phone = original
    assert instance.phone == original

@given(instance=Customer_strategy)
@settings(max_examples=50)
def test_customer_instantiation(instance):
    assert isinstance(instance, Customer)



@given(instance=Customer_strategy)
def test_customer_recruitmentDate_setter(instance):
    original = instance.recruitmentDate
    instance.recruitmentDate = original
    assert instance.recruitmentDate == original

@given(instance=Search_books_UseCase_strategy)
@settings(max_examples=50)
def test_search_books_usecase_instantiation(instance):
    assert isinstance(instance, Search_books_UseCase)

@given(instance=Librarian_Actor_strategy)
@settings(max_examples=50)
def test_librarian_actor_instantiation(instance):
    assert isinstance(instance, Librarian_Actor)

@given(instance=Member_Actor_strategy)
@settings(max_examples=50)
def test_member_actor_instantiation(instance):
    assert isinstance(instance, Member_Actor)

@given(instance=Library_Management_Component_strategy)
@settings(max_examples=50)
def test_library_management_component_instantiation(instance):
    assert isinstance(instance, Library_Management_Component)

@given(instance=Request_book_return_external_strategy)
@settings(max_examples=50)
def test_request_book_return_external_instantiation(instance):
    assert isinstance(instance, Request_book_return_external)

@given(instance=Request_book_external_strategy)
@settings(max_examples=50)
def test_request_book_external_instantiation(instance):
    assert isinstance(instance, Request_book_external)

@given(instance=Inquiry_for_membership_external_strategy)
@settings(max_examples=50)
def test_inquiry_for_membership_external_instantiation(instance):
    assert isinstance(instance, Inquiry_for_membership_external)
