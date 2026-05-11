





import java.util.List;
import java.util.ArrayList;

public class gDSL_ValueDecl  {

    private String ids;
    private String name;





    private gDSL_AtomicExp gdsl_atomicexp;




    private gDSL_Exp gdsl_exp;


    public gDSL_ValueDecl(
        String ids,        String name    ) {
        this.ids = ids;
        this.name = name;
    }


    public String getIds() {
        return ids;
    }

    public void setIds(String ids) {
        this.ids = ids;
    }
    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public gDSL_AtomicExp getGdsl_atomicexp() {
        return gdsl_atomicexp;
    }

    public void setGdsl_atomicexp(gDSL_AtomicExp gdsl_atomicexp) {
        this.gdsl_atomicexp = gdsl_atomicexp;
    }
    public gDSL_Exp getGdsl_exp() {
        return gdsl_exp;
    }

    public void setGdsl_exp(gDSL_Exp gdsl_exp) {
        this.gdsl_exp = gdsl_exp;
    }

}