from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Faculty_Actor:

    pass


class Student_Actor:

    pass


class Librarian_Actor:

    pass


class Library_Managment_System_1_week_check_out_UseCase:

    pass


class Library_Managment_System_CD_s_software_videos_UseCase:

    pass


class Library_Managment_System_Other_resources_UseCase:

    pass


class Library_Managment_System_Contents_out_of_date_UseCase:

    pass


class Library_Managment_System_Meet_requests_of_patrons_UseCase:

    pass


class Library_Managment_System_Retiring_UseCase:

    pass


class Library_Managment_System_Adding_UseCase:

    pass


class Library_Managment_System_Books_UseCase:

    pass


class Library_Managment_System_Connect_to_holding_of_other_libraries_UseCase:

    pass


class Library_Managment_System_Assist_patrons_in_research_UseCase:

    pass


class Library_Managment_System_Ordering_new_resources_UseCase:

    pass


class Library_Managment_System_Reshelving_books_UseCase:

    pass


class Library_Managment_System_Renew_subscriptions_UseCase:

    pass


class Library_Managment_System_Manage_Magazines_UseCase:

    pass


class Library_Managment_System_Issue_fines_UseCase:

    pass


class Library_Managment_System_1_year_check_out_UseCase:

    pass


class Library_Managment_System_3_month_check_out_UseCase:

    pass


class Library_Managment_System_Reserve_foreign_resources_UseCase:

    pass


class Library_Managment_System_Reserve_book__1_semester__UseCase:

    pass


class Library_Managment_System_4_week_check_out_UseCase:

    pass


class Library_Managment_System_Librarian_UseCase:

    pass


class Library_Managment_System_Faculty_UseCase:

    pass


class Library_Managment_System_Student_UseCase:

    pass


class Library_Managment_System_Status_UseCase:

    pass


class Library_Managment_System_Late_Notice_UseCase:

    pass


class Library_Managment_System_Renew_Checkout_if_not_requested_UseCase:

    pass


class Library_Managment_System_Magazines_UseCase:

    pass


class Library_Managment_System_Special_Status_UseCase:

    pass


class Library_Managment_System_Reserve_UseCase:

    pass


class Library_Managment_System_Check_out_UseCase:

    pass


class Library_Managment_System_Reference_UseCase:

    pass


class Library_Managment_System_Requested_UseCase:

    pass


class Library_Managment_System_Check_in___Return_UseCase:

    pass





