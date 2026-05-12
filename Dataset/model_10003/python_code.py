from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class Employee:

    pass
class CoachBus_Manager(Employee):

    def __init__(self, hasMBA: bool, Manager: "CoachBus_BookingOffice" = None, manager: "CoachBus_BookingOffice" = None):
        self.hasMBA = hasMBA
        self.Manager = Manager
        self.manager = manager
        
        pass
    @property
    def hasMBA(self):
        return self.__hasMBA

    @hasMBA.setter
    def hasMBA(self, hasMBA: bool):
        self.__hasMBA = hasMBA


    @property
    def manager(self):
        return self.__manager

    @manager.setter
    def manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Manager__manager", None)
        self.__manager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BookingOffice13"):
                opp_val = getattr(old_value, "BookingOffice13", None)
                if opp_val == self:
                    setattr(old_value, "BookingOffice13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BookingOffice13"):
                opp_val = getattr(value, "BookingOffice13", None)
                setattr(value, "BookingOffice13", self)

    @property
    def Manager(self):
        return self.__Manager

    @Manager.setter
    def Manager(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Manager__Manager", None)
        self.__Manager = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "office"):
                opp_val = getattr(old_value, "office", None)
                if opp_val == self:
                    setattr(old_value, "office", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "office"):
                opp_val = getattr(value, "office", None)
                setattr(value, "office", self)

class Ticket:

    pass
class CoachBus_ChildTicket(Ticket):

    def __init__(self, isSchoolTrip: bool):
        self.isSchoolTrip = isSchoolTrip
        
        pass
    @property
    def isSchoolTrip(self):
        return self.__isSchoolTrip

    @isSchoolTrip.setter
    def isSchoolTrip(self, isSchoolTrip: bool):
        self.__isSchoolTrip = isSchoolTrip


class CoachBus_AdultTicket(Ticket):

    def __init__(self, isElderlyDiscount: bool):
        self.isElderlyDiscount = isElderlyDiscount
        
        pass
    @property
    def isElderlyDiscount(self):
        return self.__isElderlyDiscount

    @isElderlyDiscount.setter
    def isElderlyDiscount(self, isElderlyDiscount: bool):
        self.__isElderlyDiscount = isElderlyDiscount


