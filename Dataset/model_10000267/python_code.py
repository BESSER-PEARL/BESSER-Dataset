from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class String(Enum):
    pass

############################################
# Definition of Classes
############################################










class Comment:

    def __init__(self, CommentID: int, User: str, Project: str, Created: str, Content: str):
        self.CommentID = CommentID
        self.User = User
        self.Project = Project
        self.Created = Created
        self.Content = Content
        
        pass
    @property
    def User(self):
        return self.__User
    @User.setter
    def User(self, User: str):
        self.__User = User

    @property
    def Created(self):
        return self.__Created
    @Created.setter
    def Created(self, Created: str):
        self.__Created = Created

    @property
    def CommentID(self):
        return self.__CommentID
    @CommentID.setter
    def CommentID(self, CommentID: int):
        self.__CommentID = CommentID

    @property
    def Project(self):
        return self.__Project
    @Project.setter
    def Project(self, Project: str):
        self.__Project = Project

    @property
    def Content(self):
        return self.__Content
    @Content.setter
    def Content(self, Content: str):
        self.__Content = Content



class Activity:

    def __init__(self, ActivityID: int, User: str, Project: str, ActivityType: int, ActivitySubType: int, PrevValue: str, NewValue: str, Seen: bool):
        self.ActivityID = ActivityID
        self.User = User
        self.Project = Project
        self.ActivityType = ActivityType
        self.ActivitySubType = ActivitySubType
        self.PrevValue = PrevValue
        self.NewValue = NewValue
        self.Seen = Seen
        
        pass
    @property
    def PrevValue(self):
        return self.__PrevValue
    @PrevValue.setter
    def PrevValue(self, PrevValue: str):
        self.__PrevValue = PrevValue

    @property
    def Project(self):
        return self.__Project
    @Project.setter
    def Project(self, Project: str):
        self.__Project = Project

    @property
    def NewValue(self):
        return self.__NewValue
    @NewValue.setter
    def NewValue(self, NewValue: str):
        self.__NewValue = NewValue

    @property
    def ActivitySubType(self):
        return self.__ActivitySubType
    @ActivitySubType.setter
    def ActivitySubType(self, ActivitySubType: int):
        self.__ActivitySubType = ActivitySubType

    @property
    def Seen(self):
        return self.__Seen
    @Seen.setter
    def Seen(self, Seen: bool):
        self.__Seen = Seen

    @property
    def ActivityID(self):
        return self.__ActivityID
    @ActivityID.setter
    def ActivityID(self, ActivityID: int):
        self.__ActivityID = ActivityID

    @property
    def User(self):
        return self.__User
    @User.setter
    def User(self, User: str):
        self.__User = User

    @property
    def ActivityType(self):
        return self.__ActivityType
    @ActivityType.setter
    def ActivityType(self, ActivityType: int):
        self.__ActivityType = ActivityType



