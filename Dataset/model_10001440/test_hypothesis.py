import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Data_Pembayaran,
    Pelanggan,
    Admin,
    Login_Admin,
    Cetak_Slip_UseCase,
    Memproses_Database_UseCase,
    Melakukan_Transaksi_UseCase,
    Memverivikasi_Data_UseCase,
    Mengentry_Data_UseCase,
    Admin_Actor,
    Pelanggan__Actor,
    Melakukan_Registrasi_UseCase,
    Melakukan_Login_UseCase,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_data_pembayaran_is_not_abstract():
    assert not inspect.isabstract(Data_Pembayaran)


def test_data_pembayaran_constructor_exists():
    assert callable(Data_Pembayaran.__init__)


def test_data_pembayaran_constructor_args():
    sig = inspect.signature(Data_Pembayaran.__init__)
    params = list(sig.parameters.keys())
    assert "angsuranke" in params, "Missing parameter 'angsuranke'"
    assert "kode_kredit" in params, "Missing parameter 'kode_kredit'"
    assert "angsuran" in params, "Missing parameter 'angsuran'"
    assert "kode_bayar" in params, "Missing parameter 'kode_bayar'"
    assert "keterangan" in params, "Missing parameter 'keterangan'"
    assert "tanggal_bayar" in params, "Missing parameter 'tanggal_bayar'"

def test_data_pembayaran_has_angsuranke():
    assert hasattr(Data_Pembayaran, "angsuranke")
    descriptor = None
    for klass in Data_Pembayaran.__mro__:
        if "angsuranke" in klass.__dict__:
            descriptor = klass.__dict__["angsuranke"]
            break
    assert isinstance(descriptor, property)

def test_data_pembayaran_has_kode_kredit():
    assert hasattr(Data_Pembayaran, "kode_kredit")
    descriptor = None
    for klass in Data_Pembayaran.__mro__:
        if "kode_kredit" in klass.__dict__:
            descriptor = klass.__dict__["kode_kredit"]
            break
    assert isinstance(descriptor, property)

def test_data_pembayaran_has_angsuran():
    assert hasattr(Data_Pembayaran, "angsuran")
    descriptor = None
    for klass in Data_Pembayaran.__mro__:
        if "angsuran" in klass.__dict__:
            descriptor = klass.__dict__["angsuran"]
            break
    assert isinstance(descriptor, property)

def test_data_pembayaran_has_kode_bayar():
    assert hasattr(Data_Pembayaran, "kode_bayar")
    descriptor = None
    for klass in Data_Pembayaran.__mro__:
        if "kode_bayar" in klass.__dict__:
            descriptor = klass.__dict__["kode_bayar"]
            break
    assert isinstance(descriptor, property)

def test_data_pembayaran_has_keterangan():
    assert hasattr(Data_Pembayaran, "keterangan")
    descriptor = None
    for klass in Data_Pembayaran.__mro__:
        if "keterangan" in klass.__dict__:
            descriptor = klass.__dict__["keterangan"]
            break
    assert isinstance(descriptor, property)

def test_data_pembayaran_has_tanggal_bayar():
    assert hasattr(Data_Pembayaran, "tanggal_bayar")
    descriptor = None
    for klass in Data_Pembayaran.__mro__:
        if "tanggal_bayar" in klass.__dict__:
            descriptor = klass.__dict__["tanggal_bayar"]
            break
    assert isinstance(descriptor, property)



def test_pelanggan_is_not_abstract():
    assert not inspect.isabstract(Pelanggan)


def test_pelanggan_constructor_exists():
    assert callable(Pelanggan.__init__)


def test_pelanggan_constructor_args():
    sig = inspect.signature(Pelanggan.__init__)
    params = list(sig.parameters.keys())
    assert "kode_pelanggan" in params, "Missing parameter 'kode_pelanggan'"
    assert "alamat" in params, "Missing parameter 'alamat'"
    assert "nama" in params, "Missing parameter 'nama'"

