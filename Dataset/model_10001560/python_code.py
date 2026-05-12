from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Report_by_ticket_amount_UseCase:

    pass


class Report_by_revenue_UseCase:

    pass


class Delete_vehicles_UseCase:

    pass


class Update_vehicles_information_UseCase:

    pass


class View_vehicles_information_UseCase:

    pass


class call_for_customers_UseCase:

    pass


class View_customers_information_UseCase:

    pass


class cancel_booking_UseCase:

    pass


class confirm_booking_UseCase:

    pass


class search_customers_UseCase:

    pass


class make_payment_UseCase:

    pass


class View_account_information_UseCase:

    pass


class Account_settings_UseCase:

    pass


class Login_UseCase:

    pass


class search_UseCase:

    pass


class confirm_information_UseCase:

    pass


class choose_seats_UseCase:

    pass


class choose_vehicle_UseCase:

    pass


class book_ticket_UseCase:

    pass


class Manager_Actor:

    pass


class statistical_reporting_UseCase:

    pass


class vehicle_management_UseCase:

    pass


class account_management_UseCase:

    pass


class customer_management_UseCase:

    pass


class Use_Actor:

    pass


class Book_ticket_UseCase:

    pass


class Search_the_route_UseCase:

    pass


class Customer_Actor:

    pass





