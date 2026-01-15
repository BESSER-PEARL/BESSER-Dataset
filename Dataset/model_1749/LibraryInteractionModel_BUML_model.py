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
libraryinteractionmodel_Library = Class(name="libraryinteractionmodel::Library")
libraryinteractionmodel_Books = Class(name="libraryinteractionmodel::Books")
libraryinteractionmodel_Authors = Class(name="libraryinteractionmodel::Authors")
libraryinteractionmodel_Reservations = Class(name="libraryinteractionmodel::Reservations")
libraryinteractionmodel_BookShort = Class(name="libraryinteractionmodel::BookShort")
libraryinteractionmodel_Clients = Class(name="libraryinteractionmodel::Clients")
libraryinteractionmodel_Book = Class(name="libraryinteractionmodel::Book")
libraryinteractionmodel_AuthorShort = Class(name="libraryinteractionmodel::AuthorShort")
libraryinteractionmodel_Reservation = Class(name="libraryinteractionmodel::Reservation")
libraryinteractionmodel_Author = Class(name="libraryinteractionmodel::Author")
libraryinteractionmodel_Client = Class(name="libraryinteractionmodel::Client")

# libraryinteractionmodel_Library class attributes and methods

# libraryinteractionmodel_Books class attributes and methods

# libraryinteractionmodel_Authors class attributes and methods

# libraryinteractionmodel_Reservations class attributes and methods

# libraryinteractionmodel_BookShort class attributes and methods
libraryinteractionmodel_BookShort_isbn: Property = Property(name="isbn", type=StringType)
libraryinteractionmodel_BookShort_title: Property = Property(name="title", type=StringType)
libraryinteractionmodel_BookShort.attributes={libraryinteractionmodel_BookShort_title, libraryinteractionmodel_BookShort_isbn}

# libraryinteractionmodel_Clients class attributes and methods

# libraryinteractionmodel_Book class attributes and methods
libraryinteractionmodel_Book_isbn: Property = Property(name="isbn", type=StringType)
libraryinteractionmodel_Book_title: Property = Property(name="title", type=StringType)
libraryinteractionmodel_Book.attributes={libraryinteractionmodel_Book_title, libraryinteractionmodel_Book_isbn}

# libraryinteractionmodel_AuthorShort class attributes and methods
libraryinteractionmodel_AuthorShort_nationality: Property = Property(name="nationality", type=StringType)
libraryinteractionmodel_AuthorShort_name: Property = Property(name="name", type=StringType)
libraryinteractionmodel_AuthorShort.attributes={libraryinteractionmodel_AuthorShort_name, libraryinteractionmodel_AuthorShort_nationality}

# libraryinteractionmodel_Reservation class attributes and methods
libraryinteractionmodel_Reservation_to: Property = Property(name="to", type=DateType)
libraryinteractionmodel_Reservation_from: Property = Property(name="from", type=DateType)
libraryinteractionmodel_Reservation.attributes={libraryinteractionmodel_Reservation_from, libraryinteractionmodel_Reservation_to}

# libraryinteractionmodel_Author class attributes and methods
libraryinteractionmodel_Author_fullBio: Property = Property(name="fullBio", type=StringType)
libraryinteractionmodel_Author_name: Property = Property(name="name", type=StringType)
libraryinteractionmodel_Author_nationality: Property = Property(name="nationality", type=StringType)
libraryinteractionmodel_Author.attributes={libraryinteractionmodel_Author_fullBio, libraryinteractionmodel_Author_nationality, libraryinteractionmodel_Author_name}

# libraryinteractionmodel_Client class attributes and methods
libraryinteractionmodel_Client_name: Property = Property(name="name", type=StringType)
libraryinteractionmodel_Client_email: Property = Property(name="email", type=StringType)
libraryinteractionmodel_Client.attributes={libraryinteractionmodel_Client_email, libraryinteractionmodel_Client_name}

