from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class sample_Person:

    def __init__(self, name: str, birthdate: date, Person: "sample_Group" = None, persons: "sample_Group" = None):
        self.name = name
        self.birthdate = birthdate
        self.Person = Person
        self.persons = persons
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def birthdate(self) -> date:
        return self.__birthdate

    @birthdate.setter
    def birthdate(self, birthdate: date):
        self.__birthdate = birthdate

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "group"):
                opp_val = getattr(old_value, "group", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "group"):
                opp_val = getattr(value, "group", None)
                if opp_val is None:
                    setattr(value, "group", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def persons(self):
        return self.__persons

    @persons.setter
    def persons(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Person__persons", None)
        self.__persons = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Group7"):
                opp_val = getattr(old_value, "Group7", None)
                if opp_val == self:
                    setattr(old_value, "Group7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Group7"):
                opp_val = getattr(value, "Group7", None)
                setattr(value, "Group7", self)

class sample_Group:

    def __init__(self, name: str, Group: "sample_Department" = None, group: set["sample_Person"] = None, groups: "sample_Department" = None, Group7: "sample_Person" = None):
        self.name = name
        self.Group = Group
        self.group = group if group is not None else set()
        self.groups = groups
        self.Group7 = Group7
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Group(self):
        return self.__Group

    @Group.setter
    def Group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Group__Group", None)
        self.__Group = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "department"):
                opp_val = getattr(old_value, "department", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "department"):
                opp_val = getattr(value, "department", None)
                if opp_val is None:
                    setattr(value, "department", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def groups(self):
        return self.__groups

    @groups.setter
    def groups(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Group__groups", None)
        self.__groups = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Department5"):
                opp_val = getattr(old_value, "Department5", None)
                if opp_val == self:
                    setattr(old_value, "Department5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Department5"):
                opp_val = getattr(value, "Department5", None)
                setattr(value, "Department5", self)

    @property
    def group(self):
        return self.__group

    @group.setter
    def group(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Group__group", None)
        self.__group = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    if opp_val == self:
                        setattr(item, "Person", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Person"):
                    opp_val = getattr(item, "Person", None)
                    
                    setattr(item, "Person", self)
                    

    @property
    def Group7(self):
        return self.__Group7

    @Group7.setter
    def Group7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Group__Group7", None)
        self.__Group7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "persons"):
                opp_val = getattr(old_value, "persons", None)
                if opp_val == self:
                    setattr(old_value, "persons", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "persons"):
                opp_val = getattr(value, "persons", None)
                setattr(value, "persons", self)

class sample_Department:

    def __init__(self, name: str, Department: "sample_Company" = None, department: set["sample_Group"] = None, departments: "sample_Company" = None, Department5: "sample_Group" = None):
        self.name = name
        self.Department = Department
        self.department = department if department is not None else set()
        self.departments = departments
        self.Department5 = Department5
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def department(self):
        return self.__department

    @department.setter
    def department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Department__department", None)
        self.__department = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    if opp_val == self:
                        setattr(item, "Group", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Group"):
                    opp_val = getattr(item, "Group", None)
                    
                    setattr(item, "Group", self)
                    

    @property
    def Department5(self):
        return self.__Department5

    @Department5.setter
    def Department5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Department__Department5", None)
        self.__Department5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "groups"):
                opp_val = getattr(old_value, "groups", None)
                if opp_val == self:
                    setattr(old_value, "groups", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "groups"):
                opp_val = getattr(value, "groups", None)
                setattr(value, "groups", self)

    @property
    def departments(self):
        return self.__departments

    @departments.setter
    def departments(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Department__departments", None)
        self.__departments = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company"):
                opp_val = getattr(old_value, "Company", None)
                if opp_val == self:
                    setattr(old_value, "Company", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company"):
                opp_val = getattr(value, "Company", None)
                setattr(value, "Company", self)

    @property
    def Department(self):
        return self.__Department

    @Department.setter
    def Department(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Department__Department", None)
        self.__Department = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "company"):
                opp_val = getattr(old_value, "company", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "company"):
                opp_val = getattr(value, "company", None)
                if opp_val is None:
                    setattr(value, "company", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class sample_Company:

    def __init__(self, name: str, company: set["sample_Department"] = None, Company: "sample_Department" = None):
        self.name = name
        self.company = company if company is not None else set()
        self.Company = Company
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def company(self):
        return self.__company

    @company.setter
    def company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Company__company", None)
        self.__company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    if opp_val == self:
                        setattr(item, "Department", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Department"):
                    opp_val = getattr(item, "Department", None)
                    
                    setattr(item, "Department", self)
                    

    @property
    def Company(self):
        return self.__Company

    @Company.setter
    def Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_sample_Company__Company", None)
        self.__Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "departments"):
                opp_val = getattr(old_value, "departments", None)
                if opp_val == self:
                    setattr(old_value, "departments", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "departments"):
                opp_val = getattr(value, "departments", None)
                setattr(value, "departments", self)
