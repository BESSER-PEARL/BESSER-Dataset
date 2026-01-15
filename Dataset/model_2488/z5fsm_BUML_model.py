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
z5fsm_Region = Class(name="z5fsm::Region")
z5fsm_AbstractState = Class(name="z5fsm::AbstractState", is_abstract=True)
z5fsm_State = Class(name="z5fsm::State")
AbstractState = Class(name="AbstractState")

# z5fsm_Region class attributes and methods
z5fsm_Region_name: Property = Property(name="name", type=StringType)
z5fsm_Region.attributes={z5fsm_Region_name}

# z5fsm_AbstractState class attributes and methods
z5fsm_AbstractState_id: Property = Property(name="id", type=StringType)
z5fsm_AbstractState.attributes={z5fsm_AbstractState_id}

# z5fsm_State class attributes and methods

# AbstractState class attributes and methods

# Relationships
astates0: BinaryAssociation = BinaryAssociation(
    name="astates0",
    ends={
        Property(name="z5fsm_AbstractState", type=z5fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="z5fsm_Region", type=z5fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subElements2: BinaryAssociation = BinaryAssociation(
    name="subElements2",
    ends={
        Property(name="z5fsm_AbstractState3", type=z5fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="z5fsm_AbstractState1", type=z5fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_z5fsm_State_AbstractState = Generalization(general=AbstractState, specific=z5fsm_State)

# Domain Model
domain_model = DomainModel(
    name="z5fsm",
    types={z5fsm_Region, z5fsm_AbstractState, z5fsm_State, AbstractState},
    associations={astates0, subElements2},
    generalizations={gen_z5fsm_State_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)