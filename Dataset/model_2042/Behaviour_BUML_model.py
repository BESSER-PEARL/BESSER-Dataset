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
Behaviour_PreTransitionConnection = Class(name="Behaviour::PreTransitionConnection")
Behaviour_Connection = Class(name="Behaviour::Connection", is_abstract=True)
Behaviour_Place = Class(name="Behaviour::Place", is_abstract=True)
Identifier = Class(name="Identifier")
Behaviour_Token = Class(name="Behaviour::Token")
Behaviour_Transition = Class(name="Behaviour::Transition", is_abstract=True)
Behaviour_PostTransitionConnection = Class(name="Behaviour::PostTransitionConnection")
Connection = Class(name="Connection")
Behaviour_DefaultPlace = Class(name="Behaviour::DefaultPlace")
Place = Class(name="Place")
Behaviour_QueuePlace = Class(name="Behaviour::QueuePlace", is_abstract=True)
Behaviour_Server = Class(name="Behaviour::Server")
Behaviour_WaitingLine = Class(name="Behaviour::WaitingLine")
Behaviour_StartPlace = Class(name="Behaviour::StartPlace")
Behaviour_ConditionalTransition = Class(name="Behaviour::ConditionalTransition")
Transition = Class(name="Transition")
Behaviour_TransitionFunction = Class(name="Behaviour::TransitionFunction")
Behaviour_StochasticTransition = Class(name="Behaviour::StochasticTransition")
Behaviour_Description = Class(name="Behaviour::Description")
Behaviour_Colour = Class(name="Behaviour::Colour")

# Behaviour_PreTransitionConnection class attributes and methods
Behaviour_PreTransitionConnection_requiredTokenAmount: Property = Property(name="requiredTokenAmount", type=IntegerType)
Behaviour_PreTransitionConnection.attributes={Behaviour_PreTransitionConnection_requiredTokenAmount}

# Behaviour_Connection class attributes and methods

# Behaviour_Place class attributes and methods

# Identifier class attributes and methods

# Behaviour_Token class attributes and methods

# Behaviour_Transition class attributes and methods

# Behaviour_PostTransitionConnection class attributes and methods

# Connection class attributes and methods

# Behaviour_DefaultPlace class attributes and methods

# Place class attributes and methods

# Behaviour_QueuePlace class attributes and methods

# Behaviour_Server class attributes and methods
Behaviour_Server_capacity: Property = Property(name="capacity", type=IntegerType)
Behaviour_Server.attributes={Behaviour_Server_capacity}

# Behaviour_WaitingLine class attributes and methods
Behaviour_WaitingLine_schedulingPolicy: Property = Property(name="schedulingPolicy", type=StringType)
Behaviour_WaitingLine.attributes={Behaviour_WaitingLine_schedulingPolicy}

# Behaviour_StartPlace class attributes and methods
Behaviour_StartPlace_spawnPolicy: Property = Property(name="spawnPolicy", type=StringType)
Behaviour_StartPlace.attributes={Behaviour_StartPlace_spawnPolicy}

# Behaviour_ConditionalTransition class attributes and methods

# Transition class attributes and methods

# Behaviour_TransitionFunction class attributes and methods
Behaviour_TransitionFunction_transitionFunction: Property = Property(name="transitionFunction", type=StringType)
Behaviour_TransitionFunction.attributes={Behaviour_TransitionFunction_transitionFunction}

# Behaviour_StochasticTransition class attributes and methods

# Behaviour_Description class attributes and methods

# Behaviour_Colour class attributes and methods
Behaviour_Colour_attribute: Property = Property(name="attribute", type=StringType)
Behaviour_Colour.attributes={Behaviour_Colour_attribute}

