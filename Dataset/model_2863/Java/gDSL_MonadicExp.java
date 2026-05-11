





import java.util.List;
import java.util.ArrayList;

public class gDSL_MonadicExp  {

    private String name;





    private gDSL_Exp gdsl_exp;




    private gDSL_ClosedExp gdsl_closedexp;


    public gDSL_MonadicExp(
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
    public gDSL_ClosedExp getGdsl_closedexp() {
        return gdsl_closedexp;
    }

    public void setGdsl_closedexp(gDSL_ClosedExp gdsl_closedexp) {
        this.gdsl_closedexp = gdsl_closedexp;
    }

}