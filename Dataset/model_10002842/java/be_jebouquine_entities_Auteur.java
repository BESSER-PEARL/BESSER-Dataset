





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Auteur  {

    private String nomAuteur;
    private int idAuteur;





    private be_jebouquine_entities_Livre be_jebouquine_entities_livre;


    public be_jebouquine_entities_Auteur(
        String nomAuteur,        int idAuteur    ) {
        this.nomAuteur = nomAuteur;
        this.idAuteur = idAuteur;
    }


    public String getNomauteur() {
        return nomAuteur;
    }

    public void setNomauteur(String nomAuteur) {
        this.nomAuteur = nomAuteur;
    }
    public int getIdauteur() {
        return idAuteur;
    }

    public void setIdauteur(int idAuteur) {
        this.idAuteur = idAuteur;
    }

    public be_jebouquine_entities_Livre getBe_jebouquine_entities_livre() {
        return be_jebouquine_entities_livre;
    }

    public void setBe_jebouquine_entities_livre(be_jebouquine_entities_Livre be_jebouquine_entities_livre) {
        this.be_jebouquine_entities_livre = be_jebouquine_entities_livre;
    }

}