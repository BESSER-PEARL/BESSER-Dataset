from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Rendez_vous_Medecin_Patient_external:

    pass


class Rendez_vous_Laboratoire_Patient_external:

    pass


class Produit:

    def __init__(self, id: int, nom: str, dose: str, posologie: str, ordonance14: "Ordonance" = None):
        self.id = id
        self.nom = nom
        self.dose = dose
        self.posologie = posologie
        self.ordonance14 = ordonance14
        
        pass
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def posologie(self):
        return self.__posologie
    @posologie.setter
    def posologie(self, posologie: str):
        self.__posologie = posologie

    @property
    def dose(self):
        return self.__dose
    @dose.setter
    def dose(self, dose: str):
        self.__dose = dose

    @property
    def ordonance14(self):
        return self.__ordonance14
    @ordonance14.setter
    def ordonance14(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Produit__ordonance14", None)
        self.__ordonance14 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "produit15"):
                opp_val = getattr(old_value, "produit15", None)
                if opp_val == self:
                    setattr(old_value, "produit15", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "produit15"):
                opp_val = getattr(value, "produit15", None)
                setattr(value, "produit15", self)



class Ordonance:

    def __init__(self, id: int, date: str, rendez_vous_Medecin_Patient10: "Rendez_vous_Medecin_Patient_external" = None, produit15: "Produit" = None):
        self.id = id
        self.date = date
        self.rendez_vous_Medecin_Patient10 = rendez_vous_Medecin_Patient10
        self.produit15 = produit15
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def produit15(self):
        return self.__produit15
    @produit15.setter
    def produit15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordonance__produit15", None)
        self.__produit15 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordonance14"):
                opp_val = getattr(old_value, "ordonance14", None)
                if opp_val == self:
                    setattr(old_value, "ordonance14", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordonance14"):
                opp_val = getattr(value, "ordonance14", None)
                setattr(value, "ordonance14", self)

    @property
    def rendez_vous_Medecin_Patient10(self):
        return self.__rendez_vous_Medecin_Patient10
    @rendez_vous_Medecin_Patient10.setter
    def rendez_vous_Medecin_Patient10(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ordonance__rendez_vous_Medecin_Patient10", None)
        self.__rendez_vous_Medecin_Patient10 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "ordonance11"):
                opp_val = getattr(old_value, "ordonance11", None)
                if opp_val == self:
                    setattr(old_value, "ordonance11", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "ordonance11"):
                opp_val = getattr(value, "ordonance11", None)
                setattr(value, "ordonance11", self)



class Rendez_vous:

    def __init__(self, numero: str, date: str, id: int):
        self.numero = numero
        self.date = date
        self.id = id
        
        pass
    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: str):
        self.__date = date

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero



class Contact:

    def __init__(self, id: int, telephone: int, mail: str, personne4: "Personne" = None):
        self.id = id
        self.telephone = telephone
        self.mail = mail
        self.personne4 = personne4
        
        pass
    @property
    def mail(self):
        return self.__mail
    @mail.setter
    def mail(self, mail: str):
        self.__mail = mail

    @property
    def telephone(self):
        return self.__telephone
    @telephone.setter
    def telephone(self, telephone: int):
        self.__telephone = telephone

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def personne4(self):
        return self.__personne4
    @personne4.setter
    def personne4(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Contact__personne4", None)
        self.__personne4 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "contact5"):
                opp_val = getattr(old_value, "contact5", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "contact5"):
                opp_val = getattr(value, "contact5", None)
                if opp_val is None:
                    setattr(value, "contact5", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)



class Personne:

    def __init__(self, id: int, numero: str, nom: str, prenom: str, attribute: str, numeroMedecin: int, contact5: set["Contact"] = None):
        self.id = id
        self.numero = numero
        self.nom = nom
        self.prenom = prenom
        self.attribute = attribute
        self.numeroMedecin = numeroMedecin
        self.contact5 = contact5 if contact5 is not None else set()
        
        pass
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def numeroMedecin(self):
        return self.__numeroMedecin
    @numeroMedecin.setter
    def numeroMedecin(self, numeroMedecin: int):
        self.__numeroMedecin = numeroMedecin

    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @property
    def attribute(self):
        return self.__attribute
    @attribute.setter
    def attribute(self, attribute: str):
        self.__attribute = attribute

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def contact5(self):
        return self.__contact5
    @contact5.setter
    def contact5(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Personne__contact5", None)
        self.__contact5 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "personne4"):
                    opp_val = getattr(item, "personne4", None)
                    
                    if opp_val == self:
                        setattr(item, "personne4", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "personne4"):
                    opp_val = getattr(item, "personne4", None)
                    
                    setattr(item, "personne4", self)
                    



