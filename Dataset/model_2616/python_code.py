from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class BOLDType(Enum):
    true = "true"
class ITALICType(Enum):
    true = "true"
    false = "false"
class FOLDEDType(Enum):
    true = "true"
    false = "false"
class POSITIONType(Enum):
    left = "left"
    right = "right"


############################################
# Definition of Classes
############################################

class Freemind_ParametersType:

    def __init__(self, RemindUserAt: str, Freemind_ParametersType: "Freemind_DocumentRoot" = None, Freemind_ParametersType26: "Freemind_HookType" = None):
        self.RemindUserAt = RemindUserAt
        self.Freemind_ParametersType = Freemind_ParametersType
        self.Freemind_ParametersType26 = Freemind_ParametersType26
        
    @property
    def RemindUserAt(self) -> str:
        return self.__RemindUserAt

    @RemindUserAt.setter
    def RemindUserAt(self, RemindUserAt: str):
        self.__RemindUserAt = RemindUserAt

    @property
    def Freemind_ParametersType(self):
        return self.__Freemind_ParametersType

    @Freemind_ParametersType.setter
    def Freemind_ParametersType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_ParametersType__Freemind_ParametersType", None)
        self.__Freemind_ParametersType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot21"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot21"):
                opp_val = getattr(value, "Freemind_DocumentRoot21", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_ParametersType26(self):
        return self.__Freemind_ParametersType26

    @Freemind_ParametersType26.setter
    def Freemind_ParametersType26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_ParametersType__Freemind_ParametersType26", None)
        self.__Freemind_ParametersType26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_HookType25"):
                opp_val = getattr(old_value, "Freemind_HookType25", None)
                if opp_val == self:
                    setattr(old_value, "Freemind_HookType25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_HookType25"):
                opp_val = getattr(value, "Freemind_HookType25", None)
                setattr(value, "Freemind_HookType25", self)

class Freemind_NodeType:

    def __init__(self, group: str, Created: str, EncryptedContent: str, Folded: str, BackgroundColor: str, Color: str, Modified: str, Position: str, Style: str, Text: str, Hgap: str, Id: str, Link: str, Vgap: str, Vshift: str, Freemind_NodeType: "Freemind_DocumentRoot" = None, Freemind_NodeType32: "Freemind_MapType" = None, Freemind_NodeType37: set["Freemind_CloudType"] = None, Freemind_NodeType46: set["Freemind_HookType"] = None, Freemind_NodeType34: set["Freemind_ArrowlinkType"] = None, Freemind_NodeType49: set["Freemind_IconType"] = None, Freemind_NodeType40: set["Freemind_EdgeType"] = None, Freemind_NodeType43: set["Freemind_FontType"] = None, Freemind_NodeType53: "Freemind_NodeType" = None, Freemind_NodeType51: set["Freemind_NodeType"] = None):
        self.group = group
        self.Created = Created
        self.EncryptedContent = EncryptedContent
        self.Folded = Folded
        self.BackgroundColor = BackgroundColor
        self.Color = Color
        self.Modified = Modified
        self.Position = Position
        self.Style = Style
        self.Text = Text
        self.Hgap = Hgap
        self.Id = Id
        self.Link = Link
        self.Vgap = Vgap
        self.Vshift = Vshift
        self.Freemind_NodeType = Freemind_NodeType
        self.Freemind_NodeType32 = Freemind_NodeType32
        self.Freemind_NodeType37 = Freemind_NodeType37 if Freemind_NodeType37 is not None else set()
        self.Freemind_NodeType46 = Freemind_NodeType46 if Freemind_NodeType46 is not None else set()
        self.Freemind_NodeType34 = Freemind_NodeType34 if Freemind_NodeType34 is not None else set()
        self.Freemind_NodeType49 = Freemind_NodeType49 if Freemind_NodeType49 is not None else set()
        self.Freemind_NodeType40 = Freemind_NodeType40 if Freemind_NodeType40 is not None else set()
        self.Freemind_NodeType43 = Freemind_NodeType43 if Freemind_NodeType43 is not None else set()
        self.Freemind_NodeType53 = Freemind_NodeType53
        self.Freemind_NodeType51 = Freemind_NodeType51 if Freemind_NodeType51 is not None else set()
        
    @property
    def Created(self) -> str:
        return self.__Created

    @Created.setter
    def Created(self, Created: str):
        self.__Created = Created

    @property
    def Folded(self) -> str:
        return self.__Folded

    @Folded.setter
    def Folded(self, Folded: str):
        self.__Folded = Folded

    @property
    def Modified(self) -> str:
        return self.__Modified

    @Modified.setter
    def Modified(self, Modified: str):
        self.__Modified = Modified

    @property
    def Text(self) -> str:
        return self.__Text

    @Text.setter
    def Text(self, Text: str):
        self.__Text = Text

    @property
    def Position(self) -> str:
        return self.__Position

    @Position.setter
    def Position(self, Position: str):
        self.__Position = Position

    @property
    def BackgroundColor(self) -> str:
        return self.__BackgroundColor

    @BackgroundColor.setter
    def BackgroundColor(self, BackgroundColor: str):
        self.__BackgroundColor = BackgroundColor

    @property
    def Vgap(self) -> str:
        return self.__Vgap

    @Vgap.setter
    def Vgap(self, Vgap: str):
        self.__Vgap = Vgap

    @property
    def Vshift(self) -> str:
        return self.__Vshift

    @Vshift.setter
    def Vshift(self, Vshift: str):
        self.__Vshift = Vshift

    @property
    def Style(self) -> str:
        return self.__Style

    @Style.setter
    def Style(self, Style: str):
        self.__Style = Style

    @property
    def Color(self) -> str:
        return self.__Color

    @Color.setter
    def Color(self, Color: str):
        self.__Color = Color

    @property
    def Link(self) -> str:
        return self.__Link

    @Link.setter
    def Link(self, Link: str):
        self.__Link = Link

    @property
    def EncryptedContent(self) -> str:
        return self.__EncryptedContent

    @EncryptedContent.setter
    def EncryptedContent(self, EncryptedContent: str):
        self.__EncryptedContent = EncryptedContent

    @property
    def group(self) -> str:
        return self.__group

    @group.setter
    def group(self, group: str):
        self.__group = group

    @property
    def Hgap(self) -> str:
        return self.__Hgap

    @Hgap.setter
    def Hgap(self, Hgap: str):
        self.__Hgap = Hgap

    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def Freemind_NodeType32(self):
        return self.__Freemind_NodeType32

    @Freemind_NodeType32.setter
    def Freemind_NodeType32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType32", None)
        self.__Freemind_NodeType32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_MapType31"):
                opp_val = getattr(old_value, "Freemind_MapType31", None)
                if opp_val == self:
                    setattr(old_value, "Freemind_MapType31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_MapType31"):
                opp_val = getattr(value, "Freemind_MapType31", None)
                setattr(value, "Freemind_MapType31", self)

    @property
    def Freemind_NodeType40(self):
        return self.__Freemind_NodeType40

    @Freemind_NodeType40.setter
    def Freemind_NodeType40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType40", None)
        self.__Freemind_NodeType40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_EdgeType41"):
                    opp_val = getattr(item, "Freemind_EdgeType41", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_EdgeType41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_EdgeType41"):
                    opp_val = getattr(item, "Freemind_EdgeType41", None)
                    
                    setattr(item, "Freemind_EdgeType41", self)
                    

    @property
    def Freemind_NodeType37(self):
        return self.__Freemind_NodeType37

    @Freemind_NodeType37.setter
    def Freemind_NodeType37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType37", None)
        self.__Freemind_NodeType37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_CloudType38"):
                    opp_val = getattr(item, "Freemind_CloudType38", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_CloudType38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_CloudType38"):
                    opp_val = getattr(item, "Freemind_CloudType38", None)
                    
                    setattr(item, "Freemind_CloudType38", self)
                    

    @property
    def Freemind_NodeType49(self):
        return self.__Freemind_NodeType49

    @Freemind_NodeType49.setter
    def Freemind_NodeType49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType49", None)
        self.__Freemind_NodeType49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_IconType50"):
                    opp_val = getattr(item, "Freemind_IconType50", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_IconType50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_IconType50"):
                    opp_val = getattr(item, "Freemind_IconType50", None)
                    
                    setattr(item, "Freemind_IconType50", self)
                    

    @property
    def Freemind_NodeType51(self):
        return self.__Freemind_NodeType51

    @Freemind_NodeType51.setter
    def Freemind_NodeType51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType51", None)
        self.__Freemind_NodeType51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_NodeType53"):
                    opp_val = getattr(item, "Freemind_NodeType53", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_NodeType53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_NodeType53"):
                    opp_val = getattr(item, "Freemind_NodeType53", None)
                    
                    setattr(item, "Freemind_NodeType53", self)
                    

    @property
    def Freemind_NodeType53(self):
        return self.__Freemind_NodeType53

    @Freemind_NodeType53.setter
    def Freemind_NodeType53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType53", None)
        self.__Freemind_NodeType53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_NodeType51"):
                opp_val = getattr(old_value, "Freemind_NodeType51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_NodeType51"):
                opp_val = getattr(value, "Freemind_NodeType51", None)
                if opp_val is None:
                    setattr(value, "Freemind_NodeType51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_NodeType43(self):
        return self.__Freemind_NodeType43

    @Freemind_NodeType43.setter
    def Freemind_NodeType43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType43", None)
        self.__Freemind_NodeType43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_FontType44"):
                    opp_val = getattr(item, "Freemind_FontType44", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_FontType44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_FontType44"):
                    opp_val = getattr(item, "Freemind_FontType44", None)
                    
                    setattr(item, "Freemind_FontType44", self)
                    

    @property
    def Freemind_NodeType34(self):
        return self.__Freemind_NodeType34

    @Freemind_NodeType34.setter
    def Freemind_NodeType34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType34", None)
        self.__Freemind_NodeType34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_ArrowlinkType35"):
                    opp_val = getattr(item, "Freemind_ArrowlinkType35", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_ArrowlinkType35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_ArrowlinkType35"):
                    opp_val = getattr(item, "Freemind_ArrowlinkType35", None)
                    
                    setattr(item, "Freemind_ArrowlinkType35", self)
                    

    @property
    def Freemind_NodeType46(self):
        return self.__Freemind_NodeType46

    @Freemind_NodeType46.setter
    def Freemind_NodeType46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType46", None)
        self.__Freemind_NodeType46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_HookType47"):
                    opp_val = getattr(item, "Freemind_HookType47", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_HookType47", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_HookType47"):
                    opp_val = getattr(item, "Freemind_HookType47", None)
                    
                    setattr(item, "Freemind_HookType47", self)
                    

    @property
    def Freemind_NodeType(self):
        return self.__Freemind_NodeType

    @Freemind_NodeType.setter
    def Freemind_NodeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_NodeType__Freemind_NodeType", None)
        self.__Freemind_NodeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot19"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot19"):
                opp_val = getattr(value, "Freemind_DocumentRoot19", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Freemind_TextType:

    pass
class Freemind_HookType:

    def __init__(self, Name: str, Freemind_HookType: "Freemind_DocumentRoot" = None, Freemind_HookType25: "Freemind_ParametersType" = None, Freemind_HookType28: "Freemind_TextType" = None, Freemind_HookType47: "Freemind_NodeType" = None):
        self.Name = Name
        self.Freemind_HookType = Freemind_HookType
        self.Freemind_HookType25 = Freemind_HookType25
        self.Freemind_HookType28 = Freemind_HookType28
        self.Freemind_HookType47 = Freemind_HookType47
        
    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Freemind_HookType47(self):
        return self.__Freemind_HookType47

    @Freemind_HookType47.setter
    def Freemind_HookType47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_HookType__Freemind_HookType47", None)
        self.__Freemind_HookType47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_NodeType46"):
                opp_val = getattr(old_value, "Freemind_NodeType46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_NodeType46"):
                opp_val = getattr(value, "Freemind_NodeType46", None)
                if opp_val is None:
                    setattr(value, "Freemind_NodeType46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_HookType28(self):
        return self.__Freemind_HookType28

    @Freemind_HookType28.setter
    def Freemind_HookType28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_HookType__Freemind_HookType28", None)
        self.__Freemind_HookType28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_TextType29"):
                opp_val = getattr(old_value, "Freemind_TextType29", None)
                if opp_val == self:
                    setattr(old_value, "Freemind_TextType29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_TextType29"):
                opp_val = getattr(value, "Freemind_TextType29", None)
                setattr(value, "Freemind_TextType29", self)

    @property
    def Freemind_HookType(self):
        return self.__Freemind_HookType

    @Freemind_HookType.setter
    def Freemind_HookType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_HookType__Freemind_HookType", None)
        self.__Freemind_HookType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot13"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot13"):
                opp_val = getattr(value, "Freemind_DocumentRoot13", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_HookType25(self):
        return self.__Freemind_HookType25

    @Freemind_HookType25.setter
    def Freemind_HookType25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_HookType__Freemind_HookType25", None)
        self.__Freemind_HookType25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_ParametersType26"):
                opp_val = getattr(old_value, "Freemind_ParametersType26", None)
                if opp_val == self:
                    setattr(old_value, "Freemind_ParametersType26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_ParametersType26"):
                opp_val = getattr(value, "Freemind_ParametersType26", None)
                setattr(value, "Freemind_ParametersType26", self)

class Freemind_FontType:

    def __init__(self, Bold: str, Italic: str, Name: str, Size: str, Freemind_FontType: "Freemind_DocumentRoot" = None, Freemind_FontType44: "Freemind_NodeType" = None):
        self.Bold = Bold
        self.Italic = Italic
        self.Name = Name
        self.Size = Size
        self.Freemind_FontType = Freemind_FontType
        self.Freemind_FontType44 = Freemind_FontType44
        
    @property
    def Bold(self) -> str:
        return self.__Bold

    @Bold.setter
    def Bold(self, Bold: str):
        self.__Bold = Bold

    @property
    def Italic(self) -> str:
        return self.__Italic

    @Italic.setter
    def Italic(self, Italic: str):
        self.__Italic = Italic

    @property
    def Size(self) -> str:
        return self.__Size

    @Size.setter
    def Size(self, Size: str):
        self.__Size = Size

    @property
    def Name(self) -> str:
        return self.__Name

    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Freemind_FontType44(self):
        return self.__Freemind_FontType44

    @Freemind_FontType44.setter
    def Freemind_FontType44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_FontType__Freemind_FontType44", None)
        self.__Freemind_FontType44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_NodeType43"):
                opp_val = getattr(old_value, "Freemind_NodeType43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_NodeType43"):
                opp_val = getattr(value, "Freemind_NodeType43", None)
                if opp_val is None:
                    setattr(value, "Freemind_NodeType43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_FontType(self):
        return self.__Freemind_FontType

    @Freemind_FontType.setter
    def Freemind_FontType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_FontType__Freemind_FontType", None)
        self.__Freemind_FontType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot11"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot11"):
                opp_val = getattr(value, "Freemind_DocumentRoot11", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Freemind_MapType:

    def __init__(self, version: str, Freemind_MapType: "Freemind_DocumentRoot" = None, Freemind_MapType31: "Freemind_NodeType" = None):
        self.version = version
        self.Freemind_MapType = Freemind_MapType
        self.Freemind_MapType31 = Freemind_MapType31
        
    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def Freemind_MapType(self):
        return self.__Freemind_MapType

    @Freemind_MapType.setter
    def Freemind_MapType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_MapType__Freemind_MapType", None)
        self.__Freemind_MapType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot17"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot17"):
                opp_val = getattr(value, "Freemind_DocumentRoot17", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_MapType31(self):
        return self.__Freemind_MapType31

    @Freemind_MapType31.setter
    def Freemind_MapType31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_MapType__Freemind_MapType31", None)
        self.__Freemind_MapType31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_NodeType32"):
                opp_val = getattr(old_value, "Freemind_NodeType32", None)
                if opp_val == self:
                    setattr(old_value, "Freemind_NodeType32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_NodeType32"):
                opp_val = getattr(value, "Freemind_NodeType32", None)
                setattr(value, "Freemind_NodeType32", self)

class Freemind_IconType:

    def __init__(self, Builtin: str, Freemind_IconType: "Freemind_DocumentRoot" = None, Freemind_IconType50: "Freemind_NodeType" = None):
        self.Builtin = Builtin
        self.Freemind_IconType = Freemind_IconType
        self.Freemind_IconType50 = Freemind_IconType50
        
    @property
    def Builtin(self) -> str:
        return self.__Builtin

    @Builtin.setter
    def Builtin(self, Builtin: str):
        self.__Builtin = Builtin

    @property
    def Freemind_IconType(self):
        return self.__Freemind_IconType

    @Freemind_IconType.setter
    def Freemind_IconType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_IconType__Freemind_IconType", None)
        self.__Freemind_IconType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot15"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot15"):
                opp_val = getattr(value, "Freemind_DocumentRoot15", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_IconType50(self):
        return self.__Freemind_IconType50

    @Freemind_IconType50.setter
    def Freemind_IconType50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_IconType__Freemind_IconType50", None)
        self.__Freemind_IconType50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_NodeType49"):
                opp_val = getattr(old_value, "Freemind_NodeType49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_NodeType49"):
                opp_val = getattr(value, "Freemind_NodeType49", None)
                if opp_val is None:
                    setattr(value, "Freemind_NodeType49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Freemind_EdgeType:

    def __init__(self, Color: str, Style: str, Width: str, Freemind_EdgeType: "Freemind_DocumentRoot" = None, Freemind_EdgeType41: "Freemind_NodeType" = None):
        self.Color = Color
        self.Style = Style
        self.Width = Width
        self.Freemind_EdgeType = Freemind_EdgeType
        self.Freemind_EdgeType41 = Freemind_EdgeType41
        
    @property
    def Color(self) -> str:
        return self.__Color

    @Color.setter
    def Color(self, Color: str):
        self.__Color = Color

    @property
    def Style(self) -> str:
        return self.__Style

    @Style.setter
    def Style(self, Style: str):
        self.__Style = Style

    @property
    def Width(self) -> str:
        return self.__Width

    @Width.setter
    def Width(self, Width: str):
        self.__Width = Width

    @property
    def Freemind_EdgeType(self):
        return self.__Freemind_EdgeType

    @Freemind_EdgeType.setter
    def Freemind_EdgeType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_EdgeType__Freemind_EdgeType", None)
        self.__Freemind_EdgeType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot9"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot9"):
                opp_val = getattr(value, "Freemind_DocumentRoot9", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_EdgeType41(self):
        return self.__Freemind_EdgeType41

    @Freemind_EdgeType41.setter
    def Freemind_EdgeType41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_EdgeType__Freemind_EdgeType41", None)
        self.__Freemind_EdgeType41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_NodeType40"):
                opp_val = getattr(old_value, "Freemind_NodeType40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_NodeType40"):
                opp_val = getattr(value, "Freemind_NodeType40", None)
                if opp_val is None:
                    setattr(value, "Freemind_NodeType40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Freemind_CloudType:

    def __init__(self, Color: str, Freemind_CloudType: "Freemind_DocumentRoot" = None, Freemind_CloudType38: "Freemind_NodeType" = None):
        self.Color = Color
        self.Freemind_CloudType = Freemind_CloudType
        self.Freemind_CloudType38 = Freemind_CloudType38
        
    @property
    def Color(self) -> str:
        return self.__Color

    @Color.setter
    def Color(self, Color: str):
        self.__Color = Color

    @property
    def Freemind_CloudType(self):
        return self.__Freemind_CloudType

    @Freemind_CloudType.setter
    def Freemind_CloudType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_CloudType__Freemind_CloudType", None)
        self.__Freemind_CloudType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot7"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot7"):
                opp_val = getattr(value, "Freemind_DocumentRoot7", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_CloudType38(self):
        return self.__Freemind_CloudType38

    @Freemind_CloudType38.setter
    def Freemind_CloudType38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_CloudType__Freemind_CloudType38", None)
        self.__Freemind_CloudType38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_NodeType37"):
                opp_val = getattr(old_value, "Freemind_NodeType37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_NodeType37"):
                opp_val = getattr(value, "Freemind_NodeType37", None)
                if opp_val is None:
                    setattr(value, "Freemind_NodeType37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Freemind_EStringToStringMapEntry:

    pass
class Freemind_DocumentRoot:

    def __init__(self, mixed: str, Freemind_DocumentRoot7: set["Freemind_CloudType"] = None, Freemind_DocumentRoot9: set["Freemind_EdgeType"] = None, Freemind_DocumentRoot: set["Freemind_EStringToStringMapEntry"] = None, Freemind_DocumentRoot2: set["Freemind_EStringToStringMapEntry"] = None, Freemind_DocumentRoot5: set["Freemind_ArrowlinkType"] = None, Freemind_DocumentRoot15: set["Freemind_IconType"] = None, Freemind_DocumentRoot17: set["Freemind_MapType"] = None, Freemind_DocumentRoot11: set["Freemind_FontType"] = None, Freemind_DocumentRoot13: set["Freemind_HookType"] = None, Freemind_DocumentRoot23: set["Freemind_TextType"] = None, Freemind_DocumentRoot19: set["Freemind_NodeType"] = None, Freemind_DocumentRoot21: set["Freemind_ParametersType"] = None):
        self.mixed = mixed
        self.Freemind_DocumentRoot7 = Freemind_DocumentRoot7 if Freemind_DocumentRoot7 is not None else set()
        self.Freemind_DocumentRoot9 = Freemind_DocumentRoot9 if Freemind_DocumentRoot9 is not None else set()
        self.Freemind_DocumentRoot = Freemind_DocumentRoot if Freemind_DocumentRoot is not None else set()
        self.Freemind_DocumentRoot2 = Freemind_DocumentRoot2 if Freemind_DocumentRoot2 is not None else set()
        self.Freemind_DocumentRoot5 = Freemind_DocumentRoot5 if Freemind_DocumentRoot5 is not None else set()
        self.Freemind_DocumentRoot15 = Freemind_DocumentRoot15 if Freemind_DocumentRoot15 is not None else set()
        self.Freemind_DocumentRoot17 = Freemind_DocumentRoot17 if Freemind_DocumentRoot17 is not None else set()
        self.Freemind_DocumentRoot11 = Freemind_DocumentRoot11 if Freemind_DocumentRoot11 is not None else set()
        self.Freemind_DocumentRoot13 = Freemind_DocumentRoot13 if Freemind_DocumentRoot13 is not None else set()
        self.Freemind_DocumentRoot23 = Freemind_DocumentRoot23 if Freemind_DocumentRoot23 is not None else set()
        self.Freemind_DocumentRoot19 = Freemind_DocumentRoot19 if Freemind_DocumentRoot19 is not None else set()
        self.Freemind_DocumentRoot21 = Freemind_DocumentRoot21 if Freemind_DocumentRoot21 is not None else set()
        
    @property
    def mixed(self) -> str:
        return self.__mixed

    @mixed.setter
    def mixed(self, mixed: str):
        self.__mixed = mixed

    @property
    def Freemind_DocumentRoot23(self):
        return self.__Freemind_DocumentRoot23

    @Freemind_DocumentRoot23.setter
    def Freemind_DocumentRoot23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot23", None)
        self.__Freemind_DocumentRoot23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_TextType"):
                    opp_val = getattr(item, "Freemind_TextType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_TextType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_TextType"):
                    opp_val = getattr(item, "Freemind_TextType", None)
                    
                    setattr(item, "Freemind_TextType", self)
                    

    @property
    def Freemind_DocumentRoot7(self):
        return self.__Freemind_DocumentRoot7

    @Freemind_DocumentRoot7.setter
    def Freemind_DocumentRoot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot7", None)
        self.__Freemind_DocumentRoot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_CloudType"):
                    opp_val = getattr(item, "Freemind_CloudType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_CloudType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_CloudType"):
                    opp_val = getattr(item, "Freemind_CloudType", None)
                    
                    setattr(item, "Freemind_CloudType", self)
                    

    @property
    def Freemind_DocumentRoot21(self):
        return self.__Freemind_DocumentRoot21

    @Freemind_DocumentRoot21.setter
    def Freemind_DocumentRoot21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot21", None)
        self.__Freemind_DocumentRoot21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_ParametersType"):
                    opp_val = getattr(item, "Freemind_ParametersType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_ParametersType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_ParametersType"):
                    opp_val = getattr(item, "Freemind_ParametersType", None)
                    
                    setattr(item, "Freemind_ParametersType", self)
                    

    @property
    def Freemind_DocumentRoot9(self):
        return self.__Freemind_DocumentRoot9

    @Freemind_DocumentRoot9.setter
    def Freemind_DocumentRoot9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot9", None)
        self.__Freemind_DocumentRoot9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_EdgeType"):
                    opp_val = getattr(item, "Freemind_EdgeType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_EdgeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_EdgeType"):
                    opp_val = getattr(item, "Freemind_EdgeType", None)
                    
                    setattr(item, "Freemind_EdgeType", self)
                    

    @property
    def Freemind_DocumentRoot15(self):
        return self.__Freemind_DocumentRoot15

    @Freemind_DocumentRoot15.setter
    def Freemind_DocumentRoot15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot15", None)
        self.__Freemind_DocumentRoot15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_IconType"):
                    opp_val = getattr(item, "Freemind_IconType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_IconType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_IconType"):
                    opp_val = getattr(item, "Freemind_IconType", None)
                    
                    setattr(item, "Freemind_IconType", self)
                    

    @property
    def Freemind_DocumentRoot13(self):
        return self.__Freemind_DocumentRoot13

    @Freemind_DocumentRoot13.setter
    def Freemind_DocumentRoot13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot13", None)
        self.__Freemind_DocumentRoot13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_HookType"):
                    opp_val = getattr(item, "Freemind_HookType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_HookType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_HookType"):
                    opp_val = getattr(item, "Freemind_HookType", None)
                    
                    setattr(item, "Freemind_HookType", self)
                    

    @property
    def Freemind_DocumentRoot2(self):
        return self.__Freemind_DocumentRoot2

    @Freemind_DocumentRoot2.setter
    def Freemind_DocumentRoot2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot2", None)
        self.__Freemind_DocumentRoot2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "Freemind_EStringToStringMapEntry3", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_EStringToStringMapEntry3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_EStringToStringMapEntry3"):
                    opp_val = getattr(item, "Freemind_EStringToStringMapEntry3", None)
                    
                    setattr(item, "Freemind_EStringToStringMapEntry3", self)
                    

    @property
    def Freemind_DocumentRoot(self):
        return self.__Freemind_DocumentRoot

    @Freemind_DocumentRoot.setter
    def Freemind_DocumentRoot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot", None)
        self.__Freemind_DocumentRoot = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Freemind_EStringToStringMapEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_EStringToStringMapEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_EStringToStringMapEntry"):
                    opp_val = getattr(item, "Freemind_EStringToStringMapEntry", None)
                    
                    setattr(item, "Freemind_EStringToStringMapEntry", self)
                    

    @property
    def Freemind_DocumentRoot19(self):
        return self.__Freemind_DocumentRoot19

    @Freemind_DocumentRoot19.setter
    def Freemind_DocumentRoot19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot19", None)
        self.__Freemind_DocumentRoot19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_NodeType"):
                    opp_val = getattr(item, "Freemind_NodeType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_NodeType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_NodeType"):
                    opp_val = getattr(item, "Freemind_NodeType", None)
                    
                    setattr(item, "Freemind_NodeType", self)
                    

    @property
    def Freemind_DocumentRoot11(self):
        return self.__Freemind_DocumentRoot11

    @Freemind_DocumentRoot11.setter
    def Freemind_DocumentRoot11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot11", None)
        self.__Freemind_DocumentRoot11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_FontType"):
                    opp_val = getattr(item, "Freemind_FontType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_FontType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_FontType"):
                    opp_val = getattr(item, "Freemind_FontType", None)
                    
                    setattr(item, "Freemind_FontType", self)
                    

    @property
    def Freemind_DocumentRoot17(self):
        return self.__Freemind_DocumentRoot17

    @Freemind_DocumentRoot17.setter
    def Freemind_DocumentRoot17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot17", None)
        self.__Freemind_DocumentRoot17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_MapType"):
                    opp_val = getattr(item, "Freemind_MapType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_MapType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_MapType"):
                    opp_val = getattr(item, "Freemind_MapType", None)
                    
                    setattr(item, "Freemind_MapType", self)
                    

    @property
    def Freemind_DocumentRoot5(self):
        return self.__Freemind_DocumentRoot5

    @Freemind_DocumentRoot5.setter
    def Freemind_DocumentRoot5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_DocumentRoot__Freemind_DocumentRoot5", None)
        self.__Freemind_DocumentRoot5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Freemind_ArrowlinkType"):
                    opp_val = getattr(item, "Freemind_ArrowlinkType", None)
                    
                    if opp_val == self:
                        setattr(item, "Freemind_ArrowlinkType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Freemind_ArrowlinkType"):
                    opp_val = getattr(item, "Freemind_ArrowlinkType", None)
                    
                    setattr(item, "Freemind_ArrowlinkType", self)
                    

class Freemind_ArrowlinkType:

    def __init__(self, EndInclination: str, Id: str, StartArrow: str, Color: str, Destination: str, EndArrow: str, StartInclination: str, Freemind_ArrowlinkType: "Freemind_DocumentRoot" = None, Freemind_ArrowlinkType35: "Freemind_NodeType" = None):
        self.EndInclination = EndInclination
        self.Id = Id
        self.StartArrow = StartArrow
        self.Color = Color
        self.Destination = Destination
        self.EndArrow = EndArrow
        self.StartInclination = StartInclination
        self.Freemind_ArrowlinkType = Freemind_ArrowlinkType
        self.Freemind_ArrowlinkType35 = Freemind_ArrowlinkType35
        
    @property
    def StartArrow(self) -> str:
        return self.__StartArrow

    @StartArrow.setter
    def StartArrow(self, StartArrow: str):
        self.__StartArrow = StartArrow

    @property
    def Color(self) -> str:
        return self.__Color

    @Color.setter
    def Color(self, Color: str):
        self.__Color = Color

    @property
    def Id(self) -> str:
        return self.__Id

    @Id.setter
    def Id(self, Id: str):
        self.__Id = Id

    @property
    def StartInclination(self) -> str:
        return self.__StartInclination

    @StartInclination.setter
    def StartInclination(self, StartInclination: str):
        self.__StartInclination = StartInclination

    @property
    def EndArrow(self) -> str:
        return self.__EndArrow

    @EndArrow.setter
    def EndArrow(self, EndArrow: str):
        self.__EndArrow = EndArrow

    @property
    def EndInclination(self) -> str:
        return self.__EndInclination

    @EndInclination.setter
    def EndInclination(self, EndInclination: str):
        self.__EndInclination = EndInclination

    @property
    def Destination(self) -> str:
        return self.__Destination

    @Destination.setter
    def Destination(self, Destination: str):
        self.__Destination = Destination

    @property
    def Freemind_ArrowlinkType(self):
        return self.__Freemind_ArrowlinkType

    @Freemind_ArrowlinkType.setter
    def Freemind_ArrowlinkType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_ArrowlinkType__Freemind_ArrowlinkType", None)
        self.__Freemind_ArrowlinkType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_DocumentRoot5"):
                opp_val = getattr(old_value, "Freemind_DocumentRoot5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_DocumentRoot5"):
                opp_val = getattr(value, "Freemind_DocumentRoot5", None)
                if opp_val is None:
                    setattr(value, "Freemind_DocumentRoot5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Freemind_ArrowlinkType35(self):
        return self.__Freemind_ArrowlinkType35

    @Freemind_ArrowlinkType35.setter
    def Freemind_ArrowlinkType35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Freemind_ArrowlinkType__Freemind_ArrowlinkType35", None)
        self.__Freemind_ArrowlinkType35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Freemind_NodeType34"):
                opp_val = getattr(old_value, "Freemind_NodeType34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Freemind_NodeType34"):
                opp_val = getattr(value, "Freemind_NodeType34", None)
                if opp_val is None:
                    setattr(value, "Freemind_NodeType34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
