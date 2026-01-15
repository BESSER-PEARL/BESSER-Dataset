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
atomic_AGraph = Class(name="atomic::AGraph")
atomic_AToken = Class(name="atomic::AToken")
atomic_AStructured = Class(name="atomic::AStructured")
atomic_AEdge = Class(name="atomic::AEdge")
atomic_XAnnotable = Class(name="atomic::XAnnotable", is_abstract=True)
ANode = Class(name="ANode")
atomic_ANode = Class(name="atomic::ANode", is_abstract=True)
XAnnotable = Class(name="XAnnotable")
atomic_ATargetEdge = Class(name="atomic::ATargetEdge")

# atomic_AGraph class attributes and methods
atomic_AGraph_corpus: Property = Property(name="corpus", type=StringType)
atomic_AGraph.attributes={atomic_AGraph_corpus}

# atomic_AToken class attributes and methods
atomic_AToken_text: Property = Property(name="text", type=StringType)
atomic_AToken.attributes={atomic_AToken_text}

# atomic_AStructured class attributes and methods

# atomic_AEdge class attributes and methods

# atomic_XAnnotable class attributes and methods

# ANode class attributes and methods

# atomic_ANode class attributes and methods

# XAnnotable class attributes and methods

# atomic_ATargetEdge class attributes and methods

# Relationships
tokens0: BinaryAssociation = BinaryAssociation(
    name="tokens0",
    ends={
        Property(name="AToken", type=atomic_AGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph", type=atomic_AToken, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
structures1: BinaryAssociation = BinaryAssociation(
    name="structures1",
    ends={
        Property(name="AStructured", type=atomic_AGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph2", type=atomic_AStructured, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
edges3: BinaryAssociation = BinaryAssociation(
    name="edges3",
    ends={
        Property(name="AEdge", type=atomic_AGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph4", type=atomic_AEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
graph13: BinaryAssociation = BinaryAssociation(
    name="graph13",
    ends={
        Property(name="AGraph14", type=atomic_AStructured, multiplicity=Multiplicity(1, 1)),
        Property(name="structures", type=atomic_AGraph, multiplicity=Multiplicity(1, 1))
    }
)
graph15: BinaryAssociation = BinaryAssociation(
    name="graph15",
    ends={
        Property(name="AGraph16", type=atomic_AEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="edges", type=atomic_AGraph, multiplicity=Multiplicity(1, 1))
    }
)
source17: BinaryAssociation = BinaryAssociation(
    name="source17",
    ends={
        Property(name="atomic_ANode18", type=atomic_AEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="atomic_AEdge", type=atomic_ANode, multiplicity=Multiplicity(1, 1))
    }
)
target19: BinaryAssociation = BinaryAssociation(
    name="target19",
    ends={
        Property(name="atomic_ANode21", type=atomic_AEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="atomic_AEdge20", type=atomic_ANode, multiplicity=Multiplicity(1, 1))
    }
)
target22: BinaryAssociation = BinaryAssociation(
    name="target22",
    ends={
        Property(name="atomic_ANode24", type=atomic_ATargetEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="atomic_ATargetEdge23", type=atomic_ANode, multiplicity=Multiplicity(1, 1))
    }
)
graph25: BinaryAssociation = BinaryAssociation(
    name="graph25",
    ends={
        Property(name="atomic_AGraph", type=atomic_ATargetEdge, multiplicity=Multiplicity(1, 1)),
        Property(name="atomic_ATargetEdge26", type=atomic_AGraph, multiplicity=Multiplicity(1, 1))
    }
)
next6: BinaryAssociation = BinaryAssociation(
    name="next6",
    ends={
        Property(name="AToken7", type=atomic_AToken, multiplicity=Multiplicity(1, 1)),
        Property(name="previous", type=atomic_AToken, multiplicity=Multiplicity(0, 1))
    }
)
previous9: BinaryAssociation = BinaryAssociation(
    name="previous9",
    ends={
        Property(name="AToken10", type=atomic_AToken, multiplicity=Multiplicity(1, 1)),
        Property(name="next", type=atomic_AToken, multiplicity=Multiplicity(0, 1))
    }
)
graph11: BinaryAssociation = BinaryAssociation(
    name="graph11",
    ends={
        Property(name="AGraph", type=atomic_AToken, multiplicity=Multiplicity(1, 1)),
        Property(name="tokens", type=atomic_AGraph, multiplicity=Multiplicity(0, 1))
    }
)
targetedges12: BinaryAssociation = BinaryAssociation(
    name="targetedges12",
    ends={
        Property(name="atomic_ATargetEdge", type=atomic_ANode, multiplicity=Multiplicity(1, 1)),
        Property(name="atomic_ANode", type=atomic_ATargetEdge, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_atomic_AStructured_ANode = Generalization(general=ANode, specific=atomic_AStructured)
gen_atomic_AToken_ANode = Generalization(general=ANode, specific=atomic_AToken)
gen_atomic_ANode_XAnnotable = Generalization(general=XAnnotable, specific=atomic_ANode)

# Domain Model
domain_model = DomainModel(
    name="atomic",
    types={atomic_AGraph, atomic_AToken, atomic_AStructured, atomic_AEdge, atomic_XAnnotable, ANode, atomic_ANode, XAnnotable, atomic_ATargetEdge},
    associations={tokens0, structures1, edges3, graph13, graph15, source17, target19, target22, graph25, next6, previous9, graph11, targetedges12},
    generalizations={gen_atomic_AStructured_ANode, gen_atomic_AToken_ANode, gen_atomic_ANode_XAnnotable},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)