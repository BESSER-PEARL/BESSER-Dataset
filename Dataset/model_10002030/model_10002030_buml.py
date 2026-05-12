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
LIBRARIAN = Class(name="LIBRARIAN")
book_mdatabase = Class(name="book_mdatabase")
patron = Class(name="patron")
vendor = Class(name="vendor")
patronrecord = Class(name="patronrecord")

# library class attributes and methods
library__location: Property = Property(name="_location", type=StringType)
library__librarion_id: Property = Property(name="_librarion_id", type=StringType)
library.attributes={library__librarion_id, library__location}

# LIBRARIAN class attributes and methods
LIBRARIAN_NAME: Property = Property(name="NAME", type=StringType)
LIBRARIAN_LIBRARIAN_ID: Property = Property(name="LIBRARIAN_ID", type=StringType)
LIBRARIAN_issue_status: Property = Property(name="issue_status", type=StringType)
LIBRARIAN_searchbook__: Property = Property(name="searchbook__", type=StringType)
LIBRARIAN_issue_book: Property = Property(name="issue_book", type=StringType)
LIBRARIAN_verify_member__: Property = Property(name="verify_member__", type=StringType)
LIBRARIAN.attributes={LIBRARIAN_verify_member__, LIBRARIAN_NAME, LIBRARIAN_issue_book, LIBRARIAN_issue_status, LIBRARIAN_LIBRARIAN_ID, LIBRARIAN_searchbook__}

# book_mdatabase class attributes and methods
book_mdatabase_booktitle: Property = Property(name="booktitle", type=StringType)
book_mdatabase_author: Property = Property(name="author", type=StringType)
book_mdatabase_bookid: Property = Property(name="bookid", type=StringType)
book_mdatabase_update: Property = Property(name="update", type=StringType)
book_mdatabase.attributes={book_mdatabase_update, book_mdatabase_author, book_mdatabase_bookid, book_mdatabase_booktitle}

# patron class attributes and methods
patron_details: Property = Property(name="details", type=StringType)
patron_patronid: Property = Property(name="patronid", type=StringType)
patron_search: Property = Property(name="search", type=StringType)
patron_request: Property = Property(name="request", type=StringType)
patron_payfine: Property = Property(name="payfine", type=StringType)
patron.attributes={patron_details, patron_search, patron_patronid, patron_request, patron_payfine}

# vendor class attributes and methods
vendor_search: Property = Property(name="search", type=StringType)
vendor_supplybooks: Property = Property(name="supplybooks", type=StringType)
vendor_bookdetails: Property = Property(name="bookdetails", type=StringType)
vendor_paymentdetails: Property = Property(name="paymentdetails", type=StringType)
vendor.attributes={vendor_search, vendor_bookdetails, vendor_supplybooks, vendor_paymentdetails}

# patronrecord class attributes and methods
patronrecord_patronid: Property = Property(name="patronid", type=StringType)
patronrecord_type: Property = Property(name="type", type=StringType)
patronrecord_dateofmembership: Property = Property(name="dateofmembership", type=StringType)
patronrecord_noofbooks_alooted: Property = Property(name="noofbooks_alooted", type=StringType)
patronrecord_name: Property = Property(name="name", type=StringType)
patronrecord_phone_no: Property = Property(name="phone_no", type=StringType)
patronrecord_address: Property = Property(name="address", type=StringType)
patronrecord_filesowned: Property = Property(name="filesowned", type=StringType)
patronrecord.attributes={patronrecord_dateofmembership, patronrecord_patronid, patronrecord_name, patronrecord_phone_no, patronrecord_noofbooks_alooted, patronrecord_filesowned, patronrecord_type, patronrecord_address}

# Relationships
library_LIBRARIAN: BinaryAssociation = BinaryAssociation(
    name="library_LIBRARIAN",
    ends={
        Property(name="lIBRARIAN0", type=LIBRARIAN, multiplicity=Multiplicity(0, 1)),
        Property(name="library1", type=library, multiplicity=Multiplicity(0, 1))
    }
)
library_book_mdatabase: BinaryAssociation = BinaryAssociation(
    name="library_book_mdatabase",
    ends={
        Property(name="book_mdatabase2", type=book_mdatabase, multiplicity=Multiplicity(0, 1)),
        Property(name="library3", type=library, multiplicity=Multiplicity(0, 1))
    }
)
book_mdatabase_patron: BinaryAssociation = BinaryAssociation(
    name="book_mdatabase_patron",
    ends={
        Property(name="patron4", type=patron, multiplicity=Multiplicity(0, 1)),
        Property(name="book_mdatabase5", type=book_mdatabase, multiplicity=Multiplicity(0, 1))
    }
)
patron_patronrecord: BinaryAssociation = BinaryAssociation(
    name="patron_patronrecord",
    ends={
        Property(name="patronrecord6", type=patronrecord, multiplicity=Multiplicity(0, 1)),
        Property(name="patron7", type=patron, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_kiZ6sADrEeiLEbIzy5aHfg",
    types={library, LIBRARIAN, book_mdatabase, patron, vendor, patronrecord},
    associations={library_LIBRARIAN, library_book_mdatabase, book_mdatabase_patron, patron_patronrecord},
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