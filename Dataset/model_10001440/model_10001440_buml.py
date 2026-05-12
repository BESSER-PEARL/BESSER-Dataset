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
Melakukan_Login_UseCase = Class(name="Melakukan_Login_UseCase")
Melakukan_Registrasi_UseCase = Class(name="Melakukan_Registrasi_UseCase")
Pelanggan__Actor = Class(name="Pelanggan__Actor")
Admin_Actor = Class(name="Admin_Actor")
Mengentry_Data_UseCase = Class(name="Mengentry_Data_UseCase")
Memverivikasi_Data_UseCase = Class(name="Memverivikasi_Data_UseCase")
Melakukan_Transaksi_UseCase = Class(name="Melakukan_Transaksi_UseCase")
Memproses_Database_UseCase = Class(name="Memproses_Database_UseCase")
Cetak_Slip_UseCase = Class(name="Cetak_Slip_UseCase")
Login_Admin = Class(name="Login_Admin")
Admin = Class(name="Admin")
Pelanggan = Class(name="Pelanggan")
Data_Pembayaran = Class(name="Data_Pembayaran")

# Melakukan_Login_UseCase class attributes and methods

# Melakukan_Registrasi_UseCase class attributes and methods

# Pelanggan__Actor class attributes and methods

# Admin_Actor class attributes and methods

# Mengentry_Data_UseCase class attributes and methods

# Memverivikasi_Data_UseCase class attributes and methods

# Melakukan_Transaksi_UseCase class attributes and methods

# Memproses_Database_UseCase class attributes and methods

# Cetak_Slip_UseCase class attributes and methods

# Login_Admin class attributes and methods
Login_Admin_User_name: Property = Property(name="User_name", type=StringType)
Login_Admin_attribute: Property = Property(name="attribute", type=StringType)
Login_Admin.attributes={Login_Admin_User_name, Login_Admin_attribute}

# Admin class attributes and methods
Admin_id: Property = Property(name="id", type=StringType)
Admin_nama: Property = Property(name="nama", type=StringType)
Admin_alamat: Property = Property(name="alamat", type=StringType)
Admin_no_tlp: Property = Property(name="no_tlp", type=IntegerType)
Admin.attributes={Admin_no_tlp, Admin_nama, Admin_alamat, Admin_id}

# Pelanggan class attributes and methods
Pelanggan_kode_pelanggan: Property = Property(name="kode_pelanggan", type=StringType)
Pelanggan_nama: Property = Property(name="nama", type=StringType)
Pelanggan_alamat: Property = Property(name="alamat", type=StringType)
Pelanggan.attributes={Pelanggan_nama, Pelanggan_alamat, Pelanggan_kode_pelanggan}

# Data_Pembayaran class attributes and methods
Data_Pembayaran_kode_bayar: Property = Property(name="kode_bayar", type=StringType)
Data_Pembayaran_tanggal_bayar: Property = Property(name="tanggal_bayar", type=StringType)
Data_Pembayaran_kode_kredit: Property = Property(name="kode_kredit", type=StringType)
Data_Pembayaran_angsuran: Property = Property(name="angsuran", type=IntegerType)
Data_Pembayaran_angsuranke: Property = Property(name="angsuranke", type=IntegerType)
Data_Pembayaran_keterangan: Property = Property(name="keterangan", type=StringType)
Data_Pembayaran.attributes={Data_Pembayaran_kode_bayar, Data_Pembayaran_angsuran, Data_Pembayaran_keterangan, Data_Pembayaran_angsuranke, Data_Pembayaran_tanggal_bayar, Data_Pembayaran_kode_kredit}

