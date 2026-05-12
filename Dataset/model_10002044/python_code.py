from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class nurse:

    def __init__(self, id: int, name: str, contact: int, availability: bool, room18: "Room" = None):
        self.id = id
        self.name = name
        self.contact = contact
        self.availability = availability
        self.room18 = room18
        
        pass
    @property
    def availability(self):
        return self.__availability
    @availability.setter
    def availability(self, availability: bool):
        self.__availability = availability

    @property
    def contact(self):
        return self.__contact
    @contact.setter
    def contact(self, contact: int):
        self.__contact = contact

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
    def room18(self):
        return self.__room18
    @room18.setter
    def room18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_nurse__room18", None)
        self.__room18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nurse19"):
                opp_val = getattr(old_value, "nurse19", None)
                if opp_val == self:
                    setattr(old_value, "nurse19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nurse19"):
                opp_val = getattr(value, "nurse19", None)
                setattr(value, "nurse19", self)



class medicine:

    def __init__(self, m_code: int, m_name: str, quantity: int, price: float, bill15: "Bill" = None, doctor17: "Doctor" = None):
        self.m_code = m_code
        self.m_name = m_name
        self.quantity = quantity
        self.price = price
        self.bill15 = bill15
        self.doctor17 = doctor17
        
        pass
    @property
    def quantity(self):
        return self.__quantity
    @quantity.setter
    def quantity(self, quantity: int):
        self.__quantity = quantity

    @property
    def m_code(self):
        return self.__m_code
    @m_code.setter
    def m_code(self, m_code: int):
        self.__m_code = m_code

    @property
    def m_name(self):
        return self.__m_name
    @m_name.setter
    def m_name(self, m_name: str):
        self.__m_name = m_name

    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def doctor17(self):
        return self.__doctor17
    @doctor17.setter
    def doctor17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_medicine__doctor17", None)
        self.__doctor17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicine16"):
                opp_val = getattr(old_value, "medicine16", None)
                if opp_val == self:
                    setattr(old_value, "medicine16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicine16"):
                opp_val = getattr(value, "medicine16", None)
                setattr(value, "medicine16", self)

    @property
    def bill15(self):
        return self.__bill15
    @bill15.setter
    def bill15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_medicine__bill15", None)
        self.__bill15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medicine14"):
                opp_val = getattr(old_value, "medicine14", None)
                if opp_val == self:
                    setattr(old_value, "medicine14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medicine14"):
                opp_val = getattr(value, "medicine14", None)
                setattr(value, "medicine14", self)



class appointment:

    def __init__(self, A_no: int, time: date, p_id: int, p_name: str, d_name: str, doctor9: "Doctor" = None, patient11: "Patient" = None):
        self.A_no = A_no
        self.time = time
        self.p_id = p_id
        self.p_name = p_name
        self.d_name = d_name
        self.doctor9 = doctor9
        self.patient11 = patient11
        
        pass
    @property
    def p_name(self):
        return self.__p_name
    @p_name.setter
    def p_name(self, p_name: str):
        self.__p_name = p_name

    @property
    def d_name(self):
        return self.__d_name
    @d_name.setter
    def d_name(self, d_name: str):
        self.__d_name = d_name

    @property
    def p_id(self):
        return self.__p_id
    @p_id.setter
    def p_id(self, p_id: int):
        self.__p_id = p_id

    @property
    def time(self):
        return self.__time
    @time.setter
    def time(self, time: date):
        self.__time = time

    @property
    def A_no(self):
        return self.__A_no
    @A_no.setter
    def A_no(self, A_no: int):
        self.__A_no = A_no

    @property
    def patient11(self):
        return self.__patient11
    @patient11.setter
    def patient11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appointment__patient11", None)
        self.__patient11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment10"):
                opp_val = getattr(old_value, "appointment10", None)
                if opp_val == self:
                    setattr(old_value, "appointment10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment10"):
                opp_val = getattr(value, "appointment10", None)
                setattr(value, "appointment10", self)

    @property
    def doctor9(self):
        return self.__doctor9
    @doctor9.setter
    def doctor9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_appointment__doctor9", None)
        self.__doctor9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment8"):
                opp_val = getattr(old_value, "appointment8", None)
                if opp_val == self:
                    setattr(old_value, "appointment8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment8"):
                opp_val = getattr(value, "appointment8", None)
                setattr(value, "appointment8", self)



