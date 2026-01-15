from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class df_Expression:

    pass
class df_Tag:

    def __init__(self, identifiers: str, df_Tag: "df_Action" = None):
        self.identifiers = identifiers
        self.df_Tag = df_Tag
        
    @property
    def identifiers(self) -> str:
        return self.__identifiers

    @identifiers.setter
    def identifiers(self, identifiers: str):
        self.__identifiers = identifiers

    @property
    def df_Tag(self):
        return self.__df_Tag

    @df_Tag.setter
    def df_Tag(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Tag__df_Tag", None)
        self.__df_Tag = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Action77"):
                opp_val = getattr(old_value, "df_Action77", None)
                if opp_val == self:
                    setattr(old_value, "df_Action77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Action77"):
                opp_val = getattr(value, "df_Action77", None)
                setattr(value, "df_Action77", self)

class df_VarToPortMapEntry:

    pass
class df_PortToVarMapEntry:

    pass
class df_PortToEIntegerObjectMapEntry:

    def __init__(self, value: str, df_PortToEIntegerObjectMapEntry: "df_Pattern" = None, df_PortToEIntegerObjectMapEntry95: "df_Port" = None):
        self.value = value
        self.df_PortToEIntegerObjectMapEntry = df_PortToEIntegerObjectMapEntry
        self.df_PortToEIntegerObjectMapEntry95 = df_PortToEIntegerObjectMapEntry95
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def df_PortToEIntegerObjectMapEntry(self):
        return self.__df_PortToEIntegerObjectMapEntry

    @df_PortToEIntegerObjectMapEntry.setter
    def df_PortToEIntegerObjectMapEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_PortToEIntegerObjectMapEntry__df_PortToEIntegerObjectMapEntry", None)
        self.__df_PortToEIntegerObjectMapEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Pattern81"):
                opp_val = getattr(old_value, "df_Pattern81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Pattern81"):
                opp_val = getattr(value, "df_Pattern81", None)
                if opp_val is None:
                    setattr(value, "df_Pattern81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def df_PortToEIntegerObjectMapEntry95(self):
        return self.__df_PortToEIntegerObjectMapEntry95

    @df_PortToEIntegerObjectMapEntry95.setter
    def df_PortToEIntegerObjectMapEntry95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_PortToEIntegerObjectMapEntry__df_PortToEIntegerObjectMapEntry95", None)
        self.__df_PortToEIntegerObjectMapEntry95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Port96"):
                opp_val = getattr(old_value, "df_Port96", None)
                if opp_val == self:
                    setattr(old_value, "df_Port96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Port96"):
                opp_val = getattr(value, "df_Port96", None)
                setattr(value, "df_Port96", self)

class Edge:

    pass
class df_Transition(Edge):

    pass
class df_Connection(Edge):

    pass
class df_Pattern:

    pass
class Graph:

    pass
class df_Vertex:

    pass
class df_MoC:

    pass
class df_FSM(Graph):

    pass
class Vertex:

    pass
class df_State(Vertex):

    pass
class df_Port(Vertex):

    def __init__(self, numTokensProduced: int, name: str, numTokensConsumed: int, df_Port: "df_Type" = None, df_Port8: "df_Entity" = None, df_Port11: "df_Entity" = None, df_Port31: "df_Actor" = None, df_Port26: "df_Actor" = None, df_Port44: "df_Network" = None, df_Port50: "df_Network" = None, df_Port58: "df_Connection" = None, df_Port61: "df_Connection" = None, df_Port84: "df_Pattern" = None, df_Port99: "df_PortToVarMapEntry" = None, df_Port108: "df_VarToPortMapEntry" = None, df_Port96: "df_PortToEIntegerObjectMapEntry" = None):
        self.numTokensProduced = numTokensProduced
        self.name = name
        self.numTokensConsumed = numTokensConsumed
        self.df_Port = df_Port
        self.df_Port8 = df_Port8
        self.df_Port11 = df_Port11
        self.df_Port31 = df_Port31
        self.df_Port26 = df_Port26
        self.df_Port44 = df_Port44
        self.df_Port50 = df_Port50
        self.df_Port58 = df_Port58
        self.df_Port61 = df_Port61
        self.df_Port84 = df_Port84
        self.df_Port99 = df_Port99
        self.df_Port108 = df_Port108
        self.df_Port96 = df_Port96
        
    @property
    def numTokensConsumed(self) -> int:
        return self.__numTokensConsumed

    @numTokensConsumed.setter
    def numTokensConsumed(self, numTokensConsumed: int):
        self.__numTokensConsumed = numTokensConsumed

    @property
    def numTokensProduced(self) -> int:
        return self.__numTokensProduced

    @numTokensProduced.setter
    def numTokensProduced(self, numTokensProduced: int):
        self.__numTokensProduced = numTokensProduced

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def df_Port50(self):
        return self.__df_Port50

    @df_Port50.setter
    def df_Port50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port50", None)
        self.__df_Port50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Network49"):
                opp_val = getattr(old_value, "df_Network49", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Network49"):
                opp_val = getattr(value, "df_Network49", None)
                if opp_val is None:
                    setattr(value, "df_Network49", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def df_Port44(self):
        return self.__df_Port44

    @df_Port44.setter
    def df_Port44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port44", None)
        self.__df_Port44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Network43"):
                opp_val = getattr(old_value, "df_Network43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Network43"):
                opp_val = getattr(value, "df_Network43", None)
                if opp_val is None:
                    setattr(value, "df_Network43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def df_Port11(self):
        return self.__df_Port11

    @df_Port11.setter
    def df_Port11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port11", None)
        self.__df_Port11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Entity10"):
                opp_val = getattr(old_value, "df_Entity10", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Entity10"):
                opp_val = getattr(value, "df_Entity10", None)
                if opp_val is None:
                    setattr(value, "df_Entity10", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def df_Port84(self):
        return self.__df_Port84

    @df_Port84.setter
    def df_Port84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port84", None)
        self.__df_Port84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Pattern83"):
                opp_val = getattr(old_value, "df_Pattern83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Pattern83"):
                opp_val = getattr(value, "df_Pattern83", None)
                if opp_val is None:
                    setattr(value, "df_Pattern83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def df_Port61(self):
        return self.__df_Port61

    @df_Port61.setter
    def df_Port61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port61", None)
        self.__df_Port61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Connection60"):
                opp_val = getattr(old_value, "df_Connection60", None)
                if opp_val == self:
                    setattr(old_value, "df_Connection60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Connection60"):
                opp_val = getattr(value, "df_Connection60", None)
                setattr(value, "df_Connection60", self)

    @property
    def df_Port31(self):
        return self.__df_Port31

    @df_Port31.setter
    def df_Port31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port31", None)
        self.__df_Port31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Actor30"):
                opp_val = getattr(old_value, "df_Actor30", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Actor30"):
                opp_val = getattr(value, "df_Actor30", None)
                if opp_val is None:
                    setattr(value, "df_Actor30", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def df_Port(self):
        return self.__df_Port

    @df_Port.setter
    def df_Port(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port", None)
        self.__df_Port = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Type"):
                opp_val = getattr(old_value, "df_Type", None)
                if opp_val == self:
                    setattr(old_value, "df_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Type"):
                opp_val = getattr(value, "df_Type", None)
                setattr(value, "df_Type", self)

    @property
    def df_Port58(self):
        return self.__df_Port58

    @df_Port58.setter
    def df_Port58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port58", None)
        self.__df_Port58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Connection"):
                opp_val = getattr(old_value, "df_Connection", None)
                if opp_val == self:
                    setattr(old_value, "df_Connection", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Connection"):
                opp_val = getattr(value, "df_Connection", None)
                setattr(value, "df_Connection", self)

    @property
    def df_Port26(self):
        return self.__df_Port26

    @df_Port26.setter
    def df_Port26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port26", None)
        self.__df_Port26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Actor25"):
                opp_val = getattr(old_value, "df_Actor25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Actor25"):
                opp_val = getattr(value, "df_Actor25", None)
                if opp_val is None:
                    setattr(value, "df_Actor25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def df_Port96(self):
        return self.__df_Port96

    @df_Port96.setter
    def df_Port96(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port96", None)
        self.__df_Port96 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_PortToEIntegerObjectMapEntry95"):
                opp_val = getattr(old_value, "df_PortToEIntegerObjectMapEntry95", None)
                if opp_val == self:
                    setattr(old_value, "df_PortToEIntegerObjectMapEntry95", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_PortToEIntegerObjectMapEntry95"):
                opp_val = getattr(value, "df_PortToEIntegerObjectMapEntry95", None)
                setattr(value, "df_PortToEIntegerObjectMapEntry95", self)

    @property
    def df_Port108(self):
        return self.__df_Port108

    @df_Port108.setter
    def df_Port108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port108", None)
        self.__df_Port108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_VarToPortMapEntry107"):
                opp_val = getattr(old_value, "df_VarToPortMapEntry107", None)
                if opp_val == self:
                    setattr(old_value, "df_VarToPortMapEntry107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_VarToPortMapEntry107"):
                opp_val = getattr(value, "df_VarToPortMapEntry107", None)
                setattr(value, "df_VarToPortMapEntry107", self)

    @property
    def df_Port99(self):
        return self.__df_Port99

    @df_Port99.setter
    def df_Port99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port99", None)
        self.__df_Port99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_PortToVarMapEntry98"):
                opp_val = getattr(old_value, "df_PortToVarMapEntry98", None)
                if opp_val == self:
                    setattr(old_value, "df_PortToVarMapEntry98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_PortToVarMapEntry98"):
                opp_val = getattr(value, "df_PortToVarMapEntry98", None)
                setattr(value, "df_PortToVarMapEntry98", self)

    @property
    def df_Port8(self):
        return self.__df_Port8

    @df_Port8.setter
    def df_Port8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Port__df_Port8", None)
        self.__df_Port8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_Entity"):
                opp_val = getattr(old_value, "df_Entity", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_Entity"):
                opp_val = getattr(value, "df_Entity", None)
                if opp_val is None:
                    setattr(value, "df_Entity", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class df_Procedure:

    pass
class df_EObject:

    pass
class df_Argument:

    pass
class Adaptable:

    pass
class df_Network(Graph, Adaptable):

    def __init__(self, fileName: str, name: str, df_Network: set["df_Vertex"] = None, df_Network43: set["df_Port"] = None, df_Network46: "df_MoC" = None, df_Network49: set["df_Port"] = None, df_Network52: set["df_Var"] = None, df_Network55: set["df_Var"] = None):
        self.fileName = fileName
        self.name = name
        self.df_Network = df_Network if df_Network is not None else set()
        self.df_Network43 = df_Network43 if df_Network43 is not None else set()
        self.df_Network46 = df_Network46
        self.df_Network49 = df_Network49 if df_Network49 is not None else set()
        self.df_Network52 = df_Network52 if df_Network52 is not None else set()
        self.df_Network55 = df_Network55 if df_Network55 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def df_Network46(self):
        return self.__df_Network46

    @df_Network46.setter
    def df_Network46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Network__df_Network46", None)
        self.__df_Network46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_MoC47"):
                opp_val = getattr(old_value, "df_MoC47", None)
                if opp_val == self:
                    setattr(old_value, "df_MoC47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_MoC47"):
                opp_val = getattr(value, "df_MoC47", None)
                setattr(value, "df_MoC47", self)

    @property
    def df_Network49(self):
        return self.__df_Network49

    @df_Network49.setter
    def df_Network49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Network__df_Network49", None)
        self.__df_Network49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Port50"):
                    opp_val = getattr(item, "df_Port50", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Port50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Port50"):
                    opp_val = getattr(item, "df_Port50", None)
                    
                    setattr(item, "df_Port50", self)
                    

    @property
    def df_Network(self):
        return self.__df_Network

    @df_Network.setter
    def df_Network(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Network__df_Network", None)
        self.__df_Network = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Vertex"):
                    opp_val = getattr(item, "df_Vertex", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Vertex", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Vertex"):
                    opp_val = getattr(item, "df_Vertex", None)
                    
                    setattr(item, "df_Vertex", self)
                    

    @property
    def df_Network52(self):
        return self.__df_Network52

    @df_Network52.setter
    def df_Network52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Network__df_Network52", None)
        self.__df_Network52 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Var53"):
                    opp_val = getattr(item, "df_Var53", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Var53", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Var53"):
                    opp_val = getattr(item, "df_Var53", None)
                    
                    setattr(item, "df_Var53", self)
                    

    @property
    def df_Network55(self):
        return self.__df_Network55

    @df_Network55.setter
    def df_Network55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Network__df_Network55", None)
        self.__df_Network55 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Var56"):
                    opp_val = getattr(item, "df_Var56", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Var56", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Var56"):
                    opp_val = getattr(item, "df_Var56", None)
                    
                    setattr(item, "df_Var56", self)
                    

    @property
    def df_Network43(self):
        return self.__df_Network43

    @df_Network43.setter
    def df_Network43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Network__df_Network43", None)
        self.__df_Network43 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Port44"):
                    opp_val = getattr(item, "df_Port44", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Port44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Port44"):
                    opp_val = getattr(item, "df_Port44", None)
                    
                    setattr(item, "df_Port44", self)
                    

class df_Actor(Vertex, Adaptable):

    def __init__(self, fileName: str, native: bool, name: str, lineNumber: int, df_Actor: set["df_Action"] = None, df_Actor17: set["df_Action"] = None, df_Actor20: "df_FSM" = None, df_Actor22: set["df_Action"] = None, df_Actor28: "df_MoC" = None, df_Actor30: set["df_Port"] = None, df_Actor33: set["df_Var"] = None, df_Actor36: set["df_Procedure"] = None, df_Actor25: set["df_Port"] = None, df_Actor39: set["df_Var"] = None):
        self.fileName = fileName
        self.native = native
        self.name = name
        self.lineNumber = lineNumber
        self.df_Actor = df_Actor if df_Actor is not None else set()
        self.df_Actor17 = df_Actor17 if df_Actor17 is not None else set()
        self.df_Actor20 = df_Actor20
        self.df_Actor22 = df_Actor22 if df_Actor22 is not None else set()
        self.df_Actor28 = df_Actor28
        self.df_Actor30 = df_Actor30 if df_Actor30 is not None else set()
        self.df_Actor33 = df_Actor33 if df_Actor33 is not None else set()
        self.df_Actor36 = df_Actor36 if df_Actor36 is not None else set()
        self.df_Actor25 = df_Actor25 if df_Actor25 is not None else set()
        self.df_Actor39 = df_Actor39 if df_Actor39 is not None else set()
        
    @property
    def native(self) -> bool:
        return self.__native

    @native.setter
    def native(self, native: bool):
        self.__native = native

    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def lineNumber(self) -> int:
        return self.__lineNumber

    @lineNumber.setter
    def lineNumber(self, lineNumber: int):
        self.__lineNumber = lineNumber

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def df_Actor17(self):
        return self.__df_Actor17

    @df_Actor17.setter
    def df_Actor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor17", None)
        self.__df_Actor17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Action18"):
                    opp_val = getattr(item, "df_Action18", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Action18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Action18"):
                    opp_val = getattr(item, "df_Action18", None)
                    
                    setattr(item, "df_Action18", self)
                    

    @property
    def df_Actor25(self):
        return self.__df_Actor25

    @df_Actor25.setter
    def df_Actor25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor25", None)
        self.__df_Actor25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Port26"):
                    opp_val = getattr(item, "df_Port26", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Port26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Port26"):
                    opp_val = getattr(item, "df_Port26", None)
                    
                    setattr(item, "df_Port26", self)
                    

    @property
    def df_Actor22(self):
        return self.__df_Actor22

    @df_Actor22.setter
    def df_Actor22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor22", None)
        self.__df_Actor22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Action23"):
                    opp_val = getattr(item, "df_Action23", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Action23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Action23"):
                    opp_val = getattr(item, "df_Action23", None)
                    
                    setattr(item, "df_Action23", self)
                    

    @property
    def df_Actor39(self):
        return self.__df_Actor39

    @df_Actor39.setter
    def df_Actor39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor39", None)
        self.__df_Actor39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Var40"):
                    opp_val = getattr(item, "df_Var40", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Var40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Var40"):
                    opp_val = getattr(item, "df_Var40", None)
                    
                    setattr(item, "df_Var40", self)
                    

    @property
    def df_Actor30(self):
        return self.__df_Actor30

    @df_Actor30.setter
    def df_Actor30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor30", None)
        self.__df_Actor30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Port31"):
                    opp_val = getattr(item, "df_Port31", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Port31", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Port31"):
                    opp_val = getattr(item, "df_Port31", None)
                    
                    setattr(item, "df_Port31", self)
                    

    @property
    def df_Actor(self):
        return self.__df_Actor

    @df_Actor.setter
    def df_Actor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor", None)
        self.__df_Actor = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Action"):
                    opp_val = getattr(item, "df_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Action"):
                    opp_val = getattr(item, "df_Action", None)
                    
                    setattr(item, "df_Action", self)
                    

    @property
    def df_Actor33(self):
        return self.__df_Actor33

    @df_Actor33.setter
    def df_Actor33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor33", None)
        self.__df_Actor33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Var34"):
                    opp_val = getattr(item, "df_Var34", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Var34", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Var34"):
                    opp_val = getattr(item, "df_Var34", None)
                    
                    setattr(item, "df_Var34", self)
                    

    @property
    def df_Actor36(self):
        return self.__df_Actor36

    @df_Actor36.setter
    def df_Actor36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor36", None)
        self.__df_Actor36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Procedure37"):
                    opp_val = getattr(item, "df_Procedure37", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Procedure37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Procedure37"):
                    opp_val = getattr(item, "df_Procedure37", None)
                    
                    setattr(item, "df_Procedure37", self)
                    

    @property
    def df_Actor20(self):
        return self.__df_Actor20

    @df_Actor20.setter
    def df_Actor20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor20", None)
        self.__df_Actor20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_FSM"):
                opp_val = getattr(old_value, "df_FSM", None)
                if opp_val == self:
                    setattr(old_value, "df_FSM", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_FSM"):
                opp_val = getattr(value, "df_FSM", None)
                setattr(value, "df_FSM", self)

    @property
    def df_Actor28(self):
        return self.__df_Actor28

    @df_Actor28.setter
    def df_Actor28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Actor__df_Actor28", None)
        self.__df_Actor28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_MoC"):
                opp_val = getattr(old_value, "df_MoC", None)
                if opp_val == self:
                    setattr(old_value, "df_MoC", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_MoC"):
                opp_val = getattr(value, "df_MoC", None)
                setattr(value, "df_MoC", self)

class df_Instance(Vertex, Adaptable):

    def __init__(self, name: str, df_Instance: set["df_Argument"] = None, df_Instance6: "df_EObject" = None):
        self.name = name
        self.df_Instance = df_Instance if df_Instance is not None else set()
        self.df_Instance6 = df_Instance6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def df_Instance(self):
        return self.__df_Instance

    @df_Instance.setter
    def df_Instance(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Instance__df_Instance", None)
        self.__df_Instance = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Argument"):
                    opp_val = getattr(item, "df_Argument", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Argument", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Argument"):
                    opp_val = getattr(item, "df_Argument", None)
                    
                    setattr(item, "df_Argument", self)
                    

    @property
    def df_Instance6(self):
        return self.__df_Instance6

    @df_Instance6.setter
    def df_Instance6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Instance__df_Instance6", None)
        self.__df_Instance6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "df_EObject"):
                opp_val = getattr(old_value, "df_EObject", None)
                if opp_val == self:
                    setattr(old_value, "df_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "df_EObject"):
                opp_val = getattr(value, "df_EObject", None)
                setattr(value, "df_EObject", self)

class df_Type:

    pass
class df_Var:

    pass
class Attributable:

    pass
class df_Action(Attributable):

    pass
class df_Entity(Adaptable, Attributable):

    def __init__(self, incomingPortMap: str, name: str, outgoingPortMap: str, df_Entity: set["df_Port"] = None, df_Entity13: set["df_Var"] = None, df_Entity10: set["df_Port"] = None):
        self.incomingPortMap = incomingPortMap
        self.name = name
        self.outgoingPortMap = outgoingPortMap
        self.df_Entity = df_Entity if df_Entity is not None else set()
        self.df_Entity13 = df_Entity13 if df_Entity13 is not None else set()
        self.df_Entity10 = df_Entity10 if df_Entity10 is not None else set()
        
    @property
    def outgoingPortMap(self) -> str:
        return self.__outgoingPortMap

    @outgoingPortMap.setter
    def outgoingPortMap(self, outgoingPortMap: str):
        self.__outgoingPortMap = outgoingPortMap

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def incomingPortMap(self) -> str:
        return self.__incomingPortMap

    @incomingPortMap.setter
    def incomingPortMap(self, incomingPortMap: str):
        self.__incomingPortMap = incomingPortMap

    @property
    def df_Entity10(self):
        return self.__df_Entity10

    @df_Entity10.setter
    def df_Entity10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Entity__df_Entity10", None)
        self.__df_Entity10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Port11"):
                    opp_val = getattr(item, "df_Port11", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Port11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Port11"):
                    opp_val = getattr(item, "df_Port11", None)
                    
                    setattr(item, "df_Port11", self)
                    

    @property
    def df_Entity(self):
        return self.__df_Entity

    @df_Entity.setter
    def df_Entity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Entity__df_Entity", None)
        self.__df_Entity = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Port8"):
                    opp_val = getattr(item, "df_Port8", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Port8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Port8"):
                    opp_val = getattr(item, "df_Port8", None)
                    
                    setattr(item, "df_Port8", self)
                    

    @property
    def df_Entity13(self):
        return self.__df_Entity13

    @df_Entity13.setter
    def df_Entity13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Entity__df_Entity13", None)
        self.__df_Entity13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Var14"):
                    opp_val = getattr(item, "df_Var14", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Var14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Var14"):
                    opp_val = getattr(item, "df_Var14", None)
                    
                    setattr(item, "df_Var14", self)
                    

class df_Unit(Attributable):

    def __init__(self, fileName: str, lineNumber: int, name: str, df_Unit: set["df_Var"] = None, df_Unit2: set["df_Procedure"] = None):
        self.fileName = fileName
        self.lineNumber = lineNumber
        self.name = name
        self.df_Unit = df_Unit if df_Unit is not None else set()
        self.df_Unit2 = df_Unit2 if df_Unit2 is not None else set()
        
    @property
    def fileName(self) -> str:
        return self.__fileName

    @fileName.setter
    def fileName(self, fileName: str):
        self.__fileName = fileName

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def lineNumber(self) -> int:
        return self.__lineNumber

    @lineNumber.setter
    def lineNumber(self, lineNumber: int):
        self.__lineNumber = lineNumber

    @property
    def df_Unit(self):
        return self.__df_Unit

    @df_Unit.setter
    def df_Unit(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Unit__df_Unit", None)
        self.__df_Unit = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Var"):
                    opp_val = getattr(item, "df_Var", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Var", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Var"):
                    opp_val = getattr(item, "df_Var", None)
                    
                    setattr(item, "df_Var", self)
                    

    @property
    def df_Unit2(self):
        return self.__df_Unit2

    @df_Unit2.setter
    def df_Unit2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_df_Unit__df_Unit2", None)
        self.__df_Unit2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "df_Procedure"):
                    opp_val = getattr(item, "df_Procedure", None)
                    
                    if opp_val == self:
                        setattr(item, "df_Procedure", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "df_Procedure"):
                    opp_val = getattr(item, "df_Procedure", None)
                    
                    setattr(item, "df_Procedure", self)
                    
