from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DataMove:

    pass
class pyrep_Turn(DataMove):

    pass
class pyrep_Move(DataMove):

    def __init__(self, distance: str):
        self.distance = distance
        
        pass
    @property
    def distance(self):
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance


class AbstractDataMove:

    pass
class pyrep_AbstractCrossMove(AbstractDataMove):

    pass
class pyrep_AbstractMove(AbstractDataMove):

    pass
class pyrep_AbstractDataMove:

    pass
class Entity:

    pass
class pyrep_DataMove(Entity):

    def __init__(self, name: bool, type: str, velocity: str, pyrep_DataMove: "pyrep_AbstractMove" = None, pyrep_DataMove15: "pyrep_AbstractCrossMove" = None):
        self.name = name
        self.type = type
        self.velocity = velocity
        self.pyrep_DataMove = pyrep_DataMove
        self.pyrep_DataMove15 = pyrep_DataMove15
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name


    @property
    def velocity(self):
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: str):
        self.__velocity = velocity


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def pyrep_DataMove15(self):
        return self.__pyrep_DataMove15

    @pyrep_DataMove15.setter
    def pyrep_DataMove15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_DataMove__pyrep_DataMove15", None)
        self.__pyrep_DataMove15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_AbstractCrossMove"):
                opp_val = getattr(old_value, "pyrep_AbstractCrossMove", None)
                if opp_val == self:
                    setattr(old_value, "pyrep_AbstractCrossMove", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_AbstractCrossMove"):
                opp_val = getattr(value, "pyrep_AbstractCrossMove", None)
                setattr(value, "pyrep_AbstractCrossMove", self)

    @property
    def pyrep_DataMove(self):
        return self.__pyrep_DataMove

    @pyrep_DataMove.setter
    def pyrep_DataMove(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_DataMove__pyrep_DataMove", None)
        self.__pyrep_DataMove = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_AbstractMove"):
                opp_val = getattr(old_value, "pyrep_AbstractMove", None)
                if opp_val == self:
                    setattr(old_value, "pyrep_AbstractMove", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_AbstractMove"):
                opp_val = getattr(value, "pyrep_AbstractMove", None)
                setattr(value, "pyrep_AbstractMove", self)

class pyrep_MoveCollection(Entity):

    def __init__(self, name: str, concurrent: bool, pyrep_MoveCollection9: "pyrep_Robot" = None, pyrep_MoveCollection12: set["pyrep_AbstractDataMove"] = None, pyrep_MoveCollection: "pyrep_Environment" = None):
        self.name = name
        self.concurrent = concurrent
        self.pyrep_MoveCollection9 = pyrep_MoveCollection9
        self.pyrep_MoveCollection12 = pyrep_MoveCollection12 if pyrep_MoveCollection12 is not None else set()
        self.pyrep_MoveCollection = pyrep_MoveCollection
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def concurrent(self):
        return self.__concurrent

    @concurrent.setter
    def concurrent(self, concurrent: bool):
        self.__concurrent = concurrent


    @property
    def pyrep_MoveCollection12(self):
        return self.__pyrep_MoveCollection12

    @pyrep_MoveCollection12.setter
    def pyrep_MoveCollection12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_MoveCollection__pyrep_MoveCollection12", None)
        self.__pyrep_MoveCollection12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pyrep_AbstractDataMove"):
                    opp_val = getattr(item, "pyrep_AbstractDataMove", None)
                    
                    if opp_val == self:
                        setattr(item, "pyrep_AbstractDataMove", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pyrep_AbstractDataMove"):
                    opp_val = getattr(item, "pyrep_AbstractDataMove", None)
                    
                    setattr(item, "pyrep_AbstractDataMove", self)
                    

    @property
    def pyrep_MoveCollection(self):
        return self.__pyrep_MoveCollection

    @pyrep_MoveCollection.setter
    def pyrep_MoveCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_MoveCollection__pyrep_MoveCollection", None)
        self.__pyrep_MoveCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_Environment5"):
                opp_val = getattr(old_value, "pyrep_Environment5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_Environment5"):
                opp_val = getattr(value, "pyrep_Environment5", None)
                if opp_val is None:
                    setattr(value, "pyrep_Environment5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pyrep_MoveCollection9(self):
        return self.__pyrep_MoveCollection9

    @pyrep_MoveCollection9.setter
    def pyrep_MoveCollection9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_MoveCollection__pyrep_MoveCollection9", None)
        self.__pyrep_MoveCollection9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_Robot10"):
                opp_val = getattr(old_value, "pyrep_Robot10", None)
                if opp_val == self:
                    setattr(old_value, "pyrep_Robot10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_Robot10"):
                opp_val = getattr(value, "pyrep_Robot10", None)
                setattr(value, "pyrep_Robot10", self)

class pyrep_Sensor(Entity):

    def __init__(self, name: str, pyrep_Sensor: "pyrep_TypeSensor" = None):
        self.name = name
        self.pyrep_Sensor = pyrep_Sensor
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pyrep_Sensor(self):
        return self.__pyrep_Sensor

    @pyrep_Sensor.setter
    def pyrep_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_Sensor__pyrep_Sensor", None)
        self.__pyrep_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_TypeSensor"):
                opp_val = getattr(old_value, "pyrep_TypeSensor", None)
                if opp_val == self:
                    setattr(old_value, "pyrep_TypeSensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_TypeSensor"):
                opp_val = getattr(value, "pyrep_TypeSensor", None)
                setattr(value, "pyrep_TypeSensor", self)

class pyrep_IP(Entity):

    def __init__(self, name: str, ip: str, pyrep_IP: "pyrep_Environment" = None):
        self.name = name
        self.ip = ip
        self.pyrep_IP = pyrep_IP
        
        pass
    @property
    def ip(self):
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pyrep_IP(self):
        return self.__pyrep_IP

    @pyrep_IP.setter
    def pyrep_IP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_IP__pyrep_IP", None)
        self.__pyrep_IP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_Environment"):
                opp_val = getattr(old_value, "pyrep_Environment", None)
                if opp_val == self:
                    setattr(old_value, "pyrep_Environment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_Environment"):
                opp_val = getattr(value, "pyrep_Environment", None)
                setattr(value, "pyrep_Environment", self)

class pyrep_Robot(Entity):

    def __init__(self, name: str, port: int, pyrep_Robot10: "pyrep_MoveCollection" = None, pyrep_Robot: "pyrep_Environment" = None, pyrep_Robot7: set["pyrep_Wheel"] = None):
        self.name = name
        self.port = port
        self.pyrep_Robot10 = pyrep_Robot10
        self.pyrep_Robot = pyrep_Robot
        self.pyrep_Robot7 = pyrep_Robot7 if pyrep_Robot7 is not None else set()
        
        pass
    @property
    def port(self):
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pyrep_Robot7(self):
        return self.__pyrep_Robot7

    @pyrep_Robot7.setter
    def pyrep_Robot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_Robot__pyrep_Robot7", None)
        self.__pyrep_Robot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pyrep_Wheel"):
                    opp_val = getattr(item, "pyrep_Wheel", None)
                    
                    if opp_val == self:
                        setattr(item, "pyrep_Wheel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pyrep_Wheel"):
                    opp_val = getattr(item, "pyrep_Wheel", None)
                    
                    setattr(item, "pyrep_Wheel", self)
                    

    @property
    def pyrep_Robot(self):
        return self.__pyrep_Robot

    @pyrep_Robot.setter
    def pyrep_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_Robot__pyrep_Robot", None)
        self.__pyrep_Robot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_Environment3"):
                opp_val = getattr(old_value, "pyrep_Environment3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_Environment3"):
                opp_val = getattr(value, "pyrep_Environment3", None)
                if opp_val is None:
                    setattr(value, "pyrep_Environment3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def pyrep_Robot10(self):
        return self.__pyrep_Robot10

    @pyrep_Robot10.setter
    def pyrep_Robot10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_Robot__pyrep_Robot10", None)
        self.__pyrep_Robot10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_MoveCollection9"):
                opp_val = getattr(old_value, "pyrep_MoveCollection9", None)
                if opp_val == self:
                    setattr(old_value, "pyrep_MoveCollection9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_MoveCollection9"):
                opp_val = getattr(value, "pyrep_MoveCollection9", None)
                setattr(value, "pyrep_MoveCollection9", self)

class pyrep_TypeSensor(Entity):

    def __init__(self, typeName: str, pyrep_TypeSensor: "pyrep_Sensor" = None):
        self.typeName = typeName
        self.pyrep_TypeSensor = pyrep_TypeSensor
        
        pass
    @property
    def typeName(self):
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName


    @property
    def pyrep_TypeSensor(self):
        return self.__pyrep_TypeSensor

    @pyrep_TypeSensor.setter
    def pyrep_TypeSensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_TypeSensor__pyrep_TypeSensor", None)
        self.__pyrep_TypeSensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_Sensor"):
                opp_val = getattr(old_value, "pyrep_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "pyrep_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_Sensor"):
                opp_val = getattr(value, "pyrep_Sensor", None)
                setattr(value, "pyrep_Sensor", self)

class pyrep_Wheel(Entity):

    def __init__(self, name: str, radius: str, pyrep_Wheel: "pyrep_Robot" = None):
        self.name = name
        self.radius = radius
        self.pyrep_Wheel = pyrep_Wheel
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def radius(self):
        return self.__radius

    @radius.setter
    def radius(self, radius: str):
        self.__radius = radius


    @property
    def pyrep_Wheel(self):
        return self.__pyrep_Wheel

    @pyrep_Wheel.setter
    def pyrep_Wheel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_Wheel__pyrep_Wheel", None)
        self.__pyrep_Wheel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_Robot7"):
                opp_val = getattr(old_value, "pyrep_Robot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_Robot7"):
                opp_val = getattr(value, "pyrep_Robot7", None)
                if opp_val is None:
                    setattr(value, "pyrep_Robot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class pyrep_Environment(Entity):

    def __init__(self, name: str, pyrep_Environment: "pyrep_IP" = None, pyrep_Environment3: set["pyrep_Robot"] = None, pyrep_Environment5: set["pyrep_MoveCollection"] = None):
        self.name = name
        self.pyrep_Environment = pyrep_Environment
        self.pyrep_Environment3 = pyrep_Environment3 if pyrep_Environment3 is not None else set()
        self.pyrep_Environment5 = pyrep_Environment5 if pyrep_Environment5 is not None else set()
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def pyrep_Environment5(self):
        return self.__pyrep_Environment5

    @pyrep_Environment5.setter
    def pyrep_Environment5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_Environment__pyrep_Environment5", None)
        self.__pyrep_Environment5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pyrep_MoveCollection"):
                    opp_val = getattr(item, "pyrep_MoveCollection", None)
                    
                    if opp_val == self:
                        setattr(item, "pyrep_MoveCollection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pyrep_MoveCollection"):
                    opp_val = getattr(item, "pyrep_MoveCollection", None)
                    
                    setattr(item, "pyrep_MoveCollection", self)
                    

    @property
    def pyrep_Environment(self):
        return self.__pyrep_Environment

    @pyrep_Environment.setter
    def pyrep_Environment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_Environment__pyrep_Environment", None)
        self.__pyrep_Environment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "pyrep_IP"):
                opp_val = getattr(old_value, "pyrep_IP", None)
                if opp_val == self:
                    setattr(old_value, "pyrep_IP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "pyrep_IP"):
                opp_val = getattr(value, "pyrep_IP", None)
                setattr(value, "pyrep_IP", self)

    @property
    def pyrep_Environment3(self):
        return self.__pyrep_Environment3

    @pyrep_Environment3.setter
    def pyrep_Environment3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pyrep_Environment__pyrep_Environment3", None)
        self.__pyrep_Environment3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pyrep_Robot"):
                    opp_val = getattr(item, "pyrep_Robot", None)
                    
                    if opp_val == self:
                        setattr(item, "pyrep_Robot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pyrep_Robot"):
                    opp_val = getattr(item, "pyrep_Robot", None)
                    
                    setattr(item, "pyrep_Robot", self)
                    

class pyrep_Entity:

    pass
class pyrep_Model:

    pass