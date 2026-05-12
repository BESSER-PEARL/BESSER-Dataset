from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Health_Records:

    def __init__(self, healthhistory: str, doctor19: "Doctor" = None, patient20: "Patient" = None):
        self.healthhistory = healthhistory
        self.doctor19 = doctor19
        self.patient20 = patient20
        
        pass
    @property
    def healthhistory(self):
        return self.__healthhistory
    @healthhistory.setter
    def healthhistory(self, healthhistory: str):
        self.__healthhistory = healthhistory

    @property
    def patient20(self):
        return self.__patient20
    @patient20.setter
    def patient20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Health_Records__patient20", None)
        self.__patient20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "health_Records21"):
                opp_val = getattr(old_value, "health_Records21", None)
                if opp_val == self:
                    setattr(old_value, "health_Records21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "health_Records21"):
                opp_val = getattr(value, "health_Records21", None)
                setattr(value, "health_Records21", self)

    @property
    def doctor19(self):
        return self.__doctor19
    @doctor19.setter
    def doctor19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Health_Records__doctor19", None)
        self.__doctor19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "health_Records18"):
                opp_val = getattr(old_value, "health_Records18", None)
                if opp_val == self:
                    setattr(old_value, "health_Records18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "health_Records18"):
                opp_val = getattr(value, "health_Records18", None)
                setattr(value, "health_Records18", self)



class Sickness:

    def __init__(self, symptoms: str, recommendations: str, prescription: str, patient16: "Patient" = None):
        self.symptoms = symptoms
        self.recommendations = recommendations
        self.prescription = prescription
        self.patient16 = patient16
        
        pass
    @property
    def prescription(self):
        return self.__prescription
    @prescription.setter
    def prescription(self, prescription: str):
        self.__prescription = prescription

    @property
    def recommendations(self):
        return self.__recommendations
    @recommendations.setter
    def recommendations(self, recommendations: str):
        self.__recommendations = recommendations

    @property
    def symptoms(self):
        return self.__symptoms
    @symptoms.setter
    def symptoms(self, symptoms: str):
        self.__symptoms = symptoms

    @property
    def patient16(self):
        return self.__patient16
    @patient16.setter
    def patient16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sickness__patient16", None)
        self.__patient16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sickness17"):
                opp_val = getattr(old_value, "sickness17", None)
                if opp_val == self:
                    setattr(old_value, "sickness17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sickness17"):
                opp_val = getattr(value, "sickness17", None)
                setattr(value, "sickness17", self)



class Appointment:

    def __init__(self, date: str, time: int, location: str, patient14: "Patient" = None, doctor12: "Doctor" = None):
        self.date = date
        self.time = time
        self.location = location
        self.patient14 = patient14
        self.doctor12 = doctor12
        
        pass
    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: int):
        self.__time = time

    @property
    def doctor12(self):
        return self.__doctor12
    @doctor12.setter
    def doctor12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__doctor12", None)
        self.__doctor12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment13"):
                opp_val = getattr(old_value, "appointment13", None)
                if opp_val == self:
                    setattr(old_value, "appointment13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment13"):
                opp_val = getattr(value, "appointment13", None)
                setattr(value, "appointment13", self)

    @property
    def patient14(self):
        return self.__patient14
    @patient14.setter
    def patient14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__patient14", None)
        self.__patient14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment15"):
                opp_val = getattr(old_value, "appointment15", None)
                if opp_val == self:
                    setattr(old_value, "appointment15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment15"):
                opp_val = getattr(value, "appointment15", None)
                setattr(value, "appointment15", self)



