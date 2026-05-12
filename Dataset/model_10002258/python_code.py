from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Halaman_Publikasi__major_sales_record_UseCase:

    pass


class Halaman_Publikasi__news_UseCase:

    pass


class Halaman_Publikasi__produk_UseCase:

    pass


class halaman_admin_login_UseCase:

    pass


class halaman_admin_news_UseCase:

    pass


class halaman_admin_major_sales_record_UseCase:

    pass


class halaman_admin_register_UseCase:

    pass


class halaman_admin_produk_UseCase:

    pass


class Pengunjung_Website_Actor:

    pass


class admin_Actor:

    pass





class halaman_admin_major_sales_record_UseCase1:

    pass


class halaman_admin_news_UseCase2:

    pass


class halaman_admin_news_UseCase1:

    pass


class halaman_admin_produk_UseCase2:

    pass


class halaman_admin_register_UseCase2:

    pass


class halaman_admin_register_UseCase1:

    pass


class halaman_admin_produk_UseCase1:

    pass


class login_admin:

    def __init__(self, email: str, password: str, admin21: "admin" = None):
        self.email = email
        self.password = password
        self.admin21 = admin21
        
        pass
    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def admin21(self):
        return self.__admin21
    @admin21.setter
    def admin21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login_admin__admin21", None)
        self.__admin21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login_admin20"):
                opp_val = getattr(old_value, "login_admin20", None)
                if opp_val == self:
                    setattr(old_value, "login_admin20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login_admin20"):
                opp_val = getattr(value, "login_admin20", None)
                setattr(value, "login_admin20", self)



class register_admin:

    def __init__(self, id_user: int, nama_lengkap: str, nik: str, email: str, password: str, admin19: "admin" = None):
        self.id_user = id_user
        self.nama_lengkap = nama_lengkap
        self.nik = nik
        self.email = email
        self.password = password
        self.admin19 = admin19
        
        pass
    @property
    def nik(self):
        return self.__nik
    @nik.setter
    def nik(self, nik: str):
        self.__nik = nik

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def nama_lengkap(self):
        return self.__nama_lengkap
    @nama_lengkap.setter
    def nama_lengkap(self, nama_lengkap: str):
        self.__nama_lengkap = nama_lengkap

    @property
    def id_user(self):
        return self.__id_user
    @id_user.setter
    def id_user(self, id_user: int):
        self.__id_user = id_user

    @property
    def admin19(self):
        return self.__admin19
    @admin19.setter
    def admin19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_register_admin__admin19", None)
        self.__admin19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "register_admin18"):
                opp_val = getattr(old_value, "register_admin18", None)
                if opp_val == self:
                    setattr(old_value, "register_admin18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "register_admin18"):
                opp_val = getattr(value, "register_admin18", None)
                setattr(value, "register_admin18", self)



class produk_Interface:

    pass


class admin:

    pass


class pengunjung_website:

    pass


class our_costumer_Interface:

    pass


class news_Interface:

    pass


class our_costumer___major:

    def __init__(self, id_major: int, logo_major: str, admin1: "admin" = None):
        self.id_major = id_major
        self.logo_major = logo_major
        self.admin1 = admin1
        
        pass
    @property
    def id_major(self):
        return self.__id_major
    @id_major.setter
    def id_major(self, id_major: int):
        self.__id_major = id_major

    @property
    def logo_major(self):
        return self.__logo_major
    @logo_major.setter
    def logo_major(self, logo_major: str):
        self.__logo_major = logo_major

    @property
    def admin1(self):
        return self.__admin1
    @admin1.setter
    def admin1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_our_costumer___major__admin1", None)
        self.__admin1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "our_costumer___major0"):
                opp_val = getattr(old_value, "our_costumer___major0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "our_costumer___major0"):
                opp_val = getattr(value, "our_costumer___major0", None)
                if opp_val is None:
                    setattr(value, "our_costumer___major0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class produk:

    def __init__(self, id_produk: int, website: str, foto_produk: str, admin3: "admin" = None):
        self.id_produk = id_produk
        self.website = website
        self.foto_produk = foto_produk
        self.admin3 = admin3
        
        pass
    @property
    def website(self):
        return self.__website
    @website.setter
    def website(self, website: str):
        self.__website = website

    @property
    def foto_produk(self):
        return self.__foto_produk
    @foto_produk.setter
    def foto_produk(self, foto_produk: str):
        self.__foto_produk = foto_produk

    @property
    def id_produk(self):
        return self.__id_produk
    @id_produk.setter
    def id_produk(self, id_produk: int):
        self.__id_produk = id_produk

    @property
    def admin3(self):
        return self.__admin3
    @admin3.setter
    def admin3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_produk__admin3", None)
        self.__admin3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "produk2"):
                opp_val = getattr(old_value, "produk2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "produk2"):
                opp_val = getattr(value, "produk2", None)
                if opp_val is None:
                    setattr(value, "produk2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class news:

    def __init__(self, id_news: int, foto_news: str, judul_news: str, isi_news: str, admin5: "admin" = None):
        self.id_news = id_news
        self.foto_news = foto_news
        self.judul_news = judul_news
        self.isi_news = isi_news
        self.admin5 = admin5
        
        pass
    @property
    def id_news(self):
        return self.__id_news
    @id_news.setter
    def id_news(self, id_news: int):
        self.__id_news = id_news

    @property
    def judul_news(self):
        return self.__judul_news
    @judul_news.setter
    def judul_news(self, judul_news: str):
        self.__judul_news = judul_news

    @property
    def isi_news(self):
        return self.__isi_news
    @isi_news.setter
    def isi_news(self, isi_news: str):
        self.__isi_news = isi_news

    @property
    def foto_news(self):
        return self.__foto_news
    @foto_news.setter
    def foto_news(self, foto_news: str):
        self.__foto_news = foto_news

    @property
    def admin5(self):
        return self.__admin5
    @admin5.setter
    def admin5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_news__admin5", None)
        self.__admin5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "news4"):
                opp_val = getattr(old_value, "news4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "news4"):
                opp_val = getattr(value, "news4", None)
                if opp_val is None:
                    setattr(value, "news4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

