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

    def __init__(self, id: str, name: str, pass1: str, receptionist11: "receptionist" = None):
        self.id = id
        self.name = name
        self.pass1 = pass1
        self.receptionist11 = receptionist11
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def pass1(self):
        return self.__pass1
    @pass1.setter
    def pass1(self, pass1: str):
        self.__pass = pass1

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def receptionist11(self):
        return self.__receptionist11
    @receptionist11.setter
    def receptionist11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_login__receptionist11", None)
        self.__receptionist11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "login10"):
                opp_val = getattr(old_value, "login10", None)
                if opp_val == self:
                    setattr(old_value, "login10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "login10"):
                opp_val = getattr(value, "login10", None)
                setattr(value, "login10", self)



class loan:

    def __init__(self, patient_name: str, amount: str, billing15: "billing" = None):
        self.patient_name = patient_name
        self.amount = amount
        self.billing15 = billing15
        
        pass
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
    def billing15(self):
        return self.__billing15
    @billing15.setter
    def billing15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_loan__billing15", None)
        self.__billing15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "loan14"):
                opp_val = getattr(old_value, "loan14", None)
                if opp_val == self:
                    setattr(old_value, "loan14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "loan14"):
                opp_val = getattr(value, "loan14", None)
                setattr(value, "loan14", self)



class billing:

    def __init__(self, bill_no: str, patient_name: str, amount: str, patient9: "patient" = None, receptionist13: "receptionist" = None, loan14: "loan" = None):
        self.bill_no = bill_no
        self.patient_name = patient_name
        self.amount = amount
        self.patient9 = patient9
        self.receptionist13 = receptionist13
        self.loan14 = loan14
        
        pass
    @property
    def patient_name(self):
        return self.__patient_name
    @patient_name.setter
    def patient_name(self, patient_name: str):
        self.__patient_name = patient_name

    @property
    def bill_no(self):
        return self.__bill_no
    @bill_no.setter
    def bill_no(self, bill_no: str):
        self.__bill_no = bill_no

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def loan14(self):
        return self.__loan14
    @loan14.setter
    def loan14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_billing__loan14", None)
        self.__loan14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "billing15"):
                opp_val = getattr(old_value, "billing15", None)
                if opp_val == self:
                    setattr(old_value, "billing15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "billing15"):
                opp_val = getattr(value, "billing15", None)
                setattr(value, "billing15", self)

    @property
    def receptionist13(self):
        return self.__receptionist13
    @receptionist13.setter
    def receptionist13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_billing__receptionist13", None)
        self.__receptionist13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "billing12"):
                opp_val = getattr(old_value, "billing12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "billing12"):
                opp_val = getattr(value, "billing12", None)
                if opp_val is None:
                    setattr(value, "billing12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patient9(self):
        return self.__patient9
    @patient9.setter
    def patient9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_billing__patient9", None)
        self.__patient9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "billing8"):
                opp_val = getattr(old_value, "billing8", None)
                if opp_val == self:
                    setattr(old_value, "billing8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "billing8"):
                opp_val = getattr(value, "billing8", None)
                setattr(value, "billing8", self)



class test:

    def __init__(self, disease_name: str, doctor3: "doctor" = None):
        self.disease_name = disease_name
        self.doctor3 = doctor3
        
        pass
    @property
    def disease_name(self):
        return self.__disease_name
    @disease_name.setter
    def disease_name(self, disease_name: str):
        self.__disease_name = disease_name

    @property
    def doctor3(self):
        return self.__doctor3
    @doctor3.setter
    def doctor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_test__doctor3", None)
        self.__doctor3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "test2"):
                opp_val = getattr(old_value, "test2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "test2"):
                opp_val = getattr(value, "test2", None)
                if opp_val is None:
                    setattr(value, "test2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class room:

    def __init__(self, room_no: str, patient5: "patient" = None):
        self.room_no = room_no
        self.patient5 = patient5
        
        pass
    @property
    def room_no(self):
        return self.__room_no
    @room_no.setter
    def room_no(self, room_no: str):
        self.__room_no = room_no

    @property
    def patient5(self):
        return self.__patient5
    @patient5.setter
    def patient5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_room__patient5", None)
        self.__patient5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room4"):
                opp_val = getattr(old_value, "room4", None)
                if opp_val == self:
                    setattr(old_value, "room4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room4"):
                opp_val = getattr(value, "room4", None)
                setattr(value, "room4", self)



class receptionist:

    def __init__(self, rid: str, name: str, login10: "login" = None, billing12: set["billing"] = None):
        self.rid = rid
        self.name = name
        self.login10 = login10
        self.billing12 = billing12 if billing12 is not None else set()
        
        pass
    @property
    def rid(self):
        return self.__rid
    @rid.setter
    def rid(self, rid: str):
        self.__rid = rid

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def billing12(self):
        return self.__billing12
    @billing12.setter
    def billing12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_receptionist__billing12", None)
        self.__billing12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist13"):
                    opp_val = getattr(item, "receptionist13", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionist13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist13"):
                    opp_val = getattr(item, "receptionist13", None)
                    
                    setattr(item, "receptionist13", self)
                    

    @property
    def login10(self):
        return self.__login10
    @login10.setter
    def login10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_receptionist__login10", None)
        self.__login10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist11"):
                opp_val = getattr(old_value, "receptionist11", None)
                if opp_val == self:
                    setattr(old_value, "receptionist11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist11"):
                opp_val = getattr(value, "receptionist11", None)
                setattr(value, "receptionist11", self)



class doctor:

    def __init__(self, did: str, name: str, dept: str, specilization: str, phone_no: str, test2: set["test"] = None, patient7: set["patient"] = None):
        self.did = did
        self.name = name
        self.dept = dept
        self.specilization = specilization
        self.phone_no = phone_no
        self.test2 = test2 if test2 is not None else set()
        self.patient7 = patient7 if patient7 is not None else set()
        
        pass
    @property
    def phone_no(self):
        return self.__phone_no
    @phone_no.setter
    def phone_no(self, phone_no: str):
        self.__phone_no = phone_no

    @property
    def did(self):
        return self.__did
    @did.setter
    def did(self, did: str):
        self.__did = did

    @property
    def dept(self):
        return self.__dept
    @dept.setter
    def dept(self, dept: str):
        self.__dept = dept

    @property
    def specilization(self):
        return self.__specilization
    @specilization.setter
    def specilization(self, specilization: str):
        self.__specilization = specilization

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def patient7(self):
        return self.__patient7
    @patient7.setter
    def patient7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__patient7", None)
        self.__patient7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor6"):
                    opp_val = getattr(item, "doctor6", None)
                    
                    if opp_val == self:
                        setattr(item, "doctor6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor6"):
                    opp_val = getattr(item, "doctor6", None)
                    
                    setattr(item, "doctor6", self)
                    

    @property
    def test2(self):
        return self.__test2
    @test2.setter
    def test2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__test2", None)
        self.__test2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor3"):
                    opp_val = getattr(item, "doctor3", None)
                    
                    if opp_val == self:
                        setattr(item, "doctor3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor3"):
                    opp_val = getattr(item, "doctor3", None)
                    
                    setattr(item, "doctor3", self)
                    



class patient:

    def __init__(self, pid: str, name: str, phone_no: str, address: str, age: str, room_no: str, room4: "room" = None, doctor6: "doctor" = None, billing8: "billing" = None):
        self.pid = pid
        self.name = name
        self.phone_no = phone_no
        self.address = address
        self.age = age
        self.room_no = room_no
        self.room4 = room4
        self.doctor6 = doctor6
        self.billing8 = billing8
        
        pass
    @property
    def room_no(self):
        return self.__room_no
    @room_no.setter
    def room_no(self, room_no: str):
        self.__room_no = room_no

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
    def pid(self):
        return self.__pid
    @pid.setter
    def pid(self, pid: str):
        self.__pid = pid

    @property
    def phone_no(self):
        return self.__phone_no
    @phone_no.setter
    def phone_no(self, phone_no: str):
        self.__phone_no = phone_no

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def doctor6(self):
        return self.__doctor6
    @doctor6.setter
    def doctor6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__doctor6", None)
        self.__doctor6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient7"):
                opp_val = getattr(old_value, "patient7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient7"):
                opp_val = getattr(value, "patient7", None)
                if opp_val is None:
                    setattr(value, "patient7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def billing8(self):
        return self.__billing8
    @billing8.setter
    def billing8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__billing8", None)
        self.__billing8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient9"):
                opp_val = getattr(old_value, "patient9", None)
                if opp_val == self:
                    setattr(old_value, "patient9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient9"):
                opp_val = getattr(value, "patient9", None)
                setattr(value, "patient9", self)

    @property
    def room4(self):
        return self.__room4
    @room4.setter
    def room4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__room4", None)
        self.__room4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient5"):
                opp_val = getattr(old_value, "patient5", None)
                if opp_val == self:
                    setattr(old_value, "patient5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient5"):
                opp_val = getattr(value, "patient5", None)
                setattr(value, "patient5", self)



class staff:

    def __init__(self, name: str, department1: set["department"] = None):
        self.name = name
        self.department1 = department1 if department1 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def department1(self):
        return self.__department1
    @department1.setter
    def department1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_staff__department1", None)
        self.__department1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "staff0"):
                    opp_val = getattr(item, "staff0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "staff0"):
                    opp_val = getattr(item, "staff0", None)
                    
                    if opp_val is None:
                        setattr(item, "staff0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class department:

    def __init__(self, depart_id: str, loacation: str, staff0: set["staff"] = None):
        self.depart_id = depart_id
        self.loacation = loacation
        self.staff0 = staff0 if staff0 is not None else set()
        
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
    def staff0(self):
        return self.__staff0
    @staff0.setter
    def staff0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_department__staff0", None)
        self.__staff0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "department1"):
                    opp_val = getattr(item, "department1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "department1"):
                    opp_val = getattr(item, "department1", None)
                    
                    if opp_val is None:
                        setattr(item, "department1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

