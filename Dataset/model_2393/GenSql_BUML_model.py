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
TIPO: Enumeration = Enumeration(
    name="TIPO",
    literals={
            EnumerationLiteral(name="date"),
			EnumerationLiteral(name="number"),
			EnumerationLiteral(name="varchar"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="String"),
			EnumerationLiteral(name="boolean")
    }
)

# Classes
genSql_PrimaryKey = Class(name="genSql::PrimaryKey")
genSql_ForeignKey = Class(name="genSql::ForeignKey")
genSql_DataBase = Class(name="genSql::DataBase")
genSql_Table = Class(name="genSql::Table")
genSql_Column = Class(name="genSql::Column")

# genSql_PrimaryKey class attributes and methods

# genSql_ForeignKey class attributes and methods

# genSql_DataBase class attributes and methods

# genSql_Table class attributes and methods
genSql_Table_name: Property = Property(name="name", type=StringType)
genSql_Table.attributes={genSql_Table_name}

# genSql_Column class attributes and methods
genSql_Column_name: Property = Property(name="name", type=StringType)
genSql_Column_SQLType: Property = Property(name="SQLType", type=StringType)
genSql_Column.attributes={genSql_Column_name, genSql_Column_SQLType}

# Relationships
primarykey3: BinaryAssociation = BinaryAssociation(
    name="primarykey3",
    ends={
        Property(name="genSql_PrimaryKey", type=genSql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="genSql_Table4", type=genSql_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
foreignkeys5: BinaryAssociation = BinaryAssociation(
    name="foreignkeys5",
    ends={
        Property(name="genSql_ForeignKey", type=genSql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="genSql_Table6", type=genSql_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="genSql_Table", type=genSql_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="genSql_DataBase", type=genSql_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="genSql_Column", type=genSql_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="genSql_Table2", type=genSql_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns7: BinaryAssociation = BinaryAssociation(
    name="columns7",
    ends={
        Property(name="genSql_Column9", type=genSql_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="genSql_PrimaryKey8", type=genSql_Column, multiplicity=Multiplicity(0, 9999))
    }
)
columns10: BinaryAssociation = BinaryAssociation(
    name="columns10",
    ends={
        Property(name="genSql_Column12", type=genSql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="genSql_ForeignKey11", type=genSql_Column, multiplicity=Multiplicity(0, 9999))
    }
)
tableRef13: BinaryAssociation = BinaryAssociation(
    name="tableRef13",
    ends={
        Property(name="genSql_Table15", type=genSql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="genSql_ForeignKey14", type=genSql_Table, multiplicity=Multiplicity(0, 1))
    }
)
columnsRef16: BinaryAssociation = BinaryAssociation(
    name="columnsRef16",
    ends={
        Property(name="genSql_Column18", type=genSql_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="genSql_ForeignKey17", type=genSql_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="genSql",
    types={genSql_PrimaryKey, genSql_ForeignKey, genSql_DataBase, genSql_Table, genSql_Column, TIPO},
    associations={primarykey3, foreignkeys5, tables0, columns1, columns7, columns10, tableRef13, columnsRef16},
    generalizations={},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)