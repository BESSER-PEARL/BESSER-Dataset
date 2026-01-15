from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class output_list:

    pass
class pascal_output_value(output_list):

    pass
class pascal_output_list:

    pass
class pascal_ordinal_type_identifier:

    pass
class pascal_bound_specification:

    pass
class pascal_unpacked_conformant_array_schema:

    pass
class pascal_packed_conformant_array_schema:

    pass
class pascal_conformant_array_schema:

    pass
class pascal_parameter_type:

    pass
class pascal_result_type:

    pass
class pascal_function_parameter_section:

    pass
class pascal_procedure_parameter_section:

    pass
class pascal_variable_parameter_section:

    pass
class pascal_value_parameter_section:

    pass
class pascal_formal_parameter_section:

    pass
class pascal_formal_parameter_list:

    pass
class pascal_compiler_defined_directives:

    pass
class pascal_variable_declaration:

    pass
class pascal_upper_bound:

    pass
class pascal_lower_bound:

    pass
class pascal_enumerated_type:

    pass
class pascal_subrange_type:

    pass
class pascal_element_type:

    pass
class pascal_index_type:

    pass
class pascal_variant:

    pass
class pascal_tag_field:

    pass
class pascal_record_section:

    pass
class pascal_fixed_part:

    pass
class pascal_variant_part:

    pass
class pascal_field_list:

    pass
class pascal_base_type:

    pass
class pascal_file_component_type:

    pass
class pascal_file_type:

    pass
class pascal_set_type:

    pass
class pascal_record_type:

    pass
class pascal_array_type:

    pass
class pascal_unpacked_structured_type:

    pass
class pascal_type_identifier:

    pass
class pascal_pointer_type:

    pass
class pascal_structured_type:

    pass
class pascal_simple_type:

    pass
class pascal_type:

    pass
class pascal_type_definition:

    pass
class pascal_constant_definition:

    pass
class pascal_function_identification:

    pass
class pascal_function_body:

    pass
class pascal_function_heading:

    pass
class pascal_procedure_identification:

    pass
class pascal_directive:

    pass
class pascal_procedure_body:

    pass
class pascal_procedure_heading:

    pass
class pascal_variable_declaration_part:

    pass
class pascal_type_definition_part:

    pass
class pascal_label_declaration_part:

    pass
class pascal_constant_definition_part:

    pass
class pascal_final_expression:

    pass
class pascal_initial_expression:

    pass
class pascal_for_statement:

    pass
class pascal_repeat_statement:

    pass
class pascal_while_statement:

    pass
