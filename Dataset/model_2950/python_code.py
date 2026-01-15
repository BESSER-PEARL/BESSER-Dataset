from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class metamodeloArquitecturaPila_FunctionBody:

    def __init__(self, content: str, metamodeloArquitecturaPila_FunctionBody: "metamodeloArquitecturaPila_Function" = None):
        self.content = content
        self.metamodeloArquitecturaPila_FunctionBody = metamodeloArquitecturaPila_FunctionBody
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def metamodeloArquitecturaPila_FunctionBody(self):
        return self.__metamodeloArquitecturaPila_FunctionBody

    @metamodeloArquitecturaPila_FunctionBody.setter
    def metamodeloArquitecturaPila_FunctionBody(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_FunctionBody__metamodeloArquitecturaPila_FunctionBody", None)
        self.__metamodeloArquitecturaPila_FunctionBody = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Function73"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Function73", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Function73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Function73"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Function73", None)
                setattr(value, "metamodeloArquitecturaPila_Function73", self)

class ServiceType:

    pass
class metamodeloArquitecturaPila_Read(ServiceType):

    pass
class metamodeloArquitecturaPila_Update(ServiceType):

    pass
class metamodeloArquitecturaPila_Delete(ServiceType):

    pass
class metamodeloArquitecturaPila_Create(ServiceType):

    pass
class Input:

    pass
class metamodeloArquitecturaPila_DatePicker(Input):

    pass
class metamodeloArquitecturaPila_Check(Input):

    pass
class metamodeloArquitecturaPila_Number(Input):

    pass
class metamodeloArquitecturaPila_Radio(Input):

    pass
class metamodeloArquitecturaPila_Text(Input):

    pass
class DataType:

    pass
class metamodeloArquitecturaPila_String(DataType):

    pass
class metamodeloArquitecturaPila_Enum(DataType):

    pass
class metamodeloArquitecturaPila_Date(DataType):

    pass
class metamodeloArquitecturaPila_Float(DataType):

    pass
class metamodeloArquitecturaPila_Boolean(DataType):

    pass
class metamodeloArquitecturaPila_Integer(DataType):

    pass
class metamodeloArquitecturaPila_Body:

    def __init__(self, content: str, metamodeloArquitecturaPila_Body: "metamodeloArquitecturaPila_Method" = None):
        self.content = content
        self.metamodeloArquitecturaPila_Body = metamodeloArquitecturaPila_Body
        
    @property
    def content(self) -> str:
        return self.__content

    @content.setter
    def content(self, content: str):
        self.__content = content

    @property
    def metamodeloArquitecturaPila_Body(self):
        return self.__metamodeloArquitecturaPila_Body

    @metamodeloArquitecturaPila_Body.setter
    def metamodeloArquitecturaPila_Body(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Body__metamodeloArquitecturaPila_Body", None)
        self.__metamodeloArquitecturaPila_Body = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Method62"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Method62", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Method62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Method62"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Method62", None)
                setattr(value, "metamodeloArquitecturaPila_Method62", self)

class metamodeloArquitecturaPila_Function:

    def __init__(self, name: str, metamodeloArquitecturaPila_Function: "metamodeloArquitecturaPila_Service" = None, metamodeloArquitecturaPila_Function65: "metamodeloArquitecturaPila_BusinessLogic" = None, metamodeloArquitecturaPila_Function67: set["metamodeloArquitecturaPila_Parameter"] = None, metamodeloArquitecturaPila_Function70: "metamodeloArquitecturaPila_Parameter" = None, metamodeloArquitecturaPila_Function73: "metamodeloArquitecturaPila_FunctionBody" = None):
        self.name = name
        self.metamodeloArquitecturaPila_Function = metamodeloArquitecturaPila_Function
        self.metamodeloArquitecturaPila_Function65 = metamodeloArquitecturaPila_Function65
        self.metamodeloArquitecturaPila_Function67 = metamodeloArquitecturaPila_Function67 if metamodeloArquitecturaPila_Function67 is not None else set()
        self.metamodeloArquitecturaPila_Function70 = metamodeloArquitecturaPila_Function70
        self.metamodeloArquitecturaPila_Function73 = metamodeloArquitecturaPila_Function73
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_Function73(self):
        return self.__metamodeloArquitecturaPila_Function73

    @metamodeloArquitecturaPila_Function73.setter
    def metamodeloArquitecturaPila_Function73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Function__metamodeloArquitecturaPila_Function73", None)
        self.__metamodeloArquitecturaPila_Function73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_FunctionBody"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_FunctionBody", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_FunctionBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_FunctionBody"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_FunctionBody", None)
                setattr(value, "metamodeloArquitecturaPila_FunctionBody", self)

    @property
    def metamodeloArquitecturaPila_Function65(self):
        return self.__metamodeloArquitecturaPila_Function65

    @metamodeloArquitecturaPila_Function65.setter
    def metamodeloArquitecturaPila_Function65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Function__metamodeloArquitecturaPila_Function65", None)
        self.__metamodeloArquitecturaPila_Function65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_BusinessLogic64"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_BusinessLogic64", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_BusinessLogic64"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_BusinessLogic64", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_BusinessLogic64", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_Function70(self):
        return self.__metamodeloArquitecturaPila_Function70

    @metamodeloArquitecturaPila_Function70.setter
    def metamodeloArquitecturaPila_Function70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Function__metamodeloArquitecturaPila_Function70", None)
        self.__metamodeloArquitecturaPila_Function70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Parameter71"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Parameter71", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Parameter71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Parameter71"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Parameter71", None)
                setattr(value, "metamodeloArquitecturaPila_Parameter71", self)

    @property
    def metamodeloArquitecturaPila_Function(self):
        return self.__metamodeloArquitecturaPila_Function

    @metamodeloArquitecturaPila_Function.setter
    def metamodeloArquitecturaPila_Function(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Function__metamodeloArquitecturaPila_Function", None)
        self.__metamodeloArquitecturaPila_Function = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Service40"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Service40", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Service40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Service40"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Service40", None)
                setattr(value, "metamodeloArquitecturaPila_Service40", self)

    @property
    def metamodeloArquitecturaPila_Function67(self):
        return self.__metamodeloArquitecturaPila_Function67

    @metamodeloArquitecturaPila_Function67.setter
    def metamodeloArquitecturaPila_Function67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Function__metamodeloArquitecturaPila_Function67", None)
        self.__metamodeloArquitecturaPila_Function67 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Parameter68"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Parameter68", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Parameter68", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Parameter68"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Parameter68", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Parameter68", self)
                    

