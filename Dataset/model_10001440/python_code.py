from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Cetak_Slip_UseCase:

    pass


class Memproses_Database_UseCase:

    pass


class Melakukan_Transaksi_UseCase:

    pass


class Memverivikasi_Data_UseCase:

    pass


class Mengentry_Data_UseCase:

    pass


class Admin_Actor:

    pass


class Pelanggan__Actor:

    pass


class Melakukan_Registrasi_UseCase:

    pass


class Melakukan_Login_UseCase:

    pass





class Data_Pembayaran:

    def __init__(self, kode_bayar: str, tanggal_bayar: str, kode_kredit: str, angsuran: int, angsuranke: int, keterangan: str, pelanggan25: "Pelanggan" = None, admin27: set["Admin"] = None):
        self.kode_bayar = kode_bayar
        self.tanggal_bayar = tanggal_bayar
        self.kode_kredit = kode_kredit
        self.angsuran = angsuran
        self.angsuranke = angsuranke
        self.keterangan = keterangan
        self.pelanggan25 = pelanggan25
        self.admin27 = admin27 if admin27 is not None else set()
        
        pass
    @property
    def angsuran(self):
        return self.__angsuran
    @angsuran.setter
    def angsuran(self, angsuran: int):
        self.__angsuran = angsuran

    @property
    def kode_kredit(self):
        return self.__kode_kredit
    @kode_kredit.setter
    def kode_kredit(self, kode_kredit: str):
        self.__kode_kredit = kode_kredit

    @property
    def keterangan(self):
        return self.__keterangan
    @keterangan.setter
    def keterangan(self, keterangan: str):
        self.__keterangan = keterangan

    @property
    def angsuranke(self):
        return self.__angsuranke
    @angsuranke.setter
    def angsuranke(self, angsuranke: int):
        self.__angsuranke = angsuranke

    @property
    def tanggal_bayar(self):
        return self.__tanggal_bayar
    @tanggal_bayar.setter
    def tanggal_bayar(self, tanggal_bayar: str):
        self.__tanggal_bayar = tanggal_bayar

    @property
    def kode_bayar(self):
        return self.__kode_bayar
    @kode_bayar.setter
    def kode_bayar(self, kode_bayar: str):
        self.__kode_bayar = kode_bayar

    @property
    def pelanggan25(self):
        return self.__pelanggan25
    @pelanggan25.setter
    def pelanggan25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Pembayaran__pelanggan25", None)
        self.__pelanggan25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "data_Pembayaran24"):
                opp_val = getattr(old_value, "data_Pembayaran24", None)
                if opp_val == self:
                    setattr(old_value, "data_Pembayaran24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "data_Pembayaran24"):
                opp_val = getattr(value, "data_Pembayaran24", None)
                setattr(value, "data_Pembayaran24", self)

    @property
    def admin27(self):
        return self.__admin27
    @admin27.setter
    def admin27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_Pembayaran__admin27", None)
        self.__admin27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "data_Pembayaran26"):
                    opp_val = getattr(item, "data_Pembayaran26", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "data_Pembayaran26"):
                    opp_val = getattr(item, "data_Pembayaran26", None)
                    
                    if opp_val is None:
                        setattr(item, "data_Pembayaran26", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Pelanggan:

    def __init__(self, kode_pelanggan: str, nama: str, alamat: str, admin23: set["Admin"] = None, data_Pembayaran24: "Data_Pembayaran" = None):
        self.kode_pelanggan = kode_pelanggan
        self.nama = nama
        self.alamat = alamat
        self.admin23 = admin23 if admin23 is not None else set()
        self.data_Pembayaran24 = data_Pembayaran24
        
        pass
    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama: str):
        self.__nama = nama

    @property
    def kode_pelanggan(self):
        return self.__kode_pelanggan
    @kode_pelanggan.setter
    def kode_pelanggan(self, kode_pelanggan: str):
        self.__kode_pelanggan = kode_pelanggan

    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, alamat: str):
        self.__alamat = alamat

    @property
    def admin23(self):
        return self.__admin23
    @admin23.setter
    def admin23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pelanggan__admin23", None)
        self.__admin23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pelanggan22"):
                    opp_val = getattr(item, "pelanggan22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pelanggan22"):
                    opp_val = getattr(item, "pelanggan22", None)
                    
                    if opp_val is None:
                        setattr(item, "pelanggan22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def data_Pembayaran24(self):
        return self.__data_Pembayaran24
    @data_Pembayaran24.setter
    def data_Pembayaran24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pelanggan__data_Pembayaran24", None)
        self.__data_Pembayaran24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pelanggan25"):
                opp_val = getattr(old_value, "pelanggan25", None)
                if opp_val == self:
                    setattr(old_value, "pelanggan25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pelanggan25"):
                opp_val = getattr(value, "pelanggan25", None)
                setattr(value, "pelanggan25", self)



class Admin:

    def __init__(self, id: str, nama: str, alamat: str, no_tlp: int, login_Admin20: "Login_Admin" = None, pelanggan22: set["Pelanggan"] = None, data_Pembayaran26: set["Data_Pembayaran"] = None):
        self.id = id
        self.nama = nama
        self.alamat = alamat
        self.no_tlp = no_tlp
        self.login_Admin20 = login_Admin20
        self.pelanggan22 = pelanggan22 if pelanggan22 is not None else set()
        self.data_Pembayaran26 = data_Pembayaran26 if data_Pembayaran26 is not None else set()
        
        pass
    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, alamat: str):
        self.__alamat = alamat

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama: str):
        self.__nama = nama

    @property
    def no_tlp(self):
        return self.__no_tlp
    @no_tlp.setter
    def no_tlp(self, no_tlp: int):
        self.__no_tlp = no_tlp

    @property
    def data_Pembayaran26(self):
        return self.__data_Pembayaran26
    @data_Pembayaran26.setter
    def data_Pembayaran26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__data_Pembayaran26", None)
        self.__data_Pembayaran26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin27"):
                    opp_val = getattr(item, "admin27", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin27"):
                    opp_val = getattr(item, "admin27", None)
                    
                    if opp_val is None:
                        setattr(item, "admin27", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def login_Admin20(self):
        return self.__login_Admin20
    @login_Admin20.setter
    def login_Admin20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__login_Admin20", None)
        self.__login_Admin20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin21"):
                opp_val = getattr(old_value, "admin21", None)
                if opp_val == self:
                    setattr(old_value, "admin21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin21"):
                opp_val = getattr(value, "admin21", None)
                setattr(value, "admin21", self)

    @property
    def pelanggan22(self):
        return self.__pelanggan22
    @pelanggan22.setter
    def pelanggan22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__pelanggan22", None)
        self.__pelanggan22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin23"):
                    opp_val = getattr(item, "admin23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin23"):
                    opp_val = getattr(item, "admin23", None)
                    
                    if opp_val is None:
                        setattr(item, "admin23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Login_Admin:

    def __init__(self, User_name: str, attribute: str, admin21: "Admin" = None):
        self.User_name = User_name
        self.attribute = attribute
        self.admin21 = admin21
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def User_name(self):
        return self.__User_name
    @User_name.setter
    def User_name(self, User_name: str):
        self.__User_name = User_name

    @property
    def admin21(self):
        return self.__admin21
    @admin21.setter
    def admin21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Login_Admin__admin21", None)
        self.__admin21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login_Admin20"):
                opp_val = getattr(old_value, "login_Admin20", None)
                if opp_val == self:
                    setattr(old_value, "login_Admin20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login_Admin20"):
                opp_val = getattr(value, "login_Admin20", None)
                setattr(value, "login_Admin20", self)

