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
Type: Enumeration = Enumeration(
    name="Type",
    literals={
            EnumerationLiteral(name="ascii"),
			EnumerationLiteral(name="blob"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="counter"),
			EnumerationLiteral(name="decimal"),
			EnumerationLiteral(name="double"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="int"),
			EnumerationLiteral(name="text"),
			EnumerationLiteral(name="timestamp"),
			EnumerationLiteral(name="uuid"),
			EnumerationLiteral(name="timeuuid"),
			EnumerationLiteral(name="varchar"),
			EnumerationLiteral(name="varint"),
			EnumerationLiteral(name="bigint")
    }
)

# Classes
nosql_KeySpace = Class(name="nosql::KeySpace")
nosql_Index = Class(name="nosql::Index")
nosql_ColumnFamily = Class(name="nosql::ColumnFamily")
nosql_Options = Class(name="nosql::Options")
nosql_PK = Class(name="nosql::PK")
nosql_Row = Class(name="nosql::Row")
nosql_Column = Class(name="nosql::Column")
ColumnFamily = Class(name="ColumnFamily")
nosql_Cell = Class(name="nosql::Cell")

# nosql_KeySpace class attributes and methods
nosql_KeySpace_name: Property = Property(name="name", type=StringType)
nosql_KeySpace.attributes={nosql_KeySpace_name}

# nosql_Index class attributes and methods
nosql_Index_name: Property = Property(name="name", type=StringType)
nosql_Index_reference: Property = Property(name="reference", type=StringType)
nosql_Index.attributes={nosql_Index_name, nosql_Index_reference}

# nosql_ColumnFamily class attributes and methods
nosql_ColumnFamily_name: Property = Property(name="name", type=StringType)
nosql_ColumnFamily_comment: Property = Property(name="comment", type=StringType)
nosql_ColumnFamily.attributes={nosql_ColumnFamily_comment, nosql_ColumnFamily_name}

# nosql_Options class attributes and methods
nosql_Options_name: Property = Property(name="name", type=StringType)
nosql_Options_value: Property = Property(name="value", type=StringType)
nosql_Options.attributes={nosql_Options_name, nosql_Options_value}

# nosql_PK class attributes and methods

# nosql_Row class attributes and methods

# nosql_Column class attributes and methods
nosql_Column_name: Property = Property(name="name", type=StringType)
nosql_Column_datatype: Property = Property(name="datatype", type=StringType)
nosql_Column_size: Property = Property(name="size", type=StringType)
nosql_Column.attributes={nosql_Column_name, nosql_Column_datatype, nosql_Column_size}

# ColumnFamily class attributes and methods

# nosql_Cell class attributes and methods
nosql_Cell_value: Property = Property(name="value", type=StringType)
nosql_Cell.attributes={nosql_Cell_value}

# Relationships
idexes0: BinaryAssociation = BinaryAssociation(
    name="idexes0",
    ends={
        Property(name="nosql_Index", type=nosql_KeySpace, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_KeySpace", type=nosql_Index, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
families1: BinaryAssociation = BinaryAssociation(
    name="families1",
    ends={
        Property(name="nosql_ColumnFamily", type=nosql_KeySpace, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_KeySpace2", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
EReference03: BinaryAssociation = BinaryAssociation(
    name="EReference03",
    ends={
        Property(name="nosql_Options", type=nosql_KeySpace, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_KeySpace4", type=nosql_Options, multiplicity=Multiplicity(0, 1))
    }
)
options5: BinaryAssociation = BinaryAssociation(
    name="options5",
    ends={
        Property(name="nosql_Options7", type=nosql_KeySpace, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_KeySpace6", type=nosql_Options, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
hasPK8: BinaryAssociation = BinaryAssociation(
    name="hasPK8",
    ends={
        Property(name="nosql_PK", type=nosql_KeySpace, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_KeySpace9", type=nosql_PK, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns12: BinaryAssociation = BinaryAssociation(
    name="columns12",
    ends={
        Property(name="nosql_Column14", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_ColumnFamily13", type=nosql_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
options15: BinaryAssociation = BinaryAssociation(
    name="options15",
    ends={
        Property(name="nosql_Options17", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_ColumnFamily16", type=nosql_Options, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
PK18: BinaryAssociation = BinaryAssociation(
    name="PK18",
    ends={
        Property(name="nosql_PK20", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_ColumnFamily19", type=nosql_PK, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
rows21: BinaryAssociation = BinaryAssociation(
    name="rows21",
    ends={
        Property(name="nosql_Row", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_ColumnFamily22", type=nosql_Row, multiplicity=Multiplicity(0, 9999))
    }
)
keyspace23: BinaryAssociation = BinaryAssociation(
    name="keyspace23",
    ends={
        Property(name="nosql_KeySpace25", type=nosql_ColumnFamily, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_ColumnFamily24", type=nosql_KeySpace, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
applyTo10: BinaryAssociation = BinaryAssociation(
    name="applyTo10",
    ends={
        Property(name="nosql_Column", type=nosql_Index, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_Index11", type=nosql_Column, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
columns29: BinaryAssociation = BinaryAssociation(
    name="columns29",
    ends={
        Property(name="nosql_Column31", type=nosql_PK, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_PK30", type=nosql_Column, multiplicity=Multiplicity(1, 9999))
    }
)
cells32: BinaryAssociation = BinaryAssociation(
    name="cells32",
    ends={
        Property(name="nosql_Cell", type=nosql_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_Row33", type=nosql_Cell, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
columnFamily26: BinaryAssociation = BinaryAssociation(
    name="columnFamily26",
    ends={
        Property(name="nosql_ColumnFamily28", type=nosql_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_Column27", type=nosql_ColumnFamily, multiplicity=Multiplicity(0, 1))
    }
)
column37: BinaryAssociation = BinaryAssociation(
    name="column37",
    ends={
        Property(name="nosql_Column39", type=nosql_Cell, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_Cell38", type=nosql_Column, multiplicity=Multiplicity(1, 1))
    }
)
additionalColumns34: BinaryAssociation = BinaryAssociation(
    name="additionalColumns34",
    ends={
        Property(name="nosql_Column36", type=nosql_Row, multiplicity=Multiplicity(1, 1)),
        Property(name="nosql_Row35", type=nosql_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)

# Generalizations
gen_nosql_Row_ColumnFamily = Generalization(general=ColumnFamily, specific=nosql_Row)

# Domain Model
domain_model = DomainModel(
    name="nosql",
    types={nosql_KeySpace, nosql_Index, nosql_ColumnFamily, nosql_Options, nosql_PK, nosql_Row, nosql_Column, ColumnFamily, nosql_Cell, Type},
    associations={idexes0, families1, EReference03, options5, hasPK8, columns12, options15, PK18, rows21, keyspace23, applyTo10, columns29, cells32, columnFamily26, column37, additionalColumns34},
    generalizations={gen_nosql_Row_ColumnFamily},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)