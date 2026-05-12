





import java.util.List;
import java.util.ArrayList;

public class be_jebouquine_entities_Langue  {

    private String libelleLangue;
    private int idLangue;



    public be_jebouquine_entities_Langue(
        String libelleLangue,        int idLangue    ) {
        this.libelleLangue = libelleLangue;
        this.idLangue = idLangue;
    }


    public String getLibellelangue() {
        return libelleLangue;
    }

    public void setLibellelangue(String libelleLangue) {
        this.libelleLangue = libelleLangue;
    }
    public int getIdlangue() {
        return idLangue;
    }

    public void setIdlangue(int idLangue) {
        this.idLangue = idLangue;
    }


}