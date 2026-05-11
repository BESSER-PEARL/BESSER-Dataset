





import java.util.List;
import java.util.ArrayList;

public class mathInterpreter_PlusOrMinus  {

    private String operator;





    private mathInterpreter_Expression mathinterpreter_expression;


    public mathInterpreter_PlusOrMinus(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public mathInterpreter_Expression getMathinterpreter_expression() {
        return mathinterpreter_expression;
    }

    public void setMathinterpreter_expression(mathInterpreter_Expression mathinterpreter_expression) {
        this.mathinterpreter_expression = mathinterpreter_expression;
    }

}