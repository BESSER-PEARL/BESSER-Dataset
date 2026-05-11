





import java.util.List;
import java.util.ArrayList;

public class drn_DepY_Impl extends Expression {

    private String name;
    private String distanceCST;
    private String tempsCST;





    private drn_And drn_and;




    private drn_Parametre drn_parametre;




    private drn_Parametre drn_parametre;


    public drn_DepY_Impl(
        String name,        String distanceCST,        String tempsCST    ) {
        super(
        );
        this.name = name;
        this.distanceCST = distanceCST;
        this.tempsCST = tempsCST;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getDistancecst() {
        return distanceCST;
    }

    public void setDistancecst(String distanceCST) {
        this.distanceCST = distanceCST;
    }
    public String getTempscst() {
        return tempsCST;
    }

    public void setTempscst(String tempsCST) {
        this.tempsCST = tempsCST;
    }

    public drn_And getDrn_and() {
        return drn_and;
    }

    public void setDrn_and(drn_And drn_and) {
        this.drn_and = drn_and;
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