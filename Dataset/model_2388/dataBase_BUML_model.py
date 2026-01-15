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
RailsData: Enumeration = Enumeration(
    name="RailsData",
    literals={
            EnumerationLiteral(name="binary"),
			EnumerationLiteral(name="boolean"),
			EnumerationLiteral(name="date"),
			EnumerationLiteral(name="dateTime"),
			EnumerationLiteral(name="decimal"),
			EnumerationLiteral(name="float"),
			EnumerationLiteral(name="integer"),
			EnumerationLiteral(name="string"),
			EnumerationLiteral(name="text"),
			EnumerationLiteral(name="time"),
			EnumerationLiteral(name="timestamp")
    }
)

# Classes
database_DataBaseElement = Class(name="database::DataBaseElement", is_abstract=True)
database_Schema = Class(name="database::Schema")
DataBaseElement = Class(name="DataBaseElement")
database_Column = Class(name="database::Column")
database_ForeignKey = Class(name="database::ForeignKey")
database_Table = Class(name="database::Table")

# database_DataBaseElement class attributes and methods
database_DataBaseElement_name: Property = Property(name="name", type=StringType)
database_DataBaseElement.attributes={database_DataBaseElement_name}

# database_Schema class attributes and methods

# DataBaseElement class attributes and methods

# database_Column class attributes and methods
database_Column_type: Property = Property(name="type", type=StringType)
database_Column.attributes={database_Column_type}

# database_ForeignKey class attributes and methods

# database_Table class attributes and methods

# Relationships
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="database_Column", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table2", type=database_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primaryKey3: BinaryAssociation = BinaryAssociation(
    name="primaryKey3",
    ends={
        Property(name="database_Column5", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table4", type=database_Column, multiplicity=Multiplicity(1, 1))
    }
)
foreignKeys6: BinaryAssociation = BinaryAssociation(
    name="foreignKeys6",
    ends={
        Property(name="database_ForeignKey", type=database_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Table7", type=database_ForeignKey, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="database_Table", type=database_Schema, multiplicity=Multiplicity(1, 1)),
        Property(name="database_Schema", type=database_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
column8: BinaryAssociation = BinaryAssociation(
    name="column8",
    ends={
        Property(name="database_Column10", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey9", type=database_Column, multiplicity=Multiplicity(1, 1))
    }
)
reference11: BinaryAssociation = BinaryAssociation(
    name="reference11",
    ends={
        Property(name="database_Table13", type=database_ForeignKey, multiplicity=Multiplicity(1, 1)),
        Property(name="database_ForeignKey12", type=database_Table, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_database_Schema_DataBaseElement = Generalization(general=DataBaseElement, specific=database_Schema)
gen_database_Table_DataBaseElement = Generalization(general=DataBaseElement, specific=database_Table)
gen_database_Column_DataBaseElement = Generalization(general=DataBaseElement, specific=database_Column)

# Domain Model
domain_model = DomainModel(
    name="database",
    types={database_DataBaseElement, database_Schema, DataBaseElement, database_Column, database_ForeignKey, database_Table, RailsData},
    associations={columns1, primaryKey3, foreignKeys6, tables0, column8, reference11},
    generalizations={gen_database_Schema_DataBaseElement, gen_database_Table_DataBaseElement, gen_database_Column_DataBaseElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)