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
NullableType: Enumeration = Enumeration(
    name="NullableType",
    literals={
            EnumerationLiteral(name="NO_NULLS"),
			EnumerationLiteral(name="NULLABLE"),
			EnumerationLiteral(name="NULLABLE_UNKNOWN")
    }
)

SearchabilityType: Enumeration = Enumeration(
    name="SearchabilityType",
    literals={
            EnumerationLiteral(name="SEARCHABLE"),
			EnumerationLiteral(name="ALL_EXCEPT_LIKE"),
			EnumerationLiteral(name="LIKE_ONLY"),
			EnumerationLiteral(name="UNSEARCHABLE")
    }
)

DirectionKind: Enumeration = Enumeration(
    name="DirectionKind",
    literals={
            EnumerationLiteral(name="IN"),
			EnumerationLiteral(name="OUT"),
			EnumerationLiteral(name="INOUT"),
			EnumerationLiteral(name="RETURN"),
			EnumerationLiteral(name="UNKNOWN")
    }
)

MultiplicityKind: Enumeration = Enumeration(
    name="MultiplicityKind",
    literals={
            EnumerationLiteral(name="UNSPECIFIED"),
			EnumerationLiteral(name="ONE"),
			EnumerationLiteral(name="MANY"),
			EnumerationLiteral(name="ZERO_TO_ONE"),
			EnumerationLiteral(name="ZERO_TO_MANY")
    }
)

ProcedureUpdateCount: Enumeration = Enumeration(
    name="ProcedureUpdateCount",
    literals={
            EnumerationLiteral(name="AUTO"),
			EnumerationLiteral(name="ZERO"),
			EnumerationLiteral(name="ONE"),
			EnumerationLiteral(name="MULTIPLE")
    }
)

# Classes
relational_Table = Class(name="relational_Table", is_abstract=True)
ColumnSet = Class(name="ColumnSet")
relational_Schema = Class(name="relational_Schema")
relational_AccessPattern = Class(name="relational_AccessPattern")
relational_Catalog = Class(name="relational_Catalog")
relational_LogicalRelationshipEnd = Class(name="relational_LogicalRelationshipEnd")
relational_Column = Class(name="relational_Column")
RelationalEntity = Class(name="RelationalEntity")
relational_Procedure = Class(name="relational_Procedure")
relational_UniqueKey = Class(name="relational_UniqueKey", is_abstract=True)
relational_Index = Class(name="relational_Index")
relational_ForeignKey = Class(name="relational_ForeignKey")
relational_ColumnSet = Class(name="relational_ColumnSet", is_abstract=True)
relational_EObject = Class(name="relational_EObject")
relational_LogicalRelationship = Class(name="relational_LogicalRelationship")
relational_PrimaryKey = Class(name="relational_PrimaryKey")
UniqueKey = Class(name="UniqueKey")
relational_BaseTable = Class(name="relational_BaseTable")
Relationship = Class(name="Relationship")
relational_RelationalEntity = Class(name="relational_RelationalEntity", is_abstract=True)
relational_View = Class(name="relational_View")
Table = Class(name="Table")
relational_ProcedureParameter = Class(name="relational_ProcedureParameter")
relational_ProcedureResult = Class(name="relational_ProcedureResult")
relational_Relationship = Class(name="relational_Relationship", is_abstract=True)
relational_UniqueConstraint = Class(name="relational_UniqueConstraint")

# relational_Table class attributes and methods
relational_Table_system: Property = Property(name="system", type=BooleanType)
relational_Table_cardinality: Property = Property(name="cardinality", type=IntegerType)
relational_Table_supportsUpdate: Property = Property(name="supportsUpdate", type=BooleanType)
relational_Table_materialized: Property = Property(name="materialized", type=BooleanType)
relational_Table.attributes={relational_Table_supportsUpdate, relational_Table_system, relational_Table_materialized, relational_Table_cardinality}

# ColumnSet class attributes and methods

# relational_Schema class attributes and methods

# relational_AccessPattern class attributes and methods

# relational_Catalog class attributes and methods

