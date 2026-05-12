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
RelationalDBContent_NamedElement = Class(name="RelationalDBContent_NamedElement", is_abstract=True)
RelationalDBContent_DataBase = Class(name="RelationalDBContent_DataBase")
NamedElement = Class(name="NamedElement")
Table = Class(name="Table")
RelationalDBContent_Table = Class(name="RelationalDBContent_Table")
DataBase = Class(name="DataBase")
Tuple = Class(name="Tuple")
RelationalDBContent_Tuple = Class(name="RelationalDBContent_Tuple")
TupleElement = Class(name="TupleElement")
RelationalDBContent_TupleElement = Class(name="RelationalDBContent_TupleElement")

# RelationalDBContent_NamedElement class attributes and methods
RelationalDBContent_NamedElement_name: Property = Property(name="name", type=StringType)
RelationalDBContent_NamedElement.attributes={RelationalDBContent_NamedElement_name}

# RelationalDBContent_DataBase class attributes and methods
RelationalDBContent_DataBase_SGBDname: Property = Property(name="SGBDname", type=StringType)
RelationalDBContent_DataBase.attributes={RelationalDBContent_DataBase_SGBDname}

# NamedElement class attributes and methods

# Table class attributes and methods

# RelationalDBContent_Table class attributes and methods

# DataBase class attributes and methods

# Tuple class attributes and methods

# RelationalDBContent_Tuple class attributes and methods

# TupleElement class attributes and methods

# RelationalDBContent_TupleElement class attributes and methods
RelationalDBContent_TupleElement_value: Property = Property(name="value", type=StringType)
RelationalDBContent_TupleElement.attributes={RelationalDBContent_TupleElement_value}

# Relationships
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="Table", type=RelationalDBContent_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="database", type=Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
database1: BinaryAssociation = BinaryAssociation(
    name="database1",
    ends={
        Property(name="DataBase", type=RelationalDBContent_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables", type=DataBase, multiplicity=Multiplicity(1, 1))
    }
)
tuples2: BinaryAssociation = BinaryAssociation(
    name="tuples2",
    ends={
        Property(name="Tuple", type=RelationalDBContent_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="owner", type=Tuple, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
owner3: BinaryAssociation = BinaryAssociation(
    name="owner3",
    ends={
        Property(name="Table4", type=RelationalDBContent_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="tuples", type=Table, multiplicity=Multiplicity(1, 1))
    }
)
elements5: BinaryAssociation = BinaryAssociation(
    name="elements5",
    ends={
        Property(name="TupleElement", type=RelationalDBContent_Tuple, multiplicity=Multiplicity(1, 1)),
        Property(name="tuple", type=TupleElement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tuple6: BinaryAssociation = BinaryAssociation(
    name="tuple6",
    ends={
        Property(name="Tuple7", type=RelationalDBContent_TupleElement, multiplicity=Multiplicity(1, 1)),
        Property(name="elements", type=Tuple, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_RelationalDBContent_DataBase_NamedElement = Generalization(general=NamedElement, specific=RelationalDBContent_DataBase)
gen_RelationalDBContent_Table_NamedElement = Generalization(general=NamedElement, specific=RelationalDBContent_Table)

# Domain Model
domain_model = DomainModel(
    name="PrimitiveTypes",
    types={RelationalDBContent_NamedElement, RelationalDBContent_DataBase, NamedElement, Table, RelationalDBContent_Table, DataBase, Tuple, RelationalDBContent_Tuple, TupleElement, RelationalDBContent_TupleElement},
    associations={tables0, database1, tuples2, owner3, elements5, tuple6},
    generalizations={gen_RelationalDBContent_DataBase_NamedElement, gen_RelationalDBContent_Table_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)