





import java.util.List;
import java.util.ArrayList;

public class Expression  {






    private mt_expressions_Parenthesis mt_expressions_parenthesis;




    private mt_expressions_Not mt_expressions_not;




    private mt_expressions_Operator mt_expressions_operator;


    public Expression(
    ) {
    }



    public mt_expressions_Parenthesis getMt_expressions_parenthesis() {
        return mt_expressions_parenthesis;
    }

    public void setMt_expressions_parenthesis(mt_expressions_Parenthesis mt_expressions_parenthesis) {
        this.mt_expressions_parenthesis = mt_expressions_parenthesis;
    }
    public mt_expressions_Not getMt_expressions_not() {
        return mt_expressions_not;
    }

    public void setMt_expressions_not(mt_expressions_Not mt_expressions_not) {
        this.mt_expressions_not = mt_expressions_not;
    }
    public mt_expressions_Operator getMt_expressions_operator() {
        return mt_expressions_operator;
    }

    public void setMt_expressions_operator(mt_expressions_Operator mt_expressions_operator) {
        this.mt_expressions_operator = mt_expressions_operator;
    }

}