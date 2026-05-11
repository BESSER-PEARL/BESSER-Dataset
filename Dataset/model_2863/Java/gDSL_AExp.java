





import java.util.List;
import java.util.ArrayList;

public class gDSL_AExp extends RExp {

    private String sym;





    private gDSL_AExp gdsl_aexp;


    public gDSL_AExp(
        String sym    ) {
        super(
        );
        this.sym = sym;
    }


    public String getSym() {
        return sym;
    }

    public void setSym(String sym) {
        this.sym = sym;
    }

    public gDSL_AExp getGdsl_aexp() {
        return gdsl_aexp;
    }

    public void setGdsl_aexp(gDSL_AExp gdsl_aexp) {
        this.gdsl_aexp = gdsl_aexp;
    }

}