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
    Ar_Condicionado,
    Quado_Branco,
    Members,
    Retro_Projetor,
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
    assert "gender" in params, "Missing parameter 'gender'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "password" in params, "Missing parameter 'password'"
    assert "Staff_ID" in params, "Missing parameter 'Staff_ID'"
    assert "username" in params, "Missing parameter 'username'"
    assert "address" in params, "Missing parameter 'address'"
    assert "contact" in params, "Missing parameter 'contact'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "position" in params, "Missing parameter 'position'"
    assert "email" in params, "Missing parameter 'email'"

def test_staff_has_gender():
    assert hasattr(Staff, "gender")
    descriptor = None
    for klass in Staff.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
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

def test_staff_has_password():
    assert hasattr(Staff, "password")
    descriptor = None
    for klass in Staff.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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

def test_staff_has_username():
    assert hasattr(Staff, "username")
    descriptor = None
    for klass in Staff.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
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

def test_staff_has_lname():
    assert hasattr(Staff, "lname")
    descriptor = None
    for klass in Staff.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
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



def test_ar_condicionado_is_not_abstract():
    assert not inspect.isabstract(Ar_Condicionado)


def test_ar_condicionado_constructor_exists():
    assert callable(Ar_Condicionado.__init__)


def test_ar_condicionado_constructor_args():
    sig = inspect.signature(Ar_Condicionado.__init__)
    params = list(sig.parameters.keys())
    assert "returned_date" in params, "Missing parameter 'returned_date'"
    assert "book_id" in params, "Missing parameter 'book_id'"
    assert "fine_amount" in params, "Missing parameter 'fine_amount'"
    assert "borrowed_date" in params, "Missing parameter 'borrowed_date'"
    assert "member_id" in params, "Missing parameter 'member_id'"

def test_ar_condicionado_has_returned_date():
    assert hasattr(Ar_Condicionado, "returned_date")
    descriptor = None
    for klass in Ar_Condicionado.__mro__:
        if "returned_date" in klass.__dict__:
            descriptor = klass.__dict__["returned_date"]
            break
    assert isinstance(descriptor, property)

def test_ar_condicionado_has_book_id():
    assert hasattr(Ar_Condicionado, "book_id")
    descriptor = None
    for klass in Ar_Condicionado.__mro__:
        if "book_id" in klass.__dict__:
            descriptor = klass.__dict__["book_id"]
            break
    assert isinstance(descriptor, property)

def test_ar_condicionado_has_fine_amount():
    assert hasattr(Ar_Condicionado, "fine_amount")
    descriptor = None
    for klass in Ar_Condicionado.__mro__:
        if "fine_amount" in klass.__dict__:
            descriptor = klass.__dict__["fine_amount"]
            break
    assert isinstance(descriptor, property)

def test_ar_condicionado_has_borrowed_date():
    assert hasattr(Ar_Condicionado, "borrowed_date")
    descriptor = None
    for klass in Ar_Condicionado.__mro__:
        if "borrowed_date" in klass.__dict__:
            descriptor = klass.__dict__["borrowed_date"]
            break
    assert isinstance(descriptor, property)

def test_ar_condicionado_has_member_id():
    assert hasattr(Ar_Condicionado, "member_id")
    descriptor = None
    for klass in Ar_Condicionado.__mro__:
        if "member_id" in klass.__dict__:
            descriptor = klass.__dict__["member_id"]
            break
    assert isinstance(descriptor, property)



def test_quado_branco_is_not_abstract():
    assert not inspect.isabstract(Quado_Branco)


def test_quado_branco_constructor_exists():
    assert callable(Quado_Branco.__init__)


def test_quado_branco_constructor_args():
    sig = inspect.signature(Quado_Branco.__init__)
    params = list(sig.parameters.keys())
    assert "lname" in params, "Missing parameter 'lname'"
    assert "dob" in params, "Missing parameter 'dob'"
    assert "member_pwd" in params, "Missing parameter 'member_pwd'"
    assert "member_id" in params, "Missing parameter 'member_id'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "address" in params, "Missing parameter 'address'"
    assert "cont_no" in params, "Missing parameter 'cont_no'"

def test_quado_branco_has_lname():
    assert hasattr(Quado_Branco, "lname")
    descriptor = None
    for klass in Quado_Branco.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)

def test_quado_branco_has_dob():
    assert hasattr(Quado_Branco, "dob")
    descriptor = None
    for klass in Quado_Branco.__mro__:
        if "dob" in klass.__dict__:
            descriptor = klass.__dict__["dob"]
            break
    assert isinstance(descriptor, property)

