from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class delete_honor_member_UseCase:

    pass


class modify_honor_member_information__UseCase:

    pass


class print_honor_member_information__UseCase:

    pass


class display_honor_member_UseCase:

    pass


class print_volunteer_data_UseCase:

    pass


class delete_volunteer_UseCase:

    pass


class modify_volunteer_data_UseCase:

    pass


class display_volunteer_list_UseCase:

    pass


class display_beneficiaries_list_UseCase:

    pass


class change_his_password__UseCase:

    pass


class Log_in__UseCase:

    pass


class Log_out_UseCase:

    pass


class print_employee_information_UseCase:

    pass


class manage_holiday_UseCase:

    pass


class delete_employee_UseCase:

    pass


class modify_employee_data_UseCase:

    pass


class add_employee_UseCase:

    pass


class display_employee_information_UseCase:

    pass


class display_data_entry_UseCase:

    pass


class delete_data_entry_account__UseCase:

    pass


class add_new_data_entry_account_UseCase:

    pass


class change_the_organization_information__UseCase:

    pass


class change_his_password_UseCase:

    pass


class display_organization_information_UseCase:

    pass


class Administrator__Actor:

    pass


class Data_entry_employee__Actor:

    pass


class display_all_UseCase:

    pass


class add_honor_member_UseCase:

    pass


class add_new_volunteer_UseCase:

    pass


class Browse_based_number_of_children_UseCase:

    pass


class Browse_based_age_UseCase:

    pass


class Browse_based_Housing_kind_UseCase:

    pass


class Browse_based_Scientific_qualification_UseCase:

    pass


class Browse_based_name_UseCase:

    pass


class Browse_based_care_type_UseCase:

    pass


class print_beneficiaries_list_UseCase:

    pass


class delete_beneficiary__UseCase:

    pass


class print_beneficiary_information_UseCase:

    pass


class modify_beneficiary_information_UseCase:

    pass


class add_new_beneficiary_UseCase:

    pass


class account_statement__UseCase:

    pass





class The_20member_external:

    pass


class _20Data_20entry_external:

    pass


class Vacation:

    def __init__(self, Employee_ID: int, Beginning_date: str, Expiry_date: str, employee38: "Employee" = None):
        self.Employee_ID = Employee_ID
        self.Beginning_date = Beginning_date
        self.Expiry_date = Expiry_date
        self.employee38 = employee38
        
        pass
    @property
    def Beginning_date(self):
        return self.__Beginning_date
    @Beginning_date.setter
    def Beginning_date(self, Beginning_date: str):
        self.__Beginning_date = Beginning_date

    @property
    def Expiry_date(self):
        return self.__Expiry_date
    @Expiry_date.setter
    def Expiry_date(self, Expiry_date: str):
        self.__Expiry_date = Expiry_date

    @property
    def Employee_ID(self):
        return self.__Employee_ID
    @Employee_ID.setter
    def Employee_ID(self, Employee_ID: int):
        self.__Employee_ID = Employee_ID

    @property
    def employee38(self):
        return self.__employee38
    @employee38.setter
    def employee38(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Vacation__employee38", None)
        self.__employee38 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "vacation39"):
                opp_val = getattr(old_value, "vacation39", None)
                if opp_val == self:
                    setattr(old_value, "vacation39", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "vacation39"):
                opp_val = getattr(value, "vacation39", None)
                setattr(value, "vacation39", self)



