####################
# STRUCTURAL MODEL #
####################

from besser.BUML.metamodel.structural import (
    Class, Property, Method, Parameter,
    BinaryAssociation, Generalization, DomainModel,
    Enumeration, EnumerationLiteral, Multiplicity,
    StringType, IntegerType, FloatType, BooleanType,
    TimeType, DateType, DateTimeType, TimeDeltaType,
    AnyType, Constraint, AssociationClass, Metadata
)

# Classes
_Component = Class(name="_Component")
Peserta_Actor = Class(name="Peserta_Actor")
Admin_Actor = Class(name="Admin_Actor")
user = Class(name="user")
testimoni = Class(name="testimoni")
transaksi = Class(name="transaksi")
kota = Class(name="kota")
e_ticket = Class(name="e_ticket")
event = Class(name="event")
admin = Class(name="admin")
bookmark = Class(name="bookmark")
Tambah_Link_Grup_Whatsapp_external = Class(name="Tambah_Link_Grup_Whatsapp_external")
Lihat_Hasil_Jawaban__make_it_better__external = Class(name="Lihat_Hasil_Jawaban__make_it_better__external")
Lihat_Ringkasan_Transaksi_external = Class(name="Lihat_Ringkasan_Transaksi_external")
Registrasi_external = Class(name="Registrasi_external")
Logout_external = Class(name="Logout_external")
Update_Profil_external = Class(name="Update_Profil_external")
Lihat_Event_external = Class(name="Lihat_Event_external")
Lihat_Detail_Event_external = Class(name="Lihat_Detail_Event_external")
Bayar_Tiket_external = Class(name="Bayar_Tiket_external")
Beli_Tiket_external = Class(name="Beli_Tiket_external")
Masuk_Link_Grup_Whatsapp_external = Class(name="Masuk_Link_Grup_Whatsapp_external")
Unduh_E_Ticket_external = Class(name="Unduh_E_Ticket_external")
Melihat_pertanyaan__make_it_better__external = Class(name="Melihat_pertanyaan__make_it_better__external")
Update__isi__pertanyaan__make_it_better__external = Class(name="Update__isi__pertanyaan__make_it_better__external")
Tambah_Event_external = Class(name="Tambah_Event_external")
Lihat_Seluruh_Peserta_external = Class(name="Lihat_Seluruh_Peserta_external")
Lihat_Peserta_Sudah_Bayar_external = Class(name="Lihat_Peserta_Sudah_Bayar_external")
Lihat_Peserta_Belum_Bayar_external = Class(name="Lihat_Peserta_Belum_Bayar_external")
Tambah_Kota_external = Class(name="Tambah_Kota_external")

# _Component class attributes and methods

# Peserta_Actor class attributes and methods

# Admin_Actor class attributes and methods

# user class attributes and methods
user_id_user: Property = Property(name="id_user", type=IntegerType)
user_nama_lengkap: Property = Property(name="nama_lengkap", type=StringType)
user_email: Property = Property(name="email", type=StringType)
user_password: Property = Property(name="password", type=StringType)
user_no_telp: Property = Property(name="no_telp", type=StringType)
user_instagram: Property = Property(name="instagram", type=StringType)
user_jenis_kelamin: Property = Property(name="jenis_kelamin", type=StringType)
user_asal_kota: Property = Property(name="asal_kota", type=StringType)
user_asal_sekolah: Property = Property(name="asal_sekolah", type=StringType)
user_gambar: Property = Property(name="gambar", type=StringType)
user.attributes={user_nama_lengkap, user_id_user, user_no_telp, user_password, user_gambar, user_email, user_asal_sekolah, user_jenis_kelamin, user_instagram, user_asal_kota}