class metamodeloArquitecturaPila_Parameter:

    def __init__(self, name: str, metamodeloArquitecturaPila_Parameter: "metamodeloArquitecturaPila_Service" = None, metamodeloArquitecturaPila_Parameter38: "metamodeloArquitecturaPila_Service" = None, metamodeloArquitecturaPila_Parameter57: "metamodeloArquitecturaPila_Method" = None, metamodeloArquitecturaPila_Parameter60: "metamodeloArquitecturaPila_Method" = None, metamodeloArquitecturaPila_Parameter68: "metamodeloArquitecturaPila_Function" = None, metamodeloArquitecturaPila_Parameter71: "metamodeloArquitecturaPila_Function" = None, metamodeloArquitecturaPila_Parameter75: "metamodeloArquitecturaPila_DataType" = None):
        self.name = name
        self.metamodeloArquitecturaPila_Parameter = metamodeloArquitecturaPila_Parameter
        self.metamodeloArquitecturaPila_Parameter38 = metamodeloArquitecturaPila_Parameter38
        self.metamodeloArquitecturaPila_Parameter57 = metamodeloArquitecturaPila_Parameter57
        self.metamodeloArquitecturaPila_Parameter60 = metamodeloArquitecturaPila_Parameter60
        self.metamodeloArquitecturaPila_Parameter68 = metamodeloArquitecturaPila_Parameter68
        self.metamodeloArquitecturaPila_Parameter71 = metamodeloArquitecturaPila_Parameter71
        self.metamodeloArquitecturaPila_Parameter75 = metamodeloArquitecturaPila_Parameter75
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_Parameter57(self):
        return self.__metamodeloArquitecturaPila_Parameter57

    @metamodeloArquitecturaPila_Parameter57.setter
    def metamodeloArquitecturaPila_Parameter57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Parameter__metamodeloArquitecturaPila_Parameter57", None)
        self.__metamodeloArquitecturaPila_Parameter57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Method56"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Method56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Method56"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Method56", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Method56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_Parameter75(self):
        return self.__metamodeloArquitecturaPila_Parameter75

    @metamodeloArquitecturaPila_Parameter75.setter
    def metamodeloArquitecturaPila_Parameter75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Parameter__metamodeloArquitecturaPila_Parameter75", None)
        self.__metamodeloArquitecturaPila_Parameter75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_DataType76"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_DataType76", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_DataType76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_DataType76"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_DataType76", None)
                setattr(value, "metamodeloArquitecturaPila_DataType76", self)

    @property
    def metamodeloArquitecturaPila_Parameter38(self):
        return self.__metamodeloArquitecturaPila_Parameter38

    @metamodeloArquitecturaPila_Parameter38.setter
    def metamodeloArquitecturaPila_Parameter38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Parameter__metamodeloArquitecturaPila_Parameter38", None)
        self.__metamodeloArquitecturaPila_Parameter38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Service37"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Service37", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Service37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Service37"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Service37", None)
                setattr(value, "metamodeloArquitecturaPila_Service37", self)

    @property
    def metamodeloArquitecturaPila_Parameter(self):
        return self.__metamodeloArquitecturaPila_Parameter

    @metamodeloArquitecturaPila_Parameter.setter
    def metamodeloArquitecturaPila_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Parameter__metamodeloArquitecturaPila_Parameter", None)
        self.__metamodeloArquitecturaPila_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Service35"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Service35", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Service35"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Service35", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Service35", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_Parameter60(self):
        return self.__metamodeloArquitecturaPila_Parameter60

    @metamodeloArquitecturaPila_Parameter60.setter
    def metamodeloArquitecturaPila_Parameter60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Parameter__metamodeloArquitecturaPila_Parameter60", None)
        self.__metamodeloArquitecturaPila_Parameter60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Method59"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Method59", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Method59", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Method59"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Method59", None)
                setattr(value, "metamodeloArquitecturaPila_Method59", self)

    @property
    def metamodeloArquitecturaPila_Parameter71(self):
        return self.__metamodeloArquitecturaPila_Parameter71

    @metamodeloArquitecturaPila_Parameter71.setter
    def metamodeloArquitecturaPila_Parameter71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Parameter__metamodeloArquitecturaPila_Parameter71", None)
        self.__metamodeloArquitecturaPila_Parameter71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Function70"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Function70", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Function70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Function70"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Function70", None)
                setattr(value, "metamodeloArquitecturaPila_Function70", self)

    @property
    def metamodeloArquitecturaPila_Parameter68(self):
        return self.__metamodeloArquitecturaPila_Parameter68

    @metamodeloArquitecturaPila_Parameter68.setter
    def metamodeloArquitecturaPila_Parameter68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Parameter__metamodeloArquitecturaPila_Parameter68", None)
        self.__metamodeloArquitecturaPila_Parameter68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Function67"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Function67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Function67"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Function67", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Function67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class ComplexComponent:

    pass
class metamodeloArquitecturaPila_Select(ComplexComponent):

    pass
class metamodeloArquitecturaPila_TextArea(ComplexComponent):

    def __init__(self, visibleLines: str):
        self.visibleLines = visibleLines
        
    @property
    def visibleLines(self) -> str:
        return self.__visibleLines

    @visibleLines.setter
    def visibleLines(self, visibleLines: str):
        self.__visibleLines = visibleLines

class metamodeloArquitecturaPila_Grid(ComplexComponent):

    def __init__(self, cols: str, rows: str):
        self.cols = cols
        self.rows = rows
        
    @property
    def cols(self) -> str:
        return self.__cols

    @cols.setter
    def cols(self, cols: str):
        self.__cols = cols

    @property
    def rows(self) -> str:
        return self.__rows

    @rows.setter
    def rows(self, rows: str):
        self.__rows = rows

