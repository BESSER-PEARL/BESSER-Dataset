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
main_M = Class(name="main::M")
subsub_SSC = Class(name="subsub::SSC")
main_subsub_SSC = Class(name="main::subsub::SSC")

# main_M class attributes and methods

# subsub_SSC class attributes and methods

# main_subsub_SSC class attributes and methods

# Relationships
p0: BinaryAssociation = BinaryAssociation(
    name="p0",
    ends={
        Property(name="subsub_SSC", type=main_M, multiplicity=Multiplicity(1, 1)),
        Property(name="main_M", type=subsub_SSC, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="main",
    types={main_M, subsub_SSC, main_subsub_SSC},
    associations={p0},
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