from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class keluar:

    def __init__(self, pembeli: pelanggan):
        self.pembeli = pembeli
        
        pass
    @property
    def pembeli(self):
        return self.__pembeli
    @pembeli.setter
    def pembeli(self, pembeli: pelanggan):
        self.__pembeli = pembeli



class masuk:

    def __init__(self, penyuplai: supplier):
        self.penyuplai = penyuplai
        
        pass
    @property
    def penyuplai(self):
        return self.__penyuplai
    @penyuplai.setter
    def penyuplai(self, penyuplai: supplier):
        self.__penyuplai = penyuplai



class sistem:

    def __init__(self, user: str, barang: barang, supplier: supplier, user1: "user" = None, barang27: "barang" = None, supplier29: "supplier" = None, transaksi10: "transaksi" = None):
        self.user = user
        self.barang = barang
        self.supplier = supplier
        self.user1 = user1
        self.barang27 = barang27
        self.supplier29 = supplier29
        self.transaksi10 = transaksi10
        
        pass
    @property
    def barang(self):
        return self.__barang
    @barang.setter
    def barang(self, barang: barang):
        self.__barang = barang

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def supplier(self):
        return self.__supplier
    @supplier.setter
    def supplier(self, supplier: supplier):
        self.__supplier = supplier

    @property
    def user1(self):
        return self.__user1
    @user1.setter
    def user1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistem__user1", None)
        self.__user1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistem0"):
                opp_val = getattr(old_value, "sistem0", None)
                if opp_val == self:
                    setattr(old_value, "sistem0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistem0"):
                opp_val = getattr(value, "sistem0", None)
                setattr(value, "sistem0", self)

    @property
    def transaksi10(self):
        return self.__transaksi10
    @transaksi10.setter
    def transaksi10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistem__transaksi10", None)
        self.__transaksi10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistem11"):
                opp_val = getattr(old_value, "sistem11", None)
                if opp_val == self:
                    setattr(old_value, "sistem11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistem11"):
                opp_val = getattr(value, "sistem11", None)
                setattr(value, "sistem11", self)

    @property
    def supplier29(self):
        return self.__supplier29
    @supplier29.setter
    def supplier29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistem__supplier29", None)
        self.__supplier29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistem8"):
                opp_val = getattr(old_value, "sistem8", None)
                if opp_val == self:
                    setattr(old_value, "sistem8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistem8"):
                opp_val = getattr(value, "sistem8", None)
                setattr(value, "sistem8", self)

    @property
    def barang27(self):
        return self.__barang27
    @barang27.setter
    def barang27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sistem__barang27", None)
        self.__barang27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sistem6"):
                opp_val = getattr(old_value, "sistem6", None)
                if opp_val == self:
                    setattr(old_value, "sistem6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sistem6"):
                opp_val = getattr(value, "sistem6", None)
                setattr(value, "sistem6", self)



