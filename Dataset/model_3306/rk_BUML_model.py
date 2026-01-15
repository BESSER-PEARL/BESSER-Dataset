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
rk_RungeKutta = Class(name="rk::RungeKutta")
Solver = Class(name="Solver")

# rk_RungeKutta class attributes and methods
rk_RungeKutta_relativeTolerance: Property = Property(name="relativeTolerance", type=FloatType)
rk_RungeKutta.attributes={rk_RungeKutta_relativeTolerance}

# Solver class attributes and methods

# Generalizations
gen_rk_RungeKutta_Solver = Generalization(general=Solver, specific=rk_RungeKutta)

# Domain Model
domain_model = DomainModel(
    name="rk",
    types={rk_RungeKutta, Solver},
    associations={},
    generalizations={gen_rk_RungeKutta_Solver},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)