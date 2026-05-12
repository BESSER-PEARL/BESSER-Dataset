from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class appointment:

    def __init__(self, day: int, hour: int, minute: int, duration: int):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration
        
        pass
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self, minute: int):
        self.__minute = minute

    @property
    def day(self):
        return self.__day
    @day.setter
    def day(self, day: int):
        self.__day = day

    @property
    def hour(self):
        return self.__hour
    @hour.setter
    def hour(self, hour: int):
        self.__hour = hour



class Room:

    def __init__(self, num: int, capasittity: int, patients: str, room_type: str, available: bool, patient0: "Patient" = None, nurse3: "nurse" = None):
        self.num = num
        self.capasittity = capasittity
        self.patients = patients
        self.room_type = room_type
        self.available = available
        self.patient0 = patient0
        self.nurse3 = nurse3
        
        pass
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def capasittity(self):
        return self.__capasittity
    @capasittity.setter
    def capasittity(self, capasittity: int):
        self.__capasittity = capasittity

    @property
    def patients(self):
        return self.__patients
    @patients.setter
    def patients(self, patients: str):
        self.__patients = patients

    @property
    def room_type(self):
        return self.__room_type
    @room_type.setter
    def room_type(self, room_type: str):
        self.__room_type = room_type

    @property
    def available(self):
        return self.__available
    @available.setter
    def available(self, available: bool):
        self.__available = available

    @property
    def patient0(self):
        return self.__patient0
    @patient0.setter
    def patient0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__patient0", None)
        self.__patient0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room1"):
                opp_val = getattr(old_value, "room1", None)
                if opp_val == self:
                    setattr(old_value, "room1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room1"):
                opp_val = getattr(value, "room1", None)
                setattr(value, "room1", self)

    @property
    def nurse3(self):
        return self.__nurse3
    @nurse3.setter
    def nurse3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__nurse3", None)
        self.__nurse3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room2"):
                opp_val = getattr(old_value, "room2", None)
                if opp_val == self:
                    setattr(old_value, "room2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room2"):
                opp_val = getattr(value, "room2", None)
                setattr(value, "room2", self)



class Patient:

    def __init__(self, illness: str, id: str, _doc: doctor, _nur: nurse, room1: "Room" = None, doctor4: "doctor" = None):
        self.illness = illness
        self.id = id
        self._doc = _doc
        self._nur = _nur
        self.room1 = room1
        self.doctor4 = doctor4
        
        pass
    @property
    def _doc(self):
        return self.___doc
    @_doc.setter
    def _doc(self, _doc: doctor):
        self.___doc = _doc

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def illness(self):
        return self.__illness
    @illness.setter
    def illness(self, illness: str):
        self.__illness = illness

    @property
    def _nur(self):
        return self.___nur
    @_nur.setter
    def _nur(self, _nur: nurse):
        self.___nur = _nur

    @property
    def doctor4(self):
        return self.__doctor4
    @doctor4.setter
    def doctor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor4", None)
        self.__doctor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_25"):
                opp_val = getattr(old_value, "patient_25", None)
                if opp_val == self:
                    setattr(old_value, "patient_25", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_25"):
                opp_val = getattr(value, "patient_25", None)
                setattr(value, "patient_25", self)

    @property
    def room1(self):
        return self.__room1
    @room1.setter
    def room1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__room1", None)
        self.__room1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient0"):
                opp_val = getattr(old_value, "patient0", None)
                if opp_val == self:
                    setattr(old_value, "patient0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient0"):
                opp_val = getattr(value, "patient0", None)
                setattr(value, "patient0", self)



class Receptionist:

    pass


class It:

    def __init__(self, password: str):
        self.password = password
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class nurse:

    def __init__(self, _rom: Room, room2: "Room" = None):
        self._rom = _rom
        self.room2 = room2
        
        pass
    @property
    def _rom(self):
        return self.___rom
    @_rom.setter
    def _rom(self, _rom: Room):
        self.___rom = _rom

    @property
    def room2(self):
        return self.__room2
    @room2.setter
    def room2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nurse__room2", None)
        self.__room2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nurse3"):
                opp_val = getattr(old_value, "nurse3", None)
                if opp_val == self:
                    setattr(old_value, "nurse3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nurse3"):
                opp_val = getattr(value, "nurse3", None)
                setattr(value, "nurse3", self)



class doctor:

    def __init__(self, weekappointment: str, patient: str, patient_25: "Patient" = None):
        self.weekappointment = weekappointment
        self.patient = patient
        self.patient_25 = patient_25
        
        pass
    @property
    def weekappointment(self):
        return self.__weekappointment
    @weekappointment.setter
    def weekappointment(self, weekappointment: str):
        self.__weekappointment = weekappointment

    @property
    def patient(self):
        return self.__patient
    @patient.setter
    def patient(self, patient: str):
        self.__patient = patient

    @property
    def patient_25(self):
        return self.__patient_25
    @patient_25.setter
    def patient_25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__patient_25", None)
        self.__patient_25 = value
        
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



class employee:

    def __init__(self, Salary: int, password: str, department: str, id: str):
        self.Salary = Salary
        self.password = password
        self.department = department
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: int):
        self.__Salary = Salary

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password



class Person:

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

