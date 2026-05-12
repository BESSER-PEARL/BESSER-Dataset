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
RentalMobil = Class(name="RentalMobil")
Login = Class(name="Login")
Pemilik = Class(name="Pemilik")
Admin = Class(name="Admin")
Pelanggan = Class(name="Pelanggan")
Administrasi = Class(name="Administrasi")
Pesan = Class(name="Pesan")
Kendaraan = Class(name="Kendaraan")

# RentalMobil class attributes and methods
RentalMobil_Nama: Property = Property(name="Nama", type=StringType)
RentalMobil_Alamat: Property = Property(name="Alamat", type=StringType)
RentalMobil_Telepon: Property = Property(name="Telepon", type=StringType)
RentalMobil_Email: Property = Property(name="Email", type=StringType)
RentalMobil.attributes={RentalMobil_Email, RentalMobil_Telepon, RentalMobil_Alamat, RentalMobil_Nama}

# Login class attributes and methods
Login_Username: Property = Property(name="Username", type=StringType)
Login_Password: Property = Property(name="Password", type=StringType)
Login.attributes={Login_Username, Login_Password}

# Pemilik class attributes and methods
Pemilik_Username: Property = Property(name="Username", type=StringType)
Pemilik_Password: Property = Property(name="Password", type=StringType)
Pemilik.attributes={Pemilik_Password, Pemilik_Username}

# Admin class attributes and methods
Admin_Username: Property = Property(name="Username", type=StringType)
Admin_Password: Property = Property(name="Password", type=StringType)
Admin.attributes={Admin_Password, Admin_Username}

# Pelanggan class attributes and methods
Pelanggan_Username: Property = Property(name="Username", type=StringType)
Pelanggan_Password: Property = Property(name="Password", type=StringType)
Pelanggan_IdPelanggan: Property = Property(name="IdPelanggan", type=IntegerType)
Pelanggan_NoKTP: Property = Property(name="NoKTP", type=StringType)
Pelanggan_JenisKelamin: Property = Property(name="JenisKelamin", type=StringType)
Pelanggan_Umur: Property = Property(name="Umur", type=IntegerType)
Pelanggan_Pekerjaan: Property = Property(name="Pekerjaan", type=StringType)
Pelanggan_Alamat: Property = Property(name="Alamat", type=StringType)
Pelanggan_Telepon: Property = Property(name="Telepon", type=StringType)
Pelanggan.attributes={Pelanggan_IdPelanggan, Pelanggan_Password, Pelanggan_Pekerjaan, Pelanggan_NoKTP, Pelanggan_Alamat, Pelanggan_Username, Pelanggan_JenisKelamin, Pelanggan_Telepon, Pelanggan_Umur}

# Administrasi class attributes and methods
Administrasi_IdAdmin: Property = Property(name="IdAdmin", type=IntegerType)
Administrasi_NoPesan: Property = Property(name="NoPesan", type=IntegerType)
Administrasi_IdPelanggan: Property = Property(name="IdPelanggan", type=IntegerType)
Administrasi_HargaSewa: Property = Property(name="HargaSewa", type=StringType)
Administrasi_Bayar: Property = Property(name="Bayar", type=StringType)
Administrasi_Kembali: Property = Property(name="Kembali", type=StringType)
Administrasi.attributes={Administrasi_Bayar, Administrasi_Kembali, Administrasi_IdAdmin, Administrasi_HargaSewa, Administrasi_IdPelanggan, Administrasi_NoPesan}

# Pesan class attributes and methods
Pesan_NoPesan: Property = Property(name="NoPesan", type=IntegerType)
Pesan_IdPelanggan: Property = Property(name="IdPelanggan", type=IntegerType)
Pesan_TanggalRental: Property = Property(name="TanggalRental", type=StringType)
Pesan_TanggalKembali: Property = Property(name="TanggalKembali", type=StringType)
Pesan.attributes={Pesan_NoPesan, Pesan_TanggalKembali, Pesan_IdPelanggan, Pesan_TanggalRental}

# Kendaraan class attributes and methods
Kendaraan_NoMesin: Property = Property(name="NoMesin", type=StringType)
Kendaraan_NoRangka: Property = Property(name="NoRangka", type=StringType)
Kendaraan_NoPolisi: Property = Property(name="NoPolisi", type=StringType)
Kendaraan_Merk: Property = Property(name="Merk", type=StringType)
Kendaraan_Warna: Property = Property(name="Warna", type=StringType)
Kendaraan_TahunPembuatan: Property = Property(name="TahunPembuatan", type=StringType)
Kendaraan.attributes={Kendaraan_TahunPembuatan, Kendaraan_NoRangka, Kendaraan_Warna, Kendaraan_NoPolisi, Kendaraan_NoMesin, Kendaraan_Merk}

# Relationships
Admin_Pelanggan: BinaryAssociation = BinaryAssociation(
    name="Admin_Pelanggan",
    ends={
        Property(name="admin3", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="pelanggan2", type=Pelanggan, multiplicity=Multiplicity(1, 9999))
    }
)
Pelanggan_Kendaraan: BinaryAssociation = BinaryAssociation(
    name="Pelanggan_Kendaraan",
    ends={
        Property(name="kendaraan4", type=Kendaraan, multiplicity=Multiplicity(1, 9999)),
        Property(name="pelanggan5", type=Pelanggan, multiplicity=Multiplicity(0, 1))
    }
)
Kendaraan_Pesan: BinaryAssociation = BinaryAssociation(
    name="Kendaraan_Pesan",
    ends={
        Property(name="pesan6", type=Pesan, multiplicity=Multiplicity(1, 1)),
        Property(name="kendaraan7", type=Kendaraan, multiplicity=Multiplicity(1, 9999))
    }
)
Administrasi_Pesan: BinaryAssociation = BinaryAssociation(
    name="Administrasi_Pesan",
    ends={
        Property(name="pesan8", type=Pesan, multiplicity=Multiplicity(1, 1)),
        Property(name="administrasi9", type=Administrasi, multiplicity=Multiplicity(1, 1))
    }
)
Pelanggan_Pesan: BinaryAssociation = BinaryAssociation(
    name="Pelanggan_Pesan",
    ends={
        Property(name="pesan10", type=Pesan, multiplicity=Multiplicity(1, 9999)),
        Property(name="pelanggan11", type=Pelanggan, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Pesan: BinaryAssociation = BinaryAssociation(
    name="Admin_Pesan",
    ends={
        Property(name="pesan12", type=Pesan, multiplicity=Multiplicity(1, 1)),
        Property(name="admin13", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Administrasi: BinaryAssociation = BinaryAssociation(
    name="Admin_Administrasi",
    ends={
        Property(name="administrasi14", type=Administrasi, multiplicity=Multiplicity(1, 1)),
        Property(name="admin15", type=Admin, multiplicity=Multiplicity(1, 1))
    }
)
Pemilik_Admin: BinaryAssociation = BinaryAssociation(
    name="Pemilik_Admin",
    ends={
        Property(name="admin0", type=Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="pemilik1", type=Pemilik, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6_kVMNgEEei47sN0sCkjiA",
    types={RentalMobil, Login, Pemilik, Admin, Pelanggan, Administrasi, Pesan, Kendaraan},
    associations={Admin_Pelanggan, Pelanggan_Kendaraan, Kendaraan_Pesan, Administrasi_Pesan, Pelanggan_Pesan, Admin_Pesan, Admin_Administrasi, Pemilik_Admin},
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