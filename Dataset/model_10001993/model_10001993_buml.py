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
Package2_melakukan_registrasi_UseCase = Class(name="Package2_melakukan_registrasi_UseCase")
Package2_melihat_riwayat_donasi_UseCase = Class(name="Package2_melihat_riwayat_donasi_UseCase")
Package2_melihat_inf_umum_yayasan_UseCase = Class(name="Package2_melihat_inf_umum_yayasan_UseCase")
Package2_melihat_laporan_penyaluran_donasi_UseCase = Class(name="Package2_melihat_laporan_penyaluran_donasi_UseCase")
Package2_melihat_program_donasi_UseCase = Class(name="Package2_melihat_program_donasi_UseCase")
Package2_mengubah_profil_UseCase = Class(name="Package2_mengubah_profil_UseCase")
Package2_membayar_tagihan_donasi_tetap_UseCase = Class(name="Package2_membayar_tagihan_donasi_tetap_UseCase")
Package2_melakukan_donasi_UseCase = Class(name="Package2_melakukan_donasi_UseCase")
Package2_konfirmasi_donasi_UseCase = Class(name="Package2_konfirmasi_donasi_UseCase")
Package2_cek_status_donasi_UseCase = Class(name="Package2_cek_status_donasi_UseCase")
Package2_cetak_laporan_UseCase = Class(name="Package2_cetak_laporan_UseCase")
Package2_mengelola_donasi_UseCase = Class(name="Package2_mengelola_donasi_UseCase")
Package2_Donatur_Actor = Class(name="Package2_Donatur_Actor")
Package2_Donatur_Tetap_Actor = Class(name="Package2_Donatur_Tetap_Actor")
Package2_Pengunjung_Actor = Class(name="Package2_Pengunjung_Actor")
mengelola_inf_umum_yayasan_UseCase = Class(name="mengelola_inf_umum_yayasan_UseCase")
Admin_Actor = Class(name="Admin_Actor")
login_UseCase4 = Class(name="login_UseCase4")
verifikasi_donasi_UseCase1 = Class(name="verifikasi_donasi_UseCase1")
melakukan_registrasi_UseCase = Class(name="melakukan_registrasi_UseCase")
melihat_riwayat_donasi_UseCase = Class(name="melihat_riwayat_donasi_UseCase")
melihat_inf_umum_yayasan_UseCase = Class(name="melihat_inf_umum_yayasan_UseCase")
melihat_laporan_penyaluran_donasi_UseCase = Class(name="melihat_laporan_penyaluran_donasi_UseCase")
melihat_program_donasi_UseCase1 = Class(name="melihat_program_donasi_UseCase1")
mengubah_profil_UseCase = Class(name="mengubah_profil_UseCase")
melakukan_donasi_UseCase3 = Class(name="melakukan_donasi_UseCase3")
konfirmasi_donasi_UseCase = Class(name="konfirmasi_donasi_UseCase")
cetak_laporan_UseCase = Class(name="cetak_laporan_UseCase")
mengelola_donasi_UseCase2 = Class(name="mengelola_donasi_UseCase2")
Donatur__Actor = Class(name="Donatur__Actor")
Umum_Actor = Class(name="Umum_Actor")
user = Class(name="user")
mengelola_program_donasi_UseCase5 = Class(name="mengelola_program_donasi_UseCase5")
mengelola_donatur_UseCase = Class(name="mengelola_donatur_UseCase")
cek_status_donasi_UseCase1 = Class(name="cek_status_donasi_UseCase1")
pemilik_yayasan_Actor = Class(name="pemilik_yayasan_Actor")
pengurus_yayasan_Actor = Class(name="pengurus_yayasan_Actor")
pengunjung_Actor = Class(name="pengunjung_Actor")
donatur_tidak_tetap_Actor = Class(name="donatur_tidak_tetap_Actor")
donatur_Actor = Class(name="donatur_Actor")
login_UseCase = Class(name="login_UseCase")
mengelola_pengurus_UseCase = Class(name="mengelola_pengurus_UseCase")
melakukan_donasi_UseCase = Class(name="melakukan_donasi_UseCase")
lihat_informasi_donatur_UseCase = Class(name="lihat_informasi_donatur_UseCase")
mencari_program_donasi_UseCase = Class(name="mencari_program_donasi_UseCase")
infomasi_donatur_UseCase = Class(name="infomasi_donatur_UseCase")
mengelola_data_donatur_UseCase = Class(name="mengelola_data_donatur_UseCase")
mengelola_data_donasi_UseCase = Class(name="mengelola_data_donasi_UseCase")
melakukan_donasi_UseCase1 = Class(name="melakukan_donasi_UseCase1")
mengelola_laporan_data_donasi_UseCase = Class(name="mengelola_laporan_data_donasi_UseCase")
meilhat_riwayat_donasi_UseCase = Class(name="meilhat_riwayat_donasi_UseCase")
mengelola_program_donasi_UseCase = Class(name="mengelola_program_donasi_UseCase")
melihat_informasi_umum2_UseCase = Class(name="melihat_informasi_umum2_UseCase")
melakukan_donasi_UseCase2 = Class(name="melakukan_donasi_UseCase2")
mengelola_data_donatur_UseCase1 = Class(name="mengelola_data_donatur_UseCase1")
mengelola_program_donasi_UseCase1 = Class(name="mengelola_program_donasi_UseCase1")
mengelola_data_donasi_UseCase1 = Class(name="mengelola_data_donasi_UseCase1")
mengelola_program_donasi_UseCase2 = Class(name="mengelola_program_donasi_UseCase2")
edit_profil_donatur_UseCase = Class(name="edit_profil_donatur_UseCase")
melihat_informasi_umum_yayasan_UseCase = Class(name="melihat_informasi_umum_yayasan_UseCase")
login_UseCase1 = Class(name="login_UseCase1")
login_UseCase2 = Class(name="login_UseCase2")
tambah_informasi_umum_yayasan_UseCase = Class(name="tambah_informasi_umum_yayasan_UseCase")
donatur_Actor1 = Class(name="donatur_Actor1")
registrasi_UseCase = Class(name="registrasi_UseCase")
login_UseCase3 = Class(name="login_UseCase3")
manajemen_donasi_UseCase = Class(name="manajemen_donasi_UseCase")
informasi_donatur_UseCase = Class(name="informasi_donatur_UseCase")
melihat_laporan_donasi_UseCase = Class(name="melihat_laporan_donasi_UseCase")
mengelola_donasi_UseCase = Class(name="mengelola_donasi_UseCase")
melihat__program_donasi_UseCase = Class(name="melihat__program_donasi_UseCase")
pemilik_yayasan_Actor1 = Class(name="pemilik_yayasan_Actor1")
mengelola_inf__umum_yayasan_UseCase = Class(name="mengelola_inf__umum_yayasan_UseCase")
melihat_program_donasi_UseCase = Class(name="melihat_program_donasi_UseCase")
melihat_program_donasi2_UseCase = Class(name="melihat_program_donasi2_UseCase")
mengelola_program_donasi_UseCase3 = Class(name="mengelola_program_donasi_UseCase3")
donatur_tetap_Actor = Class(name="donatur_tetap_Actor")
registrasi_UseCase1 = Class(name="registrasi_UseCase1")
melihat__informasi_umum_yayasan_UseCase = Class(name="melihat__informasi_umum_yayasan_UseCase")
verifikasi_donasi_UseCase = Class(name="verifikasi_donasi_UseCase")
cek_status_donasi_UseCase = Class(name="cek_status_donasi_UseCase")
Component_Component = Class(name="Component_Component")
mengelola_program_donasi_UseCase4 = Class(name="mengelola_program_donasi_UseCase4")
mencetak_laporan_UseCase = Class(name="mencetak_laporan_UseCase")
melakukan_registrasi__UseCase = Class(name="melakukan_registrasi__UseCase")
mengelola_donasi_UseCase1 = Class(name="mengelola_donasi_UseCase1")
mengelola_donasi2_UseCase = Class(name="mengelola_donasi2_UseCase")
Package2_Pemilik_Yayasan_Actor = Class(name="Package2_Pemilik_Yayasan_Actor")
Package2_mengelola_data_pengurus_UseCase = Class(name="Package2_mengelola_data_pengurus_UseCase")
Package2_mengelola_inf_umum_yayasan_UseCase = Class(name="Package2_mengelola_inf_umum_yayasan_UseCase")
Package2_mengelola_program_donasi_UseCase = Class(name="Package2_mengelola_program_donasi_UseCase")
Package2_mengelola_donatur_UseCase = Class(name="Package2_mengelola_donatur_UseCase")
Package2_Pengurus_Yayasan_Actor = Class(name="Package2_Pengurus_Yayasan_Actor")
Package2_login_UseCase = Class(name="Package2_login_UseCase")
Package2_verifikasi_donasi_UseCase = Class(name="Package2_verifikasi_donasi_UseCase")

