from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class soaml_Categorization:

    pass
class FreeFormValue:

    pass
class soaml_CategoryValue(FreeFormValue):

    pass
class soaml_FreeFormValue:

    pass
class soaml_FreeFormDescriptor:

    pass
class soaml_Connector:

    pass
class soaml_ServiceChannel:

    pass
class soaml_Service:

    pass
class soaml_Request:

    pass
class soaml_Port:

    def __init__(self, connectorRequired: str, soaml_Port: "soaml_Port" = None, soaml_Port20: "soaml_Port" = None, soaml_Port23: "soaml_Request" = None, soaml_Port25: "soaml_Service" = None):
        self.connectorRequired = connectorRequired
        self.soaml_Port = soaml_Port
        self.soaml_Port20 = soaml_Port20
        self.soaml_Port23 = soaml_Port23
        self.soaml_Port25 = soaml_Port25
        
    @property
    def connectorRequired(self) -> str:
        return self.__connectorRequired

    @connectorRequired.setter
    def connectorRequired(self, connectorRequired: str):
        self.__connectorRequired = connectorRequired

    @property
    def soaml_Port25(self):
        return self.__soaml_Port25

    @soaml_Port25.setter
    def soaml_Port25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Port__soaml_Port25", None)
        self.__soaml_Port25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Service"):
                opp_val = getattr(old_value, "soaml_Service", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Service", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Service"):
                opp_val = getattr(value, "soaml_Service", None)
                setattr(value, "soaml_Service", self)

    @property
    def soaml_Port(self):
        return self.__soaml_Port

    @soaml_Port.setter
    def soaml_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Port__soaml_Port", None)
        self.__soaml_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Port20"):
                opp_val = getattr(old_value, "soaml_Port20", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Port20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Port20"):
                opp_val = getattr(value, "soaml_Port20", None)
                setattr(value, "soaml_Port20", self)

    @property
    def soaml_Port20(self):
        return self.__soaml_Port20

    @soaml_Port20.setter
    def soaml_Port20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Port__soaml_Port20", None)
        self.__soaml_Port20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Port"):
                opp_val = getattr(old_value, "soaml_Port", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Port", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Port"):
                opp_val = getattr(value, "soaml_Port", None)
                setattr(value, "soaml_Port", self)

    @property
    def soaml_Port23(self):
        return self.__soaml_Port23

    @soaml_Port23.setter
    def soaml_Port23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Port__soaml_Port23", None)
        self.__soaml_Port23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Request"):
                opp_val = getattr(old_value, "soaml_Request", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Request", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Request"):
                opp_val = getattr(value, "soaml_Request", None)
                setattr(value, "soaml_Request", self)

class Participant:

    pass
class soaml_Package:

    pass
class NodeDescriptor:

    pass
class soaml_Category(NodeDescriptor):

    pass
class soaml_Catalog(NodeDescriptor):

    pass
class soaml_Artifact:

    pass
class soaml_NodeDescriptor:

    pass
class soaml_Dependency:

    pass
class soaml_Expose:

    pass
class soaml_Capability:

    pass
class soaml_Comment:

    pass
class soaml_ValueSpecification:

    pass
class soaml_Milestone:

    def __init__(self, progress: str, soaml_Milestone: set["soaml_ValueSpecification"] = None, soaml_Milestone39: "soaml_Signal" = None, soaml_Milestone42: "soaml_Comment" = None):
        self.progress = progress
        self.soaml_Milestone = soaml_Milestone if soaml_Milestone is not None else set()
        self.soaml_Milestone39 = soaml_Milestone39
        self.soaml_Milestone42 = soaml_Milestone42
        
    @property
    def progress(self) -> str:
        return self.__progress

    @progress.setter
    def progress(self, progress: str):
        self.__progress = progress

    @property
    def soaml_Milestone42(self):
        return self.__soaml_Milestone42

    @soaml_Milestone42.setter
    def soaml_Milestone42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Milestone__soaml_Milestone42", None)
        self.__soaml_Milestone42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Comment"):
                opp_val = getattr(old_value, "soaml_Comment", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Comment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Comment"):
                opp_val = getattr(value, "soaml_Comment", None)
                setattr(value, "soaml_Comment", self)

    @property
    def soaml_Milestone39(self):
        return self.__soaml_Milestone39

    @soaml_Milestone39.setter
    def soaml_Milestone39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Milestone__soaml_Milestone39", None)
        self.__soaml_Milestone39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Signal40"):
                opp_val = getattr(old_value, "soaml_Signal40", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Signal40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Signal40"):
                opp_val = getattr(value, "soaml_Signal40", None)
                setattr(value, "soaml_Signal40", self)

    @property
    def soaml_Milestone(self):
        return self.__soaml_Milestone

    @soaml_Milestone.setter
    def soaml_Milestone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Milestone__soaml_Milestone", None)
        self.__soaml_Milestone = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "soaml_ValueSpecification"):
                    opp_val = getattr(item, "soaml_ValueSpecification", None)
                    
                    if opp_val == self:
                        setattr(item, "soaml_ValueSpecification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "soaml_ValueSpecification"):
                    opp_val = getattr(item, "soaml_ValueSpecification", None)
                    
                    setattr(item, "soaml_ValueSpecification", self)
                    

class soaml_Signal:

    pass
class soaml_DataType:

    pass
class soaml_MessageType:

    def __init__(self, encoding: str, soaml_MessageType: "soaml_Class" = None, soaml_MessageType34: "soaml_DataType" = None, soaml_MessageType36: "soaml_Signal" = None):
        self.encoding = encoding
        self.soaml_MessageType = soaml_MessageType
        self.soaml_MessageType34 = soaml_MessageType34
        self.soaml_MessageType36 = soaml_MessageType36
        
    @property
    def encoding(self) -> str:
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding

    @property
    def soaml_MessageType(self):
        return self.__soaml_MessageType

    @soaml_MessageType.setter
    def soaml_MessageType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_MessageType__soaml_MessageType", None)
        self.__soaml_MessageType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Class32"):
                opp_val = getattr(old_value, "soaml_Class32", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Class32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Class32"):
                opp_val = getattr(value, "soaml_Class32", None)
                setattr(value, "soaml_Class32", self)

    @property
    def soaml_MessageType36(self):
        return self.__soaml_MessageType36

    @soaml_MessageType36.setter
    def soaml_MessageType36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_MessageType__soaml_MessageType36", None)
        self.__soaml_MessageType36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Signal"):
                opp_val = getattr(old_value, "soaml_Signal", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Signal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Signal"):
                opp_val = getattr(value, "soaml_Signal", None)
                setattr(value, "soaml_Signal", self)

    @property
    def soaml_MessageType34(self):
        return self.__soaml_MessageType34

    @soaml_MessageType34.setter
    def soaml_MessageType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_MessageType__soaml_MessageType34", None)
        self.__soaml_MessageType34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_DataType"):
                opp_val = getattr(old_value, "soaml_DataType", None)
                if opp_val == self:
                    setattr(old_value, "soaml_DataType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_DataType"):
                opp_val = getattr(value, "soaml_DataType", None)
                setattr(value, "soaml_DataType", self)

class soaml_Attachment:

    def __init__(self, encoding: str, mimeType: str, soaml_Attachment: "soaml_Property" = None):
        self.encoding = encoding
        self.mimeType = mimeType
        self.soaml_Attachment = soaml_Attachment
        
    @property
    def encoding(self) -> str:
        return self.__encoding

    @encoding.setter
    def encoding(self, encoding: str):
        self.__encoding = encoding

    @property
    def mimeType(self) -> str:
        return self.__mimeType

    @mimeType.setter
    def mimeType(self, mimeType: str):
        self.__mimeType = mimeType

    @property
    def soaml_Attachment(self):
        return self.__soaml_Attachment

    @soaml_Attachment.setter
    def soaml_Attachment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Attachment__soaml_Attachment", None)
        self.__soaml_Attachment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Property30"):
                opp_val = getattr(old_value, "soaml_Property30", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Property30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Property30"):
                opp_val = getattr(value, "soaml_Property30", None)
                setattr(value, "soaml_Property30", self)

class soaml_Property:

    def __init__(self, isID: str, soaml_Property: "soaml_Property" = None, soaml_Property27: "soaml_Property" = None, soaml_Property30: "soaml_Attachment" = None, soaml_Property49: "soaml_FreeFormDescriptor" = None):
        self.isID = isID
        self.soaml_Property = soaml_Property
        self.soaml_Property27 = soaml_Property27
        self.soaml_Property30 = soaml_Property30
        self.soaml_Property49 = soaml_Property49
        
    @property
    def isID(self) -> str:
        return self.__isID

    @isID.setter
    def isID(self, isID: str):
        self.__isID = isID

    @property
    def soaml_Property49(self):
        return self.__soaml_Property49

    @soaml_Property49.setter
    def soaml_Property49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Property__soaml_Property49", None)
        self.__soaml_Property49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_FreeFormDescriptor"):
                opp_val = getattr(old_value, "soaml_FreeFormDescriptor", None)
                if opp_val == self:
                    setattr(old_value, "soaml_FreeFormDescriptor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_FreeFormDescriptor"):
                opp_val = getattr(value, "soaml_FreeFormDescriptor", None)
                setattr(value, "soaml_FreeFormDescriptor", self)

    @property
    def soaml_Property30(self):
        return self.__soaml_Property30

    @soaml_Property30.setter
    def soaml_Property30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Property__soaml_Property30", None)
        self.__soaml_Property30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Attachment"):
                opp_val = getattr(old_value, "soaml_Attachment", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Attachment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Attachment"):
                opp_val = getattr(value, "soaml_Attachment", None)
                setattr(value, "soaml_Attachment", self)

    @property
    def soaml_Property27(self):
        return self.__soaml_Property27

    @soaml_Property27.setter
    def soaml_Property27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Property__soaml_Property27", None)
        self.__soaml_Property27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Property"):
                opp_val = getattr(old_value, "soaml_Property", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Property", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Property"):
                opp_val = getattr(value, "soaml_Property", None)
                setattr(value, "soaml_Property", self)

    @property
    def soaml_Property(self):
        return self.__soaml_Property

    @soaml_Property.setter
    def soaml_Property(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Property__soaml_Property", None)
        self.__soaml_Property = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Property27"):
                opp_val = getattr(old_value, "soaml_Property27", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Property27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Property27"):
                opp_val = getattr(value, "soaml_Property27", None)
                setattr(value, "soaml_Property27", self)

class soaml_Agent(Participant):

    pass
class soaml_Participant:

    pass
class soaml_ServiceInterface:

    pass
class soaml_Realization:

    pass
class soaml_MotivationRealization:

    pass
class soaml_Provider:

    pass
class soaml_Class:

    pass
class soaml_Interface:

    pass
class soaml_Consumer:

    pass
class soaml_CollaborationUse:

    def __init__(self, isStrict: str, soaml_CollaborationUse: "soaml_CollaborationUse" = None, soaml_CollaborationUse2: "soaml_CollaborationUse" = None):
        self.isStrict = isStrict
        self.soaml_CollaborationUse = soaml_CollaborationUse
        self.soaml_CollaborationUse2 = soaml_CollaborationUse2
        
    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

    @property
    def soaml_CollaborationUse2(self):
        return self.__soaml_CollaborationUse2

    @soaml_CollaborationUse2.setter
    def soaml_CollaborationUse2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_CollaborationUse__soaml_CollaborationUse2", None)
        self.__soaml_CollaborationUse2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_CollaborationUse"):
                opp_val = getattr(old_value, "soaml_CollaborationUse", None)
                if opp_val == self:
                    setattr(old_value, "soaml_CollaborationUse", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_CollaborationUse"):
                opp_val = getattr(value, "soaml_CollaborationUse", None)
                setattr(value, "soaml_CollaborationUse", self)

    @property
    def soaml_CollaborationUse(self):
        return self.__soaml_CollaborationUse

    @soaml_CollaborationUse.setter
    def soaml_CollaborationUse(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_CollaborationUse__soaml_CollaborationUse", None)
        self.__soaml_CollaborationUse = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_CollaborationUse2"):
                opp_val = getattr(old_value, "soaml_CollaborationUse2", None)
                if opp_val == self:
                    setattr(old_value, "soaml_CollaborationUse2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_CollaborationUse2"):
                opp_val = getattr(value, "soaml_CollaborationUse2", None)
                setattr(value, "soaml_CollaborationUse2", self)

class Collaboration:

    pass
class soaml_ServiceContract(Collaboration):

    pass
class soaml_ServiceArchitecture(Collaboration):

    pass
class soaml_Collaboration:

    def __init__(self, isStrict: str, soaml_Collaboration: "soaml_Collaboration" = None, soaml_Collaboration0: "soaml_Collaboration" = None):
        self.isStrict = isStrict
        self.soaml_Collaboration = soaml_Collaboration
        self.soaml_Collaboration0 = soaml_Collaboration0
        
    @property
    def isStrict(self) -> str:
        return self.__isStrict

    @isStrict.setter
    def isStrict(self, isStrict: str):
        self.__isStrict = isStrict

    @property
    def soaml_Collaboration0(self):
        return self.__soaml_Collaboration0

    @soaml_Collaboration0.setter
    def soaml_Collaboration0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Collaboration__soaml_Collaboration0", None)
        self.__soaml_Collaboration0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Collaboration"):
                opp_val = getattr(old_value, "soaml_Collaboration", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Collaboration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Collaboration"):
                opp_val = getattr(value, "soaml_Collaboration", None)
                setattr(value, "soaml_Collaboration", self)

    @property
    def soaml_Collaboration(self):
        return self.__soaml_Collaboration

    @soaml_Collaboration.setter
    def soaml_Collaboration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_soaml_Collaboration__soaml_Collaboration", None)
        self.__soaml_Collaboration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "soaml_Collaboration0"):
                opp_val = getattr(old_value, "soaml_Collaboration0", None)
                if opp_val == self:
                    setattr(old_value, "soaml_Collaboration0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "soaml_Collaboration0"):
                opp_val = getattr(value, "soaml_Collaboration0", None)
                setattr(value, "soaml_Collaboration0", self)
