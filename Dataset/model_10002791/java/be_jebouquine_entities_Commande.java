




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Commande  {

    private int idcommande;
    private int idEtat;
    private int idLivraisonInfo;
    private LocalDate dateCommande;
    private int idClient;





    private be_jebouquine_entities_Client be_jebouquine_entities_client;




    private be_jebouquine_entities_LivraisonType be_jebouquine_entities_livraisontype;




    private List<be_jebouquine_entities_LigneCommande> be_jebouquine_entities_lignecommandes;


    public be_jebouquine_entities_Commande(
        int idcommande,        int idEtat,        int idLivraisonInfo,        LocalDate dateCommande,        int idClient    ) {
        this.idcommande = idcommande;
        this.idEtat = idEtat;
        this.idLivraisonInfo = idLivraisonInfo;
        this.dateCommande = dateCommande;
        this.idClient = idClient;
        this.be_jebouquine_entities_lignecommandes = new ArrayList<>();
    }

    public be_jebouquine_entities_Commande(
        int idcommande,        int idEtat,        int idLivraisonInfo,        LocalDate dateCommande,        int idClient        ArrayList<be_jebouquine_entities_LigneCommande> be_jebouquine_entities_lignecommandes    ) {
        this.idcommande = idcommande;
        this.idEtat = idEtat;
        this.idLivraisonInfo = idLivraisonInfo;
        this.dateCommande = dateCommande;
        this.idClient = idClient;
        this.be_jebouquine_entities_lignecommandes = be_jebouquine_entities_lignecommandes;
    }

    public int getIdcommande() {
        return idcommande;
    }

    public void setIdcommande(int idcommande) {
        this.idcommande = idcommande;
    }
    public int getIdetat() {
        return idEtat;
    }

    public void setIdetat(int idEtat) {
        this.idEtat = idEtat;
    }
    public int getIdlivraisoninfo() {
        return idLivraisonInfo;
    }

    public void setIdlivraisoninfo(int idLivraisonInfo) {
        this.idLivraisonInfo = idLivraisonInfo;
    }
    public LocalDate getDatecommande() {
        return dateCommande;
    }

    public void setDatecommande(LocalDate dateCommande) {
        this.dateCommande = dateCommande;
    }
    public int getIdclient() {
        return idClient;
    }

    public void setIdclient(int idClient) {
        this.idClient = idClient;
    }

    public be_jebouquine_entities_Client getBe_jebouquine_entities_client() {
        return be_jebouquine_entities_client;
    }

    public void setBe_jebouquine_entities_client(be_jebouquine_entities_Client be_jebouquine_entities_client) {
        this.be_jebouquine_entities_client = be_jebouquine_entities_client;
    }
    public be_jebouquine_entities_LivraisonType getBe_jebouquine_entities_livraisontype() {
        return be_jebouquine_entities_livraisontype;
    }

    public void setBe_jebouquine_entities_livraisontype(be_jebouquine_entities_LivraisonType be_jebouquine_entities_livraisontype) {
        this.be_jebouquine_entities_livraisontype = be_jebouquine_entities_livraisontype;
    }
    public List<be_jebouquine_entities_LigneCommande> getBe_jebouquine_entities_lignecommandes() {
        return be_jebouquine_entities_lignecommandes;
    }

    public void addBe_jebouquine_entities_lignecommande(Be_jebouquine_entities_lignecommande be_jebouquine_entities_lignecommande) {
        this.be_jebouquine_entities_lignecommandes.add(be_jebouquine_entities_lignecommande);
    }

}