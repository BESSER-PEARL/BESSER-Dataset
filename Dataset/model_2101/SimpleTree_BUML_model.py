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
SimpleTree_Attribute = Class(name="SimpleTree::Attribute")
TreeElement = Class(name="TreeElement")
SimpleTree_Node = Class(name="SimpleTree::Node")
SimpleTree_File = Class(name="SimpleTree::File")
SimpleTree_Folder = Class(name="SimpleTree::Folder")
SimpleTree_TreeElement = Class(name="SimpleTree::TreeElement", is_abstract=True)
Text = Class(name="Text")
SimpleTree_Text = Class(name="SimpleTree::Text")

# SimpleTree_Attribute class attributes and methods
SimpleTree_Attribute_value: Property = Property(name="value", type=StringType)
SimpleTree_Attribute.attributes={SimpleTree_Attribute_value}

# TreeElement class attributes and methods

# SimpleTree_Node class attributes and methods
SimpleTree_Node_startLineIndex: Property = Property(name="startLineIndex", type=IntegerType)
SimpleTree_Node_stopIndex: Property = Property(name="stopIndex", type=IntegerType)
SimpleTree_Node_startIndex: Property = Property(name="startIndex", type=IntegerType)
SimpleTree_Node_stopLineIndex: Property = Property(name="stopLineIndex", type=IntegerType)
SimpleTree_Node.attributes={SimpleTree_Node_stopIndex, SimpleTree_Node_stopLineIndex, SimpleTree_Node_startLineIndex, SimpleTree_Node_startIndex}

# SimpleTree_File class attributes and methods

# SimpleTree_Folder class attributes and methods

# SimpleTree_TreeElement class attributes and methods
SimpleTree_TreeElement_index: Property = Property(name="index", type=IntegerType)
SimpleTree_TreeElement_name: Property = Property(name="name", type=StringType)
SimpleTree_TreeElement.attributes={SimpleTree_TreeElement_index, SimpleTree_TreeElement_name}

# Text class attributes and methods

# SimpleTree_Text class attributes and methods

# Relationships
folder1: BinaryAssociation = BinaryAssociation(
    name="folder1",
    ends={
        Property(name="Folder", type=SimpleTree_File, multiplicity=Multiplicity(1, 1)),
        Property(name="file", type=SimpleTree_Folder, multiplicity=Multiplicity(1, 1))
    }
)
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="Node", type=SimpleTree_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=SimpleTree_Node, multiplicity=Multiplicity(1, 1))
    }
)
rootNode2: BinaryAssociation = BinaryAssociation(
    name="rootNode2",
    ends={
        Property(name="SimpleTree_TreeElement", type=SimpleTree_File, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleTree_File", type=SimpleTree_TreeElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subFolder4: BinaryAssociation = BinaryAssociation(
    name="subFolder4",
    ends={
        Property(name="Folder5", type=SimpleTree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFolder", type=SimpleTree_Folder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentFolder7: BinaryAssociation = BinaryAssociation(
    name="parentFolder7",
    ends={
        Property(name="Folder8", type=SimpleTree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="subFolder", type=SimpleTree_Folder, multiplicity=Multiplicity(1, 1))
    }
)
file9: BinaryAssociation = BinaryAssociation(
    name="file9",
    ends={
        Property(name="File", type=SimpleTree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="folder", type=SimpleTree_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="Text", type=SimpleTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parentNode", type=SimpleTree_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute11: BinaryAssociation = BinaryAssociation(
    name="attribute11",
    ends={
        Property(name="Attribute", type=SimpleTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=SimpleTree_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNode12: BinaryAssociation = BinaryAssociation(
    name="parentNode12",
    ends={
        Property(name="Node13", type=SimpleTree_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=SimpleTree_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_SimpleTree_Attribute_TreeElement = Generalization(general=TreeElement, specific=SimpleTree_Attribute)
gen_SimpleTree_File_TreeElement = Generalization(general=TreeElement, specific=SimpleTree_File)
gen_SimpleTree_Folder_TreeElement = Generalization(general=TreeElement, specific=SimpleTree_Folder)
gen_SimpleTree_Node_Text = Generalization(general=Text, specific=SimpleTree_Node)
gen_SimpleTree_Text_TreeElement = Generalization(general=TreeElement, specific=SimpleTree_Text)

# Domain Model
domain_model = DomainModel(
    name="SimpleTree",
    types={SimpleTree_Attribute, TreeElement, SimpleTree_Node, SimpleTree_File, SimpleTree_Folder, SimpleTree_TreeElement, Text, SimpleTree_Text},
    associations={folder1, node0, rootNode2, subFolder4, parentFolder7, file9, children10, attribute11, parentNode12},
    generalizations={gen_SimpleTree_Attribute_TreeElement, gen_SimpleTree_File_TreeElement, gen_SimpleTree_Folder_TreeElement, gen_SimpleTree_Node_Text, gen_SimpleTree_Text_TreeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)