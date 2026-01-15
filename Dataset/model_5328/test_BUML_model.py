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
Root_NewEClass1 = Class(name="Root::NewEClass1")
Root_NewEClass2 = Class(name="Root::NewEClass2")
Root_NewEClass3 = Class(name="Root::NewEClass3")

# Root_NewEClass1 class attributes and methods

# Root_NewEClass2 class attributes and methods

# Root_NewEClass3 class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="Root",
    types={Root_NewEClass1, Root_NewEClass2, Root_NewEClass3},
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