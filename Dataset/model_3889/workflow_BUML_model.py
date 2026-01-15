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
workflow_Named = Class(name="workflow::Named", is_abstract=True)
EObject = Class(name="EObject")
workflow_Workflow = Class(name="workflow::Workflow")
Named = Class(name="Named")
StateContainer = Class(name="StateContainer")
workflow_StateTransition = Class(name="workflow::StateTransition")
workflow_AbstractState = Class(name="workflow::AbstractState", is_abstract=True)
workflow_FromState = Class(name="workflow::FromState", is_abstract=True)
workflow_ToState = Class(name="workflow::ToState", is_abstract=True)
workflow_StateContainer = Class(name="workflow::StateContainer", is_abstract=True)
workflow_Start = Class(name="workflow::Start")
workflow_IntermediateState = Class(name="workflow::IntermediateState", is_abstract=True)
workflow_End = Class(name="workflow::End")
workflow_Task = Class(name="workflow::Task")
IntermediateState = Class(name="IntermediateState")
workflow_Processing = Class(name="workflow::Processing")
workflow_Decision = Class(name="workflow::Decision")
workflow_Fork = Class(name="workflow::Fork")
workflow_Join = Class(name="workflow::Join")
workflow_SubProcess = Class(name="workflow::SubProcess")
AbstractState = Class(name="AbstractState")
FromState = Class(name="FromState")
ToState = Class(name="ToState")

# workflow_Named class attributes and methods
workflow_Named_name: Property = Property(name="name", type=StringType)
workflow_Named.attributes={workflow_Named_name}

# EObject class attributes and methods

# workflow_Workflow class attributes and methods

# Named class attributes and methods

# StateContainer class attributes and methods

# workflow_StateTransition class attributes and methods

# workflow_AbstractState class attributes and methods
workflow_AbstractState_associatedClass: Property = Property(name="associatedClass", type=StringType)
workflow_AbstractState.attributes={workflow_AbstractState_associatedClass}

# workflow_FromState class attributes and methods

# workflow_ToState class attributes and methods

# workflow_StateContainer class attributes and methods

# workflow_Start class attributes and methods

# workflow_IntermediateState class attributes and methods

# workflow_End class attributes and methods

# workflow_Task class attributes and methods

# IntermediateState class attributes and methods

# workflow_Processing class attributes and methods

# workflow_Decision class attributes and methods

# workflow_Fork class attributes and methods

# workflow_Join class attributes and methods

# workflow_SubProcess class attributes and methods

# AbstractState class attributes and methods

# FromState class attributes and methods

# ToState class attributes and methods

