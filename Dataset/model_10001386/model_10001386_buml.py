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
Laporan_work_order_UseCase = Class(name="Laporan_work_order_UseCase")
Admin_Gudang_Actor = Class(name="Admin_Gudang_Actor")
Input_data_barang_masuk_UseCase = Class(name="Input_data_barang_masuk_UseCase")
Input_data_barang_keluar_UseCase = Class(name="Input_data_barang_keluar_UseCase")
Input_data_supplier_UseCase = Class(name="Input_data_supplier_UseCase")
Input_data_pembeli_UseCase = Class(name="Input_data_pembeli_UseCase")
Input_data_sortir_UseCase = Class(name="Input_data_sortir_UseCase")
Cek_ketersediaan_barang_UseCase = Class(name="Cek_ketersediaan_barang_UseCase")
Work_order_UseCase = Class(name="Work_order_UseCase")
Direktur_pemasaran_Actor = Class(name="Direktur_pemasaran_Actor")
Barang = Class(name="Barang")
Direktur_utama_Actor = Class(name="Direktur_utama_Actor")
Laporan_ready_stock_UseCase = Class(name="Laporan_ready_stock_UseCase")
Laporan_data_supplier_UseCase = Class(name="Laporan_data_supplier_UseCase")
Laporan_data_Pembelian_UseCase = Class(name="Laporan_data_Pembelian_UseCase")
Laporan_data_barang_masuk_UseCase = Class(name="Laporan_data_barang_masuk_UseCase")
Laporan_data_barang_keluar_UseCase = Class(name="Laporan_data_barang_keluar_UseCase")
Laporan_data_sortir_UseCase = Class(name="Laporan_data_sortir_UseCase")

# Laporan_work_order_UseCase class attributes and methods

# Admin_Gudang_Actor class attributes and methods

# Input_data_barang_masuk_UseCase class attributes and methods

# Input_data_barang_keluar_UseCase class attributes and methods

# Input_data_supplier_UseCase class attributes and methods

# Input_data_pembeli_UseCase class attributes and methods

# Input_data_sortir_UseCase class attributes and methods

# Cek_ketersediaan_barang_UseCase class attributes and methods

# Work_order_UseCase class attributes and methods

# Direktur_pemasaran_Actor class attributes and methods

# Barang class attributes and methods
Barang_attribute: Property = Property(name="attribute", type=StringType)
Barang_attribute2: Property = Property(name="attribute2", type=StringType)
Barang.attributes={Barang_attribute2, Barang_attribute}

# Direktur_utama_Actor class attributes and methods

# Laporan_ready_stock_UseCase class attributes and methods

# Laporan_data_supplier_UseCase class attributes and methods

# Laporan_data_Pembelian_UseCase class attributes and methods

# Laporan_data_barang_masuk_UseCase class attributes and methods

# Laporan_data_barang_keluar_UseCase class attributes and methods

# Laporan_data_sortir_UseCase class attributes and methods

