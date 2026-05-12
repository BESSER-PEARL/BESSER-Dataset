import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Class,
    lecturer,
    admin,
    Staff,
    Reserved,
    Borrowed,
    Fine,
    Librarian,
    Member,
    Books,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_class_is_not_abstract():
    assert not inspect.isabstract(Class)


def test_class_constructor_exists():
    assert callable(Class.__init__)


def test_class_constructor_args():
    sig = inspect.signature(Class.__init__)
    params = list(sig.parameters.keys())



def test_lecturer_is_not_abstract():
    assert not inspect.isabstract(lecturer)


def test_lecturer_constructor_exists():
    assert callable(lecturer.__init__)


def test_lecturer_constructor_args():
    sig = inspect.signature(lecturer.__init__)
    params = list(sig.parameters.keys())
    assert "module" in params, "Missing parameter 'module'"

def test_lecturer_has_module():
    assert hasattr(lecturer, "module")
    descriptor = None
    for klass in lecturer.__mro__:
        if "module" in klass.__dict__:
            descriptor = klass.__dict__["module"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(admin)


def test_admin_constructor_exists():
    assert callable(admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(admin.__init__)
    params = list(sig.parameters.keys())
    assert "Experience" in params, "Missing parameter 'Experience'"

def test_admin_has_Experience():
    assert hasattr(admin, "Experience")
    descriptor = None
    for klass in admin.__mro__:
        if "Experience" in klass.__dict__:
            descriptor = klass.__dict__["Experience"]
            break
    assert isinstance(descriptor, property)



def test_staff_is_not_abstract():
    assert not inspect.isabstract(Staff)


def test_staff_constructor_exists():
    assert callable(Staff.__init__)


def test_staff_constructor_args():
    sig = inspect.signature(Staff.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "address" in params, "Missing parameter 'address'"
    assert "contact" in params, "Missing parameter 'contact'"
    assert "position" in params, "Missing parameter 'position'"
    assert "email" in params, "Missing parameter 'email'"
    assert "Staff_ID" in params, "Missing parameter 'Staff_ID'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "username" in params, "Missing parameter 'username'"

def test_staff_has_lname():
    assert hasattr(Staff, "lname")
    descriptor = None
    for klass in Staff.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_password():
    assert hasattr(Staff, "password")
    descriptor = None
    for klass in Staff.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_fname():
    assert hasattr(Staff, "fname")
    descriptor = None
    for klass in Staff.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_address():
    assert hasattr(Staff, "address")
    descriptor = None
    for klass in Staff.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_contact():
    assert hasattr(Staff, "contact")
    descriptor = None
    for klass in Staff.__mro__:
        if "contact" in klass.__dict__:
            descriptor = klass.__dict__["contact"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_position():
    assert hasattr(Staff, "position")
    descriptor = None
    for klass in Staff.__mro__:
        if "position" in klass.__dict__:
            descriptor = klass.__dict__["position"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_email():
    assert hasattr(Staff, "email")
    descriptor = None
    for klass in Staff.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_Staff_ID():
    assert hasattr(Staff, "Staff_ID")
    descriptor = None
    for klass in Staff.__mro__:
        if "Staff_ID" in klass.__dict__:
            descriptor = klass.__dict__["Staff_ID"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_gender():
    assert hasattr(Staff, "gender")
    descriptor = None
    for klass in Staff.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_staff_has_username():
    assert hasattr(Staff, "username")
    descriptor = None
    for klass in Staff.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_reserved_is_not_abstract():
    assert not inspect.isabstract(Reserved)


def test_reserved_constructor_exists():
    assert callable(Reserved.__init__)


def test_reserved_constructor_args():
    sig = inspect.signature(Reserved.__init__)
    params = list(sig.parameters.keys())
    assert "reserved_date" in params, "Missing parameter 'reserved_date'"

def test_reserved_has_reserved_date():
    assert hasattr(Reserved, "reserved_date")
    descriptor = None
    for klass in Reserved.__mro__:
        if "reserved_date" in klass.__dict__:
            descriptor = klass.__dict__["reserved_date"]
            break
    assert isinstance(descriptor, property)



def test_borrowed_is_not_abstract():
    assert not inspect.isabstract(Borrowed)


def test_borrowed_constructor_exists():
    assert callable(Borrowed.__init__)


def test_borrowed_constructor_args():
    sig = inspect.signature(Borrowed.__init__)
    params = list(sig.parameters.keys())
    assert "returned_date" in params, "Missing parameter 'returned_date'"
    assert "borrowed_date" in params, "Missing parameter 'borrowed_date'"

def test_borrowed_has_returned_date():
    assert hasattr(Borrowed, "returned_date")
    descriptor = None
    for klass in Borrowed.__mro__:
        if "returned_date" in klass.__dict__:
            descriptor = klass.__dict__["returned_date"]
            break
    assert isinstance(descriptor, property)

def test_borrowed_has_borrowed_date():
    assert hasattr(Borrowed, "borrowed_date")
    descriptor = None
    for klass in Borrowed.__mro__:
        if "borrowed_date" in klass.__dict__:
            descriptor = klass.__dict__["borrowed_date"]
            break
    assert isinstance(descriptor, property)



def test_fine_is_not_abstract():
    assert not inspect.isabstract(Fine)


def test_fine_constructor_exists():
    assert callable(Fine.__init__)


def test_fine_constructor_args():
    sig = inspect.signature(Fine.__init__)
    params = list(sig.parameters.keys())
    assert "member_id" in params, "Missing parameter 'member_id'"
    assert "returned_date" in params, "Missing parameter 'returned_date'"
    assert "fine_amount" in params, "Missing parameter 'fine_amount'"
    assert "borrowed_date" in params, "Missing parameter 'borrowed_date'"
    assert "book_id" in params, "Missing parameter 'book_id'"

def test_fine_has_member_id():
    assert hasattr(Fine, "member_id")
    descriptor = None
    for klass in Fine.__mro__:
        if "member_id" in klass.__dict__:
            descriptor = klass.__dict__["member_id"]
            break
    assert isinstance(descriptor, property)

def test_fine_has_returned_date():
    assert hasattr(Fine, "returned_date")
    descriptor = None
    for klass in Fine.__mro__:
        if "returned_date" in klass.__dict__:
            descriptor = klass.__dict__["returned_date"]
            break
    assert isinstance(descriptor, property)

def test_fine_has_fine_amount():
    assert hasattr(Fine, "fine_amount")
    descriptor = None
    for klass in Fine.__mro__:
        if "fine_amount" in klass.__dict__:
            descriptor = klass.__dict__["fine_amount"]
            break
    assert isinstance(descriptor, property)

def test_fine_has_borrowed_date():
    assert hasattr(Fine, "borrowed_date")
    descriptor = None
    for klass in Fine.__mro__:
        if "borrowed_date" in klass.__dict__:
            descriptor = klass.__dict__["borrowed_date"]
            break
    assert isinstance(descriptor, property)

def test_fine_has_book_id():
    assert hasattr(Fine, "book_id")
    descriptor = None
    for klass in Fine.__mro__:
        if "book_id" in klass.__dict__:
            descriptor = klass.__dict__["book_id"]
            break
    assert isinstance(descriptor, property)



def test_librarian_is_not_abstract():
    assert not inspect.isabstract(Librarian)


def test_librarian_constructor_exists():
    assert callable(Librarian.__init__)


def test_librarian_constructor_args():
    sig = inspect.signature(Librarian.__init__)
    params = list(sig.parameters.keys())
    assert "member_pwd" in params, "Missing parameter 'member_pwd'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "member_id" in params, "Missing parameter 'member_id'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "cont_no" in params, "Missing parameter 'cont_no'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "address" in params, "Missing parameter 'address'"
    assert "dob" in params, "Missing parameter 'dob'"

def test_librarian_has_member_pwd():
    assert hasattr(Librarian, "member_pwd")
    descriptor = None
    for klass in Librarian.__mro__:
        if "member_pwd" in klass.__dict__:
            descriptor = klass.__dict__["member_pwd"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_gender():
    assert hasattr(Librarian, "gender")
    descriptor = None
    for klass in Librarian.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_member_id():
    assert hasattr(Librarian, "member_id")
    descriptor = None
    for klass in Librarian.__mro__:
        if "member_id" in klass.__dict__:
            descriptor = klass.__dict__["member_id"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_fname():
    assert hasattr(Librarian, "fname")
    descriptor = None
    for klass in Librarian.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_cont_no():
    assert hasattr(Librarian, "cont_no")
    descriptor = None
    for klass in Librarian.__mro__:
        if "cont_no" in klass.__dict__:
            descriptor = klass.__dict__["cont_no"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_lname():
    assert hasattr(Librarian, "lname")
    descriptor = None
    for klass in Librarian.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_address():
    assert hasattr(Librarian, "address")
    descriptor = None
    for klass in Librarian.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_librarian_has_dob():
    assert hasattr(Librarian, "dob")
    descriptor = None
    for klass in Librarian.__mro__:
        if "dob" in klass.__dict__:
            descriptor = klass.__dict__["dob"]
            break
    assert isinstance(descriptor, property)



def test_member_is_not_abstract():
    assert not inspect.isabstract(Member)


def test_member_constructor_exists():
    assert callable(Member.__init__)


def test_member_constructor_args():
    sig = inspect.signature(Member.__init__)
    params = list(sig.parameters.keys())
    assert "cont_no" in params, "Missing parameter 'cont_no'"
    assert "member_id" in params, "Missing parameter 'member_id'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "address" in params, "Missing parameter 'address'"
    assert "dob" in params, "Missing parameter 'dob'"
    assert "member_pwd" in params, "Missing parameter 'member_pwd'"

def test_member_has_cont_no():
    assert hasattr(Member, "cont_no")
    descriptor = None
    for klass in Member.__mro__:
        if "cont_no" in klass.__dict__:
            descriptor = klass.__dict__["cont_no"]
            break
    assert isinstance(descriptor, property)

def test_member_has_member_id():
    assert hasattr(Member, "member_id")
    descriptor = None
    for klass in Member.__mro__:
        if "member_id" in klass.__dict__:
            descriptor = klass.__dict__["member_id"]
            break
    assert isinstance(descriptor, property)

def test_member_has_gender():
    assert hasattr(Member, "gender")
    descriptor = None
    for klass in Member.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_member_has_fname():
    assert hasattr(Member, "fname")
    descriptor = None
    for klass in Member.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_member_has_lname():
    assert hasattr(Member, "lname")
    descriptor = None
    for klass in Member.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)

def test_member_has_address():
    assert hasattr(Member, "address")
    descriptor = None
    for klass in Member.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_member_has_dob():
    assert hasattr(Member, "dob")
    descriptor = None
    for klass in Member.__mro__:
        if "dob" in klass.__dict__:
            descriptor = klass.__dict__["dob"]
            break
    assert isinstance(descriptor, property)

def test_member_has_member_pwd():
    assert hasattr(Member, "member_pwd")
    descriptor = None
    for klass in Member.__mro__:
        if "member_pwd" in klass.__dict__:
            descriptor = klass.__dict__["member_pwd"]
            break
    assert isinstance(descriptor, property)



def test_books_is_not_abstract():
    assert not inspect.isabstract(Books)


def test_books_constructor_exists():
    assert callable(Books.__init__)


def test_books_constructor_args():
    sig = inspect.signature(Books.__init__)
    params = list(sig.parameters.keys())
    assert "author_name" in params, "Missing parameter 'author_name'"
    assert "title" in params, "Missing parameter 'title'"
    assert "ISBN_no" in params, "Missing parameter 'ISBN_no'"
    assert "book_id" in params, "Missing parameter 'book_id'"
    assert "book_qty" in params, "Missing parameter 'book_qty'"
    assert "publisher" in params, "Missing parameter 'publisher'"

def test_books_has_author_name():
    assert hasattr(Books, "author_name")
    descriptor = None
    for klass in Books.__mro__:
        if "author_name" in klass.__dict__:
            descriptor = klass.__dict__["author_name"]
            break
    assert isinstance(descriptor, property)

def test_books_has_title():
    assert hasattr(Books, "title")
    descriptor = None
    for klass in Books.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_books_has_ISBN_no():
    assert hasattr(Books, "ISBN_no")
    descriptor = None
    for klass in Books.__mro__:
        if "ISBN_no" in klass.__dict__:
            descriptor = klass.__dict__["ISBN_no"]
            break
    assert isinstance(descriptor, property)

def test_books_has_book_id():
    assert hasattr(Books, "book_id")
    descriptor = None
    for klass in Books.__mro__:
        if "book_id" in klass.__dict__:
            descriptor = klass.__dict__["book_id"]
            break
    assert isinstance(descriptor, property)

def test_books_has_book_qty():
    assert hasattr(Books, "book_qty")
    descriptor = None
    for klass in Books.__mro__:
        if "book_qty" in klass.__dict__:
            descriptor = klass.__dict__["book_qty"]
            break
    assert isinstance(descriptor, property)

def test_books_has_publisher():
    assert hasattr(Books, "publisher")
    descriptor = None
    for klass in Books.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
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
Class_strategy = st.builds(
    Class,
)
lecturer_strategy = st.builds(
    lecturer,
    module=
        safe_text
)
admin_strategy = st.builds(
    admin,
    Experience=
        safe_text
)
Staff_strategy = st.builds(
    Staff,
    lname=
        safe_text,
    password=
        safe_text,
    fname=
        safe_text,
    address=
        safe_text,
    contact=
        st.integers(),
    position=
        safe_text,
    email=
        safe_text,
    Staff_ID=
        st.integers(),
    gender=
        safe_text,
    username=
        safe_text
)
Reserved_strategy = st.builds(
    Reserved,
    reserved_date=
        safe_text
)
Borrowed_strategy = st.builds(
    Borrowed,
    returned_date=
        safe_text,
    borrowed_date=
        safe_text
)
Fine_strategy = st.builds(
    Fine,
    member_id=
        st.integers(),
    returned_date=
        safe_text,
    fine_amount=
        st.integers(),
    borrowed_date=
        safe_text,
    book_id=
        st.integers()
)
Librarian_strategy = st.builds(
    Librarian,
    member_pwd=
        safe_text,
    gender=
        safe_text,
    member_id=
        st.integers(),
    fname=
        safe_text,
    cont_no=
        st.integers(),
    lname=
        safe_text,
    address=
        safe_text,
    dob=
        safe_text
)
Member_strategy = st.builds(
    Member,
    cont_no=
        st.integers(),
    member_id=
        st.integers(),
    gender=
        safe_text,
    fname=
        safe_text,
    lname=
        safe_text,
    address=
        safe_text,
    dob=
        safe_text,
    member_pwd=
        safe_text
)
Books_strategy = st.builds(
    Books,
    author_name=
        safe_text,
    title=
        safe_text,
    ISBN_no=
        safe_text,
    book_id=
        st.integers(),
    book_qty=
        st.integers(),
    publisher=
        safe_text
)

@given(instance=Class_strategy)
@settings(max_examples=50)
def test_class_instantiation(instance):
    assert isinstance(instance, Class)

@given(instance=lecturer_strategy)
@settings(max_examples=50)
def test_lecturer_instantiation(instance):
    assert isinstance(instance, lecturer)



@given(instance=lecturer_strategy)
def test_lecturer_module_setter(instance):
    original = instance.module
    instance.module = original
    assert instance.module == original

@given(instance=admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, admin)



@given(instance=admin_strategy)
def test_admin_Experience_setter(instance):
    original = instance.Experience
    instance.Experience = original
    assert instance.Experience == original

@given(instance=Staff_strategy)
@settings(max_examples=50)
def test_staff_instantiation(instance):
    assert isinstance(instance, Staff)



@given(instance=Staff_strategy)
def test_staff_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Staff_strategy)
def test_staff_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Staff_strategy)
def test_staff_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Staff_strategy)
def test_staff_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Staff_strategy)
def test_staff_contact_setter(instance):
    original = instance.contact
    instance.contact = original
    assert instance.contact == original



@given(instance=Staff_strategy)
def test_staff_position_setter(instance):
    original = instance.position
    instance.position = original
    assert instance.position == original



@given(instance=Staff_strategy)
def test_staff_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Staff_strategy)
def test_staff_Staff_ID_setter(instance):
    original = instance.Staff_ID
    instance.Staff_ID = original
    assert instance.Staff_ID == original



@given(instance=Staff_strategy)
def test_staff_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Staff_strategy)
def test_staff_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Reserved_strategy)
@settings(max_examples=50)
def test_reserved_instantiation(instance):
    assert isinstance(instance, Reserved)



@given(instance=Reserved_strategy)
def test_reserved_reserved_date_setter(instance):
    original = instance.reserved_date
    instance.reserved_date = original
    assert instance.reserved_date == original

@given(instance=Borrowed_strategy)
@settings(max_examples=50)
def test_borrowed_instantiation(instance):
    assert isinstance(instance, Borrowed)



@given(instance=Borrowed_strategy)
def test_borrowed_returned_date_setter(instance):
    original = instance.returned_date
    instance.returned_date = original
    assert instance.returned_date == original



@given(instance=Borrowed_strategy)
def test_borrowed_borrowed_date_setter(instance):
    original = instance.borrowed_date
    instance.borrowed_date = original
    assert instance.borrowed_date == original

@given(instance=Fine_strategy)
@settings(max_examples=50)
def test_fine_instantiation(instance):
    assert isinstance(instance, Fine)



@given(instance=Fine_strategy)
def test_fine_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original



@given(instance=Fine_strategy)
def test_fine_returned_date_setter(instance):
    original = instance.returned_date
    instance.returned_date = original
    assert instance.returned_date == original



@given(instance=Fine_strategy)
def test_fine_fine_amount_setter(instance):
    original = instance.fine_amount
    instance.fine_amount = original
    assert instance.fine_amount == original



@given(instance=Fine_strategy)
def test_fine_borrowed_date_setter(instance):
    original = instance.borrowed_date
    instance.borrowed_date = original
    assert instance.borrowed_date == original



@given(instance=Fine_strategy)
def test_fine_book_id_setter(instance):
    original = instance.book_id
    instance.book_id = original
    assert instance.book_id == original

@given(instance=Librarian_strategy)
@settings(max_examples=50)
def test_librarian_instantiation(instance):
    assert isinstance(instance, Librarian)



@given(instance=Librarian_strategy)
def test_librarian_member_pwd_setter(instance):
    original = instance.member_pwd
    instance.member_pwd = original
    assert instance.member_pwd == original



@given(instance=Librarian_strategy)
def test_librarian_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Librarian_strategy)
def test_librarian_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original



