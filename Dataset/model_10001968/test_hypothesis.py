import inspect
import pytest
from hypothesis import given, assume, settings
import hypothesis.strategies as st
import copy
from datetime import date, datetime

from python_code import (
    Setting,
    masterBiaya,
    Menu_Utama,
    masterKategori,
    Login,
    Prodis,
    Jurusans,
    Mahasiswas,
    Tata_Usaha_Actor,
    Administrator_Actor,
    Sistem_Pembayaran_Add_User_UseCase,
    Sistem_Pembayaran_Add_Role_UseCase,
    Sistem_Pembayaran_Setting_UseCase,
    Sistem_Pembayaran_Pembayaran_UseCase,
    Sistem_Pembayaran_Mahasiswa_UseCase,
    Sistem_Pembayaran_Jurusan_UseCase,
    Sistem_Pembayaran_Prodi_UseCase,
    Sistem_Pembayaran_Biaya_Kuliah_UseCase,
    Sistem_Pembayaran_Kategori_Biaya_UseCase,
    Sistem_Pembayaran_Masukkan_Password_UseCase,
    Sistem_Pembayaran_Masukkan_Username_Email_UseCase,
    Sistem_Pembayaran_Login_UseCase,
    Mahasiswa_Actor,
    Sistem_Mahasiswa_Ganti_Password_UseCase,
    Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase,
    Sistem_Mahasiswa_Melihat_Informasi_UseCase,
    Sistem_Mahasiswa_Masukkan_Password_UseCase,
    Sistem_Mahasiswa_Masukkan_NIM_UseCase,
    Sistem_Mahasiswa_Login_UseCase,
    Pembayarans,
)

# =============================================================================
# SECTION 1 — STRUCTURAL TESTS
# =============================================================================



def test_setting_is_not_abstract():
    assert not inspect.isabstract(Setting)


def test_setting_constructor_exists():
    assert callable(Setting.__init__)


def test_setting_constructor_args():
    sig = inspect.signature(Setting.__init__)
    params = list(sig.parameters.keys())
    assert "logo_kampus" in params, "Missing parameter 'logo_kampus'"
    assert "nama" in params, "Missing parameter 'nama'"
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "id" in params, "Missing parameter 'id'"
    assert "alamat" in params, "Missing parameter 'alamat'"
    assert "email" in params, "Missing parameter 'email'"
    assert "no_telepon" in params, "Missing parameter 'no_telepon'"
    assert "no_faximile" in params, "Missing parameter 'no_faximile'"

def test_setting_has_logo_kampus():
    assert hasattr(Setting, "logo_kampus")
    descriptor = None
    for klass in Setting.__mro__:
        if "logo_kampus" in klass.__dict__:
            descriptor = klass.__dict__["logo_kampus"]
            break
    assert isinstance(descriptor, property)

def test_setting_has_nama():
    assert hasattr(Setting, "nama")
    descriptor = None
    for klass in Setting.__mro__:
        if "nama" in klass.__dict__:
            descriptor = klass.__dict__["nama"]
            break
    assert isinstance(descriptor, property)

def test_setting_has_user_id():
    assert hasattr(Setting, "user_id")
    descriptor = None
    for klass in Setting.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_setting_has_id():
    assert hasattr(Setting, "id")
    descriptor = None
    for klass in Setting.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_setting_has_alamat():
    assert hasattr(Setting, "alamat")
    descriptor = None
    for klass in Setting.__mro__:
        if "alamat" in klass.__dict__:
            descriptor = klass.__dict__["alamat"]
            break
    assert isinstance(descriptor, property)

def test_setting_has_email():
    assert hasattr(Setting, "email")
    descriptor = None
    for klass in Setting.__mro__:
        if "email" in klass.__dict__:
            descriptor = klass.__dict__["email"]
            break
    assert isinstance(descriptor, property)

def test_setting_has_no_telepon():
    assert hasattr(Setting, "no_telepon")
    descriptor = None
    for klass in Setting.__mro__:
        if "no_telepon" in klass.__dict__:
            descriptor = klass.__dict__["no_telepon"]
            break
    assert isinstance(descriptor, property)

def test_setting_has_no_faximile():
    assert hasattr(Setting, "no_faximile")
    descriptor = None
    for klass in Setting.__mro__:
        if "no_faximile" in klass.__dict__:
            descriptor = klass.__dict__["no_faximile"]
            break
    assert isinstance(descriptor, property)



def test_masterbiaya_is_not_abstract():
    assert not inspect.isabstract(masterBiaya)


