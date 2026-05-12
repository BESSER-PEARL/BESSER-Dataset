





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_LigneCommande  {

    private int idLigneCommande;
    private int idCommande;
    private int idLivre;



    public be_jebouquine_entities_LigneCommande(
        int idLigneCommande,        int idCommande,        int idLivre    ) {
        this.idLigneCommande = idLigneCommande;
        this.idCommande = idCommande;
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
    public int getIdlivre() {
        return idLivre;
    }

    public void setIdlivre(int idLivre) {
        this.idLivre = idLivre;
    }


}