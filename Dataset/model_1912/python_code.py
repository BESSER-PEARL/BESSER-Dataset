from datetime import datetime, date, time
from abc import ABC, abstractmethod

from enum import Enum

############################################
# Definition of Enumerations
############################################

class AccountType(Enum):
    Manager = "Manager"
    CustomerService = "CustomerService"
    Guest = "Guest"
    Staff = "Staff"
class ConferenceRoomCategory(Enum):
    DiningRoom = "DiningRoom"
    LectureRoom = "LectureRoom"
    MeetingRoom = "MeetingRoom"
    Other = "Other"
class HotelRoomCategory(Enum):
    StandardRoom = "StandardRoom"
    FamilyRoom = "FamilyRoom"
    Suite = "Suite"


############################################
# Definition of Classes
############################################

class Classes_Requests_Request:

    def __init__(self, id: str, description: str, isResolved: str):
        self.id = id
        self.description = description
        self.isResolved = isResolved
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def isResolved(self):
        return self.__isResolved

    @isResolved.setter
    def isResolved(self, isResolved: str):
        self.__isResolved = isResolved


class Request:

    pass
class Classes_Requests_IRequests(ABC):

    def __init__(self):
        
        pass
    def addRequest(self, Classes_specialRequestId, Classes_description):
        # TODO: Implement addRequest method
        pass

    def createRequest(self, Classes_description):
        # TODO: Implement createRequest method
        pass

    def deleteRequest(self, Classes_specialRequestId):
        # TODO: Implement deleteRequest method
        pass

    def setRequestResolved(self, Classes_SpecialRequestId):
        # TODO: Implement setRequestResolved method
        pass

    def changeRequestDesc(self, Classes_description, Classes_specialRequestId):
        # TODO: Implement changeRequestDesc method
        pass

    def getAllRequestIDs(self) :
        # TODO: Implement getAllRequestIDs method
        pass

    def hasRequestBeenResolved(self, Classes_specialRequestId) :
        # TODO: Implement hasRequestBeenResolved method
        pass

    def getRequestDescription(self, Classes_specialRequestId) :
        # TODO: Implement getRequestDescription method
        pass

    def setRequestDescription(self, Classes_specialRequestId, Classes_description):
        # TODO: Implement setRequestDescription method
        pass

    def searchRequests(self, Classes_keyword) :
        # TODO: Implement searchRequests method
        pass

class Classes_Feedback_Feedback:

    def __init__(self, description: str, isNoted: str, isResolved: str, id: str):
        self.description = description
        self.isNoted = isNoted
        self.isResolved = isResolved
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def isResolved(self):
        return self.__isResolved

    @isResolved.setter
    def isResolved(self, isResolved: str):
        self.__isResolved = isResolved


    @property
    def isNoted(self):
        return self.__isNoted

    @isNoted.setter
    def isNoted(self, isNoted: str):
        self.__isNoted = isNoted


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


class Feedback:

    pass
class IFeedback:

    pass
class Classes_Feedback_FeedbackManager(IFeedback):

    pass
class IRequests:

    pass
class Classes_Requests_RequestsManager(IRequests):

    pass
class Classes_Restaurants_RestaurantTable:

    def __init__(self, tableNumber: str, numberOfSeats: str):
        self.tableNumber = tableNumber
        self.numberOfSeats = numberOfSeats
        
        pass
    @property
    def numberOfSeats(self):
        return self.__numberOfSeats

    @numberOfSeats.setter
    def numberOfSeats(self, numberOfSeats: str):
        self.__numberOfSeats = numberOfSeats


    @property
    def tableNumber(self):
        return self.__tableNumber

    @tableNumber.setter
    def tableNumber(self, tableNumber: str):
        self.__tableNumber = tableNumber


