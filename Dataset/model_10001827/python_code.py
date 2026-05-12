from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Artist:

    pass


class Song:

    def __init__(self, title: str, artist: Artist):
        self.title = title
        self.artist = artist
        
        pass
    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def artist(self):
        return self.__artist
    @artist.setter
    def artist(self, artist: Artist):
        self.__artist = artist



class Nurse:

    def __init__(self, department: Department, department_211: "Department" = None, manager7: "Manager" = None):
        self.department = department
        self.department_211 = department_211
        self.manager7 = manager7
        
        pass
    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: Department):
        self.__department = department

    @property
    def manager7(self):
        return self.__manager7
    @manager7.setter
    def manager7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nurse__manager7", None)
        self.__manager7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nurse6"):
                opp_val = getattr(old_value, "nurse6", None)
                if opp_val == self:
                    setattr(old_value, "nurse6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nurse6"):
                opp_val = getattr(value, "nurse6", None)
                setattr(value, "nurse6", self)

    @property
    def department_211(self):
        return self.__department_211
    @department_211.setter
    def department_211(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Nurse__department_211", None)
        self.__department_211 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "nurse10"):
                opp_val = getattr(old_value, "nurse10", None)
                if opp_val == self:
                    setattr(old_value, "nurse10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "nurse10"):
                opp_val = getattr(value, "nurse10", None)
                setattr(value, "nurse10", self)



class Doctor:

    def __init__(self, department: Department, department_29: "Department" = None, manager5: "Manager" = None):
        self.department = department
        self.department_29 = department_29
        self.manager5 = manager5
        
        pass
    @property
    def department(self):
        return self.__department
    @department.setter
    def department(self, department: Department):
        self.__department = department

    @property
    def manager5(self):
        return self.__manager5
    @manager5.setter
    def manager5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__manager5", None)
        self.__manager5 = value
        
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

    @property
    def department_29(self):
        return self.__department_29
    @department_29.setter
    def department_29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Doctor__department_29", None)
        self.__department_29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor8"):
                opp_val = getattr(old_value, "doctor8", None)
                if opp_val == self:
                    setattr(old_value, "doctor8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor8"):
                opp_val = getattr(value, "doctor8", None)
                setattr(value, "doctor8", self)



class Manager:

    def __init__(self, employeeList: str, allowance: str, doctor4: "Doctor" = None, nurse6: "Nurse" = None):
        self.employeeList = employeeList
        self.allowance = allowance
        self.doctor4 = doctor4
        self.nurse6 = nurse6
        
        pass
    @property
    def allowance(self):
        return self.__allowance
    @allowance.setter
    def allowance(self, allowance: str):
        self.__allowance = allowance

    @property
    def employeeList(self):
        return self.__employeeList
    @employeeList.setter
    def employeeList(self, employeeList: str):
        self.__employeeList = employeeList

    @property
    def doctor4(self):
        return self.__doctor4
    @doctor4.setter
    def doctor4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__doctor4", None)
        self.__doctor4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager5"):
                opp_val = getattr(old_value, "manager5", None)
                if opp_val == self:
                    setattr(old_value, "manager5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager5"):
                opp_val = getattr(value, "manager5", None)
                setattr(value, "manager5", self)

    @property
    def nurse6(self):
        return self.__nurse6
    @nurse6.setter
    def nurse6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Manager__nurse6", None)
        self.__nurse6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager7"):
                opp_val = getattr(old_value, "manager7", None)
                if opp_val == self:
                    setattr(old_value, "manager7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager7"):
                opp_val = getattr(value, "manager7", None)
                setattr(value, "manager7", self)



class Employee:

    def __init__(self, employeeID: str, salary: str):
        self.employeeID = employeeID
        self.salary = salary
        
        pass
    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: str):
        self.__salary = salary

    @property
    def employeeID(self):
        return self.__employeeID
    @employeeID.setter
    def employeeID(self, employeeID: str):
        self.__employeeID = employeeID



class outPatient:

    def __init__(self, inDate: str, outDate: str, roomNumber: str):
        self.inDate = inDate
        self.outDate = outDate
        self.roomNumber = roomNumber
        
        pass
    @property
    def outDate(self):
        return self.__outDate
    @outDate.setter
    def outDate(self, outDate: str):
        self.__outDate = outDate

    @property
    def inDate(self):
        return self.__inDate
    @inDate.setter
    def inDate(self, inDate: str):
        self.__inDate = inDate

    @property
    def roomNumber(self):
        return self.__roomNumber
    @roomNumber.setter
    def roomNumber(self, roomNumber: str):
        self.__roomNumber = roomNumber



class inPatient:

    def __init__(self, inDate: str, outDate: str, rooomNumber: str):
        self.inDate = inDate
        self.outDate = outDate
        self.rooomNumber = rooomNumber
        
        pass
    @property
    def rooomNumber(self):
        return self.__rooomNumber
    @rooomNumber.setter
    def rooomNumber(self, rooomNumber: str):
        self.__rooomNumber = rooomNumber

    @property
    def outDate(self):
        return self.__outDate
    @outDate.setter
    def outDate(self, outDate: str):
        self.__outDate = outDate

    @property
    def inDate(self):
        return self.__inDate
    @inDate.setter
    def inDate(self, inDate: str):
        self.__inDate = inDate



