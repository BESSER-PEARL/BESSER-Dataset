





import java.util.List;
import java.util.ArrayList;

public class mathInterpreter_MultiplyOrDivide  {

    private String operator;





    private mathInterpreter_EObject mathinterpreter_eobject;




    private mathInterpreter_PlusOrMinus mathinterpreter_plusorminus;


    public mathInterpreter_MultiplyOrDivide(
        String operator    ) {
        this.operator = operator;
    }


    public String getOperator() {
        return operator;
    }

    public void setOperator(String operator) {
        this.operator = operator;
    }

    public mathInterpreter_EObject getMathinterpreter_eobject() {
        return mathinterpreter_eobject;
    }

    public void setMathinterpreter_eobject(mathInterpreter_EObject mathinterpreter_eobject) {
        this.mathinterpreter_eobject = mathinterpreter_eobject;
    }
    public mathInterpreter_PlusOrMinus getMathinterpreter_plusorminus() {
        return mathinterpreter_plusorminus;
    }

    public void setMathinterpreter_plusorminus(mathInterpreter_PlusOrMinus mathinterpreter_plusorminus) {
        this.mathinterpreter_plusorminus = mathinterpreter_plusorminus;
    }

}