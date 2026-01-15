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
simpleumltordbms_AttributeToColumn = Class(name="simpleumltordbms::AttributeToColumn")
FromAttribute = Class(name="FromAttribute")
ToColumn = Class(name="ToColumn")
simpleumltordbms_PrimitiveToName = Class(name="simpleumltordbms::PrimitiveToName", is_abstract=True)
simpleumltordbms_Key = Class(name="simpleumltordbms::Key")
simpleumltordbms_Table = Class(name="simpleumltordbms::Table")
simpleumltordbms_Class = Class(name="simpleumltordbms::Class")
simpleumltordbms_AssociationToForeignKey = Class(name="simpleumltordbms::AssociationToForeignKey")
UmlToRdbmsModelElement = Class(name="UmlToRdbmsModelElement")
simpleumltordbms_Association = Class(name="simpleumltordbms::Association")
simpleumltordbms_ForeignKey = Class(name="simpleumltordbms::ForeignKey")
simpleumltordbms_ClassToTable = Class(name="simpleumltordbms::ClassToTable")
simpleumltordbms_BooleanToBoolean = Class(name="simpleumltordbms::BooleanToBoolean")
PrimitiveToName = Class(name="PrimitiveToName")
FromAttributeOwner = Class(name="FromAttributeOwner")
simpleumltordbms_PackageToSchema = Class(name="simpleumltordbms::PackageToSchema")
simpleumltordbms_FromAttribute = Class(name="simpleumltordbms::FromAttribute", is_abstract=True)
simpleumltordbms_Attribute = Class(name="simpleumltordbms::Attribute")
simpleumltordbms_IntegerToNumber = Class(name="simpleumltordbms::IntegerToNumber")
simpleumltordbms_NonLeafAttribute = Class(name="simpleumltordbms::NonLeafAttribute")
simpleumltordbms_FromAttributeOwner = Class(name="simpleumltordbms::FromAttributeOwner", is_abstract=True)
simpleumltordbms_Schema = Class(name="simpleumltordbms::Schema")
simpleumltordbms_PrimitiveDataType = Class(name="simpleumltordbms::PrimitiveDataType")
simpleumltordbms_StringToVarchar = Class(name="simpleumltordbms::StringToVarchar")
simpleumltordbms_ToColumn = Class(name="simpleumltordbms::ToColumn", is_abstract=True)
simpleumltordbms_Column = Class(name="simpleumltordbms::Column")
simpleumltordbms_Package = Class(name="simpleumltordbms::Package")
simpleumltordbms_UmlToRdbmsModelElement = Class(name="simpleumltordbms::UmlToRdbmsModelElement", is_abstract=True)

# simpleumltordbms_AttributeToColumn class attributes and methods

# FromAttribute class attributes and methods

# ToColumn class attributes and methods

# simpleumltordbms_PrimitiveToName class attributes and methods
simpleumltordbms_PrimitiveToName_typeName: Property = Property(name="typeName", type=StringType)
simpleumltordbms_PrimitiveToName.attributes={simpleumltordbms_PrimitiveToName_typeName}

# simpleumltordbms_Key class attributes and methods

# simpleumltordbms_Table class attributes and methods

# simpleumltordbms_Class class attributes and methods

# simpleumltordbms_AssociationToForeignKey class attributes and methods

# UmlToRdbmsModelElement class attributes and methods

# simpleumltordbms_Association class attributes and methods

# simpleumltordbms_ForeignKey class attributes and methods

# simpleumltordbms_ClassToTable class attributes and methods

# simpleumltordbms_BooleanToBoolean class attributes and methods

# PrimitiveToName class attributes and methods

# FromAttributeOwner class attributes and methods

# simpleumltordbms_PackageToSchema class attributes and methods

# simpleumltordbms_FromAttribute class attributes and methods
simpleumltordbms_FromAttribute_kind: Property = Property(name="kind", type=StringType)
simpleumltordbms_FromAttribute.attributes={simpleumltordbms_FromAttribute_kind}