# Package2_melakukan_registrasi_UseCase class attributes and methods

# Package2_melihat_riwayat_donasi_UseCase class attributes and methods

# Package2_melihat_inf_umum_yayasan_UseCase class attributes and methods

# Package2_melihat_laporan_penyaluran_donasi_UseCase class attributes and methods

# Package2_melihat_program_donasi_UseCase class attributes and methods

# Package2_mengubah_profil_UseCase class attributes and methods

# Package2_membayar_tagihan_donasi_tetap_UseCase class attributes and methods

# Package2_melakukan_donasi_UseCase class attributes and methods

# Package2_konfirmasi_donasi_UseCase class attributes and methods

# Package2_cek_status_donasi_UseCase class attributes and methods

# Package2_cetak_laporan_UseCase class attributes and methods

# Package2_mengelola_donasi_UseCase class attributes and methods

# Package2_Donatur_Actor class attributes and methods

# Package2_Donatur_Tetap_Actor class attributes and methods

# Package2_Pengunjung_Actor class attributes and methods

# mengelola_inf_umum_yayasan_UseCase class attributes and methods

# Admin_Actor class attributes and methods

# login_UseCase4 class attributes and methods

# verifikasi_donasi_UseCase1 class attributes and methods

# melakukan_registrasi_UseCase class attributes and methods

# melihat_riwayat_donasi_UseCase class attributes and methods

# melihat_inf_umum_yayasan_UseCase class attributes and methods

# melihat_laporan_penyaluran_donasi_UseCase class attributes and methods

# melihat_program_donasi_UseCase1 class attributes and methods