def test_quado_branco_has_member_pwd():
    assert hasattr(Quado_Branco, "member_pwd")
    descriptor = None
    for klass in Quado_Branco.__mro__:
        if "member_pwd" in klass.__dict__:
            descriptor = klass.__dict__["member_pwd"]
            break
    assert isinstance(descriptor, property)

def test_quado_branco_has_member_id():
    assert hasattr(Quado_Branco, "member_id")
    descriptor = None
    for klass in Quado_Branco.__mro__:
        if "member_id" in klass.__dict__:
            descriptor = klass.__dict__["member_id"]
            break
    assert isinstance(descriptor, property)

def test_quado_branco_has_gender():
    assert hasattr(Quado_Branco, "gender")
    descriptor = None
    for klass in Quado_Branco.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_quado_branco_has_fname():
    assert hasattr(Quado_Branco, "fname")
    descriptor = None
    for klass in Quado_Branco.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_quado_branco_has_address():
    assert hasattr(Quado_Branco, "address")
    descriptor = None
    for klass in Quado_Branco.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_quado_branco_has_cont_no():
    assert hasattr(Quado_Branco, "cont_no")
    descriptor = None
    for klass in Quado_Branco.__mro__:
        if "cont_no" in klass.__dict__:
            descriptor = klass.__dict__["cont_no"]
            break
    assert isinstance(descriptor, property)



def test_members_is_not_abstract():
    assert not inspect.isabstract(Members)


def test_members_constructor_exists():
    assert callable(Members.__init__)


def test_members_constructor_args():
    sig = inspect.signature(Members.__init__)
    params = list(sig.parameters.keys())
    assert "member_pwd" in params, "Missing parameter 'member_pwd'"
    assert "member_id" in params, "Missing parameter 'member_id'"
    assert "lname" in params, "Missing parameter 'lname'"
    assert "dob" in params, "Missing parameter 'dob'"
    assert "gender" in params, "Missing parameter 'gender'"
    assert "address" in params, "Missing parameter 'address'"
    assert "fname" in params, "Missing parameter 'fname'"
    assert "cont_no" in params, "Missing parameter 'cont_no'"

def test_members_has_member_pwd():
    assert hasattr(Members, "member_pwd")
    descriptor = None
    for klass in Members.__mro__:
        if "member_pwd" in klass.__dict__:
            descriptor = klass.__dict__["member_pwd"]
            break
    assert isinstance(descriptor, property)

def test_members_has_member_id():
    assert hasattr(Members, "member_id")
    descriptor = None
    for klass in Members.__mro__:
        if "member_id" in klass.__dict__:
            descriptor = klass.__dict__["member_id"]
            break
    assert isinstance(descriptor, property)

def test_members_has_lname():
    assert hasattr(Members, "lname")
    descriptor = None
    for klass in Members.__mro__:
        if "lname" in klass.__dict__:
            descriptor = klass.__dict__["lname"]
            break
    assert isinstance(descriptor, property)

def test_members_has_dob():
    assert hasattr(Members, "dob")
    descriptor = None
    for klass in Members.__mro__:
        if "dob" in klass.__dict__:
            descriptor = klass.__dict__["dob"]
            break
    assert isinstance(descriptor, property)

def test_members_has_gender():
    assert hasattr(Members, "gender")
    descriptor = None
    for klass in Members.__mro__:
        if "gender" in klass.__dict__:
            descriptor = klass.__dict__["gender"]
            break
    assert isinstance(descriptor, property)

def test_members_has_address():
    assert hasattr(Members, "address")
    descriptor = None
    for klass in Members.__mro__:
        if "address" in klass.__dict__:
            descriptor = klass.__dict__["address"]
            break
    assert isinstance(descriptor, property)

def test_members_has_fname():
    assert hasattr(Members, "fname")
    descriptor = None
    for klass in Members.__mro__:
        if "fname" in klass.__dict__:
            descriptor = klass.__dict__["fname"]
            break
    assert isinstance(descriptor, property)

def test_members_has_cont_no():
    assert hasattr(Members, "cont_no")
    descriptor = None
    for klass in Members.__mro__:
        if "cont_no" in klass.__dict__:
            descriptor = klass.__dict__["cont_no"]
            break
    assert isinstance(descriptor, property)



def test_retro_projetor_is_not_abstract():
    assert not inspect.isabstract(Retro_Projetor)


