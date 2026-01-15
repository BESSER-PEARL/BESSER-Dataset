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

# Classes
relational_ENamedElement = Class(name="relational::ENamedElement", is_abstract=True)
relational_SQLObject = Class(name="relational::SQLObject", is_abstract=True)
ENamedElement = Class(name="ENamedElement")
relational_DataType = Class(name="relational::DataType")
SQLObject = Class(name="SQLObject")
relational_TypedElement = Class(name="relational::TypedElement", is_abstract=True)
relational_Schema = Class(name="relational::Schema")
relational_Table = Class(name="relational::Table", is_abstract=True)
relational_Trigger = Class(name="relational::Trigger")
relational_Comment = Class(name="relational::Comment", is_abstract=True)
relational_ReferenceConstraint = Class(name="relational::ReferenceConstraint", is_abstract=True)
relational_ForeignKey = Class(name="relational::ForeignKey")
relational_BaseTable = Class(name="relational::BaseTable")
Table = Class(name="Table")
relational_Column = Class(name="relational::Column")
TypedElement = Class(name="TypedElement")
relational_Constraint = Class(name="relational::Constraint", is_abstract=True)
Constraint = Class(name="Constraint")
TableConstraint = Class(name="TableConstraint")
ReferenceConstraint = Class(name="ReferenceConstraint")
relational_TableConstraint = Class(name="relational::TableConstraint", is_abstract=True)
relational_PrimaryKey = Class(name="relational::PrimaryKey")
UniqueConstraint = Class(name="UniqueConstraint")
relational_UniqueConstraint = Class(name="relational::UniqueConstraint")

# relational_ENamedElement class attributes and methods
relational_ENamedElement_name: Property = Property(name="name", type=StringType)
relational_ENamedElement.attributes={relational_ENamedElement_name}

# relational_SQLObject class attributes and methods
relational_SQLObject_description: Property = Property(name="description", type=StringType)
relational_SQLObject_label: Property = Property(name="label", type=StringType)
relational_SQLObject.attributes={relational_SQLObject_description, relational_SQLObject_label}

# ENamedElement class attributes and methods

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
relational_Trigger.attributes={relational_Trigger_deleteType, relational_Trigger_actionTime, relational_Trigger_updateType, relational_Trigger_insertType}

# relational_Comment class attributes and methods
relational_Comment_description: Property = Property(name="description", type=StringType)
relational_Comment.attributes={relational_Comment_description}

# relational_ReferenceConstraint class attributes and methods

# relational_ForeignKey class attributes and methods

# relational_BaseTable class attributes and methods

# Table class attributes and methods

# relational_Column class attributes and methods
relational_Column_length: Property = Property(name="length", type=IntegerType)
relational_Column_nullable: Property = Property(name="nullable", type=BooleanType)
relational_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
relational_Column.attributes={relational_Column_length, relational_Column_nullable, relational_Column_defaultValue}

# TypedElement class attributes and methods

# relational_Constraint class attributes and methods

# Constraint class attributes and methods

# TableConstraint class attributes and methods

# ReferenceConstraint class attributes and methods

# relational_TableConstraint class attributes and methods

# relational_PrimaryKey class attributes and methods

# UniqueConstraint class attributes and methods

# relational_UniqueConstraint class attributes and methods

