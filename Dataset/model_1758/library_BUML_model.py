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
library_book = Class(name="library::book")

# library_book class attributes and methods
library_book_pages: Property = Property(name="pages", type=StringType)
library_book_title: Property = Property(name="title", type=StringType)
library_book_author: Property = Property(name="author", type=StringType)
library_book_published: Property = Property(name="published", type=StringType)
library_book.attributes={library_book_pages, library_book_published, library_book_author, library_book_title}

# Domain Model
domain_model = DomainModel(
    name="library",
    types={library_book},
    associations={},
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