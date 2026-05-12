from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Admin_Actor:

    pass


class Peserta_Actor:

    pass





class Tambah_Kota_external:

    pass


class Lihat_Peserta_Belum_Bayar_external:

    pass


class Lihat_Peserta_Sudah_Bayar_external:

    pass


class Lihat_Seluruh_Peserta_external:

    pass


class Tambah_Event_external:

    pass


class Update__isi__pertanyaan__make_it_better__external:

    pass


class Melihat_pertanyaan__make_it_better__external:

    pass


class Unduh_E_Ticket_external:

    pass


class Masuk_Link_Grup_Whatsapp_external:

    pass


class Beli_Tiket_external:

    pass


class Bayar_Tiket_external:

    pass


class Lihat_Detail_Event_external:

    pass


class Lihat_Event_external:

    pass


class Update_Profil_external:

    pass


class Logout_external:

    pass


class Registrasi_external:

    pass


class Lihat_Ringkasan_Transaksi_external:

    pass


class Lihat_Hasil_Jawaban__make_it_better__external:

    pass


class Tambah_Link_Grup_Whatsapp_external:

    pass


class bookmark:

    def __init__(self, id_bookmark: int, id_event: int, id_user: int, user54: "user" = None):
        self.id_bookmark = id_bookmark
        self.id_event = id_event
        self.id_user = id_user
        self.user54 = user54
        
        pass
    @property
    def id_user(self):
        return self.__id_user
    @id_user.setter
    def id_user(self, id_user: int):
        self.__id_user = id_user

    @property
    def id_event(self):
        return self.__id_event
    @id_event.setter
    def id_event(self, id_event: int):
        self.__id_event = id_event

    @property
    def id_bookmark(self):
        return self.__id_bookmark
    @id_bookmark.setter
    def id_bookmark(self, id_bookmark: int):
        self.__id_bookmark = id_bookmark

    @property
    def user54(self):
        return self.__user54
    @user54.setter
    def user54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bookmark__user54", None)
        self.__user54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bookmark55"):
                opp_val = getattr(old_value, "bookmark55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bookmark55"):
                opp_val = getattr(value, "bookmark55", None)
                if opp_val is None:
                    setattr(value, "bookmark55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class admin:

    def __init__(self, id_admin: int, username: str, password: str, testimoni56: set["testimoni"] = None, event58: set["event"] = None):
        self.id_admin = id_admin
        self.username = username
        self.password = password
        self.testimoni56 = testimoni56 if testimoni56 is not None else set()
        self.event58 = event58 if event58 is not None else set()
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def id_admin(self):
        return self.__id_admin
    @id_admin.setter
    def id_admin(self, id_admin: int):
        self.__id_admin = id_admin

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def event58(self):
        return self.__event58
    @event58.setter
    def event58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_admin__event58", None)
        self.__event58 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin59"):
                    opp_val = getattr(item, "admin59", None)
                    
                    if opp_val == self:
                        setattr(item, "admin59", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin59"):
                    opp_val = getattr(item, "admin59", None)
                    
                    setattr(item, "admin59", self)
                    

    @property
    def testimoni56(self):
        return self.__testimoni56
    @testimoni56.setter
    def testimoni56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_admin__testimoni56", None)
        self.__testimoni56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "admin57"):
                    opp_val = getattr(item, "admin57", None)
                    
                    if opp_val == self:
                        setattr(item, "admin57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "admin57"):
                    opp_val = getattr(item, "admin57", None)
                    
                    setattr(item, "admin57", self)
                    



class event:

    def __init__(self, detail: str, harga_reguler: int, harga_premium: int, tanggal: str, deskripsi: str, lokasi: str, latitude: str, longitude: str, gambar: str, id_event: int, id_kota: int, id_admin: int, nama_event: str, kota52: "kota" = None, admin59: "admin" = None, e_ticket60: "e_ticket" = None, transaksi49: set["transaksi"] = None):
        self.detail = detail
        self.harga_reguler = harga_reguler
        self.harga_premium = harga_premium
        self.tanggal = tanggal
        self.deskripsi = deskripsi
        self.lokasi = lokasi
        self.latitude = latitude
        self.longitude = longitude
        self.gambar = gambar
        self.id_event = id_event
        self.id_kota = id_kota
        self.id_admin = id_admin
        self.nama_event = nama_event
        self.kota52 = kota52
        self.admin59 = admin59
        self.e_ticket60 = e_ticket60
        self.transaksi49 = transaksi49 if transaksi49 is not None else set()
        
        pass
    @property
    def longitude(self):
        return self.__longitude
    @longitude.setter
    def longitude(self, longitude: str):
        self.__longitude = longitude

    @property
    def id_admin(self):
        return self.__id_admin
    @id_admin.setter
    def id_admin(self, id_admin: int):
        self.__id_admin = id_admin

    @property
    def id_event(self):
        return self.__id_event
    @id_event.setter
    def id_event(self, id_event: int):
        self.__id_event = id_event

    @property
    def detail(self):
        return self.__detail
    @detail.setter
    def detail(self, detail: str):
        self.__detail = detail

    @property
    def harga_premium(self):
        return self.__harga_premium
    @harga_premium.setter
    def harga_premium(self, harga_premium: int):
        self.__harga_premium = harga_premium

    @property
    def gambar(self):
        return self.__gambar
    @gambar.setter
    def gambar(self, gambar: str):
        self.__gambar = gambar

    @property
    def lokasi(self):
        return self.__lokasi
    @lokasi.setter
    def lokasi(self, lokasi: str):
        self.__lokasi = lokasi

    @property
    def latitude(self):
        return self.__latitude
    @latitude.setter
    def latitude(self, latitude: str):
        self.__latitude = latitude

    @property
    def harga_reguler(self):
        return self.__harga_reguler
    @harga_reguler.setter
    def harga_reguler(self, harga_reguler: int):
        self.__harga_reguler = harga_reguler

    @property
    def nama_event(self):
        return self.__nama_event
    @nama_event.setter
    def nama_event(self, nama_event: str):
        self.__nama_event = nama_event

    @property
    def id_kota(self):
        return self.__id_kota
    @id_kota.setter
    def id_kota(self, id_kota: int):
        self.__id_kota = id_kota

    @property
    def tanggal(self):
        return self.__tanggal
    @tanggal.setter
    def tanggal(self, tanggal: str):
        self.__tanggal = tanggal

    @property
    def deskripsi(self):
        return self.__deskripsi
    @deskripsi.setter
    def deskripsi(self, deskripsi: str):
        self.__deskripsi = deskripsi

    @property
    def kota52(self):
        return self.__kota52
    @kota52.setter
    def kota52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_event__kota52", None)
        self.__kota52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event53"):
                opp_val = getattr(old_value, "event53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event53"):
                opp_val = getattr(value, "event53", None)
                if opp_val is None:
                    setattr(value, "event53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def transaksi49(self):
        return self.__transaksi49
    @transaksi49.setter
    def transaksi49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_event__transaksi49", None)
        self.__transaksi49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "event48"):
                    opp_val = getattr(item, "event48", None)
                    
                    if opp_val == self:
                        setattr(item, "event48", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "event48"):
                    opp_val = getattr(item, "event48", None)
                    
                    setattr(item, "event48", self)
                    

    @property
    def e_ticket60(self):
        return self.__e_ticket60
    @e_ticket60.setter
    def e_ticket60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_event__e_ticket60", None)
        self.__e_ticket60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event61"):
                opp_val = getattr(old_value, "event61", None)
                if opp_val == self:
                    setattr(old_value, "event61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event61"):
                opp_val = getattr(value, "event61", None)
                setattr(value, "event61", self)

    @property
    def admin59(self):
        return self.__admin59
    @admin59.setter
    def admin59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_event__admin59", None)
        self.__admin59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "event58"):
                opp_val = getattr(old_value, "event58", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "event58"):
                opp_val = getattr(value, "event58", None)
                if opp_val is None:
                    setattr(value, "event58", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class e_ticket:

    def __init__(self, id_ticket: int, date: str, due_date: str, id_user: int, status: str, bukti_trf: str, id_event: int, event61: "event" = None, user47: set["user"] = None):
        self.id_ticket = id_ticket
        self.date = date
        self.due_date = due_date
        self.id_user = id_user
        self.status = status
        self.bukti_trf = bukti_trf
        self.id_event = id_event
        self.event61 = event61
        self.user47 = user47 if user47 is not None else set()
        
        pass
    @property
    def id_user(self):
        return self.__id_user
    @id_user.setter
    def id_user(self, id_user: int):
        self.__id_user = id_user

    @property
    def status(self):
        return self.__status
    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def id_ticket(self):
        return self.__id_ticket
    @id_ticket.setter
    def id_ticket(self, id_ticket: int):
        self.__id_ticket = id_ticket

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def id_event(self):
        return self.__id_event
    @id_event.setter
    def id_event(self, id_event: int):
        self.__id_event = id_event

    @property
    def bukti_trf(self):
        return self.__bukti_trf
    @bukti_trf.setter
    def bukti_trf(self, bukti_trf: str):
        self.__bukti_trf = bukti_trf

    @property
    def due_date(self):
        return self.__due_date
    @due_date.setter
    def due_date(self, due_date: str):
        self.__due_date = due_date

    @property
    def event61(self):
        return self.__event61
    @event61.setter
    def event61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_ticket__event61", None)
        self.__event61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "e_ticket60"):
                opp_val = getattr(old_value, "e_ticket60", None)
                if opp_val == self:
                    setattr(old_value, "e_ticket60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "e_ticket60"):
                opp_val = getattr(value, "e_ticket60", None)
                setattr(value, "e_ticket60", self)

    @property
    def user47(self):
        return self.__user47
    @user47.setter
    def user47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_e_ticket__user47", None)
        self.__user47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "e_ticket46"):
                    opp_val = getattr(item, "e_ticket46", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "e_ticket46"):
                    opp_val = getattr(item, "e_ticket46", None)
                    
                    if opp_val is None:
                        setattr(item, "e_ticket46", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class kota:

    def __init__(self, id_kota: int, nama_kota: str, gambar: str, event53: set["event"] = None):
        self.id_kota = id_kota
        self.nama_kota = nama_kota
        self.gambar = gambar
        self.event53 = event53 if event53 is not None else set()
        
        pass
    @property
    def nama_kota(self):
        return self.__nama_kota
    @nama_kota.setter
    def nama_kota(self, nama_kota: str):
        self.__nama_kota = nama_kota

    @property
    def id_kota(self):
        return self.__id_kota
    @id_kota.setter
    def id_kota(self, id_kota: int):
        self.__id_kota = id_kota

    @property
    def gambar(self):
        return self.__gambar
    @gambar.setter
    def gambar(self, gambar: str):
        self.__gambar = gambar

    @property
    def event53(self):
        return self.__event53
    @event53.setter
    def event53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kota__event53", None)
        self.__event53 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kota52"):
                    opp_val = getattr(item, "kota52", None)
                    
                    if opp_val == self:
                        setattr(item, "kota52", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kota52"):
                    opp_val = getattr(item, "kota52", None)
                    
                    setattr(item, "kota52", self)
                    



class transaksi:

    def __init__(self, id_orders: int, id_kota: int, nama_event: str, tipe_tiket: str, harga: int, id_event: int, user51: "user" = None, event48: "event" = None):
        self.id_orders = id_orders
        self.id_kota = id_kota
        self.nama_event = nama_event
        self.tipe_tiket = tipe_tiket
        self.harga = harga
        self.id_event = id_event
        self.user51 = user51
        self.event48 = event48
        
        pass
    @property
    def id_event(self):
        return self.__id_event
    @id_event.setter
    def id_event(self, id_event: int):
        self.__id_event = id_event

    @property
    def harga(self):
        return self.__harga
    @harga.setter
    def harga(self, harga: int):
        self.__harga = harga

    @property
    def id_orders(self):
        return self.__id_orders
    @id_orders.setter
    def id_orders(self, id_orders: int):
        self.__id_orders = id_orders

    @property
    def id_kota(self):
        return self.__id_kota
    @id_kota.setter
    def id_kota(self, id_kota: int):
        self.__id_kota = id_kota

    @property
    def tipe_tiket(self):
        return self.__tipe_tiket
    @tipe_tiket.setter
    def tipe_tiket(self, tipe_tiket: str):
        self.__tipe_tiket = tipe_tiket

    @property
    def nama_event(self):
        return self.__nama_event
    @nama_event.setter
    def nama_event(self, nama_event: str):
        self.__nama_event = nama_event

    @property
    def event48(self):
        return self.__event48
    @event48.setter
    def event48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaksi__event48", None)
        self.__event48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaksi49"):
                opp_val = getattr(old_value, "transaksi49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaksi49"):
                opp_val = getattr(value, "transaksi49", None)
                if opp_val is None:
                    setattr(value, "transaksi49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def user51(self):
        return self.__user51
    @user51.setter
    def user51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_transaksi__user51", None)
        self.__user51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "transaksi50"):
                opp_val = getattr(old_value, "transaksi50", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "transaksi50"):
                opp_val = getattr(value, "transaksi50", None)
                if opp_val is None:
                    setattr(value, "transaksi50", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class testimoni:

    def __init__(self, id: int, akses_instagram: str, sarana: str, buka_instagram: str, waktu_instagram: str, info_instagram: str, kepuasan_instagram: str, mudah_info: str, ptn: str, pts_favorit: str, kritik: str, admin57: "admin" = None):
        self.id = id
        self.akses_instagram = akses_instagram
        self.sarana = sarana
        self.buka_instagram = buka_instagram
        self.waktu_instagram = waktu_instagram
        self.info_instagram = info_instagram
        self.kepuasan_instagram = kepuasan_instagram
        self.mudah_info = mudah_info
        self.ptn = ptn
        self.pts_favorit = pts_favorit
        self.kritik = kritik
        self.admin57 = admin57
        
        pass
    @property
    def mudah_info(self):
        return self.__mudah_info
    @mudah_info.setter
    def mudah_info(self, mudah_info: str):
        self.__mudah_info = mudah_info

    @property
    def ptn(self):
        return self.__ptn
    @ptn.setter
    def ptn(self, ptn: str):
        self.__ptn = ptn

    @property
    def sarana(self):
        return self.__sarana
    @sarana.setter
    def sarana(self, sarana: str):
        self.__sarana = sarana

    @property
    def info_instagram(self):
        return self.__info_instagram
    @info_instagram.setter
    def info_instagram(self, info_instagram: str):
        self.__info_instagram = info_instagram

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def kritik(self):
        return self.__kritik
    @kritik.setter
    def kritik(self, kritik: str):
        self.__kritik = kritik

    @property
    def akses_instagram(self):
        return self.__akses_instagram
    @akses_instagram.setter
    def akses_instagram(self, akses_instagram: str):
        self.__akses_instagram = akses_instagram

    @property
    def kepuasan_instagram(self):
        return self.__kepuasan_instagram
    @kepuasan_instagram.setter
    def kepuasan_instagram(self, kepuasan_instagram: str):
        self.__kepuasan_instagram = kepuasan_instagram

    @property
    def waktu_instagram(self):
        return self.__waktu_instagram
    @waktu_instagram.setter
    def waktu_instagram(self, waktu_instagram: str):
        self.__waktu_instagram = waktu_instagram

    @property
    def buka_instagram(self):
        return self.__buka_instagram
    @buka_instagram.setter
    def buka_instagram(self, buka_instagram: str):
        self.__buka_instagram = buka_instagram

    @property
    def pts_favorit(self):
        return self.__pts_favorit
    @pts_favorit.setter
    def pts_favorit(self, pts_favorit: str):
        self.__pts_favorit = pts_favorit

    @property
    def admin57(self):
        return self.__admin57
    @admin57.setter
    def admin57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_testimoni__admin57", None)
        self.__admin57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "testimoni56"):
                opp_val = getattr(old_value, "testimoni56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "testimoni56"):
                opp_val = getattr(value, "testimoni56", None)
                if opp_val is None:
                    setattr(value, "testimoni56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class user:

    def __init__(self, id_user: int, nama_lengkap: str, email: str, password: str, no_telp: str, instagram: str, jenis_kelamin: str, asal_kota: str, asal_sekolah: str, gambar: str, transaksi50: set["transaksi"] = None, bookmark55: set["bookmark"] = None, e_ticket46: set["e_ticket"] = None):
        self.id_user = id_user
        self.nama_lengkap = nama_lengkap
        self.email = email
        self.password = password
        self.no_telp = no_telp
        self.instagram = instagram
        self.jenis_kelamin = jenis_kelamin
        self.asal_kota = asal_kota
        self.asal_sekolah = asal_sekolah
        self.gambar = gambar
        self.transaksi50 = transaksi50 if transaksi50 is not None else set()
        self.bookmark55 = bookmark55 if bookmark55 is not None else set()
        self.e_ticket46 = e_ticket46 if e_ticket46 is not None else set()
        
        pass
    @property
    def id_user(self):
        return self.__id_user
    @id_user.setter
    def id_user(self, id_user: int):
        self.__id_user = id_user

    @property
    def no_telp(self):
        return self.__no_telp
    @no_telp.setter
    def no_telp(self, no_telp: str):
        self.__no_telp = no_telp

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def asal_kota(self):
        return self.__asal_kota
    @asal_kota.setter
    def asal_kota(self, asal_kota: str):
        self.__asal_kota = asal_kota

    @property
    def instagram(self):
        return self.__instagram
    @instagram.setter
    def instagram(self, instagram: str):
        self.__instagram = instagram

    @property
    def asal_sekolah(self):
        return self.__asal_sekolah
    @asal_sekolah.setter
    def asal_sekolah(self, asal_sekolah: str):
        self.__asal_sekolah = asal_sekolah

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def gambar(self):
        return self.__gambar
    @gambar.setter
    def gambar(self, gambar: str):
        self.__gambar = gambar

    @property
    def nama_lengkap(self):
        return self.__nama_lengkap
    @nama_lengkap.setter
    def nama_lengkap(self, nama_lengkap: str):
        self.__nama_lengkap = nama_lengkap

    @property
    def jenis_kelamin(self):
        return self.__jenis_kelamin
    @jenis_kelamin.setter
    def jenis_kelamin(self, jenis_kelamin: str):
        self.__jenis_kelamin = jenis_kelamin

    @property
    def transaksi50(self):
        return self.__transaksi50
    @transaksi50.setter
    def transaksi50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__transaksi50", None)
        self.__transaksi50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user51"):
                    opp_val = getattr(item, "user51", None)
                    
                    if opp_val == self:
                        setattr(item, "user51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user51"):
                    opp_val = getattr(item, "user51", None)
                    
                    setattr(item, "user51", self)
                    

    @property
    def e_ticket46(self):
        return self.__e_ticket46
    @e_ticket46.setter
    def e_ticket46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__e_ticket46", None)
        self.__e_ticket46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user47"):
                    opp_val = getattr(item, "user47", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user47"):
                    opp_val = getattr(item, "user47", None)
                    
                    if opp_val is None:
                        setattr(item, "user47", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def bookmark55(self):
        return self.__bookmark55
    @bookmark55.setter
    def bookmark55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_user__bookmark55", None)
        self.__bookmark55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "user54"):
                    opp_val = getattr(item, "user54", None)
                    
                    if opp_val == self:
                        setattr(item, "user54", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "user54"):
                    opp_val = getattr(item, "user54", None)
                    
                    setattr(item, "user54", self)
                    



class _Component:

    pass
