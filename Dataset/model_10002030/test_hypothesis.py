import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    patronrecord,
    vendor,
    patron,
    book_mdatabase,
    LIBRARIAN,
    library,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_patronrecord_is_not_abstract():
    assert not inspect.isabstract(patronrecord)


def test_patronrecord_constructor_exists():
    assert callable(patronrecord.__init__)


def test_patronrecord_constructor_args():
    sig = inspect.signature(patronrecord.__init__)
    params = list(sig.parameters.keys())
    assert "phone_no" in params, "Missing parameter 'phone_no'"
    assert "name" in params, "Missing parameter 'name'"
    assert "address" in params, "Missing parameter 'address'"
    assert "filesowned" in params, "Missing parameter 'filesowned'"
    assert "patronid" in params, "Missing parameter 'patronid'"
    assert "dateofmembership" in params, "Missing parameter 'dateofmembership'"
    assert "type" in params, "Missing parameter 'type'"
    assert "noofbooks_alooted" in params, "Missing parameter 'noofbooks_alooted'"

def test_patronrecord_has_phone_no():
    assert hasattr(patronrecord, "phone_no")
    descriptor = None
    for klass in patronrecord.__mro__:
        if "phone_no" in klass.__dict__:
            descriptor = klass.__dict__["phone_no"]
            break
    assert isinstance(descriptor, property)

def test_patronrecord_has_name():
    assert hasattr(patronrecord, "name")
    descriptor = None
    for klass in patronrecord.__mro__:
        if "name" in klass.__dict__:
            descriptor = klass.__dict__["name"]
            break
    assert isinstance(descriptor, property)

def test_patronrecord_has_address():
    assert hasattr(patronrecord, "address")
    descriptor = None
    for klass in patronrecord.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_patronrecord_has_filesowned():
    assert hasattr(patronrecord, "filesowned")
    descriptor = None
    for klass in patronrecord.__mro__:
        if "filesowned" in klass.__dict__:
            descriptor = klass.__dict__["filesowned"]
            break
    assert isinstance(descriptor, property)

def test_patronrecord_has_patronid():
    assert hasattr(patronrecord, "patronid")
    descriptor = None
    for klass in patronrecord.__mro__:
        if "patronid" in klass.__dict__:
            descriptor = klass.__dict__["patronid"]
            break
    assert isinstance(descriptor, property)

def test_patronrecord_has_dateofmembership():
    assert hasattr(patronrecord, "dateofmembership")
    descriptor = None
    for klass in patronrecord.__mro__:
        if "dateofmembership" in klass.__dict__:
            descriptor = klass.__dict__["dateofmembership"]
            break
    assert isinstance(descriptor, property)

def test_patronrecord_has_type():
    assert hasattr(patronrecord, "type")
    descriptor = None
    for klass in patronrecord.__mro__:
        if "type" in klass.__dict__:
            descriptor = klass.__dict__["type"]
            break
    assert isinstance(descriptor, property)

def test_patronrecord_has_noofbooks_alooted():
    assert hasattr(patronrecord, "noofbooks_alooted")
    descriptor = None
    for klass in patronrecord.__mro__:
        if "noofbooks_alooted" in klass.__dict__:
            descriptor = klass.__dict__["noofbooks_alooted"]
            break
    assert isinstance(descriptor, property)



def test_vendor_is_not_abstract():
    assert not inspect.isabstract(vendor)


def test_vendor_constructor_exists():
    assert callable(vendor.__init__)


def test_vendor_constructor_args():
    sig = inspect.signature(vendor.__init__)
    params = list(sig.parameters.keys())
    assert "search" in params, "Missing parameter 'search'"
    assert "paymentdetails" in params, "Missing parameter 'paymentdetails'"
    assert "bookdetails" in params, "Missing parameter 'bookdetails'"
    assert "supplybooks" in params, "Missing parameter 'supplybooks'"

