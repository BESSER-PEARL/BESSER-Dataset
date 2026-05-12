





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Categorie  {

    private int idCategorie;
    private String ordreCategorie;





    private be_jebouquine_entities_Livre be_jebouquine_entities_livre;


    public be_jebouquine_entities_Categorie(
        int idCategorie,        String ordreCategorie    ) {
        this.idCategorie = idCategorie;
        this.ordreCategorie = ordreCategorie;
    }


    public int getIdcategorie() {
        return idCategorie;
    }

    public void setIdcategorie(int idCategorie) {
        this.idCategorie = idCategorie;
    }
    public String getOrdrecategorie() {
        return ordreCategorie;
    }

    public void setOrdrecategorie(String ordreCategorie) {
        this.ordreCategorie = ordreCategorie;
    }

    public be_jebouquine_entities_Livre getBe_jebouquine_entities_livre() {
        return be_jebouquine_entities_livre;
    }

    public void setBe_jebouquine_entities_livre(be_jebouquine_entities_Livre be_jebouquine_entities_livre) {
        this.be_jebouquine_entities_livre = be_jebouquine_entities_livre;
    }

}