class Employee:

    def __init__(self, ID: int, First_name: str, Last_name: str, Email_address: str, Mobile_number: int, Remaining_days: int, Functional_number: int, vacation39: "Vacation" = None, admin42: "Admin" = None):
        self.ID = ID
        self.First_name = First_name
        self.Last_name = Last_name
        self.Email_address = Email_address
        self.Mobile_number = Mobile_number
        self.Remaining_days = Remaining_days
        self.Functional_number = Functional_number
        self.vacation39 = vacation39
        self.admin42 = admin42
        
        pass
    @property
    def Email_address(self):
        return self.__Email_address
    @Email_address.setter
    def Email_address(self, Email_address: str):
        self.__Email_address = Email_address

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Last_name(self):
        return self.__Last_name
    @Last_name.setter
    def Last_name(self, Last_name: str):
        self.__Last_name = Last_name

    @property
    def First_name(self):
        return self.__First_name
    @First_name.setter
    def First_name(self, First_name: str):
        self.__First_name = First_name

    @property
    def Remaining_days(self):
        return self.__Remaining_days
    @Remaining_days.setter
    def Remaining_days(self, Remaining_days: int):
        self.__Remaining_days = Remaining_days

    @property
    def Functional_number(self):
        return self.__Functional_number
    @Functional_number.setter
    def Functional_number(self, Functional_number: int):
        self.__Functional_number = Functional_number

    @property
    def Mobile_number(self):
        return self.__Mobile_number
    @Mobile_number.setter
    def Mobile_number(self, Mobile_number: int):
        self.__Mobile_number = Mobile_number

    @property
    def admin42(self):
        return self.__admin42
    @admin42.setter
    def admin42(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__admin42", None)
        self.__admin42 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee43"):
                opp_val = getattr(old_value, "employee43", None)
                if opp_val == self:
                    setattr(old_value, "employee43", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee43"):
                opp_val = getattr(value, "employee43", None)
                setattr(value, "employee43", self)

    @property
    def vacation39(self):
        return self.__vacation39
    @vacation39.setter
    def vacation39(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Employee__vacation39", None)
        self.__vacation39 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employee38"):
                opp_val = getattr(old_value, "employee38", None)
                if opp_val == self:
                    setattr(old_value, "employee38", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employee38"):
                opp_val = getattr(value, "employee38", None)
                setattr(value, "employee38", self)



class Care:

    def __init__(self, Care_sort: str, Civil_Registry: str, Street: str, Workplace: str, Health_status: str, Children_health_status: str, Income_sources: str, Income_amount: str, Housing_description: str, Housing_kind: str, Number_of_children: str, Family_members__The_number: int, Guardian: str, Relation_of_the_guardian: str, Profession_of_the_guardian: str, Workplace_the_guardian: str, Monthly_income: int, Adopting_degree: str, Family_bonding: str, Interaction_degree: str, the_amount37: "Amount" = None):
        self.Care_sort = Care_sort
        self.Civil_Registry = Civil_Registry
        self.Street = Street
        self.Workplace = Workplace
        self.Health_status = Health_status
        self.Children_health_status = Children_health_status
        self.Income_sources = Income_sources
        self.Income_amount = Income_amount
        self.Housing_description = Housing_description
        self.Housing_kind = Housing_kind
        self.Number_of_children = Number_of_children
        self.Family_members__The_number = Family_members__The_number
        self.Guardian = Guardian
        self.Relation_of_the_guardian = Relation_of_the_guardian
        self.Profession_of_the_guardian = Profession_of_the_guardian
        self.Workplace_the_guardian = Workplace_the_guardian
        self.Monthly_income = Monthly_income
        self.Adopting_degree = Adopting_degree
        self.Family_bonding = Family_bonding
        self.Interaction_degree = Interaction_degree
        self.the_amount37 = the_amount37
        
        pass
    @property
    def Number_of_children(self):
        return self.__Number_of_children
    @Number_of_children.setter
    def Number_of_children(self, Number_of_children: str):
        self.__Number_of_children = Number_of_children

    @property
    def Income_sources(self):
        return self.__Income_sources
    @Income_sources.setter
    def Income_sources(self, Income_sources: str):
        self.__Income_sources = Income_sources

    @property
    def Workplace(self):
        return self.__Workplace
    @Workplace.setter
    def Workplace(self, Workplace: str):
        self.__Workplace = Workplace

    @property
    def Income_amount(self):
        return self.__Income_amount
    @Income_amount.setter
    def Income_amount(self, Income_amount: str):
        self.__Income_amount = Income_amount

    @property
    def Monthly_income(self):
        return self.__Monthly_income
    @Monthly_income.setter
    def Monthly_income(self, Monthly_income: int):
        self.__Monthly_income = Monthly_income

    @property
    def Health_status(self):
        return self.__Health_status
    @Health_status.setter
    def Health_status(self, Health_status: str):
        self.__Health_status = Health_status

    @property
    def Children_health_status(self):
        return self.__Children_health_status
    @Children_health_status.setter
    def Children_health_status(self, Children_health_status: str):
        self.__Children_health_status = Children_health_status

    @property
    def Interaction_degree(self):
        return self.__Interaction_degree
    @Interaction_degree.setter
    def Interaction_degree(self, Interaction_degree: str):
        self.__Interaction_degree = Interaction_degree

    @property
    def Relation_of_the_guardian(self):
        return self.__Relation_of_the_guardian
    @Relation_of_the_guardian.setter
    def Relation_of_the_guardian(self, Relation_of_the_guardian: str):
        self.__Relation_of_the_guardian = Relation_of_the_guardian

    @property
    def Housing_kind(self):
        return self.__Housing_kind
    @Housing_kind.setter
    def Housing_kind(self, Housing_kind: str):
        self.__Housing_kind = Housing_kind

    @property
    def Guardian(self):
        return self.__Guardian
    @Guardian.setter
    def Guardian(self, Guardian: str):
        self.__Guardian = Guardian

    @property
    def Family_bonding(self):
        return self.__Family_bonding
    @Family_bonding.setter
    def Family_bonding(self, Family_bonding: str):
        self.__Family_bonding = Family_bonding

    @property
    def Workplace_the_guardian(self):
        return self.__Workplace_the_guardian
    @Workplace_the_guardian.setter
    def Workplace_the_guardian(self, Workplace_the_guardian: str):
        self.__Workplace_the_guardian = Workplace_the_guardian

    @property
    def Civil_Registry(self):
        return self.__Civil_Registry
    @Civil_Registry.setter
    def Civil_Registry(self, Civil_Registry: str):
        self.__Civil_Registry = Civil_Registry

    @property
    def Family_members__The_number(self):
        return self.__Family_members__The_number
    @Family_members__The_number.setter
    def Family_members__The_number(self, Family_members__The_number: int):
        self.__Family_members__The_number = Family_members__The_number

    @property
    def Profession_of_the_guardian(self):
        return self.__Profession_of_the_guardian
    @Profession_of_the_guardian.setter
    def Profession_of_the_guardian(self, Profession_of_the_guardian: str):
        self.__Profession_of_the_guardian = Profession_of_the_guardian

    @property
    def Street(self):
        return self.__Street
    @Street.setter
    def Street(self, Street: str):
        self.__Street = Street

    @property
    def Adopting_degree(self):
        return self.__Adopting_degree
    @Adopting_degree.setter
    def Adopting_degree(self, Adopting_degree: str):
        self.__Adopting_degree = Adopting_degree

    @property
    def Housing_description(self):
        return self.__Housing_description
    @Housing_description.setter
    def Housing_description(self, Housing_description: str):
        self.__Housing_description = Housing_description

    @property
    def Care_sort(self):
        return self.__Care_sort
    @Care_sort.setter
    def Care_sort(self, Care_sort: str):
        self.__Care_sort = Care_sort

    @property
    def the_amount37(self):
        return self.__the_amount37
    @the_amount37.setter
    def the_amount37(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Care__the_amount37", None)
        self.__the_amount37 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "care36"):
                opp_val = getattr(old_value, "care36", None)
                if opp_val == self:
                    setattr(old_value, "care36", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "care36"):
                opp_val = getattr(value, "care36", None)
                setattr(value, "care36", self)



class Marriage_Demand:

    def __init__(self, Nationality: str, Nationality_of_the_mother: str, Tribe: str, Legitimate_vision: str, Salary: str, Marital_status_of_the_proposer: str, Educational_status: str, Other_district: str, Accept_multi_marriage: str, Relation_with_proposal: str):
        self.Nationality = Nationality
        self.Nationality_of_the_mother = Nationality_of_the_mother
        self.Tribe = Tribe
        self.Legitimate_vision = Legitimate_vision
        self.Salary = Salary
        self.Marital_status_of_the_proposer = Marital_status_of_the_proposer
        self.Educational_status = Educational_status
        self.Other_district = Other_district
        self.Accept_multi_marriage = Accept_multi_marriage
        self.Relation_with_proposal = Relation_with_proposal
        
        pass
    @property
    def Nationality_of_the_mother(self):
        return self.__Nationality_of_the_mother
    @Nationality_of_the_mother.setter
    def Nationality_of_the_mother(self, Nationality_of_the_mother: str):
        self.__Nationality_of_the_mother = Nationality_of_the_mother

    @property
    def Salary(self):
        return self.__Salary
    @Salary.setter
    def Salary(self, Salary: str):
        self.__Salary = Salary

    @property
    def Relation_with_proposal(self):
        return self.__Relation_with_proposal
    @Relation_with_proposal.setter
    def Relation_with_proposal(self, Relation_with_proposal: str):
        self.__Relation_with_proposal = Relation_with_proposal

    @property
    def Legitimate_vision(self):
        return self.__Legitimate_vision
    @Legitimate_vision.setter
    def Legitimate_vision(self, Legitimate_vision: str):
        self.__Legitimate_vision = Legitimate_vision

    @property
    def Nationality(self):
        return self.__Nationality
    @Nationality.setter
    def Nationality(self, Nationality: str):
        self.__Nationality = Nationality

    @property
    def Marital_status_of_the_proposer(self):
        return self.__Marital_status_of_the_proposer
    @Marital_status_of_the_proposer.setter
    def Marital_status_of_the_proposer(self, Marital_status_of_the_proposer: str):
        self.__Marital_status_of_the_proposer = Marital_status_of_the_proposer

    @property
    def Educational_status(self):
        return self.__Educational_status
    @Educational_status.setter
    def Educational_status(self, Educational_status: str):
        self.__Educational_status = Educational_status

    @property
    def Tribe(self):
        return self.__Tribe
    @Tribe.setter
    def Tribe(self, Tribe: str):
        self.__Tribe = Tribe

    @property
    def Other_district(self):
        return self.__Other_district
    @Other_district.setter
    def Other_district(self, Other_district: str):
        self.__Other_district = Other_district

    @property
    def Accept_multi_marriage(self):
        return self.__Accept_multi_marriage
    @Accept_multi_marriage.setter
    def Accept_multi_marriage(self, Accept_multi_marriage: str):
        self.__Accept_multi_marriage = Accept_multi_marriage



class Amount:

    def __init__(self, Amount: int, Subvention_date: str, Month: int, care36: "Care" = None):
        self.Amount = Amount
        self.Subvention_date = Subvention_date
        self.Month = Month
        self.care36 = care36
        
        pass
    @property
    def Month(self):
        return self.__Month
    @Month.setter
    def Month(self, Month: int):
        self.__Month = Month

    @property
    def Subvention_date(self):
        return self.__Subvention_date
    @Subvention_date.setter
    def Subvention_date(self, Subvention_date: str):
        self.__Subvention_date = Subvention_date

    @property
    def Amount(self):
        return self.__Amount
    @Amount.setter
    def Amount(self, Amount: int):
        self.__Amount = Amount

    @property
    def care36(self):
        return self.__care36
    @care36.setter
    def care36(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Amount__care36", None)
        self.__care36 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "the_amount37"):
                opp_val = getattr(old_value, "the_amount37", None)
                if opp_val == self:
                    setattr(old_value, "the_amount37", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "the_amount37"):
                opp_val = getattr(value, "the_amount37", None)
                setattr(value, "the_amount37", self)



class Beneficiary:

    def __init__(self, House_number: int, Date_of_birth: str, Phone: int, Scientific_qualification: str, Marital_status: str, Beneficiary__ID: int, F_name: str, L_name: str, Address: str, District: str, Job: str, Data_entry35: "_20Data_20entry_external" = None):
        self.House_number = House_number
        self.Date_of_birth = Date_of_birth
        self.Phone = Phone
        self.Scientific_qualification = Scientific_qualification
        self.Marital_status = Marital_status
        self.Beneficiary__ID = Beneficiary__ID
        self.F_name = F_name
        self.L_name = L_name
        self.Address = Address
        self.District = District
        self.Job = Job
        self.Data_entry35 = Data_entry35
        
        pass
    @property
    def L_name(self):
        return self.__L_name
    @L_name.setter
    def L_name(self, L_name: str):
        self.__L_name = L_name

    @property
    def Marital_status(self):
        return self.__Marital_status
    @Marital_status.setter
    def Marital_status(self, Marital_status: str):
        self.__Marital_status = Marital_status

    @property
    def Phone(self):
        return self.__Phone
    @Phone.setter
    def Phone(self, Phone: int):
        self.__Phone = Phone

    @property
    def Scientific_qualification(self):
        return self.__Scientific_qualification
    @Scientific_qualification.setter
    def Scientific_qualification(self, Scientific_qualification: str):
        self.__Scientific_qualification = Scientific_qualification

    @property
    def Address(self):
        return self.__Address
    @Address.setter
    def Address(self, Address: str):
        self.__Address = Address

    @property
    def Date_of_birth(self):
        return self.__Date_of_birth
    @Date_of_birth.setter
    def Date_of_birth(self, Date_of_birth: str):
        self.__Date_of_birth = Date_of_birth

    @property
    def District(self):
        return self.__District
    @District.setter
    def District(self, District: str):
        self.__District = District

    @property
    def House_number(self):
        return self.__House_number
    @House_number.setter
    def House_number(self, House_number: int):
        self.__House_number = House_number

    @property
    def F_name(self):
        return self.__F_name
    @F_name.setter
    def F_name(self, F_name: str):
        self.__F_name = F_name

    @property
    def Job(self):
        return self.__Job
    @Job.setter
    def Job(self, Job: str):
        self.__Job = Job

    @property
    def Beneficiary__ID(self):
        return self.__Beneficiary__ID
    @Beneficiary__ID.setter
    def Beneficiary__ID(self, Beneficiary__ID: int):
        self.__Beneficiary__ID = Beneficiary__ID

    @property
    def Data_entry35(self):
        return self.__Data_entry35
    @Data_entry35.setter
    def Data_entry35(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Beneficiary__Data_entry35", None)
        self.__Data_entry35 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Beneficiary34"):
                opp_val = getattr(old_value, "Beneficiary34", None)
                if opp_val == self:
                    setattr(old_value, "Beneficiary34", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Beneficiary34"):
                opp_val = getattr(value, "Beneficiary34", None)
                setattr(value, "Beneficiary34", self)



class Volunteer:

    def __init__(self, Volunteer_ID: int, Age: int, Time_of_volunteering: str, Preparing_event: str, Design_and_montag: str, Public_relations: str, Decor__and_aesthetic_touches: str, Organization: str, Professional_status: str):
        self.Volunteer_ID = Volunteer_ID
        self.Age = Age
        self.Time_of_volunteering = Time_of_volunteering
        self.Preparing_event = Preparing_event
        self.Design_and_montag = Design_and_montag
        self.Public_relations = Public_relations
        self.Decor__and_aesthetic_touches = Decor__and_aesthetic_touches
        self.Organization = Organization
        self.Professional_status = Professional_status
        
        pass
    @property
    def Organization(self):
        return self.__Organization
    @Organization.setter
    def Organization(self, Organization: str):
        self.__Organization = Organization

    @property
    def Professional_status(self):
        return self.__Professional_status
    @Professional_status.setter
    def Professional_status(self, Professional_status: str):
        self.__Professional_status = Professional_status

    @property
    def Age(self):
        return self.__Age
    @Age.setter
    def Age(self, Age: int):
        self.__Age = Age

    @property
    def Time_of_volunteering(self):
        return self.__Time_of_volunteering
    @Time_of_volunteering.setter
    def Time_of_volunteering(self, Time_of_volunteering: str):
        self.__Time_of_volunteering = Time_of_volunteering

    @property
    def Preparing_event(self):
        return self.__Preparing_event
    @Preparing_event.setter
    def Preparing_event(self, Preparing_event: str):
        self.__Preparing_event = Preparing_event

    @property
    def Public_relations(self):
        return self.__Public_relations
    @Public_relations.setter
    def Public_relations(self, Public_relations: str):
        self.__Public_relations = Public_relations

    @property
    def Design_and_montag(self):
        return self.__Design_and_montag
    @Design_and_montag.setter
    def Design_and_montag(self, Design_and_montag: str):
        self.__Design_and_montag = Design_and_montag

    @property
    def Volunteer_ID(self):
        return self.__Volunteer_ID
    @Volunteer_ID.setter
    def Volunteer_ID(self, Volunteer_ID: int):
        self.__Volunteer_ID = Volunteer_ID

    @property
    def Decor__and_aesthetic_touches(self):
        return self.__Decor__and_aesthetic_touches
    @Decor__and_aesthetic_touches.setter
    def Decor__and_aesthetic_touches(self, Decor__and_aesthetic_touches: str):
        self.__Decor__and_aesthetic_touches = Decor__and_aesthetic_touches



class Honor_member:

    def __init__(self, Member_start_date: str, Amount_of_partnership: int):
        self.Member_start_date = Member_start_date
        self.Amount_of_partnership = Amount_of_partnership
        
        pass
    @property
    def Amount_of_partnership(self):
        return self.__Amount_of_partnership
    @Amount_of_partnership.setter
    def Amount_of_partnership(self, Amount_of_partnership: int):
        self.__Amount_of_partnership = Amount_of_partnership

    @property
    def Member_start_date(self):
        return self.__Member_start_date
    @Member_start_date.setter
    def Member_start_date(self, Member_start_date: str):
        self.__Member_start_date = Member_start_date



class Member:

    def __init__(self, F_name: str, L_name: str, Job: str, Mobile_number: int, Scientific_qualifications: str, Email_address: str, Vacation_type: str):
        self.F_name = F_name
        self.L_name = L_name
        self.Job = Job
        self.Mobile_number = Mobile_number
        self.Scientific_qualifications = Scientific_qualifications
        self.Email_address = Email_address
        self.Vacation_type = Vacation_type
        
        pass
    @property
    def Mobile_number(self):
        return self.__Mobile_number
    @Mobile_number.setter
    def Mobile_number(self, Mobile_number: int):
        self.__Mobile_number = Mobile_number

    @property
    def L_name(self):
        return self.__L_name
    @L_name.setter
    def L_name(self, L_name: str):
        self.__L_name = L_name

    @property
    def Scientific_qualifications(self):
        return self.__Scientific_qualifications
    @Scientific_qualifications.setter
    def Scientific_qualifications(self, Scientific_qualifications: str):
        self.__Scientific_qualifications = Scientific_qualifications

    @property
    def Vacation_type(self):
        return self.__Vacation_type
    @Vacation_type.setter
    def Vacation_type(self, Vacation_type: str):
        self.__Vacation_type = Vacation_type

    @property
    def Job(self):
        return self.__Job
    @Job.setter
    def Job(self, Job: str):
        self.__Job = Job

    @property
    def Email_address(self):
        return self.__Email_address
    @Email_address.setter
    def Email_address(self, Email_address: str):
        self.__Email_address = Email_address

    @property
    def F_name(self):
        return self.__F_name
    @F_name.setter
    def F_name(self, F_name: str):
        self.__F_name = F_name



class Data_entry:

    def __init__(self, attribute: str, attribute2: str, the_member41: "The_20member_external" = None):
        self.attribute = attribute
        self.attribute2 = attribute2
        self.the_member41 = the_member41
        
        pass
    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def the_member41(self):
        return self.__the_member41
    @the_member41.setter
    def the_member41(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Data_entry__the_member41", None)
        self.__the_member41 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Data_entry40"):
                opp_val = getattr(old_value, "Data_entry40", None)
                if opp_val == self:
                    setattr(old_value, "Data_entry40", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Data_entry40"):
                opp_val = getattr(value, "Data_entry40", None)
                setattr(value, "Data_entry40", self)



class Origination:

    def __init__(self, Logo: str, Full_name: str, Executive_manager: str, General_supervisor: str, Admin_The_origination_133: "Admin" = None):
        self.Logo = Logo
        self.Full_name = Full_name
        self.Executive_manager = Executive_manager
        self.General_supervisor = General_supervisor
        self.Admin_The_origination_133 = Admin_The_origination_133
        
        pass
    @property
    def Full_name(self):
        return self.__Full_name
    @Full_name.setter
    def Full_name(self, Full_name: str):
        self.__Full_name = Full_name

    @property
    def Logo(self):
        return self.__Logo
    @Logo.setter
    def Logo(self, Logo: str):
        self.__Logo = Logo

    @property
    def Executive_manager(self):
        return self.__Executive_manager
    @Executive_manager.setter
    def Executive_manager(self, Executive_manager: str):
        self.__Executive_manager = Executive_manager

    @property
    def General_supervisor(self):
        return self.__General_supervisor
    @General_supervisor.setter
    def General_supervisor(self, General_supervisor: str):
        self.__General_supervisor = General_supervisor

    @property
    def Admin_The_origination_133(self):
        return self.__Admin_The_origination_133
    @Admin_The_origination_133.setter
    def Admin_The_origination_133(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Origination__Admin_The_origination_133", None)
        self.__Admin_The_origination_133 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin_The_origination_032"):
                opp_val = getattr(old_value, "Admin_The_origination_032", None)
                if opp_val == self:
                    setattr(old_value, "Admin_The_origination_032", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin_The_origination_032"):
                opp_val = getattr(value, "Admin_The_origination_032", None)
                setattr(value, "Admin_The_origination_032", self)



class Admin:

    def __init__(self, ID: int, User_name: str, Password: int, Admin_The_origination_032: "Origination" = None, employee43: "Employee" = None):
        self.ID = ID
        self.User_name = User_name
        self.Password = Password
        self.Admin_The_origination_032 = Admin_The_origination_032
        self.employee43 = employee43
        
        pass
    @property
    def User_name(self):
        return self.__User_name
    @User_name.setter
    def User_name(self, User_name: str):
        self.__User_name = User_name

    @property
    def ID(self):
        return self.__ID
    @ID.setter
    def ID(self, ID: int):
        self.__ID = ID

    @property
    def Password(self):
        return self.__Password
    @Password.setter
    def Password(self, Password: int):
        self.__Password = Password

    @property
    def Admin_The_origination_032(self):
        return self.__Admin_The_origination_032
    @Admin_The_origination_032.setter
    def Admin_The_origination_032(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__Admin_The_origination_032", None)
        self.__Admin_The_origination_032 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Admin_The_origination_133"):
                opp_val = getattr(old_value, "Admin_The_origination_133", None)
                if opp_val == self:
                    setattr(old_value, "Admin_The_origination_133", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Admin_The_origination_133"):
                opp_val = getattr(value, "Admin_The_origination_133", None)
                setattr(value, "Admin_The_origination_133", self)

    @property
    def employee43(self):
        return self.__employee43
    @employee43.setter
    def employee43(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Admin__employee43", None)
        self.__employee43 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "admin42"):
                opp_val = getattr(old_value, "admin42", None)
                if opp_val == self:
                    setattr(old_value, "admin42", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "admin42"):
                opp_val = getattr(value, "admin42", None)
                setattr(value, "admin42", self)

