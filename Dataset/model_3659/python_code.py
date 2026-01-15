from datetime import datetime, date, time
from enum import Enum

############################################
# Definition of Enumerations
############################################

class ProjectSize(Enum):
    small = "small"
    medium = "medium"
    big = "big"
class ProjectStatus(Enum):
    planned = "planned"
    active = "active"
    finished = "finished"
    suspended = "suspended"


############################################
# Definition of Classes
############################################

class Project:

    pass
class Projects_Training(Project):

    pass
class Projects_Worker:

    def __init__(self, nickname: str, salary: int, employees: "Projects_Company" = None, workers: set["Projects_Qualification"] = None, members: set["Projects_Project"] = None, Worker: "Projects_Company" = None, Worker21: "Projects_Qualification" = None, Worker10: "Projects_Project" = None):
        self.nickname = nickname
        self.salary = salary
        self.employees = employees
        self.workers = workers if workers is not None else set()
        self.members = members if members is not None else set()
        self.Worker = Worker
        self.Worker21 = Worker21
        self.Worker10 = Worker10
        
    @property
    def salary(self) -> int:
        return self.__salary

    @salary.setter
    def salary(self, salary: int):
        self.__salary = salary

    @property
    def nickname(self) -> str:
        return self.__nickname

    @nickname.setter
    def nickname(self, nickname: str):
        self.__nickname = nickname

    @property
    def Worker10(self):
        return self.__Worker10

    @Worker10.setter
    def Worker10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Worker__Worker10", None)
        self.__Worker10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projects9"):
                opp_val = getattr(old_value, "projects9", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projects9"):
                opp_val = getattr(value, "projects9", None)
                if opp_val is None:
                    setattr(value, "projects9", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Worker(self):
        return self.__Worker

    @Worker.setter
    def Worker(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Worker__Worker", None)
        self.__Worker = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employer"):
                opp_val = getattr(old_value, "employer", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employer"):
                opp_val = getattr(value, "employer", None)
                if opp_val is None:
                    setattr(value, "employer", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Worker21(self):
        return self.__Worker21

    @Worker21.setter
    def Worker21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Worker__Worker21", None)
        self.__Worker21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "qualifications"):
                opp_val = getattr(old_value, "qualifications", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "qualifications"):
                opp_val = getattr(value, "qualifications", None)
                if opp_val is None:
                    setattr(value, "qualifications", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def workers(self):
        return self.__workers

    @workers.setter
    def workers(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Worker__workers", None)
        self.__workers = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Qualification"):
                    opp_val = getattr(item, "Qualification", None)
                    
                    if opp_val == self:
                        setattr(item, "Qualification", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Qualification"):
                    opp_val = getattr(item, "Qualification", None)
                    
                    setattr(item, "Qualification", self)
                    

    @property
    def employees(self):
        return self.__employees

    @employees.setter
    def employees(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Worker__employees", None)
        self.__employees = value
        
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
    def members(self):
        return self.__members

    @members.setter
    def members(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Worker__members", None)
        self.__members = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project5"):
                    opp_val = getattr(item, "Project5", None)
                    
                    if opp_val == self:
                        setattr(item, "Project5", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project5"):
                    opp_val = getattr(item, "Project5", None)
                    
                    setattr(item, "Project5", self)
                    

    def isOverloaded(self) -> bool:
        # TODO: Implement isOverloaded method
        pass

class Projects_Qualification:

    def __init__(self, description: str, Qualification: "Projects_Worker" = None, Qualification13: "Projects_Project" = None, qualifications: set["Projects_Worker"] = None, requirements: set["Projects_Project"] = None, trained: "Projects_Training" = None, Qualification26: "Projects_Training" = None):
        self.description = description
        self.Qualification = Qualification
        self.Qualification13 = Qualification13
        self.qualifications = qualifications if qualifications is not None else set()
        self.requirements = requirements if requirements is not None else set()
        self.trained = trained
        self.Qualification26 = Qualification26
        
    @property
    def description(self) -> str:
        return self.__description

    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def Qualification13(self):
        return self.__Qualification13

    @Qualification13.setter
    def Qualification13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Qualification__Qualification13", None)
        self.__Qualification13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projects12"):
                opp_val = getattr(old_value, "projects12", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projects12"):
                opp_val = getattr(value, "projects12", None)
                if opp_val is None:
                    setattr(value, "projects12", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def qualifications(self):
        return self.__qualifications

    @qualifications.setter
    def qualifications(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Qualification__qualifications", None)
        self.__qualifications = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Worker21"):
                    opp_val = getattr(item, "Worker21", None)
                    
                    if opp_val == self:
                        setattr(item, "Worker21", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Worker21"):
                    opp_val = getattr(item, "Worker21", None)
                    
                    setattr(item, "Worker21", self)
                    

    @property
    def trained(self):
        return self.__trained

    @trained.setter
    def trained(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Qualification__trained", None)
        self.__trained = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Training"):
                opp_val = getattr(old_value, "Training", None)
                if opp_val == self:
                    setattr(old_value, "Training", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Training"):
                opp_val = getattr(value, "Training", None)
                setattr(value, "Training", self)

    @property
    def requirements(self):
        return self.__requirements

    @requirements.setter
    def requirements(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Qualification__requirements", None)
        self.__requirements = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project23"):
                    opp_val = getattr(item, "Project23", None)
                    
                    if opp_val == self:
                        setattr(item, "Project23", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project23"):
                    opp_val = getattr(item, "Project23", None)
                    
                    setattr(item, "Project23", self)
                    

    @property
    def Qualification26(self):
        return self.__Qualification26

    @Qualification26.setter
    def Qualification26(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Qualification__Qualification26", None)
        self.__Qualification26 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "trainings"):
                opp_val = getattr(old_value, "trainings", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "trainings"):
                opp_val = getattr(value, "trainings", None)
                if opp_val is None:
                    setattr(value, "trainings", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Qualification(self):
        return self.__Qualification

    @Qualification.setter
    def Qualification(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Qualification__Qualification", None)
        self.__Qualification = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "workers"):
                opp_val = getattr(old_value, "workers", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "workers"):
                opp_val = getattr(value, "workers", None)
                if opp_val is None:
                    setattr(value, "workers", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

class Projects_Company:

    def __init__(self, name: str, company: set["Projects_Project"] = None, Company: "Projects_Worker" = None, Company7: "Projects_Project" = None, employer: set["Projects_Worker"] = None):
        self.name = name
        self.company = company if company is not None else set()
        self.Company = Company
        self.Company7 = Company7
        self.employer = employer if employer is not None else set()
        
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
        old_value = getattr(self, f"_Projects_Company__company", None)
        self.__company = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project"):
                    opp_val = getattr(item, "Project", None)
                    
                    if opp_val == self:
                        setattr(item, "Project", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project"):
                    opp_val = getattr(item, "Project", None)
                    
                    setattr(item, "Project", self)
                    

    @property
    def employer(self):
        return self.__employer

    @employer.setter
    def employer(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Company__employer", None)
        self.__employer = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Worker"):
                    opp_val = getattr(item, "Worker", None)
                    
                    if opp_val == self:
                        setattr(item, "Worker", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Worker"):
                    opp_val = getattr(item, "Worker", None)
                    
                    setattr(item, "Worker", self)
                    

    @property
    def Company(self):
        return self.__Company

    @Company.setter
    def Company(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Company__Company", None)
        self.__Company = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "employees"):
                opp_val = getattr(old_value, "employees", None)
                if opp_val == self:
                    setattr(old_value, "employees", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "employees"):
                opp_val = getattr(value, "employees", None)
                setattr(value, "employees", self)

    @property
    def Company7(self):
        return self.__Company7

    @Company7.setter
    def Company7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Company__Company7", None)
        self.__Company7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "projects"):
                opp_val = getattr(old_value, "projects", None)
                if opp_val == self:
                    setattr(old_value, "projects", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "projects"):
                opp_val = getattr(value, "projects", None)
                setattr(value, "projects", self)

    def hire(self, w: str):
        # TODO: Implement hire method
        pass

    def start(self, p: str):
        # TODO: Implement start method
        pass

    def createProject(self, ws: str, n: str, qs: str, s: str) -> str:
        # TODO: Implement createProject method
        pass

    def createWorker(self, qs: str) -> str:
        # TODO: Implement createWorker method
        pass

    def finish(self, p: str):
        # TODO: Implement finish method
        pass

    def fire(self, w: str):
        # TODO: Implement fire method
        pass

class Projects_Project:

    def __init__(self, name: str, size: str, status: str, Project: "Projects_Company" = None, Project5: "Projects_Worker" = None, projects: "Projects_Company" = None, projects12: set["Projects_Qualification"] = None, Project16: "Projects_Project" = None, successors: set["Projects_Project"] = None, Project19: "Projects_Project" = None, predecessors: set["Projects_Project"] = None, Project23: "Projects_Qualification" = None, projects9: set["Projects_Worker"] = None):
        self.name = name
        self.size = size
        self.status = status
        self.Project = Project
        self.Project5 = Project5
        self.projects = projects
        self.projects12 = projects12 if projects12 is not None else set()
        self.Project16 = Project16
        self.successors = successors if successors is not None else set()
        self.Project19 = Project19
        self.predecessors = predecessors if predecessors is not None else set()
        self.Project23 = Project23
        self.projects9 = projects9 if projects9 is not None else set()
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name

    @property
    def size(self) -> str:
        return self.__size

    @size.setter
    def size(self, size: str):
        self.__size = size

    @property
    def status(self) -> str:
        return self.__status

    @status.setter
    def status(self, status: str):
        self.__status = status

    @property
    def Project16(self):
        return self.__Project16

    @Project16.setter
    def Project16(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Project16", None)
        self.__Project16 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "successors"):
                opp_val = getattr(old_value, "successors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "successors"):
                opp_val = getattr(value, "successors", None)
                if opp_val is None:
                    setattr(value, "successors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def projects9(self):
        return self.__projects9

    @projects9.setter
    def projects9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__projects9", None)
        self.__projects9 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Worker10"):
                    opp_val = getattr(item, "Worker10", None)
                    
                    if opp_val == self:
                        setattr(item, "Worker10", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Worker10"):
                    opp_val = getattr(item, "Worker10", None)
                    
                    setattr(item, "Worker10", self)
                    

    @property
    def successors(self):
        return self.__successors

    @successors.setter
    def successors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__successors", None)
        self.__successors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project16"):
                    opp_val = getattr(item, "Project16", None)
                    
                    if opp_val == self:
                        setattr(item, "Project16", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project16"):
                    opp_val = getattr(item, "Project16", None)
                    
                    setattr(item, "Project16", self)
                    

    @property
    def Project(self):
        return self.__Project

    @Project.setter
    def Project(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Project", None)
        self.__Project = value
        
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

    @property
    def Project23(self):
        return self.__Project23

    @Project23.setter
    def Project23(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Project23", None)
        self.__Project23 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "requirements"):
                opp_val = getattr(old_value, "requirements", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "requirements"):
                opp_val = getattr(value, "requirements", None)
                if opp_val is None:
                    setattr(value, "requirements", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def projects(self):
        return self.__projects

    @projects.setter
    def projects(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__projects", None)
        self.__projects = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Company7"):
                opp_val = getattr(old_value, "Company7", None)
                if opp_val == self:
                    setattr(old_value, "Company7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Company7"):
                opp_val = getattr(value, "Company7", None)
                setattr(value, "Company7", self)

    @property
    def predecessors(self):
        return self.__predecessors

    @predecessors.setter
    def predecessors(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__predecessors", None)
        self.__predecessors = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Project19"):
                    opp_val = getattr(item, "Project19", None)
                    
                    if opp_val == self:
                        setattr(item, "Project19", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Project19"):
                    opp_val = getattr(item, "Project19", None)
                    
                    setattr(item, "Project19", self)
                    

    @property
    def projects12(self):
        return self.__projects12

    @projects12.setter
    def projects12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__projects12", None)
        self.__projects12 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Qualification13"):
                    opp_val = getattr(item, "Qualification13", None)
                    
                    if opp_val == self:
                        setattr(item, "Qualification13", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Qualification13"):
                    opp_val = getattr(item, "Qualification13", None)
                    
                    setattr(item, "Qualification13", self)
                    

    @property
    def Project19(self):
        return self.__Project19

    @Project19.setter
    def Project19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Project19", None)
        self.__Project19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "predecessors"):
                opp_val = getattr(old_value, "predecessors", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "predecessors"):
                opp_val = getattr(value, "predecessors", None)
                if opp_val is None:
                    setattr(value, "predecessors", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Project5(self):
        return self.__Project5

    @Project5.setter
    def Project5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Projects_Project__Project5", None)
        self.__Project5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "members"):
                opp_val = getattr(old_value, "members", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "members"):
                opp_val = getattr(value, "members", None)
                if opp_val is None:
                    setattr(value, "members", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    def missingQualifications(self) -> str:
        # TODO: Implement missingQualifications method
        pass

    def isHelpful(self, w: str) -> bool:
        # TODO: Implement isHelpful method
        pass
