from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class SubjectSheduleController:

    def __init__(self, subjectCodeService: str, groupNumberService: int, activityTypeCodeService: int, dateService: str, individualIdentificationCodeService: int, auditoriumNumberService: int):
        self.subjectCodeService = subjectCodeService
        self.groupNumberService = groupNumberService
        self.activityTypeCodeService = activityTypeCodeService
        self.dateService = dateService
        self.individualIdentificationCodeService = individualIdentificationCodeService
        self.auditoriumNumberService = auditoriumNumberService
        
        pass
    @property
    def dateService(self):
        return self.__dateService
    @dateService.setter
    def dateService(self, dateService: str):
        self.__dateService = dateService

    @property
    def individualIdentificationCodeService(self):
        return self.__individualIdentificationCodeService
    @individualIdentificationCodeService.setter
    def individualIdentificationCodeService(self, individualIdentificationCodeService: int):
        self.__individualIdentificationCodeService = individualIdentificationCodeService

    @property
    def groupNumberService(self):
        return self.__groupNumberService
    @groupNumberService.setter
    def groupNumberService(self, groupNumberService: int):
        self.__groupNumberService = groupNumberService

    @property
    def subjectCodeService(self):
        return self.__subjectCodeService
    @subjectCodeService.setter
    def subjectCodeService(self, subjectCodeService: str):
        self.__subjectCodeService = subjectCodeService

    @property
    def activityTypeCodeService(self):
        return self.__activityTypeCodeService
    @activityTypeCodeService.setter
    def activityTypeCodeService(self, activityTypeCodeService: int):
        self.__activityTypeCodeService = activityTypeCodeService

    @property
    def auditoriumNumberService(self):
        return self.__auditoriumNumberService
    @auditoriumNumberService.setter
    def auditoriumNumberService(self, auditoriumNumberService: int):
        self.__auditoriumNumberService = auditoriumNumberService



class ActivityType:

    def __init__(self, id: int, activityTypeCode: int, activityTypeName: str, subjectCode: int, assoc_11: "Subject" = None):
        self.id = id
        self.activityTypeCode = activityTypeCode
        self.activityTypeName = activityTypeName
        self.subjectCode = subjectCode
        self.assoc_11 = assoc_11
        
        pass
    @property
    def activityTypeCode(self):
        return self.__activityTypeCode
    @activityTypeCode.setter
    def activityTypeCode(self, activityTypeCode: int):
        self.__activityTypeCode = activityTypeCode

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def subjectCode(self):
        return self.__subjectCode
    @subjectCode.setter
    def subjectCode(self, subjectCode: int):
        self.__subjectCode = subjectCode

    @property
    def activityTypeName(self):
        return self.__activityTypeName
    @activityTypeName.setter
    def activityTypeName(self, activityTypeName: str):
        self.__activityTypeName = activityTypeName

    @property
    def assoc_11(self):
        return self.__assoc_11
    @assoc_11.setter
    def assoc_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ActivityType__assoc_11", None)
        self.__assoc_11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "assoc_00"):
                opp_val = getattr(old_value, "assoc_00", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "assoc_00"):
                opp_val = getattr(value, "assoc_00", None)
                if opp_val is None:
                    setattr(value, "assoc_00", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Subject:

    def __init__(self, id: int, subjectCode: int, subjectName: str, assoc_00: set["ActivityType"] = None):
        self.id = id
        self.subjectCode = subjectCode
        self.subjectName = subjectName
        self.assoc_00 = assoc_00 if assoc_00 is not None else set()
        
        pass
    @property
    def subjectName(self):
        return self.__subjectName
    @subjectName.setter
    def subjectName(self, subjectName: str):
        self.__subjectName = subjectName

    @property
    def subjectCode(self):
        return self.__subjectCode
    @subjectCode.setter
    def subjectCode(self, subjectCode: int):
        self.__subjectCode = subjectCode

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def assoc_00(self):
        return self.__assoc_00
    @assoc_00.setter
    def assoc_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Subject__assoc_00", None)
        self.__assoc_00 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "assoc_11"):
                    opp_val = getattr(item, "assoc_11", None)
                    
                    if opp_val == self:
                        setattr(item, "assoc_11", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "assoc_11"):
                    opp_val = getattr(item, "assoc_11", None)
                    
                    setattr(item, "assoc_11", self)
                    



