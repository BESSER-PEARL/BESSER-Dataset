





import java.util.List;
import java.util.ArrayList;

public class HALL_Conditions_UnaryOperator extends PreConditionMessageExpression {

    private String operatorname;





    private Conditions_PreConditionMessageExpression conditions_preconditionmessageexpression;


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

    public Conditions_PreConditionMessageExpression getConditions_preconditionmessageexpression() {
        return conditions_preconditionmessageexpression;
    }

    public void setConditions_preconditionmessageexpression(Conditions_PreConditionMessageExpression conditions_preconditionmessageexpression) {
        this.conditions_preconditionmessageexpression = conditions_preconditionmessageexpression;
    }

}