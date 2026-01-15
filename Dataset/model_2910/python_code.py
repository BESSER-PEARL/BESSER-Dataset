from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class agentDSL_Goal:

    def __init__(self, name: str, agentDSL_Goal: "agentDSL_Outcome" = None, agentDSL_Goal16: set["agentDSL_Attribute"] = None):
        self.name = name
        self.agentDSL_Goal = agentDSL_Goal
        self.agentDSL_Goal16 = agentDSL_Goal16 if agentDSL_Goal16 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def agentDSL_Goal(self):
        return self.__agentDSL_Goal

    @agentDSL_Goal.setter
    def agentDSL_Goal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Goal__agentDSL_Goal", None)
        self.__agentDSL_Goal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Outcome14"):
                opp_val = getattr(old_value, "agentDSL_Outcome14", None)
                if opp_val == self:
                    setattr(old_value, "agentDSL_Outcome14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Outcome14"):
                opp_val = getattr(value, "agentDSL_Outcome14", None)
                setattr(value, "agentDSL_Outcome14", self)

    @property
    def agentDSL_Goal16(self):
        return self.__agentDSL_Goal16

    @agentDSL_Goal16.setter
    def agentDSL_Goal16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Goal__agentDSL_Goal16", None)
        self.__agentDSL_Goal16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "agentDSL_Attribute17"):
                    opp_val = getattr(item, "agentDSL_Attribute17", None)
                    
                    if opp_val == self:
                        setattr(item, "agentDSL_Attribute17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "agentDSL_Attribute17"):
                    opp_val = getattr(item, "agentDSL_Attribute17", None)
                    
                    setattr(item, "agentDSL_Attribute17", self)
                    

class agentDSL_Attribute:

    def __init__(self, many: bool, name: str, agentDSL_Attribute: "agentDSL_Entity" = None, agentDSL_Attribute7: "agentDSL_Task" = None, agentDSL_Attribute21: "agentDSL_Type" = None, agentDSL_Attribute12: "agentDSL_Outcome" = None, agentDSL_Attribute17: "agentDSL_Goal" = None, agentDSL_Attribute19: "agentDSL_Function" = None):
        self.many = many
        self.name = name
        self.agentDSL_Attribute = agentDSL_Attribute
        self.agentDSL_Attribute7 = agentDSL_Attribute7
        self.agentDSL_Attribute21 = agentDSL_Attribute21
        self.agentDSL_Attribute12 = agentDSL_Attribute12
        self.agentDSL_Attribute17 = agentDSL_Attribute17
        self.agentDSL_Attribute19 = agentDSL_Attribute19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def many(self) -> bool:
        return self.__many

    @many.setter
    def many(self, many: bool):
        self.__many = many

    @property
    def agentDSL_Attribute12(self):
        return self.__agentDSL_Attribute12

    @agentDSL_Attribute12.setter
    def agentDSL_Attribute12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Attribute__agentDSL_Attribute12", None)
        self.__agentDSL_Attribute12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Outcome11"):
                opp_val = getattr(old_value, "agentDSL_Outcome11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Outcome11"):
                opp_val = getattr(value, "agentDSL_Outcome11", None)
                if opp_val is None:
                    setattr(value, "agentDSL_Outcome11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def agentDSL_Attribute(self):
        return self.__agentDSL_Attribute

    @agentDSL_Attribute.setter
    def agentDSL_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Attribute__agentDSL_Attribute", None)
        self.__agentDSL_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Entity5"):
                opp_val = getattr(old_value, "agentDSL_Entity5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Entity5"):
                opp_val = getattr(value, "agentDSL_Entity5", None)
                if opp_val is None:
                    setattr(value, "agentDSL_Entity5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def agentDSL_Attribute19(self):
        return self.__agentDSL_Attribute19

    @agentDSL_Attribute19.setter
    def agentDSL_Attribute19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Attribute__agentDSL_Attribute19", None)
        self.__agentDSL_Attribute19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Function"):
                opp_val = getattr(old_value, "agentDSL_Function", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Function"):
                opp_val = getattr(value, "agentDSL_Function", None)
                if opp_val is None:
                    setattr(value, "agentDSL_Function", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def agentDSL_Attribute17(self):
        return self.__agentDSL_Attribute17

    @agentDSL_Attribute17.setter
    def agentDSL_Attribute17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Attribute__agentDSL_Attribute17", None)
        self.__agentDSL_Attribute17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Goal16"):
                opp_val = getattr(old_value, "agentDSL_Goal16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Goal16"):
                opp_val = getattr(value, "agentDSL_Goal16", None)
                if opp_val is None:
                    setattr(value, "agentDSL_Goal16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def agentDSL_Attribute7(self):
        return self.__agentDSL_Attribute7

    @agentDSL_Attribute7.setter
    def agentDSL_Attribute7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Attribute__agentDSL_Attribute7", None)
        self.__agentDSL_Attribute7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Task"):
                opp_val = getattr(old_value, "agentDSL_Task", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Task"):
                opp_val = getattr(value, "agentDSL_Task", None)
                if opp_val is None:
                    setattr(value, "agentDSL_Task", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def agentDSL_Attribute21(self):
        return self.__agentDSL_Attribute21

    @agentDSL_Attribute21.setter
    def agentDSL_Attribute21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Attribute__agentDSL_Attribute21", None)
        self.__agentDSL_Attribute21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Type22"):
                opp_val = getattr(old_value, "agentDSL_Type22", None)
                if opp_val == self:
                    setattr(old_value, "agentDSL_Type22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Type22"):
                opp_val = getattr(value, "agentDSL_Type22", None)
                setattr(value, "agentDSL_Type22", self)

class agentDSL_Type:

    def __init__(self, name: str, agentDSL_Type: "agentDSL_Model" = None, agentDSL_Type22: "agentDSL_Attribute" = None):
        self.name = name
        self.agentDSL_Type = agentDSL_Type
        self.agentDSL_Type22 = agentDSL_Type22
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def agentDSL_Type22(self):
        return self.__agentDSL_Type22

    @agentDSL_Type22.setter
    def agentDSL_Type22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Type__agentDSL_Type22", None)
        self.__agentDSL_Type22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Attribute21"):
                opp_val = getattr(old_value, "agentDSL_Attribute21", None)
                if opp_val == self:
                    setattr(old_value, "agentDSL_Attribute21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Attribute21"):
                opp_val = getattr(value, "agentDSL_Attribute21", None)
                setattr(value, "agentDSL_Attribute21", self)

    @property
    def agentDSL_Type(self):
        return self.__agentDSL_Type

    @agentDSL_Type.setter
    def agentDSL_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_Type__agentDSL_Type", None)
        self.__agentDSL_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_Model"):
                opp_val = getattr(old_value, "agentDSL_Model", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_Model"):
                opp_val = getattr(value, "agentDSL_Model", None)
                if opp_val is None:
                    setattr(value, "agentDSL_Model", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class agentDSL_Model:

    pass
class agentDSL_JAVAID:

    def __init__(self, name: str, agentDSL_JAVAID: "agentDSL_TypeDef" = None):
        self.name = name
        self.agentDSL_JAVAID = agentDSL_JAVAID
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def agentDSL_JAVAID(self):
        return self.__agentDSL_JAVAID

    @agentDSL_JAVAID.setter
    def agentDSL_JAVAID(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_agentDSL_JAVAID__agentDSL_JAVAID", None)
        self.__agentDSL_JAVAID = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "agentDSL_TypeDef"):
                opp_val = getattr(old_value, "agentDSL_TypeDef", None)
                if opp_val == self:
                    setattr(old_value, "agentDSL_TypeDef", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "agentDSL_TypeDef"):
                opp_val = getattr(value, "agentDSL_TypeDef", None)
                setattr(value, "agentDSL_TypeDef", self)

class Type:

    pass
class agentDSL_Function(Type):

    pass
class agentDSL_Outcome(Type):

    pass
class agentDSL_Entity(Type):

    pass
class agentDSL_Task(Type):

    pass
class agentDSL_TypeDef(Type):

    pass