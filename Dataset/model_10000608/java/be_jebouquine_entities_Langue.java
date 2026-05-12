





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Langue  {

    private int idLangue;
    private String libelleLangue;





    private List<be_jebouquine_entities_Livre> be_jebouquine_entities_livres;


    public be_jebouquine_entities_Langue(
        int idLangue,        String libelleLangue    ) {
        this.idLangue = idLangue;
        this.libelleLangue = libelleLangue;
        this.be_jebouquine_entities_livres = new ArrayList<>();
    }

    public be_jebouquine_entities_Langue(
        int idLangue,        String libelleLangue        ArrayList<be_jebouquine_entities_Livre> be_jebouquine_entities_livres    ) {
        this.idLangue = idLangue;
        this.libelleLangue = libelleLangue;
        this.be_jebouquine_entities_livres = be_jebouquine_entities_livres;
    }

    public int getIdlangue() {
        return idLangue;
    }

    public void setIdlangue(int idLangue) {
        this.idLangue = idLangue;
    }
    public String getLibellelangue() {
        return libelleLangue;
    }

    public void setLibellelangue(String libelleLangue) {
        this.libelleLangue = libelleLangue;
    }

    public List<be_jebouquine_entities_Livre> getBe_jebouquine_entities_livres() {
        return be_jebouquine_entities_livres;
    }

    public void addBe_jebouquine_entities_livre(Be_jebouquine_entities_livre be_jebouquine_entities_livre) {
        this.be_jebouquine_entities_livres.add(be_jebouquine_entities_livre);
    }

}