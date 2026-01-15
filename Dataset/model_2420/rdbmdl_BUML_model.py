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
PrimitiveTypeCodes: Enumeration = Enumeration(
    name="PrimitiveTypeCodes",
    literals={
            EnumerationLiteral(name="ARRAY"),
			EnumerationLiteral(name="BIGINT"),
			EnumerationLiteral(name="BINARY"),
			EnumerationLiteral(name="BIT"),
			EnumerationLiteral(name="BLOB"),
			EnumerationLiteral(name="BOOLEAN"),
			EnumerationLiteral(name="DISTINCT"),
			EnumerationLiteral(name="DOUBLE"),
			EnumerationLiteral(name="FLOAT"),
			EnumerationLiteral(name="INTEGER"),
			EnumerationLiteral(name="JAVA_OBJECT"),
			EnumerationLiteral(name="LONGNVARCHAR"),
			EnumerationLiteral(name="LONGVARBINARY"),
			EnumerationLiteral(name="LONGVARCHAR"),
			EnumerationLiteral(name="NCHAR"),
			EnumerationLiteral(name="CHAR"),
			EnumerationLiteral(name="CLOB"),
			EnumerationLiteral(name="DATALINK"),
			EnumerationLiteral(name="DATE"),
			EnumerationLiteral(name="DECIMAL"),
			EnumerationLiteral(name="REAL"),
			EnumerationLiteral(name="REF"),
			EnumerationLiteral(name="ROWID"),
			EnumerationLiteral(name="SMALLINT"),
			EnumerationLiteral(name="SQLXML"),
			EnumerationLiteral(name="STRUCT"),
			EnumerationLiteral(name="TIME"),
			EnumerationLiteral(name="TIMESTAMP"),
			EnumerationLiteral(name="TINYINT"),
			EnumerationLiteral(name="NCLOB"),
			EnumerationLiteral(name="NULL"),
			EnumerationLiteral(name="NUMERIC"),
			EnumerationLiteral(name="NVARCHAR"),
			EnumerationLiteral(name="OTHER"),
			EnumerationLiteral(name="VARBINARY"),
			EnumerationLiteral(name="VARCHAR")
    }
)

# Classes
rdbmdl_Element = Class(name="rdbmdl::Element")
rdbmdl_NamedColumnSet = Class(name="rdbmdl::NamedColumnSet", is_abstract=True)
SchemaElement = Class(name="SchemaElement")
rdbmdl_NamedElement = Class(name="rdbmdl::NamedElement", is_abstract=True)
Element = Class(name="Element")
rdbmdl_SchemaElement = Class(name="rdbmdl::SchemaElement", is_abstract=True)
rdbmdl_Table = Class(name="rdbmdl::Table")
NamedColumnSet = Class(name="NamedColumnSet")
rdbmdl_TableColumn = Class(name="rdbmdl::TableColumn")
PrimaryKey = Class(name="PrimaryKey")
rdbmdl_Model = Class(name="rdbmdl::Model")
NamedElement = Class(name="NamedElement")
rdbmdl_Schema = Class(name="rdbmdl::Schema")
Index = Class(name="Index")
CheckConstraint = Class(name="CheckConstraint")
rdbmdl_Column = Class(name="rdbmdl::Column", is_abstract=True)
Column = Class(name="Column")
Domain = Class(name="Domain")
PrimitiveDataType = Class(name="PrimitiveDataType")
rdbmdl_constraints_Constraint = Class(name="rdbmdl::constraints::Constraint", is_abstract=True)
UniqueConstraint = Class(name="UniqueConstraint")
ForeignKey = Class(name="ForeignKey")
rdbmdl_constraints_UniqueConstraint = Class(name="rdbmdl::constraints::UniqueConstraint")
ColumnRefConstraint = Class(name="ColumnRefConstraint")
rdbmdl_constraints_PrimaryKey = Class(name="rdbmdl::constraints::PrimaryKey")
rdbmdl_constraints_ForeignKey = Class(name="rdbmdl::constraints::ForeignKey")
rdbmdl_constraints_Index = Class(name="rdbmdl::constraints::Index")
IndexedColumn = Class(name="IndexedColumn")
rdbmdl_constraints_IndexedColumn = Class(name="rdbmdl::constraints::IndexedColumn")
rdbmdl_constraints_CheckConstraint = Class(name="rdbmdl::constraints::CheckConstraint")
Constraint = Class(name="Constraint")
rdbmdl_constraints_ColumnRefConstraint = Class(name="rdbmdl::constraints::ColumnRefConstraint", is_abstract=True)
constraints_rdbmdl_TableColumn = Class(name="constraints::rdbmdl::TableColumn")
rdbmdl_datatypes_DataType = Class(name="rdbmdl::datatypes::DataType", is_abstract=True)
rdbmdl_datatypes_Domain = Class(name="rdbmdl::datatypes::Domain")
datatypes_PrimitiveDataType = Class(name="datatypes::PrimitiveDataType")
rdbmdl_datatypes_PrimitiveDataType = Class(name="rdbmdl::datatypes::PrimitiveDataType")
DataType = Class(name="DataType")
ViewColumn = Class(name="ViewColumn")
ViewAlias = Class(name="ViewAlias")
rdbmdl_view_ViewAlias = Class(name="rdbmdl::view::ViewAlias")
rdbmdl_view_View = Class(name="rdbmdl::view::View")
rdbmdl_view_ViewColumn = Class(name="rdbmdl::view::ViewColumn", is_abstract=True)
rdbmdl_view_ViewExpressionColumn = Class(name="rdbmdl::view::ViewExpressionColumn")
rdbmdl_view_ReferencedViewColumn = Class(name="rdbmdl::view::ReferencedViewColumn")
view_rdbmdl_Column = Class(name="view::rdbmdl::Column")
view_rdbmdl_NamedColumnSet = Class(name="view::rdbmdl::NamedColumnSet")

