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
        
    @property
    def isResolved(self) -> str:
        return self.__isResolved

    @isResolved.setter
    def isResolved(self, isResolved: str):
        self.__isResolved = isResolved

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

class Request:

    pass
class IRequests:

    pass
class Classes_Requests_RequestsManager(IRequests):

    pass
class Classes_Requests_IRequests(ABC):

    def __init__(self):
        
    def createRequest(self, description: str):
        # TODO: Implement createRequest method
        pass

    def addRequest(self, description: str, specialRequestId: str):
        # TODO: Implement addRequest method
        pass

    def setRequestDescription(self, description: str, specialRequestId: str):
        # TODO: Implement setRequestDescription method
        pass

    def changeRequestDesc(self, specialRequestId: str, description: str):
        # TODO: Implement changeRequestDesc method
        pass

    def hasRequestBeenResolved(self, specialRequestId: str) -> str:
        # TODO: Implement hasRequestBeenResolved method
        pass

    def getAllRequestIDs(self) -> str:
        # TODO: Implement getAllRequestIDs method
        pass

    def getRequestDescription(self, specialRequestId: str) -> str:
        # TODO: Implement getRequestDescription method
        pass

    def searchRequests(self, keyword: str) -> str:
        # TODO: Implement searchRequests method
        pass

    def deleteRequest(self, specialRequestId: str):
        # TODO: Implement deleteRequest method
        pass

    def setRequestResolved(self, SpecialRequestId: str):
        # TODO: Implement setRequestResolved method
        pass

class Classes_Feedback_Feedback:

    def __init__(self, description: str, isNoted: str, isResolved: str, id: str):
        self.description = description
        self.isNoted = isNoted
        self.isResolved = isResolved
        self.id = id
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def isResolved(self) -> str:
        return self.__isResolved

    @isResolved.setter
    def isResolved(self, isResolved: str):
        self.__isResolved = isResolved

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isNoted(self) -> str:
        return self.__isNoted

    @isNoted.setter
    def isNoted(self, isNoted: str):
        self.__isNoted = isNoted

class Feedback:

    pass
class IFeedback:

    pass
class Classes_Feedback_FeedbackManager(IFeedback):

    pass
class Classes_Restaurants_RestaurantTable:

    def __init__(self, tableNumber: str, numberOfSeats: str):
        self.tableNumber = tableNumber
        self.numberOfSeats = numberOfSeats
        
    @property
    def numberOfSeats(self) -> str:
        return self.__numberOfSeats

    @numberOfSeats.setter
    def numberOfSeats(self, numberOfSeats: str):
        self.__numberOfSeats = numberOfSeats

    @property
    def tableNumber(self) -> str:
        return self.__tableNumber

    @tableNumber.setter
    def tableNumber(self, tableNumber: str):
        self.__tableNumber = tableNumber

class Classes_Feedback_IFeedback(ABC):

    def __init__(self):
        
    def setFeedbackDescription(self, desc: str, id: str):
        # TODO: Implement setFeedbackDescription method
        pass

    def setFeedbackIsNoted(self, id: str, status: str):
        # TODO: Implement setFeedbackIsNoted method
        pass

    def getFeedbackIsResolved(self, id: str) -> str:
        # TODO: Implement getFeedbackIsResolved method
        pass

    def getFeedbackDescription(self, id: str) -> str:
        # TODO: Implement getFeedbackDescription method
        pass

    def setFeedbackIsResolved(self, id: str, status: str):
        # TODO: Implement setFeedbackIsResolved method
        pass

    def getFeedbackIsNoted(self, id: str) -> str:
        # TODO: Implement getFeedbackIsNoted method
        pass

    def searchFeedback(self, keyword: str) -> str:
        # TODO: Implement searchFeedback method
        pass

    def getAllFeedbackIDs(self) -> str:
        # TODO: Implement getAllFeedbackIDs method
        pass

    def addFeedback(self, desc: str):
        # TODO: Implement addFeedback method
        pass

class Classes_Restaurants_RestaurantMenu:

    def __init__(self, name: str, items: str):
        self.name = name
        self.items = items
        
    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def addItem(self, itemID: str):
        # TODO: Implement addItem method
        pass

    def removeItem(self, itemID: str):
        # TODO: Implement removeItem method
        pass

class Classes_Restaurants_Reservation:

    def __init__(self, id: str, reservedBy: str, from: date, to: date, Classes_Restaurants_Reservation: set["RestaurantTable"] = None):
        self.id = id
        self.reservedBy = reservedBy
        self.from = from
        self.to = to
        self.Classes_Restaurants_Reservation = Classes_Restaurants_Reservation if Classes_Restaurants_Reservation is not None else set()
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def to(self) -> date:
        return self.__to

    @to.setter
    def to(self, to: date):
        self.__to = to

    @property
    def from(self) -> date:
        return self.__from

    @from.setter
    def from(self, from: date):
        self.__from = from

    @property
    def reservedBy(self) -> str:
        return self.__reservedBy

    @reservedBy.setter
    def reservedBy(self, reservedBy: str):
        self.__reservedBy = reservedBy

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
        
    @property
    def name(self) -> str:
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

    def addReservation(self):
        # TODO: Implement addReservation method
        pass

    def getReservation(self, reservationID: str):
        # TODO: Implement getReservation method
        pass

class Restaurant:

    pass
class IRestaurantsManage:

    pass
class Classes_Restaurants_RestaurantsManager(IRestaurantsManage):

    pass
class Classes_Restaurants_IRestaurantsAccess(ABC):

    def __init__(self):
        
    def getRestaurantTables(self, restaurantID: str) -> str:
        # TODO: Implement getRestaurantTables method
        pass

    def changeReservedTables(self, tables: str, reservationID: str, restaurantID: str):
        # TODO: Implement changeReservedTables method
        pass

    def searchRestaurantTables(self, restaurantID: str, keyword: str) -> str:
        # TODO: Implement searchRestaurantTables method
        pass

    def getAvailableTables(self, to: date, restaurantID: str, from: date) -> str:
        # TODO: Implement getAvailableTables method
        pass

    def getRestaurantMenuItems(self, restaurantID: str) -> str:
        # TODO: Implement getRestaurantMenuItems method
        pass

    def getReservationGuest(self, restaurantID: str, reservationID: str) -> str:
        # TODO: Implement getReservationGuest method
        pass

    def searchRestaurantReservationsWithTime(self, keyword: str, restaurantID: str, from: date, to: date) -> str:
        # TODO: Implement searchRestaurantReservationsWithTime method
        pass

    def getReservationToTime(self, restaurantID: str, reservationID: str) -> date:
        # TODO: Implement getReservationToTime method
        pass

    def getRestaurantReservations(self, restaurantID: str) -> str:
        # TODO: Implement getRestaurantReservations method
        pass

    def getAvailableTablesByNbrGuests(self, from: date, nbrGuests: str, restaurantID: str, to: date) -> str:
        # TODO: Implement getAvailableTablesByNbrGuests method
        pass

    def cancelReservation(self, reservationID: str, restaurantID: str):
        # TODO: Implement cancelReservation method
        pass

    def makeReservation(self, from: date, guestID: str, restaurantID: str, to: date, tables: str):
        # TODO: Implement makeReservation method
        pass

    def getAllRestaurantNames(self) -> str:
        # TODO: Implement getAllRestaurantNames method
        pass

    def getRestaurantMenuName(self, restaurantID: str) -> str:
        # TODO: Implement getRestaurantMenuName method
        pass

    def getRestaurantTableNumberOfSeats(self, restaurantID: str, tableNbr: str) -> str:
        # TODO: Implement getRestaurantTableNumberOfSeats method
        pass

    def getReservationFromTime(self, restaurantID: str, reservationID: str) -> date:
        # TODO: Implement getReservationFromTime method
        pass

    def searchRestaurants(self, keyword: str) -> str:
        # TODO: Implement searchRestaurants method
        pass

    def searchRestaurantReservations(self, keyword: str, restaurantID: str) -> str:
        # TODO: Implement searchRestaurantReservations method
        pass

