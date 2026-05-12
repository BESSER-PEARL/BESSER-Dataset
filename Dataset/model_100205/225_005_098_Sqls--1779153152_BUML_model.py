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
TriggerTime: Enumeration = Enumeration(
    name="TriggerTime",
    literals={
            EnumerationLiteral(name="BEFORE"),
			EnumerationLiteral(name="AFTER")
    }
)

# Classes
sqls_SqlLibrary = Class(name="sqls_SqlLibrary")
sqls_Import = Class(name="sqls_Import")
sqls_Tag = Class(name="sqls_Tag")
sqls_Type = Class(name="sqls_Type")
sqls_Table = Class(name="sqls_Table")
sqls_Column = Class(name="sqls_Column")
sqls_Trigger = Class(name="sqls_Trigger")
sqls_SqlMethod = Class(name="sqls_SqlMethod")
sqls_EnumElement = Class(name="sqls_EnumElement")
sqls_SqlType = Class(name="sqls_SqlType")
sqls_SqlExpr = Class(name="sqls_SqlExpr")
sqls_TableConstraint = Class(name="sqls_TableConstraint")
sqls_UniqueTableConstraint = Class(name="sqls_UniqueTableConstraint")
TableConstraint = Class(name="TableConstraint")
sqls_Select = Class(name="sqls_Select")
SqlSentence = Class(name="SqlSentence")
sqls_SqlSentence = Class(name="sqls_SqlSentence")
sqls_OrderingTerm = Class(name="sqls_OrderingTerm")
sqls_ResultColumn = Class(name="sqls_ResultColumn")
sqls_SelectList = Class(name="sqls_SelectList")
sqls_SqlFunction = Class(name="sqls_SqlFunction")
SqlExpr = Class(name="SqlExpr")
sqls_Function = Class(name="sqls_Function")
sqls_TableRef = Class(name="sqls_TableRef")
sqls_Insert = Class(name="sqls_Insert")
sqls_InsertStatement = Class(name="sqls_InsertStatement")
sqls_Delete = Class(name="sqls_Delete")
sqls_Update = Class(name="sqls_Update")
sqls_UpdateColumnExpression = Class(name="sqls_UpdateColumnExpression")
sqls_Get = Class(name="sqls_Get")
sqls_SqlBinaryExpr = Class(name="sqls_SqlBinaryExpr")
sqls_TriggerAction = Class(name="sqls_TriggerAction")
sqls_Enum = Class(name="sqls_Enum")
Type = Class(name="Type")
sqls_TypeDef = Class(name="sqls_TypeDef")
sqls_SqlPlaceholder = Class(name="sqls_SqlPlaceholder")
sqls_NewColumn = Class(name="sqls_NewColumn")
sqls_OldColumn = Class(name="sqls_OldColumn")
sqls_SqlNested = Class(name="sqls_SqlNested")
sqls_ColumnRef = Class(name="sqls_ColumnRef")
sqls_SqlParam = Class(name="sqls_SqlParam")
sqls_SqlStringLiteral = Class(name="sqls_SqlStringLiteral")
sqls_SqlNumberLiteral = Class(name="sqls_SqlNumberLiteral")
sqls_SqlMethodRef = Class(name="sqls_SqlMethodRef")
sqls_DeleteTable = Class(name="sqls_DeleteTable")
sqls_TriggerInsert = Class(name="sqls_TriggerInsert")
TriggerAction = Class(name="TriggerAction")
sqls_TriggerDelete = Class(name="sqls_TriggerDelete")
sqls_TriggerUpdate = Class(name="sqls_TriggerUpdate")

# sqls_SqlLibrary class attributes and methods
sqls_SqlLibrary_database: Property = Property(name="database", type=StringType)
sqls_SqlLibrary_version: Property = Property(name="version", type=IntegerType)
sqls_SqlLibrary.attributes={sqls_SqlLibrary_version, sqls_SqlLibrary_database}

# sqls_Import class attributes and methods