@given(instance=Librarian_strategy)
def test_librarian_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Librarian_strategy)
def test_librarian_cont_no_setter(instance):
    original = instance.cont_no
    instance.cont_no = original
    assert instance.cont_no == original



@given(instance=Librarian_strategy)
def test_librarian_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Librarian_strategy)
def test_librarian_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Librarian_strategy)
def test_librarian_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original

@given(instance=Member_strategy)
@settings(max_examples=50)
def test_member_instantiation(instance):
    assert isinstance(instance, Member)



@given(instance=Member_strategy)
def test_member_cont_no_setter(instance):
    original = instance.cont_no
    instance.cont_no = original
    assert instance.cont_no == original



@given(instance=Member_strategy)
def test_member_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original



@given(instance=Member_strategy)
def test_member_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Member_strategy)
def test_member_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Member_strategy)
def test_member_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Member_strategy)
def test_member_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Member_strategy)
def test_member_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original



@given(instance=Member_strategy)
def test_member_member_pwd_setter(instance):
    original = instance.member_pwd
    instance.member_pwd = original
    assert instance.member_pwd == original

@given(instance=Books_strategy)
@settings(max_examples=50)
def test_books_instantiation(instance):
    assert isinstance(instance, Books)



@given(instance=Books_strategy)
def test_books_author_name_setter(instance):
    original = instance.author_name
    instance.author_name = original
    assert instance.author_name == original



@given(instance=Books_strategy)
def test_books_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Books_strategy)
def test_books_ISBN_no_setter(instance):
    original = instance.ISBN_no
    instance.ISBN_no = original
    assert instance.ISBN_no == original



@given(instance=Books_strategy)
def test_books_book_id_setter(instance):
    original = instance.book_id
    instance.book_id = original
    assert instance.book_id == original



@given(instance=Books_strategy)
def test_books_book_qty_setter(instance):
    original = instance.book_qty
    instance.book_qty = original
    assert instance.book_qty == original



@given(instance=Books_strategy)
def test_books_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original
