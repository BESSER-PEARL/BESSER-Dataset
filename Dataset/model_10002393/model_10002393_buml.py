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
Book = Class(name="Book")
Magazine = Class(name="Magazine")
Patron = Class(name="Patron")
Computer = Class(name="Computer")
Media = Class(name="Media")
Staff = Class(name="Staff")

# Book class attributes and methods
Book_title: Property = Property(name="title", type=StringType)
Book_author: Property = Property(name="author", type=StringType)
Book_refNum: Property = Property(name="refNum", type=IntegerType)
Book_dueDate: Property = Property(name="dueDate", type=StringType)
Book.attributes={Book_title, Book_dueDate, Book_author, Book_refNum}

# Magazine class attributes and methods
Magazine_name: Property = Property(name="name", type=StringType)
Magazine_issueNum: Property = Property(name="issueNum", type=IntegerType)
Magazine_location: Property = Property(name="location", type=StringType)
Magazine.attributes={Magazine_issueNum, Magazine_location, Magazine_name}

# Patron class attributes and methods
Patron_name: Property = Property(name="name", type=StringType)
Patron_id: Property = Property(name="id", type=IntegerType)
Patron_position: Property = Property(name="position", type=StringType)
Patron.attributes={Patron_position, Patron_name, Patron_id}

# Computer class attributes and methods
Computer_compID: Property = Property(name="compID", type=IntegerType)
Computer.attributes={Computer_compID}

# Media class attributes and methods
Media_type: Property = Property(name="type", type=IntegerType)
Media_refNum: Property = Property(name="refNum", type=IntegerType)
Media.attributes={Media_refNum, Media_type}

# Staff class attributes and methods
Staff_name: Property = Property(name="name", type=StringType)
Staff_id: Property = Property(name="id", type=IntegerType)
Staff.attributes={Staff_id, Staff_name}

# Relationships
Patron_Media: BinaryAssociation = BinaryAssociation(
    name="Patron_Media",
    ends={
        Property(name="media4", type=Media, multiplicity=Multiplicity(0, 1)),
        Property(name="patron5", type=Patron, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Computer: BinaryAssociation = BinaryAssociation(
    name="Patron_Computer",
    ends={
        Property(name="computer6", type=Computer, multiplicity=Multiplicity(0, 1)),
        Property(name="patron7", type=Patron, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Book: BinaryAssociation = BinaryAssociation(
    name="Staff_Book",
    ends={
        Property(name="book8", type=Book, multiplicity=Multiplicity(0, 1)),
        Property(name="staff9", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Magazine: BinaryAssociation = BinaryAssociation(
    name="Staff_Magazine",
    ends={
        Property(name="magazine10", type=Magazine, multiplicity=Multiplicity(0, 1)),
        Property(name="staff11", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Media: BinaryAssociation = BinaryAssociation(
    name="Staff_Media",
    ends={
        Property(name="media12", type=Media, multiplicity=Multiplicity(0, 1)),
        Property(name="staff13", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Staff_Computer: BinaryAssociation = BinaryAssociation(
    name="Staff_Computer",
    ends={
        Property(name="computer14", type=Computer, multiplicity=Multiplicity(0, 1)),
        Property(name="staff15", type=Staff, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Book: BinaryAssociation = BinaryAssociation(
    name="Patron_Book",
    ends={
        Property(name="book0", type=Book, multiplicity=Multiplicity(0, 1)),
        Property(name="patron1", type=Patron, multiplicity=Multiplicity(0, 1))
    }
)
Patron_Magazine: BinaryAssociation = BinaryAssociation(
    name="Patron_Magazine",
    ends={
        Property(name="magazine2", type=Magazine, multiplicity=Multiplicity(0, 1)),
        Property(name="patron3", type=Patron, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="ae7317ec_b00a_440c_884e_fb70918074dd",
    types={Book, Magazine, Patron, Computer, Media, Staff},
    associations={Patron_Media, Patron_Computer, Staff_Book, Staff_Magazine, Staff_Media, Staff_Computer, Patron_Book, Patron_Magazine},
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