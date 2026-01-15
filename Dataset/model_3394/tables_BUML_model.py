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
tables_Table = Class(name="tables::Table")
tables_Chair = Class(name="tables::Chair")
tables_Waitress = Class(name="tables::Waitress")
tables_Restaurant = Class(name="tables::Restaurant")

# tables_Table class attributes and methods
tables_Table_id: Property = Property(name="id", type=IntegerType)
tables_Table_isReserved: Property = Property(name="isReserved", type=BooleanType)
tables_Table.attributes={tables_Table_isReserved, tables_Table_id}

# tables_Chair class attributes and methods
tables_Chair_order: Property = Property(name="order", type=IntegerType)
tables_Chair.attributes={tables_Chair_order}

# tables_Waitress class attributes and methods
tables_Waitress_name: Property = Property(name="name", type=StringType)
tables_Waitress.attributes={tables_Waitress_name}

# tables_Restaurant class attributes and methods

# Relationships
chairs0: BinaryAssociation = BinaryAssociation(
    name="chairs0",
    ends={
        Property(name="tables_Chair", type=tables_Table, multiplicity=Multiplicity(1, 1)),
        Property(name="tables_Table", type=tables_Chair, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables1: BinaryAssociation = BinaryAssociation(
    name="tables1",
    ends={
        Property(name="tables_Table2", type=tables_Waitress, multiplicity=Multiplicity(1, 1)),
        Property(name="tables_Waitress", type=tables_Table, multiplicity=Multiplicity(0, 9999))
    }
)
waitress3: BinaryAssociation = BinaryAssociation(
    name="waitress3",
    ends={
        Property(name="tables_Waitress4", type=tables_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="tables_Restaurant", type=tables_Waitress, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
tables5: BinaryAssociation = BinaryAssociation(
    name="tables5",
    ends={
        Property(name="tables_Table7", type=tables_Restaurant, multiplicity=Multiplicity(1, 1)),
        Property(name="tables_Restaurant6", type=tables_Table, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="tables",
    types={tables_Table, tables_Chair, tables_Waitress, tables_Restaurant},
    associations={chairs0, tables1, waitress3, tables5},
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