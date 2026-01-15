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
z7fsm_Region = Class(name="z7fsm::Region")
AbstractState = Class(name="AbstractState")
z7fsm_AbstractState = Class(name="z7fsm::AbstractState", is_abstract=True)
z7fsm_State = Class(name="z7fsm::State")

# z7fsm_Region class attributes and methods
z7fsm_Region_name: Property = Property(name="name", type=StringType)
z7fsm_Region.attributes={z7fsm_Region_name}

# AbstractState class attributes and methods

# z7fsm_AbstractState class attributes and methods
z7fsm_AbstractState_id: Property = Property(name="id", type=StringType)
z7fsm_AbstractState.attributes={z7fsm_AbstractState_id}

# z7fsm_State class attributes and methods

# Relationships
astates0: BinaryAssociation = BinaryAssociation(
    name="astates0",
    ends={
        Property(name="z7fsm_Region", type=z7fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="z7fsm_AbstractState", type=z7fsm_Region, multiplicity=Multiplicity(1, 1))
    }
)
subElements2: BinaryAssociation = BinaryAssociation(
    name="subElements2",
    ends={
        Property(name="z7fsm_AbstractState3", type=z7fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="z7fsm_AbstractState1", type=z7fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_z7fsm_Region_AbstractState = Generalization(general=AbstractState, specific=z7fsm_Region)
gen_z7fsm_State_AbstractState = Generalization(general=AbstractState, specific=z7fsm_State)

# Domain Model
domain_model = DomainModel(
    name="z7fsm",
    types={z7fsm_Region, AbstractState, z7fsm_AbstractState, z7fsm_State},
    associations={astates0, subElements2},
    generalizations={gen_z7fsm_Region_AbstractState, gen_z7fsm_State_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)