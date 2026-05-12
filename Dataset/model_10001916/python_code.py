from __future__ import annotations
from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class bo(Enum):
    pass

############################################
# Definition of Classes
############################################










class course:

    def __init__(self, course_name: str, course_id: int_Interface, teached_by: str, placed_on: str, student43: "student" = None):
        self.course_name = course_name
        self.course_id = course_id
        self.teached_by = teached_by
        self.placed_on = placed_on
        self.student43 = student43
        
        pass
    @property
    def teached_by(self):
        return self.__teached_by
    @teached_by.setter
    def teached_by(self, teached_by: str):
        self.__teached_by = teached_by

    @property
    def course_name(self):
        return self.__course_name
    @course_name.setter
    def course_name(self, course_name: str):
        self.__course_name = course_name

    @property
    def course_id(self):
        return self.__course_id
    @course_id.setter
    def course_id(self, course_id: int_Interface):
        self.__course_id = course_id

    @property
    def placed_on(self):
        return self.__placed_on
    @placed_on.setter
    def placed_on(self, placed_on: str):
        self.__placed_on = placed_on

    @property
    def student43(self):
        return self.__student43
    @student43.setter
    def student43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_course__student43", None)
        self.__student43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "course42"):
                opp_val = getattr(old_value, "course42", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "course42"):
                opp_val = getattr(value, "course42", None)
                if opp_val is None:
                    setattr(value, "course42", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Billing_system:

    def __init__(self, course_fees: int_Interface, course_status: str, student51: set["student"] = None):
        self.course_fees = course_fees
        self.course_status = course_status
        self.student51 = student51 if student51 is not None else set()
        
        pass
    @property
    def course_fees(self):
        return self.__course_fees
    @course_fees.setter
    def course_fees(self, course_fees: int_Interface):
        self.__course_fees = course_fees

    @property
    def course_status(self):
        return self.__course_status
    @course_status.setter
    def course_status(self, course_status: str):
        self.__course_status = course_status

    @property
    def student51(self):
        return self.__student51
    @student51.setter
    def student51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Billing_system__student51", None)
        self.__student51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "billing_system50"):
                    opp_val = getattr(item, "billing_system50", None)
                    
                    if opp_val == self:
                        setattr(item, "billing_system50", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "billing_system50"):
                    opp_val = getattr(item, "billing_system50", None)
                    
                    setattr(item, "billing_system50", self)
                    



