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
TypeA_A = Class(name="TypeA::A")
TypeA_B = Class(name="TypeA::B")
TypeA_C = Class(name="TypeA::C")

# TypeA_A class attributes and methods
TypeA_A_name: Property = Property(name="name", type=StringType)
TypeA_A.attributes={TypeA_A_name}

# TypeA_B class attributes and methods
TypeA_B_name: Property = Property(name="name", type=StringType)
TypeA_B_description1: Property = Property(name="description1", type=StringType)
TypeA_B_description2: Property = Property(name="description2", type=StringType)
TypeA_B_description3: Property = Property(name="description3", type=StringType)
TypeA_B.attributes={TypeA_B_description1, TypeA_B_description2, TypeA_B_name, TypeA_B_description3}

# TypeA_C class attributes and methods
TypeA_C_description2: Property = Property(name="description2", type=StringType)
TypeA_C_name: Property = Property(name="name", type=StringType)
TypeA_C_description1: Property = Property(name="description1", type=StringType)
TypeA_C.attributes={TypeA_C_name, TypeA_C_description1, TypeA_C_description2}

# Relationships
bElements0: BinaryAssociation = BinaryAssociation(
    name="bElements0",
    ends={
        Property(name="TypeA_B", type=TypeA_A, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_A", type=TypeA_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cElements1: BinaryAssociation = BinaryAssociation(
    name="cElements1",
    ends={
        Property(name="TypeA_C", type=TypeA_A, multiplicity=Multiplicity(1, 1)),
        Property(name="TypeA_A2", type=TypeA_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TypeA",
    types={TypeA_A, TypeA_B, TypeA_C},
    associations={bElements0, cElements1},
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