# Relationships
Laporan_ready_stock_Direktur_utama: BinaryAssociation = BinaryAssociation(
    name="Laporan_ready_stock_Direktur_utama",
    ends={
        Property(name="direktur_utama0", type=Direktur_utama_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="laporan_ready_stock1", type=Laporan_ready_stock_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Laporan_data_supplier_Direktur_utama: BinaryAssociation = BinaryAssociation(
    name="Laporan_data_supplier_Direktur_utama",
    ends={
        Property(name="direktur_utama2", type=Direktur_utama_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="laporan_data_supplier3", type=Laporan_data_supplier_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Laporan_data_Pembelian_Direktur_utama: BinaryAssociation = BinaryAssociation(
    name="Laporan_data_Pembelian_Direktur_utama",
    ends={
        Property(name="direktur_utama4", type=Direktur_utama_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="laporan_data_Pembelian5", type=Laporan_data_Pembelian_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Laporan_data_barang_masuk_Direktur_utama: BinaryAssociation = BinaryAssociation(
    name="Laporan_data_barang_masuk_Direktur_utama",
    ends={
        Property(name="direktur_utama6", type=Direktur_utama_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="laporan_data_barang_masuk7", type=Laporan_data_barang_masuk_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Laporan_data_barang_keluar_Direktur_utama: BinaryAssociation = BinaryAssociation(
    name="Laporan_data_barang_keluar_Direktur_utama",
    ends={
        Property(name="direktur_utama8", type=Direktur_utama_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="laporan_data_barang_keluar9", type=Laporan_data_barang_keluar_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Laporan_data_sortir_Direktur_utama: BinaryAssociation = BinaryAssociation(
    name="Laporan_data_sortir_Direktur_utama",
    ends={
        Property(name="direktur_utama10", type=Direktur_utama_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="laporan_data_sortir11", type=Laporan_data_sortir_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Laporan_work_order_Direktur_utama: BinaryAssociation = BinaryAssociation(
    name="Laporan_work_order_Direktur_utama",
    ends={
        Property(name="direktur_utama12", type=Direktur_utama_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="laporan_work_order13", type=Laporan_work_order_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_barang_masuk_Admin_Gudang: BinaryAssociation = BinaryAssociation(
    name="Input_data_barang_masuk_Admin_Gudang",
    ends={
        Property(name="admin_Gudang14", type=Admin_Gudang_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_barang_masuk15", type=Input_data_barang_masuk_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_barang_keluar_Admin_Gudang: BinaryAssociation = BinaryAssociation(
    name="Input_data_barang_keluar_Admin_Gudang",
    ends={
        Property(name="admin_Gudang16", type=Admin_Gudang_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_barang_keluar17", type=Input_data_barang_keluar_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_supplier_Admin_Gudang: BinaryAssociation = BinaryAssociation(
    name="Input_data_supplier_Admin_Gudang",
    ends={
        Property(name="admin_Gudang18", type=Admin_Gudang_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_supplier19", type=Input_data_supplier_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_pembeli_Admin_Gudang: BinaryAssociation = BinaryAssociation(
    name="Input_data_pembeli_Admin_Gudang",
    ends={
        Property(name="admin_Gudang20", type=Admin_Gudang_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_pembeli21", type=Input_data_pembeli_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_sortir_Admin_Gudang: BinaryAssociation = BinaryAssociation(
    name="Input_data_sortir_Admin_Gudang",
    ends={
        Property(name="admin_Gudang22", type=Admin_Gudang_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_sortir23", type=Input_data_sortir_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Direktur_utama_Work_order: BinaryAssociation = BinaryAssociation(
    name="Direktur_utama_Work_order",
    ends={
        Property(name="work_order24", type=Work_order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="direktur_utama25", type=Direktur_utama_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Direktur_pemasaran_Cek_ketersediaan_barang: BinaryAssociation = BinaryAssociation(
    name="Direktur_pemasaran_Cek_ketersediaan_barang",
    ends={
        Property(name="cek_ketersediaan_barang26", type=Cek_ketersediaan_barang_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="direktur_pemasaran27", type=Direktur_pemasaran_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Gudang_Laporan_work_order: BinaryAssociation = BinaryAssociation(
    name="Admin_Gudang_Laporan_work_order",
    ends={
        Property(name="laporan_work_order28", type=Laporan_work_order_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin_Gudang29", type=Admin_Gudang_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_3oBAUE_IEeeu8_4LH_yuyg",
    types={Laporan_work_order_UseCase, Admin_Gudang_Actor, Input_data_barang_masuk_UseCase, Input_data_barang_keluar_UseCase, Input_data_supplier_UseCase, Input_data_pembeli_UseCase, Input_data_sortir_UseCase, Cek_ketersediaan_barang_UseCase, Work_order_UseCase, Direktur_pemasaran_Actor, Barang, Direktur_utama_Actor, Laporan_ready_stock_UseCase, Laporan_data_supplier_UseCase, Laporan_data_Pembelian_UseCase, Laporan_data_barang_masuk_UseCase, Laporan_data_barang_keluar_UseCase, Laporan_data_sortir_UseCase},
    associations={Laporan_ready_stock_Direktur_utama, Laporan_data_supplier_Direktur_utama, Laporan_data_Pembelian_Direktur_utama, Laporan_data_barang_masuk_Direktur_utama, Laporan_data_barang_keluar_Direktur_utama, Laporan_data_sortir_Direktur_utama, Laporan_work_order_Direktur_utama, Input_data_barang_masuk_Admin_Gudang, Input_data_barang_keluar_Admin_Gudang, Input_data_supplier_Admin_Gudang, Input_data_pembeli_Admin_Gudang, Input_data_sortir_Admin_Gudang, Direktur_utama_Work_order, Direktur_pemasaran_Cek_ketersediaan_barang, Admin_Gudang_Laporan_work_order},
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