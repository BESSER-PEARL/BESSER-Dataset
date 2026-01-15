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
m_ToplevelClass = Class(name="m::ToplevelClass")
m_pa_A = Class(name="m::pa::A")
m_pa_B = Class(name="m::pa::B")
m_pa_C = Class(name="m::pa::C")

# m_ToplevelClass class attributes and methods

# m_pa_A class attributes and methods

# m_pa_B class attributes and methods

# m_pa_C class attributes and methods

# Domain Model
domain_model = DomainModel(
    name="m",
    types={m_ToplevelClass, m_pa_A, m_pa_B, m_pa_C},
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