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
TypeD_A = Class(name="TypeD::A")
TypeD_B = Class(name="TypeD::B")
TypeD_C = Class(name="TypeD::C")
TypeD_AElementName = Class(name="TypeD::AElementName")
TypeD_BElementName = Class(name="TypeD::BElementName")

# TypeD_A class attributes and methods
TypeD_A_name: Property = Property(name="name", type=StringType)
TypeD_A.attributes={TypeD_A_name}

# TypeD_B class attributes and methods
TypeD_B_name: Property = Property(name="name", type=StringType)
TypeD_B.attributes={TypeD_B_name}

# TypeD_C class attributes and methods
TypeD_C_name: Property = Property(name="name", type=StringType)
TypeD_C.attributes={TypeD_C_name}

# TypeD_AElementName class attributes and methods
TypeD_AElementName_name: Property = Property(name="name", type=StringType)
TypeD_AElementName.attributes={TypeD_AElementName_name}

# TypeD_BElementName class attributes and methods
TypeD_BElementName_name: Property = Property(name="name", type=StringType)
TypeD_BElementName.attributes={TypeD_BElementName_name}

# Relationships
elms0: BinaryAssociation = BinaryAssociation(
    name="elms0",
    ends={
        Property(name="TypeD_B", type=TypeD_A, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeD_A", type=TypeD_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elms1: BinaryAssociation = BinaryAssociation(
    name="elms1",
    ends={
        Property(name="TypeD_A3", type=TypeD_B, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeD_B2", type=TypeD_A, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TypeD",
    types={TypeD_A, TypeD_B, TypeD_C, TypeD_AElementName, TypeD_BElementName},
    associations={elms0, elms1},
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