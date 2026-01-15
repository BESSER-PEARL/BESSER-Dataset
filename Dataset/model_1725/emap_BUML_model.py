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
Category: Enumeration = Enumeration(
    name="Category",
    literals={
            EnumerationLiteral(name="Complex"),
			EnumerationLiteral(name="Simple")
    }
)

# Classes
emap_Book = Class(name="emap::Book")
emap_StringToWriterMapEntry = Class(name="emap::StringToWriterMapEntry")
emap_StringToStringMapEntry = Class(name="emap::StringToStringMapEntry")
emap_WriterToStringMapEntry = Class(name="emap::WriterToStringMapEntry")
emap_DateToCategoryMapEntry = Class(name="emap::DateToCategoryMapEntry")
emap_Writer = Class(name="emap::Writer")

# emap_Book class attributes and methods
emap_Book_title: Property = Property(name="title", type=StringType)
emap_Book.attributes={emap_Book_title}

# emap_StringToWriterMapEntry class attributes and methods
emap_StringToWriterMapEntry_key: Property = Property(name="key", type=StringType)
emap_StringToWriterMapEntry.attributes={emap_StringToWriterMapEntry_key}

# emap_StringToStringMapEntry class attributes and methods
emap_StringToStringMapEntry_key: Property = Property(name="key", type=StringType)
emap_StringToStringMapEntry_value: Property = Property(name="value", type=StringType)
emap_StringToStringMapEntry.attributes={emap_StringToStringMapEntry_key, emap_StringToStringMapEntry_value}

# emap_WriterToStringMapEntry class attributes and methods
emap_WriterToStringMapEntry_value: Property = Property(name="value", type=StringType)
emap_WriterToStringMapEntry.attributes={emap_WriterToStringMapEntry_value}

# emap_DateToCategoryMapEntry class attributes and methods
emap_DateToCategoryMapEntry_key: Property = Property(name="key", type=StringType)
emap_DateToCategoryMapEntry_value: Property = Property(name="value", type=StringType)
emap_DateToCategoryMapEntry.attributes={emap_DateToCategoryMapEntry_value, emap_DateToCategoryMapEntry_key}

# emap_Writer class attributes and methods
emap_Writer_name: Property = Property(name="name", type=StringType)
emap_Writer.attributes={emap_Writer_name}

# Relationships
writers0: BinaryAssociation = BinaryAssociation(
    name="writers0",
    ends={
        Property(name="emap_StringToWriterMapEntry", type=emap_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="emap_Book", type=emap_StringToWriterMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
keyWords1: BinaryAssociation = BinaryAssociation(
    name="keyWords1",
    ends={
        Property(name="emap_StringToStringMapEntry", type=emap_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="emap_Book2", type=emap_StringToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
cityByWriter3: BinaryAssociation = BinaryAssociation(
    name="cityByWriter3",
    ends={
        Property(name="emap_WriterToStringMapEntry", type=emap_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="emap_Book4", type=emap_WriterToStringMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
categoryByDate5: BinaryAssociation = BinaryAssociation(
    name="categoryByDate5",
    ends={
        Property(name="emap_DateToCategoryMapEntry", type=emap_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="emap_Book6", type=emap_DateToCategoryMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
key9: BinaryAssociation = BinaryAssociation(
    name="key9",
    ends={
        Property(name="emap_Writer11", type=emap_WriterToStringMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="emap_WriterToStringMapEntry10", type=emap_Writer, multiplicity=Multiplicity(0, 1))
    }
)
value7: BinaryAssociation = BinaryAssociation(
    name="value7",
    ends={
        Property(name="emap_Writer", type=emap_StringToWriterMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="emap_StringToWriterMapEntry8", type=emap_Writer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="emap",
    types={emap_Book, emap_StringToWriterMapEntry, emap_StringToStringMapEntry, emap_WriterToStringMapEntry, emap_DateToCategoryMapEntry, emap_Writer, Category},
    associations={writers0, keyWords1, cityByWriter3, categoryByDate5, key9, value7},
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