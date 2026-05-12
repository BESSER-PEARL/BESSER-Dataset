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
Student_Actor = Class(name="Student_Actor")
Resources_Component = Class(name="Resources_Component")
Staff_Actor1 = Class(name="Staff_Actor1")
Patron = Class(name="Patron")
Books = Class(name="Books")
MultiMedia = Class(name="MultiMedia")
StaffMember = Class(name="StaffMember")
Computers_external = Class(name="Computers_external")
Aid_Patrons_external = Class(name="Aid_Patrons_external")
Reserved_or_reference_books_external = Class(name="Reserved_or_reference_books_external")
Books_external = Class(name="Books_external")
Multimedia_external = Class(name="Multimedia_external")
Periodicals_external = Class(name="Periodicals_external")
Acquiring_Retiring_Books_external = Class(name="Acquiring_Retiring_Books_external")
Fees_for_overdue_books_external = Class(name="Fees_for_overdue_books_external")
Patron_Actor = Class(name="Patron_Actor")
Staff_Actor = Class(name="Staff_Actor")
Faculty_Actor = Class(name="Faculty_Actor")

# Student_Actor class attributes and methods

# Resources_Component class attributes and methods

# Staff_Actor1 class attributes and methods

# Patron class attributes and methods

# Books class attributes and methods
Books_title: Property = Property(name="title", type=StringType)
Books.attributes={Books_title}

# MultiMedia class attributes and methods

# StaffMember class attributes and methods

# Computers_external class attributes and methods

# Aid_Patrons_external class attributes and methods

# Reserved_or_reference_books_external class attributes and methods

# Books_external class attributes and methods

# Multimedia_external class attributes and methods

# Periodicals_external class attributes and methods

# Acquiring_Retiring_Books_external class attributes and methods

# Fees_for_overdue_books_external class attributes and methods

# Patron_Actor class attributes and methods

# Staff_Actor class attributes and methods

# Faculty_Actor class attributes and methods

# Relationships
Aid_Patrons_Computers: BinaryAssociation = BinaryAssociation(
    name="Aid_Patrons_Computers",
    ends={
        Property(name="computers0", type=Computers_external, multiplicity=Multiplicity(0, 1)),
        Property(name="aid_Patrons1", type=Aid_Patrons_external, multiplicity=Multiplicity(0, 1))
    }
)
Aid_Patrons_Reserved_or_reference_books: BinaryAssociation = BinaryAssociation(
    name="Aid_Patrons_Reserved_or_reference_books",
    ends={
        Property(name="reserved_or_reference_books2", type=Reserved_or_reference_books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="aid_Patrons3", type=Aid_Patrons_external, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Books: BinaryAssociation = BinaryAssociation(
    name="Patron_Books",
    ends={
        Property(name="books4", type=Books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron5", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Multimedia: BinaryAssociation = BinaryAssociation(
    name="Patron_Multimedia",
    ends={
        Property(name="multimedia6", type=Multimedia_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron7", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Reserved_or_reference_books: BinaryAssociation = BinaryAssociation(
    name="Patron_Reserved_or_reference_books",
    ends={
        Property(name="reserved_or_reference_books8", type=Reserved_or_reference_books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron9", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Periodicals: BinaryAssociation = BinaryAssociation(
    name="Patron_Periodicals",
    ends={
        Property(name="periodicals10", type=Periodicals_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron11", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Computers: BinaryAssociation = BinaryAssociation(
    name="Patron_Computers",
    ends={
        Property(name="computers12", type=Computers_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron13", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Acquiring_Retiring: BinaryAssociation = BinaryAssociation(
    name="Staff_Acquiring_Retiring",
    ends={
        Property(name="acquiring_Retiring14", type=Acquiring_Retiring_Books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="staff15", type=Staff_Actor1, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Fees_for_overdue_books: BinaryAssociation = BinaryAssociation(
    name="Patron_Fees_for_overdue_books",
    ends={
        Property(name="fees_for_overdue_books16", type=Fees_for_overdue_books_external, multiplicity=Multiplicity(0, 1)),
        Property(name="patron17", type=Patron_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Aid_Patrons: BinaryAssociation = BinaryAssociation(
    name="Staff_Aid_Patrons",
    ends={
        Property(name="aid_Patrons18", type=Aid_Patrons_external, multiplicity=Multiplicity(0, 1)),
        Property(name="staff19", type=Staff_Actor1, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_ec35gMQnEeeWu_SLkciAbg",
    types={Student_Actor, Resources_Component, Staff_Actor1, Patron, Books, MultiMedia, StaffMember, Computers_external, Aid_Patrons_external, Reserved_or_reference_books_external, Books_external, Multimedia_external, Periodicals_external, Acquiring_Retiring_Books_external, Fees_for_overdue_books_external, Patron_Actor, Staff_Actor, Faculty_Actor},
    associations={Aid_Patrons_Computers, Aid_Patrons_Reserved_or_reference_books, Patron_Books, Patron_Multimedia, Patron_Reserved_or_reference_books, Patron_Periodicals, Patron_Computers, Staff_Acquiring_Retiring, Patron_Fees_for_overdue_books, Staff_Aid_Patrons},
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