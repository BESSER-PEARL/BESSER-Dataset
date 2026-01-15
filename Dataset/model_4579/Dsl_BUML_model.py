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
dsl_Robot = Class(name="dsl::Robot")
dsl_Device = Class(name="dsl::Device")
dsl_EJavaObject = Class(name="dsl::EJavaObject")
dsl_Capture = Class(name="dsl::Capture")
Fonctionnalite = Class(name="Fonctionnalite")
dsl_Action = Class(name="dsl::Action")
dsl_Object = Class(name="dsl::Object")
EJavaObject = Class(name="EJavaObject")
dsl_IDevice = Class(name="dsl::IDevice")
dsl_Fonctionnalite = Class(name="dsl::Fonctionnalite")
dsl_Parametre = Class(name="dsl::Parametre")

# dsl_Robot class attributes and methods
dsl_Robot_name: Property = Property(name="name", type=StringType)
dsl_Robot.attributes={dsl_Robot_name}

# dsl_Device class attributes and methods
dsl_Device_name: Property = Property(name="name", type=StringType)
dsl_Device.attributes={dsl_Device_name}

# dsl_EJavaObject class attributes and methods

# dsl_Capture class attributes and methods

# Fonctionnalite class attributes and methods

# dsl_Action class attributes and methods

# dsl_Object class attributes and methods

# EJavaObject class attributes and methods

# dsl_IDevice class attributes and methods
dsl_IDevice_typeof: Property = Property(name="typeof", type=StringType)
dsl_IDevice_name: Property = Property(name="name", type=StringType)
dsl_IDevice.attributes={dsl_IDevice_typeof, dsl_IDevice_name}

# dsl_Fonctionnalite class attributes and methods
dsl_Fonctionnalite_name: Property = Property(name="name", type=StringType)
dsl_Fonctionnalite.attributes={dsl_Fonctionnalite_name}

# dsl_Parametre class attributes and methods
dsl_Parametre_name: Property = Property(name="name", type=StringType)
dsl_Parametre.attributes={dsl_Parametre_name}

# Relationships
refFonction2: BinaryAssociation = BinaryAssociation(
    name="refFonction2",
    ends={
        Property(name="dsl_Fonctionnalite3", type=dsl_Device, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Device", type=dsl_Fonctionnalite, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type4: BinaryAssociation = BinaryAssociation(
    name="type4",
    ends={
        Property(name="dsl_EJavaObject", type=dsl_Parametre, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Parametre5", type=dsl_EJavaObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
return6: BinaryAssociation = BinaryAssociation(
    name="return6",
    ends={
        Property(name="dsl_EJavaObject7", type=dsl_Action, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Action", type=dsl_EJavaObject, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
instances0: BinaryAssociation = BinaryAssociation(
    name="instances0",
    ends={
        Property(name="dsl_IDevice", type=dsl_Robot, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Robot", type=dsl_IDevice, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ListeParametres1: BinaryAssociation = BinaryAssociation(
    name="ListeParametres1",
    ends={
        Property(name="dsl_Parametre", type=dsl_Fonctionnalite, multiplicity=Multiplicity(1, 1)),
        Property(name="dsl_Fonctionnalite", type=dsl_Parametre, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_dsl_Capture_Fonctionnalite = Generalization(general=Fonctionnalite, specific=dsl_Capture)
gen_dsl_Action_Fonctionnalite = Generalization(general=Fonctionnalite, specific=dsl_Action)
gen_dsl_Object_EJavaObject = Generalization(general=EJavaObject, specific=dsl_Object)

# Domain Model
domain_model = DomainModel(
    name="dsl",
    types={dsl_Robot, dsl_Device, dsl_EJavaObject, dsl_Capture, Fonctionnalite, dsl_Action, dsl_Object, EJavaObject, dsl_IDevice, dsl_Fonctionnalite, dsl_Parametre},
    associations={refFonction2, type4, return6, instances0, ListeParametres1},
    generalizations={gen_dsl_Capture_Fonctionnalite, gen_dsl_Action_Fonctionnalite, gen_dsl_Object_EJavaObject},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)