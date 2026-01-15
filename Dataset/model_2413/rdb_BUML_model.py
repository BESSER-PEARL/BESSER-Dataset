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
rdb_NamedElement = Class(name="rdb::NamedElement", is_abstract=True)
Element = Class(name="Element")
rdb_Element = Class(name="rdb::Element")
rdb_NamedColumnSet = Class(name="rdb::NamedColumnSet", is_abstract=True)
SchemaElement = Class(name="SchemaElement")
rdb_SchemaElement = Class(name="rdb::SchemaElement", is_abstract=True)
rdb_Model = Class(name="rdb::Model")
NamedElement = Class(name="NamedElement")
rdb_Schema = Class(name="rdb::Schema")
rdb_Table = Class(name="rdb::Table")
NamedColumnSet = Class(name="NamedColumnSet")
rdb_TableColumn = Class(name="rdb::TableColumn")
Index = Class(name="Index")
PrimaryKey = Class(name="PrimaryKey")
UniqueConstraint = Class(name="UniqueConstraint")
ForeignKey = Class(name="ForeignKey")
PrimitiveDataType = Class(name="PrimitiveDataType")
CheckConstraint = Class(name="CheckConstraint")
rdb_Column = Class(name="rdb::Column", is_abstract=True)
Column = Class(name="Column")
Domain = Class(name="Domain")
constraints_rdb_TableColumn = Class(name="constraints::rdb::TableColumn")
rdb_constraints_Constraint = Class(name="rdb::constraints::Constraint", is_abstract=True)
rdb_constraints_CheckConstraint = Class(name="rdb::constraints::CheckConstraint")
Constraint = Class(name="Constraint")
rdb_constraints_ColumnRefConstraint = Class(name="rdb::constraints::ColumnRefConstraint", is_abstract=True)
IndexedColumn = Class(name="IndexedColumn")
rdb_constraints_UniqueConstraint = Class(name="rdb::constraints::UniqueConstraint")
ColumnRefConstraint = Class(name="ColumnRefConstraint")
rdb_constraints_PrimaryKey = Class(name="rdb::constraints::PrimaryKey")
rdb_constraints_ForeignKey = Class(name="rdb::constraints::ForeignKey")
rdb_constraints_Index = Class(name="rdb::constraints::Index")
datatypes_PrimitiveDataType = Class(name="datatypes::PrimitiveDataType")
rdb_constraints_IndexedColumn = Class(name="rdb::constraints::IndexedColumn")
rdb_datatypes_Domain = Class(name="rdb::datatypes::Domain")
rdb_datatypes_DataType = Class(name="rdb::datatypes::DataType", is_abstract=True)
rdb_datatypes_PrimitiveDataType = Class(name="rdb::datatypes::PrimitiveDataType")
DataType = Class(name="DataType")
rdb_view_View = Class(name="rdb::view::View")
ViewColumn = Class(name="ViewColumn")
ViewAlias = Class(name="ViewAlias")
view_rdb_Column = Class(name="view::rdb::Column")
rdb_view_ViewAlias = Class(name="rdb::view::ViewAlias")
view_rdb_NamedColumnSet = Class(name="view::rdb::NamedColumnSet")
rdb_view_ViewColumn = Class(name="rdb::view::ViewColumn", is_abstract=True)
rdb_view_ViewExpressionColumn = Class(name="rdb::view::ViewExpressionColumn")
rdb_view_ReferencedViewColumn = Class(name="rdb::view::ReferencedViewColumn")

# rdb_NamedElement class attributes and methods
rdb_NamedElement_name: Property = Property(name="name", type=StringType)
rdb_NamedElement.attributes={rdb_NamedElement_name}

# Element class attributes and methods

# rdb_Element class attributes and methods

# rdb_NamedColumnSet class attributes and methods

# SchemaElement class attributes and methods

# rdb_SchemaElement class attributes and methods
rdb_SchemaElement_owner: Property = Property(name="owner", type=StringType)
rdb_SchemaElement.attributes={rdb_SchemaElement_owner}

# rdb_Model class attributes and methods
rdb_Model_server_id: Property = Property(name="server_id", type=StringType)
rdb_Model.attributes={rdb_Model_server_id}

# NamedElement class attributes and methods

# rdb_Schema class attributes and methods

# rdb_Table class attributes and methods

# NamedColumnSet class attributes and methods

# rdb_TableColumn class attributes and methods
rdb_TableColumn_isPrimaryKey: Property = Property(name="isPrimaryKey", type=StringType)
rdb_TableColumn_isForeignKey: Property = Property(name="isForeignKey", type=StringType)
rdb_TableColumn.attributes={rdb_TableColumn_isPrimaryKey, rdb_TableColumn_isForeignKey}

# Index class attributes and methods

