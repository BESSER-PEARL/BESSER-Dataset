from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Graph_TLong:

    def __init__(self, value: str, Graph_TLong: "Graph_Graph" = None):
        self.value = value
        self.Graph_TLong = Graph_TLong
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def Graph_TLong(self):
        return self.__Graph_TLong

    @Graph_TLong.setter
    def Graph_TLong(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TLong__Graph_TLong", None)
        self.__Graph_TLong = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph12"):
                opp_val = getattr(old_value, "Graph_Graph12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph12"):
                opp_val = getattr(value, "Graph_Graph12", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_TInt:

    def __init__(self, value: int, Graph_TInt: "Graph_Graph" = None):
        self.value = value
        self.Graph_TInt = Graph_TInt
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: int):
        self.__value = value


    @property
    def Graph_TInt(self):
        return self.__Graph_TInt

    @Graph_TInt.setter
    def Graph_TInt(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TInt__Graph_TInt", None)
        self.__Graph_TInt = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph10"):
                opp_val = getattr(old_value, "Graph_Graph10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph10"):
                opp_val = getattr(value, "Graph_Graph10", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_TShort:

    def __init__(self, value: str, Graph_TShort: "Graph_Graph" = None):
        self.value = value
        self.Graph_TShort = Graph_TShort
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def Graph_TShort(self):
        return self.__Graph_TShort

    @Graph_TShort.setter
    def Graph_TShort(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TShort__Graph_TShort", None)
        self.__Graph_TShort = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph8"):
                opp_val = getattr(old_value, "Graph_Graph8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph8"):
                opp_val = getattr(value, "Graph_Graph8", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_TByte:

    def __init__(self, value: str, Graph_TByte: "Graph_Graph" = None):
        self.value = value
        self.Graph_TByte = Graph_TByte
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def Graph_TByte(self):
        return self.__Graph_TByte

    @Graph_TByte.setter
    def Graph_TByte(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TByte__Graph_TByte", None)
        self.__Graph_TByte = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph6"):
                opp_val = getattr(old_value, "Graph_Graph6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph6"):
                opp_val = getattr(value, "Graph_Graph6", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_TChar:

    def __init__(self, value: str, Graph_TChar: "Graph_Graph" = None):
        self.value = value
        self.Graph_TChar = Graph_TChar
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def Graph_TChar(self):
        return self.__Graph_TChar

    @Graph_TChar.setter
    def Graph_TChar(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TChar__Graph_TChar", None)
        self.__Graph_TChar = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph4"):
                opp_val = getattr(old_value, "Graph_Graph4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph4"):
                opp_val = getattr(value, "Graph_Graph4", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_TString:

    def __init__(self, id: str, name: str, Graph_TString: "Graph_Graph" = None, Graph_TString21: "Graph_ID1006" = None):
        self.id = id
        self.name = name
        self.Graph_TString = Graph_TString
        self.Graph_TString21 = Graph_TString21
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Graph_TString21(self):
        return self.__Graph_TString21

    @Graph_TString21.setter
    def Graph_TString21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TString__Graph_TString21", None)
        self.__Graph_TString21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_ID100620"):
                opp_val = getattr(old_value, "Graph_ID100620", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_ID100620"):
                opp_val = getattr(value, "Graph_ID100620", None)
                if opp_val is None:
                    setattr(value, "Graph_ID100620", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Graph_TString(self):
        return self.__Graph_TString

    @Graph_TString.setter
    def Graph_TString(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TString__Graph_TString", None)
        self.__Graph_TString = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph18"):
                opp_val = getattr(old_value, "Graph_Graph18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph18"):
                opp_val = getattr(value, "Graph_Graph18", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_TDouble:

    def __init__(self, value: float, Graph_TDouble: "Graph_Graph" = None):
        self.value = value
        self.Graph_TDouble = Graph_TDouble
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


    @property
    def Graph_TDouble(self):
        return self.__Graph_TDouble

    @Graph_TDouble.setter
    def Graph_TDouble(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TDouble__Graph_TDouble", None)
        self.__Graph_TDouble = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph16"):
                opp_val = getattr(old_value, "Graph_Graph16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph16"):
                opp_val = getattr(value, "Graph_Graph16", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_TFloat:

    def __init__(self, value: float, Graph_TFloat: "Graph_Graph" = None):
        self.value = value
        self.Graph_TFloat = Graph_TFloat
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value


    @property
    def Graph_TFloat(self):
        return self.__Graph_TFloat

    @Graph_TFloat.setter
    def Graph_TFloat(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TFloat__Graph_TFloat", None)
        self.__Graph_TFloat = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph14"):
                opp_val = getattr(old_value, "Graph_Graph14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph14"):
                opp_val = getattr(value, "Graph_Graph14", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_TBoolean:

    def __init__(self, value: bool, Graph_TBoolean: "Graph_Graph" = None):
        self.value = value
        self.Graph_TBoolean = Graph_TBoolean
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: bool):
        self.__value = value


    @property
    def Graph_TBoolean(self):
        return self.__Graph_TBoolean

    @Graph_TBoolean.setter
    def Graph_TBoolean(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_TBoolean__Graph_TBoolean", None)
        self.__Graph_TBoolean = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph2"):
                opp_val = getattr(old_value, "Graph_Graph2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph2"):
                opp_val = getattr(value, "Graph_Graph2", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_ID1006:

    def __init__(self, id: str, name: str, Graph_ID1006: "Graph_Graph" = None, Graph_ID100620: set["Graph_TString"] = None):
        self.id = id
        self.name = name
        self.Graph_ID1006 = Graph_ID1006
        self.Graph_ID100620 = Graph_ID100620 if Graph_ID100620 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def Graph_ID100620(self):
        return self.__Graph_ID100620

    @Graph_ID100620.setter
    def Graph_ID100620(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_ID1006__Graph_ID100620", None)
        self.__Graph_ID100620 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TString21"):
                    opp_val = getattr(item, "Graph_TString21", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TString21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TString21"):
                    opp_val = getattr(item, "Graph_TString21", None)
                    
                    setattr(item, "Graph_TString21", self)
                    

    @property
    def Graph_ID1006(self):
        return self.__Graph_ID1006

    @Graph_ID1006.setter
    def Graph_ID1006(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_ID1006__Graph_ID1006", None)
        self.__Graph_ID1006 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Graph_Graph"):
                opp_val = getattr(old_value, "Graph_Graph", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Graph_Graph"):
                opp_val = getattr(value, "Graph_Graph", None)
                if opp_val is None:
                    setattr(value, "Graph_Graph", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Graph_Graph:

    def __init__(self, id: str, Graph_Graph: set["Graph_ID1006"] = None, Graph_Graph12: set["Graph_TLong"] = None, Graph_Graph14: set["Graph_TFloat"] = None, Graph_Graph16: set["Graph_TDouble"] = None, Graph_Graph2: set["Graph_TBoolean"] = None, Graph_Graph4: set["Graph_TChar"] = None, Graph_Graph6: set["Graph_TByte"] = None, Graph_Graph8: set["Graph_TShort"] = None, Graph_Graph10: set["Graph_TInt"] = None, Graph_Graph18: set["Graph_TString"] = None):
        self.id = id
        self.Graph_Graph = Graph_Graph if Graph_Graph is not None else set()
        self.Graph_Graph12 = Graph_Graph12 if Graph_Graph12 is not None else set()
        self.Graph_Graph14 = Graph_Graph14 if Graph_Graph14 is not None else set()
        self.Graph_Graph16 = Graph_Graph16 if Graph_Graph16 is not None else set()
        self.Graph_Graph2 = Graph_Graph2 if Graph_Graph2 is not None else set()
        self.Graph_Graph4 = Graph_Graph4 if Graph_Graph4 is not None else set()
        self.Graph_Graph6 = Graph_Graph6 if Graph_Graph6 is not None else set()
        self.Graph_Graph8 = Graph_Graph8 if Graph_Graph8 is not None else set()
        self.Graph_Graph10 = Graph_Graph10 if Graph_Graph10 is not None else set()
        self.Graph_Graph18 = Graph_Graph18 if Graph_Graph18 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def Graph_Graph2(self):
        return self.__Graph_Graph2

    @Graph_Graph2.setter
    def Graph_Graph2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph2", None)
        self.__Graph_Graph2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TBoolean"):
                    opp_val = getattr(item, "Graph_TBoolean", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TBoolean", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TBoolean"):
                    opp_val = getattr(item, "Graph_TBoolean", None)
                    
                    setattr(item, "Graph_TBoolean", self)
                    

    @property
    def Graph_Graph4(self):
        return self.__Graph_Graph4

    @Graph_Graph4.setter
    def Graph_Graph4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph4", None)
        self.__Graph_Graph4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TChar"):
                    opp_val = getattr(item, "Graph_TChar", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TChar", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TChar"):
                    opp_val = getattr(item, "Graph_TChar", None)
                    
                    setattr(item, "Graph_TChar", self)
                    

    @property
    def Graph_Graph6(self):
        return self.__Graph_Graph6

    @Graph_Graph6.setter
    def Graph_Graph6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph6", None)
        self.__Graph_Graph6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TByte"):
                    opp_val = getattr(item, "Graph_TByte", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TByte", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TByte"):
                    opp_val = getattr(item, "Graph_TByte", None)
                    
                    setattr(item, "Graph_TByte", self)
                    

    @property
    def Graph_Graph12(self):
        return self.__Graph_Graph12

    @Graph_Graph12.setter
    def Graph_Graph12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph12", None)
        self.__Graph_Graph12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TLong"):
                    opp_val = getattr(item, "Graph_TLong", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TLong", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TLong"):
                    opp_val = getattr(item, "Graph_TLong", None)
                    
                    setattr(item, "Graph_TLong", self)
                    

    @property
    def Graph_Graph16(self):
        return self.__Graph_Graph16

    @Graph_Graph16.setter
    def Graph_Graph16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph16", None)
        self.__Graph_Graph16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TDouble"):
                    opp_val = getattr(item, "Graph_TDouble", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TDouble", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TDouble"):
                    opp_val = getattr(item, "Graph_TDouble", None)
                    
                    setattr(item, "Graph_TDouble", self)
                    

    @property
    def Graph_Graph14(self):
        return self.__Graph_Graph14

    @Graph_Graph14.setter
    def Graph_Graph14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph14", None)
        self.__Graph_Graph14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TFloat"):
                    opp_val = getattr(item, "Graph_TFloat", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TFloat", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TFloat"):
                    opp_val = getattr(item, "Graph_TFloat", None)
                    
                    setattr(item, "Graph_TFloat", self)
                    

    @property
    def Graph_Graph10(self):
        return self.__Graph_Graph10

    @Graph_Graph10.setter
    def Graph_Graph10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph10", None)
        self.__Graph_Graph10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TInt"):
                    opp_val = getattr(item, "Graph_TInt", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TInt", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TInt"):
                    opp_val = getattr(item, "Graph_TInt", None)
                    
                    setattr(item, "Graph_TInt", self)
                    

    @property
    def Graph_Graph8(self):
        return self.__Graph_Graph8

    @Graph_Graph8.setter
    def Graph_Graph8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph8", None)
        self.__Graph_Graph8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TShort"):
                    opp_val = getattr(item, "Graph_TShort", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TShort", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TShort"):
                    opp_val = getattr(item, "Graph_TShort", None)
                    
                    setattr(item, "Graph_TShort", self)
                    

    @property
    def Graph_Graph18(self):
        return self.__Graph_Graph18

    @Graph_Graph18.setter
    def Graph_Graph18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph18", None)
        self.__Graph_Graph18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_TString"):
                    opp_val = getattr(item, "Graph_TString", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_TString", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_TString"):
                    opp_val = getattr(item, "Graph_TString", None)
                    
                    setattr(item, "Graph_TString", self)
                    

    @property
    def Graph_Graph(self):
        return self.__Graph_Graph

    @Graph_Graph.setter
    def Graph_Graph(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Graph_Graph__Graph_Graph", None)
        self.__Graph_Graph = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Graph_ID1006"):
                    opp_val = getattr(item, "Graph_ID1006", None)
                    
                    if opp_val == self:
                        setattr(item, "Graph_ID1006", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Graph_ID1006"):
                    opp_val = getattr(item, "Graph_ID1006", None)
                    
                    setattr(item, "Graph_ID1006", self)
                    