# Relationships
incommingEdges2: BinaryAssociation = BinaryAssociation(
    name="incommingEdges2",
    ends={
        Property(name="Behaviour_PreTransitionConnection", type=Behaviour_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Transition3", type=Behaviour_PreTransitionConnection, multiplicity=Multiplicity(1, 9999))
    }
)
place4: BinaryAssociation = BinaryAssociation(
    name="place4",
    ends={
        Property(name="Behaviour_Place5", type=Behaviour_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Connection", type=Behaviour_Place, multiplicity=Multiplicity(1, 1))
    }
)
transition6: BinaryAssociation = BinaryAssociation(
    name="transition6",
    ends={
        Property(name="Behaviour_Transition8", type=Behaviour_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Connection7", type=Behaviour_Transition, multiplicity=Multiplicity(1, 1))
    }
)
token0: BinaryAssociation = BinaryAssociation(
    name="token0",
    ends={
        Property(name="Behaviour_Token", type=Behaviour_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Place", type=Behaviour_Token, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingEdges1: BinaryAssociation = BinaryAssociation(
    name="outgoingEdges1",
    ends={
        Property(name="Behaviour_PostTransitionConnection", type=Behaviour_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Transition", type=Behaviour_PostTransitionConnection, multiplicity=Multiplicity(0, 9999))
    }
)
preTransitions9: BinaryAssociation = BinaryAssociation(
    name="preTransitions9",
    ends={
        Property(name="Behaviour_PreTransitionConnection10", type=Behaviour_DefaultPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_DefaultPlace", type=Behaviour_PreTransitionConnection, multiplicity=Multiplicity(1, 9999))
    }
)
postTransitions11: BinaryAssociation = BinaryAssociation(
    name="postTransitions11",
    ends={
        Property(name="Behaviour_PostTransitionConnection13", type=Behaviour_DefaultPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_DefaultPlace12", type=Behaviour_PostTransitionConnection, multiplicity=Multiplicity(1, 9999))
    }
)
server14: BinaryAssociation = BinaryAssociation(
    name="server14",
    ends={
        Property(name="Behaviour_Server", type=Behaviour_QueuePlace, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_QueuePlace", type=Behaviour_Server, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
waitingLine15: BinaryAssociation = BinaryAssociation(
    name="waitingLine15",
    ends={
        Property(name="Behaviour_WaitingLine", type=Behaviour_QueuePlace, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_QueuePlace16", type=Behaviour_WaitingLine, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
preTransitions17: BinaryAssociation = BinaryAssociation(
    name="preTransitions17",
    ends={
        Property(name="Behaviour_PreTransitionConnection18", type=Behaviour_StartPlace, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_StartPlace", type=Behaviour_PreTransitionConnection, multiplicity=Multiplicity(1, 9999))
    }
)
transitionFunction19: BinaryAssociation = BinaryAssociation(
    name="transitionFunction19",
    ends={
        Property(name="Behaviour_TransitionFunction", type=Behaviour_ConditionalTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_ConditionalTransition", type=Behaviour_TransitionFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionFunction20: BinaryAssociation = BinaryAssociation(
    name="transitionFunction20",
    ends={
        Property(name="Behaviour_TransitionFunction21", type=Behaviour_StochasticTransition, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_StochasticTransition", type=Behaviour_TransitionFunction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
waitingLine22: BinaryAssociation = BinaryAssociation(
    name="waitingLine22",
    ends={
        Property(name="WaitingLine", type=Behaviour_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="server", type=Behaviour_WaitingLine, multiplicity=Multiplicity(1, 1))
    }
)
preTransition23: BinaryAssociation = BinaryAssociation(
    name="preTransition23",
    ends={
        Property(name="Behaviour_PreTransitionConnection25", type=Behaviour_Server, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Server24", type=Behaviour_PreTransitionConnection, multiplicity=Multiplicity(1, 1))
    }
)
arrows32: BinaryAssociation = BinaryAssociation(
    name="arrows32",
    ends={
        Property(name="Behaviour_Connection33", type=Behaviour_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Description", type=Behaviour_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
place34: BinaryAssociation = BinaryAssociation(
    name="place34",
    ends={
        Property(name="Behaviour_Place36", type=Behaviour_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Description35", type=Behaviour_Place, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
server26: BinaryAssociation = BinaryAssociation(
    name="server26",
    ends={
        Property(name="Server", type=Behaviour_WaitingLine, multiplicity=Multiplicity(1, 1)),
        Property(name="waitingLine", type=Behaviour_Server, multiplicity=Multiplicity(1, 1))
    }
)
postTransitions27: BinaryAssociation = BinaryAssociation(
    name="postTransitions27",
    ends={
        Property(name="Behaviour_PostTransitionConnection29", type=Behaviour_WaitingLine, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_WaitingLine28", type=Behaviour_PostTransitionConnection, multiplicity=Multiplicity(1, 9999))
    }
)
attributes30: BinaryAssociation = BinaryAssociation(
    name="attributes30",
    ends={
        Property(name="Behaviour_Colour", type=Behaviour_Token, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Token31", type=Behaviour_Colour, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transition37: BinaryAssociation = BinaryAssociation(
    name="transition37",
    ends={
        Property(name="Behaviour_Transition39", type=Behaviour_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Description38", type=Behaviour_Transition, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
token40: BinaryAssociation = BinaryAssociation(
    name="token40",
    ends={
        Property(name="Behaviour_Token42", type=Behaviour_Description, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_Description41", type=Behaviour_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transitionConnection43: BinaryAssociation = BinaryAssociation(
    name="transitionConnection43",
    ends={
        Property(name="Behaviour_PostTransitionConnection45", type=Behaviour_TransitionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_TransitionFunction44", type=Behaviour_PostTransitionConnection, multiplicity=Multiplicity(1, 1))
    }
)
emittedToken46: BinaryAssociation = BinaryAssociation(
    name="emittedToken46",
    ends={
        Property(name="Behaviour_Token48", type=Behaviour_TransitionFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="Behaviour_TransitionFunction47", type=Behaviour_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_Behaviour_Connection_Identifier = Generalization(general=Identifier, specific=Behaviour_Connection)
gen_Behaviour_Place_Identifier = Generalization(general=Identifier, specific=Behaviour_Place)
gen_Behaviour_Transition_Identifier = Generalization(general=Identifier, specific=Behaviour_Transition)
gen_Behaviour_PostTransitionConnection_Connection = Generalization(general=Connection, specific=Behaviour_PostTransitionConnection)
gen_Behaviour_PreTransitionConnection_Connection = Generalization(general=Connection, specific=Behaviour_PreTransitionConnection)
gen_Behaviour_DefaultPlace_Place = Generalization(general=Place, specific=Behaviour_DefaultPlace)
gen_Behaviour_QueuePlace_Place = Generalization(general=Place, specific=Behaviour_QueuePlace)
gen_Behaviour_StartPlace_Place = Generalization(general=Place, specific=Behaviour_StartPlace)
gen_Behaviour_ConditionalTransition_Transition = Generalization(general=Transition, specific=Behaviour_ConditionalTransition)
gen_Behaviour_StochasticTransition_Transition = Generalization(general=Transition, specific=Behaviour_StochasticTransition)
gen_Behaviour_Server_Place = Generalization(general=Place, specific=Behaviour_Server)
gen_Behaviour_Description_Identifier = Generalization(general=Identifier, specific=Behaviour_Description)
gen_Behaviour_WaitingLine_Place = Generalization(general=Place, specific=Behaviour_WaitingLine)
gen_Behaviour_Token_Identifier = Generalization(general=Identifier, specific=Behaviour_Token)
gen_Behaviour_Colour_Identifier = Generalization(general=Identifier, specific=Behaviour_Colour)

# Domain Model
domain_model = DomainModel(
    name="Behaviour",
    types={Behaviour_PreTransitionConnection, Behaviour_Connection, Behaviour_Place, Identifier, Behaviour_Token, Behaviour_Transition, Behaviour_PostTransitionConnection, Connection, Behaviour_DefaultPlace, Place, Behaviour_QueuePlace, Behaviour_Server, Behaviour_WaitingLine, Behaviour_StartPlace, Behaviour_ConditionalTransition, Transition, Behaviour_TransitionFunction, Behaviour_StochasticTransition, Behaviour_Description, Behaviour_Colour},
    associations={incommingEdges2, place4, transition6, token0, outgoingEdges1, preTransitions9, postTransitions11, server14, waitingLine15, preTransitions17, transitionFunction19, transitionFunction20, waitingLine22, preTransition23, arrows32, place34, server26, postTransitions27, attributes30, transition37, token40, transitionConnection43, emittedToken46},
    generalizations={gen_Behaviour_Connection_Identifier, gen_Behaviour_Place_Identifier, gen_Behaviour_Transition_Identifier, gen_Behaviour_PostTransitionConnection_Connection, gen_Behaviour_PreTransitionConnection_Connection, gen_Behaviour_DefaultPlace_Place, gen_Behaviour_QueuePlace_Place, gen_Behaviour_StartPlace_Place, gen_Behaviour_ConditionalTransition_Transition, gen_Behaviour_StochasticTransition_Transition, gen_Behaviour_Server_Place, gen_Behaviour_Description_Identifier, gen_Behaviour_WaitingLine_Place, gen_Behaviour_Token_Identifier, gen_Behaviour_Colour_Identifier},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)