# rdbmdl_Element class attributes and methods

# rdbmdl_NamedColumnSet class attributes and methods

# SchemaElement class attributes and methods

# rdbmdl_NamedElement class attributes and methods
rdbmdl_NamedElement_uid: Property = Property(name="uid", type=StringType)
rdbmdl_NamedElement_name: Property = Property(name="name", type=StringType)
rdbmdl_NamedElement.attributes={rdbmdl_NamedElement_name, rdbmdl_NamedElement_uid}

# Element class attributes and methods

# rdbmdl_SchemaElement class attributes and methods
rdbmdl_SchemaElement_owner: Property = Property(name="owner", type=StringType)
rdbmdl_SchemaElement.attributes={rdbmdl_SchemaElement_owner}

# rdbmdl_Table class attributes and methods

# NamedColumnSet class attributes and methods

# rdbmdl_TableColumn class attributes and methods
rdbmdl_TableColumn_isPrimaryKey: Property = Property(name="isPrimaryKey", type=StringType)
rdbmdl_TableColumn_isForeignKey: Property = Property(name="isForeignKey", type=StringType)
rdbmdl_TableColumn.attributes={rdbmdl_TableColumn_isPrimaryKey, rdbmdl_TableColumn_isForeignKey}

# PrimaryKey class attributes and methods

# rdbmdl_Model class attributes and methods
rdbmdl_Model_server_id: Property = Property(name="server_id", type=StringType)
rdbmdl_Model.attributes={rdbmdl_Model_server_id}

# NamedElement class attributes and methods

# rdbmdl_Schema class attributes and methods

# Index class attributes and methods

# CheckConstraint class attributes and methods

# rdbmdl_Column class attributes and methods

# Column class attributes and methods

# Domain class attributes and methods

# PrimitiveDataType class attributes and methods

# rdbmdl_constraints_Constraint class attributes and methods

# UniqueConstraint class attributes and methods

# ForeignKey class attributes and methods

# rdbmdl_constraints_UniqueConstraint class attributes and methods

# ColumnRefConstraint class attributes and methods

# rdbmdl_constraints_PrimaryKey class attributes and methods

# rdbmdl_constraints_ForeignKey class attributes and methods

# rdbmdl_constraints_Index class attributes and methods

# IndexedColumn class attributes and methods

# rdbmdl_constraints_IndexedColumn class attributes and methods
rdbmdl_constraints_IndexedColumn_ascending: Property = Property(name="ascending", type=BooleanType)
rdbmdl_constraints_IndexedColumn.attributes={rdbmdl_constraints_IndexedColumn_ascending}

# rdbmdl_constraints_CheckConstraint class attributes and methods
rdbmdl_constraints_CheckConstraint_expression: Property = Property(name="expression", type=StringType)
rdbmdl_constraints_CheckConstraint.attributes={rdbmdl_constraints_CheckConstraint_expression}

# Constraint class attributes and methods

# rdbmdl_constraints_ColumnRefConstraint class attributes and methods

# constraints_rdbmdl_TableColumn class attributes and methods

