from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class private:

    pass


class general:

    pass


class login:

    def __init__(self, id1: str, name: str, pass1: str, receptionist_login_111: "receptionist" = None):
        self.id1 = id1
        self.name = name
        self.pass1 = pass1
        self.receptionist_login_111 = receptionist_login_111
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id1(self):
        return self.__id1
    @id1.setter
    def id1(self, id1: str):
        self.__id1 = id1

    @property
    def pass1(self):
        return self.__pass1
    @pass1.setter
    def pass1(self, pass1: str):
        self.__pass1 = pass1

    @property
    def receptionist_login_111(self):
        return self.__receptionist_login_111
    @receptionist_login_111.setter
    def receptionist_login_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login__receptionist_login_111", None)
        self.__receptionist_login_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist_login_010"):
                opp_val = getattr(old_value, "receptionist_login_010", None)
                if opp_val == self:
                    setattr(old_value, "receptionist_login_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist_login_010"):
                opp_val = getattr(value, "receptionist_login_010", None)
                setattr(value, "receptionist_login_010", self)



class loan:

    def __init__(self, patient_name: str, amount: str, billing_loan_115: "Bill" = None):
        self.patient_name = patient_name
        self.amount = amount
        self.billing_loan_115 = billing_loan_115
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def patient_name(self):
        return self.__patient_name
    @patient_name.setter
    def patient_name(self, patient_name: str):
        self.__patient_name = patient_name

    @property
    def billing_loan_115(self):
        return self.__billing_loan_115
    @billing_loan_115.setter
    def billing_loan_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan__billing_loan_115", None)
        self.__billing_loan_115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "billing_loan_014"):
                opp_val = getattr(old_value, "billing_loan_014", None)
                if opp_val == self:
                    setattr(old_value, "billing_loan_014", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "billing_loan_014"):
                opp_val = getattr(value, "billing_loan_014", None)
                setattr(value, "billing_loan_014", self)



