from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Doctor:

    def __init__(self, registorno: str, specialization: str, corporation: str, personel4: "Personel" = None, personel11: "Personel" = None, appointment18: set["Appointment"] = None):
        self.registorno = registorno
        self.specialization = specialization
        self.corporation = corporation
        self.personel4 = personel4
        self.personel11 = personel11
        self.appointment18 = appointment18 if appointment18 is not None else set()
        
        pass
    @property
    def corporation(self):
        return self.__corporation
    @corporation.setter
    def corporation(self, corporation: str):
        self.__corporation = corporation

    @property
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, specialization: str):
        self.__specialization = specialization

    @property
    def registorno(self):
        return self.__registorno
    @registorno.setter
    def registorno(self, registorno: str):
        self.__registorno = registorno

    @property
    def personel11(self):
        return self.__personel11
    @personel11.setter
    def personel11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__personel11", None)
        self.__personel11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor10"):
                opp_val = getattr(old_value, "doctor10", None)
                if opp_val == self:
                    setattr(old_value, "doctor10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor10"):
                opp_val = getattr(value, "doctor10", None)
                setattr(value, "doctor10", self)

    @property
    def personel4(self):
        return self.__personel4
    @personel4.setter
    def personel4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__personel4", None)
        self.__personel4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor5"):
                opp_val = getattr(old_value, "doctor5", None)
                if opp_val == self:
                    setattr(old_value, "doctor5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor5"):
                opp_val = getattr(value, "doctor5", None)
                setattr(value, "doctor5", self)

    @property
    def appointment18(self):
        return self.__appointment18
    @appointment18.setter
    def appointment18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__appointment18", None)
        self.__appointment18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor19"):
                    opp_val = getattr(item, "doctor19", None)
                    
                    if opp_val == self:
                        setattr(item, "doctor19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor19"):
                    opp_val = getattr(item, "doctor19", None)
                    
                    setattr(item, "doctor19", self)
                    



