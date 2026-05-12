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
librarian = Class(name="librarian")
patron = Class(name="patron")
Book = Class(name="Book")
library_data_base = Class(name="library_data_base")

# librarian class attributes and methods
librarian_name: Property = Property(name="name", type=StringType)
librarian_username: Property = Property(name="username", type=IntegerType)
librarian.attributes={librarian_name, librarian_username}

# patron class attributes and methods
patron_Address: Property = Property(name="Address", type=StringType)
patron_Name: Property = Property(name="Name", type=StringType)
patron_Contact_number: Property = Property(name="Contact_number", type=IntegerType)
patron.attributes={patron_Name, patron_Contact_number, patron_Address}

# Book class attributes and methods
Book_Book_ISBN: Property = Property(name="Book_ISBN", type=IntegerType)
Book_book_name: Property = Property(name="book_name", type=StringType)
Book_Book_Author: Property = Property(name="Book_Author", type=IntegerType)
Book.attributes={Book_book_name, Book_Book_Author, Book_Book_ISBN}

# library_data_base class attributes and methods
library_data_base_list_of_books: Property = Property(name="list_of_books", type=StringType)
library_data_base_members_information: Property = Property(name="members_information", type=StringType)
library_data_base_record_patron_borrowing_book: Property = Property(name="record_patron_borrowing_book", type=IntegerType)
library_data_base.attributes={library_data_base_record_patron_borrowing_book, library_data_base_members_information, library_data_base_list_of_books}

# Domain Model
domain_model = DomainModel(
    name="_OJNm8FHcEemyf9F2UZM0TQ",
    types={librarian, patron, Book, library_data_base},
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