# Relationships
availableBooks0: BinaryAssociation = BinaryAssociation(
    name="availableBooks0",
    ends={
        Property(name="libraryinteractionmodel_Books", type=libraryinteractionmodel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Library", type=libraryinteractionmodel_Books, multiplicity=Multiplicity(1, 1))
    }
)
authors1: BinaryAssociation = BinaryAssociation(
    name="authors1",
    ends={
        Property(name="libraryinteractionmodel_Authors", type=libraryinteractionmodel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Library2", type=libraryinteractionmodel_Authors, multiplicity=Multiplicity(1, 1))
    }
)
reservations8: BinaryAssociation = BinaryAssociation(
    name="reservations8",
    ends={
        Property(name="libraryinteractionmodel_Reservations", type=libraryinteractionmodel_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Book9", type=libraryinteractionmodel_Reservations, multiplicity=Multiplicity(1, 1))
    }
)
items10: BinaryAssociation = BinaryAssociation(
    name="items10",
    ends={
        Property(name="libraryinteractionmodel_BookShort", type=libraryinteractionmodel_Books, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Books11", type=libraryinteractionmodel_BookShort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
clients3: BinaryAssociation = BinaryAssociation(
    name="clients3",
    ends={
        Property(name="libraryinteractionmodel_Clients", type=libraryinteractionmodel_Library, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Library4", type=libraryinteractionmodel_Clients, multiplicity=Multiplicity(1, 1))
    }
)
author5: BinaryAssociation = BinaryAssociation(
    name="author5",
    ends={
        Property(name="libraryinteractionmodel_AuthorShort", type=libraryinteractionmodel_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Book", type=libraryinteractionmodel_AuthorShort, multiplicity=Multiplicity(1, 1), is_composite=True)
    }
)
currentReservation6: BinaryAssociation = BinaryAssociation(
    name="currentReservation6",
    ends={
        Property(name="libraryinteractionmodel_Reservation", type=libraryinteractionmodel_Book, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Book7", type=libraryinteractionmodel_Reservation, multiplicity=Multiplicity(0, 1))
    }
)
items19: BinaryAssociation = BinaryAssociation(
    name="items19",
    ends={
        Property(name="libraryinteractionmodel_Client21", type=libraryinteractionmodel_Clients, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Clients20", type=libraryinteractionmodel_Client, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
client22: BinaryAssociation = BinaryAssociation(
    name="client22",
    ends={
        Property(name="libraryinteractionmodel_Client24", type=libraryinteractionmodel_Reservation, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Reservation23", type=libraryinteractionmodel_Client, multiplicity=Multiplicity(1, 1))
    }
)
items12: BinaryAssociation = BinaryAssociation(
    name="items12",
    ends={
        Property(name="libraryinteractionmodel_AuthorShort14", type=libraryinteractionmodel_Authors, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Authors13", type=libraryinteractionmodel_AuthorShort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
self15: BinaryAssociation = BinaryAssociation(
    name="self15",
    ends={
        Property(name="libraryinteractionmodel_Author", type=libraryinteractionmodel_AuthorShort, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_AuthorShort16", type=libraryinteractionmodel_Author, multiplicity=Multiplicity(1, 1))
    }
)
self18: BinaryAssociation = BinaryAssociation(
    name="self18",
    ends={
        Property(name="libraryinteractionmodel_Client", type=libraryinteractionmodel_Client, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Client17", type=libraryinteractionmodel_Client, multiplicity=Multiplicity(1, 1))
    }
)
self31: BinaryAssociation = BinaryAssociation(
    name="self31",
    ends={
        Property(name="libraryinteractionmodel_Book33", type=libraryinteractionmodel_BookShort, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_BookShort32", type=libraryinteractionmodel_Book, multiplicity=Multiplicity(1, 1))
    }
)
book25: BinaryAssociation = BinaryAssociation(
    name="book25",
    ends={
        Property(name="libraryinteractionmodel_Book27", type=libraryinteractionmodel_Reservation, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Reservation26", type=libraryinteractionmodel_Book, multiplicity=Multiplicity(1, 1))
    }
)
books28: BinaryAssociation = BinaryAssociation(
    name="books28",
    ends={
        Property(name="libraryinteractionmodel_BookShort30", type=libraryinteractionmodel_Author, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Author29", type=libraryinteractionmodel_BookShort, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)
items34: BinaryAssociation = BinaryAssociation(
    name="items34",
    ends={
        Property(name="libraryinteractionmodel_Reservation36", type=libraryinteractionmodel_Reservations, multiplicity=Multiplicity(1, 1)),
        Property(name="libraryinteractionmodel_Reservations35", type=libraryinteractionmodel_Reservation, multiplicity=Multiplicity(0, 9999), is_composite=True)
    }
)

# Domain Model
domain_model = DomainModel(
    name="libraryinteractionmodel",
    types={libraryinteractionmodel_Library, libraryinteractionmodel_Books, libraryinteractionmodel_Authors, libraryinteractionmodel_Reservations, libraryinteractionmodel_BookShort, libraryinteractionmodel_Clients, libraryinteractionmodel_Book, libraryinteractionmodel_AuthorShort, libraryinteractionmodel_Reservation, libraryinteractionmodel_Author, libraryinteractionmodel_Client},
    associations={availableBooks0, authors1, reservations8, items10, clients3, author5, currentReservation6, items19, client22, items12, self15, self18, self31, book25, books28, items34},
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