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
Melakukan_Logout_UseCase = Class(name="Melakukan_Logout_UseCase")
Buku_berbahasa_Asing_UseCase = Class(name="Buku_berbahasa_Asing_UseCase")
Melakukan_Penerjemahan_Buku_Bacaan_UseCase = Class(name="Melakukan_Penerjemahan_Buku_Bacaan_UseCase")
Login = Class(name="Login")
Class_ = Class(name="Class")
MyClass = Class(name="MyClass")
Menu_Utama = Class(name="Menu_Utama")
Profil = Class(name="Profil")
Login1 = Class(name="Login1")
Buku = Class(name="Buku")
Keluar = Class(name="Keluar")
User_Actor = Class(name="User_Actor")
Melakukan_Login_UseCase = Class(name="Melakukan_Login_UseCase")
Melihat_Tampilan_Awal_Aplikasi_UseCase = Class(name="Melihat_Tampilan_Awal_Aplikasi_UseCase")
Memilih_Kategori_Buku_UseCase = Class(name="Memilih_Kategori_Buku_UseCase")
Mulai_Membaca_UseCase = Class(name="Mulai_Membaca_UseCase")
Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase = Class(name="Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase")

# Melakukan_Logout_UseCase class attributes and methods

# Buku_berbahasa_Asing_UseCase class attributes and methods

# Melakukan_Penerjemahan_Buku_Bacaan_UseCase class attributes and methods

# Login class attributes and methods
Login_username: Property = Property(name="username", type=StringType)
Login_password: Property = Property(name="password", type=StringType)
Login.attributes={Login_password, Login_username}

# Class class attributes and methods

# MyClass class attributes and methods

# Menu_Utama class attributes and methods

# Profil class attributes and methods
Profil_Biodata: Property = Property(name="Biodata", type=StringType)
Profil.attributes={Profil_Biodata}

# Login1 class attributes and methods
Login1_usernam: Property = Property(name="usernam", type=StringType)
Login1_password: Property = Property(name="password", type=StringType)
Login1.attributes={Login1_password, Login1_usernam}

# Buku class attributes and methods

# Keluar class attributes and methods
Keluar_Keluar: Property = Property(name="Keluar", type=StringType)
Keluar.attributes={Keluar_Keluar}

# User_Actor class attributes and methods

# Melakukan_Login_UseCase class attributes and methods

# Melihat_Tampilan_Awal_Aplikasi_UseCase class attributes and methods

# Memilih_Kategori_Buku_UseCase class attributes and methods

# Mulai_Membaca_UseCase class attributes and methods

# Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase class attributes and methods

# Relationships
User_Melakukan_Login: BinaryAssociation = BinaryAssociation(
    name="User_Melakukan_Login",
    ends={
        Property(name="melakukan_Login0", type=Melakukan_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Melihat_Tampilan_Awal_Aplikasi: BinaryAssociation = BinaryAssociation(
    name="User_Melihat_Tampilan_Awal_Aplikasi",
    ends={
        Property(name="melihat_Tampilan_Awal_Aplikasi2", type=Melihat_Tampilan_Awal_Aplikasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user3", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Memilih_Kategori_Buku: BinaryAssociation = BinaryAssociation(
    name="User_Memilih_Kategori_Buku",
    ends={
        Property(name="memilih_Kategori_Buku4", type=Memilih_Kategori_Buku_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user5", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
User_Melakukan_Logout: BinaryAssociation = BinaryAssociation(
    name="User_Melakukan_Logout",
    ends={
        Property(name="melakukan_Logout6", type=Melakukan_Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="user7", type=User_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Melakukan_Login_Melihat_Tampilan_Awal_Aplikasi: BinaryAssociation = BinaryAssociation(
    name="Melakukan_Login_Melihat_Tampilan_Awal_Aplikasi",
    ends={
        Property(name="melihat_Tampilan_Awal_Aplikasi8", type=Melihat_Tampilan_Awal_Aplikasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="melakukan_Login9", type=Melakukan_Login_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Melihat_Tampilan_Awal_Aplikasi_Memilih_Kategori_Buku: BinaryAssociation = BinaryAssociation(
    name="Melihat_Tampilan_Awal_Aplikasi_Memilih_Kategori_Buku",
    ends={
        Property(name="memilih_Kategori_Buku10", type=Memilih_Kategori_Buku_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="melihat_Tampilan_Awal_Aplikasi11", type=Melihat_Tampilan_Awal_Aplikasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Memilih_Kategori_Buku_Mulai_Membaca: BinaryAssociation = BinaryAssociation(
    name="Memilih_Kategori_Buku_Mulai_Membaca",
    ends={
        Property(name="mulai_Membaca12", type=Mulai_Membaca_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="memilih_Kategori_Buku13", type=Memilih_Kategori_Buku_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Mulai_Membaca_Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial: BinaryAssociation = BinaryAssociation(
    name="Mulai_Membaca_Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial",
    ends={
        Property(name="otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial14", type=Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="mulai_Membaca15", type=Mulai_Membaca_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_Melakukan_Logout: BinaryAssociation = BinaryAssociation(
    name="Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_Melakukan_Logout",
    ends={
        Property(name="melakukan_Logout16", type=Melakukan_Logout_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial17", type=Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="c05e4fa0_4ec3_47a0_ae4d_5091b85fb55a",
    types={Melakukan_Logout_UseCase, Buku_berbahasa_Asing_UseCase, Melakukan_Penerjemahan_Buku_Bacaan_UseCase, Login, Class_, MyClass, Menu_Utama, Profil, Login1, Buku, Keluar, User_Actor, Melakukan_Login_UseCase, Melihat_Tampilan_Awal_Aplikasi_UseCase, Memilih_Kategori_Buku_UseCase, Mulai_Membaca_UseCase, Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_UseCase},
    associations={User_Melakukan_Login, User_Melihat_Tampilan_Awal_Aplikasi, User_Memilih_Kategori_Buku, User_Melakukan_Logout, Melakukan_Login_Melihat_Tampilan_Awal_Aplikasi, Melihat_Tampilan_Awal_Aplikasi_Memilih_Kategori_Buku, Memilih_Kategori_Buku_Mulai_Membaca, Mulai_Membaca_Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial, Otomatis_Menginterupsi_Notifikasi_Akun_Media_Sosial_Melakukan_Logout},
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