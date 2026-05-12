from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Logging_as_existing_user_UseCase:

    pass


class Create_new_patient_account_UseCase:

    pass


class Authorization_UseCase:

    pass


class Billing_UseCase:

    pass


class Diagnose_UseCase:

    pass


class Remove_appointment_UseCase:

    pass


class New_appointment_UseCase:

    pass


class Appointment_management_UseCase:

    pass


class Logging_into_system_UseCase:

    pass


class Patient_Actor:

    pass


class Doctor_Actor:

    pass


class Nurse_Actor:

    pass


class Employee_Actor:

    pass





class AppointmentDiagnose_external:

    pass


class Appointment_external:

    pass


class Bill:

    def __init__(self, billID: str, date: str, ammount: float, appointment12: "Appointment_external" = None, nurse14: "Nurse" = None):
        self.billID = billID
        self.date = date
        self.ammount = ammount
        self.appointment12 = appointment12
        self.nurse14 = nurse14
        
        pass
    @property
    def ammount(self):
        return self.__ammount
    @ammount.setter
    def ammount(self, ammount: float):
        self.__ammount = ammount

    @property
    def billID(self):
        return self.__billID
    @billID.setter
    def billID(self, billID: str):
        self.__billID = billID

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def appointment12(self):
        return self.__appointment12
    @appointment12.setter
    def appointment12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__appointment12", None)
        self.__appointment12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill13"):
                opp_val = getattr(old_value, "bill13", None)
                if opp_val == self:
                    setattr(old_value, "bill13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill13"):
                opp_val = getattr(value, "bill13", None)
                setattr(value, "bill13", self)

    @property
    def nurse14(self):
        return self.__nurse14
    @nurse14.setter
    def nurse14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__nurse14", None)
        self.__nurse14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bill15"):
                opp_val = getattr(old_value, "bill15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bill15"):
                opp_val = getattr(value, "bill15", None)
                if opp_val is None:
                    setattr(value, "bill15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class TreatmentList:

    def __init__(self, treatmentID: int, treatmentName: str, treatmentPrice: float, appointmentDiagnose11: set["AppointmentDiagnose_external"] = None):
        self.treatmentID = treatmentID
        self.treatmentName = treatmentName
        self.treatmentPrice = treatmentPrice
        self.appointmentDiagnose11 = appointmentDiagnose11 if appointmentDiagnose11 is not None else set()
        
        pass
    @property
    def treatmentName(self):
        return self.__treatmentName
    @treatmentName.setter
    def treatmentName(self, treatmentName: str):
        self.__treatmentName = treatmentName

    @property
    def treatmentID(self):
        return self.__treatmentID
    @treatmentID.setter
    def treatmentID(self, treatmentID: int):
        self.__treatmentID = treatmentID

    @property
    def treatmentPrice(self):
        return self.__treatmentPrice
    @treatmentPrice.setter
    def treatmentPrice(self, treatmentPrice: float):
        self.__treatmentPrice = treatmentPrice

    @property
    def appointmentDiagnose11(self):
        return self.__appointmentDiagnose11
    @appointmentDiagnose11.setter
    def appointmentDiagnose11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TreatmentList__appointmentDiagnose11", None)
        self.__appointmentDiagnose11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "treatmentList10"):
                    opp_val = getattr(item, "treatmentList10", None)
                    
                    if opp_val == self:
                        setattr(item, "treatmentList10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "treatmentList10"):
                    opp_val = getattr(item, "treatmentList10", None)
                    
                    setattr(item, "treatmentList10", self)
                    



class Diagnose:

    def __init__(self, diagnoseID: int, symptomps: str, medication: str):
        self.diagnoseID = diagnoseID
        self.symptomps = symptomps
        self.medication = medication
        
        pass
    @property
    def diagnoseID(self):
        return self.__diagnoseID
    @diagnoseID.setter
    def diagnoseID(self, diagnoseID: int):
        self.__diagnoseID = diagnoseID

    @property
    def medication(self):
        return self.__medication
    @medication.setter
    def medication(self, medication: str):
        self.__medication = medication

    @property
    def symptomps(self):
        return self.__symptomps
    @symptomps.setter
    def symptomps(self, symptomps: str):
        self.__symptomps = symptomps



class Schedule:

    def __init__(self, scheduleID: int, startTime: str, endTime: str, date: str, available: bool):
        self.scheduleID = scheduleID
        self.startTime = startTime
        self.endTime = endTime
        self.date = date
        self.available = available
        
        pass
    @property
    def scheduleID(self):
        return self.__scheduleID
    @scheduleID.setter
    def scheduleID(self, scheduleID: int):
        self.__scheduleID = scheduleID

    @property
    def startTime(self):
        return self.__startTime
    @startTime.setter
    def startTime(self, startTime: str):
        self.__startTime = startTime

    @property
    def available(self):
        return self.__available
    @available.setter
    def available(self, available: bool):
        self.__available = available

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def endTime(self):
        return self.__endTime
    @endTime.setter
    def endTime(self, endTime: str):
        self.__endTime = endTime



class Patient:

    def __init__(self, coupon: float, patientID: int, patientName: str, patientSurname: str, patientMobile: str, patientEmail: str, patientAddress: str, appointment9: set["Appointment_external"] = None):
        self.coupon = coupon
        self.patientID = patientID
        self.patientName = patientName
        self.patientSurname = patientSurname
        self.patientMobile = patientMobile
        self.patientEmail = patientEmail
        self.patientAddress = patientAddress
        self.appointment9 = appointment9 if appointment9 is not None else set()
        
        pass
    @property
    def patientID(self):
        return self.__patientID
    @patientID.setter
    def patientID(self, patientID: int):
        self.__patientID = patientID

    @property
    def patientSurname(self):
        return self.__patientSurname
    @patientSurname.setter
    def patientSurname(self, patientSurname: str):
        self.__patientSurname = patientSurname

    @property
    def coupon(self):
        return self.__coupon
    @coupon.setter
    def coupon(self, coupon: float):
        self.__coupon = coupon

    @property
    def patientAddress(self):
        return self.__patientAddress
    @patientAddress.setter
    def patientAddress(self, patientAddress: str):
        self.__patientAddress = patientAddress

    @property
    def patientMobile(self):
        return self.__patientMobile
    @patientMobile.setter
    def patientMobile(self, patientMobile: str):
        self.__patientMobile = patientMobile

    @property
    def patientEmail(self):
        return self.__patientEmail
    @patientEmail.setter
    def patientEmail(self, patientEmail: str):
        self.__patientEmail = patientEmail

    @property
    def patientName(self):
        return self.__patientName
    @patientName.setter
    def patientName(self, patientName: str):
        self.__patientName = patientName

    @property
    def appointment9(self):
        return self.__appointment9
    @appointment9.setter
    def appointment9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__appointment9", None)
        self.__appointment9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient8"):
                    opp_val = getattr(item, "patient8", None)
                    
                    if opp_val == self:
                        setattr(item, "patient8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient8"):
                    opp_val = getattr(item, "patient8", None)
                    
                    setattr(item, "patient8", self)
                    



class Nurse:

    def __init__(self, experience: str, bill15: set["Bill"] = None):
        self.experience = experience
        self.bill15 = bill15 if bill15 is not None else set()
        
        pass
    @property
    def experience(self):
        return self.__experience
    @experience.setter
    def experience(self, experience: str):
        self.__experience = experience

    @property
    def bill15(self):
        return self.__bill15
    @bill15.setter
    def bill15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nurse__bill15", None)
        self.__bill15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "nurse14"):
                    opp_val = getattr(item, "nurse14", None)
                    
                    if opp_val == self:
                        setattr(item, "nurse14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "nurse14"):
                    opp_val = getattr(item, "nurse14", None)
                    
                    setattr(item, "nurse14", self)
                    



class Doctor:

    def __init__(self, specialization: str):
        self.specialization = specialization
        
        pass
    @property
    def specialization(self):
        return self.__specialization
    @specialization.setter
    def specialization(self, specialization: str):
        self.__specialization = specialization



class Employee:

    def __init__(self, employeeID: int, employeeName: str, employeeSurname: str, employeeAddress: str, employeeMobile: str, employeeEmail: str, employeeUsername: str, employeePassword: str):
        self.employeeID = employeeID
        self.employeeName = employeeName
        self.employeeSurname = employeeSurname
        self.employeeAddress = employeeAddress
        self.employeeMobile = employeeMobile
        self.employeeEmail = employeeEmail
        self.employeeUsername = employeeUsername
        self.employeePassword = employeePassword
        
        pass
    @property
    def employeePassword(self):
        return self.__employeePassword
    @employeePassword.setter
    def employeePassword(self, employeePassword: str):
        self.__employeePassword = employeePassword

    @property
    def employeeEmail(self):
        return self.__employeeEmail
    @employeeEmail.setter
    def employeeEmail(self, employeeEmail: str):
        self.__employeeEmail = employeeEmail

    @property
    def employeeMobile(self):
        return self.__employeeMobile
    @employeeMobile.setter
    def employeeMobile(self, employeeMobile: str):
        self.__employeeMobile = employeeMobile

    @property
    def employeeUsername(self):
        return self.__employeeUsername
    @employeeUsername.setter
    def employeeUsername(self, employeeUsername: str):
        self.__employeeUsername = employeeUsername

    @property
    def employeeID(self):
        return self.__employeeID
    @employeeID.setter
    def employeeID(self, employeeID: int):
        self.__employeeID = employeeID

    @property
    def employeeAddress(self):
        return self.__employeeAddress
    @employeeAddress.setter
    def employeeAddress(self, employeeAddress: str):
        self.__employeeAddress = employeeAddress

    @property
    def employeeSurname(self):
        return self.__employeeSurname
    @employeeSurname.setter
    def employeeSurname(self, employeeSurname: str):
        self.__employeeSurname = employeeSurname

    @property
    def employeeName(self):
        return self.__employeeName
    @employeeName.setter
    def employeeName(self, employeeName: str):
        self.__employeeName = employeeName

