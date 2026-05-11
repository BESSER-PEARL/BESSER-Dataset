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
SortDirectionEnum: Enumeration = Enumeration(
    name="SortDirectionEnum",
    literals={
            EnumerationLiteral(name="ASC"),
			EnumerationLiteral(name="DESC")
    }
)

# Classes
ddlDsl_Column = Class(name="ddlDsl_Column")
ddlDsl_AddTableConstraint = Class(name="ddlDsl_AddTableConstraint")
ddlDsl_Create = Class(name="ddlDsl_Create")
Create = Class(name="Create")
ddlDsl_Ddl = Class(name="ddlDsl_Ddl")
ddlDsl_DdlStatement = Class(name="ddlDsl_DdlStatement")
ddlDsl_Alter = Class(name="ddlDsl_Alter")
DdlStatement = Class(name="DdlStatement")
ddlDsl_CreateTable = Class(name="ddlDsl_CreateTable")
ddlDsl_AlterTableAction = Class(name="ddlDsl_AlterTableAction")
ddlDsl_Constraint = Class(name="ddlDsl_Constraint")
ddlDsl_DropTableConstraint = Class(name="ddlDsl_DropTableConstraint")
AlterTableAction = Class(name="AlterTableAction")
ddlDsl_Comment = Class(name="ddlDsl_Comment")
ddlDsl_TableComment = Class(name="ddlDsl_TableComment")
Comment = Class(name="Comment")
ddlDsl_ColumnComment = Class(name="ddlDsl_ColumnComment")
ddlDsl_TableProperty = Class(name="ddlDsl_TableProperty")
ddlDsl_CreateIndex = Class(name="ddlDsl_CreateIndex")
TableProperty = Class(name="TableProperty")
ddlDsl_SqlDataType = Class(name="ddlDsl_SqlDataType")
ddlDsl_ReferenceClause = Class(name="ddlDsl_ReferenceClause")
ddlDsl_Drop = Class(name="ddlDsl_Drop")
ddlDsl_NullableConstraint = Class(name="ddlDsl_NullableConstraint")
Constraint = Class(name="Constraint")
ddlDsl_UniqueKeyConstraint = Class(name="ddlDsl_UniqueKeyConstraint")
ddlDsl_PrimaryKeyConstraint = Class(name="ddlDsl_PrimaryKeyConstraint")
ddlDsl_ForeignKeyConstraint = Class(name="ddlDsl_ForeignKeyConstraint")
ddlDsl_SqlCharacter = Class(name="ddlDsl_SqlCharacter")
SqlDataType = Class(name="SqlDataType")
ddlDsl_SqlNumber = Class(name="ddlDsl_SqlNumber")
ddlDsl_LongRaw = Class(name="ddlDsl_LongRaw")
ddlDsl_Long = Class(name="ddlDsl_Long")
LongRaw = Class(name="LongRaw")
ddlDsl_Raw = Class(name="ddlDsl_Raw")
ddlDsl_SqlDateTime = Class(name="ddlDsl_SqlDateTime")
ddlDsl_SqlDate = Class(name="ddlDsl_SqlDate")
SqlDateTime = Class(name="SqlDateTime")
ddlDsl_SqlTimeStamp = Class(name="ddlDsl_SqlTimeStamp")
ddlDsl_SqlInterval = Class(name="ddlDsl_SqlInterval")
ddlDsl_LargeObjectType = Class(name="ddlDsl_LargeObjectType")
ddlDsl_RowIdType = Class(name="ddlDsl_RowIdType")
ddlDsl_SqlBoolean = Class(name="ddlDsl_SqlBoolean")

# ddlDsl_Column class attributes and methods
ddlDsl_Column_sorted: Property = Property(name="sorted", type=BooleanType)
ddlDsl_Column_default: Property = Property(name="default", type=StringType)
ddlDsl_Column.attributes={ddlDsl_Column_default, ddlDsl_Column_sorted}

# ddlDsl_AddTableConstraint class attributes and methods
ddlDsl_AddTableConstraint_name: Property = Property(name="name", type=StringType)
ddlDsl_AddTableConstraint.attributes={ddlDsl_AddTableConstraint_name}

# ddlDsl_Create class attributes and methods
ddlDsl_Create_name: Property = Property(name="name", type=StringType)
ddlDsl_Create.attributes={ddlDsl_Create_name}

# Create class attributes and methods

# ddlDsl_Ddl class attributes and methods