class Patient:

    def __init__(self, healthrecords: str, name: str, id: int, appointment15: "Appointment" = None, sickness17: "Sickness" = None, health_Records21: "Health_Records" = None, person11: "Person" = None):
        self.healthrecords = healthrecords
        self.name = name
        self.id = id
        self.appointment15 = appointment15
        self.sickness17 = sickness17
        self.health_Records21 = health_Records21
        self.person11 = person11
        
        pass
    @property
    def healthrecords(self):
        return self.__healthrecords
    @healthrecords.setter
    def healthrecords(self, healthrecords: str):
        self.__healthrecords = healthrecords

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def person11(self):
        return self.__person11
    @person11.setter
    def person11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__person11", None)
        self.__person11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient10"):
                opp_val = getattr(old_value, "patient10", None)
                if opp_val == self:
                    setattr(old_value, "patient10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient10"):
                opp_val = getattr(value, "patient10", None)
                setattr(value, "patient10", self)

    @property
    def appointment15(self):
        return self.__appointment15
    @appointment15.setter
    def appointment15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__appointment15", None)
        self.__appointment15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient14"):
                opp_val = getattr(old_value, "patient14", None)
                if opp_val == self:
                    setattr(old_value, "patient14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient14"):
                opp_val = getattr(value, "patient14", None)
                setattr(value, "patient14", self)

    @property
    def health_Records21(self):
        return self.__health_Records21
    @health_Records21.setter
    def health_Records21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__health_Records21", None)
        self.__health_Records21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient20"):
                opp_val = getattr(old_value, "patient20", None)
                if opp_val == self:
                    setattr(old_value, "patient20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient20"):
                opp_val = getattr(value, "patient20", None)
                setattr(value, "patient20", self)

    @property
    def sickness17(self):
        return self.__sickness17
    @sickness17.setter
    def sickness17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__sickness17", None)
        self.__sickness17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient16"):
                opp_val = getattr(old_value, "patient16", None)
                if opp_val == self:
                    setattr(old_value, "patient16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient16"):
                opp_val = getattr(value, "patient16", None)
                setattr(value, "patient16", self)



class Medicine:

    def __init__(self, name: str, code: int, price: str, amount: int, doctor9: "Doctor" = None):
        self.name = name
        self.code = code
        self.price = price
        self.amount = amount
        self.doctor9 = doctor9
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: int):
        self.__amount = amount

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def doctor9(self):
        return self.__doctor9
    @doctor9.setter
    def doctor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medicine__doctor9", None)
        self.__doctor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicine8"):
                opp_val = getattr(old_value, "medicine8", None)
                if opp_val == self:
                    setattr(old_value, "medicine8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicine8"):
                opp_val = getattr(value, "medicine8", None)
                setattr(value, "medicine8", self)



