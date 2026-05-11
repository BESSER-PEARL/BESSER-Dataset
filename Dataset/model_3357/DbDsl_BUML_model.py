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
dbDsl_NumberType = Class(name="dbDsl_NumberType")
dbDsl_Root = Class(name="dbDsl_Root")
dbDsl_Database = Class(name="dbDsl_Database")
Root = Class(name="Root")
dbDsl_Table = Class(name="dbDsl_Table")
dbDsl_Column = Class(name="dbDsl_Column")
dbDsl_AbstractDataType = Class(name="dbDsl_AbstractDataType")
dbDsl_AbstractColumnMapper = Class(name="dbDsl_AbstractColumnMapper")
dbDsl_CharType = Class(name="dbDsl_CharType")
AbstractDataType = Class(name="AbstractDataType")

# dbDsl_NumberType class attributes and methods

# dbDsl_Root class attributes and methods

# dbDsl_Database class attributes and methods
dbDsl_Database_name: Property = Property(name="name", type=StringType)
dbDsl_Database.attributes={dbDsl_Database_name}

# Root class attributes and methods

# dbDsl_Table class attributes and methods
dbDsl_Table_name: Property = Property(name="name", type=StringType)
dbDsl_Table.attributes={dbDsl_Table_name}

# dbDsl_Column class attributes and methods
dbDsl_Column_name: Property = Property(name="name", type=StringType)
dbDsl_Column.attributes={dbDsl_Column_name}

# dbDsl_AbstractDataType class attributes and methods

# dbDsl_AbstractColumnMapper class attributes and methods

# dbDsl_CharType class attributes and methods

# AbstractDataType class attributes and methods

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="dbDsl_Table", type=dbDsl_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="dbDsl_Database", type=dbDsl_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="dbDsl_Column", type=dbDsl_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="dbDsl_Table2", type=dbDsl_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
type3: BinaryAssociation = BinaryAssociation(
    name="type3",
    ends={
        Property(name="dbDsl_AbstractDataType", type=dbDsl_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="dbDsl_Column4", type=dbDsl_AbstractDataType, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
mapper5: BinaryAssociation = BinaryAssociation(
    name="mapper5",
    ends={
        Property(name="dbDsl_AbstractColumnMapper", type=dbDsl_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="dbDsl_Column6", type=dbDsl_AbstractColumnMapper, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Generalizations
gen_dbDsl_NumberType_AbstractDataType = Generalization(general=AbstractDataType, specific=dbDsl_NumberType)
gen_dbDsl_Database_Root = Generalization(general=Root, specific=dbDsl_Database)
gen_dbDsl_CharType_AbstractDataType = Generalization(general=AbstractDataType, specific=dbDsl_CharType)

# Domain Model
domain_model = DomainModel(
    name="dbDsl",
    types={dbDsl_NumberType, dbDsl_Root, dbDsl_Database, Root, dbDsl_Table, dbDsl_Column, dbDsl_AbstractDataType, dbDsl_AbstractColumnMapper, dbDsl_CharType, AbstractDataType},
    associations={tables0, columns1, type3, mapper5},
    generalizations={gen_dbDsl_NumberType_AbstractDataType, gen_dbDsl_Database_Root, gen_dbDsl_CharType_AbstractDataType},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)