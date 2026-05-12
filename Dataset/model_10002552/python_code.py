from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase:

    pass


class Mulai_Membaca_UseCase:

    pass


class Memilih_Kategori_Buku_UseCase:

    pass


class Melihat_Tampilan_Awal_Aplikasi_UseCase:

    pass


class Melakukan_Login_UseCase:

    pass


class User_Actor:

    pass


class Melakukan_Penerjemahan_Buku_Bacaan_UseCase:

    pass


class Buku_berbahasa_Asing_UseCase:

    pass


class Melakukan_Logout_UseCase:

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


class Login1:

    def __init__(self, usernam: str, password: str):
        self.usernam = usernam
        self.password = password
        
        pass
    @property
    def usernam(self):
        return self.__usernam
    @usernam.setter
    def usernam(self, usernam: str):
        self.__usernam = usernam

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Profil:

    def __init__(self, Biodata: str):
        self.Biodata = Biodata
        
        pass
    @property
    def Biodata(self):
        return self.__Biodata
    @Biodata.setter
    def Biodata(self, Biodata: str):
        self.__Biodata = Biodata



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