class Technician:

    def __init__(self, name: str, id: int, staff7: "Staff" = None):
        self.name = name
        self.id = id
        self.staff7 = staff7
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def staff7(self):
        return self.__staff7
    @staff7.setter
    def staff7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Technician__staff7", None)
        self.__staff7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "technician6"):
                opp_val = getattr(old_value, "technician6", None)
                if opp_val == self:
                    setattr(old_value, "technician6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "technician6"):
                opp_val = getattr(value, "technician6", None)
                setattr(value, "technician6", self)



class Doctor:

    def __init__(self, speciality: str, name: str, id: int, health_Records18: "Health_Records" = None, staff5: "Staff" = None, medicine8: "Medicine" = None, appointment13: "Appointment" = None):
        self.speciality = speciality
        self.name = name
        self.id = id
        self.health_Records18 = health_Records18
        self.staff5 = staff5
        self.medicine8 = medicine8
        self.appointment13 = appointment13
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def speciality(self):
        return self.__speciality
    @speciality.setter
    def speciality(self, speciality: str):
        self.__speciality = speciality

    @property
    def appointment13(self):
        return self.__appointment13
    @appointment13.setter
    def appointment13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__appointment13", None)
        self.__appointment13 = value
        
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

    @property
    def staff5(self):
        return self.__staff5
    @staff5.setter
    def staff5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__staff5", None)
        self.__staff5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor4"):
                opp_val = getattr(old_value, "doctor4", None)
                if opp_val == self:
                    setattr(old_value, "doctor4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor4"):
                opp_val = getattr(value, "doctor4", None)
                setattr(value, "doctor4", self)

    @property
    def health_Records18(self):
        return self.__health_Records18
    @health_Records18.setter
    def health_Records18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__health_Records18", None)
        self.__health_Records18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor19"):
                opp_val = getattr(old_value, "doctor19", None)
                if opp_val == self:
                    setattr(old_value, "doctor19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor19"):
                opp_val = getattr(value, "doctor19", None)
                setattr(value, "doctor19", self)

    @property
    def medicine8(self):
        return self.__medicine8
    @medicine8.setter
    def medicine8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__medicine8", None)
        self.__medicine8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor9"):
                opp_val = getattr(old_value, "doctor9", None)
                if opp_val == self:
                    setattr(old_value, "doctor9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor9"):
                opp_val = getattr(value, "doctor9", None)
                setattr(value, "doctor9", self)



class Nurse:

    def __init__(self, name: str, id: int, staff3: "Staff" = None):
        self.name = name
        self.id = id
        self.staff3 = staff3
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def staff3(self):
        return self.__staff3
    @staff3.setter
    def staff3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nurse__staff3", None)
        self.__staff3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nurse2"):
                opp_val = getattr(old_value, "nurse2", None)
                if opp_val == self:
                    setattr(old_value, "nurse2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nurse2"):
                opp_val = getattr(value, "nurse2", None)
                setattr(value, "nurse2", self)



class Staff:

    def __init__(self, name: str, job: str, person1: "Person" = None, nurse2: "Nurse" = None, doctor4: "Doctor" = None, technician6: "Technician" = None):
        self.name = name
        self.job = job
        self.person1 = person1
        self.nurse2 = nurse2
        self.doctor4 = doctor4
        self.technician6 = technician6
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def job(self):
        return self.__job
    @job.setter
    def job(self, job: str):
        self.__job = job

    @property
    def doctor4(self):
        return self.__doctor4
    @doctor4.setter
    def doctor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__doctor4", None)
        self.__doctor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff5"):
                opp_val = getattr(old_value, "staff5", None)
                if opp_val == self:
                    setattr(old_value, "staff5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff5"):
                opp_val = getattr(value, "staff5", None)
                setattr(value, "staff5", self)

    @property
    def nurse2(self):
        return self.__nurse2
    @nurse2.setter
    def nurse2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__nurse2", None)
        self.__nurse2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff3"):
                opp_val = getattr(old_value, "staff3", None)
                if opp_val == self:
                    setattr(old_value, "staff3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff3"):
                opp_val = getattr(value, "staff3", None)
                setattr(value, "staff3", self)

    @property
    def person1(self):
        return self.__person1
    @person1.setter
    def person1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__person1", None)
        self.__person1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff0"):
                opp_val = getattr(old_value, "staff0", None)
                if opp_val == self:
                    setattr(old_value, "staff0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff0"):
                opp_val = getattr(value, "staff0", None)
                setattr(value, "staff0", self)

    @property
    def technician6(self):
        return self.__technician6
    @technician6.setter
    def technician6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Staff__technician6", None)
        self.__technician6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "staff7"):
                opp_val = getattr(old_value, "staff7", None)
                if opp_val == self:
                    setattr(old_value, "staff7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "staff7"):
                opp_val = getattr(value, "staff7", None)
                setattr(value, "staff7", self)



class Person:

    def __init__(self, name: str, id: int, email: str, job: str, staff0: "Staff" = None, patient10: "Patient" = None):
        self.name = name
        self.id = id
        self.email = email
        self.job = job
        self.staff0 = staff0
        self.patient10 = patient10
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def job(self):
        return self.__job
    @job.setter
    def job(self, job: str):
        self.__job = job

    @property
    def staff0(self):
        return self.__staff0
    @staff0.setter
    def staff0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__staff0", None)
        self.__staff0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person1"):
                opp_val = getattr(old_value, "person1", None)
                if opp_val == self:
                    setattr(old_value, "person1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person1"):
                opp_val = getattr(value, "person1", None)
                setattr(value, "person1", self)

    @property
    def patient10(self):
        return self.__patient10
    @patient10.setter
    def patient10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__patient10", None)
        self.__patient10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person11"):
                opp_val = getattr(old_value, "person11", None)
                if opp_val == self:
                    setattr(old_value, "person11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person11"):
                opp_val = getattr(value, "person11", None)
                setattr(value, "person11", self)

