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
DataType: Enumeration = Enumeration(
    name="DataType",
    literals={
            EnumerationLiteral(name="varchar"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="number")
    }
)

# Classes
sQL_DataBase = Class(name="sQL::DataBase")
sQL_PrimaryKey = Class(name="sQL::PrimaryKey")
sQL_Table = Class(name="sQL::Table")
sQL_Column = Class(name="sQL::Column")
sQL_ForeignKey = Class(name="sQL::ForeignKey")

# sQL_DataBase class attributes and methods

# sQL_PrimaryKey class attributes and methods

# sQL_Table class attributes and methods
sQL_Table_name: Property = Property(name="name", type=StringType)
sQL_Table.attributes={sQL_Table_name}

# sQL_Column class attributes and methods
sQL_Column_name: Property = Property(name="name", type=StringType)
sQL_Column_type: Property = Property(name="type", type=StringType)
sQL_Column_isNull: Property = Property(name="isNull", type=BooleanType)
sQL_Column.attributes={sQL_Column_name, sQL_Column_type, sQL_Column_isNull}

# sQL_ForeignKey class attributes and methods

# Relationships
primarykey3: BinaryAssociation = BinaryAssociation(
    name="primarykey3",
    ends={
        Property(name="sQL_PrimaryKey", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table4", type=sQL_PrimaryKey, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
table0: BinaryAssociation = BinaryAssociation(
    name="table0",
    ends={
        Property(name="sQL_Table", type=sQL_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_DataBase", type=sQL_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column1: BinaryAssociation = BinaryAssociation(
    name="column1",
    ends={
        Property(name="sQL_Column", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table2", type=sQL_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column7: BinaryAssociation = BinaryAssociation(
    name="column7",
    ends={
        Property(name="sQL_Column9", type=sQL_PrimaryKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_PrimaryKey8", type=sQL_Column, multiplicity=Multiplicity(0, 9999))
    }
)
foreignkey5: BinaryAssociation = BinaryAssociation(
    name="foreignkey5",
    ends={
        Property(name="sQL_ForeignKey", type=sQL_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_Table6", type=sQL_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column10: BinaryAssociation = BinaryAssociation(
    name="column10",
    ends={
        Property(name="sQL_Column12", type=sQL_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_ForeignKey11", type=sQL_Column, multiplicity=Multiplicity(0, 9999))
    }
)
tableRef13: BinaryAssociation = BinaryAssociation(
    name="tableRef13",
    ends={
        Property(name="sQL_Table15", type=sQL_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_ForeignKey14", type=sQL_Table, multiplicity=Multiplicity(0, 1))
    }
)
columnsRef16: BinaryAssociation = BinaryAssociation(
    name="columnsRef16",
    ends={
        Property(name="sQL_Column18", type=sQL_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="sQL_ForeignKey17", type=sQL_Column, multiplicity=Multiplicity(0, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="sQL",
    types={sQL_DataBase, sQL_PrimaryKey, sQL_Table, sQL_Column, sQL_ForeignKey, DataType},
    associations={primarykey3, table0, column1, column7, foreignkey5, column10, tableRef13, columnsRef16},
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