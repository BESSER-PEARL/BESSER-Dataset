





import java.util.List;
import java.util.ArrayList;

public class mathinterpreter_Variable  {

    private String name;





    private mathinterpreter_PMExpression mathinterpreter_pmexpression;




    private mathinterpreter_DefineExpr mathinterpreter_defineexpr;


    public mathinterpreter_Variable(
        String name    ) {
        this.name = name;
    }


    public String getName() {
        return name;
    }

    public void setName(String name) {
        this.name = name;
    }

    public mathinterpreter_PMExpression getMathinterpreter_pmexpression() {
        return mathinterpreter_pmexpression;
    }

    public void setMathinterpreter_pmexpression(mathinterpreter_PMExpression mathinterpreter_pmexpression) {
        this.mathinterpreter_pmexpression = mathinterpreter_pmexpression;
    }
    public mathinterpreter_DefineExpr getMathinterpreter_defineexpr() {
        return mathinterpreter_defineexpr;
    }

    public void setMathinterpreter_defineexpr(mathinterpreter_DefineExpr mathinterpreter_defineexpr) {
        this.mathinterpreter_defineexpr = mathinterpreter_defineexpr;
    }

}