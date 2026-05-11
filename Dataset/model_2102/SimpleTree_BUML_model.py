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
SimpleTree_Attribute = Class(name="SimpleTree_Attribute")
TreeElement = Class(name="TreeElement")
SimpleTree_Node = Class(name="SimpleTree_Node")
SimpleTree_File = Class(name="SimpleTree_File")
SimpleTree_Folder = Class(name="SimpleTree_Folder")
SimpleTree_TreeElement = Class(name="SimpleTree_TreeElement", is_abstract=True)
SimpleTree_Text = Class(name="SimpleTree_Text")
Text = Class(name="Text")

# SimpleTree_Attribute class attributes and methods
SimpleTree_Attribute_value: Property = Property(name="value", type=StringType)
SimpleTree_Attribute.attributes={SimpleTree_Attribute_value}

# TreeElement class attributes and methods

# SimpleTree_Node class attributes and methods
SimpleTree_Node_startIndex: Property = Property(name="startIndex", type=IntegerType)
SimpleTree_Node_startLineIndex: Property = Property(name="startLineIndex", type=IntegerType)
SimpleTree_Node_stopIndex: Property = Property(name="stopIndex", type=IntegerType)
SimpleTree_Node_stopLineIndex: Property = Property(name="stopLineIndex", type=IntegerType)
SimpleTree_Node.attributes={SimpleTree_Node_stopIndex, SimpleTree_Node_startIndex, SimpleTree_Node_stopLineIndex, SimpleTree_Node_startLineIndex}

# SimpleTree_File class attributes and methods

# SimpleTree_Folder class attributes and methods

# SimpleTree_TreeElement class attributes and methods
SimpleTree_TreeElement_index: Property = Property(name="index", type=IntegerType)
SimpleTree_TreeElement_name: Property = Property(name="name", type=StringType)
SimpleTree_TreeElement.attributes={SimpleTree_TreeElement_name, SimpleTree_TreeElement_index}

# SimpleTree_Text class attributes and methods

# Text class attributes and methods

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="Node", type=SimpleTree_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=SimpleTree_Node, multiplicity=Multiplicity(1, 1))
    }
)
folder1: BinaryAssociation = BinaryAssociation(
    name="folder1",
    ends={
        Property(name="Folder", type=SimpleTree_File, multiplicity=Multiplicity(1, 1)),
        Property(name="file", type=SimpleTree_Folder, multiplicity=Multiplicity(1, 1))
    }
)
rootNode2: BinaryAssociation = BinaryAssociation(
    name="rootNode2",
    ends={
        Property(name="SimpleTree_TreeElement", type=SimpleTree_File, multiplicity=Multiplicity(1, 1)),
        Property(name="SimpleTree_File", type=SimpleTree_TreeElement, multiplicity=Multiplicity(1, 1), is_composite=True)
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

# Generalizations
gen_SimpleTree_Attribute_TreeElement = Generalization(general=TreeElement, specific=SimpleTree_Attribute)
gen_SimpleTree_File_TreeElement = Generalization(general=TreeElement, specific=SimpleTree_File)
gen_SimpleTree_Text_TreeElement = Generalization(general=TreeElement, specific=SimpleTree_Text)
gen_SimpleTree_Folder_TreeElement = Generalization(general=TreeElement, specific=SimpleTree_Folder)
gen_SimpleTree_Node_Text = Generalization(general=Text, specific=SimpleTree_Node)

# Domain Model
domain_model = DomainModel(
    name="SimpleTree",
    types={SimpleTree_Attribute, TreeElement, SimpleTree_Node, SimpleTree_File, SimpleTree_Folder, SimpleTree_TreeElement, SimpleTree_Text, Text},
    associations={node0, folder1, rootNode2, children10, attribute11, parentNode12, subFolder4, parentFolder7, file9},
    generalizations={gen_SimpleTree_Attribute_TreeElement, gen_SimpleTree_File_TreeElement, gen_SimpleTree_Text_TreeElement, gen_SimpleTree_Folder_TreeElement, gen_SimpleTree_Node_Text},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)