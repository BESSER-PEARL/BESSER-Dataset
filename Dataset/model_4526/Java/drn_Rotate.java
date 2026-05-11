





import java.util.List;
import java.util.ArrayList;

public class drn_Rotate extends Expression {

    private String name;
    private String tempsCST;
    private String angleCST;





    private drn_Parametre drn_parametre;




    private drn_And drn_and;




    private drn_Parametre drn_parametre;


    public drn_Rotate(
        String name,        String tempsCST,        String angleCST    ) {
        super(
        );
        this.name = name;
        this.tempsCST = tempsCST;
        this.angleCST = angleCST;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }
    public String getTempscst() {
        return tempsCST;
    }

    public void setTempscst(String tempsCST) {
        this.tempsCST = tempsCST;
    }
    public String getAnglecst() {
        return angleCST;
    }

    public void setAnglecst(String angleCST) {
        this.angleCST = angleCST;
    }

    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
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

}