class SubjectShedule:

    def __init__(self, id: int, subjectCode: int, groupNumber: int, activityTypeCode: int, date: str, individualIdentificationCode: int, auditoriumNumber: int):
        self.id = id
        self.subjectCode = subjectCode
        self.groupNumber = groupNumber
        self.activityTypeCode = activityTypeCode
        self.date = date
        self.individualIdentificationCode = individualIdentificationCode
        self.auditoriumNumber = auditoriumNumber
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def individualIdentificationCode(self):
        return self.__individualIdentificationCode
    @individualIdentificationCode.setter
    def individualIdentificationCode(self, individualIdentificationCode: int):
        self.__individualIdentificationCode = individualIdentificationCode

    @property
    def activityTypeCode(self):
        return self.__activityTypeCode
    @activityTypeCode.setter
    def activityTypeCode(self, activityTypeCode: int):
        self.__activityTypeCode = activityTypeCode

    @property
    def groupNumber(self):
        return self.__groupNumber
    @groupNumber.setter
    def groupNumber(self, groupNumber: int):
        self.__groupNumber = groupNumber

    @property
    def subjectCode(self):
        return self.__subjectCode
    @subjectCode.setter
    def subjectCode(self, subjectCode: int):
        self.__subjectCode = subjectCode

    @property
    def auditoriumNumber(self):
        return self.__auditoriumNumber
    @auditoriumNumber.setter
    def auditoriumNumber(self, auditoriumNumber: int):
        self.__auditoriumNumber = auditoriumNumber

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id



class DocumentStorage:

    def __init__(self, documentPath: str, documentCode: int, is_exist: bool, id: int):
        self.documentPath = documentPath
        self.documentCode = documentCode
        self.is_exist = is_exist
        self.id = id
        
        pass
    @property
    def is_exist(self):
        return self.__is_exist
    @is_exist.setter
    def is_exist(self, is_exist: bool):
        self.__is_exist = is_exist

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def documentPath(self):
        return self.__documentPath
    @documentPath.setter
    def documentPath(self, documentPath: str):
        self.__documentPath = documentPath

    @property
    def documentCode(self):
        return self.__documentCode
    @documentCode.setter
    def documentCode(self, documentCode: int):
        self.__documentCode = documentCode



class TimeCreditForEducationalSemester:

    def __init__(self, id: int, groupNumber: int, subjectCode: int, activityTypeCode: int, totalHours: int):
        self.id = id
        self.groupNumber = groupNumber
        self.subjectCode = subjectCode
        self.activityTypeCode = activityTypeCode
        self.totalHours = totalHours
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def groupNumber(self):
        return self.__groupNumber
    @groupNumber.setter
    def groupNumber(self, groupNumber: int):
        self.__groupNumber = groupNumber

    @property
    def totalHours(self):
        return self.__totalHours
    @totalHours.setter
    def totalHours(self, totalHours: int):
        self.__totalHours = totalHours

    @property
    def subjectCode(self):
        return self.__subjectCode
    @subjectCode.setter
    def subjectCode(self, subjectCode: int):
        self.__subjectCode = subjectCode

    @property
    def activityTypeCode(self):
        return self.__activityTypeCode
    @activityTypeCode.setter
    def activityTypeCode(self, activityTypeCode: int):
        self.__activityTypeCode = activityTypeCode



class EducationalPlan:

    def __init__(self, id: int, individualIdentificationCode: int, subjectCode: int):
        self.id = id
        self.individualIdentificationCode = individualIdentificationCode
        self.subjectCode = subjectCode
        
        pass
    @property
    def individualIdentificationCode(self):
        return self.__individualIdentificationCode
    @individualIdentificationCode.setter
    def individualIdentificationCode(self, individualIdentificationCode: int):
        self.__individualIdentificationCode = individualIdentificationCode

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def subjectCode(self):
        return self.__subjectCode
    @subjectCode.setter
    def subjectCode(self, subjectCode: int):
        self.__subjectCode = subjectCode



class Specialty:

    def __init__(self, id: int, specialtyCode: int, specialtyName: str, subjectCode: int):
        self.id = id
        self.specialtyCode = specialtyCode
        self.specialtyName = specialtyName
        self.subjectCode = subjectCode
        
        pass
    @property
    def specialtyCode(self):
        return self.__specialtyCode
    @specialtyCode.setter
    def specialtyCode(self, specialtyCode: int):
        self.__specialtyCode = specialtyCode

    @property
    def subjectCode(self):
        return self.__subjectCode
    @subjectCode.setter
    def subjectCode(self, subjectCode: int):
        self.__subjectCode = subjectCode

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def specialtyName(self):
        return self.__specialtyName
    @specialtyName.setter
    def specialtyName(self, specialtyName: str):
        self.__specialtyName = specialtyName



class Group:

    def __init__(self, id: int, groupNumber: int, educationalYear: int, specialtyCode: int):
        self.id = id
        self.groupNumber = groupNumber
        self.educationalYear = educationalYear
        self.specialtyCode = specialtyCode
        
        pass
    @property
    def groupNumber(self):
        return self.__groupNumber
    @groupNumber.setter
    def groupNumber(self, groupNumber: int):
        self.__groupNumber = groupNumber

    @property
    def specialtyCode(self):
        return self.__specialtyCode
    @specialtyCode.setter
    def specialtyCode(self, specialtyCode: int):
        self.__specialtyCode = specialtyCode

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def educationalYear(self):
        return self.__educationalYear
    @educationalYear.setter
    def educationalYear(self, educationalYear: int):
        self.__educationalYear = educationalYear