class AuthenticationService:

    def __init__(self, user: str, role: String, authState: str, attribute: str, attribute2: str, attribute3: str, attribute4: str, usuario17: "Usuario_Interface" = None, authenticationService18: "AuthenticationService" = None, authenticationService19: "AuthenticationService" = None):
        self.user = user
        self.role = role
        self.authState = authState
        self.attribute = attribute
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.attribute4 = attribute4
        self.usuario17 = usuario17
        self.authenticationService18 = authenticationService18
        self.authenticationService19 = authenticationService19
        
        pass
    @property
    def authState(self):
        return self.__authState
    @authState.setter
    def authState(self, authState: str):
        self.__authState = authState

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def user(self):
        return self.__user
    @user.setter
    def user(self, user: str):
        self.__user = user

    @property
    def attribute4(self):
        return self.__attribute4
    @attribute4.setter
    def attribute4(self, attribute4: str):
        self.__attribute4 = attribute4

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def role(self):
        return self.__role
    @role.setter
    def role(self, role: String):
        self.__role = role

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def authenticationService18(self):
        return self.__authenticationService18
    @authenticationService18.setter
    def authenticationService18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AuthenticationService__authenticationService18", None)
        self.__authenticationService18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authenticationService19"):
                opp_val = getattr(old_value, "authenticationService19", None)
                if opp_val == self:
                    setattr(old_value, "authenticationService19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authenticationService19"):
                opp_val = getattr(value, "authenticationService19", None)
                setattr(value, "authenticationService19", self)

    @property
    def authenticationService19(self):
        return self.__authenticationService19
    @authenticationService19.setter
    def authenticationService19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AuthenticationService__authenticationService19", None)
        self.__authenticationService19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authenticationService18"):
                opp_val = getattr(old_value, "authenticationService18", None)
                if opp_val == self:
                    setattr(old_value, "authenticationService18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authenticationService18"):
                opp_val = getattr(value, "authenticationService18", None)
                setattr(value, "authenticationService18", self)

    @property
    def usuario17(self):
        return self.__usuario17
    @usuario17.setter
    def usuario17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_AuthenticationService__usuario17", None)
        self.__usuario17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "authenticationService16"):
                opp_val = getattr(old_value, "authenticationService16", None)
                if opp_val == self:
                    setattr(old_value, "authenticationService16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "authenticationService16"):
                opp_val = getattr(value, "authenticationService16", None)
                setattr(value, "authenticationService16", self)



class SpeechRecognitionService:

    def __init__(self, _attr: str, grabando: bool, speechRecognition: str, mensaje13: "Mensaje_Interface" = None, chatService15: "ChatService" = None):
        self._attr = _attr
        self.grabando = grabando
        self.speechRecognition = speechRecognition
        self.mensaje13 = mensaje13
        self.chatService15 = chatService15
        
        pass
    @property
    def speechRecognition(self):
        return self.__speechRecognition
    @speechRecognition.setter
    def speechRecognition(self, speechRecognition: str):
        self.__speechRecognition = speechRecognition

    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def grabando(self):
        return self.__grabando
    @grabando.setter
    def grabando(self, grabando: bool):
        self.__grabando = grabando

    @property
    def chatService15(self):
        return self.__chatService15
    @chatService15.setter
    def chatService15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpeechRecognitionService__chatService15", None)
        self.__chatService15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speechRecognitionService14"):
                opp_val = getattr(old_value, "speechRecognitionService14", None)
                if opp_val == self:
                    setattr(old_value, "speechRecognitionService14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speechRecognitionService14"):
                opp_val = getattr(value, "speechRecognitionService14", None)
                setattr(value, "speechRecognitionService14", self)

    @property
    def mensaje13(self):
        return self.__mensaje13
    @mensaje13.setter
    def mensaje13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_SpeechRecognitionService__mensaje13", None)
        self.__mensaje13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "speechRecognitionService12"):
                opp_val = getattr(old_value, "speechRecognitionService12", None)
                if opp_val == self:
                    setattr(old_value, "speechRecognitionService12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "speechRecognitionService12"):
                opp_val = getattr(value, "speechRecognitionService12", None)
                setattr(value, "speechRecognitionService12", self)



class RoomService:

    def __init__(self, roomsCollection: str, itemsCollection: str, idiomas: str, niveles: str, room11: "Room_Interface" = None):
        self.roomsCollection = roomsCollection
        self.itemsCollection = itemsCollection
        self.idiomas = idiomas
        self.niveles = niveles
        self.room11 = room11
        
        pass
    @property
    def idiomas(self):
        return self.__idiomas
    @idiomas.setter
    def idiomas(self, idiomas: str):
        self.__idiomas = idiomas

    @property
    def roomsCollection(self):
        return self.__roomsCollection
    @roomsCollection.setter
    def roomsCollection(self, roomsCollection: str):
        self.__roomsCollection = roomsCollection

    @property
    def niveles(self):
        return self.__niveles
    @niveles.setter
    def niveles(self, niveles: str):
        self.__niveles = niveles

    @property
    def itemsCollection(self):
        return self.__itemsCollection
    @itemsCollection.setter
    def itemsCollection(self, itemsCollection: str):
        self.__itemsCollection = itemsCollection

    @property
    def room11(self):
        return self.__room11
    @room11.setter
    def room11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_RoomService__room11", None)
        self.__room11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "roomService10"):
                opp_val = getattr(old_value, "roomService10", None)
                if opp_val == self:
                    setattr(old_value, "roomService10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "roomService10"):
                opp_val = getattr(value, "roomService10", None)
                setattr(value, "roomService10", self)



class ChatService:

    def __init__(self, itemsCollection: str, salasCollection: str, attribute: str, usuario: Usuario_Interface, attribute2: str, attribute3: str, mensaje7: "Mensaje_Interface" = None, room8: "Room_Interface" = None, speechRecognitionService14: "SpeechRecognitionService" = None):
        self.itemsCollection = itemsCollection
        self.salasCollection = salasCollection
        self.attribute = attribute
        self.usuario = usuario
        self.attribute2 = attribute2
        self.attribute3 = attribute3
        self.mensaje7 = mensaje7
        self.room8 = room8
        self.speechRecognitionService14 = speechRecognitionService14
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def itemsCollection(self):
        return self.__itemsCollection
    @itemsCollection.setter
    def itemsCollection(self, itemsCollection: str):
        self.__itemsCollection = itemsCollection

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def usuario(self):
        return self.__usuario
    @usuario.setter
    def usuario(self, usuario: Usuario_Interface):
        self.__usuario = usuario

    @property
    def salasCollection(self):
        return self.__salasCollection
    @salasCollection.setter
    def salasCollection(self, salasCollection: str):
        self.__salasCollection = salasCollection

    @property
    def attribute3(self):
        return self.__attribute3
    @attribute3.setter
    def attribute3(self, attribute3: str):
        self.__attribute3 = attribute3

    @property
    def mensaje7(self):
        return self.__mensaje7
    @mensaje7.setter
    def mensaje7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ChatService__mensaje7", None)
        self.__mensaje7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chatService6"):
                opp_val = getattr(old_value, "chatService6", None)
                if opp_val == self:
                    setattr(old_value, "chatService6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chatService6"):
                opp_val = getattr(value, "chatService6", None)
                setattr(value, "chatService6", self)

    @property
    def room8(self):
        return self.__room8
    @room8.setter
    def room8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ChatService__room8", None)
        self.__room8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chatService9"):
                opp_val = getattr(old_value, "chatService9", None)
                if opp_val == self:
                    setattr(old_value, "chatService9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chatService9"):
                opp_val = getattr(value, "chatService9", None)
                setattr(value, "chatService9", self)

    @property
    def speechRecognitionService14(self):
        return self.__speechRecognitionService14
    @speechRecognitionService14.setter
    def speechRecognitionService14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ChatService__speechRecognitionService14", None)
        self.__speechRecognitionService14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "chatService15"):
                opp_val = getattr(old_value, "chatService15", None)
                if opp_val == self:
                    setattr(old_value, "chatService15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "chatService15"):
                opp_val = getattr(value, "chatService15", None)
                setattr(value, "chatService15", self)



class Room_Interface:

    pass


class Mensaje_Interface:

    pass


class Usuario_Interface:

    pass


class Role:

    def __init__(self, nombre: String, Name: String, descripcion: str, usuario5: "Usuario_Interface" = None):
        self.nombre = nombre
        self.Name = Name
        self.descripcion = descripcion
        self.usuario5 = usuario5
        
        pass
    @property
    def descripcion(self):
        return self.__descripcion
    @descripcion.setter
    def descripcion(self, descripcion: str):
        self.__descripcion = descripcion

    @property
    def nombre(self):
        return self.__nombre
    @nombre.setter
    def nombre(self, nombre: String):
        self.__nombre = nombre

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: String):
        self.__Name = Name

    @property
    def usuario5(self):
        return self.__usuario5
    @usuario5.setter
    def usuario5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Role__usuario5", None)
        self.__usuario5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "role4"):
                opp_val = getattr(old_value, "role4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "role4"):
                opp_val = getattr(value, "role4", None)
                if opp_val is None:
                    setattr(value, "role4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Attachment:

    def __init__(self, AttachmentID: int, User: str, Project: str, Created: str, Size: str, Extension: str, Path: str, Name: str):
        self.AttachmentID = AttachmentID
        self.User = User
        self.Project = Project
        self.Created = Created
        self.Size = Size
        self.Extension = Extension
        self.Path = Path
        self.Name = Name
        
        pass
    @property
    def Extension(self):
        return self.__Extension
    @Extension.setter
    def Extension(self, Extension: str):
        self.__Extension = Extension

    @property
    def Created(self):
        return self.__Created
    @Created.setter
    def Created(self, Created: str):
        self.__Created = Created

    @property
    def Project(self):
        return self.__Project
    @Project.setter
    def Project(self, Project: str):
        self.__Project = Project

    @property
    def Size(self):
        return self.__Size
    @Size.setter
    def Size(self, Size: str):
        self.__Size = Size

    @property
    def User(self):
        return self.__User
    @User.setter
    def User(self, User: str):
        self.__User = User

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def AttachmentID(self):
        return self.__AttachmentID
    @AttachmentID.setter
    def AttachmentID(self, AttachmentID: int):
        self.__AttachmentID = AttachmentID

    @property
    def Path(self):
        return self.__Path
    @Path.setter
    def Path(self, Path: str):
        self.__Path = Path

