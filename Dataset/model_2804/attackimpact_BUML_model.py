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
attackimpact_EObject = Class(name="attackimpact::EObject")
attackimpact_Node = Class(name="attackimpact::Node")
attackimpact_Vulnerability = Class(name="attackimpact::Vulnerability")
attackimpact_Propagation = Class(name="attackimpact::Propagation")
attackimpact_Model = Class(name="attackimpact::Model")

# attackimpact_EObject class attributes and methods

# attackimpact_Node class attributes and methods
attackimpact_Node_tags: Property = Property(name="tags", type=StringType)
attackimpact_Node_domains: Property = Property(name="domains", type=StringType)
attackimpact_Node_name: Property = Property(name="name", type=StringType)
attackimpact_Node_description: Property = Property(name="description", type=StringType)
attackimpact_Node.attributes={attackimpact_Node_description, attackimpact_Node_tags, attackimpact_Node_domains, attackimpact_Node_name}

# attackimpact_Vulnerability class attributes and methods
attackimpact_Vulnerability_name: Property = Property(name="name", type=StringType)
attackimpact_Vulnerability_description: Property = Property(name="description", type=StringType)
attackimpact_Vulnerability_type: Property = Property(name="type", type=StringType)
attackimpact_Vulnerability_tags: Property = Property(name="tags", type=StringType)
attackimpact_Vulnerability_severity: Property = Property(name="severity", type=IntegerType)
attackimpact_Vulnerability.attributes={attackimpact_Vulnerability_severity, attackimpact_Vulnerability_name, attackimpact_Vulnerability_tags, attackimpact_Vulnerability_type, attackimpact_Vulnerability_description}

# attackimpact_Propagation class attributes and methods
attackimpact_Propagation_tags: Property = Property(name="tags", type=StringType)
attackimpact_Propagation_type: Property = Property(name="type", type=StringType)
attackimpact_Propagation_severity: Property = Property(name="severity", type=IntegerType)
attackimpact_Propagation.attributes={attackimpact_Propagation_type, attackimpact_Propagation_severity, attackimpact_Propagation_tags}

# attackimpact_Model class attributes and methods
attackimpact_Model_name: Property = Property(name="name", type=StringType)
attackimpact_Model_description: Property = Property(name="description", type=StringType)
attackimpact_Model.attributes={attackimpact_Model_name, attackimpact_Model_description}

# Relationships
relatedObject3: BinaryAssociation = BinaryAssociation(
    name="relatedObject3",
    ends={
        Property(name="attackimpact_EObject", type=attackimpact_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="attackimpact_Node4", type=attackimpact_EObject, multiplicity=Multiplicity(0, 1))
    }
)
vulnerabilities0: BinaryAssociation = BinaryAssociation(
    name="vulnerabilities0",
    ends={
        Property(name="attackimpact_Vulnerability", type=attackimpact_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="attackimpact_Node", type=attackimpact_Vulnerability, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propagations1: BinaryAssociation = BinaryAssociation(
    name="propagations1",
    ends={
        Property(name="attackimpact_Propagation", type=attackimpact_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="attackimpact_Node2", type=attackimpact_Propagation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
propagations5: BinaryAssociation = BinaryAssociation(
    name="propagations5",
    ends={
        Property(name="attackimpact_Propagation7", type=attackimpact_Vulnerability, multiplicity=Multiplicity(1, 1)),
        Property(name="attackimpact_Vulnerability6", type=attackimpact_Propagation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
destinations8: BinaryAssociation = BinaryAssociation(
    name="destinations8",
    ends={
        Property(name="attackimpact_Node10", type=attackimpact_Propagation, multiplicity=Multiplicity(1, 1)),
        Property(name="attackimpact_Propagation9", type=attackimpact_Node, multiplicity=Multiplicity(1, 9999))
    }
)
nodes11: BinaryAssociation = BinaryAssociation(
    name="nodes11",
    ends={
        Property(name="attackimpact_Node12", type=attackimpact_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="attackimpact_Model", type=attackimpact_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="attackimpact",
    types={attackimpact_EObject, attackimpact_Node, attackimpact_Vulnerability, attackimpact_Propagation, attackimpact_Model, vulnerabilityType, propagationType},
    associations={relatedObject3, vulnerabilities0, propagations1, propagations5, destinations8, nodes11},
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