class pascal_constant:

    def __init__(self, sign: str, strings: str, boolean: str, pascal_constant: "pascal_case_label_list" = None, pascal_constant251: "pascal_constant_definition" = None, pascal_constant253: "pascal_identifier" = None, pascal_constant256: "pascal_number" = None, pascal_constant352: "pascal_lower_bound" = None, pascal_constant355: "pascal_upper_bound" = None):
        self.sign = sign
        self.strings = strings
        self.boolean = boolean
        self.pascal_constant = pascal_constant
        self.pascal_constant251 = pascal_constant251
        self.pascal_constant253 = pascal_constant253
        self.pascal_constant256 = pascal_constant256
        self.pascal_constant352 = pascal_constant352
        self.pascal_constant355 = pascal_constant355
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def strings(self) -> str:
        return self.__strings

    @strings.setter
    def strings(self, strings: str):
        self.__strings = strings

    @property
    def boolean(self) -> str:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: str):
        self.__boolean = boolean

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
            if hasattr(old_value, "pascal_case_label_list175"):
                opp_val = getattr(old_value, "pascal_case_label_list175", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_label_list175"):
                opp_val = getattr(value, "pascal_case_label_list175", None)
                if opp_val is None:
                    setattr(value, "pascal_case_label_list175", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_constant355(self):
        return self.__pascal_constant355

    @pascal_constant355.setter
    def pascal_constant355(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant355", None)
        self.__pascal_constant355 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_upper_bound354"):
                opp_val = getattr(old_value, "pascal_upper_bound354", None)
                if opp_val == self:
                    setattr(old_value, "pascal_upper_bound354", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_upper_bound354"):
                opp_val = getattr(value, "pascal_upper_bound354", None)
                setattr(value, "pascal_upper_bound354", self)

    @property
    def pascal_constant251(self):
        return self.__pascal_constant251

    @pascal_constant251.setter
    def pascal_constant251(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant251", None)
        self.__pascal_constant251 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant_definition250"):
                opp_val = getattr(old_value, "pascal_constant_definition250", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant_definition250", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant_definition250"):
                opp_val = getattr(value, "pascal_constant_definition250", None)
                setattr(value, "pascal_constant_definition250", self)

    @property
    def pascal_constant256(self):
        return self.__pascal_constant256

    @pascal_constant256.setter
    def pascal_constant256(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant256", None)
        self.__pascal_constant256 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_number257"):
                opp_val = getattr(old_value, "pascal_number257", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number257", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number257"):
                opp_val = getattr(value, "pascal_number257", None)
                setattr(value, "pascal_number257", self)

    @property
    def pascal_constant253(self):
        return self.__pascal_constant253

    @pascal_constant253.setter
    def pascal_constant253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant253", None)
        self.__pascal_constant253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_identifier254"):
                opp_val = getattr(old_value, "pascal_identifier254", None)
                if opp_val == self:
                    setattr(old_value, "pascal_identifier254", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_identifier254"):
                opp_val = getattr(value, "pascal_identifier254", None)
                setattr(value, "pascal_identifier254", self)

    @property
    def pascal_constant352(self):
        return self.__pascal_constant352

    @pascal_constant352.setter
    def pascal_constant352(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant352", None)
        self.__pascal_constant352 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_lower_bound351"):
                opp_val = getattr(old_value, "pascal_lower_bound351", None)
                if opp_val == self:
                    setattr(old_value, "pascal_lower_bound351", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_lower_bound351"):
                opp_val = getattr(value, "pascal_lower_bound351", None)
                setattr(value, "pascal_lower_bound351", self)

class pascal_case_label_list:

    pass
class pascal_case_limb:

    pass
class pascal_case_statement:

    pass
class pascal_if_statement:

    pass
class pascal_with_statement:

    pass
class pascal_conditional_statement:

    pass
class pascal_compound_statement:

    pass
class pascal_scale_factor:

    def __init__(self, sign: str, pascal_scale_factor125: "pascal_digit_sequence" = None, pascal_scale_factor: "pascal_real_number" = None):
        self.sign = sign
        self.pascal_scale_factor125 = pascal_scale_factor125
        self.pascal_scale_factor = pascal_scale_factor
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def pascal_scale_factor(self):
        return self.__pascal_scale_factor

    @pascal_scale_factor.setter
    def pascal_scale_factor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_scale_factor__pascal_scale_factor", None)
        self.__pascal_scale_factor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_real_number123"):
                opp_val = getattr(old_value, "pascal_real_number123", None)
                if opp_val == self:
                    setattr(old_value, "pascal_real_number123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_real_number123"):
                opp_val = getattr(value, "pascal_real_number123", None)
                setattr(value, "pascal_real_number123", self)

    @property
    def pascal_scale_factor125(self):
        return self.__pascal_scale_factor125

    @pascal_scale_factor125.setter
    def pascal_scale_factor125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_scale_factor__pascal_scale_factor125", None)
        self.__pascal_scale_factor125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_digit_sequence126"):
                opp_val = getattr(old_value, "pascal_digit_sequence126", None)
                if opp_val == self:
                    setattr(old_value, "pascal_digit_sequence126", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_digit_sequence126"):
                opp_val = getattr(value, "pascal_digit_sequence126", None)
                setattr(value, "pascal_digit_sequence126", self)

class pascal_expression_list:

    pass
class pascal_entire_variable:

    pass
class pascal_digit_sequence:

    def __init__(self, sign: str, unsigned_digit_sequence: str, pascal_digit_sequence: "pascal_real_number" = None, pascal_digit_sequence121: "pascal_real_number" = None, pascal_digit_sequence145: "pascal_integer_number" = None, pascal_digit_sequence126: "pascal_scale_factor" = None):
        self.sign = sign
        self.unsigned_digit_sequence = unsigned_digit_sequence
        self.pascal_digit_sequence = pascal_digit_sequence
        self.pascal_digit_sequence121 = pascal_digit_sequence121
        self.pascal_digit_sequence145 = pascal_digit_sequence145
        self.pascal_digit_sequence126 = pascal_digit_sequence126
        
    @property
    def unsigned_digit_sequence(self) -> str:
        return self.__unsigned_digit_sequence

    @unsigned_digit_sequence.setter
    def unsigned_digit_sequence(self, unsigned_digit_sequence: str):
        self.__unsigned_digit_sequence = unsigned_digit_sequence

    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def pascal_digit_sequence(self):
        return self.__pascal_digit_sequence

    @pascal_digit_sequence.setter
    def pascal_digit_sequence(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_digit_sequence__pascal_digit_sequence", None)
        self.__pascal_digit_sequence = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_real_number118"):
                opp_val = getattr(old_value, "pascal_real_number118", None)
                if opp_val == self:
                    setattr(old_value, "pascal_real_number118", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_real_number118"):
                opp_val = getattr(value, "pascal_real_number118", None)
                setattr(value, "pascal_real_number118", self)

    @property
    def pascal_digit_sequence121(self):
        return self.__pascal_digit_sequence121

    @pascal_digit_sequence121.setter
    def pascal_digit_sequence121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_digit_sequence__pascal_digit_sequence121", None)
        self.__pascal_digit_sequence121 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_real_number120"):
                opp_val = getattr(old_value, "pascal_real_number120", None)
                if opp_val == self:
                    setattr(old_value, "pascal_real_number120", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_real_number120"):
                opp_val = getattr(value, "pascal_real_number120", None)
                setattr(value, "pascal_real_number120", self)

    @property
    def pascal_digit_sequence145(self):
        return self.__pascal_digit_sequence145

    @pascal_digit_sequence145.setter
    def pascal_digit_sequence145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_digit_sequence__pascal_digit_sequence145", None)
        self.__pascal_digit_sequence145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_integer_number144"):
                opp_val = getattr(old_value, "pascal_integer_number144", None)
                if opp_val == self:
                    setattr(old_value, "pascal_integer_number144", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_integer_number144"):
                opp_val = getattr(value, "pascal_integer_number144", None)
                setattr(value, "pascal_integer_number144", self)

    @property
    def pascal_digit_sequence126(self):
        return self.__pascal_digit_sequence126

    @pascal_digit_sequence126.setter
    def pascal_digit_sequence126(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_digit_sequence__pascal_digit_sequence126", None)
        self.__pascal_digit_sequence126 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_scale_factor125"):
                opp_val = getattr(old_value, "pascal_scale_factor125", None)
                if opp_val == self:
                    setattr(old_value, "pascal_scale_factor125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_scale_factor125"):
                opp_val = getattr(value, "pascal_scale_factor125", None)
                setattr(value, "pascal_scale_factor125", self)

class pascal_repetitive_statement:

    pass
class pascal_real_number:

    pass
class pascal_integer_number:

    pass
class pascal_function_designator:

    pass
class pascal_set:

    pass
class pascal_number:

    pass
class pascal_element_list:

    pass
class pascal_addition_operator:

    def __init__(self, sign: str, pascal_addition_operator: "pascal_simple_expression" = None):
        self.sign = sign
        self.pascal_addition_operator = pascal_addition_operator
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

    @property
    def pascal_addition_operator(self):
        return self.__pascal_addition_operator

    @pascal_addition_operator.setter
    def pascal_addition_operator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_addition_operator__pascal_addition_operator", None)
        self.__pascal_addition_operator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simple_expression81"):
                opp_val = getattr(old_value, "pascal_simple_expression81", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_expression81"):
                opp_val = getattr(value, "pascal_simple_expression81", None)
                if opp_val is None:
                    setattr(value, "pascal_simple_expression81", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_term:

    def __init__(self, multiplication_operator: str, pascal_term83: set["pascal_factor"] = None, pascal_term: "pascal_simple_expression" = None):
        self.multiplication_operator = multiplication_operator
        self.pascal_term83 = pascal_term83 if pascal_term83 is not None else set()
        self.pascal_term = pascal_term
        
    @property
    def multiplication_operator(self) -> str:
        return self.__multiplication_operator

    @multiplication_operator.setter
    def multiplication_operator(self, multiplication_operator: str):
        self.__multiplication_operator = multiplication_operator

    @property
    def pascal_term83(self):
        return self.__pascal_term83

    @pascal_term83.setter
    def pascal_term83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_term__pascal_term83", None)
        self.__pascal_term83 = value if value is not None else set()
        
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
                    

    @property
    def pascal_term(self):
        return self.__pascal_term

    @pascal_term.setter
    def pascal_term(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_term__pascal_term", None)
        self.__pascal_term = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simple_expression79"):
                opp_val = getattr(old_value, "pascal_simple_expression79", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_expression79"):
                opp_val = getattr(value, "pascal_simple_expression79", None)
                if opp_val is None:
                    setattr(value, "pascal_simple_expression79", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_simple_expression:

    def __init__(self, sign: str, pascal_simple_expression: "pascal_expression" = None, pascal_simple_expression79: set["pascal_term"] = None, pascal_simple_expression81: set["pascal_addition_operator"] = None):
        self.sign = sign
        self.pascal_simple_expression = pascal_simple_expression
        self.pascal_simple_expression79 = pascal_simple_expression79 if pascal_simple_expression79 is not None else set()
        self.pascal_simple_expression81 = pascal_simple_expression81 if pascal_simple_expression81 is not None else set()
        
    @property
    def sign(self) -> str:
        return self.__sign

    @sign.setter
    def sign(self, sign: str):
        self.__sign = sign

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
            if hasattr(old_value, "pascal_expression74"):
                opp_val = getattr(old_value, "pascal_expression74", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression74"):
                opp_val = getattr(value, "pascal_expression74", None)
                if opp_val is None:
                    setattr(value, "pascal_expression74", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_simple_expression81(self):
        return self.__pascal_simple_expression81

    @pascal_simple_expression81.setter
    def pascal_simple_expression81(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_expression__pascal_simple_expression81", None)
        self.__pascal_simple_expression81 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_addition_operator"):
                    opp_val = getattr(item, "pascal_addition_operator", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_addition_operator", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_addition_operator"):
                    opp_val = getattr(item, "pascal_addition_operator", None)
                    
                    setattr(item, "pascal_addition_operator", self)
                    

    @property
    def pascal_simple_expression79(self):
        return self.__pascal_simple_expression79

    @pascal_simple_expression79.setter
    def pascal_simple_expression79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_expression__pascal_simple_expression79", None)
        self.__pascal_simple_expression79 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_term"):
                    opp_val = getattr(item, "pascal_term", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_term", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_term"):
                    opp_val = getattr(item, "pascal_term", None)
                    
                    setattr(item, "pascal_term", self)
                    

class output_value:

    pass
class pascal_factor:

    def __init__(self, strings: str, boolean: str, pascal_factor: "pascal_term" = None, pascal_factor85: "pascal_variable" = None, pascal_factor88: "pascal_number" = None, pascal_factor90: "pascal_set" = None, pascal_factor92: "pascal_identifier" = None, pascal_factor95: "pascal_function_designator" = None, pascal_factor97: "pascal_expression" = None, pascal_factor101: "pascal_factor" = None, pascal_factor99: "pascal_factor" = None):
        self.strings = strings
        self.boolean = boolean
        self.pascal_factor = pascal_factor
        self.pascal_factor85 = pascal_factor85
        self.pascal_factor88 = pascal_factor88
        self.pascal_factor90 = pascal_factor90
        self.pascal_factor92 = pascal_factor92
        self.pascal_factor95 = pascal_factor95
        self.pascal_factor97 = pascal_factor97
        self.pascal_factor101 = pascal_factor101
        self.pascal_factor99 = pascal_factor99
        
    @property
    def strings(self) -> str:
        return self.__strings

    @strings.setter
    def strings(self, strings: str):
        self.__strings = strings

    @property
    def boolean(self) -> str:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: str):
        self.__boolean = boolean

    @property
    def pascal_factor90(self):
        return self.__pascal_factor90

    @pascal_factor90.setter
    def pascal_factor90(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor90", None)
        self.__pascal_factor90 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_set"):
                opp_val = getattr(old_value, "pascal_set", None)
                if opp_val == self:
                    setattr(old_value, "pascal_set", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_set"):
                opp_val = getattr(value, "pascal_set", None)
                setattr(value, "pascal_set", self)

    @property
    def pascal_factor85(self):
        return self.__pascal_factor85

    @pascal_factor85.setter
    def pascal_factor85(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor85", None)
        self.__pascal_factor85 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable86"):
                opp_val = getattr(old_value, "pascal_variable86", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable86", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable86"):
                opp_val = getattr(value, "pascal_variable86", None)
                setattr(value, "pascal_variable86", self)

    @property
    def pascal_factor88(self):
        return self.__pascal_factor88

    @pascal_factor88.setter
    def pascal_factor88(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor88", None)
        self.__pascal_factor88 = value
        
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
    def pascal_factor97(self):
        return self.__pascal_factor97

    @pascal_factor97.setter
    def pascal_factor97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor97", None)
        self.__pascal_factor97 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression98"):
                opp_val = getattr(old_value, "pascal_expression98", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression98", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression98"):
                opp_val = getattr(value, "pascal_expression98", None)
                setattr(value, "pascal_expression98", self)

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
            if hasattr(old_value, "pascal_term83"):
                opp_val = getattr(old_value, "pascal_term83", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_term83"):
                opp_val = getattr(value, "pascal_term83", None)
                if opp_val is None:
                    setattr(value, "pascal_term83", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_factor101(self):
        return self.__pascal_factor101

    @pascal_factor101.setter
    def pascal_factor101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor101", None)
        self.__pascal_factor101 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor99"):
                opp_val = getattr(old_value, "pascal_factor99", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor99"):
                opp_val = getattr(value, "pascal_factor99", None)
                setattr(value, "pascal_factor99", self)

    @property
    def pascal_factor95(self):
        return self.__pascal_factor95

    @pascal_factor95.setter
    def pascal_factor95(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor95", None)
        self.__pascal_factor95 = value
        
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

    @property
    def pascal_factor92(self):
        return self.__pascal_factor92

    @pascal_factor92.setter
    def pascal_factor92(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor92", None)
        self.__pascal_factor92 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_identifier93"):
                opp_val = getattr(old_value, "pascal_identifier93", None)
                if opp_val == self:
                    setattr(old_value, "pascal_identifier93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_identifier93"):
                opp_val = getattr(value, "pascal_identifier93", None)
                setattr(value, "pascal_identifier93", self)

    @property
    def pascal_factor99(self):
        return self.__pascal_factor99

    @pascal_factor99.setter
    def pascal_factor99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor99", None)
        self.__pascal_factor99 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor101"):
                opp_val = getattr(old_value, "pascal_factor101", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor101", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor101"):
                opp_val = getattr(value, "pascal_factor101", None)
                setattr(value, "pascal_factor101", self)

class pascal_variable:

    pass
class pascal_actual_function:

    pass
class pascal_actual_procedure:

    pass
class pascal_actual_variable:

    pass
class pascal_actual_value:

    pass
class pascal_expression(output_value):

    def __init__(self, relational_operator: str, pascal_expression: "pascal_actual_value" = None, pascal_expression72: "pascal_assignment_statement" = None, pascal_expression74: set["pascal_simple_expression"] = None, pascal_expression77: "pascal_expression" = None, pascal_expression75: set["pascal_expression"] = None, pascal_expression98: "pascal_factor" = None, pascal_expression112: "pascal_element_list" = None, pascal_expression139: "pascal_expression_list" = None, pascal_expression166: "pascal_case_statement" = None, pascal_expression178: "pascal_if_statement" = None, pascal_expression200: "pascal_final_expression" = None, pascal_expression203: "pascal_initial_expression" = None, pascal_expression209: "pascal_repeat_statement" = None, pascal_expression212: "pascal_while_statement" = None):
        self.relational_operator = relational_operator
        self.pascal_expression = pascal_expression
        self.pascal_expression72 = pascal_expression72
        self.pascal_expression74 = pascal_expression74 if pascal_expression74 is not None else set()
        self.pascal_expression77 = pascal_expression77
        self.pascal_expression75 = pascal_expression75 if pascal_expression75 is not None else set()
        self.pascal_expression98 = pascal_expression98
        self.pascal_expression112 = pascal_expression112
        self.pascal_expression139 = pascal_expression139
        self.pascal_expression166 = pascal_expression166
        self.pascal_expression178 = pascal_expression178
        self.pascal_expression200 = pascal_expression200
        self.pascal_expression203 = pascal_expression203
        self.pascal_expression209 = pascal_expression209
        self.pascal_expression212 = pascal_expression212
        
    @property
    def relational_operator(self) -> str:
        return self.__relational_operator

    @relational_operator.setter
    def relational_operator(self, relational_operator: str):
        self.__relational_operator = relational_operator

    @property
    def pascal_expression200(self):
        return self.__pascal_expression200

    @pascal_expression200.setter
    def pascal_expression200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression200", None)
        self.__pascal_expression200 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_final_expression199"):
                opp_val = getattr(old_value, "pascal_final_expression199", None)
                if opp_val == self:
                    setattr(old_value, "pascal_final_expression199", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_final_expression199"):
                opp_val = getattr(value, "pascal_final_expression199", None)
                setattr(value, "pascal_final_expression199", self)

    @property
    def pascal_expression209(self):
        return self.__pascal_expression209

    @pascal_expression209.setter
    def pascal_expression209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression209", None)
        self.__pascal_expression209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_repeat_statement208"):
                opp_val = getattr(old_value, "pascal_repeat_statement208", None)
                if opp_val == self:
                    setattr(old_value, "pascal_repeat_statement208", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_repeat_statement208"):
                opp_val = getattr(value, "pascal_repeat_statement208", None)
                setattr(value, "pascal_repeat_statement208", self)

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
            if hasattr(old_value, "pascal_actual_value63"):
                opp_val = getattr(old_value, "pascal_actual_value63", None)
                if opp_val == self:
                    setattr(old_value, "pascal_actual_value63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_actual_value63"):
                opp_val = getattr(value, "pascal_actual_value63", None)
                setattr(value, "pascal_actual_value63", self)

    @property
    def pascal_expression166(self):
        return self.__pascal_expression166

    @pascal_expression166.setter
    def pascal_expression166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression166", None)
        self.__pascal_expression166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_case_statement165"):
                opp_val = getattr(old_value, "pascal_case_statement165", None)
                if opp_val == self:
                    setattr(old_value, "pascal_case_statement165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_statement165"):
                opp_val = getattr(value, "pascal_case_statement165", None)
                setattr(value, "pascal_case_statement165", self)

    @property
    def pascal_expression139(self):
        return self.__pascal_expression139

    @pascal_expression139.setter
    def pascal_expression139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression139", None)
        self.__pascal_expression139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list138"):
                opp_val = getattr(old_value, "pascal_expression_list138", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list138"):
                opp_val = getattr(value, "pascal_expression_list138", None)
                if opp_val is None:
                    setattr(value, "pascal_expression_list138", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_expression212(self):
        return self.__pascal_expression212

    @pascal_expression212.setter
    def pascal_expression212(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression212", None)
        self.__pascal_expression212 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_while_statement211"):
                opp_val = getattr(old_value, "pascal_while_statement211", None)
                if opp_val == self:
                    setattr(old_value, "pascal_while_statement211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_while_statement211"):
                opp_val = getattr(value, "pascal_while_statement211", None)
                setattr(value, "pascal_while_statement211", self)

    @property
    def pascal_expression72(self):
        return self.__pascal_expression72

    @pascal_expression72.setter
    def pascal_expression72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression72", None)
        self.__pascal_expression72 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_assignment_statement71"):
                opp_val = getattr(old_value, "pascal_assignment_statement71", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement71"):
                opp_val = getattr(value, "pascal_assignment_statement71", None)
                setattr(value, "pascal_assignment_statement71", self)

    @property
    def pascal_expression112(self):
        return self.__pascal_expression112

    @pascal_expression112.setter
    def pascal_expression112(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression112", None)
        self.__pascal_expression112 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_element_list111"):
                opp_val = getattr(old_value, "pascal_element_list111", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_element_list111"):
                opp_val = getattr(value, "pascal_element_list111", None)
                if opp_val is None:
                    setattr(value, "pascal_element_list111", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_expression178(self):
        return self.__pascal_expression178

    @pascal_expression178.setter
    def pascal_expression178(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression178", None)
        self.__pascal_expression178 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_if_statement177"):
                opp_val = getattr(old_value, "pascal_if_statement177", None)
                if opp_val == self:
                    setattr(old_value, "pascal_if_statement177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_if_statement177"):
                opp_val = getattr(value, "pascal_if_statement177", None)
                setattr(value, "pascal_if_statement177", self)

    @property
    def pascal_expression74(self):
        return self.__pascal_expression74

    @pascal_expression74.setter
    def pascal_expression74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression74", None)
        self.__pascal_expression74 = value if value is not None else set()
        
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
    def pascal_expression75(self):
        return self.__pascal_expression75

    @pascal_expression75.setter
    def pascal_expression75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression75", None)
        self.__pascal_expression75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pascal_expression77"):
                    opp_val = getattr(item, "pascal_expression77", None)
                    
                    if opp_val == self:
                        setattr(item, "pascal_expression77", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pascal_expression77"):
                    opp_val = getattr(item, "pascal_expression77", None)
                    
                    setattr(item, "pascal_expression77", self)
                    

    @property
    def pascal_expression203(self):
        return self.__pascal_expression203

    @pascal_expression203.setter
    def pascal_expression203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression203", None)
        self.__pascal_expression203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_initial_expression202"):
                opp_val = getattr(old_value, "pascal_initial_expression202", None)
                if opp_val == self:
                    setattr(old_value, "pascal_initial_expression202", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_initial_expression202"):
                opp_val = getattr(value, "pascal_initial_expression202", None)
                setattr(value, "pascal_initial_expression202", self)

    @property
    def pascal_expression98(self):
        return self.__pascal_expression98

    @pascal_expression98.setter
    def pascal_expression98(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression98", None)
        self.__pascal_expression98 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor97"):
                opp_val = getattr(old_value, "pascal_factor97", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor97", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor97"):
                opp_val = getattr(value, "pascal_factor97", None)
                setattr(value, "pascal_factor97", self)

    @property
    def pascal_expression77(self):
        return self.__pascal_expression77

    @pascal_expression77.setter
    def pascal_expression77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression77", None)
        self.__pascal_expression77 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression75"):
                opp_val = getattr(old_value, "pascal_expression75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression75"):
                opp_val = getattr(value, "pascal_expression75", None)
                if opp_val is None:
                    setattr(value, "pascal_expression75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_goto_statement:

    pass
class pascal_procedure_statement:

    pass
class pascal_assignment_statement:

    pass
class pascal_structured_statement:

    pass
class pascal_simple_statement:

    pass
class pascal_label:

    pass
class pascal_statement:

    pass
class pascal_actual_parameter:

    pass
class pascal_actual_parameter_list:

    pass
class pascal_identifier:

    def __init__(self, identifier: str, pascal_identifier: "pascal_procedure_statement" = None, pascal_identifier69: "pascal_assignment_statement" = None, pascal_identifier56: "pascal_actual_function" = None, pascal_identifier59: "pascal_actual_procedure" = None, pascal_identifier104: "pascal_function_designator" = None, pascal_identifier93: "pascal_factor" = None, pascal_identifier133: "pascal_variable" = None, pascal_identifier136: "pascal_entire_variable" = None, pascal_identifier190: "pascal_for_statement" = None, pascal_identifier248: "pascal_constant_definition" = None, pascal_identifier254: "pascal_constant" = None, pascal_identifier262: "pascal_type_definition" = None, pascal_identifier275: "pascal_type_identifier" = None, pascal_identifier328: "pascal_tag_field" = None, pascal_identifier366: "pascal_function_identification" = None, pascal_identifier372: "pascal_procedure_identification" = None, pascal_identifier383: "pascal_procedure_heading" = None, pascal_identifier401: "pascal_function_heading" = None, pascal_identifier443: "pascal_bound_specification" = None, pascal_identifier446: "pascal_bound_specification" = None):
        self.identifier = identifier
        self.pascal_identifier = pascal_identifier
        self.pascal_identifier69 = pascal_identifier69
        self.pascal_identifier56 = pascal_identifier56
        self.pascal_identifier59 = pascal_identifier59
        self.pascal_identifier104 = pascal_identifier104
        self.pascal_identifier93 = pascal_identifier93
        self.pascal_identifier133 = pascal_identifier133
        self.pascal_identifier136 = pascal_identifier136
        self.pascal_identifier190 = pascal_identifier190
        self.pascal_identifier248 = pascal_identifier248
        self.pascal_identifier254 = pascal_identifier254
        self.pascal_identifier262 = pascal_identifier262
        self.pascal_identifier275 = pascal_identifier275
        self.pascal_identifier328 = pascal_identifier328
        self.pascal_identifier366 = pascal_identifier366
        self.pascal_identifier372 = pascal_identifier372
        self.pascal_identifier383 = pascal_identifier383
        self.pascal_identifier401 = pascal_identifier401
        self.pascal_identifier443 = pascal_identifier443
        self.pascal_identifier446 = pascal_identifier446
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def pascal_identifier69(self):
        return self.__pascal_identifier69

    @pascal_identifier69.setter
    def pascal_identifier69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier69", None)
        self.__pascal_identifier69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_assignment_statement68"):
                opp_val = getattr(old_value, "pascal_assignment_statement68", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement68"):
                opp_val = getattr(value, "pascal_assignment_statement68", None)
                setattr(value, "pascal_assignment_statement68", self)

    @property
    def pascal_identifier401(self):
        return self.__pascal_identifier401

    @pascal_identifier401.setter
    def pascal_identifier401(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier401", None)
        self.__pascal_identifier401 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_heading400"):
                opp_val = getattr(old_value, "pascal_function_heading400", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_heading400", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_heading400"):
                opp_val = getattr(value, "pascal_function_heading400", None)
                setattr(value, "pascal_function_heading400", self)

    @property
    def pascal_identifier59(self):
        return self.__pascal_identifier59

    @pascal_identifier59.setter
    def pascal_identifier59(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier59", None)
        self.__pascal_identifier59 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_actual_procedure58"):
                opp_val = getattr(old_value, "pascal_actual_procedure58", None)
                if opp_val == self:
                    setattr(old_value, "pascal_actual_procedure58", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_actual_procedure58"):
                opp_val = getattr(value, "pascal_actual_procedure58", None)
                setattr(value, "pascal_actual_procedure58", self)

    @property
    def pascal_identifier248(self):
        return self.__pascal_identifier248

    @pascal_identifier248.setter
    def pascal_identifier248(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier248", None)
        self.__pascal_identifier248 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant_definition247"):
                opp_val = getattr(old_value, "pascal_constant_definition247", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant_definition247", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant_definition247"):
                opp_val = getattr(value, "pascal_constant_definition247", None)
                setattr(value, "pascal_constant_definition247", self)

    @property
    def pascal_identifier443(self):
        return self.__pascal_identifier443

    @pascal_identifier443.setter
    def pascal_identifier443(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier443", None)
        self.__pascal_identifier443 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_bound_specification442"):
                opp_val = getattr(old_value, "pascal_bound_specification442", None)
                if opp_val == self:
                    setattr(old_value, "pascal_bound_specification442", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_bound_specification442"):
                opp_val = getattr(value, "pascal_bound_specification442", None)
                setattr(value, "pascal_bound_specification442", self)

    @property
    def pascal_identifier133(self):
        return self.__pascal_identifier133

    @pascal_identifier133.setter
    def pascal_identifier133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier133", None)
        self.__pascal_identifier133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable132"):
                opp_val = getattr(old_value, "pascal_variable132", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable132"):
                opp_val = getattr(value, "pascal_variable132", None)
                if opp_val is None:
                    setattr(value, "pascal_variable132", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_identifier372(self):
        return self.__pascal_identifier372

    @pascal_identifier372.setter
    def pascal_identifier372(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier372", None)
        self.__pascal_identifier372 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_procedure_identification371"):
                opp_val = getattr(old_value, "pascal_procedure_identification371", None)
                if opp_val == self:
                    setattr(old_value, "pascal_procedure_identification371", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_identification371"):
                opp_val = getattr(value, "pascal_procedure_identification371", None)
                setattr(value, "pascal_procedure_identification371", self)

    @property
    def pascal_identifier262(self):
        return self.__pascal_identifier262

    @pascal_identifier262.setter
    def pascal_identifier262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier262", None)
        self.__pascal_identifier262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_type_definition261"):
                opp_val = getattr(old_value, "pascal_type_definition261", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type_definition261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type_definition261"):
                opp_val = getattr(value, "pascal_type_definition261", None)
                setattr(value, "pascal_type_definition261", self)

    @property
    def pascal_identifier446(self):
        return self.__pascal_identifier446

    @pascal_identifier446.setter
    def pascal_identifier446(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier446", None)
        self.__pascal_identifier446 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_bound_specification445"):
                opp_val = getattr(old_value, "pascal_bound_specification445", None)
                if opp_val == self:
                    setattr(old_value, "pascal_bound_specification445", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_bound_specification445"):
                opp_val = getattr(value, "pascal_bound_specification445", None)
                setattr(value, "pascal_bound_specification445", self)

    @property
    def pascal_identifier190(self):
        return self.__pascal_identifier190

    @pascal_identifier190.setter
    def pascal_identifier190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier190", None)
        self.__pascal_identifier190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_for_statement189"):
                opp_val = getattr(old_value, "pascal_for_statement189", None)
                if opp_val == self:
                    setattr(old_value, "pascal_for_statement189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_for_statement189"):
                opp_val = getattr(value, "pascal_for_statement189", None)
                setattr(value, "pascal_for_statement189", self)

    @property
    def pascal_identifier328(self):
        return self.__pascal_identifier328

    @pascal_identifier328.setter
    def pascal_identifier328(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier328", None)
        self.__pascal_identifier328 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_tag_field327"):
                opp_val = getattr(old_value, "pascal_tag_field327", None)
                if opp_val == self:
                    setattr(old_value, "pascal_tag_field327", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_tag_field327"):
                opp_val = getattr(value, "pascal_tag_field327", None)
                setattr(value, "pascal_tag_field327", self)

    @property
    def pascal_identifier104(self):
        return self.__pascal_identifier104

    @pascal_identifier104.setter
    def pascal_identifier104(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier104", None)
        self.__pascal_identifier104 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_designator103"):
                opp_val = getattr(old_value, "pascal_function_designator103", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_designator103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_designator103"):
                opp_val = getattr(value, "pascal_function_designator103", None)
                setattr(value, "pascal_function_designator103", self)

    @property
    def pascal_identifier56(self):
        return self.__pascal_identifier56

    @pascal_identifier56.setter
    def pascal_identifier56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier56", None)
        self.__pascal_identifier56 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_actual_function55"):
                opp_val = getattr(old_value, "pascal_actual_function55", None)
                if opp_val == self:
                    setattr(old_value, "pascal_actual_function55", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_actual_function55"):
                opp_val = getattr(value, "pascal_actual_function55", None)
                setattr(value, "pascal_actual_function55", self)

    @property
    def pascal_identifier254(self):
        return self.__pascal_identifier254

    @pascal_identifier254.setter
    def pascal_identifier254(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier254", None)
        self.__pascal_identifier254 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant253"):
                opp_val = getattr(old_value, "pascal_constant253", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant253", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant253"):
                opp_val = getattr(value, "pascal_constant253", None)
                setattr(value, "pascal_constant253", self)

    @property
    def pascal_identifier(self):
        return self.__pascal_identifier

    @pascal_identifier.setter
    def pascal_identifier(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier", None)
        self.__pascal_identifier = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_procedure_statement41"):
                opp_val = getattr(old_value, "pascal_procedure_statement41", None)
                if opp_val == self:
                    setattr(old_value, "pascal_procedure_statement41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_statement41"):
                opp_val = getattr(value, "pascal_procedure_statement41", None)
                setattr(value, "pascal_procedure_statement41", self)

    @property
    def pascal_identifier136(self):
        return self.__pascal_identifier136

    @pascal_identifier136.setter
    def pascal_identifier136(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier136", None)
        self.__pascal_identifier136 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_entire_variable135"):
                opp_val = getattr(old_value, "pascal_entire_variable135", None)
                if opp_val == self:
                    setattr(old_value, "pascal_entire_variable135", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_entire_variable135"):
                opp_val = getattr(value, "pascal_entire_variable135", None)
                setattr(value, "pascal_entire_variable135", self)

    @property
    def pascal_identifier383(self):
        return self.__pascal_identifier383

    @pascal_identifier383.setter
    def pascal_identifier383(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier383", None)
        self.__pascal_identifier383 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_procedure_heading382"):
                opp_val = getattr(old_value, "pascal_procedure_heading382", None)
                if opp_val == self:
                    setattr(old_value, "pascal_procedure_heading382", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_heading382"):
                opp_val = getattr(value, "pascal_procedure_heading382", None)
                setattr(value, "pascal_procedure_heading382", self)

    @property
    def pascal_identifier366(self):
        return self.__pascal_identifier366

    @pascal_identifier366.setter
    def pascal_identifier366(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier366", None)
        self.__pascal_identifier366 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_identification365"):
                opp_val = getattr(old_value, "pascal_function_identification365", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_identification365", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_identification365"):
                opp_val = getattr(value, "pascal_function_identification365", None)
                setattr(value, "pascal_function_identification365", self)

    @property
    def pascal_identifier275(self):
        return self.__pascal_identifier275

    @pascal_identifier275.setter
    def pascal_identifier275(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier275", None)
        self.__pascal_identifier275 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_type_identifier274"):
                opp_val = getattr(old_value, "pascal_type_identifier274", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type_identifier274", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type_identifier274"):
                opp_val = getattr(value, "pascal_type_identifier274", None)
                setattr(value, "pascal_type_identifier274", self)

    @property
    def pascal_identifier93(self):
        return self.__pascal_identifier93

    @pascal_identifier93.setter
    def pascal_identifier93(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier__pascal_identifier93", None)
        self.__pascal_identifier93 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor92"):
                opp_val = getattr(old_value, "pascal_factor92", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor92", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor92"):
                opp_val = getattr(value, "pascal_factor92", None)
                setattr(value, "pascal_factor92", self)

class pascal_function_block:

    pass
class pascal_statement_part:

    pass
class pascal_declaration_part:

    pass
class pascal_procedure_block:

    pass
class pascal_identifier_list:

    def __init__(self, identifier: str, pascal_identifier_list: "pascal_program_heading" = None, pascal_identifier_list309: "pascal_record_section" = None, pascal_identifier_list345: "pascal_enumerated_type" = None, pascal_identifier_list360: "pascal_variable_declaration" = None, pascal_identifier_list415: "pascal_variable_parameter_section" = None, pascal_identifier_list420: "pascal_value_parameter_section" = None):
        self.identifier = identifier
        self.pascal_identifier_list = pascal_identifier_list
        self.pascal_identifier_list309 = pascal_identifier_list309
        self.pascal_identifier_list345 = pascal_identifier_list345
        self.pascal_identifier_list360 = pascal_identifier_list360
        self.pascal_identifier_list415 = pascal_identifier_list415
        self.pascal_identifier_list420 = pascal_identifier_list420
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def pascal_identifier_list420(self):
        return self.__pascal_identifier_list420

    @pascal_identifier_list420.setter
    def pascal_identifier_list420(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list420", None)
        self.__pascal_identifier_list420 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_value_parameter_section419"):
                opp_val = getattr(old_value, "pascal_value_parameter_section419", None)
                if opp_val == self:
                    setattr(old_value, "pascal_value_parameter_section419", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_value_parameter_section419"):
                opp_val = getattr(value, "pascal_value_parameter_section419", None)
                setattr(value, "pascal_value_parameter_section419", self)

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
            if hasattr(old_value, "pascal_program_heading6"):
                opp_val = getattr(old_value, "pascal_program_heading6", None)
                if opp_val == self:
                    setattr(old_value, "pascal_program_heading6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_program_heading6"):
                opp_val = getattr(value, "pascal_program_heading6", None)
                setattr(value, "pascal_program_heading6", self)

    @property
    def pascal_identifier_list309(self):
        return self.__pascal_identifier_list309

    @pascal_identifier_list309.setter
    def pascal_identifier_list309(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list309", None)
        self.__pascal_identifier_list309 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_record_section308"):
                opp_val = getattr(old_value, "pascal_record_section308", None)
                if opp_val == self:
                    setattr(old_value, "pascal_record_section308", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_record_section308"):
                opp_val = getattr(value, "pascal_record_section308", None)
                setattr(value, "pascal_record_section308", self)

    @property
    def pascal_identifier_list345(self):
        return self.__pascal_identifier_list345

    @pascal_identifier_list345.setter
    def pascal_identifier_list345(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list345", None)
        self.__pascal_identifier_list345 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_enumerated_type344"):
                opp_val = getattr(old_value, "pascal_enumerated_type344", None)
                if opp_val == self:
                    setattr(old_value, "pascal_enumerated_type344", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_enumerated_type344"):
                opp_val = getattr(value, "pascal_enumerated_type344", None)
                setattr(value, "pascal_enumerated_type344", self)

    @property
    def pascal_identifier_list415(self):
        return self.__pascal_identifier_list415

    @pascal_identifier_list415.setter
    def pascal_identifier_list415(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list415", None)
        self.__pascal_identifier_list415 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_parameter_section414"):
                opp_val = getattr(old_value, "pascal_variable_parameter_section414", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_parameter_section414", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_parameter_section414"):
                opp_val = getattr(value, "pascal_variable_parameter_section414", None)
                setattr(value, "pascal_variable_parameter_section414", self)

    @property
    def pascal_identifier_list360(self):
        return self.__pascal_identifier_list360

    @pascal_identifier_list360.setter
    def pascal_identifier_list360(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list360", None)
        self.__pascal_identifier_list360 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_declaration359"):
                opp_val = getattr(old_value, "pascal_variable_declaration359", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_declaration359", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_declaration359"):
                opp_val = getattr(value, "pascal_variable_declaration359", None)
                setattr(value, "pascal_variable_declaration359", self)

class pascal_block:

    pass
class pascal_program_heading:

    def __init__(self, identifier: str, pascal_program_heading: "pascal_program" = None, pascal_program_heading6: "pascal_identifier_list" = None):
        self.identifier = identifier
        self.pascal_program_heading = pascal_program_heading
        self.pascal_program_heading6 = pascal_program_heading6
        
    @property
    def identifier(self) -> str:
        return self.__identifier

    @identifier.setter
    def identifier(self, identifier: str):
        self.__identifier = identifier

    @property
    def pascal_program_heading6(self):
        return self.__pascal_program_heading6

    @pascal_program_heading6.setter
    def pascal_program_heading6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_program_heading__pascal_program_heading6", None)
        self.__pascal_program_heading6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_identifier_list"):
                opp_val = getattr(old_value, "pascal_identifier_list", None)
                if opp_val == self:
                    setattr(old_value, "pascal_identifier_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_identifier_list"):
                opp_val = getattr(value, "pascal_identifier_list", None)
                setattr(value, "pascal_identifier_list", self)

    @property
    def pascal_program_heading(self):
        return self.__pascal_program_heading

    @pascal_program_heading.setter
    def pascal_program_heading(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_program_heading__pascal_program_heading", None)
        self.__pascal_program_heading = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_program2"):
                opp_val = getattr(old_value, "pascal_program2", None)
                if opp_val == self:
                    setattr(old_value, "pascal_program2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_program2"):
                opp_val = getattr(value, "pascal_program2", None)
                setattr(value, "pascal_program2", self)

class pascal_statement_sequence:

    pass
class pascal_program:

    pass
class pascal_Begin:

    pass