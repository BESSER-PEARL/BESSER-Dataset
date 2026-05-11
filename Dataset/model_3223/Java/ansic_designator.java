





import java.util.List;
import java.util.ArrayList;

public class ansic_designator  {

    private String identifier;





    private ansic_conditional_expression ansic_conditional_expression;




    private ansic_designator_list ansic_designator_list;


    public ansic_designator(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public ansic_conditional_expression getAnsic_conditional_expression() {
        return ansic_conditional_expression;
    }

    public void setAnsic_conditional_expression(ansic_conditional_expression ansic_conditional_expression) {
        this.ansic_conditional_expression = ansic_conditional_expression;
    }
    public ansic_designator_list getAnsic_designator_list() {
        return ansic_designator_list;
    }

    public void setAnsic_designator_list(ansic_designator_list ansic_designator_list) {
        this.ansic_designator_list = ansic_designator_list;
    }

}