class Classes_Restaurants_Reservation:

    def __init__(self, id: str, reservedBy: str, from_: date, to: date, Classes_Restaurants_Reservation: set["RestaurantTable"] = None):
        self.id = id
        self.reservedBy = reservedBy
        self.from_ = from_
        self.to = to
        self.Classes_Restaurants_Reservation = Classes_Restaurants_Reservation if Classes_Restaurants_Reservation is not None else set()
        
        pass
    @property
    def from_(self):
        return self.__from_

    @from_.setter
    def from_(self, from_: date):
        self.__from_ = from_


    @property
    def to(self):
        return self.__to

    @to.setter
    def to(self, to: date):
        self.__to = to


    @property
    def reservedBy(self):
        return self.__reservedBy

    @reservedBy.setter
    def reservedBy(self, reservedBy: str):
        self.__reservedBy = reservedBy


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def Classes_Restaurants_Reservation(self):
        return self.__Classes_Restaurants_Reservation

    @Classes_Restaurants_Reservation.setter
    def Classes_Restaurants_Reservation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Restaurants_Reservation__Classes_Restaurants_Reservation", None)
        self.__Classes_Restaurants_Reservation = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RestaurantTable81"):
                    opp_val = getattr(item, "RestaurantTable81", None)
                    
                    if opp_val == self:
                        setattr(item, "RestaurantTable81", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RestaurantTable81"):
                    opp_val = getattr(item, "RestaurantTable81", None)
                    
                    setattr(item, "RestaurantTable81", self)
                    

class RestaurantMenu:

    pass
class RestaurantTable:

    pass
class Reservation:

    pass
class Classes_Restaurants_Restaurant:

    def __init__(self, name: str, Classes_Restaurants_Restaurant: set["Reservation"] = None, Classes_Restaurants_Restaurant77: set["RestaurantTable"] = None, Classes_Restaurants_Restaurant79: "RestaurantMenu" = None):
        self.name = name
        self.Classes_Restaurants_Restaurant = Classes_Restaurants_Restaurant if Classes_Restaurants_Restaurant is not None else set()
        self.Classes_Restaurants_Restaurant77 = Classes_Restaurants_Restaurant77 if Classes_Restaurants_Restaurant77 is not None else set()
        self.Classes_Restaurants_Restaurant79 = Classes_Restaurants_Restaurant79
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Classes_Restaurants_Restaurant77(self):
        return self.__Classes_Restaurants_Restaurant77

    @Classes_Restaurants_Restaurant77.setter
    def Classes_Restaurants_Restaurant77(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Restaurants_Restaurant__Classes_Restaurants_Restaurant77", None)
        self.__Classes_Restaurants_Restaurant77 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "RestaurantTable"):
                    opp_val = getattr(item, "RestaurantTable", None)
                    
                    if opp_val == self:
                        setattr(item, "RestaurantTable", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "RestaurantTable"):
                    opp_val = getattr(item, "RestaurantTable", None)
                    
                    setattr(item, "RestaurantTable", self)
                    

    @property
    def Classes_Restaurants_Restaurant(self):
        return self.__Classes_Restaurants_Restaurant

    @Classes_Restaurants_Restaurant.setter
    def Classes_Restaurants_Restaurant(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Restaurants_Restaurant__Classes_Restaurants_Restaurant", None)
        self.__Classes_Restaurants_Restaurant = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Reservation"):
                    opp_val = getattr(item, "Reservation", None)
                    
                    if opp_val == self:
                        setattr(item, "Reservation", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Reservation"):
                    opp_val = getattr(item, "Reservation", None)
                    
                    setattr(item, "Reservation", self)
                    

    @property
    def Classes_Restaurants_Restaurant79(self):
        return self.__Classes_Restaurants_Restaurant79

    @Classes_Restaurants_Restaurant79.setter
    def Classes_Restaurants_Restaurant79(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Restaurants_Restaurant__Classes_Restaurants_Restaurant79", None)
        self.__Classes_Restaurants_Restaurant79 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "RestaurantMenu"):
                opp_val = getattr(old_value, "RestaurantMenu", None)
                if opp_val == self:
                    setattr(old_value, "RestaurantMenu", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "RestaurantMenu"):
                opp_val = getattr(value, "RestaurantMenu", None)
                setattr(value, "RestaurantMenu", self)

    def getReservation(self, Classes_reservationID):
        # TODO: Implement getReservation method
        pass

    def addReservation(self):
        # TODO: Implement addReservation method
        pass

class Classes_Feedback_IFeedback(ABC):

    def __init__(self):
        
        pass
    def setFeedbackIsNoted(self, Classes_status, Classes_id):
        # TODO: Implement setFeedbackIsNoted method
        pass

    def setFeedbackIsResolved(self, Classes_status, Classes_id):
        # TODO: Implement setFeedbackIsResolved method
        pass

    def getFeedbackIsNoted(self, Classes_id) :
        # TODO: Implement getFeedbackIsNoted method
        pass

    def setFeedbackDescription(self, Classes_desc, Classes_id):
        # TODO: Implement setFeedbackDescription method
        pass

    def getFeedbackDescription(self, Classes_id) :
        # TODO: Implement getFeedbackDescription method
        pass

    def getFeedbackIsResolved(self, Classes_id) :
        # TODO: Implement getFeedbackIsResolved method
        pass

    def searchFeedback(self, Classes_keyword) :
        # TODO: Implement searchFeedback method
        pass

    def addFeedback(self, Classes_desc):
        # TODO: Implement addFeedback method
        pass

    def getAllFeedbackIDs(self) :
        # TODO: Implement getAllFeedbackIDs method
        pass

class Classes_Restaurants_RestaurantMenu:

    def __init__(self, name: str, items: str):
        self.name = name
        self.items = items
        
        pass
    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    def removeItem(self, Classes_itemID):
        # TODO: Implement removeItem method
        pass

    def addItem(self, Classes_itemID):
        # TODO: Implement addItem method
        pass

class Restaurant:

    pass
class IRestaurantsManage:

    pass
class Classes_Restaurants_RestaurantsManager(IRestaurantsManage):

    pass
class Classes_Restaurants_IRestaurantsAccess(ABC):

    def __init__(self):
        
        pass
    def cancelReservation(self, Classes_restaurantID, Classes_reservationID):
        # TODO: Implement cancelReservation method
        pass

    def makeReservation(self, Classes_to, Classes_from_, Classes_restaurantID, Classes_tables, Classes_guestID):
        # TODO: Implement makeReservation method
        pass

    def getAvailableTablesByNbrGuests(self, Classes_restaurantID, Classes_nbrGuests, Classes_from_, Classes_to) :
        # TODO: Implement getAvailableTablesByNbrGuests method
        pass

    def getRestaurantMenuItems(self, Classes_restaurantID) :
        # TODO: Implement getRestaurantMenuItems method
        pass

    def getRestaurantTables(self, Classes_restaurantID) :
        # TODO: Implement getRestaurantTables method
        pass

    def getReservationToTime(self, Classes_restaurantID, Classes_reservationID) :
        # TODO: Implement getReservationToTime method
        pass

    def getReservationGuest(self, Classes_reservationID, Classes_restaurantID) :
        # TODO: Implement getReservationGuest method
        pass

    def searchRestaurantReservationsWithTime(self, Classes_to, Classes_from_, Classes_keyword, Classes_restaurantID) :
        # TODO: Implement searchRestaurantReservationsWithTime method
        pass

    def searchRestaurantReservations(self, Classes_keyword, Classes_restaurantID) :
        # TODO: Implement searchRestaurantReservations method
        pass

    def getReservationFromTime(self, Classes_restaurantID, Classes_reservationID) :
        # TODO: Implement getReservationFromTime method
        pass

    def getRestaurantMenuName(self, Classes_restaurantID) :
        # TODO: Implement getRestaurantMenuName method
        pass

    def searchRestaurantTables(self, Classes_keyword, Classes_restaurantID) :
        # TODO: Implement searchRestaurantTables method
        pass

    def getRestaurantReservations(self, Classes_restaurantID) :
        # TODO: Implement getRestaurantReservations method
        pass

    def getRestaurantTableNumberOfSeats(self, Classes_restaurantID, Classes_tableNbr) :
        # TODO: Implement getRestaurantTableNumberOfSeats method
        pass

    def getAllRestaurantNames(self) :
        # TODO: Implement getAllRestaurantNames method
        pass

    def changeReservedTables(self, Classes_restaurantID, Classes_tables, Classes_reservationID):
        # TODO: Implement changeReservedTables method
        pass

    def searchRestaurants(self, Classes_keyword) :
        # TODO: Implement searchRestaurants method
        pass

    def getAvailableTables(self, Classes_restaurantID, Classes_from_, Classes_to) :
        # TODO: Implement getAvailableTables method
        pass

class IRestaurantsAccess:

    pass
class Classes_Restaurants_IRestaurantsManage(IRestaurantsAccess):

    def __init__(self):
        
        pass
    def removeMenuItem(self, Classes_itemID, Classes_restaurantID):
        # TODO: Implement removeMenuItem method
        pass

    def addMenuItem(self, Classes_restaurantID, Classes_itemID):
        # TODO: Implement addMenuItem method
        pass

    def removeRestaurant(self, Classes_restaurantID):
        # TODO: Implement removeRestaurant method
        pass

    def changeTableNumber(self, Classes_restaurantID, Classes_newTableNbr, Classes_oldTableNbr):
        # TODO: Implement changeTableNumber method
        pass

    def changeRestaurantName(self, Classes_restaurantID, Classes_name):
        # TODO: Implement changeRestaurantName method
        pass

    def removeRestaurantTable(self, Classes_restaurantID, Classes_tableNbr):
        # TODO: Implement removeRestaurantTable method
        pass

    def addRestaurantTable(self, Classes_tableNbr, Classes_nbrSeats, Classes_restaurantID):
        # TODO: Implement addRestaurantTable method
        pass

    def changeMenuName(self, Classes_name, Classes_restaurantID):
        # TODO: Implement changeMenuName method
        pass

    def addRestaurant(self, Classes_name):
        # TODO: Implement addRestaurant method
        pass

    def changeTableNumberOfSeats(self, Classes_restaurantID, Classes_tableNbr, Classes_nbrSeats):
        # TODO: Implement changeTableNumberOfSeats method
        pass

class Classes_Staff_SalaryContract(ABC):

    def __init__(self):
        
        pass
    def getSalary(self) :
        # TODO: Implement getSalary method
        pass

    def getType(self) :
        # TODO: Implement getType method
        pass

    def setSalary(self, Classes_salary):
        # TODO: Implement setSalary method
        pass

class SalaryContract:

    pass
class Classes_Staff_MonthlySalaryContract(SalaryContract):

    def __init__(self, salary: float, SalaryContract: "Classes_Staff_Staff" = None):
        self.salary = salary
        
        pass
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary


class Classes_Staff_Staff:

    def __init__(self, firstName: str, lastName: str, job: str, phone: str, email: str, ssid: str, Classes_Staff_Staff: "SalaryContract" = None):
        self.firstName = firstName
        self.lastName = lastName
        self.job = job
        self.phone = phone
        self.email = email
        self.ssid = ssid
        self.Classes_Staff_Staff = Classes_Staff_Staff
        
        pass
    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone


    @property
    def ssid(self):
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def job(self):
        return self.__job

    @job.setter
    def job(self, job: str):
        self.__job = job


    @property
    def Classes_Staff_Staff(self):
        return self.__Classes_Staff_Staff

    @Classes_Staff_Staff.setter
    def Classes_Staff_Staff(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Staff_Staff__Classes_Staff_Staff", None)
        self.__Classes_Staff_Staff = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "SalaryContract"):
                opp_val = getattr(old_value, "SalaryContract", None)
                if opp_val == self:
                    setattr(old_value, "SalaryContract", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "SalaryContract"):
                opp_val = getattr(value, "SalaryContract", None)
                setattr(value, "SalaryContract", self)

class Staff:

    pass
class Classes_Staff_IStaff(ABC):

    def __init__(self):
        
        pass
    def getStaffLastName(self, Classes_SSID) :
        # TODO: Implement getStaffLastName method
        pass

    def addEmployee(self, Classes_email, Classes_lastname, Classes_job, Classes_SSID, Classes_salaryContractType, Classes_firstname, Classes_salary, Classes_phone):
        # TODO: Implement addEmployee method
        pass

    def getStaffJob(self, Classes_SSID) :
        # TODO: Implement getStaffJob method
        pass

    def getStaffSalaryContractType(self, Classes_SSID) :
        # TODO: Implement getStaffSalaryContractType method
        pass

    def changeStaffLastName(self, Classes_SSID, Classes_lastName):
        # TODO: Implement changeStaffLastName method
        pass

    def changeStaffPhone(self, Classes_phoneNumber, Classes_SSID):
        # TODO: Implement changeStaffPhone method
        pass

    def getStaffSalary(self, Classes_SSID) :
        # TODO: Implement getStaffSalary method
        pass

    def searchStaff(self, Classes_keyword) :
        # TODO: Implement searchStaff method
        pass

    def changeStaffFirstName(self, Classes_SSID, Classes_firstName):
        # TODO: Implement changeStaffFirstName method
        pass

    def scheduleStaff(self, Classes_to, Classes_from_) :
        # TODO: Implement scheduleStaff method
        pass

    def changeStaffJob(self, Classes_SSID, Classes_job):
        # TODO: Implement changeStaffJob method
        pass

    def getStaffFirstName(self, Classes_SSID) :
        # TODO: Implement getStaffFirstName method
        pass

    def changeStaffSalaryContract(self, Classes_SSID, Classes_salaryContract):
        # TODO: Implement changeStaffSalaryContract method
        pass

    def getStaffPhone(self, Classes_SSID) :
        # TODO: Implement getStaffPhone method
        pass

    def getStaffEmail(self, Classes_SSID) :
        # TODO: Implement getStaffEmail method
        pass

    def getAllStaff(self) :
        # TODO: Implement getAllStaff method
        pass

class Classes_Staff_HourlySalaryContract(SalaryContract):

    def __init__(self, salary: float, SalaryContract: "Classes_Staff_Staff" = None):
        self.salary = salary
        
        pass
    @property
    def salary(self):
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary


class Classes_Statistics_IStatisticsGenerator(ABC):

    def __init__(self):
        
        pass
    def getRevenueStatistics(self, Classes_from_, Classes_to) :
        # TODO: Implement getRevenueStatistics method
        pass

    def getOccupancyStatistics(self, Classes_from_, Classes_to) :
        # TODO: Implement getOccupancyStatistics method
        pass

    def getProfitStatistics(self, Classes_to, Classes_from_) :
        # TODO: Implement getProfitStatistics method
        pass

class Classes_Statistics_Date:

    pass
class Classes_Statistics_StatisticEntry:

    def __init__(self, value: str, Classes_Statistics_StatisticEntry: "Date" = None):
        self.value = value
        self.Classes_Statistics_StatisticEntry = Classes_Statistics_StatisticEntry
        
        pass
    @property
    def value(self):
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value


    @property
    def Classes_Statistics_StatisticEntry(self):
        return self.__Classes_Statistics_StatisticEntry

    @Classes_Statistics_StatisticEntry.setter
    def Classes_Statistics_StatisticEntry(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Statistics_StatisticEntry__Classes_Statistics_StatisticEntry", None)
        self.__Classes_Statistics_StatisticEntry = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Date63"):
                opp_val = getattr(old_value, "Date63", None)
                if opp_val == self:
                    setattr(old_value, "Date63", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Date63"):
                opp_val = getattr(value, "Date63", None)
                setattr(value, "Date63", self)

class Date:

    pass
class StatisticEntry:

    pass
class Classes_Statistics_Statistic:

    def __init__(self, type: str, Classes_Statistics_Statistic: set["StatisticEntry"] = None, Classes_Statistics_Statistic58: "Date" = None, Classes_Statistics_Statistic60: "Date" = None):
        self.type = type
        self.Classes_Statistics_Statistic = Classes_Statistics_Statistic if Classes_Statistics_Statistic is not None else set()
        self.Classes_Statistics_Statistic58 = Classes_Statistics_Statistic58
        self.Classes_Statistics_Statistic60 = Classes_Statistics_Statistic60
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def Classes_Statistics_Statistic(self):
        return self.__Classes_Statistics_Statistic

    @Classes_Statistics_Statistic.setter
    def Classes_Statistics_Statistic(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Statistics_Statistic__Classes_Statistics_Statistic", None)
        self.__Classes_Statistics_Statistic = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "StatisticEntry"):
                    opp_val = getattr(item, "StatisticEntry", None)
                    
                    if opp_val == self:
                        setattr(item, "StatisticEntry", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "StatisticEntry"):
                    opp_val = getattr(item, "StatisticEntry", None)
                    
                    setattr(item, "StatisticEntry", self)
                    

    @property
    def Classes_Statistics_Statistic60(self):
        return self.__Classes_Statistics_Statistic60

    @Classes_Statistics_Statistic60.setter
    def Classes_Statistics_Statistic60(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Statistics_Statistic__Classes_Statistics_Statistic60", None)
        self.__Classes_Statistics_Statistic60 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Date61"):
                opp_val = getattr(old_value, "Date61", None)
                if opp_val == self:
                    setattr(old_value, "Date61", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Date61"):
                opp_val = getattr(value, "Date61", None)
                setattr(value, "Date61", self)

    @property
    def Classes_Statistics_Statistic58(self):
        return self.__Classes_Statistics_Statistic58

    @Classes_Statistics_Statistic58.setter
    def Classes_Statistics_Statistic58(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Statistics_Statistic__Classes_Statistics_Statistic58", None)
        self.__Classes_Statistics_Statistic58 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Date"):
                opp_val = getattr(old_value, "Date", None)
                if opp_val == self:
                    setattr(old_value, "Date", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Date"):
                opp_val = getattr(value, "Date", None)
                setattr(value, "Date", self)

class IStaff:

    pass
class Classes_Staff_StaffManager(IStaff):

    pass
class IStatisticsGenerator:

    pass
class Classes_Statistics_StatisticsGenerator(IStatisticsGenerator):

    def __init__(self, staticExpenses: float, Classes_Statistics_StatisticsGenerator: "IBills" = None, Classes_Statistics_StatisticsGenerator67: "IBookings" = None, Classes_Statistics_StatisticsGenerator69: "IStaff" = None, IStatisticsGenerator: "Classes_Staff_StaffManager" = None):
        self.staticExpenses = staticExpenses
        self.Classes_Statistics_StatisticsGenerator = Classes_Statistics_StatisticsGenerator
        self.Classes_Statistics_StatisticsGenerator67 = Classes_Statistics_StatisticsGenerator67
        self.Classes_Statistics_StatisticsGenerator69 = Classes_Statistics_StatisticsGenerator69
        
        pass
    @property
    def staticExpenses(self):
        return self.__staticExpenses

    @staticExpenses.setter
    def staticExpenses(self, staticExpenses: float):
        self.__staticExpenses = staticExpenses


    @property
    def Classes_Statistics_StatisticsGenerator69(self):
        return self.__Classes_Statistics_StatisticsGenerator69

    @Classes_Statistics_StatisticsGenerator69.setter
    def Classes_Statistics_StatisticsGenerator69(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Statistics_StatisticsGenerator__Classes_Statistics_StatisticsGenerator69", None)
        self.__Classes_Statistics_StatisticsGenerator69 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IStaff"):
                opp_val = getattr(old_value, "IStaff", None)
                if opp_val == self:
                    setattr(old_value, "IStaff", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IStaff"):
                opp_val = getattr(value, "IStaff", None)
                setattr(value, "IStaff", self)

    @property
    def Classes_Statistics_StatisticsGenerator(self):
        return self.__Classes_Statistics_StatisticsGenerator

    @Classes_Statistics_StatisticsGenerator.setter
    def Classes_Statistics_StatisticsGenerator(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Statistics_StatisticsGenerator__Classes_Statistics_StatisticsGenerator", None)
        self.__Classes_Statistics_StatisticsGenerator = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IBills65"):
                opp_val = getattr(old_value, "IBills65", None)
                if opp_val == self:
                    setattr(old_value, "IBills65", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IBills65"):
                opp_val = getattr(value, "IBills65", None)
                setattr(value, "IBills65", self)

    @property
    def Classes_Statistics_StatisticsGenerator67(self):
        return self.__Classes_Statistics_StatisticsGenerator67

    @Classes_Statistics_StatisticsGenerator67.setter
    def Classes_Statistics_StatisticsGenerator67(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Statistics_StatisticsGenerator__Classes_Statistics_StatisticsGenerator67", None)
        self.__Classes_Statistics_StatisticsGenerator67 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "IBookings"):
                opp_val = getattr(old_value, "IBookings", None)
                if opp_val == self:
                    setattr(old_value, "IBookings", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "IBookings"):
                opp_val = getattr(value, "IBookings", None)
                setattr(value, "IBookings", self)

class Classes_Customers_ICustomers(ABC):

    def __init__(self):
        
        pass
    def getCustomerPhone(self, Classes_SSID) :
        # TODO: Implement getCustomerPhone method
        pass

    def removeCustomerBooking(self, Classes_SSID, Classes_bookingID):
        # TODO: Implement removeCustomerBooking method
        pass

    def getCustomerBookings(self, Classes_SSID) :
        # TODO: Implement getCustomerBookings method
        pass

    def getCustomerRequests(self, Classes_SSID) :
        # TODO: Implement getCustomerRequests method
        pass

    def changeCustomerPhone(self, Classes_SSID, Classes_phoneNr):
        # TODO: Implement changeCustomerPhone method
        pass

    def getCustomerLastName(self, Classes_SSID) :
        # TODO: Implement getCustomerLastName method
        pass

    def getCustomerFirstName(self, Classes_SSID) :
        # TODO: Implement getCustomerFirstName method
        pass

    def getAllCustomers(self) :
        # TODO: Implement getAllCustomers method
        pass

    def changeCustomerFirstName(self, Classes_firstName, Classes_SSID):
        # TODO: Implement changeCustomerFirstName method
        pass

    def addCustomer(self, Classes_title, Classes_phone, Classes_email, Classes_firstname, Classes_lastname, Classes_SSID):
        # TODO: Implement addCustomer method
        pass

    def changeCustomerEmail(self, Classes_SSID, Classes_eMail):
        # TODO: Implement changeCustomerEmail method
        pass

    def searchCustomers(self, Classes_keyword) :
        # TODO: Implement searchCustomers method
        pass

    def changeCustomerLastName(self, Classes_SSID, Classes_lastName):
        # TODO: Implement changeCustomerLastName method
        pass

    def addCustomerBooking(self, Classes_SSID, Classes_bookingID):
        # TODO: Implement addCustomerBooking method
        pass

    def removeCustomerRequest(self, Classes_SSID, Classes_requestID):
        # TODO: Implement removeCustomerRequest method
        pass

    def changeCustomerTitle(self, Classes_SSID, Classes_title):
        # TODO: Implement changeCustomerTitle method
        pass

    def getCustomerTitle(self, Classes_SSID) :
        # TODO: Implement getCustomerTitle method
        pass

    def getCustomerEmail(self, Classes_SSID) :
        # TODO: Implement getCustomerEmail method
        pass

    def addCustomerRequest(self, Classes_description, Classes_SSID):
        # TODO: Implement addCustomerRequest method
        pass

class Classes_Customers_Customer:

    def __init__(self, firstname: str, lastname: str, title: str, email: str, phone: str, ssid: str, bookings: str, requests: str):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.email = email
        self.phone = phone
        self.ssid = ssid
        self.bookings = bookings
        self.requests = requests
        
        pass
    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname


    @property
    def bookings(self):
        return self.__bookings

    @bookings.setter
    def bookings(self, bookings: str):
        self.__bookings = bookings


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def requests(self):
        return self.__requests

    @requests.setter
    def requests(self, requests: str):
        self.__requests = requests


    @property
    def ssid(self):
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid


    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone


    def removeRequest(self):
        # TODO: Implement removeRequest method
        pass

    def addRequest(self):
        # TODO: Implement addRequest method
        pass

    def removeBooking(self):
        # TODO: Implement removeBooking method
        pass

    def addBooking(self):
        # TODO: Implement addBooking method
        pass

class Customer:

    pass
class Booking:

    pass
class IBookings:

    pass
class Classes_Bookings_BookingsManager(IBookings):

    pass
class Classes_Bookings_Booking:

    def __init__(self, bookedStays: str, customer: str, bookingNbr: str, nbrGuests: str, issueDate: date, requests: str, Classes_Bookings_Booking: "CreditCard" = None):
        self.bookedStays = bookedStays
        self.customer = customer
        self.bookingNbr = bookingNbr
        self.nbrGuests = nbrGuests
        self.issueDate = issueDate
        self.requests = requests
        self.Classes_Bookings_Booking = Classes_Bookings_Booking
        
        pass
    @property
    def requests(self):
        return self.__requests

    @requests.setter
    def requests(self, requests: str):
        self.__requests = requests


    @property
    def issueDate(self):
        return self.__issueDate

    @issueDate.setter
    def issueDate(self, issueDate: date):
        self.__issueDate = issueDate


    @property
    def bookedStays(self):
        return self.__bookedStays

    @bookedStays.setter
    def bookedStays(self, bookedStays: str):
        self.__bookedStays = bookedStays


    @property
    def customer(self):
        return self.__customer

    @customer.setter
    def customer(self, customer: str):
        self.__customer = customer


    @property
    def nbrGuests(self):
        return self.__nbrGuests

    @nbrGuests.setter
    def nbrGuests(self, nbrGuests: str):
        self.__nbrGuests = nbrGuests


    @property
    def bookingNbr(self):
        return self.__bookingNbr

    @bookingNbr.setter
    def bookingNbr(self, bookingNbr: str):
        self.__bookingNbr = bookingNbr


    @property
    def Classes_Bookings_Booking(self):
        return self.__Classes_Bookings_Booking

    @Classes_Bookings_Booking.setter
    def Classes_Bookings_Booking(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Bookings_Booking__Classes_Bookings_Booking", None)
        self.__Classes_Bookings_Booking = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CreditCard36"):
                opp_val = getattr(old_value, "CreditCard36", None)
                if opp_val == self:
                    setattr(old_value, "CreditCard36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CreditCard36"):
                opp_val = getattr(value, "CreditCard36", None)
                setattr(value, "CreditCard36", self)

    def addRequest(self, Classes_requestID):
        # TODO: Implement addRequest method
        pass

    def cancelBookedStay(self, Classes_stayID):
        # TODO: Implement cancelBookedStay method
        pass

    def removeRequest(self, Classes_requestID):
        # TODO: Implement removeRequest method
        pass

    def addBookedStay(self, Classes_stayID):
        # TODO: Implement addBookedStay method
        pass

class Classes_Bookings_IBookings(ABC):

    def __init__(self):
        
        pass
    def payBookingBills(self, Classes_bookingID):
        # TODO: Implement payBookingBills method
        pass

    def getAvailableBookablesInPeriod(self, Classes_from_, Classes_to) :
        # TODO: Implement getAvailableBookablesInPeriod method
        pass

    def removeBookingRequest(self, Classes_requestID, Classes_bookingID):
        # TODO: Implement removeBookingRequest method
        pass

    def makeBooking(self, Classes_requests, Classes_expiryYear, Classes_ccv, Classes_ccNumber, Classes_customerID, Classes_bookables, Classes_expiryMonth, Classes_firstName, Classes_lastName, Classes_guests):
        # TODO: Implement makeBooking method
        pass

    def getBookingRequests(self, Classes_bookingID) :
        # TODO: Implement getBookingRequests method
        pass

    def searchForAvailableHotelRoomsInPeriod(self, Classes_from_, Classes_keyword, Classes_to) :
        # TODO: Implement searchForAvailableHotelRoomsInPeriod method
        pass

    def searchBookingsMadeInPeriod(self, Classes_keyword, Classes_from_, Classes_to) :
        # TODO: Implement searchBookingsMadeInPeriod method
        pass

    def searchBookings(self, Classes_keyword) :
        # TODO: Implement searchBookings method
        pass

    def getAvailableHotelRoomsInPeriod(self, Classes_to, Classes_from_) :
        # TODO: Implement getAvailableHotelRoomsInPeriod method
        pass

    def cancelBooking(self, Classes_bookingID):
        # TODO: Implement cancelBooking method
        pass

    def getAllBookings(self) :
        # TODO: Implement getAllBookings method
        pass

    def getNbrGuestOfBooking(self, Classes_bookingID) :
        # TODO: Implement getNbrGuestOfBooking method
        pass

    def searchForAvailableBookablesInPeriod(self, Classes_to, Classes_keyword, Classes_from_) :
        # TODO: Implement searchForAvailableBookablesInPeriod method
        pass

    def addBookingRequest(self, Classes_bookingID, Classes_requestID):
        # TODO: Implement addBookingRequest method
        pass

    def getAvailableHostelBedsInPeriod(self, Classes_from_, Classes_to) :
        # TODO: Implement getAvailableHostelBedsInPeriod method
        pass

    def searchForAvailableHostelBedsInPeriod(self, Classes_keyword, Classes_to, Classes_from_) :
        # TODO: Implement searchForAvailableHostelBedsInPeriod method
        pass

    def addBookedStayToBooking(self, Classes_stayID, Classes_bookingID):
        # TODO: Implement addBookedStayToBooking method
        pass

    def getCustomerOfBooking(self, Classes_bookingID) :
        # TODO: Implement getCustomerOfBooking method
        pass

    def payStayBills(self, Classes_bookingID, Classes_stayID):
        # TODO: Implement payStayBills method
        pass

    def searchForAvailableConferenceRoomsInPeriod(self, Classes_from_, Classes_keyword, Classes_to) :
        # TODO: Implement searchForAvailableConferenceRoomsInPeriod method
        pass

    def changeNbrGuestsOfBooking(self, Classes_nbrGuests, Classes_bookingID):
        # TODO: Implement changeNbrGuestsOfBooking method
        pass

    def cancelStayOfBooking(self, Classes_stayID, Classes_bookingID):
        # TODO: Implement cancelStayOfBooking method
        pass

    def getAllBookingsWithStaysInPeriod(self, Classes_to, Classes_from_) :
        # TODO: Implement getAllBookingsWithStaysInPeriod method
        pass

    def getAllBookingsWithinPeriod(self, Classes_to, Classes_from_) :
        # TODO: Implement getAllBookingsWithinPeriod method
        pass

    def getBookedStaysOfBooking(self, Classes_bookingID) :
        # TODO: Implement getBookedStaysOfBooking method
        pass

    def searchBookingsWithStaysInPeriod(self, Classes_keyword, Classes_from_, Classes_to) :
        # TODO: Implement searchBookingsWithStaysInPeriod method
        pass

    def getAvailableConferenceRoomsInPeriod(self, Classes_from_, Classes_to) :
        # TODO: Implement getAvailableConferenceRoomsInPeriod method
        pass

class ICustomers:

    pass
class Classes_Customers_CustomersManager(ICustomers):

    pass
class Classes_Accounts_IManageAccounts(ABC):

    def __init__(self):
        
        pass
    def searchAccounts(self, Classes_keyword) :
        # TODO: Implement searchAccounts method
        pass

    def changePassword(self, Classes_newPassword, Classes_username):
        # TODO: Implement changePassword method
        pass

    def getAccountPassword(self, Classes_username) :
        # TODO: Implement getAccountPassword method
        pass

    def deleteAccount(self, Classes_username):
        # TODO: Implement deleteAccount method
        pass

    def getAccountName(self, Classes_username) :
        # TODO: Implement getAccountName method
        pass

    def renameAccount(self, Classes_newUsername, Classes_oldUsername):
        # TODO: Implement renameAccount method
        pass

    def addAccount(self, Classes_password, Classes_type, Classes_username):
        # TODO: Implement addAccount method
        pass

class Classes_Accounts_IAccountsAccess(ABC):

    def __init__(self):
        
        pass
    def validateAccount(self, Classes_password, Classes_username) :
        # TODO: Implement validateAccount method
        pass

    def login(self, Classes_username, Classes_password) :
        # TODO: Implement login method
        pass

class Account:

    pass
class Accounts_IAccountsAccess:

    pass
class Accounts_IManageAccounts:

    pass
class Classes_Accounts_AccountsManager(Accounts_IManageAccounts, Accounts_IAccountsAccess):

    pass
class Classes_Accounts_Account:

    def __init__(self, accountType: str, username: str, password: str):
        self.accountType = accountType
        self.username = username
        self.password = password
        
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
    def accountType(self):
        return self.__accountType

    @accountType.setter
    def accountType(self, accountType: str):
        self.__accountType = accountType


class Classes_Guests_Guest:

    def __init__(self, phone: str, ssid: str, requests: str, stays: str, account: str, firstname: str, lastname: str, title: str, email: str):
        self.phone = phone
        self.ssid = ssid
        self.requests = requests
        self.stays = stays
        self.account = account
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.email = email
        
        pass
    @property
    def stays(self):
        return self.__stays

    @stays.setter
    def stays(self, stays: str):
        self.__stays = stays


    @property
    def title(self):
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title


    @property
    def lastname(self):
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname


    @property
    def ssid(self):
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid


    @property
    def phone(self):
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone


    @property
    def firstname(self):
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname


    @property
    def email(self):
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email


    @property
    def requests(self):
        return self.__requests

    @requests.setter
    def requests(self, requests: str):
        self.__requests = requests


    @property
    def account(self):
        return self.__account

    @account.setter
    def account(self, account: str):
        self.__account = account


    def addRequest(self, Classes_description, Classes_requestID):
        # TODO: Implement addRequest method
        pass

    def addStay(self, Classes_bookingID, Classes_toDate, Classes_fromDate, Classes_bookableID):
        # TODO: Implement addStay method
        pass

    def removeRequest(self, Classes_requestID):
        # TODO: Implement removeRequest method
        pass

    def removeStay(self, Classes_stayID):
        # TODO: Implement removeStay method
        pass

class IManageAccounts:

    pass
class Guest:

    pass
class Classes_Guests_IGuests(ABC):

    def __init__(self):
        
        pass
    def changeGuestLastName(self, Classes_SSID, Classes_lastName):
        # TODO: Implement changeGuestLastName method
        pass

    def getGuestEmail(self, Classes_SSID) :
        # TODO: Implement getGuestEmail method
        pass

    def getGuestAccountPassword(self, Classes_SSID) :
        # TODO: Implement getGuestAccountPassword method
        pass

    def searchGuests(self, Classes_keyword) :
        # TODO: Implement searchGuests method
        pass

    def getGuestStays(self, Classes_SSID) :
        # TODO: Implement getGuestStays method
        pass

    def generateGuestAccount(self, Classes_SSID):
        # TODO: Implement generateGuestAccount method
        pass

    def changeGuestPhone(self, Classes_SSID, Classes_phoneNr):
        # TODO: Implement changeGuestPhone method
        pass

    def getGuestLastName(self, Classes_SSID) :
        # TODO: Implement getGuestLastName method
        pass

    def getGuestTitle(self, Classes_SSID) :
        # TODO: Implement getGuestTitle method
        pass

    def addGuest(self, Classes_SSID, Classes_phone, Classes_title, Classes_firstname, Classes_email, Classes_lastname):
        # TODO: Implement addGuest method
        pass

    def changeGuestTitle(self, Classes_title, Classes_SSID):
        # TODO: Implement changeGuestTitle method
        pass

    def getGuestRequests(self, Classes_SSID) :
        # TODO: Implement getGuestRequests method
        pass

    def changeGuestEmail(self, Classes_eMail, Classes_SSID):
        # TODO: Implement changeGuestEmail method
        pass

    def getGuestFirstName(self, Classes_SSID) :
        # TODO: Implement getGuestFirstName method
        pass

    def getAllGuestIDs(self) :
        # TODO: Implement getAllGuestIDs method
        pass

    def addGuestRequest(self, Classes_desctiption, Classes_SSID, Classes_requestID):
        # TODO: Implement addGuestRequest method
        pass

    def removeGuestRequest(self, Classes_SSID, Classes_requestID):
        # TODO: Implement removeGuestRequest method
        pass

    def removeGuestStay(self, Classes_stayID, Classes_SSID):
        # TODO: Implement removeGuestStay method
        pass

    def getGuestPhone(self, Classes_SSID) :
        # TODO: Implement getGuestPhone method
        pass

    def removeGuestAccount(self, Classes_SSID):
        # TODO: Implement removeGuestAccount method
        pass

    def changeGuestFirstName(self, Classes_firstName, Classes_SSID):
        # TODO: Implement changeGuestFirstName method
        pass

    def getGuestAccountUsername(self, Classes_SSID) :
        # TODO: Implement getGuestAccountUsername method
        pass

class Classes_Services_IServicesAccess(ABC):

    def __init__(self):
        
        pass
    def getAllServiceIDs(self) :
        # TODO: Implement getAllServiceIDs method
        pass

    def getRSOItems(self, Classes_orderID) :
        # TODO: Implement getRSOItems method
        pass

    def changeRSOISDelivered(self, Classes_orderID, Classes_isDelivered):
        # TODO: Implement changeRSOISDelivered method
        pass

    def isRSODelivered(self, Classes_orderID) :
        # TODO: Implement isRSODelivered method
        pass

    def setRSOBill(self, Classes_orderID, Classes_billID):
        # TODO: Implement setRSOBill method
        pass

    def getRoomServiceMenuItems(self) :
        # TODO: Implement getRoomServiceMenuItems method
        pass

    def makeRoomServiceOrder(self, Classes_isDelivered, Classes_items, Classes_bookable, Classes_deliveryDate, Classes_services, Classes_bill):
        # TODO: Implement makeRoomServiceOrder method
        pass

    def getServicePrice(self, Classes_serviceID) :
        # TODO: Implement getServicePrice method
        pass

    def getAllRoomServiceOrderIDs(self) :
        # TODO: Implement getAllRoomServiceOrderIDs method
        pass

    def searchServices(self, Classes_keyword) :
        # TODO: Implement searchServices method
        pass

    def getRSODeliveryDate(self, Classes_orderID) :
        # TODO: Implement getRSODeliveryDate method
        pass

    def searchRoomServiceOrders(self, Classes_keyword) :
        # TODO: Implement searchRoomServiceOrders method
        pass

    def getRoomServiceMenuName(self) :
        # TODO: Implement getRoomServiceMenuName method
        pass

    def getRSOBookable(self, Classes_orderID) :
        # TODO: Implement getRSOBookable method
        pass

    def getServiceName(self, Classes_serviceID) :
        # TODO: Implement getServiceName method
        pass

    def getRSOBill(self, Classes_orderID) :
        # TODO: Implement getRSOBill method
        pass

    def changeRSODeliveryDate(self, Classes_date, Classes_orderID):
        # TODO: Implement changeRSODeliveryDate method
        pass

    def getRSOServices(self, Classes_orderID) :
        # TODO: Implement getRSOServices method
        pass

    def getServiceExpense(self, Classes_serviceID) :
        # TODO: Implement getServiceExpense method
        pass

class Classes_Services_RoomServiceOrder:

    def __init__(self, isDelivered: str, deliveryDate: date, bookable: str, items: str, id: str, bill: str, Classes_Services_RoomServiceOrder: set["Service"] = None):
        self.isDelivered = isDelivered
        self.deliveryDate = deliveryDate
        self.bookable = bookable
        self.items = items
        self.id = id
        self.bill = bill
        self.Classes_Services_RoomServiceOrder = Classes_Services_RoomServiceOrder if Classes_Services_RoomServiceOrder is not None else set()
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items


    @property
    def bill(self):
        return self.__bill

    @bill.setter
    def bill(self, bill: str):
        self.__bill = bill


    @property
    def deliveryDate(self):
        return self.__deliveryDate

    @deliveryDate.setter
    def deliveryDate(self, deliveryDate: date):
        self.__deliveryDate = deliveryDate


    @property
    def bookable(self):
        return self.__bookable

    @bookable.setter
    def bookable(self, bookable: str):
        self.__bookable = bookable


    @property
    def isDelivered(self):
        return self.__isDelivered

    @isDelivered.setter
    def isDelivered(self, isDelivered: str):
        self.__isDelivered = isDelivered


    @property
    def Classes_Services_RoomServiceOrder(self):
        return self.__Classes_Services_RoomServiceOrder

    @Classes_Services_RoomServiceOrder.setter
    def Classes_Services_RoomServiceOrder(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Services_RoomServiceOrder__Classes_Services_RoomServiceOrder", None)
        self.__Classes_Services_RoomServiceOrder = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Service30"):
                    opp_val = getattr(item, "Service30", None)
                    
                    if opp_val == self:
                        setattr(item, "Service30", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Service30"):
                    opp_val = getattr(item, "Service30", None)
                    
                    setattr(item, "Service30", self)
                    

    def addService(self):
        # TODO: Implement addService method
        pass

    def removeItem(self):
        # TODO: Implement removeItem method
        pass

    def addItem(self):
        # TODO: Implement addItem method
        pass

    def removeService(self):
        # TODO: Implement removeService method
        pass

class Classes_Services_Service:

    def __init__(self, name: str, price: float, expense: float, id: str):
        self.name = name
        self.price = price
        self.expense = expense
        self.id = id
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def expense(self):
        return self.__expense

    @expense.setter
    def expense(self, expense: float):
        self.__expense = expense


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


class RoomServiceMenu:

    pass
class Classes_Inventory_IInventoryAccess(ABC):

    def __init__(self):
        
        pass
    def changeItemStock(self, Classes_stock, Classes_id):
        # TODO: Implement changeItemStock method
        pass

    def getItemName(self, Classes_id) :
        # TODO: Implement getItemName method
        pass

    def getItemPrice(self, Classes_id) :
        # TODO: Implement getItemPrice method
        pass

    def getAllItemIDs(self) :
        # TODO: Implement getAllItemIDs method
        pass

    def getItemExpense(self, Classes_id) :
        # TODO: Implement getItemExpense method
        pass

    def searchItems(self, Classes_keyword) :
        # TODO: Implement searchItems method
        pass

    def getItemStock(self, Classes_id) :
        # TODO: Implement getItemStock method
        pass

class Classes_Inventory_Item:

    def __init__(self, name: str, price: float, expense: float, stock: str, id: str):
        self.name = name
        self.price = price
        self.expense = expense
        self.stock = stock
        self.id = id
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def expense(self):
        return self.__expense

    @expense.setter
    def expense(self, expense: float):
        self.__expense = expense


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def stock(self):
        return self.__stock

    @stock.setter
    def stock(self, stock: str):
        self.__stock = stock


class Item:

    pass
class IManageInventory:

    pass
class Classes_Inventory_InventoryManager(IManageInventory):

    pass
class RoomServiceOrder:

    pass
class Service:

    pass
class IServicesManage:

    pass
class Classes_Services_ServiceManager(IServicesManage):

    pass
class Classes_Services_RoomServiceMenu:

    def __init__(self, name: str, items: str):
        self.name = name
        self.items = items
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items


    def removeItem(self, Classes_itemID):
        # TODO: Implement removeItem method
        pass

    def addItem(self, Classes_itemID):
        # TODO: Implement addItem method
        pass

class Classes_Bills_Bill:

    def __init__(self, isPaid: str, paymentType: str, id: str, items: str, services: str, bookable: str, issueDate: date, paymentDate: date, totalAmount: float):
        self.isPaid = isPaid
        self.paymentType = paymentType
        self.id = id
        self.items = items
        self.services = services
        self.bookable = bookable
        self.issueDate = issueDate
        self.paymentDate = paymentDate
        self.totalAmount = totalAmount
        
        pass
    @property
    def bookable(self):
        return self.__bookable

    @bookable.setter
    def bookable(self, bookable: str):
        self.__bookable = bookable


    @property
    def issueDate(self):
        return self.__issueDate

    @issueDate.setter
    def issueDate(self, issueDate: date):
        self.__issueDate = issueDate


    @property
    def paymentDate(self):
        return self.__paymentDate

    @paymentDate.setter
    def paymentDate(self, paymentDate: date):
        self.__paymentDate = paymentDate


    @property
    def isPaid(self):
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: str):
        self.__isPaid = isPaid


    @property
    def services(self):
        return self.__services

    @services.setter
    def services(self, services: str):
        self.__services = services


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def items(self):
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items


    @property
    def paymentType(self):
        return self.__paymentType

    @paymentType.setter
    def paymentType(self, paymentType: str):
        self.__paymentType = paymentType


    @property
    def totalAmount(self):
        return self.__totalAmount

    @totalAmount.setter
    def totalAmount(self, totalAmount: float):
        self.__totalAmount = totalAmount


    def addService(self, Classes_serviceID):
        # TODO: Implement addService method
        pass

    def addItem(self, Classes_itemID):
        # TODO: Implement addItem method
        pass

class IServicesAccess:

    pass
class Classes_Services_IServicesManage(IServicesAccess):

    def __init__(self, IServicesAccess: "Classes_Bills_BillsManager" = None):
        
        pass
    def changeServicePrice(self, Classes_serviceID, Classes_price):
        # TODO: Implement changeServicePrice method
        pass

    def changeRoomServiceMenuName(self, Classes_name):
        # TODO: Implement changeRoomServiceMenuName method
        pass

    def addRoomServiceMenuItem(self, Classes_itemID):
        # TODO: Implement addRoomServiceMenuItem method
        pass

    def changeServiceName(self, Classes_name, Classes_serviceID):
        # TODO: Implement changeServiceName method
        pass

    def addService(self, Classes_expense, Classes_price, Classes_name):
        # TODO: Implement addService method
        pass

    def changeServiceExpense(self, Classes_expense, Classes_serviceID):
        # TODO: Implement changeServiceExpense method
        pass

    def removeRoomServiceMenuItem(self, Classes_itemID):
        # TODO: Implement removeRoomServiceMenuItem method
        pass

class IInventoryAccess:

    pass
class Classes_Inventory_IManageInventory(IInventoryAccess):

    def __init__(self, IInventoryAccess: "Classes_Bills_BillsManager" = None):
        
        pass
    def changeItemPrice(self, Classes_price, Classes_id):
        # TODO: Implement changeItemPrice method
        pass

    def addItem(self, Classes_name, Classes_price, Classes_expense, Classes_stock):
        # TODO: Implement addItem method
        pass

    def removeItem(self, Classes_id):
        # TODO: Implement removeItem method
        pass

    def changeItemName(self, Classes_id, Classes_name):
        # TODO: Implement changeItemName method
        pass

    def changeItemExpense(self, Classes_id, Classes_expense):
        # TODO: Implement changeItemExpense method
        pass

class Bill:

    pass
class Classes_Bills_IBills(ABC):

    def __init__(self):
        
        pass
    def addBill(self, Classes_bookable, Classes_services, Classes_items):
        # TODO: Implement addBill method
        pass

    def getBillTotalAmount(self, Classes_billID) :
        # TODO: Implement getBillTotalAmount method
        pass

    def removeBill(self, Classes_billID):
        # TODO: Implement removeBill method
        pass

    def getAllBillIDs(self) :
        # TODO: Implement getAllBillIDs method
        pass

    def sendInvoice(self, Classes_email, Classes_billID):
        # TODO: Implement sendInvoice method
        pass

    def getBillBookable(self, Classes_billID) :
        # TODO: Implement getBillBookable method
        pass

    def getBillPaymentDate(self, Classes_billID) :
        # TODO: Implement getBillPaymentDate method
        pass

    def getBillServices(self, Classes_billID) :
        # TODO: Implement getBillServices method
        pass

    def payBillsWithCreditCard(self, Classes_ccNumber, Classes_bills, Classes_firstName, Classes_expiryMonth, Classes_ccv, Classes_lastName, Classes_expiryYear):
        # TODO: Implement payBillsWithCreditCard method
        pass

    def getBillPaymentType(self, Classes_billID) :
        # TODO: Implement getBillPaymentType method
        pass

    def getBillIssueDate(self, Classes_billID) :
        # TODO: Implement getBillIssueDate method
        pass

    def getIsBillPaid(self, Classes_billID) :
        # TODO: Implement getIsBillPaid method
        pass

    def getAllPayedBills(self) :
        # TODO: Implement getAllPayedBills method
        pass

    def payBillsWithCash(self, Classes_bills):
        # TODO: Implement payBillsWithCash method
        pass

    def getAllBillsNotPaid(self) :
        # TODO: Implement getAllBillsNotPaid method
        pass

    def getBillItems(self, Classes_billID) :
        # TODO: Implement getBillItems method
        pass

    def searchBills(self, Classes_keyword) :
        # TODO: Implement searchBills method
        pass

class Classes_Banking_CustomerProvides(ABC):

    def __init__(self):
        
        pass
    def makePayment(self, Classes_firstName, Classes_expiryMonth, Classes_ccv, Classes_lastName, Classes_ccNumber, Classes_expiryYear, Classes_sum) :
        # TODO: Implement makePayment method
        pass

    def isCreditCardValid(self, Classes_expiryMonth, Classes_expiryYear, Classes_firstName, Classes_ccv, Classes_ccNumber, Classes_lastName) :
        # TODO: Implement isCreditCardValid method
        pass

class Classes_Banking_AdministratorProvides(ABC):

    def __init__(self):
        
        pass
    def getBalance(self, Classes_expiryMonth, Classes_expiryYear, Classes_lastName, Classes_ccNumber, Classes_ccv, Classes_firstName) :
        # TODO: Implement getBalance method
        pass

    def makeDeposit(self, Classes_expiryYear, Classes_lastName, Classes_ccNumber, Classes_expiryMonth, Classes_sum, Classes_firstName, Classes_ccv) :
        # TODO: Implement makeDeposit method
        pass

    def addCreditCard(self, Classes_lastName, Classes_firstName, Classes_expiryMonth, Classes_ccNumber, Classes_expiryYear, Classes_ccv) :
        # TODO: Implement addCreditCard method
        pass

    def removeCreditCard(self, Classes_ccNumber, Classes_expiryMonth, Classes_expiryYear, Classes_lastName, Classes_firstName, Classes_ccv) :
        # TODO: Implement removeCreditCard method
        pass

class CustomerProvides:

    pass
class Stay:

    pass
class Classes_Stays_CreditCard:

    def __init__(self, ccNumber: str, ccv: str, expiryMonth: str, expiryYear: str, firstName: str, lastName: str):
        self.ccNumber = ccNumber
        self.ccv = ccv
        self.expiryMonth = expiryMonth
        self.expiryYear = expiryYear
        self.firstName = firstName
        self.lastName = lastName
        
        pass
    @property
    def lastName(self):
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName


    @property
    def ccNumber(self):
        return self.__ccNumber

    @ccNumber.setter
    def ccNumber(self, ccNumber: str):
        self.__ccNumber = ccNumber


    @property
    def firstName(self):
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName


    @property
    def ccv(self):
        return self.__ccv

    @ccv.setter
    def ccv(self, ccv: str):
        self.__ccv = ccv


    @property
    def expiryYear(self):
        return self.__expiryYear

    @expiryYear.setter
    def expiryYear(self, expiryYear: str):
        self.__expiryYear = expiryYear


    @property
    def expiryMonth(self):
        return self.__expiryMonth

    @expiryMonth.setter
    def expiryMonth(self, expiryMonth: str):
        self.__expiryMonth = expiryMonth


class CreditCard:

    pass
class Classes_Stays_IStays(ABC):

    def __init__(self):
        
        pass
    def searchHotelStays(self, Classes_keyword) :
        # TODO: Implement searchHotelStays method
        pass

    def removeStay(self, Classes_stayID):
        # TODO: Implement removeStay method
        pass

    def changePeriodOfStay(self, Classes_stayID, Classes_to, Classes_from_):
        # TODO: Implement changePeriodOfStay method
        pass

    def billCreditCardWithAllUnpaidBillsOfHotelStay(self, Classes_stayID):
        # TODO: Implement billCreditCardWithAllUnpaidBillsOfHotelStay method
        pass

    def isResponsibleCreditCardAdded(self, Classes_stayID) :
        # TODO: Implement isResponsibleCreditCardAdded method
        pass

    def addResponsibleCreditCard(self, Classes_expiryYear, Classes_stayID, Classes_firstName, Classes_ccNumber, Classes_lastName, Classes_expiryMonth, Classes_ccv):
        # TODO: Implement addResponsibleCreditCard method
        pass

    def checkInGuest(self, Classes_guestID, Classes_stayID):
        # TODO: Implement checkInGuest method
        pass

    def getAllHotelStaysWithinPeriod(self, Classes_to, Classes_from_) :
        # TODO: Implement getAllHotelStaysWithinPeriod method
        pass

    def searchHotelStaysWithinPeriod(self, Classes_to, Classes_keyword, Classes_from_) :
        # TODO: Implement searchHotelStaysWithinPeriod method
        pass

    def getBillsOfHotelStay(self, Classes_stayID) :
        # TODO: Implement getBillsOfHotelStay method
        pass

    def removeBillFromStay(self, Classes_stayID, Classes_billID):
        # TODO: Implement removeBillFromStay method
        pass

    def checkOutGuest(self, Classes_stayID, Classes_guestID):
        # TODO: Implement checkOutGuest method
        pass

    def getCheckedInGuestsOfHotelStay(self, Classes_stayID) :
        # TODO: Implement getCheckedInGuestsOfHotelStay method
        pass

    def getCheckedOutGuestsOfHotelStay(self, Classes_stayID) :
        # TODO: Implement getCheckedOutGuestsOfHotelStay method
        pass

    def addBillToStay(self, Classes_billID, Classes_stayID):
        # TODO: Implement addBillToStay method
        pass

    def getAllUnpayedBillsOfHotelStay(self, Classes_stayID) :
        # TODO: Implement getAllUnpayedBillsOfHotelStay method
        pass

    def getAllHotelStayIDs(self) :
        # TODO: Implement getAllHotelStayIDs method
        pass

    def getGuestsOfHotelStay(self, Classes_stayID) :
        # TODO: Implement getGuestsOfHotelStay method
        pass

    def getBookingOfHotelStay(self, Classes_stayID) :
        # TODO: Implement getBookingOfHotelStay method
        pass

    def changeResponsibleCreditCard(self, Classes_expiryYear, Classes_lastName, Classes_stayID, Classes_ccv, Classes_expiryMonth, Classes_firstName, Classes_ccNumber):
        # TODO: Implement changeResponsibleCreditCard method
        pass

    def changeBookableOfStay(self, Classes_stayID, Classes_bookableID):
        # TODO: Implement changeBookableOfStay method
        pass

    def getBookableOfHotelStay(self, Classes_stayID) :
        # TODO: Implement getBookableOfHotelStay method
        pass

    def addNewStay(self, Classes_toDate, Classes_fromDate, Classes_bookingID, Classes_bookableID):
        # TODO: Implement addNewStay method
        pass

class IGuests:

    pass
class Classes_Guests_GuestsManager(IGuests):

    pass
class IBills:

    pass
class Classes_Bills_BillsManager(IBills):

    pass
class Classes_Stays_Stay:

    def __init__(self, ID: str, bookable: str, bills: str, checkedInGuests: str, booking: str, checkedOutGuests: str, fromDate: date, toDate: date, Classes_Stays_Stay: "CreditCard" = None):
        self.ID = ID
        self.bookable = bookable
        self.bills = bills
        self.checkedInGuests = checkedInGuests
        self.booking = booking
        self.checkedOutGuests = checkedOutGuests
        self.fromDate = fromDate
        self.toDate = toDate
        self.Classes_Stays_Stay = Classes_Stays_Stay
        
        pass
    @property
    def bills(self):
        return self.__bills

    @bills.setter
    def bills(self, bills: str):
        self.__bills = bills


    @property
    def fromDate(self):
        return self.__fromDate

    @fromDate.setter
    def fromDate(self, fromDate: date):
        self.__fromDate = fromDate


    @property
    def checkedInGuests(self):
        return self.__checkedInGuests

    @checkedInGuests.setter
    def checkedInGuests(self, checkedInGuests: str):
        self.__checkedInGuests = checkedInGuests


    @property
    def checkedOutGuests(self):
        return self.__checkedOutGuests

    @checkedOutGuests.setter
    def checkedOutGuests(self, checkedOutGuests: str):
        self.__checkedOutGuests = checkedOutGuests


    @property
    def ID(self):
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID


    @property
    def booking(self):
        return self.__booking

    @booking.setter
    def booking(self, booking: str):
        self.__booking = booking


    @property
    def bookable(self):
        return self.__bookable

    @bookable.setter
    def bookable(self, bookable: str):
        self.__bookable = bookable


    @property
    def toDate(self):
        return self.__toDate

    @toDate.setter
    def toDate(self, toDate: date):
        self.__toDate = toDate


    @property
    def Classes_Stays_Stay(self):
        return self.__Classes_Stays_Stay

    @Classes_Stays_Stay.setter
    def Classes_Stays_Stay(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Classes_Stays_Stay__Classes_Stays_Stay", None)
        self.__Classes_Stays_Stay = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CreditCard"):
                opp_val = getattr(old_value, "CreditCard", None)
                if opp_val == self:
                    setattr(old_value, "CreditCard", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CreditCard"):
                opp_val = getattr(value, "CreditCard", None)
                setattr(value, "CreditCard", self)

    def addCheckedInGuest(self, Classes_SSID):
        # TODO: Implement addCheckedInGuest method
        pass

    def checkOutGuest(self):
        # TODO: Implement checkOutGuest method
        pass

    def addBill(self, Classes_billID):
        # TODO: Implement addBill method
        pass

class IStays:

    pass
class Classes_Stays_StaysManager(IStays):

    pass
class IBookablesManage:

    pass
class Classes_Bookables_BookablesManager(IBookablesManage):

    pass
class Classes_Bookables_IBookablesAccess(ABC):

    def __init__(self):
        
        pass
    def getAllBookableIDs(self) :
        # TODO: Implement getAllBookableIDs method
        pass

    def getHotelRoomNbrBeds(self, Classes_ID) :
        # TODO: Implement getHotelRoomNbrBeds method
        pass

    def getAllHotelRoomIDs(self) :
        # TODO: Implement getAllHotelRoomIDs method
        pass

    def getBookableDescription(self, Classes_bookableID) :
        # TODO: Implement getBookableDescription method
        pass

    def getHotelRoomCategory(self, Classes_roomID) :
        # TODO: Implement getHotelRoomCategory method
        pass

    def getConferenceRoomCapacity(self, Classes_roomID) :
        # TODO: Implement getConferenceRoomCapacity method
        pass

    def getConferenceRoomCategory(self, Classes_roomID) :
        # TODO: Implement getConferenceRoomCategory method
        pass

    def searchConferenceRooms(self, Classes_keyword, Classes_category) :
        # TODO: Implement searchConferenceRooms method
        pass

    def getRoomOfHostelBed(self, Classes_hostelBedID) :
        # TODO: Implement getRoomOfHostelBed method
        pass

    def getAllConferenceRoomIDs(self) :
        # TODO: Implement getAllConferenceRoomIDs method
        pass

    def getRoomLocationInfo(self, Classes_roomID) :
        # TODO: Implement getRoomLocationInfo method
        pass

    def getBookableBasePrice(self, Classes_bookableID) :
        # TODO: Implement getBookableBasePrice method
        pass

    def getRoomLocationFloor(self, Classes_roomID) :
        # TODO: Implement getRoomLocationFloor method
        pass

    def searchForBookable(self, Classes_keyword) :
        # TODO: Implement searchForBookable method
        pass

    def searchHostelBeds(self, Classes_keyword) :
        # TODO: Implement searchHostelBeds method
        pass

    def getAllHostelBedIDs(self) :
        # TODO: Implement getAllHostelBedIDs method
        pass

    def searchHotelRooms(self, Classes_category, Classes_keyword) :
        # TODO: Implement searchHotelRooms method
        pass

class IBookablesAccess:

    pass
class Classes_Bookables_IBookablesManage(IBookablesAccess):

    def __init__(self, IBookablesAccess40: "Classes_Bookings_BookingsManager" = None, IBookablesAccess: "Classes_Bills_BillsManager" = None):
        
        pass
    def changeConferenceRoomCapacity(self, Classes_capacity, Classes_roomID):
        # TODO: Implement changeConferenceRoomCapacity method
        pass

    def changeRoomLocation(self, Classes_roomID, Classes_floor, Classes_additionalInfo):
        # TODO: Implement changeRoomLocation method
        pass

    def changeHostelBedRoom(self, Classes_hostelBedID, Classes_roomID):
        # TODO: Implement changeHostelBedRoom method
        pass

    def addHostelBed(self, Classes_description, Classes_basePrice, Classes_bedNumber, Classes_roomID) :
        # TODO: Implement addHostelBed method
        pass

    def changeBookableBasePrice(self, Classes_basePrice, Classes_bookableID):
        # TODO: Implement changeBookableBasePrice method
        pass

    def changeHotelRoomNumberBeds(self, Classes_roomID, Classes_nbrBeds):
        # TODO: Implement changeHotelRoomNumberBeds method
        pass

    def changeHotelRoomCategory(self, Classes_category, Classes_roomID):
        # TODO: Implement changeHotelRoomCategory method
        pass

    def changeBookableDescription(self, Classes_bookableID, Classes_description):
        # TODO: Implement changeBookableDescription method
        pass

    def addHotelRoom(self, Classes_nbrBeds, Classes_roomNumber, Classes_description, Classes_locationInfo, Classes_floor, Classes_category, Classes_basePrice) :
        # TODO: Implement addHotelRoom method
        pass

    def addConferenceRoom(self, Classes_category, Classes_description, Classes_floor, Classes_basePrice, Classes_locationInfo, Classes_roomNumber, Classes_capacity) :
        # TODO: Implement addConferenceRoom method
        pass

    def deleteBookable(self, Classes_bookableID):
        # TODO: Implement deleteBookable method
        pass

    def changeConferenceRoomCategory(self, Classes_roomID, Classes_category):
        # TODO: Implement changeConferenceRoomCategory method
        pass

class Room:

    pass
class Classes_Bookables_ConferenceRoom(Room):

    def __init__(self, category: str, capacity: str):
        self.category = category
        self.capacity = capacity
        
        pass
    @property
    def capacity(self):
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


class Classes_Bookables_HotelRoom(Room):

    def __init__(self, category: str, nbrBeds: str):
        self.category = category
        self.nbrBeds = nbrBeds
        
        pass
    @property
    def nbrBeds(self):
        return self.__nbrBeds

    @nbrBeds.setter
    def nbrBeds(self, nbrBeds: str):
        self.__nbrBeds = nbrBeds


    @property
    def category(self):
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category


class HotelRoom:

    pass
class Classes_Bookables_Bookable(ABC):

    def __init__(self, id: str, description: str, baseprice: float):
        self.id = id
        self.description = description
        self.baseprice = baseprice
        
        pass
    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def baseprice(self):
        return self.__baseprice

    @baseprice.setter
    def baseprice(self, baseprice: float):
        self.__baseprice = baseprice


class Classes_Bookables_RoomLocation:

    def __init__(self, floor: str, addtionalInfo: str):
        self.floor = floor
        self.addtionalInfo = addtionalInfo
        
        pass
    @property
    def addtionalInfo(self):
        return self.__addtionalInfo

    @addtionalInfo.setter
    def addtionalInfo(self, addtionalInfo: str):
        self.__addtionalInfo = addtionalInfo


    @property
    def floor(self):
        return self.__floor

    @floor.setter
    def floor(self, floor: str):
        self.__floor = floor


class RoomLocation:

    pass
class Bookable:

    pass
class Classes_Bookables_HostelBed(Bookable):

    pass
class Classes_Bookables_Room(Bookable):

    pass