class CoachBus_VendingMachine:

    def __init__(self, number: int, VendingMachine: "CoachBus_BookingOffice" = None, VendingMachine23: "CoachBus_Ticket" = None, vm: set["CoachBus_Ticket"] = None, vms: "CoachBus_BookingOffice" = None):
        self.number = number
        self.VendingMachine = VendingMachine
        self.VendingMachine23 = VendingMachine23
        self.vm = vm if vm is not None else set()
        self.vms = vms
        
        pass
    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


    @property
    def vm(self):
        return self.__vm

    @vm.setter
    def vm(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_VendingMachine__vm", None)
        self.__vm = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ticket25"):
                    opp_val = getattr(item, "Ticket25", None)
                    
                    if opp_val == self:
                        setattr(item, "Ticket25", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ticket25"):
                    opp_val = getattr(item, "Ticket25", None)
                    
                    setattr(item, "Ticket25", self)
                    

    @property
    def VendingMachine23(self):
        return self.__VendingMachine23

    @VendingMachine23.setter
    def VendingMachine23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_VendingMachine__VendingMachine23", None)
        self.__VendingMachine23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tickets22"):
                opp_val = getattr(old_value, "tickets22", None)
                if opp_val == self:
                    setattr(old_value, "tickets22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tickets22"):
                opp_val = getattr(value, "tickets22", None)
                setattr(value, "tickets22", self)

    @property
    def VendingMachine(self):
        return self.__VendingMachine

    @VendingMachine.setter
    def VendingMachine(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_VendingMachine__VendingMachine", None)
        self.__VendingMachine = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "office18"):
                opp_val = getattr(old_value, "office18", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "office18"):
                opp_val = getattr(value, "office18", None)
                if opp_val is None:
                    setattr(value, "office18", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vms(self):
        return self.__vms

    @vms.setter
    def vms(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_VendingMachine__vms", None)
        self.__vms = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BookingOffice27"):
                opp_val = getattr(old_value, "BookingOffice27", None)
                if opp_val == self:
                    setattr(old_value, "BookingOffice27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BookingOffice27"):
                opp_val = getattr(value, "BookingOffice27", None)
                setattr(value, "BookingOffice27", self)

class Trip:

    pass
class CoachBus_RegularTrip(Trip):

    pass
class CoachBus_Passenger:

    def __init__(self, name: str, age: int, idCard: str, passengers: set["CoachBus_Trip"] = None, psg: set["CoachBus_Ticket"] = None, Passenger: "CoachBus_Trip" = None, Passenger20: "CoachBus_Ticket" = None):
        self.name = name
        self.age = age
        self.idCard = idCard
        self.passengers = passengers if passengers is not None else set()
        self.psg = psg if psg is not None else set()
        self.Passenger = Passenger
        self.Passenger20 = Passenger20
        
        pass
    @property
    def idCard(self):
        return self.__idCard

    @idCard.setter
    def idCard(self, idCard: str):
        self.__idCard = idCard


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
    def Passenger(self):
        return self.__Passenger

    @Passenger.setter
    def Passenger(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Passenger__Passenger", None)
        self.__Passenger = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trips2"):
                opp_val = getattr(old_value, "trips2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trips2"):
                opp_val = getattr(value, "trips2", None)
                if opp_val is None:
                    setattr(value, "trips2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Passenger20(self):
        return self.__Passenger20

    @Passenger20.setter
    def Passenger20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Passenger__Passenger20", None)
        self.__Passenger20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "tickets"):
                opp_val = getattr(old_value, "tickets", None)
                if opp_val == self:
                    setattr(old_value, "tickets", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "tickets"):
                opp_val = getattr(value, "tickets", None)
                setattr(value, "tickets", self)

    @property
    def psg(self):
        return self.__psg

    @psg.setter
    def psg(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Passenger__psg", None)
        self.__psg = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Ticket"):
                    opp_val = getattr(item, "Ticket", None)
                    
                    if opp_val == self:
                        setattr(item, "Ticket", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Ticket"):
                    opp_val = getattr(item, "Ticket", None)
                    
                    setattr(item, "Ticket", self)
                    

    @property
    def passengers(self):
        return self.__passengers

    @passengers.setter
    def passengers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Passenger__passengers", None)
        self.__passengers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trip8"):
                    opp_val = getattr(item, "Trip8", None)
                    
                    if opp_val == self:
                        setattr(item, "Trip8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trip8"):
                    opp_val = getattr(item, "Trip8", None)
                    
                    setattr(item, "Trip8", self)
                    

class CoachBus_Coach:

    def __init__(self, id: int, name: str, model: str, noOfSeats: int, coaches: set["CoachBus_Trip"] = None, coach: set["CoachBus_SecurityGuard"] = None, coaches6: set["CoachBus_BookingOffice"] = None, Coach: "CoachBus_Trip" = None, Coach15: "CoachBus_BookingOffice" = None, Coach11: "CoachBus_SecurityGuard" = None):
        self.id = id
        self.name = name
        self.model = model
        self.noOfSeats = noOfSeats
        self.coaches = coaches if coaches is not None else set()
        self.coach = coach if coach is not None else set()
        self.coaches6 = coaches6 if coaches6 is not None else set()
        self.Coach = Coach
        self.Coach15 = Coach15
        self.Coach11 = Coach11
        
        pass
    @property
    def model(self):
        return self.__model

    @model.setter
    def model(self, model: str):
        self.__model = model


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def noOfSeats(self):
        return self.__noOfSeats

    @noOfSeats.setter
    def noOfSeats(self, noOfSeats: int):
        self.__noOfSeats = noOfSeats


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def Coach(self):
        return self.__Coach

    @Coach.setter
    def Coach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Coach__Coach", None)
        self.__Coach = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trips"):
                opp_val = getattr(old_value, "trips", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trips"):
                opp_val = getattr(value, "trips", None)
                if opp_val is None:
                    setattr(value, "trips", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Coach15(self):
        return self.__Coach15

    @Coach15.setter
    def Coach15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Coach__Coach15", None)
        self.__Coach15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "offices"):
                opp_val = getattr(old_value, "offices", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "offices"):
                opp_val = getattr(value, "offices", None)
                if opp_val is None:
                    setattr(value, "offices", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def coaches6(self):
        return self.__coaches6

    @coaches6.setter
    def coaches6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Coach__coaches6", None)
        self.__coaches6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "BookingOffice"):
                    opp_val = getattr(item, "BookingOffice", None)
                    
                    if opp_val == self:
                        setattr(item, "BookingOffice", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "BookingOffice"):
                    opp_val = getattr(item, "BookingOffice", None)
                    
                    setattr(item, "BookingOffice", self)
                    

    @property
    def coaches(self):
        return self.__coaches

    @coaches.setter
    def coaches(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Coach__coaches", None)
        self.__coaches = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Trip"):
                    opp_val = getattr(item, "Trip", None)
                    
                    if opp_val == self:
                        setattr(item, "Trip", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Trip"):
                    opp_val = getattr(item, "Trip", None)
                    
                    setattr(item, "Trip", self)
                    

    @property
    def Coach11(self):
        return self.__Coach11

    @Coach11.setter
    def Coach11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Coach__Coach11", None)
        self.__Coach11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "guards"):
                opp_val = getattr(old_value, "guards", None)
                if opp_val == self:
                    setattr(old_value, "guards", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "guards"):
                opp_val = getattr(value, "guards", None)
                setattr(value, "guards", self)

    @property
    def coach(self):
        return self.__coach

    @coach.setter
    def coach(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Coach__coach", None)
        self.__coach = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "SecurityGuard"):
                    opp_val = getattr(item, "SecurityGuard", None)
                    
                    if opp_val == self:
                        setattr(item, "SecurityGuard", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "SecurityGuard"):
                    opp_val = getattr(item, "SecurityGuard", None)
                    
                    setattr(item, "SecurityGuard", self)
                    

class CoachBus_Employee:

    def __init__(self, id: int, baseSalary: float):
        self.id = id
        self.baseSalary = baseSalary
        
        pass
    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: int):
        self.__id = id


    @property
    def baseSalary(self):
        return self.__baseSalary

    @baseSalary.setter
    def baseSalary(self, baseSalary: float):
        self.__baseSalary = baseSalary


class CoachBus_Ticket:

    def __init__(self, number: int, price: float, isRoundTrip: bool, Ticket: "CoachBus_Passenger" = None, tickets: "CoachBus_Passenger" = None, tickets22: "CoachBus_VendingMachine" = None, Ticket25: "CoachBus_VendingMachine" = None):
        self.number = number
        self.price = price
        self.isRoundTrip = isRoundTrip
        self.Ticket = Ticket
        self.tickets = tickets
        self.tickets22 = tickets22
        self.Ticket25 = Ticket25
        
        pass
    @property
    def isRoundTrip(self):
        return self.__isRoundTrip

    @isRoundTrip.setter
    def isRoundTrip(self, isRoundTrip: bool):
        self.__isRoundTrip = isRoundTrip


    @property
    def price(self):
        return self.__price

    @price.setter
    def price(self, price: float):
        self.__price = price


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


    @property
    def tickets(self):
        return self.__tickets

    @tickets.setter
    def tickets(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Ticket__tickets", None)
        self.__tickets = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Passenger20"):
                opp_val = getattr(old_value, "Passenger20", None)
                if opp_val == self:
                    setattr(old_value, "Passenger20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Passenger20"):
                opp_val = getattr(value, "Passenger20", None)
                setattr(value, "Passenger20", self)

    @property
    def Ticket(self):
        return self.__Ticket

    @Ticket.setter
    def Ticket(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Ticket__Ticket", None)
        self.__Ticket = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "psg"):
                opp_val = getattr(old_value, "psg", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "psg"):
                opp_val = getattr(value, "psg", None)
                if opp_val is None:
                    setattr(value, "psg", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def tickets22(self):
        return self.__tickets22

    @tickets22.setter
    def tickets22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Ticket__tickets22", None)
        self.__tickets22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "VendingMachine23"):
                opp_val = getattr(old_value, "VendingMachine23", None)
                if opp_val == self:
                    setattr(old_value, "VendingMachine23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "VendingMachine23"):
                opp_val = getattr(value, "VendingMachine23", None)
                setattr(value, "VendingMachine23", self)

    @property
    def Ticket25(self):
        return self.__Ticket25

    @Ticket25.setter
    def Ticket25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Ticket__Ticket25", None)
        self.__Ticket25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vm"):
                opp_val = getattr(old_value, "vm", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vm"):
                opp_val = getattr(value, "vm", None)
                if opp_val is None:
                    setattr(value, "vm", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CoachBus_BookingOffice:

    def __init__(self, officeID: int, name: str, location: str, BookingOffice: "CoachBus_Coach" = None, offices: set["CoachBus_Coach"] = None, office: "CoachBus_Manager" = None, office18: set["CoachBus_VendingMachine"] = None, BookingOffice27: "CoachBus_VendingMachine" = None, BookingOffice13: "CoachBus_Manager" = None):
        self.officeID = officeID
        self.name = name
        self.location = location
        self.BookingOffice = BookingOffice
        self.offices = offices if offices is not None else set()
        self.office = office
        self.office18 = office18 if office18 is not None else set()
        self.BookingOffice27 = BookingOffice27
        self.BookingOffice13 = BookingOffice13
        
        pass
    @property
    def officeID(self):
        return self.__officeID

    @officeID.setter
    def officeID(self, officeID: int):
        self.__officeID = officeID


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
    def BookingOffice(self):
        return self.__BookingOffice

    @BookingOffice.setter
    def BookingOffice(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_BookingOffice__BookingOffice", None)
        self.__BookingOffice = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coaches6"):
                opp_val = getattr(old_value, "coaches6", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coaches6"):
                opp_val = getattr(value, "coaches6", None)
                if opp_val is None:
                    setattr(value, "coaches6", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def office(self):
        return self.__office

    @office.setter
    def office(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_BookingOffice__office", None)
        self.__office = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Manager"):
                opp_val = getattr(old_value, "Manager", None)
                if opp_val == self:
                    setattr(old_value, "Manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Manager"):
                opp_val = getattr(value, "Manager", None)
                setattr(value, "Manager", self)

    @property
    def BookingOffice27(self):
        return self.__BookingOffice27

    @BookingOffice27.setter
    def BookingOffice27(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_BookingOffice__BookingOffice27", None)
        self.__BookingOffice27 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vms"):
                opp_val = getattr(old_value, "vms", None)
                if opp_val == self:
                    setattr(old_value, "vms", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vms"):
                opp_val = getattr(value, "vms", None)
                setattr(value, "vms", self)

    @property
    def BookingOffice13(self):
        return self.__BookingOffice13

    @BookingOffice13.setter
    def BookingOffice13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_BookingOffice__BookingOffice13", None)
        self.__BookingOffice13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "manager"):
                opp_val = getattr(old_value, "manager", None)
                if opp_val == self:
                    setattr(old_value, "manager", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "manager"):
                opp_val = getattr(value, "manager", None)
                setattr(value, "manager", self)

    @property
    def offices(self):
        return self.__offices

    @offices.setter
    def offices(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_BookingOffice__offices", None)
        self.__offices = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Coach15"):
                    opp_val = getattr(item, "Coach15", None)
                    
                    if opp_val == self:
                        setattr(item, "Coach15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Coach15"):
                    opp_val = getattr(item, "Coach15", None)
                    
                    setattr(item, "Coach15", self)
                    

    @property
    def office18(self):
        return self.__office18

    @office18.setter
    def office18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_BookingOffice__office18", None)
        self.__office18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "VendingMachine"):
                    opp_val = getattr(item, "VendingMachine", None)
                    
                    if opp_val == self:
                        setattr(item, "VendingMachine", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "VendingMachine"):
                    opp_val = getattr(item, "VendingMachine", None)
                    
                    setattr(item, "VendingMachine", self)
                    

class CoachBus_SecurityGuard(Employee):

    def __init__(self, shift: str, SecurityGuard: "CoachBus_Coach" = None, guards: "CoachBus_Coach" = None):
        self.shift = shift
        self.SecurityGuard = SecurityGuard
        self.guards = guards
        
        pass
    @property
    def shift(self):
        return self.__shift

    @shift.setter
    def shift(self, shift: str):
        self.__shift = shift


    @property
    def guards(self):
        return self.__guards

    @guards.setter
    def guards(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_SecurityGuard__guards", None)
        self.__guards = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Coach11"):
                opp_val = getattr(old_value, "Coach11", None)
                if opp_val == self:
                    setattr(old_value, "Coach11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Coach11"):
                opp_val = getattr(value, "Coach11", None)
                setattr(value, "Coach11", self)

    @property
    def SecurityGuard(self):
        return self.__SecurityGuard

    @SecurityGuard.setter
    def SecurityGuard(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_SecurityGuard__SecurityGuard", None)
        self.__SecurityGuard = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coach"):
                opp_val = getattr(old_value, "coach", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coach"):
                opp_val = getattr(value, "coach", None)
                if opp_val is None:
                    setattr(value, "coach", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class CoachBus_PrivateTrip(Trip):

    def __init__(self, extras: str):
        self.extras = extras
        
        pass
    @property
    def extras(self):
        return self.__extras

    @extras.setter
    def extras(self, extras: str):
        self.__extras = extras


class CoachBus_Trip:

    def __init__(self, name: str, origin: str, destination: str, type: str, number: int, Trip: "CoachBus_Coach" = None, Trip8: "CoachBus_Passenger" = None, trips: set["CoachBus_Coach"] = None, trips2: set["CoachBus_Passenger"] = None):
        self.name = name
        self.origin = origin
        self.destination = destination
        self.type = type
        self.number = number
        self.Trip = Trip
        self.Trip8 = Trip8
        self.trips = trips if trips is not None else set()
        self.trips2 = trips2 if trips2 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def destination(self):
        return self.__destination

    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination


    @property
    def number(self):
        return self.__number

    @number.setter
    def number(self, number: int):
        self.__number = number


    @property
    def origin(self):
        return self.__origin

    @origin.setter
    def origin(self, origin: str):
        self.__origin = origin


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def trips2(self):
        return self.__trips2

    @trips2.setter
    def trips2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Trip__trips2", None)
        self.__trips2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Passenger"):
                    opp_val = getattr(item, "Passenger", None)
                    
                    if opp_val == self:
                        setattr(item, "Passenger", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Passenger"):
                    opp_val = getattr(item, "Passenger", None)
                    
                    setattr(item, "Passenger", self)
                    

    @property
    def Trip(self):
        return self.__Trip

    @Trip.setter
    def Trip(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Trip__Trip", None)
        self.__Trip = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "coaches"):
                opp_val = getattr(old_value, "coaches", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "coaches"):
                opp_val = getattr(value, "coaches", None)
                if opp_val is None:
                    setattr(value, "coaches", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def trips(self):
        return self.__trips

    @trips.setter
    def trips(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Trip__trips", None)
        self.__trips = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Coach"):
                    opp_val = getattr(item, "Coach", None)
                    
                    if opp_val == self:
                        setattr(item, "Coach", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Coach"):
                    opp_val = getattr(item, "Coach", None)
                    
                    setattr(item, "Coach", self)
                    

    @property
    def Trip8(self):
        return self.__Trip8

    @Trip8.setter
    def Trip8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CoachBus_Trip__Trip8", None)
        self.__Trip8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passengers"):
                opp_val = getattr(old_value, "passengers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passengers"):
                opp_val = getattr(value, "passengers", None)
                if opp_val is None:
                    setattr(value, "passengers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)
