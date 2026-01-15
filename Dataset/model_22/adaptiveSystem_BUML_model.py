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
Temp: Enumeration = Enumeration(
    name="Temp",
    literals={
            EnumerationLiteral(name="cold"),
			EnumerationLiteral(name="without"),
			EnumerationLiteral(name="hot")
    }
)

Orientation: Enumeration = Enumeration(
    name="Orientation",
    literals={
            EnumerationLiteral(name="normal"),
			EnumerationLiteral(name="anti")
    }
)

Quantor: Enumeration = Enumeration(
    name="Quantor",
    literals={
            EnumerationLiteral(name="universal"),
			EnumerationLiteral(name="existencial")
    }
)

# Classes
adaptiveSystem_DoNet = Class(name="adaptiveSystem::DoNet")
adaptiveSystem_AdaptiveSystem = Class(name="adaptiveSystem::AdaptiveSystem")
adaptiveSystem_Oclet = Class(name="adaptiveSystem::Oclet")
adaptiveSystem_AdaptiveProcess = Class(name="adaptiveSystem::AdaptiveProcess")
adaptiveSystem_PreNet = Class(name="adaptiveSystem::PreNet")
adaptiveSystem_OccurrenceNet = Class(name="adaptiveSystem::OccurrenceNet", is_abstract=True)
adaptiveSystem_Node = Class(name="adaptiveSystem::Node", is_abstract=True)
adaptiveSystem_Arc = Class(name="adaptiveSystem::Arc")
OccurrenceNet = Class(name="OccurrenceNet")
adaptiveSystem_Condition = Class(name="adaptiveSystem::Condition")
Node = Class(name="Node")
adaptiveSystem_Event = Class(name="adaptiveSystem::Event")
adaptiveSystem_ArcToCondition = Class(name="adaptiveSystem::ArcToCondition")
adaptiveSystem_ArcToEvent = Class(name="adaptiveSystem::ArcToEvent")
Arc = Class(name="Arc")

# adaptiveSystem_DoNet class attributes and methods

# adaptiveSystem_AdaptiveSystem class attributes and methods
adaptiveSystem_AdaptiveSystem_setWellformednessToOclets: Property = Property(name="setWellformednessToOclets", type=BooleanType)
adaptiveSystem_AdaptiveSystem.attributes={adaptiveSystem_AdaptiveSystem_setWellformednessToOclets}

# adaptiveSystem_Oclet class attributes and methods
adaptiveSystem_Oclet_name: Property = Property(name="name", type=StringType)
adaptiveSystem_Oclet_orientation: Property = Property(name="orientation", type=StringType)
adaptiveSystem_Oclet_quantor: Property = Property(name="quantor", type=StringType)
adaptiveSystem_Oclet_wellFormed: Property = Property(name="wellFormed", type=BooleanType)
adaptiveSystem_Oclet.attributes={adaptiveSystem_Oclet_wellFormed, adaptiveSystem_Oclet_name, adaptiveSystem_Oclet_orientation, adaptiveSystem_Oclet_quantor}

# adaptiveSystem_AdaptiveProcess class attributes and methods

# adaptiveSystem_PreNet class attributes and methods

# adaptiveSystem_OccurrenceNet class attributes and methods
adaptiveSystem_OccurrenceNet_name: Property = Property(name="name", type=StringType)
adaptiveSystem_OccurrenceNet.attributes={adaptiveSystem_OccurrenceNet_name}

# adaptiveSystem_Node class attributes and methods
adaptiveSystem_Node_disabledByConflict: Property = Property(name="disabledByConflict", type=BooleanType)
adaptiveSystem_Node_name: Property = Property(name="name", type=StringType)
adaptiveSystem_Node_abstract: Property = Property(name="abstract", type=BooleanType)
adaptiveSystem_Node_temp: Property = Property(name="temp", type=StringType)
adaptiveSystem_Node_disabledByAntiOclet: Property = Property(name="disabledByAntiOclet", type=BooleanType)
adaptiveSystem_Node.attributes={adaptiveSystem_Node_disabledByConflict, adaptiveSystem_Node_name, adaptiveSystem_Node_abstract, adaptiveSystem_Node_temp, adaptiveSystem_Node_disabledByAntiOclet}

# adaptiveSystem_Arc class attributes and methods
adaptiveSystem_Arc_weight: Property = Property(name="weight", type=IntegerType)
adaptiveSystem_Arc.attributes={adaptiveSystem_Arc_weight}

# OccurrenceNet class attributes and methods