def test_masterbiaya_constructor_exists():
    assert callable(masterBiaya.__init__)


def test_masterbiaya_constructor_args():
    sig = inspect.signature(masterBiaya.__init__)
    params = list(sig.parameters.keys())
    assert "status" in params, "Missing parameter 'status'"
    assert "nama_biaya" in params, "Missing parameter 'nama_biaya'"
    assert "id" in params, "Missing parameter 'id'"
    assert "jumlah_biaya" in params, "Missing parameter 'jumlah_biaya'"
    assert "kategori_id" in params, "Missing parameter 'kategori_id'"
    assert "jml_bayar" in params, "Missing parameter 'jml_bayar'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_masterbiaya_has_status():
    assert hasattr(masterBiaya, "status")
    descriptor = None
    for klass in masterBiaya.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_masterbiaya_has_nama_biaya():
    assert hasattr(masterBiaya, "nama_biaya")
    descriptor = None
    for klass in masterBiaya.__mro__:
        if "nama_biaya" in klass.__dict__:
            descriptor = klass.__dict__["nama_biaya"]
            break
    assert isinstance(descriptor, property)

def test_masterbiaya_has_id():
    assert hasattr(masterBiaya, "id")
    descriptor = None
    for klass in masterBiaya.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_masterbiaya_has_jumlah_biaya():
    assert hasattr(masterBiaya, "jumlah_biaya")
    descriptor = None
    for klass in masterBiaya.__mro__:
        if "jumlah_biaya" in klass.__dict__:
            descriptor = klass.__dict__["jumlah_biaya"]
            break
    assert isinstance(descriptor, property)

def test_masterbiaya_has_kategori_id():
    assert hasattr(masterBiaya, "kategori_id")
    descriptor = None
    for klass in masterBiaya.__mro__:
        if "kategori_id" in klass.__dict__:
            descriptor = klass.__dict__["kategori_id"]
            break
    assert isinstance(descriptor, property)

def test_masterbiaya_has_jml_bayar():
    assert hasattr(masterBiaya, "jml_bayar")
    descriptor = None
    for klass in masterBiaya.__mro__:
        if "jml_bayar" in klass.__dict__:
            descriptor = klass.__dict__["jml_bayar"]
            break
    assert isinstance(descriptor, property)

def test_masterbiaya_has_user_id():
    assert hasattr(masterBiaya, "user_id")
    descriptor = None
    for klass in masterBiaya.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_menu_utama_is_not_abstract():
    assert not inspect.isabstract(Menu_Utama)


def test_menu_utama_constructor_exists():
    assert callable(Menu_Utama.__init__)


def test_menu_utama_constructor_args():
    sig = inspect.signature(Menu_Utama.__init__)
    params = list(sig.parameters.keys())



def test_masterkategori_is_not_abstract():
    assert not inspect.isabstract(masterKategori)


def test_masterkategori_constructor_exists():
    assert callable(masterKategori.__init__)


def test_masterkategori_constructor_args():
    sig = inspect.signature(masterKategori.__init__)
    params = list(sig.parameters.keys())
    assert "nama_kategori" in params, "Missing parameter 'nama_kategori'"
    assert "status" in params, "Missing parameter 'status'"
    assert "id" in params, "Missing parameter 'id'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_masterkategori_has_nama_kategori():
    assert hasattr(masterKategori, "nama_kategori")
    descriptor = None
    for klass in masterKategori.__mro__:
        if "nama_kategori" in klass.__dict__:
            descriptor = klass.__dict__["nama_kategori"]
            break
    assert isinstance(descriptor, property)

def test_masterkategori_has_status():
    assert hasattr(masterKategori, "status")
    descriptor = None
    for klass in masterKategori.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_masterkategori_has_id():
    assert hasattr(masterKategori, "id")
    descriptor = None
    for klass in masterKategori.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_masterkategori_has_user_id():
    assert hasattr(masterKategori, "user_id")
    descriptor = None
    for klass in masterKategori.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_login_is_not_abstract():
    assert not inspect.isabstract(Login)


def test_login_constructor_exists():
    assert callable(Login.__init__)


def test_login_constructor_args():
    sig = inspect.signature(Login.__init__)
    params = list(sig.parameters.keys())
    assert "password" in params, "Missing parameter 'password'"
    assert "username" in params, "Missing parameter 'username'"

def test_login_has_password():
    assert hasattr(Login, "password")
    descriptor = None
    for klass in Login.__mro__:
        if "password" in klass.__dict__:
            descriptor = klass.__dict__["password"]
            break
    assert isinstance(descriptor, property)