# rdbmdl_datatypes_DataType class attributes and methods
rdbmdl_datatypes_DataType_size: Property = Property(name="size", type=IntegerType)
rdbmdl_datatypes_DataType_decimalDigits: Property = Property(name="decimalDigits", type=IntegerType)
rdbmdl_datatypes_DataType_nullable: Property = Property(name="nullable", type=BooleanType)
rdbmdl_datatypes_DataType_default: Property = Property(name="default", type=StringType)
rdbmdl_datatypes_DataType_check: Property = Property(name="check", type=StringType)
rdbmdl_datatypes_DataType_var: Property = Property(name="var", type=StringType)
rdbmdl_datatypes_DataType.attributes={rdbmdl_datatypes_DataType_decimalDigits, rdbmdl_datatypes_DataType_size, rdbmdl_datatypes_DataType_default, rdbmdl_datatypes_DataType_check, rdbmdl_datatypes_DataType_nullable, rdbmdl_datatypes_DataType_var}

# rdbmdl_datatypes_Domain class attributes and methods

# datatypes_PrimitiveDataType class attributes and methods

# rdbmdl_datatypes_PrimitiveDataType class attributes and methods
rdbmdl_datatypes_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
rdbmdl_datatypes_PrimitiveDataType.attributes={rdbmdl_datatypes_PrimitiveDataType_type}

# DataType class attributes and methods

# ViewColumn class attributes and methods

# ViewAlias class attributes and methods

# rdbmdl_view_ViewAlias class attributes and methods

# rdbmdl_view_View class attributes and methods
rdbmdl_view_View_ddl: Property = Property(name="ddl", type=StringType)
rdbmdl_view_View.attributes={rdbmdl_view_View_ddl}

# rdbmdl_view_ViewColumn class attributes and methods

# rdbmdl_view_ViewExpressionColumn class attributes and methods
rdbmdl_view_ViewExpressionColumn_expression: Property = Property(name="expression", type=StringType)
rdbmdl_view_ViewExpressionColumn.attributes={rdbmdl_view_ViewExpressionColumn_expression}

# rdbmdl_view_ReferencedViewColumn class attributes and methods

# view_rdbmdl_Column class attributes and methods

