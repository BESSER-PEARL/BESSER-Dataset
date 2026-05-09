





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMConditions_UnaryOperator extends PreConditionExpression {

    private String operatorname;





    private FSMConditions_PreConditionExpression fsmconditions_preconditionexpression;


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

    public FSMConditions_PreConditionExpression getFsmconditions_preconditionexpression() {
        return fsmconditions_preconditionexpression;
    }

    public void setFsmconditions_preconditionexpression(FSMConditions_PreConditionExpression fsmconditions_preconditionexpression) {
        this.fsmconditions_preconditionexpression = fsmconditions_preconditionexpression;
    }

}