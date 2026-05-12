from __future__ import annotations
from datetime import datetime, date, time
from abc import ABC, abstractmethod

############################################
# Definition of Classes
############################################










class MainWindow:

    def __init__(self, _logicdoc: doctor, _logininit: It, _Loginnurs: employee, roomss: str, nursess: str, doctorss: str, patientss: str, itss: str, UI: str):
        self._logicdoc = _logicdoc
        self._logininit = _logininit
        self._Loginnurs = _Loginnurs
        self.roomss = roomss
        self.nursess = nursess
        self.doctorss = doctorss
        self.patientss = patientss
        self.itss = itss
        self.UI = UI
        
        pass
    @property
    def patientss(self):
        return self.__patientss
    @patientss.setter
    def patientss(self, patientss: str):
        self.__patientss = patientss

    @property
    def _logicdoc(self):
        return self.___logicdoc
    @_logicdoc.setter
    def _logicdoc(self, _logicdoc: doctor):
        self.___logicdoc = _logicdoc

    @property
    def itss(self):
        return self.__itss
    @itss.setter
    def itss(self, itss: str):
        self.__itss = itss

    @property
    def nursess(self):
        return self.__nursess
    @nursess.setter
    def nursess(self, nursess: str):
        self.__nursess = nursess

    @property
    def UI(self):
        return self.__UI
    @UI.setter
    def UI(self, UI: str):
        self.__UI = UI

    @property
    def doctorss(self):
        return self.__doctorss
    @doctorss.setter
    def doctorss(self, doctorss: str):
        self.__doctorss = doctorss

    @property
    def _logininit(self):
        return self.___logininit
    @_logininit.setter
    def _logininit(self, _logininit: It):
        self.___logininit = _logininit

    @property
    def roomss(self):
        return self.__roomss
    @roomss.setter
    def roomss(self, roomss: str):
        self.__roomss = roomss

    @property
    def _Loginnurs(self):
        return self.___Loginnurs
    @_Loginnurs.setter
    def _Loginnurs(self, _Loginnurs: employee):
        self.___Loginnurs = _Loginnurs



class appointment:

    def __init__(self, day: int, hour: int, minute: int, duration: int, title: str):
        self.day = day
        self.hour = hour
        self.minute = minute
        self.duration = duration
        self.title = title
        
        pass
    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

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

    @property
    def minute(self):
        return self.__minute
    @minute.setter
    def minute(self, minute: int):
        self.__minute = minute

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title



class Room:

    def __init__(self, num: int, capasittity: int, patients: str, room_type: str, available: bool, _nurs: nurse, patient0: "Patient" = None, nurse3: "nurse" = None):
        self.num = num
        self.capasittity = capasittity
        self.patients = patients
        self.room_type = room_type
        self.available = available
        self._nurs = _nurs
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
    def capasittity(self):
        return self.__capasittity
    @capasittity.setter
    def capasittity(self, capasittity: int):
        self.__capasittity = capasittity

    @property
    def _nurs(self):
        return self.___nurs
    @_nurs.setter
    def _nurs(self, _nurs: nurse):
        self.___nurs = _nurs

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

    def __init__(self, room: int, hasdoc: bool, hasroom: bool, disease: str, duration: int, room1: "Room" = None, doctor4: "doctor" = None):
        self.room = room
        self.hasdoc = hasdoc
        self.hasroom = hasroom
        self.disease = disease
        self.duration = duration
        self.room1 = room1
        self.doctor4 = doctor4
        
        pass
    @property
    def disease(self):
        return self.__disease
    @disease.setter
    def disease(self, disease: str):
        self.__disease = disease

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def hasdoc(self):
        return self.__hasdoc
    @hasdoc.setter
    def hasdoc(self, hasdoc: bool):
        self.__hasdoc = hasdoc

    @property
    def room(self):
        return self.__room
    @room.setter
    def room(self, room: int):
        self.__room = room

    @property
    def hasroom(self):
        return self.__hasroom
    @hasroom.setter
    def hasroom(self, hasroom: bool):
        self.__hasroom = hasroom

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



class It:

    def __init__(self, password: str, name: str):
        self.password = password
        self.name = name
        
        pass
    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

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



class employee(ABC):

    def __init__(self, password: str, department: str):
        self.password = password
        self.department = department
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department



class Person(ABC):

    def __init__(self, name: str, age: int):
        self.name = name
        self.age = age
        
        pass
    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

