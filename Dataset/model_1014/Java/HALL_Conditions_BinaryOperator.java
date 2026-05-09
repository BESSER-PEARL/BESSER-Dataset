





import java.util.List;
import java.util.ArrayList;

public class HALL_Conditions_BinaryOperator extends PreConditionMessageExpressionElement {

    private String operatorname;



    public HALL_Conditions_BinaryOperator(
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