class IRestaurantsAccess:

    pass
class Classes_Restaurants_IRestaurantsManage(IRestaurantsAccess):

    def __init__(self):
        
    def removeRestaurant(self, restaurantID: str):
        # TODO: Implement removeRestaurant method
        pass

    def addMenuItem(self, itemID: str, restaurantID: str):
        # TODO: Implement addMenuItem method
        pass

    def addRestaurant(self, name: str):
        # TODO: Implement addRestaurant method
        pass

    def changeTableNumber(self, newTableNbr: str, restaurantID: str, oldTableNbr: str):
        # TODO: Implement changeTableNumber method
        pass

    def removeMenuItem(self, restaurantID: str, itemID: str):
        # TODO: Implement removeMenuItem method
        pass

    def changeTableNumberOfSeats(self, nbrSeats: str, restaurantID: str, tableNbr: str):
        # TODO: Implement changeTableNumberOfSeats method
        pass

    def removeRestaurantTable(self, tableNbr: str, restaurantID: str):
        # TODO: Implement removeRestaurantTable method
        pass

    def changeMenuName(self, restaurantID: str, name: str):
        # TODO: Implement changeMenuName method
        pass

    def addRestaurantTable(self, tableNbr: str, nbrSeats: str, restaurantID: str):
        # TODO: Implement addRestaurantTable method
        pass

    def changeRestaurantName(self, name: str, restaurantID: str):
        # TODO: Implement changeRestaurantName method
        pass

class Classes_Staff_IStaff(ABC):

    def __init__(self):
        
    def changeStaffLastName(self, SSID: str, lastName: str):
        # TODO: Implement changeStaffLastName method
        pass

    def changeStaffFirstName(self, firstName: str, SSID: str):
        # TODO: Implement changeStaffFirstName method
        pass

    def getAllStaff(self) -> str:
        # TODO: Implement getAllStaff method
        pass

    def getStaffFirstName(self, SSID: str) -> str:
        # TODO: Implement getStaffFirstName method
        pass

    def scheduleStaff(self, to: date, from: date) -> str:
        # TODO: Implement scheduleStaff method
        pass

    def searchStaff(self, keyword: str) -> str:
        # TODO: Implement searchStaff method
        pass

    def getStaffLastName(self, SSID: str) -> str:
        # TODO: Implement getStaffLastName method
        pass

    def getStaffSalary(self, SSID: str) -> str:
        # TODO: Implement getStaffSalary method
        pass

    def changeStaffJob(self, SSID: str, job: str):
        # TODO: Implement changeStaffJob method
        pass

    def changeStaffSalaryContract(self, salaryContract: str, SSID: str):
        # TODO: Implement changeStaffSalaryContract method
        pass

    def getStaffSalaryContractType(self, SSID: str) -> str:
        # TODO: Implement getStaffSalaryContractType method
        pass

    def addEmployee(self, phone: str, email: str, salaryContractType: str, lastname: str, salary: float, SSID: str, firstname: str, job: str):
        # TODO: Implement addEmployee method
        pass

    def getStaffPhone(self, SSID: str) -> str:
        # TODO: Implement getStaffPhone method
        pass

    def getStaffEmail(self, SSID: str) -> str:
        # TODO: Implement getStaffEmail method
        pass

    def changeStaffPhone(self, phoneNumber: str, SSID: str):
        # TODO: Implement changeStaffPhone method
        pass

    def getStaffJob(self, SSID: str) -> str:
        # TODO: Implement getStaffJob method
        pass

class Classes_Staff_SalaryContract(ABC):

    def __init__(self):
        
    def getSalary(self) -> float:
        # TODO: Implement getSalary method
        pass

    def getType(self) -> str:
        # TODO: Implement getType method
        pass

    def setSalary(self, salary: float):
        # TODO: Implement setSalary method
        pass

class SalaryContract:

    pass
class Classes_Staff_HourlySalaryContract(SalaryContract):

    def __init__(self, salary: float, SalaryContract: "Classes_Staff_Staff"):
        self.salary = salary
        
    @property
    def salary(self) -> float:
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
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def ssid(self) -> str:
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid

    @property
    def job(self) -> str:
        return self.__job

    @job.setter
    def job(self, job: str):
        self.__job = job

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

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
class IStaff:

    pass
class Classes_Staff_StaffManager(IStaff):

    pass
class IStatisticsGenerator:

    pass
class Classes_Statistics_StatisticsGenerator(IStatisticsGenerator):

    def __init__(self, staticExpenses: float, Classes_Statistics_StatisticsGenerator: "IBills" = None, Classes_Statistics_StatisticsGenerator67: "IBookings" = None, Classes_Statistics_StatisticsGenerator69: "IStaff" = None, IStatisticsGenerator: "Classes_Staff_StaffManager"):
        self.staticExpenses = staticExpenses
        self.Classes_Statistics_StatisticsGenerator = Classes_Statistics_StatisticsGenerator
        self.Classes_Statistics_StatisticsGenerator67 = Classes_Statistics_StatisticsGenerator67
        self.Classes_Statistics_StatisticsGenerator69 = Classes_Statistics_StatisticsGenerator69
        
    @property
    def staticExpenses(self) -> float:
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

class Classes_Staff_MonthlySalaryContract(SalaryContract):

    def __init__(self, salary: float, SalaryContract: "Classes_Staff_Staff"):
        self.salary = salary
        
    @property
    def salary(self) -> float:
        return self.__salary

    @salary.setter
    def salary(self, salary: float):
        self.__salary = salary

