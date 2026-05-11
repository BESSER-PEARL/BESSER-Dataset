





import java.util.List;
import java.util.ArrayList;

public class gDSL_CONS  {

    private String conName;





    private gDSL_ConDecl gdsl_condecl;


    public gDSL_CONS(
        String conName    ) {
        this.conName = conName;
    }


    public String getConname() {
        return conName;
    }

    public void setConname(String conName) {
        this.conName = conName;
    }

    public gDSL_ConDecl getGdsl_condecl() {
        return gdsl_condecl;
    }

    public void setGdsl_condecl(gDSL_ConDecl gdsl_condecl) {
        this.gdsl_condecl = gdsl_condecl;
    }

}