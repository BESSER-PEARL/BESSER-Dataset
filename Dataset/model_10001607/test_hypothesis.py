import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    HasilBidding,
    Bidding,
    Biddee,
    Bidder,
    Admin,
    User,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_hasilbidding_is_not_abstract():
    assert not inspect.isabstract(HasilBidding)


def test_hasilbidding_constructor_exists():
    assert callable(HasilBidding.__init__)


def test_hasilbidding_constructor_args():
    sig = inspect.signature(HasilBidding.__init__)
    params = list(sig.parameters.keys())



def test_bidding_is_not_abstract():
    assert not inspect.isabstract(Bidding)


def test_bidding_constructor_exists():
    assert callable(Bidding.__init__)


def test_bidding_constructor_args():
    sig = inspect.signature(Bidding.__init__)
    params = list(sig.parameters.keys())
    assert "bidder" in params, "Missing parameter 'bidder'"
    assert "catatanBidder" in params, "Missing parameter 'catatanBidder'"
    assert "notulensi" in params, "Missing parameter 'notulensi'"
    assert "biddee" in params, "Missing parameter 'biddee'"
    assert "berkas" in params, "Missing parameter 'berkas'"
    assert "jabatan" in params, "Missing parameter 'jabatan'"
    assert "statusBidding" in params, "Missing parameter 'statusBidding'"
    assert "nilai" in params, "Missing parameter 'nilai'"

def test_bidding_has_bidder():
    assert hasattr(Bidding, "bidder")
    descriptor = None
    for klass in Bidding.__mro__:
        if "bidder" in klass.__dict__:
            descriptor = klass.__dict__["bidder"]
            break
    assert isinstance(descriptor, property)

def test_bidding_has_catatanBidder():
    assert hasattr(Bidding, "catatanBidder")
    descriptor = None
    for klass in Bidding.__mro__:
        if "catatanBidder" in klass.__dict__:
            descriptor = klass.__dict__["catatanBidder"]
            break
    assert isinstance(descriptor, property)

def test_bidding_has_notulensi():
    assert hasattr(Bidding, "notulensi")
    descriptor = None
    for klass in Bidding.__mro__:
        if "notulensi" in klass.__dict__:
            descriptor = klass.__dict__["notulensi"]
            break
    assert isinstance(descriptor, property)

def test_bidding_has_biddee():
    assert hasattr(Bidding, "biddee")
    descriptor = None
    for klass in Bidding.__mro__:
        if "biddee" in klass.__dict__:
            descriptor = klass.__dict__["biddee"]
            break
    assert isinstance(descriptor, property)

def test_bidding_has_berkas():
    assert hasattr(Bidding, "berkas")
    descriptor = None
    for klass in Bidding.__mro__:
        if "berkas" in klass.__dict__:
            descriptor = klass.__dict__["berkas"]
            break
    assert isinstance(descriptor, property)

def test_bidding_has_jabatan():
    assert hasattr(Bidding, "jabatan")
    descriptor = None
    for klass in Bidding.__mro__:
        if "jabatan" in klass.__dict__:
            descriptor = klass.__dict__["jabatan"]
            break
    assert isinstance(descriptor, property)

def test_bidding_has_statusBidding():
    assert hasattr(Bidding, "statusBidding")
    descriptor = None
    for klass in Bidding.__mro__:
        if "statusBidding" in klass.__dict__:
            descriptor = klass.__dict__["statusBidding"]
            break
    assert isinstance(descriptor, property)

def test_bidding_has_nilai():
    assert hasattr(Bidding, "nilai")
    descriptor = None
    for klass in Bidding.__mro__:
        if "nilai" in klass.__dict__:
            descriptor = klass.__dict__["nilai"]
            break
    assert isinstance(descriptor, property)



def test_biddee_is_not_abstract():
    assert not inspect.isabstract(Biddee)


def test_biddee_constructor_exists():
    assert callable(Biddee.__init__)


def test_biddee_constructor_args():
    sig = inspect.signature(Biddee.__init__)
    params = list(sig.parameters.keys())
    assert "statusBiddee" in params, "Missing parameter 'statusBiddee'"

def test_biddee_has_statusBiddee():
    assert hasattr(Biddee, "statusBiddee")
    descriptor = None
    for klass in Biddee.__mro__:
        if "statusBiddee" in klass.__dict__:
            descriptor = klass.__dict__["statusBiddee"]
            break
    assert isinstance(descriptor, property)



def test_bidder_is_not_abstract():
    assert not inspect.isabstract(Bidder)


def test_bidder_constructor_exists():
    assert callable(Bidder.__init__)


def test_bidder_constructor_args():
    sig = inspect.signature(Bidder.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())



def test_user_is_not_abstract():
    assert not inspect.isabstract(User)


def test_user_constructor_exists():
    assert callable(User.__init__)


