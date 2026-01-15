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
library_EStringToWriterMapEntry = Class(name="library::EStringToWriterMapEntry")
library_Book = Class(name="library::Book")
library_Writer = Class(name="library::Writer")
library_Library = Class(name="library::Library")
library_EStringToBookMapEntry = Class(name="library::EStringToBookMapEntry")

# library_EStringToWriterMapEntry class attributes and methods
library_EStringToWriterMapEntry_key: Property = Property(name="key", type=StringType)
library_EStringToWriterMapEntry.attributes={library_EStringToWriterMapEntry_key}

# library_Book class attributes and methods
library_Book_title: Property = Property(name="title", type=StringType)
library_Book_pages: Property = Property(name="pages", type=IntegerType)
library_Book_category: Property = Property(name="category", type=StringType)
library_Book.attributes={library_Book_pages, library_Book_title, library_Book_category}

# library_Writer class attributes and methods
library_Writer_name: Property = Property(name="name", type=StringType)
library_Writer.attributes={library_Writer_name}

# library_Library class attributes and methods
library_Library_options: Property = Property(name="options", type=StringType)
library_Library_writerByIDMap: Property = Property(name="writerByIDMap", type=StringType)
library_Library_name: Property = Property(name="name", type=StringType)
library_Library.attributes={library_Library_options, library_Library_writerByIDMap, library_Library_name}

# library_EStringToBookMapEntry class attributes and methods
library_EStringToBookMapEntry_key: Property = Property(name="key", type=StringType)
library_EStringToBookMapEntry.attributes={library_EStringToBookMapEntry_key}

# Relationships
bookByTitleMap7: BinaryAssociation = BinaryAssociation(
    name="bookByTitleMap7",
    ends={
        Property(name="library_EStringToBookMapEntry", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library8", type=library_EStringToBookMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
writerByNameMap9: BinaryAssociation = BinaryAssociation(
    name="writerByNameMap9",
    ends={
        Property(name="library_EStringToWriterMapEntry", type=library_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_Library10", type=library_EStringToWriterMapEntry, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books11: BinaryAssociation = BinaryAssociation(
    name="books11",
    ends={
        Property(name="Book", type=library_Writer, multiplicity=Multiplicity(1, 1)),
        Property(name="author", type=library_Book, multiplicity=Multiplicity(0, 9999))
    }
)
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
value12: BinaryAssociation = BinaryAssociation(
    name="value12",
    ends={
        Property(name="library_Book14", type=library_EStringToBookMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EStringToBookMapEntry13", type=library_Book, multiplicity=Multiplicity(0, 1))
    }
)
value15: BinaryAssociation = BinaryAssociation(
    name="value15",
    ends={
        Property(name="library_Writer17", type=library_EStringToWriterMapEntry, multiplicity=Multiplicity(1, 1)),
        Property(name="library_EStringToWriterMapEntry16", type=library_Writer, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_EStringToWriterMapEntry, library_Book, library_Writer, library_Library, library_EStringToBookMapEntry, BookCategory},
    associations={bookByTitleMap7, writerByNameMap9, books11, author0, writers1, books2, specialBooks4, value12, value15},
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