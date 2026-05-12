from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################







class Benutzer_Actor:

    pass


class Supervisor_Actor:

    pass





class Kalendarische_Ansicht_ver_ndern_external:

    pass


class PDF_Datei_erstellen_external:

    pass


class Pr_fungen_sehen_external:

    pass


class Pr_fungstermine_verschieben_external:

    pass


class Pr_fungsplaner_einsehen_external:

    pass


class Im_LTS_anmelden_external:

    pass


class Pr_funungen_einsehen_external:

    pass


class ExaminationDate:

    def __init__(self, attribute: str, attribute2: str):
        self.attribute = attribute
        self.attribute2 = attribute2
        
        pass
    @property
    def attribute2(self):
        return self.__attribute2
    @attribute2.setter
    def attribute2(self, attribute2: str):
        self.__attribute2 = attribute2

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute



class Pr_fungsplaner_Component:

    pass
