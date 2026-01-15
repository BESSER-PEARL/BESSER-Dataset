from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class helloWeb_UserFunction:

    def __init__(self, name: str, helloWeb_UserFunction: set["helloWeb_Command"] = None):
        self.name = name
        self.helloWeb_UserFunction = helloWeb_UserFunction if helloWeb_UserFunction is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def helloWeb_UserFunction(self):
        return self.__helloWeb_UserFunction

    @helloWeb_UserFunction.setter
    def helloWeb_UserFunction(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloWeb_UserFunction__helloWeb_UserFunction", None)
        self.__helloWeb_UserFunction = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloWeb_Command"):
                    opp_val = getattr(item, "helloWeb_Command", None)
                    
                    if opp_val == self:
                        setattr(item, "helloWeb_Command", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloWeb_Command"):
                    opp_val = getattr(item, "helloWeb_Command", None)
                    
                    setattr(item, "helloWeb_Command", self)
                    

class helloWeb_RecordedFlight:

    def __init__(self, video_name: str):
        self.video_name = video_name
        
    @property
    def video_name(self) -> str:
        return self.__video_name

    @video_name.setter
    def video_name(self, video_name: str):
        self.__video_name = video_name

class helloWeb_SuperCommand:

    pass
class helloWeb_Main:

    def __init__(self, takeoff: str, land: str, helloWeb_Main: "helloWeb_Program" = None, helloWeb_Main2: set["helloWeb_SuperCommand"] = None):
        self.takeoff = takeoff
        self.land = land
        self.helloWeb_Main = helloWeb_Main
        self.helloWeb_Main2 = helloWeb_Main2 if helloWeb_Main2 is not None else set()
        
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
    def helloWeb_Main2(self):
        return self.__helloWeb_Main2

    @helloWeb_Main2.setter
    def helloWeb_Main2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloWeb_Main__helloWeb_Main2", None)
        self.__helloWeb_Main2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "helloWeb_SuperCommand"):
                    opp_val = getattr(item, "helloWeb_SuperCommand", None)
                    
                    if opp_val == self:
                        setattr(item, "helloWeb_SuperCommand", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "helloWeb_SuperCommand"):
                    opp_val = getattr(item, "helloWeb_SuperCommand", None)
                    
                    setattr(item, "helloWeb_SuperCommand", self)
                    

    @property
    def helloWeb_Main(self):
        return self.__helloWeb_Main

    @helloWeb_Main.setter
    def helloWeb_Main(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_helloWeb_Main__helloWeb_Main", None)
        self.__helloWeb_Main = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "helloWeb_Program"):
                opp_val = getattr(old_value, "helloWeb_Program", None)
                if opp_val == self:
                    setattr(old_value, "helloWeb_Program", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "helloWeb_Program"):
                opp_val = getattr(value, "helloWeb_Program", None)
                setattr(value, "helloWeb_Program", self)

class helloWeb_Program:

    pass
class Command:

    pass
class helloWeb_Right(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class helloWeb_Up(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class helloWeb_RotateL(Command):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class helloWeb_Wait(Command):

    def __init__(self, seconds: str):
        self.seconds = seconds
        
    @property
    def seconds(self) -> str:
        return self.__seconds

    @seconds.setter
    def seconds(self, seconds: str):
        self.__seconds = seconds

class helloWeb_Down(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class helloWeb_Backward(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class helloWeb_RotateR(Command):

    def __init__(self, angle: int):
        self.angle = angle
        
    @property
    def angle(self) -> int:
        return self.__angle

    @angle.setter
    def angle(self, angle: int):
        self.__angle = angle

class helloWeb_Left(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class helloWeb_Forward(Command):

    def __init__(self, distance: str):
        self.distance = distance
        
    @property
    def distance(self) -> str:
        return self.__distance

    @distance.setter
    def distance(self, distance: str):
        self.__distance = distance

class helloWeb_Snapshot(Command):

    def __init__(self, image_name: str):
        self.image_name = image_name
        
    @property
    def image_name(self) -> str:
        return self.__image_name

    @image_name.setter
    def image_name(self, image_name: str):
        self.__image_name = image_name

class SuperCommand:

    pass
class helloWeb_FunctionName(SuperCommand):

    def __init__(self, func_name: str):
        self.func_name = func_name
        
    @property
    def func_name(self) -> str:
        return self.__func_name

    @func_name.setter
    def func_name(self, func_name: str):
        self.__func_name = func_name

class helloWeb_FeatureMatch:

    def __init__(self, image_name: str):
        self.image_name = image_name
        
    @property
    def image_name(self) -> str:
        return self.__image_name

    @image_name.setter
    def image_name(self, image_name: str):
        self.__image_name = image_name

class helloWeb_Command(SuperCommand):

    pass