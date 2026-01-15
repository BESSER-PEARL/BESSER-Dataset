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
fsmProv_Region = Class(name="fsmProv::Region")
fsmProv_StateMachine = Class(name="fsmProv::StateMachine")
fsmProv_AbstractState = Class(name="fsmProv::AbstractState", is_abstract=True)
fsmProv_State = Class(name="fsmProv::State")
fsmProv_Transition = Class(name="fsmProv::Transition")
fsmProv_Trigger = Class(name="fsmProv::Trigger")

# fsmProv_Region class attributes and methods

# fsmProv_StateMachine class attributes and methods

# fsmProv_AbstractState class attributes and methods

# fsmProv_State class attributes and methods

# fsmProv_Transition class attributes and methods

# fsmProv_Trigger class attributes and methods
fsmProv_Trigger_expression: Property = Property(name="expression", type=StringType)
fsmProv_Trigger_m_evalTrigger: Method = Method(name="evalTrigger", parameters={Parameter(name='events')}, type=BooleanType)
fsmProv_Trigger.attributes={fsmProv_Trigger_expression}
fsmProv_Trigger.methods={fsmProv_Trigger_m_evalTrigger}

# Domain Model
domain_model = DomainModel(
    name="fsmProv",
    types={fsmProv_Region, fsmProv_StateMachine, fsmProv_AbstractState, fsmProv_State, fsmProv_Transition, fsmProv_Trigger},
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