def test_login_has_username():
    assert hasattr(Login, "username")
    descriptor = None
    for klass in Login.__mro__:
        if "username" in klass.__dict__:
            descriptor = klass.__dict__["username"]
            break
    assert isinstance(descriptor, property)



def test_prodis_is_not_abstract():
    assert not inspect.isabstract(Prodis)


def test_prodis_constructor_exists():
    assert callable(Prodis.__init__)


def test_prodis_constructor_args():
    sig = inspect.signature(Prodis.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"
    assert "prodi_name" in params, "Missing parameter 'prodi_name'"
    assert "kapasitas_max" in params, "Missing parameter 'kapasitas_max'"
    assert "status" in params, "Missing parameter 'status'"
    assert "user_id" in params, "Missing parameter 'user_id'"

def test_prodis_has_id():
    assert hasattr(Prodis, "id")
    descriptor = None
    for klass in Prodis.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_prodis_has_prodi_name():
    assert hasattr(Prodis, "prodi_name")
    descriptor = None
    for klass in Prodis.__mro__:
        if "prodi_name" in klass.__dict__:
            descriptor = klass.__dict__["prodi_name"]
            break
    assert isinstance(descriptor, property)

def test_prodis_has_kapasitas_max():
    assert hasattr(Prodis, "kapasitas_max")
    descriptor = None
    for klass in Prodis.__mro__:
        if "kapasitas_max" in klass.__dict__:
            descriptor = klass.__dict__["kapasitas_max"]
            break
    assert isinstance(descriptor, property)

def test_prodis_has_status():
    assert hasattr(Prodis, "status")
    descriptor = None
    for klass in Prodis.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_prodis_has_user_id():
    assert hasattr(Prodis, "user_id")
    descriptor = None
    for klass in Prodis.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)



def test_jurusans_is_not_abstract():
    assert not inspect.isabstract(Jurusans)


def test_jurusans_constructor_exists():
    assert callable(Jurusans.__init__)


def test_jurusans_constructor_args():
    sig = inspect.signature(Jurusans.__init__)
    params = list(sig.parameters.keys())
    assert "jurusan_name" in params, "Missing parameter 'jurusan_name'"
    assert "prodi_id" in params, "Missing parameter 'prodi_id'"
    assert "id" in params, "Missing parameter 'id'"

def test_jurusans_has_jurusan_name():
    assert hasattr(Jurusans, "jurusan_name")
    descriptor = None
    for klass in Jurusans.__mro__:
        if "jurusan_name" in klass.__dict__:
            descriptor = klass.__dict__["jurusan_name"]
            break
    assert isinstance(descriptor, property)

def test_jurusans_has_prodi_id():
    assert hasattr(Jurusans, "prodi_id")
    descriptor = None
    for klass in Jurusans.__mro__:
        if "prodi_id" in klass.__dict__:
            descriptor = klass.__dict__["prodi_id"]
            break
    assert isinstance(descriptor, property)

def test_jurusans_has_id():
    assert hasattr(Jurusans, "id")
    descriptor = None
    for klass in Jurusans.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_mahasiswas_is_not_abstract():
    assert not inspect.isabstract(Mahasiswas)


def test_mahasiswas_constructor_exists():
    assert callable(Mahasiswas.__init__)


def test_mahasiswas_constructor_args():
    sig = inspect.signature(Mahasiswas.__init__)
    params = list(sig.parameters.keys())
    assert "id" in params, "Missing parameter 'id'"

def test_mahasiswas_has_id():
    assert hasattr(Mahasiswas, "id")
    descriptor = None
    for klass in Mahasiswas.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)



def test_tata_usaha_actor_is_not_abstract():
    assert not inspect.isabstract(Tata_Usaha_Actor)


def test_tata_usaha_actor_constructor_exists():
    assert callable(Tata_Usaha_Actor.__init__)


def test_tata_usaha_actor_constructor_args():
    sig = inspect.signature(Tata_Usaha_Actor.__init__)
    params = list(sig.parameters.keys())



def test_administrator_actor_is_not_abstract():
    assert not inspect.isabstract(Administrator_Actor)


def test_administrator_actor_constructor_exists():
    assert callable(Administrator_Actor.__init__)


def test_administrator_actor_constructor_args():
    sig = inspect.signature(Administrator_Actor.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_add_user_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Add_User_UseCase)


def test_sistem_pembayaran_add_user_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Add_User_UseCase.__init__)


