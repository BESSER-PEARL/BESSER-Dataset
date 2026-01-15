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
TreeElementType: Enumeration = Enumeration(
    name="TreeElementType",
    literals={
            EnumerationLiteral(name="empty"),
			EnumerationLiteral(name="yes"),
			EnumerationLiteral(name="no"),
			EnumerationLiteral(name="trusted"),
			EnumerationLiteral(name="dont_know"),
			EnumerationLiteral(name="inadmissible")
    }
)

# Classes
ed2_EDD = Class(name="ed2::EDD")
ed2_TreeObject = Class(name="ed2::TreeObject")
ed2_TreeParent = Class(name="ed2::TreeParent")
ed2_TreeElement = Class(name="ed2::TreeElement", is_abstract=True)
ed2_Node = Class(name="ed2::Node")
TreeElement = Class(name="TreeElement")
ed2_ED2 = Class(name="ed2::ED2")
ed2_Model = Class(name="ed2::Model")
ed2_Leaf = Class(name="ed2::Leaf")

# ed2_EDD class attributes and methods
ed2_EDD_name: Property = Property(name="name", type=StringType)
ed2_EDD.attributes={ed2_EDD_name}

# ed2_TreeObject class attributes and methods
ed2_TreeObject_type: Property = Property(name="type", type=StringType)
ed2_TreeObject_index: Property = Property(name="index", type=StringType)
ed2_TreeObject_name: Property = Property(name="name", type=StringType)
ed2_TreeObject.attributes={ed2_TreeObject_type, ed2_TreeObject_index, ed2_TreeObject_name}

# ed2_TreeParent class attributes and methods
ed2_TreeParent_index: Property = Property(name="index", type=StringType)
ed2_TreeParent_name: Property = Property(name="name", type=StringType)
ed2_TreeParent_type: Property = Property(name="type", type=StringType)
ed2_TreeParent.attributes={ed2_TreeParent_name, ed2_TreeParent_type, ed2_TreeParent_index}

# ed2_TreeElement class attributes and methods
ed2_TreeElement_index: Property = Property(name="index", type=StringType)
ed2_TreeElement_name: Property = Property(name="name", type=StringType)
ed2_TreeElement_type: Property = Property(name="type", type=StringType)
ed2_TreeElement.attributes={ed2_TreeElement_type, ed2_TreeElement_name, ed2_TreeElement_index}

# ed2_Node class attributes and methods

# TreeElement class attributes and methods

# ed2_ED2 class attributes and methods
ed2_ED2_name: Property = Property(name="name", type=StringType)
ed2_ED2.attributes={ed2_ED2_name}

# ed2_Model class attributes and methods

# ed2_Leaf class attributes and methods

# Relationships
treeObjects0: BinaryAssociation = BinaryAssociation(
    name="treeObjects0",
    ends={
        Property(name="ed2_TreeObject", type=ed2_EDD, multiplicity=Multiplicity(1, 1)),
        Property(name="ed2_EDD", type=ed2_TreeObject, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
treeParents1: BinaryAssociation = BinaryAssociation(
    name="treeParents1",
    ends={
        Property(name="ed2_TreeParent", type=ed2_EDD, multiplicity=Multiplicity(1, 1)),
        Property(name="ed2_EDD2", type=ed2_TreeParent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
treeElements13: BinaryAssociation = BinaryAssociation(
    name="treeElements13",
    ends={
        Property(name="ed2_TreeElement", type=ed2_ED2, multiplicity=Multiplicity(1, 1)),
        Property(name="ed2_ED2", type=ed2_TreeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
ed214: BinaryAssociation = BinaryAssociation(
    name="ed214",
    ends={
        Property(name="ed2_ED215", type=ed2_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="ed2_Model", type=ed2_ED2, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
leaves3: BinaryAssociation = BinaryAssociation(
    name="leaves3",
    ends={
        Property(name="ed2_Leaf", type=ed2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="ed2_Node", type=ed2_Leaf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
nodes5: BinaryAssociation = BinaryAssociation(
    name="nodes5",
    ends={
        Property(name="ed2_Node6", type=ed2_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="ed2_Node4", type=ed2_Node, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
treeObjects7: BinaryAssociation = BinaryAssociation(
    name="treeObjects7",
    ends={
        Property(name="ed2_TreeObject9", type=ed2_TreeParent, multiplicity=Multiplicity(1, 1)),
        Property(name="ed2_TreeParent8", type=ed2_TreeObject, multiplicity=Multiplicity(0, 9999))
    }
)
treeParents11: BinaryAssociation = BinaryAssociation(
    name="treeParents11",
    ends={
        Property(name="ed2_TreeParent12", type=ed2_TreeParent, multiplicity=Multiplicity(1, 1)),
        Property(name="ed2_TreeParent10", type=ed2_TreeParent, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ed2_Node_TreeElement = Generalization(general=TreeElement, specific=ed2_Node)
gen_ed2_Leaf_TreeElement = Generalization(general=TreeElement, specific=ed2_Leaf)

# Domain Model
domain_model = DomainModel(
    name="ed2",
    types={ed2_EDD, ed2_TreeObject, ed2_TreeParent, ed2_TreeElement, ed2_Node, TreeElement, ed2_ED2, ed2_Model, ed2_Leaf, TreeElementType},
    associations={treeObjects0, treeParents1, treeElements13, ed214, leaves3, nodes5, treeObjects7, treeParents11},
    generalizations={gen_ed2_Node_TreeElement, gen_ed2_Leaf_TreeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)