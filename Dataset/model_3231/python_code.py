from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pascal_record_type:

    def __init__(self, recordKeyword: str, endKeyword: str, pascal_record_type123: "pascal_field_list" = None, pascal_record_type: "pascal_unpacked_structured_type" = None):
        self.recordKeyword = recordKeyword
        self.endKeyword = endKeyword
        self.pascal_record_type123 = pascal_record_type123
        self.pascal_record_type = pascal_record_type
        
    @property
    def recordKeyword(self) -> str:
        return self.__recordKeyword

    @recordKeyword.setter
    def recordKeyword(self, recordKeyword: str):
        self.__recordKeyword = recordKeyword

    @property
    def endKeyword(self) -> str:
        return self.__endKeyword

    @endKeyword.setter
    def endKeyword(self, endKeyword: str):
        self.__endKeyword = endKeyword

    @property
    def pascal_record_type123(self):
        return self.__pascal_record_type123

    @pascal_record_type123.setter
    def pascal_record_type123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_record_type__pascal_record_type123", None)
        self.__pascal_record_type123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_field_list"):
                opp_val = getattr(old_value, "pascal_field_list", None)
                if opp_val == self:
                    setattr(old_value, "pascal_field_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_field_list"):
                opp_val = getattr(value, "pascal_field_list", None)
                setattr(value, "pascal_field_list", self)

    @property
    def pascal_record_type(self):
        return self.__pascal_record_type

    @pascal_record_type.setter
    def pascal_record_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_record_type__pascal_record_type", None)
        self.__pascal_record_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_structured_type121"):
                opp_val = getattr(old_value, "pascal_unpacked_structured_type121", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unpacked_structured_type121", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_structured_type121"):
                opp_val = getattr(value, "pascal_unpacked_structured_type121", None)
                setattr(value, "pascal_unpacked_structured_type121", self)