# ddlDsl_DdlStatement class attributes and methods

# ddlDsl_Alter class attributes and methods

# DdlStatement class attributes and methods

# ddlDsl_CreateTable class attributes and methods

# ddlDsl_AlterTableAction class attributes and methods

# ddlDsl_Constraint class attributes and methods

# ddlDsl_DropTableConstraint class attributes and methods

# AlterTableAction class attributes and methods

# ddlDsl_Comment class attributes and methods
ddlDsl_Comment_comment: Property = Property(name="comment", type=StringType)
ddlDsl_Comment.attributes={ddlDsl_Comment_comment}

# ddlDsl_TableComment class attributes and methods

# Comment class attributes and methods

# ddlDsl_ColumnComment class attributes and methods

# ddlDsl_TableProperty class attributes and methods
ddlDsl_TableProperty_name: Property = Property(name="name", type=StringType)
ddlDsl_TableProperty.attributes={ddlDsl_TableProperty_name}

# ddlDsl_CreateIndex class attributes and methods
ddlDsl_CreateIndex_unique: Property = Property(name="unique", type=BooleanType)
ddlDsl_CreateIndex_sortOrders: Property = Property(name="sortOrders", type=StringType)
ddlDsl_CreateIndex.attributes={ddlDsl_CreateIndex_unique, ddlDsl_CreateIndex_sortOrders}

# TableProperty class attributes and methods

# ddlDsl_SqlDataType class attributes and methods
ddlDsl_SqlDataType_name: Property = Property(name="name", type=StringType)
ddlDsl_SqlDataType.attributes={ddlDsl_SqlDataType_name}

# ddlDsl_ReferenceClause class attributes and methods

# ddlDsl_Drop class attributes and methods
ddlDsl_Drop_object: Property = Property(name="object", type=StringType)
ddlDsl_Drop.attributes={ddlDsl_Drop_object}

# ddlDsl_NullableConstraint class attributes and methods
ddlDsl_NullableConstraint_not_: Property = Property(name="not_", type=BooleanType)
ddlDsl_NullableConstraint.attributes={ddlDsl_NullableConstraint_not_}

# Constraint class attributes and methods

# ddlDsl_UniqueKeyConstraint class attributes and methods

# ddlDsl_PrimaryKeyConstraint class attributes and methods

# ddlDsl_ForeignKeyConstraint class attributes and methods

# ddlDsl_SqlCharacter class attributes and methods
ddlDsl_SqlCharacter_national: Property = Property(name="national", type=BooleanType)
ddlDsl_SqlCharacter_size: Property = Property(name="size", type=IntegerType)
ddlDsl_SqlCharacter.attributes={ddlDsl_SqlCharacter_national, ddlDsl_SqlCharacter_size}

# SqlDataType class attributes and methods

# ddlDsl_SqlNumber class attributes and methods
ddlDsl_SqlNumber_hasPrecision: Property = Property(name="hasPrecision", type=BooleanType)
ddlDsl_SqlNumber_precision: Property = Property(name="precision", type=IntegerType)
ddlDsl_SqlNumber_scale: Property = Property(name="scale", type=IntegerType)
ddlDsl_SqlNumber.attributes={ddlDsl_SqlNumber_hasPrecision, ddlDsl_SqlNumber_scale, ddlDsl_SqlNumber_precision}

# ddlDsl_LongRaw class attributes and methods

# ddlDsl_Long class attributes and methods
ddlDsl_Long_raw: Property = Property(name="raw", type=BooleanType)
ddlDsl_Long.attributes={ddlDsl_Long_raw}

# LongRaw class attributes and methods

# ddlDsl_Raw class attributes and methods
ddlDsl_Raw_size: Property = Property(name="size", type=IntegerType)
ddlDsl_Raw.attributes={ddlDsl_Raw_size}

# ddlDsl_SqlDateTime class attributes and methods

# ddlDsl_SqlDate class attributes and methods

# SqlDateTime class attributes and methods

# ddlDsl_SqlTimeStamp class attributes and methods
ddlDsl_SqlTimeStamp_precision: Property = Property(name="precision", type=IntegerType)
ddlDsl_SqlTimeStamp.attributes={ddlDsl_SqlTimeStamp_precision}

