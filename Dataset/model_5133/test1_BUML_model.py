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
TestMerge_A = Class(name="TestMerge::A")
TestMerge_B = Class(name="TestMerge::B")

# TestMerge_A class attributes and methods
TestMerge_A_attr1: Property = Property(name="attr1", type=StringType)
TestMerge_A.attributes={TestMerge_A_attr1}

# TestMerge_B class attributes and methods

# Relationships
b0: BinaryAssociation = BinaryAssociation(
    name="b0",
    ends={
        Property(name="TestMerge_B", type=TestMerge_A, multiplicity=Multiplicity(1, 1)),
        Property(name="TestMerge_A", type=TestMerge_B, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="TestMerge",
    types={TestMerge_A, TestMerge_B},
    associations={b0},
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