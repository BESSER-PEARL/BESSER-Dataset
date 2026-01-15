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
z3fsm_Region = Class(name="z3fsm::Region")
AbstractState = Class(name="AbstractState")
z3fsm_State = Class(name="z3fsm::State")
z3fsm_AbstractState = Class(name="z3fsm::AbstractState", is_abstract=True)

# z3fsm_Region class attributes and methods
z3fsm_Region_name: Property = Property(name="name", type=StringType)
z3fsm_Region.attributes={z3fsm_Region_name}

# AbstractState class attributes and methods

# z3fsm_State class attributes and methods

# z3fsm_AbstractState class attributes and methods
z3fsm_AbstractState_id: Property = Property(name="id", type=StringType)
z3fsm_AbstractState.attributes={z3fsm_AbstractState_id}

# Relationships
subElements0: BinaryAssociation = BinaryAssociation(
    name="subElements0",
    ends={
        Property(name="z3fsm_AbstractState", type=z3fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="z3fsm_Region", type=z3fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_z3fsm_Region_AbstractState = Generalization(general=AbstractState, specific=z3fsm_Region)
gen_z3fsm_State_AbstractState = Generalization(general=AbstractState, specific=z3fsm_State)

# Domain Model
domain_model = DomainModel(
    name="z3fsm",
    types={z3fsm_Region, AbstractState, z3fsm_State, z3fsm_AbstractState},
    associations={subElements0},
    generalizations={gen_z3fsm_Region_AbstractState, gen_z3fsm_State_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)