def test_vendor_has_search():
    assert hasattr(vendor, "search")
    descriptor = None
    for klass in vendor.__mro__:
        if "search" in klass.__dict__:
            descriptor = klass.__dict__["search"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_paymentdetails():
    assert hasattr(vendor, "paymentdetails")
    descriptor = None
    for klass in vendor.__mro__:
        if "paymentdetails" in klass.__dict__:
            descriptor = klass.__dict__["paymentdetails"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_bookdetails():
    assert hasattr(vendor, "bookdetails")
    descriptor = None
    for klass in vendor.__mro__:
        if "bookdetails" in klass.__dict__:
            descriptor = klass.__dict__["bookdetails"]
            break
    assert isinstance(descriptor, property)

def test_vendor_has_supplybooks():
    assert hasattr(vendor, "supplybooks")
    descriptor = None
    for klass in vendor.__mro__:
        if "supplybooks" in klass.__dict__:
            descriptor = klass.__dict__["supplybooks"]
            break
    assert isinstance(descriptor, property)



def test_patron_is_not_abstract():
    assert not inspect.isabstract(patron)


def test_patron_constructor_exists():
    assert callable(patron.__init__)


def test_patron_constructor_args():
    sig = inspect.signature(patron.__init__)
    params = list(sig.parameters.keys())
    assert "patronid" in params, "Missing parameter 'patronid'"
    assert "details" in params, "Missing parameter 'details'"
    assert "payfine" in params, "Missing parameter 'payfine'"
    assert "request" in params, "Missing parameter 'request'"
    assert "search" in params, "Missing parameter 'search'"

def test_patron_has_patronid():
    assert hasattr(patron, "patronid")
    descriptor = None
    for klass in patron.__mro__:
        if "patronid" in klass.__dict__:
            descriptor = klass.__dict__["patronid"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_details():
    assert hasattr(patron, "details")
    descriptor = None
    for klass in patron.__mro__:
        if "details" in klass.__dict__:
            descriptor = klass.__dict__["details"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_payfine():
    assert hasattr(patron, "payfine")
    descriptor = None
    for klass in patron.__mro__:
        if "payfine" in klass.__dict__:
            descriptor = klass.__dict__["payfine"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_request():
    assert hasattr(patron, "request")
    descriptor = None
    for klass in patron.__mro__:
        if "request" in klass.__dict__:
            descriptor = klass.__dict__["request"]
            break
    assert isinstance(descriptor, property)

def test_patron_has_search():
    assert hasattr(patron, "search")
    descriptor = None
    for klass in patron.__mro__:
        if "search" in klass.__dict__:
            descriptor = klass.__dict__["search"]
            break
    assert isinstance(descriptor, property)



def test_book_mdatabase_is_not_abstract():
    assert not inspect.isabstract(book_mdatabase)


def test_book_mdatabase_constructor_exists():
    assert callable(book_mdatabase.__init__)


def test_book_mdatabase_constructor_args():
    sig = inspect.signature(book_mdatabase.__init__)
    params = list(sig.parameters.keys())
    assert "author" in params, "Missing parameter 'author'"
    assert "bookid" in params, "Missing parameter 'bookid'"
    assert "update" in params, "Missing parameter 'update'"
    assert "booktitle" in params, "Missing parameter 'booktitle'"

def test_book_mdatabase_has_author():
    assert hasattr(book_mdatabase, "author")
    descriptor = None
    for klass in book_mdatabase.__mro__:
        if "author" in klass.__dict__:
            descriptor = klass.__dict__["author"]
            break
    assert isinstance(descriptor, property)

def test_book_mdatabase_has_bookid():
    assert hasattr(book_mdatabase, "bookid")
    descriptor = None
    for klass in book_mdatabase.__mro__:
        if "bookid" in klass.__dict__:
            descriptor = klass.__dict__["bookid"]
            break
    assert isinstance(descriptor, property)

def test_book_mdatabase_has_update():
    assert hasattr(book_mdatabase, "update")
    descriptor = None
    for klass in book_mdatabase.__mro__:
        if "update" in klass.__dict__:
            descriptor = klass.__dict__["update"]
            break
    assert isinstance(descriptor, property)

def test_book_mdatabase_has_booktitle():
    assert hasattr(book_mdatabase, "booktitle")
    descriptor = None
    for klass in book_mdatabase.__mro__:
        if "booktitle" in klass.__dict__:
            descriptor = klass.__dict__["booktitle"]
            break
    assert isinstance(descriptor, property)



def test_librarian_is_not_abstract():
    assert not inspect.isabstract(LIBRARIAN)


def test_librarian_constructor_exists():
    assert callable(LIBRARIAN.__init__)


def test_librarian_constructor_args():
    sig = inspect.signature(LIBRARIAN.__init__)
    params = list(sig.parameters.keys())
    assert "NAME" in params, "Missing parameter 'NAME'"
    assert "searchbook__" in params, "Missing parameter 'searchbook__'"
    assert "LIBRARIAN_ID" in params, "Missing parameter 'LIBRARIAN_ID'"
    assert "issue_status" in params, "Missing parameter 'issue_status'"
    assert "issue_book" in params, "Missing parameter 'issue_book'"
    assert "verify_member__" in params, "Missing parameter 'verify_member__'"

def test_librarian_has_NAME():
    assert hasattr(LIBRARIAN, "NAME")
    descriptor = None
    for klass in LIBRARIAN.__mro__:
        if "NAME" in klass.__dict__:
            descriptor = klass.__dict__["NAME"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_searchbook__():
    assert hasattr(LIBRARIAN, "searchbook__")
    descriptor = None
    for klass in LIBRARIAN.__mro__:
        if "searchbook__" in klass.__dict__:
            descriptor = klass.__dict__["searchbook__"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_LIBRARIAN_ID():
    assert hasattr(LIBRARIAN, "LIBRARIAN_ID")
    descriptor = None
    for klass in LIBRARIAN.__mro__:
        if "LIBRARIAN_ID" in klass.__dict__:
            descriptor = klass.__dict__["LIBRARIAN_ID"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_issue_status():
    assert hasattr(LIBRARIAN, "issue_status")
    descriptor = None
    for klass in LIBRARIAN.__mro__:
        if "issue_status" in klass.__dict__:
            descriptor = klass.__dict__["issue_status"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_issue_book():
    assert hasattr(LIBRARIAN, "issue_book")
    descriptor = None
    for klass in LIBRARIAN.__mro__:
        if "issue_book" in klass.__dict__:
            descriptor = klass.__dict__["issue_book"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_verify_member__():
    assert hasattr(LIBRARIAN, "verify_member__")
    descriptor = None
    for klass in LIBRARIAN.__mro__:
        if "verify_member__" in klass.__dict__:
            descriptor = klass.__dict__["verify_member__"]
            break
    assert isinstance(descriptor, property)



def test_library_is_not_abstract():
    assert not inspect.isabstract(library)


def test_library_constructor_exists():
    assert callable(library.__init__)


def test_library_constructor_args():
    sig = inspect.signature(library.__init__)
    params = list(sig.parameters.keys())
    assert "_librarion_id" in params, "Missing parameter '_librarion_id'"
    assert "_location" in params, "Missing parameter '_location'"

def test_library_has__librarion_id():
    assert hasattr(library, "_librarion_id")
    descriptor = None
    for klass in library.__mro__:
        if "_librarion_id" in klass.__dict__:
            descriptor = klass.__dict__["_librarion_id"]
            break
    assert isinstance(descriptor, property)

def test_library_has__location():
    assert hasattr(library, "_location")
    descriptor = None
    for klass in library.__mro__:
        if "_location" in klass.__dict__:
            descriptor = klass.__dict__["_location"]
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
patronrecord_strategy = st.builds(
    patronrecord,
    phone_no=
        safe_text,
    name=
        safe_text,
    address=
        safe_text,
    filesowned=
        safe_text,
    patronid=
        safe_text,
    dateofmembership=
        safe_text,
    type=
        safe_text,
    noofbooks_alooted=
        safe_text
)
vendor_strategy = st.builds(
    vendor,
    search=
        safe_text,
    paymentdetails=
        safe_text,
    bookdetails=
        safe_text,
    supplybooks=
        safe_text
)
patron_strategy = st.builds(
    patron,
    patronid=
        safe_text,
    details=
        safe_text,
    payfine=
        safe_text,
    request=
        safe_text,
    search=
        safe_text
)
book_mdatabase_strategy = st.builds(
    book_mdatabase,
    author=
        safe_text,
    bookid=
        safe_text,
    update=
        safe_text,
    booktitle=
        safe_text
)
LIBRARIAN_strategy = st.builds(
    LIBRARIAN,
    NAME=
        safe_text,
    searchbook__=
        safe_text,
    LIBRARIAN_ID=
        safe_text,
    issue_status=
        safe_text,
    issue_book=
        safe_text,
    verify_member__=
        safe_text
)
library_strategy = st.builds(
    library,
    _librarion_id=
        safe_text,
    _location=
        safe_text
)

@given(instance=patronrecord_strategy)
@settings(max_examples=50)
def test_patronrecord_instantiation(instance):
    assert isinstance(instance, patronrecord)



@given(instance=patronrecord_strategy)
def test_patronrecord_phone_no_setter(instance):
    original = instance.phone_no
    instance.phone_no = original
    assert instance.phone_no == original



@given(instance=patronrecord_strategy)
def test_patronrecord_name_setter(instance):
    original = instance.name
    instance.name = original
    assert instance.name == original



@given(instance=patronrecord_strategy)
def test_patronrecord_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=patronrecord_strategy)
def test_patronrecord_filesowned_setter(instance):
    original = instance.filesowned
    instance.filesowned = original
    assert instance.filesowned == original



@given(instance=patronrecord_strategy)
def test_patronrecord_patronid_setter(instance):
    original = instance.patronid
    instance.patronid = original
    assert instance.patronid == original



@given(instance=patronrecord_strategy)
def test_patronrecord_dateofmembership_setter(instance):
    original = instance.dateofmembership
    instance.dateofmembership = original
    assert instance.dateofmembership == original



@given(instance=patronrecord_strategy)
def test_patronrecord_type_setter(instance):
    original = instance.type
    instance.type = original
    assert instance.type == original



@given(instance=patronrecord_strategy)
def test_patronrecord_noofbooks_alooted_setter(instance):
    original = instance.noofbooks_alooted
    instance.noofbooks_alooted = original
    assert instance.noofbooks_alooted == original

@given(instance=vendor_strategy)
@settings(max_examples=50)
def test_vendor_instantiation(instance):
    assert isinstance(instance, vendor)



@given(instance=vendor_strategy)
def test_vendor_search_setter(instance):
    original = instance.search
    instance.search = original
    assert instance.search == original



@given(instance=vendor_strategy)
def test_vendor_paymentdetails_setter(instance):
    original = instance.paymentdetails
    instance.paymentdetails = original
    assert instance.paymentdetails == original



@given(instance=vendor_strategy)
def test_vendor_bookdetails_setter(instance):
    original = instance.bookdetails
    instance.bookdetails = original
    assert instance.bookdetails == original



@given(instance=vendor_strategy)
def test_vendor_supplybooks_setter(instance):
    original = instance.supplybooks
    instance.supplybooks = original
    assert instance.supplybooks == original

@given(instance=patron_strategy)
@settings(max_examples=50)
def test_patron_instantiation(instance):
    assert isinstance(instance, patron)



@given(instance=patron_strategy)
def test_patron_patronid_setter(instance):
    original = instance.patronid
    instance.patronid = original
    assert instance.patronid == original



@given(instance=patron_strategy)
def test_patron_details_setter(instance):
    original = instance.details
    instance.details = original
    assert instance.details == original



@given(instance=patron_strategy)
def test_patron_payfine_setter(instance):
    original = instance.payfine
    instance.payfine = original
    assert instance.payfine == original



@given(instance=patron_strategy)
def test_patron_request_setter(instance):
    original = instance.request
    instance.request = original
    assert instance.request == original



@given(instance=patron_strategy)
def test_patron_search_setter(instance):
    original = instance.search
    instance.search = original
    assert instance.search == original

@given(instance=book_mdatabase_strategy)
@settings(max_examples=50)
def test_book_mdatabase_instantiation(instance):
    assert isinstance(instance, book_mdatabase)



@given(instance=book_mdatabase_strategy)
def test_book_mdatabase_author_setter(instance):
    original = instance.author
    instance.author = original
    assert instance.author == original



@given(instance=book_mdatabase_strategy)
def test_book_mdatabase_bookid_setter(instance):
    original = instance.bookid
    instance.bookid = original
    assert instance.bookid == original



@given(instance=book_mdatabase_strategy)
def test_book_mdatabase_update_setter(instance):
    original = instance.update
    instance.update = original
    assert instance.update == original



@given(instance=book_mdatabase_strategy)
def test_book_mdatabase_booktitle_setter(instance):
    original = instance.booktitle
    instance.booktitle = original
    assert instance.booktitle == original

@given(instance=LIBRARIAN_strategy)
@settings(max_examples=50)
def test_librarian_instantiation(instance):
    assert isinstance(instance, LIBRARIAN)



@given(instance=LIBRARIAN_strategy)
def test_librarian_NAME_setter(instance):
    original = instance.NAME
    instance.NAME = original
    assert instance.NAME == original



@given(instance=LIBRARIAN_strategy)
def test_librarian_searchbook___setter(instance):
    original = instance.searchbook__
    instance.searchbook__ = original
    assert instance.searchbook__ == original



@given(instance=LIBRARIAN_strategy)
def test_librarian_LIBRARIAN_ID_setter(instance):
    original = instance.LIBRARIAN_ID
    instance.LIBRARIAN_ID = original
    assert instance.LIBRARIAN_ID == original



@given(instance=LIBRARIAN_strategy)
def test_librarian_issue_status_setter(instance):
    original = instance.issue_status
    instance.issue_status = original
    assert instance.issue_status == original



@given(instance=LIBRARIAN_strategy)
def test_librarian_issue_book_setter(instance):
    original = instance.issue_book
    instance.issue_book = original
    assert instance.issue_book == original



@given(instance=LIBRARIAN_strategy)
def test_librarian_verify_member___setter(instance):
    original = instance.verify_member__
    instance.verify_member__ = original
    assert instance.verify_member__ == original

@given(instance=library_strategy)
@settings(max_examples=50)
def test_library_instantiation(instance):
    assert isinstance(instance, library)



@given(instance=library_strategy)
def test_library__librarion_id_setter(instance):
    original = instance._librarion_id
    instance._librarion_id = original
    assert instance._librarion_id == original



@given(instance=library_strategy)
def test_library__location_setter(instance):
    original = instance._location
    instance._location = original
    assert instance._location == original