class Laboratoire:

    def __init__(self, id: int, numero: str, nom: str):
        self.id = id
        self.numero = numero
        self.nom = nom
        
        pass
    @property
    def numero(self):
        return self.__numero
    @numero.setter
    def numero(self, numero: str):
        self.__numero = numero

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom



class ResultatExamen:

    def __init__(self, numeroResultat: int, infoResultat: str, examen8: "Examen" = None):
        self.numeroResultat = numeroResultat
        self.infoResultat = infoResultat
        self.examen8 = examen8
        
        pass
    @property
    def infoResultat(self):
        return self.__infoResultat
    @infoResultat.setter
    def infoResultat(self, infoResultat: str):
        self.__infoResultat = infoResultat

    @property
    def numeroResultat(self):
        return self.__numeroResultat
    @numeroResultat.setter
    def numeroResultat(self, numeroResultat: int):
        self.__numeroResultat = numeroResultat

    @property
    def examen8(self):
        return self.__examen8
    @examen8.setter
    def examen8(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_ResultatExamen__examen8", None)
        self.__examen8 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "resultatExamen9"):
                opp_val = getattr(old_value, "resultatExamen9", None)
                if opp_val == self:
                    setattr(old_value, "resultatExamen9", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "resultatExamen9"):
                opp_val = getattr(value, "resultatExamen9", None)
                setattr(value, "resultatExamen9", self)



class CentreHospitalier:

    def __init__(self, numeroCentre: int, nomCentre: str, descriptionCentre: str, service3: set["Service"] = None):
        self.numeroCentre = numeroCentre
        self.nomCentre = nomCentre
        self.descriptionCentre = descriptionCentre
        self.service3 = service3 if service3 is not None else set()
        
        pass
    @property
    def nomCentre(self):
        return self.__nomCentre
    @nomCentre.setter
    def nomCentre(self, nomCentre: str):
        self.__nomCentre = nomCentre

    @property
    def numeroCentre(self):
        return self.__numeroCentre
    @numeroCentre.setter
    def numeroCentre(self, numeroCentre: int):
        self.__numeroCentre = numeroCentre

    @property
    def descriptionCentre(self):
        return self.__descriptionCentre
    @descriptionCentre.setter
    def descriptionCentre(self, descriptionCentre: str):
        self.__descriptionCentre = descriptionCentre

    @property
    def service3(self):
        return self.__service3
    @service3.setter
    def service3(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_CentreHospitalier__service3", None)
        self.__service3 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "centreHospitalier2"):
                    opp_val = getattr(item, "centreHospitalier2", None)
                    
                    if opp_val == self:
                        setattr(item, "centreHospitalier2", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "centreHospitalier2"):
                    opp_val = getattr(item, "centreHospitalier2", None)
                    
                    setattr(item, "centreHospitalier2", self)
                    



class Programme:

    def __init__(self, numeroProgramme: str, date: str, heure: str, examen13: "Examen" = None):
        self.numeroProgramme = numeroProgramme
        self.date = date
        self.heure = heure
        self.examen13 = examen13
        
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
    def examen13(self):
        return self.__examen13
    @examen13.setter
    def examen13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Programme__examen13", None)
        self.__examen13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "programme12"):
                opp_val = getattr(old_value, "programme12", None)
                if opp_val == self:
                    setattr(old_value, "programme12", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "programme12"):
                opp_val = getattr(value, "programme12", None)
                setattr(value, "programme12", self)



