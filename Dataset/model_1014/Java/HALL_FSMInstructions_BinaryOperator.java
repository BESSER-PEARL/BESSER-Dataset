





import java.util.List;
import java.util.ArrayList;

public class HALL_FSMInstructions_BinaryOperator extends PosConditionExpressionElement {

    private String operatorname;



    public HALL_FSMInstructions_BinaryOperator(
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


}