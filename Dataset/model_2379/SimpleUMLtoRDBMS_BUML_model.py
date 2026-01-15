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
uml2rdbms_AssociationToForeignKey = Class(name="uml2rdbms::AssociationToForeignKey")
ToColumn = Class(name="ToColumn")
uml2rdbms_ClassToTable = Class(name="uml2rdbms::ClassToTable")
uml2rdbms_Association = Class(name="uml2rdbms::Association")
uml2rdbms_ForeignKey = Class(name="uml2rdbms::ForeignKey")
uml2rdbms_AttributeToColumn = Class(name="uml2rdbms::AttributeToColumn")
FromAttribute = Class(name="FromAttribute")
uml2rdbms_PrimitiveToName = Class(name="uml2rdbms::PrimitiveToName")
FromAttributeOwner = Class(name="FromAttributeOwner")
uml2rdbms_PackageToSchema = Class(name="uml2rdbms::PackageToSchema")
uml2rdbms_Class = Class(name="uml2rdbms::Class")
uml2rdbms_Table = Class(name="uml2rdbms::Table")
uml2rdbms_Key = Class(name="uml2rdbms::Key")
uml2rdbms_FromAttribute = Class(name="uml2rdbms::FromAttribute", is_abstract=True)
uml2rdbms_FromAttributeOwner = Class(name="uml2rdbms::FromAttributeOwner", is_abstract=True)
uml2rdbms_Attribute = Class(name="uml2rdbms::Attribute")
uml2rdbms_Package = Class(name="uml2rdbms::Package")
uml2rdbms_Schema = Class(name="uml2rdbms::Schema")
uml2rdbms_PrimitiveDataType = Class(name="uml2rdbms::PrimitiveDataType")
uml2rdbms_ToColumn = Class(name="uml2rdbms::ToColumn", is_abstract=True)
uml2rdbms_Column = Class(name="uml2rdbms::Column")
uml2rdbms_NonLeafAttribute = Class(name="uml2rdbms::NonLeafAttribute")

# uml2rdbms_AssociationToForeignKey class attributes and methods
uml2rdbms_AssociationToForeignKey_name: Property = Property(name="name", type=StringType)
uml2rdbms_AssociationToForeignKey.attributes={uml2rdbms_AssociationToForeignKey_name}

# ToColumn class attributes and methods

# uml2rdbms_ClassToTable class attributes and methods
uml2rdbms_ClassToTable_name: Property = Property(name="name", type=StringType)
uml2rdbms_ClassToTable.attributes={uml2rdbms_ClassToTable_name}

# uml2rdbms_Association class attributes and methods

# uml2rdbms_ForeignKey class attributes and methods

# uml2rdbms_AttributeToColumn class attributes and methods

# FromAttribute class attributes and methods

# uml2rdbms_PrimitiveToName class attributes and methods
uml2rdbms_PrimitiveToName_name: Property = Property(name="name", type=StringType)
uml2rdbms_PrimitiveToName_typeName: Property = Property(name="typeName", type=StringType)
uml2rdbms_PrimitiveToName.attributes={uml2rdbms_PrimitiveToName_name, uml2rdbms_PrimitiveToName_typeName}

# FromAttributeOwner class attributes and methods

# uml2rdbms_PackageToSchema class attributes and methods
uml2rdbms_PackageToSchema_name: Property = Property(name="name", type=StringType)
uml2rdbms_PackageToSchema.attributes={uml2rdbms_PackageToSchema_name}

# uml2rdbms_Class class attributes and methods

# uml2rdbms_Table class attributes and methods

# uml2rdbms_Key class attributes and methods

# uml2rdbms_FromAttribute class attributes and methods
uml2rdbms_FromAttribute_name: Property = Property(name="name", type=StringType)
uml2rdbms_FromAttribute_kind: Property = Property(name="kind", type=StringType)
uml2rdbms_FromAttribute.attributes={uml2rdbms_FromAttribute_kind, uml2rdbms_FromAttribute_name}

# uml2rdbms_FromAttributeOwner class attributes and methods

# uml2rdbms_Attribute class attributes and methods

# uml2rdbms_Package class attributes and methods