class Service:

    def __init__(self, numeroService: int, nomService: str, descriptionService: str, medecin1: "Medecin" = None, centreHospitalier2: "CentreHospitalier" = None):
        self.numeroService = numeroService
        self.nomService = nomService
        self.descriptionService = descriptionService
        self.medecin1 = medecin1
        self.centreHospitalier2 = centreHospitalier2
        
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
    def centreHospitalier2(self):
        return self.__centreHospitalier2
    @centreHospitalier2.setter
    def centreHospitalier2(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__centreHospitalier2", None)
        self.__centreHospitalier2 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service3"):
                opp_val = getattr(old_value, "service3", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service3"):
                opp_val = getattr(value, "service3", None)
                if opp_val is None:
                    setattr(value, "service3", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def medecin1(self):
        return self.__medecin1
    @medecin1.setter
    def medecin1(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Service__medecin1", None)
        self.__medecin1 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "service0"):
                opp_val = getattr(old_value, "service0", None)
                if opp_val == self:
                    setattr(old_value, "service0", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "service0"):
                opp_val = getattr(value, "service0", None)
                setattr(value, "service0", self)



class Medecin:

    def __init__(self, nomMedecin: str, prenomMedecin: str, dateNaissance: str, specialite: str, service0: "Service" = None):
        self.nomMedecin = nomMedecin
        self.prenomMedecin = prenomMedecin
        self.dateNaissance = dateNaissance
        self.specialite = specialite
        self.service0 = service0
        
        pass
    @property
    def prenomMedecin(self):
        return self.__prenomMedecin
    @prenomMedecin.setter
    def prenomMedecin(self, prenomMedecin: str):
        self.__prenomMedecin = prenomMedecin

    @property
    def nomMedecin(self):
        return self.__nomMedecin
    @nomMedecin.setter
    def nomMedecin(self, nomMedecin: str):
        self.__nomMedecin = nomMedecin

    @property
    def specialite(self):
        return self.__specialite
    @specialite.setter
    def specialite(self, specialite: str):
        self.__specialite = specialite

    @property
    def dateNaissance(self):
        return self.__dateNaissance
    @dateNaissance.setter
    def dateNaissance(self, dateNaissance: str):
        self.__dateNaissance = dateNaissance

    @property
    def service0(self):
        return self.__service0
    @service0.setter
    def service0(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Medecin__service0", None)
        self.__service0 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "medecin1"):
                opp_val = getattr(old_value, "medecin1", None)
                if opp_val == self:
                    setattr(old_value, "medecin1", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "medecin1"):
                opp_val = getattr(value, "medecin1", None)
                setattr(value, "medecin1", self)



class Examen:

    def __init__(self, numeroExamen: int, dateProvisoir: str, heure: str, motif: str, rendez_vous_Laboratoire_Patient6: "Rendez_vous_Laboratoire_Patient_external" = None, resultatExamen9: "ResultatExamen" = None, programme12: "Programme" = None):
        self.numeroExamen = numeroExamen
        self.dateProvisoir = dateProvisoir
        self.heure = heure
        self.motif = motif
        self.rendez_vous_Laboratoire_Patient6 = rendez_vous_Laboratoire_Patient6
        self.resultatExamen9 = resultatExamen9
        self.programme12 = programme12
        
        pass
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
    def motif(self):
        return self.__motif
    @motif.setter
    def motif(self, motif: str):
        self.__motif = motif

    @property
    def heure(self):
        return self.__heure
    @heure.setter
    def heure(self, heure: str):
        self.__heure = heure

    @property
    def resultatExamen9(self):
        return self.__resultatExamen9
    @resultatExamen9.setter
    def resultatExamen9(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Examen__resultatExamen9", None)
        self.__resultatExamen9 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "examen8"):
                opp_val = getattr(old_value, "examen8", None)
                if opp_val == self:
                    setattr(old_value, "examen8", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "examen8"):
                opp_val = getattr(value, "examen8", None)
                setattr(value, "examen8", self)

    @property
    def rendez_vous_Laboratoire_Patient6(self):
        return self.__rendez_vous_Laboratoire_Patient6
    @rendez_vous_Laboratoire_Patient6.setter
    def rendez_vous_Laboratoire_Patient6(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Examen__rendez_vous_Laboratoire_Patient6", None)
        self.__rendez_vous_Laboratoire_Patient6 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "examen7"):
                opp_val = getattr(old_value, "examen7", None)
                if opp_val == self:
                    setattr(old_value, "examen7", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "examen7"):
                opp_val = getattr(value, "examen7", None)
                setattr(value, "examen7", self)

    @property
    def programme12(self):
        return self.__programme12
    @programme12.setter
    def programme12(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Examen__programme12", None)
        self.__programme12 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "examen13"):
                opp_val = getattr(old_value, "examen13", None)
                if opp_val == self:
                    setattr(old_value, "examen13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "examen13"):
                opp_val = getattr(value, "examen13", None)
                setattr(value, "examen13", self)



class Patient:

    def __init__(self, numeroPatien: int, nomPatient: str, prenomPatien: str, agePatient: int, lieuResidence: str, profession: str):
        self.numeroPatien = numeroPatien
        self.nomPatient = nomPatient
        self.prenomPatien = prenomPatien
        self.agePatient = agePatient
        self.lieuResidence = lieuResidence
        self.profession = profession
        
        pass
    @property
    def nomPatient(self):
        return self.__nomPatient
    @nomPatient.setter
    def nomPatient(self, nomPatient: str):
        self.__nomPatient = nomPatient

    @property
    def agePatient(self):
        return self.__agePatient
    @agePatient.setter
    def agePatient(self, agePatient: int):
        self.__agePatient = agePatient

    @property
    def lieuResidence(self):
        return self.__lieuResidence
    @lieuResidence.setter
    def lieuResidence(self, lieuResidence: str):
        self.__lieuResidence = lieuResidence

    @property
    def profession(self):
        return self.__profession
    @profession.setter
    def profession(self, profession: str):
        self.__profession = profession

    @property
    def numeroPatien(self):
        return self.__numeroPatien
    @numeroPatien.setter
    def numeroPatien(self, numeroPatien: int):
        self.__numeroPatien = numeroPatien

    @property
    def prenomPatien(self):
        return self.__prenomPatien
    @prenomPatien.setter
    def prenomPatien(self, prenomPatien: str):
        self.__prenomPatien = prenomPatien

