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
graph_Cause = Class(name="graph::Cause")
graph_Dependency = Class(name="graph::Dependency")
graph_Node = Class(name="graph::Node")
graph_DependencyGraph = Class(name="graph::DependencyGraph")
graph_DocumentRoot = Class(name="graph::DocumentRoot")
graph_EStringToStringMapEntry = Class(name="graph::EStringToStringMapEntry")
graph_DeploymentUnitType = Class(name="graph::DeploymentUnitType")

# graph_Cause class attributes and methods
graph_Cause_name: Property = Property(name="name", type=StringType)
graph_Cause_type: Property = Property(name="type", type=StringType)
graph_Cause.attributes={graph_Cause_name, graph_Cause_type}

# graph_Dependency class attributes and methods
graph_Dependency_id: Property = Property(name="id", type=StringType)
graph_Dependency_locality: Property = Property(name="locality", type=StringType)
graph_Dependency.attributes={graph_Dependency_locality, graph_Dependency_id}

# graph_Node class attributes and methods
graph_Node_id: Property = Property(name="id", type=StringType)
graph_Node.attributes={graph_Node_id}

# graph_DependencyGraph class attributes and methods

# graph_DocumentRoot class attributes and methods
graph_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
graph_DocumentRoot.attributes={graph_DocumentRoot_mixed}

# graph_EStringToStringMapEntry class attributes and methods

# graph_DeploymentUnitType class attributes and methods

# Relationships
cause0: BinaryAssociation = BinaryAssociation(
    name="cause0",
    ends={
        Property(name="graph_Dependency", type=graph_Cause, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="graph_Cause", type=graph_Dependency, multiplicity=Multiplicity(1, 1))
    }
)
destination1: BinaryAssociation = BinaryAssociation(
    name="destination1",
    ends={
        Property(name="graph_Node", type=graph_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Dependency2", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
source3: BinaryAssociation = BinaryAssociation(
    name="source3",
    ends={
        Property(name="graph_Node5", type=graph_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Dependency4", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
node6: BinaryAssociation = BinaryAssociation(
    name="node6",
    ends={
        Property(name="graph_Node7", type=graph_DependencyGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DependencyGraph", type=graph_Node, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dependency8: BinaryAssociation = BinaryAssociation(
    name="dependency8",
    ends={
        Property(name="graph_Dependency10", type=graph_DependencyGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DependencyGraph9", type=graph_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
origin11: BinaryAssociation = BinaryAssociation(
    name="origin11",
    ends={
        Property(name="graph_Node13", type=graph_DependencyGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DependencyGraph12", type=graph_Node, multiplicity=Multiplicity(0, 1))
    }
)
xMLNSPrefixMap14: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap14",
    ends={
        Property(name="graph_EStringToStringMapEntry", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot", type=graph_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation15: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation15",
    ends={
        Property(name="graph_EStringToStringMapEntry17", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot16", type=graph_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependencyGraph18: BinaryAssociation = BinaryAssociation(
    name="dependencyGraph18",
    ends={
        Property(name="graph_DependencyGraph20", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot19", type=graph_DependencyGraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
unit21: BinaryAssociation = BinaryAssociation(
    name="unit21",
    ends={
        Property(name="graph_DeploymentUnitType", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node22", type=graph_DeploymentUnitType, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
dependency23: BinaryAssociation = BinaryAssociation(
    name="dependency23",
    ends={
        Property(name="graph_Dependency25", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node24", type=graph_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Cause, graph_Dependency, graph_Node, graph_DependencyGraph, graph_DocumentRoot, graph_EStringToStringMapEntry, graph_DeploymentUnitType},
    associations={cause0, destination1, source3, node6, dependency8, origin11, xMLNSPrefixMap14, xSISchemaLocation15, dependencyGraph18, unit21, dependency23},
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