class pascal_variable_identifier_list:

    def __init__(self, names: str, pascal_variable_identifier_list: "pascal_variable_section" = None):
        self.names = names
        self.pascal_variable_identifier_list = pascal_variable_identifier_list
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def pascal_variable_identifier_list(self):
        return self.__pascal_variable_identifier_list

    @pascal_variable_identifier_list.setter
    def pascal_variable_identifier_list(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable_identifier_list__pascal_variable_identifier_list", None)
        self.__pascal_variable_identifier_list = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_section135"):
                opp_val = getattr(old_value, "pascal_variable_section135", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_section135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_section135"):
                opp_val = getattr(value, "pascal_variable_section135", None)
                setattr(value, "pascal_variable_section135", self)

class pascal_variable_section:

    pass
class pascal_record_section:

    pass
class pascal_field_list:

    pass
class pascal_type:

    pass
class pascal_type_definition:

    def __init__(self, name: str, pascal_type_definition: "pascal_type_definition_part" = None, pascal_type_definition113: "pascal_type" = None):
        self.name = name
        self.pascal_type_definition = pascal_type_definition
        self.pascal_type_definition113 = pascal_type_definition113
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_type_definition(self):
        return self.__pascal_type_definition

    @pascal_type_definition.setter
    def pascal_type_definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type_definition__pascal_type_definition", None)
        self.__pascal_type_definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_type_definition_part111"):
                opp_val = getattr(old_value, "pascal_type_definition_part111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type_definition_part111"):
                opp_val = getattr(value, "pascal_type_definition_part111", None)
                if opp_val is None:
                    setattr(value, "pascal_type_definition_part111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_type_definition113(self):
        return self.__pascal_type_definition113

    @pascal_type_definition113.setter
    def pascal_type_definition113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type_definition__pascal_type_definition113", None)
        self.__pascal_type_definition113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_type"):
                opp_val = getattr(old_value, "pascal_type", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type"):
                opp_val = getattr(value, "pascal_type", None)
                setattr(value, "pascal_type", self)

class pascal_unpacked_structured_type:

    pass
class pascal_constant_definition:

    def __init__(self, name: str, pascal_constant_definition: "pascal_constant_definition_part" = None, pascal_constant_definition108: "pascal_constant" = None):
        self.name = name
        self.pascal_constant_definition = pascal_constant_definition
        self.pascal_constant_definition108 = pascal_constant_definition108
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_constant_definition(self):
        return self.__pascal_constant_definition

    @pascal_constant_definition.setter
    def pascal_constant_definition(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant_definition__pascal_constant_definition", None)
        self.__pascal_constant_definition = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant_definition_part106"):
                opp_val = getattr(old_value, "pascal_constant_definition_part106", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant_definition_part106"):
                opp_val = getattr(value, "pascal_constant_definition_part106", None)
                if opp_val is None:
                    setattr(value, "pascal_constant_definition_part106", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_constant_definition108(self):
        return self.__pascal_constant_definition108

    @pascal_constant_definition108.setter
    def pascal_constant_definition108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant_definition__pascal_constant_definition108", None)
        self.__pascal_constant_definition108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant109"):
                opp_val = getattr(old_value, "pascal_constant109", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant109", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant109"):
                opp_val = getattr(value, "pascal_constant109", None)
                setattr(value, "pascal_constant109", self)

class pascal_structured_type:

    pass
class pascal_simple_type:

    def __init__(self, name: str, pascal_simple_type: "pascal_type" = None):
        self.name = name
        self.pascal_simple_type = pascal_simple_type
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "pascal_type115"):
                opp_val = getattr(old_value, "pascal_type115", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type115"):
                opp_val = getattr(value, "pascal_type115", None)
                setattr(value, "pascal_type115", self)

class pascal_any_number:

    def __init__(self, integer: str, real: str, pascal_any_number: "pascal_number" = None):
        self.integer = integer
        self.real = real
        self.pascal_any_number = pascal_any_number
        
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
    def pascal_any_number(self):
        return self.__pascal_any_number

    @pascal_any_number.setter
    def pascal_any_number(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_any_number__pascal_any_number", None)
        self.__pascal_any_number = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_number99"):
                opp_val = getattr(old_value, "pascal_number99", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number99"):
                opp_val = getattr(value, "pascal_number99", None)
                setattr(value, "pascal_number99", self)

class pascal_parameter_type:

    def __init__(self, name: str, pascal_parameter_type: "pascal_value_parameter_section" = None, pascal_parameter_type97: "pascal_variable_parameter_section" = None):
        self.name = name
        self.pascal_parameter_type = pascal_parameter_type
        self.pascal_parameter_type97 = pascal_parameter_type97
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "pascal_value_parameter_section91"):
                opp_val = getattr(old_value, "pascal_value_parameter_section91", None)
                if opp_val == self:
                    setattr(old_value, "pascal_value_parameter_section91", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_value_parameter_section91"):
                opp_val = getattr(value, "pascal_value_parameter_section91", None)
                setattr(value, "pascal_value_parameter_section91", self)

    @property
    def pascal_parameter_type97(self):
        return self.__pascal_parameter_type97

    @pascal_parameter_type97.setter
    def pascal_parameter_type97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type97", None)
        self.__pascal_parameter_type97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_parameter_section96"):
                opp_val = getattr(old_value, "pascal_variable_parameter_section96", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_parameter_section96", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_parameter_section96"):
                opp_val = getattr(value, "pascal_variable_parameter_section96", None)
                setattr(value, "pascal_variable_parameter_section96", self)

class pascal_identifier_list:

    def __init__(self, names: str, pascal_identifier_list: "pascal_value_parameter_section" = None, pascal_identifier_list94: "pascal_variable_parameter_section" = None, pascal_identifier_list128: "pascal_record_section" = None):
        self.names = names
        self.pascal_identifier_list = pascal_identifier_list
        self.pascal_identifier_list94 = pascal_identifier_list94
        self.pascal_identifier_list128 = pascal_identifier_list128
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

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
            if hasattr(old_value, "pascal_value_parameter_section89"):
                opp_val = getattr(old_value, "pascal_value_parameter_section89", None)
                if opp_val == self:
                    setattr(old_value, "pascal_value_parameter_section89", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_value_parameter_section89"):
                opp_val = getattr(value, "pascal_value_parameter_section89", None)
                setattr(value, "pascal_value_parameter_section89", self)

    @property
    def pascal_identifier_list94(self):
        return self.__pascal_identifier_list94

    @pascal_identifier_list94.setter
    def pascal_identifier_list94(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list94", None)
        self.__pascal_identifier_list94 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_parameter_section93"):
                opp_val = getattr(old_value, "pascal_variable_parameter_section93", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_parameter_section93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_parameter_section93"):
                opp_val = getattr(value, "pascal_variable_parameter_section93", None)
                setattr(value, "pascal_variable_parameter_section93", self)

    @property
    def pascal_identifier_list128(self):
        return self.__pascal_identifier_list128

    @pascal_identifier_list128.setter
    def pascal_identifier_list128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list128", None)
        self.__pascal_identifier_list128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_record_section127"):
                opp_val = getattr(old_value, "pascal_record_section127", None)
                if opp_val == self:
                    setattr(old_value, "pascal_record_section127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_record_section127"):
                opp_val = getattr(value, "pascal_record_section127", None)
                setattr(value, "pascal_record_section127", self)

class pascal_constant:

    def __init__(self, opterator: str, name: str, string: str, boolLiteral: str, nil: bool, pascal_constant: "pascal_number" = None, pascal_constant109: "pascal_constant_definition" = None):
        self.opterator = opterator
        self.name = name
        self.string = string
        self.boolLiteral = boolLiteral
        self.nil = nil
        self.pascal_constant = pascal_constant
        self.pascal_constant109 = pascal_constant109
        
    @property
    def boolLiteral(self) -> str:
        return self.__boolLiteral

    @boolLiteral.setter
    def boolLiteral(self, boolLiteral: str):
        self.__boolLiteral = boolLiteral

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def nil(self) -> bool:
        return self.__nil

    @nil.setter
    def nil(self, nil: bool):
        self.__nil = nil

    @property
    def opterator(self) -> str:
        return self.__opterator

    @opterator.setter
    def opterator(self, opterator: str):
        self.__opterator = opterator

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
            if hasattr(old_value, "pascal_number104"):
                opp_val = getattr(old_value, "pascal_number104", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number104", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number104"):
                opp_val = getattr(value, "pascal_number104", None)
                setattr(value, "pascal_number104", self)

    @property
    def pascal_constant109(self):
        return self.__pascal_constant109

    @pascal_constant109.setter
    def pascal_constant109(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant109", None)
        self.__pascal_constant109 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant_definition108"):
                opp_val = getattr(old_value, "pascal_constant_definition108", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant_definition108", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant_definition108"):
                opp_val = getattr(value, "pascal_constant_definition108", None)
                setattr(value, "pascal_constant_definition108", self)

class pascal_formal_parameter_list:

    pass
class pascal_abstraction_heading:

    def __init__(self, returnType: str, name: str, pascal_abstraction_heading: "pascal_formal_parameter_list" = None, pascal_abstraction_heading72: "pascal_abstraction_declaration" = None, pascal_abstraction_heading84: "pascal_formal_parameter_section" = None, pascal_abstraction_heading87: "pascal_formal_parameter_section" = None):
        self.returnType = returnType
        self.name = name
        self.pascal_abstraction_heading = pascal_abstraction_heading
        self.pascal_abstraction_heading72 = pascal_abstraction_heading72
        self.pascal_abstraction_heading84 = pascal_abstraction_heading84
        self.pascal_abstraction_heading87 = pascal_abstraction_heading87
        
    @property
    def returnType(self) -> str:
        return self.__returnType

    @returnType.setter
    def returnType(self, returnType: str):
        self.__returnType = returnType

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_abstraction_heading72(self):
        return self.__pascal_abstraction_heading72

    @pascal_abstraction_heading72.setter
    def pascal_abstraction_heading72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading72", None)
        self.__pascal_abstraction_heading72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_abstraction_declaration71"):
                opp_val = getattr(old_value, "pascal_abstraction_declaration71", None)
                if opp_val == self:
                    setattr(old_value, "pascal_abstraction_declaration71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_abstraction_declaration71"):
                opp_val = getattr(value, "pascal_abstraction_declaration71", None)
                setattr(value, "pascal_abstraction_declaration71", self)

    @property
    def pascal_abstraction_heading(self):
        return self.__pascal_abstraction_heading

    @pascal_abstraction_heading.setter
    def pascal_abstraction_heading(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading", None)
        self.__pascal_abstraction_heading = value
        
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
    def pascal_abstraction_heading84(self):
        return self.__pascal_abstraction_heading84

    @pascal_abstraction_heading84.setter
    def pascal_abstraction_heading84(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading84", None)
        self.__pascal_abstraction_heading84 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_section83"):
                opp_val = getattr(old_value, "pascal_formal_parameter_section83", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_section83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_section83"):
                opp_val = getattr(value, "pascal_formal_parameter_section83", None)
                setattr(value, "pascal_formal_parameter_section83", self)

    @property
    def pascal_abstraction_heading87(self):
        return self.__pascal_abstraction_heading87

    @pascal_abstraction_heading87.setter
    def pascal_abstraction_heading87(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading87", None)
        self.__pascal_abstraction_heading87 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_section86"):
                opp_val = getattr(old_value, "pascal_formal_parameter_section86", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_section86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_section86"):
                opp_val = getattr(value, "pascal_formal_parameter_section86", None)
                setattr(value, "pascal_formal_parameter_section86", self)

class pascal_abstraction_declaration:

    pass
class pascal_number:

    pass
class pascal_variable_parameter_section:

    pass
class pascal_value_parameter_section:

    pass
class pascal_formal_parameter_section:

    pass
class pascal_expression:

    def __init__(self, operators: str, pascal_expression41: "pascal_expression_list" = None, pascal_expression43: set["pascal_simple_expression"] = None, pascal_expression: "pascal_assignment_statement" = None, pascal_expression57: "pascal_factor" = None, pascal_expression141: "pascal_while_statement" = None):
        self.operators = operators
        self.pascal_expression41 = pascal_expression41
        self.pascal_expression43 = pascal_expression43 if pascal_expression43 is not None else set()
        self.pascal_expression = pascal_expression
        self.pascal_expression57 = pascal_expression57
        self.pascal_expression141 = pascal_expression141
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def pascal_expression41(self):
        return self.__pascal_expression41

    @pascal_expression41.setter
    def pascal_expression41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression41", None)
        self.__pascal_expression41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list"):
                opp_val = getattr(old_value, "pascal_expression_list", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list"):
                opp_val = getattr(value, "pascal_expression_list", None)
                if opp_val is None:
                    setattr(value, "pascal_expression_list", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_expression57(self):
        return self.__pascal_expression57

    @pascal_expression57.setter
    def pascal_expression57(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression57", None)
        self.__pascal_expression57 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor56"):
                opp_val = getattr(old_value, "pascal_factor56", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor56", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor56"):
                opp_val = getattr(value, "pascal_factor56", None)
                setattr(value, "pascal_factor56", self)

    @property
    def pascal_expression141(self):
        return self.__pascal_expression141

    @pascal_expression141.setter
    def pascal_expression141(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression141", None)
        self.__pascal_expression141 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_while_statement140"):
                opp_val = getattr(old_value, "pascal_while_statement140", None)
                if opp_val == self:
                    setattr(old_value, "pascal_while_statement140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_while_statement140"):
                opp_val = getattr(value, "pascal_while_statement140", None)
                setattr(value, "pascal_while_statement140", self)

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
            if hasattr(old_value, "pascal_assignment_statement39"):
                opp_val = getattr(old_value, "pascal_assignment_statement39", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement39"):
                opp_val = getattr(value, "pascal_assignment_statement39", None)
                setattr(value, "pascal_assignment_statement39", self)

    @property
    def pascal_expression43(self):
        return self.__pascal_expression43

    @pascal_expression43.setter
    def pascal_expression43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression43", None)
        self.__pascal_expression43 = value if value is not None else set()
        
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
                    

class pascal_variable:

    def __init__(self, name: str, pascal_variable49: "pascal_factor" = None, pascal_variable: "pascal_assignment_statement" = None):
        self.name = name
        self.pascal_variable49 = pascal_variable49
        self.pascal_variable = pascal_variable
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_variable49(self):
        return self.__pascal_variable49

    @pascal_variable49.setter
    def pascal_variable49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable49", None)
        self.__pascal_variable49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor48"):
                opp_val = getattr(old_value, "pascal_factor48", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor48"):
                opp_val = getattr(value, "pascal_factor48", None)
                setattr(value, "pascal_factor48", self)

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
            if hasattr(old_value, "pascal_assignment_statement37"):
                opp_val = getattr(old_value, "pascal_assignment_statement37", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement37"):
                opp_val = getattr(value, "pascal_assignment_statement37", None)
                setattr(value, "pascal_assignment_statement37", self)

class pascal_while_statement:

    pass
class pascal_compound_statement:

    pass
class pascal_factor:

    def __init__(self, string: str, boolean: str, nil: bool, pascal_factor: "pascal_term" = None, pascal_factor48: "pascal_variable" = None, pascal_factor51: "pascal_number" = None, pascal_factor53: "pascal_function_designator" = None, pascal_factor56: "pascal_expression" = None, pascal_factor60: "pascal_factor" = None, pascal_factor58: "pascal_factor" = None):
        self.string = string
        self.boolean = boolean
        self.nil = nil
        self.pascal_factor = pascal_factor
        self.pascal_factor48 = pascal_factor48
        self.pascal_factor51 = pascal_factor51
        self.pascal_factor53 = pascal_factor53
        self.pascal_factor56 = pascal_factor56
        self.pascal_factor60 = pascal_factor60
        self.pascal_factor58 = pascal_factor58
        
    @property
    def nil(self) -> bool:
        return self.__nil

    @nil.setter
    def nil(self, nil: bool):
        self.__nil = nil

    @property
    def boolean(self) -> str:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: str):
        self.__boolean = boolean

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def pascal_factor56(self):
        return self.__pascal_factor56

    @pascal_factor56.setter
    def pascal_factor56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor56", None)
        self.__pascal_factor56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression57"):
                opp_val = getattr(old_value, "pascal_expression57", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression57"):
                opp_val = getattr(value, "pascal_expression57", None)
                setattr(value, "pascal_expression57", self)

    @property
    def pascal_factor51(self):
        return self.__pascal_factor51

    @pascal_factor51.setter
    def pascal_factor51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor51", None)
        self.__pascal_factor51 = value
        
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
    def pascal_factor53(self):
        return self.__pascal_factor53

    @pascal_factor53.setter
    def pascal_factor53(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor53", None)
        self.__pascal_factor53 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_designator54"):
                opp_val = getattr(old_value, "pascal_function_designator54", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_designator54", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_designator54"):
                opp_val = getattr(value, "pascal_function_designator54", None)
                setattr(value, "pascal_function_designator54", self)

    @property
    def pascal_factor48(self):
        return self.__pascal_factor48

    @pascal_factor48.setter
    def pascal_factor48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor48", None)
        self.__pascal_factor48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable49"):
                opp_val = getattr(old_value, "pascal_variable49", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable49"):
                opp_val = getattr(value, "pascal_variable49", None)
                setattr(value, "pascal_variable49", self)

    @property
    def pascal_factor58(self):
        return self.__pascal_factor58

    @pascal_factor58.setter
    def pascal_factor58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor58", None)
        self.__pascal_factor58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor60"):
                opp_val = getattr(old_value, "pascal_factor60", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor60", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor60"):
                opp_val = getattr(value, "pascal_factor60", None)
                setattr(value, "pascal_factor60", self)

    @property
    def pascal_factor60(self):
        return self.__pascal_factor60

    @pascal_factor60.setter
    def pascal_factor60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor60", None)
        self.__pascal_factor60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor58"):
                opp_val = getattr(old_value, "pascal_factor58", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor58"):
                opp_val = getattr(value, "pascal_factor58", None)
                setattr(value, "pascal_factor58", self)

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
            if hasattr(old_value, "pascal_term"):
                opp_val = getattr(old_value, "pascal_term", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_term"):
                opp_val = getattr(value, "pascal_term", None)
                if opp_val is None:
                    setattr(value, "pascal_term", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_term:

    def __init__(self, operators: str, pascal_term: set["pascal_factor"] = None):
        self.operators = operators
        self.pascal_term = pascal_term if pascal_term is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def pascal_term(self):
        return self.__pascal_term

    @pascal_term.setter
    def pascal_term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_term__pascal_term", None)
        self.__pascal_term = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_factor"):
                    opp_val = getattr(item, "pascal_factor", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_factor", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_factor"):
                    opp_val = getattr(item, "pascal_factor", None)
                    
                    setattr(item, "pascal_factor", self)
                    

class pascal_EObject:

    pass
class pascal_simple_expression:

    def __init__(self, prefixOperator: str, operators: str, pascal_simple_expression: "pascal_expression" = None, pascal_simple_expression45: set["pascal_EObject"] = None):
        self.prefixOperator = prefixOperator
        self.operators = operators
        self.pascal_simple_expression = pascal_simple_expression
        self.pascal_simple_expression45 = pascal_simple_expression45 if pascal_simple_expression45 is not None else set()
        
    @property
    def prefixOperator(self) -> str:
        return self.__prefixOperator

    @prefixOperator.setter
    def prefixOperator(self, prefixOperator: str):
        self.__prefixOperator = prefixOperator

    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def pascal_simple_expression45(self):
        return self.__pascal_simple_expression45

    @pascal_simple_expression45.setter
    def pascal_simple_expression45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_expression__pascal_simple_expression45", None)
        self.__pascal_simple_expression45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_EObject"):
                    opp_val = getattr(item, "pascal_EObject", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_EObject", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_EObject"):
                    opp_val = getattr(item, "pascal_EObject", None)
                    
                    setattr(item, "pascal_EObject", self)
                    

    @property
    def pascal_simple_expression(self):
        return self.__pascal_simple_expression

    @pascal_simple_expression.setter
    def pascal_simple_expression(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_expression__pascal_simple_expression", None)
        self.__pascal_simple_expression = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression43"):
                opp_val = getattr(old_value, "pascal_expression43", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression43"):
                opp_val = getattr(value, "pascal_expression43", None)
                if opp_val is None:
                    setattr(value, "pascal_expression43", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_expression_list:

    pass
class pascal_statement:

    pass
class pascal_statement_sequence:

    pass
class pascal_statement_part:

    pass
class pascal_function_procedure_declaration:

    pass
class pascal_constant_definition_part:

    pass
class pascal_function_designator:

    def __init__(self, name: str, pascal_function_designator: "pascal_simple_statement" = None, pascal_function_designator54: "pascal_factor" = None, pascal_function_designator62: "pascal_expression_list" = None):
        self.name = name
        self.pascal_function_designator = pascal_function_designator
        self.pascal_function_designator54 = pascal_function_designator54
        self.pascal_function_designator62 = pascal_function_designator62
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_function_designator62(self):
        return self.__pascal_function_designator62

    @pascal_function_designator62.setter
    def pascal_function_designator62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator62", None)
        self.__pascal_function_designator62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list63"):
                opp_val = getattr(old_value, "pascal_expression_list63", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression_list63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list63"):
                opp_val = getattr(value, "pascal_expression_list63", None)
                setattr(value, "pascal_expression_list63", self)

    @property
    def pascal_function_designator54(self):
        return self.__pascal_function_designator54

    @pascal_function_designator54.setter
    def pascal_function_designator54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator54", None)
        self.__pascal_function_designator54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor53"):
                opp_val = getattr(old_value, "pascal_factor53", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor53", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor53"):
                opp_val = getattr(value, "pascal_factor53", None)
                setattr(value, "pascal_factor53", self)

    @property
    def pascal_function_designator(self):
        return self.__pascal_function_designator

    @pascal_function_designator.setter
    def pascal_function_designator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator", None)
        self.__pascal_function_designator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simple_statement28"):
                opp_val = getattr(old_value, "pascal_simple_statement28", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simple_statement28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_statement28"):
                opp_val = getattr(value, "pascal_simple_statement28", None)
                setattr(value, "pascal_simple_statement28", self)

class pascal_assignment_statement:

    pass
class pascal_structured_statement:

    pass
class pascal_simple_statement:

    def __init__(self, function_noargs: str, pascal_simple_statement: "pascal_statement" = None, pascal_simple_statement26: "pascal_assignment_statement" = None, pascal_simple_statement28: "pascal_function_designator" = None):
        self.function_noargs = function_noargs
        self.pascal_simple_statement = pascal_simple_statement
        self.pascal_simple_statement26 = pascal_simple_statement26
        self.pascal_simple_statement28 = pascal_simple_statement28
        
    @property
    def function_noargs(self) -> str:
        return self.__function_noargs

    @function_noargs.setter
    def function_noargs(self, function_noargs: str):
        self.__function_noargs = function_noargs

    @property
    def pascal_simple_statement(self):
        return self.__pascal_simple_statement

    @pascal_simple_statement.setter
    def pascal_simple_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement", None)
        self.__pascal_simple_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_statement22"):
                opp_val = getattr(old_value, "pascal_statement22", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement22"):
                opp_val = getattr(value, "pascal_statement22", None)
                setattr(value, "pascal_statement22", self)

    @property
    def pascal_simple_statement26(self):
        return self.__pascal_simple_statement26

    @pascal_simple_statement26.setter
    def pascal_simple_statement26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement26", None)
        self.__pascal_simple_statement26 = value
        
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
    def pascal_simple_statement28(self):
        return self.__pascal_simple_statement28

    @pascal_simple_statement28.setter
    def pascal_simple_statement28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement28", None)
        self.__pascal_simple_statement28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_designator"):
                opp_val = getattr(old_value, "pascal_function_designator", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_designator", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_designator"):
                opp_val = getattr(value, "pascal_function_designator", None)
                setattr(value, "pascal_function_designator", self)

class pascal_label:

    def __init__(self, number: str, pascal_label: "pascal_statement" = None, pascal_label102: "pascal_label_declaration" = None):
        self.number = number
        self.pascal_label = pascal_label
        self.pascal_label102 = pascal_label102
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

    @property
    def pascal_label102(self):
        return self.__pascal_label102

    @pascal_label102.setter
    def pascal_label102(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_label__pascal_label102", None)
        self.__pascal_label102 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_label_declaration101"):
                opp_val = getattr(old_value, "pascal_label_declaration101", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_label_declaration101"):
                opp_val = getattr(value, "pascal_label_declaration101", None)
                if opp_val is None:
                    setattr(value, "pascal_label_declaration101", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "pascal_statement20"):
                opp_val = getattr(old_value, "pascal_statement20", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement20"):
                opp_val = getattr(value, "pascal_statement20", None)
                setattr(value, "pascal_statement20", self)

class pascal_program_heading_block:

    def __init__(self, name: str, pascal_program_heading_block: "pascal_program" = None):
        self.name = name
        self.pascal_program_heading_block = pascal_program_heading_block
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_program_heading_block(self):
        return self.__pascal_program_heading_block

    @pascal_program_heading_block.setter
    def pascal_program_heading_block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_program_heading_block__pascal_program_heading_block", None)
        self.__pascal_program_heading_block = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_program"):
                opp_val = getattr(old_value, "pascal_program", None)
                if opp_val == self:
                    setattr(old_value, "pascal_program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_program"):
                opp_val = getattr(value, "pascal_program", None)
                setattr(value, "pascal_program", self)

class pascal_program:

    pass
class pascal_variable_declaration_part:

    pass
class pascal_type_definition_part:

    pass
class pascal_label_declaration:

    pass
class pascal_block:

    pass