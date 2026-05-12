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
Mahasiswa = Class(name="Mahasiswa")
Nilai = Class(name="Nilai")
Dosen_Actor = Class(name="Dosen_Actor")
Aplikasi_Input_Nilai_Matakuliah_Component = Class(name="Aplikasi_Input_Nilai_Matakuliah_Component")
DAO_Mahasiswa = Class(name="DAO_Mahasiswa")
DAO_Nilai = Class(name="DAO_Nilai")
view_control_Mahasiswa = Class(name="view_control_Mahasiswa")
view_control_Nilai = Class(name="view_control_Nilai")
Activity_Data_Mahasiswa = Class(name="Activity_Data_Mahasiswa")
Activity_Data_Nilai = Class(name="Activity_Data_Nilai")
Activity_Input_Mahasiswa = Class(name="Activity_Input_Mahasiswa")
Melihat_Data_Mahasiswa_external = Class(name="Melihat_Data_Mahasiswa_external")
Melihat_Data_Nilai_external = Class(name="Melihat_Data_Nilai_external")
Menambah_Data_Mahasiswa_external = Class(name="Menambah_Data_Mahasiswa_external")
Menambah_Data_Nilai_external = Class(name="Menambah_Data_Nilai_external")
Mengubah_Data_Mahasiswa_external = Class(name="Mengubah_Data_Mahasiswa_external")
Mengubah_Data_Nilai_external = Class(name="Mengubah_Data_Nilai_external")
Menghapus_Mahasiswa_external = Class(name="Menghapus_Mahasiswa_external")
Menghapus_Nilai_external = Class(name="Menghapus_Nilai_external")

# Mahasiswa class attributes and methods
Mahasiswa_nim: Property = Property(name="nim", type=StringType)
Mahasiswa_nama: Property = Property(name="nama", type=StringType)
Mahasiswa_tahun: Property = Property(name="tahun", type=StringType)
Mahasiswa.attributes={Mahasiswa_nim, Mahasiswa_tahun, Mahasiswa_nama}

# Nilai class attributes and methods
Nilai_uts: Property = Property(name="uts", type=IntegerType)
Nilai_uas: Property = Property(name="uas", type=IntegerType)
Nilai_tugas: Property = Property(name="tugas", type=IntegerType)
Nilai_namaMK: Property = Property(name="namaMK", type=StringType)
Nilai.attributes={Nilai_uts, Nilai_uas, Nilai_tugas, Nilai_namaMK}

# Dosen_Actor class attributes and methods

# Aplikasi_Input_Nilai_Matakuliah_Component class attributes and methods

# DAO_Mahasiswa class attributes and methods
DAO_Mahasiswa_nim: Property = Property(name="nim", type=StringType)
DAO_Mahasiswa_nama: Property = Property(name="nama", type=StringType)
DAO_Mahasiswa_tahun: Property = Property(name="tahun", type=StringType)
DAO_Mahasiswa.attributes={DAO_Mahasiswa_nama, DAO_Mahasiswa_tahun, DAO_Mahasiswa_nim}

# DAO_Nilai class attributes and methods
DAO_Nilai_uts: Property = Property(name="uts", type=StringType)
DAO_Nilai_uas: Property = Property(name="uas", type=StringType)
DAO_Nilai_tugas: Property = Property(name="tugas", type=StringType)
DAO_Nilai_namaMk: Property = Property(name="namaMk", type=StringType)
DAO_Nilai.attributes={DAO_Nilai_tugas, DAO_Nilai_namaMk, DAO_Nilai_uas, DAO_Nilai_uts}

# view_control_Mahasiswa class attributes and methods

# view_control_Nilai class attributes and methods

# Activity_Data_Mahasiswa class attributes and methods

# Activity_Data_Nilai class attributes and methods

# Activity_Input_Mahasiswa class attributes and methods

# Melihat_Data_Mahasiswa_external class attributes and methods

# Melihat_Data_Nilai_external class attributes and methods

# Menambah_Data_Mahasiswa_external class attributes and methods

# Menambah_Data_Nilai_external class attributes and methods

# Mengubah_Data_Mahasiswa_external class attributes and methods

# Mengubah_Data_Nilai_external class attributes and methods

# Menghapus_Mahasiswa_external class attributes and methods

# Menghapus_Nilai_external class attributes and methods

