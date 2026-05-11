





import java.util.List;
import java.util.ArrayList;

public class drn_DepYZ_IMPL extends Expression {

    private String tempsCST;
    private String name;





    private drn_Parametre drn_parametre;


    public drn_DepYZ_IMPL(
        String tempsCST,        String name    ) {
        super(
        );
        this.tempsCST = tempsCST;
        this.name = name;
    }


    public String getTempscst() {
        return tempsCST;
    }

    public void setTempscst(String tempsCST) {
        this.tempsCST = tempsCST;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public drn_Parametre getDrn_parametre() {
        return drn_parametre;
    }

    public void setDrn_parametre(drn_Parametre drn_parametre) {
        this.drn_parametre = drn_parametre;
    }

}