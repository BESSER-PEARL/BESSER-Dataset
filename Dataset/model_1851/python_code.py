from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class message_Language:

    def __init__(self, defaultLang: bool, uid: str, lang: str, code: str, message_Language: "message_Translation" = None):
        self.defaultLang = defaultLang
        self.uid = uid
        self.lang = lang
        self.code = code
        self.message_Language = message_Language
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def defaultLang(self) -> bool:
        return self.__defaultLang

    @defaultLang.setter
    def defaultLang(self, defaultLang: bool):
        self.__defaultLang = defaultLang

    @property
    def code(self) -> str:
        return self.__code

    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def lang(self) -> str:
        return self.__lang

    @lang.setter
    def lang(self, lang: str):
        self.__lang = lang

    @property
    def message_Language(self):
        return self.__message_Language

    @message_Language.setter
    def message_Language(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_message_Language__message_Language", None)
        self.__message_Language = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message_Translation4"):
                opp_val = getattr(old_value, "message_Translation4", None)
                if opp_val == self:
                    setattr(old_value, "message_Translation4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message_Translation4"):
                opp_val = getattr(value, "message_Translation4", None)
                setattr(value, "message_Translation4", self)

class Categorized:

    pass
class message_MessageLibrary(Categorized):

    def __init__(self, name: str, uid: str, message_MessageLibrary: set["message_Message"] = None):
        self.name = name
        self.uid = uid
        self.message_MessageLibrary = message_MessageLibrary if message_MessageLibrary is not None else set()
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def message_MessageLibrary(self):
        return self.__message_MessageLibrary

    @message_MessageLibrary.setter
    def message_MessageLibrary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_message_MessageLibrary__message_MessageLibrary", None)
        self.__message_MessageLibrary = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "message_Message"):
                    opp_val = getattr(item, "message_Message", None)
                    
                    if opp_val == self:
                        setattr(item, "message_Message", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "message_Message"):
                    opp_val = getattr(item, "message_Message", None)
                    
                    setattr(item, "message_Message", self)
                    

class message_Translation:

    def __init__(self, uid: str, translation: str, message_Translation: "message_Message" = None, message_Translation4: "message_Language" = None):
        self.uid = uid
        self.translation = translation
        self.message_Translation = message_Translation
        self.message_Translation4 = message_Translation4
        
    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def translation(self) -> str:
        return self.__translation

    @translation.setter
    def translation(self, translation: str):
        self.__translation = translation

    @property
    def message_Translation4(self):
        return self.__message_Translation4

    @message_Translation4.setter
    def message_Translation4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_message_Translation__message_Translation4", None)
        self.__message_Translation4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message_Language"):
                opp_val = getattr(old_value, "message_Language", None)
                if opp_val == self:
                    setattr(old_value, "message_Language", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message_Language"):
                opp_val = getattr(value, "message_Language", None)
                setattr(value, "message_Language", self)

    @property
    def message_Translation(self):
        return self.__message_Translation

    @message_Translation.setter
    def message_Translation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_message_Translation__message_Translation", None)
        self.__message_Translation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message_Message2"):
                opp_val = getattr(old_value, "message_Message2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message_Message2"):
                opp_val = getattr(value, "message_Message2", None)
                if opp_val is None:
                    setattr(value, "message_Message2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class message_Message:

    def __init__(self, uid: str, name: str, message_Message: "message_MessageLibrary" = None, message_Message2: set["message_Translation"] = None):
        self.uid = uid
        self.name = name
        self.message_Message = message_Message
        self.message_Message2 = message_Message2 if message_Message2 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def uid(self) -> str:
        return self.__uid

    @uid.setter
    def uid(self, uid: str):
        self.__uid = uid

    @property
    def message_Message2(self):
        return self.__message_Message2

    @message_Message2.setter
    def message_Message2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_message_Message__message_Message2", None)
        self.__message_Message2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "message_Translation"):
                    opp_val = getattr(item, "message_Translation", None)
                    
                    if opp_val == self:
                        setattr(item, "message_Translation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "message_Translation"):
                    opp_val = getattr(item, "message_Translation", None)
                    
                    setattr(item, "message_Translation", self)
                    

    @property
    def message_Message(self):
        return self.__message_Message

    @message_Message.setter
    def message_Message(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_message_Message__message_Message", None)
        self.__message_Message = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "message_MessageLibrary"):
                opp_val = getattr(old_value, "message_MessageLibrary", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "message_MessageLibrary"):
                opp_val = getattr(value, "message_MessageLibrary", None)
                if opp_val is None:
                    setattr(value, "message_MessageLibrary", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