def test_pelanggan_has_kode_pelanggan():
    assert hasattr(Pelanggan, "kode_pelanggan")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "kode_pelanggan" in klass.__dict__:
            descriptor = klass.__dict__["kode_pelanggan"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_alamat():
    assert hasattr(Pelanggan, "alamat")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "alamat" in klass.__dict__:
            descriptor = klass.__dict__["alamat"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_nama():
    assert hasattr(Pelanggan, "nama")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "nama" in klass.__dict__:
            descriptor = klass.__dict__["nama"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "alamat" in params, "Missing parameter 'alamat'"
    assert "id" in params, "Missing parameter 'id'"
    assert "nama" in params, "Missing parameter 'nama'"
    assert "no_tlp" in params, "Missing parameter 'no_tlp'"

def test_admin_has_alamat():
    assert hasattr(Admin, "alamat")
    descriptor = None
    for klass in Admin.__mro__:
        if "alamat" in klass.__dict__:
            descriptor = klass.__dict__["alamat"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_id():
    assert hasattr(Admin, "id")
    descriptor = None
    for klass in Admin.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_nama():
    assert hasattr(Admin, "nama")
    descriptor = None
    for klass in Admin.__mro__:
        if "nama" in klass.__dict__:
            descriptor = klass.__dict__["nama"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_no_tlp():
    assert hasattr(Admin, "no_tlp")
    descriptor = None
    for klass in Admin.__mro__:
        if "no_tlp" in klass.__dict__:
            descriptor = klass.__dict__["no_tlp"]
            break
    assert isinstance(descriptor, property)



def test_login_admin_is_not_abstract():
    assert not inspect.isabstract(Login_Admin)


def test_login_admin_constructor_exists():
    assert callable(Login_Admin.__init__)


def test_login_admin_constructor_args():
    sig = inspect.signature(Login_Admin.__init__)
    params = list(sig.parameters.keys())
    assert "User_name" in params, "Missing parameter 'User_name'"
    assert "attribute" in params, "Missing parameter 'attribute'"

def test_login_admin_has_User_name():
    assert hasattr(Login_Admin, "User_name")
    descriptor = None
    for klass in Login_Admin.__mro__:
        if "User_name" in klass.__dict__:
            descriptor = klass.__dict__["User_name"]
            break
    assert isinstance(descriptor, property)

def test_login_admin_has_attribute():
    assert hasattr(Login_Admin, "attribute")
    descriptor = None
    for klass in Login_Admin.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)



def test_cetak_slip_usecase_is_not_abstract():
    assert not inspect.isabstract(Cetak_Slip_UseCase)


def test_cetak_slip_usecase_constructor_exists():
    assert callable(Cetak_Slip_UseCase.__init__)


def test_cetak_slip_usecase_constructor_args():
    sig = inspect.signature(Cetak_Slip_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_memproses_database_usecase_is_not_abstract():
    assert not inspect.isabstract(Memproses_Database_UseCase)


def test_memproses_database_usecase_constructor_exists():
    assert callable(Memproses_Database_UseCase.__init__)


def test_memproses_database_usecase_constructor_args():
    sig = inspect.signature(Memproses_Database_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_melakukan_transaksi_usecase_is_not_abstract():
    assert not inspect.isabstract(Melakukan_Transaksi_UseCase)


def test_melakukan_transaksi_usecase_constructor_exists():
    assert callable(Melakukan_Transaksi_UseCase.__init__)


def test_melakukan_transaksi_usecase_constructor_args():
    sig = inspect.signature(Melakukan_Transaksi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_memverivikasi_data_usecase_is_not_abstract():
    assert not inspect.isabstract(Memverivikasi_Data_UseCase)


def test_memverivikasi_data_usecase_constructor_exists():
    assert callable(Memverivikasi_Data_UseCase.__init__)


def test_memverivikasi_data_usecase_constructor_args():
    sig = inspect.signature(Memverivikasi_Data_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_mengentry_data_usecase_is_not_abstract():
    assert not inspect.isabstract(Mengentry_Data_UseCase)


def test_mengentry_data_usecase_constructor_exists():
    assert callable(Mengentry_Data_UseCase.__init__)


def test_mengentry_data_usecase_constructor_args():
    sig = inspect.signature(Mengentry_Data_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_pelanggan__actor_is_not_abstract():
    assert not inspect.isabstract(Pelanggan__Actor)


def test_pelanggan__actor_constructor_exists():
    assert callable(Pelanggan__Actor.__init__)


def test_pelanggan__actor_constructor_args():
    sig = inspect.signature(Pelanggan__Actor.__init__)
    params = list(sig.parameters.keys())



def test_melakukan_registrasi_usecase_is_not_abstract():
    assert not inspect.isabstract(Melakukan_Registrasi_UseCase)


def test_melakukan_registrasi_usecase_constructor_exists():
    assert callable(Melakukan_Registrasi_UseCase.__init__)


def test_melakukan_registrasi_usecase_constructor_args():
    sig = inspect.signature(Melakukan_Registrasi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_melakukan_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Melakukan_Login_UseCase)


def test_melakukan_login_usecase_constructor_exists():
    assert callable(Melakukan_Login_UseCase.__init__)


def test_melakukan_login_usecase_constructor_args():
    sig = inspect.signature(Melakukan_Login_UseCase.__init__)
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
Data_Pembayaran_strategy = st.builds(
    Data_Pembayaran,
    angsuranke=
        st.integers(),
    kode_kredit=
        safe_text,
    angsuran=
        st.integers(),
    kode_bayar=
        safe_text,
    keterangan=
        safe_text,
    tanggal_bayar=
        safe_text
)
Pelanggan_strategy = st.builds(
    Pelanggan,
    kode_pelanggan=
        safe_text,
    alamat=
        safe_text,
    nama=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    alamat=
        safe_text,
    id=
        safe_text,
    nama=
        safe_text,
    no_tlp=
        st.integers()
)
Login_Admin_strategy = st.builds(
    Login_Admin,
    User_name=
        safe_text,
    attribute=
        safe_text
)
Cetak_Slip_UseCase_strategy = st.builds(
    Cetak_Slip_UseCase,
)
Memproses_Database_UseCase_strategy = st.builds(
    Memproses_Database_UseCase,
)
Melakukan_Transaksi_UseCase_strategy = st.builds(
    Melakukan_Transaksi_UseCase,
)
Memverivikasi_Data_UseCase_strategy = st.builds(
    Memverivikasi_Data_UseCase,
)
Mengentry_Data_UseCase_strategy = st.builds(
    Mengentry_Data_UseCase,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)
Pelanggan__Actor_strategy = st.builds(
    Pelanggan__Actor,
)
Melakukan_Registrasi_UseCase_strategy = st.builds(
    Melakukan_Registrasi_UseCase,
)
Melakukan_Login_UseCase_strategy = st.builds(
    Melakukan_Login_UseCase,
)

@given(instance=Data_Pembayaran_strategy)
@settings(max_examples=50)
def test_data_pembayaran_instantiation(instance):
    assert isinstance(instance, Data_Pembayaran)



@given(instance=Data_Pembayaran_strategy)
def test_data_pembayaran_angsuranke_setter(instance):
    original = instance.angsuranke
    instance.angsuranke = original
    assert instance.angsuranke == original



@given(instance=Data_Pembayaran_strategy)
def test_data_pembayaran_kode_kredit_setter(instance):
    original = instance.kode_kredit
    instance.kode_kredit = original
    assert instance.kode_kredit == original



@given(instance=Data_Pembayaran_strategy)
def test_data_pembayaran_angsuran_setter(instance):
    original = instance.angsuran
    instance.angsuran = original
    assert instance.angsuran == original



@given(instance=Data_Pembayaran_strategy)
def test_data_pembayaran_kode_bayar_setter(instance):
    original = instance.kode_bayar
    instance.kode_bayar = original
    assert instance.kode_bayar == original



@given(instance=Data_Pembayaran_strategy)
def test_data_pembayaran_keterangan_setter(instance):
    original = instance.keterangan
    instance.keterangan = original
    assert instance.keterangan == original



@given(instance=Data_Pembayaran_strategy)
def test_data_pembayaran_tanggal_bayar_setter(instance):
    original = instance.tanggal_bayar
    instance.tanggal_bayar = original
    assert instance.tanggal_bayar == original

@given(instance=Pelanggan_strategy)
@settings(max_examples=50)
def test_pelanggan_instantiation(instance):
    assert isinstance(instance, Pelanggan)



@given(instance=Pelanggan_strategy)
def test_pelanggan_kode_pelanggan_setter(instance):
    original = instance.kode_pelanggan
    instance.kode_pelanggan = original
    assert instance.kode_pelanggan == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_alamat_setter(instance):
    original = instance.alamat
    instance.alamat = original
    assert instance.alamat == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_nama_setter(instance):
    original = instance.nama
    instance.nama = original
    assert instance.nama == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_alamat_setter(instance):
    original = instance.alamat
    instance.alamat = original
    assert instance.alamat == original



@given(instance=Admin_strategy)
def test_admin_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Admin_strategy)
def test_admin_nama_setter(instance):
    original = instance.nama
    instance.nama = original
    assert instance.nama == original



@given(instance=Admin_strategy)
def test_admin_no_tlp_setter(instance):
    original = instance.no_tlp
    instance.no_tlp = original
    assert instance.no_tlp == original

@given(instance=Login_Admin_strategy)
@settings(max_examples=50)
def test_login_admin_instantiation(instance):
    assert isinstance(instance, Login_Admin)



@given(instance=Login_Admin_strategy)
def test_login_admin_User_name_setter(instance):
    original = instance.User_name
    instance.User_name = original
    assert instance.User_name == original



@given(instance=Login_Admin_strategy)
def test_login_admin_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original

@given(instance=Cetak_Slip_UseCase_strategy)
@settings(max_examples=50)
def test_cetak_slip_usecase_instantiation(instance):
    assert isinstance(instance, Cetak_Slip_UseCase)

@given(instance=Memproses_Database_UseCase_strategy)
@settings(max_examples=50)
def test_memproses_database_usecase_instantiation(instance):
    assert isinstance(instance, Memproses_Database_UseCase)

@given(instance=Melakukan_Transaksi_UseCase_strategy)
@settings(max_examples=50)
def test_melakukan_transaksi_usecase_instantiation(instance):
    assert isinstance(instance, Melakukan_Transaksi_UseCase)

@given(instance=Memverivikasi_Data_UseCase_strategy)
@settings(max_examples=50)
def test_memverivikasi_data_usecase_instantiation(instance):
    assert isinstance(instance, Memverivikasi_Data_UseCase)

@given(instance=Mengentry_Data_UseCase_strategy)
@settings(max_examples=50)
def test_mengentry_data_usecase_instantiation(instance):
    assert isinstance(instance, Mengentry_Data_UseCase)

@given(instance=Admin_Actor_strategy)
@settings(max_examples=50)
def test_admin_actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)

@given(instance=Pelanggan__Actor_strategy)
@settings(max_examples=50)
def test_pelanggan__actor_instantiation(instance):
    assert isinstance(instance, Pelanggan__Actor)

@given(instance=Melakukan_Registrasi_UseCase_strategy)
@settings(max_examples=50)
def test_melakukan_registrasi_usecase_instantiation(instance):
    assert isinstance(instance, Melakukan_Registrasi_UseCase)

@given(instance=Melakukan_Login_UseCase_strategy)
@settings(max_examples=50)
def test_melakukan_login_usecase_instantiation(instance):
    assert isinstance(instance, Melakukan_Login_UseCase)
