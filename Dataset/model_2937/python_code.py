from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class PageActionPositionKind(Enum):
    top = "top"
    center = "center"
    bottom = "bottom"
class PageKinds(Enum):
    custom = "custom"
    list = "list"
    details = "details"
class PageActionKind(Enum):
    SAVE = "SAVE"
    NEW = "NEW"
    SAVE_CLOSE = "SAVE_CLOSE"
    SAVE_COPY = "SAVE_COPY"
    CANCEL = "CANCEL"
    CLOSE = "CLOSE"
    ARCHIVE = "ARCHIVE"
    EDIT = "EDIT"
    PUBLISH = "PUBLISH"
    UNPUBLISH = "UNPUBLISH"
    HIDE = "HIDE"
    CHECKIN = "CHECKIN"
    TRASH = "TRASH"
    INDIVIDUAL = "INDIVIDUAL"
    LOGIN = "LOGIN"
    PWRESET = "PWRESET"
class SimpleHTMLTypeKinds(Enum):
    Integer = "Integer"
    Yes_No_Buttons = "Yes_No_Buttons"
    Textarea = "Textarea"
    Text_Field = "Text_Field"
    Link = "Link"
    Datepicker = "Datepicker"
    Imagepicker = "Imagepicker"
    Filepicker = "Filepicker"
    Text_Field_NE = "Text_Field_NE"
    Editor = "Editor"
class CoreComponent(Enum):
    User = "User"
    Menu = "Menu"
    Content = "Content"
class StandardTypeKinds(Enum):
    Integer = "Integer"
    Boolean = "Boolean"
    Text = "Text"
    Short_Text = "Short_Text"
    Time = "Time"
    Date = "Date"
    Datetime = "Datetime"
    Link = "Link"
    Image = "Image"
    File = "File"
    Label = "Label"
    Encrypted_Text = "Encrypted_Text"
class ComplexHTMLTypeKinds(Enum):
    Select = "Select"
    Multiselect = "Multiselect"
    Checkbox = "Checkbox"
    Radiobutton = "Radiobutton"
class DataAccessKinds(Enum):
    backendDAO = "backendDAO"
    frontendDAO = "frontendDAO"
    database = "database"
    webservice = "webservice"
class PluginKinds(Enum):
    authenticate = "authenticate"
    captcha = "captcha"
    content = "content"
    contact = "contact"
    editors = "editors"
    extensions = "extensions"
    finder = "finder"
    quick_icons = "quick_icons"
    search = "search"
    system = "system"
    user = "user"
    xml_rpc = "xml_rpc"


############################################
# Definition of Classes
############################################

