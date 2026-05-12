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

# Enumerations
String: Enumeration = Enumeration(
    name="String",
    literals={
            
    }
)

# Classes
Activity = Class(name="Activity")
Comment = Class(name="Comment")
Attachment = Class(name="Attachment")
Role = Class(name="Role")
Usuario_Interface = Class(name="Usuario_Interface")
Mensaje_Interface = Class(name="Mensaje_Interface")
Room_Interface = Class(name="Room_Interface")
ChatService = Class(name="ChatService")
RoomService = Class(name="RoomService")
SpeechRecognitionService = Class(name="SpeechRecognitionService")
AuthenticationService = Class(name="AuthenticationService")

# Activity class attributes and methods
Activity_ActivityID: Property = Property(name="ActivityID", type=IntegerType)
Activity_User: Property = Property(name="User", type=StringType)
Activity_Project: Property = Property(name="Project", type=StringType)
Activity_ActivityType: Property = Property(name="ActivityType", type=IntegerType)
Activity_ActivitySubType: Property = Property(name="ActivitySubType", type=IntegerType)
Activity_PrevValue: Property = Property(name="PrevValue", type=StringType)
Activity_NewValue: Property = Property(name="NewValue", type=StringType)
Activity_Seen: Property = Property(name="Seen", type=BooleanType)
Activity.attributes={Activity_Project, Activity_ActivitySubType, Activity_User, Activity_ActivityID, Activity_Seen, Activity_NewValue, Activity_PrevValue, Activity_ActivityType}

# Comment class attributes and methods
Comment_CommentID: Property = Property(name="CommentID", type=IntegerType)
Comment_User: Property = Property(name="User", type=StringType)
Comment_Project: Property = Property(name="Project", type=StringType)
Comment_Created: Property = Property(name="Created", type=StringType)
Comment_Content: Property = Property(name="Content", type=StringType)
Comment.attributes={Comment_User, Comment_CommentID, Comment_Created, Comment_Project, Comment_Content}

# Attachment class attributes and methods
Attachment_AttachmentID: Property = Property(name="AttachmentID", type=IntegerType)
Attachment_User: Property = Property(name="User", type=StringType)
Attachment_Project: Property = Property(name="Project", type=StringType)
Attachment_Created: Property = Property(name="Created", type=StringType)
Attachment_Size: Property = Property(name="Size", type=StringType)
Attachment_Extension: Property = Property(name="Extension", type=StringType)
Attachment_Path: Property = Property(name="Path", type=StringType)
Attachment_Name: Property = Property(name="Name", type=StringType)
Attachment.attributes={Attachment_Created, Attachment_Project, Attachment_Size, Attachment_Name, Attachment_Extension, Attachment_AttachmentID, Attachment_Path, Attachment_User}

# Role class attributes and methods
Role_nombre: Property = Property(name="nombre", type=String)
Role_Name: Property = Property(name="Name", type=String)
Role_descripcion: Property = Property(name="descripcion", type=StringType)
Role.attributes={Role_descripcion, Role_Name, Role_nombre}

# Usuario_Interface class attributes and methods

# Mensaje_Interface class attributes and methods

# Room_Interface class attributes and methods

# ChatService class attributes and methods
ChatService_itemsCollection: Property = Property(name="itemsCollection", type=StringType)
ChatService_salasCollection: Property = Property(name="salasCollection", type=StringType)
ChatService_attribute: Property = Property(name="attribute", type=StringType)
ChatService_usuario: Property = Property(name="usuario", type=Usuario_Interface)
ChatService_attribute2: Property = Property(name="attribute2", type=StringType)
ChatService_attribute3: Property = Property(name="attribute3", type=StringType)
ChatService.attributes={ChatService_attribute2, ChatService_attribute3, ChatService_salasCollection, ChatService_attribute, ChatService_usuario, ChatService_itemsCollection}

# RoomService class attributes and methods
RoomService_roomsCollection: Property = Property(name="roomsCollection", type=StringType)
RoomService_itemsCollection: Property = Property(name="itemsCollection", type=StringType)
RoomService_idiomas: Property = Property(name="idiomas", type=StringType)
RoomService_niveles: Property = Property(name="niveles", type=StringType)
RoomService.attributes={RoomService_niveles, RoomService_roomsCollection, RoomService_idiomas, RoomService_itemsCollection}

# SpeechRecognitionService class attributes and methods
SpeechRecognitionService__attr: Property = Property(name="_attr", type=StringType)
SpeechRecognitionService_grabando: Property = Property(name="grabando", type=BooleanType)
SpeechRecognitionService_speechRecognition: Property = Property(name="speechRecognition", type=StringType)
SpeechRecognitionService.attributes={SpeechRecognitionService_speechRecognition, SpeechRecognitionService_grabando, SpeechRecognitionService__attr}

