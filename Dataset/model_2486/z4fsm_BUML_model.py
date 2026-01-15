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
z4fsm_Region = Class(name="z4fsm::Region")
z4fsm_AbstractState = Class(name="z4fsm::AbstractState", is_abstract=True)
z4fsm_State = Class(name="z4fsm::State")
AbstractState = Class(name="AbstractState")

# z4fsm_Region class attributes and methods
z4fsm_Region_name: Property = Property(name="name", type=StringType)
z4fsm_Region.attributes={z4fsm_Region_name}

# z4fsm_AbstractState class attributes and methods
z4fsm_AbstractState_id: Property = Property(name="id", type=StringType)
z4fsm_AbstractState.attributes={z4fsm_AbstractState_id}

# z4fsm_State class attributes and methods

# AbstractState class attributes and methods

# Relationships
astates0: BinaryAssociation = BinaryAssociation(
    name="astates0",
    ends={
        Property(name="z4fsm_AbstractState", type=z4fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="z4fsm_Region", type=z4fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subElements1: BinaryAssociation = BinaryAssociation(
    name="subElements1",
    ends={
        Property(name="z4fsm_State", type=z4fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="z4fsm_AbstractState2", type=z4fsm_State, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_z4fsm_State_AbstractState = Generalization(general=AbstractState, specific=z4fsm_State)

# Domain Model
domain_model = DomainModel(
    name="z4fsm",
    types={z4fsm_Region, z4fsm_AbstractState, z4fsm_State, AbstractState},
    associations={astates0, subElements1},
    generalizations={gen_z4fsm_State_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)