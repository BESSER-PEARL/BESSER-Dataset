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
cfgraph_EndVertex = Class(name="cfgraph_EndVertex")
BodyVertex = Class(name="BodyVertex")
cfgraph_StatementVertex = Class(name="cfgraph_StatementVertex", is_abstract=True)
cfgraph_ControlFlowGraph = Class(name="cfgraph_ControlFlowGraph")
cfgraph_StartVertex = Class(name="cfgraph_StartVertex")
cfgraph_ControlFlowEdge = Class(name="cfgraph_ControlFlowEdge")
cfgraph_BodyVertex = Class(name="cfgraph_BodyVertex", is_abstract=True)
cfgraph_ControlFlowVertex = Class(name="cfgraph_ControlFlowVertex", is_abstract=True)
ControlFlowVertex = Class(name="ControlFlowVertex")
cfgraph_SimpleStatementVertex = Class(name="cfgraph_SimpleStatementVertex")
StatementVertex = Class(name="StatementVertex")
cfgraph_CallVertex = Class(name="cfgraph_CallVertex")
cfgraph_BranchingVertex = Class(name="cfgraph_BranchingVertex")

# cfgraph_EndVertex class attributes and methods

# BodyVertex class attributes and methods

# cfgraph_StatementVertex class attributes and methods

# cfgraph_ControlFlowGraph class attributes and methods

# cfgraph_StartVertex class attributes and methods

# cfgraph_ControlFlowEdge class attributes and methods
cfgraph_ControlFlowEdge_backward: Property = Property(name="backward", type=BooleanType)
cfgraph_ControlFlowEdge.attributes={cfgraph_ControlFlowEdge_backward}

# cfgraph_BodyVertex class attributes and methods

# cfgraph_ControlFlowVertex class attributes and methods

# ControlFlowVertex class attributes and methods

# cfgraph_SimpleStatementVertex class attributes and methods

# StatementVertex class attributes and methods

# cfgraph_CallVertex class attributes and methods

# cfgraph_BranchingVertex class attributes and methods

# Relationships
next2: BinaryAssociation = BinaryAssociation(
    name="next2",
    ends={
        Property(name="cfgraph_ControlFlowEdge", type=cfgraph_StartVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="cfgraph_StartVertex3", type=cfgraph_ControlFlowEdge, multiplicity=Multiplicity(1, 1))
    }
)
incomingEdges4: BinaryAssociation = BinaryAssociation(
    name="incomingEdges4",
    ends={
        Property(name="ControlFlowEdge", type=cfgraph_BodyVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="end", type=cfgraph_ControlFlowEdge, multiplicity=Multiplicity(1, 9999))
    }
)
startVertices0: BinaryAssociation = BinaryAssociation(
    name="startVertices0",
    ends={
        Property(name="cfgraph_StartVertex", type=cfgraph_ControlFlowGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="cfgraph_ControlFlowGraph", type=cfgraph_StartVertex, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
end1: BinaryAssociation = BinaryAssociation(
    name="end1",
    ends={
        Property(name="BodyVertex", type=cfgraph_ControlFlowEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingEdges", type=cfgraph_BodyVertex, multiplicity=Multiplicity(1, 1))
    }
)
next5: BinaryAssociation = BinaryAssociation(
    name="next5",
    ends={
        Property(name="cfgraph_ControlFlowEdge6", type=cfgraph_StatementVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="cfgraph_StatementVertex", type=cfgraph_ControlFlowEdge, multiplicity=Multiplicity(1, 1))
    }
)
called7: BinaryAssociation = BinaryAssociation(
    name="called7",
    ends={
        Property(name="cfgraph_StartVertex8", type=cfgraph_CallVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="cfgraph_CallVertex", type=cfgraph_StartVertex, multiplicity=Multiplicity(1, 1))
    }
)
branches9: BinaryAssociation = BinaryAssociation(
    name="branches9",
    ends={
        Property(name="cfgraph_ControlFlowEdge10", type=cfgraph_BranchingVertex, multiplicity=Multiplicity(1, 1)),
        Property(name="cfgraph_BranchingVertex", type=cfgraph_ControlFlowEdge, multiplicity=Multiplicity(2, 9999))
    }
)

# Generalizations
gen_cfgraph_BodyVertex_ControlFlowVertex = Generalization(general=ControlFlowVertex, specific=cfgraph_BodyVertex)
gen_cfgraph_EndVertex_BodyVertex = Generalization(general=BodyVertex, specific=cfgraph_EndVertex)
gen_cfgraph_StatementVertex_BodyVertex = Generalization(general=BodyVertex, specific=cfgraph_StatementVertex)
gen_cfgraph_StartVertex_ControlFlowVertex = Generalization(general=ControlFlowVertex, specific=cfgraph_StartVertex)
gen_cfgraph_SimpleStatementVertex_StatementVertex = Generalization(general=StatementVertex, specific=cfgraph_SimpleStatementVertex)
gen_cfgraph_CallVertex_StatementVertex = Generalization(general=StatementVertex, specific=cfgraph_CallVertex)
gen_cfgraph_BranchingVertex_BodyVertex = Generalization(general=BodyVertex, specific=cfgraph_BranchingVertex)

# Domain Model
domain_model = DomainModel(
    name="cfgraph",
    types={cfgraph_EndVertex, BodyVertex, cfgraph_StatementVertex, cfgraph_ControlFlowGraph, cfgraph_StartVertex, cfgraph_ControlFlowEdge, cfgraph_BodyVertex, cfgraph_ControlFlowVertex, ControlFlowVertex, cfgraph_SimpleStatementVertex, StatementVertex, cfgraph_CallVertex, cfgraph_BranchingVertex},
    associations={next2, incomingEdges4, startVertices0, end1, next5, called7, branches9},
    generalizations={gen_cfgraph_BodyVertex_ControlFlowVertex, gen_cfgraph_EndVertex_BodyVertex, gen_cfgraph_StatementVertex_BodyVertex, gen_cfgraph_StartVertex_ControlFlowVertex, gen_cfgraph_SimpleStatementVertex_StatementVertex, gen_cfgraph_CallVertex_StatementVertex, gen_cfgraph_BranchingVertex_BodyVertex},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)