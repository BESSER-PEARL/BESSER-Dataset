import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    keluar,
    masuk,
    sistem,
    transaksi,
    supplier,
    pelanggan,
    user,
    barang,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_keluar_is_not_abstract():
    assert not inspect.isabstract(keluar)


def test_keluar_constructor_exists():
    assert callable(keluar.__init__)


def test_keluar_constructor_args():
    sig = inspect.signature(keluar.__init__)
    params = list(sig.parameters.keys())
    assert "pembeli" in params, "Missing parameter 'pembeli'"

def test_keluar_has_pembeli():
    assert hasattr(keluar, "pembeli")
    descriptor = None
    for klass in keluar.__mro__:
        if "pembeli" in klass.__dict__:
            descriptor = klass.__dict__["pembeli"]
            break
    assert isinstance(descriptor, property)



def test_masuk_is_not_abstract():
    assert not inspect.isabstract(masuk)


def test_masuk_constructor_exists():
    assert callable(masuk.__init__)


def test_masuk_constructor_args():
    sig = inspect.signature(masuk.__init__)
    params = list(sig.parameters.keys())
    assert "penyuplai" in params, "Missing parameter 'penyuplai'"

def test_masuk_has_penyuplai():
    assert hasattr(masuk, "penyuplai")
    descriptor = None
    for klass in masuk.__mro__:
        if "penyuplai" in klass.__dict__:
            descriptor = klass.__dict__["penyuplai"]
            break
    assert isinstance(descriptor, property)



def test_sistem_is_not_abstract():
    assert not inspect.isabstract(sistem)


def test_sistem_constructor_exists():
    assert callable(sistem.__init__)


def test_sistem_constructor_args():
    sig = inspect.signature(sistem.__init__)
    params = list(sig.parameters.keys())
    assert "supplier" in params, "Missing parameter 'supplier'"
    assert "barang" in params, "Missing parameter 'barang'"
    assert "user" in params, "Missing parameter 'user'"

def test_sistem_has_supplier():
    assert hasattr(sistem, "supplier")
    descriptor = None
    for klass in sistem.__mro__:
        if "supplier" in klass.__dict__:
            descriptor = klass.__dict__["supplier"]
            break
    assert isinstance(descriptor, property)

def test_sistem_has_barang():
    assert hasattr(sistem, "barang")
    descriptor = None
    for klass in sistem.__mro__:
        if "barang" in klass.__dict__:
            descriptor = klass.__dict__["barang"]
            break
    assert isinstance(descriptor, property)

def test_sistem_has_user():
    assert hasattr(sistem, "user")
    descriptor = None
    for klass in sistem.__mro__:
        if "user" in klass.__dict__:
            descriptor = klass.__dict__["user"]
            break
    assert isinstance(descriptor, property)



def test_transaksi_is_not_abstract():
    assert not inspect.isabstract(transaksi)


def test_transaksi_constructor_exists():
    assert callable(transaksi.__init__)


def test_transaksi_constructor_args():
    sig = inspect.signature(transaksi.__init__)
    params = list(sig.parameters.keys())
    assert "id_transaksi" in params, "Missing parameter 'id_transaksi'"
    assert "nama_barang" in params, "Missing parameter 'nama_barang'"
    assert "total" in params, "Missing parameter 'total'"
    assert "tanggal" in params, "Missing parameter 'tanggal'"