# uml2rdbms_Schema class attributes and methods

# uml2rdbms_PrimitiveDataType class attributes and methods

# uml2rdbms_ToColumn class attributes and methods

# uml2rdbms_Column class attributes and methods

# uml2rdbms_NonLeafAttribute class attributes and methods

# Relationships
owner1: BinaryAssociation = BinaryAssociation(
    name="owner1",
    ends={
        Property(name="associationToForeignKeys", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(0, 1)),
        Property(name="ClassToTable", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
referenced0: BinaryAssociation = BinaryAssociation(
    name="referenced0",
    ends={
        Property(name="uml2rdbms_ClassToTable", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_AssociationToForeignKey", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(0, 1))
    }
)
association2: BinaryAssociation = BinaryAssociation(
    name="association2",
    ends={
        Property(name="uml2rdbms_Association", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_AssociationToForeignKey3", type=uml2rdbms_Association, multiplicity=Multiplicity(0, 1))
    }
)
foreignKey4: BinaryAssociation = BinaryAssociation(
    name="foreignKey4",
    ends={
        Property(name="uml2rdbms_ForeignKey", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_AssociationToForeignKey5", type=uml2rdbms_ForeignKey, multiplicity=Multiplicity(0, 1))
    }
)
type6: BinaryAssociation = BinaryAssociation(
    name="type6",
    ends={
        Property(name="uml2rdbms_PrimitiveToName", type=uml2rdbms_AttributeToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_AttributeToColumn", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(0, 1))
    }
)
owner7: BinaryAssociation = BinaryAssociation(
    name="owner7",
    ends={
        Property(name="PackageToSchema", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="classesToTables", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(0, 1))
    }
)
associationToForeignKeys8: BinaryAssociation = BinaryAssociation(
    name="associationToForeignKeys8",
    ends={
        Property(name="AssociationToForeignKey", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
umlClass9: BinaryAssociation = BinaryAssociation(
    name="umlClass9",
    ends={
        Property(name="uml2rdbms_Class", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_ClassToTable10", type=uml2rdbms_Class, multiplicity=Multiplicity(0, 1))
    }
)
table11: BinaryAssociation = BinaryAssociation(
    name="table11",
    ends={
        Property(name="uml2rdbms_Table", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_ClassToTable12", type=uml2rdbms_Table, multiplicity=Multiplicity(0, 1))
    }
)
primaryKey13: BinaryAssociation = BinaryAssociation(
    name="primaryKey13",
    ends={
        Property(name="uml2rdbms_Key", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_ClassToTable14", type=uml2rdbms_Key, multiplicity=Multiplicity(0, 1))
    }
)
owner15: BinaryAssociation = BinaryAssociation(
    name="owner15",
    ends={
        Property(name="FromAttributeOwner", type=uml2rdbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="fromAttributes", type=uml2rdbms_FromAttributeOwner, multiplicity=Multiplicity(0, 1))
    }
)
leafs16: BinaryAssociation = BinaryAssociation(
    name="leafs16",
    ends={
        Property(name="uml2rdbms_AttributeToColumn17", type=uml2rdbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_FromAttribute", type=uml2rdbms_AttributeToColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
attribute18: BinaryAssociation = BinaryAssociation(
    name="attribute18",
    ends={
        Property(name="uml2rdbms_Attribute", type=uml2rdbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_FromAttribute19", type=uml2rdbms_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
fromAttributes20: BinaryAssociation = BinaryAssociation(
    name="fromAttributes20",
    ends={
        Property(name="FromAttribute", type=uml2rdbms_FromAttributeOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="owner21", type=uml2rdbms_FromAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column34: BinaryAssociation = BinaryAssociation(
    name="column34",
    ends={
        Property(name="uml2rdbms_ToColumn", type=uml2rdbms_Column, multiplicity=Multiplicity(0, 1)),
        Property(name="uml2rdbms_Column", type=uml2rdbms_ToColumn, multiplicity=Multiplicity(1, 1))
    }
)
classesToTables22: BinaryAssociation = BinaryAssociation(
    name="classesToTables22",
    ends={
        Property(name="ClassToTable24", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner23", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primitivesToNames25: BinaryAssociation = BinaryAssociation(
    name="primitivesToNames25",
    ends={
        Property(name="PrimitiveToName", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner26", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
umlPackage27: BinaryAssociation = BinaryAssociation(
    name="umlPackage27",
    ends={
        Property(name="uml2rdbms_Package", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_PackageToSchema", type=uml2rdbms_Package, multiplicity=Multiplicity(0, 1))
    }
)
schema28: BinaryAssociation = BinaryAssociation(
    name="schema28",
    ends={
        Property(name="uml2rdbms_Schema", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_PackageToSchema29", type=uml2rdbms_Schema, multiplicity=Multiplicity(0, 1))
    }
)
owner30: BinaryAssociation = BinaryAssociation(
    name="owner30",
    ends={
        Property(name="PackageToSchema31", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(1, 1)),
        Property(name="primitivesToNames", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(0, 1))
    }
)
primitive32: BinaryAssociation = BinaryAssociation(
    name="primitive32",
    ends={
        Property(name="uml2rdbms_PrimitiveDataType", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_PrimitiveToName33", type=uml2rdbms_PrimitiveDataType, multiplicity=Multiplicity(0, 1))
    }
)
type35: BinaryAssociation = BinaryAssociation(
    name="type35",
    ends={
        Property(name="uml2rdbms_PrimitiveToName36", type=uml2rdbms_NonLeafAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_NonLeafAttribute", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_uml2rdbms_AssociationToForeignKey_ToColumn = Generalization(general=ToColumn, specific=uml2rdbms_AssociationToForeignKey)
gen_uml2rdbms_AttributeToColumn_FromAttribute = Generalization(general=FromAttribute, specific=uml2rdbms_AttributeToColumn)
gen_uml2rdbms_AttributeToColumn_ToColumn = Generalization(general=ToColumn, specific=uml2rdbms_AttributeToColumn)
gen_uml2rdbms_ClassToTable_FromAttributeOwner = Generalization(general=FromAttributeOwner, specific=uml2rdbms_ClassToTable)
gen_uml2rdbms_ClassToTable_ToColumn = Generalization(general=ToColumn, specific=uml2rdbms_ClassToTable)
gen_uml2rdbms_NonLeafAttribute_FromAttributeOwner = Generalization(general=FromAttributeOwner, specific=uml2rdbms_NonLeafAttribute)
gen_uml2rdbms_NonLeafAttribute_FromAttribute = Generalization(general=FromAttribute, specific=uml2rdbms_NonLeafAttribute)

# Domain Model
domain_model = DomainModel(
    name="uml2rdbms",
    types={uml2rdbms_AssociationToForeignKey, ToColumn, uml2rdbms_ClassToTable, uml2rdbms_Association, uml2rdbms_ForeignKey, uml2rdbms_AttributeToColumn, FromAttribute, uml2rdbms_PrimitiveToName, FromAttributeOwner, uml2rdbms_PackageToSchema, uml2rdbms_Class, uml2rdbms_Table, uml2rdbms_Key, uml2rdbms_FromAttribute, uml2rdbms_FromAttributeOwner, uml2rdbms_Attribute, uml2rdbms_Package, uml2rdbms_Schema, uml2rdbms_PrimitiveDataType, uml2rdbms_ToColumn, uml2rdbms_Column, uml2rdbms_NonLeafAttribute},
    associations={owner1, referenced0, association2, foreignKey4, type6, owner7, associationToForeignKeys8, umlClass9, table11, primaryKey13, owner15, leafs16, attribute18, fromAttributes20, column34, classesToTables22, primitivesToNames25, umlPackage27, schema28, owner30, primitive32, type35},
    generalizations={gen_uml2rdbms_AssociationToForeignKey_ToColumn, gen_uml2rdbms_AttributeToColumn_FromAttribute, gen_uml2rdbms_AttributeToColumn_ToColumn, gen_uml2rdbms_ClassToTable_FromAttributeOwner, gen_uml2rdbms_ClassToTable_ToColumn, gen_uml2rdbms_NonLeafAttribute_FromAttributeOwner, gen_uml2rdbms_NonLeafAttribute_FromAttribute},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)