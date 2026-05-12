from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Tata_Usaha_Actor:

    pass


class Administrator_Actor:

    pass


class Sistem_Pembayaran_Add_User_UseCase:

    pass


class Sistem_Pembayaran_Add_Role_UseCase:

    pass


class Sistem_Pembayaran_Setting_UseCase:

    pass


class Sistem_Pembayaran_Pembayaran_UseCase:

    pass


class Sistem_Pembayaran_Mahasiswa_UseCase:

    pass


class Sistem_Pembayaran_Jurusan_UseCase:

    pass


class Sistem_Pembayaran_Prodi_UseCase:

    pass


class Sistem_Pembayaran_Biaya_Kuliah_UseCase:

    pass


class Sistem_Pembayaran_Kategori_Biaya_UseCase:

    pass


class Sistem_Pembayaran_Masukkan_Password_UseCase:

    pass


class Sistem_Pembayaran_Masukkan_Username_Email_UseCase:

    pass


class Sistem_Pembayaran_Login_UseCase:

    pass


class Mahasiswa_Actor:

    pass


class Sistem_Mahasiswa_Ganti_Password_UseCase:

    pass


class Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase:

    pass


class Sistem_Mahasiswa_Melihat_Informasi_UseCase:

    pass


class Sistem_Mahasiswa_Masukkan_Password_UseCase:

    pass


class Sistem_Mahasiswa_Masukkan_NIM_UseCase:

    pass


class Sistem_Mahasiswa_Login_UseCase:

    pass





class Pembayarans:

    def __init__(self, id: int, prefix: str, no_pembayaran: str, tanggal_pembayaran: str, mahasiswa_id: int, pembayaran_tipe: int, semester_id: int, biaya_kuliah_id: int, keterangan: str, jumlah: int, status: int, user_id: int):
        self.id = id
        self.prefix = prefix
        self.no_pembayaran = no_pembayaran
        self.tanggal_pembayaran = tanggal_pembayaran
        self.mahasiswa_id = mahasiswa_id
        self.pembayaran_tipe = pembayaran_tipe
        self.semester_id = semester_id
        self.biaya_kuliah_id = biaya_kuliah_id
        self.keterangan = keterangan
        self.jumlah = jumlah
        self.status = status
        self.user_id = user_id
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def prefix(self):
        return self.__prefix
    @prefix.setter
    def prefix(self, prefix: str):
        self.__prefix = prefix

    @property
    def biaya_kuliah_id(self):
        return self.__biaya_kuliah_id
    @biaya_kuliah_id.setter
    def biaya_kuliah_id(self, biaya_kuliah_id: int):
        self.__biaya_kuliah_id = biaya_kuliah_id

    @property
    def pembayaran_tipe(self):
        return self.__pembayaran_tipe
    @pembayaran_tipe.setter
    def pembayaran_tipe(self, pembayaran_tipe: int):
        self.__pembayaran_tipe = pembayaran_tipe

    @property
    def no_pembayaran(self):
        return self.__no_pembayaran
    @no_pembayaran.setter
    def no_pembayaran(self, no_pembayaran: str):
        self.__no_pembayaran = no_pembayaran

    @property
    def jumlah(self):
        return self.__jumlah
    @jumlah.setter
    def jumlah(self, jumlah: int):
        self.__jumlah = jumlah

    @property
    def semester_id(self):
        return self.__semester_id
    @semester_id.setter
    def semester_id(self, semester_id: int):
        self.__semester_id = semester_id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def tanggal_pembayaran(self):
        return self.__tanggal_pembayaran
    @tanggal_pembayaran.setter
    def tanggal_pembayaran(self, tanggal_pembayaran: str):
        self.__tanggal_pembayaran = tanggal_pembayaran

    @property
    def mahasiswa_id(self):
        return self.__mahasiswa_id
    @mahasiswa_id.setter
    def mahasiswa_id(self, mahasiswa_id: int):
        self.__mahasiswa_id = mahasiswa_id

    @property
    def keterangan(self):
        return self.__keterangan
    @keterangan.setter
    def keterangan(self, keterangan: str):
        self.__keterangan = keterangan



