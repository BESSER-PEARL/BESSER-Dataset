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
abc_A = Class(name="abc::A")
abc_B = Class(name="abc::B")
abc_C = Class(name="abc::C")

# abc_A class attributes and methods

# abc_B class attributes and methods

# abc_C class attributes and methods

# Relationships
bes0: BinaryAssociation = BinaryAssociation(
    name="bes0",
    ends={
        Property(name="abc_B", type=abc_A, multiplicity=Multiplicity(1, 1)),
        Property(name="abc_A", type=abc_B, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ces1: BinaryAssociation = BinaryAssociation(
    name="ces1",
    ends={
        Property(name="abc_C", type=abc_B, multiplicity=Multiplicity(1, 1)),
        Property(name="abc_B2", type=abc_C, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="abc",
    types={abc_A, abc_B, abc_C},
    associations={bes0, ces1},
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