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
            EnumerationLiteral(name="ONLY_ONE"),
			EnumerationLiteral(name="ZERO_OR_ONE"),
			EnumerationLiteral(name="ZERO_OR_MANY"),
			EnumerationLiteral(name="ONE_OR_MANY")
    }
)

# Classes
ERDInfo = Class(name="ERDInfo")
rdb_Table = Class(name="rdb::Table")
rdb_Relation = Class(name="rdb::Relation")
rdb_Column = Class(name="rdb::Column")
rdb_DB = Class(name="rdb::DB")
rdb_UserComment = Class(name="rdb::UserComment")
rdb_View = Class(name="rdb::View")
Table = Class(name="Table")
rdb_ERDInfo = Class(name="rdb::ERDInfo")

# ERDInfo class attributes and methods

# rdb_Table class attributes and methods
rdb_Table_name: Property = Property(name="name", type=StringType)
rdb_Table_logicalName: Property = Property(name="logicalName", type=StringType)
rdb_Table_comment: Property = Property(name="comment", type=StringType)
rdb_Table_constraints: Property = Property(name="constraints", type=StringType)
rdb_Table.attributes={rdb_Table_comment, rdb_Table_logicalName, rdb_Table_name, rdb_Table_constraints}

# rdb_Relation class attributes and methods
rdb_Relation_source_kind: Property = Property(name="source_kind", type=StringType)
rdb_Relation_comment: Property = Property(name="comment", type=StringType)
rdb_Relation_constraint_name: Property = Property(name="constraint_name", type=StringType)
rdb_Relation_target_kind: Property = Property(name="target_kind", type=StringType)
rdb_Relation_column_name: Property = Property(name="column_name", type=StringType)
rdb_Relation_referenced_column_name: Property = Property(name="referenced_column_name", type=StringType)
rdb_Relation_bendpoint: Property = Property(name="bendpoint", type=StringType)
rdb_Relation.attributes={rdb_Relation_referenced_column_name, rdb_Relation_bendpoint, rdb_Relation_target_kind, rdb_Relation_constraint_name, rdb_Relation_column_name, rdb_Relation_source_kind, rdb_Relation_comment}

# rdb_Column class attributes and methods
rdb_Column_field: Property = Property(name="field", type=StringType)
rdb_Column_type: Property = Property(name="type", type=StringType)
rdb_Column_null: Property = Property(name="null", type=StringType)
rdb_Column_default: Property = Property(name="default", type=StringType)
rdb_Column_extra: Property = Property(name="extra", type=StringType)
rdb_Column_logicalField: Property = Property(name="logicalField", type=StringType)
rdb_Column_key: Property = Property(name="key", type=StringType)
rdb_Column_comment: Property = Property(name="comment", type=StringType)
rdb_Column.attributes={rdb_Column_null, rdb_Column_type, rdb_Column_comment, rdb_Column_extra, rdb_Column_default, rdb_Column_key, rdb_Column_field, rdb_Column_logicalField}

# rdb_DB class attributes and methods
rdb_DB_dbType: Property = Property(name="dbType", type=StringType)
rdb_DB_key: Property = Property(name="key", type=StringType)
rdb_DB_url: Property = Property(name="url", type=StringType)
rdb_DB_id: Property = Property(name="id", type=StringType)
rdb_DB_sid: Property = Property(name="sid", type=StringType)
rdb_DB_comment: Property = Property(name="comment", type=StringType)
rdb_DB.attributes={rdb_DB_comment, rdb_DB_url, rdb_DB_key, rdb_DB_id, rdb_DB_sid, rdb_DB_dbType}

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
references1: BinaryAssociation = BinaryAssociation(
    name="references1",
    ends={
        Property(name="Relation", type=rdb_DB, multiplicity=Multiplicity(1, 1)),
        Property(name="db2", type=rdb_Relation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns3: BinaryAssociation = BinaryAssociation(
    name="columns3",
    ends={
        Property(name="Column", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="table", type=rdb_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
db4: BinaryAssociation = BinaryAssociation(
    name="db4",
    ends={
        Property(name="DB", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=rdb_DB, multiplicity=Multiplicity(1, 1))
    }
)
UserCommentReference9: BinaryAssociation = BinaryAssociation(
    name="UserCommentReference9",
    ends={
        Property(name="rdb_UserComment", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_Table", type=rdb_UserComment, multiplicity=Multiplicity(0, 1))
    }
)
table10: BinaryAssociation = BinaryAssociation(
    name="table10",
    ends={
        Property(name="Table11", type=rdb_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=rdb_Table, multiplicity=Multiplicity(1, 1))
    }
)
source12: BinaryAssociation = BinaryAssociation(
    name="source12",
    ends={
        Property(name="Table13", type=rdb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="outgoingLinks", type=rdb_Table, multiplicity=Multiplicity(0, 1))
    }
)
target14: BinaryAssociation = BinaryAssociation(
    name="target14",
    ends={
        Property(name="Table15", type=rdb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="incomingLinks", type=rdb_Table, multiplicity=Multiplicity(0, 1))
    }
)
incomingLinks5: BinaryAssociation = BinaryAssociation(
    name="incomingLinks5",
    ends={
        Property(name="Relation6", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="target", type=rdb_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
outgoingLinks7: BinaryAssociation = BinaryAssociation(
    name="outgoingLinks7",
    ends={
        Property(name="Relation8", type=rdb_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="source", type=rdb_Relation, multiplicity=Multiplicity(0, 9999))
    }
)
db16: BinaryAssociation = BinaryAssociation(
    name="db16",
    ends={
        Property(name="DB17", type=rdb_Relation, multiplicity=Multiplicity(1, 1)),
        Property(name="references", type=rdb_DB, multiplicity=Multiplicity(1, 1))
    }
)
tableName18: BinaryAssociation = BinaryAssociation(
    name="tableName18",
    ends={
        Property(name="rdb_Table19", type=rdb_View, multiplicity=Multiplicity(1, 1)),
        Property(name="rdb_View", type=rdb_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_rdb_DB_ERDInfo = Generalization(general=ERDInfo, specific=rdb_DB)
gen_rdb_View_Table = Generalization(general=Table, specific=rdb_View)

# Domain Model
domain_model = DomainModel(
    name="rdb",
    types={ERDInfo, rdb_Table, rdb_Relation, rdb_Column, rdb_DB, rdb_UserComment, rdb_View, Table, rdb_ERDInfo, RelationKind},
    associations={tables0, references1, columns3, db4, UserCommentReference9, table10, source12, target14, incomingLinks5, outgoingLinks7, db16, tableName18},
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