def test_user_constructor_args():
    sig = inspect.signature(User.__init__)
    params = list(sig.parameters.keys())
    assert "userName" in params, "Missing parameter 'userName'"
    assert "nama" in params, "Missing parameter 'nama'"
    assert "loginStatus" in params, "Missing parameter 'loginStatus'"
    assert "password" in params, "Missing parameter 'password'"

def test_user_has_userName():
    assert hasattr(User, "userName")
    descriptor = None
    for klass in User.__mro__:
        if "userName" in klass.__dict__:
            descriptor = klass.__dict__["userName"]
            break
    assert isinstance(descriptor, property)

def test_user_has_nama():
    assert hasattr(User, "nama")
    descriptor = None
    for klass in User.__mro__:
        if "nama" in klass.__dict__:
            descriptor = klass.__dict__["nama"]
            break
    assert isinstance(descriptor, property)

def test_user_has_loginStatus():
    assert hasattr(User, "loginStatus")
    descriptor = None
    for klass in User.__mro__:
        if "loginStatus" in klass.__dict__:
            descriptor = klass.__dict__["loginStatus"]
            break
    assert isinstance(descriptor, property)

def test_user_has_password():
    assert hasattr(User, "password")
    descriptor = None
    for klass in User.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
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
HasilBidding_strategy = st.builds(
    HasilBidding,
)
Bidding_strategy = st.builds(
    Bidding,
    bidder=
        safe_text,
    catatanBidder=
        safe_text,
    notulensi=
        safe_text,
    biddee=
        safe_text,
    berkas=
        safe_text,
    jabatan=
        safe_text,
    statusBidding=
        safe_text,
    nilai=
        st.integers()
)
Biddee_strategy = st.builds(
    Biddee,
    statusBiddee=
        safe_text
)
Bidder_strategy = st.builds(
    Bidder,
)
Admin_strategy = st.builds(
    Admin,
)
User_strategy = st.builds(
    User,
    userName=
        safe_text,
    nama=
        safe_text,
    loginStatus=
        safe_text,
    password=
        safe_text
)

@given(instance=HasilBidding_strategy)
@settings(max_examples=50)
def test_hasilbidding_instantiation(instance):
    assert isinstance(instance, HasilBidding)

@given(instance=Bidding_strategy)
@settings(max_examples=50)
def test_bidding_instantiation(instance):
    assert isinstance(instance, Bidding)



@given(instance=Bidding_strategy)
def test_bidding_bidder_setter(instance):
    original = instance.bidder
    instance.bidder = original
    assert instance.bidder == original



@given(instance=Bidding_strategy)
def test_bidding_catatanBidder_setter(instance):
    original = instance.catatanBidder
    instance.catatanBidder = original
    assert instance.catatanBidder == original



@given(instance=Bidding_strategy)
def test_bidding_notulensi_setter(instance):
    original = instance.notulensi
    instance.notulensi = original
    assert instance.notulensi == original



@given(instance=Bidding_strategy)
def test_bidding_biddee_setter(instance):
    original = instance.biddee
    instance.biddee = original
    assert instance.biddee == original



@given(instance=Bidding_strategy)
def test_bidding_berkas_setter(instance):
    original = instance.berkas
    instance.berkas = original
    assert instance.berkas == original



@given(instance=Bidding_strategy)
def test_bidding_jabatan_setter(instance):
    original = instance.jabatan
    instance.jabatan = original
    assert instance.jabatan == original



@given(instance=Bidding_strategy)
def test_bidding_statusBidding_setter(instance):
    original = instance.statusBidding
    instance.statusBidding = original
    assert instance.statusBidding == original



@given(instance=Bidding_strategy)
def test_bidding_nilai_setter(instance):
    original = instance.nilai
    instance.nilai = original
    assert instance.nilai == original

@given(instance=Biddee_strategy)
@settings(max_examples=50)
def test_biddee_instantiation(instance):
    assert isinstance(instance, Biddee)



@given(instance=Biddee_strategy)
def test_biddee_statusBiddee_setter(instance):
    original = instance.statusBiddee
    instance.statusBiddee = original
    assert instance.statusBiddee == original

@given(instance=Bidder_strategy)
@settings(max_examples=50)
def test_bidder_instantiation(instance):
    assert isinstance(instance, Bidder)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)

@given(instance=User_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, User)



@given(instance=User_strategy)
def test_user_userName_setter(instance):
    original = instance.userName
    instance.userName = original
    assert instance.userName == original



@given(instance=User_strategy)
def test_user_nama_setter(instance):
    original = instance.nama
    instance.nama = original
    assert instance.nama == original



@given(instance=User_strategy)
def test_user_loginStatus_setter(instance):
    original = instance.loginStatus
    instance.loginStatus = original
    assert instance.loginStatus == original



@given(instance=User_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original