class transaksi:

    def __init__(self, id_transaksi: int, nama_barang: barang, total: int, tanggal: str, pelanggan3: "pelanggan" = None, supplier5: "supplier" = None, sistem11: "sistem" = None):
        self.id_transaksi = id_transaksi
        self.nama_barang = nama_barang
        self.total = total
        self.tanggal = tanggal
        self.pelanggan3 = pelanggan3
        self.supplier5 = supplier5
        self.sistem11 = sistem11
        
        pass
    @property
    def total(self):
        return self.__total
    @total.setter
    def total(self, total: int):
        self.__total = total

    @property
    def tanggal(self):
        return self.__tanggal
    @tanggal.setter
    def tanggal(self, tanggal: str):
        self.__tanggal = tanggal

    @property
    def id_transaksi(self):
        return self.__id_transaksi
    @id_transaksi.setter
    def id_transaksi(self, id_transaksi: int):
        self.__id_transaksi = id_transaksi

    @property
    def nama_barang(self):
        return self.__nama_barang
    @nama_barang.setter
    def nama_barang(self, nama_barang: barang):
        self.__nama_barang = nama_barang

    @property
    def sistem11(self):
        return self.__sistem11
    @sistem11.setter
    def sistem11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaksi__sistem11", None)
        self.__sistem11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaksi10"):
                opp_val = getattr(old_value, "transaksi10", None)
                if opp_val == self:
                    setattr(old_value, "transaksi10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaksi10"):
                opp_val = getattr(value, "transaksi10", None)
                setattr(value, "transaksi10", self)

    @property
    def pelanggan3(self):
        return self.__pelanggan3
    @pelanggan3.setter
    def pelanggan3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaksi__pelanggan3", None)
        self.__pelanggan3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaksi2"):
                opp_val = getattr(old_value, "transaksi2", None)
                if opp_val == self:
                    setattr(old_value, "transaksi2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaksi2"):
                opp_val = getattr(value, "transaksi2", None)
                setattr(value, "transaksi2", self)

    @property
    def supplier5(self):
        return self.__supplier5
    @supplier5.setter
    def supplier5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaksi__supplier5", None)
        self.__supplier5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaksi4"):
                opp_val = getattr(old_value, "transaksi4", None)
                if opp_val == self:
                    setattr(old_value, "transaksi4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaksi4"):
                opp_val = getattr(value, "transaksi4", None)
                setattr(value, "transaksi4", self)