# Relationships
Dosen_Menambah_Data_Nilai: BinaryAssociation = BinaryAssociation(
    name="Dosen_Menambah_Data_Nilai",
    ends={
        Property(name="menambah_Data_Nilai8", type=Menambah_Data_Nilai_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dosen9", type=Dosen_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mahasiswa_Nilai: BinaryAssociation = BinaryAssociation(
    name="Mahasiswa_Nilai",
    ends={
        Property(name="nilai0", type=Nilai, multiplicity=Multiplicity(0, 1)),
        Property(name="mahasiswa1", type=Mahasiswa, multiplicity=Multiplicity(0, 1))
    }
)
Dosen_Melihat_Data_Mahasiswa: BinaryAssociation = BinaryAssociation(
    name="Dosen_Melihat_Data_Mahasiswa",
    ends={
        Property(name="melihat_Data_Mahasiswa2", type=Melihat_Data_Mahasiswa_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dosen3", type=Dosen_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dosen_Melihat_Data_Nilai: BinaryAssociation = BinaryAssociation(
    name="Dosen_Melihat_Data_Nilai",
    ends={
        Property(name="melihat_Data_Nilai4", type=Melihat_Data_Nilai_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dosen5", type=Dosen_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dosen_Menambah_Data_Mahasiswa: BinaryAssociation = BinaryAssociation(
    name="Dosen_Menambah_Data_Mahasiswa",
    ends={
        Property(name="menambah_Data_Mahasiswa6", type=Menambah_Data_Mahasiswa_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dosen7", type=Dosen_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dosen_Mengubah_Data_Mahasiswa: BinaryAssociation = BinaryAssociation(
    name="Dosen_Mengubah_Data_Mahasiswa",
    ends={
        Property(name="mengubah_Data_Mahasiswa10", type=Mengubah_Data_Mahasiswa_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dosen11", type=Dosen_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dosen_Mengubah_Data_Nilai: BinaryAssociation = BinaryAssociation(
    name="Dosen_Mengubah_Data_Nilai",
    ends={
        Property(name="mengubah_Data_Nilai12", type=Mengubah_Data_Nilai_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dosen13", type=Dosen_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dosen_Menghapus_Mahasiswa: BinaryAssociation = BinaryAssociation(
    name="Dosen_Menghapus_Mahasiswa",
    ends={
        Property(name="menghapus_Mahasiswa14", type=Menghapus_Mahasiswa_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dosen15", type=Dosen_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Dosen_Menghapus_Nilai: BinaryAssociation = BinaryAssociation(
    name="Dosen_Menghapus_Nilai",
    ends={
        Property(name="menghapus_Nilai16", type=Menghapus_Nilai_external, multiplicity=Multiplicity(0, 1)),
        Property(name="dosen17", type=Dosen_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Mahasiswa_Mahasiswa: BinaryAssociation = BinaryAssociation(
    name="Mahasiswa_Mahasiswa",
    ends={
        Property(name="mahasiswa18", type=view_control_Mahasiswa, multiplicity=Multiplicity(0, 1)),
        Property(name="mahasiswa19", type=DAO_Mahasiswa, multiplicity=Multiplicity(0, 1))
    }
)
Nilai_Nilai: BinaryAssociation = BinaryAssociation(
    name="Nilai_Nilai",
    ends={
        Property(name="nilai20", type=view_control_Nilai, multiplicity=Multiplicity(0, 1)),
        Property(name="nilai21", type=DAO_Nilai, multiplicity=Multiplicity(0, 1))
    }
)
Mahasiswa_Mahasiswa1: BinaryAssociation = BinaryAssociation(
    name="Mahasiswa_Mahasiswa1",
    ends={
        Property(name="mahasiswa22", type=DAO_Mahasiswa, multiplicity=Multiplicity(0, 1)),
        Property(name="mahasiswa23", type=Mahasiswa, multiplicity=Multiplicity(0, 1))
    }
)
Nilai_Nilai1: BinaryAssociation = BinaryAssociation(
    name="Nilai_Nilai1",
    ends={
        Property(name="nilai24", type=DAO_Nilai, multiplicity=Multiplicity(0, 1)),
        Property(name="nilai25", type=Nilai, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_lN40MCWBEemcRoPW7FVMlA",
    types={Mahasiswa, Nilai, Dosen_Actor, Aplikasi_Input_Nilai_Matakuliah_Component, DAO_Mahasiswa, DAO_Nilai, view_control_Mahasiswa, view_control_Nilai, Activity_Data_Mahasiswa, Activity_Data_Nilai, Activity_Input_Mahasiswa, Melihat_Data_Mahasiswa_external, Melihat_Data_Nilai_external, Menambah_Data_Mahasiswa_external, Menambah_Data_Nilai_external, Mengubah_Data_Mahasiswa_external, Mengubah_Data_Nilai_external, Menghapus_Mahasiswa_external, Menghapus_Nilai_external},
    associations={Dosen_Menambah_Data_Nilai, Mahasiswa_Nilai, Dosen_Melihat_Data_Mahasiswa, Dosen_Melihat_Data_Nilai, Dosen_Menambah_Data_Mahasiswa, Dosen_Mengubah_Data_Mahasiswa, Dosen_Mengubah_Data_Nilai, Dosen_Menghapus_Mahasiswa, Dosen_Menghapus_Nilai, Mahasiswa_Mahasiswa, Nilai_Nilai, Mahasiswa_Mahasiswa1, Nilai_Nilai1},
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