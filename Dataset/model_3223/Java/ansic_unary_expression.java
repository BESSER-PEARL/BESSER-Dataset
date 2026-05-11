





import java.util.List;
import java.util.ArrayList;

public class ansic_unary_expression  {

    private String unary_operator;





    private ansic_assignment_expression ansic_assignment_expression;




    private ansic_unary_expression ansic_unary_expression;




    private ansic_type_name ansic_type_name;




    private ansic_postfix_expression ansic_postfix_expression;


    public ansic_unary_expression(
        String unary_operator    ) {
        this.unary_operator = unary_operator;
    }


    public String getUnary_operator() {
        return unary_operator;
    }

    public void setUnary_operator(String unary_operator) {
        this.unary_operator = unary_operator;
    }

    public ansic_assignment_expression getAnsic_assignment_expression() {
        return ansic_assignment_expression;
    }

    public void setAnsic_assignment_expression(ansic_assignment_expression ansic_assignment_expression) {
        this.ansic_assignment_expression = ansic_assignment_expression;
    }
    public ansic_unary_expression getAnsic_unary_expression() {
        return ansic_unary_expression;
    }

    public void setAnsic_unary_expression(ansic_unary_expression ansic_unary_expression) {
        this.ansic_unary_expression = ansic_unary_expression;
    }
    public ansic_type_name getAnsic_type_name() {
        return ansic_type_name;
    }

    public void setAnsic_type_name(ansic_type_name ansic_type_name) {
        this.ansic_type_name = ansic_type_name;
    }
    public ansic_postfix_expression getAnsic_postfix_expression() {
        return ansic_postfix_expression;
    }

    public void setAnsic_postfix_expression(ansic_postfix_expression ansic_postfix_expression) {
        this.ansic_postfix_expression = ansic_postfix_expression;
    }

}