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
library_t_library = Class(name="library::t::library")
library_t_book = Class(name="library::t::book")
library_t_author = Class(name="library::t::author")
library_t_published = Class(name="library::t::published")

# library_t_library class attributes and methods
library_t_library_tagName: Property = Property(name="tagName", type=StringType)
library_t_library_text: Property = Property(name="text", type=StringType)
library_t_library.attributes={library_t_library_text, library_t_library_tagName}

# library_t_book class attributes and methods
library_t_book_text: Property = Property(name="text", type=StringType)
library_t_book_pages: Property = Property(name="pages", type=IntegerType)
library_t_book_title: Property = Property(name="title", type=StringType)
library_t_book_tagName: Property = Property(name="tagName", type=StringType)
library_t_book.attributes={library_t_book_text, library_t_book_title, library_t_book_pages, library_t_book_tagName}

# library_t_author class attributes and methods
library_t_author_tagName: Property = Property(name="tagName", type=StringType)
library_t_author_text: Property = Property(name="text", type=StringType)
library_t_author.attributes={library_t_author_tagName, library_t_author_text}

# library_t_published class attributes and methods
library_t_published_tagName: Property = Property(name="tagName", type=StringType)
library_t_published_text: Property = Property(name="text", type=StringType)
library_t_published.attributes={library_t_published_text, library_t_published_tagName}

# Relationships
book0: BinaryAssociation = BinaryAssociation(
    name="book0",
    ends={
        Property(name="library_t_book", type=library_t_library, multiplicity=Multiplicity(1, 1)),
        Property(name="library_t_library", type=library_t_book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
parentNode1: BinaryAssociation = BinaryAssociation(
    name="parentNode1",
    ends={
        Property(name="library_t_library3", type=library_t_book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_t_book2", type=library_t_library, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
author4: BinaryAssociation = BinaryAssociation(
    name="author4",
    ends={
        Property(name="library_t_author", type=library_t_book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_t_book5", type=library_t_author, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
published6: BinaryAssociation = BinaryAssociation(
    name="published6",
    ends={
        Property(name="library_t_published", type=library_t_book, multiplicity=Multiplicity(1, 1)),
        Property(name="library_t_book7", type=library_t_published, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentNode8: BinaryAssociation = BinaryAssociation(
    name="parentNode8",
    ends={
        Property(name="library_t_book10", type=library_t_author, multiplicity=Multiplicity(1, 1)),
        Property(name="library_t_author9", type=library_t_book, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
parentNode11: BinaryAssociation = BinaryAssociation(
    name="parentNode11",
    ends={
        Property(name="library_t_book13", type=library_t_published, multiplicity=Multiplicity(1, 1)),
        Property(name="library_t_published12", type=library_t_book, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_t_library, library_t_book, library_t_author, library_t_published},
    associations={book0, parentNode1, author4, published6, parentNode8, parentNode11},
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