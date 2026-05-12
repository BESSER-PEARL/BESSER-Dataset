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
Column = Class(name="Column")
Table = Class(name="Table")
CWMRelationalData_Column = Class(name="CWMRelationalData_Column")
CWMRelationalData_QueryExpression = Class(name="CWMRelationalData_QueryExpression")
CWMRelationalData_CheckConstraint = Class(name="CWMRelationalData_CheckConstraint")
CWMRelationalData_Table = Class(name="CWMRelationalData_Table")
CWMRelationalData_View = Class(name="CWMRelationalData_View")
CheckConstraint = Class(name="CheckConstraint")
SQLDataType = Class(name="SQLDataType")
ColumnSet = Class(name="ColumnSet")
NamedColumnSet = Class(name="NamedColumnSet")
CWMRelationalData_ColumnSet = Class(name="CWMRelationalData_ColumnSet")
CWMRelationalData_NamedColumnSet = Class(name="CWMRelationalData_NamedColumnSet")
Trigger = Class(name="Trigger")
CWMRelationalData_QueryColumnSet = Class(name="CWMRelationalData_QueryColumnSet")
QueryExpression = Class(name="QueryExpression")
CWMRelationalData_Trigger = Class(name="CWMRelationalData_Trigger")
CWMRelationalData_SQLDataType = Class(name="CWMRelationalData_SQLDataType")
CWMRelationalData_SQLDistinctType = Class(name="CWMRelationalData_SQLDistinctType")
SQLSimpleType = Class(name="SQLSimpleType")
CWMRelationalData_SQLSimpleType = Class(name="CWMRelationalData_SQLSimpleType")
SQLDistinctType = Class(name="SQLDistinctType")

# Column class attributes and methods

# Table class attributes and methods

# CWMRelationalData_Column class attributes and methods
CWMRelationalData_Column_precision: Property = Property(name="precision", type=StringType)
CWMRelationalData_Column_scale: Property = Property(name="scale", type=StringType)
CWMRelationalData_Column_isNullable: Property = Property(name="isNullable", type=StringType)
CWMRelationalData_Column_length: Property = Property(name="length", type=StringType)
CWMRelationalData_Column_collectionName: Property = Property(name="collectionName", type=StringType)
CWMRelationalData_Column_characterSetName: Property = Property(name="characterSetName", type=StringType)
CWMRelationalData_Column.attributes={CWMRelationalData_Column_length, CWMRelationalData_Column_scale, CWMRelationalData_Column_collectionName, CWMRelationalData_Column_precision, CWMRelationalData_Column_isNullable, CWMRelationalData_Column_characterSetName}

# CWMRelationalData_QueryExpression class attributes and methods
CWMRelationalData_QueryExpression_expresssion: Property = Property(name="expresssion", type=StringType)
CWMRelationalData_QueryExpression.attributes={CWMRelationalData_QueryExpression_expresssion}

# CWMRelationalData_CheckConstraint class attributes and methods

# CWMRelationalData_Table class attributes and methods
CWMRelationalData_Table_isTemporary: Property = Property(name="isTemporary", type=StringType)
CWMRelationalData_Table_temporaryScope: Property = Property(name="temporaryScope", type=StringType)
CWMRelationalData_Table_isSystem: Property = Property(name="isSystem", type=StringType)
CWMRelationalData_Table.attributes={CWMRelationalData_Table_isSystem, CWMRelationalData_Table_temporaryScope, CWMRelationalData_Table_isTemporary}

# CWMRelationalData_View class attributes and methods
CWMRelationalData_View_isReadOnly: Property = Property(name="isReadOnly", type=StringType)
CWMRelationalData_View_checkOption: Property = Property(name="checkOption", type=StringType)
CWMRelationalData_View.attributes={CWMRelationalData_View_checkOption, CWMRelationalData_View_isReadOnly}

# CheckConstraint class attributes and methods

# SQLDataType class attributes and methods

# ColumnSet class attributes and methods

# NamedColumnSet class attributes and methods

# CWMRelationalData_ColumnSet class attributes and methods

# CWMRelationalData_NamedColumnSet class attributes and methods

# Trigger class attributes and methods

# CWMRelationalData_QueryColumnSet class attributes and methods

# QueryExpression class attributes and methods

# CWMRelationalData_Trigger class attributes and methods

