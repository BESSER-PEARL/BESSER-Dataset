





import java.util.List;
import java.util.ArrayList;

public class CompleteDSLPckg_ArithmeticExpression extends Expression {

    private String operator;



    public CompleteDSLPckg_ArithmeticExpression(
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


}