class Classes_Statistics_IStatisticsGenerator(ABC):

    def __init__(self):
        
    def getRevenueStatistics(self, from: date, to: date) -> str:
        # TODO: Implement getRevenueStatistics method
        pass

    def getProfitStatistics(self, from: date, to: date) -> str:
        # TODO: Implement getProfitStatistics method
        pass

    def getOccupancyStatistics(self, to: date, from: date) -> str:
        # TODO: Implement getOccupancyStatistics method
        pass

class Classes_Statistics_Date:

    pass
class Classes_Statistics_StatisticEntry:

    def __init__(self, value: str, Classes_Statistics_StatisticEntry: "Date" = None):
        self.value = value
        self.Classes_Statistics_StatisticEntry = Classes_Statistics_StatisticEntry
        
    @property
    def value(self) -> str:
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
        
    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

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
                    

class Classes_Customers_ICustomers(ABC):

    def __init__(self):
        
    def changeCustomerLastName(self, lastName: str, SSID: str):
        # TODO: Implement changeCustomerLastName method
        pass

    def getCustomerFirstName(self, SSID: str) -> str:
        # TODO: Implement getCustomerFirstName method
        pass

    def getCustomerPhone(self, SSID: str) -> str:
        # TODO: Implement getCustomerPhone method
        pass

    def getCustomerRequests(self, SSID: str) -> str:
        # TODO: Implement getCustomerRequests method
        pass

    def getCustomerTitle(self, SSID: str) -> str:
        # TODO: Implement getCustomerTitle method
        pass

    def addCustomerRequest(self, description: str, SSID: str):
        # TODO: Implement addCustomerRequest method
        pass

    def changeCustomerTitle(self, SSID: str, title: str):
        # TODO: Implement changeCustomerTitle method
        pass

    def searchCustomers(self, keyword: str) -> str:
        # TODO: Implement searchCustomers method
        pass

    def getAllCustomers(self) -> str:
        # TODO: Implement getAllCustomers method
        pass

    def changeCustomerFirstName(self, SSID: str, firstName: str):
        # TODO: Implement changeCustomerFirstName method
        pass

    def getCustomerLastName(self, SSID: str) -> str:
        # TODO: Implement getCustomerLastName method
        pass

    def removeCustomerRequest(self, SSID: str, requestID: str):
        # TODO: Implement removeCustomerRequest method
        pass

    def addCustomerBooking(self, bookingID: str, SSID: str):
        # TODO: Implement addCustomerBooking method
        pass

    def removeCustomerBooking(self, SSID: str, bookingID: str):
        # TODO: Implement removeCustomerBooking method
        pass

    def changeCustomerPhone(self, phoneNr: str, SSID: str):
        # TODO: Implement changeCustomerPhone method
        pass

    def getCustomerBookings(self, SSID: str) -> str:
        # TODO: Implement getCustomerBookings method
        pass

    def addCustomer(self, email: str, lastname: str, SSID: str, firstname: str, phone: str, title: str):
        # TODO: Implement addCustomer method
        pass

    def getCustomerEmail(self, SSID: str) -> str:
        # TODO: Implement getCustomerEmail method
        pass

    def changeCustomerEmail(self, SSID: str, eMail: str):
        # TODO: Implement changeCustomerEmail method
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
        
    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def requests(self) -> str:
        return self.__requests

    @requests.setter
    def requests(self, requests: str):
        self.__requests = requests

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def bookings(self) -> str:
        return self.__bookings

    @bookings.setter
    def bookings(self, bookings: str):
        self.__bookings = bookings

    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def ssid(self) -> str:
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

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
class Classes_Bookings_IBookings(ABC):

    def __init__(self):
        
    def removeBookingRequest(self, bookingID: str, requestID: str):
        # TODO: Implement removeBookingRequest method
        pass

    def getAllBookingsWithinPeriod(self, from: date, to: date) -> str:
        # TODO: Implement getAllBookingsWithinPeriod method
        pass

    def payBookingBills(self, bookingID: str):
        # TODO: Implement payBookingBills method
        pass

    def getNbrGuestOfBooking(self, bookingID: str) -> str:
        # TODO: Implement getNbrGuestOfBooking method
        pass

    def makeBooking(self, ccv: str, expiryYear: int, guests: str, firstName: str, requests: str, expiryMonth: int, ccNumber: str, bookables: str, customerID: str, lastName: str):
        # TODO: Implement makeBooking method
        pass

    def getAvailableConferenceRoomsInPeriod(self, from: date, to: date) -> str:
        # TODO: Implement getAvailableConferenceRoomsInPeriod method
        pass

    def searchForAvailableConferenceRoomsInPeriod(self, keyword: str, from: date, to: date) -> str:
        # TODO: Implement searchForAvailableConferenceRoomsInPeriod method
        pass

    def getCustomerOfBooking(self, bookingID: str) -> str:
        # TODO: Implement getCustomerOfBooking method
        pass

    def cancelBooking(self, bookingID: str):
        # TODO: Implement cancelBooking method
        pass

    def searchBookingsWithStaysInPeriod(self, to: date, from: date, keyword: str) -> str:
        # TODO: Implement searchBookingsWithStaysInPeriod method
        pass

    def getAvailableHostelBedsInPeriod(self, from: date, to: date) -> str:
        # TODO: Implement getAvailableHostelBedsInPeriod method
        pass

    def cancelStayOfBooking(self, bookingID: str, stayID: str):
        # TODO: Implement cancelStayOfBooking method
        pass

    def getAllBookings(self) -> str:
        # TODO: Implement getAllBookings method
        pass

    def addBookedStayToBooking(self, stayID: str, bookingID: str):
        # TODO: Implement addBookedStayToBooking method
        pass

    def searchBookingsMadeInPeriod(self, keyword: str, to: date, from: date) -> str:
        # TODO: Implement searchBookingsMadeInPeriod method
        pass

    def getBookingRequests(self, bookingID: str) -> str:
        # TODO: Implement getBookingRequests method
        pass

    def getAvailableHotelRoomsInPeriod(self, to: date, from: date) -> str:
        # TODO: Implement getAvailableHotelRoomsInPeriod method
        pass

    def searchForAvailableHostelBedsInPeriod(self, to: date, keyword: str, from: date) -> str:
        # TODO: Implement searchForAvailableHostelBedsInPeriod method
        pass

    def getAvailableBookablesInPeriod(self, to: date, from: date) -> str:
        # TODO: Implement getAvailableBookablesInPeriod method
        pass

    def addBookingRequest(self, bookingID: str, requestID: str):
        # TODO: Implement addBookingRequest method
        pass

    def getAllBookingsWithStaysInPeriod(self, to: date, from: date) -> str:
        # TODO: Implement getAllBookingsWithStaysInPeriod method
        pass

    def searchForAvailableHotelRoomsInPeriod(self, keyword: str, to: date, from: date) -> str:
        # TODO: Implement searchForAvailableHotelRoomsInPeriod method
        pass

    def changeNbrGuestsOfBooking(self, bookingID: str, nbrGuests: str):
        # TODO: Implement changeNbrGuestsOfBooking method
        pass

    def payStayBills(self, stayID: str, bookingID: str):
        # TODO: Implement payStayBills method
        pass

    def searchBookings(self, keyword: str) -> str:
        # TODO: Implement searchBookings method
        pass

    def getBookedStaysOfBooking(self, bookingID: str) -> str:
        # TODO: Implement getBookedStaysOfBooking method
        pass

    def searchForAvailableBookablesInPeriod(self, to: date, keyword: str, from: date) -> str:
        # TODO: Implement searchForAvailableBookablesInPeriod method
        pass

