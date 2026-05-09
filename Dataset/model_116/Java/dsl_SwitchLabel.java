





import java.util.List;
import java.util.ArrayList;

public class dsl_SwitchLabel  {

    private String defaultOp;





    private dsl_Expression dsl_expression;




    private dsl_SwitchStatement dsl_switchstatement;


    public dsl_SwitchLabel(
        String defaultOp    ) {
        this.defaultOp = defaultOp;
    }


    public String getDefaultop() {
        return defaultOp;
    }

    public void setDefaultop(String defaultOp) {
        this.defaultOp = defaultOp;
    }

    public dsl_Expression getDsl_expression() {
        return dsl_expression;
    }

    public void setDsl_expression(dsl_Expression dsl_expression) {
        this.dsl_expression = dsl_expression;
    }
    public dsl_SwitchStatement getDsl_switchstatement() {
        return dsl_switchstatement;
    }

    public void setDsl_switchstatement(dsl_SwitchStatement dsl_switchstatement) {
        this.dsl_switchstatement = dsl_switchstatement;
    }

}