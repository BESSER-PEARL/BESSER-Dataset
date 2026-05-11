





import java.util.List;
import java.util.ArrayList;

public class hlp_Condition  {

    private String operator;





    private hlp_ConditionalLoop hlp_conditionalloop;




    private hlp_Expression hlp_expression;




    private hlp_Expression hlp_expression;




    private hlp_IfStatement hlp_ifstatement;


    public hlp_Condition(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public hlp_ConditionalLoop getHlp_conditionalloop() {
        return hlp_conditionalloop;
    }

    public void setHlp_conditionalloop(hlp_ConditionalLoop hlp_conditionalloop) {
        this.hlp_conditionalloop = hlp_conditionalloop;
    }
    public hlp_Expression getHlp_expression() {
        return hlp_expression;
    }

    public void setHlp_expression(hlp_Expression hlp_expression) {
        this.hlp_expression = hlp_expression;
    }
    public hlp_Expression getHlp_expression() {
        return hlp_expression;
    }

    public void setHlp_expression(hlp_Expression hlp_expression) {
        this.hlp_expression = hlp_expression;
    }
    public hlp_IfStatement getHlp_ifstatement() {
        return hlp_ifstatement;
    }

    public void setHlp_ifstatement(hlp_IfStatement hlp_ifstatement) {
        this.hlp_ifstatement = hlp_ifstatement;
    }

}