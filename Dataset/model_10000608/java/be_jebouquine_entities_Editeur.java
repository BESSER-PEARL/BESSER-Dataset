





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Editeur  {

    private String nomEditeur;
    private int idEditeur;
    private String adresseEditeur;





    private be_jebouquine_entities_Livre be_jebouquine_entities_livre;


    public be_jebouquine_entities_Editeur(
        String nomEditeur,        int idEditeur,        String adresseEditeur    ) {
        this.nomEditeur = nomEditeur;
        this.idEditeur = idEditeur;
        this.adresseEditeur = adresseEditeur;
    }


    public String getNomediteur() {
        return nomEditeur;
    }

    public void setNomediteur(String nomEditeur) {
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

    public be_jebouquine_entities_Livre getBe_jebouquine_entities_livre() {
        return be_jebouquine_entities_livre;
    }

    public void setBe_jebouquine_entities_livre(be_jebouquine_entities_Livre be_jebouquine_entities_livre) {
        this.be_jebouquine_entities_livre = be_jebouquine_entities_livre;
    }

}