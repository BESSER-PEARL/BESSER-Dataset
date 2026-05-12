





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Editeur  {

    private int idEditeur;
    private String adresseEditeur;
    private String nomEditeur;





    private be_jebouquine_entities_Livre be_jebouquine_entities_livre;


    public be_jebouquine_entities_Editeur(
        int idEditeur,        String adresseEditeur,        String nomEditeur    ) {
        this.idEditeur = idEditeur;
        this.adresseEditeur = adresseEditeur;
        this.nomEditeur = nomEditeur;
    }


    public int getIdediteur() {
        return idEditeur;
    }

    public void setIdediteur(int idEditeur) {
        this.idEditeur = idEditeur;
    }
    public String getAdresseediteur() {
        return adresseEditeur;
    }

    public void setAdresseediteur(String adresseEditeur) {
        this.adresseEditeur = adresseEditeur;
    }
    public String getNomediteur() {
        return nomEditeur;
    }

    public void setNomediteur(String nomEditeur) {
        this.nomEditeur = nomEditeur;
    }

    public be_jebouquine_entities_Livre getBe_jebouquine_entities_livre() {
        return be_jebouquine_entities_livre;
    }

    public void setBe_jebouquine_entities_livre(be_jebouquine_entities_Livre be_jebouquine_entities_livre) {
        this.be_jebouquine_entities_livre = be_jebouquine_entities_livre;
    }

}