def test_retro_projetor_constructor_exists():
    assert callable(Retro_Projetor.__init__)


def test_retro_projetor_constructor_args():
    sig = inspect.signature(Retro_Projetor.__init__)
    params = list(sig.parameters.keys())
    assert "author_name" in params, "Missing parameter 'author_name'"
    assert "book_id" in params, "Missing parameter 'book_id'"
    assert "book_qty" in params, "Missing parameter 'book_qty'"
    assert "title" in params, "Missing parameter 'title'"
    assert "publisher" in params, "Missing parameter 'publisher'"
    assert "ISBN_no" in params, "Missing parameter 'ISBN_no'"

def test_retro_projetor_has_author_name():
    assert hasattr(Retro_Projetor, "author_name")
    descriptor = None
    for klass in Retro_Projetor.__mro__:
        if "author_name" in klass.__dict__:
            descriptor = klass.__dict__["author_name"]
            break
    assert isinstance(descriptor, property)

def test_retro_projetor_has_book_id():
    assert hasattr(Retro_Projetor, "book_id")
    descriptor = None
    for klass in Retro_Projetor.__mro__:
        if "book_id" in klass.__dict__:
            descriptor = klass.__dict__["book_id"]
            break
    assert isinstance(descriptor, property)

def test_retro_projetor_has_book_qty():
    assert hasattr(Retro_Projetor, "book_qty")
    descriptor = None
    for klass in Retro_Projetor.__mro__:
        if "book_qty" in klass.__dict__:
            descriptor = klass.__dict__["book_qty"]
            break
    assert isinstance(descriptor, property)

def test_retro_projetor_has_title():
    assert hasattr(Retro_Projetor, "title")
    descriptor = None
    for klass in Retro_Projetor.__mro__:
        if "title" in klass.__dict__:
            descriptor = klass.__dict__["title"]
            break
    assert isinstance(descriptor, property)

def test_retro_projetor_has_publisher():
    assert hasattr(Retro_Projetor, "publisher")
    descriptor = None
    for klass in Retro_Projetor.__mro__:
        if "publisher" in klass.__dict__:
            descriptor = klass.__dict__["publisher"]
            break
    assert isinstance(descriptor, property)

def test_retro_projetor_has_ISBN_no():
    assert hasattr(Retro_Projetor, "ISBN_no")
    descriptor = None
    for klass in Retro_Projetor.__mro__:
        if "ISBN_no" in klass.__dict__:
            descriptor = klass.__dict__["ISBN_no"]
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
    gender=
        safe_text,
    fname=
        safe_text,
    password=
        safe_text,
    Staff_ID=
        st.integers(),
    username=
        safe_text,
    address=
        safe_text,
    contact=
        st.integers(),
    lname=
        safe_text,
    position=
        safe_text,
    email=
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
Ar_Condicionado_strategy = st.builds(
    Ar_Condicionado,
    returned_date=
        safe_text,
    book_id=
        st.integers(),
    fine_amount=
        st.integers(),
    borrowed_date=
        safe_text,
    member_id=
        st.integers()
)
Quado_Branco_strategy = st.builds(
    Quado_Branco,
    lname=
        safe_text,
    dob=
        safe_text,
    member_pwd=
        safe_text,
    member_id=
        st.integers(),
    gender=
        safe_text,
    fname=
        safe_text,
    address=
        safe_text,
    cont_no=
        st.integers()
)
Members_strategy = st.builds(
    Members,
    member_pwd=
        safe_text,
    member_id=
        st.integers(),
    lname=
        safe_text,
    dob=
        safe_text,
    gender=
        safe_text,
    address=
        safe_text,
    fname=
        safe_text,
    cont_no=
        st.integers()
)
Retro_Projetor_strategy = st.builds(
    Retro_Projetor,
    author_name=
        safe_text,
    book_id=
        st.integers(),
    book_qty=
        st.integers(),
    title=
        safe_text,
    publisher=
        safe_text,
    ISBN_no=
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
def test_staff_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Staff_strategy)
def test_staff_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Staff_strategy)
def test_staff_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Staff_strategy)
def test_staff_Staff_ID_setter(instance):
    original = instance.Staff_ID
    instance.Staff_ID = original
    assert instance.Staff_ID == original



@given(instance=Staff_strategy)
def test_staff_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



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
def test_staff_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



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

@given(instance=Ar_Condicionado_strategy)
@settings(max_examples=50)
def test_ar_condicionado_instantiation(instance):
    assert isinstance(instance, Ar_Condicionado)



