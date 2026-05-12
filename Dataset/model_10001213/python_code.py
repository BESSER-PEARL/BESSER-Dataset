from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Train:

    def __init__(self, myEngine: str, myCoach: str):
        self.myEngine = myEngine
        self.myCoach = myCoach
        
        pass
    @property
    def myCoach(self):
        return self.__myCoach
    @myCoach.setter
    def myCoach(self, myCoach: str):
        self.__myCoach = myCoach

    @property
    def myEngine(self):
        return self.__myEngine
    @myEngine.setter
    def myEngine(self, myEngine: str):
        self.__myEngine = myEngine



class Engine:

    def __init__(self, horsePower: str, fuelAvg: str):
        self.horsePower = horsePower
        self.fuelAvg = fuelAvg
        
        pass
    @property
    def fuelAvg(self):
        return self.__fuelAvg
    @fuelAvg.setter
    def fuelAvg(self, fuelAvg: str):
        self.__fuelAvg = fuelAvg

    @property
    def horsePower(self):
        return self.__horsePower
    @horsePower.setter
    def horsePower(self, horsePower: str):
        self.__horsePower = horsePower



class Route:

    def __init__(self, destination: str, source: str, stops: str, routeId: int, service11: "Service" = None):
        self.destination = destination
        self.source = source
        self.stops = stops
        self.routeId = routeId
        self.service11 = service11
        
        pass
    @property
    def routeId(self):
        return self.__routeId
    @routeId.setter
    def routeId(self, routeId: int):
        self.__routeId = routeId

    @property
    def destination(self):
        return self.__destination
    @destination.setter
    def destination(self, destination: str):
        self.__destination = destination

    @property
    def source(self):
        return self.__source
    @source.setter
    def source(self, source: str):
        self.__source = source

    @property
    def stops(self):
        return self.__stops
    @stops.setter
    def stops(self, stops: str):
        self.__stops = stops

    @property
    def service11(self):
        return self.__service11
    @service11.setter
    def service11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Route__service11", None)
        self.__service11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "route10"):
                opp_val = getattr(old_value, "route10", None)
                if opp_val == self:
                    setattr(old_value, "route10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "route10"):
                opp_val = getattr(value, "route10", None)
                setattr(value, "route10", self)



class TrainBuilder_Interface:

    pass


class Coach:

    def __init__(self, capacity: int, totalPassengers: int, temprature: str, humidity: str, coachType: str):
        self.capacity = capacity
        self.totalPassengers = totalPassengers
        self.temprature = temprature
        self.humidity = humidity
        self.coachType = coachType
        
        pass
    @property
    def humidity(self):
        return self.__humidity
    @humidity.setter
    def humidity(self, humidity: str):
        self.__humidity = humidity

    @property
    def capacity(self):
        return self.__capacity
    @capacity.setter
    def capacity(self, capacity: int):
        self.__capacity = capacity

    @property
    def totalPassengers(self):
        return self.__totalPassengers
    @totalPassengers.setter
    def totalPassengers(self, totalPassengers: int):
        self.__totalPassengers = totalPassengers

    @property
    def temprature(self):
        return self.__temprature
    @temprature.setter
    def temprature(self, temprature: str):
        self.__temprature = temprature

    @property
    def coachType(self):
        return self.__coachType
    @coachType.setter
    def coachType(self, coachType: str):
        self.__coachType = coachType



class Sleeper:

    def __init__(self, builder: TrainBuilder_Interface, sleeperTrain: str, trainBuilder4: "TrainBuilder_Interface" = None, trainBuilder16: set["TrainBuilder_Interface"] = None):
        self.builder = builder
        self.sleeperTrain = sleeperTrain
        self.trainBuilder4 = trainBuilder4
        self.trainBuilder16 = trainBuilder16 if trainBuilder16 is not None else set()
        
        pass
    @property
    def sleeperTrain(self):
        return self.__sleeperTrain
    @sleeperTrain.setter
    def sleeperTrain(self, sleeperTrain: str):
        self.__sleeperTrain = sleeperTrain

    @property
    def builder(self):
        return self.__builder
    @builder.setter
    def builder(self, builder: TrainBuilder_Interface):
        self.__builder = builder

    @property
    def trainBuilder16(self):
        return self.__trainBuilder16
    @trainBuilder16.setter
    def trainBuilder16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sleeper__trainBuilder16", None)
        self.__trainBuilder16 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "sleeper17"):
                    opp_val = getattr(item, "sleeper17", None)
                    
                    if opp_val == self:
                        setattr(item, "sleeper17", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "sleeper17"):
                    opp_val = getattr(item, "sleeper17", None)
                    
                    setattr(item, "sleeper17", self)
                    

    @property
    def trainBuilder4(self):
        return self.__trainBuilder4
    @trainBuilder4.setter
    def trainBuilder4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Sleeper__trainBuilder4", None)
        self.__trainBuilder4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "sleeper5"):
                opp_val = getattr(old_value, "sleeper5", None)
                if opp_val == self:
                    setattr(old_value, "sleeper5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "sleeper5"):
                opp_val = getattr(value, "sleeper5", None)
                setattr(value, "sleeper5", self)



class InterCity:

    def __init__(self, builder: TrainBuilder_Interface, interCityTrain: str, trainBuilder6: "TrainBuilder_Interface" = None, trainBuilder14: set["TrainBuilder_Interface"] = None):
        self.builder = builder
        self.interCityTrain = interCityTrain
        self.trainBuilder6 = trainBuilder6
        self.trainBuilder14 = trainBuilder14 if trainBuilder14 is not None else set()
        
        pass
    @property
    def interCityTrain(self):
        return self.__interCityTrain
    @interCityTrain.setter
    def interCityTrain(self, interCityTrain: str):
        self.__interCityTrain = interCityTrain

    @property
    def builder(self):
        return self.__builder
    @builder.setter
    def builder(self, builder: TrainBuilder_Interface):
        self.__builder = builder

    @property
    def trainBuilder14(self):
        return self.__trainBuilder14
    @trainBuilder14.setter
    def trainBuilder14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_InterCity__trainBuilder14", None)
        self.__trainBuilder14 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "interCity15"):
                    opp_val = getattr(item, "interCity15", None)
                    
                    if opp_val == self:
                        setattr(item, "interCity15", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "interCity15"):
                    opp_val = getattr(item, "interCity15", None)
                    
                    setattr(item, "interCity15", self)
                    

    @property
    def trainBuilder6(self):
        return self.__trainBuilder6
    @trainBuilder6.setter
    def trainBuilder6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_InterCity__trainBuilder6", None)
        self.__trainBuilder6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "interCity7"):
                opp_val = getattr(old_value, "interCity7", None)
                if opp_val == self:
                    setattr(old_value, "interCity7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "interCity7"):
                opp_val = getattr(value, "interCity7", None)
                setattr(value, "interCity7", self)



class Commutator:

    def __init__(self, builder: TrainBuilder_Interface, commutatorTrain: str, trainBuilder8: "TrainBuilder_Interface" = None, trainBuilder18: set["TrainBuilder_Interface"] = None):
        self.builder = builder
        self.commutatorTrain = commutatorTrain
        self.trainBuilder8 = trainBuilder8
        self.trainBuilder18 = trainBuilder18 if trainBuilder18 is not None else set()
        
        pass
    @property
    def builder(self):
        return self.__builder
    @builder.setter
    def builder(self, builder: TrainBuilder_Interface):
        self.__builder = builder

    @property
    def commutatorTrain(self):
        return self.__commutatorTrain
    @commutatorTrain.setter
    def commutatorTrain(self, commutatorTrain: str):
        self.__commutatorTrain = commutatorTrain

    @property
    def trainBuilder18(self):
        return self.__trainBuilder18
    @trainBuilder18.setter
    def trainBuilder18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Commutator__trainBuilder18", None)
        self.__trainBuilder18 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "commutator19"):
                    opp_val = getattr(item, "commutator19", None)
                    
                    if opp_val == self:
                        setattr(item, "commutator19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "commutator19"):
                    opp_val = getattr(item, "commutator19", None)
                    
                    setattr(item, "commutator19", self)
                    

    @property
    def trainBuilder8(self):
        return self.__trainBuilder8
    @trainBuilder8.setter
    def trainBuilder8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Commutator__trainBuilder8", None)
        self.__trainBuilder8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "commutator9"):
                opp_val = getattr(old_value, "commutator9", None)
                if opp_val == self:
                    setattr(old_value, "commutator9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "commutator9"):
                opp_val = getattr(value, "commutator9", None)
                setattr(value, "commutator9", self)



class ServiceType_Interface:

    pass


class ServiceTypeFactory:

    def __init__(self, type: str, getServiceType: ServiceType_Interface, service1: "Service" = None, serviceType2: set["ServiceType_Interface"] = None):
        self.type = type
        self.getServiceType = getServiceType
        self.service1 = service1
        self.serviceType2 = serviceType2 if serviceType2 is not None else set()
        
        pass
    @property
    def getServiceType(self):
        return self.__getServiceType
    @getServiceType.setter
    def getServiceType(self, getServiceType: ServiceType_Interface):
        self.__getServiceType = getServiceType

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def service1(self):
        return self.__service1
    @service1.setter
    def service1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ServiceTypeFactory__service1", None)
        self.__service1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "serviceTypeFactory0"):
                opp_val = getattr(old_value, "serviceTypeFactory0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "serviceTypeFactory0"):
                opp_val = getattr(value, "serviceTypeFactory0", None)
                if opp_val is None:
                    setattr(value, "serviceTypeFactory0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def serviceType2(self):
        return self.__serviceType2
    @serviceType2.setter
    def serviceType2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ServiceTypeFactory__serviceType2", None)
        self.__serviceType2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "serviceTypeFactory3"):
                    opp_val = getattr(item, "serviceTypeFactory3", None)
                    
                    if opp_val == self:
                        setattr(item, "serviceTypeFactory3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "serviceTypeFactory3"):
                    opp_val = getattr(item, "serviceTypeFactory3", None)
                    
                    setattr(item, "serviceTypeFactory3", self)
                    



class TrainStats:

    def __init__(self, trainService: str, fuelAvg: str, passengerCount: int, tempAvg: str, humidityAvg: str, service12: "Service" = None):
        self.trainService = trainService
        self.fuelAvg = fuelAvg
        self.passengerCount = passengerCount
        self.tempAvg = tempAvg
        self.humidityAvg = humidityAvg
        self.service12 = service12
        
        pass
    @property
    def tempAvg(self):
        return self.__tempAvg
    @tempAvg.setter
    def tempAvg(self, tempAvg: str):
        self.__tempAvg = tempAvg

    @property
    def trainService(self):
        return self.__trainService
    @trainService.setter
    def trainService(self, trainService: str):
        self.__trainService = trainService

    @property
    def passengerCount(self):
        return self.__passengerCount
    @passengerCount.setter
    def passengerCount(self, passengerCount: int):
        self.__passengerCount = passengerCount

    @property
    def fuelAvg(self):
        return self.__fuelAvg
    @fuelAvg.setter
    def fuelAvg(self, fuelAvg: str):
        self.__fuelAvg = fuelAvg

    @property
    def humidityAvg(self):
        return self.__humidityAvg
    @humidityAvg.setter
    def humidityAvg(self, humidityAvg: str):
        self.__humidityAvg = humidityAvg

    @property
    def service12(self):
        return self.__service12
    @service12.setter
    def service12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_TrainStats__service12", None)
        self.__service12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trainStats13"):
                opp_val = getattr(old_value, "trainStats13", None)
                if opp_val == self:
                    setattr(old_value, "trainStats13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trainStats13"):
                opp_val = getattr(value, "trainStats13", None)
                setattr(value, "trainStats13", self)



class Service:

    def __init__(self, arrivalDateTime: str, departureDateTime: str, serviceName: str, serviceId: int, type: ServiceType_Interface, serviceTypeFactory0: set["ServiceTypeFactory"] = None, route10: "Route" = None, trainStats13: "TrainStats" = None):
        self.arrivalDateTime = arrivalDateTime
        self.departureDateTime = departureDateTime
        self.serviceName = serviceName
        self.serviceId = serviceId
        self.type = type
        self.serviceTypeFactory0 = serviceTypeFactory0 if serviceTypeFactory0 is not None else set()
        self.route10 = route10
        self.trainStats13 = trainStats13
        
        pass
    @property
    def arrivalDateTime(self):
        return self.__arrivalDateTime
    @arrivalDateTime.setter
    def arrivalDateTime(self, arrivalDateTime: str):
        self.__arrivalDateTime = arrivalDateTime

    @property
    def serviceId(self):
        return self.__serviceId
    @serviceId.setter
    def serviceId(self, serviceId: int):
        self.__serviceId = serviceId

    @property
    def departureDateTime(self):
        return self.__departureDateTime
    @departureDateTime.setter
    def departureDateTime(self, departureDateTime: str):
        self.__departureDateTime = departureDateTime

    @property
    def serviceName(self):
        return self.__serviceName
    @serviceName.setter
    def serviceName(self, serviceName: str):
        self.__serviceName = serviceName

    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: ServiceType_Interface):
        self.__type = type

    @property
    def trainStats13(self):
        return self.__trainStats13
    @trainStats13.setter
    def trainStats13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__trainStats13", None)
        self.__trainStats13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service12"):
                opp_val = getattr(old_value, "service12", None)
                if opp_val == self:
                    setattr(old_value, "service12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service12"):
                opp_val = getattr(value, "service12", None)
                setattr(value, "service12", self)

    @property
    def route10(self):
        return self.__route10
    @route10.setter
    def route10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__route10", None)
        self.__route10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service11"):
                opp_val = getattr(old_value, "service11", None)
                if opp_val == self:
                    setattr(old_value, "service11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service11"):
                opp_val = getattr(value, "service11", None)
                setattr(value, "service11", self)

    @property
    def serviceTypeFactory0(self):
        return self.__serviceTypeFactory0
    @serviceTypeFactory0.setter
    def serviceTypeFactory0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__serviceTypeFactory0", None)
        self.__serviceTypeFactory0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "service1"):
                    opp_val = getattr(item, "service1", None)
                    
                    if opp_val == self:
                        setattr(item, "service1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "service1"):
                    opp_val = getattr(item, "service1", None)
                    
                    setattr(item, "service1", self)
                    