# PrimaryKey class attributes and methods

# UniqueConstraint class attributes and methods

# ForeignKey class attributes and methods

# PrimitiveDataType class attributes and methods

# CheckConstraint class attributes and methods

# rdb_Column class attributes and methods

# Column class attributes and methods

# Domain class attributes and methods

# constraints_rdb_TableColumn class attributes and methods

# rdb_constraints_Constraint class attributes and methods

# rdb_constraints_CheckConstraint class attributes and methods
rdb_constraints_CheckConstraint_expression: Property = Property(name="expression", type=StringType)
rdb_constraints_CheckConstraint.attributes={rdb_constraints_CheckConstraint_expression}

# Constraint class attributes and methods

# rdb_constraints_ColumnRefConstraint class attributes and methods

# IndexedColumn class attributes and methods

# rdb_constraints_UniqueConstraint class attributes and methods

# ColumnRefConstraint class attributes and methods

# rdb_constraints_PrimaryKey class attributes and methods

# rdb_constraints_ForeignKey class attributes and methods

# rdb_constraints_Index class attributes and methods

# datatypes_PrimitiveDataType class attributes and methods

# rdb_constraints_IndexedColumn class attributes and methods
rdb_constraints_IndexedColumn_ascending: Property = Property(name="ascending", type=BooleanType)
rdb_constraints_IndexedColumn.attributes={rdb_constraints_IndexedColumn_ascending}

# rdb_datatypes_Domain class attributes and methods

# rdb_datatypes_DataType class attributes and methods
rdb_datatypes_DataType_var: Property = Property(name="var", type=StringType)
rdb_datatypes_DataType_size: Property = Property(name="size", type=IntegerType)
rdb_datatypes_DataType_decimalDigits: Property = Property(name="decimalDigits", type=IntegerType)
rdb_datatypes_DataType_nullable: Property = Property(name="nullable", type=BooleanType)
rdb_datatypes_DataType_default: Property = Property(name="default", type=StringType)
rdb_datatypes_DataType_check: Property = Property(name="check", type=StringType)
rdb_datatypes_DataType.attributes={rdb_datatypes_DataType_check, rdb_datatypes_DataType_default, rdb_datatypes_DataType_var, rdb_datatypes_DataType_decimalDigits, rdb_datatypes_DataType_nullable, rdb_datatypes_DataType_size}

# rdb_datatypes_PrimitiveDataType class attributes and methods
rdb_datatypes_PrimitiveDataType_type: Property = Property(name="type", type=StringType)
rdb_datatypes_PrimitiveDataType.attributes={rdb_datatypes_PrimitiveDataType_type}

# DataType class attributes and methods

# rdb_view_View class attributes and methods
rdb_view_View_ddl: Property = Property(name="ddl", type=StringType)
rdb_view_View.attributes={rdb_view_View_ddl}

# ViewColumn class attributes and methods

# ViewAlias class attributes and methods

# view_rdb_Column class attributes and methods

# rdb_view_ViewAlias class attributes and methods

# view_rdb_NamedColumnSet class attributes and methods

# rdb_view_ViewColumn class attributes and methods

# rdb_view_ViewExpressionColumn class attributes and methods
rdb_view_ViewExpressionColumn_expression: Property = Property(name="expression", type=StringType)
rdb_view_ViewExpressionColumn.attributes={rdb_view_ViewExpressionColumn_expression}

# rdb_view_ReferencedViewColumn class attributes and methods

