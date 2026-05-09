





import java.util.List;
import java.util.ArrayList;

public class HALL_Conditions_UnaryOperator extends PreConditionMessageExpressionElement {

    private String operatorname;





    private Conditions_PreConditionMessageExpressionElement conditions_preconditionmessageexpressionelement;


    public HALL_Conditions_UnaryOperator(
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

    public Conditions_PreConditionMessageExpressionElement getConditions_preconditionmessageexpressionelement() {
        return conditions_preconditionmessageexpressionelement;
    }

    public void setConditions_preconditionmessageexpressionelement(Conditions_PreConditionMessageExpressionElement conditions_preconditionmessageexpressionelement) {
        this.conditions_preconditionmessageexpressionelement = conditions_preconditionmessageexpressionelement;
    }

}