class Setting:

    def __init__(self, id: int, nama: str, alamat: str, no_telepon: str, no_faximile: str, email: str, logo_kampus: str, user_id: int):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.no_telepon = no_telepon
        self.no_faximile = no_faximile
        self.email = email
        self.logo_kampus = logo_kampus
        self.user_id = user_id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def no_telepon(self):
        return self.__no_telepon
    @no_telepon.setter
    def no_telepon(self, no_telepon: str):
        self.__no_telepon = no_telepon

    @property
    def no_faximile(self):
        return self.__no_faximile
    @no_faximile.setter
    def no_faximile(self, no_faximile: str):
        self.__no_faximile = no_faximile

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama: str):
        self.__nama = nama

    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, alamat: str):
        self.__alamat = alamat

    @property
    def logo_kampus(self):
        return self.__logo_kampus
    @logo_kampus.setter
    def logo_kampus(self, logo_kampus: str):
        self.__logo_kampus = logo_kampus



class masterBiaya:

    def __init__(self, id: int, kategori_id: int, nama_biaya: str, jml_bayar: int, jumlah_biaya: int, status: int, user_id: int):
        self.id = id
        self.kategori_id = kategori_id
        self.nama_biaya = nama_biaya
        self.jml_bayar = jml_bayar
        self.jumlah_biaya = jumlah_biaya
        self.status = status
        self.user_id = user_id
        
        pass
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def jumlah_biaya(self):
        return self.__jumlah_biaya
    @jumlah_biaya.setter
    def jumlah_biaya(self, jumlah_biaya: int):
        self.__jumlah_biaya = jumlah_biaya

    @property
    def nama_biaya(self):
        return self.__nama_biaya
    @nama_biaya.setter
    def nama_biaya(self, nama_biaya: str):
        self.__nama_biaya = nama_biaya

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def kategori_id(self):
        return self.__kategori_id
    @kategori_id.setter
    def kategori_id(self, kategori_id: int):
        self.__kategori_id = kategori_id

    @property
    def jml_bayar(self):
        return self.__jml_bayar
    @jml_bayar.setter
    def jml_bayar(self, jml_bayar: int):
        self.__jml_bayar = jml_bayar



class Menu_Utama:

    pass


class masterKategori:

    def __init__(self, id: int, nama_kategori: str, status: int, user_id: int):
        self.id = id
        self.nama_kategori = nama_kategori
        self.status = status
        self.user_id = user_id
        
        pass
    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def nama_kategori(self):
        return self.__nama_kategori
    @nama_kategori.setter
    def nama_kategori(self, nama_kategori: str):
        self.__nama_kategori = nama_kategori



class Login:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username



class Prodis:

    def __init__(self, id: int, prodi_name: str, kapasitas_max: int, status: int, user_id: int):
        self.id = id
        self.prodi_name = prodi_name
        self.kapasitas_max = kapasitas_max
        self.status = status
        self.user_id = user_id
        
        pass
    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: int):
        self.__status = status

    @property
    def kapasitas_max(self):
        return self.__kapasitas_max
    @kapasitas_max.setter
    def kapasitas_max(self, kapasitas_max: int):
        self.__kapasitas_max = kapasitas_max

    @property
    def prodi_name(self):
        return self.__prodi_name
    @prodi_name.setter
    def prodi_name(self, prodi_name: str):
        self.__prodi_name = prodi_name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def user_id(self):
        return self.__user_id
    @user_id.setter
    def user_id(self, user_id: int):
        self.__user_id = user_id



class Jurusans:

    def __init__(self, id: int, prodi_id: int, jurusan_name: str):
        self.id = id
        self.prodi_id = prodi_id
        self.jurusan_name = jurusan_name
        
        pass
    @property
    def prodi_id(self):
        return self.__prodi_id
    @prodi_id.setter
    def prodi_id(self, prodi_id: int):
        self.__prodi_id = prodi_id

    @property
    def jurusan_name(self):
        return self.__jurusan_name
    @jurusan_name.setter
    def jurusan_name(self, jurusan_name: str):
        self.__jurusan_name = jurusan_name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Mahasiswas:

    def __init__(self, id: int):
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

