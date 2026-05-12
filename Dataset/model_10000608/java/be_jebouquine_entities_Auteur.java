





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Auteur  {

    private int idAuteur;
    private String nomAuteur;





    private be_jebouquine_entities_Livre be_jebouquine_entities_livre;


    public be_jebouquine_entities_Auteur(
        int idAuteur,        String nomAuteur    ) {
        this.idAuteur = idAuteur;
        this.nomAuteur = nomAuteur;
    }


    public int getIdauteur() {
        return idAuteur;
    }

    public void setIdauteur(int idAuteur) {
        this.idAuteur = idAuteur;
    }
    public String getNomauteur() {
        return nomAuteur;
    }

    public void setNomauteur(String nomAuteur) {
        this.nomAuteur = nomAuteur;
    }

    public be_jebouquine_entities_Livre getBe_jebouquine_entities_livre() {
        return be_jebouquine_entities_livre;
    }

    public void setBe_jebouquine_entities_livre(be_jebouquine_entities_Livre be_jebouquine_entities_livre) {
        this.be_jebouquine_entities_livre = be_jebouquine_entities_livre;
    }

}