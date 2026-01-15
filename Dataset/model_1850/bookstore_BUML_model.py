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
BookStorePackage_BookStore = Class(name="BookStorePackage::BookStore")
BookStorePackage_Book = Class(name="BookStorePackage::Book")
BookStorePackage_TypeParameterTest1_XClass = Class(name="BookStorePackage::TypeParameterTest1::XClass")
BookStorePackage_TypeParameterTest1_ZClass = Class(name="BookStorePackage::TypeParameterTest1::ZClass")
BookStorePackage_TypeParameterTest1_YClass = Class(name="BookStorePackage::TypeParameterTest1::YClass")

# BookStorePackage_BookStore class attributes and methods
BookStorePackage_BookStore_owner: Property = Property(name="owner", type=StringType)
BookStorePackage_BookStore_location: Property = Property(name="location", type=StringType)
BookStorePackage_BookStore.attributes={BookStorePackage_BookStore_owner, BookStorePackage_BookStore_location}

# BookStorePackage_Book class attributes and methods
BookStorePackage_Book_name: Property = Property(name="name", type=StringType)
BookStorePackage_Book_isbn: Property = Property(name="isbn", type=IntegerType)
BookStorePackage_Book.attributes={BookStorePackage_Book_isbn, BookStorePackage_Book_name}

# BookStorePackage_TypeParameterTest1_XClass class attributes and methods
BookStorePackage_TypeParameterTest1_XClass_owner: Property = Property(name="owner", type=StringType)
BookStorePackage_TypeParameterTest1_XClass.attributes={BookStorePackage_TypeParameterTest1_XClass_owner}

# BookStorePackage_TypeParameterTest1_ZClass class attributes and methods

# BookStorePackage_TypeParameterTest1_YClass class attributes and methods

# Relationships
books0: BinaryAssociation = BinaryAssociation(
    name="books0",
    ends={
        Property(name="BookStorePackage_Book", type=BookStorePackage_BookStore, multiplicity=Multiplicity(1, 1)),
        Property(name="BookStorePackage_BookStore", type=BookStorePackage_Book, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="BookStorePackage",
    types={BookStorePackage_BookStore, BookStorePackage_Book, BookStorePackage_TypeParameterTest1_XClass, BookStorePackage_TypeParameterTest1_ZClass, BookStorePackage_TypeParameterTest1_YClass},
    associations={books0},
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