class Library_Management_System_Librarian:

    def __init__(self, LibrarianName: str, patron51: set["Library_Management_System_Patron"] = None):
        self.LibrarianName = LibrarianName
        self.patron51 = patron51 if patron51 is not None else set()
        
        pass
    @property
    def LibrarianName(self):
        return self.__LibrarianName
    @LibrarianName.setter
    def LibrarianName(self, LibrarianName: str):
        self.__LibrarianName = LibrarianName

    @property
    def patron51(self):
        return self.__patron51
    @patron51.setter
    def patron51(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Librarian__patron51", None)
        self.__patron51 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "librarian50"):
                    opp_val = getattr(item, "librarian50", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "librarian50"):
                    opp_val = getattr(item, "librarian50", None)
                    
                    if opp_val is None:
                        setattr(item, "librarian50", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Library_Management_System_Faculty:

    def __init__(self, FacultyId: int, FacultyName: str, patron49: set["Library_Management_System_Patron"] = None):
        self.FacultyId = FacultyId
        self.FacultyName = FacultyName
        self.patron49 = patron49 if patron49 is not None else set()
        
        pass
    @property
    def FacultyId(self):
        return self.__FacultyId
    @FacultyId.setter
    def FacultyId(self, FacultyId: int):
        self.__FacultyId = FacultyId

    @property
    def FacultyName(self):
        return self.__FacultyName
    @FacultyName.setter
    def FacultyName(self, FacultyName: str):
        self.__FacultyName = FacultyName

    @property
    def patron49(self):
        return self.__patron49
    @patron49.setter
    def patron49(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Faculty__patron49", None)
        self.__patron49 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "faculty48"):
                    opp_val = getattr(item, "faculty48", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "faculty48"):
                    opp_val = getattr(item, "faculty48", None)
                    
                    if opp_val is None:
                        setattr(item, "faculty48", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Library_Management_System_Student:

    def __init__(self, StudentId: int, StudentName: str, patron47: set["Library_Management_System_Patron"] = None):
        self.StudentId = StudentId
        self.StudentName = StudentName
        self.patron47 = patron47 if patron47 is not None else set()
        
        pass
    @property
    def StudentId(self):
        return self.__StudentId
    @StudentId.setter
    def StudentId(self, StudentId: int):
        self.__StudentId = StudentId

    @property
    def StudentName(self):
        return self.__StudentName
    @StudentName.setter
    def StudentName(self, StudentName: str):
        self.__StudentName = StudentName

    @property
    def patron47(self):
        return self.__patron47
    @patron47.setter
    def patron47(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Student__patron47", None)
        self.__patron47 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student46"):
                    opp_val = getattr(item, "student46", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student46"):
                    opp_val = getattr(item, "student46", None)
                    
                    if opp_val is None:
                        setattr(item, "student46", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Library_Management_System_Patron:

    def __init__(self, Books: str, OtherResources: str, Status: Library_Management_System_Patron, SpecialStatus: str, Magazines: str, librarian50: set["Library_Management_System_Librarian"] = None, student46: set["Library_Management_System_Student"] = None, faculty48: set["Library_Management_System_Faculty"] = None):
        self.Books = Books
        self.OtherResources = OtherResources
        self.Status = Status
        self.SpecialStatus = SpecialStatus
        self.Magazines = Magazines
        self.librarian50 = librarian50 if librarian50 is not None else set()
        self.student46 = student46 if student46 is not None else set()
        self.faculty48 = faculty48 if faculty48 is not None else set()
        
        pass
    @property
    def OtherResources(self):
        return self.__OtherResources
    @OtherResources.setter
    def OtherResources(self, OtherResources: str):
        self.__OtherResources = OtherResources

    @property
    def SpecialStatus(self):
        return self.__SpecialStatus
    @SpecialStatus.setter
    def SpecialStatus(self, SpecialStatus: str):
        self.__SpecialStatus = SpecialStatus

    @property
    def Status(self):
        return self.__Status
    @Status.setter
    def Status(self, Status: Library_Management_System_Patron):
        self.__Status = Status

    @property
    def Books(self):
        return self.__Books
    @Books.setter
    def Books(self, Books: str):
        self.__Books = Books

    @property
    def Magazines(self):
        return self.__Magazines
    @Magazines.setter
    def Magazines(self, Magazines: str):
        self.__Magazines = Magazines

    @property
    def librarian50(self):
        return self.__librarian50
    @librarian50.setter
    def librarian50(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Patron__librarian50", None)
        self.__librarian50 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patron51"):
                    opp_val = getattr(item, "patron51", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patron51"):
                    opp_val = getattr(item, "patron51", None)
                    
                    if opp_val is None:
                        setattr(item, "patron51", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def student46(self):
        return self.__student46
    @student46.setter
    def student46(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Patron__student46", None)
        self.__student46 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patron47"):
                    opp_val = getattr(item, "patron47", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patron47"):
                    opp_val = getattr(item, "patron47", None)
                    
                    if opp_val is None:
                        setattr(item, "patron47", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def faculty48(self):
        return self.__faculty48
    @faculty48.setter
    def faculty48(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Patron__faculty48", None)
        self.__faculty48 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patron49"):
                    opp_val = getattr(item, "patron49", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patron49"):
                    opp_val = getattr(item, "patron49", None)
                    
                    if opp_val is None:
                        setattr(item, "patron49", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

