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
Admin_Actor = Class(name="Admin_Actor")
Input_data_pengemudi_UseCase = Class(name="Input_data_pengemudi_UseCase")
Input_data_kendaraan_UseCase = Class(name="Input_data_kendaraan_UseCase")
Input_data_mekanik_UseCase = Class(name="Input_data_mekanik_UseCase")
Input_data_service_UseCase = Class(name="Input_data_service_UseCase")
laporan_service_UseCase = Class(name="laporan_service_UseCase")
Mekanik_UseCase = Class(name="Mekanik_UseCase")
Cetak_SPK_UseCase = Class(name="Cetak_SPK_UseCase")
Input_data_kerusakan_UseCase = Class(name="Input_data_kerusakan_UseCase")
Login_admin_UseCase = Class(name="Login_admin_UseCase")
Class_ = Class(name="Class")

# Admin_Actor class attributes and methods

# Input_data_pengemudi_UseCase class attributes and methods

# Input_data_kendaraan_UseCase class attributes and methods

# Input_data_mekanik_UseCase class attributes and methods

# Input_data_service_UseCase class attributes and methods

# laporan_service_UseCase class attributes and methods

# Mekanik_UseCase class attributes and methods

# Cetak_SPK_UseCase class attributes and methods

# Input_data_kerusakan_UseCase class attributes and methods

# Login_admin_UseCase class attributes and methods

# Class class attributes and methods

# Relationships
Admin_Input_data_pengemudi: BinaryAssociation = BinaryAssociation(
    name="Admin_Input_data_pengemudi",
    ends={
        Property(name="input_data_pengemudi0", type=Input_data_pengemudi_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin1", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Input_data_pengemudi2: BinaryAssociation = BinaryAssociation(
    name="Admin_Input_data_pengemudi2",
    ends={
        Property(name="input_data_pengemudi22", type=Input_data_kendaraan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin3", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Input_data_pengemudi22: BinaryAssociation = BinaryAssociation(
    name="Admin_Input_data_pengemudi22",
    ends={
        Property(name="input_data_pengemudi224", type=Input_data_mekanik_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin5", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Input_data_pengemudi27: BinaryAssociation = BinaryAssociation(
    name="Admin_Input_data_pengemudi27",
    ends={
        Property(name="input_data_pengemudi276", type=Input_data_kerusakan_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin7", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Input_data_pengemudi23: BinaryAssociation = BinaryAssociation(
    name="Admin_Input_data_pengemudi23",
    ends={
        Property(name="input_data_pengemudi238", type=Input_data_service_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="admin9", type=Admin_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_pengemudi27_Input_data_pengemudi26: BinaryAssociation = BinaryAssociation(
    name="Input_data_pengemudi27_Input_data_pengemudi26",
    ends={
        Property(name="input_data_pengemudi2610", type=Cetak_SPK_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_pengemudi2711", type=Input_data_kerusakan_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_pengemudi26_Input_data_pengemudi25: BinaryAssociation = BinaryAssociation(
    name="Input_data_pengemudi26_Input_data_pengemudi25",
    ends={
        Property(name="input_data_pengemudi2512", type=Mekanik_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_pengemudi2613", type=Cetak_SPK_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_pengemudi23_Input_data_pengemudi24: BinaryAssociation = BinaryAssociation(
    name="Input_data_pengemudi23_Input_data_pengemudi24",
    ends={
        Property(name="input_data_pengemudi2414", type=laporan_service_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_pengemudi2315", type=Input_data_service_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_service_Login_admin: BinaryAssociation = BinaryAssociation(
    name="Input_data_service_Login_admin",
    ends={
        Property(name="login_admin16", type=Login_admin_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_service17", type=Input_data_service_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_kerusakan_Login_admin: BinaryAssociation = BinaryAssociation(
    name="Input_data_kerusakan_Login_admin",
    ends={
        Property(name="login_admin18", type=Login_admin_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_kerusakan19", type=Input_data_kerusakan_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_mekanik_Login_admin: BinaryAssociation = BinaryAssociation(
    name="Input_data_mekanik_Login_admin",
    ends={
        Property(name="login_admin20", type=Login_admin_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_mekanik21", type=Input_data_mekanik_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_kendaraan_Login_admin: BinaryAssociation = BinaryAssociation(
    name="Input_data_kendaraan_Login_admin",
    ends={
        Property(name="login_admin22", type=Login_admin_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_kendaraan23", type=Input_data_kendaraan_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Input_data_pengemudi_Login_admin: BinaryAssociation = BinaryAssociation(
    name="Input_data_pengemudi_Login_admin",
    ends={
        Property(name="login_admin24", type=Login_admin_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="input_data_pengemudi25", type=Input_data_pengemudi_UseCase, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_cNWfoC1gEeqqcaoAsxFIeg",
    types={Admin_Actor, Input_data_pengemudi_UseCase, Input_data_kendaraan_UseCase, Input_data_mekanik_UseCase, Input_data_service_UseCase, laporan_service_UseCase, Mekanik_UseCase, Cetak_SPK_UseCase, Input_data_kerusakan_UseCase, Login_admin_UseCase, Class_},
    associations={Admin_Input_data_pengemudi, Admin_Input_data_pengemudi2, Admin_Input_data_pengemudi22, Admin_Input_data_pengemudi27, Admin_Input_data_pengemudi23, Input_data_pengemudi27_Input_data_pengemudi26, Input_data_pengemudi26_Input_data_pengemudi25, Input_data_pengemudi23_Input_data_pengemudi24, Input_data_service_Login_admin, Input_data_kerusakan_Login_admin, Input_data_mekanik_Login_admin, Input_data_kendaraan_Login_admin, Input_data_pengemudi_Login_admin},
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