class metamodeloArquitecturaPila_Method:

    def __init__(self, name: str, metamodeloArquitecturaPila_Method: "metamodeloArquitecturaPila_Entity" = None, metamodeloArquitecturaPila_Method56: set["metamodeloArquitecturaPila_Parameter"] = None, metamodeloArquitecturaPila_Method59: "metamodeloArquitecturaPila_Parameter" = None, metamodeloArquitecturaPila_Method62: "metamodeloArquitecturaPila_Body" = None):
        self.name = name
        self.metamodeloArquitecturaPila_Method = metamodeloArquitecturaPila_Method
        self.metamodeloArquitecturaPila_Method56 = metamodeloArquitecturaPila_Method56 if metamodeloArquitecturaPila_Method56 is not None else set()
        self.metamodeloArquitecturaPila_Method59 = metamodeloArquitecturaPila_Method59
        self.metamodeloArquitecturaPila_Method62 = metamodeloArquitecturaPila_Method62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_Method62(self):
        return self.__metamodeloArquitecturaPila_Method62

    @metamodeloArquitecturaPila_Method62.setter
    def metamodeloArquitecturaPila_Method62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Method__metamodeloArquitecturaPila_Method62", None)
        self.__metamodeloArquitecturaPila_Method62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Body"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Body", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Body", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Body"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Body", None)
                setattr(value, "metamodeloArquitecturaPila_Body", self)

    @property
    def metamodeloArquitecturaPila_Method56(self):
        return self.__metamodeloArquitecturaPila_Method56

    @metamodeloArquitecturaPila_Method56.setter
    def metamodeloArquitecturaPila_Method56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Method__metamodeloArquitecturaPila_Method56", None)
        self.__metamodeloArquitecturaPila_Method56 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Parameter57"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Parameter57", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Parameter57", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Parameter57"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Parameter57", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Parameter57", self)
                    

    @property
    def metamodeloArquitecturaPila_Method59(self):
        return self.__metamodeloArquitecturaPila_Method59

    @metamodeloArquitecturaPila_Method59.setter
    def metamodeloArquitecturaPila_Method59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Method__metamodeloArquitecturaPila_Method59", None)
        self.__metamodeloArquitecturaPila_Method59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Parameter60"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Parameter60", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Parameter60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Parameter60"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Parameter60", None)
                setattr(value, "metamodeloArquitecturaPila_Parameter60", self)

    @property
    def metamodeloArquitecturaPila_Method(self):
        return self.__metamodeloArquitecturaPila_Method

    @metamodeloArquitecturaPila_Method.setter
    def metamodeloArquitecturaPila_Method(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Method__metamodeloArquitecturaPila_Method", None)
        self.__metamodeloArquitecturaPila_Method = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Entity48"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Entity48", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Entity48"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Entity48", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Entity48", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodeloArquitecturaPila_Attribute:

    def __init__(self, value: str, name: str, metamodeloArquitecturaPila_Attribute: "metamodeloArquitecturaPila_Entity" = None, metamodeloArquitecturaPila_Attribute53: "metamodeloArquitecturaPila_DataType" = None):
        self.value = value
        self.name = name
        self.metamodeloArquitecturaPila_Attribute = metamodeloArquitecturaPila_Attribute
        self.metamodeloArquitecturaPila_Attribute53 = metamodeloArquitecturaPila_Attribute53
        
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
    def metamodeloArquitecturaPila_Attribute53(self):
        return self.__metamodeloArquitecturaPila_Attribute53

    @metamodeloArquitecturaPila_Attribute53.setter
    def metamodeloArquitecturaPila_Attribute53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Attribute__metamodeloArquitecturaPila_Attribute53", None)
        self.__metamodeloArquitecturaPila_Attribute53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_DataType54"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_DataType54", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_DataType54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_DataType54"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_DataType54", None)
                setattr(value, "metamodeloArquitecturaPila_DataType54", self)

    @property
    def metamodeloArquitecturaPila_Attribute(self):
        return self.__metamodeloArquitecturaPila_Attribute

    @metamodeloArquitecturaPila_Attribute.setter
    def metamodeloArquitecturaPila_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Attribute__metamodeloArquitecturaPila_Attribute", None)
        self.__metamodeloArquitecturaPila_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Entity46"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Entity46", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Entity46"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Entity46", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Entity46", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodeloArquitecturaPila_DataType:

    def __init__(self, name: str, metamodeloArquitecturaPila_DataType: "metamodeloArquitecturaPila_BusinessModel" = None, metamodeloArquitecturaPila_DataType54: "metamodeloArquitecturaPila_Attribute" = None, metamodeloArquitecturaPila_DataType76: "metamodeloArquitecturaPila_Parameter" = None):
        self.name = name
        self.metamodeloArquitecturaPila_DataType = metamodeloArquitecturaPila_DataType
        self.metamodeloArquitecturaPila_DataType54 = metamodeloArquitecturaPila_DataType54
        self.metamodeloArquitecturaPila_DataType76 = metamodeloArquitecturaPila_DataType76
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_DataType(self):
        return self.__metamodeloArquitecturaPila_DataType

    @metamodeloArquitecturaPila_DataType.setter
    def metamodeloArquitecturaPila_DataType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_DataType__metamodeloArquitecturaPila_DataType", None)
        self.__metamodeloArquitecturaPila_DataType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_BusinessModel44"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_BusinessModel44", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_BusinessModel44"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_BusinessModel44", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_BusinessModel44", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_DataType54(self):
        return self.__metamodeloArquitecturaPila_DataType54

    @metamodeloArquitecturaPila_DataType54.setter
    def metamodeloArquitecturaPila_DataType54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_DataType__metamodeloArquitecturaPila_DataType54", None)
        self.__metamodeloArquitecturaPila_DataType54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Attribute53"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Attribute53", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Attribute53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Attribute53"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Attribute53", None)
                setattr(value, "metamodeloArquitecturaPila_Attribute53", self)

    @property
    def metamodeloArquitecturaPila_DataType76(self):
        return self.__metamodeloArquitecturaPila_DataType76

    @metamodeloArquitecturaPila_DataType76.setter
    def metamodeloArquitecturaPila_DataType76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_DataType__metamodeloArquitecturaPila_DataType76", None)
        self.__metamodeloArquitecturaPila_DataType76 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Parameter75"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Parameter75", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Parameter75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Parameter75"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Parameter75", None)
                setattr(value, "metamodeloArquitecturaPila_Parameter75", self)

