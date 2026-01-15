from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class vmLogo_Segment:

    pass
class vmLogo_Point:

    def __init__(self, x: str, y: str, vmLogo_Point8: "vmLogo_Segment" = None, vmLogo_Point11: "vmLogo_Segment" = None, vmLogo_Point: "vmLogo_Turtle" = None, vmLogo_Point5: "vmLogo_Turtle" = None):
        self.x = x
        self.y = y
        self.vmLogo_Point8 = vmLogo_Point8
        self.vmLogo_Point11 = vmLogo_Point11
        self.vmLogo_Point = vmLogo_Point
        self.vmLogo_Point5 = vmLogo_Point5
        
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
    def vmLogo_Point5(self):
        return self.__vmLogo_Point5

    @vmLogo_Point5.setter
    def vmLogo_Point5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmLogo_Point__vmLogo_Point5", None)
        self.__vmLogo_Point5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmLogo_Turtle4"):
                opp_val = getattr(old_value, "vmLogo_Turtle4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmLogo_Turtle4"):
                opp_val = getattr(value, "vmLogo_Turtle4", None)
                if opp_val is None:
                    setattr(value, "vmLogo_Turtle4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def vmLogo_Point11(self):
        return self.__vmLogo_Point11

    @vmLogo_Point11.setter
    def vmLogo_Point11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmLogo_Point__vmLogo_Point11", None)
        self.__vmLogo_Point11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmLogo_Segment10"):
                opp_val = getattr(old_value, "vmLogo_Segment10", None)
                if opp_val == self:
                    setattr(old_value, "vmLogo_Segment10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmLogo_Segment10"):
                opp_val = getattr(value, "vmLogo_Segment10", None)
                setattr(value, "vmLogo_Segment10", self)

    @property
    def vmLogo_Point(self):
        return self.__vmLogo_Point

    @vmLogo_Point.setter
    def vmLogo_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmLogo_Point__vmLogo_Point", None)
        self.__vmLogo_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmLogo_Turtle"):
                opp_val = getattr(old_value, "vmLogo_Turtle", None)
                if opp_val == self:
                    setattr(old_value, "vmLogo_Turtle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmLogo_Turtle"):
                opp_val = getattr(value, "vmLogo_Turtle", None)
                setattr(value, "vmLogo_Turtle", self)

    @property
    def vmLogo_Point8(self):
        return self.__vmLogo_Point8

    @vmLogo_Point8.setter
    def vmLogo_Point8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmLogo_Point__vmLogo_Point8", None)
        self.__vmLogo_Point8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmLogo_Segment7"):
                opp_val = getattr(old_value, "vmLogo_Segment7", None)
                if opp_val == self:
                    setattr(old_value, "vmLogo_Segment7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmLogo_Segment7"):
                opp_val = getattr(value, "vmLogo_Segment7", None)
                setattr(value, "vmLogo_Segment7", self)

class vmLogo_Turtle:

    def __init__(self, heading: str, penUp: str, vmLogo_Turtle: "vmLogo_Point" = None, vmLogo_Turtle2: set["vmLogo_Segment"] = None, vmLogo_Turtle4: set["vmLogo_Point"] = None):
        self.heading = heading
        self.penUp = penUp
        self.vmLogo_Turtle = vmLogo_Turtle
        self.vmLogo_Turtle2 = vmLogo_Turtle2 if vmLogo_Turtle2 is not None else set()
        self.vmLogo_Turtle4 = vmLogo_Turtle4 if vmLogo_Turtle4 is not None else set()
        
    @property
    def heading(self) -> str:
        return self.__heading

    @heading.setter
    def heading(self, heading: str):
        self.__heading = heading

    @property
    def penUp(self) -> str:
        return self.__penUp

    @penUp.setter
    def penUp(self, penUp: str):
        self.__penUp = penUp

    @property
    def vmLogo_Turtle(self):
        return self.__vmLogo_Turtle

    @vmLogo_Turtle.setter
    def vmLogo_Turtle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmLogo_Turtle__vmLogo_Turtle", None)
        self.__vmLogo_Turtle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmLogo_Point"):
                opp_val = getattr(old_value, "vmLogo_Point", None)
                if opp_val == self:
                    setattr(old_value, "vmLogo_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmLogo_Point"):
                opp_val = getattr(value, "vmLogo_Point", None)
                setattr(value, "vmLogo_Point", self)

    @property
    def vmLogo_Turtle2(self):
        return self.__vmLogo_Turtle2

    @vmLogo_Turtle2.setter
    def vmLogo_Turtle2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmLogo_Turtle__vmLogo_Turtle2", None)
        self.__vmLogo_Turtle2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vmLogo_Segment"):
                    opp_val = getattr(item, "vmLogo_Segment", None)
                    
                    if opp_val == self:
                        setattr(item, "vmLogo_Segment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vmLogo_Segment"):
                    opp_val = getattr(item, "vmLogo_Segment", None)
                    
                    setattr(item, "vmLogo_Segment", self)
                    

    @property
    def vmLogo_Turtle4(self):
        return self.__vmLogo_Turtle4

    @vmLogo_Turtle4.setter
    def vmLogo_Turtle4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmLogo_Turtle__vmLogo_Turtle4", None)
        self.__vmLogo_Turtle4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vmLogo_Point5"):
                    opp_val = getattr(item, "vmLogo_Point5", None)
                    
                    if opp_val == self:
                        setattr(item, "vmLogo_Point5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vmLogo_Point5"):
                    opp_val = getattr(item, "vmLogo_Point5", None)
                    
                    setattr(item, "vmLogo_Point5", self)
                    
