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
model_Person = Class(name="model::Person")
model_Book = Class(name="model::Book")
model_Library = Class(name="model::Library")
model_Location = Class(name="model::Location")
model_MappedLibrary = Class(name="model::MappedLibrary")

# model_Person class attributes and methods
model_Person_name: Property = Property(name="name", type=StringType)
model_Person.attributes={model_Person_name}

# model_Book class attributes and methods
model_Book_tags: Property = Property(name="tags", type=StringType)
model_Book_data: Property = Property(name="data", type=StringType)
model_Book_title: Property = Property(name="title", type=StringType)
model_Book.attributes={model_Book_data, model_Book_title, model_Book_tags}

# model_Library class attributes and methods

# model_Location class attributes and methods
model_Location_address: Property = Property(name="address", type=StringType)
model_Location_id: Property = Property(name="id", type=StringType)
model_Location.attributes={model_Location_id, model_Location_address}

# model_MappedLibrary class attributes and methods
model_MappedLibrary_books: Property = Property(name="books", type=StringType)
model_MappedLibrary.attributes={model_MappedLibrary_books}

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="Book", type=model_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="authors", type=model_Book, multiplicity=Multiplicity(0, 9999))
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="Person", type=model_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=model_Person, multiplicity=Multiplicity(0, 9999))
    }
)
regularBooks16: BinaryAssociation = BinaryAssociation(
    name="regularBooks16",
    ends={
        Property(name="model_Book18", type=model_MappedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappedLibrary17", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books2: BinaryAssociation = BinaryAssociation(
    name="books2",
    ends={
        Property(name="model_Book", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
location3: BinaryAssociation = BinaryAssociation(
    name="location3",
    ends={
        Property(name="model_Location", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library4", type=model_Location, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
latestBook5: BinaryAssociation = BinaryAssociation(
    name="latestBook5",
    ends={
        Property(name="model_Book7", type=model_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Library6", type=model_Book, multiplicity=Multiplicity(0, 1))
    }
)
featuredBook8: BinaryAssociation = BinaryAssociation(
    name="featuredBook8",
    ends={
        Property(name="model_Book10", type=model_Location, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Location9", type=model_Book, multiplicity=Multiplicity(0, 1))
    }
)
location11: BinaryAssociation = BinaryAssociation(
    name="location11",
    ends={
        Property(name="model_Location12", type=model_MappedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappedLibrary", type=model_Location, multiplicity=Multiplicity(0, 1), is_composite=True)
    }
)
rareBooks13: BinaryAssociation = BinaryAssociation(
    name="rareBooks13",
    ends={
        Property(name="model_Book15", type=model_MappedLibrary, multiplicity=Multiplicity(1, 1)),
        Property(name="model_MappedLibrary14", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Person, model_Book, model_Library, model_Location, model_MappedLibrary},
    associations={books0, authors1, regularBooks16, books2, location3, latestBook5, featuredBook8, location11, rareBooks13},
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