# CWMRelationalData_SQLDataType class attributes and methods
CWMRelationalData_SQLDataType_typeNumber: Property = Property(name="typeNumber", type=StringType)
CWMRelationalData_SQLDataType.attributes={CWMRelationalData_SQLDataType_typeNumber}

# CWMRelationalData_SQLDistinctType class attributes and methods
CWMRelationalData_SQLDistinctType_length: Property = Property(name="length", type=StringType)
CWMRelationalData_SQLDistinctType_precision: Property = Property(name="precision", type=StringType)
CWMRelationalData_SQLDistinctType_scale: Property = Property(name="scale", type=StringType)
CWMRelationalData_SQLDistinctType.attributes={CWMRelationalData_SQLDistinctType_length, CWMRelationalData_SQLDistinctType_precision, CWMRelationalData_SQLDistinctType_scale}

# SQLSimpleType class attributes and methods

# CWMRelationalData_SQLSimpleType class attributes and methods
CWMRelationalData_SQLSimpleType_characterMaximumLength: Property = Property(name="characterMaximumLength", type=StringType)
CWMRelationalData_SQLSimpleType_characterOctetLength: Property = Property(name="characterOctetLength", type=StringType)
CWMRelationalData_SQLSimpleType_numericPrecision: Property = Property(name="numericPrecision", type=StringType)
CWMRelationalData_SQLSimpleType_numericPrecisionRadix: Property = Property(name="numericPrecisionRadix", type=StringType)
CWMRelationalData_SQLSimpleType_numericScale: Property = Property(name="numericScale", type=StringType)
CWMRelationalData_SQLSimpleType_dateTimePrecision: Property = Property(name="dateTimePrecision", type=StringType)
CWMRelationalData_SQLSimpleType.attributes={CWMRelationalData_SQLSimpleType_numericScale, CWMRelationalData_SQLSimpleType_numericPrecisionRadix, CWMRelationalData_SQLSimpleType_characterMaximumLength, CWMRelationalData_SQLSimpleType_characterOctetLength, CWMRelationalData_SQLSimpleType_numericPrecision, CWMRelationalData_SQLSimpleType_dateTimePrecision}

# SQLDistinctType class attributes and methods