def test_sistem_pembayaran_add_user_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Add_User_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_add_role_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Add_Role_UseCase)


def test_sistem_pembayaran_add_role_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Add_Role_UseCase.__init__)


def test_sistem_pembayaran_add_role_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Add_Role_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_setting_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Setting_UseCase)


def test_sistem_pembayaran_setting_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Setting_UseCase.__init__)


def test_sistem_pembayaran_setting_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Setting_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_pembayaran_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Pembayaran_UseCase)


def test_sistem_pembayaran_pembayaran_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Pembayaran_UseCase.__init__)


def test_sistem_pembayaran_pembayaran_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Pembayaran_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_mahasiswa_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Mahasiswa_UseCase)


def test_sistem_pembayaran_mahasiswa_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Mahasiswa_UseCase.__init__)


def test_sistem_pembayaran_mahasiswa_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Mahasiswa_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_jurusan_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Jurusan_UseCase)


def test_sistem_pembayaran_jurusan_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Jurusan_UseCase.__init__)


def test_sistem_pembayaran_jurusan_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Jurusan_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_prodi_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Prodi_UseCase)


def test_sistem_pembayaran_prodi_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Prodi_UseCase.__init__)


def test_sistem_pembayaran_prodi_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Prodi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_biaya_kuliah_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Biaya_Kuliah_UseCase)


def test_sistem_pembayaran_biaya_kuliah_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Biaya_Kuliah_UseCase.__init__)


def test_sistem_pembayaran_biaya_kuliah_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Biaya_Kuliah_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_kategori_biaya_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Kategori_Biaya_UseCase)


def test_sistem_pembayaran_kategori_biaya_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Kategori_Biaya_UseCase.__init__)


def test_sistem_pembayaran_kategori_biaya_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Kategori_Biaya_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_masukkan_password_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Masukkan_Password_UseCase)


def test_sistem_pembayaran_masukkan_password_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Masukkan_Password_UseCase.__init__)


def test_sistem_pembayaran_masukkan_password_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Masukkan_Password_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_masukkan_username_email_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Masukkan_Username_Email_UseCase)


def test_sistem_pembayaran_masukkan_username_email_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Masukkan_Username_Email_UseCase.__init__)


def test_sistem_pembayaran_masukkan_username_email_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Masukkan_Username_Email_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_pembayaran_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Pembayaran_Login_UseCase)


def test_sistem_pembayaran_login_usecase_constructor_exists():
    assert callable(Sistem_Pembayaran_Login_UseCase.__init__)


def test_sistem_pembayaran_login_usecase_constructor_args():
    sig = inspect.signature(Sistem_Pembayaran_Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_mahasiswa_actor_is_not_abstract():
    assert not inspect.isabstract(Mahasiswa_Actor)


def test_mahasiswa_actor_constructor_exists():
    assert callable(Mahasiswa_Actor.__init__)


def test_mahasiswa_actor_constructor_args():
    sig = inspect.signature(Mahasiswa_Actor.__init__)
    params = list(sig.parameters.keys())



def test_sistem_mahasiswa_ganti_password_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Ganti_Password_UseCase)


def test_sistem_mahasiswa_ganti_password_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Ganti_Password_UseCase.__init__)


def test_sistem_mahasiswa_ganti_password_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Ganti_Password_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_mahasiswa_update_data_mahasiswa_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase)


def test_sistem_mahasiswa_update_data_mahasiswa_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase.__init__)


def test_sistem_mahasiswa_update_data_mahasiswa_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_mahasiswa_melihat_informasi_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Melihat_Informasi_UseCase)


def test_sistem_mahasiswa_melihat_informasi_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Melihat_Informasi_UseCase.__init__)


def test_sistem_mahasiswa_melihat_informasi_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Melihat_Informasi_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_mahasiswa_masukkan_password_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Masukkan_Password_UseCase)


def test_sistem_mahasiswa_masukkan_password_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Masukkan_Password_UseCase.__init__)


def test_sistem_mahasiswa_masukkan_password_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Masukkan_Password_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_mahasiswa_masukkan_nim_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Masukkan_NIM_UseCase)


def test_sistem_mahasiswa_masukkan_nim_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Masukkan_NIM_UseCase.__init__)


def test_sistem_mahasiswa_masukkan_nim_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Masukkan_NIM_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_sistem_mahasiswa_login_usecase_is_not_abstract():
    assert not inspect.isabstract(Sistem_Mahasiswa_Login_UseCase)


