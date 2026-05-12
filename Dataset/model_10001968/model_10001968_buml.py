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
Mahasiswas = Class(name="Mahasiswas")
Jurusans = Class(name="Jurusans")
Prodis = Class(name="Prodis")
Login = Class(name="Login")
masterKategori = Class(name="masterKategori")
Menu_Utama = Class(name="Menu_Utama")
masterBiaya = Class(name="masterBiaya")
Setting = Class(name="Setting")
Pembayarans = Class(name="Pembayarans")
Sistem_Mahasiswa_Login_UseCase = Class(name="Sistem_Mahasiswa_Login_UseCase")
Sistem_Mahasiswa_Masukkan_NIM_UseCase = Class(name="Sistem_Mahasiswa_Masukkan_NIM_UseCase")
Sistem_Mahasiswa_Masukkan_Password_UseCase = Class(name="Sistem_Mahasiswa_Masukkan_Password_UseCase")
Sistem_Mahasiswa_Melihat_Informasi_UseCase = Class(name="Sistem_Mahasiswa_Melihat_Informasi_UseCase")
Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase = Class(name="Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase")
Sistem_Mahasiswa_Ganti_Password_UseCase = Class(name="Sistem_Mahasiswa_Ganti_Password_UseCase")
Mahasiswa_Actor = Class(name="Mahasiswa_Actor")
Sistem_Pembayaran_Login_UseCase = Class(name="Sistem_Pembayaran_Login_UseCase")
Sistem_Pembayaran_Masukkan_Username_Email_UseCase = Class(name="Sistem_Pembayaran_Masukkan_Username_Email_UseCase")
Sistem_Pembayaran_Masukkan_Password_UseCase = Class(name="Sistem_Pembayaran_Masukkan_Password_UseCase")
Sistem_Pembayaran_Kategori_Biaya_UseCase = Class(name="Sistem_Pembayaran_Kategori_Biaya_UseCase")
Sistem_Pembayaran_Biaya_Kuliah_UseCase = Class(name="Sistem_Pembayaran_Biaya_Kuliah_UseCase")
Sistem_Pembayaran_Prodi_UseCase = Class(name="Sistem_Pembayaran_Prodi_UseCase")
Sistem_Pembayaran_Jurusan_UseCase = Class(name="Sistem_Pembayaran_Jurusan_UseCase")
Sistem_Pembayaran_Mahasiswa_UseCase = Class(name="Sistem_Pembayaran_Mahasiswa_UseCase")
Sistem_Pembayaran_Pembayaran_UseCase = Class(name="Sistem_Pembayaran_Pembayaran_UseCase")
Sistem_Pembayaran_Setting_UseCase = Class(name="Sistem_Pembayaran_Setting_UseCase")
Sistem_Pembayaran_Add_Role_UseCase = Class(name="Sistem_Pembayaran_Add_Role_UseCase")
Sistem_Pembayaran_Add_User_UseCase = Class(name="Sistem_Pembayaran_Add_User_UseCase")
Administrator_Actor = Class(name="Administrator_Actor")
Tata_Usaha_Actor = Class(name="Tata_Usaha_Actor")

# Mahasiswas class attributes and methods
Mahasiswas_id: Property = Property(name="id", type=IntegerType)
Mahasiswas.attributes={Mahasiswas_id}

# Jurusans class attributes and methods
Jurusans_id: Property = Property(name="id", type=IntegerType)
Jurusans_prodi_id: Property = Property(name="prodi_id", type=IntegerType)
Jurusans_jurusan_name: Property = Property(name="jurusan_name", type=StringType)
Jurusans.attributes={Jurusans_jurusan_name, Jurusans_id, Jurusans_prodi_id}

# Prodis class attributes and methods
Prodis_id: Property = Property(name="id", type=IntegerType)
Prodis_prodi_name: Property = Property(name="prodi_name", type=StringType)
Prodis_kapasitas_max: Property = Property(name="kapasitas_max", type=IntegerType)
Prodis_status: Property = Property(name="status", type=IntegerType)
Prodis_user_id: Property = Property(name="user_id", type=IntegerType)
Prodis.attributes={Prodis_prodi_name, Prodis_user_id, Prodis_id, Prodis_kapasitas_max, Prodis_status}

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_username, Login_password}

