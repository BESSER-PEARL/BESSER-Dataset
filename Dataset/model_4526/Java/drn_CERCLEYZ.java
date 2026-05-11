





import java.util.List;
import java.util.ArrayList;

public class drn_CERCLEYZ extends DepYZ_IMPL {

    private String rayonCST;





    private drn_Parametre drn_parametre;


    public drn_CERCLEYZ(
        String rayonCST    ) {
        super(
        );
        this.rayonCST = rayonCST;
    }


    public String getRayoncst() {
        return rayonCST;
    }

    public void setRayoncst(String rayonCST) {
        this.rayonCST = rayonCST;
    }

    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
    }

}