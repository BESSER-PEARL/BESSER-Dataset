from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class UserwithRole:

    def __init__(self, UserId: int, RoleId: int, users13: set["Users"] = None, userRoles15: set["UserRoles"] = None):
        self.UserId = UserId
        self.RoleId = RoleId
        self.users13 = users13 if users13 is not None else set()
        self.userRoles15 = userRoles15 if userRoles15 is not None else set()
        
        pass
    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: int):
        self.__UserId = UserId

    @property
    def RoleId(self):
        return self.__RoleId
    @RoleId.setter
    def RoleId(self, RoleId: int):
        self.__RoleId = RoleId

    @property
    def userRoles15(self):
        return self.__userRoles15
    @userRoles15.setter
    def userRoles15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UserwithRole__userRoles15", None)
        self.__userRoles15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "userwithRole14"):
                    opp_val = getattr(item, "userwithRole14", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "userwithRole14"):
                    opp_val = getattr(item, "userwithRole14", None)
                    
                    if opp_val is None:
                        setattr(item, "userwithRole14", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def users13(self):
        return self.__users13
    @users13.setter
    def users13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UserwithRole__users13", None)
        self.__users13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "userwithRole12"):
                    opp_val = getattr(item, "userwithRole12", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "userwithRole12"):
                    opp_val = getattr(item, "userwithRole12", None)
                    
                    if opp_val is None:
                        setattr(item, "userwithRole12", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class UserRoles:

    def __init__(self, Id: int, Name: str, userwithRole14: set["UserwithRole"] = None):
        self.Id = Id
        self.Name = Name
        self.userwithRole14 = userwithRole14 if userwithRole14 is not None else set()
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def userwithRole14(self):
        return self.__userwithRole14
    @userwithRole14.setter
    def userwithRole14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_UserRoles__userwithRole14", None)
        self.__userwithRole14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "userRoles15"):
                    opp_val = getattr(item, "userRoles15", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "userRoles15"):
                    opp_val = getattr(item, "userRoles15", None)
                    
                    if opp_val is None:
                        setattr(item, "userRoles15", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Users:

    def __init__(self, Id: int, Email: str, EmailConfirmed: str, PasswordHash: str, SecurityStamp: str, PhoneNumber: str, PhoneNumberConfirmed: str, TwoFactorEnabled: str, LockoutEndDateUtc: str, LockoutEnabled: str, AccessFailedCount: int, UserName: str, userwithRole12: set["UserwithRole"] = None):
        self.Id = Id
        self.Email = Email
        self.EmailConfirmed = EmailConfirmed
        self.PasswordHash = PasswordHash
        self.SecurityStamp = SecurityStamp
        self.PhoneNumber = PhoneNumber
        self.PhoneNumberConfirmed = PhoneNumberConfirmed
        self.TwoFactorEnabled = TwoFactorEnabled
        self.LockoutEndDateUtc = LockoutEndDateUtc
        self.LockoutEnabled = LockoutEnabled
        self.AccessFailedCount = AccessFailedCount
        self.UserName = UserName
        self.userwithRole12 = userwithRole12 if userwithRole12 is not None else set()
        
        pass
    @property
    def EmailConfirmed(self):
        return self.__EmailConfirmed
    @EmailConfirmed.setter
    def EmailConfirmed(self, EmailConfirmed: str):
        self.__EmailConfirmed = EmailConfirmed

    @property
    def SecurityStamp(self):
        return self.__SecurityStamp
    @SecurityStamp.setter
    def SecurityStamp(self, SecurityStamp: str):
        self.__SecurityStamp = SecurityStamp

    @property
    def TwoFactorEnabled(self):
        return self.__TwoFactorEnabled
    @TwoFactorEnabled.setter
    def TwoFactorEnabled(self, TwoFactorEnabled: str):
        self.__TwoFactorEnabled = TwoFactorEnabled

    @property
    def PasswordHash(self):
        return self.__PasswordHash
    @PasswordHash.setter
    def PasswordHash(self, PasswordHash: str):
        self.__PasswordHash = PasswordHash

    @property
    def LockoutEndDateUtc(self):
        return self.__LockoutEndDateUtc
    @LockoutEndDateUtc.setter
    def LockoutEndDateUtc(self, LockoutEndDateUtc: str):
        self.__LockoutEndDateUtc = LockoutEndDateUtc

    @property
    def Id(self):
        return self.__Id
    @Id.setter
    def Id(self, Id: int):
        self.__Id = Id

    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: str):
        self.__PhoneNumber = PhoneNumber

    @property
    def AccessFailedCount(self):
        return self.__AccessFailedCount
    @AccessFailedCount.setter
    def AccessFailedCount(self, AccessFailedCount: int):
        self.__AccessFailedCount = AccessFailedCount

    @property
    def LockoutEnabled(self):
        return self.__LockoutEnabled
    @LockoutEnabled.setter
    def LockoutEnabled(self, LockoutEnabled: str):
        self.__LockoutEnabled = LockoutEnabled

    @property
    def UserName(self):
        return self.__UserName
    @UserName.setter
    def UserName(self, UserName: str):
        self.__UserName = UserName

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def PhoneNumberConfirmed(self):
        return self.__PhoneNumberConfirmed
    @PhoneNumberConfirmed.setter
    def PhoneNumberConfirmed(self, PhoneNumberConfirmed: str):
        self.__PhoneNumberConfirmed = PhoneNumberConfirmed

    @property
    def userwithRole12(self):
        return self.__userwithRole12
    @userwithRole12.setter
    def userwithRole12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Users__userwithRole12", None)
        self.__userwithRole12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "users13"):
                    opp_val = getattr(item, "users13", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "users13"):
                    opp_val = getattr(item, "users13", None)
                    
                    if opp_val is None:
                        setattr(item, "users13", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Receptionist:

    def __init__(self, ReceptionistId: int, RId: str, UserId: int, ReceptionistName: str, DateOfBirth: str, Email: str, PhoneNumber: str):
        self.ReceptionistId = ReceptionistId
        self.RId = RId
        self.UserId = UserId
        self.ReceptionistName = ReceptionistName
        self.DateOfBirth = DateOfBirth
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        
        pass
    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: str):
        self.__PhoneNumber = PhoneNumber

    @property
    def RId(self):
        return self.__RId
    @RId.setter
    def RId(self, RId: str):
        self.__RId = RId

    @property
    def DateOfBirth(self):
        return self.__DateOfBirth
    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth: str):
        self.__DateOfBirth = DateOfBirth

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: int):
        self.__UserId = UserId

    @property
    def ReceptionistName(self):
        return self.__ReceptionistName
    @ReceptionistName.setter
    def ReceptionistName(self, ReceptionistName: str):
        self.__ReceptionistName = ReceptionistName

    @property
    def ReceptionistId(self):
        return self.__ReceptionistId
    @ReceptionistId.setter
    def ReceptionistId(self, ReceptionistId: int):
        self.__ReceptionistId = ReceptionistId

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email



