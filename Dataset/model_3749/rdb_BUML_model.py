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
RelationKind: Enumeration = Enumeration(
    name="RelationKind",
    literals={
            EnumerationLiteral(name="ZERO_OR_ONE"),
			EnumerationLiteral(name="ZERO_OR_MANY"),
			EnumerationLiteral(name="ONE_OR_MANY"),
			EnumerationLiteral(name="ONLY_ONE")
    }
)

# Classes
rdb_DB = Class(name="rdb::DB")
ERDInfo = Class(name="ERDInfo")
rdb_Table = Class(name="rdb::Table")
rdb_Style = Class(name="rdb::Style")
rdb_Column = Class(name="rdb::Column")
rdb_Relation = Class(name="rdb::Relation")
rdb_UserComment = Class(name="rdb::UserComment")
rdb_View = Class(name="rdb::View")
Table = Class(name="Table")
rdb_ERDInfo = Class(name="rdb::ERDInfo")

# rdb_DB class attributes and methods
rdb_DB_dbType: Property = Property(name="dbType", type=StringType)
rdb_DB_key: Property = Property(name="key", type=StringType)
rdb_DB_url: Property = Property(name="url", type=StringType)
rdb_DB_id: Property = Property(name="id", type=StringType)
rdb_DB_sid: Property = Property(name="sid", type=StringType)
rdb_DB_comment: Property = Property(name="comment", type=StringType)
rdb_DB.attributes={rdb_DB_url, rdb_DB_comment, rdb_DB_sid, rdb_DB_key, rdb_DB_id, rdb_DB_dbType}

# ERDInfo class attributes and methods

# rdb_Table class attributes and methods
rdb_Table_schema: Property = Property(name="schema", type=StringType)
rdb_Table_name: Property = Property(name="name", type=StringType)
rdb_Table_constraints: Property = Property(name="constraints", type=StringType)
rdb_Table_logicalName: Property = Property(name="logicalName", type=StringType)
rdb_Table_comment: Property = Property(name="comment", type=StringType)
rdb_Table.attributes={rdb_Table_constraints, rdb_Table_logicalName, rdb_Table_comment, rdb_Table_schema, rdb_Table_name}

# rdb_Style class attributes and methods
rdb_Style_grid: Property = Property(name="grid", type=StringType)
rdb_Style_scale: Property = Property(name="scale", type=StringType)
rdb_Style_tableTitle: Property = Property(name="tableTitle", type=StringType)
rdb_Style_columnPrimaryKey: Property = Property(name="columnPrimaryKey", type=StringType)
rdb_Style_columnName: Property = Property(name="columnName", type=StringType)
rdb_Style_columnComment: Property = Property(name="columnComment", type=StringType)
rdb_Style_columnType: Property = Property(name="columnType", type=StringType)
rdb_Style_columnNullCheck: Property = Property(name="columnNullCheck", type=StringType)
rdb_Style.attributes={rdb_Style_columnNullCheck, rdb_Style_columnComment, rdb_Style_scale, rdb_Style_columnPrimaryKey, rdb_Style_grid, rdb_Style_tableTitle, rdb_Style_columnType, rdb_Style_columnName}

# rdb_Column class attributes and methods
rdb_Column_extra: Property = Property(name="extra", type=StringType)
rdb_Column_field: Property = Property(name="field", type=StringType)
rdb_Column_type: Property = Property(name="type", type=StringType)
rdb_Column_null: Property = Property(name="null", type=StringType)
rdb_Column_default: Property = Property(name="default", type=StringType)
rdb_Column_logicalField: Property = Property(name="logicalField", type=StringType)
rdb_Column_key: Property = Property(name="key", type=StringType)
rdb_Column_comment: Property = Property(name="comment", type=StringType)
rdb_Column.attributes={rdb_Column_key, rdb_Column_type, rdb_Column_extra, rdb_Column_null, rdb_Column_logicalField, rdb_Column_field, rdb_Column_default, rdb_Column_comment}

# rdb_Relation class attributes and methods
rdb_Relation_type: Property = Property(name="type", type=StringType)
rdb_Relation_source_kind: Property = Property(name="source_kind", type=StringType)
rdb_Relation_target_kind: Property = Property(name="target_kind", type=StringType)
rdb_Relation_column_name: Property = Property(name="column_name", type=StringType)
rdb_Relation_referenced_column_name: Property = Property(name="referenced_column_name", type=StringType)
rdb_Relation_bendpoint: Property = Property(name="bendpoint", type=StringType)
rdb_Relation_comment: Property = Property(name="comment", type=StringType)
rdb_Relation_constraint_name: Property = Property(name="constraint_name", type=StringType)
rdb_Relation.attributes={rdb_Relation_referenced_column_name, rdb_Relation_constraint_name, rdb_Relation_target_kind, rdb_Relation_source_kind, rdb_Relation_bendpoint, rdb_Relation_comment, rdb_Relation_column_name, rdb_Relation_type}

