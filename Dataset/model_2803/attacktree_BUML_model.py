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
vulnerabilityType: Enumeration = Enumeration(
    name="vulnerabilityType",
    literals={
            EnumerationLiteral(name="Timing"),
			EnumerationLiteral(name="Isolation"),
			EnumerationLiteral(name="ResourceAllocation"),
			EnumerationLiteral(name="Exposure"),
			EnumerationLiteral(name="Authentication"),
			EnumerationLiteral(name="Concurrency")
    }
)

propagationType: Enumeration = Enumeration(
    name="propagationType",
    literals={
            EnumerationLiteral(name="bus"),
			EnumerationLiteral(name="dataFlow"),
			EnumerationLiteral(name="local"),
			EnumerationLiteral(name="memory"),
			EnumerationLiteral(name="processor"),
			EnumerationLiteral(name="data")
    }
)

# Classes
attacktree_Node = Class(name="attacktree::Node")
attacktree_Vulnerability = Class(name="attacktree::Vulnerability")
attacktree_EObject = Class(name="attacktree::EObject")
attacktree_Model = Class(name="attacktree::Model")

# attacktree_Node class attributes and methods
attacktree_Node_name: Property = Property(name="name", type=StringType)
attacktree_Node_description: Property = Property(name="description", type=StringType)
attacktree_Node_tags: Property = Property(name="tags", type=StringType)
attacktree_Node_domains: Property = Property(name="domains", type=StringType)
attacktree_Node.attributes={attacktree_Node_name, attacktree_Node_domains, attacktree_Node_tags, attacktree_Node_description}

# attacktree_Vulnerability class attributes and methods
attacktree_Vulnerability_name: Property = Property(name="name", type=StringType)
attacktree_Vulnerability_description: Property = Property(name="description", type=StringType)
attacktree_Vulnerability_type: Property = Property(name="type", type=StringType)
attacktree_Vulnerability_tags: Property = Property(name="tags", type=StringType)
attacktree_Vulnerability_severity: Property = Property(name="severity", type=IntegerType)
attacktree_Vulnerability.attributes={attacktree_Vulnerability_severity, attacktree_Vulnerability_description, attacktree_Vulnerability_name, attacktree_Vulnerability_tags, attacktree_Vulnerability_type}

# attacktree_EObject class attributes and methods

# attacktree_Model class attributes and methods
attacktree_Model_name: Property = Property(name="name", type=StringType)
attacktree_Model_description: Property = Property(name="description", type=StringType)
attacktree_Model.attributes={attacktree_Model_name, attacktree_Model_description}

# Relationships
vulnerabilities0: BinaryAssociation = BinaryAssociation(
    name="vulnerabilities0",
    ends={
        Property(name="attacktree_Vulnerability", type=attacktree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="attacktree_Node", type=attacktree_Vulnerability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
subNodes2: BinaryAssociation = BinaryAssociation(
    name="subNodes2",
    ends={
        Property(name="attacktree_Node3", type=attacktree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="attacktree_Node1", type=attacktree_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedObject4: BinaryAssociation = BinaryAssociation(
    name="relatedObject4",
    ends={
        Property(name="attacktree_EObject", type=attacktree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="attacktree_Node5", type=attacktree_EObject, multiplicity=Multiplicity(0, 1))
    }
)
rootNode6: BinaryAssociation = BinaryAssociation(
    name="rootNode6",
    ends={
        Property(name="attacktree_Node7", type=attacktree_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="attacktree_Model", type=attacktree_Node, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="attacktree",
    types={attacktree_Node, attacktree_Vulnerability, attacktree_EObject, attacktree_Model, vulnerabilityType, propagationType},
    associations={vulnerabilities0, subNodes2, relatedObject4, rootNode6},
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