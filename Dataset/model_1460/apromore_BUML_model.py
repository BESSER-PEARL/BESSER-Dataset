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
apromore_Edge = Class(name="apromore::Edge")
apromore_CanonicalProcess = Class(name="apromore::CanonicalProcess")
apromore_Net = Class(name="apromore::Net")
apromore_Node = Class(name="apromore::Node", is_abstract=True)
apromore_Routing = Class(name="apromore::Routing")
apromore_Split = Class(name="apromore::Split")
Routing = Class(name="Routing")
apromore_ORSplit = Class(name="apromore::ORSplit")
Split = Class(name="Split")
apromore_XORSplit = Class(name="apromore::XORSplit")
apromore_ANDSplit = Class(name="apromore::ANDSplit")
apromore_Work = Class(name="apromore::Work")
Node = Class(name="Node")
apromore_Event = Class(name="apromore::Event")
Work = Class(name="Work")
apromore_Message = Class(name="apromore::Message")
Event = Class(name="Event")
apromore_Time = Class(name="apromore::Time")
apromore_Task = Class(name="apromore::Task")
apromore_State = Class(name="apromore::State")
apromore_Join = Class(name="apromore::Join")
apromore_ORJoin = Class(name="apromore::ORJoin")
Join = Class(name="Join")
apromore_XORJoin = Class(name="apromore::XORJoin")
apromore_ANDJoin = Class(name="apromore::ANDJoin")

# apromore_Edge class attributes and methods
apromore_Edge_ident: Property = Property(name="ident", type=IntegerType)
apromore_Edge_condition: Property = Property(name="condition", type=StringType)
apromore_Edge_default: Property = Property(name="default", type=BooleanType)
apromore_Edge.attributes={apromore_Edge_condition, apromore_Edge_default, apromore_Edge_ident}

# apromore_CanonicalProcess class attributes and methods
apromore_CanonicalProcess_uri: Property = Property(name="uri", type=StringType)
apromore_CanonicalProcess_version: Property = Property(name="version", type=StringType)
apromore_CanonicalProcess_author: Property = Property(name="author", type=StringType)
apromore_CanonicalProcess.attributes={apromore_CanonicalProcess_version, apromore_CanonicalProcess_author, apromore_CanonicalProcess_uri}

# apromore_Net class attributes and methods
apromore_Net_ident: Property = Property(name="ident", type=IntegerType)
apromore_Net.attributes={apromore_Net_ident}

# apromore_Node class attributes and methods
apromore_Node_ident: Property = Property(name="ident", type=IntegerType)
apromore_Node_name: Property = Property(name="name", type=StringType)
apromore_Node_configurable: Property = Property(name="configurable", type=BooleanType)
apromore_Node.attributes={apromore_Node_ident, apromore_Node_configurable, apromore_Node_name}

# apromore_Routing class attributes and methods

# apromore_Split class attributes and methods

# Routing class attributes and methods

# apromore_ORSplit class attributes and methods

# Split class attributes and methods

# apromore_XORSplit class attributes and methods

# apromore_ANDSplit class attributes and methods

# apromore_Work class attributes and methods

# Node class attributes and methods

# apromore_Event class attributes and methods

# Work class attributes and methods

# apromore_Message class attributes and methods

# Event class attributes and methods

# apromore_Time class attributes and methods

# apromore_Task class attributes and methods

# apromore_State class attributes and methods

# apromore_Join class attributes and methods

# apromore_ORJoin class attributes and methods

# Join class attributes and methods

# apromore_XORJoin class attributes and methods

# apromore_ANDJoin class attributes and methods

