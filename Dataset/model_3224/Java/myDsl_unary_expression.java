





import java.util.List;
import java.util.ArrayList;

public class myDsl_unary_expression  {

    private String unary_operator;





    private myDsl_postfix_expression mydsl_postfix_expression;




    private myDsl_unary_expression mydsl_unary_expression;


    public myDsl_unary_expression(
        String unary_operator    ) {
        this.unary_operator = unary_operator;
    }


    public String getUnary_operator() {
        return unary_operator;
    }

    public void setUnary_operator(String unary_operator) {
        this.unary_operator = unary_operator;
    }

    public myDsl_postfix_expression getMydsl_postfix_expression() {
        return mydsl_postfix_expression;
    }

    public void setMydsl_postfix_expression(myDsl_postfix_expression mydsl_postfix_expression) {
        this.mydsl_postfix_expression = mydsl_postfix_expression;
    }
    public myDsl_unary_expression getMydsl_unary_expression() {
        return mydsl_unary_expression;
    }

    public void setMydsl_unary_expression(myDsl_unary_expression mydsl_unary_expression) {
        this.mydsl_unary_expression = mydsl_unary_expression;
    }

}