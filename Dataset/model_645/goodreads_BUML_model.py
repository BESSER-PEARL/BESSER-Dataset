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
model_Book = Class(name="model::Book")
model_BookShelf = Class(name="model::BookShelf")
model_Person = Class(name="model::Person")
model_DataBase = Class(name="model::DataBase")

# model_Book class attributes and methods
model_Book_name: Property = Property(name="name", type=StringType)
model_Book_author: Property = Property(name="author", type=StringType)
model_Book_avgRating: Property = Property(name="avgRating", type=IntegerType)
model_Book.attributes={model_Book_name, model_Book_avgRating, model_Book_author}

# model_BookShelf class attributes and methods
model_BookShelf_name: Property = Property(name="name", type=StringType)
model_BookShelf.attributes={model_BookShelf_name}

# model_Person class attributes and methods
model_Person_name: Property = Property(name="name", type=StringType)
model_Person.attributes={model_Person_name}

# model_DataBase class attributes and methods

# Relationships
presentIn0: BinaryAssociation = BinaryAssociation(
    name="presentIn0",
    ends={
        Property(name="BookShelf", type=model_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="books", type=model_BookShelf, multiplicity=Multiplicity(0, 9999))
    }
)
shelves1: BinaryAssociation = BinaryAssociation(
    name="shelves1",
    ends={
        Property(name="BookShelf2", type=model_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="ownedBy", type=model_BookShelf, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
friends4: BinaryAssociation = BinaryAssociation(
    name="friends4",
    ends={
        Property(name="model_Person", type=model_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="model_Person3", type=model_Person, multiplicity=Multiplicity(0, 9999))
    }
)
books5: BinaryAssociation = BinaryAssociation(
    name="books5",
    ends={
        Property(name="Book", type=model_BookShelf, multiplicity=Multiplicity(1, 1)),
        Property(name="presentIn", type=model_Book, multiplicity=Multiplicity(0, 9999))
    }
)
ownedBy6: BinaryAssociation = BinaryAssociation(
    name="ownedBy6",
    ends={
        Property(name="Person", type=model_BookShelf, multiplicity=Multiplicity(1, 1)),
        Property(name="shelves", type=model_Person, multiplicity=Multiplicity(1, 1))
    }
)
people7: BinaryAssociation = BinaryAssociation(
    name="people7",
    ends={
        Property(name="model_Person8", type=model_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DataBase", type=model_Person, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
books9: BinaryAssociation = BinaryAssociation(
    name="books9",
    ends={
        Property(name="model_Book", type=model_DataBase, multiplicity=Multiplicity(1, 1)),
        Property(name="model_DataBase10", type=model_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="model",
    types={model_Book, model_BookShelf, model_Person, model_DataBase},
    associations={presentIn0, shelves1, friends4, books5, ownedBy6, people7, books9},
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