def test_transaksi_has_id_transaksi():
    assert hasattr(transaksi, "id_transaksi")
    descriptor = None
    for klass in transaksi.__mro__:
        if "id_transaksi" in klass.__dict__:
            descriptor = klass.__dict__["id_transaksi"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_has_nama_barang():
    assert hasattr(transaksi, "nama_barang")
    descriptor = None
    for klass in transaksi.__mro__:
        if "nama_barang" in klass.__dict__:
            descriptor = klass.__dict__["nama_barang"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_has_total():
    assert hasattr(transaksi, "total")
    descriptor = None
    for klass in transaksi.__mro__:
        if "total" in klass.__dict__:
            descriptor = klass.__dict__["total"]
            break
    assert isinstance(descriptor, property)

def test_transaksi_has_tanggal():
    assert hasattr(transaksi, "tanggal")
    descriptor = None
    for klass in transaksi.__mro__:
        if "tanggal" in klass.__dict__:
            descriptor = klass.__dict__["tanggal"]
            break
    assert isinstance(descriptor, property)



def test_supplier_is_not_abstract():
    assert not inspect.isabstract(supplier)


def test_supplier_constructor_exists():
    assert callable(supplier.__init__)


def test_supplier_constructor_args():
    sig = inspect.signature(supplier.__init__)
    params = list(sig.parameters.keys())
    assert "nama_supplier" in params, "Missing parameter 'nama_supplier'"
    assert "no_telp_supp" in params, "Missing parameter 'no_telp_supp'"
    assert "id_supplier" in params, "Missing parameter 'id_supplier'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "alamat" in params, "Missing parameter 'alamat'"

def test_supplier_has_nama_supplier():
    assert hasattr(supplier, "nama_supplier")
    descriptor = None
    for klass in supplier.__mro__:
        if "nama_supplier" in klass.__dict__:
            descriptor = klass.__dict__["nama_supplier"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_no_telp_supp():
    assert hasattr(supplier, "no_telp_supp")
    descriptor = None
    for klass in supplier.__mro__:
        if "no_telp_supp" in klass.__dict__:
            descriptor = klass.__dict__["no_telp_supp"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_id_supplier():
    assert hasattr(supplier, "id_supplier")
    descriptor = None
    for klass in supplier.__mro__:
        if "id_supplier" in klass.__dict__:
            descriptor = klass.__dict__["id_supplier"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_attribute():
    assert hasattr(supplier, "attribute")
    descriptor = None
    for klass in supplier.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_supplier_has_alamat():
    assert hasattr(supplier, "alamat")
    descriptor = None
    for klass in supplier.__mro__:
        if "alamat" in klass.__dict__:
            descriptor = klass.__dict__["alamat"]
            break
    assert isinstance(descriptor, property)



def test_pelanggan_is_not_abstract():
    assert not inspect.isabstract(pelanggan)


def test_pelanggan_constructor_exists():
    assert callable(pelanggan.__init__)


def test_pelanggan_constructor_args():
    sig = inspect.signature(pelanggan.__init__)
    params = list(sig.parameters.keys())
    assert "id_pelanggan" in params, "Missing parameter 'id_pelanggan'"
    assert "nama_pelanggan" in params, "Missing parameter 'nama_pelanggan'"
    assert "alamat" in params, "Missing parameter 'alamat'"
    assert "no_telp_pelanggan" in params, "Missing parameter 'no_telp_pelanggan'"

def test_pelanggan_has_id_pelanggan():
    assert hasattr(pelanggan, "id_pelanggan")
    descriptor = None
    for klass in pelanggan.__mro__:
        if "id_pelanggan" in klass.__dict__:
            descriptor = klass.__dict__["id_pelanggan"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_nama_pelanggan():
    assert hasattr(pelanggan, "nama_pelanggan")
    descriptor = None
    for klass in pelanggan.__mro__:
        if "nama_pelanggan" in klass.__dict__:
            descriptor = klass.__dict__["nama_pelanggan"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_alamat():
    assert hasattr(pelanggan, "alamat")
    descriptor = None
    for klass in pelanggan.__mro__:
        if "alamat" in klass.__dict__:
            descriptor = klass.__dict__["alamat"]
            break
    assert isinstance(descriptor, property)

def test_pelanggan_has_no_telp_pelanggan():
    assert hasattr(pelanggan, "no_telp_pelanggan")
    descriptor = None
    for klass in pelanggan.__mro__:
        if "no_telp_pelanggan" in klass.__dict__:
            descriptor = klass.__dict__["no_telp_pelanggan"]
            break
    assert isinstance(descriptor, property)



def test_user_is_not_abstract():
    assert not inspect.isabstract(user)


def test_user_constructor_exists():
    assert callable(user.__init__)


def test_user_constructor_args():
    sig = inspect.signature(user.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"
    assert "nama_user" in params, "Missing parameter 'nama_user'"
    assert "id_user" in params, "Missing parameter 'id_user'"

def test_user_has_password():
    assert hasattr(user, "password")
    descriptor = None
    for klass in user.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_user_has_username():
    assert hasattr(user, "username")
    descriptor = None
    for klass in user.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_user_has_nama_user():
    assert hasattr(user, "nama_user")
    descriptor = None
    for klass in user.__mro__:
        if "nama_user" in klass.__dict__:
            descriptor = klass.__dict__["nama_user"]
            break
    assert isinstance(descriptor, property)

def test_user_has_id_user():
    assert hasattr(user, "id_user")
    descriptor = None
    for klass in user.__mro__:
        if "id_user" in klass.__dict__:
            descriptor = klass.__dict__["id_user"]
            break
    assert isinstance(descriptor, property)



def test_barang_is_not_abstract():
    assert not inspect.isabstract(barang)


def test_barang_constructor_exists():
    assert callable(barang.__init__)


def test_barang_constructor_args():
    sig = inspect.signature(barang.__init__)
    params = list(sig.parameters.keys())
    assert "harga" in params, "Missing parameter 'harga'"
    assert "kategori" in params, "Missing parameter 'kategori'"
    assert "id_barang" in params, "Missing parameter 'id_barang'"
    assert "stok" in params, "Missing parameter 'stok'"
    assert "nama_barang" in params, "Missing parameter 'nama_barang'"
    assert "satuan" in params, "Missing parameter 'satuan'"

def test_barang_has_harga():
    assert hasattr(barang, "harga")
    descriptor = None
    for klass in barang.__mro__:
        if "harga" in klass.__dict__:
            descriptor = klass.__dict__["harga"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_kategori():
    assert hasattr(barang, "kategori")
    descriptor = None
    for klass in barang.__mro__:
        if "kategori" in klass.__dict__:
            descriptor = klass.__dict__["kategori"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_id_barang():
    assert hasattr(barang, "id_barang")
    descriptor = None
    for klass in barang.__mro__:
        if "id_barang" in klass.__dict__:
            descriptor = klass.__dict__["id_barang"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_stok():
    assert hasattr(barang, "stok")
    descriptor = None
    for klass in barang.__mro__:
        if "stok" in klass.__dict__:
            descriptor = klass.__dict__["stok"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_nama_barang():
    assert hasattr(barang, "nama_barang")
    descriptor = None
    for klass in barang.__mro__:
        if "nama_barang" in klass.__dict__:
            descriptor = klass.__dict__["nama_barang"]
            break
    assert isinstance(descriptor, property)

def test_barang_has_satuan():
    assert hasattr(barang, "satuan")
    descriptor = None
    for klass in barang.__mro__:
        if "satuan" in klass.__dict__:
            descriptor = klass.__dict__["satuan"]
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
keluar_strategy = st.builds(
    keluar,
    pembeli=
        st.none()
)
masuk_strategy = st.builds(
    masuk,
    penyuplai=
        st.none()
)
sistem_strategy = st.builds(
    sistem,
    supplier=
        st.none(),
    barang=
        st.none(),
    user=
        safe_text
)
transaksi_strategy = st.builds(
    transaksi,
    id_transaksi=
        st.integers(),
    nama_barang=
        st.none(),
    total=
        st.integers(),
    tanggal=
        safe_text
)
supplier_strategy = st.builds(
    supplier,
    nama_supplier=
        st.none(),
    no_telp_supp=
        safe_text,
    id_supplier=
        st.integers(),
    attribute=
        safe_text,
    alamat=
        safe_text
)
pelanggan_strategy = st.builds(
    pelanggan,
    id_pelanggan=
        st.integers(),
    nama_pelanggan=
        st.none(),
    alamat=
        safe_text,
    no_telp_pelanggan=
        safe_text
)
user_strategy = st.builds(
    user,
    password=
        safe_text,
    username=
        safe_text,
    nama_user=
        safe_text,
    id_user=
        st.integers()
)
barang_strategy = st.builds(
    barang,
    harga=
        st.integers(),
    kategori=
        safe_text,
    id_barang=
        safe_text,
    stok=
        st.integers(),
    nama_barang=
        st.none(),
    satuan=
        safe_text
)

@given(instance=keluar_strategy)
@settings(max_examples=50)
def test_keluar_instantiation(instance):
    assert isinstance(instance, keluar)



@given(instance=keluar_strategy)
def test_keluar_pembeli_setter(instance):
    original = instance.pembeli
    instance.pembeli = original
    assert instance.pembeli == original

@given(instance=masuk_strategy)
@settings(max_examples=50)
def test_masuk_instantiation(instance):
    assert isinstance(instance, masuk)



@given(instance=masuk_strategy)
def test_masuk_penyuplai_setter(instance):
    original = instance.penyuplai
    instance.penyuplai = original
    assert instance.penyuplai == original

@given(instance=sistem_strategy)
@settings(max_examples=50)
def test_sistem_instantiation(instance):
    assert isinstance(instance, sistem)



@given(instance=sistem_strategy)
def test_sistem_supplier_setter(instance):
    original = instance.supplier
    instance.supplier = original
    assert instance.supplier == original



@given(instance=sistem_strategy)
def test_sistem_barang_setter(instance):
    original = instance.barang
    instance.barang = original
    assert instance.barang == original



@given(instance=sistem_strategy)
def test_sistem_user_setter(instance):
    original = instance.user
    instance.user = original
    assert instance.user == original

@given(instance=transaksi_strategy)
@settings(max_examples=50)
def test_transaksi_instantiation(instance):
    assert isinstance(instance, transaksi)



@given(instance=transaksi_strategy)
def test_transaksi_id_transaksi_setter(instance):
    original = instance.id_transaksi
    instance.id_transaksi = original
    assert instance.id_transaksi == original



@given(instance=transaksi_strategy)
def test_transaksi_nama_barang_setter(instance):
    original = instance.nama_barang
    instance.nama_barang = original
    assert instance.nama_barang == original



@given(instance=transaksi_strategy)
def test_transaksi_total_setter(instance):
    original = instance.total
    instance.total = original
    assert instance.total == original



@given(instance=transaksi_strategy)
def test_transaksi_tanggal_setter(instance):
    original = instance.tanggal
    instance.tanggal = original
    assert instance.tanggal == original

@given(instance=supplier_strategy)
@settings(max_examples=50)
def test_supplier_instantiation(instance):
    assert isinstance(instance, supplier)



@given(instance=supplier_strategy)
def test_supplier_nama_supplier_setter(instance):
    original = instance.nama_supplier
    instance.nama_supplier = original
    assert instance.nama_supplier == original



@given(instance=supplier_strategy)
def test_supplier_no_telp_supp_setter(instance):
    original = instance.no_telp_supp
    instance.no_telp_supp = original
    assert instance.no_telp_supp == original



@given(instance=supplier_strategy)
def test_supplier_id_supplier_setter(instance):
    original = instance.id_supplier
    instance.id_supplier = original
    assert instance.id_supplier == original



@given(instance=supplier_strategy)
def test_supplier_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=supplier_strategy)
def test_supplier_alamat_setter(instance):
    original = instance.alamat
    instance.alamat = original
    assert instance.alamat == original

@given(instance=pelanggan_strategy)
@settings(max_examples=50)
def test_pelanggan_instantiation(instance):
    assert isinstance(instance, pelanggan)



@given(instance=pelanggan_strategy)
def test_pelanggan_id_pelanggan_setter(instance):
    original = instance.id_pelanggan
    instance.id_pelanggan = original
    assert instance.id_pelanggan == original



@given(instance=pelanggan_strategy)
def test_pelanggan_nama_pelanggan_setter(instance):
    original = instance.nama_pelanggan
    instance.nama_pelanggan = original
    assert instance.nama_pelanggan == original



@given(instance=pelanggan_strategy)
def test_pelanggan_alamat_setter(instance):
    original = instance.alamat
    instance.alamat = original
    assert instance.alamat == original



@given(instance=pelanggan_strategy)
def test_pelanggan_no_telp_pelanggan_setter(instance):
    original = instance.no_telp_pelanggan
    instance.no_telp_pelanggan = original
    assert instance.no_telp_pelanggan == original

@given(instance=user_strategy)
@settings(max_examples=50)
def test_user_instantiation(instance):
    assert isinstance(instance, user)



@given(instance=user_strategy)
def test_user_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=user_strategy)
def test_user_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=user_strategy)
def test_user_nama_user_setter(instance):
    original = instance.nama_user
    instance.nama_user = original
    assert instance.nama_user == original



@given(instance=user_strategy)
def test_user_id_user_setter(instance):
    original = instance.id_user
    instance.id_user = original
    assert instance.id_user == original

@given(instance=barang_strategy)
@settings(max_examples=50)
def test_barang_instantiation(instance):
    assert isinstance(instance, barang)



@given(instance=barang_strategy)
def test_barang_harga_setter(instance):
    original = instance.harga
    instance.harga = original
    assert instance.harga == original



@given(instance=barang_strategy)
def test_barang_kategori_setter(instance):
    original = instance.kategori
    instance.kategori = original
    assert instance.kategori == original



@given(instance=barang_strategy)
def test_barang_id_barang_setter(instance):
    original = instance.id_barang
    instance.id_barang = original
    assert instance.id_barang == original



@given(instance=barang_strategy)
def test_barang_stok_setter(instance):
    original = instance.stok
    instance.stok = original
    assert instance.stok == original



@given(instance=barang_strategy)
def test_barang_nama_barang_setter(instance):
    original = instance.nama_barang
    instance.nama_barang = original
    assert instance.nama_barang == original



@given(instance=barang_strategy)
def test_barang_satuan_setter(instance):
    original = instance.satuan
    instance.satuan = original
    assert instance.satuan == original