class supplier:

    def __init__(self, id_supplier: int, nama_supplier: supplier, alamat: str, no_telp_supp: str, attribute: str, transaksi4: "transaksi" = None, sistem8: "sistem" = None):
        self.id_supplier = id_supplier
        self.nama_supplier = nama_supplier
        self.alamat = alamat
        self.no_telp_supp = no_telp_supp
        self.attribute = attribute
        self.transaksi4 = transaksi4
        self.sistem8 = sistem8
        
        pass
    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, alamat: str):
        self.__alamat = alamat

    @property
    def no_telp_supp(self):
        return self.__no_telp_supp
    @no_telp_supp.setter
    def no_telp_supp(self, no_telp_supp: str):
        self.__no_telp_supp = no_telp_supp

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def id_supplier(self):
        return self.__id_supplier
    @id_supplier.setter
    def id_supplier(self, id_supplier: int):
        self.__id_supplier = id_supplier

    @property
    def nama_supplier(self):
        return self.__nama_supplier
    @nama_supplier.setter
    def nama_supplier(self, nama_supplier: supplier):
        self.__nama_supplier = nama_supplier

    @property
    def sistem8(self):
        return self.__sistem8
    @sistem8.setter
    def sistem8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_supplier__sistem8", None)
        self.__sistem8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supplier29"):
                opp_val = getattr(old_value, "supplier29", None)
                if opp_val == self:
                    setattr(old_value, "supplier29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supplier29"):
                opp_val = getattr(value, "supplier29", None)
                setattr(value, "supplier29", self)

    @property
    def transaksi4(self):
        return self.__transaksi4
    @transaksi4.setter
    def transaksi4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_supplier__transaksi4", None)
        self.__transaksi4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "supplier5"):
                opp_val = getattr(old_value, "supplier5", None)
                if opp_val == self:
                    setattr(old_value, "supplier5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "supplier5"):
                opp_val = getattr(value, "supplier5", None)
                setattr(value, "supplier5", self)



class pelanggan:

    def __init__(self, id_pelanggan: int, nama_pelanggan: pelanggan, alamat: str, no_telp_pelanggan: str, transaksi2: "transaksi" = None):
        self.id_pelanggan = id_pelanggan
        self.nama_pelanggan = nama_pelanggan
        self.alamat = alamat
        self.no_telp_pelanggan = no_telp_pelanggan
        self.transaksi2 = transaksi2
        
        pass
    @property
    def id_pelanggan(self):
        return self.__id_pelanggan
    @id_pelanggan.setter
    def id_pelanggan(self, id_pelanggan: int):
        self.__id_pelanggan = id_pelanggan

    @property
    def alamat(self):
        return self.__alamat
    @alamat.setter
    def alamat(self, alamat: str):
        self.__alamat = alamat

    @property
    def no_telp_pelanggan(self):
        return self.__no_telp_pelanggan
    @no_telp_pelanggan.setter
    def no_telp_pelanggan(self, no_telp_pelanggan: str):
        self.__no_telp_pelanggan = no_telp_pelanggan

    @property
    def nama_pelanggan(self):
        return self.__nama_pelanggan
    @nama_pelanggan.setter
    def nama_pelanggan(self, nama_pelanggan: pelanggan):
        self.__nama_pelanggan = nama_pelanggan

    @property
    def transaksi2(self):
        return self.__transaksi2
    @transaksi2.setter
    def transaksi2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pelanggan__transaksi2", None)
        self.__transaksi2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pelanggan3"):
                opp_val = getattr(old_value, "pelanggan3", None)
                if opp_val == self:
                    setattr(old_value, "pelanggan3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pelanggan3"):
                opp_val = getattr(value, "pelanggan3", None)
                setattr(value, "pelanggan3", self)



class user:

    def __init__(self, id_user: int, username: str, password: str, nama_user: str, sistem0: "sistem" = None):
        self.id_user = id_user
        self.username = username
        self.password = password
        self.nama_user = nama_user
        self.sistem0 = sistem0
        
        pass
    @property
    def id_user(self):
        return self.__id_user
    @id_user.setter
    def id_user(self, id_user: int):
        self.__id_user = id_user

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def nama_user(self):
        return self.__nama_user
    @nama_user.setter
    def nama_user(self, nama_user: str):
        self.__nama_user = nama_user

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def sistem0(self):
        return self.__sistem0
    @sistem0.setter
    def sistem0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__sistem0", None)
        self.__sistem0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "user1"):
                opp_val = getattr(old_value, "user1", None)
                if opp_val == self:
                    setattr(old_value, "user1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "user1"):
                opp_val = getattr(value, "user1", None)
                setattr(value, "user1", self)



class barang:

    def __init__(self, id_barang: str, nama_barang: barang, kategori: str, stok: int, harga: int, satuan: str, sistem6: "sistem" = None):
        self.id_barang = id_barang
        self.nama_barang = nama_barang
        self.kategori = kategori
        self.stok = stok
        self.harga = harga
        self.satuan = satuan
        self.sistem6 = sistem6
        
        pass
    @property
    def id_barang(self):
        return self.__id_barang
    @id_barang.setter
    def id_barang(self, id_barang: str):
        self.__id_barang = id_barang

    @property
    def stok(self):
        return self.__stok
    @stok.setter
    def stok(self, stok: int):
        self.__stok = stok

    @property
    def nama_barang(self):
        return self.__nama_barang
    @nama_barang.setter
    def nama_barang(self, nama_barang: barang):
        self.__nama_barang = nama_barang

    @property
    def harga(self):
        return self.__harga
    @harga.setter
    def harga(self, harga: int):
        self.__harga = harga

    @property
    def kategori(self):
        return self.__kategori
    @kategori.setter
    def kategori(self, kategori: str):
        self.__kategori = kategori

    @property
    def satuan(self):
        return self.__satuan
    @satuan.setter
    def satuan(self, satuan: str):
        self.__satuan = satuan

    @property
    def sistem6(self):
        return self.__sistem6
    @sistem6.setter
    def sistem6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_barang__sistem6", None)
        self.__sistem6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "barang27"):
                opp_val = getattr(old_value, "barang27", None)
                if opp_val == self:
                    setattr(old_value, "barang27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "barang27"):
                opp_val = getattr(value, "barang27", None)
                setattr(value, "barang27", self)