class eJSL_PositionParameter:

    def __init__(self, name: str, divid: str, type: str, eJSL_PositionParameter: "eJSL_Position" = None, eJSL_PositionParameter184: set["eJSL_KeyValuePair"] = None):
        self.name = name
        self.divid = divid
        self.type = type
        self.eJSL_PositionParameter = eJSL_PositionParameter
        self.eJSL_PositionParameter184 = eJSL_PositionParameter184 if eJSL_PositionParameter184 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def divid(self) -> str:
        return self.__divid

    @divid.setter
    def divid(self, divid: str):
        self.__divid = divid

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def eJSL_PositionParameter(self):
        return self.__eJSL_PositionParameter

    @eJSL_PositionParameter.setter
    def eJSL_PositionParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_PositionParameter__eJSL_PositionParameter", None)
        self.__eJSL_PositionParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Position182"):
                opp_val = getattr(old_value, "eJSL_Position182", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Position182"):
                opp_val = getattr(value, "eJSL_Position182", None)
                if opp_val is None:
                    setattr(value, "eJSL_Position182", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_PositionParameter184(self):
        return self.__eJSL_PositionParameter184

    @eJSL_PositionParameter184.setter
    def eJSL_PositionParameter184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_PositionParameter__eJSL_PositionParameter184", None)
        self.__eJSL_PositionParameter184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_KeyValuePair185"):
                    opp_val = getattr(item, "eJSL_KeyValuePair185", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_KeyValuePair185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_KeyValuePair185"):
                    opp_val = getattr(item, "eJSL_KeyValuePair185", None)
                    
                    setattr(item, "eJSL_KeyValuePair185", self)
                    

class eJSL_Author:

    def __init__(self, name: str, authoremail: str, authorurl: str, eJSL_Author: "eJSL_Manifestation" = None):
        self.name = name
        self.authoremail = authoremail
        self.authorurl = authorurl
        self.eJSL_Author = eJSL_Author
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def authoremail(self) -> str:
        return self.__authoremail

    @authoremail.setter
    def authoremail(self, authoremail: str):
        self.__authoremail = authoremail

    @property
    def authorurl(self) -> str:
        return self.__authorurl

    @authorurl.setter
    def authorurl(self, authorurl: str):
        self.__authorurl = authorurl

    @property
    def eJSL_Author(self):
        return self.__eJSL_Author

    @eJSL_Author.setter
    def eJSL_Author(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Author__eJSL_Author", None)
        self.__eJSL_Author = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Manifestation177"):
                opp_val = getattr(old_value, "eJSL_Manifestation177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Manifestation177"):
                opp_val = getattr(value, "eJSL_Manifestation177", None)
                if opp_val is None:
                    setattr(value, "eJSL_Manifestation177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_CssBlock:

    def __init__(self, selector: str, eJSL_CssBlock: "eJSL_Template" = None, eJSL_CssBlock187: set["eJSL_KeyValuePair"] = None):
        self.selector = selector
        self.eJSL_CssBlock = eJSL_CssBlock
        self.eJSL_CssBlock187 = eJSL_CssBlock187 if eJSL_CssBlock187 is not None else set()
        
    @property
    def selector(self) -> str:
        return self.__selector

    @selector.setter
    def selector(self, selector: str):
        self.__selector = selector

    @property
    def eJSL_CssBlock187(self):
        return self.__eJSL_CssBlock187

    @eJSL_CssBlock187.setter
    def eJSL_CssBlock187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_CssBlock__eJSL_CssBlock187", None)
        self.__eJSL_CssBlock187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_KeyValuePair188"):
                    opp_val = getattr(item, "eJSL_KeyValuePair188", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_KeyValuePair188", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_KeyValuePair188"):
                    opp_val = getattr(item, "eJSL_KeyValuePair188", None)
                    
                    setattr(item, "eJSL_KeyValuePair188", self)
                    

    @property
    def eJSL_CssBlock(self):
        return self.__eJSL_CssBlock

    @eJSL_CssBlock.setter
    def eJSL_CssBlock(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_CssBlock__eJSL_CssBlock", None)
        self.__eJSL_CssBlock = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Template175"):
                opp_val = getattr(old_value, "eJSL_Template175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Template175"):
                opp_val = getattr(value, "eJSL_Template175", None)
                if opp_val is None:
                    setattr(value, "eJSL_Template175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Position:

    def __init__(self, name: str, eJSL_Position: "eJSL_Template" = None, eJSL_Position182: set["eJSL_PositionParameter"] = None):
        self.name = name
        self.eJSL_Position = eJSL_Position
        self.eJSL_Position182 = eJSL_Position182 if eJSL_Position182 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Position(self):
        return self.__eJSL_Position

    @eJSL_Position.setter
    def eJSL_Position(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Position__eJSL_Position", None)
        self.__eJSL_Position = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Template173"):
                opp_val = getattr(old_value, "eJSL_Template173", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Template173"):
                opp_val = getattr(value, "eJSL_Template173", None)
                if opp_val is None:
                    setattr(value, "eJSL_Template173", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Position182(self):
        return self.__eJSL_Position182

    @eJSL_Position182.setter
    def eJSL_Position182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Position__eJSL_Position182", None)
        self.__eJSL_Position182 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_PositionParameter"):
                    opp_val = getattr(item, "eJSL_PositionParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_PositionParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_PositionParameter"):
                    opp_val = getattr(item, "eJSL_PositionParameter", None)
                    
                    setattr(item, "eJSL_PositionParameter", self)
                    

class eJSL_MethodParameter:

    def __init__(self, name: str, eJSL_MethodParameter: "eJSL_Method" = None, eJSL_MethodParameter168: "eJSL_Type" = None):
        self.name = name
        self.eJSL_MethodParameter = eJSL_MethodParameter
        self.eJSL_MethodParameter168 = eJSL_MethodParameter168
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_MethodParameter168(self):
        return self.__eJSL_MethodParameter168

    @eJSL_MethodParameter168.setter
    def eJSL_MethodParameter168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_MethodParameter__eJSL_MethodParameter168", None)
        self.__eJSL_MethodParameter168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Type169"):
                opp_val = getattr(old_value, "eJSL_Type169", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Type169", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Type169"):
                opp_val = getattr(value, "eJSL_Type169", None)
                setattr(value, "eJSL_Type169", self)

    @property
    def eJSL_MethodParameter(self):
        return self.__eJSL_MethodParameter

    @eJSL_MethodParameter.setter
    def eJSL_MethodParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_MethodParameter__eJSL_MethodParameter", None)
        self.__eJSL_MethodParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Method166"):
                opp_val = getattr(old_value, "eJSL_Method166", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Method166"):
                opp_val = getattr(value, "eJSL_Method166", None)
                if opp_val is None:
                    setattr(value, "eJSL_Method166", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_ComponentReference:

    def __init__(self, core: str, eJSL_ComponentReference130: "eJSL_Component" = None, eJSL_ComponentReference: "eJSL_PageReference" = None):
        self.core = core
        self.eJSL_ComponentReference130 = eJSL_ComponentReference130
        self.eJSL_ComponentReference = eJSL_ComponentReference
        
    @property
    def core(self) -> str:
        return self.__core

    @core.setter
    def core(self, core: str):
        self.__core = core

    @property
    def eJSL_ComponentReference(self):
        return self.__eJSL_ComponentReference

    @eJSL_ComponentReference.setter
    def eJSL_ComponentReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_ComponentReference__eJSL_ComponentReference", None)
        self.__eJSL_ComponentReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_PageReference128"):
                opp_val = getattr(old_value, "eJSL_PageReference128", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_PageReference128", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_PageReference128"):
                opp_val = getattr(value, "eJSL_PageReference128", None)
                setattr(value, "eJSL_PageReference128", self)

    @property
    def eJSL_ComponentReference130(self):
        return self.__eJSL_ComponentReference130

    @eJSL_ComponentReference130.setter
    def eJSL_ComponentReference130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_ComponentReference__eJSL_ComponentReference130", None)
        self.__eJSL_ComponentReference130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Component131"):
                opp_val = getattr(old_value, "eJSL_Component131", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Component131", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Component131"):
                opp_val = getattr(value, "eJSL_Component131", None)
                setattr(value, "eJSL_Component131", self)

class eJSL_Method:

    def __init__(self, name: str, returnvalue: str, eJSL_Method: "eJSL_Class" = None, eJSL_Method166: set["eJSL_MethodParameter"] = None, eJSL_Method163: "eJSL_Type" = None):
        self.name = name
        self.returnvalue = returnvalue
        self.eJSL_Method = eJSL_Method
        self.eJSL_Method166 = eJSL_Method166 if eJSL_Method166 is not None else set()
        self.eJSL_Method163 = eJSL_Method163
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returnvalue(self) -> str:
        return self.__returnvalue

    @returnvalue.setter
    def returnvalue(self, returnvalue: str):
        self.__returnvalue = returnvalue

    @property
    def eJSL_Method163(self):
        return self.__eJSL_Method163

    @eJSL_Method163.setter
    def eJSL_Method163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Method__eJSL_Method163", None)
        self.__eJSL_Method163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Type164"):
                opp_val = getattr(old_value, "eJSL_Type164", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Type164", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Type164"):
                opp_val = getattr(value, "eJSL_Type164", None)
                setattr(value, "eJSL_Type164", self)

    @property
    def eJSL_Method166(self):
        return self.__eJSL_Method166

    @eJSL_Method166.setter
    def eJSL_Method166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Method__eJSL_Method166", None)
        self.__eJSL_Method166 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_MethodParameter"):
                    opp_val = getattr(item, "eJSL_MethodParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_MethodParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_MethodParameter"):
                    opp_val = getattr(item, "eJSL_MethodParameter", None)
                    
                    setattr(item, "eJSL_MethodParameter", self)
                    

    @property
    def eJSL_Method(self):
        return self.__eJSL_Method

    @eJSL_Method.setter
    def eJSL_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Method__eJSL_Method", None)
        self.__eJSL_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Class161"):
                opp_val = getattr(old_value, "eJSL_Class161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Class161"):
                opp_val = getattr(value, "eJSL_Class161", None)
                if opp_val is None:
                    setattr(value, "eJSL_Class161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Package:

    def __init__(self, name: str, eJSL_Package: "eJSL_Library" = None, eJSL_Package147: "eJSL_Package" = None, eJSL_Package145: set["eJSL_Package"] = None, eJSL_Package149: set["eJSL_Class"] = None):
        self.name = name
        self.eJSL_Package = eJSL_Package
        self.eJSL_Package147 = eJSL_Package147
        self.eJSL_Package145 = eJSL_Package145 if eJSL_Package145 is not None else set()
        self.eJSL_Package149 = eJSL_Package149 if eJSL_Package149 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Package147(self):
        return self.__eJSL_Package147

    @eJSL_Package147.setter
    def eJSL_Package147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Package__eJSL_Package147", None)
        self.__eJSL_Package147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Package145"):
                opp_val = getattr(old_value, "eJSL_Package145", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Package145"):
                opp_val = getattr(value, "eJSL_Package145", None)
                if opp_val is None:
                    setattr(value, "eJSL_Package145", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Package149(self):
        return self.__eJSL_Package149

    @eJSL_Package149.setter
    def eJSL_Package149(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Package__eJSL_Package149", None)
        self.__eJSL_Package149 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Class150"):
                    opp_val = getattr(item, "eJSL_Class150", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Class150", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Class150"):
                    opp_val = getattr(item, "eJSL_Class150", None)
                    
                    setattr(item, "eJSL_Class150", self)
                    

    @property
    def eJSL_Package145(self):
        return self.__eJSL_Package145

    @eJSL_Package145.setter
    def eJSL_Package145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Package__eJSL_Package145", None)
        self.__eJSL_Package145 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Package147"):
                    opp_val = getattr(item, "eJSL_Package147", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Package147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Package147"):
                    opp_val = getattr(item, "eJSL_Package147", None)
                    
                    setattr(item, "eJSL_Package147", self)
                    

    @property
    def eJSL_Package(self):
        return self.__eJSL_Package

    @eJSL_Package.setter
    def eJSL_Package(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Package__eJSL_Package", None)
        self.__eJSL_Package = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Library144"):
                opp_val = getattr(old_value, "eJSL_Library144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Library144"):
                opp_val = getattr(value, "eJSL_Library144", None)
                if opp_val is None:
                    setattr(value, "eJSL_Library144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Class:

    def __init__(self, name: str, eJSL_Class: "eJSL_Library" = None, eJSL_Class150: "eJSL_Package" = None, eJSL_Class153: "eJSL_Class" = None, eJSL_Class151: "eJSL_Class" = None, eJSL_Class156: "eJSL_Class" = None, eJSL_Class154: set["eJSL_Class"] = None, eJSL_Class158: set["eJSL_Entity"] = None, eJSL_Class161: set["eJSL_Method"] = None):
        self.name = name
        self.eJSL_Class = eJSL_Class
        self.eJSL_Class150 = eJSL_Class150
        self.eJSL_Class153 = eJSL_Class153
        self.eJSL_Class151 = eJSL_Class151
        self.eJSL_Class156 = eJSL_Class156
        self.eJSL_Class154 = eJSL_Class154 if eJSL_Class154 is not None else set()
        self.eJSL_Class158 = eJSL_Class158 if eJSL_Class158 is not None else set()
        self.eJSL_Class161 = eJSL_Class161 if eJSL_Class161 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Class150(self):
        return self.__eJSL_Class150

    @eJSL_Class150.setter
    def eJSL_Class150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Class__eJSL_Class150", None)
        self.__eJSL_Class150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Package149"):
                opp_val = getattr(old_value, "eJSL_Package149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Package149"):
                opp_val = getattr(value, "eJSL_Package149", None)
                if opp_val is None:
                    setattr(value, "eJSL_Package149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Class151(self):
        return self.__eJSL_Class151

    @eJSL_Class151.setter
    def eJSL_Class151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Class__eJSL_Class151", None)
        self.__eJSL_Class151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Class153"):
                opp_val = getattr(old_value, "eJSL_Class153", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Class153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Class153"):
                opp_val = getattr(value, "eJSL_Class153", None)
                setattr(value, "eJSL_Class153", self)

    @property
    def eJSL_Class154(self):
        return self.__eJSL_Class154

    @eJSL_Class154.setter
    def eJSL_Class154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Class__eJSL_Class154", None)
        self.__eJSL_Class154 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Class156"):
                    opp_val = getattr(item, "eJSL_Class156", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Class156", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Class156"):
                    opp_val = getattr(item, "eJSL_Class156", None)
                    
                    setattr(item, "eJSL_Class156", self)
                    

    @property
    def eJSL_Class(self):
        return self.__eJSL_Class

    @eJSL_Class.setter
    def eJSL_Class(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Class__eJSL_Class", None)
        self.__eJSL_Class = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Library142"):
                opp_val = getattr(old_value, "eJSL_Library142", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Library142"):
                opp_val = getattr(value, "eJSL_Library142", None)
                if opp_val is None:
                    setattr(value, "eJSL_Library142", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Class161(self):
        return self.__eJSL_Class161

    @eJSL_Class161.setter
    def eJSL_Class161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Class__eJSL_Class161", None)
        self.__eJSL_Class161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Method"):
                    opp_val = getattr(item, "eJSL_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Method"):
                    opp_val = getattr(item, "eJSL_Method", None)
                    
                    setattr(item, "eJSL_Method", self)
                    

    @property
    def eJSL_Class153(self):
        return self.__eJSL_Class153

    @eJSL_Class153.setter
    def eJSL_Class153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Class__eJSL_Class153", None)
        self.__eJSL_Class153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Class151"):
                opp_val = getattr(old_value, "eJSL_Class151", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Class151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Class151"):
                opp_val = getattr(value, "eJSL_Class151", None)
                setattr(value, "eJSL_Class151", self)

    @property
    def eJSL_Class156(self):
        return self.__eJSL_Class156

    @eJSL_Class156.setter
    def eJSL_Class156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Class__eJSL_Class156", None)
        self.__eJSL_Class156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Class154"):
                opp_val = getattr(old_value, "eJSL_Class154", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Class154"):
                opp_val = getattr(value, "eJSL_Class154", None)
                if opp_val is None:
                    setattr(value, "eJSL_Class154", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Class158(self):
        return self.__eJSL_Class158

    @eJSL_Class158.setter
    def eJSL_Class158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Class__eJSL_Class158", None)
        self.__eJSL_Class158 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Entity159"):
                    opp_val = getattr(item, "eJSL_Entity159", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Entity159", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Entity159"):
                    opp_val = getattr(item, "eJSL_Entity159", None)
                    
                    setattr(item, "eJSL_Entity159", self)
                    

class Section:

    pass
class eJSL_FrontendSection(Section):

    pass
class eJSL_BackendSection(Section):

    pass
class eJSL_PageReference:

    def __init__(self, sect: str, eJSL_PageReference: "eJSL_Section" = None, eJSL_PageReference133: "eJSL_Module" = None, eJSL_PageReference125: "eJSL_Page" = None, eJSL_PageReference128: "eJSL_ComponentReference" = None):
        self.sect = sect
        self.eJSL_PageReference = eJSL_PageReference
        self.eJSL_PageReference133 = eJSL_PageReference133
        self.eJSL_PageReference125 = eJSL_PageReference125
        self.eJSL_PageReference128 = eJSL_PageReference128
        
    @property
    def sect(self) -> str:
        return self.__sect

    @sect.setter
    def sect(self, sect: str):
        self.__sect = sect

    @property
    def eJSL_PageReference128(self):
        return self.__eJSL_PageReference128

    @eJSL_PageReference128.setter
    def eJSL_PageReference128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_PageReference__eJSL_PageReference128", None)
        self.__eJSL_PageReference128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_ComponentReference"):
                opp_val = getattr(old_value, "eJSL_ComponentReference", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_ComponentReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_ComponentReference"):
                opp_val = getattr(value, "eJSL_ComponentReference", None)
                setattr(value, "eJSL_ComponentReference", self)

    @property
    def eJSL_PageReference(self):
        return self.__eJSL_PageReference

    @eJSL_PageReference.setter
    def eJSL_PageReference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_PageReference__eJSL_PageReference", None)
        self.__eJSL_PageReference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Section123"):
                opp_val = getattr(old_value, "eJSL_Section123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Section123"):
                opp_val = getattr(value, "eJSL_Section123", None)
                if opp_val is None:
                    setattr(value, "eJSL_Section123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_PageReference125(self):
        return self.__eJSL_PageReference125

    @eJSL_PageReference125.setter
    def eJSL_PageReference125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_PageReference__eJSL_PageReference125", None)
        self.__eJSL_PageReference125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Page126"):
                opp_val = getattr(old_value, "eJSL_Page126", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Page126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Page126"):
                opp_val = getattr(value, "eJSL_Page126", None)
                setattr(value, "eJSL_Page126", self)

    @property
    def eJSL_PageReference133(self):
        return self.__eJSL_PageReference133

    @eJSL_PageReference133.setter
    def eJSL_PageReference133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_PageReference__eJSL_PageReference133", None)
        self.__eJSL_PageReference133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Module"):
                opp_val = getattr(old_value, "eJSL_Module", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Module", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Module"):
                opp_val = getattr(value, "eJSL_Module", None)
                setattr(value, "eJSL_Module", self)

class Extension:

    pass
class eJSL_Module(Extension):

    pass
class eJSL_Library(Extension):

    pass
class eJSL_Template(Extension):

    pass
class eJSL_Component(Extension):

    pass
class eJSL_Plugin(Extension):

    def __init__(self, type: str, eJSL_Plugin: set["eJSL_Entity"] = None, eJSL_Plugin137: set["eJSL_Parameter"] = None):
        self.type = type
        self.eJSL_Plugin = eJSL_Plugin if eJSL_Plugin is not None else set()
        self.eJSL_Plugin137 = eJSL_Plugin137 if eJSL_Plugin137 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def eJSL_Plugin(self):
        return self.__eJSL_Plugin

    @eJSL_Plugin.setter
    def eJSL_Plugin(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Plugin__eJSL_Plugin", None)
        self.__eJSL_Plugin = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Entity135"):
                    opp_val = getattr(item, "eJSL_Entity135", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Entity135", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Entity135"):
                    opp_val = getattr(item, "eJSL_Entity135", None)
                    
                    setattr(item, "eJSL_Entity135", self)
                    

    @property
    def eJSL_Plugin137(self):
        return self.__eJSL_Plugin137

    @eJSL_Plugin137.setter
    def eJSL_Plugin137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Plugin__eJSL_Plugin137", None)
        self.__eJSL_Plugin137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Parameter138"):
                    opp_val = getattr(item, "eJSL_Parameter138", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Parameter138", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Parameter138"):
                    opp_val = getattr(item, "eJSL_Parameter138", None)
                    
                    setattr(item, "eJSL_Parameter138", self)
                    

class eJSL_ExtensionPackage(Extension):

    pass
class eJSL_Language:

    def __init__(self, sys: bool, name: str, eJSL_Language: "eJSL_Extension" = None, eJSL_Language179: set["eJSL_KeyValuePair"] = None):
        self.sys = sys
        self.name = name
        self.eJSL_Language = eJSL_Language
        self.eJSL_Language179 = eJSL_Language179 if eJSL_Language179 is not None else set()
        
    @property
    def sys(self) -> bool:
        return self.__sys

    @sys.setter
    def sys(self, sys: bool):
        self.__sys = sys

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Language179(self):
        return self.__eJSL_Language179

    @eJSL_Language179.setter
    def eJSL_Language179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Language__eJSL_Language179", None)
        self.__eJSL_Language179 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_KeyValuePair180"):
                    opp_val = getattr(item, "eJSL_KeyValuePair180", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_KeyValuePair180", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_KeyValuePair180"):
                    opp_val = getattr(item, "eJSL_KeyValuePair180", None)
                    
                    setattr(item, "eJSL_KeyValuePair180", self)
                    

    @property
    def eJSL_Language(self):
        return self.__eJSL_Language

    @eJSL_Language.setter
    def eJSL_Language(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Language__eJSL_Language", None)
        self.__eJSL_Language = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Extension114"):
                opp_val = getattr(old_value, "eJSL_Extension114", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Extension114"):
                opp_val = getattr(value, "eJSL_Extension114", None)
                if opp_val is None:
                    setattr(value, "eJSL_Extension114", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Manifestation:

    def __init__(self, creationdate: str, copyright: str, license: str, link: str, version: str, description: str, eJSL_Manifestation: "eJSL_Extension" = None, eJSL_Manifestation177: set["eJSL_Author"] = None):
        self.creationdate = creationdate
        self.copyright = copyright
        self.license = license
        self.link = link
        self.version = version
        self.description = description
        self.eJSL_Manifestation = eJSL_Manifestation
        self.eJSL_Manifestation177 = eJSL_Manifestation177 if eJSL_Manifestation177 is not None else set()
        
    @property
    def license(self) -> str:
        return self.__license

    @license.setter
    def license(self, license: str):
        self.__license = license

    @property
    def link(self) -> str:
        return self.__link

    @link.setter
    def link(self, link: str):
        self.__link = link

    @property
    def copyright(self) -> str:
        return self.__copyright

    @copyright.setter
    def copyright(self, copyright: str):
        self.__copyright = copyright

    @property
    def version(self) -> str:
        return self.__version

    @version.setter
    def version(self, version: str):
        self.__version = version

    @property
    def creationdate(self) -> str:
        return self.__creationdate

    @creationdate.setter
    def creationdate(self, creationdate: str):
        self.__creationdate = creationdate

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def eJSL_Manifestation(self):
        return self.__eJSL_Manifestation

    @eJSL_Manifestation.setter
    def eJSL_Manifestation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Manifestation__eJSL_Manifestation", None)
        self.__eJSL_Manifestation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Extension112"):
                opp_val = getattr(old_value, "eJSL_Extension112", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Extension112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Extension112"):
                opp_val = getattr(value, "eJSL_Extension112", None)
                setattr(value, "eJSL_Extension112", self)

    @property
    def eJSL_Manifestation177(self):
        return self.__eJSL_Manifestation177

    @eJSL_Manifestation177.setter
    def eJSL_Manifestation177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Manifestation__eJSL_Manifestation177", None)
        self.__eJSL_Manifestation177 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Author"):
                    opp_val = getattr(item, "eJSL_Author", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Author", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Author"):
                    opp_val = getattr(item, "eJSL_Author", None)
                    
                    setattr(item, "eJSL_Author", self)
                    

class eJSL_LinkParameter:

    def __init__(self, name: str, id: bool, value: str, eJSL_LinkParameter: "eJSL_ContextLink" = None, eJSL_LinkParameter109: "eJSL_Attribute" = None):
        self.name = name
        self.id = id
        self.value = value
        self.eJSL_LinkParameter = eJSL_LinkParameter
        self.eJSL_LinkParameter109 = eJSL_LinkParameter109
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def id(self) -> bool:
        return self.__id

    @id.setter
    def id(self, id: bool):
        self.__id = id

    @property
    def eJSL_LinkParameter(self):
        return self.__eJSL_LinkParameter

    @eJSL_LinkParameter.setter
    def eJSL_LinkParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_LinkParameter__eJSL_LinkParameter", None)
        self.__eJSL_LinkParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_ContextLink"):
                opp_val = getattr(old_value, "eJSL_ContextLink", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_ContextLink"):
                opp_val = getattr(value, "eJSL_ContextLink", None)
                if opp_val is None:
                    setattr(value, "eJSL_ContextLink", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_LinkParameter109(self):
        return self.__eJSL_LinkParameter109

    @eJSL_LinkParameter109.setter
    def eJSL_LinkParameter109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_LinkParameter__eJSL_LinkParameter109", None)
        self.__eJSL_LinkParameter109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Attribute110"):
                opp_val = getattr(old_value, "eJSL_Attribute110", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Attribute110", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Attribute110"):
                opp_val = getattr(value, "eJSL_Attribute110", None)
                setattr(value, "eJSL_Attribute110", self)

class InternalLink:

    pass
class eJSL_ContextLink(InternalLink):

    pass
class Link:

    pass
class eJSL_InternalLink(Link):

    def __init__(self, name: str, eJSL_InternalLink: "eJSL_Page" = None):
        self.name = name
        self.eJSL_InternalLink = eJSL_InternalLink
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_InternalLink(self):
        return self.__eJSL_InternalLink

    @eJSL_InternalLink.setter
    def eJSL_InternalLink(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_InternalLink__eJSL_InternalLink", None)
        self.__eJSL_InternalLink = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Page106"):
                opp_val = getattr(old_value, "eJSL_Page106", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Page106", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Page106"):
                opp_val = getattr(value, "eJSL_Page106", None)
                setattr(value, "eJSL_Page106", self)

class eJSL_ExternalLink(Link):

    def __init__(self, target: str, label: str):
        self.target = target
        self.label = label
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def target(self) -> str:
        return self.__target

    @target.setter
    def target(self, target: str):
        self.__target = target

class eJSL_DetailPageField:

    pass
class DynamicPage:

    pass
class eJSL_DetailsPage(DynamicPage):

    pass
class eJSL_IndexPage(DynamicPage):

    pass
class Page:

    pass
class eJSL_CustomPage(Page):

    def __init__(self, preserve: str, pageType: str, eJSL_CustomPage: set["eJSL_Entity"] = None):
        self.preserve = preserve
        self.pageType = pageType
        self.eJSL_CustomPage = eJSL_CustomPage if eJSL_CustomPage is not None else set()
        
    @property
    def preserve(self) -> str:
        return self.__preserve

    @preserve.setter
    def preserve(self, preserve: str):
        self.__preserve = preserve

    @property
    def pageType(self) -> str:
        return self.__pageType

    @pageType.setter
    def pageType(self, pageType: str):
        self.__pageType = pageType

    @property
    def eJSL_CustomPage(self):
        return self.__eJSL_CustomPage

    @eJSL_CustomPage.setter
    def eJSL_CustomPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_CustomPage__eJSL_CustomPage", None)
        self.__eJSL_CustomPage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Entity98"):
                    opp_val = getattr(item, "eJSL_Entity98", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Entity98", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Entity98"):
                    opp_val = getattr(item, "eJSL_Entity98", None)
                    
                    setattr(item, "eJSL_Entity98", self)
                    

class eJSL_DynamicPage(Page):

    def __init__(self, preserve: bool, eJSL_DynamicPage: set["eJSL_Entity"] = None, eJSL_DynamicPage79: set["eJSL_Attribute"] = None, eJSL_DynamicPage82: set["eJSL_Attribute"] = None):
        self.preserve = preserve
        self.eJSL_DynamicPage = eJSL_DynamicPage if eJSL_DynamicPage is not None else set()
        self.eJSL_DynamicPage79 = eJSL_DynamicPage79 if eJSL_DynamicPage79 is not None else set()
        self.eJSL_DynamicPage82 = eJSL_DynamicPage82 if eJSL_DynamicPage82 is not None else set()
        
    @property
    def preserve(self) -> bool:
        return self.__preserve

    @preserve.setter
    def preserve(self, preserve: bool):
        self.__preserve = preserve

    @property
    def eJSL_DynamicPage(self):
        return self.__eJSL_DynamicPage

    @eJSL_DynamicPage.setter
    def eJSL_DynamicPage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_DynamicPage__eJSL_DynamicPage", None)
        self.__eJSL_DynamicPage = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Entity77"):
                    opp_val = getattr(item, "eJSL_Entity77", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Entity77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Entity77"):
                    opp_val = getattr(item, "eJSL_Entity77", None)
                    
                    setattr(item, "eJSL_Entity77", self)
                    

    @property
    def eJSL_DynamicPage79(self):
        return self.__eJSL_DynamicPage79

    @eJSL_DynamicPage79.setter
    def eJSL_DynamicPage79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_DynamicPage__eJSL_DynamicPage79", None)
        self.__eJSL_DynamicPage79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Attribute80"):
                    opp_val = getattr(item, "eJSL_Attribute80", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Attribute80", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Attribute80"):
                    opp_val = getattr(item, "eJSL_Attribute80", None)
                    
                    setattr(item, "eJSL_Attribute80", self)
                    

    @property
    def eJSL_DynamicPage82(self):
        return self.__eJSL_DynamicPage82

    @eJSL_DynamicPage82.setter
    def eJSL_DynamicPage82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_DynamicPage__eJSL_DynamicPage82", None)
        self.__eJSL_DynamicPage82 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Attribute83"):
                    opp_val = getattr(item, "eJSL_Attribute83", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Attribute83", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Attribute83"):
                    opp_val = getattr(item, "eJSL_Attribute83", None)
                    
                    setattr(item, "eJSL_Attribute83", self)
                    

class eJSL_StaticPage(Page):

    def __init__(self, preserve: bool, HTMLBody: str):
        self.preserve = preserve
        self.HTMLBody = HTMLBody
        
    @property
    def preserve(self) -> bool:
        return self.__preserve

    @preserve.setter
    def preserve(self, preserve: bool):
        self.__preserve = preserve

    @property
    def HTMLBody(self) -> str:
        return self.__HTMLBody

    @HTMLBody.setter
    def HTMLBody(self, HTMLBody: str):
        self.__HTMLBody = HTMLBody

class eJSL_Link:

    pass
class eJSL_PageAction:

    def __init__(self, name: str, pageActionType: str, pageActionPosition: str, eJSL_PageAction: "eJSL_Page" = None, eJSL_PageAction104: "eJSL_Link" = None):
        self.name = name
        self.pageActionType = pageActionType
        self.pageActionPosition = pageActionPosition
        self.eJSL_PageAction = eJSL_PageAction
        self.eJSL_PageAction104 = eJSL_PageAction104
        
    @property
    def pageActionType(self) -> str:
        return self.__pageActionType

    @pageActionType.setter
    def pageActionType(self, pageActionType: str):
        self.__pageActionType = pageActionType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pageActionPosition(self) -> str:
        return self.__pageActionPosition

    @pageActionPosition.setter
    def pageActionPosition(self, pageActionPosition: str):
        self.__pageActionPosition = pageActionPosition

    @property
    def eJSL_PageAction104(self):
        return self.__eJSL_PageAction104

    @eJSL_PageAction104.setter
    def eJSL_PageAction104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_PageAction__eJSL_PageAction104", None)
        self.__eJSL_PageAction104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Link103"):
                opp_val = getattr(old_value, "eJSL_Link103", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Link103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Link103"):
                opp_val = getattr(value, "eJSL_Link103", None)
                setattr(value, "eJSL_Link103", self)

    @property
    def eJSL_PageAction(self):
        return self.__eJSL_PageAction

    @eJSL_PageAction.setter
    def eJSL_PageAction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_PageAction__eJSL_PageAction", None)
        self.__eJSL_PageAction = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Page73"):
                opp_val = getattr(old_value, "eJSL_Page73", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Page73"):
                opp_val = getattr(value, "eJSL_Page73", None)
                if opp_val is None:
                    setattr(value, "eJSL_Page73", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Reference:

    def __init__(self, preserve: bool, id: bool, lower: str, upper: str, eJSL_Reference: "eJSL_Entity" = None, eJSL_Reference55: set["eJSL_Attribute"] = None, eJSL_Reference58: "eJSL_Entity" = None, eJSL_Reference61: set["eJSL_Attribute"] = None):
        self.preserve = preserve
        self.id = id
        self.lower = lower
        self.upper = upper
        self.eJSL_Reference = eJSL_Reference
        self.eJSL_Reference55 = eJSL_Reference55 if eJSL_Reference55 is not None else set()
        self.eJSL_Reference58 = eJSL_Reference58
        self.eJSL_Reference61 = eJSL_Reference61 if eJSL_Reference61 is not None else set()
        
    @property
    def lower(self) -> str:
        return self.__lower

    @lower.setter
    def lower(self, lower: str):
        self.__lower = lower

    @property
    def id(self) -> bool:
        return self.__id

    @id.setter
    def id(self, id: bool):
        self.__id = id

    @property
    def upper(self) -> str:
        return self.__upper

    @upper.setter
    def upper(self, upper: str):
        self.__upper = upper

    @property
    def preserve(self) -> bool:
        return self.__preserve

    @preserve.setter
    def preserve(self, preserve: bool):
        self.__preserve = preserve

    @property
    def eJSL_Reference58(self):
        return self.__eJSL_Reference58

    @eJSL_Reference58.setter
    def eJSL_Reference58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Reference__eJSL_Reference58", None)
        self.__eJSL_Reference58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Entity59"):
                opp_val = getattr(old_value, "eJSL_Entity59", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Entity59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Entity59"):
                opp_val = getattr(value, "eJSL_Entity59", None)
                setattr(value, "eJSL_Entity59", self)

    @property
    def eJSL_Reference(self):
        return self.__eJSL_Reference

    @eJSL_Reference.setter
    def eJSL_Reference(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Reference__eJSL_Reference", None)
        self.__eJSL_Reference = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Entity48"):
                opp_val = getattr(old_value, "eJSL_Entity48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Entity48"):
                opp_val = getattr(value, "eJSL_Entity48", None)
                if opp_val is None:
                    setattr(value, "eJSL_Entity48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Reference61(self):
        return self.__eJSL_Reference61

    @eJSL_Reference61.setter
    def eJSL_Reference61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Reference__eJSL_Reference61", None)
        self.__eJSL_Reference61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Attribute62"):
                    opp_val = getattr(item, "eJSL_Attribute62", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Attribute62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Attribute62"):
                    opp_val = getattr(item, "eJSL_Attribute62", None)
                    
                    setattr(item, "eJSL_Attribute62", self)
                    

    @property
    def eJSL_Reference55(self):
        return self.__eJSL_Reference55

    @eJSL_Reference55.setter
    def eJSL_Reference55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Reference__eJSL_Reference55", None)
        self.__eJSL_Reference55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Attribute56"):
                    opp_val = getattr(item, "eJSL_Attribute56", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Attribute56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Attribute56"):
                    opp_val = getattr(item, "eJSL_Attribute56", None)
                    
                    setattr(item, "eJSL_Attribute56", self)
                    

class eJSL_Attribute:

    def __init__(self, name: str, preserve: bool, isunique: bool, id: bool, isprimary: bool, eJSL_Attribute: "eJSL_Entity" = None, eJSL_Attribute50: "eJSL_Type" = None, eJSL_Attribute53: "eJSL_Attribute" = None, eJSL_Attribute51: "eJSL_Attribute" = None, eJSL_Attribute56: "eJSL_Reference" = None, eJSL_Attribute62: "eJSL_Reference" = None, eJSL_Attribute80: "eJSL_DynamicPage" = None, eJSL_Attribute83: "eJSL_DynamicPage" = None, eJSL_Attribute87: "eJSL_DetailPageField" = None, eJSL_Attribute101: "eJSL_Link" = None, eJSL_Attribute110: "eJSL_LinkParameter" = None):
        self.name = name
        self.preserve = preserve
        self.isunique = isunique
        self.id = id
        self.isprimary = isprimary
        self.eJSL_Attribute = eJSL_Attribute
        self.eJSL_Attribute50 = eJSL_Attribute50
        self.eJSL_Attribute53 = eJSL_Attribute53
        self.eJSL_Attribute51 = eJSL_Attribute51
        self.eJSL_Attribute56 = eJSL_Attribute56
        self.eJSL_Attribute62 = eJSL_Attribute62
        self.eJSL_Attribute80 = eJSL_Attribute80
        self.eJSL_Attribute83 = eJSL_Attribute83
        self.eJSL_Attribute87 = eJSL_Attribute87
        self.eJSL_Attribute101 = eJSL_Attribute101
        self.eJSL_Attribute110 = eJSL_Attribute110
        
    @property
    def isprimary(self) -> bool:
        return self.__isprimary

    @isprimary.setter
    def isprimary(self, isprimary: bool):
        self.__isprimary = isprimary

    @property
    def preserve(self) -> bool:
        return self.__preserve

    @preserve.setter
    def preserve(self, preserve: bool):
        self.__preserve = preserve

    @property
    def isunique(self) -> bool:
        return self.__isunique

    @isunique.setter
    def isunique(self, isunique: bool):
        self.__isunique = isunique

    @property
    def id(self) -> bool:
        return self.__id

    @id.setter
    def id(self, id: bool):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Attribute62(self):
        return self.__eJSL_Attribute62

    @eJSL_Attribute62.setter
    def eJSL_Attribute62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute62", None)
        self.__eJSL_Attribute62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Reference61"):
                opp_val = getattr(old_value, "eJSL_Reference61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Reference61"):
                opp_val = getattr(value, "eJSL_Reference61", None)
                if opp_val is None:
                    setattr(value, "eJSL_Reference61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Attribute51(self):
        return self.__eJSL_Attribute51

    @eJSL_Attribute51.setter
    def eJSL_Attribute51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute51", None)
        self.__eJSL_Attribute51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Attribute53"):
                opp_val = getattr(old_value, "eJSL_Attribute53", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Attribute53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Attribute53"):
                opp_val = getattr(value, "eJSL_Attribute53", None)
                setattr(value, "eJSL_Attribute53", self)

    @property
    def eJSL_Attribute101(self):
        return self.__eJSL_Attribute101

    @eJSL_Attribute101.setter
    def eJSL_Attribute101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute101", None)
        self.__eJSL_Attribute101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Link100"):
                opp_val = getattr(old_value, "eJSL_Link100", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Link100", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Link100"):
                opp_val = getattr(value, "eJSL_Link100", None)
                setattr(value, "eJSL_Link100", self)

    @property
    def eJSL_Attribute56(self):
        return self.__eJSL_Attribute56

    @eJSL_Attribute56.setter
    def eJSL_Attribute56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute56", None)
        self.__eJSL_Attribute56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Reference55"):
                opp_val = getattr(old_value, "eJSL_Reference55", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Reference55"):
                opp_val = getattr(value, "eJSL_Reference55", None)
                if opp_val is None:
                    setattr(value, "eJSL_Reference55", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Attribute110(self):
        return self.__eJSL_Attribute110

    @eJSL_Attribute110.setter
    def eJSL_Attribute110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute110", None)
        self.__eJSL_Attribute110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_LinkParameter109"):
                opp_val = getattr(old_value, "eJSL_LinkParameter109", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_LinkParameter109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_LinkParameter109"):
                opp_val = getattr(value, "eJSL_LinkParameter109", None)
                setattr(value, "eJSL_LinkParameter109", self)

    @property
    def eJSL_Attribute80(self):
        return self.__eJSL_Attribute80

    @eJSL_Attribute80.setter
    def eJSL_Attribute80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute80", None)
        self.__eJSL_Attribute80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_DynamicPage79"):
                opp_val = getattr(old_value, "eJSL_DynamicPage79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_DynamicPage79"):
                opp_val = getattr(value, "eJSL_DynamicPage79", None)
                if opp_val is None:
                    setattr(value, "eJSL_DynamicPage79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Attribute50(self):
        return self.__eJSL_Attribute50

    @eJSL_Attribute50.setter
    def eJSL_Attribute50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute50", None)
        self.__eJSL_Attribute50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Type"):
                opp_val = getattr(old_value, "eJSL_Type", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Type"):
                opp_val = getattr(value, "eJSL_Type", None)
                setattr(value, "eJSL_Type", self)

    @property
    def eJSL_Attribute87(self):
        return self.__eJSL_Attribute87

    @eJSL_Attribute87.setter
    def eJSL_Attribute87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute87", None)
        self.__eJSL_Attribute87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_DetailPageField86"):
                opp_val = getattr(old_value, "eJSL_DetailPageField86", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_DetailPageField86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_DetailPageField86"):
                opp_val = getattr(value, "eJSL_DetailPageField86", None)
                setattr(value, "eJSL_DetailPageField86", self)

    @property
    def eJSL_Attribute83(self):
        return self.__eJSL_Attribute83

    @eJSL_Attribute83.setter
    def eJSL_Attribute83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute83", None)
        self.__eJSL_Attribute83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_DynamicPage82"):
                opp_val = getattr(old_value, "eJSL_DynamicPage82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_DynamicPage82"):
                opp_val = getattr(value, "eJSL_DynamicPage82", None)
                if opp_val is None:
                    setattr(value, "eJSL_DynamicPage82", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Attribute53(self):
        return self.__eJSL_Attribute53

    @eJSL_Attribute53.setter
    def eJSL_Attribute53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute53", None)
        self.__eJSL_Attribute53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Attribute51"):
                opp_val = getattr(old_value, "eJSL_Attribute51", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Attribute51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Attribute51"):
                opp_val = getattr(value, "eJSL_Attribute51", None)
                setattr(value, "eJSL_Attribute51", self)

    @property
    def eJSL_Attribute(self):
        return self.__eJSL_Attribute

    @eJSL_Attribute.setter
    def eJSL_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Attribute__eJSL_Attribute", None)
        self.__eJSL_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Entity46"):
                opp_val = getattr(old_value, "eJSL_Entity46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Entity46"):
                opp_val = getattr(value, "eJSL_Entity46", None)
                if opp_val is None:
                    setattr(value, "eJSL_Entity46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Entity:

    def __init__(self, name: str, preserve: bool, eJSL_Entity: "eJSL_Feature" = None, eJSL_Entity44: "eJSL_Entity" = None, eJSL_Entity42: "eJSL_Entity" = None, eJSL_Entity46: set["eJSL_Attribute"] = None, eJSL_Entity48: set["eJSL_Reference"] = None, eJSL_Entity59: "eJSL_Reference" = None, eJSL_Entity38: "eJSL_Entitypackage" = None, eJSL_Entity77: "eJSL_DynamicPage" = None, eJSL_Entity98: "eJSL_CustomPage" = None, eJSL_Entity135: "eJSL_Plugin" = None, eJSL_Entity140: "eJSL_Library" = None, eJSL_Entity159: "eJSL_Class" = None):
        self.name = name
        self.preserve = preserve
        self.eJSL_Entity = eJSL_Entity
        self.eJSL_Entity44 = eJSL_Entity44
        self.eJSL_Entity42 = eJSL_Entity42
        self.eJSL_Entity46 = eJSL_Entity46 if eJSL_Entity46 is not None else set()
        self.eJSL_Entity48 = eJSL_Entity48 if eJSL_Entity48 is not None else set()
        self.eJSL_Entity59 = eJSL_Entity59
        self.eJSL_Entity38 = eJSL_Entity38
        self.eJSL_Entity77 = eJSL_Entity77
        self.eJSL_Entity98 = eJSL_Entity98
        self.eJSL_Entity135 = eJSL_Entity135
        self.eJSL_Entity140 = eJSL_Entity140
        self.eJSL_Entity159 = eJSL_Entity159
        
    @property
    def preserve(self) -> bool:
        return self.__preserve

    @preserve.setter
    def preserve(self, preserve: bool):
        self.__preserve = preserve

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Entity48(self):
        return self.__eJSL_Entity48

    @eJSL_Entity48.setter
    def eJSL_Entity48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity48", None)
        self.__eJSL_Entity48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Reference"):
                    opp_val = getattr(item, "eJSL_Reference", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Reference", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Reference"):
                    opp_val = getattr(item, "eJSL_Reference", None)
                    
                    setattr(item, "eJSL_Reference", self)
                    

    @property
    def eJSL_Entity159(self):
        return self.__eJSL_Entity159

    @eJSL_Entity159.setter
    def eJSL_Entity159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity159", None)
        self.__eJSL_Entity159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Class158"):
                opp_val = getattr(old_value, "eJSL_Class158", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Class158"):
                opp_val = getattr(value, "eJSL_Class158", None)
                if opp_val is None:
                    setattr(value, "eJSL_Class158", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Entity(self):
        return self.__eJSL_Entity

    @eJSL_Entity.setter
    def eJSL_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity", None)
        self.__eJSL_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Feature13"):
                opp_val = getattr(old_value, "eJSL_Feature13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Feature13"):
                opp_val = getattr(value, "eJSL_Feature13", None)
                if opp_val is None:
                    setattr(value, "eJSL_Feature13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Entity77(self):
        return self.__eJSL_Entity77

    @eJSL_Entity77.setter
    def eJSL_Entity77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity77", None)
        self.__eJSL_Entity77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_DynamicPage"):
                opp_val = getattr(old_value, "eJSL_DynamicPage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_DynamicPage"):
                opp_val = getattr(value, "eJSL_DynamicPage", None)
                if opp_val is None:
                    setattr(value, "eJSL_DynamicPage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Entity140(self):
        return self.__eJSL_Entity140

    @eJSL_Entity140.setter
    def eJSL_Entity140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity140", None)
        self.__eJSL_Entity140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Library"):
                opp_val = getattr(old_value, "eJSL_Library", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Library"):
                opp_val = getattr(value, "eJSL_Library", None)
                if opp_val is None:
                    setattr(value, "eJSL_Library", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Entity42(self):
        return self.__eJSL_Entity42

    @eJSL_Entity42.setter
    def eJSL_Entity42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity42", None)
        self.__eJSL_Entity42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Entity44"):
                opp_val = getattr(old_value, "eJSL_Entity44", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Entity44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Entity44"):
                opp_val = getattr(value, "eJSL_Entity44", None)
                setattr(value, "eJSL_Entity44", self)

    @property
    def eJSL_Entity38(self):
        return self.__eJSL_Entity38

    @eJSL_Entity38.setter
    def eJSL_Entity38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity38", None)
        self.__eJSL_Entity38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Entitypackage37"):
                opp_val = getattr(old_value, "eJSL_Entitypackage37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Entitypackage37"):
                opp_val = getattr(value, "eJSL_Entitypackage37", None)
                if opp_val is None:
                    setattr(value, "eJSL_Entitypackage37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Entity44(self):
        return self.__eJSL_Entity44

    @eJSL_Entity44.setter
    def eJSL_Entity44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity44", None)
        self.__eJSL_Entity44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Entity42"):
                opp_val = getattr(old_value, "eJSL_Entity42", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Entity42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Entity42"):
                opp_val = getattr(value, "eJSL_Entity42", None)
                setattr(value, "eJSL_Entity42", self)

    @property
    def eJSL_Entity46(self):
        return self.__eJSL_Entity46

    @eJSL_Entity46.setter
    def eJSL_Entity46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity46", None)
        self.__eJSL_Entity46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Attribute"):
                    opp_val = getattr(item, "eJSL_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Attribute"):
                    opp_val = getattr(item, "eJSL_Attribute", None)
                    
                    setattr(item, "eJSL_Attribute", self)
                    

    @property
    def eJSL_Entity135(self):
        return self.__eJSL_Entity135

    @eJSL_Entity135.setter
    def eJSL_Entity135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity135", None)
        self.__eJSL_Entity135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Plugin"):
                opp_val = getattr(old_value, "eJSL_Plugin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Plugin"):
                opp_val = getattr(value, "eJSL_Plugin", None)
                if opp_val is None:
                    setattr(value, "eJSL_Plugin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Entity59(self):
        return self.__eJSL_Entity59

    @eJSL_Entity59.setter
    def eJSL_Entity59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity59", None)
        self.__eJSL_Entity59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Reference58"):
                opp_val = getattr(old_value, "eJSL_Reference58", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Reference58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Reference58"):
                opp_val = getattr(value, "eJSL_Reference58", None)
                setattr(value, "eJSL_Reference58", self)

    @property
    def eJSL_Entity98(self):
        return self.__eJSL_Entity98

    @eJSL_Entity98.setter
    def eJSL_Entity98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entity__eJSL_Entity98", None)
        self.__eJSL_Entity98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_CustomPage"):
                opp_val = getattr(old_value, "eJSL_CustomPage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_CustomPage"):
                opp_val = getattr(value, "eJSL_CustomPage", None)
                if opp_val is None:
                    setattr(value, "eJSL_CustomPage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Entitypackage:

    def __init__(self, name: str, eJSL_Entitypackage: "eJSL_Feature" = None, eJSL_Entitypackage37: set["eJSL_Entity"] = None, eJSL_Entitypackage40: set["eJSL_Datatype"] = None, eJSL_Entitypackage35: "eJSL_Entitypackage" = None, eJSL_Entitypackage33: set["eJSL_Entitypackage"] = None):
        self.name = name
        self.eJSL_Entitypackage = eJSL_Entitypackage
        self.eJSL_Entitypackage37 = eJSL_Entitypackage37 if eJSL_Entitypackage37 is not None else set()
        self.eJSL_Entitypackage40 = eJSL_Entitypackage40 if eJSL_Entitypackage40 is not None else set()
        self.eJSL_Entitypackage35 = eJSL_Entitypackage35
        self.eJSL_Entitypackage33 = eJSL_Entitypackage33 if eJSL_Entitypackage33 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Entitypackage37(self):
        return self.__eJSL_Entitypackage37

    @eJSL_Entitypackage37.setter
    def eJSL_Entitypackage37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entitypackage__eJSL_Entitypackage37", None)
        self.__eJSL_Entitypackage37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Entity38"):
                    opp_val = getattr(item, "eJSL_Entity38", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Entity38", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Entity38"):
                    opp_val = getattr(item, "eJSL_Entity38", None)
                    
                    setattr(item, "eJSL_Entity38", self)
                    

    @property
    def eJSL_Entitypackage33(self):
        return self.__eJSL_Entitypackage33

    @eJSL_Entitypackage33.setter
    def eJSL_Entitypackage33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entitypackage__eJSL_Entitypackage33", None)
        self.__eJSL_Entitypackage33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Entitypackage35"):
                    opp_val = getattr(item, "eJSL_Entitypackage35", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Entitypackage35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Entitypackage35"):
                    opp_val = getattr(item, "eJSL_Entitypackage35", None)
                    
                    setattr(item, "eJSL_Entitypackage35", self)
                    

    @property
    def eJSL_Entitypackage40(self):
        return self.__eJSL_Entitypackage40

    @eJSL_Entitypackage40.setter
    def eJSL_Entitypackage40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entitypackage__eJSL_Entitypackage40", None)
        self.__eJSL_Entitypackage40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Datatype41"):
                    opp_val = getattr(item, "eJSL_Datatype41", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Datatype41", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Datatype41"):
                    opp_val = getattr(item, "eJSL_Datatype41", None)
                    
                    setattr(item, "eJSL_Datatype41", self)
                    

    @property
    def eJSL_Entitypackage(self):
        return self.__eJSL_Entitypackage

    @eJSL_Entitypackage.setter
    def eJSL_Entitypackage(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entitypackage__eJSL_Entitypackage", None)
        self.__eJSL_Entitypackage = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Feature11"):
                opp_val = getattr(old_value, "eJSL_Feature11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Feature11"):
                opp_val = getattr(value, "eJSL_Feature11", None)
                if opp_val is None:
                    setattr(value, "eJSL_Feature11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Entitypackage35(self):
        return self.__eJSL_Entitypackage35

    @eJSL_Entitypackage35.setter
    def eJSL_Entitypackage35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Entitypackage__eJSL_Entitypackage35", None)
        self.__eJSL_Entitypackage35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Entitypackage33"):
                opp_val = getattr(old_value, "eJSL_Entitypackage33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Entitypackage33"):
                opp_val = getattr(value, "eJSL_Entitypackage33", None)
                if opp_val is None:
                    setattr(value, "eJSL_Entitypackage33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Extension:

    def __init__(self, name: str, eJSL_Extension: "eJSL_CMSExtension" = None, eJSL_Extension112: "eJSL_Manifestation" = None, eJSL_Extension114: set["eJSL_Language"] = None, eJSL_Extension116: "eJSL_ExtensionPackage" = None):
        self.name = name
        self.eJSL_Extension = eJSL_Extension
        self.eJSL_Extension112 = eJSL_Extension112
        self.eJSL_Extension114 = eJSL_Extension114 if eJSL_Extension114 is not None else set()
        self.eJSL_Extension116 = eJSL_Extension116
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Extension114(self):
        return self.__eJSL_Extension114

    @eJSL_Extension114.setter
    def eJSL_Extension114(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Extension__eJSL_Extension114", None)
        self.__eJSL_Extension114 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Language"):
                    opp_val = getattr(item, "eJSL_Language", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Language", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Language"):
                    opp_val = getattr(item, "eJSL_Language", None)
                    
                    setattr(item, "eJSL_Language", self)
                    

    @property
    def eJSL_Extension116(self):
        return self.__eJSL_Extension116

    @eJSL_Extension116.setter
    def eJSL_Extension116(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Extension__eJSL_Extension116", None)
        self.__eJSL_Extension116 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_ExtensionPackage"):
                opp_val = getattr(old_value, "eJSL_ExtensionPackage", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_ExtensionPackage"):
                opp_val = getattr(value, "eJSL_ExtensionPackage", None)
                if opp_val is None:
                    setattr(value, "eJSL_ExtensionPackage", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Extension112(self):
        return self.__eJSL_Extension112

    @eJSL_Extension112.setter
    def eJSL_Extension112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Extension__eJSL_Extension112", None)
        self.__eJSL_Extension112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Manifestation"):
                opp_val = getattr(old_value, "eJSL_Manifestation", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_Manifestation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Manifestation"):
                opp_val = getattr(value, "eJSL_Manifestation", None)
                setattr(value, "eJSL_Manifestation", self)

    @property
    def eJSL_Extension(self):
        return self.__eJSL_Extension

    @eJSL_Extension.setter
    def eJSL_Extension(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Extension__eJSL_Extension", None)
        self.__eJSL_Extension = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_CMSExtension"):
                opp_val = getattr(old_value, "eJSL_CMSExtension", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_CMSExtension"):
                opp_val = getattr(value, "eJSL_CMSExtension", None)
                if opp_val is None:
                    setattr(value, "eJSL_CMSExtension", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_coreFeature:

    pass
class EJSLPart:

    pass
class eJSL_CMSExtension(EJSLPart):

    pass
class eJSL_KeyValuePair:

    def __init__(self, name: str, value: str, eJSL_KeyValuePair: "eJSL_Parameter" = None, eJSL_KeyValuePair26: "eJSL_Parameter" = None, eJSL_KeyValuePair93: "eJSL_DetailPageField" = None, eJSL_KeyValuePair96: "eJSL_DetailPageField" = None, eJSL_KeyValuePair180: "eJSL_Language" = None, eJSL_KeyValuePair185: "eJSL_PositionParameter" = None, eJSL_KeyValuePair188: "eJSL_CssBlock" = None):
        self.name = name
        self.value = value
        self.eJSL_KeyValuePair = eJSL_KeyValuePair
        self.eJSL_KeyValuePair26 = eJSL_KeyValuePair26
        self.eJSL_KeyValuePair93 = eJSL_KeyValuePair93
        self.eJSL_KeyValuePair96 = eJSL_KeyValuePair96
        self.eJSL_KeyValuePair180 = eJSL_KeyValuePair180
        self.eJSL_KeyValuePair185 = eJSL_KeyValuePair185
        self.eJSL_KeyValuePair188 = eJSL_KeyValuePair188
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_KeyValuePair93(self):
        return self.__eJSL_KeyValuePair93

    @eJSL_KeyValuePair93.setter
    def eJSL_KeyValuePair93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_KeyValuePair__eJSL_KeyValuePair93", None)
        self.__eJSL_KeyValuePair93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_DetailPageField92"):
                opp_val = getattr(old_value, "eJSL_DetailPageField92", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_DetailPageField92"):
                opp_val = getattr(value, "eJSL_DetailPageField92", None)
                if opp_val is None:
                    setattr(value, "eJSL_DetailPageField92", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_KeyValuePair180(self):
        return self.__eJSL_KeyValuePair180

    @eJSL_KeyValuePair180.setter
    def eJSL_KeyValuePair180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_KeyValuePair__eJSL_KeyValuePair180", None)
        self.__eJSL_KeyValuePair180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Language179"):
                opp_val = getattr(old_value, "eJSL_Language179", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Language179"):
                opp_val = getattr(value, "eJSL_Language179", None)
                if opp_val is None:
                    setattr(value, "eJSL_Language179", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_KeyValuePair96(self):
        return self.__eJSL_KeyValuePair96

    @eJSL_KeyValuePair96.setter
    def eJSL_KeyValuePair96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_KeyValuePair__eJSL_KeyValuePair96", None)
        self.__eJSL_KeyValuePair96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_DetailPageField95"):
                opp_val = getattr(old_value, "eJSL_DetailPageField95", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_DetailPageField95"):
                opp_val = getattr(value, "eJSL_DetailPageField95", None)
                if opp_val is None:
                    setattr(value, "eJSL_DetailPageField95", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_KeyValuePair188(self):
        return self.__eJSL_KeyValuePair188

    @eJSL_KeyValuePair188.setter
    def eJSL_KeyValuePair188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_KeyValuePair__eJSL_KeyValuePair188", None)
        self.__eJSL_KeyValuePair188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_CssBlock187"):
                opp_val = getattr(old_value, "eJSL_CssBlock187", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_CssBlock187"):
                opp_val = getattr(value, "eJSL_CssBlock187", None)
                if opp_val is None:
                    setattr(value, "eJSL_CssBlock187", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_KeyValuePair185(self):
        return self.__eJSL_KeyValuePair185

    @eJSL_KeyValuePair185.setter
    def eJSL_KeyValuePair185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_KeyValuePair__eJSL_KeyValuePair185", None)
        self.__eJSL_KeyValuePair185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_PositionParameter184"):
                opp_val = getattr(old_value, "eJSL_PositionParameter184", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_PositionParameter184"):
                opp_val = getattr(value, "eJSL_PositionParameter184", None)
                if opp_val is None:
                    setattr(value, "eJSL_PositionParameter184", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_KeyValuePair26(self):
        return self.__eJSL_KeyValuePair26

    @eJSL_KeyValuePair26.setter
    def eJSL_KeyValuePair26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_KeyValuePair__eJSL_KeyValuePair26", None)
        self.__eJSL_KeyValuePair26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Parameter25"):
                opp_val = getattr(old_value, "eJSL_Parameter25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Parameter25"):
                opp_val = getattr(value, "eJSL_Parameter25", None)
                if opp_val is None:
                    setattr(value, "eJSL_Parameter25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_KeyValuePair(self):
        return self.__eJSL_KeyValuePair

    @eJSL_KeyValuePair.setter
    def eJSL_KeyValuePair(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_KeyValuePair__eJSL_KeyValuePair", None)
        self.__eJSL_KeyValuePair = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Parameter23"):
                opp_val = getattr(old_value, "eJSL_Parameter23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Parameter23"):
                opp_val = getattr(value, "eJSL_Parameter23", None)
                if opp_val is None:
                    setattr(value, "eJSL_Parameter23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_HTMLTypes:

    pass
class HTMLTypes:

    pass
class eJSL_SimpleHTMLTypes(HTMLTypes):

    def __init__(self, htmltype: str):
        self.htmltype = htmltype
        
    @property
    def htmltype(self) -> str:
        return self.__htmltype

    @htmltype.setter
    def htmltype(self, htmltype: str):
        self.__htmltype = htmltype

class eJSL_ComplexHTMLTypes(HTMLTypes):

    def __init__(self, htmltype: str):
        self.htmltype = htmltype
        
    @property
    def htmltype(self) -> str:
        return self.__htmltype

    @htmltype.setter
    def htmltype(self, htmltype: str):
        self.__htmltype = htmltype

class Type:

    pass
class eJSL_StandardTypes(Type):

    def __init__(self, type: str, notnull: bool, default: str, autoincrement: bool):
        self.type = type
        self.notnull = notnull
        self.default = default
        self.autoincrement = autoincrement
        
    @property
    def notnull(self) -> bool:
        return self.__notnull

    @notnull.setter
    def notnull(self, notnull: bool):
        self.__notnull = notnull

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def default(self) -> str:
        return self.__default

    @default.setter
    def default(self, default: str):
        self.__default = default

    @property
    def autoincrement(self) -> bool:
        return self.__autoincrement

    @autoincrement.setter
    def autoincrement(self, autoincrement: bool):
        self.__autoincrement = autoincrement

class eJSL_DatatypeReference(Type, HTMLTypes):

    pass
class eJSL_Type:

    pass
class eJSL_Section:

    pass
class eJSL_Page:

    def __init__(self, name: str, eJSL_Page: "eJSL_Feature" = None, eJSL_Page64: set["eJSL_ParameterGroup"] = None, eJSL_Page67: set["eJSL_Parameter"] = None, eJSL_Page75: set["eJSL_Link"] = None, eJSL_Page70: set["eJSL_Parameter"] = None, eJSL_Page73: set["eJSL_PageAction"] = None, eJSL_Page106: "eJSL_InternalLink" = None, eJSL_Page126: "eJSL_PageReference" = None):
        self.name = name
        self.eJSL_Page = eJSL_Page
        self.eJSL_Page64 = eJSL_Page64 if eJSL_Page64 is not None else set()
        self.eJSL_Page67 = eJSL_Page67 if eJSL_Page67 is not None else set()
        self.eJSL_Page75 = eJSL_Page75 if eJSL_Page75 is not None else set()
        self.eJSL_Page70 = eJSL_Page70 if eJSL_Page70 is not None else set()
        self.eJSL_Page73 = eJSL_Page73 if eJSL_Page73 is not None else set()
        self.eJSL_Page106 = eJSL_Page106
        self.eJSL_Page126 = eJSL_Page126
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_Page67(self):
        return self.__eJSL_Page67

    @eJSL_Page67.setter
    def eJSL_Page67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Page__eJSL_Page67", None)
        self.__eJSL_Page67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Parameter68"):
                    opp_val = getattr(item, "eJSL_Parameter68", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Parameter68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Parameter68"):
                    opp_val = getattr(item, "eJSL_Parameter68", None)
                    
                    setattr(item, "eJSL_Parameter68", self)
                    

    @property
    def eJSL_Page70(self):
        return self.__eJSL_Page70

    @eJSL_Page70.setter
    def eJSL_Page70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Page__eJSL_Page70", None)
        self.__eJSL_Page70 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Parameter71"):
                    opp_val = getattr(item, "eJSL_Parameter71", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Parameter71", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Parameter71"):
                    opp_val = getattr(item, "eJSL_Parameter71", None)
                    
                    setattr(item, "eJSL_Parameter71", self)
                    

    @property
    def eJSL_Page126(self):
        return self.__eJSL_Page126

    @eJSL_Page126.setter
    def eJSL_Page126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Page__eJSL_Page126", None)
        self.__eJSL_Page126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_PageReference125"):
                opp_val = getattr(old_value, "eJSL_PageReference125", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_PageReference125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_PageReference125"):
                opp_val = getattr(value, "eJSL_PageReference125", None)
                setattr(value, "eJSL_PageReference125", self)

    @property
    def eJSL_Page75(self):
        return self.__eJSL_Page75

    @eJSL_Page75.setter
    def eJSL_Page75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Page__eJSL_Page75", None)
        self.__eJSL_Page75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Link"):
                    opp_val = getattr(item, "eJSL_Link", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Link", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Link"):
                    opp_val = getattr(item, "eJSL_Link", None)
                    
                    setattr(item, "eJSL_Link", self)
                    

    @property
    def eJSL_Page106(self):
        return self.__eJSL_Page106

    @eJSL_Page106.setter
    def eJSL_Page106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Page__eJSL_Page106", None)
        self.__eJSL_Page106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_InternalLink"):
                opp_val = getattr(old_value, "eJSL_InternalLink", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_InternalLink", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_InternalLink"):
                opp_val = getattr(value, "eJSL_InternalLink", None)
                setattr(value, "eJSL_InternalLink", self)

    @property
    def eJSL_Page73(self):
        return self.__eJSL_Page73

    @eJSL_Page73.setter
    def eJSL_Page73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Page__eJSL_Page73", None)
        self.__eJSL_Page73 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_PageAction"):
                    opp_val = getattr(item, "eJSL_PageAction", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_PageAction", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_PageAction"):
                    opp_val = getattr(item, "eJSL_PageAction", None)
                    
                    setattr(item, "eJSL_PageAction", self)
                    

    @property
    def eJSL_Page(self):
        return self.__eJSL_Page

    @eJSL_Page.setter
    def eJSL_Page(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Page__eJSL_Page", None)
        self.__eJSL_Page = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Feature15"):
                opp_val = getattr(old_value, "eJSL_Feature15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Feature15"):
                opp_val = getattr(value, "eJSL_Feature15", None)
                if opp_val is None:
                    setattr(value, "eJSL_Feature15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Page64(self):
        return self.__eJSL_Page64

    @eJSL_Page64.setter
    def eJSL_Page64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Page__eJSL_Page64", None)
        self.__eJSL_Page64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_ParameterGroup65"):
                    opp_val = getattr(item, "eJSL_ParameterGroup65", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_ParameterGroup65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_ParameterGroup65"):
                    opp_val = getattr(item, "eJSL_ParameterGroup65", None)
                    
                    setattr(item, "eJSL_ParameterGroup65", self)
                    

class eJSL_CMSCore(EJSLPart):

    pass
class eJSL_Feature:

    pass
class eJSL_ParameterGroup:

    def __init__(self, name: str, label: str, eJSL_ParameterGroup: "eJSL_EJSLPart" = None, eJSL_ParameterGroup28: set["eJSL_Parameter"] = None, eJSL_ParameterGroup31: set["eJSL_Parameter"] = None, eJSL_ParameterGroup65: "eJSL_Page" = None, eJSL_ParameterGroup118: "eJSL_Component" = None):
        self.name = name
        self.label = label
        self.eJSL_ParameterGroup = eJSL_ParameterGroup
        self.eJSL_ParameterGroup28 = eJSL_ParameterGroup28 if eJSL_ParameterGroup28 is not None else set()
        self.eJSL_ParameterGroup31 = eJSL_ParameterGroup31 if eJSL_ParameterGroup31 is not None else set()
        self.eJSL_ParameterGroup65 = eJSL_ParameterGroup65
        self.eJSL_ParameterGroup118 = eJSL_ParameterGroup118
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_ParameterGroup31(self):
        return self.__eJSL_ParameterGroup31

    @eJSL_ParameterGroup31.setter
    def eJSL_ParameterGroup31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_ParameterGroup__eJSL_ParameterGroup31", None)
        self.__eJSL_ParameterGroup31 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Parameter32"):
                    opp_val = getattr(item, "eJSL_Parameter32", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Parameter32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Parameter32"):
                    opp_val = getattr(item, "eJSL_Parameter32", None)
                    
                    setattr(item, "eJSL_Parameter32", self)
                    

    @property
    def eJSL_ParameterGroup28(self):
        return self.__eJSL_ParameterGroup28

    @eJSL_ParameterGroup28.setter
    def eJSL_ParameterGroup28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_ParameterGroup__eJSL_ParameterGroup28", None)
        self.__eJSL_ParameterGroup28 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_Parameter29"):
                    opp_val = getattr(item, "eJSL_Parameter29", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_Parameter29", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_Parameter29"):
                    opp_val = getattr(item, "eJSL_Parameter29", None)
                    
                    setattr(item, "eJSL_Parameter29", self)
                    

    @property
    def eJSL_ParameterGroup118(self):
        return self.__eJSL_ParameterGroup118

    @eJSL_ParameterGroup118.setter
    def eJSL_ParameterGroup118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_ParameterGroup__eJSL_ParameterGroup118", None)
        self.__eJSL_ParameterGroup118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Component"):
                opp_val = getattr(old_value, "eJSL_Component", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Component"):
                opp_val = getattr(value, "eJSL_Component", None)
                if opp_val is None:
                    setattr(value, "eJSL_Component", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_ParameterGroup(self):
        return self.__eJSL_ParameterGroup

    @eJSL_ParameterGroup.setter
    def eJSL_ParameterGroup(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_ParameterGroup__eJSL_ParameterGroup", None)
        self.__eJSL_ParameterGroup = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_EJSLPart6"):
                opp_val = getattr(old_value, "eJSL_EJSLPart6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_EJSLPart6"):
                opp_val = getattr(value, "eJSL_EJSLPart6", None)
                if opp_val is None:
                    setattr(value, "eJSL_EJSLPart6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_ParameterGroup65(self):
        return self.__eJSL_ParameterGroup65

    @eJSL_ParameterGroup65.setter
    def eJSL_ParameterGroup65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_ParameterGroup__eJSL_ParameterGroup65", None)
        self.__eJSL_ParameterGroup65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Page64"):
                opp_val = getattr(old_value, "eJSL_Page64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Page64"):
                opp_val = getattr(value, "eJSL_Page64", None)
                if opp_val is None:
                    setattr(value, "eJSL_Page64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Parameter:

    def __init__(self, name: str, defaultvalue: str, label: str, size: int, descripton: str, eJSL_Parameter: "eJSL_EJSLPart" = None, eJSL_Parameter21: "eJSL_HTMLTypes" = None, eJSL_Parameter23: set["eJSL_KeyValuePair"] = None, eJSL_Parameter25: set["eJSL_KeyValuePair"] = None, eJSL_Parameter29: "eJSL_ParameterGroup" = None, eJSL_Parameter32: "eJSL_ParameterGroup" = None, eJSL_Parameter68: "eJSL_Page" = None, eJSL_Parameter71: "eJSL_Page" = None, eJSL_Parameter138: "eJSL_Plugin" = None, eJSL_Parameter171: "eJSL_Template" = None):
        self.name = name
        self.defaultvalue = defaultvalue
        self.label = label
        self.size = size
        self.descripton = descripton
        self.eJSL_Parameter = eJSL_Parameter
        self.eJSL_Parameter21 = eJSL_Parameter21
        self.eJSL_Parameter23 = eJSL_Parameter23 if eJSL_Parameter23 is not None else set()
        self.eJSL_Parameter25 = eJSL_Parameter25 if eJSL_Parameter25 is not None else set()
        self.eJSL_Parameter29 = eJSL_Parameter29
        self.eJSL_Parameter32 = eJSL_Parameter32
        self.eJSL_Parameter68 = eJSL_Parameter68
        self.eJSL_Parameter71 = eJSL_Parameter71
        self.eJSL_Parameter138 = eJSL_Parameter138
        self.eJSL_Parameter171 = eJSL_Parameter171
        
    @property
    def size(self) -> int:
        return self.__size

    @size.setter
    def size(self, size: int):
        self.__size = size

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def defaultvalue(self) -> str:
        return self.__defaultvalue

    @defaultvalue.setter
    def defaultvalue(self, defaultvalue: str):
        self.__defaultvalue = defaultvalue

    @property
    def descripton(self) -> str:
        return self.__descripton

    @descripton.setter
    def descripton(self, descripton: str):
        self.__descripton = descripton

    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def eJSL_Parameter(self):
        return self.__eJSL_Parameter

    @eJSL_Parameter.setter
    def eJSL_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter", None)
        self.__eJSL_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_EJSLPart4"):
                opp_val = getattr(old_value, "eJSL_EJSLPart4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_EJSLPart4"):
                opp_val = getattr(value, "eJSL_EJSLPart4", None)
                if opp_val is None:
                    setattr(value, "eJSL_EJSLPart4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Parameter68(self):
        return self.__eJSL_Parameter68

    @eJSL_Parameter68.setter
    def eJSL_Parameter68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter68", None)
        self.__eJSL_Parameter68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Page67"):
                opp_val = getattr(old_value, "eJSL_Page67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Page67"):
                opp_val = getattr(value, "eJSL_Page67", None)
                if opp_val is None:
                    setattr(value, "eJSL_Page67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Parameter32(self):
        return self.__eJSL_Parameter32

    @eJSL_Parameter32.setter
    def eJSL_Parameter32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter32", None)
        self.__eJSL_Parameter32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_ParameterGroup31"):
                opp_val = getattr(old_value, "eJSL_ParameterGroup31", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_ParameterGroup31"):
                opp_val = getattr(value, "eJSL_ParameterGroup31", None)
                if opp_val is None:
                    setattr(value, "eJSL_ParameterGroup31", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Parameter23(self):
        return self.__eJSL_Parameter23

    @eJSL_Parameter23.setter
    def eJSL_Parameter23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter23", None)
        self.__eJSL_Parameter23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_KeyValuePair"):
                    opp_val = getattr(item, "eJSL_KeyValuePair", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_KeyValuePair", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_KeyValuePair"):
                    opp_val = getattr(item, "eJSL_KeyValuePair", None)
                    
                    setattr(item, "eJSL_KeyValuePair", self)
                    

    @property
    def eJSL_Parameter171(self):
        return self.__eJSL_Parameter171

    @eJSL_Parameter171.setter
    def eJSL_Parameter171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter171", None)
        self.__eJSL_Parameter171 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Template"):
                opp_val = getattr(old_value, "eJSL_Template", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Template"):
                opp_val = getattr(value, "eJSL_Template", None)
                if opp_val is None:
                    setattr(value, "eJSL_Template", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Parameter138(self):
        return self.__eJSL_Parameter138

    @eJSL_Parameter138.setter
    def eJSL_Parameter138(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter138", None)
        self.__eJSL_Parameter138 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Plugin137"):
                opp_val = getattr(old_value, "eJSL_Plugin137", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Plugin137"):
                opp_val = getattr(value, "eJSL_Plugin137", None)
                if opp_val is None:
                    setattr(value, "eJSL_Plugin137", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Parameter29(self):
        return self.__eJSL_Parameter29

    @eJSL_Parameter29.setter
    def eJSL_Parameter29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter29", None)
        self.__eJSL_Parameter29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_ParameterGroup28"):
                opp_val = getattr(old_value, "eJSL_ParameterGroup28", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_ParameterGroup28"):
                opp_val = getattr(value, "eJSL_ParameterGroup28", None)
                if opp_val is None:
                    setattr(value, "eJSL_ParameterGroup28", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Parameter21(self):
        return self.__eJSL_Parameter21

    @eJSL_Parameter21.setter
    def eJSL_Parameter21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter21", None)
        self.__eJSL_Parameter21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_HTMLTypes"):
                opp_val = getattr(old_value, "eJSL_HTMLTypes", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_HTMLTypes", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_HTMLTypes"):
                opp_val = getattr(value, "eJSL_HTMLTypes", None)
                setattr(value, "eJSL_HTMLTypes", self)

    @property
    def eJSL_Parameter25(self):
        return self.__eJSL_Parameter25

    @eJSL_Parameter25.setter
    def eJSL_Parameter25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter25", None)
        self.__eJSL_Parameter25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "eJSL_KeyValuePair26"):
                    opp_val = getattr(item, "eJSL_KeyValuePair26", None)
                    
                    if opp_val == self:
                        setattr(item, "eJSL_KeyValuePair26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "eJSL_KeyValuePair26"):
                    opp_val = getattr(item, "eJSL_KeyValuePair26", None)
                    
                    setattr(item, "eJSL_KeyValuePair26", self)
                    

    @property
    def eJSL_Parameter71(self):
        return self.__eJSL_Parameter71

    @eJSL_Parameter71.setter
    def eJSL_Parameter71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Parameter__eJSL_Parameter71", None)
        self.__eJSL_Parameter71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Page70"):
                opp_val = getattr(old_value, "eJSL_Page70", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Page70"):
                opp_val = getattr(value, "eJSL_Page70", None)
                if opp_val is None:
                    setattr(value, "eJSL_Page70", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_Datatype:

    def __init__(self, name: str, type: str, eJSL_Datatype: "eJSL_EJSLPart" = None, eJSL_Datatype19: "eJSL_DatatypeReference" = None, eJSL_Datatype41: "eJSL_Entitypackage" = None):
        self.name = name
        self.type = type
        self.eJSL_Datatype = eJSL_Datatype
        self.eJSL_Datatype19 = eJSL_Datatype19
        self.eJSL_Datatype41 = eJSL_Datatype41
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def eJSL_Datatype19(self):
        return self.__eJSL_Datatype19

    @eJSL_Datatype19.setter
    def eJSL_Datatype19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Datatype__eJSL_Datatype19", None)
        self.__eJSL_Datatype19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_DatatypeReference"):
                opp_val = getattr(old_value, "eJSL_DatatypeReference", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_DatatypeReference", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_DatatypeReference"):
                opp_val = getattr(value, "eJSL_DatatypeReference", None)
                setattr(value, "eJSL_DatatypeReference", self)

    @property
    def eJSL_Datatype(self):
        return self.__eJSL_Datatype

    @eJSL_Datatype.setter
    def eJSL_Datatype(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Datatype__eJSL_Datatype", None)
        self.__eJSL_Datatype = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_EJSLPart2"):
                opp_val = getattr(old_value, "eJSL_EJSLPart2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_EJSLPart2"):
                opp_val = getattr(value, "eJSL_EJSLPart2", None)
                if opp_val is None:
                    setattr(value, "eJSL_EJSLPart2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def eJSL_Datatype41(self):
        return self.__eJSL_Datatype41

    @eJSL_Datatype41.setter
    def eJSL_Datatype41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_Datatype__eJSL_Datatype41", None)
        self.__eJSL_Datatype41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_Entitypackage40"):
                opp_val = getattr(old_value, "eJSL_Entitypackage40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_Entitypackage40"):
                opp_val = getattr(value, "eJSL_Entitypackage40", None)
                if opp_val is None:
                    setattr(value, "eJSL_Entitypackage40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class eJSL_EJSLPart:

    pass
class eJSL_EJSLModel:

    def __init__(self, name: str, eJSL_EJSLModel: "eJSL_EJSLPart" = None):
        self.name = name
        self.eJSL_EJSLModel = eJSL_EJSLModel
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def eJSL_EJSLModel(self):
        return self.__eJSL_EJSLModel

    @eJSL_EJSLModel.setter
    def eJSL_EJSLModel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_eJSL_EJSLModel__eJSL_EJSLModel", None)
        self.__eJSL_EJSLModel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "eJSL_EJSLPart"):
                opp_val = getattr(old_value, "eJSL_EJSLPart", None)
                if opp_val == self:
                    setattr(old_value, "eJSL_EJSLPart", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "eJSL_EJSLPart"):
                opp_val = getattr(value, "eJSL_EJSLPart", None)
                setattr(value, "eJSL_EJSLPart", self)
