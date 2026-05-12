




import java.time.LocalDate;

import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Commande  {

    private int idClient;
    private int idEtat;
    private int idLivraisonInfo;
    private LocalDate dateCommande;
    private int idcommande;





    private be_jebouquine_entities_Client be_jebouquine_entities_client;


    public be_jebouquine_entities_Commande(
        int idClient,        int idEtat,        int idLivraisonInfo,        LocalDate dateCommande,        int idcommande    ) {
        this.idClient = idClient;
        this.idEtat = idEtat;
        this.idLivraisonInfo = idLivraisonInfo;
        this.dateCommande = dateCommande;
        this.idcommande = idcommande;
    }


    public int getIdclient() {
        return idClient;
    }

    public void setIdclient(int idClient) {
        this.idClient = idClient;
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
    public int getIdcommande() {
        return idcommande;
    }

    public void setIdcommande(int idcommande) {
        this.idcommande = idcommande;
    }

    public be_jebouquine_entities_Client getBe_jebouquine_entities_client() {
        return be_jebouquine_entities_client;
    }

    public void setBe_jebouquine_entities_client(be_jebouquine_entities_Client be_jebouquine_entities_client) {
        this.be_jebouquine_entities_client = be_jebouquine_entities_client;
    }

}