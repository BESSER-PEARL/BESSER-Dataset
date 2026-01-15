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
graph_Dependency = Class(name="graph::Dependency")
graph_Node = Class(name="graph::Node")
graph_Cause = Class(name="graph::Cause")
graph_DocumentRoot = Class(name="graph::DocumentRoot")
graph_EStringToStringMapEntry = Class(name="graph::EStringToStringMapEntry")
graph_EnvironmentGraph = Class(name="graph::EnvironmentGraph")

# graph_Dependency class attributes and methods
graph_Dependency_locality: Property = Property(name="locality", type=StringType)
graph_Dependency_id: Property = Property(name="id", type=StringType)
graph_Dependency.attributes={graph_Dependency_id, graph_Dependency_locality}

# graph_Node class attributes and methods
graph_Node_containerName: Property = Property(name="containerName", type=StringType)
graph_Node_id: Property = Property(name="id", type=StringType)
graph_Node_nodeName: Property = Property(name="nodeName", type=StringType)
graph_Node_unitName: Property = Property(name="unitName", type=StringType)
graph_Node_unitVersion: Property = Property(name="unitVersion", type=StringType)
graph_Node.attributes={graph_Node_containerName, graph_Node_id, graph_Node_unitVersion, graph_Node_nodeName, graph_Node_unitName}

# graph_Cause class attributes and methods
graph_Cause_type: Property = Property(name="type", type=StringType)
graph_Cause_version: Property = Property(name="version", type=StringType)
graph_Cause_name: Property = Property(name="name", type=StringType)
graph_Cause.attributes={graph_Cause_name, graph_Cause_version, graph_Cause_type}

# graph_DocumentRoot class attributes and methods
graph_DocumentRoot_mixed: Property = Property(name="mixed", type=StringType)
graph_DocumentRoot.attributes={graph_DocumentRoot_mixed}

# graph_EStringToStringMapEntry class attributes and methods

# graph_EnvironmentGraph class attributes and methods

# Relationships
cause0: BinaryAssociation = BinaryAssociation(
    name="cause0",
    ends={
        Property(name="graph_Cause", type=graph_Dependency, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Dependency", type=graph_Cause, multiplicity=Multiplicity(0, 9999), is_composite=True)
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
xMLNSPrefixMap6: BinaryAssociation = BinaryAssociation(
    name="xMLNSPrefixMap6",
    ends={
        Property(name="graph_EStringToStringMapEntry", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot", type=graph_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cause10: BinaryAssociation = BinaryAssociation(
    name="cause10",
    ends={
        Property(name="graph_Cause12", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot11", type=graph_Cause, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
dependency13: BinaryAssociation = BinaryAssociation(
    name="dependency13",
    ends={
        Property(name="graph_Dependency15", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot14", type=graph_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
environmentGraph16: BinaryAssociation = BinaryAssociation(
    name="environmentGraph16",
    ends={
        Property(name="graph_EnvironmentGraph", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot17", type=graph_EnvironmentGraph, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
xSISchemaLocation7: BinaryAssociation = BinaryAssociation(
    name="xSISchemaLocation7",
    ends={
        Property(name="graph_EStringToStringMapEntry9", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot8", type=graph_EStringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
node21: BinaryAssociation = BinaryAssociation(
    name="node21",
    ends={
        Property(name="graph_Node23", type=graph_EnvironmentGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_EnvironmentGraph22", type=graph_Node, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
dependencies24: BinaryAssociation = BinaryAssociation(
    name="dependencies24",
    ends={
        Property(name="graph_Dependency26", type=graph_EnvironmentGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_EnvironmentGraph25", type=graph_Dependency, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
origins27: BinaryAssociation = BinaryAssociation(
    name="origins27",
    ends={
        Property(name="graph_Node29", type=graph_EnvironmentGraph, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_EnvironmentGraph28", type=graph_Node, multiplicity=Multiplicity(0, 9999))
    }
)
node18: BinaryAssociation = BinaryAssociation(
    name="node18",
    ends={
        Property(name="graph_Node20", type=graph_DocumentRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_DocumentRoot19", type=graph_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
isRequiredBy33: BinaryAssociation = BinaryAssociation(
    name="isRequiredBy33",
    ends={
        Property(name="graph_Dependency35", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node34", type=graph_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)
dependencies30: BinaryAssociation = BinaryAssociation(
    name="dependencies30",
    ends={
        Property(name="graph_Dependency32", type=graph_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="graph_Node31", type=graph_Dependency, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="graph",
    types={graph_Dependency, graph_Node, graph_Cause, graph_DocumentRoot, graph_EStringToStringMapEntry, graph_EnvironmentGraph},
    associations={cause0, destination1, source3, xMLNSPrefixMap6, cause10, dependency13, environmentGraph16, xSISchemaLocation7, node21, dependencies24, origins27, node18, isRequiredBy33, dependencies30},
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