# masterKategori class attributes and methods
masterKategori_id: Property = Property(name="id", type=IntegerType)
masterKategori_nama_kategori: Property = Property(name="nama_kategori", type=StringType)
masterKategori_status: Property = Property(name="status", type=IntegerType)
masterKategori_user_id: Property = Property(name="user_id", type=IntegerType)
masterKategori.attributes={masterKategori_nama_kategori, masterKategori_status, masterKategori_user_id, masterKategori_id}

# Menu_Utama class attributes and methods

# masterBiaya class attributes and methods
masterBiaya_id: Property = Property(name="id", type=IntegerType)
masterBiaya_kategori_id: Property = Property(name="kategori_id", type=IntegerType)
masterBiaya_nama_biaya: Property = Property(name="nama_biaya", type=StringType)
masterBiaya_jml_bayar: Property = Property(name="jml_bayar", type=IntegerType)
masterBiaya_jumlah_biaya: Property = Property(name="jumlah_biaya", type=IntegerType)
masterBiaya_status: Property = Property(name="status", type=IntegerType)
masterBiaya_user_id: Property = Property(name="user_id", type=IntegerType)
masterBiaya.attributes={masterBiaya_jml_bayar, masterBiaya_id, masterBiaya_nama_biaya, masterBiaya_kategori_id, masterBiaya_user_id, masterBiaya_status, masterBiaya_jumlah_biaya}

# Setting class attributes and methods
Setting_id: Property = Property(name="id", type=IntegerType)
Setting_nama: Property = Property(name="nama", type=StringType)
Setting_alamat: Property = Property(name="alamat", type=StringType)
Setting_no_telepon: Property = Property(name="no_telepon", type=StringType)
Setting_no_faximile: Property = Property(name="no_faximile", type=StringType)
Setting_email: Property = Property(name="email", type=StringType)
Setting_logo_kampus: Property = Property(name="logo_kampus", type=StringType)
Setting_user_id: Property = Property(name="user_id", type=IntegerType)
Setting.attributes={Setting_logo_kampus, Setting_nama, Setting_user_id, Setting_no_telepon, Setting_no_faximile, Setting_alamat, Setting_id, Setting_email}

# Pembayarans class attributes and methods
Pembayarans_id: Property = Property(name="id", type=IntegerType)
Pembayarans_prefix: Property = Property(name="prefix", type=StringType)
Pembayarans_no_pembayaran: Property = Property(name="no_pembayaran", type=StringType)
Pembayarans_tanggal_pembayaran: Property = Property(name="tanggal_pembayaran", type=StringType)
Pembayarans_mahasiswa_id: Property = Property(name="mahasiswa_id", type=IntegerType)
Pembayarans_pembayaran_tipe: Property = Property(name="pembayaran_tipe", type=IntegerType)
Pembayarans_semester_id: Property = Property(name="semester_id", type=IntegerType)
Pembayarans_biaya_kuliah_id: Property = Property(name="biaya_kuliah_id", type=IntegerType)
Pembayarans_keterangan: Property = Property(name="keterangan", type=StringType)
Pembayarans_jumlah: Property = Property(name="jumlah", type=IntegerType)
Pembayarans_status: Property = Property(name="status", type=IntegerType)
Pembayarans_user_id: Property = Property(name="user_id", type=IntegerType)
Pembayarans.attributes={Pembayarans_mahasiswa_id, Pembayarans_prefix, Pembayarans_biaya_kuliah_id, Pembayarans_no_pembayaran, Pembayarans_tanggal_pembayaran, Pembayarans_user_id, Pembayarans_id, Pembayarans_jumlah, Pembayarans_pembayaran_tipe, Pembayarans_keterangan, Pembayarans_status, Pembayarans_semester_id}

# Sistem_Mahasiswa_Login_UseCase class attributes and methods

# Sistem_Mahasiswa_Masukkan_NIM_UseCase class attributes and methods

# Sistem_Mahasiswa_Masukkan_Password_UseCase class attributes and methods

# Sistem_Mahasiswa_Melihat_Informasi_UseCase class attributes and methods

# Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase class attributes and methods

