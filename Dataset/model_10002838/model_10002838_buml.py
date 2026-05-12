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
barang = Class(name="barang")
user = Class(name="user")
pelanggan = Class(name="pelanggan")
supplier = Class(name="supplier")
transaksi = Class(name="transaksi")
sistem = Class(name="sistem")
masuk = Class(name="masuk")
keluar = Class(name="keluar")

# barang class attributes and methods
barang_id_barang: Property = Property(name="id_barang", type=StringType)
barang_nama_barang: Property = Property(name="nama_barang", type=barang)
barang_kategori: Property = Property(name="kategori", type=StringType)
barang_stok: Property = Property(name="stok", type=IntegerType)
barang_harga: Property = Property(name="harga", type=IntegerType)
barang_satuan: Property = Property(name="satuan", type=StringType)
barang.attributes={barang_harga, barang_satuan, barang_id_barang, barang_nama_barang, barang_stok, barang_kategori}

# user class attributes and methods
user_id_user: Property = Property(name="id_user", type=IntegerType)
user_username: Property = Property(name="username", type=StringType)
user_password: Property = Property(name="password", type=StringType)
user_nama_user: Property = Property(name="nama_user", type=StringType)
user.attributes={user_password, user_id_user, user_username, user_nama_user}

# pelanggan class attributes and methods
pelanggan_id_pelanggan: Property = Property(name="id_pelanggan", type=IntegerType)
pelanggan_nama_pelanggan: Property = Property(name="nama_pelanggan", type=pelanggan)
pelanggan_alamat: Property = Property(name="alamat", type=StringType)
pelanggan_no_telp_pelanggan: Property = Property(name="no_telp_pelanggan", type=StringType)
pelanggan.attributes={pelanggan_alamat, pelanggan_no_telp_pelanggan, pelanggan_nama_pelanggan, pelanggan_id_pelanggan}

# supplier class attributes and methods
supplier_id_supplier: Property = Property(name="id_supplier", type=IntegerType)
supplier_nama_supplier: Property = Property(name="nama_supplier", type=supplier)
supplier_alamat: Property = Property(name="alamat", type=StringType)
supplier_no_telp_supp: Property = Property(name="no_telp_supp", type=StringType)
supplier_attribute: Property = Property(name="attribute", type=StringType)
supplier.attributes={supplier_id_supplier, supplier_nama_supplier, supplier_alamat, supplier_no_telp_supp, supplier_attribute}

# transaksi class attributes and methods
transaksi_id_transaksi: Property = Property(name="id_transaksi", type=IntegerType)
transaksi_nama_barang: Property = Property(name="nama_barang", type=barang)
transaksi_total: Property = Property(name="total", type=IntegerType)
transaksi_tanggal: Property = Property(name="tanggal", type=StringType)
transaksi.attributes={transaksi_total, transaksi_nama_barang, transaksi_id_transaksi, transaksi_tanggal}

# sistem class attributes and methods
sistem_user: Property = Property(name="user", type=StringType)
sistem_barang: Property = Property(name="barang", type=barang)
sistem_supplier: Property = Property(name="supplier", type=supplier)
sistem.attributes={sistem_user, sistem_supplier, sistem_barang}

# masuk class attributes and methods
masuk_penyuplai: Property = Property(name="penyuplai", type=supplier)
masuk.attributes={masuk_penyuplai}

# keluar class attributes and methods
keluar_pembeli: Property = Property(name="pembeli", type=pelanggan)
keluar.attributes={keluar_pembeli}

# Relationships
user_sistem: BinaryAssociation = BinaryAssociation(
    name="user_sistem",
    ends={
        Property(name="sistem0", type=sistem, multiplicity=Multiplicity(0, 1)),
        Property(name="user1", type=user, multiplicity=Multiplicity(0, 1))
    }
)
pelanggan_transaksi: BinaryAssociation = BinaryAssociation(
    name="pelanggan_transaksi",
    ends={
        Property(name="transaksi2", type=transaksi, multiplicity=Multiplicity(0, 1)),
        Property(name="pelanggan3", type=pelanggan, multiplicity=Multiplicity(0, 1))
    }
)
supplier_transaksi: BinaryAssociation = BinaryAssociation(
    name="supplier_transaksi",
    ends={
        Property(name="transaksi4", type=transaksi, multiplicity=Multiplicity(0, 1)),
        Property(name="supplier5", type=supplier, multiplicity=Multiplicity(0, 1))
    }
)
barang_sistem: BinaryAssociation = BinaryAssociation(
    name="barang_sistem",
    ends={
        Property(name="sistem6", type=sistem, multiplicity=Multiplicity(0, 1)),
        Property(name="barang27", type=barang, multiplicity=Multiplicity(0, 1))
    }
)
supplier_sistem: BinaryAssociation = BinaryAssociation(
    name="supplier_sistem",
    ends={
        Property(name="sistem8", type=sistem, multiplicity=Multiplicity(0, 1)),
        Property(name="supplier29", type=supplier, multiplicity=Multiplicity(0, 1))
    }
)
sistem_transaksi: BinaryAssociation = BinaryAssociation(
    name="sistem_transaksi",
    ends={
        Property(name="transaksi10", type=transaksi, multiplicity=Multiplicity(0, 1)),
        Property(name="sistem11", type=sistem, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="e121749e_83e4_4a3e_ad4c_58eddc6f7d39",
    types={barang, user, pelanggan, supplier, transaksi, sistem, masuk, keluar},
    associations={user_sistem, pelanggan_transaksi, supplier_transaksi, barang_sistem, supplier_sistem, sistem_transaksi},
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