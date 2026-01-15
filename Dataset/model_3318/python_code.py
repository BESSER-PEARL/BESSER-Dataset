from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class java_Return_value:

    def __init__(self, name: str, java_Return_value: "java_Return_Statement" = None):
        self.name = name
        self.java_Return_value = java_Return_value
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Return_value(self):
        return self.__java_Return_value

    @java_Return_value.setter
    def java_Return_value(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Return_value__java_Return_value", None)
        self.__java_Return_value = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Return_Statement186"):
                opp_val = getattr(old_value, "java_Return_Statement186", None)
                if opp_val == self:
                    setattr(old_value, "java_Return_Statement186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Return_Statement186"):
                opp_val = getattr(value, "java_Return_Statement186", None)
                setattr(value, "java_Return_Statement186", self)

class java_Try_statement:

    def __init__(self, try: str, catchs: str, finally: str, java_Try_statement: "java_Statement" = None, java_Try_statement188: "java_Statement" = None, java_Try_statement191: set["java_Parameter"] = None, java_Try_statement194: set["java_Statement"] = None, java_Try_statement197: "java_Statement" = None):
        self.try = try
        self.catchs = catchs
        self.finally = finally
        self.java_Try_statement = java_Try_statement
        self.java_Try_statement188 = java_Try_statement188
        self.java_Try_statement191 = java_Try_statement191 if java_Try_statement191 is not None else set()
        self.java_Try_statement194 = java_Try_statement194 if java_Try_statement194 is not None else set()
        self.java_Try_statement197 = java_Try_statement197
        
    @property
    def catchs(self) -> str:
        return self.__catchs

    @catchs.setter
    def catchs(self, catchs: str):
        self.__catchs = catchs

    @property
    def finally(self) -> str:
        return self.__finally

    @finally.setter
    def finally(self, finally: str):
        self.__finally = finally

    @property
    def try(self) -> str:
        return self.__try

    @try.setter
    def try(self, try: str):
        self.__try = try

    @property
    def java_Try_statement194(self):
        return self.__java_Try_statement194

    @java_Try_statement194.setter
    def java_Try_statement194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Try_statement__java_Try_statement194", None)
        self.__java_Try_statement194 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Statement195"):
                    opp_val = getattr(item, "java_Statement195", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Statement195", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Statement195"):
                    opp_val = getattr(item, "java_Statement195", None)
                    
                    setattr(item, "java_Statement195", self)
                    

    @property
    def java_Try_statement188(self):
        return self.__java_Try_statement188

    @java_Try_statement188.setter
    def java_Try_statement188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Try_statement__java_Try_statement188", None)
        self.__java_Try_statement188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement189"):
                opp_val = getattr(old_value, "java_Statement189", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement189"):
                opp_val = getattr(value, "java_Statement189", None)
                setattr(value, "java_Statement189", self)

    @property
    def java_Try_statement191(self):
        return self.__java_Try_statement191

    @java_Try_statement191.setter
    def java_Try_statement191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Try_statement__java_Try_statement191", None)
        self.__java_Try_statement191 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Parameter192"):
                    opp_val = getattr(item, "java_Parameter192", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Parameter192", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Parameter192"):
                    opp_val = getattr(item, "java_Parameter192", None)
                    
                    setattr(item, "java_Parameter192", self)
                    

    @property
    def java_Try_statement(self):
        return self.__java_Try_statement

    @java_Try_statement.setter
    def java_Try_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Try_statement__java_Try_statement", None)
        self.__java_Try_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement136"):
                opp_val = getattr(old_value, "java_Statement136", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement136"):
                opp_val = getattr(value, "java_Statement136", None)
                setattr(value, "java_Statement136", self)

    @property
    def java_Try_statement197(self):
        return self.__java_Try_statement197

    @java_Try_statement197.setter
    def java_Try_statement197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Try_statement__java_Try_statement197", None)
        self.__java_Try_statement197 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement198"):
                opp_val = getattr(old_value, "java_Statement198", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement198"):
                opp_val = getattr(value, "java_Statement198", None)
                setattr(value, "java_Statement198", self)

class java_Statement:

    def __init__(self, name: str, java_Statement118: "java_Return_Statement" = None, java_Statement120: "java_Variable_declaration" = None, java_Statement123: "java_Expression" = None, java_Statement126: "java_If_Statement" = None, java_Statement128: "java_Do_Statement" = None, java_Statement130: "java_While_Statement" = None, java_Statement132: "java_For_Statement" = None, java_Statement134: "java_Switch_Statement" = None, java_Statement: "java_Statement_block" = None, java_Statement139: "java_Statement" = None, java_Statement137: "java_Statement" = None, java_Statement148: "java_Switch_Statement" = None, java_Statement136: "java_Try_statement" = None, java_Statement163: "java_For_Statement" = None, java_Statement169: "java_While_Statement" = None, java_Statement172: "java_Do_Statement" = None, java_Statement181: "java_If_Statement" = None, java_Statement184: "java_If_Statement" = None, java_Statement189: "java_Try_statement" = None, java_Statement195: "java_Try_statement" = None, java_Statement198: "java_Try_statement" = None):
        self.name = name
        self.java_Statement118 = java_Statement118
        self.java_Statement120 = java_Statement120
        self.java_Statement123 = java_Statement123
        self.java_Statement126 = java_Statement126
        self.java_Statement128 = java_Statement128
        self.java_Statement130 = java_Statement130
        self.java_Statement132 = java_Statement132
        self.java_Statement134 = java_Statement134
        self.java_Statement = java_Statement
        self.java_Statement139 = java_Statement139
        self.java_Statement137 = java_Statement137
        self.java_Statement148 = java_Statement148
        self.java_Statement136 = java_Statement136
        self.java_Statement163 = java_Statement163
        self.java_Statement169 = java_Statement169
        self.java_Statement172 = java_Statement172
        self.java_Statement181 = java_Statement181
        self.java_Statement184 = java_Statement184
        self.java_Statement189 = java_Statement189
        self.java_Statement195 = java_Statement195
        self.java_Statement198 = java_Statement198
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Statement134(self):
        return self.__java_Statement134

    @java_Statement134.setter
    def java_Statement134(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement134", None)
        self.__java_Statement134 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Switch_Statement"):
                opp_val = getattr(old_value, "java_Switch_Statement", None)
                if opp_val == self:
                    setattr(old_value, "java_Switch_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Switch_Statement"):
                opp_val = getattr(value, "java_Switch_Statement", None)
                setattr(value, "java_Switch_Statement", self)

    @property
    def java_Statement148(self):
        return self.__java_Statement148

    @java_Statement148.setter
    def java_Statement148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement148", None)
        self.__java_Statement148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Switch_Statement147"):
                opp_val = getattr(old_value, "java_Switch_Statement147", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Switch_Statement147"):
                opp_val = getattr(value, "java_Switch_Statement147", None)
                if opp_val is None:
                    setattr(value, "java_Switch_Statement147", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Statement172(self):
        return self.__java_Statement172

    @java_Statement172.setter
    def java_Statement172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement172", None)
        self.__java_Statement172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Do_Statement171"):
                opp_val = getattr(old_value, "java_Do_Statement171", None)
                if opp_val == self:
                    setattr(old_value, "java_Do_Statement171", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Do_Statement171"):
                opp_val = getattr(value, "java_Do_Statement171", None)
                setattr(value, "java_Do_Statement171", self)

    @property
    def java_Statement118(self):
        return self.__java_Statement118

    @java_Statement118.setter
    def java_Statement118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement118", None)
        self.__java_Statement118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Return_Statement"):
                opp_val = getattr(old_value, "java_Return_Statement", None)
                if opp_val == self:
                    setattr(old_value, "java_Return_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Return_Statement"):
                opp_val = getattr(value, "java_Return_Statement", None)
                setattr(value, "java_Return_Statement", self)

    @property
    def java_Statement184(self):
        return self.__java_Statement184

    @java_Statement184.setter
    def java_Statement184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement184", None)
        self.__java_Statement184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_If_Statement183"):
                opp_val = getattr(old_value, "java_If_Statement183", None)
                if opp_val == self:
                    setattr(old_value, "java_If_Statement183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_If_Statement183"):
                opp_val = getattr(value, "java_If_Statement183", None)
                setattr(value, "java_If_Statement183", self)

    @property
    def java_Statement163(self):
        return self.__java_Statement163

    @java_Statement163.setter
    def java_Statement163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement163", None)
        self.__java_Statement163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_For_Statement162"):
                opp_val = getattr(old_value, "java_For_Statement162", None)
                if opp_val == self:
                    setattr(old_value, "java_For_Statement162", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_For_Statement162"):
                opp_val = getattr(value, "java_For_Statement162", None)
                setattr(value, "java_For_Statement162", self)

    @property
    def java_Statement198(self):
        return self.__java_Statement198

    @java_Statement198.setter
    def java_Statement198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement198", None)
        self.__java_Statement198 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Try_statement197"):
                opp_val = getattr(old_value, "java_Try_statement197", None)
                if opp_val == self:
                    setattr(old_value, "java_Try_statement197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Try_statement197"):
                opp_val = getattr(value, "java_Try_statement197", None)
                setattr(value, "java_Try_statement197", self)

    @property
    def java_Statement189(self):
        return self.__java_Statement189

    @java_Statement189.setter
    def java_Statement189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement189", None)
        self.__java_Statement189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Try_statement188"):
                opp_val = getattr(old_value, "java_Try_statement188", None)
                if opp_val == self:
                    setattr(old_value, "java_Try_statement188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Try_statement188"):
                opp_val = getattr(value, "java_Try_statement188", None)
                setattr(value, "java_Try_statement188", self)

    @property
    def java_Statement120(self):
        return self.__java_Statement120

    @java_Statement120.setter
    def java_Statement120(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement120", None)
        self.__java_Statement120 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Variable_declaration121"):
                opp_val = getattr(old_value, "java_Variable_declaration121", None)
                if opp_val == self:
                    setattr(old_value, "java_Variable_declaration121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Variable_declaration121"):
                opp_val = getattr(value, "java_Variable_declaration121", None)
                setattr(value, "java_Variable_declaration121", self)

    @property
    def java_Statement(self):
        return self.__java_Statement

    @java_Statement.setter
    def java_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement", None)
        self.__java_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement_block116"):
                opp_val = getattr(old_value, "java_Statement_block116", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement_block116"):
                opp_val = getattr(value, "java_Statement_block116", None)
                if opp_val is None:
                    setattr(value, "java_Statement_block116", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Statement137(self):
        return self.__java_Statement137

    @java_Statement137.setter
    def java_Statement137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement137", None)
        self.__java_Statement137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement139"):
                opp_val = getattr(old_value, "java_Statement139", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement139"):
                opp_val = getattr(value, "java_Statement139", None)
                setattr(value, "java_Statement139", self)

    @property
    def java_Statement128(self):
        return self.__java_Statement128

    @java_Statement128.setter
    def java_Statement128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement128", None)
        self.__java_Statement128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Do_Statement"):
                opp_val = getattr(old_value, "java_Do_Statement", None)
                if opp_val == self:
                    setattr(old_value, "java_Do_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Do_Statement"):
                opp_val = getattr(value, "java_Do_Statement", None)
                setattr(value, "java_Do_Statement", self)

    @property
    def java_Statement181(self):
        return self.__java_Statement181

    @java_Statement181.setter
    def java_Statement181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement181", None)
        self.__java_Statement181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_If_Statement180"):
                opp_val = getattr(old_value, "java_If_Statement180", None)
                if opp_val == self:
                    setattr(old_value, "java_If_Statement180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_If_Statement180"):
                opp_val = getattr(value, "java_If_Statement180", None)
                setattr(value, "java_If_Statement180", self)

    @property
    def java_Statement130(self):
        return self.__java_Statement130

    @java_Statement130.setter
    def java_Statement130(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement130", None)
        self.__java_Statement130 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_While_Statement"):
                opp_val = getattr(old_value, "java_While_Statement", None)
                if opp_val == self:
                    setattr(old_value, "java_While_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_While_Statement"):
                opp_val = getattr(value, "java_While_Statement", None)
                setattr(value, "java_While_Statement", self)

    @property
    def java_Statement136(self):
        return self.__java_Statement136

    @java_Statement136.setter
    def java_Statement136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement136", None)
        self.__java_Statement136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Try_statement"):
                opp_val = getattr(old_value, "java_Try_statement", None)
                if opp_val == self:
                    setattr(old_value, "java_Try_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Try_statement"):
                opp_val = getattr(value, "java_Try_statement", None)
                setattr(value, "java_Try_statement", self)

    @property
    def java_Statement169(self):
        return self.__java_Statement169

    @java_Statement169.setter
    def java_Statement169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement169", None)
        self.__java_Statement169 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_While_Statement168"):
                opp_val = getattr(old_value, "java_While_Statement168", None)
                if opp_val == self:
                    setattr(old_value, "java_While_Statement168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_While_Statement168"):
                opp_val = getattr(value, "java_While_Statement168", None)
                setattr(value, "java_While_Statement168", self)

    @property
    def java_Statement195(self):
        return self.__java_Statement195

    @java_Statement195.setter
    def java_Statement195(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement195", None)
        self.__java_Statement195 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Try_statement194"):
                opp_val = getattr(old_value, "java_Try_statement194", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Try_statement194"):
                opp_val = getattr(value, "java_Try_statement194", None)
                if opp_val is None:
                    setattr(value, "java_Try_statement194", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Statement126(self):
        return self.__java_Statement126

    @java_Statement126.setter
    def java_Statement126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement126", None)
        self.__java_Statement126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_If_Statement"):
                opp_val = getattr(old_value, "java_If_Statement", None)
                if opp_val == self:
                    setattr(old_value, "java_If_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_If_Statement"):
                opp_val = getattr(value, "java_If_Statement", None)
                setattr(value, "java_If_Statement", self)

    @property
    def java_Statement139(self):
        return self.__java_Statement139

    @java_Statement139.setter
    def java_Statement139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement139", None)
        self.__java_Statement139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement137"):
                opp_val = getattr(old_value, "java_Statement137", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement137", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement137"):
                opp_val = getattr(value, "java_Statement137", None)
                setattr(value, "java_Statement137", self)

    @property
    def java_Statement132(self):
        return self.__java_Statement132

    @java_Statement132.setter
    def java_Statement132(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement132", None)
        self.__java_Statement132 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_For_Statement"):
                opp_val = getattr(old_value, "java_For_Statement", None)
                if opp_val == self:
                    setattr(old_value, "java_For_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_For_Statement"):
                opp_val = getattr(value, "java_For_Statement", None)
                setattr(value, "java_For_Statement", self)

    @property
    def java_Statement123(self):
        return self.__java_Statement123

    @java_Statement123.setter
    def java_Statement123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Statement__java_Statement123", None)
        self.__java_Statement123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression124"):
                opp_val = getattr(old_value, "java_Expression124", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression124", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression124"):
                opp_val = getattr(value, "java_Expression124", None)
                setattr(value, "java_Expression124", self)

class java_Switch_Statement:

    pass
class java_For_Statement:

    def __init__(self, pv: str, java_For_Statement: "java_Statement" = None, java_For_Statement150: "java_Variable_declaration" = None, java_For_Statement153: "java_Expression" = None, java_For_Statement156: "java_Expression" = None, java_For_Statement159: "java_Expression" = None, java_For_Statement162: "java_Statement" = None):
        self.pv = pv
        self.java_For_Statement = java_For_Statement
        self.java_For_Statement150 = java_For_Statement150
        self.java_For_Statement153 = java_For_Statement153
        self.java_For_Statement156 = java_For_Statement156
        self.java_For_Statement159 = java_For_Statement159
        self.java_For_Statement162 = java_For_Statement162
        
    @property
    def pv(self) -> str:
        return self.__pv

    @pv.setter
    def pv(self, pv: str):
        self.__pv = pv

    @property
    def java_For_Statement150(self):
        return self.__java_For_Statement150

    @java_For_Statement150.setter
    def java_For_Statement150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_For_Statement__java_For_Statement150", None)
        self.__java_For_Statement150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Variable_declaration151"):
                opp_val = getattr(old_value, "java_Variable_declaration151", None)
                if opp_val == self:
                    setattr(old_value, "java_Variable_declaration151", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Variable_declaration151"):
                opp_val = getattr(value, "java_Variable_declaration151", None)
                setattr(value, "java_Variable_declaration151", self)

    @property
    def java_For_Statement153(self):
        return self.__java_For_Statement153

    @java_For_Statement153.setter
    def java_For_Statement153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_For_Statement__java_For_Statement153", None)
        self.__java_For_Statement153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression154"):
                opp_val = getattr(old_value, "java_Expression154", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression154"):
                opp_val = getattr(value, "java_Expression154", None)
                setattr(value, "java_Expression154", self)

    @property
    def java_For_Statement162(self):
        return self.__java_For_Statement162

    @java_For_Statement162.setter
    def java_For_Statement162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_For_Statement__java_For_Statement162", None)
        self.__java_For_Statement162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement163"):
                opp_val = getattr(old_value, "java_Statement163", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement163"):
                opp_val = getattr(value, "java_Statement163", None)
                setattr(value, "java_Statement163", self)

    @property
    def java_For_Statement156(self):
        return self.__java_For_Statement156

    @java_For_Statement156.setter
    def java_For_Statement156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_For_Statement__java_For_Statement156", None)
        self.__java_For_Statement156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression157"):
                opp_val = getattr(old_value, "java_Expression157", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression157"):
                opp_val = getattr(value, "java_Expression157", None)
                setattr(value, "java_Expression157", self)

    @property
    def java_For_Statement159(self):
        return self.__java_For_Statement159

    @java_For_Statement159.setter
    def java_For_Statement159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_For_Statement__java_For_Statement159", None)
        self.__java_For_Statement159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression160"):
                opp_val = getattr(old_value, "java_Expression160", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression160"):
                opp_val = getattr(value, "java_Expression160", None)
                setattr(value, "java_Expression160", self)

    @property
    def java_For_Statement(self):
        return self.__java_For_Statement

    @java_For_Statement.setter
    def java_For_Statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_For_Statement__java_For_Statement", None)
        self.__java_For_Statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement132"):
                opp_val = getattr(old_value, "java_Statement132", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement132", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement132"):
                opp_val = getattr(value, "java_Statement132", None)
                setattr(value, "java_Statement132", self)

class java_While_Statement:

    pass
class java_Do_Statement:

    pass
class java_If_Statement:

    pass
class java_Return_Statement:

    pass
class Statement:

    pass
class java_Static_initializer:

    def __init__(self, static: str, java_Static_initializer: "java_Statement_block" = None):
        self.static = static
        self.java_Static_initializer = java_Static_initializer
        
    @property
    def static(self) -> str:
        return self.__static

    @static.setter
    def static(self, static: str):
        self.__static = static

    @property
    def java_Static_initializer(self):
        return self.__java_Static_initializer

    @java_Static_initializer.setter
    def java_Static_initializer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Static_initializer__java_Static_initializer", None)
        self.__java_Static_initializer = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement_block114"):
                opp_val = getattr(old_value, "java_Statement_block114", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement_block114", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement_block114"):
                opp_val = getattr(value, "java_Statement_block114", None)
                setattr(value, "java_Statement_block114", self)

class java_Float_Literal:

    def __init__(self, decimalDigits1: int, decimalDigits2: int, exp: str, floatTypeSufix: str, java_Float_Literal: "java_Literal_Expression" = None):
        self.decimalDigits1 = decimalDigits1
        self.decimalDigits2 = decimalDigits2
        self.exp = exp
        self.floatTypeSufix = floatTypeSufix
        self.java_Float_Literal = java_Float_Literal
        
    @property
    def decimalDigits1(self) -> int:
        return self.__decimalDigits1

    @decimalDigits1.setter
    def decimalDigits1(self, decimalDigits1: int):
        self.__decimalDigits1 = decimalDigits1

    @property
    def floatTypeSufix(self) -> str:
        return self.__floatTypeSufix

    @floatTypeSufix.setter
    def floatTypeSufix(self, floatTypeSufix: str):
        self.__floatTypeSufix = floatTypeSufix

    @property
    def decimalDigits2(self) -> int:
        return self.__decimalDigits2

    @decimalDigits2.setter
    def decimalDigits2(self, decimalDigits2: int):
        self.__decimalDigits2 = decimalDigits2

    @property
    def exp(self) -> str:
        return self.__exp

    @exp.setter
    def exp(self, exp: str):
        self.__exp = exp

    @property
    def java_Float_Literal(self):
        return self.__java_Float_Literal

    @java_Float_Literal.setter
    def java_Float_Literal(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Float_Literal__java_Float_Literal", None)
        self.__java_Float_Literal = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Literal_Expression85"):
                opp_val = getattr(old_value, "java_Literal_Expression85", None)
                if opp_val == self:
                    setattr(old_value, "java_Literal_Expression85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Literal_Expression85"):
                opp_val = getattr(value, "java_Literal_Expression85", None)
                setattr(value, "java_Literal_Expression85", self)

class java_Ampersand_Rule:

    def __init__(self, a1: str, a2: str, java_Ampersand_Rule: "java_Expression_aux" = None):
        self.a1 = a1
        self.a2 = a2
        self.java_Ampersand_Rule = java_Ampersand_Rule
        
    @property
    def a2(self) -> str:
        return self.__a2

    @a2.setter
    def a2(self, a2: str):
        self.__a2 = a2

    @property
    def a1(self) -> str:
        return self.__a1

    @a1.setter
    def a1(self, a1: str):
        self.__a1 = a1

    @property
    def java_Ampersand_Rule(self):
        return self.__java_Ampersand_Rule

    @java_Ampersand_Rule.setter
    def java_Ampersand_Rule(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Ampersand_Rule__java_Ampersand_Rule", None)
        self.__java_Ampersand_Rule = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression_aux80"):
                opp_val = getattr(old_value, "java_Expression_aux80", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression_aux80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression_aux80"):
                opp_val = getattr(value, "java_Expression_aux80", None)
                setattr(value, "java_Expression_aux80", self)

class java_Creating_Expression:

    def __init__(self, className: str, typeSpecifier: str, java_Creating_Expression: "java_Expression" = None, java_Creating_Expression87: "java_Arg_List" = None, java_Creating_Expression90: "java_Expression" = None):
        self.className = className
        self.typeSpecifier = typeSpecifier
        self.java_Creating_Expression = java_Creating_Expression
        self.java_Creating_Expression87 = java_Creating_Expression87
        self.java_Creating_Expression90 = java_Creating_Expression90
        
    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def typeSpecifier(self) -> str:
        return self.__typeSpecifier

    @typeSpecifier.setter
    def typeSpecifier(self, typeSpecifier: str):
        self.__typeSpecifier = typeSpecifier

    @property
    def java_Creating_Expression87(self):
        return self.__java_Creating_Expression87

    @java_Creating_Expression87.setter
    def java_Creating_Expression87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Creating_Expression__java_Creating_Expression87", None)
        self.__java_Creating_Expression87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Arg_List88"):
                opp_val = getattr(old_value, "java_Arg_List88", None)
                if opp_val == self:
                    setattr(old_value, "java_Arg_List88", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Arg_List88"):
                opp_val = getattr(value, "java_Arg_List88", None)
                setattr(value, "java_Arg_List88", self)

    @property
    def java_Creating_Expression(self):
        return self.__java_Creating_Expression

    @java_Creating_Expression.setter
    def java_Creating_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Creating_Expression__java_Creating_Expression", None)
        self.__java_Creating_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression62"):
                opp_val = getattr(old_value, "java_Expression62", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression62"):
                opp_val = getattr(value, "java_Expression62", None)
                setattr(value, "java_Expression62", self)

    @property
    def java_Creating_Expression90(self):
        return self.__java_Creating_Expression90

    @java_Creating_Expression90.setter
    def java_Creating_Expression90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Creating_Expression__java_Creating_Expression90", None)
        self.__java_Creating_Expression90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression91"):
                opp_val = getattr(old_value, "java_Expression91", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression91"):
                opp_val = getattr(value, "java_Expression91", None)
                setattr(value, "java_Expression91", self)

class java_Cast_Expression:

    pass
class java_Bit_Expression_NR:

    pass
class java_Logical_Expression_NR:

    def __init__(self, true: str, false: str, java_Logical_Expression_NR: "java_Expression" = None, java_Logical_Expression_NR102: "java_Expression" = None):
        self.true = true
        self.false = false
        self.java_Logical_Expression_NR = java_Logical_Expression_NR
        self.java_Logical_Expression_NR102 = java_Logical_Expression_NR102
        
    @property
    def true(self) -> str:
        return self.__true

    @true.setter
    def true(self, true: str):
        self.__true = true

    @property
    def false(self) -> str:
        return self.__false

    @false.setter
    def false(self, false: str):
        self.__false = false

    @property
    def java_Logical_Expression_NR102(self):
        return self.__java_Logical_Expression_NR102

    @java_Logical_Expression_NR102.setter
    def java_Logical_Expression_NR102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Logical_Expression_NR__java_Logical_Expression_NR102", None)
        self.__java_Logical_Expression_NR102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression103"):
                opp_val = getattr(old_value, "java_Expression103", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression103"):
                opp_val = getattr(value, "java_Expression103", None)
                setattr(value, "java_Expression103", self)

    @property
    def java_Logical_Expression_NR(self):
        return self.__java_Logical_Expression_NR

    @java_Logical_Expression_NR.setter
    def java_Logical_Expression_NR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Logical_Expression_NR__java_Logical_Expression_NR", None)
        self.__java_Logical_Expression_NR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression56"):
                opp_val = getattr(old_value, "java_Expression56", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression56"):
                opp_val = getattr(value, "java_Expression56", None)
                setattr(value, "java_Expression56", self)

class java_Expression_aux:

    def __init__(self, logicalSign: str, stringSign: str, bitSign: str, name: str, sgin: str, numericSign: str, testingSign: str, java_Expression_aux66: set["java_Arg_List"] = None, java_Expression_aux: "java_Expression" = None, java_Expression_aux77: "java_Expression" = None, java_Expression_aux80: "java_Ampersand_Rule" = None, java_Expression_aux82: "java_Expression" = None, java_Expression_aux69: "java_Expression_aux" = None, java_Expression_aux67: "java_Expression_aux" = None, java_Expression_aux71: "java_Expression" = None, java_Expression_aux74: "java_Expression" = None):
        self.logicalSign = logicalSign
        self.stringSign = stringSign
        self.bitSign = bitSign
        self.name = name
        self.sgin = sgin
        self.numericSign = numericSign
        self.testingSign = testingSign
        self.java_Expression_aux66 = java_Expression_aux66 if java_Expression_aux66 is not None else set()
        self.java_Expression_aux = java_Expression_aux
        self.java_Expression_aux77 = java_Expression_aux77
        self.java_Expression_aux80 = java_Expression_aux80
        self.java_Expression_aux82 = java_Expression_aux82
        self.java_Expression_aux69 = java_Expression_aux69
        self.java_Expression_aux67 = java_Expression_aux67
        self.java_Expression_aux71 = java_Expression_aux71
        self.java_Expression_aux74 = java_Expression_aux74
        
    @property
    def testingSign(self) -> str:
        return self.__testingSign

    @testingSign.setter
    def testingSign(self, testingSign: str):
        self.__testingSign = testingSign

    @property
    def stringSign(self) -> str:
        return self.__stringSign

    @stringSign.setter
    def stringSign(self, stringSign: str):
        self.__stringSign = stringSign

    @property
    def numericSign(self) -> str:
        return self.__numericSign

    @numericSign.setter
    def numericSign(self, numericSign: str):
        self.__numericSign = numericSign

    @property
    def bitSign(self) -> str:
        return self.__bitSign

    @bitSign.setter
    def bitSign(self, bitSign: str):
        self.__bitSign = bitSign

    @property
    def sgin(self) -> str:
        return self.__sgin

    @sgin.setter
    def sgin(self, sgin: str):
        self.__sgin = sgin

    @property
    def logicalSign(self) -> str:
        return self.__logicalSign

    @logicalSign.setter
    def logicalSign(self, logicalSign: str):
        self.__logicalSign = logicalSign

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Expression_aux71(self):
        return self.__java_Expression_aux71

    @java_Expression_aux71.setter
    def java_Expression_aux71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux71", None)
        self.__java_Expression_aux71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression72"):
                opp_val = getattr(old_value, "java_Expression72", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression72"):
                opp_val = getattr(value, "java_Expression72", None)
                setattr(value, "java_Expression72", self)

    @property
    def java_Expression_aux66(self):
        return self.__java_Expression_aux66

    @java_Expression_aux66.setter
    def java_Expression_aux66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux66", None)
        self.__java_Expression_aux66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Arg_List"):
                    opp_val = getattr(item, "java_Arg_List", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Arg_List", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Arg_List"):
                    opp_val = getattr(item, "java_Arg_List", None)
                    
                    setattr(item, "java_Arg_List", self)
                    

    @property
    def java_Expression_aux74(self):
        return self.__java_Expression_aux74

    @java_Expression_aux74.setter
    def java_Expression_aux74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux74", None)
        self.__java_Expression_aux74 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression75"):
                opp_val = getattr(old_value, "java_Expression75", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression75"):
                opp_val = getattr(value, "java_Expression75", None)
                setattr(value, "java_Expression75", self)

    @property
    def java_Expression_aux80(self):
        return self.__java_Expression_aux80

    @java_Expression_aux80.setter
    def java_Expression_aux80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux80", None)
        self.__java_Expression_aux80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Ampersand_Rule"):
                opp_val = getattr(old_value, "java_Ampersand_Rule", None)
                if opp_val == self:
                    setattr(old_value, "java_Ampersand_Rule", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Ampersand_Rule"):
                opp_val = getattr(value, "java_Ampersand_Rule", None)
                setattr(value, "java_Ampersand_Rule", self)

    @property
    def java_Expression_aux77(self):
        return self.__java_Expression_aux77

    @java_Expression_aux77.setter
    def java_Expression_aux77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux77", None)
        self.__java_Expression_aux77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression78"):
                opp_val = getattr(old_value, "java_Expression78", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression78", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression78"):
                opp_val = getattr(value, "java_Expression78", None)
                setattr(value, "java_Expression78", self)

    @property
    def java_Expression_aux82(self):
        return self.__java_Expression_aux82

    @java_Expression_aux82.setter
    def java_Expression_aux82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux82", None)
        self.__java_Expression_aux82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression83"):
                opp_val = getattr(old_value, "java_Expression83", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression83"):
                opp_val = getattr(value, "java_Expression83", None)
                setattr(value, "java_Expression83", self)

    @property
    def java_Expression_aux67(self):
        return self.__java_Expression_aux67

    @java_Expression_aux67.setter
    def java_Expression_aux67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux67", None)
        self.__java_Expression_aux67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression_aux69"):
                opp_val = getattr(old_value, "java_Expression_aux69", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression_aux69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression_aux69"):
                opp_val = getattr(value, "java_Expression_aux69", None)
                setattr(value, "java_Expression_aux69", self)

    @property
    def java_Expression_aux69(self):
        return self.__java_Expression_aux69

    @java_Expression_aux69.setter
    def java_Expression_aux69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux69", None)
        self.__java_Expression_aux69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression_aux67"):
                opp_val = getattr(old_value, "java_Expression_aux67", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression_aux67", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression_aux67"):
                opp_val = getattr(value, "java_Expression_aux67", None)
                setattr(value, "java_Expression_aux67", self)

    @property
    def java_Expression_aux(self):
        return self.__java_Expression_aux

    @java_Expression_aux.setter
    def java_Expression_aux(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression_aux__java_Expression_aux", None)
        self.__java_Expression_aux = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression54"):
                opp_val = getattr(old_value, "java_Expression54", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression54"):
                opp_val = getattr(value, "java_Expression54", None)
                setattr(value, "java_Expression54", self)

class java_Numeric_Expression_NR:

    def __init__(self, sinal_numeric: str, java_Numeric_Expression_NR: "java_Expression" = None, java_Numeric_Expression_NR111: "java_Expression" = None):
        self.sinal_numeric = sinal_numeric
        self.java_Numeric_Expression_NR = java_Numeric_Expression_NR
        self.java_Numeric_Expression_NR111 = java_Numeric_Expression_NR111
        
    @property
    def sinal_numeric(self) -> str:
        return self.__sinal_numeric

    @sinal_numeric.setter
    def sinal_numeric(self, sinal_numeric: str):
        self.__sinal_numeric = sinal_numeric

    @property
    def java_Numeric_Expression_NR111(self):
        return self.__java_Numeric_Expression_NR111

    @java_Numeric_Expression_NR111.setter
    def java_Numeric_Expression_NR111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Numeric_Expression_NR__java_Numeric_Expression_NR111", None)
        self.__java_Numeric_Expression_NR111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression112"):
                opp_val = getattr(old_value, "java_Expression112", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression112"):
                opp_val = getattr(value, "java_Expression112", None)
                setattr(value, "java_Expression112", self)

    @property
    def java_Numeric_Expression_NR(self):
        return self.__java_Numeric_Expression_NR

    @java_Numeric_Expression_NR.setter
    def java_Numeric_Expression_NR(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Numeric_Expression_NR__java_Numeric_Expression_NR", None)
        self.__java_Numeric_Expression_NR = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression52"):
                opp_val = getattr(old_value, "java_Expression52", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression52"):
                opp_val = getattr(value, "java_Expression52", None)
                setattr(value, "java_Expression52", self)

class java_Arg_List:

    pass
class java_Variable_declarator:

    def __init__(self, name: str, java_Variable_declarator42: "java_Variable_initializer" = None, java_Variable_declarator: "java_Variable_declaration" = None, java_Variable_declarator40: "java_Variable_declaration" = None):
        self.name = name
        self.java_Variable_declarator42 = java_Variable_declarator42
        self.java_Variable_declarator = java_Variable_declarator
        self.java_Variable_declarator40 = java_Variable_declarator40
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Variable_declarator(self):
        return self.__java_Variable_declarator

    @java_Variable_declarator.setter
    def java_Variable_declarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Variable_declarator__java_Variable_declarator", None)
        self.__java_Variable_declarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Variable_declaration37"):
                opp_val = getattr(old_value, "java_Variable_declaration37", None)
                if opp_val == self:
                    setattr(old_value, "java_Variable_declaration37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Variable_declaration37"):
                opp_val = getattr(value, "java_Variable_declaration37", None)
                setattr(value, "java_Variable_declaration37", self)

    @property
    def java_Variable_declarator40(self):
        return self.__java_Variable_declarator40

    @java_Variable_declarator40.setter
    def java_Variable_declarator40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Variable_declarator__java_Variable_declarator40", None)
        self.__java_Variable_declarator40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Variable_declaration39"):
                opp_val = getattr(old_value, "java_Variable_declaration39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Variable_declaration39"):
                opp_val = getattr(value, "java_Variable_declaration39", None)
                if opp_val is None:
                    setattr(value, "java_Variable_declaration39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Variable_declarator42(self):
        return self.__java_Variable_declarator42

    @java_Variable_declarator42.setter
    def java_Variable_declarator42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Variable_declarator__java_Variable_declarator42", None)
        self.__java_Variable_declarator42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Variable_initializer"):
                opp_val = getattr(old_value, "java_Variable_initializer", None)
                if opp_val == self:
                    setattr(old_value, "java_Variable_initializer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Variable_initializer"):
                opp_val = getattr(value, "java_Variable_initializer", None)
                setattr(value, "java_Variable_initializer", self)

class java_Variable_declaration:

    def __init__(self, modifiers: str, java_Variable_declaration: "java_Type" = None, java_Variable_declaration37: "java_Variable_declarator" = None, java_Variable_declaration39: set["java_Variable_declarator"] = None, java_Variable_declaration121: "java_Statement" = None, java_Variable_declaration151: "java_For_Statement" = None):
        self.modifiers = modifiers
        self.java_Variable_declaration = java_Variable_declaration
        self.java_Variable_declaration37 = java_Variable_declaration37
        self.java_Variable_declaration39 = java_Variable_declaration39 if java_Variable_declaration39 is not None else set()
        self.java_Variable_declaration121 = java_Variable_declaration121
        self.java_Variable_declaration151 = java_Variable_declaration151
        
    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def java_Variable_declaration121(self):
        return self.__java_Variable_declaration121

    @java_Variable_declaration121.setter
    def java_Variable_declaration121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Variable_declaration__java_Variable_declaration121", None)
        self.__java_Variable_declaration121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement120"):
                opp_val = getattr(old_value, "java_Statement120", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement120"):
                opp_val = getattr(value, "java_Statement120", None)
                setattr(value, "java_Statement120", self)

    @property
    def java_Variable_declaration37(self):
        return self.__java_Variable_declaration37

    @java_Variable_declaration37.setter
    def java_Variable_declaration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Variable_declaration__java_Variable_declaration37", None)
        self.__java_Variable_declaration37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Variable_declarator"):
                opp_val = getattr(old_value, "java_Variable_declarator", None)
                if opp_val == self:
                    setattr(old_value, "java_Variable_declarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Variable_declarator"):
                opp_val = getattr(value, "java_Variable_declarator", None)
                setattr(value, "java_Variable_declarator", self)

    @property
    def java_Variable_declaration39(self):
        return self.__java_Variable_declaration39

    @java_Variable_declaration39.setter
    def java_Variable_declaration39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Variable_declaration__java_Variable_declaration39", None)
        self.__java_Variable_declaration39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Variable_declarator40"):
                    opp_val = getattr(item, "java_Variable_declarator40", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Variable_declarator40", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Variable_declarator40"):
                    opp_val = getattr(item, "java_Variable_declarator40", None)
                    
                    setattr(item, "java_Variable_declarator40", self)
                    

    @property
    def java_Variable_declaration(self):
        return self.__java_Variable_declaration

    @java_Variable_declaration.setter
    def java_Variable_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Variable_declaration__java_Variable_declaration", None)
        self.__java_Variable_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Type35"):
                opp_val = getattr(old_value, "java_Type35", None)
                if opp_val == self:
                    setattr(old_value, "java_Type35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Type35"):
                opp_val = getattr(value, "java_Type35", None)
                setattr(value, "java_Type35", self)

    @property
    def java_Variable_declaration151(self):
        return self.__java_Variable_declaration151

    @java_Variable_declaration151.setter
    def java_Variable_declaration151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Variable_declaration__java_Variable_declaration151", None)
        self.__java_Variable_declaration151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_For_Statement150"):
                opp_val = getattr(old_value, "java_For_Statement150", None)
                if opp_val == self:
                    setattr(old_value, "java_For_Statement150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_For_Statement150"):
                opp_val = getattr(value, "java_For_Statement150", None)
                setattr(value, "java_For_Statement150", self)

class java_Expression:

    def __init__(self, null: str, super: str, this: str, name: str, java_Expression: "java_Variable_initializer" = None, java_Expression62: "java_Creating_Expression" = None, java_Expression64: "java_Literal_Expression" = None, java_Expression52: "java_Numeric_Expression_NR" = None, java_Expression54: "java_Expression_aux" = None, java_Expression56: "java_Logical_Expression_NR" = None, java_Expression58: "java_Bit_Expression_NR" = None, java_Expression60: "java_Cast_Expression" = None, java_Expression78: "java_Expression_aux" = None, java_Expression83: "java_Expression_aux" = None, java_Expression72: "java_Expression_aux" = None, java_Expression75: "java_Expression_aux" = None, java_Expression91: "java_Creating_Expression" = None, java_Expression97: "java_Cast_Expression" = None, java_Expression100: "java_Bit_Expression_NR" = None, java_Expression106: "java_Arg_List" = None, java_Expression109: "java_Arg_List" = None, java_Expression112: "java_Numeric_Expression_NR" = None, java_Expression103: "java_Logical_Expression_NR" = None, java_Expression124: "java_Statement" = None, java_Expression142: "java_Switch_Statement" = None, java_Expression145: "java_Switch_Statement" = None, java_Expression154: "java_For_Statement" = None, java_Expression157: "java_For_Statement" = None, java_Expression160: "java_For_Statement" = None, java_Expression166: "java_While_Statement" = None, java_Expression175: "java_Do_Statement" = None, java_Expression178: "java_If_Statement" = None):
        self.null = null
        self.super = super
        self.this = this
        self.name = name
        self.java_Expression = java_Expression
        self.java_Expression62 = java_Expression62
        self.java_Expression64 = java_Expression64
        self.java_Expression52 = java_Expression52
        self.java_Expression54 = java_Expression54
        self.java_Expression56 = java_Expression56
        self.java_Expression58 = java_Expression58
        self.java_Expression60 = java_Expression60
        self.java_Expression78 = java_Expression78
        self.java_Expression83 = java_Expression83
        self.java_Expression72 = java_Expression72
        self.java_Expression75 = java_Expression75
        self.java_Expression91 = java_Expression91
        self.java_Expression97 = java_Expression97
        self.java_Expression100 = java_Expression100
        self.java_Expression106 = java_Expression106
        self.java_Expression109 = java_Expression109
        self.java_Expression112 = java_Expression112
        self.java_Expression103 = java_Expression103
        self.java_Expression124 = java_Expression124
        self.java_Expression142 = java_Expression142
        self.java_Expression145 = java_Expression145
        self.java_Expression154 = java_Expression154
        self.java_Expression157 = java_Expression157
        self.java_Expression160 = java_Expression160
        self.java_Expression166 = java_Expression166
        self.java_Expression175 = java_Expression175
        self.java_Expression178 = java_Expression178
        
    @property
    def super(self) -> str:
        return self.__super

    @super.setter
    def super(self, super: str):
        self.__super = super

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def null(self) -> str:
        return self.__null

    @null.setter
    def null(self, null: str):
        self.__null = null

    @property
    def this(self) -> str:
        return self.__this

    @this.setter
    def this(self, this: str):
        self.__this = this

    @property
    def java_Expression72(self):
        return self.__java_Expression72

    @java_Expression72.setter
    def java_Expression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression72", None)
        self.__java_Expression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression_aux71"):
                opp_val = getattr(old_value, "java_Expression_aux71", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression_aux71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression_aux71"):
                opp_val = getattr(value, "java_Expression_aux71", None)
                setattr(value, "java_Expression_aux71", self)

    @property
    def java_Expression56(self):
        return self.__java_Expression56

    @java_Expression56.setter
    def java_Expression56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression56", None)
        self.__java_Expression56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Logical_Expression_NR"):
                opp_val = getattr(old_value, "java_Logical_Expression_NR", None)
                if opp_val == self:
                    setattr(old_value, "java_Logical_Expression_NR", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Logical_Expression_NR"):
                opp_val = getattr(value, "java_Logical_Expression_NR", None)
                setattr(value, "java_Logical_Expression_NR", self)

    @property
    def java_Expression100(self):
        return self.__java_Expression100

    @java_Expression100.setter
    def java_Expression100(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression100", None)
        self.__java_Expression100 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Bit_Expression_NR99"):
                opp_val = getattr(old_value, "java_Bit_Expression_NR99", None)
                if opp_val == self:
                    setattr(old_value, "java_Bit_Expression_NR99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Bit_Expression_NR99"):
                opp_val = getattr(value, "java_Bit_Expression_NR99", None)
                setattr(value, "java_Bit_Expression_NR99", self)

    @property
    def java_Expression109(self):
        return self.__java_Expression109

    @java_Expression109.setter
    def java_Expression109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression109", None)
        self.__java_Expression109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Arg_List108"):
                opp_val = getattr(old_value, "java_Arg_List108", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Arg_List108"):
                opp_val = getattr(value, "java_Arg_List108", None)
                if opp_val is None:
                    setattr(value, "java_Arg_List108", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Expression97(self):
        return self.__java_Expression97

    @java_Expression97.setter
    def java_Expression97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression97", None)
        self.__java_Expression97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Cast_Expression96"):
                opp_val = getattr(old_value, "java_Cast_Expression96", None)
                if opp_val == self:
                    setattr(old_value, "java_Cast_Expression96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Cast_Expression96"):
                opp_val = getattr(value, "java_Cast_Expression96", None)
                setattr(value, "java_Cast_Expression96", self)

    @property
    def java_Expression175(self):
        return self.__java_Expression175

    @java_Expression175.setter
    def java_Expression175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression175", None)
        self.__java_Expression175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Do_Statement174"):
                opp_val = getattr(old_value, "java_Do_Statement174", None)
                if opp_val == self:
                    setattr(old_value, "java_Do_Statement174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Do_Statement174"):
                opp_val = getattr(value, "java_Do_Statement174", None)
                setattr(value, "java_Do_Statement174", self)

    @property
    def java_Expression91(self):
        return self.__java_Expression91

    @java_Expression91.setter
    def java_Expression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression91", None)
        self.__java_Expression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Creating_Expression90"):
                opp_val = getattr(old_value, "java_Creating_Expression90", None)
                if opp_val == self:
                    setattr(old_value, "java_Creating_Expression90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Creating_Expression90"):
                opp_val = getattr(value, "java_Creating_Expression90", None)
                setattr(value, "java_Creating_Expression90", self)

    @property
    def java_Expression78(self):
        return self.__java_Expression78

    @java_Expression78.setter
    def java_Expression78(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression78", None)
        self.__java_Expression78 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression_aux77"):
                opp_val = getattr(old_value, "java_Expression_aux77", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression_aux77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression_aux77"):
                opp_val = getattr(value, "java_Expression_aux77", None)
                setattr(value, "java_Expression_aux77", self)

    @property
    def java_Expression106(self):
        return self.__java_Expression106

    @java_Expression106.setter
    def java_Expression106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression106", None)
        self.__java_Expression106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Arg_List105"):
                opp_val = getattr(old_value, "java_Arg_List105", None)
                if opp_val == self:
                    setattr(old_value, "java_Arg_List105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Arg_List105"):
                opp_val = getattr(value, "java_Arg_List105", None)
                setattr(value, "java_Arg_List105", self)

    @property
    def java_Expression124(self):
        return self.__java_Expression124

    @java_Expression124.setter
    def java_Expression124(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression124", None)
        self.__java_Expression124 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement123"):
                opp_val = getattr(old_value, "java_Statement123", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement123"):
                opp_val = getattr(value, "java_Statement123", None)
                setattr(value, "java_Statement123", self)

    @property
    def java_Expression54(self):
        return self.__java_Expression54

    @java_Expression54.setter
    def java_Expression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression54", None)
        self.__java_Expression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression_aux"):
                opp_val = getattr(old_value, "java_Expression_aux", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression_aux", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression_aux"):
                opp_val = getattr(value, "java_Expression_aux", None)
                setattr(value, "java_Expression_aux", self)

    @property
    def java_Expression157(self):
        return self.__java_Expression157

    @java_Expression157.setter
    def java_Expression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression157", None)
        self.__java_Expression157 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_For_Statement156"):
                opp_val = getattr(old_value, "java_For_Statement156", None)
                if opp_val == self:
                    setattr(old_value, "java_For_Statement156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_For_Statement156"):
                opp_val = getattr(value, "java_For_Statement156", None)
                setattr(value, "java_For_Statement156", self)

    @property
    def java_Expression160(self):
        return self.__java_Expression160

    @java_Expression160.setter
    def java_Expression160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression160", None)
        self.__java_Expression160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_For_Statement159"):
                opp_val = getattr(old_value, "java_For_Statement159", None)
                if opp_val == self:
                    setattr(old_value, "java_For_Statement159", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_For_Statement159"):
                opp_val = getattr(value, "java_For_Statement159", None)
                setattr(value, "java_For_Statement159", self)

    @property
    def java_Expression166(self):
        return self.__java_Expression166

    @java_Expression166.setter
    def java_Expression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression166", None)
        self.__java_Expression166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_While_Statement165"):
                opp_val = getattr(old_value, "java_While_Statement165", None)
                if opp_val == self:
                    setattr(old_value, "java_While_Statement165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_While_Statement165"):
                opp_val = getattr(value, "java_While_Statement165", None)
                setattr(value, "java_While_Statement165", self)

    @property
    def java_Expression112(self):
        return self.__java_Expression112

    @java_Expression112.setter
    def java_Expression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression112", None)
        self.__java_Expression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Numeric_Expression_NR111"):
                opp_val = getattr(old_value, "java_Numeric_Expression_NR111", None)
                if opp_val == self:
                    setattr(old_value, "java_Numeric_Expression_NR111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Numeric_Expression_NR111"):
                opp_val = getattr(value, "java_Numeric_Expression_NR111", None)
                setattr(value, "java_Numeric_Expression_NR111", self)

    @property
    def java_Expression58(self):
        return self.__java_Expression58

    @java_Expression58.setter
    def java_Expression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression58", None)
        self.__java_Expression58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Bit_Expression_NR"):
                opp_val = getattr(old_value, "java_Bit_Expression_NR", None)
                if opp_val == self:
                    setattr(old_value, "java_Bit_Expression_NR", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Bit_Expression_NR"):
                opp_val = getattr(value, "java_Bit_Expression_NR", None)
                setattr(value, "java_Bit_Expression_NR", self)

    @property
    def java_Expression103(self):
        return self.__java_Expression103

    @java_Expression103.setter
    def java_Expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression103", None)
        self.__java_Expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Logical_Expression_NR102"):
                opp_val = getattr(old_value, "java_Logical_Expression_NR102", None)
                if opp_val == self:
                    setattr(old_value, "java_Logical_Expression_NR102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Logical_Expression_NR102"):
                opp_val = getattr(value, "java_Logical_Expression_NR102", None)
                setattr(value, "java_Logical_Expression_NR102", self)

    @property
    def java_Expression62(self):
        return self.__java_Expression62

    @java_Expression62.setter
    def java_Expression62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression62", None)
        self.__java_Expression62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Creating_Expression"):
                opp_val = getattr(old_value, "java_Creating_Expression", None)
                if opp_val == self:
                    setattr(old_value, "java_Creating_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Creating_Expression"):
                opp_val = getattr(value, "java_Creating_Expression", None)
                setattr(value, "java_Creating_Expression", self)

    @property
    def java_Expression83(self):
        return self.__java_Expression83

    @java_Expression83.setter
    def java_Expression83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression83", None)
        self.__java_Expression83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression_aux82"):
                opp_val = getattr(old_value, "java_Expression_aux82", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression_aux82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression_aux82"):
                opp_val = getattr(value, "java_Expression_aux82", None)
                setattr(value, "java_Expression_aux82", self)

    @property
    def java_Expression75(self):
        return self.__java_Expression75

    @java_Expression75.setter
    def java_Expression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression75", None)
        self.__java_Expression75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression_aux74"):
                opp_val = getattr(old_value, "java_Expression_aux74", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression_aux74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression_aux74"):
                opp_val = getattr(value, "java_Expression_aux74", None)
                setattr(value, "java_Expression_aux74", self)

    @property
    def java_Expression142(self):
        return self.__java_Expression142

    @java_Expression142.setter
    def java_Expression142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression142", None)
        self.__java_Expression142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Switch_Statement141"):
                opp_val = getattr(old_value, "java_Switch_Statement141", None)
                if opp_val == self:
                    setattr(old_value, "java_Switch_Statement141", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Switch_Statement141"):
                opp_val = getattr(value, "java_Switch_Statement141", None)
                setattr(value, "java_Switch_Statement141", self)

    @property
    def java_Expression64(self):
        return self.__java_Expression64

    @java_Expression64.setter
    def java_Expression64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression64", None)
        self.__java_Expression64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Literal_Expression"):
                opp_val = getattr(old_value, "java_Literal_Expression", None)
                if opp_val == self:
                    setattr(old_value, "java_Literal_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Literal_Expression"):
                opp_val = getattr(value, "java_Literal_Expression", None)
                setattr(value, "java_Literal_Expression", self)

    @property
    def java_Expression154(self):
        return self.__java_Expression154

    @java_Expression154.setter
    def java_Expression154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression154", None)
        self.__java_Expression154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_For_Statement153"):
                opp_val = getattr(old_value, "java_For_Statement153", None)
                if opp_val == self:
                    setattr(old_value, "java_For_Statement153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_For_Statement153"):
                opp_val = getattr(value, "java_For_Statement153", None)
                setattr(value, "java_For_Statement153", self)

    @property
    def java_Expression52(self):
        return self.__java_Expression52

    @java_Expression52.setter
    def java_Expression52(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression52", None)
        self.__java_Expression52 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Numeric_Expression_NR"):
                opp_val = getattr(old_value, "java_Numeric_Expression_NR", None)
                if opp_val == self:
                    setattr(old_value, "java_Numeric_Expression_NR", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Numeric_Expression_NR"):
                opp_val = getattr(value, "java_Numeric_Expression_NR", None)
                setattr(value, "java_Numeric_Expression_NR", self)

    @property
    def java_Expression60(self):
        return self.__java_Expression60

    @java_Expression60.setter
    def java_Expression60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression60", None)
        self.__java_Expression60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Cast_Expression"):
                opp_val = getattr(old_value, "java_Cast_Expression", None)
                if opp_val == self:
                    setattr(old_value, "java_Cast_Expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Cast_Expression"):
                opp_val = getattr(value, "java_Cast_Expression", None)
                setattr(value, "java_Cast_Expression", self)

    @property
    def java_Expression178(self):
        return self.__java_Expression178

    @java_Expression178.setter
    def java_Expression178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression178", None)
        self.__java_Expression178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_If_Statement177"):
                opp_val = getattr(old_value, "java_If_Statement177", None)
                if opp_val == self:
                    setattr(old_value, "java_If_Statement177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_If_Statement177"):
                opp_val = getattr(value, "java_If_Statement177", None)
                setattr(value, "java_If_Statement177", self)

    @property
    def java_Expression(self):
        return self.__java_Expression

    @java_Expression.setter
    def java_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression", None)
        self.__java_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Variable_initializer44"):
                opp_val = getattr(old_value, "java_Variable_initializer44", None)
                if opp_val == self:
                    setattr(old_value, "java_Variable_initializer44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Variable_initializer44"):
                opp_val = getattr(value, "java_Variable_initializer44", None)
                setattr(value, "java_Variable_initializer44", self)

    @property
    def java_Expression145(self):
        return self.__java_Expression145

    @java_Expression145.setter
    def java_Expression145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Expression__java_Expression145", None)
        self.__java_Expression145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Switch_Statement144"):
                opp_val = getattr(old_value, "java_Switch_Statement144", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Switch_Statement144"):
                opp_val = getattr(value, "java_Switch_Statement144", None)
                if opp_val is None:
                    setattr(value, "java_Switch_Statement144", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_Variable_initializer:

    pass
class java_Constructor_declaration:

    def __init__(self, modifiers: str, name: str, java_Constructor_declaration: "java_Parameter_list" = None, java_Constructor_declaration24: "java_Statement_block" = None):
        self.modifiers = modifiers
        self.name = name
        self.java_Constructor_declaration = java_Constructor_declaration
        self.java_Constructor_declaration24 = java_Constructor_declaration24
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def java_Constructor_declaration(self):
        return self.__java_Constructor_declaration

    @java_Constructor_declaration.setter
    def java_Constructor_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Constructor_declaration__java_Constructor_declaration", None)
        self.__java_Constructor_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Parameter_list22"):
                opp_val = getattr(old_value, "java_Parameter_list22", None)
                if opp_val == self:
                    setattr(old_value, "java_Parameter_list22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Parameter_list22"):
                opp_val = getattr(value, "java_Parameter_list22", None)
                setattr(value, "java_Parameter_list22", self)

    @property
    def java_Constructor_declaration24(self):
        return self.__java_Constructor_declaration24

    @java_Constructor_declaration24.setter
    def java_Constructor_declaration24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Constructor_declaration__java_Constructor_declaration24", None)
        self.__java_Constructor_declaration24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement_block25"):
                opp_val = getattr(old_value, "java_Statement_block25", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement_block25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement_block25"):
                opp_val = getattr(value, "java_Statement_block25", None)
                setattr(value, "java_Statement_block25", self)

class java_Parameter_list_method_call:

    def __init__(self, name: str, parameters: str, java_Parameter_list_method_call: "java_Method_call" = None):
        self.name = name
        self.parameters = parameters
        self.java_Parameter_list_method_call = java_Parameter_list_method_call
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def parameters(self) -> str:
        return self.__parameters

    @parameters.setter
    def parameters(self, parameters: str):
        self.__parameters = parameters

    @property
    def java_Parameter_list_method_call(self):
        return self.__java_Parameter_list_method_call

    @java_Parameter_list_method_call.setter
    def java_Parameter_list_method_call(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Parameter_list_method_call__java_Parameter_list_method_call", None)
        self.__java_Parameter_list_method_call = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Method_call"):
                opp_val = getattr(old_value, "java_Method_call", None)
                if opp_val == self:
                    setattr(old_value, "java_Method_call", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Method_call"):
                opp_val = getattr(value, "java_Method_call", None)
                setattr(value, "java_Method_call", self)

class Return_value:

    pass
class java_Literal_Expression(Return_value):

    def __init__(self, string: str, char: str, exp: str, exp1: int, java_Literal_Expression: "java_Expression" = None, java_Literal_Expression85: "java_Float_Literal" = None):
        self.string = string
        self.char = char
        self.exp = exp
        self.exp1 = exp1
        self.java_Literal_Expression = java_Literal_Expression
        self.java_Literal_Expression85 = java_Literal_Expression85
        
    @property
    def exp1(self) -> int:
        return self.__exp1

    @exp1.setter
    def exp1(self, exp1: int):
        self.__exp1 = exp1

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def exp(self) -> str:
        return self.__exp

    @exp.setter
    def exp(self, exp: str):
        self.__exp = exp

    @property
    def char(self) -> str:
        return self.__char

    @char.setter
    def char(self, char: str):
        self.__char = char

    @property
    def java_Literal_Expression85(self):
        return self.__java_Literal_Expression85

    @java_Literal_Expression85.setter
    def java_Literal_Expression85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Literal_Expression__java_Literal_Expression85", None)
        self.__java_Literal_Expression85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Float_Literal"):
                opp_val = getattr(old_value, "java_Float_Literal", None)
                if opp_val == self:
                    setattr(old_value, "java_Float_Literal", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Float_Literal"):
                opp_val = getattr(value, "java_Float_Literal", None)
                setattr(value, "java_Float_Literal", self)

    @property
    def java_Literal_Expression(self):
        return self.__java_Literal_Expression

    @java_Literal_Expression.setter
    def java_Literal_Expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Literal_Expression__java_Literal_Expression", None)
        self.__java_Literal_Expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Expression64"):
                opp_val = getattr(old_value, "java_Expression64", None)
                if opp_val == self:
                    setattr(old_value, "java_Expression64", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Expression64"):
                opp_val = getattr(value, "java_Expression64", None)
                setattr(value, "java_Expression64", self)

class java_Method_call(Return_value):

    pass
class java_Statement_block(Statement):

    pass
class java_Parameter_list:

    pass
class java_Type:

    def __init__(self, name: str, java_Type: "java_Method_declaration" = None, java_Type33: "java_Parameter" = None, java_Type35: "java_Variable_declaration" = None, java_Type94: "java_Cast_Expression" = None):
        self.name = name
        self.java_Type = java_Type
        self.java_Type33 = java_Type33
        self.java_Type35 = java_Type35
        self.java_Type94 = java_Type94
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Type35(self):
        return self.__java_Type35

    @java_Type35.setter
    def java_Type35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Type__java_Type35", None)
        self.__java_Type35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Variable_declaration"):
                opp_val = getattr(old_value, "java_Variable_declaration", None)
                if opp_val == self:
                    setattr(old_value, "java_Variable_declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Variable_declaration"):
                opp_val = getattr(value, "java_Variable_declaration", None)
                setattr(value, "java_Variable_declaration", self)

    @property
    def java_Type(self):
        return self.__java_Type

    @java_Type.setter
    def java_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Type__java_Type", None)
        self.__java_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Method_declaration"):
                opp_val = getattr(old_value, "java_Method_declaration", None)
                if opp_val == self:
                    setattr(old_value, "java_Method_declaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Method_declaration"):
                opp_val = getattr(value, "java_Method_declaration", None)
                setattr(value, "java_Method_declaration", self)

    @property
    def java_Type33(self):
        return self.__java_Type33

    @java_Type33.setter
    def java_Type33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Type__java_Type33", None)
        self.__java_Type33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Parameter32"):
                opp_val = getattr(old_value, "java_Parameter32", None)
                if opp_val == self:
                    setattr(old_value, "java_Parameter32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Parameter32"):
                opp_val = getattr(value, "java_Parameter32", None)
                setattr(value, "java_Parameter32", self)

    @property
    def java_Type94(self):
        return self.__java_Type94

    @java_Type94.setter
    def java_Type94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Type__java_Type94", None)
        self.__java_Type94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Cast_Expression93"):
                opp_val = getattr(old_value, "java_Cast_Expression93", None)
                if opp_val == self:
                    setattr(old_value, "java_Cast_Expression93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Cast_Expression93"):
                opp_val = getattr(value, "java_Cast_Expression93", None)
                setattr(value, "java_Cast_Expression93", self)

class java_Parameter:

    def __init__(self, name: str, java_Parameter: "java_Parameter_list" = None, java_Parameter30: "java_Parameter_list" = None, java_Parameter32: "java_Type" = None, java_Parameter192: "java_Try_statement" = None):
        self.name = name
        self.java_Parameter = java_Parameter
        self.java_Parameter30 = java_Parameter30
        self.java_Parameter32 = java_Parameter32
        self.java_Parameter192 = java_Parameter192
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Parameter192(self):
        return self.__java_Parameter192

    @java_Parameter192.setter
    def java_Parameter192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Parameter__java_Parameter192", None)
        self.__java_Parameter192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Try_statement191"):
                opp_val = getattr(old_value, "java_Try_statement191", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Try_statement191"):
                opp_val = getattr(value, "java_Try_statement191", None)
                if opp_val is None:
                    setattr(value, "java_Try_statement191", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Parameter32(self):
        return self.__java_Parameter32

    @java_Parameter32.setter
    def java_Parameter32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Parameter__java_Parameter32", None)
        self.__java_Parameter32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Type33"):
                opp_val = getattr(old_value, "java_Type33", None)
                if opp_val == self:
                    setattr(old_value, "java_Type33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Type33"):
                opp_val = getattr(value, "java_Type33", None)
                setattr(value, "java_Type33", self)

    @property
    def java_Parameter(self):
        return self.__java_Parameter

    @java_Parameter.setter
    def java_Parameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Parameter__java_Parameter", None)
        self.__java_Parameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Parameter_list27"):
                opp_val = getattr(old_value, "java_Parameter_list27", None)
                if opp_val == self:
                    setattr(old_value, "java_Parameter_list27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Parameter_list27"):
                opp_val = getattr(value, "java_Parameter_list27", None)
                setattr(value, "java_Parameter_list27", self)

    @property
    def java_Parameter30(self):
        return self.__java_Parameter30

    @java_Parameter30.setter
    def java_Parameter30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Parameter__java_Parameter30", None)
        self.__java_Parameter30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Parameter_list29"):
                opp_val = getattr(old_value, "java_Parameter_list29", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Parameter_list29"):
                opp_val = getattr(value, "java_Parameter_list29", None)
                if opp_val is None:
                    setattr(value, "java_Parameter_list29", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_Class_declaration:

    def __init__(self, implements: str, modifiers: str, className: str, extend: str, implement: str, java_Class_declaration: set["java_Field_declaration"] = None):
        self.implements = implements
        self.modifiers = modifiers
        self.className = className
        self.extend = extend
        self.implement = implement
        self.java_Class_declaration = java_Class_declaration if java_Class_declaration is not None else set()
        
    @property
    def implement(self) -> str:
        return self.__implement

    @implement.setter
    def implement(self, implement: str):
        self.__implement = implement

    @property
    def className(self) -> str:
        return self.__className

    @className.setter
    def className(self, className: str):
        self.__className = className

    @property
    def extend(self) -> str:
        return self.__extend

    @extend.setter
    def extend(self, extend: str):
        self.__extend = extend

    @property
    def implements(self) -> str:
        return self.__implements

    @implements.setter
    def implements(self, implements: str):
        self.__implements = implements

    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def java_Class_declaration(self):
        return self.__java_Class_declaration

    @java_Class_declaration.setter
    def java_Class_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Class_declaration__java_Class_declaration", None)
        self.__java_Class_declaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Field_declaration11"):
                    opp_val = getattr(item, "java_Field_declaration11", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Field_declaration11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Field_declaration11"):
                    opp_val = getattr(item, "java_Field_declaration11", None)
                    
                    setattr(item, "java_Field_declaration11", self)
                    

class java_Field_declaration:

    def __init__(self, doc: str, debug: str, java_Field_declaration11: "java_Class_declaration" = None, java_Field_declaration13: "java_EObject" = None, java_Field_declaration: "java_Interface_declaration" = None):
        self.doc = doc
        self.debug = debug
        self.java_Field_declaration11 = java_Field_declaration11
        self.java_Field_declaration13 = java_Field_declaration13
        self.java_Field_declaration = java_Field_declaration
        
    @property
    def doc(self) -> str:
        return self.__doc

    @doc.setter
    def doc(self, doc: str):
        self.__doc = doc

    @property
    def debug(self) -> str:
        return self.__debug

    @debug.setter
    def debug(self, debug: str):
        self.__debug = debug

    @property
    def java_Field_declaration13(self):
        return self.__java_Field_declaration13

    @java_Field_declaration13.setter
    def java_Field_declaration13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Field_declaration__java_Field_declaration13", None)
        self.__java_Field_declaration13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_EObject14"):
                opp_val = getattr(old_value, "java_EObject14", None)
                if opp_val == self:
                    setattr(old_value, "java_EObject14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_EObject14"):
                opp_val = getattr(value, "java_EObject14", None)
                setattr(value, "java_EObject14", self)

    @property
    def java_Field_declaration11(self):
        return self.__java_Field_declaration11

    @java_Field_declaration11.setter
    def java_Field_declaration11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Field_declaration__java_Field_declaration11", None)
        self.__java_Field_declaration11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Class_declaration"):
                opp_val = getattr(old_value, "java_Class_declaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Class_declaration"):
                opp_val = getattr(value, "java_Class_declaration", None)
                if opp_val is None:
                    setattr(value, "java_Class_declaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def java_Field_declaration(self):
        return self.__java_Field_declaration

    @java_Field_declaration.setter
    def java_Field_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Field_declaration__java_Field_declaration", None)
        self.__java_Field_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Interface_declaration"):
                opp_val = getattr(old_value, "java_Interface_declaration", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Interface_declaration"):
                opp_val = getattr(value, "java_Interface_declaration", None)
                if opp_val is None:
                    setattr(value, "java_Interface_declaration", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_Method_declaration:

    def __init__(self, modifiers: str, name: str, debug: str, java_Method_declaration: "java_Type" = None, java_Method_declaration17: "java_Parameter_list" = None, java_Method_declaration19: "java_Statement_block" = None):
        self.modifiers = modifiers
        self.name = name
        self.debug = debug
        self.java_Method_declaration = java_Method_declaration
        self.java_Method_declaration17 = java_Method_declaration17
        self.java_Method_declaration19 = java_Method_declaration19
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def debug(self) -> str:
        return self.__debug

    @debug.setter
    def debug(self, debug: str):
        self.__debug = debug

    @property
    def java_Method_declaration17(self):
        return self.__java_Method_declaration17

    @java_Method_declaration17.setter
    def java_Method_declaration17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method_declaration__java_Method_declaration17", None)
        self.__java_Method_declaration17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Parameter_list"):
                opp_val = getattr(old_value, "java_Parameter_list", None)
                if opp_val == self:
                    setattr(old_value, "java_Parameter_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Parameter_list"):
                opp_val = getattr(value, "java_Parameter_list", None)
                setattr(value, "java_Parameter_list", self)

    @property
    def java_Method_declaration(self):
        return self.__java_Method_declaration

    @java_Method_declaration.setter
    def java_Method_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method_declaration__java_Method_declaration", None)
        self.__java_Method_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Type"):
                opp_val = getattr(old_value, "java_Type", None)
                if opp_val == self:
                    setattr(old_value, "java_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Type"):
                opp_val = getattr(value, "java_Type", None)
                setattr(value, "java_Type", self)

    @property
    def java_Method_declaration19(self):
        return self.__java_Method_declaration19

    @java_Method_declaration19.setter
    def java_Method_declaration19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Method_declaration__java_Method_declaration19", None)
        self.__java_Method_declaration19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Statement_block"):
                opp_val = getattr(old_value, "java_Statement_block", None)
                if opp_val == self:
                    setattr(old_value, "java_Statement_block", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Statement_block"):
                opp_val = getattr(value, "java_Statement_block", None)
                setattr(value, "java_Statement_block", self)

class java_Import_statement:

    def __init__(self, classname: str, packagename: str, java_Import_statement: "java_Compilation_unit" = None):
        self.classname = classname
        self.packagename = packagename
        self.java_Import_statement = java_Import_statement
        
    @property
    def packagename(self) -> str:
        return self.__packagename

    @packagename.setter
    def packagename(self, packagename: str):
        self.__packagename = packagename

    @property
    def classname(self) -> str:
        return self.__classname

    @classname.setter
    def classname(self, classname: str):
        self.__classname = classname

    @property
    def java_Import_statement(self):
        return self.__java_Import_statement

    @java_Import_statement.setter
    def java_Import_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Import_statement__java_Import_statement", None)
        self.__java_Import_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Compilation_unit4"):
                opp_val = getattr(old_value, "java_Compilation_unit4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Compilation_unit4"):
                opp_val = getattr(value, "java_Compilation_unit4", None)
                if opp_val is None:
                    setattr(value, "java_Compilation_unit4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_Package_statement:

    def __init__(self, name: str, java_Package_statement: "java_Compilation_unit" = None):
        self.name = name
        self.java_Package_statement = java_Package_statement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def java_Package_statement(self):
        return self.__java_Package_statement

    @java_Package_statement.setter
    def java_Package_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Package_statement__java_Package_statement", None)
        self.__java_Package_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Compilation_unit2"):
                opp_val = getattr(old_value, "java_Compilation_unit2", None)
                if opp_val == self:
                    setattr(old_value, "java_Compilation_unit2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Compilation_unit2"):
                opp_val = getattr(value, "java_Compilation_unit2", None)
                setattr(value, "java_Compilation_unit2", self)

class java_Compilation_unit:

    pass
class java_Interface_declaration:

    def __init__(self, modifiers: str, interfaceName: str, extend: str, extends: str, java_Interface_declaration: set["java_Field_declaration"] = None):
        self.modifiers = modifiers
        self.interfaceName = interfaceName
        self.extend = extend
        self.extends = extends
        self.java_Interface_declaration = java_Interface_declaration if java_Interface_declaration is not None else set()
        
    @property
    def interfaceName(self) -> str:
        return self.__interfaceName

    @interfaceName.setter
    def interfaceName(self, interfaceName: str):
        self.__interfaceName = interfaceName

    @property
    def extend(self) -> str:
        return self.__extend

    @extend.setter
    def extend(self, extend: str):
        self.__extend = extend

    @property
    def extends(self) -> str:
        return self.__extends

    @extends.setter
    def extends(self, extends: str):
        self.__extends = extends

    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def java_Interface_declaration(self):
        return self.__java_Interface_declaration

    @java_Interface_declaration.setter
    def java_Interface_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Interface_declaration__java_Interface_declaration", None)
        self.__java_Interface_declaration = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "java_Field_declaration"):
                    opp_val = getattr(item, "java_Field_declaration", None)
                    
                    if opp_val == self:
                        setattr(item, "java_Field_declaration", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "java_Field_declaration"):
                    opp_val = getattr(item, "java_Field_declaration", None)
                    
                    setattr(item, "java_Field_declaration", self)
                    

class java_EObject:

    pass
class java_Type_declaration:

    def __init__(self, doc: str, java_Type_declaration: "java_Compilation_unit" = None, java_Type_declaration8: "java_EObject" = None):
        self.doc = doc
        self.java_Type_declaration = java_Type_declaration
        self.java_Type_declaration8 = java_Type_declaration8
        
    @property
    def doc(self) -> str:
        return self.__doc

    @doc.setter
    def doc(self, doc: str):
        self.__doc = doc

    @property
    def java_Type_declaration8(self):
        return self.__java_Type_declaration8

    @java_Type_declaration8.setter
    def java_Type_declaration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Type_declaration__java_Type_declaration8", None)
        self.__java_Type_declaration8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_EObject"):
                opp_val = getattr(old_value, "java_EObject", None)
                if opp_val == self:
                    setattr(old_value, "java_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_EObject"):
                opp_val = getattr(value, "java_EObject", None)
                setattr(value, "java_EObject", self)

    @property
    def java_Type_declaration(self):
        return self.__java_Type_declaration

    @java_Type_declaration.setter
    def java_Type_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_java_Type_declaration__java_Type_declaration", None)
        self.__java_Type_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "java_Compilation_unit6"):
                opp_val = getattr(old_value, "java_Compilation_unit6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "java_Compilation_unit6"):
                opp_val = getattr(value, "java_Compilation_unit6", None)
                if opp_val is None:
                    setattr(value, "java_Compilation_unit6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class java_Head:

    pass