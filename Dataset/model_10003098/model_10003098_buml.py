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
Librarian_Actor = Class(name="Librarian_Actor")
Issue_card_UseCase = Class(name="Issue_card_UseCase")
Manage_Books_UseCase = Class(name="Manage_Books_UseCase")
Issue_Book_UseCase = Class(name="Issue_Book_UseCase")
Return_book_UseCase = Class(name="Return_book_UseCase")
Maintain_Patron_profile_UseCase = Class(name="Maintain_Patron_profile_UseCase")
Add_books_UseCase = Class(name="Add_books_UseCase")
Remove_Books_UseCase = Class(name="Remove_Books_UseCase")
Update_Books_UseCase = Class(name="Update_Books_UseCase")
Late_fees_UseCase = Class(name="Late_fees_UseCase")
Renew_Patron_UseCase = Class(name="Renew_Patron_UseCase")
Create_library_account_UseCase = Class(name="Create_library_account_UseCase")
Request_Book_UseCase = Class(name="Request_Book_UseCase")
Checkout_book_UseCase = Class(name="Checkout_book_UseCase")
create_UseCase = Class(name="create_UseCase")
Cancel_UseCase = Class(name="Cancel_UseCase")
Patron_Actor = Class(name="Patron_Actor")
Library_Management_Component = Class(name="Library_Management_Component")
MyClass = Class(name="MyClass")
Library = Class(name="Library")

# Librarian_Actor class attributes and methods

# Issue_card_UseCase class attributes and methods

# Manage_Books_UseCase class attributes and methods

# Issue_Book_UseCase class attributes and methods

# Return_book_UseCase class attributes and methods

# Maintain_Patron_profile_UseCase class attributes and methods

# Add_books_UseCase class attributes and methods

# Remove_Books_UseCase class attributes and methods

# Update_Books_UseCase class attributes and methods

# Late_fees_UseCase class attributes and methods

# Renew_Patron_UseCase class attributes and methods

# Create_library_account_UseCase class attributes and methods

# Request_Book_UseCase class attributes and methods

# Checkout_book_UseCase class attributes and methods

# create_UseCase class attributes and methods

# Cancel_UseCase class attributes and methods

# Patron_Actor class attributes and methods

# Library_Management_Component class attributes and methods

# MyClass class attributes and methods

# Library class attributes and methods
Library_books: Property = Property(name="books", type=StringType)
Library.attributes={Library_books}

# Relationships
Issue_card_Librarian: BinaryAssociation = BinaryAssociation(
    name="Issue_card_Librarian",
    ends={
        Property(name="librarian0", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="issue_card1", type=Issue_card_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Manage_Books_Librarian: BinaryAssociation = BinaryAssociation(
    name="Manage_Books_Librarian",
    ends={
        Property(name="librarian2", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="manage_Books3", type=Manage_Books_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Issue_Book_Librarian: BinaryAssociation = BinaryAssociation(
    name="Issue_Book_Librarian",
    ends={
        Property(name="librarian4", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="issue_Book5", type=Issue_Book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Return_book_Librarian: BinaryAssociation = BinaryAssociation(
    name="Return_book_Librarian",
    ends={
        Property(name="librarian6", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="return_book7", type=Return_book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Maintain_Patron_profile_Librarian: BinaryAssociation = BinaryAssociation(
    name="Maintain_Patron_profile_Librarian",
    ends={
        Property(name="librarian8", type=Librarian_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="maintain_Patron_profile9", type=Maintain_Patron_profile_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Create_library_account_Patron: BinaryAssociation = BinaryAssociation(
    name="Create_library_account_Patron",
    ends={
        Property(name="patron10", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="create_library_account11", type=Create_library_account_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Request_Book_Patron: BinaryAssociation = BinaryAssociation(
    name="Request_Book_Patron",
    ends={
        Property(name="patron12", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="request_Book13", type=Request_Book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Checkout_book_Patron: BinaryAssociation = BinaryAssociation(
    name="Checkout_book_Patron",
    ends={
        Property(name="patron14", type=Patron_Actor, multiplicity=Multiplicity(0, 1)),
        Property(name="checkout_book15", type=Checkout_book_UseCase, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Return_book: BinaryAssociation = BinaryAssociation(
    name="Patron_Return_book",
    ends={
        Property(name="return_book16", type=Return_book_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="patron17", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="feb3ff32_255a_43db_971f_3a7bc60daab4",
    types={Librarian_Actor, Issue_card_UseCase, Manage_Books_UseCase, Issue_Book_UseCase, Return_book_UseCase, Maintain_Patron_profile_UseCase, Add_books_UseCase, Remove_Books_UseCase, Update_Books_UseCase, Late_fees_UseCase, Renew_Patron_UseCase, Create_library_account_UseCase, Request_Book_UseCase, Checkout_book_UseCase, create_UseCase, Cancel_UseCase, Patron_Actor, Library_Management_Component, MyClass, Library},
    associations={Issue_card_Librarian, Manage_Books_Librarian, Issue_Book_Librarian, Return_book_Librarian, Maintain_Patron_profile_Librarian, Create_library_account_Patron, Request_Book_Patron, Checkout_book_Patron, Patron_Return_book},
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