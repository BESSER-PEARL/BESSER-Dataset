





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_EtatCommande  {

    private int idEtat;
    private String libelleEtat;





    private List<be_jebouquine_entities_Commande> be_jebouquine_entities_commandes;


    public be_jebouquine_entities_EtatCommande(
        int idEtat,        String libelleEtat    ) {
        this.idEtat = idEtat;
        this.libelleEtat = libelleEtat;
        this.be_jebouquine_entities_commandes = new ArrayList<>();
    }

    public be_jebouquine_entities_EtatCommande(
        int idEtat,        String libelleEtat        ArrayList<be_jebouquine_entities_Commande> be_jebouquine_entities_commandes    ) {
        this.idEtat = idEtat;
        this.libelleEtat = libelleEtat;
        this.be_jebouquine_entities_commandes = be_jebouquine_entities_commandes;
    }

    public int getIdetat() {
        return idEtat;
    }

    public void setIdetat(int idEtat) {
        this.idEtat = idEtat;
    }
    public String getLibelleetat() {
        return libelleEtat;
    }

    public void setLibelleetat(String libelleEtat) {
        this.libelleEtat = libelleEtat;
    }

    public List<be_jebouquine_entities_Commande> getBe_jebouquine_entities_commandes() {
        return be_jebouquine_entities_commandes;
    }

    public void addBe_jebouquine_entities_commande(Be_jebouquine_entities_commande be_jebouquine_entities_commande) {
        this.be_jebouquine_entities_commandes.add(be_jebouquine_entities_commande);
    }

}