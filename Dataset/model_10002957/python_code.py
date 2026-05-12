from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class SupplyType(Enum):
    pass
class SalaryPayment(Enum):
    pass
class Administration(Enum):
    pass
class TypeContract(Enum):
    pass
class Position(Enum):
    pass
class Relationship(Enum):
    pass
class Sex(Enum):
    pass
class MaritalStatus(Enum):
    pass

############################################
# Definition of Classes
############################################







class Accountant_Actor:

    pass


class Payee_Actor:

    pass


class Patient_Actor:

    pass


class Medical_Director_Actor:

    pass


class Person_Actor:

    pass


class Charge_Nurse_Actor:

    pass


class Staff_Actor:

    pass


class Personnel_Officer_Actor:

    pass





class Generate_Staff_s_Payroll_external:

    pass


class Authorise_Service_Improvement_Budget_external:

    pass


class Search_Patient_external:

    pass


class Create_Patient_appointment_external:

    pass


class Maintain_next_of_kind_details_external:

    pass


class Set_staff_weekly_Rota_external:

    pass


class Maintain_suppliers_external:

    pass


class of_ward_s_supplies_external:

    pass


class Maintain_ward_s_supplies_external:

    pass


class of_Services_Improvement_external:

    pass


class of_Monthly_profit_external:

    pass


class Register_Patient_payment_external:

    pass


class of_Patients_referred_to_the_out_patient_clinic_external:

    pass


class Maintain_Patients_referred_to_the_out_patients_clinic_external:

    pass


class Maintain_Patients_referred_to_the_hospital_external:

    pass


class of_Ward_s_Staff_external:

    pass


class Search_Staff_external:

    pass


class Maintain_Staff_external:

    pass


class Maintain_resources_external:

    pass


class of_Patients_on_waiting_list_external:

    pass


class of_Patients_in_wards_external:

    pass


class of_Patients__medication_external:

    pass


class Maintian_Patients__medication_external:

    pass


class Maintain_ward_s_Patients_external:

    pass


class _Component1:

    pass


