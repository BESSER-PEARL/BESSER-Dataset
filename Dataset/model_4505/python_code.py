from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class xDrone_UpWall:

    def __init__(self, value: str, xDrone_UpWall: "xDrone_Walls" = None):
        self.value = value
        self.xDrone_UpWall = xDrone_UpWall
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def xDrone_UpWall(self):
        return self.__xDrone_UpWall

    @xDrone_UpWall.setter
    def xDrone_UpWall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_UpWall__xDrone_UpWall", None)
        self.__xDrone_UpWall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Walls38"):
                opp_val = getattr(old_value, "xDrone_Walls38", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Walls38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Walls38"):
                opp_val = getattr(value, "xDrone_Walls38", None)
                setattr(value, "xDrone_Walls38", self)

class xDrone_LeftWall:

    def __init__(self, value: str, xDrone_LeftWall: "xDrone_Walls" = None):
        self.value = value
        self.xDrone_LeftWall = xDrone_LeftWall
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def xDrone_LeftWall(self):
        return self.__xDrone_LeftWall

    @xDrone_LeftWall.setter
    def xDrone_LeftWall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_LeftWall__xDrone_LeftWall", None)
        self.__xDrone_LeftWall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Walls36"):
                opp_val = getattr(old_value, "xDrone_Walls36", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Walls36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Walls36"):
                opp_val = getattr(value, "xDrone_Walls36", None)
                setattr(value, "xDrone_Walls36", self)

class xDrone_BackWall:

    def __init__(self, value: str, xDrone_BackWall: "xDrone_Walls" = None):
        self.value = value
        self.xDrone_BackWall = xDrone_BackWall
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def xDrone_BackWall(self):
        return self.__xDrone_BackWall

    @xDrone_BackWall.setter
    def xDrone_BackWall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_BackWall__xDrone_BackWall", None)
        self.__xDrone_BackWall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Walls34"):
                opp_val = getattr(old_value, "xDrone_Walls34", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Walls34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Walls34"):
                opp_val = getattr(value, "xDrone_Walls34", None)
                setattr(value, "xDrone_Walls34", self)

class xDrone_RightWall:

    def __init__(self, value: str, xDrone_RightWall: "xDrone_Walls" = None):
        self.value = value
        self.xDrone_RightWall = xDrone_RightWall
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def xDrone_RightWall(self):
        return self.__xDrone_RightWall

    @xDrone_RightWall.setter
    def xDrone_RightWall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_RightWall__xDrone_RightWall", None)
        self.__xDrone_RightWall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Walls32"):
                opp_val = getattr(old_value, "xDrone_Walls32", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Walls32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Walls32"):
                opp_val = getattr(value, "xDrone_Walls32", None)
                setattr(value, "xDrone_Walls32", self)

class xDrone_FrontWall:

    def __init__(self, value: str, xDrone_FrontWall: "xDrone_Walls" = None):
        self.value = value
        self.xDrone_FrontWall = xDrone_FrontWall
        
    @property
    def value(self) -> str:
        return self.__value

    @value.setter
    def value(self, value: str):
        self.__value = value

    @property
    def xDrone_FrontWall(self):
        return self.__xDrone_FrontWall

    @xDrone_FrontWall.setter
    def xDrone_FrontWall(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_FrontWall__xDrone_FrontWall", None)
        self.__xDrone_FrontWall = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Walls30"):
                opp_val = getattr(old_value, "xDrone_Walls30", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Walls30", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Walls30"):
                opp_val = getattr(value, "xDrone_Walls30", None)
                setattr(value, "xDrone_Walls30", self)

class xDrone_Vector:

    def __init__(self, x: str, y: str, z: str, xDrone_Vector: "xDrone_Origin" = None, xDrone_Vector25: "xDrone_Size" = None, xDrone_Vector28: "xDrone_Position" = None):
        self.x = x
        self.y = y
        self.z = z
        self.xDrone_Vector = xDrone_Vector
        self.xDrone_Vector25 = xDrone_Vector25
        self.xDrone_Vector28 = xDrone_Vector28
        
    @property
    def y(self) -> str:
        return self.__y

    @y.setter
    def y(self, y: str):
        self.__y = y

    @property
    def x(self) -> str:
        return self.__x

    @x.setter
    def x(self, x: str):
        self.__x = x

    @property
    def z(self) -> str:
        return self.__z

    @z.setter
    def z(self, z: str):
        self.__z = z

    @property
    def xDrone_Vector25(self):
        return self.__xDrone_Vector25

    @xDrone_Vector25.setter
    def xDrone_Vector25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Vector__xDrone_Vector25", None)
        self.__xDrone_Vector25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Size24"):
                opp_val = getattr(old_value, "xDrone_Size24", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Size24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Size24"):
                opp_val = getattr(value, "xDrone_Size24", None)
                setattr(value, "xDrone_Size24", self)

    @property
    def xDrone_Vector28(self):
        return self.__xDrone_Vector28

    @xDrone_Vector28.setter
    def xDrone_Vector28(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Vector__xDrone_Vector28", None)
        self.__xDrone_Vector28 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Position27"):
                opp_val = getattr(old_value, "xDrone_Position27", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Position27", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Position27"):
                opp_val = getattr(value, "xDrone_Position27", None)
                setattr(value, "xDrone_Position27", self)

    @property
    def xDrone_Vector(self):
        return self.__xDrone_Vector

    @xDrone_Vector.setter
    def xDrone_Vector(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Vector__xDrone_Vector", None)
        self.__xDrone_Vector = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Origin22"):
                opp_val = getattr(old_value, "xDrone_Origin22", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Origin22", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Origin22"):
                opp_val = getattr(value, "xDrone_Origin22", None)
                setattr(value, "xDrone_Origin22", self)

class xDrone_Color:

    def __init__(self, color_value: str, xDrone_Color: "xDrone_Object" = None):
        self.color_value = color_value
        self.xDrone_Color = xDrone_Color
        
    @property
    def color_value(self) -> str:
        return self.__color_value

    @color_value.setter
    def color_value(self, color_value: str):
        self.__color_value = color_value

    @property
    def xDrone_Color(self):
        return self.__xDrone_Color

    @xDrone_Color.setter
    def xDrone_Color(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Color__xDrone_Color", None)
        self.__xDrone_Color = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Object20"):
                opp_val = getattr(old_value, "xDrone_Object20", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Object20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Object20"):
                opp_val = getattr(value, "xDrone_Object20", None)
                setattr(value, "xDrone_Object20", self)

class xDrone_Size:

    pass
class xDrone_Origin:

    pass
class xDrone_Position:

    pass
class Command:

    pass
class xDrone_Right(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class xDrone_Left(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class xDrone_Backward(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class xDrone_RotateR(Command):

    def __init__(self, angle: str):
        self.angle = angle
        
    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

class xDrone_Forward(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class xDrone_RotateL(Command):

    def __init__(self, angle: str):
        self.angle = angle
        
    @property
    def angle(self) -> str:
        return self.__angle

    @angle.setter
    def angle(self, angle: str):
        self.__angle = angle

class xDrone_Down(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class xDrone_Up(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class xDrone_Wait(Command):

    def __init__(self, seconds: str):
        self.seconds = seconds
        
    @property
    def seconds(self) -> str:
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: str):
        self.__seconds = seconds

class xDrone_GoTo(Command):

    def __init__(self, object_name: str):
        self.object_name = object_name
        
    @property
    def object_name(self) -> str:
        return self.__object_name

    @object_name.setter
    def object_name(self, object_name: str):
        self.__object_name = object_name

class SuperCommand:

    pass
class xDrone_Command(SuperCommand):

    pass
class xDrone_Object:

    def __init__(self, object_name: str, xDrone_Object: "xDrone_Environment" = None, xDrone_Object16: "xDrone_Origin" = None, xDrone_Object18: "xDrone_Size" = None, xDrone_Object20: "xDrone_Color" = None):
        self.object_name = object_name
        self.xDrone_Object = xDrone_Object
        self.xDrone_Object16 = xDrone_Object16
        self.xDrone_Object18 = xDrone_Object18
        self.xDrone_Object20 = xDrone_Object20
        
    @property
    def object_name(self) -> str:
        return self.__object_name

    @object_name.setter
    def object_name(self, object_name: str):
        self.__object_name = object_name

    @property
    def xDrone_Object16(self):
        return self.__xDrone_Object16

    @xDrone_Object16.setter
    def xDrone_Object16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Object__xDrone_Object16", None)
        self.__xDrone_Object16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Origin"):
                opp_val = getattr(old_value, "xDrone_Origin", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Origin", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Origin"):
                opp_val = getattr(value, "xDrone_Origin", None)
                setattr(value, "xDrone_Origin", self)

    @property
    def xDrone_Object(self):
        return self.__xDrone_Object

    @xDrone_Object.setter
    def xDrone_Object(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Object__xDrone_Object", None)
        self.__xDrone_Object = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Environment12"):
                opp_val = getattr(old_value, "xDrone_Environment12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Environment12"):
                opp_val = getattr(value, "xDrone_Environment12", None)
                if opp_val is None:
                    setattr(value, "xDrone_Environment12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xDrone_Object18(self):
        return self.__xDrone_Object18

    @xDrone_Object18.setter
    def xDrone_Object18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Object__xDrone_Object18", None)
        self.__xDrone_Object18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Size"):
                opp_val = getattr(old_value, "xDrone_Size", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Size", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Size"):
                opp_val = getattr(value, "xDrone_Size", None)
                setattr(value, "xDrone_Size", self)

    @property
    def xDrone_Object20(self):
        return self.__xDrone_Object20

    @xDrone_Object20.setter
    def xDrone_Object20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Object__xDrone_Object20", None)
        self.__xDrone_Object20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Color"):
                opp_val = getattr(old_value, "xDrone_Color", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Color", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Color"):
                opp_val = getattr(value, "xDrone_Color", None)
                setattr(value, "xDrone_Color", self)

class xDrone_Walls:

    pass
class xDrone_Drone:

    def __init__(self, rotation: str, xDrone_Drone: "xDrone_Environment" = None, xDrone_Drone14: "xDrone_Position" = None):
        self.rotation = rotation
        self.xDrone_Drone = xDrone_Drone
        self.xDrone_Drone14 = xDrone_Drone14
        
    @property
    def rotation(self) -> str:
        return self.__rotation

    @rotation.setter
    def rotation(self, rotation: str):
        self.__rotation = rotation

    @property
    def xDrone_Drone(self):
        return self.__xDrone_Drone

    @xDrone_Drone.setter
    def xDrone_Drone(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Drone__xDrone_Drone", None)
        self.__xDrone_Drone = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Environment8"):
                opp_val = getattr(old_value, "xDrone_Environment8", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Environment8"):
                opp_val = getattr(value, "xDrone_Environment8", None)
                if opp_val is None:
                    setattr(value, "xDrone_Environment8", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def xDrone_Drone14(self):
        return self.__xDrone_Drone14

    @xDrone_Drone14.setter
    def xDrone_Drone14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Drone__xDrone_Drone14", None)
        self.__xDrone_Drone14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Position"):
                opp_val = getattr(old_value, "xDrone_Position", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Position", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Position"):
                opp_val = getattr(value, "xDrone_Position", None)
                setattr(value, "xDrone_Position", self)

class xDrone_SuperCommand:

    pass
class xDrone_Environment:

    pass
class xDrone_Fly:

    def __init__(self, takeoff: str, land: str, xDrone_Fly: "xDrone_Main" = None, xDrone_Fly6: set["xDrone_SuperCommand"] = None):
        self.takeoff = takeoff
        self.land = land
        self.xDrone_Fly = xDrone_Fly
        self.xDrone_Fly6 = xDrone_Fly6 if xDrone_Fly6 is not None else set()
        
    @property
    def takeoff(self) -> str:
        return self.__takeoff

    @takeoff.setter
    def takeoff(self, takeoff: str):
        self.__takeoff = takeoff

    @property
    def land(self) -> str:
        return self.__land

    @land.setter
    def land(self, land: str):
        self.__land = land

    @property
    def xDrone_Fly(self):
        return self.__xDrone_Fly

    @xDrone_Fly.setter
    def xDrone_Fly(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Fly__xDrone_Fly", None)
        self.__xDrone_Fly = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "xDrone_Main2"):
                opp_val = getattr(old_value, "xDrone_Main2", None)
                if opp_val == self:
                    setattr(old_value, "xDrone_Main2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "xDrone_Main2"):
                opp_val = getattr(value, "xDrone_Main2", None)
                setattr(value, "xDrone_Main2", self)

    @property
    def xDrone_Fly6(self):
        return self.__xDrone_Fly6

    @xDrone_Fly6.setter
    def xDrone_Fly6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_xDrone_Fly__xDrone_Fly6", None)
        self.__xDrone_Fly6 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "xDrone_SuperCommand"):
                    opp_val = getattr(item, "xDrone_SuperCommand", None)
                    
                    if opp_val == self:
                        setattr(item, "xDrone_SuperCommand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "xDrone_SuperCommand"):
                    opp_val = getattr(item, "xDrone_SuperCommand", None)
                    
                    setattr(item, "xDrone_SuperCommand", self)
                    

class xDrone_Main:

    pass
class xDrone_Program:

    pass