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
NodeLabel = Class(name="NodeLabel")
transport_PipeStyleTransportSystem = Class(name="transport::PipeStyleTransportSystem")
transport_PipeTransportEdge = Class(name="transport::PipeTransportEdge")
transport_LoadUnloadEdge = Class(name="transport::LoadUnloadEdge")
MigrationEdge = Class(name="MigrationEdge")
transport_LoadUnloadEdgeLabel = Class(name="transport::LoadUnloadEdgeLabel")
MigrationEdgeLabel = Class(name="MigrationEdgeLabel")
DynamicLabel = Class(name="DynamicLabel")
transport_STEMTime = Class(name="transport::STEMTime")
transport_PacketStyleTransportSystem = Class(name="transport::PacketStyleTransportSystem")
TransportSystem = Class(name="TransportSystem")
transport_PacketTransportLabel = Class(name="transport::PacketTransportLabel")
transport_TransportSystem = Class(name="transport::TransportSystem", is_abstract=True)
Node = Class(name="Node")
transport_PacketTransportLabelValue = Class(name="transport::PacketTransportLabelValue")
LabelValue = Class(name="LabelValue")
transport_PacketStyleTransportSystemDecorator = Class(name="transport::PacketStyleTransportSystemDecorator")
EdgeDecorator = Class(name="EdgeDecorator")
PopulationEdge = Class(name="PopulationEdge")
transport_PipeTransportEdgeLabel = Class(name="transport::PipeTransportEdgeLabel")
EdgeLabel = Class(name="EdgeLabel")
transport_PipeTransportEdgeLabelValue = Class(name="transport::PipeTransportEdgeLabelValue")

# NodeLabel class attributes and methods

# transport_PipeStyleTransportSystem class attributes and methods
transport_PipeStyleTransportSystem_maxCapacity: Property = Property(name="maxCapacity", type=FloatType)
transport_PipeStyleTransportSystem.attributes={transport_PipeStyleTransportSystem_maxCapacity}

# transport_PipeTransportEdge class attributes and methods

# transport_LoadUnloadEdge class attributes and methods
transport_LoadUnloadEdge_loadingEdge: Property = Property(name="loadingEdge", type=BooleanType)
transport_LoadUnloadEdge.attributes={transport_LoadUnloadEdge_loadingEdge}

# MigrationEdge class attributes and methods

# transport_LoadUnloadEdgeLabel class attributes and methods
transport_LoadUnloadEdgeLabel_activatedRate: Property = Property(name="activatedRate", type=FloatType)
transport_LoadUnloadEdgeLabel.attributes={transport_LoadUnloadEdgeLabel_activatedRate}

# MigrationEdgeLabel class attributes and methods

# DynamicLabel class attributes and methods

# transport_STEMTime class attributes and methods

# transport_PacketStyleTransportSystem class attributes and methods

# TransportSystem class attributes and methods

# transport_PacketTransportLabel class attributes and methods

# transport_TransportSystem class attributes and methods

# Node class attributes and methods

# transport_PacketTransportLabelValue class attributes and methods
transport_PacketTransportLabelValue_capacity: Property = Property(name="capacity", type=FloatType)
transport_PacketTransportLabelValue.attributes={transport_PacketTransportLabelValue_capacity}

# LabelValue class attributes and methods

# transport_PacketStyleTransportSystemDecorator class attributes and methods

# EdgeDecorator class attributes and methods

# PopulationEdge class attributes and methods

# transport_PipeTransportEdgeLabel class attributes and methods

# EdgeLabel class attributes and methods

# transport_PipeTransportEdgeLabelValue class attributes and methods
transport_PipeTransportEdgeLabelValue_maxFlow: Property = Property(name="maxFlow", type=FloatType)
transport_PipeTransportEdgeLabelValue_timePeriod: Property = Property(name="timePeriod", type=StringType)
transport_PipeTransportEdgeLabelValue.attributes={transport_PipeTransportEdgeLabelValue_maxFlow, transport_PipeTransportEdgeLabelValue_timePeriod}

