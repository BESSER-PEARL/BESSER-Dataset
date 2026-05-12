from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class add_update_and_delete_job_UseCase:

    pass


class post_job_UseCase:

    pass


class search_job_UseCase:

    pass


class Response_to_users_employee_to_job_seekers__UseCase:

    pass


class Update_categories_UseCase:

    pass


class Manage_database_UseCase:

    pass


class search_jobs_UseCase:

    pass


class post_resume_UseCase:

    pass


class apply_for_job_UseCase:

    pass


class Employer_Actor:

    pass


class Job_Seeker_Actor:

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


class Administrator_Actor:

    pass





class JobSeeker:

    def __init__(self, Name: str, Qualification: str, Experience: str, administrator39: "Administrator" = None):
        self.Name = Name
        self.Qualification = Qualification
        self.Experience = Experience
        self.administrator39 = administrator39
        
        pass
    @property
    def Experience(self):
        return self.__Experience
    @Experience.setter
    def Experience(self, Experience: str):
        self.__Experience = Experience

    @property
    def Qualification(self):
        return self.__Qualification
    @Qualification.setter
    def Qualification(self, Qualification: str):
        self.__Qualification = Qualification

    @property
    def Name(self):
        return self.__Name
    @Name.setter
    def Name(self, Name: str):
        self.__Name = Name

    @property
    def administrator39(self):
        return self.__administrator39
    @administrator39.setter
    def administrator39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_JobSeeker__administrator39", None)
        self.__administrator39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "jobseeker38"):
                opp_val = getattr(old_value, "jobseeker38", None)
                if opp_val == self:
                    setattr(old_value, "jobseeker38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "jobseeker38"):
                opp_val = getattr(value, "jobseeker38", None)
                setattr(value, "jobseeker38", self)



class Administrator:

    def __init__(self, Name: str, Address: str, Company: str, employer37: "Employer" = None, jobseeker38: "JobSeeker" = None):
        self.Name = Name
        self.Address = Address
        self.Company = Company
        self.employer37 = employer37
        self.jobseeker38 = jobseeker38
        
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
    def Company(self):
        return self.__Company
    @Company.setter
    def Company(self, Company: str):
        self.__Company = Company

    @property
    def jobseeker38(self):
        return self.__jobseeker38
    @jobseeker38.setter
    def jobseeker38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__jobseeker38", None)
        self.__jobseeker38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator39"):
                opp_val = getattr(old_value, "administrator39", None)
                if opp_val == self:
                    setattr(old_value, "administrator39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator39"):
                opp_val = getattr(value, "administrator39", None)
                setattr(value, "administrator39", self)

    @property
    def employer37(self):
        return self.__employer37
    @employer37.setter
    def employer37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Administrator__employer37", None)
        self.__employer37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "administrator36"):
                opp_val = getattr(old_value, "administrator36", None)
                if opp_val == self:
                    setattr(old_value, "administrator36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "administrator36"):
                opp_val = getattr(value, "administrator36", None)
                setattr(value, "administrator36", self)



class Employer:

    def __init__(self, Name: str, Address: str, administrator36: "Administrator" = None):
        self.Name = Name
        self.Address = Address
        self.administrator36 = administrator36
        
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
    def administrator36(self):
        return self.__administrator36
    @administrator36.setter
    def administrator36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employer__administrator36", None)
        self.__administrator36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employer37"):
                opp_val = getattr(old_value, "employer37", None)
                if opp_val == self:
                    setattr(old_value, "employer37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employer37"):
                opp_val = getattr(value, "employer37", None)
                setattr(value, "employer37", self)



class User:

    def __init__(self, Name: str, Address: str):
        self.Name = Name
        self.Address = Address
        
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



class login_UseCase2:

    pass


class Administrator_Actor1:

    pass


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
