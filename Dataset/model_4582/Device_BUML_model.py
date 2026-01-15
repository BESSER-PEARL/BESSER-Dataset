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
device_Types = Class(name="device::Types")
device_Device = Class(name="device::Device")
device_Fonctionnalite = Class(name="device::Fonctionnalite")
device_Parametre = Class(name="device::Parametre")
device_EJavaObject = Class(name="device::EJavaObject")
device_Capture = Class(name="device::Capture")
Fonctionnalite = Class(name="Fonctionnalite")
device_Action = Class(name="device::Action")
device_Object = Class(name="device::Object")
EJavaObject = Class(name="EJavaObject")

# device_Types class attributes and methods

# device_Device class attributes and methods
device_Device_name: Property = Property(name="name", type=StringType)
device_Device.attributes={device_Device_name}

# device_Fonctionnalite class attributes and methods
device_Fonctionnalite_name: Property = Property(name="name", type=StringType)
device_Fonctionnalite.attributes={device_Fonctionnalite_name}

# device_Parametre class attributes and methods
device_Parametre_name: Property = Property(name="name", type=StringType)
device_Parametre.attributes={device_Parametre_name}

# device_EJavaObject class attributes and methods

# device_Capture class attributes and methods

# Fonctionnalite class attributes and methods

# device_Action class attributes and methods

# device_Object class attributes and methods

# EJavaObject class attributes and methods

# Relationships
Types0: BinaryAssociation = BinaryAssociation(
    name="Types0",
    ends={
        Property(name="device_Device", type=device_Types, multiplicity=Multiplicity(1, 1)),
        Property(name="device_Types", type=device_Device, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refFonction1: BinaryAssociation = BinaryAssociation(
    name="refFonction1",
    ends={
        Property(name="device_Fonctionnalite", type=device_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="device_Device2", type=device_Fonctionnalite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ListeParametres3: BinaryAssociation = BinaryAssociation(
    name="ListeParametres3",
    ends={
        Property(name="device_Parametre", type=device_Fonctionnalite, multiplicity=Multiplicity(1, 1)),
        Property(name="device_Fonctionnalite4", type=device_Parametre, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type5: BinaryAssociation = BinaryAssociation(
    name="type5",
    ends={
        Property(name="device_EJavaObject", type=device_Parametre, multiplicity=Multiplicity(1, 1)),
        Property(name="device_Parametre6", type=device_EJavaObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
return7: BinaryAssociation = BinaryAssociation(
    name="return7",
    ends={
        Property(name="device_EJavaObject8", type=device_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="device_Action", type=device_EJavaObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_device_Capture_Fonctionnalite = Generalization(general=Fonctionnalite, specific=device_Capture)
gen_device_Action_Fonctionnalite = Generalization(general=Fonctionnalite, specific=device_Action)
gen_device_Object_EJavaObject = Generalization(general=EJavaObject, specific=device_Object)

# Domain Model
domain_model = DomainModel(
    name="device",
    types={device_Types, device_Device, device_Fonctionnalite, device_Parametre, device_EJavaObject, device_Capture, Fonctionnalite, device_Action, device_Object, EJavaObject},
    associations={Types0, refFonction1, ListeParametres3, type5, return7},
    generalizations={gen_device_Capture_Fonctionnalite, gen_device_Action_Fonctionnalite, gen_device_Object_EJavaObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)