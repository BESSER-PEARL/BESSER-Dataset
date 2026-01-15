from datetime import datetime, date, time
from abc import ABC, abstractmethod


############################################
# Definition of Classes
############################################

class CandidateKey:

    pass
class fds_PrimaryKey(CandidateKey):

    pass
class Restriction:

    pass
class fds_CandidateKey(Restriction):

    pass
class fds_ForeignKey(Restriction):

    pass
class fds_FunctionalDependency:

    pass
class NamedElement:

    pass
class fds_Column(NamedElement):

    pass
class fds_Restriction(NamedElement):

    pass
class fds_RestrictionColumn(NamedElement):

    pass
class fds_Table(NamedElement):

    pass
class fds_Database(NamedElement):

    pass
class fds_NamedElement(ABC):

    def __init__(self, name: str):
        self.name = name
        
    @property
    def name(self) -> str:
        return self.__name

    @name.setter
    def name(self, name: str):
        self.__name = name