# Sistem_Mahasiswa_Ganti_Password_UseCase class attributes and methods

# Mahasiswa_Actor class attributes and methods

# Sistem_Pembayaran_Login_UseCase class attributes and methods

# Sistem_Pembayaran_Masukkan_Username_Email_UseCase class attributes and methods

# Sistem_Pembayaran_Masukkan_Password_UseCase class attributes and methods

# Sistem_Pembayaran_Kategori_Biaya_UseCase class attributes and methods

# Sistem_Pembayaran_Biaya_Kuliah_UseCase class attributes and methods

# Sistem_Pembayaran_Prodi_UseCase class attributes and methods

# Sistem_Pembayaran_Jurusan_UseCase class attributes and methods

# Sistem_Pembayaran_Mahasiswa_UseCase class attributes and methods

# Sistem_Pembayaran_Pembayaran_UseCase class attributes and methods

# Sistem_Pembayaran_Setting_UseCase class attributes and methods

# Sistem_Pembayaran_Add_Role_UseCase class attributes and methods

# Sistem_Pembayaran_Add_User_UseCase class attributes and methods

# Administrator_Actor class attributes and methods

# Tata_Usaha_Actor class attributes and methods

# Relationships
Administrator_Kategori_Biaya: BinaryAssociation = BinaryAssociation(
    name="Administrator_Kategori_Biaya",
    ends={
        Property(name="kategori_Biaya10", type=Sistem_Pembayaran_Kategori_Biaya_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator11", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Biaya_Kuliah: BinaryAssociation = BinaryAssociation(
    name="Administrator_Biaya_Kuliah",
    ends={
        Property(name="biaya_Kuliah12", type=Sistem_Pembayaran_Biaya_Kuliah_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator13", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Setting: BinaryAssociation = BinaryAssociation(
    name="Administrator_Setting",
    ends={
        Property(name="setting14", type=Sistem_Pembayaran_Setting_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator15", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Prodi: BinaryAssociation = BinaryAssociation(
    name="Administrator_Prodi",
    ends={
        Property(name="prodi16", type=Sistem_Pembayaran_Prodi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator17", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Jurusan: BinaryAssociation = BinaryAssociation(
    name="Administrator_Jurusan",
    ends={
        Property(name="jurusan18", type=Sistem_Pembayaran_Jurusan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator19", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Mahasiswa: BinaryAssociation = BinaryAssociation(
    name="Administrator_Mahasiswa",
    ends={
        Property(name="mahasiswa20", type=Sistem_Pembayaran_Mahasiswa_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator21", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Pembayaran: BinaryAssociation = BinaryAssociation(
    name="Administrator_Pembayaran",
    ends={
        Property(name="pembayaran22", type=Sistem_Pembayaran_Pembayaran_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator23", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Add_Role: BinaryAssociation = BinaryAssociation(
    name="Administrator_Add_Role",
    ends={
        Property(name="add_Role24", type=Sistem_Pembayaran_Add_Role_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator25", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Add_User: BinaryAssociation = BinaryAssociation(
    name="Administrator_Add_User",
    ends={
        Property(name="add_User26", type=Sistem_Pembayaran_Add_User_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator27", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tata_Usaha_Login: BinaryAssociation = BinaryAssociation(
    name="Tata_Usaha_Login",
    ends={
        Property(name="login28", type=Sistem_Pembayaran_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tata_Usaha29", type=Tata_Usaha_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tata_Usaha_Jurusan: BinaryAssociation = BinaryAssociation(
    name="Tata_Usaha_Jurusan",
    ends={
        Property(name="jurusan30", type=Sistem_Pembayaran_Jurusan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tata_Usaha31", type=Tata_Usaha_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tata_Usaha_Pembayaran: BinaryAssociation = BinaryAssociation(
    name="Tata_Usaha_Pembayaran",
    ends={
        Property(name="pembayaran32", type=Sistem_Pembayaran_Pembayaran_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tata_Usaha33", type=Tata_Usaha_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tata_Usaha_Kategori_Biaya: BinaryAssociation = BinaryAssociation(
    name="Tata_Usaha_Kategori_Biaya",
    ends={
        Property(name="kategori_Biaya34", type=Sistem_Pembayaran_Kategori_Biaya_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tata_Usaha35", type=Tata_Usaha_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tata_Usaha_Biaya_Kuliah: BinaryAssociation = BinaryAssociation(
    name="Tata_Usaha_Biaya_Kuliah",
    ends={
        Property(name="biaya_Kuliah36", type=Sistem_Pembayaran_Biaya_Kuliah_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tata_Usaha37", type=Tata_Usaha_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Tata_Usaha_Prodi: BinaryAssociation = BinaryAssociation(
    name="Tata_Usaha_Prodi",
    ends={
        Property(name="prodi38", type=Sistem_Pembayaran_Prodi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="tata_Usaha39", type=Tata_Usaha_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mahasiswa_Login: BinaryAssociation = BinaryAssociation(
    name="Mahasiswa_Login",
    ends={
        Property(name="login0", type=Sistem_Mahasiswa_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="mahasiswa1", type=Mahasiswa_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mahasiswa_Melihat_Informasi: BinaryAssociation = BinaryAssociation(
    name="Mahasiswa_Melihat_Informasi",
    ends={
        Property(name="melihat_Informasi2", type=Sistem_Mahasiswa_Melihat_Informasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="mahasiswa3", type=Mahasiswa_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mahasiswa_Update_Data_Mahasiswa: BinaryAssociation = BinaryAssociation(
    name="Mahasiswa_Update_Data_Mahasiswa",
    ends={
        Property(name="update_Data_Mahasiswa4", type=Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="mahasiswa5", type=Mahasiswa_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mahasiswa_Ganti_Password: BinaryAssociation = BinaryAssociation(
    name="Mahasiswa_Ganti_Password",
    ends={
        Property(name="ganti_Password6", type=Sistem_Mahasiswa_Ganti_Password_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="mahasiswa7", type=Mahasiswa_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Administrator_Login: BinaryAssociation = BinaryAssociation(
    name="Administrator_Login",
    ends={
        Property(name="login8", type=Sistem_Pembayaran_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="administrator9", type=Administrator_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_gMOqgHorEemKc6sUMthxaw",
    types={Mahasiswas, Jurusans, Prodis, Login, masterKategori, Menu_Utama, masterBiaya, Setting, Pembayarans, Sistem_Mahasiswa_Login_UseCase, Sistem_Mahasiswa_Masukkan_NIM_UseCase, Sistem_Mahasiswa_Masukkan_Password_UseCase, Sistem_Mahasiswa_Melihat_Informasi_UseCase, Sistem_Mahasiswa_Update_Data_Mahasiswa_UseCase, Sistem_Mahasiswa_Ganti_Password_UseCase, Mahasiswa_Actor, Sistem_Pembayaran_Login_UseCase, Sistem_Pembayaran_Masukkan_Username_Email_UseCase, Sistem_Pembayaran_Masukkan_Password_UseCase, Sistem_Pembayaran_Kategori_Biaya_UseCase, Sistem_Pembayaran_Biaya_Kuliah_UseCase, Sistem_Pembayaran_Prodi_UseCase, Sistem_Pembayaran_Jurusan_UseCase, Sistem_Pembayaran_Mahasiswa_UseCase, Sistem_Pembayaran_Pembayaran_UseCase, Sistem_Pembayaran_Setting_UseCase, Sistem_Pembayaran_Add_Role_UseCase, Sistem_Pembayaran_Add_User_UseCase, Administrator_Actor, Tata_Usaha_Actor},
    associations={Administrator_Kategori_Biaya, Administrator_Biaya_Kuliah, Administrator_Setting, Administrator_Prodi, Administrator_Jurusan, Administrator_Mahasiswa, Administrator_Pembayaran, Administrator_Add_Role, Administrator_Add_User, Tata_Usaha_Login, Tata_Usaha_Jurusan, Tata_Usaha_Pembayaran, Tata_Usaha_Kategori_Biaya, Tata_Usaha_Biaya_Kuliah, Tata_Usaha_Prodi, Mahasiswa_Login, Mahasiswa_Melihat_Informasi, Mahasiswa_Update_Data_Mahasiswa, Mahasiswa_Ganti_Password, Administrator_Login},
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