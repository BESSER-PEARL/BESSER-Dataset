import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Kendaraan,
    Pesan,
    Administrasi,
    Pelanggan,
    Admin,
    Pemilik,
    Login,
    RentalMobil,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_kendaraan_is_not_abstract():
    assert not inspect.isabstract(Kendaraan)


def test_kendaraan_constructor_exists():
    assert callable(Kendaraan.__init__)


def test_kendaraan_constructor_args():
    sig = inspect.signature(Kendaraan.__init__)
    params = list(sig.parameters.keys())
    assert "NoRangka" in params, "Missing parameter 'NoRangka'"
    assert "Merk" in params, "Missing parameter 'Merk'"
    assert "Warna" in params, "Missing parameter 'Warna'"
    assert "NoMesin" in params, "Missing parameter 'NoMesin'"
    assert "TahunPembuatan" in params, "Missing parameter 'TahunPembuatan'"
    assert "NoPolisi" in params, "Missing parameter 'NoPolisi'"

def test_kendaraan_has_NoRangka():
    assert hasattr(Kendaraan, "NoRangka")
    descriptor = None
    for klass in Kendaraan.__mro__:
        if "NoRangka" in klass.__dict__:
            descriptor = klass.__dict__["NoRangka"]
            break
    assert isinstance(descriptor, property)

def test_kendaraan_has_Merk():
    assert hasattr(Kendaraan, "Merk")
    descriptor = None
    for klass in Kendaraan.__mro__:
        if "Merk" in klass.__dict__:
            descriptor = klass.__dict__["Merk"]
            break
    assert isinstance(descriptor, property)

def test_kendaraan_has_Warna():
    assert hasattr(Kendaraan, "Warna")
    descriptor = None
    for klass in Kendaraan.__mro__:
        if "Warna" in klass.__dict__:
            descriptor = klass.__dict__["Warna"]
            break
    assert isinstance(descriptor, property)

def test_kendaraan_has_NoMesin():
    assert hasattr(Kendaraan, "NoMesin")
    descriptor = None
    for klass in Kendaraan.__mro__:
        if "NoMesin" in klass.__dict__:
            descriptor = klass.__dict__["NoMesin"]
            break
    assert isinstance(descriptor, property)

def test_kendaraan_has_TahunPembuatan():
    assert hasattr(Kendaraan, "TahunPembuatan")
    descriptor = None
    for klass in Kendaraan.__mro__:
        if "TahunPembuatan" in klass.__dict__:
            descriptor = klass.__dict__["TahunPembuatan"]
            break
    assert isinstance(descriptor, property)

def test_kendaraan_has_NoPolisi():
    assert hasattr(Kendaraan, "NoPolisi")
    descriptor = None
    for klass in Kendaraan.__mro__:
        if "NoPolisi" in klass.__dict__:
            descriptor = klass.__dict__["NoPolisi"]
            break
    assert isinstance(descriptor, property)



def test_pesan_is_not_abstract():
    assert not inspect.isabstract(Pesan)


def test_pesan_constructor_exists():
    assert callable(Pesan.__init__)


def test_pesan_constructor_args():
    sig = inspect.signature(Pesan.__init__)
    params = list(sig.parameters.keys())
    assert "NoPesan" in params, "Missing parameter 'NoPesan'"
    assert "TanggalKembali" in params, "Missing parameter 'TanggalKembali'"
    assert "TanggalRental" in params, "Missing parameter 'TanggalRental'"
    assert "IdPelanggan" in params, "Missing parameter 'IdPelanggan'"

def test_pesan_has_NoPesan():
    assert hasattr(Pesan, "NoPesan")
    descriptor = None
    for klass in Pesan.__mro__:
        if "NoPesan" in klass.__dict__:
            descriptor = klass.__dict__["NoPesan"]
            break
    assert isinstance(descriptor, property)

def test_pesan_has_TanggalKembali():
    assert hasattr(Pesan, "TanggalKembali")
    descriptor = None
    for klass in Pesan.__mro__:
        if "TanggalKembali" in klass.__dict__:
            descriptor = klass.__dict__["TanggalKembali"]
            break
    assert isinstance(descriptor, property)