# Relationships
Melakukan_Registrasi_Admin: BinaryAssociation = BinaryAssociation(
    name="Melakukan_Registrasi_Admin",
    ends={
        Property(name="admin8", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="melakukan_Registrasi9", type=Melakukan_Registrasi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Mengentry_Data: BinaryAssociation = BinaryAssociation(
    name="Admin_Mengentry_Data",
    ends={
        Property(name="mengentry_Data10", type=Mengentry_Data_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin11", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Memverivikasi_Data: BinaryAssociation = BinaryAssociation(
    name="Admin_Memverivikasi_Data",
    ends={
        Property(name="memverivikasi_Data12", type=Memverivikasi_Data_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin13", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Melakukan_Transaksi_Admin: BinaryAssociation = BinaryAssociation(
    name="Melakukan_Transaksi_Admin",
    ends={
        Property(name="admin14", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="melakukan_Transaksi15", type=Melakukan_Transaksi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Memproses_Database_Admin: BinaryAssociation = BinaryAssociation(
    name="Memproses_Database_Admin",
    ends={
        Property(name="admin16", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="memproses_Database17", type=Memproses_Database_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Cetak_Slip_Admin: BinaryAssociation = BinaryAssociation(
    name="Cetak_Slip_Admin",
    ends={
        Property(name="admin18", type=Admin_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="cetak_Slip19", type=Cetak_Slip_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Login_Admin: BinaryAssociation = BinaryAssociation(
    name="Admin_Login_Admin",
    ends={
        Property(name="login_Admin20", type=Login_Admin, multiplicity=Multiplicity(1, 1)),
        Property(name="admin21", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Pelanggan: BinaryAssociation = BinaryAssociation(
    name="Admin_Pelanggan",
    ends={
        Property(name="pelanggan22", type=Pelanggan, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin23", type=Admin, multiplicity=Multiplicity(1, 9999))
    }
)
Pelanggan_Data_Pembayaran: BinaryAssociation = BinaryAssociation(
    name="Pelanggan_Data_Pembayaran",
    ends={
        Property(name="data_Pembayaran24", type=Data_Pembayaran, multiplicity=Multiplicity(1, 1)),
        Property(name="pelanggan25", type=Pelanggan, multiplicity=Multiplicity(1, 1))
    }
)
Admin_Data_Pembayaran: BinaryAssociation = BinaryAssociation(
    name="Admin_Data_Pembayaran",
    ends={
        Property(name="data_Pembayaran26", type=Data_Pembayaran, multiplicity=Multiplicity(1, 9999)),
        Property(name="admin27", type=Admin, multiplicity=Multiplicity(1, 9999))
    }
)
Pelanggan__Melakukan_Registrasi: BinaryAssociation = BinaryAssociation(
    name="Pelanggan__Melakukan_Registrasi",
    ends={
        Property(name="melakukan_Registrasi0", type=Melakukan_Registrasi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pelanggan1", type=Pelanggan__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pelanggan__Memverivikasi_Data: BinaryAssociation = BinaryAssociation(
    name="Pelanggan__Memverivikasi_Data",
    ends={
        Property(name="memverivikasi_Data2", type=Memverivikasi_Data_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pelanggan3", type=Pelanggan__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Pelanggan__Melakukan_Transaksi: BinaryAssociation = BinaryAssociation(
    name="Pelanggan__Melakukan_Transaksi",
    ends={
        Property(name="melakukan_Transaksi4", type=Melakukan_Transaksi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="pelanggan5", type=Pelanggan__Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Melakukan_Login: BinaryAssociation = BinaryAssociation(
    name="Admin_Melakukan_Login",
    ends={
        Property(name="melakukan_Login6", type=Melakukan_Login_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin7", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_6elVMOh5EeiV94kHgjpOMg",
    types={Melakukan_Login_UseCase, Melakukan_Registrasi_UseCase, Pelanggan__Actor, Admin_Actor, Mengentry_Data_UseCase, Memverivikasi_Data_UseCase, Melakukan_Transaksi_UseCase, Memproses_Database_UseCase, Cetak_Slip_UseCase, Login_Admin, Admin, Pelanggan, Data_Pembayaran},
    associations={Melakukan_Registrasi_Admin, Admin_Mengentry_Data, Admin_Memverivikasi_Data, Melakukan_Transaksi_Admin, Memproses_Database_Admin, Cetak_Slip_Admin, Admin_Login_Admin, Admin_Pelanggan, Pelanggan_Data_Pembayaran, Admin_Data_Pembayaran, Pelanggan__Melakukan_Registrasi, Pelanggan__Memverivikasi_Data, Pelanggan__Melakukan_Transaksi, Admin_Melakukan_Login},
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