# Relationships
transition0: BinaryAssociation = BinaryAssociation(
    name="transition0",
    ends={
        Property(name="workflow_StateTransition", type=workflow_Workflow, multiplicity=Multiplicity(1, 1)),
        Property(name="workflow_Workflow", type=workflow_StateTransition, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
outboundTransitions1: BinaryAssociation = BinaryAssociation(
    name="outboundTransitions1",
    ends={
        Property(name="StateTransition", type=workflow_FromState, multiplicity=Multiplicity(1, 1)),
        Property(name="from", type=workflow_StateTransition, multiplicity=Multiplicity(1, 9999))
    }
)
inboundTransitions2: BinaryAssociation = BinaryAssociation(
    name="inboundTransitions2",
    ends={
        Property(name="StateTransition3", type=workflow_ToState, multiplicity=Multiplicity(1, 1)),
        Property(name="to", type=workflow_StateTransition, multiplicity=Multiplicity(1, 9999))
    }
)
startState4: BinaryAssociation = BinaryAssociation(
    name="startState4",
    ends={
        Property(name="Start", type=workflow_StateContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="stateContainer", type=workflow_Start, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
states5: BinaryAssociation = BinaryAssociation(
    name="states5",
    ends={
        Property(name="IntermediateState", type=workflow_StateContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="stateContainer6", type=workflow_IntermediateState, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
endState7: BinaryAssociation = BinaryAssociation(
    name="endState7",
    ends={
        Property(name="End", type=workflow_StateContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="stateContainer8", type=workflow_End, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
stateContainer9: BinaryAssociation = BinaryAssociation(
    name="stateContainer9",
    ends={
        Property(name="StateContainer", type=workflow_IntermediateState, multiplicity=Multiplicity(1, 1)),
        Property(name="states", type=workflow_StateContainer, multiplicity=Multiplicity(1, 1))
    }
)
from10: BinaryAssociation = BinaryAssociation(
    name="from10",
    ends={
        Property(name="FromState", type=workflow_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="outboundTransitions", type=workflow_FromState, multiplicity=Multiplicity(1, 1))
    }
)
to11: BinaryAssociation = BinaryAssociation(
    name="to11",
    ends={
        Property(name="ToState", type=workflow_StateTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="inboundTransitions", type=workflow_ToState, multiplicity=Multiplicity(1, 1))
    }
)
stateContainer12: BinaryAssociation = BinaryAssociation(
    name="stateContainer12",
    ends={
        Property(name="StateContainer13", type=workflow_Start, multiplicity=Multiplicity(1, 1)),
        Property(name="startState", type=workflow_StateContainer, multiplicity=Multiplicity(1, 1))
    }
)
stateContainer14: BinaryAssociation = BinaryAssociation(
    name="stateContainer14",
    ends={
        Property(name="StateContainer15", type=workflow_End, multiplicity=Multiplicity(1, 1)),
        Property(name="endState", type=workflow_StateContainer, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_workflow_Named_EObject = Generalization(general=EObject, specific=workflow_Named)
gen_workflow_Workflow_Named = Generalization(general=Named, specific=workflow_Workflow)
gen_workflow_Workflow_StateContainer = Generalization(general=StateContainer, specific=workflow_Workflow)
gen_workflow_AbstractState_Named = Generalization(general=Named, specific=workflow_AbstractState)
gen_workflow_Task_IntermediateState = Generalization(general=IntermediateState, specific=workflow_Task)
gen_workflow_Processing_IntermediateState = Generalization(general=IntermediateState, specific=workflow_Processing)
gen_workflow_Decision_IntermediateState = Generalization(general=IntermediateState, specific=workflow_Decision)
gen_workflow_Fork_IntermediateState = Generalization(general=IntermediateState, specific=workflow_Fork)
gen_workflow_Join_IntermediateState = Generalization(general=IntermediateState, specific=workflow_Join)
gen_workflow_SubProcess_StateContainer = Generalization(general=StateContainer, specific=workflow_SubProcess)
gen_workflow_SubProcess_IntermediateState = Generalization(general=IntermediateState, specific=workflow_SubProcess)
gen_workflow_IntermediateState_AbstractState = Generalization(general=AbstractState, specific=workflow_IntermediateState)
gen_workflow_IntermediateState_FromState = Generalization(general=FromState, specific=workflow_IntermediateState)
gen_workflow_IntermediateState_ToState = Generalization(general=ToState, specific=workflow_IntermediateState)
gen_workflow_StateTransition_Named = Generalization(general=Named, specific=workflow_StateTransition)
gen_workflow_Start_AbstractState = Generalization(general=AbstractState, specific=workflow_Start)
gen_workflow_Start_FromState = Generalization(general=FromState, specific=workflow_Start)
gen_workflow_End_AbstractState = Generalization(general=AbstractState, specific=workflow_End)
gen_workflow_End_ToState = Generalization(general=ToState, specific=workflow_End)

# Domain Model
domain_model = DomainModel(
    name="workflow",
    types={workflow_Named, EObject, workflow_Workflow, Named, StateContainer, workflow_StateTransition, workflow_AbstractState, workflow_FromState, workflow_ToState, workflow_StateContainer, workflow_Start, workflow_IntermediateState, workflow_End, workflow_Task, IntermediateState, workflow_Processing, workflow_Decision, workflow_Fork, workflow_Join, workflow_SubProcess, AbstractState, FromState, ToState},
    associations={transition0, outboundTransitions1, inboundTransitions2, startState4, states5, endState7, stateContainer9, from10, to11, stateContainer12, stateContainer14},
    generalizations={gen_workflow_Named_EObject, gen_workflow_Workflow_Named, gen_workflow_Workflow_StateContainer, gen_workflow_AbstractState_Named, gen_workflow_Task_IntermediateState, gen_workflow_Processing_IntermediateState, gen_workflow_Decision_IntermediateState, gen_workflow_Fork_IntermediateState, gen_workflow_Join_IntermediateState, gen_workflow_SubProcess_StateContainer, gen_workflow_SubProcess_IntermediateState, gen_workflow_IntermediateState_AbstractState, gen_workflow_IntermediateState_FromState, gen_workflow_IntermediateState_ToState, gen_workflow_StateTransition_Named, gen_workflow_Start_AbstractState, gen_workflow_Start_FromState, gen_workflow_End_AbstractState, gen_workflow_End_ToState},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)