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
RelationalDBSchema_Column = Class(name="RelationalDBSchema_Column")
RelationalDBSchema_NamedElement = Class(name="RelationalDBSchema_NamedElement", is_abstract=True)
RelationalDBSchema_DataBase = Class(name="RelationalDBSchema_DataBase")
NamedElement = Class(name="NamedElement")
Table = Class(name="Table")
RelationalDBSchema_Table = Class(name="RelationalDBSchema_Table")
DataBase = Class(name="DataBase")
Column = Class(name="Column")

# RelationalDBSchema_Column class attributes and methods
RelationalDBSchema_Column_dataType: Property = Property(name="dataType", type=StringType)
RelationalDBSchema_Column_null: Property = Property(name="null", type=StringType)
RelationalDBSchema_Column_defaultValue: Property = Property(name="defaultValue", type=StringType)
RelationalDBSchema_Column.attributes={RelationalDBSchema_Column_null, RelationalDBSchema_Column_defaultValue, RelationalDBSchema_Column_dataType}

# RelationalDBSchema_NamedElement class attributes and methods
RelationalDBSchema_NamedElement_name: Property = Property(name="name", type=StringType)
RelationalDBSchema_NamedElement.attributes={RelationalDBSchema_NamedElement_name}

# RelationalDBSchema_DataBase class attributes and methods
RelationalDBSchema_DataBase_SGBDname: Property = Property(name="SGBDname", type=StringType)
RelationalDBSchema_DataBase.attributes={RelationalDBSchema_DataBase_SGBDname}

# NamedElement class attributes and methods

# Table class attributes and methods

# RelationalDBSchema_Table class attributes and methods

# DataBase class attributes and methods

# Column class attributes and methods

# Relationships
columns2: BinaryAssociation = BinaryAssociation(
    name="columns2",
    ends={
        Property(name="Column", type=RelationalDBSchema_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key3: BinaryAssociation = BinaryAssociation(
    name="key3",
    ends={
        Property(name="Column4", type=RelationalDBSchema_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="keyOf", type=Column, multiplicity=Multiplicity(0, 9999))
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=RelationalDBSchema_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="DataBase", type=RelationalDBSchema_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=DataBase, multiplicity=Multiplicity(1, 1))
    }
)
owner5: BinaryAssociation = BinaryAssociation(
    name="owner5",
    ends={
        Property(name="Table6", type=RelationalDBSchema_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="columns", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
keyOf7: BinaryAssociation = BinaryAssociation(
    name="keyOf7",
    ends={
        Property(name="Table8", type=RelationalDBSchema_Column, multiplicity=Multiplicity(1, 1)),
        Property(name="key", type=Table, multiplicity=Multiplicity(0, 1))
    }
)

# Generalizations
gen_RelationalDBSchema_Column_NamedElement = Generalization(general=NamedElement, specific=RelationalDBSchema_Column)
gen_RelationalDBSchema_DataBase_NamedElement = Generalization(general=NamedElement, specific=RelationalDBSchema_DataBase)
gen_RelationalDBSchema_Table_NamedElement = Generalization(general=NamedElement, specific=RelationalDBSchema_Table)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={RelationalDBSchema_Column, RelationalDBSchema_NamedElement, RelationalDBSchema_DataBase, NamedElement, Table, RelationalDBSchema_Table, DataBase, Column},
    associations={columns2, key3, tables0, database1, owner5, keyOf7},
    generalizations={gen_RelationalDBSchema_Column_NamedElement, gen_RelationalDBSchema_DataBase_NamedElement, gen_RelationalDBSchema_Table_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)