





import java.util.List;
import java.util.ArrayList;

public class ccsl_expressions_BooleanExpression extends OperatorExpression {

    private String booleanOperator;



    public ccsl_expressions_BooleanExpression(
        String booleanOperator    ) {
        super(
        );
        this.booleanOperator = booleanOperator;
    }


    public String getBooleanoperator() {
        return booleanOperator;
    }

    public void setBooleanoperator(String booleanOperator) {
        this.booleanOperator = booleanOperator;
    }


}