# view_rdbmdl_NamedColumnSet class attributes and methods

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="rdbmdl_Element", type=rdbmdl_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Element0", type=rdbmdl_Element, multiplicity=Multiplicity(0, 1))
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="rdbmdl_SchemaElement", type=rdbmdl_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Schema4", type=rdbmdl_SchemaElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="rdbmdl_TableColumn", type=rdbmdl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Table", type=rdbmdl_TableColumn, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
schemas2: BinaryAssociation = BinaryAssociation(
    name="schemas2",
    ends={
        Property(name="rdbmdl_Schema", type=rdbmdl_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Model", type=rdbmdl_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indices12: BinaryAssociation = BinaryAssociation(
    name="indices12",
    ends={
        Property(name="Index", type=rdbmdl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Table13", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
checks14: BinaryAssociation = BinaryAssociation(
    name="checks14",
    ends={
        Property(name="CheckConstraint", type=rdbmdl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Table15", type=CheckConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain16: BinaryAssociation = BinaryAssociation(
    name="domain16",
    ends={
        Property(name="Domain", type=rdbmdl_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_TableColumn17", type=Domain, multiplicity=Multiplicity(0, 1))
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="PrimitiveDataType", type=rdbmdl_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_TableColumn19", type=PrimitiveDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
primaryKey6: BinaryAssociation = BinaryAssociation(
    name="primaryKey6",
    ends={
        Property(name="PrimaryKey", type=rdbmdl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Table7", type=PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uniqueConstraints8: BinaryAssociation = BinaryAssociation(
    name="uniqueConstraints8",
    ends={
        Property(name="UniqueConstraint", type=rdbmdl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Table9", type=UniqueConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys10: BinaryAssociation = BinaryAssociation(
    name="foreignKeys10",
    ends={
        Property(name="ForeignKey", type=rdbmdl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_Table11", type=ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
includedColumns20: BinaryAssociation = BinaryAssociation(
    name="includedColumns20",
    ends={
        Property(name="constraints_rdbmdl_TableColumn", type=rdbmdl_constraints_ColumnRefConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_constraints_ColumnRefConstraint", type=constraints_rdbmdl_TableColumn, multiplicity=Multiplicity(1, 9999))
    }
)
referredUC21: BinaryAssociation = BinaryAssociation(
    name="referredUC21",
    ends={
        Property(name="UniqueConstraint22", type=rdbmdl_constraints_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_constraints_ForeignKey", type=UniqueConstraint, multiplicity=Multiplicity(1, 1))
    }
)
indexedColumns23: BinaryAssociation = BinaryAssociation(
    name="indexedColumns23",
    ends={
        Property(name="IndexedColumn", type=rdbmdl_constraints_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_constraints_Index", type=IndexedColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refColumn24: BinaryAssociation = BinaryAssociation(
    name="refColumn24",
    ends={
        Property(name="constraints_rdbmdl_TableColumn25", type=rdbmdl_constraints_IndexedColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_constraints_IndexedColumn", type=constraints_rdbmdl_TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
parentDomain26: BinaryAssociation = BinaryAssociation(
    name="parentDomain26",
    ends={
        Property(name="Domain27", type=rdbmdl_datatypes_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_datatypes_Domain", type=Domain, multiplicity=Multiplicity(0, 1))
    }
)
columns28: BinaryAssociation = BinaryAssociation(
    name="columns28",
    ends={
        Property(name="ViewColumn", type=rdbmdl_view_View, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_view_View", type=ViewColumn, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
referencedTablesAndViews29: BinaryAssociation = BinaryAssociation(
    name="referencedTablesAndViews29",
    ends={
        Property(name="ViewAlias", type=rdbmdl_view_View, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_view_View30", type=ViewAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refColumn32: BinaryAssociation = BinaryAssociation(
    name="refColumn32",
    ends={
        Property(name="view_rdbmdl_Column", type=rdbmdl_view_ReferencedViewColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_view_ReferencedViewColumn", type=view_rdbmdl_Column, multiplicity=Multiplicity(1, 1))
    }
)
referencedTableOrView31: BinaryAssociation = BinaryAssociation(
    name="referencedTableOrView31",
    ends={
        Property(name="view_rdbmdl_NamedColumnSet", type=rdbmdl_view_ViewAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="rdbmdl_view_ViewAlias", type=view_rdbmdl_NamedColumnSet, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rdbmdl_NamedColumnSet_SchemaElement = Generalization(general=SchemaElement, specific=rdbmdl_NamedColumnSet)
gen_rdbmdl_NamedElement_Element = Generalization(general=Element, specific=rdbmdl_NamedElement)
gen_rdbmdl_Schema_NamedElement = Generalization(general=NamedElement, specific=rdbmdl_Schema)
gen_rdbmdl_SchemaElement_NamedElement = Generalization(general=NamedElement, specific=rdbmdl_SchemaElement)
gen_rdbmdl_Table_NamedColumnSet = Generalization(general=NamedColumnSet, specific=rdbmdl_Table)
gen_rdbmdl_Model_NamedElement = Generalization(general=NamedElement, specific=rdbmdl_Model)
gen_rdbmdl_Column_NamedElement = Generalization(general=NamedElement, specific=rdbmdl_Column)
gen_rdbmdl_TableColumn_Column = Generalization(general=Column, specific=rdbmdl_TableColumn)
gen_rdbmdl_constraints_UniqueConstraint_ColumnRefConstraint = Generalization(general=ColumnRefConstraint, specific=rdbmdl_constraints_UniqueConstraint)
gen_rdbmdl_constraints_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=rdbmdl_constraints_PrimaryKey)
gen_rdbmdl_constraints_ForeignKey_ColumnRefConstraint = Generalization(general=ColumnRefConstraint, specific=rdbmdl_constraints_ForeignKey)
gen_rdbmdl_constraints_Index_Constraint = Generalization(general=Constraint, specific=rdbmdl_constraints_Index)
gen_rdbmdl_constraints_IndexedColumn_NamedElement = Generalization(general=NamedElement, specific=rdbmdl_constraints_IndexedColumn)
gen_rdbmdl_constraints_Constraint_NamedElement = Generalization(general=NamedElement, specific=rdbmdl_constraints_Constraint)
gen_rdbmdl_constraints_CheckConstraint_Constraint = Generalization(general=Constraint, specific=rdbmdl_constraints_CheckConstraint)
gen_rdbmdl_constraints_ColumnRefConstraint_Constraint = Generalization(general=Constraint, specific=rdbmdl_constraints_ColumnRefConstraint)
gen_rdbmdl_datatypes_DataType_NamedElement = Generalization(general=NamedElement, specific=rdbmdl_datatypes_DataType)
gen_rdbmdl_datatypes_Domain_SchemaElement = Generalization(general=SchemaElement, specific=rdbmdl_datatypes_Domain)
gen_rdbmdl_datatypes_Domain_datatypes_PrimitiveDataType = Generalization(general=datatypes_PrimitiveDataType, specific=rdbmdl_datatypes_Domain)
gen_rdbmdl_datatypes_PrimitiveDataType_DataType = Generalization(general=DataType, specific=rdbmdl_datatypes_PrimitiveDataType)
gen_rdbmdl_view_View_NamedColumnSet = Generalization(general=NamedColumnSet, specific=rdbmdl_view_View)
gen_rdbmdl_view_ViewColumn_Column = Generalization(general=Column, specific=rdbmdl_view_ViewColumn)
gen_rdbmdl_view_ViewExpressionColumn_ViewColumn = Generalization(general=ViewColumn, specific=rdbmdl_view_ViewExpressionColumn)
gen_rdbmdl_view_ReferencedViewColumn_ViewColumn = Generalization(general=ViewColumn, specific=rdbmdl_view_ReferencedViewColumn)
gen_rdbmdl_view_ViewAlias_NamedElement = Generalization(general=NamedElement, specific=rdbmdl_view_ViewAlias)

# Domain Model
domain_model = DomainModel(
    name="rdbmdl",
    types={rdbmdl_Element, rdbmdl_NamedColumnSet, SchemaElement, rdbmdl_NamedElement, Element, rdbmdl_SchemaElement, rdbmdl_Table, NamedColumnSet, rdbmdl_TableColumn, PrimaryKey, rdbmdl_Model, NamedElement, rdbmdl_Schema, Index, CheckConstraint, rdbmdl_Column, Column, Domain, PrimitiveDataType, rdbmdl_constraints_Constraint, UniqueConstraint, ForeignKey, rdbmdl_constraints_UniqueConstraint, ColumnRefConstraint, rdbmdl_constraints_PrimaryKey, rdbmdl_constraints_ForeignKey, rdbmdl_constraints_Index, IndexedColumn, rdbmdl_constraints_IndexedColumn, rdbmdl_constraints_CheckConstraint, Constraint, rdbmdl_constraints_ColumnRefConstraint, constraints_rdbmdl_TableColumn, rdbmdl_datatypes_DataType, rdbmdl_datatypes_Domain, datatypes_PrimitiveDataType, rdbmdl_datatypes_PrimitiveDataType, DataType, ViewColumn, ViewAlias, rdbmdl_view_ViewAlias, rdbmdl_view_View, rdbmdl_view_ViewColumn, rdbmdl_view_ViewExpressionColumn, rdbmdl_view_ReferencedViewColumn, view_rdbmdl_Column, view_rdbmdl_NamedColumnSet, PrimitiveTypeCodes},
    associations={parent1, elements3, columns5, schemas2, indices12, checks14, domain16, type18, primaryKey6, uniqueConstraints8, foreignKeys10, includedColumns20, referredUC21, indexedColumns23, refColumn24, parentDomain26, columns28, referencedTablesAndViews29, refColumn32, referencedTableOrView31},
    generalizations={gen_rdbmdl_NamedColumnSet_SchemaElement, gen_rdbmdl_NamedElement_Element, gen_rdbmdl_Schema_NamedElement, gen_rdbmdl_SchemaElement_NamedElement, gen_rdbmdl_Table_NamedColumnSet, gen_rdbmdl_Model_NamedElement, gen_rdbmdl_Column_NamedElement, gen_rdbmdl_TableColumn_Column, gen_rdbmdl_constraints_UniqueConstraint_ColumnRefConstraint, gen_rdbmdl_constraints_PrimaryKey_UniqueConstraint, gen_rdbmdl_constraints_ForeignKey_ColumnRefConstraint, gen_rdbmdl_constraints_Index_Constraint, gen_rdbmdl_constraints_IndexedColumn_NamedElement, gen_rdbmdl_constraints_Constraint_NamedElement, gen_rdbmdl_constraints_CheckConstraint_Constraint, gen_rdbmdl_constraints_ColumnRefConstraint_Constraint, gen_rdbmdl_datatypes_DataType_NamedElement, gen_rdbmdl_datatypes_Domain_SchemaElement, gen_rdbmdl_datatypes_Domain_datatypes_PrimitiveDataType, gen_rdbmdl_datatypes_PrimitiveDataType_DataType, gen_rdbmdl_view_View_NamedColumnSet, gen_rdbmdl_view_ViewColumn_Column, gen_rdbmdl_view_ViewExpressionColumn_ViewColumn, gen_rdbmdl_view_ReferencedViewColumn_ViewColumn, gen_rdbmdl_view_ViewAlias_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)