class Medication:

    def __init__(self, patient: Patient_Actor, drug: Pharmaceutical, units_per_day: int, administration: Administration, start_date: date, finish_date: date, patient274: "Patient" = None, pharmaceutical76: set["Pharmaceutical"] = None):
        self.patient = patient
        self.drug = drug
        self.units_per_day = units_per_day
        self.administration = administration
        self.start_date = start_date
        self.finish_date = finish_date
        self.patient274 = patient274
        self.pharmaceutical76 = pharmaceutical76 if pharmaceutical76 is not None else set()
        
        pass
    @property
    def finish_date(self):
        return self.__finish_date
    @finish_date.setter
    def finish_date(self, finish_date: date):
        self.__finish_date = finish_date

    @property
    def administration(self):
        return self.__administration
    @administration.setter
    def administration(self, administration: Administration):
        self.__administration = administration

    @property
    def start_date(self):
        return self.__start_date
    @start_date.setter
    def start_date(self, start_date: date):
        self.__start_date = start_date

    @property
    def units_per_day(self):
        return self.__units_per_day
    @units_per_day.setter
    def units_per_day(self, units_per_day: int):
        self.__units_per_day = units_per_day

    @property
    def patient(self):
        return self.__patient
    @patient.setter
    def patient(self, patient: Patient_Actor):
        self.__patient = patient

    @property
    def drug(self):
        return self.__drug
    @drug.setter
    def drug(self, drug: Pharmaceutical):
        self.__drug = drug

    @property
    def pharmaceutical76(self):
        return self.__pharmaceutical76
    @pharmaceutical76.setter
    def pharmaceutical76(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medication__pharmaceutical76", None)
        self.__pharmaceutical76 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "medication77"):
                    opp_val = getattr(item, "medication77", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "medication77"):
                    opp_val = getattr(item, "medication77", None)
                    
                    if opp_val is None:
                        setattr(item, "medication77", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def patient274(self):
        return self.__patient274
    @patient274.setter
    def patient274(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medication__patient274", None)
        self.__patient274 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medication75"):
                opp_val = getattr(old_value, "medication75", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medication75"):
                opp_val = getattr(value, "medication75", None)
                if opp_val is None:
                    setattr(value, "medication75", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class OutPatient:

    def __init__(self, patient: Patient_Actor, date: date, location: str, patient272: "Patient" = None):
        self.patient = patient
        self.date = date
        self.location = location
        self.patient272 = patient272
        
        pass
    @property
    def patient(self):
        return self.__patient
    @patient.setter
    def patient(self, patient: Patient_Actor):
        self.__patient = patient

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def patient272(self):
        return self.__patient272
    @patient272.setter
    def patient272(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_OutPatient__patient272", None)
        self.__patient272 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "outPatient73"):
                opp_val = getattr(old_value, "outPatient73", None)
                if opp_val == self:
                    setattr(old_value, "outPatient73", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "outPatient73"):
                opp_val = getattr(value, "outPatient73", None)
                setattr(value, "outPatient73", self)



class Appointment:

    def __init__(self, num: int, patient: Patient_Actor, doctor: RegularDoctor, date: date, room: str, patient267: "Patient" = None, regularDoctor69: "RegularDoctor" = None, waitingList71: "WaitingList" = None):
        self.num = num
        self.patient = patient
        self.doctor = doctor
        self.date = date
        self.room = room
        self.patient267 = patient267
        self.regularDoctor69 = regularDoctor69
        self.waitingList71 = waitingList71
        
        pass
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def patient(self):
        return self.__patient
    @patient.setter
    def patient(self, patient: Patient_Actor):
        self.__patient = patient

    @property
    def doctor(self):
        return self.__doctor
    @doctor.setter
    def doctor(self, doctor: RegularDoctor):
        self.__doctor = doctor

    @property
    def room(self):
        return self.__room
    @room.setter
    def room(self, room: str):
        self.__room = room

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def regularDoctor69(self):
        return self.__regularDoctor69
    @regularDoctor69.setter
    def regularDoctor69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__regularDoctor69", None)
        self.__regularDoctor69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment68"):
                opp_val = getattr(old_value, "appointment68", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment68"):
                opp_val = getattr(value, "appointment68", None)
                if opp_val is None:
                    setattr(value, "appointment68", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def waitingList71(self):
        return self.__waitingList71
    @waitingList71.setter
    def waitingList71(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__waitingList71", None)
        self.__waitingList71 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment70"):
                opp_val = getattr(old_value, "appointment70", None)
                if opp_val == self:
                    setattr(old_value, "appointment70", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment70"):
                opp_val = getattr(value, "appointment70", None)
                setattr(value, "appointment70", self)

    @property
    def patient267(self):
        return self.__patient267
    @patient267.setter
    def patient267(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__patient267", None)
        self.__patient267 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "appointment66"):
                opp_val = getattr(old_value, "appointment66", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "appointment66"):
                opp_val = getattr(value, "appointment66", None)
                if opp_val is None:
                    setattr(value, "appointment66", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class InPatient:

    def __init__(self, patient: Patient_Actor, ward_required: Ward, duration: int, date_place: date, date_expected_leave: date, date_actual_leave: date, bed: Bed, waitingList64: "WaitingList" = None):
        self.patient = patient
        self.ward_required = ward_required
        self.duration = duration
        self.date_place = date_place
        self.date_expected_leave = date_expected_leave
        self.date_actual_leave = date_actual_leave
        self.bed = bed
        self.waitingList64 = waitingList64
        
        pass
    @property
    def patient(self):
        return self.__patient
    @patient.setter
    def patient(self, patient: Patient_Actor):
        self.__patient = patient

    @property
    def date_actual_leave(self):
        return self.__date_actual_leave
    @date_actual_leave.setter
    def date_actual_leave(self, date_actual_leave: date):
        self.__date_actual_leave = date_actual_leave

    @property
    def date_place(self):
        return self.__date_place
    @date_place.setter
    def date_place(self, date_place: date):
        self.__date_place = date_place

    @property
    def duration(self):
        return self.__duration
    @duration.setter
    def duration(self, duration: int):
        self.__duration = duration

    @property
    def ward_required(self):
        return self.__ward_required
    @ward_required.setter
    def ward_required(self, ward_required: Ward):
        self.__ward_required = ward_required

    @property
    def bed(self):
        return self.__bed
    @bed.setter
    def bed(self, bed: Bed):
        self.__bed = bed

    @property
    def date_expected_leave(self):
        return self.__date_expected_leave
    @date_expected_leave.setter
    def date_expected_leave(self, date_expected_leave: date):
        self.__date_expected_leave = date_expected_leave

    @property
    def waitingList64(self):
        return self.__waitingList64
    @waitingList64.setter
    def waitingList64(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_InPatient__waitingList64", None)
        self.__waitingList64 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "inPatient65"):
                opp_val = getattr(old_value, "inPatient65", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "inPatient65"):
                opp_val = getattr(value, "inPatient65", None)
                if opp_val is None:
                    setattr(value, "inPatient65", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class WaitingList:

    def __init__(self, patient: Patient_Actor, ward_required: Ward, date: date, inPatient65: set["InPatient"] = None, appointment70: "Appointment" = None, WaitingList_Patient_060: set["Patient"] = None, Ward_WaitingList_163: set["Ward"] = None):
        self.patient = patient
        self.ward_required = ward_required
        self.date = date
        self.inPatient65 = inPatient65 if inPatient65 is not None else set()
        self.appointment70 = appointment70
        self.WaitingList_Patient_060 = WaitingList_Patient_060 if WaitingList_Patient_060 is not None else set()
        self.Ward_WaitingList_163 = Ward_WaitingList_163 if Ward_WaitingList_163 is not None else set()
        
        pass
    @property
    def patient(self):
        return self.__patient
    @patient.setter
    def patient(self, patient: Patient_Actor):
        self.__patient = patient

    @property
    def ward_required(self):
        return self.__ward_required
    @ward_required.setter
    def ward_required(self, ward_required: Ward):
        self.__ward_required = ward_required

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def appointment70(self):
        return self.__appointment70
    @appointment70.setter
    def appointment70(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WaitingList__appointment70", None)
        self.__appointment70 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "waitingList71"):
                opp_val = getattr(old_value, "waitingList71", None)
                if opp_val == self:
                    setattr(old_value, "waitingList71", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "waitingList71"):
                opp_val = getattr(value, "waitingList71", None)
                setattr(value, "waitingList71", self)

    @property
    def WaitingList_Patient_060(self):
        return self.__WaitingList_Patient_060
    @WaitingList_Patient_060.setter
    def WaitingList_Patient_060(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WaitingList__WaitingList_Patient_060", None)
        self.__WaitingList_Patient_060 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "WaitingList_Patient_161"):
                    opp_val = getattr(item, "WaitingList_Patient_161", None)
                    
                    if opp_val == self:
                        setattr(item, "WaitingList_Patient_161", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "WaitingList_Patient_161"):
                    opp_val = getattr(item, "WaitingList_Patient_161", None)
                    
                    setattr(item, "WaitingList_Patient_161", self)
                    

    @property
    def inPatient65(self):
        return self.__inPatient65
    @inPatient65.setter
    def inPatient65(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WaitingList__inPatient65", None)
        self.__inPatient65 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "waitingList64"):
                    opp_val = getattr(item, "waitingList64", None)
                    
                    if opp_val == self:
                        setattr(item, "waitingList64", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "waitingList64"):
                    opp_val = getattr(item, "waitingList64", None)
                    
                    setattr(item, "waitingList64", self)
                    

    @property
    def Ward_WaitingList_163(self):
        return self.__Ward_WaitingList_163
    @Ward_WaitingList_163.setter
    def Ward_WaitingList_163(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_WaitingList__Ward_WaitingList_163", None)
        self.__Ward_WaitingList_163 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ward_WaitingList_062"):
                    opp_val = getattr(item, "Ward_WaitingList_062", None)
                    
                    if opp_val == self:
                        setattr(item, "Ward_WaitingList_062", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ward_WaitingList_062"):
                    opp_val = getattr(item, "Ward_WaitingList_062", None)
                    
                    setattr(item, "Ward_WaitingList_062", self)
                    



class Supplier:

    def __init__(self, num: str, fax: str, Supplier_Supply_052: set["Supply"] = None):
        self.num = num
        self.fax = fax
        self.Supplier_Supply_052 = Supplier_Supply_052 if Supplier_Supply_052 is not None else set()
        
        pass
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: str):
        self.__num = num

    @property
    def fax(self):
        return self.__fax
    @fax.setter
    def fax(self, fax: str):
        self.__fax = fax

    @property
    def Supplier_Supply_052(self):
        return self.__Supplier_Supply_052
    @Supplier_Supply_052.setter
    def Supplier_Supply_052(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supplier__Supplier_Supply_052", None)
        self.__Supplier_Supply_052 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Supplier_Supply_153"):
                    opp_val = getattr(item, "Supplier_Supply_153", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Supplier_Supply_153"):
                    opp_val = getattr(item, "Supplier_Supply_153", None)
                    
                    if opp_val is None:
                        setattr(item, "Supplier_Supply_153", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Pharmaceutical:

    def __init__(self, dosage: str, method_of_administration: str, medication77: set["Medication"] = None):
        self.dosage = dosage
        self.method_of_administration = method_of_administration
        self.medication77 = medication77 if medication77 is not None else set()
        
        pass
    @property
    def dosage(self):
        return self.__dosage
    @dosage.setter
    def dosage(self, dosage: str):
        self.__dosage = dosage

    @property
    def method_of_administration(self):
        return self.__method_of_administration
    @method_of_administration.setter
    def method_of_administration(self, method_of_administration: str):
        self.__method_of_administration = method_of_administration

    @property
    def medication77(self):
        return self.__medication77
    @medication77.setter
    def medication77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pharmaceutical__medication77", None)
        self.__medication77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pharmaceutical76"):
                    opp_val = getattr(item, "pharmaceutical76", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pharmaceutical76"):
                    opp_val = getattr(item, "pharmaceutical76", None)
                    
                    if opp_val is None:
                        setattr(item, "pharmaceutical76", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Surgical_NonSurgical:

    def __init__(self, supply_type: SupplyType):
        self.supply_type = supply_type
        
        pass
    @property
    def supply_type(self):
        return self.__supply_type
    @supply_type.setter
    def supply_type(self, supply_type: SupplyType):
        self.__supply_type = supply_type



class Supply:

    def __init__(self, num: int, name: str, description: str, stock: int, reorder_level: int, cost_per_unit: float, Supplier_Supply_153: set["Supplier"] = None, Supply_Requisition_058: set["Requisition"] = None):
        self.num = num
        self.name = name
        self.description = description
        self.stock = stock
        self.reorder_level = reorder_level
        self.cost_per_unit = cost_per_unit
        self.Supplier_Supply_153 = Supplier_Supply_153 if Supplier_Supply_153 is not None else set()
        self.Supply_Requisition_058 = Supply_Requisition_058 if Supply_Requisition_058 is not None else set()
        
        pass
    @property
    def reorder_level(self):
        return self.__reorder_level
    @reorder_level.setter
    def reorder_level(self, reorder_level: int):
        self.__reorder_level = reorder_level

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def cost_per_unit(self):
        return self.__cost_per_unit
    @cost_per_unit.setter
    def cost_per_unit(self, cost_per_unit: float):
        self.__cost_per_unit = cost_per_unit

    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def stock(self):
        return self.__stock
    @stock.setter
    def stock(self, stock: int):
        self.__stock = stock

    @property
    def Supply_Requisition_058(self):
        return self.__Supply_Requisition_058
    @Supply_Requisition_058.setter
    def Supply_Requisition_058(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supply__Supply_Requisition_058", None)
        self.__Supply_Requisition_058 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Supply_Requisition_159"):
                    opp_val = getattr(item, "Supply_Requisition_159", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Supply_Requisition_159"):
                    opp_val = getattr(item, "Supply_Requisition_159", None)
                    
                    if opp_val is None:
                        setattr(item, "Supply_Requisition_159", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Supplier_Supply_153(self):
        return self.__Supplier_Supply_153
    @Supplier_Supply_153.setter
    def Supplier_Supply_153(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Supply__Supplier_Supply_153", None)
        self.__Supplier_Supply_153 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Supplier_Supply_052"):
                    opp_val = getattr(item, "Supplier_Supply_052", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Supplier_Supply_052"):
                    opp_val = getattr(item, "Supplier_Supply_052", None)
                    
                    if opp_val is None:
                        setattr(item, "Supplier_Supply_052", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Requisition:

    def __init__(self, num: int, responsable: ChargeNurse, ward: Ward, supply: Supply, quantity_required: int, date_ordered: date, date_delivered: date, Requisition_Ward_054: "Ward" = None, Requisition_ChargeNurse_056: "ChargeNurse" = None, Supply_Requisition_159: set["Supply"] = None):
        self.num = num
        self.responsable = responsable
        self.ward = ward
        self.supply = supply
        self.quantity_required = quantity_required
        self.date_ordered = date_ordered
        self.date_delivered = date_delivered
        self.Requisition_Ward_054 = Requisition_Ward_054
        self.Requisition_ChargeNurse_056 = Requisition_ChargeNurse_056
        self.Supply_Requisition_159 = Supply_Requisition_159 if Supply_Requisition_159 is not None else set()
        
        pass
    @property
    def ward(self):
        return self.__ward
    @ward.setter
    def ward(self, ward: Ward):
        self.__ward = ward

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def supply(self):
        return self.__supply
    @supply.setter
    def supply(self, supply: Supply):
        self.__supply = supply

    @property
    def responsable(self):
        return self.__responsable
    @responsable.setter
    def responsable(self, responsable: ChargeNurse):
        self.__responsable = responsable

    @property
    def date_ordered(self):
        return self.__date_ordered
    @date_ordered.setter
    def date_ordered(self, date_ordered: date):
        self.__date_ordered = date_ordered

    @property
    def date_delivered(self):
        return self.__date_delivered
    @date_delivered.setter
    def date_delivered(self, date_delivered: date):
        self.__date_delivered = date_delivered

    @property
    def quantity_required(self):
        return self.__quantity_required
    @quantity_required.setter
    def quantity_required(self, quantity_required: int):
        self.__quantity_required = quantity_required

    @property
    def Requisition_Ward_054(self):
        return self.__Requisition_Ward_054
    @Requisition_Ward_054.setter
    def Requisition_Ward_054(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Requisition__Requisition_Ward_054", None)
        self.__Requisition_Ward_054 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Requisition_Ward_155"):
                opp_val = getattr(old_value, "Requisition_Ward_155", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Requisition_Ward_155"):
                opp_val = getattr(value, "Requisition_Ward_155", None)
                if opp_val is None:
                    setattr(value, "Requisition_Ward_155", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Requisition_ChargeNurse_056(self):
        return self.__Requisition_ChargeNurse_056
    @Requisition_ChargeNurse_056.setter
    def Requisition_ChargeNurse_056(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Requisition__Requisition_ChargeNurse_056", None)
        self.__Requisition_ChargeNurse_056 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Requisition_ChargeNurse_157"):
                opp_val = getattr(old_value, "Requisition_ChargeNurse_157", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Requisition_ChargeNurse_157"):
                opp_val = getattr(value, "Requisition_ChargeNurse_157", None)
                if opp_val is None:
                    setattr(value, "Requisition_ChargeNurse_157", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Supply_Requisition_159(self):
        return self.__Supply_Requisition_159
    @Supply_Requisition_159.setter
    def Supply_Requisition_159(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Requisition__Supply_Requisition_159", None)
        self.__Supply_Requisition_159 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Supply_Requisition_058"):
                    opp_val = getattr(item, "Supply_Requisition_058", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Supply_Requisition_058"):
                    opp_val = getattr(item, "Supply_Requisition_058", None)
                    
                    if opp_val is None:
                        setattr(item, "Supply_Requisition_058", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Bed:

    def __init__(self, num: int, Ward_Bed_147: "Ward" = None):
        self.num = num
        self.Ward_Bed_147 = Ward_Bed_147
        
        pass
    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def Ward_Bed_147(self):
        return self.__Ward_Bed_147
    @Ward_Bed_147.setter
    def Ward_Bed_147(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bed__Ward_Bed_147", None)
        self.__Ward_Bed_147 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ward_Bed_046"):
                opp_val = getattr(old_value, "Ward_Bed_046", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ward_Bed_046"):
                opp_val = getattr(value, "Ward_Bed_046", None)
                if opp_val is None:
                    setattr(value, "Ward_Bed_046", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Ward:

    def __init__(self, num: int, name: str, location: str, telephone_extension: int, responsable: ChargeNurse, staff: RegularDoctor, Ward_Bed_046: set["Bed"] = None, Ward_ChargeNurse_048: "ChargeNurse" = None, Ward_RegularDoctor_050: set["RegularDoctor"] = None, Requisition_Ward_155: set["Requisition"] = None, Ward_WaitingList_062: "WaitingList" = None):
        self.num = num
        self.name = name
        self.location = location
        self.telephone_extension = telephone_extension
        self.responsable = responsable
        self.staff = staff
        self.Ward_Bed_046 = Ward_Bed_046 if Ward_Bed_046 is not None else set()
        self.Ward_ChargeNurse_048 = Ward_ChargeNurse_048
        self.Ward_RegularDoctor_050 = Ward_RegularDoctor_050 if Ward_RegularDoctor_050 is not None else set()
        self.Requisition_Ward_155 = Requisition_Ward_155 if Requisition_Ward_155 is not None else set()
        self.Ward_WaitingList_062 = Ward_WaitingList_062
        
        pass
    @property
    def staff(self):
        return self.__staff
    @staff.setter
    def staff(self, staff: RegularDoctor):
        self.__staff = staff

    @property
    def responsable(self):
        return self.__responsable
    @responsable.setter
    def responsable(self, responsable: ChargeNurse):
        self.__responsable = responsable

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def telephone_extension(self):
        return self.__telephone_extension
    @telephone_extension.setter
    def telephone_extension(self, telephone_extension: int):
        self.__telephone_extension = telephone_extension

    @property
    def location(self):
        return self.__location
    @location.setter
    def location(self, location: str):
        self.__location = location

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Ward_WaitingList_062(self):
        return self.__Ward_WaitingList_062
    @Ward_WaitingList_062.setter
    def Ward_WaitingList_062(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__Ward_WaitingList_062", None)
        self.__Ward_WaitingList_062 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ward_WaitingList_163"):
                opp_val = getattr(old_value, "Ward_WaitingList_163", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ward_WaitingList_163"):
                opp_val = getattr(value, "Ward_WaitingList_163", None)
                if opp_val is None:
                    setattr(value, "Ward_WaitingList_163", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ward_ChargeNurse_048(self):
        return self.__Ward_ChargeNurse_048
    @Ward_ChargeNurse_048.setter
    def Ward_ChargeNurse_048(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__Ward_ChargeNurse_048", None)
        self.__Ward_ChargeNurse_048 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Ward_ChargeNurse_149"):
                opp_val = getattr(old_value, "Ward_ChargeNurse_149", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Ward_ChargeNurse_149"):
                opp_val = getattr(value, "Ward_ChargeNurse_149", None)
                if opp_val is None:
                    setattr(value, "Ward_ChargeNurse_149", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Ward_RegularDoctor_050(self):
        return self.__Ward_RegularDoctor_050
    @Ward_RegularDoctor_050.setter
    def Ward_RegularDoctor_050(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__Ward_RegularDoctor_050", None)
        self.__Ward_RegularDoctor_050 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ward_RegularDoctor_151"):
                    opp_val = getattr(item, "Ward_RegularDoctor_151", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ward_RegularDoctor_151"):
                    opp_val = getattr(item, "Ward_RegularDoctor_151", None)
                    
                    if opp_val is None:
                        setattr(item, "Ward_RegularDoctor_151", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def Requisition_Ward_155(self):
        return self.__Requisition_Ward_155
    @Requisition_Ward_155.setter
    def Requisition_Ward_155(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__Requisition_Ward_155", None)
        self.__Requisition_Ward_155 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Requisition_Ward_054"):
                    opp_val = getattr(item, "Requisition_Ward_054", None)
                    
                    if opp_val == self:
                        setattr(item, "Requisition_Ward_054", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Requisition_Ward_054"):
                    opp_val = getattr(item, "Requisition_Ward_054", None)
                    
                    setattr(item, "Requisition_Ward_054", self)
                    

    @property
    def Ward_Bed_046(self):
        return self.__Ward_Bed_046
    @Ward_Bed_046.setter
    def Ward_Bed_046(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ward__Ward_Bed_046", None)
        self.__Ward_Bed_046 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ward_Bed_147"):
                    opp_val = getattr(item, "Ward_Bed_147", None)
                    
                    if opp_val == self:
                        setattr(item, "Ward_Bed_147", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ward_Bed_147"):
                    opp_val = getattr(item, "Ward_Bed_147", None)
                    
                    setattr(item, "Ward_Bed_147", self)
                    



class RegularDoctor:

    pass


class ChargeNurse:

    pass


class PersonnelOfficer:

    pass


class MedicalDirector:

    pass


class EmploymentContract:

    def __init__(self, number_hours_per_week: int, type_contract: TypeContract, salary_payment: SalaryPayment):
        self.number_hours_per_week = number_hours_per_week
        self.type_contract = type_contract
        self.salary_payment = salary_payment
        
        pass
    @property
    def type_contract(self):
        return self.__type_contract
    @type_contract.setter
    def type_contract(self, type_contract: TypeContract):
        self.__type_contract = type_contract

    @property
    def number_hours_per_week(self):
        return self.__number_hours_per_week
    @number_hours_per_week.setter
    def number_hours_per_week(self, number_hours_per_week: int):
        self.__number_hours_per_week = number_hours_per_week

    @property
    def salary_payment(self):
        return self.__salary_payment
    @salary_payment.setter
    def salary_payment(self, salary_payment: SalaryPayment):
        self.__salary_payment = salary_payment



class WorkExperience:

    def __init__(self, organization_name: str, position: str, start_date: date, finish_date: date):
        self.organization_name = organization_name
        self.position = position
        self.start_date = start_date
        self.finish_date = finish_date
        
        pass
    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: str):
        self.__position = position

    @property
    def start_date(self):
        return self.__start_date
    @start_date.setter
    def start_date(self, start_date: date):
        self.__start_date = start_date

    @property
    def organization_name(self):
        return self.__organization_name
    @organization_name.setter
    def organization_name(self, organization_name: str):
        self.__organization_name = organization_name

    @property
    def finish_date(self):
        return self.__finish_date
    @finish_date.setter
    def finish_date(self, finish_date: date):
        self.__finish_date = finish_date



class Qualification:

    def __init__(self, date: date, type: str, institution_name: str):
        self.date = date
        self.type = type
        self.institution_name = institution_name
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: date):
        self.__date = date

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def institution_name(self):
        return self.__institution_name
    @institution_name.setter
    def institution_name(self, institution_name: str):
        self.__institution_name = institution_name



class LocalDoctor:

    def __init__(self, clinic_number: int):
        self.clinic_number = clinic_number
        
        pass
    @property
    def clinic_number(self):
        return self.__clinic_number
    @clinic_number.setter
    def clinic_number(self, clinic_number: int):
        self.__clinic_number = clinic_number



class NextOfKind:

    def __init__(self, relationship: Relationship):
        self.relationship = relationship
        
        pass
    @property
    def relationship(self):
        return self.__relationship
    @relationship.setter
    def relationship(self, relationship: Relationship):
        self.__relationship = relationship



class Staff:

    def __init__(self, num: int, nin: int, position: Position, current_salary: float, salary_scale: float, qualification: Qualification, work_experience: WorkExperience, employment_contract: EmploymentContract):
        self.num = num
        self.nin = nin
        self.position = position
        self.current_salary = current_salary
        self.salary_scale = salary_scale
        self.qualification = qualification
        self.work_experience = work_experience
        self.employment_contract = employment_contract
        
        pass
    @property
    def nin(self):
        return self.__nin
    @nin.setter
    def nin(self, nin: int):
        self.__nin = nin

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def work_experience(self):
        return self.__work_experience
    @work_experience.setter
    def work_experience(self, work_experience: WorkExperience):
        self.__work_experience = work_experience

    @property
    def position(self):
        return self.__position
    @position.setter
    def position(self, position: Position):
        self.__position = position

    @property
    def employment_contract(self):
        return self.__employment_contract
    @employment_contract.setter
    def employment_contract(self, employment_contract: EmploymentContract):
        self.__employment_contract = employment_contract

    @property
    def current_salary(self):
        return self.__current_salary
    @current_salary.setter
    def current_salary(self, current_salary: float):
        self.__current_salary = current_salary

    @property
    def qualification(self):
        return self.__qualification
    @qualification.setter
    def qualification(self, qualification: Qualification):
        self.__qualification = qualification

    @property
    def salary_scale(self):
        return self.__salary_scale
    @salary_scale.setter
    def salary_scale(self, salary_scale: float):
        self.__salary_scale = salary_scale



class Patient:

    def __init__(self, num: int, marital_status: MaritalStatus, next_of_kind: NextOfKind, local_doctor: LocalDoctor, appointment66: set["Appointment"] = None, outPatient73: "OutPatient" = None, medication75: set["Medication"] = None, WaitingList_Patient_161: "WaitingList" = None):
        self.num = num
        self.marital_status = marital_status
        self.next_of_kind = next_of_kind
        self.local_doctor = local_doctor
        self.appointment66 = appointment66 if appointment66 is not None else set()
        self.outPatient73 = outPatient73
        self.medication75 = medication75 if medication75 is not None else set()
        self.WaitingList_Patient_161 = WaitingList_Patient_161
        
        pass
    @property
    def local_doctor(self):
        return self.__local_doctor
    @local_doctor.setter
    def local_doctor(self, local_doctor: LocalDoctor):
        self.__local_doctor = local_doctor

    @property
    def next_of_kind(self):
        return self.__next_of_kind
    @next_of_kind.setter
    def next_of_kind(self, next_of_kind: NextOfKind):
        self.__next_of_kind = next_of_kind

    @property
    def num(self):
        return self.__num
    @num.setter
    def num(self, num: int):
        self.__num = num

    @property
    def marital_status(self):
        return self.__marital_status
    @marital_status.setter
    def marital_status(self, marital_status: MaritalStatus):
        self.__marital_status = marital_status

    @property
    def appointment66(self):
        return self.__appointment66
    @appointment66.setter
    def appointment66(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__appointment66", None)
        self.__appointment66 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient267"):
                    opp_val = getattr(item, "patient267", None)
                    
                    if opp_val == self:
                        setattr(item, "patient267", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient267"):
                    opp_val = getattr(item, "patient267", None)
                    
                    setattr(item, "patient267", self)
                    

    @property
    def outPatient73(self):
        return self.__outPatient73
    @outPatient73.setter
    def outPatient73(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__outPatient73", None)
        self.__outPatient73 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient272"):
                opp_val = getattr(old_value, "patient272", None)
                if opp_val == self:
                    setattr(old_value, "patient272", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient272"):
                opp_val = getattr(value, "patient272", None)
                setattr(value, "patient272", self)

    @property
    def medication75(self):
        return self.__medication75
    @medication75.setter
    def medication75(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__medication75", None)
        self.__medication75 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient274"):
                    opp_val = getattr(item, "patient274", None)
                    
                    if opp_val == self:
                        setattr(item, "patient274", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient274"):
                    opp_val = getattr(item, "patient274", None)
                    
                    setattr(item, "patient274", self)
                    

    @property
    def WaitingList_Patient_161(self):
        return self.__WaitingList_Patient_161
    @WaitingList_Patient_161.setter
    def WaitingList_Patient_161(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__WaitingList_Patient_161", None)
        self.__WaitingList_Patient_161 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "WaitingList_Patient_060"):
                opp_val = getattr(old_value, "WaitingList_Patient_060", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "WaitingList_Patient_060"):
                opp_val = getattr(value, "WaitingList_Patient_060", None)
                if opp_val is None:
                    setattr(value, "WaitingList_Patient_060", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Person:

    def __init__(self, first_name: str, last_name: str, address: str, telephone: str, date_of_birth: date, sex: Sex):
        self.first_name = first_name
        self.last_name = last_name
        self.address = address
        self.telephone = telephone
        self.date_of_birth = date_of_birth
        self.sex = sex
        
        pass
    @property
    def first_name(self):
        return self.__first_name
    @first_name.setter
    def first_name(self, first_name: str):
        self.__first_name = first_name

    @property
    def date_of_birth(self):
        return self.__date_of_birth
    @date_of_birth.setter
    def date_of_birth(self, date_of_birth: date):
        self.__date_of_birth = date_of_birth

    @property
    def last_name(self):
        return self.__last_name
    @last_name.setter
    def last_name(self, last_name: str):
        self.__last_name = last_name

    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, telephone: str):
        self.__telephone = telephone

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
    def sex(self, sex: Sex):
        self.__sex = sex



class _Component:

    pass
