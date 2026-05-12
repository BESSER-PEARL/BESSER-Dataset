from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class pharmacy:

    def __init__(self, medicine: str, price: int, medicine_cost8: "Bursar" = None, gives_medicine10: "Patient" = None):
        self.medicine = medicine
        self.price = price
        self.medicine_cost8 = medicine_cost8
        self.gives_medicine10 = gives_medicine10
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def medicine(self):
        return self.__medicine
    @medicine.setter
    def medicine(self, medicine: str):
        self.__medicine = medicine

    @property
    def medicine_cost8(self):
        return self.__medicine_cost8
    @medicine_cost8.setter
    def medicine_cost8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pharmacy__medicine_cost8", None)
        self.__medicine_cost8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pharmacy9"):
                opp_val = getattr(old_value, "pharmacy9", None)
                if opp_val == self:
                    setattr(old_value, "pharmacy9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pharmacy9"):
                opp_val = getattr(value, "pharmacy9", None)
                setattr(value, "pharmacy9", self)

    @property
    def gives_medicine10(self):
        return self.__gives_medicine10
    @gives_medicine10.setter
    def gives_medicine10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pharmacy__gives_medicine10", None)
        self.__gives_medicine10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pharmacy11"):
                opp_val = getattr(old_value, "pharmacy11", None)
                if opp_val == self:
                    setattr(old_value, "pharmacy11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pharmacy11"):
                opp_val = getattr(value, "pharmacy11", None)
                setattr(value, "pharmacy11", self)



