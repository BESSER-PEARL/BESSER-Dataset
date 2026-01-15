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
fsmgen_GraphContainer = Class(name="fsmgen::GraphContainer")
FSMGenElement = Class(name="FSMGenElement")
fsmgen_Graph = Class(name="fsmgen::Graph")
fsmgen_ModelComponent = Class(name="fsmgen::ModelComponent")
fsmgen_Node = Class(name="fsmgen::Node")
fsmgen_Link = Class(name="fsmgen::Link")
fsmgen_StateGraph = Class(name="fsmgen::StateGraph")
fsmgen_GraphItem = Class(name="fsmgen::GraphItem")
GraphItem = Class(name="GraphItem")
fsmgen_StateGraphNode = Class(name="fsmgen::StateGraphNode")
fsmgen_CommonTrigger = Class(name="fsmgen::CommonTrigger")
fsmgen_EObject = Class(name="fsmgen::EObject")
fsmgen_TransitionBase = Class(name="fsmgen::TransitionBase")
fsmgen_AbstractInterfaceItem = Class(name="fsmgen::AbstractInterfaceItem")
fsmgen_FSMGenElement = Class(name="fsmgen::FSMGenElement")

# fsmgen_GraphContainer class attributes and methods
fsmgen_GraphContainer_initializedTriggersInStates: Property = Property(name="initializedTriggersInStates", type=BooleanType)
fsmgen_GraphContainer_initializedChainHeads: Property = Property(name="initializedChainHeads", type=BooleanType)
fsmgen_GraphContainer_initializedCommonData: Property = Property(name="initializedCommonData", type=BooleanType)
fsmgen_GraphContainer.attributes={fsmgen_GraphContainer_initializedCommonData, fsmgen_GraphContainer_initializedChainHeads, fsmgen_GraphContainer_initializedTriggersInStates}

# FSMGenElement class attributes and methods

# fsmgen_Graph class attributes and methods
fsmgen_Graph_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
fsmgen_Graph.methods={fsmgen_Graph_m_toString}

# fsmgen_ModelComponent class attributes and methods

# fsmgen_Node class attributes and methods
fsmgen_Node_inheritanceLevel: Property = Property(name="inheritanceLevel", type=IntegerType)
fsmgen_Node_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
fsmgen_Node.attributes={fsmgen_Node_inheritanceLevel}
fsmgen_Node.methods={fsmgen_Node_m_toString}

# fsmgen_Link class attributes and methods
fsmgen_Link_ifitemTriggered: Property = Property(name="ifitemTriggered", type=BooleanType)
fsmgen_Link_m_toString: Method = Method(name="toString", parameters={}, type=StringType)
fsmgen_Link.attributes={fsmgen_Link_ifitemTriggered}
fsmgen_Link.methods={fsmgen_Link_m_toString}

# fsmgen_StateGraph class attributes and methods

# fsmgen_GraphItem class attributes and methods
fsmgen_GraphItem_inherited: Property = Property(name="inherited", type=BooleanType)
fsmgen_GraphItem.attributes={fsmgen_GraphItem_inherited}

# GraphItem class attributes and methods

# fsmgen_StateGraphNode class attributes and methods

# fsmgen_CommonTrigger class attributes and methods
fsmgen_CommonTrigger_hasGuard: Property = Property(name="hasGuard", type=BooleanType)
fsmgen_CommonTrigger_trigger: Property = Property(name="trigger", type=StringType)
fsmgen_CommonTrigger.attributes={fsmgen_CommonTrigger_trigger, fsmgen_CommonTrigger_hasGuard}

# fsmgen_EObject class attributes and methods

# fsmgen_TransitionBase class attributes and methods

# fsmgen_AbstractInterfaceItem class attributes and methods

# fsmgen_FSMGenElement class attributes and methods