# relational_LogicalRelationshipEnd class attributes and methods
relational_LogicalRelationshipEnd_multiplicity: Property = Property(name="multiplicity", type=StringType)
relational_LogicalRelationshipEnd.attributes={relational_LogicalRelationshipEnd_multiplicity}

# relational_Column class attributes and methods
relational_Column_nullable: Property = Property(name="nullable", type=StringType)
relational_Column_autoIncremented: Property = Property(name="autoIncremented", type=BooleanType)
relational_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
relational_Column_minimumValue: Property = Property(name="minimumValue", type=StringType)
relational_Column_maximumValue: Property = Property(name="maximumValue", type=StringType)
relational_Column_format: Property = Property(name="format", type=StringType)
relational_Column_nativeType: Property = Property(name="nativeType", type=StringType)
relational_Column_length: Property = Property(name="length", type=IntegerType)
relational_Column_fixedLength: Property = Property(name="fixedLength", type=BooleanType)
relational_Column_precision: Property = Property(name="precision", type=IntegerType)
relational_Column_scale: Property = Property(name="scale", type=IntegerType)
relational_Column_characterSetName: Property = Property(name="characterSetName", type=StringType)
relational_Column_collationName: Property = Property(name="collationName", type=StringType)
relational_Column_selectable: Property = Property(name="selectable", type=BooleanType)
relational_Column_updateable: Property = Property(name="updateable", type=BooleanType)
relational_Column_caseSensitive: Property = Property(name="caseSensitive", type=BooleanType)
relational_Column_searchability: Property = Property(name="searchability", type=StringType)
relational_Column_currency: Property = Property(name="currency", type=BooleanType)
relational_Column_radix: Property = Property(name="radix", type=IntegerType)
relational_Column_signed: Property = Property(name="signed", type=BooleanType)
relational_Column_distinctValueCount: Property = Property(name="distinctValueCount", type=IntegerType)
relational_Column_nullValueCount: Property = Property(name="nullValueCount", type=IntegerType)
relational_Column.attributes={relational_Column_autoIncremented, relational_Column_length, relational_Column_caseSensitive, relational_Column_format, relational_Column_signed, relational_Column_collationName, relational_Column_nullable, relational_Column_nullValueCount, relational_Column_updateable, relational_Column_searchability, relational_Column_radix, relational_Column_selectable, relational_Column_minimumValue, relational_Column_maximumValue, relational_Column_defaultValue, relational_Column_distinctValueCount, relational_Column_currency, relational_Column_nativeType, relational_Column_precision, relational_Column_characterSetName, relational_Column_fixedLength, relational_Column_scale}

# RelationalEntity class attributes and methods

# relational_Procedure class attributes and methods
relational_Procedure_function: Property = Property(name="function", type=BooleanType)
relational_Procedure_updateCount: Property = Property(name="updateCount", type=StringType)
relational_Procedure.attributes={relational_Procedure_updateCount, relational_Procedure_function}

# relational_UniqueKey class attributes and methods
relational_UniqueKey_m_getTable: Method = Method(name="getTable", parameters={}, type=StringType)
relational_UniqueKey.methods={relational_UniqueKey_m_getTable}

# relational_Index class attributes and methods
relational_Index_filterCondition: Property = Property(name="filterCondition", type=StringType)
relational_Index_nullable: Property = Property(name="nullable", type=BooleanType)
relational_Index_autoUpdate: Property = Property(name="autoUpdate", type=BooleanType)
relational_Index_unique: Property = Property(name="unique", type=BooleanType)
relational_Index.attributes={relational_Index_filterCondition, relational_Index_autoUpdate, relational_Index_unique, relational_Index_nullable}

# relational_ForeignKey class attributes and methods
relational_ForeignKey_foreignKeyMultiplicity: Property = Property(name="foreignKeyMultiplicity", type=StringType)
relational_ForeignKey_primaryKeyMultiplicity: Property = Property(name="primaryKeyMultiplicity", type=StringType)
relational_ForeignKey.attributes={relational_ForeignKey_foreignKeyMultiplicity, relational_ForeignKey_primaryKeyMultiplicity}

# relational_ColumnSet class attributes and methods

# relational_EObject class attributes and methods