class DoctorServices:

    def __init__(self, ServiceId: int, SId: str, ServiceName: str, ServiceDetails: str, ServicePrice: str, appointment10: set["Appointment"] = None):
        self.ServiceId = ServiceId
        self.SId = SId
        self.ServiceName = ServiceName
        self.ServiceDetails = ServiceDetails
        self.ServicePrice = ServicePrice
        self.appointment10 = appointment10 if appointment10 is not None else set()
        
        pass
    @property
    def ServiceId(self):
        return self.__ServiceId
    @ServiceId.setter
    def ServiceId(self, ServiceId: int):
        self.__ServiceId = ServiceId

    @property
    def ServiceDetails(self):
        return self.__ServiceDetails
    @ServiceDetails.setter
    def ServiceDetails(self, ServiceDetails: str):
        self.__ServiceDetails = ServiceDetails

    @property
    def ServicePrice(self):
        return self.__ServicePrice
    @ServicePrice.setter
    def ServicePrice(self, ServicePrice: str):
        self.__ServicePrice = ServicePrice

    @property
    def SId(self):
        return self.__SId
    @SId.setter
    def SId(self, SId: str):
        self.__SId = SId

    @property
    def ServiceName(self):
        return self.__ServiceName
    @ServiceName.setter
    def ServiceName(self, ServiceName: str):
        self.__ServiceName = ServiceName

    @property
    def appointment10(self):
        return self.__appointment10
    @appointment10.setter
    def appointment10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DoctorServices__appointment10", None)
        self.__appointment10 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctorServices11"):
                    opp_val = getattr(item, "doctorServices11", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctorServices11"):
                    opp_val = getattr(item, "doctorServices11", None)
                    
                    if opp_val is None:
                        setattr(item, "doctorServices11", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class DoctorSchedule:

    def __init__(self, DSid: int, DoctorId: str, AvailableDate: str, AvailableTime: str, doctor3: set["Doctor"] = None):
        self.DSid = DSid
        self.DoctorId = DoctorId
        self.AvailableDate = AvailableDate
        self.AvailableTime = AvailableTime
        self.doctor3 = doctor3 if doctor3 is not None else set()
        
        pass
    @property
    def AvailableTime(self):
        return self.__AvailableTime
    @AvailableTime.setter
    def AvailableTime(self, AvailableTime: str):
        self.__AvailableTime = AvailableTime

    @property
    def DSid(self):
        return self.__DSid
    @DSid.setter
    def DSid(self, DSid: int):
        self.__DSid = DSid

    @property
    def AvailableDate(self):
        return self.__AvailableDate
    @AvailableDate.setter
    def AvailableDate(self, AvailableDate: str):
        self.__AvailableDate = AvailableDate

    @property
    def DoctorId(self):
        return self.__DoctorId
    @DoctorId.setter
    def DoctorId(self, DoctorId: str):
        self.__DoctorId = DoctorId

    @property
    def doctor3(self):
        return self.__doctor3
    @doctor3.setter
    def doctor3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DoctorSchedule__doctor3", None)
        self.__doctor3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctorSchedule2"):
                    opp_val = getattr(item, "doctorSchedule2", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctorSchedule2"):
                    opp_val = getattr(item, "doctorSchedule2", None)
                    
                    if opp_val is None:
                        setattr(item, "doctorSchedule2", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Bill:

    def __init__(self, BillId: int, BId: str, Did: int, DoctorName: str, BillDate: str, PId: int, PatientName: str, TotalAmount: int, doctor5: set["Doctor"] = None, patient7: set["Patient"] = None):
        self.BillId = BillId
        self.BId = BId
        self.Did = Did
        self.DoctorName = DoctorName
        self.BillDate = BillDate
        self.PId = PId
        self.PatientName = PatientName
        self.TotalAmount = TotalAmount
        self.doctor5 = doctor5 if doctor5 is not None else set()
        self.patient7 = patient7 if patient7 is not None else set()
        
        pass
    @property
    def PatientName(self):
        return self.__PatientName
    @PatientName.setter
    def PatientName(self, PatientName: str):
        self.__PatientName = PatientName

    @property
    def BillId(self):
        return self.__BillId
    @BillId.setter
    def BillId(self, BillId: int):
        self.__BillId = BillId

    @property
    def BId(self):
        return self.__BId
    @BId.setter
    def BId(self, BId: str):
        self.__BId = BId

    @property
    def PId(self):
        return self.__PId
    @PId.setter
    def PId(self, PId: int):
        self.__PId = PId

    @property
    def Did(self):
        return self.__Did
    @Did.setter
    def Did(self, Did: int):
        self.__Did = Did

    @property
    def DoctorName(self):
        return self.__DoctorName
    @DoctorName.setter
    def DoctorName(self, DoctorName: str):
        self.__DoctorName = DoctorName

    @property
    def TotalAmount(self):
        return self.__TotalAmount
    @TotalAmount.setter
    def TotalAmount(self, TotalAmount: int):
        self.__TotalAmount = TotalAmount

    @property
    def BillDate(self):
        return self.__BillDate
    @BillDate.setter
    def BillDate(self, BillDate: str):
        self.__BillDate = BillDate

    @property
    def patient7(self):
        return self.__patient7
    @patient7.setter
    def patient7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__patient7", None)
        self.__patient7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "bill6"):
                    opp_val = getattr(item, "bill6", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "bill6"):
                    opp_val = getattr(item, "bill6", None)
                    
                    if opp_val is None:
                        setattr(item, "bill6", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def doctor5(self):
        return self.__doctor5
    @doctor5.setter
    def doctor5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Bill__doctor5", None)
        self.__doctor5 = value if value is not None else set()
        
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
                    



class Doctor:

    def __init__(self, DoctorId: int, DId: str, UserId: int, DoctorName: str, DateOfBirth: str, Email: str, PhoneNumber: str, Speciality: str, appointment1: set["Appointment"] = None, doctorSchedule2: set["DoctorSchedule"] = None, bill4: set["Bill"] = None):
        self.DoctorId = DoctorId
        self.DId = DId
        self.UserId = UserId
        self.DoctorName = DoctorName
        self.DateOfBirth = DateOfBirth
        self.Email = Email
        self.PhoneNumber = PhoneNumber
        self.Speciality = Speciality
        self.appointment1 = appointment1 if appointment1 is not None else set()
        self.doctorSchedule2 = doctorSchedule2 if doctorSchedule2 is not None else set()
        self.bill4 = bill4 if bill4 is not None else set()
        
        pass
    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: str):
        self.__PhoneNumber = PhoneNumber

    @property
    def DateOfBirth(self):
        return self.__DateOfBirth
    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth: str):
        self.__DateOfBirth = DateOfBirth

    @property
    def Speciality(self):
        return self.__Speciality
    @Speciality.setter
    def Speciality(self, Speciality: str):
        self.__Speciality = Speciality

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: int):
        self.__UserId = UserId

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def DoctorName(self):
        return self.__DoctorName
    @DoctorName.setter
    def DoctorName(self, DoctorName: str):
        self.__DoctorName = DoctorName

    @property
    def DoctorId(self):
        return self.__DoctorId
    @DoctorId.setter
    def DoctorId(self, DoctorId: int):
        self.__DoctorId = DoctorId

    @property
    def DId(self):
        return self.__DId
    @DId.setter
    def DId(self, DId: str):
        self.__DId = DId

    @property
    def doctorSchedule2(self):
        return self.__doctorSchedule2
    @doctorSchedule2.setter
    def doctorSchedule2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__doctorSchedule2", None)
        self.__doctorSchedule2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor3"):
                    opp_val = getattr(item, "doctor3", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor3"):
                    opp_val = getattr(item, "doctor3", None)
                    
                    if opp_val is None:
                        setattr(item, "doctor3", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def bill4(self):
        return self.__bill4
    @bill4.setter
    def bill4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__bill4", None)
        self.__bill4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor5"):
                    opp_val = getattr(item, "doctor5", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor5"):
                    opp_val = getattr(item, "doctor5", None)
                    
                    if opp_val is None:
                        setattr(item, "doctor5", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def appointment1(self):
        return self.__appointment1
    @appointment1.setter
    def appointment1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__appointment1", None)
        self.__appointment1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "doctor0"):
                    opp_val = getattr(item, "doctor0", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "doctor0"):
                    opp_val = getattr(item, "doctor0", None)
                    
                    if opp_val is None:
                        setattr(item, "doctor0", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Appointment:

    def __init__(self, AppointmentId: int, Aid: str, PatientId: int, PatientName: str, Did: int, DoctorName: str, ServiceId: int, AppointmentDate: str, AppointmentTime: str, Reason: str, AppointmentStatus: str, doctor0: set["Doctor"] = None, patient9: set["Patient"] = None, doctorServices11: set["DoctorServices"] = None):
        self.AppointmentId = AppointmentId
        self.Aid = Aid
        self.PatientId = PatientId
        self.PatientName = PatientName
        self.Did = Did
        self.DoctorName = DoctorName
        self.ServiceId = ServiceId
        self.AppointmentDate = AppointmentDate
        self.AppointmentTime = AppointmentTime
        self.Reason = Reason
        self.AppointmentStatus = AppointmentStatus
        self.doctor0 = doctor0 if doctor0 is not None else set()
        self.patient9 = patient9 if patient9 is not None else set()
        self.doctorServices11 = doctorServices11 if doctorServices11 is not None else set()
        
        pass
    @property
    def ServiceId(self):
        return self.__ServiceId
    @ServiceId.setter
    def ServiceId(self, ServiceId: int):
        self.__ServiceId = ServiceId

    @property
    def Reason(self):
        return self.__Reason
    @Reason.setter
    def Reason(self, Reason: str):
        self.__Reason = Reason

    @property
    def Did(self):
        return self.__Did
    @Did.setter
    def Did(self, Did: int):
        self.__Did = Did

    @property
    def PatientId(self):
        return self.__PatientId
    @PatientId.setter
    def PatientId(self, PatientId: int):
        self.__PatientId = PatientId

    @property
    def AppointmentId(self):
        return self.__AppointmentId
    @AppointmentId.setter
    def AppointmentId(self, AppointmentId: int):
        self.__AppointmentId = AppointmentId

    @property
    def DoctorName(self):
        return self.__DoctorName
    @DoctorName.setter
    def DoctorName(self, DoctorName: str):
        self.__DoctorName = DoctorName

    @property
    def Aid(self):
        return self.__Aid
    @Aid.setter
    def Aid(self, Aid: str):
        self.__Aid = Aid

    @property
    def AppointmentStatus(self):
        return self.__AppointmentStatus
    @AppointmentStatus.setter
    def AppointmentStatus(self, AppointmentStatus: str):
        self.__AppointmentStatus = AppointmentStatus

    @property
    def PatientName(self):
        return self.__PatientName
    @PatientName.setter
    def PatientName(self, PatientName: str):
        self.__PatientName = PatientName

    @property
    def AppointmentDate(self):
        return self.__AppointmentDate
    @AppointmentDate.setter
    def AppointmentDate(self, AppointmentDate: str):
        self.__AppointmentDate = AppointmentDate

    @property
    def AppointmentTime(self):
        return self.__AppointmentTime
    @AppointmentTime.setter
    def AppointmentTime(self, AppointmentTime: str):
        self.__AppointmentTime = AppointmentTime

    @property
    def patient9(self):
        return self.__patient9
    @patient9.setter
    def patient9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__patient9", None)
        self.__patient9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "appointment8"):
                    opp_val = getattr(item, "appointment8", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "appointment8"):
                    opp_val = getattr(item, "appointment8", None)
                    
                    if opp_val is None:
                        setattr(item, "appointment8", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def doctor0(self):
        return self.__doctor0
    @doctor0.setter
    def doctor0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__doctor0", None)
        self.__doctor0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "appointment1"):
                    opp_val = getattr(item, "appointment1", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "appointment1"):
                    opp_val = getattr(item, "appointment1", None)
                    
                    if opp_val is None:
                        setattr(item, "appointment1", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def doctorServices11(self):
        return self.__doctorServices11
    @doctorServices11.setter
    def doctorServices11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Appointment__doctorServices11", None)
        self.__doctorServices11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "appointment10"):
                    opp_val = getattr(item, "appointment10", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "appointment10"):
                    opp_val = getattr(item, "appointment10", None)
                    
                    if opp_val is None:
                        setattr(item, "appointment10", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Patient:

    def __init__(self, PatientId: int, PId: str, UserId: int, FirstName: str, LastName: str, DateOfBirth: str, Email: str, IsEmailConfirmed: str, activationcode: str, PhoneNumber: str, IsPhoneNumberConfirmed: str, StreetAddress: str, City: str, State: str, ZipCode: str, bill6: set["Bill"] = None, appointment8: set["Appointment"] = None):
        self.PatientId = PatientId
        self.PId = PId
        self.UserId = UserId
        self.FirstName = FirstName
        self.LastName = LastName
        self.DateOfBirth = DateOfBirth
        self.Email = Email
        self.IsEmailConfirmed = IsEmailConfirmed
        self.activationcode = activationcode
        self.PhoneNumber = PhoneNumber
        self.IsPhoneNumberConfirmed = IsPhoneNumberConfirmed
        self.StreetAddress = StreetAddress
        self.City = City
        self.State = State
        self.ZipCode = ZipCode
        self.bill6 = bill6 if bill6 is not None else set()
        self.appointment8 = appointment8 if appointment8 is not None else set()
        
        pass
    @property
    def PId(self):
        return self.__PId
    @PId.setter
    def PId(self, PId: str):
        self.__PId = PId

    @property
    def IsEmailConfirmed(self):
        return self.__IsEmailConfirmed
    @IsEmailConfirmed.setter
    def IsEmailConfirmed(self, IsEmailConfirmed: str):
        self.__IsEmailConfirmed = IsEmailConfirmed

    @property
    def StreetAddress(self):
        return self.__StreetAddress
    @StreetAddress.setter
    def StreetAddress(self, StreetAddress: str):
        self.__StreetAddress = StreetAddress

    @property
    def PatientId(self):
        return self.__PatientId
    @PatientId.setter
    def PatientId(self, PatientId: int):
        self.__PatientId = PatientId

    @property
    def State(self):
        return self.__State
    @State.setter
    def State(self, State: str):
        self.__State = State

    @property
    def FirstName(self):
        return self.__FirstName
    @FirstName.setter
    def FirstName(self, FirstName: str):
        self.__FirstName = FirstName

    @property
    def PhoneNumber(self):
        return self.__PhoneNumber
    @PhoneNumber.setter
    def PhoneNumber(self, PhoneNumber: str):
        self.__PhoneNumber = PhoneNumber

    @property
    def City(self):
        return self.__City
    @City.setter
    def City(self, City: str):
        self.__City = City

    @property
    def activationcode(self):
        return self.__activationcode
    @activationcode.setter
    def activationcode(self, activationcode: str):
        self.__activationcode = activationcode

    @property
    def DateOfBirth(self):
        return self.__DateOfBirth
    @DateOfBirth.setter
    def DateOfBirth(self, DateOfBirth: str):
        self.__DateOfBirth = DateOfBirth

    @property
    def ZipCode(self):
        return self.__ZipCode
    @ZipCode.setter
    def ZipCode(self, ZipCode: str):
        self.__ZipCode = ZipCode

    @property
    def UserId(self):
        return self.__UserId
    @UserId.setter
    def UserId(self, UserId: int):
        self.__UserId = UserId

    @property
    def LastName(self):
        return self.__LastName
    @LastName.setter
    def LastName(self, LastName: str):
        self.__LastName = LastName

    @property
    def IsPhoneNumberConfirmed(self):
        return self.__IsPhoneNumberConfirmed
    @IsPhoneNumberConfirmed.setter
    def IsPhoneNumberConfirmed(self, IsPhoneNumberConfirmed: str):
        self.__IsPhoneNumberConfirmed = IsPhoneNumberConfirmed

    @property
    def Email(self):
        return self.__Email
    @Email.setter
    def Email(self, Email: str):
        self.__Email = Email

    @property
    def bill6(self):
        return self.__bill6
    @bill6.setter
    def bill6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__bill6", None)
        self.__bill6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient7"):
                    opp_val = getattr(item, "patient7", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient7"):
                    opp_val = getattr(item, "patient7", None)
                    
                    if opp_val is None:
                        setattr(item, "patient7", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def appointment8(self):
        return self.__appointment8
    @appointment8.setter
    def appointment8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__appointment8", None)
        self.__appointment8 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient9"):
                    opp_val = getattr(item, "patient9", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient9"):
                    opp_val = getattr(item, "patient9", None)
                    
                    if opp_val is None:
                        setattr(item, "patient9", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