class TimeInterval:

    def __init__(self, id: int, date: str, weekIdentifier: int, weekday: int, classOrder: int):
        self.id = id
        self.date = date
        self.weekIdentifier = weekIdentifier
        self.weekday = weekday
        self.classOrder = classOrder
        
        pass
    @property
    def weekday(self):
        return self.__weekday
    @weekday.setter
    def weekday(self, weekday: int):
        self.__weekday = weekday

    @property
    def classOrder(self):
        return self.__classOrder
    @classOrder.setter
    def classOrder(self, classOrder: int):
        self.__classOrder = classOrder

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def weekIdentifier(self):
        return self.__weekIdentifier
    @weekIdentifier.setter
    def weekIdentifier(self, weekIdentifier: int):
        self.__weekIdentifier = weekIdentifier

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date



class Auditorium:

    def __init__(self, id: int, educationalBuilding: str, auditoriumNumber: int, is_busy: bool):
        self.id = id
        self.educationalBuilding = educationalBuilding
        self.auditoriumNumber = auditoriumNumber
        self.is_busy = is_busy
        
        pass
    @property
    def educationalBuilding(self):
        return self.__educationalBuilding
    @educationalBuilding.setter
    def educationalBuilding(self, educationalBuilding: str):
        self.__educationalBuilding = educationalBuilding

    @property
    def is_busy(self):
        return self.__is_busy
    @is_busy.setter
    def is_busy(self, is_busy: bool):
        self.__is_busy = is_busy

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def auditoriumNumber(self):
        return self.__auditoriumNumber
    @auditoriumNumber.setter
    def auditoriumNumber(self, auditoriumNumber: int):
        self.__auditoriumNumber = auditoriumNumber



class Users:

    def __init__(self, id: int, residentName: str, residentSurname: str, residentPatronymic: str, residentBirthday: str, residentPassword: str, registrationCertificateCode: int, residentUserType: str, universityStructureUnit: str, residentPosition: str, residentDepartment: str, residentEmail: str, individuadIdentificationCode: int):
        self.id = id
        self.residentName = residentName
        self.residentSurname = residentSurname
        self.residentPatronymic = residentPatronymic
        self.residentBirthday = residentBirthday
        self.residentPassword = residentPassword
        self.registrationCertificateCode = registrationCertificateCode
        self.residentUserType = residentUserType
        self.universityStructureUnit = universityStructureUnit
        self.residentPosition = residentPosition
        self.residentDepartment = residentDepartment
        self.residentEmail = residentEmail
        self.individuadIdentificationCode = individuadIdentificationCode
        
        pass
    @property
    def residentPatronymic(self):
        return self.__residentPatronymic
    @residentPatronymic.setter
    def residentPatronymic(self, residentPatronymic: str):
        self.__residentPatronymic = residentPatronymic

    @property
    def universityStructureUnit(self):
        return self.__universityStructureUnit
    @universityStructureUnit.setter
    def universityStructureUnit(self, universityStructureUnit: str):
        self.__universityStructureUnit = universityStructureUnit

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def residentPosition(self):
        return self.__residentPosition
    @residentPosition.setter
    def residentPosition(self, residentPosition: str):
        self.__residentPosition = residentPosition

    @property
    def residentUserType(self):
        return self.__residentUserType
    @residentUserType.setter
    def residentUserType(self, residentUserType: str):
        self.__residentUserType = residentUserType

    @property
    def residentSurname(self):
        return self.__residentSurname
    @residentSurname.setter
    def residentSurname(self, residentSurname: str):
        self.__residentSurname = residentSurname

    @property
    def residentDepartment(self):
        return self.__residentDepartment
    @residentDepartment.setter
    def residentDepartment(self, residentDepartment: str):
        self.__residentDepartment = residentDepartment

    @property
    def residentEmail(self):
        return self.__residentEmail
    @residentEmail.setter
    def residentEmail(self, residentEmail: str):
        self.__residentEmail = residentEmail

    @property
    def residentBirthday(self):
        return self.__residentBirthday
    @residentBirthday.setter
    def residentBirthday(self, residentBirthday: str):
        self.__residentBirthday = residentBirthday

    @property
    def residentName(self):
        return self.__residentName
    @residentName.setter
    def residentName(self, residentName: str):
        self.__residentName = residentName

    @property
    def individuadIdentificationCode(self):
        return self.__individuadIdentificationCode
    @individuadIdentificationCode.setter
    def individuadIdentificationCode(self, individuadIdentificationCode: int):
        self.__individuadIdentificationCode = individuadIdentificationCode

    @property
    def registrationCertificateCode(self):
        return self.__registrationCertificateCode
    @registrationCertificateCode.setter
    def registrationCertificateCode(self, registrationCertificateCode: int):
        self.__registrationCertificateCode = registrationCertificateCode

    @property
    def residentPassword(self):
        return self.__residentPassword
    @residentPassword.setter
    def residentPassword(self, residentPassword: str):
        self.__residentPassword = residentPassword

