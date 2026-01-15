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
petrinetDsl_PetriNet = Class(name="petrinetDsl::PetriNet")
petrinetDsl_Resource = Class(name="petrinetDsl::Resource")
petrinetDsl_Place = Class(name="petrinetDsl::Place")
petrinetDsl_Transaction = Class(name="petrinetDsl::Transaction")
petrinetDsl_AssureStatement = Class(name="petrinetDsl::AssureStatement")
petrinetDsl_TakeStatement = Class(name="petrinetDsl::TakeStatement")
petrinetDsl_PutStatement = Class(name="petrinetDsl::PutStatement")
petrinetDsl_Storage = Class(name="petrinetDsl::Storage")

# petrinetDsl_PetriNet class attributes and methods

# petrinetDsl_Resource class attributes and methods
petrinetDsl_Resource_name: Property = Property(name="name", type=StringType)
petrinetDsl_Resource.attributes={petrinetDsl_Resource_name}

# petrinetDsl_Place class attributes and methods
petrinetDsl_Place_name: Property = Property(name="name", type=StringType)
petrinetDsl_Place.attributes={petrinetDsl_Place_name}

# petrinetDsl_Transaction class attributes and methods
petrinetDsl_Transaction_name: Property = Property(name="name", type=StringType)
petrinetDsl_Transaction.attributes={petrinetDsl_Transaction_name}

# petrinetDsl_AssureStatement class attributes and methods
petrinetDsl_AssureStatement_count: Property = Property(name="count", type=IntegerType)
petrinetDsl_AssureStatement.attributes={petrinetDsl_AssureStatement_count}

# petrinetDsl_TakeStatement class attributes and methods
petrinetDsl_TakeStatement_count: Property = Property(name="count", type=IntegerType)
petrinetDsl_TakeStatement.attributes={petrinetDsl_TakeStatement_count}

# petrinetDsl_PutStatement class attributes and methods
petrinetDsl_PutStatement_count: Property = Property(name="count", type=IntegerType)
petrinetDsl_PutStatement.attributes={petrinetDsl_PutStatement_count}

# petrinetDsl_Storage class attributes and methods
petrinetDsl_Storage_count: Property = Property(name="count", type=IntegerType)
petrinetDsl_Storage_capacity: Property = Property(name="capacity", type=IntegerType)
petrinetDsl_Storage.attributes={petrinetDsl_Storage_capacity, petrinetDsl_Storage_count}

# Relationships
resources0: BinaryAssociation = BinaryAssociation(
    name="resources0",
    ends={
        Property(name="petrinetDsl_Resource", type=petrinetDsl_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_PetriNet", type=petrinetDsl_Resource, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
places1: BinaryAssociation = BinaryAssociation(
    name="places1",
    ends={
        Property(name="petrinetDsl_Place", type=petrinetDsl_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_PetriNet2", type=petrinetDsl_Place, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
transactions3: BinaryAssociation = BinaryAssociation(
    name="transactions3",
    ends={
        Property(name="petrinetDsl_Transaction", type=petrinetDsl_PetriNet, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_PetriNet4", type=petrinetDsl_Transaction, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
assureStatements10: BinaryAssociation = BinaryAssociation(
    name="assureStatements10",
    ends={
        Property(name="petrinetDsl_AssureStatement", type=petrinetDsl_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_Transaction11", type=petrinetDsl_AssureStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
takeStatements12: BinaryAssociation = BinaryAssociation(
    name="takeStatements12",
    ends={
        Property(name="petrinetDsl_TakeStatement", type=petrinetDsl_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_Transaction13", type=petrinetDsl_TakeStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
putStatements14: BinaryAssociation = BinaryAssociation(
    name="putStatements14",
    ends={
        Property(name="petrinetDsl_PutStatement", type=petrinetDsl_Transaction, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_Transaction15", type=petrinetDsl_PutStatement, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRef16: BinaryAssociation = BinaryAssociation(
    name="resourceRef16",
    ends={
        Property(name="petrinetDsl_Resource18", type=petrinetDsl_AssureStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_AssureStatement17", type=petrinetDsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
placeRef19: BinaryAssociation = BinaryAssociation(
    name="placeRef19",
    ends={
        Property(name="petrinetDsl_Place21", type=petrinetDsl_AssureStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_AssureStatement20", type=petrinetDsl_Place, multiplicity=Multiplicity(0, 1))
    }
)
storages5: BinaryAssociation = BinaryAssociation(
    name="storages5",
    ends={
        Property(name="petrinetDsl_Storage", type=petrinetDsl_Place, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_Place6", type=petrinetDsl_Storage, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
resourceRef7: BinaryAssociation = BinaryAssociation(
    name="resourceRef7",
    ends={
        Property(name="petrinetDsl_Resource9", type=petrinetDsl_Storage, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_Storage8", type=petrinetDsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
placeRef31: BinaryAssociation = BinaryAssociation(
    name="placeRef31",
    ends={
        Property(name="petrinetDsl_Place33", type=petrinetDsl_PutStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_PutStatement32", type=petrinetDsl_Place, multiplicity=Multiplicity(0, 1))
    }
)
resourceRef22: BinaryAssociation = BinaryAssociation(
    name="resourceRef22",
    ends={
        Property(name="petrinetDsl_Resource24", type=petrinetDsl_TakeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_TakeStatement23", type=petrinetDsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)
placeRef25: BinaryAssociation = BinaryAssociation(
    name="placeRef25",
    ends={
        Property(name="petrinetDsl_Place27", type=petrinetDsl_TakeStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_TakeStatement26", type=petrinetDsl_Place, multiplicity=Multiplicity(0, 1))
    }
)
resourceRef28: BinaryAssociation = BinaryAssociation(
    name="resourceRef28",
    ends={
        Property(name="petrinetDsl_Resource30", type=petrinetDsl_PutStatement, multiplicity=Multiplicity(1, 1)),
        Property(name="petrinetDsl_PutStatement29", type=petrinetDsl_Resource, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="petrinetDsl",
    types={petrinetDsl_PetriNet, petrinetDsl_Resource, petrinetDsl_Place, petrinetDsl_Transaction, petrinetDsl_AssureStatement, petrinetDsl_TakeStatement, petrinetDsl_PutStatement, petrinetDsl_Storage},
    associations={resources0, places1, transactions3, assureStatements10, takeStatements12, putStatements14, resourceRef16, placeRef19, storages5, resourceRef7, placeRef31, resourceRef22, placeRef25, resourceRef28},
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