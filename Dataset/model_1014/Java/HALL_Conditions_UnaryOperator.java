





import java.util.List;
import java.util.ArrayList;

public class HALL_Conditions_UnaryOperator extends PreConditionMessageExpressionElement {

    private String operatorname;



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


}