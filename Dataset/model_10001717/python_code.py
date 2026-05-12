from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class student_Actor:

    pass


class medical_technologist_Actor:

    pass


class physicians_Actor:

    pass


class floor_nurse_Actor:

    pass


class release_receptionist_Actor:

    pass


class patient_Actor:

    pass


class admission_receptionist_Actor:

    pass





class hospital_admission_system_Component:

    pass


class list_of_patients_external:

    pass


class receive_records_external:

    pass


class receive_patient_records_external:

    pass


class check_out_external:

    pass


class check_in_external:

    pass


class enter_patient_notes_external:

    pass


class enter_lab_notes_external:

    pass


class Routing_number:

    pass


class price_quote:

    def __init__(self, _bulk_rate_price: str, _supplier26: "_supplier" = None, part29: "Part" = None):
        self._bulk_rate_price = _bulk_rate_price
        self._supplier26 = _supplier26
        self.part29 = part29
        
        pass
    @property
    def _bulk_rate_price(self):
        return self.___bulk_rate_price
    @_bulk_rate_price.setter
    def _bulk_rate_price(self, _bulk_rate_price: str):
        self.___bulk_rate_price = _bulk_rate_price

    @property
    def _supplier26(self):
        return self.___supplier26
    @_supplier26.setter
    def _supplier26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_price_quote___supplier26", None)
        self.___supplier26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "price_quote27"):
                opp_val = getattr(old_value, "price_quote27", None)
                if opp_val == self:
                    setattr(old_value, "price_quote27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "price_quote27"):
                opp_val = getattr(value, "price_quote27", None)
                setattr(value, "price_quote27", self)

    @property
    def part29(self):
        return self.__part29
    @part29.setter
    def part29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_price_quote__part29", None)
        self.__part29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "price_quote28"):
                opp_val = getattr(old_value, "price_quote28", None)
                if opp_val == self:
                    setattr(old_value, "price_quote28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "price_quote28"):
                opp_val = getattr(value, "price_quote28", None)
                setattr(value, "price_quote28", self)



class _supplier:

    def __init__(self, _supplier_ID: str, part25: set["Part"] = None, price_quote27: "price_quote" = None):
        self._supplier_ID = _supplier_ID
        self.part25 = part25 if part25 is not None else set()
        self.price_quote27 = price_quote27
        
        pass
    @property
    def _supplier_ID(self):
        return self.___supplier_ID
    @_supplier_ID.setter
    def _supplier_ID(self, _supplier_ID: str):
        self.___supplier_ID = _supplier_ID

    @property
    def price_quote27(self):
        return self.__price_quote27
    @price_quote27.setter
    def price_quote27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__supplier__price_quote27", None)
        self.__price_quote27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "_supplier26"):
                opp_val = getattr(old_value, "_supplier26", None)
                if opp_val == self:
                    setattr(old_value, "_supplier26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "_supplier26"):
                opp_val = getattr(value, "_supplier26", None)
                setattr(value, "_supplier26", self)

    @property
    def part25(self):
        return self.__part25
    @part25.setter
    def part25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"__supplier__part25", None)
        self.__part25 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "_supplier24"):
                    opp_val = getattr(item, "_supplier24", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "_supplier24"):
                    opp_val = getattr(item, "_supplier24", None)
                    
                    if opp_val is None:
                        setattr(item, "_supplier24", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Storage:

    def __init__(self, instruction_ID: str, part21: set["Part"] = None):
        self.instruction_ID = instruction_ID
        self.part21 = part21 if part21 is not None else set()
        
        pass
    @property
    def instruction_ID(self):
        return self.__instruction_ID
    @instruction_ID.setter
    def instruction_ID(self, instruction_ID: str):
        self.__instruction_ID = instruction_ID

    @property
    def part21(self):
        return self.__part21
    @part21.setter
    def part21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Storage__part21", None)
        self.__part21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "storage20"):
                    opp_val = getattr(item, "storage20", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "storage20"):
                    opp_val = getattr(item, "storage20", None)
                    
                    if opp_val is None:
                        setattr(item, "storage20", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Part:

    def __init__(self, _part_number: str, _description: str, storage20: set["Storage"] = None, subpart22: set["Part"] = None, part23: set["Part"] = None, _supplier24: set["_supplier"] = None, price_quote28: "price_quote" = None, routing_number31: "Routing_number" = None):
        self._part_number = _part_number
        self._description = _description
        self.storage20 = storage20 if storage20 is not None else set()
        self.subpart22 = subpart22 if subpart22 is not None else set()
        self.part23 = part23 if part23 is not None else set()
        self._supplier24 = _supplier24 if _supplier24 is not None else set()
        self.price_quote28 = price_quote28
        self.routing_number31 = routing_number31
        
        pass
    @property
    def _description(self):
        return self.___description
    @_description.setter
    def _description(self, _description: str):
        self.___description = _description

    @property
    def _part_number(self):
        return self.___part_number
    @_part_number.setter
    def _part_number(self, _part_number: str):
        self.___part_number = _part_number

    @property
    def routing_number31(self):
        return self.__routing_number31
    @routing_number31.setter
    def routing_number31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Part__routing_number31", None)
        self.__routing_number31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "part30"):
                opp_val = getattr(old_value, "part30", None)
                if opp_val == self:
                    setattr(old_value, "part30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "part30"):
                opp_val = getattr(value, "part30", None)
                setattr(value, "part30", self)

    @property
    def storage20(self):
        return self.__storage20
    @storage20.setter
    def storage20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Part__storage20", None)
        self.__storage20 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "part21"):
                    opp_val = getattr(item, "part21", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "part21"):
                    opp_val = getattr(item, "part21", None)
                    
                    if opp_val is None:
                        setattr(item, "part21", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def part23(self):
        return self.__part23
    @part23.setter
    def part23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Part__part23", None)
        self.__part23 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "subpart22"):
                    opp_val = getattr(item, "subpart22", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "subpart22"):
                    opp_val = getattr(item, "subpart22", None)
                    
                    if opp_val is None:
                        setattr(item, "subpart22", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def subpart22(self):
        return self.__subpart22
    @subpart22.setter
    def subpart22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Part__subpart22", None)
        self.__subpart22 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "part23"):
                    opp_val = getattr(item, "part23", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "part23"):
                    opp_val = getattr(item, "part23", None)
                    
                    if opp_val is None:
                        setattr(item, "part23", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def _supplier24(self):
        return self.___supplier24
    @_supplier24.setter
    def _supplier24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Part___supplier24", None)
        self.___supplier24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "part25"):
                    opp_val = getattr(item, "part25", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "part25"):
                    opp_val = getattr(item, "part25", None)
                    
                    if opp_val is None:
                        setattr(item, "part25", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def price_quote28(self):
        return self.__price_quote28
    @price_quote28.setter
    def price_quote28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Part__price_quote28", None)
        self.__price_quote28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "part29"):
                opp_val = getattr(old_value, "part29", None)
                if opp_val == self:
                    setattr(old_value, "part29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "part29"):
                opp_val = getattr(value, "part29", None)
                setattr(value, "part29", self)

