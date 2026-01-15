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
adfg_Application = Class(name="adfg::Application")
adfg_Graph = Class(name="adfg::Graph")
adfg_GraphConnection = Class(name="adfg::GraphConnection")
adfg_Actor = Class(name="adfg::Actor", is_abstract=True)
adfg_Port = Class(name="adfg::Port", is_abstract=True)
adfg_PeriodicActor = Class(name="adfg::PeriodicActor")
adfg_OutputPort = Class(name="adfg::OutputPort")
adfg_AffineRelation = Class(name="adfg::AffineRelation")
adfg_Connection = Class(name="adfg::Connection")
Actor = Class(name="Actor")
adfg_Channel = Class(name="adfg::Channel")
Connection = Class(name="Connection")
adfg_AperiodicActor = Class(name="adfg::AperiodicActor")
adfg_LossyChannel = Class(name="adfg::LossyChannel")
adfg_InputPort = Class(name="adfg::InputPort")
Port = Class(name="Port")

# adfg_Application class attributes and methods
adfg_Application_nbGraphs: Property = Property(name="nbGraphs", type=IntegerType)
adfg_Application_name: Property = Property(name="name", type=StringType)
adfg_Application_nbProcessors: Property = Property(name="nbProcessors", type=IntegerType)
adfg_Application_dynamicChecking: Property = Property(name="dynamicChecking", type=BooleanType)
adfg_Application_schedulingAlgorithm: Property = Property(name="schedulingAlgorithm", type=StringType)
adfg_Application_sourceCode: Property = Property(name="sourceCode", type=StringType)
adfg_Application.attributes={adfg_Application_dynamicChecking, adfg_Application_sourceCode, adfg_Application_nbProcessors, adfg_Application_name, adfg_Application_nbGraphs, adfg_Application_schedulingAlgorithm}

# adfg_Graph class attributes and methods
adfg_Graph_name: Property = Property(name="name", type=StringType)
adfg_Graph_nbActors: Property = Property(name="nbActors", type=IntegerType)
adfg_Graph_nbBuffers: Property = Property(name="nbBuffers", type=IntegerType)
adfg_Graph_id: Property = Property(name="id", type=IntegerType)
adfg_Graph_sourceCode: Property = Property(name="sourceCode", type=StringType)
adfg_Graph_processorUtilization: Property = Property(name="processorUtilization", type=FloatType)
adfg_Graph_bufferingRequirements: Property = Property(name="bufferingRequirements", type=IntegerType)
adfg_Graph.attributes={adfg_Graph_bufferingRequirements, adfg_Graph_nbActors, adfg_Graph_id, adfg_Graph_processorUtilization, adfg_Graph_name, adfg_Graph_sourceCode, adfg_Graph_nbBuffers}

# adfg_GraphConnection class attributes and methods

# adfg_Actor class attributes and methods
adfg_Actor_nbPorts: Property = Property(name="nbPorts", type=IntegerType)
adfg_Actor_name: Property = Property(name="name", type=StringType)
adfg_Actor_sourceCode: Property = Property(name="sourceCode", type=StringType)
adfg_Actor_priority: Property = Property(name="priority", type=IntegerType)
adfg_Actor_procNumber: Property = Property(name="procNumber", type=IntegerType)
adfg_Actor.attributes={adfg_Actor_nbPorts, adfg_Actor_name, adfg_Actor_procNumber, adfg_Actor_sourceCode, adfg_Actor_priority}

# adfg_Port class attributes and methods
adfg_Port_sequence: Property = Property(name="sequence", type=StringType)
adfg_Port_name: Property = Property(name="name", type=StringType)
adfg_Port_type: Property = Property(name="type", type=StringType)
adfg_Port.attributes={adfg_Port_type, adfg_Port_name, adfg_Port_sequence}

# adfg_PeriodicActor class attributes and methods
adfg_PeriodicActor_period: Property = Property(name="period", type=StringType)
adfg_PeriodicActor_periodUpperBound: Property = Property(name="periodUpperBound", type=StringType)
adfg_PeriodicActor_phase: Property = Property(name="phase", type=StringType)
adfg_PeriodicActor_periodLowerBound: Property = Property(name="periodLowerBound", type=StringType)
adfg_PeriodicActor_deadline: Property = Property(name="deadline", type=StringType)
adfg_PeriodicActor_wcet: Property = Property(name="wcet", type=StringType)
adfg_PeriodicActor.attributes={adfg_PeriodicActor_periodUpperBound, adfg_PeriodicActor_periodLowerBound, adfg_PeriodicActor_wcet, adfg_PeriodicActor_deadline, adfg_PeriodicActor_phase, adfg_PeriodicActor_period}