def test_sistem_mahasiswa_login_usecase_constructor_exists():
    assert callable(Sistem_Mahasiswa_Login_UseCase.__init__)


def test_sistem_mahasiswa_login_usecase_constructor_args():
    sig = inspect.signature(Sistem_Mahasiswa_Login_UseCase.__init__)
    params = list(sig.parameters.keys())



def test_pembayarans_is_not_abstract():
    assert not inspect.isabstract(Pembayarans)


def test_pembayarans_constructor_exists():
    assert callable(Pembayarans.__init__)


def test_pembayarans_constructor_args():
    sig = inspect.signature(Pembayarans.__init__)
    params = list(sig.parameters.keys())
    assert "user_id" in params, "Missing parameter 'user_id'"
    assert "mahasiswa_id" in params, "Missing parameter 'mahasiswa_id'"
    assert "keterangan" in params, "Missing parameter 'keterangan'"
    assert "status" in params, "Missing parameter 'status'"
    assert "pembayaran_tipe" in params, "Missing parameter 'pembayaran_tipe'"
    assert "no_pembayaran" in params, "Missing parameter 'no_pembayaran'"
    assert "id" in params, "Missing parameter 'id'"
    assert "tanggal_pembayaran" in params, "Missing parameter 'tanggal_pembayaran'"
    assert "semester_id" in params, "Missing parameter 'semester_id'"
    assert "prefix" in params, "Missing parameter 'prefix'"
    assert "biaya_kuliah_id" in params, "Missing parameter 'biaya_kuliah_id'"
    assert "jumlah" in params, "Missing parameter 'jumlah'"