class Patient:

    def __init__(self, patientID: str, treatment: str):
        self.patientID = patientID
        self.treatment = treatment
        
        pass
    @property
    def patientID(self):
        return self.__patientID
    @patientID.setter
    def patientID(self, patientID: str):
        self.__patientID = patientID

    @property
    def treatment(self):
        return self.__treatment
    @treatment.setter
    def treatment(self, treatment: str):
        self.__treatment = treatment



class Person:

    def __init__(self, title: str, name: str, address: str, phoneNumber: str, gender: str, hospital3: "Hospital" = None):
        self.title = title
        self.name = name
        self.address = address
        self.phoneNumber = phoneNumber
        self.gender = gender
        self.hospital3 = hospital3
        
        pass
    @property
    def phoneNumber(self):
        return self.__phoneNumber
    @phoneNumber.setter
    def phoneNumber(self, phoneNumber: str):
        self.__phoneNumber = phoneNumber

    @property
    def title(self):
        return self.__title
    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def gender(self):
        return self.__gender
    @gender.setter
    def gender(self, gender: str):
        self.__gender = gender

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
    def hospital3(self):
        return self.__hospital3
    @hospital3.setter
    def hospital3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Person__hospital3", None)
        self.__hospital3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "person2"):
                opp_val = getattr(old_value, "person2", None)
                if opp_val == self:
                    setattr(old_value, "person2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "person2"):
                opp_val = getattr(value, "person2", None)
                setattr(value, "person2", self)



class Department:

    def __init__(self, departmentID: str, departmentName: str, doctorList: str, nurseList: str, nurse10: "Nurse" = None, hospital1: "Hospital" = None, doctor8: "Doctor" = None):
        self.departmentID = departmentID
        self.departmentName = departmentName
        self.doctorList = doctorList
        self.nurseList = nurseList
        self.nurse10 = nurse10
        self.hospital1 = hospital1
        self.doctor8 = doctor8
        
        pass
    @property
    def nurseList(self):
        return self.__nurseList
    @nurseList.setter
    def nurseList(self, nurseList: str):
        self.__nurseList = nurseList

    @property
    def departmentName(self):
        return self.__departmentName
    @departmentName.setter
    def departmentName(self, departmentName: str):
        self.__departmentName = departmentName

    @property
    def departmentID(self):
        return self.__departmentID
    @departmentID.setter
    def departmentID(self, departmentID: str):
        self.__departmentID = departmentID

    @property
    def doctorList(self):
        return self.__doctorList
    @doctorList.setter
    def doctorList(self, doctorList: str):
        self.__doctorList = doctorList

    @property
    def nurse10(self):
        return self.__nurse10
    @nurse10.setter
    def nurse10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__nurse10", None)
        self.__nurse10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department_211"):
                opp_val = getattr(old_value, "department_211", None)
                if opp_val == self:
                    setattr(old_value, "department_211", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department_211"):
                opp_val = getattr(value, "department_211", None)
                setattr(value, "department_211", self)

    @property
    def hospital1(self):
        return self.__hospital1
    @hospital1.setter
    def hospital1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__hospital1", None)
        self.__hospital1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department0"):
                opp_val = getattr(old_value, "department0", None)
                if opp_val == self:
                    setattr(old_value, "department0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department0"):
                opp_val = getattr(value, "department0", None)
                setattr(value, "department0", self)

    @property
    def doctor8(self):
        return self.__doctor8
    @doctor8.setter
    def doctor8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Department__doctor8", None)
        self.__doctor8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department_29"):
                opp_val = getattr(old_value, "department_29", None)
                if opp_val == self:
                    setattr(old_value, "department_29", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department_29"):
                opp_val = getattr(value, "department_29", None)
                setattr(value, "department_29", self)



class Hospital:

    def __init__(self, name: str, address: str, department0: "Department" = None, person2: "Person" = None):
        self.name = name
        self.address = address
        self.department0 = department0
        self.person2 = person2
        
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
    def person2(self):
        return self.__person2
    @person2.setter
    def person2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__person2", None)
        self.__person2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hospital3"):
                opp_val = getattr(old_value, "hospital3", None)
                if opp_val == self:
                    setattr(old_value, "hospital3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hospital3"):
                opp_val = getattr(value, "hospital3", None)
                setattr(value, "hospital3", self)

    @property
    def department0(self):
        return self.__department0
    @department0.setter
    def department0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Hospital__department0", None)
        self.__department0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "hospital1"):
                opp_val = getattr(old_value, "hospital1", None)
                if opp_val == self:
                    setattr(old_value, "hospital1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "hospital1"):
                opp_val = getattr(value, "hospital1", None)
                setattr(value, "hospital1", self)

