





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_LivraisonType  {

    private String typeLivraison;
    private float prixLivraison;
    private int idLivraison;



    public be_jebouquine_entities_LivraisonType(
        String typeLivraison,        float prixLivraison,        int idLivraison    ) {
        this.typeLivraison = typeLivraison;
        this.prixLivraison = prixLivraison;
        this.idLivraison = idLivraison;
    }


    public String getTypelivraison() {
        return typeLivraison;
    }

    public void setTypelivraison(String typeLivraison) {
        this.typeLivraison = typeLivraison;
    }
    public float getPrixlivraison() {
        return prixLivraison;
    }

    public void setPrixlivraison(float prixLivraison) {
        this.prixLivraison = prixLivraison;
    }
    public int getIdlivraison() {
        return idLivraison;
    }

    public void setIdlivraison(int idLivraison) {
        this.idLivraison = idLivraison;
    }


}