class lab:

    def __init__(self, results: str, price: int, assign4: "Patient" = None, assign6: "Doctor" = None):
        self.results = results
        self.price = price
        self.assign4 = assign4
        self.assign6 = assign6
        
        pass
    @property
    def results(self):
        return self.__results
    @results.setter
    def results(self, results: str):
        self.__results = results

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def assign6(self):
        return self.__assign6
    @assign6.setter
    def assign6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab__assign6", None)
        self.__assign6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lab7"):
                opp_val = getattr(old_value, "lab7", None)
                if opp_val == self:
                    setattr(old_value, "lab7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lab7"):
                opp_val = getattr(value, "lab7", None)
                setattr(value, "lab7", self)

    @property
    def assign4(self):
        return self.__assign4
    @assign4.setter
    def assign4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_lab__assign4", None)
        self.__assign4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "lab5"):
                opp_val = getattr(old_value, "lab5", None)
                if opp_val == self:
                    setattr(old_value, "lab5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "lab5"):
                opp_val = getattr(value, "lab5", None)
                setattr(value, "lab5", self)



class Bursar:

    def __init__(self, firstname: str, lastname: str, pharmacy9: "pharmacy" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.pharmacy9 = pharmacy9
        
        pass
    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def pharmacy9(self):
        return self.__pharmacy9
    @pharmacy9.setter
    def pharmacy9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bursar__pharmacy9", None)
        self.__pharmacy9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicine_cost8"):
                opp_val = getattr(old_value, "medicine_cost8", None)
                if opp_val == self:
                    setattr(old_value, "medicine_cost8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicine_cost8"):
                opp_val = getattr(value, "medicine_cost8", None)
                setattr(value, "medicine_cost8", self)



class medicine:

    def __init__(self, id: int, medicine: str, price: int):
        self.id = id
        self.medicine = medicine
        self.price = price
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def medicine(self):
        return self.__medicine
    @medicine.setter
    def medicine(self, medicine: str):
        self.__medicine = medicine

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class Bill:

    def __init__(self, billno: str, amount: float, pat1: "Patient" = None):
        self.billno = billno
        self.amount = amount
        self.pat1 = pat1
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def billno(self):
        return self.__billno
    @billno.setter
    def billno(self, billno: str):
        self.__billno = billno

    @property
    def pat1(self):
        return self.__pat1
    @pat1.setter
    def pat1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__pat1", None)
        self.__pat1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill0"):
                opp_val = getattr(old_value, "bill0", None)
                if opp_val == self:
                    setattr(old_value, "bill0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill0"):
                opp_val = getattr(value, "bill0", None)
                setattr(value, "bill0", self)



class Receptionist:

    def __init__(self, firstname: str, lastname: str, p3: "Patient" = None):
        self.firstname = firstname
        self.lastname = lastname
        self.p3 = p3
        
        pass
    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def p3(self):
        return self.__p3
    @p3.setter
    def p3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__p3", None)
        self.__p3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist2"):
                opp_val = getattr(old_value, "receptionist2", None)
                if opp_val == self:
                    setattr(old_value, "receptionist2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist2"):
                opp_val = getattr(value, "receptionist2", None)
                setattr(value, "receptionist2", self)



class Room:

    def __init__(self, roomno: int, roomname: str):
        self.roomno = roomno
        self.roomname = roomname
        
        pass
    @property
    def roomname(self):
        return self.__roomname
    @roomname.setter
    def roomname(self, roomname: str):
        self.__roomname = roomname

    @property
    def roomno(self):
        return self.__roomno
    @roomno.setter
    def roomno(self, roomno: int):
        self.__roomno = roomno



class Patient:

    def __init__(self, id: int, firstname: str, lastname: str, phonenumber: int, birthyear: int, sex: str, blood_group: int, addr: str, email: str, bill0: "Bill" = None, receptionist2: "Receptionist" = None, lab5: "lab" = None, pharmacy11: "pharmacy" = None, doctor12: "Doctor" = None):
        self.id = id
        self.firstname = firstname
        self.lastname = lastname
        self.phonenumber = phonenumber
        self.birthyear = birthyear
        self.sex = sex
        self.blood_group = blood_group
        self.addr = addr
        self.email = email
        self.bill0 = bill0
        self.receptionist2 = receptionist2
        self.lab5 = lab5
        self.pharmacy11 = pharmacy11
        self.doctor12 = doctor12
        
        pass
    @property
    def lastname(self):
        return self.__lastname
    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def phonenumber(self):
        return self.__phonenumber
    @phonenumber.setter
    def phonenumber(self, phonenumber: int):
        self.__phonenumber = phonenumber

    @property
    def blood_group(self):
        return self.__blood_group
    @blood_group.setter
    def blood_group(self, blood_group: int):
        self.__blood_group = blood_group

    @property
    def firstname(self):
        return self.__firstname
    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def birthyear(self):
        return self.__birthyear
    @birthyear.setter
    def birthyear(self, birthyear: int):
        self.__birthyear = birthyear

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def addr(self):
        return self.__addr
    @addr.setter
    def addr(self, addr: str):
        self.__addr = addr

    @property
    def lab5(self):
        return self.__lab5
    @lab5.setter
    def lab5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__lab5", None)
        self.__lab5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assign4"):
                opp_val = getattr(old_value, "assign4", None)
                if opp_val == self:
                    setattr(old_value, "assign4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assign4"):
                opp_val = getattr(value, "assign4", None)
                setattr(value, "assign4", self)

    @property
    def bill0(self):
        return self.__bill0
    @bill0.setter
    def bill0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill0", None)
        self.__bill0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pat1"):
                opp_val = getattr(old_value, "pat1", None)
                if opp_val == self:
                    setattr(old_value, "pat1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pat1"):
                opp_val = getattr(value, "pat1", None)
                setattr(value, "pat1", self)

    @property
    def doctor12(self):
        return self.__doctor12
    @doctor12.setter
    def doctor12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor12", None)
        self.__doctor12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient13"):
                opp_val = getattr(old_value, "patient13", None)
                if opp_val == self:
                    setattr(old_value, "patient13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient13"):
                opp_val = getattr(value, "patient13", None)
                setattr(value, "patient13", self)

    @property
    def pharmacy11(self):
        return self.__pharmacy11
    @pharmacy11.setter
    def pharmacy11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__pharmacy11", None)
        self.__pharmacy11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "gives_medicine10"):
                opp_val = getattr(old_value, "gives_medicine10", None)
                if opp_val == self:
                    setattr(old_value, "gives_medicine10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "gives_medicine10"):
                opp_val = getattr(value, "gives_medicine10", None)
                setattr(value, "gives_medicine10", self)

    @property
    def receptionist2(self):
        return self.__receptionist2
    @receptionist2.setter
    def receptionist2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__receptionist2", None)
        self.__receptionist2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p3"):
                opp_val = getattr(old_value, "p3", None)
                if opp_val == self:
                    setattr(old_value, "p3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p3"):
                opp_val = getattr(value, "p3", None)
                setattr(value, "p3", self)



class Doctor:

    def __init__(self, dentist: Doctor, women_doctor: Doctor, normal_doctor: Doctor, lab7: "lab" = None, patient13: "Patient" = None):
        self.dentist = dentist
        self.women_doctor = women_doctor
        self.normal_doctor = normal_doctor
        self.lab7 = lab7
        self.patient13 = patient13
        
        pass
    @property
    def dentist(self):
        return self.__dentist
    @dentist.setter
    def dentist(self, dentist: Doctor):
        self.__dentist = dentist

    @property
    def normal_doctor(self):
        return self.__normal_doctor
    @normal_doctor.setter
    def normal_doctor(self, normal_doctor: Doctor):
        self.__normal_doctor = normal_doctor

    @property
    def women_doctor(self):
        return self.__women_doctor
    @women_doctor.setter
    def women_doctor(self, women_doctor: Doctor):
        self.__women_doctor = women_doctor

    @property
    def lab7(self):
        return self.__lab7
    @lab7.setter
    def lab7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__lab7", None)
        self.__lab7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assign6"):
                opp_val = getattr(old_value, "assign6", None)
                if opp_val == self:
                    setattr(old_value, "assign6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assign6"):
                opp_val = getattr(value, "assign6", None)
                setattr(value, "assign6", self)

    @property
    def patient13(self):
        return self.__patient13
    @patient13.setter
    def patient13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__patient13", None)
        self.__patient13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor12"):
                opp_val = getattr(old_value, "doctor12", None)
                if opp_val == self:
                    setattr(old_value, "doctor12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor12"):
                opp_val = getattr(value, "doctor12", None)
                setattr(value, "doctor12", self)

