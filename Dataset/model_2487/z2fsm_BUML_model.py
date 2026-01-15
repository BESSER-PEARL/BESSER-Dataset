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
z2fsm_AbstractState = Class(name="z2fsm::AbstractState", is_abstract=True)
z2fsm_Region = Class(name="z2fsm::Region")
z2fsm_State = Class(name="z2fsm::State")
AbstractState = Class(name="AbstractState")
z2fsm_Foo = Class(name="z2fsm::Foo")

# z2fsm_AbstractState class attributes and methods
z2fsm_AbstractState_id: Property = Property(name="id", type=StringType)
z2fsm_AbstractState.attributes={z2fsm_AbstractState_id}

# z2fsm_Region class attributes and methods
z2fsm_Region_name: Property = Property(name="name", type=StringType)
z2fsm_Region.attributes={z2fsm_Region_name}

# z2fsm_State class attributes and methods

# AbstractState class attributes and methods

# z2fsm_Foo class attributes and methods

# Relationships
subElements0: BinaryAssociation = BinaryAssociation(
    name="subElements0",
    ends={
        Property(name="z2fsm_AbstractState", type=z2fsm_Region, multiplicity=Multiplicity(1, 1)),
        Property(name="z2fsm_Region", type=z2fsm_AbstractState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_z2fsm_State_AbstractState = Generalization(general=AbstractState, specific=z2fsm_State)
gen_z2fsm_Foo_AbstractState = Generalization(general=AbstractState, specific=z2fsm_Foo)

# Domain Model
domain_model = DomainModel(
    name="z2fsm",
    types={z2fsm_AbstractState, z2fsm_Region, z2fsm_State, AbstractState, z2fsm_Foo},
    associations={subElements0},
    generalizations={gen_z2fsm_State_AbstractState, gen_z2fsm_Foo_AbstractState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)