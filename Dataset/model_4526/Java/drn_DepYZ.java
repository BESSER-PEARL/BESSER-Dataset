





import java.util.List;
import java.util.ArrayList;

public class drn_DepYZ extends DepYZ_IMPL {

    private String distanceCST;





    private drn_Parametre drn_parametre;


    public drn_DepYZ(
        String distanceCST    ) {
        super(
        );
        this.distanceCST = distanceCST;
    }


    public String getDistancecst() {
        return distanceCST;
    }

    public void setDistancecst(String distanceCST) {
        this.distanceCST = distanceCST;
    }

    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
    }

}