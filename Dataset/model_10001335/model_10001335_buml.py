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
library = Class(name="library")
librarian = Class(name="librarian")
books_database = Class(name="books_database")
student = Class(name="student")
vendor = Class(name="vendor")
student_record = Class(name="student_record")

# library class attributes and methods
library_location: Property = Property(name="location", type=StringType)
library.attributes={library_location}

# librarian class attributes and methods
librarian_name: Property = Property(name="name", type=StringType)
librarian.attributes={librarian_name}

# books_database class attributes and methods
books_database_book_title: Property = Property(name="book_title", type=StringType)
books_database_author: Property = Property(name="author", type=StringType)
books_database_book_id: Property = Property(name="book_id", type=StringType)
books_database.attributes={books_database_book_id, books_database_book_title, books_database_author}

# student class attributes and methods
student_details: Property = Property(name="details", type=StringType)
student.attributes={student_details}

# vendor class attributes and methods
vendor_book_details: Property = Property(name="book_details", type=StringType)
vendor_attribute: Property = Property(name="attribute", type=StringType)
vendor.attributes={vendor_book_details, vendor_attribute}

# student_record class attributes and methods
student_record_name: Property = Property(name="name", type=StringType)
student_record_address: Property = Property(name="address", type=StringType)
student_record_phone_number: Property = Property(name="phone_number", type=StringType)
student_record_fines: Property = Property(name="fines", type=StringType)
student_record.attributes={student_record_address, student_record_phone_number, student_record_fines, student_record_name}

# Relationships
library_librarian: BinaryAssociation = BinaryAssociation(
    name="library_librarian",
    ends={
        Property(name="librarian0", type=librarian, multiplicity=Multiplicity(0, 1)),
        Property(name="library1", type=library, multiplicity=Multiplicity(0, 1))
    }
)
library_books_database: BinaryAssociation = BinaryAssociation(
    name="library_books_database",
    ends={
        Property(name="books_database2", type=books_database, multiplicity=Multiplicity(0, 1)),
        Property(name="library3", type=library, multiplicity=Multiplicity(0, 1))
    }
)
books_database_customer: BinaryAssociation = BinaryAssociation(
    name="books_database_customer",
    ends={
        Property(name="customer4", type=student, multiplicity=Multiplicity(0, 1)),
        Property(name="books_database5", type=books_database, multiplicity=Multiplicity(0, 1))
    }
)
customer_student_record: BinaryAssociation = BinaryAssociation(
    name="customer_student_record",
    ends={
        Property(name="student_record6", type=student_record, multiplicity=Multiplicity(0, 1)),
        Property(name="customer7", type=student, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_0fYbULfaEee7sYPkE4_GPA",
    types={library, librarian, books_database, student, vendor, student_record},
    associations={library_librarian, library_books_database, books_database_customer, customer_student_record},
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