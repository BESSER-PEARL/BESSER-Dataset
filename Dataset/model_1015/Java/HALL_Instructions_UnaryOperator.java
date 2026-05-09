





import java.util.List;
import java.util.ArrayList;

public class HALL_Instructions_UnaryOperator extends PosConditionMessageExpressionElement {

    private String operatorname;



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


}