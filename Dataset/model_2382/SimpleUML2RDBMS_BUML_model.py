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
uml2rdbms_AttributeToColumn = Class(name="uml2rdbms::AttributeToColumn")
FromAttribute = Class(name="FromAttribute")
ToColumn = Class(name="ToColumn")
uml2rdbms_PrimitiveToName = Class(name="uml2rdbms::PrimitiveToName", is_abstract=True)
uml2rdbms_AssociationToForeignKey = Class(name="uml2rdbms::AssociationToForeignKey")
UmlToRdbmsModelElement = Class(name="UmlToRdbmsModelElement")
uml2rdbms_Association = Class(name="uml2rdbms::Association")
uml2rdbms_BooleanToBoolean = Class(name="uml2rdbms::BooleanToBoolean")
PrimitiveToName = Class(name="PrimitiveToName")
FromAttributeOwner = Class(name="FromAttributeOwner")
uml2rdbms_PackageToSchema = Class(name="uml2rdbms::PackageToSchema")
uml2rdbms_Key = Class(name="uml2rdbms::Key")
uml2rdbms_ForeignKey = Class(name="uml2rdbms::ForeignKey")
uml2rdbms_ClassToTable = Class(name="uml2rdbms::ClassToTable")
uml2rdbms_Class = Class(name="uml2rdbms::Class")
uml2rdbms_FromAttribute = Class(name="uml2rdbms::FromAttribute", is_abstract=True)
uml2rdbms_Attribute = Class(name="uml2rdbms::Attribute")
uml2rdbms_Table = Class(name="uml2rdbms::Table")
uml2rdbms_IntegerToNumber = Class(name="uml2rdbms::IntegerToNumber")
uml2rdbms_NonLeafAttribute = Class(name="uml2rdbms::NonLeafAttribute")
uml2rdbms_Schema = Class(name="uml2rdbms::Schema")
uml2rdbms_FromAttributeOwner = Class(name="uml2rdbms::FromAttributeOwner", is_abstract=True)
uml2rdbms_PrimitiveDataType = Class(name="uml2rdbms::PrimitiveDataType")
uml2rdbms_StringToVarchar = Class(name="uml2rdbms::StringToVarchar")
uml2rdbms_ToColumn = Class(name="uml2rdbms::ToColumn", is_abstract=True)
uml2rdbms_Column = Class(name="uml2rdbms::Column")
uml2rdbms_Package = Class(name="uml2rdbms::Package")
uml2rdbms_UmlToRdbmsModelElement = Class(name="uml2rdbms::UmlToRdbmsModelElement", is_abstract=True)

# uml2rdbms_AttributeToColumn class attributes and methods

# FromAttribute class attributes and methods

# ToColumn class attributes and methods

# uml2rdbms_PrimitiveToName class attributes and methods
uml2rdbms_PrimitiveToName_typeName: Property = Property(name="typeName", type=StringType)
uml2rdbms_PrimitiveToName.attributes={uml2rdbms_PrimitiveToName_typeName}

# uml2rdbms_AssociationToForeignKey class attributes and methods

# UmlToRdbmsModelElement class attributes and methods

# uml2rdbms_Association class attributes and methods

# uml2rdbms_BooleanToBoolean class attributes and methods

# PrimitiveToName class attributes and methods

# FromAttributeOwner class attributes and methods

# uml2rdbms_PackageToSchema class attributes and methods

# uml2rdbms_Key class attributes and methods

# uml2rdbms_ForeignKey class attributes and methods

# uml2rdbms_ClassToTable class attributes and methods

# uml2rdbms_Class class attributes and methods

# uml2rdbms_FromAttribute class attributes and methods
uml2rdbms_FromAttribute_kind: Property = Property(name="kind", type=StringType)
uml2rdbms_FromAttribute.attributes={uml2rdbms_FromAttribute_kind}

# uml2rdbms_Attribute class attributes and methods

# uml2rdbms_Table class attributes and methods

# uml2rdbms_IntegerToNumber class attributes and methods

# uml2rdbms_NonLeafAttribute class attributes and methods

# uml2rdbms_Schema class attributes and methods

# uml2rdbms_FromAttributeOwner class attributes and methods

# uml2rdbms_PrimitiveDataType class attributes and methods

# uml2rdbms_StringToVarchar class attributes and methods

# uml2rdbms_ToColumn class attributes and methods

# uml2rdbms_Column class attributes and methods

# uml2rdbms_Package class attributes and methods

