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
schoollibrary_Asset = Class(name="schoollibrary::Asset")
schoollibrary_SchoolBook = Class(name="schoollibrary::SchoolBook")
Book = Class(name="Book")
Asset = Class(name="Asset")
schoollibrary_SchoolLibrary = Class(name="schoollibrary::SchoolLibrary")
Library = Class(name="Library")

# schoollibrary_Asset class attributes and methods
schoollibrary_Asset_value: Property = Property(name="value", type=FloatType)
schoollibrary_Asset.attributes={schoollibrary_Asset_value}

# schoollibrary_SchoolBook class attributes and methods

# Book class attributes and methods

# Asset class attributes and methods

# schoollibrary_SchoolLibrary class attributes and methods
schoollibrary_SchoolLibrary_location: Property = Property(name="location", type=StringType)
schoollibrary_SchoolLibrary.attributes={schoollibrary_SchoolLibrary_location}

# Library class attributes and methods

# Generalizations
gen_schoollibrary_SchoolBook_Book = Generalization(general=Book, specific=schoollibrary_SchoolBook)
gen_schoollibrary_SchoolBook_Asset = Generalization(general=Asset, specific=schoollibrary_SchoolBook)
gen_schoollibrary_SchoolLibrary_Library = Generalization(general=Library, specific=schoollibrary_SchoolLibrary)

# Domain Model
domain_model = DomainModel(
    name="schoollibrary",
    types={schoollibrary_Asset, schoollibrary_SchoolBook, Book, Asset, schoollibrary_SchoolLibrary, Library},
    associations={},
    generalizations={gen_schoollibrary_SchoolBook_Book, gen_schoollibrary_SchoolBook_Asset, gen_schoollibrary_SchoolLibrary_Library},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)