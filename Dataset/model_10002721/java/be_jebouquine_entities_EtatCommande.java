





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_EtatCommande  {

    private String libelleEtat;
    private int idEtat;





    private List<be_jebouquine_entities_Commande> be_jebouquine_entities_commandes;


    public be_jebouquine_entities_EtatCommande(
        String libelleEtat,        int idEtat    ) {
        this.libelleEtat = libelleEtat;
        this.idEtat = idEtat;
        this.be_jebouquine_entities_commandes = new ArrayList<>();
    }

    public be_jebouquine_entities_EtatCommande(
        String libelleEtat,        int idEtat        ArrayList<be_jebouquine_entities_Commande> be_jebouquine_entities_commandes    ) {
        this.libelleEtat = libelleEtat;
        this.idEtat = idEtat;
        this.be_jebouquine_entities_commandes = be_jebouquine_entities_commandes;
    }

    public String getLibelleetat() {
        return libelleEtat;
    }

    public void setLibelleetat(String libelleEtat) {
        this.libelleEtat = libelleEtat;
    }
    public int getIdetat() {
        return idEtat;
    }

    public void setIdetat(int idEtat) {
        this.idEtat = idEtat;
    }

    public List<be_jebouquine_entities_Commande> getBe_jebouquine_entities_commandes() {
        return be_jebouquine_entities_commandes;
    }

    public void addBe_jebouquine_entities_commande(Be_jebouquine_entities_commande be_jebouquine_entities_commande) {
        this.be_jebouquine_entities_commandes.add(be_jebouquine_entities_commande);
    }

}