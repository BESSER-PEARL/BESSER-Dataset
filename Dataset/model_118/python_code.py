from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Primary:

    pass
class javaDsl_PrimaryNoNewArray(Primary):

    def __init__(self, reference: str, literal: str, keyword: str, method: str, javaDsl_PrimaryNoNewArray: "javaDsl_ClassInstanceCreationExpression" = None, javaDsl_PrimaryNoNewArray203: "javaDsl_ArrayAccess" = None):
        self.reference = reference
        self.literal = literal
        self.keyword = keyword
        self.method = method
        self.javaDsl_PrimaryNoNewArray = javaDsl_PrimaryNoNewArray
        self.javaDsl_PrimaryNoNewArray203 = javaDsl_PrimaryNoNewArray203
        
    @property
    def literal(self) -> str:
        return self.__literal

    @literal.setter
    def literal(self, literal: str):
        self.__literal = literal

    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def javaDsl_PrimaryNoNewArray203(self):
        return self.__javaDsl_PrimaryNoNewArray203

    @javaDsl_PrimaryNoNewArray203.setter
    def javaDsl_PrimaryNoNewArray203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_PrimaryNoNewArray__javaDsl_PrimaryNoNewArray203", None)
        self.__javaDsl_PrimaryNoNewArray203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ArrayAccess"):
                opp_val = getattr(old_value, "javaDsl_ArrayAccess", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ArrayAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ArrayAccess"):
                opp_val = getattr(value, "javaDsl_ArrayAccess", None)
                setattr(value, "javaDsl_ArrayAccess", self)

    @property
    def javaDsl_PrimaryNoNewArray(self):
        return self.__javaDsl_PrimaryNoNewArray

    @javaDsl_PrimaryNoNewArray.setter
    def javaDsl_PrimaryNoNewArray(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_PrimaryNoNewArray__javaDsl_PrimaryNoNewArray", None)
        self.__javaDsl_PrimaryNoNewArray = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ClassInstanceCreationExpression"):
                opp_val = getattr(old_value, "javaDsl_ClassInstanceCreationExpression", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ClassInstanceCreationExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ClassInstanceCreationExpression"):
                opp_val = getattr(value, "javaDsl_ClassInstanceCreationExpression", None)
                setattr(value, "javaDsl_ClassInstanceCreationExpression", self)

class javaDsl_ArrayExpression:

    pass
class javaDsl_ArrayCreationExpression:

    def __init__(self, type: str, layers: str, javaDsl_ArrayCreationExpression: "javaDsl_PrimaryNewArray" = None, javaDsl_ArrayCreationExpression197: set["javaDsl_ArrayExpression"] = None):
        self.type = type
        self.layers = layers
        self.javaDsl_ArrayCreationExpression = javaDsl_ArrayCreationExpression
        self.javaDsl_ArrayCreationExpression197 = javaDsl_ArrayCreationExpression197 if javaDsl_ArrayCreationExpression197 is not None else set()
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def layers(self) -> str:
        return self.__layers

    @layers.setter
    def layers(self, layers: str):
        self.__layers = layers

    @property
    def javaDsl_ArrayCreationExpression197(self):
        return self.__javaDsl_ArrayCreationExpression197

    @javaDsl_ArrayCreationExpression197.setter
    def javaDsl_ArrayCreationExpression197(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ArrayCreationExpression__javaDsl_ArrayCreationExpression197", None)
        self.__javaDsl_ArrayCreationExpression197 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_ArrayExpression198"):
                    opp_val = getattr(item, "javaDsl_ArrayExpression198", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_ArrayExpression198", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_ArrayExpression198"):
                    opp_val = getattr(item, "javaDsl_ArrayExpression198", None)
                    
                    setattr(item, "javaDsl_ArrayExpression198", self)
                    

    @property
    def javaDsl_ArrayCreationExpression(self):
        return self.__javaDsl_ArrayCreationExpression

    @javaDsl_ArrayCreationExpression.setter
    def javaDsl_ArrayCreationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ArrayCreationExpression__javaDsl_ArrayCreationExpression", None)
        self.__javaDsl_ArrayCreationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_PrimaryNewArray"):
                opp_val = getattr(old_value, "javaDsl_PrimaryNewArray", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_PrimaryNewArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_PrimaryNewArray"):
                opp_val = getattr(value, "javaDsl_PrimaryNewArray", None)
                setattr(value, "javaDsl_PrimaryNewArray", self)

class javaDsl_PrimaryNewArray(Primary):

    pass
class NoArrayExpression:

    pass
class NoArrayExpressionWithoutMinus:

    pass
class javaDsl_CastExpression(NoArrayExpressionWithoutMinus):

    def __init__(self, type: str):
        self.type = type
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

class javaDsl_NoArrayExpression:

    def __init__(self, operator: str, javaDsl_NoArrayExpression: "javaDsl_MultiplicativeExpression" = None, javaDsl_NoArrayExpression174: "javaDsl_NoArrayExpression" = None, javaDsl_NoArrayExpression172: "javaDsl_NoArrayExpression" = None):
        self.operator = operator
        self.javaDsl_NoArrayExpression = javaDsl_NoArrayExpression
        self.javaDsl_NoArrayExpression174 = javaDsl_NoArrayExpression174
        self.javaDsl_NoArrayExpression172 = javaDsl_NoArrayExpression172
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javaDsl_NoArrayExpression174(self):
        return self.__javaDsl_NoArrayExpression174

    @javaDsl_NoArrayExpression174.setter
    def javaDsl_NoArrayExpression174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_NoArrayExpression__javaDsl_NoArrayExpression174", None)
        self.__javaDsl_NoArrayExpression174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_NoArrayExpression172"):
                opp_val = getattr(old_value, "javaDsl_NoArrayExpression172", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_NoArrayExpression172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_NoArrayExpression172"):
                opp_val = getattr(value, "javaDsl_NoArrayExpression172", None)
                setattr(value, "javaDsl_NoArrayExpression172", self)

    @property
    def javaDsl_NoArrayExpression172(self):
        return self.__javaDsl_NoArrayExpression172

    @javaDsl_NoArrayExpression172.setter
    def javaDsl_NoArrayExpression172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_NoArrayExpression__javaDsl_NoArrayExpression172", None)
        self.__javaDsl_NoArrayExpression172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_NoArrayExpression174"):
                opp_val = getattr(old_value, "javaDsl_NoArrayExpression174", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_NoArrayExpression174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_NoArrayExpression174"):
                opp_val = getattr(value, "javaDsl_NoArrayExpression174", None)
                setattr(value, "javaDsl_NoArrayExpression174", self)

    @property
    def javaDsl_NoArrayExpression(self):
        return self.__javaDsl_NoArrayExpression

    @javaDsl_NoArrayExpression.setter
    def javaDsl_NoArrayExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_NoArrayExpression__javaDsl_NoArrayExpression", None)
        self.__javaDsl_NoArrayExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_MultiplicativeExpression171"):
                opp_val = getattr(old_value, "javaDsl_MultiplicativeExpression171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_MultiplicativeExpression171"):
                opp_val = getattr(value, "javaDsl_MultiplicativeExpression171", None)
                if opp_val is None:
                    setattr(value, "javaDsl_MultiplicativeExpression171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class LeftHandSide:

    pass
class javaDsl_ArrayAccess(LeftHandSide):

    def __init__(self, reference: str, javaDsl_ArrayAccess: "javaDsl_PrimaryNoNewArray" = None, javaDsl_ArrayAccess205: "javaDsl_ArrayExpression" = None):
        self.reference = reference
        self.javaDsl_ArrayAccess = javaDsl_ArrayAccess
        self.javaDsl_ArrayAccess205 = javaDsl_ArrayAccess205
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def javaDsl_ArrayAccess(self):
        return self.__javaDsl_ArrayAccess

    @javaDsl_ArrayAccess.setter
    def javaDsl_ArrayAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ArrayAccess__javaDsl_ArrayAccess", None)
        self.__javaDsl_ArrayAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_PrimaryNoNewArray203"):
                opp_val = getattr(old_value, "javaDsl_PrimaryNoNewArray203", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_PrimaryNoNewArray203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_PrimaryNoNewArray203"):
                opp_val = getattr(value, "javaDsl_PrimaryNoNewArray203", None)
                setattr(value, "javaDsl_PrimaryNoNewArray203", self)

    @property
    def javaDsl_ArrayAccess205(self):
        return self.__javaDsl_ArrayAccess205

    @javaDsl_ArrayAccess205.setter
    def javaDsl_ArrayAccess205(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ArrayAccess__javaDsl_ArrayAccess205", None)
        self.__javaDsl_ArrayAccess205 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ArrayExpression206"):
                opp_val = getattr(old_value, "javaDsl_ArrayExpression206", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ArrayExpression206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ArrayExpression206"):
                opp_val = getattr(value, "javaDsl_ArrayExpression206", None)
                setattr(value, "javaDsl_ArrayExpression206", self)

class javaDsl_FieldAccess(LeftHandSide):

    def __init__(self, field: str, keyword: str, javaDsl_FieldAccess: "javaDsl_Primary" = None):
        self.field = field
        self.keyword = keyword
        self.javaDsl_FieldAccess = javaDsl_FieldAccess
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def field(self) -> str:
        return self.__field

    @field.setter
    def field(self, field: str):
        self.__field = field

    @property
    def javaDsl_FieldAccess(self):
        return self.__javaDsl_FieldAccess

    @javaDsl_FieldAccess.setter
    def javaDsl_FieldAccess(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_FieldAccess__javaDsl_FieldAccess", None)
        self.__javaDsl_FieldAccess = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Primary182"):
                opp_val = getattr(old_value, "javaDsl_Primary182", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Primary182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Primary182"):
                opp_val = getattr(value, "javaDsl_Primary182", None)
                setattr(value, "javaDsl_Primary182", self)

class javaDsl_Primary:

    def __init__(self, fields: str, javaDsl_Primary: "javaDsl_PostfixExpression" = None, javaDsl_Primary180: "javaDsl_MethodInvocation" = None, javaDsl_Primary182: "javaDsl_FieldAccess" = None, javaDsl_Primary184: set["javaDsl_ArgumentList"] = None, javaDsl_Primary187: set["javaDsl_ArrayExpression"] = None):
        self.fields = fields
        self.javaDsl_Primary = javaDsl_Primary
        self.javaDsl_Primary180 = javaDsl_Primary180
        self.javaDsl_Primary182 = javaDsl_Primary182
        self.javaDsl_Primary184 = javaDsl_Primary184 if javaDsl_Primary184 is not None else set()
        self.javaDsl_Primary187 = javaDsl_Primary187 if javaDsl_Primary187 is not None else set()
        
    @property
    def fields(self) -> str:
        return self.__fields

    @fields.setter
    def fields(self, fields: str):
        self.__fields = fields

    @property
    def javaDsl_Primary182(self):
        return self.__javaDsl_Primary182

    @javaDsl_Primary182.setter
    def javaDsl_Primary182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Primary__javaDsl_Primary182", None)
        self.__javaDsl_Primary182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_FieldAccess"):
                opp_val = getattr(old_value, "javaDsl_FieldAccess", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_FieldAccess", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_FieldAccess"):
                opp_val = getattr(value, "javaDsl_FieldAccess", None)
                setattr(value, "javaDsl_FieldAccess", self)

    @property
    def javaDsl_Primary184(self):
        return self.__javaDsl_Primary184

    @javaDsl_Primary184.setter
    def javaDsl_Primary184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Primary__javaDsl_Primary184", None)
        self.__javaDsl_Primary184 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_ArgumentList185"):
                    opp_val = getattr(item, "javaDsl_ArgumentList185", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_ArgumentList185", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_ArgumentList185"):
                    opp_val = getattr(item, "javaDsl_ArgumentList185", None)
                    
                    setattr(item, "javaDsl_ArgumentList185", self)
                    

    @property
    def javaDsl_Primary(self):
        return self.__javaDsl_Primary

    @javaDsl_Primary.setter
    def javaDsl_Primary(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Primary__javaDsl_Primary", None)
        self.__javaDsl_Primary = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_PostfixExpression"):
                opp_val = getattr(old_value, "javaDsl_PostfixExpression", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_PostfixExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_PostfixExpression"):
                opp_val = getattr(value, "javaDsl_PostfixExpression", None)
                setattr(value, "javaDsl_PostfixExpression", self)

    @property
    def javaDsl_Primary187(self):
        return self.__javaDsl_Primary187

    @javaDsl_Primary187.setter
    def javaDsl_Primary187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Primary__javaDsl_Primary187", None)
        self.__javaDsl_Primary187 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_ArrayExpression"):
                    opp_val = getattr(item, "javaDsl_ArrayExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_ArrayExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_ArrayExpression"):
                    opp_val = getattr(item, "javaDsl_ArrayExpression", None)
                    
                    setattr(item, "javaDsl_ArrayExpression", self)
                    

    @property
    def javaDsl_Primary180(self):
        return self.__javaDsl_Primary180

    @javaDsl_Primary180.setter
    def javaDsl_Primary180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Primary__javaDsl_Primary180", None)
        self.__javaDsl_Primary180 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_MethodInvocation179"):
                opp_val = getattr(old_value, "javaDsl_MethodInvocation179", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_MethodInvocation179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_MethodInvocation179"):
                opp_val = getattr(value, "javaDsl_MethodInvocation179", None)
                setattr(value, "javaDsl_MethodInvocation179", self)

class javaDsl_NoArrayExpressionWithoutMinus(NoArrayExpression):

    pass
class javaDsl_InclusiveOrExpression:

    def __init__(self, operators: str, javaDsl_InclusiveOrExpression157: set["javaDsl_ExclusiveOrExpression"] = None, javaDsl_InclusiveOrExpression: "javaDsl_ConditionalAndExpression" = None):
        self.operators = operators
        self.javaDsl_InclusiveOrExpression157 = javaDsl_InclusiveOrExpression157 if javaDsl_InclusiveOrExpression157 is not None else set()
        self.javaDsl_InclusiveOrExpression = javaDsl_InclusiveOrExpression
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_InclusiveOrExpression(self):
        return self.__javaDsl_InclusiveOrExpression

    @javaDsl_InclusiveOrExpression.setter
    def javaDsl_InclusiveOrExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_InclusiveOrExpression__javaDsl_InclusiveOrExpression", None)
        self.__javaDsl_InclusiveOrExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConditionalAndExpression155"):
                opp_val = getattr(old_value, "javaDsl_ConditionalAndExpression155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConditionalAndExpression155"):
                opp_val = getattr(value, "javaDsl_ConditionalAndExpression155", None)
                if opp_val is None:
                    setattr(value, "javaDsl_ConditionalAndExpression155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaDsl_InclusiveOrExpression157(self):
        return self.__javaDsl_InclusiveOrExpression157

    @javaDsl_InclusiveOrExpression157.setter
    def javaDsl_InclusiveOrExpression157(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_InclusiveOrExpression__javaDsl_InclusiveOrExpression157", None)
        self.__javaDsl_InclusiveOrExpression157 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_ExclusiveOrExpression"):
                    opp_val = getattr(item, "javaDsl_ExclusiveOrExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_ExclusiveOrExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_ExclusiveOrExpression"):
                    opp_val = getattr(item, "javaDsl_ExclusiveOrExpression", None)
                    
                    setattr(item, "javaDsl_ExclusiveOrExpression", self)
                    

class javaDsl_ConditionalAndExpression:

    def __init__(self, operators: str, javaDsl_ConditionalAndExpression: "javaDsl_ConditionalOrExpression" = None, javaDsl_ConditionalAndExpression155: set["javaDsl_InclusiveOrExpression"] = None):
        self.operators = operators
        self.javaDsl_ConditionalAndExpression = javaDsl_ConditionalAndExpression
        self.javaDsl_ConditionalAndExpression155 = javaDsl_ConditionalAndExpression155 if javaDsl_ConditionalAndExpression155 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_ConditionalAndExpression155(self):
        return self.__javaDsl_ConditionalAndExpression155

    @javaDsl_ConditionalAndExpression155.setter
    def javaDsl_ConditionalAndExpression155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConditionalAndExpression__javaDsl_ConditionalAndExpression155", None)
        self.__javaDsl_ConditionalAndExpression155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_InclusiveOrExpression"):
                    opp_val = getattr(item, "javaDsl_InclusiveOrExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_InclusiveOrExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_InclusiveOrExpression"):
                    opp_val = getattr(item, "javaDsl_InclusiveOrExpression", None)
                    
                    setattr(item, "javaDsl_InclusiveOrExpression", self)
                    

    @property
    def javaDsl_ConditionalAndExpression(self):
        return self.__javaDsl_ConditionalAndExpression

    @javaDsl_ConditionalAndExpression.setter
    def javaDsl_ConditionalAndExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConditionalAndExpression__javaDsl_ConditionalAndExpression", None)
        self.__javaDsl_ConditionalAndExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConditionalOrExpression153"):
                opp_val = getattr(old_value, "javaDsl_ConditionalOrExpression153", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConditionalOrExpression153"):
                opp_val = getattr(value, "javaDsl_ConditionalOrExpression153", None)
                if opp_val is None:
                    setattr(value, "javaDsl_ConditionalOrExpression153", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_ConditionalOrExpression:

    def __init__(self, operators: str, javaDsl_ConditionalOrExpression: "javaDsl_ConditionalExpression" = None, javaDsl_ConditionalOrExpression153: set["javaDsl_ConditionalAndExpression"] = None):
        self.operators = operators
        self.javaDsl_ConditionalOrExpression = javaDsl_ConditionalOrExpression
        self.javaDsl_ConditionalOrExpression153 = javaDsl_ConditionalOrExpression153 if javaDsl_ConditionalOrExpression153 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_ConditionalOrExpression153(self):
        return self.__javaDsl_ConditionalOrExpression153

    @javaDsl_ConditionalOrExpression153.setter
    def javaDsl_ConditionalOrExpression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConditionalOrExpression__javaDsl_ConditionalOrExpression153", None)
        self.__javaDsl_ConditionalOrExpression153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_ConditionalAndExpression"):
                    opp_val = getattr(item, "javaDsl_ConditionalAndExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_ConditionalAndExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_ConditionalAndExpression"):
                    opp_val = getattr(item, "javaDsl_ConditionalAndExpression", None)
                    
                    setattr(item, "javaDsl_ConditionalAndExpression", self)
                    

    @property
    def javaDsl_ConditionalOrExpression(self):
        return self.__javaDsl_ConditionalOrExpression

    @javaDsl_ConditionalOrExpression.setter
    def javaDsl_ConditionalOrExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConditionalOrExpression__javaDsl_ConditionalOrExpression", None)
        self.__javaDsl_ConditionalOrExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConditionalExpression"):
                opp_val = getattr(old_value, "javaDsl_ConditionalExpression", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ConditionalExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConditionalExpression"):
                opp_val = getattr(value, "javaDsl_ConditionalExpression", None)
                setattr(value, "javaDsl_ConditionalExpression", self)

class javaDsl_MultiplicativeExpression:

    def __init__(self, operators: str, javaDsl_MultiplicativeExpression: "javaDsl_AdditiveExpression" = None, javaDsl_MultiplicativeExpression171: set["javaDsl_NoArrayExpression"] = None):
        self.operators = operators
        self.javaDsl_MultiplicativeExpression = javaDsl_MultiplicativeExpression
        self.javaDsl_MultiplicativeExpression171 = javaDsl_MultiplicativeExpression171 if javaDsl_MultiplicativeExpression171 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_MultiplicativeExpression(self):
        return self.__javaDsl_MultiplicativeExpression

    @javaDsl_MultiplicativeExpression.setter
    def javaDsl_MultiplicativeExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MultiplicativeExpression__javaDsl_MultiplicativeExpression", None)
        self.__javaDsl_MultiplicativeExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_AdditiveExpression169"):
                opp_val = getattr(old_value, "javaDsl_AdditiveExpression169", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_AdditiveExpression169"):
                opp_val = getattr(value, "javaDsl_AdditiveExpression169", None)
                if opp_val is None:
                    setattr(value, "javaDsl_AdditiveExpression169", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaDsl_MultiplicativeExpression171(self):
        return self.__javaDsl_MultiplicativeExpression171

    @javaDsl_MultiplicativeExpression171.setter
    def javaDsl_MultiplicativeExpression171(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MultiplicativeExpression__javaDsl_MultiplicativeExpression171", None)
        self.__javaDsl_MultiplicativeExpression171 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_NoArrayExpression"):
                    opp_val = getattr(item, "javaDsl_NoArrayExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_NoArrayExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_NoArrayExpression"):
                    opp_val = getattr(item, "javaDsl_NoArrayExpression", None)
                    
                    setattr(item, "javaDsl_NoArrayExpression", self)
                    

class javaDsl_AdditiveExpression:

    def __init__(self, operators: str, javaDsl_AdditiveExpression: "javaDsl_ShiftExpression" = None, javaDsl_AdditiveExpression169: set["javaDsl_MultiplicativeExpression"] = None):
        self.operators = operators
        self.javaDsl_AdditiveExpression = javaDsl_AdditiveExpression
        self.javaDsl_AdditiveExpression169 = javaDsl_AdditiveExpression169 if javaDsl_AdditiveExpression169 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_AdditiveExpression(self):
        return self.__javaDsl_AdditiveExpression

    @javaDsl_AdditiveExpression.setter
    def javaDsl_AdditiveExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_AdditiveExpression__javaDsl_AdditiveExpression", None)
        self.__javaDsl_AdditiveExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ShiftExpression167"):
                opp_val = getattr(old_value, "javaDsl_ShiftExpression167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ShiftExpression167"):
                opp_val = getattr(value, "javaDsl_ShiftExpression167", None)
                if opp_val is None:
                    setattr(value, "javaDsl_ShiftExpression167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaDsl_AdditiveExpression169(self):
        return self.__javaDsl_AdditiveExpression169

    @javaDsl_AdditiveExpression169.setter
    def javaDsl_AdditiveExpression169(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_AdditiveExpression__javaDsl_AdditiveExpression169", None)
        self.__javaDsl_AdditiveExpression169 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_MultiplicativeExpression"):
                    opp_val = getattr(item, "javaDsl_MultiplicativeExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_MultiplicativeExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_MultiplicativeExpression"):
                    opp_val = getattr(item, "javaDsl_MultiplicativeExpression", None)
                    
                    setattr(item, "javaDsl_MultiplicativeExpression", self)
                    

class javaDsl_ShiftExpression:

    def __init__(self, operators: str, javaDsl_ShiftExpression: "javaDsl_RelationalExpression" = None, javaDsl_ShiftExpression167: set["javaDsl_AdditiveExpression"] = None):
        self.operators = operators
        self.javaDsl_ShiftExpression = javaDsl_ShiftExpression
        self.javaDsl_ShiftExpression167 = javaDsl_ShiftExpression167 if javaDsl_ShiftExpression167 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_ShiftExpression167(self):
        return self.__javaDsl_ShiftExpression167

    @javaDsl_ShiftExpression167.setter
    def javaDsl_ShiftExpression167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ShiftExpression__javaDsl_ShiftExpression167", None)
        self.__javaDsl_ShiftExpression167 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_AdditiveExpression"):
                    opp_val = getattr(item, "javaDsl_AdditiveExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_AdditiveExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_AdditiveExpression"):
                    opp_val = getattr(item, "javaDsl_AdditiveExpression", None)
                    
                    setattr(item, "javaDsl_AdditiveExpression", self)
                    

    @property
    def javaDsl_ShiftExpression(self):
        return self.__javaDsl_ShiftExpression

    @javaDsl_ShiftExpression.setter
    def javaDsl_ShiftExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ShiftExpression__javaDsl_ShiftExpression", None)
        self.__javaDsl_ShiftExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_RelationalExpression165"):
                opp_val = getattr(old_value, "javaDsl_RelationalExpression165", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_RelationalExpression165"):
                opp_val = getattr(value, "javaDsl_RelationalExpression165", None)
                if opp_val is None:
                    setattr(value, "javaDsl_RelationalExpression165", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_RelationalExpression:

    def __init__(self, operators: str, classes: str, javaDsl_RelationalExpression: "javaDsl_EqualityExpression" = None, javaDsl_RelationalExpression165: set["javaDsl_ShiftExpression"] = None):
        self.operators = operators
        self.classes = classes
        self.javaDsl_RelationalExpression = javaDsl_RelationalExpression
        self.javaDsl_RelationalExpression165 = javaDsl_RelationalExpression165 if javaDsl_RelationalExpression165 is not None else set()
        
    @property
    def classes(self) -> str:
        return self.__classes

    @classes.setter
    def classes(self, classes: str):
        self.__classes = classes

    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_RelationalExpression(self):
        return self.__javaDsl_RelationalExpression

    @javaDsl_RelationalExpression.setter
    def javaDsl_RelationalExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_RelationalExpression__javaDsl_RelationalExpression", None)
        self.__javaDsl_RelationalExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_EqualityExpression163"):
                opp_val = getattr(old_value, "javaDsl_EqualityExpression163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_EqualityExpression163"):
                opp_val = getattr(value, "javaDsl_EqualityExpression163", None)
                if opp_val is None:
                    setattr(value, "javaDsl_EqualityExpression163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaDsl_RelationalExpression165(self):
        return self.__javaDsl_RelationalExpression165

    @javaDsl_RelationalExpression165.setter
    def javaDsl_RelationalExpression165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_RelationalExpression__javaDsl_RelationalExpression165", None)
        self.__javaDsl_RelationalExpression165 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_ShiftExpression"):
                    opp_val = getattr(item, "javaDsl_ShiftExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_ShiftExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_ShiftExpression"):
                    opp_val = getattr(item, "javaDsl_ShiftExpression", None)
                    
                    setattr(item, "javaDsl_ShiftExpression", self)
                    

class javaDsl_EqualityExpression:

    def __init__(self, operators: str, javaDsl_EqualityExpression: "javaDsl_AndExpression" = None, javaDsl_EqualityExpression163: set["javaDsl_RelationalExpression"] = None):
        self.operators = operators
        self.javaDsl_EqualityExpression = javaDsl_EqualityExpression
        self.javaDsl_EqualityExpression163 = javaDsl_EqualityExpression163 if javaDsl_EqualityExpression163 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_EqualityExpression163(self):
        return self.__javaDsl_EqualityExpression163

    @javaDsl_EqualityExpression163.setter
    def javaDsl_EqualityExpression163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_EqualityExpression__javaDsl_EqualityExpression163", None)
        self.__javaDsl_EqualityExpression163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_RelationalExpression"):
                    opp_val = getattr(item, "javaDsl_RelationalExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_RelationalExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_RelationalExpression"):
                    opp_val = getattr(item, "javaDsl_RelationalExpression", None)
                    
                    setattr(item, "javaDsl_RelationalExpression", self)
                    

    @property
    def javaDsl_EqualityExpression(self):
        return self.__javaDsl_EqualityExpression

    @javaDsl_EqualityExpression.setter
    def javaDsl_EqualityExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_EqualityExpression__javaDsl_EqualityExpression", None)
        self.__javaDsl_EqualityExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_AndExpression161"):
                opp_val = getattr(old_value, "javaDsl_AndExpression161", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_AndExpression161"):
                opp_val = getattr(value, "javaDsl_AndExpression161", None)
                if opp_val is None:
                    setattr(value, "javaDsl_AndExpression161", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_AndExpression:

    def __init__(self, operators: str, javaDsl_AndExpression: "javaDsl_ExclusiveOrExpression" = None, javaDsl_AndExpression161: set["javaDsl_EqualityExpression"] = None):
        self.operators = operators
        self.javaDsl_AndExpression = javaDsl_AndExpression
        self.javaDsl_AndExpression161 = javaDsl_AndExpression161 if javaDsl_AndExpression161 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_AndExpression161(self):
        return self.__javaDsl_AndExpression161

    @javaDsl_AndExpression161.setter
    def javaDsl_AndExpression161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_AndExpression__javaDsl_AndExpression161", None)
        self.__javaDsl_AndExpression161 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_EqualityExpression"):
                    opp_val = getattr(item, "javaDsl_EqualityExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_EqualityExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_EqualityExpression"):
                    opp_val = getattr(item, "javaDsl_EqualityExpression", None)
                    
                    setattr(item, "javaDsl_EqualityExpression", self)
                    

    @property
    def javaDsl_AndExpression(self):
        return self.__javaDsl_AndExpression

    @javaDsl_AndExpression.setter
    def javaDsl_AndExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_AndExpression__javaDsl_AndExpression", None)
        self.__javaDsl_AndExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ExclusiveOrExpression159"):
                opp_val = getattr(old_value, "javaDsl_ExclusiveOrExpression159", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ExclusiveOrExpression159"):
                opp_val = getattr(value, "javaDsl_ExclusiveOrExpression159", None)
                if opp_val is None:
                    setattr(value, "javaDsl_ExclusiveOrExpression159", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_ExclusiveOrExpression:

    def __init__(self, operators: str, javaDsl_ExclusiveOrExpression: "javaDsl_InclusiveOrExpression" = None, javaDsl_ExclusiveOrExpression159: set["javaDsl_AndExpression"] = None):
        self.operators = operators
        self.javaDsl_ExclusiveOrExpression = javaDsl_ExclusiveOrExpression
        self.javaDsl_ExclusiveOrExpression159 = javaDsl_ExclusiveOrExpression159 if javaDsl_ExclusiveOrExpression159 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def javaDsl_ExclusiveOrExpression159(self):
        return self.__javaDsl_ExclusiveOrExpression159

    @javaDsl_ExclusiveOrExpression159.setter
    def javaDsl_ExclusiveOrExpression159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ExclusiveOrExpression__javaDsl_ExclusiveOrExpression159", None)
        self.__javaDsl_ExclusiveOrExpression159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_AndExpression"):
                    opp_val = getattr(item, "javaDsl_AndExpression", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_AndExpression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_AndExpression"):
                    opp_val = getattr(item, "javaDsl_AndExpression", None)
                    
                    setattr(item, "javaDsl_AndExpression", self)
                    

    @property
    def javaDsl_ExclusiveOrExpression(self):
        return self.__javaDsl_ExclusiveOrExpression

    @javaDsl_ExclusiveOrExpression.setter
    def javaDsl_ExclusiveOrExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ExclusiveOrExpression__javaDsl_ExclusiveOrExpression", None)
        self.__javaDsl_ExclusiveOrExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_InclusiveOrExpression157"):
                opp_val = getattr(old_value, "javaDsl_InclusiveOrExpression157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_InclusiveOrExpression157"):
                opp_val = getattr(value, "javaDsl_InclusiveOrExpression157", None)
                if opp_val is None:
                    setattr(value, "javaDsl_InclusiveOrExpression157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_ForUpdate:

    pass
class javaDsl_LeftHandSide:

    pass
class AssignmentExpression:

    pass
class javaDsl_ConditionalExpression(AssignmentExpression):

    pass
class StatementExpression:

    pass
class javaDsl_MethodInvocation(StatementExpression):

    def __init__(self, method: str, keyword: str, javaDsl_MethodInvocation: "javaDsl_ArgumentList" = None, javaDsl_MethodInvocation179: "javaDsl_Primary" = None):
        self.method = method
        self.keyword = keyword
        self.javaDsl_MethodInvocation = javaDsl_MethodInvocation
        self.javaDsl_MethodInvocation179 = javaDsl_MethodInvocation179
        
    @property
    def method(self) -> str:
        return self.__method

    @method.setter
    def method(self, method: str):
        self.__method = method

    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def javaDsl_MethodInvocation179(self):
        return self.__javaDsl_MethodInvocation179

    @javaDsl_MethodInvocation179.setter
    def javaDsl_MethodInvocation179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodInvocation__javaDsl_MethodInvocation179", None)
        self.__javaDsl_MethodInvocation179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Primary180"):
                opp_val = getattr(old_value, "javaDsl_Primary180", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Primary180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Primary180"):
                opp_val = getattr(value, "javaDsl_Primary180", None)
                setattr(value, "javaDsl_Primary180", self)

    @property
    def javaDsl_MethodInvocation(self):
        return self.__javaDsl_MethodInvocation

    @javaDsl_MethodInvocation.setter
    def javaDsl_MethodInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodInvocation__javaDsl_MethodInvocation", None)
        self.__javaDsl_MethodInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ArgumentList177"):
                opp_val = getattr(old_value, "javaDsl_ArgumentList177", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ArgumentList177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ArgumentList177"):
                opp_val = getattr(value, "javaDsl_ArgumentList177", None)
                setattr(value, "javaDsl_ArgumentList177", self)

class javaDsl_ClassInstanceCreationExpression(StatementExpression):

    def __init__(self, type: str, javaDsl_ClassInstanceCreationExpression191: "javaDsl_ArgumentList" = None, javaDsl_ClassInstanceCreationExpression: "javaDsl_PrimaryNoNewArray" = None):
        self.type = type
        self.javaDsl_ClassInstanceCreationExpression191 = javaDsl_ClassInstanceCreationExpression191
        self.javaDsl_ClassInstanceCreationExpression = javaDsl_ClassInstanceCreationExpression
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def javaDsl_ClassInstanceCreationExpression191(self):
        return self.__javaDsl_ClassInstanceCreationExpression191

    @javaDsl_ClassInstanceCreationExpression191.setter
    def javaDsl_ClassInstanceCreationExpression191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ClassInstanceCreationExpression__javaDsl_ClassInstanceCreationExpression191", None)
        self.__javaDsl_ClassInstanceCreationExpression191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ArgumentList192"):
                opp_val = getattr(old_value, "javaDsl_ArgumentList192", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ArgumentList192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ArgumentList192"):
                opp_val = getattr(value, "javaDsl_ArgumentList192", None)
                setattr(value, "javaDsl_ArgumentList192", self)

    @property
    def javaDsl_ClassInstanceCreationExpression(self):
        return self.__javaDsl_ClassInstanceCreationExpression

    @javaDsl_ClassInstanceCreationExpression.setter
    def javaDsl_ClassInstanceCreationExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ClassInstanceCreationExpression__javaDsl_ClassInstanceCreationExpression", None)
        self.__javaDsl_ClassInstanceCreationExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_PrimaryNoNewArray"):
                opp_val = getattr(old_value, "javaDsl_PrimaryNoNewArray", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_PrimaryNoNewArray", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_PrimaryNoNewArray"):
                opp_val = getattr(value, "javaDsl_PrimaryNoNewArray", None)
                setattr(value, "javaDsl_PrimaryNoNewArray", self)

class javaDsl_PreIncrementExpression(NoArrayExpression, StatementExpression):

    pass
class javaDsl_PostfixExpression(NoArrayExpressionWithoutMinus, StatementExpression):

    def __init__(self, reference: str, operators: str, javaDsl_PostfixExpression: "javaDsl_Primary" = None):
        self.reference = reference
        self.operators = operators
        self.javaDsl_PostfixExpression = javaDsl_PostfixExpression
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

    @property
    def javaDsl_PostfixExpression(self):
        return self.__javaDsl_PostfixExpression

    @javaDsl_PostfixExpression.setter
    def javaDsl_PostfixExpression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_PostfixExpression__javaDsl_PostfixExpression", None)
        self.__javaDsl_PostfixExpression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Primary"):
                opp_val = getattr(old_value, "javaDsl_Primary", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Primary", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Primary"):
                opp_val = getattr(value, "javaDsl_Primary", None)
                setattr(value, "javaDsl_Primary", self)

class javaDsl_PreDecrementExpression(NoArrayExpression, StatementExpression):

    pass
class javaDsl_Assignment(AssignmentExpression, StatementExpression):

    def __init__(self, operator: str, javaDsl_Assignment: "javaDsl_LeftHandSide" = None, javaDsl_Assignment144: "javaDsl_AssignmentExpression" = None):
        self.operator = operator
        self.javaDsl_Assignment = javaDsl_Assignment
        self.javaDsl_Assignment144 = javaDsl_Assignment144
        
    @property
    def operator(self) -> str:
        return self.__operator

    @operator.setter
    def operator(self, operator: str):
        self.__operator = operator

    @property
    def javaDsl_Assignment144(self):
        return self.__javaDsl_Assignment144

    @javaDsl_Assignment144.setter
    def javaDsl_Assignment144(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Assignment__javaDsl_Assignment144", None)
        self.__javaDsl_Assignment144 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_AssignmentExpression"):
                opp_val = getattr(old_value, "javaDsl_AssignmentExpression", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_AssignmentExpression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_AssignmentExpression"):
                opp_val = getattr(value, "javaDsl_AssignmentExpression", None)
                setattr(value, "javaDsl_AssignmentExpression", self)

    @property
    def javaDsl_Assignment(self):
        return self.__javaDsl_Assignment

    @javaDsl_Assignment.setter
    def javaDsl_Assignment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Assignment__javaDsl_Assignment", None)
        self.__javaDsl_Assignment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_LeftHandSide"):
                opp_val = getattr(old_value, "javaDsl_LeftHandSide", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_LeftHandSide", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_LeftHandSide"):
                opp_val = getattr(value, "javaDsl_LeftHandSide", None)
                setattr(value, "javaDsl_LeftHandSide", self)

class Expression:

    pass
class javaDsl_AssignmentExpression(Expression):

    pass
class PrimaryNoNewArray:

    pass
class ConstantExpression:

    pass
class BlockStatement:

    pass
class javaDsl_Statement(BlockStatement):

    pass
class javaDsl_LocalVariableDeclaration(BlockStatement):

    pass
class Statement:

    pass
class javaDsl_BreakStatement(Statement):

    def __init__(self, reference: str):
        self.reference = reference
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

class javaDsl_ContinueStatement(Statement):

    def __init__(self, reference: str):
        self.reference = reference
        
    @property
    def reference(self) -> str:
        return self.__reference

    @reference.setter
    def reference(self, reference: str):
        self.__reference = reference

class javaDsl_LabeledStatement(Statement):

    def __init__(self, label: str, javaDsl_LabeledStatement: "javaDsl_Statement" = None):
        self.label = label
        self.javaDsl_LabeledStatement = javaDsl_LabeledStatement
        
    @property
    def label(self) -> str:
        return self.__label

    @label.setter
    def label(self, label: str):
        self.__label = label

    @property
    def javaDsl_LabeledStatement(self):
        return self.__javaDsl_LabeledStatement

    @javaDsl_LabeledStatement.setter
    def javaDsl_LabeledStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_LabeledStatement__javaDsl_LabeledStatement", None)
        self.__javaDsl_LabeledStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Statement"):
                opp_val = getattr(old_value, "javaDsl_Statement", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Statement"):
                opp_val = getattr(value, "javaDsl_Statement", None)
                setattr(value, "javaDsl_Statement", self)

class javaDsl_ReturnStatement(Statement):

    pass
class javaDsl_ThrowsStatement(Statement):

    pass
class javaDsl_SynchronizedStatement(Statement):

    pass
class javaDsl_TryStatement(Statement):

    pass
class javaDsl_ForInit:

    pass
class javaDsl_ForStatement(Statement):

    def __init__(self, condition: bool, javaDsl_ForStatement: "javaDsl_ForInit" = None, javaDsl_ForStatement110: "javaDsl_ForUpdate" = None, javaDsl_ForStatement112: "javaDsl_Statement" = None):
        self.condition = condition
        self.javaDsl_ForStatement = javaDsl_ForStatement
        self.javaDsl_ForStatement110 = javaDsl_ForStatement110
        self.javaDsl_ForStatement112 = javaDsl_ForStatement112
        
    @property
    def condition(self) -> bool:
        return self.__condition

    @condition.setter
    def condition(self, condition: bool):
        self.__condition = condition

    @property
    def javaDsl_ForStatement110(self):
        return self.__javaDsl_ForStatement110

    @javaDsl_ForStatement110.setter
    def javaDsl_ForStatement110(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ForStatement__javaDsl_ForStatement110", None)
        self.__javaDsl_ForStatement110 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ForUpdate"):
                opp_val = getattr(old_value, "javaDsl_ForUpdate", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ForUpdate", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ForUpdate"):
                opp_val = getattr(value, "javaDsl_ForUpdate", None)
                setattr(value, "javaDsl_ForUpdate", self)

    @property
    def javaDsl_ForStatement112(self):
        return self.__javaDsl_ForStatement112

    @javaDsl_ForStatement112.setter
    def javaDsl_ForStatement112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ForStatement__javaDsl_ForStatement112", None)
        self.__javaDsl_ForStatement112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Statement113"):
                opp_val = getattr(old_value, "javaDsl_Statement113", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Statement113", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Statement113"):
                opp_val = getattr(value, "javaDsl_Statement113", None)
                setattr(value, "javaDsl_Statement113", self)

    @property
    def javaDsl_ForStatement(self):
        return self.__javaDsl_ForStatement

    @javaDsl_ForStatement.setter
    def javaDsl_ForStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ForStatement__javaDsl_ForStatement", None)
        self.__javaDsl_ForStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ForInit"):
                opp_val = getattr(old_value, "javaDsl_ForInit", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ForInit", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ForInit"):
                opp_val = getattr(value, "javaDsl_ForInit", None)
                setattr(value, "javaDsl_ForInit", self)

class javaDsl_DoStatement(Statement):

    def __init__(self, condition: bool, javaDsl_DoStatement: "javaDsl_Statement" = None):
        self.condition = condition
        self.javaDsl_DoStatement = javaDsl_DoStatement
        
    @property
    def condition(self) -> bool:
        return self.__condition

    @condition.setter
    def condition(self, condition: bool):
        self.__condition = condition

    @property
    def javaDsl_DoStatement(self):
        return self.__javaDsl_DoStatement

    @javaDsl_DoStatement.setter
    def javaDsl_DoStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_DoStatement__javaDsl_DoStatement", None)
        self.__javaDsl_DoStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Statement107"):
                opp_val = getattr(old_value, "javaDsl_Statement107", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Statement107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Statement107"):
                opp_val = getattr(value, "javaDsl_Statement107", None)
                setattr(value, "javaDsl_Statement107", self)

class javaDsl_WhileStatement(Statement):

    def __init__(self, condition: bool, javaDsl_WhileStatement: "javaDsl_Statement" = None):
        self.condition = condition
        self.javaDsl_WhileStatement = javaDsl_WhileStatement
        
    @property
    def condition(self) -> bool:
        return self.__condition

    @condition.setter
    def condition(self, condition: bool):
        self.__condition = condition

    @property
    def javaDsl_WhileStatement(self):
        return self.__javaDsl_WhileStatement

    @javaDsl_WhileStatement.setter
    def javaDsl_WhileStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_WhileStatement__javaDsl_WhileStatement", None)
        self.__javaDsl_WhileStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Statement105"):
                opp_val = getattr(old_value, "javaDsl_Statement105", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Statement105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Statement105"):
                opp_val = getattr(value, "javaDsl_Statement105", None)
                setattr(value, "javaDsl_Statement105", self)

class javaDsl_ConstantExpression:

    pass
class javaDsl_SwitchStatement(Statement):

    pass
class javaDsl_IfStatement(Statement):

    def __init__(self, condition: bool, javaDsl_IfStatement: "javaDsl_Statement" = None, javaDsl_IfStatement95: "javaDsl_Statement" = None):
        self.condition = condition
        self.javaDsl_IfStatement = javaDsl_IfStatement
        self.javaDsl_IfStatement95 = javaDsl_IfStatement95
        
    @property
    def condition(self) -> bool:
        return self.__condition

    @condition.setter
    def condition(self, condition: bool):
        self.__condition = condition

    @property
    def javaDsl_IfStatement95(self):
        return self.__javaDsl_IfStatement95

    @javaDsl_IfStatement95.setter
    def javaDsl_IfStatement95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_IfStatement__javaDsl_IfStatement95", None)
        self.__javaDsl_IfStatement95 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Statement96"):
                opp_val = getattr(old_value, "javaDsl_Statement96", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Statement96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Statement96"):
                opp_val = getattr(value, "javaDsl_Statement96", None)
                setattr(value, "javaDsl_Statement96", self)

    @property
    def javaDsl_IfStatement(self):
        return self.__javaDsl_IfStatement

    @javaDsl_IfStatement.setter
    def javaDsl_IfStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_IfStatement__javaDsl_IfStatement", None)
        self.__javaDsl_IfStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Statement93"):
                opp_val = getattr(old_value, "javaDsl_Statement93", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Statement93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Statement93"):
                opp_val = getattr(value, "javaDsl_Statement93", None)
                setattr(value, "javaDsl_Statement93", self)

class javaDsl_InterfaceBody:

    pass
class javaDsl_StatementExpression(Statement):

    pass
class javaDsl_ExtendsInterfaces:

    def __init__(self, keyword: str, interfaces: str, javaDsl_ExtendsInterfaces: "javaDsl_InterfaceDeclaration" = None):
        self.keyword = keyword
        self.interfaces = interfaces
        self.javaDsl_ExtendsInterfaces = javaDsl_ExtendsInterfaces
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def interfaces(self) -> str:
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, interfaces: str):
        self.__interfaces = interfaces

    @property
    def javaDsl_ExtendsInterfaces(self):
        return self.__javaDsl_ExtendsInterfaces

    @javaDsl_ExtendsInterfaces.setter
    def javaDsl_ExtendsInterfaces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ExtendsInterfaces__javaDsl_ExtendsInterfaces", None)
        self.__javaDsl_ExtendsInterfaces = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_InterfaceDeclaration"):
                opp_val = getattr(old_value, "javaDsl_InterfaceDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_InterfaceDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_InterfaceDeclaration"):
                opp_val = getattr(value, "javaDsl_InterfaceDeclaration", None)
                setattr(value, "javaDsl_InterfaceDeclaration", self)

class javaDsl_InterfaceDeclaration:

    def __init__(self, modifiers: str, name: str, javaDsl_InterfaceDeclaration: "javaDsl_ExtendsInterfaces" = None, javaDsl_InterfaceDeclaration65: "javaDsl_InterfaceBody" = None):
        self.modifiers = modifiers
        self.name = name
        self.javaDsl_InterfaceDeclaration = javaDsl_InterfaceDeclaration
        self.javaDsl_InterfaceDeclaration65 = javaDsl_InterfaceDeclaration65
        
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
    def javaDsl_InterfaceDeclaration65(self):
        return self.__javaDsl_InterfaceDeclaration65

    @javaDsl_InterfaceDeclaration65.setter
    def javaDsl_InterfaceDeclaration65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_InterfaceDeclaration__javaDsl_InterfaceDeclaration65", None)
        self.__javaDsl_InterfaceDeclaration65 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_InterfaceBody"):
                opp_val = getattr(old_value, "javaDsl_InterfaceBody", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_InterfaceBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_InterfaceBody"):
                opp_val = getattr(value, "javaDsl_InterfaceBody", None)
                setattr(value, "javaDsl_InterfaceBody", self)

    @property
    def javaDsl_InterfaceDeclaration(self):
        return self.__javaDsl_InterfaceDeclaration

    @javaDsl_InterfaceDeclaration.setter
    def javaDsl_InterfaceDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_InterfaceDeclaration__javaDsl_InterfaceDeclaration", None)
        self.__javaDsl_InterfaceDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ExtendsInterfaces"):
                opp_val = getattr(old_value, "javaDsl_ExtendsInterfaces", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ExtendsInterfaces", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ExtendsInterfaces"):
                opp_val = getattr(value, "javaDsl_ExtendsInterfaces", None)
                setattr(value, "javaDsl_ExtendsInterfaces", self)

class VariableInitializer:

    pass
class javaDsl_ArrayInitializer(VariableInitializer):

    pass
class InterfaceMemberDeclaration:

    pass
class javaDsl_AbstractMethodDeclaration(InterfaceMemberDeclaration):

    pass
class javaDsl_ConstantDeclaration(InterfaceMemberDeclaration):

    pass
class javaDsl_InterfaceMemberDeclaration:

    def __init__(self, modifiers: str, javaDsl_InterfaceMemberDeclaration: "javaDsl_InterfaceBody" = None):
        self.modifiers = modifiers
        self.javaDsl_InterfaceMemberDeclaration = javaDsl_InterfaceMemberDeclaration
        
    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def javaDsl_InterfaceMemberDeclaration(self):
        return self.__javaDsl_InterfaceMemberDeclaration

    @javaDsl_InterfaceMemberDeclaration.setter
    def javaDsl_InterfaceMemberDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_InterfaceMemberDeclaration__javaDsl_InterfaceMemberDeclaration", None)
        self.__javaDsl_InterfaceMemberDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_InterfaceBody67"):
                opp_val = getattr(old_value, "javaDsl_InterfaceBody67", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_InterfaceBody67"):
                opp_val = getattr(value, "javaDsl_InterfaceBody67", None)
                if opp_val is None:
                    setattr(value, "javaDsl_InterfaceBody67", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_MethodHeader:

    def __init__(self, modifiers: str, javaDsl_MethodHeader51: "javaDsl_ResultType" = None, javaDsl_MethodHeader53: "javaDsl_MethodDeclarator" = None, javaDsl_MethodHeader55: "javaDsl_Exceptions" = None, javaDsl_MethodHeader: "javaDsl_MethodDeclaration" = None):
        self.modifiers = modifiers
        self.javaDsl_MethodHeader51 = javaDsl_MethodHeader51
        self.javaDsl_MethodHeader53 = javaDsl_MethodHeader53
        self.javaDsl_MethodHeader55 = javaDsl_MethodHeader55
        self.javaDsl_MethodHeader = javaDsl_MethodHeader
        
    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def javaDsl_MethodHeader55(self):
        return self.__javaDsl_MethodHeader55

    @javaDsl_MethodHeader55.setter
    def javaDsl_MethodHeader55(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodHeader__javaDsl_MethodHeader55", None)
        self.__javaDsl_MethodHeader55 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Exceptions56"):
                opp_val = getattr(old_value, "javaDsl_Exceptions56", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Exceptions56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Exceptions56"):
                opp_val = getattr(value, "javaDsl_Exceptions56", None)
                setattr(value, "javaDsl_Exceptions56", self)

    @property
    def javaDsl_MethodHeader51(self):
        return self.__javaDsl_MethodHeader51

    @javaDsl_MethodHeader51.setter
    def javaDsl_MethodHeader51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodHeader__javaDsl_MethodHeader51", None)
        self.__javaDsl_MethodHeader51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ResultType"):
                opp_val = getattr(old_value, "javaDsl_ResultType", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ResultType", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ResultType"):
                opp_val = getattr(value, "javaDsl_ResultType", None)
                setattr(value, "javaDsl_ResultType", self)

    @property
    def javaDsl_MethodHeader53(self):
        return self.__javaDsl_MethodHeader53

    @javaDsl_MethodHeader53.setter
    def javaDsl_MethodHeader53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodHeader__javaDsl_MethodHeader53", None)
        self.__javaDsl_MethodHeader53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_MethodDeclarator"):
                opp_val = getattr(old_value, "javaDsl_MethodDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_MethodDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_MethodDeclarator"):
                opp_val = getattr(value, "javaDsl_MethodDeclarator", None)
                setattr(value, "javaDsl_MethodDeclarator", self)

    @property
    def javaDsl_MethodHeader(self):
        return self.__javaDsl_MethodHeader

    @javaDsl_MethodHeader.setter
    def javaDsl_MethodHeader(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodHeader__javaDsl_MethodHeader", None)
        self.__javaDsl_MethodHeader = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_MethodDeclaration46"):
                opp_val = getattr(old_value, "javaDsl_MethodDeclaration46", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_MethodDeclaration46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_MethodDeclaration46"):
                opp_val = getattr(value, "javaDsl_MethodDeclaration46", None)
                setattr(value, "javaDsl_MethodDeclaration46", self)

class javaDsl_Expression(ConstantExpression, PrimaryNoNewArray):

    pass
class javaDsl_VariableInitializer:

    pass
class javaDsl_MethodDeclarator:

    def __init__(self, name: str, javaDsl_MethodDeclarator: "javaDsl_MethodHeader" = None, javaDsl_MethodDeclarator61: set["javaDsl_FormalParameter"] = None, javaDsl_MethodDeclarator77: "javaDsl_AbstractMethodDeclaration" = None):
        self.name = name
        self.javaDsl_MethodDeclarator = javaDsl_MethodDeclarator
        self.javaDsl_MethodDeclarator61 = javaDsl_MethodDeclarator61 if javaDsl_MethodDeclarator61 is not None else set()
        self.javaDsl_MethodDeclarator77 = javaDsl_MethodDeclarator77
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javaDsl_MethodDeclarator(self):
        return self.__javaDsl_MethodDeclarator

    @javaDsl_MethodDeclarator.setter
    def javaDsl_MethodDeclarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodDeclarator__javaDsl_MethodDeclarator", None)
        self.__javaDsl_MethodDeclarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_MethodHeader53"):
                opp_val = getattr(old_value, "javaDsl_MethodHeader53", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_MethodHeader53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_MethodHeader53"):
                opp_val = getattr(value, "javaDsl_MethodHeader53", None)
                setattr(value, "javaDsl_MethodHeader53", self)

    @property
    def javaDsl_MethodDeclarator77(self):
        return self.__javaDsl_MethodDeclarator77

    @javaDsl_MethodDeclarator77.setter
    def javaDsl_MethodDeclarator77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodDeclarator__javaDsl_MethodDeclarator77", None)
        self.__javaDsl_MethodDeclarator77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_AbstractMethodDeclaration76"):
                opp_val = getattr(old_value, "javaDsl_AbstractMethodDeclaration76", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_AbstractMethodDeclaration76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_AbstractMethodDeclaration76"):
                opp_val = getattr(value, "javaDsl_AbstractMethodDeclaration76", None)
                setattr(value, "javaDsl_AbstractMethodDeclaration76", self)

    @property
    def javaDsl_MethodDeclarator61(self):
        return self.__javaDsl_MethodDeclarator61

    @javaDsl_MethodDeclarator61.setter
    def javaDsl_MethodDeclarator61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_MethodDeclarator__javaDsl_MethodDeclarator61", None)
        self.__javaDsl_MethodDeclarator61 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_FormalParameter62"):
                    opp_val = getattr(item, "javaDsl_FormalParameter62", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_FormalParameter62", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_FormalParameter62"):
                    opp_val = getattr(item, "javaDsl_FormalParameter62", None)
                    
                    setattr(item, "javaDsl_FormalParameter62", self)
                    

class javaDsl_ResultType:

    pass
class javaDsl_Type:

    def __init__(self, name: str, javaDsl_Type38: "javaDsl_FieldDeclaration" = None, javaDsl_Type: "javaDsl_FormalParameter" = None, javaDsl_Type59: "javaDsl_ResultType" = None, javaDsl_Type69: "javaDsl_ConstantDeclaration" = None, javaDsl_Type87: "javaDsl_LocalVariableDeclaration" = None):
        self.name = name
        self.javaDsl_Type38 = javaDsl_Type38
        self.javaDsl_Type = javaDsl_Type
        self.javaDsl_Type59 = javaDsl_Type59
        self.javaDsl_Type69 = javaDsl_Type69
        self.javaDsl_Type87 = javaDsl_Type87
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javaDsl_Type38(self):
        return self.__javaDsl_Type38

    @javaDsl_Type38.setter
    def javaDsl_Type38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Type__javaDsl_Type38", None)
        self.__javaDsl_Type38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_FieldDeclaration37"):
                opp_val = getattr(old_value, "javaDsl_FieldDeclaration37", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_FieldDeclaration37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_FieldDeclaration37"):
                opp_val = getattr(value, "javaDsl_FieldDeclaration37", None)
                setattr(value, "javaDsl_FieldDeclaration37", self)

    @property
    def javaDsl_Type59(self):
        return self.__javaDsl_Type59

    @javaDsl_Type59.setter
    def javaDsl_Type59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Type__javaDsl_Type59", None)
        self.__javaDsl_Type59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ResultType58"):
                opp_val = getattr(old_value, "javaDsl_ResultType58", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ResultType58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ResultType58"):
                opp_val = getattr(value, "javaDsl_ResultType58", None)
                setattr(value, "javaDsl_ResultType58", self)

    @property
    def javaDsl_Type(self):
        return self.__javaDsl_Type

    @javaDsl_Type.setter
    def javaDsl_Type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Type__javaDsl_Type", None)
        self.__javaDsl_Type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_FormalParameter29"):
                opp_val = getattr(old_value, "javaDsl_FormalParameter29", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_FormalParameter29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_FormalParameter29"):
                opp_val = getattr(value, "javaDsl_FormalParameter29", None)
                setattr(value, "javaDsl_FormalParameter29", self)

    @property
    def javaDsl_Type87(self):
        return self.__javaDsl_Type87

    @javaDsl_Type87.setter
    def javaDsl_Type87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Type__javaDsl_Type87", None)
        self.__javaDsl_Type87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_LocalVariableDeclaration"):
                opp_val = getattr(old_value, "javaDsl_LocalVariableDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_LocalVariableDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_LocalVariableDeclaration"):
                opp_val = getattr(value, "javaDsl_LocalVariableDeclaration", None)
                setattr(value, "javaDsl_LocalVariableDeclaration", self)

    @property
    def javaDsl_Type69(self):
        return self.__javaDsl_Type69

    @javaDsl_Type69.setter
    def javaDsl_Type69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Type__javaDsl_Type69", None)
        self.__javaDsl_Type69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConstantDeclaration"):
                opp_val = getattr(old_value, "javaDsl_ConstantDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ConstantDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConstantDeclaration"):
                opp_val = getattr(value, "javaDsl_ConstantDeclaration", None)
                setattr(value, "javaDsl_ConstantDeclaration", self)

class javaDsl_FormalParameter:

    def __init__(self, variable: str, javaDsl_FormalParameter: "javaDsl_ConstructorDeclarator" = None, javaDsl_FormalParameter29: "javaDsl_Type" = None, javaDsl_FormalParameter62: "javaDsl_MethodDeclarator" = None, javaDsl_FormalParameter135: "javaDsl_TryStatement" = None):
        self.variable = variable
        self.javaDsl_FormalParameter = javaDsl_FormalParameter
        self.javaDsl_FormalParameter29 = javaDsl_FormalParameter29
        self.javaDsl_FormalParameter62 = javaDsl_FormalParameter62
        self.javaDsl_FormalParameter135 = javaDsl_FormalParameter135
        
    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def javaDsl_FormalParameter29(self):
        return self.__javaDsl_FormalParameter29

    @javaDsl_FormalParameter29.setter
    def javaDsl_FormalParameter29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_FormalParameter__javaDsl_FormalParameter29", None)
        self.__javaDsl_FormalParameter29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Type"):
                opp_val = getattr(old_value, "javaDsl_Type", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Type"):
                opp_val = getattr(value, "javaDsl_Type", None)
                setattr(value, "javaDsl_Type", self)

    @property
    def javaDsl_FormalParameter(self):
        return self.__javaDsl_FormalParameter

    @javaDsl_FormalParameter.setter
    def javaDsl_FormalParameter(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_FormalParameter__javaDsl_FormalParameter", None)
        self.__javaDsl_FormalParameter = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConstructorDeclarator27"):
                opp_val = getattr(old_value, "javaDsl_ConstructorDeclarator27", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConstructorDeclarator27"):
                opp_val = getattr(value, "javaDsl_ConstructorDeclarator27", None)
                if opp_val is None:
                    setattr(value, "javaDsl_ConstructorDeclarator27", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaDsl_FormalParameter135(self):
        return self.__javaDsl_FormalParameter135

    @javaDsl_FormalParameter135.setter
    def javaDsl_FormalParameter135(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_FormalParameter__javaDsl_FormalParameter135", None)
        self.__javaDsl_FormalParameter135 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_TryStatement134"):
                opp_val = getattr(old_value, "javaDsl_TryStatement134", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_TryStatement134"):
                opp_val = getattr(value, "javaDsl_TryStatement134", None)
                if opp_val is None:
                    setattr(value, "javaDsl_TryStatement134", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaDsl_FormalParameter62(self):
        return self.__javaDsl_FormalParameter62

    @javaDsl_FormalParameter62.setter
    def javaDsl_FormalParameter62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_FormalParameter__javaDsl_FormalParameter62", None)
        self.__javaDsl_FormalParameter62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_MethodDeclarator61"):
                opp_val = getattr(old_value, "javaDsl_MethodDeclarator61", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_MethodDeclarator61"):
                opp_val = getattr(value, "javaDsl_MethodDeclarator61", None)
                if opp_val is None:
                    setattr(value, "javaDsl_MethodDeclarator61", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_VariableDeclarator:

    def __init__(self, name: str, javaDsl_VariableDeclarator: "javaDsl_FieldDeclaration" = None, javaDsl_VariableDeclarator42: "javaDsl_VariableInitializer" = None, javaDsl_VariableDeclarator72: "javaDsl_ConstantDeclaration" = None, javaDsl_VariableDeclarator90: "javaDsl_LocalVariableDeclaration" = None):
        self.name = name
        self.javaDsl_VariableDeclarator = javaDsl_VariableDeclarator
        self.javaDsl_VariableDeclarator42 = javaDsl_VariableDeclarator42
        self.javaDsl_VariableDeclarator72 = javaDsl_VariableDeclarator72
        self.javaDsl_VariableDeclarator90 = javaDsl_VariableDeclarator90
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javaDsl_VariableDeclarator90(self):
        return self.__javaDsl_VariableDeclarator90

    @javaDsl_VariableDeclarator90.setter
    def javaDsl_VariableDeclarator90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_VariableDeclarator__javaDsl_VariableDeclarator90", None)
        self.__javaDsl_VariableDeclarator90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_LocalVariableDeclaration89"):
                opp_val = getattr(old_value, "javaDsl_LocalVariableDeclaration89", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_LocalVariableDeclaration89"):
                opp_val = getattr(value, "javaDsl_LocalVariableDeclaration89", None)
                if opp_val is None:
                    setattr(value, "javaDsl_LocalVariableDeclaration89", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def javaDsl_VariableDeclarator42(self):
        return self.__javaDsl_VariableDeclarator42

    @javaDsl_VariableDeclarator42.setter
    def javaDsl_VariableDeclarator42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_VariableDeclarator__javaDsl_VariableDeclarator42", None)
        self.__javaDsl_VariableDeclarator42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_VariableInitializer"):
                opp_val = getattr(old_value, "javaDsl_VariableInitializer", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_VariableInitializer", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_VariableInitializer"):
                opp_val = getattr(value, "javaDsl_VariableInitializer", None)
                setattr(value, "javaDsl_VariableInitializer", self)

    @property
    def javaDsl_VariableDeclarator72(self):
        return self.__javaDsl_VariableDeclarator72

    @javaDsl_VariableDeclarator72.setter
    def javaDsl_VariableDeclarator72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_VariableDeclarator__javaDsl_VariableDeclarator72", None)
        self.__javaDsl_VariableDeclarator72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConstantDeclaration71"):
                opp_val = getattr(old_value, "javaDsl_ConstantDeclaration71", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ConstantDeclaration71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConstantDeclaration71"):
                opp_val = getattr(value, "javaDsl_ConstantDeclaration71", None)
                setattr(value, "javaDsl_ConstantDeclaration71", self)

    @property
    def javaDsl_VariableDeclarator(self):
        return self.__javaDsl_VariableDeclarator

    @javaDsl_VariableDeclarator.setter
    def javaDsl_VariableDeclarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_VariableDeclarator__javaDsl_VariableDeclarator", None)
        self.__javaDsl_VariableDeclarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_FieldDeclaration40"):
                opp_val = getattr(old_value, "javaDsl_FieldDeclaration40", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_FieldDeclaration40"):
                opp_val = getattr(value, "javaDsl_FieldDeclaration40", None)
                if opp_val is None:
                    setattr(value, "javaDsl_FieldDeclaration40", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_ArgumentList:

    pass
class javaDsl_BlockStatement:

    pass
class javaDsl_ExplicitConstructorInvocation:

    def __init__(self, keyword: str, javaDsl_ExplicitConstructorInvocation: "javaDsl_ConstructorBody" = None, javaDsl_ExplicitConstructorInvocation35: "javaDsl_ArgumentList" = None):
        self.keyword = keyword
        self.javaDsl_ExplicitConstructorInvocation = javaDsl_ExplicitConstructorInvocation
        self.javaDsl_ExplicitConstructorInvocation35 = javaDsl_ExplicitConstructorInvocation35
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def javaDsl_ExplicitConstructorInvocation35(self):
        return self.__javaDsl_ExplicitConstructorInvocation35

    @javaDsl_ExplicitConstructorInvocation35.setter
    def javaDsl_ExplicitConstructorInvocation35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ExplicitConstructorInvocation__javaDsl_ExplicitConstructorInvocation35", None)
        self.__javaDsl_ExplicitConstructorInvocation35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ArgumentList"):
                opp_val = getattr(old_value, "javaDsl_ArgumentList", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ArgumentList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ArgumentList"):
                opp_val = getattr(value, "javaDsl_ArgumentList", None)
                setattr(value, "javaDsl_ArgumentList", self)

    @property
    def javaDsl_ExplicitConstructorInvocation(self):
        return self.__javaDsl_ExplicitConstructorInvocation

    @javaDsl_ExplicitConstructorInvocation.setter
    def javaDsl_ExplicitConstructorInvocation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ExplicitConstructorInvocation__javaDsl_ExplicitConstructorInvocation", None)
        self.__javaDsl_ExplicitConstructorInvocation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConstructorBody31"):
                opp_val = getattr(old_value, "javaDsl_ConstructorBody31", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ConstructorBody31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConstructorBody31"):
                opp_val = getattr(value, "javaDsl_ConstructorBody31", None)
                setattr(value, "javaDsl_ConstructorBody31", self)

class javaDsl_FieldDeclaration:

    def __init__(self, modifiers: str, javaDsl_FieldDeclaration: "javaDsl_ClassMemberDeclaration" = None, javaDsl_FieldDeclaration37: "javaDsl_Type" = None, javaDsl_FieldDeclaration40: set["javaDsl_VariableDeclarator"] = None):
        self.modifiers = modifiers
        self.javaDsl_FieldDeclaration = javaDsl_FieldDeclaration
        self.javaDsl_FieldDeclaration37 = javaDsl_FieldDeclaration37
        self.javaDsl_FieldDeclaration40 = javaDsl_FieldDeclaration40 if javaDsl_FieldDeclaration40 is not None else set()
        
    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def javaDsl_FieldDeclaration37(self):
        return self.__javaDsl_FieldDeclaration37

    @javaDsl_FieldDeclaration37.setter
    def javaDsl_FieldDeclaration37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_FieldDeclaration__javaDsl_FieldDeclaration37", None)
        self.__javaDsl_FieldDeclaration37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Type38"):
                opp_val = getattr(old_value, "javaDsl_Type38", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Type38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Type38"):
                opp_val = getattr(value, "javaDsl_Type38", None)
                setattr(value, "javaDsl_Type38", self)

    @property
    def javaDsl_FieldDeclaration(self):
        return self.__javaDsl_FieldDeclaration

    @javaDsl_FieldDeclaration.setter
    def javaDsl_FieldDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_FieldDeclaration__javaDsl_FieldDeclaration", None)
        self.__javaDsl_FieldDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ClassMemberDeclaration17"):
                opp_val = getattr(old_value, "javaDsl_ClassMemberDeclaration17", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ClassMemberDeclaration17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ClassMemberDeclaration17"):
                opp_val = getattr(value, "javaDsl_ClassMemberDeclaration17", None)
                setattr(value, "javaDsl_ClassMemberDeclaration17", self)

    @property
    def javaDsl_FieldDeclaration40(self):
        return self.__javaDsl_FieldDeclaration40

    @javaDsl_FieldDeclaration40.setter
    def javaDsl_FieldDeclaration40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_FieldDeclaration__javaDsl_FieldDeclaration40", None)
        self.__javaDsl_FieldDeclaration40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_VariableDeclarator"):
                    opp_val = getattr(item, "javaDsl_VariableDeclarator", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_VariableDeclarator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_VariableDeclarator"):
                    opp_val = getattr(item, "javaDsl_VariableDeclarator", None)
                    
                    setattr(item, "javaDsl_VariableDeclarator", self)
                    

class javaDsl_ClassMemberDeclaration:

    pass
class javaDsl_ConstructorBody:

    pass
class javaDsl_Exceptions:

    def __init__(self, exceptions: str, javaDsl_Exceptions: "javaDsl_ConstructorDeclaration" = None, javaDsl_Exceptions56: "javaDsl_MethodHeader" = None, javaDsl_Exceptions80: "javaDsl_AbstractMethodDeclaration" = None):
        self.exceptions = exceptions
        self.javaDsl_Exceptions = javaDsl_Exceptions
        self.javaDsl_Exceptions56 = javaDsl_Exceptions56
        self.javaDsl_Exceptions80 = javaDsl_Exceptions80
        
    @property
    def exceptions(self) -> str:
        return self.__exceptions

    @exceptions.setter
    def exceptions(self, exceptions: str):
        self.__exceptions = exceptions

    @property
    def javaDsl_Exceptions(self):
        return self.__javaDsl_Exceptions

    @javaDsl_Exceptions.setter
    def javaDsl_Exceptions(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Exceptions__javaDsl_Exceptions", None)
        self.__javaDsl_Exceptions = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConstructorDeclaration23"):
                opp_val = getattr(old_value, "javaDsl_ConstructorDeclaration23", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ConstructorDeclaration23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConstructorDeclaration23"):
                opp_val = getattr(value, "javaDsl_ConstructorDeclaration23", None)
                setattr(value, "javaDsl_ConstructorDeclaration23", self)

    @property
    def javaDsl_Exceptions80(self):
        return self.__javaDsl_Exceptions80

    @javaDsl_Exceptions80.setter
    def javaDsl_Exceptions80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Exceptions__javaDsl_Exceptions80", None)
        self.__javaDsl_Exceptions80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_AbstractMethodDeclaration79"):
                opp_val = getattr(old_value, "javaDsl_AbstractMethodDeclaration79", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_AbstractMethodDeclaration79", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_AbstractMethodDeclaration79"):
                opp_val = getattr(value, "javaDsl_AbstractMethodDeclaration79", None)
                setattr(value, "javaDsl_AbstractMethodDeclaration79", self)

    @property
    def javaDsl_Exceptions56(self):
        return self.__javaDsl_Exceptions56

    @javaDsl_Exceptions56.setter
    def javaDsl_Exceptions56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Exceptions__javaDsl_Exceptions56", None)
        self.__javaDsl_Exceptions56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_MethodHeader55"):
                opp_val = getattr(old_value, "javaDsl_MethodHeader55", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_MethodHeader55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_MethodHeader55"):
                opp_val = getattr(value, "javaDsl_MethodHeader55", None)
                setattr(value, "javaDsl_MethodHeader55", self)

class javaDsl_ConstructorDeclarator:

    def __init__(self, name: str, javaDsl_ConstructorDeclarator: "javaDsl_ConstructorDeclaration" = None, javaDsl_ConstructorDeclarator27: set["javaDsl_FormalParameter"] = None):
        self.name = name
        self.javaDsl_ConstructorDeclarator = javaDsl_ConstructorDeclarator
        self.javaDsl_ConstructorDeclarator27 = javaDsl_ConstructorDeclarator27 if javaDsl_ConstructorDeclarator27 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javaDsl_ConstructorDeclarator(self):
        return self.__javaDsl_ConstructorDeclarator

    @javaDsl_ConstructorDeclarator.setter
    def javaDsl_ConstructorDeclarator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConstructorDeclarator__javaDsl_ConstructorDeclarator", None)
        self.__javaDsl_ConstructorDeclarator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConstructorDeclaration"):
                opp_val = getattr(old_value, "javaDsl_ConstructorDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ConstructorDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConstructorDeclaration"):
                opp_val = getattr(value, "javaDsl_ConstructorDeclaration", None)
                setattr(value, "javaDsl_ConstructorDeclaration", self)

    @property
    def javaDsl_ConstructorDeclarator27(self):
        return self.__javaDsl_ConstructorDeclarator27

    @javaDsl_ConstructorDeclarator27.setter
    def javaDsl_ConstructorDeclarator27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConstructorDeclarator__javaDsl_ConstructorDeclarator27", None)
        self.__javaDsl_ConstructorDeclarator27 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "javaDsl_FormalParameter"):
                    opp_val = getattr(item, "javaDsl_FormalParameter", None)
                    
                    if opp_val == self:
                        setattr(item, "javaDsl_FormalParameter", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "javaDsl_FormalParameter"):
                    opp_val = getattr(item, "javaDsl_FormalParameter", None)
                    
                    setattr(item, "javaDsl_FormalParameter", self)
                    

class javaDsl_Block(Statement):

    pass
class ClassBodyDeclaration:

    pass
class javaDsl_ConstructorDeclaration(ClassBodyDeclaration):

    def __init__(self, modifiers: str, javaDsl_ConstructorDeclaration: "javaDsl_ConstructorDeclarator" = None, javaDsl_ConstructorDeclaration23: "javaDsl_Exceptions" = None, javaDsl_ConstructorDeclaration25: "javaDsl_ConstructorBody" = None):
        self.modifiers = modifiers
        self.javaDsl_ConstructorDeclaration = javaDsl_ConstructorDeclaration
        self.javaDsl_ConstructorDeclaration23 = javaDsl_ConstructorDeclaration23
        self.javaDsl_ConstructorDeclaration25 = javaDsl_ConstructorDeclaration25
        
    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

    @property
    def javaDsl_ConstructorDeclaration25(self):
        return self.__javaDsl_ConstructorDeclaration25

    @javaDsl_ConstructorDeclaration25.setter
    def javaDsl_ConstructorDeclaration25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConstructorDeclaration__javaDsl_ConstructorDeclaration25", None)
        self.__javaDsl_ConstructorDeclaration25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConstructorBody"):
                opp_val = getattr(old_value, "javaDsl_ConstructorBody", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ConstructorBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConstructorBody"):
                opp_val = getattr(value, "javaDsl_ConstructorBody", None)
                setattr(value, "javaDsl_ConstructorBody", self)

    @property
    def javaDsl_ConstructorDeclaration(self):
        return self.__javaDsl_ConstructorDeclaration

    @javaDsl_ConstructorDeclaration.setter
    def javaDsl_ConstructorDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConstructorDeclaration__javaDsl_ConstructorDeclaration", None)
        self.__javaDsl_ConstructorDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ConstructorDeclarator"):
                opp_val = getattr(old_value, "javaDsl_ConstructorDeclarator", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ConstructorDeclarator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ConstructorDeclarator"):
                opp_val = getattr(value, "javaDsl_ConstructorDeclarator", None)
                setattr(value, "javaDsl_ConstructorDeclarator", self)

    @property
    def javaDsl_ConstructorDeclaration23(self):
        return self.__javaDsl_ConstructorDeclaration23

    @javaDsl_ConstructorDeclaration23.setter
    def javaDsl_ConstructorDeclaration23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ConstructorDeclaration__javaDsl_ConstructorDeclaration23", None)
        self.__javaDsl_ConstructorDeclaration23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Exceptions"):
                opp_val = getattr(old_value, "javaDsl_Exceptions", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Exceptions", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Exceptions"):
                opp_val = getattr(value, "javaDsl_Exceptions", None)
                setattr(value, "javaDsl_Exceptions", self)

class javaDsl_StaticInitializer(ClassBodyDeclaration):

    pass
class javaDsl_MethodDeclaration:

    pass
class javaDsl_Interfaces:

    def __init__(self, keyword: str, interfaces: str, javaDsl_Interfaces: "javaDsl_ClassDeclaration" = None):
        self.keyword = keyword
        self.interfaces = interfaces
        self.javaDsl_Interfaces = javaDsl_Interfaces
        
    @property
    def keyword(self) -> str:
        return self.__keyword

    @keyword.setter
    def keyword(self, keyword: str):
        self.__keyword = keyword

    @property
    def interfaces(self) -> str:
        return self.__interfaces

    @interfaces.setter
    def interfaces(self, interfaces: str):
        self.__interfaces = interfaces

    @property
    def javaDsl_Interfaces(self):
        return self.__javaDsl_Interfaces

    @javaDsl_Interfaces.setter
    def javaDsl_Interfaces(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_Interfaces__javaDsl_Interfaces", None)
        self.__javaDsl_Interfaces = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ClassDeclaration"):
                opp_val = getattr(old_value, "javaDsl_ClassDeclaration", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ClassDeclaration", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ClassDeclaration"):
                opp_val = getattr(value, "javaDsl_ClassDeclaration", None)
                setattr(value, "javaDsl_ClassDeclaration", self)

class javaDsl_ClassBodyDeclaration:

    pass
class javaDsl_ClassBody:

    pass
class javaDsl_TypeDeclaration:

    def __init__(self, doc: str, javaDsl_TypeDeclaration8: "javaDsl_EObject" = None, javaDsl_TypeDeclaration: "javaDsl_CompilationUnit" = None):
        self.doc = doc
        self.javaDsl_TypeDeclaration8 = javaDsl_TypeDeclaration8
        self.javaDsl_TypeDeclaration = javaDsl_TypeDeclaration
        
    @property
    def doc(self) -> str:
        return self.__doc

    @doc.setter
    def doc(self, doc: str):
        self.__doc = doc

    @property
    def javaDsl_TypeDeclaration8(self):
        return self.__javaDsl_TypeDeclaration8

    @javaDsl_TypeDeclaration8.setter
    def javaDsl_TypeDeclaration8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_TypeDeclaration__javaDsl_TypeDeclaration8", None)
        self.__javaDsl_TypeDeclaration8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_EObject"):
                opp_val = getattr(old_value, "javaDsl_EObject", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_EObject", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_EObject"):
                opp_val = getattr(value, "javaDsl_EObject", None)
                setattr(value, "javaDsl_EObject", self)

    @property
    def javaDsl_TypeDeclaration(self):
        return self.__javaDsl_TypeDeclaration

    @javaDsl_TypeDeclaration.setter
    def javaDsl_TypeDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_TypeDeclaration__javaDsl_TypeDeclaration", None)
        self.__javaDsl_TypeDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_CompilationUnit6"):
                opp_val = getattr(old_value, "javaDsl_CompilationUnit6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_CompilationUnit6"):
                opp_val = getattr(value, "javaDsl_CompilationUnit6", None)
                if opp_val is None:
                    setattr(value, "javaDsl_CompilationUnit6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_ImportStatement:

    def __init__(self, package: str, object: str, javaDsl_ImportStatement: "javaDsl_CompilationUnit" = None):
        self.package = package
        self.object = object
        self.javaDsl_ImportStatement = javaDsl_ImportStatement
        
    @property
    def package(self) -> str:
        return self.__package

    @package.setter
    def package(self, package: str):
        self.__package = package

    @property
    def object(self) -> str:
        return self.__object

    @object.setter
    def object(self, object: str):
        self.__object = object

    @property
    def javaDsl_ImportStatement(self):
        return self.__javaDsl_ImportStatement

    @javaDsl_ImportStatement.setter
    def javaDsl_ImportStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ImportStatement__javaDsl_ImportStatement", None)
        self.__javaDsl_ImportStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_CompilationUnit4"):
                opp_val = getattr(old_value, "javaDsl_CompilationUnit4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_CompilationUnit4"):
                opp_val = getattr(value, "javaDsl_CompilationUnit4", None)
                if opp_val is None:
                    setattr(value, "javaDsl_CompilationUnit4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class javaDsl_ClassDeclaration:

    def __init__(self, modifiers: str, className: str, extend: str, javaDsl_ClassDeclaration11: "javaDsl_ClassBody" = None, javaDsl_ClassDeclaration: "javaDsl_Interfaces" = None):
        self.modifiers = modifiers
        self.className = className
        self.extend = extend
        self.javaDsl_ClassDeclaration11 = javaDsl_ClassDeclaration11
        self.javaDsl_ClassDeclaration = javaDsl_ClassDeclaration
        
    @property
    def modifiers(self) -> str:
        return self.__modifiers

    @modifiers.setter
    def modifiers(self, modifiers: str):
        self.__modifiers = modifiers

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
    def javaDsl_ClassDeclaration(self):
        return self.__javaDsl_ClassDeclaration

    @javaDsl_ClassDeclaration.setter
    def javaDsl_ClassDeclaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ClassDeclaration__javaDsl_ClassDeclaration", None)
        self.__javaDsl_ClassDeclaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_Interfaces"):
                opp_val = getattr(old_value, "javaDsl_Interfaces", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_Interfaces", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_Interfaces"):
                opp_val = getattr(value, "javaDsl_Interfaces", None)
                setattr(value, "javaDsl_Interfaces", self)

    @property
    def javaDsl_ClassDeclaration11(self):
        return self.__javaDsl_ClassDeclaration11

    @javaDsl_ClassDeclaration11.setter
    def javaDsl_ClassDeclaration11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_ClassDeclaration__javaDsl_ClassDeclaration11", None)
        self.__javaDsl_ClassDeclaration11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_ClassBody"):
                opp_val = getattr(old_value, "javaDsl_ClassBody", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_ClassBody", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_ClassBody"):
                opp_val = getattr(value, "javaDsl_ClassBody", None)
                setattr(value, "javaDsl_ClassBody", self)

class javaDsl_EObject:

    pass
class javaDsl_PackageStatement:

    def __init__(self, name: str, javaDsl_PackageStatement: "javaDsl_CompilationUnit" = None):
        self.name = name
        self.javaDsl_PackageStatement = javaDsl_PackageStatement
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def javaDsl_PackageStatement(self):
        return self.__javaDsl_PackageStatement

    @javaDsl_PackageStatement.setter
    def javaDsl_PackageStatement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_javaDsl_PackageStatement__javaDsl_PackageStatement", None)
        self.__javaDsl_PackageStatement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "javaDsl_CompilationUnit2"):
                opp_val = getattr(old_value, "javaDsl_CompilationUnit2", None)
                if opp_val == self:
                    setattr(old_value, "javaDsl_CompilationUnit2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "javaDsl_CompilationUnit2"):
                opp_val = getattr(value, "javaDsl_CompilationUnit2", None)
                setattr(value, "javaDsl_CompilationUnit2", self)

class javaDsl_CompilationUnit:

    pass
class javaDsl_Head:

    pass