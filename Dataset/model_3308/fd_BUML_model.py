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
fd_FiniteDifference = Class(name="fd::FiniteDifference")
Solver = Class(name="Solver")

# fd_FiniteDifference class attributes and methods

# Solver class attributes and methods

# Generalizations
gen_fd_FiniteDifference_Solver = Generalization(general=Solver, specific=fd_FiniteDifference)

# Domain Model
domain_model = DomainModel(
    name="fd",
    types={fd_FiniteDifference, Solver},
    associations={},
    generalizations={gen_fd_FiniteDifference_Solver},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)