def test_pembayarans_has_user_id():
    assert hasattr(Pembayarans, "user_id")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "user_id" in klass.__dict__:
            descriptor = klass.__dict__["user_id"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_mahasiswa_id():
    assert hasattr(Pembayarans, "mahasiswa_id")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "mahasiswa_id" in klass.__dict__:
            descriptor = klass.__dict__["mahasiswa_id"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_keterangan():
    assert hasattr(Pembayarans, "keterangan")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "keterangan" in klass.__dict__:
            descriptor = klass.__dict__["keterangan"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_status():
    assert hasattr(Pembayarans, "status")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "status" in klass.__dict__:
            descriptor = klass.__dict__["status"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_pembayaran_tipe():
    assert hasattr(Pembayarans, "pembayaran_tipe")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "pembayaran_tipe" in klass.__dict__:
            descriptor = klass.__dict__["pembayaran_tipe"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_no_pembayaran():
    assert hasattr(Pembayarans, "no_pembayaran")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "no_pembayaran" in klass.__dict__:
            descriptor = klass.__dict__["no_pembayaran"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_id():
    assert hasattr(Pembayarans, "id")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "id" in klass.__dict__:
            descriptor = klass.__dict__["id"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_tanggal_pembayaran():
    assert hasattr(Pembayarans, "tanggal_pembayaran")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "tanggal_pembayaran" in klass.__dict__:
            descriptor = klass.__dict__["tanggal_pembayaran"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_semester_id():
    assert hasattr(Pembayarans, "semester_id")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "semester_id" in klass.__dict__:
            descriptor = klass.__dict__["semester_id"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_prefix():
    assert hasattr(Pembayarans, "prefix")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "prefix" in klass.__dict__:
            descriptor = klass.__dict__["prefix"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_biaya_kuliah_id():
    assert hasattr(Pembayarans, "biaya_kuliah_id")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "biaya_kuliah_id" in klass.__dict__:
            descriptor = klass.__dict__["biaya_kuliah_id"]
            break
    assert isinstance(descriptor, property)

def test_pembayarans_has_jumlah():
    assert hasattr(Pembayarans, "jumlah")
    descriptor = None
    for klass in Pembayarans.__mro__:
        if "jumlah" in klass.__dict__:
            descriptor = klass.__dict__["jumlah"]
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
Setting_strategy = st.builds(
    Setting,
    logo_kampus=
        safe_text,
    nama=
        safe_text,
    user_id=
        st.integers(),
    id=
        st.integers(),
    alamat=
        safe_text,
    email=
        safe_text,
    no_telepon=
        safe_text,
    no_faximile=
        safe_text
)
masterBiaya_strategy = st.builds(
    masterBiaya,
    status=
        st.integers(),
    nama_biaya=
        safe_text,
    id=
        st.integers(),
    jumlah_biaya=
        st.integers(),
    kategori_id=
        st.integers(),
    jml_bayar=
        st.integers(),
    user_id=
        st.integers()
)
Menu_Utama_strategy = st.builds(
    Menu_Utama,
)
masterKategori_strategy = st.builds(
    masterKategori,
    nama_kategori=
        safe_text,
    status=
        st.integers(),
    id=
        st.integers(),
    user_id=
        st.integers()
)
Login_strategy = st.builds(
    Login,
    password=
        safe_text,
    username=
        safe_text
)
Prodis_strategy = st.builds(
    Prodis,
    id=
        st.integers(),
    prodi_name=
        safe_text,
    kapasitas_max=
        st.integers(),
    status=
        st.integers(),
    user_id=
        st.integers()
)
Jurusans_strategy = st.builds(
    Jurusans,
    jurusan_name=
        safe_text,
    prodi_id=
        st.integers(),
    id=
        st.integers()
)
Mahasiswas_strategy = st.builds(
    Mahasiswas,
    id=
        st.integers()
)
Tata_Usaha_Actor_strategy = st.builds(
    Tata_Usaha_Actor,
)
Administrator_Actor_strategy = st.builds(
    Administrator_Actor,
)
Sistem_Pembayaran_Add_User_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Add_User_UseCase,
)
Sistem_Pembayaran_Add_Role_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Add_Role_UseCase,
)
Sistem_Pembayaran_Setting_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Setting_UseCase,
)
Sistem_Pembayaran_Pembayaran_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Pembayaran_UseCase,
)
Sistem_Pembayaran_Mahasiswa_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Mahasiswa_UseCase,
)
Sistem_Pembayaran_Jurusan_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Jurusan_UseCase,
)
Sistem_Pembayaran_Prodi_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Prodi_UseCase,
)
Sistem_Pembayaran_Biaya_Kuliah_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Biaya_Kuliah_UseCase,
)
Sistem_Pembayaran_Kategori_Biaya_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Kategori_Biaya_UseCase,
)
Sistem_Pembayaran_Masukkan_Password_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Masukkan_Password_UseCase,
)
Sistem_Pembayaran_Masukkan_Username_Email_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Masukkan_Username_Email_UseCase,
)
Sistem_Pembayaran_Login_UseCase_strategy = st.builds(
    Sistem_Pembayaran_Login_UseCase,
)
Mahasiswa_Actor_strategy = st.builds(
    Mahasiswa_Actor,
)
Sistem_Mahasiswa_Ganti_Password_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Ganti_Password_UseCase,
)
Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase,
)
Sistem_Mahasiswa_Melihat_Informasi_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Melihat_Informasi_UseCase,
)
Sistem_Mahasiswa_Masukkan_Password_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Masukkan_Password_UseCase,
)
Sistem_Mahasiswa_Masukkan_NIM_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Masukkan_NIM_UseCase,
)
Sistem_Mahasiswa_Login_UseCase_strategy = st.builds(
    Sistem_Mahasiswa_Login_UseCase,
)
Pembayarans_strategy = st.builds(
    Pembayarans,
    user_id=
        st.integers(),
    mahasiswa_id=
        st.integers(),
    keterangan=
        safe_text,
    status=
        st.integers(),
    pembayaran_tipe=
        st.integers(),
    no_pembayaran=
        safe_text,
    id=
        st.integers(),
    tanggal_pembayaran=
        safe_text,
    semester_id=
        st.integers(),
    prefix=
        safe_text,
    biaya_kuliah_id=
        st.integers(),
    jumlah=
        st.integers()
)

@given(instance=Setting_strategy)
@settings(max_examples=50)
def test_setting_instantiation(instance):
    assert isinstance(instance, Setting)



@given(instance=Setting_strategy)
def test_setting_logo_kampus_setter(instance):
    original = instance.logo_kampus
    instance.logo_kampus = original
    assert instance.logo_kampus == original



@given(instance=Setting_strategy)
def test_setting_nama_setter(instance):
    original = instance.nama
    instance.nama = original
    assert instance.nama == original



@given(instance=Setting_strategy)
def test_setting_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Setting_strategy)
def test_setting_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Setting_strategy)
def test_setting_alamat_setter(instance):
    original = instance.alamat
    instance.alamat = original
    assert instance.alamat == original



@given(instance=Setting_strategy)
def test_setting_email_setter(instance):
    original = instance.email
    instance.email = original
    assert instance.email == original



@given(instance=Setting_strategy)
def test_setting_no_telepon_setter(instance):
    original = instance.no_telepon
    instance.no_telepon = original
    assert instance.no_telepon == original



