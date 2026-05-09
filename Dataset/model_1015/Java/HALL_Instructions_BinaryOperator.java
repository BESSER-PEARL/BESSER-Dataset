





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_BinaryOperator extends PosConditionMessageExpressionElement {

    private String operatorname;



    public HALL_Instructions_BinaryOperator(
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