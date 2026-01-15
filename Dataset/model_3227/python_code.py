from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class pascal_record_section:

    pass
class pascal_variant_part:

    def __init__(self, name: str, pascal_variant_part281: "pascal_tag_field" = None, pascal_variant_part283: set["pascal_variant"] = None, pascal_variant_part: "pascal_field_list" = None):
        self.name = name
        self.pascal_variant_part281 = pascal_variant_part281
        self.pascal_variant_part283 = pascal_variant_part283 if pascal_variant_part283 is not None else set()
        self.pascal_variant_part = pascal_variant_part
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_variant_part283(self):
        return self.__pascal_variant_part283

    @pascal_variant_part283.setter
    def pascal_variant_part283(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part283", None)
        self.__pascal_variant_part283 = value if value is not None else set()
        
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
    def pascal_variant_part281(self):
        return self.__pascal_variant_part281

    @pascal_variant_part281.setter
    def pascal_variant_part281(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variant_part__pascal_variant_part281", None)
        self.__pascal_variant_part281 = value
        
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
            if hasattr(old_value, "pascal_field_list271"):
                opp_val = getattr(old_value, "pascal_field_list271", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_field_list271"):
                opp_val = getattr(value, "pascal_field_list271", None)
                if opp_val is None:
                    setattr(value, "pascal_field_list271", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pascal_fixed_part:

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
            if hasattr(old_value, "pascal_number291"):
                opp_val = getattr(old_value, "pascal_number291", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number291", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number291"):
                opp_val = getattr(value, "pascal_number291", None)
                setattr(value, "pascal_number291", self)

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
            if hasattr(old_value, "pascal_variant_part281"):
                opp_val = getattr(old_value, "pascal_variant_part281", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variant_part281", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variant_part281"):
                opp_val = getattr(value, "pascal_variant_part281", None)
                setattr(value, "pascal_variant_part281", self)

class pascal_enumerated_type:

    pass
class pascal_subrange_type:

    def __init__(self, subrange: str, pascal_subrange_type233: "pascal_constant" = None, pascal_subrange_type236: "pascal_constant" = None, pascal_subrange_type239: "pascal_constant" = None, pascal_subrange_type: "pascal_simple_type" = None):
        self.subrange = subrange
        self.pascal_subrange_type233 = pascal_subrange_type233
        self.pascal_subrange_type236 = pascal_subrange_type236
        self.pascal_subrange_type239 = pascal_subrange_type239
        self.pascal_subrange_type = pascal_subrange_type
        
    @property
    def subrange(self) -> str:
        return self.__subrange

    @subrange.setter
    def subrange(self, subrange: str):
        self.__subrange = subrange

    @property
    def pascal_subrange_type236(self):
        return self.__pascal_subrange_type236

    @pascal_subrange_type236.setter
    def pascal_subrange_type236(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type236", None)
        self.__pascal_subrange_type236 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant237"):
                opp_val = getattr(old_value, "pascal_constant237", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant237", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant237"):
                opp_val = getattr(value, "pascal_constant237", None)
                setattr(value, "pascal_constant237", self)

    @property
    def pascal_subrange_type239(self):
        return self.__pascal_subrange_type239

    @pascal_subrange_type239.setter
    def pascal_subrange_type239(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type239", None)
        self.__pascal_subrange_type239 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant240"):
                opp_val = getattr(old_value, "pascal_constant240", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant240", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant240"):
                opp_val = getattr(value, "pascal_constant240", None)
                setattr(value, "pascal_constant240", self)

    @property
    def pascal_subrange_type233(self):
        return self.__pascal_subrange_type233

    @pascal_subrange_type233.setter
    def pascal_subrange_type233(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_subrange_type__pascal_subrange_type233", None)
        self.__pascal_subrange_type233 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_constant234"):
                opp_val = getattr(old_value, "pascal_constant234", None)
                if opp_val == self:
                    setattr(old_value, "pascal_constant234", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_constant234"):
                opp_val = getattr(value, "pascal_constant234", None)
                setattr(value, "pascal_constant234", self)

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
            if hasattr(old_value, "pascal_simple_type226"):
                opp_val = getattr(old_value, "pascal_simple_type226", None)
                if opp_val == self:
                    setattr(old_value, "pascal_simple_type226", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_simple_type226"):
                opp_val = getattr(value, "pascal_simple_type226", None)
                setattr(value, "pascal_simple_type226", self)

class pascal_pointer_type:

    pass
class pascal_field_list:

    pass
class pascal_file_type:

    pass
class pascal_set_type:

    pass
class pascal_record_type:

    def __init__(self, record: str, end: str, pascal_record_type: "pascal_unpacked_structured_type" = None, pascal_record_type258: "pascal_field_list" = None):
        self.record = record
        self.end = end
        self.pascal_record_type = pascal_record_type
        self.pascal_record_type258 = pascal_record_type258
        
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
    def pascal_record_type258(self):
        return self.__pascal_record_type258

    @pascal_record_type258.setter
    def pascal_record_type258(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_record_type__pascal_record_type258", None)
        self.__pascal_record_type258 = value
        
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
            if hasattr(old_value, "pascal_unpacked_structured_type246"):
                opp_val = getattr(old_value, "pascal_unpacked_structured_type246", None)
                if opp_val == self:
                    setattr(old_value, "pascal_unpacked_structured_type246", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_unpacked_structured_type246"):
                opp_val = getattr(value, "pascal_unpacked_structured_type246", None)
                setattr(value, "pascal_unpacked_structured_type246", self)

class pascal_array_type:

    pass
class pascal_unpacked_structured_type:

    pass
class pascal_set:

    def __init__(self, brackets: str, pascal_set211: "pascal_expression_list" = None, pascal_set: "pascal_factor" = None):
        self.brackets = brackets
        self.pascal_set211 = pascal_set211
        self.pascal_set = pascal_set
        
    @property
    def brackets(self) -> str:
        return self.__brackets

    @brackets.setter
    def brackets(self, brackets: str):
        self.__brackets = brackets

    @property
    def pascal_set211(self):
        return self.__pascal_set211

    @pascal_set211.setter
    def pascal_set211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_set__pascal_set211", None)
        self.__pascal_set211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list212"):
                opp_val = getattr(old_value, "pascal_expression_list212", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression_list212", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list212"):
                opp_val = getattr(value, "pascal_expression_list212", None)
                setattr(value, "pascal_expression_list212", self)

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
            if hasattr(old_value, "pascal_factor187"):
                opp_val = getattr(old_value, "pascal_factor187", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor187", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor187"):
                opp_val = getattr(value, "pascal_factor187", None)
                setattr(value, "pascal_factor187", self)

class pascal_number:

    pass
class pascal_structured_type:

    def __init__(self, packed: bool, pascal_structured_type: "pascal_type" = None, pascal_structured_type242: "pascal_unpacked_structured_type" = None):
        self.packed = packed
        self.pascal_structured_type = pascal_structured_type
        self.pascal_structured_type242 = pascal_structured_type242
        
    @property
    def packed(self) -> bool:
        return self.__packed

    @packed.setter
    def packed(self, packed: bool):
        self.__packed = packed

    @property
    def pascal_structured_type242(self):
        return self.__pascal_structured_type242

    @pascal_structured_type242.setter
    def pascal_structured_type242(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_structured_type__pascal_structured_type242", None)
        self.__pascal_structured_type242 = value
        
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
            if hasattr(old_value, "pascal_type222"):
                opp_val = getattr(old_value, "pascal_type222", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type222", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type222"):
                opp_val = getattr(value, "pascal_type222", None)
                setattr(value, "pascal_type222", self)

class pascal_simple_type:

    def __init__(self, name: str, pascal_simple_type: "pascal_type" = None, pascal_simple_type253: "pascal_array_type" = None, pascal_simple_type226: "pascal_subrange_type" = None, pascal_simple_type228: "pascal_enumerated_type" = None):
        self.name = name
        self.pascal_simple_type = pascal_simple_type
        self.pascal_simple_type253 = pascal_simple_type253
        self.pascal_simple_type226 = pascal_simple_type226
        self.pascal_simple_type228 = pascal_simple_type228
        
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
            if hasattr(old_value, "pascal_type220"):
                opp_val = getattr(old_value, "pascal_type220", None)
                if opp_val == self:
                    setattr(old_value, "pascal_type220", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_type220"):
                opp_val = getattr(value, "pascal_type220", None)
                setattr(value, "pascal_type220", self)

    @property
    def pascal_simple_type226(self):
        return self.__pascal_simple_type226

    @pascal_simple_type226.setter
    def pascal_simple_type226(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type226", None)
        self.__pascal_simple_type226 = value
        
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
    def pascal_simple_type253(self):
        return self.__pascal_simple_type253

    @pascal_simple_type253.setter
    def pascal_simple_type253(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type253", None)
        self.__pascal_simple_type253 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_array_type252"):
                opp_val = getattr(old_value, "pascal_array_type252", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_array_type252"):
                opp_val = getattr(value, "pascal_array_type252", None)
                if opp_val is None:
                    setattr(value, "pascal_array_type252", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_simple_type228(self):
        return self.__pascal_simple_type228

    @pascal_simple_type228.setter
    def pascal_simple_type228(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_type__pascal_simple_type228", None)
        self.__pascal_simple_type228 = value
        
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

class pascal_expression_list:

    pass
class pascal_resto:

    def __init__(self, accessor: bool, name: str, pascal_resto: "pascal_variable" = None, pascal_resto200: "pascal_expression_list" = None, pascal_resto203: "pascal_resto" = None, pascal_resto201: "pascal_resto" = None, pascal_resto206: "pascal_resto" = None, pascal_resto204: "pascal_resto" = None, pascal_resto209: "pascal_resto" = None, pascal_resto207: "pascal_resto" = None):
        self.accessor = accessor
        self.name = name
        self.pascal_resto = pascal_resto
        self.pascal_resto200 = pascal_resto200
        self.pascal_resto203 = pascal_resto203
        self.pascal_resto201 = pascal_resto201
        self.pascal_resto206 = pascal_resto206
        self.pascal_resto204 = pascal_resto204
        self.pascal_resto209 = pascal_resto209
        self.pascal_resto207 = pascal_resto207
        
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
    def pascal_resto204(self):
        return self.__pascal_resto204

    @pascal_resto204.setter
    def pascal_resto204(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto204", None)
        self.__pascal_resto204 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto206"):
                opp_val = getattr(old_value, "pascal_resto206", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto206", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto206"):
                opp_val = getattr(value, "pascal_resto206", None)
                setattr(value, "pascal_resto206", self)

    @property
    def pascal_resto201(self):
        return self.__pascal_resto201

    @pascal_resto201.setter
    def pascal_resto201(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto201", None)
        self.__pascal_resto201 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto203"):
                opp_val = getattr(old_value, "pascal_resto203", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto203", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto203"):
                opp_val = getattr(value, "pascal_resto203", None)
                setattr(value, "pascal_resto203", self)

    @property
    def pascal_resto203(self):
        return self.__pascal_resto203

    @pascal_resto203.setter
    def pascal_resto203(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto203", None)
        self.__pascal_resto203 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto201"):
                opp_val = getattr(old_value, "pascal_resto201", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto201", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto201"):
                opp_val = getattr(value, "pascal_resto201", None)
                setattr(value, "pascal_resto201", self)

    @property
    def pascal_resto209(self):
        return self.__pascal_resto209

    @pascal_resto209.setter
    def pascal_resto209(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto209", None)
        self.__pascal_resto209 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto207"):
                opp_val = getattr(old_value, "pascal_resto207", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto207", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto207"):
                opp_val = getattr(value, "pascal_resto207", None)
                setattr(value, "pascal_resto207", self)

    @property
    def pascal_resto207(self):
        return self.__pascal_resto207

    @pascal_resto207.setter
    def pascal_resto207(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto207", None)
        self.__pascal_resto207 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto209"):
                opp_val = getattr(old_value, "pascal_resto209", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto209", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto209"):
                opp_val = getattr(value, "pascal_resto209", None)
                setattr(value, "pascal_resto209", self)

    @property
    def pascal_resto200(self):
        return self.__pascal_resto200

    @pascal_resto200.setter
    def pascal_resto200(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto200", None)
        self.__pascal_resto200 = value
        
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
    def pascal_resto206(self):
        return self.__pascal_resto206

    @pascal_resto206.setter
    def pascal_resto206(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_resto__pascal_resto206", None)
        self.__pascal_resto206 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_resto204"):
                opp_val = getattr(old_value, "pascal_resto204", None)
                if opp_val == self:
                    setattr(old_value, "pascal_resto204", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_resto204"):
                opp_val = getattr(value, "pascal_resto204", None)
                setattr(value, "pascal_resto204", self)

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
            if hasattr(old_value, "pascal_variable198"):
                opp_val = getattr(old_value, "pascal_variable198", None)
                if opp_val == self:
                    setattr(old_value, "pascal_variable198", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_variable198"):
                opp_val = getattr(value, "pascal_variable198", None)
                setattr(value, "pascal_variable198", self)

class pascal_case_statement:

    pass
class pascal_if_statement:

    pass
class pascal_factor:

    def __init__(self, boolean: str, string: str, nil: bool, pascal_factor: "pascal_term" = None, pascal_factor192: "pascal_expression" = None, pascal_factor196: "pascal_factor" = None, pascal_factor194: "pascal_factor" = None, pascal_factor182: "pascal_variable" = None, pascal_factor185: "pascal_number" = None, pascal_factor187: "pascal_set" = None, pascal_factor189: "pascal_function_designator" = None):
        self.boolean = boolean
        self.string = string
        self.nil = nil
        self.pascal_factor = pascal_factor
        self.pascal_factor192 = pascal_factor192
        self.pascal_factor196 = pascal_factor196
        self.pascal_factor194 = pascal_factor194
        self.pascal_factor182 = pascal_factor182
        self.pascal_factor185 = pascal_factor185
        self.pascal_factor187 = pascal_factor187
        self.pascal_factor189 = pascal_factor189
        
    @property
    def boolean(self) -> str:
        return self.__boolean

    @boolean.setter
    def boolean(self, boolean: str):
        self.__boolean = boolean

    @property
    def nil(self) -> bool:
        return self.__nil

    @nil.setter
    def nil(self, nil: bool):
        self.__nil = nil

    @property
    def string(self) -> str:
        return self.__string

    @string.setter
    def string(self, string: str):
        self.__string = string

    @property
    def pascal_factor182(self):
        return self.__pascal_factor182

    @pascal_factor182.setter
    def pascal_factor182(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor182", None)
        self.__pascal_factor182 = value
        
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
    def pascal_factor196(self):
        return self.__pascal_factor196

    @pascal_factor196.setter
    def pascal_factor196(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor196", None)
        self.__pascal_factor196 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor194"):
                opp_val = getattr(old_value, "pascal_factor194", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor194", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor194"):
                opp_val = getattr(value, "pascal_factor194", None)
                setattr(value, "pascal_factor194", self)

    @property
    def pascal_factor194(self):
        return self.__pascal_factor194

    @pascal_factor194.setter
    def pascal_factor194(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor194", None)
        self.__pascal_factor194 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor196"):
                opp_val = getattr(old_value, "pascal_factor196", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor196", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor196"):
                opp_val = getattr(value, "pascal_factor196", None)
                setattr(value, "pascal_factor196", self)

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
    def pascal_factor189(self):
        return self.__pascal_factor189

    @pascal_factor189.setter
    def pascal_factor189(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor189", None)
        self.__pascal_factor189 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_function_designator190"):
                opp_val = getattr(old_value, "pascal_function_designator190", None)
                if opp_val == self:
                    setattr(old_value, "pascal_function_designator190", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_function_designator190"):
                opp_val = getattr(value, "pascal_function_designator190", None)
                setattr(value, "pascal_function_designator190", self)

    @property
    def pascal_factor185(self):
        return self.__pascal_factor185

    @pascal_factor185.setter
    def pascal_factor185(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor185", None)
        self.__pascal_factor185 = value
        
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
    def pascal_factor187(self):
        return self.__pascal_factor187

    @pascal_factor187.setter
    def pascal_factor187(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor187", None)
        self.__pascal_factor187 = value
        
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
    def pascal_factor192(self):
        return self.__pascal_factor192

    @pascal_factor192.setter
    def pascal_factor192(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_factor__pascal_factor192", None)
        self.__pascal_factor192 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression193"):
                opp_val = getattr(old_value, "pascal_expression193", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression193", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression193"):
                opp_val = getattr(value, "pascal_expression193", None)
                setattr(value, "pascal_expression193", self)

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

    def __init__(self, prefixOperator: str, operators: str, pascal_simple_expression: "pascal_expression" = None, pascal_simple_expression179: set["pascal_EObject"] = None):
        self.prefixOperator = prefixOperator
        self.operators = operators
        self.pascal_simple_expression = pascal_simple_expression
        self.pascal_simple_expression179 = pascal_simple_expression179 if pascal_simple_expression179 is not None else set()
        
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
            if hasattr(old_value, "pascal_expression177"):
                opp_val = getattr(old_value, "pascal_expression177", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression177"):
                opp_val = getattr(value, "pascal_expression177", None)
                if opp_val is None:
                    setattr(value, "pascal_expression177", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_simple_expression179(self):
        return self.__pascal_simple_expression179

    @pascal_simple_expression179.setter
    def pascal_simple_expression179(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_simple_expression__pascal_simple_expression179", None)
        self.__pascal_simple_expression179 = value if value is not None else set()
        
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
                    

class pascal_case_label_list:

    pass
class pascal_case_limb:

    pass
class pascal_function_designator:

    def __init__(self, name: str, pascal_function_designator: "pascal_simple_statement" = None, pascal_function_designator217: "pascal_expression_list" = None, pascal_function_designator190: "pascal_factor" = None):
        self.name = name
        self.pascal_function_designator = pascal_function_designator
        self.pascal_function_designator217 = pascal_function_designator217
        self.pascal_function_designator190 = pascal_function_designator190
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def pascal_function_designator190(self):
        return self.__pascal_function_designator190

    @pascal_function_designator190.setter
    def pascal_function_designator190(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator190", None)
        self.__pascal_function_designator190 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor189"):
                opp_val = getattr(old_value, "pascal_factor189", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor189", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor189"):
                opp_val = getattr(value, "pascal_factor189", None)
                setattr(value, "pascal_factor189", self)

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
    def pascal_function_designator217(self):
        return self.__pascal_function_designator217

    @pascal_function_designator217.setter
    def pascal_function_designator217(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_function_designator__pascal_function_designator217", None)
        self.__pascal_function_designator217 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list218"):
                opp_val = getattr(old_value, "pascal_expression_list218", None)
                if opp_val == self:
                    setattr(old_value, "pascal_expression_list218", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list218"):
                opp_val = getattr(value, "pascal_expression_list218", None)
                setattr(value, "pascal_expression_list218", self)

class pascal_assignment_statement:

    pass
class pascal_structured_statement:

    pass
class pascal_simple_statement:

    pass
class pascal_statement:

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

    def __init__(self, record: str, records: str, pascal_with_statement: "pascal_structured_statement" = None, pascal_with_statement174: "pascal_statement" = None):
        self.record = record
        self.records = records
        self.pascal_with_statement = pascal_with_statement
        self.pascal_with_statement174 = pascal_with_statement174
        
    @property
    def records(self) -> str:
        return self.__records

    @records.setter
    def records(self, records: str):
        self.__records = records

    @property
    def record(self) -> str:
        return self.__record

    @record.setter
    def record(self, record: str):
        self.__record = record

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
    def pascal_with_statement174(self):
        return self.__pascal_with_statement174

    @pascal_with_statement174.setter
    def pascal_with_statement174(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_with_statement__pascal_with_statement174", None)
        self.__pascal_with_statement174 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_statement175"):
                opp_val = getattr(old_value, "pascal_statement175", None)
                if opp_val == self:
                    setattr(old_value, "pascal_statement175", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_statement175"):
                opp_val = getattr(value, "pascal_statement175", None)
                setattr(value, "pascal_statement175", self)

class pascal_conditional_statement:

    pass
class pascal_repetitive_statement:

    pass
class pascal_compound_statement:

    pass
class pascal_expression:

    def __init__(self, operators: str, pascal_expression: "pascal_assignment_statement" = None, pascal_expression128: "pascal_while_statement" = None, pascal_expression137: "pascal_repeat_statement" = None, pascal_expression140: "pascal_for_statement" = None, pascal_expression143: "pascal_for_statement" = None, pascal_expression162: "pascal_case_statement" = None, pascal_expression177: set["pascal_simple_expression"] = None, pascal_expression153: "pascal_if_statement" = None, pascal_expression193: "pascal_factor" = None, pascal_expression215: "pascal_expression_list" = None):
        self.operators = operators
        self.pascal_expression = pascal_expression
        self.pascal_expression128 = pascal_expression128
        self.pascal_expression137 = pascal_expression137
        self.pascal_expression140 = pascal_expression140
        self.pascal_expression143 = pascal_expression143
        self.pascal_expression162 = pascal_expression162
        self.pascal_expression177 = pascal_expression177 if pascal_expression177 is not None else set()
        self.pascal_expression153 = pascal_expression153
        self.pascal_expression193 = pascal_expression193
        self.pascal_expression215 = pascal_expression215
        
    @property
    def operators(self) -> str:
        return self.__operators

    @operators.setter
    def operators(self, operators: str):
        self.__operators = operators

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
    def pascal_expression153(self):
        return self.__pascal_expression153

    @pascal_expression153.setter
    def pascal_expression153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression153", None)
        self.__pascal_expression153 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_if_statement152"):
                opp_val = getattr(old_value, "pascal_if_statement152", None)
                if opp_val == self:
                    setattr(old_value, "pascal_if_statement152", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_if_statement152"):
                opp_val = getattr(value, "pascal_if_statement152", None)
                setattr(value, "pascal_if_statement152", self)

    @property
    def pascal_expression177(self):
        return self.__pascal_expression177

    @pascal_expression177.setter
    def pascal_expression177(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression177", None)
        self.__pascal_expression177 = value if value is not None else set()
        
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
    def pascal_expression215(self):
        return self.__pascal_expression215

    @pascal_expression215.setter
    def pascal_expression215(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression215", None)
        self.__pascal_expression215 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_expression_list214"):
                opp_val = getattr(old_value, "pascal_expression_list214", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_expression_list214"):
                opp_val = getattr(value, "pascal_expression_list214", None)
                if opp_val is None:
                    setattr(value, "pascal_expression_list214", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

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
    def pascal_expression193(self):
        return self.__pascal_expression193

    @pascal_expression193.setter
    def pascal_expression193(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression193", None)
        self.__pascal_expression193 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_factor192"):
                opp_val = getattr(old_value, "pascal_factor192", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor192", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor192"):
                opp_val = getattr(value, "pascal_factor192", None)
                setattr(value, "pascal_factor192", self)

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
    def pascal_expression162(self):
        return self.__pascal_expression162

    @pascal_expression162.setter
    def pascal_expression162(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_expression__pascal_expression162", None)
        self.__pascal_expression162 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_case_statement161"):
                opp_val = getattr(old_value, "pascal_case_statement161", None)
                if opp_val == self:
                    setattr(old_value, "pascal_case_statement161", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_statement161"):
                opp_val = getattr(value, "pascal_case_statement161", None)
                setattr(value, "pascal_case_statement161", self)

class pascal_variable:

    def __init__(self, name: str, pascal_variable: "pascal_assignment_statement" = None, pascal_variable198: "pascal_resto" = None, pascal_variable183: "pascal_factor" = None):
        self.name = name
        self.pascal_variable = pascal_variable
        self.pascal_variable198 = pascal_variable198
        self.pascal_variable183 = pascal_variable183
        
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
            if hasattr(old_value, "pascal_factor182"):
                opp_val = getattr(old_value, "pascal_factor182", None)
                if opp_val == self:
                    setattr(old_value, "pascal_factor182", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_factor182"):
                opp_val = getattr(value, "pascal_factor182", None)
                setattr(value, "pascal_factor182", self)

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

    @property
    def pascal_variable198(self):
        return self.__pascal_variable198

    @pascal_variable198.setter
    def pascal_variable198(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_variable__pascal_variable198", None)
        self.__pascal_variable198 = value
        
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

class pascal_goto_statement:

    pass
class pascal_formal_parameter_section:

    pass
class pascal_statement_sequence:

    pass
class pascal_bound_specification:

    def __init__(self, init: str, fin: str, name: str, pascal_bound_specification: "pascal_packed_conformant_array_schema" = None, pascal_bound_specification83: "pascal_unpacked_conformant_array_schema" = None):
        self.init = init
        self.fin = fin
        self.name = name
        self.pascal_bound_specification = pascal_bound_specification
        self.pascal_bound_specification83 = pascal_bound_specification83
        
    @property
    def fin(self) -> str:
        return self.__fin

    @fin.setter
    def fin(self, fin: str):
        self.__fin = fin

    @property
    def init(self) -> str:
        return self.__init

    @init.setter
    def init(self, init: str):
        self.__init = init

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class pascal_conformant_array_schema:

    pass
class pascal_parameter_type:

    def __init__(self, name: str, pascal_parameter_type: "pascal_value_parameter_section" = None, pascal_parameter_type72: "pascal_variable_parameter_section" = None, pascal_parameter_type74: "pascal_conformant_array_schema" = None, pascal_parameter_type86: "pascal_unpacked_conformant_array_schema" = None):
        self.name = name
        self.pascal_parameter_type = pascal_parameter_type
        self.pascal_parameter_type72 = pascal_parameter_type72
        self.pascal_parameter_type74 = pascal_parameter_type74
        self.pascal_parameter_type86 = pascal_parameter_type86
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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

class pascal_variable_parameter_section:

    pass
class pascal_value_parameter_section:

    pass
class pascal_constant_definition:

    def __init__(self, name: str, pascal_constant_definition24: "pascal_constant" = None, pascal_constant_definition: "pascal_constant_definition_part" = None):
        self.name = name
        self.pascal_constant_definition24 = pascal_constant_definition24
        self.pascal_constant_definition = pascal_constant_definition
        
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

class pascal_constant:

    def __init__(self, opterator: str, name: str, string: str, boolLiteral: str, nil: str, pascal_constant: "pascal_constant_definition" = None, pascal_constant172: "pascal_case_label_list" = None, pascal_constant234: "pascal_subrange_type" = None, pascal_constant237: "pascal_subrange_type" = None, pascal_constant240: "pascal_subrange_type" = None, pascal_constant293: "pascal_number" = None):
        self.opterator = opterator
        self.name = name
        self.string = string
        self.boolLiteral = boolLiteral
        self.nil = nil
        self.pascal_constant = pascal_constant
        self.pascal_constant172 = pascal_constant172
        self.pascal_constant234 = pascal_constant234
        self.pascal_constant237 = pascal_constant237
        self.pascal_constant240 = pascal_constant240
        self.pascal_constant293 = pascal_constant293
        
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
    def pascal_constant237(self):
        return self.__pascal_constant237

    @pascal_constant237.setter
    def pascal_constant237(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant237", None)
        self.__pascal_constant237 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type236"):
                opp_val = getattr(old_value, "pascal_subrange_type236", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type236", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type236"):
                opp_val = getattr(value, "pascal_subrange_type236", None)
                setattr(value, "pascal_subrange_type236", self)

    @property
    def pascal_constant172(self):
        return self.__pascal_constant172

    @pascal_constant172.setter
    def pascal_constant172(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant172", None)
        self.__pascal_constant172 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_case_label_list171"):
                opp_val = getattr(old_value, "pascal_case_label_list171", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_case_label_list171"):
                opp_val = getattr(value, "pascal_case_label_list171", None)
                if opp_val is None:
                    setattr(value, "pascal_case_label_list171", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pascal_constant240(self):
        return self.__pascal_constant240

    @pascal_constant240.setter
    def pascal_constant240(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant240", None)
        self.__pascal_constant240 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type239"):
                opp_val = getattr(old_value, "pascal_subrange_type239", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type239", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type239"):
                opp_val = getattr(value, "pascal_subrange_type239", None)
                setattr(value, "pascal_subrange_type239", self)

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
    def pascal_constant293(self):
        return self.__pascal_constant293

    @pascal_constant293.setter
    def pascal_constant293(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant293", None)
        self.__pascal_constant293 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_number294"):
                opp_val = getattr(old_value, "pascal_number294", None)
                if opp_val == self:
                    setattr(old_value, "pascal_number294", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_number294"):
                opp_val = getattr(value, "pascal_number294", None)
                setattr(value, "pascal_number294", self)

    @property
    def pascal_constant234(self):
        return self.__pascal_constant234

    @pascal_constant234.setter
    def pascal_constant234(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_constant__pascal_constant234", None)
        self.__pascal_constant234 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_subrange_type233"):
                opp_val = getattr(old_value, "pascal_subrange_type233", None)
                if opp_val == self:
                    setattr(old_value, "pascal_subrange_type233", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_subrange_type233"):
                opp_val = getattr(value, "pascal_subrange_type233", None)
                setattr(value, "pascal_subrange_type233", self)

class pascal_program:

    pass
class pascal_constant_definition_part:

    pass
class pascal_label_declaration_part:

    pass
class pascal_statement_part:

    pass
class pascal_declaration_part:

    pass
class pascal_identifier_list:

    def __init__(self, ids: str, pascal_identifier_list: "pascal_program_heading" = None, pascal_identifier_list64: "pascal_value_parameter_section" = None, pascal_identifier_list69: "pascal_variable_parameter_section" = None, pascal_identifier_list231: "pascal_enumerated_type" = None, pascal_identifier_list276: "pascal_record_section" = None):
        self.ids = ids
        self.pascal_identifier_list = pascal_identifier_list
        self.pascal_identifier_list64 = pascal_identifier_list64
        self.pascal_identifier_list69 = pascal_identifier_list69
        self.pascal_identifier_list231 = pascal_identifier_list231
        self.pascal_identifier_list276 = pascal_identifier_list276
        
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
            if hasattr(old_value, "pascal_program_heading4"):
                opp_val = getattr(old_value, "pascal_program_heading4", None)
                if opp_val == self:
                    setattr(old_value, "pascal_program_heading4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_program_heading4"):
                opp_val = getattr(value, "pascal_program_heading4", None)
                setattr(value, "pascal_program_heading4", self)

    @property
    def pascal_identifier_list231(self):
        return self.__pascal_identifier_list231

    @pascal_identifier_list231.setter
    def pascal_identifier_list231(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list231", None)
        self.__pascal_identifier_list231 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_enumerated_type230"):
                opp_val = getattr(old_value, "pascal_enumerated_type230", None)
                if opp_val == self:
                    setattr(old_value, "pascal_enumerated_type230", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_enumerated_type230"):
                opp_val = getattr(value, "pascal_enumerated_type230", None)
                setattr(value, "pascal_enumerated_type230", self)

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
    def pascal_identifier_list276(self):
        return self.__pascal_identifier_list276

    @pascal_identifier_list276.setter
    def pascal_identifier_list276(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pascal_identifier_list__pascal_identifier_list276", None)
        self.__pascal_identifier_list276 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pascal_record_section275"):
                opp_val = getattr(old_value, "pascal_record_section275", None)
                if opp_val == self:
                    setattr(old_value, "pascal_record_section275", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pascal_record_section275"):
                opp_val = getattr(value, "pascal_record_section275", None)
                setattr(value, "pascal_record_section275", self)

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

class pascal_block:

    pass
class pascal_program_heading:

    def __init__(self, name: str, pascal_program_heading: "pascal_program" = None, pascal_program_heading4: "pascal_identifier_list" = None):
        self.name = name
        self.pascal_program_heading = pascal_program_heading
        self.pascal_program_heading4 = pascal_program_heading4
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

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
