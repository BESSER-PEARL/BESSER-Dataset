from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Administrator_Actor:

    pass


class Login_UseCase:

    pass


class Support_Services_UseCase:

    pass


class Admin_login__firebase__UseCase:

    pass


class Add__Update_and_Delete_job_UseCase:

    pass


class Post_Job_UseCase:

    pass


class Signup_UseCase:

    pass


class Search_Jobs_UseCase:

    pass


class Set_Profile_UseCase:

    pass


class Security_UseCase:

    pass


class Manage_database_UseCase:

    pass


class Apply_for_Job_UseCase:

    pass


class Admin_____________backend__Actor:

    pass


class App_User_Actor:

    pass


class logout_UseCase:

    pass


class job_vacancies_UseCase:

    pass


class list_of_jobs_related_to_graduation_UseCase:

    pass


class job_offers_UseCase:

    pass


class Actor4_Actor:

    pass


class job_offer_UseCase:

    pass


class login_UseCase:

    pass


class Actor3_Actor:

    pass


class Actor2_Actor:

    pass


class admin_Actor:

    pass


class Actor_Actor:

    pass


class UseCase_UseCase:

    pass


class educational_qualification_UseCase:

    pass


class seeking_for_job_UseCase:

    pass


class list_of_jobs_available_UseCase:

    pass


class log_in_UseCase:

    pass


class job_seeker_Actor:

    pass


class employer_Actor:

    pass





class JobSeeker:

    def __init__(self, Name: str, Qualification: str, Experience: str, administrator35: "Administrator" = None):
        self.Name = Name
        self.Qualification = Qualification
        self.Experience = Experience
        self.administrator35 = administrator35
        
        pass
    @property
    def Experience(self):
        return self.__Experience
    @Experience.setter
    def Experience(self, Experience: str):
        self.__Experience = Experience

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Qualification(self):
        return self.__Qualification
    @Qualification.setter
    def Qualification(self, Qualification: str):
        self.__Qualification = Qualification

    @property
    def administrator35(self):
        return self.__administrator35
    @administrator35.setter
    def administrator35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JobSeeker__administrator35", None)
        self.__administrator35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jobseeker34"):
                opp_val = getattr(old_value, "jobseeker34", None)
                if opp_val == self:
                    setattr(old_value, "jobseeker34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jobseeker34"):
                opp_val = getattr(value, "jobseeker34", None)
                setattr(value, "jobseeker34", self)



class Administrator:

    def __init__(self, Name: str, Address: str, Company: str, jobseeker34: "JobSeeker" = None, employer33: "Employer" = None):
        self.Name = Name
        self.Address = Address
        self.Company = Company
        self.jobseeker34 = jobseeker34
        self.employer33 = employer33
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Company(self):
        return self.__Company
    @Company.setter
    def Company(self, Company: str):
        self.__Company = Company

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def employer33(self):
        return self.__employer33
    @employer33.setter
    def employer33(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__employer33", None)
        self.__employer33 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator32"):
                opp_val = getattr(old_value, "administrator32", None)
                if opp_val == self:
                    setattr(old_value, "administrator32", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator32"):
                opp_val = getattr(value, "administrator32", None)
                setattr(value, "administrator32", self)

    @property
    def jobseeker34(self):
        return self.__jobseeker34
    @jobseeker34.setter
    def jobseeker34(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__jobseeker34", None)
        self.__jobseeker34 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator35"):
                opp_val = getattr(old_value, "administrator35", None)
                if opp_val == self:
                    setattr(old_value, "administrator35", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator35"):
                opp_val = getattr(value, "administrator35", None)
                setattr(value, "administrator35", self)



class Employer:

    def __init__(self, Name: str, Address: str, administrator32: "Administrator" = None):
        self.Name = Name
        self.Address = Address
        self.administrator32 = administrator32
        
        pass
    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def administrator32(self):
        return self.__administrator32
    @administrator32.setter
    def administrator32(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employer__administrator32", None)
        self.__administrator32 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employer33"):
                opp_val = getattr(old_value, "employer33", None)
                if opp_val == self:
                    setattr(old_value, "employer33", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employer33"):
                opp_val = getattr(value, "employer33", None)
                setattr(value, "employer33", self)



class User:

    def __init__(self, Name: str, Address: str):
        self.Name = Name
        self.Address = Address
        
        pass
    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address



class educational_qualification_UseCase1:

    pass


class login_UseCase1:

    pass


class employer_Actor1:

    pass


class job_seeker_Actor2:

    pass


class admin_Actor2:

    pass


class job_seeker_Actor1:

    pass


class admin_Actor1:

    pass


class MyClass:

    pass
