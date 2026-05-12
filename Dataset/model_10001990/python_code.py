from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Melakukan_Penerjemahan_Buku_Bacaan_UseCase:

    pass


class Buku_berbahasa_Asing_UseCase:

    pass


class Keluar_dari_Aplikasi_UseCase:

    pass


class Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase:

    pass


class Mulai_Membaca_UseCase:

    pass


class Memilih_Kategori_Buku_UseCase:

    pass


class Melihat_Tampilan_Awal_Aplikasi_UseCase:

    pass


class Masuk_dari_Aplikasi_UseCase:

    pass


class User_Actor:

    pass





class Login1:

    def __init__(self, Username: str, Password: str):
        self.Username = Username
        self.Password = Password
        
        pass
    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username



class Pencarian:

    pass


class Keluar:

    def __init__(self, Keluar: str):
        self.Keluar = Keluar
        
        pass
    @property
    def Keluar(self):
        return self.__Keluar
    @Keluar.setter
    def Keluar(self, Keluar: str):
        self.__Keluar = Keluar



class Buku:

    pass


class Menu_Utama:

    pass


class MyClass:

    pass


class Class:

    pass


class Login:

    def __init__(self, username: str, password: str):
        self.username = username
        self.password = password
        
        pass
    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

