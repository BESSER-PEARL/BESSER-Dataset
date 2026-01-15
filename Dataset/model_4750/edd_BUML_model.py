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
edd_EDD = Class(name="edd::EDD")
edd_TreeElement = Class(name="edd::TreeElement")
edd_Node = Class(name="edd::Node")
TreeElement = Class(name="TreeElement")
edd_Leaf = Class(name="edd::Leaf")

# edd_EDD class attributes and methods
edd_EDD_name: Property = Property(name="name", type=StringType)
edd_EDD.attributes={edd_EDD_name}

# edd_TreeElement class attributes and methods
edd_TreeElement_index: Property = Property(name="index", type=StringType)
edd_TreeElement_name: Property = Property(name="name", type=StringType)
edd_TreeElement.attributes={edd_TreeElement_name, edd_TreeElement_index}

# edd_Node class attributes and methods

# TreeElement class attributes and methods

# edd_Leaf class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="edd_TreeElement", type=edd_EDD, multiplicity=Multiplicity(1, 1)),
        Property(name="edd_EDD", type=edd_TreeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children1: BinaryAssociation = BinaryAssociation(
    name="children1",
    ends={
        Property(name="edd_TreeElement2", type=edd_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="edd_Node", type=edd_TreeElement, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_edd_Node_TreeElement = Generalization(general=TreeElement, specific=edd_Node)
gen_edd_Leaf_TreeElement = Generalization(general=TreeElement, specific=edd_Leaf)

# Domain Model
domain_model = DomainModel(
    name="edd",
    types={edd_EDD, edd_TreeElement, edd_Node, TreeElement, edd_Leaf},
    associations={elements0, children1},
    generalizations={gen_edd_Node_TreeElement, gen_edd_Leaf_TreeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)