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
DDL_Statement = Class(name="DDL::Statement")
DDL_DataDefinition = Class(name="DDL::DataDefinition")
Statement = Class(name="Statement")
DDL_CreatePk = Class(name="DDL::CreatePk")
DDL_CreateCk = Class(name="DDL::CreateCk")
DDL_CreateColumn = Class(name="DDL::CreateColumn")
DDL_CreateDatabase = Class(name="DDL::CreateDatabase")
DataDefinition = Class(name="DataDefinition")
DDL_CreateFk = Class(name="DDL::CreateFk")
DDL_CreateTable = Class(name="DDL::CreateTable")
DDL_CreateCommentTable = Class(name="DDL::CreateCommentTable")
DDL_CreateCommentColumn = Class(name="DDL::CreateCommentColumn")
DDL_DDLDefinition = Class(name="DDL::DDLDefinition")

# DDL_Statement class attributes and methods

# DDL_DataDefinition class attributes and methods

# Statement class attributes and methods

# DDL_CreatePk class attributes and methods
DDL_CreatePk_namePk: Property = Property(name="namePk", type=StringType)
DDL_CreatePk_columnName: Property = Property(name="columnName", type=StringType)
DDL_CreatePk.attributes={DDL_CreatePk_namePk, DDL_CreatePk_columnName}

# DDL_CreateCk class attributes and methods
DDL_CreateCk_nameCk: Property = Property(name="nameCk", type=StringType)
DDL_CreateCk_valuesCk: Property = Property(name="valuesCk", type=StringType)
DDL_CreateCk_columnName: Property = Property(name="columnName", type=StringType)
DDL_CreateCk.attributes={DDL_CreateCk_nameCk, DDL_CreateCk_columnName, DDL_CreateCk_valuesCk}

# DDL_CreateColumn class attributes and methods
DDL_CreateColumn_columnName: Property = Property(name="columnName", type=StringType)
DDL_CreateColumn_commentColumn: Property = Property(name="commentColumn", type=StringType)
DDL_CreateColumn_columnType: Property = Property(name="columnType", type=StringType)
DDL_CreateColumn_columnNull: Property = Property(name="columnNull", type=BooleanType)
DDL_CreateColumn.attributes={DDL_CreateColumn_columnType, DDL_CreateColumn_columnNull, DDL_CreateColumn_columnName, DDL_CreateColumn_commentColumn}

# DDL_CreateDatabase class attributes and methods
DDL_CreateDatabase_databaseName: Property = Property(name="databaseName", type=StringType)
DDL_CreateDatabase.attributes={DDL_CreateDatabase_databaseName}

# DataDefinition class attributes and methods

# DDL_CreateFk class attributes and methods
DDL_CreateFk_columnReference: Property = Property(name="columnReference", type=StringType)
DDL_CreateFk_nameFk: Property = Property(name="nameFk", type=StringType)
DDL_CreateFk_columnName: Property = Property(name="columnName", type=StringType)
DDL_CreateFk.attributes={DDL_CreateFk_columnReference, DDL_CreateFk_nameFk, DDL_CreateFk_columnName}

# DDL_CreateTable class attributes and methods
DDL_CreateTable_tableName: Property = Property(name="tableName", type=StringType)
DDL_CreateTable_commentTable: Property = Property(name="commentTable", type=StringType)
DDL_CreateTable.attributes={DDL_CreateTable_commentTable, DDL_CreateTable_tableName}

# DDL_CreateCommentTable class attributes and methods
DDL_CreateCommentTable_tableName: Property = Property(name="tableName", type=StringType)
DDL_CreateCommentTable_tableComment: Property = Property(name="tableComment", type=StringType)
DDL_CreateCommentTable.attributes={DDL_CreateCommentTable_tableComment, DDL_CreateCommentTable_tableName}

# DDL_CreateCommentColumn class attributes and methods
DDL_CreateCommentColumn_tableName: Property = Property(name="tableName", type=StringType)
DDL_CreateCommentColumn_columnName: Property = Property(name="columnName", type=StringType)
DDL_CreateCommentColumn_columnComment: Property = Property(name="columnComment", type=StringType)
DDL_CreateCommentColumn.attributes={DDL_CreateCommentColumn_columnName, DDL_CreateCommentColumn_columnComment, DDL_CreateCommentColumn_tableName}

# DDL_DDLDefinition class attributes and methods

# Relationships
references0: BinaryAssociation = BinaryAssociation(
    name="references0",
    ends={
        Property(name="DDL_CreateTable", type=DDL_CreateFk, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_CreateFk", type=DDL_CreateTable, multiplicity=Multiplicity(0, 1))
    }
)
checks8: BinaryAssociation = BinaryAssociation(
    name="checks8",
    ends={
        Property(name="DDL_CreateCk", type=DDL_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_CreateTable9", type=DDL_CreateCk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
statements10: BinaryAssociation = BinaryAssociation(
    name="statements10",
    ends={
        Property(name="DDL_Statement", type=DDL_DDLDefinition, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_DDLDefinition", type=DDL_Statement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="DDL_CreateColumn", type=DDL_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_CreateTable2", type=DDL_CreateColumn, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columnsPk3: BinaryAssociation = BinaryAssociation(
    name="columnsPk3",
    ends={
        Property(name="DDL_CreatePk", type=DDL_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_CreateTable4", type=DDL_CreatePk, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columnsFk5: BinaryAssociation = BinaryAssociation(
    name="columnsFk5",
    ends={
        Property(name="DDL_CreateFk7", type=DDL_CreateTable, multiplicity=Multiplicity(1, 1)),
        Property(name="DDL_CreateTable6", type=DDL_CreateFk, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_DDL_DataDefinition_Statement = Generalization(general=Statement, specific=DDL_DataDefinition)
gen_DDL_CreateDatabase_DataDefinition = Generalization(general=DataDefinition, specific=DDL_CreateDatabase)
gen_DDL_CreateTable_DataDefinition = Generalization(general=DataDefinition, specific=DDL_CreateTable)
gen_DDL_CreateCommentTable_DataDefinition = Generalization(general=DataDefinition, specific=DDL_CreateCommentTable)
gen_DDL_CreateCommentColumn_DataDefinition = Generalization(general=DataDefinition, specific=DDL_CreateCommentColumn)

# Domain Model
domain_model = DomainModel(
    name="DDL",
    types={DDL_Statement, DDL_DataDefinition, Statement, DDL_CreatePk, DDL_CreateCk, DDL_CreateColumn, DDL_CreateDatabase, DataDefinition, DDL_CreateFk, DDL_CreateTable, DDL_CreateCommentTable, DDL_CreateCommentColumn, DDL_DDLDefinition},
    associations={references0, checks8, statements10, columns1, columnsPk3, columnsFk5},
    generalizations={gen_DDL_DataDefinition_Statement, gen_DDL_CreateDatabase_DataDefinition, gen_DDL_CreateTable_DataDefinition, gen_DDL_CreateCommentTable_DataDefinition, gen_DDL_CreateCommentColumn_DataDefinition},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)