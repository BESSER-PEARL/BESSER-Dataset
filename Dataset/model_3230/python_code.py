from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pascal_any_number:

    def __init__(self, integer: str, real: str, pascal_any_number: "pascal_number" = None):
        self.integer = integer
        self.real = real
        self.pascal_any_number = pascal_any_number
        
    @property
    def integer(self) -> str:
        return self.__integer

    @integer.setter
    def integer(self, integer: str):
        self.__integer = integer

    @property
    def real(self) -> str:
        return self.__real

    @real.setter
    def real(self, real: str):
        self.__real = real

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
            if hasattr(old_value, "pascal_number275"):
                opp_val = getattr(old_value, "pascal_number275", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number275"):
                opp_val = getattr(value, "pascal_number275", None)
                setattr(value, "pascal_number275", self)

class pascal_case_label_list:

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
            if hasattr(old_value, "pascal_variant_part266"):
                opp_val = getattr(old_value, "pascal_variant_part266", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variant_part266", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variant_part266"):
                opp_val = getattr(value, "pascal_variant_part266", None)
                setattr(value, "pascal_variant_part266", self)

class pascal_record_section:

    pass
class pascal_variant_part:

    def __init__(self, name: str, pascal_variant_part: "pascal_field_list" = None, pascal_variant_part266: "pascal_tag_field" = None, pascal_variant_part268: set["pascal_variant"] = None):
        self.name = name
        self.pascal_variant_part = pascal_variant_part
        self.pascal_variant_part266 = pascal_variant_part266
        self.pascal_variant_part268 = pascal_variant_part268 if pascal_variant_part268 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "pascal_field_list256"):
                opp_val = getattr(old_value, "pascal_field_list256", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_field_list256"):
                opp_val = getattr(value, "pascal_field_list256", None)
                if opp_val is None:
                    setattr(value, "pascal_field_list256", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_variant_part266(self):
        return self.__pascal_variant_part266

    @pascal_variant_part266.setter
    def pascal_variant_part266(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part266", None)
        self.__pascal_variant_part266 = value
        
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
    def pascal_variant_part268(self):
        return self.__pascal_variant_part268

    @pascal_variant_part268.setter
    def pascal_variant_part268(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part268", None)
        self.__pascal_variant_part268 = value if value is not None else set()
        
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
                    

class pascal_fixed_part:

    pass
class pascal_field_list:

    pass
class pascal_file_type:

    pass
class pascal_set_type:

    pass
class pascal_record_type:

    def __init__(self, record: str, end: str, pascal_record_type: "pascal_unpacked_structured_type" = None, pascal_record_type243: "pascal_field_list" = None):
        self.record = record
        self.end = end
        self.pascal_record_type = pascal_record_type
        self.pascal_record_type243 = pascal_record_type243
        
    @property
    def record(self) -> str:
        return self.__record

    @record.setter
    def record(self, record: str):
        self.__record = record

    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

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
            if hasattr(old_value, "pascal_unpacked_structured_type231"):
                opp_val = getattr(old_value, "pascal_unpacked_structured_type231", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unpacked_structured_type231", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_structured_type231"):
                opp_val = getattr(value, "pascal_unpacked_structured_type231", None)
                setattr(value, "pascal_unpacked_structured_type231", self)

    @property
    def pascal_record_type243(self):
        return self.__pascal_record_type243

    @pascal_record_type243.setter
    def pascal_record_type243(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_record_type__pascal_record_type243", None)
        self.__pascal_record_type243 = value
        
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

class pascal_array_type:

    pass
class pascal_unpacked_structured_type:

    pass
class pascal_enumerated_type:

    pass
class pascal_subrange_type:

    def __init__(self, subrange: str, pascal_subrange_type: "pascal_simple_type" = None, pascal_subrange_type218: "pascal_constant" = None, pascal_subrange_type221: "pascal_constant" = None, pascal_subrange_type224: "pascal_constant" = None):
        self.subrange = subrange
        self.pascal_subrange_type = pascal_subrange_type
        self.pascal_subrange_type218 = pascal_subrange_type218
        self.pascal_subrange_type221 = pascal_subrange_type221
        self.pascal_subrange_type224 = pascal_subrange_type224
        
    @property
    def subrange(self) -> str:
        return self.__subrange

    @subrange.setter
    def subrange(self, subrange: str):
        self.__subrange = subrange

    @property
    def pascal_subrange_type221(self):
        return self.__pascal_subrange_type221

    @pascal_subrange_type221.setter
    def pascal_subrange_type221(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type221", None)
        self.__pascal_subrange_type221 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant222"):
                opp_val = getattr(old_value, "pascal_constant222", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant222"):
                opp_val = getattr(value, "pascal_constant222", None)
                setattr(value, "pascal_constant222", self)

    @property
    def pascal_subrange_type218(self):
        return self.__pascal_subrange_type218

    @pascal_subrange_type218.setter
    def pascal_subrange_type218(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type218", None)
        self.__pascal_subrange_type218 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant219"):
                opp_val = getattr(old_value, "pascal_constant219", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant219", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant219"):
                opp_val = getattr(value, "pascal_constant219", None)
                setattr(value, "pascal_constant219", self)

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
            if hasattr(old_value, "pascal_simple_type211"):
                opp_val = getattr(old_value, "pascal_simple_type211", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simple_type211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_type211"):
                opp_val = getattr(value, "pascal_simple_type211", None)
                setattr(value, "pascal_simple_type211", self)

    @property
    def pascal_subrange_type224(self):
        return self.__pascal_subrange_type224

    @pascal_subrange_type224.setter
    def pascal_subrange_type224(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type224", None)
        self.__pascal_subrange_type224 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant225"):
                opp_val = getattr(old_value, "pascal_constant225", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant225", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant225"):
                opp_val = getattr(value, "pascal_constant225", None)
                setattr(value, "pascal_constant225", self)

class pascal_pointer_type:

    pass
class pascal_structured_type:

    def __init__(self, packed: bool, pascal_structured_type: "pascal_type" = None, pascal_structured_type227: "pascal_unpacked_structured_type" = None):
        self.packed = packed
        self.pascal_structured_type = pascal_structured_type
        self.pascal_structured_type227 = pascal_structured_type227
        
    @property
    def packed(self) -> bool:
        return self.__packed

    @packed.setter
    def packed(self, packed: bool):
        self.__packed = packed

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
            if hasattr(old_value, "pascal_type207"):
                opp_val = getattr(old_value, "pascal_type207", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type207"):
                opp_val = getattr(value, "pascal_type207", None)
                setattr(value, "pascal_type207", self)

    @property
    def pascal_structured_type227(self):
        return self.__pascal_structured_type227

    @pascal_structured_type227.setter
    def pascal_structured_type227(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_structured_type__pascal_structured_type227", None)
        self.__pascal_structured_type227 = value
        
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

class pascal_simple_type:

    def __init__(self, name: str, pascal_simple_type: "pascal_type" = None, pascal_simple_type211: "pascal_subrange_type" = None, pascal_simple_type213: "pascal_enumerated_type" = None, pascal_simple_type238: "pascal_array_type" = None):
        self.name = name
        self.pascal_simple_type = pascal_simple_type
        self.pascal_simple_type211 = pascal_simple_type211
        self.pascal_simple_type213 = pascal_simple_type213
        self.pascal_simple_type238 = pascal_simple_type238
        
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
            if hasattr(old_value, "pascal_type205"):
                opp_val = getattr(old_value, "pascal_type205", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type205", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type205"):
                opp_val = getattr(value, "pascal_type205", None)
                setattr(value, "pascal_type205", self)

    @property
    def pascal_simple_type211(self):
        return self.__pascal_simple_type211

    @pascal_simple_type211.setter
    def pascal_simple_type211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type211", None)
        self.__pascal_simple_type211 = value
        
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
    def pascal_simple_type238(self):
        return self.__pascal_simple_type238

    @pascal_simple_type238.setter
    def pascal_simple_type238(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type238", None)
        self.__pascal_simple_type238 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_array_type237"):
                opp_val = getattr(old_value, "pascal_array_type237", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_array_type237"):
                opp_val = getattr(value, "pascal_array_type237", None)
                if opp_val is None:
                    setattr(value, "pascal_array_type237", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_simple_type213(self):
        return self.__pascal_simple_type213

    @pascal_simple_type213.setter
    def pascal_simple_type213(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type213", None)
        self.__pascal_simple_type213 = value
        
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

class pascal_set:

    def __init__(self, brackets: str, pascal_set: "pascal_factor" = None, pascal_set196: "pascal_expression_list" = None):
        self.brackets = brackets
        self.pascal_set = pascal_set
        self.pascal_set196 = pascal_set196
        
    @property
    def brackets(self) -> str:
        return self.__brackets

    @brackets.setter
    def brackets(self, brackets: str):
        self.__brackets = brackets

    @property
    def pascal_set196(self):
        return self.__pascal_set196

    @pascal_set196.setter
    def pascal_set196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_set__pascal_set196", None)
        self.__pascal_set196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list197"):
                opp_val = getattr(old_value, "pascal_expression_list197", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression_list197", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list197"):
                opp_val = getattr(value, "pascal_expression_list197", None)
                setattr(value, "pascal_expression_list197", self)

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
            if hasattr(old_value, "pascal_factor172"):
                opp_val = getattr(old_value, "pascal_factor172", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor172", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor172"):
                opp_val = getattr(value, "pascal_factor172", None)
                setattr(value, "pascal_factor172", self)

class pascal_number:

    pass
class pascal_factor:

    def __init__(self, nil: bool, boolean: str, string: str, pascal_factor172: "pascal_set" = None, pascal_factor174: "pascal_function_designator" = None, pascal_factor177: "pascal_expression" = None, pascal_factor181: "pascal_factor" = None, pascal_factor179: "pascal_factor" = None, pascal_factor: "pascal_term" = None, pascal_factor167: "pascal_variable" = None, pascal_factor170: "pascal_number" = None):
        self.nil = nil
        self.boolean = boolean
        self.string = string
        self.pascal_factor172 = pascal_factor172
        self.pascal_factor174 = pascal_factor174
        self.pascal_factor177 = pascal_factor177
        self.pascal_factor181 = pascal_factor181
        self.pascal_factor179 = pascal_factor179
        self.pascal_factor = pascal_factor
        self.pascal_factor167 = pascal_factor167
        self.pascal_factor170 = pascal_factor170
        
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
    def pascal_factor181(self):
        return self.__pascal_factor181

    @pascal_factor181.setter
    def pascal_factor181(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor181", None)
        self.__pascal_factor181 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor179"):
                opp_val = getattr(old_value, "pascal_factor179", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor179", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor179"):
                opp_val = getattr(value, "pascal_factor179", None)
                setattr(value, "pascal_factor179", self)

    @property
    def pascal_factor170(self):
        return self.__pascal_factor170

    @pascal_factor170.setter
    def pascal_factor170(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor170", None)
        self.__pascal_factor170 = value
        
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
    def pascal_factor174(self):
        return self.__pascal_factor174

    @pascal_factor174.setter
    def pascal_factor174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor174", None)
        self.__pascal_factor174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_designator175"):
                opp_val = getattr(old_value, "pascal_function_designator175", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_designator175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_designator175"):
                opp_val = getattr(value, "pascal_function_designator175", None)
                setattr(value, "pascal_function_designator175", self)

    @property
    def pascal_factor167(self):
        return self.__pascal_factor167

    @pascal_factor167.setter
    def pascal_factor167(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor167", None)
        self.__pascal_factor167 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable168"):
                opp_val = getattr(old_value, "pascal_variable168", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable168", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable168"):
                opp_val = getattr(value, "pascal_variable168", None)
                setattr(value, "pascal_variable168", self)

    @property
    def pascal_factor172(self):
        return self.__pascal_factor172

    @pascal_factor172.setter
    def pascal_factor172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor172", None)
        self.__pascal_factor172 = value
        
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
    def pascal_factor177(self):
        return self.__pascal_factor177

    @pascal_factor177.setter
    def pascal_factor177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor177", None)
        self.__pascal_factor177 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression178"):
                opp_val = getattr(old_value, "pascal_expression178", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression178", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression178"):
                opp_val = getattr(value, "pascal_expression178", None)
                setattr(value, "pascal_expression178", self)

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

    @property
    def pascal_factor179(self):
        return self.__pascal_factor179

    @pascal_factor179.setter
    def pascal_factor179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor179", None)
        self.__pascal_factor179 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor181"):
                opp_val = getattr(old_value, "pascal_factor181", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor181", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor181"):
                opp_val = getattr(value, "pascal_factor181", None)
                setattr(value, "pascal_factor181", self)

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
class pascal_expression_list:

    pass
class pascal_simple_expression:

    def __init__(self, prefixOperator: str, operators: str, pascal_simple_expression: "pascal_expression" = None, pascal_simple_expression164: set["pascal_EObject"] = None):
        self.prefixOperator = prefixOperator
        self.operators = operators
        self.pascal_simple_expression = pascal_simple_expression
        self.pascal_simple_expression164 = pascal_simple_expression164 if pascal_simple_expression164 is not None else set()
        
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
    def pascal_simple_expression164(self):
        return self.__pascal_simple_expression164

    @pascal_simple_expression164.setter
    def pascal_simple_expression164(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_expression__pascal_simple_expression164", None)
        self.__pascal_simple_expression164 = value if value is not None else set()
        
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
            if hasattr(old_value, "pascal_expression162"):
                opp_val = getattr(old_value, "pascal_expression162", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression162"):
                opp_val = getattr(value, "pascal_expression162", None)
                if opp_val is None:
                    setattr(value, "pascal_expression162", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_resto:

    def __init__(self, accessor: bool, name: str, pascal_resto: "pascal_variable" = None, pascal_resto185: "pascal_expression_list" = None, pascal_resto188: "pascal_resto" = None, pascal_resto186: "pascal_resto" = None, pascal_resto191: "pascal_resto" = None, pascal_resto189: "pascal_resto" = None, pascal_resto194: "pascal_resto" = None, pascal_resto192: "pascal_resto" = None):
        self.accessor = accessor
        self.name = name
        self.pascal_resto = pascal_resto
        self.pascal_resto185 = pascal_resto185
        self.pascal_resto188 = pascal_resto188
        self.pascal_resto186 = pascal_resto186
        self.pascal_resto191 = pascal_resto191
        self.pascal_resto189 = pascal_resto189
        self.pascal_resto194 = pascal_resto194
        self.pascal_resto192 = pascal_resto192
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def accessor(self) -> bool:
        return self.__accessor

    @accessor.setter
    def accessor(self, accessor: bool):
        self.__accessor = accessor

    @property
    def pascal_resto(self):
        return self.__pascal_resto

    @pascal_resto.setter
    def pascal_resto(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto", None)
        self.__pascal_resto = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable183"):
                opp_val = getattr(old_value, "pascal_variable183", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable183", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable183"):
                opp_val = getattr(value, "pascal_variable183", None)
                setattr(value, "pascal_variable183", self)

    @property
    def pascal_resto186(self):
        return self.__pascal_resto186

    @pascal_resto186.setter
    def pascal_resto186(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto186", None)
        self.__pascal_resto186 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto188"):
                opp_val = getattr(old_value, "pascal_resto188", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto188", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto188"):
                opp_val = getattr(value, "pascal_resto188", None)
                setattr(value, "pascal_resto188", self)

    @property
    def pascal_resto188(self):
        return self.__pascal_resto188

    @pascal_resto188.setter
    def pascal_resto188(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto188", None)
        self.__pascal_resto188 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto186"):
                opp_val = getattr(old_value, "pascal_resto186", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto186", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto186"):
                opp_val = getattr(value, "pascal_resto186", None)
                setattr(value, "pascal_resto186", self)

    @property
    def pascal_resto189(self):
        return self.__pascal_resto189

    @pascal_resto189.setter
    def pascal_resto189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto189", None)
        self.__pascal_resto189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto191"):
                opp_val = getattr(old_value, "pascal_resto191", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto191", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto191"):
                opp_val = getattr(value, "pascal_resto191", None)
                setattr(value, "pascal_resto191", self)

    @property
    def pascal_resto192(self):
        return self.__pascal_resto192

    @pascal_resto192.setter
    def pascal_resto192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto192", None)
        self.__pascal_resto192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto194"):
                opp_val = getattr(old_value, "pascal_resto194", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto194"):
                opp_val = getattr(value, "pascal_resto194", None)
                setattr(value, "pascal_resto194", self)

    @property
    def pascal_resto185(self):
        return self.__pascal_resto185

    @pascal_resto185.setter
    def pascal_resto185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto185", None)
        self.__pascal_resto185 = value
        
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
    def pascal_resto194(self):
        return self.__pascal_resto194

    @pascal_resto194.setter
    def pascal_resto194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto194", None)
        self.__pascal_resto194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto192"):
                opp_val = getattr(old_value, "pascal_resto192", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto192"):
                opp_val = getattr(value, "pascal_resto192", None)
                setattr(value, "pascal_resto192", self)

    @property
    def pascal_resto191(self):
        return self.__pascal_resto191

    @pascal_resto191.setter
    def pascal_resto191(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto191", None)
        self.__pascal_resto191 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto189"):
                opp_val = getattr(old_value, "pascal_resto189", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto189"):
                opp_val = getattr(value, "pascal_resto189", None)
                setattr(value, "pascal_resto189", self)

class pascal_if_statement:

    pass
class pascal_for_statement:

    def __init__(self, initID: str, pascal_for_statement: "pascal_repetitive_statement" = None, pascal_for_statement139: "pascal_expression" = None, pascal_for_statement142: "pascal_expression" = None, pascal_for_statement145: "pascal_statement" = None):
        self.initID = initID
        self.pascal_for_statement = pascal_for_statement
        self.pascal_for_statement139 = pascal_for_statement139
        self.pascal_for_statement142 = pascal_for_statement142
        self.pascal_for_statement145 = pascal_for_statement145
        
    @property
    def initID(self) -> str:
        return self.__initID

    @initID.setter
    def initID(self, initID: str):
        self.__initID = initID

    @property
    def pascal_for_statement145(self):
        return self.__pascal_for_statement145

    @pascal_for_statement145.setter
    def pascal_for_statement145(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_for_statement__pascal_for_statement145", None)
        self.__pascal_for_statement145 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_statement146"):
                opp_val = getattr(old_value, "pascal_statement146", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement146", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement146"):
                opp_val = getattr(value, "pascal_statement146", None)
                setattr(value, "pascal_statement146", self)

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
            if hasattr(old_value, "pascal_repetitive_statement125"):
                opp_val = getattr(old_value, "pascal_repetitive_statement125", None)
                if opp_val == self:
                    setattr(old_value, "pascal_repetitive_statement125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_repetitive_statement125"):
                opp_val = getattr(value, "pascal_repetitive_statement125", None)
                setattr(value, "pascal_repetitive_statement125", self)

    @property
    def pascal_for_statement142(self):
        return self.__pascal_for_statement142

    @pascal_for_statement142.setter
    def pascal_for_statement142(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_for_statement__pascal_for_statement142", None)
        self.__pascal_for_statement142 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression143"):
                opp_val = getattr(old_value, "pascal_expression143", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression143", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression143"):
                opp_val = getattr(value, "pascal_expression143", None)
                setattr(value, "pascal_expression143", self)

    @property
    def pascal_for_statement139(self):
        return self.__pascal_for_statement139

    @pascal_for_statement139.setter
    def pascal_for_statement139(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_for_statement__pascal_for_statement139", None)
        self.__pascal_for_statement139 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression140"):
                opp_val = getattr(old_value, "pascal_expression140", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression140", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression140"):
                opp_val = getattr(value, "pascal_expression140", None)
                setattr(value, "pascal_expression140", self)

class pascal_repeat_statement:

    pass
class pascal_while_statement:

    pass
class pascal_with_statement:

    def __init__(self, record: str, records: str, pascal_with_statement: "pascal_structured_statement" = None, pascal_with_statement159: "pascal_statement" = None):
        self.record = record
        self.records = records
        self.pascal_with_statement = pascal_with_statement
        self.pascal_with_statement159 = pascal_with_statement159
        
    @property
    def record(self) -> str:
        return self.__record

    @record.setter
    def record(self, record: str):
        self.__record = record

    @property
    def records(self) -> str:
        return self.__records

    @records.setter
    def records(self, records: str):
        self.__records = records

    @property
    def pascal_with_statement(self):
        return self.__pascal_with_statement

    @pascal_with_statement.setter
    def pascal_with_statement(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_with_statement__pascal_with_statement", None)
        self.__pascal_with_statement = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_structured_statement116"):
                opp_val = getattr(old_value, "pascal_structured_statement116", None)
                if opp_val == self:
                    setattr(old_value, "pascal_structured_statement116", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_structured_statement116"):
                opp_val = getattr(value, "pascal_structured_statement116", None)
                setattr(value, "pascal_structured_statement116", self)

    @property
    def pascal_with_statement159(self):
        return self.__pascal_with_statement159

    @pascal_with_statement159.setter
    def pascal_with_statement159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_with_statement__pascal_with_statement159", None)
        self.__pascal_with_statement159 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_statement160"):
                opp_val = getattr(old_value, "pascal_statement160", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement160", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement160"):
                opp_val = getattr(value, "pascal_statement160", None)
                setattr(value, "pascal_statement160", self)

class pascal_conditional_statement:

    pass
class pascal_repetitive_statement:

    pass
class pascal_compound_statement:

    pass
class pascal_expression:

    def __init__(self, operators: str, pascal_expression: "pascal_assignment_statement" = None, pascal_expression151: "pascal_if_statement" = None, pascal_expression128: "pascal_while_statement" = None, pascal_expression137: "pascal_repeat_statement" = None, pascal_expression140: "pascal_for_statement" = None, pascal_expression143: "pascal_for_statement" = None, pascal_expression178: "pascal_factor" = None, pascal_expression162: set["pascal_simple_expression"] = None, pascal_expression200: "pascal_expression_list" = None):
        self.operators = operators
        self.pascal_expression = pascal_expression
        self.pascal_expression151 = pascal_expression151
        self.pascal_expression128 = pascal_expression128
        self.pascal_expression137 = pascal_expression137
        self.pascal_expression140 = pascal_expression140
        self.pascal_expression143 = pascal_expression143
        self.pascal_expression178 = pascal_expression178
        self.pascal_expression162 = pascal_expression162 if pascal_expression162 is not None else set()
        self.pascal_expression200 = pascal_expression200
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

    @property
    def pascal_expression140(self):
        return self.__pascal_expression140

    @pascal_expression140.setter
    def pascal_expression140(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression140", None)
        self.__pascal_expression140 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_for_statement139"):
                opp_val = getattr(old_value, "pascal_for_statement139", None)
                if opp_val == self:
                    setattr(old_value, "pascal_for_statement139", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_for_statement139"):
                opp_val = getattr(value, "pascal_for_statement139", None)
                setattr(value, "pascal_for_statement139", self)

    @property
    def pascal_expression151(self):
        return self.__pascal_expression151

    @pascal_expression151.setter
    def pascal_expression151(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression151", None)
        self.__pascal_expression151 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_if_statement150"):
                opp_val = getattr(old_value, "pascal_if_statement150", None)
                if opp_val == self:
                    setattr(old_value, "pascal_if_statement150", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_if_statement150"):
                opp_val = getattr(value, "pascal_if_statement150", None)
                setattr(value, "pascal_if_statement150", self)

    @property
    def pascal_expression162(self):
        return self.__pascal_expression162

    @pascal_expression162.setter
    def pascal_expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression162", None)
        self.__pascal_expression162 = value if value is not None else set()
        
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
    def pascal_expression143(self):
        return self.__pascal_expression143

    @pascal_expression143.setter
    def pascal_expression143(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression143", None)
        self.__pascal_expression143 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_for_statement142"):
                opp_val = getattr(old_value, "pascal_for_statement142", None)
                if opp_val == self:
                    setattr(old_value, "pascal_for_statement142", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_for_statement142"):
                opp_val = getattr(value, "pascal_for_statement142", None)
                setattr(value, "pascal_for_statement142", self)

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
            if hasattr(old_value, "pascal_repeat_statement136"):
                opp_val = getattr(old_value, "pascal_repeat_statement136", None)
                if opp_val == self:
                    setattr(old_value, "pascal_repeat_statement136", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_repeat_statement136"):
                opp_val = getattr(value, "pascal_repeat_statement136", None)
                setattr(value, "pascal_repeat_statement136", self)

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
            if hasattr(old_value, "pascal_expression_list199"):
                opp_val = getattr(old_value, "pascal_expression_list199", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list199"):
                opp_val = getattr(value, "pascal_expression_list199", None)
                if opp_val is None:
                    setattr(value, "pascal_expression_list199", set([self]))
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
            if hasattr(old_value, "pascal_assignment_statement105"):
                opp_val = getattr(old_value, "pascal_assignment_statement105", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement105", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement105"):
                opp_val = getattr(value, "pascal_assignment_statement105", None)
                setattr(value, "pascal_assignment_statement105", self)

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
            if hasattr(old_value, "pascal_while_statement127"):
                opp_val = getattr(old_value, "pascal_while_statement127", None)
                if opp_val == self:
                    setattr(old_value, "pascal_while_statement127", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_while_statement127"):
                opp_val = getattr(value, "pascal_while_statement127", None)
                setattr(value, "pascal_while_statement127", self)

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
            if hasattr(old_value, "pascal_factor177"):
                opp_val = getattr(old_value, "pascal_factor177", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor177", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor177"):
                opp_val = getattr(value, "pascal_factor177", None)
                setattr(value, "pascal_factor177", self)

class pascal_variable:

    def __init__(self, name: str, pascal_variable: "pascal_assignment_statement" = None, pascal_variable183: "pascal_resto" = None, pascal_variable168: "pascal_factor" = None):
        self.name = name
        self.pascal_variable = pascal_variable
        self.pascal_variable183 = pascal_variable183
        self.pascal_variable168 = pascal_variable168
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_variable183(self):
        return self.__pascal_variable183

    @pascal_variable183.setter
    def pascal_variable183(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable183", None)
        self.__pascal_variable183 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto"):
                opp_val = getattr(old_value, "pascal_resto", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto"):
                opp_val = getattr(value, "pascal_resto", None)
                setattr(value, "pascal_resto", self)

    @property
    def pascal_variable168(self):
        return self.__pascal_variable168

    @pascal_variable168.setter
    def pascal_variable168(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable168", None)
        self.__pascal_variable168 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor167"):
                opp_val = getattr(old_value, "pascal_factor167", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor167", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor167"):
                opp_val = getattr(value, "pascal_factor167", None)
                setattr(value, "pascal_factor167", self)

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
            if hasattr(old_value, "pascal_assignment_statement103"):
                opp_val = getattr(old_value, "pascal_assignment_statement103", None)
                if opp_val == self:
                    setattr(old_value, "pascal_assignment_statement103", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_assignment_statement103"):
                opp_val = getattr(value, "pascal_assignment_statement103", None)
                setattr(value, "pascal_assignment_statement103", self)

class pascal_goto_statement:

    pass
class pascal_function_designator:

    def __init__(self, name: str, pascal_function_designator: "pascal_simple_statement" = None, pascal_function_designator175: "pascal_factor" = None, pascal_function_designator202: "pascal_expression_list" = None):
        self.name = name
        self.pascal_function_designator = pascal_function_designator
        self.pascal_function_designator175 = pascal_function_designator175
        self.pascal_function_designator202 = pascal_function_designator202
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
            if hasattr(old_value, "pascal_simple_statement99"):
                opp_val = getattr(old_value, "pascal_simple_statement99", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simple_statement99", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_statement99"):
                opp_val = getattr(value, "pascal_simple_statement99", None)
                setattr(value, "pascal_simple_statement99", self)

    @property
    def pascal_function_designator175(self):
        return self.__pascal_function_designator175

    @pascal_function_designator175.setter
    def pascal_function_designator175(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator175", None)
        self.__pascal_function_designator175 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor174"):
                opp_val = getattr(old_value, "pascal_factor174", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor174", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor174"):
                opp_val = getattr(value, "pascal_factor174", None)
                setattr(value, "pascal_factor174", self)

    @property
    def pascal_function_designator202(self):
        return self.__pascal_function_designator202

    @pascal_function_designator202.setter
    def pascal_function_designator202(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator202", None)
        self.__pascal_function_designator202 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list203"):
                opp_val = getattr(old_value, "pascal_expression_list203", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression_list203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list203"):
                opp_val = getattr(value, "pascal_expression_list203", None)
                setattr(value, "pascal_expression_list203", self)

class pascal_assignment_statement:

    pass
class pascal_structured_statement:

    pass
class pascal_simple_statement:

    def __init__(self, function_noargs: str, pascal_simple_statement: "pascal_statement" = None, pascal_simple_statement97: "pascal_assignment_statement" = None, pascal_simple_statement99: "pascal_function_designator" = None, pascal_simple_statement101: "pascal_goto_statement" = None):
        self.function_noargs = function_noargs
        self.pascal_simple_statement = pascal_simple_statement
        self.pascal_simple_statement97 = pascal_simple_statement97
        self.pascal_simple_statement99 = pascal_simple_statement99
        self.pascal_simple_statement101 = pascal_simple_statement101
        
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
            if hasattr(old_value, "pascal_statement93"):
                opp_val = getattr(old_value, "pascal_statement93", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement93", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement93"):
                opp_val = getattr(value, "pascal_statement93", None)
                setattr(value, "pascal_statement93", self)

    @property
    def pascal_simple_statement99(self):
        return self.__pascal_simple_statement99

    @pascal_simple_statement99.setter
    def pascal_simple_statement99(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement99", None)
        self.__pascal_simple_statement99 = value
        
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
    def pascal_simple_statement97(self):
        return self.__pascal_simple_statement97

    @pascal_simple_statement97.setter
    def pascal_simple_statement97(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement97", None)
        self.__pascal_simple_statement97 = value
        
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
    def pascal_simple_statement101(self):
        return self.__pascal_simple_statement101

    @pascal_simple_statement101.setter
    def pascal_simple_statement101(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_statement__pascal_simple_statement101", None)
        self.__pascal_simple_statement101 = value
        
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

class pascal_statement:

    pass
class pascal_bound_specification:

    def __init__(self, init: str, fin: str, name: str, pascal_bound_specification: "pascal_packed_conformant_array_schema" = None, pascal_bound_specification83: "pascal_unpacked_conformant_array_schema" = None):
        self.init = init
        self.fin = fin
        self.name = name
        self.pascal_bound_specification = pascal_bound_specification
        self.pascal_bound_specification83 = pascal_bound_specification83
        
    @property
    def init(self) -> str:
        return self.__init

    @init.setter
    def init(self, init: str):
        self.__init = init

    @property
    def fin(self) -> str:
        return self.__fin

    @fin.setter
    def fin(self, fin: str):
        self.__fin = fin

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_bound_specification83(self):
        return self.__pascal_bound_specification83

    @pascal_bound_specification83.setter
    def pascal_bound_specification83(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_bound_specification__pascal_bound_specification83", None)
        self.__pascal_bound_specification83 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_conformant_array_schema82"):
                opp_val = getattr(old_value, "pascal_unpacked_conformant_array_schema82", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_conformant_array_schema82"):
                opp_val = getattr(value, "pascal_unpacked_conformant_array_schema82", None)
                if opp_val is None:
                    setattr(value, "pascal_unpacked_conformant_array_schema82", set([self]))
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
            if hasattr(old_value, "pascal_packed_conformant_array_schema80"):
                opp_val = getattr(old_value, "pascal_packed_conformant_array_schema80", None)
                if opp_val == self:
                    setattr(old_value, "pascal_packed_conformant_array_schema80", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_packed_conformant_array_schema80"):
                opp_val = getattr(value, "pascal_packed_conformant_array_schema80", None)
                setattr(value, "pascal_packed_conformant_array_schema80", self)

class pascal_unpacked_conformant_array_schema:

    pass
class pascal_packed_conformant_array_schema:

    def __init__(self, name: str, pascal_packed_conformant_array_schema: "pascal_conformant_array_schema" = None, pascal_packed_conformant_array_schema80: "pascal_bound_specification" = None):
        self.name = name
        self.pascal_packed_conformant_array_schema = pascal_packed_conformant_array_schema
        self.pascal_packed_conformant_array_schema80 = pascal_packed_conformant_array_schema80
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_packed_conformant_array_schema80(self):
        return self.__pascal_packed_conformant_array_schema80

    @pascal_packed_conformant_array_schema80.setter
    def pascal_packed_conformant_array_schema80(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_packed_conformant_array_schema__pascal_packed_conformant_array_schema80", None)
        self.__pascal_packed_conformant_array_schema80 = value
        
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
            if hasattr(old_value, "pascal_conformant_array_schema76"):
                opp_val = getattr(old_value, "pascal_conformant_array_schema76", None)
                if opp_val == self:
                    setattr(old_value, "pascal_conformant_array_schema76", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_conformant_array_schema76"):
                opp_val = getattr(value, "pascal_conformant_array_schema76", None)
                setattr(value, "pascal_conformant_array_schema76", self)

class pascal_parameter_type:

    def __init__(self, name: str, pascal_parameter_type74: "pascal_conformant_array_schema" = None, pascal_parameter_type: "pascal_value_parameter_section" = None, pascal_parameter_type72: "pascal_variable_parameter_section" = None, pascal_parameter_type86: "pascal_unpacked_conformant_array_schema" = None):
        self.name = name
        self.pascal_parameter_type74 = pascal_parameter_type74
        self.pascal_parameter_type = pascal_parameter_type
        self.pascal_parameter_type72 = pascal_parameter_type72
        self.pascal_parameter_type86 = pascal_parameter_type86
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_parameter_type86(self):
        return self.__pascal_parameter_type86

    @pascal_parameter_type86.setter
    def pascal_parameter_type86(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type86", None)
        self.__pascal_parameter_type86 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_unpacked_conformant_array_schema85"):
                opp_val = getattr(old_value, "pascal_unpacked_conformant_array_schema85", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unpacked_conformant_array_schema85", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_conformant_array_schema85"):
                opp_val = getattr(value, "pascal_unpacked_conformant_array_schema85", None)
                setattr(value, "pascal_unpacked_conformant_array_schema85", self)

    @property
    def pascal_parameter_type74(self):
        return self.__pascal_parameter_type74

    @pascal_parameter_type74.setter
    def pascal_parameter_type74(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type74", None)
        self.__pascal_parameter_type74 = value
        
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
    def pascal_parameter_type(self):
        return self.__pascal_parameter_type

    @pascal_parameter_type.setter
    def pascal_parameter_type(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type", None)
        self.__pascal_parameter_type = value
        
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
    def pascal_parameter_type72(self):
        return self.__pascal_parameter_type72

    @pascal_parameter_type72.setter
    def pascal_parameter_type72(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_parameter_type__pascal_parameter_type72", None)
        self.__pascal_parameter_type72 = value
        
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

class pascal_variable_parameter_section:

    pass
class pascal_value_parameter_section:

    pass
class pascal_formal_parameter_section:

    pass
class pascal_statement_sequence:

    pass
class pascal_formal_parameter_list:

    pass
class abstraction_declaration:

    pass
class pascal_abstraction_declaration:

    def __init__(self, forward: bool, pascal_abstraction_declaration: "pascal_procedure_and_function_declaration_part" = None, pascal_abstraction_declaration43: "pascal_abstraction_heading" = None, pascal_abstraction_declaration46: "pascal_block" = None):
        self.forward = forward
        self.pascal_abstraction_declaration = pascal_abstraction_declaration
        self.pascal_abstraction_declaration43 = pascal_abstraction_declaration43
        self.pascal_abstraction_declaration46 = pascal_abstraction_declaration46
        
    @property
    def forward(self) -> bool:
        return self.__forward

    @forward.setter
    def forward(self, forward: bool):
        self.__forward = forward

    @property
    def pascal_abstraction_declaration46(self):
        return self.__pascal_abstraction_declaration46

    @pascal_abstraction_declaration46.setter
    def pascal_abstraction_declaration46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_declaration__pascal_abstraction_declaration46", None)
        self.__pascal_abstraction_declaration46 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_block47"):
                opp_val = getattr(old_value, "pascal_block47", None)
                if opp_val == self:
                    setattr(old_value, "pascal_block47", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_block47"):
                opp_val = getattr(value, "pascal_block47", None)
                setattr(value, "pascal_block47", self)

    @property
    def pascal_abstraction_declaration43(self):
        return self.__pascal_abstraction_declaration43

    @pascal_abstraction_declaration43.setter
    def pascal_abstraction_declaration43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_declaration__pascal_abstraction_declaration43", None)
        self.__pascal_abstraction_declaration43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_abstraction_heading44"):
                opp_val = getattr(old_value, "pascal_abstraction_heading44", None)
                if opp_val == self:
                    setattr(old_value, "pascal_abstraction_heading44", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_abstraction_heading44"):
                opp_val = getattr(value, "pascal_abstraction_heading44", None)
                setattr(value, "pascal_abstraction_heading44", self)

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
            if hasattr(old_value, "pascal_procedure_and_function_declaration_part39"):
                opp_val = getattr(old_value, "pascal_procedure_and_function_declaration_part39", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_and_function_declaration_part39"):
                opp_val = getattr(value, "pascal_procedure_and_function_declaration_part39", None)
                if opp_val is None:
                    setattr(value, "pascal_procedure_and_function_declaration_part39", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_conformant_array_schema:

    pass
class pascal_variable_section:

    pass
class pascal_type:

    pass
class pascal_type_definition:

    def __init__(self, name: str, pascal_type_definition: "pascal_type_definition_part" = None, pascal_type_definition28: "pascal_type" = None):
        self.name = name
        self.pascal_type_definition = pascal_type_definition
        self.pascal_type_definition28 = pascal_type_definition28
        
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
            if hasattr(old_value, "pascal_type_definition_part26"):
                opp_val = getattr(old_value, "pascal_type_definition_part26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type_definition_part26"):
                opp_val = getattr(value, "pascal_type_definition_part26", None)
                if opp_val is None:
                    setattr(value, "pascal_type_definition_part26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_type_definition28(self):
        return self.__pascal_type_definition28

    @pascal_type_definition28.setter
    def pascal_type_definition28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_type_definition__pascal_type_definition28", None)
        self.__pascal_type_definition28 = value
        
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

class pascal_constant:

    def __init__(self, opterator: str, name: str, string: str, boolLiteral: str, nil: str, pascal_constant: "pascal_constant_definition" = None, pascal_constant219: "pascal_subrange_type" = None, pascal_constant222: "pascal_subrange_type" = None, pascal_constant225: "pascal_subrange_type" = None, pascal_constant277: "pascal_number" = None, pascal_constant281: "pascal_case_label_list" = None):
        self.opterator = opterator
        self.name = name
        self.string = string
        self.boolLiteral = boolLiteral
        self.nil = nil
        self.pascal_constant = pascal_constant
        self.pascal_constant219 = pascal_constant219
        self.pascal_constant222 = pascal_constant222
        self.pascal_constant225 = pascal_constant225
        self.pascal_constant277 = pascal_constant277
        self.pascal_constant281 = pascal_constant281
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def boolLiteral(self) -> str:
        return self.__boolLiteral

    @boolLiteral.setter
    def boolLiteral(self, boolLiteral: str):
        self.__boolLiteral = boolLiteral

    @property
    def opterator(self) -> str:
        return self.__opterator

    @opterator.setter
    def opterator(self, opterator: str):
        self.__opterator = opterator

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
    def pascal_constant219(self):
        return self.__pascal_constant219

    @pascal_constant219.setter
    def pascal_constant219(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant219", None)
        self.__pascal_constant219 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type218"):
                opp_val = getattr(old_value, "pascal_subrange_type218", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type218"):
                opp_val = getattr(value, "pascal_subrange_type218", None)
                setattr(value, "pascal_subrange_type218", self)

    @property
    def pascal_constant281(self):
        return self.__pascal_constant281

    @pascal_constant281.setter
    def pascal_constant281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant281", None)
        self.__pascal_constant281 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_case_label_list280"):
                opp_val = getattr(old_value, "pascal_case_label_list280", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_label_list280"):
                opp_val = getattr(value, "pascal_case_label_list280", None)
                if opp_val is None:
                    setattr(value, "pascal_case_label_list280", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
            if hasattr(old_value, "pascal_constant_definition24"):
                opp_val = getattr(old_value, "pascal_constant_definition24", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant_definition24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant_definition24"):
                opp_val = getattr(value, "pascal_constant_definition24", None)
                setattr(value, "pascal_constant_definition24", self)

    @property
    def pascal_constant222(self):
        return self.__pascal_constant222

    @pascal_constant222.setter
    def pascal_constant222(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant222", None)
        self.__pascal_constant222 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type221"):
                opp_val = getattr(old_value, "pascal_subrange_type221", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type221", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type221"):
                opp_val = getattr(value, "pascal_subrange_type221", None)
                setattr(value, "pascal_subrange_type221", self)

    @property
    def pascal_constant225(self):
        return self.__pascal_constant225

    @pascal_constant225.setter
    def pascal_constant225(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant225", None)
        self.__pascal_constant225 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type224"):
                opp_val = getattr(old_value, "pascal_subrange_type224", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type224", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type224"):
                opp_val = getattr(value, "pascal_subrange_type224", None)
                setattr(value, "pascal_subrange_type224", self)

    @property
    def pascal_constant277(self):
        return self.__pascal_constant277

    @pascal_constant277.setter
    def pascal_constant277(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant277", None)
        self.__pascal_constant277 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_number278"):
                opp_val = getattr(old_value, "pascal_number278", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number278", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number278"):
                opp_val = getattr(value, "pascal_number278", None)
                setattr(value, "pascal_number278", self)

class pascal_constant_definition:

    def __init__(self, name: str, pascal_constant_definition: "pascal_constant_definition_part" = None, pascal_constant_definition24: "pascal_constant" = None):
        self.name = name
        self.pascal_constant_definition = pascal_constant_definition
        self.pascal_constant_definition24 = pascal_constant_definition24
        
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
            if hasattr(old_value, "pascal_constant_definition_part22"):
                opp_val = getattr(old_value, "pascal_constant_definition_part22", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant_definition_part22"):
                opp_val = getattr(value, "pascal_constant_definition_part22", None)
                if opp_val is None:
                    setattr(value, "pascal_constant_definition_part22", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_constant_definition24(self):
        return self.__pascal_constant_definition24

    @pascal_constant_definition24.setter
    def pascal_constant_definition24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant_definition__pascal_constant_definition24", None)
        self.__pascal_constant_definition24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant"):
                opp_val = getattr(old_value, "pascal_constant", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant"):
                opp_val = getattr(value, "pascal_constant", None)
                setattr(value, "pascal_constant", self)

class pascal_label:

    def __init__(self, number: str, pascal_label: "pascal_label_declaration_part" = None, pascal_label108: "pascal_goto_statement" = None, pascal_label91: "pascal_statement" = None):
        self.number = number
        self.pascal_label = pascal_label
        self.pascal_label108 = pascal_label108
        self.pascal_label91 = pascal_label91
        
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

    @property
    def pascal_label108(self):
        return self.__pascal_label108

    @pascal_label108.setter
    def pascal_label108(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_label__pascal_label108", None)
        self.__pascal_label108 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_goto_statement107"):
                opp_val = getattr(old_value, "pascal_goto_statement107", None)
                if opp_val == self:
                    setattr(old_value, "pascal_goto_statement107", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_goto_statement107"):
                opp_val = getattr(value, "pascal_goto_statement107", None)
                setattr(value, "pascal_goto_statement107", self)

    @property
    def pascal_label91(self):
        return self.__pascal_label91

    @pascal_label91.setter
    def pascal_label91(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_label__pascal_label91", None)
        self.__pascal_label91 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_statement90"):
                opp_val = getattr(old_value, "pascal_statement90", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement90", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement90"):
                opp_val = getattr(value, "pascal_statement90", None)
                setattr(value, "pascal_statement90", self)

class pascal_procedure_and_function_declaration_part:

    pass
class pascal_variable_declaration_part:

    pass
class pascal_type_definition_part:

    pass
class pascal_constant_definition_part:

    pass
class pascal_label_declaration_part:

    pass
class pascal_statement_part:

    pass
class pascal_declaration_part:

    pass
class pascal_abstraction_heading(abstraction_declaration):

    def __init__(self, name: str, resultType: str, pascal_abstraction_heading: "pascal_procedure_and_function_declaration_part" = None, pascal_abstraction_heading41: "pascal_formal_parameter_list" = None, pascal_abstraction_heading44: "pascal_abstraction_declaration" = None, pascal_abstraction_heading58: "pascal_formal_parameter_section" = None, pascal_abstraction_heading61: "pascal_formal_parameter_section" = None):
        self.name = name
        self.resultType = resultType
        self.pascal_abstraction_heading = pascal_abstraction_heading
        self.pascal_abstraction_heading41 = pascal_abstraction_heading41
        self.pascal_abstraction_heading44 = pascal_abstraction_heading44
        self.pascal_abstraction_heading58 = pascal_abstraction_heading58
        self.pascal_abstraction_heading61 = pascal_abstraction_heading61
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def resultType(self) -> str:
        return self.__resultType

    @resultType.setter
    def resultType(self, resultType: str):
        self.__resultType = resultType

    @property
    def pascal_abstraction_heading58(self):
        return self.__pascal_abstraction_heading58

    @pascal_abstraction_heading58.setter
    def pascal_abstraction_heading58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading58", None)
        self.__pascal_abstraction_heading58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_formal_parameter_section57"):
                opp_val = getattr(old_value, "pascal_formal_parameter_section57", None)
                if opp_val == self:
                    setattr(old_value, "pascal_formal_parameter_section57", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_formal_parameter_section57"):
                opp_val = getattr(value, "pascal_formal_parameter_section57", None)
                setattr(value, "pascal_formal_parameter_section57", self)

    @property
    def pascal_abstraction_heading41(self):
        return self.__pascal_abstraction_heading41

    @pascal_abstraction_heading41.setter
    def pascal_abstraction_heading41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading41", None)
        self.__pascal_abstraction_heading41 = value
        
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
    def pascal_abstraction_heading61(self):
        return self.__pascal_abstraction_heading61

    @pascal_abstraction_heading61.setter
    def pascal_abstraction_heading61(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading61", None)
        self.__pascal_abstraction_heading61 = value
        
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
            if hasattr(old_value, "pascal_procedure_and_function_declaration_part37"):
                opp_val = getattr(old_value, "pascal_procedure_and_function_declaration_part37", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_procedure_and_function_declaration_part37"):
                opp_val = getattr(value, "pascal_procedure_and_function_declaration_part37", None)
                if opp_val is None:
                    setattr(value, "pascal_procedure_and_function_declaration_part37", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_abstraction_heading44(self):
        return self.__pascal_abstraction_heading44

    @pascal_abstraction_heading44.setter
    def pascal_abstraction_heading44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_abstraction_heading__pascal_abstraction_heading44", None)
        self.__pascal_abstraction_heading44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_abstraction_declaration43"):
                opp_val = getattr(old_value, "pascal_abstraction_declaration43", None)
                if opp_val == self:
                    setattr(old_value, "pascal_abstraction_declaration43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_abstraction_declaration43"):
                opp_val = getattr(value, "pascal_abstraction_declaration43", None)
                setattr(value, "pascal_abstraction_declaration43", self)

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
            if hasattr(old_value, "pascal_variable_section32"):
                opp_val = getattr(old_value, "pascal_variable_section32", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_section32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_section32"):
                opp_val = getattr(value, "pascal_variable_section32", None)
                setattr(value, "pascal_variable_section32", self)

class pascal_block:

    pass
class pascal_program_heading:

    def __init__(self, name: str, pascal_program_heading4: "pascal_identifier_list" = None, pascal_program_heading: "pascal_program" = None):
        self.name = name
        self.pascal_program_heading4 = pascal_program_heading4
        self.pascal_program_heading = pascal_program_heading
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_program_heading4(self):
        return self.__pascal_program_heading4

    @pascal_program_heading4.setter
    def pascal_program_heading4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_program_heading__pascal_program_heading4", None)
        self.__pascal_program_heading4 = value
        
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
class pascal_identifier_list:

    def __init__(self, ids: str, pascal_identifier_list: "pascal_program_heading" = None, pascal_identifier_list64: "pascal_value_parameter_section" = None, pascal_identifier_list69: "pascal_variable_parameter_section" = None, pascal_identifier_list216: "pascal_enumerated_type" = None, pascal_identifier_list261: "pascal_record_section" = None):
        self.ids = ids
        self.pascal_identifier_list = pascal_identifier_list
        self.pascal_identifier_list64 = pascal_identifier_list64
        self.pascal_identifier_list69 = pascal_identifier_list69
        self.pascal_identifier_list216 = pascal_identifier_list216
        self.pascal_identifier_list261 = pascal_identifier_list261
        
    @property
    def ids(self) -> str:
        return self.__ids

    @ids.setter
    def ids(self, ids: str):
        self.__ids = ids

    @property
    def pascal_identifier_list64(self):
        return self.__pascal_identifier_list64

    @pascal_identifier_list64.setter
    def pascal_identifier_list64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list64", None)
        self.__pascal_identifier_list64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_value_parameter_section63"):
                opp_val = getattr(old_value, "pascal_value_parameter_section63", None)
                if opp_val == self:
                    setattr(old_value, "pascal_value_parameter_section63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_value_parameter_section63"):
                opp_val = getattr(value, "pascal_value_parameter_section63", None)
                setattr(value, "pascal_value_parameter_section63", self)

    @property
    def pascal_identifier_list261(self):
        return self.__pascal_identifier_list261

    @pascal_identifier_list261.setter
    def pascal_identifier_list261(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list261", None)
        self.__pascal_identifier_list261 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_record_section260"):
                opp_val = getattr(old_value, "pascal_record_section260", None)
                if opp_val == self:
                    setattr(old_value, "pascal_record_section260", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_record_section260"):
                opp_val = getattr(value, "pascal_record_section260", None)
                setattr(value, "pascal_record_section260", self)

    @property
    def pascal_identifier_list216(self):
        return self.__pascal_identifier_list216

    @pascal_identifier_list216.setter
    def pascal_identifier_list216(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list216", None)
        self.__pascal_identifier_list216 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_enumerated_type215"):
                opp_val = getattr(old_value, "pascal_enumerated_type215", None)
                if opp_val == self:
                    setattr(old_value, "pascal_enumerated_type215", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_enumerated_type215"):
                opp_val = getattr(value, "pascal_enumerated_type215", None)
                setattr(value, "pascal_enumerated_type215", self)

    @property
    def pascal_identifier_list69(self):
        return self.__pascal_identifier_list69

    @pascal_identifier_list69.setter
    def pascal_identifier_list69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list69", None)
        self.__pascal_identifier_list69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_variable_parameter_section68"):
                opp_val = getattr(old_value, "pascal_variable_parameter_section68", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable_parameter_section68", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable_parameter_section68"):
                opp_val = getattr(value, "pascal_variable_parameter_section68", None)
                setattr(value, "pascal_variable_parameter_section68", self)

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
            if hasattr(old_value, "pascal_program_heading4"):
                opp_val = getattr(old_value, "pascal_program_heading4", None)
                if opp_val == self:
                    setattr(old_value, "pascal_program_heading4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_program_heading4"):
                opp_val = getattr(value, "pascal_program_heading4", None)
                setattr(value, "pascal_program_heading4", self)