# sqls_Tag class attributes and methods
sqls_Tag_name: Property = Property(name="name", type=StringType)
sqls_Tag.attributes={sqls_Tag_name}

# sqls_Type class attributes and methods

# sqls_Table class attributes and methods
sqls_Table_name: Property = Property(name="name", type=StringType)
sqls_Table.attributes={sqls_Table_name}

# sqls_Column class attributes and methods
sqls_Column_name: Property = Property(name="name", type=StringType)
sqls_Column_null: Property = Property(name="null", type=BooleanType)
sqls_Column_primaryKey: Property = Property(name="primaryKey", type=BooleanType)
sqls_Column.attributes={sqls_Column_primaryKey, sqls_Column_name, sqls_Column_null}

# sqls_Trigger class attributes and methods
sqls_Trigger_name: Property = Property(name="name", type=StringType)
sqls_Trigger_time: Property = Property(name="time", type=StringType)
sqls_Trigger.attributes={sqls_Trigger_name, sqls_Trigger_time}

# sqls_SqlMethod class attributes and methods
sqls_SqlMethod_array: Property = Property(name="array", type=BooleanType)
sqls_SqlMethod_name: Property = Property(name="name", type=StringType)
sqls_SqlMethod.attributes={sqls_SqlMethod_array, sqls_SqlMethod_name}

# sqls_EnumElement class attributes and methods
sqls_EnumElement_name: Property = Property(name="name", type=StringType)
sqls_EnumElement_text: Property = Property(name="text", type=StringType)
sqls_EnumElement.attributes={sqls_EnumElement_name, sqls_EnumElement_text}

# sqls_SqlType class attributes and methods

# sqls_SqlExpr class attributes and methods

# sqls_TableConstraint class attributes and methods

# sqls_UniqueTableConstraint class attributes and methods
sqls_UniqueTableConstraint_name: Property = Property(name="name", type=StringType)
sqls_UniqueTableConstraint.attributes={sqls_UniqueTableConstraint_name}

# TableConstraint class attributes and methods

# sqls_Select class attributes and methods
sqls_Select_all: Property = Property(name="all", type=BooleanType)
sqls_Select.attributes={sqls_Select_all}

# SqlSentence class attributes and methods

# sqls_SqlSentence class attributes and methods

# sqls_OrderingTerm class attributes and methods
sqls_OrderingTerm_asc: Property = Property(name="asc", type=BooleanType)
sqls_OrderingTerm_desc: Property = Property(name="desc", type=BooleanType)
sqls_OrderingTerm.attributes={sqls_OrderingTerm_desc, sqls_OrderingTerm_asc}

# sqls_ResultColumn class attributes and methods
sqls_ResultColumn_name: Property = Property(name="name", type=StringType)
sqls_ResultColumn.attributes={sqls_ResultColumn_name}

# sqls_SelectList class attributes and methods

# sqls_SqlFunction class attributes and methods

# SqlExpr class attributes and methods

# sqls_Function class attributes and methods

# sqls_TableRef class attributes and methods
sqls_TableRef_alias: Property = Property(name="alias", type=StringType)
sqls_TableRef.attributes={sqls_TableRef_alias}

# sqls_Insert class attributes and methods

# sqls_InsertStatement class attributes and methods

# sqls_Delete class attributes and methods

# sqls_Update class attributes and methods

# sqls_UpdateColumnExpression class attributes and methods

# sqls_Get class attributes and methods

# sqls_SqlBinaryExpr class attributes and methods
sqls_SqlBinaryExpr_op: Property = Property(name="op", type=StringType)
sqls_SqlBinaryExpr.attributes={sqls_SqlBinaryExpr_op}

# sqls_TriggerAction class attributes and methods

# sqls_Enum class attributes and methods

# Type class attributes and methods

# sqls_TypeDef class attributes and methods

# sqls_SqlPlaceholder class attributes and methods

# sqls_NewColumn class attributes and methods

# sqls_OldColumn class attributes and methods

# sqls_SqlNested class attributes and methods

# sqls_ColumnRef class attributes and methods