# adfg_OutputPort class attributes and methods

# adfg_AffineRelation class attributes and methods
adfg_AffineRelation_n: Property = Property(name="n", type=IntegerType)
adfg_AffineRelation_phi: Property = Property(name="phi", type=IntegerType)
adfg_AffineRelation_d: Property = Property(name="d", type=IntegerType)
adfg_AffineRelation.attributes={adfg_AffineRelation_d, adfg_AffineRelation_phi, adfg_AffineRelation_n}

# adfg_Connection class attributes and methods
adfg_Connection_size: Property = Property(name="size", type=IntegerType)
adfg_Connection_id: Property = Property(name="id", type=IntegerType)
adfg_Connection.attributes={adfg_Connection_id, adfg_Connection_size}

# Actor class attributes and methods

# adfg_Channel class attributes and methods
adfg_Channel_initial: Property = Property(name="initial", type=IntegerType)
adfg_Channel.attributes={adfg_Channel_initial}

# Connection class attributes and methods

# adfg_AperiodicActor class attributes and methods
adfg_AperiodicActor_capacity: Property = Property(name="capacity", type=StringType)
adfg_AperiodicActor_replenishmentPeriod: Property = Property(name="replenishmentPeriod", type=StringType)
adfg_AperiodicActor.attributes={adfg_AperiodicActor_replenishmentPeriod, adfg_AperiodicActor_capacity}

# adfg_LossyChannel class attributes and methods

# adfg_InputPort class attributes and methods

# Port class attributes and methods