@given(instance=Ar_Condicionado_strategy)
def test_ar_condicionado_returned_date_setter(instance):
    original = instance.returned_date
    instance.returned_date = original
    assert instance.returned_date == original



@given(instance=Ar_Condicionado_strategy)
def test_ar_condicionado_book_id_setter(instance):
    original = instance.book_id
    instance.book_id = original
    assert instance.book_id == original



@given(instance=Ar_Condicionado_strategy)
def test_ar_condicionado_fine_amount_setter(instance):
    original = instance.fine_amount
    instance.fine_amount = original
    assert instance.fine_amount == original



@given(instance=Ar_Condicionado_strategy)
def test_ar_condicionado_borrowed_date_setter(instance):
    original = instance.borrowed_date
    instance.borrowed_date = original
    assert instance.borrowed_date == original



@given(instance=Ar_Condicionado_strategy)
def test_ar_condicionado_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original

@given(instance=Quado_Branco_strategy)
@settings(max_examples=50)
def test_quado_branco_instantiation(instance):
    assert isinstance(instance, Quado_Branco)



@given(instance=Quado_Branco_strategy)
def test_quado_branco_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Quado_Branco_strategy)
def test_quado_branco_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original



@given(instance=Quado_Branco_strategy)
def test_quado_branco_member_pwd_setter(instance):
    original = instance.member_pwd
    instance.member_pwd = original
    assert instance.member_pwd == original



@given(instance=Quado_Branco_strategy)
def test_quado_branco_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original



@given(instance=Quado_Branco_strategy)
def test_quado_branco_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Quado_Branco_strategy)
def test_quado_branco_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Quado_Branco_strategy)
def test_quado_branco_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Quado_Branco_strategy)
def test_quado_branco_cont_no_setter(instance):
    original = instance.cont_no
    instance.cont_no = original
    assert instance.cont_no == original

@given(instance=Members_strategy)
@settings(max_examples=50)
def test_members_instantiation(instance):
    assert isinstance(instance, Members)



@given(instance=Members_strategy)
def test_members_member_pwd_setter(instance):
    original = instance.member_pwd
    instance.member_pwd = original
    assert instance.member_pwd == original



@given(instance=Members_strategy)
def test_members_member_id_setter(instance):
    original = instance.member_id
    instance.member_id = original
    assert instance.member_id == original



@given(instance=Members_strategy)
def test_members_lname_setter(instance):
    original = instance.lname
    instance.lname = original
    assert instance.lname == original



@given(instance=Members_strategy)
def test_members_dob_setter(instance):
    original = instance.dob
    instance.dob = original
    assert instance.dob == original



@given(instance=Members_strategy)
def test_members_gender_setter(instance):
    original = instance.gender
    instance.gender = original
    assert instance.gender == original



@given(instance=Members_strategy)
def test_members_address_setter(instance):
    original = instance.address
    instance.address = original
    assert instance.address == original



@given(instance=Members_strategy)
def test_members_fname_setter(instance):
    original = instance.fname
    instance.fname = original
    assert instance.fname == original



@given(instance=Members_strategy)
def test_members_cont_no_setter(instance):
    original = instance.cont_no
    instance.cont_no = original
    assert instance.cont_no == original

@given(instance=Retro_Projetor_strategy)
@settings(max_examples=50)
def test_retro_projetor_instantiation(instance):
    assert isinstance(instance, Retro_Projetor)



@given(instance=Retro_Projetor_strategy)
def test_retro_projetor_author_name_setter(instance):
    original = instance.author_name
    instance.author_name = original
    assert instance.author_name == original



@given(instance=Retro_Projetor_strategy)
def test_retro_projetor_book_id_setter(instance):
    original = instance.book_id
    instance.book_id = original
    assert instance.book_id == original



@given(instance=Retro_Projetor_strategy)
def test_retro_projetor_book_qty_setter(instance):
    original = instance.book_qty
    instance.book_qty = original
    assert instance.book_qty == original



@given(instance=Retro_Projetor_strategy)
def test_retro_projetor_title_setter(instance):
    original = instance.title
    instance.title = original
    assert instance.title == original



@given(instance=Retro_Projetor_strategy)
def test_retro_projetor_publisher_setter(instance):
    original = instance.publisher
    instance.publisher = original
    assert instance.publisher == original



@given(instance=Retro_Projetor_strategy)
def test_retro_projetor_ISBN_no_setter(instance):
    original = instance.ISBN_no
    instance.ISBN_no = original
    assert instance.ISBN_no == original
