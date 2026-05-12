from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Procedure:

    def __init__(self, name: str, price: int, idProcedure: int, treatment12: set["Treatment"] = None):
        self.name = name
        self.price = price
        self.idProcedure = idProcedure
        self.treatment12 = treatment12 if treatment12 is not None else set()
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int):
        self.__price = price

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def idProcedure(self):
        return self.__idProcedure
    @idProcedure.setter
    def idProcedure(self, idProcedure: int):
        self.__idProcedure = idProcedure

    @property
    def treatment12(self):
        return self.__treatment12
    @treatment12.setter
    def treatment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Procedure__treatment12", None)
        self.__treatment12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "procedure13"):
                    opp_val = getattr(item, "procedure13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "procedure13"):
                    opp_val = getattr(item, "procedure13", None)
                    
                    if opp_val is None:
                        setattr(item, "procedure13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Treatment:

    def __init__(self, idTreatment: int, idBill: int, patientID: int, procedureID: int, procedure13: set["Procedure"] = None, patient10: "Patient" = None):
        self.idTreatment = idTreatment
        self.idBill = idBill
        self.patientID = patientID
        self.procedureID = procedureID
        self.procedure13 = procedure13 if procedure13 is not None else set()
        self.patient10 = patient10
        
        pass
    @property
    def idBill(self):
        return self.__idBill
    @idBill.setter
    def idBill(self, idBill: int):
        self.__idBill = idBill

    @property
    def procedureID(self):
        return self.__procedureID
    @procedureID.setter
    def procedureID(self, procedureID: int):
        self.__procedureID = procedureID

    @property
    def idTreatment(self):
        return self.__idTreatment
    @idTreatment.setter
    def idTreatment(self, idTreatment: int):
        self.__idTreatment = idTreatment

    @property
    def patientID(self):
        return self.__patientID
    @patientID.setter
    def patientID(self, patientID: int):
        self.__patientID = patientID

    @property
    def procedure13(self):
        return self.__procedure13
    @procedure13.setter
    def procedure13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Treatment__procedure13", None)
        self.__procedure13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "treatment12"):
                    opp_val = getattr(item, "treatment12", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "treatment12"):
                    opp_val = getattr(item, "treatment12", None)
                    
                    if opp_val is None:
                        setattr(item, "treatment12", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def patient10(self):
        return self.__patient10
    @patient10.setter
    def patient10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Treatment__patient10", None)
        self.__patient10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "treatment11"):
                opp_val = getattr(old_value, "treatment11", None)
                if opp_val == self:
                    setattr(old_value, "treatment11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "treatment11"):
                opp_val = getattr(value, "treatment11", None)
                setattr(value, "treatment11", self)



class Bill:

    def __init__(self, billno: str, patientname: str, amount: float, pat5: set["Patient"] = None, receptionist9: set["Receptionist"] = None):
        self.billno = billno
        self.patientname = patientname
        self.amount = amount
        self.pat5 = pat5 if pat5 is not None else set()
        self.receptionist9 = receptionist9 if receptionist9 is not None else set()
        
        pass
    @property
    def patientname(self):
        return self.__patientname
    @patientname.setter
    def patientname(self, patientname: str):
        self.__patientname = patientname

    @property
    def billno(self):
        return self.__billno
    @billno.setter
    def billno(self, billno: str):
        self.__billno = billno

    @property
    def amount(self):
        return self.__amount
    @amount.setter
    def amount(self, amount: float):
        self.__amount = amount

    @property
    def receptionist9(self):
        return self.__receptionist9
    @receptionist9.setter
    def receptionist9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist9", None)
        self.__receptionist9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sbill8"):
                    opp_val = getattr(item, "sbill8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sbill8"):
                    opp_val = getattr(item, "sbill8", None)
                    
                    if opp_val is None:
                        setattr(item, "sbill8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def pat5(self):
        return self.__pat5
    @pat5.setter
    def pat5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__pat5", None)
        self.__pat5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bill4"):
                    opp_val = getattr(item, "bill4", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bill4"):
                    opp_val = getattr(item, "bill4", None)
                    
                    if opp_val is None:
                        setattr(item, "bill4", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Receptionist:

    def __init__(self, id: int, attribute2: str, p7: "Patient" = None, sbill8: set["Bill"] = None):
        self.id = id
        self.attribute2 = attribute2
        self.p7 = p7
        self.sbill8 = sbill8 if sbill8 is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def p7(self):
        return self.__p7
    @p7.setter
    def p7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__p7", None)
        self.__p7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist6"):
                opp_val = getattr(old_value, "receptionist6", None)
                if opp_val == self:
                    setattr(old_value, "receptionist6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist6"):
                opp_val = getattr(value, "receptionist6", None)
                setattr(value, "receptionist6", self)

    @property
    def sbill8(self):
        return self.__sbill8
    @sbill8.setter
    def sbill8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__sbill8", None)
        self.__sbill8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist9"):
                    opp_val = getattr(item, "receptionist9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist9"):
                    opp_val = getattr(item, "receptionist9", None)
                    
                    if opp_val is None:
                        setattr(item, "receptionist9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Patient:

    def __init__(self, id: int, name: str, telno: int, address: str, age: int, sex: str, doctors1: set["Doctor"] = None, bill4: set["Bill"] = None, receptionist6: "Receptionist" = None, treatment11: "Treatment" = None):
        self.id = id
        self.name = name
        self.telno = telno
        self.address = address
        self.age = age
        self.sex = sex
        self.doctors1 = doctors1 if doctors1 is not None else set()
        self.bill4 = bill4 if bill4 is not None else set()
        self.receptionist6 = receptionist6
        self.treatment11 = treatment11
        
        pass
    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def telno(self):
        return self.__telno
    @telno.setter
    def telno(self, telno: int):
        self.__telno = telno

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

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def bill4(self):
        return self.__bill4
    @bill4.setter
    def bill4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill4", None)
        self.__bill4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pat5"):
                    opp_val = getattr(item, "pat5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pat5"):
                    opp_val = getattr(item, "pat5", None)
                    
                    if opp_val is None:
                        setattr(item, "pat5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def receptionist6(self):
        return self.__receptionist6
    @receptionist6.setter
    def receptionist6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__receptionist6", None)
        self.__receptionist6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p7"):
                opp_val = getattr(old_value, "p7", None)
                if opp_val == self:
                    setattr(old_value, "p7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p7"):
                opp_val = getattr(value, "p7", None)
                setattr(value, "p7", self)

    @property
    def doctors1(self):
        return self.__doctors1
    @doctors1.setter
    def doctors1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__doctors1", None)
        self.__doctors1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patients0"):
                    opp_val = getattr(item, "patients0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patients0"):
                    opp_val = getattr(item, "patients0", None)
                    
                    if opp_val is None:
                        setattr(item, "patients0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def treatment11(self):
        return self.__treatment11
    @treatment11.setter
    def treatment11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__treatment11", None)
        self.__treatment11 = value
        
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



class Department:

    def __init__(self, id: int, name: str, doctor3: set["Doctor"] = None):
        self.id = id
        self.name = name
        self.doctor3 = doctor3 if doctor3 is not None else set()
        
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
    def doctor3(self):
        return self.__doctor3
    @doctor3.setter
    def doctor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__doctor3", None)
        self.__doctor3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "depmt2"):
                    opp_val = getattr(item, "depmt2", None)
                    
                    if opp_val == self:
                        setattr(item, "depmt2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "depmt2"):
                    opp_val = getattr(item, "depmt2", None)
                    
                    setattr(item, "depmt2", self)
                    



class Doctor:

    def __init__(self, docid: int, name: str, department: str, specialization: str, phno: int, address: str, departamentID: int, patients0: set["Patient"] = None, depmt2: "Department" = None):
        self.docid = docid
        self.name = name
        self.department = department
        self.specialization = specialization
        self.phno = phno
        self.address = address
        self.departamentID = departamentID
        self.patients0 = patients0 if patients0 is not None else set()
        self.depmt2 = depmt2
        
        pass
    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, specialization: str):
        self.__specialization = specialization

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def departamentID(self):
        return self.__departamentID
    @departamentID.setter
    def departamentID(self, departamentID: int):
        self.__departamentID = departamentID

    @property
    def docid(self):
        return self.__docid
    @docid.setter
    def docid(self, docid: int):
        self.__docid = docid

    @property
    def phno(self):
        return self.__phno
    @phno.setter
    def phno(self, phno: int):
        self.__phno = phno

    @property
    def depmt2(self):
        return self.__depmt2
    @depmt2.setter
    def depmt2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__depmt2", None)
        self.__depmt2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor3"):
                opp_val = getattr(old_value, "doctor3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor3"):
                opp_val = getattr(value, "doctor3", None)
                if opp_val is None:
                    setattr(value, "doctor3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patients0(self):
        return self.__patients0
    @patients0.setter
    def patients0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__patients0", None)
        self.__patients0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctors1"):
                    opp_val = getattr(item, "doctors1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctors1"):
                    opp_val = getattr(item, "doctors1", None)
                    
                    if opp_val is None:
                        setattr(item, "doctors1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