# relational_LogicalRelationship class attributes and methods

# relational_PrimaryKey class attributes and methods

# UniqueKey class attributes and methods

# relational_BaseTable class attributes and methods

# Relationship class attributes and methods

# relational_RelationalEntity class attributes and methods
relational_RelationalEntity_name: Property = Property(name="name", type=StringType)
relational_RelationalEntity_nameInSource: Property = Property(name="nameInSource", type=StringType)
relational_RelationalEntity.attributes={relational_RelationalEntity_name, relational_RelationalEntity_nameInSource}

# relational_View class attributes and methods

# Table class attributes and methods

# relational_ProcedureParameter class attributes and methods
relational_ProcedureParameter_direction: Property = Property(name="direction", type=StringType)
relational_ProcedureParameter_defaultValue: Property = Property(name="defaultValue", type=StringType)
relational_ProcedureParameter_nativeType: Property = Property(name="nativeType", type=StringType)
relational_ProcedureParameter_length: Property = Property(name="length", type=IntegerType)
relational_ProcedureParameter_precision: Property = Property(name="precision", type=IntegerType)
relational_ProcedureParameter_scale: Property = Property(name="scale", type=IntegerType)
relational_ProcedureParameter_nullable: Property = Property(name="nullable", type=StringType)
relational_ProcedureParameter_radix: Property = Property(name="radix", type=IntegerType)
relational_ProcedureParameter.attributes={relational_ProcedureParameter_defaultValue, relational_ProcedureParameter_length, relational_ProcedureParameter_nativeType, relational_ProcedureParameter_nullable, relational_ProcedureParameter_precision, relational_ProcedureParameter_direction, relational_ProcedureParameter_scale, relational_ProcedureParameter_radix}

# relational_ProcedureResult class attributes and methods

# relational_Relationship class attributes and methods

# relational_UniqueConstraint class attributes and methods

