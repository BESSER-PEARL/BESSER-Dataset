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
hExamle_4_RHS_X = Class(name="hExamle::4::RHS::X")

# hExamle_4_RHS_X class attributes and methods
hExamle_4_RHS_X_att1: Property = Property(name="att1", type=StringType)
hExamle_4_RHS_X.attributes={hExamle_4_RHS_X_att1}

# Domain Model
domain_model = DomainModel(
    name="hExamle_4_RHS",
    types={hExamle_4_RHS_X},
    associations={},
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