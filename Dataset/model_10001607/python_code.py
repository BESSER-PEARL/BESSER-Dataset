from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class HasilBidding:

    pass


class Bidding:

    def __init__(self, biddee: str, bidder: str, statusBidding: str, jabatan: str, notulensi: str, nilai: int, catatanBidder: str, berkas: str, bidder29: set["Bidder"] = None, Bidder_Bidding2_111: set["Bidder"] = None, hasilBidding1: "HasilBidding" = None, CRUD_bidding3: "Admin" = None, daftar4: set["Biddee"] = None):
        self.biddee = biddee
        self.bidder = bidder
        self.statusBidding = statusBidding
        self.jabatan = jabatan
        self.notulensi = notulensi
        self.nilai = nilai
        self.catatanBidder = catatanBidder
        self.berkas = berkas
        self.bidder29 = bidder29 if bidder29 is not None else set()
        self.Bidder_Bidding2_111 = Bidder_Bidding2_111 if Bidder_Bidding2_111 is not None else set()
        self.hasilBidding1 = hasilBidding1
        self.CRUD_bidding3 = CRUD_bidding3
        self.daftar4 = daftar4 if daftar4 is not None else set()
        
        pass
    @property
    def jabatan(self):
        return self.__jabatan
    @jabatan.setter
    def jabatan(self, jabatan: str):
        self.__jabatan = jabatan

    @property
    def statusBidding(self):
        return self.__statusBidding
    @statusBidding.setter
    def statusBidding(self, statusBidding: str):
        self.__statusBidding = statusBidding

    @property
    def nilai(self):
        return self.__nilai
    @nilai.setter
    def nilai(self, nilai: int):
        self.__nilai = nilai

    @property
    def biddee(self):
        return self.__biddee
    @biddee.setter
    def biddee(self, biddee: str):
        self.__biddee = biddee

    @property
    def notulensi(self):
        return self.__notulensi
    @notulensi.setter
    def notulensi(self, notulensi: str):
        self.__notulensi = notulensi

    @property
    def bidder(self):
        return self.__bidder
    @bidder.setter
    def bidder(self, bidder: str):
        self.__bidder = bidder

    @property
    def berkas(self):
        return self.__berkas
    @berkas.setter
    def berkas(self, berkas: str):
        self.__berkas = berkas

    @property
    def catatanBidder(self):
        return self.__catatanBidder
    @catatanBidder.setter
    def catatanBidder(self, catatanBidder: str):
        self.__catatanBidder = catatanBidder

    @property
    def bidder29(self):
        return self.__bidder29
    @bidder29.setter
    def bidder29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bidding__bidder29", None)
        self.__bidder29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "buat_catatan8"):
                    opp_val = getattr(item, "buat_catatan8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "buat_catatan8"):
                    opp_val = getattr(item, "buat_catatan8", None)
                    
                    if opp_val is None:
                        setattr(item, "buat_catatan8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def daftar4(self):
        return self.__daftar4
    @daftar4.setter
    def daftar4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bidding__daftar4", None)
        self.__daftar4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bidding5"):
                    opp_val = getattr(item, "bidding5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bidding5"):
                    opp_val = getattr(item, "bidding5", None)
                    
                    if opp_val is None:
                        setattr(item, "bidding5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Bidder_Bidding2_111(self):
        return self.__Bidder_Bidding2_111
    @Bidder_Bidding2_111.setter
    def Bidder_Bidding2_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bidding__Bidder_Bidding2_111", None)
        self.__Bidder_Bidding2_111 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "edit_nilai10"):
                    opp_val = getattr(item, "edit_nilai10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "edit_nilai10"):
                    opp_val = getattr(item, "edit_nilai10", None)
                    
                    if opp_val is None:
                        setattr(item, "edit_nilai10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def hasilBidding1(self):
        return self.__hasilBidding1
    @hasilBidding1.setter
    def hasilBidding1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bidding__hasilBidding1", None)
        self.__hasilBidding1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bidding0"):
                opp_val = getattr(old_value, "bidding0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bidding0"):
                opp_val = getattr(value, "bidding0", None)
                if opp_val is None:
                    setattr(value, "bidding0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CRUD_bidding3(self):
        return self.__CRUD_bidding3
    @CRUD_bidding3.setter
    def CRUD_bidding3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bidding__CRUD_bidding3", None)
        self.__CRUD_bidding3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bidding2"):
                opp_val = getattr(old_value, "bidding2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bidding2"):
                opp_val = getattr(value, "bidding2", None)
                if opp_val is None:
                    setattr(value, "bidding2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Biddee:

    def __init__(self, statusBiddee: str, ubah_status7: "Admin" = None, bidding5: set["Bidding"] = None):
        self.statusBiddee = statusBiddee
        self.ubah_status7 = ubah_status7
        self.bidding5 = bidding5 if bidding5 is not None else set()
        
        pass
    @property
    def statusBiddee(self):
        return self.__statusBiddee
    @statusBiddee.setter
    def statusBiddee(self, statusBiddee: str):
        self.__statusBiddee = statusBiddee

    @property
    def ubah_status7(self):
        return self.__ubah_status7
    @ubah_status7.setter
    def ubah_status7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biddee__ubah_status7", None)
        self.__ubah_status7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "biddee6"):
                opp_val = getattr(old_value, "biddee6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "biddee6"):
                opp_val = getattr(value, "biddee6", None)
                if opp_val is None:
                    setattr(value, "biddee6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def bidding5(self):
        return self.__bidding5
    @bidding5.setter
    def bidding5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Biddee__bidding5", None)
        self.__bidding5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "daftar4"):
                    opp_val = getattr(item, "daftar4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "daftar4"):
                    opp_val = getattr(item, "daftar4", None)
                    
                    if opp_val is None:
                        setattr(item, "daftar4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Bidder:

    pass


class Admin:

    pass


class User:

    def __init__(self, userName: str, password: str, loginStatus: str, nama: str, hasilBidding12: set["HasilBidding"] = None):
        self.userName = userName
        self.password = password
        self.loginStatus = loginStatus
        self.nama = nama
        self.hasilBidding12 = hasilBidding12 if hasilBidding12 is not None else set()
        
        pass
    @property
    def loginStatus(self):
        return self.__loginStatus
    @loginStatus.setter
    def loginStatus(self, loginStatus: str):
        self.__loginStatus = loginStatus

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def userName(self):
        return self.__userName
    @userName.setter
    def userName(self, userName: str):
        self.__userName = userName

    @property
    def nama(self):
        return self.__nama
    @nama.setter
    def nama(self, nama: str):
        self.__nama = nama

    @property
    def hasilBidding12(self):
        return self.__hasilBidding12
    @hasilBidding12.setter
    def hasilBidding12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_User__hasilBidding12", None)
        self.__hasilBidding12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "melihat13"):
                    opp_val = getattr(item, "melihat13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "melihat13"):
                    opp_val = getattr(item, "melihat13", None)
                    
                    if opp_val is None:
                        setattr(item, "melihat13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

