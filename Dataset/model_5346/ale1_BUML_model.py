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
ale1_A1 = Class(name="ale1::A1")
ale1_RA1 = Class(name="ale1::RA1", is_abstract=True)
ale1_RA2 = Class(name="ale1::RA2", is_abstract=True)

# ale1_A1 class attributes and methods

# ale1_RA1 class attributes and methods

# ale1_RA2 class attributes and methods

# Relationships
ra10: BinaryAssociation = BinaryAssociation(
    name="ra10",
    ends={
        Property(name="ale1_RA1", type=ale1_A1, multiplicity=Multiplicity(1, 1)),
        Property(name="ale1_A1", type=ale1_RA1, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ra21: BinaryAssociation = BinaryAssociation(
    name="ra21",
    ends={
        Property(name="ale1_RA2", type=ale1_A1, multiplicity=Multiplicity(1, 1)),
        Property(name="ale1_A12", type=ale1_RA2, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="ale1",
    types={ale1_A1, ale1_RA1, ale1_RA2},
    associations={ra10, ra21},
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