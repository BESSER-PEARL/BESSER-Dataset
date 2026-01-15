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
bookstore_Model = Class(name="bookstore::Model")
bookstore_Ent = Class(name="bookstore::Ent")
bookstore_Person = Class(name="bookstore::Person")
Ent = Class(name="Ent")
bookstore_Book = Class(name="bookstore::Book")
bookstore_Magazine = Class(name="bookstore::Magazine")
bookstore_Dvd = Class(name="bookstore::Dvd")
bookstore_Cd = Class(name="bookstore::Cd")

# bookstore_Model class attributes and methods

# bookstore_Ent class attributes and methods
bookstore_Ent_name: Property = Property(name="name", type=StringType)
bookstore_Ent.attributes={bookstore_Ent_name}

# bookstore_Person class attributes and methods
bookstore_Person_voornaam: Property = Property(name="voornaam", type=StringType)
bookstore_Person_achternaam: Property = Property(name="achternaam", type=StringType)
bookstore_Person.attributes={bookstore_Person_achternaam, bookstore_Person_voornaam}

# Ent class attributes and methods

# bookstore_Book class attributes and methods
bookstore_Book_title: Property = Property(name="title", type=StringType)
bookstore_Book_pages: Property = Property(name="pages", type=IntegerType)
bookstore_Book.attributes={bookstore_Book_pages, bookstore_Book_title}

# bookstore_Magazine class attributes and methods
bookstore_Magazine_title: Property = Property(name="title", type=StringType)
bookstore_Magazine_pages: Property = Property(name="pages", type=IntegerType)
bookstore_Magazine_version: Property = Property(name="version", type=StringType)
bookstore_Magazine.attributes={bookstore_Magazine_pages, bookstore_Magazine_title, bookstore_Magazine_version}

# bookstore_Dvd class attributes and methods
bookstore_Dvd_title: Property = Property(name="title", type=StringType)
bookstore_Dvd.attributes={bookstore_Dvd_title}

# bookstore_Cd class attributes and methods
bookstore_Cd_albumName: Property = Property(name="albumName", type=StringType)
bookstore_Cd_bandArtist: Property = Property(name="bandArtist", type=StringType)
bookstore_Cd.attributes={bookstore_Cd_bandArtist, bookstore_Cd_albumName}

# Relationships
ent0: BinaryAssociation = BinaryAssociation(
    name="ent0",
    ends={
        Property(name="bookstore_Ent", type=bookstore_Model, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Model", type=bookstore_Ent, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
manWife2: BinaryAssociation = BinaryAssociation(
    name="manWife2",
    ends={
        Property(name="bookstore_Person", type=bookstore_Person, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Person1", type=bookstore_Person, multiplicity=Multiplicity(0, 1))
    }
)
sequel4: BinaryAssociation = BinaryAssociation(
    name="sequel4",
    ends={
        Property(name="bookstore_Book", type=bookstore_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Book3", type=bookstore_Book, multiplicity=Multiplicity(0, 1))
    }
)
writer5: BinaryAssociation = BinaryAssociation(
    name="writer5",
    ends={
        Property(name="bookstore_Person7", type=bookstore_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Book6", type=bookstore_Person, multiplicity=Multiplicity(0, 1))
    }
)
writer8: BinaryAssociation = BinaryAssociation(
    name="writer8",
    ends={
        Property(name="bookstore_Person9", type=bookstore_Magazine, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Magazine", type=bookstore_Person, multiplicity=Multiplicity(0, 1))
    }
)
actor10: BinaryAssociation = BinaryAssociation(
    name="actor10",
    ends={
        Property(name="bookstore_Person11", type=bookstore_Dvd, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Dvd", type=bookstore_Person, multiplicity=Multiplicity(0, 9999))
    }
)
book12: BinaryAssociation = BinaryAssociation(
    name="book12",
    ends={
        Property(name="bookstore_Book14", type=bookstore_Dvd, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Dvd13", type=bookstore_Book, multiplicity=Multiplicity(0, 1))
    }
)
writer15: BinaryAssociation = BinaryAssociation(
    name="writer15",
    ends={
        Property(name="bookstore_Person17", type=bookstore_Dvd, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Dvd16", type=bookstore_Person, multiplicity=Multiplicity(0, 1))
    }
)
sequel19: BinaryAssociation = BinaryAssociation(
    name="sequel19",
    ends={
        Property(name="bookstore_Dvd20", type=bookstore_Dvd, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Dvd18", type=bookstore_Dvd, multiplicity=Multiplicity(0, 1))
    }
)
artiesten21: BinaryAssociation = BinaryAssociation(
    name="artiesten21",
    ends={
        Property(name="bookstore_Person22", type=bookstore_Cd, multiplicity=Multiplicity(1, 1)),
        Property(name="bookstore_Cd", type=bookstore_Person, multiplicity=Multiplicity(0, 9999))
    }
)

# Generalizations
gen_bookstore_Person_Ent = Generalization(general=Ent, specific=bookstore_Person)
gen_bookstore_Book_Ent = Generalization(general=Ent, specific=bookstore_Book)
gen_bookstore_Magazine_Ent = Generalization(general=Ent, specific=bookstore_Magazine)
gen_bookstore_Dvd_Ent = Generalization(general=Ent, specific=bookstore_Dvd)
gen_bookstore_Cd_Ent = Generalization(general=Ent, specific=bookstore_Cd)

# Domain Model
domain_model = DomainModel(
    name="bookstore",
    types={bookstore_Model, bookstore_Ent, bookstore_Person, Ent, bookstore_Book, bookstore_Magazine, bookstore_Dvd, bookstore_Cd},
    associations={ent0, manWife2, sequel4, writer5, writer8, actor10, book12, writer15, sequel19, artiesten21},
    generalizations={gen_bookstore_Person_Ent, gen_bookstore_Book_Ent, gen_bookstore_Magazine_Ent, gen_bookstore_Dvd_Ent, gen_bookstore_Cd_Ent},
    metadata=None
)


###################### 
 # PROJECT DEFINITION # 
 ###################### 
from besser.BUML.metamodel.project import Project 
from besser.BUML.metamodel.structural.structural import Metadata
metadata = Metadata(description="New project")
project = Project(name="sampleModel",models=[domain_model],owner="User",metadata=metadata)