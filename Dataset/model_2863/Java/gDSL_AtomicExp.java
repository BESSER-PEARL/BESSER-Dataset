





import java.util.List;
import java.util.ArrayList;

public class gDSL_AtomicExp extends ApplyExp {

    private String id;





    private gDSL_ApplyExp gdsl_applyexp;




    private gDSL_Exp gdsl_exp;




    private List<gDSL_Exp> gdsl_exps;


    public gDSL_AtomicExp(
        String id    ) {
        super(
        );
        this.id = id;
        this.gdsl_exps = new ArrayList<>();
    }

    public gDSL_AtomicExp(
        String id        ArrayList<gDSL_Exp> gdsl_exps    ) {
        this.id = id;
        this.gdsl_exps = gdsl_exps;
    }

    public String getId() {
        return id;
    }

    public void setId(String id) {
        this.id = id;
    }

    public gDSL_ApplyExp getGdsl_applyexp() {
        return gdsl_applyexp;
    }

    public void setGdsl_applyexp(gDSL_ApplyExp gdsl_applyexp) {
        this.gdsl_applyexp = gdsl_applyexp;
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

}