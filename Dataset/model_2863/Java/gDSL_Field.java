





import java.util.List;
import java.util.ArrayList;

public class gDSL_Field  {

    private String name;





    private gDSL_Exp gdsl_exp;




    private gDSL_AtomicExp gdsl_atomicexp;


    public gDSL_Field(
        String name    ) {
        this.name = name;
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
    public gDSL_AtomicExp getGdsl_atomicexp() {
        return gdsl_atomicexp;
    }

    public void setGdsl_atomicexp(gDSL_AtomicExp gdsl_atomicexp) {
        this.gdsl_atomicexp = gdsl_atomicexp;
    }

}