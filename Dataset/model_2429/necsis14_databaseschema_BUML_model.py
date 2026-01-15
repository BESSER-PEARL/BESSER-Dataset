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
NamedElement = Class(name="NamedElement")
necsis14_databaseschema_Column = Class(name="necsis14::databaseschema::Column")
necsis14_databaseschema_DatabaseSchema = Class(name="necsis14::databaseschema::DatabaseSchema")
necsis14_databaseschema_Table = Class(name="necsis14::databaseschema::Table")
necsis14_databaseschema_NamedElement = Class(name="necsis14::databaseschema::NamedElement", is_abstract=True)

# NamedElement class attributes and methods

# necsis14_databaseschema_Column class attributes and methods

# necsis14_databaseschema_DatabaseSchema class attributes and methods

# necsis14_databaseschema_Table class attributes and methods

# necsis14_databaseschema_NamedElement class attributes and methods
necsis14_databaseschema_NamedElement_name: Property = Property(name="name", type=StringType)
necsis14_databaseschema_NamedElement.attributes={necsis14_databaseschema_NamedElement_name}

# Relationships
columns1: BinaryAssociation = BinaryAssociation(
    name="columns1",
    ends={
        Property(name="necsis14_databaseschema_Column", type=necsis14_databaseschema_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_databaseschema_Table2", type=necsis14_databaseschema_Column, multiplicity=Multiplicity(1, 9999), is_composite=True)
    }
)
primaryKeys3: BinaryAssociation = BinaryAssociation(
    name="primaryKeys3",
    ends={
        Property(name="necsis14_databaseschema_Column5", type=necsis14_databaseschema_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_databaseschema_Table4", type=necsis14_databaseschema_Column, multiplicity=Multiplicity(1, 9999))
    }
)
tables0: BinaryAssociation = BinaryAssociation(
    name="tables0",
    ends={
        Property(name="necsis14_databaseschema_Table", type=necsis14_databaseschema_DatabaseSchema, multiplicity=Multiplicity(1, 1)),
        Property(name="necsis14_databaseschema_DatabaseSchema", type=necsis14_databaseschema_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Generalizations
gen_necsis14_databaseschema_Table_NamedElement = Generalization(general=NamedElement, specific=necsis14_databaseschema_Table)
gen_necsis14_databaseschema_Column_NamedElement = Generalization(general=NamedElement, specific=necsis14_databaseschema_Column)

# Domain Model
domain_model = DomainModel(
    name="necsis14_databaseschema",
    types={NamedElement, necsis14_databaseschema_Column, necsis14_databaseschema_DatabaseSchema, necsis14_databaseschema_Table, necsis14_databaseschema_NamedElement},
    associations={columns1, primaryKeys3, tables0},
    generalizations={gen_necsis14_databaseschema_Table_NamedElement, gen_necsis14_databaseschema_Column_NamedElement},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)