class Personel:

    def __init__(self, tcno: str, name: str, attribute: str, registerno: str, tcno1: str, name1: str, gender: str, position: str, corporation: str, attribute7: str, patient1: "Patient" = None, patient3: "Patient" = None, doctor5: "Doctor" = None, corporation26: "Corporation" = None, hospitals8: "Hospitals" = None, doctor10: "Doctor" = None, corporation13: "Corporation" = None, receptionist39: "Receptionist" = None, receptionist42: "Receptionist" = None, hospitals15: "Hospitals" = None):
        self.tcno = tcno
        self.name = name
        self.attribute = attribute
        self.registerno = registerno
        self.tcno1 = tcno1
        self.name1 = name1
        self.gender = gender
        self.position = position
        self.corporation = corporation
        self.attribute7 = attribute7
        self.patient1 = patient1
        self.patient3 = patient3
        self.doctor5 = doctor5
        self.corporation26 = corporation26
        self.hospitals8 = hospitals8
        self.doctor10 = doctor10
        self.corporation13 = corporation13
        self.receptionist39 = receptionist39
        self.receptionist42 = receptionist42
        self.hospitals15 = hospitals15
        
        pass
    @property
    def registerno(self):
        return self.__registerno
    @registerno.setter
    def registerno(self, registerno: str):
        self.__registerno = registerno

    @property
    def attribute7(self):
        return self.__attribute7
    @attribute7.setter
    def attribute7(self, attribute7: str):
        self.__attribute7 = attribute7

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def name1(self):
        return self.__name1
    @name1.setter
    def name1(self, name1: str):
        self.__name1 = name1

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def corporation(self):
        return self.__corporation
    @corporation.setter
    def corporation(self, corporation: str):
        self.__corporation = corporation

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def tcno(self):
        return self.__tcno
    @tcno.setter
    def tcno(self, tcno: str):
        self.__tcno = tcno

    @property
    def tcno1(self):
        return self.__tcno1
    @tcno1.setter
    def tcno1(self, tcno1: str):
        self.__tcno1 = tcno1

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def receptionist39(self):
        return self.__receptionist39
    @receptionist39.setter
    def receptionist39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__receptionist39", None)
        self.__receptionist39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personel38"):
                opp_val = getattr(old_value, "personel38", None)
                if opp_val == self:
                    setattr(old_value, "personel38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personel38"):
                opp_val = getattr(value, "personel38", None)
                setattr(value, "personel38", self)

    @property
    def patient3(self):
        return self.__patient3
    @patient3.setter
    def patient3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__patient3", None)
        self.__patient3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor2"):
                opp_val = getattr(old_value, "doctor2", None)
                if opp_val == self:
                    setattr(old_value, "doctor2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor2"):
                opp_val = getattr(value, "doctor2", None)
                setattr(value, "doctor2", self)

    @property
    def patient1(self):
        return self.__patient1
    @patient1.setter
    def patient1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__patient1", None)
        self.__patient1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor0"):
                opp_val = getattr(old_value, "doctor0", None)
                if opp_val == self:
                    setattr(old_value, "doctor0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor0"):
                opp_val = getattr(value, "doctor0", None)
                setattr(value, "doctor0", self)

    @property
    def corporation26(self):
        return self.__corporation26
    @corporation26.setter
    def corporation26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__corporation26", None)
        self.__corporation26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personel7"):
                opp_val = getattr(old_value, "personel7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personel7"):
                opp_val = getattr(value, "personel7", None)
                if opp_val is None:
                    setattr(value, "personel7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def receptionist42(self):
        return self.__receptionist42
    @receptionist42.setter
    def receptionist42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__receptionist42", None)
        self.__receptionist42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personel43"):
                opp_val = getattr(old_value, "personel43", None)
                if opp_val == self:
                    setattr(old_value, "personel43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personel43"):
                opp_val = getattr(value, "personel43", None)
                setattr(value, "personel43", self)

    @property
    def doctor10(self):
        return self.__doctor10
    @doctor10.setter
    def doctor10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__doctor10", None)
        self.__doctor10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personel11"):
                opp_val = getattr(old_value, "personel11", None)
                if opp_val == self:
                    setattr(old_value, "personel11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personel11"):
                opp_val = getattr(value, "personel11", None)
                setattr(value, "personel11", self)

    @property
    def corporation13(self):
        return self.__corporation13
    @corporation13.setter
    def corporation13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__corporation13", None)
        self.__corporation13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personel12"):
                opp_val = getattr(old_value, "personel12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personel12"):
                opp_val = getattr(value, "personel12", None)
                if opp_val is None:
                    setattr(value, "personel12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def hospitals8(self):
        return self.__hospitals8
    @hospitals8.setter
    def hospitals8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__hospitals8", None)
        self.__hospitals8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personel9"):
                opp_val = getattr(old_value, "personel9", None)
                if opp_val == self:
                    setattr(old_value, "personel9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personel9"):
                opp_val = getattr(value, "personel9", None)
                setattr(value, "personel9", self)

    @property
    def doctor5(self):
        return self.__doctor5
    @doctor5.setter
    def doctor5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__doctor5", None)
        self.__doctor5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personel4"):
                opp_val = getattr(old_value, "personel4", None)
                if opp_val == self:
                    setattr(old_value, "personel4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personel4"):
                opp_val = getattr(value, "personel4", None)
                setattr(value, "personel4", self)

    @property
    def hospitals15(self):
        return self.__hospitals15
    @hospitals15.setter
    def hospitals15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personel__hospitals15", None)
        self.__hospitals15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "personel14"):
                opp_val = getattr(old_value, "personel14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "personel14"):
                opp_val = getattr(value, "personel14", None)
                if opp_val is None:
                    setattr(value, "personel14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Patient:

    def __init__(self, name: str, telno: str, address: str, birth: str, gender: str, tcno: str, tcno1: str, name1: str, telno1: str, address1: str, birth1: str, gender1: str, attribute: str, patient_Medicines26: "Patient_Medicines" = None, doctor0: "Personel" = None, doctor2: "Personel" = None, patient_Prescription28: "Patient_Prescription" = None, receptionist41: "Receptionist" = None, appointment16: set["Appointment"] = None):
        self.name = name
        self.telno = telno
        self.address = address
        self.birth = birth
        self.gender = gender
        self.tcno = tcno
        self.tcno1 = tcno1
        self.name1 = name1
        self.telno1 = telno1
        self.address1 = address1
        self.birth1 = birth1
        self.gender1 = gender1
        self.attribute = attribute
        self.patient_Medicines26 = patient_Medicines26
        self.doctor0 = doctor0
        self.doctor2 = doctor2
        self.patient_Prescription28 = patient_Prescription28
        self.receptionist41 = receptionist41
        self.appointment16 = appointment16 if appointment16 is not None else set()
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def gender1(self):
        return self.__gender1
    @gender1.setter
    def gender1(self, gender1: str):
        self.__gender1 = gender1

    @property
    def address1(self):
        return self.__address1
    @address1.setter
    def address1(self, address1: str):
        self.__address1 = address1

    @property
    def tcno(self):
        return self.__tcno
    @tcno.setter
    def tcno(self, tcno: str):
        self.__tcno = tcno

    @property
    def tcno1(self):
        return self.__tcno1
    @tcno1.setter
    def tcno1(self, tcno1: str):
        self.__tcno1 = tcno1

    @property
    def name1(self):
        return self.__name1
    @name1.setter
    def name1(self, name1: str):
        self.__name1 = name1

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def telno1(self):
        return self.__telno1
    @telno1.setter
    def telno1(self, telno1: str):
        self.__telno1 = telno1

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

    @property
    def birth1(self):
        return self.__birth1
    @birth1.setter
    def birth1(self, birth1: str):
        self.__birth1 = birth1

    @property
    def telno(self):
        return self.__telno
    @telno.setter
    def telno(self, telno: str):
        self.__telno = telno

    @property
    def birth(self):
        return self.__birth
    @birth.setter
    def birth(self, birth: str):
        self.__birth = birth

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def patient_Prescription28(self):
        return self.__patient_Prescription28
    @patient_Prescription28.setter
    def patient_Prescription28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__patient_Prescription28", None)
        self.__patient_Prescription28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient29"):
                opp_val = getattr(old_value, "patient29", None)
                if opp_val == self:
                    setattr(old_value, "patient29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient29"):
                opp_val = getattr(value, "patient29", None)
                setattr(value, "patient29", self)

    @property
    def patient_Medicines26(self):
        return self.__patient_Medicines26
    @patient_Medicines26.setter
    def patient_Medicines26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__patient_Medicines26", None)
        self.__patient_Medicines26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient27"):
                opp_val = getattr(old_value, "patient27", None)
                if opp_val == self:
                    setattr(old_value, "patient27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient27"):
                opp_val = getattr(value, "patient27", None)
                setattr(value, "patient27", self)

    @property
    def doctor0(self):
        return self.__doctor0
    @doctor0.setter
    def doctor0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor0", None)
        self.__doctor0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient1"):
                opp_val = getattr(old_value, "patient1", None)
                if opp_val == self:
                    setattr(old_value, "patient1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient1"):
                opp_val = getattr(value, "patient1", None)
                setattr(value, "patient1", self)

    @property
    def doctor2(self):
        return self.__doctor2
    @doctor2.setter
    def doctor2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctor2", None)
        self.__doctor2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient3"):
                opp_val = getattr(old_value, "patient3", None)
                if opp_val == self:
                    setattr(old_value, "patient3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient3"):
                opp_val = getattr(value, "patient3", None)
                setattr(value, "patient3", self)

    @property
    def appointment16(self):
        return self.__appointment16
    @appointment16.setter
    def appointment16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__appointment16", None)
        self.__appointment16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient17"):
                    opp_val = getattr(item, "patient17", None)
                    
                    if opp_val == self:
                        setattr(item, "patient17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient17"):
                    opp_val = getattr(item, "patient17", None)
                    
                    setattr(item, "patient17", self)
                    

    @property
    def receptionist41(self):
        return self.__receptionist41
    @receptionist41.setter
    def receptionist41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__receptionist41", None)
        self.__receptionist41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient40"):
                opp_val = getattr(old_value, "patient40", None)
                if opp_val == self:
                    setattr(old_value, "patient40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient40"):
                opp_val = getattr(value, "patient40", None)
                setattr(value, "patient40", self)



class Bill:

    def __init__(self, no: int, patientno: int, amount: str):
        self.no = no
        self.patientno = patientno
        self.amount = amount
        
        pass
    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: str):
        self.__amount = amount

    @property
    def patientno(self):
        return self.__patientno
    @patientno.setter
    def patientno(self, patientno: int):
        self.__patientno = patientno

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no



class Receptionist:

    def __init__(self, no: int, checkroom: str, personel38: "Personel" = None, patient40: "Patient" = None, personel43: "Personel" = None):
        self.no = no
        self.checkroom = checkroom
        self.personel38 = personel38
        self.patient40 = patient40
        self.personel43 = personel43
        
        pass
    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def checkroom(self):
        return self.__checkroom
    @checkroom.setter
    def checkroom(self, checkroom: str):
        self.__checkroom = checkroom

    @property
    def patient40(self):
        return self.__patient40
    @patient40.setter
    def patient40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__patient40", None)
        self.__patient40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist41"):
                opp_val = getattr(old_value, "receptionist41", None)
                if opp_val == self:
                    setattr(old_value, "receptionist41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist41"):
                opp_val = getattr(value, "receptionist41", None)
                setattr(value, "receptionist41", self)

    @property
    def personel43(self):
        return self.__personel43
    @personel43.setter
    def personel43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__personel43", None)
        self.__personel43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist42"):
                opp_val = getattr(old_value, "receptionist42", None)
                if opp_val == self:
                    setattr(old_value, "receptionist42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist42"):
                opp_val = getattr(value, "receptionist42", None)
                setattr(value, "receptionist42", self)

    @property
    def personel38(self):
        return self.__personel38
    @personel38.setter
    def personel38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__personel38", None)
        self.__personel38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist39"):
                opp_val = getattr(old_value, "receptionist39", None)
                if opp_val == self:
                    setattr(old_value, "receptionist39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist39"):
                opp_val = getattr(value, "receptionist39", None)
                setattr(value, "receptionist39", self)



class Room:

    def __init__(self, no: int, floor: int, buildingname: str, appointment22: "Appointment" = None):
        self.no = no
        self.floor = floor
        self.buildingname = buildingname
        self.appointment22 = appointment22
        
        pass
    @property
    def buildingname(self):
        return self.__buildingname
    @buildingname.setter
    def buildingname(self, buildingname: str):
        self.__buildingname = buildingname

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def floor(self):
        return self.__floor
    @floor.setter
    def floor(self, floor: int):
        self.__floor = floor

    @property
    def appointment22(self):
        return self.__appointment22
    @appointment22.setter
    def appointment22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__appointment22", None)
        self.__appointment22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room23"):
                opp_val = getattr(old_value, "room23", None)
                if opp_val == self:
                    setattr(old_value, "room23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room23"):
                opp_val = getattr(value, "room23", None)
                setattr(value, "room23", self)



class Patient_Medicines:

    def __init__(self, no: int, patientno: str, medicines: str, quantities: int, patient27: "Patient" = None, patient_Prescription33: set["Patient_Prescription"] = None, medicine34: set["Medicine"] = None):
        self.no = no
        self.patientno = patientno
        self.medicines = medicines
        self.quantities = quantities
        self.patient27 = patient27
        self.patient_Prescription33 = patient_Prescription33 if patient_Prescription33 is not None else set()
        self.medicine34 = medicine34 if medicine34 is not None else set()
        
        pass
    @property
    def medicines(self):
        return self.__medicines
    @medicines.setter
    def medicines(self, medicines: str):
        self.__medicines = medicines

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def quantities(self):
        return self.__quantities
    @quantities.setter
    def quantities(self, quantities: int):
        self.__quantities = quantities

    @property
    def patientno(self):
        return self.__patientno
    @patientno.setter
    def patientno(self, patientno: str):
        self.__patientno = patientno

    @property
    def patient_Prescription33(self):
        return self.__patient_Prescription33
    @patient_Prescription33.setter
    def patient_Prescription33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient_Medicines__patient_Prescription33", None)
        self.__patient_Prescription33 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient_Medicines32"):
                    opp_val = getattr(item, "patient_Medicines32", None)
                    
                    if opp_val == self:
                        setattr(item, "patient_Medicines32", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient_Medicines32"):
                    opp_val = getattr(item, "patient_Medicines32", None)
                    
                    setattr(item, "patient_Medicines32", self)
                    

    @property
    def medicine34(self):
        return self.__medicine34
    @medicine34.setter
    def medicine34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient_Medicines__medicine34", None)
        self.__medicine34 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient_Medicines35"):
                    opp_val = getattr(item, "patient_Medicines35", None)
                    
                    if opp_val == self:
                        setattr(item, "patient_Medicines35", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient_Medicines35"):
                    opp_val = getattr(item, "patient_Medicines35", None)
                    
                    setattr(item, "patient_Medicines35", self)
                    

    @property
    def patient27(self):
        return self.__patient27
    @patient27.setter
    def patient27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient_Medicines__patient27", None)
        self.__patient27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_Medicines26"):
                opp_val = getattr(old_value, "patient_Medicines26", None)
                if opp_val == self:
                    setattr(old_value, "patient_Medicines26", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_Medicines26"):
                opp_val = getattr(value, "patient_Medicines26", None)
                setattr(value, "patient_Medicines26", self)



class diagnosis:

    def __init__(self, id: int, diagnoses: str, examination25: "Examination" = None, disease36: set["Disease"] = None):
        self.id = id
        self.diagnoses = diagnoses
        self.examination25 = examination25
        self.disease36 = disease36 if disease36 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def diagnoses(self):
        return self.__diagnoses
    @diagnoses.setter
    def diagnoses(self, diagnoses: str):
        self.__diagnoses = diagnoses

    @property
    def examination25(self):
        return self.__examination25
    @examination25.setter
    def examination25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagnosis__examination25", None)
        self.__examination25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "diagnosis24"):
                opp_val = getattr(old_value, "diagnosis24", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "diagnosis24"):
                opp_val = getattr(value, "diagnosis24", None)
                if opp_val is None:
                    setattr(value, "diagnosis24", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def disease36(self):
        return self.__disease36
    @disease36.setter
    def disease36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_diagnosis__disease36", None)
        self.__disease36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "diagnosis37"):
                    opp_val = getattr(item, "diagnosis37", None)
                    
                    if opp_val == self:
                        setattr(item, "diagnosis37", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "diagnosis37"):
                    opp_val = getattr(item, "diagnosis37", None)
                    
                    setattr(item, "diagnosis37", self)
                    



class Examination:

    def __init__(self, no: int, attribute: str, Appointmentid: int, diagnosisid: int, diagnosis24: set["diagnosis"] = None, appointment20: "Appointment" = None):
        self.no = no
        self.attribute = attribute
        self.Appointmentid = Appointmentid
        self.diagnosisid = diagnosisid
        self.diagnosis24 = diagnosis24 if diagnosis24 is not None else set()
        self.appointment20 = appointment20
        
        pass
    @property
    def diagnosisid(self):
        return self.__diagnosisid
    @diagnosisid.setter
    def diagnosisid(self, diagnosisid: int):
        self.__diagnosisid = diagnosisid

    @property
    def Appointmentid(self):
        return self.__Appointmentid
    @Appointmentid.setter
    def Appointmentid(self, Appointmentid: int):
        self.__Appointmentid = Appointmentid

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def diagnosis24(self):
        return self.__diagnosis24
    @diagnosis24.setter
    def diagnosis24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Examination__diagnosis24", None)
        self.__diagnosis24 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "examination25"):
                    opp_val = getattr(item, "examination25", None)
                    
                    if opp_val == self:
                        setattr(item, "examination25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "examination25"):
                    opp_val = getattr(item, "examination25", None)
                    
                    setattr(item, "examination25", self)
                    

    @property
    def appointment20(self):
        return self.__appointment20
    @appointment20.setter
    def appointment20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Examination__appointment20", None)
        self.__appointment20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "examination21"):
                opp_val = getattr(old_value, "examination21", None)
                if opp_val == self:
                    setattr(old_value, "examination21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "examination21"):
                opp_val = getattr(value, "examination21", None)
                setattr(value, "examination21", self)



class Appointment:

    def __init__(self, no: str, doctoradi: int, date: str, time: str, room: int, attribute: str, patient17: "Patient" = None, doctor19: "Doctor" = None, examination21: "Examination" = None, room23: "Room" = None):
        self.no = no
        self.doctoradi = doctoradi
        self.date = date
        self.time = time
        self.room = room
        self.attribute = attribute
        self.patient17 = patient17
        self.doctor19 = doctor19
        self.examination21 = examination21
        self.room23 = room23
        
        pass
    @property
    def room(self):
        return self.__room
    @room.setter
    def room(self, room: int):
        self.__room = room

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: str):
        self.__no = no

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def doctoradi(self):
        return self.__doctoradi
    @doctoradi.setter
    def doctoradi(self, doctoradi: int):
        self.__doctoradi = doctoradi

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
    def time(self, time: str):
        self.__time = time

    @property
    def examination21(self):
        return self.__examination21
    @examination21.setter
    def examination21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__examination21", None)
        self.__examination21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment20"):
                opp_val = getattr(old_value, "appointment20", None)
                if opp_val == self:
                    setattr(old_value, "appointment20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment20"):
                opp_val = getattr(value, "appointment20", None)
                setattr(value, "appointment20", self)

    @property
    def doctor19(self):
        return self.__doctor19
    @doctor19.setter
    def doctor19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__doctor19", None)
        self.__doctor19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment18"):
                opp_val = getattr(old_value, "appointment18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment18"):
                opp_val = getattr(value, "appointment18", None)
                if opp_val is None:
                    setattr(value, "appointment18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patient17(self):
        return self.__patient17
    @patient17.setter
    def patient17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__patient17", None)
        self.__patient17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment16"):
                opp_val = getattr(old_value, "appointment16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment16"):
                opp_val = getattr(value, "appointment16", None)
                if opp_val is None:
                    setattr(value, "appointment16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def room23(self):
        return self.__room23
    @room23.setter
    def room23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__room23", None)
        self.__room23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment22"):
                opp_val = getattr(old_value, "appointment22", None)
                if opp_val == self:
                    setattr(old_value, "appointment22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment22"):
                opp_val = getattr(value, "appointment22", None)
                setattr(value, "appointment22", self)



class Patient_Prescription:

    def __init__(self, code: int, code1: int, patientid: int, diseaseid: int, date: str, medicineid: int, patient29: "Patient" = None, disease30: "Disease" = None, patient_Medicines32: "Patient_Medicines" = None):
        self.code = code
        self.code1 = code1
        self.patientid = patientid
        self.diseaseid = diseaseid
        self.date = date
        self.medicineid = medicineid
        self.patient29 = patient29
        self.disease30 = disease30
        self.patient_Medicines32 = patient_Medicines32
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def code1(self):
        return self.__code1
    @code1.setter
    def code1(self, code1: int):
        self.__code1 = code1

    @property
    def patientid(self):
        return self.__patientid
    @patientid.setter
    def patientid(self, patientid: int):
        self.__patientid = patientid

    @property
    def medicineid(self):
        return self.__medicineid
    @medicineid.setter
    def medicineid(self, medicineid: int):
        self.__medicineid = medicineid

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def diseaseid(self):
        return self.__diseaseid
    @diseaseid.setter
    def diseaseid(self, diseaseid: int):
        self.__diseaseid = diseaseid

    @property
    def patient29(self):
        return self.__patient29
    @patient29.setter
    def patient29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient_Prescription__patient29", None)
        self.__patient29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_Prescription28"):
                opp_val = getattr(old_value, "patient_Prescription28", None)
                if opp_val == self:
                    setattr(old_value, "patient_Prescription28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_Prescription28"):
                opp_val = getattr(value, "patient_Prescription28", None)
                setattr(value, "patient_Prescription28", self)

    @property
    def disease30(self):
        return self.__disease30
    @disease30.setter
    def disease30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient_Prescription__disease30", None)
        self.__disease30 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_Prescription31"):
                opp_val = getattr(old_value, "patient_Prescription31", None)
                if opp_val == self:
                    setattr(old_value, "patient_Prescription31", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_Prescription31"):
                opp_val = getattr(value, "patient_Prescription31", None)
                setattr(value, "patient_Prescription31", self)

    @property
    def patient_Medicines32(self):
        return self.__patient_Medicines32
    @patient_Medicines32.setter
    def patient_Medicines32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient_Prescription__patient_Medicines32", None)
        self.__patient_Medicines32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient_Prescription33"):
                opp_val = getattr(old_value, "patient_Prescription33", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient_Prescription33"):
                opp_val = getattr(value, "patient_Prescription33", None)
                if opp_val is None:
                    setattr(value, "patient_Prescription33", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Medicine:

    def __init__(self, code: int, name: str, price: str, type: str, patient_Medicines35: "Patient_Medicines" = None):
        self.code = code
        self.name = name
        self.price = price
        self.type = type
        self.patient_Medicines35 = patient_Medicines35
        
        pass
    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: str):
        self.__price = price

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def patient_Medicines35(self):
        return self.__patient_Medicines35
    @patient_Medicines35.setter
    def patient_Medicines35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medicine__patient_Medicines35", None)
        self.__patient_Medicines35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicine34"):
                opp_val = getattr(old_value, "medicine34", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicine34"):
                opp_val = getattr(value, "medicine34", None)
                if opp_val is None:
                    setattr(value, "medicine34", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Disease:

    def __init__(self, code: int, name: str, type: str, patient_Prescription31: "Patient_Prescription" = None, diagnosis37: "diagnosis" = None):
        self.code = code
        self.name = name
        self.type = type
        self.patient_Prescription31 = patient_Prescription31
        self.diagnosis37 = diagnosis37
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: int):
        self.__code = code

    @property
    def patient_Prescription31(self):
        return self.__patient_Prescription31
    @patient_Prescription31.setter
    def patient_Prescription31(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Disease__patient_Prescription31", None)
        self.__patient_Prescription31 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "disease30"):
                opp_val = getattr(old_value, "disease30", None)
                if opp_val == self:
                    setattr(old_value, "disease30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "disease30"):
                opp_val = getattr(value, "disease30", None)
                setattr(value, "disease30", self)

    @property
    def diagnosis37(self):
        return self.__diagnosis37
    @diagnosis37.setter
    def diagnosis37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Disease__diagnosis37", None)
        self.__diagnosis37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "disease36"):
                opp_val = getattr(old_value, "disease36", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "disease36"):
                opp_val = getattr(value, "disease36", None)
                if opp_val is None:
                    setattr(value, "disease36", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Hospitals:

    def __init__(self, no: int, type: str, address: str, name: str, personel9: "Personel" = None, personel14: set["Personel"] = None):
        self.no = no
        self.type = type
        self.address = address
        self.name = name
        self.personel9 = personel9
        self.personel14 = personel14 if personel14 is not None else set()
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def personel9(self):
        return self.__personel9
    @personel9.setter
    def personel9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospitals__personel9", None)
        self.__personel9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hospitals8"):
                opp_val = getattr(old_value, "hospitals8", None)
                if opp_val == self:
                    setattr(old_value, "hospitals8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hospitals8"):
                opp_val = getattr(value, "hospitals8", None)
                setattr(value, "hospitals8", self)

    @property
    def personel14(self):
        return self.__personel14
    @personel14.setter
    def personel14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospitals__personel14", None)
        self.__personel14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "hospitals15"):
                    opp_val = getattr(item, "hospitals15", None)
                    
                    if opp_val == self:
                        setattr(item, "hospitals15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "hospitals15"):
                    opp_val = getattr(item, "hospitals15", None)
                    
                    setattr(item, "hospitals15", self)
                    



class Corporation:

    def __init__(self, no: int, name: str, address: str, personel7: set["Personel"] = None, personel12: set["Personel"] = None):
        self.no = no
        self.name = name
        self.address = address
        self.personel7 = personel7 if personel7 is not None else set()
        self.personel12 = personel12 if personel12 is not None else set()
        
        pass
    @property
    def no(self):
        return self.__no
    @no.setter
    def no(self, no: int):
        self.__no = no

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def personel12(self):
        return self.__personel12
    @personel12.setter
    def personel12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Corporation__personel12", None)
        self.__personel12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "corporation13"):
                    opp_val = getattr(item, "corporation13", None)
                    
                    if opp_val == self:
                        setattr(item, "corporation13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "corporation13"):
                    opp_val = getattr(item, "corporation13", None)
                    
                    setattr(item, "corporation13", self)
                    

    @property
    def personel7(self):
        return self.__personel7
    @personel7.setter
    def personel7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Corporation__personel7", None)
        self.__personel7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "corporation26"):
                    opp_val = getattr(item, "corporation26", None)
                    
                    if opp_val == self:
                        setattr(item, "corporation26", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "corporation26"):
                    opp_val = getattr(item, "corporation26", None)
                    
                    setattr(item, "corporation26", self)
                    

