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
ColumnType: Enumeration = Enumeration(
    name="ColumnType",
    literals={
            EnumerationLiteral(name="Date"),
			EnumerationLiteral(name="Char"),
			EnumerationLiteral(name="Number")
    }
)

# Classes
my_Table = Class(name="my::Table")
my_Database = Class(name="my::Database")
my_FKRelation = Class(name="my::FKRelation")
my_NamedElement = Class(name="my::NamedElement")
my_Column = Class(name="my::Column")
NamedElement = Class(name="NamedElement")

# my_Table class attributes and methods

# my_Database class attributes and methods

# my_FKRelation class attributes and methods
my_FKRelation_label: Property = Property(name="label", type=StringType)
my_FKRelation.attributes={my_FKRelation_label}

# my_NamedElement class attributes and methods
my_NamedElement_name: Property = Property(name="name", type=StringType)
my_NamedElement.attributes={my_NamedElement_name}

# my_Column class attributes and methods
my_Column_unique: Property = Property(name="unique", type=BooleanType)
my_Column_primary: Property = Property(name="primary", type=BooleanType)
my_Column_size: Property = Property(name="size", type=IntegerType)
my_Column_type: Property = Property(name="type", type=StringType)
my_Column.attributes={my_Column_unique, my_Column_size, my_Column_type, my_Column_primary}

# NamedElement class attributes and methods

# Relationships
columns0: BinaryAssociation = BinaryAssociation(
    name="columns0",
    ends={
        Property(name="my_Column", type=my_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="my_Table", type=my_Column, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="my_Table2", type=my_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="my_Database", type=my_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
fkrelations3: BinaryAssociation = BinaryAssociation(
    name="fkrelations3",
    ends={
        Property(name="my_FKRelation", type=my_Database, multiplicity=Multiplicity(1, 1)),
        Property(name="my_Database4", type=my_FKRelation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
target5: BinaryAssociation = BinaryAssociation(
    name="target5",
    ends={
        Property(name="my_Column7", type=my_FKRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="my_FKRelation6", type=my_Column, multiplicity=Multiplicity(1, 1))
    }
)
source8: BinaryAssociation = BinaryAssociation(
    name="source8",
    ends={
        Property(name="my_Column10", type=my_FKRelation, multiplicity=Multiplicity(1, 1)),
        Property(name="my_FKRelation9", type=my_Column, multiplicity=Multiplicity(1, 1))
    }
)

# Generalizations
gen_my_Table_NamedElement = Generalization(general=NamedElement, specific=my_Table)
gen_my_Database_NamedElement = Generalization(general=NamedElement, specific=my_Database)
gen_my_Column_NamedElement = Generalization(general=NamedElement, specific=my_Column)

# Domain Model
domain_model = DomainModel(
    name="my",
    types={my_Table, my_Database, my_FKRelation, my_NamedElement, my_Column, NamedElement, ColumnType},
    associations={columns0, tables1, fkrelations3, target5, source8},
    generalizations={gen_my_Table_NamedElement, gen_my_Database_NamedElement, gen_my_Column_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)