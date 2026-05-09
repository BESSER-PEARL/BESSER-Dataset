





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_UnaryOperator extends PosConditionMessageExpressionElement {

    private String operatorname;





    private Instructions_PosConditionMessageExpressionElement instructions_posconditionmessageexpressionelement;


    public HALL_Instructions_UnaryOperator(
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

    public Instructions_PosConditionMessageExpressionElement getInstructions_posconditionmessageexpressionelement() {
        return instructions_posconditionmessageexpressionelement;
    }

    public void setInstructions_posconditionmessageexpressionelement(Instructions_PosConditionMessageExpressionElement instructions_posconditionmessageexpressionelement) {
        this.instructions_posconditionmessageexpressionelement = instructions_posconditionmessageexpressionelement;
    }

}