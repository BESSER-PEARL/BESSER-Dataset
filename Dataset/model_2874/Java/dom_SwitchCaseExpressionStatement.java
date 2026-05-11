





import java.util.List;
import java.util.ArrayList;

public class dom_SwitchCaseExpressionStatement extends SwitchCaseStatement {






    private dom_SwitchStatement dom_switchstatement;




    private dom_Expression dom_expression;


    public dom_SwitchCaseExpressionStatement(
    ) {
        super(
        );
    }



    public dom_SwitchStatement getDom_switchstatement() {
        return dom_switchstatement;
    }

    public void setDom_switchstatement(dom_SwitchStatement dom_switchstatement) {
        this.dom_switchstatement = dom_switchstatement;
    }
    public dom_Expression getDom_expression() {
        return dom_expression;
    }

    public void setDom_expression(dom_Expression dom_expression) {
        this.dom_expression = dom_expression;
    }

}