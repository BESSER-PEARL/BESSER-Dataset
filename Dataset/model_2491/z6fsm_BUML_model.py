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
z6fsm_Region = Class(name="z6fsm::Region")
z6fsm_AbstractState = Class(name="z6fsm::AbstractState", is_abstract=True)
z6fsm_State = Class(name="z6fsm::State")
AbstractState = Class(name="AbstractState")
z6fsm_Foo = Class(name="z6fsm::Foo")

# z6fsm_Region class attributes and methods
z6fsm_Region_name: Property = Property(name="name", type=StringType)
z6fsm_Region.attributes={z6fsm_Region_name}

# z6fsm_AbstractState class attributes and methods
z6fsm_AbstractState_id: Property = Property(name="id", type=StringType)
z6fsm_AbstractState.attributes={z6fsm_AbstractState_id}

# z6fsm_State class attributes and methods

# AbstractState class attributes and methods

# z6fsm_Foo class attributes and methods

# Relationships
astates0: BinaryAssociation = BinaryAssociation(
    name="astates0",
    ends={
        Property(name="z6fsm_AbstractState", type=z6fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="z6fsm_Region", type=z6fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subElements2: BinaryAssociation = BinaryAssociation(
    name="subElements2",
    ends={
        Property(name="z6fsm_AbstractState3", type=z6fsm_AbstractState, multiplicity=Multiplicity(1, 1)),
        Property(name="z6fsm_AbstractState1", type=z6fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_z6fsm_State_AbstractState = Generalization(general=AbstractState, specific=z6fsm_State)
gen_z6fsm_Foo_AbstractState = Generalization(general=AbstractState, specific=z6fsm_Foo)

# Domain Model
domain_model = DomainModel(
    name="z6fsm",
    types={z6fsm_Region, z6fsm_AbstractState, z6fsm_State, AbstractState, z6fsm_Foo},
    associations={astates0, subElements2},
    generalizations={gen_z6fsm_State_AbstractState, gen_z6fsm_Foo_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)