# testimoni class attributes and methods
testimoni_id: Property = Property(name="id", type=IntegerType)
testimoni_akses_instagram: Property = Property(name="akses_instagram", type=StringType)
testimoni_sarana: Property = Property(name="sarana", type=StringType)
testimoni_buka_instagram: Property = Property(name="buka_instagram", type=StringType)
testimoni_waktu_instagram: Property = Property(name="waktu_instagram", type=StringType)
testimoni_info_instagram: Property = Property(name="info_instagram", type=StringType)
testimoni_kepuasan_instagram: Property = Property(name="kepuasan_instagram", type=StringType)
testimoni_mudah_info: Property = Property(name="mudah_info", type=StringType)
testimoni_ptn: Property = Property(name="ptn", type=StringType)
testimoni_pts_favorit: Property = Property(name="pts_favorit", type=StringType)
testimoni_kritik: Property = Property(name="kritik", type=StringType)
testimoni.attributes={testimoni_mudah_info, testimoni_akses_instagram, testimoni_info_instagram, testimoni_ptn, testimoni_waktu_instagram, testimoni_id, testimoni_sarana, testimoni_buka_instagram, testimoni_kepuasan_instagram, testimoni_kritik, testimoni_pts_favorit}

# transaksi class attributes and methods
transaksi_id_orders: Property = Property(name="id_orders", type=IntegerType)
transaksi_id_kota: Property = Property(name="id_kota", type=IntegerType)
transaksi_nama_event: Property = Property(name="nama_event", type=StringType)
transaksi_tipe_tiket: Property = Property(name="tipe_tiket", type=StringType)
transaksi_harga: Property = Property(name="harga", type=IntegerType)
transaksi_id_event: Property = Property(name="id_event", type=IntegerType)
transaksi.attributes={transaksi_id_orders, transaksi_id_kota, transaksi_nama_event, transaksi_id_event, transaksi_tipe_tiket, transaksi_harga}

# kota class attributes and methods
kota_id_kota: Property = Property(name="id_kota", type=IntegerType)
kota_nama_kota: Property = Property(name="nama_kota", type=StringType)
kota_gambar: Property = Property(name="gambar", type=StringType)
kota.attributes={kota_gambar, kota_id_kota, kota_nama_kota}

# e_ticket class attributes and methods
e_ticket_id_ticket: Property = Property(name="id_ticket", type=IntegerType)
e_ticket_date: Property = Property(name="date", type=StringType)
e_ticket_due_date: Property = Property(name="due_date", type=StringType)
e_ticket_id_user: Property = Property(name="id_user", type=IntegerType)
e_ticket_status: Property = Property(name="status", type=StringType)
e_ticket_bukti_trf: Property = Property(name="bukti_trf", type=StringType)
e_ticket_id_event: Property = Property(name="id_event", type=IntegerType)
e_ticket.attributes={e_ticket_date, e_ticket_id_user, e_ticket_bukti_trf, e_ticket_status, e_ticket_id_ticket, e_ticket_id_event, e_ticket_due_date}

# event class attributes and methods
event_detail: Property = Property(name="detail", type=StringType)
event_harga_reguler: Property = Property(name="harga_reguler", type=IntegerType)
event_harga_premium: Property = Property(name="harga_premium", type=IntegerType)
event_tanggal: Property = Property(name="tanggal", type=StringType)
event_deskripsi: Property = Property(name="deskripsi", type=StringType)
event_lokasi: Property = Property(name="lokasi", type=StringType)
event_latitude: Property = Property(name="latitude", type=StringType)
event_longitude: Property = Property(name="longitude", type=StringType)
event_gambar: Property = Property(name="gambar", type=StringType)
event_id_event: Property = Property(name="id_event", type=IntegerType)
event_id_kota: Property = Property(name="id_kota", type=IntegerType)
event_id_admin: Property = Property(name="id_admin", type=IntegerType)
event_nama_event: Property = Property(name="nama_event", type=StringType)
event.attributes={event_nama_event, event_latitude, event_harga_premium, event_id_event, event_id_admin, event_harga_reguler, event_longitude, event_tanggal, event_deskripsi, event_detail, event_gambar, event_lokasi, event_id_kota}

# admin class attributes and methods
admin_id_admin: Property = Property(name="id_admin", type=IntegerType)
admin_username: Property = Property(name="username", type=StringType)
admin_password: Property = Property(name="password", type=StringType)
admin.attributes={admin_username, admin_password, admin_id_admin}

