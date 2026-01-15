from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class DataMove:

    pass
class PyDslRep_Turn(DataMove):

    pass
class PyDslRep_Move(DataMove):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class AbstractDataMove:

    pass
class PyDslRep_AbstractCrossMove(AbstractDataMove):

    pass
class PyDslRep_AbstractMove(AbstractDataMove):

    pass
class PyDslRep_AbstractDataMove:

    pass
class Entity:

    pass
class PyDslRep_Wheel(Entity):

    def __init__(self, name: str, radius: str, PyDslRep_Wheel: "PyDslRep_Robot" = None):
        self.name = name
        self.radius = radius
        self.PyDslRep_Wheel = PyDslRep_Wheel
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def radius(self) -> str:
        return self.__radius

    @radius.setter
    def radius(self, radius: str):
        self.__radius = radius

    @property
    def PyDslRep_Wheel(self):
        return self.__PyDslRep_Wheel

    @PyDslRep_Wheel.setter
    def PyDslRep_Wheel(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_Wheel__PyDslRep_Wheel", None)
        self.__PyDslRep_Wheel = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_Robot7"):
                opp_val = getattr(old_value, "PyDslRep_Robot7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_Robot7"):
                opp_val = getattr(value, "PyDslRep_Robot7", None)
                if opp_val is None:
                    setattr(value, "PyDslRep_Robot7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PyDslRep_MoveCollection(Entity):

    def __init__(self, concurrent: bool, name: str, PyDslRep_MoveCollection: "PyDslRep_Environment" = None, PyDslRep_MoveCollection9: "PyDslRep_Robot" = None, PyDslRep_MoveCollection12: set["PyDslRep_AbstractDataMove"] = None):
        self.concurrent = concurrent
        self.name = name
        self.PyDslRep_MoveCollection = PyDslRep_MoveCollection
        self.PyDslRep_MoveCollection9 = PyDslRep_MoveCollection9
        self.PyDslRep_MoveCollection12 = PyDslRep_MoveCollection12 if PyDslRep_MoveCollection12 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def concurrent(self) -> bool:
        return self.__concurrent

    @concurrent.setter
    def concurrent(self, concurrent: bool):
        self.__concurrent = concurrent

    @property
    def PyDslRep_MoveCollection9(self):
        return self.__PyDslRep_MoveCollection9

    @PyDslRep_MoveCollection9.setter
    def PyDslRep_MoveCollection9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_MoveCollection__PyDslRep_MoveCollection9", None)
        self.__PyDslRep_MoveCollection9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_Robot10"):
                opp_val = getattr(old_value, "PyDslRep_Robot10", None)
                if opp_val == self:
                    setattr(old_value, "PyDslRep_Robot10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_Robot10"):
                opp_val = getattr(value, "PyDslRep_Robot10", None)
                setattr(value, "PyDslRep_Robot10", self)

    @property
    def PyDslRep_MoveCollection(self):
        return self.__PyDslRep_MoveCollection

    @PyDslRep_MoveCollection.setter
    def PyDslRep_MoveCollection(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_MoveCollection__PyDslRep_MoveCollection", None)
        self.__PyDslRep_MoveCollection = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_Environment5"):
                opp_val = getattr(old_value, "PyDslRep_Environment5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_Environment5"):
                opp_val = getattr(value, "PyDslRep_Environment5", None)
                if opp_val is None:
                    setattr(value, "PyDslRep_Environment5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PyDslRep_MoveCollection12(self):
        return self.__PyDslRep_MoveCollection12

    @PyDslRep_MoveCollection12.setter
    def PyDslRep_MoveCollection12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_MoveCollection__PyDslRep_MoveCollection12", None)
        self.__PyDslRep_MoveCollection12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PyDslRep_AbstractDataMove"):
                    opp_val = getattr(item, "PyDslRep_AbstractDataMove", None)
                    
                    if opp_val == self:
                        setattr(item, "PyDslRep_AbstractDataMove", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PyDslRep_AbstractDataMove"):
                    opp_val = getattr(item, "PyDslRep_AbstractDataMove", None)
                    
                    setattr(item, "PyDslRep_AbstractDataMove", self)
                    

class PyDslRep_Sensor(Entity):

    def __init__(self, name: str, PyDslRep_Sensor: "PyDslRep_TypeSensor" = None):
        self.name = name
        self.PyDslRep_Sensor = PyDslRep_Sensor
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PyDslRep_Sensor(self):
        return self.__PyDslRep_Sensor

    @PyDslRep_Sensor.setter
    def PyDslRep_Sensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_Sensor__PyDslRep_Sensor", None)
        self.__PyDslRep_Sensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_TypeSensor"):
                opp_val = getattr(old_value, "PyDslRep_TypeSensor", None)
                if opp_val == self:
                    setattr(old_value, "PyDslRep_TypeSensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_TypeSensor"):
                opp_val = getattr(value, "PyDslRep_TypeSensor", None)
                setattr(value, "PyDslRep_TypeSensor", self)

class PyDslRep_TypeSensor(Entity):

    def __init__(self, typeName: str, PyDslRep_TypeSensor: "PyDslRep_Sensor" = None):
        self.typeName = typeName
        self.PyDslRep_TypeSensor = PyDslRep_TypeSensor
        
    @property
    def typeName(self) -> str:
        return self.__typeName

    @typeName.setter
    def typeName(self, typeName: str):
        self.__typeName = typeName

    @property
    def PyDslRep_TypeSensor(self):
        return self.__PyDslRep_TypeSensor

    @PyDslRep_TypeSensor.setter
    def PyDslRep_TypeSensor(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_TypeSensor__PyDslRep_TypeSensor", None)
        self.__PyDslRep_TypeSensor = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_Sensor"):
                opp_val = getattr(old_value, "PyDslRep_Sensor", None)
                if opp_val == self:
                    setattr(old_value, "PyDslRep_Sensor", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_Sensor"):
                opp_val = getattr(value, "PyDslRep_Sensor", None)
                setattr(value, "PyDslRep_Sensor", self)

class PyDslRep_DataMove(Entity):

    def __init__(self, name: bool, type: str, velocity: str, PyDslRep_DataMove: "PyDslRep_AbstractMove" = None, PyDslRep_DataMove15: "PyDslRep_AbstractCrossMove" = None):
        self.name = name
        self.type = type
        self.velocity = velocity
        self.PyDslRep_DataMove = PyDslRep_DataMove
        self.PyDslRep_DataMove15 = PyDslRep_DataMove15
        
    @property
    def name(self) -> bool:
        return self.__name

    @name.setter
    def name(self, name: bool):
        self.__name = name

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def velocity(self) -> str:
        return self.__velocity

    @velocity.setter
    def velocity(self, velocity: str):
        self.__velocity = velocity

    @property
    def PyDslRep_DataMove15(self):
        return self.__PyDslRep_DataMove15

    @PyDslRep_DataMove15.setter
    def PyDslRep_DataMove15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_DataMove__PyDslRep_DataMove15", None)
        self.__PyDslRep_DataMove15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_AbstractCrossMove"):
                opp_val = getattr(old_value, "PyDslRep_AbstractCrossMove", None)
                if opp_val == self:
                    setattr(old_value, "PyDslRep_AbstractCrossMove", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_AbstractCrossMove"):
                opp_val = getattr(value, "PyDslRep_AbstractCrossMove", None)
                setattr(value, "PyDslRep_AbstractCrossMove", self)

    @property
    def PyDslRep_DataMove(self):
        return self.__PyDslRep_DataMove

    @PyDslRep_DataMove.setter
    def PyDslRep_DataMove(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_DataMove__PyDslRep_DataMove", None)
        self.__PyDslRep_DataMove = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_AbstractMove"):
                opp_val = getattr(old_value, "PyDslRep_AbstractMove", None)
                if opp_val == self:
                    setattr(old_value, "PyDslRep_AbstractMove", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_AbstractMove"):
                opp_val = getattr(value, "PyDslRep_AbstractMove", None)
                setattr(value, "PyDslRep_AbstractMove", self)

class PyDslRep_Environment(Entity):

    def __init__(self, name: str, PyDslRep_Environment: "PyDslRep_IP" = None, PyDslRep_Environment3: set["PyDslRep_Robot"] = None, PyDslRep_Environment5: set["PyDslRep_MoveCollection"] = None):
        self.name = name
        self.PyDslRep_Environment = PyDslRep_Environment
        self.PyDslRep_Environment3 = PyDslRep_Environment3 if PyDslRep_Environment3 is not None else set()
        self.PyDslRep_Environment5 = PyDslRep_Environment5 if PyDslRep_Environment5 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def PyDslRep_Environment3(self):
        return self.__PyDslRep_Environment3

    @PyDslRep_Environment3.setter
    def PyDslRep_Environment3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_Environment__PyDslRep_Environment3", None)
        self.__PyDslRep_Environment3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PyDslRep_Robot"):
                    opp_val = getattr(item, "PyDslRep_Robot", None)
                    
                    if opp_val == self:
                        setattr(item, "PyDslRep_Robot", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PyDslRep_Robot"):
                    opp_val = getattr(item, "PyDslRep_Robot", None)
                    
                    setattr(item, "PyDslRep_Robot", self)
                    

    @property
    def PyDslRep_Environment5(self):
        return self.__PyDslRep_Environment5

    @PyDslRep_Environment5.setter
    def PyDslRep_Environment5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_Environment__PyDslRep_Environment5", None)
        self.__PyDslRep_Environment5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PyDslRep_MoveCollection"):
                    opp_val = getattr(item, "PyDslRep_MoveCollection", None)
                    
                    if opp_val == self:
                        setattr(item, "PyDslRep_MoveCollection", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PyDslRep_MoveCollection"):
                    opp_val = getattr(item, "PyDslRep_MoveCollection", None)
                    
                    setattr(item, "PyDslRep_MoveCollection", self)
                    

    @property
    def PyDslRep_Environment(self):
        return self.__PyDslRep_Environment

    @PyDslRep_Environment.setter
    def PyDslRep_Environment(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_Environment__PyDslRep_Environment", None)
        self.__PyDslRep_Environment = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_IP"):
                opp_val = getattr(old_value, "PyDslRep_IP", None)
                if opp_val == self:
                    setattr(old_value, "PyDslRep_IP", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_IP"):
                opp_val = getattr(value, "PyDslRep_IP", None)
                setattr(value, "PyDslRep_IP", self)

class PyDslRep_Entity:

    pass
class PyDslRep_Model:

    pass
class PyDslRep_Robot(Entity):

    def __init__(self, name: str, port: int, PyDslRep_Robot: "PyDslRep_Environment" = None, PyDslRep_Robot7: set["PyDslRep_Wheel"] = None, PyDslRep_Robot10: "PyDslRep_MoveCollection" = None):
        self.name = name
        self.port = port
        self.PyDslRep_Robot = PyDslRep_Robot
        self.PyDslRep_Robot7 = PyDslRep_Robot7 if PyDslRep_Robot7 is not None else set()
        self.PyDslRep_Robot10 = PyDslRep_Robot10
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def port(self) -> int:
        return self.__port

    @port.setter
    def port(self, port: int):
        self.__port = port

    @property
    def PyDslRep_Robot7(self):
        return self.__PyDslRep_Robot7

    @PyDslRep_Robot7.setter
    def PyDslRep_Robot7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_Robot__PyDslRep_Robot7", None)
        self.__PyDslRep_Robot7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "PyDslRep_Wheel"):
                    opp_val = getattr(item, "PyDslRep_Wheel", None)
                    
                    if opp_val == self:
                        setattr(item, "PyDslRep_Wheel", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "PyDslRep_Wheel"):
                    opp_val = getattr(item, "PyDslRep_Wheel", None)
                    
                    setattr(item, "PyDslRep_Wheel", self)
                    

    @property
    def PyDslRep_Robot10(self):
        return self.__PyDslRep_Robot10

    @PyDslRep_Robot10.setter
    def PyDslRep_Robot10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_Robot__PyDslRep_Robot10", None)
        self.__PyDslRep_Robot10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_MoveCollection9"):
                opp_val = getattr(old_value, "PyDslRep_MoveCollection9", None)
                if opp_val == self:
                    setattr(old_value, "PyDslRep_MoveCollection9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_MoveCollection9"):
                opp_val = getattr(value, "PyDslRep_MoveCollection9", None)
                setattr(value, "PyDslRep_MoveCollection9", self)

    @property
    def PyDslRep_Robot(self):
        return self.__PyDslRep_Robot

    @PyDslRep_Robot.setter
    def PyDslRep_Robot(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_Robot__PyDslRep_Robot", None)
        self.__PyDslRep_Robot = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_Environment3"):
                opp_val = getattr(old_value, "PyDslRep_Environment3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_Environment3"):
                opp_val = getattr(value, "PyDslRep_Environment3", None)
                if opp_val is None:
                    setattr(value, "PyDslRep_Environment3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class PyDslRep_IP(Entity):

    def __init__(self, name: str, ip: str, PyDslRep_IP: "PyDslRep_Environment" = None):
        self.name = name
        self.ip = ip
        self.PyDslRep_IP = PyDslRep_IP
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def ip(self) -> str:
        return self.__ip

    @ip.setter
    def ip(self, ip: str):
        self.__ip = ip

    @property
    def PyDslRep_IP(self):
        return self.__PyDslRep_IP

    @PyDslRep_IP.setter
    def PyDslRep_IP(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PyDslRep_IP__PyDslRep_IP", None)
        self.__PyDslRep_IP = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PyDslRep_Environment"):
                opp_val = getattr(old_value, "PyDslRep_Environment", None)
                if opp_val == self:
                    setattr(old_value, "PyDslRep_Environment", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PyDslRep_Environment"):
                opp_val = getattr(value, "PyDslRep_Environment", None)
                setattr(value, "PyDslRep_Environment", self)
