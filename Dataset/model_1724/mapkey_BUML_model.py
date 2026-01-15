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
mapkey_StringToWriterMapEntry = Class(name="mapkey::StringToWriterMapEntry")
mapkey_Book = Class(name="mapkey::Book")
mapkey_Writer = Class(name="mapkey::Writer")

# mapkey_StringToWriterMapEntry class attributes and methods
mapkey_StringToWriterMapEntry_key: Property = Property(name="key", type=StringType)
mapkey_StringToWriterMapEntry.attributes={mapkey_StringToWriterMapEntry_key}

# mapkey_Book class attributes and methods
mapkey_Book_title: Property = Property(name="title", type=StringType)
mapkey_Book.attributes={mapkey_Book_title}

# mapkey_Writer class attributes and methods
mapkey_Writer_name: Property = Property(name="name", type=StringType)
mapkey_Writer.attributes={mapkey_Writer_name}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="mapkey_StringToWriterMapEntry", type=mapkey_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="mapkey_Book", type=mapkey_StringToWriterMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
value1: BinaryAssociation = BinaryAssociation(
    name="value1",
    ends={
        Property(name="mapkey_Writer", type=mapkey_StringToWriterMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="mapkey_StringToWriterMapEntry2", type=mapkey_Writer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="mapkey",
    types={mapkey_StringToWriterMapEntry, mapkey_Book, mapkey_Writer},
    associations={writers0, value1},
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