from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Billing_Report:

    def __init__(self, serviceCharges: str, testCharges: str, Receptionist_Billing_Report_127: "Receptionist" = None):
        self.serviceCharges = serviceCharges
        self.testCharges = testCharges
        self.Receptionist_Billing_Report_127 = Receptionist_Billing_Report_127
        
        pass
    @property
    def testCharges(self):
        return self.__testCharges
    @testCharges.setter
    def testCharges(self, testCharges: str):
        self.__testCharges = testCharges

    @property
    def serviceCharges(self):
        return self.__serviceCharges
    @serviceCharges.setter
    def serviceCharges(self, serviceCharges: str):
        self.__serviceCharges = serviceCharges

    @property
    def Receptionist_Billing_Report_127(self):
        return self.__Receptionist_Billing_Report_127
    @Receptionist_Billing_Report_127.setter
    def Receptionist_Billing_Report_127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Billing_Report__Receptionist_Billing_Report_127", None)
        self.__Receptionist_Billing_Report_127 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "generate26"):
                opp_val = getattr(old_value, "generate26", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "generate26"):
                opp_val = getattr(value, "generate26", None)
                if opp_val is None:
                    setattr(value, "generate26", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class BloodBank:

    def __init__(self, bloodGroup: str, phone: str, Hospital_BloodBank_125: "Hospital" = None):
        self.bloodGroup = bloodGroup
        self.phone = phone
        self.Hospital_BloodBank_125 = Hospital_BloodBank_125
        
        pass
    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def bloodGroup(self):
        return self.__bloodGroup
    @bloodGroup.setter
    def bloodGroup(self, bloodGroup: str):
        self.__bloodGroup = bloodGroup

    @property
    def Hospital_BloodBank_125(self):
        return self.__Hospital_BloodBank_125
    @Hospital_BloodBank_125.setter
    def Hospital_BloodBank_125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_BloodBank__Hospital_BloodBank_125", None)
        self.__Hospital_BloodBank_125 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has24"):
                opp_val = getattr(old_value, "has24", None)
                if opp_val == self:
                    setattr(old_value, "has24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has24"):
                opp_val = getattr(value, "has24", None)
                setattr(value, "has24", self)



class Prescription:

    def __init__(self, medicines: str, tests: str, writes19: set["Doctor"] = None):
        self.medicines = medicines
        self.tests = tests
        self.writes19 = writes19 if writes19 is not None else set()
        
        pass
    @property
    def tests(self):
        return self.__tests
    @tests.setter
    def tests(self, tests: str):
        self.__tests = tests

    @property
    def medicines(self):
        return self.__medicines
    @medicines.setter
    def medicines(self, medicines: str):
        self.__medicines = medicines

    @property
    def writes19(self):
        return self.__writes19
    @writes19.setter
    def writes19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Prescription__writes19", None)
        self.__writes19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Doctor_Prescription_018"):
                    opp_val = getattr(item, "Doctor_Prescription_018", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Doctor_Prescription_018"):
                    opp_val = getattr(item, "Doctor_Prescription_018", None)
                    
                    if opp_val is None:
                        setattr(item, "Doctor_Prescription_018", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Assistant:

    def __init__(self, name: str, CNIC: str, Assistant_Appointment_016: set["Appointment"] = None, Patients_Assistant_121: set["Patients"] = None, Doctor_Assistant_123: "Doctor" = None):
        self.name = name
        self.CNIC = CNIC
        self.Assistant_Appointment_016 = Assistant_Appointment_016 if Assistant_Appointment_016 is not None else set()
        self.Patients_Assistant_121 = Patients_Assistant_121 if Patients_Assistant_121 is not None else set()
        self.Doctor_Assistant_123 = Doctor_Assistant_123
        
        pass
    @property
    def CNIC(self):
        return self.__CNIC
    @CNIC.setter
    def CNIC(self, CNIC: str):
        self.__CNIC = CNIC

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Assistant_Appointment_016(self):
        return self.__Assistant_Appointment_016
    @Assistant_Appointment_016.setter
    def Assistant_Appointment_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assistant__Assistant_Appointment_016", None)
        self.__Assistant_Appointment_016 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "check_details17"):
                    opp_val = getattr(item, "check_details17", None)
                    
                    if opp_val == self:
                        setattr(item, "check_details17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "check_details17"):
                    opp_val = getattr(item, "check_details17", None)
                    
                    setattr(item, "check_details17", self)
                    

    @property
    def Doctor_Assistant_123(self):
        return self.__Doctor_Assistant_123
    @Doctor_Assistant_123.setter
    def Doctor_Assistant_123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assistant__Doctor_Assistant_123", None)
        self.__Doctor_Assistant_123 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "forward_patient_history22"):
                opp_val = getattr(old_value, "forward_patient_history22", None)
                if opp_val == self:
                    setattr(old_value, "forward_patient_history22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "forward_patient_history22"):
                opp_val = getattr(value, "forward_patient_history22", None)
                setattr(value, "forward_patient_history22", self)

    @property
    def Patients_Assistant_121(self):
        return self.__Patients_Assistant_121
    @Patients_Assistant_121.setter
    def Patients_Assistant_121(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Assistant__Patients_Assistant_121", None)
        self.__Patients_Assistant_121 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "record_history20"):
                    opp_val = getattr(item, "record_history20", None)
                    
                    if opp_val == self:
                        setattr(item, "record_history20", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "record_history20"):
                    opp_val = getattr(item, "record_history20", None)
                    
                    setattr(item, "record_history20", self)
                    



class PatientProfile:

    def __init__(self, appointment: str, name: str, Receptionist_PatientProfile_115: "Receptionist" = None):
        self.appointment = appointment
        self.name = name
        self.Receptionist_PatientProfile_115 = Receptionist_PatientProfile_115
        
        pass
    @property
    def appointment(self):
        return self.__appointment
    @appointment.setter
    def appointment(self, appointment: str):
        self.__appointment = appointment

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Receptionist_PatientProfile_115(self):
        return self.__Receptionist_PatientProfile_115
    @Receptionist_PatientProfile_115.setter
    def Receptionist_PatientProfile_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PatientProfile__Receptionist_PatientProfile_115", None)
        self.__Receptionist_PatientProfile_115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "create_update14"):
                opp_val = getattr(old_value, "create_update14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "create_update14"):
                opp_val = getattr(value, "create_update14", None)
                if opp_val is None:
                    setattr(value, "create_update14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class DoctorDatabase:

    def __init__(self, doctorName: str, Specialization: str, check13: "Receptionist" = None):
        self.doctorName = doctorName
        self.Specialization = Specialization
        self.check13 = check13
        
        pass
    @property
    def Specialization(self):
        return self.__Specialization
    @Specialization.setter
    def Specialization(self, Specialization: str):
        self.__Specialization = Specialization

    @property
    def doctorName(self):
        return self.__doctorName
    @doctorName.setter
    def doctorName(self, doctorName: str):
        self.__doctorName = doctorName

    @property
    def check13(self):
        return self.__check13
    @check13.setter
    def check13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DoctorDatabase__check13", None)
        self.__check13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Receptionist_DoctorDatabase_012"):
                opp_val = getattr(old_value, "Receptionist_DoctorDatabase_012", None)
                if opp_val == self:
                    setattr(old_value, "Receptionist_DoctorDatabase_012", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Receptionist_DoctorDatabase_012"):
                opp_val = getattr(value, "Receptionist_DoctorDatabase_012", None)
                setattr(value, "Receptionist_DoctorDatabase_012", self)



class Appointment:

    def __init__(self, Time: str, Patient: str, Doctor: str, Receptionist_Appointment_19: "Receptionist" = None, requests11: "Patients" = None, check_details17: "Assistant" = None):
        self.Time = Time
        self.Patient = Patient
        self.Doctor = Doctor
        self.Receptionist_Appointment_19 = Receptionist_Appointment_19
        self.requests11 = requests11
        self.check_details17 = check_details17
        
        pass
    @property
    def Time(self):
        return self.__Time
    @Time.setter
    def Time(self, Time: str):
        self.__Time = Time

    @property
    def Patient(self):
        return self.__Patient
    @Patient.setter
    def Patient(self, Patient: str):
        self.__Patient = Patient

    @property
    def Doctor(self):
        return self.__Doctor
    @Doctor.setter
    def Doctor(self, Doctor: str):
        self.__Doctor = Doctor

    @property
    def requests11(self):
        return self.__requests11
    @requests11.setter
    def requests11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__requests11", None)
        self.__requests11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Patients_Appointment_010"):
                opp_val = getattr(old_value, "Patients_Appointment_010", None)
                if opp_val == self:
                    setattr(old_value, "Patients_Appointment_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Patients_Appointment_010"):
                opp_val = getattr(value, "Patients_Appointment_010", None)
                setattr(value, "Patients_Appointment_010", self)

    @property
    def Receptionist_Appointment_19(self):
        return self.__Receptionist_Appointment_19
    @Receptionist_Appointment_19.setter
    def Receptionist_Appointment_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__Receptionist_Appointment_19", None)
        self.__Receptionist_Appointment_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "give8"):
                opp_val = getattr(old_value, "give8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "give8"):
                opp_val = getattr(value, "give8", None)
                if opp_val is None:
                    setattr(value, "give8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def check_details17(self):
        return self.__check_details17
    @check_details17.setter
    def check_details17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__check_details17", None)
        self.__check_details17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Assistant_Appointment_016"):
                opp_val = getattr(old_value, "Assistant_Appointment_016", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Assistant_Appointment_016"):
                opp_val = getattr(value, "Assistant_Appointment_016", None)
                if opp_val is None:
                    setattr(value, "Assistant_Appointment_016", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Receptionist:

    def __init__(self, name: str, CNIC: str, Patients_Receptionist_15: set["Patients"] = None, give8: set["Appointment"] = None, Receptionist_DoctorDatabase_012: "DoctorDatabase" = None, generate26: set["Billing_Report"] = None, create_update14: set["PatientProfile"] = None):
        self.name = name
        self.CNIC = CNIC
        self.Patients_Receptionist_15 = Patients_Receptionist_15 if Patients_Receptionist_15 is not None else set()
        self.give8 = give8 if give8 is not None else set()
        self.Receptionist_DoctorDatabase_012 = Receptionist_DoctorDatabase_012
        self.generate26 = generate26 if generate26 is not None else set()
        self.create_update14 = create_update14 if create_update14 is not None else set()
        
        pass
    @property
    def CNIC(self):
        return self.__CNIC
    @CNIC.setter
    def CNIC(self, CNIC: str):
        self.__CNIC = CNIC

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Patients_Receptionist_15(self):
        return self.__Patients_Receptionist_15
    @Patients_Receptionist_15.setter
    def Patients_Receptionist_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__Patients_Receptionist_15", None)
        self.__Patients_Receptionist_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "calls_query4"):
                    opp_val = getattr(item, "calls_query4", None)
                    
                    if opp_val == self:
                        setattr(item, "calls_query4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "calls_query4"):
                    opp_val = getattr(item, "calls_query4", None)
                    
                    setattr(item, "calls_query4", self)
                    

    @property
    def create_update14(self):
        return self.__create_update14
    @create_update14.setter
    def create_update14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__create_update14", None)
        self.__create_update14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Receptionist_PatientProfile_115"):
                    opp_val = getattr(item, "Receptionist_PatientProfile_115", None)
                    
                    if opp_val == self:
                        setattr(item, "Receptionist_PatientProfile_115", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Receptionist_PatientProfile_115"):
                    opp_val = getattr(item, "Receptionist_PatientProfile_115", None)
                    
                    setattr(item, "Receptionist_PatientProfile_115", self)
                    

    @property
    def Receptionist_DoctorDatabase_012(self):
        return self.__Receptionist_DoctorDatabase_012
    @Receptionist_DoctorDatabase_012.setter
    def Receptionist_DoctorDatabase_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__Receptionist_DoctorDatabase_012", None)
        self.__Receptionist_DoctorDatabase_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "check13"):
                opp_val = getattr(old_value, "check13", None)
                if opp_val == self:
                    setattr(old_value, "check13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "check13"):
                opp_val = getattr(value, "check13", None)
                setattr(value, "check13", self)

    @property
    def generate26(self):
        return self.__generate26
    @generate26.setter
    def generate26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__generate26", None)
        self.__generate26 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Receptionist_Billing_Report_127"):
                    opp_val = getattr(item, "Receptionist_Billing_Report_127", None)
                    
                    if opp_val == self:
                        setattr(item, "Receptionist_Billing_Report_127", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Receptionist_Billing_Report_127"):
                    opp_val = getattr(item, "Receptionist_Billing_Report_127", None)
                    
                    setattr(item, "Receptionist_Billing_Report_127", self)
                    

    @property
    def give8(self):
        return self.__give8
    @give8.setter
    def give8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Receptionist__give8", None)
        self.__give8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Receptionist_Appointment_19"):
                    opp_val = getattr(item, "Receptionist_Appointment_19", None)
                    
                    if opp_val == self:
                        setattr(item, "Receptionist_Appointment_19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Receptionist_Appointment_19"):
                    opp_val = getattr(item, "Receptionist_Appointment_19", None)
                    
                    setattr(item, "Receptionist_Appointment_19", self)
                    



class Patients:

    def __init__(self, name: str, weight: int, BP: int, History: str, Symptoms: str, Checks_up3: "Doctor" = None, calls_query4: "Receptionist" = None, Visit6: "Hospital" = None, Patients_Appointment_010: "Appointment" = None, record_history20: "Assistant" = None):
        self.name = name
        self.weight = weight
        self.BP = BP
        self.History = History
        self.Symptoms = Symptoms
        self.Checks_up3 = Checks_up3
        self.calls_query4 = calls_query4
        self.Visit6 = Visit6
        self.Patients_Appointment_010 = Patients_Appointment_010
        self.record_history20 = record_history20
        
        pass
    @property
    def Symptoms(self):
        return self.__Symptoms
    @Symptoms.setter
    def Symptoms(self, Symptoms: str):
        self.__Symptoms = Symptoms

    @property
    def weight(self):
        return self.__weight
    @weight.setter
    def weight(self, weight: int):
        self.__weight = weight

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def History(self):
        return self.__History
    @History.setter
    def History(self, History: str):
        self.__History = History

    @property
    def BP(self):
        return self.__BP
    @BP.setter
    def BP(self, BP: int):
        self.__BP = BP

    @property
    def calls_query4(self):
        return self.__calls_query4
    @calls_query4.setter
    def calls_query4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patients__calls_query4", None)
        self.__calls_query4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Patients_Receptionist_15"):
                opp_val = getattr(old_value, "Patients_Receptionist_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Patients_Receptionist_15"):
                opp_val = getattr(value, "Patients_Receptionist_15", None)
                if opp_val is None:
                    setattr(value, "Patients_Receptionist_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Patients_Appointment_010(self):
        return self.__Patients_Appointment_010
    @Patients_Appointment_010.setter
    def Patients_Appointment_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patients__Patients_Appointment_010", None)
        self.__Patients_Appointment_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requests11"):
                opp_val = getattr(old_value, "requests11", None)
                if opp_val == self:
                    setattr(old_value, "requests11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requests11"):
                opp_val = getattr(value, "requests11", None)
                setattr(value, "requests11", self)

    @property
    def Visit6(self):
        return self.__Visit6
    @Visit6.setter
    def Visit6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patients__Visit6", None)
        self.__Visit6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Patients_Hospital_17"):
                opp_val = getattr(old_value, "Patients_Hospital_17", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Patients_Hospital_17"):
                opp_val = getattr(value, "Patients_Hospital_17", None)
                if opp_val is None:
                    setattr(value, "Patients_Hospital_17", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Checks_up3(self):
        return self.__Checks_up3
    @Checks_up3.setter
    def Checks_up3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patients__Checks_up3", None)
        self.__Checks_up3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Doctor_Patients_02"):
                opp_val = getattr(old_value, "Doctor_Patients_02", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Doctor_Patients_02"):
                opp_val = getattr(value, "Doctor_Patients_02", None)
                if opp_val is None:
                    setattr(value, "Doctor_Patients_02", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def record_history20(self):
        return self.__record_history20
    @record_history20.setter
    def record_history20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patients__record_history20", None)
        self.__record_history20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Patients_Assistant_121"):
                opp_val = getattr(old_value, "Patients_Assistant_121", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Patients_Assistant_121"):
                opp_val = getattr(value, "Patients_Assistant_121", None)
                if opp_val is None:
                    setattr(value, "Patients_Assistant_121", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Doctor:

    def __init__(self, name: str, specilization: str, timing: str, privateConsultancy: bool, Hospital_Doctor_11: "Hospital" = None, Doctor_Patients_02: set["Patients"] = None, Doctor_Prescription_018: set["Prescription"] = None, forward_patient_history22: "Assistant" = None):
        self.name = name
        self.specilization = specilization
        self.timing = timing
        self.privateConsultancy = privateConsultancy
        self.Hospital_Doctor_11 = Hospital_Doctor_11
        self.Doctor_Patients_02 = Doctor_Patients_02 if Doctor_Patients_02 is not None else set()
        self.Doctor_Prescription_018 = Doctor_Prescription_018 if Doctor_Prescription_018 is not None else set()
        self.forward_patient_history22 = forward_patient_history22
        
        pass
    @property
    def specilization(self):
        return self.__specilization
    @specilization.setter
    def specilization(self, specilization: str):
        self.__specilization = specilization

    @property
    def timing(self):
        return self.__timing
    @timing.setter
    def timing(self, timing: str):
        self.__timing = timing

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def privateConsultancy(self):
        return self.__privateConsultancy
    @privateConsultancy.setter
    def privateConsultancy(self, privateConsultancy: bool):
        self.__privateConsultancy = privateConsultancy

    @property
    def Doctor_Patients_02(self):
        return self.__Doctor_Patients_02
    @Doctor_Patients_02.setter
    def Doctor_Patients_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__Doctor_Patients_02", None)
        self.__Doctor_Patients_02 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Checks_up3"):
                    opp_val = getattr(item, "Checks_up3", None)
                    
                    if opp_val == self:
                        setattr(item, "Checks_up3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Checks_up3"):
                    opp_val = getattr(item, "Checks_up3", None)
                    
                    setattr(item, "Checks_up3", self)
                    

    @property
    def Hospital_Doctor_11(self):
        return self.__Hospital_Doctor_11
    @Hospital_Doctor_11.setter
    def Hospital_Doctor_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__Hospital_Doctor_11", None)
        self.__Hospital_Doctor_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "has0"):
                opp_val = getattr(old_value, "has0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "has0"):
                opp_val = getattr(value, "has0", None)
                if opp_val is None:
                    setattr(value, "has0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def forward_patient_history22(self):
        return self.__forward_patient_history22
    @forward_patient_history22.setter
    def forward_patient_history22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__forward_patient_history22", None)
        self.__forward_patient_history22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Doctor_Assistant_123"):
                opp_val = getattr(old_value, "Doctor_Assistant_123", None)
                if opp_val == self:
                    setattr(old_value, "Doctor_Assistant_123", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Doctor_Assistant_123"):
                opp_val = getattr(value, "Doctor_Assistant_123", None)
                setattr(value, "Doctor_Assistant_123", self)

    @property
    def Doctor_Prescription_018(self):
        return self.__Doctor_Prescription_018
    @Doctor_Prescription_018.setter
    def Doctor_Prescription_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__Doctor_Prescription_018", None)
        self.__Doctor_Prescription_018 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "writes19"):
                    opp_val = getattr(item, "writes19", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "writes19"):
                    opp_val = getattr(item, "writes19", None)
                    
                    if opp_val is None:
                        setattr(item, "writes19", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Hospital:

    def __init__(self, name: str, address: str, phone: int, has0: set["Doctor"] = None, Patients_Hospital_17: set["Patients"] = None, has24: "BloodBank" = None):
        self.name = name
        self.address = address
        self.phone = phone
        self.has0 = has0 if has0 is not None else set()
        self.Patients_Hospital_17 = Patients_Hospital_17 if Patients_Hospital_17 is not None else set()
        self.has24 = has24
        
        pass
    @property
    def address(self):
        return self.__address
    @address.setter
    def address(self, address: str):
        self.__address = address

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def phone(self):
        return self.__phone
    @phone.setter
    def phone(self, phone: int):
        self.__phone = phone

    @property
    def has24(self):
        return self.__has24
    @has24.setter
    def has24(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__has24", None)
        self.__has24 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Hospital_BloodBank_125"):
                opp_val = getattr(old_value, "Hospital_BloodBank_125", None)
                if opp_val == self:
                    setattr(old_value, "Hospital_BloodBank_125", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Hospital_BloodBank_125"):
                opp_val = getattr(value, "Hospital_BloodBank_125", None)
                setattr(value, "Hospital_BloodBank_125", self)

    @property
    def has0(self):
        return self.__has0
    @has0.setter
    def has0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__has0", None)
        self.__has0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Hospital_Doctor_11"):
                    opp_val = getattr(item, "Hospital_Doctor_11", None)
                    
                    if opp_val == self:
                        setattr(item, "Hospital_Doctor_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Hospital_Doctor_11"):
                    opp_val = getattr(item, "Hospital_Doctor_11", None)
                    
                    setattr(item, "Hospital_Doctor_11", self)
                    

    @property
    def Patients_Hospital_17(self):
        return self.__Patients_Hospital_17
    @Patients_Hospital_17.setter
    def Patients_Hospital_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__Patients_Hospital_17", None)
        self.__Patients_Hospital_17 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Visit6"):
                    opp_val = getattr(item, "Visit6", None)
                    
                    if opp_val == self:
                        setattr(item, "Visit6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Visit6"):
                    opp_val = getattr(item, "Visit6", None)
                    
                    setattr(item, "Visit6", self)
                    