# Relationships
component1: BinaryAssociation = BinaryAssociation(
    name="component1",
    ends={
        Property(name="fsmgen_ModelComponent", type=fsmgen_GraphContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_GraphContainer2", type=fsmgen_ModelComponent, multiplicity=Multiplicity(0, 1))
    }
)
nodes3: BinaryAssociation = BinaryAssociation(
    name="nodes3",
    ends={
        Property(name="Node", type=fsmgen_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=fsmgen_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links4: BinaryAssociation = BinaryAssociation(
    name="links4",
    ends={
        Property(name="Link", type=fsmgen_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph5", type=fsmgen_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
stateGraph6: BinaryAssociation = BinaryAssociation(
    name="stateGraph6",
    ends={
        Property(name="fsmgen_StateGraph", type=fsmgen_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_Graph7", type=fsmgen_StateGraph, multiplicity=Multiplicity(0, 1))
    }
)
node8: BinaryAssociation = BinaryAssociation(
    name="node8",
    ends={
        Property(name="Node9", type=fsmgen_Graph, multiplicity=Multiplicity(1, 1)),
        Property(name="subgraph", type=fsmgen_Node, multiplicity=Multiplicity(0, 1))
    }
)
graph10: BinaryAssociation = BinaryAssociation(
    name="graph10",
    ends={
        Property(name="Graph", type=fsmgen_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="nodes", type=fsmgen_Graph, multiplicity=Multiplicity(0, 1))
    }
)
subgraph11: BinaryAssociation = BinaryAssociation(
    name="subgraph11",
    ends={
        Property(name="Graph12", type=fsmgen_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=fsmgen_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
outgoing13: BinaryAssociation = BinaryAssociation(
    name="outgoing13",
    ends={
        Property(name="Link14", type=fsmgen_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=fsmgen_Link, multiplicity=Multiplicity(0, 9999))
    }
)
incoming15: BinaryAssociation = BinaryAssociation(
    name="incoming15",
    ends={
        Property(name="Link16", type=fsmgen_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=fsmgen_Link, multiplicity=Multiplicity(0, 9999))
    }
)
stateGraphNode17: BinaryAssociation = BinaryAssociation(
    name="stateGraphNode17",
    ends={
        Property(name="fsmgen_StateGraphNode", type=fsmgen_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_Node", type=fsmgen_StateGraphNode, multiplicity=Multiplicity(0, 1))
    }
)
caughtTriggers18: BinaryAssociation = BinaryAssociation(
    name="caughtTriggers18",
    ends={
        Property(name="fsmgen_CommonTrigger", type=fsmgen_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_Node19", type=fsmgen_CommonTrigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target24: BinaryAssociation = BinaryAssociation(
    name="target24",
    ends={
        Property(name="Node25", type=fsmgen_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="incoming", type=fsmgen_Node, multiplicity=Multiplicity(0, 1))
    }
)
chainHeads27: BinaryAssociation = BinaryAssociation(
    name="chainHeads27",
    ends={
        Property(name="fsmgen_Link", type=fsmgen_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_Link26", type=fsmgen_Link, multiplicity=Multiplicity(0, 9999))
    }
)
graph0: BinaryAssociation = BinaryAssociation(
    name="graph0",
    ends={
        Property(name="fsmgen_Graph", type=fsmgen_GraphContainer, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_GraphContainer", type=fsmgen_Graph, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
commonData28: BinaryAssociation = BinaryAssociation(
    name="commonData28",
    ends={
        Property(name="fsmgen_EObject", type=fsmgen_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_Link29", type=fsmgen_EObject, multiplicity=Multiplicity(0, 1))
    }
)
transition30: BinaryAssociation = BinaryAssociation(
    name="transition30",
    ends={
        Property(name="fsmgen_TransitionBase", type=fsmgen_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_Link31", type=fsmgen_TransitionBase, multiplicity=Multiplicity(0, 1))
    }
)
msg32: BinaryAssociation = BinaryAssociation(
    name="msg32",
    ends={
        Property(name="fsmgen_EObject34", type=fsmgen_CommonTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_CommonTrigger33", type=fsmgen_EObject, multiplicity=Multiplicity(0, 1))
    }
)
ifitem35: BinaryAssociation = BinaryAssociation(
    name="ifitem35",
    ends={
        Property(name="fsmgen_AbstractInterfaceItem", type=fsmgen_CommonTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_CommonTrigger36", type=fsmgen_AbstractInterfaceItem, multiplicity=Multiplicity(0, 1))
    }
)
links37: BinaryAssociation = BinaryAssociation(
    name="links37",
    ends={
        Property(name="fsmgen_Link39", type=fsmgen_CommonTrigger, multiplicity=Multiplicity(1, 1)),
        Property(name="fsmgen_CommonTrigger38", type=fsmgen_Link, multiplicity=Multiplicity(0, 9999))
    }
)
graph20: BinaryAssociation = BinaryAssociation(
    name="graph20",
    ends={
        Property(name="Graph21", type=fsmgen_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="links", type=fsmgen_Graph, multiplicity=Multiplicity(0, 1))
    }
)
source22: BinaryAssociation = BinaryAssociation(
    name="source22",
    ends={
        Property(name="Node23", type=fsmgen_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoing", type=fsmgen_Node, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_fsmgen_GraphContainer_FSMGenElement = Generalization(general=FSMGenElement, specific=fsmgen_GraphContainer)
gen_fsmgen_Graph_FSMGenElement = Generalization(general=FSMGenElement, specific=fsmgen_Graph)
gen_fsmgen_GraphItem_FSMGenElement = Generalization(general=FSMGenElement, specific=fsmgen_GraphItem)
gen_fsmgen_Node_GraphItem = Generalization(general=GraphItem, specific=fsmgen_Node)
gen_fsmgen_Link_GraphItem = Generalization(general=GraphItem, specific=fsmgen_Link)
gen_fsmgen_CommonTrigger_FSMGenElement = Generalization(general=FSMGenElement, specific=fsmgen_CommonTrigger)

# Domain Model
domain_model = DomainModel(
    name="fsmgen",
    types={fsmgen_GraphContainer, FSMGenElement, fsmgen_Graph, fsmgen_ModelComponent, fsmgen_Node, fsmgen_Link, fsmgen_StateGraph, fsmgen_GraphItem, GraphItem, fsmgen_StateGraphNode, fsmgen_CommonTrigger, fsmgen_EObject, fsmgen_TransitionBase, fsmgen_AbstractInterfaceItem, fsmgen_FSMGenElement},
    associations={component1, nodes3, links4, stateGraph6, node8, graph10, subgraph11, outgoing13, incoming15, stateGraphNode17, caughtTriggers18, target24, chainHeads27, graph0, commonData28, transition30, msg32, ifitem35, links37, graph20, source22},
    generalizations={gen_fsmgen_GraphContainer_FSMGenElement, gen_fsmgen_Graph_FSMGenElement, gen_fsmgen_GraphItem_FSMGenElement, gen_fsmgen_Node_GraphItem, gen_fsmgen_Link_GraphItem, gen_fsmgen_CommonTrigger_FSMGenElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)