class ICustomers:

    pass
class Classes_Customers_CustomersManager(ICustomers):

    pass
class Booking:

    pass
class IBookings:

    pass
class Classes_Bookings_BookingsManager(IBookings):

    pass
class Classes_Bookings_Booking:

    def __init__(self, customer: str, bookedStays: str, bookingNbr: str, nbrGuests: str, issueDate: date, requests: str, Classes_Bookings_Booking: "CreditCard" = None):
        self.customer = customer
        self.bookedStays = bookedStays
        self.bookingNbr = bookingNbr
        self.nbrGuests = nbrGuests
        self.issueDate = issueDate
        self.requests = requests
        self.Classes_Bookings_Booking = Classes_Bookings_Booking
        
    @property
    def bookedStays(self) -> str:
        return self.__bookedStays

    @bookedStays.setter
    def bookedStays(self, bookedStays: str):
        self.__bookedStays = bookedStays

    @property
    def issueDate(self) -> date:
        return self.__issueDate

    @issueDate.setter
    def issueDate(self, issueDate: date):
        self.__issueDate = issueDate

    @property
    def bookingNbr(self) -> str:
        return self.__bookingNbr

    @bookingNbr.setter
    def bookingNbr(self, bookingNbr: str):
        self.__bookingNbr = bookingNbr

    @property
    def customer(self) -> str:
        return self.__customer

    @customer.setter
    def customer(self, customer: str):
        self.__customer = customer

    @property
    def requests(self) -> str:
        return self.__requests

    @requests.setter
    def requests(self, requests: str):
        self.__requests = requests

    @property
    def nbrGuests(self) -> str:
        return self.__nbrGuests

    @nbrGuests.setter
    def nbrGuests(self, nbrGuests: str):
        self.__nbrGuests = nbrGuests

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

    def removeRequest(self, requestID: str):
        # TODO: Implement removeRequest method
        pass

    def addBookedStay(self, stayID: str):
        # TODO: Implement addBookedStay method
        pass

    def cancelBookedStay(self, stayID: str):
        # TODO: Implement cancelBookedStay method
        pass

    def addRequest(self, requestID: str):
        # TODO: Implement addRequest method
        pass

class Classes_Accounts_IManageAccounts(ABC):

    def __init__(self):
        
    def addAccount(self, password: str, type: str, username: str):
        # TODO: Implement addAccount method
        pass

    def renameAccount(self, oldUsername: str, newUsername: str):
        # TODO: Implement renameAccount method
        pass

    def searchAccounts(self, keyword: str) -> str:
        # TODO: Implement searchAccounts method
        pass

    def changePassword(self, username: str, newPassword: str):
        # TODO: Implement changePassword method
        pass

    def getAccountName(self, username: str) -> str:
        # TODO: Implement getAccountName method
        pass

    def getAccountPassword(self, username: str) -> str:
        # TODO: Implement getAccountPassword method
        pass

    def deleteAccount(self, username: str):
        # TODO: Implement deleteAccount method
        pass

class Classes_Accounts_IAccountsAccess(ABC):

    def __init__(self):
        
    def validateAccount(self, password: str, username: str) -> str:
        # TODO: Implement validateAccount method
        pass

    def login(self, password: str, username: str) -> str:
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
        
    @property
    def password(self) -> str:
        return self.__password

    @password.setter
    def password(self, password: str):
        self.__password = password

    @property
    def username(self) -> str:
        return self.__username

    @username.setter
    def username(self, username: str):
        self.__username = username

    @property
    def accountType(self) -> str:
        return self.__accountType

    @accountType.setter
    def accountType(self, accountType: str):
        self.__accountType = accountType

class Classes_Guests_IGuests(ABC):

    def __init__(self):
        
    def changeGuestEmail(self, eMail: str, SSID: str):
        # TODO: Implement changeGuestEmail method
        pass

    def getGuestTitle(self, SSID: str) -> str:
        # TODO: Implement getGuestTitle method
        pass

    def getGuestFirstName(self, SSID: str) -> str:
        # TODO: Implement getGuestFirstName method
        pass

    def changeGuestLastName(self, lastName: str, SSID: str):
        # TODO: Implement changeGuestLastName method
        pass

    def changeGuestTitle(self, SSID: str, title: str):
        # TODO: Implement changeGuestTitle method
        pass

    def getGuestRequests(self, SSID: str) -> str:
        # TODO: Implement getGuestRequests method
        pass

    def changeGuestPhone(self, SSID: str, phoneNr: str):
        # TODO: Implement changeGuestPhone method
        pass

    def generateGuestAccount(self, SSID: str):
        # TODO: Implement generateGuestAccount method
        pass

    def getGuestStays(self, SSID: str) -> str:
        # TODO: Implement getGuestStays method
        pass

    def removeGuestRequest(self, requestID: str, SSID: str):
        # TODO: Implement removeGuestRequest method
        pass

    def getGuestAccountUsername(self, SSID: str) -> str:
        # TODO: Implement getGuestAccountUsername method
        pass

    def getGuestLastName(self, SSID: str) -> str:
        # TODO: Implement getGuestLastName method
        pass

    def getGuestAccountPassword(self, SSID: str) -> str:
        # TODO: Implement getGuestAccountPassword method
        pass

    def removeGuestStay(self, SSID: str, stayID: str):
        # TODO: Implement removeGuestStay method
        pass

    def changeGuestFirstName(self, SSID: str, firstName: str):
        # TODO: Implement changeGuestFirstName method
        pass

    def removeGuestAccount(self, SSID: str):
        # TODO: Implement removeGuestAccount method
        pass

    def getAllGuestIDs(self) -> str:
        # TODO: Implement getAllGuestIDs method
        pass

    def addGuest(self, title: str, phone: str, firstname: str, SSID: str, lastname: str, email: str):
        # TODO: Implement addGuest method
        pass

    def getGuestEmail(self, SSID: str) -> str:
        # TODO: Implement getGuestEmail method
        pass

    def addGuestRequest(self, SSID: str, desctiption: str, requestID: str):
        # TODO: Implement addGuestRequest method
        pass

    def getGuestPhone(self, SSID: str) -> str:
        # TODO: Implement getGuestPhone method
        pass

    def searchGuests(self, keyword: str) -> str:
        # TODO: Implement searchGuests method
        pass