# mengubah_profil_UseCase class attributes and methods

# melakukan_donasi_UseCase3 class attributes and methods

# konfirmasi_donasi_UseCase class attributes and methods

# cetak_laporan_UseCase class attributes and methods

# mengelola_donasi_UseCase2 class attributes and methods

# Donatur__Actor class attributes and methods

# Umum_Actor class attributes and methods

# user class attributes and methods
user_id_user: Property = Property(name="id_user", type=StringType)
user_password: Property = Property(name="password", type=StringType)
user_nama_user: Property = Property(name="nama_user", type=StringType)
user_email: Property = Property(name="email", type=StringType)
user.attributes={user_nama_user, user_password, user_email, user_id_user}

# mengelola_program_donasi_UseCase5 class attributes and methods

# mengelola_donatur_UseCase class attributes and methods

# cek_status_donasi_UseCase1 class attributes and methods

# pemilik_yayasan_Actor class attributes and methods

# pengurus_yayasan_Actor class attributes and methods

# pengunjung_Actor class attributes and methods

# donatur_tidak_tetap_Actor class attributes and methods

# donatur_Actor class attributes and methods

# login_UseCase class attributes and methods

# mengelola_pengurus_UseCase class attributes and methods

# melakukan_donasi_UseCase class attributes and methods

# lihat_informasi_donatur_UseCase class attributes and methods

# mencari_program_donasi_UseCase class attributes and methods

# infomasi_donatur_UseCase class attributes and methods

# mengelola_data_donatur_UseCase class attributes and methods

# mengelola_data_donasi_UseCase class attributes and methods

# melakukan_donasi_UseCase1 class attributes and methods

# mengelola_laporan_data_donasi_UseCase class attributes and methods

# meilhat_riwayat_donasi_UseCase class attributes and methods

# mengelola_program_donasi_UseCase class attributes and methods

# melihat_informasi_umum2_UseCase class attributes and methods

# melakukan_donasi_UseCase2 class attributes and methods

# mengelola_data_donatur_UseCase1 class attributes and methods

# mengelola_program_donasi_UseCase1 class attributes and methods

# mengelola_data_donasi_UseCase1 class attributes and methods

# mengelola_program_donasi_UseCase2 class attributes and methods

# edit_profil_donatur_UseCase class attributes and methods

# melihat_informasi_umum_yayasan_UseCase class attributes and methods

# login_UseCase1 class attributes and methods

# login_UseCase2 class attributes and methods

# tambah_informasi_umum_yayasan_UseCase class attributes and methods

# donatur_Actor1 class attributes and methods

# registrasi_UseCase class attributes and methods

# login_UseCase3 class attributes and methods

# manajemen_donasi_UseCase class attributes and methods

# informasi_donatur_UseCase class attributes and methods

# melihat_laporan_donasi_UseCase class attributes and methods

# mengelola_donasi_UseCase class attributes and methods

# melihat__program_donasi_UseCase class attributes and methods

# pemilik_yayasan_Actor1 class attributes and methods

# mengelola_inf__umum_yayasan_UseCase class attributes and methods

# melihat_program_donasi_UseCase class attributes and methods

# melihat_program_donasi2_UseCase class attributes and methods

# mengelola_program_donasi_UseCase3 class attributes and methods

# donatur_tetap_Actor class attributes and methods

# registrasi_UseCase1 class attributes and methods

# melihat__informasi_umum_yayasan_UseCase class attributes and methods

# verifikasi_donasi_UseCase class attributes and methods

# cek_status_donasi_UseCase class attributes and methods

# Component_Component class attributes and methods

# mengelola_program_donasi_UseCase4 class attributes and methods

# mencetak_laporan_UseCase class attributes and methods

# melakukan_registrasi__UseCase class attributes and methods

# mengelola_donasi_UseCase1 class attributes and methods

# mengelola_donasi2_UseCase class attributes and methods

# Package2_Pemilik_Yayasan_Actor class attributes and methods

# Package2_mengelola_data_pengurus_UseCase class attributes and methods

# Package2_mengelola_inf_umum_yayasan_UseCase class attributes and methods

# Package2_mengelola_program_donasi_UseCase class attributes and methods

# Package2_mengelola_donatur_UseCase class attributes and methods

# Package2_Pengurus_Yayasan_Actor class attributes and methods

# Package2_login_UseCase class attributes and methods

# Package2_verifikasi_donasi_UseCase class attributes and methods