class Bill:

    def __init__(self, bill_no: str, patient_name: str, amount: str, patient_billing_19: "patient" = None, receptionist_billing_113: "receptionist" = None, billing_loan_014: "loan" = None):
        self.bill_no = bill_no
        self.patient_name = patient_name
        self.amount = amount
        self.patient_billing_19 = patient_billing_19
        self.receptionist_billing_113 = receptionist_billing_113
        self.billing_loan_014 = billing_loan_014
        
        pass
    @property
    def bill_no(self):
        return self.__bill_no
    @bill_no.setter
    def bill_no(self, bill_no: str):
        self.__bill_no = bill_no

    @property
    def patient_name(self):
        return self.__patient_name
    @patient_name.setter
    def patient_name(self, patient_name: str):
        self.__patient_name = patient_name

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def billing_loan_014(self):
        return self.__billing_loan_014
    @billing_loan_014.setter
    def billing_loan_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__billing_loan_014", None)
        self.__billing_loan_014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "billing_loan_115"):
                opp_val = getattr(old_value, "billing_loan_115", None)
                if opp_val == self:
                    setattr(old_value, "billing_loan_115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "billing_loan_115"):
                opp_val = getattr(value, "billing_loan_115", None)
                setattr(value, "billing_loan_115", self)

    @property
    def patient_billing_19(self):
        return self.__patient_billing_19
    @patient_billing_19.setter
    def patient_billing_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__patient_billing_19", None)
        self.__patient_billing_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_billing_08"):
                opp_val = getattr(old_value, "patient_billing_08", None)
                if opp_val == self:
                    setattr(old_value, "patient_billing_08", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_billing_08"):
                opp_val = getattr(value, "patient_billing_08", None)
                setattr(value, "patient_billing_08", self)

    @property
    def receptionist_billing_113(self):
        return self.__receptionist_billing_113
    @receptionist_billing_113.setter
    def receptionist_billing_113(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist_billing_113", None)
        self.__receptionist_billing_113 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist_billing_012"):
                opp_val = getattr(old_value, "receptionist_billing_012", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist_billing_012"):
                opp_val = getattr(value, "receptionist_billing_012", None)
                if opp_val is None:
                    setattr(value, "receptionist_billing_012", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class test:

    def __init__(self, disease_name: str, doctor_test_13: "doctor" = None):
        self.disease_name = disease_name
        self.doctor_test_13 = doctor_test_13
        
        pass
    @property
    def disease_name(self):
        return self.__disease_name
    @disease_name.setter
    def disease_name(self, disease_name: str):
        self.__disease_name = disease_name

    @property
    def doctor_test_13(self):
        return self.__doctor_test_13
    @doctor_test_13.setter
    def doctor_test_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test__doctor_test_13", None)
        self.__doctor_test_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor_test_02"):
                opp_val = getattr(old_value, "doctor_test_02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor_test_02"):
                opp_val = getattr(value, "doctor_test_02", None)
                if opp_val is None:
                    setattr(value, "doctor_test_02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class room:

    def __init__(self, room_no: str, patient_room_15: "patient" = None):
        self.room_no = room_no
        self.patient_room_15 = patient_room_15
        
        pass
    @property
    def room_no(self):
        return self.__room_no
    @room_no.setter
    def room_no(self, room_no: str):
        self.__room_no = room_no

    @property
    def patient_room_15(self):
        return self.__patient_room_15
    @patient_room_15.setter
    def patient_room_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room__patient_room_15", None)
        self.__patient_room_15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_room_04"):
                opp_val = getattr(old_value, "patient_room_04", None)
                if opp_val == self:
                    setattr(old_value, "patient_room_04", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_room_04"):
                opp_val = getattr(value, "patient_room_04", None)
                setattr(value, "patient_room_04", self)



class receptionist:

    def __init__(self, rid: str, name: str, receptionist_login_010: "login" = None, receptionist_billing_012: set["Bill"] = None):
        self.rid = rid
        self.name = name
        self.receptionist_login_010 = receptionist_login_010
        self.receptionist_billing_012 = receptionist_billing_012 if receptionist_billing_012 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def rid(self):
        return self.__rid
    @rid.setter
    def rid(self, rid: str):
        self.__rid = rid

    @property
    def receptionist_login_010(self):
        return self.__receptionist_login_010
    @receptionist_login_010.setter
    def receptionist_login_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_receptionist__receptionist_login_010", None)
        self.__receptionist_login_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist_login_111"):
                opp_val = getattr(old_value, "receptionist_login_111", None)
                if opp_val == self:
                    setattr(old_value, "receptionist_login_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist_login_111"):
                opp_val = getattr(value, "receptionist_login_111", None)
                setattr(value, "receptionist_login_111", self)

    @property
    def receptionist_billing_012(self):
        return self.__receptionist_billing_012
    @receptionist_billing_012.setter
    def receptionist_billing_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_receptionist__receptionist_billing_012", None)
        self.__receptionist_billing_012 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist_billing_113"):
                    opp_val = getattr(item, "receptionist_billing_113", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionist_billing_113", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist_billing_113"):
                    opp_val = getattr(item, "receptionist_billing_113", None)
                    
                    setattr(item, "receptionist_billing_113", self)
                    



class doctor:

    def __init__(self, did: str, name: str, dept: str, specilization: str, phone_no: str, doctor_test_02: set["test"] = None, patient_doctor_17: set["patient"] = None):
        self.did = did
        self.name = name
        self.dept = dept
        self.specilization = specilization
        self.phone_no = phone_no
        self.doctor_test_02 = doctor_test_02 if doctor_test_02 is not None else set()
        self.patient_doctor_17 = patient_doctor_17 if patient_doctor_17 is not None else set()
        
        pass
    @property
    def phone_no(self):
        return self.__phone_no
    @phone_no.setter
    def phone_no(self, phone_no: str):
        self.__phone_no = phone_no

    @property
    def specilization(self):
        return self.__specilization
    @specilization.setter
    def specilization(self, specilization: str):
        self.__specilization = specilization

    @property
    def dept(self):
        return self.__dept
    @dept.setter
    def dept(self, dept: str):
        self.__dept = dept

    @property
    def did(self):
        return self.__did
    @did.setter
    def did(self, did: str):
        self.__did = did

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def doctor_test_02(self):
        return self.__doctor_test_02
    @doctor_test_02.setter
    def doctor_test_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__doctor_test_02", None)
        self.__doctor_test_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor_test_13"):
                    opp_val = getattr(item, "doctor_test_13", None)
                    
                    if opp_val == self:
                        setattr(item, "doctor_test_13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor_test_13"):
                    opp_val = getattr(item, "doctor_test_13", None)
                    
                    setattr(item, "doctor_test_13", self)
                    

    @property
    def patient_doctor_17(self):
        return self.__patient_doctor_17
    @patient_doctor_17.setter
    def patient_doctor_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__patient_doctor_17", None)
        self.__patient_doctor_17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient_doctor_06"):
                    opp_val = getattr(item, "patient_doctor_06", None)
                    
                    if opp_val == self:
                        setattr(item, "patient_doctor_06", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient_doctor_06"):
                    opp_val = getattr(item, "patient_doctor_06", None)
                    
                    setattr(item, "patient_doctor_06", self)
                    



class patient:

    def __init__(self, pid: str, name: str, phone_no: str, address: str, age: str, room_no: str, patient_room_04: "room" = None, patient_doctor_06: "doctor" = None, patient_billing_08: "Bill" = None):
        self.pid = pid
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.age = age
        self.room_no = room_no
        self.patient_room_04 = patient_room_04
        self.patient_doctor_06 = patient_doctor_06
        self.patient_billing_08 = patient_billing_08
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def room_no(self):
        return self.__room_no
    @room_no.setter
    def room_no(self, room_no: str):
        self.__room_no = room_no

    @property
    def pid(self):
        return self.__pid
    @pid.setter
    def pid(self, pid: str):
        self.__pid = pid

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: str):
        self.__age = age

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def phone_no(self):
        return self.__phone_no
    @phone_no.setter
    def phone_no(self, phone_no: str):
        self.__phone_no = phone_no

    @property
    def patient_doctor_06(self):
        return self.__patient_doctor_06
    @patient_doctor_06.setter
    def patient_doctor_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__patient_doctor_06", None)
        self.__patient_doctor_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_doctor_17"):
                opp_val = getattr(old_value, "patient_doctor_17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_doctor_17"):
                opp_val = getattr(value, "patient_doctor_17", None)
                if opp_val is None:
                    setattr(value, "patient_doctor_17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patient_billing_08(self):
        return self.__patient_billing_08
    @patient_billing_08.setter
    def patient_billing_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__patient_billing_08", None)
        self.__patient_billing_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_billing_19"):
                opp_val = getattr(old_value, "patient_billing_19", None)
                if opp_val == self:
                    setattr(old_value, "patient_billing_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_billing_19"):
                opp_val = getattr(value, "patient_billing_19", None)
                setattr(value, "patient_billing_19", self)

    @property
    def patient_room_04(self):
        return self.__patient_room_04
    @patient_room_04.setter
    def patient_room_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__patient_room_04", None)
        self.__patient_room_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_room_15"):
                opp_val = getattr(old_value, "patient_room_15", None)
                if opp_val == self:
                    setattr(old_value, "patient_room_15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_room_15"):
                opp_val = getattr(value, "patient_room_15", None)
                setattr(value, "patient_room_15", self)



class staff:

    def __init__(self, name: str, department_staff_11: set["department"] = None):
        self.name = name
        self.department_staff_11 = department_staff_11 if department_staff_11 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def department_staff_11(self):
        return self.__department_staff_11
    @department_staff_11.setter
    def department_staff_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_staff__department_staff_11", None)
        self.__department_staff_11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department_staff_00"):
                    opp_val = getattr(item, "department_staff_00", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department_staff_00"):
                    opp_val = getattr(item, "department_staff_00", None)
                    
                    if opp_val is None:
                        setattr(item, "department_staff_00", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class department:

    def __init__(self, depart_id: str, loacation: str, department_staff_00: set["staff"] = None):
        self.depart_id = depart_id
        self.loacation = loacation
        self.department_staff_00 = department_staff_00 if department_staff_00 is not None else set()
        
        pass
    @property
    def loacation(self):
        return self.__loacation
    @loacation.setter
    def loacation(self, loacation: str):
        self.__loacation = loacation

    @property
    def depart_id(self):
        return self.__depart_id
    @depart_id.setter
    def depart_id(self, depart_id: str):
        self.__depart_id = depart_id

    @property
    def department_staff_00(self):
        return self.__department_staff_00
    @department_staff_00.setter
    def department_staff_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_department__department_staff_00", None)
        self.__department_staff_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department_staff_11"):
                    opp_val = getattr(item, "department_staff_11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department_staff_11"):
                    opp_val = getattr(item, "department_staff_11", None)
                    
                    if opp_val is None:
                        setattr(item, "department_staff_11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