# Relationships
schema0: BinaryAssociation = BinaryAssociation(
    name="schema0",
    ends={
        Property(name="Schema", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=relational_Schema, multiplicity=Multiplicity(0, 1))
    }
)
accessPatterns1: BinaryAssociation = BinaryAssociation(
    name="accessPatterns1",
    ends={
        Property(name="AccessPattern", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=relational_AccessPattern, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog2: BinaryAssociation = BinaryAssociation(
    name="catalog2",
    ends={
        Property(name="Catalog", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables3", type=relational_Catalog, multiplicity=Multiplicity(0, 1))
    }
)
logicalRelationships4: BinaryAssociation = BinaryAssociation(
    name="logicalRelationships4",
    ends={
        Property(name="LogicalRelationshipEnd", type=relational_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table5", type=relational_LogicalRelationshipEnd, multiplicity=Multiplicity(0, 9999))
    }
)
procedures20: BinaryAssociation = BinaryAssociation(
    name="procedures20",
    ends={
        Property(name="Procedure", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema21", type=relational_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
uniqueKeys6: BinaryAssociation = BinaryAssociation(
    name="uniqueKeys6",
    ends={
        Property(name="UniqueKey", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=relational_UniqueKey, multiplicity=Multiplicity(0, 9999))
    }
)
indexes7: BinaryAssociation = BinaryAssociation(
    name="indexes7",
    ends={
        Property(name="Index", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns8", type=relational_Index, multiplicity=Multiplicity(0, 9999))
    }
)
foreignKeys9: BinaryAssociation = BinaryAssociation(
    name="foreignKeys9",
    ends={
        Property(name="ForeignKey", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns10", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
accessPatterns11: BinaryAssociation = BinaryAssociation(
    name="accessPatterns11",
    ends={
        Property(name="AccessPattern13", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns12", type=relational_AccessPattern, multiplicity=Multiplicity(0, 9999))
    }
)
owner14: BinaryAssociation = BinaryAssociation(
    name="owner14",
    ends={
        Property(name="ColumnSet", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns15", type=relational_ColumnSet, multiplicity=Multiplicity(0, 1))
    }
)
type16: BinaryAssociation = BinaryAssociation(
    name="type16",
    ends={
        Property(name="relational_EObject", type=relational_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_Column", type=relational_EObject, multiplicity=Multiplicity(1, 1))
    }
)
tables17: BinaryAssociation = BinaryAssociation(
    name="tables17",
    ends={
        Property(name="Table", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema", type=relational_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog18: BinaryAssociation = BinaryAssociation(
    name="catalog18",
    ends={
        Property(name="Catalog19", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schemas", type=relational_Catalog, multiplicity=Multiplicity(0, 1))
    }
)
indexes22: BinaryAssociation = BinaryAssociation(
    name="indexes22",
    ends={
        Property(name="Index24", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema23", type=relational_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalRelationships25: BinaryAssociation = BinaryAssociation(
    name="logicalRelationships25",
    ends={
        Property(name="LogicalRelationship", type=relational_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="schema26", type=relational_LogicalRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table27: BinaryAssociation = BinaryAssociation(
    name="table27",
    ends={
        Property(name="BaseTable", type=relational_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="primaryKey", type=relational_BaseTable, multiplicity=Multiplicity(0, 1))
    }
)
columns28: BinaryAssociation = BinaryAssociation(
    name="columns28",
    ends={
        Property(name="Column", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
uniqueKey29: BinaryAssociation = BinaryAssociation(
    name="uniqueKey29",
    ends={
        Property(name="UniqueKey31", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys30", type=relational_UniqueKey, multiplicity=Multiplicity(1, 1))
    }
)
table32: BinaryAssociation = BinaryAssociation(
    name="table32",
    ends={
        Property(name="BaseTable34", type=relational_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="foreignKeys33", type=relational_BaseTable, multiplicity=Multiplicity(0, 1))
    }
)
columns35: BinaryAssociation = BinaryAssociation(
    name="columns35",
    ends={
        Property(name="Column36", type=relational_UniqueKey, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueKeys", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
foreignKeys37: BinaryAssociation = BinaryAssociation(
    name="foreignKeys37",
    ends={
        Property(name="ForeignKey38", type=relational_UniqueKey, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueKey", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999))
    }
)
columns63: BinaryAssociation = BinaryAssociation(
    name="columns63",
    ends={
        Property(name="Column65", type=relational_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes64", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
catalog66: BinaryAssociation = BinaryAssociation(
    name="catalog66",
    ends={
        Property(name="Catalog68", type=relational_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes67", type=relational_Catalog, multiplicity=Multiplicity(0, 1))
    }
)
schemas39: BinaryAssociation = BinaryAssociation(
    name="schemas39",
    ends={
        Property(name="Schema40", type=relational_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalog", type=relational_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedures41: BinaryAssociation = BinaryAssociation(
    name="procedures41",
    ends={
        Property(name="Procedure43", type=relational_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalog42", type=relational_Procedure, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indexes44: BinaryAssociation = BinaryAssociation(
    name="indexes44",
    ends={
        Property(name="Index46", type=relational_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalog45", type=relational_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables47: BinaryAssociation = BinaryAssociation(
    name="tables47",
    ends={
        Property(name="Table49", type=relational_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalog48", type=relational_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
logicalRelationships50: BinaryAssociation = BinaryAssociation(
    name="logicalRelationships50",
    ends={
        Property(name="LogicalRelationship52", type=relational_Catalog, multiplicity=Multiplicity(1, 1)),
        Property(name="catalog51", type=relational_LogicalRelationship, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
procedure69: BinaryAssociation = BinaryAssociation(
    name="procedure69",
    ends={
        Property(name="Procedure70", type=relational_ProcedureParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="parameters", type=relational_Procedure, multiplicity=Multiplicity(0, 1))
    }
)
type71: BinaryAssociation = BinaryAssociation(
    name="type71",
    ends={
        Property(name="relational_EObject72", type=relational_ProcedureParameter, multiplicity=Multiplicity(1, 1)),
        Property(name="relational_ProcedureParameter", type=relational_EObject, multiplicity=Multiplicity(1, 1))
    }
)
schema53: BinaryAssociation = BinaryAssociation(
    name="schema53",
    ends={
        Property(name="Schema54", type=relational_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="procedures", type=relational_Schema, multiplicity=Multiplicity(0, 1))
    }
)
parameters55: BinaryAssociation = BinaryAssociation(
    name="parameters55",
    ends={
        Property(name="ProcedureParameter", type=relational_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="procedure", type=relational_ProcedureParameter, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
catalog56: BinaryAssociation = BinaryAssociation(
    name="catalog56",
    ends={
        Property(name="Catalog58", type=relational_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="procedures57", type=relational_Catalog, multiplicity=Multiplicity(0, 1))
    }
)
result59: BinaryAssociation = BinaryAssociation(
    name="result59",
    ends={
        Property(name="ProcedureResult", type=relational_Procedure, multiplicity=Multiplicity(1, 1)),
        Property(name="procedure60", type=relational_ProcedureResult, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
schema61: BinaryAssociation = BinaryAssociation(
    name="schema61",
    ends={
        Property(name="Schema62", type=relational_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="indexes", type=relational_Schema, multiplicity=Multiplicity(0, 1))
    }
)
catalog80: BinaryAssociation = BinaryAssociation(
    name="catalog80",
    ends={
        Property(name="Catalog81", type=relational_LogicalRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="logicalRelationships", type=relational_Catalog, multiplicity=Multiplicity(0, 1))
    }
)
schema82: BinaryAssociation = BinaryAssociation(
    name="schema82",
    ends={
        Property(name="Schema84", type=relational_LogicalRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="logicalRelationships83", type=relational_Schema, multiplicity=Multiplicity(0, 1))
    }
)
ends85: BinaryAssociation = BinaryAssociation(
    name="ends85",
    ends={
        Property(name="LogicalRelationshipEnd86", type=relational_LogicalRelationship, multiplicity=Multiplicity(1, 1)),
        Property(name="relationship", type=relational_LogicalRelationshipEnd, multiplicity=Multiplicity(2, 9999), is_composite=True)
    }
)
table87: BinaryAssociation = BinaryAssociation(
    name="table87",
    ends={
        Property(name="Table89", type=relational_LogicalRelationshipEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="logicalRelationships88", type=relational_Table, multiplicity=Multiplicity(1, 1))
    }
)
relationship90: BinaryAssociation = BinaryAssociation(
    name="relationship90",
    ends={
        Property(name="LogicalRelationship91", type=relational_LogicalRelationshipEnd, multiplicity=Multiplicity(1, 1)),
        Property(name="ends", type=relational_LogicalRelationship, multiplicity=Multiplicity(1, 1))
    }
)
table73: BinaryAssociation = BinaryAssociation(
    name="table73",
    ends={
        Property(name="BaseTable74", type=relational_UniqueConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="uniqueConstraints", type=relational_BaseTable, multiplicity=Multiplicity(0, 1))
    }
)
columns75: BinaryAssociation = BinaryAssociation(
    name="columns75",
    ends={
        Property(name="Column76", type=relational_AccessPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="accessPatterns", type=relational_Column, multiplicity=Multiplicity(1, 9999))
    }
)
table77: BinaryAssociation = BinaryAssociation(
    name="table77",
    ends={
        Property(name="Table79", type=relational_AccessPattern, multiplicity=Multiplicity(1, 1)),
        Property(name="accessPatterns78", type=relational_Table, multiplicity=Multiplicity(0, 1))
    }
)
procedure101: BinaryAssociation = BinaryAssociation(
    name="procedure101",
    ends={
        Property(name="Procedure102", type=relational_ProcedureResult, multiplicity=Multiplicity(1, 1)),
        Property(name="result", type=relational_Procedure, multiplicity=Multiplicity(0, 1))
    }
)
foreignKeys92: BinaryAssociation = BinaryAssociation(
    name="foreignKeys92",
    ends={
        Property(name="ForeignKey94", type=relational_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table93", type=relational_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey95: BinaryAssociation = BinaryAssociation(
    name="primaryKey95",
    ends={
        Property(name="PrimaryKey", type=relational_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table96", type=relational_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uniqueConstraints97: BinaryAssociation = BinaryAssociation(
    name="uniqueConstraints97",
    ends={
        Property(name="UniqueConstraint", type=relational_BaseTable, multiplicity=Multiplicity(1, 1)),
        Property(name="table98", type=relational_UniqueConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns99: BinaryAssociation = BinaryAssociation(
    name="columns99",
    ends={
        Property(name="Column100", type=relational_ColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=relational_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_relational_Table_ColumnSet = Generalization(general=ColumnSet, specific=relational_Table)
gen_relational_Column_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Column)
gen_relational_Schema_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Schema)
gen_relational_Catalog_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Catalog)
gen_relational_PrimaryKey_UniqueKey = Generalization(general=UniqueKey, specific=relational_PrimaryKey)
gen_relational_ForeignKey_Relationship = Generalization(general=Relationship, specific=relational_ForeignKey)
gen_relational_UniqueKey_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_UniqueKey)
gen_relational_View_Table = Generalization(general=Table, specific=relational_View)
gen_relational_ProcedureParameter_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_ProcedureParameter)
gen_relational_Procedure_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Procedure)
gen_relational_Index_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Index)
gen_relational_Relationship_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_Relationship)
gen_relational_LogicalRelationship_Relationship = Generalization(general=Relationship, specific=relational_LogicalRelationship)
gen_relational_LogicalRelationshipEnd_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_LogicalRelationshipEnd)
gen_relational_UniqueConstraint_UniqueKey = Generalization(general=UniqueKey, specific=relational_UniqueConstraint)
gen_relational_AccessPattern_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_AccessPattern)
gen_relational_BaseTable_Table = Generalization(general=Table, specific=relational_BaseTable)
gen_relational_ColumnSet_RelationalEntity = Generalization(general=RelationalEntity, specific=relational_ColumnSet)
gen_relational_ProcedureResult_ColumnSet = Generalization(general=ColumnSet, specific=relational_ProcedureResult)

# Domain Model
domain_model = DomainModel(
    name="relational",
    types={relational_Table, ColumnSet, relational_Schema, relational_AccessPattern, relational_Catalog, relational_LogicalRelationshipEnd, relational_Column, RelationalEntity, relational_Procedure, relational_UniqueKey, relational_Index, relational_ForeignKey, relational_ColumnSet, relational_EObject, relational_LogicalRelationship, relational_PrimaryKey, UniqueKey, relational_BaseTable, Relationship, relational_RelationalEntity, relational_View, Table, relational_ProcedureParameter, relational_ProcedureResult, relational_Relationship, relational_UniqueConstraint, NullableType, SearchabilityType, DirectionKind, MultiplicityKind, ProcedureUpdateCount},
    associations={schema0, accessPatterns1, catalog2, logicalRelationships4, procedures20, uniqueKeys6, indexes7, foreignKeys9, accessPatterns11, owner14, type16, tables17, catalog18, indexes22, logicalRelationships25, table27, columns28, uniqueKey29, table32, columns35, foreignKeys37, columns63, catalog66, schemas39, procedures41, indexes44, tables47, logicalRelationships50, procedure69, type71, schema53, parameters55, catalog56, result59, schema61, catalog80, schema82, ends85, table87, relationship90, table73, columns75, table77, procedure101, foreignKeys92, primaryKey95, uniqueConstraints97, columns99},
    generalizations={gen_relational_Table_ColumnSet, gen_relational_Column_RelationalEntity, gen_relational_Schema_RelationalEntity, gen_relational_Catalog_RelationalEntity, gen_relational_PrimaryKey_UniqueKey, gen_relational_ForeignKey_Relationship, gen_relational_UniqueKey_RelationalEntity, gen_relational_View_Table, gen_relational_ProcedureParameter_RelationalEntity, gen_relational_Procedure_RelationalEntity, gen_relational_Index_RelationalEntity, gen_relational_Relationship_RelationalEntity, gen_relational_LogicalRelationship_Relationship, gen_relational_LogicalRelationshipEnd_RelationalEntity, gen_relational_UniqueConstraint_UniqueKey, gen_relational_AccessPattern_RelationalEntity, gen_relational_BaseTable_Table, gen_relational_ColumnSet_RelationalEntity, gen_relational_ProcedureResult_ColumnSet},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)