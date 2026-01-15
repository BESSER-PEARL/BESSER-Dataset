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
filetree_FileTree = Class(name="filetree::FileTree")
Container = Class(name="Container")
filetree_PathToTreeElementMap = Class(name="filetree::PathToTreeElementMap")
filetree_FileTreeElement = Class(name="filetree::FileTreeElement", is_abstract=True)
filetree_AccessRight = Class(name="filetree::AccessRight")
filetree_Directory = Class(name="filetree::Directory")
filetree_H2HFile = Class(name="filetree::H2HFile")
FileTreeElement = Class(name="FileTreeElement")
filetree_User = Class(name="filetree::User")
filetree_Container = Class(name="filetree::Container")

# filetree_FileTree class attributes and methods

# Container class attributes and methods

# filetree_PathToTreeElementMap class attributes and methods
filetree_PathToTreeElementMap_key: Property = Property(name="key", type=StringType)
filetree_PathToTreeElementMap.attributes={filetree_PathToTreeElementMap_key}

# filetree_FileTreeElement class attributes and methods
filetree_FileTreeElement_path: Property = Property(name="path", type=StringType)
filetree_FileTreeElement_name: Property = Property(name="name", type=StringType)
filetree_FileTreeElement_file: Property = Property(name="file", type=StringType)
filetree_FileTreeElement.attributes={filetree_FileTreeElement_name, filetree_FileTreeElement_file, filetree_FileTreeElement_path}

# filetree_AccessRight class attributes and methods
filetree_AccessRight_readPermission: Property = Property(name="readPermission", type=BooleanType)
filetree_AccessRight_writePermission: Property = Property(name="writePermission", type=BooleanType)
filetree_AccessRight_userId: Property = Property(name="userId", type=StringType)
filetree_AccessRight.attributes={filetree_AccessRight_writePermission, filetree_AccessRight_readPermission, filetree_AccessRight_userId}

# filetree_Directory class attributes and methods

# filetree_H2HFile class attributes and methods

# FileTreeElement class attributes and methods

# filetree_User class attributes and methods
filetree_User_userId: Property = Property(name="userId", type=StringType)
filetree_User_password: Property = Property(name="password", type=StringType)
filetree_User_pin: Property = Property(name="pin", type=StringType)
filetree_User_rootDir: Property = Property(name="rootDir", type=StringType)
filetree_User.attributes={filetree_User_rootDir, filetree_User_userId, filetree_User_pin, filetree_User_password}

# filetree_Container class attributes and methods

# Relationships
elements0: BinaryAssociation = BinaryAssociation(
    name="elements0",
    ends={
        Property(name="filetree_PathToTreeElementMap", type=filetree_FileTree, multiplicity=Multiplicity(1, 1)),
        Property(name="filetree_FileTree", type=filetree_PathToTreeElementMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
accessRights2: BinaryAssociation = BinaryAssociation(
    name="accessRights2",
    ends={
        Property(name="filetree_AccessRight", type=filetree_FileTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="filetree_FileTreeElement", type=filetree_AccessRight, multiplicity=Multiplicity(0, 9999))
    }
)
children3: BinaryAssociation = BinaryAssociation(
    name="children3",
    ends={
        Property(name="FileTreeElement", type=filetree_Container, multiplicity=Multiplicity(1, 1)),
        Property(name="parent", type=filetree_FileTreeElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="Container", type=filetree_FileTreeElement, multiplicity=Multiplicity(1, 1)),
        Property(name="children", type=filetree_Container, multiplicity=Multiplicity(0, 1))
    }
)
fileTree4: BinaryAssociation = BinaryAssociation(
    name="fileTree4",
    ends={
        Property(name="filetree_User", type=filetree_FileTree, multiplicity=Multiplicity(0, 1)),
        Property(name="filetree_FileTree5", type=filetree_User, multiplicity=Multiplicity(1, 1))
    }
)
value6: BinaryAssociation = BinaryAssociation(
    name="value6",
    ends={
        Property(name="filetree_FileTreeElement8", type=filetree_PathToTreeElementMap, multiplicity=Multiplicity(1, 1)),
        Property(name="filetree_PathToTreeElementMap7", type=filetree_FileTreeElement, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_filetree_FileTree_Container = Generalization(general=Container, specific=filetree_FileTree)
gen_filetree_Directory_Container = Generalization(general=Container, specific=filetree_Directory)
gen_filetree_H2HFile_FileTreeElement = Generalization(general=FileTreeElement, specific=filetree_H2HFile)
gen_filetree_Container_FileTreeElement = Generalization(general=FileTreeElement, specific=filetree_Container)

# Domain Model
domain_model = DomainModel(
    name="filetree",
    types={filetree_FileTree, Container, filetree_PathToTreeElementMap, filetree_FileTreeElement, filetree_AccessRight, filetree_Directory, filetree_H2HFile, FileTreeElement, filetree_User, filetree_Container},
    associations={elements0, accessRights2, children3, parent1, fileTree4, value6},
    generalizations={gen_filetree_FileTree_Container, gen_filetree_Directory_Container, gen_filetree_H2HFile_FileTreeElement, gen_filetree_Container_FileTreeElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)