# bookmark class attributes and methods
bookmark_id_bookmark: Property = Property(name="id_bookmark", type=IntegerType)
bookmark_id_event: Property = Property(name="id_event", type=IntegerType)
bookmark_id_user: Property = Property(name="id_user", type=IntegerType)
bookmark.attributes={bookmark_id_event, bookmark_id_user, bookmark_id_bookmark}

# Tambah_Link_Grup_Whatsapp_external class attributes and methods

# Lihat_Hasil_Jawaban__make_it_better__external class attributes and methods

# Lihat_Ringkasan_Transaksi_external class attributes and methods

# Registrasi_external class attributes and methods

# Logout_external class attributes and methods

# Update_Profil_external class attributes and methods

# Lihat_Event_external class attributes and methods

# Lihat_Detail_Event_external class attributes and methods

# Bayar_Tiket_external class attributes and methods

# Beli_Tiket_external class attributes and methods

# Masuk_Link_Grup_Whatsapp_external class attributes and methods

# Unduh_E_Ticket_external class attributes and methods

# Melihat_pertanyaan__make_it_better__external class attributes and methods

# Update__isi__pertanyaan__make_it_better__external class attributes and methods

# Tambah_Event_external class attributes and methods

# Lihat_Seluruh_Peserta_external class attributes and methods

# Lihat_Peserta_Sudah_Bayar_external class attributes and methods

# Lihat_Peserta_Belum_Bayar_external class attributes and methods

# Tambah_Kota_external class attributes and methods

