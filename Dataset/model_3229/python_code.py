from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pascal_packed_conformant_array_schema:

    def __init__(self, name: str, pascal_packed_conformant_array_schema: "pascal_conformant_array_schema" = None, pascal_packed_conformant_array_schema292: "pascal_bound_specification" = None):
        self.name = name
        self.pascal_packed_conformant_array_schema = pascal_packed_conformant_array_schema
        self.pascal_packed_conformant_array_schema292 = pascal_packed_conformant_array_schema292
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_packed_conformant_array_schema292(self):
        return self.__pascal_packed_conformant_array_schema292

    @pascal_packed_conformant_array_schema292.setter
    def pascal_packed_conformant_array_schema292(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_packed_conformant_array_schema__pascal_packed_conformant_array_schema292", None)
        self.__pascal_packed_conformant_array_schema292 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_bound_specification"):
                opp_val = getattr(old_value, "pascal_bound_specification", None)
                if opp_val == self:
                    setattr(old_value, "pascal_bound_specification", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_bound_specification"):
                opp_val = getattr(value, "pascal_bound_specification", None)
                setattr(value, "pascal_bound_specification", self)

    @property
    def pascal_packed_conformant_array_schema(self):
        return self.__pascal_packed_conformant_array_schema

    @pascal_packed_conformant_array_schema.setter
    def pascal_packed_conformant_array_schema(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_packed_conformant_array_schema__pascal_packed_conformant_array_schema", None)
        self.__pascal_packed_conformant_array_schema = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_conformant_array_schema288"):
                opp_val = getattr(old_value, "pascal_conformant_array_schema288", None)
                if opp_val == self:
                    setattr(old_value, "pascal_conformant_array_schema288", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_conformant_array_schema288"):
                opp_val = getattr(value, "pascal_conformant_array_schema288", None)
                setattr(value, "pascal_conformant_array_schema288", self)

class pascal_conformant_array_schema:

    pass
class pascal_parameter_type:

    def __init__(self, name: str, pascal_parameter_type298: "pascal_unpacked_conformant_array_schema" = None, pascal_parameter_type304: "pascal_variable_parameter_section" = None, pascal_parameter_type: "pascal_value_parameter_section" = None, pascal_parameter_type286: "pascal_conformant_array_schema" = None):
        self.name = name
        self.pascal_parameter_type298 = pascal_parameter_type298
        self.pascal_parameter_type304 = pascal_parameter_type304
        self.pascal_parameter_type = pascal_parameter_type
        self.pascal_parameter_type286 = pascal_parameter_type286
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_parameter_type298(self):
        return self.__pascal_parameter_type298

    @pascal_parameter_type298.setter
    def pascal_parameter_type298(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type298", None)
        self.__pascal_parameter_type298 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_conformant_array_schema297"):
                opp_val = getattr(old_value, "pascal_unpacked_conformant_array_schema297", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unpacked_conformant_array_schema297", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_conformant_array_schema297"):
                opp_val = getattr(value, "pascal_unpacked_conformant_array_schema297", None)
                setattr(value, "pascal_unpacked_conformant_array_schema297", self)

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
            if hasattr(old_value, "pascal_value_parameter_section284"):
                opp_val = getattr(old_value, "pascal_value_parameter_section284", None)
                if opp_val == self:
                    setattr(old_value, "pascal_value_parameter_section284", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_value_parameter_section284"):
                opp_val = getattr(value, "pascal_value_parameter_section284", None)
                setattr(value, "pascal_value_parameter_section284", self)

    @property
    def pascal_parameter_type286(self):
        return self.__pascal_parameter_type286

    @pascal_parameter_type286.setter
    def pascal_parameter_type286(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type286", None)
        self.__pascal_parameter_type286 = value
        
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

    @property
    def pascal_parameter_type304(self):
        return self.__pascal_parameter_type304

    @pascal_parameter_type304.setter
    def pascal_parameter_type304(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type304", None)
        self.__pascal_parameter_type304 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_parameter_section303"):
                opp_val = getattr(old_value, "pascal_variable_parameter_section303", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_parameter_section303", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_parameter_section303"):
                opp_val = getattr(value, "pascal_variable_parameter_section303", None)
                setattr(value, "pascal_variable_parameter_section303", self)

class pascal_variable_parameter_section:

    pass
class pascal_value_parameter_section:

    pass
class pascal_formal_parameter_section:

    pass
class pascal_formal_parameter_list:

    pass
class abstraction_declaration:

    pass
class pascal_abstraction_declaration:

    def __init__(self, forward: bool, pascal_abstraction_declaration: "pascal_procedure_and_function_declaration_part" = None, pascal_abstraction_declaration261: "pascal_abstraction_heading" = None, pascal_abstraction_declaration264: "pascal_block" = None):
        self.forward = forward
        self.pascal_abstraction_declaration = pascal_abstraction_declaration
        self.pascal_abstraction_declaration261 = pascal_abstraction_declaration261
        self.pascal_abstraction_declaration264 = pascal_abstraction_declaration264
        
    @property
    def forward(self) -> bool:
        return self.__forward

    @forward.setter
    def forward(self, forward: bool):
        self.__forward = forward

    @property
    def pascal_abstraction_declaration(self):
        return self.__pascal_abstraction_declaration

    @pascal_abstraction_declaration.setter
    def pascal_abstraction_declaration(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_declaration__pascal_abstraction_declaration", None)
        self.__pascal_abstraction_declaration = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_procedure_and_function_declaration_part259"):
                opp_val = getattr(old_value, "pascal_procedure_and_function_declaration_part259", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_and_function_declaration_part259"):
                opp_val = getattr(value, "pascal_procedure_and_function_declaration_part259", None)
                if opp_val is None:
                    setattr(value, "pascal_procedure_and_function_declaration_part259", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_abstraction_declaration261(self):
        return self.__pascal_abstraction_declaration261

    @pascal_abstraction_declaration261.setter
    def pascal_abstraction_declaration261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_declaration__pascal_abstraction_declaration261", None)
        self.__pascal_abstraction_declaration261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_abstraction_heading262"):
                opp_val = getattr(old_value, "pascal_abstraction_heading262", None)
                if opp_val == self:
                    setattr(old_value, "pascal_abstraction_heading262", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_abstraction_heading262"):
                opp_val = getattr(value, "pascal_abstraction_heading262", None)
                setattr(value, "pascal_abstraction_heading262", self)

    @property
    def pascal_abstraction_declaration264(self):
        return self.__pascal_abstraction_declaration264

    @pascal_abstraction_declaration264.setter
    def pascal_abstraction_declaration264(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_declaration__pascal_abstraction_declaration264", None)
        self.__pascal_abstraction_declaration264 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_block265"):
                opp_val = getattr(old_value, "pascal_block265", None)
                if opp_val == self:
                    setattr(old_value, "pascal_block265", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_block265"):
                opp_val = getattr(value, "pascal_block265", None)
                setattr(value, "pascal_block265", self)

class pascal_bound_specification:

    def __init__(self, initial: str, final: str, name: str, pascal_bound_specification: "pascal_packed_conformant_array_schema" = None, pascal_bound_specification295: "pascal_unpacked_conformant_array_schema" = None):
        self.initial = initial
        self.final = final
        self.name = name
        self.pascal_bound_specification = pascal_bound_specification
        self.pascal_bound_specification295 = pascal_bound_specification295
        
    @property
    def initial(self) -> str:
        return self.__initial

    @initial.setter
    def initial(self, initial: str):
        self.__initial = initial

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def final(self) -> str:
        return self.__final

    @final.setter
    def final(self, final: str):
        self.__final = final

    @property
    def pascal_bound_specification295(self):
        return self.__pascal_bound_specification295

    @pascal_bound_specification295.setter
    def pascal_bound_specification295(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_bound_specification__pascal_bound_specification295", None)
        self.__pascal_bound_specification295 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_conformant_array_schema294"):
                opp_val = getattr(old_value, "pascal_unpacked_conformant_array_schema294", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_conformant_array_schema294"):
                opp_val = getattr(value, "pascal_unpacked_conformant_array_schema294", None)
                if opp_val is None:
                    setattr(value, "pascal_unpacked_conformant_array_schema294", set([self]))
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
            if hasattr(old_value, "pascal_packed_conformant_array_schema292"):
                opp_val = getattr(old_value, "pascal_packed_conformant_array_schema292", None)
                if opp_val == self:
                    setattr(old_value, "pascal_packed_conformant_array_schema292", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_packed_conformant_array_schema292"):
                opp_val = getattr(value, "pascal_packed_conformant_array_schema292", None)
                setattr(value, "pascal_packed_conformant_array_schema292", self)

class pascal_unpacked_conformant_array_schema:

    pass
class pascal_variant:

    pass
class pascal_tag_field:

    def __init__(self, name: str, pascal_tag_field: "pascal_variant_part" = None):
        self.name = name
        self.pascal_tag_field = pascal_tag_field
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "pascal_variant_part235"):
                opp_val = getattr(old_value, "pascal_variant_part235", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variant_part235", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variant_part235"):
                opp_val = getattr(value, "pascal_variant_part235", None)
                setattr(value, "pascal_variant_part235", self)

class pascal_variable_section:

    pass
class pascal_abstraction_heading(abstraction_declaration):

    def __init__(self, name: str, returnType: str, pascal_abstraction_heading: "pascal_procedure_and_function_declaration_part" = None, pascal_abstraction_heading262: "pascal_abstraction_declaration" = None, pascal_abstraction_heading267: "pascal_formal_parameter_list" = None, pascal_abstraction_heading276: "pascal_formal_parameter_section" = None, pascal_abstraction_heading279: "pascal_formal_parameter_section" = None):
        self.name = name
        self.returnType = returnType
        self.pascal_abstraction_heading = pascal_abstraction_heading
        self.pascal_abstraction_heading262 = pascal_abstraction_heading262
        self.pascal_abstraction_heading267 = pascal_abstraction_heading267
        self.pascal_abstraction_heading276 = pascal_abstraction_heading276
        self.pascal_abstraction_heading279 = pascal_abstraction_heading279
        
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
    def pascal_abstraction_heading(self):
        return self.__pascal_abstraction_heading

    @pascal_abstraction_heading.setter
    def pascal_abstraction_heading(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading", None)
        self.__pascal_abstraction_heading = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_procedure_and_function_declaration_part257"):
                opp_val = getattr(old_value, "pascal_procedure_and_function_declaration_part257", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_and_function_declaration_part257"):
                opp_val = getattr(value, "pascal_procedure_and_function_declaration_part257", None)
                if opp_val is None:
                    setattr(value, "pascal_procedure_and_function_declaration_part257", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_abstraction_heading267(self):
        return self.__pascal_abstraction_heading267

    @pascal_abstraction_heading267.setter
    def pascal_abstraction_heading267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading267", None)
        self.__pascal_abstraction_heading267 = value
        
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
    def pascal_abstraction_heading279(self):
        return self.__pascal_abstraction_heading279

    @pascal_abstraction_heading279.setter
    def pascal_abstraction_heading279(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading279", None)
        self.__pascal_abstraction_heading279 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_section278"):
                opp_val = getattr(old_value, "pascal_formal_parameter_section278", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_section278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_section278"):
                opp_val = getattr(value, "pascal_formal_parameter_section278", None)
                setattr(value, "pascal_formal_parameter_section278", self)

    @property
    def pascal_abstraction_heading276(self):
        return self.__pascal_abstraction_heading276

    @pascal_abstraction_heading276.setter
    def pascal_abstraction_heading276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading276", None)
        self.__pascal_abstraction_heading276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_section275"):
                opp_val = getattr(old_value, "pascal_formal_parameter_section275", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_section275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_section275"):
                opp_val = getattr(value, "pascal_formal_parameter_section275", None)
                setattr(value, "pascal_formal_parameter_section275", self)

    @property
    def pascal_abstraction_heading262(self):
        return self.__pascal_abstraction_heading262

    @pascal_abstraction_heading262.setter
    def pascal_abstraction_heading262(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading262", None)
        self.__pascal_abstraction_heading262 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_abstraction_declaration261"):
                opp_val = getattr(old_value, "pascal_abstraction_declaration261", None)
                if opp_val == self:
                    setattr(old_value, "pascal_abstraction_declaration261", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_abstraction_declaration261"):
                opp_val = getattr(value, "pascal_abstraction_declaration261", None)
                setattr(value, "pascal_abstraction_declaration261", self)

class pascal_fixed_part:

    pass
class pascal_field_list:

    pass
class pascal_index_type:

    pass
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
            if hasattr(old_value, "pascal_variable_section"):
                opp_val = getattr(old_value, "pascal_variable_section", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_section", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_section"):
                opp_val = getattr(value, "pascal_variable_section", None)
                setattr(value, "pascal_variable_section", self)

class pascal_record_section:

    pass
class pascal_variant_part:

    def __init__(self, name: str, pascal_variant_part: "pascal_field_list" = None, pascal_variant_part235: "pascal_tag_field" = None, pascal_variant_part237: set["pascal_variant"] = None):
        self.name = name
        self.pascal_variant_part = pascal_variant_part
        self.pascal_variant_part235 = pascal_variant_part235
        self.pascal_variant_part237 = pascal_variant_part237 if pascal_variant_part237 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_variant_part235(self):
        return self.__pascal_variant_part235

    @pascal_variant_part235.setter
    def pascal_variant_part235(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part235", None)
        self.__pascal_variant_part235 = value
        
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
            if hasattr(old_value, "pascal_field_list221"):
                opp_val = getattr(old_value, "pascal_field_list221", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_field_list221"):
                opp_val = getattr(value, "pascal_field_list221", None)
                if opp_val is None:
                    setattr(value, "pascal_field_list221", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_variant_part237(self):
        return self.__pascal_variant_part237

    @pascal_variant_part237.setter
    def pascal_variant_part237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part237", None)
        self.__pascal_variant_part237 = value if value is not None else set()
        
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
                    

class pascal_dynamic_array_type:

    pass
class pascal_array_type:

    pass
class pascal_unpacked_structured_type:

    pass
class pascal_file_type:

    pass
class pascal_set_type:

    pass
class pascal_record_type:

    def __init__(self, recordKeyword: str, endKeyword: str, pascal_record_type: "pascal_unpacked_structured_type" = None, pascal_record_type217: "pascal_field_list" = None):
        self.recordKeyword = recordKeyword
        self.endKeyword = endKeyword
        self.pascal_record_type = pascal_record_type
        self.pascal_record_type217 = pascal_record_type217
        
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
    def pascal_record_type(self):
        return self.__pascal_record_type

    @pascal_record_type.setter
    def pascal_record_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_record_type__pascal_record_type", None)
        self.__pascal_record_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_structured_type200"):
                opp_val = getattr(old_value, "pascal_unpacked_structured_type200", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unpacked_structured_type200", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_structured_type200"):
                opp_val = getattr(value, "pascal_unpacked_structured_type200", None)
                setattr(value, "pascal_unpacked_structured_type200", self)

    @property
    def pascal_record_type217(self):
        return self.__pascal_record_type217

    @pascal_record_type217.setter
    def pascal_record_type217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_record_type__pascal_record_type217", None)
        self.__pascal_record_type217 = value
        
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

class pascal_pointer_type:

    pass
class pascal_structured_type:

    def __init__(self, packed: bool, pascal_structured_type: "pascal_type" = None, pascal_structured_type194: "pascal_unpacked_structured_type" = None):
        self.packed = packed
        self.pascal_structured_type = pascal_structured_type
        self.pascal_structured_type194 = pascal_structured_type194
        
    @property
    def packed(self) -> bool:
        return self.__packed

    @packed.setter
    def packed(self, packed: bool):
        self.__packed = packed

    @property
    def pascal_structured_type194(self):
        return self.__pascal_structured_type194

    @pascal_structured_type194.setter
    def pascal_structured_type194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_structured_type__pascal_structured_type194", None)
        self.__pascal_structured_type194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_structured_type"):
                opp_val = getattr(old_value, "pascal_unpacked_structured_type", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unpacked_structured_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_structured_type"):
                opp_val = getattr(value, "pascal_unpacked_structured_type", None)
                setattr(value, "pascal_unpacked_structured_type", self)

    @property
    def pascal_structured_type(self):
        return self.__pascal_structured_type

    @pascal_structured_type.setter
    def pascal_structured_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_structured_type__pascal_structured_type", None)
        self.__pascal_structured_type = value
        
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

class pascal_simple_type:

    def __init__(self, name: str, pascal_simple_type178: "pascal_subrange_type" = None, pascal_simple_type180: "pascal_enumerated_type" = None, pascal_simple_type: "pascal_type" = None, pascal_simple_type215: "pascal_index_type" = None):
        self.name = name
        self.pascal_simple_type178 = pascal_simple_type178
        self.pascal_simple_type180 = pascal_simple_type180
        self.pascal_simple_type = pascal_simple_type
        self.pascal_simple_type215 = pascal_simple_type215
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_simple_type180(self):
        return self.__pascal_simple_type180

    @pascal_simple_type180.setter
    def pascal_simple_type180(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type180", None)
        self.__pascal_simple_type180 = value
        
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
    def pascal_simple_type215(self):
        return self.__pascal_simple_type215

    @pascal_simple_type215.setter
    def pascal_simple_type215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type215", None)
        self.__pascal_simple_type215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_index_type214"):
                opp_val = getattr(old_value, "pascal_index_type214", None)
                if opp_val == self:
                    setattr(old_value, "pascal_index_type214", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_index_type214"):
                opp_val = getattr(value, "pascal_index_type214", None)
                setattr(value, "pascal_index_type214", self)

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
            if hasattr(old_value, "pascal_type172"):
                opp_val = getattr(old_value, "pascal_type172", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type172"):
                opp_val = getattr(value, "pascal_type172", None)
                setattr(value, "pascal_type172", self)

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
            if hasattr(old_value, "pascal_subrange_type"):
                opp_val = getattr(old_value, "pascal_subrange_type", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type"):
                opp_val = getattr(value, "pascal_subrange_type", None)
                setattr(value, "pascal_subrange_type", self)

class pascal_type:

    pass
class pascal_type_definition:

    def __init__(self, name: str, pascal_type_definition: "pascal_type_definition_part" = None, pascal_type_definition170: "pascal_type" = None):
        self.name = name
        self.pascal_type_definition = pascal_type_definition
        self.pascal_type_definition170 = pascal_type_definition170
        
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
            if hasattr(old_value, "pascal_type_definition_part168"):
                opp_val = getattr(old_value, "pascal_type_definition_part168", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type_definition_part168"):
                opp_val = getattr(value, "pascal_type_definition_part168", None)
                if opp_val is None:
                    setattr(value, "pascal_type_definition_part168", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_type_definition170(self):
        return self.__pascal_type_definition170

    @pascal_type_definition170.setter
    def pascal_type_definition170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type_definition__pascal_type_definition170", None)
        self.__pascal_type_definition170 = value
        
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

class pascal_enumerated_type:

    pass
class pascal_subrange_type:

    def __init__(self, subrange: str, pascal_subrange_type: "pascal_simple_type" = None, pascal_subrange_type182: "pascal_constant" = None, pascal_subrange_type185: "pascal_constant" = None, pascal_subrange_type188: "pascal_constant" = None):
        self.subrange = subrange
        self.pascal_subrange_type = pascal_subrange_type
        self.pascal_subrange_type182 = pascal_subrange_type182
        self.pascal_subrange_type185 = pascal_subrange_type185
        self.pascal_subrange_type188 = pascal_subrange_type188
        
    @property
    def subrange(self) -> str:
        return self.__subrange

    @subrange.setter
    def subrange(self, subrange: str):
        self.__subrange = subrange

    @property
    def pascal_subrange_type185(self):
        return self.__pascal_subrange_type185

    @pascal_subrange_type185.setter
    def pascal_subrange_type185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type185", None)
        self.__pascal_subrange_type185 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant186"):
                opp_val = getattr(old_value, "pascal_constant186", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant186"):
                opp_val = getattr(value, "pascal_constant186", None)
                setattr(value, "pascal_constant186", self)

    @property
    def pascal_subrange_type(self):
        return self.__pascal_subrange_type

    @pascal_subrange_type.setter
    def pascal_subrange_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type", None)
        self.__pascal_subrange_type = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_simple_type178"):
                opp_val = getattr(old_value, "pascal_simple_type178", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simple_type178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_type178"):
                opp_val = getattr(value, "pascal_simple_type178", None)
                setattr(value, "pascal_simple_type178", self)

    @property
    def pascal_subrange_type188(self):
        return self.__pascal_subrange_type188

    @pascal_subrange_type188.setter
    def pascal_subrange_type188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type188", None)
        self.__pascal_subrange_type188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant189"):
                opp_val = getattr(old_value, "pascal_constant189", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant189"):
                opp_val = getattr(value, "pascal_constant189", None)
                setattr(value, "pascal_constant189", self)

    @property
    def pascal_subrange_type182(self):
        return self.__pascal_subrange_type182

    @pascal_subrange_type182.setter
    def pascal_subrange_type182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type182", None)
        self.__pascal_subrange_type182 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant183"):
                opp_val = getattr(old_value, "pascal_constant183", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant183"):
                opp_val = getattr(value, "pascal_constant183", None)
                setattr(value, "pascal_constant183", self)

class pascal_constant:

    def __init__(self, opterator: str, name: str, string: str, boolLiteral: str, nil: str, pascal_constant: "pascal_case_label_list" = None, pascal_constant148: "pascal_number" = None, pascal_constant166: "pascal_constant_definition" = None, pascal_constant183: "pascal_subrange_type" = None, pascal_constant186: "pascal_subrange_type" = None, pascal_constant189: "pascal_subrange_type" = None):
        self.opterator = opterator
        self.name = name
        self.string = string
        self.boolLiteral = boolLiteral
        self.nil = nil
        self.pascal_constant = pascal_constant
        self.pascal_constant148 = pascal_constant148
        self.pascal_constant166 = pascal_constant166
        self.pascal_constant183 = pascal_constant183
        self.pascal_constant186 = pascal_constant186
        self.pascal_constant189 = pascal_constant189
        
    @property
    def nil(self) -> str:
        return self.__nil

    @nil.setter
    def nil(self, nil: str):
        self.__nil = nil

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def opterator(self) -> str:
        return self.__opterator

    @opterator.setter
    def opterator(self, opterator: str):
        self.__opterator = opterator

    @property
    def boolLiteral(self) -> str:
        return self.__boolLiteral

    @boolLiteral.setter
    def boolLiteral(self, boolLiteral: str):
        self.__boolLiteral = boolLiteral

    @property
    def pascal_constant166(self):
        return self.__pascal_constant166

    @pascal_constant166.setter
    def pascal_constant166(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant166", None)
        self.__pascal_constant166 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant_definition165"):
                opp_val = getattr(old_value, "pascal_constant_definition165", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant_definition165", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant_definition165"):
                opp_val = getattr(value, "pascal_constant_definition165", None)
                setattr(value, "pascal_constant_definition165", self)

    @property
    def pascal_constant189(self):
        return self.__pascal_constant189

    @pascal_constant189.setter
    def pascal_constant189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant189", None)
        self.__pascal_constant189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type188"):
                opp_val = getattr(old_value, "pascal_subrange_type188", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type188"):
                opp_val = getattr(value, "pascal_subrange_type188", None)
                setattr(value, "pascal_subrange_type188", self)

    @property
    def pascal_constant183(self):
        return self.__pascal_constant183

    @pascal_constant183.setter
    def pascal_constant183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant183", None)
        self.__pascal_constant183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type182"):
                opp_val = getattr(old_value, "pascal_subrange_type182", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type182"):
                opp_val = getattr(value, "pascal_subrange_type182", None)
                setattr(value, "pascal_subrange_type182", self)

    @property
    def pascal_constant148(self):
        return self.__pascal_constant148

    @pascal_constant148.setter
    def pascal_constant148(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant148", None)
        self.__pascal_constant148 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_number149"):
                opp_val = getattr(old_value, "pascal_number149", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number149", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number149"):
                opp_val = getattr(value, "pascal_number149", None)
                setattr(value, "pascal_number149", self)

    @property
    def pascal_constant186(self):
        return self.__pascal_constant186

    @pascal_constant186.setter
    def pascal_constant186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant186", None)
        self.__pascal_constant186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type185"):
                opp_val = getattr(old_value, "pascal_subrange_type185", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type185", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type185"):
                opp_val = getattr(value, "pascal_subrange_type185", None)
                setattr(value, "pascal_subrange_type185", self)

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
            if hasattr(old_value, "pascal_case_label_list146"):
                opp_val = getattr(old_value, "pascal_case_label_list146", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_label_list146"):
                opp_val = getattr(value, "pascal_case_label_list146", None)
                if opp_val is None:
                    setattr(value, "pascal_case_label_list146", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_constant_definition:

    def __init__(self, name: str, pascal_constant_definition: "pascal_constant_definition_part" = None, pascal_constant_definition165: "pascal_constant" = None):
        self.name = name
        self.pascal_constant_definition = pascal_constant_definition
        self.pascal_constant_definition165 = pascal_constant_definition165
        
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
            if hasattr(old_value, "pascal_constant_definition_part163"):
                opp_val = getattr(old_value, "pascal_constant_definition_part163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant_definition_part163"):
                opp_val = getattr(value, "pascal_constant_definition_part163", None)
                if opp_val is None:
                    setattr(value, "pascal_constant_definition_part163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_constant_definition165(self):
        return self.__pascal_constant_definition165

    @pascal_constant_definition165.setter
    def pascal_constant_definition165(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant_definition__pascal_constant_definition165", None)
        self.__pascal_constant_definition165 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant166"):
                opp_val = getattr(old_value, "pascal_constant166", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant166", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant166"):
                opp_val = getattr(value, "pascal_constant166", None)
                setattr(value, "pascal_constant166", self)

class pascal_case_statement:

    pass
class pascal_if_statement:

    pass
class pascal_case_label_list:

    pass
class pascal_case_limb:

    pass
class pascal_for_statement:

    pass
class pascal_repeat_statement:

    pass
class pascal_while_statement:

    pass
class pascal_with_statement:

    pass
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
            if hasattr(old_value, "pascal_number77"):
                opp_val = getattr(old_value, "pascal_number77", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number77", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number77"):
                opp_val = getattr(value, "pascal_number77", None)
                setattr(value, "pascal_number77", self)

class pascal_conditional_statement:

    pass
class pascal_repetitive_statement:

    pass
class pascal_compound_statement:

    pass
class pascal_factor:

    def __init__(self, string: str, nil: bool, boolean: str, pascal_factor64: "pascal_number" = None, pascal_factor66: "pascal_set" = None, pascal_factor: "pascal_term" = None, pascal_factor61: "pascal_variable" = None, pascal_factor68: "pascal_function_designator" = None, pascal_factor71: "pascal_expression" = None, pascal_factor75: "pascal_factor" = None, pascal_factor73: "pascal_factor" = None):
        self.string = string
        self.nil = nil
        self.boolean = boolean
        self.pascal_factor64 = pascal_factor64
        self.pascal_factor66 = pascal_factor66
        self.pascal_factor = pascal_factor
        self.pascal_factor61 = pascal_factor61
        self.pascal_factor68 = pascal_factor68
        self.pascal_factor71 = pascal_factor71
        self.pascal_factor75 = pascal_factor75
        self.pascal_factor73 = pascal_factor73
        
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
    def boolean(self) -> str:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: str):
        self.__boolean = boolean

    @property
    def pascal_factor68(self):
        return self.__pascal_factor68

    @pascal_factor68.setter
    def pascal_factor68(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor68", None)
        self.__pascal_factor68 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_designator69"):
                opp_val = getattr(old_value, "pascal_function_designator69", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_designator69", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_designator69"):
                opp_val = getattr(value, "pascal_function_designator69", None)
                setattr(value, "pascal_function_designator69", self)

    @property
    def pascal_factor73(self):
        return self.__pascal_factor73

    @pascal_factor73.setter
    def pascal_factor73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor73", None)
        self.__pascal_factor73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor75"):
                opp_val = getattr(old_value, "pascal_factor75", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor75", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor75"):
                opp_val = getattr(value, "pascal_factor75", None)
                setattr(value, "pascal_factor75", self)

    @property
    def pascal_factor64(self):
        return self.__pascal_factor64

    @pascal_factor64.setter
    def pascal_factor64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor64", None)
        self.__pascal_factor64 = value
        
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
    def pascal_factor71(self):
        return self.__pascal_factor71

    @pascal_factor71.setter
    def pascal_factor71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor71", None)
        self.__pascal_factor71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression72"):
                opp_val = getattr(old_value, "pascal_expression72", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression72", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression72"):
                opp_val = getattr(value, "pascal_expression72", None)
                setattr(value, "pascal_expression72", self)

    @property
    def pascal_factor75(self):
        return self.__pascal_factor75

    @pascal_factor75.setter
    def pascal_factor75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor75", None)
        self.__pascal_factor75 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor73"):
                opp_val = getattr(old_value, "pascal_factor73", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor73"):
                opp_val = getattr(value, "pascal_factor73", None)
                setattr(value, "pascal_factor73", self)

    @property
    def pascal_factor66(self):
        return self.__pascal_factor66

    @pascal_factor66.setter
    def pascal_factor66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor66", None)
        self.__pascal_factor66 = value
        
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
    def pascal_factor61(self):
        return self.__pascal_factor61

    @pascal_factor61.setter
    def pascal_factor61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor61", None)
        self.__pascal_factor61 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable62"):
                opp_val = getattr(old_value, "pascal_variable62", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable62", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable62"):
                opp_val = getattr(value, "pascal_variable62", None)
                setattr(value, "pascal_variable62", self)

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

    def __init__(self, prefixOperator: str, operators: str, pascal_simple_expression: "pascal_expression" = None, pascal_simple_expression58: set["pascal_EObject"] = None):
        self.prefixOperator = prefixOperator
        self.operators = operators
        self.pascal_simple_expression = pascal_simple_expression
        self.pascal_simple_expression58 = pascal_simple_expression58 if pascal_simple_expression58 is not None else set()
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def prefixOperator(self) -> str:
        return self.__prefixOperator

    @prefixOperator.setter
    def prefixOperator(self, prefixOperator: str):
        self.__prefixOperator = prefixOperator

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
            if hasattr(old_value, "pascal_expression56"):
                opp_val = getattr(old_value, "pascal_expression56", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression56"):
                opp_val = getattr(value, "pascal_expression56", None)
                if opp_val is None:
                    setattr(value, "pascal_expression56", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_simple_expression58(self):
        return self.__pascal_simple_expression58

    @pascal_simple_expression58.setter
    def pascal_simple_expression58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_expression__pascal_simple_expression58", None)
        self.__pascal_simple_expression58 = value if value is not None else set()
        
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
                    

class pascal_set:

    def __init__(self, brackets: str, pascal_set: "pascal_factor" = None, pascal_set79: "pascal_expression_list" = None):
        self.brackets = brackets
        self.pascal_set = pascal_set
        self.pascal_set79 = pascal_set79
        
    @property
    def brackets(self) -> str:
        return self.__brackets

    @brackets.setter
    def brackets(self, brackets: str):
        self.__brackets = brackets

    @property
    def pascal_set(self):
        return self.__pascal_set

    @pascal_set.setter
    def pascal_set(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_set__pascal_set", None)
        self.__pascal_set = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor66"):
                opp_val = getattr(old_value, "pascal_factor66", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor66", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor66"):
                opp_val = getattr(value, "pascal_factor66", None)
                setattr(value, "pascal_factor66", self)

    @property
    def pascal_set79(self):
        return self.__pascal_set79

    @pascal_set79.setter
    def pascal_set79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_set__pascal_set79", None)
        self.__pascal_set79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list80"):
                opp_val = getattr(old_value, "pascal_expression_list80", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression_list80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list80"):
                opp_val = getattr(value, "pascal_expression_list80", None)
                setattr(value, "pascal_expression_list80", self)

class pascal_number:

    pass
class pascal_expression_list:

    pass
class pascal_var_:

    def __init__(self, accessor: bool, name: str, pascal_var_43: "pascal_var_" = None, pascal_var_48: "pascal_var_" = None, pascal_var_46: "pascal_var_" = None, pascal_var_51: "pascal_var_" = None, pascal_var_49: "pascal_var_" = None, pascal_var_: "pascal_variable" = None, pascal_var_42: "pascal_expression_list" = None, pascal_var_45: "pascal_var_" = None):
        self.accessor = accessor
        self.name = name
        self.pascal_var_43 = pascal_var_43
        self.pascal_var_48 = pascal_var_48
        self.pascal_var_46 = pascal_var_46
        self.pascal_var_51 = pascal_var_51
        self.pascal_var_49 = pascal_var_49
        self.pascal_var_ = pascal_var_
        self.pascal_var_42 = pascal_var_42
        self.pascal_var_45 = pascal_var_45
        
    @property
    def accessor(self) -> bool:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: bool):
        self.__accessor = accessor

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_var_45(self):
        return self.__pascal_var_45

    @pascal_var_45.setter
    def pascal_var_45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_var___pascal_var_45", None)
        self.__pascal_var_45 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_var_43"):
                opp_val = getattr(old_value, "pascal_var_43", None)
                if opp_val == self:
                    setattr(old_value, "pascal_var_43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_var_43"):
                opp_val = getattr(value, "pascal_var_43", None)
                setattr(value, "pascal_var_43", self)

    @property
    def pascal_var_43(self):
        return self.__pascal_var_43

    @pascal_var_43.setter
    def pascal_var_43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_var___pascal_var_43", None)
        self.__pascal_var_43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_var_45"):
                opp_val = getattr(old_value, "pascal_var_45", None)
                if opp_val == self:
                    setattr(old_value, "pascal_var_45", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_var_45"):
                opp_val = getattr(value, "pascal_var_45", None)
                setattr(value, "pascal_var_45", self)

    @property
    def pascal_var_42(self):
        return self.__pascal_var_42

    @pascal_var_42.setter
    def pascal_var_42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_var___pascal_var_42", None)
        self.__pascal_var_42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list"):
                opp_val = getattr(old_value, "pascal_expression_list", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression_list", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list"):
                opp_val = getattr(value, "pascal_expression_list", None)
                setattr(value, "pascal_expression_list", self)

    @property
    def pascal_var_(self):
        return self.__pascal_var_

    @pascal_var_.setter
    def pascal_var_(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_var___pascal_var_", None)
        self.__pascal_var_ = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable40"):
                opp_val = getattr(old_value, "pascal_variable40", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable40"):
                opp_val = getattr(value, "pascal_variable40", None)
                setattr(value, "pascal_variable40", self)

    @property
    def pascal_var_49(self):
        return self.__pascal_var_49

    @pascal_var_49.setter
    def pascal_var_49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_var___pascal_var_49", None)
        self.__pascal_var_49 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_var_51"):
                opp_val = getattr(old_value, "pascal_var_51", None)
                if opp_val == self:
                    setattr(old_value, "pascal_var_51", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_var_51"):
                opp_val = getattr(value, "pascal_var_51", None)
                setattr(value, "pascal_var_51", self)

    @property
    def pascal_var_51(self):
        return self.__pascal_var_51

    @pascal_var_51.setter
    def pascal_var_51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_var___pascal_var_51", None)
        self.__pascal_var_51 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_var_49"):
                opp_val = getattr(old_value, "pascal_var_49", None)
                if opp_val == self:
                    setattr(old_value, "pascal_var_49", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_var_49"):
                opp_val = getattr(value, "pascal_var_49", None)
                setattr(value, "pascal_var_49", self)

    @property
    def pascal_var_48(self):
        return self.__pascal_var_48

    @pascal_var_48.setter
    def pascal_var_48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_var___pascal_var_48", None)
        self.__pascal_var_48 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_var_46"):
                opp_val = getattr(old_value, "pascal_var_46", None)
                if opp_val == self:
                    setattr(old_value, "pascal_var_46", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_var_46"):
                opp_val = getattr(value, "pascal_var_46", None)
                setattr(value, "pascal_var_46", self)

    @property
    def pascal_var_46(self):
        return self.__pascal_var_46

    @pascal_var_46.setter
    def pascal_var_46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_var___pascal_var_46", None)
        self.__pascal_var_46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_var_48"):
                opp_val = getattr(old_value, "pascal_var_48", None)
                if opp_val == self:
                    setattr(old_value, "pascal_var_48", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_var_48"):
                opp_val = getattr(value, "pascal_var_48", None)
                setattr(value, "pascal_var_48", self)

class pascal_expression:

    def __init__(self, operators: str, pascal_expression: "pascal_assignment_statement" = None, pascal_expression54: "pascal_expression_list" = None, pascal_expression56: set["pascal_simple_expression"] = None, pascal_expression72: "pascal_factor" = None, pascal_expression112: "pascal_repeat_statement" = None, pascal_expression103: "pascal_while_statement" = None, pascal_expression137: "pascal_case_statement" = None, pascal_expression118: "pascal_for_statement" = None, pascal_expression128: "pascal_if_statement" = None):
        self.operators = operators
        self.pascal_expression = pascal_expression
        self.pascal_expression54 = pascal_expression54
        self.pascal_expression56 = pascal_expression56 if pascal_expression56 is not None else set()
        self.pascal_expression72 = pascal_expression72
        self.pascal_expression112 = pascal_expression112
        self.pascal_expression103 = pascal_expression103
        self.pascal_expression137 = pascal_expression137
        self.pascal_expression118 = pascal_expression118
        self.pascal_expression128 = pascal_expression128
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def pascal_expression54(self):
        return self.__pascal_expression54

    @pascal_expression54.setter
    def pascal_expression54(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression54", None)
        self.__pascal_expression54 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list53"):
                opp_val = getattr(old_value, "pascal_expression_list53", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list53"):
                opp_val = getattr(value, "pascal_expression_list53", None)
                if opp_val is None:
                    setattr(value, "pascal_expression_list53", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_expression137(self):
        return self.__pascal_expression137

    @pascal_expression137.setter
    def pascal_expression137(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression137", None)
        self.__pascal_expression137 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_case_statement136"):
                opp_val = getattr(old_value, "pascal_case_statement136", None)
                if opp_val == self:
                    setattr(old_value, "pascal_case_statement136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_statement136"):
                opp_val = getattr(value, "pascal_case_statement136", None)
                setattr(value, "pascal_case_statement136", self)

    @property
    def pascal_expression56(self):
        return self.__pascal_expression56

    @pascal_expression56.setter
    def pascal_expression56(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression56", None)
        self.__pascal_expression56 = value if value is not None else set()
        
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
    def pascal_expression118(self):
        return self.__pascal_expression118

    @pascal_expression118.setter
    def pascal_expression118(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression118", None)
        self.__pascal_expression118 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_for_statement117"):
                opp_val = getattr(old_value, "pascal_for_statement117", None)
                if opp_val == self:
                    setattr(old_value, "pascal_for_statement117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_for_statement117"):
                opp_val = getattr(value, "pascal_for_statement117", None)
                setattr(value, "pascal_for_statement117", self)

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
            if hasattr(old_value, "pascal_assignment_statement38"):
                opp_val = getattr(old_value, "pascal_assignment_statement38", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement38"):
                opp_val = getattr(value, "pascal_assignment_statement38", None)
                setattr(value, "pascal_assignment_statement38", self)

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
            if hasattr(old_value, "pascal_factor71"):
                opp_val = getattr(old_value, "pascal_factor71", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor71"):
                opp_val = getattr(value, "pascal_factor71", None)
                setattr(value, "pascal_factor71", self)

    @property
    def pascal_expression103(self):
        return self.__pascal_expression103

    @pascal_expression103.setter
    def pascal_expression103(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression103", None)
        self.__pascal_expression103 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_while_statement102"):
                opp_val = getattr(old_value, "pascal_while_statement102", None)
                if opp_val == self:
                    setattr(old_value, "pascal_while_statement102", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_while_statement102"):
                opp_val = getattr(value, "pascal_while_statement102", None)
                setattr(value, "pascal_while_statement102", self)

    @property
    def pascal_expression128(self):
        return self.__pascal_expression128

    @pascal_expression128.setter
    def pascal_expression128(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression128", None)
        self.__pascal_expression128 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_if_statement127"):
                opp_val = getattr(old_value, "pascal_if_statement127", None)
                if opp_val == self:
                    setattr(old_value, "pascal_if_statement127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_if_statement127"):
                opp_val = getattr(value, "pascal_if_statement127", None)
                setattr(value, "pascal_if_statement127", self)

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
            if hasattr(old_value, "pascal_repeat_statement111"):
                opp_val = getattr(old_value, "pascal_repeat_statement111", None)
                if opp_val == self:
                    setattr(old_value, "pascal_repeat_statement111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_repeat_statement111"):
                opp_val = getattr(value, "pascal_repeat_statement111", None)
                setattr(value, "pascal_repeat_statement111", self)

class pascal_variable:

    def __init__(self, name: str, pascal_variable: "pascal_assignment_statement" = None, pascal_variable40: "pascal_var_" = None, pascal_variable62: "pascal_factor" = None, pascal_variable152: "pascal_with_statement" = None):
        self.name = name
        self.pascal_variable = pascal_variable
        self.pascal_variable40 = pascal_variable40
        self.pascal_variable62 = pascal_variable62
        self.pascal_variable152 = pascal_variable152
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_variable152(self):
        return self.__pascal_variable152

    @pascal_variable152.setter
    def pascal_variable152(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable152", None)
        self.__pascal_variable152 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_with_statement151"):
                opp_val = getattr(old_value, "pascal_with_statement151", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_with_statement151"):
                opp_val = getattr(value, "pascal_with_statement151", None)
                if opp_val is None:
                    setattr(value, "pascal_with_statement151", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "pascal_assignment_statement36"):
                opp_val = getattr(old_value, "pascal_assignment_statement36", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement36"):
                opp_val = getattr(value, "pascal_assignment_statement36", None)
                setattr(value, "pascal_assignment_statement36", self)

    @property
    def pascal_variable62(self):
        return self.__pascal_variable62

    @pascal_variable62.setter
    def pascal_variable62(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable62", None)
        self.__pascal_variable62 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor61"):
                opp_val = getattr(old_value, "pascal_factor61", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor61"):
                opp_val = getattr(value, "pascal_factor61", None)
                setattr(value, "pascal_factor61", self)

    @property
    def pascal_variable40(self):
        return self.__pascal_variable40

    @pascal_variable40.setter
    def pascal_variable40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable40", None)
        self.__pascal_variable40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_var_"):
                opp_val = getattr(old_value, "pascal_var_", None)
                if opp_val == self:
                    setattr(old_value, "pascal_var_", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_var_"):
                opp_val = getattr(value, "pascal_var_", None)
                setattr(value, "pascal_var_", self)

class pascal_structured_statement:

    pass
class pascal_simple_statement:

    def __init__(self, function_noargs: str, pascal_simple_statement30: "pascal_assignment_statement" = None, pascal_simple_statement32: "pascal_function_designator" = None, pascal_simple_statement34: "pascal_goto_statement" = None, pascal_simple_statement: "pascal_statement" = None):
        self.function_noargs = function_noargs
        self.pascal_simple_statement30 = pascal_simple_statement30
        self.pascal_simple_statement32 = pascal_simple_statement32
        self.pascal_simple_statement34 = pascal_simple_statement34
        self.pascal_simple_statement = pascal_simple_statement
        
    @property
    def function_noargs(self) -> str:
        return self.__function_noargs

    @function_noargs.setter
    def function_noargs(self, function_noargs: str):
        self.__function_noargs = function_noargs

    @property
    def pascal_simple_statement32(self):
        return self.__pascal_simple_statement32

    @pascal_simple_statement32.setter
    def pascal_simple_statement32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement32", None)
        self.__pascal_simple_statement32 = value
        
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
    def pascal_simple_statement34(self):
        return self.__pascal_simple_statement34

    @pascal_simple_statement34.setter
    def pascal_simple_statement34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement34", None)
        self.__pascal_simple_statement34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_goto_statement"):
                opp_val = getattr(old_value, "pascal_goto_statement", None)
                if opp_val == self:
                    setattr(old_value, "pascal_goto_statement", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_goto_statement"):
                opp_val = getattr(value, "pascal_goto_statement", None)
                setattr(value, "pascal_goto_statement", self)

    @property
    def pascal_simple_statement30(self):
        return self.__pascal_simple_statement30

    @pascal_simple_statement30.setter
    def pascal_simple_statement30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement30", None)
        self.__pascal_simple_statement30 = value
        
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
    def pascal_simple_statement(self):
        return self.__pascal_simple_statement

    @pascal_simple_statement.setter
    def pascal_simple_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement", None)
        self.__pascal_simple_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_statement26"):
                opp_val = getattr(old_value, "pascal_statement26", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement26"):
                opp_val = getattr(value, "pascal_statement26", None)
                setattr(value, "pascal_statement26", self)

class pascal_label:

    def __init__(self, number: str, pascal_label: "pascal_statement" = None, pascal_label158: "pascal_goto_statement" = None, pascal_label161: "pascal_label_declaration_part" = None):
        self.number = number
        self.pascal_label = pascal_label
        self.pascal_label158 = pascal_label158
        self.pascal_label161 = pascal_label161
        
    @property
    def number(self) -> str:
        return self.__number

    @number.setter
    def number(self, number: str):
        self.__number = number

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
            if hasattr(old_value, "pascal_statement24"):
                opp_val = getattr(old_value, "pascal_statement24", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement24"):
                opp_val = getattr(value, "pascal_statement24", None)
                setattr(value, "pascal_statement24", self)

    @property
    def pascal_label158(self):
        return self.__pascal_label158

    @pascal_label158.setter
    def pascal_label158(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_label__pascal_label158", None)
        self.__pascal_label158 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_goto_statement157"):
                opp_val = getattr(old_value, "pascal_goto_statement157", None)
                if opp_val == self:
                    setattr(old_value, "pascal_goto_statement157", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_goto_statement157"):
                opp_val = getattr(value, "pascal_goto_statement157", None)
                setattr(value, "pascal_goto_statement157", self)

    @property
    def pascal_label161(self):
        return self.__pascal_label161

    @pascal_label161.setter
    def pascal_label161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_label__pascal_label161", None)
        self.__pascal_label161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_label_declaration_part160"):
                opp_val = getattr(old_value, "pascal_label_declaration_part160", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_label_declaration_part160"):
                opp_val = getattr(value, "pascal_label_declaration_part160", None)
                if opp_val is None:
                    setattr(value, "pascal_label_declaration_part160", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_statement:

    pass
class pascal_statement_sequence:

    pass
class pascal_statement_part:

    pass
class pascal_procedure_and_function_declaration_part:

    pass
class pascal_goto_statement:

    pass
class pascal_function_designator:

    def __init__(self, name: str, pascal_function_designator: "pascal_simple_statement" = None, pascal_function_designator82: "pascal_expression_list" = None, pascal_function_designator69: "pascal_factor" = None):
        self.name = name
        self.pascal_function_designator = pascal_function_designator
        self.pascal_function_designator82 = pascal_function_designator82
        self.pascal_function_designator69 = pascal_function_designator69
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_function_designator69(self):
        return self.__pascal_function_designator69

    @pascal_function_designator69.setter
    def pascal_function_designator69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator69", None)
        self.__pascal_function_designator69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor68"):
                opp_val = getattr(old_value, "pascal_factor68", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor68"):
                opp_val = getattr(value, "pascal_factor68", None)
                setattr(value, "pascal_factor68", self)

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
            if hasattr(old_value, "pascal_simple_statement32"):
                opp_val = getattr(old_value, "pascal_simple_statement32", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simple_statement32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_statement32"):
                opp_val = getattr(value, "pascal_simple_statement32", None)
                setattr(value, "pascal_simple_statement32", self)

    @property
    def pascal_function_designator82(self):
        return self.__pascal_function_designator82

    @pascal_function_designator82.setter
    def pascal_function_designator82(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator82", None)
        self.__pascal_function_designator82 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list83"):
                opp_val = getattr(old_value, "pascal_expression_list83", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression_list83", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list83"):
                opp_val = getattr(value, "pascal_expression_list83", None)
                setattr(value, "pascal_expression_list83", self)

class pascal_assignment_statement:

    pass
class pascal_identifier_list:

    def __init__(self, names: str, pascal_identifier_list: "pascal_program_heading_block" = None, pascal_identifier_list192: "pascal_enumerated_type" = None, pascal_identifier_list230: "pascal_record_section" = None, pascal_identifier_list301: "pascal_variable_parameter_section" = None, pascal_identifier_list282: "pascal_value_parameter_section" = None):
        self.names = names
        self.pascal_identifier_list = pascal_identifier_list
        self.pascal_identifier_list192 = pascal_identifier_list192
        self.pascal_identifier_list230 = pascal_identifier_list230
        self.pascal_identifier_list301 = pascal_identifier_list301
        self.pascal_identifier_list282 = pascal_identifier_list282
        
    @property
    def names(self) -> str:
        return self.__names

    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def pascal_identifier_list230(self):
        return self.__pascal_identifier_list230

    @pascal_identifier_list230.setter
    def pascal_identifier_list230(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list230", None)
        self.__pascal_identifier_list230 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_record_section229"):
                opp_val = getattr(old_value, "pascal_record_section229", None)
                if opp_val == self:
                    setattr(old_value, "pascal_record_section229", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_record_section229"):
                opp_val = getattr(value, "pascal_record_section229", None)
                setattr(value, "pascal_record_section229", self)

    @property
    def pascal_identifier_list282(self):
        return self.__pascal_identifier_list282

    @pascal_identifier_list282.setter
    def pascal_identifier_list282(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list282", None)
        self.__pascal_identifier_list282 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_value_parameter_section281"):
                opp_val = getattr(old_value, "pascal_value_parameter_section281", None)
                if opp_val == self:
                    setattr(old_value, "pascal_value_parameter_section281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_value_parameter_section281"):
                opp_val = getattr(value, "pascal_value_parameter_section281", None)
                setattr(value, "pascal_value_parameter_section281", self)

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
            if hasattr(old_value, "pascal_program_heading_block6"):
                opp_val = getattr(old_value, "pascal_program_heading_block6", None)
                if opp_val == self:
                    setattr(old_value, "pascal_program_heading_block6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_program_heading_block6"):
                opp_val = getattr(value, "pascal_program_heading_block6", None)
                setattr(value, "pascal_program_heading_block6", self)

    @property
    def pascal_identifier_list301(self):
        return self.__pascal_identifier_list301

    @pascal_identifier_list301.setter
    def pascal_identifier_list301(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list301", None)
        self.__pascal_identifier_list301 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_parameter_section300"):
                opp_val = getattr(old_value, "pascal_variable_parameter_section300", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_parameter_section300", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_parameter_section300"):
                opp_val = getattr(value, "pascal_variable_parameter_section300", None)
                setattr(value, "pascal_variable_parameter_section300", self)

    @property
    def pascal_identifier_list192(self):
        return self.__pascal_identifier_list192

    @pascal_identifier_list192.setter
    def pascal_identifier_list192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list192", None)
        self.__pascal_identifier_list192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_enumerated_type191"):
                opp_val = getattr(old_value, "pascal_enumerated_type191", None)
                if opp_val == self:
                    setattr(old_value, "pascal_enumerated_type191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_enumerated_type191"):
                opp_val = getattr(value, "pascal_enumerated_type191", None)
                setattr(value, "pascal_enumerated_type191", self)

class pascal_block:

    pass
class pascal_program_heading_block:

    def __init__(self, name: str, pascal_program_heading_block: "pascal_program" = None, pascal_program_heading_block6: "pascal_identifier_list" = None):
        self.name = name
        self.pascal_program_heading_block = pascal_program_heading_block
        self.pascal_program_heading_block6 = pascal_program_heading_block6
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_program_heading_block6(self):
        return self.__pascal_program_heading_block6

    @pascal_program_heading_block6.setter
    def pascal_program_heading_block6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_program_heading_block__pascal_program_heading_block6", None)
        self.__pascal_program_heading_block6 = value
        
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
    def pascal_program_heading_block(self):
        return self.__pascal_program_heading_block

    @pascal_program_heading_block.setter
    def pascal_program_heading_block(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_program_heading_block__pascal_program_heading_block", None)
        self.__pascal_program_heading_block = value
        
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

class pascal_program:

    pass
class pascal_pascal:

    pass
class pascal_variable_declaration_part:

    pass
class pascal_type_definition_part:

    pass
class pascal_constant_definition_part:

    pass
class pascal_label_declaration_part:

    pass