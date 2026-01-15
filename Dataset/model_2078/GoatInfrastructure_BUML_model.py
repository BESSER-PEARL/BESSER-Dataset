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
goatInfrastructure_Infrastructure = Class(name="goatInfrastructure::Infrastructure")
goatInfrastructure_SingleServer = Class(name="goatInfrastructure::SingleServer")
Infrastructure = Class(name="Infrastructure")
goatInfrastructure_Ring = Class(name="goatInfrastructure::Ring")
goatInfrastructure_Tree = Class(name="goatInfrastructure::Tree")
goatInfrastructure_TreeNode = Class(name="goatInfrastructure::TreeNode")
goatInfrastructure_Cluster = Class(name="goatInfrastructure::Cluster")

# goatInfrastructure_Infrastructure class attributes and methods
goatInfrastructure_Infrastructure_name: Property = Property(name="name", type=StringType)
goatInfrastructure_Infrastructure.attributes={goatInfrastructure_Infrastructure_name}

# goatInfrastructure_SingleServer class attributes and methods
goatInfrastructure_SingleServer_server: Property = Property(name="server", type=StringType)
goatInfrastructure_SingleServer_timeout: Property = Property(name="timeout", type=IntegerType)
goatInfrastructure_SingleServer.attributes={goatInfrastructure_SingleServer_server, goatInfrastructure_SingleServer_timeout}

# Infrastructure class attributes and methods

# goatInfrastructure_Ring class attributes and methods
goatInfrastructure_Ring_registration: Property = Property(name="registration", type=StringType)
goatInfrastructure_Ring_mid_assigner: Property = Property(name="mid_assigner", type=StringType)
goatInfrastructure_Ring_nodes: Property = Property(name="nodes", type=StringType)
goatInfrastructure_Ring.attributes={goatInfrastructure_Ring_mid_assigner, goatInfrastructure_Ring_registration, goatInfrastructure_Ring_nodes}

# goatInfrastructure_Tree class attributes and methods
goatInfrastructure_Tree_registration: Property = Property(name="registration", type=StringType)
goatInfrastructure_Tree.attributes={goatInfrastructure_Tree_registration}

# goatInfrastructure_TreeNode class attributes and methods
goatInfrastructure_TreeNode_address: Property = Property(name="address", type=StringType)
goatInfrastructure_TreeNode.attributes={goatInfrastructure_TreeNode_address}

# goatInfrastructure_Cluster class attributes and methods
goatInfrastructure_Cluster_message_queue: Property = Property(name="message_queue", type=StringType)
goatInfrastructure_Cluster_registration: Property = Property(name="registration", type=StringType)
goatInfrastructure_Cluster_mid_assigner: Property = Property(name="mid_assigner", type=StringType)
goatInfrastructure_Cluster_nodes: Property = Property(name="nodes", type=StringType)
goatInfrastructure_Cluster.attributes={goatInfrastructure_Cluster_mid_assigner, goatInfrastructure_Cluster_registration, goatInfrastructure_Cluster_message_queue, goatInfrastructure_Cluster_nodes}

# Relationships
root0: BinaryAssociation = BinaryAssociation(
    name="root0",
    ends={
        Property(name="goatInfrastructure_TreeNode", type=goatInfrastructure_Tree, multiplicity=Multiplicity(1, 1)),
        Property(name="goatInfrastructure_Tree", type=goatInfrastructure_TreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="goatInfrastructure_TreeNode3", type=goatInfrastructure_TreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="goatInfrastructure_TreeNode1", type=goatInfrastructure_TreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_goatInfrastructure_SingleServer_Infrastructure = Generalization(general=Infrastructure, specific=goatInfrastructure_SingleServer)
gen_goatInfrastructure_Ring_Infrastructure = Generalization(general=Infrastructure, specific=goatInfrastructure_Ring)
gen_goatInfrastructure_Tree_Infrastructure = Generalization(general=Infrastructure, specific=goatInfrastructure_Tree)
gen_goatInfrastructure_Cluster_Infrastructure = Generalization(general=Infrastructure, specific=goatInfrastructure_Cluster)

# Domain Model
domain_model = DomainModel(
    name="goatInfrastructure",
    types={goatInfrastructure_Infrastructure, goatInfrastructure_SingleServer, Infrastructure, goatInfrastructure_Ring, goatInfrastructure_Tree, goatInfrastructure_TreeNode, goatInfrastructure_Cluster},
    associations={root0, children2},
    generalizations={gen_goatInfrastructure_SingleServer_Infrastructure, gen_goatInfrastructure_Ring_Infrastructure, gen_goatInfrastructure_Tree_Infrastructure, gen_goatInfrastructure_Cluster_Infrastructure},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)