class metamodeloArquitecturaPila_Entity:

    def __init__(self, name: str, metamodeloArquitecturaPila_Entity: "metamodeloArquitecturaPila_BusinessModel" = None, metamodeloArquitecturaPila_Entity46: set["metamodeloArquitecturaPila_Attribute"] = None, metamodeloArquitecturaPila_Entity48: set["metamodeloArquitecturaPila_Method"] = None, metamodeloArquitecturaPila_Entity51: "metamodeloArquitecturaPila_Entity" = None, metamodeloArquitecturaPila_Entity49: set["metamodeloArquitecturaPila_Entity"] = None):
        self.name = name
        self.metamodeloArquitecturaPila_Entity = metamodeloArquitecturaPila_Entity
        self.metamodeloArquitecturaPila_Entity46 = metamodeloArquitecturaPila_Entity46 if metamodeloArquitecturaPila_Entity46 is not None else set()
        self.metamodeloArquitecturaPila_Entity48 = metamodeloArquitecturaPila_Entity48 if metamodeloArquitecturaPila_Entity48 is not None else set()
        self.metamodeloArquitecturaPila_Entity51 = metamodeloArquitecturaPila_Entity51
        self.metamodeloArquitecturaPila_Entity49 = metamodeloArquitecturaPila_Entity49 if metamodeloArquitecturaPila_Entity49 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_Entity48(self):
        return self.__metamodeloArquitecturaPila_Entity48

    @metamodeloArquitecturaPila_Entity48.setter
    def metamodeloArquitecturaPila_Entity48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Entity__metamodeloArquitecturaPila_Entity48", None)
        self.__metamodeloArquitecturaPila_Entity48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Method"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Method", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Method", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Method"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Method", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Method", self)
                    

    @property
    def metamodeloArquitecturaPila_Entity(self):
        return self.__metamodeloArquitecturaPila_Entity

    @metamodeloArquitecturaPila_Entity.setter
    def metamodeloArquitecturaPila_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Entity__metamodeloArquitecturaPila_Entity", None)
        self.__metamodeloArquitecturaPila_Entity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_BusinessModel42"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_BusinessModel42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_BusinessModel42"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_BusinessModel42", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_BusinessModel42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_Entity49(self):
        return self.__metamodeloArquitecturaPila_Entity49

    @metamodeloArquitecturaPila_Entity49.setter
    def metamodeloArquitecturaPila_Entity49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Entity__metamodeloArquitecturaPila_Entity49", None)
        self.__metamodeloArquitecturaPila_Entity49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Entity51"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Entity51", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Entity51", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Entity51"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Entity51", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Entity51", self)
                    

    @property
    def metamodeloArquitecturaPila_Entity51(self):
        return self.__metamodeloArquitecturaPila_Entity51

    @metamodeloArquitecturaPila_Entity51.setter
    def metamodeloArquitecturaPila_Entity51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Entity__metamodeloArquitecturaPila_Entity51", None)
        self.__metamodeloArquitecturaPila_Entity51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Entity49"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Entity49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Entity49"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Entity49", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Entity49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_Entity46(self):
        return self.__metamodeloArquitecturaPila_Entity46

    @metamodeloArquitecturaPila_Entity46.setter
    def metamodeloArquitecturaPila_Entity46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Entity__metamodeloArquitecturaPila_Entity46", None)
        self.__metamodeloArquitecturaPila_Entity46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Attribute"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Attribute"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Attribute", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Attribute", self)
                    

class metamodeloArquitecturaPila_GraphicalComponent(ABC):

    def __init__(self, name: str, length: str, height: str, id: str, displayName: str, metamodeloArquitecturaPila_GraphicalComponent26: "metamodeloArquitecturaPila_Form" = None, metamodeloArquitecturaPila_GraphicalComponent: "metamodeloArquitecturaPila_View" = None):
        self.name = name
        self.length = length
        self.height = height
        self.id = id
        self.displayName = displayName
        self.metamodeloArquitecturaPila_GraphicalComponent26 = metamodeloArquitecturaPila_GraphicalComponent26
        self.metamodeloArquitecturaPila_GraphicalComponent = metamodeloArquitecturaPila_GraphicalComponent
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def length(self) -> str:
        return self.__length

    @length.setter
    def length(self, length: str):
        self.__length = length

    @property
    def displayName(self) -> str:
        return self.__displayName

    @displayName.setter
    def displayName(self, displayName: str):
        self.__displayName = displayName

    @property
    def height(self) -> str:
        return self.__height

    @height.setter
    def height(self, height: str):
        self.__height = height

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_GraphicalComponent(self):
        return self.__metamodeloArquitecturaPila_GraphicalComponent

    @metamodeloArquitecturaPila_GraphicalComponent.setter
    def metamodeloArquitecturaPila_GraphicalComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_GraphicalComponent__metamodeloArquitecturaPila_GraphicalComponent", None)
        self.__metamodeloArquitecturaPila_GraphicalComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_View16"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_View16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_View16"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_View16", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_View16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_GraphicalComponent26(self):
        return self.__metamodeloArquitecturaPila_GraphicalComponent26

    @metamodeloArquitecturaPila_GraphicalComponent26.setter
    def metamodeloArquitecturaPila_GraphicalComponent26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_GraphicalComponent__metamodeloArquitecturaPila_GraphicalComponent26", None)
        self.__metamodeloArquitecturaPila_GraphicalComponent26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Form25"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Form25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Form25"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Form25", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Form25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodeloArquitecturaPila_Form:

    def __init__(self, name: str, id: str, metamodeloArquitecturaPila_Form25: set["metamodeloArquitecturaPila_GraphicalComponent"] = None, metamodeloArquitecturaPila_Form: "metamodeloArquitecturaPila_View" = None):
        self.name = name
        self.id = id
        self.metamodeloArquitecturaPila_Form25 = metamodeloArquitecturaPila_Form25 if metamodeloArquitecturaPila_Form25 is not None else set()
        self.metamodeloArquitecturaPila_Form = metamodeloArquitecturaPila_Form
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def metamodeloArquitecturaPila_Form25(self):
        return self.__metamodeloArquitecturaPila_Form25

    @metamodeloArquitecturaPila_Form25.setter
    def metamodeloArquitecturaPila_Form25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Form__metamodeloArquitecturaPila_Form25", None)
        self.__metamodeloArquitecturaPila_Form25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_GraphicalComponent26"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_GraphicalComponent26", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_GraphicalComponent26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_GraphicalComponent26"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_GraphicalComponent26", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_GraphicalComponent26", self)
                    

    @property
    def metamodeloArquitecturaPila_Form(self):
        return self.__metamodeloArquitecturaPila_Form

    @metamodeloArquitecturaPila_Form.setter
    def metamodeloArquitecturaPila_Form(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Form__metamodeloArquitecturaPila_Form", None)
        self.__metamodeloArquitecturaPila_Form = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_View14"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_View14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_View14"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_View14", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_View14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodeloArquitecturaPila_Menu:

    def __init__(self, name: str, id: str, metamodeloArquitecturaPila_Menu23: set["metamodeloArquitecturaPila_MenuItem"] = None, metamodeloArquitecturaPila_Menu: "metamodeloArquitecturaPila_View" = None):
        self.name = name
        self.id = id
        self.metamodeloArquitecturaPila_Menu23 = metamodeloArquitecturaPila_Menu23 if metamodeloArquitecturaPila_Menu23 is not None else set()
        self.metamodeloArquitecturaPila_Menu = metamodeloArquitecturaPila_Menu
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_Menu(self):
        return self.__metamodeloArquitecturaPila_Menu

    @metamodeloArquitecturaPila_Menu.setter
    def metamodeloArquitecturaPila_Menu(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Menu__metamodeloArquitecturaPila_Menu", None)
        self.__metamodeloArquitecturaPila_Menu = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_View12"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_View12", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_View12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_View12"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_View12", None)
                setattr(value, "metamodeloArquitecturaPila_View12", self)

    @property
    def metamodeloArquitecturaPila_Menu23(self):
        return self.__metamodeloArquitecturaPila_Menu23

    @metamodeloArquitecturaPila_Menu23.setter
    def metamodeloArquitecturaPila_Menu23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Menu__metamodeloArquitecturaPila_Menu23", None)
        self.__metamodeloArquitecturaPila_Menu23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_MenuItem"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_MenuItem", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_MenuItem", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_MenuItem"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_MenuItem", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_MenuItem", self)
                    