# Relationships
Admin_Tambah_Link_Grup_Whatsapp: BinaryAssociation = BinaryAssociation(
    name="Admin_Tambah_Link_Grup_Whatsapp",
    ends={
        Property(name="tambah_Link_Grup_Whatsapp42", type=Tambah_Link_Grup_Whatsapp_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin43", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Lihat_Hasil_Jawaban__make_it_better_: BinaryAssociation = BinaryAssociation(
    name="Admin_Lihat_Hasil_Jawaban__make_it_better_",
    ends={
        Property(name="lihat_Hasil_Jawaban__make_it_better_44", type=Lihat_Hasil_Jawaban__make_it_better__external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin45", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
user_e_ticket: BinaryAssociation = BinaryAssociation(
    name="user_e_ticket",
    ends={
        Property(name="e_ticket46", type=e_ticket, multiplicity=Multiplicity(1, 9999)),
        Property(name="user47", type=user, multiplicity=Multiplicity(1, 9999))
    }
)
transaksi_event: BinaryAssociation = BinaryAssociation(
    name="transaksi_event",
    ends={
        Property(name="event48", type=event, multiplicity=Multiplicity(0, 1)),
        Property(name="transaksi49", type=transaksi, multiplicity=Multiplicity(1, 9999))
    }
)
Lihat_Ringkasan_Transaksi_Admin: BinaryAssociation = BinaryAssociation(
    name="Lihat_Ringkasan_Transaksi_Admin",
    ends={
        Property(name="admin0", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="lihat_Ringkasan_Transaksi1", type=Lihat_Ringkasan_Transaksi_external, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Registrasi: BinaryAssociation = BinaryAssociation(
    name="Peserta_Registrasi",
    ends={
        Property(name="registrasi2", type=Registrasi_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta3", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Logout: BinaryAssociation = BinaryAssociation(
    name="Peserta_Logout",
    ends={
        Property(name="logout4", type=Logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta5", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Update_Profil: BinaryAssociation = BinaryAssociation(
    name="Peserta_Update_Profil",
    ends={
        Property(name="update_Profil6", type=Update_Profil_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta7", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Lihat_Event: BinaryAssociation = BinaryAssociation(
    name="Peserta_Lihat_Event",
    ends={
        Property(name="lihat_Event8", type=Lihat_Event_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta9", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Lihat_Detail_Event: BinaryAssociation = BinaryAssociation(
    name="Peserta_Lihat_Detail_Event",
    ends={
        Property(name="lihat_Detail_Event10", type=Lihat_Detail_Event_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta11", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Bayar_Tiket: BinaryAssociation = BinaryAssociation(
    name="Peserta_Bayar_Tiket",
    ends={
        Property(name="bayar_Tiket12", type=Bayar_Tiket_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta13", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Beli_Tiket: BinaryAssociation = BinaryAssociation(
    name="Peserta_Beli_Tiket",
    ends={
        Property(name="beli_Tiket14", type=Beli_Tiket_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta15", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Masuk_Link_Grup_Whatsapp: BinaryAssociation = BinaryAssociation(
    name="Peserta_Masuk_Link_Grup_Whatsapp",
    ends={
        Property(name="masuk_Link_Grup_Whatsapp16", type=Masuk_Link_Grup_Whatsapp_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta17", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Unduh_E_Ticket: BinaryAssociation = BinaryAssociation(
    name="Peserta_Unduh_E_Ticket",
    ends={
        Property(name="unduh_E_Ticket18", type=Unduh_E_Ticket_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta19", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Melihat_pertanyaan__make_it_better_: BinaryAssociation = BinaryAssociation(
    name="Peserta_Melihat_pertanyaan__make_it_better_",
    ends={
        Property(name="melihat_pertanyaan__make_it_better_20", type=Melihat_pertanyaan__make_it_better__external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta21", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Peserta_Update__isi__pertanyaan__make_it_better_: BinaryAssociation = BinaryAssociation(
    name="Peserta_Update__isi__pertanyaan__make_it_better_",
    ends={
        Property(name="update__isi__pertanyaan__make_it_better_22", type=Update__isi__pertanyaan__make_it_better__external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta23", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Logout: BinaryAssociation = BinaryAssociation(
    name="Admin_Logout",
    ends={
        Property(name="logout24", type=Logout_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin25", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Lihat_Event: BinaryAssociation = BinaryAssociation(
    name="Admin_Lihat_Event",
    ends={
        Property(name="lihat_Event26", type=Lihat_Event_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin27", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Lihat_Detail_Event: BinaryAssociation = BinaryAssociation(
    name="Admin_Lihat_Detail_Event",
    ends={
        Property(name="lihat_Detail_Event28", type=Lihat_Detail_Event_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin29", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Melihat_pertanyaan__make_it_better_: BinaryAssociation = BinaryAssociation(
    name="Admin_Melihat_pertanyaan__make_it_better_",
    ends={
        Property(name="melihat_pertanyaan__make_it_better_30", type=Melihat_pertanyaan__make_it_better__external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin31", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Tambah_Event: BinaryAssociation = BinaryAssociation(
    name="Admin_Tambah_Event",
    ends={
        Property(name="tambah_Event32", type=Tambah_Event_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin33", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Lihat_Seluruh_Peserta: BinaryAssociation = BinaryAssociation(
    name="Admin_Lihat_Seluruh_Peserta",
    ends={
        Property(name="lihat_Seluruh_Peserta34", type=Lihat_Seluruh_Peserta_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin35", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Lihat_Peserta_Sudah_Bayar: BinaryAssociation = BinaryAssociation(
    name="Admin_Lihat_Peserta_Sudah_Bayar",
    ends={
        Property(name="lihat_Peserta_Sudah_Bayar36", type=Lihat_Peserta_Sudah_Bayar_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin37", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Lihat_Peserta_Belum_Bayar: BinaryAssociation = BinaryAssociation(
    name="Admin_Lihat_Peserta_Belum_Bayar",
    ends={
        Property(name="lihat_Peserta_Belum_Bayar38", type=Lihat_Peserta_Belum_Bayar_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin39", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Tambah_Kota: BinaryAssociation = BinaryAssociation(
    name="Admin_Tambah_Kota",
    ends={
        Property(name="tambah_Kota40", type=Tambah_Kota_external, multiplicity=Multiplicity(0, 1)),
        Property(name="admin41", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
user_transaksi: BinaryAssociation = BinaryAssociation(
    name="user_transaksi",
    ends={
        Property(name="transaksi50", type=transaksi, multiplicity=Multiplicity(1, 9999)),
        Property(name="user51", type=user, multiplicity=Multiplicity(0, 1))
    }
)
event_kota: BinaryAssociation = BinaryAssociation(
    name="event_kota",
    ends={
        Property(name="kota52", type=kota, multiplicity=Multiplicity(0, 1)),
        Property(name="event53", type=event, multiplicity=Multiplicity(1, 9999))
    }
)
bookmark_user: BinaryAssociation = BinaryAssociation(
    name="bookmark_user",
    ends={
        Property(name="user54", type=user, multiplicity=Multiplicity(0, 1)),
        Property(name="bookmark55", type=bookmark, multiplicity=Multiplicity(1, 9999))
    }
)
admin_testimoni: BinaryAssociation = BinaryAssociation(
    name="admin_testimoni",
    ends={
        Property(name="testimoni56", type=testimoni, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin57", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
admin_event: BinaryAssociation = BinaryAssociation(
    name="admin_event",
    ends={
        Property(name="event58", type=event, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin59", type=admin, multiplicity=Multiplicity(1, 1))
    }
)
event_e_ticket: BinaryAssociation = BinaryAssociation(
    name="event_e_ticket",
    ends={
        Property(name="e_ticket60", type=e_ticket, multiplicity=Multiplicity(0, 1)),
        Property(name="event61", type=event, multiplicity=Multiplicity(1, 1))
    }
)
Peserta_Lihat_Ringkasan_Transaksi: BinaryAssociation = BinaryAssociation(
    name="Peserta_Lihat_Ringkasan_Transaksi",
    ends={
        Property(name="lihat_Ringkasan_Transaksi62", type=Lihat_Ringkasan_Transaksi_external, multiplicity=Multiplicity(0, 1)),
        Property(name="peserta63", type=Peserta_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_neRcALPXEemcsc4aPpxbEQ",
    types={_Component, Peserta_Actor, Admin_Actor, user, testimoni, transaksi, kota, e_ticket, event, admin, bookmark, Tambah_Link_Grup_Whatsapp_external, Lihat_Hasil_Jawaban__make_it_better__external, Lihat_Ringkasan_Transaksi_external, Registrasi_external, Logout_external, Update_Profil_external, Lihat_Event_external, Lihat_Detail_Event_external, Bayar_Tiket_external, Beli_Tiket_external, Masuk_Link_Grup_Whatsapp_external, Unduh_E_Ticket_external, Melihat_pertanyaan__make_it_better__external, Update__isi__pertanyaan__make_it_better__external, Tambah_Event_external, Lihat_Seluruh_Peserta_external, Lihat_Peserta_Sudah_Bayar_external, Lihat_Peserta_Belum_Bayar_external, Tambah_Kota_external},
    associations={Admin_Tambah_Link_Grup_Whatsapp, Admin_Lihat_Hasil_Jawaban__make_it_better_, user_e_ticket, transaksi_event, Lihat_Ringkasan_Transaksi_Admin, Peserta_Registrasi, Peserta_Logout, Peserta_Update_Profil, Peserta_Lihat_Event, Peserta_Lihat_Detail_Event, Peserta_Bayar_Tiket, Peserta_Beli_Tiket, Peserta_Masuk_Link_Grup_Whatsapp, Peserta_Unduh_E_Ticket, Peserta_Melihat_pertanyaan__make_it_better_, Peserta_Update__isi__pertanyaan__make_it_better_, Admin_Logout, Admin_Lihat_Event, Admin_Lihat_Detail_Event, Admin_Melihat_pertanyaan__make_it_better_, Admin_Tambah_Event, Admin_Lihat_Seluruh_Peserta, Admin_Lihat_Peserta_Sudah_Bayar, Admin_Lihat_Peserta_Belum_Bayar, Admin_Tambah_Kota, user_transaksi, event_kota, bookmark_user, admin_testimoni, admin_event, event_e_ticket, Peserta_Lihat_Ringkasan_Transaksi},
    generalizations={},
    metadata=None
)

###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)