class Classes_Guests_Guest:

    def __init__(self, firstname: str, lastname: str, title: str, email: str, phone: str, ssid: str, requests: str, stays: str, account: str):
        self.firstname = firstname
        self.lastname = lastname
        self.title = title
        self.email = email
        self.phone = phone
        self.ssid = ssid
        self.requests = requests
        self.stays = stays
        self.account = account
        
    @property
    def email(self) -> str:
        return self.__email

    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def title(self) -> str:
        return self.__title

    @title.setter
    def title(self, title: str):
        self.__title = title

    @property
    def ssid(self) -> str:
        return self.__ssid

    @ssid.setter
    def ssid(self, ssid: str):
        self.__ssid = ssid

    @property
    def requests(self) -> str:
        return self.__requests

    @requests.setter
    def requests(self, requests: str):
        self.__requests = requests

    @property
    def firstname(self) -> str:
        return self.__firstname

    @firstname.setter
    def firstname(self, firstname: str):
        self.__firstname = firstname

    @property
    def phone(self) -> str:
        return self.__phone

    @phone.setter
    def phone(self, phone: str):
        self.__phone = phone

    @property
    def lastname(self) -> str:
        return self.__lastname

    @lastname.setter
    def lastname(self, lastname: str):
        self.__lastname = lastname

    @property
    def stays(self) -> str:
        return self.__stays

    @stays.setter
    def stays(self, stays: str):
        self.__stays = stays

    @property
    def account(self) -> str:
        return self.__account

    @account.setter
    def account(self, account: str):
        self.__account = account

    def addRequest(self, requestID: str, description: str):
        # TODO: Implement addRequest method
        pass

    def removeRequest(self, requestID: str):
        # TODO: Implement removeRequest method
        pass

    def removeStay(self, stayID: str):
        # TODO: Implement removeStay method
        pass

    def addStay(self, bookingID: str, bookableID: str, fromDate: date, toDate: date):
        # TODO: Implement addStay method
        pass

class IManageAccounts:

    pass
class Guest:

    pass
class Classes_Services_IServicesAccess(ABC):

    def __init__(self):
        
    def getRoomServiceMenuName(self) -> str:
        # TODO: Implement getRoomServiceMenuName method
        pass

    def setRSOBill(self, billID: str, orderID: str):
        # TODO: Implement setRSOBill method
        pass

    def makeRoomServiceOrder(self, services: str, isDelivered: str, bill: str, bookable: str, deliveryDate: date, items: str):
        # TODO: Implement makeRoomServiceOrder method
        pass

    def getRoomServiceMenuItems(self) -> str:
        # TODO: Implement getRoomServiceMenuItems method
        pass

    def changeRSODeliveryDate(self, date: date, orderID: str):
        # TODO: Implement changeRSODeliveryDate method
        pass

    def getAllServiceIDs(self) -> str:
        # TODO: Implement getAllServiceIDs method
        pass

    def changeRSOISDelivered(self, isDelivered: str, orderID: str):
        # TODO: Implement changeRSOISDelivered method
        pass

    def getRSOItems(self, orderID: str) -> str:
        # TODO: Implement getRSOItems method
        pass

    def getRSOBookable(self, orderID: str) -> str:
        # TODO: Implement getRSOBookable method
        pass

    def isRSODelivered(self, orderID: str) -> str:
        # TODO: Implement isRSODelivered method
        pass

    def getRSOServices(self, orderID: str) -> str:
        # TODO: Implement getRSOServices method
        pass

    def getRSOBill(self, orderID: str) -> str:
        # TODO: Implement getRSOBill method
        pass

    def getServicePrice(self, serviceID: str) -> float:
        # TODO: Implement getServicePrice method
        pass

    def getServiceName(self, serviceID: str) -> str:
        # TODO: Implement getServiceName method
        pass

    def searchServices(self, keyword: str) -> str:
        # TODO: Implement searchServices method
        pass

    def getServiceExpense(self, serviceID: str) -> float:
        # TODO: Implement getServiceExpense method
        pass

    def searchRoomServiceOrders(self, keyword: str) -> str:
        # TODO: Implement searchRoomServiceOrders method
        pass

    def getRSODeliveryDate(self, orderID: str) -> date:
        # TODO: Implement getRSODeliveryDate method
        pass

    def getAllRoomServiceOrderIDs(self) -> str:
        # TODO: Implement getAllRoomServiceOrderIDs method
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
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def isDelivered(self) -> str:
        return self.__isDelivered

    @isDelivered.setter
    def isDelivered(self, isDelivered: str):
        self.__isDelivered = isDelivered

    @property
    def bill(self) -> str:
        return self.__bill

    @bill.setter
    def bill(self, bill: str):
        self.__bill = bill

    @property
    def deliveryDate(self) -> date:
        return self.__deliveryDate

    @deliveryDate.setter
    def deliveryDate(self, deliveryDate: date):
        self.__deliveryDate = deliveryDate

    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

    @property
    def bookable(self) -> str:
        return self.__bookable

    @bookable.setter
    def bookable(self, bookable: str):
        self.__bookable = bookable

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
                    

    def addItem(self):
        # TODO: Implement addItem method
        pass

    def removeService(self):
        # TODO: Implement removeService method
        pass

    def removeItem(self):
        # TODO: Implement removeItem method
        pass

    def addService(self):
        # TODO: Implement addService method
        pass

class Classes_Services_Service:

    def __init__(self, name: str, price: float, expense: float, id: str):
        self.name = name
        self.price = price
        self.expense = expense
        self.id = id
        
    @property
    def expense(self) -> float:
        return self.__expense

    @expense.setter
    def expense(self, expense: float):
        self.__expense = expense

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

class RoomServiceMenu:

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
        
    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    def addItem(self, itemID: str):
        # TODO: Implement addItem method
        pass

    def removeItem(self, itemID: str):
        # TODO: Implement removeItem method
        pass

class Classes_Inventory_IInventoryAccess(ABC):

    def __init__(self):
        
    def searchItems(self, keyword: str) -> str:
        # TODO: Implement searchItems method
        pass

    def getItemName(self, id: str) -> str:
        # TODO: Implement getItemName method
        pass

    def getItemStock(self, id: str) -> str:
        # TODO: Implement getItemStock method
        pass

    def getItemPrice(self, id: str) -> float:
        # TODO: Implement getItemPrice method
        pass

    def getAllItemIDs(self) -> str:
        # TODO: Implement getAllItemIDs method
        pass

    def getItemExpense(self, id: str) -> float:
        # TODO: Implement getItemExpense method
        pass

    def changeItemStock(self, stock: str, id: str):
        # TODO: Implement changeItemStock method
        pass

