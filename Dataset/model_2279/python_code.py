from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class fenix_Capacity:

    def __init__(self, normal: int, exam: int, fenix_Capacity: "fenix_CourseLoad" = None):
        self.normal = normal
        self.exam = exam
        self.fenix_Capacity = fenix_Capacity
        
    @property
    def exam(self) -> int:
        return self.__exam

    @exam.setter
    def exam(self, exam: int):
        self.__exam = exam

    @property
    def normal(self) -> int:
        return self.__normal

    @normal.setter
    def normal(self, normal: int):
        self.__normal = normal

    @property
    def fenix_Capacity(self):
        return self.__fenix_Capacity

    @fenix_Capacity.setter
    def fenix_Capacity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_Capacity__fenix_Capacity", None)
        self.__fenix_Capacity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_CourseLoad12"):
                opp_val = getattr(old_value, "fenix_CourseLoad12", None)
                if opp_val == self:
                    setattr(old_value, "fenix_CourseLoad12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_CourseLoad12"):
                opp_val = getattr(value, "fenix_CourseLoad12", None)
                setattr(value, "fenix_CourseLoad12", self)

class fenix_scheduleOfCourse:

    pass
class fenix_CourseLoad:

    def __init__(self, type: str, totalQuantity: int, id: str, name: str, description: str, unitQuantity: int, fenix_CourseLoad: "fenix_Shift" = None, fenix_CourseLoad7: "fenix_LessonPeriod" = None, fenix_CourseLoad10: "fenix_CourseLoad" = None, fenix_CourseLoad8: "fenix_CourseLoad" = None, fenix_CourseLoad12: "fenix_Capacity" = None, fenix_CourseLoad17: "fenix_scheduleOfCourse" = None):
        self.type = type
        self.totalQuantity = totalQuantity
        self.id = id
        self.name = name
        self.description = description
        self.unitQuantity = unitQuantity
        self.fenix_CourseLoad = fenix_CourseLoad
        self.fenix_CourseLoad7 = fenix_CourseLoad7
        self.fenix_CourseLoad10 = fenix_CourseLoad10
        self.fenix_CourseLoad8 = fenix_CourseLoad8
        self.fenix_CourseLoad12 = fenix_CourseLoad12
        self.fenix_CourseLoad17 = fenix_CourseLoad17
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def unitQuantity(self) -> int:
        return self.__unitQuantity

    @unitQuantity.setter
    def unitQuantity(self, unitQuantity: int):
        self.__unitQuantity = unitQuantity

    @property
    def type(self) -> str:
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def id(self) -> str:
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id

    @property
    def totalQuantity(self) -> int:
        return self.__totalQuantity

    @totalQuantity.setter
    def totalQuantity(self, totalQuantity: int):
        self.__totalQuantity = totalQuantity

    @property
    def fenix_CourseLoad12(self):
        return self.__fenix_CourseLoad12

    @fenix_CourseLoad12.setter
    def fenix_CourseLoad12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_CourseLoad__fenix_CourseLoad12", None)
        self.__fenix_CourseLoad12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_Capacity"):
                opp_val = getattr(old_value, "fenix_Capacity", None)
                if opp_val == self:
                    setattr(old_value, "fenix_Capacity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_Capacity"):
                opp_val = getattr(value, "fenix_Capacity", None)
                setattr(value, "fenix_Capacity", self)

    @property
    def fenix_CourseLoad(self):
        return self.__fenix_CourseLoad

    @fenix_CourseLoad.setter
    def fenix_CourseLoad(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_CourseLoad__fenix_CourseLoad", None)
        self.__fenix_CourseLoad = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_Shift4"):
                opp_val = getattr(old_value, "fenix_Shift4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_Shift4"):
                opp_val = getattr(value, "fenix_Shift4", None)
                if opp_val is None:
                    setattr(value, "fenix_Shift4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fenix_CourseLoad7(self):
        return self.__fenix_CourseLoad7

    @fenix_CourseLoad7.setter
    def fenix_CourseLoad7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_CourseLoad__fenix_CourseLoad7", None)
        self.__fenix_CourseLoad7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_LessonPeriod6"):
                opp_val = getattr(old_value, "fenix_LessonPeriod6", None)
                if opp_val == self:
                    setattr(old_value, "fenix_LessonPeriod6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_LessonPeriod6"):
                opp_val = getattr(value, "fenix_LessonPeriod6", None)
                setattr(value, "fenix_LessonPeriod6", self)

    @property
    def fenix_CourseLoad8(self):
        return self.__fenix_CourseLoad8

    @fenix_CourseLoad8.setter
    def fenix_CourseLoad8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_CourseLoad__fenix_CourseLoad8", None)
        self.__fenix_CourseLoad8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_CourseLoad10"):
                opp_val = getattr(old_value, "fenix_CourseLoad10", None)
                if opp_val == self:
                    setattr(old_value, "fenix_CourseLoad10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_CourseLoad10"):
                opp_val = getattr(value, "fenix_CourseLoad10", None)
                setattr(value, "fenix_CourseLoad10", self)

    @property
    def fenix_CourseLoad17(self):
        return self.__fenix_CourseLoad17

    @fenix_CourseLoad17.setter
    def fenix_CourseLoad17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_CourseLoad__fenix_CourseLoad17", None)
        self.__fenix_CourseLoad17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_scheduleOfCourse16"):
                opp_val = getattr(old_value, "fenix_scheduleOfCourse16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_scheduleOfCourse16"):
                opp_val = getattr(value, "fenix_scheduleOfCourse16", None)
                if opp_val is None:
                    setattr(value, "fenix_scheduleOfCourse16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fenix_CourseLoad10(self):
        return self.__fenix_CourseLoad10

    @fenix_CourseLoad10.setter
    def fenix_CourseLoad10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_CourseLoad__fenix_CourseLoad10", None)
        self.__fenix_CourseLoad10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_CourseLoad8"):
                opp_val = getattr(old_value, "fenix_CourseLoad8", None)
                if opp_val == self:
                    setattr(old_value, "fenix_CourseLoad8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_CourseLoad8"):
                opp_val = getattr(value, "fenix_CourseLoad8", None)
                setattr(value, "fenix_CourseLoad8", self)

class fenix_Shift:

    def __init__(self, types: str, name: str, fenix_Shift: "fenix_Occupation" = None, fenix_Shift2: set["fenix_LessonPeriod"] = None, fenix_Shift4: set["fenix_CourseLoad"] = None, fenix_Shift20: "fenix_scheduleOfCourse" = None):
        self.types = types
        self.name = name
        self.fenix_Shift = fenix_Shift
        self.fenix_Shift2 = fenix_Shift2 if fenix_Shift2 is not None else set()
        self.fenix_Shift4 = fenix_Shift4 if fenix_Shift4 is not None else set()
        self.fenix_Shift20 = fenix_Shift20
        
    @property
    def types(self) -> str:
        return self.__types

    @types.setter
    def types(self, types: str):
        self.__types = types

    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def fenix_Shift(self):
        return self.__fenix_Shift

    @fenix_Shift.setter
    def fenix_Shift(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_Shift__fenix_Shift", None)
        self.__fenix_Shift = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_Occupation"):
                opp_val = getattr(old_value, "fenix_Occupation", None)
                if opp_val == self:
                    setattr(old_value, "fenix_Occupation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_Occupation"):
                opp_val = getattr(value, "fenix_Occupation", None)
                setattr(value, "fenix_Occupation", self)

    @property
    def fenix_Shift2(self):
        return self.__fenix_Shift2

    @fenix_Shift2.setter
    def fenix_Shift2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_Shift__fenix_Shift2", None)
        self.__fenix_Shift2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fenix_LessonPeriod"):
                    opp_val = getattr(item, "fenix_LessonPeriod", None)
                    
                    if opp_val == self:
                        setattr(item, "fenix_LessonPeriod", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fenix_LessonPeriod"):
                    opp_val = getattr(item, "fenix_LessonPeriod", None)
                    
                    setattr(item, "fenix_LessonPeriod", self)
                    

    @property
    def fenix_Shift20(self):
        return self.__fenix_Shift20

    @fenix_Shift20.setter
    def fenix_Shift20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_Shift__fenix_Shift20", None)
        self.__fenix_Shift20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_scheduleOfCourse19"):
                opp_val = getattr(old_value, "fenix_scheduleOfCourse19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_scheduleOfCourse19"):
                opp_val = getattr(value, "fenix_scheduleOfCourse19", None)
                if opp_val is None:
                    setattr(value, "fenix_scheduleOfCourse19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fenix_Shift4(self):
        return self.__fenix_Shift4

    @fenix_Shift4.setter
    def fenix_Shift4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_Shift__fenix_Shift4", None)
        self.__fenix_Shift4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "fenix_CourseLoad"):
                    opp_val = getattr(item, "fenix_CourseLoad", None)
                    
                    if opp_val == self:
                        setattr(item, "fenix_CourseLoad", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "fenix_CourseLoad"):
                    opp_val = getattr(item, "fenix_CourseLoad", None)
                    
                    setattr(item, "fenix_CourseLoad", self)
                    

class fenix_LessonPeriod:

    def __init__(self, start: str, end: str, fenix_LessonPeriod: "fenix_Shift" = None, fenix_LessonPeriod6: "fenix_CourseLoad" = None, fenix_LessonPeriod14: "fenix_scheduleOfCourse" = None):
        self.start = start
        self.end = end
        self.fenix_LessonPeriod = fenix_LessonPeriod
        self.fenix_LessonPeriod6 = fenix_LessonPeriod6
        self.fenix_LessonPeriod14 = fenix_LessonPeriod14
        
    @property
    def start(self) -> str:
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start

    @property
    def end(self) -> str:
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end

    @property
    def fenix_LessonPeriod6(self):
        return self.__fenix_LessonPeriod6

    @fenix_LessonPeriod6.setter
    def fenix_LessonPeriod6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_LessonPeriod__fenix_LessonPeriod6", None)
        self.__fenix_LessonPeriod6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_CourseLoad7"):
                opp_val = getattr(old_value, "fenix_CourseLoad7", None)
                if opp_val == self:
                    setattr(old_value, "fenix_CourseLoad7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_CourseLoad7"):
                opp_val = getattr(value, "fenix_CourseLoad7", None)
                setattr(value, "fenix_CourseLoad7", self)

    @property
    def fenix_LessonPeriod14(self):
        return self.__fenix_LessonPeriod14

    @fenix_LessonPeriod14.setter
    def fenix_LessonPeriod14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_LessonPeriod__fenix_LessonPeriod14", None)
        self.__fenix_LessonPeriod14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_scheduleOfCourse"):
                opp_val = getattr(old_value, "fenix_scheduleOfCourse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_scheduleOfCourse"):
                opp_val = getattr(value, "fenix_scheduleOfCourse", None)
                if opp_val is None:
                    setattr(value, "fenix_scheduleOfCourse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def fenix_LessonPeriod(self):
        return self.__fenix_LessonPeriod

    @fenix_LessonPeriod.setter
    def fenix_LessonPeriod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_LessonPeriod__fenix_LessonPeriod", None)
        self.__fenix_LessonPeriod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_Shift2"):
                opp_val = getattr(old_value, "fenix_Shift2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_Shift2"):
                opp_val = getattr(value, "fenix_Shift2", None)
                if opp_val is None:
                    setattr(value, "fenix_Shift2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class fenix_Occupation:

    def __init__(self, current: int, max: int, fenix_Occupation: "fenix_Shift" = None):
        self.current = current
        self.max = max
        self.fenix_Occupation = fenix_Occupation
        
    @property
    def max(self) -> int:
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max

    @property
    def current(self) -> int:
        return self.__current

    @current.setter
    def current(self, current: int):
        self.__current = current

    @property
    def fenix_Occupation(self):
        return self.__fenix_Occupation

    @fenix_Occupation.setter
    def fenix_Occupation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_fenix_Occupation__fenix_Occupation", None)
        self.__fenix_Occupation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "fenix_Shift"):
                opp_val = getattr(old_value, "fenix_Shift", None)
                if opp_val == self:
                    setattr(old_value, "fenix_Shift", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "fenix_Shift"):
                opp_val = getattr(value, "fenix_Shift", None)
                setattr(value, "fenix_Shift", self)
