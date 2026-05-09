





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMConditions_UnaryOperator extends PreConditionExpressionElement {

    private String operatorname;





    private FSMConditions_PreConditionExpressionElement fsmconditions_preconditionexpressionelement;


    public HALL_FSMConditions_UnaryOperator(
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

    public FSMConditions_PreConditionExpressionElement getFsmconditions_preconditionexpressionelement() {
        return fsmconditions_preconditionexpressionelement;
    }

    public void setFsmconditions_preconditionexpressionelement(FSMConditions_PreConditionExpressionElement fsmconditions_preconditionexpressionelement) {
        this.fsmconditions_preconditionexpressionelement = fsmconditions_preconditionexpressionelement;
    }

}