# uml2rdbms_UmlToRdbmsModelElement class attributes and methods
uml2rdbms_UmlToRdbmsModelElement_name: Property = Property(name="name", type=StringType)
uml2rdbms_UmlToRdbmsModelElement.attributes={uml2rdbms_UmlToRdbmsModelElement_name}

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="uml2rdbms_PrimitiveToName", type=uml2rdbms_AttributeToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_AttributeToColumn", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(0, 1))
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="uml2rdbms_Association", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_AssociationToForeignKey", type=uml2rdbms_Association, multiplicity=Multiplicity(0, 1))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="associationsToForeignKeys", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ClassToTable", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1))
    }
)
referenced5: BinaryAssociation = BinaryAssociation(
    name="referenced5",
    ends={
        Property(name="uml2rdbms_ClassToTable", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_AssociationToForeignKey6", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(0, 1))
    }
)
associationsToForeignKeys7: BinaryAssociation = BinaryAssociation(
    name="associationsToForeignKeys7",
    ends={
        Property(name="AssociationToForeignKey", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner8: BinaryAssociation = BinaryAssociation(
    name="owner8",
    ends={
        Property(name="PackageToSchema", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="classesToTables", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1))
    }
)
primaryKey9: BinaryAssociation = BinaryAssociation(
    name="primaryKey9",
    ends={
        Property(name="uml2rdbms_Key", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_ClassToTable10", type=uml2rdbms_Key, multiplicity=Multiplicity(0, 1))
    }
)
foreignKey2: BinaryAssociation = BinaryAssociation(
    name="foreignKey2",
    ends={
        Property(name="uml2rdbms_ForeignKey", type=uml2rdbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_AssociationToForeignKey3", type=uml2rdbms_ForeignKey, multiplicity=Multiplicity(0, 1))
    }
)
umlClass13: BinaryAssociation = BinaryAssociation(
    name="umlClass13",
    ends={
        Property(name="uml2rdbms_Class", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_ClassToTable14", type=uml2rdbms_Class, multiplicity=Multiplicity(0, 1))
    }
)
attribute15: BinaryAssociation = BinaryAssociation(
    name="attribute15",
    ends={
        Property(name="uml2rdbms_Attribute", type=uml2rdbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_FromAttribute", type=uml2rdbms_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
table11: BinaryAssociation = BinaryAssociation(
    name="table11",
    ends={
        Property(name="uml2rdbms_Table", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_ClassToTable12", type=uml2rdbms_Table, multiplicity=Multiplicity(0, 1))
    }
)
fromAttributes20: BinaryAssociation = BinaryAssociation(
    name="fromAttributes20",
    ends={
        Property(name="FromAttribute", type=uml2rdbms_FromAttributeOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="owner21", type=uml2rdbms_FromAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
classesToTables22: BinaryAssociation = BinaryAssociation(
    name="classesToTables22",
    ends={
        Property(name="ClassToTable24", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner23", type=uml2rdbms_ClassToTable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primitivesToNames25: BinaryAssociation = BinaryAssociation(
    name="primitivesToNames25",
    ends={
        Property(name="PrimitiveToName", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner26", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema27: BinaryAssociation = BinaryAssociation(
    name="schema27",
    ends={
        Property(name="uml2rdbms_Schema", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_PackageToSchema", type=uml2rdbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
leafs16: BinaryAssociation = BinaryAssociation(
    name="leafs16",
    ends={
        Property(name="uml2rdbms_AttributeToColumn18", type=uml2rdbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_FromAttribute17", type=uml2rdbms_AttributeToColumn, multiplicity=Multiplicity(0, 9999))
    }
)
owner19: BinaryAssociation = BinaryAssociation(
    name="owner19",
    ends={
        Property(name="FromAttributeOwner", type=uml2rdbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="fromAttributes", type=uml2rdbms_FromAttributeOwner, multiplicity=Multiplicity(1, 1))
    }
)
owner30: BinaryAssociation = BinaryAssociation(
    name="owner30",
    ends={
        Property(name="PackageToSchema31", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(1, 1)),
        Property(name="primitivesToNames", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1))
    }
)
primitive32: BinaryAssociation = BinaryAssociation(
    name="primitive32",
    ends={
        Property(name="uml2rdbms_PrimitiveDataType", type=uml2rdbms_PrimitiveToName, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_PrimitiveToName33", type=uml2rdbms_PrimitiveDataType, multiplicity=Multiplicity(1, 1))
    }
)
column34: BinaryAssociation = BinaryAssociation(
    name="column34",
    ends={
        Property(name="uml2rdbms_Column", type=uml2rdbms_ToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_ToColumn", type=uml2rdbms_Column, multiplicity=Multiplicity(1, 1))
    }
)
umlPackage28: BinaryAssociation = BinaryAssociation(
    name="umlPackage28",
    ends={
        Property(name="uml2rdbms_Package", type=uml2rdbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="uml2rdbms_PackageToSchema29", type=uml2rdbms_Package, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_uml2rdbms_AttributeToColumn_FromAttribute = Generalization(general=FromAttribute, specific=uml2rdbms_AttributeToColumn)
gen_uml2rdbms_AttributeToColumn_ToColumn = Generalization(general=ToColumn, specific=uml2rdbms_AttributeToColumn)
gen_uml2rdbms_AssociationToForeignKey_ToColumn = Generalization(general=ToColumn, specific=uml2rdbms_AssociationToForeignKey)
gen_uml2rdbms_AssociationToForeignKey_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=uml2rdbms_AssociationToForeignKey)
gen_uml2rdbms_BooleanToBoolean_PrimitiveToName = Generalization(general=PrimitiveToName, specific=uml2rdbms_BooleanToBoolean)
gen_uml2rdbms_ClassToTable_FromAttributeOwner = Generalization(general=FromAttributeOwner, specific=uml2rdbms_ClassToTable)
gen_uml2rdbms_ClassToTable_ToColumn = Generalization(general=ToColumn, specific=uml2rdbms_ClassToTable)
gen_uml2rdbms_ClassToTable_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=uml2rdbms_ClassToTable)
gen_uml2rdbms_FromAttribute_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=uml2rdbms_FromAttribute)
gen_uml2rdbms_IntegerToNumber_PrimitiveToName = Generalization(general=PrimitiveToName, specific=uml2rdbms_IntegerToNumber)
gen_uml2rdbms_NonLeafAttribute_FromAttributeOwner = Generalization(general=FromAttributeOwner, specific=uml2rdbms_NonLeafAttribute)
gen_uml2rdbms_NonLeafAttribute_FromAttribute = Generalization(general=FromAttribute, specific=uml2rdbms_NonLeafAttribute)
gen_uml2rdbms_PackageToSchema_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=uml2rdbms_PackageToSchema)
gen_uml2rdbms_PrimitiveToName_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=uml2rdbms_PrimitiveToName)
gen_uml2rdbms_StringToVarchar_PrimitiveToName = Generalization(general=PrimitiveToName, specific=uml2rdbms_StringToVarchar)

# Domain Model
domain_model = DomainModel(
    name="uml2rdbms",
    types={uml2rdbms_AttributeToColumn, FromAttribute, ToColumn, uml2rdbms_PrimitiveToName, uml2rdbms_AssociationToForeignKey, UmlToRdbmsModelElement, uml2rdbms_Association, uml2rdbms_BooleanToBoolean, PrimitiveToName, FromAttributeOwner, uml2rdbms_PackageToSchema, uml2rdbms_Key, uml2rdbms_ForeignKey, uml2rdbms_ClassToTable, uml2rdbms_Class, uml2rdbms_FromAttribute, uml2rdbms_Attribute, uml2rdbms_Table, uml2rdbms_IntegerToNumber, uml2rdbms_NonLeafAttribute, uml2rdbms_Schema, uml2rdbms_FromAttributeOwner, uml2rdbms_PrimitiveDataType, uml2rdbms_StringToVarchar, uml2rdbms_ToColumn, uml2rdbms_Column, uml2rdbms_Package, uml2rdbms_UmlToRdbmsModelElement},
    associations={type0, association1, owner4, referenced5, associationsToForeignKeys7, owner8, primaryKey9, foreignKey2, umlClass13, attribute15, table11, fromAttributes20, classesToTables22, primitivesToNames25, schema27, leafs16, owner19, owner30, primitive32, column34, umlPackage28},
    generalizations={gen_uml2rdbms_AttributeToColumn_FromAttribute, gen_uml2rdbms_AttributeToColumn_ToColumn, gen_uml2rdbms_AssociationToForeignKey_ToColumn, gen_uml2rdbms_AssociationToForeignKey_UmlToRdbmsModelElement, gen_uml2rdbms_BooleanToBoolean_PrimitiveToName, gen_uml2rdbms_ClassToTable_FromAttributeOwner, gen_uml2rdbms_ClassToTable_ToColumn, gen_uml2rdbms_ClassToTable_UmlToRdbmsModelElement, gen_uml2rdbms_FromAttribute_UmlToRdbmsModelElement, gen_uml2rdbms_IntegerToNumber_PrimitiveToName, gen_uml2rdbms_NonLeafAttribute_FromAttributeOwner, gen_uml2rdbms_NonLeafAttribute_FromAttribute, gen_uml2rdbms_PackageToSchema_UmlToRdbmsModelElement, gen_uml2rdbms_PrimitiveToName_UmlToRdbmsModelElement, gen_uml2rdbms_StringToVarchar_PrimitiveToName},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)