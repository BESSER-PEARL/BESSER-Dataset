from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Secretaire_external:

    pass


class ResultatExamen:

    def __init__(self, numeroResultat: int, infoResultat: str, secretaire17: "Secretaire_external" = None, medecin18: "Medecin" = None, patient21: "Patient" = None):
        self.numeroResultat = numeroResultat
        self.infoResultat = infoResultat
        self.secretaire17 = secretaire17
        self.medecin18 = medecin18
        self.patient21 = patient21
        
        pass
    @property
    def numeroResultat(self):
        return self.__numeroResultat
    @numeroResultat.setter
    def numeroResultat(self, numeroResultat: int):
        self.__numeroResultat = numeroResultat

    @property
    def infoResultat(self):
        return self.__infoResultat
    @infoResultat.setter
    def infoResultat(self, infoResultat: str):
        self.__infoResultat = infoResultat

    @property
    def patient21(self):
        return self.__patient21
    @patient21.setter
    def patient21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ResultatExamen__patient21", None)
        self.__patient21 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resultatExamen20"):
                opp_val = getattr(old_value, "resultatExamen20", None)
                if opp_val == self:
                    setattr(old_value, "resultatExamen20", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resultatExamen20"):
                opp_val = getattr(value, "resultatExamen20", None)
                setattr(value, "resultatExamen20", self)

    @property
    def medecin18(self):
        return self.__medecin18
    @medecin18.setter
    def medecin18(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ResultatExamen__medecin18", None)
        self.__medecin18 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resultatExamen19"):
                opp_val = getattr(old_value, "resultatExamen19", None)
                if opp_val == self:
                    setattr(old_value, "resultatExamen19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resultatExamen19"):
                opp_val = getattr(value, "resultatExamen19", None)
                setattr(value, "resultatExamen19", self)

    @property
    def secretaire17(self):
        return self.__secretaire17
    @secretaire17.setter
    def secretaire17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ResultatExamen__secretaire17", None)
        self.__secretaire17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resultatExamen16"):
                opp_val = getattr(old_value, "resultatExamen16", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resultatExamen16"):
                opp_val = getattr(value, "resultatExamen16", None)
                if opp_val is None:
                    setattr(value, "resultatExamen16", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class CentreHospitalier:

    def __init__(self, numeroCentre: int, nomCentre: str, descriptionCentre: str, service15: set["Service"] = None):
        self.numeroCentre = numeroCentre
        self.nomCentre = nomCentre
        self.descriptionCentre = descriptionCentre
        self.service15 = service15 if service15 is not None else set()
        
        pass
    @property
    def nomCentre(self):
        return self.__nomCentre
    @nomCentre.setter
    def nomCentre(self, nomCentre: str):
        self.__nomCentre = nomCentre

    @property
    def descriptionCentre(self):
        return self.__descriptionCentre
    @descriptionCentre.setter
    def descriptionCentre(self, descriptionCentre: str):
        self.__descriptionCentre = descriptionCentre

    @property
    def numeroCentre(self):
        return self.__numeroCentre
    @numeroCentre.setter
    def numeroCentre(self, numeroCentre: int):
        self.__numeroCentre = numeroCentre

    @property
    def service15(self):
        return self.__service15
    @service15.setter
    def service15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CentreHospitalier__service15", None)
        self.__service15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "centreHospitalier14"):
                    opp_val = getattr(item, "centreHospitalier14", None)
                    
                    if opp_val == self:
                        setattr(item, "centreHospitalier14", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "centreHospitalier14"):
                    opp_val = getattr(item, "centreHospitalier14", None)
                    
                    setattr(item, "centreHospitalier14", self)
                    



class Programme:

    def __init__(self, numeroProgramme: str, date: str, heure: str, medecin10: "Medecin" = None):
        self.numeroProgramme = numeroProgramme
        self.date = date
        self.heure = heure
        self.medecin10 = medecin10
        
        pass
    @property
    def heure(self):
        return self.__heure
    @heure.setter
    def heure(self, heure: str):
        self.__heure = heure

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def numeroProgramme(self):
        return self.__numeroProgramme
    @numeroProgramme.setter
    def numeroProgramme(self, numeroProgramme: str):
        self.__numeroProgramme = numeroProgramme

    @property
    def medecin10(self):
        return self.__medecin10
    @medecin10.setter
    def medecin10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Programme__medecin10", None)
        self.__medecin10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme11"):
                opp_val = getattr(old_value, "programme11", None)
                if opp_val == self:
                    setattr(old_value, "programme11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme11"):
                opp_val = getattr(value, "programme11", None)
                setattr(value, "programme11", self)



class Service:

    def __init__(self, numeroService: int, nomService: str, descriptionService: str, medecin13: "Medecin" = None, centreHospitalier14: "CentreHospitalier" = None):
        self.numeroService = numeroService
        self.nomService = nomService
        self.descriptionService = descriptionService
        self.medecin13 = medecin13
        self.centreHospitalier14 = centreHospitalier14
        
        pass
    @property
    def numeroService(self):
        return self.__numeroService
    @numeroService.setter
    def numeroService(self, numeroService: int):
        self.__numeroService = numeroService

    @property
    def descriptionService(self):
        return self.__descriptionService
    @descriptionService.setter
    def descriptionService(self, descriptionService: str):
        self.__descriptionService = descriptionService

    @property
    def nomService(self):
        return self.__nomService
    @nomService.setter
    def nomService(self, nomService: str):
        self.__nomService = nomService

    @property
    def centreHospitalier14(self):
        return self.__centreHospitalier14
    @centreHospitalier14.setter
    def centreHospitalier14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__centreHospitalier14", None)
        self.__centreHospitalier14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service15"):
                opp_val = getattr(old_value, "service15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service15"):
                opp_val = getattr(value, "service15", None)
                if opp_val is None:
                    setattr(value, "service15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def medecin13(self):
        return self.__medecin13
    @medecin13.setter
    def medecin13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__medecin13", None)
        self.__medecin13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service12"):
                opp_val = getattr(old_value, "service12", None)
                if opp_val == self:
                    setattr(old_value, "service12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service12"):
                opp_val = getattr(value, "service12", None)
                setattr(value, "service12", self)



class Medecin:

    def __init__(self, numeroMedecin: int, nomMedecin: str, prenomMedecin: str, dateNaissance: str, specialite: str, rendez_Vous9: "Rendez_Vous" = None, programme11: "Programme" = None, service12: "Service" = None, resultatExamen19: "ResultatExamen" = None):
        self.numeroMedecin = numeroMedecin
        self.nomMedecin = nomMedecin
        self.prenomMedecin = prenomMedecin
        self.dateNaissance = dateNaissance
        self.specialite = specialite
        self.rendez_Vous9 = rendez_Vous9
        self.programme11 = programme11
        self.service12 = service12
        self.resultatExamen19 = resultatExamen19
        
        pass
    @property
    def numeroMedecin(self):
        return self.__numeroMedecin
    @numeroMedecin.setter
    def numeroMedecin(self, numeroMedecin: int):
        self.__numeroMedecin = numeroMedecin

    @property
    def specialite(self):
        return self.__specialite
    @specialite.setter
    def specialite(self, specialite: str):
        self.__specialite = specialite

    @property
    def nomMedecin(self):
        return self.__nomMedecin
    @nomMedecin.setter
    def nomMedecin(self, nomMedecin: str):
        self.__nomMedecin = nomMedecin

    @property
    def dateNaissance(self):
        return self.__dateNaissance
    @dateNaissance.setter
    def dateNaissance(self, dateNaissance: str):
        self.__dateNaissance = dateNaissance

    @property
    def prenomMedecin(self):
        return self.__prenomMedecin
    @prenomMedecin.setter
    def prenomMedecin(self, prenomMedecin: str):
        self.__prenomMedecin = prenomMedecin

    @property
    def programme11(self):
        return self.__programme11
    @programme11.setter
    def programme11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medecin__programme11", None)
        self.__programme11 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medecin10"):
                opp_val = getattr(old_value, "medecin10", None)
                if opp_val == self:
                    setattr(old_value, "medecin10", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medecin10"):
                opp_val = getattr(value, "medecin10", None)
                setattr(value, "medecin10", self)

    @property
    def resultatExamen19(self):
        return self.__resultatExamen19
    @resultatExamen19.setter
    def resultatExamen19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medecin__resultatExamen19", None)
        self.__resultatExamen19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medecin18"):
                opp_val = getattr(old_value, "medecin18", None)
                if opp_val == self:
                    setattr(old_value, "medecin18", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medecin18"):
                opp_val = getattr(value, "medecin18", None)
                setattr(value, "medecin18", self)

    @property
    def service12(self):
        return self.__service12
    @service12.setter
    def service12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medecin__service12", None)
        self.__service12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medecin13"):
                opp_val = getattr(old_value, "medecin13", None)
                if opp_val == self:
                    setattr(old_value, "medecin13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medecin13"):
                opp_val = getattr(value, "medecin13", None)
                setattr(value, "medecin13", self)

    @property
    def rendez_Vous9(self):
        return self.__rendez_Vous9
    @rendez_Vous9.setter
    def rendez_Vous9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medecin__rendez_Vous9", None)
        self.__rendez_Vous9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medecin8"):
                opp_val = getattr(old_value, "medecin8", None)
                if opp_val == self:
                    setattr(old_value, "medecin8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medecin8"):
                opp_val = getattr(value, "medecin8", None)
                setattr(value, "medecin8", self)



class Examen:

    def __init__(self, numeroExamen: int, dateProvisoir: str, heure: str, motif: str, rendez_Vous7: "Rendez_Vous" = None):
        self.numeroExamen = numeroExamen
        self.dateProvisoir = dateProvisoir
        self.heure = heure
        self.motif = motif
        self.rendez_Vous7 = rendez_Vous7
        
        pass
    @property
    def heure(self):
        return self.__heure
    @heure.setter
    def heure(self, heure: str):
        self.__heure = heure

    @property
    def motif(self):
        return self.__motif
    @motif.setter
    def motif(self, motif: str):
        self.__motif = motif

    @property
    def dateProvisoir(self):
        return self.__dateProvisoir
    @dateProvisoir.setter
    def dateProvisoir(self, dateProvisoir: str):
        self.__dateProvisoir = dateProvisoir

    @property
    def numeroExamen(self):
        return self.__numeroExamen
    @numeroExamen.setter
    def numeroExamen(self, numeroExamen: int):
        self.__numeroExamen = numeroExamen

    @property
    def rendez_Vous7(self):
        return self.__rendez_Vous7
    @rendez_Vous7.setter
    def rendez_Vous7(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Examen__rendez_Vous7", None)
        self.__rendez_Vous7 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "examen6"):
                opp_val = getattr(old_value, "examen6", None)
                if opp_val == self:
                    setattr(old_value, "examen6", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "examen6"):
                opp_val = getattr(value, "examen6", None)
                setattr(value, "examen6", self)



class Consultion:

    def __init__(self, numeroConsultation: int, dateConsultation: str, heure: str, description: str, rendez_Vous5: "Rendez_Vous" = None):
        self.numeroConsultation = numeroConsultation
        self.dateConsultation = dateConsultation
        self.heure = heure
        self.description = description
        self.rendez_Vous5 = rendez_Vous5
        
        pass
    @property
    def description(self):
        return self.__description
    @description.setter
    def description(self, description: str):
        self.__description = description

    @property
    def dateConsultation(self):
        return self.__dateConsultation
    @dateConsultation.setter
    def dateConsultation(self, dateConsultation: str):
        self.__dateConsultation = dateConsultation

    @property
    def heure(self):
        return self.__heure
    @heure.setter
    def heure(self, heure: str):
        self.__heure = heure

    @property
    def numeroConsultation(self):
        return self.__numeroConsultation
    @numeroConsultation.setter
    def numeroConsultation(self, numeroConsultation: int):
        self.__numeroConsultation = numeroConsultation

    @property
    def rendez_Vous5(self):
        return self.__rendez_Vous5
    @rendez_Vous5.setter
    def rendez_Vous5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Consultion__rendez_Vous5", None)
        self.__rendez_Vous5 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "consultion4"):
                opp_val = getattr(old_value, "consultion4", None)
                if opp_val == self:
                    setattr(old_value, "consultion4", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "consultion4"):
                opp_val = getattr(value, "consultion4", None)
                setattr(value, "consultion4", self)



class Rendez_Vous:

    def __init__(self, numeroRdV: int, dateRDV: str, heure: str, lieuRDV: str, patient3: "Patient" = None, consultion4: "Consultion" = None, examen6: "Examen" = None, medecin8: "Medecin" = None):
        self.numeroRdV = numeroRdV
        self.dateRDV = dateRDV
        self.heure = heure
        self.lieuRDV = lieuRDV
        self.patient3 = patient3
        self.consultion4 = consultion4
        self.examen6 = examen6
        self.medecin8 = medecin8
        
        pass
    @property
    def heure(self):
        return self.__heure
    @heure.setter
    def heure(self, heure: str):
        self.__heure = heure

    @property
    def numeroRdV(self):
        return self.__numeroRdV
    @numeroRdV.setter
    def numeroRdV(self, numeroRdV: int):
        self.__numeroRdV = numeroRdV

    @property
    def lieuRDV(self):
        return self.__lieuRDV
    @lieuRDV.setter
    def lieuRDV(self, lieuRDV: str):
        self.__lieuRDV = lieuRDV

    @property
    def dateRDV(self):
        return self.__dateRDV
    @dateRDV.setter
    def dateRDV(self, dateRDV: str):
        self.__dateRDV = dateRDV

    @property
    def medecin8(self):
        return self.__medecin8
    @medecin8.setter
    def medecin8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rendez_Vous__medecin8", None)
        self.__medecin8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rendez_Vous9"):
                opp_val = getattr(old_value, "rendez_Vous9", None)
                if opp_val == self:
                    setattr(old_value, "rendez_Vous9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rendez_Vous9"):
                opp_val = getattr(value, "rendez_Vous9", None)
                setattr(value, "rendez_Vous9", self)

    @property
    def examen6(self):
        return self.__examen6
    @examen6.setter
    def examen6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rendez_Vous__examen6", None)
        self.__examen6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rendez_Vous7"):
                opp_val = getattr(old_value, "rendez_Vous7", None)
                if opp_val == self:
                    setattr(old_value, "rendez_Vous7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rendez_Vous7"):
                opp_val = getattr(value, "rendez_Vous7", None)
                setattr(value, "rendez_Vous7", self)

    @property
    def consultion4(self):
        return self.__consultion4
    @consultion4.setter
    def consultion4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rendez_Vous__consultion4", None)
        self.__consultion4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rendez_Vous5"):
                opp_val = getattr(old_value, "rendez_Vous5", None)
                if opp_val == self:
                    setattr(old_value, "rendez_Vous5", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rendez_Vous5"):
                opp_val = getattr(value, "rendez_Vous5", None)
                setattr(value, "rendez_Vous5", self)

    @property
    def patient3(self):
        return self.__patient3
    @patient3.setter
    def patient3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Rendez_Vous__patient3", None)
        self.__patient3 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "rendez_Vous2"):
                opp_val = getattr(old_value, "rendez_Vous2", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "rendez_Vous2"):
                opp_val = getattr(value, "rendez_Vous2", None)
                if opp_val is None:
                    setattr(value, "rendez_Vous2", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Patient:

    def __init__(self, numeroPatien: int, nomPatient: str, prenomPatien: str, agePatient: int, lieuResidence: str, profession: str, resultatExamen20: "ResultatExamen" = None, dossierPatient1: set["DossierPatient"] = None, rendez_Vous2: set["Rendez_Vous"] = None):
        self.numeroPatien = numeroPatien
        self.nomPatient = nomPatient
        self.prenomPatien = prenomPatien
        self.agePatient = agePatient
        self.lieuResidence = lieuResidence
        self.profession = profession
        self.resultatExamen20 = resultatExamen20
        self.dossierPatient1 = dossierPatient1 if dossierPatient1 is not None else set()
        self.rendez_Vous2 = rendez_Vous2 if rendez_Vous2 is not None else set()
        
        pass
    @property
    def nomPatient(self):
        return self.__nomPatient
    @nomPatient.setter
    def nomPatient(self, nomPatient: str):
        self.__nomPatient = nomPatient

    @property
    def prenomPatien(self):
        return self.__prenomPatien
    @prenomPatien.setter
    def prenomPatien(self, prenomPatien: str):
        self.__prenomPatien = prenomPatien

    @property
    def profession(self):
        return self.__profession
    @profession.setter
    def profession(self, profession: str):
        self.__profession = profession

    @property
    def agePatient(self):
        return self.__agePatient
    @agePatient.setter
    def agePatient(self, agePatient: int):
        self.__agePatient = agePatient

    @property
    def numeroPatien(self):
        return self.__numeroPatien
    @numeroPatien.setter
    def numeroPatien(self, numeroPatien: int):
        self.__numeroPatien = numeroPatien

    @property
    def lieuResidence(self):
        return self.__lieuResidence
    @lieuResidence.setter
    def lieuResidence(self, lieuResidence: str):
        self.__lieuResidence = lieuResidence

    @property
    def rendez_Vous2(self):
        return self.__rendez_Vous2
    @rendez_Vous2.setter
    def rendez_Vous2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__rendez_Vous2", None)
        self.__rendez_Vous2 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient3"):
                    opp_val = getattr(item, "patient3", None)
                    
                    if opp_val == self:
                        setattr(item, "patient3", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient3"):
                    opp_val = getattr(item, "patient3", None)
                    
                    setattr(item, "patient3", self)
                    

    @property
    def resultatExamen20(self):
        return self.__resultatExamen20
    @resultatExamen20.setter
    def resultatExamen20(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__resultatExamen20", None)
        self.__resultatExamen20 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "patient21"):
                opp_val = getattr(old_value, "patient21", None)
                if opp_val == self:
                    setattr(old_value, "patient21", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "patient21"):
                opp_val = getattr(value, "patient21", None)
                setattr(value, "patient21", self)

    @property
    def dossierPatient1(self):
        return self.__dossierPatient1
    @dossierPatient1.setter
    def dossierPatient1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Patient__dossierPatient1", None)
        self.__dossierPatient1 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "patient0"):
                    opp_val = getattr(item, "patient0", None)
                    
                    if opp_val == self:
                        setattr(item, "patient0", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "patient0"):
                    opp_val = getattr(item, "patient0", None)
                    
                    setattr(item, "patient0", self)
                    



class DossierPatient:

    def __init__(self, numeroPatient: int, nomDossier: str, dateCreation: int, heure: int, infoAntecedant: str, patient0: "Patient" = None):
        self.numeroPatient = numeroPatient
        self.nomDossier = nomDossier
        self.dateCreation = dateCreation
        self.heure = heure
        self.infoAntecedant = infoAntecedant
        self.patient0 = patient0
        
        pass
    @property
    def infoAntecedant(self):
        return self.__infoAntecedant
    @infoAntecedant.setter
    def infoAntecedant(self, infoAntecedant: str):
        self.__infoAntecedant = infoAntecedant

    @property
    def numeroPatient(self):
        return self.__numeroPatient
    @numeroPatient.setter
    def numeroPatient(self, numeroPatient: int):
        self.__numeroPatient = numeroPatient

    @property
    def heure(self):
        return self.__heure
    @heure.setter
    def heure(self, heure: int):
        self.__heure = heure

    @property
    def dateCreation(self):
        return self.__dateCreation
    @dateCreation.setter
    def dateCreation(self, dateCreation: int):
        self.__dateCreation = dateCreation

    @property
    def nomDossier(self):
        return self.__nomDossier
    @nomDossier.setter
    def nomDossier(self, nomDossier: str):
        self.__nomDossier = nomDossier

    @property
    def patient0(self):
        return self.__patient0
    @patient0.setter
    def patient0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_DossierPatient__patient0", None)
        self.__patient0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "dossierPatient1"):
                opp_val = getattr(old_value, "dossierPatient1", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "dossierPatient1"):
                opp_val = getattr(value, "dossierPatient1", None)
                if opp_val is None:
                    setattr(value, "dossierPatient1", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