# simpleumltordbms_Attribute class attributes and methods

# simpleumltordbms_IntegerToNumber class attributes and methods

# simpleumltordbms_NonLeafAttribute class attributes and methods

# simpleumltordbms_FromAttributeOwner class attributes and methods

# simpleumltordbms_Schema class attributes and methods

# simpleumltordbms_PrimitiveDataType class attributes and methods

# simpleumltordbms_StringToVarchar class attributes and methods

# simpleumltordbms_ToColumn class attributes and methods

# simpleumltordbms_Column class attributes and methods

# simpleumltordbms_Package class attributes and methods

# simpleumltordbms_UmlToRdbmsModelElement class attributes and methods
simpleumltordbms_UmlToRdbmsModelElement_name: Property = Property(name="name", type=StringType)
simpleumltordbms_UmlToRdbmsModelElement.attributes={simpleumltordbms_UmlToRdbmsModelElement_name}

# Relationships
type0: BinaryAssociation = BinaryAssociation(
    name="type0",
    ends={
        Property(name="simpleumltordbms_PrimitiveToName", type=simpleumltordbms_AttributeToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_AttributeToColumn", type=simpleumltordbms_PrimitiveToName, multiplicity=Multiplicity(0, 1))
    }
)
primaryKey9: BinaryAssociation = BinaryAssociation(
    name="primaryKey9",
    ends={
        Property(name="simpleumltordbms_Key", type=simpleumltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_ClassToTable10", type=simpleumltordbms_Key, multiplicity=Multiplicity(0, 1))
    }
)
table11: BinaryAssociation = BinaryAssociation(
    name="table11",
    ends={
        Property(name="simpleumltordbms_Table", type=simpleumltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_ClassToTable12", type=simpleumltordbms_Table, multiplicity=Multiplicity(0, 1))
    }
)
umlClass13: BinaryAssociation = BinaryAssociation(
    name="umlClass13",
    ends={
        Property(name="simpleumltordbms_Class", type=simpleumltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_ClassToTable14", type=simpleumltordbms_Class, multiplicity=Multiplicity(0, 1))
    }
)
association1: BinaryAssociation = BinaryAssociation(
    name="association1",
    ends={
        Property(name="simpleumltordbms_Association", type=simpleumltordbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_AssociationToForeignKey", type=simpleumltordbms_Association, multiplicity=Multiplicity(0, 1))
    }
)
foreignKey2: BinaryAssociation = BinaryAssociation(
    name="foreignKey2",
    ends={
        Property(name="simpleumltordbms_ForeignKey", type=simpleumltordbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_AssociationToForeignKey3", type=simpleumltordbms_ForeignKey, multiplicity=Multiplicity(0, 1))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="ClassToTable", type=simpleumltordbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="associationsToForeignKeys", type=simpleumltordbms_ClassToTable, multiplicity=Multiplicity(1, 1))
    }
)
referenced5: BinaryAssociation = BinaryAssociation(
    name="referenced5",
    ends={
        Property(name="simpleumltordbms_ClassToTable", type=simpleumltordbms_AssociationToForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_AssociationToForeignKey6", type=simpleumltordbms_ClassToTable, multiplicity=Multiplicity(0, 1))
    }
)
associationsToForeignKeys7: BinaryAssociation = BinaryAssociation(
    name="associationsToForeignKeys7",
    ends={
        Property(name="AssociationToForeignKey", type=simpleumltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=simpleumltordbms_AssociationToForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner8: BinaryAssociation = BinaryAssociation(
    name="owner8",
    ends={
        Property(name="PackageToSchema", type=simpleumltordbms_ClassToTable, multiplicity=Multiplicity(1, 1)),
        Property(name="classesToTables", type=simpleumltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1))
    }
)
attribute15: BinaryAssociation = BinaryAssociation(
    name="attribute15",
    ends={
        Property(name="simpleumltordbms_Attribute", type=simpleumltordbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_FromAttribute", type=simpleumltordbms_Attribute, multiplicity=Multiplicity(0, 1))
    }
)
fromAttributes20: BinaryAssociation = BinaryAssociation(
    name="fromAttributes20",
    ends={
        Property(name="FromAttribute", type=simpleumltordbms_FromAttributeOwner, multiplicity=Multiplicity(1, 1)),
        Property(name="owner21", type=simpleumltordbms_FromAttribute, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
leafs16: BinaryAssociation = BinaryAssociation(
    name="leafs16",
    ends={
        Property(name="simpleumltordbms_AttributeToColumn18", type=simpleumltordbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_FromAttribute17", type=simpleumltordbms_AttributeToColumn, multiplicity=Multiplicity(0, 9999))
    }
)
classesToTables22: BinaryAssociation = BinaryAssociation(
    name="classesToTables22",
    ends={
        Property(name="ClassToTable24", type=simpleumltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner23", type=simpleumltordbms_ClassToTable, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primitivesToNames25: BinaryAssociation = BinaryAssociation(
    name="primitivesToNames25",
    ends={
        Property(name="PrimitiveToName", type=simpleumltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="owner26", type=simpleumltordbms_PrimitiveToName, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
schema27: BinaryAssociation = BinaryAssociation(
    name="schema27",
    ends={
        Property(name="simpleumltordbms_Schema", type=simpleumltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_PackageToSchema", type=simpleumltordbms_Schema, multiplicity=Multiplicity(1, 1))
    }
)
owner19: BinaryAssociation = BinaryAssociation(
    name="owner19",
    ends={
        Property(name="FromAttributeOwner", type=simpleumltordbms_FromAttribute, multiplicity=Multiplicity(1, 1)),
        Property(name="fromAttributes", type=simpleumltordbms_FromAttributeOwner, multiplicity=Multiplicity(1, 1))
    }
)
umlPackage28: BinaryAssociation = BinaryAssociation(
    name="umlPackage28",
    ends={
        Property(name="simpleumltordbms_Package", type=simpleumltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_PackageToSchema29", type=simpleumltordbms_Package, multiplicity=Multiplicity(1, 1))
    }
)
owner30: BinaryAssociation = BinaryAssociation(
    name="owner30",
    ends={
        Property(name="PackageToSchema31", type=simpleumltordbms_PrimitiveToName, multiplicity=Multiplicity(1, 1)),
        Property(name="primitivesToNames", type=simpleumltordbms_PackageToSchema, multiplicity=Multiplicity(1, 1))
    }
)
primitive32: BinaryAssociation = BinaryAssociation(
    name="primitive32",
    ends={
        Property(name="simpleumltordbms_PrimitiveDataType", type=simpleumltordbms_PrimitiveToName, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_PrimitiveToName33", type=simpleumltordbms_PrimitiveDataType, multiplicity=Multiplicity(1, 1))
    }
)
column34: BinaryAssociation = BinaryAssociation(
    name="column34",
    ends={
        Property(name="simpleumltordbms_Column", type=simpleumltordbms_ToColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="simpleumltordbms_ToColumn", type=simpleumltordbms_Column, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_simpleumltordbms_AttributeToColumn_FromAttribute = Generalization(general=FromAttribute, specific=simpleumltordbms_AttributeToColumn)
gen_simpleumltordbms_AttributeToColumn_ToColumn = Generalization(general=ToColumn, specific=simpleumltordbms_AttributeToColumn)
gen_simpleumltordbms_AssociationToForeignKey_ToColumn = Generalization(general=ToColumn, specific=simpleumltordbms_AssociationToForeignKey)
gen_simpleumltordbms_AssociationToForeignKey_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=simpleumltordbms_AssociationToForeignKey)
gen_simpleumltordbms_BooleanToBoolean_PrimitiveToName = Generalization(general=PrimitiveToName, specific=simpleumltordbms_BooleanToBoolean)
gen_simpleumltordbms_ClassToTable_FromAttributeOwner = Generalization(general=FromAttributeOwner, specific=simpleumltordbms_ClassToTable)
gen_simpleumltordbms_ClassToTable_ToColumn = Generalization(general=ToColumn, specific=simpleumltordbms_ClassToTable)
gen_simpleumltordbms_ClassToTable_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=simpleumltordbms_ClassToTable)
gen_simpleumltordbms_FromAttribute_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=simpleumltordbms_FromAttribute)
gen_simpleumltordbms_IntegerToNumber_PrimitiveToName = Generalization(general=PrimitiveToName, specific=simpleumltordbms_IntegerToNumber)
gen_simpleumltordbms_NonLeafAttribute_FromAttributeOwner = Generalization(general=FromAttributeOwner, specific=simpleumltordbms_NonLeafAttribute)
gen_simpleumltordbms_NonLeafAttribute_FromAttribute = Generalization(general=FromAttribute, specific=simpleumltordbms_NonLeafAttribute)
gen_simpleumltordbms_PackageToSchema_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=simpleumltordbms_PackageToSchema)
gen_simpleumltordbms_PrimitiveToName_UmlToRdbmsModelElement = Generalization(general=UmlToRdbmsModelElement, specific=simpleumltordbms_PrimitiveToName)
gen_simpleumltordbms_StringToVarchar_PrimitiveToName = Generalization(general=PrimitiveToName, specific=simpleumltordbms_StringToVarchar)

# Domain Model
domain_model = DomainModel(
    name="simpleumltordbms",
    types={simpleumltordbms_AttributeToColumn, FromAttribute, ToColumn, simpleumltordbms_PrimitiveToName, simpleumltordbms_Key, simpleumltordbms_Table, simpleumltordbms_Class, simpleumltordbms_AssociationToForeignKey, UmlToRdbmsModelElement, simpleumltordbms_Association, simpleumltordbms_ForeignKey, simpleumltordbms_ClassToTable, simpleumltordbms_BooleanToBoolean, PrimitiveToName, FromAttributeOwner, simpleumltordbms_PackageToSchema, simpleumltordbms_FromAttribute, simpleumltordbms_Attribute, simpleumltordbms_IntegerToNumber, simpleumltordbms_NonLeafAttribute, simpleumltordbms_FromAttributeOwner, simpleumltordbms_Schema, simpleumltordbms_PrimitiveDataType, simpleumltordbms_StringToVarchar, simpleumltordbms_ToColumn, simpleumltordbms_Column, simpleumltordbms_Package, simpleumltordbms_UmlToRdbmsModelElement},
    associations={type0, primaryKey9, table11, umlClass13, association1, foreignKey2, owner4, referenced5, associationsToForeignKeys7, owner8, attribute15, fromAttributes20, leafs16, classesToTables22, primitivesToNames25, schema27, owner19, umlPackage28, owner30, primitive32, column34},
    generalizations={gen_simpleumltordbms_AttributeToColumn_FromAttribute, gen_simpleumltordbms_AttributeToColumn_ToColumn, gen_simpleumltordbms_AssociationToForeignKey_ToColumn, gen_simpleumltordbms_AssociationToForeignKey_UmlToRdbmsModelElement, gen_simpleumltordbms_BooleanToBoolean_PrimitiveToName, gen_simpleumltordbms_ClassToTable_FromAttributeOwner, gen_simpleumltordbms_ClassToTable_ToColumn, gen_simpleumltordbms_ClassToTable_UmlToRdbmsModelElement, gen_simpleumltordbms_FromAttribute_UmlToRdbmsModelElement, gen_simpleumltordbms_IntegerToNumber_PrimitiveToName, gen_simpleumltordbms_NonLeafAttribute_FromAttributeOwner, gen_simpleumltordbms_NonLeafAttribute_FromAttribute, gen_simpleumltordbms_PackageToSchema_UmlToRdbmsModelElement, gen_simpleumltordbms_PrimitiveToName_UmlToRdbmsModelElement, gen_simpleumltordbms_StringToVarchar_PrimitiveToName},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)