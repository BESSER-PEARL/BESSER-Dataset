





import java.util.List;
import java.util.ArrayList;

public class myDsl_postfix_expression_complement  {

    private String identifier;





    private myDsl_expression mydsl_expression;


    public myDsl_postfix_expression_complement(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public myDsl_expression getMydsl_expression() {
        return mydsl_expression;
    }

    public void setMydsl_expression(myDsl_expression mydsl_expression) {
        this.mydsl_expression = mydsl_expression;
    }

}