# Relationships
constraintElements0: BinaryAssociation = BinaryAssociation(
    name="constraintElements0",
    ends={
        Property(name="Column", type=CWMRelationalData_CheckConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="column_constraints", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
constrainedElements1: BinaryAssociation = BinaryAssociation(
    name="constrainedElements1",
    ends={
        Property(name="Table", type=CWMRelationalData_CheckConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="table_constraints", type=Table, multiplicity=Multiplicity(0, 9999))
    }
)
table_constraints12: BinaryAssociation = BinaryAssociation(
    name="table_constraints12",
    ends={
        Property(name="CheckConstraint13", type=CWMRelationalData_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="constrainedElements", type=CheckConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
column_constraints2: BinaryAssociation = BinaryAssociation(
    name="column_constraints2",
    ends={
        Property(name="CheckConstraint", type=CWMRelationalData_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="constraintElements", type=CheckConstraint, multiplicity=Multiplicity(0, 9999))
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="SQLDataType", type=CWMRelationalData_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="structuralFeatures", type=SQLDataType, multiplicity=Multiplicity(1, 1))
    }
)
owner4: BinaryAssociation = BinaryAssociation(
    name="owner4",
    ends={
        Property(name="ColumnSet", type=CWMRelationalData_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="features", type=ColumnSet, multiplicity=Multiplicity(0, 1))
    }
)
optionScopeColumnSet5: BinaryAssociation = BinaryAssociation(
    name="optionScopeColumnSet5",
    ends={
        Property(name="NamedColumnSet", type=CWMRelationalData_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="optionScopeColumn", type=NamedColumnSet, multiplicity=Multiplicity(0, 1))
    }
)
features6: BinaryAssociation = BinaryAssociation(
    name="features6",
    ends={
        Property(name="Column7", type=CWMRelationalData_ColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
optionScopeColumn8: BinaryAssociation = BinaryAssociation(
    name="optionScopeColumn8",
    ends={
        Property(name="Column9", type=CWMRelationalData_NamedColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="optionScopeColumnSet", type=Column, multiplicity=Multiplicity(1, 1))
    }
)
triggers10: BinaryAssociation = BinaryAssociation(
    name="triggers10",
    ends={
        Property(name="Trigger", type=CWMRelationalData_NamedColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="namedColumnSet", type=Trigger, multiplicity=Multiplicity(0, 9999))
    }
)
query11: BinaryAssociation = BinaryAssociation(
    name="query11",
    ends={
        Property(name="QueryExpression", type=CWMRelationalData_QueryColumnSet, multiplicity=Multiplicity(1, 1)),
        Property(name="CWMRelationalData_QueryColumnSet", type=QueryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
sqlDistinctTypes21: BinaryAssociation = BinaryAssociation(
    name="sqlDistinctTypes21",
    ends={
        Property(name="SQLDistinctType", type=CWMRelationalData_SQLSimpleType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlSimpleType", type=SQLDistinctType, multiplicity=Multiplicity(0, 9999))
    }
)
queryExpression14: BinaryAssociation = BinaryAssociation(
    name="queryExpression14",
    ends={
        Property(name="QueryExpression15", type=CWMRelationalData_View, multiplicity=Multiplicity(1, 1)),
        Property(name="CWMRelationalData_View", type=QueryExpression, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
namedColumnSet16: BinaryAssociation = BinaryAssociation(
    name="namedColumnSet16",
    ends={
        Property(name="NamedColumnSet17", type=CWMRelationalData_Trigger, multiplicity=Multiplicity(1, 1)),
        Property(name="triggers", type=NamedColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
structuralFeatures18: BinaryAssociation = BinaryAssociation(
    name="structuralFeatures18",
    ends={
        Property(name="Column19", type=CWMRelationalData_SQLDataType, multiplicity=Multiplicity(1, 1)),
        Property(name="type", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
sqlSimpleType20: BinaryAssociation = BinaryAssociation(
    name="sqlSimpleType20",
    ends={
        Property(name="SQLSimpleType", type=CWMRelationalData_SQLDistinctType, multiplicity=Multiplicity(1, 1)),
        Property(name="sqlDistinctTypes", type=SQLSimpleType, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_CWMRelationalData_Table_NamedColumnSet = Generalization(general=NamedColumnSet, specific=CWMRelationalData_Table)
gen_CWMRelationalData_View_NamedColumnSet = Generalization(general=NamedColumnSet, specific=CWMRelationalData_View)
gen_CWMRelationalData_NamedColumnSet_ColumnSet = Generalization(general=ColumnSet, specific=CWMRelationalData_NamedColumnSet)
gen_CWMRelationalData_QueryColumnSet_ColumnSet = Generalization(general=ColumnSet, specific=CWMRelationalData_QueryColumnSet)
gen_CWMRelationalData_SQLDistinctType_SQLDataType = Generalization(general=SQLDataType, specific=CWMRelationalData_SQLDistinctType)
gen_CWMRelationalData_SQLSimpleType_SQLDataType = Generalization(general=SQLDataType, specific=CWMRelationalData_SQLSimpleType)

# Domain Model
domain_model = DomainModel(
    name="CWMRelationalData",
    types={Column, Table, CWMRelationalData_Column, CWMRelationalData_QueryExpression, CWMRelationalData_CheckConstraint, CWMRelationalData_Table, CWMRelationalData_View, CheckConstraint, SQLDataType, ColumnSet, NamedColumnSet, CWMRelationalData_ColumnSet, CWMRelationalData_NamedColumnSet, Trigger, CWMRelationalData_QueryColumnSet, QueryExpression, CWMRelationalData_Trigger, CWMRelationalData_SQLDataType, CWMRelationalData_SQLDistinctType, SQLSimpleType, CWMRelationalData_SQLSimpleType, SQLDistinctType},
    associations={constraintElements0, constrainedElements1, table_constraints12, column_constraints2, type3, owner4, optionScopeColumnSet5, features6, optionScopeColumn8, triggers10, query11, sqlDistinctTypes21, queryExpression14, namedColumnSet16, structuralFeatures18, sqlSimpleType20},
    generalizations={gen_CWMRelationalData_Table_NamedColumnSet, gen_CWMRelationalData_View_NamedColumnSet, gen_CWMRelationalData_NamedColumnSet_ColumnSet, gen_CWMRelationalData_QueryColumnSet_ColumnSet, gen_CWMRelationalData_SQLDistinctType_SQLDataType, gen_CWMRelationalData_SQLSimpleType_SQLDataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)