class metamodeloArquitecturaPila_TitleBar:

    def __init__(self, name: str, id: str, metamodeloArquitecturaPila_TitleBar21: set["metamodeloArquitecturaPila_SimpleComponent"] = None, metamodeloArquitecturaPila_TitleBar: "metamodeloArquitecturaPila_View" = None):
        self.name = name
        self.id = id
        self.metamodeloArquitecturaPila_TitleBar21 = metamodeloArquitecturaPila_TitleBar21 if metamodeloArquitecturaPila_TitleBar21 is not None else set()
        self.metamodeloArquitecturaPila_TitleBar = metamodeloArquitecturaPila_TitleBar
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def metamodeloArquitecturaPila_TitleBar(self):
        return self.__metamodeloArquitecturaPila_TitleBar

    @metamodeloArquitecturaPila_TitleBar.setter
    def metamodeloArquitecturaPila_TitleBar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_TitleBar__metamodeloArquitecturaPila_TitleBar", None)
        self.__metamodeloArquitecturaPila_TitleBar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_View10"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_View10", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_View10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_View10"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_View10", None)
                setattr(value, "metamodeloArquitecturaPila_View10", self)

    @property
    def metamodeloArquitecturaPila_TitleBar21(self):
        return self.__metamodeloArquitecturaPila_TitleBar21

    @metamodeloArquitecturaPila_TitleBar21.setter
    def metamodeloArquitecturaPila_TitleBar21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_TitleBar__metamodeloArquitecturaPila_TitleBar21", None)
        self.__metamodeloArquitecturaPila_TitleBar21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_SimpleComponent"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_SimpleComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_SimpleComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_SimpleComponent"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_SimpleComponent", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_SimpleComponent", self)
                    