# Relationships
edges6: BinaryAssociation = BinaryAssociation(
    name="edges6",
    ends={
        Property(name="apromore_Edge", type=apromore_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="apromore_Net7", type=apromore_Edge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="apromore_Node10", type=apromore_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="apromore_Edge9", type=apromore_Node, multiplicity=Multiplicity(0, 1))
    }
)
nets0: BinaryAssociation = BinaryAssociation(
    name="nets0",
    ends={
        Property(name="apromore_Net", type=apromore_CanonicalProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="apromore_CanonicalProcess", type=apromore_Net, multiplicity=Multiplicity(1, 9999))
    }
)
root1: BinaryAssociation = BinaryAssociation(
    name="root1",
    ends={
        Property(name="apromore_Net3", type=apromore_CanonicalProcess, multiplicity=Multiplicity(1, 1)),
        Property(name="apromore_CanonicalProcess2", type=apromore_Net, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
nodes4: BinaryAssociation = BinaryAssociation(
    name="nodes4",
    ends={
        Property(name="apromore_Node", type=apromore_Net, multiplicity=Multiplicity(1, 1)),
        Property(name="apromore_Net5", type=apromore_Node, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="apromore_Node13", type=apromore_Edge, multiplicity=Multiplicity(1, 1)),
        Property(name="apromore_Edge12", type=apromore_Node, multiplicity=Multiplicity(0, 1))
    }
)
subnet14: BinaryAssociation = BinaryAssociation(
    name="subnet14",
    ends={
        Property(name="apromore_Net15", type=apromore_Task, multiplicity=Multiplicity(1, 1)),
        Property(name="apromore_Task", type=apromore_Net, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_apromore_Routing_Node = Generalization(general=Node, specific=apromore_Routing)
gen_apromore_Split_Routing = Generalization(general=Routing, specific=apromore_Split)
gen_apromore_ORSplit_Split = Generalization(general=Split, specific=apromore_ORSplit)
gen_apromore_XORSplit_Split = Generalization(general=Split, specific=apromore_XORSplit)
gen_apromore_Work_Node = Generalization(general=Node, specific=apromore_Work)
gen_apromore_Event_Work = Generalization(general=Work, specific=apromore_Event)
gen_apromore_Message_Event = Generalization(general=Event, specific=apromore_Message)
gen_apromore_Time_Event = Generalization(general=Event, specific=apromore_Time)
gen_apromore_Task_Work = Generalization(general=Work, specific=apromore_Task)
gen_apromore_ANDSplit_Split = Generalization(general=Split, specific=apromore_ANDSplit)
gen_apromore_State_Routing = Generalization(general=Routing, specific=apromore_State)
gen_apromore_Join_Routing = Generalization(general=Routing, specific=apromore_Join)
gen_apromore_ORJoin_Join = Generalization(general=Join, specific=apromore_ORJoin)
gen_apromore_XORJoin_Join = Generalization(general=Join, specific=apromore_XORJoin)
gen_apromore_ANDJoin_Join = Generalization(general=Join, specific=apromore_ANDJoin)

# Domain Model
domain_model = DomainModel(
    name="apromore",
    types={apromore_Edge, apromore_CanonicalProcess, apromore_Net, apromore_Node, apromore_Routing, apromore_Split, Routing, apromore_ORSplit, Split, apromore_XORSplit, apromore_ANDSplit, apromore_Work, Node, apromore_Event, Work, apromore_Message, Event, apromore_Time, apromore_Task, apromore_State, apromore_Join, apromore_ORJoin, Join, apromore_XORJoin, apromore_ANDJoin},
    associations={edges6, source8, nets0, root1, nodes4, target11, subnet14},
    generalizations={gen_apromore_Routing_Node, gen_apromore_Split_Routing, gen_apromore_ORSplit_Split, gen_apromore_XORSplit_Split, gen_apromore_Work_Node, gen_apromore_Event_Work, gen_apromore_Message_Event, gen_apromore_Time_Event, gen_apromore_Task_Work, gen_apromore_ANDSplit_Split, gen_apromore_State_Routing, gen_apromore_Join_Routing, gen_apromore_ORJoin_Join, gen_apromore_XORJoin_Join, gen_apromore_ANDJoin_Join},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)