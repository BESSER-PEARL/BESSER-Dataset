from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Expression:

    pass
class B_Any(Expression):

    pass
class B_Begin(Expression):

    pass
class B_Skip(Expression):

    pass
class B_If(Expression):

    pass
class B_Machine:

    def __init__(self, name: str, B_Machine: "B_Machine" = None, B_Machine0: "B_Machine" = None, B_Machine3: set["B_SET"] = None, B_Machine5: set["B_Operation"] = None, B_Machine7: set["B_Predicate"] = None, B_Machine9: set["B_Variable"] = None, B_Machine11: set["B_Action"] = None):
        self.name = name
        self.B_Machine = B_Machine
        self.B_Machine0 = B_Machine0
        self.B_Machine3 = B_Machine3 if B_Machine3 is not None else set()
        self.B_Machine5 = B_Machine5 if B_Machine5 is not None else set()
        self.B_Machine7 = B_Machine7 if B_Machine7 is not None else set()
        self.B_Machine9 = B_Machine9 if B_Machine9 is not None else set()
        self.B_Machine11 = B_Machine11 if B_Machine11 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def B_Machine3(self):
        return self.__B_Machine3

    @B_Machine3.setter
    def B_Machine3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Machine__B_Machine3", None)
        self.__B_Machine3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_SET"):
                    opp_val = getattr(item, "B_SET", None)
                    
                    if opp_val == self:
                        setattr(item, "B_SET", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_SET"):
                    opp_val = getattr(item, "B_SET", None)
                    
                    setattr(item, "B_SET", self)
                    

    @property
    def B_Machine5(self):
        return self.__B_Machine5

    @B_Machine5.setter
    def B_Machine5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Machine__B_Machine5", None)
        self.__B_Machine5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_Operation"):
                    opp_val = getattr(item, "B_Operation", None)
                    
                    if opp_val == self:
                        setattr(item, "B_Operation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_Operation"):
                    opp_val = getattr(item, "B_Operation", None)
                    
                    setattr(item, "B_Operation", self)
                    

    @property
    def B_Machine0(self):
        return self.__B_Machine0

    @B_Machine0.setter
    def B_Machine0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Machine__B_Machine0", None)
        self.__B_Machine0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Machine"):
                opp_val = getattr(old_value, "B_Machine", None)
                if opp_val == self:
                    setattr(old_value, "B_Machine", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Machine"):
                opp_val = getattr(value, "B_Machine", None)
                setattr(value, "B_Machine", self)

    @property
    def B_Machine7(self):
        return self.__B_Machine7

    @B_Machine7.setter
    def B_Machine7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Machine__B_Machine7", None)
        self.__B_Machine7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_Predicate"):
                    opp_val = getattr(item, "B_Predicate", None)
                    
                    if opp_val == self:
                        setattr(item, "B_Predicate", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_Predicate"):
                    opp_val = getattr(item, "B_Predicate", None)
                    
                    setattr(item, "B_Predicate", self)
                    

    @property
    def B_Machine11(self):
        return self.__B_Machine11

    @B_Machine11.setter
    def B_Machine11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Machine__B_Machine11", None)
        self.__B_Machine11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_Action"):
                    opp_val = getattr(item, "B_Action", None)
                    
                    if opp_val == self:
                        setattr(item, "B_Action", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_Action"):
                    opp_val = getattr(item, "B_Action", None)
                    
                    setattr(item, "B_Action", self)
                    

    @property
    def B_Machine(self):
        return self.__B_Machine

    @B_Machine.setter
    def B_Machine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Machine__B_Machine", None)
        self.__B_Machine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Machine0"):
                opp_val = getattr(old_value, "B_Machine0", None)
                if opp_val == self:
                    setattr(old_value, "B_Machine0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Machine0"):
                opp_val = getattr(value, "B_Machine0", None)
                setattr(value, "B_Machine0", self)

    @property
    def B_Machine9(self):
        return self.__B_Machine9

    @B_Machine9.setter
    def B_Machine9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Machine__B_Machine9", None)
        self.__B_Machine9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_Variable"):
                    opp_val = getattr(item, "B_Variable", None)
                    
                    if opp_val == self:
                        setattr(item, "B_Variable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_Variable"):
                    opp_val = getattr(item, "B_Variable", None)
                    
                    setattr(item, "B_Variable", self)
                    

class B_VariableList:

    def __init__(self, size: str, B_VariableList: "B_Operation" = None, B_VariableList18: "B_Operation" = None, B_VariableList29: set["B_Variable"] = None, B_VariableList32: "B_Variable" = None):
        self.size = size
        self.B_VariableList = B_VariableList
        self.B_VariableList18 = B_VariableList18
        self.B_VariableList29 = B_VariableList29 if B_VariableList29 is not None else set()
        self.B_VariableList32 = B_VariableList32
        
    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def B_VariableList29(self):
        return self.__B_VariableList29

    @B_VariableList29.setter
    def B_VariableList29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_VariableList__B_VariableList29", None)
        self.__B_VariableList29 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_Variable30"):
                    opp_val = getattr(item, "B_Variable30", None)
                    
                    if opp_val == self:
                        setattr(item, "B_Variable30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_Variable30"):
                    opp_val = getattr(item, "B_Variable30", None)
                    
                    setattr(item, "B_Variable30", self)
                    

    @property
    def B_VariableList18(self):
        return self.__B_VariableList18

    @B_VariableList18.setter
    def B_VariableList18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_VariableList__B_VariableList18", None)
        self.__B_VariableList18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Operation17"):
                opp_val = getattr(old_value, "B_Operation17", None)
                if opp_val == self:
                    setattr(old_value, "B_Operation17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Operation17"):
                opp_val = getattr(value, "B_Operation17", None)
                setattr(value, "B_Operation17", self)

    @property
    def B_VariableList32(self):
        return self.__B_VariableList32

    @B_VariableList32.setter
    def B_VariableList32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_VariableList__B_VariableList32", None)
        self.__B_VariableList32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Variable33"):
                opp_val = getattr(old_value, "B_Variable33", None)
                if opp_val == self:
                    setattr(old_value, "B_Variable33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Variable33"):
                opp_val = getattr(value, "B_Variable33", None)
                setattr(value, "B_Variable33", self)

    @property
    def B_VariableList(self):
        return self.__B_VariableList

    @B_VariableList.setter
    def B_VariableList(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_VariableList__B_VariableList", None)
        self.__B_VariableList = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Operation15"):
                opp_val = getattr(old_value, "B_Operation15", None)
                if opp_val == self:
                    setattr(old_value, "B_Operation15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Operation15"):
                opp_val = getattr(value, "B_Operation15", None)
                setattr(value, "B_Operation15", self)

class B_Expression:

    def __init__(self, expression: str, B_Expression: "B_Operation" = None, B_Expression41: "B_Any" = None, B_Expression43: "B_If" = None, B_Expression46: "B_If" = None, B_Expression51: "B_Begin" = None):
        self.expression = expression
        self.B_Expression = B_Expression
        self.B_Expression41 = B_Expression41
        self.B_Expression43 = B_Expression43
        self.B_Expression46 = B_Expression46
        self.B_Expression51 = B_Expression51
        
    @property
    def expression(self) -> str:
        return self.__expression

    @expression.setter
    def expression(self, expression: str):
        self.__expression = expression

    @property
    def B_Expression(self):
        return self.__B_Expression

    @B_Expression.setter
    def B_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Expression__B_Expression", None)
        self.__B_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Operation13"):
                opp_val = getattr(old_value, "B_Operation13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Operation13"):
                opp_val = getattr(value, "B_Operation13", None)
                if opp_val is None:
                    setattr(value, "B_Operation13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B_Expression51(self):
        return self.__B_Expression51

    @B_Expression51.setter
    def B_Expression51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Expression__B_Expression51", None)
        self.__B_Expression51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Begin"):
                opp_val = getattr(old_value, "B_Begin", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Begin"):
                opp_val = getattr(value, "B_Begin", None)
                if opp_val is None:
                    setattr(value, "B_Begin", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B_Expression43(self):
        return self.__B_Expression43

    @B_Expression43.setter
    def B_Expression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Expression__B_Expression43", None)
        self.__B_Expression43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_If"):
                opp_val = getattr(old_value, "B_If", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_If"):
                opp_val = getattr(value, "B_If", None)
                if opp_val is None:
                    setattr(value, "B_If", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B_Expression46(self):
        return self.__B_Expression46

    @B_Expression46.setter
    def B_Expression46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Expression__B_Expression46", None)
        self.__B_Expression46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_If45"):
                opp_val = getattr(old_value, "B_If45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_If45"):
                opp_val = getattr(value, "B_If45", None)
                if opp_val is None:
                    setattr(value, "B_If45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B_Expression41(self):
        return self.__B_Expression41

    @B_Expression41.setter
    def B_Expression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Expression__B_Expression41", None)
        self.__B_Expression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Any40"):
                opp_val = getattr(old_value, "B_Any40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Any40"):
                opp_val = getattr(value, "B_Any40", None)
                if opp_val is None:
                    setattr(value, "B_Any40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class B_Action(Expression):

    pass
class B_Variable:

    def __init__(self, name: str, B_Variable: "B_Machine" = None, B_Variable24: "B_Variable" = None, B_Variable22: "B_Variable" = None, B_Variable26: "B_Predicate" = None, B_Variable30: "B_VariableList" = None, B_Variable33: "B_VariableList" = None, B_Variable35: "B_Any" = None):
        self.name = name
        self.B_Variable = B_Variable
        self.B_Variable24 = B_Variable24
        self.B_Variable22 = B_Variable22
        self.B_Variable26 = B_Variable26
        self.B_Variable30 = B_Variable30
        self.B_Variable33 = B_Variable33
        self.B_Variable35 = B_Variable35
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def B_Variable33(self):
        return self.__B_Variable33

    @B_Variable33.setter
    def B_Variable33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Variable__B_Variable33", None)
        self.__B_Variable33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_VariableList32"):
                opp_val = getattr(old_value, "B_VariableList32", None)
                if opp_val == self:
                    setattr(old_value, "B_VariableList32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_VariableList32"):
                opp_val = getattr(value, "B_VariableList32", None)
                setattr(value, "B_VariableList32", self)

    @property
    def B_Variable35(self):
        return self.__B_Variable35

    @B_Variable35.setter
    def B_Variable35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Variable__B_Variable35", None)
        self.__B_Variable35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Any"):
                opp_val = getattr(old_value, "B_Any", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Any"):
                opp_val = getattr(value, "B_Any", None)
                if opp_val is None:
                    setattr(value, "B_Any", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B_Variable24(self):
        return self.__B_Variable24

    @B_Variable24.setter
    def B_Variable24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Variable__B_Variable24", None)
        self.__B_Variable24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Variable22"):
                opp_val = getattr(old_value, "B_Variable22", None)
                if opp_val == self:
                    setattr(old_value, "B_Variable22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Variable22"):
                opp_val = getattr(value, "B_Variable22", None)
                setattr(value, "B_Variable22", self)

    @property
    def B_Variable(self):
        return self.__B_Variable

    @B_Variable.setter
    def B_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Variable__B_Variable", None)
        self.__B_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Machine9"):
                opp_val = getattr(old_value, "B_Machine9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Machine9"):
                opp_val = getattr(value, "B_Machine9", None)
                if opp_val is None:
                    setattr(value, "B_Machine9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B_Variable26(self):
        return self.__B_Variable26

    @B_Variable26.setter
    def B_Variable26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Variable__B_Variable26", None)
        self.__B_Variable26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Predicate27"):
                opp_val = getattr(old_value, "B_Predicate27", None)
                if opp_val == self:
                    setattr(old_value, "B_Predicate27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Predicate27"):
                opp_val = getattr(value, "B_Predicate27", None)
                setattr(value, "B_Predicate27", self)

    @property
    def B_Variable30(self):
        return self.__B_Variable30

    @B_Variable30.setter
    def B_Variable30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Variable__B_Variable30", None)
        self.__B_Variable30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_VariableList29"):
                opp_val = getattr(old_value, "B_VariableList29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_VariableList29"):
                opp_val = getattr(value, "B_VariableList29", None)
                if opp_val is None:
                    setattr(value, "B_VariableList29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B_Variable22(self):
        return self.__B_Variable22

    @B_Variable22.setter
    def B_Variable22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Variable__B_Variable22", None)
        self.__B_Variable22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Variable24"):
                opp_val = getattr(old_value, "B_Variable24", None)
                if opp_val == self:
                    setattr(old_value, "B_Variable24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Variable24"):
                opp_val = getattr(value, "B_Variable24", None)
                setattr(value, "B_Variable24", self)

class B_Predicate(Expression):

    pass
class B_Operation:

    def __init__(self, name: str, B_Operation: "B_Machine" = None, B_Operation13: set["B_Expression"] = None, B_Operation15: "B_VariableList" = None, B_Operation17: "B_VariableList" = None, B_Operation20: set["B_Predicate"] = None):
        self.name = name
        self.B_Operation = B_Operation
        self.B_Operation13 = B_Operation13 if B_Operation13 is not None else set()
        self.B_Operation15 = B_Operation15
        self.B_Operation17 = B_Operation17
        self.B_Operation20 = B_Operation20 if B_Operation20 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def B_Operation13(self):
        return self.__B_Operation13

    @B_Operation13.setter
    def B_Operation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Operation__B_Operation13", None)
        self.__B_Operation13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_Expression"):
                    opp_val = getattr(item, "B_Expression", None)
                    
                    if opp_val == self:
                        setattr(item, "B_Expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_Expression"):
                    opp_val = getattr(item, "B_Expression", None)
                    
                    setattr(item, "B_Expression", self)
                    

    @property
    def B_Operation20(self):
        return self.__B_Operation20

    @B_Operation20.setter
    def B_Operation20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Operation__B_Operation20", None)
        self.__B_Operation20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "B_Predicate21"):
                    opp_val = getattr(item, "B_Predicate21", None)
                    
                    if opp_val == self:
                        setattr(item, "B_Predicate21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "B_Predicate21"):
                    opp_val = getattr(item, "B_Predicate21", None)
                    
                    setattr(item, "B_Predicate21", self)
                    

    @property
    def B_Operation17(self):
        return self.__B_Operation17

    @B_Operation17.setter
    def B_Operation17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Operation__B_Operation17", None)
        self.__B_Operation17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_VariableList18"):
                opp_val = getattr(old_value, "B_VariableList18", None)
                if opp_val == self:
                    setattr(old_value, "B_VariableList18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_VariableList18"):
                opp_val = getattr(value, "B_VariableList18", None)
                setattr(value, "B_VariableList18", self)

    @property
    def B_Operation(self):
        return self.__B_Operation

    @B_Operation.setter
    def B_Operation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Operation__B_Operation", None)
        self.__B_Operation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Machine5"):
                opp_val = getattr(old_value, "B_Machine5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Machine5"):
                opp_val = getattr(value, "B_Machine5", None)
                if opp_val is None:
                    setattr(value, "B_Machine5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def B_Operation15(self):
        return self.__B_Operation15

    @B_Operation15.setter
    def B_Operation15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_Operation__B_Operation15", None)
        self.__B_Operation15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_VariableList"):
                opp_val = getattr(old_value, "B_VariableList", None)
                if opp_val == self:
                    setattr(old_value, "B_VariableList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_VariableList"):
                opp_val = getattr(value, "B_VariableList", None)
                setattr(value, "B_VariableList", self)

class B_SET:

    def __init__(self, name: str, B_SET: "B_Machine" = None):
        self.name = name
        self.B_SET = B_SET
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def B_SET(self):
        return self.__B_SET

    @B_SET.setter
    def B_SET(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_B_SET__B_SET", None)
        self.__B_SET = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "B_Machine3"):
                opp_val = getattr(old_value, "B_Machine3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "B_Machine3"):
                opp_val = getattr(value, "B_Machine3", None)
                if opp_val is None:
                    setattr(value, "B_Machine3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
