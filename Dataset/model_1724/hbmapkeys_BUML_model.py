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
hbmapkeys_Writer = Class(name="hbmapkeys_Writer")
hbmapkeys_Book = Class(name="hbmapkeys_Book")
hbmapkeys_StringToWriterMapEntry = Class(name="hbmapkeys_StringToWriterMapEntry")
hbmapkeys_WriterToCityMapEntry = Class(name="hbmapkeys_WriterToCityMapEntry")
hbmapkeys_City = Class(name="hbmapkeys_City")

# hbmapkeys_Writer class attributes and methods
hbmapkeys_Writer_name: Property = Property(name="name", type=StringType)
hbmapkeys_Writer.attributes={hbmapkeys_Writer_name}

# hbmapkeys_Book class attributes and methods
hbmapkeys_Book_title: Property = Property(name="title", type=StringType)
hbmapkeys_Book.attributes={hbmapkeys_Book_title}

# hbmapkeys_StringToWriterMapEntry class attributes and methods
hbmapkeys_StringToWriterMapEntry_key: Property = Property(name="key", type=StringType)
hbmapkeys_StringToWriterMapEntry.attributes={hbmapkeys_StringToWriterMapEntry_key}

# hbmapkeys_WriterToCityMapEntry class attributes and methods

# hbmapkeys_City class attributes and methods
hbmapkeys_City_name: Property = Property(name="name", type=StringType)
hbmapkeys_City.attributes={hbmapkeys_City_name}

# Relationships
cityWriter3: BinaryAssociation = BinaryAssociation(
    name="cityWriter3",
    ends={
        Property(name="hbmapkeys_Writer", type=hbmapkeys_City, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmapkeys_City", type=hbmapkeys_Writer, multiplicity=Multiplicity(1, 1))
    }
)
value4: BinaryAssociation = BinaryAssociation(
    name="value4",
    ends={
        Property(name="hbmapkeys_Writer6", type=hbmapkeys_StringToWriterMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmapkeys_StringToWriterMapEntry5", type=hbmapkeys_Writer, multiplicity=Multiplicity(0, 1))
    }
)
writersByName0: BinaryAssociation = BinaryAssociation(
    name="writersByName0",
    ends={
        Property(name="hbmapkeys_StringToWriterMapEntry", type=hbmapkeys_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmapkeys_Book", type=hbmapkeys_StringToWriterMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cityByWriter1: BinaryAssociation = BinaryAssociation(
    name="cityByWriter1",
    ends={
        Property(name="hbmapkeys_WriterToCityMapEntry", type=hbmapkeys_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmapkeys_Book2", type=hbmapkeys_WriterToCityMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key7: BinaryAssociation = BinaryAssociation(
    name="key7",
    ends={
        Property(name="hbmapkeys_Writer9", type=hbmapkeys_WriterToCityMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmapkeys_WriterToCityMapEntry8", type=hbmapkeys_Writer, multiplicity=Multiplicity(0, 1))
    }
)
value10: BinaryAssociation = BinaryAssociation(
    name="value10",
    ends={
        Property(name="hbmapkeys_City12", type=hbmapkeys_WriterToCityMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="hbmapkeys_WriterToCityMapEntry11", type=hbmapkeys_City, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="hbmapkeys",
    types={hbmapkeys_Writer, hbmapkeys_Book, hbmapkeys_StringToWriterMapEntry, hbmapkeys_WriterToCityMapEntry, hbmapkeys_City},
    associations={cityWriter3, value4, writersByName0, cityByWriter1, key7, value10},
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