class Bill:

    def __init__(self, billno: str, patientname: str, amount: float, pat3: "Patient" = None, receptionist7: "Receptionist" = None, medicine14: "medicine" = None):
        self.billno = billno
        self.patientname = patientname
        self.amount = amount
        self.pat3 = pat3
        self.receptionist7 = receptionist7
        self.medicine14 = medicine14
        
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
    def receptionist7(self):
        return self.__receptionist7
    @receptionist7.setter
    def receptionist7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__receptionist7", None)
        self.__receptionist7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill6"):
                opp_val = getattr(old_value, "bill6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill6"):
                opp_val = getattr(value, "bill6", None)
                if opp_val is None:
                    setattr(value, "bill6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def medicine14(self):
        return self.__medicine14
    @medicine14.setter
    def medicine14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__medicine14", None)
        self.__medicine14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill15"):
                opp_val = getattr(old_value, "bill15", None)
                if opp_val == self:
                    setattr(old_value, "bill15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill15"):
                opp_val = getattr(value, "bill15", None)
                setattr(value, "bill15", self)

    @property
    def pat3(self):
        return self.__pat3
    @pat3.setter
    def pat3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__pat3", None)
        self.__pat3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill2"):
                opp_val = getattr(old_value, "bill2", None)
                if opp_val == self:
                    setattr(old_value, "bill2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill2"):
                opp_val = getattr(value, "bill2", None)
                setattr(value, "bill2", self)



class Receptionist:

    def __init__(self, id: int, email: str, username: str, password: str, p5: "Patient" = None, bill6: set["Bill"] = None):
        self.id = id
        self.email = email
        self.username = username
        self.password = password
        self.p5 = p5
        self.bill6 = bill6 if bill6 is not None else set()
        
        pass
    @property
    def password(self):
        return self.__password
    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self):
        return self.__username
    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def bill6(self):
        return self.__bill6
    @bill6.setter
    def bill6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__bill6", None)
        self.__bill6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "receptionist7"):
                    opp_val = getattr(item, "receptionist7", None)
                    
                    if opp_val == self:
                        setattr(item, "receptionist7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "receptionist7"):
                    opp_val = getattr(item, "receptionist7", None)
                    
                    setattr(item, "receptionist7", self)
                    

    @property
    def p5(self):
        return self.__p5
    @p5.setter
    def p5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__p5", None)
        self.__p5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "receptionist4"):
                opp_val = getattr(old_value, "receptionist4", None)
                if opp_val == self:
                    setattr(old_value, "receptionist4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "receptionist4"):
                opp_val = getattr(value, "receptionist4", None)
                setattr(value, "receptionist4", self)



class Room:

    def __init__(self, roomno: int, roomtype: str, patient13: "Patient" = None, nurse19: "nurse" = None):
        self.roomno = roomno
        self.roomtype = roomtype
        self.patient13 = patient13
        self.nurse19 = nurse19
        
        pass
    @property
    def roomno(self):
        return self.__roomno
    @roomno.setter
    def roomno(self, roomno: int):
        self.__roomno = roomno

    @property
    def roomtype(self):
        return self.__roomtype
    @roomtype.setter
    def roomtype(self, roomtype: str):
        self.__roomtype = roomtype

    @property
    def patient13(self):
        return self.__patient13
    @patient13.setter
    def patient13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__patient13", None)
        self.__patient13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room12"):
                opp_val = getattr(old_value, "room12", None)
                if opp_val == self:
                    setattr(old_value, "room12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room12"):
                opp_val = getattr(value, "room12", None)
                setattr(value, "room12", self)

    @property
    def nurse19(self):
        return self.__nurse19
    @nurse19.setter
    def nurse19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Room__nurse19", None)
        self.__nurse19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "room18"):
                opp_val = getattr(old_value, "room18", None)
                if opp_val == self:
                    setattr(old_value, "room18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "room18"):
                opp_val = getattr(value, "room18", None)
                setattr(value, "room18", self)



class Patient:

    def __init__(self, id: int, name: str, telno: int, address: str, age: int, sex: str, roomno: int, doctors1: set["Doctor"] = None, bill2: "Bill" = None, receptionist4: "Receptionist" = None, appointment10: "appointment" = None, room12: "Room" = None):
        self.id = id
        self.name = name
        self.telno = telno
        self.address = address
        self.age = age
        self.sex = sex
        self.roomno = roomno
        self.doctors1 = doctors1 if doctors1 is not None else set()
        self.bill2 = bill2
        self.receptionist4 = receptionist4
        self.appointment10 = appointment10
        self.room12 = room12
        
        pass
    @property
    def roomno(self):
        return self.__roomno
    @roomno.setter
    def roomno(self, roomno: int):
        self.__roomno = roomno

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def age(self):
        return self.__age
    @age.setter
    def age(self, age: int):
        self.__age = age

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
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def sex(self):
        return self.__sex
    @sex.setter
    def sex(self, sex: str):
        self.__sex = sex

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
    def appointment10(self):
        return self.__appointment10
    @appointment10.setter
    def appointment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__appointment10", None)
        self.__appointment10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient11"):
                opp_val = getattr(old_value, "patient11", None)
                if opp_val == self:
                    setattr(old_value, "patient11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient11"):
                opp_val = getattr(value, "patient11", None)
                setattr(value, "patient11", self)

    @property
    def receptionist4(self):
        return self.__receptionist4
    @receptionist4.setter
    def receptionist4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__receptionist4", None)
        self.__receptionist4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "p5"):
                opp_val = getattr(old_value, "p5", None)
                if opp_val == self:
                    setattr(old_value, "p5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "p5"):
                opp_val = getattr(value, "p5", None)
                setattr(value, "p5", self)

    @property
    def bill2(self):
        return self.__bill2
    @bill2.setter
    def bill2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill2", None)
        self.__bill2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pat3"):
                opp_val = getattr(old_value, "pat3", None)
                if opp_val == self:
                    setattr(old_value, "pat3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pat3"):
                opp_val = getattr(value, "pat3", None)
                setattr(value, "pat3", self)

    @property
    def room12(self):
        return self.__room12
    @room12.setter
    def room12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__room12", None)
        self.__room12 = value
        
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



class Doctor:

    def __init__(self, docid: int, name: str, department: str, specialization: str, phno: int, address: str, patients0: set["Patient"] = None, appointment8: "appointment" = None, medicine16: "medicine" = None):
        self.docid = docid
        self.name = name
        self.department = department
        self.specialization = specialization
        self.phno = phno
        self.address = address
        self.patients0 = patients0 if patients0 is not None else set()
        self.appointment8 = appointment8
        self.medicine16 = medicine16
        
        pass
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
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: str):
        self.__department = department

    @property
    def phno(self):
        return self.__phno
    @phno.setter
    def phno(self, phno: int):
        self.__phno = phno

    @property
    def docid(self):
        return self.__docid
    @docid.setter
    def docid(self, docid: int):
        self.__docid = docid

    @property
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, specialization: str):
        self.__specialization = specialization

    @property
    def appointment8(self):
        return self.__appointment8
    @appointment8.setter
    def appointment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__appointment8", None)
        self.__appointment8 = value
        
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
                    

    @property
    def medicine16(self):
        return self.__medicine16
    @medicine16.setter
    def medicine16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__medicine16", None)
        self.__medicine16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor17"):
                opp_val = getattr(old_value, "doctor17", None)
                if opp_val == self:
                    setattr(old_value, "doctor17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor17"):
                opp_val = getattr(value, "doctor17", None)
                setattr(value, "doctor17", self)

