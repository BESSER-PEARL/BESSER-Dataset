from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Kendaraan:

    def __init__(self, NoMesin: str, NoRangka: str, NoPolisi: str, Merk: str, Warna: str, TahunPembuatan: str, pelanggan5: "Pelanggan" = None, pesan6: "Pesan" = None):
        self.NoMesin = NoMesin
        self.NoRangka = NoRangka
        self.NoPolisi = NoPolisi
        self.Merk = Merk
        self.Warna = Warna
        self.TahunPembuatan = TahunPembuatan
        self.pelanggan5 = pelanggan5
        self.pesan6 = pesan6
        
        pass
    @property
    def Merk(self):
        return self.__Merk
    @Merk.setter
    def Merk(self, Merk: str):
        self.__Merk = Merk

    @property
    def NoRangka(self):
        return self.__NoRangka
    @NoRangka.setter
    def NoRangka(self, NoRangka: str):
        self.__NoRangka = NoRangka

    @property
    def Warna(self):
        return self.__Warna
    @Warna.setter
    def Warna(self, Warna: str):
        self.__Warna = Warna

    @property
    def TahunPembuatan(self):
        return self.__TahunPembuatan
    @TahunPembuatan.setter
    def TahunPembuatan(self, TahunPembuatan: str):
        self.__TahunPembuatan = TahunPembuatan

    @property
    def NoPolisi(self):
        return self.__NoPolisi
    @NoPolisi.setter
    def NoPolisi(self, NoPolisi: str):
        self.__NoPolisi = NoPolisi

    @property
    def NoMesin(self):
        return self.__NoMesin
    @NoMesin.setter
    def NoMesin(self, NoMesin: str):
        self.__NoMesin = NoMesin

    @property
    def pesan6(self):
        return self.__pesan6
    @pesan6.setter
    def pesan6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kendaraan__pesan6", None)
        self.__pesan6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kendaraan7"):
                opp_val = getattr(old_value, "kendaraan7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kendaraan7"):
                opp_val = getattr(value, "kendaraan7", None)
                if opp_val is None:
                    setattr(value, "kendaraan7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pelanggan5(self):
        return self.__pelanggan5
    @pelanggan5.setter
    def pelanggan5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Kendaraan__pelanggan5", None)
        self.__pelanggan5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kendaraan4"):
                opp_val = getattr(old_value, "kendaraan4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kendaraan4"):
                opp_val = getattr(value, "kendaraan4", None)
                if opp_val is None:
                    setattr(value, "kendaraan4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Pesan:

    def __init__(self, NoPesan: int, IdPelanggan: int, TanggalRental: str, TanggalKembali: str, kendaraan7: set["Kendaraan"] = None, administrasi9: "Administrasi" = None, pelanggan11: "Pelanggan" = None, admin13: "Admin" = None):
        self.NoPesan = NoPesan
        self.IdPelanggan = IdPelanggan
        self.TanggalRental = TanggalRental
        self.TanggalKembali = TanggalKembali
        self.kendaraan7 = kendaraan7 if kendaraan7 is not None else set()
        self.administrasi9 = administrasi9
        self.pelanggan11 = pelanggan11
        self.admin13 = admin13
        
        pass
    @property
    def TanggalKembali(self):
        return self.__TanggalKembali
    @TanggalKembali.setter
    def TanggalKembali(self, TanggalKembali: str):
        self.__TanggalKembali = TanggalKembali

    @property
    def NoPesan(self):
        return self.__NoPesan
    @NoPesan.setter
    def NoPesan(self, NoPesan: int):
        self.__NoPesan = NoPesan

    @property
    def IdPelanggan(self):
        return self.__IdPelanggan
    @IdPelanggan.setter
    def IdPelanggan(self, IdPelanggan: int):
        self.__IdPelanggan = IdPelanggan

    @property
    def TanggalRental(self):
        return self.__TanggalRental
    @TanggalRental.setter
    def TanggalRental(self, TanggalRental: str):
        self.__TanggalRental = TanggalRental

    @property
    def kendaraan7(self):
        return self.__kendaraan7
    @kendaraan7.setter
    def kendaraan7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pesan__kendaraan7", None)
        self.__kendaraan7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pesan6"):
                    opp_val = getattr(item, "pesan6", None)
                    
                    if opp_val == self:
                        setattr(item, "pesan6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pesan6"):
                    opp_val = getattr(item, "pesan6", None)
                    
                    setattr(item, "pesan6", self)
                    

    @property
    def admin13(self):
        return self.__admin13
    @admin13.setter
    def admin13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pesan__admin13", None)
        self.__admin13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pesan12"):
                opp_val = getattr(old_value, "pesan12", None)
                if opp_val == self:
                    setattr(old_value, "pesan12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pesan12"):
                opp_val = getattr(value, "pesan12", None)
                setattr(value, "pesan12", self)

    @property
    def pelanggan11(self):
        return self.__pelanggan11
    @pelanggan11.setter
    def pelanggan11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pesan__pelanggan11", None)
        self.__pelanggan11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pesan10"):
                opp_val = getattr(old_value, "pesan10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pesan10"):
                opp_val = getattr(value, "pesan10", None)
                if opp_val is None:
                    setattr(value, "pesan10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def administrasi9(self):
        return self.__administrasi9
    @administrasi9.setter
    def administrasi9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pesan__administrasi9", None)
        self.__administrasi9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pesan8"):
                opp_val = getattr(old_value, "pesan8", None)
                if opp_val == self:
                    setattr(old_value, "pesan8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pesan8"):
                opp_val = getattr(value, "pesan8", None)
                setattr(value, "pesan8", self)



class Administrasi:

    def __init__(self, IdAdmin: int, NoPesan: int, IdPelanggan: int, HargaSewa: str, Bayar: str, Kembali: str, pesan8: "Pesan" = None, admin15: "Admin" = None):
        self.IdAdmin = IdAdmin
        self.NoPesan = NoPesan
        self.IdPelanggan = IdPelanggan
        self.HargaSewa = HargaSewa
        self.Bayar = Bayar
        self.Kembali = Kembali
        self.pesan8 = pesan8
        self.admin15 = admin15
        
        pass
    @property
    def IdPelanggan(self):
        return self.__IdPelanggan
    @IdPelanggan.setter
    def IdPelanggan(self, IdPelanggan: int):
        self.__IdPelanggan = IdPelanggan

    @property
    def Bayar(self):
        return self.__Bayar
    @Bayar.setter
    def Bayar(self, Bayar: str):
        self.__Bayar = Bayar

    @property
    def HargaSewa(self):
        return self.__HargaSewa
    @HargaSewa.setter
    def HargaSewa(self, HargaSewa: str):
        self.__HargaSewa = HargaSewa

    @property
    def NoPesan(self):
        return self.__NoPesan
    @NoPesan.setter
    def NoPesan(self, NoPesan: int):
        self.__NoPesan = NoPesan

    @property
    def Kembali(self):
        return self.__Kembali
    @Kembali.setter
    def Kembali(self, Kembali: str):
        self.__Kembali = Kembali

    @property
    def IdAdmin(self):
        return self.__IdAdmin
    @IdAdmin.setter
    def IdAdmin(self, IdAdmin: int):
        self.__IdAdmin = IdAdmin

    @property
    def admin15(self):
        return self.__admin15
    @admin15.setter
    def admin15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrasi__admin15", None)
        self.__admin15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrasi14"):
                opp_val = getattr(old_value, "administrasi14", None)
                if opp_val == self:
                    setattr(old_value, "administrasi14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrasi14"):
                opp_val = getattr(value, "administrasi14", None)
                setattr(value, "administrasi14", self)

    @property
    def pesan8(self):
        return self.__pesan8
    @pesan8.setter
    def pesan8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrasi__pesan8", None)
        self.__pesan8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrasi9"):
                opp_val = getattr(old_value, "administrasi9", None)
                if opp_val == self:
                    setattr(old_value, "administrasi9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrasi9"):
                opp_val = getattr(value, "administrasi9", None)
                setattr(value, "administrasi9", self)



class Pelanggan:

    def __init__(self, Username: str, Password: str, IdPelanggan: int, NoKTP: str, JenisKelamin: str, Umur: int, Pekerjaan: str, Alamat: str, Telepon: str, admin3: "Admin" = None, kendaraan4: set["Kendaraan"] = None, pesan10: set["Pesan"] = None):
        self.Username = Username
        self.Password = Password
        self.IdPelanggan = IdPelanggan
        self.NoKTP = NoKTP
        self.JenisKelamin = JenisKelamin
        self.Umur = Umur
        self.Pekerjaan = Pekerjaan
        self.Alamat = Alamat
        self.Telepon = Telepon
        self.admin3 = admin3
        self.kendaraan4 = kendaraan4 if kendaraan4 is not None else set()
        self.pesan10 = pesan10 if pesan10 is not None else set()
        
        pass
    @property
    def Alamat(self):
        return self.__Alamat
    @Alamat.setter
    def Alamat(self, Alamat: str):
        self.__Alamat = Alamat

    @property
    def Umur(self):
        return self.__Umur
    @Umur.setter
    def Umur(self, Umur: int):
        self.__Umur = Umur

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def Telepon(self):
        return self.__Telepon
    @Telepon.setter
    def Telepon(self, Telepon: str):
        self.__Telepon = Telepon

    @property
    def NoKTP(self):
        return self.__NoKTP
    @NoKTP.setter
    def NoKTP(self, NoKTP: str):
        self.__NoKTP = NoKTP

    @property
    def JenisKelamin(self):
        return self.__JenisKelamin
    @JenisKelamin.setter
    def JenisKelamin(self, JenisKelamin: str):
        self.__JenisKelamin = JenisKelamin

    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def IdPelanggan(self):
        return self.__IdPelanggan
    @IdPelanggan.setter
    def IdPelanggan(self, IdPelanggan: int):
        self.__IdPelanggan = IdPelanggan

    @property
    def Pekerjaan(self):
        return self.__Pekerjaan
    @Pekerjaan.setter
    def Pekerjaan(self, Pekerjaan: str):
        self.__Pekerjaan = Pekerjaan

    @property
    def pesan10(self):
        return self.__pesan10
    @pesan10.setter
    def pesan10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pelanggan__pesan10", None)
        self.__pesan10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pelanggan11"):
                    opp_val = getattr(item, "pelanggan11", None)
                    
                    if opp_val == self:
                        setattr(item, "pelanggan11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pelanggan11"):
                    opp_val = getattr(item, "pelanggan11", None)
                    
                    setattr(item, "pelanggan11", self)
                    

    @property
    def admin3(self):
        return self.__admin3
    @admin3.setter
    def admin3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pelanggan__admin3", None)
        self.__admin3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pelanggan2"):
                opp_val = getattr(old_value, "pelanggan2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pelanggan2"):
                opp_val = getattr(value, "pelanggan2", None)
                if opp_val is None:
                    setattr(value, "pelanggan2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def kendaraan4(self):
        return self.__kendaraan4
    @kendaraan4.setter
    def kendaraan4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pelanggan__kendaraan4", None)
        self.__kendaraan4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pelanggan5"):
                    opp_val = getattr(item, "pelanggan5", None)
                    
                    if opp_val == self:
                        setattr(item, "pelanggan5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pelanggan5"):
                    opp_val = getattr(item, "pelanggan5", None)
                    
                    setattr(item, "pelanggan5", self)
                    



class Admin:

    def __init__(self, Username: str, Password: str, pelanggan2: set["Pelanggan"] = None, pesan12: "Pesan" = None, administrasi14: "Administrasi" = None, pemilik1: "Pemilik" = None):
        self.Username = Username
        self.Password = Password
        self.pelanggan2 = pelanggan2 if pelanggan2 is not None else set()
        self.pesan12 = pesan12
        self.administrasi14 = administrasi14
        self.pemilik1 = pemilik1
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def pemilik1(self):
        return self.__pemilik1
    @pemilik1.setter
    def pemilik1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__pemilik1", None)
        self.__pemilik1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin0"):
                opp_val = getattr(old_value, "admin0", None)
                if opp_val == self:
                    setattr(old_value, "admin0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin0"):
                opp_val = getattr(value, "admin0", None)
                setattr(value, "admin0", self)

    @property
    def pelanggan2(self):
        return self.__pelanggan2
    @pelanggan2.setter
    def pelanggan2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__pelanggan2", None)
        self.__pelanggan2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin3"):
                    opp_val = getattr(item, "admin3", None)
                    
                    if opp_val == self:
                        setattr(item, "admin3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin3"):
                    opp_val = getattr(item, "admin3", None)
                    
                    setattr(item, "admin3", self)
                    

    @property
    def administrasi14(self):
        return self.__administrasi14
    @administrasi14.setter
    def administrasi14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__administrasi14", None)
        self.__administrasi14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin15"):
                opp_val = getattr(old_value, "admin15", None)
                if opp_val == self:
                    setattr(old_value, "admin15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin15"):
                opp_val = getattr(value, "admin15", None)
                setattr(value, "admin15", self)

    @property
    def pesan12(self):
        return self.__pesan12
    @pesan12.setter
    def pesan12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__pesan12", None)
        self.__pesan12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin13"):
                opp_val = getattr(old_value, "admin13", None)
                if opp_val == self:
                    setattr(old_value, "admin13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin13"):
                opp_val = getattr(value, "admin13", None)
                setattr(value, "admin13", self)



class Pemilik:

    def __init__(self, Username: str, Password: str, admin0: "Admin" = None):
        self.Username = Username
        self.Password = Password
        self.admin0 = admin0
        
        pass
    @property
    def Username(self):
        return self.__Username
    @Username.setter
    def Username(self, Username: str):
        self.__Username = Username

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: str):
        self.__Password = Password

    @property
    def admin0(self):
        return self.__admin0
    @admin0.setter
    def admin0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pemilik__admin0", None)
        self.__admin0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pemilik1"):
                opp_val = getattr(old_value, "pemilik1", None)
                if opp_val == self:
                    setattr(old_value, "pemilik1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pemilik1"):
                opp_val = getattr(value, "pemilik1", None)
                setattr(value, "pemilik1", self)



class Login:

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



class RentalMobil:

    def __init__(self, Nama: str, Alamat: str, Telepon: str, Email: str):
        self.Nama = Nama
        self.Alamat = Alamat
        self.Telepon = Telepon
        self.Email = Email
        
        pass
    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def Nama(self):
        return self.__Nama
    @Nama.setter
    def Nama(self, Nama: str):
        self.__Nama = Nama

    @property
    def Alamat(self):
        return self.__Alamat
    @Alamat.setter
    def Alamat(self, Alamat: str):
        self.__Alamat = Alamat

    @property
    def Telepon(self):
        return self.__Telepon
    @Telepon.setter
    def Telepon(self, Telepon: str):
        self.__Telepon = Telepon