# ddlDsl_SqlInterval class attributes and methods
ddlDsl_SqlInterval_year: Property = Property(name="year", type=BooleanType)
ddlDsl_SqlInterval_day: Property = Property(name="day", type=BooleanType)
ddlDsl_SqlInterval_precision: Property = Property(name="precision", type=IntegerType)
ddlDsl_SqlInterval_secondsPrecision: Property = Property(name="secondsPrecision", type=IntegerType)
ddlDsl_SqlInterval.attributes={ddlDsl_SqlInterval_precision, ddlDsl_SqlInterval_secondsPrecision, ddlDsl_SqlInterval_day, ddlDsl_SqlInterval_year}

# ddlDsl_LargeObjectType class attributes and methods
ddlDsl_LargeObjectType_size: Property = Property(name="size", type=IntegerType)
ddlDsl_LargeObjectType.attributes={ddlDsl_LargeObjectType_size}

# ddlDsl_RowIdType class attributes and methods
ddlDsl_RowIdType_size: Property = Property(name="size", type=IntegerType)
ddlDsl_RowIdType.attributes={ddlDsl_RowIdType_size}

# ddlDsl_SqlBoolean class attributes and methods

# Relationships
column10: BinaryAssociation = BinaryAssociation(
    name="column10",
    ends={
        Property(name="ddlDsl_Column", type=ddlDsl_ColumnComment, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_ColumnComment", type=ddlDsl_Column, multiplicity=Multiplicity(0, 1))
    }
)
statements0: BinaryAssociation = BinaryAssociation(
    name="statements0",
    ends={
        Property(name="ddlDsl_DdlStatement", type=ddlDsl_Ddl, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_Ddl", type=ddlDsl_DdlStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table1: BinaryAssociation = BinaryAssociation(
    name="table1",
    ends={
        Property(name="ddlDsl_CreateTable", type=ddlDsl_Alter, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_Alter", type=ddlDsl_CreateTable, multiplicity=Multiplicity(0, 1))
    }
)
action2: BinaryAssociation = BinaryAssociation(
    name="action2",
    ends={
        Property(name="ddlDsl_AlterTableAction", type=ddlDsl_Alter, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_Alter3", type=ddlDsl_AlterTableAction, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint4: BinaryAssociation = BinaryAssociation(
    name="constraint4",
    ends={
        Property(name="ddlDsl_Constraint", type=ddlDsl_AlterTableAction, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_AlterTableAction5", type=ddlDsl_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraintRef6: BinaryAssociation = BinaryAssociation(
    name="constraintRef6",
    ends={
        Property(name="ddlDsl_Constraint7", type=ddlDsl_DropTableConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_DropTableConstraint", type=ddlDsl_Constraint, multiplicity=Multiplicity(0, 1))
    }
)
table8: BinaryAssociation = BinaryAssociation(
    name="table8",
    ends={
        Property(name="ddlDsl_CreateTable9", type=ddlDsl_TableComment, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_TableComment", type=ddlDsl_CreateTable, multiplicity=Multiplicity(0, 1))
    }
)
columns29: BinaryAssociation = BinaryAssociation(
    name="columns29",
    ends={
        Property(name="ddlDsl_Column30", type=ddlDsl_ForeignKeyConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_ForeignKeyConstraint", type=ddlDsl_Column, multiplicity=Multiplicity(0, 9999))
    }
)
properties11: BinaryAssociation = BinaryAssociation(
    name="properties11",
    ends={
        Property(name="ddlDsl_TableProperty", type=ddlDsl_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_CreateTable12", type=ddlDsl_TableProperty, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
table13: BinaryAssociation = BinaryAssociation(
    name="table13",
    ends={
        Property(name="ddlDsl_CreateTable14", type=ddlDsl_CreateIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_CreateIndex", type=ddlDsl_CreateTable, multiplicity=Multiplicity(0, 1))
    }
)
columns15: BinaryAssociation = BinaryAssociation(
    name="columns15",
    ends={
        Property(name="ddlDsl_Column17", type=ddlDsl_CreateIndex, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_CreateIndex16", type=ddlDsl_Column, multiplicity=Multiplicity(0, 9999))
    }
)
type18: BinaryAssociation = BinaryAssociation(
    name="type18",
    ends={
        Property(name="ddlDsl_SqlDataType", type=ddlDsl_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_Column19", type=ddlDsl_SqlDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
constraint20: BinaryAssociation = BinaryAssociation(
    name="constraint20",
    ends={
        Property(name="ddlDsl_Constraint22", type=ddlDsl_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_Column21", type=ddlDsl_Constraint, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
reference23: BinaryAssociation = BinaryAssociation(
    name="reference23",
    ends={
        Property(name="ddlDsl_ReferenceClause", type=ddlDsl_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_Column24", type=ddlDsl_ReferenceClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns25: BinaryAssociation = BinaryAssociation(
    name="columns25",
    ends={
        Property(name="ddlDsl_Column26", type=ddlDsl_UniqueKeyConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_UniqueKeyConstraint", type=ddlDsl_Column, multiplicity=Multiplicity(0, 9999))
    }
)
columns27: BinaryAssociation = BinaryAssociation(
    name="columns27",
    ends={
        Property(name="ddlDsl_Column28", type=ddlDsl_PrimaryKeyConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_PrimaryKeyConstraint", type=ddlDsl_Column, multiplicity=Multiplicity(0, 9999))
    }
)
reference31: BinaryAssociation = BinaryAssociation(
    name="reference31",
    ends={
        Property(name="ddlDsl_ReferenceClause33", type=ddlDsl_ForeignKeyConstraint, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_ForeignKeyConstraint32", type=ddlDsl_ReferenceClause, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table34: BinaryAssociation = BinaryAssociation(
    name="table34",
    ends={
        Property(name="ddlDsl_CreateTable36", type=ddlDsl_ReferenceClause, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_ReferenceClause35", type=ddlDsl_CreateTable, multiplicity=Multiplicity(0, 1))
    }
)
columns37: BinaryAssociation = BinaryAssociation(
    name="columns37",
    ends={
        Property(name="ddlDsl_Column39", type=ddlDsl_ReferenceClause, multiplicity=Multiplicity(1, 1)),
        Property(name="ddlDsl_ReferenceClause38", type=ddlDsl_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_ddlDsl_AddTableConstraint_AlterTableAction = Generalization(general=AlterTableAction, specific=ddlDsl_AddTableConstraint)
gen_ddlDsl_Create_DdlStatement = Generalization(general=DdlStatement, specific=ddlDsl_Create)
gen_ddlDsl_CreateTable_Create = Generalization(general=Create, specific=ddlDsl_CreateTable)
gen_ddlDsl_Alter_DdlStatement = Generalization(general=DdlStatement, specific=ddlDsl_Alter)
gen_ddlDsl_DropTableConstraint_AlterTableAction = Generalization(general=AlterTableAction, specific=ddlDsl_DropTableConstraint)
gen_ddlDsl_Comment_DdlStatement = Generalization(general=DdlStatement, specific=ddlDsl_Comment)
gen_ddlDsl_TableComment_Comment = Generalization(general=Comment, specific=ddlDsl_TableComment)
gen_ddlDsl_ColumnComment_Comment = Generalization(general=Comment, specific=ddlDsl_ColumnComment)
gen_ddlDsl_CreateIndex_Create = Generalization(general=Create, specific=ddlDsl_CreateIndex)
gen_ddlDsl_Column_TableProperty = Generalization(general=TableProperty, specific=ddlDsl_Column)
gen_ddlDsl_Drop_DdlStatement = Generalization(general=DdlStatement, specific=ddlDsl_Drop)
gen_ddlDsl_Constraint_TableProperty = Generalization(general=TableProperty, specific=ddlDsl_Constraint)
gen_ddlDsl_NullableConstraint_Constraint = Generalization(general=Constraint, specific=ddlDsl_NullableConstraint)
gen_ddlDsl_UniqueKeyConstraint_Constraint = Generalization(general=Constraint, specific=ddlDsl_UniqueKeyConstraint)
gen_ddlDsl_PrimaryKeyConstraint_Constraint = Generalization(general=Constraint, specific=ddlDsl_PrimaryKeyConstraint)
gen_ddlDsl_ForeignKeyConstraint_Constraint = Generalization(general=Constraint, specific=ddlDsl_ForeignKeyConstraint)
gen_ddlDsl_SqlCharacter_SqlDataType = Generalization(general=SqlDataType, specific=ddlDsl_SqlCharacter)
gen_ddlDsl_SqlNumber_SqlDataType = Generalization(general=SqlDataType, specific=ddlDsl_SqlNumber)
gen_ddlDsl_LongRaw_SqlDataType = Generalization(general=SqlDataType, specific=ddlDsl_LongRaw)
gen_ddlDsl_Long_LongRaw = Generalization(general=LongRaw, specific=ddlDsl_Long)
gen_ddlDsl_Raw_LongRaw = Generalization(general=LongRaw, specific=ddlDsl_Raw)
gen_ddlDsl_SqlDateTime_SqlDataType = Generalization(general=SqlDataType, specific=ddlDsl_SqlDateTime)
gen_ddlDsl_SqlDate_SqlDateTime = Generalization(general=SqlDateTime, specific=ddlDsl_SqlDate)
gen_ddlDsl_SqlTimeStamp_SqlDateTime = Generalization(general=SqlDateTime, specific=ddlDsl_SqlTimeStamp)
gen_ddlDsl_SqlInterval_SqlDateTime = Generalization(general=SqlDateTime, specific=ddlDsl_SqlInterval)
gen_ddlDsl_LargeObjectType_SqlDataType = Generalization(general=SqlDataType, specific=ddlDsl_LargeObjectType)
gen_ddlDsl_RowIdType_SqlDataType = Generalization(general=SqlDataType, specific=ddlDsl_RowIdType)
gen_ddlDsl_SqlBoolean_SqlDataType = Generalization(general=SqlDataType, specific=ddlDsl_SqlBoolean)

# Domain Model
domain_model = DomainModel(
    name="ddlDsl",
    types={ddlDsl_Column, ddlDsl_AddTableConstraint, ddlDsl_Create, Create, ddlDsl_Ddl, ddlDsl_DdlStatement, ddlDsl_Alter, DdlStatement, ddlDsl_CreateTable, ddlDsl_AlterTableAction, ddlDsl_Constraint, ddlDsl_DropTableConstraint, AlterTableAction, ddlDsl_Comment, ddlDsl_TableComment, Comment, ddlDsl_ColumnComment, ddlDsl_TableProperty, ddlDsl_CreateIndex, TableProperty, ddlDsl_SqlDataType, ddlDsl_ReferenceClause, ddlDsl_Drop, ddlDsl_NullableConstraint, Constraint, ddlDsl_UniqueKeyConstraint, ddlDsl_PrimaryKeyConstraint, ddlDsl_ForeignKeyConstraint, ddlDsl_SqlCharacter, SqlDataType, ddlDsl_SqlNumber, ddlDsl_LongRaw, ddlDsl_Long, LongRaw, ddlDsl_Raw, ddlDsl_SqlDateTime, ddlDsl_SqlDate, SqlDateTime, ddlDsl_SqlTimeStamp, ddlDsl_SqlInterval, ddlDsl_LargeObjectType, ddlDsl_RowIdType, ddlDsl_SqlBoolean, SortDirectionEnum},
    associations={column10, statements0, table1, action2, constraint4, constraintRef6, table8, columns29, properties11, table13, columns15, type18, constraint20, reference23, columns25, columns27, reference31, table34, columns37},
    generalizations={gen_ddlDsl_AddTableConstraint_AlterTableAction, gen_ddlDsl_Create_DdlStatement, gen_ddlDsl_CreateTable_Create, gen_ddlDsl_Alter_DdlStatement, gen_ddlDsl_DropTableConstraint_AlterTableAction, gen_ddlDsl_Comment_DdlStatement, gen_ddlDsl_TableComment_Comment, gen_ddlDsl_ColumnComment_Comment, gen_ddlDsl_CreateIndex_Create, gen_ddlDsl_Column_TableProperty, gen_ddlDsl_Drop_DdlStatement, gen_ddlDsl_Constraint_TableProperty, gen_ddlDsl_NullableConstraint_Constraint, gen_ddlDsl_UniqueKeyConstraint_Constraint, gen_ddlDsl_PrimaryKeyConstraint_Constraint, gen_ddlDsl_ForeignKeyConstraint_Constraint, gen_ddlDsl_SqlCharacter_SqlDataType, gen_ddlDsl_SqlNumber_SqlDataType, gen_ddlDsl_LongRaw_SqlDataType, gen_ddlDsl_Long_LongRaw, gen_ddlDsl_Raw_LongRaw, gen_ddlDsl_SqlDateTime_SqlDataType, gen_ddlDsl_SqlDate_SqlDateTime, gen_ddlDsl_SqlTimeStamp_SqlDateTime, gen_ddlDsl_SqlInterval_SqlDateTime, gen_ddlDsl_LargeObjectType_SqlDataType, gen_ddlDsl_RowIdType_SqlDataType, gen_ddlDsl_SqlBoolean_SqlDataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)