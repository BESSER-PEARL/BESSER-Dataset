from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class scheduleOfCourse_scheduleOfCourse:

    pass
class scheduleOfCourse_TopLevelSpace:

    def __init__(self, type: str, id: str, name: str, scheduleOfCourse_TopLevelSpace: "scheduleOfCourse_Room" = None):
        self.type = type
        self.id = id
        self.name = name
        self.scheduleOfCourse_TopLevelSpace = scheduleOfCourse_TopLevelSpace
        
        pass
    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def scheduleOfCourse_TopLevelSpace(self):
        return self.__scheduleOfCourse_TopLevelSpace

    @scheduleOfCourse_TopLevelSpace.setter
    def scheduleOfCourse_TopLevelSpace(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_TopLevelSpace__scheduleOfCourse_TopLevelSpace", None)
        self.__scheduleOfCourse_TopLevelSpace = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Room15"):
                opp_val = getattr(old_value, "scheduleOfCourse_Room15", None)
                if opp_val == self:
                    setattr(old_value, "scheduleOfCourse_Room15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Room15"):
                opp_val = getattr(value, "scheduleOfCourse_Room15", None)
                setattr(value, "scheduleOfCourse_Room15", self)

class scheduleOfCourse_Capacity:

    def __init__(self, normal: int, exam: int, scheduleOfCourse_Capacity: "scheduleOfCourse_Room" = None):
        self.normal = normal
        self.exam = exam
        self.scheduleOfCourse_Capacity = scheduleOfCourse_Capacity
        
        pass
    @property
    def normal(self):
        return self.__normal

    @normal.setter
    def normal(self, normal: int):
        self.__normal = normal


    @property
    def exam(self):
        return self.__exam

    @exam.setter
    def exam(self, exam: int):
        self.__exam = exam


    @property
    def scheduleOfCourse_Capacity(self):
        return self.__scheduleOfCourse_Capacity

    @scheduleOfCourse_Capacity.setter
    def scheduleOfCourse_Capacity(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Capacity__scheduleOfCourse_Capacity", None)
        self.__scheduleOfCourse_Capacity = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Room17"):
                opp_val = getattr(old_value, "scheduleOfCourse_Room17", None)
                if opp_val == self:
                    setattr(old_value, "scheduleOfCourse_Room17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Room17"):
                opp_val = getattr(value, "scheduleOfCourse_Room17", None)
                setattr(value, "scheduleOfCourse_Room17", self)

class scheduleOfCourse_CourseLoad:

    def __init__(self, type: str, totalQuantity: int, unitQuantity: int, scheduleOfCourse_CourseLoad: "scheduleOfCourse_scheduleOfCourse" = None):
        self.type = type
        self.totalQuantity = totalQuantity
        self.unitQuantity = unitQuantity
        self.scheduleOfCourse_CourseLoad = scheduleOfCourse_CourseLoad
        
        pass
    @property
    def totalQuantity(self):
        return self.__totalQuantity

    @totalQuantity.setter
    def totalQuantity(self, totalQuantity: int):
        self.__totalQuantity = totalQuantity


    @property
    def unitQuantity(self):
        return self.__unitQuantity

    @unitQuantity.setter
    def unitQuantity(self, unitQuantity: int):
        self.__unitQuantity = unitQuantity


    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def scheduleOfCourse_CourseLoad(self):
        return self.__scheduleOfCourse_CourseLoad

    @scheduleOfCourse_CourseLoad.setter
    def scheduleOfCourse_CourseLoad(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_CourseLoad__scheduleOfCourse_CourseLoad", None)
        self.__scheduleOfCourse_CourseLoad = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_scheduleOfCourse7"):
                opp_val = getattr(old_value, "scheduleOfCourse_scheduleOfCourse7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_scheduleOfCourse7"):
                opp_val = getattr(value, "scheduleOfCourse_scheduleOfCourse7", None)
                if opp_val is None:
                    setattr(value, "scheduleOfCourse_scheduleOfCourse7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scheduleOfCourse_LessonPeriod:

    def __init__(self, start: str, end: str, scheduleOfCourse_LessonPeriod: "scheduleOfCourse_scheduleOfCourse" = None):
        self.start = start
        self.end = end
        self.scheduleOfCourse_LessonPeriod = scheduleOfCourse_LessonPeriod
        
        pass
    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end


    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start


    @property
    def scheduleOfCourse_LessonPeriod(self):
        return self.__scheduleOfCourse_LessonPeriod

    @scheduleOfCourse_LessonPeriod.setter
    def scheduleOfCourse_LessonPeriod(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_LessonPeriod__scheduleOfCourse_LessonPeriod", None)
        self.__scheduleOfCourse_LessonPeriod = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_scheduleOfCourse"):
                opp_val = getattr(old_value, "scheduleOfCourse_scheduleOfCourse", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_scheduleOfCourse"):
                opp_val = getattr(value, "scheduleOfCourse_scheduleOfCourse", None)
                if opp_val is None:
                    setattr(value, "scheduleOfCourse_scheduleOfCourse", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scheduleOfCourse_Room:

    def __init__(self, type: str, id: str, name: str, description: str, scheduleOfCourse_Room: "scheduleOfCourse_Shift" = None, scheduleOfCourse_Room13: "scheduleOfCourse_Lesson" = None, scheduleOfCourse_Room15: "scheduleOfCourse_TopLevelSpace" = None, scheduleOfCourse_Room17: "scheduleOfCourse_Capacity" = None):
        self.type = type
        self.id = id
        self.name = name
        self.description = description
        self.scheduleOfCourse_Room = scheduleOfCourse_Room
        self.scheduleOfCourse_Room13 = scheduleOfCourse_Room13
        self.scheduleOfCourse_Room15 = scheduleOfCourse_Room15
        self.scheduleOfCourse_Room17 = scheduleOfCourse_Room17
        
        pass
    @property
    def type(self):
        return self.__type

    @type.setter
    def type(self, type: str):
        self.__type = type


    @property
    def id(self):
        return self.__id

    @id.setter
    def id(self, id: str):
        self.__id = id


    @property
    def description(self):
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def scheduleOfCourse_Room13(self):
        return self.__scheduleOfCourse_Room13

    @scheduleOfCourse_Room13.setter
    def scheduleOfCourse_Room13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Room__scheduleOfCourse_Room13", None)
        self.__scheduleOfCourse_Room13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Lesson12"):
                opp_val = getattr(old_value, "scheduleOfCourse_Lesson12", None)
                if opp_val == self:
                    setattr(old_value, "scheduleOfCourse_Lesson12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Lesson12"):
                opp_val = getattr(value, "scheduleOfCourse_Lesson12", None)
                setattr(value, "scheduleOfCourse_Lesson12", self)

    @property
    def scheduleOfCourse_Room(self):
        return self.__scheduleOfCourse_Room

    @scheduleOfCourse_Room.setter
    def scheduleOfCourse_Room(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Room__scheduleOfCourse_Room", None)
        self.__scheduleOfCourse_Room = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Shift4"):
                opp_val = getattr(old_value, "scheduleOfCourse_Shift4", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Shift4"):
                opp_val = getattr(value, "scheduleOfCourse_Shift4", None)
                if opp_val is None:
                    setattr(value, "scheduleOfCourse_Shift4", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scheduleOfCourse_Room17(self):
        return self.__scheduleOfCourse_Room17

    @scheduleOfCourse_Room17.setter
    def scheduleOfCourse_Room17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Room__scheduleOfCourse_Room17", None)
        self.__scheduleOfCourse_Room17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Capacity"):
                opp_val = getattr(old_value, "scheduleOfCourse_Capacity", None)
                if opp_val == self:
                    setattr(old_value, "scheduleOfCourse_Capacity", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Capacity"):
                opp_val = getattr(value, "scheduleOfCourse_Capacity", None)
                setattr(value, "scheduleOfCourse_Capacity", self)

    @property
    def scheduleOfCourse_Room15(self):
        return self.__scheduleOfCourse_Room15

    @scheduleOfCourse_Room15.setter
    def scheduleOfCourse_Room15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Room__scheduleOfCourse_Room15", None)
        self.__scheduleOfCourse_Room15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_TopLevelSpace"):
                opp_val = getattr(old_value, "scheduleOfCourse_TopLevelSpace", None)
                if opp_val == self:
                    setattr(old_value, "scheduleOfCourse_TopLevelSpace", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_TopLevelSpace"):
                opp_val = getattr(value, "scheduleOfCourse_TopLevelSpace", None)
                setattr(value, "scheduleOfCourse_TopLevelSpace", self)

class scheduleOfCourse_Lesson:

    def __init__(self, start: str, end: str, scheduleOfCourse_Lesson: "scheduleOfCourse_Shift" = None, scheduleOfCourse_Lesson12: "scheduleOfCourse_Room" = None):
        self.start = start
        self.end = end
        self.scheduleOfCourse_Lesson = scheduleOfCourse_Lesson
        self.scheduleOfCourse_Lesson12 = scheduleOfCourse_Lesson12
        
        pass
    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, end: str):
        self.__end = end


    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, start: str):
        self.__start = start


    @property
    def scheduleOfCourse_Lesson12(self):
        return self.__scheduleOfCourse_Lesson12

    @scheduleOfCourse_Lesson12.setter
    def scheduleOfCourse_Lesson12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Lesson__scheduleOfCourse_Lesson12", None)
        self.__scheduleOfCourse_Lesson12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Room13"):
                opp_val = getattr(old_value, "scheduleOfCourse_Room13", None)
                if opp_val == self:
                    setattr(old_value, "scheduleOfCourse_Room13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Room13"):
                opp_val = getattr(value, "scheduleOfCourse_Room13", None)
                setattr(value, "scheduleOfCourse_Room13", self)

    @property
    def scheduleOfCourse_Lesson(self):
        return self.__scheduleOfCourse_Lesson

    @scheduleOfCourse_Lesson.setter
    def scheduleOfCourse_Lesson(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Lesson__scheduleOfCourse_Lesson", None)
        self.__scheduleOfCourse_Lesson = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Shift2"):
                opp_val = getattr(old_value, "scheduleOfCourse_Shift2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Shift2"):
                opp_val = getattr(value, "scheduleOfCourse_Shift2", None)
                if opp_val is None:
                    setattr(value, "scheduleOfCourse_Shift2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class scheduleOfCourse_Occupation:

    def __init__(self, current: int, max: int, scheduleOfCourse_Occupation: "scheduleOfCourse_Shift" = None):
        self.current = current
        self.max = max
        self.scheduleOfCourse_Occupation = scheduleOfCourse_Occupation
        
        pass
    @property
    def max(self):
        return self.__max

    @max.setter
    def max(self, max: int):
        self.__max = max


    @property
    def current(self):
        return self.__current

    @current.setter
    def current(self, current: int):
        self.__current = current


    @property
    def scheduleOfCourse_Occupation(self):
        return self.__scheduleOfCourse_Occupation

    @scheduleOfCourse_Occupation.setter
    def scheduleOfCourse_Occupation(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Occupation__scheduleOfCourse_Occupation", None)
        self.__scheduleOfCourse_Occupation = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Shift"):
                opp_val = getattr(old_value, "scheduleOfCourse_Shift", None)
                if opp_val == self:
                    setattr(old_value, "scheduleOfCourse_Shift", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Shift"):
                opp_val = getattr(value, "scheduleOfCourse_Shift", None)
                setattr(value, "scheduleOfCourse_Shift", self)

class scheduleOfCourse_Shift:

    def __init__(self, name: str, types: str, scheduleOfCourse_Shift: "scheduleOfCourse_Occupation" = None, scheduleOfCourse_Shift2: set["scheduleOfCourse_Lesson"] = None, scheduleOfCourse_Shift4: set["scheduleOfCourse_Room"] = None, scheduleOfCourse_Shift10: "scheduleOfCourse_scheduleOfCourse" = None):
        self.name = name
        self.types = types
        self.scheduleOfCourse_Shift = scheduleOfCourse_Shift
        self.scheduleOfCourse_Shift2 = scheduleOfCourse_Shift2 if scheduleOfCourse_Shift2 is not None else set()
        self.scheduleOfCourse_Shift4 = scheduleOfCourse_Shift4 if scheduleOfCourse_Shift4 is not None else set()
        self.scheduleOfCourse_Shift10 = scheduleOfCourse_Shift10
        
        pass
    @property
    def types(self):
        return self.__types

    @types.setter
    def types(self, types: str):
        self.__types = types


    @property
    def name(self):
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name


    @property
    def scheduleOfCourse_Shift4(self):
        return self.__scheduleOfCourse_Shift4

    @scheduleOfCourse_Shift4.setter
    def scheduleOfCourse_Shift4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Shift__scheduleOfCourse_Shift4", None)
        self.__scheduleOfCourse_Shift4 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scheduleOfCourse_Room"):
                    opp_val = getattr(item, "scheduleOfCourse_Room", None)
                    
                    if opp_val == self:
                        setattr(item, "scheduleOfCourse_Room", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scheduleOfCourse_Room"):
                    opp_val = getattr(item, "scheduleOfCourse_Room", None)
                    
                    setattr(item, "scheduleOfCourse_Room", self)
                    

    @property
    def scheduleOfCourse_Shift(self):
        return self.__scheduleOfCourse_Shift

    @scheduleOfCourse_Shift.setter
    def scheduleOfCourse_Shift(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Shift__scheduleOfCourse_Shift", None)
        self.__scheduleOfCourse_Shift = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_Occupation"):
                opp_val = getattr(old_value, "scheduleOfCourse_Occupation", None)
                if opp_val == self:
                    setattr(old_value, "scheduleOfCourse_Occupation", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_Occupation"):
                opp_val = getattr(value, "scheduleOfCourse_Occupation", None)
                setattr(value, "scheduleOfCourse_Occupation", self)

    @property
    def scheduleOfCourse_Shift10(self):
        return self.__scheduleOfCourse_Shift10

    @scheduleOfCourse_Shift10.setter
    def scheduleOfCourse_Shift10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Shift__scheduleOfCourse_Shift10", None)
        self.__scheduleOfCourse_Shift10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "scheduleOfCourse_scheduleOfCourse9"):
                opp_val = getattr(old_value, "scheduleOfCourse_scheduleOfCourse9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "scheduleOfCourse_scheduleOfCourse9"):
                opp_val = getattr(value, "scheduleOfCourse_scheduleOfCourse9", None)
                if opp_val is None:
                    setattr(value, "scheduleOfCourse_scheduleOfCourse9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def scheduleOfCourse_Shift2(self):
        return self.__scheduleOfCourse_Shift2

    @scheduleOfCourse_Shift2.setter
    def scheduleOfCourse_Shift2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_scheduleOfCourse_Shift__scheduleOfCourse_Shift2", None)
        self.__scheduleOfCourse_Shift2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "scheduleOfCourse_Lesson"):
                    opp_val = getattr(item, "scheduleOfCourse_Lesson", None)
                    
                    if opp_val == self:
                        setattr(item, "scheduleOfCourse_Lesson", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "scheduleOfCourse_Lesson"):
                    opp_val = getattr(item, "scheduleOfCourse_Lesson", None)
                    
                    setattr(item, "scheduleOfCourse_Lesson", self)
                    
