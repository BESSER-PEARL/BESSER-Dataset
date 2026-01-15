from datetime import datetime, date, time

############################################
# Definition of Classes
############################################

class PersonCompany_Company:

    def __init__(self, name: str, CompanyJob_Company_role_employer: set["PersonCompany_Job"] = None, Company: "PersonCompany_Job" = None):
        self.name = name
        self.CompanyJob_Company_role_employer = CompanyJob_Company_role_employer if CompanyJob_Company_role_employer is not None else set()
        self.Company = Company
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def CompanyJob_Company_role_employer(self):
        return self.__CompanyJob_Company_role_employer

    @CompanyJob_Company_role_employer.setter
    def CompanyJob_Company_role_employer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Company__CompanyJob_Company_role_employer", None)
        self.__CompanyJob_Company_role_employer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Job2"):
                    opp_val = getattr(item, "Job2", None)
                    
                    if opp_val == self:
                        setattr(item, "Job2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Job2"):
                    opp_val = getattr(item, "Job2", None)
                    
                    setattr(item, "Job2", self)
                    

    @property
    def Company(self):
        return self.__Company

    @Company.setter
    def Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Company__Company", None)
        self.__Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyJob_Job_role_job"):
                opp_val = getattr(old_value, "CompanyJob_Job_role_job", None)
                if opp_val == self:
                    setattr(old_value, "CompanyJob_Job_role_job", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyJob_Job_role_job"):
                opp_val = getattr(value, "CompanyJob_Job_role_job", None)
                setattr(value, "CompanyJob_Job_role_job", self)

    def employee(self) -> str:
        # TODO: Implement employee method
        pass

class PersonCompany_Job:

    def __init__(self, salary: int, Job: "PersonCompany_Person" = None, Job2: "PersonCompany_Company" = None, PersonJob_Job_role_job: "PersonCompany_Person" = None, CompanyJob_Job_role_job: "PersonCompany_Company" = None, Job7: "PersonCompany_Job" = None, BossWorker_Job_role_boss: set["PersonCompany_Job"] = None, Job10: "PersonCompany_Job" = None, BossWorker_Job_role_worker: "PersonCompany_Job" = None):
        self.salary = salary
        self.Job = Job
        self.Job2 = Job2
        self.PersonJob_Job_role_job = PersonJob_Job_role_job
        self.CompanyJob_Job_role_job = CompanyJob_Job_role_job
        self.Job7 = Job7
        self.BossWorker_Job_role_boss = BossWorker_Job_role_boss if BossWorker_Job_role_boss is not None else set()
        self.Job10 = Job10
        self.BossWorker_Job_role_worker = BossWorker_Job_role_worker
        
    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def BossWorker_Job_role_worker(self):
        return self.__BossWorker_Job_role_worker

    @BossWorker_Job_role_worker.setter
    def BossWorker_Job_role_worker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Job__BossWorker_Job_role_worker", None)
        self.__BossWorker_Job_role_worker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Job10"):
                opp_val = getattr(old_value, "Job10", None)
                if opp_val == self:
                    setattr(old_value, "Job10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Job10"):
                opp_val = getattr(value, "Job10", None)
                setattr(value, "Job10", self)

    @property
    def Job7(self):
        return self.__Job7

    @Job7.setter
    def Job7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Job__Job7", None)
        self.__Job7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BossWorker_Job_role_boss"):
                opp_val = getattr(old_value, "BossWorker_Job_role_boss", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BossWorker_Job_role_boss"):
                opp_val = getattr(value, "BossWorker_Job_role_boss", None)
                if opp_val is None:
                    setattr(value, "BossWorker_Job_role_boss", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Job2(self):
        return self.__Job2

    @Job2.setter
    def Job2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Job__Job2", None)
        self.__Job2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "CompanyJob_Company_role_employer"):
                opp_val = getattr(old_value, "CompanyJob_Company_role_employer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "CompanyJob_Company_role_employer"):
                opp_val = getattr(value, "CompanyJob_Company_role_employer", None)
                if opp_val is None:
                    setattr(value, "CompanyJob_Company_role_employer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def PersonJob_Job_role_job(self):
        return self.__PersonJob_Job_role_job

    @PersonJob_Job_role_job.setter
    def PersonJob_Job_role_job(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Job__PersonJob_Job_role_job", None)
        self.__PersonJob_Job_role_job = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Person"):
                opp_val = getattr(old_value, "Person", None)
                if opp_val == self:
                    setattr(old_value, "Person", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Person"):
                opp_val = getattr(value, "Person", None)
                setattr(value, "Person", self)

    @property
    def Job10(self):
        return self.__Job10

    @Job10.setter
    def Job10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Job__Job10", None)
        self.__Job10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "BossWorker_Job_role_worker"):
                opp_val = getattr(old_value, "BossWorker_Job_role_worker", None)
                if opp_val == self:
                    setattr(old_value, "BossWorker_Job_role_worker", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "BossWorker_Job_role_worker"):
                opp_val = getattr(value, "BossWorker_Job_role_worker", None)
                setattr(value, "BossWorker_Job_role_worker", self)

    @property
    def BossWorker_Job_role_boss(self):
        return self.__BossWorker_Job_role_boss

    @BossWorker_Job_role_boss.setter
    def BossWorker_Job_role_boss(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Job__BossWorker_Job_role_boss", None)
        self.__BossWorker_Job_role_boss = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Job7"):
                    opp_val = getattr(item, "Job7", None)
                    
                    if opp_val == self:
                        setattr(item, "Job7", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Job7"):
                    opp_val = getattr(item, "Job7", None)
                    
                    setattr(item, "Job7", self)
                    

    @property
    def Job(self):
        return self.__Job

    @Job.setter
    def Job(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Job__Job", None)
        self.__Job = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonJob_Person_role_employee"):
                opp_val = getattr(old_value, "PersonJob_Person_role_employee", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonJob_Person_role_employee"):
                opp_val = getattr(value, "PersonJob_Person_role_employee", None)
                if opp_val is None:
                    setattr(value, "PersonJob_Person_role_employee", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def CompanyJob_Job_role_job(self):
        return self.__CompanyJob_Job_role_job

    @CompanyJob_Job_role_job.setter
    def CompanyJob_Job_role_job(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Job__CompanyJob_Job_role_job", None)
        self.__CompanyJob_Job_role_job = value
        
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

    def workerPlusOnSet(self, s: str) -> str:
        # TODO: Implement workerPlusOnSet method
        pass

    def bossPlus(self) -> str:
        # TODO: Implement bossPlus method
        pass

    def workerPlus(self) -> str:
        # TODO: Implement workerPlus method
        pass

class PersonCompany_Person:

    def __init__(self, name: str, PersonJob_Person_role_employee: set["PersonCompany_Job"] = None, Person: "PersonCompany_Job" = None):
        self.name = name
        self.PersonJob_Person_role_employee = PersonJob_Person_role_employee if PersonJob_Person_role_employee is not None else set()
        self.Person = Person
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def Person(self):
        return self.__Person

    @Person.setter
    def Person(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Person__Person", None)
        self.__Person = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "PersonJob_Job_role_job"):
                opp_val = getattr(old_value, "PersonJob_Job_role_job", None)
                if opp_val == self:
                    setattr(old_value, "PersonJob_Job_role_job", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "PersonJob_Job_role_job"):
                opp_val = getattr(value, "PersonJob_Job_role_job", None)
                setattr(value, "PersonJob_Job_role_job", self)

    @property
    def PersonJob_Person_role_employee(self):
        return self.__PersonJob_Person_role_employee

    @PersonJob_Person_role_employee.setter
    def PersonJob_Person_role_employee(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_PersonCompany_Person__PersonJob_Person_role_employee", None)
        self.__PersonJob_Person_role_employee = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Job"):
                    opp_val = getattr(item, "Job", None)
                    
                    if opp_val == self:
                        setattr(item, "Job", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Job"):
                    opp_val = getattr(item, "Job", None)
                    
                    setattr(item, "Job", self)
                    

    def employer(self) -> str:
        # TODO: Implement employer method
        pass