class metamodeloArquitecturaPila_BusinessLogic:

    def __init__(self, name: str, metamodeloArquitecturaPila_BusinessLogic: "metamodeloArquitecturaPila_Architecture" = None, metamodeloArquitecturaPila_BusinessLogic64: set["metamodeloArquitecturaPila_Function"] = None):
        self.name = name
        self.metamodeloArquitecturaPila_BusinessLogic = metamodeloArquitecturaPila_BusinessLogic
        self.metamodeloArquitecturaPila_BusinessLogic64 = metamodeloArquitecturaPila_BusinessLogic64 if metamodeloArquitecturaPila_BusinessLogic64 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_BusinessLogic64(self):
        return self.__metamodeloArquitecturaPila_BusinessLogic64

    @metamodeloArquitecturaPila_BusinessLogic64.setter
    def metamodeloArquitecturaPila_BusinessLogic64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_BusinessLogic__metamodeloArquitecturaPila_BusinessLogic64", None)
        self.__metamodeloArquitecturaPila_BusinessLogic64 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Function65"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Function65", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Function65", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Function65"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Function65", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Function65", self)
                    

    @property
    def metamodeloArquitecturaPila_BusinessLogic(self):
        return self.__metamodeloArquitecturaPila_BusinessLogic

    @metamodeloArquitecturaPila_BusinessLogic.setter
    def metamodeloArquitecturaPila_BusinessLogic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_BusinessLogic__metamodeloArquitecturaPila_BusinessLogic", None)
        self.__metamodeloArquitecturaPila_BusinessLogic = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Architecture8"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Architecture8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Architecture8"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Architecture8", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Architecture8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodeloArquitecturaPila_ServiceType:

    def __init__(self, name: str, metamodeloArquitecturaPila_ServiceType: "metamodeloArquitecturaPila_Architecture" = None, metamodeloArquitecturaPila_ServiceType33: "metamodeloArquitecturaPila_Service" = None):
        self.name = name
        self.metamodeloArquitecturaPila_ServiceType = metamodeloArquitecturaPila_ServiceType
        self.metamodeloArquitecturaPila_ServiceType33 = metamodeloArquitecturaPila_ServiceType33
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_ServiceType33(self):
        return self.__metamodeloArquitecturaPila_ServiceType33

    @metamodeloArquitecturaPila_ServiceType33.setter
    def metamodeloArquitecturaPila_ServiceType33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_ServiceType__metamodeloArquitecturaPila_ServiceType33", None)
        self.__metamodeloArquitecturaPila_ServiceType33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Service32"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Service32", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Service32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Service32"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Service32", None)
                setattr(value, "metamodeloArquitecturaPila_Service32", self)

    @property
    def metamodeloArquitecturaPila_ServiceType(self):
        return self.__metamodeloArquitecturaPila_ServiceType

    @metamodeloArquitecturaPila_ServiceType.setter
    def metamodeloArquitecturaPila_ServiceType(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_ServiceType__metamodeloArquitecturaPila_ServiceType", None)
        self.__metamodeloArquitecturaPila_ServiceType = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Architecture6"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Architecture6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Architecture6"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Architecture6", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Architecture6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodeloArquitecturaPila_Service:

    def __init__(self, name: str, metamodeloArquitecturaPila_Service: "metamodeloArquitecturaPila_Architecture" = None, metamodeloArquitecturaPila_Service40: "metamodeloArquitecturaPila_Function" = None, metamodeloArquitecturaPila_Service32: "metamodeloArquitecturaPila_ServiceType" = None, metamodeloArquitecturaPila_Service35: set["metamodeloArquitecturaPila_Parameter"] = None, metamodeloArquitecturaPila_Service37: "metamodeloArquitecturaPila_Parameter" = None):
        self.name = name
        self.metamodeloArquitecturaPila_Service = metamodeloArquitecturaPila_Service
        self.metamodeloArquitecturaPila_Service40 = metamodeloArquitecturaPila_Service40
        self.metamodeloArquitecturaPila_Service32 = metamodeloArquitecturaPila_Service32
        self.metamodeloArquitecturaPila_Service35 = metamodeloArquitecturaPila_Service35 if metamodeloArquitecturaPila_Service35 is not None else set()
        self.metamodeloArquitecturaPila_Service37 = metamodeloArquitecturaPila_Service37
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_Service32(self):
        return self.__metamodeloArquitecturaPila_Service32

    @metamodeloArquitecturaPila_Service32.setter
    def metamodeloArquitecturaPila_Service32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Service__metamodeloArquitecturaPila_Service32", None)
        self.__metamodeloArquitecturaPila_Service32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_ServiceType33"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_ServiceType33", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_ServiceType33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_ServiceType33"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_ServiceType33", None)
                setattr(value, "metamodeloArquitecturaPila_ServiceType33", self)

    @property
    def metamodeloArquitecturaPila_Service37(self):
        return self.__metamodeloArquitecturaPila_Service37

    @metamodeloArquitecturaPila_Service37.setter
    def metamodeloArquitecturaPila_Service37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Service__metamodeloArquitecturaPila_Service37", None)
        self.__metamodeloArquitecturaPila_Service37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Parameter38"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Parameter38", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Parameter38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Parameter38"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Parameter38", None)
                setattr(value, "metamodeloArquitecturaPila_Parameter38", self)

    @property
    def metamodeloArquitecturaPila_Service35(self):
        return self.__metamodeloArquitecturaPila_Service35

    @metamodeloArquitecturaPila_Service35.setter
    def metamodeloArquitecturaPila_Service35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Service__metamodeloArquitecturaPila_Service35", None)
        self.__metamodeloArquitecturaPila_Service35 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Parameter"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Parameter", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Parameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Parameter"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Parameter", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Parameter", self)
                    

    @property
    def metamodeloArquitecturaPila_Service40(self):
        return self.__metamodeloArquitecturaPila_Service40

    @metamodeloArquitecturaPila_Service40.setter
    def metamodeloArquitecturaPila_Service40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Service__metamodeloArquitecturaPila_Service40", None)
        self.__metamodeloArquitecturaPila_Service40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Function"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Function", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Function", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Function"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Function", None)
                setattr(value, "metamodeloArquitecturaPila_Function", self)

    @property
    def metamodeloArquitecturaPila_Service(self):
        return self.__metamodeloArquitecturaPila_Service

    @metamodeloArquitecturaPila_Service.setter
    def metamodeloArquitecturaPila_Service(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Service__metamodeloArquitecturaPila_Service", None)
        self.__metamodeloArquitecturaPila_Service = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Architecture4"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Architecture4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Architecture4"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Architecture4", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Architecture4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class metamodeloArquitecturaPila_ListItem:

    def __init__(self, isSelected: str, action: str, metamodeloArquitecturaPila_ListItem: "metamodeloArquitecturaPila_DropdownList" = None):
        self.isSelected = isSelected
        self.action = action
        self.metamodeloArquitecturaPila_ListItem = metamodeloArquitecturaPila_ListItem
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

    @property
    def isSelected(self) -> str:
        return self.__isSelected

    @isSelected.setter
    def isSelected(self, isSelected: str):
        self.__isSelected = isSelected

    @property
    def metamodeloArquitecturaPila_ListItem(self):
        return self.__metamodeloArquitecturaPila_ListItem

    @metamodeloArquitecturaPila_ListItem.setter
    def metamodeloArquitecturaPila_ListItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_ListItem__metamodeloArquitecturaPila_ListItem", None)
        self.__metamodeloArquitecturaPila_ListItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_DropdownList"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_DropdownList", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_DropdownList"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_DropdownList", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_DropdownList", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class GraphicalComponent:

    pass
class metamodeloArquitecturaPila_ComplexComponent(GraphicalComponent):

    pass
class SimpleComponent:

    pass
class metamodeloArquitecturaPila_Input(SimpleComponent):

    def __init__(self, action: str):
        self.action = action
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

class metamodeloArquitecturaPila_DropdownList(SimpleComponent):

    pass
class metamodeloArquitecturaPila_Label(SimpleComponent):

    pass
class metamodeloArquitecturaPila_Button(SimpleComponent):

    def __init__(self, action: str):
        self.action = action
        
    @property
    def action(self) -> str:
        return self.__action

    @action.setter
    def action(self, action: str):
        self.__action = action

class metamodeloArquitecturaPila_MenuItem:

    def __init__(self, name: str, id: str, metamodeloArquitecturaPila_MenuItem: "metamodeloArquitecturaPila_Menu" = None, metamodeloArquitecturaPila_MenuItem28: "metamodeloArquitecturaPila_SimpleComponent" = None):
        self.name = name
        self.id = id
        self.metamodeloArquitecturaPila_MenuItem = metamodeloArquitecturaPila_MenuItem
        self.metamodeloArquitecturaPila_MenuItem28 = metamodeloArquitecturaPila_MenuItem28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def metamodeloArquitecturaPila_MenuItem(self):
        return self.__metamodeloArquitecturaPila_MenuItem

    @metamodeloArquitecturaPila_MenuItem.setter
    def metamodeloArquitecturaPila_MenuItem(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_MenuItem__metamodeloArquitecturaPila_MenuItem", None)
        self.__metamodeloArquitecturaPila_MenuItem = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Menu23"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Menu23", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Menu23"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Menu23", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Menu23", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_MenuItem28(self):
        return self.__metamodeloArquitecturaPila_MenuItem28

    @metamodeloArquitecturaPila_MenuItem28.setter
    def metamodeloArquitecturaPila_MenuItem28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_MenuItem__metamodeloArquitecturaPila_MenuItem28", None)
        self.__metamodeloArquitecturaPila_MenuItem28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_SimpleComponent29"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_SimpleComponent29", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_SimpleComponent29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_SimpleComponent29"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_SimpleComponent29", None)
                setattr(value, "metamodeloArquitecturaPila_SimpleComponent29", self)

class metamodeloArquitecturaPila_SimpleComponent(GraphicalComponent):

    def __init__(self, value: str, metamodeloArquitecturaPila_SimpleComponent: "metamodeloArquitecturaPila_TitleBar" = None, metamodeloArquitecturaPila_SimpleComponent29: "metamodeloArquitecturaPila_MenuItem" = None):
        self.value = value
        self.metamodeloArquitecturaPila_SimpleComponent = metamodeloArquitecturaPila_SimpleComponent
        self.metamodeloArquitecturaPila_SimpleComponent29 = metamodeloArquitecturaPila_SimpleComponent29
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def metamodeloArquitecturaPila_SimpleComponent(self):
        return self.__metamodeloArquitecturaPila_SimpleComponent

    @metamodeloArquitecturaPila_SimpleComponent.setter
    def metamodeloArquitecturaPila_SimpleComponent(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_SimpleComponent__metamodeloArquitecturaPila_SimpleComponent", None)
        self.__metamodeloArquitecturaPila_SimpleComponent = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_TitleBar21"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_TitleBar21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_TitleBar21"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_TitleBar21", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_TitleBar21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_SimpleComponent29(self):
        return self.__metamodeloArquitecturaPila_SimpleComponent29

    @metamodeloArquitecturaPila_SimpleComponent29.setter
    def metamodeloArquitecturaPila_SimpleComponent29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_SimpleComponent__metamodeloArquitecturaPila_SimpleComponent29", None)
        self.__metamodeloArquitecturaPila_SimpleComponent29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_MenuItem28"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_MenuItem28", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_MenuItem28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_MenuItem28"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_MenuItem28", None)
                setattr(value, "metamodeloArquitecturaPila_MenuItem28", self)

class metamodeloArquitecturaPila_BusinessModel:

    pass
class metamodeloArquitecturaPila_View:

    def __init__(self, name: str, metamodeloArquitecturaPila_View: "metamodeloArquitecturaPila_Architecture" = None, metamodeloArquitecturaPila_View16: set["metamodeloArquitecturaPila_GraphicalComponent"] = None, metamodeloArquitecturaPila_View19: "metamodeloArquitecturaPila_View" = None, metamodeloArquitecturaPila_View17: set["metamodeloArquitecturaPila_View"] = None, metamodeloArquitecturaPila_View10: "metamodeloArquitecturaPila_TitleBar" = None, metamodeloArquitecturaPila_View12: "metamodeloArquitecturaPila_Menu" = None, metamodeloArquitecturaPila_View14: set["metamodeloArquitecturaPila_Form"] = None):
        self.name = name
        self.metamodeloArquitecturaPila_View = metamodeloArquitecturaPila_View
        self.metamodeloArquitecturaPila_View16 = metamodeloArquitecturaPila_View16 if metamodeloArquitecturaPila_View16 is not None else set()
        self.metamodeloArquitecturaPila_View19 = metamodeloArquitecturaPila_View19
        self.metamodeloArquitecturaPila_View17 = metamodeloArquitecturaPila_View17 if metamodeloArquitecturaPila_View17 is not None else set()
        self.metamodeloArquitecturaPila_View10 = metamodeloArquitecturaPila_View10
        self.metamodeloArquitecturaPila_View12 = metamodeloArquitecturaPila_View12
        self.metamodeloArquitecturaPila_View14 = metamodeloArquitecturaPila_View14 if metamodeloArquitecturaPila_View14 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_View12(self):
        return self.__metamodeloArquitecturaPila_View12

    @metamodeloArquitecturaPila_View12.setter
    def metamodeloArquitecturaPila_View12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_View__metamodeloArquitecturaPila_View12", None)
        self.__metamodeloArquitecturaPila_View12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Menu"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Menu", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_Menu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Menu"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Menu", None)
                setattr(value, "metamodeloArquitecturaPila_Menu", self)

    @property
    def metamodeloArquitecturaPila_View(self):
        return self.__metamodeloArquitecturaPila_View

    @metamodeloArquitecturaPila_View.setter
    def metamodeloArquitecturaPila_View(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_View__metamodeloArquitecturaPila_View", None)
        self.__metamodeloArquitecturaPila_View = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_Architecture"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_Architecture", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_Architecture"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_Architecture", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_Architecture", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_View10(self):
        return self.__metamodeloArquitecturaPila_View10

    @metamodeloArquitecturaPila_View10.setter
    def metamodeloArquitecturaPila_View10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_View__metamodeloArquitecturaPila_View10", None)
        self.__metamodeloArquitecturaPila_View10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_TitleBar"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_TitleBar", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_TitleBar", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_TitleBar"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_TitleBar", None)
                setattr(value, "metamodeloArquitecturaPila_TitleBar", self)

    @property
    def metamodeloArquitecturaPila_View16(self):
        return self.__metamodeloArquitecturaPila_View16

    @metamodeloArquitecturaPila_View16.setter
    def metamodeloArquitecturaPila_View16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_View__metamodeloArquitecturaPila_View16", None)
        self.__metamodeloArquitecturaPila_View16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_GraphicalComponent"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_GraphicalComponent", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_GraphicalComponent", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_GraphicalComponent"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_GraphicalComponent", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_GraphicalComponent", self)
                    

    @property
    def metamodeloArquitecturaPila_View14(self):
        return self.__metamodeloArquitecturaPila_View14

    @metamodeloArquitecturaPila_View14.setter
    def metamodeloArquitecturaPila_View14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_View__metamodeloArquitecturaPila_View14", None)
        self.__metamodeloArquitecturaPila_View14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Form"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Form", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Form", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Form"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Form", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Form", self)
                    

    @property
    def metamodeloArquitecturaPila_View19(self):
        return self.__metamodeloArquitecturaPila_View19

    @metamodeloArquitecturaPila_View19.setter
    def metamodeloArquitecturaPila_View19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_View__metamodeloArquitecturaPila_View19", None)
        self.__metamodeloArquitecturaPila_View19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_View17"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_View17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_View17"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_View17", None)
                if opp_val is None:
                    setattr(value, "metamodeloArquitecturaPila_View17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def metamodeloArquitecturaPila_View17(self):
        return self.__metamodeloArquitecturaPila_View17

    @metamodeloArquitecturaPila_View17.setter
    def metamodeloArquitecturaPila_View17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_View__metamodeloArquitecturaPila_View17", None)
        self.__metamodeloArquitecturaPila_View17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_View19"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_View19", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_View19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_View19"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_View19", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_View19", self)
                    

class metamodeloArquitecturaPila_Architecture:

    def __init__(self, name: str, metamodeloArquitecturaPila_Architecture: set["metamodeloArquitecturaPila_View"] = None, metamodeloArquitecturaPila_Architecture2: "metamodeloArquitecturaPila_BusinessModel" = None, metamodeloArquitecturaPila_Architecture4: set["metamodeloArquitecturaPila_Service"] = None, metamodeloArquitecturaPila_Architecture6: set["metamodeloArquitecturaPila_ServiceType"] = None, metamodeloArquitecturaPila_Architecture8: set["metamodeloArquitecturaPila_BusinessLogic"] = None):
        self.name = name
        self.metamodeloArquitecturaPila_Architecture = metamodeloArquitecturaPila_Architecture if metamodeloArquitecturaPila_Architecture is not None else set()
        self.metamodeloArquitecturaPila_Architecture2 = metamodeloArquitecturaPila_Architecture2
        self.metamodeloArquitecturaPila_Architecture4 = metamodeloArquitecturaPila_Architecture4 if metamodeloArquitecturaPila_Architecture4 is not None else set()
        self.metamodeloArquitecturaPila_Architecture6 = metamodeloArquitecturaPila_Architecture6 if metamodeloArquitecturaPila_Architecture6 is not None else set()
        self.metamodeloArquitecturaPila_Architecture8 = metamodeloArquitecturaPila_Architecture8 if metamodeloArquitecturaPila_Architecture8 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def metamodeloArquitecturaPila_Architecture2(self):
        return self.__metamodeloArquitecturaPila_Architecture2

    @metamodeloArquitecturaPila_Architecture2.setter
    def metamodeloArquitecturaPila_Architecture2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Architecture__metamodeloArquitecturaPila_Architecture2", None)
        self.__metamodeloArquitecturaPila_Architecture2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "metamodeloArquitecturaPila_BusinessModel"):
                opp_val = getattr(old_value, "metamodeloArquitecturaPila_BusinessModel", None)
                if opp_val == self:
                    setattr(old_value, "metamodeloArquitecturaPila_BusinessModel", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "metamodeloArquitecturaPila_BusinessModel"):
                opp_val = getattr(value, "metamodeloArquitecturaPila_BusinessModel", None)
                setattr(value, "metamodeloArquitecturaPila_BusinessModel", self)

    @property
    def metamodeloArquitecturaPila_Architecture(self):
        return self.__metamodeloArquitecturaPila_Architecture

    @metamodeloArquitecturaPila_Architecture.setter
    def metamodeloArquitecturaPila_Architecture(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Architecture__metamodeloArquitecturaPila_Architecture", None)
        self.__metamodeloArquitecturaPila_Architecture = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_View"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_View", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_View", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_View"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_View", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_View", self)
                    

    @property
    def metamodeloArquitecturaPila_Architecture6(self):
        return self.__metamodeloArquitecturaPila_Architecture6

    @metamodeloArquitecturaPila_Architecture6.setter
    def metamodeloArquitecturaPila_Architecture6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Architecture__metamodeloArquitecturaPila_Architecture6", None)
        self.__metamodeloArquitecturaPila_Architecture6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_ServiceType"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_ServiceType", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_ServiceType", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_ServiceType"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_ServiceType", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_ServiceType", self)
                    

    @property
    def metamodeloArquitecturaPila_Architecture8(self):
        return self.__metamodeloArquitecturaPila_Architecture8

    @metamodeloArquitecturaPila_Architecture8.setter
    def metamodeloArquitecturaPila_Architecture8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Architecture__metamodeloArquitecturaPila_Architecture8", None)
        self.__metamodeloArquitecturaPila_Architecture8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_BusinessLogic"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_BusinessLogic", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_BusinessLogic", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_BusinessLogic"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_BusinessLogic", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_BusinessLogic", self)
                    

    @property
    def metamodeloArquitecturaPila_Architecture4(self):
        return self.__metamodeloArquitecturaPila_Architecture4

    @metamodeloArquitecturaPila_Architecture4.setter
    def metamodeloArquitecturaPila_Architecture4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_metamodeloArquitecturaPila_Architecture__metamodeloArquitecturaPila_Architecture4", None)
        self.__metamodeloArquitecturaPila_Architecture4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "metamodeloArquitecturaPila_Service"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Service", None)
                    
                    if opp_val == self:
                        setattr(item, "metamodeloArquitecturaPila_Service", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "metamodeloArquitecturaPila_Service"):
                    opp_val = getattr(item, "metamodeloArquitecturaPila_Service", None)
                    
                    setattr(item, "metamodeloArquitecturaPila_Service", self)
                    