class Classes_Inventory_Item:

    def __init__(self, name: str, price: float, expense: float, stock: str, id: str):
        self.name = name
        self.price = price
        self.expense = expense
        self.stock = stock
        self.id = id
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def price(self) -> float:
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def expense(self) -> float:
        return self.__expense

    @expense.setter
    def expense(self, expense: float):
        self.__expense = expense

    @property
    def stock(self) -> str:
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
class Classes_Bills_IBills(ABC):

    def __init__(self):
        
    def getBillPaymentType(self, billID: str) -> str:
        # TODO: Implement getBillPaymentType method
        pass

    def getAllBillIDs(self) -> str:
        # TODO: Implement getAllBillIDs method
        pass

    def getAllPayedBills(self) -> str:
        # TODO: Implement getAllPayedBills method
        pass

    def getBillPaymentDate(self, billID: str) -> date:
        # TODO: Implement getBillPaymentDate method
        pass

    def getIsBillPaid(self, billID: str) -> str:
        # TODO: Implement getIsBillPaid method
        pass

    def getAllBillsNotPaid(self) -> str:
        # TODO: Implement getAllBillsNotPaid method
        pass

    def removeBill(self, billID: str):
        # TODO: Implement removeBill method
        pass

    def getBillServices(self, billID: str) -> str:
        # TODO: Implement getBillServices method
        pass

    def searchBills(self, keyword: str) -> str:
        # TODO: Implement searchBills method
        pass

    def addBill(self, bookable: str, items: str, services: str):
        # TODO: Implement addBill method
        pass

    def getBillIssueDate(self, billID: str) -> date:
        # TODO: Implement getBillIssueDate method
        pass

    def sendInvoice(self, email: str, billID: str):
        # TODO: Implement sendInvoice method
        pass

    def payBillsWithCreditCard(self, ccv: str, ccNumber: str, lastName: str, firstName: str, bills: str, expiryMonth: int, expiryYear: int):
        # TODO: Implement payBillsWithCreditCard method
        pass

    def getBillItems(self, billID: str) -> str:
        # TODO: Implement getBillItems method
        pass

    def getBillTotalAmount(self, billID: str) -> float:
        # TODO: Implement getBillTotalAmount method
        pass

    def payBillsWithCash(self, bills: str):
        # TODO: Implement payBillsWithCash method
        pass

    def getBillBookable(self, billID: str) -> str:
        # TODO: Implement getBillBookable method
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
        
    @property
    def paymentType(self) -> str:
        return self.__paymentType

    @paymentType.setter
    def paymentType(self, paymentType: str):
        self.__paymentType = paymentType

    @property
    def services(self) -> str:
        return self.__services

    @services.setter
    def services(self, services: str):
        self.__services = services

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def items(self) -> str:
        return self.__items

    @items.setter
    def items(self, items: str):
        self.__items = items

    @property
    def paymentDate(self) -> date:
        return self.__paymentDate

    @paymentDate.setter
    def paymentDate(self, paymentDate: date):
        self.__paymentDate = paymentDate

    @property
    def issueDate(self) -> date:
        return self.__issueDate

    @issueDate.setter
    def issueDate(self, issueDate: date):
        self.__issueDate = issueDate

    @property
    def totalAmount(self) -> float:
        return self.__totalAmount

    @totalAmount.setter
    def totalAmount(self, totalAmount: float):
        self.__totalAmount = totalAmount

    @property
    def isPaid(self) -> str:
        return self.__isPaid

    @isPaid.setter
    def isPaid(self, isPaid: str):
        self.__isPaid = isPaid

    @property
    def bookable(self) -> str:
        return self.__bookable

    @bookable.setter
    def bookable(self, bookable: str):
        self.__bookable = bookable

    def addService(self, serviceID: str):
        # TODO: Implement addService method
        pass

    def addItem(self, itemID: str):
        # TODO: Implement addItem method
        pass

class IServicesAccess:

    pass
class Classes_Services_IServicesManage(IServicesAccess):

    def __init__(self, IServicesAccess: "Classes_Bills_BillsManager"):
        
    def addService(self, name: str, price: float, expense: float):
        # TODO: Implement addService method
        pass

    def changeServiceName(self, serviceID: str, name: str):
        # TODO: Implement changeServiceName method
        pass

    def changeServiceExpense(self, expense: float, serviceID: str):
        # TODO: Implement changeServiceExpense method
        pass

    def removeRoomServiceMenuItem(self, itemID: str):
        # TODO: Implement removeRoomServiceMenuItem method
        pass

    def addRoomServiceMenuItem(self, itemID: str):
        # TODO: Implement addRoomServiceMenuItem method
        pass

    def changeServicePrice(self, serviceID: str, price: float):
        # TODO: Implement changeServicePrice method
        pass

    def changeRoomServiceMenuName(self, name: str):
        # TODO: Implement changeRoomServiceMenuName method
        pass

class IInventoryAccess:

    pass
class Classes_Inventory_IManageInventory(IInventoryAccess):

    def __init__(self, IInventoryAccess: "Classes_Bills_BillsManager"):
        
    def addItem(self, price: float, stock: str, expense: float, name: str):
        # TODO: Implement addItem method
        pass

    def changeItemExpense(self, expense: float, id: str):
        # TODO: Implement changeItemExpense method
        pass

    def changeItemPrice(self, price: float, id: str):
        # TODO: Implement changeItemPrice method
        pass

    def changeItemName(self, name: str, id: str):
        # TODO: Implement changeItemName method
        pass

    def removeItem(self, id: str):
        # TODO: Implement removeItem method
        pass

class Bill:

    pass
class Classes_Banking_CustomerProvides(ABC):

    def __init__(self):
        
    def makePayment(self, ccNumber: str, expiryMonth: int, lastName: str, firstName: str, ccv: str, sum: float, expiryYear: int) -> bool:
        # TODO: Implement makePayment method
        pass

    def isCreditCardValid(self, firstName: str, lastName: str, expiryMonth: int, ccNumber: str, expiryYear: int, ccv: str) -> bool:
        # TODO: Implement isCreditCardValid method
        pass

class Classes_Banking_AdministratorProvides(ABC):

    def __init__(self):
        
    def makeDeposit(self, expiryYear: int, expiryMonth: int, firstName: str, ccNumber: str, sum: float, ccv: str, lastName: str) -> float:
        # TODO: Implement makeDeposit method
        pass

    def addCreditCard(self, ccv: str, ccNumber: str, lastName: str, expiryYear: int, expiryMonth: int, firstName: str) -> bool:
        # TODO: Implement addCreditCard method
        pass

    def removeCreditCard(self, ccv: str, expiryYear: int, expiryMonth: int, ccNumber: str, lastName: str, firstName: str) -> bool:
        # TODO: Implement removeCreditCard method
        pass

    def getBalance(self, ccNumber: str, firstName: str, ccv: str, lastName: str, expiryMonth: int, expiryYear: int) -> float:
        # TODO: Implement getBalance method
        pass

