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

    def __init__(self, LibrarianName: str, patron41: set["Library_Management_System_Patron"] = None):
        self.LibrarianName = LibrarianName
        self.patron41 = patron41 if patron41 is not None else set()
        
        pass
    @property
    def LibrarianName(self):
        return self.__LibrarianName
    @LibrarianName.setter
    def LibrarianName(self, LibrarianName: str):
        self.__LibrarianName = LibrarianName

    @property
    def patron41(self):
        return self.__patron41
    @patron41.setter
    def patron41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Librarian__patron41", None)
        self.__patron41 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "librarian40"):
                    opp_val = getattr(item, "librarian40", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "librarian40"):
                    opp_val = getattr(item, "librarian40", None)
                    
                    if opp_val is None:
                        setattr(item, "librarian40", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Library_Management_System_Faculty:

    def __init__(self, FacultyId: int, FacultyName: str, patron39: set["Library_Management_System_Patron"] = None):
        self.FacultyId = FacultyId
        self.FacultyName = FacultyName
        self.patron39 = patron39 if patron39 is not None else set()
        
        pass
    @property
    def FacultyName(self):
        return self.__FacultyName
    @FacultyName.setter
    def FacultyName(self, FacultyName: str):
        self.__FacultyName = FacultyName

    @property
    def FacultyId(self):
        return self.__FacultyId
    @FacultyId.setter
    def FacultyId(self, FacultyId: int):
        self.__FacultyId = FacultyId

    @property
    def patron39(self):
        return self.__patron39
    @patron39.setter
    def patron39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Faculty__patron39", None)
        self.__patron39 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "faculty38"):
                    opp_val = getattr(item, "faculty38", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "faculty38"):
                    opp_val = getattr(item, "faculty38", None)
                    
                    if opp_val is None:
                        setattr(item, "faculty38", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Library_Management_System_Student:

    def __init__(self, StudentId: int, StudentName: str, patron37: set["Library_Management_System_Patron"] = None):
        self.StudentId = StudentId
        self.StudentName = StudentName
        self.patron37 = patron37 if patron37 is not None else set()
        
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
    def patron37(self):
        return self.__patron37
    @patron37.setter
    def patron37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Student__patron37", None)
        self.__patron37 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "student36"):
                    opp_val = getattr(item, "student36", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "student36"):
                    opp_val = getattr(item, "student36", None)
                    
                    if opp_val is None:
                        setattr(item, "student36", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    



class Library_Management_System_Patron:

    def __init__(self, Books: str, OtherResources: str, Status: Library_Management_System_Patron, SpecialStatus: str, Magazines: str, librarian40: set["Library_Management_System_Librarian"] = None, student36: set["Library_Management_System_Student"] = None, faculty38: set["Library_Management_System_Faculty"] = None):
        self.Books = Books
        self.OtherResources = OtherResources
        self.Status = Status
        self.SpecialStatus = SpecialStatus
        self.Magazines = Magazines
        self.librarian40 = librarian40 if librarian40 is not None else set()
        self.student36 = student36 if student36 is not None else set()
        self.faculty38 = faculty38 if faculty38 is not None else set()
        
        pass
    @property
    def Magazines(self):
        return self.__Magazines
    @Magazines.setter
    def Magazines(self, Magazines: str):
        self.__Magazines = Magazines

    @property
    def Books(self):
        return self.__Books
    @Books.setter
    def Books(self, Books: str):
        self.__Books = Books

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
    def OtherResources(self):
        return self.__OtherResources
    @OtherResources.setter
    def OtherResources(self, OtherResources: str):
        self.__OtherResources = OtherResources

    @property
    def faculty38(self):
        return self.__faculty38
    @faculty38.setter
    def faculty38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Patron__faculty38", None)
        self.__faculty38 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patron39"):
                    opp_val = getattr(item, "patron39", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patron39"):
                    opp_val = getattr(item, "patron39", None)
                    
                    if opp_val is None:
                        setattr(item, "patron39", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def student36(self):
        return self.__student36
    @student36.setter
    def student36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Patron__student36", None)
        self.__student36 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patron37"):
                    opp_val = getattr(item, "patron37", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patron37"):
                    opp_val = getattr(item, "patron37", None)
                    
                    if opp_val is None:
                        setattr(item, "patron37", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

    @property
    def librarian40(self):
        return self.__librarian40
    @librarian40.setter
    def librarian40(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Library_Management_System_Patron__librarian40", None)
        self.__librarian40 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patron41"):
                    opp_val = getattr(item, "patron41", None)
                    
                    if isinstance(opp_val, set):
                        opp_val.discard(self)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patron41"):
                    opp_val = getattr(item, "patron41", None)
                    
                    if opp_val is None:
                        setattr(item, "patron41", set([self]))
                    elif isinstance(opp_val, set):
                        opp_val.add(self)
                    

