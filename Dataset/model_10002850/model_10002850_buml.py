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
Doctor_Actor = Class(name="Doctor_Actor")
View_Patient_Mental_Info_UseCase = Class(name="View_Patient_Mental_Info_UseCase")
Update_Patient_Mental_Info_UseCase = Class(name="Update_Patient_Mental_Info_UseCase")
View_Patient_Clinical_info_UseCase = Class(name="View_Patient_Clinical_info_UseCase")
Inbox = Class(name="Inbox")
Sent = Class(name="Sent")
Deleted = Class(name="Deleted")
message = Class(name="message")
From_Author = Class(name="From_Author")
To_Author = Class(name="To_Author")

# Doctor_Actor class attributes and methods

# View_Patient_Mental_Info_UseCase class attributes and methods

# Update_Patient_Mental_Info_UseCase class attributes and methods

# View_Patient_Clinical_info_UseCase class attributes and methods

# Inbox class attributes and methods

# Sent class attributes and methods

# Deleted class attributes and methods

# message class attributes and methods

# From_Author class attributes and methods

# To_Author class attributes and methods

# Relationships
Doctor_View_Patient_Clinical_info: BinaryAssociation = BinaryAssociation(
    name="Doctor_View_Patient_Clinical_info",
    ends={
        Property(name="view_Patient_Clinical_info0", type=View_Patient_Clinical_info_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor1", type=Doctor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_Update_Patient_Mental_Info: BinaryAssociation = BinaryAssociation(
    name="Doctor_Update_Patient_Mental_Info",
    ends={
        Property(name="update_Patient_Mental_Info2", type=Update_Patient_Mental_Info_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor3", type=Doctor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Doctor_View_Patient_Mental_Info: BinaryAssociation = BinaryAssociation(
    name="Doctor_View_Patient_Mental_Info",
    ends={
        Property(name="view_Patient_Mental_Info4", type=View_Patient_Mental_Info_UseCase, multiplicity=Multiplicity(0, 1)),
        Property(name="doctor5", type=Doctor_Actor, multiplicity=Multiplicity(0, 1))
    }
)
Inbox_message: BinaryAssociation = BinaryAssociation(
    name="Inbox_message",
    ends={
        Property(name="is_in6", type=message, multiplicity=Multiplicity(0, 9999)),
        Property(name="Inbox_message_17", type=Inbox, multiplicity=Multiplicity(0, 1))
    }
)
Sent_message: BinaryAssociation = BinaryAssociation(
    name="Sent_message",
    ends={
        Property(name="message8", type=message, multiplicity=Multiplicity(0, 9999)),
        Property(name="sent9", type=Sent, multiplicity=Multiplicity(0, 1))
    }
)
message_Deleted: BinaryAssociation = BinaryAssociation(
    name="message_Deleted",
    ends={
        Property(name="deleted10", type=Deleted, multiplicity=Multiplicity(0, 1)),
        Property(name="message11", type=message, multiplicity=Multiplicity(0, 9999))
    }
)
message_To: BinaryAssociation = BinaryAssociation(
    name="message_To",
    ends={
        Property(name="Sent_to12", type=To_Author, multiplicity=Multiplicity(1, 9999)),
        Property(name="message13", type=message, multiplicity=Multiplicity(1, 9999))
    }
)
From_message: BinaryAssociation = BinaryAssociation(
    name="From_message",
    ends={
        Property(name="From_message_014", type=message, multiplicity=Multiplicity(1, 9999)),
        Property(name="Came_from15", type=From_Author, multiplicity=Multiplicity(1, 9999))
    }
)

# Domain Model
domain_model = DomainModel(
    name="e2b5dc7b_3046_4945_a5b8_404cb943ac14",
    types={Doctor_Actor, View_Patient_Mental_Info_UseCase, Update_Patient_Mental_Info_UseCase, View_Patient_Clinical_info_UseCase, Inbox, Sent, Deleted, message, From_Author, To_Author},
    associations={Doctor_View_Patient_Clinical_info, Doctor_Update_Patient_Mental_Info, Doctor_View_Patient_Mental_Info, Inbox_message, Sent_message, message_Deleted, message_To, From_message},
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