def test_pesan_has_TanggalRental():
    assert hasattr(Pesan, "TanggalRental")
    descriptor = None
    for klass in Pesan.__mro__:
        if "TanggalRental" in klass.__dict__:
            descriptor = klass.__dict__["TanggalRental"]
            break
    assert isinstance(descriptor, property)

def test_pesan_has_IdPelanggan():
    assert hasattr(Pesan, "IdPelanggan")
    descriptor = None
    for klass in Pesan.__mro__:
        if "IdPelanggan" in klass.__dict__:
            descriptor = klass.__dict__["IdPelanggan"]
            break
    assert isinstance(descriptor, property)



def test_administrasi_is_not_abstract():
    assert not inspect.isabstract(Administrasi)


def test_administrasi_constructor_exists():
    assert callable(Administrasi.__init__)


def test_administrasi_constructor_args():
    sig = inspect.signature(Administrasi.__init__)
    params = list(sig.parameters.keys())
    assert "Kembali" in params, "Missing parameter 'Kembali'"
    assert "NoPesan" in params, "Missing parameter 'NoPesan'"
    assert "Bayar" in params, "Missing parameter 'Bayar'"
    assert "HargaSewa" in params, "Missing parameter 'HargaSewa'"
    assert "IdPelanggan" in params, "Missing parameter 'IdPelanggan'"
    assert "IdAdmin" in params, "Missing parameter 'IdAdmin'"

def test_administrasi_has_Kembali():
    assert hasattr(Administrasi, "Kembali")
    descriptor = None
    for klass in Administrasi.__mro__:
        if "Kembali" in klass.__dict__:
            descriptor = klass.__dict__["Kembali"]
            break
    assert isinstance(descriptor, property)

def test_administrasi_has_NoPesan():
    assert hasattr(Administrasi, "NoPesan")
    descriptor = None
    for klass in Administrasi.__mro__:
        if "NoPesan" in klass.__dict__:
            descriptor = klass.__dict__["NoPesan"]
            break
    assert isinstance(descriptor, property)

def test_administrasi_has_Bayar():
    assert hasattr(Administrasi, "Bayar")
    descriptor = None
    for klass in Administrasi.__mro__:
        if "Bayar" in klass.__dict__:
            descriptor = klass.__dict__["Bayar"]
            break
    assert isinstance(descriptor, property)

def test_administrasi_has_HargaSewa():
    assert hasattr(Administrasi, "HargaSewa")
    descriptor = None
    for klass in Administrasi.__mro__:
        if "HargaSewa" in klass.__dict__:
            descriptor = klass.__dict__["HargaSewa"]
            break
    assert isinstance(descriptor, property)

def test_administrasi_has_IdPelanggan():
    assert hasattr(Administrasi, "IdPelanggan")
    descriptor = None
    for klass in Administrasi.__mro__:
        if "IdPelanggan" in klass.__dict__:
            descriptor = klass.__dict__["IdPelanggan"]
            break
    assert isinstance(descriptor, property)

def test_administrasi_has_IdAdmin():
    assert hasattr(Administrasi, "IdAdmin")
    descriptor = None
    for klass in Administrasi.__mro__:
        if "IdAdmin" in klass.__dict__:
            descriptor = klass.__dict__["IdAdmin"]
            break
    assert isinstance(descriptor, property)



def test_pelanggan_is_not_abstract():
    assert not inspect.isabstract(Pelanggan)


def test_pelanggan_constructor_exists():
    assert callable(Pelanggan.__init__)