# Relationships
parent1: BinaryAssociation = BinaryAssociation(
    name="parent1",
    ends={
        Property(name="rdb_Element", type=rdb_Element, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Element0", type=rdb_Element, multiplicity=Multiplicity(0, 1))
    }
)
schemas2: BinaryAssociation = BinaryAssociation(
    name="schemas2",
    ends={
        Property(name="rdb_Schema", type=rdb_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Model", type=rdb_Schema, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns5: BinaryAssociation = BinaryAssociation(
    name="columns5",
    ends={
        Property(name="rdb_TableColumn", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table", type=rdb_TableColumn, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
elements3: BinaryAssociation = BinaryAssociation(
    name="elements3",
    ends={
        Property(name="rdb_SchemaElement", type=rdb_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Schema4", type=rdb_SchemaElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
indices12: BinaryAssociation = BinaryAssociation(
    name="indices12",
    ends={
        Property(name="Index", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table13", type=Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
primaryKey6: BinaryAssociation = BinaryAssociation(
    name="primaryKey6",
    ends={
        Property(name="PrimaryKey", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table7", type=PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
uniqueConstraints8: BinaryAssociation = BinaryAssociation(
    name="uniqueConstraints8",
    ends={
        Property(name="UniqueConstraint", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table9", type=UniqueConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
foreignKeys10: BinaryAssociation = BinaryAssociation(
    name="foreignKeys10",
    ends={
        Property(name="ForeignKey", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table11", type=ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="PrimitiveDataType", type=rdb_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_TableColumn19", type=PrimitiveDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
checks14: BinaryAssociation = BinaryAssociation(
    name="checks14",
    ends={
        Property(name="CheckConstraint", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table15", type=CheckConstraint, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
domain16: BinaryAssociation = BinaryAssociation(
    name="domain16",
    ends={
        Property(name="Domain", type=rdb_TableColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_TableColumn17", type=Domain, multiplicity=Multiplicity(0, 1))
    }
)
includedColumns20: BinaryAssociation = BinaryAssociation(
    name="includedColumns20",
    ends={
        Property(name="constraints_rdb_TableColumn", type=rdb_constraints_ColumnRefConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_constraints_ColumnRefConstraint", type=constraints_rdb_TableColumn, multiplicity=Multiplicity(1, 9999))
    }
)
referredUC21: BinaryAssociation = BinaryAssociation(
    name="referredUC21",
    ends={
        Property(name="UniqueConstraint22", type=rdb_constraints_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_constraints_ForeignKey", type=UniqueConstraint, multiplicity=Multiplicity(1, 1))
    }
)
indexedColumns23: BinaryAssociation = BinaryAssociation(
    name="indexedColumns23",
    ends={
        Property(name="IndexedColumn", type=rdb_constraints_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_constraints_Index", type=IndexedColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
refColumn24: BinaryAssociation = BinaryAssociation(
    name="refColumn24",
    ends={
        Property(name="constraints_rdb_TableColumn25", type=rdb_constraints_IndexedColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_constraints_IndexedColumn", type=constraints_rdb_TableColumn, multiplicity=Multiplicity(1, 1))
    }
)
parentDomain26: BinaryAssociation = BinaryAssociation(
    name="parentDomain26",
    ends={
        Property(name="Domain27", type=rdb_datatypes_Domain, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_datatypes_Domain", type=Domain, multiplicity=Multiplicity(0, 1))
    }
)
columns28: BinaryAssociation = BinaryAssociation(
    name="columns28",
    ends={
        Property(name="ViewColumn", type=rdb_view_View, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_view_View", type=ViewColumn, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
referencedTablesAndViews29: BinaryAssociation = BinaryAssociation(
    name="referencedTablesAndViews29",
    ends={
        Property(name="ViewAlias", type=rdb_view_View, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_view_View30", type=ViewAlias, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
referencedTableOrView31: BinaryAssociation = BinaryAssociation(
    name="referencedTableOrView31",
    ends={
        Property(name="view_rdb_NamedColumnSet", type=rdb_view_ViewAlias, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_view_ViewAlias", type=view_rdb_NamedColumnSet, multiplicity=Multiplicity(1, 1))
    }
)
refColumn32: BinaryAssociation = BinaryAssociation(
    name="refColumn32",
    ends={
        Property(name="view_rdb_Column", type=rdb_view_ReferencedViewColumn, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_view_ReferencedViewColumn", type=view_rdb_Column, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rdb_NamedElement_Element = Generalization(general=Element, specific=rdb_NamedElement)
gen_rdb_NamedColumnSet_SchemaElement = Generalization(general=SchemaElement, specific=rdb_NamedColumnSet)
gen_rdb_Schema_NamedElement = Generalization(general=NamedElement, specific=rdb_Schema)
gen_rdb_Model_NamedElement = Generalization(general=NamedElement, specific=rdb_Model)
gen_rdb_SchemaElement_NamedElement = Generalization(general=NamedElement, specific=rdb_SchemaElement)
gen_rdb_Table_NamedColumnSet = Generalization(general=NamedColumnSet, specific=rdb_Table)
gen_rdb_Column_NamedElement = Generalization(general=NamedElement, specific=rdb_Column)
gen_rdb_TableColumn_Column = Generalization(general=Column, specific=rdb_TableColumn)
gen_rdb_constraints_Constraint_NamedElement = Generalization(general=NamedElement, specific=rdb_constraints_Constraint)
gen_rdb_constraints_CheckConstraint_Constraint = Generalization(general=Constraint, specific=rdb_constraints_CheckConstraint)
gen_rdb_constraints_ColumnRefConstraint_Constraint = Generalization(general=Constraint, specific=rdb_constraints_ColumnRefConstraint)
gen_rdb_constraints_UniqueConstraint_ColumnRefConstraint = Generalization(general=ColumnRefConstraint, specific=rdb_constraints_UniqueConstraint)
gen_rdb_constraints_PrimaryKey_UniqueConstraint = Generalization(general=UniqueConstraint, specific=rdb_constraints_PrimaryKey)
gen_rdb_constraints_ForeignKey_ColumnRefConstraint = Generalization(general=ColumnRefConstraint, specific=rdb_constraints_ForeignKey)
gen_rdb_constraints_Index_Constraint = Generalization(general=Constraint, specific=rdb_constraints_Index)
gen_rdb_datatypes_Domain_SchemaElement = Generalization(general=SchemaElement, specific=rdb_datatypes_Domain)
gen_rdb_datatypes_Domain_datatypes_PrimitiveDataType = Generalization(general=datatypes_PrimitiveDataType, specific=rdb_datatypes_Domain)
gen_rdb_constraints_IndexedColumn_NamedElement = Generalization(general=NamedElement, specific=rdb_constraints_IndexedColumn)
gen_rdb_datatypes_DataType_NamedElement = Generalization(general=NamedElement, specific=rdb_datatypes_DataType)
gen_rdb_datatypes_PrimitiveDataType_DataType = Generalization(general=DataType, specific=rdb_datatypes_PrimitiveDataType)
gen_rdb_view_View_NamedColumnSet = Generalization(general=NamedColumnSet, specific=rdb_view_View)
gen_rdb_view_ViewAlias_NamedElement = Generalization(general=NamedElement, specific=rdb_view_ViewAlias)
gen_rdb_view_ViewColumn_Column = Generalization(general=Column, specific=rdb_view_ViewColumn)
gen_rdb_view_ViewExpressionColumn_ViewColumn = Generalization(general=ViewColumn, specific=rdb_view_ViewExpressionColumn)
gen_rdb_view_ReferencedViewColumn_ViewColumn = Generalization(general=ViewColumn, specific=rdb_view_ReferencedViewColumn)

# Domain Model
domain_model = DomainModel(
    name="rdb",
    types={rdb_NamedElement, Element, rdb_Element, rdb_NamedColumnSet, SchemaElement, rdb_SchemaElement, rdb_Model, NamedElement, rdb_Schema, rdb_Table, NamedColumnSet, rdb_TableColumn, Index, PrimaryKey, UniqueConstraint, ForeignKey, PrimitiveDataType, CheckConstraint, rdb_Column, Column, Domain, constraints_rdb_TableColumn, rdb_constraints_Constraint, rdb_constraints_CheckConstraint, Constraint, rdb_constraints_ColumnRefConstraint, IndexedColumn, rdb_constraints_UniqueConstraint, ColumnRefConstraint, rdb_constraints_PrimaryKey, rdb_constraints_ForeignKey, rdb_constraints_Index, datatypes_PrimitiveDataType, rdb_constraints_IndexedColumn, rdb_datatypes_Domain, rdb_datatypes_DataType, rdb_datatypes_PrimitiveDataType, DataType, rdb_view_View, ViewColumn, ViewAlias, view_rdb_Column, rdb_view_ViewAlias, view_rdb_NamedColumnSet, rdb_view_ViewColumn, rdb_view_ViewExpressionColumn, rdb_view_ReferencedViewColumn},
    associations={parent1, schemas2, columns5, elements3, indices12, primaryKey6, uniqueConstraints8, foreignKeys10, type18, checks14, domain16, includedColumns20, referredUC21, indexedColumns23, refColumn24, parentDomain26, columns28, referencedTablesAndViews29, referencedTableOrView31, refColumn32},
    generalizations={gen_rdb_NamedElement_Element, gen_rdb_NamedColumnSet_SchemaElement, gen_rdb_Schema_NamedElement, gen_rdb_Model_NamedElement, gen_rdb_SchemaElement_NamedElement, gen_rdb_Table_NamedColumnSet, gen_rdb_Column_NamedElement, gen_rdb_TableColumn_Column, gen_rdb_constraints_Constraint_NamedElement, gen_rdb_constraints_CheckConstraint_Constraint, gen_rdb_constraints_ColumnRefConstraint_Constraint, gen_rdb_constraints_UniqueConstraint_ColumnRefConstraint, gen_rdb_constraints_PrimaryKey_UniqueConstraint, gen_rdb_constraints_ForeignKey_ColumnRefConstraint, gen_rdb_constraints_Index_Constraint, gen_rdb_datatypes_Domain_SchemaElement, gen_rdb_datatypes_Domain_datatypes_PrimitiveDataType, gen_rdb_constraints_IndexedColumn_NamedElement, gen_rdb_datatypes_DataType_NamedElement, gen_rdb_datatypes_PrimitiveDataType_DataType, gen_rdb_view_View_NamedColumnSet, gen_rdb_view_ViewAlias_NamedElement, gen_rdb_view_ViewColumn_Column, gen_rdb_view_ViewExpressionColumn_ViewColumn, gen_rdb_view_ReferencedViewColumn_ViewColumn},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)