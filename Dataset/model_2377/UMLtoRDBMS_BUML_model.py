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
umltordbms_ClassToTable = Class(name="umltordbms::ClassToTable")
umltordbms_AttributeToColumn = Class(name="umltordbms::AttributeToColumn")
FromAttribute = Class(name="FromAttribute")
ToColumn = Class(name="ToColumn")
umltordbms_PrimitiveToName = Class(name="umltordbms::PrimitiveToName")
umltordbms_AssociationToForeignKey = Class(name="umltordbms::AssociationToForeignKey")
umltordbms_Table = Class(name="umltordbms::Table")
umltordbms_Key = Class(name="umltordbms::Key")
umltordbms_Association = Class(name="umltordbms::Association")
umltordbms_ForeignKey = Class(name="umltordbms::ForeignKey")
FromAttributeOwner = Class(name="FromAttributeOwner")
umltordbms_PackageToSchema = Class(name="umltordbms::PackageToSchema")
umltordbms_Class = Class(name="umltordbms::Class")
umltordbms_NonLeafAttribute = Class(name="umltordbms::NonLeafAttribute")
umltordbms_FromAttribute = Class(name="umltordbms::FromAttribute", is_abstract=True)
umltordbms_FromAttributeOwner = Class(name="umltordbms::FromAttributeOwner", is_abstract=True)
umltordbms_Attribute = Class(name="umltordbms::Attribute")
umltordbms_ToColumn = Class(name="umltordbms::ToColumn")
umltordbms_Column = Class(name="umltordbms::Column")
umltordbms_Package = Class(name="umltordbms::Package")
umltordbms_Schema = Class(name="umltordbms::Schema")
umltordbms_PrimitiveDataType = Class(name="umltordbms::PrimitiveDataType")

# umltordbms_ClassToTable class attributes and methods
umltordbms_ClassToTable_name: Property = Property(name="name", type=StringType)
umltordbms_ClassToTable.attributes={umltordbms_ClassToTable_name}

# umltordbms_AttributeToColumn class attributes and methods

# FromAttribute class attributes and methods

# ToColumn class attributes and methods

# umltordbms_PrimitiveToName class attributes and methods
umltordbms_PrimitiveToName_typeName: Property = Property(name="typeName", type=StringType)
umltordbms_PrimitiveToName_name: Property = Property(name="name", type=StringType)
umltordbms_PrimitiveToName.attributes={umltordbms_PrimitiveToName_typeName, umltordbms_PrimitiveToName_name}

# umltordbms_AssociationToForeignKey class attributes and methods
umltordbms_AssociationToForeignKey_name: Property = Property(name="name", type=StringType)
umltordbms_AssociationToForeignKey.attributes={umltordbms_AssociationToForeignKey_name}

# umltordbms_Table class attributes and methods

# umltordbms_Key class attributes and methods

# umltordbms_Association class attributes and methods

# umltordbms_ForeignKey class attributes and methods

# FromAttributeOwner class attributes and methods

# umltordbms_PackageToSchema class attributes and methods
umltordbms_PackageToSchema_name: Property = Property(name="name", type=StringType)
umltordbms_PackageToSchema.attributes={umltordbms_PackageToSchema_name}

# umltordbms_Class class attributes and methods

# umltordbms_NonLeafAttribute class attributes and methods

# umltordbms_FromAttribute class attributes and methods
umltordbms_FromAttribute_name: Property = Property(name="name", type=StringType)
umltordbms_FromAttribute_kind: Property = Property(name="kind", type=StringType)
umltordbms_FromAttribute.attributes={umltordbms_FromAttribute_kind, umltordbms_FromAttribute_name}

# umltordbms_FromAttributeOwner class attributes and methods

# umltordbms_Attribute class attributes and methods

# umltordbms_ToColumn class attributes and methods

# umltordbms_Column class attributes and methods

# umltordbms_Package class attributes and methods

