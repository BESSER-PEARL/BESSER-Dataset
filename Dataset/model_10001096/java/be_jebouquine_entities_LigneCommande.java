





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_LigneCommande  {

    private int idLivre;
    private int idLigneCommande;
    private int idCommande;





    private be_jebouquine_entities_Commande be_jebouquine_entities_commande;




    private be_jebouquine_entities_Livre be_jebouquine_entities_livre;


    public be_jebouquine_entities_LigneCommande(
        int idLivre,        int idLigneCommande,        int idCommande    ) {
        this.idLivre = idLivre;
        this.idLigneCommande = idLigneCommande;
        this.idCommande = idCommande;
    }


    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }
    public int getIdlignecommande() {
        return idLigneCommande;
    }

    public void setIdlignecommande(int idLigneCommande) {
        this.idLigneCommande = idLigneCommande;
    }
    public int getIdcommande() {
        return idCommande;
    }

    public void setIdcommande(int idCommande) {
        this.idCommande = idCommande;
    }

    public be_jebouquine_entities_Commande getBe_jebouquine_entities_commande() {
        return be_jebouquine_entities_commande;
    }

    public void setBe_jebouquine_entities_commande(be_jebouquine_entities_Commande be_jebouquine_entities_commande) {
        this.be_jebouquine_entities_commande = be_jebouquine_entities_commande;
    }
    public be_jebouquine_entities_Livre getBe_jebouquine_entities_livre() {
        return be_jebouquine_entities_livre;
    }

    public void setBe_jebouquine_entities_livre(be_jebouquine_entities_Livre be_jebouquine_entities_livre) {
        this.be_jebouquine_entities_livre = be_jebouquine_entities_livre;
    }

}