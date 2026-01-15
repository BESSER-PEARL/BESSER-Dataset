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
TreeNodeType: Enumeration = Enumeration(
    name="TreeNodeType",
    literals={
            EnumerationLiteral(name="FOLDER"),
			EnumerationLiteral(name="FILE"),
			EnumerationLiteral(name="PROJECT"),
			EnumerationLiteral(name="UNKNOWN")
    }
)

# Classes
SemanticResourceDB_ResourceTreeNode = Class(name="SemanticResourceDB::ResourceTreeNode")
SemanticResourceDB_SemanticDB = Class(name="SemanticResourceDB::SemanticDB")
SemanticResourceDB_TreeRoot = Class(name="SemanticResourceDB::TreeRoot")
ResourceTreeNode = Class(name="ResourceTreeNode")

# SemanticResourceDB_ResourceTreeNode class attributes and methods
SemanticResourceDB_ResourceTreeNode_name: Property = Property(name="name", type=StringType)
SemanticResourceDB_ResourceTreeNode_localOnly: Property = Property(name="localOnly", type=BooleanType)
SemanticResourceDB_ResourceTreeNode_type: Property = Property(name="type", type=StringType)
SemanticResourceDB_ResourceTreeNode_sessionProperties: Property = Property(name="sessionProperties", type=StringType)
SemanticResourceDB_ResourceTreeNode_path: Property = Property(name="path", type=StringType)
SemanticResourceDB_ResourceTreeNode_queryPart: Property = Property(name="queryPart", type=StringType)
SemanticResourceDB_ResourceTreeNode_remoteURI: Property = Property(name="remoteURI", type=StringType)
SemanticResourceDB_ResourceTreeNode_dynamicContentProviderID: Property = Property(name="dynamicContentProviderID", type=StringType)
SemanticResourceDB_ResourceTreeNode_exists: Property = Property(name="exists", type=BooleanType)
SemanticResourceDB_ResourceTreeNode_templateID: Property = Property(name="templateID", type=StringType)
SemanticResourceDB_ResourceTreeNode_persistentProperties: Property = Property(name="persistentProperties", type=StringType)
SemanticResourceDB_ResourceTreeNode.attributes={SemanticResourceDB_ResourceTreeNode_path, SemanticResourceDB_ResourceTreeNode_templateID, SemanticResourceDB_ResourceTreeNode_exists, SemanticResourceDB_ResourceTreeNode_queryPart, SemanticResourceDB_ResourceTreeNode_remoteURI, SemanticResourceDB_ResourceTreeNode_dynamicContentProviderID, SemanticResourceDB_ResourceTreeNode_name, SemanticResourceDB_ResourceTreeNode_localOnly, SemanticResourceDB_ResourceTreeNode_sessionProperties, SemanticResourceDB_ResourceTreeNode_persistentProperties, SemanticResourceDB_ResourceTreeNode_type}

# SemanticResourceDB_SemanticDB class attributes and methods

# SemanticResourceDB_TreeRoot class attributes and methods
SemanticResourceDB_TreeRoot_rootURI: Property = Property(name="rootURI", type=StringType)
SemanticResourceDB_TreeRoot.attributes={SemanticResourceDB_TreeRoot_rootURI}

# ResourceTreeNode class attributes and methods

# Relationships
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="ResourceTreeNode", type=SemanticResourceDB_ResourceTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=SemanticResourceDB_ResourceTreeNode, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent3: BinaryAssociation = BinaryAssociation(
    name="parent3",
    ends={
        Property(name="ResourceTreeNode4", type=SemanticResourceDB_ResourceTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=SemanticResourceDB_ResourceTreeNode, multiplicity=Multiplicity(0, 1))
    }
)
roots5: BinaryAssociation = BinaryAssociation(
    name="roots5",
    ends={
        Property(name="TreeRoot", type=SemanticResourceDB_SemanticDB, multiplicity=Multiplicity(1, 1)),
        Property(name="parentDB", type=SemanticResourceDB_TreeRoot, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentDB6: BinaryAssociation = BinaryAssociation(
    name="parentDB6",
    ends={
        Property(name="SemanticDB", type=SemanticResourceDB_TreeRoot, multiplicity=Multiplicity(1, 1)),
        Property(name="roots", type=SemanticResourceDB_SemanticDB, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_SemanticResourceDB_TreeRoot_ResourceTreeNode = Generalization(general=ResourceTreeNode, specific=SemanticResourceDB_TreeRoot)

# Domain Model
domain_model = DomainModel(
    name="SemanticResourceDB",
    types={SemanticResourceDB_ResourceTreeNode, SemanticResourceDB_SemanticDB, SemanticResourceDB_TreeRoot, ResourceTreeNode, TreeNodeType},
    associations={children1, parent3, roots5, parentDB6},
    generalizations={gen_SemanticResourceDB_TreeRoot_ResourceTreeNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)