# Relationships
graphs0: BinaryAssociation = BinaryAssociation(
    name="graphs0",
    ends={
        Property(name="Graph", type=adfg_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=adfg_Graph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
GraphConnections1: BinaryAssociation = BinaryAssociation(
    name="GraphConnections1",
    ends={
        Property(name="GraphConnection", type=adfg_Application, multiplicity=Multiplicity(1, 1)),
        Property(name="owner2", type=adfg_GraphConnection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Application", type=adfg_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graphs", type=adfg_Application, multiplicity=Multiplicity(1, 1))
    }
)
owner14: BinaryAssociation = BinaryAssociation(
    name="owner14",
    ends={
        Property(name="Application15", type=adfg_GraphConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="GraphConnections", type=adfg_Application, multiplicity=Multiplicity(1, 1))
    }
)
owner16: BinaryAssociation = BinaryAssociation(
    name="owner16",
    ends={
        Property(name="Graph17", type=adfg_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=adfg_Graph, multiplicity=Multiplicity(1, 1))
    }
)
ports18: BinaryAssociation = BinaryAssociation(
    name="ports18",
    ends={
        Property(name="Port", type=adfg_Actor, multiplicity=Multiplicity(1, 1)),
        Property(name="owner19", type=adfg_Port, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source20: BinaryAssociation = BinaryAssociation(
    name="source20",
    ends={
        Property(name="PeriodicActor", type=adfg_AffineRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="affineRelationSource", type=adfg_PeriodicActor, multiplicity=Multiplicity(1, 1))
    }
)
target21: BinaryAssociation = BinaryAssociation(
    name="target21",
    ends={
        Property(name="PeriodicActor22", type=adfg_AffineRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="affineRelationTarget", type=adfg_PeriodicActor, multiplicity=Multiplicity(1, 1))
    }
)
owner23: BinaryAssociation = BinaryAssociation(
    name="owner23",
    ends={
        Property(name="Graph24", type=adfg_AffineRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="affineRelations", type=adfg_Graph, multiplicity=Multiplicity(1, 1))
    }
)
nodes4: BinaryAssociation = BinaryAssociation(
    name="nodes4",
    ends={
        Property(name="Actor", type=adfg_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="owner5", type=adfg_Actor, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
affineRelations6: BinaryAssociation = BinaryAssociation(
    name="affineRelations6",
    ends={
        Property(name="AffineRelation", type=adfg_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="owner7", type=adfg_AffineRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
connections8: BinaryAssociation = BinaryAssociation(
    name="connections8",
    ends={
        Property(name="Connection", type=adfg_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="owner9", type=adfg_Connection, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source10: BinaryAssociation = BinaryAssociation(
    name="source10",
    ends={
        Property(name="adfg_Graph", type=adfg_GraphConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="adfg_GraphConnection", type=adfg_Graph, multiplicity=Multiplicity(1, 1))
    }
)
target11: BinaryAssociation = BinaryAssociation(
    name="target11",
    ends={
        Property(name="adfg_Graph13", type=adfg_GraphConnection, multiplicity=Multiplicity(1, 1)),
        Property(name="adfg_GraphConnection12", type=adfg_Graph, multiplicity=Multiplicity(1, 1))
    }
)
connection34: BinaryAssociation = BinaryAssociation(
    name="connection34",
    ends={
        Property(name="Connection35", type=adfg_OutputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=adfg_Connection, multiplicity=Multiplicity(0, 1))
    }
)
affineRelationSource36: BinaryAssociation = BinaryAssociation(
    name="affineRelationSource36",
    ends={
        Property(name="AffineRelation38", type=adfg_PeriodicActor, multiplicity=Multiplicity(1, 1)),
        Property(name="source37", type=adfg_AffineRelation, multiplicity=Multiplicity(0, 9999))
    }
)
affineRelationTarget39: BinaryAssociation = BinaryAssociation(
    name="affineRelationTarget39",
    ends={
        Property(name="AffineRelation41", type=adfg_PeriodicActor, multiplicity=Multiplicity(1, 1)),
        Property(name="target40", type=adfg_AffineRelation, multiplicity=Multiplicity(0, 9999))
    }
)
source25: BinaryAssociation = BinaryAssociation(
    name="source25",
    ends={
        Property(name="OutputPort", type=adfg_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection", type=adfg_OutputPort, multiplicity=Multiplicity(1, 1))
    }
)
target26: BinaryAssociation = BinaryAssociation(
    name="target26",
    ends={
        Property(name="InputPort", type=adfg_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connection27", type=adfg_InputPort, multiplicity=Multiplicity(1, 1))
    }
)
owner28: BinaryAssociation = BinaryAssociation(
    name="owner28",
    ends={
        Property(name="Graph29", type=adfg_Connection, multiplicity=Multiplicity(1, 1)),
        Property(name="connections", type=adfg_Graph, multiplicity=Multiplicity(1, 1))
    }
)
owner30: BinaryAssociation = BinaryAssociation(
    name="owner30",
    ends={
        Property(name="Actor31", type=adfg_Port, multiplicity=Multiplicity(1, 1)),
        Property(name="ports", type=adfg_Actor, multiplicity=Multiplicity(1, 1))
    }
)
connection32: BinaryAssociation = BinaryAssociation(
    name="connection32",
    ends={
        Property(name="Connection33", type=adfg_InputPort, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=adfg_Connection, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_adfg_PeriodicActor_Actor = Generalization(general=Actor, specific=adfg_PeriodicActor)
gen_adfg_Channel_Connection = Generalization(general=Connection, specific=adfg_Channel)
gen_adfg_AperiodicActor_Actor = Generalization(general=Actor, specific=adfg_AperiodicActor)
gen_adfg_LossyChannel_Connection = Generalization(general=Connection, specific=adfg_LossyChannel)
gen_adfg_InputPort_Port = Generalization(general=Port, specific=adfg_InputPort)
gen_adfg_OutputPort_Port = Generalization(general=Port, specific=adfg_OutputPort)

# Domain Model
domain_model = DomainModel(
    name="adfg",
    types={adfg_Application, adfg_Graph, adfg_GraphConnection, adfg_Actor, adfg_Port, adfg_PeriodicActor, adfg_OutputPort, adfg_AffineRelation, adfg_Connection, Actor, adfg_Channel, Connection, adfg_AperiodicActor, adfg_LossyChannel, adfg_InputPort, Port},
    associations={graphs0, GraphConnections1, owner3, owner14, owner16, ports18, source20, target21, owner23, nodes4, affineRelations6, connections8, source10, target11, connection34, affineRelationSource36, affineRelationTarget39, source25, target26, owner28, owner30, connection32},
    generalizations={gen_adfg_PeriodicActor_Actor, gen_adfg_Channel_Connection, gen_adfg_AperiodicActor_Actor, gen_adfg_LossyChannel_Connection, gen_adfg_InputPort_Port, gen_adfg_OutputPort_Port},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)