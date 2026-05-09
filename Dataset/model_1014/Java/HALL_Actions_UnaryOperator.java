





import java.util.List;
import java.util.ArrayList;

public class HALL_Actions_UnaryOperator extends ActionMessageExpressionElement {

    private String operatorname;





    private Actions_ActionMessageExpressionElement actions_actionmessageexpressionelement;


    public HALL_Actions_UnaryOperator(
        String operatorname    ) {
        super(
        );
        this.operatorname = operatorname;
    }


    public String getOperatorname() {
        return operatorname;
    }

    public void setOperatorname(String operatorname) {
        this.operatorname = operatorname;
    }

    public Actions_ActionMessageExpressionElement getActions_actionmessageexpressionelement() {
        return actions_actionmessageexpressionelement;
    }

    public void setActions_actionmessageexpressionelement(Actions_ActionMessageExpressionElement actions_actionmessageexpressionelement) {
        this.actions_actionmessageexpressionelement = actions_actionmessageexpressionelement;
    }

}