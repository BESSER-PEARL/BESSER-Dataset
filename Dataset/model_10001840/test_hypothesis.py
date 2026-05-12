import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Denda,
    Pembayaran,
    ReservasiKamar,
    Kamar,
    hjb_Interface,
    Admin,
    Pemesan,
    Register_UseCase,
    Login_UseCase,
    Kamar_Standard_UseCase,
    Kamar_Keluarga_UseCase,
    Kamar_Deluxe_UseCase,
    Denda_UseCase,
    Check_Out_UseCase,
    Check_in_UseCase,
    Cancel_Pemesanan_UseCase,
    Melakukan_pembayaran_UseCase,
    Kirim_e_booking_email_UseCase,
    Mengirim_e_bukti_Bayar_UseCase,
    Melakukan_reservasi_kamar_UseCase,
    Admin_Actor,
    Pemesan_Actor,
    Melihat_Katalog_Kamar_UseCase,
    Pengunjung_Actor,
    Enumeration,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_denda_is_not_abstract():
    assert not inspect.isabstract(Denda)


def test_denda_constructor_exists():
    assert callable(Denda.__init__)


def test_denda_constructor_args():
    sig = inspect.signature(Denda.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Denda" in params, "Missing parameter 'ID_Denda'"
    assert "keterangan" in params, "Missing parameter 'keterangan'"
    assert "ID_Reservasi" in params, "Missing parameter 'ID_Reservasi'"
    assert "jumlah" in params, "Missing parameter 'jumlah'"

def test_denda_has_ID_Denda():
    assert hasattr(Denda, "ID_Denda")
    descriptor = None
    for klass in Denda.__mro__:
        if "ID_Denda" in klass.__dict__:
            descriptor = klass.__dict__["ID_Denda"]
            break
    assert isinstance(descriptor, property)

def test_denda_has_keterangan():
    assert hasattr(Denda, "keterangan")
    descriptor = None
    for klass in Denda.__mro__:
        if "keterangan" in klass.__dict__:
            descriptor = klass.__dict__["keterangan"]
            break
    assert isinstance(descriptor, property)

def test_denda_has_ID_Reservasi():
    assert hasattr(Denda, "ID_Reservasi")
    descriptor = None
    for klass in Denda.__mro__:
        if "ID_Reservasi" in klass.__dict__:
            descriptor = klass.__dict__["ID_Reservasi"]
            break
    assert isinstance(descriptor, property)

def test_denda_has_jumlah():
    assert hasattr(Denda, "jumlah")
    descriptor = None
    for klass in Denda.__mro__:
        if "jumlah" in klass.__dict__:
            descriptor = klass.__dict__["jumlah"]
            break
    assert isinstance(descriptor, property)



def test_pembayaran_is_not_abstract():
    assert not inspect.isabstract(Pembayaran)


def test_pembayaran_constructor_exists():
    assert callable(Pembayaran.__init__)


def test_pembayaran_constructor_args():
    sig = inspect.signature(Pembayaran.__init__)
    params = list(sig.parameters.keys())
    assert "ID_Pembayaran" in params, "Missing parameter 'ID_Pembayaran'"
    assert "jumlah" in params, "Missing parameter 'jumlah'"
    assert "deadline_bayar" in params, "Missing parameter 'deadline_bayar'"
    assert "status" in params, "Missing parameter 'status'"
    assert "ID_Reservasi" in params, "Missing parameter 'ID_Reservasi'"

def test_pembayaran_has_ID_Pembayaran():
    assert hasattr(Pembayaran, "ID_Pembayaran")
    descriptor = None
    for klass in Pembayaran.__mro__:
        if "ID_Pembayaran" in klass.__dict__:
            descriptor = klass.__dict__["ID_Pembayaran"]
            break
    assert isinstance(descriptor, property)

def test_pembayaran_has_jumlah():
    assert hasattr(Pembayaran, "jumlah")
    descriptor = None
    for klass in Pembayaran.__mro__:
        if "jumlah" in klass.__dict__:
            descriptor = klass.__dict__["jumlah"]
            break
    assert isinstance(descriptor, property)

def test_pembayaran_has_deadline_bayar():
    assert hasattr(Pembayaran, "deadline_bayar")
    descriptor = None
    for klass in Pembayaran.__mro__:
        if "deadline_bayar" in klass.__dict__:
            descriptor = klass.__dict__["deadline_bayar"]
            break
    assert isinstance(descriptor, property)

def test_pembayaran_has_status():
    assert hasattr(Pembayaran, "status")
    descriptor = None
    for klass in Pembayaran.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_pembayaran_has_ID_Reservasi():
    assert hasattr(Pembayaran, "ID_Reservasi")
    descriptor = None
    for klass in Pembayaran.__mro__:
        if "ID_Reservasi" in klass.__dict__:
            descriptor = klass.__dict__["ID_Reservasi"]
            break
    assert isinstance(descriptor, property)



def test_reservasikamar_is_not_abstract():
    assert not inspect.isabstract(ReservasiKamar)


def test_reservasikamar_constructor_exists():
    assert callable(ReservasiKamar.__init__)


def test_reservasikamar_constructor_args():
    sig = inspect.signature(ReservasiKamar.__init__)
    params = list(sig.parameters.keys())
    assert "NIK" in params, "Missing parameter 'NIK'"
    assert "ID_pembayaran" in params, "Missing parameter 'ID_pembayaran'"
    assert "ID_admin" in params, "Missing parameter 'ID_admin'"
    assert "ID_Reservasi" in params, "Missing parameter 'ID_Reservasi'"
    assert "no_kamar" in params, "Missing parameter 'no_kamar'"
    assert "tgl_start_booking" in params, "Missing parameter 'tgl_start_booking'"
    assert "tgl_end_booking" in params, "Missing parameter 'tgl_end_booking'"

def test_reservasikamar_has_NIK():
    assert hasattr(ReservasiKamar, "NIK")
    descriptor = None
    for klass in ReservasiKamar.__mro__:
        if "NIK" in klass.__dict__:
            descriptor = klass.__dict__["NIK"]
            break
    assert isinstance(descriptor, property)

def test_reservasikamar_has_ID_pembayaran():
    assert hasattr(ReservasiKamar, "ID_pembayaran")
    descriptor = None
    for klass in ReservasiKamar.__mro__:
        if "ID_pembayaran" in klass.__dict__:
            descriptor = klass.__dict__["ID_pembayaran"]
            break
    assert isinstance(descriptor, property)

def test_reservasikamar_has_ID_admin():
    assert hasattr(ReservasiKamar, "ID_admin")
    descriptor = None
    for klass in ReservasiKamar.__mro__:
        if "ID_admin" in klass.__dict__:
            descriptor = klass.__dict__["ID_admin"]
            break
    assert isinstance(descriptor, property)

def test_reservasikamar_has_ID_Reservasi():
    assert hasattr(ReservasiKamar, "ID_Reservasi")
    descriptor = None
    for klass in ReservasiKamar.__mro__:
        if "ID_Reservasi" in klass.__dict__:
            descriptor = klass.__dict__["ID_Reservasi"]
            break
    assert isinstance(descriptor, property)

def test_reservasikamar_has_no_kamar():
    assert hasattr(ReservasiKamar, "no_kamar")
    descriptor = None
    for klass in ReservasiKamar.__mro__:
        if "no_kamar" in klass.__dict__:
            descriptor = klass.__dict__["no_kamar"]
            break
    assert isinstance(descriptor, property)

def test_reservasikamar_has_tgl_start_booking():
    assert hasattr(ReservasiKamar, "tgl_start_booking")
    descriptor = None
    for klass in ReservasiKamar.__mro__:
        if "tgl_start_booking" in klass.__dict__:
            descriptor = klass.__dict__["tgl_start_booking"]
            break
    assert isinstance(descriptor, property)

def test_reservasikamar_has_tgl_end_booking():
    assert hasattr(ReservasiKamar, "tgl_end_booking")
    descriptor = None
    for klass in ReservasiKamar.__mro__:
        if "tgl_end_booking" in klass.__dict__:
            descriptor = klass.__dict__["tgl_end_booking"]
            break
    assert isinstance(descriptor, property)



def test_kamar_is_not_abstract():
    assert not inspect.isabstract(Kamar)


def test_kamar_constructor_exists():
    assert callable(Kamar.__init__)


def test_kamar_constructor_args():
    sig = inspect.signature(Kamar.__init__)
    params = list(sig.parameters.keys())
    assert "_attr" in params, "Missing parameter '_attr'"
    assert "status" in params, "Missing parameter 'status'"
    assert "jumlah_bed" in params, "Missing parameter 'jumlah_bed'"
    assert "no_kamar" in params, "Missing parameter 'no_kamar'"
    assert "tipe" in params, "Missing parameter 'tipe'"

def test_kamar_has__attr():
    assert hasattr(Kamar, "_attr")
    descriptor = None
    for klass in Kamar.__mro__:
        if "_attr" in klass.__dict__:
            descriptor = klass.__dict__["_attr"]
            break
    assert isinstance(descriptor, property)

def test_kamar_has_status():
    assert hasattr(Kamar, "status")
    descriptor = None
    for klass in Kamar.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_kamar_has_jumlah_bed():
    assert hasattr(Kamar, "jumlah_bed")
    descriptor = None
    for klass in Kamar.__mro__:
        if "jumlah_bed" in klass.__dict__:
            descriptor = klass.__dict__["jumlah_bed"]
            break
    assert isinstance(descriptor, property)

def test_kamar_has_no_kamar():
    assert hasattr(Kamar, "no_kamar")
    descriptor = None
    for klass in Kamar.__mro__:
        if "no_kamar" in klass.__dict__:
            descriptor = klass.__dict__["no_kamar"]
            break
    assert isinstance(descriptor, property)

def test_kamar_has_tipe():
    assert hasattr(Kamar, "tipe")
    descriptor = None
    for klass in Kamar.__mro__:
        if "tipe" in klass.__dict__:
            descriptor = klass.__dict__["tipe"]
            break
    assert isinstance(descriptor, property)



def test_hjb_interface_is_not_abstract():
    assert not inspect.isabstract(hjb_Interface)


def test_hjb_interface_constructor_exists():
    assert callable(hjb_Interface.__init__)


def test_hjb_interface_constructor_args():
    sig = inspect.signature(hjb_Interface.__init__)
    params = list(sig.parameters.keys())



def test_admin_is_not_abstract():
    assert not inspect.isabstract(Admin)


def test_admin_constructor_exists():
    assert callable(Admin.__init__)


def test_admin_constructor_args():
    sig = inspect.signature(Admin.__init__)
    params = list(sig.parameters.keys())
    assert "username" in params, "Missing parameter 'username'"
    assert "attribute" in params, "Missing parameter 'attribute'"
    assert "insertData" in params, "Missing parameter 'insertData'"
    assert "password" in params, "Missing parameter 'password'"
    assert "ID_admin" in params, "Missing parameter 'ID_admin'"

def test_admin_has_username():
    assert hasattr(Admin, "username")
    descriptor = None
    for klass in Admin.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_attribute():
    assert hasattr(Admin, "attribute")
    descriptor = None
    for klass in Admin.__mro__:
        if "attribute" in klass.__dict__:
            descriptor = klass.__dict__["attribute"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_insertData():
    assert hasattr(Admin, "insertData")
    descriptor = None
    for klass in Admin.__mro__:
        if "insertData" in klass.__dict__:
            descriptor = klass.__dict__["insertData"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_password():
    assert hasattr(Admin, "password")
    descriptor = None
    for klass in Admin.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_admin_has_ID_admin():
    assert hasattr(Admin, "ID_admin")
    descriptor = None
    for klass in Admin.__mro__:
        if "ID_admin" in klass.__dict__:
            descriptor = klass.__dict__["ID_admin"]
            break
    assert isinstance(descriptor, property)



def test_pemesan_is_not_abstract():
    assert not inspect.isabstract(Pemesan)


def test_pemesan_constructor_exists():
    assert callable(Pemesan.__init__)


def test_pemesan_constructor_args():
    sig = inspect.signature(Pemesan.__init__)
    params = list(sig.parameters.keys())
    assert "Emai" in params, "Missing parameter 'Emai'"
    assert "Alamat" in params, "Missing parameter 'Alamat'"
    assert "Nama" in params, "Missing parameter 'Nama'"
    assert "username" in params, "Missing parameter 'username'"
    assert "password" in params, "Missing parameter 'password'"
    assert "NIK" in params, "Missing parameter 'NIK'"
    assert "phone_number" in params, "Missing parameter 'phone_number'"

def test_pemesan_has_Emai():
    assert hasattr(Pemesan, "Emai")
    descriptor = None
    for klass in Pemesan.__mro__:
        if "Emai" in klass.__dict__:
            descriptor = klass.__dict__["Emai"]
            break
    assert isinstance(descriptor, property)

def test_pemesan_has_Alamat():
    assert hasattr(Pemesan, "Alamat")
    descriptor = None
    for klass in Pemesan.__mro__:
        if "Alamat" in klass.__dict__:
            descriptor = klass.__dict__["Alamat"]
            break
    assert isinstance(descriptor, property)

def test_pemesan_has_Nama():
    assert hasattr(Pemesan, "Nama")
    descriptor = None
    for klass in Pemesan.__mro__:
        if "Nama" in klass.__dict__:
            descriptor = klass.__dict__["Nama"]
            break
    assert isinstance(descriptor, property)

def test_pemesan_has_username():
    assert hasattr(Pemesan, "username")
    descriptor = None
    for klass in Pemesan.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)

def test_pemesan_has_password():
    assert hasattr(Pemesan, "password")
    descriptor = None
    for klass in Pemesan.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_pemesan_has_NIK():
    assert hasattr(Pemesan, "NIK")
    descriptor = None
    for klass in Pemesan.__mro__:
        if "NIK" in klass.__dict__:
            descriptor = klass.__dict__["NIK"]
            break
    assert isinstance(descriptor, property)

def test_pemesan_has_phone_number():
    assert hasattr(Pemesan, "phone_number")
    descriptor = None
    for klass in Pemesan.__mro__:
        if "phone_number" in klass.__dict__:
            descriptor = klass.__dict__["phone_number"]
            break
    assert isinstance(descriptor, property)



def test_register_usecase_is_not_abstract():
    assert not inspect.isabstract(Register_UseCase)


def test_register_usecase_constructor_exists():
    assert callable(Register_UseCase.__init__)


def test_register_usecase_constructor_args():
    sig = inspect.signature(Register_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Login_UseCase)


def test_login_usecase_constructor_exists():
    assert callable(Login_UseCase.__init__)


def test_login_usecase_constructor_args():
    sig = inspect.signature(Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_kamar_standard_usecase_is_not_abstract():
    assert not inspect.isabstract(Kamar_Standard_UseCase)


def test_kamar_standard_usecase_constructor_exists():
    assert callable(Kamar_Standard_UseCase.__init__)


def test_kamar_standard_usecase_constructor_args():
    sig = inspect.signature(Kamar_Standard_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_kamar_keluarga_usecase_is_not_abstract():
    assert not inspect.isabstract(Kamar_Keluarga_UseCase)


def test_kamar_keluarga_usecase_constructor_exists():
    assert callable(Kamar_Keluarga_UseCase.__init__)


def test_kamar_keluarga_usecase_constructor_args():
    sig = inspect.signature(Kamar_Keluarga_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_kamar_deluxe_usecase_is_not_abstract():
    assert not inspect.isabstract(Kamar_Deluxe_UseCase)


def test_kamar_deluxe_usecase_constructor_exists():
    assert callable(Kamar_Deluxe_UseCase.__init__)


def test_kamar_deluxe_usecase_constructor_args():
    sig = inspect.signature(Kamar_Deluxe_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_denda_usecase_is_not_abstract():
    assert not inspect.isabstract(Denda_UseCase)


def test_denda_usecase_constructor_exists():
    assert callable(Denda_UseCase.__init__)


def test_denda_usecase_constructor_args():
    sig = inspect.signature(Denda_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_out_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_Out_UseCase)


def test_check_out_usecase_constructor_exists():
    assert callable(Check_Out_UseCase.__init__)


def test_check_out_usecase_constructor_args():
    sig = inspect.signature(Check_Out_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_check_in_usecase_is_not_abstract():
    assert not inspect.isabstract(Check_in_UseCase)


def test_check_in_usecase_constructor_exists():
    assert callable(Check_in_UseCase.__init__)


def test_check_in_usecase_constructor_args():
    sig = inspect.signature(Check_in_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_cancel_pemesanan_usecase_is_not_abstract():
    assert not inspect.isabstract(Cancel_Pemesanan_UseCase)


def test_cancel_pemesanan_usecase_constructor_exists():
    assert callable(Cancel_Pemesanan_UseCase.__init__)


def test_cancel_pemesanan_usecase_constructor_args():
    sig = inspect.signature(Cancel_Pemesanan_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_melakukan_pembayaran_usecase_is_not_abstract():
    assert not inspect.isabstract(Melakukan_pembayaran_UseCase)


def test_melakukan_pembayaran_usecase_constructor_exists():
    assert callable(Melakukan_pembayaran_UseCase.__init__)


def test_melakukan_pembayaran_usecase_constructor_args():
    sig = inspect.signature(Melakukan_pembayaran_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_kirim_e_booking_email_usecase_is_not_abstract():
    assert not inspect.isabstract(Kirim_e_booking_email_UseCase)


def test_kirim_e_booking_email_usecase_constructor_exists():
    assert callable(Kirim_e_booking_email_UseCase.__init__)


def test_kirim_e_booking_email_usecase_constructor_args():
    sig = inspect.signature(Kirim_e_booking_email_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_mengirim_e_bukti_bayar_usecase_is_not_abstract():
    assert not inspect.isabstract(Mengirim_e_bukti_Bayar_UseCase)


def test_mengirim_e_bukti_bayar_usecase_constructor_exists():
    assert callable(Mengirim_e_bukti_Bayar_UseCase.__init__)


def test_mengirim_e_bukti_bayar_usecase_constructor_args():
    sig = inspect.signature(Mengirim_e_bukti_Bayar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_melakukan_reservasi_kamar_usecase_is_not_abstract():
    assert not inspect.isabstract(Melakukan_reservasi_kamar_UseCase)


def test_melakukan_reservasi_kamar_usecase_constructor_exists():
    assert callable(Melakukan_reservasi_kamar_UseCase.__init__)


def test_melakukan_reservasi_kamar_usecase_constructor_args():
    sig = inspect.signature(Melakukan_reservasi_kamar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_admin_actor_is_not_abstract():
    assert not inspect.isabstract(Admin_Actor)


def test_admin_actor_constructor_exists():
    assert callable(Admin_Actor.__init__)


def test_admin_actor_constructor_args():
    sig = inspect.signature(Admin_Actor.__init__)
    params = list(sig.parameters.keys())



def test_pemesan_actor_is_not_abstract():
    assert not inspect.isabstract(Pemesan_Actor)


def test_pemesan_actor_constructor_exists():
    assert callable(Pemesan_Actor.__init__)


def test_pemesan_actor_constructor_args():
    sig = inspect.signature(Pemesan_Actor.__init__)
    params = list(sig.parameters.keys())



def test_melihat_katalog_kamar_usecase_is_not_abstract():
    assert not inspect.isabstract(Melihat_Katalog_Kamar_UseCase)


def test_melihat_katalog_kamar_usecase_constructor_exists():
    assert callable(Melihat_Katalog_Kamar_UseCase.__init__)


def test_melihat_katalog_kamar_usecase_constructor_args():
    sig = inspect.signature(Melihat_Katalog_Kamar_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_pengunjung_actor_is_not_abstract():
    assert not inspect.isabstract(Pengunjung_Actor)


def test_pengunjung_actor_constructor_exists():
    assert callable(Pengunjung_Actor.__init__)


def test_pengunjung_actor_constructor_args():
    sig = inspect.signature(Pengunjung_Actor.__init__)
    params = list(sig.parameters.keys())

def test_enumeration_exists():
    # Check that the Enumeration exists
    assert Enumeration is not None

def test_enumeration_has_all_literals():
    # Collect the names of literals in this Enumeration
    enum_literals = [lit.name for lit in Enumeration]
    expected_literals = [
    ]
    # Check that all expected literals exist
    for lit_name in expected_literals:
        assert lit_name in enum_literals, f"Literal '' missing in Enumeration"


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
Denda_strategy = st.builds(
    Denda,
    ID_Denda=
        st.integers(),
    keterangan=
        safe_text,
    ID_Reservasi=
        st.integers(),
    jumlah=
        st.integers()
)
Pembayaran_strategy = st.builds(
    Pembayaran,
    ID_Pembayaran=
        st.integers(),
    jumlah=
        st.integers(),
    deadline_bayar=
        safe_text,
    status=
        safe_text,
    ID_Reservasi=
        st.integers()
)
ReservasiKamar_strategy = st.builds(
    ReservasiKamar,
    NIK=
        st.integers(),
    ID_pembayaran=
        st.integers(),
    ID_admin=
        st.integers(),
    ID_Reservasi=
        st.integers(),
    no_kamar=
        st.integers(),
    tgl_start_booking=
        safe_text,
    tgl_end_booking=
        safe_text
)
Kamar_strategy = st.builds(
    Kamar,
    _attr=
        safe_text,
    status=
        safe_text,
    jumlah_bed=
        st.integers(),
    no_kamar=
        st.integers(),
    tipe=
        safe_text
)
hjb_Interface_strategy = st.builds(
    hjb_Interface,
)
Admin_strategy = st.builds(
    Admin,
    username=
        safe_text,
    attribute=
        safe_text,
    insertData=
        safe_text,
    password=
        safe_text,
    ID_admin=
        st.integers()
)
Pemesan_strategy = st.builds(
    Pemesan,
    Emai=
        safe_text,
    Alamat=
        safe_text,
    Nama=
        safe_text,
    username=
        safe_text,
    password=
        safe_text,
    NIK=
        st.integers(),
    phone_number=
        safe_text
)
Register_UseCase_strategy = st.builds(
    Register_UseCase,
)
Login_UseCase_strategy = st.builds(
    Login_UseCase,
)
Kamar_Standard_UseCase_strategy = st.builds(
    Kamar_Standard_UseCase,
)
Kamar_Keluarga_UseCase_strategy = st.builds(
    Kamar_Keluarga_UseCase,
)
Kamar_Deluxe_UseCase_strategy = st.builds(
    Kamar_Deluxe_UseCase,
)
Denda_UseCase_strategy = st.builds(
    Denda_UseCase,
)
Check_Out_UseCase_strategy = st.builds(
    Check_Out_UseCase,
)
Check_in_UseCase_strategy = st.builds(
    Check_in_UseCase,
)
Cancel_Pemesanan_UseCase_strategy = st.builds(
    Cancel_Pemesanan_UseCase,
)
Melakukan_pembayaran_UseCase_strategy = st.builds(
    Melakukan_pembayaran_UseCase,
)
Kirim_e_booking_email_UseCase_strategy = st.builds(
    Kirim_e_booking_email_UseCase,
)
Mengirim_e_bukti_Bayar_UseCase_strategy = st.builds(
    Mengirim_e_bukti_Bayar_UseCase,
)
Melakukan_reservasi_kamar_UseCase_strategy = st.builds(
    Melakukan_reservasi_kamar_UseCase,
)
Admin_Actor_strategy = st.builds(
    Admin_Actor,
)
Pemesan_Actor_strategy = st.builds(
    Pemesan_Actor,
)
Melihat_Katalog_Kamar_UseCase_strategy = st.builds(
    Melihat_Katalog_Kamar_UseCase,
)
Pengunjung_Actor_strategy = st.builds(
    Pengunjung_Actor,
)

@given(instance=Denda_strategy)
@settings(max_examples=50)
def test_denda_instantiation(instance):
    assert isinstance(instance, Denda)



@given(instance=Denda_strategy)
def test_denda_ID_Denda_setter(instance):
    original = instance.ID_Denda
    instance.ID_Denda = original
    assert instance.ID_Denda == original



@given(instance=Denda_strategy)
def test_denda_keterangan_setter(instance):
    original = instance.keterangan
    instance.keterangan = original
    assert instance.keterangan == original



@given(instance=Denda_strategy)
def test_denda_ID_Reservasi_setter(instance):
    original = instance.ID_Reservasi
    instance.ID_Reservasi = original
    assert instance.ID_Reservasi == original



@given(instance=Denda_strategy)
def test_denda_jumlah_setter(instance):
    original = instance.jumlah
    instance.jumlah = original
    assert instance.jumlah == original

@given(instance=Pembayaran_strategy)
@settings(max_examples=50)
def test_pembayaran_instantiation(instance):
    assert isinstance(instance, Pembayaran)



@given(instance=Pembayaran_strategy)
def test_pembayaran_ID_Pembayaran_setter(instance):
    original = instance.ID_Pembayaran
    instance.ID_Pembayaran = original
    assert instance.ID_Pembayaran == original



@given(instance=Pembayaran_strategy)
def test_pembayaran_jumlah_setter(instance):
    original = instance.jumlah
    instance.jumlah = original
    assert instance.jumlah == original



@given(instance=Pembayaran_strategy)
def test_pembayaran_deadline_bayar_setter(instance):
    original = instance.deadline_bayar
    instance.deadline_bayar = original
    assert instance.deadline_bayar == original



@given(instance=Pembayaran_strategy)
def test_pembayaran_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Pembayaran_strategy)
def test_pembayaran_ID_Reservasi_setter(instance):
    original = instance.ID_Reservasi
    instance.ID_Reservasi = original
    assert instance.ID_Reservasi == original

@given(instance=ReservasiKamar_strategy)
@settings(max_examples=50)
def test_reservasikamar_instantiation(instance):
    assert isinstance(instance, ReservasiKamar)



@given(instance=ReservasiKamar_strategy)
def test_reservasikamar_NIK_setter(instance):
    original = instance.NIK
    instance.NIK = original
    assert instance.NIK == original



@given(instance=ReservasiKamar_strategy)
def test_reservasikamar_ID_pembayaran_setter(instance):
    original = instance.ID_pembayaran
    instance.ID_pembayaran = original
    assert instance.ID_pembayaran == original



@given(instance=ReservasiKamar_strategy)
def test_reservasikamar_ID_admin_setter(instance):
    original = instance.ID_admin
    instance.ID_admin = original
    assert instance.ID_admin == original



@given(instance=ReservasiKamar_strategy)
def test_reservasikamar_ID_Reservasi_setter(instance):
    original = instance.ID_Reservasi
    instance.ID_Reservasi = original
    assert instance.ID_Reservasi == original



@given(instance=ReservasiKamar_strategy)
def test_reservasikamar_no_kamar_setter(instance):
    original = instance.no_kamar
    instance.no_kamar = original
    assert instance.no_kamar == original



@given(instance=ReservasiKamar_strategy)
def test_reservasikamar_tgl_start_booking_setter(instance):
    original = instance.tgl_start_booking
    instance.tgl_start_booking = original
    assert instance.tgl_start_booking == original



@given(instance=ReservasiKamar_strategy)
def test_reservasikamar_tgl_end_booking_setter(instance):
    original = instance.tgl_end_booking
    instance.tgl_end_booking = original
    assert instance.tgl_end_booking == original

@given(instance=Kamar_strategy)
@settings(max_examples=50)
def test_kamar_instantiation(instance):
    assert isinstance(instance, Kamar)



@given(instance=Kamar_strategy)
def test_kamar__attr_setter(instance):
    original = instance._attr
    instance._attr = original
    assert instance._attr == original



@given(instance=Kamar_strategy)
def test_kamar_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Kamar_strategy)
def test_kamar_jumlah_bed_setter(instance):
    original = instance.jumlah_bed
    instance.jumlah_bed = original
    assert instance.jumlah_bed == original



@given(instance=Kamar_strategy)
def test_kamar_no_kamar_setter(instance):
    original = instance.no_kamar
    instance.no_kamar = original
    assert instance.no_kamar == original



@given(instance=Kamar_strategy)
def test_kamar_tipe_setter(instance):
    original = instance.tipe
    instance.tipe = original
    assert instance.tipe == original

@given(instance=hjb_Interface_strategy)
@settings(max_examples=50)
def test_hjb_interface_instantiation(instance):
    assert isinstance(instance, hjb_Interface)

@given(instance=Admin_strategy)
@settings(max_examples=50)
def test_admin_instantiation(instance):
    assert isinstance(instance, Admin)



@given(instance=Admin_strategy)
def test_admin_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Admin_strategy)
def test_admin_attribute_setter(instance):
    original = instance.attribute
    instance.attribute = original
    assert instance.attribute == original



@given(instance=Admin_strategy)
def test_admin_insertData_setter(instance):
    original = instance.insertData
    instance.insertData = original
    assert instance.insertData == original



@given(instance=Admin_strategy)
def test_admin_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Admin_strategy)
def test_admin_ID_admin_setter(instance):
    original = instance.ID_admin
    instance.ID_admin = original
    assert instance.ID_admin == original

@given(instance=Pemesan_strategy)
@settings(max_examples=50)
def test_pemesan_instantiation(instance):
    assert isinstance(instance, Pemesan)



@given(instance=Pemesan_strategy)
def test_pemesan_Emai_setter(instance):
    original = instance.Emai
    instance.Emai = original
    assert instance.Emai == original



@given(instance=Pemesan_strategy)
def test_pemesan_Alamat_setter(instance):
    original = instance.Alamat
    instance.Alamat = original
    assert instance.Alamat == original



@given(instance=Pemesan_strategy)
def test_pemesan_Nama_setter(instance):
    original = instance.Nama
    instance.Nama = original
    assert instance.Nama == original



@given(instance=Pemesan_strategy)
def test_pemesan_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original



@given(instance=Pemesan_strategy)
def test_pemesan_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Pemesan_strategy)
def test_pemesan_NIK_setter(instance):
    original = instance.NIK
    instance.NIK = original
    assert instance.NIK == original



@given(instance=Pemesan_strategy)
def test_pemesan_phone_number_setter(instance):
    original = instance.phone_number
    instance.phone_number = original
    assert instance.phone_number == original

@given(instance=Register_UseCase_strategy)
@settings(max_examples=50)
def test_register_usecase_instantiation(instance):
    assert isinstance(instance, Register_UseCase)

@given(instance=Login_UseCase_strategy)
@settings(max_examples=50)
def test_login_usecase_instantiation(instance):
    assert isinstance(instance, Login_UseCase)

@given(instance=Kamar_Standard_UseCase_strategy)
@settings(max_examples=50)
def test_kamar_standard_usecase_instantiation(instance):
    assert isinstance(instance, Kamar_Standard_UseCase)

@given(instance=Kamar_Keluarga_UseCase_strategy)
@settings(max_examples=50)
def test_kamar_keluarga_usecase_instantiation(instance):
    assert isinstance(instance, Kamar_Keluarga_UseCase)

@given(instance=Kamar_Deluxe_UseCase_strategy)
@settings(max_examples=50)
def test_kamar_deluxe_usecase_instantiation(instance):
    assert isinstance(instance, Kamar_Deluxe_UseCase)

@given(instance=Denda_UseCase_strategy)
@settings(max_examples=50)
def test_denda_usecase_instantiation(instance):
    assert isinstance(instance, Denda_UseCase)

@given(instance=Check_Out_UseCase_strategy)
@settings(max_examples=50)
def test_check_out_usecase_instantiation(instance):
    assert isinstance(instance, Check_Out_UseCase)

@given(instance=Check_in_UseCase_strategy)
@settings(max_examples=50)
def test_check_in_usecase_instantiation(instance):
    assert isinstance(instance, Check_in_UseCase)

@given(instance=Cancel_Pemesanan_UseCase_strategy)
@settings(max_examples=50)
def test_cancel_pemesanan_usecase_instantiation(instance):
    assert isinstance(instance, Cancel_Pemesanan_UseCase)

@given(instance=Melakukan_pembayaran_UseCase_strategy)
@settings(max_examples=50)
def test_melakukan_pembayaran_usecase_instantiation(instance):
    assert isinstance(instance, Melakukan_pembayaran_UseCase)

@given(instance=Kirim_e_booking_email_UseCase_strategy)
@settings(max_examples=50)
def test_kirim_e_booking_email_usecase_instantiation(instance):
    assert isinstance(instance, Kirim_e_booking_email_UseCase)

@given(instance=Mengirim_e_bukti_Bayar_UseCase_strategy)
@settings(max_examples=50)
def test_mengirim_e_bukti_bayar_usecase_instantiation(instance):
    assert isinstance(instance, Mengirim_e_bukti_Bayar_UseCase)

@given(instance=Melakukan_reservasi_kamar_UseCase_strategy)
@settings(max_examples=50)
def test_melakukan_reservasi_kamar_usecase_instantiation(instance):
    assert isinstance(instance, Melakukan_reservasi_kamar_UseCase)

@given(instance=Admin_Actor_strategy)
@settings(max_examples=50)
def test_admin_actor_instantiation(instance):
    assert isinstance(instance, Admin_Actor)

@given(instance=Pemesan_Actor_strategy)
@settings(max_examples=50)
def test_pemesan_actor_instantiation(instance):
    assert isinstance(instance, Pemesan_Actor)

@given(instance=Melihat_Katalog_Kamar_UseCase_strategy)
@settings(max_examples=50)
def test_melihat_katalog_kamar_usecase_instantiation(instance):
    assert isinstance(instance, Melihat_Katalog_Kamar_UseCase)

@given(instance=Pengunjung_Actor_strategy)
@settings(max_examples=50)
def test_pengunjung_actor_instantiation(instance):
    assert isinstance(instance, Pengunjung_Actor)
