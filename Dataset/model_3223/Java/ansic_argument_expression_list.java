





import java.util.List;
import java.util.ArrayList;

public class ansic_argument_expression_list  {






    private List<ansic_assignment_expression> ansic_assignment_expressions;




    private ansic_postfix_expression_complement ansic_postfix_expression_complement;


    public ansic_argument_expression_list(
    ) {
        this.ansic_assignment_expressions = new ArrayList<>();
    }

    public ansic_argument_expression_list(
        ArrayList<ansic_assignment_expression> ansic_assignment_expressions    ) {
        this.ansic_assignment_expressions = ansic_assignment_expressions;
    }


    public List<ansic_assignment_expression> getAnsic_assignment_expressions() {
        return ansic_assignment_expressions;
    }

    public void addAnsic_assignment_expression(Ansic_assignment_expression ansic_assignment_expression) {
        this.ansic_assignment_expressions.add(ansic_assignment_expression);
    }
    public ansic_postfix_expression_complement getAnsic_postfix_expression_complement() {
        return ansic_postfix_expression_complement;
    }

    public void setAnsic_postfix_expression_complement(ansic_postfix_expression_complement ansic_postfix_expression_complement) {
        this.ansic_postfix_expression_complement = ansic_postfix_expression_complement;
    }

}