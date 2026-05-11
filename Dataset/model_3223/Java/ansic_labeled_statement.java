





import java.util.List;
import java.util.ArrayList;

public class ansic_labeled_statement  {

    private String identifier;





    private ansic_statement ansic_statement;




    private ansic_statement ansic_statement;




    private ansic_conditional_expression ansic_conditional_expression;


    public ansic_labeled_statement(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public ansic_statement getAnsic_statement() {
        return ansic_statement;
    }

    public void setAnsic_statement(ansic_statement ansic_statement) {
        this.ansic_statement = ansic_statement;
    }
    public ansic_statement getAnsic_statement() {
        return ansic_statement;
    }

    public void setAnsic_statement(ansic_statement ansic_statement) {
        this.ansic_statement = ansic_statement;
    }
    public ansic_conditional_expression getAnsic_conditional_expression() {
        return ansic_conditional_expression;
    }

    public void setAnsic_conditional_expression(ansic_conditional_expression ansic_conditional_expression) {
        this.ansic_conditional_expression = ansic_conditional_expression;
    }

}