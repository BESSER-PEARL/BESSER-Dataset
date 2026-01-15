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
fsm_State = Class(name="fsm::State")

# fsm_State class attributes and methods
fsm_State_d: Property = Property(name="d", type=FloatType)
fsm_State_f: Property = Property(name="f", type=FloatType)
fsm_State_foo: Property = Property(name="foo", type=StringType)
fsm_State_i: Property = Property(name="i", type=IntegerType)
fsm_State_b: Property = Property(name="b", type=BooleanType)
fsm_State_c: Property = Property(name="c", type=StringType)
fsm_State_l: Property = Property(name="l", type=StringType)
fsm_State.attributes={fsm_State_b, fsm_State_c, fsm_State_l, fsm_State_foo, fsm_State_i, fsm_State_d, fsm_State_f}

# Domain Model
domain_model = DomainModel(
    name="fsm",
    types={fsm_State},
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