class IBills:

    pass
class Classes_Bills_BillsManager(IBills):

    pass
class CustomerProvides:

    pass
class Stay:

    pass
class Classes_Stays_IStays(ABC):

    def __init__(self):
        
    def addBillToStay(self, billID: str, stayID: str):
        # TODO: Implement addBillToStay method
        pass

    def removeStay(self, stayID: str):
        # TODO: Implement removeStay method
        pass

    def searchHotelStays(self, keyword: str) -> str:
        # TODO: Implement searchHotelStays method
        pass

    def getAllUnpayedBillsOfHotelStay(self, stayID: str) -> str:
        # TODO: Implement getAllUnpayedBillsOfHotelStay method
        pass

    def checkOutGuest(self, guestID: str, stayID: str):
        # TODO: Implement checkOutGuest method
        pass

    def getAllHotelStayIDs(self) -> str:
        # TODO: Implement getAllHotelStayIDs method
        pass

    def getBillsOfHotelStay(self, stayID: str) -> str:
        # TODO: Implement getBillsOfHotelStay method
        pass

    def checkInGuest(self, guestID: str, stayID: str):
        # TODO: Implement checkInGuest method
        pass

    def addNewStay(self, bookingID: str, fromDate: date, toDate: date, bookableID: str):
        # TODO: Implement addNewStay method
        pass

    def removeBillFromStay(self, billID: str, stayID: str):
        # TODO: Implement removeBillFromStay method
        pass

    def getGuestsOfHotelStay(self, stayID: str) -> str:
        # TODO: Implement getGuestsOfHotelStay method
        pass

    def changeBookableOfStay(self, stayID: str, bookableID: str):
        # TODO: Implement changeBookableOfStay method
        pass

    def getCheckedInGuestsOfHotelStay(self, stayID: str) -> str:
        # TODO: Implement getCheckedInGuestsOfHotelStay method
        pass

    def getBookingOfHotelStay(self, stayID: str) -> str:
        # TODO: Implement getBookingOfHotelStay method
        pass

    def searchHotelStaysWithinPeriod(self, to: date, from: date, keyword: str) -> str:
        # TODO: Implement searchHotelStaysWithinPeriod method
        pass

    def addResponsibleCreditCard(self, ccv: str, stayID: str, expiryYear: int, expiryMonth: int, firstName: str, lastName: str, ccNumber: str):
        # TODO: Implement addResponsibleCreditCard method
        pass

    def getBookableOfHotelStay(self, stayID: str) -> str:
        # TODO: Implement getBookableOfHotelStay method
        pass

    def changeResponsibleCreditCard(self, stayID: str, expiryYear: int, lastName: str, ccNumber: str, expiryMonth: int, ccv: str, firstName: str):
        # TODO: Implement changeResponsibleCreditCard method
        pass

    def changePeriodOfStay(self, to: date, from: date, stayID: str):
        # TODO: Implement changePeriodOfStay method
        pass

    def billCreditCardWithAllUnpaidBillsOfHotelStay(self, stayID: str):
        # TODO: Implement billCreditCardWithAllUnpaidBillsOfHotelStay method
        pass

    def isResponsibleCreditCardAdded(self, stayID: str) -> str:
        # TODO: Implement isResponsibleCreditCardAdded method
        pass

    def getAllHotelStaysWithinPeriod(self, to: date, from: date) -> str:
        # TODO: Implement getAllHotelStaysWithinPeriod method
        pass

    def getCheckedOutGuestsOfHotelStay(self, stayID: str) -> str:
        # TODO: Implement getCheckedOutGuestsOfHotelStay method
        pass

class IGuests:

    pass
class Classes_Guests_GuestsManager(IGuests):

    pass
class Classes_Stays_Stay:

    def __init__(self, checkedInGuests: str, booking: str, checkedOutGuests: str, fromDate: date, toDate: date, ID: str, bookable: str, bills: str, Classes_Stays_Stay: "CreditCard" = None):
        self.checkedInGuests = checkedInGuests
        self.booking = booking
        self.checkedOutGuests = checkedOutGuests
        self.fromDate = fromDate
        self.toDate = toDate
        self.ID = ID
        self.bookable = bookable
        self.bills = bills
        self.Classes_Stays_Stay = Classes_Stays_Stay
        
    @property
    def bookable(self) -> str:
        return self.__bookable

    @bookable.setter
    def bookable(self, bookable: str):
        self.__bookable = bookable

    @property
    def checkedInGuests(self) -> str:
        return self.__checkedInGuests

    @checkedInGuests.setter
    def checkedInGuests(self, checkedInGuests: str):
        self.__checkedInGuests = checkedInGuests

    @property
    def bills(self) -> str:
        return self.__bills

    @bills.setter
    def bills(self, bills: str):
        self.__bills = bills

    @property
    def toDate(self) -> date:
        return self.__toDate

    @toDate.setter
    def toDate(self, toDate: date):
        self.__toDate = toDate

    @property
    def booking(self) -> str:
        return self.__booking

    @booking.setter
    def booking(self, booking: str):
        self.__booking = booking

    @property
    def checkedOutGuests(self) -> str:
        return self.__checkedOutGuests

    @checkedOutGuests.setter
    def checkedOutGuests(self, checkedOutGuests: str):
        self.__checkedOutGuests = checkedOutGuests

    @property
    def fromDate(self) -> date:
        return self.__fromDate

    @fromDate.setter
    def fromDate(self, fromDate: date):
        self.__fromDate = fromDate

    @property
    def ID(self) -> str:
        return self.__ID

    @ID.setter
    def ID(self, ID: str):
        self.__ID = ID

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

    def checkOutGuest(self):
        # TODO: Implement checkOutGuest method
        pass

    def addCheckedInGuest(self, SSID: str):
        # TODO: Implement addCheckedInGuest method
        pass

    def addBill(self, billID: str):
        # TODO: Implement addBill method
        pass

class IStays:

    pass
class Classes_Stays_StaysManager(IStays):

    pass
class Classes_Stays_CreditCard:

    def __init__(self, ccNumber: str, ccv: str, expiryMonth: str, expiryYear: str, firstName: str, lastName: str):
        self.ccNumber = ccNumber
        self.ccv = ccv
        self.expiryMonth = expiryMonth
        self.expiryYear = expiryYear
        self.firstName = firstName
        self.lastName = lastName
        
    @property
    def ccv(self) -> str:
        return self.__ccv

    @ccv.setter
    def ccv(self, ccv: str):
        self.__ccv = ccv

    @property
    def lastName(self) -> str:
        return self.__lastName

    @lastName.setter
    def lastName(self, lastName: str):
        self.__lastName = lastName

    @property
    def expiryYear(self) -> str:
        return self.__expiryYear

    @expiryYear.setter
    def expiryYear(self, expiryYear: str):
        self.__expiryYear = expiryYear

    @property
    def ccNumber(self) -> str:
        return self.__ccNumber

    @ccNumber.setter
    def ccNumber(self, ccNumber: str):
        self.__ccNumber = ccNumber

    @property
    def expiryMonth(self) -> str:
        return self.__expiryMonth

    @expiryMonth.setter
    def expiryMonth(self, expiryMonth: str):
        self.__expiryMonth = expiryMonth

    @property
    def firstName(self) -> str:
        return self.__firstName

    @firstName.setter
    def firstName(self, firstName: str):
        self.__firstName = firstName