# umltordbms_Schema class attributes and methods

# umltordbms_PrimitiveDataType class attributes and methods

# Relationships
referenced1: BinaryAssociation = BinaryAssociation(
    name="referenced1",
    ends={
        Property(name="umltordbms_ClassToTable", type=umltordbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_AssociationToForeignKey", type=umltordbms_ClassToTable, multiplicity=Multiplicity(0, 1))
    }
)
owner2: BinaryAssociation = BinaryAssociation(
    name="owner2",
    ends={
        Property(name="ClassToTable", type=umltordbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="associationsToForeignKeys", type=umltordbms_ClassToTable, multiplicity=Multiplicity(0, 1))
    }
)
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="umltordbms_PrimitiveToName", type=umltordbms_AttributeToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_AttributeToColumn", type=umltordbms_PrimitiveToName, multiplicity=Multiplicity(0, 1))
    }
)
umlClass9: BinaryAssociation = BinaryAssociation(
    name="umlClass9",
    ends={
        Property(name="umltordbms_Class", type=umltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_ClassToTable10", type=umltordbms_Class, multiplicity=Multiplicity(0, 1))
    }
)
table11: BinaryAssociation = BinaryAssociation(
    name="table11",
    ends={
        Property(name="umltordbms_Table", type=umltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_ClassToTable12", type=umltordbms_Table, multiplicity=Multiplicity(0, 1))
    }
)
primaryKey13: BinaryAssociation = BinaryAssociation(
    name="primaryKey13",
    ends={
        Property(name="umltordbms_Key", type=umltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_ClassToTable14", type=umltordbms_Key, multiplicity=Multiplicity(0, 1))
    }
)
association3: BinaryAssociation = BinaryAssociation(
    name="association3",
    ends={
        Property(name="umltordbms_Association", type=umltordbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_AssociationToForeignKey4", type=umltordbms_Association, multiplicity=Multiplicity(0, 1))
    }
)
foreignKey5: BinaryAssociation = BinaryAssociation(
    name="foreignKey5",
    ends={
        Property(name="umltordbms_ForeignKey", type=umltordbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_AssociationToForeignKey6", type=umltordbms_ForeignKey, multiplicity=Multiplicity(0, 1))
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="PackageToSchema", type=umltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="classesToTables", type=umltordbms_PackageToSchema, multiplicity=Multiplicity(0, 1))
    }
)
associationsToForeignKeys8: BinaryAssociation = BinaryAssociation(
    name="associationsToForeignKeys8",
    ends={
        Property(name="AssociationToForeignKey", type=umltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=umltordbms_AssociationToForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classesToTables22: BinaryAssociation = BinaryAssociation(
    name="classesToTables22",
    ends={
        Property(name="ClassToTable24", type=umltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner23", type=umltordbms_ClassToTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="FromAttributeOwner", type=umltordbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="fromAttributes", type=umltordbms_FromAttributeOwner, multiplicity=Multiplicity(0, 1))
    }
)
leafs16: BinaryAssociation = BinaryAssociation(
    name="leafs16",
    ends={
        Property(name="umltordbms_AttributeToColumn17", type=umltordbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_FromAttribute", type=umltordbms_AttributeToColumn, multiplicity=Multiplicity(0, 9999))
    }
)
attribute18: BinaryAssociation = BinaryAssociation(
    name="attribute18",
    ends={
        Property(name="umltordbms_Attribute", type=umltordbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_FromAttribute19", type=umltordbms_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
fromAttributes20: BinaryAssociation = BinaryAssociation(
    name="fromAttributes20",
    ends={
        Property(name="FromAttribute", type=umltordbms_FromAttributeOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="owner21", type=umltordbms_FromAttribute, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primitive32: BinaryAssociation = BinaryAssociation(
    name="primitive32",
    ends={
        Property(name="umltordbms_PrimitiveDataType", type=umltordbms_PrimitiveToName, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_PrimitiveToName33", type=umltordbms_PrimitiveDataType, multiplicity=Multiplicity(1, 1))
    }
)
column34: BinaryAssociation = BinaryAssociation(
    name="column34",
    ends={
        Property(name="umltordbms_Column", type=umltordbms_ToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_ToColumn", type=umltordbms_Column, multiplicity=Multiplicity(0, 1))
    }
)
primitivesToNames25: BinaryAssociation = BinaryAssociation(
    name="primitivesToNames25",
    ends={
        Property(name="PrimitiveToName", type=umltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner26", type=umltordbms_PrimitiveToName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
umlPackage27: BinaryAssociation = BinaryAssociation(
    name="umlPackage27",
    ends={
        Property(name="umltordbms_Package", type=umltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_PackageToSchema", type=umltordbms_Package, multiplicity=Multiplicity(1, 1))
    }
)
schema28: BinaryAssociation = BinaryAssociation(
    name="schema28",
    ends={
        Property(name="umltordbms_Schema", type=umltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="umltordbms_PackageToSchema29", type=umltordbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
owner30: BinaryAssociation = BinaryAssociation(
    name="owner30",
    ends={
        Property(name="PackageToSchema31", type=umltordbms_PrimitiveToName, multiplicity=Multiplicity(1, 1)),
        Property(name="primitivesToNames", type=umltordbms_PackageToSchema, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_umltordbms_AssociationToForeignKey_ToColumn = Generalization(general=ToColumn, specific=umltordbms_AssociationToForeignKey)
gen_umltordbms_AttributeToColumn_FromAttribute = Generalization(general=FromAttribute, specific=umltordbms_AttributeToColumn)
gen_umltordbms_AttributeToColumn_ToColumn = Generalization(general=ToColumn, specific=umltordbms_AttributeToColumn)
gen_umltordbms_ClassToTable_FromAttributeOwner = Generalization(general=FromAttributeOwner, specific=umltordbms_ClassToTable)
gen_umltordbms_ClassToTable_ToColumn = Generalization(general=ToColumn, specific=umltordbms_ClassToTable)
gen_umltordbms_NonLeafAttribute_FromAttributeOwner = Generalization(general=FromAttributeOwner, specific=umltordbms_NonLeafAttribute)
gen_umltordbms_NonLeafAttribute_FromAttribute = Generalization(general=FromAttribute, specific=umltordbms_NonLeafAttribute)

# Domain Model
domain_model = DomainModel(
    name="umltordbms",
    types={umltordbms_ClassToTable, umltordbms_AttributeToColumn, FromAttribute, ToColumn, umltordbms_PrimitiveToName, umltordbms_AssociationToForeignKey, umltordbms_Table, umltordbms_Key, umltordbms_Association, umltordbms_ForeignKey, FromAttributeOwner, umltordbms_PackageToSchema, umltordbms_Class, umltordbms_NonLeafAttribute, umltordbms_FromAttribute, umltordbms_FromAttributeOwner, umltordbms_Attribute, umltordbms_ToColumn, umltordbms_Column, umltordbms_Package, umltordbms_Schema, umltordbms_PrimitiveDataType},
    associations={referenced1, owner2, type0, umlClass9, table11, primaryKey13, association3, foreignKey5, owner7, associationsToForeignKeys8, classesToTables22, owner15, leafs16, attribute18, fromAttributes20, primitive32, column34, primitivesToNames25, umlPackage27, schema28, owner30},
    generalizations={gen_umltordbms_AssociationToForeignKey_ToColumn, gen_umltordbms_AttributeToColumn_FromAttribute, gen_umltordbms_AttributeToColumn_ToColumn, gen_umltordbms_ClassToTable_FromAttributeOwner, gen_umltordbms_ClassToTable_ToColumn, gen_umltordbms_NonLeafAttribute_FromAttributeOwner, gen_umltordbms_NonLeafAttribute_FromAttribute},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)