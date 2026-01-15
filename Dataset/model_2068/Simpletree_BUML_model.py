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
TreeElement = Class(name="TreeElement")
Simpletree_Node = Class(name="Simpletree::Node")
Simpletree_Attribute = Class(name="Simpletree::Attribute")
Simpletree_File = Class(name="Simpletree::File")
Simpletree_Folder = Class(name="Simpletree::Folder")
Simpletree_TreeElement = Class(name="Simpletree::TreeElement", is_abstract=True)
Text = Class(name="Text")
Simpletree_Text = Class(name="Simpletree::Text")

# TreeElement class attributes and methods

# Simpletree_Node class attributes and methods
Simpletree_Node_startLineIndex: Property = Property(name="startLineIndex", type=IntegerType)
Simpletree_Node_stopIndex: Property = Property(name="stopIndex", type=IntegerType)
Simpletree_Node_stopLineIndex: Property = Property(name="stopLineIndex", type=IntegerType)
Simpletree_Node_startIndex: Property = Property(name="startIndex", type=IntegerType)
Simpletree_Node.attributes={Simpletree_Node_stopLineIndex, Simpletree_Node_stopIndex, Simpletree_Node_startIndex, Simpletree_Node_startLineIndex}

# Simpletree_Attribute class attributes and methods
Simpletree_Attribute_value: Property = Property(name="value", type=StringType)
Simpletree_Attribute.attributes={Simpletree_Attribute_value}

# Simpletree_File class attributes and methods

# Simpletree_Folder class attributes and methods

# Simpletree_TreeElement class attributes and methods
Simpletree_TreeElement_index: Property = Property(name="index", type=IntegerType)
Simpletree_TreeElement_name: Property = Property(name="name", type=StringType)
Simpletree_TreeElement.attributes={Simpletree_TreeElement_index, Simpletree_TreeElement_name}

# Text class attributes and methods

# Simpletree_Text class attributes and methods

# Relationships
node0: BinaryAssociation = BinaryAssociation(
    name="node0",
    ends={
        Property(name="Node", type=Simpletree_Attribute, multiplicity=Multiplicity(1, 1)),
        Property(name="attribute", type=Simpletree_Node, multiplicity=Multiplicity(1, 1))
    }
)
parentFolder7: BinaryAssociation = BinaryAssociation(
    name="parentFolder7",
    ends={
        Property(name="Folder8", type=Simpletree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="subFolder", type=Simpletree_Folder, multiplicity=Multiplicity(1, 1))
    }
)
folder1: BinaryAssociation = BinaryAssociation(
    name="folder1",
    ends={
        Property(name="Folder", type=Simpletree_File, multiplicity=Multiplicity(1, 1)),
        Property(name="file", type=Simpletree_Folder, multiplicity=Multiplicity(1, 1))
    }
)
rootNode2: BinaryAssociation = BinaryAssociation(
    name="rootNode2",
    ends={
        Property(name="Simpletree_TreeElement", type=Simpletree_File, multiplicity=Multiplicity(1, 1)),
        Property(name="Simpletree_File", type=Simpletree_TreeElement, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
subFolder4: BinaryAssociation = BinaryAssociation(
    name="subFolder4",
    ends={
        Property(name="Folder5", type=Simpletree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="parentFolder", type=Simpletree_Folder, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
file9: BinaryAssociation = BinaryAssociation(
    name="file9",
    ends={
        Property(name="File", type=Simpletree_Folder, multiplicity=Multiplicity(1, 1)),
        Property(name="folder", type=Simpletree_File, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
children10: BinaryAssociation = BinaryAssociation(
    name="children10",
    ends={
        Property(name="Text", type=Simpletree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="parentNode", type=Simpletree_Text, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute11: BinaryAssociation = BinaryAssociation(
    name="attribute11",
    ends={
        Property(name="Attribute", type=Simpletree_Node, multiplicity=Multiplicity(1, 1)),
        Property(name="node", type=Simpletree_Attribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNode12: BinaryAssociation = BinaryAssociation(
    name="parentNode12",
    ends={
        Property(name="Node13", type=Simpletree_Text, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=Simpletree_Node, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_Simpletree_Attribute_TreeElement = Generalization(general=TreeElement, specific=Simpletree_Attribute)
gen_Simpletree_File_TreeElement = Generalization(general=TreeElement, specific=Simpletree_File)
gen_Simpletree_Folder_TreeElement = Generalization(general=TreeElement, specific=Simpletree_Folder)
gen_Simpletree_Node_Text = Generalization(general=Text, specific=Simpletree_Node)
gen_Simpletree_Text_TreeElement = Generalization(general=TreeElement, specific=Simpletree_Text)

# Domain Model
domain_model = DomainModel(
    name="Simpletree",
    types={TreeElement, Simpletree_Node, Simpletree_Attribute, Simpletree_File, Simpletree_Folder, Simpletree_TreeElement, Text, Simpletree_Text},
    associations={node0, parentFolder7, folder1, rootNode2, subFolder4, file9, children10, attribute11, parentNode12},
    generalizations={gen_Simpletree_Attribute_TreeElement, gen_Simpletree_File_TreeElement, gen_Simpletree_Folder_TreeElement, gen_Simpletree_Node_Text, gen_Simpletree_Text_TreeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)