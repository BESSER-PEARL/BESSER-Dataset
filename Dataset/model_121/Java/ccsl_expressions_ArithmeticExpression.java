





import java.util.List;
import java.util.ArrayList;

public class ccsl_expressions_ArithmeticExpression extends OperatorExpression {

    private String arithmeticOperator;



    public ccsl_expressions_ArithmeticExpression(
        String arithmeticOperator    ) {
        super(
        );
        this.arithmeticOperator = arithmeticOperator;
    }


    public String getArithmeticoperator() {
        return arithmeticOperator;
    }

    public void setArithmeticoperator(String arithmeticOperator) {
        this.arithmeticOperator = arithmeticOperator;
    }


}