class Register:

    def __init__(self, student_id: student, student_name: student, professer_id: Professor, professor_name: Professor, course_id: str, course_name: str, student47: set["student"] = None, professor49: set["Professor"] = None):
        self.student_id = student_id
        self.student_name = student_name
        self.professer_id = professer_id
        self.professor_name = professor_name
        self.course_id = course_id
        self.course_name = course_name
        self.student47 = student47 if student47 is not None else set()
        self.professor49 = professor49 if professor49 is not None else set()
        
        pass
    @property
    def professer_id(self):
        return self.__professer_id
    @professer_id.setter
    def professer_id(self, professer_id: Professor):
        self.__professer_id = professer_id

    @property
    def course_id(self):
        return self.__course_id
    @course_id.setter
    def course_id(self, course_id: str):
        self.__course_id = course_id

    @property
    def student_name(self):
        return self.__student_name
    @student_name.setter
    def student_name(self, student_name: student):
        self.__student_name = student_name

    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, student_id: student):
        self.__student_id = student_id

    @property
    def course_name(self):
        return self.__course_name
    @course_name.setter
    def course_name(self, course_name: str):
        self.__course_name = course_name

    @property
    def professor_name(self):
        return self.__professor_name
    @professor_name.setter
    def professor_name(self, professor_name: Professor):
        self.__professor_name = professor_name

    @property
    def professor49(self):
        return self.__professor49
    @professor49.setter
    def professor49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Register__professor49", None)
        self.__professor49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "register48"):
                    opp_val = getattr(item, "register48", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "register48"):
                    opp_val = getattr(item, "register48", None)
                    
                    if opp_val is None:
                        setattr(item, "register48", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def student47(self):
        return self.__student47
    @student47.setter
    def student47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Register__student47", None)
        self.__student47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "register46"):
                    opp_val = getattr(item, "register46", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "register46"):
                    opp_val = getattr(item, "register46", None)
                    
                    if opp_val is None:
                        setattr(item, "register46", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Professor:

    def __init__(self, course_name: str, course_id: int_Interface, professor_name: str, professor_id: int_Interface, register48: set["Register"] = None, student45: set["student"] = None):
        self.course_name = course_name
        self.course_id = course_id
        self.professor_name = professor_name
        self.professor_id = professor_id
        self.register48 = register48 if register48 is not None else set()
        self.student45 = student45 if student45 is not None else set()
        
        pass
    @property
    def professor_name(self):
        return self.__professor_name
    @professor_name.setter
    def professor_name(self, professor_name: str):
        self.__professor_name = professor_name

    @property
    def course_name(self):
        return self.__course_name
    @course_name.setter
    def course_name(self, course_name: str):
        self.__course_name = course_name

    @property
    def professor_id(self):
        return self.__professor_id
    @professor_id.setter
    def professor_id(self, professor_id: int_Interface):
        self.__professor_id = professor_id

    @property
    def course_id(self):
        return self.__course_id
    @course_id.setter
    def course_id(self, course_id: int_Interface):
        self.__course_id = course_id

    @property
    def register48(self):
        return self.__register48
    @register48.setter
    def register48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Professor__register48", None)
        self.__register48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "professor49"):
                    opp_val = getattr(item, "professor49", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "professor49"):
                    opp_val = getattr(item, "professor49", None)
                    
                    if opp_val is None:
                        setattr(item, "professor49", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def student45(self):
        return self.__student45
    @student45.setter
    def student45(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Professor__student45", None)
        self.__student45 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "professor44"):
                    opp_val = getattr(item, "professor44", None)
                    
                    if opp_val == self:
                        setattr(item, "professor44", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "professor44"):
                    opp_val = getattr(item, "professor44", None)
                    
                    setattr(item, "professor44", self)
                    



class student:

    def __init__(self, student_id: int_Interface, student_name: str, no_of_courses: int_Interface, register46: set["Register"] = None, billing_system50: "Billing_system" = None, course42: set["course"] = None, professor44: "Professor" = None):
        self.student_id = student_id
        self.student_name = student_name
        self.no_of_courses = no_of_courses
        self.register46 = register46 if register46 is not None else set()
        self.billing_system50 = billing_system50
        self.course42 = course42 if course42 is not None else set()
        self.professor44 = professor44
        
        pass
    @property
    def student_id(self):
        return self.__student_id
    @student_id.setter
    def student_id(self, student_id: int_Interface):
        self.__student_id = student_id

    @property
    def no_of_courses(self):
        return self.__no_of_courses
    @no_of_courses.setter
    def no_of_courses(self, no_of_courses: int_Interface):
        self.__no_of_courses = no_of_courses

    @property
    def student_name(self):
        return self.__student_name
    @student_name.setter
    def student_name(self, student_name: str):
        self.__student_name = student_name

    @property
    def professor44(self):
        return self.__professor44
    @professor44.setter
    def professor44(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__professor44", None)
        self.__professor44 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student45"):
                opp_val = getattr(old_value, "student45", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student45"):
                opp_val = getattr(value, "student45", None)
                if opp_val is None:
                    setattr(value, "student45", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def register46(self):
        return self.__register46
    @register46.setter
    def register46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__register46", None)
        self.__register46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student47"):
                    opp_val = getattr(item, "student47", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student47"):
                    opp_val = getattr(item, "student47", None)
                    
                    if opp_val is None:
                        setattr(item, "student47", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def billing_system50(self):
        return self.__billing_system50
    @billing_system50.setter
    def billing_system50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__billing_system50", None)
        self.__billing_system50 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "student51"):
                opp_val = getattr(old_value, "student51", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "student51"):
                opp_val = getattr(value, "student51", None)
                if opp_val is None:
                    setattr(value, "student51", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def course42(self):
        return self.__course42
    @course42.setter
    def course42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_student__course42", None)
        self.__course42 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student43"):
                    opp_val = getattr(item, "student43", None)
                    
                    if opp_val == self:
                        setattr(item, "student43", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student43"):
                    opp_val = getattr(item, "student43", None)
                    
                    setattr(item, "student43", self)
                    



class kiosk1:

    def __init__(self, check_in: Passenger, passenger40: "Passenger" = None):
        self.check_in = check_in
        self.passenger40 = passenger40
        
        pass
    @property
    def check_in(self):
        return self.__check_in
    @check_in.setter
    def check_in(self, check_in: Passenger):
        self.__check_in = check_in

    @property
    def passenger40(self):
        return self.__passenger40
    @passenger40.setter
    def passenger40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kiosk1__passenger40", None)
        self.__passenger40 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kiosk41"):
                opp_val = getattr(old_value, "kiosk41", None)
                if opp_val == self:
                    setattr(old_value, "kiosk41", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kiosk41"):
                opp_val = getattr(value, "kiosk41", None)
                setattr(value, "kiosk41", self)



class individual:

    def __init__(self, pass1: Passenger, booking_clerk36: "booking_clerk" = None, passenger34: "Passenger" = None):
        self.pass1 = pass1
        self.booking_clerk36 = booking_clerk36
        self.passenger34 = passenger34
        
        pass
    @property
    def pass1(self):
        return self.__pass1
    @pass1.setter
    def pass1(self, pass1: Passenger):
        self.__pass1 = pass1

    @property
    def booking_clerk36(self):
        return self.__booking_clerk36
    @booking_clerk36.setter
    def booking_clerk36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_individual__booking_clerk36", None)
        self.__booking_clerk36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "individual37"):
                opp_val = getattr(old_value, "individual37", None)
                if opp_val == self:
                    setattr(old_value, "individual37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "individual37"):
                opp_val = getattr(value, "individual37", None)
                setattr(value, "individual37", self)

    @property
    def passenger34(self):
        return self.__passenger34
    @passenger34.setter
    def passenger34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_individual__passenger34", None)
        self.__passenger34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "individual35"):
                opp_val = getattr(old_value, "individual35", None)
                if opp_val == self:
                    setattr(old_value, "individual35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "individual35"):
                opp_val = getattr(value, "individual35", None)
                setattr(value, "individual35", self)



class Groups:

    def __init__(self, passenger_amount: int_Interface, names: str, id: Passenger, booking_clerk38: "booking_clerk" = None, passenger33: "Passenger" = None):
        self.passenger_amount = passenger_amount
        self.names = names
        self.id = id
        self.booking_clerk38 = booking_clerk38
        self.passenger33 = passenger33
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: Passenger):
        self.__id = id

    @property
    def passenger_amount(self):
        return self.__passenger_amount
    @passenger_amount.setter
    def passenger_amount(self, passenger_amount: int_Interface):
        self.__passenger_amount = passenger_amount

    @property
    def names(self):
        return self.__names
    @names.setter
    def names(self, names: str):
        self.__names = names

    @property
    def booking_clerk38(self):
        return self.__booking_clerk38
    @booking_clerk38.setter
    def booking_clerk38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Groups__booking_clerk38", None)
        self.__booking_clerk38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups39"):
                opp_val = getattr(old_value, "groups39", None)
                if opp_val == self:
                    setattr(old_value, "groups39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups39"):
                opp_val = getattr(value, "groups39", None)
                setattr(value, "groups39", self)

    @property
    def passenger33(self):
        return self.__passenger33
    @passenger33.setter
    def passenger33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Groups__passenger33", None)
        self.__passenger33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups32"):
                opp_val = getattr(old_value, "groups32", None)
                if opp_val == self:
                    setattr(old_value, "groups32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups32"):
                opp_val = getattr(value, "groups32", None)
                setattr(value, "groups32", self)



class booking_clerk:

    pass


class Passenger:

    def __init__(self, check_in: bool, pass1: str, baggage: int_Interface, id1: int_Interface, kiosk41: "kiosk1" = None, booking_clerk30: set["booking_clerk"] = None, groups32: "Groups" = None, individual35: "individual" = None):
        self.check_in = check_in
        self.pass1 = pass1
        self.baggage = baggage
        self.id1 = id1
        self.kiosk41 = kiosk41
        self.booking_clerk30 = booking_clerk30 if booking_clerk30 is not None else set()
        self.groups32 = groups32
        self.individual35 = individual35
        
        pass
    @property
    def pass1(self):
        return self.__pass
    @pass1.setter
    def pass1(self, pass1: str):
        self.__pass = pass1

    @property
    def baggage(self):
        return self.__baggage
    @baggage.setter
    def baggage(self, baggage: int_Interface):
        self.__baggage = baggage

    @property
    def check_in(self):
        return self.__check_in
    @check_in.setter
    def check_in(self, check_in: bool):
        self.__check_in = check_in

    @property
    def id1(self):
        return self.__id1
    @id1.setter
    def id1(self, id1: int_Interface):
        self.__id1 = id1

    @property
    def individual35(self):
        return self.__individual35
    @individual35.setter
    def individual35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passenger__individual35", None)
        self.__individual35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passenger34"):
                opp_val = getattr(old_value, "passenger34", None)
                if opp_val == self:
                    setattr(old_value, "passenger34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passenger34"):
                opp_val = getattr(value, "passenger34", None)
                setattr(value, "passenger34", self)

    @property
    def groups32(self):
        return self.__groups32
    @groups32.setter
    def groups32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passenger__groups32", None)
        self.__groups32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passenger33"):
                opp_val = getattr(old_value, "passenger33", None)
                if opp_val == self:
                    setattr(old_value, "passenger33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passenger33"):
                opp_val = getattr(value, "passenger33", None)
                setattr(value, "passenger33", self)

    @property
    def kiosk41(self):
        return self.__kiosk41
    @kiosk41.setter
    def kiosk41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passenger__kiosk41", None)
        self.__kiosk41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "passenger40"):
                opp_val = getattr(old_value, "passenger40", None)
                if opp_val == self:
                    setattr(old_value, "passenger40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "passenger40"):
                opp_val = getattr(value, "passenger40", None)
                setattr(value, "passenger40", self)

    @property
    def booking_clerk30(self):
        return self.__booking_clerk30
    @booking_clerk30.setter
    def booking_clerk30(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Passenger__booking_clerk30", None)
        self.__booking_clerk30 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "passenger31"):
                    opp_val = getattr(item, "passenger31", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "passenger31"):
                    opp_val = getattr(item, "passenger31", None)
                    
                    if opp_val is None:
                        setattr(item, "passenger31", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class teacher:

    pass


class Parents:

    pass


class School_administrator:

    pass


class attendance_manager:

    def __init__(self, identify_students: str, student_names: str, Excuse_of_Absenties: str, students19: set["students"] = None, teacher20: "teacher" = None, parents25: "Parents" = None, school_administrator29: "School_administrator" = None):
        self.identify_students = identify_students
        self.student_names = student_names
        self.Excuse_of_Absenties = Excuse_of_Absenties
        self.students19 = students19 if students19 is not None else set()
        self.teacher20 = teacher20
        self.parents25 = parents25
        self.school_administrator29 = school_administrator29
        
        pass
    @property
    def Excuse_of_Absenties(self):
        return self.__Excuse_of_Absenties
    @Excuse_of_Absenties.setter
    def Excuse_of_Absenties(self, Excuse_of_Absenties: str):
        self.__Excuse_of_Absenties = Excuse_of_Absenties

    @property
    def student_names(self):
        return self.__student_names
    @student_names.setter
    def student_names(self, student_names: str):
        self.__student_names = student_names

    @property
    def identify_students(self):
        return self.__identify_students
    @identify_students.setter
    def identify_students(self, identify_students: str):
        self.__identify_students = identify_students

    @property
    def parents25(self):
        return self.__parents25
    @parents25.setter
    def parents25(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attendance_manager__parents25", None)
        self.__parents25 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance_manager24"):
                opp_val = getattr(old_value, "attendance_manager24", None)
                if opp_val == self:
                    setattr(old_value, "attendance_manager24", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance_manager24"):
                opp_val = getattr(value, "attendance_manager24", None)
                setattr(value, "attendance_manager24", self)

    @property
    def teacher20(self):
        return self.__teacher20
    @teacher20.setter
    def teacher20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attendance_manager__teacher20", None)
        self.__teacher20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance_manager21"):
                opp_val = getattr(old_value, "attendance_manager21", None)
                if opp_val == self:
                    setattr(old_value, "attendance_manager21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance_manager21"):
                opp_val = getattr(value, "attendance_manager21", None)
                setattr(value, "attendance_manager21", self)

    @property
    def school_administrator29(self):
        return self.__school_administrator29
    @school_administrator29.setter
    def school_administrator29(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attendance_manager__school_administrator29", None)
        self.__school_administrator29 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "attendance_manager28"):
                opp_val = getattr(old_value, "attendance_manager28", None)
                if opp_val == self:
                    setattr(old_value, "attendance_manager28", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "attendance_manager28"):
                opp_val = getattr(value, "attendance_manager28", None)
                setattr(value, "attendance_manager28", self)

    @property
    def students19(self):
        return self.__students19
    @students19.setter
    def students19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_attendance_manager__students19", None)
        self.__students19 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "attendance_manager18"):
                    opp_val = getattr(item, "attendance_manager18", None)
                    
                    if opp_val == self:
                        setattr(item, "attendance_manager18", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "attendance_manager18"):
                    opp_val = getattr(item, "attendance_manager18", None)
                    
                    setattr(item, "attendance_manager18", self)
                    



class students:

    def __init__(self, student_id_: int_Interface, student_name: str, attendance_manager18: "attendance_manager" = None, school_administrator22: "School_administrator" = None):
        self.student_id_ = student_id_
        self.student_name = student_name
        self.attendance_manager18 = attendance_manager18
        self.school_administrator22 = school_administrator22
        
        pass
    @property
    def student_id_(self):
        return self.__student_id_
    @student_id_.setter
    def student_id_(self, student_id_: int_Interface):
        self.__student_id_ = student_id_

    @property
    def student_name(self):
        return self.__student_name
    @student_name.setter
    def student_name(self, student_name: str):
        self.__student_name = student_name

    @property
    def attendance_manager18(self):
        return self.__attendance_manager18
    @attendance_manager18.setter
    def attendance_manager18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_students__attendance_manager18", None)
        self.__attendance_manager18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students19"):
                opp_val = getattr(old_value, "students19", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students19"):
                opp_val = getattr(value, "students19", None)
                if opp_val is None:
                    setattr(value, "students19", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def school_administrator22(self):
        return self.__school_administrator22
    @school_administrator22.setter
    def school_administrator22(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_students__school_administrator22", None)
        self.__school_administrator22 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "students23"):
                opp_val = getattr(old_value, "students23", None)
                if opp_val == self:
                    setattr(old_value, "students23", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "students23"):
                opp_val = getattr(value, "students23", None)
                setattr(value, "students23", self)



class kiosk:

    def __init__(self, newsletters: str, saving: int_Interface, discount: int_Interface, compuer13: "compuer" = None, customer15: set["customer"] = None, owner17: "Owner" = None):
        self.newsletters = newsletters
        self.saving = saving
        self.discount = discount
        self.compuer13 = compuer13
        self.customer15 = customer15 if customer15 is not None else set()
        self.owner17 = owner17
        
        pass
    @property
    def discount(self):
        return self.__discount
    @discount.setter
    def discount(self, discount: int_Interface):
        self.__discount = discount

    @property
    def saving(self):
        return self.__saving
    @saving.setter
    def saving(self, saving: int_Interface):
        self.__saving = saving

    @property
    def newsletters(self):
        return self.__newsletters
    @newsletters.setter
    def newsletters(self, newsletters: str):
        self.__newsletters = newsletters

    @property
    def owner17(self):
        return self.__owner17
    @owner17.setter
    def owner17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kiosk__owner17", None)
        self.__owner17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kiosk16"):
                opp_val = getattr(old_value, "kiosk16", None)
                if opp_val == self:
                    setattr(old_value, "kiosk16", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kiosk16"):
                opp_val = getattr(value, "kiosk16", None)
                setattr(value, "kiosk16", self)

    @property
    def customer15(self):
        return self.__customer15
    @customer15.setter
    def customer15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kiosk__customer15", None)
        self.__customer15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "kiosk14"):
                    opp_val = getattr(item, "kiosk14", None)
                    
                    if opp_val == self:
                        setattr(item, "kiosk14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "kiosk14"):
                    opp_val = getattr(item, "kiosk14", None)
                    
                    setattr(item, "kiosk14", self)
                    

    @property
    def compuer13(self):
        return self.__compuer13
    @compuer13.setter
    def compuer13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_kiosk__compuer13", None)
        self.__compuer13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "kiosk12"):
                opp_val = getattr(old_value, "kiosk12", None)
                if opp_val == self:
                    setattr(old_value, "kiosk12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "kiosk12"):
                opp_val = getattr(value, "kiosk12", None)
                setattr(value, "kiosk12", self)



class Owner:

    def __init__(self, items: str, email: str, kiosk16: "kiosk" = None):
        self.items = items
        self.email = email
        self.kiosk16 = kiosk16
        
        pass
    @property
    def items(self):
        return self.__items
    @items.setter
    def items(self, items: str):
        self.__items = items

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def kiosk16(self):
        return self.__kiosk16
    @kiosk16.setter
    def kiosk16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Owner__kiosk16", None)
        self.__kiosk16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "owner17"):
                opp_val = getattr(old_value, "owner17", None)
                if opp_val == self:
                    setattr(old_value, "owner17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "owner17"):
                opp_val = getattr(value, "owner17", None)
                setattr(value, "owner17", self)



class compuer:

    pass


class customer:

    def __init__(self, customer_Id: int_Interface, customer_name: str, _attr: str, kiosk14: "kiosk" = None, compuer10: "compuer" = None):
        self.customer_Id = customer_Id
        self.customer_name = customer_name
        self._attr = _attr
        self.kiosk14 = kiosk14
        self.compuer10 = compuer10
        
        pass
    @property
    def _attr(self):
        return self.___attr
    @_attr.setter
    def _attr(self, _attr: str):
        self.___attr = _attr

    @property
    def customer_Id(self):
        return self.__customer_Id
    @customer_Id.setter
    def customer_Id(self, customer_Id: int_Interface):
        self.__customer_Id = customer_Id

    @property
    def customer_name(self):
        return self.__customer_name
    @customer_name.setter
    def customer_name(self, customer_name: str):
        self.__customer_name = customer_name

    @property
    def kiosk14(self):
        return self.__kiosk14
    @kiosk14.setter
    def kiosk14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__kiosk14", None)
        self.__kiosk14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer15"):
                opp_val = getattr(old_value, "customer15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer15"):
                opp_val = getattr(value, "customer15", None)
                if opp_val is None:
                    setattr(value, "customer15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def compuer10(self):
        return self.__compuer10
    @compuer10.setter
    def compuer10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_customer__compuer10", None)
        self.__compuer10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "customer11"):
                opp_val = getattr(old_value, "customer11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "customer11"):
                opp_val = getattr(value, "customer11", None)
                if opp_val is None:
                    setattr(value, "customer11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class duties_manager:

    def __init__(self, make_attendence: bool, doctor7: set["doctor"] = None, clinical9: set["clinical"] = None):
        self.make_attendence = make_attendence
        self.doctor7 = doctor7 if doctor7 is not None else set()
        self.clinical9 = clinical9 if clinical9 is not None else set()
        
        pass
    @property
    def make_attendence(self):
        return self.__make_attendence
    @make_attendence.setter
    def make_attendence(self, make_attendence: bool):
        self.__make_attendence = make_attendence

    @property
    def doctor7(self):
        return self.__doctor7
    @doctor7.setter
    def doctor7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_duties_manager__doctor7", None)
        self.__doctor7 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "duties_manager6"):
                    opp_val = getattr(item, "duties_manager6", None)
                    
                    if opp_val == self:
                        setattr(item, "duties_manager6", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "duties_manager6"):
                    opp_val = getattr(item, "duties_manager6", None)
                    
                    setattr(item, "duties_manager6", self)
                    

    @property
    def clinical9(self):
        return self.__clinical9
    @clinical9.setter
    def clinical9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_duties_manager__clinical9", None)
        self.__clinical9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "duties_manager8"):
                    opp_val = getattr(item, "duties_manager8", None)
                    
                    if opp_val == self:
                        setattr(item, "duties_manager8", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "duties_manager8"):
                    opp_val = getattr(item, "duties_manager8", None)
                    
                    setattr(item, "duties_manager8", self)
                    



class pharmacy:

    def __init__(self, medicines: str, price: int_Interface, patient5: set["patient"] = None):
        self.medicines = medicines
        self.price = price
        self.patient5 = patient5 if patient5 is not None else set()
        
        pass
    @property
    def price(self):
        return self.__price
    @price.setter
    def price(self, price: int_Interface):
        self.__price = price

    @property
    def medicines(self):
        return self.__medicines
    @medicines.setter
    def medicines(self, medicines: str):
        self.__medicines = medicines

    @property
    def patient5(self):
        return self.__patient5
    @patient5.setter
    def patient5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_pharmacy__patient5", None)
        self.__patient5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "pharmacy4"):
                    opp_val = getattr(item, "pharmacy4", None)
                    
                    if opp_val == self:
                        setattr(item, "pharmacy4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "pharmacy4"):
                    opp_val = getattr(item, "pharmacy4", None)
                    
                    setattr(item, "pharmacy4", self)
                    



class bank:

    def __init__(self, bank_name: str, income_manager3: "income_manager" = None):
        self.bank_name = bank_name
        self.income_manager3 = income_manager3
        
        pass
    @property
    def bank_name(self):
        return self.__bank_name
    @bank_name.setter
    def bank_name(self, bank_name: str):
        self.__bank_name = bank_name

    @property
    def income_manager3(self):
        return self.__income_manager3
    @income_manager3.setter
    def income_manager3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_bank__income_manager3", None)
        self.__income_manager3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "bank2"):
                opp_val = getattr(old_value, "bank2", None)
                if opp_val == self:
                    setattr(old_value, "bank2", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "bank2"):
                opp_val = getattr(value, "bank2", None)
                setattr(value, "bank2", self)



class income_manager:

    def __init__(self, manager_name: str, manager_id: int_Interface, duty_hours: int_Interface, bank2: "bank" = None):
        self.manager_name = manager_name
        self.manager_id = manager_id
        self.duty_hours = duty_hours
        self.bank2 = bank2
        
        pass
    @property
    def duty_hours(self):
        return self.__duty_hours
    @duty_hours.setter
    def duty_hours(self, duty_hours: int_Interface):
        self.__duty_hours = duty_hours

    @property
    def manager_name(self):
        return self.__manager_name
    @manager_name.setter
    def manager_name(self, manager_name: str):
        self.__manager_name = manager_name

    @property
    def manager_id(self):
        return self.__manager_id
    @manager_id.setter
    def manager_id(self, manager_id: int_Interface):
        self.__manager_id = manager_id

    @property
    def bank2(self):
        return self.__bank2
    @bank2.setter
    def bank2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_income_manager__bank2", None)
        self.__bank2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "income_manager3"):
                opp_val = getattr(old_value, "income_manager3", None)
                if opp_val == self:
                    setattr(old_value, "income_manager3", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "income_manager3"):
                opp_val = getattr(value, "income_manager3", None)
                setattr(value, "income_manager3", self)



class clinical:

    def __init__(self, id: int_Interface, name: str, salary: int_Interface, duties_manager8: "duties_manager" = None):
        self.id = id
        self.name = name
        self.salary = salary
        self.duties_manager8 = duties_manager8
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int_Interface):
        self.__id = id

    @property
    def name(self):
        return self.__name
    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: int_Interface):
        self.__salary = salary

    @property
    def duties_manager8(self):
        return self.__duties_manager8
    @duties_manager8.setter
    def duties_manager8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_clinical__duties_manager8", None)
        self.__duties_manager8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "clinical9"):
                opp_val = getattr(old_value, "clinical9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "clinical9"):
                opp_val = getattr(value, "clinical9", None)
                if opp_val is None:
                    setattr(value, "clinical9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class doctor:

    def __init__(self, doctor_id: int_Interface, doctor_name: str, salary: int_Interface, attendance: bool, patient_class1: "patient" = None, duties_manager6: "duties_manager" = None):
        self.doctor_id = doctor_id
        self.doctor_name = doctor_name
        self.salary = salary
        self.attendance = attendance
        self.patient_class1 = patient_class1
        self.duties_manager6 = duties_manager6
        
        pass
    @property
    def doctor_id(self):
        return self.__doctor_id
    @doctor_id.setter
    def doctor_id(self, doctor_id: int_Interface):
        self.__doctor_id = doctor_id

    @property
    def salary(self):
        return self.__salary
    @salary.setter
    def salary(self, salary: int_Interface):
        self.__salary = salary

    @property
    def doctor_name(self):
        return self.__doctor_name
    @doctor_name.setter
    def doctor_name(self, doctor_name: str):
        self.__doctor_name = doctor_name

    @property
    def attendance(self):
        return self.__attendance
    @attendance.setter
    def attendance(self, attendance: bool):
        self.__attendance = attendance

    @property
    def duties_manager6(self):
        return self.__duties_manager6
    @duties_manager6.setter
    def duties_manager6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__duties_manager6", None)
        self.__duties_manager6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor7"):
                opp_val = getattr(old_value, "doctor7", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor7"):
                opp_val = getattr(value, "doctor7", None)
                if opp_val is None:
                    setattr(value, "doctor7", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def patient_class1(self):
        return self.__patient_class1
    @patient_class1.setter
    def patient_class1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_doctor__patient_class1", None)
        self.__patient_class1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "doctor0"):
                opp_val = getattr(old_value, "doctor0", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "doctor0"):
                opp_val = getattr(value, "doctor0", None)
                if opp_val is None:
                    setattr(value, "doctor0", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class int_Interface:

    pass


class patient:

    def __init__(self, patient_id: int_Interface, patient_name: str, disease: str, doctor0: set["doctor"] = None, pharmacy4: "pharmacy" = None):
        self.patient_id = patient_id
        self.patient_name = patient_name
        self.disease = disease
        self.doctor0 = doctor0 if doctor0 is not None else set()
        self.pharmacy4 = pharmacy4
        
        pass
    @property
    def patient_id(self):
        return self.__patient_id
    @patient_id.setter
    def patient_id(self, patient_id: int_Interface):
        self.__patient_id = patient_id

    @property
    def disease(self):
        return self.__disease
    @disease.setter
    def disease(self, disease: str):
        self.__disease = disease

    @property
    def patient_name(self):
        return self.__patient_name
    @patient_name.setter
    def patient_name(self, patient_name: str):
        self.__patient_name = patient_name

    @property
    def pharmacy4(self):
        return self.__pharmacy4
    @pharmacy4.setter
    def pharmacy4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__pharmacy4", None)
        self.__pharmacy4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient5"):
                opp_val = getattr(old_value, "patient5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient5"):
                opp_val = getattr(value, "patient5", None)
                if opp_val is None:
                    setattr(value, "patient5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def doctor0(self):
        return self.__doctor0
    @doctor0.setter
    def doctor0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_patient__doctor0", None)
        self.__doctor0 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient_class1"):
                    opp_val = getattr(item, "patient_class1", None)
                    
                    if opp_val == self:
                        setattr(item, "patient_class1", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient_class1"):
                    opp_val = getattr(item, "patient_class1", None)
                    
                    setattr(item, "patient_class1", self)
                    

