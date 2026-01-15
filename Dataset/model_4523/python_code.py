from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class vmlogo_Variable:

    def __init__(self, name: str, value: float, vmlogo_Variable: "vmlogo_StackFrame" = None):
        self.name = name
        self.value = value
        self.vmlogo_Variable = vmlogo_Variable
        
    @property
    def value(self) -> float:
        return self.__value

    @value.setter
    def value(self, value: float):
        self.__value = value

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def vmlogo_Variable(self):
        return self.__vmlogo_Variable

    @vmlogo_Variable.setter
    def vmlogo_Variable(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Variable__vmlogo_Variable", None)
        self.__vmlogo_Variable = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_StackFrame14"):
                opp_val = getattr(old_value, "vmlogo_StackFrame14", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_StackFrame14"):
                opp_val = getattr(value, "vmlogo_StackFrame14", None)
                if opp_val is None:
                    setattr(value, "vmlogo_StackFrame14", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class vmlogo_StackFrame:

    pass
class vmlogo_CallStack:

    pass
class vmlogo_Segment:

    pass
class vmlogo_Point:

    def __init__(self, x: float, y: float, vmlogo_Point: "vmlogo_Turtle" = None, vmlogo_Point7: "vmlogo_Segment" = None, vmlogo_Point10: "vmlogo_Segment" = None):
        self.x = x
        self.y = y
        self.vmlogo_Point = vmlogo_Point
        self.vmlogo_Point7 = vmlogo_Point7
        self.vmlogo_Point10 = vmlogo_Point10
        
    @property
    def x(self) -> float:
        return self.__x

    @x.setter
    def x(self, x: float):
        self.__x = x

    @property
    def y(self) -> float:
        return self.__y

    @y.setter
    def y(self, y: float):
        self.__y = y

    @property
    def vmlogo_Point7(self):
        return self.__vmlogo_Point7

    @vmlogo_Point7.setter
    def vmlogo_Point7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Point__vmlogo_Point7", None)
        self.__vmlogo_Point7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Segment6"):
                opp_val = getattr(old_value, "vmlogo_Segment6", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Segment6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Segment6"):
                opp_val = getattr(value, "vmlogo_Segment6", None)
                setattr(value, "vmlogo_Segment6", self)

    @property
    def vmlogo_Point(self):
        return self.__vmlogo_Point

    @vmlogo_Point.setter
    def vmlogo_Point(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Point__vmlogo_Point", None)
        self.__vmlogo_Point = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Turtle"):
                opp_val = getattr(old_value, "vmlogo_Turtle", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Turtle", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Turtle"):
                opp_val = getattr(value, "vmlogo_Turtle", None)
                setattr(value, "vmlogo_Turtle", self)

    @property
    def vmlogo_Point10(self):
        return self.__vmlogo_Point10

    @vmlogo_Point10.setter
    def vmlogo_Point10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Point__vmlogo_Point10", None)
        self.__vmlogo_Point10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Segment9"):
                opp_val = getattr(old_value, "vmlogo_Segment9", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Segment9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Segment9"):
                opp_val = getattr(value, "vmlogo_Segment9", None)
                setattr(value, "vmlogo_Segment9", self)

class vmlogo_Turtle:

    def __init__(self, heading: float, penUp: bool, vmlogo_Turtle: "vmlogo_Point" = None, vmlogo_Turtle2: set["vmlogo_Segment"] = None, vmlogo_Turtle4: "vmlogo_CallStack" = None):
        self.heading = heading
        self.penUp = penUp
        self.vmlogo_Turtle = vmlogo_Turtle
        self.vmlogo_Turtle2 = vmlogo_Turtle2 if vmlogo_Turtle2 is not None else set()
        self.vmlogo_Turtle4 = vmlogo_Turtle4
        
    @property
    def heading(self) -> float:
        return self.__heading

    @heading.setter
    def heading(self, heading: float):
        self.__heading = heading

    @property
    def penUp(self) -> bool:
        return self.__penUp

    @penUp.setter
    def penUp(self, penUp: bool):
        self.__penUp = penUp

    @property
    def vmlogo_Turtle4(self):
        return self.__vmlogo_Turtle4

    @vmlogo_Turtle4.setter
    def vmlogo_Turtle4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Turtle__vmlogo_Turtle4", None)
        self.__vmlogo_Turtle4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_CallStack"):
                opp_val = getattr(old_value, "vmlogo_CallStack", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_CallStack", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_CallStack"):
                opp_val = getattr(value, "vmlogo_CallStack", None)
                setattr(value, "vmlogo_CallStack", self)

    @property
    def vmlogo_Turtle(self):
        return self.__vmlogo_Turtle

    @vmlogo_Turtle.setter
    def vmlogo_Turtle(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Turtle__vmlogo_Turtle", None)
        self.__vmlogo_Turtle = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vmlogo_Point"):
                opp_val = getattr(old_value, "vmlogo_Point", None)
                if opp_val == self:
                    setattr(old_value, "vmlogo_Point", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vmlogo_Point"):
                opp_val = getattr(value, "vmlogo_Point", None)
                setattr(value, "vmlogo_Point", self)

    @property
    def vmlogo_Turtle2(self):
        return self.__vmlogo_Turtle2

    @vmlogo_Turtle2.setter
    def vmlogo_Turtle2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_vmlogo_Turtle__vmlogo_Turtle2", None)
        self.__vmlogo_Turtle2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "vmlogo_Segment"):
                    opp_val = getattr(item, "vmlogo_Segment", None)
                    
                    if opp_val == self:
                        setattr(item, "vmlogo_Segment", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "vmlogo_Segment"):
                    opp_val = getattr(item, "vmlogo_Segment", None)
                    
                    setattr(item, "vmlogo_Segment", self)
                    
