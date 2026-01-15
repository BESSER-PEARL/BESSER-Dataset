from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class constant_definition:

    pass
class goto_statement:

    pass
class statement:

    pass
class pascal_variant:

    pass
class pascal_tag_field:

    def __init__(self, id: str, pascal_tag_field: "pascal_variant_part" = None):
        self.id = id
        self.pascal_tag_field = pascal_tag_field
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pascal_tag_field(self):
        return self.__pascal_tag_field

    @pascal_tag_field.setter
    def pascal_tag_field(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_tag_field__pascal_tag_field", None)
        self.__pascal_tag_field = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variant_part225"):
                opp_val = getattr(old_value, "pascal_variant_part225", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variant_part225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variant_part225"):
                opp_val = getattr(value, "pascal_variant_part225", None)
                setattr(value, "pascal_variant_part225", self)

class pascal_record_section:

    pass
class pascal_variant_part:

    def __init__(self, id: str, pascal_variant_part: "pascal_field_list" = None, pascal_variant_part225: "pascal_tag_field" = None, pascal_variant_part227: set["pascal_variant"] = None):
        self.id = id
        self.pascal_variant_part = pascal_variant_part
        self.pascal_variant_part225 = pascal_variant_part225
        self.pascal_variant_part227 = pascal_variant_part227 if pascal_variant_part227 is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pascal_variant_part(self):
        return self.__pascal_variant_part

    @pascal_variant_part.setter
    def pascal_variant_part(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part", None)
        self.__pascal_variant_part = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_field_list215"):
                opp_val = getattr(old_value, "pascal_field_list215", None)
                if opp_val == self:
                    setattr(old_value, "pascal_field_list215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_field_list215"):
                opp_val = getattr(value, "pascal_field_list215", None)
                setattr(value, "pascal_field_list215", self)

    @property
    def pascal_variant_part227(self):
        return self.__pascal_variant_part227

    @pascal_variant_part227.setter
    def pascal_variant_part227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part227", None)
        self.__pascal_variant_part227 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_variant"):
                    opp_val = getattr(item, "pascal_variant", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_variant", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_variant"):
                    opp_val = getattr(item, "pascal_variant", None)
                    
                    setattr(item, "pascal_variant", self)
                    

    @property
    def pascal_variant_part225(self):
        return self.__pascal_variant_part225

    @pascal_variant_part225.setter
    def pascal_variant_part225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part225", None)
        self.__pascal_variant_part225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_tag_field"):
                opp_val = getattr(old_value, "pascal_tag_field", None)
                if opp_val == self:
                    setattr(old_value, "pascal_tag_field", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_tag_field"):
                opp_val = getattr(value, "pascal_tag_field", None)
                setattr(value, "pascal_tag_field", self)

class pascal_fixed_part:

    pass
class program_heading:

    pass
class pascal_file_type:

    pass
class pascal_field_list:

    pass
class pascal_enumerated_type:

    pass
class pascal_subrange_type:

    pass
class pascal_set_type:

    pass
class pascal_pointer_type:

    def __init__(self, name: str, pascal_pointer_type: "pascal_type" = None):
        self.name = name
        self.pascal_pointer_type = pascal_pointer_type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_pointer_type(self):
        return self.__pascal_pointer_type

    @pascal_pointer_type.setter
    def pascal_pointer_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_pointer_type__pascal_pointer_type", None)
        self.__pascal_pointer_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_type174"):
                opp_val = getattr(old_value, "pascal_type174", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type174"):
                opp_val = getattr(value, "pascal_type174", None)
                setattr(value, "pascal_type174", self)

class pascal_record_type:

    pass
class pascal_array_type:

    pass
class pascal_unpacked_structured_type:

    pass
class pascal_ElementList:

    pass
class pascal_ExpressionList:

    pass
class pascal_structured_type:

    pass
class pascal_simple_type:

    def __init__(self, primitiveType: str, pascal_simple_type: "pascal_type" = None, pascal_simple_type176: "pascal_subrange_type" = None, pascal_simple_type178: "pascal_enumerated_type" = None, pascal_simple_type200: "pascal_array_type" = None):
        self.primitiveType = primitiveType
        self.pascal_simple_type = pascal_simple_type
        self.pascal_simple_type176 = pascal_simple_type176
        self.pascal_simple_type178 = pascal_simple_type178
        self.pascal_simple_type200 = pascal_simple_type200
        
    @property
    def primitiveType(self) -> str:
        return self.__primitiveType

    @primitiveType.setter
    def primitiveType(self, primitiveType: str):
        self.__primitiveType = primitiveType

    @property
    def pascal_simple_type(self):
        return self.__pascal_simple_type

    @pascal_simple_type.setter
    def pascal_simple_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type", None)
        self.__pascal_simple_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_type170"):
                opp_val = getattr(old_value, "pascal_type170", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type170", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type170"):
                opp_val = getattr(value, "pascal_type170", None)
                setattr(value, "pascal_type170", self)

    @property
    def pascal_simple_type178(self):
        return self.__pascal_simple_type178

    @pascal_simple_type178.setter
    def pascal_simple_type178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type178", None)
        self.__pascal_simple_type178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_enumerated_type"):
                opp_val = getattr(old_value, "pascal_enumerated_type", None)
                if opp_val == self:
                    setattr(old_value, "pascal_enumerated_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_enumerated_type"):
                opp_val = getattr(value, "pascal_enumerated_type", None)
                setattr(value, "pascal_enumerated_type", self)

    @property
    def pascal_simple_type176(self):
        return self.__pascal_simple_type176

    @pascal_simple_type176.setter
    def pascal_simple_type176(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type176", None)
        self.__pascal_simple_type176 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type"):
                opp_val = getattr(old_value, "pascal_subrange_type", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type"):
                opp_val = getattr(value, "pascal_subrange_type", None)
                setattr(value, "pascal_subrange_type", self)

    @property
    def pascal_simple_type200(self):
        return self.__pascal_simple_type200

    @pascal_simple_type200.setter
    def pascal_simple_type200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type200", None)
        self.__pascal_simple_type200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_array_type199"):
                opp_val = getattr(old_value, "pascal_array_type199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_array_type199"):
                opp_val = getattr(value, "pascal_array_type199", None)
                if opp_val is None:
                    setattr(value, "pascal_array_type199", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class type_definition:

    pass
class pascal_number:

    def __init__(self, integer: str, real: str, pascal_number: "pascal_factor" = None, pascal_number239: "pascal_constant" = None):
        self.integer = integer
        self.real = real
        self.pascal_number = pascal_number
        self.pascal_number239 = pascal_number239
        
    @property
    def real(self) -> str:
        return self.__real

    @real.setter
    def real(self, real: str):
        self.__real = real

    @property
    def integer(self) -> str:
        return self.__integer

    @integer.setter
    def integer(self, integer: str):
        self.__integer = integer

    @property
    def pascal_number(self):
        return self.__pascal_number

    @pascal_number.setter
    def pascal_number(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_number__pascal_number", None)
        self.__pascal_number = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor148"):
                opp_val = getattr(old_value, "pascal_factor148", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor148", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor148"):
                opp_val = getattr(value, "pascal_factor148", None)
                setattr(value, "pascal_factor148", self)

    @property
    def pascal_number239(self):
        return self.__pascal_number239

    @pascal_number239.setter
    def pascal_number239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_number__pascal_number239", None)
        self.__pascal_number239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant238"):
                opp_val = getattr(old_value, "pascal_constant238", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant238", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant238"):
                opp_val = getattr(value, "pascal_constant238", None)
                setattr(value, "pascal_constant238", self)

class pascal_FunctionDesignator:

    def __init__(self, name: str, pascal_FunctionDesignator: "pascal_factor" = None):
        self.name = name
        self.pascal_FunctionDesignator = pascal_FunctionDesignator
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_FunctionDesignator(self):
        return self.__pascal_FunctionDesignator

    @pascal_FunctionDesignator.setter
    def pascal_FunctionDesignator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_FunctionDesignator__pascal_FunctionDesignator", None)
        self.__pascal_FunctionDesignator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor143"):
                opp_val = getattr(old_value, "pascal_factor143", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor143"):
                opp_val = getattr(value, "pascal_factor143", None)
                setattr(value, "pascal_factor143", self)

class pascal_factor:

    def __init__(self, nil: str, id: str, string: str, pascal_factor150: "pascal_Set" = None, pascal_factor152: "pascal_expression" = None, pascal_factor156: "pascal_factor" = None, pascal_factor154: "pascal_factor" = None, pascal_factor: "pascal_term" = None, pascal_factor143: "pascal_FunctionDesignator" = None, pascal_factor145: "pascal_variable" = None, pascal_factor148: "pascal_number" = None):
        self.nil = nil
        self.id = id
        self.string = string
        self.pascal_factor150 = pascal_factor150
        self.pascal_factor152 = pascal_factor152
        self.pascal_factor156 = pascal_factor156
        self.pascal_factor154 = pascal_factor154
        self.pascal_factor = pascal_factor
        self.pascal_factor143 = pascal_factor143
        self.pascal_factor145 = pascal_factor145
        self.pascal_factor148 = pascal_factor148
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def nil(self) -> str:
        return self.__nil

    @nil.setter
    def nil(self, nil: str):
        self.__nil = nil

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pascal_factor(self):
        return self.__pascal_factor

    @pascal_factor.setter
    def pascal_factor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor", None)
        self.__pascal_factor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_term141"):
                opp_val = getattr(old_value, "pascal_term141", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_term141"):
                opp_val = getattr(value, "pascal_term141", None)
                if opp_val is None:
                    setattr(value, "pascal_term141", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_factor152(self):
        return self.__pascal_factor152

    @pascal_factor152.setter
    def pascal_factor152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor152", None)
        self.__pascal_factor152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression153"):
                opp_val = getattr(old_value, "pascal_expression153", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression153", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression153"):
                opp_val = getattr(value, "pascal_expression153", None)
                setattr(value, "pascal_expression153", self)

    @property
    def pascal_factor150(self):
        return self.__pascal_factor150

    @pascal_factor150.setter
    def pascal_factor150(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor150", None)
        self.__pascal_factor150 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_Set"):
                opp_val = getattr(old_value, "pascal_Set", None)
                if opp_val == self:
                    setattr(old_value, "pascal_Set", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_Set"):
                opp_val = getattr(value, "pascal_Set", None)
                setattr(value, "pascal_Set", self)

    @property
    def pascal_factor145(self):
        return self.__pascal_factor145

    @pascal_factor145.setter
    def pascal_factor145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor145", None)
        self.__pascal_factor145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable146"):
                opp_val = getattr(old_value, "pascal_variable146", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable146"):
                opp_val = getattr(value, "pascal_variable146", None)
                setattr(value, "pascal_variable146", self)

    @property
    def pascal_factor143(self):
        return self.__pascal_factor143

    @pascal_factor143.setter
    def pascal_factor143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor143", None)
        self.__pascal_factor143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_FunctionDesignator"):
                opp_val = getattr(old_value, "pascal_FunctionDesignator", None)
                if opp_val == self:
                    setattr(old_value, "pascal_FunctionDesignator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_FunctionDesignator"):
                opp_val = getattr(value, "pascal_FunctionDesignator", None)
                setattr(value, "pascal_FunctionDesignator", self)

    @property
    def pascal_factor156(self):
        return self.__pascal_factor156

    @pascal_factor156.setter
    def pascal_factor156(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor156", None)
        self.__pascal_factor156 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor154"):
                opp_val = getattr(old_value, "pascal_factor154", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor154", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor154"):
                opp_val = getattr(value, "pascal_factor154", None)
                setattr(value, "pascal_factor154", self)

    @property
    def pascal_factor148(self):
        return self.__pascal_factor148

    @pascal_factor148.setter
    def pascal_factor148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor148", None)
        self.__pascal_factor148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_number"):
                opp_val = getattr(old_value, "pascal_number", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number"):
                opp_val = getattr(value, "pascal_number", None)
                setattr(value, "pascal_number", self)

    @property
    def pascal_factor154(self):
        return self.__pascal_factor154

    @pascal_factor154.setter
    def pascal_factor154(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor154", None)
        self.__pascal_factor154 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor156"):
                opp_val = getattr(old_value, "pascal_factor156", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor156", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor156"):
                opp_val = getattr(value, "pascal_factor156", None)
                setattr(value, "pascal_factor156", self)

class pascal_term:

    pass
class pascal_Variable1:

    def __init__(self, name: str, pascal_Variable1: "pascal_variable" = None, pascal_Variable1160: "pascal_ExpressionList" = None, pascal_Variable1163: "pascal_Variable1" = None, pascal_Variable1161: "pascal_Variable1" = None):
        self.name = name
        self.pascal_Variable1 = pascal_Variable1
        self.pascal_Variable1160 = pascal_Variable1160
        self.pascal_Variable1163 = pascal_Variable1163
        self.pascal_Variable1161 = pascal_Variable1161
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_Variable1160(self):
        return self.__pascal_Variable1160

    @pascal_Variable1160.setter
    def pascal_Variable1160(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_Variable1__pascal_Variable1160", None)
        self.__pascal_Variable1160 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_ExpressionList"):
                opp_val = getattr(old_value, "pascal_ExpressionList", None)
                if opp_val == self:
                    setattr(old_value, "pascal_ExpressionList", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_ExpressionList"):
                opp_val = getattr(value, "pascal_ExpressionList", None)
                setattr(value, "pascal_ExpressionList", self)

    @property
    def pascal_Variable1161(self):
        return self.__pascal_Variable1161

    @pascal_Variable1161.setter
    def pascal_Variable1161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_Variable1__pascal_Variable1161", None)
        self.__pascal_Variable1161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_Variable1163"):
                opp_val = getattr(old_value, "pascal_Variable1163", None)
                if opp_val == self:
                    setattr(old_value, "pascal_Variable1163", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_Variable1163"):
                opp_val = getattr(value, "pascal_Variable1163", None)
                setattr(value, "pascal_Variable1163", self)

    @property
    def pascal_Variable1(self):
        return self.__pascal_Variable1

    @pascal_Variable1.setter
    def pascal_Variable1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_Variable1__pascal_Variable1", None)
        self.__pascal_Variable1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable158"):
                opp_val = getattr(old_value, "pascal_variable158", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable158", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable158"):
                opp_val = getattr(value, "pascal_variable158", None)
                setattr(value, "pascal_variable158", self)

    @property
    def pascal_Variable1163(self):
        return self.__pascal_Variable1163

    @pascal_Variable1163.setter
    def pascal_Variable1163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_Variable1__pascal_Variable1163", None)
        self.__pascal_Variable1163 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_Variable1161"):
                opp_val = getattr(old_value, "pascal_Variable1161", None)
                if opp_val == self:
                    setattr(old_value, "pascal_Variable1161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_Variable1161"):
                opp_val = getattr(value, "pascal_Variable1161", None)
                setattr(value, "pascal_Variable1161", self)

class pascal_Set:

    pass
class pascal_variable:

    def __init__(self, name: str, pascal_variable: "pascal_with_statement" = None, pascal_variable158: "pascal_Variable1" = None, pascal_variable146: "pascal_factor" = None):
        self.name = name
        self.pascal_variable = pascal_variable
        self.pascal_variable158 = pascal_variable158
        self.pascal_variable146 = pascal_variable146
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_variable146(self):
        return self.__pascal_variable146

    @pascal_variable146.setter
    def pascal_variable146(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable146", None)
        self.__pascal_variable146 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor145"):
                opp_val = getattr(old_value, "pascal_factor145", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor145", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor145"):
                opp_val = getattr(value, "pascal_factor145", None)
                setattr(value, "pascal_factor145", self)

    @property
    def pascal_variable158(self):
        return self.__pascal_variable158

    @pascal_variable158.setter
    def pascal_variable158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable158", None)
        self.__pascal_variable158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_Variable1"):
                opp_val = getattr(old_value, "pascal_Variable1", None)
                if opp_val == self:
                    setattr(old_value, "pascal_Variable1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_Variable1"):
                opp_val = getattr(value, "pascal_Variable1", None)
                setattr(value, "pascal_Variable1", self)

    @property
    def pascal_variable(self):
        return self.__pascal_variable

    @pascal_variable.setter
    def pascal_variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable", None)
        self.__pascal_variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_with_statement"):
                opp_val = getattr(old_value, "pascal_with_statement", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_with_statement"):
                opp_val = getattr(value, "pascal_with_statement", None)
                if opp_val is None:
                    setattr(value, "pascal_with_statement", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_constant(constant_definition):

    def __init__(self, name: str, string: str, pascal_constant: "pascal_case_label_list" = None, pascal_constant187: "pascal_subrange_type" = None, pascal_constant184: "pascal_subrange_type" = None, pascal_constant238: "pascal_number" = None):
        self.name = name
        self.string = string
        self.pascal_constant = pascal_constant
        self.pascal_constant187 = pascal_constant187
        self.pascal_constant184 = pascal_constant184
        self.pascal_constant238 = pascal_constant238
        
    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_constant(self):
        return self.__pascal_constant

    @pascal_constant.setter
    def pascal_constant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant", None)
        self.__pascal_constant = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_case_label_list131"):
                opp_val = getattr(old_value, "pascal_case_label_list131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_label_list131"):
                opp_val = getattr(value, "pascal_case_label_list131", None)
                if opp_val is None:
                    setattr(value, "pascal_case_label_list131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_constant184(self):
        return self.__pascal_constant184

    @pascal_constant184.setter
    def pascal_constant184(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant184", None)
        self.__pascal_constant184 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type183"):
                opp_val = getattr(old_value, "pascal_subrange_type183", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type183"):
                opp_val = getattr(value, "pascal_subrange_type183", None)
                setattr(value, "pascal_subrange_type183", self)

    @property
    def pascal_constant187(self):
        return self.__pascal_constant187

    @pascal_constant187.setter
    def pascal_constant187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant187", None)
        self.__pascal_constant187 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type186"):
                opp_val = getattr(old_value, "pascal_subrange_type186", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type186"):
                opp_val = getattr(value, "pascal_subrange_type186", None)
                setattr(value, "pascal_subrange_type186", self)

    @property
    def pascal_constant238(self):
        return self.__pascal_constant238

    @pascal_constant238.setter
    def pascal_constant238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant238", None)
        self.__pascal_constant238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_number239"):
                opp_val = getattr(old_value, "pascal_number239", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number239"):
                opp_val = getattr(value, "pascal_number239", None)
                setattr(value, "pascal_number239", self)

class pascal_case_label_list:

    pass
class pascal_case_limb:

    pass
class pascal_simple_expression:

    pass
class pascal_if_statement:

    pass
class pascal_case_statement:

    pass
class structured_statement:

    pass
class pascal_repetitive_statement(structured_statement):

    pass
class pascal_with_statement(structured_statement):

    pass
class pascal_conditional_statement(structured_statement):

    pass
class pascal_compound_statement(structured_statement):

    pass
class pascal_structured_statement:

    pass
class pascal_expression:

    def __init__(self, relational_operators: str, pascal_expression91: "pascal_while_statement" = None, pascal_expression99: "pascal_repeat_statement" = None, pascal_expression: "pascal_assignment_statement" = None, pascal_expression113: "pascal_if_statement" = None, pascal_expression101: "pascal_for_statement" = None, pascal_expression104: "pascal_for_statement" = None, pascal_expression137: set["pascal_simple_expression"] = None, pascal_expression122: "pascal_case_statement" = None, pascal_expression153: "pascal_factor" = None, pascal_expression168: "pascal_ElementList" = None, pascal_expression236: "pascal_ExpressionList" = None):
        self.relational_operators = relational_operators
        self.pascal_expression91 = pascal_expression91
        self.pascal_expression99 = pascal_expression99
        self.pascal_expression = pascal_expression
        self.pascal_expression113 = pascal_expression113
        self.pascal_expression101 = pascal_expression101
        self.pascal_expression104 = pascal_expression104
        self.pascal_expression137 = pascal_expression137 if pascal_expression137 is not None else set()
        self.pascal_expression122 = pascal_expression122
        self.pascal_expression153 = pascal_expression153
        self.pascal_expression168 = pascal_expression168
        self.pascal_expression236 = pascal_expression236
        
    @property
    def relational_operators(self) -> str:
        return self.__relational_operators

    @relational_operators.setter
    def relational_operators(self, relational_operators: str):
        self.__relational_operators = relational_operators

    @property
    def pascal_expression137(self):
        return self.__pascal_expression137

    @pascal_expression137.setter
    def pascal_expression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression137", None)
        self.__pascal_expression137 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_simple_expression"):
                    opp_val = getattr(item, "pascal_simple_expression", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_simple_expression", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_simple_expression"):
                    opp_val = getattr(item, "pascal_simple_expression", None)
                    
                    setattr(item, "pascal_simple_expression", self)
                    

    @property
    def pascal_expression236(self):
        return self.__pascal_expression236

    @pascal_expression236.setter
    def pascal_expression236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression236", None)
        self.__pascal_expression236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_ExpressionList235"):
                opp_val = getattr(old_value, "pascal_ExpressionList235", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_ExpressionList235"):
                opp_val = getattr(value, "pascal_ExpressionList235", None)
                if opp_val is None:
                    setattr(value, "pascal_ExpressionList235", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_expression(self):
        return self.__pascal_expression

    @pascal_expression.setter
    def pascal_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression", None)
        self.__pascal_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_assignment_statement"):
                opp_val = getattr(old_value, "pascal_assignment_statement", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement"):
                opp_val = getattr(value, "pascal_assignment_statement", None)
                setattr(value, "pascal_assignment_statement", self)

    @property
    def pascal_expression168(self):
        return self.__pascal_expression168

    @pascal_expression168.setter
    def pascal_expression168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression168", None)
        self.__pascal_expression168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_ElementList167"):
                opp_val = getattr(old_value, "pascal_ElementList167", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_ElementList167"):
                opp_val = getattr(value, "pascal_ElementList167", None)
                if opp_val is None:
                    setattr(value, "pascal_ElementList167", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_expression99(self):
        return self.__pascal_expression99

    @pascal_expression99.setter
    def pascal_expression99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression99", None)
        self.__pascal_expression99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_repeat_statement98"):
                opp_val = getattr(old_value, "pascal_repeat_statement98", None)
                if opp_val == self:
                    setattr(old_value, "pascal_repeat_statement98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_repeat_statement98"):
                opp_val = getattr(value, "pascal_repeat_statement98", None)
                setattr(value, "pascal_repeat_statement98", self)

    @property
    def pascal_expression91(self):
        return self.__pascal_expression91

    @pascal_expression91.setter
    def pascal_expression91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression91", None)
        self.__pascal_expression91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_while_statement"):
                opp_val = getattr(old_value, "pascal_while_statement", None)
                if opp_val == self:
                    setattr(old_value, "pascal_while_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_while_statement"):
                opp_val = getattr(value, "pascal_while_statement", None)
                setattr(value, "pascal_while_statement", self)

    @property
    def pascal_expression101(self):
        return self.__pascal_expression101

    @pascal_expression101.setter
    def pascal_expression101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression101", None)
        self.__pascal_expression101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_for_statement"):
                opp_val = getattr(old_value, "pascal_for_statement", None)
                if opp_val == self:
                    setattr(old_value, "pascal_for_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_for_statement"):
                opp_val = getattr(value, "pascal_for_statement", None)
                setattr(value, "pascal_for_statement", self)

    @property
    def pascal_expression122(self):
        return self.__pascal_expression122

    @pascal_expression122.setter
    def pascal_expression122(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression122", None)
        self.__pascal_expression122 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_case_statement121"):
                opp_val = getattr(old_value, "pascal_case_statement121", None)
                if opp_val == self:
                    setattr(old_value, "pascal_case_statement121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_statement121"):
                opp_val = getattr(value, "pascal_case_statement121", None)
                setattr(value, "pascal_case_statement121", self)

    @property
    def pascal_expression153(self):
        return self.__pascal_expression153

    @pascal_expression153.setter
    def pascal_expression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression153", None)
        self.__pascal_expression153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor152"):
                opp_val = getattr(old_value, "pascal_factor152", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor152"):
                opp_val = getattr(value, "pascal_factor152", None)
                setattr(value, "pascal_factor152", self)

    @property
    def pascal_expression104(self):
        return self.__pascal_expression104

    @pascal_expression104.setter
    def pascal_expression104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression104", None)
        self.__pascal_expression104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_for_statement103"):
                opp_val = getattr(old_value, "pascal_for_statement103", None)
                if opp_val == self:
                    setattr(old_value, "pascal_for_statement103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_for_statement103"):
                opp_val = getattr(value, "pascal_for_statement103", None)
                setattr(value, "pascal_for_statement103", self)

    @property
    def pascal_expression113(self):
        return self.__pascal_expression113

    @pascal_expression113.setter
    def pascal_expression113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression113", None)
        self.__pascal_expression113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_if_statement112"):
                opp_val = getattr(old_value, "pascal_if_statement112", None)
                if opp_val == self:
                    setattr(old_value, "pascal_if_statement112", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_if_statement112"):
                opp_val = getattr(value, "pascal_if_statement112", None)
                setattr(value, "pascal_if_statement112", self)

class repetitive_statement:

    pass
class pascal_repeat_statement(repetitive_statement):

    pass
class pascal_for_statement(repetitive_statement):

    def __init__(self, name: str, pascal_for_statement: "pascal_expression" = None, pascal_for_statement103: "pascal_expression" = None, pascal_for_statement106: "pascal_statement" = None):
        self.name = name
        self.pascal_for_statement = pascal_for_statement
        self.pascal_for_statement103 = pascal_for_statement103
        self.pascal_for_statement106 = pascal_for_statement106
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_for_statement(self):
        return self.__pascal_for_statement

    @pascal_for_statement.setter
    def pascal_for_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_for_statement__pascal_for_statement", None)
        self.__pascal_for_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression101"):
                opp_val = getattr(old_value, "pascal_expression101", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression101"):
                opp_val = getattr(value, "pascal_expression101", None)
                setattr(value, "pascal_expression101", self)

    @property
    def pascal_for_statement103(self):
        return self.__pascal_for_statement103

    @pascal_for_statement103.setter
    def pascal_for_statement103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_for_statement__pascal_for_statement103", None)
        self.__pascal_for_statement103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression104"):
                opp_val = getattr(old_value, "pascal_expression104", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression104"):
                opp_val = getattr(value, "pascal_expression104", None)
                setattr(value, "pascal_expression104", self)

    @property
    def pascal_for_statement106(self):
        return self.__pascal_for_statement106

    @pascal_for_statement106.setter
    def pascal_for_statement106(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_for_statement__pascal_for_statement106", None)
        self.__pascal_for_statement106 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_statement107"):
                opp_val = getattr(old_value, "pascal_statement107", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement107"):
                opp_val = getattr(value, "pascal_statement107", None)
                setattr(value, "pascal_statement107", self)

class pascal_while_statement(repetitive_statement):

    pass
class pascal_bound_specification:

    def __init__(self, id3: str, id1: str, id2: str, pascal_bound_specification: "pascal_packed_conformant_array_schema" = None, pascal_bound_specification80: "pascal_unpacked_conformant_array_Schema" = None):
        self.id3 = id3
        self.id1 = id1
        self.id2 = id2
        self.pascal_bound_specification = pascal_bound_specification
        self.pascal_bound_specification80 = pascal_bound_specification80
        
    @property
    def id2(self) -> str:
        return self.__id2

    @id2.setter
    def id2(self, id2: str):
        self.__id2 = id2

    @property
    def id3(self) -> str:
        return self.__id3

    @id3.setter
    def id3(self, id3: str):
        self.__id3 = id3

    @property
    def id1(self) -> str:
        return self.__id1

    @id1.setter
    def id1(self, id1: str):
        self.__id1 = id1

    @property
    def pascal_bound_specification80(self):
        return self.__pascal_bound_specification80

    @pascal_bound_specification80.setter
    def pascal_bound_specification80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_bound_specification__pascal_bound_specification80", None)
        self.__pascal_bound_specification80 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_conformant_array_Schema"):
                opp_val = getattr(old_value, "pascal_unpacked_conformant_array_Schema", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_conformant_array_Schema"):
                opp_val = getattr(value, "pascal_unpacked_conformant_array_Schema", None)
                if opp_val is None:
                    setattr(value, "pascal_unpacked_conformant_array_Schema", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_bound_specification(self):
        return self.__pascal_bound_specification

    @pascal_bound_specification.setter
    def pascal_bound_specification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_bound_specification__pascal_bound_specification", None)
        self.__pascal_bound_specification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_packed_conformant_array_schema"):
                opp_val = getattr(old_value, "pascal_packed_conformant_array_schema", None)
                if opp_val == self:
                    setattr(old_value, "pascal_packed_conformant_array_schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_packed_conformant_array_schema"):
                opp_val = getattr(value, "pascal_packed_conformant_array_schema", None)
                setattr(value, "pascal_packed_conformant_array_schema", self)

class conformant_array_schema:

    pass
class pascal_unpacked_conformant_array_Schema(conformant_array_schema):

    pass
class pascal_packed_conformant_array_schema(conformant_array_schema):

    pass
class simple_statement:

    pass
class pascal_goto_statement(simple_statement):

    pass
class pascal_procedure_statement(simple_statement):

    def __init__(self, name: str, actualParameterList: str):
        self.name = name
        self.actualParameterList = actualParameterList
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def actualParameterList(self) -> str:
        return self.__actualParameterList

    @actualParameterList.setter
    def actualParameterList(self, actualParameterList: str):
        self.__actualParameterList = actualParameterList

class pascal_assignment_statement(simple_statement):

    def __init__(self, variable: str, identifier: str, pascal_assignment_statement: "pascal_expression" = None):
        self.variable = variable
        self.identifier = identifier
        self.pascal_assignment_statement = pascal_assignment_statement
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def variable(self) -> str:
        return self.__variable

    @variable.setter
    def variable(self, variable: str):
        self.__variable = variable

    @property
    def pascal_assignment_statement(self):
        return self.__pascal_assignment_statement

    @pascal_assignment_statement.setter
    def pascal_assignment_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_assignment_statement__pascal_assignment_statement", None)
        self.__pascal_assignment_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression"):
                opp_val = getattr(old_value, "pascal_expression", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression"):
                opp_val = getattr(value, "pascal_expression", None)
                setattr(value, "pascal_expression", self)

class pascal_simple_statement:

    pass
class pascal_EObject:

    pass
class pascal_statement:

    pass
class statement_part:

    pass
class pascal_statement_sequence(statement_part):

    pass
class pascal_parameter_type:

    def __init__(self, id: str, pascal_parameter_type: "pascal_value_parameter_section" = None, pascal_parameter_type75: "pascal_variable_parameter_section" = None, pascal_parameter_type77: "pascal_conformant_array_schema" = None):
        self.id = id
        self.pascal_parameter_type = pascal_parameter_type
        self.pascal_parameter_type75 = pascal_parameter_type75
        self.pascal_parameter_type77 = pascal_parameter_type77
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pascal_parameter_type75(self):
        return self.__pascal_parameter_type75

    @pascal_parameter_type75.setter
    def pascal_parameter_type75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type75", None)
        self.__pascal_parameter_type75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_parameter_section74"):
                opp_val = getattr(old_value, "pascal_variable_parameter_section74", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_parameter_section74", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_parameter_section74"):
                opp_val = getattr(value, "pascal_variable_parameter_section74", None)
                setattr(value, "pascal_variable_parameter_section74", self)

    @property
    def pascal_parameter_type(self):
        return self.__pascal_parameter_type

    @pascal_parameter_type.setter
    def pascal_parameter_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type", None)
        self.__pascal_parameter_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_value_parameter_section69"):
                opp_val = getattr(old_value, "pascal_value_parameter_section69", None)
                if opp_val == self:
                    setattr(old_value, "pascal_value_parameter_section69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_value_parameter_section69"):
                opp_val = getattr(value, "pascal_value_parameter_section69", None)
                setattr(value, "pascal_value_parameter_section69", self)

    @property
    def pascal_parameter_type77(self):
        return self.__pascal_parameter_type77

    @pascal_parameter_type77.setter
    def pascal_parameter_type77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type77", None)
        self.__pascal_parameter_type77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_conformant_array_schema"):
                opp_val = getattr(old_value, "pascal_conformant_array_schema", None)
                if opp_val == self:
                    setattr(old_value, "pascal_conformant_array_schema", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_conformant_array_schema"):
                opp_val = getattr(value, "pascal_conformant_array_schema", None)
                setattr(value, "pascal_conformant_array_schema", self)

class pascal_variable_parameter_section:

    pass
class pascal_value_parameter_section:

    pass
class pascal_conformant_array_schema:

    def __init__(self, id: str, pascal_conformant_array_schema: "pascal_parameter_type" = None, pascal_conformant_array_schema83: "pascal_unpacked_conformant_array_Schema" = None):
        self.id = id
        self.pascal_conformant_array_schema = pascal_conformant_array_schema
        self.pascal_conformant_array_schema83 = pascal_conformant_array_schema83
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pascal_conformant_array_schema83(self):
        return self.__pascal_conformant_array_schema83

    @pascal_conformant_array_schema83.setter
    def pascal_conformant_array_schema83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_conformant_array_schema__pascal_conformant_array_schema83", None)
        self.__pascal_conformant_array_schema83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_conformant_array_Schema82"):
                opp_val = getattr(old_value, "pascal_unpacked_conformant_array_Schema82", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unpacked_conformant_array_Schema82", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_conformant_array_Schema82"):
                opp_val = getattr(value, "pascal_unpacked_conformant_array_Schema82", None)
                setattr(value, "pascal_unpacked_conformant_array_Schema82", self)

    @property
    def pascal_conformant_array_schema(self):
        return self.__pascal_conformant_array_schema

    @pascal_conformant_array_schema.setter
    def pascal_conformant_array_schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_conformant_array_schema__pascal_conformant_array_schema", None)
        self.__pascal_conformant_array_schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_parameter_type77"):
                opp_val = getattr(old_value, "pascal_parameter_type77", None)
                if opp_val == self:
                    setattr(old_value, "pascal_parameter_type77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_parameter_type77"):
                opp_val = getattr(value, "pascal_parameter_type77", None)
                setattr(value, "pascal_parameter_type77", self)

class pascal_formal_parameter_list:

    pass
class pascal_formal_parameter_section:

    pass
class pascal_function_heading:

    def __init__(self, id1: str, id2: str, pascal_function_heading: "pascal_formal_parameter_list" = None, pascal_function_heading64: "pascal_formal_parameter_section" = None):
        self.id1 = id1
        self.id2 = id2
        self.pascal_function_heading = pascal_function_heading
        self.pascal_function_heading64 = pascal_function_heading64
        
    @property
    def id1(self) -> str:
        return self.__id1

    @id1.setter
    def id1(self, id1: str):
        self.__id1 = id1

    @property
    def id2(self) -> str:
        return self.__id2

    @id2.setter
    def id2(self, id2: str):
        self.__id2 = id2

    @property
    def pascal_function_heading64(self):
        return self.__pascal_function_heading64

    @pascal_function_heading64.setter
    def pascal_function_heading64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_heading__pascal_function_heading64", None)
        self.__pascal_function_heading64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_section63"):
                opp_val = getattr(old_value, "pascal_formal_parameter_section63", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_section63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_section63"):
                opp_val = getattr(value, "pascal_formal_parameter_section63", None)
                setattr(value, "pascal_formal_parameter_section63", self)

    @property
    def pascal_function_heading(self):
        return self.__pascal_function_heading

    @pascal_function_heading.setter
    def pascal_function_heading(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_heading__pascal_function_heading", None)
        self.__pascal_function_heading = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_list52"):
                opp_val = getattr(old_value, "pascal_formal_parameter_list52", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_list52", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_list52"):
                opp_val = getattr(value, "pascal_formal_parameter_list52", None)
                setattr(value, "pascal_formal_parameter_list52", self)

class pascal_procedure_heading:

    def __init__(self, name: str, pascal_procedure_heading: "pascal_formal_parameter_list" = None, pascal_procedure_heading61: "pascal_formal_parameter_section" = None):
        self.name = name
        self.pascal_procedure_heading = pascal_procedure_heading
        self.pascal_procedure_heading61 = pascal_procedure_heading61
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_procedure_heading(self):
        return self.__pascal_procedure_heading

    @pascal_procedure_heading.setter
    def pascal_procedure_heading(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_procedure_heading__pascal_procedure_heading", None)
        self.__pascal_procedure_heading = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_list50"):
                opp_val = getattr(old_value, "pascal_formal_parameter_list50", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_list50", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_list50"):
                opp_val = getattr(value, "pascal_formal_parameter_list50", None)
                setattr(value, "pascal_formal_parameter_list50", self)

    @property
    def pascal_procedure_heading61(self):
        return self.__pascal_procedure_heading61

    @pascal_procedure_heading61.setter
    def pascal_procedure_heading61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_procedure_heading__pascal_procedure_heading61", None)
        self.__pascal_procedure_heading61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_section60"):
                opp_val = getattr(old_value, "pascal_formal_parameter_section60", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_section60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_section60"):
                opp_val = getattr(value, "pascal_formal_parameter_section60", None)
                setattr(value, "pascal_formal_parameter_section60", self)

class pascal_type_definition:

    pass
class pascal_constant_definition:

    pass
class pascal_label(goto_statement, statement):

    def __init__(self, int: str, pascal_label: "pascal_label_declaration_part" = None):
        self.int = int
        self.pascal_label = pascal_label
        
    @property
    def int(self) -> str:
        return self.__int

    @int.setter
    def int(self, int: str):
        self.__int = int

    @property
    def pascal_label(self):
        return self.__pascal_label

    @pascal_label.setter
    def pascal_label(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_label__pascal_label", None)
        self.__pascal_label = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_label_declaration_part20"):
                opp_val = getattr(old_value, "pascal_label_declaration_part20", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_label_declaration_part20"):
                opp_val = getattr(value, "pascal_label_declaration_part20", None)
                if opp_val is None:
                    setattr(value, "pascal_label_declaration_part20", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_procedure_and_function_declaration_part:

    pass
class pascal_function_declaration:

    def __init__(self, name: str, pascal_function_declaration: "pascal_procedure_and_function_declaration_part" = None, pascal_function_declaration41: "pascal_formal_parameter_list" = None, pascal_function_declaration44: "pascal_type" = None, pascal_function_declaration47: "pascal_block" = None):
        self.name = name
        self.pascal_function_declaration = pascal_function_declaration
        self.pascal_function_declaration41 = pascal_function_declaration41
        self.pascal_function_declaration44 = pascal_function_declaration44
        self.pascal_function_declaration47 = pascal_function_declaration47
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_function_declaration41(self):
        return self.__pascal_function_declaration41

    @pascal_function_declaration41.setter
    def pascal_function_declaration41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_declaration__pascal_function_declaration41", None)
        self.__pascal_function_declaration41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_list42"):
                opp_val = getattr(old_value, "pascal_formal_parameter_list42", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_list42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_list42"):
                opp_val = getattr(value, "pascal_formal_parameter_list42", None)
                setattr(value, "pascal_formal_parameter_list42", self)

    @property
    def pascal_function_declaration47(self):
        return self.__pascal_function_declaration47

    @pascal_function_declaration47.setter
    def pascal_function_declaration47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_declaration__pascal_function_declaration47", None)
        self.__pascal_function_declaration47 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_block48"):
                opp_val = getattr(old_value, "pascal_block48", None)
                if opp_val == self:
                    setattr(old_value, "pascal_block48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_block48"):
                opp_val = getattr(value, "pascal_block48", None)
                setattr(value, "pascal_block48", self)

    @property
    def pascal_function_declaration(self):
        return self.__pascal_function_declaration

    @pascal_function_declaration.setter
    def pascal_function_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_declaration__pascal_function_declaration", None)
        self.__pascal_function_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_procedure_and_function_declaration_part34"):
                opp_val = getattr(old_value, "pascal_procedure_and_function_declaration_part34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_and_function_declaration_part34"):
                opp_val = getattr(value, "pascal_procedure_and_function_declaration_part34", None)
                if opp_val is None:
                    setattr(value, "pascal_procedure_and_function_declaration_part34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_function_declaration44(self):
        return self.__pascal_function_declaration44

    @pascal_function_declaration44.setter
    def pascal_function_declaration44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_declaration__pascal_function_declaration44", None)
        self.__pascal_function_declaration44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_type45"):
                opp_val = getattr(old_value, "pascal_type45", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type45"):
                opp_val = getattr(value, "pascal_type45", None)
                setattr(value, "pascal_type45", self)

class pascal_variable_declaration_part:

    pass
class pascal_procedure_declaration:

    def __init__(self, name: str, pascal_procedure_declaration: "pascal_procedure_and_function_declaration_part" = None, pascal_procedure_declaration36: "pascal_formal_parameter_list" = None, pascal_procedure_declaration38: "pascal_block" = None):
        self.name = name
        self.pascal_procedure_declaration = pascal_procedure_declaration
        self.pascal_procedure_declaration36 = pascal_procedure_declaration36
        self.pascal_procedure_declaration38 = pascal_procedure_declaration38
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_procedure_declaration36(self):
        return self.__pascal_procedure_declaration36

    @pascal_procedure_declaration36.setter
    def pascal_procedure_declaration36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_procedure_declaration__pascal_procedure_declaration36", None)
        self.__pascal_procedure_declaration36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_list"):
                opp_val = getattr(old_value, "pascal_formal_parameter_list", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_list"):
                opp_val = getattr(value, "pascal_formal_parameter_list", None)
                setattr(value, "pascal_formal_parameter_list", self)

    @property
    def pascal_procedure_declaration38(self):
        return self.__pascal_procedure_declaration38

    @pascal_procedure_declaration38.setter
    def pascal_procedure_declaration38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_procedure_declaration__pascal_procedure_declaration38", None)
        self.__pascal_procedure_declaration38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_block39"):
                opp_val = getattr(old_value, "pascal_block39", None)
                if opp_val == self:
                    setattr(old_value, "pascal_block39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_block39"):
                opp_val = getattr(value, "pascal_block39", None)
                setattr(value, "pascal_block39", self)

    @property
    def pascal_procedure_declaration(self):
        return self.__pascal_procedure_declaration

    @pascal_procedure_declaration.setter
    def pascal_procedure_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_procedure_declaration__pascal_procedure_declaration", None)
        self.__pascal_procedure_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_procedure_and_function_declaration_part32"):
                opp_val = getattr(old_value, "pascal_procedure_and_function_declaration_part32", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_and_function_declaration_part32"):
                opp_val = getattr(value, "pascal_procedure_and_function_declaration_part32", None)
                if opp_val is None:
                    setattr(value, "pascal_procedure_and_function_declaration_part32", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_type(type_definition):

    def __init__(self, name: str, pascal_type: "pascal_variable_declaration" = None, pascal_type45: "pascal_function_declaration" = None, pascal_type170: "pascal_simple_type" = None, pascal_type172: "pascal_structured_type" = None, pascal_type174: "pascal_pointer_type" = None, pascal_type208: "pascal_set_type" = None, pascal_type211: "pascal_file_type" = None, pascal_type203: "pascal_array_type" = None, pascal_type223: "pascal_record_section" = None):
        self.name = name
        self.pascal_type = pascal_type
        self.pascal_type45 = pascal_type45
        self.pascal_type170 = pascal_type170
        self.pascal_type172 = pascal_type172
        self.pascal_type174 = pascal_type174
        self.pascal_type208 = pascal_type208
        self.pascal_type211 = pascal_type211
        self.pascal_type203 = pascal_type203
        self.pascal_type223 = pascal_type223
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_type211(self):
        return self.__pascal_type211

    @pascal_type211.setter
    def pascal_type211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type211", None)
        self.__pascal_type211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_file_type210"):
                opp_val = getattr(old_value, "pascal_file_type210", None)
                if opp_val == self:
                    setattr(old_value, "pascal_file_type210", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_file_type210"):
                opp_val = getattr(value, "pascal_file_type210", None)
                setattr(value, "pascal_file_type210", self)

    @property
    def pascal_type45(self):
        return self.__pascal_type45

    @pascal_type45.setter
    def pascal_type45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type45", None)
        self.__pascal_type45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_declaration44"):
                opp_val = getattr(old_value, "pascal_function_declaration44", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_declaration44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_declaration44"):
                opp_val = getattr(value, "pascal_function_declaration44", None)
                setattr(value, "pascal_function_declaration44", self)

    @property
    def pascal_type170(self):
        return self.__pascal_type170

    @pascal_type170.setter
    def pascal_type170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type170", None)
        self.__pascal_type170 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simple_type"):
                opp_val = getattr(old_value, "pascal_simple_type", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simple_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_type"):
                opp_val = getattr(value, "pascal_simple_type", None)
                setattr(value, "pascal_simple_type", self)

    @property
    def pascal_type(self):
        return self.__pascal_type

    @pascal_type.setter
    def pascal_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type", None)
        self.__pascal_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_declaration30"):
                opp_val = getattr(old_value, "pascal_variable_declaration30", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_declaration30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_declaration30"):
                opp_val = getattr(value, "pascal_variable_declaration30", None)
                setattr(value, "pascal_variable_declaration30", self)

    @property
    def pascal_type172(self):
        return self.__pascal_type172

    @pascal_type172.setter
    def pascal_type172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type172", None)
        self.__pascal_type172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_structured_type"):
                opp_val = getattr(old_value, "pascal_structured_type", None)
                if opp_val == self:
                    setattr(old_value, "pascal_structured_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_structured_type"):
                opp_val = getattr(value, "pascal_structured_type", None)
                setattr(value, "pascal_structured_type", self)

    @property
    def pascal_type208(self):
        return self.__pascal_type208

    @pascal_type208.setter
    def pascal_type208(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type208", None)
        self.__pascal_type208 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_set_type207"):
                opp_val = getattr(old_value, "pascal_set_type207", None)
                if opp_val == self:
                    setattr(old_value, "pascal_set_type207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_set_type207"):
                opp_val = getattr(value, "pascal_set_type207", None)
                setattr(value, "pascal_set_type207", self)

    @property
    def pascal_type174(self):
        return self.__pascal_type174

    @pascal_type174.setter
    def pascal_type174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type174", None)
        self.__pascal_type174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_pointer_type"):
                opp_val = getattr(old_value, "pascal_pointer_type", None)
                if opp_val == self:
                    setattr(old_value, "pascal_pointer_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_pointer_type"):
                opp_val = getattr(value, "pascal_pointer_type", None)
                setattr(value, "pascal_pointer_type", self)

    @property
    def pascal_type203(self):
        return self.__pascal_type203

    @pascal_type203.setter
    def pascal_type203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type203", None)
        self.__pascal_type203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_array_type202"):
                opp_val = getattr(old_value, "pascal_array_type202", None)
                if opp_val == self:
                    setattr(old_value, "pascal_array_type202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_array_type202"):
                opp_val = getattr(value, "pascal_array_type202", None)
                setattr(value, "pascal_array_type202", self)

    @property
    def pascal_type223(self):
        return self.__pascal_type223

    @pascal_type223.setter
    def pascal_type223(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type__pascal_type223", None)
        self.__pascal_type223 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_record_section222"):
                opp_val = getattr(old_value, "pascal_record_section222", None)
                if opp_val == self:
                    setattr(old_value, "pascal_record_section222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_record_section222"):
                opp_val = getattr(value, "pascal_record_section222", None)
                setattr(value, "pascal_record_section222", self)

class pascal_DeclarationPart:

    pass
class pascal_identifier_list(program_heading):

    def __init__(self, ids: str, pascal_identifier_list: "pascal_variable_declaration" = None, pascal_identifier_list72: "pascal_variable_parameter_section" = None, pascal_identifier_list67: "pascal_value_parameter_section" = None, pascal_identifier_list181: "pascal_enumerated_type" = None, pascal_identifier_list220: "pascal_record_section" = None):
        self.ids = ids
        self.pascal_identifier_list = pascal_identifier_list
        self.pascal_identifier_list72 = pascal_identifier_list72
        self.pascal_identifier_list67 = pascal_identifier_list67
        self.pascal_identifier_list181 = pascal_identifier_list181
        self.pascal_identifier_list220 = pascal_identifier_list220
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def pascal_identifier_list(self):
        return self.__pascal_identifier_list

    @pascal_identifier_list.setter
    def pascal_identifier_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list", None)
        self.__pascal_identifier_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_declaration28"):
                opp_val = getattr(old_value, "pascal_variable_declaration28", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_declaration28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_declaration28"):
                opp_val = getattr(value, "pascal_variable_declaration28", None)
                setattr(value, "pascal_variable_declaration28", self)

    @property
    def pascal_identifier_list220(self):
        return self.__pascal_identifier_list220

    @pascal_identifier_list220.setter
    def pascal_identifier_list220(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list220", None)
        self.__pascal_identifier_list220 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_record_section219"):
                opp_val = getattr(old_value, "pascal_record_section219", None)
                if opp_val == self:
                    setattr(old_value, "pascal_record_section219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_record_section219"):
                opp_val = getattr(value, "pascal_record_section219", None)
                setattr(value, "pascal_record_section219", self)

    @property
    def pascal_identifier_list67(self):
        return self.__pascal_identifier_list67

    @pascal_identifier_list67.setter
    def pascal_identifier_list67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list67", None)
        self.__pascal_identifier_list67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_value_parameter_section66"):
                opp_val = getattr(old_value, "pascal_value_parameter_section66", None)
                if opp_val == self:
                    setattr(old_value, "pascal_value_parameter_section66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_value_parameter_section66"):
                opp_val = getattr(value, "pascal_value_parameter_section66", None)
                setattr(value, "pascal_value_parameter_section66", self)

    @property
    def pascal_identifier_list72(self):
        return self.__pascal_identifier_list72

    @pascal_identifier_list72.setter
    def pascal_identifier_list72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list72", None)
        self.__pascal_identifier_list72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_parameter_section71"):
                opp_val = getattr(old_value, "pascal_variable_parameter_section71", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_parameter_section71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_parameter_section71"):
                opp_val = getattr(value, "pascal_variable_parameter_section71", None)
                setattr(value, "pascal_variable_parameter_section71", self)

    @property
    def pascal_identifier_list181(self):
        return self.__pascal_identifier_list181

    @pascal_identifier_list181.setter
    def pascal_identifier_list181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list181", None)
        self.__pascal_identifier_list181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_enumerated_type180"):
                opp_val = getattr(old_value, "pascal_enumerated_type180", None)
                if opp_val == self:
                    setattr(old_value, "pascal_enumerated_type180", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_enumerated_type180"):
                opp_val = getattr(value, "pascal_enumerated_type180", None)
                setattr(value, "pascal_enumerated_type180", self)

class pascal_block:

    pass
class pascal_variable_declaration:

    pass
class pascal_type_definition_part:

    pass
class pascal_constant_definition_part:

    pass
class pascal_label_declaration_part:

    pass
class pascal_statement_part:

    pass
class pascal_program_heading:

    pass
class pascal_program:

    pass
class pascal_Model:

    pass