





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_UnaryOperator extends PosConditionExpression {

    private String operatorname;





    private FSMInstructions_PosConditionExpression fsminstructions_posconditionexpression;


    public HALL_FSMInstructions_UnaryOperator(
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

    public FSMInstructions_PosConditionExpression getFsminstructions_posconditionexpression() {
        return fsminstructions_posconditionexpression;
    }

    public void setFsminstructions_posconditionexpression(FSMInstructions_PosConditionExpression fsminstructions_posconditionexpression) {
        this.fsminstructions_posconditionexpression = fsminstructions_posconditionexpression;
    }

}