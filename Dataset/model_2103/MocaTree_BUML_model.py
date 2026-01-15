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
MocaTree_Node = Class(name="MocaTree::Node")
MocaTree_Attribute = Class(name="MocaTree::Attribute")
TreeElement = Class(name="TreeElement")
MocaTree_File = Class(name="MocaTree::File")
MocaTree_Folder = Class(name="MocaTree::Folder")
Text = Class(name="Text")
MocaTree_Link = Class(name="MocaTree::Link")
MocaTree_TreeElement = Class(name="MocaTree::TreeElement", is_abstract=True)
MocaTree_Text = Class(name="MocaTree::Text")

# MocaTree_Node class attributes and methods
MocaTree_Node_stopIndex: Property = Property(name="stopIndex", type=IntegerType)
MocaTree_Node_stopLineIndex: Property = Property(name="stopLineIndex", type=IntegerType)
MocaTree_Node_startIndex: Property = Property(name="startIndex", type=IntegerType)
MocaTree_Node_startLineIndex: Property = Property(name="startLineIndex", type=IntegerType)
MocaTree_Node.attributes={MocaTree_Node_startLineIndex, MocaTree_Node_stopLineIndex, MocaTree_Node_stopIndex, MocaTree_Node_startIndex}

# MocaTree_Attribute class attributes and methods
MocaTree_Attribute_value: Property = Property(name="value", type=StringType)
MocaTree_Attribute.attributes={MocaTree_Attribute_value}

# TreeElement class attributes and methods

# MocaTree_File class attributes and methods

# MocaTree_Folder class attributes and methods

# Text class attributes and methods

# MocaTree_Link class attributes and methods

# MocaTree_TreeElement class attributes and methods
MocaTree_TreeElement_index: Property = Property(name="index", type=IntegerType)
MocaTree_TreeElement_name: Property = Property(name="name", type=StringType)
MocaTree_TreeElement.attributes={MocaTree_TreeElement_name, MocaTree_TreeElement_index}

# MocaTree_Text class attributes and methods

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="Node", type=MocaTree_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=MocaTree_Node, multiplicity=Multiplicity(0, 1))
    }
)
subFolder6: BinaryAssociation = BinaryAssociation(
    name="subFolder6",
    ends={
        Property(name="Folder7", type=MocaTree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFolder", type=MocaTree_Folder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentFolder9: BinaryAssociation = BinaryAssociation(
    name="parentFolder9",
    ends={
        Property(name="Folder10", type=MocaTree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="subFolder", type=MocaTree_Folder, multiplicity=Multiplicity(1, 1))
    }
)
folder1: BinaryAssociation = BinaryAssociation(
    name="folder1",
    ends={
        Property(name="Folder", type=MocaTree_File, multiplicity=Multiplicity(1, 1)),
        Property(name="file", type=MocaTree_Folder, multiplicity=Multiplicity(1, 1))
    }
)
rootNode2: BinaryAssociation = BinaryAssociation(
    name="rootNode2",
    ends={
        Property(name="Node4", type=MocaTree_File, multiplicity=Multiplicity(1, 1)),
        Property(name="file3", type=MocaTree_Node, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
file15: BinaryAssociation = BinaryAssociation(
    name="file15",
    ends={
        Property(name="File16", type=MocaTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="rootNode", type=MocaTree_File, multiplicity=Multiplicity(0, 1))
    }
)
file11: BinaryAssociation = BinaryAssociation(
    name="file11",
    ends={
        Property(name="File", type=MocaTree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="folder", type=MocaTree_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
targets12: BinaryAssociation = BinaryAssociation(
    name="targets12",
    ends={
        Property(name="MocaTree_TreeElement", type=MocaTree_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="MocaTree_Link", type=MocaTree_TreeElement, multiplicity=Multiplicity(0, 9999))
    }
)
attribute13: BinaryAssociation = BinaryAssociation(
    name="attribute13",
    ends={
        Property(name="MocaTree_Attribute", type=MocaTree_Link, multiplicity=Multiplicity(1, 1)),
        Property(name="MocaTree_Link14", type=MocaTree_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNode19: BinaryAssociation = BinaryAssociation(
    name="parentNode19",
    ends={
        Property(name="Node20", type=MocaTree_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=MocaTree_Node, multiplicity=Multiplicity(0, 1))
    }
)
children17: BinaryAssociation = BinaryAssociation(
    name="children17",
    ends={
        Property(name="Text", type=MocaTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parentNode", type=MocaTree_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute18: BinaryAssociation = BinaryAssociation(
    name="attribute18",
    ends={
        Property(name="Attribute", type=MocaTree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=MocaTree_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
links21: BinaryAssociation = BinaryAssociation(
    name="links21",
    ends={
        Property(name="MocaTree_Link23", type=MocaTree_TreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="MocaTree_TreeElement22", type=MocaTree_Link, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_MocaTree_Attribute_TreeElement = Generalization(general=TreeElement, specific=MocaTree_Attribute)
gen_MocaTree_File_TreeElement = Generalization(general=TreeElement, specific=MocaTree_File)
gen_MocaTree_Folder_TreeElement = Generalization(general=TreeElement, specific=MocaTree_Folder)
gen_MocaTree_Node_Text = Generalization(general=Text, specific=MocaTree_Node)
gen_MocaTree_Link_TreeElement = Generalization(general=TreeElement, specific=MocaTree_Link)
gen_MocaTree_Text_TreeElement = Generalization(general=TreeElement, specific=MocaTree_Text)

# Domain Model
domain_model = DomainModel(
    name="MocaTree",
    types={MocaTree_Node, MocaTree_Attribute, TreeElement, MocaTree_File, MocaTree_Folder, Text, MocaTree_Link, MocaTree_TreeElement, MocaTree_Text},
    associations={node0, subFolder6, parentFolder9, folder1, rootNode2, file15, file11, targets12, attribute13, parentNode19, children17, attribute18, links21},
    generalizations={gen_MocaTree_Attribute_TreeElement, gen_MocaTree_File_TreeElement, gen_MocaTree_Folder_TreeElement, gen_MocaTree_Node_Text, gen_MocaTree_Link_TreeElement, gen_MocaTree_Text_TreeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)