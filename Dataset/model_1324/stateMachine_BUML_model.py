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

# Enumerations
VisibilityType: Enumeration = Enumeration(
    name="VisibilityType",
    literals={
            EnumerationLiteral(name="PUBLIC"),
			EnumerationLiteral(name="PRIVATE")
    }
)

# Classes
stateMachine_AbstractStateElement = Class(name="stateMachine::AbstractStateElement", is_abstract=True)
stateMachine_StateMachine = Class(name="stateMachine::StateMachine")
stateMachine_AbstractMachineElement = Class(name="stateMachine::AbstractMachineElement", is_abstract=True)
stateMachine_State = Class(name="stateMachine::State")
AbstractStateElement = Class(name="AbstractStateElement")
stateMachine_StateTransition = Class(name="stateMachine::StateTransition")
AbstractMachineElement = Class(name="AbstractMachineElement")

# stateMachine_AbstractStateElement class attributes and methods
stateMachine_AbstractStateElement_name: Property = Property(name="name", type=StringType)
stateMachine_AbstractStateElement.attributes={stateMachine_AbstractStateElement_name}

# stateMachine_StateMachine class attributes and methods
stateMachine_StateMachine_name: Property = Property(name="name", type=StringType)
stateMachine_StateMachine.attributes={stateMachine_StateMachine_name}

# stateMachine_AbstractMachineElement class attributes and methods

# stateMachine_State class attributes and methods

# AbstractStateElement class attributes and methods

# stateMachine_StateTransition class attributes and methods
stateMachine_StateTransition_visibility: Property = Property(name="visibility", type=StringType)
stateMachine_StateTransition.attributes={stateMachine_StateTransition_visibility}

# AbstractMachineElement class attributes and methods

# Relationships
from0: BinaryAssociation = BinaryAssociation(
    name="from0",
    ends={
        Property(name="stateMachine_AbstractStateElement", type=stateMachine_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateTransition", type=stateMachine_AbstractStateElement, multiplicity=Multiplicity(1, 1))
    }
)
to1: BinaryAssociation = BinaryAssociation(
    name="to1",
    ends={
        Property(name="stateMachine_AbstractStateElement3", type=stateMachine_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateTransition2", type=stateMachine_AbstractStateElement, multiplicity=Multiplicity(1, 1))
    }
)
elements4: BinaryAssociation = BinaryAssociation(
    name="elements4",
    ends={
        Property(name="stateMachine_AbstractMachineElement", type=stateMachine_StateMachine, multiplicity=Multiplicity(1, 1)),
        Property(name="stateMachine_StateMachine", type=stateMachine_AbstractMachineElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_stateMachine_AbstractStateElement_AbstractMachineElement = Generalization(general=AbstractMachineElement, specific=stateMachine_AbstractStateElement)
gen_stateMachine_State_AbstractStateElement = Generalization(general=AbstractStateElement, specific=stateMachine_State)
gen_stateMachine_StateTransition_AbstractMachineElement = Generalization(general=AbstractMachineElement, specific=stateMachine_StateTransition)

# Domain Model
domain_model = DomainModel(
    name="stateMachine",
    types={stateMachine_AbstractStateElement, stateMachine_StateMachine, stateMachine_AbstractMachineElement, stateMachine_State, AbstractStateElement, stateMachine_StateTransition, AbstractMachineElement, VisibilityType},
    associations={from0, to1, elements4},
    generalizations={gen_stateMachine_AbstractStateElement_AbstractMachineElement, gen_stateMachine_State_AbstractStateElement, gen_stateMachine_StateTransition_AbstractMachineElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)