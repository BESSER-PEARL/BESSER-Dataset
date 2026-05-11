





import java.util.List;
import java.util.ArrayList;

public class drn_CARREYZ extends DepYZ_IMPL {

    private String coteCST;





    private drn_Parametre drn_parametre;


    public drn_CARREYZ(
        String coteCST    ) {
        super(
        );
        this.coteCST = coteCST;
    }


    public String getCotecst() {
        return coteCST;
    }

    public void setCotecst(String coteCST) {
        this.coteCST = coteCST;
    }

    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
    }

}