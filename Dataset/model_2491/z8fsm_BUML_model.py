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
z8fsm_State = Class(name="z8fsm_State")
z8fsm_Region = Class(name="z8fsm_Region")
AbstractState = Class(name="AbstractState")
z8fsm_AbstractState = Class(name="z8fsm_AbstractState", is_abstract=True)

# z8fsm_State class attributes and methods

# z8fsm_Region class attributes and methods
z8fsm_Region_name: Property = Property(name="name", type=StringType)
z8fsm_Region.attributes={z8fsm_Region_name}

# AbstractState class attributes and methods

# z8fsm_AbstractState class attributes and methods
z8fsm_AbstractState_id: Property = Property(name="id", type=StringType)
z8fsm_AbstractState.attributes={z8fsm_AbstractState_id}

# Relationships
subElements2: BinaryAssociation = BinaryAssociation(
    name="subElements2",
    ends={
        Property(name="z8fsm_AbstractState3", type=z8fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="z8fsm_AbstractState1", type=z8fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
astates0: BinaryAssociation = BinaryAssociation(
    name="astates0",
    ends={
        Property(name="z8fsm_AbstractState", type=z8fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="z8fsm_Region", type=z8fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_z8fsm_State_AbstractState = Generalization(general=AbstractState, specific=z8fsm_State)
gen_z8fsm_Region_AbstractState = Generalization(general=AbstractState, specific=z8fsm_Region)

# Domain Model
domain_model = DomainModel(
    name="z8fsm",
    types={z8fsm_State, z8fsm_Region, AbstractState, z8fsm_AbstractState},
    associations={subElements2, astates0},
    generalizations={gen_z8fsm_State_AbstractState, gen_z8fsm_Region_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)