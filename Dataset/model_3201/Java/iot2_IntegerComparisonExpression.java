





import java.util.List;
import java.util.ArrayList;

public class iot2_IntegerComparisonExpression extends IntegerExpression {

    private String operator;





    private iot2_BooleanVariable iot2_booleanvariable;


    public iot2_IntegerComparisonExpression(
        String operator    ) {
        super(
        );
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public iot2_BooleanVariable getIot2_booleanvariable() {
        return iot2_booleanvariable;
    }

    public void setIot2_booleanvariable(iot2_BooleanVariable iot2_booleanvariable) {
        this.iot2_booleanvariable = iot2_booleanvariable;
    }

}