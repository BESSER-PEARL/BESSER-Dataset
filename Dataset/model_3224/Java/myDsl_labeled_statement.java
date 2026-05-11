





import java.util.List;
import java.util.ArrayList;

public class myDsl_labeled_statement  {

    private String identifier;





    private myDsl_conditional_expression mydsl_conditional_expression;




    private myDsl_statement mydsl_statement;




    private myDsl_statement mydsl_statement;


    public myDsl_labeled_statement(
        String identifier    ) {
        this.identifier = identifier;
    }


    public String getIdentifier() {
        return identifier;
    }

    public void setIdentifier(String identifier) {
        this.identifier = identifier;
    }

    public myDsl_conditional_expression getMydsl_conditional_expression() {
        return mydsl_conditional_expression;
    }

    public void setMydsl_conditional_expression(myDsl_conditional_expression mydsl_conditional_expression) {
        this.mydsl_conditional_expression = mydsl_conditional_expression;
    }
    public myDsl_statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }
    public myDsl_statement getMydsl_statement() {
        return mydsl_statement;
    }

    public void setMydsl_statement(myDsl_statement mydsl_statement) {
        this.mydsl_statement = mydsl_statement;
    }

}