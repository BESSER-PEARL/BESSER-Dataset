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
BookCategory: Enumeration = Enumeration(
    name="BookCategory",
    literals={
            EnumerationLiteral(name="MYSTERY"),
			EnumerationLiteral(name="ScienceFiction"),
			EnumerationLiteral(name="Biography")
    }
)

# Classes
library_Book = Class(name="library::Book")
library_Writer = Class(name="library::Writer")
library_Library = Class(name="library::Library")
library_WriterNameMap = Class(name="library::WriterNameMap")
library_MapOfDataTypes = Class(name="library::MapOfDataTypes")

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book_category: Property = Property(name="category", type=StringType)
library_Book.attributes={library_Book_title, library_Book_pages, library_Book_category}

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Library class attributes and methods
library_Library_name: Property = Property(name="name", type=StringType)
library_Library_bookByTitleMap: Property = Property(name="bookByTitleMap", type=StringType)
library_Library_options: Property = Property(name="options", type=StringType)
library_Library_uRIs_1: Property = Property(name="uRIs_1", type=StringType)
library_Library_map1: Property = Property(name="map1", type=StringType)
library_Library.attributes={library_Library_bookByTitleMap, library_Library_options, library_Library_map1, library_Library_name, library_Library_uRIs_1}

# library_WriterNameMap class attributes and methods
library_WriterNameMap_key: Property = Property(name="key", type=StringType)
library_WriterNameMap.attributes={library_WriterNameMap_key}

# library_MapOfDataTypes class attributes and methods
library_MapOfDataTypes_key: Property = Property(name="key", type=StringType)
library_MapOfDataTypes_value: Property = Property(name="value", type=StringType)
library_MapOfDataTypes.attributes={library_MapOfDataTypes_key, library_MapOfDataTypes_value}

# Relationships
author0: BinaryAssociation = BinaryAssociation(
    name="author0",
    ends={
        Property(name="Writer", type=library_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=library_Writer, multiplicity=Multiplicity(0, 1))
    }
)
writers1: BinaryAssociation = BinaryAssociation(
    name="writers1",
    ends={
        Property(name="library_Writer", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library", type=library_Writer, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="library_Book", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library3", type=library_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
specialBooks4: BinaryAssociation = BinaryAssociation(
    name="specialBooks4",
    ends={
        Property(name="library_Book6", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library5", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
writerByNameMap7: BinaryAssociation = BinaryAssociation(
    name="writerByNameMap7",
    ends={
        Property(name="library_WriterNameMap", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library8", type=library_WriterNameMap, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writerByIDMap9: BinaryAssociation = BinaryAssociation(
    name="writerByIDMap9",
    ends={
        Property(name="library_MapOfDataTypes", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library10", type=library_MapOfDataTypes, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books11: BinaryAssociation = BinaryAssociation(
    name="books11",
    ends={
        Property(name="Book", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
value12: BinaryAssociation = BinaryAssociation(
    name="value12",
    ends={
        Property(name="library_Writer14", type=library_WriterNameMap, multiplicity=Multiplicity(1, 1)),
        Property(name="library_WriterNameMap13", type=library_Writer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_Book, library_Writer, library_Library, library_WriterNameMap, library_MapOfDataTypes, BookCategory},
    associations={author0, writers1, books2, specialBooks4, writerByNameMap7, writerByIDMap9, books11, value12},
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