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
petrinet_Net = Class(name="petrinet::Net")
petrinet_Place = Class(name="petrinet::Place")
petrinet_Transition = Class(name="petrinet::Transition")
petrinet_NetStopEvent = Class(name="petrinet::NetStopEvent")
petrinet_TransitionFireEvent = Class(name="petrinet::TransitionFireEvent")
petrinet_Token = Class(name="petrinet::Token")

# petrinet_Net class attributes and methods
petrinet_Net_m_initializeModel: Method = Method(name="initializeModel", parameters={Parameter(name='args')})
petrinet_Net_m_run: Method = Method(name="run", parameters={})
petrinet_Net_m_fireEnabledTransition: Method = Method(name="fireEnabledTransition", parameters={})
petrinet_Net_m_stop: Method = Method(name="stop", parameters={})
petrinet_Net.methods={petrinet_Net_m_stop, petrinet_Net_m_initializeModel, petrinet_Net_m_fireEnabledTransition, petrinet_Net_m_run}

# petrinet_Place class attributes and methods
petrinet_Place_name: Property = Property(name="name", type=StringType)
petrinet_Place_initialTokens: Property = Property(name="initialTokens", type=IntegerType)
petrinet_Place.attributes={petrinet_Place_name, petrinet_Place_initialTokens}

# petrinet_Transition class attributes and methods
petrinet_Transition_name: Property = Property(name="name", type=StringType)
petrinet_Transition_m_isEnabled: Method = Method(name="isEnabled", parameters={})
petrinet_Transition_m_fire: Method = Method(name="fire", parameters={})
petrinet_Transition_m_fire_PreCondition: Method = Method(name="fire_PreCondition", parameters={})
petrinet_Transition.attributes={petrinet_Transition_name}
petrinet_Transition.methods={petrinet_Transition_m_fire, petrinet_Transition_m_fire_PreCondition, petrinet_Transition_m_isEnabled}

# petrinet_NetStopEvent class attributes and methods

# petrinet_TransitionFireEvent class attributes and methods

# petrinet_Token class attributes and methods

# Relationships
transitions1: BinaryAssociation = BinaryAssociation(
    name="transitions1",
    ends={
        Property(name="petrinet_Net2", type=petrinet_Transition, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="petrinet_Transition", type=petrinet_Net, multiplicity=Multiplicity(1, 1))
    }
)
places0: BinaryAssociation = BinaryAssociation(
    name="places0",
    ends={
        Property(name="petrinet_Place", type=petrinet_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Net", type=petrinet_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
net11: BinaryAssociation = BinaryAssociation(
    name="net11",
    ends={
        Property(name="petrinet_Net12", type=petrinet_NetStopEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_NetStopEvent", type=petrinet_Net, multiplicity=Multiplicity(0, 1))
    }
)
transition13: BinaryAssociation = BinaryAssociation(
    name="transition13",
    ends={
        Property(name="petrinet_Transition14", type=petrinet_TransitionFireEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_TransitionFireEvent", type=petrinet_Transition, multiplicity=Multiplicity(0, 1))
    }
)
input3: BinaryAssociation = BinaryAssociation(
    name="input3",
    ends={
        Property(name="petrinet_Place5", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition4", type=petrinet_Place, multiplicity=Multiplicity(1, 9999))
    }
)
output6: BinaryAssociation = BinaryAssociation(
    name="output6",
    ends={
        Property(name="petrinet_Place8", type=petrinet_Transition, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Transition7", type=petrinet_Place, multiplicity=Multiplicity(1, 9999))
    }
)
tokens9: BinaryAssociation = BinaryAssociation(
    name="tokens9",
    ends={
        Property(name="petrinet_Token", type=petrinet_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinet_Place10", type=petrinet_Token, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinet",
    types={petrinet_Net, petrinet_Place, petrinet_Transition, petrinet_NetStopEvent, petrinet_TransitionFireEvent, petrinet_Token},
    associations={transitions1, places0, net11, transition13, input3, output6, tokens9},
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