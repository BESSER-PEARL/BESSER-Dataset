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
Librarian = Class(name="Librarian")
Admin = Class(name="Admin")
log = Class(name="log")
Guest = Class(name="Guest")
Book = Class(name="Book")
Member = Class(name="Member")

# Librarian class attributes and methods
Librarian_id: Property = Property(name="id", type=IntegerType)
Librarian_attribute: Property = Property(name="attribute", type=StringType)
Librarian_password: Property = Property(name="password", type=StringType)
Librarian.attributes={Librarian_password, Librarian_attribute, Librarian_id}

# Admin class attributes and methods
Admin_id: Property = Property(name="id", type=IntegerType)
Admin_username: Property = Property(name="username", type=StringType)
Admin_password: Property = Property(name="password", type=StringType)
Admin.attributes={Admin_username, Admin_id, Admin_password}

# log class attributes and methods

# Guest class attributes and methods

# Book class attributes and methods
Book_name: Property = Property(name="name", type=StringType)
Book_author: Property = Property(name="author", type=StringType)
Book.attributes={Book_name, Book_author}

# Member class attributes and methods
Member_id: Property = Property(name="id", type=IntegerType)
Member_username: Property = Property(name="username", type=StringType)
Member_password: Property = Property(name="password", type=StringType)
Member_name: Property = Property(name="name", type=StringType)
Member.attributes={Member_name, Member_password, Member_username, Member_id}

# Relationships
log_Admin: BinaryAssociation = BinaryAssociation(
    name="log_Admin",
    ends={
        Property(name="admin0", type=Admin, multiplicity=Multiplicity(0, 9999)),
        Property(name="log1", type=log, multiplicity=Multiplicity(0, 1))
    }
)
log_Librarian: BinaryAssociation = BinaryAssociation(
    name="log_Librarian",
    ends={
        Property(name="librarian2", type=Librarian, multiplicity=Multiplicity(0, 9999)),
        Property(name="log3", type=log, multiplicity=Multiplicity(0, 1))
    }
)
Guest_Book: BinaryAssociation = BinaryAssociation(
    name="Guest_Book",
    ends={
        Property(name="book4", type=Book, multiplicity=Multiplicity(0, 1)),
        Property(name="guest5", type=Guest, multiplicity=Multiplicity(0, 1))
    }
)
Admin_Book: BinaryAssociation = BinaryAssociation(
    name="Admin_Book",
    ends={
        Property(name="book6", type=Book, multiplicity=Multiplicity(0, 1)),
        Property(name="admin7", type=Admin, multiplicity=Multiplicity(0, 1))
    }
)
log_Member: BinaryAssociation = BinaryAssociation(
    name="log_Member",
    ends={
        Property(name="member8", type=Member, multiplicity=Multiplicity(0, 1)),
        Property(name="log9", type=log, multiplicity=Multiplicity(0, 1))
    }
)
Book_Member: BinaryAssociation = BinaryAssociation(
    name="Book_Member",
    ends={
        Property(name="member10", type=Member, multiplicity=Multiplicity(0, 1)),
        Property(name="book11", type=Book, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_JKevYOatEeiDGLvZhbPYyA",
    types={Librarian, Admin, log, Guest, Book, Member},
    associations={log_Admin, log_Librarian, Guest_Book, Admin_Book, log_Member, Book_Member},
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