class accoutUser:

    def __init__(self, idUser: int, emailUser: str, passwordUser: str, codeConfirm: str, dateRegister: str, idCompany: int, accoutUser_accoutUser_125: set["Car"] = None, infoCompany_infoCompany_030: "infoCompany" = None):
        self.idUser = idUser
        self.emailUser = emailUser
        self.passwordUser = passwordUser
        self.codeConfirm = codeConfirm
        self.dateRegister = dateRegister
        self.idCompany = idCompany
        self.accoutUser_accoutUser_125 = accoutUser_accoutUser_125 if accoutUser_accoutUser_125 is not None else set()
        self.infoCompany_infoCompany_030 = infoCompany_infoCompany_030
        
        pass
    @property
    def idCompany(self):
        return self.__idCompany
    @idCompany.setter
    def idCompany(self, idCompany: int):
        self.__idCompany = idCompany

    @property
    def idUser(self):
        return self.__idUser
    @idUser.setter
    def idUser(self, idUser: int):
        self.__idUser = idUser

    @property
    def codeConfirm(self):
        return self.__codeConfirm
    @codeConfirm.setter
    def codeConfirm(self, codeConfirm: str):
        self.__codeConfirm = codeConfirm

    @property
    def emailUser(self):
        return self.__emailUser
    @emailUser.setter
    def emailUser(self, emailUser: str):
        self.__emailUser = emailUser

    @property
    def dateRegister(self):
        return self.__dateRegister
    @dateRegister.setter
    def dateRegister(self, dateRegister: str):
        self.__dateRegister = dateRegister

    @property
    def passwordUser(self):
        return self.__passwordUser
    @passwordUser.setter
    def passwordUser(self, passwordUser: str):
        self.__passwordUser = passwordUser

    @property
    def infoCompany_infoCompany_030(self):
        return self.__infoCompany_infoCompany_030
    @infoCompany_infoCompany_030.setter
    def infoCompany_infoCompany_030(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accoutUser__infoCompany_infoCompany_030", None)
        self.__infoCompany_infoCompany_030 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "infoCompany_infoCompany_131"):
                opp_val = getattr(old_value, "infoCompany_infoCompany_131", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "infoCompany_infoCompany_131"):
                opp_val = getattr(value, "infoCompany_infoCompany_131", None)
                if opp_val is None:
                    setattr(value, "infoCompany_infoCompany_131", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def accoutUser_accoutUser_125(self):
        return self.__accoutUser_accoutUser_125
    @accoutUser_accoutUser_125.setter
    def accoutUser_accoutUser_125(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_accoutUser__accoutUser_accoutUser_125", None)
        self.__accoutUser_accoutUser_125 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "accoutUser_accoutUser_024"):
                    opp_val = getattr(item, "accoutUser_accoutUser_024", None)
                    
                    if opp_val == self:
                        setattr(item, "accoutUser_accoutUser_024", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "accoutUser_accoutUser_024"):
                    opp_val = getattr(item, "accoutUser_accoutUser_024", None)
                    
                    setattr(item, "accoutUser_accoutUser_024", self)
                    



class Ticket:

    def __init__(self, idTicket: int, idCustomer: int, idCar: int, numberSeat: int, positionSeat: str, positionSeatBelow: str, statusSeat: int, timeExchange: str, code: str, Car_Car2_026: "Car" = None, Customer_Customer_028: "Customer" = None):
        self.idTicket = idTicket
        self.idCustomer = idCustomer
        self.idCar = idCar
        self.numberSeat = numberSeat
        self.positionSeat = positionSeat
        self.positionSeatBelow = positionSeatBelow
        self.statusSeat = statusSeat
        self.timeExchange = timeExchange
        self.code = code
        self.Car_Car2_026 = Car_Car2_026
        self.Customer_Customer_028 = Customer_Customer_028
        
        pass
    @property
    def idCustomer(self):
        return self.__idCustomer
    @idCustomer.setter
    def idCustomer(self, idCustomer: int):
        self.__idCustomer = idCustomer

    @property
    def code(self):
        return self.__code
    @code.setter
    def code(self, code: str):
        self.__code = code

    @property
    def idTicket(self):
        return self.__idTicket
    @idTicket.setter
    def idTicket(self, idTicket: int):
        self.__idTicket = idTicket

    @property
    def positionSeatBelow(self):
        return self.__positionSeatBelow
    @positionSeatBelow.setter
    def positionSeatBelow(self, positionSeatBelow: str):
        self.__positionSeatBelow = positionSeatBelow

    @property
    def statusSeat(self):
        return self.__statusSeat
    @statusSeat.setter
    def statusSeat(self, statusSeat: int):
        self.__statusSeat = statusSeat

    @property
    def timeExchange(self):
        return self.__timeExchange
    @timeExchange.setter
    def timeExchange(self, timeExchange: str):
        self.__timeExchange = timeExchange

    @property
    def positionSeat(self):
        return self.__positionSeat
    @positionSeat.setter
    def positionSeat(self, positionSeat: str):
        self.__positionSeat = positionSeat

    @property
    def idCar(self):
        return self.__idCar
    @idCar.setter
    def idCar(self, idCar: int):
        self.__idCar = idCar

    @property
    def numberSeat(self):
        return self.__numberSeat
    @numberSeat.setter
    def numberSeat(self, numberSeat: int):
        self.__numberSeat = numberSeat

    @property
    def Customer_Customer_028(self):
        return self.__Customer_Customer_028
    @Customer_Customer_028.setter
    def Customer_Customer_028(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__Customer_Customer_028", None)
        self.__Customer_Customer_028 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Customer_Customer_129"):
                opp_val = getattr(old_value, "Customer_Customer_129", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Customer_Customer_129"):
                opp_val = getattr(value, "Customer_Customer_129", None)
                if opp_val is None:
                    setattr(value, "Customer_Customer_129", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Car_Car2_026(self):
        return self.__Car_Car2_026
    @Car_Car2_026.setter
    def Car_Car2_026(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ticket__Car_Car2_026", None)
        self.__Car_Car2_026 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Car_Car2_127"):
                opp_val = getattr(old_value, "Car_Car2_127", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Car_Car2_127"):
                opp_val = getattr(value, "Car_Car2_127", None)
                if opp_val is None:
                    setattr(value, "Car_Car2_127", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Customer:

    def __init__(self, idCustomer: int, nameCustomer: str, phoneCustomer: str, emailCustomer: str, Customer_Customer_129: set["Ticket"] = None):
        self.idCustomer = idCustomer
        self.nameCustomer = nameCustomer
        self.phoneCustomer = phoneCustomer
        self.emailCustomer = emailCustomer
        self.Customer_Customer_129 = Customer_Customer_129 if Customer_Customer_129 is not None else set()
        
        pass
    @property
    def emailCustomer(self):
        return self.__emailCustomer
    @emailCustomer.setter
    def emailCustomer(self, emailCustomer: str):
        self.__emailCustomer = emailCustomer

    @property
    def nameCustomer(self):
        return self.__nameCustomer
    @nameCustomer.setter
    def nameCustomer(self, nameCustomer: str):
        self.__nameCustomer = nameCustomer

    @property
    def phoneCustomer(self):
        return self.__phoneCustomer
    @phoneCustomer.setter
    def phoneCustomer(self, phoneCustomer: str):
        self.__phoneCustomer = phoneCustomer

    @property
    def idCustomer(self):
        return self.__idCustomer
    @idCustomer.setter
    def idCustomer(self, idCustomer: int):
        self.__idCustomer = idCustomer

    @property
    def Customer_Customer_129(self):
        return self.__Customer_Customer_129
    @Customer_Customer_129.setter
    def Customer_Customer_129(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Customer__Customer_Customer_129", None)
        self.__Customer_Customer_129 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Customer_Customer_028"):
                    opp_val = getattr(item, "Customer_Customer_028", None)
                    
                    if opp_val == self:
                        setattr(item, "Customer_Customer_028", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Customer_Customer_028"):
                    opp_val = getattr(item, "Customer_Customer_028", None)
                    
                    setattr(item, "Customer_Customer_028", self)
                    



class infoCompany:

    def __init__(self, idCompany: int, nameCompany: str, dateEstablish: str, phoneCompany: str, addressCompany: str, describeCompany: str, showSafe: str, dateRegister: str, dateUpdate: str, infoCompany_infoCompany_131: set["accoutUser"] = None):
        self.idCompany = idCompany
        self.nameCompany = nameCompany
        self.dateEstablish = dateEstablish
        self.phoneCompany = phoneCompany
        self.addressCompany = addressCompany
        self.describeCompany = describeCompany
        self.showSafe = showSafe
        self.dateRegister = dateRegister
        self.dateUpdate = dateUpdate
        self.infoCompany_infoCompany_131 = infoCompany_infoCompany_131 if infoCompany_infoCompany_131 is not None else set()
        
        pass
    @property
    def phoneCompany(self):
        return self.__phoneCompany
    @phoneCompany.setter
    def phoneCompany(self, phoneCompany: str):
        self.__phoneCompany = phoneCompany

    @property
    def describeCompany(self):
        return self.__describeCompany
    @describeCompany.setter
    def describeCompany(self, describeCompany: str):
        self.__describeCompany = describeCompany

    @property
    def dateEstablish(self):
        return self.__dateEstablish
    @dateEstablish.setter
    def dateEstablish(self, dateEstablish: str):
        self.__dateEstablish = dateEstablish

    @property
    def dateRegister(self):
        return self.__dateRegister
    @dateRegister.setter
    def dateRegister(self, dateRegister: str):
        self.__dateRegister = dateRegister

    @property
    def nameCompany(self):
        return self.__nameCompany
    @nameCompany.setter
    def nameCompany(self, nameCompany: str):
        self.__nameCompany = nameCompany

    @property
    def showSafe(self):
        return self.__showSafe
    @showSafe.setter
    def showSafe(self, showSafe: str):
        self.__showSafe = showSafe

    @property
    def dateUpdate(self):
        return self.__dateUpdate
    @dateUpdate.setter
    def dateUpdate(self, dateUpdate: str):
        self.__dateUpdate = dateUpdate

    @property
    def idCompany(self):
        return self.__idCompany
    @idCompany.setter
    def idCompany(self, idCompany: int):
        self.__idCompany = idCompany

    @property
    def addressCompany(self):
        return self.__addressCompany
    @addressCompany.setter
    def addressCompany(self, addressCompany: str):
        self.__addressCompany = addressCompany

    @property
    def infoCompany_infoCompany_131(self):
        return self.__infoCompany_infoCompany_131
    @infoCompany_infoCompany_131.setter
    def infoCompany_infoCompany_131(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_infoCompany__infoCompany_infoCompany_131", None)
        self.__infoCompany_infoCompany_131 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "infoCompany_infoCompany_030"):
                    opp_val = getattr(item, "infoCompany_infoCompany_030", None)
                    
                    if opp_val == self:
                        setattr(item, "infoCompany_infoCompany_030", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "infoCompany_infoCompany_030"):
                    opp_val = getattr(item, "infoCompany_infoCompany_030", None)
                    
                    setattr(item, "infoCompany_infoCompany_030", self)
                    



class mapCarExchange:

    def __init__(self, mapOnCar: str, mapBelowCar: str, timeExchange: str, idMap: int, idCar: int, Car_Car_022: "Car" = None):
        self.mapOnCar = mapOnCar
        self.mapBelowCar = mapBelowCar
        self.timeExchange = timeExchange
        self.idMap = idMap
        self.idCar = idCar
        self.Car_Car_022 = Car_Car_022
        
        pass
    @property
    def timeExchange(self):
        return self.__timeExchange
    @timeExchange.setter
    def timeExchange(self, timeExchange: str):
        self.__timeExchange = timeExchange

    @property
    def idCar(self):
        return self.__idCar
    @idCar.setter
    def idCar(self, idCar: int):
        self.__idCar = idCar

    @property
    def mapOnCar(self):
        return self.__mapOnCar
    @mapOnCar.setter
    def mapOnCar(self, mapOnCar: str):
        self.__mapOnCar = mapOnCar

    @property
    def mapBelowCar(self):
        return self.__mapBelowCar
    @mapBelowCar.setter
    def mapBelowCar(self, mapBelowCar: str):
        self.__mapBelowCar = mapBelowCar

    @property
    def idMap(self):
        return self.__idMap
    @idMap.setter
    def idMap(self, idMap: int):
        self.__idMap = idMap

    @property
    def Car_Car_022(self):
        return self.__Car_Car_022
    @Car_Car_022.setter
    def Car_Car_022(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_mapCarExchange__Car_Car_022", None)
        self.__Car_Car_022 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Car_Car_123"):
                opp_val = getattr(old_value, "Car_Car_123", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Car_Car_123"):
                opp_val = getattr(value, "Car_Car_123", None)
                if opp_val is None:
                    setattr(value, "Car_Car_123", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Car:

    def __init__(self, idCar: int, idUser: int, nameCar: str, classifyCar: int, statusCar: int, phoneCar: str, positionStartCar: str, positionEndCar: str, timeStartCar: str, numberPlatesCar: str, mapOnCar: str, mapBelowCar: str, fareCar: str, imageLinkCar: str, Car_Car_123: set["mapCarExchange"] = None, accoutUser_accoutUser_024: "accoutUser" = None, Car_Car2_127: set["Ticket"] = None):
        self.idCar = idCar
        self.idUser = idUser
        self.nameCar = nameCar
        self.classifyCar = classifyCar
        self.statusCar = statusCar
        self.phoneCar = phoneCar
        self.positionStartCar = positionStartCar
        self.positionEndCar = positionEndCar
        self.timeStartCar = timeStartCar
        self.numberPlatesCar = numberPlatesCar
        self.mapOnCar = mapOnCar
        self.mapBelowCar = mapBelowCar
        self.fareCar = fareCar
        self.imageLinkCar = imageLinkCar
        self.Car_Car_123 = Car_Car_123 if Car_Car_123 is not None else set()
        self.accoutUser_accoutUser_024 = accoutUser_accoutUser_024
        self.Car_Car2_127 = Car_Car2_127 if Car_Car2_127 is not None else set()
        
        pass
    @property
    def fareCar(self):
        return self.__fareCar
    @fareCar.setter
    def fareCar(self, fareCar: str):
        self.__fareCar = fareCar

    @property
    def idUser(self):
        return self.__idUser
    @idUser.setter
    def idUser(self, idUser: int):
        self.__idUser = idUser

    @property
    def imageLinkCar(self):
        return self.__imageLinkCar
    @imageLinkCar.setter
    def imageLinkCar(self, imageLinkCar: str):
        self.__imageLinkCar = imageLinkCar

    @property
    def idCar(self):
        return self.__idCar
    @idCar.setter
    def idCar(self, idCar: int):
        self.__idCar = idCar

    @property
    def phoneCar(self):
        return self.__phoneCar
    @phoneCar.setter
    def phoneCar(self, phoneCar: str):
        self.__phoneCar = phoneCar

    @property
    def mapOnCar(self):
        return self.__mapOnCar
    @mapOnCar.setter
    def mapOnCar(self, mapOnCar: str):
        self.__mapOnCar = mapOnCar

    @property
    def mapBelowCar(self):
        return self.__mapBelowCar
    @mapBelowCar.setter
    def mapBelowCar(self, mapBelowCar: str):
        self.__mapBelowCar = mapBelowCar

    @property
    def statusCar(self):
        return self.__statusCar
    @statusCar.setter
    def statusCar(self, statusCar: int):
        self.__statusCar = statusCar

    @property
    def timeStartCar(self):
        return self.__timeStartCar
    @timeStartCar.setter
    def timeStartCar(self, timeStartCar: str):
        self.__timeStartCar = timeStartCar

    @property
    def nameCar(self):
        return self.__nameCar
    @nameCar.setter
    def nameCar(self, nameCar: str):
        self.__nameCar = nameCar

    @property
    def classifyCar(self):
        return self.__classifyCar
    @classifyCar.setter
    def classifyCar(self, classifyCar: int):
        self.__classifyCar = classifyCar

    @property
    def numberPlatesCar(self):
        return self.__numberPlatesCar
    @numberPlatesCar.setter
    def numberPlatesCar(self, numberPlatesCar: str):
        self.__numberPlatesCar = numberPlatesCar

    @property
    def positionStartCar(self):
        return self.__positionStartCar
    @positionStartCar.setter
    def positionStartCar(self, positionStartCar: str):
        self.__positionStartCar = positionStartCar

    @property
    def positionEndCar(self):
        return self.__positionEndCar
    @positionEndCar.setter
    def positionEndCar(self, positionEndCar: str):
        self.__positionEndCar = positionEndCar

    @property
    def accoutUser_accoutUser_024(self):
        return self.__accoutUser_accoutUser_024
    @accoutUser_accoutUser_024.setter
    def accoutUser_accoutUser_024(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car__accoutUser_accoutUser_024", None)
        self.__accoutUser_accoutUser_024 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "accoutUser_accoutUser_125"):
                opp_val = getattr(old_value, "accoutUser_accoutUser_125", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "accoutUser_accoutUser_125"):
                opp_val = getattr(value, "accoutUser_accoutUser_125", None)
                if opp_val is None:
                    setattr(value, "accoutUser_accoutUser_125", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Car_Car2_127(self):
        return self.__Car_Car2_127
    @Car_Car2_127.setter
    def Car_Car2_127(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car__Car_Car2_127", None)
        self.__Car_Car2_127 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Car_Car2_026"):
                    opp_val = getattr(item, "Car_Car2_026", None)
                    
                    if opp_val == self:
                        setattr(item, "Car_Car2_026", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Car_Car2_026"):
                    opp_val = getattr(item, "Car_Car2_026", None)
                    
                    setattr(item, "Car_Car2_026", self)
                    

    @property
    def Car_Car_123(self):
        return self.__Car_Car_123
    @Car_Car_123.setter
    def Car_Car_123(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Car__Car_Car_123", None)
        self.__Car_Car_123 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Car_Car_022"):
                    opp_val = getattr(item, "Car_Car_022", None)
                    
                    if opp_val == self:
                        setattr(item, "Car_Car_022", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Car_Car_022"):
                    opp_val = getattr(item, "Car_Car_022", None)
                    
                    setattr(item, "Car_Car_022", self)
                    



class Login_UseCase3:

    pass


class statistical_reporting_UseCase1:

    pass


class Manager_Actor4:

    pass


class Login_UseCase2:

    pass


class vehicle_management_UseCase1:

    pass


class Manager_Actor3:

    pass


class Login_UseCase1:

    pass


class customer_management_UseCase1:

    pass


class Manager_Actor2:

    pass


class account_management_UseCase1:

    pass


class Manager_Actor1:

    pass


class Customer_Actor1:

    pass
