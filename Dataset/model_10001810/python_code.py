from __future__ import annotations
from datetime import datetime, date, time
############################################
# Definition of Classes
############################################










class Pizzeria:

    def __init__(self, id: int, adresse_id: int, nom: str, Pizzeria_Adresse_018: "Adresse" = None, Utilisateur_Pizzeria_117: "Utilisateur" = None):
        self.id = id
        self.adresse_id = adresse_id
        self.nom = nom
        self.Pizzeria_Adresse_018 = Pizzeria_Adresse_018
        self.Utilisateur_Pizzeria_117 = Utilisateur_Pizzeria_117
        
        pass
    @property
    def adresse_id(self):
        return self.__adresse_id
    @adresse_id.setter
    def adresse_id(self, adresse_id: int):
        self.__adresse_id = adresse_id

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

    @property
    def Utilisateur_Pizzeria_117(self):
        return self.__Utilisateur_Pizzeria_117
    @Utilisateur_Pizzeria_117.setter
    def Utilisateur_Pizzeria_117(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pizzeria__Utilisateur_Pizzeria_117", None)
        self.__Utilisateur_Pizzeria_117 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Utilisateur_Pizzeria_016"):
                opp_val = getattr(old_value, "Utilisateur_Pizzeria_016", None)
                if opp_val == self:
                    setattr(old_value, "Utilisateur_Pizzeria_016", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Utilisateur_Pizzeria_016"):
                opp_val = getattr(value, "Utilisateur_Pizzeria_016", None)
                setattr(value, "Utilisateur_Pizzeria_016", self)

    @property
    def Pizzeria_Adresse_018(self):
        return self.__Pizzeria_Adresse_018
    @Pizzeria_Adresse_018.setter
    def Pizzeria_Adresse_018(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Pizzeria__Pizzeria_Adresse_018", None)
        self.__Pizzeria_Adresse_018 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pizzeria_Adresse_119"):
                opp_val = getattr(old_value, "Pizzeria_Adresse_119", None)
                if opp_val == self:
                    setattr(old_value, "Pizzeria_Adresse_119", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pizzeria_Adresse_119"):
                opp_val = getattr(value, "Pizzeria_Adresse_119", None)
                setattr(value, "Pizzeria_Adresse_119", self)



class R_le:

    def __init__(self, id: int, type: str, Utilisateur_R_le_11: set["Utilisateur"] = None):
        self.id = id
        self.type = type
        self.Utilisateur_R_le_11 = Utilisateur_R_le_11 if Utilisateur_R_le_11 is not None else set()
        
        pass
    @property
    def type(self):
        return self.__type
    @type.setter
    def type(self, type: str):
        self.__type = type

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Utilisateur_R_le_11(self):
        return self.__Utilisateur_R_le_11
    @Utilisateur_R_le_11.setter
    def Utilisateur_R_le_11(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_R_le__Utilisateur_R_le_11", None)
        self.__Utilisateur_R_le_11 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Utilisateur_R_le_00"):
                    opp_val = getattr(item, "Utilisateur_R_le_00", None)
                    
                    if opp_val == self:
                        setattr(item, "Utilisateur_R_le_00", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Utilisateur_R_le_00"):
                    opp_val = getattr(item, "Utilisateur_R_le_00", None)
                    
                    setattr(item, "Utilisateur_R_le_00", self)
                    



class Produit:

    def __init__(self, id: int, nom: str, categorie_id: int, prix: str, Produit_Recette_02: "Recette" = None, Produit_Cat_gorie_04: "Cat_gorie" = None):
        self.id = id
        self.nom = nom
        self.categorie_id = categorie_id
        self.prix = prix
        self.Produit_Recette_02 = Produit_Recette_02
        self.Produit_Cat_gorie_04 = Produit_Cat_gorie_04
        
        pass
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

    @property
    def prix(self):
        return self.__prix
    @prix.setter
    def prix(self, prix: str):
        self.__prix = prix

    @property
    def categorie_id(self):
        return self.__categorie_id
    @categorie_id.setter
    def categorie_id(self, categorie_id: int):
        self.__categorie_id = categorie_id

    @property
    def Produit_Cat_gorie_04(self):
        return self.__Produit_Cat_gorie_04
    @Produit_Cat_gorie_04.setter
    def Produit_Cat_gorie_04(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Produit__Produit_Cat_gorie_04", None)
        self.__Produit_Cat_gorie_04 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Produit_Cat_gorie_15"):
                opp_val = getattr(old_value, "Produit_Cat_gorie_15", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Produit_Cat_gorie_15"):
                opp_val = getattr(value, "Produit_Cat_gorie_15", None)
                if opp_val is None:
                    setattr(value, "Produit_Cat_gorie_15", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Produit_Recette_02(self):
        return self.__Produit_Recette_02
    @Produit_Recette_02.setter
    def Produit_Recette_02(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Produit__Produit_Recette_02", None)
        self.__Produit_Recette_02 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Produit_Recette_13"):
                opp_val = getattr(old_value, "Produit_Recette_13", None)
                if opp_val == self:
                    setattr(old_value, "Produit_Recette_13", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Produit_Recette_13"):
                opp_val = getattr(value, "Produit_Recette_13", None)
                setattr(value, "Produit_Recette_13", self)



class Recette:

    def __init__(self, id: int, produit_id: int, Produit_Recette_13: "Produit" = None):
        self.id = id
        self.produit_id = produit_id
        self.Produit_Recette_13 = Produit_Recette_13
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def produit_id(self):
        return self.__produit_id
    @produit_id.setter
    def produit_id(self, produit_id: int):
        self.__produit_id = produit_id

    @property
    def Produit_Recette_13(self):
        return self.__Produit_Recette_13
    @Produit_Recette_13.setter
    def Produit_Recette_13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Recette__Produit_Recette_13", None)
        self.__Produit_Recette_13 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Produit_Recette_02"):
                opp_val = getattr(old_value, "Produit_Recette_02", None)
                if opp_val == self:
                    setattr(old_value, "Produit_Recette_02", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Produit_Recette_02"):
                opp_val = getattr(value, "Produit_Recette_02", None)
                setattr(value, "Produit_Recette_02", self)



class Cat_gorie:

    def __init__(self, id: int, nom: str, Produit_Cat_gorie_15: set["Produit"] = None):
        self.id = id
        self.nom = nom
        self.Produit_Cat_gorie_15 = Produit_Cat_gorie_15 if Produit_Cat_gorie_15 is not None else set()
        
        pass
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

    @property
    def Produit_Cat_gorie_15(self):
        return self.__Produit_Cat_gorie_15
    @Produit_Cat_gorie_15.setter
    def Produit_Cat_gorie_15(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Cat_gorie__Produit_Cat_gorie_15", None)
        self.__Produit_Cat_gorie_15 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Produit_Cat_gorie_04"):
                    opp_val = getattr(item, "Produit_Cat_gorie_04", None)
                    
                    if opp_val == self:
                        setattr(item, "Produit_Cat_gorie_04", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Produit_Cat_gorie_04"):
                    opp_val = getattr(item, "Produit_Cat_gorie_04", None)
                    
                    setattr(item, "Produit_Cat_gorie_04", self)
                    



class Ingr_dient:

    def __init__(self, id: int, nom: str, poids: str, unit_: str, Stock_Ingr_dient_19: "Stock" = None):
        self.id = id
        self.nom = nom
        self.poids = poids
        self.unit_ = unit_
        self.Stock_Ingr_dient_19 = Stock_Ingr_dient_19
        
        pass
    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def poids(self):
        return self.__poids
    @poids.setter
    def poids(self, poids: str):
        self.__poids = poids

    @property
    def unit_(self):
        return self.__unit_
    @unit_.setter
    def unit_(self, unit_: str):
        self.__unit_ = unit_

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Stock_Ingr_dient_19(self):
        return self.__Stock_Ingr_dient_19
    @Stock_Ingr_dient_19.setter
    def Stock_Ingr_dient_19(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Ingr_dient__Stock_Ingr_dient_19", None)
        self.__Stock_Ingr_dient_19 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Stock_Ingr_dient_08"):
                opp_val = getattr(old_value, "Stock_Ingr_dient_08", None)
                if opp_val == self:
                    setattr(old_value, "Stock_Ingr_dient_08", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Stock_Ingr_dient_08"):
                opp_val = getattr(value, "Stock_Ingr_dient_08", None)
                setattr(value, "Stock_Ingr_dient_08", self)



class Stock:

    def __init__(self, ingredient_id: int, quantit_: int, date_modification: int, disponibilit_: bool, Stock_Ingr_dient_08: "Ingr_dient" = None):
        self.ingredient_id = ingredient_id
        self.quantit_ = quantit_
        self.date_modification = date_modification
        self.disponibilit_ = disponibilit_
        self.Stock_Ingr_dient_08 = Stock_Ingr_dient_08
        
        pass
    @property
    def date_modification(self):
        return self.__date_modification
    @date_modification.setter
    def date_modification(self, date_modification: int):
        self.__date_modification = date_modification

    @property
    def ingredient_id(self):
        return self.__ingredient_id
    @ingredient_id.setter
    def ingredient_id(self, ingredient_id: int):
        self.__ingredient_id = ingredient_id

    @property
    def quantit_(self):
        return self.__quantit_
    @quantit_.setter
    def quantit_(self, quantit_: int):
        self.__quantit_ = quantit_

    @property
    def disponibilit_(self):
        return self.__disponibilit_
    @disponibilit_.setter
    def disponibilit_(self, disponibilit_: bool):
        self.__disponibilit_ = disponibilit_

    @property
    def Stock_Ingr_dient_08(self):
        return self.__Stock_Ingr_dient_08
    @Stock_Ingr_dient_08.setter
    def Stock_Ingr_dient_08(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Stock__Stock_Ingr_dient_08", None)
        self.__Stock_Ingr_dient_08 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Stock_Ingr_dient_19"):
                opp_val = getattr(old_value, "Stock_Ingr_dient_19", None)
                if opp_val == self:
                    setattr(old_value, "Stock_Ingr_dient_19", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Stock_Ingr_dient_19"):
                opp_val = getattr(value, "Stock_Ingr_dient_19", None)
                setattr(value, "Stock_Ingr_dient_19", self)



class Livraison:

    def __init__(self, id: int, commande_id: int, livreur_id: int, client_id: int, geocode: str, Livraison_Utilisateur2_020: "Utilisateur" = None, Livraison_Utilisateur_012: "Utilisateur" = None, Livraison_Commande_014: "Commande" = None):
        self.id = id
        self.commande_id = commande_id
        self.livreur_id = livreur_id
        self.client_id = client_id
        self.geocode = geocode
        self.Livraison_Utilisateur2_020 = Livraison_Utilisateur2_020
        self.Livraison_Utilisateur_012 = Livraison_Utilisateur_012
        self.Livraison_Commande_014 = Livraison_Commande_014
        
        pass
    @property
    def geocode(self):
        return self.__geocode
    @geocode.setter
    def geocode(self, geocode: str):
        self.__geocode = geocode

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def commande_id(self):
        return self.__commande_id
    @commande_id.setter
    def commande_id(self, commande_id: int):
        self.__commande_id = commande_id

    @property
    def livreur_id(self):
        return self.__livreur_id
    @livreur_id.setter
    def livreur_id(self, livreur_id: int):
        self.__livreur_id = livreur_id

    @property
    def client_id(self):
        return self.__client_id
    @client_id.setter
    def client_id(self, client_id: int):
        self.__client_id = client_id

    @property
    def Livraison_Utilisateur_012(self):
        return self.__Livraison_Utilisateur_012
    @Livraison_Utilisateur_012.setter
    def Livraison_Utilisateur_012(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Livraison__Livraison_Utilisateur_012", None)
        self.__Livraison_Utilisateur_012 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "livreur13"):
                opp_val = getattr(old_value, "livreur13", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "livreur13"):
                opp_val = getattr(value, "livreur13", None)
                if opp_val is None:
                    setattr(value, "livreur13", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Livraison_Utilisateur2_020(self):
        return self.__Livraison_Utilisateur2_020
    @Livraison_Utilisateur2_020.setter
    def Livraison_Utilisateur2_020(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Livraison__Livraison_Utilisateur2_020", None)
        self.__Livraison_Utilisateur2_020 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "client21"):
                opp_val = getattr(old_value, "client21", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "client21"):
                opp_val = getattr(value, "client21", None)
                if opp_val is None:
                    setattr(value, "client21", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Livraison_Commande_014(self):
        return self.__Livraison_Commande_014
    @Livraison_Commande_014.setter
    def Livraison_Commande_014(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Livraison__Livraison_Commande_014", None)
        self.__Livraison_Commande_014 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Livraison_Commande_115"):
                opp_val = getattr(old_value, "Livraison_Commande_115", None)
                if opp_val == self:
                    setattr(old_value, "Livraison_Commande_115", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Livraison_Commande_115"):
                opp_val = getattr(value, "Livraison_Commande_115", None)
                setattr(value, "Livraison_Commande_115", self)



class Adresse:

    def __init__(self, id: int, utilisateur_id: int, voie: str, num_ro: int, ville: str, code_postal: int, t_l_phone: str, geocode: str, Pizzeria_Adresse_119: "Pizzeria" = None):
        self.id = id
        self.utilisateur_id = utilisateur_id
        self.voie = voie
        self.num_ro = num_ro
        self.ville = ville
        self.code_postal = code_postal
        self.t_l_phone = t_l_phone
        self.geocode = geocode
        self.Pizzeria_Adresse_119 = Pizzeria_Adresse_119
        
        pass
    @property
    def num_ro(self):
        return self.__num_ro
    @num_ro.setter
    def num_ro(self, num_ro: int):
        self.__num_ro = num_ro

    @property
    def geocode(self):
        return self.__geocode
    @geocode.setter
    def geocode(self, geocode: str):
        self.__geocode = geocode

    @property
    def t_l_phone(self):
        return self.__t_l_phone
    @t_l_phone.setter
    def t_l_phone(self, t_l_phone: str):
        self.__t_l_phone = t_l_phone

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def utilisateur_id(self):
        return self.__utilisateur_id
    @utilisateur_id.setter
    def utilisateur_id(self, utilisateur_id: int):
        self.__utilisateur_id = utilisateur_id

    @property
    def ville(self):
        return self.__ville
    @ville.setter
    def ville(self, ville: str):
        self.__ville = ville

    @property
    def voie(self):
        return self.__voie
    @voie.setter
    def voie(self, voie: str):
        self.__voie = voie

    @property
    def code_postal(self):
        return self.__code_postal
    @code_postal.setter
    def code_postal(self, code_postal: int):
        self.__code_postal = code_postal

    @property
    def Pizzeria_Adresse_119(self):
        return self.__Pizzeria_Adresse_119
    @Pizzeria_Adresse_119.setter
    def Pizzeria_Adresse_119(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Adresse__Pizzeria_Adresse_119", None)
        self.__Pizzeria_Adresse_119 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Pizzeria_Adresse_018"):
                opp_val = getattr(old_value, "Pizzeria_Adresse_018", None)
                if opp_val == self:
                    setattr(old_value, "Pizzeria_Adresse_018", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Pizzeria_Adresse_018"):
                opp_val = getattr(value, "Pizzeria_Adresse_018", None)
                setattr(value, "Pizzeria_Adresse_018", self)



class Etat:

    def __init__(self, id: int, nom: str, verrouillage: bool, Etat_Commande_010: "Commande" = None):
        self.id = id
        self.nom = nom
        self.verrouillage = verrouillage
        self.Etat_Commande_010 = Etat_Commande_010
        
        pass
    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def verrouillage(self):
        return self.__verrouillage
    @verrouillage.setter
    def verrouillage(self, verrouillage: bool):
        self.__verrouillage = verrouillage

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def Etat_Commande_010(self):
        return self.__Etat_Commande_010
    @Etat_Commande_010.setter
    def Etat_Commande_010(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Etat__Etat_Commande_010", None)
        self.__Etat_Commande_010 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etat_Commande_111"):
                opp_val = getattr(old_value, "Etat_Commande_111", None)
                if opp_val == self:
                    setattr(old_value, "Etat_Commande_111", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etat_Commande_111"):
                opp_val = getattr(value, "Etat_Commande_111", None)
                setattr(value, "Etat_Commande_111", self)



class Commande:

    def __init__(self, id: int, utilisateur_id: int, date: int, paiement: str, _tat: int, Commande_Utilisateur_06: "Utilisateur" = None, Etat_Commande_111: "Etat" = None, Livraison_Commande_115: "Livraison" = None):
        self.id = id
        self.utilisateur_id = utilisateur_id
        self.date = date
        self.paiement = paiement
        self._tat = _tat
        self.Commande_Utilisateur_06 = Commande_Utilisateur_06
        self.Etat_Commande_111 = Etat_Commande_111
        self.Livraison_Commande_115 = Livraison_Commande_115
        
        pass
    @property
    def utilisateur_id(self):
        return self.__utilisateur_id
    @utilisateur_id.setter
    def utilisateur_id(self, utilisateur_id: int):
        self.__utilisateur_id = utilisateur_id

    @property
    def date(self):
        return self.__date
    @date.setter
    def date(self, date: int):
        self.__date = date

    @property
    def _tat(self):
        return self.___tat
    @_tat.setter
    def _tat(self, _tat: int):
        self.___tat = _tat

    @property
    def paiement(self):
        return self.__paiement
    @paiement.setter
    def paiement(self, paiement: str):
        self.__paiement = paiement

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def Commande_Utilisateur_06(self):
        return self.__Commande_Utilisateur_06
    @Commande_Utilisateur_06.setter
    def Commande_Utilisateur_06(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Commande__Commande_Utilisateur_06", None)
        self.__Commande_Utilisateur_06 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Commande_Utilisateur_17"):
                opp_val = getattr(old_value, "Commande_Utilisateur_17", None)
                if opp_val == self:
                    setattr(old_value, "Commande_Utilisateur_17", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Commande_Utilisateur_17"):
                opp_val = getattr(value, "Commande_Utilisateur_17", None)
                setattr(value, "Commande_Utilisateur_17", self)

    @property
    def Livraison_Commande_115(self):
        return self.__Livraison_Commande_115
    @Livraison_Commande_115.setter
    def Livraison_Commande_115(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Commande__Livraison_Commande_115", None)
        self.__Livraison_Commande_115 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Livraison_Commande_014"):
                opp_val = getattr(old_value, "Livraison_Commande_014", None)
                if opp_val == self:
                    setattr(old_value, "Livraison_Commande_014", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Livraison_Commande_014"):
                opp_val = getattr(value, "Livraison_Commande_014", None)
                setattr(value, "Livraison_Commande_014", self)

    @property
    def Etat_Commande_111(self):
        return self.__Etat_Commande_111
    @Etat_Commande_111.setter
    def Etat_Commande_111(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Commande__Etat_Commande_111", None)
        self.__Etat_Commande_111 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Etat_Commande_010"):
                opp_val = getattr(old_value, "Etat_Commande_010", None)
                if opp_val == self:
                    setattr(old_value, "Etat_Commande_010", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Etat_Commande_010"):
                opp_val = getattr(value, "Etat_Commande_010", None)
                setattr(value, "Etat_Commande_010", self)



class Class:

    pass


class Utilisateur:

    def __init__(self, id: int, nom: str, prenom: str, civilit_: str, date_naissance: str, email: str, mot_de_passe: str, role_id: int, pizzeria_id: int, Utilisateur_R_le_00: "R_le" = None, Commande_Utilisateur_17: "Commande" = None, client21: set["Livraison"] = None, livreur13: set["Livraison"] = None, Utilisateur_Pizzeria_016: "Pizzeria" = None):
        self.id = id
        self.nom = nom
        self.prenom = prenom
        self.civilit_ = civilit_
        self.date_naissance = date_naissance
        self.email = email
        self.mot_de_passe = mot_de_passe
        self.role_id = role_id
        self.pizzeria_id = pizzeria_id
        self.Utilisateur_R_le_00 = Utilisateur_R_le_00
        self.Commande_Utilisateur_17 = Commande_Utilisateur_17
        self.client21 = client21 if client21 is not None else set()
        self.livreur13 = livreur13 if livreur13 is not None else set()
        self.Utilisateur_Pizzeria_016 = Utilisateur_Pizzeria_016
        
        pass
    @property
    def pizzeria_id(self):
        return self.__pizzeria_id
    @pizzeria_id.setter
    def pizzeria_id(self, pizzeria_id: int):
        self.__pizzeria_id = pizzeria_id

    @property
    def id(self):
        return self.__id
    @id.setter
    def id(self, id: int):
        self.__id = id

    @property
    def role_id(self):
        return self.__role_id
    @role_id.setter
    def role_id(self, role_id: int):
        self.__role_id = role_id

    @property
    def nom(self):
        return self.__nom
    @nom.setter
    def nom(self, nom: str):
        self.__nom = nom

    @property
    def civilit_(self):
        return self.__civilit_
    @civilit_.setter
    def civilit_(self, civilit_: str):
        self.__civilit_ = civilit_

    @property
    def date_naissance(self):
        return self.__date_naissance
    @date_naissance.setter
    def date_naissance(self, date_naissance: str):
        self.__date_naissance = date_naissance

    @property
    def email(self):
        return self.__email
    @email.setter
    def email(self, email: str):
        self.__email = email

    @property
    def mot_de_passe(self):
        return self.__mot_de_passe
    @mot_de_passe.setter
    def mot_de_passe(self, mot_de_passe: str):
        self.__mot_de_passe = mot_de_passe

    @property
    def prenom(self):
        return self.__prenom
    @prenom.setter
    def prenom(self, prenom: str):
        self.__prenom = prenom

    @property
    def Utilisateur_R_le_00(self):
        return self.__Utilisateur_R_le_00
    @Utilisateur_R_le_00.setter
    def Utilisateur_R_le_00(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur__Utilisateur_R_le_00", None)
        self.__Utilisateur_R_le_00 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Utilisateur_R_le_11"):
                opp_val = getattr(old_value, "Utilisateur_R_le_11", None)
                if isinstance(opp_val, set):
                    opp_val.discard(self)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Utilisateur_R_le_11"):
                opp_val = getattr(value, "Utilisateur_R_le_11", None)
                if opp_val is None:
                    setattr(value, "Utilisateur_R_le_11", set([self]))
                elif isinstance(opp_val, set):
                    opp_val.add(self)

    @property
    def Commande_Utilisateur_17(self):
        return self.__Commande_Utilisateur_17
    @Commande_Utilisateur_17.setter
    def Commande_Utilisateur_17(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur__Commande_Utilisateur_17", None)
        self.__Commande_Utilisateur_17 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Commande_Utilisateur_06"):
                opp_val = getattr(old_value, "Commande_Utilisateur_06", None)
                if opp_val == self:
                    setattr(old_value, "Commande_Utilisateur_06", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Commande_Utilisateur_06"):
                opp_val = getattr(value, "Commande_Utilisateur_06", None)
                setattr(value, "Commande_Utilisateur_06", self)

    @property
    def client21(self):
        return self.__client21
    @client21.setter
    def client21(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur__client21", None)
        self.__client21 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Livraison_Utilisateur2_020"):
                    opp_val = getattr(item, "Livraison_Utilisateur2_020", None)
                    
                    if opp_val == self:
                        setattr(item, "Livraison_Utilisateur2_020", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Livraison_Utilisateur2_020"):
                    opp_val = getattr(item, "Livraison_Utilisateur2_020", None)
                    
                    setattr(item, "Livraison_Utilisateur2_020", self)
                    

    @property
    def livreur13(self):
        return self.__livreur13
    @livreur13.setter
    def livreur13(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur__livreur13", None)
        self.__livreur13 = value if value is not None else set()
        
        # Remove self from old opposite end
        if old_value is not None:
            for item in old_value:
                if hasattr(item, "Livraison_Utilisateur_012"):
                    opp_val = getattr(item, "Livraison_Utilisateur_012", None)
                    
                    if opp_val == self:
                        setattr(item, "Livraison_Utilisateur_012", None)
                    
        # Add self to new opposite end
        if value is not None:
            for item in value:
                if hasattr(item, "Livraison_Utilisateur_012"):
                    opp_val = getattr(item, "Livraison_Utilisateur_012", None)
                    
                    setattr(item, "Livraison_Utilisateur_012", self)
                    

    @property
    def Utilisateur_Pizzeria_016(self):
        return self.__Utilisateur_Pizzeria_016
    @Utilisateur_Pizzeria_016.setter
    def Utilisateur_Pizzeria_016(self, value):
        # Bidirectional consistency
        old_value = getattr(self, f"_Utilisateur__Utilisateur_Pizzeria_016", None)
        self.__Utilisateur_Pizzeria_016 = value
        
        # Remove self from old opposite end
        if old_value is not None:
            if hasattr(old_value, "Utilisateur_Pizzeria_117"):
                opp_val = getattr(old_value, "Utilisateur_Pizzeria_117", None)
                if opp_val == self:
                    setattr(old_value, "Utilisateur_Pizzeria_117", None)
                
        # Add self to new opposite end
        if value is not None:
            if hasattr(value, "Utilisateur_Pizzeria_117"):
                opp_val = getattr(value, "Utilisateur_Pizzeria_117", None)
                setattr(value, "Utilisateur_Pizzeria_117", self)

