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
Original_Metamodel_A = Class(name="Original::Metamodel::A")
Original_Metamodel_B = Class(name="Original::Metamodel::B")
Original_Metamodel_C = Class(name="Original::Metamodel::C")
Original_Metamodel_D = Class(name="Original::Metamodel::D")

# Original_Metamodel_A class attributes and methods

# Original_Metamodel_B class attributes and methods
Original_Metamodel_B_propertyB: Property = Property(name="propertyB", type=StringType)
Original_Metamodel_B.attributes={Original_Metamodel_B_propertyB}

# Original_Metamodel_C class attributes and methods
Original_Metamodel_C_propertyC: Property = Property(name="propertyC", type=StringType)
Original_Metamodel_C.attributes={Original_Metamodel_C_propertyC}

# Original_Metamodel_D class attributes and methods

# Relationships
refA0: BinaryAssociation = BinaryAssociation(
    name="refA0",
    ends={
        Property(name="Original_Metamodel_A", type=Original_Metamodel_B, multiplicity=Multiplicity(1, 1)),
        Property(name="Original_Metamodel_B", type=Original_Metamodel_A, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="Original_Metamodel",
    types={Original_Metamodel_A, Original_Metamodel_B, Original_Metamodel_C, Original_Metamodel_D},
    associations={refA0},
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