@given(instance=Setting_strategy)
def test_setting_no_faximile_setter(instance):
    original = instance.no_faximile
    instance.no_faximile = original
    assert instance.no_faximile == original

@given(instance=masterBiaya_strategy)
@settings(max_examples=50)
def test_masterbiaya_instantiation(instance):
    assert isinstance(instance, masterBiaya)



@given(instance=masterBiaya_strategy)
def test_masterbiaya_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=masterBiaya_strategy)
def test_masterbiaya_nama_biaya_setter(instance):
    original = instance.nama_biaya
    instance.nama_biaya = original
    assert instance.nama_biaya == original



@given(instance=masterBiaya_strategy)
def test_masterbiaya_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=masterBiaya_strategy)
def test_masterbiaya_jumlah_biaya_setter(instance):
    original = instance.jumlah_biaya
    instance.jumlah_biaya = original
    assert instance.jumlah_biaya == original



@given(instance=masterBiaya_strategy)
def test_masterbiaya_kategori_id_setter(instance):
    original = instance.kategori_id
    instance.kategori_id = original
    assert instance.kategori_id == original



@given(instance=masterBiaya_strategy)
def test_masterbiaya_jml_bayar_setter(instance):
    original = instance.jml_bayar
    instance.jml_bayar = original
    assert instance.jml_bayar == original



@given(instance=masterBiaya_strategy)
def test_masterbiaya_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Menu_Utama_strategy)
@settings(max_examples=50)
def test_menu_utama_instantiation(instance):
    assert isinstance(instance, Menu_Utama)

@given(instance=masterKategori_strategy)
@settings(max_examples=50)
def test_masterkategori_instantiation(instance):
    assert isinstance(instance, masterKategori)



@given(instance=masterKategori_strategy)
def test_masterkategori_nama_kategori_setter(instance):
    original = instance.nama_kategori
    instance.nama_kategori = original
    assert instance.nama_kategori == original



@given(instance=masterKategori_strategy)
def test_masterkategori_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=masterKategori_strategy)
def test_masterkategori_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=masterKategori_strategy)
def test_masterkategori_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Login_strategy)
@settings(max_examples=50)
def test_login_instantiation(instance):
    assert isinstance(instance, Login)



@given(instance=Login_strategy)
def test_login_password_setter(instance):
    original = instance.password
    instance.password = original
    assert instance.password == original



@given(instance=Login_strategy)
def test_login_username_setter(instance):
    original = instance.username
    instance.username = original
    assert instance.username == original

@given(instance=Prodis_strategy)
@settings(max_examples=50)
def test_prodis_instantiation(instance):
    assert isinstance(instance, Prodis)



@given(instance=Prodis_strategy)
def test_prodis_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Prodis_strategy)
def test_prodis_prodi_name_setter(instance):
    original = instance.prodi_name
    instance.prodi_name = original
    assert instance.prodi_name == original



@given(instance=Prodis_strategy)
def test_prodis_kapasitas_max_setter(instance):
    original = instance.kapasitas_max
    instance.kapasitas_max = original
    assert instance.kapasitas_max == original



@given(instance=Prodis_strategy)
def test_prodis_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Prodis_strategy)
def test_prodis_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original

@given(instance=Jurusans_strategy)
@settings(max_examples=50)
def test_jurusans_instantiation(instance):
    assert isinstance(instance, Jurusans)



@given(instance=Jurusans_strategy)
def test_jurusans_jurusan_name_setter(instance):
    original = instance.jurusan_name
    instance.jurusan_name = original
    assert instance.jurusan_name == original



@given(instance=Jurusans_strategy)
def test_jurusans_prodi_id_setter(instance):
    original = instance.prodi_id
    instance.prodi_id = original
    assert instance.prodi_id == original



@given(instance=Jurusans_strategy)
def test_jurusans_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Mahasiswas_strategy)
@settings(max_examples=50)
def test_mahasiswas_instantiation(instance):
    assert isinstance(instance, Mahasiswas)



@given(instance=Mahasiswas_strategy)
def test_mahasiswas_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original

@given(instance=Tata_Usaha_Actor_strategy)
@settings(max_examples=50)
def test_tata_usaha_actor_instantiation(instance):
    assert isinstance(instance, Tata_Usaha_Actor)

@given(instance=Administrator_Actor_strategy)
@settings(max_examples=50)
def test_administrator_actor_instantiation(instance):
    assert isinstance(instance, Administrator_Actor)