# adaptiveSystem_Condition class attributes and methods
adaptiveSystem_Condition_token: Property = Property(name="token", type=IntegerType)
adaptiveSystem_Condition_marked: Property = Property(name="marked", type=BooleanType)
adaptiveSystem_Condition_maximal: Property = Property(name="maximal", type=BooleanType)
adaptiveSystem_Condition_minimal: Property = Property(name="minimal", type=BooleanType)
adaptiveSystem_Condition.attributes={adaptiveSystem_Condition_marked, adaptiveSystem_Condition_maximal, adaptiveSystem_Condition_token, adaptiveSystem_Condition_minimal}

# Node class attributes and methods

# adaptiveSystem_Event class attributes and methods
adaptiveSystem_Event_saturated: Property = Property(name="saturated", type=BooleanType)
adaptiveSystem_Event_enabled: Property = Property(name="enabled", type=BooleanType)
adaptiveSystem_Event.attributes={adaptiveSystem_Event_saturated, adaptiveSystem_Event_enabled}

# adaptiveSystem_ArcToCondition class attributes and methods

# adaptiveSystem_ArcToEvent class attributes and methods

# Arc class attributes and methods

# Relationships
oclets0: BinaryAssociation = BinaryAssociation(
    name="oclets0",
    ends={
        Property(name="adaptiveSystem_Oclet", type=adaptiveSystem_AdaptiveSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptiveSystem_AdaptiveSystem", type=adaptiveSystem_Oclet, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
adaptiveProcess1: BinaryAssociation = BinaryAssociation(
    name="adaptiveProcess1",
    ends={
        Property(name="adaptiveSystem_AdaptiveProcess", type=adaptiveSystem_AdaptiveSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptiveSystem_AdaptiveSystem2", type=adaptiveSystem_AdaptiveProcess, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
preNet3: BinaryAssociation = BinaryAssociation(
    name="preNet3",
    ends={
        Property(name="adaptiveSystem_PreNet", type=adaptiveSystem_Oclet, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptiveSystem_Oclet4", type=adaptiveSystem_PreNet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
markedConditions10: BinaryAssociation = BinaryAssociation(
    name="markedConditions10",
    ends={
        Property(name="adaptiveSystem_Condition", type=adaptiveSystem_PreNet, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptiveSystem_PreNet11", type=adaptiveSystem_Condition, multiplicity=Multiplicity(0, 9999))
    }
)
doNet5: BinaryAssociation = BinaryAssociation(
    name="doNet5",
    ends={
        Property(name="adaptiveSystem_DoNet", type=adaptiveSystem_Oclet, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptiveSystem_Oclet6", type=adaptiveSystem_DoNet, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
nodes7: BinaryAssociation = BinaryAssociation(
    name="nodes7",
    ends={
        Property(name="adaptiveSystem_Node", type=adaptiveSystem_OccurrenceNet, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptiveSystem_OccurrenceNet", type=adaptiveSystem_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
arcs8: BinaryAssociation = BinaryAssociation(
    name="arcs8",
    ends={
        Property(name="adaptiveSystem_Arc", type=adaptiveSystem_OccurrenceNet, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptiveSystem_OccurrenceNet9", type=adaptiveSystem_Arc, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
markedConditions12: BinaryAssociation = BinaryAssociation(
    name="markedConditions12",
    ends={
        Property(name="adaptiveSystem_Condition14", type=adaptiveSystem_AdaptiveProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="adaptiveSystem_AdaptiveProcess13", type=adaptiveSystem_Condition, multiplicity=Multiplicity(0, 9999))
    }
)
preEvents15: BinaryAssociation = BinaryAssociation(
    name="preEvents15",
    ends={
        Property(name="Event", type=adaptiveSystem_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="postConditions", type=adaptiveSystem_Event, multiplicity=Multiplicity(0, 9999))
    }
)
postEvents16: BinaryAssociation = BinaryAssociation(
    name="postEvents16",
    ends={
        Property(name="Event17", type=adaptiveSystem_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="preConditions", type=adaptiveSystem_Event, multiplicity=Multiplicity(0, 9999))
    }
)
incoming18: BinaryAssociation = BinaryAssociation(
    name="incoming18",
    ends={
        Property(name="ArcToCondition", type=adaptiveSystem_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="destination", type=adaptiveSystem_ArcToCondition, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing19: BinaryAssociation = BinaryAssociation(
    name="outgoing19",
    ends={
        Property(name="ArcToEvent", type=adaptiveSystem_Condition, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=adaptiveSystem_ArcToEvent, multiplicity=Multiplicity(0, 9999))
    }
)
preConditions20: BinaryAssociation = BinaryAssociation(
    name="preConditions20",
    ends={
        Property(name="Condition", type=adaptiveSystem_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="postEvents", type=adaptiveSystem_Condition, multiplicity=Multiplicity(0, 9999))
    }
)
postConditions21: BinaryAssociation = BinaryAssociation(
    name="postConditions21",
    ends={
        Property(name="Condition22", type=adaptiveSystem_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="preEvents", type=adaptiveSystem_Condition, multiplicity=Multiplicity(0, 9999))
    }
)
destination31: BinaryAssociation = BinaryAssociation(
    name="destination31",
    ends={
        Property(name="Event32", type=adaptiveSystem_ArcToEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=adaptiveSystem_Event, multiplicity=Multiplicity(0, 1))
    }
)
incoming23: BinaryAssociation = BinaryAssociation(
    name="incoming23",
    ends={
        Property(name="ArcToEvent25", type=adaptiveSystem_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="destination24", type=adaptiveSystem_ArcToEvent, multiplicity=Multiplicity(0, 9999))
    }
)
outgoing26: BinaryAssociation = BinaryAssociation(
    name="outgoing26",
    ends={
        Property(name="ArcToCondition28", type=adaptiveSystem_Event, multiplicity=Multiplicity(1, 1)),
        Property(name="source27", type=adaptiveSystem_ArcToCondition, multiplicity=Multiplicity(0, 9999))
    }
)
source33: BinaryAssociation = BinaryAssociation(
    name="source33",
    ends={
        Property(name="Event35", type=adaptiveSystem_ArcToCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing34", type=adaptiveSystem_Event, multiplicity=Multiplicity(0, 1))
    }
)
source29: BinaryAssociation = BinaryAssociation(
    name="source29",
    ends={
        Property(name="Condition30", type=adaptiveSystem_ArcToEvent, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=adaptiveSystem_Condition, multiplicity=Multiplicity(0, 1))
    }
)
destination36: BinaryAssociation = BinaryAssociation(
    name="destination36",
    ends={
        Property(name="Condition38", type=adaptiveSystem_ArcToCondition, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming37", type=adaptiveSystem_Condition, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_adaptiveSystem_DoNet_OccurrenceNet = Generalization(general=OccurrenceNet, specific=adaptiveSystem_DoNet)
gen_adaptiveSystem_PreNet_OccurrenceNet = Generalization(general=OccurrenceNet, specific=adaptiveSystem_PreNet)
gen_adaptiveSystem_AdaptiveProcess_OccurrenceNet = Generalization(general=OccurrenceNet, specific=adaptiveSystem_AdaptiveProcess)
gen_adaptiveSystem_Condition_Node = Generalization(general=Node, specific=adaptiveSystem_Condition)
gen_adaptiveSystem_Event_Node = Generalization(general=Node, specific=adaptiveSystem_Event)
gen_adaptiveSystem_ArcToCondition_Arc = Generalization(general=Arc, specific=adaptiveSystem_ArcToCondition)
gen_adaptiveSystem_ArcToEvent_Arc = Generalization(general=Arc, specific=adaptiveSystem_ArcToEvent)

# Domain Model
domain_model = DomainModel(
    name="adaptiveSystem",
    types={adaptiveSystem_DoNet, adaptiveSystem_AdaptiveSystem, adaptiveSystem_Oclet, adaptiveSystem_AdaptiveProcess, adaptiveSystem_PreNet, adaptiveSystem_OccurrenceNet, adaptiveSystem_Node, adaptiveSystem_Arc, OccurrenceNet, adaptiveSystem_Condition, Node, adaptiveSystem_Event, adaptiveSystem_ArcToCondition, adaptiveSystem_ArcToEvent, Arc, Temp, Orientation, Quantor},
    associations={oclets0, adaptiveProcess1, preNet3, markedConditions10, doNet5, nodes7, arcs8, markedConditions12, preEvents15, postEvents16, incoming18, outgoing19, preConditions20, postConditions21, destination31, incoming23, outgoing26, source33, source29, destination36},
    generalizations={gen_adaptiveSystem_DoNet_OccurrenceNet, gen_adaptiveSystem_PreNet_OccurrenceNet, gen_adaptiveSystem_AdaptiveProcess_OccurrenceNet, gen_adaptiveSystem_Condition_Node, gen_adaptiveSystem_Event_Node, gen_adaptiveSystem_ArcToCondition_Arc, gen_adaptiveSystem_ArcToEvent_Arc},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)