# sqls_SqlParam class attributes and methods
sqls_SqlParam_name: Property = Property(name="name", type=StringType)
sqls_SqlParam.attributes={sqls_SqlParam_name}

# sqls_SqlStringLiteral class attributes and methods
sqls_SqlStringLiteral_value: Property = Property(name="value", type=StringType)
sqls_SqlStringLiteral.attributes={sqls_SqlStringLiteral_value}

# sqls_SqlNumberLiteral class attributes and methods
sqls_SqlNumberLiteral_value: Property = Property(name="value", type=IntegerType)
sqls_SqlNumberLiteral.attributes={sqls_SqlNumberLiteral_value}

# sqls_SqlMethodRef class attributes and methods

# sqls_DeleteTable class attributes and methods

# sqls_TriggerInsert class attributes and methods

# TriggerAction class attributes and methods

# sqls_TriggerDelete class attributes and methods

# sqls_TriggerUpdate class attributes and methods

# Relationships
tables8: BinaryAssociation = BinaryAssociation(
    name="tables8",
    ends={
        Property(name="sqls_Table", type=sqls_SqlLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlLibrary9", type=sqls_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
imports0: BinaryAssociation = BinaryAssociation(
    name="imports0",
    ends={
        Property(name="sqls_Import", type=sqls_SqlLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlLibrary", type=sqls_Import, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags1: BinaryAssociation = BinaryAssociation(
    name="tags1",
    ends={
        Property(name="sqls_Tag", type=sqls_SqlLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlLibrary2", type=sqls_Tag, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
enums3: BinaryAssociation = BinaryAssociation(
    name="enums3",
    ends={
        Property(name="sqls_Type", type=sqls_SqlLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlLibrary4", type=sqls_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
types5: BinaryAssociation = BinaryAssociation(
    name="types5",
    ends={
        Property(name="sqls_Type7", type=sqls_SqlLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlLibrary6", type=sqls_Type, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
triggers10: BinaryAssociation = BinaryAssociation(
    name="triggers10",
    ends={
        Property(name="sqls_Trigger", type=sqls_SqlLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlLibrary11", type=sqls_Trigger, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
methods12: BinaryAssociation = BinaryAssociation(
    name="methods12",
    ends={
        Property(name="sqls_SqlMethod", type=sqls_SqlLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlLibrary13", type=sqls_SqlMethod, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type14: BinaryAssociation = BinaryAssociation(
    name="type14",
    ends={
        Property(name="sqls_Type15", type=sqls_SqlType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlType", type=sqls_Type, multiplicity=Multiplicity(0, 1))
    }
)
params16: BinaryAssociation = BinaryAssociation(
    name="params16",
    ends={
        Property(name="sqls_SqlExpr", type=sqls_SqlType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlType17", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tags18: BinaryAssociation = BinaryAssociation(
    name="tags18",
    ends={
        Property(name="sqls_Tag20", type=sqls_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Table19", type=sqls_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
columns31: BinaryAssociation = BinaryAssociation(
    name="columns31",
    ends={
        Property(name="sqls_Column32", type=sqls_UniqueTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_UniqueTableConstraint", type=sqls_Column, multiplicity=Multiplicity(0, 9999))
    }
)
fields21: BinaryAssociation = BinaryAssociation(
    name="fields21",
    ends={
        Property(name="sqls_Column", type=sqls_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Table22", type=sqls_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
constraints23: BinaryAssociation = BinaryAssociation(
    name="constraints23",
    ends={
        Property(name="sqls_TableConstraint", type=sqls_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Table24", type=sqls_TableConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type25: BinaryAssociation = BinaryAssociation(
    name="type25",
    ends={
        Property(name="sqls_SqlType27", type=sqls_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Column26", type=sqls_SqlType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
defaultValue28: BinaryAssociation = BinaryAssociation(
    name="defaultValue28",
    ends={
        Property(name="sqls_SqlExpr30", type=sqls_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Column29", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
resultColumns45: BinaryAssociation = BinaryAssociation(
    name="resultColumns45",
    ends={
        Property(name="sqls_SelectList", type=sqls_ResultColumn, multiplicity=Multiplicity(0, 9999), is_composite=True),
        Property(name="sqls_ResultColumn46", type=sqls_SelectList, multiplicity=Multiplicity(1, 1))
    }
)
tags33: BinaryAssociation = BinaryAssociation(
    name="tags33",
    ends={
        Property(name="sqls_Tag35", type=sqls_SqlMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlMethod34", type=sqls_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
type36: BinaryAssociation = BinaryAssociation(
    name="type36",
    ends={
        Property(name="sqls_Table38", type=sqls_SqlMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlMethod37", type=sqls_Table, multiplicity=Multiplicity(0, 1))
    }
)
sql39: BinaryAssociation = BinaryAssociation(
    name="sql39",
    ends={
        Property(name="sqls_SqlSentence", type=sqls_SqlMethod, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlMethod40", type=sqls_SqlSentence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
expression41: BinaryAssociation = BinaryAssociation(
    name="expression41",
    ends={
        Property(name="sqls_SqlExpr42", type=sqls_OrderingTerm, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_OrderingTerm", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
expression43: BinaryAssociation = BinaryAssociation(
    name="expression43",
    ends={
        Property(name="sqls_SqlExpr44", type=sqls_ResultColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_ResultColumn", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
selectList47: BinaryAssociation = BinaryAssociation(
    name="selectList47",
    ends={
        Property(name="sqls_SelectList48", type=sqls_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Select", type=sqls_SelectList, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
from_49: BinaryAssociation = BinaryAssociation(
    name="from_49",
    ends={
        Property(name="sqls_TableRef", type=sqls_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Select50", type=sqls_TableRef, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
where51: BinaryAssociation = BinaryAssociation(
    name="where51",
    ends={
        Property(name="sqls_SqlExpr53", type=sqls_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Select52", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
orderingTerms54: BinaryAssociation = BinaryAssociation(
    name="orderingTerms54",
    ends={
        Property(name="sqls_OrderingTerm56", type=sqls_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Select55", type=sqls_OrderingTerm, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
limit57: BinaryAssociation = BinaryAssociation(
    name="limit57",
    ends={
        Property(name="sqls_SqlExpr59", type=sqls_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Select58", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
limitOffset60: BinaryAssociation = BinaryAssociation(
    name="limitOffset60",
    ends={
        Property(name="sqls_SqlExpr62", type=sqls_Select, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Select61", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table63: BinaryAssociation = BinaryAssociation(
    name="table63",
    ends={
        Property(name="sqls_Table65", type=sqls_TableRef, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_TableRef64", type=sqls_Table, multiplicity=Multiplicity(0, 1))
    }
)
table80: BinaryAssociation = BinaryAssociation(
    name="table80",
    ends={
        Property(name="sqls_Delete", type=sqls_Table, multiplicity=Multiplicity(0, 1)),
        Property(name="sqls_Table81", type=sqls_Delete, multiplicity=Multiplicity(1, 1))
    }
)
where82: BinaryAssociation = BinaryAssociation(
    name="where82",
    ends={
        Property(name="sqls_SqlExpr84", type=sqls_Delete, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Delete83", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
function66: BinaryAssociation = BinaryAssociation(
    name="function66",
    ends={
        Property(name="sqls_Function", type=sqls_SqlFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlFunction", type=sqls_Function, multiplicity=Multiplicity(0, 1))
    }
)
params67: BinaryAssociation = BinaryAssociation(
    name="params67",
    ends={
        Property(name="sqls_SqlExpr69", type=sqls_SqlFunction, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlFunction68", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table70: BinaryAssociation = BinaryAssociation(
    name="table70",
    ends={
        Property(name="sqls_Table71", type=sqls_Insert, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Insert", type=sqls_Table, multiplicity=Multiplicity(0, 1))
    }
)
table72: BinaryAssociation = BinaryAssociation(
    name="table72",
    ends={
        Property(name="sqls_Table73", type=sqls_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_InsertStatement", type=sqls_Table, multiplicity=Multiplicity(0, 1))
    }
)
columns74: BinaryAssociation = BinaryAssociation(
    name="columns74",
    ends={
        Property(name="sqls_Column76", type=sqls_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_InsertStatement75", type=sqls_Column, multiplicity=Multiplicity(0, 9999))
    }
)
expressions77: BinaryAssociation = BinaryAssociation(
    name="expressions77",
    ends={
        Property(name="sqls_SqlExpr79", type=sqls_InsertStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_InsertStatement78", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table85: BinaryAssociation = BinaryAssociation(
    name="table85",
    ends={
        Property(name="sqls_Table86", type=sqls_Update, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Update", type=sqls_Table, multiplicity=Multiplicity(0, 1))
    }
)
updateColumnExpressions87: BinaryAssociation = BinaryAssociation(
    name="updateColumnExpressions87",
    ends={
        Property(name="sqls_UpdateColumnExpression", type=sqls_Update, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Update88", type=sqls_UpdateColumnExpression, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
where89: BinaryAssociation = BinaryAssociation(
    name="where89",
    ends={
        Property(name="sqls_SqlExpr91", type=sqls_Update, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Update90", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column92: BinaryAssociation = BinaryAssociation(
    name="column92",
    ends={
        Property(name="sqls_Column94", type=sqls_UpdateColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_UpdateColumnExpression93", type=sqls_Column, multiplicity=Multiplicity(0, 1))
    }
)
expression95: BinaryAssociation = BinaryAssociation(
    name="expression95",
    ends={
        Property(name="sqls_SqlExpr97", type=sqls_UpdateColumnExpression, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_UpdateColumnExpression96", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table98: BinaryAssociation = BinaryAssociation(
    name="table98",
    ends={
        Property(name="sqls_Table99", type=sqls_Get, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Get", type=sqls_Table, multiplicity=Multiplicity(0, 1))
    }
)
tags100: BinaryAssociation = BinaryAssociation(
    name="tags100",
    ends={
        Property(name="sqls_Tag102", type=sqls_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Trigger101", type=sqls_Tag, multiplicity=Multiplicity(0, 9999))
    }
)
action103: BinaryAssociation = BinaryAssociation(
    name="action103",
    ends={
        Property(name="sqls_TriggerAction", type=sqls_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Trigger104", type=sqls_TriggerAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table105: BinaryAssociation = BinaryAssociation(
    name="table105",
    ends={
        Property(name="sqls_Table107", type=sqls_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Trigger106", type=sqls_Table, multiplicity=Multiplicity(0, 1))
    }
)
sqls108: BinaryAssociation = BinaryAssociation(
    name="sqls108",
    ends={
        Property(name="sqls_SqlSentence110", type=sqls_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Trigger109", type=sqls_SqlSentence, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
elements111: BinaryAssociation = BinaryAssociation(
    name="elements111",
    ends={
        Property(name="sqls_EnumElement", type=sqls_Enum, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_Enum", type=sqls_EnumElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
sqlType112: BinaryAssociation = BinaryAssociation(
    name="sqlType112",
    ends={
        Property(name="sqls_SqlType113", type=sqls_TypeDef, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_TypeDef", type=sqls_SqlType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
tableRef125: BinaryAssociation = BinaryAssociation(
    name="tableRef125",
    ends={
        Property(name="sqls_TableRef126", type=sqls_ColumnRef, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_ColumnRef", type=sqls_TableRef, multiplicity=Multiplicity(0, 1))
    }
)
left114: BinaryAssociation = BinaryAssociation(
    name="left114",
    ends={
        Property(name="sqls_SqlExpr115", type=sqls_SqlBinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlBinaryExpr", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
right116: BinaryAssociation = BinaryAssociation(
    name="right116",
    ends={
        Property(name="sqls_SqlExpr118", type=sqls_SqlBinaryExpr, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlBinaryExpr117", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
column119: BinaryAssociation = BinaryAssociation(
    name="column119",
    ends={
        Property(name="sqls_Column120", type=sqls_NewColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_NewColumn", type=sqls_Column, multiplicity=Multiplicity(0, 1))
    }
)
column121: BinaryAssociation = BinaryAssociation(
    name="column121",
    ends={
        Property(name="sqls_Column122", type=sqls_OldColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_OldColumn", type=sqls_Column, multiplicity=Multiplicity(0, 1))
    }
)
expression123: BinaryAssociation = BinaryAssociation(
    name="expression123",
    ends={
        Property(name="sqls_SqlExpr124", type=sqls_SqlNested, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlNested", type=sqls_SqlExpr, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table132: BinaryAssociation = BinaryAssociation(
    name="table132",
    ends={
        Property(name="sqls_DeleteTable", type=sqls_Table, multiplicity=Multiplicity(0, 1)),
        Property(name="sqls_Table133", type=sqls_DeleteTable, multiplicity=Multiplicity(1, 1))
    }
)
column127: BinaryAssociation = BinaryAssociation(
    name="column127",
    ends={
        Property(name="sqls_Column129", type=sqls_ColumnRef, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_ColumnRef128", type=sqls_Column, multiplicity=Multiplicity(0, 1))
    }
)
method130: BinaryAssociation = BinaryAssociation(
    name="method130",
    ends={
        Property(name="sqls_SqlMethod131", type=sqls_SqlMethodRef, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_SqlMethodRef", type=sqls_SqlMethod, multiplicity=Multiplicity(0, 1))
    }
)
columns134: BinaryAssociation = BinaryAssociation(
    name="columns134",
    ends={
        Property(name="sqls_Column135", type=sqls_TriggerUpdate, multiplicity=Multiplicity(1, 1)),
        Property(name="sqls_TriggerUpdate", type=sqls_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_sqls_UniqueTableConstraint_TableConstraint = Generalization(general=TableConstraint, specific=sqls_UniqueTableConstraint)
gen_sqls_Select_SqlSentence = Generalization(general=SqlSentence, specific=sqls_Select)
gen_sqls_SqlFunction_SqlExpr = Generalization(general=SqlExpr, specific=sqls_SqlFunction)
gen_sqls_Insert_SqlSentence = Generalization(general=SqlSentence, specific=sqls_Insert)
gen_sqls_InsertStatement_SqlSentence = Generalization(general=SqlSentence, specific=sqls_InsertStatement)
gen_sqls_Delete_SqlSentence = Generalization(general=SqlSentence, specific=sqls_Delete)
gen_sqls_Update_SqlSentence = Generalization(general=SqlSentence, specific=sqls_Update)
gen_sqls_Get_SqlSentence = Generalization(general=SqlSentence, specific=sqls_Get)
gen_sqls_SqlBinaryExpr_SqlExpr = Generalization(general=SqlExpr, specific=sqls_SqlBinaryExpr)
gen_sqls_Enum_Type = Generalization(general=Type, specific=sqls_Enum)
gen_sqls_TypeDef_Type = Generalization(general=Type, specific=sqls_TypeDef)
gen_sqls_SqlPlaceholder_SqlExpr = Generalization(general=SqlExpr, specific=sqls_SqlPlaceholder)
gen_sqls_NewColumn_SqlExpr = Generalization(general=SqlExpr, specific=sqls_NewColumn)
gen_sqls_OldColumn_SqlExpr = Generalization(general=SqlExpr, specific=sqls_OldColumn)
gen_sqls_SqlNested_SqlExpr = Generalization(general=SqlExpr, specific=sqls_SqlNested)
gen_sqls_ColumnRef_SqlExpr = Generalization(general=SqlExpr, specific=sqls_ColumnRef)
gen_sqls_SqlParam_SqlExpr = Generalization(general=SqlExpr, specific=sqls_SqlParam)
gen_sqls_SqlStringLiteral_SqlExpr = Generalization(general=SqlExpr, specific=sqls_SqlStringLiteral)
gen_sqls_SqlNumberLiteral_SqlExpr = Generalization(general=SqlExpr, specific=sqls_SqlNumberLiteral)
gen_sqls_SqlMethodRef_SqlSentence = Generalization(general=SqlSentence, specific=sqls_SqlMethodRef)
gen_sqls_DeleteTable_SqlSentence = Generalization(general=SqlSentence, specific=sqls_DeleteTable)
gen_sqls_TriggerInsert_TriggerAction = Generalization(general=TriggerAction, specific=sqls_TriggerInsert)
gen_sqls_TriggerDelete_TriggerAction = Generalization(general=TriggerAction, specific=sqls_TriggerDelete)
gen_sqls_TriggerUpdate_TriggerAction = Generalization(general=TriggerAction, specific=sqls_TriggerUpdate)

# Domain Model
domain_model = DomainModel(
    name="sqls",
    types={sqls_SqlLibrary, sqls_Import, sqls_Tag, sqls_Type, sqls_Table, sqls_Column, sqls_Trigger, sqls_SqlMethod, sqls_EnumElement, sqls_SqlType, sqls_SqlExpr, sqls_TableConstraint, sqls_UniqueTableConstraint, TableConstraint, sqls_Select, SqlSentence, sqls_SqlSentence, sqls_OrderingTerm, sqls_ResultColumn, sqls_SelectList, sqls_SqlFunction, SqlExpr, sqls_Function, sqls_TableRef, sqls_Insert, sqls_InsertStatement, sqls_Delete, sqls_Update, sqls_UpdateColumnExpression, sqls_Get, sqls_SqlBinaryExpr, sqls_TriggerAction, sqls_Enum, Type, sqls_TypeDef, sqls_SqlPlaceholder, sqls_NewColumn, sqls_OldColumn, sqls_SqlNested, sqls_ColumnRef, sqls_SqlParam, sqls_SqlStringLiteral, sqls_SqlNumberLiteral, sqls_SqlMethodRef, sqls_DeleteTable, sqls_TriggerInsert, TriggerAction, sqls_TriggerDelete, sqls_TriggerUpdate, TriggerTime},
    associations={tables8, imports0, tags1, enums3, types5, triggers10, methods12, type14, params16, tags18, columns31, fields21, constraints23, type25, defaultValue28, resultColumns45, tags33, type36, sql39, expression41, expression43, selectList47, from_49, where51, orderingTerms54, limit57, limitOffset60, table63, table80, where82, function66, params67, table70, table72, columns74, expressions77, table85, updateColumnExpressions87, where89, column92, expression95, table98, tags100, action103, table105, sqls108, elements111, sqlType112, tableRef125, left114, right116, column119, column121, expression123, table132, column127, method130, columns134},
    generalizations={gen_sqls_UniqueTableConstraint_TableConstraint, gen_sqls_Select_SqlSentence, gen_sqls_SqlFunction_SqlExpr, gen_sqls_Insert_SqlSentence, gen_sqls_InsertStatement_SqlSentence, gen_sqls_Delete_SqlSentence, gen_sqls_Update_SqlSentence, gen_sqls_Get_SqlSentence, gen_sqls_SqlBinaryExpr_SqlExpr, gen_sqls_Enum_Type, gen_sqls_TypeDef_Type, gen_sqls_SqlPlaceholder_SqlExpr, gen_sqls_NewColumn_SqlExpr, gen_sqls_OldColumn_SqlExpr, gen_sqls_SqlNested_SqlExpr, gen_sqls_ColumnRef_SqlExpr, gen_sqls_SqlParam_SqlExpr, gen_sqls_SqlStringLiteral_SqlExpr, gen_sqls_SqlNumberLiteral_SqlExpr, gen_sqls_SqlMethodRef_SqlSentence, gen_sqls_DeleteTable_SqlSentence, gen_sqls_TriggerInsert_TriggerAction, gen_sqls_TriggerDelete_TriggerAction, gen_sqls_TriggerUpdate_TriggerAction},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)