def test_pelanggan_constructor_args():
    sig = inspect.signature(Pelanggan.__init__)
    params = list(sig.parameters.keys())
    assert "IdPelanggan" in params, "Missing parameter 'IdPelanggan'"
    assert "NoKTP" in params, "Missing parameter 'NoKTP'"
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Telepon" in params, "Missing parameter 'Telepon'"
    assert "Pekerjaan" in params, "Missing parameter 'Pekerjaan'"
    assert "Alamat" in params, "Missing parameter 'Alamat'"
    assert "JenisKelamin" in params, "Missing parameter 'JenisKelamin'"
    assert "Umur" in params, "Missing parameter 'Umur'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_pelanggan_has_IdPelanggan():
    assert hasattr(Pelanggan, "IdPelanggan")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "IdPelanggan" in klass.__dict__:
            descriptor = klass.__dict__["IdPelanggan"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_NoKTP():
    assert hasattr(Pelanggan, "NoKTP")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "NoKTP" in klass.__dict__:
            descriptor = klass.__dict__["NoKTP"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_Username():
    assert hasattr(Pelanggan, "Username")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_Telepon():
    assert hasattr(Pelanggan, "Telepon")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "Telepon" in klass.__dict__:
            descriptor = klass.__dict__["Telepon"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_Pekerjaan():
    assert hasattr(Pelanggan, "Pekerjaan")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "Pekerjaan" in klass.__dict__:
            descriptor = klass.__dict__["Pekerjaan"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_Alamat():
    assert hasattr(Pelanggan, "Alamat")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "Alamat" in klass.__dict__:
            descriptor = klass.__dict__["Alamat"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_JenisKelamin():
    assert hasattr(Pelanggan, "JenisKelamin")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "JenisKelamin" in klass.__dict__:
            descriptor = klass.__dict__["JenisKelamin"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_Umur():
    assert hasattr(Pelanggan, "Umur")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "Umur" in klass.__dict__:
            descriptor = klass.__dict__["Umur"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_Password():
    assert hasattr(Pelanggan, "Password")
    descriptor = None
    for klass in Pelanggan.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "Password" in params, "Missing parameter 'Password'"
    assert "Username" in params, "Missing parameter 'Username'"

def test_admin_has_Password():
    assert hasattr(Admin, "Password")
    descriptor = None
    for klass in Admin.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_Username():
    assert hasattr(Admin, "Username")
    descriptor = None
    for klass in Admin.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)



def test_pemilik_is_not_abstract():
    assert not inspect.isabstract(Pemilik)


def test_pemilik_constructor_exists():
    assert callable(Pemilik.__init__)


def test_pemilik_constructor_args():
    sig = inspect.signature(Pemilik.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_pemilik_has_Username():
    assert hasattr(Pemilik, "Username")
    descriptor = None
    for klass in Pemilik.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_pemilik_has_Password():
    assert hasattr(Pemilik, "Password")
    descriptor = None
    for klass in Pemilik.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "Username" in params, "Missing parameter 'Username'"
    assert "Password" in params, "Missing parameter 'Password'"

def test_login_has_Username():
    assert hasattr(Login, "Username")
    descriptor = None
    for klass in Login.__mro__:
        if "Username" in klass.__dict__:
            descriptor = klass.__dict__["Username"]
            break
    assert isinstance(descriptor, property)

def test_login_has_Password():
    assert hasattr(Login, "Password")
    descriptor = None
    for klass in Login.__mro__:
        if "Password" in klass.__dict__:
            descriptor = klass.__dict__["Password"]
            break
    assert isinstance(descriptor, property)



def test_rentalmobil_is_not_abstract():
    assert not inspect.isabstract(RentalMobil)


def test_rentalmobil_constructor_exists():
    assert callable(RentalMobil.__init__)


def test_rentalmobil_constructor_args():
    sig = inspect.signature(RentalMobil.__init__)
    params = list(sig.parameters.keys())
    assert "Telepon" in params, "Missing parameter 'Telepon'"
    assert "Nama" in params, "Missing parameter 'Nama'"
    assert "Email" in params, "Missing parameter 'Email'"
    assert "Alamat" in params, "Missing parameter 'Alamat'"

def test_rentalmobil_has_Telepon():
    assert hasattr(RentalMobil, "Telepon")
    descriptor = None
    for klass in RentalMobil.__mro__:
        if "Telepon" in klass.__dict__:
            descriptor = klass.__dict__["Telepon"]
            break
    assert isinstance(descriptor, property)

def test_rentalmobil_has_Nama():
    assert hasattr(RentalMobil, "Nama")
    descriptor = None
    for klass in RentalMobil.__mro__:
        if "Nama" in klass.__dict__:
            descriptor = klass.__dict__["Nama"]
            break
    assert isinstance(descriptor, property)

def test_rentalmobil_has_Email():
    assert hasattr(RentalMobil, "Email")
    descriptor = None
    for klass in RentalMobil.__mro__:
        if "Email" in klass.__dict__:
            descriptor = klass.__dict__["Email"]
            break
    assert isinstance(descriptor, property)

def test_rentalmobil_has_Alamat():
    assert hasattr(RentalMobil, "Alamat")
    descriptor = None
    for klass in RentalMobil.__mro__:
        if "Alamat" in klass.__dict__:
            descriptor = klass.__dict__["Alamat"]
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
Kendaraan_strategy = st.builds(
    Kendaraan,
    NoRangka=
        safe_text,
    Merk=
        safe_text,
    Warna=
        safe_text,
    NoMesin=
        safe_text,
    TahunPembuatan=
        safe_text,
    NoPolisi=
        safe_text
)
Pesan_strategy = st.builds(
    Pesan,
    NoPesan=
        st.integers(),
    TanggalKembali=
        safe_text,
    TanggalRental=
        safe_text,
    IdPelanggan=
        st.integers()
)
Administrasi_strategy = st.builds(
    Administrasi,
    Kembali=
        safe_text,
    NoPesan=
        st.integers(),
    Bayar=
        safe_text,
    HargaSewa=
        safe_text,
    IdPelanggan=
        st.integers(),
    IdAdmin=
        st.integers()
)
Pelanggan_strategy = st.builds(
    Pelanggan,
    IdPelanggan=
        st.integers(),
    NoKTP=
        safe_text,
    Username=
        safe_text,
    Telepon=
        safe_text,
    Pekerjaan=
        safe_text,
    Alamat=
        safe_text,
    JenisKelamin=
        safe_text,
    Umur=
        st.integers(),
    Password=
        safe_text
)
Admin_strategy = st.builds(
    Admin,
    Password=
        safe_text,
    Username=
        safe_text
)
Pemilik_strategy = st.builds(
    Pemilik,
    Username=
        safe_text,
    Password=
        safe_text
)
Login_strategy = st.builds(
    Login,
    Username=
        safe_text,
    Password=
        safe_text
)
RentalMobil_strategy = st.builds(
    RentalMobil,
    Telepon=
        safe_text,
    Nama=
        safe_text,
    Email=
        safe_text,
    Alamat=
        safe_text
)

@given(instance=Kendaraan_strategy)
@settings(max_examples=50)
def test_kendaraan_instantiation(instance):
    assert isinstance(instance, Kendaraan)



@given(instance=Kendaraan_strategy)
def test_kendaraan_NoRangka_setter(instance):
    original = instance.NoRangka
    instance.NoRangka = original
    assert instance.NoRangka == original



@given(instance=Kendaraan_strategy)
def test_kendaraan_Merk_setter(instance):
    original = instance.Merk
    instance.Merk = original
    assert instance.Merk == original



@given(instance=Kendaraan_strategy)
def test_kendaraan_Warna_setter(instance):
    original = instance.Warna
    instance.Warna = original
    assert instance.Warna == original



@given(instance=Kendaraan_strategy)
def test_kendaraan_NoMesin_setter(instance):
    original = instance.NoMesin
    instance.NoMesin = original
    assert instance.NoMesin == original



@given(instance=Kendaraan_strategy)
def test_kendaraan_TahunPembuatan_setter(instance):
    original = instance.TahunPembuatan
    instance.TahunPembuatan = original
    assert instance.TahunPembuatan == original



@given(instance=Kendaraan_strategy)
def test_kendaraan_NoPolisi_setter(instance):
    original = instance.NoPolisi
    instance.NoPolisi = original
    assert instance.NoPolisi == original

@given(instance=Pesan_strategy)
@settings(max_examples=50)
def test_pesan_instantiation(instance):
    assert isinstance(instance, Pesan)



@given(instance=Pesan_strategy)
def test_pesan_NoPesan_setter(instance):
    original = instance.NoPesan
    instance.NoPesan = original
    assert instance.NoPesan == original



@given(instance=Pesan_strategy)
def test_pesan_TanggalKembali_setter(instance):
    original = instance.TanggalKembali
    instance.TanggalKembali = original
    assert instance.TanggalKembali == original



@given(instance=Pesan_strategy)
def test_pesan_TanggalRental_setter(instance):
    original = instance.TanggalRental
    instance.TanggalRental = original
    assert instance.TanggalRental == original



@given(instance=Pesan_strategy)
def test_pesan_IdPelanggan_setter(instance):
    original = instance.IdPelanggan
    instance.IdPelanggan = original
    assert instance.IdPelanggan == original

@given(instance=Administrasi_strategy)
@settings(max_examples=50)
def test_administrasi_instantiation(instance):
    assert isinstance(instance, Administrasi)



@given(instance=Administrasi_strategy)
def test_administrasi_Kembali_setter(instance):
    original = instance.Kembali
    instance.Kembali = original
    assert instance.Kembali == original



@given(instance=Administrasi_strategy)
def test_administrasi_NoPesan_setter(instance):
    original = instance.NoPesan
    instance.NoPesan = original
    assert instance.NoPesan == original



@given(instance=Administrasi_strategy)
def test_administrasi_Bayar_setter(instance):
    original = instance.Bayar
    instance.Bayar = original
    assert instance.Bayar == original



@given(instance=Administrasi_strategy)
def test_administrasi_HargaSewa_setter(instance):
    original = instance.HargaSewa
    instance.HargaSewa = original
    assert instance.HargaSewa == original



@given(instance=Administrasi_strategy)
def test_administrasi_IdPelanggan_setter(instance):
    original = instance.IdPelanggan
    instance.IdPelanggan = original
    assert instance.IdPelanggan == original



@given(instance=Administrasi_strategy)
def test_administrasi_IdAdmin_setter(instance):
    original = instance.IdAdmin
    instance.IdAdmin = original
    assert instance.IdAdmin == original

@given(instance=Pelanggan_strategy)
@settings(max_examples=50)
def test_pelanggan_instantiation(instance):
    assert isinstance(instance, Pelanggan)



@given(instance=Pelanggan_strategy)
def test_pelanggan_IdPelanggan_setter(instance):
    original = instance.IdPelanggan
    instance.IdPelanggan = original
    assert instance.IdPelanggan == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_NoKTP_setter(instance):
    original = instance.NoKTP
    instance.NoKTP = original
    assert instance.NoKTP == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_Telepon_setter(instance):
    original = instance.Telepon
    instance.Telepon = original
    assert instance.Telepon == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_Pekerjaan_setter(instance):
    original = instance.Pekerjaan
    instance.Pekerjaan = original
    assert instance.Pekerjaan == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_Alamat_setter(instance):
    original = instance.Alamat
    instance.Alamat = original
    assert instance.Alamat == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_JenisKelamin_setter(instance):
    original = instance.JenisKelamin
    instance.JenisKelamin = original
    assert instance.JenisKelamin == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_Umur_setter(instance):
    original = instance.Umur
    instance.Umur = original
    assert instance.Umur == original



@given(instance=Pelanggan_strategy)
def test_pelanggan_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original



@given(instance=Admin_strategy)
def test_admin_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original

@given(instance=Pemilik_strategy)
@settings(max_examples=50)
def test_pemilik_instantiation(instance):
    assert isinstance(instance, Pemilik)



@given(instance=Pemilik_strategy)
def test_pemilik_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Pemilik_strategy)
def test_pemilik_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_Username_setter(instance):
    original = instance.Username
    instance.Username = original
    assert instance.Username == original



@given(instance=Login_strategy)
def test_login_Password_setter(instance):
    original = instance.Password
    instance.Password = original
    assert instance.Password == original

@given(instance=RentalMobil_strategy)
@settings(max_examples=50)
def test_rentalmobil_instantiation(instance):
    assert isinstance(instance, RentalMobil)



@given(instance=RentalMobil_strategy)
def test_rentalmobil_Telepon_setter(instance):
    original = instance.Telepon
    instance.Telepon = original
    assert instance.Telepon == original



@given(instance=RentalMobil_strategy)
def test_rentalmobil_Nama_setter(instance):
    original = instance.Nama
    instance.Nama = original
    assert instance.Nama == original



@given(instance=RentalMobil_strategy)
def test_rentalmobil_Email_setter(instance):
    original = instance.Email
    instance.Email = original
    assert instance.Email == original



@given(instance=RentalMobil_strategy)
def test_rentalmobil_Alamat_setter(instance):
    original = instance.Alamat
    instance.Alamat = original
    assert instance.Alamat == original
