





import java.util.List;
import java.util.ArrayList;

public class sensinact_DSL_ResourceAction  {

    private String variable;
    private String actiontype;





    private sensinact_DSL_REF sensinact_dsl_ref;




    private sensinact_DSL_ListActions sensinact_dsl_listactions;


    public sensinact_DSL_ResourceAction(
        String variable,        String actiontype    ) {
        this.variable = variable;
        this.actiontype = actiontype;
    }


    public String getVariable() {
        return variable;
    }

    public void setVariable(String variable) {
        this.variable = variable;
    }
    public String getActiontype() {
        return actiontype;
    }

    public void setActiontype(String actiontype) {
        this.actiontype = actiontype;
    }

    public sensinact_DSL_REF getSensinact_dsl_ref() {
        return sensinact_dsl_ref;
    }

    public void setSensinact_dsl_ref(sensinact_DSL_REF sensinact_dsl_ref) {
        this.sensinact_dsl_ref = sensinact_dsl_ref;
    }
    public sensinact_DSL_ListActions getSensinact_dsl_listactions() {
        return sensinact_dsl_listactions;
    }

    public void setSensinact_dsl_listactions(sensinact_DSL_ListActions sensinact_dsl_listactions) {
        this.sensinact_dsl_listactions = sensinact_dsl_listactions;
    }

}