# AuthenticationService class attributes and methods
AuthenticationService_user: Property = Property(name="user", type=StringType)
AuthenticationService_role: Property = Property(name="role", type=String)
AuthenticationService_authState: Property = Property(name="authState", type=StringType)
AuthenticationService_attribute: Property = Property(name="attribute", type=StringType)
AuthenticationService_attribute2: Property = Property(name="attribute2", type=StringType)
AuthenticationService_attribute3: Property = Property(name="attribute3", type=StringType)
AuthenticationService_attribute4: Property = Property(name="attribute4", type=StringType)
AuthenticationService.attributes={AuthenticationService_user, AuthenticationService_authState, AuthenticationService_attribute4, AuthenticationService_attribute2, AuthenticationService_attribute3, AuthenticationService_attribute, AuthenticationService_role}

# Relationships
Usuario_Mensaje: BinaryAssociation = BinaryAssociation(
    name="Usuario_Mensaje",
    ends={
        Property(name="mensaje0", type=Mensaje_Interface, multiplicity=Multiplicity(1, 1)),
        Property(name="usuario1", type=Usuario_Interface, multiplicity=Multiplicity(1, 9999))
    }
)
Usuario_Room: BinaryAssociation = BinaryAssociation(
    name="Usuario_Room",
    ends={
        Property(name="room2", type=Room_Interface, multiplicity=Multiplicity(0, 9999)),
        Property(name="usuario3", type=Usuario_Interface, multiplicity=Multiplicity(0, 9999))
    }
)
Usuario_Role: BinaryAssociation = BinaryAssociation(
    name="Usuario_Role",
    ends={
        Property(name="role4", type=Role, multiplicity=Multiplicity(0, 9999)),
        Property(name="usuario5", type=Usuario_Interface, multiplicity=Multiplicity(1, 1))
    }
)
Mensaje_ChatService: BinaryAssociation = BinaryAssociation(
    name="Mensaje_ChatService",
    ends={
        Property(name="chatService6", type=ChatService, multiplicity=Multiplicity(1, 1)),
        Property(name="mensaje7", type=Mensaje_Interface, multiplicity=Multiplicity(1, 1))
    }
)
ChatService_Room: BinaryAssociation = BinaryAssociation(
    name="ChatService_Room",
    ends={
        Property(name="room8", type=Room_Interface, multiplicity=Multiplicity(0, 1)),
        Property(name="chatService9", type=ChatService, multiplicity=Multiplicity(0, 1))
    }
)
Room_RoomService: BinaryAssociation = BinaryAssociation(
    name="Room_RoomService",
    ends={
        Property(name="roomService10", type=RoomService, multiplicity=Multiplicity(0, 1)),
        Property(name="room11", type=Room_Interface, multiplicity=Multiplicity(0, 1))
    }
)
Mensaje_SpeechRecognitionService: BinaryAssociation = BinaryAssociation(
    name="Mensaje_SpeechRecognitionService",
    ends={
        Property(name="speechRecognitionService12", type=SpeechRecognitionService, multiplicity=Multiplicity(0, 1)),
        Property(name="mensaje13", type=Mensaje_Interface, multiplicity=Multiplicity(0, 1))
    }
)
ChatService_SpeechRecognitionService: BinaryAssociation = BinaryAssociation(
    name="ChatService_SpeechRecognitionService",
    ends={
        Property(name="speechRecognitionService14", type=SpeechRecognitionService, multiplicity=Multiplicity(0, 1)),
        Property(name="chatService15", type=ChatService, multiplicity=Multiplicity(0, 1))
    }
)
Usuario_AuthenticationService: BinaryAssociation = BinaryAssociation(
    name="Usuario_AuthenticationService",
    ends={
        Property(name="authenticationService16", type=AuthenticationService, multiplicity=Multiplicity(0, 1)),
        Property(name="usuario17", type=Usuario_Interface, multiplicity=Multiplicity(0, 1))
    }
)
AuthenticationService_AuthenticationService: BinaryAssociation = BinaryAssociation(
    name="AuthenticationService_AuthenticationService",
    ends={
        Property(name="authenticationService18", type=AuthenticationService, multiplicity=Multiplicity(0, 1)),
        Property(name="authenticationService19", type=AuthenticationService, multiplicity=Multiplicity(0, 1))
    }
)

# Domain Model
domain_model = DomainModel(
    name="_euwzAEhoEeqonN_RS9oRzw",
    types={Activity, Comment, Attachment, Role, Usuario_Interface, Mensaje_Interface, Room_Interface, ChatService, RoomService, SpeechRecognitionService, AuthenticationService, String},
    associations={Usuario_Mensaje, Usuario_Room, Usuario_Role, Mensaje_ChatService, ChatService_Room, Room_RoomService, Mensaje_SpeechRecognitionService, ChatService_SpeechRecognitionService, Usuario_AuthenticationService, AuthenticationService_AuthenticationService},
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