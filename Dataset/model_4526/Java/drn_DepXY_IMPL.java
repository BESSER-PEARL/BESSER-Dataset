





import java.util.List;
import java.util.ArrayList;

public class drn_DepXY_IMPL extends Expression {

    private String name;
    private String tempsCST;





    private drn_Parametre drn_parametre;


    public drn_DepXY_IMPL(
        String name,        String tempsCST    ) {
        super(
        );
        this.name = name;
        this.tempsCST = tempsCST;
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

    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
    }

}