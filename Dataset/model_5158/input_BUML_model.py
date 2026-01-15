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
astrans_A = Class(name="astrans::A")
astrans_B = Class(name="astrans::B")

# astrans_A class attributes and methods
astrans_A_ra: Property = Property(name="ra", type=StringType)
astrans_A.attributes={astrans_A_ra}

# astrans_B class attributes and methods

# Relationships
nonc0: BinaryAssociation = BinaryAssociation(
    name="nonc0",
    ends={
        Property(name="astrans_B", type=astrans_A, multiplicity=Multiplicity(1, 1)),
        Property(name="astrans_A", type=astrans_B, multiplicity=Multiplicity(0, 1))
    }
)
c1: BinaryAssociation = BinaryAssociation(
    name="c1",
    ends={
        Property(name="astrans_B3", type=astrans_A, multiplicity=Multiplicity(1, 1)),
        Property(name="astrans_A2", type=astrans_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rr5: BinaryAssociation = BinaryAssociation(
    name="rr5",
    ends={
        Property(name="astrans_A6", type=astrans_A, multiplicity=Multiplicity(1, 1)),
        Property(name="astrans_A4", type=astrans_A, multiplicity=Multiplicity(0, 1))
    }
)
b8: BinaryAssociation = BinaryAssociation(
    name="b8",
    ends={
        Property(name="astrans_B9", type=astrans_B, multiplicity=Multiplicity(1, 1)),
        Property(name="astrans_B7", type=astrans_B, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="astrans",
    types={astrans_A, astrans_B},
    associations={nonc0, c1, rr5, b8},
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