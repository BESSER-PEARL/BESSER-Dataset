





import java.util.List;
import java.util.ArrayList;

public class ansic_primary_expression  {

    private String identifier;





    private ansic_expression ansic_expression;




    private ansic_postfix_expression ansic_postfix_expression;




    private ansic_generic_selection ansic_generic_selection;




    private ansic_constant ansic_constant;


    public ansic_primary_expression(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public ansic_expression getAnsic_expression() {
        return ansic_expression;
    }

    public void setAnsic_expression(ansic_expression ansic_expression) {
        this.ansic_expression = ansic_expression;
    }
    public ansic_postfix_expression getAnsic_postfix_expression() {
        return ansic_postfix_expression;
    }

    public void setAnsic_postfix_expression(ansic_postfix_expression ansic_postfix_expression) {
        this.ansic_postfix_expression = ansic_postfix_expression;
    }
    public ansic_generic_selection getAnsic_generic_selection() {
        return ansic_generic_selection;
    }

    public void setAnsic_generic_selection(ansic_generic_selection ansic_generic_selection) {
        this.ansic_generic_selection = ansic_generic_selection;
    }
    public ansic_constant getAnsic_constant() {
        return ansic_constant;
    }

    public void setAnsic_constant(ansic_constant ansic_constant) {
        this.ansic_constant = ansic_constant;
    }

}