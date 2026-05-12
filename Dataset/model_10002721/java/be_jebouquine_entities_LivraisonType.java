





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_LivraisonType  {

    private float prixLivraison;
    private String typeLivraison;
    private int idLivraison;





    private List<be_jebouquine_entities_Commande> be_jebouquine_entities_commandes;


    public be_jebouquine_entities_LivraisonType(
        float prixLivraison,        String typeLivraison,        int idLivraison    ) {
        this.prixLivraison = prixLivraison;
        this.typeLivraison = typeLivraison;
        this.idLivraison = idLivraison;
        this.be_jebouquine_entities_commandes = new ArrayList<>();
    }

    public be_jebouquine_entities_LivraisonType(
        float prixLivraison,        String typeLivraison,        int idLivraison        ArrayList<be_jebouquine_entities_Commande> be_jebouquine_entities_commandes    ) {
        this.prixLivraison = prixLivraison;
        this.typeLivraison = typeLivraison;
        this.idLivraison = idLivraison;
        this.be_jebouquine_entities_commandes = be_jebouquine_entities_commandes;
    }

    public float getPrixlivraison() {
        return prixLivraison;
    }

    public void setPrixlivraison(float prixLivraison) {
        this.prixLivraison = prixLivraison;
    }
    public String getTypelivraison() {
        return typeLivraison;
    }

    public void setTypelivraison(String typeLivraison) {
        this.typeLivraison = typeLivraison;
    }
    public int getIdlivraison() {
        return idLivraison;
    }

    public void setIdlivraison(int idLivraison) {
        this.idLivraison = idLivraison;
    }

    public List<be_jebouquine_entities_Commande> getBe_jebouquine_entities_commandes() {
        return be_jebouquine_entities_commandes;
    }

    public void addBe_jebouquine_entities_commande(Be_jebouquine_entities_commande be_jebouquine_entities_commande) {
        this.be_jebouquine_entities_commandes.add(be_jebouquine_entities_commande);
    }

}