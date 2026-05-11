





import java.util.List;
import java.util.ArrayList;

public class drn_DepXYZ extends DepXYZ_IMPL {

    private String tempsCST;
    private String distanceCST;





    private drn_Parametre drn_parametre;




    private drn_Parametre drn_parametre;


    public drn_DepXYZ(
        String tempsCST,        String distanceCST    ) {
        super(
        );
        this.tempsCST = tempsCST;
        this.distanceCST = distanceCST;
    }


    public String getTempscst() {
        return tempsCST;
    }

    public void setTempscst(String tempsCST) {
        this.tempsCST = tempsCST;
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
    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
    }

}