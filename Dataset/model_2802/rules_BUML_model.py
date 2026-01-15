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
rules_RulesLattice = Class(name="rules::RulesLattice")
rules_Rule = Class(name="rules::Rule")
rules_Node = Class(name="rules::Node")
rules_NodeRelation = Class(name="rules::NodeRelation")

# rules_RulesLattice class attributes and methods
rules_RulesLattice_source: Property = Property(name="source", type=StringType)
rules_RulesLattice_target: Property = Property(name="target", type=StringType)
rules_RulesLattice.attributes={rules_RulesLattice_source, rules_RulesLattice_target}

# rules_Rule class attributes and methods
rules_Rule_name: Property = Property(name="name", type=StringType)
rules_Rule.attributes={rules_Rule_name}

# rules_Node class attributes and methods
rules_Node_type: Property = Property(name="type", type=StringType)
rules_Node.attributes={rules_Node_type}

# rules_NodeRelation class attributes and methods
rules_NodeRelation_relation: Property = Property(name="relation", type=StringType)
rules_NodeRelation_lowerBound: Property = Property(name="lowerBound", type=IntegerType)
rules_NodeRelation_upperBound: Property = Property(name="upperBound", type=IntegerType)
rules_NodeRelation_relationTgt: Property = Property(name="relationTgt", type=StringType)
rules_NodeRelation.attributes={rules_NodeRelation_relationTgt, rules_NodeRelation_lowerBound, rules_NodeRelation_upperBound, rules_NodeRelation_relation}

# Relationships
rules0: BinaryAssociation = BinaryAssociation(
    name="rules0",
    ends={
        Property(name="rules_Rule", type=rules_RulesLattice, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_RulesLattice", type=rules_Rule, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children2: BinaryAssociation = BinaryAssociation(
    name="children2",
    ends={
        Property(name="Rule", type=rules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="parents", type=rules_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
parents4: BinaryAssociation = BinaryAssociation(
    name="parents4",
    ends={
        Property(name="Rule5", type=rules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=rules_Rule, multiplicity=Multiplicity(0, 9999))
    }
)
premise6: BinaryAssociation = BinaryAssociation(
    name="premise6",
    ends={
        Property(name="rules_Node", type=rules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_Rule7", type=rules_Node, multiplicity=Multiplicity(0, 9999))
    }
)
conclusion8: BinaryAssociation = BinaryAssociation(
    name="conclusion8",
    ends={
        Property(name="rules_Node10", type=rules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_Rule9", type=rules_Node, multiplicity=Multiplicity(0, 9999))
    }
)
nodes11: BinaryAssociation = BinaryAssociation(
    name="nodes11",
    ends={
        Property(name="rules_Node13", type=rules_Rule, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_Rule12", type=rules_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
relatedNodes14: BinaryAssociation = BinaryAssociation(
    name="relatedNodes14",
    ends={
        Property(name="NodeRelation", type=rules_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=rules_NodeRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
source15: BinaryAssociation = BinaryAssociation(
    name="source15",
    ends={
        Property(name="Node", type=rules_NodeRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="relatedNodes", type=rules_Node, multiplicity=Multiplicity(1, 1))
    }
)
target16: BinaryAssociation = BinaryAssociation(
    name="target16",
    ends={
        Property(name="rules_Node17", type=rules_NodeRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="rules_NodeRelation", type=rules_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="rules",
    types={rules_RulesLattice, rules_Rule, rules_Node, rules_NodeRelation},
    associations={rules0, children2, parents4, premise6, conclusion8, nodes11, relatedNodes14, source15, target16},
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