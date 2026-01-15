from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class smalluml_Role:

    def __init__(self, Multiplicity: str, smalluml_Role: "smalluml_Association" = None, smalluml_Role27: "smalluml_SmallClass" = None):
        self.Multiplicity = Multiplicity
        self.smalluml_Role = smalluml_Role
        self.smalluml_Role27 = smalluml_Role27
        
    @property
    def Multiplicity(self) -> str:
        return self.__Multiplicity

    @Multiplicity.setter
    def Multiplicity(self, Multiplicity: str):
        self.__Multiplicity = Multiplicity

    @property
    def smalluml_Role(self):
        return self.__smalluml_Role

    @smalluml_Role.setter
    def smalluml_Role(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role", None)
        self.__smalluml_Role = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association25"):
                opp_val = getattr(old_value, "smalluml_Association25", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association25"):
                opp_val = getattr(value, "smalluml_Association25", None)
                if opp_val is None:
                    setattr(value, "smalluml_Association25", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Role27(self):
        return self.__smalluml_Role27

    @smalluml_Role27.setter
    def smalluml_Role27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Role__smalluml_Role27", None)
        self.__smalluml_Role27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_SmallClass28"):
                opp_val = getattr(old_value, "smalluml_SmallClass28", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_SmallClass28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_SmallClass28"):
                opp_val = getattr(value, "smalluml_SmallClass28", None)
                setattr(value, "smalluml_SmallClass28", self)

class smalluml_Methode:

    def __init__(self, name: str, returnType: str, smalluml_Methode: "smalluml_SmallClass" = None):
        self.name = name
        self.returnType = returnType
        self.smalluml_Methode = smalluml_Methode
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def smalluml_Methode(self):
        return self.__smalluml_Methode

    @smalluml_Methode.setter
    def smalluml_Methode(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Methode__smalluml_Methode", None)
        self.__smalluml_Methode = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_SmallClass8"):
                opp_val = getattr(old_value, "smalluml_SmallClass8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_SmallClass8"):
                opp_val = getattr(value, "smalluml_SmallClass8", None)
                if opp_val is None:
                    setattr(value, "smalluml_SmallClass8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smalluml_Attribute:

    def __init__(self, name: str, type: str, smalluml_Attribute: "smalluml_SmallClass" = None, smalluml_Attribute23: "smalluml_Association" = None):
        self.name = name
        self.type = type
        self.smalluml_Attribute = smalluml_Attribute
        self.smalluml_Attribute23 = smalluml_Attribute23
        
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
    def smalluml_Attribute(self):
        return self.__smalluml_Attribute

    @smalluml_Attribute.setter
    def smalluml_Attribute(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Attribute__smalluml_Attribute", None)
        self.__smalluml_Attribute = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_SmallClass6"):
                opp_val = getattr(old_value, "smalluml_SmallClass6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_SmallClass6"):
                opp_val = getattr(value, "smalluml_SmallClass6", None)
                if opp_val is None:
                    setattr(value, "smalluml_SmallClass6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Attribute23(self):
        return self.__smalluml_Attribute23

    @smalluml_Attribute23.setter
    def smalluml_Attribute23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Attribute__smalluml_Attribute23", None)
        self.__smalluml_Attribute23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association22"):
                opp_val = getattr(old_value, "smalluml_Association22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association22"):
                opp_val = getattr(value, "smalluml_Association22", None)
                if opp_val is None:
                    setattr(value, "smalluml_Association22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class smalluml_Association:

    def __init__(self, name: str, smalluml_Association: "smalluml_SchemaUML" = None, smalluml_Association16: "smalluml_SmallClass" = None, smalluml_Association19: "smalluml_SmallClass" = None, smalluml_Association22: set["smalluml_Attribute"] = None, smalluml_Association25: set["smalluml_Role"] = None):
        self.name = name
        self.smalluml_Association = smalluml_Association
        self.smalluml_Association16 = smalluml_Association16
        self.smalluml_Association19 = smalluml_Association19
        self.smalluml_Association22 = smalluml_Association22 if smalluml_Association22 is not None else set()
        self.smalluml_Association25 = smalluml_Association25 if smalluml_Association25 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smalluml_Association(self):
        return self.__smalluml_Association

    @smalluml_Association.setter
    def smalluml_Association(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Association__smalluml_Association", None)
        self.__smalluml_Association = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_SchemaUML4"):
                opp_val = getattr(old_value, "smalluml_SchemaUML4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_SchemaUML4"):
                opp_val = getattr(value, "smalluml_SchemaUML4", None)
                if opp_val is None:
                    setattr(value, "smalluml_SchemaUML4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_Association22(self):
        return self.__smalluml_Association22

    @smalluml_Association22.setter
    def smalluml_Association22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Association__smalluml_Association22", None)
        self.__smalluml_Association22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Attribute23"):
                    opp_val = getattr(item, "smalluml_Attribute23", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Attribute23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Attribute23"):
                    opp_val = getattr(item, "smalluml_Attribute23", None)
                    
                    setattr(item, "smalluml_Attribute23", self)
                    

    @property
    def smalluml_Association19(self):
        return self.__smalluml_Association19

    @smalluml_Association19.setter
    def smalluml_Association19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Association__smalluml_Association19", None)
        self.__smalluml_Association19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_SmallClass20"):
                opp_val = getattr(old_value, "smalluml_SmallClass20", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_SmallClass20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_SmallClass20"):
                opp_val = getattr(value, "smalluml_SmallClass20", None)
                setattr(value, "smalluml_SmallClass20", self)

    @property
    def smalluml_Association25(self):
        return self.__smalluml_Association25

    @smalluml_Association25.setter
    def smalluml_Association25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Association__smalluml_Association25", None)
        self.__smalluml_Association25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Role"):
                    opp_val = getattr(item, "smalluml_Role", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Role", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Role"):
                    opp_val = getattr(item, "smalluml_Role", None)
                    
                    setattr(item, "smalluml_Role", self)
                    

    @property
    def smalluml_Association16(self):
        return self.__smalluml_Association16

    @smalluml_Association16.setter
    def smalluml_Association16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_Association__smalluml_Association16", None)
        self.__smalluml_Association16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_SmallClass17"):
                opp_val = getattr(old_value, "smalluml_SmallClass17", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_SmallClass17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_SmallClass17"):
                opp_val = getattr(value, "smalluml_SmallClass17", None)
                setattr(value, "smalluml_SmallClass17", self)

class smalluml_SmallClass:

    def __init__(self, name: str, smalluml_SmallClass: "smalluml_SchemaUML" = None, smalluml_SmallClass6: set["smalluml_Attribute"] = None, smalluml_SmallClass8: set["smalluml_Methode"] = None, smalluml_SmallClass11: "smalluml_Generalisation" = None, smalluml_SmallClass14: "smalluml_Generalisation" = None, smalluml_SmallClass17: "smalluml_Association" = None, smalluml_SmallClass20: "smalluml_Association" = None, smalluml_SmallClass28: "smalluml_Role" = None):
        self.name = name
        self.smalluml_SmallClass = smalluml_SmallClass
        self.smalluml_SmallClass6 = smalluml_SmallClass6 if smalluml_SmallClass6 is not None else set()
        self.smalluml_SmallClass8 = smalluml_SmallClass8 if smalluml_SmallClass8 is not None else set()
        self.smalluml_SmallClass11 = smalluml_SmallClass11
        self.smalluml_SmallClass14 = smalluml_SmallClass14
        self.smalluml_SmallClass17 = smalluml_SmallClass17
        self.smalluml_SmallClass20 = smalluml_SmallClass20
        self.smalluml_SmallClass28 = smalluml_SmallClass28
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def smalluml_SmallClass20(self):
        return self.__smalluml_SmallClass20

    @smalluml_SmallClass20.setter
    def smalluml_SmallClass20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_SmallClass__smalluml_SmallClass20", None)
        self.__smalluml_SmallClass20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association19"):
                opp_val = getattr(old_value, "smalluml_Association19", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association19"):
                opp_val = getattr(value, "smalluml_Association19", None)
                setattr(value, "smalluml_Association19", self)

    @property
    def smalluml_SmallClass6(self):
        return self.__smalluml_SmallClass6

    @smalluml_SmallClass6.setter
    def smalluml_SmallClass6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_SmallClass__smalluml_SmallClass6", None)
        self.__smalluml_SmallClass6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Attribute"):
                    opp_val = getattr(item, "smalluml_Attribute", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Attribute", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Attribute"):
                    opp_val = getattr(item, "smalluml_Attribute", None)
                    
                    setattr(item, "smalluml_Attribute", self)
                    

    @property
    def smalluml_SmallClass8(self):
        return self.__smalluml_SmallClass8

    @smalluml_SmallClass8.setter
    def smalluml_SmallClass8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_SmallClass__smalluml_SmallClass8", None)
        self.__smalluml_SmallClass8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "smalluml_Methode"):
                    opp_val = getattr(item, "smalluml_Methode", None)
                    
                    if opp_val == self:
                        setattr(item, "smalluml_Methode", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "smalluml_Methode"):
                    opp_val = getattr(item, "smalluml_Methode", None)
                    
                    setattr(item, "smalluml_Methode", self)
                    

    @property
    def smalluml_SmallClass(self):
        return self.__smalluml_SmallClass

    @smalluml_SmallClass.setter
    def smalluml_SmallClass(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_SmallClass__smalluml_SmallClass", None)
        self.__smalluml_SmallClass = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_SchemaUML2"):
                opp_val = getattr(old_value, "smalluml_SchemaUML2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_SchemaUML2"):
                opp_val = getattr(value, "smalluml_SchemaUML2", None)
                if opp_val is None:
                    setattr(value, "smalluml_SchemaUML2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def smalluml_SmallClass14(self):
        return self.__smalluml_SmallClass14

    @smalluml_SmallClass14.setter
    def smalluml_SmallClass14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_SmallClass__smalluml_SmallClass14", None)
        self.__smalluml_SmallClass14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Generalisation13"):
                opp_val = getattr(old_value, "smalluml_Generalisation13", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Generalisation13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Generalisation13"):
                opp_val = getattr(value, "smalluml_Generalisation13", None)
                setattr(value, "smalluml_Generalisation13", self)

    @property
    def smalluml_SmallClass28(self):
        return self.__smalluml_SmallClass28

    @smalluml_SmallClass28.setter
    def smalluml_SmallClass28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_SmallClass__smalluml_SmallClass28", None)
        self.__smalluml_SmallClass28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Role27"):
                opp_val = getattr(old_value, "smalluml_Role27", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Role27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Role27"):
                opp_val = getattr(value, "smalluml_Role27", None)
                setattr(value, "smalluml_Role27", self)

    @property
    def smalluml_SmallClass11(self):
        return self.__smalluml_SmallClass11

    @smalluml_SmallClass11.setter
    def smalluml_SmallClass11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_SmallClass__smalluml_SmallClass11", None)
        self.__smalluml_SmallClass11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Generalisation10"):
                opp_val = getattr(old_value, "smalluml_Generalisation10", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Generalisation10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Generalisation10"):
                opp_val = getattr(value, "smalluml_Generalisation10", None)
                setattr(value, "smalluml_Generalisation10", self)

    @property
    def smalluml_SmallClass17(self):
        return self.__smalluml_SmallClass17

    @smalluml_SmallClass17.setter
    def smalluml_SmallClass17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_smalluml_SmallClass__smalluml_SmallClass17", None)
        self.__smalluml_SmallClass17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "smalluml_Association16"):
                opp_val = getattr(old_value, "smalluml_Association16", None)
                if opp_val == self:
                    setattr(old_value, "smalluml_Association16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "smalluml_Association16"):
                opp_val = getattr(value, "smalluml_Association16", None)
                setattr(value, "smalluml_Association16", self)

class smalluml_Generalisation:

    pass
class smalluml_SchemaUML:

    pass