# Relationships
inTransportEdges10: BinaryAssociation = BinaryAssociation(
    name="inTransportEdges10",
    ends={
        Property(name="transport_PipeTransportEdge", type=transport_PipeStyleTransportSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="transport_PipeStyleTransportSystem", type=transport_PipeTransportEdge, multiplicity=Multiplicity(0, 9999))
    }
)
outTransportEdges11: BinaryAssociation = BinaryAssociation(
    name="outTransportEdges11",
    ends={
        Property(name="transport_PipeTransportEdge13", type=transport_PipeStyleTransportSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="transport_PipeStyleTransportSystem12", type=transport_PipeTransportEdge, multiplicity=Multiplicity(0, 9999))
    }
)
activationTime0: BinaryAssociation = BinaryAssociation(
    name="activationTime0",
    ends={
        Property(name="transport_STEMTime", type=transport_LoadUnloadEdgeLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="transport_LoadUnloadEdgeLabel", type=transport_STEMTime, multiplicity=Multiplicity(0, 1))
    }
)
deactivationTime1: BinaryAssociation = BinaryAssociation(
    name="deactivationTime1",
    ends={
        Property(name="transport_STEMTime3", type=transport_LoadUnloadEdgeLabel, multiplicity=Multiplicity(1, 1)),
        Property(name="transport_LoadUnloadEdgeLabel2", type=transport_STEMTime, multiplicity=Multiplicity(0, 1))
    }
)
packetTransportLabel4: BinaryAssociation = BinaryAssociation(
    name="packetTransportLabel4",
    ends={
        Property(name="transport_PacketTransportLabel", type=transport_PacketStyleTransportSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="transport_PacketStyleTransportSystem", type=transport_PacketTransportLabel, multiplicity=Multiplicity(0, 1))
    }
)
loadingEdges5: BinaryAssociation = BinaryAssociation(
    name="loadingEdges5",
    ends={
        Property(name="transport_LoadUnloadEdge", type=transport_PacketStyleTransportSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="transport_PacketStyleTransportSystem6", type=transport_LoadUnloadEdge, multiplicity=Multiplicity(0, 9999))
    }
)
unloadingEdges7: BinaryAssociation = BinaryAssociation(
    name="unloadingEdges7",
    ends={
        Property(name="transport_LoadUnloadEdge9", type=transport_PacketStyleTransportSystem, multiplicity=Multiplicity(1, 1)),
        Property(name="transport_PacketStyleTransportSystem8", type=transport_LoadUnloadEdge, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_transport_PacketTransportLabel_NodeLabel = Generalization(general=NodeLabel, specific=transport_PacketTransportLabel)
gen_transport_PipeStyleTransportSystem_TransportSystem = Generalization(general=TransportSystem, specific=transport_PipeStyleTransportSystem)
gen_transport_LoadUnloadEdge_MigrationEdge = Generalization(general=MigrationEdge, specific=transport_LoadUnloadEdge)
gen_transport_LoadUnloadEdgeLabel_MigrationEdgeLabel = Generalization(general=MigrationEdgeLabel, specific=transport_LoadUnloadEdgeLabel)
gen_transport_LoadUnloadEdgeLabel_DynamicLabel = Generalization(general=DynamicLabel, specific=transport_LoadUnloadEdgeLabel)
gen_transport_PacketStyleTransportSystem_TransportSystem = Generalization(general=TransportSystem, specific=transport_PacketStyleTransportSystem)
gen_transport_TransportSystem_Node = Generalization(general=Node, specific=transport_TransportSystem)
gen_transport_PacketTransportLabelValue_LabelValue = Generalization(general=LabelValue, specific=transport_PacketTransportLabelValue)
gen_transport_PacketStyleTransportSystemDecorator_EdgeDecorator = Generalization(general=EdgeDecorator, specific=transport_PacketStyleTransportSystemDecorator)
gen_transport_PipeTransportEdge_PopulationEdge = Generalization(general=PopulationEdge, specific=transport_PipeTransportEdge)
gen_transport_PipeTransportEdgeLabel_EdgeLabel = Generalization(general=EdgeLabel, specific=transport_PipeTransportEdgeLabel)
gen_transport_PipeTransportEdgeLabelValue_LabelValue = Generalization(general=LabelValue, specific=transport_PipeTransportEdgeLabelValue)

# Domain Model
domain_model = DomainModel(
    name="transport",
    types={NodeLabel, transport_PipeStyleTransportSystem, transport_PipeTransportEdge, transport_LoadUnloadEdge, MigrationEdge, transport_LoadUnloadEdgeLabel, MigrationEdgeLabel, DynamicLabel, transport_STEMTime, transport_PacketStyleTransportSystem, TransportSystem, transport_PacketTransportLabel, transport_TransportSystem, Node, transport_PacketTransportLabelValue, LabelValue, transport_PacketStyleTransportSystemDecorator, EdgeDecorator, PopulationEdge, transport_PipeTransportEdgeLabel, EdgeLabel, transport_PipeTransportEdgeLabelValue},
    associations={inTransportEdges10, outTransportEdges11, activationTime0, deactivationTime1, packetTransportLabel4, loadingEdges5, unloadingEdges7},
    generalizations={gen_transport_PacketTransportLabel_NodeLabel, gen_transport_PipeStyleTransportSystem_TransportSystem, gen_transport_LoadUnloadEdge_MigrationEdge, gen_transport_LoadUnloadEdgeLabel_MigrationEdgeLabel, gen_transport_LoadUnloadEdgeLabel_DynamicLabel, gen_transport_PacketStyleTransportSystem_TransportSystem, gen_transport_TransportSystem_Node, gen_transport_PacketTransportLabelValue_LabelValue, gen_transport_PacketStyleTransportSystemDecorator_EdgeDecorator, gen_transport_PipeTransportEdge_PopulationEdge, gen_transport_PipeTransportEdgeLabel_EdgeLabel, gen_transport_PipeTransportEdgeLabelValue_LabelValue},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)