# Relationships
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
comments0: BinaryAssociation = BinaryAssociation(
    name="comments0",
    ends={
        Property(name="Comment", type=relational_SQLObject, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlobject", type=relational_Comment, multiplicity=Multiplicity(0, 9999))
    }
)
sqlobject1: BinaryAssociation = BinaryAssociation(
    name="sqlobject1",
    ends={
        Property(name="SQLObject", type=relational_Comment, multiplicity=Multiplicity(1, 1)),
        Property(name="comments", type=relational_SQLObject, multiplicity=Multiplicity(1, 1))
    }
)
table8: BinaryAssociation = BinaryAssociation(
    name="table8",
    ends={
        Property(name="Table10", type=relational_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers9", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
triggerTables11: BinaryAssociation = BinaryAssociation(
    name="triggerTables11",
    ends={
        Property(name="Table12", type=relational_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggersConstrainted", type=relational_Table, multiplicity=Multiplicity(1, 9999))
    }
)
schema13: BinaryAssociation = BinaryAssociation(
    name="schema13",
    ends={
        Property(name="Schema14", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=relational_Schema, multiplicity=Multiplicity(1, 1))
    }
)
triggers15: BinaryAssociation = BinaryAssociation(
    name="triggers15",
    ends={
        Property(name="Trigger16", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=relational_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
triggersConstrainted17: BinaryAssociation = BinaryAssociation(
    name="triggersConstrainted17",
    ends={
        Property(name="Trigger18", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="triggerTables", type=relational_Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
schema7: BinaryAssociation = BinaryAssociation(
    name="schema7",
    ends={
        Property(name="Schema", type=relational_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers", type=relational_Schema, multiplicity=Multiplicity(1, 1))
    }
)
table21: BinaryAssociation = BinaryAssociation(
    name="table21",
    ends={
        Property(name="Table22", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
referenceConstraint23: BinaryAssociation = BinaryAssociation(
    name="referenceConstraint23",
    ends={
        Property(name="ReferenceConstraint", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="members", type=relational_ReferenceConstraint, multiplicity=Multiplicity(1, 9999))
    }
)
foreignKey24: BinaryAssociation = BinaryAssociation(
    name="foreignKey24",
    ends={
        Property(name="ForeignKey", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedMembers", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
referencingForeignKeys25: BinaryAssociation = BinaryAssociation(
    name="referencingForeignKeys25",
    ends={
        Property(name="ForeignKey26", type=relational_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="referencedTable", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
columns19: BinaryAssociation = BinaryAssociation(
    name="columns19",
    ends={
        Property(name="Column", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table20", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
baseTable28: BinaryAssociation = BinaryAssociation(
    name="baseTable28",
    ends={
        Property(name="BaseTable", type=relational_TableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="constraints", type=relational_BaseTable, multiplicity=Multiplicity(1, 1))
    }
)
members29: BinaryAssociation = BinaryAssociation(
    name="members29",
    ends={
        Property(name="Column30", type=relational_ReferenceConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="referenceConstraint", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
constraints27: BinaryAssociation = BinaryAssociation(
    name="constraints27",
    ends={
        Property(name="TableConstraint", type=relational_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="baseTable", type=relational_TableConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
referencedMembers34: BinaryAssociation = BinaryAssociation(
    name="referencedMembers34",
    ends={
        Property(name="Column36", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey35", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
foreignKey37: BinaryAssociation = BinaryAssociation(
    name="foreignKey37",
    ends={
        Property(name="ForeignKey38", type=relational_UniqueConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueConstraint", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
referencedTable31: BinaryAssociation = BinaryAssociation(
    name="referencedTable31",
    ends={
        Property(name="BaseTable32", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="referencingForeignKeys", type=relational_BaseTable, multiplicity=Multiplicity(1, 1))
    }
)
uniqueConstraint33: BinaryAssociation = BinaryAssociation(
    name="uniqueConstraint33",
    ends={
        Property(name="UniqueConstraint", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKey", type=relational_UniqueConstraint, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_relational_SQLObject_ENamedElement = Generalization(general=ENamedElement, specific=relational_SQLObject)
gen_relational_DataType_SQLObject = Generalization(general=SQLObject, specific=relational_DataType)
gen_relational_TypedElement_SQLObject = Generalization(general=SQLObject, specific=relational_TypedElement)
gen_relational_Schema_SQLObject = Generalization(general=SQLObject, specific=relational_Schema)
gen_relational_Trigger_SQLObject = Generalization(general=SQLObject, specific=relational_Trigger)
gen_relational_Table_SQLObject = Generalization(general=SQLObject, specific=relational_Table)
gen_relational_BaseTable_Table = Generalization(general=Table, specific=relational_BaseTable)
gen_relational_Column_TypedElement = Generalization(general=TypedElement, specific=relational_Column)
gen_relational_Constraint_SQLObject = Generalization(general=SQLObject, specific=relational_Constraint)
gen_relational_TableConstraint_Constraint = Generalization(general=Constraint, specific=relational_TableConstraint)
gen_relational_ReferenceConstraint_TableConstraint = Generalization(general=TableConstraint, specific=relational_ReferenceConstraint)
gen_relational_UniqueConstraint_ReferenceConstraint = Generalization(general=ReferenceConstraint, specific=relational_UniqueConstraint)
gen_relational_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=relational_PrimaryKey)
gen_relational_ForeignKey_ReferenceConstraint = Generalization(general=ReferenceConstraint, specific=relational_ForeignKey)

# Domain Model
domain_model = DomainModel(
    name="relational",
    types={relational_ENamedElement, relational_SQLObject, ENamedElement, relational_DataType, SQLObject, relational_TypedElement, relational_Schema, relational_Table, relational_Trigger, relational_Comment, relational_ReferenceConstraint, relational_ForeignKey, relational_BaseTable, Table, relational_Column, TypedElement, relational_Constraint, Constraint, TableConstraint, ReferenceConstraint, relational_TableConstraint, relational_PrimaryKey, UniqueConstraint, relational_UniqueConstraint, ActionTimeType},
    associations={typedElement2, dataType3, tables4, triggers5, comments0, sqlobject1, table8, triggerTables11, schema13, triggers15, triggersConstrainted17, schema7, table21, referenceConstraint23, foreignKey24, referencingForeignKeys25, columns19, baseTable28, members29, constraints27, referencedMembers34, foreignKey37, referencedTable31, uniqueConstraint33},
    generalizations={gen_relational_SQLObject_ENamedElement, gen_relational_DataType_SQLObject, gen_relational_TypedElement_SQLObject, gen_relational_Schema_SQLObject, gen_relational_Trigger_SQLObject, gen_relational_Table_SQLObject, gen_relational_BaseTable_Table, gen_relational_Column_TypedElement, gen_relational_Constraint_SQLObject, gen_relational_TableConstraint_Constraint, gen_relational_ReferenceConstraint_TableConstraint, gen_relational_UniqueConstraint_ReferenceConstraint, gen_relational_PrimaryKey_UniqueConstraint, gen_relational_ForeignKey_ReferenceConstraint},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)