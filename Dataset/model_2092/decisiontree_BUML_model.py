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
DecisionTree_DecisionTreeNode = Class(name="DecisionTree::DecisionTreeNode", is_abstract=True)
DecisionTree_LeafNode = Class(name="DecisionTree::LeafNode")
DecisionTreeNode = Class(name="DecisionTreeNode")
DecisionTree_StructuralVariation = Class(name="DecisionTree::StructuralVariation")
DecisionTree_IntermediateNode = Class(name="DecisionTree::IntermediateNode")
DecisionTree_PropertySpec2 = Class(name="DecisionTree::PropertySpec2")
DecisionTree_DecisionTreeForEntity = Class(name="DecisionTree::DecisionTreeForEntity")
DecisionTree_EntityType = Class(name="DecisionTree::EntityType")
DecisionTree_DecisionTrees = Class(name="DecisionTree::DecisionTrees")
DecisionTree_Property = Class(name="DecisionTree::Property")

# DecisionTree_DecisionTreeNode class attributes and methods

# DecisionTree_LeafNode class attributes and methods

# DecisionTreeNode class attributes and methods

# DecisionTree_StructuralVariation class attributes and methods

# DecisionTree_IntermediateNode class attributes and methods

# DecisionTree_PropertySpec2 class attributes and methods
DecisionTree_PropertySpec2_needsTypeCheck: Property = Property(name="needsTypeCheck", type=BooleanType)
DecisionTree_PropertySpec2.attributes={DecisionTree_PropertySpec2_needsTypeCheck}

# DecisionTree_DecisionTreeForEntity class attributes and methods

# DecisionTree_EntityType class attributes and methods

# DecisionTree_DecisionTrees class attributes and methods
DecisionTree_DecisionTrees_name: Property = Property(name="name", type=StringType)
DecisionTree_DecisionTrees.attributes={DecisionTree_DecisionTrees_name}

# DecisionTree_Property class attributes and methods

# Relationships
yesBranch1: BinaryAssociation = BinaryAssociation(
    name="yesBranch1",
    ends={
        Property(name="DecisionTree_DecisionTreeNode", type=DecisionTree_DecisionTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="DecisionTree_DecisionTreeNode0", type=DecisionTree_DecisionTreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
noBranch3: BinaryAssociation = BinaryAssociation(
    name="noBranch3",
    ends={
        Property(name="DecisionTree_DecisionTreeNode4", type=DecisionTree_DecisionTreeNode, multiplicity=Multiplicity(1, 1)),
        Property(name="DecisionTree_DecisionTreeNode2", type=DecisionTree_DecisionTreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
identifiedVariation5: BinaryAssociation = BinaryAssociation(
    name="identifiedVariation5",
    ends={
        Property(name="DecisionTree_StructuralVariation", type=DecisionTree_LeafNode, multiplicity=Multiplicity(1, 1)),
        Property(name="DecisionTree_LeafNode", type=DecisionTree_StructuralVariation, multiplicity=Multiplicity(1, 1))
    }
)
checkedProperty6: BinaryAssociation = BinaryAssociation(
    name="checkedProperty6",
    ends={
        Property(name="DecisionTree_PropertySpec2", type=DecisionTree_IntermediateNode, multiplicity=Multiplicity(1, 1)),
        Property(name="DecisionTree_IntermediateNode", type=DecisionTree_PropertySpec2, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
root7: BinaryAssociation = BinaryAssociation(
    name="root7",
    ends={
        Property(name="DecisionTree_DecisionTreeNode8", type=DecisionTree_DecisionTreeForEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="DecisionTree_DecisionTreeForEntity", type=DecisionTree_DecisionTreeNode, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
entity9: BinaryAssociation = BinaryAssociation(
    name="entity9",
    ends={
        Property(name="DecisionTree_EntityType", type=DecisionTree_DecisionTreeForEntity, multiplicity=Multiplicity(1, 1)),
        Property(name="DecisionTree_DecisionTreeForEntity10", type=DecisionTree_EntityType, multiplicity=Multiplicity(1, 1))
    }
)
trees11: BinaryAssociation = BinaryAssociation(
    name="trees11",
    ends={
        Property(name="DecisionTree_DecisionTreeForEntity12", type=DecisionTree_DecisionTrees, multiplicity=Multiplicity(1, 1)),
        Property(name="DecisionTree_DecisionTrees", type=DecisionTree_DecisionTreeForEntity, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
property13: BinaryAssociation = BinaryAssociation(
    name="property13",
    ends={
        Property(name="DecisionTree_Property", type=DecisionTree_PropertySpec2, multiplicity=Multiplicity(1, 1)),
        Property(name="DecisionTree_PropertySpec214", type=DecisionTree_Property, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_DecisionTree_LeafNode_DecisionTreeNode = Generalization(general=DecisionTreeNode, specific=DecisionTree_LeafNode)
gen_DecisionTree_IntermediateNode_DecisionTreeNode = Generalization(general=DecisionTreeNode, specific=DecisionTree_IntermediateNode)

# Domain Model
domain_model = DomainModel(
    name="DecisionTree",
    types={DecisionTree_DecisionTreeNode, DecisionTree_LeafNode, DecisionTreeNode, DecisionTree_StructuralVariation, DecisionTree_IntermediateNode, DecisionTree_PropertySpec2, DecisionTree_DecisionTreeForEntity, DecisionTree_EntityType, DecisionTree_DecisionTrees, DecisionTree_Property},
    associations={yesBranch1, noBranch3, identifiedVariation5, checkedProperty6, root7, entity9, trees11, property13},
    generalizations={gen_DecisionTree_LeafNode_DecisionTreeNode, gen_DecisionTree_IntermediateNode_DecisionTreeNode},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)