@given(instance=Sistem_Pembayaran_Add_User_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_add_user_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Add_User_UseCase)

@given(instance=Sistem_Pembayaran_Add_Role_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_add_role_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Add_Role_UseCase)

@given(instance=Sistem_Pembayaran_Setting_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_setting_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Setting_UseCase)

@given(instance=Sistem_Pembayaran_Pembayaran_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_pembayaran_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Pembayaran_UseCase)

@given(instance=Sistem_Pembayaran_Mahasiswa_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_mahasiswa_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Mahasiswa_UseCase)

@given(instance=Sistem_Pembayaran_Jurusan_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_jurusan_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Jurusan_UseCase)

@given(instance=Sistem_Pembayaran_Prodi_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_prodi_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Prodi_UseCase)

@given(instance=Sistem_Pembayaran_Biaya_Kuliah_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_biaya_kuliah_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Biaya_Kuliah_UseCase)

@given(instance=Sistem_Pembayaran_Kategori_Biaya_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_kategori_biaya_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Kategori_Biaya_UseCase)

@given(instance=Sistem_Pembayaran_Masukkan_Password_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_masukkan_password_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Masukkan_Password_UseCase)

@given(instance=Sistem_Pembayaran_Masukkan_Username_Email_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_masukkan_username_email_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Masukkan_Username_Email_UseCase)

@given(instance=Sistem_Pembayaran_Login_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_pembayaran_login_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Pembayaran_Login_UseCase)

@given(instance=Mahasiswa_Actor_strategy)
@settings(max_examples=50)
def test_mahasiswa_actor_instantiation(instance):
    assert isinstance(instance, Mahasiswa_Actor)

@given(instance=Sistem_Mahasiswa_Ganti_Password_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_mahasiswa_ganti_password_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Ganti_Password_UseCase)

@given(instance=Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_mahasiswa_update_data_mahasiswa_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase)

@given(instance=Sistem_Mahasiswa_Melihat_Informasi_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_mahasiswa_melihat_informasi_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Melihat_Informasi_UseCase)

@given(instance=Sistem_Mahasiswa_Masukkan_Password_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_mahasiswa_masukkan_password_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Masukkan_Password_UseCase)

@given(instance=Sistem_Mahasiswa_Masukkan_NIM_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_mahasiswa_masukkan_nim_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Masukkan_NIM_UseCase)

@given(instance=Sistem_Mahasiswa_Login_UseCase_strategy)
@settings(max_examples=50)
def test_sistem_mahasiswa_login_usecase_instantiation(instance):
    assert isinstance(instance, Sistem_Mahasiswa_Login_UseCase)

@given(instance=Pembayarans_strategy)
@settings(max_examples=50)
def test_pembayarans_instantiation(instance):
    assert isinstance(instance, Pembayarans)



@given(instance=Pembayarans_strategy)
def test_pembayarans_user_id_setter(instance):
    original = instance.user_id
    instance.user_id = original
    assert instance.user_id == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_mahasiswa_id_setter(instance):
    original = instance.mahasiswa_id
    instance.mahasiswa_id = original
    assert instance.mahasiswa_id == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_keterangan_setter(instance):
    original = instance.keterangan
    instance.keterangan = original
    assert instance.keterangan == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_status_setter(instance):
    original = instance.status
    instance.status = original
    assert instance.status == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_pembayaran_tipe_setter(instance):
    original = instance.pembayaran_tipe
    instance.pembayaran_tipe = original
    assert instance.pembayaran_tipe == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_no_pembayaran_setter(instance):
    original = instance.no_pembayaran
    instance.no_pembayaran = original
    assert instance.no_pembayaran == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_id_setter(instance):
    original = instance.id
    instance.id = original
    assert instance.id == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_tanggal_pembayaran_setter(instance):
    original = instance.tanggal_pembayaran
    instance.tanggal_pembayaran = original
    assert instance.tanggal_pembayaran == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_semester_id_setter(instance):
    original = instance.semester_id
    instance.semester_id = original
    assert instance.semester_id == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_prefix_setter(instance):
    original = instance.prefix
    instance.prefix = original
    assert instance.prefix == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_biaya_kuliah_id_setter(instance):
    original = instance.biaya_kuliah_id
    instance.biaya_kuliah_id = original
    assert instance.biaya_kuliah_id == original



@given(instance=Pembayarans_strategy)
def test_pembayarans_jumlah_setter(instance):
    original = instance.jumlah
    instance.jumlah = original
    assert instance.jumlah == original
