





import java.util.List;
import java.util.ArrayList;

public class wh_Affect  {

    private String vars;
    private String exprs;



    public wh_Affect(
        String vars,        String exprs    ) {
        this.vars = vars;
        this.exprs = exprs;
    }


    public String getVars() {
        return vars;
    }

    public void setVars(String vars) {
        this.vars = vars;
    }
    public String getExprs() {
        return exprs;
    }

    public void setExprs(String exprs) {
        this.exprs = exprs;
    }


}