# rdb_UserComment class attributes and methods
rdb_UserComment_comment: Property = Property(name="comment", type=StringType)
rdb_UserComment.attributes={rdb_UserComment_comment}

# rdb_View class attributes and methods

# Table class attributes and methods

# rdb_ERDInfo class attributes and methods
rdb_ERDInfo_autoLayout: Property = Property(name="autoLayout", type=BooleanType)
rdb_ERDInfo_version: Property = Property(name="version", type=StringType)
rdb_ERDInfo.attributes={rdb_ERDInfo_autoLayout, rdb_ERDInfo_version}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=rdb_DB, multiplicity=Multiplicity(1, 1)),
        Property(name="db", type=rdb_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
styledReference4: BinaryAssociation = BinaryAssociation(
    name="styledReference4",
    ends={
        Property(name="Style", type=rdb_DB, multiplicity=Multiplicity(1, 1)),
        Property(name="db5", type=rdb_Style, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table14: BinaryAssociation = BinaryAssociation(
    name="table14",
    ends={
        Property(name="Table15", type=rdb_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=rdb_Table, multiplicity=Multiplicity(1, 1))
    }
)
columns6: BinaryAssociation = BinaryAssociation(
    name="columns6",
    ends={
        Property(name="Column", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=rdb_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
db7: BinaryAssociation = BinaryAssociation(
    name="db7",
    ends={
        Property(name="DB", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=rdb_DB, multiplicity=Multiplicity(1, 1))
    }
)
incomingLinks8: BinaryAssociation = BinaryAssociation(
    name="incomingLinks8",
    ends={
        Property(name="Relation9", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=rdb_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingLinks10: BinaryAssociation = BinaryAssociation(
    name="outgoingLinks10",
    ends={
        Property(name="Relation11", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=rdb_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
UserCommentReference12: BinaryAssociation = BinaryAssociation(
    name="UserCommentReference12",
    ends={
        Property(name="rdb_UserComment13", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table", type=rdb_UserComment, multiplicity=Multiplicity(0, 100))
    }
)
references1: BinaryAssociation = BinaryAssociation(
    name="references1",
    ends={
        Property(name="Relation", type=rdb_DB, multiplicity=Multiplicity(1, 1)),
        Property(name="db2", type=rdb_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
DBComment3: BinaryAssociation = BinaryAssociation(
    name="DBComment3",
    ends={
        Property(name="rdb_UserComment", type=rdb_DB, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_DB", type=rdb_UserComment, multiplicity=Multiplicity(0, 1))
    }
)
source16: BinaryAssociation = BinaryAssociation(
    name="source16",
    ends={
        Property(name="Table17", type=rdb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingLinks", type=rdb_Table, multiplicity=Multiplicity(0, 1))
    }
)
target18: BinaryAssociation = BinaryAssociation(
    name="target18",
    ends={
        Property(name="Table19", type=rdb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingLinks", type=rdb_Table, multiplicity=Multiplicity(0, 1))
    }
)
db20: BinaryAssociation = BinaryAssociation(
    name="db20",
    ends={
        Property(name="DB21", type=rdb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=rdb_DB, multiplicity=Multiplicity(1, 1))
    }
)
db25: BinaryAssociation = BinaryAssociation(
    name="db25",
    ends={
        Property(name="DB26", type=rdb_Style, multiplicity=Multiplicity(1, 1)),
        Property(name="styledReference", type=rdb_DB, multiplicity=Multiplicity(1, 1))
    }
)
tableName22: BinaryAssociation = BinaryAssociation(
    name="tableName22",
    ends={
        Property(name="rdb_Table23", type=rdb_View, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_View", type=rdb_Table, multiplicity=Multiplicity(1, 1))
    }
)
style24: BinaryAssociation = BinaryAssociation(
    name="style24",
    ends={
        Property(name="rdb_Style", type=rdb_ERDInfo, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_ERDInfo", type=rdb_Style, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rdb_DB_ERDInfo = Generalization(general=ERDInfo, specific=rdb_DB)
gen_rdb_View_Table = Generalization(general=Table, specific=rdb_View)

# Domain Model
domain_model = DomainModel(
    name="rdb",
    types={rdb_DB, ERDInfo, rdb_Table, rdb_Style, rdb_Column, rdb_Relation, rdb_UserComment, rdb_View, Table, rdb_ERDInfo, RelationKind},
    associations={tables0, styledReference4, table14, columns6, db7, incomingLinks8, outgoingLinks10, UserCommentReference12, references1, DBComment3, source16, target18, db20, db25, tableName22, style24},
    generalizations={gen_rdb_DB_ERDInfo, gen_rdb_View_Table},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)