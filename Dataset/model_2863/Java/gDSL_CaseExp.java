





import java.util.List;
import java.util.ArrayList;

public class gDSL_CaseExp  {

    private String name;





    private gDSL_Exp gdsl_exp;




    private List<gDSL_Exp> gdsl_exps;




    private gDSL_Exp gdsl_exp;


    public gDSL_CaseExp(
        String name    ) {
        this.name = name;
        this.gdsl_exps = new ArrayList<>();
    }

    public gDSL_CaseExp(
        String name        ArrayList<gDSL_Exp> gdsl_exps    ) {
        this.name = name;
        this.gdsl_exps = gdsl_exps;
    }

    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gDSL_Exp getGdsl_exp() {
        return gdsl_exp;
    }

    public void setGdsl_exp(gDSL_Exp gdsl_exp) {
        this.gdsl_exp = gdsl_exp;
    }
    public List<gDSL_Exp> getGdsl_exps() {
        return gdsl_exps;
    }

    public void addGdsl_exp(Gdsl_exp gdsl_exp) {
        this.gdsl_exps.add(gdsl_exp);
    }
    public gDSL_Exp getGdsl_exp() {
        return gdsl_exp;
    }

    public void setGdsl_exp(gDSL_Exp gdsl_exp) {
        this.gdsl_exp = gdsl_exp;
    }

}