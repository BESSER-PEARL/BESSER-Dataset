





import java.util.List;
import java.util.ArrayList;

public class ansic_postfix_expression_complement  {

    private String identifier;





    private ansic_expression ansic_expression;


    public ansic_postfix_expression_complement(
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

}