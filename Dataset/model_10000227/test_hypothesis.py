import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Request_book_return_external,
    Request_book_external,
    Inquiry_for_membership_external,
    UserProperties,
    Librarian_Actor,
    Member_Actor,
    Library_Management_Component,
    Cancel_membership_external,
    Maintain_book_in_records_external,
    Update_member_profile_external,
    Return_book_external,
    Issue_book_external,
    Issue_member_card_external,
    Search_books_external,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



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



def test_userproperties_is_not_abstract():
    assert not inspect.isabstract(UserProperties)


def test_userproperties_constructor_exists():
    assert callable(UserProperties.__init__)


def test_userproperties_constructor_args():
    sig = inspect.signature(UserProperties.__init__)
    params = list(sig.parameters.keys())
    assert "roles" in params, "Missing parameter 'roles'"
    assert "Roles" in params, "Missing parameter 'Roles'"

def test_userproperties_has_roles():
    assert hasattr(UserProperties, "roles")
    descriptor = None
    for klass in UserProperties.__mro__:
        if "roles" in klass.__dict__:
            descriptor = klass.__dict__["roles"]
            break
    assert isinstance(descriptor, property)

def test_userproperties_has_Roles():
    assert hasattr(UserProperties, "Roles")
    descriptor = None
    for klass in UserProperties.__mro__:
        if "Roles" in klass.__dict__:
            descriptor = klass.__dict__["Roles"]
            break
    assert isinstance(descriptor, property)



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



def test_cancel_membership_external_is_not_abstract():
    assert not inspect.isabstract(Cancel_membership_external)


def test_cancel_membership_external_constructor_exists():
    assert callable(Cancel_membership_external.__init__)


def test_cancel_membership_external_constructor_args():
    sig = inspect.signature(Cancel_membership_external.__init__)
    params = list(sig.parameters.keys())



def test_maintain_book_in_records_external_is_not_abstract():
    assert not inspect.isabstract(Maintain_book_in_records_external)


def test_maintain_book_in_records_external_constructor_exists():
    assert callable(Maintain_book_in_records_external.__init__)


def test_maintain_book_in_records_external_constructor_args():
    sig = inspect.signature(Maintain_book_in_records_external.__init__)
    params = list(sig.parameters.keys())



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



def test_search_books_external_is_not_abstract():
    assert not inspect.isabstract(Search_books_external)


def test_search_books_external_constructor_exists():
    assert callable(Search_books_external.__init__)


def test_search_books_external_constructor_args():
    sig = inspect.signature(Search_books_external.__init__)
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
Request_book_return_external_strategy = st.builds(
    Request_book_return_external,
)
Request_book_external_strategy = st.builds(
    Request_book_external,
)
Inquiry_for_membership_external_strategy = st.builds(
    Inquiry_for_membership_external,
)
UserProperties_strategy = st.builds(
    UserProperties,
    roles=
        safe_text,
    Roles=
        safe_text
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
Cancel_membership_external_strategy = st.builds(
    Cancel_membership_external,
)
Maintain_book_in_records_external_strategy = st.builds(
    Maintain_book_in_records_external,
)
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
Search_books_external_strategy = st.builds(
    Search_books_external,
)

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

@given(instance=UserProperties_strategy)
@settings(max_examples=50)
def test_userproperties_instantiation(instance):
    assert isinstance(instance, UserProperties)



@given(instance=UserProperties_strategy)
def test_userproperties_roles_setter(instance):
    original = instance.roles
    instance.roles = original
    assert instance.roles == original



@given(instance=UserProperties_strategy)
def test_userproperties_Roles_setter(instance):
    original = instance.Roles
    instance.Roles = original
    assert instance.Roles == original

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

@given(instance=Cancel_membership_external_strategy)
@settings(max_examples=50)
def test_cancel_membership_external_instantiation(instance):
    assert isinstance(instance, Cancel_membership_external)

@given(instance=Maintain_book_in_records_external_strategy)
@settings(max_examples=50)
def test_maintain_book_in_records_external_instantiation(instance):
    assert isinstance(instance, Maintain_book_in_records_external)

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

@given(instance=Search_books_external_strategy)
@settings(max_examples=50)
def test_search_books_external_instantiation(instance):
    assert isinstance(instance, Search_books_external)