class CreditCard:

    pass
class IBookablesManage:

    pass
class Classes_Bookables_BookablesManager(IBookablesManage):

    pass
class Classes_Bookables_IBookablesAccess(ABC):

    def __init__(self):
        
    def getBookableBasePrice(self, bookableID: str) -> float:
        # TODO: Implement getBookableBasePrice method
        pass

    def getRoomLocationFloor(self, roomID: str) -> str:
        # TODO: Implement getRoomLocationFloor method
        pass

    def getAllHostelBedIDs(self) -> str:
        # TODO: Implement getAllHostelBedIDs method
        pass

    def getAllConferenceRoomIDs(self) -> str:
        # TODO: Implement getAllConferenceRoomIDs method
        pass

    def getAllBookableIDs(self) -> str:
        # TODO: Implement getAllBookableIDs method
        pass

    def searchConferenceRooms(self, category: str, keyword: str) -> str:
        # TODO: Implement searchConferenceRooms method
        pass

    def getRoomOfHostelBed(self, hostelBedID: str) -> str:
        # TODO: Implement getRoomOfHostelBed method
        pass

    def getHotelRoomNbrBeds(self, ID: str) -> str:
        # TODO: Implement getHotelRoomNbrBeds method
        pass

    def searchForBookable(self, keyword: str) -> str:
        # TODO: Implement searchForBookable method
        pass

    def getAllHotelRoomIDs(self) -> str:
        # TODO: Implement getAllHotelRoomIDs method
        pass

    def getRoomLocationInfo(self, roomID: str) -> str:
        # TODO: Implement getRoomLocationInfo method
        pass

    def getConferenceRoomCapacity(self, roomID: str) -> str:
        # TODO: Implement getConferenceRoomCapacity method
        pass

    def getConferenceRoomCategory(self, roomID: str) -> str:
        # TODO: Implement getConferenceRoomCategory method
        pass

    def searchHotelRooms(self, category: str, keyword: str) -> str:
        # TODO: Implement searchHotelRooms method
        pass

    def getBookableDescription(self, bookableID: str) -> str:
        # TODO: Implement getBookableDescription method
        pass

    def getHotelRoomCategory(self, roomID: str) -> str:
        # TODO: Implement getHotelRoomCategory method
        pass

    def searchHostelBeds(self, keyword: str) -> str:
        # TODO: Implement searchHostelBeds method
        pass

class IBookablesAccess:

    pass
class Classes_Bookables_IBookablesManage(IBookablesAccess):

    def __init__(self, IBookablesAccess: "Classes_Bills_BillsManager", IBookablesAccess40: "Classes_Bookings_BookingsManager"):
        
    def addConferenceRoom(self, floor: str, capacity: str, description: str, roomNumber: str, basePrice: float, locationInfo: str, category: str) -> str:
        # TODO: Implement addConferenceRoom method
        pass

    def changeRoomLocation(self, floor: str, roomID: str, additionalInfo: str):
        # TODO: Implement changeRoomLocation method
        pass

    def changeHotelRoomNumberBeds(self, roomID: str, nbrBeds: str):
        # TODO: Implement changeHotelRoomNumberBeds method
        pass

    def changeHostelBedRoom(self, hostelBedID: str, roomID: str):
        # TODO: Implement changeHostelBedRoom method
        pass

    def changeConferenceRoomCapacity(self, roomID: str, capacity: str):
        # TODO: Implement changeConferenceRoomCapacity method
        pass

    def changeBookableBasePrice(self, bookableID: str, basePrice: float):
        # TODO: Implement changeBookableBasePrice method
        pass

    def changeConferenceRoomCategory(self, category: str, roomID: str):
        # TODO: Implement changeConferenceRoomCategory method
        pass

    def changeBookableDescription(self, description: str, bookableID: str):
        # TODO: Implement changeBookableDescription method
        pass

    def changeHotelRoomCategory(self, category: str, roomID: str):
        # TODO: Implement changeHotelRoomCategory method
        pass

    def addHostelBed(self, roomID: str, basePrice: float, description: str, bedNumber: str) -> str:
        # TODO: Implement addHostelBed method
        pass

    def addHotelRoom(self, nbrBeds: str, floor: str, basePrice: float, locationInfo: str, category: str, roomNumber: str, description: str) -> str:
        # TODO: Implement addHotelRoom method
        pass

    def deleteBookable(self, bookableID: str):
        # TODO: Implement deleteBookable method
        pass

class Room:

    pass
class Classes_Bookables_HotelRoom(Room):

    def __init__(self, category: str, nbrBeds: str):
        self.category = category
        self.nbrBeds = nbrBeds
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def nbrBeds(self) -> str:
        return self.__nbrBeds

    @nbrBeds.setter
    def nbrBeds(self, nbrBeds: str):
        self.__nbrBeds = nbrBeds

class HotelRoom:

    pass
class Classes_Bookables_ConferenceRoom(Room):

    def __init__(self, category: str, capacity: str):
        self.category = category
        self.capacity = capacity
        
    @property
    def category(self) -> str:
        return self.__category

    @category.setter
    def category(self, category: str):
        self.__category = category

    @property
    def capacity(self) -> str:
        return self.__capacity

    @capacity.setter
    def capacity(self, capacity: str):
        self.__capacity = capacity

class Classes_Bookables_RoomLocation:

    def __init__(self, floor: str, addtionalInfo: str):
        self.floor = floor
        self.addtionalInfo = addtionalInfo
        
    @property
    def floor(self) -> str:
        return self.__floor

    @floor.setter
    def floor(self, floor: str):
        self.__floor = floor

    @property
    def addtionalInfo(self) -> str:
        return self.__addtionalInfo

    @addtionalInfo.setter
    def addtionalInfo(self, addtionalInfo: str):
        self.__addtionalInfo = addtionalInfo

class RoomLocation:

    pass
class Bookable:

    pass
class Classes_Bookables_HostelBed(Bookable):

    pass
class Classes_Bookables_Room(Bookable):

    pass
class Classes_Bookables_Bookable(ABC):

    def __init__(self, baseprice: float, id: str, description: str):
        self.baseprice = baseprice
        self.id = id
        self.description = description
        
    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def baseprice(self) -> float:
        return self.__baseprice

    @baseprice.setter
    def baseprice(self, baseprice: float):
        self.__baseprice = baseprice
