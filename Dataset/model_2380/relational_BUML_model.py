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

# Enumerations
ActionTimeType: Enumeration = Enumeration(
    name="ActionTimeType",
    literals={
            EnumerationLiteral(name="AFTER"),
			EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="INSTEADOF")
    }
)

ReferentialActionType: Enumeration = Enumeration(
    name="ReferentialActionType",
    literals={
            EnumerationLiteral(name="CASCADE"),
			EnumerationLiteral(name="SET_NULL"),
			EnumerationLiteral(name="SET_DEFAULT"),
			EnumerationLiteral(name="NO_ACTION"),
			EnumerationLiteral(name="RESTRICT")
    }
)

ActionGranularityType: Enumeration = Enumeration(
    name="ActionGranularityType",
    literals={
            EnumerationLiteral(name="STATEMENT"),
			EnumerationLiteral(name="ROW")
    }
)

# Classes
relational_ENamedElement = Class(name="relational::ENamedElement", is_abstract=True)
relational_SQLObject = Class(name="relational::SQLObject", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
relational_Comment = Class(name="relational::Comment", is_abstract=True)
relational_UserDefinedType = Class(name="relational::UserDefinedType")
relational_DataType = Class(name="relational::DataType")
SQLObject = Class(name="SQLObject")
relational_TypedElement = Class(name="relational::TypedElement", is_abstract=True)
relational_Schema = Class(name="relational::Schema")
relational_Table = Class(name="relational::Table", is_abstract=True)
relational_Trigger = Class(name="relational::Trigger")
relational_Assertion = Class(name="relational::Assertion")
relational_Column = Class(name="relational::Column")
TypedElement = Class(name="TypedElement")
relational_TableConstraint = Class(name="relational::TableConstraint", is_abstract=True)
relational_ReferenceConstraint = Class(name="relational::ReferenceConstraint", is_abstract=True)
relational_ForeignKey = Class(name="relational::ForeignKey")
relational_BaseTable = Class(name="relational::BaseTable")
Table = Class(name="Table")
ReferenceConstraint = Class(name="ReferenceConstraint")
relational_Constraint = Class(name="relational::Constraint", is_abstract=True)
Constraint = Class(name="Constraint")
TableConstraint = Class(name="TableConstraint")
relational_CheckConstraint = Class(name="relational::CheckConstraint")
relational_UniqueConstraint = Class(name="relational::UniqueConstraint")
relational_PrimaryKey = Class(name="relational::PrimaryKey")
UniqueConstraint = Class(name="UniqueConstraint")
DataType = Class(name="DataType")
relational_Domain = Class(name="relational::Domain")
DistinctUserDefinedType = Class(name="DistinctUserDefinedType")
relational_DistinctUserDefinedType = Class(name="relational::DistinctUserDefinedType")
UserDefinedType = Class(name="UserDefinedType")

# relational_ENamedElement class attributes and methods
relational_ENamedElement_name: Property = Property(name="name", type=StringType)
relational_ENamedElement.attributes={relational_ENamedElement_name}

# relational_SQLObject class attributes and methods
relational_SQLObject_description: Property = Property(name="description", type=StringType)
relational_SQLObject_label: Property = Property(name="label", type=StringType)
relational_SQLObject.attributes={relational_SQLObject_description, relational_SQLObject_label}

# ENamedElement class attributes and methods

# relational_Comment class attributes and methods
relational_Comment_description: Property = Property(name="description", type=StringType)
relational_Comment.attributes={relational_Comment_description}

# relational_UserDefinedType class attributes and methods

# relational_DataType class attributes and methods

# SQLObject class attributes and methods

# relational_TypedElement class attributes and methods

# relational_Schema class attributes and methods

# relational_Table class attributes and methods

# relational_Trigger class attributes and methods
relational_Trigger_updateType: Property = Property(name="updateType", type=BooleanType)
relational_Trigger_insertType: Property = Property(name="insertType", type=BooleanType)
relational_Trigger_deleteType: Property = Property(name="deleteType", type=BooleanType)
relational_Trigger_actionTime: Property = Property(name="actionTime", type=StringType)
relational_Trigger_condition: Property = Property(name="condition", type=StringType)
relational_Trigger_statementSQL: Property = Property(name="statementSQL", type=StringType)
relational_Trigger_oldRow: Property = Property(name="oldRow", type=StringType)
relational_Trigger_newRow: Property = Property(name="newRow", type=StringType)
relational_Trigger_oldTable: Property = Property(name="oldTable", type=StringType)
relational_Trigger_newTable: Property = Property(name="newTable", type=StringType)
relational_Trigger_actionGranularity: Property = Property(name="actionGranularity", type=StringType)
relational_Trigger.attributes={relational_Trigger_newRow, relational_Trigger_insertType, relational_Trigger_updateType, relational_Trigger_oldTable, relational_Trigger_condition, relational_Trigger_statementSQL, relational_Trigger_oldRow, relational_Trigger_actionGranularity, relational_Trigger_actionTime, relational_Trigger_newTable, relational_Trigger_deleteType}

# relational_Assertion class attributes and methods
relational_Assertion_searchCondition: Property = Property(name="searchCondition", type=StringType)
relational_Assertion.attributes={relational_Assertion_searchCondition}

# relational_Column class attributes and methods
relational_Column_nullable: Property = Property(name="nullable", type=BooleanType)
relational_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
relational_Column_length: Property = Property(name="length", type=IntegerType)
relational_Column_srid: Property = Property(name="srid", type=StringType)
relational_Column.attributes={relational_Column_srid, relational_Column_nullable, relational_Column_length, relational_Column_defaultValue}

# TypedElement class attributes and methods

# relational_TableConstraint class attributes and methods

# relational_ReferenceConstraint class attributes and methods

# relational_ForeignKey class attributes and methods
relational_ForeignKey_onUpdate: Property = Property(name="onUpdate", type=StringType)
relational_ForeignKey_onDelete: Property = Property(name="onDelete", type=StringType)
relational_ForeignKey.attributes={relational_ForeignKey_onUpdate, relational_ForeignKey_onDelete}

# relational_BaseTable class attributes and methods

# Table class attributes and methods

# ReferenceConstraint class attributes and methods

# relational_Constraint class attributes and methods

# Constraint class attributes and methods

# TableConstraint class attributes and methods

# relational_CheckConstraint class attributes and methods
relational_CheckConstraint_searchCondition: Property = Property(name="searchCondition", type=StringType)
relational_CheckConstraint.attributes={relational_CheckConstraint_searchCondition}

# relational_UniqueConstraint class attributes and methods

# relational_PrimaryKey class attributes and methods

# UniqueConstraint class attributes and methods

# DataType class attributes and methods

# relational_Domain class attributes and methods
relational_Domain_defaultValue: Property = Property(name="defaultValue", type=StringType)
relational_Domain_nullable: Property = Property(name="nullable", type=BooleanType)
relational_Domain.attributes={relational_Domain_defaultValue, relational_Domain_nullable}

# DistinctUserDefinedType class attributes and methods

# relational_DistinctUserDefinedType class attributes and methods

# UserDefinedType class attributes and methods

# Relationships
comments0: BinaryAssociation = BinaryAssociation(
    name="comments0",
    ends={
        Property(name="sqlobject", type=relational_Comment, multiplicity=Multiplicity(0, 9999)),
        Property(name="Comment", type=relational_SQLObject, multiplicity=Multiplicity(1, 1))
    }
)
assertions7: BinaryAssociation = BinaryAssociation(
    name="assertions7",
    ends={
        Property(name="schema8", type=relational_Assertion, multiplicity=Multiplicity(0, 9999)),
        Property(name="Assertion", type=relational_Schema, multiplicity=Multiplicity(1, 1))
    }
)
sqlobject1: BinaryAssociation = BinaryAssociation(
    name="sqlobject1",
    ends={
        Property(name="SQLObject", type=relational_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=relational_SQLObject, multiplicity=Multiplicity(1, 1))
    }
)
typedElement2: BinaryAssociation = BinaryAssociation(
    name="typedElement2",
    ends={
        Property(name="TypedElement", type=relational_DataType, multiplicity=Multiplicity(1, 1)),
        Property(name="dataType", type=relational_TypedElement, multiplicity=Multiplicity(0, 9999))
    }
)
dataType3: BinaryAssociation = BinaryAssociation(
    name="dataType3",
    ends={
        Property(name="DataType", type=relational_TypedElement, multiplicity=Multiplicity(1, 1)),
        Property(name="typedElement", type=relational_DataType, multiplicity=Multiplicity(1, 1))
    }
)
tables4: BinaryAssociation = BinaryAssociation(
    name="tables4",
    ends={
        Property(name="Table", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=relational_Table, multiplicity=Multiplicity(0, 9999))
    }
)
triggers5: BinaryAssociation = BinaryAssociation(
    name="triggers5",
    ends={
        Property(name="Trigger", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema6", type=relational_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
triggerTables15: BinaryAssociation = BinaryAssociation(
    name="triggerTables15",
    ends={
        Property(name="Table16", type=relational_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersConstrainted", type=relational_Table, multiplicity=Multiplicity(1, 9999))
    }
)
userDefinedTypes9: BinaryAssociation = BinaryAssociation(
    name="userDefinedTypes9",
    ends={
        Property(name="UserDefinedType", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema10", type=relational_UserDefinedType, multiplicity=Multiplicity(0, 9999))
    }
)
schema11: BinaryAssociation = BinaryAssociation(
    name="schema11",
    ends={
        Property(name="Schema", type=relational_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers", type=relational_Schema, multiplicity=Multiplicity(1, 1))
    }
)
table12: BinaryAssociation = BinaryAssociation(
    name="table12",
    ends={
        Property(name="Table14", type=relational_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers13", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
schema17: BinaryAssociation = BinaryAssociation(
    name="schema17",
    ends={
        Property(name="Schema18", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=relational_Schema, multiplicity=Multiplicity(1, 1))
    }
)
table25: BinaryAssociation = BinaryAssociation(
    name="table25",
    ends={
        Property(name="Table26", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
triggers19: BinaryAssociation = BinaryAssociation(
    name="triggers19",
    ends={
        Property(name="Trigger20", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=relational_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
triggersConstrainted21: BinaryAssociation = BinaryAssociation(
    name="triggersConstrainted21",
    ends={
        Property(name="Trigger22", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="triggerTables", type=relational_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
columns23: BinaryAssociation = BinaryAssociation(
    name="columns23",
    ends={
        Property(name="Column", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table24", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
referenceConstraint27: BinaryAssociation = BinaryAssociation(
    name="referenceConstraint27",
    ends={
        Property(name="ReferenceConstraint", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=relational_ReferenceConstraint, multiplicity=Multiplicity(1, 9999))
    }
)
foreignKey28: BinaryAssociation = BinaryAssociation(
    name="foreignKey28",
    ends={
        Property(name="ForeignKey", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedMembers", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
referencingForeignKeys29: BinaryAssociation = BinaryAssociation(
    name="referencingForeignKeys29",
    ends={
        Property(name="ForeignKey30", type=relational_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedTable", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
constraints31: BinaryAssociation = BinaryAssociation(
    name="constraints31",
    ends={
        Property(name="TableConstraint", type=relational_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="baseTable", type=relational_TableConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
baseTable32: BinaryAssociation = BinaryAssociation(
    name="baseTable32",
    ends={
        Property(name="BaseTable", type=relational_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=relational_BaseTable, multiplicity=Multiplicity(1, 1))
    }
)
members33: BinaryAssociation = BinaryAssociation(
    name="members33",
    ends={
        Property(name="Column34", type=relational_ReferenceConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="referenceConstraint", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
referencedTable35: BinaryAssociation = BinaryAssociation(
    name="referencedTable35",
    ends={
        Property(name="BaseTable36", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingForeignKeys", type=relational_BaseTable, multiplicity=Multiplicity(1, 1))
    }
)
uniqueConstraint37: BinaryAssociation = BinaryAssociation(
    name="uniqueConstraint37",
    ends={
        Property(name="UniqueConstraint", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=relational_UniqueConstraint, multiplicity=Multiplicity(1, 1))
    }
)
referencedMembers38: BinaryAssociation = BinaryAssociation(
    name="referencedMembers38",
    ends={
        Property(name="Column40", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey39", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
foreignKey41: BinaryAssociation = BinaryAssociation(
    name="foreignKey41",
    ends={
        Property(name="ForeignKey42", type=relational_UniqueConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueConstraint", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
schema43: BinaryAssociation = BinaryAssociation(
    name="schema43",
    ends={
        Property(name="Schema44", type=relational_Assertion, multiplicity=Multiplicity(1, 1)),
        Property(name="assertions", type=relational_Schema, multiplicity=Multiplicity(1, 1))
    }
)
schema45: BinaryAssociation = BinaryAssociation(
    name="schema45",
    ends={
        Property(name="Schema46", type=relational_UserDefinedType, multiplicity=Multiplicity(1, 1)),
        Property(name="userDefinedTypes", type=relational_Schema, multiplicity=Multiplicity(1, 1))
    }
)
constraint47: BinaryAssociation = BinaryAssociation(
    name="constraint47",
    ends={
        Property(name="relational_CheckConstraint", type=relational_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Domain", type=relational_CheckConstraint, multiplicity=Multiplicity(0, 1))
    }
)
referencedType48: BinaryAssociation = BinaryAssociation(
    name="referencedType48",
    ends={
        Property(name="relational_DataType", type=relational_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Domain49", type=relational_DataType, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_relational_SQLObject_ENamedElement = Generalization(general=ENamedElement, specific=relational_SQLObject)
gen_relational_DataType_SQLObject = Generalization(general=SQLObject, specific=relational_DataType)
gen_relational_TypedElement_SQLObject = Generalization(general=SQLObject, specific=relational_TypedElement)
gen_relational_Schema_SQLObject = Generalization(general=SQLObject, specific=relational_Schema)
gen_relational_Trigger_SQLObject = Generalization(general=SQLObject, specific=relational_Trigger)
gen_relational_Table_SQLObject = Generalization(general=SQLObject, specific=relational_Table)
gen_relational_Column_TypedElement = Generalization(general=TypedElement, specific=relational_Column)
gen_relational_BaseTable_Table = Generalization(general=Table, specific=relational_BaseTable)
gen_relational_ForeignKey_ReferenceConstraint = Generalization(general=ReferenceConstraint, specific=relational_ForeignKey)
gen_relational_Constraint_SQLObject = Generalization(general=SQLObject, specific=relational_Constraint)
gen_relational_TableConstraint_Constraint = Generalization(general=Constraint, specific=relational_TableConstraint)
gen_relational_ReferenceConstraint_TableConstraint = Generalization(general=TableConstraint, specific=relational_ReferenceConstraint)
gen_relational_CheckConstraint_TableConstraint = Generalization(general=TableConstraint, specific=relational_CheckConstraint)
gen_relational_UniqueConstraint_ReferenceConstraint = Generalization(general=ReferenceConstraint, specific=relational_UniqueConstraint)
gen_relational_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=relational_PrimaryKey)
gen_relational_DistinctUserDefinedType_UserDefinedType = Generalization(general=UserDefinedType, specific=relational_DistinctUserDefinedType)
gen_relational_Assertion_Constraint = Generalization(general=Constraint, specific=relational_Assertion)
gen_relational_UserDefinedType_DataType = Generalization(general=DataType, specific=relational_UserDefinedType)
gen_relational_Domain_DistinctUserDefinedType = Generalization(general=DistinctUserDefinedType, specific=relational_Domain)

# Domain Model
domain_model = DomainModel(
    name="relational",
    types={relational_ENamedElement, relational_SQLObject, ENamedElement, relational_Comment, relational_UserDefinedType, relational_DataType, SQLObject, relational_TypedElement, relational_Schema, relational_Table, relational_Trigger, relational_Assertion, relational_Column, TypedElement, relational_TableConstraint, relational_ReferenceConstraint, relational_ForeignKey, relational_BaseTable, Table, ReferenceConstraint, relational_Constraint, Constraint, TableConstraint, relational_CheckConstraint, relational_UniqueConstraint, relational_PrimaryKey, UniqueConstraint, DataType, relational_Domain, DistinctUserDefinedType, relational_DistinctUserDefinedType, UserDefinedType, ActionTimeType, ReferentialActionType, ActionGranularityType},
    associations={comments0, assertions7, sqlobject1, typedElement2, dataType3, tables4, triggers5, triggerTables15, userDefinedTypes9, schema11, table12, schema17, table25, triggers19, triggersConstrainted21, columns23, referenceConstraint27, foreignKey28, referencingForeignKeys29, constraints31, baseTable32, members33, referencedTable35, uniqueConstraint37, referencedMembers38, foreignKey41, schema43, schema45, constraint47, referencedType48},
    generalizations={gen_relational_SQLObject_ENamedElement, gen_relational_DataType_SQLObject, gen_relational_TypedElement_SQLObject, gen_relational_Schema_SQLObject, gen_relational_Trigger_SQLObject, gen_relational_Table_SQLObject, gen_relational_Column_TypedElement, gen_relational_BaseTable_Table, gen_relational_ForeignKey_ReferenceConstraint, gen_relational_Constraint_SQLObject, gen_relational_TableConstraint_Constraint, gen_relational_ReferenceConstraint_TableConstraint, gen_relational_CheckConstraint_TableConstraint, gen_relational_UniqueConstraint_ReferenceConstraint, gen_relational_PrimaryKey_UniqueConstraint, gen_relational_DistinctUserDefinedType_UserDefinedType, gen_relational_Assertion_Constraint, gen_relational_UserDefinedType_DataType, gen_relational_Domain_DistinctUserDefinedType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)