# Relationships
pemilik_yayasan_mengelola_data_pengurus: BinaryAssociation = BinaryAssociation(
    name="pemilik_yayasan_mengelola_data_pengurus",
    ends={
        Property(name="mengelola_data_pengurus0", type=mengelola_pengurus_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pemilik_yayasan1", type=pemilik_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
mengelola_program_donasi_pengurus_yayasan: BinaryAssociation = BinaryAssociation(
    name="mengelola_program_donasi_pengurus_yayasan",
    ends={
        Property(name="pengurus_yayasan40", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mengelola_program_donasi41", type=mengelola_program_donasi_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_mengelola_program_donasi: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_mengelola_program_donasi",
    ends={
        Property(name="mengelola_program_donasi42", type=mengelola_program_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan43", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pemilik_yayasan_login: BinaryAssociation = BinaryAssociation(
    name="pemilik_yayasan_login",
    ends={
        Property(name="login44", type=login_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="pemilik_yayasan45", type=pemilik_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
login_pengurus_yayasan: BinaryAssociation = BinaryAssociation(
    name="login_pengurus_yayasan",
    ends={
        Property(name="pengurus_yayasan46", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login47", type=login_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
donatur_registrasi: BinaryAssociation = BinaryAssociation(
    name="donatur_registrasi",
    ends={
        Property(name="registrasi48", type=registrasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur49", type=donatur_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
donatur_login: BinaryAssociation = BinaryAssociation(
    name="donatur_login",
    ends={
        Property(name="login50", type=login_UseCase3, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur51", type=donatur_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
donatur_melakukan_donasi: BinaryAssociation = BinaryAssociation(
    name="donatur_melakukan_donasi",
    ends={
        Property(name="melakukan_donasi52", type=melakukan_donasi_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur53", type=donatur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tetap_melakukan_donasi: BinaryAssociation = BinaryAssociation(
    name="donatur_tetap_melakukan_donasi",
    ends={
        Property(name="melakukan_donasi54", type=melakukan_donasi_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tetap55", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
meilhat_riwayat_donasi_donatur_tetap: BinaryAssociation = BinaryAssociation(
    name="meilhat_riwayat_donasi_donatur_tetap",
    ends={
        Property(name="donatur_tetap56", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="meilhat_riwayat_donasi57", type=meilhat_riwayat_donasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
melihat__laporan_donasi_donatur_tetap: BinaryAssociation = BinaryAssociation(
    name="melihat__laporan_donasi_donatur_tetap",
    ends={
        Property(name="donatur_tetap58", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="melihat__laporan_donasi59", type=melihat__program_donasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
pemilik_yayasan_mengelola_data_pengurus_3: BinaryAssociation = BinaryAssociation(
    name="pemilik_yayasan_mengelola_data_pengurus_3",
    ends={
        Property(name="mengelola_data_pengurus60", type=mengelola_pengurus_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pemilik_yayasan61", type=pemilik_yayasan_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_mengelola_informasi_umum_yayasan2: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_mengelola_informasi_umum_yayasan2",
    ends={
        Property(name="mengelola_informasi_umum_yayasan262", type=mengelola_inf__umum_yayasan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan63", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
calon_donatur_donatur_tidak_tetap: BinaryAssociation = BinaryAssociation(
    name="calon_donatur_donatur_tidak_tetap",
    ends={
        Property(name="donatur_tidak_tetap2", type=donatur_tidak_tetap_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="calon_donatur3", type=donatur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tetap_melihat_data_laporan_donasi: BinaryAssociation = BinaryAssociation(
    name="donatur_tetap_melihat_data_laporan_donasi",
    ends={
        Property(name="melihat_data_laporan_donasi4", type=meilhat_riwayat_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tetap5", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengelola_yayasan_mengelola_data_donatur: BinaryAssociation = BinaryAssociation(
    name="pengelola_yayasan_mengelola_data_donatur",
    ends={
        Property(name="mengelola_data_donatur6", type=mengelola_data_donatur_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengelola_yayasan7", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
mengelola_laporan_data_donasi_pengelola_yayasan: BinaryAssociation = BinaryAssociation(
    name="mengelola_laporan_data_donasi_pengelola_yayasan",
    ends={
        Property(name="pengelola_yayasan8", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mengelola_laporan_data_donasi9", type=mengelola_laporan_data_donasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tidak_tetap_melihat_data_laporan_donasi: BinaryAssociation = BinaryAssociation(
    name="donatur_tidak_tetap_melihat_data_laporan_donasi",
    ends={
        Property(name="melihat_data_laporan_donasi10", type=meilhat_riwayat_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tidak_tetap11", type=donatur_tidak_tetap_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tidak_tetap_calon_donatur: BinaryAssociation = BinaryAssociation(
    name="donatur_tidak_tetap_calon_donatur",
    ends={
        Property(name="calon_donatur12", type=donatur_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tidak_tetap13", type=donatur_tidak_tetap_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tidak_tetap_melihat_informasi_umum: BinaryAssociation = BinaryAssociation(
    name="donatur_tidak_tetap_melihat_informasi_umum",
    ends={
        Property(name="melihat_informasi_umum14", type=melakukan_donasi_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tidak_tetap15", type=donatur_tidak_tetap_Actor, multiplicity=Multiplicity(0, 1))
    }
)
melihat_data_laporan_donasi_donatur_tetap: BinaryAssociation = BinaryAssociation(
    name="melihat_data_laporan_donasi_donatur_tetap",
    ends={
        Property(name="donatur_tetap16", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="melihat_data_laporan_donasi17", type=meilhat_riwayat_donasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
update_profile_donatur_donatur_tetap: BinaryAssociation = BinaryAssociation(
    name="update_profile_donatur_donatur_tetap",
    ends={
        Property(name="donatur_tetap18", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="update_profile_donatur19", type=mengelola_program_donasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
login_pemilik_yayasan: BinaryAssociation = BinaryAssociation(
    name="login_pemilik_yayasan",
    ends={
        Property(name="pemilik_yayasan20", type=pemilik_yayasan_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="login21", type=login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
pengelola_yayasan_login: BinaryAssociation = BinaryAssociation(
    name="pengelola_yayasan_login",
    ends={
        Property(name="login22", type=login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengelola_yayasan23", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tetap_login: BinaryAssociation = BinaryAssociation(
    name="donatur_tetap_login",
    ends={
        Property(name="login24", type=login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tetap25", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pemilik_yayasan_mengelola_data_pengurus_2: BinaryAssociation = BinaryAssociation(
    name="pemilik_yayasan_mengelola_data_pengurus_2",
    ends={
        Property(name="mengelola_data_pengurus26", type=mengelola_pengurus_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pemilik_yayasan27", type=pemilik_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengelola_yayasan_mengelola_program_donasi: BinaryAssociation = BinaryAssociation(
    name="pengelola_yayasan_mengelola_program_donasi",
    ends={
        Property(name="mengelola_program_donasi28", type=mengelola_program_donasi_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="pengelola_yayasan29", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tidak_tetap_calon_donatur2: BinaryAssociation = BinaryAssociation(
    name="donatur_tidak_tetap_calon_donatur2",
    ends={
        Property(name="calon_donatur30", type=donatur_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tidak_tetap31", type=donatur_tidak_tetap_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_mengelola_informasi_umum_yayasan: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_mengelola_informasi_umum_yayasan",
    ends={
        Property(name="mengelola_informasi_umum_yayasan32", type=login_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan33", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_pengurus_yayasan: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_pengurus_yayasan",
    ends={
        Property(name="pengurus_yayasan34", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan35", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_mengelola_data_donasi: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_mengelola_data_donasi",
    ends={
        Property(name="mengelola_data_donasi36", type=mengelola_data_donasi_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan37", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
mengelola_data_donatur_pengurus_yayasan: BinaryAssociation = BinaryAssociation(
    name="mengelola_data_donatur_pengurus_yayasan",
    ends={
        Property(name="pengurus_yayasan38", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mengelola_data_donatur39", type=mengelola_data_donatur_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_mengelola_program_donasi3: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_mengelola_program_donasi3",
    ends={
        Property(name="mengelola_program_donasi102", type=mengelola_program_donasi_UseCase4, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan103", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pemilik_Yayasan_mengelola_data_pengurus: BinaryAssociation = BinaryAssociation(
    name="Pemilik_Yayasan_mengelola_data_pengurus",
    ends={
        Property(name="mengelola_data_pengurus104", type=Package2_mengelola_data_pengurus_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pemilik_Yayasan105", type=Package2_Pemilik_Yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_mengelola_inf_umum_yayasan: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_mengelola_inf_umum_yayasan",
    ends={
        Property(name="mengelola_inf_umum_yayasan106", type=Package2_mengelola_inf_umum_yayasan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan107", type=Package2_Pengurus_Yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_mengelola_program_donasi: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_mengelola_program_donasi",
    ends={
        Property(name="mengelola_program_donasi108", type=Package2_mengelola_program_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan109", type=Package2_Pengurus_Yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_mengelola_donatur: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_mengelola_donatur",
    ends={
        Property(name="mengelola_donatur110", type=Package2_mengelola_donatur_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan111", type=Package2_Pengurus_Yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_cetak_laporan: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_cetak_laporan",
    ends={
        Property(name="cetak_laporan112", type=Package2_cetak_laporan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan113", type=Package2_Pengurus_Yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_konfirmasi_donasi: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_konfirmasi_donasi",
    ends={
        Property(name="konfirmasi_donasi114", type=Package2_verifikasi_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan115", type=Package2_Pengurus_Yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
mengelola_donasi_Pengurus_Yayasan: BinaryAssociation = BinaryAssociation(
    name="mengelola_donasi_Pengurus_Yayasan",
    ends={
        Property(name="pengurus_Yayasan116", type=Package2_Pengurus_Yayasan_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mengelola_donasi117", type=Package2_mengelola_donasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_login: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_login",
    ends={
        Property(name="login118", type=Package2_login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan119", type=Package2_Pengurus_Yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Donatur_login: BinaryAssociation = BinaryAssociation(
    name="Donatur_login",
    ends={
        Property(name="login120", type=Package2_login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur121", type=Package2_Donatur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Donatur_melihat_riwayat_transaksi: BinaryAssociation = BinaryAssociation(
    name="Donatur_melihat_riwayat_transaksi",
    ends={
        Property(name="melihat_riwayat_transaksi122", type=Package2_melihat_riwayat_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur123", type=Package2_Donatur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_melihat_inf_umum_yayasan: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_melihat_inf_umum_yayasan",
    ends={
        Property(name="melihat_inf_umum_yayasan124", type=Package2_melihat_inf_umum_yayasan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung125", type=Package2_Pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_melihat_laporan_penyaluran_donasi: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_melihat_laporan_penyaluran_donasi",
    ends={
        Property(name="melihat_laporan_penyaluran_donasi126", type=Package2_melihat_laporan_penyaluran_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung127", type=Package2_Pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_mengelola_data_donatur: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_mengelola_data_donatur",
    ends={
        Property(name="mengelola_data_donatur64", type=mengelola_data_donatur_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan65", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_mengelola_donasi: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_mengelola_donasi",
    ends={
        Property(name="mengelola_donasi66", type=mengelola_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan67", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tetap_melihat_riwayat_donasi: BinaryAssociation = BinaryAssociation(
    name="donatur_tetap_melihat_riwayat_donasi",
    ends={
        Property(name="melihat_riwayat_donasi68", type=edit_profil_donatur_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tetap69", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tetap_melihat_informasi_umum_yayasan: BinaryAssociation = BinaryAssociation(
    name="donatur_tetap_melihat_informasi_umum_yayasan",
    ends={
        Property(name="melihat_informasi_umum_yayasan70", type=melihat_laporan_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tetap71", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tetap_melihat_program_donasi: BinaryAssociation = BinaryAssociation(
    name="donatur_tetap_melihat_program_donasi",
    ends={
        Property(name="melihat_program_donasi72", type=melihat_program_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tetap73", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
melihat__program_donasi_donatur_tidak_tetap: BinaryAssociation = BinaryAssociation(
    name="melihat__program_donasi_donatur_tidak_tetap",
    ends={
        Property(name="donatur_tidak_tetap74", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="melihat__program_donasi75", type=melihat__program_donasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
melakukan_donasi_donatur_tidak_tetap: BinaryAssociation = BinaryAssociation(
    name="melakukan_donasi_donatur_tidak_tetap",
    ends={
        Property(name="donatur_tidak_tetap76", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="melakukan_donasi77", type=melakukan_donasi_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_melakukan_verifikasi_donasi: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_melakukan_verifikasi_donasi",
    ends={
        Property(name="melakukan_verifikasi_donasi78", type=mengelola_program_donasi_UseCase3, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan79", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
registrasi_donatur_tidak_tetap: BinaryAssociation = BinaryAssociation(
    name="registrasi_donatur_tidak_tetap",
    ends={
        Property(name="donatur_tidak_tetap80", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="registrasi81", type=registrasi_UseCase1, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tetap_meilhat_riwayat_donasi: BinaryAssociation = BinaryAssociation(
    name="donatur_tetap_meilhat_riwayat_donasi",
    ends={
        Property(name="meilhat_riwayat_donasi82", type=meilhat_riwayat_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tetap83", type=donatur_tetap_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tetap_edit_profil_donatur: BinaryAssociation = BinaryAssociation(
    name="donatur_tetap_edit_profil_donatur",
    ends={
        Property(name="edit_profil_donatur84", type=edit_profil_donatur_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tetap85", type=donatur_tetap_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tidak_tetap_melihat__informasi_umum_yayasan: BinaryAssociation = BinaryAssociation(
    name="donatur_tidak_tetap_melihat__informasi_umum_yayasan",
    ends={
        Property(name="melihat__informasi_umum_yayasan86", type=melihat__informasi_umum_yayasan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tidak_tetap87", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_mengelola_program_donasi2: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_mengelola_program_donasi2",
    ends={
        Property(name="mengelola_program_donasi88", type=mengelola_program_donasi_UseCase3, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan89", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengurus_yayasan_verifikasi_donasi: BinaryAssociation = BinaryAssociation(
    name="pengurus_yayasan_verifikasi_donasi",
    ends={
        Property(name="verifikasi_donasi90", type=verifikasi_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_yayasan91", type=pengurus_yayasan_Actor, multiplicity=Multiplicity(0, 1))
    }
)
donatur_tidak_tetap_cek_status_donasi: BinaryAssociation = BinaryAssociation(
    name="donatur_tidak_tetap_cek_status_donasi",
    ends={
        Property(name="cek_status_donasi92", type=cek_status_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_tidak_tetap93", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengunjung_melakukan_donasi: BinaryAssociation = BinaryAssociation(
    name="pengunjung_melakukan_donasi",
    ends={
        Property(name="melakukan_donasi94", type=melakukan_donasi_UseCase2, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung95", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengunjung_melihat__informasi_umum_yayasan: BinaryAssociation = BinaryAssociation(
    name="pengunjung_melihat__informasi_umum_yayasan",
    ends={
        Property(name="melihat__informasi_umum_yayasan96", type=melihat__informasi_umum_yayasan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung97", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengunjung_melihat__program_donasi: BinaryAssociation = BinaryAssociation(
    name="pengunjung_melihat__program_donasi",
    ends={
        Property(name="melihat__program_donasi98", type=melihat__program_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung99", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
pengunjung_melihat_data_donasi: BinaryAssociation = BinaryAssociation(
    name="pengunjung_melihat_data_donasi",
    ends={
        Property(name="melihat_data_donasi100", type=melihat_laporan_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung101", type=pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_melihat_program_donasi: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_melihat_program_donasi",
    ends={
        Property(name="melihat_program_donasi128", type=Package2_melihat_program_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung129", type=Package2_Pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Donatur_mengubah_profil: BinaryAssociation = BinaryAssociation(
    name="Donatur_mengubah_profil",
    ends={
        Property(name="mengubah_profil130", type=Package2_mengubah_profil_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur131", type=Package2_Donatur_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Donatur_Tetap_melihat_tagihan_donasi_tetap: BinaryAssociation = BinaryAssociation(
    name="Donatur_Tetap_melihat_tagihan_donasi_tetap",
    ends={
        Property(name="melihat_tagihan_donasi_tetap132", type=Package2_membayar_tagihan_donasi_tetap_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="donatur_Tetap133", type=Package2_Donatur_Tetap_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_melakukan_donasi: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_melakukan_donasi",
    ends={
        Property(name="melakukan_donasi134", type=Package2_melakukan_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung135", type=Package2_Pengunjung_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_mengelola_inf_umum_yayasan1: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_mengelola_inf_umum_yayasan1",
    ends={
        Property(name="mengelola_inf_umum_yayasan136", type=mengelola_inf_umum_yayasan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan137", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_mengelola_program_donasi1: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_mengelola_program_donasi1",
    ends={
        Property(name="mengelola_program_donasi138", type=mengelola_program_donasi_UseCase5, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan139", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_mengelola_donatur1: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_mengelola_donatur1",
    ends={
        Property(name="mengelola_donatur140", type=mengelola_donatur_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan141", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_cetak_laporan1: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_cetak_laporan1",
    ends={
        Property(name="cetak_laporan142", type=cetak_laporan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan143", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengurus_Yayasan_konfirmasi_donasi1: BinaryAssociation = BinaryAssociation(
    name="Pengurus_Yayasan_konfirmasi_donasi1",
    ends={
        Property(name="konfirmasi_donasi144", type=verifikasi_donasi_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="pengurus_Yayasan145", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
mengelola_donasi_Pengurus_Yayasan1: BinaryAssociation = BinaryAssociation(
    name="mengelola_donasi_Pengurus_Yayasan1",
    ends={
        Property(name="pengurus_Yayasan146", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="mengelola_donasi147", type=mengelola_donasi_UseCase2, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_melihat_inf_umum_yayasan1: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_melihat_inf_umum_yayasan1",
    ends={
        Property(name="melihat_inf_umum_yayasan148", type=melihat_inf_umum_yayasan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung149", type=Umum_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_melihat_laporan_penyaluran_donasi1: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_melihat_laporan_penyaluran_donasi1",
    ends={
        Property(name="melihat_laporan_penyaluran_donasi150", type=melihat_laporan_penyaluran_donasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung151", type=Umum_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_melihat_program_donasi1: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_melihat_program_donasi1",
    ends={
        Property(name="melihat_program_donasi152", type=melihat_program_donasi_UseCase1, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung153", type=Umum_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pengunjung_melakukan_donasi1: BinaryAssociation = BinaryAssociation(
    name="Pengunjung_melakukan_donasi1",
    ends={
        Property(name="melakukan_donasi154", type=melakukan_donasi_UseCase3, multiplicity=Multiplicity(0, 1)),
        Property(name="pengunjung155", type=Donatur__Actor, multiplicity=Multiplicity(0, 1))
    }
)
melihat_riwayat_donasi_Donatur_Tetap: BinaryAssociation = BinaryAssociation(
    name="melihat_riwayat_donasi_Donatur_Tetap",
    ends={
        Property(name="donatur_Tetap156", type=Donatur__Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="melihat_riwayat_donasi157", type=melihat_riwayat_donasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_iOzQcOHMEemrJo0JEnN_HA",
    types={Package2_melakukan_registrasi_UseCase, Package2_melihat_riwayat_donasi_UseCase, Package2_melihat_inf_umum_yayasan_UseCase, Package2_melihat_laporan_penyaluran_donasi_UseCase, Package2_melihat_program_donasi_UseCase, Package2_mengubah_profil_UseCase, Package2_membayar_tagihan_donasi_tetap_UseCase, Package2_melakukan_donasi_UseCase, Package2_konfirmasi_donasi_UseCase, Package2_cek_status_donasi_UseCase, Package2_cetak_laporan_UseCase, Package2_mengelola_donasi_UseCase, Package2_Donatur_Actor, Package2_Donatur_Tetap_Actor, Package2_Pengunjung_Actor, mengelola_inf_umum_yayasan_UseCase, Admin_Actor, login_UseCase4, verifikasi_donasi_UseCase1, melakukan_registrasi_UseCase, melihat_riwayat_donasi_UseCase, melihat_inf_umum_yayasan_UseCase, melihat_laporan_penyaluran_donasi_UseCase, melihat_program_donasi_UseCase1, mengubah_profil_UseCase, melakukan_donasi_UseCase3, konfirmasi_donasi_UseCase, cetak_laporan_UseCase, mengelola_donasi_UseCase2, Donatur__Actor, Umum_Actor, user, mengelola_program_donasi_UseCase5, mengelola_donatur_UseCase, cek_status_donasi_UseCase1, pemilik_yayasan_Actor, pengurus_yayasan_Actor, pengunjung_Actor, donatur_tidak_tetap_Actor, donatur_Actor, login_UseCase, mengelola_pengurus_UseCase, melakukan_donasi_UseCase, lihat_informasi_donatur_UseCase, mencari_program_donasi_UseCase, infomasi_donatur_UseCase, mengelola_data_donatur_UseCase, mengelola_data_donasi_UseCase, melakukan_donasi_UseCase1, mengelola_laporan_data_donasi_UseCase, meilhat_riwayat_donasi_UseCase, mengelola_program_donasi_UseCase, melihat_informasi_umum2_UseCase, melakukan_donasi_UseCase2, mengelola_data_donatur_UseCase1, mengelola_program_donasi_UseCase1, mengelola_data_donasi_UseCase1, mengelola_program_donasi_UseCase2, edit_profil_donatur_UseCase, melihat_informasi_umum_yayasan_UseCase, login_UseCase1, login_UseCase2, tambah_informasi_umum_yayasan_UseCase, donatur_Actor1, registrasi_UseCase, login_UseCase3, manajemen_donasi_UseCase, informasi_donatur_UseCase, melihat_laporan_donasi_UseCase, mengelola_donasi_UseCase, melihat__program_donasi_UseCase, pemilik_yayasan_Actor1, mengelola_inf__umum_yayasan_UseCase, melihat_program_donasi_UseCase, melihat_program_donasi2_UseCase, mengelola_program_donasi_UseCase3, donatur_tetap_Actor, registrasi_UseCase1, melihat__informasi_umum_yayasan_UseCase, verifikasi_donasi_UseCase, cek_status_donasi_UseCase, Component_Component, mengelola_program_donasi_UseCase4, mencetak_laporan_UseCase, melakukan_registrasi__UseCase, mengelola_donasi_UseCase1, mengelola_donasi2_UseCase, Package2_Pemilik_Yayasan_Actor, Package2_mengelola_data_pengurus_UseCase, Package2_mengelola_inf_umum_yayasan_UseCase, Package2_mengelola_program_donasi_UseCase, Package2_mengelola_donatur_UseCase, Package2_Pengurus_Yayasan_Actor, Package2_login_UseCase, Package2_verifikasi_donasi_UseCase},
    associations={pemilik_yayasan_mengelola_data_pengurus, mengelola_program_donasi_pengurus_yayasan, pengurus_yayasan_mengelola_program_donasi, pemilik_yayasan_login, login_pengurus_yayasan, donatur_registrasi, donatur_login, donatur_melakukan_donasi, donatur_tetap_melakukan_donasi, meilhat_riwayat_donasi_donatur_tetap, melihat__laporan_donasi_donatur_tetap, pemilik_yayasan_mengelola_data_pengurus_3, pengurus_yayasan_mengelola_informasi_umum_yayasan2, calon_donatur_donatur_tidak_tetap, donatur_tetap_melihat_data_laporan_donasi, pengelola_yayasan_mengelola_data_donatur, mengelola_laporan_data_donasi_pengelola_yayasan, donatur_tidak_tetap_melihat_data_laporan_donasi, donatur_tidak_tetap_calon_donatur, donatur_tidak_tetap_melihat_informasi_umum, melihat_data_laporan_donasi_donatur_tetap, update_profile_donatur_donatur_tetap, login_pemilik_yayasan, pengelola_yayasan_login, donatur_tetap_login, pemilik_yayasan_mengelola_data_pengurus_2, pengelola_yayasan_mengelola_program_donasi, donatur_tidak_tetap_calon_donatur2, pengurus_yayasan_mengelola_informasi_umum_yayasan, pengurus_yayasan_pengurus_yayasan, pengurus_yayasan_mengelola_data_donasi, mengelola_data_donatur_pengurus_yayasan, pengurus_yayasan_mengelola_program_donasi3, Pemilik_Yayasan_mengelola_data_pengurus, Pengurus_Yayasan_mengelola_inf_umum_yayasan, Pengurus_Yayasan_mengelola_program_donasi, Pengurus_Yayasan_mengelola_donatur, Pengurus_Yayasan_cetak_laporan, Pengurus_Yayasan_konfirmasi_donasi, mengelola_donasi_Pengurus_Yayasan, Pengurus_Yayasan_login, Donatur_login, Donatur_melihat_riwayat_transaksi, Pengunjung_melihat_inf_umum_yayasan, Pengunjung_melihat_laporan_penyaluran_donasi, pengurus_yayasan_mengelola_data_donatur, pengurus_yayasan_mengelola_donasi, donatur_tetap_melihat_riwayat_donasi, donatur_tetap_melihat_informasi_umum_yayasan, donatur_tetap_melihat_program_donasi, melihat__program_donasi_donatur_tidak_tetap, melakukan_donasi_donatur_tidak_tetap, pengurus_yayasan_melakukan_verifikasi_donasi, registrasi_donatur_tidak_tetap, donatur_tetap_meilhat_riwayat_donasi, donatur_tetap_edit_profil_donatur, donatur_tidak_tetap_melihat__informasi_umum_yayasan, pengurus_yayasan_mengelola_program_donasi2, pengurus_yayasan_verifikasi_donasi, donatur_tidak_tetap_cek_status_donasi, pengunjung_melakukan_donasi, pengunjung_melihat__informasi_umum_yayasan, pengunjung_melihat__program_donasi, pengunjung_melihat_data_donasi, Pengunjung_melihat_program_donasi, Donatur_mengubah_profil, Donatur_Tetap_melihat_tagihan_donasi_tetap, Pengunjung_melakukan_donasi, Pengurus_Yayasan_mengelola_inf_umum_yayasan1, Pengurus_Yayasan_mengelola_program_donasi1, Pengurus_Yayasan_mengelola_donatur1, Pengurus_Yayasan_cetak_laporan1, Pengurus_Yayasan_konfirmasi_donasi1, mengelola_donasi_Pengurus_Yayasan1, Pengunjung_melihat_inf_umum_yayasan1, Pengunjung_melihat_laporan_penyaluran_donasi1, Pengunjung_melihat_program_donasi1, Pengunjung_melakukan_donasi1, melihat_riwayat_donasi_Donatur_Tetap},
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