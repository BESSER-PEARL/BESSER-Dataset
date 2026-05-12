from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class Enumeration(Enum):
    pass

############################################
# Definition of Classes
############################################







class Register_UseCase:

    pass


class Login_UseCase:

    pass


class Kamar_Standard_UseCase:

    pass


class Kamar_Keluarga_UseCase:

    pass


class Kamar_Deluxe_UseCase:

    pass


class Denda_UseCase:

    pass


class Check_Out_UseCase:

    pass


class Check_in_UseCase:

    pass


class Cancel_Pemesanan_UseCase:

    pass


class Melakukan_pembayaran_UseCase:

    pass


class Kirim_e_booking_email_UseCase:

    pass


class Mengirim_e_bukti_Bayar_UseCase:

    pass


class Melakukan_reservasi_kamar_UseCase:

    pass


class Admin_Actor:

    pass


class Pemesan_Actor:

    pass


class Melihat_Katalog_Kamar_UseCase:

    pass


class Pengunjung_Actor:

    pass





class Denda:

    def __init__(self, ID_Denda: int, jumlah: int, keterangan: str, ID_Reservasi: int, reservasiKamar30: "ReservasiKamar" = None):
        self.ID_Denda = ID_Denda
        self.jumlah = jumlah
        self.keterangan = keterangan
        self.ID_Reservasi = ID_Reservasi
        self.reservasiKamar30 = reservasiKamar30
        
        pass
    @property
    def jumlah(self):
        return self.__jumlah
    @jumlah.setter
    def jumlah(self, jumlah: int):
        self.__jumlah = jumlah

    @property
    def ID_Denda(self):
        return self.__ID_Denda
    @ID_Denda.setter
    def ID_Denda(self, ID_Denda: int):
        self.__ID_Denda = ID_Denda

    @property
    def ID_Reservasi(self):
        return self.__ID_Reservasi
    @ID_Reservasi.setter
    def ID_Reservasi(self, ID_Reservasi: int):
        self.__ID_Reservasi = ID_Reservasi

    @property
    def keterangan(self):
        return self.__keterangan
    @keterangan.setter
    def keterangan(self, keterangan: str):
        self.__keterangan = keterangan

    @property
    def reservasiKamar30(self):
        return self.__reservasiKamar30
    @reservasiKamar30.setter
    def reservasiKamar30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Denda__reservasiKamar30", None)
        self.__reservasiKamar30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "denda31"):
                opp_val = getattr(old_value, "denda31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "denda31"):
                opp_val = getattr(value, "denda31", None)
                if opp_val is None:
                    setattr(value, "denda31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Pembayaran:

    def __init__(self, ID_Pembayaran: int, ID_Reservasi: int, jumlah: int, deadline_bayar: str, status: str, reservasiKamar32: "ReservasiKamar" = None):
        self.ID_Pembayaran = ID_Pembayaran
        self.ID_Reservasi = ID_Reservasi
        self.jumlah = jumlah
        self.deadline_bayar = deadline_bayar
        self.status = status
        self.reservasiKamar32 = reservasiKamar32
        
        pass
    @property
    def ID_Pembayaran(self):
        return self.__ID_Pembayaran
    @ID_Pembayaran.setter
    def ID_Pembayaran(self, ID_Pembayaran: int):
        self.__ID_Pembayaran = ID_Pembayaran

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def ID_Reservasi(self):
        return self.__ID_Reservasi
    @ID_Reservasi.setter
    def ID_Reservasi(self, ID_Reservasi: int):
        self.__ID_Reservasi = ID_Reservasi

    @property
    def jumlah(self):
        return self.__jumlah
    @jumlah.setter
    def jumlah(self, jumlah: int):
        self.__jumlah = jumlah

    @property
    def deadline_bayar(self):
        return self.__deadline_bayar
    @deadline_bayar.setter
    def deadline_bayar(self, deadline_bayar: str):
        self.__deadline_bayar = deadline_bayar

    @property
    def reservasiKamar32(self):
        return self.__reservasiKamar32
    @reservasiKamar32.setter
    def reservasiKamar32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pembayaran__reservasiKamar32", None)
        self.__reservasiKamar32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pembayaran33"):
                opp_val = getattr(old_value, "pembayaran33", None)
                if opp_val == self:
                    setattr(old_value, "pembayaran33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pembayaran33"):
                opp_val = getattr(value, "pembayaran33", None)
                setattr(value, "pembayaran33", self)



class ReservasiKamar:

    def __init__(self, ID_Reservasi: int, NIK: int, tgl_start_booking: str, tgl_end_booking: str, no_kamar: int, ID_admin: int, ID_pembayaran: int, pemesan25: "Pemesan" = None, admin26: "Admin" = None, kamar29: "Kamar" = None, denda31: set["Denda"] = None, pembayaran33: "Pembayaran" = None):
        self.ID_Reservasi = ID_Reservasi
        self.NIK = NIK
        self.tgl_start_booking = tgl_start_booking
        self.tgl_end_booking = tgl_end_booking
        self.no_kamar = no_kamar
        self.ID_admin = ID_admin
        self.ID_pembayaran = ID_pembayaran
        self.pemesan25 = pemesan25
        self.admin26 = admin26
        self.kamar29 = kamar29
        self.denda31 = denda31 if denda31 is not None else set()
        self.pembayaran33 = pembayaran33
        
        pass
    @property
    def no_kamar(self):
        return self.__no_kamar
    @no_kamar.setter
    def no_kamar(self, no_kamar: int):
        self.__no_kamar = no_kamar

    @property
    def tgl_end_booking(self):
        return self.__tgl_end_booking
    @tgl_end_booking.setter
    def tgl_end_booking(self, tgl_end_booking: str):
        self.__tgl_end_booking = tgl_end_booking

    @property
    def tgl_start_booking(self):
        return self.__tgl_start_booking
    @tgl_start_booking.setter
    def tgl_start_booking(self, tgl_start_booking: str):
        self.__tgl_start_booking = tgl_start_booking

    @property
    def ID_pembayaran(self):
        return self.__ID_pembayaran
    @ID_pembayaran.setter
    def ID_pembayaran(self, ID_pembayaran: int):
        self.__ID_pembayaran = ID_pembayaran

    @property
    def ID_Reservasi(self):
        return self.__ID_Reservasi
    @ID_Reservasi.setter
    def ID_Reservasi(self, ID_Reservasi: int):
        self.__ID_Reservasi = ID_Reservasi

    @property
    def ID_admin(self):
        return self.__ID_admin
    @ID_admin.setter
    def ID_admin(self, ID_admin: int):
        self.__ID_admin = ID_admin

    @property
    def NIK(self):
        return self.__NIK
    @NIK.setter
    def NIK(self, NIK: int):
        self.__NIK = NIK

    @property
    def pemesan25(self):
        return self.__pemesan25
    @pemesan25.setter
    def pemesan25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservasiKamar__pemesan25", None)
        self.__pemesan25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservasiKamar24"):
                opp_val = getattr(old_value, "reservasiKamar24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservasiKamar24"):
                opp_val = getattr(value, "reservasiKamar24", None)
                if opp_val is None:
                    setattr(value, "reservasiKamar24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kamar29(self):
        return self.__kamar29
    @kamar29.setter
    def kamar29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservasiKamar__kamar29", None)
        self.__kamar29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservasiKamar28"):
                opp_val = getattr(old_value, "reservasiKamar28", None)
                if opp_val == self:
                    setattr(old_value, "reservasiKamar28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservasiKamar28"):
                opp_val = getattr(value, "reservasiKamar28", None)
                setattr(value, "reservasiKamar28", self)

    @property
    def denda31(self):
        return self.__denda31
    @denda31.setter
    def denda31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservasiKamar__denda31", None)
        self.__denda31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "reservasiKamar30"):
                    opp_val = getattr(item, "reservasiKamar30", None)
                    
                    if opp_val == self:
                        setattr(item, "reservasiKamar30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "reservasiKamar30"):
                    opp_val = getattr(item, "reservasiKamar30", None)
                    
                    setattr(item, "reservasiKamar30", self)
                    

    @property
    def admin26(self):
        return self.__admin26
    @admin26.setter
    def admin26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservasiKamar__admin26", None)
        self.__admin26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservasiKamar27"):
                opp_val = getattr(old_value, "reservasiKamar27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservasiKamar27"):
                opp_val = getattr(value, "reservasiKamar27", None)
                if opp_val is None:
                    setattr(value, "reservasiKamar27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pembayaran33(self):
        return self.__pembayaran33
    @pembayaran33.setter
    def pembayaran33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ReservasiKamar__pembayaran33", None)
        self.__pembayaran33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "reservasiKamar32"):
                opp_val = getattr(old_value, "reservasiKamar32", None)
                if opp_val == self:
                    setattr(old_value, "reservasiKamar32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "reservasiKamar32"):
                opp_val = getattr(value, "reservasiKamar32", None)
                setattr(value, "reservasiKamar32", self)



class Kamar:

    def __init__(self, _attr: str, no_kamar: int, tipe: str, status: str, jumlah_bed: int, reservasiKamar28: "ReservasiKamar" = None):
        self._attr = _attr
        self.no_kamar = no_kamar
        self.tipe = tipe
        self.status = status
        self.jumlah_bed = jumlah_bed
        self.reservasiKamar28 = reservasiKamar28
        
        pass
    @property
    def jumlah_bed(self):
        return self.__jumlah_bed
    @jumlah_bed.setter
    def jumlah_bed(self, jumlah_bed: int):
        self.__jumlah_bed = jumlah_bed

    @property
    def no_kamar(self):
        return self.__no_kamar
    @no_kamar.setter
    def no_kamar(self, no_kamar: int):
        self.__no_kamar = no_kamar

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def tipe(self):
        return self.__tipe
    @tipe.setter
    def tipe(self, tipe: str):
        self.__tipe = tipe

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def reservasiKamar28(self):
        return self.__reservasiKamar28
    @reservasiKamar28.setter
    def reservasiKamar28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kamar__reservasiKamar28", None)
        self.__reservasiKamar28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kamar29"):
                opp_val = getattr(old_value, "kamar29", None)
                if opp_val == self:
                    setattr(old_value, "kamar29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kamar29"):
                opp_val = getattr(value, "kamar29", None)
                setattr(value, "kamar29", self)



class hjb_Interface:

    pass


class Admin:

    def __init__(self, ID_admin: int, username: str, password: str, insertData: str, attribute: str, reservasiKamar27: set["ReservasiKamar"] = None):
        self.ID_admin = ID_admin
        self.username = username
        self.password = password
        self.insertData = insertData
        self.attribute = attribute
        self.reservasiKamar27 = reservasiKamar27 if reservasiKamar27 is not None else set()
        
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

    @property
    def insertData(self):
        return self.__insertData
    @insertData.setter
    def insertData(self, insertData: str):
        self.__insertData = insertData

    @property
    def ID_admin(self):
        return self.__ID_admin
    @ID_admin.setter
    def ID_admin(self, ID_admin: int):
        self.__ID_admin = ID_admin

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def reservasiKamar27(self):
        return self.__reservasiKamar27
    @reservasiKamar27.setter
    def reservasiKamar27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__reservasiKamar27", None)
        self.__reservasiKamar27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin26"):
                    opp_val = getattr(item, "admin26", None)
                    
                    if opp_val == self:
                        setattr(item, "admin26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin26"):
                    opp_val = getattr(item, "admin26", None)
                    
                    setattr(item, "admin26", self)
                    



class Pemesan:

    def __init__(self, NIK: int, Nama: str, Alamat: str, Emai: str, username: str, password: str, phone_number: str, reservasiKamar24: set["ReservasiKamar"] = None):
        self.NIK = NIK
        self.Nama = Nama
        self.Alamat = Alamat
        self.Emai = Emai
        self.username = username
        self.password = password
        self.phone_number = phone_number
        self.reservasiKamar24 = reservasiKamar24 if reservasiKamar24 is not None else set()
        
        pass
    @property
    def Alamat(self):
        return self.__Alamat
    @Alamat.setter
    def Alamat(self, Alamat: str):
        self.__Alamat = Alamat

    @property
    def Emai(self):
        return self.__Emai
    @Emai.setter
    def Emai(self, Emai: str):
        self.__Emai = Emai

    @property
    def phone_number(self):
        return self.__phone_number
    @phone_number.setter
    def phone_number(self, phone_number: str):
        self.__phone_number = phone_number

    @property
    def NIK(self):
        return self.__NIK
    @NIK.setter
    def NIK(self, NIK: int):
        self.__NIK = NIK

    @property
    def Nama(self):
        return self.__Nama
    @Nama.setter
    def Nama(self, Nama: str):
        self.__Nama = Nama

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

    @property
    def reservasiKamar24(self):
        return self.__reservasiKamar24
    @reservasiKamar24.setter
    def reservasiKamar24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pemesan__reservasiKamar24", None)
        self.__reservasiKamar24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pemesan25"):
                    opp_val = getattr(item, "pemesan25", None)
                    
                    if opp_val == self:
                        setattr(item, "pemesan25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pemesan25"):
                    opp_val = getattr(item, "pemesan25", None)
                    
                    setattr(item, "pemesan25", self)
                    

